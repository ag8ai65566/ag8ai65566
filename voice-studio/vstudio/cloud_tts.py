"""Long-form speech on a rented RunPod GPU: tens of thousands of words in one run, for about a dollar of GPU time.

One job ("cloud_tts") per run:
1. the text is split into lines (sentences, as on the performance page), each with its style and the pause after it;
2. the model checkpoint goes up once to vs/models/<model id>/<checkpoint>/ on the network volume, before any GPU is
   rented (a 9.5 GB full fine-tune takes about an hour at home upload speeds and costs only storage), and is reused;
3. this run's bundle (lines, reference clip, settings) and the pod scripts go to vs/jobs/<run id>/;
4. the chosen card is rented; bootstrap.sh checks the engine (installed by training) and synth_entry.py writes one
   audio/<i>.wav per line;
5. lines are downloaded while the pod works; when result.json is there the studio removes the pod itself (a pod's
   own removal is not relied on), fetches the rest and writes one WAV piece by piece (two hours of speech would not
   fit in memory as one array), with a sheet of where every line starts;
6. the run folder on the volume is deleted; the model stays there for the next run.

A run that is stopped, fails or is interrupted keeps its lines on the volume and here; "continue" makes only the
missing ones. Lines the pod could not make are silence, listed on the sheet.
"""
from __future__ import annotations

import io
import json
import re
import shutil
import tarfile
import threading
import time
from pathlib import Path

import numpy as np

from . import audio, config, datasets, db, engines, jobs, perform, tags, tts
from .cloud import runpod

ACTIVE = ("queued", "uploading_model", "uploading", "starting", "running", "downloading")
ENGINES = ("voxcpm2", "mock")
MIN_VRAM_GB = 16        # VoxCPM2 needs ~8 GB to speak; any card with 16 GB or more has room
OVERHEAD_MIN = 10.0     # boot, engine check and model load on the pod
# VoxCPM2's README gives about 0.3 s of compute per second of speech on an RTX 4090; the pod runs it without
# torch.compile (optimize=False, as at home), so the estimate starts from a more careful 0.5. The first run on a card
# measures the real figure, and later estimates use that.
BASE_RTF = 0.5
REF_SPEED = 0.65        # the RTX 4090 in runpod.GPU_SPEED
UNKNOWN_SPEED = 0.4     # a card missing from runpod.GPU_SPEED: assume it is slower than a 4090
WORDS_PER_S = 2.5       # English narration, 150 words a minute
CHARS_PER_S = 7.0       # Japanese / Chinese
POLL_S = 15
SR_OUT = 48000
MARKER = ".voice-studio.json"


def _set(rid: str, **kw) -> None:
    db.update("cloud_renders", rid, kw)


# --- what a run will say, and roughly cost ---------------------------------------------------------------------------

def lines_of(text: str, eng, lang: str) -> list[dict]:
    """The pieces to speak, in order, each with its text (pronunciation dictionary applied), the text as shown, its
    style and the silence after it. A sentence is one piece unless a [pause] or a change of style ([whispers] halfway)
    splits it; a [pause] before any words of a sentence lengthens the silence before it."""
    out: list[dict] = []
    cur: dict | None = None

    def flush(pause: float) -> None:
        nonlocal cur
        if cur:
            out.append({"i": len(out), "text": tts.apply_lexicon(" ".join(cur["text"]), lang),
                        "shown": tags.strip(" ".join(cur["text"])).strip(), "style": cur["style"], "pause": 0.0})
            cur = None
        if out:
            out[-1]["pause"] = round(out[-1]["pause"] + pause, 2)

    for ln in perform.split_text(text):
        for part in tts.compose(ln["text"], [], "", None, keep_tags=eng.supports_tags):
            if part["kind"] == "pause":
                flush(float(part.get("seconds") or 0))
            elif part["kind"] == "tts" and part["text"].strip():
                style = part.get("style") or ""
                if cur and cur["style"] != style:
                    flush(0.0)
                cur = cur or {"text": [], "style": style}
                cur["text"].append(part["text"].strip())
        flush(ln["pause"])
    return out


def speech_seconds(lines: list[dict], lang: str) -> float:
    """About how long the lines take to say (narration pace), pauses included."""
    total = 0.0
    for ln in lines:
        t = ln["shown"]
        total += (len(t) / CHARS_PER_S if lang in ("ja", "zh") else len(re.findall(r"[\w']+", t)) / WORDS_PER_S)
        total += ln["pause"]
    return total


def rtf(gpu: str, engine: str = "voxcpm2") -> float:
    """Seconds of compute per second of speech on this card: measured on an earlier run, else the RTX 4090 figure
    scaled by the square root of the card's training speed (speaking one token after another gains much less from a
    bigger card than training does)."""
    seen = (config.load_settings().get("tts_rtf") or {}).get(f"{engine}:{gpu}")
    if seen:
        return float(seen)
    return BASE_RTF * (REF_SPEED / runpod.GPU_SPEED.get(gpu, UNKNOWN_SPEED)) ** 0.5


def cost(speech_s: float, gpu: str, usd_h: float | None, engine: str = "voxcpm2") -> tuple[float, float]:
    """Minutes the pod runs and what that costs, for this much speech on this card."""
    minutes = OVERHEAD_MIN + speech_s * rtf(gpu, engine) / 60
    return minutes, minutes / 60 * (usd_h or 0)


def gpu_offers(datacenter: str | None, speech_s: float, engine: str = "voxcpm2") -> dict:
    """Cards with room for the model in the volume's datacenter, with what this run would take and cost on each:
    in stock first, then by cost. The default is the cheapest run among the cards in stock (a cheap slow card can
    cost more in the end than a dearer fast one)."""
    cat = runpod.gpu_catalog(datacenter)
    offers = []
    for g in cat["gpus"]:
        if (g.get("vram") or MIN_VRAM_GB) < MIN_VRAM_GB or not g.get("usd_h"):
            continue
        minutes, usd = cost(speech_s, g["id"], g["usd_h"], engine)
        offers.append({"id": g["id"], "label": g.get("label") or g["id"].replace("NVIDIA ", ""), "vram": g.get("vram"),
                       "usd_h": g["usd_h"], "availability": g.get("availability"), "rtf": round(rtf(g["id"], engine), 2),
                       "measured": bool((config.load_settings().get("tts_rtf") or {}).get(f"{engine}:{g['id']}")),
                       "minutes": round(minutes), "usd": round(usd, 2),
                       "in_stock": (not cat["live"]) or g.get("availability") in runpod.IN_STOCK})
    offers.sort(key=lambda o: (not o["in_stock"], o["usd"], o["minutes"]))
    rentable = [o["id"] for o in offers if o["in_stock"]]
    return {"live": cat["live"], "error": cat["error"], "offers": offers, "default": rentable[0] if rentable else None}


def model_spec(m: dict, eng) -> dict:
    """What the pod needs of a model: its kind (a LoRA adapter on the base weights, a full fine-tune, or the base
    model with a reference clip), the checkpoint folder here and its place on the volume, and its files."""
    spec = {"kind": "base", "local": None, "prefix": None, "files": [], "bytes": 0, "base": None, "base_revision": None}
    if eng.id == "mock":
        return spec
    from .engines.voxcpm2 import BASE
    emeta = eng.model_meta(Path(m["path"]))
    ck = eng.checkpoint_dir(Path(m["path"]), emeta, (m["meta"] or {}).get("checkpoint"))
    spec.update(base=emeta.get("base") or BASE, base_revision=emeta.get("base_revision") or None)
    if emeta.get("mode") in ("lora", "full") and ck and ck.exists():
        files = sorted(f for f in ck.rglob("*") if f.is_file())
        spec.update(kind=emeta["mode"], local=ck, prefix=f"vs/models/{m['id']}/{ck.name}",
                    files=[(f.relative_to(ck).as_posix(), f.stat().st_size) for f in files])
        spec["bytes"] = sum(s for _, s in spec["files"])
    return spec


def model_uploaded(spec: dict, loc: dict) -> bool:
    if not spec["files"]:
        return True
    mark = runpod.get_json(f"{spec['prefix']}/{MARKER}", loc, fast=True)
    return bool(mark) and mark.get("files") == {k: s for k, s in spec["files"]}


def plan(model_id: str, text: str, gpu: str | None = None, tts_mode: str = "plain", ref_id: str | None = None,
         language: str | None = None) -> dict:
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    eng = engines.get(m["engine"])
    if eng.id not in ENGINES:
        raise ValueError("長篇雲端合成目前只支援 VoxCPM2 的模型。")
    lang = language if language and language != "auto" else tts.detect_language(tags.strip(text))
    lines = lines_of(text, eng, lang)
    if not lines:
        raise ValueError("沒有要念的文字。")
    warnings = []
    if tts_mode in ("ref", "hifi") and not tts.reference(m, ref_id):
        raise ValueError("這個模式需要參考片段，請先在模型頁加入參考片段，或改用「只用模型」。")
    speech_s = speech_seconds(lines, lang)
    try:
        loc = runpod.location()
    except runpod.RunPodError as e:
        raise ValueError(f"{e}（設定 → 雲端 GPU）") from e
    offers = gpu_offers(loc.get("datacenter"), speech_s, eng.id)
    g = gpu or offers["default"]
    o = next((x for x in offers["offers"] if x["id"] == g), None)
    if not offers["live"]:
        warnings.append(f"讀不到 RunPod 的即時庫存（{offers['error'][:120]}），價格是內建清單，不確定有沒有貨。")
    elif o and not o["in_stock"]:
        warnings.append(f"{o['label']} 在你的網路磁碟所在的資料中心現在沒貨，請換一張有貨的卡。")
    usd_h = (o or {}).get("usd_h") or runpod.GPUS.get(g or "", {}).get("usd_h") or 1.5
    minutes, usd = cost(speech_s, g or "", usd_h, eng.id)
    hours = minutes / 60
    if o and not o["measured"]:
        warnings.append("時間和費用是估計值（還沒在這張卡上實際合成過）；跑完一次後會用實測速度估算。")
    spec = model_spec(m, eng)
    try:
        uploaded = model_uploaded(spec, loc)
    except Exception:  # the volume cannot be read now: assume the model still has to go up
        uploaded = False
    bps = float(config.load_settings().get("upload_bps") or 0)
    up_gb = 0.0 if uploaded else spec["bytes"] / 1e9
    if speech_s > 4 * 3600:
        warnings.append("超過 4 小時的語音，建議分成幾次合成（每次可以單獨重做）。")
    limit = float(config.load_settings().get("runpod_max_hours") or 12)
    return {"model": m["id"], "engine": eng.id, "language": lang, "lines": len(lines), "words": len(re.findall(r"[\w']+", text)),
            "speech_min": round(speech_s / 60, 1), "gpu": g, "gpus": offers["offers"], "live": offers["live"],
            "usd_per_hour": usd_h, "estimate_min": round(minutes), "estimate_usd": round(usd, 2), "max_hours": round(min(limit, hours * 2 + 0.5), 2),
            "model_upload_gb": round(up_gb, 2), "model_upload_bytes": 0 if uploaded else spec["bytes"],
            "model_upload_min": round(up_gb * 1e9 / bps / 60) if bps and up_gb else None, "warnings": warnings}


# --- starting, stopping, continuing ----------------------------------------------------------------------------------

def _consent(m: dict) -> None:
    voice = db.get("voices", m["voice_id"])
    if m["engine"] != "mock" and (not voice or not datasets.consent_ok(voice)):
        raise datasets.ConsentMissing("這個聲音目前沒有有效的同意紀錄（可能已撤回），不能合成。")


def start(model_id: str, text: str, gpu: str | None = None, tts_mode: str = "plain", ref_id: str | None = None,
          language: str | None = None, name: str = "") -> dict:
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    _consent(m)
    pl = plan(model_id, text, gpu, tts_mode, ref_id, language)
    if not pl["gpu"]:
        raise ValueError("RunPod 這個資料中心現在沒有適合的卡有貨，等一下再試（沒有租用任何東西）。")
    chosen = next((o for o in pl["gpus"] if o["id"] == pl["gpu"]), None)
    if pl["live"] and chosen and not chosen["in_stock"]:
        raise ValueError(f"{chosen['label']} 現在沒貨，請換一張有貨的卡（沒有租用任何東西）。")
    try:
        problem = runpod.check().get("problem")
    except Exception:
        problem = ""
    if problem:
        raise ValueError(problem + "還沒有上傳或租用任何東西。")
    rid = db.new_id("rd")
    db.insert("cloud_renders", {
        "id": rid, "model_id": model_id, "status": "queued", "storage": runpod.location(), "remote_prefix": f"vs/jobs/{rid}",
        "gpu": pl["gpu"], "cost_estimate": pl["estimate_usd"], "progress": {}, "created_at": db.now(),
        "params": {"text": text, "tts_mode": tts_mode, "ref_id": ref_id, "language": pl["language"], "name": name,
                   "lines": pl["lines"], "speech_min": pl["speech_min"], "max_hours": pl["max_hours"]}})
    job = jobs.submit("cloud_tts", {"render_id": rid}, "長篇雲端合成")
    _set(rid, job_id=job["id"])
    return db.get("cloud_renders", rid)


def resume(rid: str) -> dict:
    r = db.get("cloud_renders", rid)
    if not r:
        raise KeyError(rid)
    if r["status"] not in ("failed", "canceled"):
        raise ValueError("只有停下來的合成可以繼續。")
    m = db.get("models", r["model_id"])
    if not m:
        raise ValueError("這次合成用的模型已經刪掉了，不能繼續（已完成的句子在雲端和這裡都還留著，可以按「刪除」清掉）。")
    _consent(m)
    gpu, note = r.get("gpu"), ""
    try:  # the card it had may be gone now: the cheapest run on a card in stock instead
        offers = gpu_offers((r.get("storage") or {}).get("datacenter"), float((r["params"] or {}).get("speech_min") or 0) * 60,
                            m["engine"])
        mine = next((o for o in offers["offers"] if o["id"] == gpu), None)
        if offers["live"] and offers["default"] and not (mine and mine["in_stock"]):
            gpu = offers["default"]
            note = f"原本的卡現在沒貨，改租 {gpu.replace('NVIDIA ', '')}。"
    except Exception:
        pass
    job = jobs.submit("cloud_tts", {"render_id": rid}, "長篇雲端合成（繼續）")
    _set(rid, status="queued", job_id=job["id"], note=note, finished_at=None, pod_id=None, pod_state=None, gpu=gpu)
    return db.get("cloud_renders", rid)


def cancel(rid: str) -> dict:
    r = db.get("cloud_renders", rid)
    if not r:
        raise KeyError(rid)
    if r.get("job_id"):
        jobs.cancel(r["job_id"])
    if r.get("pod_id") and r.get("pod_state") == "running":
        _remove_pod(rid, r["pod_id"])
    if r["status"] == "queued":
        _set(rid, status="canceled", finished_at=db.now())
    return db.get("cloud_renders", rid)


def delete(rid: str) -> dict:
    """The run's record, its folder on the volume and its lines here. The finished speech stays among the outputs."""
    r = db.get("cloud_renders", rid)
    if not r:
        raise KeyError(rid)
    if r["status"] in ACTIVE:
        raise ValueError("這次合成還在進行，先按「停止」。")
    if r.get("pod_state") in ("remove_failed", "creating"):
        raise ValueError("這次合成的雲端機器還沒確認關掉，等一下再刪，或先到 runpod.io → Pods 手動刪除。")
    try:
        runpod.delete_run_folder(r["remote_prefix"], r.get("storage") or None)
    except Exception as e:
        raise RuntimeError(f"雲端的檔案沒刪到（{str(e)[:160]}），紀錄先留著，可以再按一次。") from e
    shutil.rmtree(config.DATA / "jobs" / rid, ignore_errors=True)
    db.delete("cloud_renders", rid)
    return {"ok": True}


def _remove_pod(rid: str, pod_id: str | None) -> bool:
    if not pod_id:
        return True
    try:
        runpod.remove_pod(pod_id)
        _set(rid, pod_state="removed")
        return True
    except Exception as e:
        _set(rid, pod_state="remove_failed", note=f"雲端機器刪除失敗：{str(e)[:200]}。請到 runpod.io → Pods 確認。")
        return False


def resume_interrupted() -> None:
    """At start-up: a run whose job died with the app loses its pod (nothing watches it, and it would keep billing);
    the lines made so far stay, and "continue" makes the rest."""
    for r in db.query(f"SELECT * FROM cloud_renders WHERE status IN ({','.join('?' * len(ACTIVE))})", ACTIVE):
        j = db.get("jobs", r["job_id"]) if r.get("job_id") else None
        if j and j["status"] in ("queued", "running"):
            continue
        _remove_pod(r["id"], r.get("pod_id"))
        _set(r["id"], status="failed", finished_at=db.now(),
             note="程式關閉時中斷了，雲端機器已關閉。按「繼續」會從沒做完的句子接著合成，已完成的都保留。")


# --- the run itself -----------------------------------------------------------------------------------------------

@jobs.handler("cloud_tts", queue="io")
def cloud_tts(ctx: jobs.JobContext) -> dict:
    rid = ctx.params["render_id"]
    r = db.get("cloud_renders", rid)
    if not r or r.get("job_id") != ctx.id:  # "retry" on the jobs page: the run would not know this job (no stop)
        raise RuntimeError("這是之前的工作。請到「文字轉語音 → 整篇交給雲端 GPU」，按那次合成的「繼續」。")
    try:
        return _run(ctx, rid)
    except BaseException as e:
        r = db.get("cloud_renders", rid)
        if r and r.get("pod_id") and r.get("pod_state") in ("running", "creating"):
            _remove_pod(rid, r["pod_id"])
        if r and r["status"] in ACTIVE:
            done = len(list((config.DATA / "jobs" / rid / "audio").glob("*.wav")))
            why = "已停止。" if isinstance(e, jobs.Cancelled) else f"{str(e)[:300] or type(e).__name__}　"
            _set(rid, status="canceled" if isinstance(e, jobs.Cancelled) else "failed", finished_at=db.now(),
                 note=f"{why}已完成 {done} / {(r['params'] or {}).get('lines', '?')} 句，都保留著；按「繼續」會接著合成。")
        raise


def _ensure_model(ctx: jobs.JobContext, rid: str, m: dict, spec: dict, loc: dict) -> None:
    """The checkpoint on the volume, once: files already there with the same size are not sent again; a marker with
    every file's size, written last, says the copy is whole. The model remembers where its copy is, so deleting the
    model deletes the copy too."""
    if model_uploaded(spec, loc):
        return
    _set(rid, status="uploading_model")
    meta = dict((db.get("models", m["id"]) or m)["meta"] or {})  # recorded first: a half-sent copy is deleted too
    db.update("models", m["id"], {"meta": {**meta, "cloud_copy": {"prefix": f"vs/models/{m['id']}", "loc": loc}}})
    total, sent, moved, t0 = spec["bytes"] or 1, 0, 0, time.time()
    for rel, size in spec["files"]:
        key = f"{spec['prefix']}/{rel}"
        try:
            there = runpod.size(key, loc) == size
        except Exception:
            there = False
        if not there:
            base = sent
            _upload(ctx, spec["local"] / rel, key, loc, lambda f, quiet, base=base, size=size: ctx.progress(
                0.02 + 0.2 * (base + f * size) / total,
                f"把模型傳到雲端（只有第一次要傳，還沒租 GPU）：{(base + f * size) / 1e9:.1f} / {total / 1e9:.1f} GB"
                + (f"，已經 {int(quiet) // 60} 分 {int(quiet) % 60:02d} 秒沒有進度，持續重試中" if quiet >= 60 else "")))
            moved += size
        sent += size
        ctx.check()
    runpod.put_text(f"{spec['prefix']}/{MARKER}", json.dumps({"files": {k: s for k, s in spec["files"]}}), loc=loc)
    if moved >= 50 << 20:  # remembered for the estimates (as a training's upload is)
        config.save_settings({"upload_bps": round(moved / max(1.0, time.time() - t0))})


UPLOAD_TICK_S = 1.0


def _upload(ctx: jobs.JobContext, local: Path, key: str, loc: dict, report) -> None:
    """One file up, in a thread of its own while this one looks for a stop request every second (an upload RunPod
    stops answering must still be stoppable); report(fraction, seconds without progress) every tick."""
    stop, state, done = threading.Event(), {"f": 0.0, "moved": time.time()}, {}

    def progress(f: float) -> None:  # the upload's own threads: no database work here
        if stop.is_set():
            raise jobs.Cancelled()
        if f > state["f"]:
            state.update(f=f, moved=time.time())

    def run() -> None:
        try:
            runpod.upload(local, key, progress=progress, loc=loc)
        except BaseException as e:  # handed to the job's thread below
            done["error"] = e
    worker = threading.Thread(target=run, name=f"up-{key[-40:]}", daemon=True)
    worker.start()
    try:
        while worker.is_alive():
            worker.join(UPLOAD_TICK_S)
            ctx.check()
            report(state["f"], time.time() - state["moved"])
    finally:
        stop.set()
    if "error" in done:
        raise done["error"]


def _bundle(work: Path, lines: list[dict], ref: dict | None, seed: int) -> Path:
    tar_path = work / "dataset.tar"
    with tarfile.open(tar_path, "w") as t:
        rows = "".join(json.dumps({"i": ln["i"], "text": ln["text"], "style": ln["style"], "seed": seed + ln["i"]},
                                  ensure_ascii=False) + "\n" for ln in lines).encode("utf-8")
        info = tarfile.TarInfo("data/chunks.jsonl")
        info.size = len(rows)
        t.addfile(info, io.BytesIO(rows))
        if ref:
            t.add(str(ref["path"]), arcname="data/refs/ref.wav")
    return tar_path


def _run(ctx: jobs.JobContext, rid: str) -> dict:
    r = db.get("cloud_renders", rid)
    p = r["params"]
    m = db.get("models", r["model_id"])
    if not m:
        raise RuntimeError("模型已經刪掉了。")
    _consent(m)
    eng = engines.get(m["engine"])
    loc, prefix = r.get("storage") or runpod.location(), r["remote_prefix"]
    work = config.DATA / "jobs" / rid
    (work / "audio").mkdir(parents=True, exist_ok=True)
    lines_f = work / "lines.json"  # fixed at the first try, so a continued run speaks exactly the same lines
    if lines_f.exists():
        lines = json.loads(lines_f.read_text(encoding="utf-8"))
    else:
        lines = lines_of(p["text"], eng, p["language"])
        lines_f.write_text(json.dumps(lines, ensure_ascii=False), encoding="utf-8")
    n = len(lines)

    def have() -> set[int]:
        return {int(f.stem) for f in (work / "audio").glob("*.wav")}

    if len(have()) < n:
        # 1. the model, once; 2. the bundle and scripts; 3. the pod
        ctx.progress(0.01, "確認雲端的模型…")
        spec = model_spec(m, eng)
        _ensure_model(ctx, rid, m, spec, loc)
        _set(rid, status="uploading")
        ctx.progress(0.22, "上傳這次要念的文字")
        ref = tts.reference(m, p.get("ref_id")) if p.get("tts_mode") in ("ref", "hifi") else None
        seed = int(p.get("seed") or 1234)
        tar_path = _bundle(work, lines, ref, seed)
        _upload(ctx, tar_path, f"{prefix}/dataset.tar", loc, lambda f, quiet: None)
        tar_path.unlink(missing_ok=True)
        from .engines import remote
        from .training import BOOTSTRAP
        params = {"engine": eng.id, "kind": spec["kind"], "base": spec["base"], "base_revision": spec["base_revision"],
                  "model_dir": f"/workspace/{spec['prefix']}" if spec["prefix"] else None,
                  "tts_mode": p.get("tts_mode") or "plain", "cfg": 2.0, "timesteps": 10,
                  "reference": {"audio": "refs/ref.wav", "text": ref.get("text") or ""} if ref else None}
        runpod.put_text(f"{prefix}/config.json", json.dumps({"training_id": rid, "params": params}, ensure_ascii=False),
                        loc=loc)
        runpod.put_text(f"{prefix}/bootstrap.sh", BOOTSTRAP, loc=loc)
        for fname, body in eng.cloud_files().items():
            if fname != "train_entry.py":
                runpod.put_text(f"{prefix}/{fname}", body, loc=loc)
        runpod.put_text(f"{prefix}/train_entry.py", remote.read("synth_entry.py"), loc=loc)
        for stale in ("done.json", "error.json", "result.json", "progress.json"):  # from an earlier try
            runpod.delete(f"{prefix}/{stale}", loc)
        ctx.check()

        gpu = r["gpu"]
        max_s = int(float(p.get("max_hours") or 2) * 3600)
        env = {"VS_TRAINING_ID": rid, "VS_ENGINE": eng.id, "VS_MAX_SECONDS": str(max_s), "VS_IMAGE": eng.image}
        hf = config.get_secret("hf_token")
        if hf:
            env["HF_TOKEN"] = hf
        _set(rid, status="starting", pod_state="creating", deadline=time.time() + max_s + 900, started_at=time.time())
        ctx.progress(0.24, f"租用 {gpu.replace('NVIDIA ', '')}…")
        try:
            pod = runpod.create_pod(f"voice-studio-{rid}", eng.image, [gpu], env,
                                    ["bash", "-c", f"bash /workspace/{prefix}/bootstrap.sh"], loc,
                                    container_disk_gb=40, min_ram_gb=24, min_vcpu=4)
        except Exception as e:
            time.sleep(10)
            try:  # the request may have gone through even though we saw an error
                for pd in runpod.list_pods(name=f"voice-studio-{rid}", volume=loc.get("volume")):
                    runpod.remove_pod(pd.get("id"))
            except Exception:
                pass
            _set(rid, pod_state=None)
            raise RuntimeError(f"沒有租到 {gpu.replace('NVIDIA ', '')}：{str(e)[:200]}（這張卡剛好被租走了。按「繼續」會再試，"
                               "那時沒貨就自動換成最便宜的有貨的卡；模型和文字已經在雲端，不用重傳）") from e
        pod_id = pod.get("id")
        rate = pod.get("costPerHr") or pod.get("adjustedCostPerHr")
        _set(rid, status="running", pod_id=pod_id, pod_state="running", cost_per_hr=rate)
        ctx.log(f"pod {pod_id} on {gpu} at {rate} /h")
        deadline = time.time() + max_s + 900
        misses = 0
        try:
            while True:
                ctx.check()
                for _ in range(POLL_S):
                    time.sleep(1)
                    ctx.check()
                if time.time() > deadline:
                    raise RuntimeError("超過這次設定的最長時數，已關閉雲端機器。按「繼續」會接著合成。")
                try:
                    prog = runpod.get_json(f"{prefix}/progress.json", loc, fast=True) or {}
                    done = runpod.get_json(f"{prefix}/done.json", loc, fast=True)
                    err = runpod.get_json(f"{prefix}/error.json", loc, fast=True)
                    misses = 0
                except Exception as e:
                    misses += 1
                    ctx.log(f"status read failed ({misses}): {e}")
                    if misses >= 40:
                        raise RuntimeError("連續 10 分鐘讀不到雲端的進度，已關閉雲端機器。按「繼續」會接著合成。") from e
                    continue
                _fetch(work, prefix, loc, min(n, int(prog.get("done") or 0)), have(), ctx.check)
                _report(ctx, rid, prog, n, len(have()))
                if done:
                    break
                if err:
                    raise RuntimeError(f"雲端合成出錯（{STAGES.get(err.get('stage'), err.get('stage', '?'))}），按「紀錄」看原因。")
                try:
                    gone = runpod.get_pod(pod_id) is None
                except Exception:
                    gone = False
                if gone:
                    raise RuntimeError("雲端機器意外消失（可能被 RunPod 收回）。按「繼續」會接著合成，已完成的都保留。")
        finally:
            _remove_pod(rid, pod_id)

    # 4. the rest of the lines, then one file
    _set(rid, status="downloading")
    ctx.progress(0.9, "下載剩下的句子")
    _fetch(work, prefix, loc, n, have(), ctx.check)
    missing = sorted(set(range(n)) - have())
    if missing:
        raise RuntimeError(f"還有 {len(missing)} 句沒拿到（例如第 {missing[0] + 1} 句）。按「繼續」會補做。")
    try:
        result = runpod.get_json(f"{prefix}/result.json", loc) or {}
    except Exception:
        result = {}
    ctx.progress(0.95, "接成一個音檔")
    out = _stitch(rid, m, lines, work, result.get("failed") or [])
    if float(result.get("audio_s") or 0) > 0 and float(result.get("synth_s") or 0) > 0 and r.get("gpu"):
        speed = dict(config.load_settings().get("tts_rtf") or {})  # measured: better estimates next time
        speed[f"{eng.id}:{r['gpu']}"] = round(float(result["synth_s"]) / float(result["audio_s"]), 4)
        config.save_settings({"tts_rtf": speed})
    try:
        runpod.delete_run_folder(prefix, loc)
    except Exception as e:  # leftovers are listed by the record and deleted with it
        ctx.log(f"run folder clean-up failed: {e}")
    shutil.rmtree(work / "audio", ignore_errors=True)
    _set(rid, status="done", finished_at=db.now(), output_id=out["id"],
         note=f"{len(result.get('failed') or [])} 句沒有合成成功，用靜音代替（見清單）。" if result.get("failed") else "")
    return {"output_id": out["id"], "message": f"完成：{n} 句，{out['duration'] / 60:.1f} 分鐘"}


STAGES = {"setup": "安裝環境", "unpack": "解開文字", "train": "合成", "timeout": "超過時數"}


def log_tail(rid: str) -> str:
    r = db.get("cloud_renders", rid)
    if not r:
        raise KeyError(rid)
    text = runpod.get_text(f"{r['remote_prefix']}/train.log", loc=r.get("storage") or None)
    return text or "（雲端沒有紀錄：機器還沒開始，或這次合成的雲端檔案已經清掉了）"


def _fetch(work: Path, prefix: str, loc: dict, upto: int, have: set[int], check=None) -> None:
    """Lines 0 … upto-1 not here yet (the pod writes them in order, each whole before it gets its name)."""
    for i in range(upto):
        if i in have:
            continue
        if check:
            check()
        try:
            blob = runpod.get_bytes(f"{prefix}/audio/{i:05d}.wav", loc)
        except Exception:
            continue  # the next poll tries again
        tmp = work / "audio" / f"{i:05d}.part"
        tmp.write_bytes(blob)
        tmp.replace(work / "audio" / f"{i:05d}.wav")


def _report(ctx: jobs.JobContext, rid: str, prog: dict, n: int, got: int) -> None:
    done, phase = int(prog.get("done") or 0), prog.get("phase") or ""
    if phase == "synth":
        speech = float(prog.get("audio_s") or 0) / 60
        msg = f"在雲端合成：{done} / {n} 句（約 {speech:.0f} 分鐘語音），已下載 {got} 句"
    elif phase == "load":
        msg = "雲端機器已開機，載入模型中…"
    else:
        msg = "雲端機器開機、準備環境中…"
    _set(rid, progress={**prog, "downloaded": got})
    ctx.progress(0.25 + 0.65 * (done / max(1, n)), msg)


def _stitch(rid: str, m: dict, lines: list[dict], work: Path, failed: list[int]) -> dict:
    """One WAV, written line by line with the pauses (never all in memory), and its sheet."""
    import soundfile as sf
    oid = db.new_id("out")
    path = config.DATA / "outputs" / f"{oid}.wav"
    path.parent.mkdir(parents=True, exist_ok=True)
    sheet, t = [], 0.0
    with sf.SoundFile(str(path), "w", samplerate=SR_OUT, channels=1, subtype="PCM_16", format="WAV") as f:
        f.comment = audio.tag_synthetic({"model": m["id"], "voice": m["voice_id"], "render": rid})
        f.software = "Voice Studio (AI-generated speech)"
        for ln in lines:
            y, _ = audio.load(work / "audio" / f"{ln['i']:05d}.wav", SR_OUT)
            f.write(np.clip(y, -1, 1))
            sheet.append({"line": ln["i"] + 1, "text": ln["shown"], "start": round(t, 2), "duration": round(len(y) / SR_OUT, 2),
                          "failed": ln["i"] in failed})
            t += len(y) / SR_OUT
            if ln["pause"] > 0:
                f.write(np.zeros(int(SR_OUT * ln["pause"]), dtype=np.float32))
                t += ln["pause"]
    path.with_suffix(".json").write_text(json.dumps(sheet, ensure_ascii=False, indent=1), encoding="utf-8")
    r = db.get("cloud_renders", rid)
    p = r["params"]
    return db.insert("outputs", {
        "id": oid, "model_id": m["id"], "text": p["text"][:2000], "path": str(path), "duration": round(t, 2),
        "params": {"cloud": True, "render": rid, "lines": len(lines), "engine": m["engine"], "mode": p.get("tts_mode"),
                   "gpu": r.get("gpu"), "failed": failed, "language": p.get("language")},
        "score": {"best": True, "lines": len(lines)}, "batch": rid, "created_at": db.now()})

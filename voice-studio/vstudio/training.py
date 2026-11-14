"""Training runs: cloud fine-tuning (RunPod, or Google Colab through a synced Drive folder), the model registry and
zero-shot (no training) models."""
from __future__ import annotations

import json
import os
import shutil
import tarfile
import threading
import time
from pathlib import Path

from . import config, datasets, db, emotions, engines, evaluate, jobs  # noqa: F401  (evaluate registers evaluate_model)
from .cloud import colab, runpod

BOOTSTRAP = (Path(__file__).parent / "cloud" / "bootstrap" / "bootstrap.sh").read_text(encoding="utf-8")


def _speed_key(engine_id: str, preset_id: str, gpu: str) -> str:
    return f"{engine_id}:{preset_id}:{gpu}"


def _speed(engine_id: str, preset_id: str, gpu: str) -> tuple[float | None, str, str]:
    """Seconds per training step on this card, and where the number comes from:
    - "measured": an earlier run of this training method on this card;
    - "scaled": the latest run on another card, scaled by the two cards' relative speed (that card is returned);
    - "guess": the training method's first guess, scaled from the card it is listed first for.
    None (the engine's own guess) when the card's relative speed is unknown, e.g. for Colab."""
    speed = config.load_settings().get("speed") or {}
    own = (speed.get(_speed_key(engine_id, preset_id, gpu)) or {}).get("s_per_step")
    if own:
        return float(own), "measured", gpu
    rel = runpod.GPU_SPEED.get(gpu)
    if not rel:
        return None, "guess", ""
    prefix = _speed_key(engine_id, preset_id, "")
    others = sorted(((v.get("at") or 0, k[len(prefix):], float(v["s_per_step"])) for k, v in speed.items()
                     if k.startswith(prefix) and (v or {}).get("s_per_step") and k[len(prefix):] in runpod.GPU_SPEED),
                    reverse=True)
    if others:
        _, other, sps = others[0]
        return sps * runpod.GPU_SPEED[other] / rel, "scaled", other
    p = engines.get(engine_id).preset(preset_id)
    first = p.gpu[0] if p.gpu else ""
    if p.s_per_step and first in runpod.GPU_SPEED:
        return p.s_per_step * runpod.GPU_SPEED[first] / rel, "guess", first
    return None, "guess", ""


def _require_consent(voice_id: str) -> None:
    """Consent is re-checked at every step that uses the voice: building, uploading, renting, synthesizing."""
    voice = db.get("voices", voice_id)
    if not voice or not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音目前沒有有效的同意紀錄（可能已撤回），已停止。")


def plan(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, usd_h: float | None = None,
         params: dict | None = None, target: str = "runpod") -> dict:
    """What a run will use and roughly cost, shown before the user confirms. The parameters returned here are the
    exact ones that start() stores and the pod receives."""
    ds = db.get("datasets", dataset_id)
    if not ds:
        raise KeyError(dataset_id)
    eng = engines.get(engine_id)
    p = eng.preset(preset_id)
    if target == "colab":  # paid for by the Google AI plan's compute units; speed is measured under "Colab"
        gpu, usd_h = "Colab", 0.0
    else:
        gpu = gpu or p.gpu[0]
        usd_h = usd_h or runpod.GPUS.get(gpu, {}).get("usd_h", 1.5)
    st = config.load_settings()
    n_train = int(ds["meta"].get("n_train") or ds["n_items"])
    warnings, blocked = [], None
    try:
        eff = eng.effective_params(p.id, params, n_train)
    except ValueError as e:
        eff, blocked = {**p.params, **(params or {})}, str(e)
    sps, basis, basis_gpu = _speed(eng.id, p.id, gpu)
    est = eng.estimate(ds["hours"], p.id, usd_h, n_train=n_train, s_per_step=sps, params=eff)
    if est["steps"] and sps:
        est["basis"] = basis
    upload = None
    if target == "runpod":  # the dataset goes up after the GPU is rented, so the upload is billed time too
        nbytes, bps = _dataset_bytes(ds), float(st.get("upload_bps") or 0)
        if nbytes:
            upload = {"gb": round(nbytes / 1e9, 2), "minutes": round(nbytes / bps / 60, 1) if bps else None}
            if bps:
                est["hours"] = round(est["hours"] + nbytes / bps / 3600, 2)
                est["usd"] = round(est["hours"] * usd_h, 2)
    limit = float(st.get("runpod_max_hours") or 12)
    if target == "colab":
        limit = min(limit, 11.5)  # a Colab session ends after at most about 12 hours
    if ds["hours"] < p.min_hours:
        warnings.append(f"這個設定建議至少 {p.min_hours:g} 小時已核可語音，目前只有 {ds['hours']:.2f} 小時。")
    if (eff.get("epochs_effective") or 0) > 3:
        warnings.append(f"實際會跑約 {eff['epochs_effective']} 個 epoch，資料少時容易「背答案」。")
    if est["hours"] > limit:
        warnings.append(f"預估時間超過你設定的上限 {limit:g} 小時，訓練會在上限時被強制停止。請到設定調高上限。")
    if not ds["meta"].get("reference_items") and not ds["meta"].get("reference"):
        warnings.append("資料集沒有 5–12 秒的參考片段，樣本比較會比較不準。")
    units = None
    if target == "colab":
        units = colab.estimate_units(est["hours"])
        need = colab.MIN_VRAM_GB.get((eng.id, p.id), 24)
        if need >= 40:
            warnings.append(f"這個訓練方式需要 {need} GB 以上的顯示記憶體，Colab 不一定分得到；分不到時筆記本會請你換 GPU。")
        if p.disk_gb >= 200:
            warnings.append("完整微調的檢查點每個約 8 GB，要經過雲端硬碟同步回來會很久，建議用 RunPod。")
    return {"engine": eng.id, "preset": p.id, "gpu": gpu, "usd_per_hour": usd_h, "data_hours": ds["hours"],
            "target": target, "compute_units": units, "upload": upload,
            "n_train": n_train, "steps": est["steps"], "epochs_effective": eff.get("epochs_effective"),
            "estimate_hours": est["hours"], "estimate_usd": est["usd"], "estimate_basis": est["basis"],
            "estimate_from": runpod.GPUS.get(basis_gpu, {}).get("label") or basis_gpu.replace("NVIDIA ", "")
            if est["basis"] == "scaled" else None, "s_per_step": round(sps, 2) if sps else None,
            "max_hours": limit, "max_usd": round(limit * usd_h, 2), "disk_gb": p.disk_gb, "ram_gb": p.ram_gb,
            "params": eff, "warnings": warnings, "blocked": blocked}


def gpu_offers(engine_id: str, preset_id: str, catalog: dict | None = None) -> dict:
    """The GPUs a RunPod run of this training method can rent, with the live stock in the volume's datacenter.

    The preset's own cards are offered (recommended); so is any other card the engine or the price table knows with at
    least as much memory as the smallest recommended one, so a datacenter without the recommended cards can still
    train on a bigger card. With live stock, cards that can be rented now come first, recommended then cheapest."""
    eng = engines.get(engine_id)
    p = eng.preset(preset_id)
    cat = catalog or runpod.gpu_catalog(config.load_settings().get("runpod_datacenter") or None)
    live = {g["id"]: g for g in cat["gpus"]}

    def offer(gid: str) -> dict:
        g, static = live.get(gid) or {}, runpod.GPUS.get(gid, {})
        return {"id": gid, "label": g.get("label") or static.get("label") or gid.replace("NVIDIA ", ""),
                "vram": g.get("vram") or static.get("vram") or 0, "usd_h": g.get("usd_h") or static.get("usd_h"),
                "availability": (g.get("availability") or "NONE") if cat["live"] else None,
                "recommended": gid in p.gpu}
    own = [offer(g) for g in p.gpu]
    floor = min((o["vram"] for o in own if o["vram"]), default=0)
    others = dict.fromkeys([g for q in eng.presets for g in q.gpu] + list(runpod.GPUS))
    extra = [o for o in map(offer, others) if o["id"] not in p.gpu and floor and o["vram"] >= floor]
    offers = own + extra
    if cat["live"]:
        offers.sort(key=lambda o: (o["availability"] not in runpod.IN_STOCK, not o["recommended"],
                                   o["usd_h"] is None, o["usd_h"] or 0))
    rentable = [o["id"] for o in offers if o["availability"] in runpod.IN_STOCK]
    return {"live": cat["live"], "datacenter": cat["datacenter"], "error": cat["error"], "offers": offers,
            "default": (rentable[0] if rentable else None) if cat["live"] else p.gpu[0]}


def _stock_problem(engine_id: str, preset_id: str, gpu: str, datacenter: str) -> str | None:
    """Why this GPU cannot be rented for this training method in the datacenter right now; None when it can, or when
    the live stock cannot be read (then renting is simply tried, as before)."""
    res = gpu_offers(engine_id, preset_id, runpod.gpu_catalog(datacenter))
    o = next((x for x in res["offers"] if x["id"] == gpu), None)
    if o is None:
        return f"{gpu.replace('NVIDIA ', '')} 的顯示記憶體不夠這個訓練方式用，請換一張。"
    if not res["live"] or o["availability"] in runpod.IN_STOCK:
        return None
    alts = [f"{x['label']}（${x['usd_h']:.2f}/時）" if x["usd_h"] else x["label"]
            for x in res["offers"] if x["availability"] in runpod.IN_STOCK]
    return (f"{o['label']} 在 {datacenter} 現在沒貨。" +
            (f"現在有貨的：{'、'.join(alts)}。" if alts else
             "這個訓練方式能用的卡在這個資料中心都沒貨：晚點再試，或在 RunPod 其他資料中心建立網路磁碟後到設定改用它。"))


def start(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, name: str = "",
          params: dict | None = None, usd_h: float | None = None, target: str = "runpod",
          gpus: list[str] | None = None, wait_hours: float | None = None) -> dict:
    """gpus (RunPod only): auto-grab. The run waits, renting nothing, until a card of this list (in its order) is in
    stock in the volume's datacenter, for at most wait_hours; then it rents that card and continues as usual."""
    if gpus:
        gpu = gpus[0]
    ds = db.get("datasets", dataset_id)
    _require_consent(ds["voice_id"])
    voice = db.get("voices", ds["voice_id"])
    snapshot = {"kind": voice["kind"], "consent": ds["meta"].get("consent"), "consent_doc": ds["meta"].get("consent_doc")}
    if not datasets.consent_ok(snapshot):  # the dataset must have been built under a valid consent, too
        raise datasets.ConsentMissing("這個資料集建立時沒有完整的同意紀錄，請重新建立資料集。")
    pl = plan(dataset_id, engine_id, preset_id, gpu, usd_h, params, target)
    if pl["blocked"]:
        raise ValueError(pl["blocked"])
    if target == "colab":
        st = config.load_settings()
        try:
            colab.folder(st)
        except colab.ColabError as e:
            raise ValueError(str(e))
        tid = db.new_id("tr")
        db.insert("trainings", {"id": tid, "voice_id": ds["voice_id"], "dataset_id": dataset_id, "engine": engine_id,
                                "preset": {"id": pl["preset"], "params": pl["params"], "name": name},
                                "target": "colab", "status": "queued", "gpu": "Colab",
                                "storage": {"drive_root": st["colab_drive_root"], "folder": st.get("colab_folder")
                                            or "VoiceStudio"},
                                "remote_prefix": f"jobs/{tid}", "progress": {}, "cost_estimate": 0.0,
                                "created_at": db.now()})
        job = jobs.submit("colab_prepare", {"training_id": tid}, message="放進雲端硬碟資料夾")
        return db.update("trainings", tid, {"job_id": job["id"]})
    loc = runpod.location()
    try:  # the volume must still exist and be reachable over S3; an unreachable API is left to the upload itself
        chk = runpod.check()
    except Exception:
        chk = {}
    if chk.get("problem"):
        raise ValueError(chk["problem"] + "還沒有上傳任何資料。")
    row = {"voice_id": ds["voice_id"], "dataset_id": dataset_id, "engine": engine_id,
           "preset": {"id": pl["preset"], "params": pl["params"], "name": name}, "target": "runpod",
           "gpu": pl["gpu"], "storage": loc, "progress": {}, "cost_estimate": pl["estimate_usd"]}
    if gpus:  # auto-grab: only cards with enough memory for this training method; stock is the waiter's business
        usable = {o["id"] for o in gpu_offers(engine_id, pl["preset"], runpod.gpu_catalog(loc["datacenter"]))["offers"]}
        bad = [g.replace("NVIDIA ", "") for g in gpus if g not in usable]
        if bad:
            raise ValueError(f"{'、'.join(bad)} 的顯示記憶體不夠這個訓練方式用，請從清單拿掉。")
        hours = min(72.0, max(0.25, float(wait_hours or 12)))
        now = time.time()
        tid = db.new_id("tr")
        db.insert("trainings", {"id": tid, **row, "status": "waiting_gpu", "remote_prefix": f"vs/jobs/{tid}",
                                "wait": {"gpus": list(dict.fromkeys(gpus)), "since": now, "until": now + hours * 3600,
                                         "checks": 0}, "created_at": db.now()})
        GPU_WAKE.set()  # look at the stock right away
        return db.get("trainings", tid)
    problem = _stock_problem(engine_id, pl["preset"], pl["gpu"], loc["datacenter"])
    if problem:  # checked before anything is uploaded or rented
        raise ValueError(problem + "還沒有上傳任何資料。可以勾「沒貨時自動搶卡」，有貨時自動開始。")
    tid = db.new_id("tr")
    db.insert("trainings", {"id": tid, **row, "status": "queued", "remote_prefix": f"vs/jobs/{tid}",
                            "created_at": db.now()})
    job = jobs.submit("cloud_train", {"training_id": tid}, message="準備租用 GPU")
    return db.update("trainings", tid, {"job_id": job["id"]})


def _set(tid: str, **kw) -> None:
    db.update("trainings", tid, kw)


def _loc(tr: dict) -> dict:
    return tr.get("storage") or runpod.location()


def package_dataset(tid: str, work: Path) -> tuple[Path, dict]:
    """Export the dataset in the engine's format and pack it with its audio into dataset.tar."""
    tr = db.get("trainings", tid)
    ds = db.get("datasets", tr["dataset_id"])
    eng = engines.get(tr["engine"])
    exp = work / "export"
    shutil.rmtree(exp, ignore_errors=True)
    info = eng.export_dataset(ds, exp, tr["preset"]["params"])
    tar_path = work / "dataset.tar"
    with tarfile.open(tar_path, "w") as t:
        t.add(exp, arcname="data")
        t.add(Path(ds["path"]) / "wavs", arcname="data/wavs")
        t.add(Path(ds["path"]) / "meta.json", arcname="data/meta.json")
    cfg = {"training_id": tid, "engine": eng.id, "preset": tr["preset"]["id"], "params": tr["preset"]["params"],
           "dataset": {"id": ds["id"], "hours": ds["hours"], **info}, "voice_name": ds["meta"]["voice"]["name"],
           "languages": ds["meta"].get("languages", [])}
    return tar_path, cfg


def _check_reference(tr: dict, eng) -> None:
    """Engines that train on a reference clip fail only after renting a GPU when it is missing or unreadable."""
    ds = db.get("datasets", tr["dataset_id"])
    refs = ds["meta"].get("reference_items") or [{"audio": a} for a in ds["meta"].get("reference", [])]
    if not refs:
        if eng.needs_training_reference:
            raise ValueError("資料集沒有 5–12 秒的參考片段，這個引擎無法訓練。請多核可一些 5 秒以上的片段後重建資料集。")
        return
    import soundfile as sf
    try:
        info = sf.info(str(Path(ds["path"]) / refs[0]["audio"]))
    except Exception as e:
        raise ValueError(f"參考片段讀不到：{e}")
    if info.frames / max(1, info.samplerate) < 1.0:
        raise ValueError("參考片段短於 1 秒")


def _remove_pod(tid: str, pod_id: str | None) -> bool:
    """Remove the run's pod and record the outcome; a failure is left for reap() to retry."""
    if not pod_id:
        return True
    try:
        runpod.remove_pod(pod_id)
        _set(tid, pod_state="removed")
        return True
    except Exception as e:
        _set(tid, pod_state="remove_failed", note=f"雲端機器刪除失敗：{str(e)[:200]}。請到 RunPod 確認。")
        return False


def _find_pods(tid: str, loc: dict) -> list[dict]:
    """Pods created for this run (a lost POST response can still have created one, maybe more)."""
    pods = runpod.list_pods(name=f"voice-studio-{tid}", volume=loc.get("volume"))
    return [p for p in pods if (p.get("env") or {}).get("VS_TRAINING_ID", tid) == tid]


def _upload_status(status: str, sent: int, total: int) -> str:
    """upload.json, read by wait_upload in bootstrap.sh: compact JSON that changes on every write while uploading."""
    return json.dumps({"status": status, "bytes": sent, "total": total, "t": round(time.time(), 1)},
                      separators=(",", ":"))


def _upload_allowance(size: int) -> int:
    """Extra seconds on the pod's time limit for the upload that runs on rented time: twice the time it should take at
    the measured upload speed (2 MB/s before one was measured), at least 30 minutes, at most 6 hours."""
    bps = float(config.load_settings().get("upload_bps") or 0) or 2e6
    return int(min(6 * 3600, max(1800, 2 * size / bps)))


def _send_dataset(ctx: jobs.JobContext, tid: str, work: Path, prefix: str, loc: dict) -> None:
    """Package the dataset and upload it to the volume of the pod that is already rented. upload.json is rewritten
    every minute from the start, so the pod knows the studio is still at it (it gives up after 15 minutes without a
    word); an error the pod reports while setting up stops the upload early instead of finishing it for nothing."""
    sent, total, stop, trouble = [0], [0], threading.Event(), []

    def heartbeat():
        while not stop.wait(60):
            try:
                runpod.put_text(f"{prefix}/upload.json", _upload_status("uploading", sent[0], total[0]), loc=loc)
                if runpod.exists(f"{prefix}/error.json", loc, fast=True):
                    trouble.append("雲端機器在準備環境時出錯，已停止上傳。按「紀錄」看原因。")
                    return
            except Exception as e:  # a missed beat is harmless: the pod waits 15 minutes for the next one
                ctx.log(f"upload heartbeat failed: {e}")

    def progress(f: float) -> None:
        sent[0] = int(f * total[0])
        if trouble:
            raise RuntimeError(trouble[0])
        ctx.progress(0.05 + 0.15 * f, f"已租到 GPU，上傳資料 {f * 100:.0f}%（上傳完就開始訓練）")

    threading.Thread(target=heartbeat, name=f"upload-{tid}", daemon=True).start()
    try:
        ctx.progress(0.04, "已租到 GPU，整理訓練資料")
        tar_path, cfg = package_dataset(tid, work)
        total[0] = tar_path.stat().st_size
        runpod.put_text(f"{prefix}/config.json", json.dumps(cfg, ensure_ascii=False, indent=2), loc=loc)
        t0 = time.time()
        runpod.upload(tar_path, f"{prefix}/dataset.tar", progress=progress, loc=loc)
        took = time.time() - t0
    finally:
        stop.set()
    tar_path.unlink(missing_ok=True)
    runpod.put_text(f"{prefix}/upload.json", _upload_status("done", total[0], total[0]), loc=loc)
    _set(tid, uploaded_at=time.time())
    if total[0] >= 50 << 20:  # remembered for the estimates and the next pod's time limit
        config.save_settings({"upload_bps": round(total[0] / max(1.0, took))})


def _rentable(engine_id: str, preset_id: str, gpus: list[str], datacenter: str) -> list[str]:
    """The cards of the list (in its order) that can be rented in the datacenter now; all of them when the live
    stock cannot be read (renting is then simply tried)."""
    res = gpu_offers(engine_id, preset_id, runpod.gpu_catalog(datacenter))
    if not res["live"]:
        return list(gpus)
    stock = {o["id"]: o["availability"] for o in res["offers"]}
    return [g for g in gpus if stock.get(g) in runpod.IN_STOCK]


# --- auto-grab: wait for a GPU without renting anything -------------------------------------------------------------

GRAB_POLL_S = 30                 # how often the live stock is checked for runs waiting for a GPU
GPU_WAKE = threading.Event()     # set to check at once (a new waiting run)
_GRAB_LOCK = threading.Lock()


def _rewait(tid: str, why: str) -> bool:
    """Put an auto-grab run back to waiting after the card was gone again; False when its waiting time is over."""
    tr = db.get("trainings", tid)
    w = dict(tr.get("wait") or {})
    if not w or time.time() >= (w.get("until") or 0):
        return False
    w.update(misses=(w.get("misses") or 0) + 1, note=why)
    _set(tid, status="waiting_gpu", wait=w, deadline=None, started_at=None)
    return True


def wait_for_gpus() -> list[str]:
    """Runs in a server thread every GRAB_POLL_S seconds. For each run waiting for a GPU, look at the live stock of
    its datacenter; as soon as a card of its list can be rented, hand it to cloud_train with the cards in stock (in
    the person's order), which rents first and uploads after. Waiting costs nothing: no pod exists until then.
    Returns the runs that were started."""
    started = []
    with _GRAB_LOCK:
        for tr in db.query("SELECT * FROM trainings WHERE status='waiting_gpu'"):
            tid, w, now = tr["id"], dict(tr.get("wait") or {}), time.time()
            if now >= (w.get("until") or 0):
                hours = round(((w.get("until") or now) - (w.get("since") or now)) / 3600, 1)
                _set(tid, status="failed", finished_at=db.now(),
                     note=f"等了 {hours:g} 小時都沒搶到卡，已停止。沒有租用或上傳任何東西，也沒有計費。")
                continue
            try:
                _require_consent(tr["voice_id"])
            except datasets.ConsentMissing as e:
                _set(tid, status="failed", finished_at=db.now(), note=str(e))
                continue
            dc = (tr.get("storage") or {}).get("datacenter")
            res = gpu_offers(tr["engine"], tr["preset"]["id"], runpod.gpu_catalog(dc))
            stock = {o["id"]: o["availability"] for o in res["offers"]}
            ready = [g for g in w.get("gpus", []) if stock.get(g) in runpod.IN_STOCK] if res["live"] else []
            w.update(checks=(w.get("checks") or 0) + 1, last=now, error=res["error"],
                     seen={g: stock.get(g) for g in w.get("gpus", [])})
            if not ready:
                _set(tid, wait=w)
                continue
            _set(tid, wait=w, status="queued", gpu=ready[0])
            job = jobs.submit("cloud_train", {"training_id": tid, "gpus": ready}, message="有貨了，租用 GPU")
            _set(tid, job_id=job["id"])
            started.append(tid)
    return started


def _dataset_bytes(ds: dict) -> int:
    """Roughly the size of the dataset.tar a run uploads (the dataset folder: audio and metadata)."""
    total = 0
    for root, _dirs, files in os.walk(ds["path"]):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


@jobs.handler("cloud_train", queue="io")
def cloud_train(ctx: jobs.JobContext) -> dict:
    """Upload → pod → watch → download. Whatever goes wrong, the training row ends in a final state and the pod is
    removed, or marked for removal so reap() keeps trying."""
    tid = ctx.params["training_id"]
    try:
        return _cloud_train(ctx)
    except BaseException as e:
        tr = db.get("trainings", tid)
        if tr and tr["status"] not in ("done", "failed", "canceled"):
            if tr.get("pod_id"):
                _remove_pod(tid, tr["pod_id"])
            elif tr.get("pod_state") in ("creating", "uncertain"):
                _reconcile_creation(tid, _loc(tr))
            if not isinstance(e, jobs.Cancelled) and tr["status"] != "downloading" and recoverable(tr):
                try:  # the weights were published before the failure: keep them
                    _download_and_install(ctx, tid, partial=True,
                                          note=f"訓練沒有正常結束（{str(e)[:120]}），但權重已經救回。")
                    return {"message": "訓練沒有正常結束，但權重已經救回"}
                except Exception as e2:
                    ctx.log(f"weight recovery failed: {e2}")
            _set(tid, status="canceled" if isinstance(e, jobs.Cancelled) else "failed", finished_at=db.now())
            _save_log(tid, tr["remote_prefix"], config.DATA / "jobs" / tid, _loc(tr))
        raise


def _cloud_train(ctx: jobs.JobContext) -> dict:
    tid = ctx.params["training_id"]
    tr = db.get("trainings", tid)
    eng = engines.get(tr["engine"])
    loc = _loc(tr)
    prefix = tr["remote_prefix"]
    work = config.DATA / "jobs" / tid
    work.mkdir(parents=True, exist_ok=True)
    _require_consent(tr["voice_id"])

    resume = bool(ctx.params.get("resume") and tr.get("pod_id"))
    if resume:  # the studio was closed while the pod kept working: pick the run up again
        pod_id = tr["pod_id"]
        started = tr.get("started_at") or tr["created_at"]
        deadline = tr.get("deadline") or (tr["created_at"] + float(config.load_settings()["runpod_max_hours"]) * 3600)
        ctx.log(f"resuming watch of pod {pod_id}")
    else:
        # GPU first: the small files go up, the pod is rented, and only then is the dataset packaged and uploaded,
        # while the pod sets up its environment (bootstrap.sh waits for upload.json). A scarce card is never lost to a
        # long upload, and an auto-grab run holds the card seconds after it shows up in stock.
        # 1. the small files (a retry on another GPU reuses the dataset an earlier attempt of this run uploaded)
        reuse = bool(ctx.params.get("reuse_upload")) and runpod.exists(f"{prefix}/dataset.tar", loc)
        grab = bool(tr.get("wait"))  # auto-grab: the person accepts any card of their list
        gpus = ctx.params.get("gpus") or [tr["gpu"]]
        _set(tid, status="starting")
        ctx.progress(0.01, "準備租用 GPU")
        _check_reference(tr, eng)  # before paying for anything
        _require_consent(tr["voice_id"])
        size = runpod.size(f"{prefix}/dataset.tar", loc) if reuse else _dataset_bytes(db.get("datasets", tr["dataset_id"]))
        runpod.put_text(f"{prefix}/bootstrap.sh", BOOTSTRAP, loc=loc)
        for fname, text in eng.cloud_files().items():
            runpod.put_text(f"{prefix}/{fname}", text, loc=loc)
        runpod.put_text(f"{prefix}/upload.json", _upload_status("done" if reuse else "waiting", 0, size), loc=loc)
        then = ("訓練資料已經在雲端，按「換一張 GPU 重試」就好，不用重新上傳。" if reuse
                else "訓練資料還沒上傳，換一張有貨的卡再按一次開始就好。")
        if grab:
            gpus = _rentable(eng.id, tr["preset"]["id"], gpus, loc["datacenter"])
            if not gpus:
                if _rewait(tid, "剛好又沒貨了"):
                    return {"message": "剛好又沒貨了，繼續等"}
                raise RuntimeError("等卡的時間到了，還是沒有搶到卡（沒有租用或上傳任何東西）。")
        else:
            problem = _stock_problem(eng.id, tr["preset"]["id"], gpus[0], loc["datacenter"])
            if problem:
                raise RuntimeError(problem + then)
        ctx.check()

        # 2. rent the pod (intent and deadline are recorded first, so a lost response can be reconciled); its time
        # limit also covers the upload, which now runs on rented time
        max_h = float(config.load_settings().get("runpod_max_hours") or 12)
        allow = 0 if reuse else _upload_allowance(size)
        started = time.time()  # "running for" counts from here: an auto-grab run's waiting cost nothing
        deadline = started + max_h * 3600 + allow + 900
        _set(tid, pod_state="creating", deadline=deadline, started_at=started)
        ctx.progress(0.03, "租用雲端 GPU")
        env = {"VS_TRAINING_ID": tid, "VS_ENGINE": eng.id, "VS_MAX_SECONDS": str(int(max_h * 3600 + allow)),
               "VS_IMAGE": eng.image, "VS_WAIT_UPLOAD": "1"}
        hf = config.get_secret("hf_token")
        if hf:
            env["HF_TOKEN"] = hf
        preset = eng.preset(tr["preset"]["id"])
        try:
            pod = runpod.create_pod(f"voice-studio-{tid}", eng.image, gpus, env,
                                    ["bash", "-c", f"bash /workspace/{prefix}/bootstrap.sh"], loc,
                                    container_disk_gb=preset.disk_gb, min_ram_gb=preset.ram_gb,
                                    min_vcpu=preset.vcpu)
        except Exception as e:
            time.sleep(10)
            _reconcile_creation(tid, loc)  # the request may have gone through even though we saw an error
            if grab and _rewait(tid, f"差一點：{str(e)[:120]}"):
                return {"message": "差一點就搶到，被別人先租走了，繼續等"}
            raise RuntimeError(f"沒有租到 GPU：{str(e)[:300]}（這張卡剛好被租走了。{then}）")
        pod_id = pod.get("id")
        gpu_actual = (pod.get("machine") or {}).get("gpuTypeId") or gpus[0]
        rate = pod.get("costPerHr") or pod.get("adjustedCostPerHr")
        fields = {}
        if grab or gpu_actual != tr["gpu"]:  # auto-grab may rent a later card of the list: the estimate follows it
            fields["cost_estimate"] = _estimate_usd(tr, gpu_actual, rate, upload=not reuse)
        _set(tid, status="running" if reuse else "uploading", pod_id=pod_id, pod_state="running", gpu=gpu_actual,
             cost_per_hr=rate, **fields)
        ctx.log(f"pod {pod_id} created on {gpu_actual} at {pod.get('costPerHr')} /h")

        # 3. package and upload the dataset onto the rented pod's volume
        if not reuse:
            _send_dataset(ctx, tid, work, prefix, loc)
            _set(tid, status="running")

    # 3. watch
    last_poll, s3_errors, partial = 0.0, 0, False
    prog: dict = dict(tr.get("progress") or {})
    try:
        while True:
            ctx.check()
            time.sleep(5)
            if time.time() - last_poll < 30:
                continue
            last_poll = time.time()
            if time.time() > deadline:
                raise RuntimeError("超過最長時數，已強制停止。")
            try:
                prog = runpod.get_json(f"{prefix}/progress.json", loc, fast=True) or prog
                done = runpod.get_json(f"{prefix}/done.json", loc, fast=True)
                err = runpod.get_json(f"{prefix}/error.json", loc, fast=True)
                s3_errors = 0
            except Exception as e:  # network or storage hiccup: retry for ~10 minutes before giving up
                s3_errors += 1
                ctx.log(f"storage read failed ({s3_errors}): {e}")
                if s3_errors >= 20:
                    raise RuntimeError("連續 10 分鐘讀不到雲端儲存，已停止並關閉雲端機器。")
                continue
            _set(tid, progress={**prog, "wall_s": int(time.time() - started)})
            ctx.progress(0.2 + 0.65 * _fraction(prog), _phase_label(prog))
            if done:
                partial = done.get("rc", 0) != 0
                break
            if err:
                if runpod.exists(f"{prefix}/model.tar", loc):  # weights were published before the failure
                    partial = True
                    break
                raise RuntimeError(f"雲端訓練失敗（{_stage_label(err)}）。請到「雲端訓練」看紀錄。")
            if time.time() > deadline:
                raise RuntimeError("超過最長時數，已強制停止。")
            try:
                gone = runpod.get_pod(pod_id) is None
            except Exception:
                gone = False
            if gone:
                if runpod.get_json(f"{prefix}/done.json", loc) or runpod.exists(f"{prefix}/model.tar", loc):
                    partial = not runpod.get_json(f"{prefix}/done.json", loc)
                    break
                raise RuntimeError("雲端機器意外消失（可能被平台回收）。可以重試。")
    finally:
        _remove_pod(tid, pod_id)  # normally the pod has already removed itself
    if prog.get("s_per_step"):
        _remember_speed(eng.id, tr["preset"]["id"], db.get("trainings", tid)["gpu"], float(prog["s_per_step"]))

    # 4. download and register (also reachable on its own, to recover weights after a failure)
    m = _download_and_install(ctx, tid, partial)
    return {"model_id": m["id"], "message": "訓練完成，模型已下載，正在評分各檢查點"}


def _download_and_install(ctx: jobs.JobContext, tid: str, partial: bool = False, note: str = "",
                          span: tuple[float, float] = (0.86, 0.96)) -> dict:
    """model.tar is required; samples.tar is optional and never blocks registering valid weights. span is the part
    of the job's progress bar the model download fills (most of it when recovering, the end of a training run)."""
    tr = db.get("trainings", tid)
    loc, prefix = _loc(tr), tr["remote_prefix"]
    work = config.DATA / "jobs" / tid
    work.mkdir(parents=True, exist_ok=True)
    _set(tid, status="downloading")
    tar_local = work / "model.tar"
    try:  # the archive and its unpacked copy both land on this drive: say so now, not after hours of downloading
        size = runpod.size(f"{prefix}/model.tar", loc)
        part = tar_local.with_name("model.tar.part")
        need = (0 if part.exists() and part.stat().st_size == size else size) + int(size * 1.1)
        free = shutil.disk_usage(work).free
    except Exception:
        size = need = free = 0
    if need and free < need:
        raise RuntimeError(f"電腦的磁碟空間不夠：模型檔約 {size / 1e9:.1f} GB，下載加解開還需要約 {need / 1e9:.1f} GB，"
                           f"{work.anchor or '這個磁碟'} 只剩 {free / 1e9:.1f} GB。模型還在雲端，清出空間後按「救回模型」。")
    lo, hi = span
    first = {"t": time.time(), "f": None}

    def shown(f: float) -> None:  # "下載模型 37%（8.9 / 24.0 GB，12 MB/s）"
        if first["f"] is None:
            first.update(f=f, t=time.time())  # parts already down from an earlier try do not count toward the speed
        dt = time.time() - first["t"]
        rate = (f - first["f"]) * size / dt if size and dt >= 5 else 0
        amount = f"（{f * size / 1e9:.1f} / {size / 1e9:.1f} GB{f'，{rate / 1e6:.1f} MB/s' if rate else ''}）" if size else ""
        ctx.progress(lo + (hi - lo) * f, f"下載模型 {f * 100:.0f}%{amount}")
    ctx.progress(lo, f"下載模型（{size / 1e9:.1f} GB）" if size else "下載模型")
    try:  # resumable: what came down stays in the work folder, and "recover model" continues from there
        runpod.download(f"{prefix}/model.tar", tar_local, loc=loc, progress=shown, check=ctx.check)
    except jobs.Cancelled:
        raise
    except Exception as e:
        raise RuntimeError(f"模型已經訓練好，存在雲端網路磁碟上，只是下載回來時中斷了（{str(e)[:160]}）。"
                           "按「救回模型」會從中斷的地方接著下載，不用重新訓練。") from e
    samples_local = None
    try:
        if runpod.exists(f"{prefix}/samples.tar", loc):
            samples_local = runpod.download(f"{prefix}/samples.tar", work / "samples.tar", loc=loc, check=ctx.check,
                                            progress=lambda f: ctx.progress(hi + (0.99 - hi) * f, "下載樣本"))
    except jobs.Cancelled:
        raise
    except Exception as e:
        ctx.log(f"samples download failed: {e}")
        samples_local = None
    _save_log(tid, prefix, work, loc)
    m = install_model(tid, tar_local, samples_local)
    sampling = (m["meta"] or {}).get("sampling")
    if not note and (partial or samples_local is None or sampling != "complete"):
        note = "樣本試念沒有完成：模型可以用，但檢查點比較不完整。"
    _set(tid, status="done", finished_at=db.now(), note=note)
    for name in ("dataset.tar", "model.tar", "samples.tar"):  # keep the volume small; log and config stay
        try:
            runpod.delete(f"{prefix}/{name}", loc)
        except Exception:
            pass
    return m


@jobs.handler("recover_model", queue="io")
def recover_model(ctx: jobs.JobContext) -> dict:
    """Download the weights of a run that ended badly but had already published model.tar."""
    tid = ctx.params["training_id"]
    tr = db.get("trainings", tid)
    try:
        ctx.progress(0.01, "連線到雲端網路磁碟，確認模型檔還在…")
        try:  # a quick look: "cannot reach the volume" and "the file is not there" are different answers
            there = runpod.exists(f"{tr['remote_prefix']}/model.tar", _loc(tr), fast=True)
        except Exception as e:
            raise RuntimeError(f"連不上 RunPod 的網路磁碟（{str(e)[:160]}）。模型還在雲端，網路恢復後再按「救回模型」。") from e
        if not there:
            raise RuntimeError("雲端沒有這次訓練的模型檔（訓練沒有完成到存檔那一步）。")
        m = _download_and_install(ctx, tid, partial=True, note="訓練沒有正常結束，但權重已經救回。", span=(0.03, 0.95))
    except BaseException:  # back to "failed", so "recover model" can be pressed again (and continues the download)
        if (db.get("trainings", tid) or {}).get("status") == "downloading":
            _set(tid, status="failed", finished_at=db.now())
        raise
    return {"model_id": m["id"], "message": "已救回模型"}


def recoverable(tr: dict) -> bool:
    if tr.get("target") == "colab":
        return colab.recoverable(tr)
    try:
        return runpod.exists(f"{tr['remote_prefix']}/model.tar", _loc(tr))
    except Exception:
        return False


def can_retry_gpu(tr: dict) -> bool:
    """A RunPod run that uploaded its data and stopped before it got a GPU: it can try another card without
    uploading again (retry_on_gpu checks that the data is really still on the volume)."""
    return (tr.get("target") == "runpod" and tr["status"] in ("failed", "canceled") and not tr.get("pod_id")
            and bool(tr.get("uploaded_at")))


def retry_on_gpu(tid: str, gpu: str, usd_h: float | None = None) -> dict:
    tr = db.get("trainings", tid)
    if not tr:
        raise KeyError(tid)
    if not can_retry_gpu(tr):
        raise ValueError("只有資料已經上傳、但還沒租到 GPU 就停下的 RunPod 訓練可以換卡重試。")
    loc = _loc(tr)
    if not runpod.exists(f"{tr['remote_prefix']}/dataset.tar", loc):
        raise ValueError("雲端已經沒有這次上傳的資料，請重新開始一次訓練。")
    _require_consent(tr["voice_id"])
    problem = _stock_problem(tr["engine"], tr["preset"]["id"], gpu, loc["datacenter"])
    if problem:
        raise ValueError(problem)
    try:  # a create request that looked failed can still have made a pod: it must not train next to the new one
        found = _find_pods(tid, loc)
    except Exception as e:
        raise ValueError(f"暫時無法確認 RunPod 上沒有這次訓練留下的機器（{str(e)[:120]}），請稍後再試。")
    if not all(_remove_pod(tid, p.get("id")) for p in found):
        raise ValueError("RunPod 上有這次訓練留下的機器，刪除失敗。請到 runpod.io → Pods 確認後再試。")
    # the row is updated before the job exists, so the worker never reads the old GPU
    _set(tid, gpu=gpu, status="queued", pod_state=None, note="", finished_at=None, deadline=None, started_at=None,
         cost_estimate=_estimate_usd(tr, gpu, usd_h, upload=False), cost_per_hr=None, progress={})
    job = jobs.submit("cloud_train", {"training_id": tid, "reuse_upload": True}, message="換一張 GPU 重試")
    return db.update("trainings", tid, {"job_id": job["id"]})


def _estimate_usd(tr: dict, gpu: str, usd_h: float | None, upload: bool) -> float:
    """What a run costs on this card at this hourly price: training at the card's measured (or scaled) speed, plus
    the dataset upload when it still has to go up on rented time (as plan() counts it)."""
    ds, eng = db.get("datasets", tr["dataset_id"]), engines.get(tr["engine"])
    usd_h = usd_h or runpod.GPUS.get(gpu, {}).get("usd_h", 1.5)
    est = eng.estimate(ds["hours"], tr["preset"]["id"], usd_h, n_train=int(ds["meta"].get("n_train") or ds["n_items"]),
                       s_per_step=_speed(eng.id, tr["preset"]["id"], gpu)[0], params=tr["preset"]["params"])
    bps = float(config.load_settings().get("upload_bps") or 0)
    if upload and bps:
        return round((est["hours"] + _dataset_bytes(ds) / bps / 3600) * usd_h, 2)
    return est["usd"]


def _reconcile_creation(tid: str, loc: dict) -> None:
    """After an uncertain POST /pods: remove what RunPod shows for this run. If nothing is visible yet, or a removal
    fails, the run stays 'uncertain' and reap() keeps looking (a pod can appear after the listing)."""
    try:
        found = _find_pods(tid, loc)
    except Exception:
        _set(tid, pod_state="uncertain")
        return
    ok = all(_remove_pod(tid, p.get("id")) for p in found)
    _set(tid, pod_state="removed_found" if found and ok else "uncertain")


def resume_interrupted() -> list[str]:
    """At start-up: runs whose watcher died with the app are picked up again (the pod kept training); a run that
    was creating its pod is reconciled against RunPod's pod list; earlier runs are marked failed."""
    resumed = []
    for tr in db.query("SELECT * FROM trainings WHERE status IN ('queued','uploading','starting','running',"
                       "'downloading')"):
        j = db.get("jobs", tr["job_id"]) if tr.get("job_id") else None
        if j and j["status"] in ("queued", "running"):
            continue
        if tr.get("target") == "colab":  # Colab keeps training without the studio; the poller picks it up again
            if tr["status"] == "downloading":
                job = jobs.submit("colab_install", {"training_id": tr["id"], "partial": False}, "從雲端硬碟取回模型")
                _set(tr["id"], job_id=job["id"])
                resumed.append(tr["id"])
            elif tr["status"] in ("queued", "uploading"):
                _set(tr["id"], status="failed", finished_at=db.now(), note="程式關閉時還在準備 Colab 訓練，請重新開始。")
            continue
        pod_id = tr.get("pod_id")
        if not pod_id and tr.get("pod_state") == "creating":
            try:
                found = _find_pods(tr["id"], _loc(tr))
            except Exception:
                found = []
            if len(found) == 1 and tr.get("uploaded_at"):
                pod_id = found[0].get("id")
                _set(tr["id"], pod_id=pod_id, pod_state="running", status="running")
            else:
                for p in found:
                    _remove_pod(tr["id"], p.get("id"))
        if pod_id and tr["status"] in ("starting", "running", "downloading"):
            job = jobs.submit("cloud_train", {"training_id": tr["id"], "resume": True}, "重新連上雲端訓練")
            _set(tr["id"], job_id=job["id"])
            resumed.append(tr["id"])
        else:
            removed = _remove_pod(tr["id"], pod_id)
            # an auto-grab run closed while renting its card or uploading: wait again rather than give up
            if tr.get("wait") and removed and _rewait(tr["id"], "程式關閉時正在租卡或上傳，重新等卡"):
                _set(tr["id"], pod_id=None, pod_state=None, cost_per_hr=None, uploaded_at=None)
                continue
            _set(tr["id"], status="failed", finished_at=db.now(), note="程式關閉時中斷（還沒開始雲端訓練），請重新開始。")
    return resumed


def reap() -> dict:
    """The safety net outside the pod, run at start-up and every few minutes while the studio is open:
    - retry removals that failed, and keep looking for pods of runs whose creation was uncertain;
    - stop runs that are past their deadline when nothing is watching them;
    - list studio pods (named voice-studio-<training id>) that no live run owns, removing those of finished runs."""
    removed, orphans = [], []
    now = time.time()
    for tr in db.query("SELECT * FROM trainings WHERE pod_state IN ('remove_failed','creating','uncertain','running') "
                       "AND status IN ('done','failed','canceled')"):
        if tr.get("pod_id") and _remove_pod(tr["id"], tr["pod_id"]):
            removed.append(tr["pod_id"])
        elif not tr.get("pod_id"):
            _reconcile_creation(tr["id"], _loc(tr))
            # nothing has appeared for a day: the request really did not create a pod
            if (db.get("trainings", tr["id"]) or {}).get("pod_state") == "uncertain" and \
                    now - (tr.get("started_at") or tr["created_at"]) > 86400:
                _set(tr["id"], pod_state="none_found")
    for tr in db.query("SELECT * FROM trainings WHERE status IN ('starting','running','downloading') "
                       "AND deadline IS NOT NULL AND deadline < ?", (now - 1800,)):
        j = db.get("jobs", tr["job_id"]) if tr.get("job_id") else None
        if j and j["status"] == "running":
            continue  # its watcher enforces the deadline itself
        if tr.get("pod_id"):
            _remove_pod(tr["id"], tr["pod_id"])
        _set(tr["id"], status="failed", finished_at=db.now(), note="超過最長時數，雲端機器已關閉。")
    try:
        pods = runpod.studio_pods()
    except Exception as e:
        return {"removed": removed, "orphans": [], "error": str(e)[:200]}
    for p in pods:
        tid = str(p.get("name", ""))[len("voice-studio-"):]
        tr = db.get("trainings", tid)
        if tr and tr["status"] in ("done", "failed", "canceled"):
            try:
                runpod.remove_pod(p["id"])
                removed.append(p["id"])
            except Exception:
                orphans.append({"id": p.get("id"), "name": p.get("name"), "training": tid, "known": True})
        elif not tr:
            orphans.append({"id": p.get("id"), "name": p.get("name"), "training": tid, "known": False,
                            "cost_per_hr": p.get("costPerHr")})
    return {"removed": removed, "orphans": orphans}


CHECKPOINT_NAME = __import__("re").compile(r"[A-Za-z0-9_][A-Za-z0-9_.-]{0,79}")


def install_model(tid: str, tar_local: Path, samples_tar: Path | None = None) -> dict:
    """Unpack model.tar (and samples.tar) into data/models/<id>, register it once and queue checkpoint scoring."""
    existing = db.query("SELECT * FROM models WHERE training_id=?", (tid,))
    if existing:  # a crash between registering and marking the run done must not register it twice
        return existing[0]
    tr = db.get("trainings", tid)
    ds = db.get("datasets", tr["dataset_id"])
    eng = engines.get(tr["engine"])
    model_id = db.new_id("mdl")
    mdir = config.DATA / "models" / model_id
    tmp = config.DATA / "tmp" / f"unpack-{model_id}"
    for archive in [tar_local] + ([samples_tar] if samples_tar else []):
        with tarfile.open(archive) as t:
            t.extractall(tmp, filter="data")
    emeta = json.loads((tmp / "model" / "engine.json").read_text(encoding="utf-8"))
    bad = [c.get("name") for c in emeta.get("checkpoints", [])
           if not isinstance(c.get("name"), str) or not CHECKPOINT_NAME.fullmatch(c["name"]) or ".." in c["name"]]
    if bad:
        shutil.rmtree(tmp, ignore_errors=True)
        raise ValueError(f"模型檔裡有不合法的檢查點名稱：{bad[:3]}")
    shutil.move(str(tmp / "model"), str(mdir))
    shutil.rmtree(tmp, ignore_errors=True)
    for f in [tar_local] + ([samples_tar] if samples_tar else []):
        f.unlink(missing_ok=True)
    refs = _copy_references(ds, mdir)
    voice = db.get("voices", tr["voice_id"])
    cks = [c for c in emeta.get("checkpoints", []) if c.get("weights")]
    m = db.insert("models", {
        "id": model_id, "voice_id": voice["id"], "engine": eng.id,
        "name": tr["preset"].get("name") or f"{voice['name']} · {eng.name} · {eng.preset(tr['preset']['id']).label}",
        "training_id": tid, "path": str(mdir),
        "meta": {"dataset_id": ds["id"], "preset": tr["preset"], "consent": ds["meta"].get("consent"),
                 "mode": emeta.get("mode"), "checkpoint": cks[-1]["name"] if cks else None, "references": refs,
                 "languages": ds["meta"].get("languages", []), "sampling": emeta.get("sampling")},
        "metrics": {}, "created_at": db.now()})
    if (mdir / "samples").exists():
        jobs.submit("evaluate_model", {"model_id": model_id}, message="評分檢查點")
    return m


def _copy_references(ds: dict, mdir: Path, limit: int = 11) -> list[dict]:
    items = ds["meta"].get("reference_items") or [{"audio": a, "text": "", "lang": ""}
                                                    for a in ds["meta"].get("reference", [])]
    out = []
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    for k, it in enumerate(items[:limit]):
        src = Path(ds["path"]) / it["audio"]
        if not src.exists():
            continue
        dst = mdir / "references" / f"ref{k}.wav"
        shutil.copy2(src, dst)
        emo = it.get("emotion") or ""
        out.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": it.get("text", ""),
                    "lang": it.get("lang", ""), "segment_id": it.get("id"), "emotion": emo,
                    "label": f"資料集參考：{emotions.EMOTIONS[emo]}" if emo in emotions.EMOTIONS
                    else "資料集參考 " + str(k + 1)})
    return out


def create_zeroshot(voice_id: str, engine_id: str, segment_ids: list[str], name: str = "") -> dict:
    """A model without training: the base model cloning from reference clips. Free and instant; a good way to hear
    an engine before paying for training, though it copies habits and accent far less than a fine-tuned model."""
    voice = db.get("voices", voice_id)
    if not voice:
        raise KeyError(voice_id)
    if not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音的同意紀錄不完整，不能用來合成。")
    eng = engines.get(engine_id)
    if "ref" not in eng.modes({"mode": "zeroshot"}):
        raise ValueError("這個引擎不支援零樣本")
    model_id = db.new_id("mdl")
    mdir = config.DATA / "models" / model_id
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    refs = []
    for k, sid in enumerate(segment_ids[:5]):
        s = db.get("segments", sid)
        if not s or s["voice_id"] != voice_id:
            continue
        shutil.copy2(s["path"], mdir / "references" / f"ref{k}.wav")
        refs.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": s["text"], "lang": s["lang"] or "",
                     "label": (s["text"][:24] + "…") if len(s["text"]) > 24 else s["text"], "segment_id": sid,
                     "emotion": s.get("emotion") or ""})
    if not refs:
        raise ValueError("請至少選一個這個聲音的片段當參考")
    (mdir / "engine.json").write_text(json.dumps({"engine": eng.id, "mode": "zeroshot", "checkpoints": []}),
                                      encoding="utf-8")
    return db.insert("models", {"id": model_id, "voice_id": voice_id, "engine": eng.id,
                                "name": name or f"{voice['name']} · {eng.name} · 免訓練", "path": str(mdir),
                                "meta": {"mode": "zeroshot", "references": refs, "languages": voice["languages"]},
                                "metrics": {}, "created_at": db.now()})


def add_reference(model_id: str, segment_id: str, label: str = "") -> dict:
    m = db.get("models", model_id)
    s = db.get("segments", segment_id)
    if not m or not s:
        raise KeyError("model or segment")
    if s["voice_id"] != m["voice_id"]:
        raise ValueError("只能用同一個聲音的片段當參考")
    refs = list((m["meta"] or {}).get("references", []))
    k = max([int(r["id"][3:]) for r in refs if r["id"].startswith("ref")] + [-1]) + 1
    mdir = Path(m["path"])
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    shutil.copy2(s["path"], mdir / "references" / f"ref{k}.wav")
    refs.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": s["text"], "lang": s["lang"] or "",
                 "label": label or s["text"][:24], "segment_id": segment_id, "emotion": s.get("emotion") or ""})
    return db.update("models", model_id, {"meta": {**m["meta"], "references": refs}})


def set_reference_emotion(model_id: str, ref_id: str, emotion: str) -> dict:
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    refs = [dict(r) for r in (m["meta"] or {}).get("references", [])]
    ref = next((r for r in refs if r["id"] == ref_id), None)
    if ref is None:
        raise KeyError(ref_id)
    if emotion and not emotions.valid(emotion):
        raise ValueError(f"unknown emotion: {emotion}")
    ref["emotion"] = emotion or ""
    return db.update("models", model_id, {"meta": {**m["meta"], "references": refs}})


def remove_reference(model_id: str, ref_id: str) -> dict:
    """Only a registered reference can be removed, and only from inside the model's references folder."""
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    refs = (m["meta"] or {}).get("references", [])
    ref = next((r for r in refs if r["id"] == ref_id), None)
    if ref is None:
        raise KeyError(ref_id)
    root = (Path(m["path"]) / "references").resolve()
    target = (Path(m["path"]) / ref["file"]).resolve()
    if target.parent != root:
        raise ValueError("不合法的參考片段路徑")
    target.unlink(missing_ok=True)
    return db.update("models", model_id, {"meta": {**m["meta"], "references": [r for r in refs if r is not ref]}})


def _remember_speed(engine_id: str, preset_id: str, gpu: str, s_per_step: float) -> None:
    st = config.load_settings()
    speed = dict(st.get("speed") or {})
    speed[_speed_key(engine_id, preset_id, gpu)] = {"s_per_step": s_per_step, "at": db.now()}
    config.save_settings({"speed": speed})


def _save_log(tid: str, prefix: str, work: Path, loc: dict | None = None) -> None:
    try:
        work.mkdir(parents=True, exist_ok=True)
        (work / "train.log").write_text(runpod.get_text(f"{prefix}/train.log", loc=loc), encoding="utf-8")
    except Exception:
        pass


def _fraction(p: dict) -> float:
    """Overall cloud progress 0–1 across phases (training dominates)."""
    ph = p.get("phase")
    frac = (p.get("step", 0) / p["total"]) if p.get("total") else 0.0
    return {"setup": 0.02, "upload": 0.03, "unpack": 0.04, "download": 0.06, "prepare": 0.08}.get(ph) or \
        {"train": 0.1 + 0.75 * frac, "samples": 0.85 + 0.12 * frac, "package": 0.98}.get(ph, 0.0)


def _phase_label(p: dict) -> str:
    ph = p.get("phase")
    if ph == "setup":
        return "雲端安裝環境（第一次約 10 分鐘，之後會跳過）"
    if ph == "upload":
        return "環境已就緒，等資料上傳完"
    if ph == "unpack":
        return "解開資料"
    if ph == "download":
        return "下載基礎模型（第一次較久）"
    if ph == "prepare":
        return "預先處理音訊"
    if ph == "samples":
        return f"各檢查點試念樣本 {p.get('step', 0)}/{p.get('total', '?')}"
    if ph == "package":
        return "打包模型"
    if ph == "train" and p.get("total"):
        loss = f"，loss {p['loss']:.3f}" if isinstance(p.get("loss"), (int, float)) else ""
        eta = ""
        if p.get("s_per_step"):
            left = (p["total"] - p.get("step", 0)) * p["s_per_step"] / 60
            eta = f"，約剩 {left:.0f} 分"
        return f"訓練中 {p.get('step', 0)}/{p['total']}{loss}{eta}"
    return "雲端執行中"


def _stage_label(err: dict) -> str:
    return {"setup": "安裝環境", "upload": "等資料上傳（太久沒有上傳進度）", "unpack": "解開資料", "train": "訓練",
            "package": "打包",
            None: "逾時" if err.get("status") == "timeout" else "未知"}.get(err.get("stage"), err.get("stage") or "?")


def remove_model(model_id: str) -> None:
    m = db.get("models", model_id)
    if m:
        from . import tts
        tts.unload_if(model_id)
        shutil.rmtree(m["path"], ignore_errors=True)
        db.delete("models", model_id)

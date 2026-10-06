"""Training runs: cloud (RunPod) fine-tuning, the model registry and zero-shot (no training) models."""
from __future__ import annotations

import json
import shutil
import tarfile
import time
from pathlib import Path

from . import config, datasets, db, engines, evaluate, jobs  # noqa: F401  (evaluate registers evaluate_model)
from .cloud import runpod

BOOTSTRAP = (Path(__file__).parent / "cloud" / "bootstrap" / "bootstrap.sh").read_text(encoding="utf-8")


def _speed_key(engine_id: str, preset_id: str, gpu: str) -> str:
    return f"{engine_id}:{preset_id}:{gpu}"


def _require_consent(voice_id: str) -> None:
    """Consent is re-checked at every step that uses the voice: building, uploading, renting, synthesizing."""
    voice = db.get("voices", voice_id)
    if not voice or not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音目前沒有有效的同意紀錄（可能已撤回），已停止。")


def plan(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, usd_h: float | None = None,
         params: dict | None = None) -> dict:
    """What a run will use and roughly cost, shown before the user confirms. The parameters returned here are the
    exact ones that start() stores and the pod receives."""
    ds = db.get("datasets", dataset_id)
    if not ds:
        raise KeyError(dataset_id)
    eng = engines.get(engine_id)
    p = eng.preset(preset_id)
    gpu = gpu or p.gpu[0]
    usd_h = usd_h or runpod.GPUS.get(gpu, {}).get("usd_h", 1.5)
    st = config.load_settings()
    n_train = int(ds["meta"].get("n_train") or ds["n_items"])
    warnings, blocked = [], None
    try:
        eff = eng.effective_params(p.id, params, n_train)
    except ValueError as e:
        eff, blocked = {**p.params, **(params or {})}, str(e)
    measured = (st.get("speed") or {}).get(_speed_key(eng.id, p.id, gpu), {}).get("s_per_step")
    est = eng.estimate(ds["hours"], p.id, usd_h, n_train=n_train, s_per_step=measured, params=eff)
    limit = float(st.get("runpod_max_hours") or 12)
    if ds["hours"] < p.min_hours:
        warnings.append(f"這個設定建議至少 {p.min_hours:g} 小時已核可語音，目前只有 {ds['hours']:.2f} 小時。")
    if (eff.get("epochs_effective") or 0) > 3:
        warnings.append(f"實際會跑約 {eff['epochs_effective']} 個 epoch，資料少時容易「背答案」。")
    if est["hours"] > limit:
        warnings.append(f"預估時間超過你設定的上限 {limit:g} 小時，訓練會在上限時被強制停止。請到設定調高上限。")
    if not ds["meta"].get("reference_items") and not ds["meta"].get("reference"):
        warnings.append("資料集沒有 5–12 秒的參考片段，樣本比較會比較不準。")
    return {"engine": eng.id, "preset": p.id, "gpu": gpu, "usd_per_hour": usd_h, "data_hours": ds["hours"],
            "n_train": n_train, "steps": est["steps"], "epochs_effective": eff.get("epochs_effective"),
            "estimate_hours": est["hours"], "estimate_usd": est["usd"], "estimate_basis": est["basis"],
            "max_hours": limit, "max_usd": round(limit * usd_h, 2), "disk_gb": p.disk_gb, "ram_gb": p.ram_gb,
            "params": eff, "warnings": warnings, "blocked": blocked}


def start(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, name: str = "",
          params: dict | None = None, usd_h: float | None = None) -> dict:
    ds = db.get("datasets", dataset_id)
    _require_consent(ds["voice_id"])
    pl = plan(dataset_id, engine_id, preset_id, gpu, usd_h, params)
    if pl["blocked"]:
        raise ValueError(pl["blocked"])
    loc = runpod.location()
    tid = db.new_id("tr")
    db.insert("trainings", {"id": tid, "voice_id": ds["voice_id"], "dataset_id": dataset_id, "engine": engine_id,
                            "preset": {"id": pl["preset"], "params": pl["params"], "name": name},
                            "target": "runpod", "status": "queued", "gpu": pl["gpu"], "storage": loc,
                            "remote_prefix": f"vs/jobs/{tid}", "progress": {}, "cost_estimate": pl["estimate_usd"],
                            "created_at": db.now()})
    job = jobs.submit("cloud_train", {"training_id": tid}, message="準備上傳")
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
            elif tr.get("pod_state") == "creating":
                try:
                    for p in _find_pods(tid, _loc(tr)):
                        _remove_pod(tid, p.get("id"))
                except Exception:
                    _set(tid, pod_state="remove_failed")
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
        deadline = tr.get("deadline") or (tr["created_at"] + float(config.load_settings()["runpod_max_hours"]) * 3600)
        ctx.log(f"resuming watch of pod {pod_id}")
    else:
        # 1. package and upload
        _set(tid, status="uploading")
        ctx.progress(0.01, "整理訓練資料")
        tar_path, cfg = package_dataset(tid, work)
        runpod.put_text(f"{prefix}/config.json", json.dumps(cfg, ensure_ascii=False, indent=2), loc=loc)
        runpod.put_text(f"{prefix}/bootstrap.sh", BOOTSTRAP, loc=loc)
        for fname, text in eng.cloud_files().items():
            runpod.put_text(f"{prefix}/{fname}", text, loc=loc)
        runpod.upload(tar_path, f"{prefix}/dataset.tar", loc=loc,
                      progress=lambda f: ctx.progress(0.02 + 0.16 * f, f"上傳資料 {f * 100:.0f}%"))
        tar_path.unlink(missing_ok=True)
        ctx.check()
        _require_consent(tr["voice_id"])

        # 2. create the pod (intent and deadline are recorded first, so a lost response can be reconciled)
        max_h = float(config.load_settings().get("runpod_max_hours") or 12)
        deadline = time.time() + max_h * 3600 + 900
        _set(tid, status="starting", pod_state="creating", deadline=deadline, started_at=time.time())
        ctx.progress(0.19, "啟動雲端 GPU")
        env = {"VS_TRAINING_ID": tid, "VS_ENGINE": eng.id, "VS_MAX_SECONDS": str(int(max_h * 3600))}
        hf = config.get_secret("hf_token")
        if hf:
            env["HF_TOKEN"] = hf
        preset = eng.preset(tr["preset"]["id"])
        try:
            pod = runpod.create_pod(f"voice-studio-{tid}", eng.image, tr["gpu"], env,
                                    ["bash", "-c", f"bash /workspace/{prefix}/bootstrap.sh"], loc,
                                    container_disk_gb=preset.disk_gb, min_ram_gb=preset.ram_gb,
                                    min_vcpu=preset.vcpu)
        except Exception as e:
            time.sleep(10)
            for p in _find_pods(tid, loc):  # the request may have gone through even though we saw an error
                _remove_pod(tid, p.get("id"))
            _set(tid, pod_state="removed")
            raise RuntimeError(f"沒有租到 GPU：{str(e)[:300]}（這張卡在這個資料中心可能暫時沒貨，換一張試試）")
        pod_id = pod.get("id")
        gpu_actual = (pod.get("machine") or {}).get("gpuTypeId") or tr["gpu"]
        _set(tid, status="running", pod_id=pod_id, pod_state="running", gpu=gpu_actual,
             cost_per_hr=pod.get("costPerHr") or pod.get("adjustedCostPerHr"))
        ctx.log(f"pod {pod_id} created on {gpu_actual} at {pod.get('costPerHr')} /h")

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
            try:
                prog = runpod.get_json(f"{prefix}/progress.json", loc) or prog
                done = runpod.get_json(f"{prefix}/done.json", loc)
                err = runpod.get_json(f"{prefix}/error.json", loc)
                s3_errors = 0
            except Exception as e:  # network or storage hiccup: retry for ~10 minutes before giving up
                s3_errors += 1
                ctx.log(f"storage read failed ({s3_errors}): {e}")
                if s3_errors >= 20:
                    raise RuntimeError("連續 10 分鐘讀不到雲端儲存，已停止並關閉雲端機器。")
                continue
            _set(tid, progress={**prog, "wall_s": int(time.time() - (tr.get("started_at") or tr["created_at"]))})
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

    # 4. download and register
    _set(tid, status="downloading")
    tar_local = work / "model.tar"
    runpod.download(f"{prefix}/model.tar", tar_local, loc=loc,
                    progress=lambda f: ctx.progress(0.86 + 0.1 * f, f"下載模型 {f * 100:.0f}%"))
    samples_local = None
    if runpod.exists(f"{prefix}/samples.tar", loc):
        samples_local = runpod.download(f"{prefix}/samples.tar", work / "samples.tar", loc=loc,
                                        progress=lambda f: ctx.progress(0.96 + 0.03 * f, "下載樣本"))
    _save_log(tid, prefix, work, loc)
    m = install_model(tid, tar_local, samples_local)
    note = "樣本試念沒有完成：模型可以用，但沒有檢查點比較。" if partial or samples_local is None else ""
    _set(tid, status="done", finished_at=db.now(), note=note)
    for name in ("dataset.tar", "model.tar", "samples.tar"):  # keep the volume small; log and config stay
        try:
            runpod.delete(f"{prefix}/{name}", loc)
        except Exception:
            pass
    return {"model_id": m["id"], "message": "訓練完成，模型已下載，正在評分各檢查點"}


def resume_interrupted() -> list[str]:
    """At start-up: runs whose watcher died with the app are picked up again (the pod kept training); a run that
    was creating its pod is reconciled against RunPod's pod list; earlier runs are marked failed."""
    resumed = []
    for tr in db.query("SELECT * FROM trainings WHERE status IN ('queued','uploading','starting','running',"
                       "'downloading')"):
        j = db.get("jobs", tr["job_id"]) if tr.get("job_id") else None
        if j and j["status"] in ("queued", "running"):
            continue
        pod_id = tr.get("pod_id")
        if not pod_id and tr.get("pod_state") == "creating":
            try:
                found = _find_pods(tr["id"], _loc(tr))
            except Exception:
                found = []
            if len(found) == 1:
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
            _remove_pod(tr["id"], pod_id)
            _set(tr["id"], status="failed", finished_at=db.now(), note="程式關閉時中斷（還沒開始雲端訓練），請重新開始。")
    return resumed


def reap() -> dict:
    """The safety net outside the pod: retry removals that failed, and find studio pods with no live run."""
    removed, orphans = [], []
    for tr in db.query("SELECT * FROM trainings WHERE pod_state IN ('remove_failed','creating','running') "
                       "AND status IN ('done','failed','canceled')"):
        if tr.get("pod_id") and _remove_pod(tr["id"], tr["pod_id"]):
            removed.append(tr["pod_id"])
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


CHECKPOINT_NAME = __import__("re").compile(r"^[\w.-]{1,80}$")


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
    bad = [c.get("name") for c in emeta.get("checkpoints", []) if not CHECKPOINT_NAME.match(str(c.get("name", "")))]
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


def _copy_references(ds: dict, mdir: Path, limit: int = 3) -> list[dict]:
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
        out.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": it.get("text", ""),
                    "lang": it.get("lang", ""), "label": "資料集參考 " + str(k + 1), "segment_id": it.get("id")})
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
                     "label": (s["text"][:24] + "…") if len(s["text"]) > 24 else s["text"], "segment_id": sid})
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
                 "label": label or s["text"][:24], "segment_id": segment_id})
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
    return {"setup": 0.02, "unpack": 0.04, "download": 0.06, "prepare": 0.08}.get(ph) or \
        {"train": 0.1 + 0.75 * frac, "samples": 0.85 + 0.12 * frac, "package": 0.98}.get(ph, 0.0)


def _phase_label(p: dict) -> str:
    ph = p.get("phase")
    if ph == "setup":
        return "雲端安裝環境（第一次約 10 分鐘，之後會跳過）"
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
    return {"setup": "安裝環境", "unpack": "解開資料", "train": "訓練", "package": "打包",
            None: "逾時" if err.get("status") == "timeout" else "未知"}.get(err.get("stage"), err.get("stage") or "?")


def remove_model(model_id: str) -> None:
    m = db.get("models", model_id)
    if m:
        from . import tts
        tts.unload_if(model_id)
        shutil.rmtree(m["path"], ignore_errors=True)
        db.delete("models", model_id)

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


def plan(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, usd_h: float | None = None) -> dict:
    """What a run will use and roughly cost, shown before the user confirms."""
    ds = db.get("datasets", dataset_id)
    if not ds:
        raise KeyError(dataset_id)
    eng = engines.get(engine_id)
    p = eng.preset(preset_id)
    gpu = gpu or p.gpu[0]
    usd_h = usd_h or runpod.GPUS.get(gpu, {}).get("usd_h", 1.5)
    st = config.load_settings()
    measured = (st.get("speed") or {}).get(_speed_key(eng.id, p.id, gpu), {}).get("s_per_step")
    n_train = int(ds["meta"].get("n_train") or ds["n_items"])
    est = eng.estimate(ds["hours"], p.id, usd_h, n_train=n_train, s_per_step=measured)
    limit = float(st.get("runpod_max_hours") or 12)
    warnings = []
    if ds["hours"] < p.min_hours:
        warnings.append(f"這個設定建議至少 {p.min_hours:g} 小時已核可語音，目前只有 {ds['hours']:.2f} 小時。")
    if est["hours"] > limit:
        warnings.append(f"預估時間超過你設定的上限 {limit:g} 小時，訓練會在上限時被強制停止。請到設定調高上限。")
    if not ds["meta"].get("reference_items") and not ds["meta"].get("reference"):
        warnings.append("資料集沒有 5–12 秒的參考片段，樣本比較會比較不準。")
    return {"engine": eng.id, "preset": p.id, "gpu": gpu, "usd_per_hour": usd_h, "data_hours": ds["hours"],
            "n_train": n_train, "steps": est["steps"], "estimate_hours": est["hours"], "estimate_usd": est["usd"],
            "estimate_basis": est["basis"], "max_hours": limit, "max_usd": round(limit * usd_h, 2),
            "disk_gb": p.disk_gb, "warnings": warnings}


def start(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, name: str = "",
          params: dict | None = None, usd_h: float | None = None) -> dict:
    ds = db.get("datasets", dataset_id)
    voice = db.get("voices", ds["voice_id"])
    if not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音的同意紀錄不完整，不能訓練。")
    eng = engines.get(engine_id)
    pl = plan(dataset_id, engine_id, preset_id, gpu, usd_h)
    tid = db.new_id("tr")
    db.insert("trainings", {"id": tid, "voice_id": voice["id"], "dataset_id": dataset_id, "engine": engine_id,
                            "preset": {"id": pl["preset"], "params": {**eng.preset(preset_id).params, **(params or {})},
                                       "name": name},
                            "target": "runpod", "status": "queued", "gpu": pl["gpu"],
                            "remote_prefix": f"vs/jobs/{tid}", "progress": {}, "cost_estimate": pl["estimate_usd"],
                            "created_at": db.now()})
    job = jobs.submit("cloud_train", {"training_id": tid}, message="準備上傳")
    return db.update("trainings", tid, {"job_id": job["id"]})


def _set(tid: str, **kw) -> None:
    db.update("trainings", tid, kw)


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


@jobs.handler("cloud_train", queue="io")
def cloud_train(ctx: jobs.JobContext) -> dict:
    """Upload → pod → watch → download. Whatever goes wrong, the training row ends in a final state and no pod is
    left running."""
    tid = ctx.params["training_id"]
    try:
        return _cloud_train(ctx)
    except BaseException as e:
        tr = db.get("trainings", tid)
        if tr and tr["status"] not in ("done", "failed", "canceled"):
            if tr.get("pod_id"):
                try:
                    runpod.remove_pod(tr["pod_id"])
                except Exception:
                    pass
            _set(tid, status="canceled" if isinstance(e, jobs.Cancelled) else "failed", finished_at=db.now())
        raise


def _cloud_train(ctx: jobs.JobContext) -> dict:
    tid = ctx.params["training_id"]
    tr = db.get("trainings", tid)
    eng = engines.get(tr["engine"])
    st = config.load_settings()
    prefix = tr["remote_prefix"]
    work = config.DATA / "jobs" / tid
    work.mkdir(parents=True, exist_ok=True)

    resume = bool(ctx.params.get("resume") and tr.get("pod_id"))
    if resume:  # the studio was closed while the pod kept working: pick the run up again
        pod_id = tr["pod_id"]
        gpu_name = (tr.get("progress") or {}).get("gpu_name") or tr["gpu"]
        ctx.log(f"resuming watch of pod {pod_id}")
    else:
        # 1. package and upload
        _set(tid, status="uploading")
        ctx.progress(0.01, "整理訓練資料")
        tar_path, cfg = package_dataset(tid, work)
        runpod.put_text(f"{prefix}/config.json", json.dumps(cfg, ensure_ascii=False, indent=2))
        runpod.put_text(f"{prefix}/bootstrap.sh", BOOTSTRAP)
        for fname, text in eng.cloud_files().items():
            runpod.put_text(f"{prefix}/{fname}", text)
        runpod.upload(tar_path, f"{prefix}/dataset.tar",
                      progress=lambda f: ctx.progress(0.02 + 0.16 * f, f"上傳資料 {f * 100:.0f}%"))
        tar_path.unlink(missing_ok=True)
        ctx.check()

        # 2. create the pod
        _set(tid, status="starting")
        ctx.progress(0.19, "啟動雲端 GPU")
        max_h = float(st.get("runpod_max_hours") or 12)
        env = {"VS_TRAINING_ID": tid, "VS_ENGINE": eng.id, "VS_MAX_SECONDS": str(int(max_h * 3600))}
        hf = config.get_secret("hf_token")
        if hf:
            env["HF_TOKEN"] = hf
        preset = eng.preset(tr["preset"]["id"])
        gpus = [tr["gpu"]] + [g for g in preset.gpu if g != tr["gpu"]]
        pod = runpod.create_pod(f"voice-studio-{tid}", eng.image, gpus, env,
                                ["bash", "-c", f"bash /workspace/{prefix}/bootstrap.sh"],
                                container_disk_gb=preset.disk_gb)
        pod_id = pod.get("id")
        gpu_name = (pod.get("machine") or {}).get("gpuDisplayName") or tr["gpu"]
        _set(tid, status="running", pod_id=pod_id)
        ctx.log(f"pod {pod_id} created on {gpu_name}")

    # 3. watch
    max_h = float(st.get("runpod_max_hours") or 12)
    started = tr["created_at"] if resume else time.time()
    last_poll = 0.0
    prog: dict = {}
    try:
        while True:
            ctx.check()
            time.sleep(5)
            if time.time() - last_poll < 30:
                continue
            last_poll = time.time()
            prog = runpod.get_json(f"{prefix}/progress.json") or prog
            done = runpod.get_json(f"{prefix}/done.json")
            err = runpod.get_json(f"{prefix}/error.json")
            _set(tid, progress={**prog, "wall_s": int(time.time() - started), "gpu_name": gpu_name})
            ctx.progress(0.2 + 0.65 * _fraction(prog), _phase_label(prog))
            if done:
                break
            if err:
                raise RuntimeError(f"雲端訓練失敗（{_stage_label(err)}）。請到「雲端訓練」看紀錄。")
            if time.time() - started > max_h * 3600 + 900:
                raise RuntimeError("超過最長時數，已強制停止。")
            if runpod.get_pod(pod_id) is None and not runpod.get_json(f"{prefix}/done.json"):
                raise RuntimeError("雲端機器意外消失（可能被平台回收）。可以重試。")
    except jobs.Cancelled:
        runpod.remove_pod(pod_id)
        _set(tid, status="canceled", finished_at=db.now())
        _save_log(tid, prefix, work)
        raise
    except Exception:
        runpod.remove_pod(pod_id)
        _set(tid, status="failed", finished_at=db.now())
        _save_log(tid, prefix, work)
        raise
    runpod.remove_pod(pod_id)  # in case the pod did not remove itself
    _set(tid, status="downloading")
    if prog.get("s_per_step"):
        _remember_speed(eng.id, tr["preset"]["id"], tr["gpu"], float(prog["s_per_step"]))

    # 4. download and register
    tar_local = work / "model.tar"
    runpod.download(f"{prefix}/model.tar", tar_local,
                    progress=lambda f: ctx.progress(0.86 + 0.12 * f, f"下載模型 {f * 100:.0f}%"))
    _save_log(tid, prefix, work)
    m = install_model(tid, tar_local)
    _set(tid, status="done", finished_at=db.now())
    for name in ("dataset.tar", "model.tar"):  # keep the volume small; the log and config stay for reference
        try:
            runpod.delete_prefix(f"{prefix}/{name}")
        except Exception:
            pass
    return {"model_id": m["id"], "message": "訓練完成，模型已下載，正在評分各檢查點"}


def resume_interrupted() -> list[str]:
    """At start-up: runs whose watcher died with the app are picked up again (the pod kept training);
    runs interrupted before their pod existed are marked failed."""
    resumed = []
    for tr in db.query("SELECT * FROM trainings WHERE status IN ('queued','uploading','starting','running',"
                       "'downloading')"):
        j = db.get("jobs", tr["job_id"]) if tr.get("job_id") else None
        if j and j["status"] in ("queued", "running"):
            continue
        if tr["status"] in ("running", "downloading") and tr.get("pod_id"):
            job = jobs.submit("cloud_train", {"training_id": tr["id"], "resume": True}, "重新連上雲端訓練")
            _set(tr["id"], job_id=job["id"])
            resumed.append(tr["id"])
        else:
            if tr.get("pod_id"):
                try:
                    runpod.remove_pod(tr["pod_id"])
                except Exception:
                    pass
            _set(tr["id"], status="failed", finished_at=db.now())
    return resumed


def install_model(tid: str, tar_local: Path) -> dict:
    """Unpack model.tar into data/models/<id>, register it and queue checkpoint scoring."""
    tr = db.get("trainings", tid)
    ds = db.get("datasets", tr["dataset_id"])
    eng = engines.get(tr["engine"])
    model_id = db.new_id("mdl")
    mdir = config.DATA / "models" / model_id
    tmp = config.DATA / "tmp" / f"unpack-{model_id}"
    with tarfile.open(tar_local) as t:
        t.extractall(tmp, filter="data")
    shutil.move(str(tmp / "model"), str(mdir))
    shutil.rmtree(tmp, ignore_errors=True)
    tar_local.unlink(missing_ok=True)
    refs = _copy_references(ds, mdir)
    voice = db.get("voices", tr["voice_id"])
    emeta = eng.model_meta(mdir)
    cks = [c for c in emeta.get("checkpoints", []) if c.get("weights")]
    m = db.insert("models", {
        "id": model_id, "voice_id": voice["id"], "engine": eng.id,
        "name": tr["preset"].get("name") or f"{voice['name']} · {eng.name} · {eng.preset(tr['preset']['id']).label}",
        "training_id": tid, "path": str(mdir),
        "meta": {"dataset_id": ds["id"], "preset": tr["preset"], "consent": ds["meta"].get("consent"),
                 "mode": emeta.get("mode"), "checkpoint": cks[-1]["name"] if cks else None, "references": refs,
                 "languages": ds["meta"].get("languages", [])},
        "metrics": {}, "created_at": db.now()})
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
    m = db.get("models", model_id)
    refs = [r for r in m["meta"].get("references", []) if r["id"] != ref_id]
    (Path(m["path"]) / "references" / f"{ref_id}.wav").unlink(missing_ok=True)
    return db.update("models", model_id, {"meta": {**m["meta"], "references": refs}})


def _remember_speed(engine_id: str, preset_id: str, gpu: str, s_per_step: float) -> None:
    st = config.load_settings()
    speed = dict(st.get("speed") or {})
    speed[_speed_key(engine_id, preset_id, gpu)] = {"s_per_step": s_per_step, "at": db.now()}
    config.save_settings({"speed": speed})


def _save_log(tid: str, prefix: str, work: Path) -> None:
    try:
        (work / "train.log").write_text(runpod.get_text(f"{prefix}/train.log"), encoding="utf-8")
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

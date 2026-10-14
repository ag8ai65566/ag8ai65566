"""Engines, cloud checks, training runs and trained models."""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .. import config, datasets, db, engines, jobs, training, tts
from ..cloud import colab, runpod

router = APIRouter(prefix="/api", tags=["train"])


@router.get("/engines")
def list_engines():
    return [e.info() for e in engines.all_engines()]


@router.post("/engines/{engine_id}/install")
def install_engine(engine_id: str):
    try:
        engines.get(engine_id)
    except KeyError:
        raise HTTPException(404)
    active = db.query("SELECT * FROM jobs WHERE kind='install_engine' AND status IN ('queued','running')")
    if active:
        return active[0]
    return jobs.submit("install_engine", {"engine": engine_id}, f"安裝 {engines.get(engine_id).name}")


@router.get("/cloud/check")
def cloud_check():
    try:
        return runpod.check()
    except runpod.RunPodError as e:
        return {"ok": False, "error": str(e)}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}


@router.get("/cloud/gpus")
def cloud_gpus():
    st = config.load_settings()
    try:
        return runpod.gpu_catalog(st.get("runpod_datacenter") or None)
    except runpod.RunPodError:
        return [{"id": k, **v, "availability": None} for k, v in runpod.GPUS.items()]


@router.get("/cloud/datacenters")
def cloud_datacenters():
    return runpod.S3_DATACENTERS


class PlanIn(BaseModel):
    dataset_id: str
    engine: str
    preset: str
    gpu: str | None = None
    name: str = ""
    params: dict | None = None
    usd_h: float | None = None
    target: str = "runpod"   # runpod | colab


@router.post("/training/plan")
def training_plan(body: PlanIn):
    if body.target not in ("runpod", "colab"):
        raise HTTPException(400, "target")
    try:
        return training.plan(body.dataset_id, body.engine, body.preset, body.gpu, body.usd_h, body.params,
                             body.target)
    except KeyError:
        raise HTTPException(404, "找不到資料集或引擎")


@router.post("/training")
def training_start(body: PlanIn):
    try:
        if body.target not in ("runpod", "colab"):
            raise ValueError("target")
        return training.start(body.dataset_id, body.engine, body.preset, body.gpu, body.name, body.params,
                              body.usd_h, body.target)
    except datasets.ConsentMissing as e:
        raise HTTPException(409, str(e))
    except (ValueError, runpod.RunPodError) as e:
        raise HTTPException(400, str(e))


@router.post("/training/{tid}/recover")
def training_recover(tid: str):
    """Download the weights of a run that failed after it had already saved them."""
    t = db.get("trainings", tid)
    if not t:
        raise HTTPException(404)
    if t["status"] not in ("failed", "canceled"):
        raise HTTPException(400, "只有失敗或取消的訓練需要救回")
    if not training.recoverable(t):
        raise HTTPException(404, "雲端沒有這次訓練的模型檔（訓練沒有進行到存檔）")
    if t.get("target") == "colab":
        job = jobs.submit("colab_install", {"training_id": tid, "partial": True}, "從雲端硬碟取回模型")
        training._set(tid, status="downloading", job_id=job["id"])
        return job
    return jobs.submit("recover_model", {"training_id": tid}, "救回模型")


@router.post("/cloud/reap")
def cloud_reap():
    """Retry failed pod removals and list studio pods that no running training owns."""
    return training.reap()


@router.post("/cloud/pods/{pod_id}/remove")
def cloud_remove_pod(pod_id: str):
    try:
        runpod.remove_pod(pod_id)
    except runpod.RunPodError as e:
        raise HTTPException(502, str(e))
    return {"ok": True}


@router.get("/training")
def training_list():
    out = db.query("SELECT * FROM trainings ORDER BY created_at DESC")
    for t in out:
        j = db.get("jobs", t["job_id"]) if t.get("job_id") else None
        t["job"] = {k: j[k] for k in ("status", "progress", "message")} if j else None
        if t.get("target") == "colab" and t["status"] in ("waiting", "running"):
            p = t.get("progress") or {}
            t["phase"] = {"label": training._phase_label(p) if p.get("phase") else
                          ("Colab 已接手，準備中" if t["status"] == "running" else "等你在 Colab 執行筆記本"),
                          "fraction": training._fraction(p)}
            t["colab_path"] = f"{(t.get('storage') or {}).get('folder', 'VoiceStudio')}/{colab.NOTEBOOK_NAME}"
    return out


@router.get("/training/{tid}")
def training_get(tid: str):
    t = db.get("trainings", tid)
    if not t:
        raise HTTPException(404)
    log = config.DATA / "jobs" / tid / "train.log"
    t["log"] = log.read_text(encoding="utf-8")[-20000:] if log.exists() else ""
    if not t["log"] and t.get("target") == "colab":
        try:
            t["log"] = (colab.job_dir(t) / "train.log").read_text(encoding="utf-8", errors="replace")[-20000:]
        except Exception:
            pass
    elif not t["log"] and t["status"] in ("running", "starting"):
        try:
            t["log"] = runpod.get_text(f"{t['remote_prefix']}/train.log", tail=20000, loc=t.get("storage") or None)
        except Exception:
            pass
    return t


@router.post("/training/{tid}/cancel")
def training_cancel(tid: str):
    t = db.get("trainings", tid)
    if t and t.get("job_id"):
        jobs.cancel(t["job_id"])
    if t and t.get("pod_id"):
        training._remove_pod(tid, t["pod_id"])
    if t and t.get("target") == "colab" and t["status"] not in ("done", "failed", "canceled"):
        colab.cancel(t)  # the runner on Colab sees cancel.json within 30 s and stops
        training._set(tid, status="canceled", finished_at=db.now())
    return {"ok": True}


# --- Google Colab --------------------------------------------------------------------------------------------------

@router.get("/colab/status")
def colab_status():
    return colab.status()


class ColabSetup(BaseModel):
    drive_root: str
    folder: str = "VoiceStudio"


@router.post("/colab/setup")
def colab_setup(body: ColabSetup):
    """Remember the synced "My Drive" folder and put the notebook and runner into <folder> there."""
    name = body.folder.strip().strip("/\\") or "VoiceStudio"
    if any(c in name for c in '\\/:*?"<>|'):
        raise HTTPException(400, "資料夾名稱不能有 \\ / : * ? \" < > |")
    if not Path(body.drive_root.strip()).is_dir():
        raise HTTPException(400, f"找不到 {body.drive_root}。Google 雲端硬碟電腦版有沒有開著？")
    st = config.save_settings({"colab_drive_root": body.drive_root.strip(), "colab_folder": name})
    try:
        colab.install_files(st)
    except (colab.ColabError, OSError) as e:
        raise HTTPException(400, str(e))
    return colab.status()


def _model_view(m: dict) -> dict:
    eng = engines.get(m["engine"]) if m["engine"] in engines.REGISTRY else None
    emeta = eng.model_meta(Path(m["path"])) if eng else {}
    m["engine_name"] = eng.name if eng else m["engine"]
    m["modes"] = eng.modes(emeta) if eng else []
    m["checkpoints"] = emeta.get("checkpoints", [])
    m["samples"] = emeta.get("samples") or {}
    m["train_seconds"] = emeta.get("train_seconds")
    m["available"] = list(eng.available()) if eng else [False, "未知引擎"]
    return m


@router.get("/models")
def list_models(voice_id: str = ""):
    q = "SELECT * FROM models" + (" WHERE voice_id=?" if voice_id else "") + " ORDER BY created_at DESC"
    out = db.query(q, (voice_id,) if voice_id else ())
    names = {v["id"]: v["name"] for v in db.query("SELECT id, name FROM voices")}
    for m in out:
        m["voice_name"] = names.get(m["voice_id"], "?")
        _model_view(m)
    return out


@router.get("/models/{model_id}")
def get_model(model_id: str):
    m = db.get("models", model_id)
    if not m:
        raise HTTPException(404)
    v = db.get("voices", m["voice_id"])
    m["voice_name"] = v["name"] if v else "?"
    return _model_view(m)


class ModelPatch(BaseModel):
    name: str | None = None
    checkpoint: str | None = None
    notes: str | None = None


@router.patch("/models/{model_id}")
def patch_model(model_id: str, body: ModelPatch):
    m = db.get("models", model_id)
    if not m:
        raise HTTPException(404)
    upd: dict = {}
    if body.name is not None:
        upd["name"] = body.name.strip() or m["name"]
    meta = dict(m["meta"] or {})
    if body.checkpoint is not None:
        names = [c["name"] for c in get_model(model_id)["checkpoints"] if c.get("weights")]
        if body.checkpoint not in names:
            raise HTTPException(400, "這個檢查點沒有下載權重")
        meta.update(checkpoint=body.checkpoint, checkpoint_chosen_by_user=True)
        tts.unload_if(model_id)
    if body.notes is not None:
        meta["notes"] = body.notes
    upd["meta"] = meta
    return db.update("models", model_id, upd)


@router.delete("/models/{model_id}")
def delete_model(model_id: str):
    training.remove_model(model_id)
    return {"ok": True}


@router.post("/models/{model_id}/evaluate")
def evaluate_model(model_id: str):
    if not db.get("models", model_id):
        raise HTTPException(404)
    return jobs.submit("evaluate_model", {"model_id": model_id}, "評分檢查點")


def _safe_file(root: Path, rel: str) -> Path:
    f = (root / rel).resolve()
    if root.resolve() not in f.parents or not f.is_file():
        raise HTTPException(404)
    return f


@router.get("/models/{model_id}/samples/{name}/{file}")
def model_sample(model_id: str, name: str, file: str):
    m = db.get("models", model_id)
    if not m:
        raise HTTPException(404)
    return FileResponse(_safe_file(Path(m["path"]), f"samples/{name}/{file}"), media_type="audio/wav")


@router.get("/models/{model_id}/references/{ref_id}/audio")
def model_reference_audio(model_id: str, ref_id: str):
    m = db.get("models", model_id)
    if not m:
        raise HTTPException(404)
    return FileResponse(_safe_file(Path(m["path"]), f"references/{ref_id}.wav"), media_type="audio/wav")


class RefIn(BaseModel):
    segment_id: str
    label: str = ""


@router.post("/models/{model_id}/references")
def add_reference(model_id: str, body: RefIn):
    try:
        return training.add_reference(model_id, body.segment_id, body.label)
    except KeyError:
        raise HTTPException(404)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.patch("/models/{model_id}/references/{ref_id}")
def patch_reference(model_id: str, ref_id: str, body: dict):
    try:
        return training.set_reference_emotion(model_id, ref_id, body.get("emotion") or "")
    except KeyError:
        raise HTTPException(404)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.delete("/models/{model_id}/references/{ref_id}")
def delete_reference(model_id: str, ref_id: str):
    try:
        return training.remove_reference(model_id, ref_id)
    except KeyError:
        raise HTTPException(404)
    except ValueError as e:
        raise HTTPException(400, str(e))


class ZeroShotIn(BaseModel):
    voice_id: str
    engine: str
    segment_ids: list[str]
    name: str = ""


@router.post("/models/zeroshot")
def create_zeroshot(body: ZeroShotIn):
    try:
        return training.create_zeroshot(body.voice_id, body.engine, body.segment_ids, body.name)
    except datasets.ConsentMissing as e:
        raise HTTPException(409, str(e))
    except (KeyError, ValueError) as e:
        raise HTTPException(400, str(e))


@router.post("/models/demo")
def create_demo_model():
    """A model for the test engine, so the TTS pages can be tried before any real training."""
    v = db.query("SELECT * FROM voices ORDER BY created_at LIMIT 1")
    vid = v[0]["id"] if v else None
    if vid is None:
        v = db.insert("voices", {"id": db.new_id("voice"), "name": "示範聲音", "kind": "designed",
                                 "languages": ["ja", "en"], "notes": "測試用", "enrollment": [], "created_at": db.now()})
        vid = v["id"]
    mid = db.new_id("mdl")
    d = config.DATA / "models" / mid
    d.mkdir(parents=True, exist_ok=True)
    return db.insert("models", {"id": mid, "voice_id": vid, "engine": "mock", "name": "測試模型（哼聲）",
                                "path": str(d), "meta": {"mode": "mock"}, "metrics": {}, "created_at": db.now()})

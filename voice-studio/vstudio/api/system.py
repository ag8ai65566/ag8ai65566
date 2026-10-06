"""Jobs, settings, secrets and machine status."""
from __future__ import annotations

import platform
import shutil

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import __version__, config, db, jobs

router = APIRouter(prefix="/api", tags=["system"])


@router.get("/system")
def system():
    gpu = {"available": False}
    try:
        import torch
        if torch.cuda.is_available():
            p = torch.cuda.get_device_properties(0)
            free, total = torch.cuda.mem_get_info()
            gpu = {"available": True, "name": p.name, "vram_gb": round(total / 2 ** 30, 1),
                   "free_gb": round(free / 2 ** 30, 1), "torch": torch.__version__, "cuda": torch.version.cuda}
        else:
            gpu["torch"] = torch.__version__
    except Exception:
        gpu["note"] = "PyTorch 未安裝（只能用測試引擎）"
    du = shutil.disk_usage(config.DATA)
    counts = {t: db.connect().execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
              for t in ("voices", "sources", "segments", "datasets", "models", "outputs")}
    return {"version": __version__, "python": platform.python_version(), "os": platform.platform(), "gpu": gpu,
            "disk_free_gb": round(du.free / 2 ** 30, 1), "data_dir": str(config.DATA), "counts": counts}


@router.get("/jobs")
def list_jobs(limit: int = 50, active: bool = False):
    if active:
        return db.query("SELECT * FROM jobs WHERE status IN ('queued','running') ORDER BY created_at")
    return db.query("SELECT * FROM jobs ORDER BY created_at DESC LIMIT ?", (limit,))


@router.get("/jobs/{job_id}")
def get_job(job_id: str):
    j = db.get("jobs", job_id)
    if not j:
        raise HTTPException(404)
    log = config.DATA / "jobs" / f"{job_id}.log"
    j["log"] = log.read_text(encoding="utf-8")[-20000:] if log.exists() else ""
    return j


@router.post("/jobs/{job_id}/cancel")
def cancel_job(job_id: str):
    return jobs.cancel(job_id)


@router.post("/jobs/{job_id}/retry")
def retry_job(job_id: str):
    return jobs.retry(job_id)


@router.get("/settings")
def get_settings():
    return {"settings": config.load_settings(), "secrets": config.secret_status()}


@router.put("/settings")
def put_settings(body: dict):
    return {"settings": config.save_settings(body), "secrets": config.secret_status()}


class SecretIn(BaseModel):
    name: str
    value: str | None = None


@router.put("/secrets")
def put_secret(body: SecretIn):
    """Store a key in the OS credential store. The value is never sent back to the browser."""
    if body.name not in config.SECRET_NAMES:
        raise HTTPException(400, "unknown secret")
    ok = config.set_secret(body.name, (body.value or "").strip() or None)
    if not ok:
        raise HTTPException(500, "無法寫入系統的認證儲存區（Windows 認證管理員）。")
    return config.secret_status()

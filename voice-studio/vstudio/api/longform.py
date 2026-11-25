"""Long-form speech on a rented cloud GPU (see cloud_tts)."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import cloud_tts, datasets, db

router = APIRouter(prefix="/api/cloud-tts", tags=["cloud-tts"])

MAX_CHARS = 400_000  # about 60,000 English words: far past one sitting, still a few hundred kB


class Render(BaseModel):
    model_id: str
    text: str
    gpu: str | None = None
    tts_mode: str = "plain"
    ref_id: str | None = None
    language: str | None = None
    name: str = ""


def _check(body: Render) -> None:
    if len(body.text) > MAX_CHARS:
        raise HTTPException(400, f"文字太長（{len(body.text):,} 字元，上限 {MAX_CHARS:,}），請分成幾次。")
    if body.tts_mode not in ("plain", "ref", "hifi"):
        raise HTTPException(400, "不認得的合成模式")


def _view(r: dict) -> dict:
    p = dict(r.get("params") or {})
    text = p.pop("text", "")
    p["preview"] = text[:160]
    p["chars"] = len(text)
    out = db.get("outputs", r["output_id"]) if r.get("output_id") else None
    j = db.get("jobs", r["job_id"]) if r.get("job_id") else None
    return {**r, "params": p, "output": {"id": out["id"], "duration": out["duration"]} if out else None,
            "active": r["status"] in cloud_tts.ACTIVE,
            "job": {"status": j["status"], "progress": j["progress"], "message": j["message"]} if j else None}


@router.post("/plan")
def plan(body: Render):
    _check(body)
    try:
        return cloud_tts.plan(body.model_id, body.text, body.gpu, body.tts_mode, body.ref_id, body.language)
    except KeyError:
        raise HTTPException(404, "找不到這個模型")
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.post("")
def start(body: Render):
    _check(body)
    try:
        return _view(cloud_tts.start(body.model_id, body.text, body.gpu, body.tts_mode, body.ref_id, body.language,
                                     body.name))
    except KeyError:
        raise HTTPException(404, "找不到這個模型")
    except datasets.ConsentMissing as e:
        raise HTTPException(403, str(e))
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("")
def list_runs():
    return [_view(r) for r in db.query("SELECT * FROM cloud_renders ORDER BY created_at DESC")]


@router.get("/{rid}")
def get_run(rid: str):
    r = db.get("cloud_renders", rid)
    if not r:
        raise HTTPException(404)
    v = _view(r)
    v["text"] = (r.get("params") or {}).get("text", "")
    return v


@router.get("/{rid}/log")
def log(rid: str):
    try:
        return {"log": cloud_tts.log_tail(rid)}
    except KeyError:
        raise HTTPException(404)


@router.post("/{rid}/cancel")
def cancel(rid: str):
    try:
        return _view(cloud_tts.cancel(rid))
    except KeyError:
        raise HTTPException(404)


@router.post("/{rid}/resume")
def resume(rid: str):
    try:
        return _view(cloud_tts.resume(rid))
    except KeyError:
        raise HTTPException(404)
    except datasets.ConsentMissing as e:
        raise HTTPException(403, str(e))
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.delete("/{rid}")
def delete(rid: str):
    try:
        return cloud_tts.delete(rid)
    except KeyError:
        raise HTTPException(404)
    except ValueError as e:
        raise HTTPException(409, str(e))
    except RuntimeError as e:
        raise HTTPException(502, str(e))

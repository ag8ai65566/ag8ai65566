"""Catchphrases of a voice: spellings, original recordings, and how a model says them."""
from __future__ import annotations

import shutil
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .. import config, db, jobs, phrases

router = APIRouter(prefix="/api", tags=["phrases"])


def _call(fn, *a, **kw):
    try:
        return fn(*a, **kw)
    except KeyError:
        raise HTTPException(404)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("/voices/{voice_id}/phrases")
def list_phrases(voice_id: str, counts: bool = True):
    counts = phrases.counts(voice_id) if counts else {}
    return [{**p, "counts": counts.get(p["id"], {})} for p in phrases.list_for_voice(voice_id)]


class PhraseIn(BaseModel):
    text: str
    variants: list[str] = []
    lang: str | None = None


@router.post("/voices/{voice_id}/phrases")
def create_phrase(voice_id: str, body: PhraseIn):
    return _call(phrases.create, voice_id, body.text, body.variants, body.lang)


class PhrasePatch(BaseModel):
    text: str | None = None
    variants: list[str] | None = None
    lang: str | None = None


@router.patch("/phrases/{pid}")
def patch_phrase(pid: str, body: PhrasePatch):
    return _call(phrases.update, pid, body.text, body.variants, body.lang)


@router.delete("/phrases/{pid}")
def delete_phrase(pid: str):
    _call(phrases.delete, pid)
    return {"ok": True}


@router.post("/phrases/{pid}/clips")
async def add_clip(pid: str, file: UploadFile | None = File(None), segment_id: str = Form(""),
                   start: float = Form(0.0), end: float = Form(0.0), emotion: str = Form("")):
    """An original recording of the phrase: an uploaded file, or a range cut out of an imported segment."""
    if file is not None and file.filename:
        tmp = config.path("tmp", f"{db.new_id('up')}{Path(file.filename).suffix[:8]}")
        try:
            with open(tmp, "wb") as fh:
                shutil.copyfileobj(file.file, fh)
            return _call(phrases.add_clip_file, pid, tmp, emotion or None, file.filename)
        finally:
            tmp.unlink(missing_ok=True)
    if segment_id:
        return _call(phrases.add_clip_segment, pid, segment_id, start, end, emotion or None)
    raise HTTPException(400, "請上傳檔案，或選一段片段")


@router.patch("/phrases/{pid}/clips/{cid}")
def patch_clip(pid: str, cid: str, body: dict):
    return _call(phrases.set_clip_emotion, pid, cid, body.get("emotion") or "")


@router.delete("/phrases/{pid}/clips/{cid}")
def delete_clip(pid: str, cid: str):
    return _call(phrases.remove_clip, pid, cid)


@router.get("/phrases/{pid}/clips/{cid}/audio")
def clip_audio(pid: str, cid: str):
    f = _call(lambda: phrases.clip_path(phrases.get(pid), cid))
    if not f.is_file():
        raise HTTPException(404)
    return FileResponse(f, media_type="audio/wav")


@router.post("/phrases/{pid}/unify")
def unify_one(pid: str):
    ph = _call(phrases.get, pid)
    return {"changed": phrases.unify(ph["voice_id"], pid)}


@router.post("/voices/{voice_id}/phrases/unify")
def unify_all(voice_id: str):
    return {"changed": phrases.unify(voice_id)}


@router.post("/voices/{voice_id}/phrases/check")
def check(voice_id: str, body: dict):
    m = db.get("models", body.get("model_id") or "")
    if not m or m["voice_id"] != voice_id:
        raise HTTPException(400, "請選這個聲音的模型")
    if not phrases.list_for_voice(voice_id):
        raise HTTPException(400, "還沒有口頭禪")
    return jobs.submit("check_phrases", {"model_id": m["id"]}, "檢查口頭禪念法")

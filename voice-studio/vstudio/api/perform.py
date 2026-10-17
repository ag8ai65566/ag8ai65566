"""照著念: a recording to follow, its phrases (editable), and renders with a trained voice."""
from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np
from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel

from .. import db, emotions, jobs, perform

router = APIRouter(prefix="/api/perform", tags=["perform"])


def _get(pid: str) -> dict:
    rec = db.get("performances", pid)
    if not rec:
        raise HTTPException(404)
    return rec


def _view(rec: dict) -> dict:
    jobs_of = db.query("SELECT id, kind, status, progress, message FROM jobs WHERE kind IN ('perform_analyze', "
                       "'perform_render') AND params LIKE ? ORDER BY created_at DESC LIMIT 1", (f'%"{rec["id"]}"%',))
    for p in rec.get("phrases") or []:
        p["labels"] = perform.phrase_tags(p)
    return {**rec, "job": jobs_of[0] if jobs_of else None}


@router.get("")
def list_performances():
    return [_view(r) for r in db.query("SELECT * FROM performances ORDER BY created_at DESC")]


@router.post("")
async def create(file: UploadFile = File(...), language: str = Form(""), separate: bool = Form(False),
                 name: str = Form("")):
    pid = db.new_id("perf")
    d = perform.folder(pid)
    d.mkdir(parents=True, exist_ok=True)
    src = d / f"upload{Path(file.filename or 'a.wav').suffix.lower()[:8]}"
    with open(src, "wb") as fh:
        shutil.copyfileobj(file.file, fh, length=8 << 20)
    rec = db.insert("performances", {"id": pid, "name": (name or Path(file.filename or "錄音").stem)[:80],
                                     "path": str(src), "lang": language if language in ("ja", "en", "zh") else None,
                                     "status": "analyzing", "phrases": [], "params": {}, "result": {},
                                     "meta": {"copied": True, "filename": file.filename}, "created_at": db.now()})
    job = jobs.submit("perform_analyze", {"perform_id": pid, "separate": separate}, "排隊分析")
    return {**rec, "job": job}


@router.get("/{pid}")
def get_one(pid: str):
    return _view(_get(pid))


class PhraseEdit(BaseModel):
    i: int
    text: str | None = None
    emotion: str | None = None
    style: str | None = None
    pause: float | None = None
    skip: bool | None = None


class PerformPatch(BaseModel):
    name: str | None = None
    phrases: list[PhraseEdit] = []


@router.patch("/{pid}")
def patch(pid: str, body: PerformPatch):
    rec = _get(pid)
    items = {p["i"]: p for p in rec["phrases"]}
    for e in body.phrases:
        p = items.get(e.i)
        if p is None:
            raise HTTPException(400, f"沒有第 {e.i + 1} 句")
        if e.emotion is not None and e.emotion and not emotions.valid(e.emotion):
            raise HTTPException(400, f"unknown emotion: {e.emotion}")
        for k in ("text", "emotion", "style", "skip"):
            if getattr(e, k) is not None:
                p[k] = getattr(e, k)
        if e.pause is not None:
            p["pause"] = round(min(5.0, max(0.0, e.pause)), 2)
    upd: dict = {"phrases": list(items.values())}
    if body.name:
        upd["name"] = body.name[:80]
    return _view(db.update("performances", pid, upd))


class RenderIn(BaseModel):
    model_id: str
    mode: str | None = None
    takes: int = 3
    keep_pauses: bool = True
    match_timing: bool = True
    follow_level: bool = True
    phrases: bool = True
    only: list[int] = []


@router.post("/{pid}/render")
def render(pid: str, body: RenderIn):
    rec = _get(pid)
    if rec["status"] not in ("ready", "done"):
        raise HTTPException(400, {"analyzing": "還在分析，等分析完成再念", "rendering": "正在合成，等這次完成"}
                            .get(rec["status"], "分析沒有成功，請重新分析"))
    m = db.get("models", body.model_id)
    if not m:
        raise HTTPException(404, "找不到模型")
    from .. import datasets
    voice = db.get("voices", m["voice_id"])
    if m["engine"] != "mock" and (not voice or not datasets.consent_ok(voice)):
        raise HTTPException(400, "這個聲音目前沒有有效的同意紀錄，不能合成。")
    params = {"perform_id": pid, **body.model_dump(), "takes": max(1, min(5, body.takes))}
    db.update("performances", pid, {"params": {k: v for k, v in params.items() if k not in ("perform_id", "only")}})
    return jobs.submit("perform_render", params, "排隊合成")


@router.post("/{pid}/analyze")
def reanalyze(pid: str, body: dict | None = None):
    rec = _get(pid)
    lang = (body or {}).get("language")
    db.update("performances", pid, {"status": "analyzing", "lang": lang if lang in ("ja", "en", "zh") else rec["lang"],
                                    "phrases": [], "result": {}})
    return jobs.submit("perform_analyze", {"perform_id": pid, "separate": bool((body or {}).get("separate"))},
                       "排隊分析")


@router.get("/{pid}/source")
def source_audio(pid: str):
    f = perform.folder(_get(pid)["id"]) / "source.wav"
    if not f.exists():
        raise HTTPException(404)
    return FileResponse(f, media_type="audio/wav")


@router.get("/{pid}/phrase/{i}/source")
def phrase_source(pid: str, i: int):
    rec = _get(pid)
    p = next((x for x in rec["phrases"] if x["i"] == i), None)
    f = perform.folder(pid) / "source.wav"
    if not p or not f.exists():
        raise HTTPException(404)
    import io
    import soundfile as sf
    info = sf.info(str(f))
    a, b = int(max(0, p["start"] - 0.05) * info.samplerate), int((p["end"] + 0.1) * info.samplerate)
    y, sr = sf.read(str(f), start=a, stop=b, dtype="float32")
    buf = io.BytesIO()
    sf.write(buf, np.asarray(y), sr, format="WAV", subtype="PCM_16")
    return Response(buf.getvalue(), media_type="audio/wav")


@router.get("/{pid}/phrase/{i}/output")
def phrase_output(pid: str, i: int):
    f = perform.folder(_get(pid)["id"]) / f"p{int(i)}.wav"
    if not f.exists():
        raise HTTPException(404)
    return FileResponse(f, media_type="audio/wav")


@router.delete("/{pid}")
def delete(pid: str):
    rec = db.get("performances", pid)
    if rec:
        oid = (rec["result"] or {}).get("output_id")
        if oid and (o := db.get("outputs", oid)):
            Path(o["path"]).unlink(missing_ok=True)
            Path(o["path"]).with_suffix(".mp3").unlink(missing_ok=True)
            db.delete("outputs", oid)
        shutil.rmtree(perform.folder(pid), ignore_errors=True)
        db.delete("performances", pid)
    return {"ok": True}

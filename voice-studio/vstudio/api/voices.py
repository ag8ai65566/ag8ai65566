"""Voices (people whose consented recordings are trained), their consent records and enrollment clips."""
from __future__ import annotations

import shutil
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from .. import audio, config, datasets, db, jobs

router = APIRouter(prefix="/api/voices", tags=["voices"])


class VoiceIn(BaseModel):
    name: str
    kind: str = "self"  # self | other | designed
    languages: list[str] = ["ja", "en"]
    notes: str = ""


def _stats(v: dict) -> dict:
    r = db.connect().execute(
        "SELECT status, COUNT(*), COALESCE(SUM(duration),0) FROM segments WHERE voice_id=? GROUP BY status",
        (v["id"],)).fetchall()
    by = {row[0]: {"count": row[1], "minutes": round(row[2] / 60, 1)} for row in r}
    v["stats"] = by
    v["consent_ok"] = datasets.consent_ok(v)
    v["enrolled"] = sum(1 for e in v["enrollment"] if e.get("emb"))
    for e in v["enrollment"]:
        e.pop("emb", None)
    return v


@router.get("")
def list_voices():
    return [_stats(v) for v in db.query("SELECT * FROM voices ORDER BY created_at")]


@router.post("")
def create_voice(body: VoiceIn):
    if body.kind not in ("self", "other", "designed"):
        raise HTTPException(400, "kind")
    v = db.insert("voices", {"id": db.new_id("voice"), "name": body.name.strip(), "kind": body.kind,
                             "languages": body.languages, "notes": body.notes, "enrollment": [],
                             "created_at": db.now()})
    return _stats(v)


@router.get("/{voice_id}")
def get_voice(voice_id: str):
    v = db.get("voices", voice_id)
    if not v:
        raise HTTPException(404)
    return _stats(v)


@router.patch("/{voice_id}")
def update_voice(voice_id: str, body: dict):
    allowed = {k: body[k] for k in ("name", "languages", "notes", "kind") if k in body}
    return _stats(db.update("voices", voice_id, allowed))


@router.delete("/{voice_id}")
def delete_voice(voice_id: str):
    with db.tx() as c:
        c.execute("UPDATE segments SET voice_id=NULL WHERE voice_id=?", (voice_id,))
    shutil.rmtree(config.DATA / "voices" / voice_id, ignore_errors=True)
    db.delete("voices", voice_id)
    return {"ok": True}


@router.post("/{voice_id}/consent")
async def set_consent(voice_id: str, signed_name: str = Form(...), date: str = Form(...),
                      relationship: str = Form(""), scope: str = Form("train,generate"),
                      personal_only: bool = Form(True), document_note: str = Form(""),
                      agreed: bool = Form(...), document: UploadFile | None = File(None)):
    """Record who agreed, when, and to what. For other people, a signed document (scan/photo/PDF) or a note
    saying where the signed copy is kept is required before training is allowed."""
    v = db.get("voices", voice_id)
    if not v:
        raise HTTPException(404)
    doc_path = v.get("consent_doc")
    if document is not None and document.filename:
        ext = Path(document.filename).suffix.lower()[:6] or ".bin"
        dst = config.path("voices", voice_id, f"consent{ext}")
        with open(dst, "wb") as fh:
            shutil.copyfileobj(document.file, fh)
        doc_path = str(dst)
    consent = {"agreed": bool(agreed), "signed_name": signed_name.strip(), "date": date,
               "relationship": relationship, "scope": [s for s in scope.split(",") if s],
               "personal_only": personal_only, "document_note": document_note.strip(), "recorded_at": db.now()}
    return _stats(db.update("voices", voice_id, {"consent": consent, "consent_doc": doc_path}))


@router.post("/{voice_id}/enrollment")
async def add_enrollment(voice_id: str, files: list[UploadFile] = File(default=[]), segment_ids: str = Form("")):
    """Reference clips (5–30 s each, voice alone) used to recognise this person in mixed recordings."""
    v = db.get("voices", voice_id)
    if not v:
        raise HTTPException(404)
    enr = list(v["enrollment"])
    for f in files:
        tmp = config.path("tmp", f"{db.new_id('up')}{Path(f.filename or 'clip.wav').suffix}")
        with open(tmp, "wb") as fh:
            shutil.copyfileobj(f.file, fh)
        dst = config.path("voices", voice_id, f"enroll_{len(enr) + 1}.wav")
        audio.extract(tmp, dst, sr=audio.MASTER_SR)
        tmp.unlink(missing_ok=True)
        enr.append({"path": str(dst), "from": f.filename})
    for sid in [s for s in segment_ids.split(",") if s]:
        seg = db.get("segments", sid)
        if seg:
            dst = config.path("voices", voice_id, f"enroll_{len(enr) + 1}.wav")
            shutil.copy2(seg["path"], dst)
            enr.append({"path": str(dst), "from": sid})
    db.update("voices", voice_id, {"enrollment": enr})
    job = jobs.submit("enroll_voice", {"voice_id": voice_id}, message="建立聲紋")
    return {"voice": _stats(db.get("voices", voice_id)), "job": job}


@router.delete("/{voice_id}/enrollment/{index}")
def remove_enrollment(voice_id: str, index: int):
    v = db.get("voices", voice_id)
    enr = list(v["enrollment"])
    if 0 <= index < len(enr):
        Path(enr[index]["path"]).unlink(missing_ok=True)
        enr.pop(index)
    return _stats(db.update("voices", voice_id, {"enrollment": enr}))

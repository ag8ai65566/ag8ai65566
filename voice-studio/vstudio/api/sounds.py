"""Sound tags: find breathing, sighs and panting in a voice's recordings, listen, keep them as [tag] recordings."""
from __future__ import annotations

import io

import soundfile as sf
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

from .. import db, jobs, phrases, sounds

router = APIRouter(prefix="/api", tags=["sounds"])


def _find(fid: str) -> dict:
    f = db.get("sound_finds", fid)
    if not f:
        raise HTTPException(404)
    return f


def _view(f: dict) -> dict:
    return {**f, "clip_start": round(sounds.slice_start(f), 3), "clip_end": round(f["end"] + sounds.PAD, 3),
            "label": sounds.KINDS[f["kind"]][0],
            "suggest": sounds.KINDS[f["kind"]][1] or None}


@router.get("/voices/{voice_id}/sounds")
def list_finds(voice_id: str, kind: str = "", status: str = "new", limit: int = 50, offset: int = 0):
    counts = {r["kind"]: r["n"] for r in db.query(
        "SELECT kind, COUNT(*) AS n FROM sound_finds WHERE voice_id=? AND status=? GROUP BY kind", (voice_id, status))}
    where, args = "voice_id=? AND status=?", [voice_id, status]
    if kind:
        where += " AND kind=?"
        args.append(kind)
    items = db.query(f"SELECT * FROM sound_finds WHERE {where} ORDER BY score DESC, source_id, start LIMIT ? OFFSET ?",
                     (*args, max(1, min(200, limit)), max(0, offset)))
    job = db.query("SELECT id, status, progress, message FROM jobs WHERE kind='find_sounds' AND params LIKE ? "
                   "ORDER BY created_at DESC LIMIT 1", (f'%"{voice_id}"%',))
    return {"counts": counts, "items": [_view(f) for f in items], "job": job[0] if job else None,
            "kinds": {k: v[0] for k, v in sounds.KINDS.items()}}


@router.post("/voices/{voice_id}/sounds/scan")
def scan(voice_id: str):
    if not db.get("voices", voice_id):
        raise HTTPException(404)
    if not db.query("SELECT 1 FROM segments WHERE voice_id=? LIMIT 1", (voice_id,)):
        raise HTTPException(400, "這個聲音還沒有匯入的片段，先匯入錄音")
    busy = db.query("SELECT id FROM jobs WHERE kind='find_sounds' AND status IN ('queued','running') AND params LIKE ?",
                    (f'%"{voice_id}"%',))
    if busy:
        raise HTTPException(400, "正在掃描，等這次完成")
    return jobs.submit("find_sounds", {"voice_id": voice_id}, "排隊掃描")


@router.get("/sounds/{fid}/audio")
def find_audio(fid: str):
    try:
        y, sr = sounds.slice_audio(_find(fid))
    except (KeyError, RuntimeError):
        raise HTTPException(404)
    buf = io.BytesIO()
    sf.write(buf, y, sr, format="WAV", subtype="PCM_16")
    return Response(buf.getvalue(), media_type="audio/wav")


class KeepIn(BaseModel):
    phrase_id: str | None = None   # an existing sound tag of this voice
    tag: str | None = None         # or a new one, e.g. "[喘氣]"
    start: float | None = None     # seconds from the start of the played slice (clip_start); default: as found
    end: float | None = None
    emotion: str | None = None


@router.post("/sounds/{fid}/keep")
def keep(fid: str, body: KeepIn):
    f = _find(fid)
    try:
        if body.phrase_id:
            pid = body.phrase_id
            if not phrases.is_sound(phrases.get(pid)):
                raise ValueError("請選聲音標籤（像 [喘氣] 這種用中括號的）")
        else:
            tag = phrases.as_tag(body.tag or "")
            if not tag:
                raise ValueError("請選或輸入一個聲音標籤，例如 [喘氣]")
            same = [p for p in phrases.list_for_voice(f["voice_id"]) if p["text"].lower() == tag.lower()]
            pid = same[0]["id"] if same else phrases.create(f["voice_id"], tag)["id"]
        base = sounds.slice_start(f)
        a = base + body.start if body.start is not None else f["start"]
        b = base + body.end if body.end is not None else f["end"]
        return sounds.keep(f, pid, a, b, body.emotion or None)
    except KeyError:
        raise HTTPException(404)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.post("/sounds/{fid}/dismiss")
def dismiss(fid: str):
    _find(fid)
    return db.update("sound_finds", fid, {"status": "dismissed"})


@router.post("/sounds/{fid}/restore")
def restore(fid: str):
    _find(fid)
    return db.update("sound_finds", fid, {"status": "new"})

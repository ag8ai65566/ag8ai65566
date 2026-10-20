"""Checking recordings before import: upload or point at a folder, read the verdicts, import the ones that passed."""
from __future__ import annotations

import io
import re
import shutil
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import Response
from pydantic import BaseModel

from .. import audio, audiocheck, config, db, emotions, jobs, labels

router = APIRouter(prefix="/api/checks", tags=["checks"])


def _batch_ok(batch: str) -> str:
    if not re.fullmatch(r"chk_[0-9a-z]+", batch):
        raise HTTPException(400, "bad batch id")
    return batch


def _start(batch: str, deep: bool) -> dict | None:
    """A job for the batch, unless one is already waiting (a running one picks up new files as it goes, and a
    second waiting job covers the case where it has just finished)."""
    waiting = db.query("SELECT id FROM jobs WHERE kind='audio_check' AND status='queued' AND params LIKE ?",
                       (f'%"{batch}"%',))
    if waiting:
        return None
    return jobs.submit("audio_check", {"batch": batch, "deep": deep}, "排隊檢查")


@router.get("/criteria")
def criteria():
    return audiocheck.criteria()


@router.post("/batches")
def new_batch():
    return {"id": db.new_id("chk")}


@router.get("")
def list_checks(limit: int = 1000):
    rows = db.query("SELECT * FROM audio_checks ORDER BY created_at DESC LIMIT ?", (limit,))
    running = {j["params"].get("batch"): {k: j[k] for k in ("id", "status", "progress", "message")}
               for j in db.query("SELECT id, status, progress, message, params FROM jobs WHERE kind='audio_check' "
                                 "AND status IN ('queued', 'running') ORDER BY created_at")}
    batches: dict = {}
    for r in rows:
        r["bgm_ok"] = r["status"] == "done" and audiocheck.quiet_bgm(r["result"])
        b = batches.setdefault(r["batch"], {"id": r["batch"], "created_at": r["created_at"], "items": [],
                                           "root": r["root"], "job": running.get(r["batch"])})
        b["created_at"] = min(b["created_at"], r["created_at"])
        b["items"].append(r)
    for b in batches.values():
        b["items"].sort(key=lambda r: r["created_at"])
    return sorted(batches.values(), key=lambda b: -b["created_at"])


@router.post("/upload")
async def upload(file: UploadFile = File(...), batch: str = Form(...), deep: bool = Form(False)):
    _batch_ok(batch)
    name = Path(file.filename or "audio").name
    d = audiocheck.folder(batch)
    d.mkdir(parents=True, exist_ok=True)
    cid = db.new_id("ac")
    dst = d / f"{cid}_{name}"
    with open(dst, "wb") as fh:
        shutil.copyfileobj(file.file, fh, length=8 << 20)
    item = db.insert("audio_checks", {"id": cid, "batch": batch, "filename": name, "path": str(dst), "root": None,
                                      "copied": 1, "status": "queued", "result": {}, "meta": {},
                                      "created_at": db.now()})
    _start(batch, deep)
    return item


class PathIn(BaseModel):
    path: str
    recursive: bool = True
    deep: bool = False


@router.post("/path")
def check_path(body: PathIn):
    """Check files where they are (nothing is copied)."""
    root = Path(body.path.strip().strip('"')).expanduser()
    if not root.exists():
        raise HTTPException(400, f"找不到：{root}")
    files = [root] if root.is_file() else sorted(
        p for p in (root.rglob("*") if body.recursive else root.iterdir())
        if p.is_file() and p.suffix.lower() in audio.MEDIA_EXT)
    if not files:
        raise HTTPException(400, "這個資料夾裡沒有影音檔。")
    batch = db.new_id("chk")
    for f in files:
        db.insert("audio_checks", {"id": db.new_id("ac"), "batch": batch, "filename": f.name, "path": str(f),
                                   "root": str(root if root.is_dir() else root.parent), "copied": 0,
                                   "status": "queued", "result": {}, "meta": {}, "created_at": db.now()})
    _start(batch, body.deep)
    return {"batch": batch, "count": len(files)}


@router.post("/{batch}/start")
def start(batch: str, body: dict | None = None):
    _batch_ok(batch)
    return {"job": _start(batch, bool((body or {}).get("deep")))}


@router.post("/{batch}/recheck")
def recheck(batch: str, body: dict | None = None):
    """Check the whole batch again (for example with the deep check on)."""
    _batch_ok(batch)
    with db.tx() as c:
        c.execute("UPDATE audio_checks SET status='queued', verdict=NULL WHERE batch=? AND status<>'running'",
                  (batch,))
    return {"job": _start(batch, bool((body or {}).get("deep")))}


@router.get("/{cid}/audio")
def clip(cid: str, start: float = 0.0, end: float = 0.0):
    """A slice of the original recording, to hear a problem the check found."""
    item = db.get("audio_checks", cid)
    if not item or not Path(item["path"]).exists():
        raise HTTPException(404)
    s = max(0.0, start - 1.0)
    dur = min(30.0, max(1.0, (end or start + 3) - s + 1.0))
    import soundfile as sf
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        out = audio.extract(Path(item["path"]), Path(d) / "c.wav", sr=48000, start=s, dur=dur)
        y, sr = sf.read(str(out), dtype="float32")
    buf = io.BytesIO()
    sf.write(buf, y, sr, format="WAV", subtype="PCM_16")
    return Response(buf.getvalue(), media_type="audio/wav")


def _remove(item: dict) -> None:
    if item["copied"]:
        Path(item["path"]).unlink(missing_ok=True)
    db.delete("audio_checks", item["id"])


@router.delete("/batch/{batch}")
def delete_batch(batch: str):
    _batch_ok(batch)
    for item in db.query("SELECT * FROM audio_checks WHERE batch=?", (batch,)):
        _remove(item)
    shutil.rmtree(audiocheck.folder(batch), ignore_errors=True)
    return {"ok": True}


@router.delete("/{cid}")
def delete_one(cid: str):
    item = db.get("audio_checks", cid)
    if item:
        _remove(item)
    return {"ok": True}


class ImportIn(BaseModel):
    ids: list[str]
    voice_hint: str | None = None
    language: str | None = None
    emotion: str | None = None
    separate: bool = False     # remove the background music (for recordings with quiet music, bgm/)


@router.post("/import")
def import_checked(body: ImportIn):
    """Import checked recordings. Uploaded copies move into the studio's sources; checked folders stay in place.
    Emotion and language labels in file and folder names apply as in a normal import."""
    if body.emotion and not emotions.valid(body.emotion):
        raise HTTPException(400, f"unknown emotion: {body.emotion}")
    known = {s["path"] for s in db.query("SELECT path FROM sources")}
    up = config.DATA / "sources" / "_uploads"
    created = []
    for cid in body.ids:
        item = db.get("audio_checks", cid)
        if not item or not Path(item["path"]).exists() or item["path"] in known:
            continue
        path = Path(item["path"])
        folders = list(path.relative_to(item["root"]).parts[:-1]) if item["root"] and \
            path.is_relative_to(item["root"]) else []
        emo, lang, _ = labels.resolve(item["filename"], None, body.emotion, body.language, folders)
        if item["copied"]:
            up.mkdir(parents=True, exist_ok=True)
            dst = up / f"{db.new_id('up')}_{item['filename']}"
            shutil.move(str(path), dst)
            path = dst
        src = db.insert("sources", {"id": db.new_id("src"), "filename": item["filename"], "path": str(path),
                                    "status": "new", "voice_hint": body.voice_hint or None, "language": lang,
                                    "emotion": emo, "meta": {"copied": bool(item["copied"]),
                                                             "check": {"verdict": item["verdict"],
                                                                       "separated": body.separate}},
                                    "created_at": db.now()})
        jobs.submit("prepare_source", {"source_id": src["id"], "separate": body.separate}, "排隊處理")
        db.update("audio_checks", cid, {"path": str(path), "copied": 0,
                                        "meta": {**(item["meta"] or {}), "imported": src["id"]}})
        created.append(src["id"])
    return {"created": len(created)}

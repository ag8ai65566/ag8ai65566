"""Sources (imported recordings), segments (review) and datasets."""
from __future__ import annotations

import shutil
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .. import audio, config, datasets, db, jobs
from ..pipeline import prepare

router = APIRouter(prefix="/api", tags=["data"])


# --- sources --------------------------------------------------------------------------------------------------------

@router.get("/sources")
def list_sources():
    out = db.query("SELECT * FROM sources ORDER BY created_at DESC")
    counts = {r[0]: (r[1], r[2], r[3]) for r in db.connect().execute(
        "SELECT source_id, COUNT(*), SUM(status='approved'), SUM(voice_id IS NULL AND status<>'rejected') "
        "FROM segments GROUP BY source_id")}
    latest: dict = {}
    for j in db.query("SELECT id, status, progress, message, params, created_at FROM jobs "
                      "WHERE kind='prepare_source' ORDER BY created_at"):
        latest[j["params"].get("source_id")] = {k: j[k] for k in ("id", "status", "progress", "message")}
    for s in out:
        n, approved, unassigned = counts.get(s["id"], (0, 0, 0))
        s["segments"], s["approved"], s["unassigned"] = n, approved or 0, unassigned or 0
        s["job"] = latest.get(s["id"])
    return out


def _new_source(filename: str, path: str, voice_hint: str | None, language: str | None, copied: bool) -> dict:
    return db.insert("sources", {"id": db.new_id("src"), "filename": filename, "path": path, "status": "new",
                                 "voice_hint": voice_hint or None, "language": language or None,
                                 "meta": {"copied": copied}, "created_at": db.now()})


@router.post("/sources/upload")
async def upload_source(file: UploadFile = File(...), voice_hint: str = Form(""), language: str = Form(""),
                        separate: bool = Form(False), process: bool = Form(True)):
    sid_dir = config.DATA / "sources" / "_uploads"
    sid_dir.mkdir(parents=True, exist_ok=True)
    dst = sid_dir / f"{db.new_id('up')}_{Path(file.filename or 'audio').name}"
    with open(dst, "wb") as fh:
        shutil.copyfileobj(file.file, fh, length=8 << 20)
    src = _new_source(file.filename or dst.name, str(dst), voice_hint, language, True)
    job = jobs.submit("prepare_source", {"source_id": src["id"], "separate": separate}, "排隊處理") if process else None
    return {"source": src, "job": job}


class ImportPath(BaseModel):
    path: str
    recursive: bool = True
    voice_hint: str | None = None
    language: str | None = None
    separate: bool = False


@router.post("/sources/import-path")
def import_path(body: ImportPath):
    """Import files straight from a folder on this computer (no copy: large videos stay where they are)."""
    root = Path(body.path).expanduser()
    if not root.exists():
        raise HTTPException(400, f"找不到：{root}")
    files = [root] if root.is_file() else sorted(
        p for p in (root.rglob("*") if body.recursive else root.iterdir())
        if p.is_file() and p.suffix.lower() in audio.MEDIA_EXT)
    known = {s["path"] for s in db.query("SELECT path FROM sources")}
    created = []
    for f in files:
        if str(f) in known:
            continue
        src = _new_source(f.name, str(f), body.voice_hint, body.language, False)
        jobs.submit("prepare_source", {"source_id": src["id"], "separate": body.separate}, "排隊處理")
        created.append(src)
    return {"found": len(files), "created": len(created), "sources": created}


@router.post("/sources/{source_id}/process")
def process_source(source_id: str, body: dict | None = None):
    body = body or {}
    if not db.get("sources", source_id):
        raise HTTPException(404)
    return jobs.submit("prepare_source", {"source_id": source_id, "separate": bool(body.get("separate")),
                                          "language": body.get("language")}, "排隊處理")


@router.delete("/sources/{source_id}")
def delete_source(source_id: str):
    src = db.get("sources", source_id)
    prepare.remove_source(source_id)
    if src and src["meta"].get("copied"):
        Path(src["path"]).unlink(missing_ok=True)
    return {"ok": True}


@router.get("/sources/{source_id}/clusters")
def clusters(source_id: str):
    """Groups of segments that sound like the same person (when no voice could be matched automatically)."""
    rows = db.query("SELECT cluster, COUNT(*) AS n, SUM(duration) AS secs, MAX(voice_id) AS voice_id, "
                    "SUM(status='rejected') AS rejected FROM segments WHERE source_id=? "
                    "AND cluster IS NOT NULL GROUP BY cluster ORDER BY n DESC", (source_id,))
    for r in rows:
        r["samples"] = [s["id"] for s in db.query(
            "SELECT id FROM segments WHERE source_id=? AND cluster=? ORDER BY score DESC LIMIT 3",
            (source_id, r["cluster"]))]
    return rows


@router.post("/sources/{source_id}/clusters/{cluster}/assign")
def assign_cluster(source_id: str, cluster: int, body: dict):
    """Give a whole group to a voice, or (reject=true) mark it as nobody's so it never enters training."""
    voice_id = body.get("voice_id") or None
    with db.tx() as c:
        if body.get("reject"):
            c.execute("UPDATE segments SET voice_id=NULL, status='rejected' WHERE source_id=? AND cluster=?",
                      (source_id, cluster))
        else:
            c.execute("UPDATE segments SET voice_id=?, status=CASE WHEN status='rejected' THEN 'pending' ELSE status "
                      "END WHERE source_id=? AND cluster=?", (voice_id, source_id, cluster))
    _rescore(source_id)
    return {"ok": True}


def _rescore(source_id: str) -> None:
    for s in db.query("SELECT * FROM segments WHERE source_id=?", (source_id,)):
        sc, flags = prepare.score({**s, "ambiguous": "overlap" in (s["flags"] or [])})
        db.update("segments", s["id"], {"score": sc, "flags": flags})


# --- segments ---------------------------------------------------------------------------------------------------

@router.get("/segments")
def list_segments(voice_id: str = "", source_id: str = "", status: str = "", flag: str = "",
                  min_score: float = -1, max_score: float = 2, unassigned: bool = False,
                  sort: str = "score_desc", offset: int = 0, limit: int = 100, q: str = ""):
    where, args = ["1=1"], []
    if voice_id:
        where.append("voice_id=?"); args.append(voice_id)
    if unassigned:
        where.append("voice_id IS NULL")
    if source_id:
        where.append("source_id=?"); args.append(source_id)
    if status:
        where.append("status=?"); args.append(status)
    if flag:
        where.append("flags LIKE ?"); args.append(f'%"{flag}"%')
    if q:
        where.append("text LIKE ?"); args.append(f"%{q}%")
    where.append("COALESCE(score,0) BETWEEN ? AND ?"); args += [min_score, max_score]
    order = {"score_desc": "score DESC", "score_asc": "score ASC", "time": "source_id, start",
             "duration": "duration DESC"}.get(sort, "score DESC")
    w = " AND ".join(where)
    total = db.connect().execute(f"SELECT COUNT(*), COALESCE(SUM(duration),0) FROM segments WHERE {w}", args).fetchone()
    items = db.query(f"SELECT * FROM segments WHERE {w} ORDER BY {order} LIMIT ? OFFSET ?", args + [limit, offset])
    return {"total": total[0], "minutes": round(total[1] / 60, 1), "items": items}


class SegmentPatch(BaseModel):
    text: str | None = None
    status: str | None = None
    voice_id: str | None = None


@router.patch("/segments/{seg_id}")
def patch_segment(seg_id: str, body: SegmentPatch):
    upd = {}
    if body.text is not None:
        upd["text"], upd["edited"] = body.text, 1
    if body.status in ("pending", "approved", "rejected"):
        upd["status"] = body.status
    if body.voice_id is not None:
        upd["voice_id"] = body.voice_id or None
    s = db.update("segments", seg_id, upd)
    if "text" in upd or "voice_id" in upd:
        flags = [f for f in s["flags"] if f not in ("asr_disagree", "unknown_speaker", "no_text")] \
            if s["edited"] else s["flags"]
        sc, fl = prepare.score({**s, "asr_agree": 1.0 if s["edited"] else s["asr_agree"], "flags": flags,
                                "ambiguous": "overlap" in flags})
        s = db.update("segments", seg_id, {"score": sc, "flags": fl})
    return s


class Bulk(BaseModel):
    ids: list[str] = []
    filter: dict | None = None
    status: str | None = None
    voice_id: str | None = None


@router.post("/segments/bulk")
def bulk(body: Bulk):
    ids = list(body.ids)
    if body.filter is not None:
        f = dict(body.filter)
        f.update(offset=0, limit=1000000)
        ids += [s["id"] for s in list_segments(**f)["items"]]
    sets, args = [], []
    if body.status in ("pending", "approved", "rejected"):
        sets.append("status=?"); args.append(body.status)
    if body.voice_id is not None:
        sets.append("voice_id=?"); args.append(body.voice_id or None)
    if not sets or not ids:
        return {"updated": 0}
    with db.tx() as c:
        for i in range(0, len(ids), 500):
            chunk = ids[i:i + 500]
            c.execute(f"UPDATE segments SET {', '.join(sets)} WHERE id IN ({','.join('?' * len(chunk))})",
                      args + chunk)
    return {"updated": len(ids)}


@router.get("/segments/{seg_id}/audio")
def segment_audio(seg_id: str):
    s = db.get("segments", seg_id)
    if not s or not Path(s["path"]).exists():
        raise HTTPException(404)
    return FileResponse(s["path"], media_type="audio/wav")


# --- datasets ---------------------------------------------------------------------------------------------------

@router.get("/datasets")
def list_datasets(voice_id: str = ""):
    if voice_id:
        return db.query("SELECT * FROM datasets WHERE voice_id=? ORDER BY created_at DESC", (voice_id,))
    return db.query("SELECT * FROM datasets ORDER BY created_at DESC")


class DatasetIn(BaseModel):
    voice_id: str
    name: str = ""
    min_score: float = 0.0


@router.post("/datasets")
def build_dataset(body: DatasetIn):
    try:
        v = db.get("voices", body.voice_id)
        name = body.name or f"{v['name']} {db.query('SELECT COUNT(*) AS n FROM datasets WHERE voice_id=?', (body.voice_id,))[0]['n'] + 1}"
        return datasets.build(body.voice_id, name, body.min_score)
    except datasets.ConsentMissing as e:
        raise HTTPException(409, str(e))
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.delete("/datasets/{dataset_id}")
def delete_dataset(dataset_id: str):
    datasets.remove(dataset_id)
    return {"ok": True}

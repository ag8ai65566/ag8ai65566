"""Sources (imported recordings), segments (review) and datasets."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel

from .. import audio, config, datasets, db, emotions, jobs, labels
from ..pipeline import autoreview, prepare

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


def _emotion(e: str | None) -> str | None:
    if e and not emotions.valid(e):
        raise HTTPException(400, f"unknown emotion: {e}")
    return e or None


def _new_source(filename: str, path: str, voice_hint: str | None, language: str | None, copied: bool,
                emotion: str | None = None) -> dict:
    return db.insert("sources", {"id": db.new_id("src"), "filename": filename, "path": path, "status": "new",
                                 "voice_hint": voice_hint or None, "language": language or None,
                                 "emotion": _emotion(emotion), "meta": {"copied": copied}, "created_at": db.now()})


# --- emotion / language lists (Excel or CSV) ---------------------------------------------------------------------

def _labels_dir() -> Path:
    d = config.DATA / "labels"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _load_labels(labels_id: str | None) -> dict | None:
    if not labels_id:
        return None
    if not re.fullmatch(r"lbl_[0-9a-z]+", labels_id):
        raise HTTPException(400, "bad labels id")
    p = _labels_dir() / f"{labels_id}.json"
    if not p.exists():
        raise HTTPException(400, "情緒清單已過期，請重新上傳。")
    return json.loads(p.read_text(encoding="utf-8"))["rows"]


@router.post("/import-labels")
async def upload_labels(file: UploadFile = File(...)):
    """Read an emotion list once; the files uploaded or imported next refer to it by id."""
    try:
        out = labels.parse_list(await file.read(), file.filename or "list.csv")
    except ValueError as e:
        raise HTTPException(400, str(e))
    lid = db.new_id("lbl")
    (_labels_dir() / f"{lid}.json").write_text(json.dumps({"filename": file.filename, **out}, ensure_ascii=False),
                                               encoding="utf-8")
    return {"id": lid, "filename": file.filename, "count": out["count"], "errors": out["errors"],
            "emotions": _emotion_counts(out["rows"])}


def _emotion_counts(rows: dict) -> dict:
    counts: dict = {}
    for r in rows.values():
        if r.get("emotion"):
            counts[r["emotion"]] = counts.get(r["emotion"], 0) + 1
    return counts


@router.get("/import-labels/template.csv")
def labels_template():
    # the byte-order mark makes Excel open the Chinese headings as UTF-8
    return Response(("\ufeff" + labels.TEMPLATE_CSV).encode("utf-8"), media_type="text/csv",
                    headers={"Content-Disposition": "attachment; filename*=UTF-8''%E6%83%85%E7%B7%92%E6%B8%85%E5%96%AE.csv"})


@router.post("/sources/upload")
async def upload_source(file: UploadFile = File(...), voice_hint: str = Form(""), language: str = Form(""),
                        separate: bool = Form(False), process: bool = Form(True), emotion: str = Form(""),
                        labels_id: str = Form(""), relpath: str = Form("")):
    """One file from the browser. relpath is its path inside a folder picked with "選資料夾" (for folder labels)."""
    _emotion(emotion)
    rows = _load_labels(labels_id)
    name = Path(file.filename or "audio").name
    folders = [x for x in relpath.replace("\\", "/").split("/")[:-1] if x] if relpath else []
    emo, lang, label_src = labels.resolve(name, rows, emotion, language, folders)
    sid_dir = config.DATA / "sources" / "_uploads"
    sid_dir.mkdir(parents=True, exist_ok=True)
    dst = sid_dir / f"{db.new_id('up')}_{name}"
    with open(dst, "wb") as fh:
        shutil.copyfileobj(file.file, fh, length=8 << 20)
    src = _new_source(name, str(dst), voice_hint, lang, True, emo)
    job = jobs.submit("prepare_source", {"source_id": src["id"], "separate": separate}, "排隊處理") if process else None
    return {"source": src, "job": job, "label_from": label_src}


class ImportPath(BaseModel):
    path: str
    recursive: bool = True
    voice_hint: str | None = None
    language: str | None = None
    separate: bool = False
    emotion: str | None = None
    labels_id: str | None = None


@router.post("/sources/import-path")
def import_path(body: ImportPath):
    """Import files straight from a folder on this computer (no copy: large videos stay where they are).

    Emotion labels come from an uploaded list, else a list (.xlsx / .csv) inside the folder, then file names and
    folder names, then the form."""
    root = Path(body.path.strip().strip('"')).expanduser()
    if not root.exists():
        raise HTTPException(400, f"找不到：{root}")
    _emotion(body.emotion)
    rows, list_name, list_errors = _load_labels(body.labels_id), None, []
    if rows is None and root.is_dir() and (found := labels.find_list(root)):
        try:
            parsed = labels.parse_list(found.read_bytes(), found.name)
            rows, list_name, list_errors = parsed["rows"], found.name, parsed["errors"]
        except ValueError as e:
            list_name, list_errors = found.name, [str(e)]
    files = [root] if root.is_file() else sorted(
        p for p in (root.rglob("*") if body.recursive else root.iterdir())
        if p.is_file() and p.suffix.lower() in audio.MEDIA_EXT)
    known = {s["path"] for s in db.query("SELECT path FROM sources")}
    created: list = []
    by: dict = {}
    for f in files:
        if str(f) in known:
            continue
        folders = list(f.relative_to(root).parts[:-1]) if root.is_dir() else []
        emo, lang, src_of = labels.resolve(f.name, rows, body.emotion, body.language, folders)
        src = _new_source(f.name, str(f), body.voice_hint, lang, False, emo)
        jobs.submit("prepare_source", {"source_id": src["id"], "separate": body.separate}, "排隊處理")
        created.append(src)
        if emo:
            by[src_of] = by.get(src_of, 0) + 1
    return {"found": len(files), "created": len(created), "sources": created, "labelled": by,
            "list": list_name, "list_errors": list_errors}


@router.post("/sources/{source_id}/process")
def process_source(source_id: str, body: dict | None = None):
    body = body or {}
    if not db.get("sources", source_id):
        raise HTTPException(404)
    return jobs.submit("prepare_source", {"source_id": source_id, "separate": bool(body.get("separate")),
                                          "language": body.get("language")}, "排隊處理")


@router.patch("/sources/{source_id}")
def patch_source(source_id: str, body: dict):
    """Change a recording's emotion label. Its segments follow, except ones a person labelled differently."""
    src = db.get("sources", source_id)
    if not src:
        raise HTTPException(404)
    if "emotion" in body:
        new, old = _emotion(body.get("emotion")), src.get("emotion")
        with db.tx() as c:
            c.execute("UPDATE segments SET emotion=? WHERE source_id=? AND (emotion IS NULL OR emotion IS ?)",
                      (new, source_id, old))
        src = db.update("sources", source_id, {"emotion": new})
    return src


def _stop_processing(source_id: str) -> None:
    """Cancel the source's import job; a running one notices at its next step and cleans up after itself."""
    for j in db.query("SELECT id FROM jobs WHERE kind='prepare_source' AND status IN ('queued', 'running') "
                      "AND params LIKE ?", (f'%"{source_id}"%',)):
        jobs.cancel(j["id"])


def _delete_source(source_id: str) -> None:
    src = db.get("sources", source_id)
    _stop_processing(source_id)
    prepare.remove_source(source_id)
    if src and src["meta"].get("copied"):
        Path(src["path"]).unlink(missing_ok=True)


@router.delete("/sources/{source_id}")
def delete_source(source_id: str):
    _delete_source(source_id)
    return {"ok": True}


class SourceIds(BaseModel):
    ids: list[str]
    voice_id: str | None = None


@router.post("/sources/bulk-delete")
def bulk_delete_sources(body: SourceIds):
    """Remove many recordings at once (with their segments; files outside the studio are never deleted)."""
    for sid in body.ids:
        _delete_source(sid)
    return {"deleted": len(body.ids)}


@router.post("/sources/bulk-assign")
def bulk_assign(body: SourceIds):
    """Say who is speaking in many recordings at once: their segments without a voice go to this voice, and
    recordings still waiting to be processed use it as their hint. Segments marked as nobody's stay that way."""
    if not body.voice_id or not db.get("voices", body.voice_id):
        raise HTTPException(400, "請選一個聲音")
    n_seg, waiting = 0, 0
    for sid in body.ids:
        src = db.get("sources", sid)
        if not src:
            continue
        db.update("sources", sid, {"voice_hint": body.voice_id})
        if src["status"] != "ready":
            waiting += 1
            continue
        with db.tx() as c:
            n_seg += c.execute("UPDATE segments SET voice_id=? WHERE source_id=? AND voice_id IS NULL "
                               "AND status<>'rejected'", (body.voice_id, sid)).rowcount
        _rescore(sid)
    return {"segments": n_seg, "waiting": waiting}


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
                  sort: str = "score_desc", offset: int = 0, limit: int = 100, q: str = "", emotion: str = ""):
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
    if emotion == "none":
        where.append("emotion IS NULL")
    elif emotion:
        where.append("emotion=?"); args.append(emotion)
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
    emotion: str | None = None   # "" clears the label


@router.patch("/segments/{seg_id}")
def patch_segment(seg_id: str, body: SegmentPatch):
    upd = {}
    if body.text is not None:
        upd["text"], upd["edited"] = body.text, 1
    if body.status in ("pending", "approved", "rejected"):
        upd["status"] = body.status
    if body.voice_id is not None:
        upd["voice_id"] = body.voice_id or None
    if body.emotion is not None:
        upd["emotion"] = _emotion(body.emotion)
    if "status" in upd and (old := db.get("segments", seg_id)):  # a person's decision replaces the automatic one
        upd["flags"] = autoreview.human_status(old["flags"], upd["status"])
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
    emotion: str | None = None   # "" clears the label


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
    if body.emotion is not None:
        sets.append("emotion=?"); args.append(_emotion(body.emotion))
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


# --- automatic review ------------------------------------------------------------------------------------------

class AutoReviewIn(BaseModel):
    profile: str = "balanced"


def _active_auto_review(voice_id: str) -> dict | None:
    rows = db.query("SELECT * FROM jobs WHERE kind='auto_review' AND status IN ('queued','running') AND params LIKE ?",
                    (f'%"{voice_id}"%',))
    return rows[0] if rows else None


@router.get("/auto-review/{voice_id}")
def auto_review_status(voice_id: str):
    return autoreview.summary(voice_id)


@router.post("/auto-review/{voice_id}")
def auto_review_start(voice_id: str, body: AutoReviewIn):
    if not db.get("voices", voice_id):
        raise HTTPException(404)
    if body.profile not in autoreview.PROFILES:
        raise HTTPException(400, f"unknown profile: {body.profile}")
    return _active_auto_review(voice_id) or jobs.submit(
        "auto_review", {"voice_id": voice_id, "profile": body.profile}, "排隊自動審核")


@router.post("/auto-review/{voice_id}/undo")
def auto_review_undo(voice_id: str):
    if _active_auto_review(voice_id):
        raise HTTPException(409, "自動審核還在進行，請等它結束或先取消。")
    return {"reset": autoreview.undo(voice_id)}


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

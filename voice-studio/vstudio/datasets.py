"""Datasets: frozen, versioned snapshots of a voice's approved segments.

A dataset copies (or hard-links) its audio, so later edits to segments never change a dataset that was already used
for training. Every dataset records the voice's consent at the time it was built; training refuses a dataset
without one.
"""
from __future__ import annotations

import json
import os
import random
import shutil
from pathlib import Path

from . import config, db


class ConsentMissing(Exception):
    pass


def consent_ok(voice: dict) -> bool:
    c = voice.get("consent") or {}
    if not c.get("agreed") or not c.get("signed_name") or not c.get("date"):
        return False
    if voice["kind"] == "other" and not (voice.get("consent_doc") or c.get("document_note")):
        return False
    scope = set(c.get("scope") or [])
    return {"train", "generate"} <= scope


def _link(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def choose_reference(items: list[dict], n: int = 3) -> list[dict]:
    """Best-scoring clean clips of 5–12 s, used where an engine wants reference audio."""
    good = [i for i in items if 5.0 <= i["duration"] <= 12.0] or items
    good.sort(key=lambda i: (-(i.get("score") or 0), abs(i["duration"] - 8.0)))
    return good[:n]


def choose_emotion_references(items: list[dict], taken: set[str], limit: int = 8) -> list[dict]:
    """One reference per labelled emotion (the best clip of that mood), so synthesis can pick the mood it needs."""
    out = []
    for emo in sorted({i["emotion"] for i in items if i.get("emotion")}):
        pick = [i for i in choose_reference([i for i in items if i.get("emotion") == emo], 1) if i["id"] not in taken]
        out += pick
        if len(out) >= limit:
            break
    return out


def split_validation(items: list[dict], val_fraction: float, seed: int) -> set[str]:
    """Hold out whole recordings when there are enough of them, so validation lines are truly unseen
    (neighbouring clips of one recording share room sound and mood). Otherwise hold out random clips."""
    rnd = random.Random(seed)
    want = min(100, max(min(10, len(items) // 10), int(len(items) * val_fraction), 1 if len(items) >= 8 else 0))
    by_src: dict[str, list[dict]] = {}
    for i in items:
        by_src.setdefault(i.get("source") or "", []).append(i)
    if len(by_src) >= 5:
        srcs = list(by_src)
        rnd.shuffle(srcs)
        srcs.sort(key=lambda k: len(by_src[k]))  # small recordings first, so few are sacrificed
        picked: list[dict] = []
        for k in srcs:
            if len(picked) >= want:
                break
            if len(picked) + len(by_src[k]) <= max(want * 2, 12):
                picked += by_src[k]
        if picked:
            return {i["id"] for i in picked}
    order = items[:]
    rnd.shuffle(order)
    return {i["id"] for i in order[:want]}


def build(voice_id: str, name: str, min_score: float = 0.0, val_fraction: float = 0.02, seed: int = 7) -> dict:
    voice = db.get("voices", voice_id)
    if not voice:
        raise KeyError(voice_id)
    if not consent_ok(voice):
        raise ConsentMissing("這個聲音還沒有完整的同意紀錄，不能建立訓練資料。")
    segs = db.query("SELECT * FROM segments WHERE voice_id=? AND status='approved' AND COALESCE(score,1)>=? "
                    "AND text<>'' ORDER BY source_id, start", (voice_id, min_score))
    if not segs:
        raise ValueError("沒有已核可的片段。請先到「檢查資料」核可片段。")
    did = db.new_id("ds")
    root = config.DATA / "datasets" / did
    items = []
    for s in segs:
        dst = root / "wavs" / f"{s['id']}.wav"
        _link(Path(s["path"]), dst)
        items.append({"id": s["id"], "audio": f"wavs/{s['id']}.wav", "text": s["text"], "lang": s["lang"] or "",
                      "duration": round(s["duration"], 3), "score": s["score"], "source": s["source_id"],
                      "emotion": s.get("emotion") or ""})
    val_ids = split_validation(items, val_fraction, seed)
    train_items = [i for i in items if i["id"] not in val_ids]
    refs = choose_reference(train_items)
    refs += choose_emotion_references(train_items, {r["id"] for r in refs})
    with open(root / "train.jsonl", "w", encoding="utf-8") as tr, open(root / "val.jsonl", "w", encoding="utf-8") as va:
        for i in items:
            (va if i["id"] in val_ids else tr).write(json.dumps(i, ensure_ascii=False) + "\n")
    hours = sum(i["duration"] for i in items) / 3600
    langs = sorted({i["lang"] for i in items if i["lang"]})
    meta = {"voice": {"id": voice["id"], "name": voice["name"], "kind": voice["kind"]},
            "consent": voice["consent"], "consent_doc": voice.get("consent_doc"),
            "languages": langs, "n_train": len(items) - len(val_ids), "n_val": len(val_ids),
            "reference": [r["audio"] for r in refs],
            "reference_items": [{k: r[k] for k in ("id", "audio", "text", "lang", "duration", "emotion")} for r in refs],
            "emotions": {e: round(sum(i["duration"] for i in items if i["emotion"] == e) / 60, 1)
                         for e in sorted({i["emotion"] for i in items})},
            "n_sources": len({i["source"] for i in items}), "min_score": min_score, "built_at": db.now()}
    (root / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    return db.insert("datasets", {"id": did, "voice_id": voice_id, "name": name, "n_items": len(items),
                                  "hours": round(hours, 3), "path": str(root), "meta": meta, "created_at": db.now()})


def load_items(ds: dict, split: str = "train") -> list[dict]:
    f = Path(ds["path"]) / f"{split}.jsonl"
    return [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]


def remove(dataset_id: str) -> None:
    ds = db.get("datasets", dataset_id)
    if ds:
        shutil.rmtree(ds["path"], ignore_errors=True)
        db.delete("datasets", dataset_id)

"""Dataset export shared by the real engines: training manifests plus the held-out lines every checkpoint reads."""
from __future__ import annotations

import json
import random
from pathlib import Path

from .. import datasets

MANIFEST_KEYS = ("audio", "text", "duration", "lang")


def _row(it: dict) -> dict:
    return {k: it[k] for k in MANIFEST_KEYS}


def pick_samples(val: list[dict], n: int = 6) -> list[dict]:
    """Up to n held-out lines, balanced across languages, preferring 3–12 s clips with good scores."""
    by_lang: dict[str, list[dict]] = {}
    for it in sorted(val, key=lambda i: (not 3 <= i["duration"] <= 12, -(i.get("score") or 0))):
        by_lang.setdefault(it.get("lang") or "", []).append(it)
    out: list[dict] = []
    while len(out) < n and any(by_lang.values()):
        for lang in list(by_lang):
            if by_lang[lang] and len(out) < n:
                out.append(by_lang[lang].pop(0))
    return [{"id": i["id"], "text": i["text"], "lang": i.get("lang") or "", "audio": i["audio"]} for i in out]


def write(ds: dict, out_dir: Path, ref_fraction: float = 0.0, seed: int = 11) -> dict:
    """train.jsonl / val.jsonl / samples.json in out_dir (paths relative to it; the wavs travel as wavs/).

    ref_fraction > 0 adds a reference clip of the same voice to that share of training lines (VoxCPM recommends
    30–50 % so the model keeps reference-based cloning), taken from a different recording where possible."""
    out_dir.mkdir(parents=True, exist_ok=True)
    train, val = datasets.load_items(ds, "train"), datasets.load_items(ds, "val")
    rnd = random.Random(seed)
    pool = [i for i in train if 3.0 <= i["duration"] <= 15.0]
    if len(pool) < 2:
        pool = train
    n_ref = 0
    with open(out_dir / "train.jsonl", "w", encoding="utf-8") as f:
        for it in train:
            row = _row(it)
            if ref_fraction and rnd.random() < ref_fraction and len(pool) > 1:
                others = [p for p in pool if p["id"] != it["id"] and p.get("source") != it.get("source")]
                ref = rnd.choice(others or [p for p in pool if p["id"] != it["id"]])
                row.update(ref_audio=ref["audio"], ref_duration=ref["duration"])
                n_ref += 1
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(out_dir / "val.jsonl", "w", encoding="utf-8") as f:
        for it in val:
            f.write(json.dumps(_row(it), ensure_ascii=False) + "\n")
    refs = ds["meta"].get("reference_items") or [{"audio": a, "text": ""} for a in ds["meta"].get("reference", [])]
    lines = pick_samples(val)
    if not lines:  # tiny datasets have no held-out lines; fall back to training lines (marked as seen)
        lines = [{**x, "seen": True} for x in pick_samples(train, 3)]
    samples = {"lines": lines, "reference": refs[0] if refs else None}
    (out_dir / "samples.json").write_text(json.dumps(samples, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"n_train": len(train), "n_val": len(val), "n_ref": n_ref, "files": ["train.jsonl", "val.jsonl",
                                                                               "samples.json"]}

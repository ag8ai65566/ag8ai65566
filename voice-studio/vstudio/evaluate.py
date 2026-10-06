"""Score a trained model's checkpoints on the held-out lines they read aloud in the cloud.

For every checkpoint (and the untrained base, for comparison) and every sample clip:
- similarity: speaker-embedding cosine to the voice (its enrollment centroid, else the real held-out recordings);
- accuracy: speech recognition of the clip compared with the line it should have said (1 = word for word).
The recommendation is the most similar checkpoint whose accuracy is within 0.05 of the most accurate one, because
fine-tuning can raise similarity while the model starts to skip or invent words. Listening still decides: the
Models page plays every clip next to the real recording.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from . import audio, config, db, engines, jobs
from .pipeline import asr, prepare, speaker


def _clip(path: Path) -> np.ndarray:
    y, _ = audio.load(path, 16000)
    return y


@jobs.handler("evaluate_model", queue="gpu")
def evaluate_model(ctx: jobs.JobContext) -> dict:
    m = db.get("models", ctx.params["model_id"])
    mdir = Path(m["path"])
    eng = engines.get(m["engine"])
    meta = eng.model_meta(mdir)
    plan = meta.get("samples") or {}
    lines = plan.get("lines", [])
    sdir = mdir / "samples"
    names = ["base"] + [c["name"] for c in meta.get("checkpoints", [])]
    names = [n for n in names if (sdir / n).exists()]
    if not lines or not names:
        return {"message": "沒有可評分的樣本"}
    st = config.load_settings()
    emb = speaker.Embedder()
    target = prepare.voice_centroids([m["voice_id"]]).get(m["voice_id"])
    ds = db.get("datasets", (m["meta"] or {}).get("dataset_id", "")) if m.get("meta") else None
    gt_sims = []
    if ds:
        gts = [Path(ds["path"]) / ln["audio"] for ln in lines if ln.get("audio")]
        gt_embs = [emb.embed(_clip(g)) for g in gts if g.exists()]
        if gt_embs and target is None:
            c = np.mean(gt_embs, axis=0)
            target = c / (np.linalg.norm(c) + 1e-9)
            # the ceiling: each real recording against the others (leave-one-out, so it is not inflated)
            if len(gt_embs) > 1:
                gt_sims = [speaker.cosine(e, np.mean([o for j, o in enumerate(gt_embs) if j != i], axis=0))
                           for i, e in enumerate(gt_embs)]
        elif target is not None:
            gt_sims = [speaker.cosine(e, target) for e in gt_embs]
    if target is None:
        return {"message": "這個聲音沒有登錄片段，也找不到原始資料，無法計算相似度"}

    total = len(names) * len(lines)
    done = 0
    rows = []
    asr_ok = True
    for name in names:
        sims, agrees, clips = [], [], []
        for i, ln in enumerate(lines):
            ctx.check()
            for kind in ("plain", "ref"):
                f = sdir / name / f"{i}_{kind}.wav"
                if not f.exists():
                    continue
                y = _clip(f)
                sim = speaker.cosine(emb.embed(y), target)
                agree = None
                if asr_ok:
                    try:
                        t = asr.transcribe(y, st["asr_secondary"], language=ln.get("lang") or None,
                                           device=st["asr_device"])
                        agree = asr.agreement(ln["text"], t["text"], ln.get("lang") or t["lang"])
                    except Exception:
                        asr_ok = False
                sims.append(sim)
                if agree is not None:
                    agrees.append(agree)
                clips.append({"line": i, "kind": kind, "sim": round(sim, 3),
                              "agree": None if agree is None else round(agree, 3)})
            done += 1
            ctx.progress(done / total, f"評分 {name}")
        rows.append({"name": name, "sim": round(float(np.mean(sims)), 4) if sims else None,
                     "agree": round(float(np.mean(agrees)), 4) if agrees else None, "clips": clips})

    with_weights = {c["name"] for c in meta.get("checkpoints", []) if c.get("weights")}
    cands = [r for r in rows if r["name"] in with_weights and r["sim"] is not None]
    rec = None
    if cands:
        best_agree = max((r["agree"] for r in cands if r["agree"] is not None), default=None)
        ok = [r for r in cands if best_agree is None or r["agree"] is None or r["agree"] >= best_agree - 0.05]
        rec = max(ok or cands, key=lambda r: r["sim"])["name"]
    metrics = {"checkpoints": rows, "recommended": rec,
               "ground_truth_sim": round(float(np.mean(gt_sims)), 4) if gt_sims else None,
               "asr": asr_ok, "evaluated_at": db.now()}
    new_meta = dict(m["meta"] or {})
    if rec and not new_meta.get("checkpoint_chosen_by_user"):
        new_meta["checkpoint"] = rec
    db.update("models", m["id"], {"metrics": metrics, "meta": new_meta})
    return {"recommended": rec, "message": f"評分完成，建議使用 {rec}" if rec else "評分完成"}

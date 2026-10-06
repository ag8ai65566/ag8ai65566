"""Score a trained model's checkpoints on the held-out lines they read aloud in the cloud.

Each sample clip is scored on
- similarity: speaker-embedding cosine to the voice (its enrollment centroid, else the real held-out recordings);
- accuracy: speech recognition of the clip compared with the line it should have said (1 = word for word).

Clips are grouped by generation condition and never mixed: "plain" (the checkpoint alone — what training changed)
and "ref" (with a reference clip — the reference itself carries much of the timbre). The recommendation uses the
"plain" condition, only held-out lines, and only checkpoints whose every clip was scored: the most similar
checkpoint whose accuracy is within 0.05 of the most accurate one. Fine-tuning can raise similarity while the
model starts to skip or invent words, so accuracy gates the choice. Six to twelve lines and one seed are weak
evidence; listening still decides, and the Models page plays every clip next to the real recording.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from . import audio, config, db, engines, jobs
from .pipeline import asr, prepare, speaker

CONDITIONS = ("plain", "ref")


def _clip(path: Path) -> np.ndarray:
    y, _ = audio.load(path, 16000)
    return y


def _transcribe(y: np.ndarray, lang: str | None, st: dict) -> str:
    last: Exception | None = None
    for _ in range(2):  # one retry per clip; a single failure never disables scoring for the rest
        try:
            with jobs.GPU_LOCK:
                return asr.transcribe(y, st["asr_secondary"], language=lang or None, device=st["asr_device"])["text"]
        except (ImportError, ModuleNotFoundError):
            raise
        except Exception as e:
            last = e
    raise RuntimeError(str(last))


def _mean(xs: list[float]) -> float | None:
    xs = [x for x in xs if x is not None and math.isfinite(x)]
    return round(float(np.mean(xs)), 4) if xs else None


@jobs.handler("evaluate_model", queue="gpu")
def evaluate_model(ctx: jobs.JobContext) -> dict:
    m = db.get("models", ctx.params["model_id"])
    mdir = Path(m["path"])
    eng = engines.get(m["engine"])
    meta = eng.model_meta(mdir)
    lines = (meta.get("samples") or {}).get("lines", [])
    sdir = mdir / "samples"
    names = [n for n in ["base"] + [c["name"] for c in meta.get("checkpoints", [])] if (sdir / n).exists()]
    if not lines or not names:
        return {"message": "沒有可評分的樣本"}
    st = config.load_settings()
    from . import tts
    tts.unload()  # scoring needs the GPU for speech recognition; no TTS model should sit in memory meanwhile
    emb = speaker.Embedder()
    target = prepare.voice_centroids([m["voice_id"]]).get(m["voice_id"])
    ds = db.get("datasets", (m["meta"] or {}).get("dataset_id") or "")
    baseline = []
    gt_embs = []
    if ds:
        gts = [Path(ds["path"]) / ln["audio"] for ln in lines if ln.get("audio")]
        gt_embs = [emb.embed(_clip(g)) for g in gts if g.exists()]
    if target is None and gt_embs:
        c = np.mean(gt_embs, axis=0)
        target = c / (np.linalg.norm(c) + 1e-9)
        if len(gt_embs) > 1:  # each real recording against the others (leave-one-out), so it is not inflated
            baseline = [speaker.cosine(e, np.mean([o for j, o in enumerate(gt_embs) if j != i], axis=0))
                        for i, e in enumerate(gt_embs)]
    elif target is not None:
        baseline = [speaker.cosine(e, target) for e in gt_embs]
    if target is None:
        return {"message": "這個聲音沒有登錄聲紋，也找不到原始資料，無法計算相似度"}

    total = len(names) * len(lines)
    done, asr_available, asr_failures = 0, True, 0
    rows = []
    for name in names:
        clips = []
        for i, ln in enumerate(lines):
            ctx.check()
            for kind in CONDITIONS:
                f = sdir / name / f"{i}_{kind}.wav"
                if not f.exists():
                    continue
                y = _clip(f)
                sim = speaker.cosine(emb.embed(y), target)
                agree = None
                if asr_available:
                    try:
                        heard = _transcribe(y, ln.get("lang"), st)
                        agree = asr.agreement(ln["text"], heard, ln.get("lang") or None)
                    except (ImportError, ModuleNotFoundError):
                        asr_available = False
                    except Exception as e:
                        asr_failures += 1
                        ctx.log(f"ASR failed on {name}/{f.name}: {e}")
                clips.append({"line": i, "kind": kind, "sim": round(sim, 4),
                              "agree": None if agree is None else round(agree, 4), "seen": bool(ln.get("seen"))})
            done += 1
            ctx.progress(done / total, f"評分 {name}")
        summary = {}
        any_held_out = any(not ln.get("seen") for ln in lines)
        expected = {i for i, ln in enumerate(lines) if not ln.get("seen") or not any_held_out}
        for kind in CONDITIONS:
            # held-out lines only; a tiny dataset without any still gets numbers, marked as seen-only
            cs = [c for c in clips if c["kind"] == kind and c["line"] in expected]
            if cs:
                complete = ({c["line"] for c in cs} == expected
                            and all(c[k] is not None and math.isfinite(c[k]) for c in cs for k in ("sim", "agree")))
                summary[kind] = {"sim": _mean([c["sim"] for c in cs]), "agree": _mean([c["agree"] for c in cs]),
                                 "n": len(cs), "complete": complete, "seen_only": not any_held_out}
        rows.append({"name": name, "summary": summary, "clips": clips,
                     # kept for older UI code: the "plain" numbers when there are any, else "ref"
                     "sim": (summary.get("plain") or summary.get("ref") or {}).get("sim"),
                     "agree": (summary.get("plain") or summary.get("ref") or {}).get("agree")})

    held_out = sum(1 for ln in lines if not ln.get("seen"))
    with_weights = {c["name"] for c in meta.get("checkpoints", []) if c.get("weights")}
    eligible = [r for r in rows if r["name"] in with_weights and (s := r["summary"].get("plain"))
                and s["complete"] and s["n"] == held_out and s["sim"] is not None and s["agree"] is not None]
    rec, reason = None, ""
    if not held_out:
        reason = "資料太少，所有試念句子都用在訓練裡，無法客觀比較；請用耳朵選。"
    elif not asr_available:
        reason = "這台電腦沒有語音辨識模型，只算了相似度；請用耳朵選。"
    elif not eligible:
        reason = "有檢查點的樣本或辨識結果不完整，沒有自動推薦；請用耳朵選。"
    else:
        best_agree = max(r["summary"]["plain"]["agree"] for r in eligible)
        ok = [r for r in eligible if r["summary"]["plain"]["agree"] >= best_agree - 0.05]
        rec = max(ok, key=lambda r: r["summary"]["plain"]["sim"])["name"]
    base_plain = next((r["summary"].get("plain") for r in rows if r["name"] == "base"), None)
    rec_plain = next((r["summary"]["plain"] for r in rows if r["name"] == rec), None) if rec else None
    improved = None  # unmeasured unless the base read the same lines the same way (Qwen's base can only clone)
    if base_plain and rec_plain and base_plain.get("complete"):
        improved = rec_plain["sim"] > base_plain["sim"] and rec_plain["agree"] >= base_plain["agree"] - 0.05
    metrics = {"checkpoints": rows, "recommended": rec, "reason": reason, "improved_over_base": improved,
               "baseline_sim": _mean(baseline), "asr": asr_available, "asr_failures": asr_failures,
               "held_out_lines": held_out, "conditions": meta.get("sample_conditions") or {},
               "evaluated_at": db.now()}
    new_meta = dict(m["meta"] or {})
    # switch the model's checkpoint only when the pick is measurably better than the untrained base
    if rec and improved is not False and not new_meta.get("checkpoint_chosen_by_user"):
        new_meta["checkpoint"] = rec
    db.update("models", m["id"], {"metrics": metrics, "meta": new_meta})
    return {"recommended": rec, "message": f"評分完成，建議使用 {rec}" if rec else f"評分完成。{reason}"}

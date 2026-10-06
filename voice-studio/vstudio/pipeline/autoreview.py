"""Automatic review: decide most segments without a human listening to them.

Dozens of hours of recordings are hundreds of thousands of seconds of listening. Every segment already carries
signals from the import job; this job adds one more (does the voice stay the same person across the whole clip?)
and sorts each pending segment into one of three piles:

- approved: every check passes with margin (transcript confirmed by two different ASR models, right speaker for the
  whole clip, clean signal, plausible speaking rate);
- rejected: a check fails badly (another person, music or noise, transcript the two models disagree on wildly, a
  rate no person speaks at);
- needs a human: anything in between. These are usually a small share, and the review page lists them first.

A random sample of the approved ones is marked for spot checks, so the person can confirm the thresholds suit their
recordings. Segments a person has already edited or decided are never touched, and the whole run can be undone.
"""
from __future__ import annotations

import random
from pathlib import Path

import numpy as np

from .. import audio, config, db, jobs
from . import prepare, speaker

PROFILES = {
    # agree: two-model transcript agreement; snr in dB; spk_margin over the voice's match threshold;
    # drop: how far the least-similar 2 s window may fall below the clip's typical window
    "strict": {"agree": 0.95, "snr": 22.0, "spk_margin": 0.05, "drop": 0.15, "logprob": -0.5, "no_speech": 0.3},
    "balanced": {"agree": 0.88, "snr": 18.0, "spk_margin": 0.0, "drop": 0.22, "logprob": -0.8, "no_speech": 0.5},
}
AUTO_FLAGS = ("auto_approved", "auto_rejected", "auto_unsure", "spot_check", "spot_ok", "spot_fail")
REASON = {
    "agree": "兩個辨識結果不一致", "snr": "雜音偏多", "clip": "爆音", "speaker": "不像這個人",
    "window": "中途可能換人或有別的聲音", "logprob": "辨識信心低", "no_speech": "可能不是說話（笑聲、音樂）",
    "rate": "字數和長度對不上", "text": "沒有文字", "duration": "長度不適合",
}


def speech_rate(text: str, lang: str | None, seconds: float) -> float:
    """Characters per second for Japanese/Chinese, words per second otherwise."""
    if seconds <= 0:
        return 0.0
    n = len([c for c in text if not c.isspace() and c not in "、。，．,.!?！？「」『』…ー〜"]) \
        if lang in ("ja", "zh", "ko") else len(text.split())
    return n / seconds


def rate_ok(text: str, lang: str | None, seconds: float) -> bool:
    r = speech_rate(text, lang, seconds)
    return (1.0 <= r <= 14.0) if lang in ("ja", "zh", "ko") else (0.6 <= r <= 5.5)


def window_drop(emb: speaker.Embedder, y16: np.ndarray, target: np.ndarray, win: float = 2.0,
                hop: float = 1.0) -> float | None:
    """How much the least-similar 2 s stretch falls below the clip's median: a big drop means part of the clip is
    someone (or something) else, even when the clip as a whole still matches the voice."""
    n, w, h = len(y16), int(16000 * win), int(16000 * hop)
    if n < w + h:
        return None
    sims = [speaker.cosine(emb.embed(y16[i:i + w]), target) for i in range(0, n - w + 1, h)]
    return float(np.median(sims) - min(sims))


def decide(seg: dict, p: dict, threshold: float, drop: float | None) -> tuple[str, list[str]]:
    """('approve' | 'reject' | 'unsure', reasons). Missing measurements never count as a pass."""
    hard, soft = [], []
    agree, snr, clip, sim = seg.get("asr_agree"), seg.get("snr"), seg.get("clip") or 0.0, seg.get("spk_sim")
    lp, ns = seg.get("asr_logprob"), seg.get("no_speech")
    if not seg.get("text"):
        hard.append("text")
    if not 1.0 <= seg["duration"] <= 30.0:
        hard.append("duration")
    if agree is None or agree < p["agree"]:
        (hard if agree is not None and agree < 0.5 else soft).append("agree")
    if snr is None or snr < p["snr"]:
        (hard if snr is not None and snr < 10 else soft).append("snr")
    if clip > 0.001:
        (hard if clip > 0.01 else soft).append("clip")
    if sim is None or sim < threshold + p["spk_margin"]:
        (hard if sim is not None and sim < threshold - 0.15 else soft).append("speaker")
    if drop is not None and drop > p["drop"]:
        (hard if drop > 0.4 else soft).append("window")
    if lp is not None and lp < p["logprob"]:
        soft.append("logprob")
    if ns is not None and ns > p["no_speech"]:
        (hard if ns > 0.8 else soft).append("no_speech")
    if seg.get("text") and not rate_ok(seg["text"], seg.get("lang"), seg["duration"]):
        hard.append("rate")
    if hard:
        return "reject", hard + soft
    return ("unsure", soft) if soft else ("approve", [])


def _clean_flags(flags: list[str]) -> list[str]:
    return [f for f in flags if f not in AUTO_FLAGS and not f.startswith("auto:")]


def human_status(flags: list[str], status: str) -> list[str]:
    """Flags after a person sets a segment's status: the automatic verdict no longer applies (undo leaves it alone),
    and a spot check records whether the person agreed with the automatic approval."""
    out = _clean_flags(flags)
    if "spot_check" in flags and status in ("approved", "rejected"):
        out.append("spot_ok" if status == "approved" else "spot_fail")
    return out


def _target(voice_id: str, emb: speaker.Embedder) -> np.ndarray | None:
    """The voice's enrollment centroid, else the centroid of its most trustworthy segments."""
    c = prepare.voice_centroids([voice_id]).get(voice_id)
    if c is not None:
        return c
    best = db.query("SELECT path FROM segments WHERE voice_id=? AND (status='approved' OR status='pending' "
                    "AND COALESCE(asr_agree,0)>=0.9 AND COALESCE(snr,0)>=20) "
                    "ORDER BY status='approved' DESC, score DESC LIMIT 30", (voice_id,))
    embs = []
    for r in best:
        try:
            y, _ = audio.load(Path(r["path"]), 16000)
            embs.append(emb.embed(y))
        except Exception:
            continue
    if len(embs) < 5:
        return None
    m = np.median(np.array(embs), axis=0)
    return m / (np.linalg.norm(m) + 1e-9)


VERDICT_FLAG = {"approve": "auto_approved", "reject": "auto_rejected", "unsure": "auto_unsure"}
VERDICT_STATUS = {"approve": "approved", "reject": "rejected", "unsure": "pending"}


@jobs.handler("auto_review", queue="gpu")
def auto_review(ctx: jobs.JobContext) -> dict:
    voice_id, profile = ctx.params["voice_id"], ctx.params.get("profile", "balanced")
    p = PROFILES.get(profile, PROFILES["balanced"])
    st = config.load_settings()
    threshold = float(st.get("speaker_match_threshold", 0.62))
    emb = speaker.Embedder()
    target = _target(voice_id, emb)
    if target is None:
        return {"voice_id": voice_id, "message": "還沒有這個聲音的聲紋，無法判斷「是不是本人」。請先到聲音頁登錄聲紋，"
                                                 "或手動核可 5 段以上清楚的片段後再試。"}
    segs = db.query("SELECT * FROM segments WHERE voice_id=? AND status='pending' AND edited=0 ORDER BY id",
                    (voice_id,))
    counts = {"approve": 0, "reject": 0, "unsure": 0}
    minutes = {"approve": 0.0, "reject": 0.0, "unsure": 0.0}
    approved_ids: list[str] = []
    for i, s in enumerate(segs):
        if i % 20 == 0:
            ctx.check()
            ctx.progress(i / max(1, len(segs)), f"自動審核 {i}/{len(segs)}")
        try:
            y, _ = audio.load(Path(s["path"]), 16000)
        except Exception:
            y = None
        # speaker similarity is measured again against one target for every clip: segments assigned by a name hint
        # or a cluster have no (or a stale) similarity from the import
        seg = {**s, "spk_sim": speaker.cosine(emb.embed(y), target) if y is not None and len(y) else None}
        verdict, reasons = decide(seg, p, threshold, None)
        if verdict != "reject" and y is not None:  # the windowed check costs the most, so only when it can matter
            verdict, reasons = decide(seg, p, threshold, window_drop(emb, y, target))
        flags = _clean_flags(s["flags"]) + [VERDICT_FLAG[verdict]] + [f"auto:{r}" for r in reasons]
        with db.tx() as c:  # never overwrite a decision a person made while this job was running
            n = c.execute("UPDATE segments SET status=?, flags=? WHERE id=? AND status='pending' AND edited=0",
                          (VERDICT_STATUS[verdict], db.dump(flags), s["id"])).rowcount
        if not n:
            continue
        counts[verdict] += 1
        minutes[verdict] += s["duration"] / 60
        if verdict == "approve":
            approved_ids.append(s["id"])
    # spot checks: a small random sample of what was approved without anyone listening
    n_spot = min(len(approved_ids), max(10, min(100, len(approved_ids) // 50)))
    for sid in random.Random(7).sample(approved_ids, n_spot):
        s = db.get("segments", sid)
        if s and "auto_approved" in s["flags"]:
            db.update("segments", sid, {"flags": s["flags"] + ["spot_check"]})
    return {"profile": profile, "counts": counts, "minutes": {k: round(v, 1) for k, v in minutes.items()},
            "spot_checks": n_spot, "voice_id": voice_id,
            "message": (f"自動核可 {minutes['approve']:.0f} 分鐘、排除 {minutes['reject']:.0f} 分鐘；"
                        f"需要你聽 {counts['unsure']} 段，抽查 {n_spot} 段")}


def summary(voice_id: str) -> dict:
    """What is left for a person after automatic review, and how the spot checks went."""
    out = {k: 0 for k in ("unsure", "spot_left", "spot_ok", "spot_fail", "auto_approved", "auto_rejected")}
    for s in db.query("SELECT status, flags FROM segments WHERE voice_id=? "
                      "AND (flags LIKE '%\"auto%' OR flags LIKE '%\"spot%')", (voice_id,)):
        f = s["flags"]
        out["unsure"] += "auto_unsure" in f and s["status"] == "pending"
        out["spot_left"] += "spot_check" in f
        out["spot_ok"] += "spot_ok" in f
        out["spot_fail"] += "spot_fail" in f
        out["auto_approved"] += "auto_approved" in f
        out["auto_rejected"] += "auto_rejected" in f
    last = db.query("SELECT id, status, progress, message, result, params, created_at FROM jobs "
                    "WHERE kind='auto_review' AND params LIKE ? ORDER BY created_at DESC LIMIT 1", (f'%"{voice_id}"%',))
    out["job"] = last[0] if last else None
    checked = out["spot_ok"] + out["spot_fail"]
    out["advice"] = ("抽查時你排除了不少自動核可的片段：建議按「復原」，改用「嚴格」再審一次。"
                     if checked >= 10 and out["spot_fail"] / checked > 0.1 else "")
    return out


def undo(voice_id: str) -> int:
    """Put every automatic decision for this voice back to 'pending'. Decisions a person made (or changed) are kept."""
    n = 0
    for s in db.query("SELECT * FROM segments WHERE voice_id=?", (voice_id,)):
        f = s["flags"]
        if not any(x in f for x in AUTO_FLAGS) and not any(x.startswith("auto:") for x in f):
            continue
        upd = {"flags": _clean_flags(f)}
        still_auto = ("auto_approved" in f and s["status"] == "approved") or \
                     ("auto_rejected" in f and s["status"] == "rejected")
        if still_auto and not s["edited"]:
            upd["status"] = "pending"
        db.update("segments", s["id"], upd)
        n += 1
    return n

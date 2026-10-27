"""照著念: say the lines of a recording the way it was said, in your own trained voice.

The recording (anyone's, e.g. a clip you want to re-voice) is only analysed, never used as a voice prompt, so the
result keeps the trained voice's timbre, pitch and habits. From the recording the studio takes:

- the words and where each phrase starts and ends (Whisper with word times), so the lines and pauses match;
- per phrase, how it was said compared with the rest of the clip: louder or quieter, higher or lower, faster or
  slower, lively or flat, rising or falling at the end. These become an emotion label (which picks the voice's own
  reference clip of that mood) and a style hint for the engine. Both are guesses the person can change.

Rendering speaks each phrase with the trained model (several takes; the one closest in length to the original and
best understood wins), optionally stretches it a little to the original timing and follows its loudness, and joins
the phrases with the original pauses.
"""
from __future__ import annotations

import json
import math
import re
import shutil
from pathlib import Path

import numpy as np

from . import audio, config, db, emotions, jobs, phrases
from .pipeline import asr

MAX_SECONDS = 300
GAP_SPLIT = 0.3        # a pause this long between words ends a phrase
MAX_PHRASE = 12.0      # longer phrases are split at their longest pause
END_PUNCT = "。．.!?！？…"
LAUGH = re.compile(r"(笑|[wｗ]{2,}|草|哈哈|haha|lol|あはは|ふふ|へへ|ははは)", re.I)

HINTS = {  # feature → (style words for the engine, label shown to the person)
    "fast": ("fast", "快"), "slow": ("slow", "慢"),
    "loud": ("loud", "大聲"), "quiet": ("quiet", "小聲"),
    "high": ("high pitched", "偏高"), "low": ("low pitched", "偏低"),
    "lively": ("very expressive", "起伏大"), "flat": ("flat, monotone", "平平的"),
    "rising": ("rising at the end", "句尾上揚"), "falling": ("falling at the end", "句尾下降"),
    "breathy": ("whispering", "氣音"),
}


def folder(pid: str) -> Path:
    return config.DATA / "perform" / pid


# --- analysis --------------------------------------------------------------------------------------------------------

def pitch_track(x: np.ndarray, sr: int = 16000, fmin: float = 70, fmax: float = 600) -> tuple[np.ndarray, ...]:
    """f0 (Hz), voiced flags and frame level (dB) every 10 ms. Autocorrelation divided by the window's own
    autocorrelation; the shortest lag that comes close to the best peak is the period (taking the best peak itself
    often lands an octave low). A frame is voiced when that peak is strong and the frame is not near silence."""
    n, h = int(sr * 0.04), int(sr * 0.01)
    frames = (len(x) - n) // h + 1
    if frames <= 0:
        z = np.zeros(0)
        return z, z.astype(bool), z
    idx = np.arange(n)[None, :] + h * np.arange(frames)[:, None]
    win = np.hanning(n)
    f = x[idx] - x[idx].mean(axis=1, keepdims=True)
    level = 10 * np.log10(np.mean(f ** 2, axis=1) + 1e-12)
    f = f * win
    ac = np.fft.irfft(np.abs(np.fft.rfft(f, 2 * n)) ** 2)[:, :n]
    wac = np.fft.irfft(np.abs(np.fft.rfft(win, 2 * n)) ** 2)[:n]
    lo, hi = int(sr / fmax), min(n // 2, int(sr / fmin))
    ac = (ac / (ac[:, :1] + 1e-12) / (wac / wac[0]))[:, lo:hi]
    top = ac.max(axis=1)
    first = np.argmax(ac >= 0.85 * top[:, None], axis=1)
    lag = np.empty(frames, dtype=int)
    for i, j in enumerate(first):  # climb from the first lag near the top to its local peak
        while j + 1 < ac.shape[1] and ac[i, j + 1] >= ac[i, j]:
            j += 1
        lag[i] = j
    voiced = (top > 0.5) & (level > level.max() - 35)
    return sr / (lo + lag), voiced, level


def features(x: np.ndarray, sr: int, text: str, lang: str | None) -> dict:
    """How one phrase was said, in absolute terms (made relative to the whole clip in describe())."""
    f0, voiced, level = pitch_track(x, sr)
    active = level > (level.max() - 30 if len(level) else 0)
    st = 12 * np.log2(f0[voiced] / 100.0) if voiced.any() else np.zeros(0)
    if len(st):  # fold octave slips (a frame read at half or double the period) back next to the phrase's median
        off = st - np.median(st)
        st = np.where(np.abs(off) > 9, st - 12 * np.round(off / 12), st)
    units = asr.normalize(text, lang)
    n_units = len(units.split()) if lang == "en" else len(units.replace(" ", ""))
    dur = len(x) / sr
    out = {"dur": round(dur, 3), "level": round(float(np.mean(level[active])) if active.any() else -90.0, 2),
           "voiced": round(float((voiced & active).sum() / max(1, active.sum())), 3),
           "rate": round(n_units / dur, 3) if dur > 0 else 0.0}
    if len(st) >= 5:
        tail = st[int(len(st) * 0.75):]
        out.update(pitch=round(float(np.median(st)), 2),
                   range=round(float(np.percentile(st, 90) - np.percentile(st, 10)), 2),
                   end=round(float(np.median(tail) - np.median(st)), 2))
    return out


def describe(items: list[dict]) -> None:
    """Compare every phrase with the clip's typical phrase and guess an emotion and a style hint (in place)."""
    def med(key):
        v = [p["f"][key] for p in items if key in p["f"] and p["f"].get("rate", 0) > 0]
        return float(np.median(v)) if v else None
    base = {k: med(k) for k in ("level", "pitch", "range", "rate")}
    for p in items:
        f, tags = p["f"], []
        rel = {"level": f["level"] - base["level"] if base["level"] is not None else 0.0,
               "pitch": f["pitch"] - base["pitch"] if "pitch" in f and base["pitch"] is not None else 0.0,
               "range": f["range"] / base["range"] if "range" in f and base["range"] else 1.0,
               "rate": f["rate"] / base["rate"] if base["rate"] else 1.0,
               "end": f.get("end", 0.0)}
        p["rel"] = {k: round(v, 2) for k, v in rel.items()}
        if len(items) > 1:
            tags += ["fast"] if rel["rate"] >= 1.15 else ["slow"] if rel["rate"] <= 0.87 else []
            tags += ["loud"] if rel["level"] >= 4 else ["quiet"] if rel["level"] <= -4 else []
            tags += ["high"] if rel["pitch"] >= 2 else ["low"] if rel["pitch"] <= -2 else []
            tags += ["lively"] if rel["range"] >= 1.35 else ["flat"] if rel["range"] <= 0.65 else []
        tags += ["rising"] if rel["end"] >= 2.5 else ["falling"] if rel["end"] <= -3 else []
        breathy = f["voiced"] < 0.3 and f["dur"] > 0.6
        if breathy:
            tags.append("breathy")
        if breathy:
            emo = "whisper"
        elif LAUGH.search(p["text"]):
            emo = "laughing"
        elif rel["level"] >= 4 and rel["pitch"] >= 2:
            emo = "excited"
        elif rel["level"] >= 4 and rel["rate"] >= 1.05:
            emo = "angry"
        elif rel["end"] >= 4 and rel["pitch"] >= 2:
            emo = "surprised"
        elif rel["level"] <= -4:
            emo = "soft"
        elif rel["pitch"] <= -1.5 and rel["rate"] <= 0.88 and rel["range"] < 0.9:
            emo = "sad"
        else:
            emo = ""
        p["tags"] = tags
        p["guess"] = {"emotion": emo, "style": ", ".join(HINTS[t][0] for t in tags)}
        p.setdefault("emotion", emo)
        p.setdefault("style", p["guess"]["style"])


def split_phrases(words: list[dict]) -> list[dict]:
    """Group words into phrases at pauses (≥ 0.3 s) and sentence ends; phrases over 12 s split at their longest gap."""
    groups, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        gap = nxt["start"] - w["end"] if nxt else 99
        long_enough = w["end"] - cur[0]["start"] >= 1.2
        if gap >= GAP_SPLIT or (w["word"].strip()[-1:] in END_PUNCT and long_enough and gap >= 0.12):
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    out: list[list[dict]] = []
    stack = groups[::-1]
    while stack:
        g = stack.pop()
        if g[-1]["end"] - g[0]["start"] > MAX_PHRASE and len(g) > 1:
            k = max(range(len(g) - 1), key=lambda j: g[j + 1]["start"] - g[j]["end"]) + 1
            stack += [g[k:], g[:k]]
        else:
            out.append(g)
    return [{"start": round(g[0]["start"], 3), "end": round(g[-1]["end"], 3),
             "text": "".join(w["word"] for w in g).strip()} for g in out]


# --- long text: the same per-line rendering, from text instead of a recording -------------------------------------

MAX_TEXT = 20000
SENT_END = re.compile(r"(?<=[。．！？!?…])[」』）)\"'”’]*\s*|(?<=[.!?])[\"'”’)]*\s+(?=[A-Z\[\"“'‘(]|$)")
TAG_AT_START = re.compile(r"^\s*((?:\[[^\[\]]{1,40}\]\s*)+)")
PAUSE_SENTENCE, PAUSE_PARAGRAPH = 0.35, 0.8


def _cut_long(sent: str, limit: int) -> list[str]:
    """Split an over-long sentence at commas (、，,;；), then hard at the limit."""
    if len(sent) <= limit:
        return [sent]
    parts, cur = [], ""
    for piece in re.split(r"(?<=[、，,;；：:])", sent):
        if cur and len(cur) + len(piece) > limit:
            parts.append(cur)
            cur = ""
        cur += piece
    if cur:
        parts.append(cur)
    out = []
    for x in parts:
        out += [x[i:i + limit] for i in range(0, len(x), limit)]
    return out


def split_text(text: str) -> list[dict]:
    """Lines to speak one by one: sentences within paragraphs (blank-line or line-break separated). A [tag] at the
    start of a paragraph colours every sentence of it that has no tag of its own, as in ElevenLabs scripts."""
    lines: list[dict] = []
    for para in re.split(r"\n+", text.replace("\r", "")):
        para = para.strip()
        if not para:
            continue
        m = TAG_AT_START.match(para)
        lead_tag = m.group(1).strip() if m else ""
        sents = [x.strip() for x in SENT_END.split(para) if x and x.strip()]
        cjk = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", para)) > len(para) / 4
        limit = 120 if cjk else 280
        pieces = [c.strip() for x in sents for c in _cut_long(x, limit) if c.strip()]
        # very short pieces (a lone "えっと。", "Yes.") ride with the next one (the last with the one before), so
        # the engine has some context to say them naturally
        def short(c: str) -> bool:
            bare = re.sub(r"\[[^\]]*\]", "", c).strip()
            return len(bare) <= 5 if cjk else len(bare.split()) <= 2
        join = (lambda a, b: a + b) if cjk else (lambda a, b: f"{a} {b}")
        merged: list[str] = []
        carry = ""
        for c in pieces:
            c = join(carry, c) if carry else c
            carry = ""
            if short(c):
                carry = c
            else:
                merged.append(c)
        if carry:
            if merged:
                merged[-1] = join(merged[-1], carry)
            else:
                merged.append(carry)
        for j, c in enumerate(merged):
            if lead_tag and j > 0 and not TAG_AT_START.match(c):
                c = f"{lead_tag} {c}"
            lines.append({"i": len(lines), "text": c, "emotion": "", "style": "", "skip": False,
                          "pause": PAUSE_PARAGRAPH if j == len(merged) - 1 else PAUSE_SENTENCE})
    if lines:
        lines[-1]["pause"] = 0.0
    return lines


@jobs.handler("perform_analyze", queue="gpu")
def perform_analyze(ctx: jobs.JobContext) -> dict:
    try:
        return _analyze(ctx)
    except Exception as e:
        db.update("performances", ctx.params["perform_id"], {"status": "failed", "result": {"error": str(e)[:300]}})
        raise


def _analyze(ctx: jobs.JobContext) -> dict:
    pid = ctx.params["perform_id"]
    rec = db.get("performances", pid)
    d = folder(pid)
    st = config.load_settings()
    from . import tts
    tts.unload()  # free the GPU for speech recognition
    ctx.progress(0.05, "解碼音訊")
    src = Path(rec["path"])
    master = d / "source.wav"
    if src.exists():  # the upload is decoded once (first 5 minutes) and then removed
        audio.extract(src, master, sr=audio.MASTER_SR, dur=MAX_SECONDS)
        if rec["meta"].get("copied"):
            src.unlink(missing_ok=True)
    if ctx.params.get("separate"):
        ctx.progress(0.1, "分離人聲（去背景音樂）")
        from .pipeline import separate
        with jobs.GPU_LOCK:
            voc = separate.vocals(master, d / "separated")
        x48, _ = audio.load(voc, audio.MASTER_SR)
        audio.save(master, x48, audio.MASTER_SR)
        shutil.rmtree(d / "separated", ignore_errors=True)
    x48, _ = audio.load(master)
    x16 = audio.resample(x48, audio.MASTER_SR, 16000)
    ctx.progress(0.25, "辨識台詞和每個字的時間")
    with jobs.GPU_LOCK:
        t = asr.transcribe_words(x16, st["asr_primary"], language=rec.get("lang") or None, device=st["asr_device"])
    lang = t["lang"]
    ctx.progress(0.8, "分析語氣")
    items = split_phrases(t["words"])
    for p in items:
        a, b = int(max(0, p["start"] - 0.03) * 16000), int((p["end"] + 0.03) * 16000)
        p["f"] = features(x16[a:b], 16000, p["text"], lang)
    describe(items)
    for i, p in enumerate(items):
        nxt = items[i + 1]["start"] if i + 1 < len(items) else None
        p.update(i=i, pause=round(min(3.0, max(0.05, nxt - p["end"])), 2) if nxt is not None else 0.0, skip=False)
    if not items:
        raise RuntimeError("沒有聽到說話。換一段人聲清楚的錄音，或勾選去除背景音樂。")
    db.update("performances", pid, {"status": "ready", "lang": lang, "phrases": items,
                                    "duration": round(len(x48) / audio.MASTER_SR, 2)})
    return {"phrases": len(items), "message": f"分析完成：{len(items)} 句"}


# --- rendering -------------------------------------------------------------------------------------------------------

def _active_db(y: np.ndarray, sr: int) -> float:
    frame = max(1, int(sr * 0.02))
    n = len(y) // frame
    if n < 2:
        return -90.0
    e = 10 * np.log10(np.mean(y[: n * frame].reshape(n, frame) ** 2, axis=1) + 1e-12)
    return float(np.mean(e[e > e.max() - 30]))


def pick_take(outs: list[dict], target: float | None) -> tuple[dict, np.ndarray, int]:
    """The take that is understood best and closest in length to the original phrase (without an original: the
    take the engine run ranked best)."""
    best = None
    for o in outs:
        y, sr = audio.load(Path(o["path"]))
        y = phrases.trim(y, sr, pad=0.04)
        m = o["score"].get("match")
        if target is None:
            score = 1.0 if o["score"].get("best") else (m if m is not None else 0.0)
        else:
            score = (m if m is not None else 0.5) - 0.6 * abs(math.log(max(len(y) / sr, 0.05) / max(target, 0.05)))
        if best is None or score > best[0]:
            best = (score, o, y, sr)
    return best[1], best[2], best[3]


@jobs.handler("perform_render", queue="gpu")
def perform_render(ctx: jobs.JobContext) -> dict:
    pid = ctx.params["perform_id"]
    before = db.get("performances", pid)
    db.update("performances", pid, {"status": "rendering"})
    try:
        return _render(ctx)
    except Exception as e:
        db.update("performances", pid, {"status": "done" if (before["result"] or {}).get("output_id") else "ready",
                                        "result": {**(before["result"] or {}), "error": str(e)[:300]}})
        raise


def _render(ctx: jobs.JobContext) -> dict:
    from . import tts
    p = ctx.params
    pid = p["perform_id"]
    rec = db.get("performances", pid)
    d = folder(pid)
    items = [x for x in rec["phrases"] if not x.get("skip") and x["text"].strip()]
    only = set(p.get("only") or [])
    prev = {x["i"]: x for x in (rec["result"] or {}).get("phrases", [])} if only else {}
    if only and not all((d / f"p{i}.wav").exists() and prev.get(i, {}).get("model_id") == p["model_id"]
                        for x in items for i in [x["i"]] if i not in only):
        only = set()  # other phrases are from another model or missing: render everything
    sr_out = audio.MASTER_SR
    sheet, pieces = [], []
    todo = [x for x in items if not only or x["i"] in only]
    for x in items:
        if only and x["i"] not in only:
            y, _ = audio.load(d / f"p{x['i']}.wav", sr_out)
            sheet.append({k: v for k, v in prev[x["i"]].items() if k != "gain_db"})
            pieces.append((x, y))
            continue
        k = len([t for t in todo if t["i"] <= x["i"]])
        ctx.progress((k - 1) / max(1, len(todo)), f"第 {k}/{len(todo)} 句")
        # a line's own emotion wins, then a [tag] in it, then the default chosen for the whole text
        emo = x.get("emotion") or (None if emotions.from_text_tags(x["text"]) else p.get("emotion")) or None
        res = tts.generate(p["model_id"], x["text"], language=rec.get("lang"),
                           style=x.get("style") or p.get("style") or "", takes=int(p.get("takes", 3)),
                           mode=p.get("mode"), emotion=emo, phrases=bool(p.get("phrases", True)),
                           batch=f"perf_{pid}")
        timed = "start" in x  # follows a recording; lines from text have no timing to match
        target = x["end"] - x["start"] if timed else None
        best, y, sr = pick_take(res["outputs"], target)
        y = audio.resample(y, sr, sr_out)
        ratio = 1.0
        if timed and p.get("match_timing", True):
            ratio = float(np.clip(target / max(len(y) / sr_out, 0.05), 0.8, 1.25))
            y = audio.stretch(y, sr_out, ratio)
        audio.save(d / f"p{x['i']}.wav", y, sr_out, synthetic={"perform": pid, "model": p["model_id"]})
        pieces.append((x, y))
        sheet.append({"i": x["i"], "model_id": p["model_id"], "match": best["score"].get("match"),
                      "heard": best["score"].get("heard"), "emotion": res.get("emotion"), "takes": len(res["outputs"]),
                      "stretch": round(ratio, 3), "original": round(target, 2) if timed else None,
                      "spoken": round(len(y) / sr_out, 2)})
        for o in res["outputs"]:  # each phrase is kept as p<i>.wav; only the joined result goes to the output list
            Path(o["path"]).unlink(missing_ok=True)
            db.delete("outputs", o["id"])
    if not pieces:
        raise ValueError("沒有要念的句子")
    # follow the original's loudness from phrase to phrase (±6 dB), around the voice's own level
    if p.get("follow_level", True) and all("rel" in x for x, _ in pieces):
        lv = [_active_db(y, sr_out) for _, y in pieces]
        mid = float(np.median(lv))
        for j, ((x, y), cur) in enumerate(zip(pieces, lv)):
            g = float(np.clip(x.get("rel", {}).get("level", 0.0) - (cur - mid), -6, 6))
            pieces[j] = (x, y * 10 ** (g / 20))
            sheet[j] = {**sheet[j], "gain_db": round(g, 1)}
    keep = p.get("keep_pauses", True)
    lead = min(items[0]["start"], 0.8) if keep and "start" in items[0] else 0.2
    joined = [(np.zeros(int(sr_out * lead), np.float32), 0.0)]
    for j, (x, y) in enumerate(pieces):
        gap = (x.get("pause") or 0.0) if keep else 0.35
        joined.append((y, gap if j < len(pieces) - 1 else 0.3))
    mix = audio.concat(joined, sr_out)
    peak = float(np.max(np.abs(mix))) if len(mix) else 0
    if peak > 0.89:
        mix = mix * (0.89 / peak)
    old = (rec["result"] or {}).get("output_id")
    if old:
        o = db.get("outputs", old)
        if o:
            Path(o["path"]).unlink(missing_ok=True)
            Path(o["path"]).with_suffix(".mp3").unlink(missing_ok=True)
            db.delete("outputs", old)
    oid = db.new_id("out")
    path = audio.save(config.DATA / "outputs" / f"{oid}.wav", mix, sr_out,
                      synthetic={"perform": pid, "model": p["model_id"]})
    text = "\n".join(x["text"] for x, _ in pieces)
    db.insert("outputs", {"id": oid, "model_id": p["model_id"], "text": text[:2000],
                          "params": {"perform": pid, "mode": p.get("mode"), "language": rec.get("lang")},
                          "path": str(path), "duration": round(len(mix) / sr_out, 2),
                          "score": {"best": True, "lines": len(pieces)}, "batch": f"perf_{pid}", "created_at": db.now()})
    result = {"output_id": oid, "model_id": p["model_id"], "phrases": sheet,
              "options": {k: p.get(k) for k in ("mode", "takes", "keep_pauses", "match_timing", "follow_level",
                                                "phrases")}}
    db.update("performances", pid, {"status": "done", "result": result})
    (d / "sheet.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"output_id": oid, "message": f"完成：{len(pieces)} 句"}


def phrase_tags(p: dict) -> list[str]:
    return [HINTS[t][1] for t in p.get("tags", [])]


def valid_emotion(e: str | None) -> str:
    return e if e and emotions.valid(e) else ""

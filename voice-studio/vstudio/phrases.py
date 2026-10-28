"""Catchphrases: the few phrases that make a person sound like themselves.

A voice keeps a short list of phrases, each with one canonical spelling, other spellings speech recognition tends
to produce, and a few original recordings of the phrase (in different moods). They are used to
- spell the phrase the same way in every transcript (a hint to speech recognition at import, and "unify" afterwards),
  so the model learns one phrase instead of three half-phrases;
- count how often the phrase is in the training data;
- splice the original recording into synthesized speech: a line that is just the phrase plays the recording; a line
  that starts with it plays the recording and lets the model continue from it (the model hears the original and
  speaks on in the same flow); elsewhere the recording is joined between synthesized parts;
- check how a trained model says the phrase on its own, against the original.

A phrase written as a bracket tag, e.g. "[喘氣]" or "[sigh]", is a sound rather than words: breathing, a sigh, panting,
a wordless moan. Speech recognition never writes it and a model cannot be asked to say it, so it only does the third
job: where the tag is in a line, the person's own recording of that sound is played.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

import numpy as np

from . import audio, config, db, emotions, jobs

SCORE_FLAGS = {"asr_disagree", "noisy", "clipping", "unknown_speaker", "overlap", "no_text"}
PUNCT = "、。，．,.!?！？…〜~ー「」『』\"'（）()　 "
BRACKETS = str.maketrans({"［": "[", "【": "[", "〔": "[", "］": "]", "】": "]", "〕": "]"})
TAG_SPAN = re.compile(r"\[[^\[\]]*\]")


def is_sound(ph: dict | str) -> bool:
    """A sound tag such as "[喘氣]": played from the person's recording, never spoken or transcribed."""
    t = ph if isinstance(ph, str) else ph["text"]
    return len(t) > 2 and t.startswith("[") and t.endswith("]")


def as_tag(x: str) -> str:
    x = x.translate(BRACKETS).strip()
    inner = x.strip("[] ").strip()
    return f"[{inner}]" if inner else ""


def _clean_list(xs) -> list[str]:
    out: list[str] = []
    for x in xs or []:
        x = str(x).strip()
        if x and x not in out:
            out.append(x)
    return out


def get(pid: str) -> dict:
    ph = db.get("catchphrases", pid)
    if not ph:
        raise KeyError(pid)
    return ph


def list_for_voice(voice_id: str) -> list[dict]:
    return db.query("SELECT * FROM catchphrases WHERE voice_id=? ORDER BY created_at", (voice_id,))


def with_clips(voice_id: str) -> list[dict]:
    return [p for p in list_for_voice(voice_id) if p["clips"]]


def create(voice_id: str, text: str, variants=(), lang: str | None = None) -> dict:
    if not db.get("voices", voice_id):
        raise KeyError(voice_id)
    text, variants = _normalise(text, variants)
    if not text or len(text) > 60:
        raise ValueError("口頭禪要有 1–60 個字")
    if any(p["text"].lower() == text.lower() for p in list_for_voice(voice_id)):
        raise ValueError(f"「{text}」已經在清單裡")
    return db.insert("catchphrases", {"id": db.new_id("phr"), "voice_id": voice_id, "text": text,
                                      "variants": [v for v in variants if v != text],
                                      "lang": lang or None, "clips": [], "checks": {}, "created_at": db.now()})


def _normalise(text: str, variants=()) -> tuple[str, list[str]]:
    """Trim; a sound tag gets half-width brackets, and so do its other spellings ("panting" → "[panting]")."""
    text = text.translate(BRACKETS).strip()
    variants = _clean_list(variants)
    if is_sound(text):
        text = as_tag(text)
        variants = _clean_list(as_tag(v) for v in variants)
    return text, variants


def update(pid: str, text: str | None = None, variants=None, lang: str | None = None) -> dict:
    ph = get(pid)
    upd: dict = {}
    if text is not None:
        text, _ = _normalise(text)
        if not text or len(text) > 60:
            raise ValueError("口頭禪要有 1–60 個字")
        if is_sound(text) != is_sound(ph):
            raise ValueError("聲音標籤和口頭禪不能互換，請刪掉重新登記")
        upd["text"] = text
    if variants is not None:
        canon = upd.get("text", ph["text"])
        _, vs = _normalise(canon, variants)
        upd["variants"] = [v for v in vs if v != canon]
    if lang is not None:
        upd["lang"] = lang or None
    return db.update("catchphrases", pid, upd)


def delete(pid: str) -> None:
    ph = get(pid)
    shutil.rmtree(_dir(ph), ignore_errors=True)
    db.delete("catchphrases", pid)


# --- finding a phrase in text -------------------------------------------------------------------------------------

def _pattern(form: str) -> re.Pattern:
    """English spellings match whole words, any case; Japanese/Chinese ones match anywhere. A sound tag matches the
    tag with any spacing and case inside the brackets ("[ Sigh ]" = "[sigh]")."""
    if is_sound(form):
        return re.compile(r"\[\s*" + re.escape(form[1:-1].strip()) + r"\s*\]", re.IGNORECASE)
    if form.isascii():
        return re.compile(r"(?<![A-Za-z0-9'])" + re.escape(form) + r"(?![A-Za-z0-9'])", re.IGNORECASE)
    return re.compile(re.escape(form))


def find(text: str, phrases: list[dict]) -> list[tuple[int, int, dict]]:
    """Non-overlapping occurrences of any phrase in any of its spellings, longest spellings first. Words inside a
    [tag] are not the phrase being said ("[sighs]" does not contain the phrase "sigh")."""
    forms = sorted(((f, p) for p in phrases for f in [p["text"], *p["variants"]] if f), key=lambda x: -len(x[0]))
    sounds = [_pattern(f) for f, p in forms if is_sound(p)]
    taken = [(m.start(), m.end()) for m in TAG_SPAN.finditer(text)
             if not any(s.fullmatch(m.group()) for s in sounds)]
    out: list[tuple[int, int, dict]] = []
    for form, ph in forms:
        for m in _pattern(form).finditer(text):
            if any(m.start() < b and a < m.end() for a, b in taken):
                continue
            taken.append((m.start(), m.end()))
            out.append((m.start(), m.end(), ph))
    return sorted(out, key=lambda x: x[0])


def _unify_text(text: str, ph: dict) -> str:
    for v in sorted(ph["variants"], key=len, reverse=True):
        text = _pattern(v).sub(ph["text"], text)
    return text


def counts(voice_id: str) -> dict[str, dict]:
    """Per phrase: segments (not rejected) with the canonical spelling, how many approved, and how many still use
    another spelling."""
    segs = db.query("SELECT text, status FROM segments WHERE voice_id=? AND status<>'rejected'", (voice_id,))
    out = {}
    for ph in list_for_voice(voice_id):
        if is_sound(ph):
            continue
        canon = _pattern(ph["text"])
        others = [_pattern(v) for v in ph["variants"]]
        c = {"segments": 0, "approved": 0, "other_spellings": 0}
        for s in segs:
            if canon.search(s["text"]):
                c["segments"] += 1
                c["approved"] += s["status"] == "approved"
            if any(o.search(s["text"]) for o in others):
                c["other_spellings"] += 1
        out[ph["id"]] = c
    return out


def unify(voice_id: str, pid: str | None = None) -> int:
    """Rewrite other spellings to the canonical one in this voice's transcripts (both recognisers' versions, so the
    agreement score stays meaningful). Spelling is mechanical, so segments are not marked as edited by a person."""
    from .pipeline import asr, prepare
    phs = [get(pid)] if pid else list_for_voice(voice_id)
    phs = [p for p in phs if p["variants"] and p["voice_id"] == voice_id and not is_sound(p)]
    if not phs:
        return 0
    changed = 0
    for s in db.query("SELECT * FROM segments WHERE voice_id=?", (voice_id,)):
        text, alt = s["text"], s["text_alt"]
        for ph in phs:
            text, alt = _unify_text(text, ph), _unify_text(alt, ph)
        if text == s["text"] and alt == s["text_alt"]:
            continue
        agree = asr.agreement(text, alt, s["lang"] or None) if alt else s["asr_agree"]
        sc, fl = prepare.score({**s, "text": text, "asr_agree": agree, "ambiguous": "overlap" in s["flags"]})
        keep = [f for f in s["flags"] if f not in SCORE_FLAGS]  # automatic-review and spot-check marks stay
        db.update("segments", s["id"], {"text": text, "text_alt": alt, "asr_agree": agree, "score": sc,
                                        "flags": fl + [f for f in keep if f not in fl]})
        changed += 1
    return changed


def asr_prompt(voice_id: str | None, lang: str | None) -> str:
    """The voice's phrases as a hint to speech recognition, so they are written with the canonical spelling."""
    if not voice_id or not lang:
        return ""
    texts = [p["text"] for p in list_for_voice(voice_id)
             if not is_sound(p) and (not p["lang"] or p["lang"] == lang)][:12]
    if not texts:
        return ""
    return ("、".join(texts) + "。") if lang in ("ja", "zh") else (", ".join(texts) + ".")


# --- original recordings ------------------------------------------------------------------------------------------

def _dir(ph: dict) -> Path:
    return config.DATA / "voices" / ph["voice_id"] / "phrases" / ph["id"]


def clip_path(ph: dict, cid: str) -> Path:
    c = next((c for c in ph["clips"] if c["id"] == cid), None)
    if c is None:
        raise KeyError(cid)
    root = _dir(ph).resolve()
    f = (root / c["file"]).resolve()
    if f.parent != root:
        raise ValueError("不合法的片段路徑")
    return f


def trim(y: np.ndarray, sr: int, pad: float = 0.04) -> np.ndarray:
    """Cut leading and trailing silence (frames 40 dB under the loudest), keeping a few ms so nothing is clipped."""
    if len(y) == 0:
        return y
    frame = max(1, int(sr * 0.01))
    n = len(y) // frame
    if n < 3:
        return y
    e = 10 * np.log10(np.mean(y[: n * frame].reshape(n, frame) ** 2, axis=1) + 1e-12)
    on = np.where(e > max(e.max() - 40, -60))[0]
    if not len(on):
        return y
    a = max(0, on[0] * frame - int(pad * sr))
    b = min(len(y), (on[-1] + 1) * frame + int(pad * sr))
    return y[a:b]


def _add(pid: str, y: np.ndarray, sr: int, emotion: str | None, source: str,
         speech_rms: float | None = None) -> dict:
    ph = get(pid)
    if emotion and not emotions.valid(emotion):
        raise ValueError(f"unknown emotion: {emotion}")
    y = trim(audio.resample(y, sr, audio.MASTER_SR), audio.MASTER_SR)
    dur = len(y) / audio.MASTER_SR
    if not 0.2 <= dur <= 10.0:
        raise ValueError(f"原音片段要 0.2–10 秒（去掉前後靜音後是 {dur:.1f} 秒）")
    cid = db.new_id("clip")
    audio.save(_dir(ph) / f"{cid}.wav", y, audio.MASTER_SR)
    clip = {"id": cid, "file": f"{cid}.wav", "emotion": emotion or "", "duration": round(dur, 3), "from": source}
    if speech_rms and is_sound(ph):
        clip["speech_rms"] = round(float(speech_rms), 6)  # the person's speech level next to it (see match_level)
    return db.update("catchphrases", pid, {"clips": list(ph["clips"]) + [clip]})


def speech_level(source_id: str) -> float | None:
    """How loud the person speaks in a recording: the median over a few of its transcribed segments."""
    levels = []
    for r in db.query("SELECT path FROM segments WHERE source_id=? AND text<>'' AND status<>'rejected' "
                      "ORDER BY score DESC LIMIT 6", (source_id,)):
        try:
            y, sr = audio.load(Path(r["path"]))
        except Exception:
            continue
        levels.append(_active_rms(y, sr))
    return float(np.median(levels)) if levels else None


def add_clip_file(pid: str, src: Path, emotion: str | None, name: str = "") -> dict:
    tmp = config.path("tmp", f"{db.new_id('up')}.wav")
    try:
        audio.extract(src, tmp, sr=audio.MASTER_SR)
        y, sr = audio.load(tmp)
    finally:
        tmp.unlink(missing_ok=True)
    return _add(pid, y, sr, emotion, name or src.name)


def add_clip_segment(pid: str, segment_id: str, start: float, end: float, emotion: str | None) -> dict:
    ph = get(pid)
    s = db.get("segments", segment_id)
    if not s:
        raise KeyError(segment_id)
    if s["voice_id"] != ph["voice_id"]:
        raise ValueError("只能用同一個聲音的片段")
    y, sr = audio.load(Path(s["path"]))
    a, b = max(0.0, float(start)), min(len(y) / sr, float(end))
    if b - a < 0.2:
        raise ValueError("選取的範圍太短")
    return _add(pid, y[int(a * sr):int(b * sr)], sr, emotion if emotion is not None else s.get("emotion"),
                f"{segment_id} {a:.2f}–{b:.2f}s", speech_level(s["source_id"]) if is_sound(ph) else None)


def source_has_voice(source_id: str, voice_id: str) -> bool:
    src = db.get("sources", source_id)
    return bool(src) and (src.get("voice_hint") == voice_id or bool(db.query(
        "SELECT 1 FROM segments WHERE source_id=? AND voice_id=? LIMIT 1", (source_id, voice_id))))


def add_clip_source(pid: str, source_id: str, start: float, end: float, emotion: str | None) -> dict:
    """Cut a recording out of an imported recording (its processed copy), also between the cut segments: that is
    where a sigh or a breath on its own usually is."""
    import soundfile as sf
    ph = get(pid)
    if not db.get("sources", source_id):
        raise KeyError(source_id)
    if not source_has_voice(source_id, ph["voice_id"]):
        raise ValueError("只能用同一個聲音的錄音")
    master = config.DATA / "sources" / source_id / "master.wav"
    if not master.exists():
        raise ValueError("這段錄音的處理檔已經不在了，請改從片段剪或上傳檔案")
    info = sf.info(str(master))
    a, b = max(0.0, float(start)), min(info.duration, float(end))
    if b - a < 0.2:
        raise ValueError("選取的範圍太短")
    y, sr = sf.read(str(master), start=int(a * info.samplerate), stop=int(b * info.samplerate), dtype="float32",
                    always_2d=True)
    return _add(pid, y.mean(axis=1), sr, emotion, f"{source_id} {a:.2f}–{b:.2f}s", speech_level(source_id))


def remove_clip(pid: str, cid: str) -> dict:
    ph = get(pid)
    clip_path(ph, cid).unlink(missing_ok=True)
    return db.update("catchphrases", pid, {"clips": [c for c in ph["clips"] if c["id"] != cid]})


def set_clip_emotion(pid: str, cid: str, emotion: str) -> dict:
    ph = get(pid)
    if emotion and not emotions.valid(emotion):
        raise ValueError(f"unknown emotion: {emotion}")
    clips = [{**c, "emotion": emotion or ""} if c["id"] == cid else c for c in ph["clips"]]
    return db.update("catchphrases", pid, {"clips": clips})


def pick_clip(ph: dict, emotion: str | None, k: int = 0) -> dict | None:
    """A recording in the wanted mood, else the nearest mood (emotions.NEAR), else a calm or unlabelled one, else
    any; takes rotate through equals."""
    clips = ph["clips"]
    if not clips:
        return None
    pool = next((m for e in emotions.chain(emotion) if (m := [c for c in clips if c.get("emotion") == e])), None)
    pool = pool or [c for c in clips if c.get("emotion") in ("", "neutral")] or clips
    return pool[k % len(pool)]


# --- splicing into synthesized speech ------------------------------------------------------------------------------

def plan(text: str, phrases: list[dict]) -> list[dict]:
    """Split a line into synthesized parts and original-recording parts. Punctuation right after a phrase stays
    with it (it is part of how the phrase was said). Empty text parts are dropped."""
    hits = [h for h in find(text, phrases) if h[2]["clips"]]
    if not hits:
        return []
    parts: list[dict] = []
    pos = 0
    for a, b, ph in hits:
        if a > pos:
            parts.append({"kind": "tts", "text": text[pos:a]})
        tail = b
        while tail < len(text) and text[tail] in PUNCT:
            tail += 1
        parts.append({"kind": "clip", "phrase": ph, "said": text[a:tail]})
        pos = tail
    if pos < len(text):
        parts.append({"kind": "tts", "text": text[pos:]})
    return [p for p in parts if p["kind"] == "clip" or p["text"].strip(PUNCT)]


def sound_for(name: str, sounds: list[dict]) -> dict | None:
    """The sound tag with recordings that a [name] in a line plays: the same name, one of its other spellings, or
    another name of the same tag in tags.py ([panting] and [はぁはぁ] play the recordings of [喘氣])."""
    from . import tags
    for p in sounds:
        if p["clips"] and any(tags.same(f[1:-1], name) for f in [p["text"], *p["variants"]] if is_sound(f)):
            return p
    return None


def gap_after(part: dict) -> float:
    """Silence after a part, from the punctuation it ends with."""
    t = (part.get("said") or part.get("text") or "").rstrip(" 　")
    if t[-1:] in "。．.!?！？…":
        return 0.28
    if t[-1:] in "、，,〜~":
        return 0.14
    return 0.04


def _active_rms(y: np.ndarray, sr: int) -> float:
    frame = max(1, int(sr * 0.02))
    n = len(y) // frame
    if n < 1:
        return float(np.sqrt(np.mean(y ** 2) + 1e-12))
    e = np.mean(y[: n * frame].reshape(n, frame) ** 2, axis=1)
    loud = e[e > e.max() * 10 ** (-35 / 10)]
    return float(np.sqrt(np.mean(loud) + 1e-12))


def match_level(clip: np.ndarray, sr: int, near: list[np.ndarray], sound: dict | None = None) -> np.ndarray:
    """Scale an original recording to the loudness of the synthesized speech around it (within ×0.5–×2).
    A sound (the clip record of a sound tag) keeps the level it had next to the person's own speech, so a breath
    stays as quiet as a breath; an uploaded sound with no speech to compare is only ever turned down."""
    near = [x for x in near if len(x)]
    if not near:
        return clip
    target = float(np.mean([_active_rms(x, sr) for x in near]))
    if sound is None:
        gain = float(np.clip(target / max(_active_rms(clip, sr), 1e-6), 0.5, 2.0))
    elif sound.get("speech_rms"):
        gain = float(np.clip(target / sound["speech_rms"], 0.25, 4.0))
    else:
        gain = min(1.0, target / max(_active_rms(clip, sr), 1e-6))
    return clip * gain


def fade(y: np.ndarray, sr: int, ms: float = 10) -> np.ndarray:
    n = min(len(y) // 2, int(sr * ms / 1000))
    if n <= 0:
        return y
    y = y.copy()
    ramp = np.linspace(0, 1, n, dtype=np.float32)
    y[:n] *= ramp
    y[-n:] *= ramp[::-1]
    return y


# --- how a trained model says each phrase on its own ---------------------------------------------------------------

@jobs.handler("check_phrases", queue="gpu")
def check_phrases(ctx: jobs.JobContext) -> dict:
    """Say every phrase with the model alone (no original recording spliced in) and compare with the originals:
    recognised text, speaker similarity and length (dur_ratio 0.7 = the model says it 30 % quicker than the person,
    a habit it has not learned)."""
    from . import tts
    model_id = ctx.params["model_id"]
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    phs = [p for p in list_for_voice(m["voice_id"]) if not is_sound(p)]
    emb = None
    try:
        from .pipeline import speaker
        emb = speaker.Embedder()
    except Exception as e:  # no speaker model on this machine: text and speed are still checked
        ctx.log(f"speaker model unavailable: {e}")
    done = 0
    for i, ph in enumerate(phs):
        ctx.check()
        ctx.progress(i / max(1, len(phs)), f"念「{ph['text']}」")
        res = tts.generate(model_id, ph["text"], language=ph["lang"], takes=1, phrases=False,
                           batch=f"phrasecheck_{model_id}")
        out = res["outputs"][0]
        y, sr = audio.load(Path(out["path"]), audio.MASTER_SR)
        y = trim(y, sr)
        r = {"output_id": out["id"], "match": out["score"].get("match"), "sim": None, "dur_ratio": None,
             "at": db.now(), "checkpoint": out["params"].get("checkpoint")}
        originals = []
        for c in ph["clips"]:
            try:
                originals.append(audio.load(clip_path(ph, c["id"]), audio.MASTER_SR)[0])
            except Exception:
                continue
        if originals:
            r["dur_ratio"] = round(len(y) / max(1.0, float(np.median([len(o) for o in originals]))), 3)
            if emb is not None:
                from .pipeline import speaker
                to16 = lambda x: audio.resample(x, audio.MASTER_SR, 16000)  # noqa: E731
                target = np.mean([emb.embed(to16(o)) for o in originals], axis=0)
                r["sim"] = round(speaker.cosine(emb.embed(to16(y)), target), 4)
        checks = dict(get(ph["id"])["checks"] or {})
        checks[model_id] = r
        db.update("catchphrases", ph["id"], {"checks": checks})
        done += 1
    return {"checked": done, "message": f"檢查了 {done} 個口頭禪"}

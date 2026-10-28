"""Text to speech: single lines, best-of-N takes, and whole scene scripts."""
from __future__ import annotations

import json
import re
import threading
from pathlib import Path

import numpy as np

from . import audio, config, datasets, db, emotions, engines, jobs, phrases, tags
from .pipeline import asr

_loaded: dict = {"key": None, "handle": None, "engine": None}
_load_lock = threading.Lock()

KANA = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")


def detect_language(text: str) -> str:
    """Good enough for ja/en scripts: any kana or kanji means Japanese."""
    return "ja" if KANA.search(text) else "en"


def _handle(model_id: str):
    """Keep one model in GPU memory at a time; switching models (or checkpoints) unloads the previous one."""
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    ck = (m["meta"] or {}).get("checkpoint")
    key = (model_id, ck)
    with _load_lock:
        if _loaded["key"] == key:
            return m, _loaded["engine"], _loaded["handle"]
        if _loaded["handle"] is not None:
            _loaded["engine"].unload(_loaded["handle"])
            _loaded.update(key=None, handle=None, engine=None)
        eng = engines.get(m["engine"])
        ok, why = eng.available()
        if not ok:
            raise RuntimeError(f"{eng.name}：{why}")
        h = eng.load(Path(m["path"]), ck)
        _loaded.update(key=key, handle=h, engine=eng)
        return m, eng, h


def unload() -> None:
    with jobs.GPU_LOCK, _load_lock:
        if _loaded["handle"] is not None:
            _loaded["engine"].unload(_loaded["handle"])
        _loaded.update(key=None, handle=None, engine=None)


def unload_if(model_id: str) -> None:
    if _loaded["key"] and _loaded["key"][0] == model_id:
        unload()


def loaded() -> dict | None:
    k = _loaded["key"]
    return {"model_id": k[0], "checkpoint": k[1]} if k else None


def reference(m: dict, ref_id: str | None, emotion: str | None = None) -> dict | None:
    """The chosen reference clip; with none chosen (or "auto"), the first one labelled with the wanted emotion
    (or the nearest one, see emotions.NEAR), else the first one. A reference carries much of the mood, so this is how a line gets the right delivery."""
    refs = (m["meta"] or {}).get("references") or []
    r = next((x for x in refs if x["id"] == ref_id), None) if ref_id and ref_id != "auto" else None
    for e in ([] if r else emotions.chain(emotion)):  # the mood, else the nearest one, else calm
        r = r or next((x for x in refs if x.get("emotion") == e), None)
    r = r or (refs[0] if refs else None)
    if not r:
        return None
    return {"id": r["id"], "path": Path(m["path"]) / r["file"], "text": r.get("text", ""), "lang": r.get("lang", ""),
            "emotion": r.get("emotion") or ""}


def apply_lexicon(text: str, lang: str | None) -> str:
    """Replace words with how they should be read (names, readings the engine gets wrong). Longest entries first,
    so 「推しの子」 wins over 「推し」. The original text is kept for display and for the ASR check."""
    entries = [e for e in (config.load_settings().get("lexicon") or [])
               if e.get("from") and e.get("to") and (not e.get("lang") or not lang or e["lang"] == lang)]
    for e in sorted(entries, key=lambda e: -len(e["from"])):
        text = text.replace(e["from"], e["to"])
    return text


def gpu_total_gb() -> float | None:
    try:
        import torch
        if torch.cuda.is_available():
            return torch.cuda.mem_get_info()[1] / 2 ** 30
    except Exception:
        pass
    return None


def screen_device(st: dict) -> str:
    pref = st.get("asr_screen_device") or "auto"
    if pref != "auto":
        return pref
    total = gpu_total_gb()
    return "cuda" if total and total >= 12 else "cpu"


def _screen(y: np.ndarray, sr: int, text: str, lang: str | None) -> dict:
    """Transcribe a take and compare it with the requested text (catches skipped, repeated or garbled words).
    On GPUs under 12 GB this runs on the CPU, so it never competes with the loaded TTS model for VRAM."""
    try:
        x16 = audio.resample(y, sr, 16000)
        st = config.load_settings()
        t = asr.transcribe(x16, st["asr_secondary"], language=lang, device=screen_device(st))
        return {"heard": t["text"], "match": round(asr.agreement(text, t["text"], lang or t["lang"]), 3)}
    except Exception as e:  # ASR not installed (e.g. test machines)
        return {"heard": "", "match": None, "note": str(e)[:120]}


def generate(model_id: str, text: str, language: str | None = None, style: str = "", takes: int = 1,
             seed: int | None = None, screen: bool = True, batch: str | None = None, mode: str | None = None,
             ref_id: str | None = None, extra: dict | None = None, emotion: str | None = None,
             phrases: bool = True) -> dict:
    """Generate `takes` versions, score them, keep all, and mark the best. The whole request (model load,
    synthesis and the ASR check) holds the GPU, so no other job loads a model under it.

    emotion: the mood wanted (else read from the style hint / [tags]); it picks the reference clip and the
    catchphrase recording. phrases: splice the voice's original catchphrase recordings into the line."""
    with jobs.GPU_LOCK:
        return _generate(model_id, text, language, style, takes, seed, screen, batch, mode, ref_id, extra,
                         emotion, phrases)


def compose(text: str, pool: list[dict], style: str = "", emotion: str | None = None,
            keep_tags: bool = False) -> list[dict]:
    """A line as the parts to render, in order. A [tag] applies to the text after it, up to the next tag: a way of
    speaking ([nervous], [whispers]) carries on to the rest of the line, a one-off ([sighs], [pause]) does not.
    - {"kind": "tts", "text", "style", "emotion", "tags"}: text synthesized with its own style and mood;
    - {"kind": "clip", "phrase", "said", "emotion"}: the person's recording of a catchphrase or a sound tag;
    - {"kind": "pause", "seconds"}: silence ([pause], [停頓 1.5秒], [間]).
    style / emotion: the line's own (chosen in the interface): added to every piece / beating the tags' mood.
    keep_tags: for an engine that reads [tags] itself. pool: the voice's catchphrases and sounds with recordings."""
    sounds = [p for p in pool if phrases.is_sound(p)]
    words = [p for p in pool if not phrases.is_sound(p)]
    line_emotion = emotions.valid(emotion)
    parts: list[dict] = []
    carried: list[str] = []
    for names, body in tags.chunks(text):
        steps: list[dict] = []
        events, own = [], []
        for n in names:
            sec = tags.pause_seconds(n)
            ph = phrases.sound_for(n, sounds) if sec is None else None
            if sec is not None:
                steps.append({"kind": "pause", "seconds": sec})
            elif ph:
                steps.append({"kind": "clip", "phrase": ph, "said": f"[{n}]"})
            elif tags.is_event(n):
                events.append(n)
            else:
                own.append(n)
        if own:
            carried = own
        active = events + carried
        st = ", ".join(dict.fromkeys(x for x in [*map(tags.style_of, active), style] if x))
        emo = line_emotion or tags.emotion_of(active) or emotions.from_style(st)
        for x in steps:
            if x["kind"] == "clip":
                x["emotion"] = emo
        parts += steps
        if not body.strip(phrases.PUNCT):
            # tags at the end of the line: a sound without a recording colours the text before it
            prev = next((x for x in reversed(parts) if x["kind"] == "tts"), None)
            if prev is not None and events:
                prev["style"] = ", ".join(dict.fromkeys(
                    x for x in [*prev["style"].split(", "), *map(tags.style_of, events)] if x))
                prev["tags"] = prev["tags"] + events
            continue
        for x in phrases.plan(body, words) or [{"kind": "tts", "text": body}]:
            if x["kind"] == "tts":
                t = x["text"].strip()
                x = {"kind": "tts", "text": f"[{', '.join(active)}] {t}" if keep_tags and active else t,
                     "style": st, "emotion": emo, "tags": active}
            else:
                x["emotion"] = emo
            parts.append(x)
    return parts


def _generate(model_id, text, language, style, takes, seed, screen, batch, mode, ref_id, extra, emotion,
              use_phrases) -> dict:
    m0 = db.get("models", model_id)
    if not m0:
        raise KeyError(model_id)
    voice = db.get("voices", m0["voice_id"])
    if m0["engine"] != "mock" and (not voice or not datasets.consent_ok(voice)):
        raise datasets.ConsentMissing("這個聲音目前沒有有效的同意紀錄（可能已撤回），不能合成。")
    m, eng, h = _handle(model_id)
    meta = eng.model_meta(Path(m["path"]))
    modes = eng.modes(meta)
    mode = mode if mode in modes else modes[0]
    pool = phrases.with_clips(m["voice_id"]) if use_phrases else []
    parts = compose(text, pool, style, emotion, keep_tags=eng.supports_tags)
    if not any(p["kind"] in ("tts", "clip") for p in parts):
        raise ValueError("沒有要念的文字（只有標籤的話，那個聲音要先在聲音頁放進原音）")
    spoken = tags.strip(text)
    first = next(p for p in parts if p["kind"] in ("tts", "clip"))
    emotion = first.get("emotion")  # the line's mood as recorded with the output: that of its first piece
    lang = language if language and language != "auto" else detect_language(spoken)
    refs: dict = {}

    def ref_for(e):  # a reference for each mood in the line (the chosen one when the person picked one)
        if mode not in ("ref", "hifi"):
            return None
        if e not in refs:
            refs[e] = reference(m, ref_id, e)
        return refs[e]
    if mode in ("ref", "hifi") and ref_for(emotion) is None:
        raise ValueError("這個模式需要參考片段，請先在模型頁加入參考片段")
    timbre = reference(m, ref_id, emotion)  # the model's own reference (if any) keeps timbre in continuations
    styles = ", ".join(dict.fromkeys(p["style"] for p in parts if p["kind"] == "tts" and p["style"]))
    first_tts = next((p for p in parts if p["kind"] == "tts"), None)
    ref = ref_for(first_tts["emotion"]) if first_tts else None
    single = len(parts) == 1 and parts[0]["kind"] == "tts"
    outs = []
    base_seed = seed if seed is not None else int(np.random.default_rng().integers(0, 2 ** 31 - 1))
    for k in range(max(1, min(8, takes))):
        s = base_seed + k
        if single:
            syn = eng.synthesize(h, apply_lexicon(first_tts["text"], lang), language=lang, style=first_tts["style"],
                                 mode=mode, reference=ref, seed=s, **(extra or {}))
            y, sr, info, used = syn.audio, syn.sr, syn.info, []
        else:
            y, sr, info, used = _spliced(eng, h, parts, lang, mode, ref_for, timbre, s, extra, k, modes)
        oid = db.new_id("out")
        path = audio.save(config.DATA / "outputs" / f"{oid}.wav", y, sr,
                          synthetic={"engine": eng.id, "model": model_id, "voice": m["voice_id"],
                                     **({"original_clips": len(used)} if used else {})})
        dur = len(y) / sr
        sc = _screen(y, sr, spoken, lang) if screen and spoken.strip(phrases.PUNCT) else {}
        outs.append(db.insert("outputs", {"id": oid, "model_id": model_id, "text": text,
                                          "params": {"language": lang, "style": styles, "seed": s,
                                                     "engine": eng.id, "mode": mode,
                                                     "ref": ref["id"] if ref else None, "emotion": emotion,
                                                     "phrases": used, "pieces": len(parts),
                                                     "checkpoint": info.get("checkpoint"), **(extra or {})},
                                          "path": str(path), "duration": round(dur, 3), "score": sc,
                                          "batch": batch, "created_at": db.now()}))
    if len(outs) > 1:
        durs = np.array([o["duration"] for o in outs])
        med = float(np.median(durs))
        for o in outs:
            match = o["score"].get("match")
            ratio = o["duration"] / med if med else 1
            o["score"]["rank_value"] = (match if match is not None else 0.5) - abs(1 - ratio) * 0.5
        best = max(outs, key=lambda o: o["score"]["rank_value"])
        for o in outs:
            o["score"]["best"] = o["id"] == best["id"]
            db.update("outputs", o["id"], {"score": o["score"]})
    elif outs:
        outs[0]["score"]["best"] = True
        db.update("outputs", outs[0]["id"], {"score": outs[0]["score"]})
    return {"outputs": outs, "mode": mode, "language": lang, "emotion": emotion}


def _spliced(eng, h, parts, lang, mode, ref_for, timbre, seed, extra, k, modes):
    """One take of a line made of several parts (compose): text pieces each with their own style and reference,
    the person's recordings, pauses. Text right after a catchphrase recording is spoken as a continuation of it
    when the engine can ("完整複製" with the recording as the prompt), so the flow carries on from the real voice.
    A sound ([喘氣] …) is played as recorded, at the level it had next to the person's speech. Recordings are
    matched in loudness and joined with pauses taken from the punctuation; a [pause] sets the silence itself."""
    pieces: list[list] = []
    used: list[dict] = []
    sr, info, prev = None, {}, None
    for p in parts:
        if p["kind"] == "pause":
            pieces.append(["pause", p["seconds"], p, None])
            prev = None
            continue
        if p["kind"] == "clip":
            c = phrases.pick_clip(p["phrase"], p.get("emotion"), k)
            path = phrases.clip_path(p["phrase"], c["id"])
            sound = phrases.is_sound(p["phrase"])
            prev = None if sound else {"path": path, "text": p["said"],
                                       "timbre_path": timbre["path"] if timbre else None}
            pieces.append(["clip", path, p, c if sound else None])
            used.append({"phrase": p["phrase"]["text"], "clip": c["id"], "emotion": c.get("emotion") or "",
                         **({"sound": True} if sound else {})})
            continue
        t = apply_lexicon(p["text"].strip(), lang)
        if prev is not None and "hifi" in modes:
            syn = eng.synthesize(h, t, language=lang, style="", mode="hifi", reference=prev, seed=seed,
                                 **(extra or {}))
        else:
            syn = eng.synthesize(h, t, language=lang, style=p.get("style", ""), mode=mode,
                                 reference=ref_for(p.get("emotion")), seed=seed, **(extra or {}))
        sr = sr or syn.sr
        info = syn.info or info
        y = audio.resample(syn.audio, syn.sr, sr) if syn.sr != sr else np.asarray(syn.audio, dtype=np.float32)
        pieces.append(["tts", phrases.trim(y, sr, pad=0.06), p, None])
        prev = None
    sr = sr or audio.MASTER_SR
    spoken = [x[1] for x in pieces if x[0] == "tts"]
    joined: list[list] = []  # [audio, silence after, the silence was set by a pause]
    for i, (kind, a, p, sound) in enumerate(pieces):
        if kind == "pause":
            if joined:
                joined[-1][1] = joined[-1][1] + a if joined[-1][2] else a
                joined[-1][2] = True
            else:
                joined.append([np.zeros(0, dtype=np.float32), a, True])
            continue
        if kind == "clip":
            y, _ = audio.load(a, sr)
            near = [pieces[j][1] for j in (i - 1, i + 1) if 0 <= j < len(pieces) and pieces[j][0] == "tts"]
            a = phrases.fade(phrases.match_level(y, sr, near or spoken, sound), sr)
        joined.append([a, phrases.gap_after(p) if i < len(pieces) - 1 else 0.0, False])
    return audio.concat([(x[0], x[1]) for x in joined], sr), sr, \
        {"checkpoint": h.get("checkpoint") if isinstance(h, dict) else None, **info}, used


# --- scene scripts -------------------------------------------------------------------------------------------------

LINE = re.compile(r"^(?P<speaker>[^:]{1,80}?)\s*::\s*(?P<text>.*)$")
RESERVED = {"STAGE", "SFX", "PAUSE", "ROMAJI", "GLOSS", "NOTE"}


def parse_script(text: str) -> list[dict]:
    """The novel-lab scene format: `Name :: [tags] line`, with STAGE/SFX/PAUSE/ROMAJI/GLOSS metadata lines.
    Returns turns and pauses in order; narration and metadata are kept for the listening sheet but not spoken."""
    events = []
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("@@"):
            continue
        m = LINE.match(line)
        if not m:
            continue
        who, body = m.group("speaker").strip(), m.group("text").strip()
        if who in RESERVED:
            if who == "PAUSE":
                try:
                    events.append({"kind": "pause", "seconds": float(body), "line": n})
                except ValueError:
                    pass
            elif who in ("ROMAJI", "GLOSS") and events and events[-1]["kind"] == "turn":
                events[-1][who.lower()] = body
            else:
                events.append({"kind": who.lower(), "text": body, "line": n})
            continue
        events.append({"kind": "turn", "speaker": who, "text": body, "line": n})
    return events


@jobs.handler("render_script", queue="gpu")
def render_script(ctx: jobs.JobContext) -> dict:
    """Render a whole scene: every turn with its cast model, joined with natural gaps and PAUSE lines."""
    p = ctx.params
    events = parse_script(p["script"])
    cast: dict = p["cast"]  # speaker name → {model_id, language, style}
    batch = db.new_id("scene")
    turns = [e for e in events if e["kind"] == "turn" and e["speaker"].lower() != "narrator"]
    missing = sorted({t["speaker"] for t in turns if t["speaker"] not in cast})
    if missing:
        raise ValueError("這些角色還沒有指定聲音：" + "、".join(missing))
    parts, sheet, sr_out = [], [], 48000
    for i, e in enumerate(events):
        ctx.progress(i / max(1, len(events)), f"第 {i + 1}/{len(events)} 行")
        if e["kind"] == "pause" and parts:
            parts[-1] = (parts[-1][0], parts[-1][1] + e["seconds"])
            continue
        if e["kind"] != "turn" or e["speaker"].lower() == "narrator":
            continue
        c = cast[e["speaker"]]
        res = generate(c["model_id"], e["text"], language=c.get("language"), style=c.get("style", ""),
                       takes=int(p.get("takes", 2)), batch=batch, mode=c.get("mode"), ref_id=c.get("ref_id"),
                       phrases=bool(p.get("phrases", True)))
        best = next((o for o in res["outputs"] if o["score"].get("best")), res["outputs"][0])
        y, sr = audio.load(Path(best["path"]), sr_out)
        parts.append((y, float(p.get("gap", 0.35))))
        sheet.append({"line": e["line"], "speaker": e["speaker"], "text": e["text"], "romaji": e.get("romaji"),
                      "output": best["id"], "match": best["score"].get("match"), "emotion": res.get("emotion"),
                      "original_clips": len(best["params"].get("phrases") or [])})
    mix = audio.concat(parts, sr_out)
    path = audio.save(config.DATA / "outputs" / f"{batch}.wav", mix, sr_out, synthetic={"scene": batch})
    (config.DATA / "outputs" / f"{batch}.json").write_text(json.dumps(sheet, ensure_ascii=False, indent=2),
                                                           encoding="utf-8")
    db.insert("outputs", {"id": batch, "model_id": None, "text": p["script"][:2000], "params": {"scene": True},
                          "path": str(path), "duration": round(len(mix) / sr_out, 2), "score": {"lines": len(sheet)},
                          "batch": batch, "created_at": db.now()})
    return {"output_id": batch, "lines": len(sheet), "message": f"場景完成：{len(sheet)} 句"}

"""Text to speech: single lines, best-of-N takes, and whole scene scripts."""
from __future__ import annotations

import json
import re
import threading
from pathlib import Path

import numpy as np

from . import audio, config, db, engines, jobs
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
    with _load_lock:
        if _loaded["handle"] is not None:
            _loaded["engine"].unload(_loaded["handle"])
        _loaded.update(key=None, handle=None, engine=None)


def unload_if(model_id: str) -> None:
    if _loaded["key"] and _loaded["key"][0] == model_id:
        unload()


def loaded() -> dict | None:
    k = _loaded["key"]
    return {"model_id": k[0], "checkpoint": k[1]} if k else None


def reference(m: dict, ref_id: str | None) -> dict | None:
    refs = (m["meta"] or {}).get("references") or []
    r = next((x for x in refs if x["id"] == ref_id), refs[0] if refs else None)
    if not r:
        return None
    return {"id": r["id"], "path": Path(m["path"]) / r["file"], "text": r.get("text", ""), "lang": r.get("lang", "")}


def _screen(y: np.ndarray, sr: int, text: str, lang: str | None) -> dict:
    """Transcribe a take and compare it with the requested text (catches skipped, repeated or garbled words)."""
    try:
        x16 = audio.resample(y, sr, 16000)
        st = config.load_settings()
        t = asr.transcribe(x16, st["asr_secondary"], language=lang, device=st["asr_device"])
        return {"heard": t["text"], "match": round(asr.agreement(text, t["text"], lang or t["lang"]), 3)}
    except Exception as e:  # ASR not installed (e.g. test machines)
        return {"heard": "", "match": None, "note": str(e)[:120]}


def generate(model_id: str, text: str, language: str | None = None, style: str = "", takes: int = 1,
             seed: int | None = None, screen: bool = True, batch: str | None = None, mode: str | None = None,
             ref_id: str | None = None, extra: dict | None = None) -> dict:
    """Generate `takes` versions, score them, keep all, and mark the best."""
    m, eng, h = _handle(model_id)
    meta = eng.model_meta(Path(m["path"]))
    modes = eng.modes(meta)
    mode = mode if mode in modes else modes[0]
    text_engine, tag_style = eng.render_tags(text)
    if eng.supports_tags:
        text_engine = text
    full_style = ", ".join(s for s in (tag_style, style) if s)
    lang = language if language and language != "auto" else detect_language(text_engine)
    ref = reference(m, ref_id) if mode in ("ref", "hifi") else None
    if mode in ("ref", "hifi") and ref is None:
        raise ValueError("這個模式需要參考片段，請先在模型頁加入參考片段")
    outs = []
    base_seed = seed if seed is not None else int(np.random.default_rng().integers(0, 2 ** 31 - 1))
    for k in range(max(1, min(8, takes))):
        s = base_seed + k
        with jobs.GPU_LOCK:
            syn = eng.synthesize(h, text_engine, language=lang, style=full_style, mode=mode, reference=ref, seed=s,
                                 **(extra or {}))
        oid = db.new_id("out")
        path = audio.save(config.DATA / "outputs" / f"{oid}.wav", syn.audio, syn.sr,
                          synthetic={"engine": eng.id, "model": model_id, "voice": m["voice_id"]})
        dur = len(syn.audio) / syn.sr
        sc = _screen(syn.audio, syn.sr, text_engine, lang) if screen else {}
        outs.append(db.insert("outputs", {"id": oid, "model_id": model_id, "text": text,
                                          "params": {"language": lang, "style": full_style, "seed": s,
                                                     "engine": eng.id, "mode": mode,
                                                     "ref": ref["id"] if ref else None,
                                                     "checkpoint": syn.info.get("checkpoint"), **(extra or {})},
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
    return {"outputs": outs, "mode": mode, "language": lang}


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
                       takes=int(p.get("takes", 2)), batch=batch, mode=c.get("mode"), ref_id=c.get("ref_id"))
        best = next((o for o in res["outputs"] if o["score"].get("best")), res["outputs"][0])
        y, sr = audio.load(Path(best["path"]), sr_out)
        parts.append((y, float(p.get("gap", 0.35))))
        sheet.append({"line": e["line"], "speaker": e["speaker"], "text": e["text"], "romaji": e.get("romaji"),
                      "output": best["id"], "match": best["score"].get("match")})
    mix = audio.concat(parts, sr_out)
    path = audio.save(config.DATA / "outputs" / f"{batch}.wav", mix, sr_out, synthetic={"scene": batch})
    (config.DATA / "outputs" / f"{batch}.json").write_text(json.dumps(sheet, ensure_ascii=False, indent=2),
                                                           encoding="utf-8")
    db.insert("outputs", {"id": batch, "model_id": None, "text": p["script"][:2000], "params": {"scene": True},
                          "path": str(path), "duration": round(len(mix) / sr_out, 2), "score": {"lines": len(sheet)},
                          "batch": batch, "created_at": db.now()})
    return {"output_id": batch, "lines": len(sheet), "message": f"場景完成：{len(sheet)} 句"}

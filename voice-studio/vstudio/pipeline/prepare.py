"""The import job: one long recording in, scored training segments out."""
from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np

from .. import audio, config, db, jobs
from . import asr, speaker, vad


def voice_centroids(voice_ids: list[str] | None = None) -> dict[str, np.ndarray]:
    """One embedding per voice: the mean of its enrollment clips (stored with the voice)."""
    out = {}
    q = "SELECT * FROM voices" + (" WHERE id IN (%s)" % ",".join("?" * len(voice_ids)) if voice_ids else "")
    for v in db.query(q, tuple(voice_ids or ())):
        embs = [np.array(e["emb"], dtype=np.float32) for e in v["enrollment"] if e.get("emb")]
        if embs:
            c = np.mean(embs, axis=0)
            out[v["id"]] = c / (np.linalg.norm(c) + 1e-9)
    return out


def score(seg: dict) -> tuple[float, list[str]]:
    """0–1 quality score and the reasons a segment needs a look."""
    flags, s = [], 1.0
    if seg["asr_agree"] is not None:
        if seg["asr_agree"] < 0.75:
            flags.append("asr_disagree")
        s *= 0.4 + 0.6 * seg["asr_agree"]
    if seg["snr"] is not None and seg["snr"] < 15:
        flags.append("noisy")
        s *= 0.7
    if seg["clip"] and seg["clip"] > 0.001:
        flags.append("clipping")
        s *= 0.6
    if seg["voice_id"] is None:
        flags.append("unknown_speaker")
        s *= 0.5
    if seg.get("ambiguous"):
        flags.append("overlap")
        s *= 0.5
    if not seg["text"]:
        flags.append("no_text")
        s *= 0.2
    return round(s, 3), flags


@jobs.handler("prepare_source", queue="gpu")
def prepare_source(ctx: jobs.JobContext) -> dict:
    p = ctx.params
    src = db.get("sources", p["source_id"])
    st = config.load_settings()
    from .. import tts  # free the GPU for separation and speech recognition (a TTS model can hold ~8 GB)
    tts.unload()
    work = config.DATA / "sources" / src["id"]
    master = work / "master.wav"
    ctx.progress(0.02, "解碼音訊")
    audio.extract(Path(src["path"]), master, sr=audio.MASTER_SR)
    if p.get("separate", st["separate_vocals"]):
        ctx.progress(0.05, "分離人聲（去背景音樂）")
        from . import separate
        with jobs.GPU_LOCK:
            voc = separate.vocals(master, work / "separated")
        x48, _ = audio.load(voc, audio.MASTER_SR)
        audio.save(master, x48, audio.MASTER_SR)
    x48, _ = audio.load(master)
    x16 = audio.resample(x48, audio.MASTER_SR, 16000)
    duration = len(x48) / audio.MASTER_SR
    db.update("sources", src["id"], {"duration": duration, "status": "processing"})

    ctx.progress(0.10, "偵測說話段落")
    v = vad.SileroVAD()
    probs = v.probs(x16)
    regions = vad.speech_regions(probs)
    plan = vad.plan_segments(regions, probs, st["segment_min_s"], st["segment_max_s"], st["segment_target_s"])
    ctx.log(f"{len(regions)} speech regions → {len(plan)} segments over {duration / 60:.1f} min")

    # remove old segments of this source (re-import)
    for old in db.query("SELECT path FROM segments WHERE source_id=?", (src["id"],)):
        Path(old["path"]).unlink(missing_ok=True)
    with db.tx() as c:
        c.execute("DELETE FROM segments WHERE source_id=?", (src["id"],))

    emb_model = speaker.Embedder()
    hint = src.get("voice_hint")
    centroids = voice_centroids()
    threshold = float(st["speaker_match_threshold"])
    seg_dir = config.DATA / "segments" / src["id"]
    seg_dir.mkdir(parents=True, exist_ok=True)
    records, embs = [], []
    for i, r in enumerate(plan):
        ctx.progress(0.12 + 0.28 * i / max(1, len(plan)), f"切音與辨識說話者 {i + 1}/{len(plan)}")
        a, b = int(r.start * audio.MASTER_SR), int(r.end * audio.MASTER_SR)
        clip = x48[a:b]
        sid = db.new_id("seg")
        path = audio.save(seg_dir / f"{sid}.wav", clip, audio.MASTER_SR)
        s = audio.stats(clip, audio.MASTER_SR)
        e = emb_model.embed(x16[int(r.start * 16000):int(r.end * 16000)])
        embs.append(e)
        vid, sim, amb = speaker.assign(e, centroids, threshold)
        if hint and hint in centroids:
            sim = speaker.cosine(e, centroids[hint])
            vid = hint if sim >= threshold * 0.85 else None
        elif hint and not centroids:
            vid, sim = hint, None
        records.append({"id": sid, "source_id": src["id"], "voice_id": vid, "start": r.start, "end": r.end,
                        "path": str(path), "duration": r.dur, "snr": s["snr"], "clip": s["clip"],
                        "spk_sim": sim, "ambiguous": amb, "emotion": src.get("emotion")})

    if records and not centroids and not hint:
        labels = speaker.cluster(np.array(embs))
        for rec, lab in zip(records, labels):
            rec["cluster"] = int(lab)

    langs = p.get("language") or src.get("language") or None
    st_primary, st_secondary = st["asr_primary"], st["asr_secondary"]
    use_second = p.get("two_model_check", True)
    from .. import phrases
    phrase_hint: dict = {}  # voice → its catchphrases in the canonical spelling, as a hint to speech recognition
    for i, rec in enumerate(records):
        ctx.progress(0.40 + 0.58 * i / max(1, len(records)), f"轉文字 {i + 1}/{len(records)}")
        a, b = int(rec["start"] * 16000), int(rec["end"] * 16000)
        # both models get the same prompt (verbatim fillers + this voice's catchphrases), so a kept filler or a
        # catchphrase is not counted as a disagreement; only when the language is known
        if rec["voice_id"] not in phrase_hint:
            phrase_hint[rec["voice_id"]] = phrases.asr_prompt(rec["voice_id"], langs)
        prompt = ((asr.VERBATIM_PROMPT.get(langs or "", "") if st.get("asr_verbatim", True) else "")
                  + phrase_hint[rec["voice_id"]]) if langs else ""
        prompt = prompt or None
        with jobs.GPU_LOCK:
            t1 = asr.transcribe(x16[a:b], st_primary, language=langs, device=st["asr_device"], prompt=prompt)
            t2 = asr.transcribe(x16[a:b], st_secondary, language=t1["lang"], device=st["asr_device"], prompt=prompt) \
                if use_second else None
        rec["text"] = t1["text"]
        rec["lang"] = t1["lang"]
        rec["text_alt"] = t2["text"] if t2 else ""
        rec["asr_agree"] = asr.agreement(t1["text"], t2["text"], t1["lang"]) if t2 else None
        rec["asr_logprob"], rec["no_speech"] = t1.get("avg_logprob"), t1.get("no_speech")
        rec["score"], flags = score(rec)
        rec["flags"] = flags
        amb = rec.pop("ambiguous")
        rec["status"] = "pending"
        db.insert("segments", rec)
        rec["ambiguous"] = amb

    db.update("sources", src["id"], {"status": "ready"})
    if p.get("keep_master") is False:
        master.unlink(missing_ok=True)
    total = sum(r["duration"] for r in records)
    if not db.query("SELECT id FROM jobs WHERE kind='prepare_source' AND status='queued' LIMIT 1"):
        asr.unload()  # last recording in the queue: give the GPU back for text to speech
    return {"segments": len(records), "speech_minutes": round(total / 60, 1),
            "message": f"完成：{len(records)} 段，共 {total / 60:.1f} 分鐘語音"}


@jobs.handler("enroll_voice", queue="gpu")
def enroll_voice(ctx: jobs.JobContext) -> dict:
    """Compute embeddings for a voice's reference clips (and re-match unassigned segments)."""
    v = db.get("voices", ctx.params["voice_id"])
    emb_model = speaker.Embedder()
    out = []
    for e in v["enrollment"]:
        x, _ = audio.load(Path(e["path"]), 16000)
        out.append({**e, "emb": emb_model.embed(x).round(5).tolist()})
    db.update("voices", v["id"], {"enrollment": out})
    return {"message": f"已建立 {len(out)} 段參考聲紋"}


def remove_source(source_id: str) -> None:
    for s in db.query("SELECT path FROM segments WHERE source_id=?", (source_id,)):
        Path(s["path"]).unlink(missing_ok=True)
    with db.tx() as c:
        c.execute("DELETE FROM segments WHERE source_id=?", (source_id,))
        c.execute("DELETE FROM sources WHERE id=?", (source_id,))
    shutil.rmtree(config.DATA / "sources" / source_id, ignore_errors=True)
    shutil.rmtree(config.DATA / "segments" / source_id, ignore_errors=True)

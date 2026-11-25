#!/usr/bin/env python3
"""Long-form text to speech on a rented GPU. Runs as train_entry.py inside the engine environment, started by
bootstrap.sh exactly like a training run.

Before the pod is rented the studio has put on the network volume:
- the model checkpoint, once, under vs/models/<model id>/<checkpoint>/ (kept for later runs);
- this run's bundle (dataset.tar → data/chunks.jsonl: i, text, style, seed; data/refs/: the reference clip for the
  "ref" and "hifi" modes) and config.json (params: engine, checkpoint kind and path, mode, settings).

Every chunk becomes audio/<i:05d>.wav, written as .tmp and renamed, so a file with its final name is whole; chunks
already there are skipped, so a stopped run continues where it was. A chunk that fails twice is written as a short
silence and listed in result.json (one bad sentence must not stop the other two thousand). progress.json says how
far it is; result.json, written last, tells bootstrap.sh the run is done.
"""
from __future__ import annotations

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import Job, log  # noqa: E402

SILENCE_S = 0.3


def load(p: dict):
    if p.get("engine") == "mock":
        return None
    from voxcpm import VoxCPM
    kw = {"load_denoiser": False, "optimize": False}
    if p.get("kind") == "lora":  # the adapter sits on exactly the base weights it was trained on
        from huggingface_hub import snapshot_download
        base = snapshot_download(p["base"], revision=p.get("base_revision") or None)
        return VoxCPM.from_pretrained(base, lora_weights_path=p["model_dir"], **kw)
    if p.get("model_dir"):
        return VoxCPM.from_pretrained(p["model_dir"], **kw)
    return VoxCPM.from_pretrained(p["base"], **kw)


def synth(model, p: dict, c: dict, ref: dict | None):
    import numpy as np
    if model is None:  # the test engine: a hum as long as the text would take to say
        time.sleep(0.01)
        sr = 24000
        t = np.arange(int(sr * min(20.0, 0.06 * len(c["text"]) + 0.3))) / sr
        return (0.2 * np.sin(2 * np.pi * 180 * t)).astype(np.float32), sr
    args = {"cfg_value": float(p.get("cfg", 2.0)), "inference_timesteps": int(p.get("timesteps", 10)),
            "seed": c.get("seed")}
    mode = p.get("tts_mode") or "plain"
    if mode == "hifi" and ref and ref.get("text"):
        args.update(text=c["text"], prompt_wav_path=ref["path"], prompt_text=ref["text"], reference_wav_path=ref["path"])
    else:
        args["text"] = f"({c['style']}){c['text']}" if c.get("style") else c["text"]
        if mode in ("ref", "hifi") and ref:
            args["reference_wav_path"] = ref["path"]
    wav = model.generate(**args)
    return wav, model.tts_model.sample_rate


def put(job: Job, name: str, obj) -> None:
    tmp = job.dir / f"{name}.tmp"
    tmp.write_text(json.dumps(obj), encoding="utf-8")
    os.replace(tmp, job.dir / name)


def main() -> None:
    import numpy as np
    import soundfile as sf
    job = Job()
    p = job.params
    chunks = job.read_jsonl("chunks.jsonl")
    out = job.dir / "audio"
    out.mkdir(exist_ok=True)
    ref = None
    if p.get("reference"):
        ref = {"path": str(job.data / p["reference"]["audio"]), "text": p["reference"].get("text") or ""}

    def final(c: dict):
        return out / f"{int(c['i']):05d}.wav"
    todo = [c for c in chunks if not final(c).exists()]
    total, done = len(chunks), len(chunks) - len(todo)
    failed_f = job.dir / "failed.json"  # across continued runs: lines an earlier pod could not make either
    failed: list[int] = json.loads(failed_f.read_text(encoding="utf-8")) if failed_f.exists() else []
    log(f"{total} chunks, {done} already done; loading {p.get('engine')} ({p.get('kind') or 'base'})")
    job.progress(phase="load", done=done, total=total)
    model = load(p)
    t0, audio_s = time.time(), 0.0
    for c in todo:
        y, sr = None, 24000
        for attempt in (1, 2):
            try:
                y, sr = synth(model, p, c, ref)
                break
            except Exception as e:  # noqa: BLE001 (recorded; the run goes on)
                log(f"chunk {c['i']} try {attempt} failed: {type(e).__name__}: {e}")
        if y is None:
            failed.append(int(c["i"]))
            put(job, "failed.json", failed)
            y = np.zeros(int(sr * SILENCE_S), dtype=np.float32)
        tmp = out / f"{int(c['i']):05d}.wav.tmp"
        sf.write(str(tmp), np.asarray(y, dtype=np.float32), sr, format="WAV", subtype="PCM_16")
        os.replace(tmp, final(c))
        done += 1
        audio_s += len(y) / sr
        job.progress(phase="synth", done=done, total=total, audio_s=round(audio_s, 1),
                     synth_s=round(time.time() - t0, 2), failed=failed)
    put(job, "result.json", {"done": done, "total": total, "audio_s": round(audio_s, 2),
                             "synth_s": round(time.time() - t0, 2), "failed": failed})
    log(f"done: {done}/{total} chunks, {audio_s / 60:.1f} min of speech in {(time.time() - t0) / 60:.1f} min")


if __name__ == "__main__":
    main()

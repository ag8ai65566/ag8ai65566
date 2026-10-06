#!/usr/bin/env python3
"""Qwen3-TTS-12Hz-1.7B-Base single-speaker fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/qwen3).

Follows the official finetuning/ recipe of the pinned Qwen3-TTS commit:
prepare_data.py (extract 12 Hz audio codes) → sft_12hz.py (full SFT, one checkpoint per epoch).
model.tar is published right after training; then every epoch's checkpoint reads the held-out lines aloud
(samples.tar), next to the untrained base model cloning from the reference clip, for comparison.

Notes from the pinned code:
- dataset.py loads ref_audio at its native rate and asserts 24 kHz, so the reference is resampled first;
- dataset.py reads `language` but does not use it (the prompt prefix is the auto-language one), so checkpoints
  are sampled with language="Auto" to match how they were trained.
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import LANG_NAMES, Job, log, need_disk, resolved_revision, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/qwen3"))
BASE = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
TOKENIZER = "Qwen/Qwen3-TTS-Tokenizer-12Hz"
SPEAKER = "vs_speaker"
SEED = 1234


def flash_attention_works() -> bool:
    """find_spec() is not enough: the CUDA extension must actually load."""
    if importlib.util.find_spec("flash_attn") is None:
        return False
    try:
        import flash_attn  # noqa: F401
        import flash_attn_2_cuda  # noqa: F401
        return True
    except Exception as e:  # ImportError, OSError (missing .so symbols), RuntimeError
        log(f"FlashAttention present but unusable ({e}); using SDPA")
        return False


def main() -> None:
    job = Job()
    p = job.params
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE, revision=p.get("base_revision") or None)
    tok_path = snapshot_download(TOKENIZER, revision=p.get("tokenizer_revision") or None)
    attn = "flash_attention_2" if flash_attention_works() else "sdpa"
    log(f"base {BASE}@{resolved_revision(base_path)} tokenizer @{resolved_revision(tok_path)} attention {attn}")
    keep_n = int(p.get("keep", 2))
    need_disk(20 + 5 * (int(p.get("epochs", 3)) + keep_n))

    plan = sample_plan(job)
    ref = plan.get("reference") or {}
    if not ref.get("audio"):
        raise RuntimeError("dataset has no reference clip")
    import librosa
    import soundfile as sf
    y, _ = librosa.load(str(job.data / ref["audio"]), sr=24000, mono=True)
    if len(y) < 24000:
        raise RuntimeError("reference clip is shorter than one second")
    ref24 = job.work / "reference_24k.wav"
    sf.write(str(ref24), y, 24000, subtype="PCM_16")

    raw = job.work / "train_raw.jsonl"
    items = job.read_jsonl("train.jsonl")
    with raw.open("w", encoding="utf-8") as f:
        for it in items:  # the recipe recommends one fixed ref_audio for every line
            f.write(json.dumps({"audio": str(job.data / it["audio"]), "text": it["text"], "ref_audio": str(ref24),
                                "language": LANG_NAMES.get(it.get("lang") or "", "Auto")}, ensure_ascii=False) + "\n")

    job.progress(phase="prepare")
    codes = job.work / "train_with_codes.jsonl"
    ft = SRC / "finetuning"
    job.run([sys.executable, ft / "prepare_data.py", "--device", "cuda:0", "--tokenizer_model_path", tok_path,
             "--input_jsonl", raw, "--output_jsonl", codes], cwd=ft)

    # the official trainer hard-codes FlashAttention 2; fall back to PyTorch SDPA when it does not load
    script = (ft / "sft_12hz.py").read_text(encoding="utf-8")
    if attn != "flash_attention_2":
        script = script.replace('"flash_attention_2"', '"sdpa"')
    (ft / "sft_vs.py").write_text(script, encoding="utf-8")

    bs, epochs = int(p.get("batch_size", 2)), int(p.get("epochs", 3))
    per_epoch = math.ceil(len(items) / bs)
    total = per_epoch * epochs
    out = job.work / "out"
    job.progress(phase="train", step=0, total=total, per_epoch=per_epoch, mode="sft")
    pat = re.compile(r"Epoch (\d+) \| Step (\d+) \| Loss: ([\d.]+)")
    metrics_f = (job.out / "train_metrics.jsonl").open("w", encoding="utf-8")

    def on_line(line: str) -> None:
        m = pat.search(line)
        if m:
            e, s, loss = int(m.group(1)), int(m.group(2)), float(m.group(3))
            step = e * per_epoch + s + 1
            metrics_f.write(json.dumps({"split": "train", "step": step, "loss": loss, "epoch": e}) + "\n")
            metrics_f.flush()
            job.progress(phase="train", step=step, total=total, loss=round(loss, 4),
                         epoch=round(step / per_epoch, 2))

    job.run([sys.executable, "sft_vs.py", "--init_model_path", base_path, "--output_model_path", out,
             "--train_jsonl", codes, "--batch_size", bs, "--lr", float(p.get("lr", 2e-5)),
             "--num_epochs", epochs, "--speaker_name", SPEAKER], cwd=ft, on_line=on_line)
    metrics_f.close()

    ckpts = sorted((d for d in out.iterdir() if d.name.startswith("checkpoint-epoch-")),
                   key=lambda d: int(d.name.rsplit("-", 1)[1]))
    if not ckpts:
        raise RuntimeError("trainer produced no checkpoints")
    keep = ckpts[-keep_n:]
    ck_meta = [{"name": d.name, "step": (int(d.name.rsplit("-", 1)[1]) + 1) * per_epoch,
                "epoch": int(d.name.rsplit("-", 1)[1]) + 1, "weights": d in keep} for d in ckpts]
    meta = {"engine": "qwen3", "mode": "sft", "base": BASE, "base_revision": resolved_revision(base_path),
            "tokenizer_revision": resolved_revision(tok_path), "speaker": SPEAKER, "checkpoints": ck_meta,
            "samples": plan, "total_steps": total, "per_epoch": per_epoch, "attn": attn, "seed": SEED,
            "sft_language": "Auto", "sampling": "pending"}
    job.package(meta, "model.tar", [(job.out / "train_metrics.jsonl", "model/train_metrics.jsonl")]
                + [(d, f"model/checkpoints/{d.name}") for d in keep])

    try:
        sample_all(job, base_path, ckpts, plan, ref24, ref.get("text") or "", attn)
        meta.update(sampling="complete", sample_conditions={
            "plain": {"mode": "plain", "language": "Auto", "seed": SEED},
            "ref": {"mode": "hifi" if ref.get("text") else "ref", "reference": ref.get("id"), "seed": SEED,
                    "note": "base model only (zero-shot clone)"}})
    except Exception as e:
        log(f"sampling incomplete: {e}")
        meta.update(sampling="incomplete", sampling_error=str(e)[:300])
    if (job.out / "samples").exists():
        job.package(meta, "samples.tar", [(job.out / "samples", "model/samples")])


def sample_all(job: Job, base_path: str, ckpts: list[Path], plan: dict, ref24: Path, ref_text: str,
               attn: str) -> None:
    import soundfile as sf
    import torch
    from qwen_tts import Qwen3TTSModel

    job.progress(phase="samples", step=0, total=len(ckpts) + 1)
    lines = plan.get("lines", [])

    def write(name: str, fname: str, wavs, sr) -> None:
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        sf.write(str(d / fname), wavs[0], sr)

    # the untrained base can only clone from a reference, so its clips are filed as "ref", not "plain"
    base = Qwen3TTSModel.from_pretrained(base_path, device_map="cuda:0", dtype=torch.bfloat16,
                                         attn_implementation=attn)
    prompt = base.create_voice_clone_prompt(ref_audio=str(ref24), ref_text=ref_text or None,
                                            x_vector_only_mode=not ref_text)
    for i, line in enumerate(lines):
        try:
            torch.manual_seed(SEED)
            wavs, sr = base.generate_voice_clone(text=line["text"], language=LANG_NAMES.get(line.get("lang"), "Auto"),
                                                 voice_clone_prompt=prompt)
            write("base", f"{i}_ref.wav", wavs, sr)
        except Exception as e:
            log(f"base sample {i} failed: {e}")
    del base
    torch.cuda.empty_cache()
    for k, d in enumerate(ckpts):
        m = Qwen3TTSModel.from_pretrained(str(d), device_map="cuda:0", dtype=torch.bfloat16, attn_implementation=attn)
        for i, line in enumerate(lines):
            try:
                torch.manual_seed(SEED)
                wavs, sr = m.generate_custom_voice(text=line["text"], speaker=SPEAKER, language="Auto")
                write(d.name, f"{i}_plain.wav", wavs, sr)
            except Exception as e:
                log(f"sample {d.name}/{i} failed: {e}")
        del m
        torch.cuda.empty_cache()
        job.progress(phase="samples", step=k + 2, total=len(ckpts) + 1)


if __name__ == "__main__":
    main()

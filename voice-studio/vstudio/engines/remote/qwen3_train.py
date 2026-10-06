#!/usr/bin/env python3
"""Qwen3-TTS-12Hz-1.7B-Base single-speaker fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/qwen3).

Follows the official finetuning/ recipe of the pinned Qwen3-TTS commit:
prepare_data.py (extract 12 Hz audio codes) → sft_12hz.py (full SFT, one checkpoint per epoch).
Then every epoch's checkpoint, plus the untrained base model (zero-shot clone), reads the held-out lines aloud.
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import LANG_NAMES, Job, free_gb, log, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/qwen3"))
BASE = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
TOKENIZER = "Qwen/Qwen3-TTS-Tokenizer-12Hz"
SPEAKER = "vs_speaker"
SEED = 1234


def main() -> None:
    job = Job()
    p = job.params
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE)
    tok_path = snapshot_download(TOKENIZER)
    attn = "flash_attention_2" if importlib.util.find_spec("flash_attn") else "sdpa"
    log(f"attention: {attn}")

    plan = sample_plan(job)
    ref = plan.get("reference") or {}
    ref_abs = str(job.data / ref["audio"]) if ref.get("audio") else None
    if not ref_abs:
        raise RuntimeError("dataset has no reference clip")
    raw = job.work / "train_raw.jsonl"
    items = job.read_jsonl("train.jsonl")
    with raw.open("w", encoding="utf-8") as f:
        for it in items:  # the recipe recommends one fixed ref_audio for every line
            f.write(json.dumps({"audio": str(job.data / it["audio"]), "text": it["text"], "ref_audio": ref_abs,
                                "language": LANG_NAMES.get(it.get("lang") or "", "Auto")}, ensure_ascii=False) + "\n")

    job.progress(phase="prepare")
    codes = job.work / "train_with_codes.jsonl"
    ft = SRC / "finetuning"
    job.run([sys.executable, ft / "prepare_data.py", "--device", "cuda:0", "--tokenizer_model_path", tok_path,
             "--input_jsonl", raw, "--output_jsonl", codes], cwd=ft)

    # the official trainer hard-codes FlashAttention 2; fall back to PyTorch SDPA when it is not installed
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
    keep = ckpts[-int(p.get("keep", 2)):]

    import soundfile as sf
    import torch
    from qwen_tts import Qwen3TTSModel

    job.progress(phase="samples", step=0, total=len(ckpts) + 1)
    lines = plan.get("lines", [])

    def write(name: str, i: int, wavs, sr) -> None:
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        sf.write(str(d / f"{i}_plain.wav"), wavs[0], sr)

    base = Qwen3TTSModel.from_pretrained(base_path, device_map="cuda:0", dtype=torch.bfloat16,
                                         attn_implementation=attn)
    prompt = base.create_voice_clone_prompt(ref_audio=ref_abs, ref_text=ref.get("text") or "",
                                            x_vector_only_mode=not ref.get("text"))
    for i, line in enumerate(lines):
        try:
            torch.manual_seed(SEED)
            wavs, sr = base.generate_voice_clone(text=line["text"], language=LANG_NAMES.get(line.get("lang"), "Auto"),
                                                 voice_clone_prompt=prompt)
            write("base", i, wavs, sr)
        except Exception as e:
            log(f"base sample {i} failed: {e}")
    del base
    torch.cuda.empty_cache()
    for k, d in enumerate(ckpts):
        m = Qwen3TTSModel.from_pretrained(str(d), device_map="cuda:0", dtype=torch.bfloat16, attn_implementation=attn)
        for i, line in enumerate(lines):
            try:
                torch.manual_seed(SEED)
                wavs, sr = m.generate_custom_voice(text=line["text"], speaker=SPEAKER,
                                                   language=LANG_NAMES.get(line.get("lang"), "Auto"))
                write(d.name, i, wavs, sr)
            except Exception as e:
                log(f"sample {d.name}/{i} failed: {e}")
        del m
        torch.cuda.empty_cache()
        job.progress(phase="samples", step=k + 2, total=len(ckpts) + 1)

    ck_meta = []
    for d in ckpts:
        ep = int(d.name.rsplit("-", 1)[1])
        has = d in keep
        if has:
            shutil.copytree(d, job.out / "checkpoints" / d.name)
        ck_meta.append({"name": d.name, "step": (ep + 1) * per_epoch, "epoch": ep + 1, "weights": has})
    log(f"free disk before packaging: {free_gb():.0f} GB")
    job.package({"engine": "qwen3", "mode": "sft", "base": BASE, "speaker": SPEAKER, "checkpoints": ck_meta,
                 "samples": plan, "total_steps": total, "per_epoch": per_epoch, "attn": attn, "seed": SEED})


if __name__ == "__main__":
    main()

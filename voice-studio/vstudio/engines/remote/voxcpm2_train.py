#!/usr/bin/env python3
"""VoxCPM2 fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/voxcpm2).

1. writes a training config from the studio's preset (LoRA or full fine-tuning, official recipe values);
2. runs the official trainer (scripts/train_voxcpm_finetune.py from the pinned VoxCPM commit);
3. every saved checkpoint, plus the untrained base model, reads the same held-out lines aloud (with and without a
   reference clip), so you can compare checkpoints by ear and the studio can score them;
4. packs the chosen checkpoints and the samples into model.tar.
"""
from __future__ import annotations

import json
import math
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import Job, LogTail, free_gb, log, parse_metrics, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/voxcpm2"))
BASE = "openbmb/VoxCPM2"
SEED = 1234


def count_lines(p: Path) -> int:
    return sum(1 for x in p.read_text(encoding="utf-8").splitlines() if x.strip())


def main() -> None:
    job = Job()
    p = job.params
    mode = p.get("mode", "lora")
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE, revision=p.get("base_revision") or None)
    log(f"base model at {base_path}")

    train_manifest, val_manifest = job.data / "train.jsonl", job.data / "val.jsonl"
    n_train = count_lines(train_manifest)
    bs, accum = int(p.get("batch_size", 2)), int(p.get("grad_accum", 8))
    per_epoch = max(1, n_train // bs // accum)
    total = int(round(per_epoch * float(p.get("epochs", 2))))
    total = max(int(p.get("min_steps", 150)), min(total, int(p.get("max_steps_cap", 30000))))
    n_saves = int(p.get("saves", 6))
    save_every = max(25, math.ceil(total / n_saves))
    ckpt = job.work / "ckpt"
    conf = {
        "pretrained_path": base_path,
        "train_manifest": str(train_manifest),
        "val_manifest": str(val_manifest) if val_manifest.exists() and count_lines(val_manifest) else "",
        "sample_rate": 16000,
        "out_sample_rate": 48000,
        "batch_size": bs,
        "grad_accum_steps": accum,
        "num_workers": 4,
        "preprocessing_num_workers": 4,
        "num_iters": total,
        "max_steps": total,
        "log_interval": 5,
        "valid_interval": save_every,
        "save_interval": save_every,
        "learning_rate": float(p.get("lr", 1e-4 if mode == "lora" else 1e-5)),
        "weight_decay": 0.01,
        "warmup_steps": max(10, min(100, total // 10)),
        "max_batch_tokens": int(p.get("max_batch_tokens", 8192)),
        "max_grad_norm": 1.0,
        "save_path": str(ckpt),
        "tensorboard": str(job.work / "tb"),
        "lambdas": {"loss/diff": 1.0, "loss/stop": 1.0},
    }
    if mode == "lora":
        conf["lora"] = {"enable_lm": True, "enable_dit": True, "enable_proj": bool(p.get("lora_proj", False)),
                        "r": int(p.get("rank", 32)), "alpha": int(p.get("alpha", 32)), "dropout": 0.0}
    conf_path = job.work / "train_conf.yaml"
    conf_path.write_text(json.dumps(conf, indent=2), encoding="utf-8")  # JSON is valid YAML
    log(f"{mode}: {n_train} clips, {per_epoch} updates/epoch, {total} updates, save every {save_every}")
    job.progress(phase="train", step=0, total=total, per_epoch=per_epoch, mode=mode)

    metrics_f = (job.out / "train_metrics.jsonl").open("w", encoding="utf-8")

    def on_line(line: str) -> None:
        # "[train] step 120: loss/diff: 0.41, loss/stop: 0.01, lr: ..., epoch: 1.2, grad_norm: ..."
        if line.startswith("[train] step ") or line.startswith("[val] step "):
            split = line[1:line.index("]")]
            step = int(line.split("step ", 1)[1].split(":", 1)[0])
            m = parse_metrics(line.split(":", 1)[1])
            metrics_f.write(json.dumps({"split": split, "step": step, **m}) + "\n")
            metrics_f.flush()
            loss = m.get("loss/diff", 0) + m.get("loss/stop", 0)
            if split == "train":
                job.progress(phase="train", step=step + 1, total=total, loss=round(loss, 4),
                             epoch=round(m.get("epoch", 0), 2))
            else:
                job.progress(val_loss=round(loss, 4))
        if mode == "full":
            prune_optimizer_states(ckpt)

    tail = LogTail(ckpt / "train.log", on_line)
    tail.start()
    job.run([sys.executable, SRC / "scripts" / "train_voxcpm_finetune.py", "--config_path", conf_path], cwd=SRC)
    tail.stop.set()
    tail.join(5)
    metrics_f.close()
    prune_optimizer_states(ckpt, keep_latest=False)

    steps = sorted(d for d in ckpt.iterdir() if d.is_dir() and d.name.startswith("step_"))
    if not steps:
        raise RuntimeError("trainer produced no checkpoints")
    keep = steps if mode == "lora" else steps[-int(p.get("keep_full", 3)):]
    log(f"checkpoints: {[d.name for d in steps]}; keeping weights of {[d.name for d in keep]}")

    # samples from every checkpoint (+ the untrained base for comparison)
    job.progress(phase="samples", step=0, total=len(steps) + 1)
    plan = sample_plan(job)
    ref = plan.get("reference")
    ref_path = str(job.data / ref["audio"]) if ref else None
    import soundfile as sf
    from voxcpm import VoxCPM

    def speak(model, name: str) -> None:
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        for i, line in enumerate(plan.get("lines", [])):
            for kind in ("plain", "ref"):
                if kind == "ref" and not ref_path:
                    continue
                try:
                    wav = model.generate(text=line["text"], reference_wav_path=ref_path if kind == "ref" else None,
                                         cfg_value=2.0, inference_timesteps=10, seed=SEED)
                    sf.write(str(d / f"{i}_{kind}.wav"), wav, model.tts_model.sample_rate)
                except Exception as e:
                    log(f"sample {name}/{i}_{kind} failed: {e}")

    ck_meta = []
    if mode == "lora":
        model = VoxCPM.from_pretrained(base_path, load_denoiser=False, optimize=False,
                                       lora_weights_path=str(steps[0]))
        model.set_lora_enabled(False)
        speak(model, "base")
        model.set_lora_enabled(True)
        for i, d in enumerate(steps):
            model.load_lora(str(d))
            speak(model, d.name)
            job.progress(phase="samples", step=i + 2, total=len(steps) + 1)
        del model
    else:
        model = VoxCPM.from_pretrained(base_path, load_denoiser=False, optimize=False)
        speak(model, "base")
        del model
        for i, d in enumerate(steps):
            model = VoxCPM.from_pretrained(str(d), load_denoiser=False, optimize=False)
            speak(model, d.name)
            del model
            job.progress(phase="samples", step=i + 2, total=len(steps) + 1)

    for d in steps:
        st = int(d.name.split("_")[1])
        has = d in keep
        if has:
            dst = job.out / "checkpoints" / d.name
            shutil.copytree(d, dst, ignore=shutil.ignore_patterns("optimizer.pth", "scheduler.pth"))
        ck_meta.append({"name": d.name, "step": st, "epoch": round(st / per_epoch, 2), "weights": has})
    log(f"free disk before packaging: {free_gb():.0f} GB")
    job.package({"engine": "voxcpm2", "mode": mode, "base": BASE, "base_revision": p.get("base_revision"),
                 "checkpoints": ck_meta, "samples": plan, "sample_rate": 48000, "total_steps": total,
                 "per_epoch": per_epoch, "seed": SEED})


def prune_optimizer_states(ckpt: Path, keep_latest: bool = True) -> None:
    """Full fine-tuning saves ~3× the model size of optimizer state per checkpoint; only `latest` needs it."""
    if not ckpt.exists():
        return
    for d in ckpt.iterdir():
        if d.is_dir() and d.name.startswith("step_") and (d / "training_state.json").exists():
            for f in ("optimizer.pth", "scheduler.pth"):
                (d / f).unlink(missing_ok=True)
    if not keep_latest:
        shutil.rmtree(ckpt / "latest", ignore_errors=True)


if __name__ == "__main__":
    main()

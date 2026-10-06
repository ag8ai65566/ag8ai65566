#!/usr/bin/env python3
"""VoxCPM2 fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/voxcpm2).

1. writes a training config from the studio's effective parameters (LoRA or full fine-tuning, official recipe);
2. runs the official trainer (scripts/train_voxcpm_finetune.py from the pinned VoxCPM commit);
3. publishes model.tar with the distinct checkpoints as soon as training ends;
4. every checkpoint, plus the untrained base model, reads the same held-out lines aloud (model only, and with a
   reference clip), so checkpoints can be compared by ear and scored by the studio; these go into samples.tar.
"""
from __future__ import annotations

import json
import math
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import Job, LogTail, log, need_disk, parse_metrics, resolved_revision, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/voxcpm2"))
BASE = "openbmb/VoxCPM2"
SEED = 1234


def count_lines(p: Path) -> int:
    return sum(1 for x in p.read_text(encoding="utf-8").splitlines() if x.strip())


def schedule(n_train: int, p: dict) -> tuple[int, int]:
    """(updates per epoch, total updates). The studio computes the same numbers for its quote and sends
    total_steps; this fallback is only used when it is missing."""
    bs, accum = int(p.get("batch_size", 2)), int(p.get("grad_accum", 8))
    batches = n_train // bs  # the trainer drops the last incomplete batch; accumulation runs across epochs
    if batches < 1:
        raise RuntimeError(f"only {n_train} training clips: need at least {bs} for one batch")
    per_epoch = batches / accum  # optimizer updates per pass over the data (may be fractional)
    total = int(p.get("total_steps") or max(1, math.ceil(batches * float(p.get("epochs", 2)) / accum)))
    return per_epoch, min(total, int(p.get("max_steps_cap", 30000)))


def step_of(d: Path) -> int:
    return int(d.name.split("_")[1])


def main() -> None:
    job = Job()
    p = job.params
    mode = p.get("mode", "lora")
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE, revision=p.get("base_revision") or None)
    revision = resolved_revision(base_path)
    log(f"base model {BASE}@{revision}")

    train_manifest, val_manifest = job.data / "train.jsonl", job.data / "val.jsonl"
    n_train = count_lines(train_manifest)
    per_epoch, total = schedule(n_train, p)
    n_saves = int(p.get("saves", 6))
    save_every = max(10, math.ceil(total / n_saves))
    # full fine-tuning: each checkpoint ~8 GB of weights, plus optimizer state in `latest` and the archive copy
    need_disk(25 if mode == "lora" else 9 * (n_saves + 2) + 30)
    ckpt = job.work / "ckpt"
    conf = {
        "pretrained_path": base_path,
        "train_manifest": str(train_manifest),
        "val_manifest": str(val_manifest) if val_manifest.exists() and count_lines(val_manifest) else "",
        "sample_rate": 16000,
        "out_sample_rate": 48000,
        "batch_size": int(p.get("batch_size", 2)),
        "grad_accum_steps": int(p.get("grad_accum", 8)),
        "num_workers": 4,
        "preprocessing_num_workers": 4,
        "num_iters": total,
        "max_steps": total,
        "log_interval": 5,
        "valid_interval": save_every,
        "save_interval": save_every,
        "learning_rate": float(p.get("lr", 1e-4 if mode == "lora" else 1e-5)),
        "weight_decay": 0.01,
        "warmup_steps": max(1, min(100, total // 10)),
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
    log(f"{mode}: {n_train} clips, {per_epoch} updates/epoch, {total} updates "
        f"({total / per_epoch:.2f} epochs), save every {save_every}")
    job.progress(phase="train", step=0, total=total, per_epoch=per_epoch, mode=mode)

    metrics_f = (job.out / "train_metrics.jsonl").open("w", encoding="utf-8")

    def on_line(line: str) -> None:
        # "[train] step 120: loss/diff: 0.41, loss/stop: 0.01, lr: ..., epoch: 1.2, grad_norm: ..."
        if line.startswith("[train] step ") or line.startswith("[val] step "):
            split = line[1:line.index("]")]
            step = int(line.split("step ", 1)[1].split(":", 1)[0])
            m = parse_metrics(line.split(":", 1)[1])
            metrics_f.write(json.dumps({"split": split, "step": step + 1, **m}) + "\n")
            metrics_f.flush()
            loss = m.get("loss/diff", 0) + m.get("loss/stop", 0)
            if split == "train":
                job.progress(phase="train", step=step + 1, total=total, loss=round(loss, 4),
                             epoch=round(m.get("epoch", 0), 2))
            else:
                job.progress(val_loss=round(loss, 4))
        if mode == "full":
            prune_optimizer_states(ckpt, keep_newest=True)

    tail = LogTail(ckpt / "train.log", on_line)
    tail.start()
    job.run([sys.executable, SRC / "scripts" / "train_voxcpm_finetune.py", "--config_path", conf_path], cwd=SRC)
    tail.stop.set()
    tail.join(5)
    metrics_f.close()
    prune_optimizer_states(ckpt, keep_newest=False)

    # The trainer saves at step 0 (after one update), every save_every, at the last loop step (total-1) and once
    # more after the loop (total) with identical weights. Keep distinct, trained checkpoints only.
    steps = sorted((d for d in ckpt.iterdir() if d.is_dir() and d.name.startswith("step_")), key=step_of)
    if len(steps) >= 2 and step_of(steps[-1]) == total and step_of(steps[-2]) == total - 1:
        shutil.rmtree(steps.pop(-2), ignore_errors=True)
    if len(steps) >= 2 and step_of(steps[0]) == 0:
        shutil.rmtree(steps.pop(0), ignore_errors=True)
    if not steps:
        raise RuntimeError("trainer produced no checkpoints")
    keep = steps if mode == "lora" else steps[-int(p.get("keep_full", 3)):]
    log(f"checkpoints: {[d.name for d in steps]}; keeping weights of {[d.name for d in keep]}")
    # step_N holds the weights after N+1 updates (zero-based loop counter), except the final save at `total`
    updates = {d.name: (step_of(d) if step_of(d) == total else step_of(d) + 1) for d in steps}
    ck_meta = [{"name": d.name, "step": updates[d.name], "epoch": round(updates[d.name] / per_epoch, 2),
                "weights": d in keep} for d in steps]
    meta = {"engine": "voxcpm2", "mode": mode, "base": BASE, "base_revision": revision, "checkpoints": ck_meta,
            "samples": sample_plan(job), "sample_rate": 48000, "total_steps": total, "per_epoch": per_epoch,
            "seed": SEED, "sampling": "pending"}
    job.package(meta, "model.tar", [(job.out / "train_metrics.jsonl", "model/train_metrics.jsonl")]
                + [(d, f"model/checkpoints/{d.name}") for d in keep])

    try:
        conditions, made, expected = sample_all(job, base_path, mode, steps)
        meta.update(sampling="complete" if made == expected else "incomplete", sample_conditions=conditions,
                    samples_made=made, samples_expected=expected)
    except Exception as e:  # the model is already safe in model.tar
        log(f"sampling incomplete: {e}")
        meta.update(sampling="incomplete", sampling_error=str(e)[:300])
    if (job.out / "samples").exists():
        job.package(meta, "samples.tar", [(job.out / "samples", "model/samples")])


def sample_all(job: Job, base_path: str, mode: str, steps: list[Path]) -> dict:
    """Each checkpoint (and the base) reads the held-out lines: 'plain' = the model alone, 'ref' = with the same
    reference clip. Seeds are fixed so the only difference between clips is the checkpoint."""
    plan = sample_plan(job)
    ref = plan.get("reference")
    ref_path = str(job.data / ref["audio"]) if ref else None
    import soundfile as sf
    from voxcpm import VoxCPM

    job.progress(phase="samples", step=0, total=len(steps) + 1)
    counts = {"made": 0}

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
                    counts["made"] += 1
                except Exception as e:
                    log(f"sample {name}/{i}_{kind} failed: {e}")

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
    expected = (len(steps) + 1) * len(plan.get("lines", [])) * (2 if ref_path else 1)
    return ({"plain": {"mode": "plain", "seed": SEED},
             "ref": {"mode": "ref", "reference": (ref or {}).get("id"), "seed": SEED}}, counts["made"], expected)


def prune_optimizer_states(ckpt: Path, keep_newest: bool) -> None:
    """Full fine-tuning saves ~3× the model size of optimizer state per checkpoint. While training runs, the newest
    step folder may still be being copied into `latest`, so it is left alone; older ones are safe to trim."""
    if not ckpt.exists():
        return
    dirs = sorted((d for d in ckpt.glob("step_*") if d.is_dir()), key=step_of)
    for d in dirs[:-1] if keep_newest else dirs:
        for f in ("optimizer.pth", "scheduler.pth"):
            (d / f).unlink(missing_ok=True)
    if not keep_newest:
        shutil.rmtree(ckpt / "latest", ignore_errors=True)


if __name__ == "__main__":
    main()

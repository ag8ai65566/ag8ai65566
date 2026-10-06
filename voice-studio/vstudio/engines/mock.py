"""A test engine: no model, no GPU. It hums a pitch contour shaped like the text, so every screen and job of the
studio can be tried end to end before a real engine is installed. It is labelled as a test in the UI."""
from __future__ import annotations

from pathlib import Path

import numpy as np

from . import export, remote
from .base import Engine, Synthesis, TrainPreset

TRAIN_ENTRY = r'''#!/usr/bin/env python3
"""Mock training: pretends to train, writes progress.json, publishes model.tar, then hums the sample lines into
samples.tar, exactly like the real engines, so the whole cloud path can be checked cheaply."""
import math, os, struct, sys, time, wave
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import Job, sample_plan

job = Job()
steps = int(job.params.get("steps", 20))
delay = float(os.environ.get("VS_MOCK_DELAY", "0.5"))
for s in range(1, steps + 1):
    time.sleep(delay)
    job.progress(phase="train", step=s, total=steps, loss=round(2.0 / s, 4), epoch=round(s / steps, 2))
plan = sample_plan(job)
names = [f"step_{s:07d}" for s in (steps // 2, steps)]
for name in names:
    d = job.out / "checkpoints" / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "weights.txt").write_text("mock")
    (d / "optimizer.pth").write_text("not packaged")
cks = [{"name": n, "step": int(n.split("_")[1]), "epoch": int(n.split("_")[1]) / steps, "weights": True} for n in names]
meta = {"engine": "mock", "mode": "mock", "checkpoints": cks, "samples": plan, "total_steps": steps,
        "per_epoch": steps, "sampling": "pending"}
job.package(meta, "model.tar", [(job.out / "checkpoints" / n, f"model/checkpoints/{n}") for n in names])
if os.environ.get("VS_MOCK_FAIL_SAMPLES") != "1":
    for k, name in enumerate(["base"] + names):
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        for i, line in enumerate(plan.get("lines", [])):
            sr, dur = 16000, min(6.0, 0.08 * len(line["text"]) + 0.4)
            f0 = 160 + 25 * k
            with wave.open(str(d / f"{i}_plain.wav"), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
                w.writeframes(b"".join(struct.pack("<h", int(6000 * math.sin(2 * math.pi * f0 * n / sr)))
                                       for n in range(int(sr * dur))))
    meta["sampling"] = "complete"
    job.package(meta, "samples.tar", [(job.out / "samples", "model/samples")])
'''


class MockEngine(Engine):
    id = "mock"
    name = "測試引擎（不是真的語音）"
    summary = "不需要 GPU 的假引擎，用來試用整個平台流程。產生的是哼聲，不是語音。"
    license = "—"
    languages = ("ja", "en", "zh")
    supports_tags = True
    supports_instruct = True
    image = "runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04"
    presets = [TrainPreset("quick", "快速測試", "20 步，約 1 分鐘。用來確認雲端帳號與流程都正常，不會產生真的聲音。",
                           {"steps": 20}, ["NVIDIA GeForce RTX 4090", "NVIDIA RTX 6000 Ada Generation"], 0.01, disk_gb=20, ram_gb=8, vcpu=2)]

    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        return export.write(ds, out_dir)

    def cloud_files(self) -> dict[str, str]:
        setup = ('#!/bin/bash\nset -e\nENV="${VS_ROOT:-/workspace/vs}/envs/mock"\n'
                 '[ -f "$ENV/bin/activate" ] || python3 -m venv --system-site-packages "$ENV"\necho mock setup ok\n')
        return {"setup_env.sh": setup, "train_entry.py": TRAIN_ENTRY,
                "vs_common.py": remote.read("vs_common.py")}

    def steps(self, n_train: int, preset_id: str, params: dict | None = None) -> int:
        return int(self.preset(preset_id).params["steps"])

    def available(self):
        return True, "隨時可用"

    def modes(self, meta: dict) -> list[str]:
        return ["plain", "ref"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        meta = self.model_meta(model_dir)
        ck = self.checkpoint_dir(model_dir, meta, checkpoint)
        return {"meta": meta, "checkpoint": ck.name if ck else None}

    def synthesize(self, handle, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
        sr = 24000
        rng = np.random.default_rng(seed if seed is not None else abs(hash(text)) % (2 ** 32))
        units = max(1, len(text))
        dur = min(20.0, 0.09 * units + 0.3)
        t = np.arange(int(sr * dur)) / sr
        base = 180 + 40 * np.sin(2 * np.pi * 0.7 * t + rng.random())
        if "excited" in style or "bright" in style:
            base *= 1.25
        phase = 2 * np.pi * np.cumsum(base) / sr
        env = np.clip(np.sin(np.pi * t * units / dur) ** 2, 0, 1) * np.minimum(1, t * 10) * np.minimum(1, (dur - t) * 10)
        y = 0.25 * env * (np.sin(phase) + 0.3 * np.sin(2 * phase) + 0.1 * np.sin(3 * phase))
        return Synthesis(y.astype(np.float32), sr, {"mock": True, "mode": mode,
                                                    "checkpoint": (handle or {}).get("checkpoint")})

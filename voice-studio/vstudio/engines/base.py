"""The engine interface: one adapter per TTS model family.

An engine knows how to
- turn a studio dataset into its own training format (export_dataset);
- describe the cloud job that fine-tunes it (setup script, training entry point, container image, GPU sizes);
- load a fine-tuned model and synthesize speech locally (load / synthesize);
- translate the project's bracket performance tags ([deadpan], [laughs]) into its own control format.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


@dataclass
class TrainPreset:
    id: str
    label: str           # shown in the UI (zh-TW)
    description: str
    params: dict
    gpu: list[str]       # RunPod gpuTypeIds, in order of preference
    hours_per_data_hour: float  # rough wall-clock estimate per hour of training audio (before calibration)
    s_per_step: float = 0.0     # first guess of seconds per training step, replaced by measured speed after a run
    disk_gb: int = 80           # pod container disk
    min_hours: float = 0.0      # recommended minimum amount of approved audio
    recommended: bool = False


MODES = {"plain": "只用模型", "ref": "參考音色", "hifi": "完整複製"}


@dataclass
class Synthesis:
    audio: np.ndarray
    sr: int
    info: dict = field(default_factory=dict)


class Engine:
    id = "base"
    name = "Base"
    summary = ""
    license = ""
    license_note = ""
    languages: tuple[str, ...] = ()
    supports_tags = False       # inline bracket tags understood natively
    supports_instruct = False   # free-text style instruction
    needs_reference = False     # synthesis needs a reference clip
    infer_vram_gb = 0.0
    image = ""                  # container image for cloud training
    presets: list[TrainPreset] = []

    # --- dataset & training ---------------------------------------------------------------------------------
    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        """Write the engine's training files for dataset `ds` into out_dir; return info for config.json."""
        raise NotImplementedError

    def cloud_files(self) -> dict[str, str]:
        """Remote file name → contents (setup_env.sh, train_entry.py …) placed next to bootstrap.sh."""
        raise NotImplementedError

    def steps(self, n_train: int, preset_id: str) -> int:
        """Training steps the cloud script will run for n_train clips (0 = unknown)."""
        return 0

    def estimate(self, data_hours: float, preset_id: str, usd_h: float, n_train: int = 0,
                 s_per_step: float | None = None) -> dict:
        """Wall-clock and cost estimate. Uses the measured speed of an earlier run when there is one."""
        p = self.preset(preset_id)
        steps = self.steps(n_train, preset_id) if n_train else 0
        sps = s_per_step or p.s_per_step
        if steps and sps:
            train_h = steps * sps / 3600
            basis = "measured" if s_per_step else "guess"
        else:
            train_h = data_hours * p.hours_per_data_hour
            basis = "guess"
        hours = max(0.2, train_h) + 0.45  # + environment check, model download, samples, packaging
        return {"hours": round(hours, 2), "usd": round(hours * usd_h, 2), "steps": steps, "basis": basis}

    def preset(self, preset_id: str) -> TrainPreset:
        for p in self.presets:
            if p.id == preset_id:
                return p
        return self.presets[0]

    # --- inference ------------------------------------------------------------------------------------------
    def available(self) -> tuple[bool, str]:
        """Whether this machine can run the engine locally (packages installed, GPU memory)."""
        return False, "未安裝"

    def install_spec(self) -> dict:
        """pip requirements (and environment) to install the engine locally for inference."""
        return {}

    def modes(self, meta: dict) -> list[str]:
        """Synthesis modes a model supports: plain (model only), ref (reference timbre), hifi (reference + transcript)."""
        return ["plain"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        raise NotImplementedError

    def synthesize(self, handle, text: str, language: str | None = None, style: str = "", mode: str = "plain",
                   reference: dict | None = None, seed: int | None = None, **kw) -> Synthesis:
        """reference: {"path": wav, "text": transcript or ""}"""
        raise NotImplementedError

    def unload(self, handle) -> None:
        try:
            import gc
            del handle
            gc.collect()
            import torch
            torch.cuda.empty_cache()
        except Exception:
            pass

    # --- helpers for model folders -------------------------------------------------------------------------
    @staticmethod
    def model_meta(model_dir: Path) -> dict:
        """engine.json written by the cloud script; zero-shot models have none (or mode=zeroshot)."""
        import json
        f = Path(model_dir) / "engine.json"
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"mode": "zeroshot", "checkpoints": []}

    @staticmethod
    def checkpoint_dir(model_dir: Path, meta: dict, checkpoint: str | None) -> Path | None:
        cks = [c for c in meta.get("checkpoints", []) if c.get("weights")]
        if not cks:
            return None
        names = [c["name"] for c in cks]
        name = checkpoint if checkpoint in names else names[-1]
        return Path(model_dir) / "checkpoints" / name

    # --- tags -----------------------------------------------------------------------------------------------
    def render_tags(self, text_with_tags: str) -> tuple[str, str]:
        """Return (text for the engine, style instruction). Default: strip tags into a style instruction."""
        import re
        tags = re.findall(r"\[([^\[\]]+)\]", text_with_tags)
        text = re.sub(r"\s*\[[^\[\]]+\]\s*", " ", text_with_tags).strip()
        style = ", ".join(dict.fromkeys(t.strip() for t in tags))
        return text, style

    def info(self) -> dict:
        ok, why = self.available()
        return {"id": self.id, "name": self.name, "summary": self.summary, "license": self.license,
                "license_note": self.license_note, "languages": list(self.languages),
                "supports_tags": self.supports_tags, "supports_instruct": self.supports_instruct,
                "needs_reference": self.needs_reference, "infer_vram_gb": self.infer_vram_gb,
                "available": ok, "available_note": why,
                "install": bool(self.install_spec()),
                "presets": [{"id": p.id, "label": p.label, "description": p.description, "gpu": p.gpu,
                             "params": p.params, "min_hours": p.min_hours, "recommended": p.recommended}
                            for p in self.presets]}

"""Environment-driven configuration. See .env.example for the full list."""

from __future__ import annotations

import os
from pathlib import Path

from workflow import Lora, Settings

COMFY_URL = os.environ.get("COMFY_URL", "http://127.0.0.1:8188")
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/data/outputs"))
INBOX_DIR = Path(os.environ.get("INBOX_DIR", "/data/inbox"))
DONE_DIR = Path(os.environ.get("DONE_DIR", "/data/inbox/done"))
APP_URL = os.environ.get("APP_URL", "http://127.0.0.1:8000")

# Profiles pick the model files. "fp8" needs ~24GB VRAM, "gguf" runs on less.
PROFILE = os.environ.get("PROFILE", "fp8").lower()
GGUF_QUANT = os.environ.get("GGUF_QUANT", "Q4_K_M")


def _bool(name: str, default: bool) -> bool:
    return os.environ.get(name, str(default)).strip().lower() in ("1", "true", "yes", "on")


def _parse_loras(raw: str) -> list[Lora]:
    """Parse "name.safetensors:0.8, other.safetensors" into Lora objects."""
    loras: list[Lora] = []
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        name, _, strength = chunk.rpartition(":")
        if not name:  # no colon present
            loras.append(Lora(chunk))
            continue
        try:
            loras.append(Lora(name.strip(), float(strength)))
        except ValueError:
            loras.append(Lora(chunk))
    return loras


def settings() -> Settings:
    s = Settings()

    if PROFILE == "gguf":
        s.loader = "gguf"
        s.high_noise = f"Wan2.2-I2V-A14B-HighNoise-{GGUF_QUANT}.gguf"
        s.low_noise = f"Wan2.2-I2V-A14B-LowNoise-{GGUF_QUANT}.gguf"
    else:
        s.loader = "safetensors"
        s.high_noise = "wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors"
        s.low_noise = "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors"

    s.high_noise = os.environ.get("MODEL_HIGH", s.high_noise)
    s.low_noise = os.environ.get("MODEL_LOW", s.low_noise)
    s.text_encoder = os.environ.get("TEXT_ENCODER", s.text_encoder)
    s.vae = os.environ.get("VAE", s.vae)
    s.weight_dtype = os.environ.get("WEIGHT_DTYPE", s.weight_dtype)

    s.lightning = _bool("LIGHTNING", True)
    s.lightning_strength = float(os.environ.get("LIGHTNING_STRENGTH", s.lightning_strength))
    s.loras = _parse_loras(os.environ.get("LORAS", ""))
    s.loras_high = _parse_loras(os.environ.get("LORAS_HIGH", ""))
    s.loras_low = _parse_loras(os.environ.get("LORAS_LOW", ""))

    s.tier = os.environ.get("TIER", s.tier)
    s.length = int(os.environ.get("LENGTH", s.length))
    s.fps = int(os.environ.get("FPS", s.fps))

    # Only meaningful when LIGHTNING=false; the preset overrides these.
    s.steps = int(os.environ.get("STEPS", s.steps))
    s.boundary = int(os.environ.get("BOUNDARY", s.boundary))
    s.cfg = float(os.environ.get("CFG", s.cfg))
    s.shift = float(os.environ.get("SHIFT", s.shift))
    s.sampler = os.environ.get("SAMPLER", s.sampler)
    s.scheduler = os.environ.get("SCHEDULER", s.scheduler)
    return s

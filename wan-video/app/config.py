"""Environment-driven configuration. See .env.example for the full list.

Almost everything the UI exposes is chosen per job now; the values here are
just the starting defaults.
"""

from __future__ import annotations

import os
from pathlib import Path

import registry

COMFY_URL = os.environ.get("COMFY_URL", "http://127.0.0.1:8188")
MODELS_DIR = Path(os.environ.get("MODELS_DIR", "/models"))
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/data/outputs"))
INBOX_DIR = Path(os.environ.get("INBOX_DIR", "/data/inbox"))
DONE_DIR = Path(os.environ.get("DONE_DIR", "/data/inbox/done"))
APP_URL = os.environ.get("APP_URL", "http://127.0.0.1:8000")

DEFAULT_MODEL = os.environ.get("MODEL", "wan22-14b-fp8")
DEFAULT_TIER = os.environ.get("TIER", "")
DEFAULT_LENGTH = int(os.environ.get("LENGTH", "0") or 0)
PROMPT_DEFAULT = os.environ.get("PROMPT_DEFAULT", "subtle natural motion, cinematic")


def _bool(name: str, default: bool) -> bool:
    return os.environ.get(name, str(default)).strip().lower() in ("1", "true", "yes", "on")


LIGHTNING = _bool("LIGHTNING", True)
WEIGHT_DTYPE = os.environ.get("WEIGHT_DTYPE", "default")


def parse_loras(raw: str) -> list[registry.Lora]:
    """Parse "name.safetensors:0.8, other.safetensors" into Lora objects."""
    loras: list[registry.Lora] = []
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        name, _, strength = chunk.rpartition(":")
        if not name:
            loras.append(registry.Lora(chunk))
            continue
        try:
            loras.append(registry.Lora(name.strip(), float(strength)))
        except ValueError:
            loras.append(registry.Lora(chunk))
    return loras


ENV_LORAS = parse_loras(os.environ.get("LORAS", ""))
ENV_LORAS_HIGH = parse_loras(os.environ.get("LORAS_HIGH", ""))
ENV_LORAS_LOW = parse_loras(os.environ.get("LORAS_LOW", ""))


def default_model() -> registry.ModelDef:
    return registry.get(DEFAULT_MODEL) or registry.runnable()[0]


def params_for(model: registry.ModelDef, lightning: bool | None = None) -> registry.GenParams:
    """Model defaults, with .env overrides layered on top."""
    p = registry.GenParams.defaults_for(
        model, lightning=LIGHTNING if lightning is None else lightning
    )
    p.weight_dtype = WEIGHT_DTYPE
    p.loras = list(ENV_LORAS)
    p.loras_high = list(ENV_LORAS_HIGH)
    p.loras_low = list(ENV_LORAS_LOW)
    if DEFAULT_LENGTH:
        p.length = DEFAULT_LENGTH
    # Explicit sampler overrides, for people who want to experiment.
    for key, attr, cast in [
        ("STEPS", "steps", int),
        ("CFG", "cfg", float),
        ("SHIFT", "shift", float),
        ("BOUNDARY", "boundary", int),
        ("SAMPLER", "sampler", str),
        ("SCHEDULER", "scheduler", str),
        ("FPS", "fps", int),
    ]:
        raw = os.environ.get(key)
        if raw:
            setattr(p, attr, cast(raw))
    return p


def default_tier(model: registry.ModelDef) -> str:
    if DEFAULT_TIER and DEFAULT_TIER in model.tiers:
        return DEFAULT_TIER
    return next(iter(model.tiers), "480p")

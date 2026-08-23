"""Environment-driven configuration. See .env.example for the full list.

Almost everything the UI exposes is chosen per job now; the values here are
just the starting defaults.
"""

from __future__ import annotations

import os
from pathlib import Path

import registry

REPO = Path(__file__).resolve().parents[1]


def _dir(env_name: str, *candidates: Path) -> Path:
    """Env var wins; otherwise the first candidate that exists, else the first.

    The Docker images set these explicitly. A bare-metal install (or someone
    running check.py by hand) gets the paths next to the repo instead of the
    container's /models and /data, which would not exist there.
    """
    raw = os.environ.get(env_name)
    if raw:
        return Path(raw)
    return next((p for p in candidates if p.exists()), candidates[0])


COMFY_URL = os.environ.get("COMFY_URL", "http://127.0.0.1:8188")
MODELS_DIR = _dir("MODELS_DIR", REPO / "ComfyUI" / "models", REPO / "models", Path("/models"))
OUTPUT_DIR = _dir("OUTPUT_DIR", REPO / "data" / "outputs", Path("/data/outputs"))
INBOX_DIR = _dir("INBOX_DIR", REPO / "data" / "inbox", Path("/data/inbox"))
DONE_DIR = _dir("DONE_DIR", INBOX_DIR / "done")
# Source images for image-to-image and comic previews. Deliberately NOT
# INBOX_DIR: that folder is the drop-folder watcher's queue, and anything left
# there gets picked up, submitted as a video job and moved to done/ - which
# would delete an image job's source out from under it before the worker runs.
STAGING_DIR = _dir("STAGING_DIR", REPO / "data" / "staging", Path("/data/staging"))

# Official reference art, filed per character. Kept out of OUTPUT_DIR on
# purpose: these are inputs the user collected, not things this app generated,
# and losing them to a history cleanup would be someone else's afternoon.
REFS_DIR = _dir("REFS_DIR", REPO / "data" / "refs", Path("/data/refs"))
APP_URL = os.environ.get("APP_URL", "http://127.0.0.1:8000")

# Checkouts the update check looks at. In Docker the app does not own either of
# them, so both are allowed not to be git repos - the check just reports that.
REPO_DIR = _dir("REPO_DIR", REPO.parent, REPO)
COMFY_DIR = _dir("COMFY_DIR", REPO / "ComfyUI", Path("/opt/ComfyUI"))

DEFAULT_MODEL = os.environ.get("MODEL", "wan22-14b-fp8")
DEFAULT_TIER = os.environ.get("TIER", "")
DEFAULT_LENGTH = int(os.environ.get("LENGTH", "0") or 0)
PROMPT_DEFAULT = os.environ.get("PROMPT_DEFAULT", "subtle natural motion, cinematic")


def _bool(name: str, default: bool) -> bool:
    return os.environ.get(name, str(default)).strip().lower() in ("1", "true", "yes", "on")


LIGHTNING = _bool("LIGHTNING", True)
COMFY_ARGS = os.environ.get("COMFY_ARGS", "").strip()
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

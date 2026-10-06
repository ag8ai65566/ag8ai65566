"""Paths, settings and secrets.

Settings that are not secret live in data/settings.json. Secrets (API keys) live in the operating system's credential
store through `keyring` (Windows Credential Manager on Windows), so they never sit in a plain file, a log or git.
"""
from __future__ import annotations

import json
import os
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(os.environ.get("VSTUDIO_DATA", ROOT / "data")).resolve()
KEYRING_SERVICE = "voice-studio"
# model downloads (Hugging Face) are kept with the studio's data, not in the user profile
os.environ.setdefault("HF_HOME", str(DATA / "hf"))
SECRET_NAMES = ("runpod_api_key", "runpod_s3_access_key", "runpod_s3_secret_key", "hf_token")

DEFAULTS = {
    "language_ui": "zh-TW",
    "host": "127.0.0.1",
    "port": 7860,
    # data preparation
    "asr_primary": "large-v3",
    "asr_secondary": "large-v3-turbo",
    "asr_device": "auto",
    "segment_min_s": 2.0,
    "segment_max_s": 15.0,
    "segment_target_s": 8.0,
    "separate_vocals": False,
    "speaker_match_threshold": 0.62,
    # cloud
    "runpod_volume_id": "",
    "runpod_datacenter": "",
    "runpod_cloud_type": "SECURE",
    "runpod_max_hours": 12.0,
    # engine
    "default_engine": "voxcpm2",
    "speed": {},          # measured seconds per training step, per engine:preset:gpu (filled in after runs)
    # pronunciation dictionary applied before synthesis: [{"from": "推し", "to": "おし", "lang": "ja"}]
    "lexicon": [],
}

_lock = threading.Lock()


def path(*parts: str) -> Path:
    p = DATA.joinpath(*parts)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def ensure_dirs() -> None:
    for d in ("sources", "segments", "voices", "datasets", "models", "outputs", "jobs", "presets", "tmp"):
        (DATA / d).mkdir(parents=True, exist_ok=True)


def load_settings() -> dict:
    f = DATA / "settings.json"
    data = dict(DEFAULTS)
    if f.exists():
        try:
            data.update(json.loads(f.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            pass
    return data


def save_settings(update: dict) -> dict:
    with _lock:
        data = load_settings()
        for k, v in update.items():
            if k in DEFAULTS:
                data[k] = v
        f = DATA / "settings.json"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return data


# --- secrets -----------------------------------------------------------------------------------------------------

def _keyring():
    try:
        import keyring
        keyring.get_keyring()
        return keyring
    except Exception:  # no usable backend (headless Linux test boxes)
        return None


def get_secret(name: str) -> str | None:
    if name not in SECRET_NAMES:
        raise KeyError(name)
    env = os.environ.get("VSTUDIO_" + name.upper())
    if env:
        return env
    kr = _keyring()
    if kr is None:
        return None
    try:
        return kr.get_password(KEYRING_SERVICE, name)
    except Exception:
        return None


def set_secret(name: str, value: str | None) -> bool:
    if name not in SECRET_NAMES:
        raise KeyError(name)
    kr = _keyring()
    if kr is None:
        return False
    try:
        if value:
            kr.set_password(KEYRING_SERVICE, name, value)
        else:
            try:
                kr.delete_password(KEYRING_SERVICE, name)
            except Exception:
                pass
        return True
    except Exception:
        return False


def secret_status() -> dict:
    """Which secrets are set, never their values."""
    return {n: bool(get_secret(n)) for n in SECRET_NAMES}

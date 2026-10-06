"""Small helper models downloaded on first use into data/assets (never committed)."""
from __future__ import annotations

import hashlib
import urllib.request
from pathlib import Path

from . import config

ASSETS = {
    # Silero VAD v5 (MIT), ONNX, 16 kHz
    "silero_vad.onnx": "https://raw.githubusercontent.com/snakers4/silero-vad/master/src/silero_vad/data/silero_vad.onnx",
}


def fetch(name: str) -> Path:
    dst = config.path("assets", name)
    if dst.exists() and dst.stat().st_size > 1000:
        return dst
    url = ASSETS[name]
    tmp = dst.with_suffix(dst.suffix + ".part")
    with urllib.request.urlopen(url, timeout=120) as r, open(tmp, "wb") as fh:
        while chunk := r.read(1 << 20):
            fh.write(chunk)
    tmp.replace(dst)
    return dst


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        while chunk := fh.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()

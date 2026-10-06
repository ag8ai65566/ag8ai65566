"""Audio I/O. ffmpeg comes from the imageio-ffmpeg wheel, so nothing has to be installed separately on Windows."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf

MASTER_SR = 48000  # the studio keeps 48 kHz mono masters; engines resample when a dataset is exported
MEDIA_EXT = {".wav", ".flac", ".mp3", ".m4a", ".aac", ".ogg", ".opus", ".wma",
             ".mp4", ".mkv", ".mov", ".webm", ".avi", ".flv", ".ts", ".m4v"}


def ffmpeg() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    flags = 0x08000000 if hasattr(subprocess, "STARTUPINFO") else 0  # CREATE_NO_WINDOW on Windows
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                          creationflags=flags)


def probe_duration(src: Path) -> float | None:
    """Duration in seconds, parsed from ffmpeg's header output (no ffprobe needed)."""
    r = _run([ffmpeg(), "-hide_banner", "-i", str(src)])
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", r.stderr)
    if not m:
        return None
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def has_audio(src: Path) -> bool:
    r = _run([ffmpeg(), "-hide_banner", "-i", str(src)])
    return "Audio:" in r.stderr


def extract(src: Path, dst: Path, sr: int = MASTER_SR, start: float | None = None, dur: float | None = None) -> Path:
    """Decode any audio or video file to mono 16-bit WAV at `sr`."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [ffmpeg(), "-hide_banner", "-loglevel", "error", "-y"]
    if start is not None:
        cmd += ["-ss", f"{start:.3f}"]
    cmd += ["-i", str(src)]
    if dur is not None:
        cmd += ["-t", f"{dur:.3f}"]
    cmd += ["-vn", "-ac", "1", "-ar", str(sr), "-c:a", "pcm_s16le", str(dst)]
    r = _run(cmd)
    if r.returncode != 0 or not dst.exists():
        raise RuntimeError(f"ffmpeg failed: {r.stderr[-400:]}")
    return dst


def load(path: Path, sr: int | None = None) -> tuple[np.ndarray, int]:
    data, rate = sf.read(str(path), dtype="float32", always_2d=False)
    if data.ndim > 1:
        data = data.mean(axis=1)
    if sr and rate != sr:
        data = resample(data, rate, sr)
        rate = sr
    return data, rate


def save(path: Path, data: np.ndarray, sr: int, synthetic: dict | None = None) -> Path:
    """16-bit WAV. Synthetic speech gets a RIFF INFO comment saying so (see tag_synthetic)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with sf.SoundFile(str(path), "w", samplerate=sr, channels=1, subtype="PCM_16", format="WAV") as f:
        if synthetic is not None:
            f.comment = tag_synthetic(synthetic)
            f.software = "Voice Studio (AI-generated speech)"
        f.write(np.clip(np.asarray(data, dtype=np.float32), -1, 1))
    return path


def resample(x: np.ndarray, sr_from: int, sr_to: int) -> np.ndarray:
    if sr_from == sr_to:
        return x
    from math import gcd
    from scipy.signal import resample_poly
    g = gcd(sr_from, sr_to)
    return resample_poly(x, sr_to // g, sr_from // g).astype(np.float32)


def stats(x: np.ndarray, sr: int) -> dict:
    """Cheap quality signals: peak, clipping ratio, RMS level and a rough SNR from frame energies."""
    if len(x) == 0:
        return {"peak": 0.0, "clip": 0.0, "rms_db": -120.0, "snr": 0.0}
    peak = float(np.max(np.abs(x)))
    clip = float(np.mean(np.abs(x) > 0.985))
    frame = max(1, int(sr * 0.02))
    n = len(x) // frame
    if n < 4:
        e = np.array([np.mean(x ** 2) + 1e-12])
    else:
        e = np.mean(x[: n * frame].reshape(n, frame) ** 2, axis=1) + 1e-12
    rms_db = float(10 * np.log10(np.mean(e)))
    noise = np.percentile(e, 10)
    speech = np.percentile(e, 90)
    snr = float(10 * np.log10(speech / noise)) if noise > 0 else 60.0
    return {"peak": peak, "clip": clip, "rms_db": rms_db, "snr": snr}


def concat(parts: list[tuple[np.ndarray, float]], sr: int) -> np.ndarray:
    """Join clips; each tuple is (audio, silence-after-seconds)."""
    out = []
    for audio, gap in parts:
        out.append(audio)
        if gap > 0:
            out.append(np.zeros(int(sr * gap), dtype=np.float32))
    return np.concatenate(out) if out else np.zeros(0, dtype=np.float32)


def to_mp3(src: Path, dst: Path, bitrate: str = "192k", synthetic: dict | None = None) -> Path:
    tags = ["-metadata", f"comment={tag_synthetic(synthetic)}"] if synthetic is not None else []
    r = _run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-y", "-i", str(src), "-b:a", bitrate, *tags, str(dst)])
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-300:])
    return dst


def tag_synthetic(meta: dict) -> str:
    """Metadata comment written into exported files so synthetic speech stays labelled as such."""
    return json.dumps({"synthetic": True, "generator": "Voice Studio", **meta}, ensure_ascii=False)

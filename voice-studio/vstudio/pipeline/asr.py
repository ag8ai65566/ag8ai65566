"""Transcription with two Whisper models and an agreement score.

Each segment is transcribed by a primary model (large-v3) and a second, different model (large-v3-turbo). Where the
two agree, the transcript is very likely right; where they disagree, the segment is flagged for review or dropped.
Training on wrong transcripts is the most common reason a fine-tuned voice mumbles or skips words.
"""
from __future__ import annotations

import os
import re
import unicodedata

import numpy as np

_models: dict = {}


def _device(pref: str = "auto") -> tuple[str, str]:
    if pref != "auto":
        return pref, ("float16" if pref == "cuda" else "int8")
    try:
        import ctranslate2
        if ctranslate2.get_cuda_device_count() > 0:
            return "cuda", "float16"
    except Exception:
        pass
    return "cpu", "int8"


def _load_cuda_dlls() -> None:
    """On Windows CTranslate2 needs the cuBLAS/cuDNN DLLs that the CUDA build of PyTorch ships; importing torch
    first loads them into the process, so no separate CUDA toolkit install is needed."""
    if os.name == "nt":
        try:
            import torch  # noqa: F401
        except Exception:
            pass


def model(name: str, device: str = "auto"):
    key = (name, device)
    if key not in _models:
        _load_cuda_dlls()
        from faster_whisper import WhisperModel
        dev, ct = _device(device)
        from .. import config
        _models[key] = WhisperModel(name, device=dev, compute_type=ct, download_root=str(config.DATA / "assets" / "whisper"))
    return _models[key]


def unload() -> None:
    _models.clear()
    try:
        import gc
        gc.collect()
        import torch
        torch.cuda.empty_cache()
    except Exception:
        pass


def transcribe(audio16k: np.ndarray, name: str, language: str | None = None, device: str = "auto",
               prompt: str | None = None) -> dict:
    m = model(name, device)
    segs, info = m.transcribe(audio16k, language=language, beam_size=5, vad_filter=False,
                              condition_on_previous_text=False, initial_prompt=prompt, without_timestamps=True)
    segs = list(segs)
    text = "".join(s.text for s in segs).strip()
    lp = float(np.mean([s.avg_logprob for s in segs])) if segs else -9.0
    nsp = float(np.max([s.no_speech_prob for s in segs])) if segs else 1.0
    return {"text": text, "lang": info.language, "lang_prob": float(info.language_probability),
            "avg_logprob": lp, "no_speech": nsp}


# --- agreement --------------------------------------------------------------------------------------------------

def normalize(text: str, lang: str | None) -> str:
    t = unicodedata.normalize("NFKC", text).lower()
    t = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in t)  # katakana → hiragana
    t = re.sub(r"[\s\W_]+", " " if lang == "en" else "", t, flags=re.UNICODE)
    return t.strip()


def _lev(a, b) -> int:
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def agreement(a: str, b: str, lang: str | None) -> float:
    """1 − error rate between the two transcripts: characters for Japanese/Chinese, words for other languages."""
    na, nb = normalize(a, lang), normalize(b, lang)
    if not na and not nb:
        return 0.0
    if lang in ("ja", "zh", "ko") or not lang:
        ua, ub = list(na.replace(" ", "")), list(nb.replace(" ", ""))
    else:
        ua, ub = na.split(), nb.split()
    if not ua:
        return 0.0
    return max(0.0, 1.0 - _lev(ua, ub) / max(len(ua), len(ub)))

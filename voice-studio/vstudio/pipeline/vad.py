"""Speech detection with Silero VAD v5 (ONNX, runs on CPU) and slicing into training-sized segments."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .. import assets

SR = 16000
WINDOW = 512
CONTEXT = 64


class SileroVAD:
    def __init__(self):
        import onnxruntime as ort
        opts = ort.SessionOptions()
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = 2
        self.sess = ort.InferenceSession(str(assets.fetch("silero_vad.onnx")), sess_options=opts,
                                         providers=["CPUExecutionProvider"])

    def probs(self, audio16k: np.ndarray) -> np.ndarray:
        """Speech probability for every 32 ms window."""
        state = np.zeros((2, 1, 128), dtype=np.float32)
        context = np.zeros((1, CONTEXT), dtype=np.float32)
        sr = np.array(SR, dtype=np.int64)
        n = len(audio16k) // WINDOW
        out = np.zeros(n, dtype=np.float32)
        x = audio16k.astype(np.float32)
        for i in range(n):
            chunk = x[i * WINDOW:(i + 1) * WINDOW][None, :]
            inp = np.concatenate([context, chunk], axis=1)
            p, state = self.sess.run(None, {"input": inp, "state": state, "sr": sr})
            context = inp[:, -CONTEXT:]
            out[i] = float(p[0][0])
        return out


@dataclass
class Region:
    start: float
    end: float

    @property
    def dur(self) -> float:
        return self.end - self.start


def speech_regions(probs: np.ndarray, threshold: float = 0.5, min_speech: float = 0.25,
                   min_silence: float = 0.3, pad: float = 0.08) -> list[Region]:
    step = WINDOW / SR
    regions, start, silence = [], None, 0
    neg = threshold - 0.15
    for i, p in enumerate(probs):
        t = i * step
        if start is None:
            if p >= threshold:
                start, silence = t, 0
        else:
            if p < neg:
                silence += 1
                if silence * step >= min_silence:
                    end = t - silence * step + step
                    if end - start >= min_speech:
                        regions.append(Region(max(0.0, start - pad), end + pad))
                    start, silence = None, 0
            else:
                silence = 0
    if start is not None:
        end = len(probs) * step
        if end - start >= min_speech:
            regions.append(Region(max(0.0, start - pad), end))
    return regions


def plan_segments(regions: list[Region], probs: np.ndarray, min_s: float = 2.0, max_s: float = 15.0,
                  target_s: float = 8.0, join_gap: float = 0.6) -> list[Region]:
    """Join short neighbouring regions up to the target length, and split long ones at their quietest point."""
    step = WINDOW / SR
    joined: list[Region] = []
    for r in regions:
        if joined and r.start - joined[-1].end <= join_gap and r.end - joined[-1].start <= target_s:
            joined[-1] = Region(joined[-1].start, r.end)
        else:
            joined.append(Region(r.start, r.end))

    def split(r: Region) -> list[Region]:
        if r.dur <= max_s:
            return [r]
        a, b = int((r.start + min_s) / step), int((r.end - min_s) / step)
        if b <= a:
            mid = (r.start + r.end) / 2
        else:
            window = probs[a:b]
            mid = (a + int(np.argmin(window))) * step
        return split(Region(r.start, mid)) + split(Region(mid, r.end))

    out = []
    for r in joined:
        out.extend(split(r))
    return [r for r in out if r.dur >= min_s]

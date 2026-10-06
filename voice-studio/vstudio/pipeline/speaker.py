"""Speaker identification: who is speaking in each segment.

Embeddings come from WeSpeaker's ResNet34-LM (VoxCeleb, CC-BY-4.0, ONNX, CPU). Two ways to assign segments:
- enrollment: each voice has 1–5 short reference clips; a segment goes to the most similar voice when the cosine
  similarity clears the threshold (recordings of "me and others" sort themselves out);
- clustering: segments of one recording are grouped, and the user names each group by listening to a sample.
A segment similar to two voices at once is flagged as possible overlap.
"""
from __future__ import annotations

import numpy as np

from .. import assets

SR = 16000
assets.ASSETS["wespeaker_resnet34_LM.onnx"] = (
    "https://huggingface.co/Wespeaker/wespeaker-voxceleb-resnet34-LM/resolve/main/voxceleb_resnet34_LM.onnx")


def kaldi_fbank(x: np.ndarray, sr: int = SR, n_mels: int = 80) -> np.ndarray:
    """Kaldi-compatible log-mel filterbank (torchaudio.compliance.kaldi.fbank with WeSpeaker's settings:
    25 ms Hamming frames, 10 ms shift, dither 0, pre-emphasis 0.97, DC removal, power spectrum, 20 Hz–Nyquist)."""
    x = x.astype(np.float64) * 32768.0
    win, hop, nfft = int(0.025 * sr), int(0.010 * sr), 512
    if len(x) < win:
        x = np.pad(x, (0, win - len(x)))
    n = 1 + (len(x) - win) // hop
    idx = np.arange(win)[None, :] + hop * np.arange(n)[:, None]
    frames = x[idx]
    frames = frames - frames.mean(axis=1, keepdims=True)
    frames = np.concatenate([frames[:, :1] * (1 - 0.97), frames[:, 1:] - 0.97 * frames[:, :-1]], axis=1)
    frames = frames * (0.54 - 0.46 * np.cos(2 * np.pi * np.arange(win) / (win - 1)))
    spec = np.abs(np.fft.rfft(frames, n=nfft)) ** 2  # (n, 257)
    mel = lambda f: 1127.0 * np.log(1.0 + f / 700.0)
    lo, hi = mel(20.0), mel(sr / 2)
    centers = np.linspace(lo, hi, n_mels + 2)
    fft_mel = mel(np.arange(nfft // 2) * sr / nfft)
    bank = np.zeros((n_mels, nfft // 2 + 1))
    for m in range(n_mels):
        left, center, right = centers[m], centers[m + 1], centers[m + 2]
        up = (fft_mel - left) / (center - left)
        down = (right - fft_mel) / (right - center)
        bank[m, : nfft // 2] = np.maximum(0.0, np.minimum(up, down))
    feats = np.log(np.maximum(spec @ bank.T, np.finfo(np.float32).eps))
    return feats.astype(np.float32)


class Embedder:
    def __init__(self):
        import onnxruntime as ort
        self.sess = ort.InferenceSession(str(assets.fetch("wespeaker_resnet34_LM.onnx")),
                                         providers=["CPUExecutionProvider"])

    def embed(self, audio16k: np.ndarray) -> np.ndarray:
        f = kaldi_fbank(audio16k)
        f = f - f.mean(axis=0, keepdims=True)  # cepstral mean normalization, as WeSpeaker does
        e = self.sess.run(None, {"feats": f[None, :, :]})[0][0]
        return e / (np.linalg.norm(e) + 1e-9)


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / ((np.linalg.norm(a) * np.linalg.norm(b)) + 1e-9))


def assign(emb: np.ndarray, centroids: dict[str, np.ndarray], threshold: float) -> tuple[str | None, float, bool]:
    """Best matching voice, its similarity, and whether a second voice is nearly as close (possible overlap)."""
    if not centroids:
        return None, 0.0, False
    scored = sorted(((cosine(emb, c), vid) for vid, c in centroids.items()), reverse=True)
    best, vid = scored[0]
    ambiguous = len(scored) > 1 and scored[1][0] >= threshold and best - scored[1][0] < 0.08
    return (vid if best >= threshold else None), best, ambiguous


def cluster(embs: np.ndarray, threshold: float = 0.6, max_clusters: int = 12) -> np.ndarray:
    """Agglomerative clustering on cosine distance; segments of the same person end up with the same label."""
    if len(embs) == 0:
        return np.zeros(0, dtype=int)
    if len(embs) == 1:
        return np.zeros(1, dtype=int)
    from scipy.cluster.hierarchy import fcluster, linkage
    z = linkage(embs, method="average", metric="cosine")
    labels = fcluster(z, t=1 - threshold, criterion="distance")
    if labels.max() > max_clusters:
        labels = fcluster(z, t=max_clusters, criterion="maxclust")
    # relabel by size, largest first
    order = {lab: i for i, (lab, _) in enumerate(sorted(
        ((l, int((labels == l).sum())) for l in set(labels)), key=lambda t: -t[1]))}
    return np.array([order[l] for l in labels], dtype=int)

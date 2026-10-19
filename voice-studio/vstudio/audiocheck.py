"""Check a recording before importing it: is the sound itself good enough to train a voice on?

Only the sound is judged here (who is speaking, what is said and how are checked after import): background sounds,
steady noise and hum, echo, distortion, level, bandwidth, dropouts and traces of noise gates. Each check passes,
warns ("usable, not ideal") or fails, with the times where the problem is so it can be heard.

How background sounds are found: Silero VAD marks where the person speaks; the pauses between phrases are where the
background can be heard on its own. Each half second of pause is measured: how loud it is next to the voice, whether
it is steady like a fan or hiss (flat spectrum, even level), a hum at 50/60 Hz, speech-like (someone else, a video),
or changing and tonal like music and game sounds. Music that stops exactly when the person speaks is rare, so the
pauses catch nearly all of it. The optional deep check separates the voice with BS-RoFormer and measures what is
left under the speech itself.

Long recordings (over 20 minutes) are sampled: 20 windows of 60 s spread evenly over the file.
"""
from __future__ import annotations

import math
import re
import shutil
import tempfile
from pathlib import Path

import numpy as np

from . import audio, config, db, jobs

FULL_LIMIT = 1200.0           # analyse files up to 20 minutes completely
WINDOWS, WINDOW_S = 20, 60.0  # longer files: 20 windows of 60 s
BLOCK = 0.5                   # pause content is judged in half-second blocks

# Pass / warn limits. Levels are dB relative to the voice (the loud end of its phrases) unless noted.
LIMITS = {
    "snr_pass": 25.0, "snr_warn": 18.0,            # voice above the steady background (auto-review approves at 18)
    "bg_loud": -30.0, "bg_audible": -42.0,         # music/other sounds this loud next to the voice
    "bg_fail_share": 0.05, "bg_warn_share": 0.02,  # share of pause time with them
    "hum_warn": -40.0, "hum_fail": -30.0,
    "rt_pass": 0.35, "rt_warn": 0.6,               # echo: seconds for the sound to die away by 60 dB
    "clip_warn": 1e-4, "clip_fail": 1e-3,          # share of speech samples clipped (auto-review flags 0.1%)
    "level_pass": -35.0, "level_fail": -45.0,      # dBFS of the voice
    "band_pass": 13000.0, "band_fail": 7000.0,     # highest frequency with real content, Hz
    "under_pass": -30.0, "under_warn": -20.0,      # deep check: what separation leaves under the speech
}
ORDER = {"pass": 0, "info": 0, "unknown": 1, "warn": 2, "fail": 3}


# --- reading ---------------------------------------------------------------------------------------------------------

def probe(path: Path) -> dict:
    """Duration, codec, sample rate, channels and bitrate from ffmpeg's header (no ffprobe needed)."""
    r = audio._run([audio.ffmpeg(), "-hide_banner", "-i", str(path)])
    out: dict = {"duration": audio.probe_duration(path)}
    m = re.search(r"Audio:\s*([\w\-]+)[^\n]*?(\d+)\s*Hz,\s*([^,\n]+)", r.stderr)
    if m:
        out.update(codec=m.group(1), sr=int(m.group(2)), channels_text=m.group(3).strip())
        ch = m.group(3).strip()
        out["channels"] = 1 if ch == "mono" else 2 if ch == "stereo" else int(re.match(r"(\d+)", ch).group(1)) \
            if re.match(r"\d+", ch) else 2
    b = re.search(r"Audio:[^\n]*?(\d+)\s*kb/s", r.stderr)
    if b:
        out["kbps"] = int(b.group(1))
    return out


def plan_windows(duration: float) -> list[tuple[float, float]]:
    if duration <= FULL_LIMIT:
        return [(0.0, duration)]
    starts = np.linspace(0, duration - WINDOW_S, WINDOWS)
    return [(float(s), WINDOW_S) for s in starts]


def _decode(path: Path, start: float, dur: float, sr: int, channels: int = 1) -> np.ndarray:
    with tempfile.TemporaryDirectory() as d:
        dst = Path(d) / "w.wav"
        cmd = [audio.ffmpeg(), "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{start:.3f}", "-i", str(path),
               "-t", f"{dur:.3f}", "-vn", "-ac", str(channels), "-ar", str(sr), "-c:a", "pcm_f32le", str(dst)]
        r = audio._run(cmd)
        if r.returncode != 0 or not dst.exists():
            raise RuntimeError(f"讀不到聲音：{r.stderr[-300:]}")
        import soundfile as sf
        y, _ = sf.read(str(dst), dtype="float32", always_2d=channels > 1)
        return y


# --- measurements ----------------------------------------------------------------------------------------------------

def frames_db(x: np.ndarray, sr: int, win: float = 0.02, hop: float = 0.01) -> np.ndarray:
    n, h = max(1, int(sr * win)), max(1, int(sr * hop))
    if len(x) < n:
        return np.full(1, 10 * np.log10(np.mean(x ** 2) + 1e-12))
    k = (len(x) - n) // h + 1
    idx = np.arange(n)[None, :] + h * np.arange(k)[:, None]
    return 10 * np.log10(np.mean(x[idx] ** 2, axis=1) + 1e-12)


def block_features(x: np.ndarray, sr: int) -> dict:
    """What half a second of pause sounds like: level, how steady, how tonal, how much 50/60 Hz hum."""
    nfft = 1 << int(math.ceil(math.log2(sr * 0.04)))
    hop = nfft // 2
    k = max(1, (len(x) - nfft) // hop + 1)
    idx = np.arange(nfft)[None, :] + hop * np.arange(k)[:, None]
    seg = x[idx] if len(x) >= nfft else np.pad(x, (0, nfft - len(x)))[None, :]
    spec = np.abs(np.fft.rfft(seg * np.hanning(nfft), axis=1)) ** 2
    freqs = np.fft.rfftfreq(nfft, 1 / sr)
    band = (freqs >= 100) & (freqs <= min(8000, sr / 2 - 1))
    p = spec[:, band] + 1e-20
    # flatness of the frames that carry the sound (a short jingle in a quiet half second still counts)
    e = p.sum(axis=1)
    loud = e >= e.max() * 0.1
    flat = float(np.median((np.exp(np.mean(np.log(p), axis=1)) / np.mean(p, axis=1))[loud]))
    fdb = frames_db(x, sr)
    return {"db": float(10 * np.log10(np.mean(x ** 2) + 1e-12)), "std": float(np.std(fdb)), "flat": flat,
            "hum": hum_score(x, sr)}


def hum_score(x: np.ndarray, sr: int) -> float:
    """Share of the first 8 harmonics of 50 or 60 Hz that stand 10 dB above their neighbourhood (mains hum).
    Needs a long FFT: at 3 Hz resolution a fan's rumble does not look like hum."""
    nfft = 1 << int(math.ceil(math.log2(max(len(x), int(0.3 * sr)))))
    p = np.abs(np.fft.rfft(x * np.hanning(len(x)), nfft)) ** 2 + 1e-20
    df = sr / nfft
    best = 0
    for base in (50.0, 60.0):
        n = 0
        for k in range(1, 9):
            f = base * k
            c = int(round(f / df))
            w2, w15 = max(1, int(2 / df)), max(3, int(15 / df))
            peak = p[max(0, c - w2): c + w2 + 1].max()
            ring = np.concatenate([p[max(0, c - w15): max(0, c - 2 * w2)], p[c + 2 * w2 + 1: c + w15 + 1]])
            if len(ring) and peak > 10 * np.median(ring):
                n += 1
        best = max(best, n)
    return best / 8


def classify_block(f: dict, rel: float, vad_p: float) -> str:
    """One half second of pause: quiet / voice (someone else, a video) / hum / music (tonal: notes, jingles, most
    game sounds) / transient (knocks, clicks, breaths: noisy and uneven) / noise (steady hiss, fan)."""
    if rel < -50:
        return "quiet"
    if vad_p >= 0.35:
        return "voice"
    if f["hum"] >= 0.375 and f["std"] < 3:
        return "hum"
    if f["flat"] < 0.05:
        return "music"
    if f["std"] >= 4.0:
        return "transient"
    return "noise"


def decay_time(fdb: np.ndarray, hop: float, t_end: float, gap: float, noise: float) -> float | None:
    """Echo estimate at the end of a phrase: how fast the level falls after the last loud moment, scaled to 60 dB."""
    a, b = int((t_end - 0.35) / hop), int((t_end + min(gap, 0.8) - 0.05) / hop)
    if a < 0 or b > len(fdb) or b - a < 10:
        return None
    seg = fdb[a:b]
    pk = int(np.argmax(seg[: int(0.35 / hop) + 1]))
    top = seg[pk]
    span = 20.0 if top - noise >= 30 else 15.0 if top - noise >= 24 else 0.0
    if not span:
        return None
    after = seg[pk:]
    i5 = np.argmax(after <= top - 5) if (after <= top - 5).any() else None
    ie = np.argmax(after <= top - 5 - span) if (after <= top - 5 - span).any() else None
    if i5 is None or ie is None or ie <= i5:
        return None
    return float((ie - i5) * hop * 60.0 / span)


def ltas(x: np.ndarray, sr: int, mask: np.ndarray, hop: float = 0.01) -> tuple[np.ndarray, np.ndarray]:
    """Average power spectrum of the speech frames."""
    nfft = 2048 if sr > 24000 else 1024
    h = int(sr * hop)
    starts = np.nonzero(mask)[0] * h
    starts = starts[starts + nfft <= len(x)][:: max(1, len(starts) // 600)]
    if not len(starts):
        return np.zeros(nfft // 2 + 1), np.fft.rfftfreq(nfft, 1 / sr)
    seg = x[starts[:, None] + np.arange(nfft)[None, :]]
    spec = (np.abs(np.fft.rfft(seg * np.hanning(nfft), axis=1)) ** 2).sum(axis=0)
    return spec, np.fft.rfftfreq(nfft, 1 / sr)


def cutoff(spec: np.ndarray, freqs: np.ndarray) -> float | None:
    """Highest frequency that still carries sound. Lossy codecs and low sample rates leave a cliff: above it the
    spectrum drops to a floor (digital silence or rounding noise). Measured in 500 Hz bands so single spikes do not
    count; a recording with sound (or hiss) right up to the top of its range counts as full band."""
    if spec.sum() <= 0:
        return None
    db = 10 * np.log10(spec / spec.sum() + 1e-30)
    ref = float(np.median(db[(freqs >= 300) & (freqs <= 3000)]))
    edges = np.arange(1000, freqs[-1] + 1, 500)
    bands = [(hi, float(np.median(db[(freqs >= lo) & (freqs < hi)]))) for lo, hi in zip(edges, edges[1:])
             if ((freqs >= lo) & (freqs < hi)).any()]
    if len(bands) < 4:
        return float(freqs[-1])
    vals = np.array([v for _, v in bands])
    # a cliff: 30 dB or more down within 1.5 kHz, with nothing above it coming back
    # (natural speech fades far more gently; codecs and resamplers cut like this)
    for k in range(len(vals) - 2, -1, -1):
        rest = vals[min(k + 3, len(vals) - 1):]
        if vals[k] - rest.max() >= 30:
            return float(bands[k][0])
    floor = float(np.median(vals[-3:]))
    if floor > ref - 60:  # sound (or hiss) right up to the top of the range
        return float(freqs[-1])
    above = [hi for hi, v in bands if v > floor + 12]
    return float(above[-1]) if above else 1000.0


def runs(mask: np.ndarray, min_len: int) -> list[tuple[int, int]]:
    """(start, end) index pairs of True runs at least min_len long."""
    if not mask.any():
        return []
    d = np.diff(np.concatenate([[0], mask.astype(np.int8), [0]]))
    s, e = np.nonzero(d == 1)[0], np.nonzero(d == -1)[0]
    return [(int(a), int(b)) for a, b in zip(s, e) if b - a >= min_len]


def merge(times: list[tuple[float, float]], gap: float = 0.6) -> list[tuple[float, float]]:
    out: list[list[float]] = []
    for a, b in sorted(times):
        if out and a - out[-1][1] <= gap:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return [(round(a, 2), round(b, 2)) for a, b in out]


# --- one window --------------------------------------------------------------------------------------------------------

def analyse_window(x: np.ndarray, sr: int, t0: float, vad_model) -> dict:
    from .pipeline import vad
    x16 = audio.resample(x, sr, 16000)
    probs = vad_model.probs(x16) if len(x16) >= vad.WINDOW else np.zeros(0)
    regions = [(r.start, r.end) for r in vad.speech_regions(probs)] if len(probs) else []
    hop = 0.01
    fdb = frames_db(x, sr, 0.02, hop)
    t = np.arange(len(fdb)) * hop + 0.01
    speech = np.zeros(len(fdb), dtype=bool)
    for a, b in regions:
        speech[(t >= a) & (t < b)] = True
    # pauses: between phrases (and before/after them), 0.2 s away from speech so breaths and tails stay out
    bounds = [(-1e9, -1e9)] + regions + [(len(x) / sr + 1e9, len(x) / sr + 1e9)]
    gaps = []
    for (a0, b0), (a1, b1) in zip(bounds, bounds[1:]):
        s = max(0.1, b0 + 0.2)
        e = min(len(x) / sr - 0.1, a1 - 0.2)
        if e - s >= BLOCK:
            gaps.append((s, e, b0 > 0 and a1 < len(x) / sr))
    gap = np.zeros(len(fdb), dtype=bool)
    for s, e, _ in gaps:
        gap[(t >= s) & (t < e)] = True

    blocks = []
    step = len(probs) and 512 / 16000
    for s, e, _ in gaps:
        for b0 in np.arange(s, e - BLOCK + 1e-6, BLOCK):
            seg = x[int(b0 * sr): int((b0 + BLOCK) * sr)]
            f = block_features(seg, sr)
            vp = float(np.mean(probs[int(b0 / step): int((b0 + BLOCK) / step) + 1])) if step else 0.0
            blocks.append({"t": round(t0 + b0, 2), **f, "vad": vp})

    # clipping: samples at full scale, or flat tops at the file's own peak (clipped, then turned down)
    ax = np.abs(x)
    m = float(ax.max()) if len(ax) else 0.0
    hard = ax >= 0.995
    flat = np.zeros_like(hard)
    if m >= 0.25:
        for a, b in runs(ax >= m * 0.999, 3):
            flat[a:b] = True
    clipped = hard | flat
    clip_times = merge([(t0 + a / sr, t0 + b / sr) for a, b in runs(clipped, 1)], 0.2)

    # exact digital silence of 5 ms or more inside a phrase: a dropout when the voice is loud right before and
    # after it (the sound was cut), a noise gate when it falls in a quiet gap between words
    drops, gate_runs = [], 0
    zero = ax < 1e-7
    loud_ref = float(np.percentile(fdb[speech], 90)) if speech.any() else 0.0
    w10 = int(0.01 * sr)
    for a, b in regions:
        ia, ib = int((a + 0.05) * sr), int((b - 0.05) * sr)
        if ib <= ia:
            continue
        for s0, e0 in runs(zero[ia:ib], int(0.005 * sr)):
            s0, e0 = ia + s0, ia + e0
            before = 10 * np.log10(np.mean(x[max(0, s0 - w10): s0] ** 2) + 1e-12)
            after = 10 * np.log10(np.mean(x[e0: e0 + w10] ** 2) + 1e-12)
            if min(before, after) >= loud_ref - 25:
                drops.append((t0 + s0 / sr, t0 + e0 / sr))
            else:
                gate_runs += 1

    # echo at phrase ends followed by a real pause
    noise_local = float(np.median(fdb[gap])) if gap.any() else float(np.percentile(fdb, 10))
    rts = []
    for (a, b), nxt in zip(regions, regions[1:] + [(len(x) / sr, 0)]):
        g = nxt[0] - b
        if g >= 0.35:
            rt = decay_time(fdb, hop, b, g, noise_local)
            if rt is not None:
                rts.append(rt)

    spec, freqs = ltas(x, sr, speech)
    speech_samples = int(speech.sum() * hop * sr)
    return {"t0": t0, "dur": len(x) / sr, "fdb": fdb, "speech": speech, "gap": gap, "blocks": blocks,
            "regions": [(t0 + a, t0 + b) for a, b in regions], "clip_samples": int(clipped.sum()),
            "clip_times": clip_times, "drops": merge(drops, 0.2), "gate_runs": gate_runs, "rts": rts,
            "spec": spec, "freqs": freqs,
            "speech_samples": speech_samples}


# --- the whole file ----------------------------------------------------------------------------------------------------

def _check(key: str, label: str, level: str, value: str, detail: str, ranges=None) -> dict:
    return {"key": key, "label": label, "level": level, "value": value, "detail": detail,
            "ranges": [list(r) for r in (ranges or [])][:12]}


def analyse(path: Path, deep: bool = False, progress=None) -> dict:
    from .pipeline import vad
    info = probe(path)
    dur = info.get("duration") or 0.0
    if not info.get("sr") or dur <= 0:
        raise ValueError("這個檔案裡沒有聲音，或格式讀不懂。")
    sr = min(int(info["sr"]), 48000)
    model = vad.SileroVAD()
    parts = []
    plan = plan_windows(dur)
    for i, (s, d) in enumerate(plan):
        if progress:
            progress(i / (len(plan) + (2 if deep else 0)), f"分析第 {i + 1}/{len(plan)} 段")
        x = _decode(path, s, d, sr)
        if len(x):
            parts.append(analyse_window(x, sr, s, model))
    if not parts:
        raise ValueError("讀不到聲音。")
    result = summarise(parts, info, sr, dur)
    if deep:
        if progress:
            progress(len(plan) / (len(plan) + 2), "人聲分離（深入檢查）")
        result["checks"].append(deep_check(path, plan, sr, parts))
        result["verdict"] = verdict(result["checks"])
    return result


def summarise(parts: list[dict], info: dict, sr: int, dur: float) -> dict:
    fdb = np.concatenate([p["fdb"] for p in parts])
    speech = np.concatenate([p["speech"] for p in parts])
    gap = np.concatenate([p["gap"] for p in parts])
    analysed = sum(p["dur"] for p in parts)
    speech_s = float(speech.sum() * 0.01)
    checks = []

    if speech_s < 2 or speech_s < 0.05 * analysed:
        checks.append(_check("speech", "有沒有說話", "fail", f"說話 {speech_s:.0f} 秒",
                             "幾乎沒有偵測到說話，其他項目無法判斷。"))
        return {"verdict": "fail", "checks": checks, "info": _info(info, sr, dur, analysed, speech_s, 0.0, parts),
                "timeline": _timeline(parts, [])}

    ref = float(np.percentile(fdb[speech], 90))           # the loud end of the voice
    active = speech & (fdb > ref - 30)
    level = float(np.median(fdb[active]))
    gap_s = float(gap.sum() * 0.01)
    noise = float(np.median(fdb[gap])) if gap_s >= 2 else float(np.percentile(fdb, 10))
    snr = ref - noise

    blocks = [b for p in parts for b in p["blocks"]]
    for b in blocks:
        b["rel"] = b["db"] - ref
        b["kind"] = classify_block(b, b["rel"], b["vad"])
    block_s = len(blocks) * BLOCK

    # 1. background sounds: music, game sounds, other voices
    flagged = [b for b in blocks if b["kind"] in ("music", "voice") and b["rel"] >= LIMITS["bg_audible"]]
    loud = [b for b in flagged if b["rel"] >= LIMITS["bg_loud"]]
    ranges = merge([(b["t"], b["t"] + BLOCK) for b in flagged])
    if block_s < 3:
        bg = _check("background", "背景音（音樂、音效、別人說話）", "warn", "沒有停頓可以聽",
                    "這段錄音幾乎一直在說話，聽不到背景，所以沒辦法確認。勾「深入檢查」用人聲分離再檢查一次。")
    else:
        share, loud_share = len(flagged) * BLOCK / block_s, len(loud) * BLOCK / block_s
        voices = sum(1 for b in flagged if b["kind"] == "voice")
        what = "別人說話或影片人聲" if voices > len(flagged) / 2 else "音樂或音效"
        rel = float(np.median([b["rel"] for b in flagged])) if flagged else None
        if loud_share >= LIMITS["bg_fail_share"] and len(loud) * BLOCK >= 2:
            lvl = "fail"
        elif share >= LIMITS["bg_warn_share"] and flagged:
            lvl = "warn"
        else:
            lvl = "pass"
        if lvl == "pass":
            value, detail = "沒有聽到", "停頓的時候沒有音樂、音效或別人的聲音。"
            if flagged:
                detail += f"只有零星 {len(flagged) * BLOCK:.1f} 秒有一點聲音，可以聽一下下面的位置。"
        else:
            value = f"停頓中 {share:.0%} 的時間有{what}，比你的聲音小 {abs(rel):.0f} dB"
            detail = ("背景聲會被當成你聲音的一部分學進去。" +
                      ("聲音不小，" if lvl == "fail" else "聲音不大，但") +
                      "建議換一段乾淨的；真的要用，匯入時勾「去除背景音樂」。")
        bg = _check("background", "背景音（音樂、音效、別人說話）", lvl, value, detail, ranges)
    checks.append(bg)

    # 2. steady noise and hum
    hum = [b for b in blocks if b["kind"] == "hum" and b["rel"] >= LIMITS["hum_warn"]]
    hum_rel = float(np.median([b["rel"] for b in hum])) if hum else None
    lvl = "pass" if snr >= LIMITS["snr_pass"] else "warn" if snr >= LIMITS["snr_warn"] else "fail"
    notes = []
    if hum and len(hum) * BLOCK >= max(1.0, 0.2 * block_s):
        hl = "fail" if hum_rel >= LIMITS["hum_fail"] else "warn"
        lvl = max(lvl, hl, key=lambda v: ORDER[v])
        notes.append(f"有電源的嗡嗡聲（50／60 Hz），比你的聲音小 {abs(hum_rel):.0f} dB")
    detail = {"pass": "背景很安靜。", "warn": "可以用，但不理想：雜音會被學進去一點，合成出來可能帶一點沙沙聲。",
              "fail": "雜音太大。平台自動審核會把大部分句子判成雜音偏多。"}[lvl]
    if gap_s < 2:
        detail += "（停頓很少，雜音是用最安靜的片刻估的。）"
    checks.append(_check("noise", "雜音（底噪、風扇、嗡嗡聲）", lvl,
                         f"人聲比背景大 {snr:.0f} dB" + ("；" + "；".join(notes) if notes else ""),
                         detail + f" 標準：25 dB 以上通過，18–25 dB 勉強可用。",
                         merge([(b["t"], b["t"] + BLOCK) for b in hum]) if notes else None))

    # 3. echo
    rts = [r for p in parts for r in p["rts"]]
    if len(rts) >= 3:
        rt = float(np.median(rts))
        lvl = "pass" if rt <= LIMITS["rt_pass"] else "warn" if rt <= LIMITS["rt_warn"] else "fail"
        checks.append(_check("echo", "回音", lvl, f"殘響約 {rt:.2f} 秒",
                             {"pass": "收音很乾，幾乎沒有回音。",
                              "warn": "有一點房間的回音，合成出來會帶一點空間感。",
                              "fail": "回音明顯，模型會把回音學成你的音色，合成出來像在空房間裡說話。"}[lvl]
                             + " 標準：0.35 秒以下通過，0.6 秒以下勉強可用。"))
    else:
        checks.append(_check("echo", "回音", "unknown", "無法判斷",
                             "句尾之後的停頓太少或雜音太大，量不出回音。"))

    # 4. clipping
    speech_samples = max(1, sum(p["speech_samples"] for p in parts))
    clip = sum(p["clip_samples"] for p in parts) / speech_samples
    ct = [r for p in parts for r in p["clip_times"]]
    lvl = "pass" if clip < LIMITS["clip_warn"] else "warn" if clip < LIMITS["clip_fail"] else "fail"
    checks.append(_check("clipping", "破音（爆音）", lvl,
                         "沒有" if not ct else f"{len(ct)} 處，佔說話時間 {clip:.3%}",
                         {"pass": "沒有破音。" if not ct else "只有極少數幾個取樣碰頂，影響不大。",
                          "warn": "有幾處破音，平台會把那些句子標記出來，檢查時排除就好。",
                          "fail": "破音很多。破音是刺耳的失真，會被模型學走；請換一段音量沒有碰頂的錄音。"}[lvl], ct))

    # 5. level
    lvl = "pass" if level >= LIMITS["level_pass"] else "warn" if level >= LIMITS["level_fail"] else "fail"
    checks.append(_check("level", "音量", lvl, f"說話時約 {level:.0f} dBFS",
                         {"pass": "音量合適。", "warn": "偏小聲，雜音比例會變高；可以用，但不要事後放大很多。",
                          "fail": "太小聲。放大會連雜音一起放大，請換一段錄音。"}[lvl]))

    # 6. bandwidth (lossy codecs and low sample rates cut the highs)
    spec = sum(p["spec"] for p in parts)
    co = cutoff(spec, parts[0]["freqs"])
    if co is None:
        checks.append(_check("band", "音質（頻寬）", "unknown", "無法判斷", ""))
    else:
        lvl = "pass" if co >= LIMITS["band_pass"] else "warn" if co >= LIMITS["band_fail"] else "fail"
        checks.append(_check("band", "音質（頻寬）", lvl, f"聲音到約 {co / 1000:.1f} kHz",
                             {"pass": "高音完整。",
                              "warn": "高音被切掉了（壓縮得很重或取樣率偏低），合成出來會比較悶。",
                              "fail": "像電話的音質，高音幾乎都沒了，不適合訓練。"}[lvl]
                             + " 標準：13 kHz 以上通過，7 kHz 以上勉強可用。"))

    # 7. traces of noise gates / denoising: pauses (or gaps between words) of exact digital silence
    silent = float(np.mean(fdb[gap] < -90)) if gap_s >= 2 else 0.0
    gates = sum(p["gate_runs"] for p in parts)
    if silent >= 0.5 or gates >= max(5, speech_s / 12):
        what = f"停頓中 {silent:.0%} 完全無聲" if silent >= 0.5 else f"字和字之間 {gates} 處突然完全無聲"
        checks.append(_check("processed", "後製痕跡", "warn", what,
                             "數位的完全無聲，通常是用過降噪或噪音閘門（例如 OBS 的噪音閘）。處理過的聲音會改變音色、"
                             "字尾會被切掉；有原檔的話用原檔。"))
    else:
        checks.append(_check("processed", "後製痕跡", "pass", "沒有明顯痕跡",
                             "停頓裡有自然的底噪，看起來沒有用過噪音閘門。（不是所有處理都看得出來。）"))

    # 8. dropouts
    drops = [r for p in parts for r in p["drops"]]
    lvl = "pass" if not drops else "warn" if len(drops) < 3 else "fail"
    checks.append(_check("dropouts", "斷訊", lvl, "沒有" if not drops else f"{len(drops)} 處",
                         "說話中間沒有突然無聲。" if not drops else "說話中間有突然完全無聲的地方（斷訊或剪接），那些句子要排除。",
                         drops))
    return {"verdict": verdict(checks), "checks": checks,
            "info": _info(info, sr, dur, analysed, speech_s, snr, parts, level=level, ref=ref, noise=noise),
            "timeline": _timeline(parts, flagged)}


def verdict(checks: list[dict]) -> str:
    worst = max((ORDER[c["level"]] for c in checks), default=0)
    return "fail" if worst >= 3 else "warn" if worst >= 2 else "pass"


def _info(info: dict, sr: int, dur: float, analysed: float, speech_s: float, snr: float, parts, **kw) -> dict:
    return {"codec": info.get("codec"), "sr": info.get("sr"), "channels": info.get("channels"), "kbps": info.get("kbps"),
            "duration": round(dur, 2), "analysed": round(analysed, 1), "sampled": len(parts) > 1,
            "speech_seconds": round(speech_s, 1), "snr": round(snr, 1),
            **{k: round(v, 1) for k, v in kw.items() if v is not None}}


def _timeline(parts: list[dict], flagged: list[dict]) -> dict:
    return {"windows": [[round(p["t0"], 2), round(p["t0"] + p["dur"], 2)] for p in parts],
            "speech": [[round(a, 2), round(b, 2)] for p in parts for a, b in p["regions"]][:4000],
            "background": [list(r) for r in merge([(b["t"], b["t"] + BLOCK) for b in flagged])][:2000],
            "clipping": [list(r) for p in parts for r in p["clip_times"]][:500]}


# --- deep check: separate the voice and measure what is left under it ---------------------------------------------------

def under_speech(mix: np.ndarray, voice: np.ndarray, sr: int, speech: np.ndarray, t0: float) -> tuple[list, list]:
    """Per speech frame: background left after separation, dB relative to the voice."""
    n = min(len(mix), len(voice))
    rest = mix[:n] - voice[:n]
    vdb, rdb = frames_db(voice[:n], sr), frames_db(rest, sr)
    k = min(len(vdb), len(rdb), len(speech))
    sel = speech[:k] & (vdb[:k] > np.percentile(vdb[:k], 90) - 30) if speech[:k].any() else speech[:k]
    rel = (rdb[:k] - vdb[:k])[sel]
    times = (np.nonzero(sel)[0] * 0.01 + t0)
    return list(rel), list(times)


def deep_check(path: Path, plan, sr: int, parts: list[dict]) -> dict:
    from .pipeline import separate
    rels, times = [], []
    try:
        with tempfile.TemporaryDirectory() as d:
            for (s, dur), p in zip(plan, parts):
                x = _decode(path, s, dur, sr)
                src = Path(d) / f"w{int(s)}.wav"
                audio.save(src, x, sr)
                voc = separate.vocals(src, Path(d) / "sep")
                v, _ = audio.load(voc, sr)
                r, t = under_speech(x, v, sr, p["speech"], s)
                rels += r
                times += t
                shutil.rmtree(Path(d) / "sep", ignore_errors=True)
    except ImportError:
        return _check("under", "說話時底下的背景（深入）", "unknown", "沒有安裝人聲分離",
                      "需要人聲分離模組（install.bat 會安裝）。")
    except Exception as e:
        return _check("under", "說話時底下的背景（深入）", "unknown", "沒有完成", str(e)[:200])
    if not rels:
        return _check("under", "說話時底下的背景（深入）", "unknown", "無法判斷", "")
    rel = float(np.median(rels))
    lvl = "pass" if rel <= LIMITS["under_pass"] else "warn" if rel <= LIMITS["under_warn"] else "fail"
    loud = [tt for rr, tt in zip(rels, times) if rr > LIMITS["under_warn"]]
    return _check("under", "說話時底下的背景（深入）", lvl, f"分離後剩下的背景比人聲小 {abs(rel):.0f} dB",
                  {"pass": "說話時底下也很乾淨。",
                   "warn": "說話時底下有一點背景聲。",
                   "fail": "說話時底下有明顯的背景聲（音樂或音效）。"}[lvl]
                  + " 標準：小 30 dB 以上通過，20 dB 以上勉強可用。（人聲分離本身會留下一點點，這個數字是參考。）",
                  merge([(tt, tt + 0.01) for tt in loud], 0.5))


# --- the job: check every queued recording of a batch ------------------------------------------------------------------

def folder(batch: str) -> Path:
    return config.DATA / "checks" / batch


@jobs.handler("audio_check", queue="check")
def audio_check(ctx: jobs.JobContext) -> dict:
    """Checks the recordings of a batch one by one, including ones added while it runs."""
    batch, deep = ctx.params["batch"], bool(ctx.params.get("deep"))
    if deep:
        from . import tts
        tts.unload()  # the separator needs the GPU
    done = 0
    while True:
        rows = db.query("SELECT * FROM audio_checks WHERE batch=? AND status='queued' ORDER BY created_at LIMIT 1",
                        (batch,))
        if not rows:
            break
        item = rows[0]
        total = done + len(db.query("SELECT id FROM audio_checks WHERE batch=? AND status='queued'", (batch,)))
        db.update("audio_checks", item["id"], {"status": "running"})

        def progress(f: float, msg: str, _d=done, _t=total, _n=item["filename"]) -> None:
            ctx.progress((_d + f) / max(1, _t), f"{_n}：{msg}")
        try:
            if deep:
                with jobs.GPU_LOCK:
                    res = analyse(Path(item["path"]), deep=True, progress=progress)
            else:
                res = analyse(Path(item["path"]), progress=progress)
            db.update("audio_checks", item["id"], {"status": "done", "verdict": res["verdict"], "result": res,
                                                   "duration": res["info"]["duration"]})
        except jobs.Cancelled:
            db.update("audio_checks", item["id"], {"status": "queued"})
            raise
        except Exception as e:
            ctx.log(f"{item['filename']}: {e}")
            db.update("audio_checks", item["id"], {"status": "failed", "result": {"error": str(e)[:300]}})
        done += 1
    counts = {v: n for v, n in db.connect().execute(
        "SELECT verdict, COUNT(*) FROM audio_checks WHERE batch=? AND status='done' GROUP BY verdict", (batch,))}
    return {"message": f"檢查完成：通過 {counts.get('pass', 0)}、勉強可用 {counts.get('warn', 0)}、"
                       f"不通過 {counts.get('fail', 0)}"}


def criteria() -> list[dict]:
    """The pass / warn limits, as shown on the check page."""
    L = LIMITS
    return [
        {"label": "背景音（音樂、音效、別人說話）",
         "pass": "停頓的時候聽不到（比人聲小 42 dB 以上，或只有零星一點）",
         "warn": f"停頓中有 {L['bg_warn_share']:.0%} 以上的時間聽得到",
         "fail": f"停頓中有 {L['bg_fail_share']:.0%} 以上的時間有、而且只比人聲小不到 30 dB"},
        {"label": "雜音（底噪、風扇、嗡嗡聲）", "pass": f"人聲比背景大 {L['snr_pass']:.0f} dB 以上",
         "warn": f"{L['snr_warn']:.0f}–{L['snr_pass']:.0f} dB；或有電源嗡嗡聲", "fail": f"不到 {L['snr_warn']:.0f} dB；或嗡嗡聲只比人聲小不到 30 dB"},
        {"label": "回音", "pass": f"殘響 {L['rt_pass']} 秒以下", "warn": f"{L['rt_pass']}–{L['rt_warn']} 秒",
         "fail": f"超過 {L['rt_warn']} 秒"},
        {"label": "破音（爆音）", "pass": "說話時間的 0.01% 以下", "warn": "0.01%–0.1%", "fail": "超過 0.1%"},
        {"label": "音量", "pass": f"說話時 {L['level_pass']:.0f} dBFS 以上", "warn": f"{L['level_fail']:.0f} 到 {L['level_pass']:.0f} dBFS",
         "fail": f"低於 {L['level_fail']:.0f} dBFS"},
        {"label": "音質（頻寬）", "pass": f"聲音到 {L['band_pass'] / 1000:.0f} kHz 以上", "warn": f"{L['band_fail'] / 1000:.0f}–{L['band_pass'] / 1000:.0f} kHz",
         "fail": f"不到 {L['band_fail'] / 1000:.0f} kHz（電話音質）"},
        {"label": "後製痕跡", "pass": "停頓有自然的底噪", "warn": "停頓或字和字之間是數位的完全無聲（降噪、噪音閘門）", "fail": "—"},
        {"label": "斷訊", "pass": "沒有", "warn": "1–2 處", "fail": "3 處以上"},
        {"label": "說話時底下的背景（深入檢查才有）", "pass": f"分離後剩下的比人聲小 {abs(L['under_pass']):.0f} dB 以上",
         "warn": f"小 {abs(L['under_warn']):.0f}–{abs(L['under_pass']):.0f} dB", "fail": f"小不到 {abs(L['under_warn']):.0f} dB"},
    ]

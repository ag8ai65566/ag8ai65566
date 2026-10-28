"""Finding breathing, sighs, panting and wordless sounds in a voice's recordings, to use as sound tags.

Speech recognition writes no text for these, so most never became training material: voice detection cuts a sigh on
its own away, and a segment with no words is rejected. They are still in the imported recordings. This scan lists
candidates to listen to, then keep (as the person's own recording of a sound tag like [喘氣]) or dismiss:
- breath: an unvoiced, breathy sound of 0.25–2.5 s, quieter than speech, close to this voice's speech (an inhale
  before a sentence, an exhale or a sigh after one);
- pant: three or more short breaths in a row with hardly any voiced speech between them;
- sigh / pant / gasp by text: transcripts with はぁ, ふぅ, ため息, はぁはぁ, ひっ, 唉, phew …;
- voice: a segment with voice in it but (almost) no words: 嗯, 啊, a moan, a hum, a laugh.
The detectors are plain measurements (level, voicing, where the energy sits in the spectrum), so these are
candidates: listening decides.
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np

from . import audio, config, db, jobs, phrases
from .audiocheck import runs

SR = 16000
HOP = 160      # 10 ms between frames
WIN = 640      # 40 ms window: two periods of a 50 Hz voice, for the voicing measure
NFFT = 2048
NEAR = 1.5     # a sound within this many seconds of one of the voice's segments counts as this voice's
PAD = 0.4      # context played before and after a candidate

KINDS = {  # kind → name, and the sound tag it suggests (a name tags.py knows)
    "breath": ("呼吸聲", "[吸氣]"), "pant": ("喘氣", "[喘氣]"), "sigh": ("嘆氣", "[嘆氣]"),
    "gasp": ("倒抽一口氣", "[倒抽一口氣]"), "laugh": ("笑聲", "[笑聲]"), "cry": ("哭聲", "[抽泣]"),
    "cough": ("咳嗽", "[咳嗽]"), "throat": ("清喉嚨", "[清喉嚨]"), "sneeze": ("打噴嚏", "[打噴嚏]"),
    "sniff": ("吸鼻子", "[吸鼻子]"), "yawn": ("打哈欠", "[打哈欠]"), "hum": ("哼歌", "[哼歌]"), "tsk": ("嘖", "[嘖]"),
    "scoff": ("哼・嗤笑", "[哼]"), "scream": ("尖叫", "[尖叫]"), "groan": ("呻吟", "[呻吟]"),
    "gulp": ("吞口水", "[吞口水]"), "hiccup": ("打嗝", "[打嗝]"), "voice": ("沒有字的聲音", ""),
}


def _ann(words: str) -> str:
    """A description of a sound in brackets, parentheses or asterisks, as speech recognition writes them in English
    transcripts: "(laughs)", "[Laughter]", "*sighs*", "(breathing heavily)", "(clears throat)"."""
    return r"[(\[*（【][^)\]*）】]{0,30}?\b(?:" + words + r")"


TEXT_KINDS = [(k, re.compile(rx, re.IGNORECASE)) for k, rx in [  # the first that matches a transcript wins
    ("pant", _ann(r"pant\w*|breathing heavily|heavy breathing|out of breath|breathless|huff\w*")
     + r"|(?:(?:はぁ|ハァ|はあ|ハア|はっ|ハッ|ぜえ|ゼエ)[、。…・っッー〜~!！\s]*){2,}|\bhuff(?:ing)?\b|喘氣|喘息|呼哧|氣喘吁吁"),
    ("laugh", _ann(r"laugh\w*|chuckl\w*|giggl\w*|snicker\w*|cackl\w*|guffaw\w*")
     + r"|[(（]笑[)）]|\b(?:a?ha){2,}h?\b|\b(?:he){2,}h?\b|\blol\b|\blmao\b|あはは|アハハ|えへへ|エヘヘ|うふふ|ウフフ"
       r"|ふふっ|フフッ|くすくす|クスクス|ははは|ハハハ|[wｗ]{3,}|哈哈|呵呵|嘻嘻|嘿嘿|噗哧"),
    ("cry", _ann(r"cr(?:y|ies|ying)|sob\w*|whimper\w*|sniffl\w*|weep\w*")
     + r"|ぐすっ|グスッ|ぐすん|えぐっ|うえーん|うわーん|嗚嗚|啜泣|抽泣"),
    ("cough", _ann(r"cough\w*") + r"|ゴホ|ごほ|げほ|ゲホ|けほ|ケホ|コホッ|こほっ|咳咳"),
    ("throat", _ann(r"clears? (?:\w+ )?throat|throat[- ]clear\w*") + r"|\bahem\b|咳払い|清喉嚨|清嗓"),
    ("sneeze", _ann(r"sneez\w*") + r"|\ba?h?-?choo\b|くしゅん|クシュン|へっくし|ハクション|はくしょん|くちゅん|哈啾|阿嚏"),
    ("sniff", _ann(r"sniffs?\b|sniffing") + r"|すんすん|スンスン|ずずっ|吸鼻子"),
    ("yawn", _ann(r"yawn\w*") + r"|ふぁ[ぁあ〜ー]|ふわぁ|ふあ[〜ー]|あくび|打哈欠|哈欠|呵欠"),
    ("hum", _ann(r"hums\b|humming") + r"|鼻歌|ふんふん|フンフン|ルンルン|哼歌"),
    ("tsk", _ann(r"tsk|tuts?|clicks? (?:\w+ )?tongue") + r"|\btsk\b|\btch\b|ちっ|チッ|ちぇっ|チェッ|舌打ち|嘖"),
    ("scoff", _ann(r"scoff\w*|snort\w*|sneer\w*") + r"|\bpff+t?\b|\bhmph\b|\bpsh\b|ふんっ|フンッ|哼"),
    ("scream", _ann(r"scream\w*|shriek\w*|yelp\w*|squeal\w*")
     + r"|\beek\b|\ba{3,}h*\b|きゃー|キャー|きゃあ|ぎゃー|ギャー|ひゃっ|ヒャッ|うわあああ|啊啊啊|尖叫"),
    ("groan", _ann(r"groan\w*|moan\w*|grunt\w*|whin\w*") + r"|\bugh+\b|\bargh+\b|\bnngh?\b|ううう|ぐぬぬ|うめき|呻吟"),
    ("gulp", _ann(r"gulp\w*|swallow\w*") + r"|ごくり|ゴクリ|ごくっ|ゴクッ|吞口水|咕嚕"),
    ("hiccup", _ann(r"hiccup\w*") + r"|しゃっくり|打嗝"),
    ("sigh", _ann(r"sigh\w*|exhal\w*") + r"|\bphew\b|\bwhew\b|はぁ|ハァ|はあ[ぁあ…ー]|ハア[ァア…ー]|ふぅ|フゥ|ふう|ふー|フー"
     r"|やれやれ|ため息|溜息|唉|嘆氣|嘆息"),
    ("gasp", _ann(r"gasp\w*|inhal\w*|breath(?:es)? in|sharp breath") + r"|ひっ(?!く)|ヒッ(?!ク)|はっ[!！]|ハッ[!！]|息をのむ|倒抽"),
    ("breath", _ann(r"breath\w*")),
]]
ANNOTATION = re.compile(r"[(\[*（【][^)\]*）】]{1,40}[)\]*）】]")
# a transcript made only of these is a sound rather than words (はい and いいえ are words, so い and え are left out)
WORDLESS_JA = re.compile(r"[ぁぅぉあうおんっーはひふへほハヒフヘホアウオンッ〜嗯啊唔哦呃喔哈呵嘿哼]+")
WORDLESS_EN = re.compile(r"(?:m+|h+m+|a+h*|o+h*|u+h+|u+m+|e+h+|h+a+|h+e+|h+u+h*|ugh+|oof|whew|phew|pff+t?|hmph|tsk|tch"
                         r"|eek|o+h+|aw+|mhm|mm-?hmm|uh-?huh|ahem|a?h?-?choo)", re.IGNORECASE)
PUNCT = re.compile(r"[\s、。，．,.!?！？…〜~・\"'「」『』（）()\-]+")


def text_kind(text: str) -> str | None:
    for kind, rx in TEXT_KINDS:
        if rx.search(text or ""):
            return kind
    return None


def wordless(text: str) -> bool:
    """Only interjections, sound descriptions ("(laughs)") or nothing."""
    toks = [t for t in PUNCT.split(ANNOTATION.sub(" ", text or "")) if t]
    return all(WORDLESS_JA.fullmatch(t) or WORDLESS_EN.fullmatch(t) for t in toks)


# --- measurements ---------------------------------------------------------------------------------------------------

def _blocks(path: Path):
    """The recording at 16 kHz in blocks of a minute (a long recording is not held in memory)."""
    import soundfile as sf
    with sf.SoundFile(str(path)) as fh:
        sr = fh.samplerate
        for block in fh.blocks(blocksize=sr * 60, dtype="float32", always_2d=True):
            yield audio.resample(block.mean(axis=1), sr, SR)


def features(blocks) -> dict:
    """Per 10 ms frame: level (dB), voicing (0–1: the normalised autocorrelation peak in the 70–500 Hz pitch range)
    and spectral centroid (Hz). `blocks`: consecutive pieces of a 16 kHz signal."""
    from scipy import fft
    w = np.hanning(WIN).astype(np.float32)
    wac = fft.irfft(np.abs(fft.rfft(w, NFFT)) ** 2, NFFT)[:WIN]
    wac = np.maximum(wac / wac[0], 1e-3)  # the window's own autocorrelation, divided out (Boersma 1993)
    lo, hi = SR // 500, SR // 70
    freqs = np.fft.rfftfreq(NFFT, 1 / SR).astype(np.float32)
    mid = slice(WIN // 2 - 200, WIN // 2 + 200)
    es, vs, cs = [], [], []
    tail = np.zeros(0, np.float32)
    for block in blocks:
        x = np.concatenate([tail, np.asarray(block, np.float32)])
        k = (len(x) - WIN) // HOP + 1 if len(x) >= WIN else 0
        for a in range(0, k, 2000):
            n = min(2000, k - a)
            fr = x[(a + np.arange(n))[:, None] * HOP + np.arange(WIN)[None, :]]
            es.append(10 * np.log10(np.mean(fr[:, mid] ** 2, axis=1) + 1e-10))
            sp = fft.rfft(fr * w, NFFT, axis=1)
            p = sp.real ** 2 + sp.imag ** 2
            ac = fft.irfft(p, NFFT, axis=1)[:, :hi + 1]
            ac = ac / np.maximum(ac[:, :1], 1e-12) / wac[:hi + 1]
            vs.append(np.clip(ac[:, lo:].max(axis=1), 0, 1))
            cs.append((p * freqs).sum(axis=1) / np.maximum(p.sum(axis=1), 1e-12))
        tail = x[k * HOP:]
    cat = lambda xs: np.concatenate(xs).astype(np.float32) if xs else np.zeros(0, np.float32)  # noqa: E731
    f = {"e": cat(es), "v": cat(vs), "c": cat(cs)}
    if len(f["e"]):
        f["floor"] = local_floor(f["e"])
        f["voiced"] = (f["v"] > 0.6) & (f["e"] > f["floor"] + 12)
        f["speech"] = float(np.percentile(f["e"][f["voiced"]], 90)) if f["voiced"].sum() >= 30 else None
    return f


def local_floor(e: np.ndarray, block: int = 500) -> np.ndarray:
    """The background level around each frame: the 10th percentile of every 5 s, ignoring digital silence (a muted
    intro would make music after it look like quiet background), interpolated between blocks."""
    centres, levels = [], []
    for a in range(0, len(e), block):
        x = e[a:a + block]
        x = x[x > -90]
        if len(x) >= 20:
            centres.append(a + block / 2)
            levels.append(float(np.percentile(x, 10)))
    if not levels:
        return np.full(len(e), -100.0, np.float32)
    return np.interp(np.arange(len(e)), centres, levels).astype(np.float32)


def _t(i: int) -> float:
    return round(i * HOP / SR, 2)


def _close(mask: np.ndarray, n: int) -> np.ndarray:
    from scipy import ndimage
    return ndimage.binary_closing(mask, structure=np.ones(n, bool)) if len(mask) else mask


def detect(f: dict) -> list[dict]:
    """Breaths and panting in a recording's measurements."""
    if len(f["e"]) < 50 or f.get("speech") is None:
        return []  # no speech to compare with
    e, v, c, floor, speech = f["e"], f["v"], f["c"], f["floor"], f["speech"]
    # where music or noise is behind the voice a breath cannot be told from it (transcripts are still searched)
    clear = (speech - floor) >= 30
    if not clear.any():
        return []
    talk = f["voiced"] & (e > speech - 15)
    breathy = _close(clear & (v < 0.45) & (e > floor + 6) & (e < speech - 4) & (c > 500) & (c < 3800), 7)
    loose = _close(clear & (v < 0.6) & (e > floor + 6) & (e < speech - 1) & (c > 500) & (c < 4000), 3)
    # breath noise sits around 1–3 kHz; a low hum or rumble (under ~800 Hz) is not a breath, nor an "s" (over 4 kHz)
    airy = lambda a, b: 800 < float(np.median(c[a:b])) < 3500  # noqa: E731
    out: list[dict] = []
    audible = lambda a, b: float(np.mean(e[a:b])) > speech - 40  # noqa: E731  (quieter is too faint to use)
    # panting: three or more short breaths (0.1–0.9 s) at most 0.6 s apart, with hardly any speech between them
    groups: list[list[tuple[int, int]]] = []
    for a, b in runs(loose, 10):
        if b - a > 90 or not audible(a, b) or not airy(a, b):
            continue
        if groups and a - groups[-1][-1][1] <= 60:
            groups[-1].append((a, b))
        else:
            groups.append([(a, b)])
    for g in groups:
        a, b = g[0][0], g[-1][1]
        if len(g) >= 3 and b - a <= 800 and talk[a:b].mean() < 0.15 and e[a:b].max() < speech - 3:
            out.append({"kind": "pant", "start": _t(a), "end": _t(b + 4), "score": round(min(1.0, len(g) / 6), 3),
                        "meta": {"bursts": len(g)}})
    # single breaths: 0.25–2.5 s
    for a, b in runs(breathy, 25):
        if b - a > 250 or not audible(a, b) or not airy(a, b) \
                or any(_t(a) < o["end"] and o["start"] < _t(b) for o in out):
            continue
        where = "before" if talk[b:b + 40].any() else "after" if talk[max(0, a - 40):a].any() else "alone"
        level = float(np.mean(e[a:b] - floor[a:b]) / np.mean(speech - floor[a:b]))
        out.append({"kind": "breath", "start": _t(a), "end": _t(b + 4),
                    "score": round(min(1.0, level * 1.5) * min(1.0, (b - a) / 50), 3), "meta": {"where": where}})
    return out


def voiced_share(f: dict, start: float, end: float) -> float:
    a, b = int(start * SR / HOP), int(end * SR / HOP)
    seg = f["voiced"][a:b] if len(f.get("e", [])) else np.zeros(0)
    return float(seg.mean()) if len(seg) else 0.0


# --- the scan ---------------------------------------------------------------------------------------------------------

def master_of(source_id: str) -> Path:
    return config.DATA / "sources" / source_id / "master.wav"


def _overlap(a: tuple[float, float], b: tuple[float, float]) -> float:
    return max(0.0, min(a[1], b[1]) - max(a[0], b[0])) / max(1e-6, min(a[1] - a[0], b[1] - b[0]))


@jobs.handler("find_sounds", queue="check")
def find_sounds(ctx: jobs.JobContext) -> dict:
    vid = ctx.params["voice_id"]
    segs = db.query('SELECT id, source_id, start, "end", text FROM segments WHERE voice_id=? ORDER BY source_id, start',
                    (vid,))
    by_source: dict[str, list[dict]] = {}
    for s in segs:
        by_source.setdefault(s["source_id"], []).append(s)
    decided: dict[str, list[tuple[float, float]]] = {}  # kept or dismissed earlier: not listed again
    for r in db.query('SELECT source_id, start, "end" FROM sound_finds WHERE voice_id=? AND status<>\'new\'', (vid,)):
        decided.setdefault(r["source_id"], []).append((r["start"], r["end"]))
    with db.tx() as c:
        c.execute("DELETE FROM sound_finds WHERE voice_id=? AND status='new'", (vid,))
    counts: dict[str, int] = {}
    for i, (sid, ss) in enumerate(by_source.items()):
        ctx.check()
        ctx.progress(i / max(1, len(by_source)), f"掃描第 {i + 1}/{len(by_source)} 段錄音")
        m = master_of(sid)
        try:
            f = features(_blocks(m)) if m.exists() else None
        except Exception as e:  # an unreadable file: its transcripts are still searched
            ctx.log(f"{sid}: {e}")
            f = None
        found: list[dict] = []
        if f is not None:
            near = [(s["start"] - NEAR, s["end"] + NEAR) for s in ss]
            found += [x for x in detect(f) if any(x["start"] < b and a < x["end"] for a, b in near)]
        for s in ss:
            kind = text_kind(s["text"])
            if kind:
                found.append({"kind": kind, "start": s["start"], "end": s["end"], "segment_id": s["id"],
                              "text": s["text"], "score": 0.5, "how": "text"})
            elif wordless(s["text"]) and f is not None and (share := voiced_share(f, s["start"], s["end"])) > 0.2:
                found.append({"kind": "voice", "start": s["start"], "end": s["end"], "segment_id": s["id"],
                              "text": s["text"], "score": round(share, 3)})
        rows = []
        for x in found:
            span = (x["start"], x["end"])
            if any(_overlap(span, d) > 0.5 for d in decided.get(sid, [])):
                continue
            if not x.get("segment_id"):
                x["segment_id"] = next((s["id"] for s in ss if s["start"] <= x["start"] and x["end"] <= s["end"]),
                                       None)
            rows.append({"id": db.new_id("snd"), "voice_id": vid, "source_id": sid, "segment_id": x.get("segment_id"),
                         "start": round(x["start"], 2), "end": round(x["end"], 2), "kind": x["kind"],
                         "how": x.get("how", "sound"), "score": x["score"], "text": x.get("text", ""),
                         "status": "new", "meta": x.get("meta", {}), "created_at": db.now()})
            counts[x["kind"]] = counts.get(x["kind"], 0) + 1
        for r in rows:
            db.insert("sound_finds", r)
    total = sum(counts.values())
    parts = "、".join(f"{KINDS[k][0]} {n}" for k, n in counts.items())
    return {"counts": counts, "message": f"找到 {total} 個候選" + (f"：{parts}" if parts else "（這些錄音裡沒有找到）")}


def slice_start(find: dict) -> float:
    """Where the played slice starts in the recording (the processed recording, else the segment it is in)."""
    if not master_of(find["source_id"]).exists() and (s := db.get("segments", find["segment_id"] or "")):
        return max(s["start"], find["start"] - PAD)
    return max(0.0, find["start"] - PAD)


def slice_audio(find: dict) -> tuple[np.ndarray, int]:
    """The candidate with PAD seconds of context on either side, from slice_start(find)."""
    import soundfile as sf
    a = slice_start(find)
    m = master_of(find["source_id"])
    if m.exists():
        info = sf.info(str(m))
        b = min(info.duration, find["end"] + PAD)
        y, sr = sf.read(str(m), start=int(a * info.samplerate), stop=int(b * info.samplerate), dtype="float32",
                        always_2d=True)
        return y.mean(axis=1), sr
    s = db.get("segments", find["segment_id"] or "")
    if not s:
        raise KeyError(find["id"])
    y, sr = audio.load(Path(s["path"]))
    return y[int((a - s["start"]) * sr):int((find["end"] + PAD - s["start"]) * sr)], sr


def keep(find: dict, phrase_id: str, start: float, end: float, emotion: str | None) -> dict:
    """Cut [start, end] (seconds in the recording) into the sound tag's recordings."""
    if phrases.get(phrase_id)["voice_id"] != find["voice_id"]:
        raise ValueError("只能加到同一個聲音的標籤")
    if master_of(find["source_id"]).exists():
        ph = phrases.add_clip_source(phrase_id, find["source_id"], start, end, emotion)
    else:
        s = db.get("segments", find["segment_id"] or "")
        if not s:
            raise ValueError("這段錄音和片段都已經不在了")
        ph = phrases.add_clip_segment(phrase_id, s["id"], start - s["start"], end - s["start"], emotion)
    db.update("sound_finds", find["id"], {"status": "kept", "meta": {**(find["meta"] or {}), "phrase": phrase_id}})
    return ph

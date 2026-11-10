"""Delivery folders: one person's recordings, already cut, labelled and listed, imported in one go.

A delivery folder looks like this (see docs/16-delivery.md):

    <person>/
      交付/clean/<lang>/<emotion>/<date>_<video>_<start>-<end>.wav           quiet background
      交付/bgm/<lang>/<emotion>/...                                           faint background music
      交付/clean_去背景音樂/<lang>/<emotion>/<date>_<video>~sep_<s>-<e>.wav   music removed (not denoised)
      交付/phrases/<catchphrase>/<emotion>_<date>_<video>_<s>-<e>.wav         catchphrase clips
      交付/clips.csv, 交付/phrases.csv
      常用語/原音|已去背景音樂/<type>/<no>_<sentence>/<emotion>_<date>_<video>_<s>-<e>.wav, 常用語/常用語.csv
      素材庫/原音|已去背景音樂/<group>/<tag>/<date>_<video>_<s>-<e>.wav, 素材庫/tags.csv

What goes where:
- every clip with a transcript (交付, 常用語, and 素材庫 clips with text) becomes a training segment of the voice,
  with its language and emotion; one recording (a stream) per video, so validation holds out whole streams;
- 交付/phrases and 常用語 become catchphrases with a few original recordings each (spliced into synthesis);
- 素材庫 sounds (laughs, breaths, sneezes …) become sound tags, e.g. "[笑聲]", with the person's recordings.

Nothing is imported for a voice without a complete consent record (the same rule as datasets and training).
"""
from __future__ import annotations

import csv
import hashlib
import io
import re
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from . import audio, config, datasets, db, emotions, jobs, phrases, tags

PARTS = ("交付", "常用語", "素材庫")
AUDIO_EXT = {".wav", ".flac"}
NAME = re.compile(r"^(?:(?P<emo>[A-Za-z]+)_)?(?P<date>\d{8})_(?P<vid>.+?)(?P<sep>~sep)?_"
                  r"(?P<s>\d+(?:\.\d+)?)-(?P<e>\d+(?:\.\d+)?)$")
LANGS = {"en": "en", "ja": "ja", "jp": "ja", "mixed": None, "mix": None}
SOUND_GROUPS = ("聲音",)
ORIG, SEP = ("原音",), ("已去背景音樂",)
BGM_MODES = ("sep", "original", "skip")   # music in the background: use the music-removed copy / the original / neither


class ConsentMissing(Exception):
    pass


@dataclass
class Clip:
    path: Path
    part: str                       # delivery | phrase | common | library
    kind: str = "clean"             # clean | bgm | sep
    lang: str | None = None
    emotion: str | None = None
    date: str = ""
    vid: str = ""
    start: float | None = None
    end: float | None = None
    text: str = ""
    phrase: str = ""                # catchphrase / common phrase text, or the tag of a library clip
    group: str = ""                 # library: the tag's group; common: the phrase type
    rank: float = 0.0               # higher = better candidate for a catchphrase or sound tag
    complete: bool = True
    extra: dict = field(default_factory=dict)

    @property
    def duration(self) -> float | None:
        return round(self.end - self.start, 3) if self.start is not None and self.end is not None else None

    def key(self) -> tuple:
        return (self.vid, self.start, self.end)


# --- reading -------------------------------------------------------------------------------------------------------

def parse_name(stem: str) -> dict:
    m = NAME.match(stem)
    if not m:
        return {}
    return {"emo": (m.group("emo") or "").lower(), "date": m.group("date"), "vid": m.group("vid"),
            "sep": bool(m.group("sep")), "start": float(m.group("s")), "end": float(m.group("e"))}


def emotion(x: str | None) -> str | None:
    x = (x or "").strip().lower()
    return x if emotions.valid(x) else None


def read_csv(path: Path) -> list[dict]:
    """Rows of a CSV as dicts with lower-cased, trimmed headers (UTF-8 with or without BOM; Big5 as a fallback)."""
    if not path.exists():
        return []
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "cp950"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = raw.decode("utf-8", errors="replace")
    rows = list(csv.reader(io.StringIO(text)))
    if not rows:
        return []
    head = [h.strip().lower() for h in rows[0]]
    return [{head[i]: (r[i].strip() if i < len(r) else "") for i in range(len(head))} for r in rows[1:] if any(r)]


def col(row: dict, *names: str) -> str:
    for n in names:
        if row.get(n.lower()):
            return row[n.lower()]
    return ""


def _norm_path(x: str) -> str:
    x = unicodedata.normalize("NFC", x.replace("\\", "/").strip())
    return re.sub(r"^(\./)+", "", x).lower()


def by_file(rows: list[dict]) -> dict[str, dict]:
    """CSV rows keyed by the file column: a path from the CSV's own folder (交付\\, 常用語\\, 素材庫\\), e.g.
    "原音/開場招呼/153_…/happy_….wav", or a bare file name. A bare name is only used when it is unique: the
    original and the music-removed copy of one clip have the same name in different folders."""
    out: dict[str, dict] = {}
    names: dict[str, list[dict]] = {}
    for r in rows:
        f = col(r, "file", "檔案", "檔名", "filename", "path", "路徑", "音檔")
        if f:
            rel = _norm_path(f)
            out["rel:" + rel] = r
            names.setdefault(rel.rsplit("/", 1)[-1], []).append(r)
    for n, rs in names.items():
        if len(rs) == 1:
            out["name:" + n] = rs[0]
    return out


def row_for(rows: dict[str, dict], base: Path, p: Path) -> dict:
    """The CSV row of an audio file: by its path from the CSV's folder, else by its name when that is unique."""
    rel = _norm_path(p.relative_to(base).as_posix())
    return rows.get("rel:" + rel) or rows.get("name:" + rel.rsplit("/", 1)[-1]) or {}


def _num(x: str) -> float | None:
    try:
        return float(str(x).strip().rstrip("%")) / (100 if str(x).strip().endswith("%") else 1)
    except ValueError:
        return None


def is_complete(x: str) -> bool:
    """句子完整度: words like 完整 / complete / ok, or a number ≥ 0.9; anything unknown counts as complete."""
    s = (x or "").strip().lower()
    if not s:
        return True
    if any(w in s for w in ("不完整", "partial", "incomplete", "缺", "截斷", "cut")) or s in ("no", "false", "否", "0"):
        return False
    n = _num(s)
    return n is None or n >= 0.9


def _wavs(d: Path) -> list[Path]:
    return sorted(p for p in d.rglob("*") if p.is_file() and p.suffix.lower() in AUDIO_EXT) if d.is_dir() else []


def _clip(p: Path, part: str, **kw) -> Clip:
    n = parse_name(p.stem)
    c = Clip(path=p, part=part, date=n.get("date", ""), vid=n.get("vid", ""), start=n.get("start"), end=n.get("end"),
             **kw)
    if c.emotion is None and n.get("emo"):
        c.emotion = emotion(n["emo"])
    if not c.vid:  # a name outside the pattern: one recording per folder
        c.vid = "~" + p.parent.name
    return c


def read_delivery(root: Path) -> list[Clip]:
    d = root / "交付"
    rows = by_file(read_csv(d / "clips.csv"))
    out = []
    for kind, sub in (("clean", "clean"), ("bgm", "bgm"), ("sep", "clean_去背景音樂")):
        base = d / sub
        for p in _wavs(base):
            rel = p.relative_to(base).parts
            lang = LANGS.get(rel[0].lower()) if len(rel) > 2 else None
            emo = emotion(rel[1]) if len(rel) > 2 else None
            r = row_for(rows, d, p)
            c = _clip(p, "delivery", kind=kind, lang=lang, emotion=emo, text=col(r, "transcript", "text", "文字"))
            if r:
                c.lang = LANGS.get(col(r, "lang").lower(), c.lang) if col(r, "lang") else c.lang
                c.emotion = emotion(col(r, "emotion")) or c.emotion
                c.extra["url"] = col(r, "url")
            out.append(c)
    phr_rows = read_csv(d / "phrases.csv")
    meta: dict[str, dict] = {}
    for r in phr_rows:
        ph = col(r, "phrase", "口頭禪")
        if ph:
            m = meta.setdefault(ph, {"variants": [], "lang": None})
            m["variants"] += [v.strip() for v in re.split(r"[|;／/、,]", col(r, "variants")) if v.strip()]
            m["lang"] = m["lang"] or LANGS.get(col(r, "lang").lower())
    files = by_file(phr_rows)
    base = d / "phrases"
    if base.is_dir():
        for folder in sorted(x for x in base.iterdir() if x.is_dir()):
            for p in _wavs(folder):
                r = row_for(files, d, p)
                text = col(r, "phrase", "口頭禪") or folder.name
                c = _clip(p, "phrase", phrase=text, lang=(meta.get(text) or {}).get("lang"),
                          emotion=emotion(col(r, "emotion")))
                c.extra["variants"] = (meta.get(text) or {}).get("variants", [])
                out.append(c)
    return out


def read_common(root: Path) -> list[Clip]:
    d = root / "常用語"
    rows = by_file(read_csv(d / "常用語.csv"))
    by_no: dict[str, dict] = {}
    for k, r in rows.items():
        if not k.startswith("rel:"):
            continue
        no = col(r, "編號", "id", "no")
        if no and col(r, "原文", "text", "phrase"):
            by_no.setdefault(no, r)
    out = []
    for sub, kind in (("原音", "clean"), ("已去背景音樂", "sep")):
        base = d / sub
        for p in _wavs(base):
            rel = p.relative_to(base).parts
            if len(rel) < 3:
                continue
            ptype, folder = rel[0], rel[1]
            no, _, short = folder.partition("_")
            r = row_for(rows, d, p) or by_no.get(no, {})
            text = col(r, "原文", "text", "phrase") or short or folder
            c = _clip(p, "common", kind=kind, phrase=text, group=ptype, text=text,
                      lang=LANGS.get(col(r, "語言", "lang").lower()), emotion=emotion(col(r, "情緒", "emotion")),
                      complete=is_complete(col(r, "句子完整度", "完整度", "complete")))
            sim = _num(col(r, "聲紋相似度", "相似度", "similarity")) or 0.0
            c.rank = sim + (1.0 if c.complete else 0.0)
            c.extra["no"] = no
            out.append(c)
    return out


def read_library(root: Path) -> list[Clip]:
    d = root / "素材庫"
    rows = by_file(read_csv(d / "tags.csv"))
    out = []
    for sub, kind in (("原音", "clean"), ("已去背景音樂", "sep")):
        base = d / sub
        for p in _wavs(base):
            rel = p.relative_to(base).parts
            if len(rel) < 3:
                continue
            grp, tag = rel[0], rel[1]
            r = row_for(rows, d, p)
            c = _clip(p, "library", kind=kind, phrase=tag, group=grp, text=col(r, "文字", "text", "transcript"))
            c.emotion = tags.emotion_of([tag]) if grp not in SOUND_GROUPS else None
            out.append(c)
    return out


def is_person(d: Path) -> bool:
    return any((d / p).is_dir() for p in PARTS)


def people(root: Path, depth: int = 5) -> list[Path]:
    """The person folders under a path (the path itself when it is one), in name order."""
    if is_person(root):
        return [root]
    out: list[Path] = []
    if depth <= 0 or not root.is_dir():
        return out
    for d in sorted(x for x in root.iterdir() if x.is_dir() and not x.name.startswith(".")):
        out += people(d, depth - 1)
    return out


# --- choosing ------------------------------------------------------------------------------------------------------

def _overlaps(a: Clip, b: Clip, share: float = 0.5) -> bool:
    if a.vid != b.vid or a.start is None or b.start is None:
        return False
    inter = min(a.end, b.end) - max(a.start, b.start)
    return inter > share * min(a.end - a.start, b.end - b.start)


def training_clips(clips: list[Clip], bgm: str = "sep", common: bool = True) -> tuple[list[Clip], dict]:
    """The clips that become training segments, one copy per moment of a stream.

    Music in the background: "sep" uses the music-removed copy where one exists (the original otherwise), "original"
    uses the original, "skip" leaves both out. Delivery clips come first, then common phrases, then library clips;
    a clip that overlaps one already chosen (same stream, more than half of the shorter one) is a duplicate."""
    skipped = {"no_text": 0, "bgm": 0, "duplicate": 0, "incomplete": 0}
    deliv = [c for c in clips if c.part == "delivery"]
    seps = {c.key(): c for c in deliv if c.kind == "sep"}
    chosen: list[Clip] = []
    used_sep: set = set()
    for c in deliv:
        if c.kind == "clean":
            chosen.append(c)
        elif c.kind == "bgm":
            if bgm == "skip":
                skipped["bgm"] += 1
                continue
            alt = seps.get(c.key())
            if bgm == "sep" and alt is not None:
                alt.emotion = alt.emotion or c.emotion
                alt.text = alt.text or c.text
                chosen.append(alt)
            else:
                chosen.append(c)
            if alt is not None:
                used_sep.add(c.key())
    for k, c in seps.items():  # music-removed copies of clips that are not in bgm/
        if k not in used_sep:
            if bgm == "skip":
                skipped["bgm"] += 1
            else:
                chosen.append(c)
    extra: list[Clip] = []
    if common:
        com = [c for c in clips if c.part == "common"]
        best: dict[tuple, Clip] = {}
        for c in com:  # the same moment as original and music-removed copy: keep the one the bgm setting asks for
            k = c.key()
            prefer = "sep" if bgm == "sep" else "clean"
            if k not in best or (c.kind == prefer and best[k].kind != prefer):
                best[k] = c
        for c in best.values():
            if not c.complete:
                skipped["incomplete"] += 1
            else:
                extra.append(c)
    extra += [c for c in clips if c.part == "library" and c.group not in SOUND_GROUPS and c.kind == "clean"]
    out: list[Clip] = []
    for c in chosen + extra:
        if not c.text.strip():
            skipped["no_text"] += 1
            continue
        if any(_overlaps(c, o) for o in out if o.vid == c.vid):
            skipped["duplicate"] += 1
            continue
        out.append(c)
    return out, skipped


def pick(clips: list[Clip], n: int, prefer: str = "clean") -> list[Clip]:
    """Up to n recordings of one phrase or sound: complete ones, the preferred copy, many moods, best ranked first."""
    order = sorted(clips, key=lambda c: (not c.complete, c.kind != prefer, -c.rank, c.date, c.start or 0))
    out: list[Clip] = []
    seen_moods: set = set()
    for c in order:  # one per mood first
        if len(out) < n and (c.emotion or "") not in seen_moods and not any(_overlaps(c, o) for o in out):
            out.append(c)
            seen_moods.add(c.emotion or "")
    for c in order:
        if len(out) < n and c not in out and not any(_overlaps(c, o) for o in out):
            out.append(c)
    return out


def phrase_groups(clips: list[Clip]) -> dict[str, dict]:
    """Catchphrase text → its clips, type and variants (交付/phrases and 常用語)."""
    out: dict[str, dict] = {}
    for c in clips:
        if c.part not in ("phrase", "common") or not c.phrase.strip():
            continue
        g = out.setdefault(c.phrase.strip(), {"clips": [], "type": c.group or "口頭禪", "variants": [], "lang": c.lang})
        g["clips"].append(c)
        g["variants"] += [v for v in c.extra.get("variants", []) if v not in g["variants"]]
        g["lang"] = g["lang"] or c.lang
    return out


def sound_groups(clips: list[Clip]) -> dict[str, list[Clip]]:
    """Sound tag "[name]" → its clips (素材庫 sounds). Known tags take the catalogue's Chinese name."""
    out: dict[str, list[Clip]] = {}
    for c in clips:
        if c.part == "library" and c.group in SOUND_GROUPS:
            t = tags.lookup(c.phrase)
            out.setdefault(phrases.as_tag(t.zh if t else c.phrase), []).append(c)
    return out


# --- scan (what the import would do) -------------------------------------------------------------------------------

def read_all(root: Path) -> list[Clip]:
    return read_delivery(root) + read_common(root) + read_library(root)


def _minutes(clips) -> float:
    return round(sum(c.duration or 0 for c in clips) / 60, 1)


def scan_person(root: Path, base: Path, bgm: str = "sep") -> dict:
    clips = read_all(root)
    train, skipped = training_clips(clips, bgm)
    deliv = [c for c in clips if c.part == "delivery"]
    groups = phrase_groups(clips)
    sounds = sound_groups(clips)
    langs: dict[str, float] = {}
    emos: dict[str, float] = {}
    for c in train:
        langs[c.lang or "mixed"] = langs.get(c.lang or "mixed", 0) + (c.duration or 0) / 60
        emos[c.emotion or ""] = emos.get(c.emotion or "", 0) + (c.duration or 0) / 60
    name = root.name
    rel = root.relative_to(base).parts[:-1] if root != base and base in root.parents else ()
    match = [v for v in db.query("SELECT * FROM voices") if v["name"].strip().lower() == name.strip().lower()]
    v = match[0] if match else None
    return {
        "name": name, "path": str(root), "group": " / ".join(rel),
        "parts": {p: (root / p).is_dir() for p in PARTS},
        "delivery": {k: {"count": len(x), "minutes": _minutes(x)} for k, x in
                     (("clean", [c for c in deliv if c.kind == "clean"]), ("bgm", [c for c in deliv if c.kind == "bgm"]),
                      ("sep", [c for c in deliv if c.kind == "sep"]))},
        "training": {"count": len(train), "minutes": _minutes(train), "skipped": skipped,
                     "from_common": sum(1 for c in train if c.part == "common"),
                     "from_library": sum(1 for c in train if c.part == "library")},
        "languages": {k: round(x, 1) for k, x in sorted(langs.items(), key=lambda kv: -kv[1])},
        "emotions": {k: round(x, 1) for k, x in sorted(emos.items(), key=lambda kv: -kv[1])},
        "phrases": {"count": len(groups), "clips": sum(len(g["clips"]) for g in groups.values()),
                    "types": sorted({g["type"] for g in groups.values()})},
        "sounds": {"count": len(sounds), "clips": sum(len(x) for x in sounds.values()), "names": sorted(sounds)},
        "voice": {"id": v["id"], "name": v["name"], "consent_ok": datasets.consent_ok(v)} if v else None,
    }


def scan(path: str, bgm: str = "sep") -> dict:
    root = Path(path.strip().strip('"')).expanduser()
    if not root.exists():
        raise FileNotFoundError(f"找不到：{root}")
    found = people(root)
    return {"path": str(root), "people": [scan_person(p, root, bgm) for p in found]}


# --- import --------------------------------------------------------------------------------------------------------

def _hid(prefix: str, *parts: str) -> str:
    return f"{prefix}_{hashlib.sha1('|'.join(parts).encode('utf-8')).hexdigest()[:12]}"


def _source(voice_id: str, root: Path, c: Clip) -> str:
    """One recording per stream (video), so validation holds out whole streams."""
    sid = _hid("src", voice_id, str(root), c.vid)
    if not db.get("sources", sid):
        label = c.vid if not c.vid.startswith("~") else c.vid[1:]
        db.insert("sources", {"id": sid, "filename": f"{root.name} · {label}", "path": f"{root}#{label}",
                              "status": "ready", "voice_hint": voice_id, "language": c.lang, "emotion": None,
                              "meta": {"delivery": True, "root": str(root), "video_id": label, "date": c.date,
                                       "url": c.extra.get("url", "")},
                              "created_at": db.now()})
    return sid


def _segment(voice_id: str, root: Path, c: Clip, approve: bool) -> bool:
    """The clip as an approved (or pending) segment. Returns False when it was imported before."""
    from .pipeline import prepare
    seg_id = _hid("seg", voice_id, str(c.path.relative_to(root)))
    if db.get("segments", seg_id):
        return False
    src = _source(voice_id, root, c)
    dst = config.DATA / "segments" / src / f"{seg_id}.wav"
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        y, sr = audio.load(c.path, audio.MASTER_SR)
    except Exception:
        audio.extract(c.path, dst)
        y, sr = audio.load(dst)
    audio.save(dst, y, audio.MASTER_SR)
    st = audio.stats(y, sr)
    dur = len(y) / sr
    rec = {"id": seg_id, "source_id": src, "voice_id": voice_id, "start": c.start or 0.0,
           "end": c.end if c.end is not None else dur, "path": str(dst), "duration": dur, "text": c.text.strip(),
           "text_alt": "", "lang": c.lang, "snr": st["snr"], "clip": st["clip"], "spk_sim": None, "asr_agree": None,
           "emotion": c.emotion}
    score, flags = prepare.score(rec)
    if c.kind == "bgm":
        flags.append("bgm")
    elif c.kind == "sep":
        flags.append("separated")
    # the same length rule as automatic review: 1–30 s is approved when it passes, anything else waits for a person
    ok = approve and score >= 0.6 and "clipping" not in flags and 1.0 <= dur <= 30.0
    db.insert("segments", {**rec, "score": score, "flags": flags + (["delivery"] if ok else []),
                           "status": "approved" if ok else "pending"})
    return True


def _phrase(voice_id: str, text: str, variants: list[str], lang: str | None) -> dict | None:
    for p in phrases.list_for_voice(voice_id):
        if p["text"].lower() == text.lower() or text.lower() in [v.lower() for v in p["variants"]]:
            return p
    try:
        return phrases.create(voice_id, text, variants, lang)
    except ValueError:  # too long for a catchphrase (over phrases.MAX_TEXT characters)
        return None


def _add_clips(ph: dict, chosen: list[Clip], root: Path) -> tuple[int, list[str]]:
    have = {c.get("from") for c in ph["clips"]}
    added, problems = 0, []
    for c in chosen:
        rel = str(c.path.relative_to(root))
        if rel in have:
            continue
        try:
            phrases.add_clip_file(ph["id"], c.path, c.emotion, name=rel)
            added += 1
        except Exception as e:  # too short / long after trimming, unreadable
            problems.append(f"{rel}：{e}")
    return added, problems


def run(path: str, voice_id: str, bgm: str = "sep", common: bool = True, phrase_clips: int = 8,
        approve: bool = True, build: bool = True, progress=lambda f, m: None) -> dict:
    voice = db.get("voices", voice_id)
    if not voice:
        raise KeyError(voice_id)
    if not datasets.consent_ok(voice):
        raise ConsentMissing("這個聲音還沒有完整的同意紀錄，不能匯入。請先到「聲音與同意」填好同意紀錄。")
    if bgm not in BGM_MODES:
        raise ValueError("bgm")
    root = Path(path.strip().strip('"')).expanduser()
    if not is_person(root):
        raise FileNotFoundError(f"這不是一個人的交付資料夾（裡面沒有 交付／常用語／素材庫）：{root}")
    progress(0.01, "讀取清單")
    clips = read_all(root)
    train, skipped = training_clips(clips, bgm, common)
    added = 0
    for i, c in enumerate(train):
        if i % 20 == 0:
            progress(0.02 + 0.7 * i / max(1, len(train)), f"匯入訓練片段 {i + 1}/{len(train)}")
        added += _segment(voice_id, root, c, approve)
    groups = phrase_groups(clips)
    prefer = "sep" if bgm == "sep" else "clean"
    n_ph, n_ph_clips, problems, too_long = 0, 0, [], []
    for i, (text, g) in enumerate(groups.items()):
        progress(0.72 + 0.15 * i / max(1, len(groups)), f"口頭禪與常用語 {i + 1}/{len(groups)}")
        chosen = pick([c for c in g["clips"] if c.complete], phrase_clips, prefer)
        if not chosen:  # only cut-off recordings of this sentence
            continue
        ph = _phrase(voice_id, text, g["variants"], g["lang"])
        if ph is None:
            too_long.append(text)
            continue
        n_ph += 1
        k, bad = _add_clips(ph, chosen, root)
        n_ph_clips += k
        problems += bad
    sounds = sound_groups(clips)
    n_snd, n_snd_clips = 0, 0
    for i, (tag, cl) in enumerate(sounds.items()):
        progress(0.87 + 0.08 * i / max(1, len(sounds)), f"聲音標籤 {i + 1}/{len(sounds)}")
        ph = _phrase(voice_id, tag, [], None)
        if ph is None:
            continue
        n_snd += 1
        k, bad = _add_clips(ph, pick(cl, phrase_clips, "clean"), root)  # breaths suffer most from music removal
        n_snd_clips += k
        problems += bad
    ds = None
    ds_error = ""
    if build:
        progress(0.96, "建立資料集")
        try:
            ds = datasets.build(voice_id, f"{root.name} 交付 {time.strftime('%Y-%m-%d %H:%M')}")
        except (ValueError, datasets.ConsentMissing) as e:
            ds_error = str(e)
    approved = db.connect().execute(
        "SELECT COUNT(*), COALESCE(SUM(duration),0) FROM segments WHERE voice_id=? AND status='approved'",
        (voice_id,)).fetchone()
    pending = db.connect().execute(
        "SELECT COUNT(*) FROM segments WHERE voice_id=? AND status='pending'", (voice_id,)).fetchone()[0]
    msg = (f"匯入 {added} 段訓練片段（這個聲音共 {approved[0]} 段已核可、{approved[1] / 3600:.2f} 小時），"
           f"{n_ph} 句口頭禪／常用語（{n_ph_clips} 段原音），{n_snd} 個聲音標籤（{n_snd_clips} 段）")
    if ds:
        msg += f"；已建立資料集「{ds['name']}」"
    return {"message": msg, "added": added, "skipped": skipped, "approved": approved[0],
            "approved_hours": round(approved[1] / 3600, 3), "pending": pending,
            "phrases": n_ph, "phrase_clips": n_ph_clips, "sounds": n_snd, "sound_clips": n_snd_clips,
            "too_long": too_long[:20], "problems": problems[:30], "n_problems": len(problems),
            "dataset_id": ds["id"] if ds else None, "dataset_error": ds_error, "voice_id": voice_id}


@jobs.handler("import_delivery", queue="gpu")
def import_delivery(ctx: jobs.JobContext) -> dict:
    p = ctx.params
    return run(p["path"], p["voice_id"], p.get("bgm", "sep"), p.get("common", True), int(p.get("phrase_clips", 8)),
               p.get("approve", True), p.get("build", True), progress=ctx.progress)

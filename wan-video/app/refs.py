"""Official reference art, filed per character, ready to drive a generation.

The single biggest gap in this project - named as much by an outside review as
by the user's own results - is that everything steers a character through
*words*. Words average. danbooru holds 1-3% official art for these characters,
so a character tag reproduces a fan consensus and no amount of prompt tuning
turns that into the reference sheet.

A picture does not average. Feed the official art in as an actual image - as an
img2img source, or through ControlNet - and the model has the real proportions,
the real hair, the real costume in front of it.

So this module does the boring part that stands between "I downloaded 400
official images" and "the right one is one click away":

  * files them per character, per pack
  * matches a downloaded filename to a character, which is the whole trick -
    `Mori Calliope - 1st Costume.png`, `hoshimachi_suisei_03.jpg` and
    `星街すいせい.png` all have to land on the right person
  * keeps what it could not match, visibly, instead of dropping it silently

Matching is deliberately conservative. A wrong match is worse than no match:
an unmatched file sits in a list you can assign by hand in a second, while a
wrongly matched one quietly puts Marine's reference on Noel's card and you find
out three generations later.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
MAX_BYTES = 40 * 1024 * 1024
# A filename has to clear this to count as a match. Deliberately high: see the
# module docstring on why a wrong match costs more than a miss.
MIN_SCORE = 0.62


@dataclass
class Ref:
    """One reference image on disk."""

    name: str                  # filename inside the character's folder
    character: str             # pack character key, "" for unfiled
    pack: str = ""
    original: str = ""         # what it was called when it arrived
    width: int = 0
    height: int = 0
    bytes: int = 0
    added: float = field(default_factory=time.time)
    note: str = ""

    def public(self, url_base: str) -> dict:
        return {
            "name": self.name, "character": self.character, "pack": self.pack,
            "original": self.original, "width": self.width, "height": self.height,
            "bytes": self.bytes, "added": self.added, "note": self.note,
            "url": f"{url_base}/{self.pack}/{self.character or '_unfiled'}/{self.name}",
        }


# -- matching a downloaded filename to a character ---------------------------

_DROP = re.compile(r"\.(png|jpe?g|webp|bmp)$", re.I)
_SEP = re.compile(r"[\s_\-.,()\[\]{}#@!+~]+")
# Numbering a downloader adds: "suisei (3)", "suisei_03", "suisei-1920x1080".
_NOISE = re.compile(
    r"\b(?:\d{1,4}x\d{1,4}|v\d+|\d{1,3}|full|hd|hi?res|large|small|thumb|"
    r"official|art|illustration|render|transparent|png|jpg|wallpaper|"
    r"portrait|render|clean|cropped|copy|final)\b", re.I)


def normalise(text: str) -> str:
    """Filename -> comparable words. Width-insensitive, punctuation-free."""
    text = unicodedata.normalize("NFKC", _DROP.sub("", text or ""))
    text = _SEP.sub(" ", text)
    text = _NOISE.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def _tokens(text: str) -> list[str]:
    """Words for latin text; per-character for CJK, which has no spaces."""
    out: list[str] = []
    for word in normalise(text).split():
        if re.search(r"[぀-ヿ一-鿿]", word):
            out.extend(word)
        else:
            out.append(word)
    return [t for t in out if t]


def _score(needle: list[str], hay: list[str]) -> float:
    """How much of `needle` appears in `hay`, order-insensitive.

    Scored against the *character's* name rather than the filename, so a long
    filename full of extra words cannot dilute a complete name match - which is
    exactly the shape a downloaded file has.
    """
    if not needle:
        return 0.0
    have = list(hay)
    hits = 0
    for token in needle:
        if token in have:
            have.remove(token)
            hits += 1
    return hits / len(needle)


@dataclass(frozen=True)
class Candidate:
    key: str
    names: tuple[str, ...]


def candidates_from_pack(pack) -> list[Candidate]:
    """Every name a pack character might be filed under."""
    out = []
    for who in pack.characters:
        names = [who.name, who.key.replace("-", " ")]
        if getattr(who, "jp", ""):
            names.append(who.jp)
        # The costume trigger carries the danbooru spelling, which is what a
        # file scraped from a booru is most likely to be named after.
        for costume in who.costumes:
            first = costume.trigger.split(",")[0].replace("\\", "").strip()
            if first:
                names.append(first)
        out.append(Candidate(who.key, tuple(dict.fromkeys(names))))
    return out


def match(filename: str, candidates: list[Candidate]) -> tuple[str, float]:
    """(character key, score). Empty key means "leave it unfiled"."""
    hay = _tokens(filename)
    if not hay:
        return "", 0.0
    # Best score *per character*, not per name. Scoring every alias into one
    # flat ranking made the runner-up a different spelling of the winner - a
    # character's own name and its costume trigger both score 1.00 - so the
    # ambiguity guard below rejected every clean match it was meant to allow.
    # Score, and remember whether the winning alias was the character's *own*
    # name or merely a costume trigger. That distinction settles a real case:
    # Pekomama's trigger contains "usada pekora" (danbooru tags mother and
    # daughter together), so a file called "Usada Pekora.png" matches both
    # perfectly. Pekora matches on her own name; Pekomama only on an alias.
    best_by_key: dict[str, tuple[float, int]] = {}
    for cand in candidates:
        top, primary = 0.0, 0
        for i, name in enumerate(cand.names):
            score = _score(_tokens(name), hay)
            # names[0] is the display name, names[1] the key spelled out; both
            # are the character herself rather than an outfit.
            is_primary = 1 if i < 2 else 0
            if (score, is_primary) > (top, primary):
                top, primary = score, is_primary
        if (top, primary) > best_by_key.get(cand.key, (0.0, 0)):
            best_by_key[cand.key] = (top, primary)
    if not best_by_key:
        return "", 0.0
    ranked = [(k, v[0]) for k, v in
              sorted(best_by_key.items(), key=lambda kv: (-kv[1][0], -kv[1][1]))]
    best_key, best = ranked[0]
    runner_up = ranked[1][1] if len(ranked) > 1 else 0.0
    if best < MIN_SCORE:
        return "", best
    # Two *different* characters fitting equally well is exactly when a wrong
    # guess happens (Hololive shares plenty of given names), so decline.
    if best - runner_up < 0.15 and runner_up >= MIN_SCORE:
        # Unless the leader matched on her own name and the rival only on an
        # outfit alias - then it is not really ambiguous.
        leader_primary = best_by_key[best_key][1]
        rival = ranked[1][0]
        if not (leader_primary and not best_by_key[rival][1]):
            return "", best
    return best_key, best


# -- the store ---------------------------------------------------------------


class RefLibrary:
    """Reference images on disk, indexed by pack and character."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.index = root / ".refs.jsonl"
        self.refs: list[Ref] = []

    def load(self) -> None:
        self.refs = []
        if not self.index.is_file():
            return
        for line in self.index.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                self.refs.append(Ref(**json.loads(line)))
            except Exception:
                continue          # one bad line must not lose the rest
        # Anything deleted from disk by hand should stop being listed.
        self.refs = [r for r in self.refs if self.path(r).is_file()]

    def save(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        tmp = self.index.with_suffix(".tmp")
        tmp.write_text(
            "".join(json.dumps(r.__dict__, ensure_ascii=False) + "\n" for r in self.refs),
            encoding="utf-8")
        tmp.replace(self.index)

    def folder(self, pack: str, character: str) -> Path:
        return self.root / _safe(pack) / _safe(character or "_unfiled")

    def path(self, ref: Ref) -> Path:
        return self.folder(ref.pack, ref.character) / ref.name

    def for_character(self, pack: str, character: str) -> list[Ref]:
        return [r for r in self.refs if r.pack == pack and r.character == character]

    def unfiled(self, pack: str = "") -> list[Ref]:
        return [r for r in self.refs
                if not r.character and (not pack or r.pack == pack)]

    def counts(self, pack: str) -> dict[str, int]:
        out: dict[str, int] = {}
        for ref in self.refs:
            if ref.pack == pack and ref.character:
                out[ref.character] = out.get(ref.character, 0) + 1
        return out

    def add(self, data: bytes, filename: str, pack: str,
            candidates: list[Candidate], *, character: str | None = None) -> Ref:
        """File one image. `character=None` means "work it out from the name"."""
        if len(data) > MAX_BYTES:
            raise ValueError(f"{filename} 太大了（>{MAX_BYTES // 1024 // 1024}MB）")
        suffix = Path(filename).suffix.lower()
        if suffix not in IMAGE_SUFFIXES:
            raise ValueError(f"{filename} 不是圖片")
        key = character if character is not None else match(filename, candidates)[0]
        width, height = _size(data)
        # Content hash for the stored name: re-importing the same picture twice
        # should not make a second copy, and a downloaded set is full of dupes.
        digest = hashlib.sha1(data).hexdigest()[:12]
        name = f"{digest}{suffix}"
        existing = next((r for r in self.refs
                         if r.name == name and r.pack == pack), None)
        if existing is not None:
            if character is not None and existing.character != character:
                self.assign(existing, character)
            # Flagged so the caller can report "already had this one" instead of
            # counting the same picture twice. A downloaded set is full of
            # duplicates, and a count that inflates is a count you cannot use to
            # check whether the import actually worked.
            existing.note = "duplicate"
            return existing
        
        ref = Ref(name=name, character=key, pack=pack, original=filename,
                  width=width, height=height, bytes=len(data), note="new")
        folder = self.folder(pack, key)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / name).write_bytes(data)
        self.refs.append(ref)
        return ref

    def assign(self, ref: Ref, character: str) -> Ref:
        """Move a reference to a different character (or to unfiled)."""
        old = self.path(ref)
        ref.character = character
        new_folder = self.folder(ref.pack, character)
        new_folder.mkdir(parents=True, exist_ok=True)
        if old.is_file():
            shutil.move(str(old), str(new_folder / ref.name))
        return ref

    def delete(self, pack: str, name: str) -> bool:
        ref = next((r for r in self.refs if r.pack == pack and r.name == name), None)
        if ref is None:
            return False
        path = self.path(ref)
        if path.is_file():
            path.unlink()
        self.refs.remove(ref)
        return True

    def get(self, pack: str, name: str) -> Ref | None:
        return next((r for r in self.refs if r.pack == pack and r.name == name), None)


_UNSAFE = re.compile(r"[^A-Za-z0-9._-]")


def _safe(text: str) -> str:
    """One path component that cannot be anything but a name.

    Stripping separators is not enough on its own: `.` is a legal filename
    character, so `..` survived the substitution intact and `root / ".." / ".."`
    walked straight out of the refs folder. The pack id arrives in the URL
    (`/api/refs/{pack}/...`), so that was reachable, not theoretical.
    """
    cleaned = _UNSAFE.sub("_", text or "")[:64]
    # Any component that is only dots is traversal or the current directory.
    if not cleaned or set(cleaned) <= {"."}:
        return "_"
    return cleaned


def _size(data: bytes) -> tuple[int, int]:
    try:
        import io

        from PIL import Image

        with Image.open(io.BytesIO(data)) as im:
            return im.size
    except Exception:
        return (0, 0)

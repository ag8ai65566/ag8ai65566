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

import refnames

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
    # Where the file actually lives when it was indexed in place rather than
    # copied. An organised archive is the user's own filing system and can run
    # to several gigabytes; copying it would double that for no gain, and it
    # would also fork the truth - fix a filename in the archive and the copy
    # still has the old one. Empty means the bytes live under the refs folder.
    source: str = ""

    @property
    def linked(self) -> bool:
        return bool(self.source)

    def public(self, url_base: str) -> dict:
        return {
            "name": self.name, "character": self.character, "pack": self.pack,
            "original": self.original, "width": self.width, "height": self.height,
            "bytes": self.bytes, "added": self.added, "note": self.note,
            "linked": self.linked, "source": self.source,
            # A linked file is not under the static mount, so it is served
            # through a route that looks it up in the index - which also means
            # the route cannot reach anything the index does not know about.
            "url": (f"/api/refs/file/{self.pack}/{self.name}" if self.source else
                    f"{url_base}/{self.pack}/{self.character or '_unfiled'}/{self.name}"),
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


_CJK = re.compile(r"[぀-ヿ㐀-鿿]")


def _is_cjk_name(name: str) -> bool:
    """A name written in Han/kana, which has no word boundaries to lean on."""
    letters = [c for c in name if c.isalnum()]
    if not letters:
        return False
    return sum(1 for c in letters if _CJK.match(c)) >= len(letters) * 0.6


def _score_cjk(name: str, text: str) -> float:
    """CJK names are matched as a contiguous run, not as a bag of characters.

    Tokenising `律可` into `律` and `可` and asking how many appear anywhere in
    the filename is how a two-character name matches almost everything: those
    characters are common, and order is exactly what distinguishes a name from a
    coincidence. Han has no spaces, so substring containment is the word
    boundary - `星街彗星` has to appear as those four characters in that order.
    """
    needle = "".join(c for c in unicodedata.normalize("NFKC", name) if c.isalnum())
    hay = "".join(c for c in unicodedata.normalize("NFKC", text) if c.isalnum())
    if not needle:
        return 0.0
    if needle.lower() in hay.lower():
        return 1.0
    # A partial run still counts, so `星街すいせい` scores against `星街彗星` -
    # the two spellings share a surname. Below MIN_SCORE it decides nothing.
    best = 0
    for start in range(len(needle)):
        for end in range(len(needle), start + best, -1):
            if needle[start:end].lower() in hay.lower():
                best = max(best, end - start)
                break
    return best / len(needle)


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
    # How many leading entries of `names` are the character's own names rather
    # than costume triggers. See `match` for why the distinction settles a real
    # ambiguity (Pekomama's trigger contains "usada pekora").
    primary: int = 2


def candidates_from_pack(pack) -> list[Candidate]:
    """Every name a pack character might be filed under.

    Order matters: the first two entries are treated as the character's *own*
    name by `match`, everything after is an alias. Chinese names go in that
    primary group too - a collection organised by a Chinese speaker names the
    folder `星街彗星`, and that is no less the person's name than `Hoshimachi
    Suisei` is.
    """
    out = []
    for who in pack.characters:
        names = [who.name, who.key.replace("-", " ")]
        if getattr(who, "jp", ""):
            names.append(who.jp)
        zh = refnames.names_for(who.key)
        names.extend(zh)
        # The costume trigger carries the danbooru spelling, which is what a
        # file scraped from a booru is most likely to be named after.
        primary = len(dict.fromkeys(names))
        for costume in who.costumes:
            first = costume.trigger.split(",")[0].replace("\\", "").strip()
            if first:
                names.append(first)
        out.append(Candidate(who.key, tuple(dict.fromkeys(names)), primary))
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
            score = (_score_cjk(name, filename) if _is_cjk_name(name)
                     else _score(_tokens(name), hay))
            # Everything before the costume triggers is the character herself
            # rather than an outfit: display name, key, Japanese name, Chinese
            # names. `primary_count` is recorded per candidate when it is built,
            # because how many of those there are varies per member.
            is_primary = 1 if i < cand.primary else 0
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


def match_path(rel_path: str, candidates: list[Candidate]) -> tuple[str, float, str]:
    """(character key, score, which part of the path decided it).

    An organised archive puts the name in the folder, not always in the file:
    `01_官方角色全身立繪/星街彗星/01.png` has a filename that says nothing. So the
    filename is tried first - it is the most specific - and only if that comes
    back empty are the folders tried, nearest first.

    Combining the whole path into one bag of words instead would be worse: a top
    folder named after one member would then bleed into every file under it, and
    a nested "with 星街彗星" collab folder would outvote the filename.
    """
    parts = [x for x in re.split(r"[\\/]+", rel_path or "") if x and x not in (".", "..")]
    if not parts:
        return "", 0.0, ""
    key, score = match(parts[-1], candidates)
    if key:
        return key, score, parts[-1]
    for folder in reversed(parts[:-1]):
        key, score = match(folder, candidates)
        if key:
            return key, score, folder
    return "", score, ""


@dataclass
class ScanRow:
    """One file a scan looked at, and what it would do with it."""

    rel: str
    character: str
    score: float
    decided_by: str
    bytes: int
    skip: str = ""          # why it would not be imported at all

    def public(self) -> dict:
        return {
            "rel": self.rel, "character": self.character,
            "score": round(self.score, 3), "decided_by": self.decided_by,
            "bytes": self.bytes, "skip": self.skip,
        }


MAX_SCAN = 20000


def scan(root: Path, candidates: list[Candidate], *, limit: int = MAX_SCAN
         ) -> tuple[list[ScanRow], list[str]]:
    """Walk a folder and say what an import would do. Reads nothing but names.

    This is a dry run on purpose. An archive is somebody's own filing system,
    the matcher has never seen its naming convention, and the honest way to find
    out whether it works is to show the answer before touching anything.
    """
    rows: list[ScanRow] = []
    problems: list[str] = []
    if not root.is_dir():
        return rows, [f"找不到這個資料夾：{root}"]
    seen = 0
    for path in sorted(root.rglob("*")):
        if seen >= limit:
            problems.append(f"超過 {limit} 個檔案，只看了前面這些")
            break
        if path.is_dir() or path.is_symlink():
            continue
        rel = str(path.relative_to(root))
        suffix = path.suffix.lower()
        if suffix not in IMAGE_SUFFIXES:
            continue
        seen += 1
        try:
            size = path.stat().st_size
        except OSError as exc:
            problems.append(f"{rel}: 讀不到（{type(exc).__name__}）")
            continue
        skip = "" if size <= MAX_BYTES else f"太大（{size // 1024 // 1024}MB）"
        key, score, by = match_path(rel, candidates)
        rows.append(ScanRow(rel=rel, character=key, score=score,
                            decided_by=by, bytes=size, skip=skip))
    return rows, problems


def scan_summary(rows: list[ScanRow]) -> dict:
    matched = [r for r in rows if r.character and not r.skip]
    unmatched = [r for r in rows if not r.character and not r.skip]
    skipped = [r for r in rows if r.skip]
    per: dict[str, int] = {}
    for row in matched:
        per[row.character] = per.get(row.character, 0) + 1
    by_folder = sum(1 for r in matched if r.decided_by and
                    not r.rel.endswith(r.decided_by))
    return {
        "total": len(rows), "matched": len(matched), "unmatched": len(unmatched),
        "skipped": len(skipped), "characters": len(per),
        "by_folder": by_folder,
        "bytes": sum(r.bytes for r in rows if not r.skip),
        "counts": dict(sorted(per.items(), key=lambda kv: -kv[1])),
        # A sample of what did not match, because that is the only thing an
        # eyeball can act on - and because it is what a name table needs to be
        # fixed against real data instead of guesses.
        "unmatched_sample": [r.public() for r in unmatched[:40]],
        "skipped_sample": [r.public() for r in skipped[:10]],
    }


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
        if ref.source:
            return Path(ref.source)
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
        # match_path, not match: `filename` may be a relative path when this
        # comes from a folder import in copy mode, and in an organised archive
        # the member's name is on the folder rather than the file. A bare
        # filename is just a one-part path, so the upload route is unaffected.
        key = (character if character is not None
               else match_path(filename, candidates)[0])
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

    def add_path(self, path: Path, rel: str, pack: str,
                 candidates: list[Candidate], *, character: str | None = None,
                 copy: bool = False) -> Ref:
        """Index a file that already exists on disk.

        `copy=False` records where it is and leaves it there. That is the right
        default for a folder the user curated themselves: it is theirs, it may
        be several gigabytes, and duplicating it would fork the truth as well as
        the disk. The cost is that moving or renaming the archive breaks the
        link - `load()` drops any reference whose file has gone, so a broken
        link disappears from the list rather than 404ing from the UI.
        """
        size = path.stat().st_size
        if size > MAX_BYTES:
            raise ValueError(f"{rel} 太大了（>{MAX_BYTES // 1024 // 1024}MB）")
        if path.suffix.lower() not in IMAGE_SUFFIXES:
            raise ValueError(f"{rel} 不是圖片")
        if copy:
            return self.add(path.read_bytes(), rel, pack, candidates,
                            character=character)
        if character is not None:
            key = character
        else:
            key = match_path(rel, candidates)[0]
        # Identity is the absolute path here, not a content hash: hashing means
        # reading every byte of the archive, which is the cost this mode exists
        # to avoid. Re-scanning the same folder therefore updates rather than
        # duplicates.
        resolved = str(path.resolve())
        existing = next((r for r in self.refs
                         if r.pack == pack and r.source == resolved), None)
        if existing is not None:
            if character is not None and existing.character != character:
                existing.character = character
            existing.note = "duplicate"
            return existing
        width, height = _size_of(path)
        ref = Ref(name=_link_name(resolved, path.suffix.lower()), character=key,
                  pack=pack, original=rel, width=width, height=height,
                  bytes=size, note="new", source=resolved)
        self.refs.append(ref)
        return ref

    def assign(self, ref: Ref, character: str) -> Ref:
        """Move a reference to a different character (or to unfiled).

        A linked reference is only re-labelled: the file belongs to the user's
        own archive, and a filing tool that silently reorganises the folder it
        was pointed at is a filing tool nobody points at twice.
        """
        if ref.source:
            ref.character = character
            return ref
        old = self.path(ref)
        ref.character = character
        new_folder = self.folder(ref.pack, character)
        new_folder.mkdir(parents=True, exist_ok=True)
        if old.is_file():
            shutil.move(str(old), str(new_folder / ref.name))
        return ref

    def delete(self, pack: str, name: str) -> bool:
        """Forget a reference. A linked file is never deleted from the archive."""
        ref = next((r for r in self.refs if r.pack == pack and r.name == name), None)
        if ref is None:
            return False
        if not ref.source:
            path = self.path(ref)
            if path.is_file():
                path.unlink()
        self.refs.remove(ref)
        return True

    def import_folder(self, root: Path, pack: str, candidates: list[Candidate],
                      *, copy: bool = False, only_matched: bool = False,
                      limit: int = MAX_SCAN) -> dict:
        """Run a scan and act on it. Returns the same shape the dry run does."""
        rows, problems = scan(root, candidates, limit=limit)
        filed = unfiled = dupes = 0
        for row in rows:
            if row.skip:
                continue
            if only_matched and not row.character:
                continue
            try:
                ref = self.add_path(root / row.rel, row.rel, pack, candidates,
                                    copy=copy)
            except (ValueError, OSError) as exc:
                problems.append(f"{row.rel}: {exc}")
                continue
            if ref.note == "duplicate":
                dupes += 1
            elif ref.character:
                filed += 1
            else:
                unfiled += 1
        return {"filed": filed, "unfiled": unfiled, "dupes": dupes,
                "problems": problems[:20], **scan_summary(rows)}

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


def _link_name(resolved: str, suffix: str) -> str:
    """A stable id for a linked file. The path is the identity, so hash that."""
    return hashlib.sha1(resolved.encode("utf-8")).hexdigest()[:12] + suffix


def _size_of(path: Path) -> tuple[int, int]:
    """Dimensions without loading the pixels - PIL reads only the header."""
    try:
        from PIL import Image

        with Image.open(path) as im:
            return im.size
    except Exception:
        return (0, 0)


def _size(data: bytes) -> tuple[int, int]:
    try:
        import io

        from PIL import Image

        with Image.open(io.BytesIO(data)) as im:
            return im.size
    except Exception:
        return (0, 0)

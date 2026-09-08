"""A pose and action prompt database, classified and one click away.

The input is a community "codex" - a long document where every entry is a named
action with a tested tag string, an author, a negative list and notes. Those
documents are the real working knowledge of this hobby, and they are also
completely unusable as documents: 288 entries in one file, written in NovelAI
syntax, with the artist tags of whoever tested each entry baked into the middle
of every tag string.

So three things happen on the way in:

1. **Structure.** The category tree in the document (10 groups, 89 sections,
   288 entries) is kept, because it is a real taxonomy and it is how anyone
   navigates this - by what the pose *is*, not by searching text.

2. **Weights are translated.** The tag strings are NAI syntax, which ComfyUI
   ignores almost entirely - see naiweights.py for what that costs. Every
   string is converted so the weights the author tested actually apply.

3. **Artists are pulled out separately.** This is the point the user asked for
   and it matters more than it looks: the artist tags in a codex entry are
   *the tester's* style choices, not part of the pose. Left in, they fight
   whatever the user picked in the character pack, and a Hololive designer's
   style gets overwritten by a stranger's. Pulled out, they become an optional
   group with its own weight - keep them, drop them, or swap in your own.

The shipped database is built from the document once by scripts/build-posebook.py
and committed as JSON, so the app needs no parsing at startup and the user needs
no import step. The parser stays here because these codices get revised (this
one is dated 2026.5.27) and the next version should not need code changes.

Nothing here is invented. Titles, authors, notes and tags are verbatim from the
source document, including its typos - with the single exception of `aritst:`,
which is corrected because a misspelt prefix silently disables the artist.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import naiweights

POSES_DIR = Path(__file__).parent / "poses"

# Tags that put a minor in the frame. Entries carrying these are dropped, and
# the count is reported rather than hidden, because a database that quietly
# differs from its source document is worse than one that says what it left out.
#
# Matching is on whole tags, not substrings, so `lolita fashion` and `qi lolita`
# (clothing styles) and `child of light` survive while `child` does not.
BLOCKED_TAGS = {
    "shota", "child", "toddler", "aged down", "aged-down", "loli", "lolicon",
    "shotacon", "toddlercon", "infant", "baby", "kindergartener", "todler",
    "young child", "little girl", "little boy", "preteen", "prepubescent",
}
# Some entries are sexual and some are a costume list; a kindergarten uniform on
# an adult character is the latter. Only the sexual combination is the problem,
# so the age tags above are what gets matched - not the clothing.


@dataclass
class Variant:
    """One tag string for a pose. Most poses have one; some have alternates."""

    label: str = ""            # "着衣版", "无衣版" … "" for the main string
    raw: str = ""              # verbatim, so the conversion stays auditable
    prompt: str = ""           # converted, artists removed
    artists: str = ""          # converted artist tokens only
    artist_names: list[str] = field(default_factory=list)
    negative: str = ""         # what a negative NAI weight had to become
    notes: list[str] = field(default_factory=list)
    # Slots the author deliberately left blank for the user to fill.
    placeholders: list[str] = field(default_factory=list)
    # The cast the tester happened to use. Separated for the same reason the
    # artists are: it is not part of the pose, and left in it silently replaces
    # whoever the user actually asked for.
    characters: str = ""
    character_names: list[str] = field(default_factory=list)

    def public(self) -> dict:
        return {
            "label": self.label, "raw": self.raw, "prompt": self.prompt,
            "artists": self.artists, "artist_names": list(self.artist_names),
            "negative": self.negative, "notes": list(self.notes),
            "placeholders": list(self.placeholders),
            "characters": self.characters,
            "character_names": list(self.character_names),
        }


@dataclass
class Pose:
    id: str
    title: str
    group: str = ""
    section: str = ""
    author: str = ""
    note: str = ""
    negative: str = ""         # the entry's own 负面 Tag, converted
    variants: list[Variant] = field(default_factory=list)

    @property
    def artists(self) -> str:
        """The tester's artist run, for the whole entry.

        In this document the canonical `主要 Tag` string is always the
        artist-free one and the artist run lives on `Tag 1`/`Tag 2`, so *no*
        entry has artists on the version shown first. Modelled strictly
        per-variant, the "bring the artists in" switch therefore did nothing on
        every single pose until you first clicked a different version - it read
        as a broken checkbox, and that is how the browser test found it.

        Treating the run as belonging to the entry is also the truer model: the
        variants of one entry are the same pose from the same tester, and where
        more than one carries artists they are the same names 32 times out of 40.
        """
        return next((v.artists for v in self.variants if v.artists), "")

    @property
    def artists_from(self) -> str:
        """Which version the entry-level artist run was taken from."""
        v = next((v for v in self.variants if v.artists), None)
        return (v.label or "主要版本") if v else ""

    @property
    def people(self) -> str:
        """The group name doubles as a head-count, which is worth surfacing."""
        return PEOPLE.get(_head(self.group), "")

    def public(self) -> dict:
        return {
            "id": self.id, "title": self.title, "group": self.group,
            "section": self.section, "author": self.author, "note": self.note,
            "negative": self.negative, "people": self.people,
            "variants": [v.public() for v in self.variants],
            "artist_names": sorted({n for v in self.variants for n in v.artist_names}),
            "character_names": sorted({n for v in self.variants
                                       for n in v.character_names}),
            "artists": self.artists,
            "artists_from": self.artists_from,
        }


@dataclass
class Codex:
    id: str = ""
    name: str = ""
    source: str = ""
    note: str = ""
    advice: list[str] = field(default_factory=list)
    poses: list[Pose] = field(default_factory=list)
    skipped: int = 0           # entries dropped by BLOCKED_TAGS
    skipped_variants: int = 0

    def public(self) -> dict:
        return {
            "id": self.id, "name": self.name, "source": self.source,
            "note": self.note, "advice": list(self.advice),
            "count": len(self.poses), "skipped": self.skipped,
            "skipped_variants": self.skipped_variants,
            "groups": [
                {
                    "label": g,
                    "people": PEOPLE.get(_head(g), ""),
                    "sections": [
                        {"label": s, "poses": [p.public() for p in items]}
                        for s, items in _by_section(g, self.poses)
                    ],
                }
                for g in _groups(self.poses)
            ],
            "artists": self.artist_index(),
        }

    def get(self, pose_id: str) -> Pose | None:
        return next((p for p in self.poses if p.id == pose_id), None)

    def artist_index(self) -> list[dict]:
        """Every artist named anywhere, and how many entries use them.

        The user asked for the artist tags to be separated out; this is the
        other half of that - once separated they can be read as a list, which
        is the fastest way to find a style worth reusing.
        """
        counts: dict[str, int] = {}
        for pose in self.poses:
            for name in {n for v in pose.variants for n in v.artist_names}:
                counts[name] = counts.get(name, 0) + 1
        return [{"name": n, "uses": c}
                for n, c in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]


# The document's group names are also a head-count, which is the single most
# useful filter ("show me the solo ones"), so it is read out rather than left
# buried in a Chinese ordinal.
PEOPLE = {
    "单男单女": "1男1女", "单男多女": "1男多女", "多男单女": "多男1女",
    "多男多女": "多男多女", "单男": "單男", "单女": "單女",
    "非人": "非人", "百合": "百合（女女）", "基佬": "男男", "杂项": "雜項",
}

_GROUP = re.compile(r"^##\s+(?P<label>[^\s#].*?)\s*$")
_SECTION = re.compile(r"^###\s+(?P<label>[^\s#].*?)\s*$")
_ENTRY = re.compile(r"^####\s+(?P<label>[^\s#].*?)\s*$")
_FIELD = re.compile(r"^(?P<key>[^:：]{1,20})\s*[:：]\s*(?P<value>.*)$")

# The document's own group headings are numbered with Chinese ordinals; the body
# of the name is what carries meaning.
_ORDINAL = re.compile(r"^[一二三四五六七八九十]+、\s*")
# "（暂无）" and similar parentheticals on a heading are status, not name.
_STATUS = re.compile(r"[（(](?:暂无|暫無|待补|待補)[）)]\s*$")

# Field labels that carry a tag string. `主要 Tag` is the canonical one; the
# rest are how the same idea got written elsewhere in the document.
TAG_KEYS = ("主要 Tag", "主要Tag", "主tag", "主Tag", "Tag 1", "Tag 2", "Tag1", "Tag2")
NEG_KEYS = ("负面 Tag", "负面Tag", "負面 Tag", "負面Tag")
NOTE_KEYS = ("备注", "備註")
AUTHOR_KEYS = ("作者",)
# Anything else naming a model version or a variant also holds tags: this
# document uses `nai4 版`, `nai4.5 版`, `4.5 版tag`, `无衣版`, `人物幼化版`.
_TAGGISH = re.compile(r"(版|tag)", re.I)


def is_tag_key(key: str) -> bool:
    key = key.strip()
    if key in TAG_KEYS:
        return True
    if key in NEG_KEYS or key in NOTE_KEYS or key in AUTHOR_KEYS:
        return False
    return bool(_TAGGISH.search(key))

# Inline alternates: one tag line often carries several versions, separated by a
# Chinese label. The document is not consistent about how those look - `着衣版:`,
# `一口一舔版本:`, `特写脸:`, `背面：`, and one with no colon at all (`袜子版1girl`)
# - and every label this misses silently welds two prompts into one, which is
# both wrong and hard to notice. So the rule is structural: a short run
# containing Chinese, sitting at a tag boundary, before a colon.
#
# The negative lookahead is what keeps `(penis on 下身服装:1.5)` intact: there
# the colon introduces a *weight*, not a variant, and treating it as a label
# would cut the tag in half.
# Ideographs and kana only. The fullwidth-forms block (U+FF00-FFEF) must NOT be
# in here: it contains the fullwidth colon itself, so a label could match across
# its own delimiter - `着衣版：1girl` was read as the label `着衣版：1gir`, which
# then cut the following tag in half. It cost 33 variants, and the only reason it
# was caught is that the build script prints the variant count.
_CJK = r"\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
_INLINE = re.compile(
    r"(?:^|(?<=[,，:：\s]))\s*"
    r"(?P<label>[^,，:：\n]{0,11}[" + _CJK + r"][^,，:：\n]{0,11})"
    # A real label is followed by exactly one colon. Two colons is NAI4.5 weight
    # syntax closing (`1.5::penis on 下身服装::`) and a number is an SD
    # weight (`(penis on 下身服装:1.5)`); reading either as a label would
    # cut a tag in half and lose the weight the author tested.
    # A label is followed by exactly one colon. Two colons is NAI4.5 weight
    # syntax closing (`1.5::penis on 下身服装::`) and a number is an SD weight
    # (`(penis on 下身服装:1.5)`); reading either as a label would cut a tag
    # in half and lose the weight the author tested. The second branch is for
    # the one place the document omits the colon entirely (`uncensored 袜子版1girl`),
    # which is only safe to assume when the label ends in 版 ("version").
    r"\s*(?:[:：](?!:)(?!\s*-?\d+(?:\.\d+)?\s*\)?\s*(?:,|$))"
    r"|(?<=版)(?=[A-Za-z\d]))"
)
# Chinese inside a tag is the signal that matters. An earlier version keyed off
# "has no Latin letters" instead, which flagged half a dozen real danbooru tags
# as fill-in slots: `:>=`, `@_@`, `?`, `??` and `69` are all genuine tags with no
# letters in them. Chinese never appears in a danbooru tag, so its presence means
# either a slot the author left you or prose that leaked out of a note.
_CJK_RE = re.compile(r"[" + _CJK + r"]")


def _head(group: str) -> str:
    return _STATUS.sub("", _ORDINAL.sub("", group)).strip()


def _groups(poses: list[Pose]) -> list[str]:
    seen: list[str] = []
    for pose in poses:
        if pose.group not in seen:
            seen.append(pose.group)
    return seen


def _by_section(group: str, poses: list[Pose]) -> list[tuple[str, list[Pose]]]:
    out: list[tuple[str, list[Pose]]] = []
    for pose in poses:
        if pose.group != group:
            continue
        if not out or out[-1][0] != pose.section:
            out.append((pose.section, []))
        out[-1][1].append(pose)
    return out


def bare_tag(raw: str) -> str:
    """`(aged down:1.16)` -> `aged down`. One tag stripped of all syntax.

    Weighting brackets are peeled only when they wrap the whole tag. Stripping
    every trailing `)` instead - which is what this did first - eats the closing
    paren of a name, so `(shenhe \\(genshin impact\\):1.1)` came out as
    `shenhe (genshin impact`. That produced no wrong prompts, because this
    function only ever feeds comparisons, but it made every character tag look
    truncated in the data and would have broken any lookup keyed on the name.
    """
    tag = raw.strip().replace("\\(", "\x01").replace("\\)", "\x02")
    while True:
        m = re.fullmatch(r"[({\[]\s*(.*?)\s*[)}\]]", tag, re.S)
        if not m:
            break
        tag = m.group(1)
    tag = re.sub(r":\s*-?[\d.]+$", "", tag).strip()
    tag = tag.replace("\x01", "(").replace("\x02", ")").replace("_", " ")
    return re.sub(r"\s+", " ", tag).strip().lower()


# A parenthesised suffix on a danbooru tag is usually the series a character is
# from - which is exactly what makes it a character tag. These are the suffixes
# that are *not*: danbooru's disambiguation qualifiers. The list is the six that
# actually occur in this document (`portrait (object)`, `shrug (clothing)`,
# `piledriver (sex)`, `arrow (symbol)`, `amen pose (meme)`,
# `pom pom (cheerleading)`) plus three more that are common enough to expect.
QUALIFIERS = {
    "object", "clothing", "sex", "symbol", "meme", "cheerleading",
    "doll", "medium", "cosplay",
}

# Bare character names have no series suffix to give them away, so the ones this
# document uses as its demo cast are listed. Three of them are Hololive members,
# which is the clearest possible illustration of why this separation matters: the
# user generates Hololive, and leaving `houshou marine (1st costume)` in a pose
# string would put Marine in the picture no matter who they actually asked for.
DEMO_NAMES = {"hatsune miku", "higuchi madoka"}

_PAREN_SUFFIX = re.compile(r"^(?P<name>.+?)\s*\((?P<qualifier>[^()]*)\)$")


def is_character(tag: str, known_artists: set[str] | None = None) -> bool:
    """Is this converted chunk the tester's demo character rather than a pose?"""
    bare = bare_tag(tag)
    if not bare:
        return False
    if known_artists and bare in known_artists:
        # Two artists in this document lost their `artist:` prefix, and an
        # artist name looks exactly like a character name. If the same name
        # carries the prefix anywhere else in the same document, believe that.
        return False
    if bare in DEMO_NAMES:
        return True
    m = _PAREN_SUFFIX.match(bare)
    return bool(m and m.group("qualifier").strip() not in QUALIFIERS)


def blocked(text: str) -> bool:
    """Does this tag string put a minor in frame?

    Whole-tag matching, after stripping weighting syntax. Stripping is the part
    that has to be right: an earlier version of this ran one regex whose `$`
    anchor never fired on a wrapped tag, so `(aged down:1.16)` came out as
    `aged down:1.16`, matched nothing, and the filter passed a variant it was
    written to catch. Hence bare_tag, and hence the test that feeds it the
    weighted spellings rather than the bare ones.
    """
    for raw in re.split(r"[,\n]", text):
        if bare_tag(raw) in BLOCKED_TAGS:
            return True
    return False


def _slug(group: str, section: str, title: str, seen: set[str]) -> str:
    """A stable id that survives re-parsing the same document."""
    import hashlib

    base = hashlib.sha1(f"{group}|{section}|{title}".encode("utf-8")).hexdigest()[:10]
    slug = base
    n = 2
    while slug in seen:
        slug = f"{base}-{n}"
        n += 1
    seen.add(slug)
    return slug


# A version marker belongs to the label; an ordinary word before it does not.
# `nai4 版`, `nai4.5 版` and `4.5 版tag` are labels in full; `uncensored 着衣版`
# is the tag `uncensored` followed by the label `着衣版`.
_VERSION = re.compile(r"^(?:nai)?\d+(?:\.\d+)?$", re.I)
_SPACE_THEN_CJK = re.compile(r"\s+(?=[" + _CJK + r"])")


def _peel_label(label: str) -> tuple[str, str]:
    """`uncensored 着衣版` -> ("uncensored", "着衣版").

    Without this the whole thing became the label, which quietly deleted a tag
    from the *previous* variant - 35 of them, `uncensored` most often, plus
    `quality`, `shy`, `shoulder` and `collars`. Nothing failed; the prompts were
    just missing a tag they were tested with.
    """
    m = _SPACE_THEN_CJK.search(label)
    if not m or m.start() == 0:
        return "", label
    prefix = label[: m.start()].strip()
    if not prefix or _CJK_RE.search(prefix) or _VERSION.match(prefix):
        return "", label
    return prefix, label[m.end():].strip()


def _split_inline(value: str) -> list[tuple[str, str]]:
    """`a,b 着衣版:c,d` -> [("", "a,b"), ("着衣版", "c,d")]."""
    marks = list(_INLINE.finditer(value))
    if not marks:
        return [("", value)]
    out: list[tuple[str, str]] = []
    pending: list[str] = []          # tags peeled off the next label

    def add(label: str, body: str) -> None:
        body = ", ".join([*pending, body]) if pending else body
        pending.clear()
        body = body.strip().strip(",")
        if body:
            out.append((label, body))

    first = value[: marks[0].start()].strip().strip(",")
    peeled, label0 = _peel_label(marks[0].group("label"))
    if peeled:
        first = ", ".join(x for x in [first, peeled] if x)
    if first:
        out.append(("", first))
    labels = [label0]
    for m in marks[1:]:
        labels.append(m.group("label"))

    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(value)
        body = value[m.end():end].strip().strip(",")
        label = labels[i]
        # A tag peeled off the NEXT label belongs at the end of this body.
        if i + 1 < len(marks):
            nxt, labels[i + 1] = _peel_label(labels[i + 1])
            if nxt:
                body = ", ".join(x for x in [body, nxt] if x)
        add(label, body)
    return out or [("", value)]


def _clean_chunks(text: str, *, keep_placeholders: bool) -> tuple[str, list[str], list[str]]:
    """(cleaned, placeholders, prose) for one converted, comma-joined string.

    A chunk with no Latin letters is one of two very different things:

      * a slot the author left for you - `场景` (scene), `武器` (weapon),
        `下身服装` (lower-body clothing). All three say so in their entry's own
        note ("自己添加场景tag", "自行在武器添加tag", "自行将下身服装修改成你
        需要的服装"). Deleting those quietly removes the instruction along with
        the slot, so they are kept and reported for the UI to flag.
      * prose that leaked out of a note into a tag field - `n4 无需负面`,
        `用了也可以`, `.... 备注`. A model does nothing useful with that; it is
        conditioning noise, so it moves to the notes where it belongs.

    Which one applies follows from the field, not from guessing at the words:
    tag fields hold slots, the 负面 Tag field holds the leaked prose.
    """
    keep, placeholders, prose = [], [], []
    for chunk in _split_top(text):
        if not _CJK_RE.search(chunk):
            keep.append(chunk)
            continue
        if not keep_placeholders:
            # A negative tag list is pure danbooru vocabulary, so anything with
            # Chinese in it is a sentence that leaked out of the note field
            # ("n4 无需负面", "用了也可以"). Conditioning noise; move it.
            prose.append(chunk.strip())
            continue
        slot = bare_tag(chunk)
        keep.append(chunk)
        if slot:
            placeholders.append(slot)
    return ", ".join(keep), placeholders, prose


def _variant(label: str, raw: str, known_artists: set[str] | None = None) -> Variant:
    conv = naiweights.convert(raw)
    pose_chunks, cast_chunks = [], []
    for chunk in _split_top(conv.prompt(artists=False)):
        (cast_chunks if is_character(chunk, known_artists) else pose_chunks).append(chunk)
    prompt, slots, _ = _clean_chunks(", ".join(pose_chunks), keep_placeholders=True)
    negative, _, _ = _clean_chunks(conv.negative_prompt(), keep_placeholders=False)
    notes = list(conv.notes)
    if slots:
        notes.append("這串提詞有作者留給你自己填的空位：" + "、".join(dict.fromkeys(slots)))
    return Variant(
        label=label, raw=raw.strip(), prompt=prompt,
        artists=conv.artist_prompt(),
        artist_names=[c.artist_name for c in conv.artists],
        negative=negative, notes=notes,
        placeholders=list(dict.fromkeys(slots)),
        characters=", ".join(cast_chunks),
        character_names=[bare_tag(c) for c in cast_chunks],
    )


def parse_codex(text: str, *, codex_id: str = "codex", name: str = "",
                source: str = "") -> Codex:
    """A codex document -> a Codex. Never raises on odd input; skips instead."""
    lines = (text or "").replace("\r\n", "\n").replace("\r", "\n").split("\n")

    codex = Codex(id=codex_id, name=name, source=source)
    group = section = ""
    entry: dict[str, list[str]] | None = None
    title = ""
    seen: set[str] = set()
    started = False
    last_key = ""

    def finish() -> None:
        nonlocal entry, title
        if entry is not None and title:
            pose, dropped = _assemble(title, group, section, entry, seen)
            if pose is not None:
                codex.poses.append(pose)
            else:
                codex.skipped += 1
            codex.skipped_variants += dropped
        entry = None
        title = ""

    for line in lines:
        stripped = line.strip()

        m = _GROUP.match(stripped)
        if m:
            label = m.group("label")
            # The preamble uses `##` for prose sections too; the body starts at
            # the first ordinal-numbered heading.
            if _ORDINAL.match(label):
                finish()
                started = True
                group, section = label, ""
            continue
        if not started:
            continue

        m = _SECTION.match(stripped)
        if m:
            finish()
            section = m.group("label")
            continue

        m = _ENTRY.match(stripped)
        if m:
            label = m.group("label")
            # A "heading" that is really a labelled field belongs to the entry
            # above it. This document has one: entry 16's second tag string is
            # `4.5 版tag:1girl,...`, and whatever produced the .txt read the
            # leading "4.5" as a list number and emitted `#### 4.5 版tag:...`.
            # Taken at face value that both loses the variant and invents a
            # 287th entry with a tag string for a title.
            promoted = _FIELD.match(label)
            if entry is not None and promoted and "," in promoted.group("value"):
                last_key = promoted.group("key").strip()
                entry.setdefault(last_key, []).append(promoted.group("value"))
                continue
            finish()
            title = re.sub(r"^\d+[.、]\s*", "", label).strip()
            entry = {}
            last_key = ""
            continue

        if entry is None or not stripped:
            continue

        m = _FIELD.match(stripped)
        if m:
            last_key = m.group("key").strip()
            entry.setdefault(last_key, []).append(m.group("value"))
            continue

        # A continuation of the previous field. Long tag strings wrap when a PDF
        # text layer is extracted, and a wrapped tag list that gets dropped is a
        # silently truncated prompt - so it is appended rather than ignored.
        # Single stray characters are PDF artefacts (this document has 18 lone
        # "a" lines sitting between a heading and its 作者 line).
        if last_key and len(stripped) > 1:
            entry[last_key][-1] += " " + stripped

    finish()
    _reclaim_artists(codex)
    return codex


def _as_artist(chunk: str) -> str:
    """`(sho \\(sho lwlw\\):1.1)` -> `(artist:sho \\(sho lwlw\\):1.1)`."""
    m = re.fullmatch(r"\((?P<body>.+):(?P<w>-?[\d.]+)\)", chunk.strip())
    if m:
        return f"(artist:{m.group('body')}:{m.group('w')})"
    return "artist:" + chunk.strip()


def _reclaim_artists(codex: Codex) -> None:
    """Move names that are artists elsewhere in the document out of the cast.

    Two entries write an artist with no `artist:` prefix (`sho (sho lwlw)`,
    `noyu (noyu23386566)`), and a bare artist name is indistinguishable from a
    character name by shape alone. It is distinguishable by evidence, though:
    if the same name carries the prefix anywhere else in the same document, that
    settles it. This runs after the whole document is parsed because that is
    when the evidence is complete.
    """
    known = {n.strip().lower() for p in codex.poses
             for v in p.variants for n in v.artist_names}
    if not known:
        return
    for pose in codex.poses:
        for v in pose.variants:
            moved = [c for c in _split_top(v.characters) if bare_tag(c) in known]
            if not moved:
                continue
            kept = [c for c in _split_top(v.characters) if bare_tag(c) not in known]
            v.characters = ", ".join(kept)
            v.character_names = [bare_tag(c) for c in kept]
            # Give back the prefix the source forgot. Without it the token is
            # read as an ordinary tag and the artist has no effect at all, which
            # is the same failure as the `aritst:` typo.
            v.artists = ", ".join(x for x in [v.artists, *(_as_artist(c) for c in moved)] if x)
            v.artist_names = v.artist_names + [bare_tag(c) for c in moved]


def _assemble(title: str, group: str, section: str,
              fields: dict[str, list[str]], seen: set[str]) -> tuple[Pose | None, int]:
    author = " / ".join(v.strip() for k in AUTHOR_KEYS
                        for v in fields.get(k, []) if v.strip())
    note = " ".join(v.strip() for k in NOTE_KEYS
                    for v in fields.get(k, []) if v.strip())
    neg_raw = ", ".join(v.strip() for k in NEG_KEYS
                        for v in fields.get(k, []) if v.strip())
    negative, prose = "", []
    if neg_raw:
        # The negative field also carries inline labels (`只用于角色1:pov`), and
        # in a dozen entries it carries nothing but a sentence about whether a
        # negative is needed at all.
        joined = ", ".join(body for _, body in _split_inline(neg_raw))
        negative, _, prose = _clean_chunks(
            naiweights.convert(joined).prompt(), keep_placeholders=False)
    if prose:
        note = " ".join(x for x in [note, *prose] if x)

    variants: list[Variant] = []
    dropped = 0
    # Canonical tag fields first, then any variant field the document invented.
    keys = [k for k in TAG_KEYS if k in fields]
    keys += [k for k in fields if is_tag_key(k) and k not in keys]
    for key in keys:
        for value in fields[key]:
            for label, body in _split_inline(value):
                if not body.strip():
                    continue
                shown = label or ("" if key in ("主要 Tag", "主要Tag",
                                                 "主tag", "主Tag") else key)
                variant = _variant(shown, body)
                if blocked(variant.prompt) or blocked(variant.raw):
                    dropped += 1
                    continue
                # Once the demo cast is separated, several "variants" turn out
                # to be the same pose tested on a different character, so they
                # collapse - which is right. But the key has to include the
                # artist string: keying on the pose alone threw away the tested
                # artist run whenever a plain copy of the same pose came first.
                same = next((v for v in variants
                             if v.prompt == variant.prompt
                             and v.artists == variant.artists), None)
                if same is not None:
                    for name in variant.character_names:
                        if name not in same.character_names:
                            same.character_names.append(name)
                    continue
                variants.append(variant)

    if not variants:
        return None, dropped
    return Pose(
        id=_slug(group, section, title, seen), title=title, group=group,
        section=section, author=author, note=note, negative=negative,
        variants=variants,
    ), dropped


# -- the shipped database -----------------------------------------------------

_cache: dict[str, Codex] = {}


def _from_json(data: dict) -> Codex:
    codex = Codex(
        id=str(data.get("id", "")), name=str(data.get("name", "")),
        source=str(data.get("source", "")), note=str(data.get("note", "")),
        advice=[str(x) for x in data.get("advice", [])],
        skipped=int(data.get("skipped", 0)),
        skipped_variants=int(data.get("skipped_variants", 0)),
    )
    for raw in data.get("poses", []):
        codex.poses.append(Pose(
            id=str(raw.get("id", "")), title=str(raw.get("title", "")),
            group=str(raw.get("group", "")), section=str(raw.get("section", "")),
            author=str(raw.get("author", "")), note=str(raw.get("note", "")),
            negative=str(raw.get("negative", "")),
            variants=[Variant(
                label=str(v.get("label", "")), raw=str(v.get("raw", "")),
                prompt=str(v.get("prompt", "")), artists=str(v.get("artists", "")),
                artist_names=[str(x) for x in v.get("artist_names", [])],
                negative=str(v.get("negative", "")),
                notes=[str(x) for x in v.get("notes", [])],
                placeholders=[str(x) for x in v.get("placeholders", [])],
                characters=str(v.get("characters", "")),
                character_names=[str(x) for x in v.get("character_names", [])],
            ) for v in raw.get("variants", [])],
        ))
    return codex


def load_all(folder: Path | None = None) -> list[Codex]:
    base = folder or POSES_DIR
    key = str(base)
    if key in _cache:
        return _cache[key]  # type: ignore[return-value]
    out: list[Codex] = []
    if base.is_dir():
        for path in sorted(base.glob("*.json")):
            try:
                out.append(_from_json(json.loads(path.read_text(encoding="utf-8"))))
            except Exception:
                continue  # a broken file must not take the app down
    _cache[key] = out  # type: ignore[assignment]
    return out


def get(codex_id: str, folder: Path | None = None) -> Codex | None:
    return next((c for c in load_all(folder) if c.id == codex_id), None)


def clear_cache() -> None:
    _cache.clear()


# -- one-click prompt ---------------------------------------------------------

# The codex's own note 6: artist strings drag in chibi figures, and these four
# tags in the negative are what its authors use to stop that. Offered as a
# preset rather than forced, because it only applies when artists are on.
ARTIST_NEGATIVE = "chibi, chibi inset, doll, fumo \\(doll\\)"


def build_prompt(pose: Pose, variant: int = 0, *, artists: bool = False,
                 artist_weight: float = 1.0, cast: bool = False,
                 extra: str = "", head: str = "") -> dict:
    """The prompt for one pose, ready to paste.

    `head` is whatever identifies the cast the user actually wants - a character
    trigger out of a character pack. It goes first, then the artists, then the
    pose, which is the order the codex itself recommends (its note 4: character
    then artist, so the style locks before other tags can pull on it).

    Both `artists` and `cast` default to off. That is the whole design: what the
    codex tested with is recorded, but it does not travel into your prompt unless
    you ask for it, because `head` is usually the answer to "who is in this", and
    two competing characters at high weight is exactly the failure people report
    as "the pose came out right but it drew someone else".
    """
    if not pose.variants:
        return {"prompt": "", "negative": "", "notes": []}
    index = variant if 0 <= variant < len(pose.variants) else 0
    chosen = pose.variants[index]

    parts: list[str] = []
    if head.strip():
        parts.append(head.strip().strip(","))
    if cast and chosen.characters:
        parts.append(chosen.characters)
    # Fall back to the entry's run when this version has none of its own, or the
    # switch would silently do nothing on most poses.
    artist_run = chosen.artists or pose.artists
    if artists and artist_run:
        parts.append(_reweight(artist_run, artist_weight))
    if chosen.prompt:
        parts.append(chosen.prompt)
    if extra.strip():
        parts.append(extra.strip().strip(","))

    negatives = [chosen.negative, pose.negative]
    if artists and artist_run:
        negatives.append(ARTIST_NEGATIVE)

    return {
        "prompt": ", ".join(p for p in parts if p),
        "negative": ", ".join(dict.fromkeys(n for n in negatives if n)),
        "variant": chosen.label,
        "notes": list(chosen.notes),
        "placeholders": list(chosen.placeholders),
        "artists_used": _reweight(artist_run, artist_weight) if (artists and artist_run) else "",
        "artists_borrowed": bool(artists and artist_run and not chosen.artists),
        "artists_from": pose.artists_from if not chosen.artists else (chosen.label or "主要版本"),
    }


_TOKEN = re.compile(r"^\((?P<body>.+):(?P<weight>-?[\d.]+)\)$")


def _reweight(chunk: str, scale: float) -> str:
    """Scale every weight in an already-converted chunk.

    Used by the artist slider. Parsing back out of the rendered form keeps one
    representation rather than two, and the form is fixed and known because
    this module wrote it.
    """
    if abs(scale - 1.0) < 0.005:
        return chunk
    out = []
    for token in _split_top(chunk):
        m = _TOKEN.match(token.strip())
        if m:
            weight = naiweights.clamp(float(m.group("weight")) * scale)
            body = m.group("body")
        else:
            weight = naiweights.clamp(scale)
            body = token.strip()
        out.append(body if abs(weight - 1.0) < 0.005 else f"({body}:{weight:g})")
    return ", ".join(o for o in out if o)


def _split_top(text: str) -> list[str]:
    """Split on commas that are not inside parentheses."""
    out, depth, current = [], 0, ""
    escaped = False
    for ch in text:
        if escaped:
            current += ch
            escaped = False
            continue
        if ch == "\\":
            current += ch
            escaped = True
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth <= 0:
            out.append(current)
            current = ""
            continue
        current += ch
    out.append(current)
    return [o for o in (x.strip() for x in out) if o]

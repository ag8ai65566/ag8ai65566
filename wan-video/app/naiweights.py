"""Translate NovelAI prompt syntax into something ComfyUI actually honours.

This exists because a prompt codex written for NAI is not merely "a bit off" in
ComfyUI - most of it is silently discarded. ComfyUI's weight parser is 45 lines
of `comfy/sd1_clip.py` and it understands exactly one construct:

    parse_parentheses()  ->  splits on ( and ) only
    token_weights()      ->  "(x)" is weight *= 1.1
                             "(x:1.3)" is weight = 1.3, split on the LAST colon

That is the whole grammar. Nothing else is weighting. So in ComfyUI:

    {{{vacuum fellatio}}}   the braces are TEXT. Weight 1.0, plus six junk
                            tokens fed to CLIP.
    [[[deepthroat]]]        same. A1111 understands [], ComfyUI does not.
    1.35::breasts press::   same. NAI4.5 syntax, meaningless here.
    -2::pov::               same - and the intent (push away from POV) is lost
                            entirely, which is the worst case of the three.

A codex full of that pasted straight into an SD-family model therefore runs at
flat weight 1.0 with bracket characters polluting the conditioning. That is a
sufficient explanation on its own for "the tags are right but the picture is
wrong", and it is why every tag string is converted on the way in rather than
stored as-is.

The conversion factors are the ones the codex itself documents (its note 8):
NAI's {} and [] step by 1.05 per level, NAI4.5's `N::x::` sets the weight to N
outright, and SD's own syntax is `(x:N)`.

Two things cannot be translated and are handled honestly instead:

  * Negative weights. `-2::artist collaboration::` has no SD equivalent in the
    positive prompt, so the tag is moved to the negative prompt at weight 2.
    That is the closest真 equivalent, and it is reported rather than hidden.
  * Parentheses inside a name. `elaina (majo no tabitabi)` is a danbooru
    character name, but ComfyUI reads those parens as weighting and would
    reweight "majo no tabitabi" by 1.1 while dropping "elaina" to a bare token.
    Name parens are escaped to `\\(` `\\)`, which is what the tagger already
    does for the same reason (see tags.to_prompt).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# NovelAI's brace step. The codex states this itself; it is not SD's 1.1.
NAI_STEP = 1.05
# ComfyUI's own paren step, from token_weights(): `weight *= 1.1`.
SD_STEP = 1.1

MIN_WEIGHT = 0.05
MAX_WEIGHT = 4.0

# The codex misspells the artist prefix as `aritst:` in a number of places -
# and so did the user, copying from it. It is worth being blunt about what that
# costs: `aritst:` is not a prefix any model knows, so the whole token is read
# as the literal word "aritst" followed by a name, and the artist is simply not
# applied. Normalising it is the single highest-value fix in this file.
_TYPOS = (
    (re.compile(r"\baritst\s*:", re.I), "artist:"),
    (re.compile(r"\bartsit\s*:", re.I), "artist:"),
    (re.compile(r"\bartist\s+:", re.I), "artist:"),
)

_ARTIST = re.compile(r"^(?:artist\s*:|by\s+)\s*(?P<name>.+)$", re.I)


@dataclass
class Chunk:
    """One comma-separated tag, with the weight the NAI syntax asked for."""

    text: str
    weight: float = 1.0

    @property
    def is_artist(self) -> bool:
        return bool(_ARTIST.match(self.text.strip()))

    @property
    def artist_name(self) -> str:
        m = _ARTIST.match(self.text.strip())
        return m.group("name").strip() if m else ""


@dataclass
class Converted:
    positive: list[Chunk] = field(default_factory=list)
    artists: list[Chunk] = field(default_factory=list)
    # Tags that carried a negative NAI weight, moved here at abs(weight).
    negative: list[Chunk] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def prompt(self, *, artists: bool = True) -> str:
        chunks = self.positive if not artists else _interleave(self)
        return ", ".join(render(c) for c in chunks)

    def artist_prompt(self, scale: float = 1.0) -> str:
        return ", ".join(render(Chunk(c.text, c.weight * scale)) for c in self.artists)

    def negative_prompt(self) -> str:
        return ", ".join(render(c) for c in self.negative)

    def public(self) -> dict:
        return {
            "prompt": self.prompt(artists=False),
            "artists": self.artist_prompt(),
            "artist_names": [c.artist_name for c in self.artists],
            "negative": self.negative_prompt(),
            "notes": list(self.notes),
        }


def _interleave(conv: Converted) -> list[Chunk]:
    """Artists ahead of the rest.

    The codex's own advice (its note 4) is character first, then artist, then
    everything else, so that the style locks before other tags can pull on it.
    The character tag is whatever the caller prepends, so within this string
    the artists go first.
    """
    return list(conv.artists) + list(conv.positive)


def clamp(weight: float) -> float:
    return round(max(MIN_WEIGHT, min(float(weight), MAX_WEIGHT)), 2)


def render(chunk: Chunk) -> str:
    """One chunk as ComfyUI-safe text."""
    text = escape_names(chunk.text.strip())
    if not text:
        return ""
    weight = clamp(chunk.weight)
    if abs(weight - 1.0) < 0.005:
        return text
    # `:g` drops the trailing zero so 1.20 prints as 1.2, matching what the
    # rest of the app emits (charpacks.weighted, and the JS mirror of it).
    return f"({text}:{weight:g})"


def escape_names(text: str) -> str:
    """Escape parens that are part of a name, leaving already-escaped ones be.

    By the time this runs every weighting construct has been turned into a
    number, so any paren still present belongs to a name - `bb (baalbuddy)`,
    `fumo_(doll)`, `elaina (majo no tabitabi)`.
    """
    return re.sub(r"(?<!\\)([()])", r"\\\1", text)


# -- the parser ---------------------------------------------------------------
#
# One pass, left to right, carrying a weight multiplier. The three NAI
# constructs and SD's own parens all nest, so a stack is the honest shape:
#
#   {x}      push weight * 1.05
#   [x]      push weight / 1.05
#   N::x::   push weight = N       (NAI4.5; N may be negative)
#   (x)      push weight * 1.1     (the codex mixes SD syntax in too)
#   (x:N)    push weight = N
#
# The one genuinely ambiguous character is `(`. It is a weighting bracket when
# it opens a tag, and part of a name when it follows text inside one:
#
#   ((artist:CiloRanko))          -> weighting, twice
#   elaina (majo no tabitabi)     -> name
#
# That rule is applied by looking at whether anything has been collected in the
# current tag yet, which is cheap and gets every case in the codex right.

_NUM = re.compile(r"(-?\d+(?:\.\d+)?)::")


def parse(text: str) -> Converted:
    """NAI-syntax tag string -> chunks with real weights."""
    fixed = 0
    for pattern, fix in _TYPOS:
        text, n = pattern.subn(fix, text)
        fixed += n
    text = text.replace("。", ",").replace("，", ",")

    out = Converted()
    # Counted while substituting, not looked for afterwards: searching the
    # already-corrected string can only ever find nothing, so the note that
    # explains the correction never appeared.
    typo = fixed > 0

    stack: list[float] = [1.0]
    current = ""
    i = 0
    depth_kinds: list[str] = []

    def flush() -> None:
        nonlocal current
        tag = current.strip().strip(",").strip()
        current = ""
        if not tag:
            return
        chunk = Chunk(_tidy(tag), stack[-1])
        if chunk.weight < 0:
            out.negative.append(Chunk(chunk.text, abs(chunk.weight)))
        elif chunk.is_artist:
            out.artists.append(chunk)
        else:
            out.positive.append(chunk)

    while i < len(text):
        ch = text[i]

        # NAI4.5 numeric weight: `1.35::a,b::`
        m = _NUM.match(text, i)
        if m:
            flush()
            stack.append(float(m.group(1)))
            depth_kinds.append("num")
            i = m.end()
            continue
        if text.startswith("::", i) and depth_kinds and depth_kinds[-1] == "num":
            flush()
            stack.pop()
            depth_kinds.pop()
            i += 2
            continue

        if ch == "{":
            flush()
            stack.append(stack[-1] * NAI_STEP)
            depth_kinds.append("brace")
            i += 1
            continue
        if ch == "}":
            if depth_kinds and depth_kinds[-1] == "brace":
                flush()
                stack.pop()
                depth_kinds.pop()
            # An unmatched closer is a typo in the source, and this document has
            # several. Dropping it is right: kept as text it becomes a literal
            # `}}` token handed to CLIP, which is pure noise.
            i += 1
            continue
        if ch == "[":
            flush()
            stack.append(stack[-1] / NAI_STEP)
            depth_kinds.append("bracket")
            i += 1
            continue
        if ch == "]":
            if depth_kinds and depth_kinds[-1] == "bracket":
                flush()
                stack.pop()
                depth_kinds.pop()
            i += 1
            continue

        if ch == "(" and not current.strip():
            # Opens a tag, so it is SD weighting rather than part of a name.
            body, end = _matching(text, i)
            inner, weight = _paren_weight(body)
            flush()
            stack.append(stack[-1] * weight if weight == SD_STEP else weight)
            depth_kinds.append("paren")
            # Recurse on the contents so nested constructs still work.
            sub = parse(inner)
            for c in sub.positive:
                out.positive.append(Chunk(c.text, c.weight * stack[-1]))
            for c in sub.artists:
                out.artists.append(Chunk(c.text, c.weight * stack[-1]))
            for c in sub.negative:
                out.negative.append(Chunk(c.text, c.weight * stack[-1]))
            stack.pop()
            depth_kinds.pop()
            i = end
            continue

        if ch == ",":
            flush()
            i += 1
            continue

        current += ch
        i += 1

    flush()

    if typo:
        out.notes.append("原文把 artist 拼成 aritst，已修正（拼錯的話畫師根本不會生效）")
    if out.negative:
        moved = "、".join(c.text for c in out.negative)
        out.notes.append(f"原文用了 NAI 的負權重，SD 沒有這個寫法，已改放到負面提詞：{moved}")
    return out


def _tidy(tag: str) -> str:
    """Whitespace and underscores, per the codex's own note 7."""
    tag = tag.replace("_", " ")
    return _balance(re.sub(r"\s+", " ", tag).strip())


def _balance(tag: str) -> str:
    """Close a name paren the source left open.

    One entry in this codex reads `{w(arknights}` - the character is
    `w_(arknights)` and the closing paren never got typed. Escaped as-is it
    does not break ComfyUI's parser (the escape sentinel protects it), so this
    is not a crash; it is worse than that, because `w(arknights` is a name no
    model has ever seen and the tag silently does nothing. Balancing it gives
    back the tag the author meant.
    """
    opens = tag.count("(") - tag.count(")")
    if opens > 0:
        return tag + ")" * opens
    if opens < 0:
        return "(" * -opens + tag
    return tag


def _matching(text: str, start: int) -> tuple[str, int]:
    """Contents of the paren group at `start`, and the index just past it."""
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
    return text[start + 1:], len(text)


def _paren_weight(body: str) -> tuple[str, float]:
    """`x:1.3` -> ("x", 1.3); `x` -> ("x", 1.1). Splits on the LAST colon.

    The last colon is what ComfyUI's token_weights does (`x.rfind(":")`), and
    it is the reason `(artist:ciloranko:1.05)` works at all: the tag keeps its
    own colon and only the trailing number is read as a weight.
    """
    cut = body.rfind(":")
    if cut > 0:
        try:
            return body[:cut], float(body[cut + 1:])
        except ValueError:
            pass
    return body, SD_STEP


def convert(text: str) -> Converted:
    """Public entry point: NAI tag string -> Converted."""
    return parse(text or "")

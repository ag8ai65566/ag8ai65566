"""Merging a style recipe into a prompt without wrecking what is already there.

The naive version is `prompt + ", " + recipe`, and it fails in four ways people
actually hit: the same tag lands twice in different spellings, the new style
fights the old one (`monochrome` on top of `pastel colors`), the checkpoint gets
tokens from a different model's dialect (`score_9` on NoobAI), and the user
cannot see what changed so they cannot undo it.

So merging here is: split on commas that are actually separators, key each tag
by its bare form, drop duplicates keeping the user's own spelling and weight,
retire only the tags the incoming recipe explicitly conflicts with, strip the
tokens this checkpoint has no use for, and hand back a diff.

Two rules that are deliberate and worth stating, because both are easy to get
wrong in the "helpful" direction:

  * **The user's tags win.** If a tag is already in the prompt, its spelling and
    its weight survive. A recipe never re-weights something the user typed.
  * **Nothing unknown is ever removed.** Only tags on a known conflict list get
    retired, and even then only when the incoming recipe actually brings the
    other side of that conflict. Anything the merger does not recognise -
    character names, LoRA triggers, wildcards, the user's own inventions - is
    passed through untouched. A prompt tool that eats a LoRA trigger is worse
    than no prompt tool.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import styles


# --- splitting --------------------------------------------------------------

def split_tags(text: str) -> list[str]:
    """Split a prompt on separator commas.

    A comma inside brackets is not a separator - `(a, b:1.2)` is one weighted
    group - and neither is an escaped one. Everything else is.
    """
    out: list[str] = []
    buf: list[str] = []
    depth = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            buf.append(text[i:i + 2])
            i += 2
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            piece = "".join(buf).strip()
            if piece:
                out.append(piece)
            buf = []
        else:
            buf.append(ch)
        i += 1
    piece = "".join(buf).strip()
    if piece:
        out.append(piece)
    return out


def key(tag: str) -> str:
    """The comparison form of a tag: no weights, no brackets, no underscores."""
    from posebook import bare_tag
    return bare_tag(tag)


def dedupe(tags: list[str]) -> list[str]:
    """First spelling of each tag wins; order is preserved."""
    seen: set[str] = set()
    out: list[str] = []
    for t in tags:
        k = key(t)
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(t)
    return out


# --- conflicts --------------------------------------------------------------
# Tags that cannot all be true of one picture. Only tags named here are ever
# retired, and only against the other side of the same conflict.
#
# The spec's version of this list was a flat list of groups, which quietly says
# that every member excludes every other member. That is wrong twice over:
# `monochrome` and `greyscale` are the same thing (they co-occur on 684,962
# posts), and `realistic` and `photorealistic` are a subset relation - all 1,750
# `photorealistic` posts are also `realistic`. A flat group would have made each
# of those pairs delete the other. So a conflict here has *sides*: within a side
# tags coexist, across sides they do not.
#
# Two of the five conflicts are true by construction - a picture has one upload
# date and one rating, so NoobAI's five date buckets and danbooru's ratings are
# exclusive whatever the data says. (The spec listed six date buckets; the model
# card documents five. There is no `oldest`.)
#
# The other three were measured on danbooru rather than asserted. `lift` is how
# often two tags actually co-occur divided by how often they would if they were
# independent, over the 12,003,162 posts danbooru held on 2026-08-23:
#
#     monochrome   + greyscale        14.2x    same thing
#     monochrome   + spot color        9.8x    spot colour is monochrome-plus-one
#     realistic    + photorealistic     370x   subset
#     portrait     + close-up          11.2x   co-occur happily
#     -------------------------------------------------------------------
#     greyscale    + pastel colors    0.007x   conflict
#     monochrome   + anime coloring   0.011x   conflict
#     anime colr.  + realistic        0.033x   conflict
#     monochrome   + pastel colors    0.072x   conflict
#     3d           + flat color       0.150x   conflict
#     flat color   + realistic        0.220x   conflict
#     3d           + anime coloring   0.210x   conflict
#
# And three pairs the spec would have made conflict, which measurably do not:
#
#     anime coloring + flat color     0.570x   fine together, both ship in recipes
#     portrait       + upper body     0.640x   fine
#     muted colors   + pastel colors   2.2x    they actually co-occur
#
# The last one matters: framing tags are left out of this list entirely.
# Illustrious's card says do not *overuse* `close-up` / `cowboy shot`, not that
# they cannot be combined - and the data agrees. That belongs in the prompt
# doctor as a warning, not here as a deletion.

@dataclass(frozen=True)
class Conflict:
    id: str
    sides: tuple[tuple[str, ...], ...]
    why: str
    evidence: str = ""


CONFLICTS: list[Conflict] = [
    Conflict(
        "era",
        (("old",), ("early",), ("mid",), ("recent",), ("newest",)),
        "NoobAI 的年代桶一張圖只會有一個（old=2005-2010 … newest=2021-2024）。",
        "Laxhar/noobai-XL-1.1 model card 的 Date tags 表，五格。",
    ),
    Conflict(
        "rating",
        (("safe",), ("sensitive",), ("questionable",), ("nsfw", "explicit")),
        "分級一張圖只有一個。",
        "danbooru 的分級定義；NoobAI 官方範例提詞用 safe / nsfw 這兩個字。",
    ),
    Conflict(
        "color-mode",
        (("monochrome", "greyscale", "spot color"), ("pastel colors",)),
        "整張黑白就不會有粉彩色盤。",
        "danbooru 共現：monochrome+greyscale 14.2 倍（同一件事）、"
        "monochrome+spot color 9.8 倍（同一側）；monochrome+pastel colors 0.072 倍、"
        "greyscale+pastel colors 0.007 倍（互斥）。",
    ),
    Conflict(
        "color-vs-mono",
        (("monochrome", "greyscale"), ("anime coloring",)),
        "黑白跟動畫上色是兩種不同的成品。",
        "danbooru 共現 0.011 倍。",
    ),
    Conflict(
        "render",
        (("anime coloring", "flat color"), ("realistic", "photorealistic", "3d")),
        "動畫上色跟寫實／3D 渲染會互相拉扯，出來通常是四不像的 2.5D。",
        "danbooru 共現：anime coloring+realistic 0.033 倍、flat color+realistic 0.22 倍、"
        "3d+flat color 0.15 倍、3d+anime coloring 0.21 倍。"
        "同一側的 realistic+photorealistic 是 370 倍（photorealistic 全部都是 realistic 的子集）。",
    ),
]


def _side_of(tag: str) -> list[tuple[str, int]]:
    """Every (conflict id, side index) this tag sits on."""
    k = key(tag)
    out = []
    for c in CONFLICTS:
        for i, side in enumerate(c.sides):
            if k in side:
                out.append((c.id, i))
    return out


CONFLICT_BY_ID = {c.id: c for c in CONFLICTS}


def conflicts_with(incoming: str, existing: str) -> str:
    """The conflict id if these two cannot coexist, otherwise an empty string."""
    if key(incoming) == key(existing):
        return ""
    mine, theirs = _side_of(incoming), _side_of(existing)
    for cid, i in mine:
        for cid2, j in theirs:
            if cid == cid2 and i != j:
                return cid
    return ""


# --- model cleanup ----------------------------------------------------------
# Tokens that belong to a different checkpoint's dialect. Removing them is safe
# because each one is inert-to-harmful on the target, and each is listed by name
# - nothing is removed by pattern-matching, so a LoRA trigger can never be hit.

PONY_SCORES = [
    "score_9", "score_8_up", "score_7_up", "score_6_up", "score_5_up", "score_4_up",
    "score_8", "score_7", "score_6", "score_5", "score_4", "score_3", "score_9_up",
]

# Words each family has no training for. Verified: NoobAI's card lists five
# quality tags and five date buckets; Illustrious's lists six quality tags and
# `displeasing`; Pony's captions have neither, and had artist names stripped.
FOREIGN: dict[str, list[str]] = {
    "noobai": PONY_SCORES + ["very aesthetic", "amazing quality", "displeasing",
                             "very displeasing", "source_anime", "rating_safe"],
    "illustrious": PONY_SCORES + ["newest", "recent", "mid", "early", "old",
                                  "very aesthetic", "amazing quality"],
    "pony": ["newest", "recent", "mid", "early", "old", "masterpiece",
             "best quality", "worst quality", "very aesthetic", "displeasing",
             "very displeasing"],
    "juggernaut": PONY_SCORES + ["newest", "recent", "mid", "early", "old",
                                 "masterpiece", "displeasing", "very displeasing"],
    "sdxl-base": PONY_SCORES + ["newest", "recent", "mid", "early", "old",
                                "displeasing", "very displeasing"],
}

# Why each removal happens, so the UI can say it rather than just doing it.
FOREIGN_WHY: dict[str, str] = {
    "score": "Pony 專屬的品質詞。Pony 以外的模型沒有訓練過這串，只是佔 token。",
    "era": "NoobAI 專屬的年代桶（old/early/mid/recent/newest），只有 NoobAI 的 caption 有。",
    "quality": "這個模型的 model card 沒有列這個品質詞——它是別的微調自己加的。",
}


def _why(tag: str) -> str:
    k = key(tag)
    if k.startswith("score "):
        return FOREIGN_WHY["score"]
    if k in {"old", "early", "mid", "recent", "newest"}:
        return FOREIGN_WHY["era"]
    return FOREIGN_WHY["quality"]


def cleanup_for_model(tags: list[str], model_id: str) -> tuple[list[str], list[dict]]:
    """Drop tokens from another checkpoint's dialect. Returns (kept, removed)."""
    foreign = {k.replace("_", " ") for k in FOREIGN.get(model_id, [])}
    kept: list[str] = []
    dropped: list[dict] = []
    for t in tags:
        if key(t) in foreign:
            dropped.append({"tag": t, "why": _why(t)})
        else:
            kept.append(t)
    return kept, dropped


# --- the merge --------------------------------------------------------------

@dataclass
class Merge:
    prompt: str
    negative: str
    added: list[str] = field(default_factory=list)
    already: list[str] = field(default_factory=list)
    replaced: list[dict] = field(default_factory=list)
    cleaned: list[dict] = field(default_factory=list)
    negative_added: list[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.added or self.replaced or self.cleaned or self.negative_added)

    def public(self) -> dict:
        return {
            "prompt": self.prompt, "negative": self.negative,
            "added": self.added, "already": self.already,
            "replaced": self.replaced, "cleaned": self.cleaned,
            "negative_added": self.negative_added, "changed": self.changed,
        }


def merge(
    prompt: str,
    negative: str,
    add: list[str],
    add_negative: list[str] | None = None,
    *,
    model_id: str = "",
    replace_conflicts: bool = True,
    clean_model: bool = True,
) -> Merge:
    """Fold `add` into `prompt`, returning the result and a diff.

    `replace_conflicts=False` is the "keep my current look" button: new tags are
    still appended, but nothing already in the prompt is retired.
    """
    current = split_tags(prompt)
    incoming = dedupe([t.strip() for t in add if t.strip()])

    out = list(current)
    res = Merge(prompt="", negative="")
    # Only tags that were already in the prompt can be retired. A recipe that
    # ships both sides of a conflict on purpose - `ink-manga` ships `monochrome`
    # and `greyscale`, `beauty-closeup` ships `portrait` and `upper body` - must
    # not end up deleting half of itself on the way in.
    protected = {key(t) for t in incoming}

    for tag in incoming:
        if any(key(tag) == key(t) for t in out):
            res.already.append(tag)
            continue
        if replace_conflicts:
            for lost in list(out):
                if key(lost) in protected:
                    continue
                cid = conflicts_with(tag, lost)
                if not cid:
                    continue
                out.remove(lost)
                res.replaced.append({
                    "removed": lost, "because": tag, "conflict": cid,
                    "why": CONFLICT_BY_ID[cid].why,
                })
        out.append(tag)
        res.added.append(tag)

    if clean_model and model_id:
        out, res.cleaned = cleanup_for_model(out, model_id)

    neg = split_tags(negative)
    for tag in dedupe([t.strip() for t in (add_negative or []) if t.strip()]):
        if not any(key(tag) == key(t) for t in neg):
            neg.append(tag)
            res.negative_added.append(tag)

    res.prompt = ", ".join(dedupe(out))
    res.negative = ", ".join(dedupe(neg))
    return res


def apply_recipe(
    prompt: str,
    negative: str,
    recipe_id: str,
    *,
    model_id: str = "",
    tag_style: str = "danbooru",
    replace_conflicts: bool = True,
) -> Merge | None:
    r = styles.get(recipe_id)
    if r is None:
        return None
    return merge(
        prompt, negative,
        [c.emit(tag_style) for c in r.resolve(r.chips)],
        [c.emit(tag_style) for c in r.resolve(r.negative)],
        model_id=model_id, replace_conflicts=replace_conflicts,
    )


def apply_preset(
    prompt: str, negative: str, preset_id: str, *, model_id: str = "",
) -> Merge | None:
    p = styles.PRESET_BY_ID.get(preset_id)
    if p is None:
        return None
    return merge(
        prompt, negative, split_tags(p.positive), split_tags(p.negative),
        model_id=model_id, replace_conflicts=True,
    )


def remove_tags(prompt: str, tags: list[str]) -> str:
    """Take specific tags back out - the undo half of a one-click apply."""
    drop = {key(t) for t in tags}
    return ", ".join(t for t in split_tags(prompt) if key(t) not in drop)

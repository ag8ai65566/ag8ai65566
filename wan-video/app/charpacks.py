"""Character packs: one LoRA, its whole cast, and a one-click prompt for each.

A big character LoRA is not one trigger word - it is several hundred. The
Hololive collection alone carries 75 characters with 319 outfits between them,
and the only place that information exists is a wall of text on a CivitAI page.
Copying the right line out of it every time is the actual work of using the
LoRA, so it is copied in once, here, and turned into a picker.

A pack is a JSON file in app/packs/. Adding another LoRA means adding another
file - no code changes - which is the point: this is meant to grow as the user
finds more LoRAs worth keeping.

Nothing in a pack is invented. Every trigger, tag, filename, byte size and
version id came from the model's own CivitAI page or the CivitAI API.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

PACKS_DIR = Path(__file__).parent / "packs"


@dataclass
class Costume:
    label: str
    trigger: str          # the character (and outfit) trigger words
    tags: str             # the appearance tags that go with that outfit

    def public(self) -> dict:
        return {"label": self.label, "trigger": self.trigger, "tags": self.tags}


@dataclass
class Character:
    key: str
    name: str
    jp: str = ""
    emoji: str = ""
    group: str = ""
    former: bool = False
    # Who actually drew this character ("mama"), and the danbooru artist tag
    # for them if one exists. The tag is what a danbooru-trained model needs to
    # be told in order to draw in that person's style.
    designer: str = ""
    designer_url: str = ""
    artist_tag: str = ""
    artist_posts: int = 0
    # How many danbooru posts carry this character's own tag - i.e. how well a
    # danbooru-trained base model knows them with no LoRA at all.
    danbooru_posts: int = 0
    wiki: str = ""
    costumes: list[Costume] = field(default_factory=list)

    def public(self) -> dict:
        return {
            "key": self.key, "name": self.name, "jp": self.jp, "emoji": self.emoji,
            "group": self.group, "former": self.former,
            "designer": self.designer, "designer_url": self.designer_url,
            "artist_tag": self.artist_tag, "artist_posts": self.artist_posts,
            "danbooru_posts": self.danbooru_posts, "wiki": self.wiki,
            "costumes": [c.public() for c in self.costumes],
        }


@dataclass
class Group:
    id: str
    label: str
    members: list[str]


@dataclass
class Pack:
    id: str
    label: str
    file: str                     # the .safetensors this pack needs
    groups: list[Group]
    characters: list[Character]
    subject: str = ""
    author: str = ""
    civitai: str = ""
    model_id: int = 0
    version_id: int = 0
    version: str = ""
    size: int = 0
    download_url: str = ""
    base_model: str = ""
    wants_model: str = ""         # an id in images.IMAGE_MODELS
    strength: float = 0.8
    strength_clip: float = 0.8
    scaffold: str = ""            # tags the author says to add to every prompt
    quality: str = ""             # the quality-tag prefix this LoRA was rated with
    negative: str = ""
    note: str = ""
    license: str = ""
    # Base models trained with danbooru artist tags intact, mapped to the form
    # each one actually wants. They differ, and the difference matters:
    # NoobAI's own model card prompts with `artist:john_kafka`, while the
    # Illustrious guidance is `by ebifurya`. Pony is in neither - its model card
    # says artist names were removed from the training captions.
    artist_tag_models: dict[str, str] = field(default_factory=dict)
    # Base models that know these characters without the LoRA at all.
    native_models: list[str] = field(default_factory=list)
    style_note: str = ""
    # The danbooru copyright tag for this cast. NoobAI's documented caption
    # order is <1girl>, <character>, <series>, <artists>, ... so on a
    # danbooru-trained model naming the series is worth a tag; on Pony it is
    # noise, because Pony was not captioned that way.
    series: str = ""

    @property
    def by_key(self) -> dict[str, Character]:
        return {c.key: c for c in self.characters}

    def public(self) -> dict:
        return {
            "id": self.id, "label": self.label, "subject": self.subject,
            "author": self.author, "civitai": self.civitai, "version": self.version,
            "version_id": self.version_id, "file": self.file, "size": self.size,
            "base_model": self.base_model, "wants_model": self.wants_model,
            "strength": self.strength, "strength_clip": self.strength_clip,
            "scaffold": self.scaffold, "quality": self.quality,
            "negative": self.negative, "note": self.note, "license": self.license,
            "artist_tag_models": self.artist_tag_models,
            "native_models": self.native_models, "style_note": self.style_note,
            "series": self.series,
            "groups": [{"id": g.id, "label": g.label, "members": g.members}
                       for g in self.groups],
            "characters": [c.public() for c in self.characters],
            "count": len(self.characters),
            "costume_count": sum(len(c.costumes) for c in self.characters),
        }


# "{tag}" is where the artist name goes. A bare list is still accepted so a
# hand-written pack does not have to know about per-model forms - but it then
# gets the form that model documents, not one blanket default. A list of
# ["illustrious"] used to come back as `artist:{tag}`, which is precisely the
# spelling this project's own docs call wrong for Illustrious.
DEFAULT_ARTIST_FORM = "artist:{tag}"
KNOWN_ARTIST_FORMS = {
    "noobai": "artist:{tag}",        # its model card prompts with artist:john_kafka
    "illustrious": "by {tag}",       # its guidance is "by ebifurya"
}


def _forms(raw) -> dict[str, str]:
    if isinstance(raw, dict):
        return {str(k): (str(v) if "{tag}" in str(v)
                         else KNOWN_ARTIST_FORMS.get(str(k), DEFAULT_ARTIST_FORM))
                for k, v in raw.items()}
    return {str(m): KNOWN_ARTIST_FORMS.get(str(m), DEFAULT_ARTIST_FORM)
            for m in (raw or [])}


def _load(path: Path) -> Pack | None:
    """One pack file. A broken file is skipped, never fatal.

    These are data files the user may hand-edit to add their own LoRA, so a
    typo in one must not take the whole app down with it.
    """
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(raw, dict) or not raw.get("id") or not raw.get("file"):
        return None

    characters: list[Character] = []
    for entry in raw.get("characters") or []:
        if not isinstance(entry, dict) or not entry.get("key"):
            continue
        costumes = [
            Costume(label=str(c.get("label", "")), trigger=str(c.get("trigger", "")),
                    tags=str(c.get("tags", "")))
            for c in (entry.get("costumes") or []) if isinstance(c, dict)
        ]
        if not costumes:
            continue
        try:
            posts = int(entry.get("artist_posts") or 0)
            native = int(entry.get("danbooru_posts") or 0)
        except (TypeError, ValueError):
            posts = native = 0
        characters.append(Character(
            key=str(entry["key"]), name=str(entry.get("name", entry["key"])),
            jp=str(entry.get("jp", "")), emoji=str(entry.get("emoji", "")),
            group=str(entry.get("group", "")), former=bool(entry.get("former")),
            designer=str(entry.get("designer", "")),
            designer_url=str(entry.get("designer_url", "")),
            artist_tag=str(entry.get("artist_tag", "")), artist_posts=posts,
            danbooru_posts=native, wiki=str(entry.get("wiki", "")),
            costumes=costumes,
        ))
    if not characters:
        return None

    known = {c.key for c in characters}
    groups = [
        Group(id=str(g.get("id", "")), label=str(g.get("label", "")),
              # A group listing someone who is not in the file would render an
              # empty slot the user can click and get nothing from.
              members=[m for m in (g.get("members") or []) if m in known])
        for g in (raw.get("groups") or []) if isinstance(g, dict) and g.get("id")
    ]
    grouped = {m for g in groups for m in g.members}
    loose = [c.key for c in characters if c.key not in grouped]
    if loose:
        groups.append(Group(id="_other", label="其他", members=loose))

    def num(key, default):
        try:
            return type(default)(raw.get(key, default))
        except (TypeError, ValueError):
            return default

    return Pack(
        id=str(raw["id"]), label=str(raw.get("label", raw["id"])), file=str(raw["file"]),
        groups=[g for g in groups if g.members], characters=characters,
        subject=str(raw.get("subject", "")), author=str(raw.get("author", "")),
        civitai=str(raw.get("civitai", "")), model_id=num("model_id", 0),
        version_id=num("version_id", 0), version=str(raw.get("version", "")),
        size=num("size", 0), download_url=str(raw.get("download_url", "")),
        base_model=str(raw.get("base_model", "")), wants_model=str(raw.get("wants_model", "")),
        strength=num("strength", 0.8), strength_clip=num("strength_clip", 0.8),
        scaffold=str(raw.get("scaffold", "")), quality=str(raw.get("quality", "")),
        negative=str(raw.get("negative", "")), note=str(raw.get("note", "")),
        license=str(raw.get("license", "")),
        artist_tag_models=_forms(raw.get("artist_tag_models")),
        native_models=[str(m) for m in (raw.get("native_models") or [])],
        style_note=str(raw.get("style_note", "")), series=str(raw.get("series", "")),
    )


def load(folder: Path | None = None) -> list[Pack]:
    base = folder or PACKS_DIR
    if not base.is_dir():
        return []
    packs = [p for p in (_load(f) for f in sorted(base.glob("*.json"))) if p]
    # Two files claiming the same id would make `get` depend on glob order.
    seen: set[str] = set()
    return [p for p in packs if not (p.id in seen or seen.add(p.id))]


PACKS: list[Pack] = load()


def get(pack_id: str) -> Pack | None:
    return next((p for p in PACKS if p.id == pack_id), None)


def style_advice(pack: Pack, who: Character, model: str) -> dict:
    """Can this base model be told to draw in the original designer's style?

    Only a model trained with danbooru artist tags can. Pony V6's own model card
    says artist names were removed from its captions, so `by teshima_nari` there
    is three tokens of nothing - and quietly adding it anyway would look like
    the feature works when it does not.
    """
    out = {"tag": who.artist_tag, "designer": who.designer, "posts": who.artist_posts,
           "wiki": who.wiki, "works": False, "why": "", "form": ""}
    if not who.artist_tag:
        out["why"] = (
            f"{who.name} 的原畫師"
            + (f"（{who.designer}）" if who.designer else "")
            + "在 danbooru 上沒有可用的畫師標籤，所以沒辦法用標籤指定畫風。"
        )
        return out
    if model and model in pack.artist_tag_models:
        out["works"] = True
        out["form"] = pack.artist_tag_models[model].replace("{tag}", who.artist_tag)
        out["why"] = (f"{who.designer} 的 danbooru 畫師標籤（{who.artist_posts} 張），"
                      f"這個底模認得，寫法是 `{out['form']}`。")
        return out
    known = "／".join(pack.artist_tag_models) or "沒有"
    out["why"] = (
        f"這個底模不吃畫師標籤，加了也沒作用（{pack.base_model or '它'} 訓練時把畫師名字拿掉了）。"
        f"要靠標籤貼近 {who.designer or '原畫師'} 的畫風，底模要換成 {known}。"
    )
    if who.danbooru_posts >= 1000:
        out["why"] += (
            f" 好消息是 {who.name} 在 danbooru 上有 {who.danbooru_posts} 張圖，"
            "換過去之後不用這支 LoRA 也畫得出來。"
        )
    return out


def weighted(token: str, weight: float) -> str:
    """`(token:1.3)` - the only weighting syntax ComfyUI actually parses.

    Checked by running ComfyUI 0.33's own token_weights() over the result: it
    splits on the *last* colon, so `(artist:amashiro_natsuki:1.3)` comes back as
    the tag `artist:amashiro_natsuki` at 1.3, colon in the tag and all. The
    NovelAI form `{{tag}}` comes back as literal braces at weight 1.0 - i.e. it
    does nothing here except put punctuation in the prompt.
    """
    weight = round(max(0.1, min(weight, 2.0)), 2)
    # `:g` rather than str(): the browser shows this same token before the
    # request is made, and JS prints 2 where Python prints 2.0. A preview that
    # does not match the thing sent is worse than no preview.
    return token if abs(weight - 1.0) < 0.005 else f"({token}:{weight:g})"


# `(artist:x:1.2)` / `(by x)` / `((x))` - any parenthesised spelling of one tag.
_WEIGHTED = re.compile(r"^\(+\s*(?:artist:|by\s+)?(?P<tag>[^():]+?)\s*(?::[\d.]+)?\s*\)+$",
                       re.IGNORECASE)


def _drop_duplicate_artist(chunk: str, bare: str) -> str:
    """Strip any weighted mention of `bare` from a comma-separated chunk."""
    if not chunk or bare not in chunk.lower():
        return chunk
    kept = []
    for tag in chunk.split(","):
        m = _WEIGHTED.match(tag.strip())
        if m and m.group("tag").strip().lower() == bare:
            continue
        kept.append(tag)
    return ",".join(kept)


# Tags that pull towards the official design rather than the fan-art average.
# `official_art` is a 533,688-post tag, so the model knows it well as a framing
# and finish; combined with a character it biases towards that character's own
# small official subset. `newest` is NoobAI's own recency bucket, which matters
# because a VTuber's current look is the recent one.
LIKENESS_TAGS = "official art, newest"


def likeness_advice(pack: Pack, who: Character) -> dict:
    """Why a generated character drifts from the stream model, with numbers.

    This is the most common disappointment with a character LoRA and the reason
    is not a bug, it is what the training data is: danbooru holds fan art, and
    only 1-3% of any of these characters is official art. So the concept the
    model learned is a *fan consensus*, not the reference sheet - it will be
    recognisably them and still not match the Live2D model.

    Naming the original designer does not fix it either, and the numbers say why
    more clearly than any explanation: of Mori Calliope's 12,544 danbooru posts,
    30 are by her designer Yukisame. Of Hoshimachi Suisei's 15,155, fourteen are
    by Teshima Nari. The artist tag therefore contributes that person's *general*
    style - mostly drawn on other subjects - rather than their rendering of this
    character, which is why it can make likeness worse rather than better.

    What does help is measurable too: the costume tag. `mori_calliope_(1st_costume)`
    carries 3,136 posts, `gawr_gura_(1st_costume)` 7,598 - because the official
    look *is* that outfit, and the outfit tag is the part of the identity that
    fan art reproduces faithfully.
    """
    costume_tags = [c.trigger for c in who.costumes]
    return {
        "posts": who.danbooru_posts,
        "designer": who.designer,
        "artist_tag": who.artist_tag,
        "artist_posts": who.artist_posts,
        "wiki": who.wiki,
        "costumes": len(costume_tags),
        "why": (
            f"danbooru 上 {who.danbooru_posts:,} 張{who.name}裡，官方圖只佔 1～3%。"
            "模型學到的是「同人平均值」，不是設定圖。"
        ),
        "artist_why": (
            f"{who.designer} 在 danbooru 只有 {who.artist_posts:,} 張，"
            f"其中畫{who.name}的更少 —— 所以掛他的 tag 是把他<b>畫別人時</b>的畫風"
            "拉進來，對「像不像本人」通常沒幫助，甚至會扯後腿。"
        ) if who.artist_tag else "",
    }


def build_prompt(pack: Pack, character_key: str, costume: int = 0, *,
                 extra: str = "", quality: bool = True, model: str = "",
                 style: bool = False, quality_tags: str = "",
                 artist_weight: float = 1.0, likeness: float = 0.0) -> dict | None:
    """The one-click prompt: who, wearing what, in the order the author wants.

    Trigger first, then that outfit's appearance tags, then whatever the user
    typed, then the quality tags last. Pony reads the score tags as a global
    quality signal rather than as subject matter, and every example on the
    model's own page puts them at the end - so that is where they go.

    `style` asks for the original character designer's own look. It is honoured
    only on a base model that was trained with artist tags; everywhere else the
    request comes back refused with a reason, rather than silently doing nothing.
    """
    who = pack.by_key.get(character_key)
    if who is None:
        return None
    index = costume if 0 <= costume < len(who.costumes) else 0
    outfit = who.costumes[index]
    advice = style_advice(pack, who, model)
    applied = bool(style and advice["works"])

    # The artist tag goes right after the character, which is where every
    # Illustrious style guide puts it and where it has the most pull.
    # `likeness` weights the costume trigger, which is the strongest identity
    # lever there is - see likeness_advice for the counts behind that claim.
    head = [weighted(outfit.trigger, likeness) if likeness else outfit.trigger]
    if likeness:
        head.append(LIKENESS_TAGS)
    if pack.series and model in pack.native_models:
        head.append(pack.series)
    mine = extra.strip()
    if applied:
        head.append(weighted(advice["form"], artist_weight))
        # Any weighted spelling of the same artist typed by hand - `(artist:x:1.2)`,
        # `((x))`, `(by x:0.9)` - is a second pull on one artist at a different
        # strength, which is the exact thing the weight slider exists to control.
        # Only the user's own text is filtered: running this over `head` as well
        # deleted the token the slider had just produced.
        mine = _drop_duplicate_artist(mine, who.artist_tag.lower())
    parts = [*head, pack.scaffold, outfit.tags, mine]
    if quality:
        # A different base model wants different quality tags: Pony's score_*
        # ladder means nothing to Illustrious and vice versa.
        parts.append(quality_tags.strip() or pack.quality)
    seen: set[str] = set()
    tags: list[str] = []
    if applied:
        # A hand-typed `artist:x` next to the weighted one is two artist tags
        # pulling at different strengths, which is not what the slider means.
        # Every spelling is blocked except the one actually being emitted -
        # discarding the *form* instead let the unweighted copy back in at
        # weight 1.0, where the form and the emitted token are the same string.
        bare = who.artist_tag.lower()
        seen |= {bare, f"artist:{bare}", f"by {bare}"}
        seen.discard(weighted(advice["form"], artist_weight).lower())
    for chunk in parts:
        for tag in (t.strip() for t in chunk.split(",")):
            # Dropping repeats matters here: the scaffold says "1girl" and so do
            # a few of the per-outfit tag lists, and a doubled tag is a weight
            # the user did not ask for.
            if tag and tag.lower() not in seen:
                seen.add(tag.lower())
                tags.append(tag)
    return {
        "prompt": ", ".join(tags),
        "negative": pack.negative,
        "character": who.name,
        "costume": outfit.label,
        "lora": pack.file,
        "strength": pack.strength,
        "strength_clip": pack.strength_clip,
        "wants_model": pack.wants_model,
        "likeness": likeness_advice(pack, who),
        "style": {**advice, "applied": applied,
                  "weight": round(max(0.1, min(artist_weight, 2.0)), 2),
                  "emitted": weighted(advice["form"], artist_weight) if applied else ""},
    }


HELP = (
    "角色包 = 一支角色 LoRA + 它認得的所有角色和衣裝，整理成可以直接點的清單。"
    "選人、選衣服，提詞就填好了 —— 不用再回 CivitAI 的說明頁翻那一大串標籤。"
)

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
    # Base models that were trained with danbooru artist tags intact, so
    # "by <artist>" actually steers the style. Pony V6 is not one of them: its
    # own model card says artist names were removed from the training captions.
    artist_tag_models: list[str] = field(default_factory=list)
    # Base models that know these characters without the LoRA at all.
    native_models: list[str] = field(default_factory=list)
    style_note: str = ""

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
            "groups": [{"id": g.id, "label": g.label, "members": g.members}
                       for g in self.groups],
            "characters": [c.public() for c in self.characters],
            "count": len(self.characters),
            "costume_count": sum(len(c.costumes) for c in self.characters),
        }


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
        artist_tag_models=[str(m) for m in (raw.get("artist_tag_models") or [])],
        native_models=[str(m) for m in (raw.get("native_models") or [])],
        style_note=str(raw.get("style_note", "")),
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
           "wiki": who.wiki, "works": False, "why": ""}
    if not who.artist_tag:
        out["why"] = (
            f"{who.name} 的原畫師"
            + (f"（{who.designer}）" if who.designer else "")
            + "在 danbooru 上沒有可用的畫師標籤，所以沒辦法用標籤指定畫風。"
        )
        return out
    if model and model in pack.artist_tag_models:
        out["works"] = True
        out["why"] = f"{who.designer} 的 danbooru 畫師標籤（{who.artist_posts} 張），這個底模認得。"
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


def build_prompt(pack: Pack, character_key: str, costume: int = 0, *,
                 extra: str = "", quality: bool = True, model: str = "",
                 style: bool = False, quality_tags: str = "") -> dict | None:
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
    head = [outfit.trigger] + ([f"by {who.artist_tag}"] if applied else [])
    parts = [*head, pack.scaffold, outfit.tags, extra.strip()]
    if quality:
        # A different base model wants different quality tags: Pony's score_*
        # ladder means nothing to Illustrious and vice versa.
        parts.append(quality_tags.strip() or pack.quality)
    seen: set[str] = set()
    tags: list[str] = []
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
        "style": {**advice, "applied": applied},
    }


HELP = (
    "角色包 = 一支角色 LoRA + 它認得的所有角色和衣裝，整理成可以直接點的清單。"
    "選人、選衣服，提詞就填好了 —— 不用再回 CivitAI 的說明頁翻那一大串標籤。"
)

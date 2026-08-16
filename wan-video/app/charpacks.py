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
    costumes: list[Costume] = field(default_factory=list)

    def public(self) -> dict:
        return {
            "key": self.key, "name": self.name, "jp": self.jp, "emoji": self.emoji,
            "group": self.group, "former": self.former,
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
        characters.append(Character(
            key=str(entry["key"]), name=str(entry.get("name", entry["key"])),
            jp=str(entry.get("jp", "")), emoji=str(entry.get("emoji", "")),
            group=str(entry.get("group", "")), former=bool(entry.get("former")),
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


def build_prompt(pack: Pack, character_key: str, costume: int = 0, *,
                 extra: str = "", quality: bool = True) -> dict | None:
    """The one-click prompt: who, wearing what, in the order the author wants.

    Trigger first, then that outfit's appearance tags, then whatever the user
    typed, then the quality tags last. Pony reads the score tags as a global
    quality signal rather than as subject matter, and every example on the
    model's own page puts them at the end - so that is where they go.
    """
    who = pack.by_key.get(character_key)
    if who is None:
        return None
    index = costume if 0 <= costume < len(who.costumes) else 0
    outfit = who.costumes[index]
    parts = [outfit.trigger, pack.scaffold, outfit.tags, extra.strip()]
    if quality and pack.quality:
        parts.append(pack.quality)
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
    }


HELP = (
    "角色包 = 一支角色 LoRA + 它認得的所有角色和衣裝，整理成可以直接點的清單。"
    "選人、選衣服，提詞就填好了 —— 不用再回 CivitAI 的說明頁翻那一大串標籤。"
)

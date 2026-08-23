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
    # How many danbooru posts currently carry this character's own tag. This is
    # *corpus prevalence*, not a measurement of how strongly any checkpoint
    # learned the concept: between the two sit the training snapshot's cutoff,
    # dedup, caption normalisation, tag dropout and sampling weights. A high
    # count is a good prior that a danbooru-trained base model knows them
    # without a LoRA; only a generation can say whether it does.
    danbooru_posts: int = 0
    # How many of those posts also carry `official_art`. Measured per character
    # against danbooru on 2026-08-23, because the previous version of this file
    # quoted a flat "1-3%" for everyone - a figure taken from a handful of the
    # most popular members and generalised to all 75. It does not hold: across
    # the 75 the real range is 0.62% to 9.45%, median 3.7%, and 28 of them are
    # above 5%. See `official_ratio` for what the number actually tracks.
    official_posts: int = 0
    wiki: str = ""
    costumes: list[Costume] = field(default_factory=list)

    @property
    def official_ratio(self) -> float:
        """Share of this character's danbooru posts that are official art, in %."""
        if self.danbooru_posts <= 0:
            return 0.0
        return round(self.official_posts / self.danbooru_posts * 100, 2)

    def public(self) -> dict:
        return {
            "key": self.key, "name": self.name, "jp": self.jp, "emoji": self.emoji,
            "group": self.group, "former": self.former,
            "designer": self.designer, "designer_url": self.designer_url,
            "artist_tag": self.artist_tag, "artist_posts": self.artist_posts,
            "danbooru_posts": self.danbooru_posts,
            "official_posts": self.official_posts,
            "official_ratio": self.official_ratio, "wiki": self.wiki,
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
            danbooru_posts=native,
            official_posts=int(entry.get("official_posts") or 0),
            wiki=str(entry.get("wiki", "")),
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
    says artist names were removed from its captions, so an artist tag there has
    no caption behind it - which is a fact about the training data, not a
    measured result. This project has never generated an image, so it does not
    know what Pony does with those tokens; it declines to add them silently,
    because a feature that looks like it works and does not is worse than one
    that says up front it is unverified.
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
        f"這個底模的訓練標註裡沒有畫師名字（{pack.base_model or '它'} 官方說明寫的），"
        "所以本專案不會自動幫你加 —— **加了會怎樣本專案沒有實測過**。"
        f"要靠標籤貼近 {who.designer or '原畫師'} 的畫風，底模換成 {known} 比較有把握。"
    )
    if who.danbooru_posts >= 1000:
        out["why"] += (
            f" 另外 {who.name} 在 danbooru 上有 {who.danbooru_posts:,} 張圖，"
            "以 danbooru 訓練的底模來說算是常見角色，換過去之後**有機會**不用這支 LoRA "
            "也畫得出來——這是先驗不是保證，實際認不認得要生一張才知道。"
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


# A bias towards official-art *rendering*, not a query for a character's official
# subset. Worth stating precisely, because the loose version of this claim does
# not survive review: `character + official_art` is compositional conditioning,
# so what it actually pulls in is what `official_art` looks like - clean finish,
# promotional framing, plain backgrounds. Whether that lands closer to the
# reference sheet for any given character is a hypothesis this project has not
# tested, which is why the UI calls it experimental.
#
# `newest` used to be in here, justified as "a VTuber's current look is the
# recent one". That was simply wrong: NoobAI's model card defines `newest` as
# the date bucket **2021-2024**, alongside old/early/mid/recent. It is a
# recency label for the *artwork*, not for the character's design, and NoobAI
# already carries it in its own quality prefix - so adding it here was both
# meaningless and a duplicate. Worse, it was added regardless of checkpoint,
# handing a NoobAI-specific token to Pony and to the photo models.
LIKENESS_TAGS = "official art"


# The quartiles of the measured distribution across all 75 members, so the
# wording is anchored on where this character actually sits rather than on a
# threshold picked to sound decisive. Q1 2.50%, median 3.70%, Q3 5.87%.
RATIO_Q1 = 2.50
RATIO_Q3 = 5.87


def _ratio_note(ratio: float) -> str:
    """How strongly the fan-consensus argument applies to this exact character."""
    if ratio < RATIO_Q1:
        return ("這在 75 位裡屬於<b>偏低的四分之一</b>，"
                "所以模型能學到的主要是「同人平均值」而不是設定圖。")
    if ratio > RATIO_Q3:
        return ("這在 75 位裡屬於<b>偏高的四分之一</b>，"
                "所以「只學到同人平均」對她比較講不通 —— 不像的原因可能在別的地方"
                "（LoRA 強度、解析度、服裝 tag、尺寸）。")
    return ("這大約落在 75 位的<b>中間</b>（中位數 3.7%）。"
            "官方圖仍然是少數，但沒有少到可以斷定「一定學不到」。")


def likeness_advice(pack: Pack, who: Character) -> dict:
    """Why a generated character drifts from the stream model, with numbers.

    This is the most common disappointment with a character LoRA and the reason
    is not a bug, it is what the training data is: danbooru holds mostly fan
    art, so the concept a danbooru-trained model can learn is a *fan consensus*
    rather than the reference sheet.

    How lopsided that is was measured per character rather than asserted, after
    a review pointed out that the earlier version of this docstring quoted a
    flat "1-3% official art" for all 75 members. **That figure was wrong.** It
    came from spot-checking a few of the most popular members and generalising.
    Measured across all 75 on 2026-08-23:

        range      0.62% (Kiryu Coco) to 9.45% (Tokino Sora)
        median     3.7%
        pooled     3.17%  (13,434 official of 424,064 posts)
        above 5%   28 of 74 measurable members

    And the spread is not noise - it tracks popularity, in the direction that
    weakens the original claim rather than the one that flatters it:

        Pearson r (log10 posts vs official %)   -0.646
        members with >=10,000 posts   median 2.08%
        members with  <2,000 posts    median 7.79%

    Which makes sense: official art accrues at a roughly fixed rate per member
    while fan art compounds with popularity, so the *most* drawn members are
    exactly the ones whose official share is thinnest. So the argument holds
    strongly for Gura (1.06%) and barely at all for Tokino Sora (9.45%), and
    the honest thing is to quote the number for the character in front of the
    user instead of a range that fits nobody.

    Even per character, the ratio is corpus prevalence and not a measurement of
    what any checkpoint learned. It is a good reason to expect drift; it is not
    evidence of drift. Only a generation is that.

    Naming the original designer does not fix it either, and the numbers say why
    more clearly than any explanation: of Mori Calliope's 12,544 danbooru posts,
    30 are by her designer Yukisame. Of Hoshimachi Suisei's 15,155, fourteen are
    by Teshima Nari. The artist tag therefore contributes that person's *general*
    style - mostly drawn on other subjects - rather than their rendering of this
    character, which is why it can make likeness worse rather than better.

    The costume tag is offered as an explicit control over the outfit half of
    the identity: `mori_calliope_(1st_costume)` carries 3,136 posts,
    `gawr_gura_(1st_costume)` 7,598, and the official look *is* that outfit.
    That is a reason to give the user the lever, not a finding that it is the
    strongest one. Which lever actually wins is what the fixed-seed benchmark in
    experiments.py exists to answer, and it has not been run.
    """
    costume_tags = [c.trigger for c in who.costumes]
    return {
        "posts": who.danbooru_posts,
        "designer": who.designer,
        "artist_tag": who.artist_tag,
        "artist_posts": who.artist_posts,
        "wiki": who.wiki,
        "costumes": len(costume_tags),
        "official_posts": who.official_posts,
        "official_ratio": who.official_ratio,
        # The number for *this* character, measured, rather than a range that
        # fits nobody. The wording changes with it: at 1% the fan-consensus
        # argument is strong, at 9% it is weak, and pretending otherwise was
        # the thing a review correctly objected to.
        "why": (
            f"danbooru 上 {who.name} 有 {who.danbooru_posts:,} 張，"
            f"其中帶 <code>official art</code> 的有 {who.official_posts:,} 張，"
            f"<b>{who.official_ratio}%</b>。"
            + _ratio_note(who.official_ratio)
            + "（這是 danbooru 的<b>資料比例</b>，不是量到的模型行為。）"
        ) if who.danbooru_posts else "",
        # What the counts support is "not a reliable identity token", which is
        # not the same as "makes it worse" - diffusion composes concepts that
        # rarely co-occur, so the artist tag can carry style without carrying
        # identity. Saying more than that would be inventing a causal claim on
        # top of a correlational one.
        "artist_why": (
            f"{who.designer} 在 danbooru 只有 {who.artist_posts:,} 張，"
            f"其中畫{who.name}的更少 —— 所以這個 tag 帶進來的主要是他<b>畫別人時</b>"
            "的畫風。它是<b>畫風控制</b>，不是身份控制；對「像不像本人」幫不上忙，"
            "至於會不會反而扯後腿，要你自己 A/B 比過才知道。"
        ) if who.artist_tag else "",
    }


def build_prompt(pack: Pack, character_key: str, costume: int = 0, *,
                 extra: str = "", quality: bool = True, model: str = "",
                 style: bool = False, quality_tags: str = "",
                 artist_weight: float = 1.0, likeness: float = 0.0,
                 likeness_tags: str = "") -> dict | None:
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
    # `likeness` weights the costume trigger. That is an *explicit control* over
    # the outfit half of the identity, offered because the outfit is the part
    # fan art reproduces most faithfully - not a claim that it is the strongest
    # identity lever. Which lever wins is what the fixed-seed benchmark in
    # experiments.py is for, and it has not been run.
    head = [weighted(outfit.trigger, likeness) if likeness else outfit.trigger]
    if likeness and likeness_tags.strip():
        # Opt-in only. `likeness_tags` used to default to LIKENESS_TAGS when the
        # caller passed nothing, so calling this function directly - as any
        # script or future endpoint would - silently posted a danbooru general
        # tag to a photo model that has never seen one. The caller knows the
        # checkpoint; this function does not, so it adds nothing it was not
        # given. The HTTP route passes it explicitly after checking tag_style.
        head.append(likeness_tags.strip())
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
            # a few of the per-outfit tag lists. Repeating a tag is not the same
            # mechanism as `(tag:1.1)` - it just puts the token in twice - but it
            # does add conditioning influence nobody asked for, and it wastes
            # context. Tidiness, not arithmetic.
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

"""Guess danbooru tags for an image, so a picture can become a prompt.

This runs SmilingWolf's WD tagger, the model the anime-generation community
actually uses, straight through onnxruntime in this process. No ComfyUI custom
node is involved, so there is nothing to install into ComfyUI and nothing to
break on its next update.

The preprocessing was settled by experiment, not from memory, because every
detail of it fails silently. Feeding the model RGB instead of BGR still returns
confident-looking tags - they are just wrong in ways you would not notice
without ground truth. On ComfyUI's own example.png (a blonde girl in a pink
dress with blue eyes against a blue sky) the two orders give:

    RGB   solo .93, smile .90, dress .78, ... no pink, no blue eyes
    BGR   solo .94, pink_dress .91, 1girl .82, sky .74, blue_eyes .62

The colour-dependent tags are the tell: red and blue are swapped in RGB, so
pink_dress and blue_eyes never surface. BGR it is - the model was trained on
images loaded with cv2.

Tags come out in the form these checkpoints expect: underscores become spaces,
and parentheses are escaped, because in ComfyUI `(x)` is weighting syntax and
an unescaped character name like `rem_(re:zero)` would silently reweight the
rest of the prompt.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

from registry import ModelFile

# Category ids in selected_tags.csv.
CAT_GENERAL = 0
CAT_CHARACTER = 4
CAT_RATING = 9

# SmilingWolf's own defaults for the v3 taggers.
DEFAULT_GENERAL = 0.35
DEFAULT_CHARACTER = 0.85


@dataclass(frozen=True)
class Tagger:
    id: str
    label: str
    model: ModelFile
    labels: ModelFile
    note: str

    @property
    def size(self) -> int:
        return self.model.size + self.labels.size


def _tagger(tagger_id: str, label: str, repo: str, size: int, note: str) -> Tagger:
    # Every one of these repos names its weights model.onnx and its labels
    # selected_tags.csv, so they need a folder each or the second download
    # silently overwrites the first.
    where = f"taggers/{tagger_id}"
    return Tagger(
        id=tagger_id, label=label, note=note,
        model=ModelFile(repo, "model.onnx", where, size),
        labels=ModelFile(repo, "selected_tags.csv", where, 308468),
    )


TAGGERS: list[Tagger] = [
    _tagger(
        "wd-vit-v3", "WD ViT v3（推薦）", "SmilingWolf/wd-vit-tagger-v3", 378536310,
        "378MB。速度和準確度的平衡點，CPU 也跑得動（一張約 1～3 秒）。",
    ),
    _tagger(
        "wd-swinv2-v3", "WD SwinV2 v3", "SmilingWolf/wd-swinv2-tagger-v3", 467460978,
        "467MB。下載數最高的一支，細節標籤略多一點。",
    ),
    _tagger(
        "wd-eva02-v3", "WD EVA02 Large v3", "SmilingWolf/wd-eva02-large-tagger-v3", 1260435999,
        "1.2GB。最準，但慢，CPU 上一張要十幾秒。",
    ),
]

BY_ID = {t.id: t for t in TAGGERS}


def get(tagger_id: str) -> Tagger | None:
    return BY_ID.get(tagger_id)


def folder(models_dir: Path, tagger_id: str) -> Path:
    return models_dir / "taggers" / tagger_id


def installed(models_dir: Path) -> list[str]:
    out = []
    for tagger in TAGGERS:
        base = folder(models_dir, tagger.id)
        if (base / "model.onnx").is_file() and (base / "selected_tags.csv").is_file():
            out.append(tagger.id)
    return out


# -- inference ---------------------------------------------------------------

_ESCAPE = re.compile(r"([()])")
_sessions: dict[str, tuple] = {}


def to_prompt(name: str) -> str:
    """`rem_(re:zero)` -> `rem \\(re:zero\\)`, ready to paste into a prompt."""
    return _ESCAPE.sub(r"\\\1", name.replace("_", " "))


def _load(base: Path) -> tuple:
    key = str(base)
    if key in _sessions:
        return _sessions[key]
    import onnxruntime as ort  # imported lazily: it is a large optional dependency

    session = ort.InferenceSession(
        str(base / "model.onnx"), providers=["CPUExecutionProvider"]
    )
    with (base / "selected_tags.csv").open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    names = [r["name"] for r in rows]
    cats = [int(r["category"]) for r in rows]
    size = int(session.get_inputs()[0].shape[1])
    _sessions[key] = (session, names, cats, size)
    return _sessions[key]


@dataclass
class Guess:
    general: list[tuple[str, float]] = field(default_factory=list)
    characters: list[tuple[str, float]] = field(default_factory=list)
    rating: str = ""
    ratings: list[tuple[str, float]] = field(default_factory=list)

    @property
    def prompt(self) -> str:
        """Characters first, then general tags - the order these models expect."""
        names = [n for n, _ in self.characters] + [n for n, _ in self.general]
        return ", ".join(to_prompt(n) for n in names)

    def parts(self) -> dict[str, list[str]]:
        """The guess split into what it is *of* versus what is happening.

        Sometimes only the staging is wanted - "the pose and the background, I
        will add my own character" - and that is not a matter of deleting the
        character name alone. A tagger describing a picture also reports the
        hair, the eyes and the body, and those follow the character just as
        much as the name does. So the same three buckets the restage feature
        uses are reported here (see classify): `character` is the name, `look`
        is who they are, `outfit` is what they have on, `scene` is the pose,
        the framing and the place.
        """
        split = split_tags([n for n, _ in self.general])
        return {
            "character": [to_prompt(n) for n, _ in self.characters],
            "look": [to_prompt(n) for n in split["look"]],
            "outfit": [to_prompt(n) for n in split["outfit"]],
            "scene": [to_prompt(n) for n in split["scene"]],
            "drop": [to_prompt(n) for n in split["drop"]],
        }

    def public(self) -> dict:
        return {
            "prompt": self.prompt,
            "general": [{"name": to_prompt(n), "raw": n, "p": round(p, 3)}
                        for n, p in self.general],
            "characters": [{"name": to_prompt(n), "raw": n, "p": round(p, 3)}
                           for n, p in self.characters],
            "rating": self.rating,
            "ratings": [{"name": n, "p": round(p, 3)} for n, p in self.ratings],
            "parts": self.parts(),
        }


def describe(
    image,
    base: Path,
    general_threshold: float = DEFAULT_GENERAL,
    character_threshold: float = DEFAULT_CHARACTER,
    limit: int = 40,
) -> Guess:
    """Danbooru tags for a PIL image."""
    import numpy as np
    from PIL import Image

    session, names, cats, size = _load(base)

    # Flatten transparency onto white, pad to a square, then resize. Padding
    # rather than stretching matters: the model reads aspect ratio as content.
    picture = image.convert("RGBA")
    flat = Image.new("RGBA", picture.size, (255, 255, 255, 255))
    flat.alpha_composite(picture)
    picture = flat.convert("RGB")
    side = max(picture.size)
    square = Image.new("RGB", (side, side), (255, 255, 255))
    square.paste(picture, ((side - picture.width) // 2, (side - picture.height) // 2))
    square = square.resize((size, size), Image.BICUBIC)

    array = np.asarray(square, dtype=np.float32)[:, :, ::-1]  # RGB -> BGR
    scores = session.run(None, {session.get_inputs()[0].name: array[None, ...]})[0][0]

    guess = Guess()
    general: list[tuple[str, float]] = []
    characters: list[tuple[str, float]] = []
    for score, name, category in zip(scores, names, cats):
        value = float(score)
        if category == CAT_RATING:
            guess.ratings.append((name, value))
        elif category == CAT_CHARACTER and value >= character_threshold:
            characters.append((name, value))
        elif category == CAT_GENERAL and value >= general_threshold:
            general.append((name, value))
    guess.general = sorted(general, key=lambda x: -x[1])[:limit]
    guess.characters = sorted(characters, key=lambda x: -x[1])[:8]
    guess.ratings.sort(key=lambda x: -x[1])
    guess.rating = guess.ratings[0][0] if guess.ratings else ""
    return guess


# -- splitting a description into "who" and "what is happening" ---------------

# Restaging a page means keeping its blocking and swapping its cast, so the
# tags a panel produces have to be sorted into what belongs to the shot and
# what belongs to the character. Danbooru's vocabulary makes that tractable,
# because the tag families are lexically obvious: `*_hair` and `*_eyes` are
# always the person, `from_above` and `sitting` are always the shot.
#
# Clothing is the genuinely ambiguous family - a signature outfit is part of a
# character, a swimsuit at the beach is part of the scene - so it is kept as a
# third bucket the user assigns, rather than guessed at.

_SCENE_EXACT = {
    "solo", "solo_focus", "multiple_girls", "multiple_boys", "multiple_views",
    "looking_at_viewer", "looking_at_another", "looking_away", "looking_back",
    "looking_down", "looking_up", "looking_to_the_side", "eye_contact",
    "full_body", "upper_body", "lower_body", "cowboy_shot", "portrait",
    "close-up", "profile", "facing_viewer", "facing_away", "dutch_angle",
    "from_above", "from_below", "from_side", "from_behind", "from_outside",
    "pov", "depth_of_field", "blurry_background", "blurry_foreground",
    "sitting", "standing", "kneeling", "squatting", "lying", "on_back",
    "on_stomach", "on_side", "walking", "running", "jumping", "leaning",
    "leaning_forward", "leaning_back", "arms_up", "arm_up", "arms_behind_back",
    "crossed_arms", "spread_arms", "outstretched_arms", "outstretched_hand",
    "hand_on_own_hip", "hands_on_hips", "hand_up", "hand_on_own_face",
    "holding", "hugging", "carrying", "bent_over", "arched_back", "all_fours",
    "spread_legs", "crossed_legs", "legs_up", "knees_up", "kneeling",
    "smile", "grin", "frown", "blush", "open_mouth", "closed_mouth",
    "closed_eyes", "half-closed_eyes", "wide-eyed", "surprised", "angry",
    "sad", "crying", "tears", "embarrassed", "smug", "seductive_smile",
    "indoors", "outdoors", "day", "night", "sunset", "sky", "cloud",
    "simple_background", "white_background", "transparent_background",
    "gradient_background", "sunlight", "backlighting", "dappled_sunlight",
    "hetero", "yuri", "yaoi", "male_focus",
    # How many people are in frame belongs to the shot, not to the character -
    # restaging a two-hander with a new lead still needs two people.
    "1girl", "1boy", "1other", "2girls", "2boys", "3girls", "multiple_boys",
}
_SCENE_SUBSTRINGS = (
    "background", "_focus", "from_", "shot", "angle", "lighting", "_view",
    "sitting", "standing", "lying", "kneeling", "squat", "pose", "looking_",
    "_grab", "_lift", "_hold", "holding_", "leaning", "walking", "running",
)
# Locations and props: anything ending in one of these is set dressing.
_PLACE_WORDS = (
    "room", "classroom", "kitchen", "bathroom", "bedroom", "office", "street",
    "city", "forest", "beach", "ocean", "pool", "park", "cafe", "library",
    "shrine", "train", "car", "bed", "chair", "desk", "table", "window",
    "door", "wall", "floor", "stairs", "rooftop", "garden", "snow", "rain",
)

_LOOK_WORDS = (
    "hair", "eyes", "eye", "eyelashes", "eyebrows", "breasts", "skin",
    "ears", "tail", "horns", "wings", "freckles", "mole", "scar",
    "muscular", "thighs", "fang", "fangs", "beard", "moustache", "hairstyle",
)
_LOOK_EXACT = {
    "ahoge", "braid", "twintails", "ponytail", "sidelocks", "bangs", "ahoge",
    "long_hair", "short_hair", "very_long_hair", "medium_hair", "bald",
    "dark_skin", "pale_skin", "tan", "petite", "curvy", "toned", "abs",
    "thighs", "collarbone",
}

# How much skin is showing follows from the outfit and the pose, so it travels
# with whichever of those the user picks rather than with the face.
_EXPOSURE = {
    "cleavage", "nipples", "navel", "ass", "bare_shoulders", "bare_arms",
    "bare_legs", "midriff", "sideboob", "underboob", "cameltoe",
}

# Whole words, matched against the tag's own words - see _has_word.
_OUTFIT_WORDS = (
    "shirt", "skirt", "dress", "uniform", "jacket", "coat", "sweater",
    "hoodie", "pants", "shorts", "socks", "thighhighs", "pantyhose",
    "gloves", "glove", "hat", "cap", "ribbon", "bow", "necktie", "tie",
    "scarf", "shoes", "boots", "sandals", "swimsuit", "bikini", "lingerie",
    "panties", "bra", "underwear", "apron", "cape", "armor", "kimono",
    "leotard", "sleeves", "collar", "jewelry", "earrings", "necklace",
    "glasses", "mask", "ornament", "headband", "hairband", "choker",
    "frills", "sleeveless", "costume", "clothes", "clothing", "outfit",
    "nude", "naked", "topless", "bottomless", "barefoot", "hairclip",
    "hairpin", "veil", "crown", "belt", "bag", "backpack",
)

# Never carried across: they describe the medium, not the picture.
_DROP = {
    "comic", "4koma", "2koma", "3koma", "monochrome", "greyscale", "sketch",
    "lineart", "traditional_media", "speech_bubble", "text", "english_text",
    "japanese_text", "translated", "commentary", "commentary_request",
    "artist_name", "signature", "watermark", "username", "web_address",
    "highres", "absurdres", "lowres", "border", "panels", "halftone",
    "screentone", "censored", "mosaic_censoring", "bar_censor",
}


def _words(tag: str) -> list[str]:
    """danbooru tags are underscore-separated words; treat them as such."""
    return [w for w in re.split(r"[_\-()]+", tag) if w]


def _has_word(tag: str, vocabulary: tuple[str, ...]) -> bool:
    """Whole-word match, not a substring.

    Naive `in` matching is what put `landscape`, `cityscape` and `library` into
    the clothing bucket (all contain a garment or accessory as a substring:
    "cape", "cape", "bra"), and `rainbow`/`elbow`/`bowing` followed "bow". With
    "outfit from my character" on, the whole bucket is discarded - so those
    backgrounds simply vanished from the restaged panel.
    """
    return any(word in vocabulary for word in _words(tag))


def _has_suffix(tag: str, vocabulary: tuple[str, ...]) -> bool:
    """For families named by their last word: `school_uniform`, `blue_eyes`."""
    words = _words(tag)
    return bool(words) and words[-1] in vocabulary


def classify(name: str) -> str:
    """'scene' | 'look' | 'outfit' | 'drop' for one danbooru tag."""
    tag = name.strip().lower().replace(" ", "_")
    if tag in _DROP:
        return "drop"
    if tag in _SCENE_EXACT:
        return "scene"
    if tag in _LOOK_EXACT:
        return "look"
    if tag in _EXPOSURE:
        return "outfit"
    # Places win over everything: `library` and `cityscape` are rooms and views,
    # whatever garment their letters happen to spell.
    if _has_word(tag, _PLACE_WORDS) or _has_suffix(tag, _PLACE_WORDS):
        return "scene"
    if _has_word(tag, _OUTFIT_WORDS) or _has_suffix(tag, _OUTFIT_WORDS):
        return "outfit"
    if _has_word(tag, _LOOK_WORDS) or _has_suffix(tag, _LOOK_WORDS):
        return "look"
    if any(word in tag for word in _SCENE_SUBSTRINGS):
        return "scene"
    # Unknown tags describe the picture more often than the person, and a
    # stray scene tag is a much smaller mistake than dropping the character's
    # defining feature, so the shot is the safer default.
    return "scene"


def split_tags(names: list[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {"scene": [], "look": [], "outfit": [], "drop": []}
    for name in names:
        out[classify(name)].append(name)
    return out


# -- turning a guess into advice ---------------------------------------------

# Tags that say "this is a photo", so a realism checkpoint suits it better than
# an anime one. Everything else defaults to the anime side, which is what the
# tagger itself is trained on.
PHOTO_TAGS = {"realistic", "photorealistic", "photo_(medium)", "3d"}
RATING_LABEL = {
    "general": "全年齡",
    "sensitive": "有點擦邊",
    "questionable": "成人邊緣",
    "explicit": "成人內容",
}


def suggest_model(guess: Guess) -> str:
    raw = {n for n, _ in guess.general}
    if raw & PHOTO_TAGS:
        return "juggernaut"
    return "illustrious"


def matching_loras(guess: Guess, installed_loras: list[dict]) -> list[dict]:
    """Installed LoRAs whose trigger words appear in the guessed tags.

    This is a hint, not identification. Nothing in an image says which LoRA made
    it; all this can honestly say is "you have a LoRA whose trigger words match
    what is in this picture".
    """
    words = {n.replace("_", " ").lower() for n, _ in guess.general + guess.characters}
    out = []
    for lora in installed_loras:
        hits = [
            w for w in (lora.get("trained_words") or [])
            if w and w.replace("_", " ").lower() in words
        ]
        if hits:
            out.append({"name": lora["name"], "label": lora.get("label") or lora["name"],
                        "matched": hits[:4]})
    return out

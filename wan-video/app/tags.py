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


def unload() -> None:
    _sessions.clear()


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

    def public(self) -> dict:
        return {
            "prompt": self.prompt,
            "general": [{"name": to_prompt(n), "raw": n, "p": round(p, 3)}
                        for n, p in self.general],
            "characters": [{"name": to_prompt(n), "raw": n, "p": round(p, 3)}
                           for n, p in self.characters],
            "rating": self.rating,
            "ratings": [{"name": n, "p": round(p, 3)} for n, p in self.ratings],
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

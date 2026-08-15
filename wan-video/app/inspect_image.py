"""Work out how an image was made, from the image.

Two very different things, kept apart because one is fact and the other is
opinion, and a UI that blurs them is worse than useless.

**Reading** (`read_metadata`) is exact. Generators write their settings into
the file and nobody strips them unless they mean to:

- ComfyUI puts the whole API-format graph in a PNG text chunk called `prompt`
  (nodes.py: `metadata.add_text("prompt", json.dumps(prompt))`), and the editor
  graph in `workflow`. Everything is recoverable - checkpoint, every LoRA and
  its strength, seed, steps, cfg, sampler, scheduler, size.
- Automatic1111 / Forge write one `parameters` chunk in their own text format,
  and the same string into EXIF UserComment for JPEG and WebP.
- CivitAI serves A1111-format `parameters` on downloads that keep metadata.

**Guessing** (`tags.py`) is a model looking at pixels. It can describe what is
in a picture; it cannot know which LoRA made it. Those are labelled differently
everywhere they surface.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from PIL import Image

# EXIF tag id for UserComment, where A1111 hides the same string in a JPEG.
EXIF_USER_COMMENT = 0x9286


@dataclass
class Found:
    """What an image admitted to, and how sure we are of it."""

    source: str = ""  # comfyui | a1111 | none
    prompt: str = ""
    negative: str = ""
    model: str = ""
    loras: list[dict] = field(default_factory=list)  # {name, strength, strength_clip}
    seed: int | None = None
    steps: int | None = None
    cfg: float | None = None
    sampler: str = ""
    scheduler: str = ""
    width: int = 0
    height: int = 0
    clip_skip: int | None = None
    extras: dict = field(default_factory=dict)
    note: str = ""

    def public(self) -> dict:
        return {
            "source": self.source, "prompt": self.prompt, "negative": self.negative,
            "model": self.model, "loras": self.loras, "seed": self.seed,
            "steps": self.steps, "cfg": self.cfg, "sampler": self.sampler,
            "scheduler": self.scheduler, "width": self.width, "height": self.height,
            "clip_skip": self.clip_skip, "extras": self.extras, "note": self.note,
        }


def read_metadata(image: Image.Image) -> Found:
    """Recover the generation settings, or return an empty Found."""
    text: dict[str, str] = dict(getattr(image, "text", {}) or {})
    for key in ("prompt", "workflow", "parameters"):
        value = image.info.get(key)
        if isinstance(value, str):
            text.setdefault(key, value)

    if "prompt" in text:
        if found := _from_comfy(text["prompt"]):
            return found
    if "parameters" in text:
        if found := _from_a1111(text["parameters"]):
            return found
    if comment := _exif_comment(image):
        if found := _from_a1111(comment):
            return found
    if "workflow" in text:
        # A UI graph with no API graph: widget values are positional, so this is
        # far less reliable. Say what it is rather than pretending otherwise.
        return Found(source="comfyui", note="這張圖只帶了 ComfyUI 的畫布資料，沒有完整參數。")
    return Found()


def _exif_comment(image: Image.Image) -> str:
    try:
        exif = image.getexif()
    except Exception:  # noqa: BLE001 - a broken EXIF block is not an error here
        return ""
    raw = None
    for source in (exif, exif.get_ifd(0x8769) if hasattr(exif, "get_ifd") else {}):
        try:
            raw = (source or {}).get(EXIF_USER_COMMENT)
        except Exception:  # noqa: BLE001
            raw = None
        if raw:
            break
    if not raw:
        return ""
    if isinstance(raw, bytes):
        # A1111 writes "UNICODE\0" then UTF-16-BE.
        if raw[:8] in (b"UNICODE\x00", b"UNICODE\0"):
            try:
                return raw[8:].decode("utf-16-be", errors="replace")
            except Exception:  # noqa: BLE001
                return ""
        return raw.decode("utf-8", errors="replace")
    return str(raw)


# -- ComfyUI -----------------------------------------------------------------

# Which node classes mean what. Anything unknown is ignored rather than guessed.
CKPT_NODES = {"CheckpointLoaderSimple", "CheckpointLoader", "UNETLoader", "UnetLoaderGGUF"}
LORA_NODES = {"LoraLoader", "LoraLoaderModelOnly"}
SAMPLER_NODES = {"KSampler", "KSamplerAdvanced"}


def _from_comfy(raw: str) -> Found | None:
    try:
        graph = json.loads(raw)
    except (ValueError, TypeError):
        return None
    if not isinstance(graph, dict) or not graph:
        return None
    nodes = {
        k: v for k, v in graph.items()
        if isinstance(v, dict) and isinstance(v.get("inputs"), dict) and v.get("class_type")
    }
    if not nodes:
        return None

    found = Found(source="comfyui")
    for node in nodes.values():
        cls, inputs = node["class_type"], node["inputs"]
        if cls in CKPT_NODES and not found.model:
            for key in ("ckpt_name", "unet_name"):
                if isinstance(inputs.get(key), str):
                    found.model = inputs[key]
                    break
        elif cls in LORA_NODES and isinstance(inputs.get("lora_name"), str):
            model_s = _number(inputs.get("strength_model"), 1.0)
            found.loras.append(
                {
                    "name": inputs["lora_name"],
                    "strength": model_s,
                    "strength_clip": _number(inputs.get("strength_clip"), model_s),
                }
            )
        elif cls == "CLIPSetLastLayer":
            found.clip_skip = int(_number(inputs.get("stop_at_clip_layer"), -1))
        elif cls == "EmptyLatentImage" and not found.width:
            found.width = int(_number(inputs.get("width"), 0))
            found.height = int(_number(inputs.get("height"), 0))

    sampler = _main_sampler(nodes)
    if sampler is not None:
        inputs = sampler["inputs"]
        found.steps = int(_number(inputs.get("steps"), 0)) or None
        found.cfg = _number(inputs.get("cfg"), 0.0) or None
        found.sampler = str(inputs.get("sampler_name") or "")
        found.scheduler = str(inputs.get("scheduler") or "")
        seed = inputs.get("seed", inputs.get("noise_seed"))
        if isinstance(seed, (int, float)):
            found.seed = int(seed)
        found.prompt = _text_behind(nodes, inputs.get("positive"))
        found.negative = _text_behind(nodes, inputs.get("negative"))

    if not (found.prompt or found.model or found.loras):
        return None
    return found


def _main_sampler(nodes: dict) -> dict | None:
    """The sampler whose result is saved.

    A hi-res workflow has two or more; the interesting one is the last in the
    chain, so prefer a sampler no other sampler feeds from.
    """
    samplers = {k: v for k, v in nodes.items() if v["class_type"] in SAMPLER_NODES}
    if not samplers:
        return None
    upstream: set[str] = set()
    for node in samplers.values():
        for value in node["inputs"].values():
            if isinstance(value, list) and len(value) == 2 and str(value[0]) in samplers:
                upstream.add(str(value[0]))
    tail = [k for k in samplers if k not in upstream]
    return samplers[tail[-1] if tail else list(samplers)[-1]]


def _text_behind(nodes: dict, link: Any, depth: int = 0) -> str:
    """Follow a conditioning link back to the text that produced it."""
    if depth > 8 or not (isinstance(link, list) and len(link) == 2):
        return ""
    node = nodes.get(str(link[0]))
    if node is None:
        return ""
    inputs = node["inputs"]
    for key in ("text", "text_g", "prompt"):
        if isinstance(inputs.get(key), str):
            return inputs[key]
    for key in ("conditioning", "conditioning_1", "conditioning_to", "positive", "negative"):
        if key in inputs:
            if text := _text_behind(nodes, inputs[key], depth + 1):
                return text
    return ""


def _number(value: Any, default: float) -> float:
    return float(value) if isinstance(value, (int, float)) else default


# -- Automatic1111 -----------------------------------------------------------

_SETTINGS = re.compile(r"([A-Za-z][\w \-/]*?):\s*("
                       r'"[^"]*"'          # quoted, e.g. Lora hashes: "a: 1234"
                       r"|[^,]*)"          # or up to the next comma
                       )
_INLINE_LORA = re.compile(r"<lora:([^:>]+)(?::([\d.]+))?(?::([\d.]+))?>", re.I)


def _from_a1111(raw: str) -> Found | None:
    text = (raw or "").strip()
    if not text:
        return None
    negative, settings_line = "", ""
    body = text
    if "Negative prompt:" in text:
        body, _, rest = text.partition("Negative prompt:")
        negative, _, settings_line = rest.partition("\n")
    else:
        lines = text.rsplit("\n", 1)
        if len(lines) == 2 and "Steps:" in lines[1]:
            body, settings_line = lines
    if not settings_line and "Steps:" not in text:
        return None

    settings = {}
    for key, value in _SETTINGS.findall(settings_line):
        settings[key.strip()] = value.strip().strip('"')

    found = Found(source="a1111", prompt=body.strip(), negative=negative.strip())
    found.model = settings.get("Model", "")
    found.sampler = settings.get("Sampler", "")
    found.scheduler = settings.get("Schedule type", "")
    for key, attr, cast in (
        ("Steps", "steps", int), ("Seed", "seed", int),
        ("CFG scale", "cfg", float), ("Clip skip", "clip_skip", int),
    ):
        if key in settings:
            try:
                setattr(found, attr, cast(float(settings[key])))
            except (TypeError, ValueError):
                pass
    if found.clip_skip is not None and found.clip_skip > 0:
        # A1111 counts up from 1, ComfyUI counts down from -1.
        found.clip_skip = -abs(found.clip_skip)
    if size := settings.get("Size", ""):
        parts = size.lower().split("x")
        if len(parts) == 2 and all(p.strip().isdigit() for p in parts):
            found.width, found.height = int(parts[0]), int(parts[1])

    # LoRAs appear inline in the prompt and/or as a "Lora hashes" list.
    for name, strength, _ in _INLINE_LORA.findall(found.prompt):
        found.loras.append(
            {"name": name.strip(), "strength": float(strength or 1.0),
             "strength_clip": float(strength or 1.0)}
        )
    if hashes := settings.get("Lora hashes", ""):
        known = {l["name"] for l in found.loras}
        for chunk in hashes.split(","):
            name = chunk.split(":")[0].strip()
            if name and name not in known:
                found.loras.append({"name": name, "strength": 1.0, "strength_clip": 1.0})
    found.extras = {
        k: v for k, v in settings.items()
        if k not in ("Steps", "Seed", "CFG scale", "Sampler", "Model", "Size",
                     "Clip skip", "Lora hashes", "Schedule type")
    }
    return found

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
- NovelAI writes PNG text fields (`Software: NovelAI`, `Source` = model,
  `Comment` = JSON with prompt, `uc`, seed, steps, scale, sampler, V4
  character captions) *and* a gzip copy of them in the lowest bit of the
  alpha channel ("stealth_pngcomp"), which survives sites that strip text
  chunks but keep the PNG lossless. Format taken from NovelAI's own reader,
  github.com/NovelAI/novelai-image-metadata (nai_meta.py). The A1111
  extension sd-webui-stealth-pnginfo uses the same layout for its
  `parameters` string ("stealth_pnginfo" uncompressed, or "stealth_pngcomp").

**Guessing** (`tags.py`) is a model looking at pixels. It can describe what is
in a picture; it cannot know which LoRA made it. Those are labelled differently
everywhere they surface.
"""

from __future__ import annotations

import json
import re
import zlib
from dataclasses import dataclass, field
from typing import Any

from PIL import Image

import prompts

# EXIF tag id for UserComment, where A1111 hides the same string in a JPEG.
EXIF_USER_COMMENT = 0x9286


@dataclass
class Found:
    """What an image admitted to, and how sure we are of it."""

    source: str = ""  # comfyui | a1111 | novelai | civitai | none
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
    # What lets a model be looked up rather than guessed at by name: A1111's
    # short model hash, and the exact CivitAI version ids an image made on
    # CivitAI lists in "Civitai resources". See reverse.resolve.
    model_hash: str = ""
    resources: list[dict] = field(default_factory=list)  # {type, version_id, name, weight}
    extras: dict = field(default_factory=dict)
    note: str = ""

    def public(self) -> dict:
        return {
            "source": self.source, "prompt": self.prompt, "negative": self.negative,
            "model": self.model, "loras": self.loras, "seed": self.seed,
            "steps": self.steps, "cfg": self.cfg, "sampler": self.sampler,
            "scheduler": self.scheduler, "width": self.width, "height": self.height,
            "clip_skip": self.clip_skip, "extras": self.extras, "note": self.note,
            "model_hash": self.model_hash, "resources": self.resources,
        }


def read_metadata(image: Image.Image) -> Found:
    """Recover the generation settings, or return an empty Found."""
    text: dict[str, str] = dict(getattr(image, "text", {}) or {})
    for key in ("prompt", "workflow", "parameters"):
        value = image.info.get(key)
        if isinstance(value, str):
            text.setdefault(key, value)

    partial = None
    if "prompt" in text:
        if found := _from_comfy(text["prompt"]):
            if found.prompt:
                return found
            # A graph built from nodes this reader does not know (a new model's
            # own sampler, say) gives a model name and nothing else. Keep it in
            # case nothing better turns up - CivitAI's generator, for one, also
            # writes a complete A1111 `parameters` block into the same file.
            partial = found
    if "parameters" in text:
        if found := _from_a1111(text["parameters"]):
            return found
    if partial is not None:
        return partial
    if comment := _exif_comment(image):
        if found := _from_a1111(comment):
            return found
    if "Comment" in text:
        if found := _from_novelai(text):
            return found
    hidden = read_stealth(image)
    if isinstance(hidden, dict):
        if found := _from_novelai(hidden):
            found.note = (found.note + " " if found.note else "") + "（這份資料是從圖片的透明通道讀出來的。）"
            return found
    elif isinstance(hidden, str):
        if found := _from_a1111(hidden):
            found.note = "這份參數藏在圖片的透明通道裡（stealth pnginfo），不是一般的文字欄位。"
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


# -- NovelAI -----------------------------------------------------------------

STEALTH_MAGICS = (b"stealth_pngcomp", b"stealth_pnginfo")
STEALTH_HEADER = 15 + 4            # the magic, then the payload length in bits
MAX_STEALTH = 4 * 1024 * 1024      # far above any real payload; a cap on a crafted one
# NovelAI's sampler and schedule names, in ComfyUI's words.
NAI_SAMPLERS = {"ddim_v3": "ddim"}
NAI_SCHEDULES = {"native": "normal"}


def read_stealth(image: Image.Image) -> dict | str | None:
    """Settings hidden in the lowest bit of the alpha channel, if any.

    Bits run down each column, then across (NovelAI reads `alpha.T`), eight
    to a byte, most significant first. Only the columns the payload needs are
    read, so a large picture costs no more than a small one.
    """
    if "A" not in image.getbands():
        return None
    import numpy as np

    alpha = np.asarray(image.getchannel("A"), dtype=np.uint8)
    height, width = alpha.shape
    if not height or not width:
        return None

    def first(count: int) -> bytes | None:
        bits_needed = count * 8
        columns = -(-bits_needed // height)
        if columns > width:
            return None
        bits = (alpha[:, :columns].T.reshape(-1) & 1)[:bits_needed]
        return np.packbits(bits).tobytes()

    head = first(STEALTH_HEADER)
    if not head or head[:15] not in STEALTH_MAGICS:
        return None
    size = int.from_bytes(head[15:19], "big") // 8
    if size <= 0 or size > MAX_STEALTH:
        return None
    data = first(STEALTH_HEADER + size)
    if data is None:
        return None
    payload = data[STEALTH_HEADER:]
    if head[:15] == b"stealth_pngcomp":
        unpack = zlib.decompressobj(wbits=31)          # gzip
        try:
            payload = unpack.decompress(payload, MAX_STEALTH)
        except zlib.error:
            return None
        if not unpack.eof:                             # truncated, or bigger than the cap
            return None
    text = payload.decode("utf-8", errors="replace")
    if not text.strip():
        return None
    try:
        parsed = json.loads(text)
    except ValueError:
        return text
    return parsed if isinstance(parsed, dict) else text


def _from_novelai(fields: dict) -> Found | None:
    comment = fields.get("Comment")
    if isinstance(comment, str):
        try:
            comment = json.loads(comment)
        except ValueError:
            return None
    if not isinstance(comment, dict):
        return None
    software = str(fields.get("Software") or "")
    if not (software.startswith("NovelAI") or "uc" in comment or "v4_prompt" in comment):
        return None

    def caption(block) -> tuple[str, list[str]]:
        inner = (block or {}).get("caption") if isinstance(block, dict) else None
        if not isinstance(inner, dict):
            return "", []
        chars = [str(c.get("char_caption") or "").strip()
                 for c in inner.get("char_captions") or [] if isinstance(c, dict)]
        return str(inner.get("base_caption") or ""), [c for c in chars if c]

    base, chars = caption(comment.get("v4_prompt"))
    nbase, nchars = caption(comment.get("v4_negative_prompt"))
    prompt = str(comment.get("prompt") or base or fields.get("Description") or "")
    negative = str(comment.get("uc") or nbase or "")
    # NovelAI V4 keeps each character's prompt in its own box with a position.
    # The models here have one prompt, so they follow the scene description.
    parts = [prompts.from_novelai(prompt)] + [prompts.from_novelai(c) for c in chars]
    neg_parts = [prompts.from_novelai(negative)] + [prompts.from_novelai(c) for c in nchars]

    def number(key: str, kind):
        try:
            return kind(comment[key]) if comment.get(key) is not None else None
        except (TypeError, ValueError):
            return None

    sampler = str(comment.get("sampler") or "")
    sampler = NAI_SAMPLERS.get(sampler, sampler[2:] if sampler.startswith("k_") else sampler)
    schedule = str(comment.get("noise_schedule") or "")
    found = Found(
        source="novelai",
        prompt=", ".join(p for p in parts if p.strip()),
        negative=", ".join(p for p in neg_parts if p.strip()),
        model=str(fields.get("Source") or software or "NovelAI"),
        seed=number("seed", int), steps=number("steps", int), cfg=number("scale", float),
        sampler=sampler, scheduler=NAI_SCHEDULES.get(schedule, schedule),
        width=number("width", int) or 0, height=number("height", int) or 0,
        note=("NovelAI 的模型不公開，這裡用不到它：提詞可以直接拿去 NoobAI／Illustrious 用"
              "（NovelAI 的加重寫法 {}、[]、1.2:: 已經換成這邊的 (詞:1.1)），種子和取樣器換了模型就不會一樣。"),
    )
    if chars:
        found.extras["characters"] = chars
        found.note += " V4 的分角色提詞已經接在主提詞後面（這邊的底模沒有分角色的欄位）。"
    return found


# -- CivitAI image pages ---------------------------------------------------------

_CIVITAI_IMAGE = re.compile(r"(?:^|/images/)(\d{3,})(?:[/?#]|$)")


def civitai_image_id(text: str) -> int | None:
    """The image id in a CivitAI image link (or a bare id)."""
    text = (text or "").strip()
    if text.isdigit():
        return int(text)
    match = _CIVITAI_IMAGE.search(text)
    return int(match.group(1)) if match and "civitai" in text.lower() else None


def from_civitai_meta(meta: dict) -> Found | None:
    """The generation data CivitAI shows beside a posted image.

    Read from its images API (`meta`, checked against live answers on
    2026-11-27): prompt, negativePrompt, seed, steps, sampler, scheduler,
    cfgScale, width/height (or an older "Size"), Model, `civitaiResources`
    with exact version ids, LoRAs by name in `resources` or
    `additionalResources`, and - for ComfyUI uploads - the whole API graph in
    `comfy`, which is read the same way as a ComfyUI PNG.
    """
    if not isinstance(meta, dict) or not meta:
        return None
    # Asked for one image (imageId=), CivitAI wraps it: {"id": ..., "meta": {...}}.
    # Listings give the inner dict directly. Both seen live on 2026-11-27.
    if isinstance(meta.get("meta"), dict):
        meta = meta["meta"]
    found = None
    comfy = meta.get("comfy")
    if isinstance(comfy, str):
        try:
            graph = json.loads(comfy)
        except ValueError:
            graph = None
        if isinstance(graph, dict) and isinstance(graph.get("prompt"), dict):
            found = _from_comfy(json.dumps(graph["prompt"]))
            if found is not None and not found.width:
                try:
                    found.width, found.height = int(meta.get("width") or 0), int(meta.get("height") or 0)
                except (TypeError, ValueError):
                    pass
    if found is None:
        prompt = str(meta.get("prompt") or "")
        if not prompt:
            return None
        found = Found(prompt=prompt, negative=str(meta.get("negativePrompt") or ""),
                      model=str(meta.get("Model") or ""), sampler=str(meta.get("sampler") or ""),
                      scheduler=str(meta.get("scheduler") or ""),
                      model_hash=str(meta.get("Model hash") or ""))
        for key, attr, cast in (("seed", "seed", int), ("steps", "steps", int),
                                ("cfgScale", "cfg", float), ("clipSkip", "clip_skip", int),
                                ("width", "width", int), ("height", "height", int)):
            try:
                if meta.get(key) is not None:
                    setattr(found, attr, cast(meta[key]))
            except (TypeError, ValueError):
                pass
        if found.clip_skip is not None and found.clip_skip > 0:
            found.clip_skip = -found.clip_skip
        size = str(meta.get("Size") or "").lower().split("x")
        if not found.width and len(size) == 2 and all(s.strip().isdigit() for s in size):
            found.width, found.height = int(size[0]), int(size[1])
        for entry in (meta.get("resources") or []) + (meta.get("additionalResources") or []):
            if isinstance(entry, dict) and str(entry.get("type", "")).lower() == "lora" and entry.get("name"):
                strength = entry.get("weight", entry.get("strength", 1.0))
                try:
                    strength = float(strength)
                except (TypeError, ValueError):
                    strength = 1.0
                lora = {"name": str(entry["name"]), "strength": strength, "strength_clip": strength}
                if entry.get("hash"):
                    lora["hash"] = str(entry["hash"])
                found.loras.append(lora)
    found.source = "civitai"
    for entry in meta.get("civitaiResources") or []:
        if isinstance(entry, dict) and str(entry.get("modelVersionId") or "").isdigit():
            found.resources.append({
                "type": str(entry.get("type") or "").lower(),
                "version_id": int(entry["modelVersionId"]),
                "name": str(entry.get("modelVersionName") or entry.get("modelName") or ""),
                "weight": entry.get("weight"),
            })
    found.note = ("這是 CivitAI 圖片頁上作者附的生成資料（不是猜的）。"
                  "模型和 LoRA 有版本編號的，下面「查 CivitAI」會直接找到那一版。")
    return found


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

    # A JSON list inside a comma-separated line: cut it out before the simple
    # key/value split below, which would shred it at its first comma.
    resources: list[dict] = []
    marker = "Civitai resources:"
    if marker in settings_line:
        head, _, tail = settings_line.partition(marker)
        try:
            listed, used = json.JSONDecoder().raw_decode(tail.lstrip())
            tail = tail.lstrip()[used:]
        except ValueError:
            listed = []
        for entry in listed if isinstance(listed, list) else []:
            if isinstance(entry, dict) and entry.get("modelVersionId"):
                resources.append({
                    "type": str(entry.get("type") or "").lower(),
                    "version_id": int(entry["modelVersionId"]),
                    "name": str(entry.get("modelName") or ""),
                    "weight": entry.get("weight"),
                })
        settings_line = head + tail

    settings = {}
    for key, value in _SETTINGS.findall(settings_line):
        settings[key.strip()] = value.strip().strip('"')

    found = Found(source="a1111", prompt=body.strip(), negative=negative.strip())
    found.model = settings.get("Model", "")
    found.model_hash = settings.get("Model hash", "")
    found.resources = resources
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
        by_name = {l["name"]: l for l in found.loras}
        for chunk in hashes.split(","):
            name, _, digest = chunk.partition(":")
            name, digest = name.strip(), digest.strip()
            if not name:
                continue
            if name not in by_name:
                by_name[name] = {"name": name, "strength": 1.0, "strength_clip": 1.0}
                found.loras.append(by_name[name])
            if digest:
                by_name[name]["hash"] = digest
    found.extras = {
        k: v for k, v in settings.items()
        if k not in ("Steps", "Seed", "CFG scale", "Sampler", "Model", "Size",
                     "Clip skip", "Lora hashes", "Schedule type")
    }
    return found

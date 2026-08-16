"""Builds ComfyUI API-format graphs for each supported model family.

Graphs are assembled in code rather than loaded from an exported .json so that
resolution, clip length, LoRAs and step counts stay config-driven. Node class
names and parameter values were checked against a real ComfyUI 0.33.0
/object_info; comfy_client.validate() re-checks them against the target
install before anything is submitted.
"""

from __future__ import annotations

import math

from registry import GenParams, Lora, ModelDef

# Kept as module-level aliases so existing callers/tests keep working.
from registry import WAN_NEGATIVE as DEFAULT_NEGATIVE  # noqa: F401

TIERS = {"480p": 832 * 480, "704p": 1280 * 704, "720p": 1280 * 720}


def tier_budget(model: ModelDef | None, tier: str) -> int:
    """Pixel budget for a tier, preferring the model's own canonical sizes."""
    if model and tier in model.tiers:
        w, h = model.tiers[tier]
        return w * h
    return TIERS.get(tier, TIERS["480p"])


def fit_dimensions(width: int, height: int, tier: str, model: ModelDef | None = None) -> tuple[int, int]:
    """Scale the source image to the tier's pixel budget, keeping aspect ratio.

    Snapped to a multiple of 16: the video VAEs downsample by 8 or 16 and the
    DiT patchifies on top of that.
    """
    budget = tier_budget(model, tier)
    scale = math.sqrt(budget / max(1, width * height))
    w = max(16, int(round(width * scale / 16)) * 16)
    h = max(16, int(round(height * scale / 16)) * 16)
    return w, h


def frames_for_seconds(seconds: float, fps: int) -> int:
    """The official Wan template computes floor(seconds * fps + 1).

    Duration is the number people actually think in; frames are an artefact of
    how the model is built. The UI asks for seconds and derives this.
    """
    return normalize_length(int(seconds * fps) + 1)


def seconds_for_frames(frames: int, fps: int) -> float:
    return round(frames / fps, 2) if fps else 0.0


def normalize_length(frames: int) -> int:
    """Every supported model compresses time 4:1, so frame count must be 4n+1."""
    frames = max(5, min(frames, 241))
    return ((frames - 1) // 4) * 4 + 1


class GraphBuilder:
    def __init__(self) -> None:
        self.nodes: dict[str, dict] = {}
        self._n = 0

    def add(self, class_type: str, inputs: dict, title: str | None = None) -> str:
        self._n += 1
        node_id = str(self._n)
        self.nodes[node_id] = {
            "class_type": class_type,
            "inputs": inputs,
            "_meta": {"title": title or class_type},
        }
        return node_id


def _lora_chain(g: GraphBuilder, model_node: str, loras: list[Lora]) -> str:
    chain = model_node
    for lora in loras:
        chain = g.add(
            "LoraLoaderModelOnly",
            {"model": [chain, 0], "lora_name": lora.name, "strength_model": lora.strength},
            f"LoRA {lora.name}",
        )
    return chain


def output_fps(p: GenParams, nodes: set[str]) -> int:
    """The frame rate the saved file will really have.

    Interpolation is skipped when the install lacks the nodes for it, so the
    requested multiplier is not what the clip plays at. Reporting the request
    instead of the result makes a card claim "@32fps（補幀）" over a 16fps file.
    """
    if p.interpolate > 1 and p.interpolate_model and \
            {"FrameInterpolationModelLoader", "FrameInterpolate"} <= nodes:
        return int(round(p.fps * p.interpolate))
    return p.fps


def _post_process(g: GraphBuilder, images: str, p: GenParams, nodes: set[str]) -> tuple[str, int]:
    """Optional smoothing and enlargement between the decode and the save.

    Both operate on the decoded frames, so they are ordinary image nodes applied
    to a video batch - which is exactly what ComfyUI's own gan_upscaler template
    does. Interpolation runs first: doubling the frames and *then* upscaling
    them is the same picture for less work than the other order, because the
    interpolator is cheaper at the smaller size.
    """
    fps = p.fps
    if p.interpolate > 1 and p.interpolate_model and \
            {"FrameInterpolationModelLoader", "FrameInterpolate"} <= nodes:
        loader = g.add(
            "FrameInterpolationModelLoader",
            {"model_name": p.interpolate_model},
            "Interpolation model",
        )
        images = g.add(
            "FrameInterpolate",
            {
                "interp_model": [loader, 0],
                "images": [images, 0],
                "multiplier": max(2, min(int(p.interpolate), 16)),
            },
            "Smooth",
        )
        # More frames over the same wall-clock seconds means a higher frame rate,
        # not a slow-motion clip - so the save node has to be told.
        fps = int(round(p.fps * p.interpolate))
    if p.upscaler and {"UpscaleModelLoader", "ImageUpscaleWithModel"} <= nodes:
        loader = g.add("UpscaleModelLoader", {"model_name": p.upscaler}, "Upscale model")
        images = g.add(
            "ImageUpscaleWithModel",
            {"upscale_model": [loader, 0], "image": [images, 0]},
            "Upscale",
        )
    return images, fps


def _video_output(g: GraphBuilder, images: str, fps: int, prefix: str, nodes: set[str]) -> None:
    """Attach the best available save node for this ComfyUI install."""
    if "CreateVideo" in nodes and "SaveVideo" in nodes:
        video = g.add("CreateVideo", {"images": [images, 0], "fps": fps}, "Assemble video")
        g.add(
            "SaveVideo",
            {"video": [video, 0], "filename_prefix": prefix, "format": "mp4", "codec": "h264"},
            "Save mp4",
        )
    elif "VHS_VideoCombine" in nodes:
        g.add(
            "VHS_VideoCombine",
            {
                "images": [images, 0],
                "frame_rate": fps,
                "loop_count": 0,
                "filename_prefix": prefix,
                "format": "video/h264-mp4",
                "pix_fmt": "yuv420p",
                "crf": 19,
                "save_metadata": True,
                "pingpong": False,
                "save_output": True,
            },
            "Save mp4 (VHS)",
        )
    else:
        # Always present in core ComfyUI, so there is always some output.
        g.add(
            "SaveAnimatedWEBP",
            {
                "images": [images, 0],
                "filename_prefix": prefix,
                "fps": fps,
                "lossless": False,
                "quality": 90,
                "method": "default",
            },
            "Save webp",
        )


def _diffusion_loader(g: GraphBuilder, model: ModelDef, filename: str, dtype: str, title: str) -> str:
    if filename.endswith(".gguf"):
        return g.add("UnetLoaderGGUF", {"unet_name": filename}, title)
    return g.add("UNETLoader", {"unet_name": filename, "weight_dtype": dtype}, title)


def _main_files(model: ModelDef, folder: str) -> list[str]:
    return [f.name for f in model.files if f.folder == folder]


def _pick(model: ModelDef, folders: tuple[str, ...]) -> list[str]:
    out: list[str] = []
    for folder in folders:
        out.extend(_main_files(model, folder))
    return out


# -- per-family builders -----------------------------------------------------


def _build_wan22_14b(g, model, p, *, image, prompt, negative, seed, width, height, nodes, prefix):
    """Wan 2.2 I2V A14B: a mixture-of-experts pair sampled in two stages."""
    weights = _pick(model, ("diffusion_models", "unet"))
    high = next((w for w in weights if "high" in w.lower()), weights[0])
    low = next((w for w in weights if "low" in w.lower()), weights[-1])

    high_node = _diffusion_loader(g, model, high, p.weight_dtype, "High noise expert")
    low_node = _diffusion_loader(g, model, low, p.weight_dtype, "Low noise expert")

    if p.lightning and model.lightning:
        names = [f.name for f in model.lightning]
        lit_high = next((n for n in names if "high" in n), names[0])
        lit_low = next((n for n in names if "low" in n), names[-1])
        high_node = _lora_chain(g, high_node, [Lora(lit_high, 1.0)])
        low_node = _lora_chain(g, low_node, [Lora(lit_low, 1.0)])

    high_node = _lora_chain(g, high_node, [*p.loras, *p.loras_high])
    low_node = _lora_chain(g, low_node, [*p.loras, *p.loras_low])

    high_node = g.add("ModelSamplingSD3", {"model": [high_node, 0], "shift": p.shift}, "Shift (high)")
    low_node = g.add("ModelSamplingSD3", {"model": [low_node, 0], "shift": p.shift}, "Shift (low)")

    clip = g.add("CLIPLoader", {"clip_name": _main_files(model, "text_encoders")[0], "type": "wan"}, "UMT5")
    vae = g.add("VAELoader", {"vae_name": _main_files(model, "vae")[0]}, "Wan VAE")
    pos = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": prompt}, "Prompt")
    neg = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": negative}, "Negative")
    img = g.add("LoadImage", {"image": image}, "Input image")

    i2v = g.add(
        "WanImageToVideo",
        {
            "positive": [pos, 0],
            "negative": [neg, 0],
            "vae": [vae, 0],
            "start_image": [img, 0],
            "width": width,
            "height": height,
            "length": p.length,
            "batch_size": 1,
        },
        "Wan I2V latent",
    )

    boundary = p.boundary if p.boundary is not None else max(1, p.steps // 2)
    common = {
        "steps": p.steps,
        "cfg": p.cfg,
        "sampler_name": p.sampler,
        "scheduler": p.scheduler,
        "noise_seed": seed,
        "positive": [i2v, 0],
        "negative": [i2v, 1],
    }
    stage1 = g.add(
        "KSamplerAdvanced",
        {
            **common,
            "add_noise": "enable",
            "model": [high_node, 0],
            "latent_image": [i2v, 2],
            "start_at_step": 0,
            "end_at_step": boundary,
            "return_with_leftover_noise": "enable",
        },
        "Sample (high noise)",
    )
    stage2 = g.add(
        "KSamplerAdvanced",
        {
            **common,
            "add_noise": "disable",
            "model": [low_node, 0],
            "latent_image": [stage1, 0],
            "start_at_step": boundary,
            "end_at_step": 10000,
            "return_with_leftover_noise": "disable",
        },
        "Sample (low noise)",
    )
    decoded = g.add("VAEDecode", {"samples": [stage2, 0], "vae": [vae, 0]}, "Decode")
    frames, out_fps = _post_process(g, decoded, p, nodes)
    _video_output(g, frames, out_fps, prefix, nodes)


def _build_wan22_5b(g, model, p, *, image, prompt, negative, seed, width, height, nodes, prefix):
    """Wan 2.2 TI2V 5B: one dense model, one sampling pass, 16x-compressing VAE."""
    unet = _diffusion_loader(g, model, _pick(model, ("diffusion_models", "unet"))[0], p.weight_dtype, "Wan 5B")
    unet = _lora_chain(g, unet, p.loras)
    unet = g.add("ModelSamplingSD3", {"model": [unet, 0], "shift": p.shift}, "Shift")

    clip = g.add("CLIPLoader", {"clip_name": _main_files(model, "text_encoders")[0], "type": "wan"}, "UMT5")
    vae = g.add("VAELoader", {"vae_name": _main_files(model, "vae")[0]}, "Wan 2.2 VAE")
    pos = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": prompt}, "Prompt")
    neg = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": negative}, "Negative")
    img = g.add("LoadImage", {"image": image}, "Input image")

    # Unlike WanImageToVideo this returns only a latent; conditioning is untouched.
    latent = g.add(
        "Wan22ImageToVideoLatent",
        {
            "vae": [vae, 0],
            "width": width,
            "height": height,
            "length": p.length,
            "batch_size": 1,
            "start_image": [img, 0],
        },
        "Wan 2.2 I2V latent",
    )
    sampled = g.add(
        "KSampler",
        {
            "model": [unet, 0],
            "seed": seed,
            "steps": p.steps,
            "cfg": p.cfg,
            "sampler_name": p.sampler,
            "scheduler": p.scheduler,
            "positive": [pos, 0],
            "negative": [neg, 0],
            "latent_image": [latent, 0],
            "denoise": 1.0,
        },
        "Sample",
    )
    decoded = g.add("VAEDecode", {"samples": [sampled, 0], "vae": [vae, 0]}, "Decode")
    frames, out_fps = _post_process(g, decoded, p, nodes)
    _video_output(g, frames, out_fps, prefix, nodes)


def _build_hunyuan15(g, model, p, *, image, prompt, negative, seed, width, height, nodes, prefix):
    """HunyuanVideo 1.5 I2V: dual text encoder plus a SigLIP vision embedding."""
    unet = _diffusion_loader(g, model, _pick(model, ("diffusion_models", "unet"))[0], p.weight_dtype, "HunyuanVideo 1.5")
    unet = _lora_chain(g, unet, p.loras)
    unet = g.add("ModelSamplingSD3", {"model": [unet, 0], "shift": p.shift}, "Shift")

    encoders = _main_files(model, "text_encoders")
    qwen = next((n for n in encoders if "qwen" in n), encoders[0])
    byt5 = next((n for n in encoders if "byt5" in n), encoders[-1])
    clip = g.add(
        "DualCLIPLoader",
        {"clip_name1": qwen, "clip_name2": byt5, "type": "hunyuan_video_15"},
        "Qwen2.5-VL + ByT5",
    )
    vae = g.add("VAELoader", {"vae_name": _main_files(model, "vae")[0]}, "HunyuanVideo VAE")
    pos = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": prompt}, "Prompt")
    neg = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": negative}, "Negative")
    img = g.add("LoadImage", {"image": image}, "Input image")

    vision = g.add("CLIPVisionLoader", {"clip_name": _main_files(model, "clip_vision")[0]}, "SigLIP")
    vision_out = g.add(
        "CLIPVisionEncode",
        {"clip_vision": [vision, 0], "image": [img, 0], "crop": "center"},
        "Encode image",
    )

    i2v = g.add(
        "HunyuanVideo15ImageToVideo",
        {
            "positive": [pos, 0],
            "negative": [neg, 0],
            "vae": [vae, 0],
            "width": width,
            "height": height,
            "length": p.length,
            "batch_size": 1,
            "start_image": [img, 0],
            "clip_vision_output": [vision_out, 0],
        },
        "HunyuanVideo I2V latent",
    )
    sampled = g.add(
        "KSampler",
        {
            "model": [unet, 0],
            "seed": seed,
            "steps": p.steps,
            "cfg": p.cfg,
            "sampler_name": p.sampler,
            "scheduler": p.scheduler,
            "positive": [i2v, 0],
            "negative": [i2v, 1],
            "latent_image": [i2v, 2],
            "denoise": 1.0,
        },
        "Sample",
    )
    decoded = g.add("VAEDecode", {"samples": [sampled, 0], "vae": [vae, 0]}, "Decode")
    frames, out_fps = _post_process(g, decoded, p, nodes)
    _video_output(g, frames, out_fps, prefix, nodes)


BUILDERS = {
    "wan22_14b": _build_wan22_14b,
    "wan22_5b": _build_wan22_5b,
    "hunyuan15": _build_hunyuan15,
}


class UnsupportedModel(RuntimeError):
    pass


def build(
    model: ModelDef,
    params: GenParams,
    *,
    image_name: str,
    prompt: str,
    negative: str | None = None,
    seed: int,
    width: int,
    height: int,
    available_nodes: set[str] | None = None,
    filename_prefix: str = "wan/anim",
) -> dict:
    builder = BUILDERS.get(model.family)
    if builder is None:
        raise UnsupportedModel(
            f"{model.label} 不能由這個 app 直接生成"
            + ("（只提供檔案下載，請用 ComfyUI 內建範例）" if model.family == "files_only" else "")
        )

    g = GraphBuilder()
    builder(
        g,
        model,
        params,
        image=image_name,
        prompt=prompt,
        negative=model.negative if negative is None else negative,
        seed=seed,
        width=width,
        height=height,
        nodes=available_nodes or set(),
        prefix=filename_prefix,
    )
    return g.nodes

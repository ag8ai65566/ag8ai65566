"""Builds a ComfyUI API-format graph for Wan 2.2 I2V (14B MoE, high/low noise pair).

The graph is assembled programmatically instead of loading an exported .json so
that resolution, length, LoRAs and step split can be driven by config. Node
class names and their inputs are validated against the live ComfyUI
/object_info before submission (see comfy_client.validate).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

# The negative prompt shipped with the official Wan repo. Kept verbatim - it is
# tuned for this model family and works far better than an English equivalent.
DEFAULT_NEGATIVE = (
    "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，"
    "整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，"
    "画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，"
    "静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走"
)

# Pixel budgets per quality tier. Wan 2.2 14B was trained at 480p and 720p;
# anything in between works but drifts. Values are the canonical training sizes.
TIERS = {
    "480p": 832 * 480,
    "720p": 1280 * 720,
}


@dataclass
class Lora:
    name: str
    strength: float = 1.0


@dataclass
class Settings:
    """Everything the graph needs. Populated from env in config.py."""

    # model files
    high_noise: str = "wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors"
    low_noise: str = "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors"
    loader: str = "safetensors"  # "safetensors" | "gguf"
    weight_dtype: str = "default"  # only for safetensors loader
    text_encoder: str = "umt5_xxl_fp8_e4m3fn_scaled.safetensors"
    vae: str = "wan_2.1_vae.safetensors"

    # sampling
    steps: int = 20
    boundary: int = 10  # step at which we hand off high-noise -> low-noise
    cfg: float = 3.5
    shift: float = 8.0
    sampler: str = "euler"
    scheduler: str = "simple"

    # speed LoRAs (4-step lightx2v). Applied to both experts.
    lightning: bool = False
    lightning_high: str = "wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors"
    lightning_low: str = "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"
    lightning_strength: float = 1.0

    # extra LoRAs (style / subject / NSFW), applied to both experts
    loras: list[Lora] = field(default_factory=list)
    loras_high: list[Lora] = field(default_factory=list)  # high-noise only
    loras_low: list[Lora] = field(default_factory=list)  # low-noise only

    # output
    tier: str = "480p"
    length: int = 81  # frames; Wan wants 4n+1
    fps: int = 16

    def resolved(self) -> "Settings":
        """Apply the lightning preset, which overrides the sampler numbers."""
        if not self.lightning:
            return self
        s = Settings(**{**self.__dict__})
        s.steps, s.boundary, s.cfg, s.shift = 4, 2, 1.0, 5.0
        return s


def fit_dimensions(width: int, height: int, tier: str) -> tuple[int, int]:
    """Scale the source image to the tier's pixel budget, keeping aspect ratio.

    Both dimensions are snapped to a multiple of 16 because the Wan VAE
    downsamples by 8 and the DiT patchifies by 2.
    """
    budget = TIERS.get(tier) or TIERS["480p"]
    scale = math.sqrt(budget / (width * height))
    w = max(16, int(round(width * scale / 16)) * 16)
    h = max(16, int(round(height * scale / 16)) * 16)
    return w, h


def normalize_length(frames: int) -> int:
    """Wan's temporal VAE compresses 4:1, so frame count must be 4n+1."""
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

    def build(self) -> dict:
        return self.nodes


def build(
    *,
    image_name: str,
    prompt: str,
    negative: str,
    seed: int,
    width: int,
    height: int,
    settings: Settings,
    available_nodes: set[str] | None = None,
    filename_prefix: str = "wan/anim",
) -> dict:
    """Return a ComfyUI API-format prompt graph.

    available_nodes, when given, is used to pick between the modern
    CreateVideo/SaveVideo pair and VideoHelperSuite's VHS_VideoCombine.
    """
    s = settings.resolved()
    g = GraphBuilder()
    nodes = available_nodes or set()

    # ---- loaders -----------------------------------------------------------
    def diffusion_loader(fname: str, title: str) -> str:
        if s.loader == "gguf":
            return g.add("UnetLoaderGGUF", {"unet_name": fname}, title)
        return g.add(
            "UNETLoader",
            {"unet_name": fname, "weight_dtype": s.weight_dtype},
            title,
        )

    high = diffusion_loader(s.high_noise, "High noise expert")
    low = diffusion_loader(s.low_noise, "Low noise expert")

    clip = g.add(
        "CLIPLoader",
        {"clip_name": s.text_encoder, "type": "wan"},
        "UMT5 text encoder",
    )
    vae = g.add("VAELoader", {"vae_name": s.vae}, "Wan VAE")

    # ---- LoRA chains -------------------------------------------------------
    def apply_loras(model: str, extra: list[Lora], lightning_lora: str) -> str:
        chain = model
        if s.lightning and lightning_lora:
            chain = g.add(
                "LoraLoaderModelOnly",
                {
                    "model": [chain, 0],
                    "lora_name": lightning_lora,
                    "strength_model": s.lightning_strength,
                },
                "Lightning 4-step",
            )
        for lora in [*s.loras, *extra]:
            chain = g.add(
                "LoraLoaderModelOnly",
                {
                    "model": [chain, 0],
                    "lora_name": lora.name,
                    "strength_model": lora.strength,
                },
                f"LoRA {lora.name}",
            )
        return chain

    high = apply_loras(high, s.loras_high, s.lightning_high)
    low = apply_loras(low, s.loras_low, s.lightning_low)

    high = g.add("ModelSamplingSD3", {"model": [high, 0], "shift": s.shift}, "Shift (high)")
    low = g.add("ModelSamplingSD3", {"model": [low, 0], "shift": s.shift}, "Shift (low)")

    # ---- conditioning ------------------------------------------------------
    pos = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": prompt}, "Prompt")
    neg = g.add("CLIPTextEncode", {"clip": [clip, 0], "text": negative}, "Negative")
    image = g.add("LoadImage", {"image": image_name}, "Input image")

    i2v = g.add(
        "WanImageToVideo",
        {
            "positive": [pos, 0],
            "negative": [neg, 0],
            "vae": [vae, 0],
            "start_image": [image, 0],
            "width": width,
            "height": height,
            "length": s.length,
            "batch_size": 1,
        },
        "Wan I2V latent",
    )

    # ---- two-stage sampling ------------------------------------------------
    common = {
        "steps": s.steps,
        "cfg": s.cfg,
        "sampler_name": s.sampler,
        "scheduler": s.scheduler,
        "noise_seed": seed,
        "positive": [i2v, 0],
        "negative": [i2v, 1],
    }
    stage1 = g.add(
        "KSamplerAdvanced",
        {
            **common,
            "add_noise": "enable",
            "model": [high, 0],
            "latent_image": [i2v, 2],
            "start_at_step": 0,
            "end_at_step": s.boundary,
            "return_with_leftover_noise": "enable",
        },
        "Sample (high noise)",
    )
    stage2 = g.add(
        "KSamplerAdvanced",
        {
            **common,
            "add_noise": "disable",
            "model": [low, 0],
            "latent_image": [stage1, 0],
            "start_at_step": s.boundary,
            "end_at_step": 10000,
            "return_with_leftover_noise": "disable",
        },
        "Sample (low noise)",
    )

    decoded = g.add("VAEDecode", {"samples": [stage2, 0], "vae": [vae, 0]}, "Decode")

    # ---- video output ------------------------------------------------------
    # Prefer ComfyUI's native video nodes; fall back to VideoHelperSuite.
    if "CreateVideo" in nodes and "SaveVideo" in nodes:
        video = g.add(
            "CreateVideo", {"images": [decoded, 0], "fps": s.fps}, "Assemble video"
        )
        g.add(
            "SaveVideo",
            {
                "video": [video, 0],
                "filename_prefix": filename_prefix,
                "format": "mp4",
                "codec": "h264",
            },
            "Save mp4",
        )
    elif "VHS_VideoCombine" in nodes:
        g.add(
            "VHS_VideoCombine",
            {
                "images": [decoded, 0],
                "frame_rate": s.fps,
                "loop_count": 0,
                "filename_prefix": filename_prefix,
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
        # Last resort: an animated webp, which core ComfyUI always supports.
        g.add(
            "SaveAnimatedWEBP",
            {
                "images": [decoded, 0],
                "filename_prefix": filename_prefix,
                "fps": s.fps,
                "lossless": False,
                "quality": 90,
                "method": "default",
            },
            "Save webp",
        )

    return g.build()

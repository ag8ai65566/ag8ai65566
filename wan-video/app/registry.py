"""Catalogue of installable models.

Every filename, repo path and byte size here was read from the Hugging Face
API, and every node name and parameter value in the builders was validated
against a real ComfyUI 0.32.0 /object_info. Sampler numbers come from the
official ComfyUI workflow templates for each model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

WAN_REPO = "Comfy-Org/Wan_2.2_ComfyUI_Repackaged"
HY_REPO = "Comfy-Org/HunyuanVideo_1.5_repackaged"
GGUF_REPO = "QuantStack/Wan2.2-I2V-A14B-GGUF"

# The negative prompt shipped with the official Wan workflows. Kept verbatim -
# it is tuned for this model family and beats an English equivalent.
WAN_NEGATIVE = (
    "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，"
    "整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，"
    "画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，"
    "静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走"
)
HY_NEGATIVE = "pc game, console game, video game, cartoon, childish, ugly, static, blurry, watermark, subtitles"


@dataclass(frozen=True)
class ModelFile:
    repo: str
    path: str
    folder: str  # ComfyUI models/<folder>
    size: int

    @property
    def name(self) -> str:
        return self.path.rsplit("/", 1)[-1]


@dataclass
class ModelDef:
    id: str
    label: str
    family: str  # wan22_14b | wan22_5b | hunyuan15 | files_only
    vram_gb: int  # realistic minimum
    files: list[ModelFile]
    tiers: dict[str, tuple[int, int]]
    fps: int = 16
    length: int = 81
    steps: int = 20
    cfg: float = 3.5
    shift: float = 8.0
    sampler: str = "euler"
    scheduler: str = "simple"
    negative: str = WAN_NEGATIVE
    # wan22_14b only: which step the high-noise expert hands off to the low one
    boundary: int | None = None
    # Optional speed LoRAs, downloaded with the model and toggleable per job.
    lightning: tuple[ModelFile, ...] = ()
    lightning_steps: int = 4
    lightning_cfg: float = 1.0
    lightning_shift: float = 5.0
    supports_lora: bool = True
    # Exact CivitAI baseModel strings, best match first. Filters the in-app
    # LoRA browser to things that stand a chance of working with this model.
    civitai_bases: tuple[str, ...] = ()
    # Trained for a neighbouring model; often works, sometimes not.
    civitai_bases_loose: tuple[str, ...] = ()
    note: str = ""

    @property
    def vram_note(self) -> str:
        """VRAM here is a recommendation, never a limit - said in one place."""
        return (
            f"建議 {self.vram_gb}GB 顯存。低於這個數字仍然跑得動 —— "
            "ComfyUI 會把權重換到系統記憶體，只是慢很多。"
        )

    @property
    def all_files(self) -> list[ModelFile]:
        return [*self.files, *self.lightning]

    @property
    def download_bytes(self) -> int:
        return sum(f.size for f in self.all_files)

    @property
    def runnable(self) -> bool:
        return self.family != "files_only"


# -- shared component sets ---------------------------------------------------

WAN_TE = ModelFile(WAN_REPO, "split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors", "text_encoders", 6735906897)
WAN21_VAE = ModelFile(WAN_REPO, "split_files/vae/wan_2.1_vae.safetensors", "vae", 253815318)
WAN22_VAE = ModelFile(WAN_REPO, "split_files/vae/wan2.2_vae.safetensors", "vae", 1409400960)
WAN_LIGHTNING = (
    ModelFile(WAN_REPO, "split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors", "loras", 1226977424),
    ModelFile(WAN_REPO, "split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors", "loras", 1226977424),
)

HY_COMMON = [
    ModelFile(HY_REPO, "split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors", "text_encoders", 9384670680),
    ModelFile(HY_REPO, "split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors", "text_encoders", 438643184),
    ModelFile(HY_REPO, "split_files/vae/hunyuanvideo15_vae_fp16.safetensors", "vae", 2521292758),
    ModelFile(HY_REPO, "split_files/clip_vision/sigclip_vision_patch14_384.safetensors", "clip_vision", 856505640),
]

# CivitAI baseModel strings, verified against live search results.
WAN22_I2V_BASES = ("Wan Video 2.2 I2V-A14B",)
WAN22_I2V_LOOSE = (
    "Wan Video 2.2 T2V-A14B",
    "Wan Video 14B i2v 480p",
    "Wan Video 14B i2v 720p",
    "Wan Video 14B t2v",
    "Wan Video",
)

WAN_TIERS = {"480p": (832, 480), "720p": (1280, 720)}
HY_TIERS = {"480p": (848, 480), "720p": (1280, 720)}


def _gguf(quant: str, size: int) -> list[ModelFile]:
    return [
        ModelFile(GGUF_REPO, f"HighNoise/Wan2.2-I2V-A14B-HighNoise-{quant}.gguf", "unet", size),
        ModelFile(GGUF_REPO, f"LowNoise/Wan2.2-I2V-A14B-LowNoise-{quant}.gguf", "unet", size),
    ]


MODELS: list[ModelDef] = [
    ModelDef(
        id="wan22-14b-fp8",
        label="Wan 2.2 I2V 14B — fp8（畫質最好）",
        family="wan22_14b",
        vram_gb=24,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors", "diffusion_models", 14294742832),
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors", "diffusion_models", 14294742832),
            WAN_TE,
            WAN21_VAE,
        ],
        tiers=WAN_TIERS,
        fps=16,
        length=81,
        steps=20,
        cfg=3.5,
        shift=8.0,
        boundary=10,
        lightning=WAN_LIGHTNING,
        civitai_bases=WAN22_I2V_BASES,
        civitai_bases_loose=WAN22_I2V_LOOSE,
        note="NSFW LoRA 生態最完整的選擇。",
    ),
    ModelDef(
        id="wan22-14b-q8",
        label="Wan 2.2 I2V 14B — GGUF Q8（接近 fp8）",
        family="wan22_14b",
        vram_gb=16,
        files=[*_gguf("Q8_0", 15406608896), WAN_TE, WAN21_VAE],
        tiers=WAN_TIERS,
        fps=16,
        length=81,
        steps=20,
        cfg=3.5,
        shift=8.0,
        boundary=10,
        lightning=WAN_LIGHTNING,
        civitai_bases=WAN22_I2V_BASES,
        civitai_bases_loose=WAN22_I2V_LOOSE,
        note="需要 ComfyUI-GGUF 節點（安裝腳本已含）。",
    ),
    ModelDef(
        id="wan22-14b-q4",
        label="Wan 2.2 I2V 14B — GGUF Q4_K_M（省顯存）",
        family="wan22_14b",
        vram_gb=12,
        files=[*_gguf("Q4_K_M", 9651728896), WAN_TE, WAN21_VAE],
        tiers=WAN_TIERS,
        fps=16,
        length=81,
        steps=20,
        cfg=3.5,
        shift=8.0,
        boundary=10,
        lightning=WAN_LIGHTNING,
        civitai_bases=WAN22_I2V_BASES,
        civitai_bases_loose=WAN22_I2V_LOOSE,
        note="12GB 顯卡的主力選擇。畫質略降但動態仍好。",
    ),
    ModelDef(
        id="wan22-5b",
        label="Wan 2.2 TI2V 5B（輕量、原生 720p）",
        family="wan22_5b",
        vram_gb=12,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors", "diffusion_models", 9999658848),
            WAN_TE,
            WAN22_VAE,
        ],
        tiers={"480p": (832, 480), "704p": (1280, 704)},
        fps=24,
        length=121,
        steps=20,
        cfg=5.0,
        shift=8.0,
        sampler="uni_pc",
        civitai_bases=("Wan Video 2.2 TI2V-5B",),
        civitai_bases_loose=("Wan Video",),
        note="單一模型、下載量小。畫質明顯輸 14B，但快很多。",
    ),
    ModelDef(
        id="hy15-480p",
        label="HunyuanVideo 1.5 480p — fp8 cfg-distilled（最省顯存）",
        family="hunyuan15",
        vram_gb=10,
        files=[
            ModelFile(HY_REPO, "split_files/diffusion_models/hunyuanvideo1.5_480p_i2v_cfg_distilled_fp8_scaled.safetensors", "diffusion_models", 8330399746),
            *HY_COMMON,
        ],
        tiers={"480p": (848, 480)},
        fps=24,
        length=121,
        steps=20,
        cfg=1.0,  # CFG is distilled into the weights; a real cfg would double the cost
        shift=7.0,
        negative=HY_NEGATIVE,
        # CivitAI's "Hunyuan Video" is the original architecture, not 1.5,
        # so those LoRAs are a gamble rather than a match.
        civitai_bases_loose=("Hunyuan Video",),
        note="主模型只有 8.3GB。人臉與物理最自然，NSFW 生態比 Wan 少。",
    ),
    ModelDef(
        id="hy15-720p",
        label="HunyuanVideo 1.5 720p — fp8 cfg-distilled",
        family="hunyuan15",
        vram_gb=12,
        files=[
            ModelFile(HY_REPO, "split_files/diffusion_models/hunyuanvideo1.5_720p_i2v_cfg_distilled_fp8_scaled.safetensors", "diffusion_models", 8330399746),
            *HY_COMMON,
        ],
        tiers=HY_TIERS,
        fps=24,
        length=121,
        steps=20,
        cfg=1.0,
        shift=7.0,
        negative=HY_NEGATIVE,
        civitai_bases_loose=("Hunyuan Video",),
    ),
    ModelDef(
        id="hy15-720p-hq",
        label="HunyuanVideo 1.5 720p — fp16（品質優先）",
        family="hunyuan15",
        vram_gb=20,
        files=[
            ModelFile(HY_REPO, "split_files/diffusion_models/hunyuanvideo1.5_720p_i2v_fp16.safetensors", "diffusion_models", 16653368128),
            *HY_COMMON,
        ],
        tiers=HY_TIERS,
        fps=24,
        length=121,
        steps=20,
        cfg=6.0,  # official template value for the non-distilled build
        shift=7.0,
        negative=HY_NEGATIVE,
        civitai_bases_loose=("Hunyuan Video",),
        note="官方範例的設定（cfg 6 / shift 7 / 20 步）。",
    ),
    # Files only: LTX-2.3's official pipeline is a ~50 node graph with two-pass
    # sampling, latent upscaling and a joint audio/video latent. Reproducing it
    # in code would be guesswork this stack cannot verify, so the manager
    # downloads the weights and you drive them from ComfyUI's own built-in
    # template (or export that template and drop it in workflows/).
    ModelDef(
        id="ltx23",
        label="LTX-2.3 22B — 只下載檔案（用 ComfyUI 內建範例跑）",
        family="files_only",
        vram_gb=24,
        files=[
            ModelFile("Lightricks/LTX-2.3-fp8", "ltx-2.3-22b-dev-fp8.safetensors", "checkpoints", 29145431166),
            ModelFile("Comfy-Org/ltx-2", "split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors", "text_encoders", 9447702218),
            ModelFile("Comfy-Org/ltx-2.3", "split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors", "loras", 2741024390),
            ModelFile("Comfy-Org/ltx-2", "split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "loras", 628203616),
            ModelFile("Lightricks/LTX-2.3", "ltx-2.3-spatial-upscaler-x2-1.1.safetensors", "latent_upscale_models", 1002438656),
        ],
        tiers={},
        supports_lora=False,
        civitai_bases=("LTXV 2.3",),
        note="影音同步一次生成。下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → LTX-2.3 I2V。",
    ),
]

BY_ID = {m.id: m for m in MODELS}


def get(model_id: str) -> ModelDef | None:
    return BY_ID.get(model_id)


def runnable() -> list[ModelDef]:
    return [m for m in MODELS if m.runnable]


@dataclass
class Lora:
    name: str
    strength: float = 1.0


@dataclass
class GenParams:
    """Per-job sampling parameters, seeded from the model then overridden."""

    steps: int
    cfg: float
    shift: float
    sampler: str
    scheduler: str
    length: int
    fps: int
    boundary: int | None = None
    lightning: bool = False
    weight_dtype: str = "default"
    loras: list[Lora] = field(default_factory=list)
    loras_high: list[Lora] = field(default_factory=list)
    loras_low: list[Lora] = field(default_factory=list)

    @classmethod
    def defaults_for(cls, model: ModelDef, lightning: bool = False) -> "GenParams":
        use_lightning = lightning and bool(model.lightning)
        return cls(
            steps=model.lightning_steps if use_lightning else model.steps,
            cfg=model.lightning_cfg if use_lightning else model.cfg,
            shift=model.lightning_shift if use_lightning else model.shift,
            sampler=model.sampler,
            scheduler=model.scheduler,
            length=model.length,
            fps=model.fps,
            boundary=(model.lightning_steps // 2) if use_lightning else model.boundary,
            lightning=use_lightning,
        )

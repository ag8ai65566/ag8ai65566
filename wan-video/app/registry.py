"""Catalogue of installable models.

Every filename, repo path and byte size here was read from the Hugging Face
API, and every node name and parameter value in the builders was validated
against a real ComfyUI 0.33.0 /object_info. Sampler numbers come from the
official ComfyUI workflow templates for each model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

WAN_REPO = "Comfy-Org/Wan_2.2_ComfyUI_Repackaged"
HY_REPO = "Comfy-Org/HunyuanVideo_1.5_repackaged"
GGUF_REPO = "QuantStack/Wan2.2-I2V-A14B-GGUF"
LTX25_REPO = "Lightricks/LTX-2.5"

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
    # Some repos publish everything as `diffusion_pytorch_model.safetensors`,
    # so the basename would collide between models and tell the user nothing in
    # the loader's dropdown. This is the name it lands under instead.
    save_as: str = ""
    # Hugging Face "gated" repos answer 401 to an anonymous request even though
    # the weights are free: you have to be logged in *and* have clicked accept
    # on the model page. Flagged here so the UI can say that before a 40GB
    # download fails at the first byte, rather than after.
    gated: bool = False

    @property
    def name(self) -> str:
        return self.save_as or self.path.rsplit("/", 1)[-1]


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
    def gated_repos(self) -> list[str]:
        """Repos that need a Hugging Face token plus an accepted licence."""
        return sorted({f.repo for f in self.all_files if f.gated})

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
        # The one thing a short drama cannot be made without: a character who
        # talks. S2V is audio-driven - the audio goes in and the lip movement
        # comes out of the same pass, rather than being pasted on afterwards by
        # a separate lip-sync model. That ordering matters in practice: the
        # audio has to exist first, and its length decides the shot's length.
        id="wan22-s2v",
        label="Wan 2.2 S2V 14B — 說話鏡頭（音訊驅動，原生口型）",
        family="files_only",
        vram_gb=16,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors",
                      "diffusion_models", 16394832474),
            # S2V listens through wav2vec, so the audio encoder is not optional.
            ModelFile(WAN_REPO, "split_files/audio_encoders/wav2vec2_large_english_fp16.safetensors",
                      "audio_encoders", 630997322),
            WAN_TE,
            WAN21_VAE,
        ],
        tiers={},
        fps=16,
        supports_lora=False,
        civitai_bases=("Wan Video 2.2 I2V-A14B",),
        note="**短劇有台詞的鏡頭就是靠這個。** 音檔進去、對好口型的影片出來，"
             "不是事後再貼一層 lip-sync。所以順序是**先做音檔再生影片** —— "
             "音檔長度直接決定鏡頭長度，反過來做就要重跑。"
             "下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → Wan 2.2 S2V。",
    ),
    ModelDef(
        # Motion retargeting: take the pose and expression out of a driving
        # video and put them on your character. For short drama this is an asset
        # play, not a one-off - the genre runs on the same handful of beats
        # (a slap, a turn, a door slammed, an embrace), so one good driving clip
        # gets reused across characters and episodes.
        id="wan22-animate",
        label="Wan 2.2 Animate 14B — 動作轉移（把參考影片的動作套到你的角色）",
        family="files_only",
        vram_gb=16,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_animate_14B_int8_convrot.safetensors",
                      "diffusion_models", 18413068672),
            # Relight LoRA: without it the character keeps the lighting of the
            # plate they came from and looks pasted into the scene.
            ModelFile(WAN_REPO, "split_files/loras/wan2.2_animate_14B_relight_lora_bf16.safetensors",
                      "loras", 1436673432),
            WAN_TE,
            WAN21_VAE,
        ],
        tiers={},
        fps=16,
        supports_lora=False,
        civitai_bases=("Wan Video 2.2 I2V-A14B",),
        note="**動作也可以當資產。** 短劇的動作是高度重複的（甩巴掌、轉身、摔門、"
             "擁抱），錄一次或找一段參考影片，就能套到不同角色身上重複用。"
             "附的 relight LoRA 會把角色的光線重打成場景的光線，不加會像貼上去的。"
             "下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → Wan 2.2 Animate。",
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
    ModelDef(
        # The current LTX generation, and the newest open-weight video model in
        # this catalogue. Worth stating why it is here at all: the models people
        # ask for by name - Seedance, Wan 2.5 - are closed APIs with no weights
        # to download, so "the latest" and "runs on your machine" have stopped
        # being the same list. This is the newest thing that is actually both.
        id="ltx25",
        label="LTX-2.5 22B — 只下載檔案（用 ComfyUI 內建範例跑）",
        family="files_only",
        vram_gb=24,
        files=[
            # The int8 "convrot" builds are the ones ComfyUI's own LTX-2.5 page
            # lists. The bf16 transformer is 42GB and the distilled one is what
            # the documented workflow loads, so the extra 20GB buys nothing here.
            ModelFile(LTX25_REPO,
                      "diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors",
                      "diffusion_models", 21504034224, gated=True),
            # Not interchangeable with LTX-2.3's Gemma 3: the projection is baked
            # in and the loader checks the encoder version against the one the
            # checkpoint was trained with, so this exact file or nothing.
            ModelFile(LTX25_REPO,
                      "text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors",
                      "text_encoders", 15372969374, gated=True),
            ModelFile(LTX25_REPO, "vae/ltx-2.5-video-vae-bf16.safetensors",
                      "vae", 1472223346, gated=True),
            # Audio is generated in the same pass as the picture, so its VAE is
            # not optional the way an upscaler is.
            ModelFile(LTX25_REPO, "vae/ltx-2.5-audio-vae-bf16.safetensors",
                      "vae", 364866540, gated=True),
            ModelFile(LTX25_REPO,
                      "latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors",
                      "latent_upscale_models", 995778752, gated=True),
        ],
        tiers={},
        supports_lora=False,
        civitai_bases=("LTXV 2.5",),
        civitai_bases_loose=("LTXV 2.3",),
        note="影音同步一次生成，官方說支援到 4K HDR / 50fps。"
             "**這個倉庫是 gated**：要先到 huggingface.co/Lightricks/LTX-2.5 按同意授權，"
             "再到「設定」分頁貼上 Hugging Face token，否則下載會直接 401。"
             "下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → LTX-2.5。",
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
    # Post-processing on the decoded frames. Neither changes what the model
    # generates; both are applied after it, so they cost no VRAM during sampling.
    interpolate: int = 1  # frame multiplier; 1 = off
    interpolate_model: str = ""
    upscaler: str = ""  # a file in models/upscale_models, "" = leave as rendered

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

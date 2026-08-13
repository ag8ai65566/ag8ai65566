"""Text-to-image: the model catalogue, the ComfyUI graph, and the knob help.

All four checkpoints are SDXL-architecture, so they share one graph. What
differs between them is the stuff a newcomer cannot guess and that ComfyUI
never tells you: Pony wants `score_9, score_8_up…` at the front of every
prompt or it produces mush, Illustrious wants danbooru-style tags and CLIP skip
-2, and photoreal SDXL merges want neither. Those are encoded per model here
and surfaced in the UI rather than left as folklore.

Node names and parameter ranges were read from a real ComfyUI 0.32.x
/object_info; file sizes come from the Hugging Face API.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from registry import ModelFile

SDXL_VAE = ModelFile(
    "madebyollin/sdxl-vae-fp16-fix", "sdxl.vae.safetensors", "vae", 334641162
)


@dataclass
class ImageModel:
    id: str
    label: str
    file: ModelFile
    vram_gb: int = 8
    # Sampling defaults that actually suit this checkpoint.
    steps: int = 28
    cfg: float = 6.0
    sampler: str = "dpmpp_2m"
    scheduler: str = "karras"
    clip_skip: int = -1  # SDXL default; anime merges usually want -2
    # Prompt scaffolding this checkpoint expects.
    positive_prefix: str = ""
    negative: str = ""
    prompt_style: str = ""  # one line telling the user how to write for it
    sizes: dict[str, tuple[int, int]] = field(default_factory=dict)
    default_size: str = "1024×1024 方形"
    nsfw_note: str = ""
    note: str = ""
    extra_files: tuple[ModelFile, ...] = ()

    @property
    def all_files(self) -> list[ModelFile]:
        return [self.file, *self.extra_files]

    @property
    def download_bytes(self) -> int:
        return sum(f.size for f in self.all_files)


# SDXL is trained at ~1 megapixel; these are the ratios that stay coherent.
SDXL_SIZES = {
    "1024×1024 方形": (1024, 1024),
    "832×1216 直式": (832, 1216),
    "1216×832 橫式": (1216, 832),
    "896×1152 直式(緩)": (896, 1152),
    "1152×896 橫式(緩)": (1152, 896),
    "768×1344 長直式": (768, 1344),
    "1344×768 寬橫式": (1344, 768),
}

ANIME_NEG = (
    "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, "
    "fewer digits, cropped, worst quality, low quality, normal quality, "
    "jpeg artifacts, signature, watermark, username, blurry"
)
PHOTO_NEG = (
    "worst quality, low quality, lowres, blurry, jpeg artifacts, watermark, "
    "signature, text, deformed, bad anatomy, bad hands, extra fingers, "
    "mutated hands, cartoon, anime, 3d render"
)

IMAGE_MODELS: list[ImageModel] = [
    ImageModel(
        id="illustrious",
        label="Illustrious XL — 動漫 / 插畫（NSFW 生態最大）",
        file=ModelFile(
            "OnomaAIResearch/Illustrious-xl-early-release-v0",
            "Illustrious-XL-v0.1.safetensors", "checkpoints", 6938040760,
        ),
        vram_gb=8,
        steps=28, cfg=6.0, sampler="euler_ancestral", scheduler="normal",
        clip_skip=-2,
        positive_prefix="masterpiece, best quality, amazing quality, very aesthetic",
        negative="bad quality, worst quality, worst detail, sketch, censor, " + ANIME_NEG,
        prompt_style="用 danbooru 標籤，逗號分隔：`1girl, long hair, school uniform, sitting, from side`。句子式描述效果差。",
        sizes=SDXL_SIZES,
        nsfw_note="Illustrious 系的 LoRA 在 CivitAI 上最多，NSFW 題材涵蓋最廣。",
        note="CivitAI 上下載數最高的 NSFW 底模系列（WAI-illustrious 等都是它的微調）。",
        extra_files=(SDXL_VAE,),
    ),
    ImageModel(
        id="pony",
        label="Pony Diffusion V6 XL — 動漫 / 多元題材",
        file=ModelFile(
            "LyliaEngine/Pony_Diffusion_V6_XL",
            "ponyDiffusionV6XL_v6StartWithThisOne.safetensors", "checkpoints", 6938041050,
        ),
        vram_gb=8,
        steps=25, cfg=7.0, sampler="euler_ancestral", scheduler="normal",
        clip_skip=-2,
        positive_prefix="score_9, score_8_up, score_7_up",
        negative="score_6, score_5, score_4, " + ANIME_NEG,
        prompt_style="**開頭一定要有 `score_9, score_8_up, score_7_up`**（已自動加），否則畫面會爛。之後用 danbooru 標籤。",
        sizes=SDXL_SIZES,
        nsfw_note="NSFW 生態僅次於 Illustrious，寫實向的 Pony 微調也很多。",
        note="那串 score_ 標籤是 Pony 特有的品質控制，不是裝飾。",
        extra_files=(SDXL_VAE,),
    ),
    ImageModel(
        id="juggernaut",
        label="Juggernaut XL v9 — 寫實照片風",
        file=ModelFile(
            "RunDiffusion/Juggernaut-XL-v9",
            "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors", "checkpoints", 7105348188,
        ),
        vram_gb=8,
        steps=30, cfg=5.0, sampler="dpmpp_2m", scheduler="karras",
        clip_skip=-1,
        positive_prefix="",
        negative=PHOTO_NEG,
        prompt_style="用自然句子描述場景與光線：`a woman standing by a window, soft morning light, 85mm portrait, shallow depth of field`。",
        sizes=SDXL_SIZES,
        nsfw_note="底模本身沒有內容過濾，但寫實 NSFW 通常要再加 LoRA。",
        note="CivitAI 上最多下載的寫實 SDXL。",
        extra_files=(SDXL_VAE,),
    ),
    ImageModel(
        id="sdxl-base",
        label="SDXL 1.0 官方底模（乾淨基準）",
        file=ModelFile(
            "stabilityai/stable-diffusion-xl-base-1.0",
            "sd_xl_base_1.0.safetensors", "checkpoints", 6938078334,
        ),
        vram_gb=8,
        steps=30, cfg=7.0, sampler="dpmpp_2m", scheduler="karras",
        clip_skip=-1,
        negative=PHOTO_NEG,
        prompt_style="自然句子。這是未微調的官方底模，風格最中性，也最不擅長 NSFW。",
        sizes=SDXL_SIZES,
        note="拿來當基準或給 LoRA 當底，不是最好看的選擇。",
        extra_files=(SDXL_VAE,),
    ),
]

BY_ID = {m.id: m for m in IMAGE_MODELS}


def get(model_id: str) -> ImageModel | None:
    return BY_ID.get(model_id)


CUSTOM_PREFIX = "custom:"


def custom_model(filename: str) -> ImageModel:
    """Wrap a checkpoint the user installed themselves (e.g. from CivitAI).

    We know nothing about it beyond the filename, so it gets neutral SDXL
    defaults and says so, rather than silently applying Pony's score tags or
    Illustrious's CLIP skip to a checkpoint that wants neither.
    """
    return ImageModel(
        id=CUSTOM_PREFIX + filename,
        label=f"（自己裝的）{filename}",
        file=ModelFile("", filename, "checkpoints", 0),
        steps=28, cfg=6.0, sampler="dpmpp_2m", scheduler="karras", clip_skip=-1,
        negative=ANIME_NEG,
        prompt_style=(
            "這是你自己裝的底模，我不知道它的習慣。"
            "動漫系通常要 danbooru 標籤 + CLIP skip -2；寫實系用自然句子 + CLIP skip -1。"
            "去它的 CivitAI 頁面看作者建議的參數。"
        ),
        sizes=SDXL_SIZES,
        note="用中性的 SDXL 預設值。參數請照該模型作者的建議自己調。",
        extra_files=(),
    )


def resolve(model_id: str, installed: list[str] | None = None) -> ImageModel | None:
    """A catalogue model, or a user-installed checkpoint by filename."""
    if model_id.startswith(CUSTOM_PREFIX):
        name = model_id[len(CUSTOM_PREFIX):]
        if installed is not None and name not in installed:
            return None
        return custom_model(name)
    return BY_ID.get(model_id)


# CivitAI baseModel strings that match SDXL-architecture checkpoints, so the
# LoRA browser can filter to things that will actually load.
CIVITAI_BASES = {
    "illustrious": ("Illustrious", "NoobAI"),
    "pony": ("Pony",),
    "juggernaut": ("SDXL 1.0", "SDXL Lightning"),
    "sdxl-base": ("SDXL 1.0", "SDXL Lightning"),
}
CIVITAI_BASES_LOOSE = ("SDXL 1.0", "Illustrious", "Pony", "NoobAI", "SDXL Lightning")


# What every knob does, in one sentence each, shown next to the control.
HELP = {
    "steps": "畫幾次。20～30 是甜蜜點；再高多半只是變慢，不會更好看。",
    "cfg": "多聽話。低=有創意但可能跑題，高=照著寫但容易僵硬、顏色過飽和。",
    "sampler": "去噪的演算法。`euler_ancestral` 適合動漫、每次變化大；`dpmpp_2m` 穩定、適合寫實。",
    "scheduler": "配合 sampler 的噪聲排程。動漫用 `normal`，寫實用 `karras`。",
    "size": "SDXL 是在約 100 萬像素上訓練的，偏離太多會出現雙頭、肢體重複。用清單裡的比例最穩。",
    "batch": "一次生幾張。同一組設定不同種子，用來一次挑好的。越多越吃顯存。",
    "seed": "隨機起點。固定同一個 seed + 同樣設定 = 同一張圖。`-1` 是每次隨機。",
    "clip_skip": "跳過文字編碼器最後幾層。動漫模型（Pony / Illustrious）習慣 -2，寫實模型用 -1。",
    "denoise": "只在有放大時有意義：重畫多少。0.3～0.5 是加細節，1.0 等於整張重畫。",
    "hires": "先小圖再放大重畫一次，細節更好但時間大約多一倍。手和臉會明顯改善。",
    "lora": "外掛的畫風／角色／題材模型。強度 0.6～1.0，一次加一支比較好抓。",
    "prefix": "這個底模習慣的品質標籤，會自動加在你的提詞最前面。取消勾選就不加。",
}


def build(
    model: ImageModel,
    *,
    prompt: str,
    negative: str,
    seed: int,
    width: int,
    height: int,
    batch: int = 1,
    steps: int | None = None,
    cfg: float | None = None,
    sampler: str | None = None,
    scheduler: str | None = None,
    clip_skip: int | None = None,
    loras: list[tuple[str, float]] | None = None,
    use_vae: bool = True,
    hires_scale: float = 0.0,
    hires_denoise: float = 0.45,
    available_nodes: set[str] | None = None,
    filename_prefix: str = "img/out",
) -> dict:
    """Standard SDXL text-to-image graph, optionally with a hi-res second pass."""
    nodes: dict[str, dict] = {}
    n = 0

    def add(class_type: str, inputs: dict, title: str = "") -> str:
        nonlocal n
        n += 1
        nodes[str(n)] = {
            "class_type": class_type,
            "inputs": inputs,
            "_meta": {"title": title or class_type},
        }
        return str(n)

    ckpt = add("CheckpointLoaderSimple", {"ckpt_name": model.file.name}, "Checkpoint")
    model_link: list = [ckpt, 0]
    clip_link: list = [ckpt, 1]
    vae_link: list = [ckpt, 2]

    # LoRAs affect both the model and the text encoder, so LoraLoader (not the
    # model-only variant used for video) is the right node here.
    for name, strength in loras or []:
        node = add(
            "LoraLoader",
            {
                "model": model_link,
                "clip": clip_link,
                "lora_name": name,
                "strength_model": strength,
                "strength_clip": strength,
            },
            f"LoRA {name}",
        )
        model_link, clip_link = [node, 0], [node, 1]

    skip = model.clip_skip if clip_skip is None else clip_skip
    if skip < -1:
        clip_node = add("CLIPSetLastLayer", {"clip": clip_link, "stop_at_clip_layer": skip}, "CLIP skip")
        clip_link = [clip_node, 0]

    if use_vae and (available_nodes is None or "VAELoader" in available_nodes):
        if any(f.folder == "vae" for f in model.extra_files):
            vae_name = next(f.name for f in model.extra_files if f.folder == "vae")
            vae_node = add("VAELoader", {"vae_name": vae_name}, "VAE (fp16 fix)")
            vae_link = [vae_node, 0]

    pos = add("CLIPTextEncode", {"clip": clip_link, "text": prompt}, "Prompt")
    neg = add("CLIPTextEncode", {"clip": clip_link, "text": negative}, "Negative")
    latent = add(
        "EmptyLatentImage",
        {"width": width, "height": height, "batch_size": max(1, min(batch, 16))},
        "Empty latent",
    )

    sampled = add(
        "KSampler",
        {
            "model": model_link,
            "seed": seed,
            "steps": model.steps if steps is None else steps,
            "cfg": model.cfg if cfg is None else cfg,
            "sampler_name": sampler or model.sampler,
            "scheduler": scheduler or model.scheduler,
            "positive": [pos, 0],
            "negative": [neg, 0],
            "latent_image": [latent, 0],
            "denoise": 1.0,
        },
        "Sample",
    )

    if hires_scale and hires_scale > 1.0:
        up = add(
            "LatentUpscale",
            {
                "samples": [sampled, 0],
                "upscale_method": "nearest-exact",
                "width": int(width * hires_scale) // 8 * 8,
                "height": int(height * hires_scale) // 8 * 8,
                "crop": "disabled",
            },
            "Upscale latent",
        )
        sampled = add(
            "KSampler",
            {
                "model": model_link,
                "seed": seed,
                "steps": model.steps if steps is None else steps,
                "cfg": model.cfg if cfg is None else cfg,
                "sampler_name": sampler or model.sampler,
                "scheduler": scheduler or model.scheduler,
                "positive": [pos, 0],
                "negative": [neg, 0],
                "latent_image": [up, 0],
                "denoise": max(0.05, min(hires_denoise, 1.0)),
            },
            "Hi-res pass",
        )

    decoded = add("VAEDecode", {"samples": [sampled, 0], "vae": vae_link}, "Decode")
    add("SaveImage", {"images": [decoded, 0], "filename_prefix": filename_prefix}, "Save")
    return nodes

"""Text-to-image and image-to-image: the catalogue, the graph, and the knob help.

All four checkpoints are SDXL-architecture, so they share one graph. What
differs between them is the stuff a newcomer cannot guess and that ComfyUI
never tells you: Pony wants `score_9, score_8_up…` at the front of every
prompt or it produces mush, Illustrious wants danbooru-style tags and CLIP skip
-2, and photoreal SDXL merges want neither. Those are encoded per model here
and surfaced in the UI rather than left as folklore.

Node names and parameter ranges were read from a real ComfyUI 0.33.0
/object_info; file sizes come from the Hugging Face API.
"""

from __future__ import annotations

from dataclasses import dataclass, field, fields

import controlnets
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
    # Which vocabulary this checkpoint was actually conditioned on. The anime
    # finetunes are trained on danbooru tag strings, so the exact tag is a sharp
    # lever; the photo models never saw those tags and want a plain description
    # of the same thing. Same idea, two spellings - see quicktags.FAVORITES.
    tag_style: str = "danbooru"
    # How this checkpoint wants an artist named, if at all. NoobAI's model card
    # prompts `artist:john_kafka`; Illustrious uses `by <name>`; Pony V6 removed
    # artist names from its captions altogether, so an artist tag does close to
    # nothing there whatever the spelling - an empty string says exactly that.
    artist_form: str = ""
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

# NoobAI's own model card, verbatim. It ships `nsfw` in the negative and `safe`
# in the prefix; both are removed here because this app has no content filter
# and silently negating what the user asked for is worse than a bad default.
NOOB_NEG = (
    "worst quality, old, early, low quality, lowres, signature, username, logo, "
    "bad hands, mutated hands, mammal, anthro, furry, ambiguous form, feral, semi-anthro"
)

IMAGE_MODELS: list[ImageModel] = [
    ImageModel(
        id="noobai",
        label="NoobAI-XL v1.1 — 動漫首選（認得角色，也認得畫師）",
        file=ModelFile(
            "Laxhar/noobai-XL-1.1", "NoobAI-XL-v1.1.safetensors", "checkpoints", 7105349958,
        ),
        vram_gb=8,
        # CFG 5~6, 25~30 steps, Euler a - straight off the model card.
        steps=28, cfg=5.5, sampler="euler_ancestral", scheduler="normal",
        clip_skip=-2,
        artist_form="artist:{tag}",
        positive_prefix="masterpiece, best quality, newest, absurdres, highres",
        negative=NOOB_NEG,
        prompt_style=(
            "用 danbooru 標籤，而且**照這個順序**："
            "`1girl, 角色名, 作品名, by 畫師, 特殊標籤, 一般標籤`。"
            "這是它訓練時的排法，照著寫差很多。年代標籤 `newest` 代表 2021-2024 的畫風。"
        ),
        sizes=SDXL_SIZES,
        default_size="832×1216 直式",
        nsfw_note=(
            "官方建議的負面詞裡本來有 `nsfw`，這裡拿掉了 —— 要成人內容不用再改設定。"
            "反過來想要全年齡就在提詞加 `safe`。"
        ),
        note=(
            "拿最新的 danbooru + e621 全量訓練，是 Illustrious 的再微調。"
            "**它認得 danbooru 的畫師標籤**（`by yukisame`），也認得幾乎所有 VTuber 角色 —— "
            "這兩件事 Pony 都做不到。授權：Fair AI Public License 1.0-SD，禁止商用。"
        ),
        extra_files=(SDXL_VAE,),
    ),
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
        artist_form="by {tag}",
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
        tag_style="natural",
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
        tag_style="natural",
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
    "noobai": ("NoobAI", "Illustrious"),
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
    "denoise": "重畫多少。只有「以圖生圖」時才有意義：0.3=只改材質，0.5～0.6=保構圖換風格，0.8 以上≈重畫。",
    "hires": "先小圖再放大重畫一次，細節更好但時間大約多一倍。手和臉會明顯改善。",
    "hires_denoise": "放大後那一次要重畫多少。0.4～0.5 最安全；超過 0.6 構圖會跑掉。",
    "hires_steps": "放大那一次跑幾步。留 0 就跟上面一樣；想省時間可以設成一半。",
    "hires_upscaler": "放大的方式。用放大模型比純拉大清楚很多，但要先在「模型」分頁下載一個。",
    "upscaler": "生完之後直接放大成品，不重畫。快、絕對不會改構圖，但也不會多出新細節。",
    "lora": "外掛的畫風／角色／題材模型。強度 0.6～1.0，一次加一支比較好抓。",
    "lora_clip": "LoRA 對「文字理解」的影響力，通常和左邊一樣。畫風 LoRA 把它調低一點，可以避免它蓋掉你的提詞。",
    "prefix": "這個底模習慣的品質標籤，會自動加在你的提詞最前面。取消勾選就不加。",
    "init": "放一張圖進來就變成「以圖生圖」：照著這張的構圖重畫。要改多少看下面的「重畫強度」。",
    "freeu": "免費的畫質補丁，不用下載也不太花時間。通常讓細節更立體，但偶爾會讓顏色變重 —— 覺得怪就關掉。",
    "pag": "另一種畫質補丁，對「構圖崩掉、手畫壞」特別有效，代價是生成時間大約多一倍。建議值 3。",
    "rescale_cfg": "CFG 開很高時用來救回過飽和的顏色。CFG 沒開很高就不用動。0.7 是常見值。",
    "tiled_vae": "把最後解碼的步驟切成小塊做。畫大圖時顯存不夠會在最後一刻爆掉，開這個就能過關，只是慢一點。",
    "wildcards": "提詞裡寫 `{紅|藍|綠}` 就會每張隨機挑一個，一次生 8 張＝8 種變化。",
}


@dataclass
class ImageSettings:
    """Every knob for one image job.

    One dataclass rather than twenty keyword arguments threaded through the API
    handler and the job runner, because those two used to read and write the
    same settings dict independently and could drift apart silently.
    """

    steps: int = 28
    cfg: float = 6.0
    sampler: str = "dpmpp_2m"
    scheduler: str = "karras"
    clip_skip: int = -1
    batch: int = 1
    denoise: float = 1.0
    # (name, strength_model, strength_clip)
    loras: list[tuple[str, float, float]] = field(default_factory=list)
    # Second diffusion pass at a higher resolution.
    hires_scale: float = 0.0
    hires_denoise: float = 0.45
    hires_steps: int = 0  # 0 = same as the main pass
    hires_upscaler: str = ""  # "" = latent upscale; else an upscale_models file
    # Plain enlargement of the finished image, no re-diffusion.
    upscaler: str = ""
    # Keep a reference picture's composition and redraw its contents. The
    # control picture itself is passed per call, not stored here, because a
    # comic page needs a different one for every panel.
    controlnet: str = ""            # a file in models/controlnet
    controlnet_strength: float = 0.75
    controlnet_start: float = 0.0
    controlnet_end: float = 0.75
    controlnet_preprocess: str = "canny"   # canny | none
    controlnet_low: float = 0.4
    controlnet_high: float = 0.8
    controlnet_union_type: str = ""  # "" = ask the catalogue what this model wants
    # Quality patches, all off by default.
    freeu: bool = False
    pag: float = 0.0
    rescale_cfg: float = 0.0
    tiled_vae: bool = False
    tile_size: int = 512

    @classmethod
    def from_dict(cls, raw: dict) -> "ImageSettings":
        """Tolerant of missing and legacy keys, so old history still replays."""
        known = {f.name: f for f in fields(cls)}
        out = cls()
        for key, value in (raw or {}).items():
            if key not in known or value is None:
                continue
            if key == "loras":
                out.loras = [normalize_lora(entry) for entry in value or []]
                continue
            current = getattr(out, key)
            try:
                setattr(out, key, type(current)(value) if not isinstance(current, bool)
                        else bool(value))
            except (TypeError, ValueError):
                pass
        return out

    def to_dict(self) -> dict:
        return {
            **{f.name: getattr(self, f.name) for f in fields(self) if f.name != "loras"},
            "loras": [list(entry) for entry in self.loras],
        }


def normalize_lora(entry) -> tuple[str, float, float]:
    """Accept (name, strength) from older records as well as the 3-tuple form."""
    if isinstance(entry, dict):
        name = str(entry.get("name", ""))
        model_s = float(entry.get("strength", entry.get("strength_model", 0.8)))
        clip_s = float(entry.get("strength_clip", model_s))
        return name, model_s, clip_s
    parts = list(entry)
    name = str(parts[0])
    model_s = float(parts[1]) if len(parts) > 1 else 0.8
    clip_s = float(parts[2]) if len(parts) > 2 else model_s
    return name, model_s, clip_s


class _ControlNet:
    """The ControlNet half of a graph, built once and applied many times.

    The model is loaded by a single node no matter how many panels use it - a
    nine-panel page must not load 2.5GB nine times - while each panel gets its
    own hint image and its own apply node, because the whole point is that each
    panel keeps *its own* composition.

    An instance is only ever created when the graph can actually carry it; the
    callers hold `None` otherwise, so every call site reads the same way.
    """

    def __init__(self, add, supported, settings: "ImageSettings") -> None:
        self.add = add
        self.supported = supported
        self.settings = settings
        node = add(
            "ControlNetLoader", {"control_net_name": settings.controlnet}, "ControlNet"
        )
        link: list = [node, 0]
        # The union models carry every control type in one file and have to be
        # told which one is meant. A plain ControlNet has no such input, so
        # setting it would make the graph invalid - hence asking the catalogue.
        known = controlnets.by_name(settings.controlnet)
        want = settings.controlnet_union_type or (
            known.union_type if known and known.union else ""
        )
        if want and want in controlnets.UNION_TYPES and supported("SetUnionControlNetType"):
            link = [add("SetUnionControlNetType",
                        {"control_net": link, "type": want}, "ControlNet type"), 0]
        self.link = link

    @staticmethod
    def usable(settings: "ImageSettings", supported) -> bool:
        return bool(
            settings.controlnet
            and supported("ControlNetLoader")
            and supported("ControlNetApplyAdvanced")
            and supported("LoadImage")
        )

    def apply(self, positive: list, negative: list, image_name: str,
              width: int, height: int, tag: str = "") -> tuple[list, list]:
        """Route one panel's conditioning through its own hint image."""
        if not image_name:
            return positive, negative
        s = self.settings
        loaded = self.add("LoadImage", {"image": image_name}, f"Control source{tag}")
        # The hint has to be the size of the thing being drawn, or the outlines
        # land in the wrong place and the result is a smeared double exposure.
        hint: list = [self.add(
            "ImageScale",
            {"image": [loaded, 0], "upscale_method": "lanczos",
             "width": width, "height": height, "crop": "center"},
            f"Fit control{tag}",
        ), 0]
        if s.controlnet_preprocess == "canny" and self.supported("Canny"):
            low = max(0.01, min(s.controlnet_low, 0.99))
            high = max(low + 0.01, min(s.controlnet_high, 0.99))
            hint = [self.add(
                "Canny",
                {"image": hint, "low_threshold": round(low, 2),
                 "high_threshold": round(high, 2)},
                f"Edges{tag}",
            ), 0]
        applied = self.add(
            "ControlNetApplyAdvanced",
            {
                "positive": positive, "negative": negative, "control_net": self.link,
                "image": hint,
                "strength": round(max(0.0, min(s.controlnet_strength, 2.0)), 2),
                "start_percent": round(max(0.0, min(s.controlnet_start, 1.0)), 3),
                "end_percent": round(max(0.0, min(s.controlnet_end, 1.0)), 3),
            },
            f"Apply ControlNet{tag}",
        )
        return [applied, 0], [applied, 1]


def defaults_for(model: ImageModel) -> ImageSettings:
    return ImageSettings(
        steps=model.steps, cfg=model.cfg, sampler=model.sampler,
        scheduler=model.scheduler, clip_skip=model.clip_skip,
    )


def build_comic(
    model: ImageModel,
    settings: ImageSettings,
    *,
    panels: list[tuple],
    negative: str,
    seed: int,
    available_nodes: set[str] | None = None,
    filename_prefix: str = "comic/out",
) -> dict:
    """One graph that renders every panel of a page, each at its own size.

    A panel is `(prompt, width, height)`, or `(prompt, width, height, control)`
    where `control` names an image already uploaded to ComfyUI. That fourth
    slot is how a restaged page keeps the original's shot composition: each
    panel is guided by the crop it was measured from.

    Panels are separate branches with their own SaveImage rather than one
    batched latent, for two reasons: a batch forces every image to the same
    dimensions, and a page wants a tall panel next to a wide one; and ImageBatch
    could not stitch them afterwards anyway. Each panel therefore lands as its
    own file and the page is assembled from those.

    Everything before the sampler - checkpoint, LoRAs, patches, CLIP skip - is
    built once and shared, so N panels cost one model load, not N.
    """
    nodes: dict[str, dict] = {}
    n = 0
    have = available_nodes

    def add(class_type: str, inputs: dict, title: str = "") -> str:
        nonlocal n
        n += 1
        nodes[str(n)] = {
            "class_type": class_type,
            "inputs": inputs,
            "_meta": {"title": title or class_type},
        }
        return str(n)

    def supported(class_type: str) -> bool:
        return have is None or class_type in have

    ckpt = add("CheckpointLoaderSimple", {"ckpt_name": model.file.name}, "Checkpoint")
    model_link: list = [ckpt, 0]
    clip_link: list = [ckpt, 1]
    vae_link: list = [ckpt, 2]

    for name, strength_model, strength_clip in settings.loras:
        node = add(
            "LoraLoader",
            {
                "model": model_link, "clip": clip_link, "lora_name": name,
                "strength_model": strength_model, "strength_clip": strength_clip,
            },
            f"LoRA {name}",
        )
        model_link, clip_link = [node, 0], [node, 1]

    if settings.freeu and supported("FreeU_V2"):
        node = add("FreeU_V2", {"model": model_link, "b1": 1.3, "b2": 1.4,
                                "s1": 0.9, "s2": 0.2}, "FreeU v2")
        model_link = [node, 0]
    if settings.pag > 0 and supported("PerturbedAttentionGuidance"):
        node = add("PerturbedAttentionGuidance",
                   {"model": model_link, "scale": round(settings.pag, 2)}, "PAG")
        model_link = [node, 0]
    if settings.rescale_cfg > 0 and supported("RescaleCFG"):
        node = add("RescaleCFG",
                   {"model": model_link,
                    "multiplier": round(min(settings.rescale_cfg, 1.0), 2)}, "Rescale CFG")
        model_link = [node, 0]

    if settings.clip_skip < -1:
        node = add("CLIPSetLastLayer",
                   {"clip": clip_link, "stop_at_clip_layer": settings.clip_skip}, "CLIP skip")
        clip_link = [node, 0]

    if supported("VAELoader") and any(f.folder == "vae" for f in model.extra_files):
        vae_name = next(f.name for f in model.extra_files if f.folder == "vae")
        vae_link = [add("VAELoader", {"vae_name": vae_name}, "VAE (fp16 fix)"), 0]

    neg = add("CLIPTextEncode", {"clip": clip_link, "text": negative}, "Negative")
    can_upscale = supported("UpscaleModelLoader") and supported("ImageUpscaleWithModel")

    # One loader for the whole page; the per-panel apply nodes come later.
    control = (
        _ControlNet(add, supported, settings)
        if _ControlNet.usable(settings, supported)
        and any(len(p) > 3 and p[3] for p in panels)
        else None
    )

    for index, panel in enumerate(panels):
        text, width, height = panel[0], panel[1], panel[2]
        control_image = str(panel[3]) if len(panel) > 3 and panel[3] else ""
        tag = f" P{index + 1}"
        pos = add("CLIPTextEncode", {"clip": clip_link, "text": text}, f"Prompt{tag}")
        pos_link: list = [pos, 0]
        neg_link: list = [neg, 0]
        if control is not None:
            pos_link, neg_link = control.apply(
                pos_link, neg_link, control_image, width, height, tag
            )
        latent = add("EmptyLatentImage",
                     {"width": width, "height": height, "batch_size": 1}, f"Latent{tag}")
        # Each panel gets its own seed so a page is not four variations of one
        # composition, but a fixed page seed still reproduces the whole page.
        sampled = add(
            "KSampler",
            {
                "model": model_link, "seed": seed + index, "steps": settings.steps,
                "cfg": settings.cfg, "sampler_name": settings.sampler,
                "scheduler": settings.scheduler, "positive": pos_link,
                "negative": neg_link, "latent_image": [latent, 0], "denoise": 1.0,
            },
            f"Sample{tag}",
        )
        if settings.tiled_vae and supported("VAEDecodeTiled"):
            decoded = add(
                "VAEDecodeTiled",
                {"samples": [sampled, 0], "vae": vae_link,
                 "tile_size": max(64, settings.tile_size), "overlap": 64,
                 "temporal_size": 64, "temporal_overlap": 8},
                f"Decode{tag}",
            )
        else:
            decoded = add("VAEDecode", {"samples": [sampled, 0], "vae": vae_link},
                          f"Decode{tag}")
        link: list = [decoded, 0]
        if settings.upscaler and can_upscale:
            loader = add("UpscaleModelLoader", {"model_name": settings.upscaler},
                         f"Upscale model{tag}")
            link = [add("ImageUpscaleWithModel",
                        {"upscale_model": [loader, 0], "image": link}, f"Upscale{tag}"), 0]
        # Zero-padded so the panels sort back into page order on disk.
        add("SaveImage",
            {"images": link, "filename_prefix": f"{filename_prefix}-p{index + 1:02d}"},
            f"Save{tag}")

    return nodes


def build(
    model: ImageModel,
    settings: ImageSettings,
    *,
    prompt: str | list[str],
    negative: str,
    seed: int,
    width: int,
    height: int,
    init_image: str = "",
    control_image: str = "",
    use_vae: bool = True,
    available_nodes: set[str] | None = None,
    filename_prefix: str = "img/out",
) -> dict:
    """SDXL graph: text-to-image or image-to-image, with optional hi-res and upscale.

    The shape is the one every ComfyUI SDXL workflow converges on, assembled in
    code so the knobs stay data:

        checkpoint -> LoRA chain -> patches -> KSampler -> [hi-res] -> decode
                                 -> CLIP skip -> two CLIPTextEncode
        latent: EmptyLatentImage, or VAEEncode of an uploaded image

    `prompt` may be a list, one entry per image. That is how wildcards earn
    their keep: a batch of four with `{red|blue|green}` needs four *different*
    prompts, and a single batched latent can only carry one. When the list has
    more than one distinct entry the graph forks into one sampler per image and
    the results are stitched back together with ImageBatch; the plain batched
    latent is kept for the ordinary case because it is faster.
    """
    nodes: dict[str, dict] = {}
    n = 0
    have = available_nodes

    def add(class_type: str, inputs: dict, title: str = "") -> str:
        nonlocal n
        n += 1
        nodes[str(n)] = {
            "class_type": class_type,
            "inputs": inputs,
            "_meta": {"title": title or class_type},
        }
        return str(n)

    def supported(class_type: str) -> bool:
        return have is None or class_type in have

    ckpt = add("CheckpointLoaderSimple", {"ckpt_name": model.file.name}, "Checkpoint")
    model_link: list = [ckpt, 0]
    clip_link: list = [ckpt, 1]
    vae_link: list = [ckpt, 2]

    # LoRAs affect both the model and the text encoder, so LoraLoader (not the
    # model-only variant used for video) is the right node here. The two
    # strengths are separate on purpose: style LoRAs often want a weaker CLIP
    # side so they do not hijack the wording of the prompt.
    for name, strength_model, strength_clip in settings.loras:
        node = add(
            "LoraLoader",
            {
                "model": model_link,
                "clip": clip_link,
                "lora_name": name,
                "strength_model": strength_model,
                "strength_clip": strength_clip,
            },
            f"LoRA {name}",
        )
        model_link, clip_link = [node, 0], [node, 1]

    # Model patches, in the order the ComfyUI examples chain them.
    if settings.freeu and supported("FreeU_V2"):
        patched = add(
            "FreeU_V2",
            {"model": model_link, "b1": 1.3, "b2": 1.4, "s1": 0.9, "s2": 0.2},
            "FreeU v2",
        )
        model_link = [patched, 0]
    if settings.pag > 0 and supported("PerturbedAttentionGuidance"):
        patched = add(
            "PerturbedAttentionGuidance",
            {"model": model_link, "scale": round(settings.pag, 2)},
            "PAG",
        )
        model_link = [patched, 0]
    if settings.rescale_cfg > 0 and supported("RescaleCFG"):
        patched = add(
            "RescaleCFG",
            {"model": model_link, "multiplier": round(min(settings.rescale_cfg, 1.0), 2)},
            "Rescale CFG",
        )
        model_link = [patched, 0]

    if settings.clip_skip < -1:
        clip_node = add(
            "CLIPSetLastLayer",
            {"clip": clip_link, "stop_at_clip_layer": settings.clip_skip},
            "CLIP skip",
        )
        clip_link = [clip_node, 0]

    if use_vae and supported("VAELoader"):
        if any(f.folder == "vae" for f in model.extra_files):
            vae_name = next(f.name for f in model.extra_files if f.folder == "vae")
            vae_node = add("VAELoader", {"vae_name": vae_name}, "VAE (fp16 fix)")
            vae_link = [vae_node, 0]

    batch = max(1, min(settings.batch, 16))
    texts = [prompt] if isinstance(prompt, str) else list(prompt) or [""]
    texts = texts[:batch]
    # One branch per distinct prompt; the last one carries any leftover images.
    forked = len(set(texts)) > 1
    if not forked:
        texts = texts[:1]

    neg = add("CLIPTextEncode", {"clip": clip_link, "text": negative}, "Negative")
    control = (
        _ControlNet(add, supported, settings)
        if control_image and _ControlNet.usable(settings, supported)
        else None
    )

    source_image: list | None = None
    if init_image:
        # image-to-image: the uploaded picture becomes the starting latent, and
        # denoise decides how much of it survives.
        loaded = add("LoadImage", {"image": init_image}, "Source image")
        scaled = add(
            "ImageScale",
            {
                "image": [loaded, 0],
                "upscale_method": "lanczos",
                "width": width,
                "height": height,
                "crop": "center",
            },
            "Fit to size",
        )
        source_image = [scaled, 0]

    def make_latent(count: int) -> str:
        if source_image is not None:
            encoded = add("VAEEncode", {"pixels": source_image, "vae": vae_link}, "Encode")
            if count > 1:
                return add(
                    "RepeatLatentBatch", {"samples": [encoded, 0], "amount": count}, "Batch"
                )
            return encoded
        return add(
            "EmptyLatentImage",
            {"width": width, "height": height, "batch_size": count},
            "Empty latent",
        )

    denoise = max(0.05, min(settings.denoise, 1.0)) if init_image else 1.0

    def sample(
        latent_node: str, denoise_value: float, steps: int, title: str,
        positive: list, noise_seed: int, negative: list | None = None,
    ) -> str:
        return add(
            "KSampler",
            {
                "model": model_link,
                "seed": noise_seed,
                "steps": steps,
                "cfg": settings.cfg,
                "sampler_name": settings.sampler,
                "scheduler": settings.scheduler,
                "positive": positive,
                "negative": negative if negative is not None else [neg, 0],
                "latent_image": [latent_node, 0],
                "denoise": denoise_value,
            },
            title,
        )

    def decode(latent_node: str, title: str = "Decode") -> str:
        if settings.tiled_vae and supported("VAEDecodeTiled"):
            return add(
                "VAEDecodeTiled",
                {
                    "samples": [latent_node, 0],
                    "vae": vae_link,
                    "tile_size": max(64, settings.tile_size),
                    "overlap": 64,
                    "temporal_size": 64,
                    "temporal_overlap": 8,
                },
                title + " (tiled)",
            )
        return add("VAEDecode", {"samples": [latent_node, 0], "vae": vae_link}, title)

    can_upscale = supported("UpscaleModelLoader") and supported("ImageUpscaleWithModel")

    def branch(text: str, count: int, noise_seed: int, tag: str) -> list:
        """One prompt all the way to a decoded image, ready to save."""
        pos = add("CLIPTextEncode", {"clip": clip_link, "text": text}, f"Prompt{tag}")
        pos_link: list = [pos, 0]
        neg_link: list = [neg, 0]
        if control is not None:
            pos_link, neg_link = control.apply(
                pos_link, neg_link, control_image, width, height, tag
            )
        latent = make_latent(count)
        sampled = sample(latent, denoise, settings.steps, f"Sample{tag}", pos_link,
                         noise_seed, neg_link)

        if settings.hires_scale and settings.hires_scale > 1.0:
            target_w = int(width * settings.hires_scale) // 8 * 8
            target_h = int(height * settings.hires_scale) // 8 * 8
            hires_steps = settings.hires_steps or settings.steps
            hires_denoise = max(0.05, min(settings.hires_denoise, 1.0))
            if settings.hires_upscaler and can_upscale:
                # Enlarge with a trained GAN, then re-diffuse. Sharper than
                # growing the latent, which just interpolates and leaves the
                # sampler to invent everything back.
                decoded = decode(sampled, f"Decode for upscale{tag}")
                loader = add(
                    "UpscaleModelLoader",
                    {"model_name": settings.hires_upscaler},
                    "Upscale model",
                )
                big = add(
                    "ImageUpscaleWithModel",
                    {"upscale_model": [loader, 0], "image": [decoded, 0]},
                    f"Upscale{tag}",
                )
                fitted = add(
                    "ImageScale",
                    {
                        "image": [big, 0],
                        "upscale_method": "lanczos",
                        "width": target_w,
                        "height": target_h,
                        "crop": "disabled",
                    },
                    f"Fit to target{tag}",
                )
                reencoded = add(
                    "VAEEncode", {"pixels": [fitted, 0], "vae": vae_link}, f"Re-encode{tag}"
                )
                sampled = sample(
                    reencoded, hires_denoise, hires_steps, f"Hi-res pass{tag}",
                    pos_link, noise_seed, neg_link,
                )
            else:
                up = add(
                    "LatentUpscale",
                    {
                        "samples": [sampled, 0],
                        "upscale_method": "nearest-exact",
                        "width": target_w,
                        "height": target_h,
                        "crop": "disabled",
                    },
                    f"Upscale latent{tag}",
                )
                sampled = sample(
                    up, hires_denoise, hires_steps, f"Hi-res pass{tag}", pos_link,
                    noise_seed, neg_link,
                )

        return [decode(sampled, f"Decode{tag}"), 0]

    if forked:
        # Each image gets its own prompt and its own noise, then they are
        # stitched into one batch so a single SaveImage writes them all.
        links = [
            branch(text, 1, seed + i, f" {i + 1}") for i, text in enumerate(texts)
        ]
        image_link = links[0]
        for extra in links[1:]:
            merged = add("ImageBatch", {"image1": image_link, "image2": extra}, "Combine")
            image_link = [merged, 0]
    else:
        image_link = branch(texts[0], batch, seed, "")

    # A final plain enlargement, after everything else. No sampler runs, so it
    # costs seconds rather than another full generation.
    if settings.upscaler and can_upscale:
        loader = add(
            "UpscaleModelLoader", {"model_name": settings.upscaler}, "Upscale model"
        )
        final = add(
            "ImageUpscaleWithModel",
            {"upscale_model": [loader, 0], "image": image_link},
            "Final upscale",
        )
        image_link = [final, 0]

    add("SaveImage", {"images": image_link, "filename_prefix": filename_prefix}, "Save")
    return nodes

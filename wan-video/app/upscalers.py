"""GAN upscale models: the thing "hi-res fix" is actually supposed to use.

Enlarging in latent space (LatentUpscale) is what a from-scratch ComfyUI graph
does because it needs no extra download, but it is the weaker option: it blurs,
and the second sampler pass has to reinvent the detail. A trained ESRGAN-family
upscaler reconstructs detail directly, is ~100x faster than another diffusion
pass, and costs 60MB on disk.

ComfyUI's own utility-gan_upscaler template uses RealESRGAN_x4plus from
Comfy-Org/Real-ESRGAN_repackaged; the others here are the ESRGAN models that
actually get used in the image-generation community. Every filename and size
below came from the Hugging Face API, not from memory.

The models are loaded by spandrel, which ComfyUI already depends on, so `.pth`
and `.safetensors` both work with no extra install.
"""

from __future__ import annotations

from dataclasses import dataclass

from registry import ModelFile


@dataclass(frozen=True)
class Upscaler:
    id: str
    label: str
    file: ModelFile
    scale: int
    best_for: str

    @property
    def name(self) -> str:
        return self.file.name

    @property
    def size(self) -> int:
        return self.file.size


UPSCALERS: list[Upscaler] = [
    Upscaler(
        id="ultrasharp",
        label="4x-UltraSharp",
        file=ModelFile("lokCX/4x-Ultrasharp", "4x-UltraSharp.pth", "upscale_models", 66961958),
        scale=4,
        best_for="通用首選。銳利、細節多，動漫和寫實都好用。不知道選哪個就選這個。",
    ),
    Upscaler(
        id="realesrgan",
        label="RealESRGAN x4plus",
        file=ModelFile(
            "Comfy-Org/Real-ESRGAN_repackaged",
            "RealESRGAN_x4plus.safetensors", "upscale_models", 66857836,
        ),
        scale=4,
        best_for="最保守、最不會出錯的一個，ComfyUI 官方範例用的就是它。畫面乾淨但比較平。",
    ),
    Upscaler(
        id="remacri",
        label="4x Remacri",
        file=ModelFile(
            "uwg/upscaler", "ESRGAN/4x_foolhardy_Remacri.pth", "upscale_models", 67025055,
        ),
        scale=4,
        best_for="寫實照片、皮膚紋理。比 UltraSharp 柔一點，不會把皮膚變成砂紙。",
    ),
    Upscaler(
        id="ultrasharp-v2",
        label="4x-UltraSharpV2",
        file=ModelFile(
            "Kim2091/UltraSharpV2", "4x-UltraSharpV2.safetensors", "upscale_models", 139792588,
        ),
        scale=4,
        best_for="UltraSharp 的新版，更會處理壓縮痕跡，但檔案大一倍、也慢一點。",
    ),
]

# ModelFile.name is the basename, and the downloader writes every file flat
# into models/<folder>/, so this is exactly what UpscaleModelLoader will list -
# including for Remacri, whose repo path carries an ESRGAN/ prefix.
BY_ID = {u.id: u for u in UPSCALERS}
BY_NAME = {u.name: u for u in UPSCALERS}


def get(upscaler_id: str) -> Upscaler | None:
    return BY_ID.get(upscaler_id)


HELP = (
    "放大模型是專門訓練來「補細節」的小模型（約 60MB），和畫圖的底模無關。"
    "它比再跑一次擴散快幾百倍，也不會把構圖畫歪 —— "
    "純放大選它，想連內容一起重畫就用「高解析重繪」。"
    "影片也吃同一批模型（官方的 GAN upscaler 範例就是這樣做的）。"
)


@dataclass(frozen=True)
class Interpolator:
    """A frame-interpolation model: invents in-between frames to raise fps.

    Wan renders at 16fps, which reads as visibly choppy. Doubling to 32fps costs
    seconds and no VRAM worth mentioning, and it is the single biggest
    "why does mine look worse than theirs" difference in a Wan clip.

    Core ComfyUI 0.33 gained FrameInterpolate / FrameInterpolationModelLoader,
    so this needs no custom nodes - only a model in models/frame_interpolation/.
    Filenames and sizes are from Comfy-Org's own repo for these nodes.
    """

    id: str
    label: str
    file: ModelFile
    best_for: str

    @property
    def name(self) -> str:
        return self.file.name

    @property
    def size(self) -> int:
        return self.file.size


INTERP_REPO = "Comfy-Org/frame_interpolation"

INTERPOLATORS: list[Interpolator] = [
    Interpolator(
        id="rife426",
        label="RIFE 4.26",
        file=ModelFile(
            INTERP_REPO, "frame_interpolation/rife_v4.26.safetensors",
            "frame_interpolation", 22674688,
        ),
        best_for="通用首選。22MB，很快，動作流暢度提升最明顯。",
    ),
    Interpolator(
        id="rife425-heavy",
        label="RIFE 4.25 heavy",
        file=ModelFile(
            INTERP_REPO, "frame_interpolation/rife_v4.25_heavy.safetensors",
            "frame_interpolation", 86669816,
        ),
        best_for="大動作、快速鏡頭比較不會糊，但慢一些、檔案也大。",
    ),
    Interpolator(
        id="film",
        label="FILM",
        file=ModelFile(
            INTERP_REPO, "frame_interpolation/film_net_fp16.safetensors",
            "frame_interpolation", 68882302,
        ),
        best_for="另一種演算法。RIFE 出現鬼影時可以換這個試試。",
    ),
]

INTERP_BY_ID = {i.id: i for i in INTERPOLATORS}

INTERP_HELP = (
    "補幀 = 在原本的畫格之間補出新的畫格，讓影片變順。"
    "Wan 出來是 16fps，看起來會頓；補成 2 倍就是 32fps，順很多。"
    "它不會改變內容，也幾乎不吃顯存，只是多花幾秒。"
)


def interpolator(interp_id: str) -> Interpolator | None:
    return INTERP_BY_ID.get(interp_id)

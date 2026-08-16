"""ControlNet: keep a picture's composition while replacing everything in it.

This is the piece that makes "same panel layout, different character" mean the
same *shot* and not just the same rectangle. Tag-copying alone reproduces
"1girl, classroom, from above"; ControlNet reproduces the actual framing, the
angle of the body, where the horizon sits. The original art is turned into
outlines and the sampler is told to stay on them.

Only core ComfyUI 0.33 nodes are involved - ControlNetLoader,
ControlNetApplyAdvanced, SetUnionControlNetType and Canny all ship with
ComfyUI, so nothing here needs a custom node pack. That constraint is why the
catalogue stops where it does: openpose and depth models exist and are good,
but their preprocessors (DWPose, Depth-Anything) are custom nodes, and a model
you cannot feed is not a feature.

Every repo path and byte size below came from the Hugging Face API.
"""

from __future__ import annotations

from dataclasses import dataclass

from registry import ModelFile

# The union model's `type` values, straight out of comfy/cldm/control_types.py.
# "auto" is accepted by the node as well and lets it guess.
UNION_TYPES = (
    "auto",
    "openpose",
    "depth",
    "hed/pidi/scribble/ted",
    "canny/lineart/anime_lineart/mlsd",
    "normal",
    "segment",
    "tile",
    "repaint",
)


@dataclass(frozen=True)
class ControlNet:
    id: str
    label: str
    file: ModelFile
    union: bool
    # Which UNION_TYPES entry to set when this model is a union model.
    union_type: str
    best_for: str

    @property
    def name(self) -> str:
        return self.file.name

    @property
    def size(self) -> int:
        return self.file.size


CONTROLNETS: list[ControlNet] = [
    ControlNet(
        id="union-promax",
        label="ControlNet Union Promax (SDXL)",
        file=ModelFile(
            "xinsir/controlnet-union-sdxl-1.0",
            "diffusion_pytorch_model_promax.safetensors",
            "controlnet",
            2513342408,
            save_as="controlnet-union-sdxl-promax.safetensors",
        ),
        union=True,
        union_type="canny/lineart/anime_lineart/mlsd",
        best_for=(
            "不知道選哪個就選這個。一個檔案包含線稿、深度、姿勢、tile 等多種控制，"
            "漫畫分鏡克隆用的就是它的線稿模式。"
        ),
    ),
    ControlNet(
        id="canny",
        label="ControlNet Canny (SDXL)",
        file=ModelFile(
            "xinsir/controlnet-canny-sdxl-1.0",
            "diffusion_pytorch_model_V2.safetensors",
            "controlnet",
            2502139104,
            save_as="controlnet-canny-sdxl-v2.safetensors",
        ),
        union=False,
        union_type="",
        best_for="只做線稿一件事，但做得很紮實。上面那個在你的 ComfyUI 上不相容時用這個。",
    ),
    ControlNet(
        id="scribble",
        label="ControlNet Scribble (SDXL)",
        file=ModelFile(
            "xinsir/controlnet-scribble-sdxl-1.0",
            "diffusion_pytorch_model.safetensors",
            "controlnet",
            2502139104,
            save_as="controlnet-scribble-sdxl.safetensors",
        ),
        union=False,
        union_type="",
        best_for=(
            "抓得最鬆。只想保留「人在左邊、桌子在右邊」這種大致構圖、"
            "其他全部重畫時用它。也吃你自己隨手畫的草圖。"
        ),
    ),
]

BY_ID = {c.id: c for c in CONTROLNETS}
BY_NAME = {c.name: c for c in CONTROLNETS}


def get(controlnet_id: str) -> ControlNet | None:
    return BY_ID.get(controlnet_id)


def by_name(filename: str) -> ControlNet | None:
    """A catalogue entry for an installed file, if we know it.

    Unknown files are still usable - they are just treated as non-union, which
    is the safe assumption: setting a union type on a plain ControlNet would
    make the graph invalid, while not setting one on a union model only costs
    it the hint and it falls back to guessing.
    """
    return BY_NAME.get(filename)


# How to turn the source picture into something the ControlNet understands.
# "canny" is the only real preprocessor core ComfyUI has; "none" hands the
# picture over untouched, which is what tile/repaint and already-lineart
# sources want.
PREPROCESSORS = {
    "canny": "邊緣偵測：抽出線條。分鏡克隆的預設，構圖跟得最準。",
    "none": "不處理，直接把原圖丟給 ControlNet。原圖本來就是線稿、或用 tile 模式時選這個。",
}

HELP = {
    "controlnet": (
        "ControlNet 會把一張參考圖的「構圖」鎖住，然後讓模型重畫裡面的東西。"
        "漫畫分鏡克隆就是靠它 —— 只複製標籤只能得到「差不多的場景」，"
        "加上 ControlNet 才會得到「同一個鏡頭、同一個角度、換一個人」。"
    ),
    "strength": (
        "抓多緊。0.5～0.8 是甜蜜點：構圖跟得住，模型也還有空間畫新角色。"
        "拉到 1.0 以上會連原角色的體型都複製過來，反而換不掉人。"
    ),
    "start": "從第幾成的步數開始管。留 0 就是一開始就管。",
    "end": (
        "管到第幾成就放手。這是最重要的一格：設 0.6～0.8 表示「前面照著構圖畫，"
        "後面放手讓它畫細節」，臉和手會明顯比全程 1.0 好看。"
    ),
    "preprocess": "怎麼把參考圖變成控制訊號。分鏡克隆用「邊緣偵測」。",
    "threshold": (
        "邊緣偵測的鬆緊。低的抓到比較多線（連網點都算），高的只留主要輪廓。"
        "原圖很花時把低的調高一點。"
    ),
}

NOTE = (
    "ControlNet 模型約 2.5GB，和底模無關，下載一次所有 SDXL 底模都能用"
    "（Illustrious / Pony / Juggernaut 都是 SDXL）。"
)

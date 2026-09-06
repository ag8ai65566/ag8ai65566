"""Character LoRA training: plan the dataset, check it, emit a real config.

Why this module exists
----------------------
Every route to a consistent face in a multi-shot drama ends at the same place:
a LoRA trained on that face. Reference images, IP-Adapter and inpainting all
help, but they are per-image work, and a 25-shot episode is 25 chances to
drift. So the app needs to get the user from "I have some pictures" to "I have
a trained character" without them guessing at parameters.

What this module does **not** do
--------------------------------
It does not train. Training needs a GPU, several hours and one of the trainers
below - none of which live in this app, and none of which this project has ever
run. What it does instead is the part that is checkable without a GPU:

  * plan how many images of what kind (``DatasetPlan``)
  * inspect a folder of images and say what is wrong with it (``check_dataset``)
  * write the captions in the shape the trainer expects (``caption_for``)
  * emit a config file for the right trainer, with the numbers filled in
    (``config_for``), plus the exact command to run it

That split is deliberate. A wrapper that shelled out to a trainer this project
has never executed would be an untested claim wearing a button. Preparing the
dataset is real work, it is where beginners actually fail, and it is verifiable
here - so that is what is implemented.

Every number that is a recommendation rather than an arithmetic fact is
registered in ``claims.py`` and carries its evidence grade into the UI.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path

import claims


SCHEMA_VERSION = 1

# Formats PIL opens and every trainer below reads.
IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".webp", ".bmp")


# -- what a dataset should look like ------------------------------------------

@dataclass(frozen=True)
class ShotMix:
    """One slice of the training set: how much of it, and why that framing."""

    key: str
    zh: str
    share: float          # fraction of the whole set
    why: str


# The point of the mix is that a LoRA learns what it is shown. Thirty portraits
# of one face at one distance produce a character who only exists at that
# distance - which is exactly the wrong shape for a drama that needs wide shots.
SHOT_MIX: tuple[ShotMix, ...] = (
    ShotMix("face", "臉部／肩上（正面、四分之三、側面）", 0.30,
            "身份主要從這裡學。三個角度都要有，不然側臉會崩。"),
    ShotMix("half", "半身", 0.30,
            "對白鏡頭最常用的景別。"),
    ShotMix("full", "全身、不同姿勢", 0.25,
            "缺這一段，遠景就會變成另一個人。"),
    ShotMix("hard", "困難條件：低角度、俯視、不同表情、不同光線", 0.15,
            "這一段決定它在你真正要用的鏡頭裡撐不撐得住。"),
)


@dataclass(frozen=True)
class Trainer:
    """A trainer this app can write a config for."""

    id: str
    label: str
    trains: tuple[str, ...]      # architectures
    repo: str
    vram_gb: int
    claim_id: str
    config_format: str           # "toml" | "yaml"
    why: str


TRAINERS: dict[str, Trainer] = {
    "kohya": Trainer(
        id="kohya", label="kohya_ss",
        trains=("sdxl",),
        repo="https://github.com/bmaltais/kohya_ss",
        vram_gb=24,
        claim_id="train.kohya_sdxl",
        config_format="toml",
        why="SDXL 角色 LoRA 最成熟的一條路，社群參數最多人驗證過。",
    ),
    "onetrainer": Trainer(
        id="onetrainer", label="OneTrainer",
        trains=("sdxl", "flux"),
        repo="https://github.com/Nerogar/OneTrainer",
        vram_gb=24,
        claim_id="train.onetrainer",
        config_format="json",
        why="有 GUI、資料管理方便；SDXL 和 FLUX 都能訓。",
    ),
    "ai-toolkit": Trainer(
        id="ai-toolkit", label="ai-toolkit",
        trains=("flux",),
        repo="https://github.com/ostris/ai-toolkit",
        vram_gb=24,
        claim_id="train.aitoolkit_flux",
        config_format="yaml",
        why="FLUX 角色 LoRA 的標準工具，官方就附 24GB 的設定檔。",
    ),
    "diffusion-pipe": Trainer(
        id="diffusion-pipe", label="diffusion-pipe",
        trains=("wan", "hunyuan", "ltx"),
        repo="https://github.com/tdrussell/diffusion-pipe",
        vram_gb=24,
        claim_id="train.diffusionpipe_video",
        config_format="toml",
        why="影片模型的 LoRA（Wan / HunyuanVideo / LTX）。24GB 是緊繃配置。",
    ),
}


@dataclass(frozen=True)
class Recipe:
    """Training hyper-parameters for one architecture.

    These are starting points, not tuned optima - nothing here was measured by
    this project. They are registered as a claim so the UI cannot present them
    as more than they are.
    """

    arch: str
    zh: str
    trainer_id: str
    network_dim: int
    network_alpha: int
    learning_rate: float
    text_encoder_lr: float
    optimizer: str
    scheduler: str
    resolution: int
    batch_size: int
    repeats: int
    epochs: int
    claim_id: str
    note: str = ""

    def steps_for(self, image_count: int) -> int:
        """Total optimiser steps this recipe implies for a given set size.

        Plain arithmetic - images x repeats x epochs / batch - not a claim.
        """
        if image_count <= 0 or self.batch_size <= 0:
            return 0
        return math.ceil(image_count * self.repeats * self.epochs / self.batch_size)


RECIPES: dict[str, Recipe] = {
    "sdxl": Recipe(
        arch="sdxl", zh="SDXL 寫實人物", trainer_id="kohya",
        network_dim=32, network_alpha=16,
        learning_rate=1e-4, text_encoder_lr=1e-5,
        optimizer="AdamW8bit", scheduler="cosine",
        resolution=1024, batch_size=1, repeats=10, epochs=6,
        claim_id="train.sdxl_recipe",
        note="寫實人臉的 dim 不需要開很大；開太大反而更容易把訓練圖的光線和瑕疵一起學進去。",
    ),
    "flux": Recipe(
        arch="flux", zh="FLUX 寫實人物", trainer_id="ai-toolkit",
        network_dim=16, network_alpha=16,
        learning_rate=1e-4, text_encoder_lr=0.0,
        optimizer="adamw8bit", scheduler="constant",
        resolution=1024, batch_size=1, repeats=10, epochs=6,
        claim_id="train.flux_recipe",
        note="FLUX 一般不訓 text encoder，所以 text_encoder_lr 是 0。",
    ),
    "wan": Recipe(
        arch="wan", zh="Wan 影片 LoRA", trainer_id="diffusion-pipe",
        network_dim=32, network_alpha=32,
        learning_rate=2e-5, text_encoder_lr=0.0,
        optimizer="adamw8bit", scheduler="constant",
        resolution=512, batch_size=1, repeats=5, epochs=10,
        claim_id="train.wan_recipe",
        note="影片 LoRA 比圖片 LoRA 貴一個數量級。身份先用關鍵幀的 SDXL/FLUX LoRA 鎖，"
             "這裡留給動作或風格。",
    ),
}


# -- captions -----------------------------------------------------------------

# A trigger has to be a token the base model has no prior opinion about. A real
# name is the classic mistake: "emma" already means something to the model and
# the LoRA then fights that meaning instead of filling an empty slot.
TRIGGER_RE = re.compile(r"^[a-z][a-z0-9_]{2,31}$")


def check_trigger(trigger: str) -> str:
    """Return a complaint about this trigger word, or '' if it is fine."""
    t = (trigger or "").strip()
    if not t:
        return "要有一個觸發詞，不然沒有東西可以叫出這個角色。"
    if not TRIGGER_RE.match(t):
        return ("觸發詞只能用小寫英數和底線，開頭是字母，3-32 字："
                "像 `s1vra_person`。中文和空格在標註檔裡會被切開。")
    if t in COMMON_WORDS:
        return (f"`{t}` 是底模本來就認得的字，LoRA 會跟它原本的意思打架。"
                "改成一個沒有意義的字，像 `s1vra_person`。")
    return ""


COMMON_WORDS = {
    "woman", "man", "girl", "boy", "person", "female", "male", "lady",
    "model", "actress", "actor", "portrait", "photo", "character", "human",
}


def caption_for(trigger: str, *, shot: str = "", hair: str = "", eyes: str = "",
                expression: str = "", wearing: str = "", setting: str = "",
                light: str = "") -> str:
    """Build one caption in the shape the recipes above expect.

    The rule that matters is which side of the comma a detail goes on. Anything
    described in the caption is being taught as *variable*; anything left out is
    being folded into the trigger. So the pose, the clothes, the framing and the
    light are all named - and the face is not, because the face is the thing
    being learnt.
    """
    parts = [trigger.strip(), "adult"]
    for value in (shot, hair, eyes, expression, wearing, setting, light):
        if value and value.strip():
            parts.append(value.strip())
    return ", ".join(p for p in parts if p)


# -- looking at what the user actually has ------------------------------------

@dataclass
class Sample:
    """One image in a training folder, plus whatever is wrong with it."""

    name: str
    width: int
    height: int
    caption: str = ""
    problems: list[str] = field(default_factory=list)

    @property
    def long_edge(self) -> int:
        return max(self.width, self.height)

    @property
    def ratio(self) -> float:
        return self.width / self.height if self.height else 0.0

    def public(self) -> dict:
        return {"name": self.name, "width": self.width, "height": self.height,
                "caption": self.caption, "problems": self.problems,
                "long_edge": self.long_edge, "ratio": round(self.ratio, 3)}


@dataclass
class Finding:
    id: str
    level: str
    zh: str
    detail: str = ""
    kind: str = "INTEGRITY"
    claim_id: str = ""

    def public(self) -> dict:
        claim = claims.get(self.claim_id) if self.claim_id else None
        return {"id": self.id, "level": self.level, "zh": self.zh,
                "detail": self.detail, "kind": self.kind,
                "claim_id": self.claim_id,
                "badge": claim.badge if claim else "資料檢查",
                "claim": claim.public() if claim else None}


def read_dataset(folder: Path) -> list[Sample]:
    """Read a folder of images plus their sidecar .txt captions.

    Sizes come from the file header via PIL, not from the filename - a folder
    curated by hand is full of images that were renamed but never resized.
    """
    from PIL import Image

    out: list[Sample] = []
    if not folder.is_dir():
        return out
    for path in sorted(folder.iterdir()):
        if path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        try:
            with Image.open(path) as im:
                width, height = im.size
        except Exception:
            out.append(Sample(path.name, 0, 0, problems=["讀不開，可能不是圖片或檔案壞了"]))
            continue
        caption_path = path.with_suffix(".txt")
        caption = ""
        if caption_path.is_file():
            try:
                caption = caption_path.read_text(encoding="utf-8").strip()
            except OSError:
                caption = ""
        out.append(Sample(path.name, width, height, caption=caption))
    return out


def _bucket(sample: Sample) -> str:
    """Coarse aspect bucket, used only to see whether the set is all one shape."""
    r = sample.ratio
    if r <= 0:
        return "?"
    if r < 0.7:
        return "直式"
    if r > 1.4:
        return "橫式"
    return "方形"


def check_dataset(samples: list[Sample], *, trigger: str = "",
                  arch: str = "sdxl") -> list[Finding]:
    """Everything wrong with this training set that can be seen without a GPU.

    Ordered by how much it costs to find out later: a set that is too small
    wastes the whole run, a missing caption wastes the trigger, and a set that
    is all one framing produces a character who only exists at one distance -
    which you discover three hours in, on the first wide shot.
    """
    recipe = RECIPES.get(arch) or RECIPES["sdxl"]
    out: list[Finding] = []
    usable = [s for s in samples if s.width and s.height]

    if complaint := check_trigger(trigger):
        out.append(Finding("trigger", claims.BLOCK, "觸發詞有問題。", complaint))

    broken = [s for s in samples if not (s.width and s.height)]
    if broken:
        out.append(Finding(
            "unreadable", claims.BLOCK,
            f"有 {len(broken)} 個檔案讀不開。",
            "、".join(s.name for s in broken[:5])
            + ("…" if len(broken) > 5 else "")
            + " —— 訓練會在中途停掉，先把它們挑掉。"))

    count = len(usable)
    if count == 0:
        out.append(Finding("empty", claims.BLOCK, "這個資料夾裡沒有圖。",
                           "把角色的圖放進去再回來。"))
        return out
    if count < 10:
        out.append(_claim_finding(
            "too-few", "train.dataset_size", claims.BLOCK,
            f"只有 {count} 張，太少了。",
            "10-15 張是能起步的最低，20-40 張才是常見的範圍。"))
    elif count < 20:
        out.append(_claim_finding(
            "few", "train.dataset_size", claims.WARN,
            f"{count} 張，勉強夠。",
            "20-40 張比較穩。現在這個數量對側臉和全身會比較弱。"))
    elif count > 60:
        out.append(_claim_finding(
            "many", "train.dataset_size", claims.INFO,
            f"{count} 張，比常見範圍多。",
            "不是錯，但每多一張就多一份把它的光線和瑕疵學進去的機會。"
            "寧可挑掉不確定的那幾張。"))

    small = [s for s in usable if s.long_edge < recipe.resolution]
    if small:
        out.append(_claim_finding(
            "low-res", "train.resolution", claims.WARN,
            f"有 {len(small)} 張長邊不到 {recipe.resolution}。",
            f"最小的是 {min(s.long_edge for s in small)}px（{recipe.zh}要 "
            f"{recipe.resolution}）。放大過的圖會把插值的糊一起教進去 —— "
            "與其塞進來，不如不要。"))

    buckets = {}
    for s in usable:
        buckets[_bucket(s)] = buckets.get(_bucket(s), 0) + 1
    if len(buckets) == 1 and count >= 10:
        only = next(iter(buckets))
        out.append(_claim_finding(
            "one-shape", "train.shot_mix", claims.WARN,
            f"全部 {count} 張都是{only}。",
            "整組同一個比例，通常表示也是同一個景別。"
            "臉、半身、全身要都有，不然遠景會變成另一個人。"))

    captioned = [s for s in usable if s.caption.strip()]
    if not captioned:
        out.append(_claim_finding(
            "no-captions", "train.captions", claims.BLOCK,
            "一張標註都沒有。",
            "每張圖旁邊要有一個同名的 .txt。沒有標註，模型不知道哪些是"
            "「這個人」、哪些只是那天的衣服和光線，兩者會黏在一起。"))
    elif len(captioned) < count:
        out.append(Finding(
            "some-captions", claims.BLOCK,
            f"{count - len(captioned)} 張沒有標註。",
            "、".join(s.name for s in usable if not s.caption.strip())[:120]
            + " —— 少一張就是少一張的控制權。"))

    if trigger and captioned:
        missing = [s for s in captioned if trigger.lower() not in s.caption.lower()]
        if missing:
            out.append(Finding(
                "trigger-missing", claims.BLOCK,
                f"有 {len(missing)} 張的標註裡沒有 `{trigger}`。",
                "觸發詞要出現在**每一張**的標註裡，否則那幾張等於在訓練"
                "一個叫不出來的東西。"))

    dupes: dict[str, list[str]] = {}
    for s in captioned:
        dupes.setdefault(s.caption.strip().lower(), []).append(s.name)
    repeated = {c: names for c, names in dupes.items() if len(names) > 1}
    if repeated and len(captioned) >= 10:
        worst = max(repeated.values(), key=len)
        out.append(_claim_finding(
            "same-caption", "train.captions", claims.WARN,
            f"有 {sum(len(v) for v in repeated.values())} 張的標註一模一樣。",
            f"最多的一組有 {len(worst)} 張。標註完全相同，等於沒有告訴模型"
            "這幾張差在哪 —— 姿勢、服裝、景別、光線要分別寫出來。"))

    steps = recipe.steps_for(count)
    out.append(Finding(
        "steps", claims.INFO,
        f"照這個配方，{count} 張會跑 {steps} 步。",
        f"{count} 張 × {recipe.repeats} repeats × {recipe.epochs} epochs "
        f"÷ batch {recipe.batch_size}。這是算出來的，不是建議值。",
        kind="INTEGRITY"))
    return out


def _claim_finding(finding_id: str, claim_id: str, level: str,
                   zh: str, detail: str) -> Finding:
    claim = claims.get(claim_id)
    return Finding(finding_id, level, zh, detail,
                   kind=claim.evidence_kind if claim else "INTEGRITY",
                   claim_id=claim_id)


def summary(findings: list[Finding]) -> dict:
    counts = {p: sum(1 for f in findings if f.level == p) for p in claims.POLICIES}
    if counts[claims.BLOCK]:
        line, level = f"有 {counts[claims.BLOCK]} 個一定要先修的問題", "high"
    elif counts[claims.WARN]:
        line, level = f"有 {counts[claims.WARN]} 個值得看一下的地方", "warn"
    else:
        line, level = "這組資料可以拿去訓練", "ok"
    return {"level": level, "line": line, "counts": counts,
            "findings": [f.public() for f in findings]}


def plan_for(count: int) -> list[dict]:
    """How the requested number of images should be split across framings.

    Largest-remainder, so the parts always add back up to the whole - a plan
    that says 30/30/25/15 of 25 images and lists 24 is a plan nobody trusts.
    """
    if count <= 0:
        return [{**{"key": m.key, "zh": m.zh, "why": m.why},
                 "share": m.share, "count": 0} for m in SHOT_MIX]
    raw = [(m, m.share * count) for m in SHOT_MIX]
    base = [(m, int(v)) for m, v in raw]
    short = count - sum(v for _, v in base)
    order = sorted(range(len(raw)), key=lambda i: raw[i][1] - base[i][1], reverse=True)
    counts = [v for _, v in base]
    for i in order[:short]:
        counts[i] += 1
    return [{"key": m.key, "zh": m.zh, "why": m.why, "share": m.share,
             "count": c} for (m, _), c in zip(raw, counts)]


# -- the config the trainer actually reads ------------------------------------

def _toml_value(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value)
    return json.dumps(str(value), ensure_ascii=False)


def _toml(section: str, pairs: list[tuple[str, object]]) -> str:
    body = "\n".join(f"{k} = {_toml_value(v)}" for k, v in pairs)
    return f"[{section}]\n{body}\n"


@dataclass
class TrainJob:
    """Everything needed to start one training run, as files plus a command."""

    trigger: str
    arch: str
    dataset_dir: str
    output_dir: str
    output_name: str
    base_model: str
    image_count: int
    # A recipe names the trainer it was written for, but more than one trainer
    # can train the same architecture - OneTrainer does SDXL as well as kohya.
    # An empty string means "whatever the recipe says".
    trainer_override: str = ""

    @property
    def recipe(self) -> Recipe:
        return RECIPES.get(self.arch) or RECIPES["sdxl"]

    @property
    def trainer(self) -> Trainer:
        chosen = TRAINERS.get(self.trainer_override)
        if chosen and self.arch in chosen.trains:
            return chosen
        return TRAINERS[self.recipe.trainer_id]

    @property
    def steps(self) -> int:
        return self.recipe.steps_for(self.image_count)


def config_for(job: TrainJob) -> dict:
    """The config file and the command line for this job.

    Returned as text rather than written to disk: the trainer runs on the
    user's machine, in their own checkout, and this app has no business
    deciding where their training folder lives.
    """
    recipe, trainer = job.recipe, job.trainer
    if trainer.id == "kohya":
        text = _kohya_toml(job)
        filename = f"{job.output_name}.toml"
        command = (f"accelerate launch sdxl_train_network.py "
                   f"--config_file \"{filename}\"")
    elif trainer.id == "ai-toolkit":
        text = _aitoolkit_yaml(job)
        filename = f"{job.output_name}.yaml"
        command = f"python run.py \"{filename}\""
    elif trainer.id == "diffusion-pipe":
        text = _diffusionpipe_toml(job)
        filename = f"{job.output_name}.toml"
        command = (f"deepspeed --num_gpus=1 train.py "
                   f"--deepspeed --config \"{filename}\"")
    else:
        text = _onetrainer_json(job)
        filename = f"{job.output_name}.json"
        command = "OneTrainer 的 GUI：Load config → 選這個檔 → Start training"
    return {
        "trainer": trainer.id, "trainer_label": trainer.label,
        "repo": trainer.repo, "format": trainer.config_format,
        "filename": filename, "text": text, "command": command,
        "steps": job.steps, "vram_gb": trainer.vram_gb,
        "claim_id": recipe.claim_id,
    }


def _kohya_toml(job: TrainJob) -> str:
    r = job.recipe
    return (
        f"# {job.output_name} — {r.zh}\n"
        f"# 由 wan-video 產生。這些是起點參數，本專案沒有跑過任何一次訓練。\n"
        f"# 預期 {job.image_count} 張 × {r.repeats} repeats × {r.epochs} epochs "
        f"= {job.steps} 步。\n\n"
        + _toml("model_arguments", [
            ("pretrained_model_name_or_path", job.base_model),
            ("v2", False), ("v_parameterization", False), ("sdxl", True),
        ]) + "\n"
        + _toml("dataset_arguments", [
            ("train_data_dir", job.dataset_dir),
            ("resolution", f"{r.resolution},{r.resolution}"),
            # Buckets are what let a mixed set of framings train together. Without
            # them every image is cropped square and the full-body shots - the
            # ones that stop the character collapsing at distance - lose their legs.
            ("enable_bucket", True),
            ("min_bucket_reso", 640), ("max_bucket_reso", 1536),
            ("bucket_reso_steps", 64), ("bucket_no_upscale", True),
            ("caption_extension", ".txt"), ("shuffle_caption", True),
            # The trigger must survive shuffling, so it is pinned as the first token.
            ("keep_tokens", 1),
        ]) + "\n"
        + _toml("training_arguments", [
            ("output_dir", job.output_dir), ("output_name", job.output_name),
            ("save_model_as", "safetensors"),
            ("max_train_epochs", r.epochs),
            ("dataset_repeats", r.repeats),
            ("train_batch_size", r.batch_size),
            ("learning_rate", r.learning_rate),
            ("text_encoder_lr", r.text_encoder_lr),
            ("unet_lr", r.learning_rate),
            ("optimizer_type", r.optimizer),
            ("lr_scheduler", r.scheduler),
            ("lr_warmup_steps", max(1, job.steps // 20)),
            ("mixed_precision", "bf16"), ("save_precision", "bf16"),
            # The three that decide whether 24GB is enough.
            ("gradient_checkpointing", True),
            ("cache_latents", True), ("cache_latents_to_disk", True),
            ("xformers", True), ("max_data_loader_n_workers", 2),
            ("seed", 42),
            # Every epoch, not just the last: a LoRA that is right at epoch 4 and
            # overfitted at 6 is the normal case, and without these you cannot
            # go back and pick.
            ("save_every_n_epochs", 1),
        ]) + "\n"
        + _toml("network_arguments", [
            ("network_module", "networks.lora"),
            ("network_dim", r.network_dim),
            ("network_alpha", r.network_alpha),
        ])
    )


def _aitoolkit_yaml(job: TrainJob) -> str:
    r = job.recipe
    return f"""# {job.output_name} — {r.zh}
# 由 wan-video 產生。起點參數，本專案沒有跑過任何一次訓練。
job: extension
config:
  name: {job.output_name}
  process:
    - type: sd_trainer
      training_folder: {job.output_dir}
      device: cuda:0
      network:
        type: lora
        linear: {r.network_dim}
        linear_alpha: {r.network_alpha}
      save:
        dtype: float16
        save_every: {max(1, job.steps // r.epochs)}
        max_step_saves_to_keep: {r.epochs}
      datasets:
        - folder_path: {job.dataset_dir}
          caption_ext: txt
          caption_dropout_rate: 0.05
          shuffle_tokens: false
          cache_latents_to_disk: true
          resolution: [{r.resolution}]
      train:
        batch_size: {r.batch_size}
        steps: {job.steps}
        gradient_accumulation_steps: 1
        train_unet: true
        train_text_encoder: false
        gradient_checkpointing: true
        noise_scheduler: flowmatch
        optimizer: {r.optimizer}
        lr: {r.learning_rate}
        dtype: bf16
      model:
        name_or_path: {job.base_model}
        is_flux: true
        quantize: true
      sample:
        sampler: flowmatch
        sample_every: {max(1, job.steps // 4)}
        width: 1024
        height: 1024
        prompts:
          - "{job.trigger}, adult, three-quarter portrait, soft window light"
          - "{job.trigger}, adult, full body, standing, indoor"
"""


def _diffusionpipe_toml(job: TrainJob) -> str:
    r = job.recipe
    return (
        f"# {job.output_name} — {r.zh}\n"
        f"# 由 wan-video 產生。起點參數，本專案沒有跑過任何一次訓練。\n"
        f"# 影片 LoRA 比圖片 LoRA 貴一個數量級，先確認你真的需要它。\n\n"
        + _toml("", [
            ("output_dir", job.output_dir),
            ("dataset", f"{job.output_name}_dataset.toml"),
            ("epochs", r.epochs),
            ("micro_batch_size_per_gpu", r.batch_size),
            ("pipeline_stages", 1),
            ("gradient_accumulation_steps", 1),
            ("gradient_clipping", 1.0),
            ("warmup_steps", max(1, job.steps // 20)),
            ("save_every_n_epochs", 1),
            # Block swapping is the reason this fits on 24GB at all.
            ("blocks_to_swap", 20),
        ]).replace("[]\n", "")
        + "\n" + _toml("model", [
            ("type", "wan"), ("ckpt_path", job.base_model),
            ("dtype", "bfloat16"), ("transformer_dtype", "float8"),
            ("timestep_sample_method", "logit_normal"),
        ]) + "\n"
        + _toml("adapter", [
            ("type", "lora"), ("rank", r.network_dim), ("dtype", "bfloat16"),
        ]) + "\n"
        + _toml("optimizer", [
            ("type", r.optimizer), ("lr", r.learning_rate),
            ("betas", "0.9, 0.99"), ("weight_decay", 0.01),
        ])
    )


def _onetrainer_json(job: TrainJob) -> str:
    r = job.recipe
    return json.dumps({
        "__comment": f"{job.output_name} — {r.zh}。由 wan-video 產生，"
                     "起點參數，本專案沒有跑過任何一次訓練。",
        "training_method": "LORA",
        "model_type": "STABLE_DIFFUSION_XL_10_BASE" if job.arch == "sdxl" else "FLUX_DEV_1",
        "base_model_name": job.base_model,
        "output_model_destination": f"{job.output_dir}/{job.output_name}.safetensors",
        "lora_rank": r.network_dim, "lora_alpha": float(r.network_alpha),
        "learning_rate": r.learning_rate,
        "optimizer": {"optimizer": r.optimizer.upper()},
        "learning_rate_scheduler": r.scheduler.upper(),
        "epochs": r.epochs, "batch_size": r.batch_size,
        "resolution": str(r.resolution),
        "aspect_ratio_bucketing": True,
        "gradient_checkpointing": True,
        "latent_caching": True,
        "train_text_encoder": r.text_encoder_lr > 0,
        "concepts": [{"path": job.dataset_dir, "repeats": r.repeats,
                      "include_subdirectories": False}],
    }, ensure_ascii=False, indent=2)

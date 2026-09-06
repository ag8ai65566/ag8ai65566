"""短劇 projects: a shot list, the format rules, and what to generate per shot.

This is the piece between "I can make a five-second clip" and "I have an
episode". The clip was never the hard part - the hard part is that an episode is
a hundred of them that have to look like the same person in the same room, and
that discipline is bookkeeping, not prompting.

Everything here comes out of docs/short-drama.md, which reverse-engineers how
the AI short-drama platforms actually work. Three findings shape this module:

**The asset layer is the ceiling.** Character consistency measures ~85-90% with
a closed platform's reference-image feature, 90-95% with IP-Adapter plus
ControlNet, and near 100% with a per-character LoRA trained on 30-50 images.
Manual retouching is over 40% of total production hours, and almost all of it is
paying off consistency that was not locked down first. So a project here starts
by naming its cast and their LoRAs, and refuses to be useful until it has.

**A 3.2-second median shot is a technical limit written into an aesthetic.**
An eight-minute episode is ~117 shots. Video models drift as a clip runs long -
faces wander, hands fail, physics gives up - and three seconds is roughly where
this generation still holds. Cutting often is a quality technique, not a
shortcut, so the validator says so when shots run long.

**The visible "AI tell" in the platforms' NSFW shots is a frame-rate artifact,
and it is self-inflicted.** They run two tracks - commercial APIs for ordinary
shots, local models for the ones an API would refuse - and those tracks have
different native frame rates that meet on one timeline. A local-only pipeline
has no reason to make that compromise, so the validator treats mixed frame rates
as an error rather than a preference. It is the one place where being unable to
use a filtered API is an advantage.

Nothing here filters content. A shot type is a shot type.
"""

from __future__ import annotations

import json
import re
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

import registry


# -- the format ---------------------------------------------------------------
# Industry convention for vertical short drama, not invented here. Sources in
# docs/short-drama.md; the numbers are what the validator measures against.

EPISODE_SECONDS = (60, 180)      # 1-3 minutes per episode
SHOT_MEDIAN_TARGET = 3.2         # seconds; the measured median of a real episode
SHOT_LONG = 6.0                  # past here a clip visibly drifts
DIALOGUE_MAX_CHARS = 15          # per line, so it can be read at short-drama pace
EPISODE_DIALOGUE_CHARS = (200, 300)
HOOK_SECONDS = 3.0               # the "golden three seconds"

# 景別 - the shot sizes a storyboard actually uses, with the danbooru/booru tag
# that puts a still image at that distance. The tag matters: this is what gets
# composed into the keyframe prompt, and the image models were trained on these
# exact strings.
SHOT_SIZES: dict[str, dict] = {
    "特寫": {"tag": "portrait, close-up", "zh": "臉部特寫", "why": "情緒。短劇有一半的鏡頭是這個。"},
    "近景": {"tag": "upper body", "zh": "胸上", "why": "對話的預設景別。"},
    "中景": {"tag": "cowboy shot", "zh": "膝上", "why": "看得到手勢和一點環境。"},
    "全身": {"tag": "full body", "zh": "全身", "why": "進場、離場、打鬥。"},
    "過肩": {"tag": "over-the-shoulder shot, from behind", "zh": "過肩", "why": "兩人對峙。"},
    "俯拍": {"tag": "from above", "zh": "由上往下", "why": "壓迫感、示弱。"},
    "仰拍": {"tag": "from below", "zh": "由下往上", "why": "威脅感、氣勢。"},
    "特寫物件": {"tag": "still life, close-up, no humans", "zh": "道具特寫", "why": "轉場、伏筆。很省，很好用。"},
}

# How a shot gets from a still to moving pictures. `model` names the video model
# family it needs, so the validator can say "you have not downloaded that yet".
METHODS: dict[str, dict] = {
    "i2v": {
        "zh": "圖生影片", "needs": "video",
        "why": "一張關鍵幀 → 動起來。沒有台詞的鏡頭都用這個。",
    },
    "flf": {
        "zh": "首尾幀", "needs": "video",
        "why": "出兩張關鍵幀，中間交給模型。運鏡要準的時候用。",
    },
    "s2v": {
        "zh": "說話（音訊驅動）", "needs": "s2v",
        "why": "音訊驅動、原生口型同步。**有台詞的鏡頭用這個**，"
               "而且音檔要先做好——音檔長度決定鏡頭長度。",
    },
    "animate": {
        "zh": "動作轉移", "needs": "animate",
        "why": "拿一段參考影片的姿勢＋表情，套到你的角色身上。"
               "甩巴掌、轉身、摔門這種短劇高頻動作，錄一次就能重複用。",
    },
}

MODEL_ROLE = {"video": "wan22-14b-fp8", "s2v": "wan22-s2v", "animate": "wan22-animate"}


# -- one project --------------------------------------------------------------

@dataclass
class Character:
    """A cast member. `lora` is the whole point - see the module docstring."""

    key: str
    name: str
    lora: str = ""              # installed LoRA filename, "" = not trained yet
    trigger: str = ""           # prompt fragment that summons them
    costume: str = ""           # locked wardrobe tags, pasted verbatim every shot
    voice: str = ""             # TTS voice sample id, for dialogue shots
    note: str = ""

    def public(self) -> dict:
        return asdict(self)


@dataclass
class Shot:
    no: int
    seconds: float = 3.2
    size: str = "近景"          # key into SHOT_SIZES
    who: list[str] = field(default_factory=list)   # Character.key
    action: str = ""            # what happens, in plain words
    dialogue: str = ""          # spoken line, "" for silent shots
    method: str = "i2v"         # key into METHODS
    scene: str = ""             # location, matched against the scene library
    extra: str = ""             # anything else that goes in the prompt verbatim
    keyframe: str = ""          # job id of the still
    video: str = ""             # job id of the clip
    status: str = "todo"        # todo | keyframe | video | done | fix
    note: str = ""

    def public(self) -> dict:
        return asdict(self)


@dataclass
class Project:
    id: str
    title: str = ""
    # The spec, locked before anything is generated. See `SPECS`.
    model: str = "hy15-720p"    # the ONE video model for the whole episode
    fps: int = 24
    width: int = 832            # keyframe size; SDXL-native, upscaled later
    height: int = 1216
    deliver_width: int = 1080
    deliver_height: int = 1920
    image_model: str = "noobai"
    style: str = ""             # style recipe id from styles.py
    cast: list[Character] = field(default_factory=list)
    shots: list[Shot] = field(default_factory=list)
    created: float = field(default_factory=time.time)
    note: str = ""

    @property
    def seconds(self) -> float:
        return round(sum(s.seconds for s in self.shots), 1)

    @property
    def dialogue_chars(self) -> int:
        return sum(len(_clean_line(s.dialogue)) for s in self.shots)

    @property
    def median_shot(self) -> float:
        if not self.shots:
            return 0.0
        lengths = sorted(s.seconds for s in self.shots)
        mid = len(lengths) // 2
        if len(lengths) % 2:
            return round(lengths[mid], 2)
        return round((lengths[mid - 1] + lengths[mid]) / 2, 2)

    def character(self, key: str) -> Character | None:
        return next((c for c in self.cast if c.key == key), None)

    def public(self) -> dict:
        return {
            "id": self.id, "title": self.title, "model": self.model, "fps": self.fps,
            "width": self.width, "height": self.height,
            "deliver_width": self.deliver_width, "deliver_height": self.deliver_height,
            "image_model": self.image_model, "style": self.style,
            "created": self.created, "note": self.note,
            "cast": [c.public() for c in self.cast],
            "shots": [s.public() for s in self.shots],
            "seconds": self.seconds, "shot_count": len(self.shots),
            "median_shot": self.median_shot, "dialogue_chars": self.dialogue_chars,
            "done": sum(1 for s in self.shots if s.status == "done"),
        }


def _clean_line(text: str) -> str:
    """Dialogue length is counted in characters people read, not punctuation."""
    return re.sub(r"[\s，。！？、,.!?…「」“”\"']", "", text or "")


# -- spec presets -------------------------------------------------------------
# One video model for the whole episode, and the frame rate that model is native
# at. Mixing is the single artifact that gives the AI platforms away, and it is
# only forced on them because half their shots have to go through an API that
# would refuse the other half. Running everything locally, there is no reason to
# inherit that compromise - so these presets exist to stop it happening by
# accident.

@dataclass(frozen=True)
class Spec:
    id: str
    label: str
    model: str
    fps: int
    clip_seconds: float
    finish: str          # what to do about frame rate at the end
    why: str


SPECS: list[Spec] = [
    Spec("hunyuan-24", "HunyuanVideo 1.5 · 24fps 原生（推薦）",
         "hy15-720p", 24, 5.04,
         "時間線就設 24fps，**一格都不用補幀**。",
         "人臉與物理最自然，而且 24fps 是原生的 —— 交付 24fps 就完全不會有補幀痕跡，"
         "那正是那些平台最明顯的破綻。"),
    Spec("wan5b-24", "Wan 2.2 5B · 24fps 原生",
         "wan22-5b", 24, 5.04,
         "時間線就設 24fps，不用補幀。",
         "輕量、快、原生 720p。12GB 顯卡的實際選擇。"),
    Spec("wan14b-16", "Wan 2.2 I2V 14B · 16fps（NSFW LoRA 最多）",
         "wan22-14b-fp8", 16, 5.06,
         "RIFE ×2 → **32fps 整條交付**，或整條均勻 retime 到 30fps"
         "（慢 6.25%，看不出來，不掉幀不抖）。**絕不要 16 直接補到 30**。",
         "社群為 Wan 2.2 訓練的 LoRA 遠多於其他模型，成人題材尤其。"
         "代價是 16fps 不是整數倍，補幀要照上面那樣做才不會露餡。"),
]

SPEC_BY_ID = {s.id: s for s in SPECS}


# -- building the prompt for one shot -----------------------------------------

def keyframe_prompt(project: Project, shot: Shot) -> dict:
    """Compose the still-image prompt for one shot, in the order that matters.

    Order is not decoration. The danbooru-trained checkpoints were captioned as
    `<count>, <character>, <series>, <artist>, <special>, <general>`, and the
    front of the prompt pulls hardest - so the character and their locked
    costume go first, the camera next, and the loose description last where it
    can flavour without overriding.
    """
    bits: list[str] = []
    people = [project.character(k) for k in shot.who]
    people = [p for p in people if p]

    count = {0: "", 1: "1girl", 2: "2girls"}.get(len(people), f"{len(people)} people")
    if count:
        bits.append(count)
    for who in people:
        if who.trigger:
            bits.append(who.trigger)
        if who.costume:
            bits.append(who.costume)

    size = SHOT_SIZES.get(shot.size)
    if size:
        bits.append(size["tag"])
    if shot.scene:
        bits.append(shot.scene)
    if shot.action:
        bits.append(shot.action)
    if shot.extra:
        bits.append(shot.extra)

    # Deduped through the same comparison the merge engine uses, because a
    # character trigger very often already starts with `1girl` and a doubled tag
    # is a silent double weight rather than an emphasis.
    import promptmerge

    pieces: list[str] = []
    for chunk in bits:
        pieces.extend(promptmerge.split_tags(chunk))
    return {
        "prompt": ", ".join(promptmerge.dedupe(pieces)),
        "loras": [w.lora for w in people if w.lora],
        "model": project.image_model,
        "width": project.width, "height": project.height,
        "style": project.style,
    }


def shot_plan(project: Project, shot: Shot) -> dict:
    """Everything the user has to do for this shot, in order, with the reason."""
    method = METHODS.get(shot.method, METHODS["i2v"])
    steps = []
    if shot.dialogue:
        steps.append({
            "do": "先做音檔",
            "why": "S2V 是音訊驅動的，音檔長度決定鏡頭長度。順序顛倒就要重跑。",
        })
    steps.append({
        "do": f"生關鍵幀（{project.width}×{project.height}）",
        "why": "在靜態圖修，不要在影片修。這裡一隻沒修好的手，"
               f"會被複製到這個鏡頭的 {int(shot.seconds * project.fps)} 格裡去。",
    })
    if shot.method == "flf":
        steps.append({"do": "再生一張結束幀", "why": "首尾幀要兩張。"})
    steps.append({
        "do": f"{method['zh']} → {shot.seconds} 秒",
        "why": method["why"],
    })
    return {"no": shot.no, "method": shot.method, "steps": steps,
            "frames": int(round(shot.seconds * project.fps))}


# -- the validator -------------------------------------------------------------
# Same idea as promptdoctor: every finding is a checkable rule with a stated
# source, never a prediction about how the result will look. This project has
# never generated a frame of video, so it cannot make the second kind of claim.

@dataclass
class Finding:
    id: str
    level: str          # high | warn | info
    zh: str
    detail: str = ""
    shots: list[int] = field(default_factory=list)

    def public(self) -> dict:
        return asdict(self)


def check(project: Project, *, installed: set[str] | None = None) -> list[Finding]:
    """Everything wrong with this episode that can be seen without rendering it.

    `installed` is the set of model ids actually on disk. `None` means the
    caller does not know and the download check is skipped; an *empty set* means
    nothing is installed, which is a real answer and must not be confused with
    not knowing - that confusion is why the check silently never fired.
    """
    out: list[Finding] = []
    shots = project.shots

    if not shots:
        out.append(Finding("empty", "info", "還沒有鏡頭。",
                           "先把分鏡表寫完再開始生成。資產層和分鏡沒鎖就開工，"
                           "是人工精修那 40% 工時的第二大來源。"))
        return out

    # -- 1. the cast. This is the ceiling on everything else.
    used = {k for s in shots for k in s.who}
    nameless = sorted(k for k in used if not project.character(k))
    if nameless:
        out.append(Finding(
            "unknown-cast", "high", f"有 {len(nameless)} 個角色沒有在卡司裡定義。",
            f"鏡頭引用了 {'、'.join(nameless)}，但卡司名單裡沒有他們，"
            "所以生成時不會帶到 LoRA、觸發詞或服裝。"))
    no_lora = [c.name for c in project.cast if c.key in used and not c.lora]
    if no_lora:
        out.append(Finding(
            "no-lora", "warn", f"{len(no_lora)} 位角色還沒有專屬 LoRA。",
            "角色一致性：閉源參考圖 85-90%、IP-Adapter＋ControlNet 90-95%、"
            "**專屬 LoRA 接近 100%**。差的那 5-10% 在上百個鏡頭裡會變成"
            "「每十個鏡頭臉就跑掉一次」，而**人工精修佔總工時 40% 以上**，"
            "那 40% 幾乎全是一致性沒鎖好的帳。"
            f"沒訓練的：{'、'.join(no_lora)}"))
    no_costume = [c.name for c in project.cast if c.key in used and not c.costume]
    if no_costume:
        out.append(Finding(
            "no-costume", "info", f"{len(no_costume)} 位角色沒有鎖定服裝。",
            "服裝要寫死成一段文字、每個鏡頭原封不動貼上去。"
            "靠每次重打描述來維持連戲，是穿幫最常見的原因。"))

    # -- 2. frame rate. The one artifact that is entirely self-inflicted.
    spec = next((s for s in SPECS if s.model == project.model), None)
    if spec and spec.fps != project.fps:
        out.append(Finding(
            "fps-mismatch", "high",
            f"時間線設 {project.fps}fps，但 {project.model} 的原生幀率是 {spec.fps}fps。",
            "混幀率就是那些 AI 短劇平台最明顯的破綻 —— 而他們是被內容審核逼的"
            "（一半鏡頭得走商業 API），你不是。整條線都在本機，就沒有理由自己製造這個問題。"
            f"處理方式：{spec.finish}"))

    # -- 3. shot length. A technical limit wearing an aesthetic's clothes.
    long_shots = [s.no for s in shots if s.seconds > SHOT_LONG]
    if long_shots:
        out.append(Finding(
            "long-shots", "warn", f"{len(long_shots)} 個鏡頭超過 {SHOT_LONG} 秒。",
            "AI 影片越長越飄：角色漂移、手壞掉、物理崩掉。"
            f"真實短劇的鏡頭中位數是 {SHOT_MEDIAN_TARGET} 秒，那不是巧合，"
            "是技術限制被寫進了美學。**在它變糟之前就切掉**。",
            long_shots))
    if spec:
        over = [s.no for s in shots if s.seconds > spec.clip_seconds]
        if over:
            out.append(Finding(
                "over-clip", "warn",
                f"{len(over)} 個鏡頭比這個模型單次能生成的長度還長"
                f"（{spec.clip_seconds} 秒）。",
                "超過的部分要嘛拆成兩個鏡頭，要嘛接兩段 —— 接的地方一定看得出來。"
                "拆成兩個鏡頭比較好，反正短劇本來就該多切。", over))
    if project.median_shot > SHOT_MEDIAN_TARGET * 1.6:
        out.append(Finding(
            "slow-pace", "info",
            f"鏡頭中位數 {project.median_shot} 秒，比短劇慣例（{SHOT_MEDIAN_TARGET} 秒）慢不少。",
            "節奏偏慢在短劇裡是真的會掉觀眾的。也不一定要照抄，但要是刻意的。"))

    # -- 4. dialogue. Format conventions, and the lip-sync trap.
    long_lines = [s.no for s in shots if len(_clean_line(s.dialogue)) > DIALOGUE_MAX_CHARS]
    if long_lines:
        out.append(Finding(
            "long-dialogue", "info",
            f"{len(long_lines)} 句台詞超過 {DIALOGUE_MAX_CHARS} 個字。",
            "短劇的台詞慣例是單句壓在 15 字以內、一集有效台詞 200-300 字。"
            "講太長觀眾會滑掉，而且配音也難卡秒數。", long_lines))
    talking_wrong = [s.no for s in shots if s.dialogue and s.method not in ("s2v",)]
    if talking_wrong:
        out.append(Finding(
            "no-lipsync", "warn",
            f"{len(talking_wrong)} 個有台詞的鏡頭沒有用音訊驅動（S2V）。",
            "圖生影片不會對口型。這些鏡頭之後要另外補口型"
            "（InfiniteTalk 或 LatentSync），而補的永遠比原生生的差。"
            "能用 S2V 就用 S2V。", talking_wrong))
    chars = project.dialogue_chars
    lo, hi = EPISODE_DIALOGUE_CHARS
    if chars > hi * 1.5:
        out.append(Finding(
            "wordy", "info", f"整集台詞 {chars} 字，慣例是 {lo}-{hi} 字。",
            "短劇是靠剪和衝突推進的，不是靠台詞。話多通常代表劇情沒有用畫面講。"))

    # -- 5. the hook. Three seconds is the whole industry's number.
    first = shots[0]
    if not (first.action or first.dialogue):
        out.append(Finding(
            "no-hook", "warn", "第一個鏡頭是空的。",
            "**黃金 3 秒**：開篇 30 秒內必須拋出核心衝突或懸念，而第一個鏡頭"
            "決定觀眾要不要看第二個。這是短劇唯一真正不能省的地方。", [first.no]))
    elif first.seconds > HOOK_SECONDS * 2:
        out.append(Finding(
            "slow-hook", "info", f"第一個鏡頭 {first.seconds} 秒，開場偏慢。",
            "黃金 3 秒的意思是前 3 秒就要有東西發生。", [first.no]))

    # -- 6. episode length
    lo_s, hi_s = EPISODE_SECONDS
    if project.seconds < lo_s * 0.5:
        out.append(Finding(
            "short-episode", "info",
            f"整集 {project.seconds} 秒，短劇單集慣例是 {lo_s}-{hi_s} 秒。",
            "比慣例短很多不是錯，但如果是要放到平台上，長度會影響推薦。"))
    elif project.seconds > hi_s * 1.5:
        out.append(Finding(
            "long-episode", "info",
            f"整集 {project.seconds} 秒，比單集慣例（{lo_s}-{hi_s} 秒）長不少。",
            "考慮拆成兩集 —— 多一個結尾就是多一個鉤子。"))

    # -- 7. models actually on disk
    needed = {METHODS[s.method]["needs"] for s in shots if s.method in METHODS}
    for role in sorted(needed):
        want = MODEL_ROLE.get(role)
        if role == "video":
            want = project.model
        if want and installed is not None and want not in installed:
            model = registry.get(want)
            out.append(Finding(
                f"missing-{role}", "high",
                f"有鏡頭需要 {model.label if model else want}，但它還沒下載。",
                "到「模型」分頁下載。" + (
                    f"（{model.download_bytes / 1e9:.1f}GB）" if model else "")))

    # -- 8. keyframe size
    px = project.width * project.height
    if min(project.width, project.height) < 640 or px < 1024 * 1024 * 0.45:
        out.append(Finding(
            "small-keyframe", "high",
            f"關鍵幀設 {project.width}×{project.height}，對 SDXL 太小。",
            "SDXL 是在 1024² 附近訓練的。關鍵幀是整條線裡你控制力最強的地方，"
            "在這裡省像素等於在源頭省畫質。建議 832×1216，最後再放大到 "
            f"{project.deliver_width}×{project.deliver_height}。"))
    if project.width > project.height:
        out.append(Finding(
            "not-vertical", "warn",
            f"關鍵幀是橫的（{project.width}×{project.height}）。",
            "短劇是直式的（9:16）。"))

    order = {"high": 0, "warn": 1, "info": 2}
    out.sort(key=lambda f: order[f.level])
    return out


def summary(findings: list[Finding]) -> dict:
    highs = sum(1 for f in findings if f.level == "high")
    warns = sum(1 for f in findings if f.level == "warn")
    if highs:
        line, level = f"有 {highs} 個要先處理的問題", "high"
    elif warns:
        line, level = f"有 {warns} 個值得看一下的地方", "warn"
    elif findings:
        line, level = "大致沒問題，有幾個小提醒", "info"
    else:
        line, level = "分鏡表看起來沒問題", "ok"
    return {"level": level, "line": line, "high": highs, "warn": warns,
            "info": len(findings) - highs - warns,
            "findings": [f.public() for f in findings]}


# -- the store ----------------------------------------------------------------

class ProjectStore:
    """One JSONL file. Same shape as ExperimentStore, same reasoning."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.items: dict[str, Project] = {}

    def load(self) -> None:
        self.items = {}
        if not self.path.is_file():
            return
        for line in self.path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
                project = Project(
                    id=raw["id"], title=raw.get("title", ""),
                    model=raw.get("model", "hy15-720p"), fps=int(raw.get("fps", 24)),
                    width=int(raw.get("width", 832)), height=int(raw.get("height", 1216)),
                    deliver_width=int(raw.get("deliver_width", 1080)),
                    deliver_height=int(raw.get("deliver_height", 1920)),
                    image_model=raw.get("image_model", "noobai"),
                    style=raw.get("style", ""),
                    created=raw.get("created", time.time()), note=raw.get("note", ""),
                    cast=[Character(**c) for c in raw.get("cast", [])],
                    shots=[Shot(**s) for s in raw.get("shots", [])],
                )
                self.items[project.id] = project
            except Exception:
                continue          # one bad line must not lose the rest

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        rows = [json.dumps({
            "id": p.id, "title": p.title, "model": p.model, "fps": p.fps,
            "width": p.width, "height": p.height,
            "deliver_width": p.deliver_width, "deliver_height": p.deliver_height,
            "image_model": p.image_model, "style": p.style,
            "created": p.created, "note": p.note,
            "cast": [c.public() for c in p.cast],
            "shots": [s.public() for s in p.shots],
        }, ensure_ascii=False) for p in self.items.values()]
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text("".join(r + "\n" for r in rows), encoding="utf-8")
        tmp.replace(self.path)

    def create(self, title: str, spec_id: str = "hunyuan-24") -> Project:
        spec = SPEC_BY_ID.get(spec_id) or SPECS[0]
        project = Project(id=uuid.uuid4().hex[:10], title=title or "未命名短劇",
                          model=spec.model, fps=spec.fps)
        self.items[project.id] = project
        return project

    def get(self, project_id: str) -> Project | None:
        return self.items.get(project_id)

    def delete(self, project_id: str) -> bool:
        return self.items.pop(project_id, None) is not None

    def list(self) -> list[Project]:
        return sorted(self.items.values(), key=lambda p: -p.created)


def renumber(project: Project) -> None:
    """Shot numbers are 1..n in order, always. They are referred to by number."""
    for i, shot in enumerate(project.shots, 1):
        shot.no = i


def public() -> dict:
    """The static half: what the UI needs to render the pickers and the guide."""
    return {
        "sizes": {k: v for k, v in SHOT_SIZES.items()},
        "methods": {k: v for k, v in METHODS.items()},
        "specs": [asdict(s) for s in SPECS],
        "format": {
            "episode_seconds": list(EPISODE_SECONDS),
            "shot_median": SHOT_MEDIAN_TARGET,
            "shot_long": SHOT_LONG,
            "dialogue_max": DIALOGUE_MAX_CHARS,
            "episode_dialogue": list(EPISODE_DIALOGUE_CHARS),
            "hook_seconds": HOOK_SECONDS,
        },
    }

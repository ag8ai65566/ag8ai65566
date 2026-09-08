"""短劇 projects: a shot list, what to generate for each shot, and what is wrong.

This module holds an episode's plan. It does not generate anything - the image
and video tabs do that, because that is where the full controls live - and it
does not decide whether a picture is good, because this project has never
generated one.

What it is responsible for:

  * the delivery spec, the keyframe profile, and one route per shot method
  * the cast, and the prompt fragments locked to each of them
  * the shot list, with a stable id per shot
  * which generation attempts belong to which shot, and which one was accepted
  * validation, split into two kinds that must not be confused

**Validation is two different things.** An INTEGRITY finding says the record is
broken - a speaker who is not in the shot, a negative duration, a method this
project has no route for. Those are facts about the data and are never softened.
A CLAIM-backed finding says something about the world, and every one of them
carries a `claim_id` into `claims.py`, where the evidence behind it is written
down once and graded. Nothing in this file states a claim in its own words.

That separation exists because the first version of this module did not have it,
and an outside review took it apart: "a LoRA is ~100% consistent", "three seconds
is where the model starts to break", "the frame-rate artifact is what gives those
platforms away" were all asserted as fact, in three places each, with nothing
behind them. See `claims.py` for what each of them is actually worth.

Persistence is one JSONL file under the output directory, `schema_version` 2.
Version 1 projects (a single `model` plus `fps`) are migrated on load into the
delivery/keyframe/route split; the old fields are read and never written back,
so there is only ever one source of truth on disk.
"""

from __future__ import annotations

import json
import re
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

import claims
import registry

SCHEMA_VERSION = 3


# -- format constants ---------------------------------------------------------
# Each one is a number some claim in claims.py is about. They live here so the
# validator can compute with them; the *reason* they matter lives there.

EPISODE_SECONDS = (60, 180)          # format.episode_length
SHOT_MEDIAN_REFERENCE = 3.2          # format.shot_median
SHOT_LONG_HINT = 6.0                 # video.drift_with_length - a hint, not a rule
DIALOGUE_MAX_CHARS = 15              # format.line_length
EPISODE_DIALOGUE_CHARS = (200, 300)  # format.line_length
HOOK_SECONDS = 3.0                   # format.hook
VERTICAL_RATIO = 9 / 16              # format.vertical
VERTICAL_TOLERANCE = 0.06            # 4:5 is not 9:16 and must not pass as it
MAX_SHOT_SECONDS = 600.0             # anything beyond this is a typo, not a shot


# 景別. The tag is what gets composed into the keyframe prompt, so it is the
# booru string the image models were actually captioned with.
# `tag` is the danbooru spelling the anime checkpoints were captioned with.
# `photo` is the same framing said the way a photoreal checkpoint understands
# it - `cowboy shot` is a booru word and means nothing to LUSTIFY, while
# "medium shot from the knees up, 50mm" is the vocabulary its captions used.
# Which one is emitted follows the checkpoint's tag_style, not a global switch.
SHOT_SIZES: dict[str, dict] = {
    "特寫": {"tag": "portrait, close-up", "zh": "臉部特寫", "people": True,
             "photo": "close-up portrait, head and shoulders, 85mm lens, "
                      "shallow depth of field",
             "why": "臉部情緒。"},
    "近景": {"tag": "upper body", "zh": "胸上", "people": True,
             "photo": "medium close-up, from the chest up, 50mm lens",
             "why": "看得到表情和上半身手勢。"},
    "中景": {"tag": "cowboy shot", "zh": "膝上", "people": True,
             "photo": "medium shot, from the knees up, 35mm lens",
             "why": "看得到手勢和一點環境。"},
    "全身": {"tag": "full body", "zh": "全身", "people": True,
             "photo": "full body shot, head to feet in frame, 35mm lens",
             "why": "進場、離場、打鬥。"},
    "過肩": {"tag": "over-the-shoulder shot, from behind", "zh": "過肩", "people": True,
             "photo": "over-the-shoulder shot, camera behind one person's shoulder",
             "why": "兩人對峙。"},
    "俯拍": {"tag": "from above", "zh": "由上往下", "people": True,
             "photo": "high angle shot, camera looking down",
             "why": "從上往下拍。"},
    "仰拍": {"tag": "from below", "zh": "由下往上", "people": True,
             "photo": "low angle shot, camera looking up",
             "why": "從下往上拍。"},
    # `people: False` is load-bearing: this size emits `no humans`, so a cast
    # list on the same shot would produce a prompt that contradicts itself.
    "空鏡": {"tag": "still life, close-up, no humans", "zh": "道具／空景特寫",
             "people": False,
             "photo": "still life close-up, no people in frame",
             "why": "沒有人的畫面。會送出 `no humans`，所以不能有出場角色。"},
}

# The count tag that opens a danbooru-style prompt, by who is in the shot.
# Getting this from the cast rather than hard-coding `1girl` is not a detail:
# the first version emitted `1girl` for an all-male shot, so every male
# character was fighting a female count tag at the front of his own prompt.
# `one`/`many` are booru count tags. `photo_one`/`photo_many` say the same
# thing in the words a photoreal checkpoint was captioned with - "1girl" is not
# English and a photo model has no entry for it. Note the photo spelling says
# "woman", never "girl": these are adults.
GENDERS = {
    "female": {"zh": "女", "one": "1girl", "many": "{n}girls",
               "photo_one": "one adult woman", "photo_many": "{n} adult women"},
    "male": {"zh": "男", "one": "1boy", "many": "{n}boys",
             "photo_one": "one adult man", "photo_many": "{n} adult men"},
    "other": {"zh": "其他／不指定", "one": "1other", "many": "{n}others",
              "photo_one": "one adult person", "photo_many": "{n} adult people"},
}


@dataclass(frozen=True)
class Method:
    id: str
    zh: str
    needs_route: bool = True
    needs_endframe: bool = False
    needs_audio: bool = False
    claim_id: str = ""
    why: str = ""


METHODS: dict[str, Method] = {m.id: m for m in (
    Method("i2v", "圖生影片",
           why="一張關鍵幀 → 一段影片。"),
    Method("flf", "首尾幀", needs_endframe=True,
           claim_id="wan22.flf_uses_i2v_weights",
           why="出兩張關鍵幀，中間由模型補。"),
    Method("s2v", "說話（音訊驅動）", needs_audio=True,
           claim_id="s2v.audio_driven",
           why="音檔是輸入，口型在同一個 pass 產生。"),
    Method("animate", "動作轉移",
           why="拿一段參考影片的姿勢與表情，套到你的角色身上。"),
)}

# Which model each method's default route points at. A project may override any
# of them; nothing requires them to be the same model, because they cannot be -
# S2V and Animate are separate checkpoints from the I2V one.
DEFAULT_ROUTE_MODEL = {
    "i2v": "hy15-720p",
    "flf": "wan22-14b-fp8",
    "s2v": "wan22-s2v",
    "animate": "wan22-animate",
}

STAGES = ("keyframe", "endframe", "video", "audio")


# -- the three layers ---------------------------------------------------------
# Locking "one video model for the whole episode" was wrong and the data model
# could not express what actually happens: the moment a project has one line of
# dialogue it needs S2V, which is a different checkpoint from the I2V one. What
# is genuinely locked is the *delivery*; each method then says how it gets there.

@dataclass
class FinishPolicy:
    """How a route's native frame rate reaches the delivery frame rate.

    Machine-readable on purpose. The first version kept this as a sentence of
    Chinese, which meant the actual rule - the one the validator has to check -
    was hidden inside display text and could not be checked at all.
    """

    mode: str = "native"        # native | interpolate | retime | manual
    factor: int = 1             # interpolate: frames multiplier
    retime_audio: bool = False  # retime: was the audio stretched to match?

    def public(self) -> dict:
        return asdict(self)


@dataclass
class Route:
    """How one shot method gets generated."""

    model_id: str
    finish: FinishPolicy = field(default_factory=FinishPolicy)

    @property
    def native_fps(self) -> int:
        model = registry.get(self.model_id)
        return model.fps if model else 0

    @property
    def clip_seconds(self) -> float:
        """Seconds this route's *configured* length produces: frames / fps.

        Not a hard ceiling. The official workflows let the frame count be
        changed and Animate has an extension mechanism, so this is what the
        catalogue's default would generate - which is still worth checking a
        shot against, but is not a limit of the model.
        """
        model = registry.get(self.model_id)
        if not model or not model.fps:
            return 0.0
        return round(model.length / model.fps, 2)

    def delivered_fps(self, delivery_fps: int) -> int:
        """The frame rate this route lands on before the timeline takes over."""
        native = self.native_fps
        if self.finish.mode == "interpolate":
            return native * max(1, self.finish.factor)
        if self.finish.mode in ("retime", "manual"):
            return delivery_fps
        return native

    def public(self) -> dict:
        return {"model_id": self.model_id, "finish": self.finish.public(),
                "native_fps": self.native_fps, "clip_seconds": self.clip_seconds}


@dataclass
class DeliverySpec:
    width: int = 1080
    height: int = 1920
    fps: int = 24
    # What to do with a shot that is not this shape: "cover" crops, "contain"
    # letterboxes. Empty means the user has not been asked, which is the right
    # starting state - both answers throw something away, and which loss is
    # acceptable is not a default worth burying. Nothing asks until a shot
    # actually is the wrong shape, so most projects never see the question.
    # No migration: empty is exactly what an older project means here.
    fit: str = ""

    @property
    def ratio(self) -> float:
        return self.width / self.height if self.height else 0.0

    def public(self) -> dict:
        return {"width": self.width, "height": self.height, "fps": self.fps,
                "fit": self.fit, "ratio": round(self.ratio, 4)}


@dataclass
class KeyframeProfile:
    model_id: str = "noobai"
    # 9:16 (0.565), both axes multiples of 16, and 1.04MP - SDXL's native area.
    # Was 832x1216, which is 2:3: every frame of a 9:16 episode would have had
    # to be cropped by a fifth, because Wan I2V's output follows its input.
    width: int = 768
    height: int = 1360
    style_id: str = ""

    @property
    def pixels(self) -> int:
        return self.width * self.height

    def public(self) -> dict:
        return {"model_id": self.model_id, "width": self.width,
                "height": self.height, "style_id": self.style_id,
                "pixels": self.pixels}


# -- cast and shots -----------------------------------------------------------

@dataclass
class Character:
    key: str
    name: str
    gender: str = "female"      # key into GENDERS; drives the count tag
    trigger: str = ""           # prompt fragment that summons them
    costume: str = ""           # locked wardrobe tags, pasted verbatim
    lora: str = ""              # installed LoRA filename, if one was trained
    voice: str = ""             # TTS voice sample id, for dialogue shots
    note: str = ""

    def public(self) -> dict:
        return asdict(self)


@dataclass
class Shot:
    # A stable id, because the display number is not one: deleting shot 3
    # renumbers everything after it, and a job recorded against "shot 7" would
    # then point at a different shot than the one it was generated for.
    id: str = ""
    no: int = 0
    seconds: float = 3.2
    size: str = "近景"
    who: list[str] = field(default_factory=list)
    speaker: str = ""           # which of `who` is talking; S2V drives them
    # Two prompts, two fields. A still wants a frozen instant ("hand resting on
    # his shoulder"); a video wants change over time ("she walks over and puts
    # her hand on his shoulder"). One field served both and could only ever be
    # right for one of them - the video handoff even carried a comment saying
    # it sent motion while it was sending the still's description.
    action: str = ""            # keyframe: the pose, state and mood in frame
    motion: str = ""            # video: what moves, and how the camera moves
    dialogue: str = ""
    method: str = "i2v"
    scene: str = ""
    extra: str = ""             # anything else, pasted into the prompt verbatim
    # Attempts, not results. One shot is generated several times before one is
    # kept, and the last job to finish is not the one the user chose.
    keyframe_jobs: list[str] = field(default_factory=list)
    endframe_jobs: list[str] = field(default_factory=list)
    video_jobs: list[str] = field(default_factory=list)
    # STAGES has listed "audio" since the first version, but the fields behind
    # it were never added - so a dialogue shot had a stage the data model could
    # not hold. S2V and H3 both take sound as an input, so this is where it goes.
    audio_jobs: list[str] = field(default_factory=list)
    active_keyframe: str = ""   # the accepted take, set only by an explicit act
    active_endframe: str = ""
    active_video: str = ""
    active_audio: str = ""
    note: str = ""

    def jobs_for(self, stage: str) -> list[str]:
        return {"keyframe": self.keyframe_jobs, "endframe": self.endframe_jobs,
                "video": self.video_jobs, "audio": self.audio_jobs}.get(stage, [])

    def active_for(self, stage: str) -> str:
        return {"keyframe": self.active_keyframe, "endframe": self.active_endframe,
                "video": self.active_video,
                "audio": self.active_audio}.get(stage, "")

    def carry_over(self, prior: "Shot | None") -> "Shot":
        """Take every stage's attempts and acceptance from the stored shot.

        The browser edits the shot *table* - seconds, cast, prompts - and must
        never be the source of generation bookkeeping: a stale tab would
        otherwise wipe a finished render on its next save. Written as a loop
        over STAGES rather than a list of fields on purpose. The audio stage
        was added and the copy of it was forgotten, which meant an uploaded
        sound file survived exactly until the next time anything was saved.
        """
        if prior is None:
            return self
        for stage in STAGES:
            self.jobs_for(stage)[:] = list(prior.jobs_for(stage))
            self.set_active(stage, prior.active_for(stage))
        return self

    def set_active(self, stage: str, job_id: str) -> None:
        if stage == "keyframe":
            self.active_keyframe = job_id
        elif stage == "endframe":
            self.active_endframe = job_id
        elif stage == "video":
            self.active_video = job_id
        elif stage == "audio":
            self.active_audio = job_id

    def public(self) -> dict:
        return asdict(self)


@dataclass
class Project:
    id: str
    title: str = ""
    schema_version: int = SCHEMA_VERSION
    delivery: DeliverySpec = field(default_factory=DeliverySpec)
    keyframes: KeyframeProfile = field(default_factory=KeyframeProfile)
    routes: dict[str, Route] = field(default_factory=dict)
    cast: list[Character] = field(default_factory=list)
    shots: list[Shot] = field(default_factory=list)
    created: float = field(default_factory=time.time)
    note: str = ""

    def route(self, method: str) -> Route | None:
        return self.routes.get(method)

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

    @property
    def methods_used(self) -> set[str]:
        return {s.method for s in self.shots if s.method in METHODS}

    def character(self, key: str) -> Character | None:
        return next((c for c in self.cast if c.key == key), None)

    def shot(self, shot_id: str) -> Shot | None:
        return next((s for s in self.shots if s.id == shot_id), None)

    def public(self, jobs: dict | None = None) -> dict:
        states = {s.id: shot_state(s, jobs or {}) for s in self.shots}
        return {
            "id": self.id, "title": self.title, "schema_version": self.schema_version,
            "delivery": self.delivery.public(), "keyframes": self.keyframes.public(),
            "routes": {k: v.public() for k, v in self.routes.items()},
            "created": self.created, "note": self.note,
            "cast": [c.public() for c in self.cast],
            "shots": [{**s.public(), "state": states[s.id]} for s in self.shots],
            "seconds": self.seconds, "shot_count": len(self.shots),
            "median_shot": self.median_shot, "dialogue_chars": self.dialogue_chars,
            # Derived, not `bool(active_video)`. An accepted job that was later
            # deleted leaves the string in place, and counting the string made
            # the progress line say "1/1 done" for a shot whose own state said
            # otherwise - the exact contradiction this whole design is against.
            "done": sum(1 for st in states.values() if st["phase"] == "done"),
        }


def _clean_line(text: str) -> str:
    """Dialogue length counts characters people read, not punctuation."""
    return re.sub(r"[\s，。！？、,.!?…「」“”\"']", "", text or "")


# -- derived state ------------------------------------------------------------
# Not persisted. A shot's progress is a function of its attempts and what the
# job store currently says about them, so storing it would mean storing a copy
# of something that changes underneath - and the copy would be the one the UI
# showed.

def shot_state(shot: Shot, jobs: dict) -> dict:
    """Where this shot has got to, computed against the job store."""

    def status_of(job_id: str) -> str:
        record = jobs.get(job_id)
        if record is None:
            return "missing"       # deleted from the library, or never existed
        return getattr(record, "status", "") or "unknown"

    def stage_state(stage: str) -> dict:
        attempts = shot.jobs_for(stage)
        active = shot.active_for(stage)
        live = [j for j in attempts if status_of(j) not in ("missing",)]
        return {
            "attempts": len(attempts),
            "missing": len(attempts) - len(live),
            "running": sum(1 for j in live if status_of(j) in ("queued", "running")),
            "done": sum(1 for j in live if status_of(j) == "done"),
            "failed": sum(1 for j in live if status_of(j) == "error"),
            "active": active,
            # An accepted job that has since been deleted is worse than none:
            # the shot claims to be finished and the file is gone.
            "active_missing": bool(active and status_of(active) == "missing"),
            # And "accepted" is not the same as "finished". The API only accepts
            # a completed job, but hand-edited JSONL and older records exist, so
            # the phase is computed from what the job store says now.
            "active_done": bool(active and status_of(active) == "done"),
        }

    stages = {s: stage_state(s) for s in STAGES}
    if stages["video"]["active_done"]:
        phase = "done"
    # "Review" outranks "running": if one take has finished, there is something
    # the user can act on, and that is the more useful thing to say even while
    # another attempt is still in the queue.
    elif stages["video"]["done"]:
        phase = "video_review"
    elif stages["video"]["running"]:
        phase = "video_running"
    elif stages["keyframe"]["active_done"]:
        phase = "keyframe_accepted"
    elif stages["keyframe"]["done"]:
        phase = "keyframe_review"
    elif stages["keyframe"]["running"]:
        phase = "keyframe_running"
    elif any(stages[s]["failed"] for s in stages):
        phase = "error"
    else:
        phase = "todo"
    return {"phase": phase, "stages": stages}


PHASE_ZH = {
    "todo": "還沒開始",
    "keyframe_running": "關鍵幀生成中",
    "keyframe_review": "關鍵幀待選",
    "keyframe_accepted": "關鍵幀已採用",
    "video_running": "影片生成中",
    "video_review": "影片待選",
    "done": "完成",
    "error": "上一次失敗",
}


# -- validation ---------------------------------------------------------------

@dataclass
class Finding:
    id: str
    level: str                  # BLOCK | WARN | INFO | GUIDE
    zh: str
    detail: str = ""
    kind: str = "INTEGRITY"     # INTEGRITY, or a claims.evidence_kind
    claim_id: str = ""
    shots: list[int] = field(default_factory=list)

    def public(self) -> dict:
        claim = claims.get(self.claim_id) if self.claim_id else None
        return {
            "id": self.id, "level": self.level, "zh": self.zh,
            "detail": self.detail, "kind": self.kind, "claim_id": self.claim_id,
            "badge": claim.badge if claim else "資料檢查",
            "claim": claim.public() if claim else None,
            "shots": self.shots,
        }


def _claim_finding(finding_id: str, claim_id: str, zh: str, detail: str = "",
                   shots: list[int] | None = None,
                   level: str | None = None) -> Finding:
    """A finding whose justification lives in claims.py, never restated here."""
    claim = claims.get(claim_id)
    return Finding(
        id=finding_id, level=level or (claim.policy if claim else claims.INFO),
        zh=zh, detail=detail, claim_id=claim_id,
        kind=claim.evidence_kind if claim else "INTEGRITY",
        shots=shots or [],
    )


def check_integrity(project: Project) -> list[Finding]:
    """Ways the record itself is broken. Never softened, never a matter of taste."""
    out: list[Finding] = []
    shots = project.shots

    keys = [c.key for c in project.cast]
    dupes = sorted({k for k in keys if keys.count(k) > 1})
    if dupes:
        out.append(Finding("cast-dupe", claims.BLOCK,
                           f"有 {len(dupes)} 個角色 key 重複。",
                           f"重複的：{'、'.join(dupes)}。鏡頭引用時會指到哪一個是不確定的。"))
    if any(not c.key or not c.name for c in project.cast):
        out.append(Finding("cast-blank", claims.BLOCK, "有角色沒有 key 或名字。"))
    bad_gender = sorted({c.gender for c in project.cast if c.gender not in GENDERS})
    if bad_gender:
        out.append(Finding("cast-gender", claims.BLOCK,
                           f"有角色的性別欄位不合法：{'、'.join(bad_gender)}",
                           "這個欄位決定提詞最前面的人數 tag（1girl／1boy／1other）。"))

    known = {c.key for c in project.cast}
    for shot in shots:
        n = shot.no
        if not (shot.seconds and shot.seconds > 0) or shot.seconds != shot.seconds:
            out.append(Finding("shot-seconds", claims.BLOCK,
                               f"第 {n} 顆的秒數不是正數。", shots=[n]))
        elif shot.seconds > MAX_SHOT_SECONDS:
            out.append(Finding("shot-seconds-huge", claims.BLOCK,
                               f"第 {n} 顆是 {shot.seconds} 秒，這比較像打錯了。",
                               shots=[n]))
        if shot.size not in SHOT_SIZES:
            out.append(Finding("shot-size", claims.BLOCK,
                               f"第 {n} 顆的景別「{shot.size}」不認得。", shots=[n]))
        if shot.method not in METHODS:
            out.append(Finding("shot-method", claims.BLOCK,
                               f"第 {n} 顆的生成方式「{shot.method}」不認得。", shots=[n]))
        missing = [w for w in shot.who if w not in known]
        if missing:
            out.append(Finding("shot-cast", claims.BLOCK,
                               f"第 {n} 顆引用了卡司裡沒有的角色。",
                               f"找不到：{'、'.join(missing)}。"
                               "這些鏡頭不會帶到觸發詞、鎖定服裝或 LoRA。", shots=[n]))
        if len(set(shot.who)) != len(shot.who):
            out.append(Finding("shot-who-dupe", claims.WARN,
                               f"第 {n} 顆的出場角色有重複。", shots=[n]))
        size = SHOT_SIZES.get(shot.size)
        if size and not size["people"] and shot.who:
            out.append(Finding(
                "shot-object-people", claims.BLOCK,
                f"第 {n} 顆是「{shot.size}」卻有出場角色。",
                f"「{shot.size}」會送出 `no humans`，跟人數 tag 直接互相矛盾——"
                "提詞會同時要求有人和沒人。要嘛換景別，要嘛把角色拿掉。", shots=[n]))
        if shot.dialogue and not shot.speaker:
            out.append(Finding("shot-no-speaker", claims.BLOCK,
                               f"第 {n} 顆有台詞卻沒指定誰在說。",
                               "同框兩個人的時候，沒有這個欄位就無法決定音訊要驅動誰。",
                               shots=[n]))
        if shot.speaker and shot.speaker not in shot.who:
            out.append(Finding("shot-speaker-absent", claims.BLOCK,
                               f"第 {n} 顆指定的說話者不在這顆的出場角色裡。", shots=[n]))
        method = METHODS.get(shot.method)
        if method and method.needs_endframe and not (
                shot.endframe_jobs or shot.active_endframe):
            out.append(_claim_finding(
                "shot-no-endframe", "wan22.flf_uses_i2v_weights",
                f"第 {n} 顆用首尾幀，但還沒有結束幀。",
                "首尾幀要兩張圖：起始幀和結束幀。只有一張就跑不了這個工作流。",
                shots=[n], level=claims.BLOCK))
        if method and method.needs_route and shot.method not in project.routes:
            out.append(Finding("shot-no-route", claims.BLOCK,
                               f"第 {n} 顆用「{method.zh}」，但專案沒有設定這條路線。",
                               "到第 0 步指定這個生成方式要用哪個模型。", shots=[n]))

    ids = [s.id for s in shots]
    if len(set(ids)) != len(ids) or any(not i for i in ids):
        out.append(Finding("shot-id", claims.BLOCK, "鏡頭的內部 id 有重複或空的。",
                           "這會讓生成紀錄掛到錯的鏡頭上。"))
    return out


def check_claims(project: Project, *, installed: set[str] | None = None
                 ) -> list[Finding]:
    """Findings about the world. Every one carries its evidence into claims.py.

    `installed` is the set of model ids on disk. `None` means the caller does
    not know and the download check is skipped; an *empty set* means nothing is
    installed, which is a real answer - conflating the two is a bug this module
    already shipped once.
    """
    out: list[Finding] = []
    shots = project.shots
    if not shots:
        return out

    # -- delivery shape
    ratio = project.delivery.ratio
    if ratio and abs(ratio - VERTICAL_RATIO) > VERTICAL_TOLERANCE:
        out.append(_claim_finding(
            "delivery-ratio", "format.vertical",
            f"交付尺寸 {project.delivery.width}×{project.delivery.height} "
            f"不是 9:16（比例 {ratio:.3f}，9:16 是 {VERTICAL_RATIO:.3f}）。",
            "只檢查「高比寬大」會讓 4:5 過關，所以這裡比的是實際比例。"))

    # -- keyframe size against the checkpoint's trained resolution
    px = project.keyframes.pixels
    if px and px < 1024 * 1024 * 0.45:
        out.append(_claim_finding(
            "keyframe-small", "sdxl.native_resolution",
            f"關鍵幀 {project.keyframes.width}×{project.keyframes.height} "
            f"只有原生面積的 {px / (1024 * 1024):.0%}。",
            "關鍵幀是整條線裡控制力最強的一步，在這裡省像素等於在源頭省畫質。"))

    # -- keyframe shape against the delivery shape. The video model does not
    # reframe for you: Wan I2V's output ratio follows the still it is handed.
    # So a 2:3 keyframe on a 9:16 timeline is not a rounding difference, it is
    # a crop of roughly a fifth of every frame, decided later and by hand.
    kf = project.keyframes
    kf_ratio = kf.width / kf.height if kf.height else 0.0
    if kf_ratio and project.delivery.ratio:
        drift = abs(kf_ratio - project.delivery.ratio)
        if drift > VERTICAL_TOLERANCE:
            lost = 1 - (project.delivery.ratio / kf_ratio) if kf_ratio > project.delivery.ratio \
                else 1 - (kf_ratio / project.delivery.ratio)
            out.append(_claim_finding(
                "keyframe-ratio", "wan.output_follows_input_ratio",
                f"關鍵幀 {kf.width}×{kf.height} 是 {kf_ratio:.3f}，"
                f"交付是 {project.delivery.ratio:.3f}。",
                f"影片會照關鍵幀的比例出來，所以每一顆都要再裁掉約 "
                f"{lost:.0%} 才放得進時間線。與其之後一顆一顆裁，"
                f"不如現在就把關鍵幀改成同比例。"))

    # -- a size the video node can actually take. Only the keyframe: the
    # delivery size is an export target that goes through upscaling in post and
    # never reaches the video node, so 1080x1920 is right and not a defect.
    if (kf.width % 16) or (kf.height % 16):
        out.append(_claim_finding(
            "size-align", "wan.vertical_sizes",
            f"關鍵幀 {kf.width}×{kf.height} 不是 16 的倍數。",
            "ComfyUI 的影片節點寬高都以 16 為步進。不對齊會被無聲調整，"
            "算出來的格數就跟你設定的對不上。"))

    # -- frame rate: per route, against the delivery timeline
    for method in sorted(project.methods_used):
        route = project.route(method)
        if route is None:
            continue
        landed = route.delivered_fps(project.delivery.fps)
        if landed and landed != project.delivery.fps:
            out.append(_claim_finding(
                "fps-route", "fps.single_native_rate",
                f"「{METHODS[method].zh}」這條路線落在 {landed}fps，"
                f"但時間線是 {project.delivery.fps}fps。",
                f"{route.model_id} 原生 {route.native_fps}fps。"
                "在第 0 步替這條路線選一個收尾方式（原生／補幀／retime），"
                "否則會在後期變成非整數倍的轉換。", level=claims.WARN))
        if route.finish.mode == "retime" and not route.finish.retime_audio:
            out.append(_claim_finding(
                "retime-audio", "fps.retime_audio",
                f"「{METHODS[method].zh}」設定成 retime，但沒有勾聲音一起處理。",
                "畫面被拉長或壓縮之後，沒跟著處理的聲音就會失去同步。",
                level=claims.WARN))

    # -- clip length against what one pass can produce
    for method in sorted(project.methods_used):
        route = project.route(method)
        if route is None or not route.clip_seconds:
            continue
        over = [s.no for s in shots
                if s.method == method and s.seconds > route.clip_seconds]
        if over:
            out.append(_claim_finding(
                "over-clip", "video.clip_length_is_spec",
                f"{len(over)} 顆鏡頭比 {route.model_id} 單次能生成的長度還長"
                f"（{route.clip_seconds} 秒）。",
                "要嘛把秒數改短，要嘛在 ComfyUI 裡把工作流的幀數調高，"
                "要嘛拆成兩顆。（幀數是可以改的，這裡比的是目前設定的預設值。）",
                shots=over, level=claims.WARN))

    long_shots = [s.no for s in shots if s.seconds > SHOT_LONG_HINT]
    if long_shots:
        out.append(_claim_finding(
            "long-shots", "video.drift_with_length",
            f"{len(long_shots)} 顆鏡頭超過 {SHOT_LONG_HINT} 秒。",
            "社群普遍回報片段越長越容易漂移，但本專案沒有量過，"
            f"所以 {SHOT_LONG_HINT} 秒只是一個提醒用的門檻，不是實測的閾值。",
            shots=long_shots))

    # -- format conventions
    if project.median_shot > SHOT_MEDIAN_REFERENCE * 1.6:
        out.append(_claim_finding(
            "slow-pace", "format.shot_median",
            f"鏡頭中位數 {project.median_shot} 秒，"
            f"參考值是 {SHOT_MEDIAN_REFERENCE} 秒。",
            "那個參考值是某一部成片的剪輯統計，不是規定。慢是可以的，但要是刻意的。"))
    long_lines = [s.no for s in shots
                  if len(_clean_line(s.dialogue)) > DIALOGUE_MAX_CHARS]
    if long_lines:
        out.append(_claim_finding(
            "long-dialogue", "format.line_length",
            f"{len(long_lines)} 句台詞超過 {DIALOGUE_MAX_CHARS} 個字。",
            "標點不算在內。", shots=long_lines))
    chars = project.dialogue_chars
    if chars > EPISODE_DIALOGUE_CHARS[1] * 1.5:
        out.append(_claim_finding(
            "wordy", "format.line_length",
            f"整集台詞 {chars} 字，慣例是 {'-'.join(map(str, EPISODE_DIALOGUE_CHARS))} 字。"))
    first = shots[0]
    if not (first.action or first.dialogue):
        out.append(_claim_finding(
            "no-hook", "format.hook", "第一顆鏡頭是空的。",
            "這顆目前既沒有動作也沒有台詞。", shots=[first.no], level=claims.WARN))
    lo_s, hi_s = EPISODE_SECONDS
    if project.seconds and not (lo_s * 0.5 <= project.seconds <= hi_s * 1.5):
        out.append(_claim_finding(
            "episode-length", "format.episode_length",
            f"整集 {project.seconds} 秒，慣例是 {lo_s}-{hi_s} 秒。"))

    # -- consistency strategy: offered, never assumed
    used = {k for s in shots for k in s.who}
    styled = [c for c in project.cast if c.key in used and (c.lora or c.trigger)]
    bare = [c.name for c in project.cast if c.key in used
            and not c.lora and not c.trigger]
    if bare:
        out.append(_claim_finding(
            "no-strategy", "consistency.lora",
            f"{len(bare)} 位角色既沒有觸發詞也沒有 LoRA。",
            f"這份記錄裡，{'、'.join(bare)} 沒有任何共用的外觀描述，"
            "所以每顆鏡頭送出去的提詞只有景別、場景和動作。"
            "角色 LoRA、觸發詞、參考圖控制都是可以用的方法——"
            "本專案沒有比較過哪個好，但這份記錄裡一個都沒有。"
            "（如果你是在 app 外面用別的方式控一致性，這條可以忽略。）",
            level=claims.WARN))
    # On an anime checkpoint a danbooru character tag is a real handle: the
    # model was captioned with it and knows the face. A photoreal checkpoint has
    # no such vocabulary, so a trigger word alone is just an unfamiliar token -
    # the only thing that pins the face is a LoRA. Which makes this the point
    # where a photoreal project has to go and train one.
    if dialect_for(project.keyframes.model_id) == "natural":
        trigger_only = [c.name for c in project.cast
                        if c.key in used and c.trigger and not c.lora]
        if trigger_only:
            out.append(_claim_finding(
                "photoreal-no-lora", "consistency.photoreal_needs_lora",
                f"底模是寫實的，但 {len(trigger_only)} 位角色只有觸發詞、沒有 LoRA。",
                f"{'、'.join(trigger_only)} 的觸發詞在寫實底模上不會叫出固定的臉 —— "
                "動漫底模的標註裡有角色標籤，寫實底模沒有。"
                "到「訓練角色」分頁做一個角色 LoRA，"
                "或改用參考圖控制；不然每顆鏡頭都會是不同的人。",
                level=claims.WARN))

    # Two character LoRAs on one still is the case the research is about, and
    # the trigger is the LoRAs, not the head count: two people where only one
    # has a LoRA is a different situation entirely.
    for shot in shots:
        people = [p for p in (project.character(k) for k in shot.who) if p]
        with_lora = [p for p in people if p.lora]
        if len(with_lora) < 2:
            continue
        out.append(_claim_finding(
            "multi-lora", "consistency.multi_lora_bleed",
            f"第 {shot.no} 顆鏡頭同時要載入 {len(with_lora)} 個角色 LoRA"
            f"（{'、'.join(p.name for p in with_lora)}）。",
            "普通的 LoRA 載入是**改整個模型**，不會把 A 的 LoRA 限制在 A 身上，"
            "所以兩人的臉、髮型或服裝可能互相混合，也可能其中一個失去辨識度。"
            "**這不是一定會發生。** 可以試的順序："
            "①把這顆拆成近景／反應／過肩，讓兩人不同框（現在就做得到，也最有效）；"
            "②先生構圖，再遮住一個人、只掛一個 LoRA 分別重繪臉；"
            "③把各自的 LoRA 強度往下調 —— 但**沒有可靠的安全值**，"
            "0.7 這種數字沒有依據，要自己試。",
            level=claims.WARN))

    # A shot with no motion prompt still generates - the fallback sees to that -
    # but it is being driven by a description of a frozen instant, which is not
    # the same instruction. Said as INFO, and without claiming the clip will
    # come out static: an I2V model can find movement in the picture itself.
    silent = [s.no for s in shots if not (s.motion or "").strip() and (s.action or "").strip()]
    if silent:
        out.append(_claim_finding(
            "no-motion", "video.motion_prompt",
            f"{len(silent)} 顆鏡頭還沒填「影片怎麼動」。",
            f"第 {'、'.join(str(n) for n in silent[:8])} 顆"
            + ("…" if len(silent) > 8 else "")
            + "。目前會暫時拿「關鍵幀姿勢」那一欄當影片指令 —— "
            "那一欄寫的是**凝固的一瞬間**，不是時間上的變化。"
            "要指定走路、伸手、轉身或運鏡，就填「影片怎麼動」。",
            level=claims.INFO))

    no_costume = [c.name for c in project.cast if c.key in used and not c.costume]
    if no_costume and styled:
        out.append(_claim_finding(
            "no-costume", "consistency.lora",
            f"{len(no_costume)} 位角色沒有鎖定服裝。",
            "把服裝描述集中保存一份、每顆鏡頭原封不動貼，"
            "可以避免不同鏡頭之間出現文字上的差異——這是資料一致性，不是畫質主張。"))

    # -- audio ordering
    talking = [s.no for s in shots if s.dialogue and s.method != "s2v"]
    if talking:
        out.append(_claim_finding(
            "dialogue-not-s2v", "s2v.vs_postsync",
            f"{len(talking)} 顆有台詞的鏡頭不是用音訊驅動。",
            "這些之後要另外補口型（InfiniteTalk／LatentSync）。"
            "兩條路的輸入和返工成本不同，成品差異本專案沒有比較過。",
            shots=talking))

    # -- can this app actually run the route, or only download its files?
    # A `files_only` model is one this app has no validated graph for, so it is
    # generated in ComfyUI by hand. Planning twenty dialogue shots and finding
    # that out at generation time is exactly the trap this check exists to close.
    for method in sorted(project.methods_used):
        route = project.route(method)
        model = registry.get(route.model_id) if route else None
        if model and not model.runnable:
            out.append(Finding(
                f"not-runnable-{method}", claims.WARN,
                f"「{METHODS[method].zh}」用的 {model.label.split('—')[0].strip()} "
                "沒辦法從這個 app 生成。",
                "這個模型只下載檔案，本頁沒有驗證過的工作流可以跑它 —— "
                "要到 ComfyUI（:8188）用官方範本手動生成，再回來把結果掛到鏡頭上。"
                "先知道總比排完二十顆才發現好。",
                kind="INTEGRITY"))

    # -- methods this app has no graph for, whatever model they point at.
    # A first/last-frame shot needs two pictures fed to a different graph, and
    # this app builds neither. Generating it anyway would send only the first
    # frame through the ordinary image-to-video path - the user would get a
    # video, it would not be the one they asked for, and nothing would say so.
    flf = [s.no for s in shots if METHODS.get(s.method, METHODS["i2v"]).needs_endframe]
    if flf:
        out.append(Finding(
            "no-flf-graph", claims.WARN,
            f"{len(flf)} 顆鏡頭用「首尾幀」，這個 app 還不能生成這種。",
            "首尾幀要把兩張圖送進另一種工作流，本頁沒有 —— "
            "生成的時候會直接擋下來，不會偷偷只拿第一張去生成一段普通的圖生影片。"
            "現在的做法：改成「圖生影片」，或到 ComfyUI 用官方首尾幀範本手動生成，"
            "再把結果掛回這顆鏡頭。",
            shots=flf, kind="INTEGRITY"))

    # -- a route pointing at a model that has no such mode. Different from
    # "not downloaded" and from "no graph here": this one can never work, no
    # matter what you install or import, because the model does not do that.
    for method in sorted(project.methods_used):
        route = project.route(method)
        model = registry.get(route.model_id) if route else None
        if model is None or not model.methods or method in model.methods:
            continue
        can = "、".join(METHODS[m].zh for m in model.methods if m in METHODS)
        out.append(Finding(
            f"wrong-mode-{method}", claims.BLOCK,
            f"「{METHODS[method].zh}」指到 {model.label.split('—')[0].strip()}，"
            f"但這個模型沒有這種模式。",
            f"它只能做：{can}。"
            "在第 0 步把這條路線換成別的模型，或者把用到這種鏡頭的生成方式改掉 —— "
            "不然生成的時候會失敗，或是生出跟你要的不一樣的東西。",
            kind="INTEGRITY"))

    # -- models on disk
    if installed is not None:
        for method in sorted(project.methods_used):
            route = project.route(method)
            if route is None or route.model_id in installed:
                continue
            model = registry.get(route.model_id)
            out.append(Finding(
                f"missing-{method}", claims.BLOCK,
                f"「{METHODS[method].zh}」要用的 "
                f"{model.label if model else route.model_id} 還沒下載。",
                ("下面「整集」那一格有這個模型的下載按鈕"
                 + (f"（{model.download_bytes / 1e9:.1f}GB）" if model else "")
                 + "，按下去就會開始下載，不用離開這一頁。"),
                kind="INTEGRITY"))
    return out


ORDER = {claims.BLOCK: 0, claims.WARN: 1, claims.INFO: 2, claims.GUIDE: 3}


def check(project: Project, *, installed: set[str] | None = None) -> list[Finding]:
    """Integrity first, always: a broken record makes every other check noise."""
    found = check_integrity(project) + check_claims(project, installed=installed)
    found.sort(key=lambda f: (ORDER.get(f.level, 9), f.kind != "INTEGRITY"))
    return found


def summary(findings: list[Finding]) -> dict:
    counts = {p: sum(1 for f in findings if f.level == p) for p in claims.POLICIES}
    integrity = sum(1 for f in findings if f.kind == "INTEGRITY")
    if counts[claims.BLOCK]:
        line, level = f"有 {counts[claims.BLOCK]} 個一定要先修的問題", "high"
    elif counts[claims.WARN]:
        line, level = f"有 {counts[claims.WARN]} 個值得看一下的地方", "warn"
    elif findings:
        line, level = "沒有擋路的問題，有幾個提醒", "info"
    else:
        line, level = "分鏡表看起來沒問題", "ok"
    return {"level": level, "line": line, "counts": counts,
            "integrity": integrity, "claims": len(findings) - integrity,
            "findings": [f.public() for f in findings]}


# -- building one shot's prompt -----------------------------------------------

def count_tag(people: list[Character], *, dialect: str = "danbooru") -> str:
    """The count tag that opens the prompt, derived from who is actually in it.

    The first version hard-coded `1girl` / `2girls`, so an all-male shot opened
    with a female count tag and every male character spent the rest of the
    prompt arguing with it. Mixed casts get one tag per gender, which is how
    danbooru captions them.

    `dialect` picks the spelling, not the meaning. A photoreal checkpoint has
    never seen the token `1girl`; it was captioned in English sentences, so it
    gets "one adult woman" for the same cast.
    """
    if not people:
        return ""
    photo = dialect == "natural"
    order = ["female", "male", "other"]
    buckets: dict[str, int] = {}
    for who in people:
        gender = who.gender if who.gender in GENDERS else "other"
        buckets[gender] = buckets.get(gender, 0) + 1
    parts = []
    for gender in order:
        n = buckets.get(gender, 0)
        if not n:
            continue
        spec = GENDERS[gender]
        one, many = ("photo_one", "photo_many") if photo else ("one", "many")
        parts.append(spec[one] if n == 1 else spec[many].format(n=n))
    return ", ".join(parts)


def dialect_for(model_id: str) -> str:
    """Which vocabulary this keyframe checkpoint was captioned in.

    Read off the image catalogue rather than stored on the project: the answer
    is a property of the checkpoint, and a stored copy would go stale the moment
    the keyframe model is changed.
    """
    import images

    model = images.get(model_id) or images.resolve(model_id, [])
    return model.tag_style if model else "danbooru"


def video_prompt(shot: Shot) -> dict:
    """What to tell the video model, and whether it is really a motion prompt.

    `motion` when it is filled, `action` when it is not. The fallback exists for
    backwards compatibility, not as a recommendation: a v2 project's `action`
    was written to describe a still, and handing a still's description to a
    video model is how you get a clip that holds the pose.

    `extra` is deliberately not included. It is the keyframe's supplement -
    light, expression, props - and it was being appended to the video prompt
    too, which meant the split only went half way.
    """
    text = (shot.motion or "").strip()
    if text:
        return {"prompt": text, "from": "motion", "fallback": False}
    return {"prompt": (shot.action or "").strip(), "from": "action",
            "fallback": bool((shot.action or "").strip())}


def keyframe_prompt(project: Project, shot: Shot) -> dict:
    """Compose the still-image prompt for one shot.

    The order is the one danbooru captions use - count, character, then the
    looser description. That the front of a prompt carries more weight is a
    common belief and is *not* asserted here; the order is followed because it
    matches how the training captions were written, which is checkable.
    """
    import promptmerge

    size = SHOT_SIZES.get(shot.size, SHOT_SIZES["近景"])
    people = [p for p in (project.character(k) for k in shot.who) if p]
    dialect = dialect_for(project.keyframes.model_id)
    bits: list[str] = []

    # A shot size that emits `no humans` never gets a cast; check_integrity
    # blocks that combination, and this is the second line of defence so a
    # contradictory prompt cannot be built even if the record slipped through.
    if size["people"]:
        count = count_tag(people, dialect=dialect)
        if count:
            bits.append(count)
        for who in people:
            if who.trigger:
                bits.append(who.trigger)
            if who.costume:
                bits.append(who.costume)

    # The framing, said the way this checkpoint was captioned. `cowboy shot` is
    # a booru word: at a photoreal model it is closer to noise than to a
    # framing instruction.
    bits.append(size["photo"] if dialect == "natural" else size["tag"])
    for extra in (shot.scene, shot.action, shot.extra):
        if extra:
            bits.append(extra)

    pieces: list[str] = []
    for chunk in bits:
        pieces.extend(promptmerge.split_tags(chunk))
    return {
        "prompt": ", ".join(promptmerge.dedupe(pieces)),
        "dialect": dialect,
        "loras": [w.lora for w in people if w.lora],
        "model": project.keyframes.model_id,
        "width": project.keyframes.width, "height": project.keyframes.height,
        "style": project.keyframes.style_id,
    }


def shot_plan(project: Project, shot: Shot) -> dict:
    """What to do for this shot, in order, each step saying which claim it rests on."""
    method = METHODS.get(shot.method, METHODS["i2v"])
    route = project.route(shot.method)
    steps: list[dict] = []

    if method.needs_audio or shot.dialogue:
        steps.append({"do": "先做音檔", "claim_id": "s2v.audio_first"})
    steps.append({"do": f"生關鍵幀（{project.keyframes.width}×{project.keyframes.height}）",
                  "claim_id": "workflow.fix_stills_first"})
    if method.needs_endframe:
        steps.append({"do": "再生一張結束幀",
                      "claim_id": "wan22.flf_uses_i2v_weights"})
    steps.append({"do": f"{method.zh} → {shot.seconds} 秒",
                  "claim_id": method.claim_id})

    for step in steps:
        claim = claims.get(step.get("claim_id") or "")
        step["why"] = claim.text if claim else ""
        step["badge"] = claim.badge if claim else ""
    fps = route.native_fps if route else project.delivery.fps
    return {"no": shot.no, "id": shot.id, "method": shot.method, "steps": steps,
            "frames": int(round(shot.seconds * fps)) if fps else 0,
            "route": route.public() if route else None,
            "method_why": method.why}


# -- the store ----------------------------------------------------------------

def default_routes() -> dict[str, Route]:
    return {m: Route(model_id) for m, model_id in DEFAULT_ROUTE_MODEL.items()}


def _route_from(raw: dict) -> Route:
    finish = raw.get("finish") or {}
    return Route(
        model_id=str(raw.get("model_id") or ""),
        finish=FinishPolicy(mode=str(finish.get("mode") or "native"),
                            factor=int(finish.get("factor") or 1),
                            retime_audio=bool(finish.get("retime_audio"))),
    )


def _migrate_v2(raw: dict) -> dict:
    """Version 2 had one `action` meaning both the pose and the movement.

    The old value is left in `action` and `motion` starts empty - deliberately
    not copied. We do not know whether a given v2 shot was written as a frozen
    pose or as a movement, and copying it would present a guess as a completed
    migration. The video step falls back to `action` at read time instead, so
    nothing breaks and nothing is invented.
    """
    shots = []
    for shot in raw.get("shots") or []:
        shots.append({**shot, "motion": shot.get("motion") or ""})
    return {"shots": shots}


def _migrate_v1(raw: dict) -> dict:
    """Version 1 stored one `model` plus `fps` for the whole episode.

    That could not describe a project with dialogue, because S2V is a different
    checkpoint - so the old value becomes the i2v route and the rest take their
    defaults. The v1 keys are read here and never written back: two sources of
    truth on disk is how they start disagreeing.
    """
    routes = default_routes()
    if raw.get("model"):
        routes["i2v"] = Route(str(raw["model"]))
    return {
        "delivery": {"width": int(raw.get("deliver_width") or 1080),
                     "height": int(raw.get("deliver_height") or 1920),
                     "fps": int(raw.get("fps") or 24)},
        "keyframes": {"model_id": raw.get("image_model") or "noobai",
                      "width": int(raw.get("width") or 832),
                      "height": int(raw.get("height") or 1216),
                      "style_id": raw.get("style") or ""},
        "routes": {k: {"model_id": v.model_id} for k, v in routes.items()},
    }


class ProjectStore:
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
                version = int(raw.get("schema_version") or 1)
                if version < 2:
                    raw = {**raw, **_migrate_v1(raw)}
                if version < 3:
                    raw = {**raw, **_migrate_v2(raw)}
                delivery = raw.get("delivery") or {}
                keyframes = raw.get("keyframes") or {}
                project = Project(
                    id=raw["id"], title=raw.get("title", ""),
                    delivery=DeliverySpec(
                        width=int(delivery.get("width") or 1080),
                        height=int(delivery.get("height") or 1920),
                        fps=int(delivery.get("fps") or 24),
                        fit=str(delivery.get("fit") or "")),
                    keyframes=KeyframeProfile(
                        model_id=keyframes.get("model_id") or "noobai",
                        width=int(keyframes.get("width") or 832),
                        height=int(keyframes.get("height") or 1216),
                        style_id=keyframes.get("style_id") or ""),
                    routes={k: _route_from(v)
                            for k, v in (raw.get("routes") or {}).items()},
                    created=raw.get("created", time.time()), note=raw.get("note", ""),
                    cast=[Character(**c) for c in raw.get("cast", [])],
                    shots=[Shot(**s) for s in raw.get("shots", [])],
                )
                if not project.routes:
                    project.routes = default_routes()
                normalise(project)
                self.items[project.id] = project
            except Exception:
                continue          # one bad line must not lose the rest

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        rows = [json.dumps({
            "id": p.id, "title": p.title, "schema_version": SCHEMA_VERSION,
            "delivery": {"width": p.delivery.width, "height": p.delivery.height,
                         "fps": p.delivery.fps},
            "keyframes": {"model_id": p.keyframes.model_id,
                          "width": p.keyframes.width, "height": p.keyframes.height,
                          "style_id": p.keyframes.style_id},
            "routes": {k: {"model_id": v.model_id, "finish": v.finish.public()}
                       for k, v in p.routes.items()},
            "created": p.created, "note": p.note,
            "cast": [c.public() for c in p.cast],
            "shots": [s.public() for s in p.shots],
        }, ensure_ascii=False) for p in self.items.values()]
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text("".join(r + "\n" for r in rows), encoding="utf-8")
        tmp.replace(self.path)

    def create(self, title: str) -> Project:
        project = Project(id=uuid.uuid4().hex[:10], title=title or "未命名短劇",
                          routes=default_routes())
        self.items[project.id] = project
        return project

    def get(self, project_id: str) -> Project | None:
        return self.items.get(project_id)

    def delete(self, project_id: str) -> bool:
        return self.items.pop(project_id, None) is not None

    def list(self) -> list[Project]:
        return sorted(self.items.values(), key=lambda p: -p.created)


def normalise(project: Project) -> None:
    """Give every shot a stable id and a display number. Idempotent."""
    for i, shot in enumerate(project.shots, 1):
        if not shot.id:
            shot.id = uuid.uuid4().hex[:8]
        shot.no = i


def public() -> dict:
    """The static tables the UI renders its pickers and its guide from."""
    return {
        "sizes": SHOT_SIZES,
        "genders": GENDERS,
        "methods": {k: {**asdict(v), "claim": (claims.get(v.claim_id).public()
                                               if claims.get(v.claim_id) else None)}
                    for k, v in METHODS.items()},
        "default_routes": DEFAULT_ROUTE_MODEL,
        "phases": PHASE_ZH,
        "stages": list(STAGES),
        "format": {
            "episode_seconds": list(EPISODE_SECONDS),
            "shot_median": SHOT_MEDIAN_REFERENCE,
            "shot_long_hint": SHOT_LONG_HINT,
            "dialogue_max": DIALOGUE_MAX_CHARS,
            "episode_dialogue": list(EPISODE_DIALOGUE_CHARS),
            "hook_seconds": HOOK_SECONDS,
            "vertical_ratio": round(VERTICAL_RATIO, 4),
        },
        "claims": claims.public(),
    }

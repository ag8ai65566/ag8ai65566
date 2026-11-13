"""Make a picture again by trying, scoring and correcting - automatically.

What it does
------------
The loop the research projects run (WeavePrompt, Prompt Studio's agent, ARPO,
Idea2Img - see README), with this app's own parts:

    generate a few candidates  ->  score each against the original
    ->  keep the best so far   ->  correct the prompt (and the denoise)
    ->  again, until the score is good enough, stops improving, or the
        round limit is reached

Scoring has three parts, because "alike" means three different things:

* **content** - what is in the picture: the cosine of the tagger's full score
  vectors (reverse.similarity).
* **style** - how it is painted: palette, saturation, line density
  (reverse.style_signature).
* **structure** - where things are: a small blurred greyscale and colour
  thumbnail compared pixel by pixel. The only one of the three that can tell
  "the same scene" from "a similar scene", and the one prompt-only methods
  cannot move - ARPO's own table has its layout-sensitive score (DINO) stuck
  around 0.5 while its content score passes 0.8.

Correction is deliberately plain: tags the original has and the attempt lacks
are added to the prompt, tags the attempt has and the original lacks go to the
negative (unless the model has no negative), and when the layout is off the
denoise is lowered so more of the original survives. No language model is in
the loop - it is the part of the research systems this app does not have, and
the page says so rather than pretending.

The benchmark
-------------
The same loop twice, from the same starting prompt: once from an empty canvas
(prompt only - what every research method above does) and once starting from
the original picture (image-to-image). The page shows both curves round by
round, so "does starting from the picture really help" is answered with this
user's own numbers rather than with the claim in the README.

The loop itself never touches ComfyUI: `drive` is given the three operations
it needs (submit, wait, score), so it can be tested without a GPU.
"""

from __future__ import annotations

import asyncio
import json
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

WEIGHTS = {"content": 0.4, "style": 0.3, "structure": 0.3}
PLATEAU = 0.01          # a round must beat the best by this much to count
PLATEAU_ROUNDS = 2      # ... and failing that this many times in a row stops
MAX_ADD = 6             # tags added per correction, so one round cannot swamp the prompt
DENOISE_MIN, DENOISE_MAX, DENOISE_STEP = 0.3, 0.7, 0.05


# -- scoring -------------------------------------------------------------------


def structure_signature(picture):
    """Where things are: a 32x32 blurred greyscale and an 8x8 colour thumbnail."""
    import numpy as np
    from PIL import ImageFilter

    rgb = picture.convert("RGB")
    grey = rgb.convert("L").filter(ImageFilter.GaussianBlur(2)).resize((32, 32))
    colour = rgb.resize((8, 8))
    return (np.asarray(grey, dtype=np.float32) / 255.0,
            np.asarray(colour, dtype=np.float32) / 255.0)


def structure_similarity(a, b) -> float:
    """0..1. Both pictures are squashed to the same grid, so aspect differences count."""
    import numpy as np

    (ga, ca), (gb, cb) = a, b
    grey = 1.0 - float(np.abs(ga - gb).mean()) * 2.5
    colour = 1.0 - float(np.abs(ca - cb).mean()) * 2.5
    # Correlation of the greyscale layout: "the dark shape is in the same
    # place" even when the overall brightness differs.
    da, db = ga - ga.mean(), gb - gb.mean()
    denom = float(np.sqrt((da * da).sum() * (db * db).sum()))
    if denom > 1e-6:
        corr = float((da * db).sum() / denom)
    else:
        # At least one side is a flat field, so there is no layout to
        # correlate. Two flat fields of the same tone are the same layout;
        # anything else is not.
        corr = 1.0 if float(np.abs(ga - gb).mean()) < 0.02 else 0.0
    parts = [max(0.0, grey), max(0.0, colour), max(0.0, corr)]
    return max(0.0, min(1.0, 0.35 * parts[0] + 0.25 * parts[1] + 0.4 * parts[2]))


def overall(content: float, style: float, structure: float) -> float:
    return round(WEIGHTS["content"] * content + WEIGHTS["style"] * style
                 + WEIGHTS["structure"] * structure, 4)


# -- correcting ----------------------------------------------------------------


def _split(text: str) -> list[str]:
    return [t.strip() for t in str(text or "").split(",") if t.strip()]


def refine(prompt: str, negative: str, missing: list[str], extra: list[str], *,
           zero_negative: bool, protected: str = "") -> tuple[str, str, list[str]]:
    """The next prompt and negative, and what changed, in words.

    `protected` is the starting prompt: a tag that was asked for is never
    pushed into the negative just because one attempt overdid it.
    """
    have = {t.lower() for t in _split(prompt)}
    keep = {t.lower() for t in _split(protected)} | have
    added = [t for t in missing if t.lower() not in have][:MAX_ADD]
    changes = []
    if added:
        prompt = ", ".join(_split(prompt) + added)
        changes.append("提詞加上：" + "、".join(added))
    if not zero_negative:
        neg_have = {t.lower() for t in _split(negative)}
        banned = [t for t in extra if t.lower() not in keep and t.lower() not in neg_have][:MAX_ADD]
        if banned:
            negative = ", ".join(_split(negative) + banned)
            changes.append("負面提詞加上：" + "、".join(banned))
    return prompt, negative, changes


def next_denoise(current: float | None, structure: float, content: float) -> tuple[float | None, str]:
    """Less redrawing when the layout drifted; more when the layout is fine but the content is not."""
    if current is None:
        return None, ""
    if structure < 0.75 and current > DENOISE_MIN:
        value = round(max(DENOISE_MIN, current - DENOISE_STEP), 2)
        return value, f"構圖跑掉了，重畫強度降到 {value}"
    if structure >= 0.85 and content < 0.6 and current < DENOISE_MAX:
        value = round(min(DENOISE_MAX, current + DENOISE_STEP), 2)
        return value, f"構圖對了但內容不對，重畫強度升到 {value}"
    return current, ""


# -- state ---------------------------------------------------------------------


@dataclass
class Attempt:
    job: str
    output: str = ""
    score: float = 0.0
    content: float = 0.0
    style: float = 0.0
    structure: float = 0.0
    missing: list = field(default_factory=list)
    extra: list = field(default_factory=list)
    error: str = ""


@dataclass
class Round:
    n: int
    prompt: str
    negative: str
    denoise: float | None
    attempts: list = field(default_factory=list)
    best: float = 0.0
    changes: list = field(default_factory=list)   # what was changed *after* this round


@dataclass
class Arm:
    key: str                 # "approach" | "prompt" | "original"
    label: str
    start_from_original: bool
    prompt: str
    negative: str
    denoise: float | None
    rounds: list = field(default_factory=list)
    best_score: float = 0.0
    best_job: str = ""
    best_round: int = 0
    status: str = "waiting"  # waiting | running | done | stopped | error
    stop_reason: str = ""


@dataclass
class Run:
    id: str
    created: float
    original: str            # staged file name of the picture being copied
    base: dict               # the image tab's payload: model, size, LoRAs, steps...
    max_rounds: int
    per_round: int
    target: float
    zero_negative: bool
    arms: list = field(default_factory=list)
    status: str = "running"
    message: str = ""
    benchmark: bool = False

    def public(self) -> dict:
        data = asdict(self)
        data.pop("base", None)
        data["model"] = self.base.get("model", "")
        return data


def new_run(*, original: str, base: dict, prompt: str, negative: str, max_rounds: int,
            per_round: int, target: float, start_from_original: bool, denoise: float,
            benchmark: bool, zero_negative: bool) -> Run:
    run = Run(id=uuid.uuid4().hex[:10], created=time.time(), original=original, base=dict(base),
              max_rounds=max(1, min(int(max_rounds), 12)),
              per_round=max(1, min(int(per_round), 4)),
              target=max(0.5, min(float(target), 0.99)),
              zero_negative=zero_negative, benchmark=benchmark)
    denoise = max(DENOISE_MIN, min(float(denoise), 0.9))
    if benchmark:
        run.arms = [
            Arm("prompt", "只用提詞", False, prompt, negative, None),
            Arm("original", "提詞＋從原圖開始", True, prompt, negative, denoise),
        ]
    else:
        run.arms = [Arm("approach", "從原圖開始" if start_from_original else "只用提詞",
                        start_from_original, prompt, negative,
                        denoise if start_from_original else None)]
    return run


def stop_reason(arm: Arm, target: float, max_rounds: int) -> str:
    if arm.best_score >= target:
        return f"達標（{arm.best_score:.2f} ≥ {target:.2f}）"
    if len(arm.rounds) >= max_rounds:
        return f"跑滿 {max_rounds} 輪"
    if len(arm.rounds) > PLATEAU_ROUNDS:
        before = max(r.best for r in arm.rounds[:-PLATEAU_ROUNDS])
        if all(r.best < before + PLATEAU for r in arm.rounds[-PLATEAU_ROUNDS:]):
            return f"連續 {PLATEAU_ROUNDS} 輪沒有進步，再跑也只是花時間"
    return ""


async def drive(run: Run, *, submit, wait, score, cancelled, save=lambda: None) -> None:
    """Run every arm of `run` to the end.

    submit(arm, round) -> list[job_id]       queue the round's candidates
    wait(job_ids) -> dict[job_id, (status, output, message)]
    score(output) -> dict(content, style, structure, missing, extra)
    cancelled() -> bool                       the user pressed stop
    """
    try:
        for arm in run.arms:
            arm.status = "running"
            save()
            while True:
                if cancelled():
                    arm.status, arm.stop_reason = "stopped", "你按了停止"
                    break
                rnd = Round(n=len(arm.rounds) + 1, prompt=arm.prompt, negative=arm.negative,
                            denoise=arm.denoise)
                arm.rounds.append(rnd)
                run.message = f"{arm.label}：第 {rnd.n} 輪，生 {run.per_round} 張…"
                save()
                jobs = await submit(arm, rnd)
                rnd.attempts = [Attempt(job=j) for j in jobs]
                save()
                done = await wait(jobs)
                run.message = f"{arm.label}：第 {rnd.n} 輪，評分中…"
                for attempt in rnd.attempts:
                    status, output, message = done.get(attempt.job, ("error", "", "沒有結果"))
                    attempt.output = output
                    if status != "done" or not output:
                        attempt.error = message or status
                        continue
                    s = await score(output)
                    attempt.content, attempt.style, attempt.structure = (
                        round(s["content"], 3), round(s["style"], 3), round(s["structure"], 3))
                    attempt.score = overall(s["content"], s["style"], s["structure"])
                    attempt.missing, attempt.extra = s.get("missing", []), s.get("extra", [])
                scored = [a for a in rnd.attempts if not a.error]
                if not scored:
                    arm.status = "error"
                    arm.stop_reason = ("這一輪一張都沒生出來：" +
                                       (rnd.attempts[0].error if rnd.attempts else "沒有送出"))
                    break
                top = max(scored, key=lambda a: a.score)
                rnd.best = top.score
                if top.score > arm.best_score:
                    arm.best_score, arm.best_job, arm.best_round = top.score, top.job, rnd.n
                save()
                reason = stop_reason(arm, run.target, run.max_rounds)
                if reason:
                    arm.status, arm.stop_reason = "done", reason
                    break
                # Correct from the best attempt so far, not merely this round's:
                # a bad round must not drag the prompt somewhere worse.
                best_attempt = next(a for r in arm.rounds for a in r.attempts if a.job == arm.best_job)
                arm.prompt, arm.negative, changes = refine(
                    arm.prompt, arm.negative, best_attempt.missing, best_attempt.extra,
                    zero_negative=run.zero_negative, protected=arm.rounds[0].prompt)
                arm.denoise, note = next_denoise(arm.denoise, best_attempt.structure,
                                                 best_attempt.content)
                rnd.changes = changes + ([note] if note else [])
                if not rnd.changes:
                    rnd.changes = ["沒有可以改的標籤了，換種子再試"]
                save()
        run.status = "stopped" if any(a.status == "stopped" for a in run.arms) else "done"
        run.message = ""
    except Exception as exc:  # noqa: BLE001 - reported on the page, not a 500
        run.status, run.message = "error", f"{type(exc).__name__}: {exc}"
        for arm in run.arms:
            if arm.status == "running":
                arm.status = "error"
    finally:
        save()


class Store:
    """The last few runs, on disk so a restarted app can still show them."""

    def __init__(self, path: Path, keep: int = 12) -> None:
        self.path, self.keep = path, keep
        self.runs: dict[str, Run] = {}

    def load(self) -> None:
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return
        for item in raw if isinstance(raw, list) else []:
            try:
                arms = [Arm(**{**a, "rounds": [Round(**{**r, "attempts": [Attempt(**x) for x in r["attempts"]]})
                                                for r in a["rounds"]]}) for a in item.pop("arms")]
                run = Run(**item, arms=arms)
            except (TypeError, KeyError):
                continue
            if run.status == "running":
                # The process that was driving it is gone.
                run.status, run.message = "stopped", "app 重新啟動過，這次的逼近停在這裡"
                for arm in run.arms:
                    if arm.status in ("running", "waiting"):
                        arm.status = "stopped"
            self.runs[run.id] = run

    def add(self, run: Run) -> None:
        self.runs[run.id] = run
        for old in sorted(self.runs.values(), key=lambda r: r.created)[:-self.keep]:
            self.runs.pop(old.id, None)
        self.save()

    def save(self) -> None:
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            data = [asdict(r) for r in sorted(self.runs.values(), key=lambda r: r.created)]
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            tmp.replace(self.path)
        except OSError:
            pass


async def poll_jobs(get_record, job_ids: list[str], cancelled, interval: float = 2.0,
                    timeout: float = 3 * 3600) -> dict:
    """Wait for library records to finish; used by the server's `wait`."""
    deadline = time.time() + timeout
    while True:
        out, pending = {}, False
        for job in job_ids:
            record = get_record(job)
            if record is None:
                out[job] = ("error", "", "工作不見了")
            elif record.status in ("done", "error"):
                out[job] = (record.status, record.output or "", record.message or "")
            else:
                pending = True
        if not pending or cancelled() or time.time() > deadline:
            for job in job_ids:
                out.setdefault(job, ("error", "", "等太久或被停止"))
            return out
        await asyncio.sleep(interval)

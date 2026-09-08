"""Queue every shot in an episode from one press, instead of one at a time.

What this is
------------
A loop over the shot list that submits the same jobs the buttons submit, and
records each one against its shot. Nothing else: it does not decide anything a
person would want to decide.

What it deliberately does not do
--------------------------------
**It never accepts a take.** After the keyframes are queued it stops, and the
user picks which one of each shot's candidates counts. Only then does the video
pass have anything to work from.

That is a real cost - it means two presses per episode, not one - and it is the
right one. Every generation produces several candidates and the last one to
finish is not the one anybody wanted; a runner that auto-accepted would fill a
progress bar with pictures nobody chose. The whole drama page is built on
"nothing completes itself", and a batch button is not a reason to abandon that.

State is derived, not stored
----------------------------
Which shots are done is computed from the shots and the job library, exactly as
the single-shot path computes it. The only thing held here is whether a run is
currently in flight, and what went wrong while queueing - neither of which can
be derived from anything.

The run record is its own file, not part of the project
-------------------------------------------------------
A project is what the user wrote: cast, shots, prompts, delivery. A run is one
attempt at executing it, and there can be many. Keeping the run inside the
project would mean the second run overwrote the first, and would rewrite the
creative file every time a job finished.

Restarting the app ends the run in flight. That is stated rather than hidden:
the app cannot prove what a queue was doing before it died, so the run is
marked interrupted and nothing restarts by itself. Pressing the button again
picks up where it stopped, because "what still needs doing" is derived - shots
that already got their takes are skipped.
"""

from __future__ import annotations

import json
import os
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path


# Queueing is cheap; generating is not. A cap exists so that "run the episode"
# on a fifty-shot project cannot commit the machine to a day of work before the
# user sees a single frame and realises the prompt was wrong.
MAX_PER_RUN = 60

# How many of a run's jobs may be unfinished at once. The app has one worker, so
# a bigger number does not make anything faster - it only means a queue full of
# this episode, and a user who wants to test one shot waiting behind twenty.
# Small also makes "stop" mean something: the jobs not yet submitted never are.
# A product choice, not a ComfyUI limit.
WINDOW = 3

# How long to wait between checks for room. Long enough not to spin, short
# enough that the queue does not sit empty after a job finishes.
POLL_SECONDS = 1.5

# How long to wait for one slot before giving up on the run. A video job on a
# slow card genuinely takes many minutes, so this is deliberately generous -
# it is here to stop a run waiting forever on a worker that died, not to cut
# off a job that is still working.
SLOT_TIMEOUT_SECONDS = 45 * 60


@dataclass
class Task:
    """One job to submit, with everything it needs already decided.

    The point is that it is decided *at the press*, not at the moment the job
    is finally submitted. A run feeds jobs in a few at a time, so an episode
    takes as long as generating it does - and in that window the user can edit
    shot 12. Without this, shots 1-11 would go out with the old prompt, 12-20
    with the new one, and nothing anywhere would record that the episode was
    made from two different versions of itself.

    So the payload is frozen here, and the runner submits it verbatim. Editing
    during a run changes the next run, not this one - which is a rule that can
    be stated to the user, unlike "it depends when the job went out".
    """

    shot_id: str
    shot_no: int
    stage: str
    payload: dict = field(default_factory=dict)

    def public(self) -> dict:
        return {"shot_id": self.shot_id, "shot_no": self.shot_no,
                "stage": self.stage, "payload": self.payload}

    @classmethod
    def restore(cls, raw: dict) -> "Task":
        return cls(shot_id=str(raw.get("shot_id") or ""),
                   shot_no=int(raw.get("shot_no") or 0),
                   stage=str(raw.get("stage") or "keyframe"),
                   payload=dict(raw.get("payload") or {}))


@dataclass
class Failure:
    shot_no: int
    reason: str

    def public(self) -> dict:
        return {"shot_no": self.shot_no, "reason": self.reason}


@dataclass
class Run:
    """One pass over a project, persisted so a restart can say what happened."""

    project: str
    stage: str                  # "keyframe" | "video"
    per_shot: int
    total: int = 0
    queued: int = 0
    failures: list[Failure] = field(default_factory=list)
    started: float = field(default_factory=time.time)
    finished: float | None = None
    stopped: bool = False
    message: str = ""
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    interrupted: bool = False
    # The frozen plan. Written before the first job is submitted, and never
    # rebuilt from the project afterwards.
    tasks: list[Task] = field(default_factory=list)

    @property
    def active(self) -> bool:
        return self.finished is None and not self.stopped

    def public(self) -> dict:
        return {
            "project": self.project, "stage": self.stage,
            "per_shot": self.per_shot, "total": self.total, "queued": self.queued,
            "failures": [f.public() for f in self.failures],
            "started": self.started, "finished": self.finished,
            "stopped": self.stopped, "active": self.active,
            "message": self.message, "id": self.id,
            "interrupted": self.interrupted,
            "window": WINDOW,
            # The count, not the plan itself: the payloads carry prompts and
            # are large, and no screen shows them.
            "planned": len(self.tasks),
        }

    def store(self) -> dict:
        return {**self.public(), "schema": 2,
                "tasks": [t.public() for t in self.tasks]}

    @classmethod
    def restore(cls, raw: dict) -> "Run":
        run = cls(project=str(raw.get("project") or ""),
                  stage=str(raw.get("stage") or "keyframe"),
                  per_shot=int(raw.get("per_shot") or 1))
        run.id = str(raw.get("id") or run.id)
        run.total = int(raw.get("total") or 0)
        run.queued = int(raw.get("queued") or 0)
        run.failures = [Failure(int(f.get("shot_no") or 0), str(f.get("reason") or ""))
                        for f in raw.get("failures") or []]
        run.started = float(raw.get("started") or time.time())
        run.finished = raw.get("finished")
        run.stopped = bool(raw.get("stopped"))
        run.message = str(raw.get("message") or "")
        run.interrupted = bool(raw.get("interrupted"))
        run.tasks = [Task.restore(t) for t in raw.get("tasks") or []]
        return run


class Runs:
    """The run in flight, if any. One at a time, on purpose.

    Two concurrent runs would compete for the same single worker queue and
    interleave two episodes' shots, which is confusing to watch and impossible
    to reason about when one of them fails.
    """

    def __init__(self, path: Path | None = None) -> None:
        self.current: Run | None = None
        self.path = path

    # -- persistence ---------------------------------------------------------
    # One file, replaced atomically. A run is small and only the latest one is
    # ever shown, so an append-only log would mean replaying events to answer a
    # question the file can answer directly.
    def load(self) -> None:
        if not self.path or not self.path.is_file():
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return
        run = Run.restore(raw)
        if run.finished is None and not run.stopped:
            # The app cannot prove what the queue was doing before it died, so
            # it does not claim the run continued - and it does not restart it
            # either. Taking the GPU on boot is not something to do unasked.
            run.interrupted = True
            run.stopped = True
            run.message = ("app 重開過，這一輪停在這裡了。"
                           "再按一次就從還沒做的鏡頭接著跑。")
        self.current = run

    def save(self) -> None:
        if not self.path or not self.current:
            return
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            temp = self.path.with_suffix(".tmp")
            temp.write_text(json.dumps(self.current.store(), ensure_ascii=False),
                            encoding="utf-8")
            os.replace(temp, self.path)
        except OSError:
            # Losing the record of a run is not a reason to fail the run.
            pass

    def start(self, project: str, stage: str, per_shot: int,
              tasks: list[Task]) -> Run:
        self.current = Run(project=project, stage=stage, per_shot=per_shot,
                           total=len(tasks), tasks=list(tasks))
        self.save()
        return self.current

    def stop(self) -> bool:
        if self.current and self.current.active:
            self.current.stopped = True
            self.current.message = "已停止 —— 已經排進去的還是會跑完。"
            self.save()
            return True
        return False

    def public(self) -> dict:
        return self.current.public() if self.current else {"active": False}


def shots_needing(project, jobs, stage: str) -> list:
    """Which shots still need work at this stage, in shot order.

    A shot with an accepted take is skipped: re-running the whole episode after
    picking half of it should not throw away the half that was picked.
    """
    import shortdrama

    out = []
    for shot in project.shots:
        state = shortdrama.shot_state(shot, jobs)
        stages = state["stages"]
        if stage == "keyframe":
            if not stages["keyframe"]["active_done"]:
                out.append(shot)
        elif stage == "video":
            # A video pass needs an accepted keyframe to work from, and there is
            # no point regenerating a shot whose video is already chosen.
            if stages["keyframe"]["active_done"] and not stages["video"]["active_done"]:
                out.append(shot)
    return out


def blocked_reason(project, jobs, stage: str) -> str:
    """Why this pass cannot start, in the user's words, or "" if it can."""
    import shortdrama

    if not project.shots:
        return "這個專案還沒有鏡頭。"
    if stage == "video":
        without = [s.no for s in project.shots
                   if not shortdrama.shot_state(s, jobs)["stages"]["keyframe"]["active_done"]]
        if without:
            return (f"有 {len(without)} 顆鏡頭還沒有採用的關鍵幀"
                    f"（第 {'、'.join(str(n) for n in without[:8])} 顆"
                    + ("…" if len(without) > 8 else "") + "）。"
                    "影片是從關鍵幀長出來的，所以要先每顆都挑一張。")
    return ""

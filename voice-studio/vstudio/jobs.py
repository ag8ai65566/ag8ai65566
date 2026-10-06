"""Persistent background jobs.

Two queues, each served by one worker thread:
- "gpu": data preparation, evaluation and anything else that needs the local GPU (one at a time);
- "io": uploads, cloud training monitoring and downloads (network-bound, so they never block the GPU queue).

Jobs live in the database, so the job list survives a restart; a job that was running when the app stopped is
marked failed with an explanation and can be retried. Handlers report progress and check for cancellation through
the JobContext they receive.
"""
from __future__ import annotations

import threading
import time
import traceback
from typing import Callable

from . import config, db

HANDLERS: dict[str, tuple[str, Callable]] = {}
GPU_LOCK = threading.RLock()  # shared with the TTS endpoints so generation and preparation never collide


class Cancelled(Exception):
    pass


def handler(kind: str, queue: str = "gpu"):
    def deco(fn):
        HANDLERS[kind] = (queue, fn)
        return fn
    return deco


class JobContext:
    def __init__(self, job: dict):
        self.job = job
        self.id = job["id"]
        self.params = job["params"]
        self._last = 0.0
        self.log_path = config.path("jobs", f"{self.id}.log")

    def progress(self, fraction: float, message: str = "", force: bool = False) -> None:
        t = time.time()
        if force or t - self._last > 0.5 or fraction >= 1:
            self._last = t
            db.update("jobs", self.id, {"progress": max(0.0, min(1.0, fraction)), "message": message})
        self.check()

    def log(self, line: str) -> None:
        with open(self.log_path, "a", encoding="utf-8") as fh:
            fh.write(time.strftime("[%H:%M:%S] ") + line.rstrip() + "\n")

    def check(self) -> None:
        r = db.connect().execute("SELECT cancel FROM jobs WHERE id=?", (self.id,)).fetchone()
        if r and r[0]:
            raise Cancelled()


def submit(kind: str, params: dict | None = None, message: str = "") -> dict:
    if kind not in HANDLERS:
        raise KeyError(f"unknown job kind {kind}")
    queue = HANDLERS[kind][0]
    job = db.insert("jobs", {"id": db.new_id("job"), "kind": kind, "queue": queue, "status": "queued",
                              "progress": 0.0, "message": message or "等待中", "params": params or {},
                              "result": {}, "created_at": db.now()})
    _wake.set()
    return job


def cancel(job_id: str) -> dict | None:
    job = db.get("jobs", job_id)
    if job and job["status"] in ("queued", "running"):
        if job["status"] == "queued":
            return db.update("jobs", job_id, {"status": "canceled", "cancel": 1, "finished_at": db.now(),
                                              "message": "已取消"})
        return db.update("jobs", job_id, {"cancel": 1, "message": "正在取消…"})
    return job


def retry(job_id: str) -> dict | None:
    job = db.get("jobs", job_id)
    if not job or job["status"] not in ("failed", "canceled"):
        return job
    return submit(job["kind"], job["params"])


_wake = threading.Event()
_stop = threading.Event()
_threads: list[threading.Thread] = []


def _next(queue: str) -> dict | None:
    with db.tx() as c:
        r = c.execute("SELECT * FROM jobs WHERE queue=? AND status='queued' ORDER BY created_at LIMIT 1",
                      (queue,)).fetchone()
        if r is None:
            return None
        c.execute("UPDATE jobs SET status='running', started_at=?, message=? WHERE id=?",
                  (db.now(), "執行中", r["id"]))
    return db.get("jobs", r["id"])


def _run(job: dict) -> None:
    ctx = JobContext(job)
    _, fn = HANDLERS[job["kind"]]
    try:
        result = fn(ctx) or {}
        db.update("jobs", job["id"], {"status": "done", "progress": 1.0, "result": result,
                                      "finished_at": db.now(), "message": result.get("message", "完成")})
    except Cancelled:
        db.update("jobs", job["id"], {"status": "canceled", "finished_at": db.now(), "message": "已取消"})
    except Exception as e:  # report the error in the UI and keep the worker alive
        ctx.log(traceback.format_exc())
        db.update("jobs", job["id"], {"status": "failed", "finished_at": db.now(),
                                      "message": f"{type(e).__name__}: {e}"[:500]})


def _worker(queue: str) -> None:
    while not _stop.is_set():
        job = _next(queue)
        if job is None:
            _wake.wait(1.0)
            _wake.clear()
            continue
        _run(job)


def start() -> None:
    """Mark jobs interrupted by a previous shutdown as failed, then start one worker per queue."""
    with db.tx() as c:
        c.execute("UPDATE jobs SET status='failed', message='程式關閉時中斷，可按「重試」', finished_at=? "
                  "WHERE status='running'", (db.now(),))
    if _threads:
        return
    for q in ("gpu", "io"):
        t = threading.Thread(target=_worker, args=(q,), name=f"jobs-{q}", daemon=True)
        t.start()
        _threads.append(t)


def stop() -> None:
    _stop.set()
    _wake.set()


def run_inline(kind: str, params: dict) -> dict:
    """Run a job synchronously in the calling thread (tests, scripts)."""
    job = db.insert("jobs", {"id": db.new_id("job"), "kind": kind, "queue": HANDLERS[kind][0], "status": "running",
                              "params": params, "result": {}, "created_at": db.now(), "started_at": db.now()})
    _run(job)
    return db.get("jobs", job["id"])

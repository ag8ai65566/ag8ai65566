"""Helpers shared by the engines' cloud training entry points.

This file runs on the rented GPU machine (inside the engine's environment), not on your PC. It is uploaded next to
bootstrap.sh for every training run. It only uses the standard library so it works in any engine environment.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import threading
import time
from pathlib import Path

LANG_NAMES = {"ja": "Japanese", "en": "English", "zh": "Chinese", "ko": "Korean", "de": "German", "fr": "French",
              "ru": "Russian", "pt": "Portuguese", "es": "Spanish", "it": "Italian"}


def log(msg: str) -> None:
    print(f"[vs] {msg}", flush=True)


class Job:
    """One training run: paths, parameters, progress reporting and packaging."""

    def __init__(self) -> None:
        argv = sys.argv
        self.config_path = Path(argv[argv.index("--config") + 1]).resolve()
        self.dir = self.config_path.parent                      # on the network volume (visible to the studio)
        self.data = Path(argv[argv.index("--data") + 1]) / "data"  # unpacked dataset (container disk)
        self.cfg = json.loads(self.config_path.read_text(encoding="utf-8"))
        self.params: dict = self.cfg.get("params", {})
        self.work = Path(os.environ.get("VS_WORK", "/root/vswork"))
        self.work.mkdir(parents=True, exist_ok=True)
        self.out = self.work / "model"                           # becomes model.tar → model/
        self.out.mkdir(parents=True, exist_ok=True)
        self._t0 = time.time()
        self._train_t0: float | None = None
        self._train_s0 = 0
        self._state: dict = {}

    # progress.json is read by the studio every 30 s over the S3 API
    def progress(self, **kw) -> None:
        self._state.update(kw)
        now = time.time()
        self._state["elapsed_s"] = int(now - self._t0)
        if kw.get("phase") == "train":  # measured speed, used by the studio to calibrate future estimates
            if self._train_t0 is None:
                self._train_t0, self._train_s0 = now, int(kw.get("step") or 0)
            elif (kw.get("step") or 0) > self._train_s0 + 2:
                self._state["s_per_step"] = round((now - self._train_t0) / (kw["step"] - self._train_s0), 3)
        tmp = self.dir / "progress.json.tmp"
        tmp.write_text(json.dumps(self._state), encoding="utf-8")
        os.replace(tmp, self.dir / "progress.json")

    def read_jsonl(self, name: str) -> list[dict]:
        f = self.data / name
        if not f.exists():
            return []
        return [json.loads(x) for x in f.read_text(encoding="utf-8").splitlines() if x.strip()]

    def run(self, cmd: list[str], cwd: Path | None = None, on_line=None, env: dict | None = None) -> None:
        """Run a command, echo its output to train.log and feed each line to on_line; raise on failure."""
        log("$ " + " ".join(str(c) for c in cmd))
        p = subprocess.Popen([str(c) for c in cmd], cwd=str(cwd) if cwd else None, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, bufsize=1, env={**os.environ, **(env or {})},
                             errors="replace")
        assert p.stdout is not None
        for line in p.stdout:
            sys.stdout.write(line)
            if on_line:
                try:
                    on_line(line.rstrip("\n"))
                except Exception as e:  # progress parsing must never stop training
                    log(f"progress parse: {e}")
        code = p.wait()
        if code != 0:
            raise RuntimeError(f"command failed with exit code {code}: {cmd[:3]}")

    def package(self, meta: dict) -> None:
        """Write engine.json and pack model/ into model.tar on the network volume (atomic rename)."""
        meta = {**meta, "training_id": self.cfg.get("training_id"), "params": self.params,
                "train_seconds": int(time.time() - self._t0)}
        (self.out / "engine.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        self.progress(phase="package")
        tmp = self.dir / "model.tar.tmp"
        with tarfile.open(tmp, "w") as t:
            t.add(self.out, arcname="model")
        os.replace(tmp, self.dir / "model.tar")
        log(f"packaged {(self.dir / 'model.tar').stat().st_size / 1e9:.2f} GB")


def sample_plan(job: Job) -> dict:
    """The held-out lines every checkpoint reads aloud, so checkpoints can be compared by ear and by score."""
    f = job.data / "samples.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"lines": [], "reference": None}


def free_gb(path: str = "/root") -> float:
    return shutil.disk_usage(path).free / 1e9


class LogTail(threading.Thread):
    """Follow a log file written by a trainer and call on_line for each new line."""

    def __init__(self, path: Path, on_line) -> None:
        super().__init__(daemon=True)
        self.path, self.on_line, self.stop = path, on_line, threading.Event()

    def run(self) -> None:
        pos = 0
        while not self.stop.is_set():
            if self.path.exists():
                with self.path.open("r", encoding="utf-8", errors="replace") as f:
                    f.seek(pos)
                    for line in f:
                        try:
                            self.on_line(line.rstrip("\n"))
                        except Exception:
                            pass
                    pos = f.tell()
            self.stop.wait(2)


METRIC = re.compile(r"([\w/]+):\s*(-?[\d.]+(?:e-?\d+)?)")


def parse_metrics(s: str) -> dict:
    return {k: float(v) for k, v in METRIC.findall(s)}

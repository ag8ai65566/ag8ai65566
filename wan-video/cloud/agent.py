#!/usr/bin/env python3
"""The part of this app that runs on the rented machine.

Why it exists
-------------
A rented GPU arrives empty. ComfyUI has an endpoint for uploading a picture and
none for putting a 20GB model where it can find it, so something on that machine
has to fetch the files, say how far along it is, and say what went wrong at
boot. That is all this does. It never touches the GPU and never sees a prompt.

It is one file with no dependencies beyond the standard library, on purpose: it
has to start in the first second of a cold boot, before anything is installed,
so that the app at home has something to ask "how is the install going?" while
the slow part is still running. A boot that fails silently on a machine that
bills by the second is the worst outcome available here.

What is open and what is not
----------------------------
The address this listens on is public - RunPod's proxy puts it on the internet
and says so. So:

* ``GET /status`` is open. It reports the boot phase and the tail of the boot
  log, and nothing else. No path, token or prompt is ever written to that log.
* Everything that reads or changes the disk needs the token the app generated
  when it rented the machine, compared in constant time.
* A download's auth header is used for that one request and then dropped. It
  is not written to disk, not kept in the status table, and not sent on to a
  different host if the server redirects - the same rule the local downloader
  follows, for the same reason: a redirect is how a token ends up somewhere
  nobody chose to send it.
"""

from __future__ import annotations

import argparse
import hmac
import json
import math
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

VERSION = "1"
CHUNK = 1 << 20
MAX_JSON = 1 << 20
# One upload request has to finish inside the proxy's 100-second limit, so the
# app sends a big file as a series of these rather than as one long request.
MAX_UPLOAD_CHUNK = 64 << 20
PARALLEL = 2
RETRIES = 4
SAFE_SEGMENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _.()+,=@\-]*$")
# Headers a caller may attach to a download. Anything else is dropped: this is
# a file fetcher, not a general-purpose request forwarder.
ALLOWED_HEADERS = {"authorization", "user-agent"}
# LoRA training (kohya-ss/sd-scripts, SDXL). Pinned for the same reason
# ComfyUI is: the arguments below were read off this release's own docs.
SDSCRIPTS_REPO = "https://github.com/kohya-ss/sd-scripts.git"
SDSCRIPTS_REF = os.environ.get("WAN_SDSCRIPTS_REF", "v0.12.3")
OPTIMIZERS = {"AdamW8bit", "AdamW", "Adafactor", "Prodigy"}
SCHEDULERS = {"cosine", "constant", "constant_with_warmup", "linear", "cosine_with_restarts"}
# Every number the app may set, with its type and bounds. Anything else in the
# request is ignored: the agent builds the command itself and never runs a
# command line or a config file it was handed.
TRAIN_NUMBERS = {
    "network_dim": (int, 1, 256), "network_alpha": (float, 0.1, 256.0),
    "learning_rate": (float, 1e-7, 1e-2), "unet_lr": (float, 1e-7, 1e-2),
    "text_encoder_lr": (float, 0.0, 1e-2), "epochs": (int, 1, 50),
    "repeats": (int, 1, 100), "resolution": (int, 512, 2048), "batch_size": (int, 1, 8),
}
IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".webp")
FILE_CHUNK = 32 << 20


class Refused(Exception):
    """The request was understood and will not be done. Carries the reason."""

    def __init__(self, message: str, status: int = 400) -> None:
        super().__init__(message)
        self.status = status


def safe_relative(folder: str, name: str) -> Path:
    """`folder/name` as a relative path that cannot leave the models directory.

    Every segment has to look like a filename. That rules out `..`, absolute
    paths, empty segments and drive letters in one test, instead of trying to
    list the bad cases.
    """
    parts = [p for p in str(folder).replace("\\", "/").split("/") if p != ""]
    parts.append(str(name))
    if not parts or len(parts) > 6:
        raise Refused("路徑不對")
    for part in parts:
        if part in (".", "..") or not SAFE_SEGMENT.match(part):
            raise Refused(f"路徑裡有不允許的片段：{part[:40]!r}")
    return Path(*parts)


class State:
    """Everything the agent knows, behind one lock."""

    def __init__(self, root: Path, token: str) -> None:
        self.root = root
        self.models = root / "ComfyUI" / "models"
        self.train_root = root / "train"
        self.token = token
        self.lock = threading.Lock()
        self.downloads: dict[str, dict] = {}
        # Auth headers live here, separately from `downloads`, so that nothing
        # which serialises the table can leak one.
        self._secrets: dict[str, dict] = {}
        self.slots = threading.Semaphore(PARALLEL)
        self.started = time.time()
        # When the app that rented this machine was last heard from. Only an
        # authorised request counts: /status is open to anyone, and a stranger
        # polling it must not be able to keep a paid machine alive.
        self.last_seen = time.time()

    # -- paths ---------------------------------------------------------------

    def target(self, folder: str, name: str, area: str = "models") -> Path:
        rel = safe_relative(folder, name)
        root = self.train_root if area == "train" else self.models
        path = (root / rel).resolve()
        base = root.resolve()
        if base != path and base not in path.parents:
            raise Refused("路徑跑到模型資料夾外面了")
        return path

    # -- boot ----------------------------------------------------------------

    def phase(self) -> str:
        try:
            return (self.root / "phase").read_text(encoding="utf-8").strip()
        except OSError:
            return "booting"

    def log_tail(self, name: str, lines: int) -> list[str]:
        # Only the two logs this app writes. `name` is a key, never a path.
        path = {"boot": self.root / "boot.log", "comfy": self.root / "comfy.log"}.get(name)
        if path is None or not path.is_file():
            return []
        try:
            with path.open("rb") as handle:
                handle.seek(0, os.SEEK_END)
                size = handle.tell()
                handle.seek(max(0, size - 64_000))
                text = handle.read().decode("utf-8", errors="replace")
        except OSError:
            return []
        return text.splitlines()[-max(1, min(lines, 400)):]

    def status(self) -> dict:
        usage = shutil.disk_usage(self.root)
        with self.lock:
            active = sum(1 for d in self.downloads.values()
                         if d["status"] in ("queued", "running"))
        return {
            "agent": VERSION,
            "phase": self.phase(),
            "uptime": int(time.time() - self.started),
            "disk": {"free": usage.free, "total": usage.total},
            "downloading": active,
            "training": bool(getattr(self, "trainer", None) and self.trainer.running),
            "log": self.log_tail("boot", 40),
        }

    # -- files ---------------------------------------------------------------

    def files(self) -> list[dict]:
        out = []
        if not self.models.is_dir():
            return out
        for path in sorted(self.models.rglob("*")):
            if not path.is_file() or path.name.endswith(".part"):
                continue
            if path.name.startswith("put_") and path.name.endswith("_here"):
                continue          # ComfyUI's own placeholder files
            rel = path.relative_to(self.models)
            out.append({"folder": rel.parent.as_posix(), "name": rel.name,
                        "size": path.stat().st_size})
        return out

    def delete(self, folder: str, name: str) -> bool:
        path = self.target(folder, name)
        removed = False
        for candidate in (path, path.with_name(path.name + ".part")):
            if candidate.is_file():
                candidate.unlink()
                removed = True
        return removed

    # -- downloads -----------------------------------------------------------

    def public_downloads(self) -> dict:
        with self.lock:
            return {key: dict(value) for key, value in self.downloads.items()}

    def enqueue(self, url: str, folder: str, name: str, size: int, headers: dict) -> dict:
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme != "https" and not _local_test_url(parsed):
            raise Refused("只接受 https 的下載來源")
        target = self.target(folder, name)
        key = f"{folder.strip('/')}/{name}"
        clean = {k: str(v) for k, v in (headers or {}).items()
                 if k.lower() in ALLOWED_HEADERS}
        with self.lock:
            current = self.downloads.get(key)
            if current and current["status"] in ("queued", "running"):
                return dict(current)
            if target.is_file() and (not size or target.stat().st_size == size):
                entry = {"id": key, "status": "done", "done": target.stat().st_size,
                         "total": target.stat().st_size, "error": "", "speed": 0}
                self.downloads[key] = entry
                return dict(entry)
            entry = {"id": key, "status": "queued", "done": 0, "total": int(size or 0),
                     "error": "", "speed": 0}
            self.downloads[key] = entry
            self._secrets[key] = clean
        threading.Thread(target=self._work, args=(key, url, target, int(size or 0)),
                         daemon=True).start()
        return dict(entry)

    def cancel(self, key: str) -> bool:
        with self.lock:
            entry = self.downloads.get(key)
            if not entry or entry["status"] not in ("queued", "running"):
                return False
            entry["status"] = "cancelled"
        return True

    def _set(self, key: str, **changes) -> None:
        with self.lock:
            self.downloads[key].update(changes)

    def _cancelled(self, key: str) -> bool:
        with self.lock:
            return self.downloads[key]["status"] == "cancelled"

    def _work(self, key: str, url: str, target: Path, size: int) -> None:
        with self.slots:
            if self._cancelled(key):
                return
            self._set(key, status="running")
            error = ""
            for attempt in range(RETRIES):
                try:
                    self._fetch(key, url, target, size)
                    error = ""
                    break
                except Refused as exc:        # a definite answer; do not retry
                    error = str(exc)
                    break
                except Exception as exc:      # noqa: BLE001 - network: try again
                    error = f"{type(exc).__name__}: {exc}"
                    time.sleep(min(2 ** attempt, 8))
                if self._cancelled(key):
                    return
            with self.lock:
                self._secrets.pop(key, None)
                entry = self.downloads[key]
                if entry["status"] == "cancelled":
                    return
                entry["status"] = "error" if error else "done"
                entry["error"] = error
                entry["speed"] = 0

    def _fetch(self, key: str, url: str, target: Path, size: int) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        part = target.with_name(target.name + ".part")
        have = part.stat().st_size if part.is_file() else 0
        if size and have > size:              # a stale partial from another file
            part.unlink()
            have = 0
        free = shutil.disk_usage(target.parent).free
        if size and size - have > free:
            raise Refused(
                f"雲端機的硬碟不夠：還需要 {(size - have) / 1e9:.1f} GB，"
                f"只剩 {free / 1e9:.1f} GB。")

        with self.lock:
            headers = dict(self._secrets.get(key) or {})
        headers.setdefault("User-Agent", "wan-video-agent/" + VERSION)
        if have:
            headers["Range"] = f"bytes={have}-"

        response = _open(url, headers)
        try:
            status = response.status
            if status == 200 and have:
                # The server ignored the range: start the file again rather
                # than append a whole copy to half of one.
                have = 0
                mode = "wb"
            elif status == 206:
                mode = "ab"
            elif status == 200:
                mode = "wb"
            elif status == 416 and size and have == size:
                part.replace(target)
                self._set(key, done=size, total=size)
                return
            else:
                raise Refused(_explain_http(status, url))
            length = int(response.headers.get("Content-Length") or 0)
            total = size or (have + length if length else 0)
            self._set(key, done=have, total=total)

            done, mark, mark_done = have, time.time(), have
            with part.open(mode) as handle:
                while True:
                    if self._cancelled(key):
                        return
                    block = response.read(CHUNK)
                    if not block:
                        break
                    handle.write(block)
                    done += len(block)
                    now = time.time()
                    if now - mark >= 1.0:
                        self._set(key, done=done,
                                  speed=int((done - mark_done) / (now - mark)))
                        mark, mark_done = now, done
            self._set(key, done=done)
        finally:
            response.close()

        if size and done != size:
            if done > size:
                part.unlink(missing_ok=True)
                raise Refused(
                    f"下載到的大小不對（{done} bytes，應該是 {size}）。"
                    "來源那邊的檔案換過了，或者網址指到別的東西。")
            raise ConnectionError(f"連線中斷在 {done}/{size}")   # retry resumes
        part.replace(target)

    # -- uploads -------------------------------------------------------------

    def read_slice(self, folder: str, name: str, offset: int) -> tuple[bytes, int]:
        """A piece of a model file, for sending a trained LoRA back to the app."""
        path = self.target(folder, name)
        if not path.is_file():
            raise Refused("沒有這個檔案", 404)
        total = path.stat().st_size
        with path.open("rb") as handle:
            handle.seek(max(0, offset))
            return handle.read(FILE_CHUNK), total

    def receive(self, folder: str, name: str, offset: int, total: int, body: bytes,
                area: str = "models") -> dict:
        """One slice of a file the app is pushing up from the user's own disk."""
        if total <= 0 or offset < 0 or offset + len(body) > total:
            raise Refused("上傳的位置或大小不對")
        target = self.target(folder, name, area)
        part = target.with_name(target.name + ".part")
        target.parent.mkdir(parents=True, exist_ok=True)
        have = part.stat().st_size if part.is_file() else 0
        if offset == 0 and have:
            part.unlink()
            have = 0
        if offset != have:
            # Out of step - say where we actually are, so the sender can resume
            # from there instead of starting a multi-gigabyte upload again.
            return {"received": have, "complete": False, "resync": True}
        with part.open("ab") as handle:
            handle.write(body)
        have += len(body)
        if have == total:
            part.replace(target)
            return {"received": have, "complete": True}
        return {"received": have, "complete": False}


class Trainer:
    """One LoRA training run at a time, with kohya-ss/sd-scripts.

    The app sends a name, the base checkpoint (a file already in models/),
    and a handful of numbers. This class checks each one, writes the dataset
    config itself, and starts the trainer with an argument list - there is
    no shell and no config text from outside, so nothing the request says can
    turn into a command. The images and captions were uploaded first into
    train/<name>/img (PUT /upload?area=train).

    The result is written straight into models/loras/<name>/, so the ComfyUI
    on this machine can use it the moment it exists; the app fetches it back
    with GET /file.

    WAN_TRAIN_CMD replaces the trainer with a script (tests only): it is run
    with the output folder, name and total steps, and nothing is installed.
    """

    def __init__(self, state: "State") -> None:
        self.state = state
        self.lock = threading.Lock()
        self.proc: subprocess.Popen | None = None
        self.info = {"phase": "idle", "name": "", "step": 0, "total": 0, "error": "",
                     "started": 0.0, "finished": 0.0, "outputs": []}
        self._stop = False

    @property
    def running(self) -> bool:
        return self.info["phase"] in ("installing", "training")

    # -- checking the request ------------------------------------------------

    def _spec(self, data: dict) -> dict:
        name = str(data.get("name") or "")
        if not SAFE_SEGMENT.match(name) or len(name) > 64:
            raise Refused("訓練名稱只能用英數字、底線、減號")
        base_folder, base_name = str(data.get("base_folder") or "checkpoints"), str(data.get("base_name") or "")
        if base_folder != "checkpoints":
            raise Refused("底模要放在 checkpoints 資料夾")
        base = self.state.target(base_folder, base_name)
        if not base.is_file():
            raise Refused(f"雲端機上沒有底模 {base_name}，先下載再訓練")
        spec = {"name": name, "base": base}
        for key, (kind, low, high) in TRAIN_NUMBERS.items():
            try:
                value = kind(data[key])
            except (KeyError, TypeError, ValueError) as exc:
                raise Refused(f"缺少或看不懂 {key}") from exc
            if not low <= value <= high:
                raise Refused(f"{key} 要在 {low} 到 {high} 之間")
            spec[key] = value
        spec["optimizer"] = str(data.get("optimizer") or "AdamW8bit")
        spec["scheduler"] = str(data.get("scheduler") or "cosine")
        if spec["optimizer"] not in OPTIMIZERS or spec["scheduler"] not in SCHEDULERS:
            raise Refused("不支援的 optimizer 或 scheduler")
        images = [p for p in (self.state.train_root / name / "img").glob("*")
                  if p.suffix.lower() in IMAGE_SUFFIXES]
        if len(images) < 5:
            raise Refused(f"訓練圖太少（{len(images)} 張），至少要 5 張，建議 15～30 張")
        spec["images"] = len(images)
        steps_per_epoch = math.ceil(len(images) * spec["repeats"] / spec["batch_size"])
        spec["total"] = steps_per_epoch * spec["epochs"]
        return spec

    def start(self, data: dict) -> dict:
        with self.lock:
            if self.running:
                raise Refused("已經有一個訓練在跑了", 409)
            spec = self._spec(data)
            self._stop = False
            self.info = {"phase": "installing", "name": spec["name"], "step": 0,
                         "total": spec["total"], "error": "", "started": time.time(),
                         "finished": 0.0, "outputs": []}
        threading.Thread(target=self._run, args=(spec,), daemon=True).start()
        return self.status()

    def stop(self) -> dict:
        self._stop = True
        proc = self.proc
        if proc is not None and proc.poll() is None:
            proc.terminate()
        return self.status()

    # -- running ---------------------------------------------------------------

    def _folder(self, name: str) -> Path:
        return self.state.train_root / name

    def _log(self, name: str) -> Path:
        return self._folder(name) / "train.log"

    def _say(self, name: str, text: str) -> None:
        with self._log(name).open("a", encoding="utf-8") as handle:
            handle.write(time.strftime("[%H:%M:%S] ", time.gmtime()) + text + "\n")

    def _install(self, name: str) -> Path:
        """sd-scripts in its own environment, so its packages never meet ComfyUI's."""
        repo = self.state.root / "sd-scripts"
        venv = self.state.root / "train-venv"
        marker = self.state.root / f".sd-scripts-{SDSCRIPTS_REF}"
        if marker.is_file() and (venv / "bin" / "python").is_file():
            return venv / "bin" / "python"
        self._say(name, f"第一次訓練：安裝 sd-scripts {SDSCRIPTS_REF}（幾分鐘）")
        if repo.is_dir():
            shutil.rmtree(repo)
        steps = [
            ["git", "clone", "--quiet", "--depth", "1", "--branch", SDSCRIPTS_REF, SDSCRIPTS_REPO, str(repo)],
            [sys.executable, "-m", "venv", "--system-site-packages", str(venv)],
            [str(venv / "bin" / "python"), "-m", "pip", "install", "--quiet", "-r", "requirements.txt"],
        ]
        for argv in steps:
            with self._log(name).open("a", encoding="utf-8") as handle:
                done = subprocess.run(argv, cwd=str(repo) if repo.is_dir() else None,
                                      stdout=handle, stderr=subprocess.STDOUT)
            if done.returncode != 0:
                raise RuntimeError(f"安裝 sd-scripts 失敗：{' '.join(argv[:3])}（看訓練紀錄）")
        marker.touch()
        return venv / "bin" / "python"

    def _dataset_config(self, spec: dict) -> Path:
        """kohya's documented dataset config (docs/config_README-en.md): the
        repeats are num_repeats on the subset, not a folder-name prefix."""
        folder = self._folder(spec["name"])
        text = (
            "[general]\nshuffle_caption = true\ncaption_extension = '.txt'\nkeep_tokens = 1\n\n"
            f"[[datasets]]\nresolution = {spec['resolution']}\nbatch_size = {spec['batch_size']}\n"
            "enable_bucket = true\nmin_bucket_reso = 640\nmax_bucket_reso = 1536\n"
            "bucket_reso_steps = 64\nbucket_no_upscale = true\n\n"
            f"  [[datasets.subsets]]\n  image_dir = {json.dumps(str(folder / 'img'))}\n"
            f"  num_repeats = {spec['repeats']}\n")
        path = folder / "dataset.toml"
        path.write_text(text, encoding="utf-8")
        return path

    def command(self, spec: dict, python: Path, out_dir: Path) -> tuple[list[str], Path | None]:
        fake = os.environ.get("WAN_TRAIN_CMD")
        if fake:
            return [sys.executable, fake, str(out_dir), spec["name"], str(spec["total"])], None
        repo = self.state.root / "sd-scripts"
        dataset = self._dataset_config(spec)
        # The documented SDXL command (docs/sdxl_train_network.md), checked
        # flag by flag against the pinned release's own argument parser - the
        # docs on `main` show --text_encoder_lr1/2, which v0.12.3 does not
        # have: there it is one --text_encoder_lr taking a value per encoder.
        # --sdpa in place of xformers, which the image may not have.
        accelerate = python.parent / "accelerate"
        argv = [str(accelerate), "launch", "--num_cpu_threads_per_process", "1",
                "sdxl_train_network.py",
                "--pretrained_model_name_or_path", str(spec["base"]),
                "--dataset_config", str(dataset),
                "--output_dir", str(out_dir), "--output_name", spec["name"],
                "--save_model_as", "safetensors",
                "--network_module", "networks.lora",
                "--network_dim", str(spec["network_dim"]), "--network_alpha", str(spec["network_alpha"]),
                "--learning_rate", str(spec["learning_rate"]), "--unet_lr", str(spec["unet_lr"]),
                "--text_encoder_lr", str(spec["text_encoder_lr"]), str(spec["text_encoder_lr"]),
                "--optimizer_type", spec["optimizer"], "--lr_scheduler", spec["scheduler"],
                "--max_train_epochs", str(spec["epochs"]), "--save_every_n_epochs", "1",
                "--mixed_precision", "bf16", "--save_precision", "bf16",
                "--gradient_checkpointing", "--cache_latents", "--cache_latents_to_disk",
                "--sdpa", "--seed", "42", "--max_data_loader_n_workers", "2"]
        return argv, repo

    def _run(self, spec: dict) -> None:
        name = spec["name"]
        out_dir = self.state.models / "loras" / name
        try:
            self._folder(name).mkdir(parents=True, exist_ok=True)
            python = Path(sys.executable) if os.environ.get("WAN_TRAIN_CMD") else self._install(name)
            if self._stop:
                raise InterruptedError
            out_dir.mkdir(parents=True, exist_ok=True)
            argv, cwd = self.command(spec, python, out_dir)
            self.info["phase"] = "training"
            self._say(name, f"開始訓練：{spec['images']} 張 × {spec['repeats']} 次 × {spec['epochs']} 輪 = {spec['total']} 步")
            with self._log(name).open("ab") as handle:
                self.proc = subprocess.Popen(argv, cwd=str(cwd) if cwd else None,
                                             stdout=handle, stderr=subprocess.STDOUT)
            while self.proc.poll() is None:
                self._progress(name)
                time.sleep(2)
            self._progress(name)
            if self._stop:
                raise InterruptedError
            if self.proc.returncode != 0:
                raise RuntimeError(f"訓練程式結束代碼 {self.proc.returncode}（看訓練紀錄）")
            self.info["outputs"] = sorted(p.name for p in out_dir.glob("*.safetensors"))
            if not self.info["outputs"]:
                raise RuntimeError("訓練跑完了，但沒有產生任何 LoRA 檔")
            self.info["phase"] = "done"
            self._say(name, "訓練完成：" + "、".join(self.info["outputs"]))
        except InterruptedError:
            self.info["phase"] = "stopped"
            self._say(name, "訓練被停止")
        except Exception as exc:  # noqa: BLE001 - reported, never crashes the agent
            self.info["phase"], self.info["error"] = "failed", str(exc)
            try:
                self._say(name, f"訓練失敗：{exc}")
            except OSError:
                pass
        finally:
            self.info["finished"] = time.time()
            self.proc = None

    _STEP = re.compile(rb"(\d+)/(\d+) \[")

    def _progress(self, name: str) -> None:
        """tqdm's `120/1000 [` in the log's last few kilobytes, if there is one."""
        try:
            with self._log(name).open("rb") as handle:
                handle.seek(0, os.SEEK_END)
                handle.seek(max(0, handle.tell() - 8192))
                tail = handle.read()
        except OSError:
            return
        found = self._STEP.findall(tail.replace(b"\r", b"\n"))
        if found:
            step, total = found[-1]
            self.info["step"] = int(step)
            if int(total) > 0:
                self.info["total"] = int(total)

    def status(self) -> dict:
        out = dict(self.info)
        name = out["name"]
        out["log"] = []
        if name:
            try:
                lines = self._log(name).read_text(encoding="utf-8", errors="replace")
                out["log"] = [line for line in lines.replace("\r", "\n").splitlines() if line.strip()][-25:]
            except OSError:
                pass
        return out


def _local_test_url(parsed: urllib.parse.SplitResult) -> bool:
    """Plain http is allowed to this machine only, which is what the tests use."""
    return parsed.scheme == "http" and parsed.hostname in ("127.0.0.1", "localhost")


class _StripAuthOnHostChange(urllib.request.HTTPRedirectHandler):
    """Follow redirects, but never carry credentials to a different host.

    Hugging Face answers a download with a redirect to a storage host, and
    CivitAI does the same. The default handler copies every header across,
    which hands the user's token to whoever the redirect names.
    """

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is None:
            return None
        old_host = urllib.parse.urlsplit(req.full_url).netloc.lower()
        new_host = urllib.parse.urlsplit(newurl).netloc.lower()
        if old_host != new_host:
            for name in list(new.headers):
                if name.lower() == "authorization":
                    del new.headers[name]
            for name in list(new.unredirected_hdrs):
                if name.lower() == "authorization":
                    del new.unredirected_hdrs[name]
        return new


def _open(url: str, headers: dict):
    opener = urllib.request.build_opener(_StripAuthOnHostChange())
    request = urllib.request.Request(url, headers=headers)
    try:
        return opener.open(request, timeout=60)
    except urllib.error.HTTPError as exc:
        if exc.code == 416:
            return exc                     # carries .status and .headers
        raise Refused(_explain_http(exc.code, url)) from exc


def _explain_http(status: int, url: str) -> str:
    host = urllib.parse.urlsplit(url).hostname or ""
    if status in (401, 403):
        if "huggingface.co" in host:
            return (f"HTTP {status}：Hugging Face 拒絕了。這個倉庫是閘門式的 —— "
                    "設定頁要有 Hugging Face token，而且要先到那個模型頁按同意授權。")
        if "civitai.com" in host:
            return f"HTTP {status}：CivitAI 拒絕了。到設定頁確認 CivitAI API key。"
        return f"HTTP {status}：來源拒絕存取（{host}）。"
    if status == 404:
        return f"HTTP 404：來源那邊沒有這個檔案（{host}）。"
    return f"HTTP {status}（{host}）"


def gpu_info() -> dict:
    """What card this machine actually has, from nvidia-smi. Empty if none."""
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,memory.total,memory.used",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return {}
    if not out:
        return {}
    name, total, used = [part.strip() for part in out.splitlines()[0].split(",")][:3]
    try:
        return {"name": name, "vram_mb": int(total), "used_mb": int(used)}
    except ValueError:
        return {"name": name}


def comfy_busy(port: int) -> bool:
    """Is ComfyUI on this machine running or holding a job?"""
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/queue", timeout=5) as response:
            queue = json.loads(response.read().decode("utf-8"))
    except Exception:  # noqa: BLE001 - not up, or mid-restart: nothing queued
        return False
    return bool(queue.get("queue_running") or queue.get("queue_pending"))


def should_stop(state: State, minutes: int, now: float, busy: bool) -> bool:
    """The dead-man rule, on its own so it can be tested without a clock.

    Stop only when all three hold: the switch is on, the app has been silent
    for the whole window, and nothing is in flight. A render someone started
    and walked away from is not abandonment - it finishes first.
    """
    if minutes <= 0 or busy:
        return False
    with state.lock:
        downloading = any(d["status"] in ("queued", "running")
                          for d in state.downloads.values())
    if downloading:
        return False
    return now - state.last_seen >= minutes * 60


def stop_this_machine() -> str:
    """Ask Runpod to stop the machine this is running on. Returns how.

    Tried in order, because which of these a given image has is not something
    this file can know: the REST call needs nothing installed, and the two CLI
    spellings cover the tool before and after its arguments were reordered.
    Stopping ends the GPU billing; the models are on a network volume and stay.
    """
    pod_id = os.environ.get("RUNPOD_POD_ID") or ""
    if not pod_id:
        return ""
    key = os.environ.get("RUNPOD_API_KEY") or ""
    if key:
        try:
            request = urllib.request.Request(
                f"https://api.runpod.io/v2/pods/{pod_id}/action",
                data=json.dumps({"action": "stop"}).encode("utf-8"), method="POST",
                headers={"Authorization": f"Bearer {key}",
                         "Content-Type": "application/json"})
            with urllib.request.urlopen(request, timeout=30) as response:
                if 200 <= response.status < 300:
                    return "api"
        except Exception:  # noqa: BLE001 - fall through to the CLI
            pass
    for argv in (["runpodctl", "pod", "stop", pod_id], ["runpodctl", "stop", "pod", pod_id]):
        try:
            if subprocess.run(argv, capture_output=True, timeout=60).returncode == 0:
                return "cli"
        except (OSError, subprocess.SubprocessError):
            continue
    return ""


def deadman_loop(state: State, minutes: int, comfy_port: int) -> None:
    """Stop the machine once the app that rented it has clearly gone away.

    The commonest way to leave a rented GPU running overnight is to close the
    laptop. The app's own idle timer cannot help with that - it is not running
    either - so the machine has to notice for itself.
    """
    log = state.root / "boot.log"
    while True:
        time.sleep(60)
        busy = comfy_busy(comfy_port) or bool(getattr(state, "trainer", None) and state.trainer.running)
        if not should_stop(state, minutes, time.time(), busy):
            continue
        how = stop_this_machine()
        try:
            with log.open("a", encoding="utf-8") as handle:
                handle.write(time.strftime("[%H:%M:%S] ", time.gmtime())
                             + (f"{minutes} 分鐘沒有收到 app 的訊號，也沒有工作在跑：已自動關機（{how}）\n"
                                if how else
                                f"{minutes} 分鐘沒有收到 app 的訊號，但關機指令沒有成功 —— 請到 Runpod 主控台手動關\n"))
        except OSError:
            pass
        # Either it is stopping, or it could not be stopped; do not hammer.
        time.sleep(600)


def make_handler(state: State):
    class Handler(BaseHTTPRequestHandler):
        server_version = "wan-agent/" + VERSION
        protocol_version = "HTTP/1.1"

        def log_message(self, *args) -> None:      # keep the boot log readable
            pass

        # -- plumbing --------------------------------------------------------

        def _send(self, payload: dict, status: int = 200) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _send_bytes(self, data: bytes, total: int) -> None:
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("X-Total-Size", str(total))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def _authorised(self) -> bool:
            given = self.headers.get("X-Wan-Token") or ""
            return bool(state.token) and hmac.compare_digest(given, state.token)

        def _body(self, limit: int) -> bytes:
            length = int(self.headers.get("Content-Length") or 0)
            if length < 0 or length > limit:
                raise Refused("內容太大", 413)
            return self.rfile.read(length) if length else b""

        def _json(self) -> dict:
            raw = self._body(MAX_JSON)
            try:
                data = json.loads(raw.decode("utf-8") or "{}")
            except ValueError as exc:
                raise Refused("不是 JSON") from exc
            if not isinstance(data, dict):
                raise Refused("要是一個 JSON 物件")
            return data

        def _route(self, method: str) -> None:
            url = urllib.parse.urlsplit(self.path)
            query = {k: v[0] for k, v in urllib.parse.parse_qs(url.query).items()}
            try:
                if method == "GET" and url.path == "/status":
                    return self._send(state.status())
                if not self._authorised():
                    # Drain what was sent so the connection stays usable.
                    try:
                        self._body(MAX_UPLOAD_CHUNK)
                    except Refused:
                        pass
                    return self._send({"error": "token 不對"}, 401)
                state.last_seen = time.time()
                if method == "POST" and url.path == "/ping":
                    self._body(MAX_JSON)
                    return self._send({"ok": True})

                if method == "GET" and url.path == "/files":
                    return self._send({"files": state.files()})
                if method == "GET" and url.path == "/downloads":
                    return self._send({"items": state.public_downloads()})
                if method == "GET" and url.path == "/gpu":
                    return self._send({"gpu": gpu_info()})
                if method == "GET" and url.path == "/log":
                    return self._send({"lines": state.log_tail(
                        query.get("name", "comfy"), int(query.get("tail", "120") or 120))})
                if method == "POST" and url.path == "/download":
                    data = self._json()
                    return self._send(state.enqueue(
                        str(data.get("url") or ""), str(data.get("folder") or ""),
                        str(data.get("name") or ""), int(data.get("size") or 0),
                        data.get("headers") if isinstance(data.get("headers"), dict) else {}))
                if method == "POST" and url.path == "/cancel":
                    return self._send({"cancelled": state.cancel(str(self._json().get("id") or ""))})
                if method == "POST" and url.path == "/delete":
                    data = self._json()
                    return self._send({"deleted": state.delete(
                        str(data.get("folder") or ""), str(data.get("name") or ""))})
                if method == "PUT" and url.path == "/upload":
                    body = self._body(MAX_UPLOAD_CHUNK)
                    return self._send(state.receive(
                        query.get("folder", ""), query.get("name", ""),
                        int(query.get("offset", "0") or 0),
                        int(query.get("total", "0") or 0), body,
                        "train" if query.get("area") == "train" else "models"))
                if method == "GET" and url.path == "/file":
                    data, total = state.read_slice(query.get("folder", ""), query.get("name", ""),
                                                   int(query.get("offset", "0") or 0))
                    return self._send_bytes(data, total)
                if method == "POST" and url.path == "/train":
                    return self._send(state.trainer.start(self._json()))
                if method == "GET" and url.path == "/train":
                    return self._send(state.trainer.status())
                if method == "POST" and url.path == "/train/stop":
                    self._body(MAX_JSON)
                    return self._send(state.trainer.stop())
                return self._send({"error": "沒有這個路徑"}, 404)
            except Refused as exc:
                return self._send({"error": str(exc)}, exc.status)
            except (ValueError, OSError) as exc:
                return self._send({"error": f"{type(exc).__name__}: {exc}"}, 400)

        def do_GET(self) -> None:      # noqa: N802 - http.server's naming
            self._route("GET")

        def do_POST(self) -> None:     # noqa: N802
            self._route("POST")

        def do_PUT(self) -> None:      # noqa: N802
            self._route("PUT")

    return Handler


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--root", default=os.environ.get("WAN_ROOT", "/workspace/wan"))
    parser.add_argument("--port", type=int,
                        default=int(os.environ.get("WAN_AGENT_PORT", "8189")))
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()

    token = (os.environ.get("WAN_AGENT_TOKEN") or "").strip()
    if len(token) < 16:
        # Without a token every write endpoint would be open to the internet.
        # Refusing to start is the only safe answer; /status would not be worth it.
        raise SystemExit("WAN_AGENT_TOKEN is missing or too short; refusing to start.")
    root = Path(args.root)
    root.mkdir(parents=True, exist_ok=True)
    state = State(root, token)
    state.trainer = Trainer(state)
    server = ThreadingHTTPServer((args.host, args.port), make_handler(state))
    server.daemon_threads = True
    try:
        minutes = int(os.environ.get("WAN_DEADMAN_MINUTES") or 0)
    except ValueError:
        minutes = 0
    if minutes > 0 and os.environ.get("RUNPOD_POD_ID"):
        threading.Thread(
            target=deadman_loop,
            args=(state, minutes, int(os.environ.get("WAN_COMFY_PORT") or 8188)),
            daemon=True).start()
    print(f"wan agent {VERSION} listening on {args.host}:{args.port}, root {root}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()

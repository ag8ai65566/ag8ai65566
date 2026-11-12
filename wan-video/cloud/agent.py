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
import os
import re
import shutil
import subprocess
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

    def target(self, folder: str, name: str) -> Path:
        rel = safe_relative(folder, name)
        path = (self.models / rel).resolve()
        base = self.models.resolve()
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

    def receive(self, folder: str, name: str, offset: int, total: int, body: bytes) -> dict:
        """One slice of a file the app is pushing up from the user's own disk."""
        if total <= 0 or offset < 0 or offset + len(body) > total:
            raise Refused("上傳的位置或大小不對")
        target = self.target(folder, name)
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
        if not should_stop(state, minutes, time.time(), comfy_busy(comfy_port)):
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
                        int(query.get("total", "0") or 0), body))
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

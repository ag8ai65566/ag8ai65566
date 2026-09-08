"""Find ComfyUI on this machine, and start it.

Why this exists
---------------
This app does not generate anything. It builds a graph and hands it to
ComfyUI, which is the program that actually uses the graphics card. So
"ComfyUI is not running" is the single most common failure there is - and the
user hit it holding an error that said `ClientConnectorError` and a fix that
named `run_nvidia_gpu.bat`, a file their install does not contain.

Their install does not contain it because `setup-windows.ps1` clones ComfyUI
into `<repo>/ComfyUI` and `start.bat` launches it from the shared venv. The
advice was written for the portable ComfyUI download instead. Guessing at
someone's layout and then telling them to go find a file is worse than saying
nothing: they go looking, do not find it, and conclude the app is broken.

So this module looks, and says what it found. If ComfyUI is where this
project's own installer puts it, the app can start it without the user
touching a terminal at all.
"""

from __future__ import annotations

import os
import shlex
import subprocess
import urllib.parse
import sys
from dataclasses import dataclass
from pathlib import Path

import config


@dataclass
class Found:
    """What is actually on disk, and therefore what to tell the user."""

    comfy: Path | None = None       # a directory containing main.py
    python: Path | None = None      # the interpreter to run it with
    installer: Path | None = None   # this project's own setup script
    starter: Path | None = None     # this project's own start script

    @property
    def installed(self) -> bool:
        return self.comfy is not None

    @property
    def startable(self) -> bool:
        """Whether this app can start it, rather than only describe it."""
        return bool(self.comfy and self.python)

    def public(self) -> dict:
        return {
            "installed": self.installed,
            "startable": self.startable,
            "comfy": str(self.comfy) if self.comfy else "",
            "python": str(self.python) if self.python else "",
            "installer": self.installer.name if self.installer else "",
            "starter": self.starter.name if self.starter else "",
        }


def _python_for(root: Path) -> Path | None:
    """The interpreter `start.bat` would use, or this one as a fallback.

    A ComfyUI clone has no interpreter of its own; the installer builds one
    venv and shares it between ComfyUI and this app. Running ComfyUI with the
    wrong Python is how you get "no module named torch" from a machine that
    demonstrably has torch.
    """
    for rel in ("venv/Scripts/python.exe", "venv/bin/python",
                ".venv/Scripts/python.exe", ".venv/bin/python"):
        candidate = root / rel
        if candidate.is_file():
            return candidate
    # Embedded portable layout: ComfyUI_windows_portable/python_embeded.
    for rel in ("python_embeded/python.exe", "../python_embeded/python.exe"):
        candidate = root / rel
        if candidate.is_file():
            return candidate.resolve()
    return Path(sys.executable) if sys.executable else None


def find(root: Path | None = None) -> Found:
    """Where ComfyUI is, if it is anywhere this project knows to look."""
    base = Path(root) if root else config.REPO
    out = Found()
    for name in ("install.bat", "setup-windows.ps1", "setup-linux.sh"):
        if (base / name).is_file():
            out.installer = base / name
            break
    for name in ("start.bat", "start-windows.ps1"):
        if (base / name).is_file():
            out.starter = base / name
            break

    seen: list[Path] = []
    configured = getattr(config, "COMFY_DIR", None)
    if configured:
        seen.append(Path(configured))
    seen += [base / "ComfyUI", base.parent / "ComfyUI", Path("/opt/ComfyUI")]
    for candidate in seen:
        try:
            if (candidate / "main.py").is_file():
                out.comfy = candidate
                break
        except OSError:
            continue
    if out.comfy:
        out.python = _python_for(base)
    return out


def advice(found: Found, url: str) -> str:
    """What to do next, in terms of files this install actually has.

    Three different situations that used to share one message: it is installed
    and merely not running, it was never installed, or this is a Docker/remote
    setup where neither applies.
    """
    if found.startable:
        return (
            f"ComfyUI 裝好了（{found.comfy}），只是現在沒有在跑。\n"
            "按下面那顆「幫我啟動 ComfyUI」就好 —— "
            f"或關掉現在這個視窗，改用雙擊 {found.starter.name if found.starter else 'start.bat'}"
            "，它會同時開 ComfyUI 和這個 app。"
        )
    if found.installed:
        return (
            f"ComfyUI 在 {found.comfy}，但找不到可以跑它的 Python。\n"
            f"雙擊 {found.installer.name if found.installer else 'install.bat'} 重跑一次安裝，"
            "它會把環境補起來。"
        )
    if found.installer:
        return (
            "**你還沒有安裝 ComfyUI。** 它是真正用你顯卡算圖的程式，"
            "這個 app 只是它的前端。\n"
            f"雙擊專案資料夾裡的 **{found.installer.name}** —— "
            "它會自動把 ComfyUI 和需要的東西都裝好（要下載幾 GB，會跑一陣子）。\n"
            f"裝完之後改用雙擊 **{found.starter.name if found.starter else 'start.bat'}** 啟動，"
            "它會同時開 ComfyUI 和這個 app。"
        )
    return (
        f"連不上 ComfyUI（{url}），而且在這台機器上找不到它。\n"
        "如果你是用 Docker 跑的，`docker compose up -d` 會把兩個都帶起來。"
    )


class StartError(RuntimeError):
    pass


def listen_for(url: str) -> tuple[str, str]:
    """The host and port to start ComfyUI on, taken from the URL we will call.

    Starting it on 8188 while the app talks to :8189 gives the worst possible
    outcome: it really did start, the button says so, and the banner never goes
    away because nothing is listening where this app looks.
    """
    parts = urllib.parse.urlsplit(url or "")
    host = parts.hostname or "127.0.0.1"
    port = str(parts.port or 8188)
    return host, port


def split_args(args: str) -> list[str]:
    """`COMFY_ARGS` from .env, as argv. Quoted paths stay in one piece.

    `.split()` broke `--foo "D:\My Files"` into two arguments, which is how a
    perfectly correct setting turns into an unreadable ComfyUI error.
    """
    try:
        return [a for a in shlex.split(args or "") if a]
    except ValueError:
        # Unbalanced quotes. Whitespace splitting is wrong too, but it is what
        # the user's line most nearly means, and refusing to start over a
        # stray quote helps nobody.
        return [a for a in (args or "").split() if a]


def start(found: Found, args: str = "", url: str = "") -> subprocess.Popen:
    """Launch ComfyUI the way this project's own start script does.

    Detached on purpose: it has to outlive the request that started it, and on
    Windows it needs its own console or closing this app's window would take
    ComfyUI down with it.
    """
    if not found.startable:
        raise StartError("找不到 ComfyUI 或可以跑它的 Python。")
    extra = split_args(args)
    host, port = listen_for(url)
    command = [str(found.python), "main.py"]
    # Only when the user has not said otherwise in COMFY_ARGS. Passing both
    # would leave two --port flags and the answer depending on argparse order.
    if "--listen" not in extra:
        command += ["--listen", host]
    if "--port" not in extra:
        command += ["--port", port]
    command += extra
    kwargs: dict = {"cwd": str(found.comfy)}
    if os.name == "nt":
        # CREATE_NEW_CONSOLE. ComfyUI prints its progress there, which is where
        # the user has always been told to look when something goes wrong.
        kwargs["creationflags"] = 0x00000010
    else:
        kwargs["start_new_session"] = True
        kwargs["stdout"] = subprocess.DEVNULL
        kwargs["stderr"] = subprocess.DEVNULL
    try:
        return subprocess.Popen(command, **kwargs)
    except OSError as exc:
        raise StartError(f"叫不動 ComfyUI：{exc}") from exc

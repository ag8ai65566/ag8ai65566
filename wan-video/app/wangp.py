"""WanGP: a separate app that this one installs and starts - not a part of it.

Why it is here
--------------
"Give it a picture and let it work out the rest" - plan the shots, generate
them, look at every take, redo the bad ones, cut a video - is what WanGP's
Showrunner does (github.com/deepbeepmeep/Wan2GP; v20.20, 2026-11-24, read
from its README and docs). Its planner is a local language model: Qwen3.8 27B,
in a "Bonsai" quantisation under 6GB that it picks by itself on cards with less
than 16GB. It also runs video models this ComfyUI front end cannot fit on a
10GB card - by its own account MiniMax H3 at 1080p for 15 s in 5.9GB with its
"extreme chunker".

Rebuilding that inside this app would be a worse copy of something that is
already free, local and maintained, so this app puts it next to itself
(`WanGP\\`), installs it with WanGP's own installer and starts it. The work is
in wangp-windows.ps1; this module only answers "is it there, is it running,
and what is the command".

Nothing is sent to WanGP and nothing is read from it. Its own options that
would send things off the computer (a remote LLM for its assistant, web
search) are off by default, and the page says to leave them off for adult
material.
"""

from __future__ import annotations

import socket
from pathlib import Path

PORT = 7860
URL = f"http://127.0.0.1:{PORT}"
HOME = "https://github.com/deepbeepmeep/Wan2GP"
SCRIPT = "wangp-windows.ps1"
ACTIONS = ("install", "start", "update")


def folder(root: Path) -> Path:
    return root / "WanGP"


def installed(root: Path) -> bool:
    return (folder(root) / "wgp.py").is_file()


def ready(root: Path) -> bool:
    """Installed *and* its installer finished: it writes envs.json last."""
    return installed(root) and (folder(root) / "envs.json").is_file()


def running(host: str = "127.0.0.1", port: int = PORT, timeout: float = 0.3) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def status(root: Path) -> dict:
    return {"installed": installed(root), "ready": ready(root), "running": running(),
            "url": URL, "home": HOME, "folder": str(folder(root)),
            "script": (root / SCRIPT).is_file() and (root / LAUNCHER).is_file()}


LAUNCHER = "wangp.bat"


def command(root: Path, action: str) -> list[str]:
    """What the page's buttons run, in a console of its own.

    Through wangp.bat rather than PowerShell directly: the .bat ends with
    `pause`, so the window stays open on "installed" - or on the reason it was
    not - instead of closing the instant the script exits. The name is
    relative (the process starts in `root`), which keeps cmd.exe's quoting
    rules out of it for folders with spaces or parentheses in their path.
    """
    if action not in ACTIONS:
        raise ValueError(action)
    return ["cmd.exe", "/c", LAUNCHER, "-Action", action]

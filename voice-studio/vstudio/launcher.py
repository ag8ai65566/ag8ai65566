"""The "Voice Manager" button at the top right: opens another program on this computer in one click.

The target is a program (.exe), a batch file, a shortcut (.lnk / .url), a folder or a web address, stored in the
settings as "voice_manager". Until one is chosen, the default folder (E:\\HololiveVoiceManager) is searched for
something that starts a program; when exactly one is found, that one is used.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

from . import config

DEFAULT_DIR = Path(os.environ.get("VSTUDIO_VOICE_MANAGER_DIR", r"E:\HololiveVoiceManager"))
LAUNCH_EXT = {".exe", ".bat", ".cmd", ".lnk", ".url"}
URL = re.compile(r"^https?://[^\s]+$", re.IGNORECASE)
PREFER = re.compile(r"start|run|launch|open|manager|gui|app|啟動|開啟|執行", re.IGNORECASE)
AVOID = re.compile(r"install|setup|update|uninstall|unins|build|test|安裝|更新|移除", re.IGNORECASE)


def candidates(folder: Path) -> list[str]:
    """Things in a folder (and one level down) that start a program, the likeliest first."""
    if not folder.is_dir():
        return []
    found: list[Path] = []
    for p in sorted(folder.iterdir()):
        if p.is_file() and p.suffix.lower() in LAUNCH_EXT:
            found.append(p)
        elif p.is_dir() and not p.name.startswith((".", "_")) and p.name.lower() not in ("node_modules", "venv", ".venv"):
            found += [q for q in sorted(p.iterdir()) if q.is_file() and q.suffix.lower() in LAUNCH_EXT]
    found = [p for p in found if not AVOID.search(p.stem)]
    found.sort(key=lambda p: (len(p.relative_to(folder).parts), not PREFER.search(p.stem), p.suffix.lower() != ".exe",
                              p.name.lower()))
    return [str(p) for p in found[:12]]


def valid(target: str) -> bool:
    t = target.strip().strip('"')
    if URL.match(t):
        return True
    p = Path(t)
    return p.is_dir() or (p.is_file() and p.suffix.lower() in LAUNCH_EXT)


def status() -> dict:
    target = (config.load_settings().get("voice_manager") or "").strip()
    folder = DEFAULT_DIR
    resolved = None
    if target and URL.match(target):
        resolved = target
    elif target and Path(target).is_file() and Path(target).suffix.lower() in LAUNCH_EXT:
        resolved = target
    elif target and Path(target).is_dir():
        folder = Path(target)
    found = candidates(folder) if resolved is None else []
    if resolved is None and not target and len(found) == 1:
        resolved = found[0]
    if resolved is None and target and Path(target).is_dir():
        resolved = found[0] if len(found) == 1 else target  # a folder with no single program opens the folder
    return {"target": target, "resolved": resolved, "folder": str(folder), "folder_exists": folder.is_dir(),
            "candidates": found, "is_url": bool(resolved and URL.match(resolved))}


def launch(target: str) -> None:
    """Open a program, shortcut, batch file or folder the way double-clicking it would."""
    p = Path(target)
    if sys.platform == "win32":
        # "start" opens .exe/.bat/.lnk/.url and folders like Explorer does; a batch file runs from its own folder
        subprocess.Popen(["cmd", "/c", "start", "", str(p)], cwd=str(p if p.is_dir() else p.parent),
                         creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    elif sys.platform == "darwin":
        subprocess.Popen(["open", str(p)])
    else:
        subprocess.Popen(["xdg-open", str(p)], cwd=str(p if p.is_dir() else p.parent))

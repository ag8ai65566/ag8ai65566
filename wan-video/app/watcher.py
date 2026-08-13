"""Drop-folder mode: put images in inbox/, videos come out in outputs/.

The prompt for foo.png comes from foo.txt next to it; without one, the filename
itself is used (underscores become spaces), then PROMPT_DEFAULT as a fallback.
Submits through the same HTTP API the browser uses, so there is one code path.
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import config
import requests

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
POLL_SECONDS = float(os.environ.get("WATCH_INTERVAL", "3"))
PROMPT_DEFAULT = os.environ.get("PROMPT_DEFAULT", "subtle natural motion, cinematic")


def stable(path: Path, checks: int = 2) -> bool:
    """Wait for the file size to stop changing, so we don't read a partial copy."""
    try:
        last = path.stat().st_size
    except OSError:
        return False
    for _ in range(checks):
        time.sleep(1)
        try:
            size = path.stat().st_size
        except OSError:
            return False
        if size != last or size == 0:
            last = size
            return False
    return True


def prompt_for(path: Path) -> str:
    sidecar = path.with_suffix(".txt")
    if sidecar.is_file():
        text = sidecar.read_text(encoding="utf-8", errors="replace").strip()
        if text:
            return text
    stem = path.stem.replace("_", " ").replace("-", " ").strip()
    return stem or PROMPT_DEFAULT


def submit(path: Path) -> None:
    prompt = prompt_for(path)
    print(f"[watch] {path.name} -> {prompt!r}", flush=True)
    with path.open("rb") as fh:
        response = requests.post(
            f"{config.APP_URL}/api/generate",
            files={"image": (path.name, fh, "application/octet-stream")},
            data={"prompt": prompt},
            timeout=120,
        )
    if response.status_code != 200:
        print(f"[watch] 送出失敗 {path.name}: {response.status_code} {response.text[:300]}", flush=True)
        return

    job = response.json()
    done = config.DONE_DIR
    done.mkdir(parents=True, exist_ok=True)
    path.rename(done / f"{job['id']}-{path.name}")
    sidecar = path.with_suffix(".txt")
    if sidecar.is_file():
        sidecar.rename(done / f"{job['id']}-{sidecar.name}")


def main() -> int:
    inbox = config.INBOX_DIR
    inbox.mkdir(parents=True, exist_ok=True)
    print(f"[watch] 監看 {inbox} → {config.OUTPUT_DIR}", flush=True)

    for attempt in range(60):
        try:
            requests.get(f"{config.APP_URL}/api/health", timeout=10)
            break
        except requests.RequestException:
            time.sleep(2)
    else:
        print(f"[watch] 連不上 {config.APP_URL}", flush=True)
        return 1

    while True:
        try:
            candidates = sorted(
                p for p in inbox.iterdir()
                if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
            )
            for path in candidates:
                if stable(path):
                    submit(path)
        except Exception as exc:  # noqa: BLE001 - a watcher must not die
            print(f"[watch] {type(exc).__name__}: {exc}", flush=True)
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    sys.exit(main())

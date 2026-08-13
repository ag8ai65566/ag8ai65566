#!/usr/bin/env python3
"""Download a model's files from the command line, resumably.

    python3 scripts/fetch-model.py --list
    python3 scripts/fetch-model.py wan22-14b-fp8
    python3 scripts/fetch-model.py hy15-480p --models-dir ./ComfyUI/models

Uses the same catalogue as the web UI (app/registry.py), so filenames and
destinations can never drift between the two. Only the standard library is
needed, so this runs before any dependencies are installed.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))

import registry  # noqa: E402

CHUNK = 1 << 20
HF = "https://huggingface.co"


def human(n: float) -> str:
    """Decimal units, to match the web UI and how Hugging Face reports sizes."""
    for unit in ("B", "KB", "MB", "GB"):
        if abs(n) < 1000 or unit == "GB":
            return f"{n:.0f}{unit}" if unit in ("B", "KB") else f"{n:.1f}{unit}"
        n /= 1000
    return f"{n:.1f}GB"


def fetch(file: registry.ModelFile, dest_root: Path) -> bool:
    target = dest_root / file.folder / file.name
    target.parent.mkdir(parents=True, exist_ok=True)
    part = target.with_suffix(target.suffix + ".part")

    if target.exists() and target.stat().st_size == file.size:
        print(f"  ✓ {file.name}（已完成）")
        return True

    url = f"{HF}/{file.repo}/resolve/main/{file.path}"
    for attempt in range(1, 6):
        have = part.stat().st_size if part.exists() else 0
        if have > file.size:
            part.unlink()
            have = 0
        if have == file.size:
            break

        request = urllib.request.Request(url)
        if have:
            request.add_header("Range", f"bytes={have}-")
            print(f"  ↻ {file.name}（從 {human(have)} 續傳）")
        else:
            print(f"  ↓ {file.name}（{human(file.size)}）")

        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                mode = "ab" if response.status == 206 else "wb"
                if mode == "wb":
                    have = 0
                start, last = time.time(), 0.0
                with part.open(mode) as fh:
                    while True:
                        chunk = response.read(CHUNK)
                        if not chunk:
                            break
                        fh.write(chunk)
                        have += len(chunk)
                        now = time.time()
                        if now - last > 0.5:
                            last = now
                            pct = have / file.size * 100
                            rate = have / max(0.1, now - start)
                            print(f"\r     {pct:5.1f}%  {human(have)} / {human(file.size)}  {human(rate)}/s   ",
                                  end="", flush=True)
                print()
            break
        except urllib.error.HTTPError as exc:
            if exc.code == 416 and part.exists() and part.stat().st_size == file.size:
                break
            print(f"\n     HTTP {exc.code}（第 {attempt}/5 次）")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            print(f"\n     {type(exc).__name__}: {exc}（第 {attempt}/5 次）")
        if attempt == 5:
            print(f"  ✗ {file.name} 下載失敗")
            return False
        time.sleep(2 ** attempt)

    actual = part.stat().st_size if part.exists() else 0
    if actual != file.size:
        print(f"  ✗ {file.name} 大小不符：{actual} != {file.size}")
        return False
    part.replace(target)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="下載 wan-video 的模型檔案")
    parser.add_argument("model", nargs="?", help="模型 id（用 --list 看有哪些）")
    parser.add_argument("--models-dir", default=None, help="ComfyUI 的 models 目錄")
    parser.add_argument("--list", action="store_true", help="列出所有模型")
    parser.add_argument("--check", action="store_true", help="只檢查、不下載")
    args = parser.parse_args()

    if args.list or not args.model:
        print(f"{'id':16} {'顯存':>6} {'下載':>9}  說明")
        for m in registry.MODELS:
            print(f"{m.id:16} {str(m.vram_gb) + 'GB':>6} {human(m.download_bytes):>9}  {m.label}")
        print("\n用法：python3 scripts/fetch-model.py <id>")
        return 0

    model = registry.get(args.model)
    if model is None:
        print(f"不認識的模型：{args.model}（用 --list 看清單）", file=sys.stderr)
        return 1

    root = Path(args.models_dir) if args.models_dir else next(
        (p for p in (ROOT / "models", ROOT / "ComfyUI" / "models") if p.exists()), ROOT / "models"
    )
    root.mkdir(parents=True, exist_ok=True)

    print(f"{model.label}")
    print(f"目標目錄：{root}")
    print(f"總共 {len(model.all_files)} 個檔，{human(model.download_bytes)}")

    if args.check:
        for f in model.all_files:
            path = root / f.folder / f.name
            size = path.stat().st_size if path.exists() else 0
            mark = "✓" if size == f.size else ("◐" if size else "·")
            print(f"  {mark} {f.folder}/{f.name}  {human(size)} / {human(f.size)}")
        return 0

    free = shutil.disk_usage(root).free
    if free < model.download_bytes * 1.05:
        print(f"\n磁碟空間不足：剩 {human(free)}，需要約 {human(model.download_bytes)}", file=sys.stderr)
        return 1

    print()
    ok = all(fetch(f, root) for f in model.all_files)
    print()
    if ok:
        print(f"完成。在網頁上選「{model.label}」就能用了。")
        return 0
    print("有檔案沒下載完，再跑一次會從斷點續傳。", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())

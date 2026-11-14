#!/usr/bin/env python3
"""Cut a run's model.tar on the network volume into parts the studio can download.

RunPod's S3 API could not serve a 28.6 GB model.tar written on the pod: every ranged GET, even of its first bytes,
ended in a 524 from RunPod's proxy. Files of 64 MB are served at once. A pod with the volume mounted reads the file
directly, so this script writes model.tar.p0000, model.tar.p0001 … and the manifest model.tar.json (the same layout a
training run writes since then), which the studio then downloads part by part.

Usage: split_model.py <run folder> <part bytes>

- copy: when the volume has room for a second copy, the parts are copied out and model.tar is left as it is;
- in place: otherwise the last part is written, synced, and model.tar is truncated by that much, from the end to the
  start, so the data is always whole in model.tar plus the parts and at most one part of extra space is needed.

Re-running continues where an interrupted run stopped. progress lands in split.json (status running / done / error).
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import time
from pathlib import Path


def put(d: Path, name: str, obj: dict) -> None:
    tmp = d / f"{name}.tmp"
    tmp.write_text(json.dumps(obj), encoding="utf-8")
    os.replace(tmp, d / name)


def write_part(d: Path, key: str, data: bytes) -> None:
    tmp = d / f"{key}.tmp"
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, d / key)
    try:  # the rename itself must be on disk before model.tar is cut
        fd = os.open(d, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
    except OSError:
        pass


def split(d: Path, part: int) -> dict:
    src, manifest_f, state_f = d / "model.tar", d / "model.tar.json", d / "model.tar.split.json"
    if manifest_f.exists():
        return json.loads(manifest_f.read_text(encoding="utf-8"))
    if state_f.exists():
        state = json.loads(state_f.read_text(encoding="utf-8"))
    else:
        if not src.exists():
            raise FileNotFoundError(f"{src} is not there")
        size = src.stat().st_size
        mode = "copy" if shutil.disk_usage(d).free > size + (1 << 30) else "inplace"
        state = {"size": size, "part": part, "mode": mode}
        put(d, state_f.name, state)
    size, part, mode = int(state["size"]), int(state["part"]), state["mode"]
    n = max(1, -(-size // part))
    keys = [f"model.tar.p{i:04d}" for i in range(n)]
    want = [min(part, size - i * part) for i in range(n)]
    t0, made = time.time(), 0

    def report(i_done: int) -> None:
        put(d, "split.json", {"status": "running", "mode": mode, "parts": n, "done": i_done,
                              "elapsed_s": int(time.time() - t0)})

    if mode == "copy":
        with open(src, "rb") as f:
            for i in range(n):
                p = d / keys[i]
                if not (p.exists() and p.stat().st_size == want[i]):
                    f.seek(i * part)
                    write_part(d, keys[i], f.read(want[i]))
                made += 1
                if made % 8 == 0 or made == n:
                    report(made)
    else:
        left = src.stat().st_size if src.exists() else 0
        while left > 0:
            i = (left - 1) // part
            a = i * part
            p = d / keys[i]
            if not (p.exists() and p.stat().st_size == left - a):
                with open(src, "rb") as f:
                    f.seek(a)
                    data = f.read(left - a)
                if len(data) != left - a:
                    raise OSError(f"short read of part {i}: {len(data)} of {left - a} bytes")
                write_part(d, keys[i], data)
            os.truncate(src, a)
            left = a
            made = n - i
            if made % 8 == 0 or left == 0:
                report(made)
    for i in range(n):  # every part must be whole before the manifest says so
        if (d / keys[i]).stat().st_size != want[i]:
            raise OSError(f"part {keys[i]} has {(d / keys[i]).stat().st_size} bytes, expected {want[i]}")
    manifest = {"name": "model.tar", "size": size, "parts": [{"key": k, "size": w} for k, w in zip(keys, want, strict=True)]}
    put(d, manifest_f.name, manifest)
    src.unlink(missing_ok=True)  # the parts hold everything now (in place: it is empty already)
    state_f.unlink(missing_ok=True)
    return manifest


def main() -> None:
    d, part = Path(sys.argv[1]), int(sys.argv[2])
    try:
        m = split(d, part)
        put(d, "split.json", {"status": "done", "parts": len(m["parts"]), "size": m["size"]})
        print(f"[vs] split model.tar into {len(m['parts'])} parts", flush=True)
    except Exception as e:  # the studio reads why
        put(d, "split.json", {"status": "error", "error": f"{type(e).__name__}: {e}"[:500]})
        print(f"[vs] split failed: {e}", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

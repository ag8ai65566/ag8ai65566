"""Refresh tests/schema_core.json from a running ComfyUI.

    python3 tests/dump_schema.py http://127.0.0.1:8188

Run this after a ComfyUI upgrade so the test fixture keeps matching what the
real server accepts. Only the node types this app builds with are captured.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

NEEDED = [
    "UNETLoader", "UnetLoaderGGUF", "CLIPLoader", "DualCLIPLoader", "VAELoader",
    "LoraLoaderModelOnly", "ModelSamplingSD3", "CLIPTextEncode", "LoadImage",
    "WanImageToVideo", "Wan22ImageToVideoLatent", "HunyuanVideo15ImageToVideo",
    "CLIPVisionLoader", "CLIPVisionEncode", "KSampler", "KSamplerAdvanced",
    "VAEDecode", "CreateVideo", "SaveVideo", "SaveAnimatedWEBP",
    # text-to-image
    "CheckpointLoaderSimple", "EmptyLatentImage", "LoraLoader", "CLIPSetLastLayer",
    "LatentUpscale", "SaveImage",
]


def main() -> int:
    base = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8188").rstrip("/")
    with urllib.request.urlopen(f"{base}/object_info", timeout=120) as r:
        info = json.load(r)

    out, missing = {}, []
    for name in NEEDED:
        if name in info:
            out[name] = {"input": info[name]["input"], "output": info[name].get("output", [])}
        else:
            missing.append(name)

    target = Path(__file__).parent / "schema_core.json"
    target.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    print(f"wrote {len(out)} schemas to {target}")
    if missing:
        print("not present on this install (custom nodes not loaded?):", ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())

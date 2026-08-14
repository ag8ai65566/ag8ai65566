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
    # image-to-image, upscaling, quality patches
    "VAEEncode", "ImageScale", "RepeatLatentBatch", "ImageBatch",
    "UpscaleModelLoader", "ImageUpscaleWithModel", "VAEDecodeTiled",
    "FreeU_V2", "PerturbedAttentionGuidance", "RescaleCFG",
    # video post-processing
    "FrameInterpolationModelLoader", "FrameInterpolate",
]


# Nodes that come from custom node packages rather than core ComfyUI, so a
# plain install never reports them. Hand-written from each package's own source
# and merged back in, otherwise re-running this dumper silently deletes them and
# every GGUF graph starts failing validation against the fixture.
STUBS = {
    "UnetLoaderGGUF": {
        "input": {
            "required": {
                "unet_name": [
                    [
                        "Wan2.2-I2V-A14B-HighNoise-Q4_K_M.gguf",
                        "Wan2.2-I2V-A14B-LowNoise-Q4_K_M.gguf",
                    ]
                ]
            }
        },
        "output": ["MODEL"],
    },
}


def main() -> int:
    base = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8188").rstrip("/")
    with urllib.request.urlopen(f"{base}/object_info", timeout=120) as r:
        info = json.load(r)

    out, missing, stubbed = {}, [], []
    for name in NEEDED:
        if name in info:
            out[name] = {"input": info[name]["input"], "output": info[name].get("output", [])}
        elif name in STUBS:
            out[name] = STUBS[name]
            stubbed.append(name)
        else:
            missing.append(name)

    target = Path(__file__).parent / "schema_core.json"
    target.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    print(f"wrote {len(out)} schemas to {target}")
    if stubbed:
        print("kept hand-written stubs for custom nodes:", ", ".join(stubbed))
    if missing:
        print("NOT captured and no stub available:", ", ".join(missing))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())

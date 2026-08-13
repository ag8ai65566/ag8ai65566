"""Pre-flight check: are ComfyUI, the custom nodes and the model files all in place?

    docker compose run --rm app python check.py
"""

from __future__ import annotations

import asyncio
import sys

import config
import workflow
from comfy_client import ComfyClient


async def main() -> int:
    client = ComfyClient(config.COMFY_URL)
    print(f"ComfyUI: {config.COMFY_URL}")
    try:
        await client.wait_until_ready(timeout=60)
    except Exception as exc:  # noqa: BLE001
        print(f"  ✗ 連不上：{exc}")
        return 1

    info = await client.object_info()
    print(f"  ✓ 就緒（{len(info)} 種節點）")

    for node in ("WanImageToVideo", "KSamplerAdvanced", "ModelSamplingSD3", "LoraLoaderModelOnly"):
        print(f"  {'✓' if node in info else '✗'} {node}")
    if "UnetLoaderGGUF" in info:
        print("  ✓ UnetLoaderGGUF（GGUF 可用）")
    video_nodes = [n for n in ("CreateVideo", "SaveVideo", "VHS_VideoCombine") if n in info]
    print(f"  影片輸出節點：{', '.join(video_nodes) or '只有 SaveAnimatedWEBP'}")

    settings = config.settings().resolved()
    print(f"\nProfile: {config.PROFILE} / loader={settings.loader}")
    print(f"  steps={settings.steps} boundary={settings.boundary} cfg={settings.cfg} shift={settings.shift}")

    # Building a real graph is enough to prove every model filename resolves,
    # without spending GPU time on a generation.
    graph = workflow.build(
        image_name="placeholder.png",
        prompt="test",
        negative=workflow.DEFAULT_NEGATIVE,
        seed=1,
        width=832,
        height=480,
        settings=settings,
        available_nodes=set(info),
    )
    problems = await client.validate(graph)

    print("\n工作流程檢查：")
    if not problems:
        print("  ✓ 全部通過，可以開始生成")
        return 0
    for problem in problems:
        print(f"  ✗ {problem}")
    print("\n模型檔名對不上的話，檢查 ./models 下的檔案，或在 .env 用 MODEL_HIGH/MODEL_LOW 指定。")
    return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

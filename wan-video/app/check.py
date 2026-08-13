"""Pre-flight check: ComfyUI, custom nodes, model files and every graph.

    docker compose run --rm app python check.py
    .\venv\Scripts\python.exe app\check.py
"""

from __future__ import annotations

import asyncio
import sys

import config
import downloader
import registry
import workflow
from comfy_client import ComfyClient


def gb(n: int) -> str:
    return f"{n / 1e9:.1f}GB"


async def main() -> int:
    client = ComfyClient(config.COMFY_URL)
    print(f"ComfyUI: {config.COMFY_URL}")
    try:
        await client.wait_until_ready(timeout=60)
    except Exception as exc:  # noqa: BLE001
        print(f"  ✗ 連不上：{exc}")
        return 1

    info = await client.object_info()
    nodes = set(info)
    print(f"  ✓ 就緒（{len(info)} 種節點）")
    for node in ("WanImageToVideo", "Wan22ImageToVideoLatent", "HunyuanVideo15ImageToVideo", "DualCLIPLoader"):
        print(f"  {'✓' if node in nodes else '✗'} {node}")
    print(f"  {'✓' if 'UnetLoaderGGUF' in nodes else '✗'} UnetLoaderGGUF（GGUF 量化模型）")
    video = [n for n in ("CreateVideo", "SaveVideo", "VHS_VideoCombine") if n in nodes]
    print(f"  影片輸出節點：{', '.join(video) or '只有 SaveAnimatedWEBP'}")

    manager = downloader.Manager(config.MODELS_DIR)
    print(f"\n模型目錄：{config.MODELS_DIR}")
    if not config.MODELS_DIR.is_dir():
        print("  ✗ 這個目錄不存在 —— 檢查 MODELS_DIR 或 docker compose 的掛載")
    else:
        # List what is actually on disk. When the app and ComfyUI disagree about
        # which files exist, this is the line that shows why.
        for folder in ("diffusion_models", "unet", "text_encoders", "vae", "clip_vision", "checkpoints"):
            here = sorted((config.MODELS_DIR / folder).glob("*")) if (config.MODELS_DIR / folder).is_dir() else []
            real = [f for f in here if f.is_file() and not f.name.startswith(".")]
            if real:
                print(f"  {folder}/")
                for f in real:
                    print(f"      {f.name}  {gb(f.stat().st_size)}")
    print(f"預設模型（設定）：{config.DEFAULT_MODEL}")

    failures = 0
    for model in registry.MODELS:
        state = manager.model_status(model)
        mark = "✓" if state["installed"] else ("◐" if state["partial"] else "·")
        print(f"\n  {mark} {model.label}")
        print(f"      顯存 {model.vram_gb}GB+ · 下載 {gb(model.download_bytes)} · 已有 {gb(state['bytes_on_disk'])}")
        if not state["installed"]:
            print(f"      缺 {len(state['missing'])} 個檔：{', '.join(state['missing'][:3])}")
            continue
        if not model.runnable:
            print("      （只提供檔案，用 ComfyUI 內建範例跑）")
            continue

        for lightning in ([False, True] if model.lightning else [False]):
            params = config.params_for(model, lightning=lightning)
            tier = config.default_tier(model)
            w, h = workflow.fit_dimensions(1024, 1024, tier, model)
            graph = workflow.build(
                model, params, image_name="placeholder.png", prompt="test",
                seed=1, width=w, height=h, available_nodes=nodes,
            )
            problems = await client.validate(graph)
            tag = "4 步加速" if lightning else "標準"
            if problems:
                failures += 1
                print(f"      ✗ 工作流程（{tag}）:")
                for p in problems:
                    print(f"          {p}")
            else:
                print(f"      ✓ 工作流程（{tag}）{len(graph)} 節點 · {w}x{h} · {params.steps} 步")

    loras = manager.list_loras()
    print(f"\nLoRA（{config.MODELS_DIR / 'loras'}）：{len(loras)} 個")
    for lora in loras[:8]:
        print(f"  · {lora['name']}{' [內建加速]' if lora['builtin'] else ''}")

    runnable_installed = [
        m for m in registry.runnable() if manager.model_status(m)["installed"]
    ]
    print()
    if not runnable_installed:
        print("還沒有可用的模型。開 http://127.0.0.1:8000 的「模型管理」下載一個。")
        return 1
    if failures:
        print(f"有 {failures} 個工作流程不相容，看上面的訊息。")
        return 1
    print(f"可以開始生成，{len(runnable_installed)} 個模型就緒。")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

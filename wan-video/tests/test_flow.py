"""Runs the whole pipeline against a fake ComfyUI. No GPU needed.

    python tests/test_flow.py
"""

from __future__ import annotations

import asyncio
import io
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from aiohttp import web  # noqa: E402
from fake_comfy import FakeComfy  # noqa: E402
from PIL import Image  # noqa: E402

failures: list[str] = []


def check(condition: bool, label: str) -> None:
    print(f"  {'✓' if condition else '✗'} {label}")
    if not condition:
        failures.append(label)


async def start_fake(fake: FakeComfy) -> tuple[web.AppRunner, str]:
    runner = web.AppRunner(fake.app())
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", 0)
    await site.start()
    port = runner.addresses[0][1]
    return runner, f"http://127.0.0.1:{port}"


def sample_png(size=(1024, 1536)) -> bytes:
    buf = io.BytesIO()
    Image.new("RGB", size, (120, 90, 160)).save(buf, "PNG")
    return buf.getvalue()


def node_of(graph: dict, class_type: str) -> list[dict]:
    return [n for n in graph.values() if n["class_type"] == class_type]


# -- pure functions ---------------------------------------------------------


def test_dimensions() -> None:
    import workflow

    print("\n[dimensions]")
    w, h = workflow.fit_dimensions(1024, 1536, "480p")
    check(w % 16 == 0 and h % 16 == 0, f"480p snaps to /16 ({w}x{h})")
    check(abs((w / h) - (1024 / 1536)) < 0.05, "aspect ratio preserved")
    check(0.7 < (w * h) / workflow.TIERS["480p"] < 1.4, "close to the 480p pixel budget")

    w7, h7 = workflow.fit_dimensions(1024, 1536, "720p")
    check(w7 * h7 > w * h, "720p is bigger than 480p")

    w2, h2 = workflow.fit_dimensions(64, 12000, "480p")
    check(w2 >= 16 and h2 >= 16, f"extreme aspect stays legal ({w2}x{h2})")

    print("\n[length]")
    check(workflow.normalize_length(81) == 81, "81 unchanged")
    check(workflow.normalize_length(80) == 77, "80 -> 77 (4n+1)")
    check(workflow.normalize_length(1) == 5, "clamped up to 5")
    check(workflow.normalize_length(9999) == 241, "clamped down to 241")
    check(all((workflow.normalize_length(n) - 1) % 4 == 0 for n in range(1, 300)), "always 4n+1")


def test_config() -> None:
    print("\n[config]")
    import importlib

    os.environ["LORAS"] = "a.safetensors:0.7, b.safetensors, c.safetensors:1.25"
    os.environ["PROFILE"] = "gguf"
    os.environ["GGUF_QUANT"] = "Q5_K_M"
    import config

    importlib.reload(config)
    s = config.settings()
    check(s.loader == "gguf", "gguf profile selects the GGUF loader")
    check("Q5_K_M" in s.high_noise, f"quant baked into filename ({s.high_noise})")
    check([l.strength for l in s.loras] == [0.7, 1.0, 1.25], "LoRA strengths parsed")
    check([l.name for l in s.loras][1] == "b.safetensors", "LoRA without strength defaults to 1.0")

    os.environ["PROFILE"] = "fp8"
    os.environ["LORAS"] = ""
    importlib.reload(config)
    check(config.settings().loader == "safetensors", "fp8 profile selects UNETLoader")


def test_lightning_preset() -> None:
    print("\n[lightning preset]")
    import workflow

    base = workflow.Settings(lightning=False, steps=20, cfg=3.5)
    check(base.resolved().steps == 20, "non-lightning keeps configured steps")

    lit = workflow.Settings(lightning=True, steps=20, cfg=3.5, shift=8.0)
    r = lit.resolved()
    check((r.steps, r.boundary, r.cfg, r.shift) == (4, 2, 1.0, 5.0), "lightning overrides sampler numbers")
    check(lit.steps == 20, "resolved() does not mutate the original")


# -- graph shape ------------------------------------------------------------


async def test_graph_valid() -> None:
    print("\n[graph vs live schema]")
    import workflow
    from comfy_client import ComfyClient

    fake = FakeComfy()
    runner, url = await start_fake(fake)
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()

        s = workflow.Settings(lightning=True, loras=[workflow.Lora("my_style.safetensors", 0.8)])
        graph = workflow.build(
            image_name="example.png",
            prompt="she turns her head",
            negative=workflow.DEFAULT_NEGATIVE,
            seed=42,
            width=832,
            height=480,
            settings=s,
            available_nodes=nodes,
        )
        problems = await client.validate(graph)
        check(problems == [], f"fp8 + lightning + LoRA graph validates ({problems})")

        samplers = node_of(graph, "KSamplerAdvanced")
        check(len(samplers) == 2, "two-stage sampling (high + low noise expert)")
        first, second = samplers
        check(first["inputs"]["add_noise"] == "enable", "stage 1 adds noise")
        check(second["inputs"]["add_noise"] == "disable", "stage 2 does not re-add noise")
        check(first["inputs"]["return_with_leftover_noise"] == "enable", "stage 1 hands off leftover noise")
        check(
            first["inputs"]["end_at_step"] == second["inputs"]["start_at_step"],
            "the two stages meet exactly at the boundary",
        )
        check(first["inputs"]["noise_seed"] == second["inputs"]["noise_seed"] == 42, "same seed both stages")
        check(first["inputs"]["cfg"] == 1.0 and first["inputs"]["steps"] == 4, "lightning numbers reached the sampler")

        loras = node_of(graph, "LoraLoaderModelOnly")
        check(len(loras) == 4, f"lightning + extra LoRA on both experts = 4 nodes (got {len(loras)})")
        names = {n["inputs"]["lora_name"] for n in loras}
        check("my_style.safetensors" in names, "extra LoRA present")
        check(any("high_noise" in n for n in names) and any("low_noise" in n for n in names),
              "correct lightning LoRA per expert")

        i2v = node_of(graph, "WanImageToVideo")[0]
        check(i2v["inputs"]["width"] == 832 and i2v["inputs"]["length"] == 81, "resolution/length wired in")
        check(isinstance(i2v["inputs"]["start_image"], list), "input image feeds start_image")

        save = node_of(graph, "SaveVideo")
        check(len(save) == 1, "SaveVideo used when available")

        # GGUF variant
        s2 = workflow.Settings(
            loader="gguf",
            high_noise="Wan2.2-I2V-A14B-HighNoise-Q4_K_M.gguf",
            low_noise="Wan2.2-I2V-A14B-LowNoise-Q4_K_M.gguf",
            lightning=False,
        )
        g2 = workflow.build(
            image_name="example.png", prompt="x", negative="y", seed=1,
            width=832, height=480, settings=s2, available_nodes=nodes,
        )
        check(await client.validate(g2) == [], "gguf graph validates")
        check(len(node_of(g2, "UnetLoaderGGUF")) == 2, "two GGUF loaders")
        check(node_of(g2, "LoraLoaderModelOnly") == [], "no LoRA nodes when lightning is off")
    finally:
        await runner.cleanup()


async def test_validator_catches_mistakes() -> None:
    print("\n[validator]")
    import workflow
    from comfy_client import ComfyClient

    fake = FakeComfy()
    runner, url = await start_fake(fake)
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()

        # A just-uploaded image is not in the cached /object_info listing, so the
        # validator must not reject it (this once broke every generation).
        fresh = workflow.build(
            image_name="wan-drop/uploaded-2s-ago.png", prompt="x", negative="y", seed=1,
            width=832, height=480, settings=workflow.Settings(), available_nodes=nodes,
        )
        check(await client.validate(fresh) == [], "freshly uploaded image name is accepted")

        bad_model = workflow.Settings(high_noise="does_not_exist.safetensors")
        graph = workflow.build(
            image_name="example.png", prompt="x", negative="y", seed=1,
            width=832, height=480, settings=bad_model, available_nodes=nodes,
        )
        problems = await client.validate(graph)
        check(any("does_not_exist" in p for p in problems), "missing model file is reported")

        bad_sampler = workflow.Settings(lightning=False, sampler="not_a_sampler")
        graph = workflow.build(
            image_name="example.png", prompt="x", negative="y", seed=1,
            width=832, height=480, settings=bad_sampler, available_nodes=nodes,
        )
        problems = await client.validate(graph)
        check(any("not_a_sampler" in p for p in problems), "invalid sampler name is reported")

        graph["1"]["class_type"] = "TotallyMadeUpNode"
        problems = await client.validate(graph)
        check(any("TotallyMadeUpNode" in p for p in problems), "unknown node class is reported")

        graph = workflow.build(
            image_name="example.png", prompt="x", negative="y", seed=1,
            width=832, height=480, settings=workflow.Settings(), available_nodes=nodes,
        )
        del graph["1"]["inputs"]["weight_dtype"]
        problems = await client.validate(graph)
        check(any("weight_dtype" in p for p in problems), "missing required input is reported")
    finally:
        await runner.cleanup()


async def test_video_node_fallback() -> None:
    print("\n[video output fallback]")
    import workflow
    from comfy_client import ComfyClient

    for available, expected in [
        ({"CreateVideo", "SaveVideo"}, "SaveVideo"),
        ({"VHS_VideoCombine"}, "VHS_VideoCombine"),
        (set(), "SaveAnimatedWEBP"),
    ]:
        fake = FakeComfy(video_nodes=available)
        runner, url = await start_fake(fake)
        try:
            client = ComfyClient(url)
            nodes = await client.node_classes()
            graph = workflow.build(
                image_name="example.png", prompt="x", negative="y", seed=1,
                width=832, height=480, settings=workflow.Settings(), available_nodes=nodes,
            )
            check(len(node_of(graph, expected)) == 1, f"{available or 'core only'} -> {expected}")
            check(await client.validate(graph) == [], f"{expected} graph validates")
        finally:
            await runner.cleanup()


# -- client behaviour -------------------------------------------------------


async def test_client_run() -> None:
    print("\n[client run]")
    import workflow
    from comfy_client import ComfyClient, ComfyError

    fake = FakeComfy()
    runner, url = await start_fake(fake)
    try:
        client = ComfyClient(url)
        name = await client.upload_image(sample_png((64, 64)), "job.png")
        check(name == "wan-drop/job.png", f"upload returns subfolder-qualified name ({name})")

        graph = workflow.build(
            image_name=name, prompt="x", negative="y", seed=7,
            width=832, height=480, settings=workflow.Settings(),
            available_nodes=await client.node_classes(),
        )
        seen: list[float] = []
        files = await client.run(graph, on_progress=seen.append)
        check(len(files) == 1, "picks exactly one output file")
        check(files[0].filename.endswith(".mp4"), "prefers the mp4 over the preview frame")
        check(seen == [0.25, 0.5, 0.75, 1.0], f"progress reported ({seen})")

        data = await client.download(files[0])
        check(data == fake.video_bytes, "downloaded bytes match")
    finally:
        await runner.cleanup()

    print("\n[client errors]")
    fake = FakeComfy(fail="execution_error")
    runner, url = await start_fake(fake)
    try:
        client = ComfyClient(url)
        graph = workflow.build(
            image_name="example.png", prompt="x", negative="y", seed=1,
            width=832, height=480, settings=workflow.Settings(),
            available_nodes=await client.node_classes(),
        )
        try:
            await client.run(graph)
            check(False, "execution_error should raise")
        except ComfyError as exc:
            check("CUDA out of memory" in str(exc), f"error surfaces the real message ({exc})")
    finally:
        await runner.cleanup()


# -- end to end through the HTTP API ---------------------------------------


async def test_server_end_to_end() -> None:
    print("\n[server end to end]")
    import aiohttp

    fake = FakeComfy()
    fake_runner, comfy_url = await start_fake(fake)

    root = Path(__file__).resolve().parents[1]
    data_dir = root / "tests" / ".tmp"
    env = {
        **os.environ,
        "COMFY_URL": comfy_url,
        "OUTPUT_DIR": str(data_dir / "outputs"),
        "INBOX_DIR": str(data_dir / "inbox"),
        "DONE_DIR": str(data_dir / "inbox" / "done"),
        "PROFILE": "fp8",
        "LIGHTNING": "true",
        "TIER": "480p",
        "LENGTH": "81",
        "PYTHONPATH": str(root / "app"),
        "LORAS": "",
    }
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "18421",
        cwd=str(root / "app"), env=env,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
    )
    base = "http://127.0.0.1:18421"
    try:
        async with aiohttp.ClientSession() as s:
            for _ in range(120):
                try:
                    async with s.get(f"{base}/api/health", timeout=5) as r:
                        if r.status == 200:
                            health = await r.json()
                            break
                except Exception:  # noqa: BLE001
                    await asyncio.sleep(0.25)
            else:
                out = await proc.stdout.read(4000)
                raise AssertionError(f"server never started:\n{out.decode(errors='replace')}")

            check(health["comfy"]["ok"], "health reports ComfyUI reachable")
            check(health["sampling"]["steps"] == 4, "health shows the lightning preset")

            async with s.get(f"{base}/", timeout=10) as r:
                html = await r.text()
            check(r.status == 200 and "把圖片拖進來" in html, "UI page serves")

            form = aiohttp.FormData()
            form.add_field("image", sample_png((1024, 1536)), filename="cat.png", content_type="image/png")
            form.add_field("prompt", "她慢慢轉頭")
            form.add_field("length", "80")
            form.add_field("seed", "-1")
            async with s.post(f"{base}/api/generate", data=form, timeout=30) as r:
                job = await r.json()
            check(r.status == 200, "generate accepted")
            check(job["length"] == 77, f"80 frames normalized to 77 ({job['length']})")
            check(job["seed"] >= 0, "random seed assigned")

            for _ in range(200):
                async with s.get(f"{base}/api/jobs/{job['id']}", timeout=10) as r:
                    job = await r.json()
                if job["status"] in ("done", "error"):
                    break
                await asyncio.sleep(0.1)
            check(job["status"] == "done", f"job completed ({job['status']}: {job['message']})")
            # 1024x1536 is 2:3; the 480p budget (832*480) lands it on 512x768.
            check(job["size"] == "512x768", f"portrait input keeps 2:3 aspect at 480p budget ({job['size']})")

            if job["output"]:
                async with s.get(f"{base}{job['output']}", timeout=30) as r:
                    body = await r.read()
                check(body == fake.video_bytes, "video served back over HTTP")

                async with s.get(f"{base}{job['thumb']}", timeout=30) as r:
                    check(r.status == 200, "thumbnail served")

            # The graph ComfyUI actually received.
            graph = fake.graphs[-1]
            i2v = node_of(graph, "WanImageToVideo")[0]
            check(i2v["inputs"]["length"] == 77, "normalized length reached ComfyUI")
            check(i2v["inputs"]["height"] == 768, "computed height reached ComfyUI")
            text = node_of(graph, "CLIPTextEncode")[0]["inputs"]["text"]
            check(text == "她慢慢轉頭", "Chinese prompt survives the round trip")
            check(node_of(graph, "LoadImage")[0]["inputs"]["image"].endswith(".png"), "uploaded image referenced")

            # Bad input should be rejected, not crash the worker.
            form = aiohttp.FormData()
            form.add_field("image", b"not an image", filename="x.png", content_type="image/png")
            async with s.post(f"{base}/api/generate", data=form, timeout=30) as r:
                check(r.status == 400, f"garbage upload rejected with 400 (got {r.status})")

            async with s.post(f"{base}/api/cancel", timeout=10) as r:
                check(r.status == 200 and fake.interrupts == 1, "cancel forwards to ComfyUI")

            async with s.get(f"{base}/outputs/../../etc/passwd", timeout=10) as r:
                check(r.status in (403, 404), f"path traversal blocked ({r.status})")
    finally:
        proc.terminate()
        await proc.wait()
        await fake_runner.cleanup()


async def test_watcher() -> None:
    print("\n[watcher]")
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
    import importlib

    tmp = Path(__file__).resolve().parent / ".tmp" / "watch"
    (tmp / "inbox").mkdir(parents=True, exist_ok=True)
    os.environ["INBOX_DIR"] = str(tmp / "inbox")
    os.environ["DONE_DIR"] = str(tmp / "inbox" / "done")
    import config

    importlib.reload(config)
    import watcher

    importlib.reload(watcher)

    img = tmp / "inbox" / "a_girl_turning_around.png"
    img.write_bytes(sample_png((64, 64)))
    check(watcher.prompt_for(img) == "a girl turning around", "filename becomes the prompt")

    img.with_suffix(".txt").write_text("鏡頭緩慢推近", encoding="utf-8")
    check(watcher.prompt_for(img) == "鏡頭緩慢推近", "sidecar .txt wins over the filename")

    # A name that carries no words at all (e.g. straight off a camera roll).
    empty = tmp / "inbox" / "___.png"
    empty.write_bytes(sample_png((64, 64)))
    check(watcher.prompt_for(empty) == watcher.PROMPT_DEFAULT, "falls back to the default prompt")

    check(watcher.IMAGE_SUFFIXES >= {".png", ".jpg", ".jpeg", ".webp"}, "common formats watched")


async def main() -> int:
    test_dimensions()
    test_config()
    test_lightning_preset()
    await test_graph_valid()
    await test_validator_catches_mistakes()
    await test_video_node_fallback()
    await test_client_run()
    await test_server_end_to_end()
    await test_watcher()

    print()
    if failures:
        print(f"FAILED ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("所有測試通過")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

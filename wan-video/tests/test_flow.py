"""Runs the whole pipeline against a fake ComfyUI and a fake Hugging Face.

    python3 tests/test_flow.py            # no GPU, no network, no weights
    COMFY_URL=http://127.0.0.1:8188 python3 tests/test_flow.py --live
                                          # also validate every graph against
                                          # a real ComfyUI at that URL
"""

from __future__ import annotations

import asyncio
import io
import json
import os
import random
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from aiohttp import web  # noqa: E402
from fake_civitai import FakeCivitai  # noqa: E402
from fake_comfy import FakeComfy  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

failures: list[str] = []
TMP = ROOT / "tests" / ".tmp"


def check(condition: bool, label: str) -> None:
    print(f"  {'✓' if condition else '✗'} {label}")
    if not condition:
        failures.append(label)


def section(name: str) -> None:
    print(f"\n[{name}]")


async def start(app: web.Application) -> tuple[web.AppRunner, str]:
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "127.0.0.1", 0).start()
    return runner, f"http://127.0.0.1:{runner.addresses[0][1]}"


def sample_png(size=(1024, 1536)) -> bytes:
    buf = io.BytesIO()
    Image.new("RGB", size, (120, 90, 160)).save(buf, "PNG")
    return buf.getvalue()


def nodes_of(graph: dict, class_type: str) -> list[dict]:
    return [n for n in graph.values() if n["class_type"] == class_type]


def install(root: Path, model, include_lightning=True) -> None:
    """Create correctly-sized sparse files so the manager sees the model as installed."""
    for f in model.all_files:
        if not include_lightning and f in model.lightning:
            continue
        path = root / f.folder / f.name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as fh:
            fh.truncate(f.size)


# -- registry ----------------------------------------------------------------


def test_registry() -> None:
    import registry

    section("registry")
    check(len(registry.MODELS) >= 7, f"{len(registry.MODELS)} models catalogued")
    check(len({m.id for m in registry.MODELS}) == len(registry.MODELS), "model ids unique")

    families = {m.family for m in registry.runnable()}
    check(families == {"wan22_14b", "wan22_5b", "hunyuan15"}, f"three runnable families ({families})")
    check(all(not m.runnable or m.tiers for m in registry.MODELS), "every runnable model has tiers")
    check(all(f.size > 0 for m in registry.MODELS for f in m.all_files), "every file has a real size")
    check(
        all(f.path.rsplit("/", 1)[-1] == f.name for m in registry.MODELS for f in m.all_files),
        "file names derive from repo paths",
    )
    for m in registry.runnable():
        folders = {f.folder for f in m.files}
        check("text_encoders" in folders, f"{m.id} ships a text encoder")
        check("vae" in folders, f"{m.id} ships a VAE")
        check(bool(folders & {"diffusion_models", "unet"}), f"{m.id} ships weights")

    hy = registry.get("hy15-720p")
    check("clip_vision" in {f.folder for f in hy.files}, "hunyuan ships clip_vision")
    check(registry.get("ltx23").family == "files_only", "LTX-2.3 is files-only")

    section("gen params")
    wan = registry.get("wan22-14b-fp8")
    base = registry.GenParams.defaults_for(wan, lightning=False)
    lit = registry.GenParams.defaults_for(wan, lightning=True)
    check((base.steps, base.cfg, base.shift) == (20, 3.5, 8.0), "wan base sampler numbers")
    check((lit.steps, lit.cfg, lit.shift, lit.boundary) == (4, 1.0, 5.0, 2), "lightning preset applied")
    hy_p = registry.GenParams.defaults_for(hy, lightning=True)
    check(not hy_p.lightning, "lightning ignored for models without the LoRAs")
    check(hy_p.cfg == 1.0 and hy_p.shift == 7.0, "hunyuan cfg-distilled numbers")
    check(registry.get("wan22-5b").sampler == "uni_pc", "wan 5B uses uni_pc per the official template")


def test_dimensions() -> None:
    import registry
    import workflow

    section("dimensions")
    wan = registry.get("wan22-14b-fp8")
    w, h = workflow.fit_dimensions(1024, 1536, "480p", wan)
    check(w % 16 == 0 and h % 16 == 0, f"snaps to /16 ({w}x{h})")
    check(abs((w / h) - (1024 / 1536)) < 0.05, "aspect preserved")
    w7, h7 = workflow.fit_dimensions(1024, 1536, "720p", wan)
    check(w7 * h7 > w * h, "720p larger than 480p")

    hy = registry.get("hy15-480p")
    wh, hh = workflow.fit_dimensions(1000, 1000, "480p", hy)
    check(abs(wh * hh - 848 * 480) / (848 * 480) < 0.25, f"hunyuan uses its own 848x480 budget ({wh}x{hh})")
    five = registry.get("wan22-5b")
    w5, h5 = workflow.fit_dimensions(1000, 1000, "704p", five)
    check(abs(w5 * h5 - 1280 * 704) / (1280 * 704) < 0.25, f"wan 5B uses 1280x704 ({w5}x{h5})")

    ew, eh = workflow.fit_dimensions(64, 12000, "480p", wan)
    check(ew >= 16 and eh >= 16, f"extreme aspect stays legal ({ew}x{eh})")

    section("length")
    check(workflow.normalize_length(81) == 81, "81 unchanged")
    check(workflow.normalize_length(80) == 77, "80 -> 77")
    check(workflow.normalize_length(1) == 5, "clamped up to 5")
    check(all((workflow.normalize_length(n) - 1) % 4 == 0 for n in range(1, 300)), "always 4n+1")


# -- graphs ------------------------------------------------------------------


async def test_graphs(base_url: str | None = None) -> None:
    import registry
    import workflow
    from comfy_client import ComfyClient

    label = "graphs vs real ComfyUI" if base_url else "graphs vs fake schema"
    section(label)

    runner = None
    if base_url is None:
        fake = FakeComfy()
        runner, base_url = await start(fake.app())
    client = ComfyClient(base_url)
    try:
        nodes = await client.node_classes()
        for model in registry.runnable():
            for lightning in ([False, True] if model.lightning else [False]):
                for tier in model.tiers:
                    p = registry.GenParams.defaults_for(model, lightning=lightning)
                    w, h = workflow.fit_dimensions(1024, 1536, tier, model)
                    g = workflow.build(
                        model, p, image_name="wan-drop/fresh.png", prompt="p",
                        seed=1, width=w, height=h, available_nodes=nodes,
                    )
                    problems = await client.validate(g)
                    tag = f"{model.id} {'4step' if lightning else 'base '} {tier}"
                    check(problems == [], f"{tag} validates" + ("" if not problems else f" {problems}"))

        # family-specific shape assertions
        wan = registry.get("wan22-14b-fp8")
        g = workflow.build(wan, registry.GenParams.defaults_for(wan, True),
                           image_name="i.png", prompt="p", seed=99, width=832, height=480,
                           available_nodes=nodes)
        samplers = nodes_of(g, "KSamplerAdvanced")
        check(len(samplers) == 2, "wan 14B samples in two stages")
        check(samplers[0]["inputs"]["end_at_step"] == samplers[1]["inputs"]["start_at_step"],
              "stages meet at the boundary")
        check(samplers[0]["inputs"]["add_noise"] == "enable" and samplers[1]["inputs"]["add_noise"] == "disable",
              "only the first stage adds noise")
        lit_names = {n["inputs"]["lora_name"] for n in nodes_of(g, "LoraLoaderModelOnly")}
        check(any("high" in n for n in lit_names) and any("low" in n for n in lit_names),
              "correct lightning LoRA per expert")

        five = registry.get("wan22-5b")
        g5 = workflow.build(five, registry.GenParams.defaults_for(five),
                            image_name="i.png", prompt="p", seed=1, width=832, height=480,
                            available_nodes=nodes)
        check(len(nodes_of(g5, "KSampler")) == 1, "wan 5B is single-stage")
        check(len(nodes_of(g5, "Wan22ImageToVideoLatent")) == 1, "wan 5B uses Wan22ImageToVideoLatent")
        check(nodes_of(g5, "VAELoader")[0]["inputs"]["vae_name"] == "wan2.2_vae.safetensors",
              "wan 5B uses the 2.2 VAE, not the 2.1 one")

        hy = registry.get("hy15-720p")
        ghy = workflow.build(hy, registry.GenParams.defaults_for(hy),
                             image_name="i.png", prompt="p", seed=1, width=848, height=480,
                             available_nodes=nodes)
        dual = nodes_of(ghy, "DualCLIPLoader")[0]["inputs"]
        check(dual["type"] == "hunyuan_video_15", "hunyuan dual encoder type")
        check("qwen" in dual["clip_name1"] and "byt5" in dual["clip_name2"],
              "qwen goes in slot 1, byt5 in slot 2")
        check(len(nodes_of(ghy, "CLIPVisionEncode")) == 1, "hunyuan encodes the image with SigLIP")
        i2v = nodes_of(ghy, "HunyuanVideo15ImageToVideo")[0]["inputs"]
        check(isinstance(i2v["clip_vision_output"], list), "vision embedding is wired into the latent node")

        # LoRAs applied to the single-model families too
        for mid in ("wan22-5b", "hy15-720p"):
            m = registry.get(mid)
            p = registry.GenParams.defaults_for(m)
            p.loras = [registry.Lora("wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors", 0.6)]
            g2 = workflow.build(m, p, image_name="i.png", prompt="p", seed=1,
                                width=832, height=480, available_nodes=nodes)
            check(len(nodes_of(g2, "LoraLoaderModelOnly")) == 1, f"{mid} accepts an extra LoRA")

        # files-only model must refuse rather than emit something broken
        try:
            ltx = registry.get("ltx23")
            workflow.build(ltx, registry.GenParams.defaults_for(ltx), image_name="i.png",
                           prompt="p", seed=1, width=512, height=512, available_nodes=nodes)
            check(False, "files-only model raises UnsupportedModel")
        except workflow.UnsupportedModel:
            check(True, "files-only model raises UnsupportedModel")
    finally:
        if runner:
            await runner.cleanup()


async def test_validator() -> None:
    import registry
    import workflow
    from comfy_client import ComfyClient

    section("validator")
    fake = FakeComfy()
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()
        model = registry.get("wan22-14b-fp8")
        p = registry.GenParams.defaults_for(model)

        # A just-uploaded image is not in the cached listing; must not be rejected.
        g = workflow.build(model, p, image_name="wan-drop/uploaded-2s-ago.png", prompt="p",
                           seed=1, width=832, height=480, available_nodes=nodes)
        check(await client.validate(g) == [], "freshly uploaded image name accepted")

        p_bad = registry.GenParams.defaults_for(model)
        p_bad.sampler = "not_a_sampler"
        g = workflow.build(model, p_bad, image_name="i.png", prompt="p", seed=1,
                           width=832, height=480, available_nodes=nodes)
        check(any("not_a_sampler" in x for x in await client.validate(g)), "bad sampler reported")

        g["1"]["class_type"] = "MadeUpNode"
        check(any("MadeUpNode" in x for x in await client.validate(g)), "unknown node reported")

        g = workflow.build(model, p, image_name="i.png", prompt="p", seed=1,
                           width=832, height=480, available_nodes=nodes)
        del g["1"]["inputs"]["weight_dtype"]
        check(any("weight_dtype" in x for x in await client.validate(g)), "missing required input reported")

    finally:
        await runner.cleanup()

    # An install that only has the fp8 model must reject a graph for a model
    # whose weights are not on disk, naming the file that is absent.
    partial = FakeComfy(installed={"wan22-14b-fp8"})
    runner, url = await start(partial.app())
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()
        q8 = registry.get("wan22-14b-q8")
        g = workflow.build(q8, registry.GenParams.defaults_for(q8), image_name="i.png",
                           prompt="p", seed=1, width=832, height=480, available_nodes=nodes)
        probs = await client.validate(g)
        check(any("Q8_0" in x for x in probs), f"not-yet-downloaded weights reported by name ({probs[:1]})")

        # Same story when the whole folder is empty rather than merely lacking
        # this one file, which is what a fresh install looks like.
        q4 = registry.get("wan22-14b-q4")
        g4 = workflow.build(q4, registry.GenParams.defaults_for(q4), image_name="i.png",
                            prompt="p", seed=1, width=832, height=480, available_nodes=nodes)
        check(any("Q4_K_M" in x for x in await client.validate(g4)),
              "empty model folder is reported, not silently accepted")

        fp8 = registry.get("wan22-14b-fp8")
        g_ok = workflow.build(fp8, registry.GenParams.defaults_for(fp8), image_name="i.png",
                              prompt="p", seed=1, width=832, height=480, available_nodes=nodes)
        check(await client.validate(g_ok) == [], "the installed model still validates")
    finally:
        await runner.cleanup()


async def test_video_fallback() -> None:
    import registry
    import workflow
    from comfy_client import ComfyClient

    section("video output fallback")
    model = registry.get("wan22-14b-fp8")
    for available, expected in [
        ({"CreateVideo", "SaveVideo"}, "SaveVideo"),
        ({"VHS_VideoCombine"}, "VHS_VideoCombine"),
        (set(), "SaveAnimatedWEBP"),
    ]:
        fake = FakeComfy(video_nodes=available)
        runner, url = await start(fake.app())
        try:
            client = ComfyClient(url)
            nodes = await client.node_classes()
            g = workflow.build(model, registry.GenParams.defaults_for(model), image_name="i.png",
                               prompt="p", seed=1, width=832, height=480, available_nodes=nodes)
            check(len(nodes_of(g, expected)) == 1, f"{available or 'core only'} -> {expected}")
            check(await client.validate(g) == [], f"{expected} graph validates")
        finally:
            await runner.cleanup()


# -- download manager --------------------------------------------------------


class FakeHF:
    """Serves byte payloads for registry file paths, with Range support."""

    def __init__(self, sizes: dict[str, int], fail_once: set[str] | None = None) -> None:
        self.sizes = sizes
        self.fail_once = fail_once or set()
        self.requests: list[tuple[str, str]] = []

    def app(self) -> web.Application:
        app = web.Application()
        app.router.add_get("/{tail:.*}", self.serve)
        return app

    async def serve(self, request: web.Request) -> web.StreamResponse:
        path = request.match_info["tail"]
        key = path.rsplit("/", 1)[-1]
        size = self.sizes.get(key)
        self.requests.append((key, request.headers.get("Range", "")))
        if size is None:
            raise web.HTTPNotFound()
        if key in self.fail_once:
            self.fail_once.discard(key)
            # Send half the promised body then kill the connection, the way a
            # real interrupted transfer behaves. Aborting the transport (rather
            # than raising) makes the client see a reset immediately instead of
            # waiting out its read timeout.
            resp = web.StreamResponse(status=200, headers={"Content-Length": str(size)})
            await resp.prepare(request)
            await resp.write(b"\0" * (size // 2))
            request.transport.abort()
            return resp

        start = 0
        rng = request.headers.get("Range")
        if rng and rng.startswith("bytes="):
            start = int(rng.split("=")[1].split("-")[0])
            if start >= size:
                raise web.HTTPRequestRangeNotSatisfiable()
        body = b"\0" * (size - start)
        status = 206 if start else 200
        headers = {"Content-Length": str(len(body))}
        if start:
            headers["Content-Range"] = f"bytes {start}-{size - 1}/{size}"
        return web.Response(status=status, body=body, headers=headers)


async def test_downloader() -> None:
    import downloader
    import registry

    section("download manager")
    root = TMP / "models"
    if root.exists():
        import shutil

        shutil.rmtree(root)
    root.mkdir(parents=True)

    # Shrink the catalogue to something a test can actually move.
    small = registry.ModelDef(
        id="test-model",
        label="Test model",
        family="wan22_5b",
        vram_gb=1,
        files=[
            registry.ModelFile("fake/repo", "split/a_weights.safetensors", "diffusion_models", 4096),
            registry.ModelFile("fake/repo", "split/a_te.safetensors", "text_encoders", 2048),
            registry.ModelFile("fake/repo", "split/a_vae.safetensors", "vae", 1024),
        ],
        tiers={"480p": (832, 480)},
    )
    sizes = {f.name: f.size for f in small.all_files}
    hf = FakeHF(sizes, fail_once={"a_te.safetensors"})
    runner, url = await start(hf.app())
    downloader.HF = url  # point the manager at the fake host
    try:
        manager = downloader.Manager(root)
        state = manager.model_status(small)
        check(not state["installed"] and state["bytes_on_disk"] == 0, "starts uninstalled")
        check(len(manager.missing_files(small)) == 3, "all three files missing")

        dl = manager.enqueue(small)
        for _ in range(400):
            if dl.status in ("done", "error", "cancelled"):
                break
            await asyncio.sleep(0.02)
        check(dl.status == "done", f"download completed ({dl.status}: {dl.message})")
        check(dl.done_bytes == dl.total == 7168, f"all bytes accounted for ({dl.done_bytes})")

        state = manager.model_status(small)
        check(state["installed"], "model reports installed afterwards")
        check(state["missing"] == [], "nothing missing")
        for f in small.files:
            path = root / f.folder / f.name
            check(path.is_file() and path.stat().st_size == f.size, f"{f.name} written at exact size")
            check(not path.with_suffix(path.suffix + ".part").exists(), f"{f.name} .part cleaned up")
        check(any(r[1].startswith("bytes=") for r in hf.requests), "resumed with a Range request after failure")

        # Re-enqueueing an installed model is a no-op that still reports done.
        again = manager.enqueue(small)
        check(again.status == "done" and manager.queue.qsize() == 0, "re-download of a complete model is a no-op")

        # A wrong-sized file on disk counts as partial, not installed.
        (root / "vae" / "a_vae.safetensors").write_bytes(b"\0" * 999)
        state = manager.model_status(small)
        check(not state["installed"] and state["partial"], "truncated file detected as partial")

        # 404 surfaces as an error rather than a hang.
        missing = registry.ModelDef(
            id="nope", label="Nope", family="wan22_5b", vram_gb=1,
            files=[registry.ModelFile("fake/repo", "split/not_there.safetensors", "vae", 512)],
            tiers={"480p": (832, 480)},
        )
        bad = manager.enqueue(missing)
        for _ in range(400):
            if bad.status in ("done", "error", "cancelled"):
                break
            await asyncio.sleep(0.02)
        check(bad.status == "error" and "404" in bad.message, f"404 becomes an error ({bad.message})")

        worker = manager.stop()
        check(worker is not None and not worker.done(), "worker task exposed for clean shutdown")
        worker.cancel()
    finally:
        await runner.cleanup()
        downloader.HF = "https://huggingface.co"

    section("lora listing")
    (root / "loras").mkdir(exist_ok=True)
    (root / "loras" / "my_nsfw_style.safetensors").write_bytes(b"x" * 10)
    (root / "loras" / "wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors").write_bytes(b"x" * 10)
    (root / "loras" / "notes.txt").write_text("ignored")
    manager = downloader.Manager(root)
    listed = manager.list_loras()
    check(len(listed) == 2, f"only .safetensors listed ({len(listed)})")
    check([l["name"] for l in listed][0] == "my_nsfw_style.safetensors", "sorted by name")
    check(next(l["builtin"] for l in listed if "lightx2v" in l["name"]), "built-in lightning LoRA flagged")
    check(not next(l["builtin"] for l in listed if "nsfw" in l["name"]), "user LoRA not flagged built-in")


# -- client ------------------------------------------------------------------


async def test_client() -> None:
    import registry
    import workflow
    from comfy_client import ComfyClient, ComfyError

    section("client")
    fake = FakeComfy()
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        name = await client.upload_image(sample_png((64, 64)), "job.png")
        check(name == "wan-drop/job.png", f"upload returns qualified name ({name})")

        model = registry.get("wan22-14b-fp8")
        g = workflow.build(model, registry.GenParams.defaults_for(model), image_name=name,
                           prompt="p", seed=7, width=832, height=480,
                           available_nodes=await client.node_classes())
        seen: list[float] = []
        files = await client.run(g, on_progress=seen.append)
        check(len(files) == 1 and files[0].filename.endswith(".mp4"), "picks the mp4, not the preview frame")
        check(seen == [0.25, 0.5, 0.75, 1.0], f"progress reported ({seen})")
        check(await client.download(files[0]) == fake.video_bytes, "bytes match")
    finally:
        await runner.cleanup()

    fake = FakeComfy(fail="execution_error")
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        model = registry.get("wan22-14b-fp8")
        g = workflow.build(model, registry.GenParams.defaults_for(model), image_name="i.png",
                           prompt="p", seed=1, width=832, height=480,
                           available_nodes=await client.node_classes())
        try:
            await client.run(g)
            check(False, "execution_error raises")
        except ComfyError as exc:
            check("CUDA out of memory" in str(exc), f"error surfaces the real message ({exc})")
    finally:
        await runner.cleanup()


# -- server end to end -------------------------------------------------------


async def test_server() -> None:
    import aiohttp
    import registry

    section("server end to end")
    fake = FakeComfy()
    comfy_runner, comfy_url = await start(fake.app())

    data_dir = TMP / "srv"
    models_dir = TMP / "srv-models"
    for model_id in ("wan22-14b-fp8", "hy15-720p"):
        install(models_dir, registry.get(model_id))
    (models_dir / "loras").mkdir(parents=True, exist_ok=True)
    (models_dir / "loras" / "spicy_style.safetensors").write_bytes(b"x" * 32)

    env = {
        **os.environ,
        "COMFY_URL": comfy_url,
        "MODELS_DIR": str(models_dir),
        "OUTPUT_DIR": str(data_dir / "outputs"),
        "INBOX_DIR": str(data_dir / "inbox"),
        "DONE_DIR": str(data_dir / "inbox" / "done"),
        "MODEL": "wan22-14b-fp8",
        "LIGHTNING": "true",
        "PYTHONPATH": str(ROOT / "app"),
        "LORAS": "",
    }
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "18422",
        cwd=str(ROOT / "app"), env=env,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
    )
    base = "http://127.0.0.1:18422"
    try:
        async with aiohttp.ClientSession() as s:
            for _ in range(160):
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

            check(health["comfy"]["ok"], "health sees ComfyUI")
            check(set(health["installed"]) == {"wan22-14b-fp8", "hy15-720p"},
                  f"health lists exactly the installed models ({health['installed']})")

            async with s.get(f"{base}/api/models") as r:
                cat = await r.json()
            by_id = {m["id"]: m for m in cat["models"]}
            check(len(cat["models"]) == len(registry.MODELS), "catalogue exposed")
            check(by_id["wan22-14b-fp8"]["installed"], "installed model flagged")
            check(not by_id["wan22-14b-q4"]["installed"], "uninstalled model flagged")
            check(by_id["wan22-14b-q4"]["missing"], "missing files listed")
            check(by_id["hy15-720p"]["supports_lightning"] is False, "hunyuan has no lightning")
            check(by_id["wan22-14b-fp8"]["supports_lightning"] is True, "wan 14B has lightning")
            check(by_id["ltx23"]["runnable"] is False, "LTX flagged not runnable")
            check(by_id["wan22-5b"]["tiers"] == ["480p", "704p"], "per-model tiers exposed")

            async with s.get(f"{base}/api/loras") as r:
                check("spicy_style.safetensors" in [l["name"] for l in (await r.json())["loras"]],
                      "user LoRA listed")

            async with s.get(f"{base}/") as r:
                html = await r.text()
            for tab in ("生成", "素材庫", "LoRA", "模型", "設定"):
                check(f'>{tab}' in html or f'>{tab}<' in html, f"UI has the {tab} tab")
            check("把圖片拖進來" in html, "UI serves the drop zone")

            # --- generate on the default model, with a LoRA
            form = aiohttp.FormData()
            form.add_field("image", sample_png((1024, 1536)), filename="cat.png", content_type="image/png")
            form.add_field("prompt", "她慢慢轉頭")
            form.add_field("model", "wan22-14b-fp8")
            form.add_field("length", "80")
            form.add_field("lightning", "1")
            form.add_field("loras", json.dumps([{"name": "spicy_style.safetensors", "strength": 0.65}]))
            async with s.post(f"{base}/api/generate", data=form) as r:
                job = await r.json()
                check(r.status == 200, f"generate accepted ({r.status})")
            check(job["length"] == 77, f"80 -> 77 frames ({job['length']})")
            check(job["lightning"] is True, "lightning honoured")

            for _ in range(300):
                async with s.get(f"{base}/api/jobs/{job['id']}") as r:
                    job = await r.json()
                if job["status"] in ("done", "error"):
                    break
                await asyncio.sleep(0.1)
            check(job["status"] == "done", f"job done ({job['status']}: {job['message']})")
            check(job["size"] == "512x768", f"2:3 input at 480p budget ({job['size']})")

            g = fake.graphs[-1]
            check(nodes_of(g, "CLIPTextEncode")[0]["inputs"]["text"] == "她慢慢轉頭", "Chinese prompt round-trips")
            check(nodes_of(g, "WanImageToVideo")[0]["inputs"]["length"] == 77, "length reached ComfyUI")
            lora_names = {n["inputs"]["lora_name"] for n in nodes_of(g, "LoraLoaderModelOnly")}
            check("spicy_style.safetensors" in lora_names, "picked LoRA reached ComfyUI")
            strengths = [n["inputs"]["strength_model"] for n in nodes_of(g, "LoraLoaderModelOnly")
                         if n["inputs"]["lora_name"] == "spicy_style.safetensors"]
            check(strengths == [0.65, 0.65], f"strength applied to both experts ({strengths})")
            check(len(nodes_of(g, "KSamplerAdvanced")) == 2, "two-stage graph submitted")

            # --- switch model mid-session
            form = aiohttp.FormData()
            form.add_field("image", sample_png((800, 800)), filename="b.png", content_type="image/png")
            form.add_field("prompt", "slow zoom")
            form.add_field("model", "hy15-720p")
            form.add_field("tier", "720p")
            async with s.post(f"{base}/api/generate", data=form) as r:
                job2 = await r.json()
            for _ in range(300):
                async with s.get(f"{base}/api/jobs/{job2['id']}") as r:
                    job2 = await r.json()
                if job2["status"] in ("done", "error"):
                    break
                await asyncio.sleep(0.1)
            check(job2["status"] == "done", f"hunyuan job done ({job2['status']}: {job2['message']})")
            g2 = fake.graphs[-1]
            check(len(nodes_of(g2, "HunyuanVideo15ImageToVideo")) == 1, "hunyuan graph submitted")
            check(len(nodes_of(g2, "DualCLIPLoader")) == 1, "hunyuan dual encoder used")
            check(job2["model_label"].startswith("HunyuanVideo"), "job records which model ran")

            # --- an uninstalled model is refused at the API boundary, so no
            # doomed job ever reaches the queue
            before = len((await (await s.get(f"{base}/api/jobs")).json())["jobs"])
            form = aiohttp.FormData()
            form.add_field("image", sample_png((512, 512)), filename="c.png", content_type="image/png")
            form.add_field("model", "wan22-14b-q4")
            async with s.post(f"{base}/api/generate", data=form) as r:
                status3, body3 = r.status, await r.json()
            check(status3 == 400, f"uninstalled model rejected with 400 (got {status3})")
            check("還沒下載完" in body3.get("detail", ""),
                  f"message explains what to do ({body3.get('detail','')[:50]})")
            after = len((await (await s.get(f"{base}/api/jobs")).json())["jobs"])
            check(after == before, "no job was queued for the uninstalled model")

            # --- files-only model refused at the API boundary
            form = aiohttp.FormData()
            form.add_field("image", sample_png((512, 512)), filename="d.png", content_type="image/png")
            form.add_field("model", "ltx23")
            async with s.post(f"{base}/api/generate", data=form) as r:
                check(r.status == 400, f"files-only model rejected with 400 ({r.status})")

            form = aiohttp.FormData()
            form.add_field("image", sample_png((512, 512)), filename="e.png", content_type="image/png")
            form.add_field("model", "no-such-model")
            async with s.post(f"{base}/api/generate", data=form) as r:
                check(r.status == 400, f"unknown model rejected with 400 ({r.status})")

            form = aiohttp.FormData()
            form.add_field("image", b"not an image", filename="x.png", content_type="image/png")
            async with s.post(f"{base}/api/generate", data=form) as r:
                check(r.status == 400, f"garbage upload rejected ({r.status})")

            async with s.get(f"{base}/outputs/../../etc/passwd") as r:
                check(r.status in (403, 404), f"path traversal blocked ({r.status})")

            async with s.post(f"{base}/api/cancel") as r:
                check(r.status == 200 and fake.interrupts == 1, "cancel forwards to ComfyUI")

            async with s.get(f"{base}/api/downloads") as r:
                check((await r.json())["current"] is None, "no download running")

            # --- gallery management: star, delete, stats, clear
            async with s.get(f"{base}/api/library/stats") as r:
                st = await r.json()
            check(st["count"] >= 2, f"library stats count videos ({st['count']})")
            check(st["bytes"] > 0, "library stats report bytes on disk")

            async with s.post(f"{base}/api/jobs/{job['id']}/star",
                              json={"value": True}) as r:
                check(r.status == 200 and (await r.json())["starred"], "star a job")
            async with s.get(f"{base}/api/jobs/{job['id']}") as r:
                check((await r.json())["starred"], "star persists in the record")

            async with s.post(f"{base}/api/library/clear", json={"keep_starred": True}) as r:
                cleared = (await r.json())["removed"]
            check(cleared >= 1, f"clear removed the unstarred jobs ({cleared})")
            async with s.get(f"{base}/api/jobs") as r:
                left = (await r.json())["jobs"]
            check([j["id"] for j in left] == [job["id"]], f"only the starred job survived ({len(left)})")

            async with s.delete(f"{base}/api/jobs/{job['id']}") as r:
                check(r.status == 200, "delete the starred job explicitly")
            async with s.get(f"{base}/api/jobs") as r:
                check((await r.json())["jobs"] == [], "library now empty")
            async with s.delete(f"{base}/api/jobs/nope") as r:
                check(r.status == 404, "deleting a missing job 404s")

            # --- VRAM is reported, and is advice rather than a gate
            async with s.get(f"{base}/api/models") as r:
                cat2 = await r.json()
            check("gpu" in cat2, "catalogue reports gpu info")
            for m in cat2["models"]:
                check("vram_advice" in m and "vram_note" in m,
                      f"{m['id']} carries vram advice") if m["id"] == "wan22-14b-fp8" else None
            big = next(m for m in cat2["models"] if m["id"] == "wan22-14b-fp8")
            check("跑得動" in big["vram_note"], "vram_note says a small card still runs")

            # --- CivitAI endpoints are wired up
            async with s.get(f"{base}/api/civitai/status") as r:
                cs = await r.json()
            check(cs["has_key"] is False, "no key configured in this test")
            check("Most Downloaded" in cs["sorts"], "sort options exposed")

            async with s.post(f"{base}/api/civitai/download",
                              json={"files": [{"url": "https://x/y", "name": "a.safetensors"}]}) as r:
                body = await r.json()
                check(r.status == 400 and "API key" in body.get("detail", ""),
                      f"lora download without a key 400s with a useful message ({r.status})")

            async with s.post(f"{base}/api/civitai/download",
                              json={"files": [{"url": "https://x/y", "name": "../evil.safetensors"}]}) as r:
                check(r.status == 400, "traversal in a lora filename is rejected")

            async with s.get(f"{base}/api/loras") as r:
                lr = await r.json()
            check("civitai_key" in lr, "lora listing reports key status")
            async with s.delete(f"{base}/api/loras/..%2F..%2Fetc%2Fpasswd") as r:
                check(r.status in (400, 404), f"lora delete blocks traversal ({r.status})")

            # --- the trap that bit in practice: MODEL names an uninstalled
            # model, so the UI must not preselect it and the API must refuse it
            # up front rather than queueing a job that can only fail.
            check(cat["default"] in ("wan22-14b-fp8", "hy15-720p"),
                  f"default is an installed model ({cat['default']})")
            check(cat["configured_default"] == "wan22-14b-fp8", "configured default still reported")
            check("models_dir" in cat, "catalogue reports which folder it reads")
    finally:
        proc.terminate()
        await proc.wait()
        await comfy_runner.cleanup()


async def test_uninstalled_model_is_refused_up_front() -> None:
    """With only hy15-480p on disk but MODEL=wan22-14b-fp8 configured."""
    import aiohttp
    import registry

    section("uninstalled default model")
    fake = FakeComfy(installed={"hy15-480p"})
    comfy_runner, comfy_url = await start(fake.app())

    models_dir = TMP / "only-hy"
    install(models_dir, registry.get("hy15-480p"))

    env = {
        **os.environ,
        "COMFY_URL": comfy_url,
        "MODELS_DIR": str(models_dir),
        "OUTPUT_DIR": str(TMP / "only-hy-out"),
        "INBOX_DIR": str(TMP / "only-hy-in"),
        "MODEL": "wan22-14b-fp8",          # configured but NOT installed
        "PYTHONPATH": str(ROOT / "app"),
        "LORAS": "",
    }
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "18423",
        cwd=str(ROOT / "app"), env=env,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
    )
    base = "http://127.0.0.1:18423"
    try:
        async with aiohttp.ClientSession() as s:
            for _ in range(160):
                try:
                    async with s.get(f"{base}/api/health", timeout=5) as r:
                        if r.status == 200:
                            break
                except Exception:  # noqa: BLE001
                    await asyncio.sleep(0.25)
            else:
                out = await proc.stdout.read(4000)
                raise AssertionError(f"server never started:\n{out.decode(errors='replace')}")

            async with s.get(f"{base}/api/models") as r:
                cat = await r.json()
            check(cat["default"] == "hy15-480p",
                  f"UI preselects the installed model, not the configured one ({cat['default']})")
            check(cat["configured_default"] == "wan22-14b-fp8", "configured default still visible")

            # asking for the uninstalled model must 400 with a useful message
            form = aiohttp.FormData()
            form.add_field("image", sample_png((1100, 1600)), filename="a.png", content_type="image/png")
            form.add_field("model", "wan22-14b-fp8")
            async with s.post(f"{base}/api/generate", data=form) as r:
                body = await r.json()
                status = r.status
            check(status == 400, f"uninstalled model refused with 400, not queued (got {status})")
            detail = body.get("detail", "")
            check("還沒下載完" in detail, f"message says it needs downloading ({detail[:40]})")
            check("「模型」分頁" in detail, f"message points at the model tab ({detail[-30:]})")
            check("wan2.2_i2v_high_noise" in detail, "message names a missing file")

            async with s.get(f"{base}/api/jobs") as r:
                check((await r.json())["jobs"] == [], "no doomed job was queued")

            # the installed model still works
            form = aiohttp.FormData()
            form.add_field("image", sample_png((1100, 1600)), filename="b.png", content_type="image/png")
            form.add_field("model", "hy15-480p")
            form.add_field("prompt", "slow pan")
            async with s.post(f"{base}/api/generate", data=form) as r:
                check(r.status == 200, f"installed model accepted ({r.status})")
                job = await r.json()
            for _ in range(300):
                async with s.get(f"{base}/api/jobs/{job['id']}") as r:
                    job = await r.json()
                if job["status"] in ("done", "error"):
                    break
                await asyncio.sleep(0.1)
            check(job["status"] == "done", f"hy15 job runs ({job['status']}: {job['message'][:80]})")
    finally:
        proc.terminate()
        await proc.wait()
        await comfy_runner.cleanup()


# -- text to image -----------------------------------------------------------


def test_image_registry() -> None:
    import images

    section("image models")
    check(len(images.IMAGE_MODELS) >= 4, f"{len(images.IMAGE_MODELS)} checkpoints catalogued")
    check(len({m.id for m in images.IMAGE_MODELS}) == len(images.IMAGE_MODELS), "ids unique")
    for m in images.IMAGE_MODELS:
        check(m.file.folder == "checkpoints", f"{m.id} installs into checkpoints/")
        check(m.file.size > 1e9, f"{m.id} has a real size ({m.file.size/1e9:.1f}GB)")
        check(bool(m.sizes), f"{m.id} offers sizes")
        check(bool(m.prompt_style), f"{m.id} explains how to prompt it")
        check(bool(m.negative), f"{m.id} ships a default negative prompt")
        check(-12 <= m.clip_skip <= -1, f"{m.id} clip skip in range ({m.clip_skip})")
        check(any(f.folder == "vae" for f in m.extra_files), f"{m.id} pairs an fp16 VAE")

    # The per-model knowledge that is the whole point of the catalogue.
    pony = images.get("pony")
    check(pony.positive_prefix.startswith("score_9"), "Pony gets its score_ tags")
    illus = images.get("illustrious")
    check(illus.clip_skip == -2, "Illustrious uses CLIP skip -2")
    jug = images.get("juggernaut")
    check(jug.clip_skip == -1 and not jug.positive_prefix, "photoreal model needs neither")

    for key in ("steps", "cfg", "sampler", "scheduler", "size", "batch", "seed", "clip_skip", "hires", "lora"):
        check(key in images.HELP and len(images.HELP[key]) > 10, f"help text for {key}")


async def test_image_graphs() -> None:
    import images
    from comfy_client import ComfyClient

    section("image graphs")
    fake = FakeComfy()
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()
        def settings(**kw) -> "images.ImageSettings":
            base = images.defaults_for(kw.pop("_model"))
            for key, value in kw.items():
                setattr(base, key, value)
            return base

        for model in images.IMAGE_MODELS:
            for hires in (0.0, 1.5):
                w, h = list(model.sizes.values())[0]
                g = images.build(
                    model,
                    settings(_model=model, batch=3, hires_scale=hires,
                             loras=[("my_style.safetensors", 0.8, 0.8)]),
                    prompt="p", negative="n", seed=1, width=w, height=h,
                    available_nodes=nodes,
                )
                problems = await client.validate(g)
                check(problems == [], f"{model.id} hires={hires} validates {problems[:1]}")

        model = images.get("illustrious")
        g = images.build(
            model,
            settings(_model=model, batch=4,
                     loras=[("a.safetensors", 0.6, 0.6), ("b.safetensors", 1.0, 0.4)]),
            prompt="p", negative="n", seed=7, width=832, height=1216, available_nodes=nodes,
        )
        check(len(nodes_of(g, "LoraLoader")) == 2, "two LoRAs chained")
        second = nodes_of(g, "LoraLoader")[1]["inputs"]
        check(second["strength_model"] == 1.0 and second["strength_clip"] == 0.4,
              "model and CLIP strengths stay independent")
        check(nodes_of(g, "EmptyLatentImage")[0]["inputs"]["batch_size"] == 4, "batch size wired")
        check(len(nodes_of(g, "CLIPSetLastLayer")) == 1, "clip skip -2 adds the node")
        check(nodes_of(g, "CLIPSetLastLayer")[0]["inputs"]["stop_at_clip_layer"] == -2, "…with -2")
        check(len(nodes_of(g, "KSampler")) == 1, "single pass without hires")

        g2 = images.build(
            images.get("juggernaut"), settings(_model=images.get("juggernaut")),
            prompt="p", negative="n", seed=1, width=1024, height=1024, available_nodes=nodes,
        )
        check(nodes_of(g2, "CLIPSetLastLayer") == [], "clip skip -1 omits the node entirely")

        g3 = images.build(
            model, settings(_model=model, hires_scale=1.5, hires_denoise=0.4),
            prompt="p", negative="n", seed=1, width=1024, height=1024, available_nodes=nodes,
        )
        ks = nodes_of(g3, "KSampler")
        check(len(ks) == 2, "hires adds a second sampler")
        check(ks[0]["inputs"]["denoise"] == 1.0 and ks[1]["inputs"]["denoise"] == 0.4,
              "second pass uses the hires denoise")
        up = nodes_of(g3, "LatentUpscale")[0]["inputs"]
        check(up["width"] == 1536 and up["width"] % 8 == 0, f"upscaled to a legal size ({up['width']})")

        check(nodes_of(g, "SaveImage")[0]["inputs"]["filename_prefix"].startswith("img/"),
              "images save under their own prefix")

        # -- image to image --------------------------------------------------
        g4 = images.build(
            model, settings(_model=model, denoise=0.55, batch=2),
            prompt="p", negative="n", seed=3, width=1024, height=1024,
            init_image="src.png", available_nodes=nodes,
        )
        check(await client.validate(g4) == [], "img2img validates")
        check(nodes_of(g4, "EmptyLatentImage") == [], "img2img starts from the picture, not noise")
        check(len(nodes_of(g4, "VAEEncode")) == 1, "the source is encoded once")
        check(nodes_of(g4, "RepeatLatentBatch")[0]["inputs"]["amount"] == 2,
              "a batch repeats the encoded latent")
        check(nodes_of(g4, "KSampler")[0]["inputs"]["denoise"] == 0.55,
              "denoise reaches the sampler in img2img")
        check(nodes_of(g4, "LoadImage")[0]["inputs"]["image"] == "src.png", "source wired in")

        g5 = images.build(
            model, settings(_model=model),
            prompt="p", negative="n", seed=1, width=1024, height=1024, available_nodes=nodes,
        )
        check(nodes_of(g5, "KSampler")[0]["inputs"]["denoise"] == 1.0,
              "text-to-image ignores denoise entirely")
    finally:
        await runner.cleanup()


async def test_controlnet() -> None:
    """Keeping a picture's composition while replacing what is in it.

    This is what makes panel restaging reproduce the *shot* and not just the
    rectangle, so the graph shape matters: one model load for a whole page, one
    hint per panel, and the conditioning actually reaching the sampler.
    """
    import comics
    import controlnets
    import images
    import server
    from comfy_client import ComfyClient

    section("controlnet")
    fake = FakeComfy()
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()
        model = images.get("illustrious")
        union = controlnets.get("union-promax")
        plain = controlnets.get("canny")
        check(union is not None and plain is not None, "the catalogue has both kinds")
        check(union.file.folder == "controlnet",
              f"ControlNets land where ComfyUI looks for them ({union.file.folder})")
        # Three repos all publish "diffusion_pytorch_model.safetensors"; without
        # a rename they would overwrite each other and the dropdown would be
        # three identical lines.
        names = [c.name for c in controlnets.CONTROLNETS]
        check(len(set(names)) == len(names), f"every ControlNet has its own filename ({names})")
        for c in controlnets.CONTROLNETS:
            check(c.name.endswith(".safetensors") and "diffusion_pytorch_model" not in c.name,
                  f"{c.id} is saved under a name that says what it is ({c.name})")
        check(all(c.union_type in controlnets.UNION_TYPES for c in controlnets.CONTROLNETS
                  if c.union_type),
              "every declared union type is one the node accepts")

        def settings(**kw):
            base = images.defaults_for(model)
            for key, value in kw.items():
                setattr(base, key, value)
            return base

        off = images.build(model, settings(), prompt="p", negative="n", seed=1,
                           width=1024, height=1024, available_nodes=nodes)
        check(nodes_of(off, "ControlNetLoader") == [], "ControlNet stays off by default")

        # Asked for but with no picture to follow: nothing to do, and above all
        # not a broken graph.
        armed = images.build(model, settings(controlnet=union.name), prompt="p",
                             negative="n", seed=1, width=1024, height=1024,
                             available_nodes=nodes)
        check(nodes_of(armed, "ControlNetLoader") == [],
              "a ControlNet with no reference picture adds nothing")

        g = images.build(
            model, settings(controlnet=union.name, controlnet_strength=0.7,
                            controlnet_end=0.65),
            prompt="p", negative="n", seed=1, width=832, height=1216,
            control_image="ref.png", available_nodes=nodes,
        )
        check(await client.validate(g) == [], "a ControlNet graph validates")
        check(len(nodes_of(g, "ControlNetLoader")) == 1, "the model is loaded once")
        check(nodes_of(g, "ControlNetLoader")[0]["inputs"]["control_net_name"] == union.name,
              "…by name")
        typed = nodes_of(g, "SetUnionControlNetType")
        check(len(typed) == 1 and typed[0]["inputs"]["type"] == union.union_type,
              f"a union model is told which control it is doing ({typed})")
        canny = nodes_of(g, "Canny")
        check(len(canny) == 1, "the reference is turned into outlines")
        fit = g[canny[0]["inputs"]["image"][0]]
        check(fit["class_type"] == "ImageScale"
              and (fit["inputs"]["width"], fit["inputs"]["height"]) == (832, 1216),
              f"…after being fitted to the panel it will guide ({fit['inputs']})")
        applied = nodes_of(g, "ControlNetApplyAdvanced")[0]["inputs"]
        check(applied["strength"] == 0.7 and applied["end_percent"] == 0.65,
              f"strength and end reach the node ({applied['strength']}, {applied['end_percent']})")
        # Both halves of the conditioning have to come back out of the apply
        # node - wiring only the positive silently halves the effect.
        sampler = nodes_of(g, "KSampler")[0]["inputs"]
        check(g[sampler["positive"][0]]["class_type"] == "ControlNetApplyAdvanced"
              and g[sampler["negative"][0]]["class_type"] == "ControlNetApplyAdvanced",
              "the sampler reads both conditionings through the ControlNet")
        check(sampler["positive"][1] == 0 and sampler["negative"][1] == 1,
              "…off the right output slots")

        # A hi-res pass that dropped the control would redraw the composition
        # away in its second pass, which is exactly what it must not do.
        hi = images.build(
            model, settings(controlnet=union.name, hires_scale=1.5),
            prompt="p", negative="n", seed=1, width=1024, height=1024,
            control_image="ref.png", available_nodes=nodes,
        )
        check(await client.validate(hi) == [], "hi-res plus ControlNet validates")
        for ks in nodes_of(hi, "KSampler"):
            check(hi[ks["inputs"]["positive"][0]]["class_type"] == "ControlNetApplyAdvanced",
                  "every pass keeps the composition, including the hi-res one")

        # A plain (non-union) model has no type input; setting one is invalid.
        p = images.build(model, settings(controlnet=plain.name), prompt="p", negative="n",
                         seed=1, width=1024, height=1024, control_image="ref.png",
                         available_nodes=nodes)
        check(await client.validate(p) == [], "a plain ControlNet graph validates")
        check(nodes_of(p, "SetUnionControlNetType") == [],
              "a single-purpose ControlNet is not given a union type")
        unknown = images.build(model, settings(controlnet="whatever_i_downloaded.safetensors"),
                               prompt="p", negative="n", seed=1, width=1024, height=1024,
                               control_image="ref.png", available_nodes=nodes)
        check(nodes_of(unknown, "SetUnionControlNetType") == [],
              "an unrecognised file is treated as plain, which is the safe guess")
        check(len(nodes_of(unknown, "ControlNetLoader")) == 1, "…but is still loaded")

        raw = images.build(model, settings(controlnet=plain.name, controlnet_preprocess="none"),
                           prompt="p", negative="n", seed=1, width=1024, height=1024,
                           control_image="ref.png", available_nodes=nodes)
        check(nodes_of(raw, "Canny") == [], "'none' hands the picture over untouched")

        # Out-of-range numbers come from a text box; they must be clamped, not
        # sent to ComfyUI to be rejected.
        wild = images.build(
            model,
            settings(controlnet=plain.name, controlnet_strength=99.0, controlnet_start=-3.0,
                     controlnet_end=8.0, controlnet_low=0.9, controlnet_high=0.2),
            prompt="p", negative="n", seed=1, width=1024, height=1024,
            control_image="ref.png", available_nodes=nodes,
        )
        check(await client.validate(wild) == [], "absurd ControlNet numbers still validate")
        a = nodes_of(wild, "ControlNetApplyAdvanced")[0]["inputs"]
        check(a["strength"] == 2.0 and a["start_percent"] == 0.0 and a["end_percent"] == 1.0,
              f"strength/start/end clamped ({a['strength']}, {a['start_percent']}, {a['end_percent']})")
        edge = nodes_of(wild, "Canny")[0]["inputs"]
        check(edge["high_threshold"] > edge["low_threshold"],
              f"a reversed threshold pair is straightened out ({edge})")

        # An older ComfyUI without these nodes must fall back, not produce a
        # graph referring to something that is not there.
        without = images.build(model, settings(controlnet=union.name), prompt="p",
                               negative="n", seed=1, width=1024, height=1024,
                               control_image="ref.png",
                               available_nodes=nodes - {"ControlNetApplyAdvanced"})
        check(nodes_of(without, "ControlNetLoader") == [],
              "no apply node means no ControlNet at all, rather than a dangling loader")
        no_union = images.build(model, settings(controlnet=union.name), prompt="p",
                                negative="n", seed=1, width=1024, height=1024,
                                control_image="ref.png",
                                available_nodes=nodes - {"SetUnionControlNetType"})
        check(len(nodes_of(no_union, "ControlNetLoader")) == 1
              and nodes_of(no_union, "SetUnionControlNetType") == [],
              "without the type node the union model is still used, just unhinted")

        # -- a whole page ----------------------------------------------------
        grid = comics.get("four-grid")
        page = [
            (f"panel {i}", *comics.panel_size(p, grid.aspect), f"ctrl-{i}.png")
            for i, p in enumerate(grid.panels)
        ]
        cg = images.build_comic(
            model, settings(controlnet=union.name), panels=page, negative="n", seed=5,
            available_nodes=nodes,
        )
        check(await client.validate(cg) == [], "a controlled page validates")
        check(len(nodes_of(cg, "ControlNetLoader")) == 1,
              f"2.5GB is loaded once for the page, not once per panel "
              f"({len(nodes_of(cg, 'ControlNetLoader'))})")
        check(len(nodes_of(cg, "SetUnionControlNetType")) == 1, "…and typed once")
        check(len(nodes_of(cg, "ControlNetApplyAdvanced")) == 4, "but applied per panel")
        used = [n["inputs"]["image"] for n in nodes_of(cg, "LoadImage")]
        check(used == [f"ctrl-{i}.png" for i in range(4)],
              f"each panel follows its own crop, in order ({used})")
        for i, ks in enumerate(nodes_of(cg, "KSampler")):
            check(cg[ks["inputs"]["positive"][0]]["class_type"] == "ControlNetApplyAdvanced",
                  f"panel {i + 1} is sampled through its own control")

        # A page where one crop was too small to keep: that panel goes
        # unguided, and the others must not shift onto the wrong reference.
        gap = [(t, w, h, "" if i == 1 else c) for i, (t, w, h, c) in enumerate(page)]
        cg2 = images.build_comic(model, settings(controlnet=union.name), panels=gap,
                                 negative="n", seed=5, available_nodes=nodes)
        check(await client.validate(cg2) == [], "a page with a missing crop validates")
        check(len(nodes_of(cg2, "ControlNetApplyAdvanced")) == 3, "three panels are guided")
        kept = [n["inputs"]["image"] for n in nodes_of(cg2, "LoadImage")]
        check(kept == ["ctrl-0.png", "ctrl-2.png", "ctrl-3.png"],
              f"…and they are still the right three ({kept})")
        second = nodes_of(cg2, "KSampler")[1]["inputs"]
        check(cg2[second["positive"][0]]["class_type"] == "CLIPTextEncode",
              "the unguided panel goes straight from its prompt to the sampler")

        # Panels are still allowed to be 3-tuples; every existing caller is one.
        old = images.build_comic(
            model, settings(controlnet=union.name),
            panels=[("a", 512, 768), ("b", 512, 768)], negative="n", seed=1,
            available_nodes=nodes,
        )
        check(await client.validate(old) == [], "a page with no crops at all validates")
        check(nodes_of(old, "ControlNetLoader") == [],
              "…and does not load a ControlNet it has nothing to feed")

        # -- the page that drives it -----------------------------------------
        html = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
        check("/api/controlnets" in html, "the UI asks the server which models are here")
        check("data-cn=" in html and "/api/controlnets/${encodeURIComponent(b.dataset.cn)}/download"
              in html, "…and can download one from the models tab")
        check("/api/comic/control/" in html,
              "each panel's reference is shown, not just counted")
        check("controls: payload.controlnet" in html,
              "the per-panel references are sent with a comic job")
        check("...controlPayload()" in html, "the ControlNet knobs ride along with every job")
        # Turning it on with nothing to follow is the one way to get a page that
        # silently ignores the setting, so it has to be refused in the browser.
        check("開了構圖鎖定" in html, "asking for control with no reference is explained")

        # -- what the upload actually tells you ------------------------------
        # There was no way to tell a successful upload from a dead button: the
        # file went in and nothing appeared until the analysis finished.
        check("已讀取 ${files.length} 頁" in html,
              "the uploaded pages are echoed back the moment they are picked")
        check("esc(f.name)" in html, "…by name")
        check('id="cpagefile" accept="image/*" multiple' in html,
              "several連貫的 pages can be picked at once")
        check("async function queueAllPages()" in html and "頁一起畫" in html,
              "…and queued as one job per page")
        check("await submitImage(true)" in html,
              "…through the same submit path a single press takes")

        # A measured layout must not be swappable for a different panel count
        # while the prompts and the reference crops still belong to the old one.
        check("COMIC.locked = { count: L.count" in html,
              "applying a measured page pins the layout to it")
        check("$('#clayout').disabled = !!lock" in html,
              "…so the panel-count picker cannot be changed behind it")
        check("id=\"cunlock\"" in html, "…with an explicit way out")
        check("CN.controls = []; $('#icn').value = ''" in html,
              "…which drops the crops, since they belong to the old rectangles")

        # -- the reason it looked completely broken --------------------------
        # Restaging needs a tagger (for the per-panel prompts) and a ControlNet
        # (for the composition). With neither, it measured rectangles and drew
        # whatever was in the shared prompt: four panels of the same thing,
        # unrelated to the uploaded page. It now says so before the upload.
        layouts = json.loads((await server.comic_layouts()).body)
        check("restage_ready" in layouts, "the server reports what restaging is missing")
        check(set(layouts["restage_ready"]) == {"tagger", "controlnet"},
              f"…both prerequisites ({layouts['restage_ready']})")
        check("function renderRestageReady()" in html,
              "the page warns about them before anything is uploaded")
        check("只會半套" in html, "…in words, not a silent degrade")
        check("內容和構圖都沒有" in html,
              "…and after applying, says plainly when nothing useful was produced")

        # -- getting back out ------------------------------------------------
        check("function clearRestage(" in html, "a restage can be cleared entirely")
        check('id="crsclear"' in html and 'id="cdrop"' in html,
              "…from the toolbar and from the lock banner")
        check("opt.remove()" in html,
              "…which takes the one-off layout back out of the picker")
        check("切回單張圖片：剛才那一頁的構圖鎖定已經關掉了" in html,
              "switching to single-image mode drops the page's crops, "
              "instead of refusing the next plain image for having no reference")

        # A feature nobody can find is not a feature.
        guide = ROOT / "docs" / "comic-restage.md"
        check(guide.is_file(), "the restage tutorial exists")
        text = guide.read_text(encoding="utf-8")
        check("docs/comic-restage.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
              "…and the README points at it")
        for topic in ("真人照片", "未成年", "ControlNet", "閱讀方向", "no_humans"):
            check(topic in text, f"the tutorial covers {topic}")
        for c in controlnets.CONTROLNETS:
            check(str(round(c.size / 1e9, 1)) in text or "2.5GB" in text,
                  "…and states the download size")
            break
    finally:
        await runner.cleanup()


async def test_image_extras() -> None:
    """The knobs added to catch up with (and pass) ComfyUI's own surface."""
    import images
    import prompts
    from comfy_client import ComfyClient

    section("image extras")
    fake = FakeComfy()
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()
        model = images.get("illustrious")

        def settings(**kw):
            base = images.defaults_for(model)
            for key, value in kw.items():
                setattr(base, key, value)
            return base

        # Quality patches chain onto the model, in order, and only when asked.
        plain = images.build(model, settings(), prompt="p", negative="n", seed=1,
                             width=1024, height=1024, available_nodes=nodes)
        for cls in ("FreeU_V2", "PerturbedAttentionGuidance", "RescaleCFG", "VAEDecodeTiled"):
            check(nodes_of(plain, cls) == [], f"{cls} stays off by default")

        patched = images.build(
            model, settings(freeu=True, pag=3.0, rescale_cfg=0.7, tiled_vae=True),
            prompt="p", negative="n", seed=1, width=1024, height=1024, available_nodes=nodes,
        )
        check(await client.validate(patched) == [], "patched graph validates")
        for cls in ("FreeU_V2", "PerturbedAttentionGuidance", "RescaleCFG"):
            check(len(nodes_of(patched, cls)) == 1, f"{cls} added once")
        check(nodes_of(patched, "PerturbedAttentionGuidance")[0]["inputs"]["scale"] == 3.0,
              "PAG scale wired")
        check(nodes_of(patched, "VAEDecode") == [] and len(nodes_of(patched, "VAEDecodeTiled")) == 1,
              "tiled decode replaces the plain one")
        sampler = nodes_of(patched, "KSampler")[0]["inputs"]["model"][0]
        check(patched[sampler]["class_type"] == "RescaleCFG",
              "the sampler reads the end of the patch chain, not the raw checkpoint")

        # A GAN upscaler, both as a hi-res step and as a plain enlargement.
        upscaled = images.build(
            model, settings(upscaler="4x-UltraSharp.pth"),
            prompt="p", negative="n", seed=1, width=1024, height=1024, available_nodes=nodes,
        )
        check(len(nodes_of(upscaled, "ImageUpscaleWithModel")) == 1, "final upscale added")
        saved = nodes_of(upscaled, "SaveImage")[0]["inputs"]["images"][0]
        check(upscaled[saved]["class_type"] == "ImageUpscaleWithModel",
              "SaveImage takes the upscaled image, not the raw decode")
        check(len(nodes_of(upscaled, "KSampler")) == 1, "a plain upscale runs no extra sampler")

        hires_model = images.build(
            model, settings(hires_scale=1.5, hires_upscaler="4x-UltraSharp.pth"),
            prompt="p", negative="n", seed=1, width=1024, height=1024, available_nodes=nodes,
        )
        check(nodes_of(hires_model, "LatentUpscale") == [],
              "a model upscaler replaces the latent upscale")
        check(len(nodes_of(hires_model, "ImageUpscaleWithModel")) == 1, "…with a real upscale")
        check(len(nodes_of(hires_model, "KSampler")) == 2, "…and still re-diffuses")

        # An install without the upscale nodes must still produce a graph.
        without = images.build(
            model, settings(hires_scale=1.5, hires_upscaler="4x-UltraSharp.pth",
                            upscaler="4x-UltraSharp.pth", tiled_vae=True),
            prompt="p", negative="n", seed=1, width=1024, height=1024,
            available_nodes={"CheckpointLoaderSimple", "CLIPTextEncode", "EmptyLatentImage",
                             "KSampler", "VAEDecode", "SaveImage", "LatentUpscale",
                             "CLIPSetLastLayer", "VAELoader"},
        )
        check(nodes_of(without, "ImageUpscaleWithModel") == [], "missing nodes are skipped")
        check(len(nodes_of(without, "LatentUpscale")) == 1, "…falling back to latent upscale")
        check(len(nodes_of(without, "VAEDecode")) == 1, "…and to the plain decode")

        # Wildcards: one prompt per image, stitched back into one batch.
        varied = [prompts.expand("a {red|blue} car", random.Random(i)) for i in range(4)]
        forked = images.build(
            model, settings(batch=4), prompt=varied, negative="n", seed=5,
            width=1024, height=1024, available_nodes=nodes,
        )
        check(await client.validate(forked) == [], "forked wildcard graph validates")
        if len(set(varied)) > 1:
            check(len(nodes_of(forked, "KSampler")) == len(varied),
                  "one sampler per distinct prompt")
            check(len(nodes_of(forked, "ImageBatch")) == len(varied) - 1,
                  "branches stitched back together")
            seeds = {n["inputs"]["seed"] for n in nodes_of(forked, "KSampler")}
            check(len(seeds) == len(varied), "each branch gets its own seed")
            texts = {n["inputs"]["text"] for n in nodes_of(forked, "CLIPTextEncode")}
            check(len(texts) >= len(set(varied)), "each branch encodes its own prompt")

        same = images.build(
            model, settings(batch=4), prompt=["x", "x", "x", "x"], negative="n", seed=5,
            width=1024, height=1024, available_nodes=nodes,
        )
        check(len(nodes_of(same, "KSampler")) == 1, "identical prompts stay one batched sampler")
        check(nodes_of(same, "EmptyLatentImage")[0]["inputs"]["batch_size"] == 4,
              "…using a batched latent")
    finally:
        await runner.cleanup()


async def test_new_endpoints() -> None:
    """The API surface added for the image page, exercised against a live app."""
    import aiohttp
    import images
    import registry

    section("new endpoints")
    fake = FakeComfy()
    comfy_runner, comfy_url = await start(fake.app())
    models_dir = TMP / "ep-models"
    install(models_dir, registry.get("wan22-14b-fp8"))
    for f in images.get("illustrious").all_files:
        path = models_dir / f.folder / f.name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as fh:
            fh.truncate(f.size)
    (models_dir / "loras").mkdir(parents=True, exist_ok=True)
    (models_dir / "loras" / "my_style.safetensors").write_bytes(b"\0" * 2048)
    (models_dir / "upscale_models").mkdir(parents=True, exist_ok=True)
    (models_dir / "upscale_models" / "4x-UltraSharp.pth").write_bytes(b"\0" * 512)

    env = {
        **os.environ,
        "COMFY_URL": comfy_url,
        "MODELS_DIR": str(models_dir),
        "OUTPUT_DIR": str(TMP / "ep-out"),
        "INBOX_DIR": str(TMP / "ep-in"),
        "STAGING_DIR": str(TMP / "ep-stage"),
        "MODEL": "wan22-14b-fp8",
        "PYTHONPATH": str(ROOT / "app"),
        "LORAS": "",
    }
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "18426",
        cwd=str(ROOT / "app"), env=env,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
    )
    base = "http://127.0.0.1:18426"
    try:
        async with aiohttp.ClientSession() as s:
            for _ in range(160):
                try:
                    async with s.get(f"{base}/api/health", timeout=5) as r:
                        if r.status == 200:
                            break
                except Exception:  # noqa: BLE001
                    await asyncio.sleep(0.25)
            else:
                out = await proc.stdout.read(4000)
                raise AssertionError(f"server never started:\n{out.decode(errors='replace')}")

            # -- upscaler / interpolator catalogues --------------------------
            async with s.get(f"{base}/api/upscalers") as r:
                cat = await r.json()
            ups = {u["name"]: u for u in cat["upscalers"]}
            check("4x-UltraSharp.pth" in ups and ups["4x-UltraSharp.pth"]["installed"],
                  "an installed upscaler reports installed")
            check(any(not u["installed"] for u in cat["upscalers"]),
                  "the rest are offered as downloads")
            check(len(cat["interpolators"]) >= 3, "interpolators are catalogued too")

            # -- wildcard preview --------------------------------------------
            async with s.post(f"{base}/api/prompt/preview",
                              json={"prompt": "a {red|blue|green} car", "count": 6}) as r:
                pv = await r.json()
            check(pv["has_wildcards"], "wildcards detected")
            check(len(pv["samples"]) == 6, "asked-for number of samples")
            check(len(set(pv["samples"])) > 1, "the samples actually differ")
            async with s.post(f"{base}/api/prompt/preview", json={"prompt": "a (cat:1.2 car"}) as r:
                check((await r.json())["warning"], "an unbalanced weight is reported, not thrown")

            # -- bad input is refused at the boundary ------------------------
            for payload, why in [
                ({"model": "illustrious", "prompt": "a (cat:1.2 x"}, "unbalanced weights"),
                ({"model": "illustrious", "prompt": "<lora:x:1> y"}, "inline lora syntax"),
                ({"model": "illustrious", "prompt": "x", "upscaler": "nope.pth"}, "missing upscaler"),
                ({"model": "illustrious", "prompt": "x", "hires_upscaler": "nope.pth"},
                 "missing hires upscaler"),
                ({"model": "illustrious", "prompt": "x", "init_image": "../../etc/passwd"},
                 "a traversal source path"),
                ({"model": "illustrious", "prompt": ""}, "an empty prompt with no source image"),
            ]:
                async with s.post(f"{base}/api/image/generate", json=payload) as r:
                    check(r.status == 400, f"{why} is refused ({r.status})")

            # -- image-to-image round trip -----------------------------------
            buf = io.BytesIO()
            Image.new("RGB", (900, 600), (30, 90, 160)).save(buf, "PNG")
            form = aiohttp.FormData()
            form.add_field("image", buf.getvalue(), filename="src.png", content_type="image/png")
            async with s.post(f"{base}/api/image/upload", data=form) as r:
                up = await r.json()
            check(r.status == 200 and up["width"] == 900, "a source image uploads and reports its size")

            async with s.post(f"{base}/api/image/generate", json={
                "model": "illustrious", "prompt": "x", "init_image": up["name"],
                "denoise": 0.5, "batch": 2,
            }) as r:
                job = await r.json()
            check(r.status == 200, f"img2img submits ({r.status})")
            check(job["settings"]["denoise"] == 0.5, "denoise is carried on the record")
            check(job["source"] == up["name"], "…along with which source it used")
            check((TMP / "ep-stage" / f"{job['id']}.png").is_file(),
                  "the source is copied under the job id, so a re-run still has it")

            # Deleting the job takes its source image with it. Wait for the job
            # to stop running first: a running job refuses deletion by design.
            for _ in range(80):
                async with s.get(f"{base}/api/jobs/{job['id']}") as r:
                    if (await r.json())["status"] in ("done", "error"):
                        break
                await asyncio.sleep(0.25)
            async with s.delete(f"{base}/api/jobs/{job['id']}") as r:
                check(r.status == 200, f"the finished job deletes ({r.status})")
            check(not (TMP / "ep-stage" / f"{job['id']}.png").is_file(),
                  "deleting the job cleans up its source image")

            # -- the prompt library --------------------------------------------
            collection = (
                "Prompt: 1girl, silver hair, gothic dress\n"
                "Negative: bad hands, blurry\n"
                "Tags: gothic\n\n"
                "Prompt: 2girls, bedroom, intimate\n"
                "Negative: bad anatomy\n"
            ).encode("utf-8")

            form = aiohttp.FormData()
            form.add_field("file", collection, filename="mine.txt",
                           content_type="text/plain")
            async with s.post(f"{base}/api/promptbook/preview", data=form) as r:
                pv = await r.json()
            check(r.status == 200 and pv["count"] == 2, f"preview parses ({r.status})")
            check(pv["new"] == 2 and pv["how"], "…reporting how it split and what is new")
            async with s.get(f"{base}/api/promptbook") as r:
                check((await r.json())["all"] == 0, "previewing saves nothing")

            check("entries" not in pv and pv.get("token"),
                  "preview returns a token, not the whole collection")
            async with s.post(f"{base}/api/promptbook/import",
                              json={"token": pv["token"]}) as r:
                done = await r.json()
            check(done["added"] == 2, f"import keeps them ({done})")
            # A token is single-use, so a double-click cannot import twice.
            async with s.post(f"{base}/api/promptbook/import",
                              json={"token": pv["token"]}) as r:
                check(r.status == 400, f"a spent token is refused ({r.status})")

            form = aiohttp.FormData()
            form.add_field("file", collection, filename="mine.txt",
                           content_type="text/plain")
            async with s.post(f"{base}/api/promptbook/preview", data=form) as r:
                pv2 = await r.json()
            check(pv2["new"] == 0, "the second preview sees them as already known")
            async with s.post(f"{base}/api/promptbook/import",
                              json={"token": pv2["token"]}) as r:
                again = await r.json()
            check(again["added"] == 0 and again["duplicate"] == 2,
                  "re-importing the same file adds nothing")

            async with s.get(f"{base}/api/promptbook?q=bedroom") as r:
                hits = await r.json()
            check(hits["total"] == 1, "search works over the library")
            entry_id = hits["entries"][0]["id"]
            async with s.post(f"{base}/api/promptbook/{entry_id}/star",
                              json={"starred": True}) as r:
                check(r.status == 200, "an entry can be starred")
            async with s.get(f"{base}/api/promptbook?starred=true") as r:
                check((await r.json())["total"] == 1, "…and filtered to")

            for name, body, why in [
                ("x.exe", b"MZ", "an unsupported extension"),
                ("x.txt", b"", "an empty file"),
            ]:
                form = aiohttp.FormData()
                form.add_field("file", body, filename=name, content_type="application/octet-stream")
                async with s.post(f"{base}/api/promptbook/preview", data=form) as r:
                    check(r.status == 400, f"{why} is refused ({r.status})")

            async with s.post(f"{base}/api/promptbook/import", json={"token": "nope"}) as r:
                check(r.status == 400, f"an unknown token is refused ({r.status})")

            async with s.delete(f"{base}/api/promptbook/source/mine.txt") as r:
                check((await r.json())["removed"] == 2, "a whole import can be undone")

            # -- restaging an existing page ------------------------------------
            import comics as comics_mod

            hero = comics_mod.get("hero-two")
            art_panels = [
                Image.new("RGB", comics_mod.panel_size(p, hero.aspect),
                          (40 + i * 60, 90, 160))
                for i, p in enumerate(hero.panels)
            ]
            page_png = io.BytesIO()
            comics_mod.compose(hero, art_panels,
                               style=comics_mod.PageStyle(width=900)).save(page_png, "PNG")

            form = aiohttp.FormData()
            form.add_field("page", page_png.getvalue(), filename="page.png",
                           content_type="image/png")
            async with s.post(f"{base}/api/comic/restage", data=form) as r:
                staged = await r.json()
            check(r.status == 200, f"restage answers ({r.status})")
            check(staged["layout"]["count"] == 3,
                  f"the page's 3 panels are recovered ({staged['layout']['count']})")
            check(staged["layout"]["confidence"] > 0.8, "…confidently")
            # No tagger installed in this fixture: the layout still comes back.
            check(staged["tagger_error"], "a missing tagger is explained")
            check(len(staged["panels"]) == 3, "…and there is still a slot per panel")

            # The measured rectangles must be usable as a layout.
            async with s.post(f"{base}/api/comic/preview", json={
                "layout": "custom", "custom_panels": staged["layout"]["panels"],
                "custom_aspect": 2 / 3,
            }) as r:
                png = await r.read()
            check(r.status == 200 and png[:8] == b"\x89PNG\r\n\x1a\n",
                  f"a measured layout previews ({r.status})")

            async with s.post(f"{base}/api/comic/generate", json={
                "model": "illustrious", "layout": "custom",
                "custom_panels": staged["layout"]["panels"], "custom_aspect": 2 / 3,
                "panels": ["a", "b", "c"], "shared": "1girl", "seed": 3,
            }) as r:
                job = await r.json()
            check(r.status == 200 and job["length"] == 3,
                  f"…and generates ({r.status}, {job.get('length')})")
            check(len(job["settings"]["custom_panels"]) == 3,
                  "the rectangles are stored on the record for a re-run")

            for payload, why in [
                ({"model": "illustrious", "layout": "custom", "custom_panels": [],
                  "panels": ["a"]}, "a custom layout with no rectangles"),
            ]:
                async with s.post(f"{base}/api/comic/generate", json=payload) as r:
                    check(r.status == 400, f"{why} is refused ({r.status})")

            form = aiohttp.FormData()
            form.add_field("page", b"not an image", filename="x.png",
                           content_type="image/png")
            async with s.post(f"{base}/api/comic/restage", data=form) as r:
                check(r.status == 400, f"a non-image page is refused ({r.status})")

            # -- inspecting an image -------------------------------------------
            async with s.get(f"{base}/api/taggers") as r:
                tg = await r.json()
            check(len(tg["taggers"]) >= 3, "taggers are offered for download")
            check(not any(t["installed"] for t in tg["taggers"]),
                  "none installed in this fixture")

            from PIL.PngImagePlugin import PngInfo
            settings = images.defaults_for(images.get("illustrious"))
            settings.loras = [("my_style.safetensors", 0.85, 0.5),
                              ("absent_v2.safetensors", 0.7, 0.7)]
            graph = images.build(
                images.get("illustrious"), settings, prompt="1girl, pink dress",
                negative="bad hands", seed=4242, width=832, height=1216,
            )
            meta = PngInfo()
            meta.add_text("prompt", json.dumps(graph))
            buf = io.BytesIO()
            Image.new("RGB", (128, 128), (60, 20, 40)).save(buf, "PNG", pnginfo=meta)

            form = aiohttp.FormData()
            form.add_field("image", buf.getvalue(), filename="a.png", content_type="image/png")
            async with s.post(f"{base}/api/inspect", data=form) as r:
                got = await r.json()
            check(r.status == 200, f"inspect answers ({r.status})")
            check(got["metadata"]["source"] == "comfyui", "the graph is read out of the file")
            check(got["metadata"]["prompt"] == "1girl, pink dress", "…exactly")
            check(got["metadata"]["seed"] == 4242, "…seed included")
            by_name = {l["name"]: l for l in got["loras"]}
            check(by_name["my_style.safetensors"]["installed"],
                  "a LoRA we have is marked as had")
            check(not by_name["absent_v2.safetensors"]["installed"],
                  "one we lack is marked as missing")
            check("civitai.com" in by_name["absent_v2.safetensors"]["search"],
                  "…with somewhere to go and get it")
            # No tagger installed here: that must degrade to a message, not a 500,
            # and must not stop the exact half from being returned.
            check(got["tags"] is None and got["tagger_error"],
                  f"a missing tagger is explained, not thrown ({got['tagger_error'][:40]})")

            plain = io.BytesIO()
            Image.new("RGB", (64, 64), (10, 10, 10)).save(plain, "PNG")
            form = aiohttp.FormData()
            form.add_field("image", plain.getvalue(), filename="b.png", content_type="image/png")
            async with s.post(f"{base}/api/inspect", data=form) as r:
                bare = await r.json()
            check(r.status == 200 and bare["metadata"]["source"] == "",
                  "an image with no metadata claims nothing")
            check(bare["loras"] == [], "…and invents no LoRAs")

            form = aiohttp.FormData()
            form.add_field("image", b"not an image", filename="c.png", content_type="image/png")
            async with s.post(f"{base}/api/inspect", data=form) as r:
                check(r.status == 400, f"a non-image is refused ({r.status})")

            # -- comics --------------------------------------------------------
            async with s.get(f"{base}/api/comic/layouts") as r:
                cat = await r.json()
            check(len(cat["layouts"]) >= 8, "layouts are offered")
            check(all(len(l["panels"]) == l["count"] for l in cat["layouts"]),
                  "each layout reports as many rectangles as panels")

            async with s.post(f"{base}/api/comic/preview", json={
                "layout": "4koma", "gutter": 18, "border": 5,
                "bubbles": [[{"text": "早安", "at": "top-left"}], [], [], []],
            }) as r:
                png = await r.read()
            check(r.status == 200 and png[:8] == b"\x89PNG\r\n\x1a\n",
                  f"the layout preview renders a PNG ({r.status})")
            preview = Image.open(io.BytesIO(png))
            check(preview.height > preview.width * 2,
                  f"…with 4koma's tall page shape {preview.size}")

            for payload, why in [
                ({"model": "illustrious", "layout": "nope", "panels": ["x"]}, "an unknown layout"),
                ({"model": "illustrious", "layout": "four-grid", "panels": ["", "", "", ""]},
                 "a page with nothing in it"),
                ({"model": "illustrious", "layout": "four-grid", "panels": ["a (b:1.2 c"]},
                 "a broken weight in a panel"),
            ]:
                async with s.post(f"{base}/api/comic/generate", json=payload) as r:
                    check(r.status == 400, f"{why} is refused ({r.status})")

            async with s.post(f"{base}/api/comic/generate", json={
                "model": "illustrious", "layout": "four-grid",
                "shared": "1girl, red dress",
                "panels": ["wide shot", "close-up", "from above", "smiling"],
                "bubbles": [[{"text": "早安", "at": "top-left"}], [], [], []],
                "full_color": True, "seed": 11, "steps": 6,
            }) as r:
                job = await r.json()
            check(r.status == 200, f"a comic submits ({r.status})")
            check(job["kind"] == "comic", "…as a comic record")
            check(job["length"] == 4, "…knowing how many panels it has")
            check("monochrome" in job["negative"],
                  "…with full colour enforced through the negative prompt")
            check(job["settings"]["layout"] == "four-grid" and
                  len(job["settings"]["panels"]) == 4,
                  "…and the panels stored for a re-run")

            async with s.post(f"{base}/api/comic/generate", json={
                "model": "illustrious", "layout": "two-v", "panels": ["a", "b"],
                "full_color": False,
            }) as r:
                grey = await r.json()
            check("monochrome" not in grey["negative"],
                  "black-and-white pages stop excluding monochrome")

            # -- LoRA previews -----------------------------------------------
            async with s.get(f"{base}/api/loras") as r:
                before = {l["name"]: l for l in (await r.json())["loras"]}
            check(before["my_style.safetensors"]["preview"] is False, "no preview to start with")

            cover = io.BytesIO()
            Image.new("RGB", (800, 800), (200, 40, 90)).save(cover, "PNG")
            form = aiohttp.FormData()
            form.add_field("image", cover.getvalue(), filename="c.png", content_type="image/png")
            async with s.post(f"{base}/api/loras/my_style.safetensors/preview/upload",
                              data=form) as r:
                check(r.status == 200, f"a cover can be uploaded ({r.status})")
            async with s.get(f"{base}/api/loras") as r:
                after = {l["name"]: l for l in (await r.json())["loras"]}
            check(after["my_style.safetensors"]["preview"] is True, "…and is then reported")
            async with s.get(f"{base}/api/loras/my_style.safetensors/preview") as r:
                blob = await r.read()
            check(r.status == 200 and blob[:2] == b"\xff\xd8", "…and served back as a JPEG")
            check(Image.open(io.BytesIO(blob)).size[0] <= 512, "…downscaled, not stored full size")

            for bad in ("..%2F..%2Fetc%2Fpasswd", "nope.safetensors"):
                async with s.get(f"{base}/api/loras/{bad}/preview") as r:
                    check(r.status in (400, 404), f"preview for {bad} refused ({r.status})")

            # Deleting the LoRA takes the preview with it.
            async with s.delete(f"{base}/api/loras/my_style.safetensors") as r:
                await r.read()
            check(not (models_dir / "loras" / "my_style.safetensors.preview.jpg").exists(),
                  "deleting a LoRA removes its preview too")
    finally:
        proc.terminate()
        await proc.wait()
        await comfy_runner.cleanup()


async def test_video_post() -> None:
    """Interpolation and upscaling ride on the decoded frames, after sampling."""
    import registry
    import upscalers
    import workflow
    from comfy_client import ComfyClient

    section("video post-processing")
    fake = FakeComfy()
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()
        model = registry.get("wan22-14b-fp8")

        def graph(**kw):
            p = registry.GenParams.defaults_for(model)
            for k, v in kw.items():
                setattr(p, k, v)
            return p, workflow.build(
                model, p, image_name="i.png", prompt="p", seed=1,
                width=832, height=480, available_nodes=nodes,
            )

        _, plain = graph()
        check(nodes_of(plain, "FrameInterpolate") == [], "no interpolation by default")
        check(nodes_of(plain, "ImageUpscaleWithModel") == [], "no upscale by default")

        _, both = graph(interpolate=2, interpolate_model="rife_v4.26.safetensors",
                        upscaler="4x-UltraSharp.pth")
        check(await client.validate(both) == [], "post-processed video graph validates")
        check(len(nodes_of(both, "FrameInterpolate")) == 1, "interpolation added")
        check(nodes_of(both, "FrameInterpolate")[0]["inputs"]["multiplier"] == 2, "…with the multiplier")
        check(len(nodes_of(both, "ImageUpscaleWithModel")) == 1, "upscale added")

        # Order matters for cost: interpolate the small frames, then enlarge.
        up = nodes_of(both, "ImageUpscaleWithModel")[0]["inputs"]["image"][0]
        check(both[up]["class_type"] == "FrameInterpolate",
              "upscale runs on the interpolated frames, not the other way round")

        # Doubling the frames over the same seconds is a higher frame rate.
        save = (nodes_of(both, "CreateVideo") or nodes_of(both, "SaveAnimatedWEBP"))[0]
        check(save["inputs"]["fps"] == model.fps * 2, "the save node is told the new fps")
        _, once = graph(interpolate=1, interpolate_model="rife_v4.26.safetensors")
        save1 = (nodes_of(once, "CreateVideo") or nodes_of(once, "SaveAnimatedWEBP"))[0]
        check(save1["inputs"]["fps"] == model.fps, "…and left alone when off")

        # An install without the nodes still produces a runnable graph.
        _, bare = graph(interpolate=2, interpolate_model="x.safetensors",
                        upscaler="4x-UltraSharp.pth")
        bare = workflow.build(
            model, registry.GenParams.defaults_for(model), image_name="i.png", prompt="p",
            seed=1, width=832, height=480,
            available_nodes=nodes - {"FrameInterpolate", "ImageUpscaleWithModel"},
        )
        check(nodes_of(bare, "FrameInterpolate") == [], "missing nodes are skipped, not crashed on")

        check({u.file.folder for u in upscalers.UPSCALERS} == {"upscale_models"},
              "upscalers land where ComfyUI looks for them")
        check({i.file.folder for i in upscalers.INTERPOLATORS} == {"frame_interpolation"},
              "interpolators land where ComfyUI looks for them")
    finally:
        await runner.cleanup()


def test_promptbook() -> None:
    """Importing a collection of prompt examples in whatever shape it arrives."""
    import zipfile

    import promptbook as pb

    section("prompt library")

    def parse(text, name="x.txt"):
        return pb.parse(text.encode("utf-8") if isinstance(text, str) else text, name)

    # -- one prompt per line, no blank lines. The nastiest case: joining these
    # into one entry is the worst possible outcome, and used to happen.
    got = parse("1girl, long hair, school uniform, sitting\n"
                "2girls, beach, swimsuit, summer\n"
                "solo, cat ears, maid outfit, indoors\n")
    check(len(got.entries) == 3, f"a tag dump splits per line ({len(got.entries)})")
    check(all("\n" not in e.positive for e in got.entries), "…without gluing lines together")

    # A prompt genuinely wrapped over lines must NOT be split.
    wrapped = parse("masterpiece, best quality,\n1girl, long hair,\noutdoors\n")
    check(len(wrapped.entries) == 1,
          f"a trailing comma means the prompt continues ({len(wrapped.entries)})")

    # -- blank-line blocks with titles
    got = parse("校園場景\n1girl, school uniform, classroom, sitting at desk\n\n"
                "海邊\n2girls, bikini, beach, ocean, sunset\n")
    check(len(got.entries) == 2, "blank lines separate entries")
    check(got.entries[0].title == "校園場景", f"a short first line is a title ({got.entries[0].title})")
    check("1girl" in got.entries[0].positive and "校園場景" not in got.entries[0].positive,
          "…and is not left inside the prompt")

    # -- labelled
    got = parse("Prompt: 1girl, silver hair, gothic dress\n"
                "Negative: bad hands, blurry\n"
                "Tags: gothic, portrait\n\n"
                "Prompt: 2girls, bedroom, intimate\n"
                "Negative: bad anatomy\n")
    check(len(got.entries) == 2, "Prompt:/Negative: pairs split into entries")
    check(got.entries[0].negative == "bad hands, blurry", "the negative is kept apart")
    check(got.entries[0].tags == ["gothic", "portrait"], "tags are split")
    check(got.how.startswith("標籤式"), f"and it says how it split ({got.how})")

    # -- A1111 blocks, reusing the image inspector's parser
    got = parse("masterpiece, 1girl, standing\n"
                "Negative prompt: bad hands, blurry\n"
                "Steps: 28, Sampler: DPM++ 2M, CFG scale: 7, Seed: 1, Size: 832x1216, "
                "Model: illustriousXL\n\n"
                "score_9, 1girl, bedroom\n"
                "Negative prompt: score_4\n"
                "Steps: 30, Sampler: Euler a, CFG scale: 6, Seed: 2, Size: 832x1216, "
                "Model: ponyV6\n")
    check(len(got.entries) == 2, "pasted A1111 blocks split into entries")
    check(got.entries[0].negative == "bad hands, blurry", "…keeping the negative")
    check("illustriousXL" in got.entries[0].note and "28" in got.entries[0].note,
          f"…and noting the settings ({got.entries[0].note})")

    # -- markdown, separators, json, jsonl, csv
    got = parse("# 校園\n\n```\n1girl, school uniform, classroom\n```\n\n"
                "## 泳裝\n\n```\n1girl, swimsuit, poolside, summer\n```\n", "b.md")
    check(len(got.entries) == 2 and got.entries[0].title == "校園",
          "markdown headings + fenced blocks")

    got = parse("1girl, library, glasses\n---\n1girl, kitchen, apron\n---\n2girls, park, picnic\n")
    check(len(got.entries) == 3, "--- separates entries")

    payload = json.dumps([
        {"title": "A", "prompt": "1girl, red dress, city", "negative": "bad hands",
         "tags": ["urban"]},
        {"title": "B", "positive": "2girls, forest, armor", "negative": "blurry"},
    ], ensure_ascii=False)
    got = parse(payload, "p.json")
    check(len(got.entries) == 2, "a JSON array imports")
    check(got.entries[0].tags == ["urban"] and got.entries[1].positive.startswith("2girls"),
          "…reading both `prompt` and `positive` spellings")

    got = parse('{"prompt":"1girl, cafe, coffee"}\n{"prompt":"1boy, rain, umbrella"}\n', "d.jsonl")
    check(len(got.entries) == 2, "JSONL imports")

    got = parse('title,prompt,negative,tags\n'
                '甲,"1girl, kimono, festival","bad hands","japanese,festival"\n'
                '乙,"2girls, gym, sportswear","blurry","sport"\n', "s.csv")
    check(len(got.entries) == 2 and got.entries[0].title == "甲", "a CSV with headers imports")
    check(got.entries[0].tags == ["japanese", "festival"], "…splitting the tags column")

    # A headerless CSV takes the longest cell as the prompt.
    got = parse("1,\"1girl, red dress, standing\",note\n2,\"2girls, beach, summer\",note\n", "n.csv")
    check(len(got.entries) == 2, "a headerless CSV still imports")
    check(got.entries[0].positive.startswith("1girl"), "…picking the prompt column")

    # -- .docx, read with the standard library only
    buf = io.BytesIO()
    ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    paras = ["提詞範例集", "1girl, maid outfit, cafe, serving", "",
             "1girl, nurse uniform, hospital, night", "", "2girls, office, suit, evening"]
    body = "".join(f"<w:p><w:r><w:t>{p}</w:t></w:r></w:p>" for p in paras)
    with zipfile.ZipFile(buf, "w") as archive:
        archive.writestr("[Content_Types].xml", "<Types/>")
        archive.writestr("word/document.xml",
                         f'<?xml version="1.0"?><w:document xmlns:w="{ns}"><w:body>'
                         f"{body}</w:body></w:document>")
    got = parse(buf.getvalue(), "examples.docx")
    check(len(got.entries) == 3, f"a .docx imports with no extra dependency ({len(got.entries)})")
    check("maid outfit" in got.entries[0].positive, "…with the text intact")

    # -- failures degrade, never raise
    for data, name, why in [
        (b"not a zip", "x.docx", "a corrupt docx"),
        (b"%PDF-1.4 broken", "x.pdf", "an unreadable pdf"),
        (b"", "x.txt", "an empty file"),
        ("純散文沒有任何提詞".encode("utf-8"), "x.txt", "prose with no prompts"),
        (b"\xff\xfe\x00\x01\x02", "x.txt", "binary junk"),
    ]:
        out = pb.parse(data, name)
        check(out.entries == [] or all(e.positive for e in out.entries),
              f"{why} yields no broken entries")
        check(isinstance(out.note, str), f"{why} explains itself instead of raising")

    # Big5 and UTF-16 files are common on Windows.
    for encoding in ("big5", "utf-16"):
        raw = "1girl, 學校制服, 教室, 坐著\n2girls, 海邊, 泳裝, 夏天\n".encode(encoding)
        out = pb.parse(raw, "x.txt")
        check(len(out.entries) == 2, f"{encoding} decodes ({len(out.entries)})")
        check("學校制服" in out.entries[0].positive, f"…with {encoding} characters intact")

    # -- the store
    store = Book = pb.Book(TMP / "pb" / "book.jsonl")
    store.entries.clear()
    entries = parse("Prompt: 1girl, a, b\nNegative: bad\n\nPrompt: 2girls, c, d\n").entries
    added, dup = store.add_all(entries)
    check((added, dup) == (2, 0), f"entries are added ({added}, {dup})")
    added, dup = store.add_all(entries)
    check((added, dup) == (0, 2), "re-importing the same file adds nothing")

    found, total = store.search("2girls")
    check(total == 1 and found[0].positive.startswith("2girls"), "search finds by word")
    found, total = store.search("1girl b")
    check(total == 1, "several words must all match")
    check(store.search("nothing-like-this")[1] == 0, "a miss returns nothing")

    key = entries[0].key
    check(store.star(key, True), "an entry can be starred")
    check(store.search("", starred=True)[1] == 1, "…and filtered to")
    check(store.search("")[0][0].starred, "starred entries sort first")

    reloaded = pb.Book(store.path)
    reloaded.load()
    check(len(reloaded.entries) == 2, "the library survives a restart")
    check(reloaded.entries[key].starred, "…including the stars")

    check(store.delete_source(entries[0].source) == 2, "a whole import can be undone")
    check(len(store.entries) == 0, "…leaving nothing behind")


def test_restage() -> None:
    """Reading an existing page's panels, and sorting its tags into who/what."""
    import comics
    import pagelayout
    import tags

    section("restaging a page")

    def art(w, h, seed):
        rng = random.Random(seed)
        image = Image.new("RGB", (w, h),
                          (rng.randint(60, 200), rng.randint(60, 200), rng.randint(60, 200)))
        draw = ImageDraw.Draw(image)
        for _ in range(40):
            x, y = rng.randint(0, w), rng.randint(0, h)
            draw.ellipse([x, y, x + rng.randint(20, 90), y + rng.randint(20, 90)],
                         fill=(rng.randint(0, 255),) * 3)
        return image

    def overlap(a, b) -> float:
        ix = max(0, min(a.x + a.w, b.x + b.w) - max(a.x, b.x))
        iy = max(0, min(a.y + a.h, b.y + b.h) - max(a.y, b.y))
        inter = ix * iy
        union = a.w * a.h + b.w * b.h - inter
        return inter / union if union else 0.0

    # -- every layout this app can draw, it can also read back --------------
    for layout in comics.LAYOUTS:
        panels = [art(*comics.panel_size(p, layout.aspect), i)
                  for i, p in enumerate(layout.panels)]
        page = comics.compose(layout, panels, style=comics.PageStyle(width=1000))
        found = pagelayout.detect(page)
        check(len(found.boxes) == layout.count,
              f"{layout.id}: {layout.count} panels detected ({len(found.boxes)})")
        scores = [
            max((overlap(pagelayout.Box(p.x, p.y, p.w, p.h), g) for g in found.boxes),
                default=0.0)
            for p in layout.panels
        ]
        worst = min(scores)
        check(worst > 0.8, f"{layout.id}: every panel matched its rectangle ({worst:.2f})")
        check(found.confidence > 0.8, f"{layout.id}: reported confident ({found.confidence:.2f})")

    # A gutter inside a band is not a gutter across the page, so the profiles
    # have to be measured per region. Wide-over-two is the layout that proves it.
    hero = comics.get("hero-two")
    page = comics.compose(
        hero, [art(*comics.panel_size(p, hero.aspect), i) for i, p in enumerate(hero.panels)],
        style=comics.PageStyle(width=1000),
    )
    found = pagelayout.detect(page)
    check(len(found.boxes) == 3, f"a wide panel over two narrow ones reads as 3 ({len(found.boxes)})")
    tops = sorted({round(b.y, 1) for b in found.boxes})
    check(len(tops) == 2, f"…in two rows ({tops})")

    # -- awkward pages must fail safely, not confidently ---------------------
    blank = pagelayout.detect(Image.new("RGB", (800, 1200), (255, 255, 255)))
    check(blank.boxes == [] and blank.confidence == 0.0, "a blank page finds nothing")
    check(blank.note, "…and says so")

    # A single illustration must never be shattered into panels, whichever
    # route gets there - the background search may read it cleanly as one
    # picture, or the gutter-consistency check may reject the cut.
    flat = pagelayout.detect(art(800, 1200, 9))
    check(len(flat.boxes) == 1, f"a full-bleed image is one panel ({len(flat.boxes)})")

    # The consistency check itself: flat bands inside one drawing vary wildly in
    # width, unlike a real page's gutters, and that is what exposes them.
    grey = Image.new("RGB", (800, 1200), (150, 150, 150))
    pen = ImageDraw.Draw(grey)
    rng = random.Random(4)
    for _ in range(30):
        x, y = rng.randint(0, 800), rng.randint(0, 1200)
        pen.ellipse([x, y, x + rng.randint(20, 80), y + rng.randint(20, 80)],
                    fill=(rng.randint(0, 255),) * 3)
    band = pagelayout.detect(grey)
    check(len(band.boxes) <= 1, f"flat art is not split into panels ({len(band.boxes)})")
    if band.boxes and band.confidence < 0.6:
        check("滿版" in band.note, "…and when unsure it explains why")

    # A page whose row gutters are much wider than its column gutters is
    # perfectly ordinary manga, and must not be mistaken for flat art: the two
    # axes are compared separately for exactly this reason.
    mixed = Image.new("RGB", (900, 1300), (255, 255, 255))
    cell_w, cell_h = (900 - 8) // 2, (1300 - 2 * 32) // 3
    for row in range(3):
        for col in range(2):
            mixed.paste(art(cell_w, cell_h, row * 2 + col),
                        (col * (cell_w + 8), row * (cell_h + 32)))
    uneven = pagelayout.detect(mixed)
    check(len(uneven.boxes) == 6,
          f"8px column gutters with 32px row gutters still read as 6 ({len(uneven.boxes)})")

    # The page's own shape has to come back, or every restage is composed at 2:3.
    wide = comics.compose(comics.get("two-h"),
                          [art(400, 300, 1), art(400, 300, 2)],
                          style=comics.PageStyle(width=1200))
    got = pagelayout.detect(wide)
    check(abs(got.aspect - wide.width / wide.height) < 0.02,
          f"the page's aspect is measured and returned ({got.aspect:.2f})")

    # Manga is read right to left; panel 1 is then the top *right*.
    grid_page = comics.compose(
        comics.get("four-grid"),
        [art(*comics.panel_size(p, comics.get("four-grid").aspect), i)
         for i, p in enumerate(comics.get("four-grid").panels)],
        style=comics.PageStyle(width=900),
    )
    ltr = pagelayout.detect(grid_page, reading="ltr")
    rtl = pagelayout.detect(grid_page, reading="rtl")
    check(len(ltr.boxes) == len(rtl.boxes) == 4, "both reading orders find 4 panels")
    check(rtl.boxes[0].x > ltr.boxes[0].x,
          f"rtl starts on the right ({rtl.boxes[0].x:.2f} vs {ltr.boxes[0].x:.2f})")
    check(ltr.reading == "ltr" and rtl.reading == "rtl", "…and the order is reported")

    # A page with more panels than the stock catalogue holds must survive.
    nine = comics.Layout(id="n", label="n", panels=comics._grid(3, 3), aspect=2 / 3)
    big = comics.compose(nine, [art(*comics.panel_size(p, nine.aspect), i)
                                for i, p in enumerate(nine.panels)],
                         style=comics.PageStyle(width=1000))
    found9 = pagelayout.detect(big)
    check(len(found9.boxes) == 9, f"a 3x3 page reads as 9 panels ({len(found9.boxes)})")
    made9 = comics.custom_layout([b.public() for b in found9.boxes], found9.aspect)
    check(made9 is not None and made9.count == 9,
          f"…and all 9 survive into the layout ({made9.count if made9 else 0})")
    check(comics.MAX_PANELS >= pagelayout.MAX_PANELS,
          "the layout cap is not below what the detector can return")

    grid = comics.get("four-grid")
    imgs = [art(*comics.panel_size(p, grid.aspect), i) for i, p in enumerate(grid.panels)]
    dark = comics.compose(grid, imgs, style=comics.PageStyle(
        width=900, background=(12, 12, 12), ink=(230, 230, 230)))
    got = pagelayout.detect(dark)
    check(len(got.boxes) == 4, f"a dark-background page still reads ({len(got.boxes)})")
    check(got.background == "dark", "…and is reported as dark")

    borderless = comics.compose(grid, imgs, style=comics.PageStyle(width=900, border=0, gutter=26))
    check(len(pagelayout.detect(borderless).boxes) == 4, "gutters alone are enough, no border needed")
    check(len(pagelayout.detect(Image.new("RGB", (30, 40), (200, 30, 30))).boxes) <= 1,
          "a tiny image does not explode")

    check(len(pagelayout.crops(page, found.boxes)) == len(found.boxes),
          "each detected panel yields a crop to tag")

    # -- who vs what ---------------------------------------------------------
    expected = {
        "long_hair": "look", "blue_eyes": "look", "large_breasts": "look",
        "collarbone": "look", "animal_ears": "look",
        "school_uniform": "outfit", "thighhighs": "outfit", "hairband": "outfit",
        "choker": "outfit", "cleavage": "outfit", "nude": "outfit",
        "from_above": "scene", "close-up": "scene", "sitting": "scene",
        "looking_at_viewer": "scene", "blush": "scene", "classroom": "scene",
        "outdoors": "scene", "night": "scene",
        # Cast size is blocking: restaging a two-hander still needs two people.
        "1girl": "scene", "2girls": "scene", "1boy": "scene",
        "comic": "drop", "monochrome": "drop", "speech_bubble": "drop",
        "artist_name": "drop", "4koma": "drop",
    }
    # Naive substring matching sent all of these to the wrong bucket, and with
    # "outfit from my character" on, the outfit bucket is discarded - so these
    # backgrounds simply vanished from the restaged page.
    expected.update({
        "landscape": "scene", "cityscape": "scene", "library": "scene",
        "rainbow": "scene", "bowl": "scene", "elbow": "scene",
        "bowing": "scene", "hatching": "scene", "detailed_background": "scene",
        "windowsill": "scene", "scenery": "scene",
        # …while these must still reach it
        "elbow_gloves": "outfit", "hair_ribbon": "outfit", "white_shirt": "outfit",
    })
    wrong = {t: tags.classify(t) for t, want in expected.items() if tags.classify(t) != want}
    check(not wrong, f"tags sort into who/what/drop correctly ({wrong or 'all correct'})")

    split = tags.split_tags(list(expected))
    check(len(split["scene"]) + len(split["look"]) + len(split["outfit"])
          + len(split["drop"]) == len(expected), "every tag lands in exactly one bucket")
    check("collarbone" not in split["outfit"],
          "a body part is not mistaken for clothing by the 'collar' substring")
    # An unknown tag is safer as scene than as identity.
    check(tags.classify("zzz_unknown_thing") == "scene", "unknown tags default to the shot")

    # -- a layout measured off a page is usable ------------------------------
    made = comics.custom_layout([b.public() for b in found.boxes], 2 / 3)
    check(made is not None and made.count == 3, "detected rectangles become a layout")
    check(made.id == comics.CUSTOM_ID, "…flagged as custom")
    check(comics.custom_layout([], 0.5) is None, "no rectangles means no layout")
    junk = comics.custom_layout(
        [{"x": -5, "y": 0.1, "w": 99, "h": 0.4}, {"nope": 1}, {"x": 0.1, "y": 0.1, "w": 0.5, "h": 0.5}],
        99.0,
    )
    check(junk is not None and junk.count == 2, f"malformed rectangles are skipped ({junk.count})")
    for panel in junk.panels:
        inside = (0 <= panel.x <= 1 and 0 <= panel.y <= 1
                  and 0 < panel.w <= 1 and 0 < panel.h <= 1
                  and panel.x + panel.w <= 1.001 and panel.y + panel.h <= 1.001)
        check(inside, f"…and the rest are clamped onto the page ({panel})")
    check(0.2 <= junk.aspect <= 4.0, f"an absurd aspect is clamped ({junk.aspect})")

    # It composes like any other layout.
    page2 = comics.compose(made, [art(400, 400, i) for i in range(3)],
                           style=comics.PageStyle(width=800))
    check(page2.size[0] == 800, "a measured layout composes into a page")


async def test_restage_deferred() -> None:
    """The two-phase restage: layout first, then one panel at a time.

    Tagging costs ~2s a panel on CPU, so a nine-panel page used to be half a
    minute of a blank screen. The panels are fetched under a token instead, and
    that token is what these checks are about - it has to expire, it has to be
    bounded, and a panel must always come back on the rectangle it was asked
    for even when its neighbour fails to read.
    """
    from fastapi import HTTPException

    import comics
    import pagelayout
    import server
    import tags

    section("restaging: deferred panels")

    def art(w, h, seed):
        rng = random.Random(seed)
        image = Image.new("RGB", (w, h),
                          (rng.randint(60, 200), rng.randint(60, 200), rng.randint(60, 200)))
        draw = ImageDraw.Draw(image)
        for _ in range(30):
            x, y = rng.randint(0, w), rng.randint(0, h)
            draw.ellipse([x, y, x + rng.randint(20, 90), y + rng.randint(20, 90)],
                         fill=(rng.randint(0, 255),) * 3)
        return image

    grid = comics.get("four-grid")
    page = comics.compose(
        grid, [art(*comics.panel_size(p, grid.aspect), i) for i, p in enumerate(grid.panels)],
        style=comics.PageStyle(width=900),
    )
    boxes = pagelayout.detect(page).boxes
    check(len(boxes) == 4, f"the test page reads as 4 panels ({len(boxes)})")

    # The tagger needs a 380MB ONNX model, so it is stood in for. Panel 1 is a
    # deliberately empty establishing shot and panel 2 deliberately explodes.
    calls: list[int] = []

    def fake_describe(image, base, *a, **k):
        calls.append(image.size[0])
        if len(calls) == 3:
            raise RuntimeError("onnx exploded")
        guess = tags.Guess(rating="questionable")
        if len(calls) == 2:
            guess.general = [("no_humans", 0.9), ("scenery", 0.8), ("night", 0.7)]
        else:
            guess.general = [("1girl", 0.99), ("classroom", 0.9), ("school_uniform", 0.8),
                             ("from_above", 0.7)]
            guess.characters = [("hatsune_miku", 0.95)]
        return guess

    real_describe = tags.describe
    tags.describe = fake_describe
    real_store = dict(server._restage)
    server._restage.clear()
    try:
        look = ["long_hair", "blue_eyes"]
        outfit = ["thighhighs"]
        token = "tok0"
        server._restage[token] = (time.time(), page, ROOT, look, outfit, "character", boxes)

        got = await server.restage_panel(token, 0)
        body = json.loads(got.body)
        check(body["index"] == 0, f"the panel comes back on its own index ({body['index']})")
        panel = body["panel"]
        check("long hair" in panel["prompt"] and "blue eyes" in panel["prompt"],
              f"the new character's looks are applied ({panel['prompt']})")
        check("thighhighs" in panel["prompt"],
              "…and their outfit, since outfit_from=character")
        check("school uniform" not in panel["prompt"],
              "…replacing the outfit the page was wearing")
        check("classroom" in panel["prompt"] and "from above" in panel["prompt"],
              "the shot keeps its own staging")
        check("hatsune miku" not in panel["prompt"],
              "the original cast is never carried over")
        check("hatsune miku" in panel["dropped"], "…and is listed as dropped, not hidden")
        check(panel["rating"] == "questionable", "the panel's rating is reported")

        # An establishing shot with nobody in it must not get a person pasted in.
        empty = json.loads((await server.restage_panel(token, 1)).body)["panel"]
        check(empty["no_people"], "a no-humans panel is flagged")
        check("long hair" not in empty["prompt"],
              f"…and the character is not pasted into it ({empty['prompt']})")
        check("thighhighs" not in empty["prompt"],
              "…nor their clothes, which would draw them just as surely")
        check(empty["note"], "…and the page says why")

        # A panel that fails to read must not take the layout down with it.
        broken = json.loads((await server.restage_panel(token, 2)).body)["panel"]
        check(broken["prompt"] == "" and "失敗" in broken["note"],
              f"a failed panel returns empty with a reason ({broken['note']!r})")

        # The switch can be flipped without re-uploading the page.
        kept = json.loads(
            (await server.restage_panel(token, 3, {"outfit_from": "page"})).body)["panel"]
        check("school uniform" in kept["prompt"] and "thighhighs" not in kept["prompt"],
              f"outfit_from=page keeps the page's clothes ({kept['prompt']})")
        again = json.loads((await server.restage_panel(token, 0)).body)["panel"]
        check("school uniform" in again["prompt"],
              "…and the choice sticks for later panels without re-sending it")
        bogus = json.loads(
            (await server.restage_panel(token, 0, {"outfit_from": "nonsense"})).body)["panel"]
        check(bogus["prompt"] == again["prompt"], "an unknown outfit_from is ignored, not obeyed")

        for index in (-1, 4, 99):
            try:
                await server.restage_panel(token, index)
                check(False, f"panel {index} should not exist")
            except HTTPException as exc:
                check(exc.status_code == 404, f"panel {index} is a 404 ({exc.status_code})")
        try:
            await server.restage_panel("nope", 0)
            check(False, "an unknown token should be refused")
        except HTTPException as exc:
            check(exc.status_code == 400 and "過期" in exc.detail,
                  f"an expired token says so in Chinese ({exc.detail!r})")

        # Each page held is a full-size bitmap, so the store is bounded twice:
        # by age, and by count.
        server._restage.clear()
        server._restage["old"] = (time.time() - server.RESTAGE_TTL - 1, page, ROOT,
                                  [], [], "character", boxes)
        server._restage["new"] = (time.time(), page, ROOT, [], [], "character", boxes)
        server._sweep_restage()
        check("old" not in server._restage and "new" in server._restage,
              f"a stale page is swept, a fresh one kept ({sorted(server._restage)})")

        server._restage.clear()
        for i in range(server.RESTAGE_MAX + 3):
            server._restage[f"t{i}"] = (time.time() + i, page, ROOT, [], [],
                                        "character", boxes)
            server._sweep_restage()
        check(len(server._restage) <= server.RESTAGE_MAX,
              f"no more than {server.RESTAGE_MAX} pages are held ({len(server._restage)})")
        check("t0" not in server._restage and f"t{server.RESTAGE_MAX + 2}" in server._restage,
              "…and it is the oldest that goes")

        # Touching a token has to keep it alive - a nine-panel page takes longer
        # to read than a short TTL would allow.
        server._restage.clear()
        stamp = time.time() - 600
        server._restage["live"] = (stamp, page, ROOT, [], [], "character", boxes)
        await server.restage_panel("live", 0)
        check(server._restage["live"][0] > stamp, "reading a panel refreshes the token")

        # -- the composition crops -------------------------------------------
        # Copying tags gives a similar scene; copying the panel's own art into
        # a ControlNet gives the same shot. These are those crops.
        import config

        saved = server._save_controls(page, boxes)
        check(len(saved) == len(boxes), f"one reference per panel ({len(saved)})")
        check(all(server.control_path(n) is not None for n in saved),
              "every one of them is on disk")
        sizes = [Image.open(server.control_path(n)).size for n in saved]
        check(all(w > 8 and h > 8 for w, h in sizes), f"…and is real art ({sizes})")
        check(len(set(saved)) == len(saved), "no two panels share a reference file")

        # A box too small to crop must leave a hole, not shift the rest.
        gappy = [boxes[0], pagelayout.Box(0.5, 0.5, 0.0005, 0.0005), boxes[1]]
        holed = server._save_controls(page, gappy)
        check(len(holed) == 3 and holed[1] == "",
              f"a degenerate panel yields an empty slot ({holed})")
        check(server.control_path(holed[0]) and server.control_path(holed[2]),
              "…and its neighbours keep their own crops")

        # The name makes a round trip through the browser, so it is matched
        # against the shape this server writes rather than trusted.
        for bad in ("", "../../.env", "ctrl-../../x-00.png", "src-abc.png",
                    "ctrl-zz-00.png", "ctrl-0123456789ab-00.png.txt",
                    "/etc/passwd", "ctrl-0123456789ab-0.png"):
            check(server.control_path(bad) is None, f"{bad!r} is refused")
        check(server.control_path("ctrl-0123456789ab-00.png") is None,
              "a well-shaped name that is not on disk is refused too")

        # Old crops are swept, or the staging folder grows without limit.
        old_crop = config.STAGING_DIR / "ctrl-ffffffffffff-00.png"
        old_crop.parent.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", (16, 16)).save(old_crop, "PNG")
        os.utime(old_crop, (0, time.time() - server.CONTROL_TTL - 60))
        fresh = server._save_controls(page, boxes[:1])
        check(not old_crop.exists(), "a crop older than the TTL is swept")
        check(server.control_path(fresh[0]) is not None, "…while the new one survives")

        # -- the whole round trip --------------------------------------------
        # Restage measures the page and keeps the crops; the browser hands both
        # back; the job has to end up carrying the crops in panel order. This is
        # the seam where a page silently loses its composition.
        import controlnets

        crops = server._save_controls(page, boxes)
        installed = [c.name for c in controlnets.CONTROLNETS]
        real_installed = server.installed_controlnets
        real_status = server.image_status
        server.installed_controlnets = lambda: installed
        # There is no 7GB checkpoint on disk here, and the endpoint refuses
        # before it ever reaches the crops - so it is stood in for.
        server.image_status = lambda m: {"installed": True, "missing": []}
        try:
            payload = {
                "model": "illustrious",
                "layout": "custom",
                "custom_panels": [b.public() for b in boxes],
                "custom_aspect": 2 / 3,
                "panels": ["a", "b", "c", "d"],
                "controlnet": installed[0],
                "controls": crops,
                "controlnet_strength": 0.6,
            }
            out = json.loads((await server.comic_generate(payload)).body)
            stored = next(r for r in server.lib.recent() if r.id == out["id"]).settings
            check(stored["controls"] == crops, "the crops reach the job in panel order")
            check(stored["controlnet"] == installed[0], "…along with the model")
            check(stored["controlnet_strength"] == 0.6, "…and the strength")

            # A ControlNet that is not on disk has to be caught here, not by
            # ComfyUI half a minute into the job.
            try:
                await server.comic_generate({**payload, "controlnet": "nope.safetensors"})
                check(False, "an uninstalled ControlNet should be refused")
            except HTTPException as exc:
                check(exc.status_code == 400 and "下載" in exc.detail,
                      f"an uninstalled ControlNet is refused up front ({exc.detail[:24]})")

            # A dead reference must cost that panel its guide, not the page.
            (config.STAGING_DIR / crops[1]).unlink()
            out2 = json.loads((await server.comic_generate(payload)).body)
            kept = next(r for r in server.lib.recent() if r.id == out2["id"]).settings["controls"]
            check(kept[1] == "" and kept[0] and kept[2],
                  f"a swept crop leaves a hole, not a shift ({kept})")
            check(len(kept) == len(crops), "…and the list keeps its length")

            # All of them gone means the page would silently ignore the setting,
            # so that is the one case worth stopping for.
            for name in crops:
                (config.STAGING_DIR / name).unlink(missing_ok=True)
            try:
                await server.comic_generate(payload)
                check(False, "a page with every reference gone should be refused")
            except HTTPException as exc:
                check(exc.status_code == 400 and "重新上傳" in exc.detail,
                      f"…and says to upload the original again ({exc.detail[:20]})")
        finally:
            server.installed_controlnets = real_installed
            server.image_status = real_status
    finally:
        tags.describe = real_describe
        server._restage.clear()
        server._restage.update(real_store)


def test_second_review_regressions() -> None:
    """Each case is a defect the second review found. All were reproduced."""
    import config
    import promptbook as pb
    import registry
    import watcher
    import workflow

    section("second review regressions")

    def parse(text, name="x.txt"):
        return pb.parse(text.encode("utf-8") if isinstance(text, str) else text, name)

    # -- the blocker: a tab with no entry in the switcher's list -------------
    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    buttons = set(re.findall(r'<button[^>]*data-tab="([^"]+)"', page))
    panels = set(re.findall(r'id="tab-([^"]+)"', page))
    check(buttons == panels,
          f"every tab button has a panel and vice versa ({buttons ^ panels or 'matched'})")
    # The defect this guards against is a hand-written list of tab ids that
    # silently loses any tab added later. Assert that property, not one exact
    # line of source - the literal string broke the moment the switcher was
    # refactored for keyboard support, while the property still held.
    switcher = re.search(r"const TABS = ([^;]+);", page)
    check(switcher is not None, "the tab list is derived, not written out")
    if switcher:
        derived = switcher.group(1)
        check("querySelectorAll" in derived or "TABBTNS" in derived,
              f"…from the DOM ({derived.strip()[:60]})")
        check("'gen'" not in derived and '"gen"' not in derived,
              "…with no tab id hardcoded into it")

    # The same defect one level down: `$('#thing')` on an id that no longer
    # exists returns null and the whole handler dies on the next line, taking
    # every later listener on the page with it. Ids written into template
    # literals count - that is how the restage cards and the LoRA rows are
    # built - so the search is over the whole file, markup and script alike.
    have_ids = set(re.findall(r'\bid="([A-Za-z][\w-]*)"', page))
    wanted = set(re.findall(r"""\$\('#([A-Za-z][\w-]*)'\)""", page))
    wanted |= set(re.findall(r"""getElementById\('([A-Za-z][\w-]*)'\)""", page))
    missing = sorted(wanted - have_ids)
    check(not missing, f"every id the script reaches for exists ({missing or 'all present'})")

    # -- `Negative prompt:` with no `Steps:` line ---------------------------
    got = parse("Prompt: 1girl, silver hair\nNegative prompt: bad hands, blurry\n")
    check(got.entries[0].negative == "bad hands, blurry",
          f"'Negative prompt:' is matched whole ({got.entries[0].negative!r})")
    check("Negative" not in got.entries[0].positive,
          "…and is not glued onto the positive")
    for label in ("負面提詞", "負面", "Negative", "neg"):
        out = parse(f"Prompt: 1girl, a, b\n{label}: bad hands\n")
        check(out.entries[0].negative == "bad hands", f"'{label}:' is recognised")
    for label in ("名稱", "標題", "Title"):
        out = parse(f"{label}: 甲\nPrompt: 1girl, a, b\n")
        check(out.entries[0].title == "甲", f"'{label}:' is recognised")

    # -- two short prompts in one blank-line block --------------------------
    got = parse("1girl, red, a\n2girls, blue, b\n\n1boy, green, c\n3girls, gold, d\n")
    check(len(got.entries) == 4, f"no prompt is eaten as a title ({len(got.entries)})")
    check(all(e.title == "" for e in got.entries), "…and none is mislabelled")
    # A real title still works.
    titled = parse("校園場景\n1girl, school uniform, classroom, sitting\n")
    check(titled.entries[0].title == "校園場景", "a genuine title is still detected")

    # -- BOM-less Big5 of even byte length ----------------------------------
    for pad in ("", "a", "aa", "aaa"):
        text = f"1girl, 學校制服{pad}\n2girls, 海邊泳裝\n"
        raw = text.encode("big5")
        out = pb.parse(raw, "x.txt")
        check(len(out.entries) == 2 and "學校制服" in out.entries[0].positive,
              f"Big5 decodes at byte length {len(raw)} ({'even' if len(raw) % 2 == 0 else 'odd'})")
    check(pb.decode("測試中文一二三四".encode("big5")) == "測試中文一二三四",
          "an even-length Big5 blob is not mistaken for UTF-16")
    for codec in ("utf-8-sig", "utf-16", "utf-16-le", "utf-16-be"):
        blob = "1girl, red dress\n2girls, blue sky\n".encode(codec)
        out = pb.parse(blob, "x.txt")
        check(len(out.entries) == 2, f"{codec} still decodes ({len(out.entries)})")

    # -- Title: before its Prompt: ------------------------------------------
    got = parse("Title: A\nPrompt: 1girl, aaa, bbb\n\nTitle: B\nPrompt: 2girls, ccc, ddd\n")
    check([e.title for e in got.entries] == ["A", "B"],
          f"a title stays with the entry it introduces ({[e.title for e in got.entries]})")
    check(len(got.entries) == 2, "…and no entry is lost")

    # -- <w:br/> inside a Word paragraph ------------------------------------
    import zipfile
    ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    body = ("<w:p><w:r><w:t>1girl, maid outfit, cafe</w:t><w:br/>"
            "<w:t>2girls, beach, summer</w:t></w:r></w:p>")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as archive:
        archive.writestr("[Content_Types].xml", "<Types/>")
        archive.writestr("word/document.xml",
                         f'<?xml version="1.0"?><w:document xmlns:w="{ns}">'
                         f"<w:body>{body}</w:body></w:document>")
    got = pb.parse(buf.getvalue(), "x.docx")
    check(len(got.entries) == 2, f"Shift+Enter is a line break ({len(got.entries)})")
    check("cafe2girls" not in " ".join(e.positive for e in got.entries),
          "…so consecutive prompts are not glued together")

    # -- structured parsers must not short-circuit on an empty result -------
    got = pb.parse(json.dumps([{"weird_key": "1girl, red dress, standing"}]).encode(),
                   "x.json")
    check(len(got.entries) >= 1,
          f"a .json with unknown keys falls through to the text splitters ({len(got.entries)})")
    got = pb.parse(b"1girl, red dress, standing\n2girls, blue sky, outdoors\n", "x.csv")
    check(len(got.entries) == 2, f"a .csv that is really a plain list still imports ({len(got.entries)})")

    # -- staging must not live in the watcher's drop folder -----------------
    check(config.STAGING_DIR != config.INBOX_DIR,
          "image staging has its own directory")
    check(not str(config.STAGING_DIR).startswith(str(config.INBOX_DIR) + os.sep),
          "…and is not nested inside the watched one either")
    server_src = (ROOT / "app" / "server.py").read_text(encoding="utf-8")
    check("INBOX_DIR / f\"{record.id}.png\"" not in server_src,
          "no job source is written into the watched folder")
    check(watcher.IMAGE_SUFFIXES, "the watcher does claim image files (hence the split)")

    # -- out_fps must describe what happened, not what was asked ------------
    model = registry.get("wan22-14b-fp8")
    params = registry.GenParams.defaults_for(model)
    params.interpolate, params.interpolate_model = 2, "rife_v4.26.safetensors"
    full = {"FrameInterpolationModelLoader", "FrameInterpolate"}
    check(workflow.output_fps(params, full) == model.fps * 2,
          "interpolation doubles the reported fps when it runs")
    check(workflow.output_fps(params, set()) == model.fps,
          "…and does not when the nodes are missing")
    params.interpolate_model = ""
    check(workflow.output_fps(params, full) == model.fps,
          "…nor when no interpolation model was chosen")
    params.interpolate = 1
    check(workflow.output_fps(params, full) == model.fps, "off means off")

    # -- a partial download with an unknown size must resume ----------------
    dl_src = (ROOT / "app" / "downloader.py").read_text(encoding="utf-8")
    check("if state.file.size and existing > state.file.size:" in dl_src,
          "a .part is only discarded when a known size proves it too big")

    # -- fire-and-forget tasks must be held ---------------------------------
    check("_background.add(task)" in server_src,
          "background tasks are referenced so they cannot be collected mid-flight")

    # -- the comic preview must not share one filename ----------------------
    check("comic-preview.png" not in server_src,
          "the layout preview is returned as bytes, not via a shared file")


def test_inspect_image() -> None:
    """Recovering settings out of a generated file. This half must be exact."""
    import images
    import inspect_image
    import tags
    from PIL.PngImagePlugin import PngInfo

    section("reading an image's settings")

    model = images.get("illustrious")
    settings = images.defaults_for(model)
    settings.loras = [("my_style.safetensors", 0.85, 0.5), ("other.safetensors", 0.6, 0.6)]
    settings.steps, settings.cfg, settings.hires_scale = 30, 5.5, 1.5
    graph = images.build(
        model, settings, prompt="1girl, pink dress", negative="bad hands",
        seed=424242, width=832, height=1216,
    )

    def png_with(**chunks) -> Image.Image:
        meta = PngInfo()
        for key, value in chunks.items():
            meta.add_text(key, value)
        buf = io.BytesIO()
        Image.new("RGB", (64, 64), (20, 30, 40)).save(buf, "PNG", pnginfo=meta)
        return Image.open(io.BytesIO(buf.getvalue()))

    # -- ComfyUI ------------------------------------------------------------
    # The chunk name and JSON encoding match ComfyUI's nodes.py exactly:
    # metadata.add_text("prompt", json.dumps(prompt)).
    found = inspect_image.read_metadata(png_with(prompt=json.dumps(graph)))
    check(found.source == "comfyui", "a ComfyUI png is recognised")
    check(found.prompt == "1girl, pink dress", f"the prompt comes back verbatim ({found.prompt})")
    check(found.negative == "bad hands", "so does the negative")
    check(found.model == model.file.name, f"and the checkpoint ({found.model})")
    check(found.seed == 424242 and found.steps == 30 and found.cfg == 5.5,
          "seed, steps and cfg come back")
    check(found.sampler == model.sampler and found.scheduler == model.scheduler,
          "sampler and scheduler come back")
    check(found.clip_skip == -2, f"CLIP skip comes back ({found.clip_skip})")
    check((found.width, found.height) == (832, 1216), "so does the size")
    check([l["name"] for l in found.loras] == ["my_style.safetensors", "other.safetensors"],
          "every LoRA is listed")
    check(found.loras[0]["strength"] == 0.85 and found.loras[0]["strength_clip"] == 0.5,
          "…with its two strengths kept apart")

    # A hi-res graph has two samplers; the one that produced the saved image is
    # the last in the chain, not the first.
    check(len(nodes_of(graph, "KSampler")) == 2, "the fixture really has two samplers")
    plain = images.build(model, images.defaults_for(model), prompt="x", negative="y",
                         seed=7, width=1024, height=1024)
    simple = inspect_image.read_metadata(png_with(prompt=json.dumps(plain)))
    check(simple.prompt == "x" and simple.seed == 7, "a single-sampler graph reads too")

    # -- Automatic1111 -------------------------------------------------------
    a1111 = (
        "masterpiece, 1girl, <lora:animeStyle:0.8> standing\n"
        "Negative prompt: bad hands, blurry\n"
        "Steps: 28, Sampler: DPM++ 2M, Schedule type: Karras, CFG scale: 7.5, "
        'Seed: 987654, Size: 832x1216, Model hash: abc123, Model: ponyDiffusionV6XL, '
        'Clip skip: 2, Lora hashes: "animeStyle: 1a2b, extraDetail: 9z8y", Version: v1.10.1'
    )
    found = inspect_image.read_metadata(png_with(parameters=a1111))
    check(found.source == "a1111", "an A1111 png is recognised")
    check(found.prompt.startswith("masterpiece, 1girl"), "prompt parsed")
    check(found.negative == "bad hands, blurry", "negative parsed")
    check(found.model == "ponyDiffusionV6XL" and found.seed == 987654, "model and seed parsed")
    check(found.steps == 28 and found.cfg == 7.5, "steps and cfg parsed")
    check(found.sampler == "DPM++ 2M" and found.scheduler == "Karras", "sampler parsed")
    check((found.width, found.height) == (832, 1216), "size parsed")
    check(found.clip_skip == -2,
          f"A1111 counts clip skip up from 1, ComfyUI down from -1 ({found.clip_skip})")
    names = [l["name"] for l in found.loras]
    check("animeStyle" in names and "extraDetail" in names,
          f"inline and hash-listed LoRAs both found ({names})")
    check(next(l for l in found.loras if l["name"] == "animeStyle")["strength"] == 0.8,
          "…with the inline strength")
    check(found.extras.get("Model hash") == "abc123", "unrecognised settings are kept, not lost")

    # A1111 also hides the same string in EXIF for JPEG.
    buf = io.BytesIO()
    exif = Image.Exif()
    exif[inspect_image.EXIF_USER_COMMENT] = b"UNICODE\x00" + a1111.encode("utf-16-be")
    Image.new("RGB", (32, 32)).save(buf, "JPEG", exif=exif)
    from_jpeg = inspect_image.read_metadata(Image.open(io.BytesIO(buf.getvalue())))
    check(from_jpeg.source == "a1111", "a JPEG's EXIF UserComment is read too")
    check(from_jpeg.seed == 987654, "…with the same values")

    # -- nothing, and rubbish ------------------------------------------------
    blank = io.BytesIO()
    Image.new("RGB", (32, 32)).save(blank, "PNG")
    nothing = inspect_image.read_metadata(Image.open(io.BytesIO(blank.getvalue())))
    check(nothing.source == "" and not nothing.prompt,
          "a plain photo claims nothing rather than inventing it")
    for junk in ("{not json", "[]", "{}", json.dumps({"1": {"class_type": "Nope"}}), ""):
        out = inspect_image.read_metadata(png_with(prompt=junk))
        check(out.source in ("", "comfyui"), f"junk metadata does not crash ({junk[:12]})")
        check(not out.prompt, "…and does not fabricate a prompt")
    check(inspect_image.read_metadata(png_with(parameters="just a caption")).source == "",
          "an ordinary text chunk is not mistaken for A1111 settings")

    # -- tag helpers ---------------------------------------------------------
    check(tags.to_prompt("long_hair") == "long hair", "underscores become spaces")
    check(tags.to_prompt("rem_(re:zero)") == r"rem \(re:zero\)",
          "parentheses are escaped, or they would reweight the prompt")
    folders = [t.model.folder for t in tags.TAGGERS]
    check(len(set(folders)) == len(folders),
          "each tagger downloads to its own folder (all are named model.onnx)")
    check(all(t.model.folder == t.labels.folder for t in tags.TAGGERS),
          "weights and labels land together")

    guess = tags.Guess(general=[("1girl", 0.9), ("long_hair", 0.8)],
                       characters=[("rem_(re:zero)", 0.9)])
    check(guess.prompt.startswith("rem "), "characters lead the prompt")
    check("long hair" in guess.prompt, "general tags follow")
    check(tags.suggest_model(guess) == "illustrious", "anime tags suggest the anime model")
    photo = tags.Guess(general=[("realistic", 0.9), ("1girl", 0.8)])
    check(tags.suggest_model(photo) == "juggernaut", "realistic tags suggest the photo model")
    hints = tags.matching_loras(
        guess, [{"name": "a.safetensors", "trained_words": ["long hair", "nope"]},
                {"name": "b.safetensors", "trained_words": ["unrelated"]}])
    check([h["name"] for h in hints] == ["a.safetensors"],
          "only LoRAs whose trigger words appear are hinted")
    check(hints[0]["matched"] == ["long hair"], "…and it says which word matched")


async def test_comics() -> None:
    """Panel layouts, the graph they build, and the page they compose into."""
    import comics
    import images
    from comfy_client import ComfyClient

    section("comics")
    fake = FakeComfy()
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        nodes = await client.node_classes()
        model = images.get("illustrious")

        # -- layout geometry ------------------------------------------------
        for layout in comics.LAYOUTS:
            total = sum(p.w * p.h for p in layout.panels)
            check(abs(total - 1.0) < 0.001, f"{layout.id} panels tile the page exactly ({total})")
            for p in layout.panels:
                inside = 0 <= p.x and 0 <= p.y and p.x + p.w <= 1.001 and p.y + p.h <= 1.001
                check(inside, f"{layout.id} panel stays on the page")
            for w, h in (comics.panel_size(p, layout.aspect) for p in layout.panels):
                mp = w * h / 1e6
                check(0.9 < mp < 1.15, f"{layout.id} panel is ~1MP, not off-distribution ({mp:.2f})")
                check(w % 8 == 0 and h % 8 == 0, f"{layout.id} panel size is a multiple of 8")

        # A tall slot must get a tall render and a wide slot a wide one.
        wide = comics.panel_size(comics.Panel(0, 0, 1, 0.25), 2 / 3)
        tall = comics.panel_size(comics.Panel(0, 0, 0.25, 1), 2 / 3)
        check(wide[0] > wide[1], f"a wide slot renders landscape {wide}")
        check(tall[1] > tall[0], f"a tall slot renders portrait {tall}")

        # -- graph ----------------------------------------------------------
        for layout in comics.LAYOUTS:
            settings = images.defaults_for(model)
            settings.loras = [("my_style.safetensors", 0.7, 0.5)]
            settings.freeu, settings.pag, settings.tiled_vae = True, 3.0, True
            panels = [
                (comics.scaffold("close-up", "1girl", "score_9"),
                 *comics.panel_size(p, layout.aspect))
                for p in layout.panels
            ]
            g = images.build_comic(
                model, settings, panels=panels,
                negative=comics.negative_for(model.negative), seed=5,
                available_nodes=nodes, filename_prefix="comic/t",
            )
            problems = await client.validate(g)
            check(problems == [], f"{layout.id} graph validates {problems[:1]}")
            check(len(nodes_of(g, "SaveImage")) == layout.count,
                  f"{layout.id} saves one file per panel")
            check(len(nodes_of(g, "EmptyLatentImage")) == layout.count,
                  f"{layout.id} gives every panel its own latent")
            # The expensive parts are shared, not repeated per panel.
            check(len(nodes_of(g, "CheckpointLoaderSimple")) == 1,
                  f"{layout.id} loads the checkpoint once")
            check(len(nodes_of(g, "LoraLoader")) == 1, f"{layout.id} loads the LoRA once")
            check(len(nodes_of(g, "FreeU_V2")) == 1, f"{layout.id} patches the model once")
            seeds = [n["inputs"]["seed"] for n in nodes_of(g, "KSampler")]
            check(len(set(seeds)) == layout.count,
                  f"{layout.id} varies the seed per panel, so it is not one image N times")
            prefixes = [n["inputs"]["filename_prefix"] for n in nodes_of(g, "SaveImage")]
            check(len(set(prefixes)) == layout.count, f"{layout.id} panel files do not collide")
            check(prefixes == sorted(prefixes), f"{layout.id} filenames sort into page order")

        # -- prompt scaffolding ----------------------------------------------
        full = comics.negative_for(model.negative, full_color=True)
        grey = comics.negative_for(model.negative, full_color=False)
        check("monochrome" in full and "greyscale" in full,
              "full colour works by excluding monochrome (52% of danbooru comics are grey)")
        check("monochrome" not in grey, "turning colour off stops excluding it")
        check("speech bubble" in comics.negative_for("", draw_text=True),
              "the model is told not to letter, because the app letters afterwards")
        check("speech bubble" not in comics.negative_for("", draw_text=False),
              "…unless the user wants the model's own lettering")
        built = comics.scaffold("close-up", "1girl, red dress", "score_9")
        check(built.startswith("score_9"), "the model's own prefix stays first")
        check("comic" in built and "1girl" in built and "close-up" in built,
              "panel prompt = prefix + comic style + shared + panel")
        check(comics.scaffold("x", "") == f"{comics.PANEL_STYLE}, x", "empty parts are dropped")

        # -- page composition -------------------------------------------------
        layout = comics.get("four-grid")
        art = [Image.new("RGB", comics.panel_size(p, layout.aspect), (i * 40, 90, 120))
               for i, p in enumerate(layout.panels)]
        page = comics.compose(layout, art, style=comics.PageStyle(width=1200))
        check(page.size == (1200, 1800), f"page follows the layout aspect {page.size}")
        check(page.getpixel((3, 3)) == (255, 255, 255), "the page has a margin")

        # Panels must be cropped to fill, never letterboxed - a grey bar in a
        # comic panel is the tell that the art did not fit.
        squashed = comics.compose(
            layout, [Image.new("RGB", (1536, 640), (200, 30, 30))] * 4,
            style=comics.PageStyle(width=1200, border=0, gutter=0, margin=0),
        )
        check(squashed.getpixel((300, 400)) == (200, 30, 30),
              "a wrong-shaped panel is cropped to fill, not letterboxed")

        # Missing art still yields a page, so a partial render is inspectable.
        partial = comics.compose(layout, art[:2], style=comics.PageStyle(width=800))
        check(partial.size == (800, 1200), "a partial page still composes")

        # Spacing is relative to page width, so the same numbers look the same.
        small = comics.compose(layout, art, style=comics.PageStyle(width=600))
        big = comics.compose(layout, art, style=comics.PageStyle(width=2400))
        check(big.size[0] == 4 * small.size[0], "page scales cleanly")

        # -- lettering --------------------------------------------------------
        if comics.find_font(20):
            plain = comics.compose(layout, art, style=comics.PageStyle(width=1000))
            lettered = comics.compose(
                layout, art,
                [[comics.Bubble("這是對白，測試中文", "top-left")], [], [], []],
                comics.PageStyle(width=1000),
            )
            check(list(plain.getdata()) != list(lettered.getdata()),
                  "a bubble actually changes the page")
            white_plain = sum(1 for p in plain.getdata() if p == (255, 255, 255))
            white_bubble = sum(1 for p in lettered.getdata() if p == (255, 255, 255))
            check(white_bubble > white_plain + 5000, "the bubble is drawn, not just the text")
            empty = comics.compose(layout, art, [[comics.Bubble("   ", "top")], [], [], []],
                                   comics.PageStyle(width=1000))
            check(list(empty.getdata()) == list(plain.getdata()),
                  "a blank bubble draws nothing")
        else:
            check(True, "no CJK font here; lettering checks skipped")

        check(comics._wrap("", 10) == [], "empty text wraps to nothing")
        check(len(comics._wrap("一二三四五六七八九十", 5)) == 2, "CJK wraps by character count")
        check(all(len(l) <= 20 for l in comics._wrap("the quick brown fox jumps over it", 8)),
              "Latin wraps on word boundaries")
        check(len(comics._wrap("x\n" * 40, 10)) <= 6, "runaway text is capped")
    finally:
        await runner.cleanup()


async def test_charpacks() -> None:
    """Character packs: a LoRA's whole cast turned into a one-click prompt.

    The data is transcribed from a model page, so the checks that matter are
    about the transcription staying usable: every character reachable from a
    group, every costume carrying tags, and the parentheses escaped - a bare
    `(1st costume)` is ComfyUI weighting syntax, not a costume name.
    """
    from fastapi import HTTPException

    import charpacks
    import images
    import server

    section("character packs")

    check(charpacks.PACKS, f"packs load from disk ({len(charpacks.PACKS)})")
    for pack in charpacks.PACKS:
        tag = pack.id
        check(pack.file.endswith(".safetensors"), f"{tag}: names a real weight file")
        check(pack.characters, f"{tag}: has characters")
        keys = [c.key for c in pack.characters]
        check(len(set(keys)) == len(keys), f"{tag}: every character key is unique")

        # A character in no group is a character nobody can click.
        grouped = [m for g in pack.groups for m in g.members]
        check(sorted(grouped) == sorted(keys),
              f"{tag}: every character is in exactly one group "
              f"({sorted(set(keys) - set(grouped)) or 'all placed'})")
        check(len(grouped) == len(set(grouped)), f"{tag}: nobody is listed twice")

        for c in pack.characters:
            check(c.costumes, f"{tag}/{c.key}: has at least one outfit")
            labels = [k.label for k in c.costumes]
            check(len(set(labels)) == len(labels),
                  f"{tag}/{c.key}: outfit names are distinct ({labels})")
            for k in c.costumes:
                check(k.trigger.strip(), f"{tag}/{c.key}/{k.label}: has a trigger")
                # ComfyUI parses ( ) as weighting. An unescaped costume name
                # would quietly become a 1.1x weight on the wrong words.
                bare = re.sub(r"\\[()]", "", k.trigger)
                check("(" not in bare and ")" not in bare,
                      f"{tag}/{c.key}/{k.label}: parens escaped ({k.trigger})")

        if pack.wants_model:
            check(images.get(pack.wants_model) is not None,
                  f"{tag}: wants a base model this app actually has ({pack.wants_model})")

    # -- the Hololive pack in particular -------------------------------------
    holo = charpacks.get("hololive-collection")
    check(holo is not None, "the Hololive pack is there")
    check(holo.wants_model == "pony", f"…and says it needs Pony ({holo.wants_model})")
    check(holo.size == 913775292, f"…with the size the CivitAI API reported ({holo.size})")
    check(len(holo.characters) == 75, f"75 members ({len(holo.characters)})")
    check(sum(len(c.costumes) for c in holo.characters) == 319,
          f"319 outfits ({sum(len(c.costumes) for c in holo.characters)})")
    # Groups run in debut order, which is the whole reason for grouping at all.
    order = [g.id for g in holo.groups]
    check(order[:4] == ["jp-gen0", "jp-gen1", "jp-gen2", "jp-gamers"],
          f"generations are in debut order ({order[:4]})")
    check(order.index("en-myth") > order.index("jp-regloss")
          and order.index("id-gen1") > order.index("en-justice"),
          f"JP then EN then ID ({order})")
    for who, group in [("gawr-gura", "en-myth"), ("hoshimachi-suisei", "jp-gen0"),
                       ("kobo-kanaeru", "id-gen3"), ("la-darknesss", "jp-gen6")]:
        got = holo.by_key.get(who)
        check(got is not None and got.group == group,
              f"{who} is in {group} ({got.group if got else 'missing'})")
    check(holo.by_key["kiryu-coco"].former, "a graduated member is flagged as such")
    check(not holo.by_key["gawr-gura"].former, "…and an active one is not")

    # -- building a prompt ---------------------------------------------------
    built = charpacks.build_prompt(holo, "hoshimachi-suisei", 0, extra="sitting, night")
    check(built is not None, "a prompt is built")
    tags = [t.strip() for t in built["prompt"].split(",")]
    check(tags[0] == "hoshimachi suisei", f"the trigger leads ({tags[0]})")
    check(r"hoshimachi suisei \(1st costume\)" in built["prompt"], "…and names the outfit")
    check("1girl" in tags and "virtual youtuber" in tags, "the author's scaffold is added")
    check("blue hair" in tags, "the outfit's own tags come along")
    check("sitting" in tags and "night" in tags, "…as does whatever the user typed")
    # Pony reads the score tags as a global quality signal; every example on the
    # model's own page puts them last.
    check(tags[-1] == "very aesthetic", f"quality tags go at the end ({tags[-3:]})")
    check(len(set(t.lower() for t in tags)) == len(tags),
          "no tag is repeated (a doubled tag is a weight nobody asked for)")
    check(built["lora"] == holo.file and built["strength"] == holo.strength,
          "the prompt says which LoRA to switch on, and how hard")
    check("score_4" in built["negative"], "the author's negative prompt comes back too")

    plain = charpacks.build_prompt(holo, "hoshimachi-suisei", 0, quality=False)
    check("score_9" not in plain["prompt"], "quality tags can be turned off")

    # The scaffold says 1girl and so do some outfit lines; deduping is what
    # stops "1girl, 1girl" becoming an accidental emphasis.
    dupe = charpacks.build_prompt(holo, "gawr-gura", 0, extra="1girl, blue eyes, 1girl")
    dtags = [t.strip().lower() for t in dupe["prompt"].split(",")]
    check(dtags.count("1girl") == 1, f"a repeated tag is collapsed ({dtags.count('1girl')})")

    second = charpacks.build_prompt(holo, "gawr-gura", 2)
    check(second["costume"] == holo.by_key["gawr-gura"].costumes[2].label,
          "a different outfit index picks a different outfit")
    over = charpacks.build_prompt(holo, "gawr-gura", 99)
    check(over["costume"] == holo.by_key["gawr-gura"].costumes[0].label,
          "an out-of-range outfit falls back to the first, not a crash")
    check(charpacks.build_prompt(holo, "nobody-here") is None, "an unknown character is None")

    # -- a broken or hand-edited pack file -----------------------------------
    folder = TMP / "packs"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "broken.json").write_text("{ not json", encoding="utf-8")
    (folder / "empty.json").write_text('{"id": "e", "file": "x.safetensors"}', encoding="utf-8")
    (folder / "nofile.json").write_text('{"id": "n", "characters": []}', encoding="utf-8")
    (folder / "good.json").write_text(json.dumps({
        "id": "mine", "label": "My pack", "file": "mine.safetensors",
        "groups": [{"id": "g1", "label": "One", "members": ["a", "ghost"]}],
        "characters": [
            {"key": "a", "name": "A", "costumes": [{"label": "1st", "trigger": "a", "tags": "x"}]},
            {"key": "b", "name": "B", "costumes": [{"label": "1st", "trigger": "b", "tags": "y"}]},
            {"key": "c", "name": "C", "costumes": []},
        ],
        "strength": "not a number",
    }, ensure_ascii=False), encoding="utf-8")
    loaded = charpacks.load(folder)
    check([p.id for p in loaded] == ["mine"],
          f"a malformed pack file is skipped, not fatal ({[p.id for p in loaded]})")
    mine = loaded[0]
    check([c.key for c in mine.characters] == ["a", "b"],
          "a character with no outfits is dropped")
    check(mine.groups[0].members == ["a"], "a group member who does not exist is dropped")
    check(mine.groups[-1].id == "_other" and mine.groups[-1].members == ["b"],
          f"an ungrouped character still gets a home ({[g.id for g in mine.groups]})")
    check(mine.strength == 0.8, f"a non-numeric strength falls back ({mine.strength})")

    # -- the endpoints -------------------------------------------------------
    listed = json.loads((await server.list_packs()).body)
    check(listed["packs"] and listed["packs"][0]["id"] == holo.id, "the pack list is served")
    first = listed["packs"][0]
    for key in ("installed", "model_installed", "model_label", "groups", "characters"):
        check(key in first, f"the list says {key}")
    got = json.loads((await server.pack_prompt(
        holo.id, {"character": "gawr-gura", "costume": 1})).body)
    check("gawr gura" in got["prompt"], "the endpoint builds a prompt")
    check("lora_installed" in got, "…and says whether the LoRA is actually here")
    junk = json.loads((await server.pack_prompt(
        holo.id, {"character": "gawr-gura", "costume": "nonsense"})).body)
    check(junk["costume"] == holo.by_key["gawr-gura"].costumes[0].label,
          "a non-numeric costume index is a fallback, not a 500")
    bare = json.loads((await server.pack_prompt(holo.id, {"character": "gawr-gura"})).body)
    check(bare["prompt"], "a body with no costume builds the first outfit")
    try:
        await server.pack_prompt("no-such-pack", {"character": "x"})
        check(False, "an unknown pack should 404")
    except HTTPException as exc:
        check(exc.status_code == 404, f"an unknown pack is a 404 ({exc.status_code})")
    try:
        await server.pack_prompt(holo.id, {"character": "not-a-member"})
        check(False, "an unknown character should 404")
    except HTTPException as exc:
        check(exc.status_code == 404, f"an unknown character is a 404 ({exc.status_code})")

    # -- the page ------------------------------------------------------------
    html = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check("/api/packs" in html, "the UI fetches the packs")
    check("packswitch" in html and "onImageModelChange()" in html,
          "…and can switch the base model in one click, through the real handler")
    check("/api/packs/${encodeURIComponent(p.id)}/download" in html,
          "…and can download the LoRA in one click")
    check("function packExtra()" in html,
          "switching member does not drag the previous member's tags along")
    check("function packField()" in html and "comicMode() ? $('#cshared')" in html,
          "in comic mode the character lands in the shared box, not the unused one")

    # -- the original artist's style ----------------------------------------
    # Every artist tag here was matched to danbooru through the designer's own
    # registered URL, not by name: fuzzy name search turned "Ordan" into
    # "edward_jordan" (9 posts), and a wrong artist tag steers the style
    # somewhere that has nothing to do with the character.
    tagged = [c for c in holo.characters if c.artist_tag]
    check(len(tagged) >= 70, f"most members carry a designer's artist tag ({len(tagged)}/75)")
    check(all(c.artist_posts >= 40 for c in tagged),
          "…and none of them is a tag too thin to have taught the model anything")
    named = [c for c in holo.characters if c.designer]
    check(len(named) >= 70, f"…and the designer is named even where the tag is missing ({len(named)})")
    check(all(c.wiki.startswith("https://") for c in holo.characters),
          "every character links its official design gallery")
    for key, want in [("mori-calliope", "yukisame"), ("hoshimachi-suisei", "teshima_nari"),
                      ("gawr-gura", "amashiro_natsuki"), ("shirakami-fubuki", "nagishiro_mito")]:
        check(holo.by_key[key].artist_tag == want,
              f"{key} -> {want} ({holo.by_key[key].artist_tag})")
    # Checked and genuinely absent rather than guessed.
    check(not holo.by_key["watson-amelia"].artist_tag,
          "a designer with no danbooru artist tag is left blank, not invented")

    # Each model's own documentation, not one convention applied everywhere:
    # NoobAI's model card prompts with `artist:john_kafka`; the Illustrious
    # guidance is `by ebifurya`.
    check(holo.artist_tag_models == {"noobai": "artist:{tag}", "illustrious": "by {tag}"},
          f"each danbooru model gets the artist form it documents ({holo.artist_tag_models})")
    check("pony" not in holo.artist_tag_models,
          "…and Pony is not one of them: its model card says artist names were removed")
    check(holo.wants_model not in holo.artist_tag_models,
          "…which is not the model this LoRA needs - that tension is the point")

    # NoobAI-XL is the answer to "the output looks bad": it is Illustrious
    # re-tuned on the full danbooru + e621 set, so unlike Pony it keeps artist
    # tags AND knows these characters. Every number below is off its model card.
    noob = images.get("noobai")
    check(noob is not None, "NoobAI-XL is in the catalogue")
    check(noob.file.size == 7105349958, f"…at the size HF reports ({noob.file.size})")
    check(noob.sampler == "euler_ancestral" and 5 <= noob.cfg <= 6 and 25 <= noob.steps <= 30,
          f"…with the model card's sampler/cfg/steps ({noob.sampler}, {noob.cfg}, {noob.steps})")
    check(noob.default_size == "832×1216 直式", f"…and its preferred size ({noob.default_size})")
    check(noob.positive_prefix == "masterpiece, best quality, newest, absurdres, highres",
          f"…and its prefix verbatim ({noob.positive_prefix})")
    # The card ships `nsfw` in the negative and `safe` in the prefix. This app
    # has no content filter, so silently negating what the user asked for would
    # be the wrong default.
    check("nsfw" not in noob.negative, "the card's `nsfw` negative is dropped, not smuggled in")
    check("safe" not in noob.positive_prefix.split(", "), "…and so is `safe`")
    check("mammal" in noob.negative and "furry" in noob.negative,
          "…while the rest of the card's negative is kept")
    check("noobai" in holo.native_models, "the pack knows NoobAI can draw these characters")

    series = charpacks.build_prompt(holo, "mori-calliope", 0, model="noobai")
    stags = [t.strip() for t in series["prompt"].split(",")]
    check("hololive" in stags, f"the series tag is added on a danbooru model ({stags[:4]})")
    check(stags.index("hololive") < stags.index("1girl"),
          "…in the caption order NoobAI documents: character, series, artist, then the rest")
    plain_pony = charpacks.build_prompt(holo, "mori-calliope", 0, model="pony")
    check("hololive" not in [t.strip() for t in plain_pony["prompt"].split(",")],
          "…and not on Pony, which was not captioned that way")

    calli = charpacks.build_prompt(holo, "mori-calliope", 0, model="pony", style=True)
    check(not calli["style"]["applied"],
          "asking for the artist's style on Pony does not silently do nothing")
    check("by yukisame" not in calli["prompt"], "…the tag is not added")
    check("沒有畫師名字" in calli["style"]["why"]
          and "沒有實測過" in calli["style"]["why"],
          f"…and says why without overclaiming: Pony's captions have no artist "
          f"names, and what it does with one anyway was never measured here "
          f"({calli['style']['why'][:30]})")
    check("12496" in calli["style"]["why"] or "danbooru" in calli["style"]["why"],
          "…and points at the way that does work")

    illus = charpacks.build_prompt(holo, "mori-calliope", 0, model="illustrious", style=True)
    check(illus["style"]["applied"], "on Illustrious it is applied")
    tags2 = [t.strip() for t in illus["prompt"].split(",")]
    check("by yukisame" in tags2, f"…as 'by <artist>' on Illustrious ({tags2[:4]})")
    nb = charpacks.build_prompt(holo, "mori-calliope", 0, model="noobai", style=True)
    ntags = [t.strip() for t in nb["prompt"].split(",")]
    check("artist:yukisame" in ntags,
          f"…and as 'artist:<artist>' on NoobAI, which is what its card prompts with ({ntags[:4]})")
    check("by yukisame" not in ntags, "…not both forms at once")
    check(tags2.index("by yukisame") <= 3,
          f"…right after the character and series, where NoobAI's caption order puts it ({tags2[:4]})")
    off = charpacks.build_prompt(holo, "mori-calliope", 0, model="illustrious", style=False)
    check("by yukisame" not in off["prompt"], "…and only when asked for")

    # -- weighting the artist -------------------------------------------------
    # `{{tag}}` is NovelAI syntax. ComfyUI's parser only knows `(x)` and
    # `(x:1.3)`, so the braces would land in the prompt as literal text. The
    # weights below are therefore emitted in the one form ComfyUI parses, and
    # checked against a re-implementation of its own splitting rule.
    def comfy_weight(text):
        """ComfyUI 0.33 splits a parenthesised group on its LAST colon."""
        if not (text.startswith("(") and text.endswith(")")):
            return text, 1.0
        inner = text[1:-1]
        cut = inner.rfind(":")
        if cut <= 0:
            return inner, 1.1
        try:
            return inner[:cut], float(inner[cut + 1:])
        except ValueError:
            return inner, 1.1

    check(charpacks.weighted("artist:x", 1.0) == "artist:x",
          "weight 1.0 emits the bare tag, no pointless parentheses")
    heavy = charpacks.weighted("artist:amashiro_natsuki", 1.35)
    check(heavy == "(artist:amashiro_natsuki:1.35)", f"…and above 1.0 wraps it ({heavy})")
    # The colon inside the tag is the trap: a parser splitting on the FIRST
    # colon would read the weight as "amashiro_natsuki:1.35" and give up.
    tag, weight = comfy_weight(heavy)
    check(tag == "artist:amashiro_natsuki" and weight == 1.35,
          f"ComfyUI reads it back as tag+weight, colon in the tag and all ({tag}, {weight})")
    check(charpacks.weighted("artist:x", 99) == "(artist:x:2)"
          and charpacks.weighted("artist:x", -5) == "(artist:x:0.1)",
          "an absurd weight is clamped rather than sent on")
    # The browser previews this same token before the request is made, and JS
    # prints 2 where Python's str() prints 2.0. A preview that does not match
    # what is sent is worse than no preview.
    check(charpacks.weighted("artist:x", 1.20) == "(artist:x:1.2)",
          f"the weight is formatted the way JS would ({charpacks.weighted('artist:x', 1.20)})")

    for w, want in [(1.0, "artist:yukisame"), (1.25, "(artist:yukisame:1.25)")]:
        got = charpacks.build_prompt(holo, "mori-calliope", 0, model="noobai",
                                     style=True, artist_weight=w)
        check(got["style"]["emitted"] == want,
              f"weight {w} emits {want} ({got['style']['emitted']})")
        check(want in got["prompt"], "…and it is in the prompt")
    # A hand-typed copy of the same artist would be a second, unweighted pull.
    # Every spelling of the same artist a user might reasonably type, at both
    # the weighted and the unweighted setting. The parenthesised ones are the
    # ones the FAQ actively teaches, and they used to slip straight past.
    for weight in (1.0, 1.3):
        want = charpacks.weighted("artist:yukisame", weight)
        for typed in ("artist:yukisame", "by yukisame", "yukisame",
                      "(artist:yukisame:1.2)", "((yukisame))", "(by yukisame:0.9)"):
            both = charpacks.build_prompt(holo, "mori-calliope", 0, model="noobai",
                                          style=True, artist_weight=weight,
                                          extra=f"{typed}, night")
            btags = [t.strip() for t in both["prompt"].split(",")]
            hits = [t for t in btags if "yukisame" in t]
            check(hits == [want],
                  f"w={weight} with {typed!r} typed leaves exactly one artist tag ({hits})")
            check("night" in btags, "…without eating the rest of what was typed")

    page_txt = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check("packstylew" in page_txt and "畫師權重" in page_txt,
          "the page has the weight control")
    check("packstyletok" in page_txt,
          "…and shows the exact token it will emit, at that weight")
    import prompts as pmod
    check(any("{{" in a for a, _ in pmod.NOT_SUPPORTED),
          "the syntax help warns that NovelAI's {{ }} does nothing in ComfyUI")

    swapped = charpacks.build_prompt(holo, "mori-calliope", 0, model="illustrious",
                                     quality_tags="masterpiece, best quality, very aesthetic")
    check("score_9" not in swapped["prompt"] and "very aesthetic" in swapped["prompt"],
          "a different base model gets its own quality tags, not Pony's score ladder")

    nomama = charpacks.build_prompt(holo, "watson-amelia", 0, model="illustrious", style=True)
    check(not nomama["style"]["applied"] and "沒有可用的畫師標籤" in nomama["style"]["why"],
          f"a member with no artist tag says so plainly ({nomama['style']['why'][:30]})")

    styled = json.loads((await server.pack_prompt(holo.id, {
        "character": "hoshimachi-suisei", "model": "illustrious", "style": True})).body)
    check(styled["style"]["applied"] and "by teshima_nari" in styled["prompt"],
          "the endpoint honours the style request")
    check("packstylechk" in html and "官方設定圖" in html,
          "the page offers the toggle and links the official design sheets")
    check("ControlNet" in html and "packstyleswitch" in html,
          "…and offers both routes: switch model, or use the design sheet as a reference")
    guide = ROOT / "docs" / "character-packs.md"
    check(guide.is_file(), "the character-pack tutorial exists")
    check("docs/character-packs.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")
    text = guide.read_text(encoding="utf-8")
    for topic in ("app/packs/", "wants_model", r"\\(", "Pony"):
        check(topic in text, f"the tutorial covers {topic}")


async def test_settings_and_updates() -> None:
    """The .env box and the ComfyUI update button.

    Both exist because the app used to end an instruction with "填進 .env 然後
    重啟" or "在 ComfyUI 資料夾按 git pull" and then leave the user there.
    """
    import shutil
    import subprocess

    from fastapi import HTTPException

    import envfile
    import server
    import updates

    section("settings and updates")

    env = TMP / "envtest" / ".env"
    env.parent.mkdir(parents=True, exist_ok=True)
    env.write_text(
        "# 這是註解，不能被吃掉\n"
        "MODEL=wan22-14b-q4\n"
        "COMFY_ARGS=--lowvram\n"
        "\n"
        "# 另一段註解\n"
        "LORAS=x.safetensors:0.8\n",
        encoding="utf-8",
    )
    got = envfile.read(env)
    check(got["MODEL"] == "wan22-14b-q4" and got["COMFY_ARGS"] == "--lowvram",
          f"existing values are read ({got}) ")

    envfile.write("CIVITAI_API_KEY", "abcd1234efgh5678", env)
    text = env.read_text(encoding="utf-8")
    check("CIVITAI_API_KEY=abcd1234efgh5678" in text, "a new key is appended")
    check("# 這是註解，不能被吃掉" in text and "# 另一段註解" in text,
          "…and every comment in the file survives")
    check("LORAS=x.safetensors:0.8" in text, "…as does every other setting")
    check(os.environ.get("CIVITAI_API_KEY") == "abcd1234efgh5678",
          "the running process picks it up immediately, with no restart")
    import civitai
    check(civitai.api_key() == "abcd1234efgh5678", "…so downloads work right away")

    envfile.write("COMFY_ARGS", "--novram", env)
    lines = [l for l in env.read_text(encoding="utf-8").splitlines()
             if l.startswith("COMFY_ARGS")]
    check(lines == ["COMFY_ARGS=--novram"],
          f"an existing key is replaced in place, not duplicated ({lines})")

    envfile.write("CIVITAI_API_KEY", "", env)
    check("CIVITAI_API_KEY" not in env.read_text(encoding="utf-8"),
          "clearing removes the line rather than leaving KEY=")
    check(not os.environ.get("CIVITAI_API_KEY"), "…and unsets it live too")

    # A settings box must never become a general environment writer.
    for bad in ("PATH", "MODELS_DIR", "PYTHONPATH", ""):
        try:
            envfile.write(bad, "x", env)
            check(False, f"{bad} should be refused")
        except ValueError:
            check(True, f"{bad} cannot be set from the browser")
    try:
        envfile.write("CIVITAI_API_KEY", "line1\nMODELS_DIR=/etc", env)
        check(False, "a newline should be refused")
    except ValueError:
        check(True, "a value cannot smuggle in a second line")

    check(envfile.mask("abcd1234efgh5678") == "abcd••••••••5678",
          f"a secret is shown masked ({envfile.mask('abcd1234efgh5678')})")
    check(envfile.mask("") == "" and envfile.mask("short") == "•••••",
          "…and a short one gives nothing away")
    fresh = TMP / "envtest2" / ".env"
    envfile.write("CIVITAI_API_KEY", "k", fresh)
    check(fresh.is_file() and fresh.read_text(encoding="utf-8").strip() == "CIVITAI_API_KEY=k",
          "a missing .env is created rather than erroring")
    envfile.write("CIVITAI_API_KEY", "", fresh)

    names = {f["name"] for f in envfile.state(env)}
    check(names == set(envfile.WRITABLE), f"the page lists every writable setting ({names})")

    body = json.loads((await server.get_settings()).body)
    check(body["settings"] and body["file"], "the endpoint serves them")
    try:
        await server.set_setting({"name": "PATH", "value": "/tmp"})
        check(False, "PATH should be refused by the endpoint too")
    except HTTPException as exc:
        check(exc.status_code == 400, f"an unwritable name is a 400 ({exc.status_code})")

    # -- pulling ComfyUI -----------------------------------------------------
    if not shutil.which("git"):
        check(True, "git not installed here; skipping the pull test")
    else:
        base = TMP / "gitpull"
        shutil.rmtree(base, ignore_errors=True)
        origin, clone = base / "origin", base / "clone"
        origin.mkdir(parents=True)
        run = lambda cwd, *a: subprocess.run(["git", "-C", str(cwd), *a],  # noqa: E731
                                             capture_output=True, text=True)
        subprocess.run(["git", "init", "--quiet", "-b", "main", str(origin)],
                       capture_output=True)
        (origin / "nodes.py").write_text("one\n")
        run(origin, "add", "-A")
        run(origin, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "one")
        subprocess.run(["git", "clone", "--quiet", str(origin), str(clone)],
                       capture_output=True)
        # Untracked files are what models/ and custom_nodes/ are, so this is the
        # thing that must survive.
        (clone / "models").mkdir()
        (clone / "models" / "big.safetensors").write_text("MODEL")

        same = updates.pull(clone)
        check(same["ok"] and "最新" in same["detail"], f"an up-to-date checkout says so ({same})")

        (origin / "nodes.py").write_text("two\n")
        run(origin, "add", "-A")
        run(origin, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "two")
        moved = updates.pull(clone)
        check(moved["ok"] and moved["before"] != moved["after"],
              f"a behind checkout fast-forwards ({moved})")
        check((clone / "nodes.py").read_text().strip() == "two", "…and the code is new")
        check((clone / "models" / "big.safetensors").read_text() == "MODEL",
              "the models sitting inside ComfyUI are untouched")

        # A user who edited a tracked file must not have it clobbered.
        (clone / "nodes.py").write_text("mine\n")
        (origin / "nodes.py").write_text("three\n")
        run(origin, "add", "-A")
        run(origin, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "three")
        dirty = updates.pull(clone)
        check(not dirty["ok"] and "改過" in dirty["detail"],
              f"a modified checkout is left alone, with a reason ({dirty['detail'][:40]})")
        check("nodes.py" in dirty["detail"],
              f"…naming the file whole, not clipped ({dirty['detail'][-20:]})")
        check((clone / "nodes.py").read_text().strip() == "mine", "…and the edit survives")

        nogit = base / "plain"
        nogit.mkdir(parents=True)
        out = updates.pull(nogit)
        check(not out["ok"] and "git" in out["detail"], "a non-git folder says so, not crashes")

    # -- the update script now covers ComfyUI too ----------------------------
    script = (ROOT / "update-windows.ps1").read_bytes().decode("utf-8-sig")
    check("$keep = @('ComfyUI', 'venv', 'data', 'models', '.env')" in script,
          "ComfyUI is still on the never-overwrite list (every model lives there)")
    check("'pull', '--ff-only'" in script,
          "…and is instead updated in place, which is why it used to fall behind")
    check("'status', '--porcelain'" in script,
          "…skipping it when the user has edited it")

    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check("/api/settings" in page, "the settings tab writes .env itself")
    check("setpullcomfy" in page and "/api/updates/comfy/pull" in page,
          "…and has the button the 'git pull' notice used to just describe")
    check("為什麼 update.bat 更新完 ComfyUI 還是舊的" in page,
          "…and explains why the two update separately")
    faq = ROOT / "docs" / "faq.md"
    check(faq.is_file(), "the FAQ answering all of this exists")
    text = faq.read_text(encoding="utf-8")
    for topic in ("API Keys", "git pull --ff-only", "$keep = @('ComfyUI'",
                  "總強度", "by yukisame", "沒有顯卡",
                  # The three the user hit this round.
                  "內容和構圖都沒有", "✕ 清除分鏡", "NoobAI-XL",
                  "(artist:amashiro_natsuki:1.3)", "artist:john_kafka",
                  "prefers-reduced-motion", "--line-strong", "browser_check.js",
                  "NativeCommandError", "Invoke-Git"):
        check(topic in text, f"the FAQ covers {topic}")
    check("docs/faq.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")
    check("id=\"iloranote\"" in page and "function loraBudget()" in page,
          "the LoRA list shows a live strength budget")


def test_vendored_skill() -> None:
    """The vendored ui-ux-pro-max skill is present and its scripts run.

    It is committed rather than installed per-machine, so it has to keep
    working like any other file in the repo - and its own scripts are the only
    thing that can say whether the data files came across intact.
    """
    import subprocess

    section("vendored skill")
    root = ROOT.parent / ".claude" / "skills" / "ui-ux-pro-max"
    if not root.is_dir():
        check(False, f"the skill directory exists ({root})")
        return
    check(True, "the skill directory exists")
    skill = root / "SKILL.md"
    check(skill.is_file(), "SKILL.md is there")
    text = skill.read_text(encoding="utf-8")
    check(text.startswith("---\nname: ui-ux-pro-max"),
          "…with the frontmatter Claude Code needs to register it")
    check("{{" not in text, "…and no unsubstituted template placeholders")
    check((root / "LICENSE").is_file(), "the upstream MIT licence travelled with it")
    check((root / "INSTALLED.md").is_file(), "…and a note saying where it came from")
    check((root / "data" / "styles.csv").is_file(), "the data files came across")

    search = root / "scripts" / "search.py"
    check(search.is_file(), "search.py is there")
    done = subprocess.run(
        [sys.executable, str(search), "form validation", "--domain", "ux"],
        capture_output=True, text=True, timeout=120,
    )
    check(done.returncode == 0 and "Search Results" in done.stdout,
          f"…and it runs ({(done.stdout or done.stderr).strip()[:60]})")
    # Standard library only is the whole reason this is safe to vendor.
    imports = set()
    for py in (root / "scripts").glob("*.py"):
        for line in py.read_text(encoding="utf-8").splitlines():
            if line.startswith(("import ", "from ")):
                imports.add(line.split()[1].split(".")[0])
    third_party = imports - set(sys.stdlib_module_names) - {"core", "design_system",
                                                            "reasoning_contract"}
    check(not third_party, f"the scripts need no third-party packages ({third_party or 'none'})")


def test_accessibility() -> None:
    """The CRITICAL items from the UI/UX review, as properties of the page.

    All measurable, all counted from the markup rather than eyeballed. Each one
    was failing before the review: no focus ring at all, three icon-only
    buttons with no name, no reduced-motion support, no landmarks, and a tab
    strip that told assistive tech nothing about what was selected.
    """
    section("accessibility")
    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", page, re.S).group(1)

    def luminance(hex_colour: str) -> float:
        raw = hex_colour.lstrip("#")
        parts = [int(raw[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        parts = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in parts]
        return 0.2126 * parts[0] + 0.7152 * parts[1] + 0.0722 * parts[2]

    def contrast(a_hex: str, b_hex: str) -> float:
        la, lb = luminance(a_hex), luminance(b_hex)
        return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

    tokens = dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6});", css))
    for name in ("bg", "panel", "panel2", "text", "muted", "accent", "line-strong"):
        check(name in tokens, f"the palette defines --{name}")

    # Body text on every surface it can land on.
    for surface in ("bg", "panel", "panel2"):
        got = contrast(tokens["text"], tokens[surface])
        check(got >= 4.5, f"body text on --{surface} meets AA ({got:.2f}:1)")
        quiet = contrast(tokens["muted"], tokens[surface])
        check(quiet >= 4.5, f"secondary text on --{surface} meets AA ({quiet:.2f}:1)")
    # A control's border is often the only thing marking where the control is,
    # which puts it under the non-text 3:1 rule rather than the decorative one.
    for surface in ("bg", "panel", "panel2"):
        edge = contrast(tokens["line-strong"], tokens[surface])
        check(edge >= 3.0, f"control borders on --{surface} meet the 3:1 minimum ({edge:.2f}:1)")

    check(":focus-visible" in css, "there is a focus-visible ring")
    check(re.search(r":focus-visible[^{]*\{[^}]*outline:\s*\d", css) is not None,
          "…and it is a real outline, not just a colour change")
    check(not re.search(r"outline:\s*none", re.sub(r"/\*.*?\*/", "", css, flags=re.S)),
          "nothing strips the outline without replacing it")
    check("prefers-reduced-motion" in css, "motion respects the OS setting")

    # An icon-only control has no accessible name unless it is given one.
    nameless = []
    for m in re.finditer(r"<button([^>]*)>(.*?)</button>", page, re.S):
        attrs, inner = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if "aria-label" in attrs or not inner:
            continue
        # Digits are a real label ("1.2" on a preset button), so only a label
        # made purely of symbols or emoji counts as nameless.
        if not re.sub(r"[^\w]", "", inner, flags=re.UNICODE):
            nameless.append(inner[:12])
    check(not nameless, f"every icon-only button has an accessible name ({nameless or 'all named'})")

    check("<nav" in page and 'role="tablist"' in page, "the tab strip is a labelled navigation landmark")
    check(page.count('role="tab"') == page.count('role="tabpanel"') == len(
        re.findall(r'<button[^>]*data-tab="', page)),
        "every tab has a panel and both are announced as such")
    # Per element, not by global count. Counting every aria-controls on the page
    # and comparing to the number of tabs asserted something that was never the
    # rule: a disclosure button is *supposed* to carry aria-controls alongside
    # aria-expanded, so the first collapsible panel added to the page failed a
    # test about tabs.
    tabs_without_target = [
        m.group(0)[:60] for m in re.finditer(r"<button[^>]*>", page)
        if 'role="tab"' in m.group(0) and "aria-controls" not in m.group(0)
    ]
    check(not tabs_without_target,
          f"…and each tab names the panel it controls ({tabs_without_target or 'all do'})")
    check("x.setAttribute('aria-selected'" in page,
          "the selected tab is kept truthful for assistive tech, not just styled")
    check("ArrowRight" in page and "ArrowLeft" in page,
          "a tablist is one tab stop with arrow-key movement between tabs")

    # A placeholder vanishes the moment you type, so it cannot be the only name.
    #
    # Three things name a control, and this has to accept all three or it fails
    # valid markup: aria-label, an explicit `for=`, and a wrapping <label>. The
    # implicit form is what most of this page already uses; the test only passed
    # before because every placeholder-bearing input happened to also carry an
    # aria-label, so the first `<label class="f">…<input placeholder></label>`
    # tripped it.
    body = page[page.index("</style>"):page.index("<script>")]
    wrapped: set[str] = set()
    for m in re.finditer(r"<label\b[^>]*>(.*?)</label>", body, re.S):
        for inner in re.finditer(r'<(?:input|textarea|select)\b[^>]*id="([^"]+)"',
                                 m.group(1)):
            wrapped.add(inner.group(1))
    unnamed = []
    for m in re.finditer(r"<(input|textarea)\b([^>]*)>", body):
        attrs = m.group(2)
        ident = re.search(r'id="([^"]+)"', attrs)
        if not ident or "aria-label" in attrs or "hidden" in attrs:
            continue
        name = ident.group(1)
        if "placeholder=" in attrs and f'for="{name}"' not in body and name not in wrapped:
            unnamed.append(name)
    check(not unnamed, f"no control relies on its placeholder as its name ({unnamed or 'none do'})")

    # -- the two layout bugs a real browser found ----------------------------
    # Both were invisible to every static check here and to the JS harness;
    # they only showed up by loading the page in Chromium at 375px.
    chk = re.search(r"\.chk \{[^}]*\}", css, re.S)
    check(chk is not None, "the checkbox-label rule is still there")
    check(chk and "white-space:nowrap" not in chk.group(0),
          "checkbox labels can wrap - nowrap pushed the page 112px past a 375px phone")
    check("overflow-wrap:anywhere" in css.replace(" ", ""),
          "long machine strings (tag lists, filenames) are allowed to break")
    check(re.search(r"\.row > \*\s*\{[^}]*min-width:\s*0", css) is not None,
          "…and flex children may shrink below their content")
    check('rel="icon"' in page,
          "a favicon is supplied - its absence was a 404 and a console error on every load")


def test_naiweights() -> None:
    """NAI syntax -> ComfyUI weights, checked against ComfyUI's own parser.

    This is the load-bearing conversion in the pose database, and the whole
    reason it exists is that ComfyUI honours exactly one weighting construct.
    So the assertions are not "my function returns what I expect" - they run the
    output through a copy of comfy/sd1_clip.py's parse_parentheses/token_weights
    and check the weight CLIP would actually receive.
    """
    section("naiweights (NAI -> ComfyUI)")
    import naiweights as nw

    # A local transcription of ComfyUI 0.33's parser. Kept short deliberately:
    # it is the entire grammar, which is the point being tested.
    def parse_parens(string):
        result, current, nest = [], "", 0
        for char in string:
            if char == "(":
                if nest == 0:
                    if current:
                        result.append(current)
                    current = "("
                else:
                    current += char
                nest += 1
            elif char == ")":
                nest -= 1
                if nest == 0:
                    result.append(current + ")")
                    current = ""
                else:
                    current += char
            else:
                current += char
        if current:
            result.append(current)
        return result

    def token_weights(string, current_weight):
        out = []
        for x in parse_parens(string):
            weight = current_weight
            if len(x) >= 2 and x[-1] == ")" and x[0] == "(":
                x = x[1:-1]
                xx = x.rfind(":")
                weight *= 1.1
                if xx > 0:
                    try:
                        weight = float(x[xx + 1:])
                        x = x[:xx]
                    except ValueError:
                        pass
                out += token_weights(x, weight)
            else:
                out += [(x, current_weight)]
        return out

    def comfy_sees(text):
        # escape_important/unescape_important, so `\(` is protected exactly as
        # ComfyUI protects it.
        t = text.replace("\\)", "\0\1").replace("\\(", "\0\2")
        got = token_weights(t, 1.0)
        return [(x.replace("\0\1", ")").replace("\0\2", "(").strip(), round(w, 4))
                for x, w in got if x.strip()]

    def weight_of(text, tag):
        return next((w for t, w in comfy_sees(text) if t == tag), None)

    # NAI braces step by 1.05, not SD's 1.1: five of them is 1.276, not 1.61.
    out = nw.convert("{{{{{vacuum fellatio}}}}}").prompt()
    check(weight_of(out, "vacuum fellatio") == 1.28,
          f"{{}}x5 becomes 1.05^5 = 1.28 ({out})")
    out = nw.convert("[[[deepthroat]]]").prompt()
    check(weight_of(out, "deepthroat") == 0.86, f"[]x3 becomes 1/1.05^3 = 0.86 ({out})")

    # NAI4.5 numeric weights, distributed over the whole group.
    out = nw.convert("1.35::breasts press,girl arms around another's waist::").prompt()
    check(weight_of(out, "breasts press") == 1.35
          and weight_of(out, "girl arms around another's waist") == 1.35,
          f"N::a,b:: puts N on both tags ({out})")

    # A negative NAI weight has no positive-prompt equivalent, so it moves.
    conv = nw.convert("1girl,-2::pov::")
    check("pov" not in conv.prompt(), "a negative NAI weight leaves the positive prompt")
    check(weight_of(conv.negative_prompt(), "pov") == 2.0,
          f"…and lands in the negative at abs(weight) ({conv.negative_prompt()})")
    check(any("負權重" in n for n in conv.notes), "…and the move is reported, not silent")

    # Character names must be escaped or ComfyUI reweights half of them.
    out = nw.convert("{{{{{{{{elaina (majo no tabitabi)}}}}}}}}").prompt()
    check(weight_of(out, "elaina (majo no tabitabi)") == 1.48,
          f"a name's own parens are escaped, not read as weighting ({out})")
    check("\\(" in out, "…which means the emitted text carries backslashes")

    # The codex's `aritst:` typo silently disables the artist, so it is fixed.
    conv = nw.convert("{{aritst:deadflow}}")
    check(conv.artist_prompt().startswith("(artist:deadflow"),
          f"aritst: is corrected to artist: ({conv.artist_prompt()})")
    check(any("aritst" in n for n in conv.notes), "…and says so")

    # Artists come out as their own group - the feature the user asked for.
    conv = nw.convert("1girl,[artist:ciloranko],((artist:CiloRanko)),fellatio")
    check(conv.artist_prompt() and "artist:ciloranko" in conv.artist_prompt(),
          "artist tokens are separated from the pose")
    check("artist" not in conv.prompt(artists=False),
          f"…and the pose string has none left ({conv.prompt(artists=False)})")
    check(weight_of(conv.artist_prompt(), "artist:ciloranko") == 0.95,
          "…keeping the weight the [] asked for")
    check(weight_of(conv.artist_prompt(), "artist:CiloRanko") == 1.21,
          "…and SD-style (()) too, since the document mixes both")

    # `(artist:x:1.05)` only works because ComfyUI splits on the LAST colon.
    check(weight_of("(artist:ciloranko:1.05)", "artist:ciloranko") == 1.05,
          "a weighted artist token survives its own colon")

    # An unclosed name paren in the source is closed rather than shipped broken.
    out = nw.convert("{w(arknights}").prompt()
    check(weight_of(out, "w(arknights)") == 1.05,
          f"an unbalanced name paren from the source is repaired ({out})")

    # Weights are clamped, so a stacked source cannot produce nonsense.
    out = nw.convert("{" * 40 + "x" + "}" * 40).prompt()
    check(weight_of(out, "x") == nw.MAX_WEIGHT, f"weights are clamped ({out})")

    # `:g` formatting has to match charpacks and the JS mirror of it.
    check(nw.render(nw.Chunk("x", 1.2)) == "(x:1.2)", "1.20 prints as 1.2, not 1.20")


def test_posebook() -> None:
    """The shipped pose database: structure, separation, and the safety filter."""
    section("posebook")
    import posebook

    posebook.clear_cache()
    books = posebook.load_all()
    check(len(books) >= 1, f"a pose codex ships with the app ({len(books)} found)")
    book = books[0]
    check(book.id and book.name, f"…with an id and a name ({book.id})")

    # Accounting against the source document: it holds 288 `####` headings, one
    # of which is a mis-promoted field, so 287 real entries - 2 blocked = 285.
    check(len(book.poses) == 285,
          f"285 entries parsed ({len(book.poses)})")
    check(book.skipped == 2, f"2 entries excluded by the minors filter ({book.skipped})")
    check(book.skipped_variants >= 3,
          f"…plus variants inside otherwise-fine entries ({book.skipped_variants})")

    variants = [v for p in book.poses for v in p.variants]
    check(len(variants) >= 400, f"{len(variants)} tag strings in total")
    check(all(p.id for p in book.poses), "every entry has an id")
    check(len({p.id for p in book.poses}) == len(book.poses), "…and the ids are unique")
    check(all(p.title for p in book.poses), "every entry has a title")
    check(all(p.group and p.section for p in book.poses),
          "every entry keeps its place in the document's own taxonomy")

    groups = {p.group for p in book.poses}
    check(len(groups) == 8,
          f"8 of the document's 10 groups have entries; 2 are empty in the source ({len(groups)})")
    check(any(p.people == "單女" for p in book.poses),
          "the group name is read as a head-count, which is the useful filter")

    # -- no NAI syntax survives anywhere -------------------------------------
    leftover = []
    for pose in book.poses:
        for v in pose.variants:
            for field_name in ("prompt", "artists", "characters", "negative"):
                text = getattr(v, field_name)
                if re.search(r"[{}\[\]]", text) or "::" in text:
                    leftover.append((pose.title, field_name, text[:60]))
    check(not leftover, f"no NAI bracket or :: syntax survives conversion ({leftover[:3]})")

    # -- artists are separated, which is the point ---------------------------
    # 69 of the 415 tag strings carry an artist run, spread over 40 entries and
    # 26 distinct artists. Measured, not guessed - a first pass at this test
    # asserted >=100 from misreading the artist index (which counts entries per
    # artist, not strings) and failed on correct data.
    with_artists = [v for v in variants if v.artists]
    check(len(with_artists) == 69,
          f"69 tag strings carried artist tags ({len(with_artists)})")
    check(sum(1 for p in book.poses if any(v.artists for v in p.variants)) == 40,
          "…across 40 entries")
    strays = [v.prompt[:60] for v in variants
              if re.search(r"\bartist\s*:", v.prompt, re.I)]
    check(not strays, f"…and not one is left in a pose string ({strays[:2]})")
    check(all(a.startswith("artist:") or a.startswith("(artist:")
              for v in with_artists for a in posebook._split_top(v.artists)),
          "the artist group holds only artist tokens")
    index = book.artist_index()
    check(len(index) >= 20, f"the artists are also readable as a list ({len(index)} of them)")
    check(index == sorted(index, key=lambda a: (-a["uses"], a["name"])),
          "…ordered by how often the document uses them")

    # -- the tester's own cast is separated too -------------------------------
    cast = [v for v in variants if v.characters]
    check(len(cast) >= 40, f"{len(cast)} strings carried the tester's demo character")
    names = {n for v in cast for n in v.character_names}
    check("elaina (majo no tabitabi)" in names,
          f"…the most common one is found ({sorted(names)[:3]})")
    check(any("houshou marine" in n for n in names),
          "…including a Hololive member, which is exactly why this matters")
    check(not [v for v in variants
               if any(posebook.is_character(c) for c in posebook._split_top(v.prompt))],
          "no demo character is left in a pose string")

    # -- the minors filter ---------------------------------------------------
    check(posebook.blocked("1girl, (aged down:1.16), (child:1.16)"),
          "the filter sees a weighted tag, not just a bare one")
    check(posebook.blocked("1girl,shota,nsfw"), "…and a bare one")
    check(not posebook.blocked("1girl, (qi lolita:1.1), lolita fashion"),
          "…and does not confuse a clothing style with an age")
    check(not posebook.blocked("1girl, childe (genshin impact)"),
          "…nor a name that merely contains a blocked word")
    reached: list[str] = []
    for pose in book.poses:
        for v in pose.variants:
            if posebook.blocked(v.prompt) or posebook.blocked(v.raw):
                reached.append(pose.title)

    check(not reached, f"no blocked variant reached the shipped database ({reached[:3]})")

    # A kindergarten uniform on an adult is a costume; the aged-down variant of
    # the same entry is not. Dropping the variant and keeping the entry is the
    # precise behaviour, so it is pinned.
    uniform = next((p for p in book.poses if "幼儿园" in p.title), None)
    check(uniform is not None, "the costume entry survives")
    if uniform:
        check(not any("幼化" in v.label for v in uniform.variants),
              "…while its aged-down variant does not")

    # -- placeholders --------------------------------------------------------
    slots = {s for v in variants for s in v.placeholders}
    check(slots, f"the author's fill-in slots are found and flagged ({sorted(slots)[:3]})")
    check(any("场景" in s for s in slots), "…including the scene slot")
    check(not any(s in (":>=", "@ @", "?", "69") for s in slots),
          "…and real danbooru tags with no letters are not mistaken for slots")

    # -- prose never reaches a prompt ----------------------------------------
    cjk = re.compile(r"[一-鿿]")
    prose = []
    for pose in book.poses:
        for chunk in posebook._split_top(pose.negative):
            if cjk.search(chunk):
                prose.append((pose.title, chunk))
    check(not prose, f"no Chinese prose leaked into a negative prompt ({prose[:3]})")

    # -- one-click assembly --------------------------------------------------
    pose = next(p for p in book.poses if any(v.artists for v in p.variants))
    idx = next(i for i, v in enumerate(pose.variants) if v.artists)
    plain = posebook.build_prompt(pose, idx, head="mori calliope, hololive")
    check(plain["prompt"].startswith("mori calliope, hololive"),
          "the character you asked for goes first")
    check("artist:" not in plain["prompt"],
          "artists are OFF by default, so they cannot overrule your own choice")
    withart = posebook.build_prompt(pose, idx, artists=True, artist_weight=1.3,
                                    head="mori calliope, hololive")
    check("artist:" in withart["prompt"], "…and ON when asked")
    check(withart["prompt"].index("artist:")
          < withart["prompt"].index(pose.variants[idx].prompt.split(",")[0]),
          "…placed between the character and the pose, per the codex's own advice")
    check("chibi" in withart["negative"],
          "…with the negative the codex prescribes for artist strings")
    check("chibi" not in plain["negative"],
          "…which is not added when the artists are off")

    # The switch has to work on the version shown FIRST, or it reads as broken.
    # In this document the canonical `主要 Tag` string is always the artist-free
    # one and the artist run lives on `Tag 1`/`Tag 2`, so zero entries carry
    # artists on variant 0. Found in a real browser: ticking "bring the artists
    # in" changed nothing on every single pose.
    firsts = [p for p in book.poses if p.variants[0].artists]
    check(not firsts,
          "no entry has artists on its first variant - which is why they are "
          f"treated as belonging to the entry ({len(firsts)})")
    have_artists = [p for p in book.poses if p.artists]
    check(len(have_artists) == 40,
          f"40 entries expose an entry-level artist run ({len(have_artists)})")
    for p in have_artists[:20]:
        built = posebook.build_prompt(p, 0, artists=True)
        if not re.search(r"\bartist\s*:", built["prompt"]):
            check(False, f"the artist switch does nothing on {p.title} variant 0")
            break
    else:
        check(True, "…and the switch works on variant 0 for every one of them")
    borrowed = posebook.build_prompt(have_artists[0], 0, artists=True)
    check(borrowed["artists_borrowed"] is True,
          "…reporting that the run was borrowed from another version")
    check(borrowed["artists_from"],
          f"…and naming which one ({borrowed['artists_from']})")
    check(posebook.build_prompt(have_artists[0], 0)["artists_used"] == "",
          "nothing is borrowed when the switch is off")

    # The artist slider scales every token in the group.
    scaled = posebook._reweight("(artist:hiten:1.0), artist:wlop", 1.5)
    check("(artist:hiten:1.5)" in scaled and "(artist:wlop:1.5)" in scaled,
          f"the artist weight scales a whole group ({scaled})")
    check(posebook._reweight("artist:wlop", 1.0) == "artist:wlop",
          "…and weight 1.0 leaves the token bare")

    cast_on = posebook.build_prompt(pose, idx, cast=True)
    cast_off = posebook.build_prompt(pose, idx, cast=False)
    if pose.variants[idx].characters:
        check(pose.variants[idx].characters in cast_on["prompt"],
              "the demo cast can be brought back deliberately")
        check(pose.variants[idx].characters not in cast_off["prompt"],
              "…but is absent by default")

    # -- re-parsing is stable -------------------------------------------------
    raw = (ROOT / "app" / "poses").glob("*.json")
    path = next(iter(sorted(raw)))
    again = posebook._from_json(json.loads(path.read_text(encoding="utf-8")))
    check(len(again.poses) == len(book.poses), "the JSON round-trips")
    check([p.id for p in again.poses] == [p.id for p in book.poses],
          "…with stable ids, so a rebuild does not shuffle them")

    # -- a fresh parse of a tiny document ------------------------------------
    doc = "\n".join([
        "## 一、单男单女",
        "### （一）口",
        "#### 1. 測試動作",
        "作者：某人",
        "主要 Tag：1girl,{{{kiss}}},[artist:someone],着衣版:1girl,{{hug}}",
        "负面 Tag：{{bad}},n4 无需负面",
        "备注：隨便寫的",
    ])
    small = posebook.parse_codex(doc, codex_id="t")
    check(len(small.poses) == 1, "a minimal document parses")
    p0 = small.poses[0]
    check(p0.title == "測試動作" and p0.author == "某人", "title and author are read")
    check(len(p0.variants) == 2,
          f"an inline 着衣版 label makes a second variant ({len(p0.variants)})")
    check(p0.variants[1].label == "着衣版", "…labelled with what the document called it")
    check("artist:someone" in p0.variants[0].artists, "the artist is separated")
    check("bad" in p0.negative and "无需" not in p0.negative,
          f"prose is stripped from the negative ({p0.negative})")
    check("无需" in p0.note, "…and kept in the note instead")


def test_inspect_parts() -> None:
    """The guesser can hand back the staging without the character."""
    section("inspect: drop the character")
    import tags as tagmod

    guess = tagmod.Guess(
        general=[("sitting", 0.9), ("blue_hair", 0.8), ("school_uniform", 0.7),
                 ("classroom", 0.6), ("from_above", 0.5), ("comic", 0.4)],
        characters=[("hoshimachi_suisei", 0.95)],
        rating="general",
    )
    parts = guess.parts()
    check(parts["character"] == ["hoshimachi suisei"], f"the name is its own bucket ({parts})")
    check("blue hair" in parts["look"],
          "hair goes with the character, not the shot - dropping the name alone is not enough")
    check("school uniform" in parts["outfit"], "clothing is its own bucket")
    check("sitting" in parts["scene"] and "classroom" in parts["scene"]
          and "from above" in parts["scene"],
          f"pose, place and framing are the shot ({parts['scene']})")
    check("comic" in parts["drop"], "medium tags are dropped, never offered")
    everything = sum((parts[k] for k in ("character", "look", "outfit", "scene", "drop")), [])
    check(len(everything) == len(guess.general) + len(guess.characters),
          "every guessed tag lands in exactly one bucket")
    check("parts" in guess.public(), "…and the split is on the wire for the UI")

    doc = ROOT / "docs" / "pose-library.md"
    check(doc.is_file(), "the pose library is documented")
    text = doc.read_text(encoding="utf-8")
    check("完全無效" in text,
          "…leading with the fact that the source's weights do nothing in ComfyUI")
    check("aritst" in text, "…and the typo that silently disables the artist")
    check("預設關閉" in text, "…and that the artist/cast groups are off by default")
    check("docs/pose-library.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")

    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check('id="inspnochar"' in page, "the UI has a one-click 'only the pose and background'")
    check("INSP_ORDER" in page and "'drop'" not in page.split("INSP_ORDER")[1][:120],
          "…and never offers the medium bucket as a choice")
    check('class="insppart"' in page, "each bucket is separately switchable")


def test_quicktags() -> None:
    """The quick-pick tag list, and the claim that every tag in it is real.

    The value of this list is entirely in the verification, so that is what gets
    tested: a tag with no danbooru posts is one the model was never taught, and
    shipping it would send the user off adjusting weights on a word that does
    nothing. The counts are recorded, so this can assert on them.
    """
    section("quicktags")
    import quicktags as qt

    data = qt.public()
    check(data["count"] >= 300, f"{data['count']} tags in the quick-pick list")
    check(len(data["groups"]) == 9, f"grouped into 9 families ({len(data['groups'])})")
    check(all(g["title"] and g["tags"] for g in data["groups"]),
          "every group is named and non-empty")

    tags = [t for g in qt.GROUPS for t in g.tags]
    check(all(t.posts > 0 for t in tags), "every tag has a real danbooru post count")
    thin = [t.tag for t in tags if t.posts < 500]
    check(not thin, f"…and none is below 500 posts ({thin})")
    check(all(t.zh for t in tags), "every tag carries a Chinese label")
    seen = [t.tag for t in tags]
    dupes = {x for x in seen if seen.count(x) > 1}
    check(not dupes, f"no tag appears twice ({dupes})")

    # The four the list started from, and what happened to each.
    check(qt.BY_TAG["ahegao"].posts == 28089, "ahegao is real (28,089 posts)")
    check(qt.BY_TAG["breasts_out"].posts == 87377, "breasts out is real (87,377)")
    check("double_peace_gesture" not in qt.BY_TAG,
          "double peace gesture is not shipped - it is not a danbooru tag")
    check(qt.correction("double peace gesture") is not None
          and qt.correction("double peace gesture").tag == "double_v",
          "…typing it answers with double_v instead")
    check("ahegao_face" not in qt.BY_TAG,
          "ahegao face is not shipped - the name exists but has 0 posts")
    check(qt.correction("ahegao face").tag == "ahegao", "…and redirects to ahegao")
    check(qt.correction("half naked").tag == "topless_female",
          "half naked (0 posts) redirects to topless_female")

    # Prompt-guide vocabulary that does nothing on a danbooru-trained model.
    for dead in ("soft lighting", "cinematic lighting", "dramatic lighting",
                 "rim lighting", "volumetric lighting"):
        check(dead.replace(" ", "_") not in qt.BY_TAG,
              f"{dead} is not shipped (0 danbooru posts)")
        check(qt.correction(dead) is not None,
              f"…but {dead} still points at the sharper word")
    for real in ("backlighting", "sidelighting", "underlighting", "dim_lighting"):
        check(real in qt.BY_TAG, f"{real} is real, so it is offered")

    # Aliases resolve to the form that has the posts.
    check(qt.correction("naked").tag == "nude", "naked -> nude")
    check(qt.correction("see-through").tag == "see-through_clothes",
          "see-through -> see-through_clothes")
    check(qt.correction("cat pose").tag == "paw_pose", "cat pose -> paw_pose")
    check(qt.correction("erect nipples").tag == "covered_nipples",
          "erect nipples -> covered_nipples")
    check(qt.correction("breasts out") is None,
          "a tag that already works needs no correction")

    # Emitted text has to be what a checkpoint wants, not what danbooru stores.
    check(qt.BY_TAG["top-down_bottom-up"].prompt == "top-down bottom-up",
          "underscores become spaces")
    check(qt.BY_TAG["shower_(place)"].prompt == "shower \\(place\\)",
          f"parens are escaped ({qt.BY_TAG['shower_(place)'].prompt})")
    check("\\" not in qt.BY_TAG["ahegao"].prompt, "…and a plain tag is left alone")

    # The strength banding is what tells the user which tags need help.
    check(qt.BY_TAG["blush"].strength == "strong", "4M posts is 'strong'")
    check(qt.BY_TAG["ahegao"].strength == "ok", "28k posts is 'ok'")
    check(qt.BY_TAG["peace_symbol"].strength == "weak", "1.6k posts is 'weak'")

    found = qt.search("ahegao")
    check(found and found[0].tag == "ahegao", "search finds an English tag")
    check([t.tag for t in qt.search("阿嘿顏")] == ["ahegao"], "…and a Chinese label")
    check(len(qt.search("")) == 0, "an empty query returns nothing rather than everything")
    check([t.posts for t in qt.search("cum")]
          == sorted([t.posts for t in qt.search("cum")], reverse=True),
          "results are ordered by how well the model knows them")

    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check("W_STEP = 0.05" in page, "the weight step matches A1111's, so the habit transfers")
    check("W_MAX = 2.0" in page and "W_MIN = 0.1" in page,
          "…and the bounds match charpacks/naiweights")
    check("function bareTag" in page,
          "the tag-dedup compares bare tags, so a weighted copy is still a duplicate")
    check("SDXL_PIXELS" in page and "1.35" in page,
          "the custom-size readout warns past SDXL's trained pixel budget")
    check('data-ratio="9:16"' in page, "…and offers common ratios")
    check("SIZE_ASKED" in page,
          "…and admits when snapping to 64 changed the ratio you asked for")

    # A user reported that `peace` / `double peace gesture` / `ahegao face` work
    # for them, and they were right: CLIP reads English, so a paraphrase lands
    # near the tag rather than nowhere. Measured on CLIP ViT-L/14 (SDXL's own
    # text encoder 1) at 0.884 / 0.567 against a 0.28-0.34 unrelated baseline.
    # These pin the corrected framing so it cannot quietly regress.
    src = (ROOT / "app" / "quicktags.py").read_text(encoding="utf-8")
    for gone in ("does nothing", "打了等於沒打", "completely useless"):
        check(gone not in src, f"the module no longer claims a paraphrase {gone!r}")
    check("0.884" in src and "0.567" in src,
          "…and records the measurement that settled it")
    check("is not a pass/fail" in src,
          "…stating plainly what a post count does and does not mean")
    page_src = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check("打了等於沒打" not in page_src, "the UI copy was corrected too")
    check("圖片數少不等於沒用" in page_src, "…and says so where the user reads it")

    # -- favourites, pinned by the character picker -------------------------
    favs = qt.public()["favorites"]
    check(len(favs) == 13, f"13 favourites are pinned ({len(favs)})")
    keys = {f["key"] for f in favs}
    for want in ("v", "double_v", "breasts_out", "ahegao", "topless", "bottomless",
                 "horse_stance", "m_legs", "expressionless", "disgust", "serious",
                 "happy"):
        check(want in keys, f"…including {want}")
    check(all(f["danbooru"] and f["natural"] for f in favs),
          "every favourite carries both a danbooru and a natural spelling")
    check(all(f["danbooru"] != f["natural"] for f in favs),
          "…and the two really differ, or the switch would be theatre")
    check(qt.FAV_BY_KEY["double_v"].emit("danbooru") == "double v",
          "the anime models get the tag")
    check("peace sign" in qt.FAV_BY_KEY["double_v"].emit("natural"),
          "…and the photo models get a description")
    check(qt.FAV_BY_KEY["bottomless"].emit() == "bottomless",
          "bottomless_female has 0 posts, so the real tag is used")
    check(qt.FAV_BY_KEY["horse_stance"].emit() == "squatting, spread legs",
          "danbooru has no horse-stance tag; the pair that means it is used")
    check("30 張" in (ROOT / "docs" / "prompt-weights.md").read_text(encoding="utf-8"),
          "…and the doc says why")

    # tag_style is the single source of truth for which spelling to use.
    import images
    styles = {m.id: m.tag_style for m in images.IMAGE_MODELS}
    check(styles["noobai"] == styles["illustrious"] == styles["pony"] == "danbooru",
          f"the anime finetunes are marked danbooru ({styles})")
    check(styles["juggernaut"] == styles["sdxl-base"] == "natural",
          "…and the photo models natural, because they never saw a danbooru tag")
    check('"tag_style": model.tag_style' in (ROOT / "app" / "server.py").read_text(encoding="utf-8"),
          "…and it reaches the browser")
    check("function favIsOn" in page_src,
          "whether a favourite is on is derived from the prompt, not tracked beside it")
    check("FAV_ADDED" not in page_src,
          "…the drifting side-list is gone (it desynced whenever anything else "
          "wrote the prompt)")

    doc = ROOT / "docs" / "prompt-weights.md"
    check(doc.is_file(), "weights and the tag list are documented")
    text = doc.read_text(encoding="utf-8")
    check("Ctrl" in text and "1.05" in text, "…including the shortcut and the step")
    check("那句話是錯的" in text,
          "…and openly corrects the earlier overclaim rather than quietly editing it")
    check("0.884" in text and "0.567" in text,
          "…backing the correction with the measured CLIP similarities")
    check("docs/prompt-weights.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")



def test_artists() -> None:
    """The artist roster: real tags, per-model prefixes, and measured styles."""
    section("artists")
    import artists as art
    import images

    data = art.public()
    check(data["count"] >= 30, f"at least 30 artists, as asked ({data['count']})")
    check(len(data["groups"]) >= 5, f"grouped by style family ({data['groups']})")
    check(all(a.posts >= 100 for a in art.ARTISTS),
          "every artist has enough danbooru posts for the finetune to have seen them")
    check(all(a.zh and a.style and a.group for a in art.ARTISTS),
          "every artist has a name, a style note and a group")
    check(all(a.signals for a in art.ARTISTS),
          "…and the measured tags that back the note up")
    tags = [a.tag for a in art.ARTISTS]
    check(len(set(tags)) == len(tags), "no artist appears twice")

    # The codex the user imported must be represented, since that is what they
    # are actually generating with.
    from_codex = [a for a in art.ARTISTS if a.codex]
    check(len(from_codex) >= 15,
          f"the artists their own codex uses are included ({len(from_codex)})")
    for want in ("ciloranko", "wlop", "hiten_(hitenkei)", "ningen_mame",
                 "bee_(deadflow)", "modare", "wanke", "na_tarapisu153"):
        check(want in art.BY_TAG, f"…including {want}")

    # Two of the codex's most-used artists are written as tags that name nobody.
    check("hiten" not in art.BY_TAG and art.misnamed("hiten").tag == "hiten_(hitenkei)",
          "the codex's `artist:hiten` (37 entries) points at hiten_(hitenkei)")
    check(art.misnamed("deadflow").tag == "bee_(deadflow)",
          "…and its `aritst:deadflow` (32 entries) at bee_(deadflow)")
    check(art.misnamed("sho (sho lwlw)") is None,
          "…while sho_(sho_lwlw) has no redirect, because its target was excluded")
    check(art.misnamed("ciloranko") is None,
          "a name that is already right needs no redirect")

    # Emitted text has to suit the checkpoint, and one checkpoint ignores these
    # entirely - which is worth being loud about rather than letting it fail
    # silently.
    forms = {m.id: m.artist_form for m in images.IMAGE_MODELS}
    check(forms["noobai"] == "artist:{tag}",
          "NoobAI's own model card prompts artist:<name>")
    check(forms["illustrious"] == "by {tag}", "Illustrious uses `by <name>`")
    check(forms["pony"] == "",
          "Pony V6 stripped artist names from training, so it gets no form at all")
    check(forms["juggernaut"] == forms["sdxl-base"] == "",
          "…same for the photo models")
    wlop = art.BY_TAG["wlop"]
    check(wlop.emit(forms["noobai"]) == "artist:wlop", "the NoobAI spelling")
    check(wlop.emit(forms["illustrious"]) == "by wlop", "the Illustrious spelling")
    check(art.BY_TAG["bb_(baalbuddy)"].name == "bb \\(baalbuddy\\)",
          f"parens in an artist name are escaped ({art.BY_TAG['bb_(baalbuddy)'].name})")
    check(art.BY_TAG["yd_(orange_maru)"].emit("artist:{tag}")
          == "artist:yd \\(orange maru\\)",
          "…and survive the prefix")

    # Nothing whose signature output is minors.
    for gone in ("kedama_milk", "toraishi_666", "todoroki_masaru"):
        check(gone not in art.BY_TAG, f"{gone} is not in the roster")
    src = (ROOT / "app" / "artists.py").read_text(encoding="utf-8")
    check("loli" in src and "does not do" in src,
          "…and the file says why, rather than leaving a silent gap")

    check(art.search("厚塗"), "search works on the Chinese style note")
    check([a.tag for a in art.search("bkub")] == ["bkub"], "…and on the tag")
    check(art.search("halftone"), "…and on the measured signals")

    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check('id="artbox"' in page and 'id="artlist"' in page, "the panel exists")
    check("function artistIsOn" in page,
          "on/off is derived from the prompt, like the favourites")
    check('id="artswitch"' in page,
          "…and a model that ignores artists offers the switch to one that does not")
    check("artist_form" in page, "the prefix comes from the model, not the page")

    doc = ROOT / "docs" / "artists.md"
    check(doc.is_file(), "the roster is documented")
    text = doc.read_text(encoding="utf-8")
    flat = text.replace("_", " ")
    check("hiten (hitenkei)" in flat and "bee (deadflow)" in flat,
          "…including the two names the codex got wrong")
    check("Pony" in text, "…and that Pony ignores artist tags")
    check("docs/artists.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")



def test_likeness() -> None:
    """Why a generated Hololive member drifts from the stream model, and the fix.

    The user's report - "even with the original designer's artist tag it still
    does not look like them" - is not a bug, and the numbers say why. These pin
    the explanation to measured data so it cannot decay into folklore.
    """
    section("likeness (official design)")
    import charpacks

    pack = charpacks.get("hololive-collection")
    check(pack is not None, "the Hololive pack loads")
    who = pack.by_key["mori-calliope"]
    info = charpacks.likeness_advice(pack, who)
    check(info["posts"] > 10000,
          f"the character is well represented on danbooru ({info['posts']:,})")
    check(info["artist_posts"] and info["artist_posts"] < info["posts"] / 50,
          f"…but the designer has a tiny fraction of that ({info['artist_posts']} "
          f"vs {info['posts']}) - which is why naming them does not fix likeness")
    check(info["wiki"].startswith("https://virtualyoutuber.fandom.com"),
          "…and the official gallery is on hand as a reference image source")
    # The measured ratio for this exact character, not a range. The previous
    # version of this said "1-3% for all of them", which a review flagged and
    # measuring disproved: across the 75 the real spread is 0.62%-9.45%.
    check(f"{info['official_ratio']}%" in info["why"],
          f"the explanation quotes this character's measured ratio "
          f"({info['official_ratio']}%)")
    check("資料比例" in info["why"] and "不是量到的模型行為" in info["why"],
          "…and says outright that it is corpus prevalence, not model behaviour")
    ratios = [c.official_ratio for c in pack.characters if c.danbooru_posts]
    check(len(ratios) == 75, f"every character has a measured ratio ({len(ratios)})")
    check(min(ratios) < 1 and max(ratios) > 9,
          f"…and they really do span an order of magnitude "
          f"({min(ratios)}% - {max(ratios)}%)")
    check(sum(1 for r in ratios if r > 5) > 20,
          f"…with far more than a handful above 5% ({sum(1 for r in ratios if r > 5)}), "
          f"which is why the old flat '1-3%' could not be right")
    low = charpacks.likeness_advice(pack, next(
        c for c in pack.characters if c.key == "gawr-gura"))
    high = charpacks.likeness_advice(pack, next(
        c for c in pack.characters if c.key == "tokino-sora"))
    check("同人平均值" in low["why"], "at 1.06% the fan-consensus argument is stated")
    check("講不通" in high["why"],
          "…and at 9.45% it is explicitly withdrawn rather than repeated")
    check(who.designer in info["artist_why"], "…and names the designer with their count")

    plain = charpacks.build_prompt(pack, "mori-calliope", 0, model="noobai")
    strong = charpacks.build_prompt(pack, "mori-calliope", 0, model="noobai",
                                    likeness=1.25,
                                    likeness_tags=charpacks.LIKENESS_TAGS)
    check("official art" not in plain["prompt"], "the mode is off by default")
    check("official art" in strong["prompt"],
          "…and adds the official-art bias when the caller asks for it by name")
    # `likeness_tags` no longer defaults to LIKENESS_TAGS. It used to, which
    # meant calling this function directly - as any script or future endpoint
    # would - posted a danbooru general tag to whatever checkpoint was named,
    # including the photo models that have never seen one. This function does
    # not know the checkpoint; the caller does.
    bare = charpacks.build_prompt(pack, "mori-calliope", 0, model="juggernaut",
                                  likeness=1.25)
    check("official art" not in bare["prompt"],
          "…and adds nothing on its own, even with likeness on")
    check("newest" not in strong["prompt"],
          "…and NOT `newest`, which is a 2021-2024 date bucket for the artwork, "
          "not the character's current design")
    import images as _img
    photo = charpacks.build_prompt(pack, "mori-calliope", 0, model="juggernaut",
                                   likeness=1.25, likeness_tags="")
    check("official art" not in photo["prompt"],
          "a danbooru general tag is not handed to a checkpoint that never saw one")
    check(_img.get("pony").positive_prefix.count("score_") == 6,
          "Pony gets its full six-tag ladder, not the three-tag shorthand "
          f"({_img.get('pony').positive_prefix})")
    check(":1.25)" in strong["prompt"],
          f"…and weights the costume trigger ({strong['prompt'][:60]})")
    check(strong["prompt"].startswith("("),
          "…which stays first, where a tag has the most pull")
    # The costume tag is the lever, so it must be inside the weighted group.
    head = strong["prompt"].split("),")[0]
    check("1st costume" in head,
          f"the costume tag is what gets weighted ({head[:70]})")

    for w in (0, 1.05, 1.5):
        built = charpacks.build_prompt(pack, "mori-calliope", 0, model="noobai",
                                       likeness=w)
        check(built is not None and built["prompt"],
              f"likeness={w} still produces a prompt")

    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check('id="packlike"' in page, "the UI exposes it")
    check("function renderLikeness" in page, "…with the explanation attached")
    check("以圖生圖" in page and "ControlNet" in page,
          "…leading with the reference-image answer, which is the strong one")
    check("反方向" in page,
          "…and warning when the designer-style switch is fighting it")

    doc = ROOT / "docs" / "character-packs.md"
    text = doc.read_text(encoding="utf-8")
    check("同人" in text and "official art" in text,
          "…and the pack doc explains the drift")
    check("畫風" in text and "A/B" in text,
          "…and says the artist tag is style control, not proof it hurts likeness")

    # A second model reviewed this and found real defects; the response is
    # tracked so the corrections cannot quietly regress into the old claims.
    resp = ROOT / "docs" / "review-response.md"
    check(resp.is_file(), "the review has a written response")
    rtext = resp.read_text(encoding="utf-8")
    for label in ("FACT", "AUTHOR-REC", "MEASURED", "HEURISTIC", "HYPOTHESIS"):
        check(label in rtext, f"…adopting the evidence grade {label}")
    check("2021-2024" in rtext,
          "…and recording what `newest` actually is")
    check("OpenCLIP bigG" in rtext,
          "…and that the cosine measurement is not on SDXL's pooled path")
    check("沒有" in rtext.split("我保留意見的部分")[1][:40],
          "…and is honest that nothing in the review needed rebutting")
    page2 = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check("官方風格偏移（實驗性）" in page2,
          "the UI label no longer promises more than the evidence carries")
    check("貼近官方設定<" not in page2 and "> 貼近官方設定" not in page2,
          "…and the old overclaiming label is gone")



def test_refs() -> None:
    """Official reference art: filing a download, and refusing to guess.

    The matcher is the whole feature - if it files Marine's art under Noel, the
    user finds out three generations later - so the tests are mostly about what
    it declines to do.
    """
    section("reference art")
    import charpacks
    import refs as refslib

    pack = charpacks.get("hololive-collection")
    cands = refslib.candidates_from_pack(pack)
    check(len(cands) == 75, f"every character is a candidate ({len(cands)})")

    # Shapes a downloaded file actually comes in.
    for filename, want in [
        ("Mori Calliope - 1st Costume.png", "mori-calliope"),
        ("hoshimachi_suisei_03.jpg", "hoshimachi-suisei"),
        ("星街すいせい.png", "hoshimachi-suisei"),
        ("Gawr Gura 2nd outfit official art 1920x1080.png", "gawr-gura"),
        ("houshou_marine_(1st_costume).webp", "houshou-marine"),
        ("Nakiri Ayame (1st costume).png", "nakiri-ayame"),
        ("tokino_sora_wallpaper_1920x1080_v2.png", "tokino-sora"),
        ("sakura miko.webp", "sakura-miko"),
        ("兎田ぺこら.png", "usada-pekora"),
    ]:
        got, score = refslib.match(filename, cands)
        check(got == want, f"{filename!r} -> {want} (got {got or 'unfiled'}, {score:.2f})")

    # …and the ones where guessing would be worse than declining.
    for filename in ("IMG_2831.PNG", "random_landscape_photo.jpg", "noel.png",
                     "DSC00194.jpg", "wallpaper.png"):
        got, _ = refslib.match(filename, cands)
        check(not got, f"{filename!r} is left unfiled rather than guessed ({got})")

    # A real ambiguity in this pack: Pekomama's costume trigger contains
    # "usada pekora", because danbooru tags mother and daughter together. The
    # daughter wins on her own name; the mother only matched an outfit alias.
    got, _ = refslib.match("Usada Pekora official art.png", cands)
    check(got == "usada-pekora",
          f"a name matching a character AND someone's outfit picks the character ({got})")
    got, _ = refslib.match("Pekomama.png", cands)
    check(got == "pekomama", f"…and the other one still files correctly ({got})")

    # Store behaviour, on a scratch directory.
    import shutil
    root = TMP / "refs"
    shutil.rmtree(root, ignore_errors=True)
    lib_ = refslib.RefLibrary(root)
    lib_.load()
    png = (b"\x89PNG\r\n\x1a\n" + b"x" * 64)
    a = lib_.add(png, "Mori Calliope.png", "p", cands)
    check(a.character == "mori-calliope", "add() files by name")
    check(a.note == "new", "…and reports it as new")
    b = lib_.add(png, "a totally different name.png", "p", cands)
    check(b.name == a.name and b.note == "duplicate",
          "the same bytes are one file, reported as a duplicate not a second import")
    check(len(lib_.refs) == 1, f"…and only one record exists ({len(lib_.refs)})")
    c = lib_.add(png + b"different", "IMG_0001.png", "p", cands)
    check(c.character == "", "an unnameable file lands unfiled")
    check(len(lib_.unfiled("p")) == 1, "…and is listed as such")
    lib_.assign(c, "gawr-gura")
    check(lib_.path(c).is_file(), "assigning by hand moves the file on disk")
    check(lib_.counts("p") == {"mori-calliope": 1, "gawr-gura": 1},
          f"counts follow ({lib_.counts('p')})")
    lib_.save()
    again = refslib.RefLibrary(root)
    again.load()
    check(len(again.refs) == 2, "the index round-trips")
    check(lib_.delete("p", a.name) and not lib_.path(a).is_file(),
          "delete removes the file too")
    shutil.rmtree(root, ignore_errors=True)

    # Path safety: a pack or character id must never escape the refs folder.
    # The property is *containment* - separators are stripped, so "../../etc"
    # collapses to one harmless component rather than walking up.
    store = refslib.RefLibrary(root)
    for bad_pack, bad_char in (("../../etc", "../../../root"),
                               ("..", ".."), ("a/b", "c\\d"), ("", "")):
        where = store.folder(bad_pack, bad_char).resolve()
        check(root.resolve() in where.parents or where == root.resolve(),
              f"{bad_pack!r}/{bad_char!r} stays inside the refs folder ({where.name})")

    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check('id="refbox"' in page and 'id="reffiles"' in page, "the UI exists")
    check("refasinit" in page and "refasctrl" in page,
          "…offering both img2img and ControlNet, which is the point")
    check("不會亂猜" in page, "…and telling the user why something was left unfiled")
    check("multiple" in page.split('id="reffiles"')[1][:200],
          "…and accepting a whole download at once")

    doc = ROOT / "docs" / "reference-art.md"
    check(doc.is_file(), "the reference library is documented")
    dtext = doc.read_text(encoding="utf-8")
    check("不會亂猜" in dtext, "…including that it declines rather than guesses")
    check("Pekomama" in dtext, "…with the real ambiguity spelled out")
    check("路徑穿越" in dtext, "…and the traversal bug the tests caught")
    check("docs/reference-art.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")



def test_styles() -> None:
    """The style library, and the claim that every tag in it was checked.

    The recipes came from a written spec whose author had not seen the code and
    had not checked the tags. 47% of them turned out not to exist on danbooru,
    so the whole value of this module is the substitution pass - which means the
    substitution pass is what has to be tested. Two things must hold: nothing a
    recipe ships is an invented phrase, and every replacement is recorded.
    """
    section("style recipes")
    import styles

    check(len(styles.RECIPES) == 22, f"22 recipes ({len(styles.RECIPES)})")
    check(len({r.id for r in styles.RECIPES}) == 22, "every recipe id is unique")
    check(all(r.zh and r.en and r.desc for r in styles.RECIPES),
          "every recipe has a Chinese name, an English name and a description")
    check(all(r.chips for r in styles.RECIPES), "no recipe is empty")

    # Every tag a recipe names has to resolve in the shared vocabulary; a typo
    # here would ship a tag that is not the one that was verified.
    unknown = []
    for r in styles.RECIPES:
        for name in r.chips + r.negative:
            if name not in styles.ALL_CHIPS:
                unknown.append((r.id, name))
    check(not unknown, f"every recipe tag resolves ({unknown})")

    # The core claim. A `danbooru` chip must have a real post count; a `caption`
    # chip must name the model card it came from; nothing may be unlabelled.
    bad_kind = [c.tag for c in styles.ALL_CHIPS.values()
                if c.kind not in {"danbooru", "caption", "plain"}]
    check(not bad_kind, f"every chip declares its kind ({bad_kind})")
    zero = [c.tag for c in styles.ALL_CHIPS.values() if c.kind == "danbooru" and c.posts <= 0]
    check(not zero, f"every danbooru chip has a real post count ({zero})")
    unsourced = [c.tag for c in styles.ALL_CHIPS.values()
                 if c.kind == "caption" and not c.source]
    check(not unsourced, f"every caption token names its model card ({unsourced})")

    # The dangerous one. `2d` is an active danbooru alias of the artist `nidy`,
    # so the spec's "Matte 2D" recipe would have asked for one artist's style.
    shipped = {c for r in styles.RECIPES for c in r.chips + r.negative}
    check("2d" not in shipped and "2d" not in styles.ALL_CHIPS,
          "`2d` is not shipped - it aliases to the artist `nidy` (409 posts)")
    check("2d" in styles.REPLACED, "…and the reason is recorded in REPLACED")

    # The rest of the invented phrases. If one is ever added back it must go
    # through REPLACED, so the audit trail cannot rot.
    invented = ["clean lineart", "cel shading", "rim light", "dramatic lighting",
                "volumetric lighting", "detailed eyes", "detailed background",
                "cinematic composition", "glossy skin", "soft lighting",
                "matte colors", "reflections", "wet street", "catchlight"]
    leaked = [t for t in invented if t.replace(" ", "_") in styles.ALL_CHIPS]
    check(not leaked, f"none of the spec's invented phrases ships ({leaked})")
    missing = [t for t in invented if t not in styles.REPLACED]
    check(not missing, f"…and each one's replacement is written down ({missing})")
    check(len(styles.REPLACED) >= 70,
          f"{len(styles.REPLACED)} substitutions recorded in total")

    # `spot color` is a real tag (62,361 posts) that the spec used wrongly: it
    # means "monochrome except for one colour", so it does not belong in a
    # matte-2D recipe. It stays in the vocabulary, just not in that recipe.
    matte = styles.BY_ID["matte-2d-no-ai-gloss"]
    check("spot_color" not in matte.chips, "matte-2D does not ship `spot color`")
    check("spot_color" in styles.ALL_CHIPS, "…but the tag itself is still available")

    # Date buckets: five, from the model card, not the spec's six.
    check(set(styles.ERAS) == {"old", "early", "mid", "recent", "newest"},
          "five NoobAI date buckets, not six")
    check("newest" not in shipped,
          "`newest` is not used as a quality word in any recipe")

    # Prompts render, and the natural-language spelling is different.
    r = styles.BY_ID["clean-anime-keyvisual"]
    check("official art" in r.prompt(), "a recipe renders a comma-separated prompt")
    check(r.prompt("natural") != r.prompt(),
          "…and spells itself differently for a natural-language checkpoint")
    ink = styles.BY_ID["ink-manga"]
    check("\\(" in ink.prompt(), "parens in tag names are escaped for ComfyUI")

    # Model gating.
    for m in ("noobai", "illustrious", "pony", "juggernaut", "sdxl-base"):
        got = styles.recipes_for(m)
        check(bool(got), f"{m} has recipes ({len(got)})")
        check(all(m in r.models for r in got), f"…all gated to {m}")
    check(len(styles.recipes_for("juggernaut")) < len(styles.recipes_for("noobai")),
          "a photo checkpoint gets fewer anime recipes than NoobAI")

    # Search covers names, descriptions, keywords and the tags inside.
    check([r.id for r in styles.search("雨")] == ["neon-cyberpunk", "rainy-cinematic"],
          "search finds recipes by Chinese keyword")
    check("hair-detail" in [r.id for r in styles.search("backlighting")],
          "…and by a tag buried inside the recipe")
    check(len(styles.search("")) == 22, "an empty search returns everything")

    # Quality presets are quoted from model cards, and kept apart from recipes.
    check(len(styles.PRESETS) >= 5, f"{len(styles.PRESETS)} quality presets")
    check(all(p.source for p in styles.PRESETS), "every preset names its source")
    pony = styles.PRESET_BY_ID["pony-official"]
    check(pony.positive.count("score_") == 6, "Pony's preset has all six score tags")
    ill = styles.PRESET_BY_ID["illustrious-official"]
    check("amazing quality" not in ill.positive and "very aesthetic" not in ill.positive,
          "Illustrious's preset uses its own card's words, not WAI's")
    check(ill.positive == "masterpiece, best quality",
          "…which is `masterpiece, best quality`")
    check("comic" not in ill.negative and "monochrome" not in ill.negative,
          "…and the card's negative is trimmed so the manga recipe still works")


def test_promptmerge() -> None:
    """Merging a recipe into a prompt without eating anything.

    The two rules that matter are that the user's own tags survive and that
    nothing unrecognised is ever removed, so both are tested with the worst
    case: a prompt full of things the merger has never heard of.
    """
    section("prompt merge")
    import promptmerge as pm

    # Splitting has to respect brackets, or a weighted group becomes two tags.
    check(pm.split_tags("a, b, c") == ["a", "b", "c"], "splits on commas")
    check(pm.split_tags("(a, b:1.2), c") == ["(a, b:1.2)", "c"],
          "a comma inside a weight group is not a separator")
    check(pm.split_tags("shenhe \\(genshin impact\\), 1girl")
          == ["shenhe \\(genshin impact\\)", "1girl"],
          "escaped parens in a character name survive")
    check(pm.split_tags("a,,  , b") == ["a", "b"], "empty pieces are dropped")

    check(pm.key("(smile:1.3)") == "smile", "weights do not change a tag's identity")
    check(pm.key("flat_color") == "flat color", "nor do underscores")

    # Conflicts have sides: same side coexists, across sides does not.
    check(not pm.conflicts_with("monochrome", "greyscale"),
          "monochrome and greyscale are the same side (14.2x co-occurrence)")
    check(not pm.conflicts_with("realistic", "photorealistic"),
          "photorealistic is a subset of realistic, not a conflict")
    check(not pm.conflicts_with("anime coloring", "flat color"),
          "anime coloring and flat color measure 0.57x - not a conflict")
    check(not pm.conflicts_with("portrait", "upper body"),
          "framing tags are a warning, not a deletion")
    check(pm.conflicts_with("monochrome", "pastel colors") == "color-mode",
          "monochrome and pastel colors are (0.072x)")
    check(pm.conflicts_with("newest", "old") == "era", "two date buckets are")
    check(pm.conflicts_with("flat color", "3d") == "render", "flat color and 3d are")
    check(all(c.why and c.evidence for c in pm.CONFLICTS),
          "every conflict states its reason and its evidence")
    check(len(pm.CONFLICTS[0].sides) == 5, "five date buckets, not the spec's six")

    # A recipe that ships both sides of a conflict must not delete half of
    # itself: ink-manga carries monochrome *and* greyscale.
    m = pm.apply_recipe("1girl", "", "ink-manga", model_id="noobai")
    check("monochrome" in m.prompt and "greyscale" in m.prompt,
          "a recipe never retires its own tags")
    check(not m.replaced, "…and reports nothing replaced")

    # The user's tags win.
    m = pm.merge("1girl, (smile:1.3), my_lora_trigger, {red|blue} dress",
                 "", ["smile", "lineart"], model_id="noobai")
    check("(smile:1.3)" in m.prompt, "the user's weight survives")
    check(m.already == ["smile"], "…and the duplicate is reported, not added")
    check("my_lora_trigger" in m.prompt, "an unknown LoRA trigger is untouched")
    check("{red|blue} dress" in m.prompt, "so is a wildcard")

    # Conflicts replace, and say why.
    m = pm.merge("1girl, pastel colors", "", ["monochrome"], model_id="noobai")
    check("pastel colors" not in m.prompt, "an incoming tag retires what it conflicts with")
    check(m.replaced[0]["because"] == "monochrome" and m.replaced[0]["why"],
          "…and the diff says which tag did it and why")
    m = pm.merge("1girl, pastel colors", "", ["monochrome"],
                 model_id="noobai", replace_conflicts=False)
    check("pastel colors" in m.prompt, "keep-my-style leaves the conflict alone")

    # Model cleanup, by name only.
    m = pm.merge("score_9, score_8_up, 1girl, newest", "", [], model_id="noobai")
    check("score_9" not in m.prompt and "newest" in m.prompt,
          "Pony scores are stripped on NoobAI; NoobAI's own era tag is not")
    m = pm.merge("score_9, 1girl, newest, masterpiece", "", [], model_id="pony")
    check("score_9" in m.prompt and "newest" not in m.prompt,
          "on Pony it is the other way round")
    check(all(c["why"] for c in m.cleaned), "every cleanup says why")
    m = pm.merge("1girl, my_score_lora, scorecard", "", [], model_id="noobai")
    check("my_score_lora" in m.prompt and "scorecard" in m.prompt,
          "cleanup matches whole tags only - it cannot eat a lookalike trigger")

    # Negatives merge separately and do not duplicate.
    m = pm.merge("1girl", "3d, realistic", [], ["3d", "photorealistic"], model_id="noobai")
    check(m.negative == "3d, realistic, photorealistic", "negatives dedupe")
    check(m.negative_added == ["photorealistic"], "…and only the new one is reported")

    # Undo.
    check(pm.remove_tags("1girl, lineart, (smile:1.2)", ["lineart", "smile"]) == "1girl",
          "removing tags matches through weights")

    check(pm.apply_recipe("", "", "nope") is None, "an unknown recipe id returns None")
    check(pm.apply_preset("", "", "nope") is None, "so does an unknown preset id")


def test_promptdoctor() -> None:
    """The prompt health check.

    Every finding has to be checkable from data - a model card or a danbooru
    count - because the app has never generated an image and so cannot make a
    claim about how anything will look.
    """
    section("prompt doctor")
    import promptdoctor as pd

    # The single most useful thing it says.
    f = pd.check("1girl", model_id="noobai", width=512, height=512)
    ids = [x.id for x in f]
    check("resolution" in ids, "512x512 on an SDXL checkpoint is flagged")
    res = next(x for x in f if x.id == "resolution")
    check(res.level == "high", "…at the highest level")
    check(res.action == "resize" and res.size == (832, 1216), "…with a fix attached")
    check("25%" in res.detail, "…and states the actual fraction of the trained area")
    check(not [x for x in pd.check("1girl", model_id="noobai", width=832, height=1216)
               if x.id == "resolution"],
          "a native size is not flagged")
    big = pd.check("1girl", model_id="noobai", width=2048, height=1536)
    check("resolution-big" in [x.id for x in big], "and far above native is flagged too")

    # Dialect.
    f = pd.check("score_9, score_8_up, 1girl", model_id="noobai", width=832, height=1216)
    sc = next(x for x in f if x.id == "score-dialect")
    check(len(sc.tags) == 2 and sc.action == "remove", "Pony scores on NoobAI are removable")
    check(not [x for x in pd.check("score_9, 1girl", model_id="pony", width=1024, height=1024)
               if x.id == "score-dialect"], "…and are fine on Pony")
    f = pd.check("1girl", model_id="pony", width=1024, height=1024)
    miss = next(x for x in f if x.id == "score-missing")
    check(len(miss.tags) == 6, "Pony without its scores is told to add all six")

    # Folklore quality words.
    f = pd.check("1girl, 8k, ultra detailed, trending on artstation, masterpiece",
                 model_id="noobai", width=832, height=1216)
    fl = next(x for x in f if x.id == "folklore-quality")
    check(len(fl.tags) == 3, "three undocumented buzzwords found")
    check("masterpiece" not in fl.tags, "…and a real card word is not among them")

    # Words from another finetune's dialect.
    f = pd.check("1girl, amazing quality, very aesthetic", model_id="illustrious",
                 width=832, height=1216)
    fq = next(x for x in f if x.id == "foreign-quality")
    check(set(fq.tags) == {"amazing quality", "very aesthetic"},
          "WAI's quality words are named as not being on Illustrious's card")

    # Contradictions.
    f = pd.check("1girl, smile", "smile, worst quality", model_id="noobai",
                 width=832, height=1216)
    both = next(x for x in f if x.id == "both-sides")
    check(both.level == "high" and both.tags == ["smile"],
          "the same tag on both sides is a high-level finding")

    f = pd.check("1girl, monochrome, pastel colors", model_id="noobai",
                 width=832, height=1216)
    con = next(x for x in f if x.id.startswith("conflict-"))
    check("0.072" in con.detail, "a conflict quotes its measured co-occurrence")

    f = pd.check("1girl, smile, smile", model_id="noobai", width=832, height=1216)
    check("duplicate" in [x.id for x in f], "a repeated tag is noticed")
    dup = next(x for x in f if x.id == "duplicate")
    check("不等於加權" in dup.detail, "…and the reason repeating is not weighting is given")

    # Illustrious's own advice about framing tags.
    f = pd.check("1girl, portrait, upper body, close-up", model_id="noobai",
                 width=832, height=1216)
    fr = next(x for x in f if x.id == "framing")
    check(fr.level == "info", "three framing tags is a note, not an error")
    check("11 倍" in fr.detail, "…because the data says they do co-occur")

    # Artist spelling.
    f = pd.check("1girl, artist:wlop", model_id="pony", width=1024, height=1024)
    check("artist-ignored" in [x.id for x in f],
          "Pony is told artist tags do nothing there")
    f = pd.check("1girl, artist:wlop", model_id="illustrious", width=832, height=1216)
    check("artist-form" in [x.id for x in f],
          "Illustrious is told its card spells it `by name`")
    check(not [x for x in pd.check("1girl, artist:wlop", model_id="noobai",
                                   width=832, height=1216) if x.id == "artist-form"],
          "…and NoobAI, whose card uses `artist:`, is not")

    # Subject count.
    check("no-subject" in [x.id for x in pd.check("blue hair, smile", model_id="noobai",
                                                  width=832, height=1216)],
          "a prompt with no 1girl/1boy/no humans is noted")
    check("empty" in [x.id for x in pd.check("", model_id="noobai")],
          "an empty prompt is caught")

    # A clean prompt gets a clean bill.
    good = pd.check("1girl, hoshimachi suisei, official art, anime coloring, "
                    "masterpiece, best quality",
                    "worst quality, lowres", model_id="noobai", width=832, height=1216)
    s = pd.summary(good)
    check(s["level"] == "ok" and not good, f"a clean prompt reports 良好 ({[x.id for x in good]})")
    check(pd.summary(pd.check("1girl", model_id="noobai", width=512, height=512))["level"]
          == "high", "and a broken one does not")

    # Findings come back worst first.
    f = pd.check("score_9, 1girl, smile, smile", "smile", model_id="noobai",
                 width=512, height=512)
    levels = [x.level for x in f]
    check(levels == sorted(levels, key=lambda l: {"high": 0, "warn": 1, "info": 2}[l]),
          "findings are ordered worst first")


def test_ref_chinese_names() -> None:
    """Chinese filenames find their member, and near-misses still do not.

    The user's own collection is organised in Chinese - the folder is literally
    `01_官方角色全身立繪_最重要` - and before this the matcher scored every one of
    those names zero. The table is data lifted from zh.wikipedia in both scripts,
    so the test checks the provenance holds as much as the matching does.
    """
    section("reference art: Chinese names")
    import charpacks
    import refnames
    import refs as refslib

    pack = charpacks.get("hololive-collection")
    cands = refslib.candidates_from_pack(pack)

    check(len(refnames.ZH_NAMES) == 73, f"73 members have Chinese names ({len(refnames.ZH_NAMES)})")
    absent = [c.key for c in pack.characters if c.key not in refnames.ZH_NAMES]
    check(sorted(absent) == sorted(refnames.NO_ZH_NAME),
          f"the two without one are declared, not forgotten ({absent})")
    check(all(refnames.NO_ZH_NAME.values()), "…each with a stated reason")
    keys = {c.key for c in pack.characters}
    stray = [k for k in refnames.ZH_NAMES if k not in keys]
    check(not stray, f"no name belongs to a character the pack does not have ({stray})")

    # Both scripts came from the source, so both have to work.
    for filename, want in [
        ("星街彗星.png", "hoshimachi-suisei"),
        ("兔田佩克拉_立繪.png", "usada-pekora"),
        ("寶鐘瑪琳.png", "houshou-marine"),
        ("宝钟玛琳 (3).jpg", "houshou-marine"),
        ("時乃空.png", "tokino-sora"),
        ("时乃空.png", "tokino-sora"),
        ("櫻巫女_立繪.png", "sakura-miko"),
        ("樱巫女.png", "sakura-miko"),
        ("森美聲.png", "mori-calliope"),
        ("噶嗚·古拉 official.png", "gawr-gura"),
    ]:
        got, score = refslib.match(filename, cands)
        check(got == want, f"{filename} -> {got or '(none)'} ({score:.2f})")

    # Watson Amelia's two sources disagree on the *translation*, not the script.
    for filename in ("華生·艾米莉亞.png", "沃森·阿米莉亚.png"):
        got, _ = refslib.match(filename, cands)
        check(got == "watson-amelia", f"{filename} -> {got or '(none)'}")

    # The reason CJK is matched as a run rather than a bag of characters: a
    # two-character name tokenised into its characters matches almost anything.
    check(refslib._is_cjk_name("星街彗星") and not refslib._is_cjk_name("Gawr Gura"),
          "a Han name is detected as one; a latin name is not")
    check(refslib._score_cjk("律可", "可律的圖") == 0.5,
          "reversed characters do not count as the name")
    check(refslib._score_cjk("星街彗星", "01_星街彗星_full.png") == 1.0,
          "…but the name inside a longer filename does")
    for filename in ("可律的圖.png", "霧夜的可怕故事.png", "某某某.png", "背景圖.png"):
        got, _ = refslib.match(filename, cands)
        check(got == "", f"{filename} matches nobody, correctly")


def test_ref_folder_import(tmp: Path) -> None:
    """Scanning and importing a local folder, without moving the user's files.

    The archive being imported here is 5GB of somebody's own filing system on
    their own machine. Three things must hold: the scan says what it will do
    before anything happens, the import does not move or copy by default, and
    re-running it does not duplicate.
    """
    section("reference art: folder import")
    import charpacks
    import refs as refslib
    from PIL import Image

    pack = charpacks.get("hololive-collection")
    cands = refslib.candidates_from_pack(pack)

    root = tmp / "archive" / "01_官方角色全身立繪_最重要"
    # Every picture is a different colour on purpose. Copy mode identifies a
    # file by the hash of its bytes, so seven identical test images would all
    # collapse into one and the test would be measuring nothing.
    shade = 0
    for folder, files in [
        ("星街彗星", ["01.png", "02.png"]),
        ("兔田佩克拉", ["a.png"]),
        ("宝钟玛琳", ["marine.png"]),
        ("其他", ["unknown_thing.png", "背景.png"]),
    ]:
        (root / folder).mkdir(parents=True, exist_ok=True)
        for name in files:
            shade += 17
            Image.new("RGB", (64, 96), (shade, 30, 60)).save(root / folder / name)
    Image.new("RGB", (64, 96), (7, 20, 30)).save(root / "Mori Calliope 1st.png")
    (root / "notes.txt").write_text("not an image", encoding="utf-8")

    rows, problems = refslib.scan(root, cands)
    summary = refslib.scan_summary(rows)
    check(not problems, f"a clean folder scans without complaint ({problems})")
    check(summary["total"] == 7, f"only the images are counted ({summary['total']})")
    check(summary["matched"] == 5, f"5 match ({summary['matched']})")
    check(summary["unmatched"] == 2, f"2 do not ({summary['unmatched']})")
    check(summary["characters"] == 4, f"across 4 members ({summary['characters']})")
    check(summary["by_folder"] == 4,
          f"4 were decided by the folder name, not the filename ({summary['by_folder']})")
    check(summary["counts"].get("hoshimachi-suisei") == 2,
          "…and the per-member counts are right")
    check(any("unknown_thing" in r["rel"] for r in summary["unmatched_sample"]),
          "the unmatched sample names actual files, so it can be acted on")

    # Nothing is written by a scan.
    before = sorted(p.name for p in root.rglob("*"))

    store = refslib.RefLibrary(tmp / "reflib")
    result = store.import_folder(root, "hololive-collection", cands, only_matched=True)
    check(result["filed"] == 5, f"the import files 5 ({result['filed']})")
    check(result["unfiled"] == 0, "…and skipped the unmatched, as asked")
    check(sorted(p.name for p in root.rglob("*")) == before,
          "the source folder is untouched - nothing moved, nothing renamed")
    check(not any((tmp / "reflib").rglob("*.png")),
          "and nothing was copied: the archive is indexed where it lies")
    check(all(r.linked and Path(r.source).is_file() for r in store.refs),
          "every reference points at a real file in the archive")

    again = store.import_folder(root, "hololive-collection", cands, only_matched=True)
    check(again["filed"] == 0 and again["dupes"] == 5,
          f"re-running finds them all already there ({again})")
    check(len(store.refs) == 5, f"…and does not duplicate ({len(store.refs)})")

    # A linked reference survives a round trip through the index file.
    store.save()
    reopened = refslib.RefLibrary(tmp / "reflib")
    reopened.load()
    check(len(reopened.refs) == 5, f"the index reloads ({len(reopened.refs)})")
    check(reopened.counts("hololive-collection").get("hoshimachi-suisei") == 2,
          "…with the filing intact")

    # Deleting a linked reference forgets it; it must not delete the user's file.
    victim = reopened.refs[0]
    source = Path(victim.source)
    check(reopened.delete("hololive-collection", victim.name), "a linked ref can be removed")
    check(source.is_file(), "…and the file in the archive is still there")

    # If the archive moves, the references disappear rather than 404 forever.
    reopened.save()
    moved = tmp / "archive-moved"
    (root.parent).rename(moved)
    after = refslib.RefLibrary(tmp / "reflib")
    after.load()
    check(not after.refs, "moving the archive drops the stale references")
    moved.rename(root.parent)

    # copy=True is the other mode, for a USB stick you are about to unplug.
    copied = refslib.RefLibrary(tmp / "reflib-copy")
    result = copied.import_folder(root, "hololive-collection", cands,
                                  copy=True, only_matched=True)
    check(result["filed"] == 5, "copy mode files the same 5")
    check(len(list((tmp / "reflib-copy").rglob("*.png"))) == 5,
          "…and this time the bytes really are copied")
    check(all(not r.linked for r in copied.refs), "…and they are not linked")

    # A path that is not there is an error, not a silent empty result.
    rows, problems = refslib.scan(tmp / "nope", cands)
    check(not rows and problems, "a missing folder reports a problem")

def test_experiments() -> None:
    """Fixed-seed sweeps: the matrix, the cap, the pairing, and the counting.

    All of this is arithmetic and bookkeeping, which is exactly why it is worth
    testing hard - the value of a sweep is that its comparisons are controlled,
    and every bug here is a silently uncontrolled comparison.
    """
    section("experiments")
    import random

    import experiments as ex

    # -- the matrix ----------------------------------------------------------
    seeds = ex.make_seeds(4, random.Random(7))
    check(len(seeds) == 4 and len(set(seeds)) == 4, f"distinct seeds ({seeds})")
    check(len(ex.make_seeds(999)) == ex.MAX_SEEDS, "seed count is capped")
    check(len(ex.make_seeds(0)) == 1, "…and never zero")

    variants, warning = ex.expand(
        {"lora_strength": [0.6, 0.8, 1.0], "denoise": [0.35, 0.45]}, seeds)
    check(len(variants) == 6, f"3x2 axes make 6 variants ({len(variants)})")
    check(not warning, "…with no warning at this size")
    check(len({v.id for v in variants}) == 6, "variant ids are unique")
    combos = {tuple(sorted(v.values.items())) for v in variants}
    check(len(combos) == 6, "every cell of the product is distinct")
    check(all("LoRA 強度" in v.label for v in variants),
          f"…and labelled readably ({variants[0].label})")

    empty, _ = ex.expand({}, seeds)
    check(len(empty) == 1 and empty[0].values == {},
          "no axes means one baseline variant, not zero")
    junk, _ = ex.expand({"nonsense": [1, 2], "lora_strength": []}, seeds)
    check(len(junk) == 1, "unknown or empty axes are ignored")
    dupes, _ = ex.expand({"cfg": [5, 5, 5, 6]}, seeds)
    check(len(dupes) == 2, f"repeated values collapse ({len(dupes)})")

    big, warn2 = ex.expand({"lora_strength": [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1],
                            "cfg": [4, 5, 6, 7, 8], "steps": [20, 25, 30, 35]}, seeds)
    check(len(big) * len(seeds) <= ex.MAX_JOBS,
          f"an oversized sweep is capped ({len(big) * len(seeds)} <= {ex.MAX_JOBS})")
    check("超過上限" in warn2, "…and says so rather than quietly truncating")

    # -- one concrete request ------------------------------------------------
    base = {"prompt": "1girl", "model": "noobai", "cfg": 5.5}
    got = ex.settings_for(base, variants[0], 1234)
    check(got["prompt"] == "1girl" and got["model"] == "noobai",
          "the fixed base carries through")
    check(got["seed"] == 1234, "…with the seed the sweep chose")
    check(got["lora_strength"] == variants[0].values["lora_strength"],
          "…and the axis value overriding the base")
    override = ex.settings_for({"cfg": 5.5}, ex.Variant("v", {"cfg": 9.0}), 1)
    check(override["cfg"] == 9.0, "an axis beats the base for the same key")

    # -- the store -----------------------------------------------------------
    path = TMP / "experiments.jsonl"
    path.unlink(missing_ok=True)
    store = ex.ExperimentStore(path)
    store.load()
    exp, _ = store.create("sweep", base, {"cfg": [5, 6]}, seeds[:2])
    check(len(exp.variants) == 2, "created with its variants")
    check(exp.job_count == 0, "…and no jobs until it is run")
    exp.variants[0].jobs = ["j1", "j2"]
    exp.variants[1].jobs = ["j3", "j4"]
    store.save()
    again = ex.ExperimentStore(path)
    again.load()
    back = again.get(exp.id)
    check(back is not None and back.job_count == 4, "the store round-trips jobs")
    check(back.seeds == exp.seeds, "…and the seeds, which is the control")
    check(again.delete(exp.id) and again.get(exp.id) is None, "delete works")
    path.unlink(missing_ok=True)

    # -- pairing: the same seed on both sides, or it measures the dice --------
    exp2 = ex.Experiment(id="e", seeds=[11, 22], variants=[
        ex.Variant("v0", {"cfg": 5}, ["a1", "a2"]),
        ex.Variant("v1", {"cfg": 6}, ["b1", "b2"]),
    ])
    seen_pairs = set()
    for _ in range(40):
        pair = ex.next_pair(exp2, "likeness", random.Random())
        if pair is None:
            break
        jobs = {pair["a"]["job"], pair["b"]["job"]}
        # a1/b1 belong to seed 11, a2/b2 to seed 22 - never mixed.
        check_ok = jobs in ({"a1", "b1"}, {"a2", "b2"})
        if not check_ok:
            check(False, f"a pair mixed seeds: {jobs}")
            break
        check_ok = pair["a"]["variant"] != pair["b"]["variant"]
        if not check_ok:
            check(False, "a pair compared a variant with itself")
            break
        seen_pairs.add(tuple(sorted(jobs)))
    else:
        check(True, "every pair is same-seed and cross-variant")
    check(len(seen_pairs) == 2, f"both seeds get offered ({seen_pairs})")

    sides = set()
    for _ in range(60):
        pair = ex.next_pair(exp2, "costume", random.Random())
        if pair:
            sides.add(pair["a"]["variant"])
    check(len(sides) == 2, "which variant is shown first is randomised (position bias)")

    # A voted-on comparison is not offered again - but only on the seed it was
    # judged on. This is the regression an outside review caught: the dedup key
    # had no seed in it, so one vote on A-vs-B retired that pair across every
    # seed, and a four-seed experiment collected one vote per pair and declared
    # itself finished. Running fixed seeds and then throwing away all but one of
    # them is worse than not running them, because the result still looks
    # controlled.
    exp2.votes.append(ex.Vote(criterion="likeness", winner="v0", loser="v1", seed=11))
    remaining = ex.next_pair(exp2, "likeness", random.Random(0))
    check(remaining is not None and remaining["seed"] == 22,
          f"the same A/B is still judged on the second seed ({remaining and remaining['seed']})")
    exp2.votes.append(ex.Vote(criterion="likeness", winner="v1", loser="v0", seed=22))
    check(ex.next_pair(exp2, "likeness", random.Random()) is None,
          "…and only then is that criterion finished")
    check(ex.next_pair(exp2, "costume", random.Random()) is not None,
          "…but a different criterion still has work to do")

    # A failed generation must not slide later seeds one place to the left. The
    # position of a job in the list is the only thing that says which seed it
    # came from, so a dropped cell relabels every job after it - a wrong result
    # rather than a missing one.
    partial = ex.Experiment(id="p", seeds=[11, 22, 33], variants=[
        ex.Variant("v0", {}, ["a11", "", "a33"]),
        ex.Variant("v1", {}, ["b11", "b22", "b33"]),
    ])
    offered = set()
    for _ in range(60):
        pair = ex.next_pair(partial, "likeness", random.Random())
        if pair is None:
            break
        offered.add((pair["seed"], tuple(sorted((pair["a"]["job"], pair["b"]["job"])))))
    check(offered == {(11, ("a11", "b11")), (33, ("a33", "b33"))},
          f"a failed middle cell is skipped, not shifted ({sorted(offered)})")
    check(not any(j == "b22" for _, jobs in offered for j in jobs),
          "…so seed 22's surviving picture is never paired against seed 33's")
    check(partial.job_count == 5, f"job_count counts real jobs, not slots ({partial.job_count})")
    check(partial.has_run, "…and has_run is true even with a hole in it")
    check(not ex.Experiment(id="q", seeds=[11], variants=[ex.Variant("v0", {}, [])]).has_run,
          "an experiment that was never run says so")
    allfail = ex.Experiment(id="r", seeds=[11], variants=[ex.Variant("v0", {}, [""])])
    check(allfail.has_run and allfail.job_count == 0,
          "a run where everything failed still counts as run - or it gets queued twice")

    # -- counting ------------------------------------------------------------
    table = exp2.standings()["likeness"]
    check(table["v0"]["win"] == 1 and table["v0"]["loss"] == 1,
          f"wins and losses are counted per variant ({table['v0']})")
    check(table["v0"]["rate"] == 0.5, f"…and a win rate derived ({table['v0']['rate']})")
    # A tie is a statement about two variants, so it has to be credited to both.
    # Storing one side made ties asymmetric, which is the one thing a tie cannot
    # be, and left the pairing logic unable to tell what had been compared.
    exp2.votes.append(ex.Vote(criterion="beauty", winner="", loser="v0",
                              other="v1", seed=11))
    beauty = exp2.standings()["beauty"]
    check(beauty["v0"]["tie"] == 1 and beauty["v1"]["tie"] == 1,
          f"a tie counts for both sides ({beauty['v0']['tie']}, {beauty['v1']['tie']})")
    check(beauty["v0"]["win"] == 0, "…and for neither as a win")
    tie_vote = exp2.votes[-1]
    check(tie_vote.pair == ("v0", "v1"), f"a tie knows which pair it was ({tie_vote.pair})")
    check(ex.next_pair(exp2, "beauty", random.Random(0))["seed"] == 22,
          "…so the tied pair is not offered again on the same seed")

    # Votes written before `other` existed still load, and are not guessed at.
    legacy = ex.Vote(criterion="adherence", winner="", loser="v0")
    check(legacy.pair == ("v0", "v0") and legacy.sides == ("v0",),
          "a legacy tie reports one known side rather than inventing the other")
    exp2.votes.append(legacy)
    legacy_table = exp2.standings()["adherence"]
    check(legacy_table["v0"]["tie"] == 1 and legacy_table["v1"]["tie"] == 0,
          "…and is credited only where it actually has data")
    check(set(exp2.standings()) == set(ex.CRITERIA),
          "every criterion gets its own table - beauty and likeness are "
          "different questions and must not be averaged together")

    # -- provenance ----------------------------------------------------------
    sample = TMP / "prov.bin"
    sample.write_bytes(b"weights")
    first = ex.file_hash(sample)
    check(len(first) == 64, f"a file hashes to sha256 ({first[:12]}…)")
    check(ex.file_hash(sample) == first, "…and the cache returns the same value")
    time.sleep(0.01)
    sample.write_bytes(b"different weights")
    check(ex.file_hash(sample) != first,
          "…but rewriting the file changes it - the cache key includes size and "
          "mtime, because reusing a filename for new weights is the exact "
          "failure provenance exists to catch")
    # The case a one-second cache key silently gets wrong: same filename, same
    # size, rewritten inside the same second. os.utime pins both stat times to
    # the same integer second with different nanoseconds, which is exactly the
    # shape a fast overwrite produces - and with `int(st_mtime)` in the key the
    # cache handed back the previous file's digest, making the provenance record
    # a lie about which weights produced the picture.
    same = TMP / "same-second.bin"
    same.write_bytes(b"A" * 32)
    at = same.stat().st_mtime
    os.utime(same, ns=(int(at) * 10**9 + 100, int(at) * 10**9 + 100))
    before = ex.file_hash(same)
    same.write_bytes(b"B" * 32)
    os.utime(same, ns=(int(at) * 10**9 + 900, int(at) * 10**9 + 900))
    after_stat = same.stat()
    check(int(after_stat.st_mtime) == int(at) and same.stat().st_size == 32,
          "the rewrite really does share the same whole second and size")
    check(ex.file_hash(same) != before,
          "…and the hash still changes, because the cache key is nanoseconds")
    same.unlink(missing_ok=True)

    check(ex.file_hash(TMP / "does-not-exist") == "",
          "a missing file hashes to empty rather than raising")
    prov = ex.provenance(checkpoints={"m.safetensors": sample}, loras={},
                         comfy_commit="abc1234")
    check(prov["checkpoints"]["m.safetensors"] and prov["comfy_commit"] == "abc1234",
          "provenance records content hashes and the commit")
    sample.unlink(missing_ok=True)

    import updates
    check(updates.head_commit(ROOT.parent) or True,
          "head_commit runs without touching the network")

    page = (ROOT / "app" / "static" / "index.html").read_text(encoding="utf-8")
    check('id="expcard"' in page and "function wireExperiments" in page,
          "the UI exists")
    check("同一批 seed" in page,
          "…and states the control where the user reads it")
    doc = ROOT / "docs" / "experiments.md"
    check(doc.is_file(), "experiments are documented")
    dtext = doc.read_text(encoding="utf-8")
    check("骰子" in dtext, "…explaining why the seeds are shared")
    check("內容雜湊" in dtext, "…and why provenance is by hash, not filename")
    check("不該在" in dtext,
          "…and that beauty and likeness are never averaged together")
    check("HEURISTIC" in dtext,
          "…and what this unblocks: turning the heuristics into measurements")
    check("docs/experiments.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")



async def test_experiment_run() -> None:
    """A whole sweep through the real endpoints against a fake ComfyUI.

    The unit tests cover the matrix arithmetic; this covers the thing that
    actually matters at runtime - that every variant really did run the same
    seeds, and that each job really carried its own axis values. A sweep whose
    comparisons are not controlled is worse than no sweep, because it produces
    a confident number from noise.
    """
    section("experiment run (end to end)")
    import config
    import images
    import server
    from fastapi import HTTPException

    fake = FakeComfy()
    runner, url = await start(fake.app())
    old_url = config.COMFY_URL
    config.COMFY_URL = url
    ck = config.MODELS_DIR / "checkpoints"
    ck.mkdir(parents=True, exist_ok=True)
    stub = ck / "sweeptest-experiment.safetensors"
    stub.write_bytes(b"fake weights")
    saved = dict(server.EXPERIMENTS.items)
    server.EXPERIMENTS.items = {}
    try:
        base = {"prompt": "1girl, hoshimachi suisei",
                "model": images.CUSTOM_PREFIX + stub.name, "batch": 1}
        created = json.loads(bytes((await server.create_experiment({
            "name": "sweep", "base": base,
            "axes": {"cfg": [5, 6], "steps": [20, 25]}, "seed_count": 2})).body))
        check(len(created["variants"]) == 4,
              f"2x2 axes make 4 variants ({len(created['variants'])})")
        check(len(created["seeds"]) == 2, "…on 2 seeds")
        digest = list(created["provenance"].get("checkpoints", {}).values())
        check(digest and len(digest[0]) == 64,
              "the checkpoint is recorded by content hash, not filename")
        check(created["provenance"].get("app_commit") is not None,
              "…alongside the app commit")

        run = json.loads(bytes((await server.run_experiment(created["id"])).body))
        check(run["queued"] == 8, f"8 jobs queued ({run['queued']}) {run['failed'][:1]}")
        check(not run["failed"], f"…with nothing rejected ({run['failed'][:1]})")

        got = json.loads(bytes((await server.get_experiment(created["id"])).body))
        per_variant = [[got["jobs"][j]["seed"] for j in v["jobs"]]
                       for v in got["variants"]]
        check(all(row == per_variant[0] for row in per_variant),
              f"every variant ran the SAME seeds - the whole control ({per_variant})")
        mismatched = [v["label"] for v in got["variants"]
                      if got["jobs"][v["jobs"][0]]["settings"]["cfg"] != v["values"]["cfg"]
                      or got["jobs"][v["jobs"][0]]["settings"]["steps"] != v["values"]["steps"]]
        check(not mismatched, f"…and each job carried its own axis values ({mismatched})")

        # Blind pairing over finished jobs.
        experiment = server.EXPERIMENTS.get(created["id"])
        for variant in experiment.variants:
            for job_id in variant.jobs:
                record = server.lib.records[job_id]
                record.status = "done"
                record.output = f"{job_id}.png"
        pair = json.loads(bytes(
            (await server.experiment_pair(created["id"], "likeness")).body))
        check(not pair["done"], "there is a pair to judge")
        a_seed = server.lib.records[pair["pair"]["a"]["job"]].seed
        b_seed = server.lib.records[pair["pair"]["b"]["job"]].seed
        check(a_seed == b_seed,
              f"both sides of a comparison share a seed ({a_seed} vs {b_seed})")
        check(pair["pair"]["a"]["variant"] != pair["pair"]["b"]["variant"],
              "…and are different variants")

        voted = json.loads(bytes((await server.experiment_vote(created["id"], {
            "criterion": "likeness", "winner": pair["pair"]["a"]["variant"],
            "loser": pair["pair"]["b"]["variant"], "seed": pair["pair"]["seed"]})).body))
        won = voted["standings"]["likeness"][pair["pair"]["a"]["variant"]]
        check(won["win"] == 1 and won["rate"] == 1.0, f"the vote counts ({won})")
        other = voted["standings"]["beauty"][pair["pair"]["a"]["variant"]]
        check(other["played"] == 0,
              "…and a likeness vote does not leak into the beauty table")

        try:
            await server.run_experiment(created["id"])
            check(False, "re-running an experiment should be refused")
        except HTTPException as exc:
            check("跑過" in str(exc.detail), f"re-running is refused ({exc.detail})")
    finally:
        config.COMFY_URL = old_url
        stub.unlink(missing_ok=True)
        server.EXPERIMENTS.items = saved
        await runner.cleanup()



def test_ui_smoke() -> None:
    """Run the page's own script and call its render functions for real.

    Every other index.html check in this file greps for a substring, which
    proves a line exists and nothing about whether it runs. Four bugs shipped
    behind that in one commit - `artist_tag_models` became a dict in Python
    while the JS still called `.includes()` on it, so the whole style block
    threw and silently disappeared while every grep still passed.
    """
    import shutil
    import subprocess

    import charpacks

    section("ui smoke (real JS)")
    node = shutil.which("node")
    if not node:
        check(True, "node not installed here; skipping the JS smoke test")
        return

    # The browser previews the same token the server will emit, so the two
    # formatters are compared against each other rather than against a guess.
    want = {str(w): charpacks.weighted("artist:x", w) for w in (1, 1.05, 1.2, 1.35, 1.6)}
    done = subprocess.run(
        [node, str(ROOT / "tests" / "ui_smoke.js"), json.dumps(want)],
        capture_output=True, text=True, timeout=120, cwd=str(ROOT),
    )
    out = (done.stdout + done.stderr).strip()
    for line in out.splitlines():
        stripped = line.strip()
        if stripped.startswith("ok "):
            check(True, stripped[3:].strip())
        elif stripped.startswith("FAIL "):
            check(False, stripped[5:].strip())
    check(done.returncode == 0, f"the page's JS runs clean ({out.splitlines()[-1] if out else 'no output'})")


def test_prompts() -> None:
    import prompts

    section("prompt syntax")
    rng = random.Random(0)
    for _ in range(20):
        out = prompts.expand("a {red|blue|green} car", rng)
        check(out in ("a red car", "a blue car", "a green car"), f"wildcard picks one ({out})")
    check(prompts.expand("{2$$a|b|c}", random.Random(1)).count(",") == 1, "N$$ picks N")
    check(prompts.expand("no braces here") == "no braces here", "plain text untouched")
    check(prompts.expand("{}") == "{}", "an empty brace is left alone")
    check(prompts.expand("{single}") == "{single}", "a brace with no | is not a wildcard")
    check(prompts.expand("{a|{b|c}}", random.Random(3)) in ("a", "b", "c"), "nesting resolves")
    check(prompts.has_wildcards("a {x|y}") and not prompts.has_wildcards("a {x}"),
          "wildcard detection needs a |")
    check(len(prompts.preview("{a|b}", 5, seed=1)) == 5, "preview returns the asked-for count")
    check(prompts.preview("{a|b}", 3, seed=7) == prompts.preview("{a|b}", 3, seed=7),
          "preview is reproducible for a seed")

    check(prompts.weights_ok("a (cat:1.2) sitting") == "", "balanced weights pass")
    check(prompts.weights_ok("a (cat:1.2 sitting") != "", "an unclosed ( is caught")
    check(prompts.weights_ok("a cat:1.2) sitting") != "", "a stray ) is caught")
    check(prompts.weights_ok("a \\(cat\\) sitting") == "", "escaped parens are literal text")
    check("lora" in prompts.weights_ok("<lora:foo:1> cat").lower() or
          "LoRA" in prompts.weights_ok("<lora:foo:1> cat"), "A1111 inline lora is called out")
    check(prompts.weights_ok("(cat:3.0)") != "", "an absurd weight is called out")
    check(prompts.weights_ok("") == "", "an empty prompt is fine")
    check(prompts.strip_prefix("score_9, score_8_up, a cat", "score_9, score_8_up") == "a cat",
          "the auto prefix can be removed again")


def test_seconds_to_frames() -> None:
    import workflow

    section("duration")
    # The official Wan template computes floor(seconds * fps + 1).
    check(workflow.frames_for_seconds(5, 16) == 81, "5s @16fps -> 81 frames (the official default)")
    check(workflow.frames_for_seconds(5, 24) == 121, "5s @24fps -> 121 frames")
    for sec in (1, 2, 3, 5, 7.5, 10):
        for fps in (16, 24):
            f = workflow.frames_for_seconds(sec, fps)
            check((f - 1) % 4 == 0, f"{sec}s @{fps} stays 4n+1 ({f})")
            check(abs(workflow.seconds_for_frames(f, fps) - sec) < 0.2,
                  f"{sec}s @{fps} round-trips ({workflow.seconds_for_frames(f, fps)})")
    check(workflow.frames_for_seconds(999, 16) == 241, "absurd duration clamps")
    check(workflow.frames_for_seconds(0, 16) == 5, "zero clamps up to the minimum")


# -- regressions from the code review ----------------------------------------


async def test_review_regressions() -> None:
    """Each case here is a bug the review found; all were real."""
    import aiohttp
    import images
    import registry

    section("review regressions")

    fake = FakeComfy()
    comfy_runner, comfy_url = await start(fake.app())
    models_dir = TMP / "rev-models"
    install(models_dir, registry.get("wan22-14b-fp8"))
    for f in images.get("illustrious").all_files:
        path = models_dir / f.folder / f.name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as fh:
            fh.truncate(f.size)
    # A checkpoint the user installed themselves.
    (models_dir / "checkpoints" / "myMerge_v3.safetensors").write_bytes(b"\0" * 2048)

    env = {
        **os.environ,
        "COMFY_URL": comfy_url,
        "MODELS_DIR": str(models_dir),
        "OUTPUT_DIR": str(TMP / "rev-out"),
        "INBOX_DIR": str(TMP / "rev-in"),
        "MODEL": "wan22-14b-fp8",
        "PYTHONPATH": str(ROOT / "app"),
        "LORAS": "",
    }
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "18424",
        cwd=str(ROOT / "app"), env=env,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
    )
    base = "http://127.0.0.1:18424"
    try:
        async with aiohttp.ClientSession() as s:
            for _ in range(160):
                try:
                    async with s.get(f"{base}/api/health", timeout=5) as r:
                        if r.status == 200:
                            break
                except Exception:  # noqa: BLE001
                    await asyncio.sleep(0.25)
            else:
                out = await proc.stdout.read(4000)
                raise AssertionError(f"server never started:\n{out.decode(errors='replace')}")

            async with s.get(f"{base}/api/image/models") as r:
                cat = await r.json()
            by_id = {m["id"]: m for m in cat["models"]}

            # A user-installed checkpoint must be selectable, not just listed.
            custom_id = "custom:myMerge_v3.safetensors"
            check(custom_id in by_id, f"self-installed checkpoint is a selectable model ({list(by_id)[-1]})")
            check(by_id[custom_id]["installed"], "…and reports installed")
            check(by_id[custom_id]["custom"], "…flagged as custom so the UI can warn")
            check(not by_id[custom_id]["positive_prefix"],
                  "…and gets no borrowed prompt prefix")

            # It must also be removable.
            async with s.delete(f"{base}/api/checkpoints/myMerge_v3.safetensors") as r:
                check(r.status == 200, f"custom checkpoint deletable ({r.status})")
            check(not (models_dir / "checkpoints" / "myMerge_v3.safetensors").exists(),
                  "…file actually gone")
            async with s.delete(f"{base}/api/checkpoints/..%2F..%2Fetc%2Fpasswd") as r:
                check(r.status in (400, 404), f"checkpoint delete blocks traversal ({r.status})")
            async with s.delete(f"{base}/api/checkpoints/Illustrious-XL-v0.1.safetensors") as r:
                check(r.status == 400, "catalogue checkpoints are not deleted this way")

            # An empty negative prompt is a choice, not an omission.
            async with s.post(f"{base}/api/image/generate", json={
                "model": "illustrious", "prompt": "a cat", "negative": "", "batch": 2,
            }) as r:
                job = await r.json()
                check(r.status == 200, f"image job accepted ({r.status})")
            check(job["negative"] == "", f"empty negative survives ({job['negative'][:20]!r})")

            # The auto prefix must be applied once, and the raw prompt kept.
            check(job["prompt"].startswith("masterpiece"), "prefix applied")
            check(job["prompt_raw"] == "a cat", f"raw prompt stored ({job['prompt_raw']})")

            for _ in range(300):
                async with s.get(f"{base}/api/jobs/{job['id']}") as r:
                    job = await r.json()
                if job["status"] in ("done", "error"):
                    break
                await asyncio.sleep(0.1)
            check(job["status"] == "done", f"image job ran ({job['status']}: {job['message'][:70]})")
            check(job["kind"] == "image", "recorded as an image job")
            check(job["model_label"].startswith("Illustrious"),
                  f"image jobs show the friendly label, not the id ({job['model_label']})")

            # Re-running must not prepend the prefix a second time.
            async with s.post(f"{base}/api/image/generate", json={
                "model": "illustrious", "prompt": job["prompt"], "negative": "n",
            }) as r:
                again = await r.json()
            check(again["prompt"].count("masterpiece") == 1,
                  f"prefix not doubled on re-run ({again['prompt'][:60]})")

            # Server-side kind filtering, so one kind cannot hide the other.
            async with s.get(f"{base}/api/jobs?kind=image") as r:
                only = (await r.json())["jobs"]
            check(only and all(j["kind"] == "image" for j in only), "kind=image filters server-side")
            async with s.get(f"{base}/api/jobs?kind=video") as r:
                vids = (await r.json())["jobs"]
            check(all(j["kind"] == "video" for j in vids), "kind=video filters server-side")

            # Stats split videos from images.
            async with s.get(f"{base}/api/library/stats") as r:
                st = await r.json()
            check("videos" in st and "images" in st, "stats break down by kind")
            check(st["images"] >= 1, f"the image job is counted as an image ({st['images']})")

            # A seed of -1 must mean random, not literal 0.
            async with s.post(f"{base}/api/image/generate", json={
                "model": "illustrious", "prompt": "x", "seed": -1,
            }) as r:
                rnd = await r.json()
            check(rnd["seed"] > 0, f"seed -1 becomes a random seed ({rnd['seed']})")
    finally:
        proc.terminate()
        await proc.wait()
        await comfy_runner.cleanup()


async def test_object_info_cache_invalidation() -> None:
    """Downloading a model must not leave validate() blind to it."""
    import registry
    import workflow
    from comfy_client import ComfyClient

    section("schema cache invalidation")
    fake = FakeComfy(installed={"hy15-480p"})
    runner, url = await start(fake.app())
    try:
        client = ComfyClient(url)
        wan = registry.get("wan22-14b-fp8")
        params = registry.GenParams.defaults_for(wan)
        graph = workflow.build(wan, params, image_name="i.png", prompt="p", seed=1,
                               width=832, height=480,
                               available_nodes=await client.node_classes())
        check(bool(await client.validate(graph)), "before install: rejected, as expected")
        check(client._object_info is not None, "…and the schema is now cached")

        # The model arrives; ComfyUI now offers it. The original bug was that
        # the cached schema hid this forever. There are two defences and both
        # must hold: validate() re-reads once before reporting a failure, and
        # anything that changes models/ can still invalidate explicitly.
        fake.installed = None
        check(await client.validate(graph) == [],
              "a failing check re-reads the schema instead of reporting a stale answer")

        fake.installed = {"hy15-480p"}
        client.invalidate()
        check(bool(await client.validate(graph)), "an uninstalled model is still rejected")
        fake.installed = None
        client.invalidate()
        check(await client.validate(graph) == [], "invalidate() also picks up the change")

        # The refresh must not cost a second request when nothing is wrong.
        before = fake.object_info_calls
        check(await client.validate(graph) == [], "a passing graph validates")
        check(fake.object_info_calls == before,
              "a passing graph does not re-read the schema")
    finally:
        await runner.cleanup()


def test_webp_classification() -> None:
    """SaveAnimatedWEBP is the video fallback, so .webp is not always an image."""
    import library

    section("webp classification")
    root = TMP / "webp"
    root.mkdir(parents=True, exist_ok=True)
    (root / ".thumbs").mkdir(exist_ok=True)
    lib = library.Library(root)
    for kind, name in (("video", "v.webp"), ("image", "i.webp"), ("image", "p.png")):
        (root / name).write_bytes(b"x" * 16)
        lib.add(library.Record(id=name, model_id="m", prompt="p", kind=kind,
                               outputs=[name], status="done"))
    st = lib.stats()
    check(st["videos"] == 1, f"a .webp video counts as a video ({st['videos']})")
    check(st["images"] == 2, f"…and .webp/.png images as images ({st['images']})")

    # An orphan has no record, so the extension is all there is to go on.
    (root / "stray.webp").write_bytes(b"x" * 4)
    st = lib.stats()
    check(st["count"] == 4, "orphan still counted in the total")


def test_codex_setup_never_touches_the_key() -> None:
    """The Codex installer must not take a credential, in any form.

    A credential belongs to the user. It must not be a script parameter (it
    lands in shell history and in `ps` output), must not be written to a file
    the script controls, and must never be echoed. `codex login` reads it from
    stdin precisely so none of that happens, so the script's job is to say so
    and step back.
    """
    section("codex setup")
    script = (ROOT / "setup-codex.ps1").read_bytes().decode("utf-8-sig")

    check("param(" not in script.split("function")[0],
          "the script takes no parameters at all, so no key can be passed in")
    # An assignment would mean the script is holding the value.
    bad = [l.strip() for l in script.splitlines()
           if ("OPENAI_API_KEY" in l or "api-key" in l.lower())
           and "=" in l and "Write-Host" not in l]
    check(not bad, f"nothing assigns or captures a key ({bad})")
    check("--with-api-key" in script,
          "…but the stdin-based route is shown to the user")
    check("codex login" in script, "…as is the browser sign-in")
    check("codex login --with-api-key" not in script.replace("| codex login --with-api-key", ""),
          "the script never runs the key-based login itself")

    # Never install a language runtime on someone's machine behind their back.
    for danger in ("winget install", "choco install", "apt-get", "sudo "):
        check(danger not in script, f"the script does not run `{danger.strip()}`")
    check("Install Node.js LTS from https://nodejs.org/" in script,
          "…it tells the user to install Node themselves instead")

    # Same stderr lesson as the git pull bug.
    check("function Invoke-Native" in script,
          "native calls go through a wrapper that judges on the exit code")
    outside = [l.strip() for l in script.splitlines()
               if "2>&1" in l and "&" in l and "$lines" not in l]
    check(not outside, f"no native call merges stderr outside it ({outside})")

    # Re-running must not add the server twice.
    check("mcp', 'list'" in script and "match 'codex'" in script,
          "registration is idempotent - it checks before adding")

    doc = ROOT / "docs" / "codex-mcp.md"
    check(doc.is_file(), "there is a doc explaining it")
    text = doc.read_text(encoding="utf-8")
    check("不要，而且不需要" in text, "…which answers the API-key question first")
    check("用完就丟" in text, "…and is honest that this container cannot hold an install")
    check("沒驗過" in text, "…and separates what was verified from what was not")
    # Measured, not assumed: registering an MCP server mid-session does not make
    # it visible to the session that is already running, and this container is
    # disposable so a fresh session would not have codex installed either.
    check("沒有任何 reload 指令" in text,
          "…and states there is no in-session reload, because there isn't one")
    check("用完就丟" in text, "…and why installing it here cannot persist")
    brief = ROOT / "docs" / "codex-review-brief.md"
    check(brief.is_file(), "there is a self-contained brief a second model can check")
    btext = brief.read_text(encoding="utf-8")
    check("0.884" in btext and "12,544" in btext,
          "…carrying the actual measurements, not just the conclusions")
    check("弱點" in btext and "推論不是實測" in btext,
          "…and naming the weak points itself rather than waiting to be caught")
    check("docs/codex-mcp.md" in (ROOT / "README.md").read_text(encoding="utf-8"),
          "…and the README points at it")

    # The first thing the user tried after installing was typing /codex, which
    # does not exist: the server declares only a `tools` capability and answers
    # nothing for prompts/list, so it contributes no slash command at all.
    # Probed over JSON-RPC against codex-cli 0.147.0. Say so in the doc, or the
    # next reader wastes the same round trip.
    check("沒有 `/codex` 這個指令" in text,
          "…and says up front that /codex is not a command")
    for tool in ("codex-reply", "tools/list", "prompts/list"):
        check(tool in text, f"…and names what the server really exposes ({tool})")
    check("不是你打的" in text,
          "…and explains the tools are called by Claude Code, not typed")


def test_powershell_scripts_parse() -> None:
    """Every shipped .ps1 must parse. Cheap, and the only check that scales.

    These scripts cannot be fully executed here - they install Python packages
    and clone repositories onto a Windows box - so a syntax slip would otherwise
    reach the user as a crash on line 1. The PowerShell parser answers that in
    milliseconds without running a thing.
    """
    import shutil
    import subprocess

    section("powershell scripts parse")
    pwsh = shutil.which("pwsh") or shutil.which("powershell")
    if not pwsh:
        check(True, "PowerShell not installed here; skipping")
        return
    for name in sorted(pth.name for pth in ROOT.glob("*.ps1")):
        probe = (
            "$errs = $null; "
            f"$text = Get-Content -Raw -LiteralPath '{ROOT / name}'; "
            "[void][System.Management.Automation.Language.Parser]::ParseInput("
            "$text, [ref]$null, [ref]$errs); "
            "if ($errs.Count) { $errs | ForEach-Object { "
            "Write-Host \"ERR line $($_.Extent.StartLineNumber): $($_.Message)\" } } "
            "else { Write-Host 'CLEAN' }"
        )
        done = subprocess.run([pwsh, "-NoProfile", "-Command", probe],
                              capture_output=True, text=True, timeout=120)
        out = (done.stdout + done.stderr).strip()
        check("CLEAN" in out, f"{name} parses ({out[:110]})")


def test_windows_script_encoding() -> None:
    """Windows PowerShell 5.1 is unforgiving about how these files are stored.

    Without a UTF-8 BOM it decodes .ps1 using the system ANSI codepage, so the
    Chinese text becomes mojibake - and Big5 trail bytes include { } ' " \\,
    which breaks parsing outright. It also fails to terminate here-strings when
    the line endings are LF-only. pwsh 7 tolerates both, so a parse check alone
    does not catch this; these byte-level invariants do.
    """
    section("windows script encoding")
    bom = b"\xef\xbb\xbf"

    scripts = sorted(pth.name for pth in ROOT.glob("*.ps1"))
    check(len(scripts) >= 4, f"every shipped .ps1 is checked, not a hand-kept three ({scripts})")
    for name in scripts:
        raw = (ROOT / name).read_bytes()
        check(raw.startswith(bom), f"{name} starts with a UTF-8 BOM")
        body = raw[len(bom):]
        lf, crlf = body.count(b"\n"), body.count(b"\r\n")
        check(lf > 0 and lf == crlf, f"{name} is entirely CRLF ({lf} lines, {crlf} CRLF)")

        text = body.decode("utf-8")
        # A here-string opener is @' or @" at the end of a line.
        openers = [
            n for n, line in enumerate(text.splitlines(), 1)
            if line.rstrip().endswith(("@'", '@"'))
        ]
        check(not openers, f"{name} uses no here-strings (lines {openers or 'none'})")

    for name in sorted(pth.name for pth in ROOT.glob("*.bat")):
        raw = (ROOT / name).read_bytes()
        check(not raw.startswith(bom), f"{name} has no BOM (cmd.exe would echo it)")
        try:
            raw.decode("ascii")
            ascii_only = True
        except UnicodeDecodeError:
            ascii_only = False
        check(ascii_only, f"{name} is pure ASCII (read in the system ANSI codepage)")
        lf, crlf = raw.count(b"\n"), raw.count(b"\r\n")
        check(lf > 0 and lf == crlf, f"{name} is entirely CRLF")

    attrs = (ROOT / ".gitattributes").read_text()
    check("*.ps1 -text" in attrs, ".gitattributes stops git normalising .ps1 endings")
    check("*.bat -text" in attrs, ".gitattributes stops git normalising .bat endings")

    # A venv's .exe shims hard-code the interpreter's absolute path, so any use
    # of pip.exe silently breaks as soon as the folder is moved - and moving the
    # folder off the Desktop is the standard cure for Windows refusing writes.
    for name in ("setup-windows.ps1", "start-windows.ps1", "update-windows.ps1"):
        body = (ROOT / name).read_bytes().decode("utf-8-sig")
        # Comments are allowed to name them - that is where the reason is
        # written down. Only real code is checked.
        code = [l for l in body.splitlines() if not l.lstrip().startswith("#")]
        for shim in ("pip.exe", "uvicorn.exe"):
            hits = [n for n, l in enumerate(code, 1) if shim in l]
            check(not hits, f"{name} never calls {shim} (a moved venv breaks it)")


def test_git_stderr_is_not_an_error() -> None:
    """A successful `git pull` writes to stderr, and that must not be fatal.

    Reported failure: the ComfyUI update died on `From
    https://github.com/comfyanonymous/ComfyUI` - which is what git prints after
    a fetch that *worked*. Windows PowerShell 5.1 turns a redirected native
    stderr line into a terminating NativeCommandError while
    $ErrorActionPreference is 'Stop', so the script reported UPDATE DID NOT
    COMPLETE for an update that had already succeeded.

    The decision has to come from the exit code. These cases run the real
    Invoke-Git out of the real script against a stub git.
    """
    import shutil
    import subprocess

    section("git stderr is not an error")
    pwsh = shutil.which("pwsh") or shutil.which("powershell")
    if not pwsh:
        check(True, "PowerShell not installed here; skipping")
        return

    script = (ROOT / "update-windows.ps1").read_bytes().decode("utf-8-sig")
    check("function Invoke-Git" in script, "the script has a native-call wrapper")
    check("$ErrorActionPreference = 'Continue'" in script,
          "…which neutralises the stream around the call")
    # Nothing may pipe native stderr into the pipeline outside that wrapper.
    outside = [
        l.strip() for l in script.replace("\r\n", "\n").split("\n")
        if "2>&1" in l and "&" in l and "$lines" not in l
    ]
    check(not outside, f"no native call merges stderr except inside it ({outside})")

    work = TMP / "gitstderr"
    shutil.rmtree(work, ignore_errors=True)
    (work / "bin").mkdir(parents=True)

    def stub_git(message: str, code: int) -> None:
        """A git that behaves like the real one: chatter on stderr, then exit."""
        shim = work / "bin" / "git"
        shim.write_text(
            "#!/bin/sh\n"
            f'echo "{message}" >&2\n'
            f"exit {code}\n",
            encoding="utf-8",
        )
        shim.chmod(0o755)

    # Lift the function itself out of the shipped script by brace matching, so
    # this exercises the real code rather than a copy that can drift from it.
    body = script.replace("\r\n", "\n")
    start = body.index("function Invoke-Git")
    depth, end = 0, None
    for i in range(body.index("{", start), len(body)):
        if body[i] == "{":
            depth += 1
        elif body[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    check(end is not None, "Invoke-Git can be lifted out of the script")
    func = body[start:end]

    def run_case(label: str) -> str:
        # $ErrorActionPreference = 'Stop' is what the real script sets, and is
        # the condition under which the bug fired.
        harness = (
            "$ErrorActionPreference = 'Stop'\n"
            + func + "\n"
            "$r = Invoke-Git @('pull', '--ff-only')\n"
            "Write-Host \"CODE=$($r.Code) TEXT=$($r.Text)\"\n"
            "Write-Host 'SURVIVED'\n"
        )
        path = work / f"{label}.ps1"
        path.write_text(harness, encoding="utf-8")
        done = subprocess.run(
            [pwsh, "-NoProfile", "-File", str(path)],
            capture_output=True, text=True, timeout=120,
            env={**os.environ, "PATH": f"{work / 'bin'}:{os.environ['PATH']}"},
        )
        return done.stdout + done.stderr

    # 1. The reported case, verbatim: chatter on stderr, exit 0.
    stub_git("From https://github.com/comfyanonymous/ComfyUI", 0)
    out = run_case("success")
    check("SURVIVED" in out, f"a pull that talks on stderr does not kill the script ({out.strip()[:90]})")
    check("CODE=0" in out, f"…and is reported as success ({out.strip()[:70]})")
    check("From https://github.com" in out, "…with the message still available")

    # The ComfyUI step runs last, after the app code is copied and verified, so
    # it must not be able to fail the whole update no matter what it hits.
    tail = body[body.index("更新 ComfyUI 本體") - 400:]
    check("try {" in tail.split("Say '更新 ComfyUI 本體'")[0][-500:],
          "the ComfyUI step is inside a try block")
    check("app 的程式碼已經更新並驗證過了" in body,
          "…and its catch says the app itself is fine")

    # 2. A real failure must still be a failure.
    stub_git("fatal: Not possible to fast-forward, aborting.", 1)
    out = run_case("failure")
    check("SURVIVED" in out, "a genuine failure is also handled without dying")
    check("CODE=1" in out, f"…and is reported as a failure ({out.strip()[:70]})")
    check("fatal:" in out, "…with git's own reason carried through, not swallowed")


def test_update_script_is_atomic() -> None:
    """The update must not leave a half-new, half-old app/ directory.

    Reproduces the reported failure: one file in app/ cannot be overwritten. The
    original code handed whole directories to Copy-Item -Recurse and died
    part-way through, leaving new modules next to old ones - which starts up and
    then fails later in ways that look like a bug in the program.
    """
    import shutil
    import subprocess

    section("update script atomicity")
    pwsh = shutil.which("pwsh") or shutil.which("powershell")
    if not pwsh:
        check(True, "PowerShell not installed here; skipping the behavioural test")
        return

    work = TMP / "upd"
    shutil.rmtree(work, ignore_errors=True)
    src = work / "src" / "wan-video" / "app"
    root = work / "root" / "app"
    for d in (src, root, work / "root" / "models"):
        d.mkdir(parents=True, exist_ok=True)
    names = ["check.py", "images.py", "registry.py", "requirements.txt", "server.py"]
    for n in names:
        (src / n).write_text("NEW\n")
        (root / n).write_text("old\n")
    (src.parent / "README.md").write_text("NEW\n")
    (root.parent / "README.md").write_text("old\n")
    # A folder the installed copy has never seen. Character packs arrived as a
    # brand-new app/packs/, and Copy-Item does not create parent directories -
    # so an update would have "succeeded" with the packs missing.
    (src / "packs").mkdir(parents=True, exist_ok=True)
    (src / "packs" / "hololive.json").write_text("NEW\n")
    (work / "root" / "models" / "big.safetensors").write_text("MODEL\n")
    (work / "root" / ".env").write_text("KEY=secret\n")

    # A destination that cannot be opened for writing. Making it a directory
    # raises the same UnauthorizedAccessException Windows raises for a locked
    # file, controlled-folder-access block, or an antivirus hold.
    (root / "requirements.txt").unlink()
    (root / "requirements.txt").mkdir()

    # Run the real functions out of the real script, so this tests shipped code.
    script = (ROOT / "update-windows.ps1").read_bytes().decode("utf-8-sig")
    harness = f"""
$ErrorActionPreference = 'Stop'
$ast = [System.Management.Automation.Language.Parser]::ParseFile(
  '{(ROOT / "update-windows.ps1").as_posix()}', [ref]$null, [ref]$null)
$fns = $ast.FindAll({{ $args[0] -is
  [System.Management.Automation.Language.FunctionDefinitionAst] }}, $true)
foreach ($f in $fns) {{ Invoke-Expression $f.Extent.Text }}

$src  = '{(work / "src" / "wan-video").as_posix()}'
$root = '{(work / "root").as_posix()}'
$keep = @('ComfyUI','venv','data','models','.env')
$sep  = [IO.Path]::DirectorySeparatorChar
$plan = @()
foreach ($file in Get-ChildItem -Path $src -Recurse -File -Force) {{
  $rel = $file.FullName.Substring($src.Length).TrimStart($sep)
  if ($keep -contains $rel.Split($sep)[0]) {{ continue }}
  $plan += [pscustomobject]@{{ Rel=$rel; From=$file.FullName; To=(Join-Path $root $rel) }}
}}
$blocked = @($plan | Where-Object {{
  (Test-Path -LiteralPath $_.To) -and -not (Test-Writable $_.To) }})
Write-Output ("BLOCKED=" + $blocked.Count)
"""
    done = subprocess.run(
        [pwsh, "-NoProfile", "-Command", harness],
        capture_output=True, text=True, timeout=180,
    )
    out = done.stdout + done.stderr
    check("BLOCKED=1" in out, f"the unwritable file is found before copying ({out.strip()[:120]})")

    # The whole point: having found it, nothing was touched.
    untouched = [n for n in names if n != "requirements.txt"]
    check(all((root / n).read_text().strip() == "old" for n in untouched),
          "no app file was overwritten")
    check((root.parent / "README.md").read_text().strip() == "old", "nor anything above it")
    check((work / "root" / "models" / "big.safetensors").read_text().strip() == "MODEL",
          "models untouched")
    check((work / "root" / ".env").read_text().strip() == "KEY=secret", ".env untouched")

    # And with the blockage cleared, the same plan copies everything.
    (root / "requirements.txt").rmdir()
    (root / "requirements.txt").write_text("old\n")
    copy = harness.replace(
        'Write-Output ("BLOCKED=" + $blocked.Count)',
        """$failed = @()
foreach ($i in $plan) {{ if (-not (Copy-One $i.From $i.To)) {{ $failed += $i }} }}
Write-Output ("BLOCKED=" + $blocked.Count + " FAILED=" + $failed.Count)""".replace("{{", "{").replace("}}", "}"),
    )
    done = subprocess.run(
        [pwsh, "-NoProfile", "-Command", copy],
        capture_output=True, text=True, timeout=180,
    )
    out = done.stdout + done.stderr
    check("BLOCKED=0 FAILED=0" in out, f"nothing blocks the retry ({out.strip()[:120]})")
    check(all((root / n).read_text().strip() == "NEW" for n in names),
          "re-running after the fix updates every file")
    new_dir = root / "packs" / "hololive.json"
    check(new_dir.is_file() and new_dir.read_text().strip() == "NEW",
          "a folder the installed copy never had is created, not skipped")
    check((work / "root" / "models" / "big.safetensors").read_text().strip() == "MODEL",
          "models still untouched by the successful run")
    check((work / "root" / ".env").read_text().strip() == "KEY=secret",
          ".env still untouched by the successful run")


# -- library / gallery -------------------------------------------------------


def test_library() -> None:
    import library

    section("library")
    root = TMP / "lib"
    import shutil

    if root.exists():
        shutil.rmtree(root)
    (root / ".thumbs").mkdir(parents=True)

    lib = library.Library(root)
    for i in range(3):
        r = library.Record(id=f"job{i}", model_id="wan22-14b-fp8", prompt=f"p{i}", status="done")
        r.output = f"job{i}.mp4"
        r.thumb = f"job{i}.jpg"
        (root / r.output).write_bytes(b"video" * 100)
        (root / ".thumbs" / r.thumb).write_bytes(b"jpg")
        lib.add(r)
    check(len(lib.recent()) == 3, "three records stored")
    check(lib.index.is_file(), "history file written")

    # Reload from disk: the whole point of persisting.
    again = library.Library(root)
    again.load()
    check(len(again.recent()) == 3, f"records survive a restart ({len(again.recent())})")
    check(again.recent()[0].id == "job2", "newest first")

    # A record whose video vanished must not come back as a dead link.
    (root / "job1.mp4").unlink()
    third = library.Library(root)
    third.load()
    check({r.id for r in third.recent()} == {"job0", "job2"},
          f"record with a missing file is dropped ({[r.id for r in third.recent()]})")

    stats = third.stats()
    check(stats["count"] == 2 and stats["bytes"] > 0, f"disk stats ({stats['count']}, {stats['bytes']}B)")

    check(third.star("job0", True), "starring works")
    check(third.clear(keep_starred=True) == 1, "clear keeps starred")
    check([r.id for r in third.recent()] == ["job0"], "starred record survived")
    check(not (root / "job2.mp4").exists(), "cleared video deleted from disk")
    check((root / "job0.mp4").exists(), "starred video kept on disk")

    # Orphan sweep: a file with no record.
    (root / "stray.mp4").write_bytes(b"x" * 10)
    check(third.sweep_orphans() == 1, "orphan swept")
    check(not (root / "stray.mp4").exists(), "orphan file gone")
    check((root / "job0.mp4").exists(), "known file untouched by sweep")

    # An interrupted job should not come back as still-running.
    r = library.Record(id="mid", model_id="wan22-14b-fp8", prompt="x", status="running")
    third.add(r)
    fourth = library.Library(root)
    fourth.load()
    revived = next(x for x in fourth.recent() if x.id == "mid")
    check(revived.status == "error" and "重啟" in revived.message,
          f"interrupted job marked failed ({revived.status})")


# -- VRAM advice -------------------------------------------------------------


def test_vram_advice() -> None:
    section("vram advice")
    sys.path.insert(0, str(ROOT / "app"))
    import registry
    import server

    wan = registry.get("wan22-14b-fp8")   # recommends 24GB
    hy = registry.get("hy15-480p")        # recommends 10GB

    plenty = server.vram_advice(wan, 24)
    check(plenty["level"] == "ok", f"24GB card on a 24GB model is ok ({plenty['level']})")

    tight = server.vram_advice(wan, 12)
    check(tight["level"] == "tight", f"12GB on 24GB is tight ({tight['level']})")
    check("跑得動" in tight["text"], "tight advice says it still runs")
    check(tight["flags"] == "--lowvram", f"suggests --lowvram ({tight['flags']})")

    dire = server.vram_advice(wan, 8)
    check(dire["level"] == "very_tight", f"8GB on 24GB is very tight ({dire['level']})")
    check("跑得動" in dire["text"], "very tight advice still says it runs")
    check(dire["flags"] == "--novram", f"suggests --novram ({dire['flags']})")

    check(server.vram_advice(hy, 10)["level"] == "ok", "10GB card on the 10GB model is ok")
    check(server.vram_advice(wan, 0)["level"] == "unknown", "no reading -> unknown, not a block")

    # The whole point: advice is never a refusal.
    for gb_ in (0, 4, 8, 12, 24, 48):
        a = server.vram_advice(wan, gb_)
        check("不能" not in a["text"] and "無法" not in a["text"],
              f"advice at {gb_}GB never says it cannot run")


# -- CivitAI -----------------------------------------------------------------


async def test_civitai() -> None:
    import civitai

    section("civitai client")
    fake = FakeCivitai()
    runner, url = await start(fake.app())
    fake.base = url
    old_api, old_key = civitai.API, os.environ.get("CIVITAI_API_KEY")
    civitai.API = f"{url}/api/v1"
    os.environ.pop("CIVITAI_API_KEY", None)
    try:
        res = await civitai.search(query="", base_models=["Wan Video 2.2 I2V-A14B"])
        names = [i["name"] for i in res["items"]]
        check("Glass Kiss" in names, f"base-model filter returns Wan 2.2 I2V items ({names})")
        check("T2V Only Thing" not in names, "other base models filtered out")
        check("Broken" not in names, "model with no weight file is dropped")
        check(res["next_cursor"] == "2", f"cursor passed through ({res['next_cursor']})")
        check(fake.searches[-1]["types"] == "LORA", "always asks for LORA type")

        glass = next(i for i in res["items"] if i["name"] == "Glass Kiss")
        files = glass["versions"][0]["files"]
        check(len(files) == 2, f"only weight files kept ({[f['name'] for f in files]})")
        check(all(f["size"] == 4096 * 1024 for f in files), "sizeKB converted to bytes")
        check(glass["versions"][0]["trained_words"] == ["glasskiss"], "trigger words parsed")
        check(glass["url"].endswith("/models/1"), "page url built")

        page2 = await civitai.search(cursor="2")
        check(page2["items"], "cursor fetches another page")

        nsfw = await civitai.search(nsfw=True)
        check(all(i["nsfw"] for i in nsfw["items"]) and nsfw["items"], "nsfw filter honoured")

        # Downloads need a key; search does not.
        try:
            civitai.download_headers()
            check(False, "download without a key raises")
        except civitai.NeedsApiKey as exc:
            check("API key" in str(exc), f"clear message about the key ({str(exc)[:30]})")

        os.environ["CIVITAI_API_KEY"] = "testkey"
        headers = civitai.download_headers()
        check(headers["Authorization"] == "Bearer testkey", "key becomes a bearer token")
        check("User-Agent" in headers, "download sends a User-Agent too")
    finally:
        civitai.API = old_api
        if old_key is None:
            os.environ.pop("CIVITAI_API_KEY", None)
        else:
            os.environ["CIVITAI_API_KEY"] = old_key
        await runner.cleanup()

    section("civitai 403 without a User-Agent")
    fake2 = FakeCivitai()
    runner, url = await start(fake2.app())
    fake2.base = url
    try:
        import aiohttp

        async with aiohttp.ClientSession(skip_auto_headers=["User-Agent"]) as s:
            async with s.get(f"{url}/api/v1/models") as r:
                check(r.status == 403, f"the fake reproduces the real 403 ({r.status})")
    finally:
        await runner.cleanup()


async def test_lora_download() -> None:
    import civitai
    import downloader
    import registry

    section("lora download")
    fake = FakeCivitai()
    runner, url = await start(fake.app())
    fake.base = url
    root = TMP / "lora-models"
    (root / "loras").mkdir(parents=True, exist_ok=True)
    manager = downloader.Manager(root)
    try:
        os.environ["CIVITAI_API_KEY"] = "testkey"
        headers = tuple(civitai.download_headers().items())
        files = [
            downloader.RemoteFile(url=f"{url}/api/download/models/10", folder="loras",
                                  name="glass_kiss_high.safetensors", size=4096, headers=headers),
            downloader.RemoteFile(url=f"{url}/api/download/models/11", folder="loras",
                                  name="glass_kiss_low.safetensors", size=4096, headers=headers),
        ]
        dl = manager.enqueue_files(
            key="civitai:10", label="LoRA · Glass Kiss", files=files,
            sidecars={f.name: {"trained_words": ["glasskiss"], "url": "https://civitai.com/models/1",
                               "base_model": "Wan Video 2.2 I2V-A14B"} for f in files},
        )
        for _ in range(400):
            if dl.status in ("done", "error", "cancelled"):
                break
            await asyncio.sleep(0.02)
        check(dl.status == "done", f"lora download completed ({dl.status}: {dl.message})")
        check(dl.kind == "lora", "download is tagged as a lora")
        for f in files:
            path = root / "loras" / f.name
            check(path.is_file() and path.stat().st_size == 4096, f"{f.name} written")
            check(path.with_name(path.name + ".civitai.json").is_file(), f"{f.name} sidecar written")

        listed = manager.list_loras()
        entry = next(l for l in listed if l["name"] == "glass_kiss_high.safetensors")
        check(entry["trained_words"] == ["glasskiss"], "trigger words read back from the sidecar")
        check(entry["base_model"].startswith("Wan Video 2.2"), "base model read back")
        check(entry["source"].endswith("/models/1"), "source url read back")

        check(manager.delete_lora("glass_kiss_high.safetensors"), "delete works")
        check(not (root / "loras" / "glass_kiss_high.safetensors").exists(), "file gone")
        check(not (root / "loras" / "glass_kiss_high.safetensors.civitai.json").exists(),
              "sidecar removed too")
        check(not manager.delete_lora("nope.safetensors"), "deleting a missing lora returns False")
        for bad in ("../evil", "a/b", "..", ""):
            try:
                manager.lora_path(bad)
                check(False, f"path traversal blocked: {bad!r}")
            except ValueError:
                check(True, f"path traversal blocked: {bad!r}")

        # Without a key the fetch must fail with a message that says why.
        os.environ.pop("CIVITAI_API_KEY", None)
        nokey = manager.enqueue_files(
            key="civitai:11", label="no key",
            files=[downloader.RemoteFile(url=f"{url}/api/download/models/10", folder="loras",
                                         name="nokey.safetensors", size=4096)],
        )
        for _ in range(400):
            if nokey.status in ("done", "error", "cancelled"):
                break
            await asyncio.sleep(0.02)
        check(nokey.status == "error" and "API key" in nokey.message,
              f"401 explained as a missing key ({nokey.message[:60]})")

        worker = manager.stop()
        if worker:
            worker.cancel()
    finally:
        os.environ.pop("CIVITAI_API_KEY", None)
        await runner.cleanup()


async def test_watcher() -> None:
    section("watcher")
    import importlib

    watch_dir = TMP / "watch"
    (watch_dir / "inbox").mkdir(parents=True, exist_ok=True)
    os.environ["INBOX_DIR"] = str(watch_dir / "inbox")
    os.environ["DONE_DIR"] = str(watch_dir / "inbox" / "done")
    import config

    importlib.reload(config)
    import watcher

    importlib.reload(watcher)

    img = watch_dir / "inbox" / "a_girl_turning_around.png"
    img.write_bytes(sample_png((64, 64)))
    check(watcher.prompt_for(img) == "a girl turning around", "filename becomes the prompt")
    img.with_suffix(".txt").write_text("鏡頭緩慢推近", encoding="utf-8")
    check(watcher.prompt_for(img) == "鏡頭緩慢推近", "sidecar .txt wins")
    blank = watch_dir / "inbox" / "___.png"
    blank.write_bytes(sample_png((64, 64)))
    check(watcher.prompt_for(blank) == watcher.PROMPT_DEFAULT, "falls back to the default prompt")
    check(watcher.IMAGE_SUFFIXES >= {".png", ".jpg", ".jpeg", ".webp"}, "common formats watched")


async def main() -> int:
    live = "--live" in sys.argv
    # Previous runs leave models, outputs and history behind; without this the
    # suite passes or fails depending on what ran before it.
    if TMP.exists():
        import shutil

        shutil.rmtree(TMP)
    TMP.mkdir(parents=True, exist_ok=True)
    test_registry()
    test_dimensions()
    await test_graphs()
    await test_validator()
    await test_video_fallback()
    await test_downloader()
    await test_client()
    await test_server()
    await test_uninstalled_model_is_refused_up_front()
    test_library()
    test_image_registry()
    await test_image_graphs()
    await test_image_extras()
    await test_controlnet()
    await test_video_post()
    await test_new_endpoints()
    await test_comics()
    test_promptbook()
    test_restage()
    await test_restage_deferred()
    test_second_review_regressions()
    test_inspect_image()
    await test_charpacks()
    await test_settings_and_updates()
    test_vendored_skill()
    test_accessibility()
    test_ui_smoke()
    test_naiweights()
    test_posebook()
    test_inspect_parts()
    test_quicktags()
    test_artists()
    test_likeness()
    test_refs()
    test_ref_chinese_names()
    test_ref_folder_import(TMP / "reffolder")
    test_experiments()
    test_styles()
    test_promptmerge()
    test_promptdoctor()
    await test_experiment_run()
    test_prompts()
    test_seconds_to_frames()
    test_vram_advice()
    await test_civitai()
    await test_lora_download()
    await test_review_regressions()
    await test_object_info_cache_invalidation()
    test_webp_classification()
    test_codex_setup_never_touches_the_key()
    test_powershell_scripts_parse()
    test_windows_script_encoding()
    test_git_stderr_is_not_an_error()
    test_update_script_is_atomic()
    await test_watcher()
    if live:
        await test_graphs(os.environ.get("COMFY_URL", "http://127.0.0.1:8188"))

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

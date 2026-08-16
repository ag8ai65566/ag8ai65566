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

    # A single illustration has flat bands that read as gutters, but of wildly
    # varying width. That inconsistency is the proof it has no panel grid.
    flat = pagelayout.detect(art(800, 1200, 9))
    check(len(flat.boxes) == 1, f"a full-bleed image is one panel ({len(flat.boxes)})")
    check(flat.confidence < 0.6, f"…and says it is unsure ({flat.confidence:.2f})")
    check("滿版" in flat.note, "…explaining why, rather than drawing 6 rectangles")

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
    check("const TABS = [...document.querySelectorAll('.tabs button')]" in page,
          "the switcher derives its tab list from the DOM, not a hand-kept array")

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

    for name in ("setup-windows.ps1", "start-windows.ps1", "update-windows.ps1"):
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

    for name in ("install.bat", "start.bat", "update.bat"):
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
    await test_video_post()
    await test_new_endpoints()
    await test_comics()
    test_promptbook()
    test_restage()
    test_second_review_regressions()
    test_inspect_image()
    test_prompts()
    test_seconds_to_frames()
    test_vram_advice()
    await test_civitai()
    await test_lora_download()
    await test_review_regressions()
    await test_object_info_cache_invalidation()
    test_webp_classification()
    test_windows_script_encoding()
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

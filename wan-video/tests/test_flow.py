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
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from aiohttp import web  # noqa: E402
from fake_comfy import FakeComfy  # noqa: E402
from PIL import Image  # noqa: E402

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
            check("把圖片拖進來" in html and "模型管理" in html, "UI serves with both tabs")

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
            check("模型管理" in detail, "message points at the model manager")
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

    for name in ("setup-windows.ps1", "start-windows.ps1"):
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

    for name in ("install.bat", "start.bat"):
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
    test_registry()
    test_dimensions()
    await test_graphs()
    await test_validator()
    await test_video_fallback()
    await test_downloader()
    await test_client()
    await test_server()
    await test_uninstalled_model_is_refused_up_front()
    test_windows_script_encoding()
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

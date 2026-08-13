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
from fake_civitai import FakeCivitai  # noqa: E402
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
        for model in images.IMAGE_MODELS:
            for hires in (0.0, 1.5):
                w, h = list(model.sizes.values())[0]
                g = images.build(model, prompt="p", negative="n", seed=1, width=w, height=h,
                                 batch=3, hires_scale=hires,
                                 loras=[("my_style.safetensors", 0.8)],
                                 available_nodes=nodes)
                problems = await client.validate(g)
                check(problems == [], f"{model.id} hires={hires} validates {problems[:1]}")

        model = images.get("illustrious")
        g = images.build(model, prompt="p", negative="n", seed=7, width=832, height=1216,
                         batch=4, loras=[("a.safetensors", 0.6), ("b.safetensors", 1.0)],
                         available_nodes=nodes)
        check(len(nodes_of(g, "LoraLoader")) == 2, "two LoRAs chained")
        check(all(n["inputs"]["strength_model"] == n["inputs"]["strength_clip"]
                  for n in nodes_of(g, "LoraLoader")), "image LoRAs drive model and CLIP together")
        check(nodes_of(g, "EmptyLatentImage")[0]["inputs"]["batch_size"] == 4, "batch size wired")
        check(len(nodes_of(g, "CLIPSetLastLayer")) == 1, "clip skip -2 adds the node")
        check(nodes_of(g, "CLIPSetLastLayer")[0]["inputs"]["stop_at_clip_layer"] == -2, "…with -2")
        check(len(nodes_of(g, "KSampler")) == 1, "single pass without hires")

        g2 = images.build(images.get("juggernaut"), prompt="p", negative="n", seed=1,
                          width=1024, height=1024, available_nodes=nodes)
        check(nodes_of(g2, "CLIPSetLastLayer") == [], "clip skip -1 omits the node entirely")

        g3 = images.build(model, prompt="p", negative="n", seed=1, width=1024, height=1024,
                          hires_scale=1.5, hires_denoise=0.4, available_nodes=nodes)
        ks = nodes_of(g3, "KSampler")
        check(len(ks) == 2, "hires adds a second sampler")
        check(ks[0]["inputs"]["denoise"] == 1.0 and ks[1]["inputs"]["denoise"] == 0.4,
              "second pass uses the hires denoise")
        up = nodes_of(g3, "LatentUpscale")[0]["inputs"]
        check(up["width"] == 1536 and up["width"] % 8 == 0, f"upscaled to a legal size ({up['width']})")

        check(nodes_of(g, "SaveImage")[0]["inputs"]["filename_prefix"].startswith("img/"),
              "images save under their own prefix")
    finally:
        await runner.cleanup()


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

        # The model arrives; ComfyUI now offers it.
        fake.installed = None
        check(bool(await client.validate(graph)),
              "stale cache still rejects it (this was the bug)")
        client.invalidate()
        check(await client.validate(graph) == [],
              "after invalidate() the freshly installed model validates")
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
    test_seconds_to_frames()
    test_vram_advice()
    await test_civitai()
    await test_lora_download()
    await test_review_regressions()
    await test_object_info_cache_invalidation()
    test_webp_classification()
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

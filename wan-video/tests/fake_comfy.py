"""A stand-in ComfyUI server for testing without a GPU.

The node schemas in schema_core.json were dumped from a real ComfyUI 0.32.0
/object_info, so the validator here exercises exactly the shapes the real
server enforces. Only the file-listing combos are substituted, since those
depend on what is on disk.

Regenerate the fixture against a running ComfyUI with:
    python3 tests/dump_schema.py http://127.0.0.1:8188
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from aiohttp import WSMsgType, web

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
import images  # noqa: E402
import registry  # noqa: E402

SCHEMA = json.loads((Path(__file__).parent / "schema_core.json").read_text())

# (node class, input name) -> which models/<folder> the combo lists
FILE_INPUTS = {
    ("CheckpointLoaderSimple", "ckpt_name"): ("checkpoints",),
    ("UNETLoader", "unet_name"): ("diffusion_models", "unet"),
    ("UnetLoaderGGUF", "unet_name"): ("unet",),
    ("CLIPLoader", "clip_name"): ("text_encoders",),
    ("DualCLIPLoader", "clip_name1"): ("text_encoders",),
    ("DualCLIPLoader", "clip_name2"): ("text_encoders",),
    ("CLIPVisionLoader", "clip_name"): ("clip_vision",),
    ("VAELoader", "vae_name"): ("vae",),
    ("LoraLoaderModelOnly", "lora_name"): ("loras",),
    ("CLIPSetLastLayer", "__none__"): (),
    ("LoraLoader", "lora_name"): ("loras",),
    ("LoadImage", "image"): ("__images__",),
}

EXTRA_LORAS = ["spicy_style.safetensors", "my_style.safetensors"]


def installed_names(folders: tuple[str, ...], only: set[str] | None) -> list[str]:
    """Filenames the fake install exposes for the given models/<folder> dirs."""
    if folders == ("__images__",):
        return ["example.png"]
    names: set[str] = set()
    if "checkpoints" in folders:
        names.update(f.name for m in images.IMAGE_MODELS for f in m.all_files
                     if f.folder == "checkpoints")
    if "vae" in folders:
        names.update(f.name for m in images.IMAGE_MODELS for f in m.all_files
                     if f.folder == "vae")
    for model in registry.MODELS:
        if only is not None and model.id not in only:
            continue
        for f in model.all_files:
            if f.folder in folders:
                names.add(f.name)
    if "loras" in folders:
        names.update(EXTRA_LORAS)
    return sorted(names)


def object_info(video_nodes: set[str], installed: set[str] | None = None) -> dict:
    info: dict = {}
    for name, schema in SCHEMA.items():
        if name in ("CreateVideo", "SaveVideo", "VHS_VideoCombine") and name not in video_nodes:
            continue
        spec = {"required": {}, "optional": {}}
        for kind in ("required", "optional"):
            for key, value in (schema["input"].get(kind) or {}).items():
                folders = FILE_INPUTS.get((name, key))
                if folders:
                    rest = value[1] if len(value) > 1 else {}
                    spec[kind][key] = [installed_names(folders, installed), rest]
                else:
                    spec[kind][key] = value
        info[name] = {"input": spec, "output": schema.get("output", [])}

    if "VHS_VideoCombine" in video_nodes:
        info["VHS_VideoCombine"] = {
            "input": {
                "required": {
                    "images": ["IMAGE"],
                    "frame_rate": ["FLOAT", {"default": 8.0}],
                    "loop_count": ["INT", {"default": 0}],
                    "filename_prefix": ["STRING", {"default": "AnimateDiff"}],
                    "format": [["image/gif", "video/h264-mp4", "video/webm"]],
                    "pix_fmt": [["yuv420p", "yuv420p10le"]],
                    "crf": ["INT", {"default": 19}],
                    "save_metadata": ["BOOLEAN", {"default": True}],
                    "pingpong": ["BOOLEAN", {"default": False}],
                    "save_output": ["BOOLEAN", {"default": True}],
                },
                "optional": {"audio": ["AUDIO"]},
            },
            "output": ["VHS_FILENAMES"],
        }
    return info


class FakeComfy:
    """Records what it was asked to do so tests can assert on the graph."""

    def __init__(
        self,
        video_nodes: set[str] | None = None,
        fail: str | None = None,
        installed: set[str] | None = None,
    ) -> None:
        self.video_nodes = video_nodes if video_nodes is not None else {"CreateVideo", "SaveVideo"}
        self.fail = fail
        self.installed = installed
        self.graphs: list[dict] = []
        self.uploads: list[str] = []
        self.video_bytes = b"\x00\x00\x00\x18ftypmp42FAKE-MP4-PAYLOAD"
        self.interrupts = 0

    def app(self) -> web.Application:
        app = web.Application()
        app.add_routes(
            [
                web.get("/system_stats", self.stats),
                web.get("/object_info", self.info),
                web.post("/upload/image", self.upload),
                web.post("/prompt", self.prompt),
                web.post("/interrupt", self.interrupt),
                web.get("/ws", self.ws),
                web.get("/history/{pid}", self.history),
                web.get("/view", self.view),
            ]
        )
        return app

    async def stats(self, _req):
        return web.json_response({"system": {"comfyui_version": "fake-0.32.0"}})

    async def info(self, _req):
        return web.json_response(object_info(self.video_nodes, self.installed))

    async def upload(self, req):
        data = await req.post()
        field = data["image"]
        self.uploads.append(field.filename)
        return web.json_response(
            {"name": field.filename, "subfolder": data.get("subfolder", ""), "type": "input"}
        )

    async def prompt(self, req):
        body = await req.json()
        self.graphs.append(body["prompt"])
        return web.json_response({"prompt_id": "fake-prompt-1", "number": 1})

    async def interrupt(self, _req):
        self.interrupts += 1
        return web.json_response({})

    async def ws(self, req):
        ws = web.WebSocketResponse()
        await ws.prepare(req)
        before = len(self.graphs)
        for _ in range(200):
            if len(self.graphs) > before:
                break
            await asyncio.sleep(0.02)

        if self.fail == "execution_error":
            await ws.send_json(
                {
                    "type": "execution_error",
                    "data": {
                        "prompt_id": "fake-prompt-1",
                        "node_type": "KSamplerAdvanced",
                        "exception_message": "CUDA out of memory",
                    },
                }
            )
            return ws

        for step in range(1, 5):
            await ws.send_json(
                {"type": "progress", "data": {"value": step, "max": 4, "prompt_id": "fake-prompt-1"}}
            )
            await asyncio.sleep(0.01)
        await ws.send_json({"type": "executing", "data": {"node": None, "prompt_id": "fake-prompt-1"}})
        async for msg in ws:
            if msg.type is WSMsgType.ERROR:
                break
        return ws

    async def history(self, _req):
        outputs = {} if self.fail == "no_output" else {
            "15": {
                "images": [{"filename": "anim_00001.png", "subfolder": "wan", "type": "output"}],
                "videos": [{"filename": "anim_00001.mp4", "subfolder": "wan", "type": "output"}],
            }
        }
        return web.json_response(
            {"fake-prompt-1": {"status": {"status_str": "success", "completed": True}, "outputs": outputs}}
        )

    async def view(self, req):
        assert req.query["filename"].endswith(".mp4"), "should fetch the video, not a frame"
        return web.Response(body=self.video_bytes, content_type="video/mp4")


async def serve(port: int) -> None:
    fake = FakeComfy()
    runner = web.AppRunner(fake.app())
    await runner.setup()
    await web.TCPSite(runner, "127.0.0.1", port).start()
    print(f"fake comfy on :{port}", flush=True)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(serve(int(sys.argv[1]) if len(sys.argv) > 1 else 18188))

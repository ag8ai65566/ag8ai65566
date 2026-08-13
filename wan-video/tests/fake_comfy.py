"""A stand-in ComfyUI server for testing without a GPU.

Mirrors the real /object_info schema shape closely enough that the validator in
comfy_client exercises the same code paths it will hit against real ComfyUI.
"""

from __future__ import annotations

import asyncio
import json
import sys

from aiohttp import WSMsgType, web

MODELS = {
    "diffusion": [
        "wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors",
        "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors",
    ],
    "gguf": [
        "Wan2.2-I2V-A14B-HighNoise-Q4_K_M.gguf",
        "Wan2.2-I2V-A14B-LowNoise-Q4_K_M.gguf",
    ],
    "clip": ["umt5_xxl_fp8_e4m3fn_scaled.safetensors"],
    "vae": ["wan_2.1_vae.safetensors"],
    "loras": [
        "wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors",
        "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors",
        "my_style.safetensors",
    ],
    "images": ["example.png"],
}

SAMPLERS = ["euler", "euler_ancestral", "dpmpp_2m", "ddim", "uni_pc"]
SCHEDULERS = ["normal", "karras", "exponential", "simple", "beta"]

FLOAT = ["FLOAT", {"default": 1.0}]
INT = ["INT", {"default": 1}]
BOOL = ["BOOLEAN", {"default": True}]


def object_info(video_nodes: set[str]) -> dict:
    info = {
        "UNETLoader": {
            "input": {
                "required": {
                    "unet_name": [MODELS["diffusion"]],
                    "weight_dtype": [["default", "fp8_e4m3fn", "fp8_e4m3fn_fast", "fp8_e5m2"]],
                }
            },
            "output": ["MODEL"],
        },
        "UnetLoaderGGUF": {
            "input": {"required": {"unet_name": [MODELS["gguf"]]}},
            "output": ["MODEL"],
        },
        "CLIPLoader": {
            "input": {
                "required": {
                    "clip_name": [MODELS["clip"]],
                    "type": [["stable_diffusion", "sdxl", "flux", "wan", "hunyuan_video"]],
                },
                "optional": {"device": [["default", "cpu"]]},
            },
            "output": ["CLIP"],
        },
        "VAELoader": {
            "input": {"required": {"vae_name": [MODELS["vae"]]}},
            "output": ["VAE"],
        },
        "LoraLoaderModelOnly": {
            "input": {
                "required": {
                    "model": ["MODEL"],
                    "lora_name": [MODELS["loras"]],
                    "strength_model": FLOAT,
                }
            },
            "output": ["MODEL"],
        },
        "ModelSamplingSD3": {
            "input": {"required": {"model": ["MODEL"], "shift": FLOAT}},
            "output": ["MODEL"],
        },
        "CLIPTextEncode": {
            "input": {"required": {"text": ["STRING", {"multiline": True}], "clip": ["CLIP"]}},
            "output": ["CONDITIONING"],
        },
        "LoadImage": {
            "input": {"required": {"image": [MODELS["images"], {"image_upload": True}]}},
            "output": ["IMAGE", "MASK"],
        },
        "WanImageToVideo": {
            "input": {
                "required": {
                    "positive": ["CONDITIONING"],
                    "negative": ["CONDITIONING"],
                    "vae": ["VAE"],
                    "width": INT,
                    "height": INT,
                    "length": INT,
                    "batch_size": INT,
                },
                "optional": {"clip_vision_output": ["CLIP_VISION_OUTPUT"], "start_image": ["IMAGE"]},
            },
            "output": ["CONDITIONING", "CONDITIONING", "LATENT"],
        },
        "KSamplerAdvanced": {
            "input": {
                "required": {
                    "model": ["MODEL"],
                    "add_noise": [["enable", "disable"]],
                    "noise_seed": INT,
                    "steps": INT,
                    "cfg": FLOAT,
                    "sampler_name": [SAMPLERS],
                    "scheduler": [SCHEDULERS],
                    "positive": ["CONDITIONING"],
                    "negative": ["CONDITIONING"],
                    "latent_image": ["LATENT"],
                    "start_at_step": INT,
                    "end_at_step": INT,
                    "return_with_leftover_noise": [["disable", "enable"]],
                }
            },
            "output": ["LATENT"],
        },
        "VAEDecode": {
            "input": {"required": {"samples": ["LATENT"], "vae": ["VAE"]}},
            "output": ["IMAGE"],
        },
        "SaveAnimatedWEBP": {
            "input": {
                "required": {
                    "images": ["IMAGE"],
                    "filename_prefix": ["STRING", {"default": "ComfyUI"}],
                    "fps": FLOAT,
                    "lossless": BOOL,
                    "quality": INT,
                    "method": [["default", "fastest", "slowest"]],
                }
            },
            "output": [],
        },
    }
    if "CreateVideo" in video_nodes:
        info["CreateVideo"] = {
            "input": {"required": {"images": ["IMAGE"], "fps": FLOAT}, "optional": {"audio": ["AUDIO"]}},
            "output": ["VIDEO"],
        }
        info["SaveVideo"] = {
            "input": {
                "required": {
                    "video": ["VIDEO"],
                    "filename_prefix": ["STRING", {"default": "video/ComfyUI"}],
                    "format": [["auto", "mp4", "webm"]],
                    "codec": [["auto", "h264", "vp9"]],
                }
            },
            "output": [],
        }
    if "VHS_VideoCombine" in video_nodes:
        info["VHS_VideoCombine"] = {
            "input": {
                "required": {
                    "images": ["IMAGE"],
                    "frame_rate": FLOAT,
                    "loop_count": INT,
                    "filename_prefix": ["STRING", {"default": "AnimateDiff"}],
                    "format": [["image/gif", "video/h264-mp4", "video/webm"]],
                    "pix_fmt": [["yuv420p", "yuv420p10le"]],
                    "crf": INT,
                    "save_metadata": BOOL,
                    "pingpong": BOOL,
                    "save_output": BOOL,
                },
                "optional": {"audio": ["AUDIO"]},
            },
            "output": ["VHS_FILENAMES"],
        }
    return info


class FakeComfy:
    """Records what it was asked to do so tests can assert on the graph."""

    def __init__(self, video_nodes: set[str] | None = None, fail: str | None = None) -> None:
        self.video_nodes = video_nodes if video_nodes is not None else {"CreateVideo", "SaveVideo"}
        self.fail = fail
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
        return web.json_response({"system": {"comfyui_version": "fake"}})

    async def info(self, _req):
        return web.json_response(object_info(self.video_nodes))

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
        # Wait for the client to queue its prompt, as real ComfyUI would.
        for _ in range(100):
            if self.graphs:
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
                {
                    "type": "progress",
                    "data": {"value": step, "max": 4, "prompt_id": "fake-prompt-1"},
                }
            )
            await asyncio.sleep(0.01)
        await ws.send_json(
            {"type": "executing", "data": {"node": None, "prompt_id": "fake-prompt-1"}}
        )
        async for msg in ws:
            if msg.type is WSMsgType.ERROR:
                break
        return ws

    async def history(self, _req):
        if self.fail == "no_output":
            outputs = {}
        else:
            outputs = {
                "15": {
                    "images": [
                        {"filename": "anim_00001.png", "subfolder": "wan", "type": "output"}
                    ],
                    "videos": [
                        {"filename": "anim_00001.mp4", "subfolder": "wan", "type": "output"}
                    ],
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

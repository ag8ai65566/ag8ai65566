"""Drop an image, pick a model, type an instruction, get a short animation.

A single-worker queue in front of ComfyUI: one job at a time, because the GPU
is the bottleneck and everything else just waits its turn.
"""

from __future__ import annotations

import asyncio
import io
import json
import random
import time
import traceback
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import config
import downloader
import registry
import workflow
from comfy_client import ComfyClient, ComfyError
from fastapi import FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

STATIC = Path(__file__).parent / "static"
OUT = config.OUTPUT_DIR
THUMBS = OUT / ".thumbs"


@dataclass
class Job:
    id: str
    model_id: str
    prompt: str
    source_name: str
    tier: str
    length: int
    seed: int
    lightning: bool
    loras: list[registry.Lora]
    status: str = "queued"  # queued | running | done | error
    progress: float = 0.0
    message: str = ""
    output: str | None = None
    thumb: str | None = None
    width: int = 0
    height: int = 0
    created: float = field(default_factory=time.time)
    started: float | None = None
    finished: float | None = None

    def public(self) -> dict:
        model = registry.get(self.model_id)
        return {
            "id": self.id,
            "model": self.model_id,
            "model_label": model.label if model else self.model_id,
            "prompt": self.prompt,
            "source": self.source_name,
            "status": self.status,
            "progress": round(self.progress, 3),
            "message": self.message,
            "output": f"/outputs/{self.output}" if self.output else None,
            "thumb": f"/thumbs/{self.thumb}" if self.thumb else None,
            "tier": self.tier,
            "length": self.length,
            "seed": self.seed,
            "lightning": self.lightning,
            "loras": [f"{l.name}:{l.strength}" for l in self.loras],
            "size": f"{self.width}x{self.height}" if self.width else None,
            "elapsed": round((self.finished or time.time()) - (self.started or self.created), 1),
        }


app = FastAPI(title="wan-drop")
client = ComfyClient(config.COMFY_URL)
models = downloader.Manager(config.MODELS_DIR)
jobs: dict[str, Job] = {}
order: list[str] = []
queue: asyncio.Queue[tuple[str, bytes]] = asyncio.Queue()


@app.on_event("startup")
async def startup() -> None:
    for d in (OUT, THUMBS, config.INBOX_DIR):
        d.mkdir(parents=True, exist_ok=True)
    models.start()
    app.state.worker = asyncio.create_task(worker())


@app.on_event("shutdown")
async def shutdown() -> None:
    for task in (getattr(app.state, "worker", None), models.stop()):
        if task:
            task.cancel()


async def worker() -> None:
    """Serial job runner. Survives individual job failures."""
    await client.wait_until_ready()
    while True:
        job_id, image_bytes = await queue.get()
        job = jobs[job_id]
        try:
            job.status, job.started = "running", time.time()
            job.message = "準備中…"
            await run_job(job, image_bytes)
            job.status, job.progress, job.message = "done", 1.0, ""
        except (ComfyError, workflow.UnsupportedModel) as exc:
            job.status, job.message = "error", str(exc)
        except Exception as exc:  # noqa: BLE001 - never kill the worker
            job.status = "error"
            job.message = f"{type(exc).__name__}: {exc}"
            traceback.print_exc()
        finally:
            job.finished = time.time()
            queue.task_done()


async def run_job(job: Job, image_bytes: bytes) -> None:
    model = registry.get(job.model_id)
    if model is None:
        raise ComfyError(f"不認識的模型：{job.model_id}")

    state = models.model_status(model)
    if not state["installed"]:
        raise ComfyError(
            f"{model.label} 還沒下載完，缺少：" + ", ".join(state["missing"][:4])
        )

    params = config.params_for(model, lightning=job.lightning)
    params.length = job.length
    params.loras = [*params.loras, *job.loras]

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    job.width, job.height = workflow.fit_dimensions(*image.size, job.tier, model)

    thumb = image.copy()
    thumb.thumbnail((320, 320))
    job.thumb = f"{job.id}.jpg"
    thumb.save(THUMBS / job.thumb, "JPEG", quality=82)

    png = io.BytesIO()
    image.save(png, "PNG")
    uploaded = await client.upload_image(png.getvalue(), f"{job.id}.png")

    graph = workflow.build(
        model,
        params,
        image_name=uploaded,
        prompt=job.prompt,
        seed=job.seed,
        width=job.width,
        height=job.height,
        available_nodes=await client.node_classes(),
        filename_prefix=f"wan/{job.id}",
    )

    if problems := await client.validate(graph):
        raise ComfyError("工作流程與這台 ComfyUI 不相容：\n- " + "\n- ".join(problems))

    def progress(value: float) -> None:
        job.progress = value
        job.message = f"生成中 {value * 100:.0f}%"

    job.message = "載入模型…（第一次會比較久）"
    files = await client.run(graph, on_progress=progress)
    if not files:
        raise ComfyError("ComfyUI 沒有回傳任何輸出檔案")

    job.message = "下載結果…"
    data = await client.download(files[0])
    job.output = f"{job.id}{Path(files[0].filename).suffix or '.mp4'}"
    (OUT / job.output).write_bytes(data)


def submit(
    image_bytes: bytes,
    *,
    prompt: str,
    source: str,
    model: registry.ModelDef,
    tier: str,
    length: int,
    seed: int,
    lightning: bool,
    loras: list[registry.Lora],
) -> Job:
    job = Job(
        id=uuid.uuid4().hex[:12],
        model_id=model.id,
        prompt=prompt.strip(),
        source_name=source,
        tier=tier,
        length=workflow.normalize_length(length),
        seed=seed,
        lightning=lightning and bool(model.lightning),
        loras=loras,
    )
    jobs[job.id] = job
    order.append(job.id)
    queue.put_nowait((job.id, image_bytes))
    return job


# -- generation -------------------------------------------------------------


@app.post("/api/generate")
async def generate(
    image: UploadFile,
    prompt: str = Form(""),
    model: str = Form(""),
    tier: str = Form(""),
    length: int = Form(0),
    seed: int = Form(-1),
    lightning: str = Form(""),
    loras: str = Form(""),
) -> JSONResponse:
    data = await image.read()
    if not data:
        raise HTTPException(400, "圖片是空的")
    try:
        Image.open(io.BytesIO(data)).verify()
    except Exception:
        raise HTTPException(400, "無法辨識這個圖片格式")

    chosen = registry.get(model) if model else config.default_model()
    if chosen is None:
        raise HTTPException(400, f"不認識的模型：{model}")
    if not chosen.runnable:
        raise HTTPException(400, f"{chosen.label} 只提供檔案下載，不能從這裡生成")

    defaults = config.params_for(chosen)
    use_lightning = config.LIGHTNING if lightning == "" else lightning.lower() in ("1", "true", "on", "yes")

    picked: list[registry.Lora] = []
    if loras.strip() and chosen.supports_lora:
        try:
            for entry in json.loads(loras):
                picked.append(registry.Lora(entry["name"], float(entry.get("strength", 1.0))))
        except (ValueError, KeyError, TypeError):
            picked = config.parse_loras(loras)

    job = submit(
        data,
        prompt=prompt or config.PROMPT_DEFAULT,
        source=image.filename or "upload",
        model=chosen,
        tier=tier if tier in chosen.tiers else config.default_tier(chosen),
        length=length or defaults.length,
        seed=seed if seed >= 0 else random.randint(0, 2**31 - 1),
        lightning=use_lightning,
        loras=picked,
    )
    return JSONResponse(job.public())


@app.get("/api/jobs")
async def list_jobs(limit: int = 50) -> JSONResponse:
    return JSONResponse(
        {"jobs": [jobs[i].public() for i in reversed(order[-limit:])], "queued": queue.qsize()}
    )


@app.get("/api/jobs/{job_id}")
async def get_job(job_id: str) -> JSONResponse:
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(404, "找不到這個工作")
    return JSONResponse(job.public())


@app.post("/api/cancel")
async def cancel() -> JSONResponse:
    await client.interrupt()
    return JSONResponse({"ok": True})


# -- models -----------------------------------------------------------------


@app.get("/api/models")
async def list_models() -> JSONResponse:
    out = []
    for model in registry.MODELS:
        state = models.model_status(model)
        params = config.params_for(model)
        out.append(
            {
                "id": model.id,
                "label": model.label,
                "family": model.family,
                "runnable": model.runnable,
                "vram_gb": model.vram_gb,
                "download_bytes": model.download_bytes,
                "tiers": list(model.tiers),
                "default_tier": config.default_tier(model),
                "length": params.length,
                "fps": model.fps,
                "supports_lightning": bool(model.lightning),
                "supports_lora": model.supports_lora,
                "note": model.note,
                "sampling": {
                    "steps": params.steps,
                    "cfg": params.cfg,
                    "shift": params.shift,
                    "sampler": params.sampler,
                    "scheduler": params.scheduler,
                },
                **state,
            }
        )
    return JSONResponse({"models": out, "default": config.default_model().id})


@app.post("/api/models/{model_id}/download")
async def download_model(model_id: str) -> JSONResponse:
    model = registry.get(model_id)
    if model is None:
        raise HTTPException(404, f"不認識的模型：{model_id}")
    return JSONResponse(models.enqueue(model).public())


@app.get("/api/downloads")
async def downloads() -> JSONResponse:
    return JSONResponse(models.state())


@app.post("/api/downloads/cancel")
async def cancel_download() -> JSONResponse:
    return JSONResponse({"cancelled": models.cancel()})


@app.get("/api/loras")
async def list_loras() -> JSONResponse:
    return JSONResponse({"loras": models.list_loras(), "dir": str(config.MODELS_DIR / "loras")})


@app.get("/api/health")
async def health() -> JSONResponse:
    try:
        classes = await client.node_classes()
        comfy_ok, detail = True, f"{len(classes)} node types"
    except Exception as exc:  # noqa: BLE001
        comfy_ok, detail = False, str(exc)
    installed = [m.id for m in registry.MODELS if models.model_status(m)["installed"]]
    return JSONResponse(
        {
            "comfy": {"url": config.COMFY_URL, "ok": comfy_ok, "detail": detail},
            "models_dir": str(config.MODELS_DIR),
            "installed": installed,
            "default_model": config.default_model().id,
            "lightning_default": config.LIGHTNING,
        }
    )


# -- files ------------------------------------------------------------------


def _serve(folder: Path, name: str) -> FileResponse:
    path = (folder / name).resolve()
    if not path.is_file() or folder.resolve() not in path.parents:
        raise HTTPException(404, "沒有這個檔案")
    return FileResponse(path)


@app.get("/outputs/{name}")
async def output(name: str) -> FileResponse:
    return _serve(OUT, name)


@app.get("/thumbs/{name}")
async def thumb(name: str) -> FileResponse:
    return _serve(THUMBS, name)


app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/")
async def index() -> HTMLResponse:
    return HTMLResponse((STATIC / "index.html").read_text(encoding="utf-8"))

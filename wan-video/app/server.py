"""Drop an image, type an instruction, get a short animation.

A single-worker queue in front of ComfyUI. One job runs at a time because the
GPU is the bottleneck; everything else just waits its turn.
"""

from __future__ import annotations

import asyncio
import io
import random
import time
import traceback
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import config
import workflow
from comfy_client import ComfyClient, ComfyError
from fastapi import FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

STATIC = Path(__file__).parent / "static"


@dataclass
class Job:
    id: str
    prompt: str
    source_name: str
    tier: str
    length: int
    seed: int
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
        return {
            "id": self.id,
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
            "size": f"{self.width}x{self.height}" if self.width else None,
            "elapsed": round((self.finished or time.time()) - (self.started or self.created), 1),
        }


app = FastAPI(title="wan-drop")
client = ComfyClient(config.COMFY_URL)
jobs: dict[str, Job] = {}
order: list[str] = []
queue: asyncio.Queue[tuple[str, bytes]] = asyncio.Queue()

OUT = config.OUTPUT_DIR
THUMBS = OUT / ".thumbs"


@app.on_event("startup")
async def startup() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    THUMBS.mkdir(parents=True, exist_ok=True)
    config.INBOX_DIR.mkdir(parents=True, exist_ok=True)
    app.state.worker = asyncio.create_task(worker())


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
            job.status, job.progress = "done", 1.0
            job.message = ""
        except ComfyError as exc:
            job.status, job.message = "error", str(exc)
        except Exception as exc:  # noqa: BLE001 - never kill the worker
            job.status = "error"
            job.message = f"{type(exc).__name__}: {exc}"
            traceback.print_exc()
        finally:
            job.finished = time.time()
            queue.task_done()


async def run_job(job: Job, image_bytes: bytes) -> None:
    settings = config.settings()
    settings.tier = job.tier
    settings.length = job.length

    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGB")
    job.width, job.height = workflow.fit_dimensions(*image.size, job.tier)

    # Save a thumbnail so the UI can show what was submitted.
    thumb = image.copy()
    thumb.thumbnail((320, 320))
    job.thumb = f"{job.id}.jpg"
    thumb.save(THUMBS / job.thumb, "JPEG", quality=82)

    png = io.BytesIO()
    image.save(png, "PNG")
    uploaded = await client.upload_image(png.getvalue(), f"{job.id}.png")

    graph = workflow.build(
        image_name=uploaded,
        prompt=job.prompt,
        negative=workflow.DEFAULT_NEGATIVE,
        seed=job.seed,
        width=job.width,
        height=job.height,
        settings=settings,
        available_nodes=await client.node_classes(),
        filename_prefix=f"wan/{job.id}",
    )

    if problems := await client.validate(graph):
        raise ComfyError("工作流程與這台 ComfyUI 不相容:\n- " + "\n- ".join(problems))

    def progress(value: float) -> None:
        job.progress = value
        job.message = f"生成中 {value * 100:.0f}%"

    job.message = "載入模型…（第一次會比較久）"
    files = await client.run(graph, on_progress=progress)
    if not files:
        raise ComfyError("ComfyUI 沒有回傳任何輸出檔案")

    job.message = "下載結果…"
    data = await client.download(files[0])
    suffix = Path(files[0].filename).suffix or ".mp4"
    job.output = f"{job.id}{suffix}"
    (OUT / job.output).write_bytes(data)


def submit(image_bytes: bytes, prompt: str, source: str, tier: str, length: int, seed: int) -> Job:
    job = Job(
        id=uuid.uuid4().hex[:12],
        prompt=prompt.strip(),
        source_name=source,
        tier=tier,
        length=workflow.normalize_length(length),
        seed=seed,
    )
    jobs[job.id] = job
    order.append(job.id)
    queue.put_nowait((job.id, image_bytes))
    return job


# -- API --------------------------------------------------------------------


@app.post("/api/generate")
async def generate(
    image: UploadFile,
    prompt: str = Form(""),
    tier: str = Form(""),
    length: int = Form(0),
    seed: int = Form(-1),
) -> JSONResponse:
    data = await image.read()
    if not data:
        raise HTTPException(400, "圖片是空的")
    try:
        Image.open(io.BytesIO(data)).verify()
    except Exception:
        raise HTTPException(400, "無法辨識這個圖片格式")

    defaults = config.settings()
    job = submit(
        data,
        prompt or "subtle natural motion, cinematic",
        image.filename or "upload",
        tier if tier in workflow.TIERS else defaults.tier,
        length or defaults.length,
        seed if seed >= 0 else random.randint(0, 2**31 - 1),
    )
    return JSONResponse(job.public())


@app.get("/api/jobs")
async def list_jobs(limit: int = 50) -> JSONResponse:
    recent = [jobs[i].public() for i in reversed(order[-limit:])]
    return JSONResponse({"jobs": recent, "queued": queue.qsize()})


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


@app.get("/api/health")
async def health() -> JSONResponse:
    s = config.settings().resolved()
    try:
        classes = await client.node_classes()
        comfy_ok, detail = True, f"{len(classes)} node types"
    except Exception as exc:  # noqa: BLE001
        comfy_ok, detail = False, str(exc)
    return JSONResponse(
        {
            "comfy": {"url": config.COMFY_URL, "ok": comfy_ok, "detail": detail},
            "profile": config.PROFILE,
            "model": {"high": s.high_noise, "low": s.low_noise, "loader": s.loader},
            "sampling": {
                "lightning": s.lightning,
                "steps": s.steps,
                "boundary": s.boundary,
                "cfg": s.cfg,
                "shift": s.shift,
            },
            "loras": [f"{l.name}:{l.strength}" for l in s.loras],
            "defaults": {"tier": s.tier, "length": s.length, "fps": s.fps},
        }
    )


@app.get("/outputs/{name}")
async def output(name: str) -> FileResponse:
    path = (OUT / name).resolve()
    if not path.is_file() or OUT.resolve() not in path.parents:
        raise HTTPException(404, "沒有這個檔案")
    return FileResponse(path)


@app.get("/thumbs/{name}")
async def thumb(name: str) -> FileResponse:
    path = (THUMBS / name).resolve()
    if not path.is_file() or THUMBS.resolve() not in path.parents:
        raise HTTPException(404, "沒有這個檔案")
    return FileResponse(path)


app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/")
async def index() -> HTMLResponse:
    return HTMLResponse((STATIC / "index.html").read_text(encoding="utf-8"))

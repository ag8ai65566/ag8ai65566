"""Drop an image, pick a model, type an instruction, get a short animation.

A single-worker queue in front of ComfyUI: one job at a time, because the GPU
is the bottleneck and everything else just waits its turn.

On VRAM: the per-model numbers are a *recommendation*, not a gate. Nothing here
refuses a job because a card looks small - ComfyUI swaps weights out to system
RAM and runs slower instead. The UI says how much headroom you have and offers
the flags that make a tight fit work; the choice is the user's.
"""

from __future__ import annotations

import asyncio
import io
import json
import random
import time
import traceback
import uuid
from pathlib import Path

import civitai
import config
import images
import downloader
import library
import registry
import workflow
from comfy_client import ComfyClient, ComfyError
from fastapi import Body, FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

STATIC = Path(__file__).parent / "static"

app = FastAPI(title="wan-drop")
client = ComfyClient(config.COMFY_URL)
models = downloader.Manager(config.MODELS_DIR)
lib = library.Library(config.OUTPUT_DIR)
queue: asyncio.Queue[tuple[str, bytes]] = asyncio.Queue()
running: set[str] = set()


def public(record: library.Record) -> dict:
    model = registry.get(record.model_id)
    progress = getattr(record, "_progress", 0.0)
    return {
        "id": record.id,
        "model": record.model_id,
        "model_label": model.label if model else record.model_id,
        "prompt": record.prompt,
        "negative": record.negative,
        "source": record.source_name,
        "status": record.status,
        "progress": round(progress, 3),
        "message": record.message,
        "kind": record.kind,
        "output": f"/outputs/{record.output}" if record.output else None,
        "outputs": [f"/outputs/{o}" for o in record.outputs],
        "fps": record.fps,
        "duration": round(record.length / record.fps, 2) if record.fps and record.length else 0,
        "settings": record.settings,
        "thumb": f"/thumbs/{record.thumb}" if record.thumb else None,
        "tier": record.tier,
        "length": record.length,
        "seed": record.seed,
        "lightning": record.lightning,
        "loras": record.loras,
        "starred": record.starred,
        "size": f"{record.width}x{record.height}" if record.width else None,
        "created": record.created,
        "elapsed": round((record.finished or time.time()) - (record.started or record.created), 1),
    }


@app.on_event("startup")
async def startup() -> None:
    for d in (config.OUTPUT_DIR, lib.thumbs, config.INBOX_DIR):
        d.mkdir(parents=True, exist_ok=True)
    lib.load()
    models.start()
    app.state.worker = asyncio.create_task(worker())


@app.on_event("shutdown")
async def shutdown() -> None:
    lib.save()
    for task in (getattr(app.state, "worker", None), models.stop()):
        if task:
            task.cancel()


async def worker() -> None:
    """Serial job runner. Survives individual job failures."""
    await client.wait_until_ready()
    while True:
        job_id, image_bytes = await queue.get()
        record = lib.get(job_id)
        if record is None:
            queue.task_done()
            continue
        running.add(job_id)
        try:
            record.status, record.started = "running", time.time()
            record.message = "準備中…"
            await run_job(record, image_bytes)
            record.status, record.message = "done", ""
            record._progress = 1.0
        except (ComfyError, workflow.UnsupportedModel) as exc:
            record.status, record.message = "error", str(exc)
        except Exception as exc:  # noqa: BLE001 - never kill the worker
            record.status = "error"
            record.message = f"{type(exc).__name__}: {exc}"
            traceback.print_exc()
        finally:
            record.finished = time.time()
            running.discard(job_id)
            lib.save()
            queue.task_done()


async def run_job(record: library.Record, image_bytes: bytes) -> None:
    if record.kind == "image":
        return await run_image_job(record)
    model = registry.get(record.model_id)
    if model is None:
        raise ComfyError(f"不認識的模型：{record.model_id}")
    if reason := missing_reason(model):
        raise ComfyError(reason)

    params = config.params_for(model, lightning=record.lightning)
    params.length = record.length
    params.loras = [*params.loras, *config.parse_loras(",".join(record.loras))]
    record.fps = params.fps
    record.settings = {
        "steps": params.steps, "cfg": params.cfg, "shift": params.shift,
        "sampler": params.sampler, "scheduler": params.scheduler,
    }

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    record.width, record.height = workflow.fit_dimensions(*image.size, record.tier, model)

    thumb = image.copy()
    thumb.thumbnail((360, 360))
    record.thumb = f"{record.id}.jpg"
    thumb.save(lib.thumbs / record.thumb, "JPEG", quality=82)

    png = io.BytesIO()
    image.save(png, "PNG")
    uploaded = await client.upload_image(png.getvalue(), f"{record.id}.png")

    graph = workflow.build(
        model,
        params,
        image_name=uploaded,
        prompt=record.prompt,
        negative=record.negative or None,
        seed=record.seed,
        width=record.width,
        height=record.height,
        available_nodes=await client.node_classes(),
        filename_prefix=f"wan/{record.id}",
    )
    if problems := await client.validate(graph):
        raise ComfyError("工作流程與這台 ComfyUI 不相容：\n- " + "\n- ".join(problems))

    def progress(value: float) -> None:
        record._progress = value
        record.message = f"生成中 {value * 100:.0f}%"

    record.message = "載入模型…（第一次會比較久）"
    files = await client.run(graph, on_progress=progress)
    if not files:
        raise ComfyError("ComfyUI 沒有回傳任何輸出檔案")

    record.message = "下載結果…"
    record.outputs = []
    for index, f in enumerate(files):
        data = await client.download(f)
        suffix = Path(f.filename).suffix or (".png" if record.kind == "image" else ".mp4")
        name = f"{record.id}{'' if index == 0 else f'-{index + 1}'}{suffix}"
        (config.OUTPUT_DIR / name).write_bytes(data)
        record.outputs.append(name)
    record.output = record.outputs[0]


# -- model availability ------------------------------------------------------


def effective_default() -> registry.ModelDef:
    """The model the UI preselects: the configured one only if installed."""
    configured = config.default_model()
    if models.model_status(configured)["installed"]:
        return configured
    for model in registry.runnable():
        if models.model_status(model)["installed"]:
            return model
    return configured


def missing_reason(model: registry.ModelDef) -> str | None:
    state = models.model_status(model)
    if state["installed"]:
        return None
    missing = ", ".join(state["missing"][:3])
    more = " 等" if len(state["missing"]) > 3 else ""
    return (
        f"{model.label} 還沒下載完（缺 {len(state['missing'])} 個檔："
        f"{missing}{more}）。請到「模型」分頁下載，或改選已安裝的模型。"
    )


async def gpu_info() -> dict:
    """Real VRAM, straight from ComfyUI, so advice is based on the actual card."""
    try:
        stats = await client.system_stats()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "detail": str(exc), "devices": []}
    devices = [
        {
            "name": d.get("name", "?"),
            "type": d.get("type", "?"),
            "vram_total": d.get("vram_total") or 0,
            "vram_free": d.get("vram_free") or 0,
        }
        for d in (stats.get("devices") or [])
    ]
    gpus = [d for d in devices if d["type"] == "cuda"] or devices
    total = max((d["vram_total"] for d in gpus), default=0)
    return {
        "ok": True,
        "devices": devices,
        "vram_total": total,
        "vram_gb": round(total / 1024**3, 1) if total else 0,
        "ram_total": (stats.get("system") or {}).get("ram_total") or 0,
        "comfy_version": (stats.get("system") or {}).get("comfyui_version", ""),
    }


def vram_advice_generic(need_gb: int, vram_gb: float) -> dict:
    """Advisory only, for any model kind. Never used to block a job."""
    note = (f"建議 {need_gb}GB 顯存。低於這個數字仍然跑得動 —— "
            "ComfyUI 會把權重換到系統記憶體，只是慢很多。")
    if not vram_gb:
        return {"level": "unknown", "text": note, "flags": ""}
    if vram_gb + 0.5 >= need_gb:
        return {"level": "ok", "text": f"你的 {vram_gb}GB 夠跑這個模型。", "flags": ""}
    ratio = vram_gb / need_gb
    flags = "--lowvram" if ratio >= 0.45 else "--novram"
    how_slow = "慢 2～4 倍" if ratio >= 0.45 else "慢 5 倍以上"
    return {
        "level": "tight" if ratio >= 0.45 else "very_tight",
        "text": (f"這個模型建議 {need_gb}GB，你有 {vram_gb}GB。"
                 f"**還是跑得動** —— ComfyUI 會把權重換到系統記憶體，大約{how_slow}。"
                 f"建議在 .env 加 COMFY_ARGS={flags} 再重啟。"),
        "flags": flags,
    }


def vram_advice(model: registry.ModelDef, vram_gb: float) -> dict:
    """Advisory only. Never used to block a job."""
    if not vram_gb:
        return {"level": "unknown", "text": model.vram_note, "flags": ""}
    if vram_gb + 0.5 >= model.vram_gb:
        return {"level": "ok", "text": f"你的 {vram_gb}GB 夠跑這個模型。", "flags": ""}
    ratio = vram_gb / model.vram_gb
    flags = "--lowvram" if ratio >= 0.45 else "--novram"
    how_slow = "慢 2～4 倍" if ratio >= 0.45 else "慢 5 倍以上"
    return {
        "level": "tight" if ratio >= 0.45 else "very_tight",
        "text": (
            f"這個模型建議 {model.vram_gb}GB，你有 {vram_gb}GB。"
            f"**還是跑得動** —— ComfyUI 會把權重換到系統記憶體，大約{how_slow}。"
            f"建議在 .env 加 COMFY_ARGS={flags} 再重啟。"
        ),
        "flags": flags,
    }


# -- generation --------------------------------------------------------------


def submit(
    image_bytes: bytes,
    *,
    prompt: str,
    negative: str,
    source: str,
    model: registry.ModelDef,
    tier: str,
    length: int,
    seed: int,
    lightning: bool,
    loras: list[str],
) -> library.Record:
    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=model.id,
        prompt=prompt.strip(),
        negative=negative.strip(),
        source_name=source,
        tier=tier,
        length=workflow.normalize_length(length),
        seed=seed,
        lightning=lightning and bool(model.lightning),
        loras=loras,
    )
    lib.add(record)
    queue.put_nowait((record.id, image_bytes))
    return record


@app.post("/api/generate")
async def generate(
    image: UploadFile,
    prompt: str = Form(""),
    negative: str = Form(""),
    model: str = Form(""),
    tier: str = Form(""),
    length: int = Form(0),
    seconds: float = Form(0.0),
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

    chosen = registry.get(model) if model else effective_default()
    if chosen is None:
        raise HTTPException(400, f"不認識的模型：{model}")
    if not chosen.runnable:
        raise HTTPException(400, f"{chosen.label} 只提供檔案下載，不能從這裡生成")
    if reason := missing_reason(chosen):
        raise HTTPException(400, reason)

    defaults = config.params_for(chosen)
    use_lightning = config.LIGHTNING if lightning == "" else lightning.lower() in ("1", "true", "on", "yes")

    picked: list[str] = []
    if loras.strip() and chosen.supports_lora:
        try:
            for entry in json.loads(loras):
                picked.append(f"{entry['name']}:{float(entry.get('strength', 1.0))}")
        except (ValueError, KeyError, TypeError):
            picked = [chunk.strip() for chunk in loras.split(",") if chunk.strip()]

    record = submit(
        data,
        prompt=prompt or config.PROMPT_DEFAULT,
        negative=negative,
        source=image.filename or "upload",
        model=chosen,
        tier=tier if tier in chosen.tiers else config.default_tier(chosen),
        length=(workflow.frames_for_seconds(seconds, chosen.fps) if seconds > 0
                else (length or defaults.length)),
        seed=seed if seed >= 0 else random.randint(0, 2**31 - 1),
        lightning=use_lightning,
        loras=picked,
    )
    return JSONResponse(public(record))


@app.get("/api/jobs")
async def list_jobs(limit: int = 60, kind: str = "") -> JSONResponse:
    return JSONResponse(
        {"jobs": [public(r) for r in lib.recent(limit, kind)], "queued": queue.qsize()}
    )


@app.get("/api/jobs/{job_id}")
async def get_job(job_id: str) -> JSONResponse:
    record = lib.get(job_id)
    if record is None:
        raise HTTPException(404, "找不到這個工作")
    return JSONResponse(public(record))


@app.delete("/api/jobs/{job_id}")
async def delete_job(job_id: str) -> JSONResponse:
    if job_id in running:
        raise HTTPException(409, "這個工作正在跑，先按「中斷」再刪")
    if not lib.delete(job_id):
        raise HTTPException(404, "找不到這個工作")
    return JSONResponse({"deleted": job_id})


@app.post("/api/jobs/{job_id}/star")
async def star_job(job_id: str, value: bool = Body(True, embed=True)) -> JSONResponse:
    if not lib.star(job_id, value):
        raise HTTPException(404, "找不到這個工作")
    return JSONResponse({"id": job_id, "starred": value})


@app.post("/api/library/clear")
async def clear_library(keep_starred: bool = Body(True, embed=True)) -> JSONResponse:
    if running:
        raise HTTPException(409, "還有工作在跑，等它跑完或按「中斷」")
    return JSONResponse({"removed": lib.clear(keep_starred=keep_starred)})


@app.post("/api/library/sweep")
async def sweep_library() -> JSONResponse:
    return JSONResponse({"removed": lib.sweep_orphans()})


@app.get("/api/library/stats")
async def library_stats() -> JSONResponse:
    return JSONResponse(lib.stats())


@app.post("/api/cancel")
async def cancel() -> JSONResponse:
    await client.interrupt()
    return JSONResponse({"ok": True})


# -- models ------------------------------------------------------------------


@app.get("/api/models")
async def list_models() -> JSONResponse:
    gpu = await gpu_info()
    vram = gpu.get("vram_gb") or 0
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
                "vram_note": model.vram_note,
                "vram_advice": vram_advice(model, vram),
                "download_bytes": model.download_bytes,
                "tiers": list(model.tiers),
                "default_tier": config.default_tier(model),
                "length": params.length,
                "fps": model.fps,
                "negative": model.negative,
                "supports_lightning": bool(model.lightning),
                "supports_lora": model.supports_lora,
                "civitai_bases": list(model.civitai_bases),
                "civitai_bases_loose": list(model.civitai_bases_loose),
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
    return JSONResponse(
        {
            "models": out,
            "default": effective_default().id,
            "configured_default": config.default_model().id,
            "models_dir": str(config.MODELS_DIR),
            "gpu": gpu,
        }
    )


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


# -- LoRAs -------------------------------------------------------------------


@app.get("/api/loras")
async def list_loras() -> JSONResponse:
    return JSONResponse(
        {
            "loras": models.list_loras(),
            "dir": str(config.MODELS_DIR / "loras"),
            "civitai_key": bool(civitai.api_key()),
        }
    )


@app.delete("/api/loras/{name}")
async def delete_lora(name: str) -> JSONResponse:
    try:
        if not models.delete_lora(name):
            raise HTTPException(404, f"找不到 {name}")
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    return JSONResponse({"deleted": name})


@app.get("/api/civitai/search")
async def civitai_search(
    query: str = "",
    model: str = "",
    image_model: str = "",
    types: str = "LORA",
    scope: str = "strict",
    nsfw: str = "",
    sort: str = "Most Downloaded",
    period: str = "AllTime",
    cursor: str = "",
    limit: int = 24,
) -> JSONResponse:
    bases: list[str] = []
    if image_model:
        # Image side: SDXL-family bases for the selected checkpoint.
        if scope != "all":
            bases = list(images.CIVITAI_BASES.get(image_model, ()))
            if scope == "loose" or not bases:
                bases = list(images.CIVITAI_BASES_LOOSE)
    else:
        chosen = registry.get(model) if model else None
        if chosen and scope != "all":
            bases = list(chosen.civitai_bases)
            if scope == "loose":
                bases += list(chosen.civitai_bases_loose)
            if not bases and scope == "strict":
                # No exact base exists for this model (HunyuanVideo 1.5); fall
                # back so the search returns something rather than nothing.
                bases = list(chosen.civitai_bases_loose)
    want_nsfw = None if nsfw == "" else nsfw.lower() in ("1", "true", "yes", "on")
    try:
        result = await civitai.search(
            query=query, base_models=bases, nsfw=want_nsfw,
            sort=sort, period=period, cursor=cursor, limit=limit, types=types,
        )
    except civitai.CivitaiError as exc:
        raise HTTPException(502, str(exc))
    result["bases_used"] = bases
    installed = {l["name"] for l in models.list_loras()}
    ckpt_dir = config.MODELS_DIR / "checkpoints"
    if ckpt_dir.is_dir():
        installed |= {p.name for p in ckpt_dir.glob("*.safetensors")}
    for item in result["items"]:
        for version in item["versions"]:
            for f in version["files"]:
                f["installed"] = f["name"] in installed
    return JSONResponse(result)


@app.post("/api/civitai/download")
async def civitai_download(payload: dict = Body(...)) -> JSONResponse:
    files = payload.get("files") or []
    if not files:
        raise HTTPException(400, "沒有指定要下載的檔案")
    try:
        headers = tuple(civitai.download_headers().items())
    except civitai.NeedsApiKey as exc:
        raise HTTPException(400, str(exc))

    folder = "checkpoints" if payload.get("kind") == "checkpoint" else "loras"
    remote = []
    for f in files:
        url, name = f.get("url"), f.get("name")
        if not url or not name:
            raise HTTPException(400, "檔案缺少 url 或 name")
        if "/" in name or "\\" in name:
            raise HTTPException(400, f"不合法的檔名：{name}")
        remote.append(
            downloader.RemoteFile(
                url=url, folder=folder, name=name,
                size=int(f.get("size") or 0), headers=headers,
            )
        )

    label = payload.get("label") or remote[0].name
    meta = {
        "url": payload.get("page_url", ""),
        "trained_words": payload.get("trained_words") or [],
        "base_model": payload.get("base_model", ""),
        "name": label,
    }
    download = models.enqueue_files(
        key=f"civitai:{payload.get('version_id') or remote[0].name}",
        label=f"LoRA · {label}",
        files=remote,
        sidecars={f.name: meta for f in remote},
    )
    return JSONResponse(download.public())


@app.get("/api/civitai/status")
async def civitai_status() -> JSONResponse:
    return JSONResponse(
        {
            "has_key": bool(civitai.api_key()),
            "sorts": civitai.SORTS,
            "periods": civitai.PERIODS,
            "help": (
                "搜尋不用 API key，下載需要。到 civitai.com → 右上頭像 → "
                "Account settings → API Keys 產生一個，填進 .env 的 "
                "CIVITAI_API_KEY=，然後重啟 app。"
            ),
        }
    )


# -- text to image -----------------------------------------------------------


def image_status(model: images.ImageModel) -> dict:
    states = [models.file_status(f) for f in model.all_files]
    on_disk = sum(n for _, n in states)
    missing = [f.name for f, (st, _) in zip(model.all_files, states) if st != "ok"]
    return {
        "installed": not missing,
        "partial": bool(missing) and on_disk > 0,
        "bytes_on_disk": on_disk,
        "missing": missing,
    }


async def run_image_job(record: library.Record) -> None:
    model = images.get(record.model_id)
    if model is None:
        raise ComfyError(f"不認識的圖片模型：{record.model_id}")
    state = image_status(model)
    if not state["installed"]:
        raise ComfyError(
            f"{model.label} 還沒下載完（缺 {', '.join(state['missing'][:3])}）。"
            "請到「模型」分頁下載。"
        )

    cfg = record.settings
    graph = images.build(
        model,
        prompt=record.prompt,
        negative=record.negative,
        seed=record.seed,
        width=record.width,
        height=record.height,
        batch=cfg.get("batch", 1),
        steps=cfg.get("steps"),
        cfg=cfg.get("cfg"),
        sampler=cfg.get("sampler"),
        scheduler=cfg.get("scheduler"),
        clip_skip=cfg.get("clip_skip"),
        loras=[(n, s) for n, s in cfg.get("loras", [])],
        hires_scale=cfg.get("hires_scale", 0.0),
        hires_denoise=cfg.get("hires_denoise", 0.45),
        available_nodes=await client.node_classes(),
        filename_prefix=f"img/{record.id}",
    )
    if problems := await client.validate(graph):
        raise ComfyError("工作流程與這台 ComfyUI 不相容：\n- " + "\n- ".join(problems))

    def progress(value: float) -> None:
        record._progress = value
        record.message = f"生成中 {value * 100:.0f}%"

    record.message = "載入模型…（第一次會比較久）"
    files = await client.run(graph, on_progress=progress)
    if not files:
        raise ComfyError("ComfyUI 沒有回傳任何輸出檔案")

    record.message = "下載結果…"
    record.outputs = []
    for index, f in enumerate(files):
        data = await client.download(f)
        name = f"{record.id}{'' if index == 0 else f'-{index + 1}'}{Path(f.filename).suffix or '.png'}"
        (config.OUTPUT_DIR / name).write_bytes(data)
        record.outputs.append(name)
    record.output = record.outputs[0]

    # A thumbnail keeps the gallery light even with a big batch of PNGs.
    try:
        thumb = Image.open(config.OUTPUT_DIR / record.output).convert("RGB")
        thumb.thumbnail((420, 420))
        record.thumb = f"{record.id}.jpg"
        thumb.save(lib.thumbs / record.thumb, "JPEG", quality=84)
    except Exception:  # noqa: BLE001 - a missing thumbnail is not a failure
        pass


@app.get("/api/image/models")
async def image_models() -> JSONResponse:
    gpu = await gpu_info()
    vram = gpu.get("vram_gb") or 0
    try:
        info = await client.object_info()
        samplers = (info.get("KSampler", {}).get("input", {})
                    .get("required", {}).get("sampler_name", [[]])[0])
        schedulers = (info.get("KSampler", {}).get("input", {})
                      .get("required", {}).get("scheduler", [[]])[0])
        extra = sorted(
            f.name for f in (config.MODELS_DIR / "checkpoints").glob("*.safetensors")
        ) if (config.MODELS_DIR / "checkpoints").is_dir() else []
    except Exception:  # noqa: BLE001
        samplers, schedulers, extra = [], [], []

    known = {m.file.name for m in images.IMAGE_MODELS}
    out = []
    for model in images.IMAGE_MODELS:
        state = image_status(model)
        out.append(
            {
                "id": model.id,
                "label": model.label,
                "vram_gb": model.vram_gb,
                "vram_advice": vram_advice_generic(model.vram_gb, vram),
                "download_bytes": model.download_bytes,
                "steps": model.steps,
                "cfg": model.cfg,
                "sampler": model.sampler,
                "scheduler": model.scheduler,
                "clip_skip": model.clip_skip,
                "positive_prefix": model.positive_prefix,
                "negative": model.negative,
                "prompt_style": model.prompt_style,
                "sizes": {k: list(v) for k, v in model.sizes.items()},
                "default_size": model.default_size,
                "nsfw_note": model.nsfw_note,
                "note": model.note,
                "civitai_bases": list(images.CIVITAI_BASES.get(model.id, ())),
                **state,
            }
        )
    return JSONResponse(
        {
            "models": out,
            "help": images.HELP,
            "samplers": samplers,
            "schedulers": schedulers,
            "loose_bases": list(images.CIVITAI_BASES_LOOSE),
            "other_checkpoints": [n for n in extra if n not in known],
            "gpu": gpu,
        }
    )


@app.post("/api/image/models/{model_id}/download")
async def download_image_model(model_id: str) -> JSONResponse:
    model = images.get(model_id)
    if model is None:
        raise HTTPException(404, f"不認識的圖片模型：{model_id}")
    remote = [
        downloader.RemoteFile(
            url=downloader.url_for(f), folder=f.folder, name=f.name, size=f.size
        )
        for f in model.all_files
    ]
    return JSONResponse(
        models.enqueue_files(
            key=f"image:{model.id}", label=model.label, files=remote, kind="model"
        ).public()
    )


@app.post("/api/image/generate")
async def image_generate(payload: dict = Body(...)) -> JSONResponse:
    model = images.get(str(payload.get("model", "")))
    if model is None:
        raise HTTPException(400, f"不認識的圖片模型：{payload.get('model')}")
    state = image_status(model)
    if not state["installed"]:
        raise HTTPException(
            400,
            f"{model.label} 還沒下載完（缺 {', '.join(state['missing'][:3])}）。"
            "請到「模型」分頁下載，或改選已安裝的。",
        )

    prompt = str(payload.get("prompt", "")).strip()
    if not prompt:
        raise HTTPException(400, "提詞是空的 —— 圖片生成沒有輸入圖，全靠提詞")
    if payload.get("use_prefix", True) and model.positive_prefix:
        prompt = f"{model.positive_prefix}, {prompt}"

    size_name = str(payload.get("size") or model.default_size)
    width, height = model.sizes.get(size_name, (1024, 1024))
    batch = max(1, min(int(payload.get("batch", 1)), 16))
    seed = int(payload.get("seed", -1))

    picked: list[tuple[str, float]] = []
    for entry in payload.get("loras") or []:
        name = str(entry.get("name", ""))
        if "/" in name or "\\" in name or not name:
            raise HTTPException(400, f"不合法的 LoRA 檔名：{name}")
        picked.append((name, float(entry.get("strength", 0.8))))

    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=model.id,
        kind="image",
        prompt=prompt,
        negative=str(payload.get("negative") or model.negative),
        seed=seed if seed >= 0 else random.randint(0, 2**31 - 1),
        width=width,
        height=height,
        tier=size_name,
        length=batch,
        loras=[f"{n}:{s}" for n, s in picked],
        settings={
            "batch": batch,
            "steps": int(payload.get("steps") or model.steps),
            "cfg": float(payload.get("cfg") or model.cfg),
            "sampler": str(payload.get("sampler") or model.sampler),
            "scheduler": str(payload.get("scheduler") or model.scheduler),
            "clip_skip": int(payload.get("clip_skip") or model.clip_skip),
            "hires_scale": float(payload.get("hires_scale") or 0.0),
            "hires_denoise": float(payload.get("hires_denoise") or 0.45),
            "loras": picked,
        },
    )
    lib.add(record)
    queue.put_nowait((record.id, b""))
    return JSONResponse(public(record))


# -- health & files ----------------------------------------------------------


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
            "default_model": effective_default().id,
            "lightning_default": config.LIGHTNING,
            "gpu": await gpu_info(),
            "library": lib.stats(),
            "civitai_key": bool(civitai.api_key()),
            "comfy_args": config.COMFY_ARGS,
        }
    )


def _serve(folder: Path, name: str) -> FileResponse:
    path = (folder / name).resolve()
    if not path.is_file() or folder.resolve() not in path.parents:
        raise HTTPException(404, "沒有這個檔案")
    return FileResponse(path)


@app.get("/outputs/{name}")
async def output(name: str) -> FileResponse:
    return _serve(config.OUTPUT_DIR, name)


@app.get("/thumbs/{name}")
async def thumb(name: str) -> FileResponse:
    return _serve(lib.thumbs, name)


app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/")
async def index() -> HTMLResponse:
    return HTMLResponse((STATIC / "index.html").read_text(encoding="utf-8"))

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
import comics
import config
import images
import downloader
import library
import prompts
import registry
import updates
import upscalers
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
lib = library.Library(config.OUTPUT_DIR, config.INBOX_DIR)
queue: asyncio.Queue[tuple[str, bytes]] = asyncio.Queue()
running: set[str] = set()


def model_label(record: library.Record) -> str:
    """Records span two catalogues; look in the right one."""
    if record.kind in ("image", "comic"):
        model = images.resolve(record.model_id)
        return model.label if model else record.model_id
    model = registry.get(record.model_id)
    return model.label if model else record.model_id


def public(record: library.Record) -> dict:
    progress = getattr(record, "_progress", 0.0)
    return {
        "id": record.id,
        "model": record.model_id,
        "model_label": model_label(record),
        "prompt": record.prompt,
        # The prompt as typed, before any auto prefix - so "run again" does not
        # prepend Pony's score tags a second time.
        "prompt_raw": record.prompt_raw or record.prompt,
        "negative": record.negative,
        "negative_custom": record.negative_custom,
        "source": record.source_name,
        "status": record.status,
        "progress": round(progress, 3),
        "message": record.message,
        "kind": record.kind,
        "output": f"/outputs/{record.output}" if record.output else None,
        "outputs": [f"/outputs/{o}" for o in record.outputs],
        "fps": record.fps,
        # Interpolation raises the playback rate without changing the duration,
        # so both numbers are reported rather than one standing in for the other.
        "out_fps": (record.settings or {}).get("out_fps") or record.fps,
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
    # A finished download changes what ComfyUI can offer, and its /object_info
    # is cached; drop that cache or the new model looks uninstalled.
    models.on_change = client.invalidate
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
    if record.kind in ("image", "comic"):
        return await run_image_job(record)
    model = registry.get(record.model_id)
    if model is None:
        raise ComfyError(f"不認識的模型：{record.model_id}")
    if reason := missing_reason(model):
        raise ComfyError(reason)

    params = config.params_for(model, lightning=record.lightning)
    params.length = record.length
    params.loras = [*params.loras, *config.parse_loras(",".join(record.loras))]
    extra = record.settings or {}
    params.interpolate = int(extra.get("interpolate") or 1)
    params.interpolate_model = str(extra.get("interpolate_model") or "")
    params.upscaler = str(extra.get("upscaler") or "")
    if params.interpolate > 1 and not params.interpolate_model:
        params.interpolate = 1
    record.fps = params.fps
    record.settings = {
        "steps": params.steps, "cfg": params.cfg, "shift": params.shift,
        "sampler": params.sampler, "scheduler": params.scheduler,
        "interpolate": params.interpolate, "interpolate_model": params.interpolate_model,
        "upscaler": params.upscaler,
        # What the file will actually play at, once interpolation is counted.
        "out_fps": params.fps * max(1, params.interpolate),
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
        # "" is a deliberate "no negative prompt"; only an unset one falls back.
        negative=record.negative if record.negative_custom else None,
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
    negative_custom: bool = False,
    source: str,
    model: registry.ModelDef,
    tier: str,
    length: int,
    seed: int,
    lightning: bool,
    loras: list[str],
    settings: dict | None = None,
) -> library.Record:
    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=model.id,
        prompt=prompt.strip(),
        negative=negative.strip(),
        negative_custom=negative_custom,
        source_name=source,
        tier=tier,
        length=workflow.normalize_length(length),
        seed=seed,
        lightning=lightning and bool(model.lightning),
        loras=loras,
        settings=settings or {},
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
    negative_custom: str = Form(""),
    loras: str = Form(""),
    interpolate: int = Form(1),
    interpolate_model: str = Form(""),
    upscaler: str = Form(""),
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
        negative_custom=negative_custom.lower() in ("1", "true", "on", "yes"),
        source=image.filename or "upload",
        model=chosen,
        tier=tier if tier in chosen.tiers else config.default_tier(chosen),
        # defaults.fps honours an FPS override in .env; chosen.fps would not,
        # and then the produced clip would not be the duration that was picked.
        length=(workflow.frames_for_seconds(seconds, defaults.fps) if seconds > 0
                else (length or defaults.length)),
        seed=seed if seed >= 0 else random.randint(0, 2**31 - 1),
        lightning=use_lightning,
        loras=picked,
        settings={
            "interpolate": max(1, min(interpolate, 4)),
            "interpolate_model": interpolate_model,
            "upscaler": upscaler,
        },
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
            "upscalers": installed_upscalers(),
            "interpolators": installed_interpolators(),
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
        "version_id": payload.get("version_id"),
        "name": label,
    }
    download = models.enqueue_files(
        key=f"civitai:{payload.get('version_id') or remote[0].name}",
        label=f"LoRA · {label}",
        files=remote,
        sidecars={f.name: meta for f in remote},
    )
    # The sample image is small and the search response already handed us the
    # URL; fetching it now is what turns the LoRA list from filenames into
    # something you can actually recognise.
    if preview_url := str(payload.get("preview") or ""):
        for f in remote:
            asyncio.create_task(models.fetch_preview(folder, f.name, preview_url))
    return JSONResponse(download.public())


@app.get("/api/loras/{name}/preview")
async def lora_preview(name: str) -> FileResponse:
    try:
        path = models.preview_path("loras", name)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    if not path.is_file():
        raise HTTPException(404, "這個 LoRA 沒有預覽圖")
    return FileResponse(path)


@app.post("/api/loras/{name}/preview")
async def set_lora_preview(name: str, payload: dict = Body(...)) -> JSONResponse:
    """Attach a preview to a LoRA that arrived without one."""
    url = str(payload.get("url") or "")
    if not url:
        raise HTTPException(400, "沒有給圖片網址")
    try:
        target = models.preview_path("loras", name)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    target.unlink(missing_ok=True)
    if not await models.fetch_preview("loras", name, url):
        raise HTTPException(502, "抓不到這張預覽圖")
    return JSONResponse({"name": name, "preview": True})


@app.post("/api/loras/{name}/preview/upload")
async def upload_lora_preview(name: str, image: UploadFile) -> JSONResponse:
    """Or use one of your own generated images as the LoRA's cover."""
    data = await image.read()
    if not data:
        raise HTTPException(400, "圖片是空的")
    try:
        target = models.preview_path("loras", name)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    try:
        picture = Image.open(io.BytesIO(data)).convert("RGB")
    except Exception:
        raise HTTPException(400, "無法辨識這個圖片格式")
    picture.thumbnail((512, 512))
    target.parent.mkdir(parents=True, exist_ok=True)
    picture.save(target, "JPEG", quality=85)
    return JSONResponse({"name": name, "preview": True})


@app.get("/api/updates")
async def check_updates(refresh: bool = False) -> JSONResponse:
    """Is anything here out of date? Best-effort; never blocks generation."""
    if refresh:
        updates.forget()
    loop = asyncio.get_running_loop()
    git = await loop.run_in_executor(
        None, updates.app_updates, config.REPO_DIR, config.COMFY_DIR
    )
    watched: list = []
    for folder in ("loras", "checkpoints"):
        directory = config.MODELS_DIR / folder
        if directory.is_dir():
            watched += sorted(directory.glob("*.safetensors"))
    try:
        civitai_items = await updates.civitai_updates(watched)
    except Exception as exc:  # noqa: BLE001 - a check must never break the page
        return JSONResponse({**git, "civitai": [], "civitai_error": str(exc)})
    return JSONResponse({**git, "civitai": civitai_items, "civitai_error": ""})


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
    if model.id.startswith(images.CUSTOM_PREFIX):
        # Size is unknown for a user-installed file; presence is all we can check.
        here = (config.MODELS_DIR / "checkpoints" / model.file.name).is_file()
        return {"installed": here, "partial": False, "bytes_on_disk": 0,
                "missing": [] if here else [model.file.name]}
    states = [models.file_status(f) for f in model.all_files]
    on_disk = sum(n for _, n in states)
    missing = [f.name for f, (st, _) in zip(model.all_files, states) if st != "ok"]
    return {
        "installed": not missing,
        "partial": bool(missing) and on_disk > 0,
        "bytes_on_disk": on_disk,
        "missing": missing,
    }


def installed_checkpoints() -> list[str]:
    folder = config.MODELS_DIR / "checkpoints"
    return sorted(p.name for p in folder.glob("*.safetensors")) if folder.is_dir() else []


async def run_comic_job(record: library.Record) -> None:
    """Render every panel, then compose the page here rather than in ComfyUI."""
    model = images.resolve(record.model_id, installed_checkpoints())
    if model is None:
        raise ComfyError(f"不認識的圖片模型：{record.model_id}")
    state = image_status(model)
    if not state["installed"]:
        raise ComfyError(
            f"{model.label} 還沒下載完（缺 {', '.join(state['missing'][:3])}）。"
            "請到「模型」分頁下載。"
        )
    cfg = record.settings or {}
    layout = comics.get(str(cfg.get("layout", "")))
    if layout is None:
        raise ComfyError(f"不認識的分鏡：{cfg.get('layout')}")

    settings = images.ImageSettings.from_dict(cfg)
    rng = random.Random(record.seed)
    shared = prompts.expand(str(cfg.get("shared", "")), rng)
    raw_panels = list(cfg.get("panels") or [])
    panels: list[tuple[str, int, int]] = []
    for index, panel in enumerate(layout.panels):
        text = raw_panels[index] if index < len(raw_panels) else ""
        width, height = comics.panel_size(panel, layout.aspect)
        panels.append(
            (
                comics.scaffold(
                    prompts.expand(str(text), rng), shared,
                    model.positive_prefix if cfg.get("use_prefix", True) else "",
                ),
                width,
                height,
            )
        )

    graph = images.build_comic(
        model,
        settings,
        panels=panels,
        negative=record.negative,
        seed=record.seed,
        available_nodes=await client.node_classes(),
        filename_prefix=f"comic/{record.id}",
    )
    if problems := await client.validate(graph):
        raise ComfyError("工作流程與這台 ComfyUI 不相容：\n- " + "\n- ".join(problems))

    def progress(value: float) -> None:
        record._progress = value
        record.message = f"畫第 {min(layout.count, int(value * layout.count) + 1)}/{layout.count} 格…"

    record.message = "載入模型…（第一次會比較久）"
    files = await client.run(graph, on_progress=progress)
    if not files:
        raise ComfyError("ComfyUI 沒有回傳任何輸出檔案")

    record.message = "拼版中…"
    # ComfyUI returns outputs in node order, which is panel order here, but the
    # filenames carry the index too - sort on those so a reordered response
    # cannot silently scramble the page.
    ordered = sorted(files, key=lambda f: f.filename)
    art: list[Image.Image] = []
    record.outputs = []
    for index, f in enumerate(ordered[: layout.count]):
        data = await client.download(f)
        name = f"{record.id}-p{index + 1:02d}.png"
        (config.OUTPUT_DIR / name).write_bytes(data)
        record.outputs.append(name)
        art.append(Image.open(io.BytesIO(data)))

    bubbles = [
        [comics.Bubble(text=str(b.get("text", "")), at=str(b.get("at", "top-left")))
         for b in (row or []) if str(b.get("text", "")).strip()]
        for row in (cfg.get("bubbles") or [])
    ]
    style = comics.PageStyle(
        gutter=int(cfg.get("gutter", 18)),
        border=int(cfg.get("border", 5)),
        width=int(cfg.get("page_width", 1600)),
        font_path=str(cfg.get("font", "")),
    )
    page = comics.compose(layout, art, bubbles, style)
    page_name = f"{record.id}.png"
    page.save(config.OUTPUT_DIR / page_name, "PNG")
    # The page is the deliverable, so it leads; the panels stay available for
    # anyone who wants to re-letter or re-crop one.
    record.outputs.insert(0, page_name)
    record.output = page_name
    record.width, record.height = page.size

    thumb = page.copy()
    thumb.thumbnail((480, 480))
    record.thumb = f"{record.id}.jpg"
    thumb.convert("RGB").save(lib.thumbs / record.thumb, "JPEG", quality=84)


async def run_image_job(record: library.Record) -> None:
    if record.kind == "comic":
        return await run_comic_job(record)
    model = images.resolve(record.model_id, installed_checkpoints())
    if model is None:
        raise ComfyError(f"不認識的圖片模型：{record.model_id}")
    state = image_status(model)
    if not state["installed"]:
        raise ComfyError(
            f"{model.label} 還沒下載完（缺 {', '.join(state['missing'][:3])}）。"
            "請到「模型」分頁下載。"
        )

    settings = images.ImageSettings.from_dict(record.settings)
    # One expansion per image, seeded by the job's own seed so a re-run with the
    # same seed reproduces the same set of wildcard picks.
    rng = random.Random(record.seed)
    expanded = [prompts.expand(record.prompt, rng) for _ in range(settings.batch)]
    if len(set(expanded)) > 1:
        record.settings = {**record.settings, "expanded": expanded}

    init_name = ""
    if record.source_name:
        # image-to-image: the source was stashed at submit time, because the
        # worker runs long after the upload request has gone.
        source = config.INBOX_DIR / f"{record.id}.png"
        if not source.is_file():
            raise ComfyError("找不到剛才那張來源圖，請重新上傳一次")
        init_name = await client.upload_image(source.read_bytes(), f"{record.id}.png")

    graph = images.build(
        model,
        settings,
        prompt=expanded,
        negative=prompts.expand(record.negative, rng),
        seed=record.seed,
        width=record.width,
        height=record.height,
        init_image=init_name,
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
    except Exception:  # noqa: BLE001
        samplers, schedulers = [], []

    known = {m.file.name for m in images.IMAGE_MODELS}
    # Checkpoints the user installed themselves are first-class entries, not a
    # list they can look at but never select.
    catalogue = list(images.IMAGE_MODELS) + [
        images.custom_model(name) for name in installed_checkpoints() if name not in known
    ]
    installed_up = installed_upscalers()

    out = []
    for model in catalogue:
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
                "custom": model.id.startswith(images.CUSTOM_PREFIX),
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
            "upscalers": installed_up,
            "embeddings": await client.embeddings(),
            "custom_size": CUSTOM_SIZE,
            "syntax": [list(pair) for pair in prompts.SYNTAX_HELP],
            "not_supported": [list(pair) for pair in prompts.NOT_SUPPORTED],
            "gpu": gpu,
        }
    )


@app.delete("/api/checkpoints/{name}")
async def delete_checkpoint(name: str) -> JSONResponse:
    folder = (config.MODELS_DIR / "checkpoints").resolve()
    path = (folder / name).resolve()
    if folder != path.parent or not path.name:
        raise HTTPException(400, f"不合法的檔名：{name}")
    if name in {m.file.name for m in images.IMAGE_MODELS}:
        raise HTTPException(
            400, "這是目錄裡的內建底模，請到「模型」分頁處理，避免和下載狀態不同步"
        )
    if not path.is_file():
        raise HTTPException(404, f"找不到 {name}")
    path.unlink()
    client.invalidate()
    return JSONResponse({"deleted": name})


@app.post("/api/image/models/{model_id}/download")
async def download_image_model(model_id: str) -> JSONResponse:
    model = images.get(model_id)
    if model is None:
        raise HTTPException(404, f"不認識的圖片模型：{model_id}")
    if not model.file.repo:
        raise HTTPException(400, "自己裝的底模沒有下載來源")
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
    model = images.resolve(str(payload.get("model", "")), installed_checkpoints())
    if model is None:
        raise HTTPException(400, f"不認識的圖片模型：{payload.get('model')}")
    state = image_status(model)
    if not state["installed"]:
        raise HTTPException(
            400,
            f"{model.label} 還沒下載完（缺 {', '.join(state['missing'][:3])}）。"
            "請到「模型」分頁下載，或改選已安裝的。",
        )

    init_name = str(payload.get("init_image") or "")
    raw_prompt = str(payload.get("prompt", "")).strip()
    if not raw_prompt and not init_name:
        raise HTTPException(400, "提詞是空的 —— 沒放來源圖的話，畫面全靠提詞")
    if complaint := prompts.weights_ok(raw_prompt):
        raise HTTPException(400, complaint)

    prompt = raw_prompt
    # Never prepend twice: a re-run sends back a prompt that may already carry
    # the prefix.
    if (payload.get("use_prefix", True) and model.positive_prefix
            and not raw_prompt.startswith(model.positive_prefix)):
        prompt = f"{model.positive_prefix}, {raw_prompt}"

    size_name = str(payload.get("size") or model.default_size)
    if size_name == CUSTOM_SIZE:
        width, height = custom_size(payload)
    else:
        width, height = model.sizes.get(size_name, (1024, 1024))
    batch = max(1, min(int(payload.get("batch", 1)), 16))
    seed = int(payload.get("seed", -1))

    settings = images.ImageSettings.from_dict(
        {
            **images.defaults_for(model).to_dict(),
            **{k: v for k, v in payload.items() if v is not None},
            "batch": batch,
            "loras": parse_image_loras(payload.get("loras") or []),
        }
    )
    if settings.upscaler and settings.upscaler not in installed_upscalers():
        raise HTTPException(400, f"還沒下載放大模型 {settings.upscaler}，請到「模型」分頁下載")
    if settings.hires_upscaler and settings.hires_upscaler not in installed_upscalers():
        raise HTTPException(400, f"還沒下載放大模型 {settings.hires_upscaler}，請到「模型」分頁下載")

    source_name = ""
    if init_name:
        source = (config.INBOX_DIR / init_name).resolve()
        if config.INBOX_DIR.resolve() not in source.parents or not source.is_file():
            raise HTTPException(400, "找不到剛才上傳的來源圖，請重新放一次")
        source_name = init_name

    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=model.id,
        kind="image",
        prompt=prompt,
        prompt_raw=raw_prompt,
        # Key presence, not truthiness: an empty string is a deliberate
        # "run with no negative prompt".
        negative=str(payload["negative"]) if "negative" in payload else model.negative,
        negative_custom=True,
        seed=seed if seed >= 0 else random.randint(0, 2**31 - 1),
        width=width,
        height=height,
        tier=size_name,
        length=batch,
        source_name=source_name,
        loras=[f"{n}:{m}" for n, m, _ in settings.loras],
        settings=settings.to_dict(),
    )
    if source_name:
        # The worker runs long after this request is gone, so the picture has to
        # be on disk under the job's own name rather than held in memory.
        (config.INBOX_DIR / f"{record.id}.png").write_bytes(source.read_bytes())
    lib.add(record)
    queue.put_nowait((record.id, b""))
    return JSONResponse(public(record))


CUSTOM_SIZE = "自訂尺寸"


def custom_size(payload: dict) -> tuple[int, int]:
    """SDXL wants multiples of 8 and falls apart far from ~1 megapixel."""
    try:
        width = int(payload.get("width") or 1024)
        height = int(payload.get("height") or 1024)
    except (TypeError, ValueError):
        raise HTTPException(400, "自訂尺寸要填數字")
    width = max(256, min(width, 2048)) // 8 * 8
    height = max(256, min(height, 2048)) // 8 * 8
    return width, height


def parse_image_loras(raw: list) -> list[list]:
    picked: list[list] = []
    for entry in raw:
        name = str(entry.get("name", ""))
        if "/" in name or "\\" in name or not name:
            raise HTTPException(400, f"不合法的 LoRA 檔名：{name}")
        model_s = float(entry.get("strength", 0.8))
        clip_s = float(entry.get("strength_clip", model_s))
        picked.append([name, model_s, clip_s])
    return picked


def installed_upscalers() -> list[str]:
    folder = config.MODELS_DIR / "upscale_models"
    if not folder.is_dir():
        return []
    return sorted(
        p.name for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in (".pth", ".safetensors")
    )


@app.post("/api/image/upload")
async def image_upload(image: UploadFile) -> JSONResponse:
    """Stash a source image for image-to-image, and report its aspect ratio."""
    data = await image.read()
    if not data:
        raise HTTPException(400, "圖片是空的")
    try:
        opened = Image.open(io.BytesIO(data))
        opened.verify()
        width, height = Image.open(io.BytesIO(data)).size
    except Exception:
        raise HTTPException(400, "無法辨識這個圖片格式")
    name = f"src-{uuid.uuid4().hex[:12]}.png"
    config.INBOX_DIR.mkdir(parents=True, exist_ok=True)
    # Staging files belong to nobody until a job claims a copy, so sweep the
    # ones an abandoned tab left behind rather than growing the folder forever.
    cutoff = time.time() - 24 * 3600
    for stale in config.INBOX_DIR.glob("src-*.png"):
        if stale.stat().st_mtime < cutoff:
            stale.unlink(missing_ok=True)
    Image.open(io.BytesIO(data)).convert("RGB").save(config.INBOX_DIR / name, "PNG")
    return JSONResponse({"name": name, "width": width, "height": height})


@app.get("/api/upscalers")
async def list_upscalers() -> JSONResponse:
    here = set(installed_upscalers())
    out = [
        {
            "id": u.id, "label": u.label, "name": u.name, "scale": u.scale,
            "best_for": u.best_for, "size": u.size, "installed": u.name in here,
        }
        for u in upscalers.UPSCALERS
    ]
    extra = sorted(here - {u.name for u in upscalers.UPSCALERS})
    out += [
        {"id": "", "label": name, "name": name, "scale": 0, "best_for": "你自己放進去的",
         "size": 0, "installed": True}
        for name in extra
    ]
    here_interp = set(installed_interpolators())
    interp = [
        {
            "id": i.id, "label": i.label, "name": i.name, "best_for": i.best_for,
            "size": i.size, "installed": i.name in here_interp,
        }
        for i in upscalers.INTERPOLATORS
    ]
    interp += [
        {"id": "", "label": name, "name": name, "best_for": "你自己放進去的",
         "size": 0, "installed": True}
        for name in sorted(here_interp - {i.name for i in upscalers.INTERPOLATORS})
    ]
    return JSONResponse(
        {
            "upscalers": out, "help": upscalers.HELP,
            "interpolators": interp, "interp_help": upscalers.INTERP_HELP,
        }
    )


def installed_interpolators() -> list[str]:
    folder = config.MODELS_DIR / "frame_interpolation"
    if not folder.is_dir():
        return []
    return sorted(
        p.name for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in (".pth", ".safetensors", ".pkl")
    )


def _queue_single(key: str, label: str, file) -> dict:
    remote = downloader.RemoteFile(
        url=downloader.url_for(file), folder=file.folder, name=file.name, size=file.size,
    )
    return models.enqueue_files(
        key=key, label=label, files=[remote], kind="model"
    ).public()


@app.post("/api/upscalers/{upscaler_id}/download")
async def download_upscaler(upscaler_id: str) -> JSONResponse:
    chosen = upscalers.get(upscaler_id)
    if chosen is None:
        raise HTTPException(404, f"不認識的放大模型：{upscaler_id}")
    return JSONResponse(
        _queue_single(f"upscaler:{chosen.id}", f"放大模型 · {chosen.label}", chosen.file)
    )


@app.post("/api/interpolators/{interp_id}/download")
async def download_interpolator(interp_id: str) -> JSONResponse:
    chosen = upscalers.interpolator(interp_id)
    if chosen is None:
        raise HTTPException(404, f"不認識的補幀模型：{interp_id}")
    return JSONResponse(
        _queue_single(f"interp:{chosen.id}", f"補幀模型 · {chosen.label}", chosen.file)
    )


@app.get("/api/comic/layouts")
async def comic_layouts() -> JSONResponse:
    return JSONResponse(
        {
            "layouts": [comics.public(l) for l in comics.LAYOUTS],
            "help": comics.HELP,
            "shots": [list(pair) for pair in comics.SHOT_HINTS],
            "anchors": list(comics.ANCHORS),
            "max_panels": comics.MAX_PANELS,
            # Without a CJK-capable font the bubbles have to be skipped, so the
            # UI needs to know before the user types dialogue into them.
            "font": bool(comics.find_font(20)),
            "color_negative": comics.COLOR_NEGATIVE,
        }
    )


@app.post("/api/comic/generate")
async def comic_generate(payload: dict = Body(...)) -> JSONResponse:
    model = images.resolve(str(payload.get("model", "")), installed_checkpoints())
    if model is None:
        raise HTTPException(400, f"不認識的圖片模型：{payload.get('model')}")
    state = image_status(model)
    if not state["installed"]:
        raise HTTPException(
            400,
            f"{model.label} 還沒下載完（缺 {', '.join(state['missing'][:3])}）。"
            "請到「模型」分頁下載，或改選已安裝的。",
        )
    layout = comics.get(str(payload.get("layout", "four-grid")))
    if layout is None:
        raise HTTPException(400, f"不認識的分鏡：{payload.get('layout')}")

    panels = [str(p or "") for p in (payload.get("panels") or [])][: layout.count]
    shared = str(payload.get("shared", ""))
    if not any(p.strip() for p in panels) and not shared.strip():
        raise HTTPException(400, "每一格都是空的 —— 至少寫一格要畫什麼，或填共用提詞")
    for text in [*panels, shared]:
        if complaint := prompts.weights_ok(text):
            raise HTTPException(400, complaint)

    settings = images.ImageSettings.from_dict(
        {
            **images.defaults_for(model).to_dict(),
            **{k: v for k, v in payload.items() if v is not None},
            "batch": 1,
            "loras": parse_image_loras(payload.get("loras") or []),
        }
    )
    if settings.upscaler and settings.upscaler not in installed_upscalers():
        raise HTTPException(400, f"還沒下載放大模型 {settings.upscaler}，請到「模型」分頁下載")

    full_color = bool(payload.get("full_color", True))
    negative = comics.negative_for(
        str(payload["negative"]) if "negative" in payload else model.negative,
        full_color=full_color,
        # Lettering is drawn afterwards, so the model is told not to attempt it -
        # unless the user wants the model's own (unreadable) sound effects.
        draw_text=not bool(payload.get("model_text", False)),
    )
    seed = int(payload.get("seed", -1))
    bubbles = payload.get("bubbles") or []

    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=model.id,
        kind="comic",
        prompt=" / ".join(p.strip() for p in panels if p.strip()) or shared,
        prompt_raw=" / ".join(panels),
        negative=negative,
        negative_custom=True,
        seed=seed if seed >= 0 else random.randint(0, 2**31 - 1),
        tier=layout.label,
        length=layout.count,
        loras=[f"{n}:{m}" for n, m, _ in settings.loras],
        settings={
            **settings.to_dict(),
            "layout": layout.id,
            "panels": panels,
            "shared": shared,
            "bubbles": bubbles,
            "full_color": full_color,
            "use_prefix": bool(payload.get("use_prefix", True)),
            "gutter": max(0, min(int(payload.get("gutter", 18)), 80)),
            "border": max(0, min(int(payload.get("border", 5)), 20)),
            "page_width": max(768, min(int(payload.get("page_width", 1600)), 3000)),
        },
    )
    lib.add(record)
    queue.put_nowait((record.id, b""))
    return JSONResponse(public(record))


@app.post("/api/comic/preview")
async def comic_preview(payload: dict = Body(...)) -> FileResponse:
    """The page with placeholder panels, so the layout can be judged instantly.

    Rendering four panels takes minutes; deciding whether the dialogue fits
    should not. This draws the real geometry and the real lettering with grey
    boxes where the art will go.
    """
    layout = comics.get(str(payload.get("layout", "four-grid")))
    if layout is None:
        raise HTTPException(400, f"不認識的分鏡：{payload.get('layout')}")
    bubbles = [
        [comics.Bubble(text=str(b.get("text", "")), at=str(b.get("at", "top-left")))
         for b in (row or []) if str(b.get("text", "")).strip()]
        for row in (payload.get("bubbles") or [])
    ]
    style = comics.PageStyle(
        gutter=max(0, min(int(payload.get("gutter", 18)), 80)),
        border=max(0, min(int(payload.get("border", 5)), 20)),
        width=900,
    )
    page = comics.compose(layout, [], bubbles, style)
    config.INBOX_DIR.mkdir(parents=True, exist_ok=True)
    target = config.INBOX_DIR / "comic-preview.png"
    page.save(target, "PNG")
    return FileResponse(target, media_type="image/png",
                        headers={"Cache-Control": "no-store"})


@app.post("/api/prompt/preview")
async def prompt_preview(payload: dict = Body(...)) -> JSONResponse:
    """What a wildcard prompt will actually expand to, before spending a GPU on it."""
    text = str(payload.get("prompt", ""))
    count = max(1, min(int(payload.get("count", 3)), 16))
    return JSONResponse(
        {
            "has_wildcards": prompts.has_wildcards(text),
            "samples": prompts.preview(text, count, seed=int(payload.get("seed", 0))),
            "warning": prompts.weights_ok(text),
        }
    )


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

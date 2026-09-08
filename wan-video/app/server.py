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
import re
import shutil
import time
import traceback
import uuid
from pathlib import Path

import artists
import assemble
import charpacks
import civitai
import claims
import comics
import config
import controlnets
import images
import downloader
import envfile
import hfhub
import experiments as exp_mod
import inspect_image
import library
import pagelayout
import posebook
import promptbook
import prompts
import promptdoctor
import promptmerge
import quicktags
import shortdrama
import styles
import refs as refslib
import registry
import runner as runner_mod
import tags
import training
import updates
import upscalers
import wfimport
import workflow
import comfy_client
from comfy_client import ComfyClient, ComfyError
from fastapi import Body, FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps

STATIC = Path(__file__).parent / "static"

app = FastAPI(title="wan-drop")
client = ComfyClient(config.COMFY_URL)
models = downloader.Manager(config.MODELS_DIR)
lib = library.Library(config.OUTPUT_DIR, config.STAGING_DIR)
book = promptbook.Book(config.OUTPUT_DIR.parent / "promptbook.jsonl")
queue: asyncio.Queue[tuple[str, bytes]] = asyncio.Queue()
running: set[str] = set()
# Strong references to fire-and-forget tasks; see civitai_download.
_background: set[asyncio.Task] = set()


UPLOAD_MODEL_ID = "user-upload"
# A joined episode is its own kind of thing: no model made it, and it must not
# borrow the name of the one that made its shots. It is also not the same as an
# imported file, because deleting the shots it was built from does not
# invalidate it - it is a finished, independent file.
ASSEMBLY_MODEL_ID = "drama-assembly"

# Caps on an imported still. Not about disk - a decompression bomb is a small
# file that becomes gigabytes of pixels in memory, and a keyframe has no reason
# to be anywhere near either limit.
MAX_IMPORT_BYTES = 80_000_000
MAX_IMPORT_PIXELS = 64_000_000


def model_label(record: library.Record) -> str:
    """Records span two catalogues; look in the right one."""
    # An imported picture was not generated here, so it must not wear the name
    # of a model that did not make it - "which model produced this" has to keep
    # meaning what it says.
    if record.model_id == UPLOAD_MODEL_ID:
        return "（你自己匯入的圖）"
    if record.model_id == ASSEMBLY_MODEL_ID:
        return "（整集接起來的成品）"
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
    for d in (config.OUTPUT_DIR, lib.thumbs, config.STAGING_DIR, config.INBOX_DIR):
        d.mkdir(parents=True, exist_ok=True)
    lib.load()
    book.load()
    # A finished download changes what ComfyUI can offer, and its /object_info
    # is cached; drop that cache or the new model looks uninstalled.
    models.on_change = client.invalidate
    models.start()
    app.state.worker = asyncio.create_task(worker())


@app.on_event("shutdown")
async def shutdown() -> None:
    lib.save()
    book.flush()
    for task in (getattr(app.state, "worker", None), models.stop()):
        if task:
            task.cancel()


async def worker() -> None:
    """Serial job runner. Survives individual job failures."""
    while True:
        # A third element for the one model that takes a second picture; older
        # two-element items are still accepted so nothing in flight breaks.
        item = await queue.get()
        job_id, image_bytes = item[0], item[1]
        end_bytes = item[2] if len(item) > 2 else b""
        record = lib.get(job_id)
        if record is None:
            queue.task_done()
            continue
        running.add(job_id)
        try:
            # Waited for per job, not once at startup. Outside the try, a
            # ComfyUI that is slow to boot kills the only queue consumer, and
            # because nothing restarts it every later job sits at "排隊中"
            # forever with no error to show for it.
            record.message = "等 ComfyUI 就緒…"
            await client.wait_until_ready()
            record.status, record.started = "running", time.time()
            record.message = "準備中…"
            await run_job(record, image_bytes, end_bytes)
            record.status, record.message = "done", ""
            record._progress = 1.0
        except (ComfyError, workflow.UnsupportedModel) as exc:
            record.status, record.message = "error", str(exc)
        except Exception as exc:  # noqa: BLE001 - never kill the worker
            record.status = "error"
            # `explain` turns a connection failure into "ComfyUI is not
            # running, here is how to start it". Anything it does not
            # recognise still falls back to the class name and the message.
            record.message = comfy_client.explain(exc, config.COMFY_URL)
            traceback.print_exc()
        finally:
            record.finished = time.time()
            running.discard(job_id)
            lib.save()
            queue.task_done()


async def run_job(record: library.Record, image_bytes: bytes,
                  end_bytes: bytes = b"") -> None:
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
    available = await client.node_classes()
    record.settings = {
        "steps": params.steps, "cfg": params.cfg, "shift": params.shift,
        "sampler": params.sampler, "scheduler": params.scheduler,
        "interpolate": params.interpolate, "interpolate_model": params.interpolate_model,
        "upscaler": params.upscaler,
        # What the file will really play at - asked of the same function the
        # graph builder uses, so a skipped interpolation is not advertised.
        "out_fps": workflow.output_fps(params, available),
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

    # The second picture, for the one model that takes one. Uploaded under its
    # own name so the graph can reference both.
    end_uploaded = ""
    if end_bytes:
        end_png = io.BytesIO()
        Image.open(io.BytesIO(end_bytes)).convert("RGB").save(end_png, "PNG")
        end_uploaded = await client.upload_image(end_png.getvalue(), f"{record.id}-end.png")

    # An imported workflow wins over a built one. It is the official graph from
    # the user's own ComfyUI, where it demonstrably runs; this app's builders
    # only exist for the families it has been able to verify.
    stored = wfimport.load(config.WORKFLOWS_DIR, model.id)
    if stored:
        slots = wfimport.slots_from(stored)
        graph = wfimport.apply(
            stored["graph"], slots,
            image=uploaded,
            prompt=record.prompt,
            negative=record.negative if record.negative_custom else model.negative,
            seed=record.seed,
            width=record.width,
            height=record.height,
            prefix=f"wan/{record.id}",
        )
        record.message = "用你匯入的工作流…"
    else:
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
            available_nodes=available,
            filename_prefix=f"wan/{record.id}",
            end_image_name=end_uploaded or None,
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
    # The second picture, for the one model whose node takes one. Empty for
    # everything else, and refused by the graph builder if it is not empty and
    # the model has nowhere to put it.
    end_bytes: bytes = b"",
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
    queue.put_nowait((record.id, image_bytes, end_bytes))
    return record


@app.post("/api/generate")
async def generate(
    image: UploadFile,
    # Only MiniMax H3 has anywhere to put this: its node takes an optional
    # `last_frame`. Every other model refuses rather than ignoring it.
    end_image: UploadFile | None = None,
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

    end_data = await end_image.read() if end_image is not None else b""
    if end_image is not None and not end_data:
        raise HTTPException(400, "最後一張圖是空的")
    if end_data:
        try:
            Image.open(io.BytesIO(end_data)).verify()
        except Exception:
            raise HTTPException(400, "無法辨識最後一張圖的格式")

    chosen = registry.get(model) if model else effective_default()
    if chosen is None:
        raise HTTPException(400, f"不認識的模型：{model}")
    # Runnable here means "this app ships a graph for it" OR "the user imported
    # one". Checking only the first is what made the picker offer a model the
    # server then refused.
    if not chosen.runnable and not wfimport.load(config.WORKFLOWS_DIR, chosen.id):
        raise HTTPException(
            400,
            f"{chosen.label} 只提供檔案下載，這個 app 沒有可以跑它的工作流。"
            "把 ComfyUI 官方的工作流匯入就可以了 —— "
            "短劇分頁「整集」那一格有「去匯入官方工作流」的按鈕，"
            "「模型」分頁最下面也有同一個地方。")
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
        end_bytes=end_data,
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
    imported_workflows = wfimport.installed(config.WORKFLOWS_DIR)
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
                # A gated repo answers 401 to the very first byte, so the UI has
                # to be able to say so before the download button, not after.
                "gated_repos": model.gated_repos,
                "has_hf_token": bool(downloader.hf_token()),
                # Some licences restrict where the weights may be used at all -
                # HunyuanVideo excludes the EU, UK and Korea; MiniMax H3 adds
                # the United States. That belongs in front of the download
                # button, not in a note under it.
                "licence": model.licence.public() if model.licence else None,
                # A files-only model becomes generatable once the user imports
                # the official workflow from their own ComfyUI, so "can I run
                # this" is not a catalogue fact - it depends on this machine.
                "has_workflow": model.id in imported_workflows,
                "runnable_here": model.runnable or model.id in imported_workflows,
                # "video" or "tts". Only the video ones belong in a picker that
                # asks which model makes the clip.
                "role": model.role,
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


@app.get("/api/workflows")
async def list_workflows() -> JSONResponse:
    """Which models have an imported workflow behind them."""
    return JSONResponse({
        "workflows": wfimport.installed(config.WORKFLOWS_DIR),
        "folder": str(config.WORKFLOWS_DIR),
        # The models this is for: ones the app downloads but has no verified
        # graph of its own for.
        # Video models only. The TTS entries are also files-only, but a
        # ComfyUI video workflow is not a thing they have - offering them here
        # is a dead end dressed up as an option.
        "candidates": [
            {"id": m.id, "label": m.label,
             "installed": models.model_status(m)["installed"]}
            for m in registry.MODELS
            if not m.family_runnable and m.role == "video"
        ],
    })


@app.post("/api/workflows/inspect")
async def inspect_workflow(payload: dict = Body(default={})) -> JSONResponse:
    """Read an exported workflow and say what it found, without saving."""
    payload = payload if isinstance(payload, dict) else {}
    try:
        graph = wfimport.parse(str(payload.get("json") or ""))
    except wfimport.ImportError_ as exc:
        raise HTTPException(400, str(exc)) from exc
    detected = wfimport.detect(graph)
    return JSONResponse({
        "nodes": len(graph),
        "detected": detected.public(),
        "summary": wfimport.summary(detected),
        "comfy_url": config.COMFY_URL,
    })


@app.post("/api/workflows/{model_id}")
async def save_workflow(model_id: str, payload: dict = Body(default={})) -> JSONResponse:
    """Attach an exported workflow to a model, so it can be generated from here."""
    model = registry.get(model_id)
    if model is None:
        raise HTTPException(404, f"不認識的模型：{model_id}")
    payload = payload if isinstance(payload, dict) else {}
    try:
        graph = wfimport.parse(str(payload.get("json") or ""))
    except wfimport.ImportError_ as exc:
        raise HTTPException(400, str(exc)) from exc
    detected = wfimport.detect(graph)

    # Overrides from the confirmation step, when detection got something wrong.
    for name in ("image", "positive", "negative"):
        chosen = payload.get(name)
        if isinstance(chosen, dict) and chosen.get("node"):
            node_id = str(chosen["node"])
            node = graph.get(node_id)
            if node is None:
                raise HTTPException(400, f"這個工作流沒有第 {node_id} 號節點")
            key = str(chosen.get("key") or "")
            if key not in (node.get("inputs") or {}):
                raise HTTPException(400, f"第 {node_id} 號節點沒有 {key} 這個欄位")
            setattr(detected, name, wfimport.Slot(
                node_id, key, node.get("class_type", ""),
                str((node.get("_meta") or {}).get("title") or "")))

    if not detected.usable:
        raise HTTPException(
            400, "這個工作流少了必要的東西：" + "、".join(detected.missing)
                 + "。要有一個放提詞的欄位和一個儲存節點才跑得起來。")
    record = wfimport.save(config.WORKFLOWS_DIR, model_id, graph, detected,
                           source=str(payload.get("source") or ""))
    return JSONResponse({"saved": True, "model_id": model_id,
                         "nodes": record["nodes"],
                         "summary": wfimport.summary(detected)})


@app.delete("/api/workflows/{model_id}")
async def delete_workflow(model_id: str) -> JSONResponse:
    return JSONResponse({"removed": wfimport.remove(config.WORKFLOWS_DIR, model_id)})


@app.post("/api/civitai/resolve")
async def civitai_resolve(payload: dict = Body(default={})) -> JSONResponse:
    """Turn a CivitAI link the user pasted into something downloadable.

    The built-in search only finds what CivitAI's own ranking surfaces. Someone
    who already found the LoRA they want - in a browser, from a friend, off a
    forum post - has a URL and no way to use it, which is the gap this closes.
    """
    payload = payload if isinstance(payload, dict) else {}
    try:
        return JSONResponse(await civitai.resolve(str(payload.get("url") or "")))
    except civitai.CivitaiError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/api/hf/resolve")
async def hf_resolve(payload: dict = Body(default={})) -> JSONResponse:
    """Look up a pasted Hugging Face link and list the weight files in it.

    There is no HF search here on purpose - see hfhub.py for the two reasons.
    This answers the narrower question the module can answer honestly: the user
    has a link, what is in it.
    """
    payload = payload if isinstance(payload, dict) else {}
    try:
        return JSONResponse(await hfhub.resolve(
            str(payload.get("url") or ""), token=downloader.hf_token()))
    except hfhub.NeedsToken as exc:
        raise HTTPException(401, str(exc)) from exc
    except hfhub.HubError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/api/hf/download")
async def hf_download(payload: dict = Body(default={})) -> JSONResponse:
    """Fetch the files the user ticked.

    The browser sends repo, revision and paths - never a URL. hfhub builds the
    URL, so the Hugging Face token can only ever be sent to huggingface.co.
    """
    payload = payload if isinstance(payload, dict) else {}
    repo_id = str(payload.get("repo_id") or "")
    revision = str(payload.get("revision") or "main")
    wanted = payload.get("files") or []
    if not wanted:
        raise HTTPException(400, "沒有勾選任何檔案")

    token = downloader.hf_token()
    headers = (("Authorization", f"Bearer {token}"),) if token else ()

    remote = []
    for item in wanted:
        if not isinstance(item, dict):
            raise HTTPException(400, "檔案格式不對")
        path = str(item.get("path") or "")
        folder = str(item.get("folder") or "loras")
        if folder not in ("loras", "checkpoints", "vae", "text_encoders",
                          "diffusion_models", "controlnet"):
            raise HTTPException(400, f"不認識的資料夾：{folder}")
        try:
            url = hfhub.download_url(repo_id, revision, path)
        except hfhub.HubError as exc:
            raise HTTPException(400, str(exc)) from exc
        remote.append(downloader.RemoteFile(
            url=url, folder=folder, name=path.rsplit("/", 1)[-1],
            size=int(item.get("size") or 0), headers=headers,
            label=f"{repo_id}/{path}"))

    meta = {
        "source": "huggingface",
        "url": f"https://huggingface.co/{repo_id}",
        "repo_id": repo_id, "revision": revision,
        "base_model": str(payload.get("base_model") or ""),
        "base_confidence": str(payload.get("base_confidence") or "unknown"),
        "license": str(payload.get("licence") or ""),
        "name": repo_id.rsplit("/", 1)[-1],
        "trained_words": payload.get("trained_words") or [],
    }
    return JSONResponse(models.enqueue_files(
        key=f"hf:{repo_id}@{revision}",
        label=f"HF · {repo_id}",
        files=remote,
        sidecars={f.name: meta for f in remote},
    ).public())


@app.post("/api/loras/import")
async def import_lora(payload: dict = Body(default={})) -> JSONResponse:
    """Copy a .safetensors the user already has into the LoRA folder.

    A path rather than an upload: this app is local, the file is already on the
    same disk, and a 500MB round trip through the browser to land two
    directories away would be pure ceremony. A folder imports everything in it,
    which is what someone who has been collecting LoRAs actually has.
    """
    payload = payload if isinstance(payload, dict) else {}
    raw = str(payload.get("path") or "").strip().strip('"')
    if not raw:
        raise HTTPException(400, "要先給一個檔案或資料夾的路徑")
    source = Path(raw).expanduser()
    if not source.exists():
        raise HTTPException(404, f"找不到：{source}")

    if source.is_dir():
        found = sorted(p for p in source.iterdir()
                       if p.suffix.lower() in (".safetensors", ".pt"))
        if not found:
            raise HTTPException(400, f"{source} 裡面沒有 .safetensors 檔案")
    else:
        if source.suffix.lower() not in (".safetensors", ".pt"):
            raise HTTPException(
                400,
                f"LoRA 要是 .safetensors 檔（你給的是 {source.suffix or '沒有副檔名'}）。"
                "如果你下載到的是 .zip，先解壓縮。")
        found = [source]

    target_dir = config.MODELS_DIR / "loras"
    target_dir.mkdir(parents=True, exist_ok=True)
    copied, skipped, failed = [], [], []
    for item in found:
        target = target_dir / item.name
        # Already there is not an error, and silently overwriting someone's file
        # because the names collide would be worse than saying so.
        if target.exists():
            skipped.append(item.name)
            continue
        try:
            # Copy, never move: the user's own copy stays where they put it.
            # Written beside the target first so a failure cannot leave a
            # half-file that ComfyUI would list and then choke on.
            part = target.with_name(target.name + ".part")
            shutil.copyfile(item, part)
            part.replace(target)
            copied.append(item.name)
        except OSError as exc:
            failed.append(f"{item.name}（{exc.strerror or exc}）")
            for leftover in (target_dir / (item.name + ".part"),):
                leftover.unlink(missing_ok=True)

    return JSONResponse({
        "copied": copied, "skipped": skipped, "failed": failed,
        "folder": str(target_dir),
        "loras": models.list_loras(),
    })


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
            # Held in a set until done: asyncio keeps only a weak reference to a
            # running task, so a bare create_task can be garbage-collected
            # mid-flight and the LoRA quietly installs with no cover image.
            task = asyncio.create_task(models.fetch_preview(folder, f.name, preview_url))
            _background.add(task)
            task.add_done_callback(_background.discard)
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
    layout = resolve_layout(cfg)
    if layout is None:
        raise ComfyError(f"不認識的分鏡：{cfg.get('layout')}")

    settings = images.ImageSettings.from_dict(cfg)
    rng = random.Random(record.seed)
    shared = prompts.expand(str(cfg.get("shared", "")), rng)
    raw_panels = list(cfg.get("panels") or [])
    raw_controls = list(cfg.get("controls") or [])
    # Each surviving crop is handed to ComfyUI once, up front. A crop that has
    # since been swept just leaves that panel unguided - the rest of the page
    # still keeps its composition.
    uploaded: dict[str, str] = {}
    if settings.controlnet:
        for name in dict.fromkeys(c for c in raw_controls if c):
            path = control_path(str(name))
            if path is None:
                continue
            try:
                uploaded[str(name)] = await client.upload_image(path.read_bytes(), str(name))
            except (OSError, ComfyError):
                continue
    # Whatever the crops did, say so on the finished card rather than in a
    # message the progress ticker overwrites two lines later.
    warning = ""
    if settings.controlnet and raw_controls and not uploaded:
        warning = "構圖參考圖已經過期，這一頁只照提詞畫。回「分鏡克隆」重讀一次原稿就會有。"
    elif settings.controlnet and len(uploaded) < len([c for c in raw_controls if c]):
        warning = "有幾格的構圖參考圖過期了，那幾格只照提詞畫。"

    panels: list[tuple[str, int, int, str]] = []
    for index, panel in enumerate(layout.panels):
        text = raw_panels[index] if index < len(raw_panels) else ""
        control = raw_controls[index] if index < len(raw_controls) else ""
        width, height = comics.panel_size(panel, layout.aspect)
        panels.append(
            (
                comics.scaffold(
                    prompts.expand(str(text), rng), shared,
                    model.positive_prefix if cfg.get("use_prefix", True) else "",
                ),
                width,
                height,
                uploaded.get(str(control), ""),
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
    if warning:
        record.message = warning


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
        source = config.STAGING_DIR / f"{record.id}.png"
        if not source.is_file():
            raise ComfyError("找不到剛才那張來源圖，請重新上傳一次")
        init_name = await client.upload_image(source.read_bytes(), f"{record.id}.png")

    control_name = ""
    if settings.controlnet and (record.settings or {}).get("control_image"):
        staged = config.STAGING_DIR / f"{record.id}-control.png"
        if not staged.is_file():
            raise ComfyError("找不到剛才那張構圖參考圖，請重新上傳一次")
        control_name = await client.upload_image(
            staged.read_bytes(), f"{record.id}-control.png"
        )

    graph = images.build(
        model,
        settings,
        prompt=expanded,
        negative=prompts.expand(record.negative, rng),
        seed=record.seed,
        width=record.width,
        height=record.height,
        init_image=init_name,
        control_image=control_name,
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
                "tag_style": model.tag_style,
                "artist_form": model.artist_form,
                "sizes": {k: list(v) for k, v in model.sizes.items()},
                "default_size": model.default_size,
                "nsfw_note": model.nsfw_note,
                "note": model.note,
                "civitai_bases": list(images.CIVITAI_BASES.get(model.id, ())),
                "custom": model.id.startswith(images.CUSTOM_PREFIX),
                # Where the weights come from, and - for CivitAI - whether the
                # user has the key that fetching them needs. Saying that on the
                # card beats a download that 401s after the user picked it.
                "source": model.source,
                "needs_civitai_key": bool(model.civitai_version) and not civitai.api_key(),
                "sha256": model.sha256,
                "checked": model.checked,
                # The checkpoint filename, so an image that names the model it
                # was made with can be matched back to an entry here.
                "file_name": model.file.name,
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
    if not model.downloadable:
        raise HTTPException(400, "自己裝的底模沒有下載來源")

    # A CivitAI checkpoint needs the user's key, and the key goes only to
    # civitai.com. The extra files (the SDXL VAE) still come from Hugging Face,
    # so they keep the plain URL and no auth - one model can span both hosts and
    # neither host gets the other's credentials.
    civitai_headers: tuple[tuple[str, str], ...] = ()
    if model.civitai_version:
        try:
            civitai_headers = tuple(civitai.download_headers().items())
        except civitai.NeedsApiKey as exc:
            raise HTTPException(400, str(exc)) from exc

    remote = []
    for f in model.all_files:
        if model.civitai_version and f is model.file:
            remote.append(downloader.RemoteFile(
                url=f"https://civitai.com/api/download/models/{model.civitai_version}",
                folder=f.folder, name=f.name, size=f.size,
                headers=civitai_headers, label=model.label))
        else:
            remote.append(downloader.RemoteFile(
                url=downloader.url_for(f), folder=f.folder, name=f.name, size=f.size))
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
            "短劇分頁「整集」那一格、或「模型」分頁，都可以下載它。",
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
        source = (config.STAGING_DIR / init_name).resolve()
        if config.STAGING_DIR.resolve() not in source.parents or not source.is_file():
            raise HTTPException(400, "找不到剛才上傳的來源圖，請重新放一次")
        source_name = init_name

    control_name = ""
    if settings.controlnet:
        if settings.controlnet not in installed_controlnets():
            raise HTTPException(
                400, f"還沒下載 ControlNet 模型 {settings.controlnet}，請到「模型」分頁下載"
            )
        raw_control = str(payload.get("control_image") or "")
        control = (config.STAGING_DIR / raw_control).resolve() if raw_control else None
        if control is None or config.STAGING_DIR.resolve() not in control.parents \
                or not control.is_file():
            raise HTTPException(400, "開了 ControlNet 就要放一張構圖參考圖")
        control_name = raw_control

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
        settings={**settings.to_dict(), "control_image": control_name},
    )
    if source_name:
        # The worker runs long after this request is gone, so the picture has to
        # be on disk under the job's own name rather than held in memory.
        (config.STAGING_DIR / f"{record.id}.png").write_bytes(source.read_bytes())
    if control_name:
        (config.STAGING_DIR / f"{record.id}-control.png").write_bytes(control.read_bytes())
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
    config.STAGING_DIR.mkdir(parents=True, exist_ok=True)
    # Staging files belong to nobody until a job claims a copy, so sweep the
    # ones an abandoned tab left behind rather than growing the folder forever.
    cutoff = time.time() - 24 * 3600
    for stale in config.STAGING_DIR.glob("src-*.png"):
        if stale.stat().st_mtime < cutoff:
            stale.unlink(missing_ok=True)
    Image.open(io.BytesIO(data)).convert("RGB").save(config.STAGING_DIR / name, "PNG")
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


def installed_controlnets() -> list[str]:
    folder = config.MODELS_DIR / "controlnet"
    if not folder.is_dir():
        return []
    return sorted(
        p.name for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in (".pth", ".safetensors", ".ckpt")
    )


@app.get("/api/controlnets")
async def list_controlnets() -> JSONResponse:
    here = set(installed_controlnets())
    out = [
        {
            "id": c.id, "label": c.label, "name": c.name, "best_for": c.best_for,
            "size": c.size, "installed": c.name in here, "union": c.union,
            "union_type": c.union_type,
        }
        for c in controlnets.CONTROLNETS
    ]
    # A file the user dropped in themselves is perfectly usable; we just do not
    # know whether it is a union model, so it is offered as a plain one.
    out += [
        {"id": "", "label": name, "name": name, "best_for": "你自己放進去的",
         "size": 0, "installed": True, "union": False, "union_type": ""}
        for name in sorted(here - {c.name for c in controlnets.CONTROLNETS})
    ]
    return JSONResponse(
        {
            "controlnets": out,
            "help": controlnets.HELP,
            "note": controlnets.NOTE,
            "union_types": list(controlnets.UNION_TYPES),
            "preprocessors": [{"id": k, "help": v}
                              for k, v in controlnets.PREPROCESSORS.items()],
        }
    )


@app.post("/api/updates/comfy/pull")
async def pull_comfy() -> JSONResponse:
    """The "在 ComfyUI 資料夾按 git pull" the update notice used to just tell you to do.

    update.bat deliberately never touches ComfyUI/ - that folder holds every
    model you downloaded - so the two are updated separately, and this is the
    other half.
    """
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, updates.pull, config.COMFY_DIR)
    result["dir"] = str(config.COMFY_DIR)
    result["note"] = (
        "ComfyUI 更新完要重開它才生效（關掉 ComfyUI 那個黑視窗，再跑一次 start.bat）。"
        if result["ok"] and result.get("before") != result.get("after") else ""
    )
    if not result["ok"]:
        raise HTTPException(400, result["detail"])
    return JSONResponse(result)


@app.get("/api/settings")
async def get_settings() -> JSONResponse:
    return JSONResponse({"settings": envfile.state(), "file": str(envfile.path())})


@app.post("/api/settings")
async def set_setting(payload: dict = Body(...)) -> JSONResponse:
    name = str((payload or {}).get("name", ""))
    if name not in envfile.WRITABLE:
        raise HTTPException(400, f"不能從網頁設定這個：{name}")
    try:
        envfile.write(name, str((payload or {}).get("value", "")))
    except (OSError, ValueError) as exc:
        raise HTTPException(400, f"寫不進 .env：{exc}")
    return JSONResponse({"settings": envfile.state(), "file": str(envfile.path()),
                         "needs_restart": envfile.WRITABLE[name]["restart"]})


@app.get("/api/packs")
async def list_packs() -> JSONResponse:
    """Every character pack, with whether its LoRA and its base model are here.

    The whole cast ships in one response - it is ~130KB for the Hololive pack
    and the picker has to be instant, so paging it would cost more than it saves.
    """
    here = {l["name"] for l in models.list_loras()}
    installed_ckpts = installed_checkpoints()
    out = []
    for pack in charpacks.PACKS:
        wanted = images.get(pack.wants_model) if pack.wants_model else None
        out.append({
            **pack.public(),
            "installed": pack.file in here,
            "model_installed": bool(wanted and image_status(wanted)["installed"]),
            "model_label": wanted.label if wanted else "",
            "checkpoints": installed_ckpts,
        })
    return JSONResponse({"packs": out, "help": charpacks.HELP,
                         "civitai_key": bool(civitai.api_key())})


def _as_float(value, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


@app.post("/api/packs/{pack_id}/prompt")
async def pack_prompt(pack_id: str, payload: dict = Body(default={})) -> JSONResponse:
    """One character in one outfit, assembled into a prompt ready to generate."""
    pack = charpacks.get(pack_id)
    if pack is None:
        raise HTTPException(404, f"不認識的角色包：{pack_id}")
    payload = payload if isinstance(payload, dict) else {}
    try:
        costume = int(payload.get("costume", 0))
    except (TypeError, ValueError):
        costume = 0
    # Which base model is selected changes the answer twice over: whether the
    # artist tag does anything, and which quality tags belong on the end.
    model_id = str(payload.get("model", "") or pack.wants_model)
    model = images.resolve(model_id, installed_checkpoints())
    built = charpacks.build_prompt(
        pack, str(payload.get("character", "")), costume,
        extra=str(payload.get("extra", "")),
        quality=payload.get("quality", True) is not False,
        model=model.id if model else "",
        style=bool(payload.get("style")),
        artist_weight=_as_float(payload.get("artist_weight"), 1.0),
        likeness=_as_float(payload.get("likeness"), 0.0),
        # `official art` is danbooru vocabulary, so it only belongs on a
        # checkpoint trained on danbooru captions.
        likeness_tags=(charpacks.LIKENESS_TAGS
                       if (model and model.tag_style == "danbooru") else ""),
        quality_tags=(model.positive_prefix if model and model.id != pack.wants_model else ""),
    )
    if built is None:
        raise HTTPException(404, f"這個角色包裡沒有：{payload.get('character')}")
    here = {l["name"] for l in models.list_loras()}
    built["lora_installed"] = pack.file in here
    return JSONResponse(built)


@app.get("/api/quicktags")
async def list_quicktags() -> JSONResponse:
    """The verified quick-pick tag list, with post counts and the corrections.

    Static data, so it ships whole and is filtered in the browser.
    """
    return JSONResponse(quicktags.public())


# -- style library: recipes, quality presets, merge, prompt doctor -----------


@app.get("/api/styles")
async def list_styles(model: str = "", tag_style: str = "") -> JSONResponse:
    """Every style recipe and quality preset, optionally filtered to one model.

    `tag_style` decides which spelling the one-click prompt uses: `danbooru` for
    the anime finetunes, `natural` for Juggernaut and SDXL base. When it is not
    given it is taken from the model, which is what the UI does.
    """
    if not tag_style:
        m = images.get(model) if model else None
        tag_style = m.tag_style if m else "danbooru"
    return JSONResponse(styles.public(model, tag_style))


@app.get("/api/styles/search")
async def search_styles(q: str = "", model: str = "", tag_style: str = "") -> JSONResponse:
    if not tag_style:
        m = images.get(model) if model else None
        tag_style = m.tag_style if m else "danbooru"
    hits = styles.search(q, model)
    return JSONResponse({"recipes": [r.public(tag_style) for r in hits], "query": q})


@app.post("/api/styles/apply")
async def apply_style(payload: dict) -> JSONResponse:
    """Merge a recipe or a quality preset into a prompt and return the diff.

    Nothing is written anywhere: the browser gets the merged prompt plus a list
    of what changed, and decides whether to accept it. That is the whole point of
    the diff - a one-click apply the user cannot see into is a one-click apply
    they stop trusting the second it eats a LoRA trigger.
    """
    prompt = str(payload.get("prompt") or "")
    negative = str(payload.get("negative") or "")
    model_id = str(payload.get("model") or "")
    replace = payload.get("replace_conflicts", True)
    m = images.get(model_id) if model_id else None
    tag_style = str(payload.get("tag_style") or (m.tag_style if m else "danbooru"))

    recipe_id = str(payload.get("recipe") or "")
    preset_id = str(payload.get("preset") or "")
    tags = payload.get("tags")

    if recipe_id:
        merged = promptmerge.apply_recipe(
            prompt, negative, recipe_id, model_id=model_id,
            tag_style=tag_style, replace_conflicts=bool(replace),
        )
        if merged is None:
            raise HTTPException(status_code=404, detail="沒有這個風格配方")
    elif preset_id:
        merged = promptmerge.apply_preset(prompt, negative, preset_id, model_id=model_id)
        if merged is None:
            raise HTTPException(status_code=404, detail="沒有這個品質預設")
    elif isinstance(tags, list):
        merged = promptmerge.merge(
            prompt, negative, [str(t) for t in tags],
            [str(t) for t in (payload.get("negative_tags") or [])],
            model_id=model_id, replace_conflicts=bool(replace),
        )
    else:
        raise HTTPException(status_code=400, detail="要給 recipe、preset 或 tags 其中一個")

    return JSONResponse(merged.public())


@app.post("/api/styles/remove")
async def remove_style_tags(payload: dict) -> JSONResponse:
    """The undo half: take a named set of tags back out of a prompt."""
    prompt = str(payload.get("prompt") or "")
    tags = [str(t) for t in (payload.get("tags") or [])]
    return JSONResponse({"prompt": promptmerge.remove_tags(prompt, tags)})


@app.post("/api/prompt/check")
async def check_prompt(payload: dict) -> JSONResponse:
    """Prompt health: canvas size, dialect, conflicts, duplicates.

    Runs on plain data with no model loaded, so it is cheap enough to call on
    every keystroke-debounce from the browser.
    """
    findings = promptdoctor.check(
        str(payload.get("prompt") or ""),
        str(payload.get("negative") or ""),
        model_id=str(payload.get("model") or ""),
        width=int(payload.get("width") or 0),
        height=int(payload.get("height") or 0),
    )
    return JSONResponse(promptdoctor.summary(findings))


# -- 短劇: shot lists, the format rules, and what to generate per shot --------
#
# The clip was never the hard part. An episode is a hundred clips that have to
# look like the same person in the same room, and that is bookkeeping. This
# group of endpoints is the bookkeeping - including which generation attempts
# belong to which shot, which is what turns a progress counter into a fact
# rather than a decoration.

DRAMAS = shortdrama.ProjectStore(config.OUTPUT_DIR / ".shortdrama.jsonl")


def _drama_installed() -> set[str]:
    return {m.id for m in registry.MODELS if models.model_status(m).get("installed")}


def _drama_jobs(project) -> dict:
    """The job records this project's shots refer to, for derived state.

    Read from the library rather than stored on the shot: a job can finish,
    fail or be deleted after the shot was saved, and a copy of its status would
    be the version the UI shows.
    """
    wanted: set[str] = set()
    for shot in project.shots:
        for stage in ("keyframe", "endframe", "video"):
            wanted.update(shot.jobs_for(stage))
            if shot.active_for(stage):
                wanted.add(shot.active_for(stage))
    return {j: lib.records[j] for j in wanted if j in lib.records}


def _drama_or_404(project_id: str):
    DRAMAS.load()
    project = DRAMAS.get(project_id)
    if project is None:
        raise HTTPException(404, "找不到這個短劇專案")
    return project


def _drama_payload(project) -> dict:
    jobs = _drama_jobs(project)
    findings = shortdrama.check(project, installed=_drama_installed())
    return {**project.public(jobs), "health": shortdrama.summary(findings),
            "jobs": {j: public(r) for j, r in jobs.items()}}


@app.get("/api/drama")
async def list_dramas() -> JSONResponse:
    DRAMAS.load()
    return JSONResponse({
        **shortdrama.public(),
        "projects": [p.public(_drama_jobs(p)) for p in DRAMAS.list()],
        "installed": sorted(_drama_installed()),
    })


@app.post("/api/drama")
async def create_drama(payload: dict = Body(default={})) -> JSONResponse:
    payload = payload if isinstance(payload, dict) else {}
    DRAMAS.load()
    project = DRAMAS.create(str(payload.get("title") or ""))
    DRAMAS.save()
    return JSONResponse(_drama_payload(project))


@app.get("/api/drama/{project_id}")
async def get_drama(project_id: str) -> JSONResponse:
    return JSONResponse(_drama_payload(_drama_or_404(project_id)))


@app.post("/api/drama/{project_id}")
async def update_drama(project_id: str, payload: dict = Body(default={})
                       ) -> JSONResponse:
    """Replace the spec, the cast and the shot list in one write.

    Whole-document, because the shot list is edited as a table and a partial
    update would need the browser and the server to agree on row identity. The
    generation bookkeeping is the exception: `keyframe_jobs`, `active_video` and
    their siblings are carried over from the stored shot by id and are never
    taken from the browser, so a stale table cannot wipe a finished render.
    """
    project = _drama_or_404(project_id)
    payload = payload if isinstance(payload, dict) else {}

    for key in ("title", "note"):
        if key in payload:
            setattr(project, key, str(payload[key] or ""))

    if isinstance(payload.get("delivery"), dict):
        d = payload["delivery"]
        project.delivery = shortdrama.DeliverySpec(
            width=max(1, int(d.get("width") or project.delivery.width)),
            height=max(1, int(d.get("height") or project.delivery.height)),
            fps=max(1, int(d.get("fps") or project.delivery.fps)),
            fit=(str(d.get("fit") or project.delivery.fit)
                 if str(d.get("fit") or project.delivery.fit) in assemble.FITS else ""))
    if isinstance(payload.get("keyframes"), dict):
        k = payload["keyframes"]
        want = str(k.get("model_id") or project.keyframes.model_id)
        if images.get(want) is None:
            raise HTTPException(400, f"沒有這個圖片底模：{want}")
        project.keyframes = shortdrama.KeyframeProfile(
            model_id=want,
            width=max(1, int(k.get("width") or project.keyframes.width)),
            height=max(1, int(k.get("height") or project.keyframes.height)),
            style_id=str(k.get("style_id") or ""))
    if isinstance(payload.get("routes"), dict):
        routes = {}
        for method, raw in payload["routes"].items():
            if method not in shortdrama.METHODS or not isinstance(raw, dict):
                continue
            model_id = str(raw.get("model_id") or "")
            if model_id and registry.get(model_id) is None:
                raise HTTPException(400, f"沒有這個影片模型：{model_id}")
            finish = raw.get("finish") or {}
            mode = str(finish.get("mode") or "native")
            if mode not in ("native", "interpolate", "retime", "manual"):
                raise HTTPException(400, f"不認識的收尾方式：{mode}")
            routes[method] = shortdrama.Route(
                model_id=model_id,
                finish=shortdrama.FinishPolicy(
                    mode=mode, factor=max(1, int(finish.get("factor") or 1)),
                    retime_audio=bool(finish.get("retime_audio"))))
        if routes:
            project.routes = routes

    if isinstance(payload.get("cast"), list):
        project.cast = [shortdrama.Character(
            key=str(c.get("key") or "").strip() or uuid.uuid4().hex[:6],
            name=str(c.get("name") or ""),
            gender=str(c.get("gender") or "female"),
            trigger=str(c.get("trigger") or ""), costume=str(c.get("costume") or ""),
            lora=str(c.get("lora") or ""), voice=str(c.get("voice") or ""),
            note=str(c.get("note") or ""),
        ) for c in payload["cast"] if isinstance(c, dict)]

    if isinstance(payload.get("shots"), list):
        keep = {s.id: s for s in project.shots if s.id}
        shots = []
        for raw in payload["shots"]:
            if not isinstance(raw, dict):
                continue
            prior = keep.get(str(raw.get("id") or ""))
            shots.append(shortdrama.Shot(
                id=str(raw.get("id") or ""), no=0,
                seconds=round(float(raw.get("seconds") or 3.2), 2),
                size=str(raw.get("size") or "近景"),
                who=[str(w) for w in (raw.get("who") or [])],
                speaker=str(raw.get("speaker") or ""),
                action=str(raw.get("action") or ""),
                motion=str(raw.get("motion") or ""),
                dialogue=str(raw.get("dialogue") or ""),
                method=str(raw.get("method") or "i2v"),
                scene=str(raw.get("scene") or ""),
                extra=str(raw.get("extra") or ""),
                note=str(raw.get("note") or ""),
            # Attempts and acceptances are never from the browser - they are
            # copied from the stored shot, every stage of them. See the
            # docstring, and Shot.carry_over for why it is a loop.
            ).carry_over(prior))
        project.shots = shots
        shortdrama.normalise(project)

    DRAMAS.save()
    return JSONResponse(_drama_payload(project))


@app.delete("/api/drama/{project_id}")
async def delete_drama(project_id: str) -> JSONResponse:
    DRAMAS.load()
    if not DRAMAS.delete(project_id):
        raise HTTPException(404, "找不到這個短劇專案")
    DRAMAS.save()
    return JSONResponse({"ok": True})


def _shot_or_404(project, shot_id: str):
    shot = project.shot(shot_id)
    if shot is None:
        raise HTTPException(404, "這個專案沒有這顆鏡頭")
    return shot


@app.get("/api/drama/{project_id}/shot/{shot_id}")
async def drama_shot(project_id: str, shot_id: str) -> JSONResponse:
    """The keyframe prompt and the ordered plan for one shot."""
    project = _drama_or_404(project_id)
    shot = _shot_or_404(project, shot_id)
    built = shortdrama.keyframe_prompt(project, shot)
    model = images.get(project.keyframes.model_id)
    if project.keyframes.style_id:
        merged = promptmerge.apply_recipe(
            built["prompt"], "", project.keyframes.style_id,
            model_id=project.keyframes.model_id,
            tag_style=model.tag_style if model else "danbooru")
        if merged is not None:
            built["prompt"] = merged.prompt
            built["negative"] = merged.negative
    jobs = _drama_jobs(project)
    return JSONResponse({**built, "shot": shot.public(),
                         "state": shortdrama.shot_state(shot, jobs),
                         "plan": shortdrama.shot_plan(project, shot),
                         # What the video step will actually be told, and
                         # whether that is the motion field or a fallback to the
                         # keyframe's description. The browser should not have
                         # to re-derive a rule that lives in shortdrama.py.
                         "video": shortdrama.video_prompt(shot)})


RUNS = runner_mod.Runs(config.OUTPUT_DIR / ".drama-run.json")
RUNS.load()


def _drama_models(project) -> list[dict]:
    """Every model this episode needs, and whether it is actually on disk.

    The drama page used to report a missing model once per shot, as twenty
    identical failures with a filename in them and no way to act - the user
    had to work out which tab to go to and which of forty entries it was. The
    same information belongs here, once, with the button attached.
    """
    out: list[dict] = []
    image_model = images.get(project.keyframes.model_id)
    if image_model is not None:
        state = image_status(image_model)
        out.append({
            "kind": "image", "id": image_model.id, "label": image_model.label,
            "for": "關鍵幀",
            "installed": state["installed"],
            "missing": state["missing"][:3],
            "bytes": sum(f.size for f in image_model.all_files),
            "downloadable": bool(getattr(image_model, "downloadable", True)),
        })
    for method in sorted(project.methods_used):
        route = project.route(method)
        model = registry.get(route.model_id) if route else None
        if model is None:
            continue
        state = models.model_status(model)
        out.append({
            "kind": "video", "id": model.id, "label": model.label,
            "for": shortdrama.METHODS[method].zh,
            "installed": state["installed"],
            "missing": (state.get("missing") or [])[:3],
            "bytes": sum(f.size for f in model.all_files),
            "downloadable": True,
            "runnable_here": model.runnable or bool(
                wfimport.load(config.WORKFLOWS_DIR, model.id)),
        })
    # One entry per model: a project with four methods on one model should not
    # offer the same download four times.
    seen, unique = set(), []
    for entry in out:
        if (entry["kind"], entry["id"]) in seen:
            continue
        seen.add((entry["kind"], entry["id"]))
        unique.append(entry)
    return unique



@app.get("/api/drama/{project_id}/run")
async def run_status(project_id: str) -> JSONResponse:
    """What a run would do, and what one in flight has done so far."""
    project = _drama_or_404(project_id)
    jobs = _drama_jobs(project)
    # Only this project's run. The runner holds one at a time, and showing
    # another project's summary under these shots would be a lie about what
    # was queued - it was the first thing this panel got wrong.
    current = RUNS.current
    mine = current is not None and current.project == project_id
    return JSONResponse({
        "run": current.public() if mine else {"active": False},
        "other_run": (current.public() if current is not None and not mine
                      else None),
        "keyframe_todo": [s.no for s in runner_mod.shots_needing(project, jobs, "keyframe")],
        "video_todo": [s.no for s in runner_mod.shots_needing(project, jobs, "video")],
        "video_blocked": runner_mod.blocked_reason(project, jobs, "video"),
        "max_per_run": runner_mod.MAX_PER_RUN,
        # What this episode needs on disk, with enough for the page to offer
        # the download itself instead of sending the user to another tab.
        "models": _drama_models(project),
    })


@app.post("/api/drama/{project_id}/run/stop")
async def run_stop(project_id: str) -> JSONResponse:
    _drama_or_404(project_id)
    return JSONResponse({"stopped": RUNS.stop(), "run": RUNS.public()})


@app.post("/api/drama/{project_id}/run")
async def run_episode(project_id: str, payload: dict = Body(default={})) -> JSONResponse:
    """Queue one pass over the whole episode.

    Deliberately two passes rather than one: keyframes, then the user picks,
    then videos. See runner.py for why nothing is accepted automatically.
    """
    project = _drama_or_404(project_id)
    payload = payload if isinstance(payload, dict) else {}
    stage = str(payload.get("stage") or "keyframe")
    if stage not in ("keyframe", "video"):
        raise HTTPException(400, f"不認識的階段：{stage}")
    if RUNS.current and RUNS.current.active:
        raise HTTPException(409, "已經有一輪在排了。等它排完，或按「停止」。")

    per_shot = max(1, min(int(payload.get("per_shot") or 2), 4))
    jobs = _drama_jobs(project)
    if reason := runner_mod.blocked_reason(project, jobs, stage):
        raise HTTPException(400, reason)
    # A missing model is one problem, not twenty. Reporting it per shot was
    # technically accurate and completely useless: the same sentence repeated,
    # with a filename in it, and nothing to press.
    want = "image" if stage == "keyframe" else "video"
    absent = [m for m in _drama_models(project)
              if m["kind"] == want and not m["installed"]]
    if absent:
        raise HTTPException(
            400,
            f"{absent[0]['label'].split('—')[0].strip()} 還沒下載完，"
            f"所以現在生不出東西。下面那顆「下載」按鈕可以直接下載"
            f"（{absent[0]['bytes'] / 1e9:.1f}GB），下載完再按一次。")
    # Downloaded but with no graph this app can drive is a different problem
    # with a different fix, and it was surfacing once per shot as a sentence
    # that got cut off before the part explaining what to do.
    # A model that has no such mode can never work - not by downloading, not by
    # importing a graph - so it is checked before either of those.
    if want == "video":
        for method in sorted(project.methods_used):
            route = project.route(method)
            model = registry.get(route.model_id) if route else None
            if model is None or not model.methods or method in model.methods:
                continue
            can = "、".join(shortdrama.METHODS[m].zh for m in model.methods
                            if m in shortdrama.METHODS)
            raise HTTPException(
                400,
                f"「{shortdrama.METHODS[method].zh}」這條路線指到 "
                f"{model.label.split('—')[0].strip()}，但這個模型沒有這種模式"
                f"（它只能做：{can}）。到第 0 步把這條路線換成別的模型。")

    ungraphed = [m for m in _drama_models(project)
                 if m["kind"] == want and m["installed"]
                 and m.get("runnable_here") is False]
    if ungraphed:
        raise HTTPException(
            400,
            f"{ungraphed[0]['label'].split('—')[0].strip()} 的檔案下載好了，"
            "但這個 app 沒有可以跑它的工作流。下面那顆「去匯入官方工作流」"
            "會帶你到匯入的地方（模型也幫你選好）—— "
            "在 ComfyUI 用官方範本跑一次確認會動，Workflow → Export (API) "
            "存出 .json，匯進來之後這一頁就能用它生成。")
    todo = runner_mod.shots_needing(project, jobs, stage)
    if not todo:
        raise HTTPException(
            400, "每顆鏡頭都已經有採用的" + ("影片" if stage == "video" else "關鍵幀") + "了。")
    if len(todo) * per_shot > runner_mod.MAX_PER_RUN:
        raise HTTPException(
            400,
            f"{len(todo)} 顆鏡頭 × 一次 {per_shot} 個 = {len(todo) * per_shot} 個工作，"
            f"超過一輪的上限 {runner_mod.MAX_PER_RUN}。把「一次幾個」調低，"
            "或分批跑。")

    # Freeze the plan before submitting anything. A run lasts as long as
    # generating does, and editing shot 12 halfway through must not mean the
    # first half of the episode used one version of the project and the second
    # half another, with nothing recording it.
    tasks, refusals = _plan_run(project, jobs, stage, per_shot)
    if not tasks:
        raise HTTPException(
            400,
            "這一輪沒有可以排的工作。" + (refusals[0].reason if refusals else ""))

    run = RUNS.start(project.id, stage, per_shot, tasks)
    # Shots that cannot run are known now, not twenty minutes in.
    run.failures.extend(refusals)
    RUNS.save()
    asyncio.create_task(_drive_run(project.id, run))
    return JSONResponse({"run": run.public()})


def _plan_run(project, jobs: dict, stage: str, per_shot: int
              ) -> tuple[list, list]:
    """Build every task's payload up front, and collect what cannot be built.

    Doing it here rather than at submission time means a shot that can never
    work - no motion written, a route this app has no graph for - is reported
    the moment the button is pressed, instead of after the shots before it have
    already taken twenty minutes of GPU.
    """
    tasks, refusals = [], []
    for shot in runner_mod.shots_needing(project, jobs, stage):
        try:
            payload = (_keyframe_payload(project, shot) if stage == "keyframe"
                       else _video_payload(project, jobs, shot))
        except HTTPException as exc:
            refusals.append(runner_mod.Failure(shot.no, str(exc.detail)))
            continue
        for _ in range(per_shot):
            tasks.append(runner_mod.Task(shot.id, shot.no, stage, dict(payload)))
    return tasks, refusals


async def _drive_run(project_id: str, run) -> None:
    """Submit the frozen plan, recording what fails instead of stopping.

    One shot failing is not a reason to abandon the other nineteen - and the
    reason it failed is usually the same for all of them, which is much easier
    to see from a list at the end than from one error and silence.

    Jobs go in a few at a time rather than all at once. There is one worker, so
    a full queue is not faster; it only means someone who wants to try a single
    shot waits behind the whole episode, and that "stop" arrives too late to
    stop anything.

    The project is read only to record job ids against shots. Everything the
    jobs are made from was decided in `_plan_run`, so an edit made while this
    is running lands on the next run, not on the second half of this one.
    """
    submitted: list[str] = []
    refused: set[str] = set()
    for task in run.tasks:
        if run.stopped:
            break
        # A shot that already failed does not get its remaining candidates
        # attempted: the reason is the same every time, and three copies of it
        # in the failure list tell the user nothing extra.
        if task.shot_id in refused:
            continue
        project = DRAMAS.get(project_id)
        if project is None:
            run.message = "專案不見了。"
            break
        await _wait_for_room(run, submitted)
        if run.stopped:
            break
        try:
            job_id = await (_queue_keyframe(task.payload) if task.stage == "keyframe"
                            else _queue_video(task.payload))
        except HTTPException as exc:
            run.failures.append(runner_mod.Failure(task.shot_no, str(exc.detail)))
            refused.add(task.shot_id)
            RUNS.save()
            continue
        except Exception as exc:                                  # noqa: BLE001
            run.failures.append(runner_mod.Failure(task.shot_no, str(exc)))
            refused.add(task.shot_id)
            RUNS.save()
            continue
        submitted.append(job_id)
        shot = project.shot(task.shot_id)
        if shot is not None:
            attempts = shot.jobs_for(task.stage)
            if job_id not in attempts:
                attempts.append(job_id)
            DRAMAS.save()
        run.queued += 1
        RUNS.save()
    run.finished = time.time()
    if not run.message:
        run.message = (f"這一輪送了 {run.queued} 個工作"
                       + (f"，其中 {len(run.failures)} 顆有問題" if run.failures else "")
                       + "。到每顆鏡頭挑一個採用。")
    RUNS.save()


async def _wait_for_room(run, submitted: list[str]) -> None:
    """Block until fewer than WINDOW of this run's jobs are still unfinished.

    Counts only jobs this run submitted. A job the user started by hand is
    their business, and stalling the episode because of it would be wrong -
    though it does share the same single worker, so it will be waited on
    anyway, just not counted against the window.
    """
    waited = 0.0
    while not run.stopped:
        pending = 0
        for job_id in submitted:
            record = lib.get(job_id)
            if record is not None and record.status in ("queued", "running"):
                pending += 1
        if pending < runner_mod.WINDOW:
            return
        if waited > runner_mod.SLOT_TIMEOUT_SECONDS:
            # A job that never finishes would otherwise leave this loop running
            # for as long as the app does. Stopping says so; carrying on would
            # mean quietly abandoning the window and flooding the queue.
            run.stopped = True
            run.message = ("等了很久前面的工作都沒有跑完，這一輪先停下來。"
                           "到素材庫看看是不是有工作卡住了。")
            RUNS.save()
            return
        await asyncio.sleep(runner_mod.POLL_SECONDS)
        waited += runner_mod.POLL_SECONDS


def _keyframe_payload(project, shot) -> dict:
    """Everything one keyframe job needs, resolved now rather than at submit.

    The style recipe is merged here too: a recipe swapped mid-run would
    otherwise apply to the back half of the episode only.
    """
    built = shortdrama.keyframe_prompt(project, shot)
    model = images.get(project.keyframes.model_id)
    if project.keyframes.style_id:
        merged = promptmerge.apply_recipe(
            built["prompt"], "", project.keyframes.style_id,
            model_id=project.keyframes.model_id,
            tag_style=model.tag_style if model else "danbooru")
        if merged is not None:
            built["prompt"], built["negative"] = merged.prompt, merged.negative
    return {
        "model": project.keyframes.model_id,
        "prompt": built["prompt"], "negative": built.get("negative") or "",
        "width": project.keyframes.width, "height": project.keyframes.height,
        "batch": 1, "seed": -1,
        "loras": [{"name": n, "strength": 1.0, "strength_clip": 1.0}
                  for n in built.get("loras") or []],
    }


async def _queue_keyframe(payload: dict) -> str:
    """Submit one frozen keyframe payload through the ordinary image path."""
    response = await image_generate(dict(payload))
    return json.loads(bytes(response.body))["id"]


def _video_payload(project, jobs: dict, shot) -> dict:
    """Everything one video job needs, including which file it starts from.

    The source is pinned to the accepted keyframe *as it is now*. Accepting a
    different take while the run is going changes the next run, not this one.
    """
    method = shortdrama.METHODS.get(shot.method)
    route = project.route(shot.method)
    model = registry.get(route.model_id) if route else None
    end_name = ""
    if method is not None and method.needs_endframe:
        # Only a model that actually takes two pictures may run this. Sending
        # just the first frame would produce a perfectly good video that is not
        # the one asked for, and nothing downstream would notice.
        if model is None or (model.methods and "flf" not in model.methods):
            raise HTTPException(
                400,
                f"「首尾幀」這條路線指到 {(model.label if model else route.model_id if route else '?')}"
                "，但它吃不了第二張圖。目前只有 MiniMax H3 做得到首尾幀 —— "
                "到第 0 步把這條路線改成它，或把這顆改成「圖生影片」。")
        end_id = shot.active_for("endframe")
        end_rec = jobs.get(end_id) if end_id else None
        end_out = getattr(end_rec, "output", None) if end_rec else None
        if not end_out or not (config.OUTPUT_DIR / end_out).is_file():
            raise HTTPException(
                400,
                "「首尾幀」還缺最後一張圖 —— 這顆鏡頭要先採用一張<b>結束幀</b>。"
                "在這顆鏡頭的面板裡生一張或上傳一張，採用它之後再排影片。")
        end_name = end_out
    job_id = shot.active_for("keyframe")
    record = jobs.get(job_id) if job_id else None
    output = getattr(record, "output", None) if record else None
    path = (config.OUTPUT_DIR / output) if output else None
    if not path or not path.is_file():
        raise HTTPException(400, "找不到採用的關鍵幀檔案")
    motion = shortdrama.video_prompt(shot)["prompt"]
    if not motion:
        raise HTTPException(400, "還沒填「影片怎麼動」")
    if route is None:
        raise HTTPException(400, f"「{shot.method}」沒有設定路線")
    return {"source": output, "prompt": motion, "model": route.model_id,
            "seconds": shot.seconds, "end_source": end_name}


async def _queue_video(payload: dict) -> str:
    """Submit one frozen video payload through the ordinary video path."""
    path = config.OUTPUT_DIR / str(payload.get("source") or "")
    if not path.is_file():
        # The file was there when the run was planned. Someone has cleared the
        # library since, and saying so beats a failure from inside ffmpeg.
        raise HTTPException(400, "採用的關鍵幀檔案在這一輪開始之後不見了")

    class _Upload:
        """The shape /api/generate's UploadFile parameter is used through."""

        def __init__(self, where):
            self.path = where
            self.filename = where.name

        async def read(self) -> bytes:
            return self.path.read_bytes()

    end = str(payload.get("end_source") or "")
    end_path = (config.OUTPUT_DIR / end) if end else None
    if end and (end_path is None or not end_path.is_file()):
        raise HTTPException(400, "採用的結束幀在這一輪開始之後不見了")

    response = await generate(
        image=_Upload(path),
        end_image=_Upload(end_path) if end_path else None,
        prompt=str(payload.get("prompt") or ""),
        model=str(payload.get("model") or ""),
        seconds=float(payload.get("seconds") or 0.0), seed=-1)
    return json.loads(bytes(response.body))["id"]


@app.get("/api/drama/{project_id}/assemble")
async def assemble_status(project_id: str) -> JSONResponse:
    """Can this project be joined into one file yet, and with what."""
    project = _drama_or_404(project_id)
    jobs = _drama_jobs(project)
    ready, missing = _assemble_segments(project, jobs)
    ffmpeg = assemble.find_ffmpeg(config.REPO_DIR)
    ffprobe = assemble.find_ffprobe(ffmpeg)
    # Measuring is a subprocess per shot, so it happens off the event loop and
    # only when there is a plausible chance of joining.
    if ready and ffmpeg and not missing:
        await asyncio.to_thread(_measure, ready, ffmpeg, ffprobe)
    odd = assemble.off_ratio(ready, project.delivery.width, project.delivery.height)
    unknown = assemble.unmeasured(ready)
    can = bool(ready) and not missing and bool(ffmpeg) and not (
        odd and not project.delivery.fit)
    return JSONResponse({
        "ready": [s.public() for s in ready],
        "missing": missing,
        "can": can,
        "ffmpeg": ffmpeg,
        "ffmpeg_version": assemble.version(ffmpeg) if ffmpeg else "",
        "ffprobe": ffprobe,
        "ffprobe_version": assemble.version(ffprobe) if ffprobe else "",
        "how_to_get": "" if ffmpeg else assemble.HOW_TO_GET,
        "delivery": project.delivery.public(),
        # The shape question, and whether it has been answered.
        "off_ratio": odd,
        "unmeasured": unknown,
        "fit": project.delivery.fit,
        "fit_options": assemble.FITS,
        "needs_fit": bool(odd) and not project.delivery.fit,
    })


def _measure(segments: list, ffmpeg: str, ffprobe: str) -> None:
    """Fill in what each accepted file actually is. Blocking; run in a thread."""
    for segment in segments:
        if segment.media is None:
            try:
                segment.media = assemble.probe_cached(
                    segment.path, ffprobe=ffprobe, ffmpeg=ffmpeg)
            except assemble.AssembleError:
                segment.media = None


def _assemble_segments(project, jobs) -> tuple[list, list[int]]:
    """The accepted videos in shot order, and which shots have none.

    Order is the shot list's, not the library's: a shot regenerated later is
    still the same shot, and sorting by creation time would silently reorder
    the episode.
    """
    ready, missing = [], []
    for shot in project.shots:
        job_id = shot.active_for("video")
        record = jobs.get(job_id) if job_id else None
        output = getattr(record, "output", None) if record else None
        path = (config.OUTPUT_DIR / output) if output else None
        if path and path.is_file():
            ready.append(assemble.Segment(path, shot.seconds, shot.no))
        else:
            missing.append(shot.no)
    return ready, missing


@app.post("/api/drama/{project_id}/assemble")
async def assemble_episode(project_id: str, payload: dict = Body(default={})) -> JSONResponse:
    """Join every accepted shot into one playable file."""
    project = _drama_or_404(project_id)
    payload = payload if isinstance(payload, dict) else {}
    jobs = _drama_jobs(project)
    ready, missing = _assemble_segments(project, jobs)
    if missing:
        raise HTTPException(
            400,
            f"還有 {len(missing)} 顆鏡頭沒有採用的影片"
            f"（第 {'、'.join(str(n) for n in missing[:8])} 顆"
            + ("…" if len(missing) > 8 else "") + "）。每一顆都要先採用一支。")
    if not ready:
        raise HTTPException(400, "這個專案還沒有鏡頭。")
    ffmpeg = assemble.find_ffmpeg(config.REPO_DIR)
    if not ffmpeg:
        raise HTTPException(400, assemble.HOW_TO_GET)
    ffprobe = assemble.find_ffprobe(ffmpeg)

    # A fit sent with the press is the user answering the question below, so it
    # is remembered rather than applied once and forgotten.
    if str(payload.get("fit") or "") in assemble.FITS:
        project.delivery.fit = str(payload["fit"])
        DRAMAS.save()

    await asyncio.to_thread(_measure, ready, ffmpeg, ffprobe)
    odd = assemble.off_ratio(ready, project.delivery.width, project.delivery.height)
    if odd and not project.delivery.fit:
        # Both answers lose something, so this is not a default to pick quietly:
        # one crops faces out of frame, the other adds bars. The user chooses
        # once and the choice is kept.
        raise HTTPException(
            400,
            f"有 {len(odd)} 顆鏡頭的比例跟交付尺寸不一樣"
            f"（第 {'、'.join(str(n) for n in odd[:6])} 顆）。"
            f"要「{assemble.FITS['cover']}」還是「{assemble.FITS['contain']}」？"
            "在下面選一個再按一次。")
    fit = project.delivery.fit or "contain"

    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=ASSEMBLY_MODEL_ID,
        prompt=f"{project.title or '短劇'} 完整成品".strip(),
        kind="video",
        status="running",
        source_name=project.title,
        width=project.delivery.width, height=project.delivery.height,
        fps=project.delivery.fps,
        created=time.time(),
        # Enough provenance to answer "where did this come from" a month later,
        # without needing the project to still exist in the same shape.
        settings={
            "origin": "assemble", "project": project.id,
            "project_title": project.title,
            "shots": len(ready),
            "shot_numbers": [s.shot_no for s in ready],
            "sources": [s.path.name for s in ready],
            "fit": fit,
            "ffmpeg": assemble.version(ffmpeg),
            "ffprobe": assemble.version(ffprobe),
            "measured": bool(ffprobe),
        },
    )
    lib.add(record)

    def progress(value: float, message: str) -> None:
        record._progress = value
        record.message = message

    try:
        result = await asyncio.to_thread(
            assemble.build, ready,
            config.OUTPUT_DIR / f"{record.id}.mp4",
            width=project.delivery.width, height=project.delivery.height,
            fps=project.delivery.fps, ffmpeg=ffmpeg, ffprobe=ffprobe,
            fit=fit,
            workdir=config.OUTPUT_DIR / ".assemble" / record.id,
            on_progress=progress)
    except assemble.AssembleError as exc:
        record.status = "error"
        record.message = str(exc)
        lib.save()
        raise HTTPException(400, str(exc)) from exc

    record.status = "done"
    record.message = ""
    record._progress = 1.0
    record.outputs = [result["file"]]
    record.output = result["file"]
    record.length = int(result["seconds"] * project.delivery.fps)
    record.finished = time.time()
    record.settings = {**record.settings, **result}
    lib.save()
    return JSONResponse({"job": record.id, **result})


@app.post("/api/drama/{project_id}/shot/{shot_id}/upload")
async def drama_upload(project_id: str, shot_id: str,
                       image: UploadFile,
                       stage: str = Form("keyframe")) -> JSONResponse:
    """Use a picture the user already has as this shot's keyframe.

    The gap this closes: the drama tab could only ever *generate* a keyframe,
    so "I already have the shot I want" had nowhere to go - which is image-to-
    video's most natural use.

    The upload becomes a real library record rather than a path stored on the
    shot. That keeps one source of truth: `shot_state` computes progress by
    joining attempts against the library, and a second kind of attempt that
    lived somewhere else would need every one of those paths to learn about it.
    """
    project = _drama_or_404(project_id)
    shot = _shot_or_404(project, shot_id)
    if stage not in ("keyframe", "endframe"):
        # Not "video": an uploaded clip has no frames this app produced and
        # nothing downstream can re-derive, and letting one in would make
        # "已採用影片" mean two different things. Audio has its own endpoint,
        # because it is not an image and must not be run through PIL.
        raise HTTPException(400, f"只能匯入關鍵幀或結束幀，不能匯入 {stage}")

    data = await image.read()
    if not data:
        raise HTTPException(400, "圖片是空的")
    if len(data) > MAX_IMPORT_BYTES:
        raise HTTPException(
            400, f"檔案太大（{len(data)/1e6:.0f}MB）。上限是 "
                 f"{MAX_IMPORT_BYTES//1_000_000}MB —— 關鍵幀不需要這麼大。")
    try:
        probe = Image.open(io.BytesIO(data))
        probe.verify()
        opened = Image.open(io.BytesIO(data))
        pixels = opened.size[0] * opened.size[1]
        if pixels > MAX_IMPORT_PIXELS:
            raise HTTPException(
                400, f"這張圖 {opened.size[0]}×{opened.size[1]}，像素太多。"
                     f"上限約 {MAX_IMPORT_PIXELS//1_000_000} 百萬像素。")
        # EXIF orientation is a real trap: a phone photo can be stored
        # landscape with a "rotate me" tag, and PIL ignores it unless asked.
        # The video model would then animate a sideways picture.
        opened = ImageOps.exif_transpose(opened)
        had_alpha = opened.mode in ("RGBA", "LA", "P")
        mode_was = opened.mode
        if had_alpha:
            # Flattening onto black is a choice, not a no-op: `.convert("RGB")`
            # would do it silently and the user would wonder where the
            # transparent background went.
            flat = Image.new("RGB", opened.size, (0, 0, 0))
            alpha = opened.convert("RGBA").split()[-1]
            flat.paste(opened.convert("RGB"), mask=alpha)
            opened = flat
        else:
            # Covers CMYK JPEGs and greyscale, both of which reach here.
            opened = opened.convert("RGB")
        width, height = opened.size
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(400, "無法辨識這個圖片格式。JPG / PNG / WebP 都可以。")

    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=UPLOAD_MODEL_ID,
        prompt=f"（匯入的圖片）{image.filename or ''}".strip(),
        kind="image",
        status="done",
        source_name=image.filename or "upload",
        width=width, height=height,
        created=time.time(),
        finished=time.time(),
        # `kind` means media type, not how it was obtained - the gallery and the
        # job filters both branch on it - so the origin lives in settings.
        settings={"origin": "upload",
                  "original_filename": image.filename or "",
                  "original_mode": mode_was,
                  "import_stage": stage},
    )
    name = f"{record.id}.png"
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Re-encoded rather than stored as uploaded, which drops EXIF, GPS and XMP
    # along the way. A holiday photo should not carry its coordinates into a
    # folder the user will later share.
    clean = Image.new("RGB", opened.size)
    clean.putdata(list(opened.getdata()))
    clean.save(config.OUTPUT_DIR / name, "PNG")
    opened = clean
    record.outputs = [name]
    record.output = name
    thumb = opened.copy()
    thumb.thumbnail((480, 480))
    record.thumb = f"{record.id}.jpg"
    lib.thumbs.mkdir(parents=True, exist_ok=True)
    thumb.convert("RGB").save(lib.thumbs / record.thumb, "JPEG", quality=84)
    lib.add(record)

    attempts = shot.jobs_for(stage)
    if record.id not in attempts:
        attempts.append(record.id)
    # Accepted only when nothing was accepted yet. Choosing the file is a
    # deliberate act, so the first import needs no second confirmation - but
    # silently replacing a take the user already picked is the "progress that
    # fills itself in" failure this page was built to avoid.
    replaced = bool(shot.active_for(stage))
    if not replaced:
        shot.set_active(stage, record.id)
    DRAMAS.save()

    # The video model's output follows the ratio of the still it is handed, so a
    # picture that is not the delivery shape is worth saying so about now rather
    # than after twenty shots have been generated from it.
    delivery = project.delivery
    note = ""
    if width and height and delivery.ratio:
        ratio = width / height
        if abs(ratio - delivery.ratio) > shortdrama.VERTICAL_TOLERANCE:
            note = (f"這張圖是 {width}×{height}（比例 {ratio:.3f}），"
                    f"交付是 {delivery.ratio:.3f}。影片會照這張圖的比例出來，"
                    f"所以之後得再裁掉一部分。")
    if replaced:
        note = ("這顆鏡頭已經有採用的" + ("結束幀" if stage == "endframe" else "關鍵幀")
                + "了，所以這張先放著沒有取代它 —— 要換的話按它下面的「採用這個」。"
                + ("　" + note if note else ""))
    if had_alpha:
        note = ("原圖有透明背景，已經填成黑色（不然影片模型會拿到一塊沒定義的區域）。"
                + ("　" + note if note else ""))
    return JSONResponse({**_drama_payload(project), "imported": record.id,
                         "accepted": not replaced, "note": note})


AUDIO_SUFFIXES = (".wav", ".mp3", ".flac", ".m4a", ".ogg", ".opus")
MAX_AUDIO_BYTES = 60_000_000


@app.post("/api/drama/{project_id}/shot/{shot_id}/audio")
async def drama_audio(project_id: str, shot_id: str,
                      audio: UploadFile) -> JSONResponse:
    """Attach a sound file to a shot, for the routes that take one.

    S2V and MiniMax H3 are audio-driven: the sound is an *input*, and the lip
    movement is generated to match it. So the file has to reach the shot before
    the video is generated, not be laid over it afterwards.

    Uploaded rather than generated: this app has no text-to-speech, and has
    never run one. See docs for the candidates.
    """
    project = _drama_or_404(project_id)
    shot = _shot_or_404(project, shot_id)
    name = audio.filename or "audio"
    if not name.lower().endswith(AUDIO_SUFFIXES):
        raise HTTPException(
            400, f"要是聲音檔（{'、'.join(AUDIO_SUFFIXES)}），你給的是 {name}")
    data = await audio.read()
    if not data:
        raise HTTPException(400, "這個檔案是空的")
    if len(data) > MAX_AUDIO_BYTES:
        raise HTTPException(
            400, f"檔案太大（{len(data)/1e6:.0f}MB）。一句台詞不會這麼大。")

    record = library.Record(
        id=uuid.uuid4().hex[:12],
        model_id=UPLOAD_MODEL_ID,
        prompt=f"（匯入的音檔）{name}",
        kind="audio",
        status="done",
        source_name=name,
        created=time.time(), finished=time.time(),
        settings={"origin": "upload", "original_filename": name,
                  "import_stage": "audio"},
    )
    suffix = Path(name).suffix.lower()
    stored = f"{record.id}{suffix}"
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (config.OUTPUT_DIR / stored).write_bytes(data)
    record.outputs = [stored]
    record.output = stored
    lib.add(record)

    attempts = shot.jobs_for("audio")
    if record.id not in attempts:
        attempts.append(record.id)
    if not shot.active_for("audio"):
        shot.set_active("audio", record.id)
    DRAMAS.save()

    note = ""
    if shot.method != "s2v" and not shot.dialogue:
        note = ("這顆鏡頭的生成方式不是「說話（音訊驅動）」，"
                "所以這個音檔目前只會被記著，不會進生成 —— "
                "要讓它驅動口型，把生成方式改成 S2V。")
    return JSONResponse({**_drama_payload(project), "imported": record.id,
                         "note": note})


@app.post("/api/drama/{project_id}/shot/{shot_id}/attach")
async def drama_attach(project_id: str, shot_id: str,
                       payload: dict = Body(default={})) -> JSONResponse:
    """Record that a generation job belongs to this shot at this stage.

    The job is created by the ordinary image/video endpoints - this app has one
    generator and it stays that way - and then pointed at here. Recording the
    link rather than the result is deliberate: the shot keeps a list of attempts
    and their status is read back from the library, so a job that fails or is
    deleted later cannot leave the shot claiming to be finished.
    """
    project = _drama_or_404(project_id)
    shot = _shot_or_404(project, shot_id)
    payload = payload if isinstance(payload, dict) else {}
    stage = str(payload.get("stage") or "")
    job_id = str(payload.get("job") or "")
    if stage not in ("keyframe", "endframe", "video", "audio"):
        raise HTTPException(400, f"不認識的階段：{stage}")
    if job_id not in lib.records:
        raise HTTPException(404, "找不到這個生成工作")
    attempts = shot.jobs_for(stage)
    if job_id not in attempts:
        attempts.append(job_id)
    DRAMAS.save()
    return JSONResponse(_drama_payload(project))


@app.post("/api/drama/{project_id}/shot/{shot_id}/accept")
async def drama_accept(project_id: str, shot_id: str,
                       payload: dict = Body(default={})) -> JSONResponse:
    """Mark one attempt as the take that counts. Only this makes a shot done.

    Nothing is accepted automatically. The last job to finish is not the one the
    user picked, and a progress bar that fills itself in is a progress bar that
    lies.
    """
    project = _drama_or_404(project_id)
    shot = _shot_or_404(project, shot_id)
    payload = payload if isinstance(payload, dict) else {}
    stage = str(payload.get("stage") or "")
    job_id = str(payload.get("job") or "")
    if stage not in ("keyframe", "endframe", "video", "audio"):
        raise HTTPException(400, f"不認識的階段：{stage}")
    if job_id and job_id not in shot.jobs_for(stage):
        raise HTTPException(400, "這個工作不屬於這顆鏡頭的這個階段")
    if job_id:
        record = lib.records.get(job_id)
        if record is None or record.status != "done":
            raise HTTPException(400, "只有已經跑完的工作可以採用")
    shot.set_active(stage, job_id)     # "" clears the acceptance
    DRAMAS.save()
    return JSONResponse(_drama_payload(project))


# -- experiments: fixed-seed sweeps ------------------------------------------

EXPERIMENTS = exp_mod.ExperimentStore(config.OUTPUT_DIR / ".experiments.jsonl")
EXPERIMENTS.load()


def _provenance(payload: dict) -> dict:
    """Hash what actually produced the pictures, by content not by filename."""
    ckpt_dir = config.MODELS_DIR / "checkpoints"
    lora_dir = config.MODELS_DIR / "loras"
    wanted_models = set(payload.get("axes", {}).get("model", []) or [])
    base_model = str(payload.get("base", {}).get("model", ""))
    if base_model:
        wanted_models.add(base_model)
    checkpoints = {}
    for model_id in wanted_models:
        model = images.resolve(model_id, installed_checkpoints())
        if model is not None:
            path = ckpt_dir / model.file.name
            if path.is_file():
                checkpoints[model.file.name] = path
    loras = {}
    for entry in payload.get("base", {}).get("loras", []) or []:
        name = str(entry.get("name", ""))
        path = lora_dir / name
        if name and path.is_file():
            loras[name] = path
    return exp_mod.provenance(
        checkpoints=checkpoints, loras=loras,
        comfy_commit=updates.head_commit(config.COMFY_DIR),
        extra={"app_commit": updates.head_commit(config.REPO_DIR)})


@app.get("/api/experiments")
async def list_experiments() -> JSONResponse:
    return JSONResponse({
        "experiments": [e.public() for e in EXPERIMENTS.recent()],
        "axes": exp_mod.AXES,
        "criteria": exp_mod.CRITERIA,
        "max_jobs": exp_mod.MAX_JOBS,
        "max_seeds": exp_mod.MAX_SEEDS,
    })


@app.post("/api/experiments/preview")
async def preview_experiment(payload: dict = Body(default={})) -> JSONResponse:
    """What a sweep would cost, before committing a GPU to it."""
    payload = payload if isinstance(payload, dict) else {}
    seeds = [int(s) for s in payload.get("seeds", []) if str(s).lstrip("-").isdigit()]
    if not seeds:
        seeds = exp_mod.make_seeds(int(payload.get("seed_count", 3) or 3))
    variants, warning = exp_mod.expand(payload.get("axes", {}) or {}, seeds)
    return JSONResponse({
        "variants": [v.public() for v in variants],
        "seeds": seeds,
        "jobs": len(variants) * len(seeds),
        "warning": warning,
    })


@app.post("/api/experiments")
async def create_experiment(payload: dict = Body(default={})) -> JSONResponse:
    payload = payload if isinstance(payload, dict) else {}
    base = payload.get("base", {}) or {}
    if not isinstance(base, dict) or not base.get("prompt"):
        raise HTTPException(400, "實驗要有一段基礎提詞")
    seeds = [int(s) for s in payload.get("seeds", []) if str(s).lstrip("-").isdigit()]
    if not seeds:
        seeds = exp_mod.make_seeds(int(payload.get("seed_count", 3) or 3))
    EXPERIMENTS.load()
    experiment, warning = EXPERIMENTS.create(
        str(payload.get("name", "")), base, payload.get("axes", {}) or {}, seeds,
        _provenance(payload))
    EXPERIMENTS.save()
    return JSONResponse({**experiment.public(), "warning": warning})


@app.post("/api/experiments/{exp_id}/run")
async def run_experiment(exp_id: str) -> JSONResponse:
    """Queue every cell of the matrix, on the same seeds.

    Each job goes through the ordinary generate endpoint, so a sweep is exactly
    the generation the user would have run by hand - same validation, same
    graph, same history - just without the bookkeeping mistakes.
    """
    EXPERIMENTS.load()
    experiment = EXPERIMENTS.get(exp_id)
    if experiment is None:
        raise HTTPException(404, "找不到這個實驗")
    # has_run, not job_count: a run where every generation failed leaves
    # placeholders and no job ids, and guarding on the count would let the whole
    # experiment be queued a second time on top of the first.
    if experiment.has_run:
        raise HTTPException(400, "這個實驗已經跑過了")
    queued, failed = 0, []
    for variant in experiment.variants:
        variant.jobs = []
        for seed in experiment.seeds:
            request = exp_mod.settings_for(experiment.base, variant, seed)
            request["batch"] = 1
            try:
                response = await image_generate(request)
                record = json.loads(bytes(response.body).decode("utf-8"))
            except HTTPException as exc:
                failed.append(f"{variant.label} · seed {seed}: {exc.detail}")
                # Keep the slot. Position in this list is what says which seed a
                # job belongs to, so dropping a failed cell slides every later
                # job one seed to the left - and the pairwise comparison then
                # labels seed 33's picture as seed 22. That is a wrong result
                # rather than a missing one, which is far worse.
                variant.jobs.append("")
                continue
            variant.jobs.append(record["id"])
            queued += 1
    EXPERIMENTS.save()
    return JSONResponse({**experiment.public(), "queued": queued,
                         "failed": failed[:10]})


@app.get("/api/experiments/{exp_id}")
async def get_experiment(exp_id: str) -> JSONResponse:
    EXPERIMENTS.load()
    experiment = EXPERIMENTS.get(exp_id)
    if experiment is None:
        raise HTTPException(404, "找不到這個實驗")
    # Attach the current state of each job so a contact sheet can render.
    jobs = {}
    for variant in experiment.variants:
        for job_id in variant.jobs:
            record = lib.records.get(job_id)
            if record is not None:
                jobs[job_id] = public(record)
    return JSONResponse({**experiment.public(), "jobs": jobs})


@app.get("/api/experiments/{exp_id}/pair")
async def experiment_pair(exp_id: str, criterion: str = "likeness") -> JSONResponse:
    """The next blind pair to judge, or nothing left."""
    EXPERIMENTS.load()
    experiment = EXPERIMENTS.get(exp_id)
    if experiment is None:
        raise HTTPException(404, "找不到這個實驗")
    if criterion not in exp_mod.CRITERIA:
        raise HTTPException(400, f"不認識的評分項目：{criterion}")
    pair = exp_mod.next_pair(experiment, criterion)
    if pair is None:
        return JSONResponse({"done": True, "standings": experiment.standings()})
    for side in ("a", "b"):
        record = lib.records.get(pair[side]["job"])
        pair[side]["image"] = public(record)["output"] if record else ""
        pair[side]["ready"] = bool(record and record.status == "done")
    return JSONResponse({"done": False, "pair": pair, "criterion": criterion,
                         "question": exp_mod.CRITERIA[criterion]})


@app.post("/api/experiments/{exp_id}/vote")
async def experiment_vote(exp_id: str, payload: dict = Body(default={})
                          ) -> JSONResponse:
    EXPERIMENTS.load()
    experiment = EXPERIMENTS.get(exp_id)
    if experiment is None:
        raise HTTPException(404, "找不到這個實驗")
    payload = payload if isinstance(payload, dict) else {}
    criterion = str(payload.get("criterion", ""))
    if criterion not in exp_mod.CRITERIA:
        raise HTTPException(400, f"不認識的評分項目：{criterion}")
    winner = str(payload.get("winner", ""))
    loser = str(payload.get("loser", ""))
    other = str(payload.get("other", ""))
    known = {v.id for v in experiment.variants}
    if loser not in known or (winner and winner not in known):
        raise HTTPException(400, "投票對象不在這個實驗裡")
    if winner:
        if winner == loser:
            raise HTTPException(400, "贏家和輸家不能是同一組設定")
        other = ""      # a decided vote has no third side
    else:
        # A tie is a statement about two variants, so both have to arrive or the
        # standings credit one of them and the pairing logic cannot tell what
        # was compared.
        if other not in known or other == loser:
            raise HTTPException(400, "平手投票必須帶兩個不同的設定")
    experiment.votes.append(exp_mod.Vote(
        criterion=criterion, winner=winner, loser=loser, other=other,
        seed=int(payload.get("seed", 0) or 0)))
    EXPERIMENTS.save()
    return JSONResponse({"standings": experiment.standings(),
                         "votes": len(experiment.votes)})


@app.delete("/api/experiments/{exp_id}")
async def delete_experiment(exp_id: str) -> JSONResponse:
    EXPERIMENTS.load()
    if not EXPERIMENTS.delete(exp_id):
        raise HTTPException(404, "找不到這個實驗")
    EXPERIMENTS.save()
    return JSONResponse({"ok": True})


# -- official reference art --------------------------------------------------
#
# The point of this whole group of endpoints is one button: take a picture the
# user collected and hand it to the generator as an image, because words average
# and a picture does not. Everything else here is filing.

REF_LIB = refslib.RefLibrary(config.REFS_DIR)
REF_LIB.load()


def _ref_candidates(pack_id: str):
    pack = charpacks.get(pack_id)
    return refslib.candidates_from_pack(pack) if pack else []


@app.get("/api/refs")
async def list_refs(pack: str = "hololive-collection") -> JSONResponse:
    REF_LIB.load()
    return JSONResponse({
        "pack": pack,
        "counts": REF_LIB.counts(pack),
        "unfiled": [r.public("/refs") for r in REF_LIB.unfiled(pack)],
        "total": sum(1 for r in REF_LIB.refs if r.pack == pack),
    })


@app.get("/api/refs/{pack}/{character}")
async def refs_for_character(pack: str, character: str) -> JSONResponse:
    REF_LIB.load()
    return JSONResponse({
        "refs": [r.public("/refs") for r in REF_LIB.for_character(pack, character)]
    })


@app.post("/api/refs/scan")
async def scan_refs(payload: dict = Body(default={})) -> JSONResponse:
    """Dry run: look at a local folder and say what an import would do.

    Reads filenames only, never pixels, and writes nothing. The archive is the
    user's own filing system and this matcher has never seen its naming
    convention, so showing the answer before touching anything is the only
    honest way to find out whether it works.
    """
    payload = payload if isinstance(payload, dict) else {}
    pack = str(payload.get("pack") or "hololive-collection")
    cands = _ref_candidates(pack)
    if not cands:
        raise HTTPException(400, f"不認識的角色包：{pack}")
    folder = str(payload.get("path") or "").strip().strip('"')
    if not folder:
        raise HTTPException(400, "要給一個資料夾路徑")
    root = Path(folder).expanduser()
    if not root.is_dir():
        raise HTTPException(400, f"找不到這個資料夾：{root}")
    rows, problems = refslib.scan(root, cands)
    return JSONResponse({
        "path": str(root), "pack": pack, "problems": problems,
        **refslib.scan_summary(rows),
    })


@app.post("/api/refs/import-folder")
async def import_refs_folder(payload: dict = Body(default={})) -> JSONResponse:
    """Import a local folder. Indexes in place by default; never moves anything.

    `copy: true` takes a copy into the refs folder instead, which is what you
    want if the source is a USB stick or a temp download you are about to
    delete. Otherwise the archive stays where it is and only gets an index.
    """
    payload = payload if isinstance(payload, dict) else {}
    pack = str(payload.get("pack") or "hololive-collection")
    cands = _ref_candidates(pack)
    if not cands:
        raise HTTPException(400, f"不認識的角色包：{pack}")
    folder = str(payload.get("path") or "").strip().strip('"')
    if not folder:
        raise HTTPException(400, "要給一個資料夾路徑")
    root = Path(folder).expanduser()
    if not root.is_dir():
        raise HTTPException(400, f"找不到這個資料夾：{root}")
    REF_LIB.load()
    result = REF_LIB.import_folder(
        root, pack, cands,
        copy=bool(payload.get("copy")),
        only_matched=bool(payload.get("only_matched")),
    )
    REF_LIB.save()
    return JSONResponse({
        **result, "path": str(root), "pack": pack,
        "counts": REF_LIB.counts(pack),
        "unfiled_list": [r.public("/refs") for r in REF_LIB.unfiled(pack)][:60],
    })


@app.get("/api/refs/file/{pack}/{name}")
async def ref_file(pack: str, name: str) -> FileResponse:
    """Serve one reference image.

    The static mount under /refs only covers files that live in the refs folder.
    A linked reference lives in the user's own archive, so it needs a route that
    looks the path up in the index - which also means nothing outside the index
    is reachable through it.
    """
    REF_LIB.load()
    ref = REF_LIB.get(pack, name)
    if ref is None:
        raise HTTPException(404, "找不到這張參考圖")
    path = REF_LIB.path(ref)
    if not path.is_file():
        raise HTTPException(404, "檔案不在了（原始資料夾被移動或刪掉了？）")
    return FileResponse(path)


@app.post("/api/refs/import")
async def import_refs(files: list[UploadFile], pack: str = Form("hololive-collection")
                      ) -> JSONResponse:
    """Take a pile of downloaded images (or a zip of them) and file them.

    Reports what it could not place rather than guessing: an unmatched file is
    one click to assign, a mis-matched one is a wrong reference you find out
    about three generations later.
    """
    cands = _ref_candidates(pack)
    if not cands:
        raise HTTPException(400, f"不認識的角色包：{pack}")
    REF_LIB.load()
    filed, unfiled, dupes, failed = 0, 0, 0, []
    for upload in files:
        raw = await upload.read()
        name = upload.filename or "image.png"
        items: list[tuple[str, bytes]] = []
        if name.lower().endswith(".zip"):
            import io
            import zipfile
            try:
                with zipfile.ZipFile(io.BytesIO(raw)) as zf:
                    for info in zf.infolist():
                        if info.is_dir() or info.file_size > refslib.MAX_BYTES:
                            continue
                        if Path(info.filename).suffix.lower() in refslib.IMAGE_SUFFIXES:
                            items.append((Path(info.filename).name, zf.read(info)))
            except Exception as exc:  # noqa: BLE001
                failed.append(f"{name}: 解不開（{type(exc).__name__}）")
                continue
        else:
            items.append((name, raw))
        for item_name, data in items:
            try:
                ref = REF_LIB.add(data, item_name, pack, cands)
            except ValueError as exc:
                failed.append(str(exc))
                continue
            if ref.note == "duplicate":
                dupes += 1
            elif ref.character:
                filed += 1
            else:
                unfiled += 1
    REF_LIB.save()
    return JSONResponse({
        "filed": filed, "unfiled": unfiled, "dupes": dupes, "failed": failed[:20],
        "counts": REF_LIB.counts(pack),
        "unfiled_list": [r.public("/refs") for r in REF_LIB.unfiled(pack)],
    })


@app.post("/api/refs/{pack}/{name}/assign")
async def assign_ref(pack: str, name: str, payload: dict = Body(default={})
                     ) -> JSONResponse:
    REF_LIB.load()
    ref = REF_LIB.get(pack, name)
    if ref is None:
        raise HTTPException(404, "找不到這張參考圖")
    payload = payload if isinstance(payload, dict) else {}
    character = str(payload.get("character", ""))
    if character and not any(c.key == character for c in _ref_candidates(pack)):
        raise HTTPException(400, f"這個角色包裡沒有：{character}")
    REF_LIB.assign(ref, character)
    REF_LIB.save()
    return JSONResponse(ref.public("/refs"))


@app.delete("/api/refs/{pack}/{name}")
async def delete_ref(pack: str, name: str) -> JSONResponse:
    REF_LIB.load()
    if not REF_LIB.delete(pack, name):
        raise HTTPException(404, "找不到這張參考圖")
    REF_LIB.save()
    return JSONResponse({"ok": True})


@app.post("/api/refs/{pack}/{name}/use")
async def use_ref(pack: str, name: str) -> JSONResponse:
    """Copy a reference into staging so a generation can use it.

    Same staging path an uploaded source image takes, so it works with img2img
    and ControlNet without either of those knowing references exist.
    """
    REF_LIB.load()
    ref = REF_LIB.get(pack, name)
    if ref is None:
        raise HTTPException(404, "找不到這張參考圖")
    source = REF_LIB.path(ref)
    if not source.is_file():
        raise HTTPException(404, "這張參考圖的檔案不見了")
    config.STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged = f"ref-{uuid.uuid4().hex[:10]}{source.suffix.lower()}"
    (config.STAGING_DIR / staged).write_bytes(source.read_bytes())
    return JSONResponse({"name": staged, "width": ref.width, "height": ref.height,
                         "original": ref.original})


@app.get("/api/artists")
async def list_artists() -> JSONResponse:
    """The artist roster: tag, style note, measured signals, post count."""
    return JSONResponse(artists.public())


@app.get("/api/posebook")
async def list_posebook() -> JSONResponse:
    """Every pose codex, whole. Same reasoning as /api/packs.

    ~380KB for the one that ships, and the picker walks a 3-level tree that has
    to feel instant, so it is sent once and filtered in the browser.
    """
    books = posebook.load_all()
    return JSONResponse({
        "books": [b.public() for b in books],
        "artist_negative": posebook.ARTIST_NEGATIVE,
    })


@app.post("/api/posebook/{book_id}/prompt")
async def posebook_prompt(book_id: str, payload: dict = Body(default={})) -> JSONResponse:
    """One pose, assembled. The artist group is opt-in, which is the point.

    A codex entry's artist tags are the tester's style, not the pose. Left on by
    default they would quietly overrule whatever the user picked in a character
    pack, so `artists` defaults to off and carries its own weight when on.
    """
    book = posebook.get(book_id)
    if book is None:
        raise HTTPException(404, f"不認識的動作庫：{book_id}")
    payload = payload if isinstance(payload, dict) else {}
    pose = book.get(str(payload.get("pose", "")))
    if pose is None:
        raise HTTPException(404, f"這個動作庫裡沒有：{payload.get('pose')}")
    try:
        variant = int(payload.get("variant", 0))
    except (TypeError, ValueError):
        variant = 0
    built = posebook.build_prompt(
        pose, variant,
        artists=bool(payload.get("artists")),
        artist_weight=_as_float(payload.get("artist_weight"), 1.0),
        cast=bool(payload.get("cast")),
        extra=str(payload.get("extra", "")),
        head=str(payload.get("head", "")),
    )
    return JSONResponse(built)


@app.post("/api/posebook/import")
async def import_posebook(file: UploadFile) -> JSONResponse:
    """Preview what a codex document would become, without saving anything.

    These documents get revised, and the next revision should not need a code
    change - but it should not silently replace a working database either, so
    this reports what it found and leaves writing to the build script.
    """
    data = await file.read()
    if not data:
        raise HTTPException(400, "檔案是空的")
    text, error = promptbook.read_text(data, file.filename or "codex.txt")
    if error:
        raise HTTPException(400, error)
    book = posebook.parse_codex(text, codex_id="preview",
                                name=file.filename or "", source="")
    groups = book.public()["groups"]
    return JSONResponse({
        "count": len(book.poses),
        "variants": sum(len(p.variants) for p in book.poses),
        "skipped": book.skipped,
        "skipped_variants": book.skipped_variants,
        "groups": [{"label": g["label"],
                    "sections": len(g["sections"]),
                    "poses": sum(len(s["poses"]) for s in g["sections"])}
                   for g in groups],
        "artists": book.artist_index()[:30],
        "sample": [p.public() for p in book.poses[:3]],
    })


@app.post("/api/packs/{pack_id}/download")
async def download_pack_lora(pack_id: str) -> JSONResponse:
    """Fetch the pack's LoRA from CivitAI, which needs the user's own API key."""
    pack = charpacks.get(pack_id)
    if pack is None:
        raise HTTPException(404, f"不認識的角色包：{pack_id}")
    if not pack.download_url:
        raise HTTPException(400, f"這個角色包沒有附下載連結，請自己到 {pack.civitai} 抓")
    try:
        headers = tuple(civitai.download_headers().items())
    except civitai.NeedsApiKey as exc:
        raise HTTPException(400, str(exc))
    remote = downloader.RemoteFile(
        url=pack.download_url, folder="loras", name=pack.file,
        size=pack.size, headers=headers,
    )
    meta = {"url": pack.civitai, "trained_words": [], "base_model": pack.base_model,
            "version_id": pack.version_id, "name": pack.label}
    return JSONResponse(
        models.enqueue_files(
            key=f"pack:{pack.id}", label=f"角色包 · {pack.label}",
            files=[remote], sidecars={pack.file: meta},
        ).public()
    )


@app.post("/api/controlnets/{controlnet_id}/download")
async def download_controlnet(controlnet_id: str) -> JSONResponse:
    chosen = controlnets.get(controlnet_id)
    if chosen is None:
        raise HTTPException(404, f"不認識的 ControlNet：{controlnet_id}")
    return JSONResponse(
        _queue_single(f"controlnet:{chosen.id}", f"ControlNet · {chosen.label}", chosen.file)
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


@app.post("/api/promptbook/preview")
async def promptbook_preview(file: UploadFile) -> JSONResponse:
    """Parse an uploaded collection and show what came out - saving nothing.

    A guess about the shape of someone else's document should be reviewable
    before it lands in their library, so importing is two steps: look, then
    keep.
    """
    data = await file.read()
    if not data:
        raise HTTPException(400, "檔案是空的")
    if len(data) > 64 * 1024 * 1024:
        raise HTTPException(400, "檔案太大了（上限 64MB）")
    name = Path(file.filename or "collection.txt").name
    if Path(name).suffix.lower() not in promptbook.SUPPORTED:
        raise HTTPException(
            400,
            f"不支援 {Path(name).suffix or '這種'} 檔。支援："
            + "、".join(sorted(promptbook.SUPPORTED)),
        )
    parsed = await asyncio.get_running_loop().run_in_executor(
        None, promptbook.parse, data, name
    )
    known = set(book.entries)
    # The parse result stays here and is imported by token. Returning every
    # entry so the browser can post it straight back would round-trip the whole
    # collection twice - a 64MB upload (this endpoint's own cap) becomes
    # 100MB+ of JSON each way - to render forty preview rows.
    token = uuid.uuid4().hex[:16]
    _pending[token] = (time.time(), name, parsed.entries)
    _sweep_pending()
    return JSONResponse(
        {
            "token": token,
            "how": parsed.how,
            "note": parsed.note,
            "count": len(parsed.entries),
            "new": sum(1 for e in parsed.entries if e.key not in known),
            "source": name,
            "sample": [e.public() for e in parsed.entries[:40]],
        }
    )


# token -> (when, source, entries). Previews the user never confirmed are
# dropped rather than held forever.
_pending: dict[str, tuple[float, str, list]] = {}
PENDING_TTL = 30 * 60
PENDING_MAX = 8


def _sweep_pending() -> None:
    cutoff = time.time() - PENDING_TTL
    for key in [k for k, v in _pending.items() if v[0] < cutoff]:
        _pending.pop(key, None)
    while len(_pending) > PENDING_MAX:
        _pending.pop(min(_pending, key=lambda k: _pending[k][0]), None)


@app.post("/api/promptbook/import")
async def promptbook_import(payload: dict = Body(...)) -> JSONResponse:
    """Keep the entries a preview produced, minus anything the user dropped."""
    token = str(payload.get("token", ""))
    staged = _pending.pop(token, None)
    if staged is None:
        raise HTTPException(400, "這份預覽已經過期了，請重新選一次檔案")
    _, source, entries = staged
    drop = {str(d) for d in (payload.get("drop") or [])}
    # Entries came from promptbook.parse, so they are already cleaned and
    # length-capped by _finish; nothing untrusted is reconstructed here.
    keep = [e for e in entries if e.key not in drop]
    if not keep:
        raise HTTPException(400, "沒有要匯入的內容")
    added, duplicate = await asyncio.get_running_loop().run_in_executor(
        None, book.add_all, keep
    )
    return JSONResponse(
        {"added": added, "duplicate": duplicate, "total": len(book.entries),
         "source": source}
    )


@app.get("/api/promptbook")
async def promptbook_list(q: str = "", starred: bool = False,
                          limit: int = 60, offset: int = 0) -> JSONResponse:
    found, total = book.search(q, starred, max(1, min(limit, 300)), max(0, offset))
    return JSONResponse(
        {
            "entries": [e.public() for e in found],
            "total": total,
            "all": len(book.entries),
            "sources": book.sources(),
        }
    )


@app.post("/api/promptbook/{entry_id}/star")
async def promptbook_star(entry_id: str, payload: dict = Body(...)) -> JSONResponse:
    if not book.star(entry_id, bool(payload.get("starred", True))):
        raise HTTPException(404, "找不到這一則")
    return JSONResponse({"ok": True})


@app.post("/api/promptbook/{entry_id}/used")
async def promptbook_used(entry_id: str) -> JSONResponse:
    book.used(entry_id)
    return JSONResponse({"ok": True})


@app.delete("/api/promptbook/{entry_id}")
async def promptbook_delete(entry_id: str) -> JSONResponse:
    if not book.delete(entry_id):
        raise HTTPException(404, "找不到這一則")
    return JSONResponse({"ok": True, "total": len(book.entries)})


@app.delete("/api/promptbook/source/{source}")
async def promptbook_delete_source(source: str) -> JSONResponse:
    removed = book.delete_source(source)
    return JSONResponse({"removed": removed, "total": len(book.entries)})


@app.get("/api/taggers")
async def list_taggers() -> JSONResponse:
    here = set(tags.installed(config.MODELS_DIR))
    return JSONResponse(
        {
            "taggers": [
                {"id": t.id, "label": t.label, "note": t.note, "size": t.size,
                 "installed": t.id in here}
                for t in tags.TAGGERS
            ],
            "installed": sorted(here),
            "runtime": _has_onnx(),
        }
    )


def _has_onnx() -> bool:
    try:
        import onnxruntime  # noqa: F401
        return True
    except Exception:  # noqa: BLE001
        return False


@app.post("/api/taggers/{tagger_id}/download")
async def download_tagger(tagger_id: str) -> JSONResponse:
    chosen = tags.get(tagger_id)
    if chosen is None:
        raise HTTPException(404, f"不認識的分析模型：{tagger_id}")
    remote = [
        downloader.RemoteFile(url=downloader.url_for(f), folder=f.folder,
                              name=f.name, size=f.size)
        for f in (chosen.model, chosen.labels)
    ]
    return JSONResponse(
        models.enqueue_files(
            key=f"tagger:{chosen.id}", label=f"看圖分析 · {chosen.label}",
            files=remote, kind="model",
        ).public()
    )


@app.post("/api/inspect")
async def inspect(image: UploadFile, tagger: str = Form(""),
                  threshold: float = Form(tags.DEFAULT_GENERAL)) -> JSONResponse:
    """What made this image, and what is in it.

    Two answers with very different standing, so they are returned separately
    and labelled: `metadata` is read out of the file and is exact; `tags` is a
    model's opinion of the pixels. Nothing here claims to identify a LoRA from
    an image, because nothing can - a LoRA is only reported when the file
    itself names one.
    """
    data = await image.read()
    if not data:
        raise HTTPException(400, "圖片是空的")
    try:
        picture = Image.open(io.BytesIO(data))
        picture.load()
    except Exception:
        raise HTTPException(400, "無法辨識這個圖片格式")

    found = inspect_image.read_metadata(picture)
    result: dict = {
        "size": list(picture.size),
        "metadata": found.public(),
        "tags": None,
        "tagger_error": "",
        "loras": [],
        "suggest_model": "",
        "rating_label": "",
    }

    here = tags.installed(config.MODELS_DIR)
    chosen = tagger if tagger in here else (here[0] if here else "")
    if chosen:
        try:
            loop = asyncio.get_running_loop()
            guess = await loop.run_in_executor(
                None, tags.describe, picture,
                tags.folder(config.MODELS_DIR, chosen),
                max(0.05, min(float(threshold), 0.95)),
            )
            result["tags"] = guess.public()
            result["suggest_model"] = tags.suggest_model(guess)
            result["rating_label"] = tags.RATING_LABEL.get(guess.rating, guess.rating)
            result["lora_hints"] = tags.matching_loras(guess, models.list_loras())
        except ImportError:
            result["tagger_error"] = (
                "缺少 onnxruntime 套件。關掉 app，跑一次 update.bat 或 install.bat 就會裝好。"
            )
        except Exception as exc:  # noqa: BLE001 - a failed guess must not 500
            result["tagger_error"] = f"分析失敗：{type(exc).__name__}: {exc}"
    elif not tags.installed(config.MODELS_DIR):
        result["tagger_error"] = "還沒下載看圖分析模型（到「模型」分頁下載，約 380MB）。"

    # Which of the LoRAs the file named do we actually have?
    have = {l["name"] for l in models.list_loras()}
    for lora in found.loras:
        name = str(lora.get("name", ""))
        stem = name.rsplit(".", 1)[0].lower()
        match = next((h for h in have if h.rsplit(".", 1)[0].lower() == stem), "")
        result["loras"].append(
            {
                **lora,
                "installed": bool(match),
                "installed_as": match,
                "search": f"https://civitai.com/search/models?query={name.rsplit('.', 1)[0]}",
            }
        )
    return JSONResponse(result)


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
            # Restaging needs two downloads to do anything. Without them it
            # still "works" - it measures rectangles and then draws whatever
            # you typed, which looks exactly like the feature being broken.
            # So the requirements are stated before the upload, not after.
            "restage_ready": {
                "tagger": bool(tags.installed(config.MODELS_DIR)),
                "controlnet": bool(installed_controlnets()),
            },
        }
    )


def resolve_layout(payload: dict):
    """A catalogue layout, or one measured off a page the user uploaded."""
    name = str(payload.get("layout", "four-grid"))
    if name == comics.CUSTOM_ID:
        try:
            aspect = float(payload.get("custom_aspect") or (2 / 3))
        except (TypeError, ValueError):
            # Comes from the client; a bad value is a 400, not a 500.
            aspect = 2 / 3
        return comics.custom_layout(payload.get("custom_panels") or [], aspect)
    return comics.get(name)


@app.post("/api/comic/restage")
async def comic_restage(
    page: UploadFile,
    character: UploadFile | None = None,
    outfit_from: str = Form("character"),
    reading: str = Form("ltr"),
    tagger: str = Form(""),
    defer: bool = Form(True),
) -> JSONResponse:
    """Read a page's panel layout and staging, ready to redraw with someone else.

    Nothing is generated here. It returns the detected panels, and for each one
    a suggested prompt built from the shot's own tags plus the new character's
    - so the whole thing lands in the comic editor as editable text rather than
    as a black box. Every tag is labelled with where it came from.
    """
    page_bytes = await page.read()
    if not page_bytes:
        raise HTTPException(400, "頁面圖片是空的")
    try:
        page_image = Image.open(io.BytesIO(page_bytes))
        page_image.load()
        page_image = page_image.convert("RGB")
    except Exception:
        raise HTTPException(400, "無法辨識這個頁面圖片")

    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(
        None, pagelayout.detect, page_image, 900,
        "rtl" if reading == "rtl" else "ltr",
    )
    result: dict = {
        "layout": found.public(),
        "panels": [],
        "character": None,
        "tagger_error": "",
        "outfit_from": "page" if outfit_from == "page" else "character",
        "controls": [],
        "controlnets": installed_controlnets(),
    }
    if not found.boxes:
        result["tagger_error"] = found.note
        return JSONResponse(result)

    # Every panel's own crop is kept, so the new page can be guided by the old
    # one's actual composition and not merely by tags copied off it. This is
    # what turns "a similar scene" into "the same shot with someone else in it".
    result["controls"] = _save_controls(page_image, found.boxes)

    here = tags.installed(config.MODELS_DIR)
    chosen = tagger if tagger in here else (here[0] if here else "")
    if not chosen:
        result["tagger_error"] = (
            "分鏡切出來了，但要看懂每一格畫了什麼需要「看圖分析模型」"
            "（到「模型」分頁下載，約 380MB）。現在只會給你空的格子。"
            "（構圖參考圖已經留好了，即使沒有這個模型，用 ControlNet 一樣能複製分鏡。）"
        )
        result["panels"] = [{"scene": [], "prompt": ""} for _ in found.boxes]
        return JSONResponse(result)

    base = tags.folder(config.MODELS_DIR, chosen)
    look: list[str] = []
    outfit: list[str] = []
    if character is not None:
        char_bytes = await character.read()
        if char_bytes:
            try:
                char_image = Image.open(io.BytesIO(char_bytes))
                char_image.load()
            except Exception:
                raise HTTPException(400, "無法辨識這個角色圖片")
            try:
                guess = await loop.run_in_executor(None, tags.describe, char_image, base)
            except ImportError:
                result["tagger_error"] = (
                    "缺少 onnxruntime 套件，所以看不懂圖。關掉 app 跑一次 update.bat 就會裝好。"
                    "分鏡還是量好了。"
                )
                return JSONResponse(result)
            except Exception as exc:  # noqa: BLE001 - keep the layout we did get
                result["tagger_error"] = f"角色圖分析失敗：{type(exc).__name__}: {exc}"
                return JSONResponse(result)
            split = tags.split_tags([n for n, _ in guess.general])
            look = split["look"]
            outfit = split["outfit"]
            result["character"] = {
                **guess.public(),
                "look": [tags.to_prompt(t) for t in look],
                "outfit": [tags.to_prompt(t) for t in outfit],
                "dropped": [tags.to_prompt(t) for t in split["scene"] + split["drop"]],
            }

    # Tagging is ~2s per panel on CPU, so a nine-panel page is half a minute of
    # nothing happening. The layout itself takes under a second, so it is handed
    # back straight away under a token and the panels are fetched one at a time,
    # which gives the UI something real to show progress against.
    if defer:
        token = uuid.uuid4().hex[:16]
        _restage[token] = (time.time(), page_image, base, look, outfit,
                           result["outfit_from"], found.boxes)
        _sweep_restage()
        result["token"] = token
        result["panels"] = [None] * len(found.boxes)
        return JSONResponse(result)

    for box in found.boxes:
        result["panels"].append(
            await _read_panel(page_image, box, base, look, outfit,
                              result["outfit_from"])
        )
    return JSONResponse(result)


CONTROL_PREFIX = "ctrl-"
CONTROL_RE = re.compile(r"^ctrl-[0-9a-f]{12}-\d{2}\.png$")
# A control crop is only wanted for as long as the tab that made it is open.
CONTROL_TTL = 24 * 3600


def _save_controls(page_image: Image.Image, boxes: list) -> list[str]:
    """Stash each panel's own art, to guide the redraw of that same panel.

    Returns one entry per box, in box order, so index N of this list always
    belongs to panel N. A box too small to crop yields "" rather than shifting
    every later panel's reference onto the wrong rectangle.
    """
    config.STAGING_DIR.mkdir(parents=True, exist_ok=True)
    cutoff = time.time() - CONTROL_TTL
    for stale in config.STAGING_DIR.glob(f"{CONTROL_PREFIX}*.png"):
        try:
            if stale.stat().st_mtime < cutoff:
                stale.unlink(missing_ok=True)
        except OSError:
            pass
    group = uuid.uuid4().hex[:12]
    out: list[str] = []
    for index, box in enumerate(boxes[:99]):
        crop = pagelayout.crops(page_image, [box])
        if not crop:
            out.append("")
            continue
        name = f"{CONTROL_PREFIX}{group}-{index:02d}.png"
        try:
            crop[0].convert("RGB").save(config.STAGING_DIR / name, "PNG")
        except OSError:
            out.append("")
            continue
        out.append(name)
    return out


def control_path(name: str) -> Path | None:
    """The staged crop behind a name the client sent back, or None.

    The name makes a round trip through the browser, so it is matched against
    the exact shape this server writes rather than trusted - otherwise it is a
    path straight out of the staging folder.
    """
    if not CONTROL_RE.match(name or ""):
        return None
    path = config.STAGING_DIR / name
    return path if path.is_file() else None


@app.get("/api/comic/control/{name}")
async def comic_control(name: str) -> FileResponse:
    """The stashed crop, so the editor can show what each panel will follow."""
    path = control_path(name)
    if path is None:
        raise HTTPException(404, "找不到這張構圖參考圖（可能已經過期）")
    return FileResponse(path, media_type="image/png")


# token -> (when, page, tagger dir, look, outfit, outfit_from, boxes)
_restage: dict[str, tuple] = {}
RESTAGE_TTL = 20 * 60
RESTAGE_MAX = 4


def _sweep_restage() -> None:
    cutoff = time.time() - RESTAGE_TTL
    for key in [k for k, v in _restage.items() if v[0] < cutoff]:
        _restage.pop(key, None)
    while len(_restage) > RESTAGE_MAX:
        _restage.pop(min(_restage, key=lambda k: _restage[k][0]), None)


async def _read_panel(page_image, box, base, look, outfit, outfit_from) -> dict:
    """Tag one panel and turn it into a prompt for the new character."""
    blank = {"scene": [], "outfit": [], "dropped": [], "rating": "",
             "no_people": False, "prompt": ""}
    # crops() skips a degenerate box, so panels are paired to rectangles
    # explicitly - zipping the two lists would shift every later panel's prompt
    # onto the wrong rectangle whenever one crop was dropped.
    crop = pagelayout.crops(page_image, [box])
    if not crop:
        return {**blank, "note": "這一格太小，讀不出內容"}
    try:
        guess = await asyncio.get_running_loop().run_in_executor(
            None, tags.describe, crop[0], base
        )
    except Exception as exc:  # noqa: BLE001 - a failed panel must not lose the layout
        return {**blank, "note": f"這一格分析失敗：{type(exc).__name__}"}

    split = tags.split_tags([n for n, _ in guess.general])
    # The shot keeps its blocking; the character brings their own face. A
    # character name detected on the page is always dropped - that is the
    # original cast, and replacing them is the entire point.
    # An establishing shot with nobody in it must not have a character pasted
    # into it - "no humans, blue eyes, long hair" argues with itself, and the
    # model settles the argument by drawing a person. Their clothes do it just
    # as surely as their face, so an empty panel takes neither: it keeps only
    # what the page itself had.
    empty = any(n in ("no_humans", "scenery") for n, _ in guess.general)
    pieces = list(split["scene"])
    if empty:
        pieces += split["outfit"]
    else:
        pieces = look + pieces
        pieces += (outfit or split["outfit"]) if outfit_from == "character" else split["outfit"]
    seen: set[str] = set()
    ordered = [t for t in pieces if not (t in seen or seen.add(t))]
    return {
        "scene": [tags.to_prompt(t) for t in split["scene"]],
        "outfit": [tags.to_prompt(t) for t in split["outfit"]],
        "dropped": [tags.to_prompt(t) for t in split["look"] + split["drop"]]
        + [tags.to_prompt(n) for n, _ in guess.characters],
        "rating": guess.rating,
        "no_people": empty,
        "note": "這格沒有人物，所以沒有套用角色外觀" if empty else "",
        "prompt": ", ".join(tags.to_prompt(t) for t in ordered),
    }


@app.post("/api/comic/restage/{token}/panel/{index}")
async def restage_panel(token: str, index: int,
                        payload: dict = Body(default={})) -> JSONResponse:
    """Read one panel of a page a previous restage call measured."""
    staged = _restage.get(token)
    if staged is None:
        raise HTTPException(400, "這次的分析已經過期了，請重新上傳一次頁面")
    when, page_image, base, look, outfit, outfit_from, boxes = staged
    if not 0 <= index < len(boxes):
        raise HTTPException(404, "沒有這一格")
    # The switch can be flipped after the fact without re-uploading anything.
    # A body of `null` arrives as None rather than as the default, so the shape
    # is checked instead of assumed.
    payload = payload if isinstance(payload, dict) else {}
    if payload.get("outfit_from") in ("character", "page"):
        outfit_from = str(payload["outfit_from"])
    _restage[token] = (time.time(), page_image, base, look, outfit, outfit_from, boxes)
    return JSONResponse(
        {"index": index,
         "panel": await _read_panel(page_image, boxes[index], base, look,
                                    outfit, outfit_from)}
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
    layout = resolve_layout(payload)
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

    # Composition references, one per panel, produced by a restage. Anything
    # that is not a crop this server wrote is dropped rather than refused: a
    # stale reference should cost that panel its guide, not the whole page.
    controls: list[str] = []
    if settings.controlnet:
        if settings.controlnet not in installed_controlnets():
            raise HTTPException(
                400,
                f"還沒下載 ControlNet 模型 {settings.controlnet}，請到「模型」分頁下載",
            )
        raw = [str(c or "") for c in (payload.get("controls") or [])][: layout.count]
        controls = [c if control_path(c) else "" for c in raw]
        if raw and not any(controls):
            raise HTTPException(
                400,
                "構圖參考圖都不見了（超過保存時間，或 app 重開過）。"
                "請回到「分鏡克隆」重新上傳一次原稿。",
            )

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
            "custom_panels": [
                {"x": p.x, "y": p.y, "w": p.w, "h": p.h} for p in layout.panels
            ] if layout.id == comics.CUSTOM_ID else [],
            "custom_aspect": layout.aspect,
            "panels": panels,
            "controls": controls,
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
    layout = resolve_layout(payload)
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
    # Returned as bytes rather than written to a shared filename: this fires on
    # every keystroke in a dialogue box, so two overlapping requests would
    # truncate each other's file mid-read, and the file outlived every sweep.
    buf = io.BytesIO()
    page.save(buf, "PNG")
    return Response(content=buf.getvalue(), media_type="image/png",
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
        # The header shows this. "ComfyUI is not running, start it like this"
        # belongs there more than a Python class name does.
        comfy_ok, detail = False, comfy_client.explain(exc, config.COMFY_URL)
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


# -- character LoRA training ---------------------------------------------------
# The app prepares and checks the dataset and writes the config; the trainer
# itself runs outside, on the user's GPU. See training.py for why that line is
# drawn there rather than wrapping a trainer this project has never executed.


@app.get("/api/training")
async def training_meta() -> JSONResponse:
    return JSONResponse({
        "trainers": [
            {"id": t.id, "label": t.label, "trains": list(t.trains),
             "repo": t.repo, "vram_gb": t.vram_gb, "why": t.why,
             "claim": (claims.get(t.claim_id).public() if claims.get(t.claim_id) else None)}
            for t in training.TRAINERS.values()
        ],
        "recipes": [
            {"arch": r.arch, "zh": r.zh, "trainer": r.trainer_id,
             "network_dim": r.network_dim, "network_alpha": r.network_alpha,
             "learning_rate": r.learning_rate, "optimizer": r.optimizer,
             "resolution": r.resolution, "repeats": r.repeats,
             "epochs": r.epochs, "batch_size": r.batch_size, "note": r.note,
             "claim": (claims.get(r.claim_id).public() if claims.get(r.claim_id) else None)}
            for r in training.RECIPES.values()
        ],
        "shot_mix": [{"key": m.key, "zh": m.zh, "share": m.share, "why": m.why}
                     for m in training.SHOT_MIX],
        "claims": claims.public(),
    })


@app.post("/api/training/plan")
async def training_plan(payload: dict = Body(default={})) -> JSONResponse:
    """How many images of which framing, for a target set size."""
    payload = payload if isinstance(payload, dict) else {}
    try:
        count = int(payload.get("count") or 0)
    except (TypeError, ValueError):
        count = 0
    return JSONResponse({"count": max(0, count), "plan": training.plan_for(max(0, count))})


@app.post("/api/training/caption")
async def training_caption(payload: dict = Body(default={})) -> JSONResponse:
    """One caption in the shape the recipes expect."""
    payload = payload if isinstance(payload, dict) else {}
    trigger = str(payload.get("trigger") or "")
    text = training.caption_for(
        trigger,
        shot=str(payload.get("shot") or ""), hair=str(payload.get("hair") or ""),
        eyes=str(payload.get("eyes") or ""),
        expression=str(payload.get("expression") or ""),
        wearing=str(payload.get("wearing") or ""),
        setting=str(payload.get("setting") or ""),
        light=str(payload.get("light") or ""))
    return JSONResponse({"caption": text, "trigger_problem": training.check_trigger(trigger)})


@app.post("/api/training/check")
async def training_check(payload: dict = Body(default={})) -> JSONResponse:
    """Read a training folder off disk and say what is wrong with it.

    The folder is whatever the user typed. This app is local and already reads
    the reference-art folders the same way; nothing is uploaded anywhere.
    """
    payload = payload if isinstance(payload, dict) else {}
    folder = Path(str(payload.get("folder") or "").strip()).expanduser()
    trigger = str(payload.get("trigger") or "")
    arch = str(payload.get("arch") or "sdxl")
    if not str(folder):
        raise HTTPException(400, "要先給一個資料夾")
    if not folder.is_dir():
        raise HTTPException(404, f"找不到這個資料夾：{folder}")
    samples = training.read_dataset(folder)
    findings = training.check_dataset(samples, trigger=trigger, arch=arch)
    recipe = training.RECIPES.get(arch) or training.RECIPES["sdxl"]
    usable = [s for s in samples if s.width and s.height]
    return JSONResponse({
        "folder": str(folder),
        "count": len(usable),
        "samples": [s.public() for s in samples[:200]],
        "truncated": len(samples) > 200,
        "health": training.summary(findings),
        "steps": recipe.steps_for(len(usable)),
        "plan": training.plan_for(len(usable) or 30),
    })


@app.post("/api/training/config")
async def training_config(payload: dict = Body(default={})) -> JSONResponse:
    """The config file text and the command that runs it."""
    payload = payload if isinstance(payload, dict) else {}
    arch = str(payload.get("arch") or "sdxl")
    if arch not in training.RECIPES:
        raise HTTPException(400, f"不認識的架構：{arch}")
    trigger = str(payload.get("trigger") or "").strip()
    if problem := training.check_trigger(trigger):
        raise HTTPException(400, problem)
    name = re.sub(r"[^A-Za-z0-9_.-]", "_", str(payload.get("name") or trigger)).strip("_")
    if not name:
        raise HTTPException(400, "輸出名稱不能是空的")
    try:
        count = int(payload.get("count") or 0)
    except (TypeError, ValueError):
        count = 0
    override = str(payload.get("trainer") or "")
    if override:
        if override not in training.TRAINERS:
            raise HTTPException(400, f"不認識的訓練器：{override}")
        if arch not in training.TRAINERS[override].trains:
            raise HTTPException(
                400, f"{training.TRAINERS[override].label} 不訓 {arch}")
    job = training.TrainJob(
        trigger=trigger, arch=arch,
        dataset_dir=str(payload.get("dataset_dir") or ""),
        output_dir=str(payload.get("output_dir") or ""),
        output_name=name,
        base_model=str(payload.get("base_model") or ""),
        image_count=max(0, count),
        trainer_override=override,
    )
    return JSONResponse(training.config_for(job))


app.mount("/static", StaticFiles(directory=STATIC), name="static")
# Reference art is served straight off disk. It never leaves the machine - the
# whole app is local - and the paths are content hashes under a per-character
# folder, so there is nothing to guess at.
config.REFS_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/refs", StaticFiles(directory=config.REFS_DIR), name="refs")


@app.get("/")
async def index() -> HTMLResponse:
    return HTMLResponse((STATIC / "index.html").read_text(encoding="utf-8"))

"""Text to speech, scene scripts, outputs and character presets."""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .. import audio, db, jobs, tts
from ..presets import holoen

router = APIRouter(prefix="/api", tags=["tts"])


class SpeakIn(BaseModel):
    model_id: str
    text: str
    language: str | None = None
    style: str = ""
    takes: int = 1
    seed: int | None = None
    screen: bool = True
    mode: str | None = None
    ref_id: str | None = None
    cfg: float | None = None
    emotion: str | None = None     # picks the reference clip and catchphrase recording; else read from the style
    phrases: bool = True           # splice original catchphrase recordings into the line


@router.post("/tts")
async def speak(body: SpeakIn):
    if not body.text.strip():
        raise HTTPException(400, "請輸入文字")
    if len(body.text) > 2000:
        raise HTTPException(400, "一次最多 2000 字；長文請用「劇本配音」分句合成")
    extra = {"cfg": body.cfg} if body.cfg else None
    try:
        return await run_in_threadpool(tts.generate, body.model_id, body.text.strip(), body.language, body.style,
                                       body.takes, body.seed, body.screen, None, body.mode, body.ref_id, extra,
                                       body.emotion or None, body.phrases)
    except KeyError:
        raise HTTPException(404, "找不到模型")
    except (ValueError, RuntimeError) as e:
        raise HTTPException(400, str(e))


@router.get("/tts/loaded")
def tts_loaded():
    return tts.loaded()


@router.post("/tts/unload")
def tts_unload():
    tts.unload()
    return {"ok": True}


@router.get("/outputs")
def outputs(model_id: str = "", favorite: bool = False, limit: int = 200, scenes: bool = False):
    where, args = ["1=1"], []
    if model_id:
        where.append("model_id=?"); args.append(model_id)
    if favorite:
        where.append("favorite=1")
    where.append("model_id IS NULL" if scenes else "model_id IS NOT NULL")
    return db.query(f"SELECT * FROM outputs WHERE {' AND '.join(where)} ORDER BY created_at DESC LIMIT ?",
                    args + [limit])


@router.get("/outputs/{oid}/audio")
def output_audio(oid: str, format: str = "wav"):
    o = db.get("outputs", oid)
    if not o or not Path(o["path"]).exists():
        raise HTTPException(404)
    if format == "mp3":
        mp3 = Path(o["path"]).with_suffix(".mp3")
        if not mp3.exists():
            audio.to_mp3(Path(o["path"]), mp3, synthetic={"output": oid})
        return FileResponse(mp3, media_type="audio/mpeg", filename=f"{oid}.mp3")
    return FileResponse(o["path"], media_type="audio/wav", filename=f"{oid}.wav")


@router.get("/outputs/{oid}/sheet")
def output_sheet(oid: str):
    """The per-line listening sheet of a rendered scene."""
    import json
    o = db.get("outputs", oid)
    if not o:
        raise HTTPException(404)
    f = Path(o["path"]).with_suffix(".json")
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else []


@router.patch("/outputs/{oid}")
def patch_output(oid: str, body: dict):
    return db.update("outputs", oid, {"favorite": 1 if body.get("favorite") else 0})


@router.delete("/outputs/{oid}")
def delete_output(oid: str):
    o = db.get("outputs", oid)
    if o:
        Path(o["path"]).unlink(missing_ok=True)
        Path(o["path"]).with_suffix(".mp3").unlink(missing_ok=True)
        db.delete("outputs", oid)
    return {"ok": True}


class ScriptIn(BaseModel):
    script: str
    cast: dict = {}
    takes: int = 2
    gap: float = 0.35
    phrases: bool = True


@router.post("/script/parse")
def script_parse(body: ScriptIn):
    ev = tts.parse_script(body.script)
    speakers = sorted({e["speaker"] for e in ev if e["kind"] == "turn" and e["speaker"].lower() != "narrator"})
    presets = {p["name"]: p for p in db.query("SELECT * FROM presets")}
    return {"events": ev, "speakers": [{"name": s, "preset": presets.get(s)} for s in speakers]}


@router.post("/script/render")
def script_render(body: ScriptIn):
    return jobs.submit("render_script", body.model_dump(), "排隊合成場景")


@router.get("/presets")
def list_presets():
    return db.query("SELECT * FROM presets ORDER BY name")


@router.post("/presets/import-holoen")
def import_holoen():
    try:
        return holoen.import_all()
    except FileNotFoundError as e:
        raise HTTPException(404, str(e))


@router.patch("/presets/{pid}")
def cast_preset(pid: str, body: dict):
    """Assign a model to a character (and optionally a default mode / reference clip for it)."""
    pr = db.get("presets", pid)
    if not pr:
        raise HTTPException(404)
    data = dict(pr["data"])
    for k in ("mode", "ref_id", "style"):
        if k in body:
            data["cast_" + k] = body[k]
    return db.update("presets", pid, {"model_id": body.get("model_id", pr["model_id"]) or None, "data": data})

"""Delivery folders: scan a folder of people, then import one person in one go (see vstudio/delivery.py)."""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import datasets, db, delivery, jobs

router = APIRouter(prefix="/api/delivery", tags=["delivery"])


class ScanIn(BaseModel):
    path: str
    bgm: str = "sep"


@router.post("/scan")
def scan(body: ScanIn):
    if body.bgm not in delivery.BGM_MODES:
        raise HTTPException(400, "bgm")
    try:
        return delivery.scan(body.path, body.bgm)
    except FileNotFoundError as e:
        raise HTTPException(400, str(e))


class ImportIn(BaseModel):
    path: str
    voice_id: str
    bgm: str = "sep"            # sep | original | skip
    common: bool = True         # common phrases are training data too
    phrase_clips: int = 8       # recordings kept per catchphrase / sound tag
    approve: bool = True        # approve clips that pass the quality checks
    build: bool = True          # build a dataset afterwards


@router.post("/import")
def start_import(body: ImportIn):
    v = db.get("voices", body.voice_id)
    if not v:
        raise HTTPException(404, "找不到這個聲音")
    if not datasets.consent_ok(v):
        raise HTTPException(409, "這個聲音還沒有完整的同意紀錄，不能匯入。請先到「聲音與同意」填好同意紀錄。")
    if body.bgm not in delivery.BGM_MODES or not 1 <= body.phrase_clips <= 30:
        raise HTTPException(400, "bgm / phrase_clips")
    root = Path(body.path.strip().strip('"')).expanduser()
    if not delivery.is_person(root):
        raise HTTPException(400, f"這不是一個人的交付資料夾（裡面沒有 交付／常用語／素材庫）：{root}")
    return jobs.submit("import_delivery", {**body.model_dump(), "path": str(root)}, f"匯入交付資料夾：{root.name}")

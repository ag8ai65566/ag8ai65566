"""The built-in tutorial: Markdown files in voice-studio/docs, shown on the 教學 page."""
from __future__ import annotations

import re

from fastapi import APIRouter, HTTPException

from .. import config

router = APIRouter(prefix="/api", tags=["docs"])
DOCS = config.ROOT / "docs"


def _docs() -> list[dict]:
    out = []
    for f in sorted(DOCS.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.M)
        out.append({"id": f.stem, "title": m.group(1).strip() if m else f.stem})
    return out


@router.get("/docs")
def list_docs():
    return _docs()


@router.get("/docs/{doc_id}")
def get_doc(doc_id: str):
    if not re.fullmatch(r"[\w-]+", doc_id):
        raise HTTPException(404)
    f = DOCS / f"{doc_id}.md"
    if not f.exists():
        raise HTTPException(404)
    return {"id": doc_id, "markdown": f.read_text(encoding="utf-8"),
            "title": next((d["title"] for d in _docs() if d["id"] == doc_id), doc_id)}

"""Character presets from the novel-lab holoen performance sheets.

Each sheet (novel-lab/projects/holoen/export/elevenlabs/<member>.md) becomes a preset:
- dialogue language (§2 "Dialogue language: Japanese"; English otherwise);
- default tags and situation → tags palette (§4), signature sounds (§5);
- reading guide (§6), what to avoid (§7), example lines (§8, with ROMAJI where given).
A preset carries style only. The voice that speaks it is whichever consented, trained model the user casts for it;
presets never contain audio of the members.
"""
from __future__ import annotations

import re
from pathlib import Path

from .. import config, db

DEFAULT_DIR = config.ROOT.parent / "novel-lab" / "projects" / "holoen" / "export" / "elevenlabs"
TAG = re.compile(r"`?\[([^\[\]\n]+)\]`?")


def _section(text: str, n: int) -> str:
    m = re.search(r"^## " + str(n) + r"\.[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def parse_sheet(text: str) -> dict | None:
    title = re.search(r"^# ElevenLabs v4 Performance Sheet: (.+)$", text, re.M)
    if not title:
        return None
    s2, s4, s5, s6, s7, s8 = (_section(text, i) for i in (2, 4, 5, 6, 7, 8))
    lang = "ja" if re.search(r"Dialogue language:\s*\**Japanese", s2) else "en"
    situations = []
    for row in s4.splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] and not cells[0].startswith(("Situation", "---")) and "`[" in cells[1]:
            tags = [t.strip() for t in TAG.findall(cells[1])]
            situations.append({"situation": cells[0], "tags": tags,
                               "example": cells[2] if len(cells) > 2 else ""})
    extra = []
    m = re.search(r"Additional proposed scene directions[^:]*:\s*(.+)", s4)
    if m:
        extra = [t.strip() for t in TAG.findall(m.group(1))]
    people = []
    m = re.search(r"With people[^:]*:\s*(.+)", s4)
    if m:
        for part in m.group(1).split(";"):
            pm = re.match(r"\s*([^`\[]+?)\s*`?\[", part)
            if pm:
                people.append({"with": pm.group(1).strip(), "tags": [t.strip() for t in TAG.findall(part)]})
    examples = []
    code = re.search(r"```\n(.*?)\n```", s8, re.S)
    if code:
        lines = code.group(1).splitlines()
        for ln in lines:
            if ln.startswith("ROMAJI ::") and examples:
                examples[-1]["romaji"] = ln.split("::", 1)[1].strip()
            elif ln.strip():
                examples.append({"text": ln.strip()})
    sounds = [t.strip() for t in TAG.findall(s5)]
    return {"character": title.group(1).strip(), "language": lang,
            "default_tags": situations[0]["tags"] if situations else [],
            "situations": situations, "extra_tags": extra, "people": people, "sounds": sounds,
            "reading_guide": s6, "avoid": s7, "examples": examples}


def import_all(directory: Path = DEFAULT_DIR) -> dict:
    """Create or refresh one preset per sheet. Existing castings (model choice) are kept."""
    if not directory.exists():
        raise FileNotFoundError(f"找不到表演表資料夾：{directory}")
    existing = {p["name"]: p for p in db.query("SELECT * FROM presets WHERE source='holoen'")}
    n_new = n_upd = 0
    for f in sorted(directory.glob("*.md")):
        data = parse_sheet(f.read_text(encoding="utf-8"))
        if not data:
            continue
        old = existing.get(data["character"])
        if old:
            db.update("presets", old["id"], {"data": data})
            n_upd += 1
        else:
            db.insert("presets", {"id": db.new_id("pre"), "name": data["character"], "source": "holoen",
                                  "model_id": None, "data": data, "created_at": db.now()})
            n_new += 1
    return {"created": n_new, "updated": n_upd}

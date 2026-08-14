"""Persistent job history and output housekeeping.

Job records used to live only in memory, so restarting the app left the videos
on disk with no way to see them in the UI. They are now appended to a JSONL
file next to the outputs and reloaded on startup.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

MAX_HISTORY = 2000
VIDEO_SUFFIXES = {".mp4", ".webm", ".gif"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}
# .webp is genuinely ambiguous: SaveAnimatedWEBP is the video fallback on
# ComfyUI installs without CreateVideo/VHS, and it is also a still format. The
# record's own `kind` decides; extension is only the fallback for orphans.
AMBIGUOUS_SUFFIXES = {".webp"}
MEDIA_SUFFIXES = VIDEO_SUFFIXES | IMAGE_SUFFIXES | AMBIGUOUS_SUFFIXES


@dataclass
class Record:
    id: str
    model_id: str
    prompt: str
    # "video" or "image". Images can produce several files from one job, so
    # `outputs` is the real field; `output` is kept as the first one for
    # backwards compatibility with history written before batches existed.
    kind: str = "video"
    outputs: list[str] = field(default_factory=list)
    fps: int = 0
    settings: dict = field(default_factory=dict)
    negative: str = ""
    negative_custom: bool = False
    prompt_raw: str = ""
    source_name: str = ""
    tier: str = ""
    length: int = 0
    seed: int = 0
    lightning: bool = False
    loras: list[str] = field(default_factory=list)
    status: str = "queued"
    message: str = ""
    output: str | None = None
    thumb: str | None = None
    width: int = 0
    height: int = 0
    created: float = field(default_factory=time.time)
    started: float | None = None
    finished: float | None = None
    starred: bool = False


class Library:
    def __init__(self, output_dir: Path, inbox_dir: Path | None = None) -> None:
        self.dir = output_dir
        self.thumbs = output_dir / ".thumbs"
        self.index = output_dir / ".history.jsonl"
        # Source images for image-to-image live here under the job's own id, so
        # "run again" still works; they are deleted with the job that owns them.
        self.inbox = inbox_dir
        self.records: dict[str, Record] = {}
        self.order: list[str] = []

    # -- persistence ---------------------------------------------------------

    def load(self) -> None:
        if not self.index.is_file():
            return
        for line in self.index.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
            except ValueError:
                continue
            known = {f for f in Record.__dataclass_fields__}
            record = Record(**{k: v for k, v in raw.items() if k in known})
            # Older records only had a single `output`.
            if record.output and not record.outputs:
                record.outputs = [record.output]
            elif record.outputs and not record.output:
                record.output = record.outputs[0]
            # A record whose video is gone is history we cannot show; drop it so
            # the gallery never offers a dead link.
            if record.status == "done" and record.outputs:
                record.outputs = [o for o in record.outputs if (self.dir / o).is_file()]
                if not record.outputs:
                    continue
                record.output = record.outputs[0]
            elif record.status in ("queued", "running"):
                # Interrupted by a restart; nothing is running now.
                record.status = "error"
                record.message = "app 重啟，這個工作沒跑完"
            self.records[record.id] = record
            self.order.append(record.id)
        self._trim()

    def save(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        lines = [
            json.dumps(asdict(self.records[i]), ensure_ascii=False)
            for i in self.order
            if i in self.records
        ]
        tmp = self.index.with_suffix(".tmp")
        tmp.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        tmp.replace(self.index)

    def _trim(self) -> None:
        while len(self.order) > MAX_HISTORY:
            self.delete(self.order[0], persist=False)

    # -- records -------------------------------------------------------------

    def add(self, record: Record) -> Record:
        self.records[record.id] = record
        self.order.append(record.id)
        self._trim()
        self.save()
        return record

    def get(self, job_id: str) -> Record | None:
        return self.records.get(job_id)

    def recent(self, limit: int = 60, kind: str = "") -> list[Record]:
        out: list[Record] = []
        for i in reversed(self.order):
            record = self.records.get(i)
            if record is None or (kind and record.kind != kind):
                continue
            out.append(record)
            if len(out) >= limit:
                break
        return out

    def delete(self, job_id: str, persist: bool = True) -> bool:
        record = self.records.pop(job_id, None)
        if record is None:
            return False
        if job_id in self.order:
            self.order.remove(job_id)
        paths = [self.dir / o for o in (record.outputs or ([record.output] if record.output else []))]
        if record.thumb:
            paths.append(self.thumbs / record.thumb)
        if self.inbox is not None and record.source_name:
            paths.append(self.inbox / f"{record.id}.png")
        for path in paths:
            if path.is_file():
                try:
                    path.unlink()
                except OSError:
                    pass
        if persist:
            self.save()
        return True

    def clear(self, keep_starred: bool = True) -> int:
        removed = 0
        for job_id in list(self.order):
            record = self.records.get(job_id)
            if keep_starred and record and record.starred:
                continue
            removed += bool(self.delete(job_id, persist=False))
        self.save()
        return removed

    def star(self, job_id: str, value: bool) -> bool:
        record = self.records.get(job_id)
        if record is None:
            return False
        record.starred = value
        self.save()
        return True

    # -- disk ----------------------------------------------------------------

    def stats(self) -> dict:
        # Which record produced each file, so kind is authoritative and only
        # unowned files fall back to guessing from the extension.
        owner = {o: r.kind for r in self.records.values() for o in r.outputs}
        files = 0
        total = 0
        videos = images = 0
        if self.dir.is_dir():
            for path in self.dir.iterdir():
                if not path.is_file() or path.suffix.lower() not in MEDIA_SUFFIXES:
                    continue
                files += 1
                total += path.stat().st_size
                kind = owner.get(path.name)
                if kind is None:
                    kind = "video" if path.suffix.lower() in VIDEO_SUFFIXES else "image"
                if kind == "video":
                    videos += 1
                else:
                    images += 1
        known = set(owner)
        on_disk_known = sum(1 for o in known if (self.dir / o).is_file())
        return {
            "dir": str(self.dir),
            "count": files,
            "videos": videos,
            "images": images,
            "bytes": total,
            "records": len(self.records),
            "orphans": max(0, files - on_disk_known),
            "starred": sum(1 for r in self.records.values() if r.starred),
        }

    def sweep_orphans(self) -> int:
        """Delete media files with no matching record (e.g. from an old run)."""
        known = {o for r in self.records.values() for o in r.outputs}
        removed = 0
        if not self.dir.is_dir():
            return 0
        for path in self.dir.iterdir():
            if not path.is_file():
                continue
            if path.suffix.lower() not in MEDIA_SUFFIXES:
                continue
            if path.name not in known:
                try:
                    path.unlink()
                    removed += 1
                except OSError:
                    pass
        return removed

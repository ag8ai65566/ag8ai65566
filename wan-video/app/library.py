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

MAX_HISTORY = 500


@dataclass
class Record:
    id: str
    model_id: str
    prompt: str
    negative: str = ""
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
    def __init__(self, output_dir: Path) -> None:
        self.dir = output_dir
        self.thumbs = output_dir / ".thumbs"
        self.index = output_dir / ".history.jsonl"
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
            # A record whose video is gone is history we cannot show; drop it so
            # the gallery never offers a dead link.
            if record.status == "done" and record.output:
                if not (self.dir / record.output).is_file():
                    continue
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

    def recent(self, limit: int = 60) -> list[Record]:
        return [self.records[i] for i in reversed(self.order[-limit:]) if i in self.records]

    def delete(self, job_id: str, persist: bool = True) -> bool:
        record = self.records.pop(job_id, None)
        if record is None:
            return False
        if job_id in self.order:
            self.order.remove(job_id)
        for path in (
            self.dir / record.output if record.output else None,
            self.thumbs / record.thumb if record.thumb else None,
        ):
            if path and path.is_file():
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
        videos = 0
        video_bytes = 0
        if self.dir.is_dir():
            for path in self.dir.iterdir():
                if path.is_file() and path.suffix.lower() in (".mp4", ".webm", ".webp", ".gif"):
                    videos += 1
                    video_bytes += path.stat().st_size
        orphans = videos - sum(
            1 for r in self.records.values() if r.output and (self.dir / r.output).is_file()
        )
        return {
            "dir": str(self.dir),
            "count": videos,
            "bytes": video_bytes,
            "records": len(self.records),
            "orphans": max(0, orphans),
            "starred": sum(1 for r in self.records.values() if r.starred),
        }

    def sweep_orphans(self) -> int:
        """Delete video files with no matching record (e.g. from an old run)."""
        known = {r.output for r in self.records.values() if r.output}
        removed = 0
        if not self.dir.is_dir():
            return 0
        for path in self.dir.iterdir():
            if not path.is_file():
                continue
            if path.suffix.lower() not in (".mp4", ".webm", ".webp", ".gif"):
                continue
            if path.name not in known:
                try:
                    path.unlink()
                    removed += 1
                except OSError:
                    pass
        return removed

"""Downloads model files into the ComfyUI models tree, resumably.

Runs as a single background task so two downloads never fight for bandwidth.
Progress is polled by the UI rather than pushed, which keeps this simple and
survives a page reload.
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field
from pathlib import Path

import aiohttp
import registry
from registry import ModelDef, ModelFile

CHUNK = 1 << 20  # 1 MiB
HF = "https://huggingface.co"


def url_for(file: ModelFile) -> str:
    return f"{HF}/{file.repo}/resolve/main/{file.path}"


@dataclass
class FileState:
    file: ModelFile
    done: int = 0
    status: str = "pending"  # pending | downloading | done | error
    message: str = ""

    def public(self) -> dict:
        return {
            "name": self.file.name,
            "folder": self.file.folder,
            "size": self.file.size,
            "done": self.done,
            "status": self.status,
            "message": self.message,
        }


@dataclass
class Download:
    model_id: str
    label: str
    files: list[FileState]
    status: str = "queued"  # queued | running | done | error | cancelled
    message: str = ""
    started: float = field(default_factory=time.time)
    finished: float | None = None

    @property
    def total(self) -> int:
        return sum(f.file.size for f in self.files)

    @property
    def done_bytes(self) -> int:
        return sum(f.done for f in self.files)

    def public(self) -> dict:
        total = self.total
        elapsed = (self.finished or time.time()) - self.started
        done = self.done_bytes
        rate = done / elapsed if elapsed > 1 and self.status == "running" else 0
        remaining = (total - done) / rate if rate > 0 else None
        return {
            "model": self.model_id,
            "label": self.label,
            "status": self.status,
            "message": self.message,
            "total": total,
            "done": done,
            "progress": round(done / total, 4) if total else 0,
            "rate": round(rate),
            "eta": round(remaining) if remaining else None,
            "files": [f.public() for f in self.files],
        }


class Manager:
    """Tracks what is installed and runs one download at a time."""

    def __init__(self, models_dir: Path) -> None:
        self.root = models_dir
        self.queue: asyncio.Queue[Download] = asyncio.Queue()
        self.current: Download | None = None
        self.history: dict[str, Download] = {}
        self._cancel = False
        self._worker: asyncio.Task | None = None

    # -- installed state ----------------------------------------------------

    def path_for(self, file: ModelFile) -> Path:
        return self.root / file.folder / file.name

    def file_status(self, file: ModelFile) -> tuple[str, int]:
        """('missing' | 'partial' | 'ok', bytes_on_disk)."""
        path = self.path_for(file)
        if not path.exists():
            return "missing", 0
        size = path.stat().st_size
        if size == file.size:
            return "ok", size
        return "partial", size

    def model_status(self, model: ModelDef) -> dict:
        states = [(f, *self.file_status(f)) for f in model.all_files]
        required = [(f, s, n) for f, s, n in states if f not in model.lightning]
        on_disk = sum(n for _, _, n in states)
        installed = all(s == "ok" for _, s, _ in required)
        return {
            "installed": installed,
            "partial": not installed and on_disk > 0,
            "bytes_on_disk": on_disk,
            "missing": [f.name for f, s, _ in states if s != "ok"],
        }

    def missing_files(self, model: ModelDef) -> list[ModelFile]:
        return [f for f in model.all_files if self.file_status(f)[0] != "ok"]

    # -- queueing -----------------------------------------------------------

    def start(self) -> None:
        if self._worker is None or self._worker.done():
            self._worker = asyncio.create_task(self._run())

    def stop(self) -> asyncio.Task | None:
        """Hand the worker task back so the caller can cancel it on shutdown."""
        return self._worker

    def enqueue(self, model: ModelDef) -> Download:
        pending = self.missing_files(model)
        download = Download(
            model_id=model.id,
            label=model.label,
            files=[FileState(f) for f in pending],
        )
        # Files already on disk still count toward the totals, so the bar
        # reflects the model rather than only this session's work.
        for f in model.all_files:
            if f not in pending:
                download.files.append(FileState(f, done=f.size, status="done"))
        if not pending:
            download.status = "done"
            download.finished = time.time()
        self.history[model.id] = download
        if pending:
            self.queue.put_nowait(download)
        self.start()
        return download

    def cancel(self) -> bool:
        if self.current and self.current.status == "running":
            self._cancel = True
            return True
        return False

    def state(self) -> dict:
        return {
            "current": self.current.public() if self.current else None,
            "queued": self.queue.qsize(),
            "recent": [d.public() for d in list(self.history.values())[-6:]],
        }

    # -- the worker ---------------------------------------------------------

    async def _run(self) -> None:
        while True:
            download = await self.queue.get()
            self.current = download
            self._cancel = False
            download.status = "running"
            download.started = time.time()
            try:
                async with aiohttp.ClientSession() as session:
                    for state in download.files:
                        if state.status == "done":
                            continue
                        if self._cancel:
                            break
                        await self._fetch(session, state)
                download.status = "cancelled" if self._cancel else "done"
            except asyncio.CancelledError:
                download.status = "cancelled"
                raise
            except Exception as exc:  # noqa: BLE001 - the manager must survive
                download.status = "error"
                download.message = f"{type(exc).__name__}: {exc}"
            finally:
                download.finished = time.time()
                self.current = None
                self.queue.task_done()

    async def _fetch(self, session: aiohttp.ClientSession, state: FileState) -> None:
        target = self.path_for(state.file)
        target.parent.mkdir(parents=True, exist_ok=True)
        part = target.with_suffix(target.suffix + ".part")

        # Resume from whatever a previous run left behind.
        existing = part.stat().st_size if part.exists() else 0
        if existing > state.file.size:
            existing = 0
            part.unlink(missing_ok=True)

        state.status = "downloading"
        state.done = existing
        headers = {"Range": f"bytes={existing}-"} if existing else {}

        for attempt in range(5):
            try:
                # No total timeout (files run to 30GB), but a stalled socket
                # must fail fast enough to retry rather than wedge the queue.
                timeout = aiohttp.ClientTimeout(total=None, sock_connect=30, sock_read=60)
                async with session.get(url_for(state.file), headers=headers, timeout=timeout) as response:
                    if existing and response.status == 416:
                        break  # already complete
                    if response.status not in (200, 206):
                        raise RuntimeError(f"HTTP {response.status} for {state.file.path}")
                    mode = "ab" if response.status == 206 else "wb"
                    if mode == "wb":
                        state.done = 0
                    with part.open(mode) as fh:
                        async for chunk in response.content.iter_chunked(CHUNK):
                            if self._cancel:
                                state.status = "pending"
                                return
                            fh.write(chunk)
                            state.done += len(chunk)
                break
            except (aiohttp.ClientError, asyncio.TimeoutError, OSError) as exc:
                if attempt == 4:
                    state.status = "error"
                    state.message = str(exc)
                    raise
                await asyncio.sleep(2 ** attempt)
                existing = part.stat().st_size if part.exists() else 0
                state.done = existing
                headers = {"Range": f"bytes={existing}-"} if existing else {}

        if self._cancel:
            state.status = "pending"
            return

        actual = part.stat().st_size if part.exists() else 0
        if actual != state.file.size:
            state.status = "error"
            state.message = f"大小不符：拿到 {actual}，應該是 {state.file.size}"
            raise RuntimeError(state.message)

        part.replace(target)
        state.status = "done"
        state.done = state.file.size

    # -- LoRAs the user dropped in themselves -------------------------------

    def list_loras(self) -> list[dict]:
        folder = self.root / "loras"
        if not folder.is_dir():
            return []
        known = {f.name for m in registry.MODELS for f in m.lightning}
        out = []
        for path in sorted(folder.glob("*.safetensors")):
            out.append(
                {
                    "name": path.name,
                    "size": path.stat().st_size,
                    "builtin": path.name in known,
                }
            )
        return out

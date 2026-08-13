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


@dataclass(frozen=True)
class RemoteFile:
    """A file to fetch from an arbitrary URL, e.g. a CivitAI LoRA.

    Mirrors the parts of ModelFile the fetcher uses, so both kinds flow through
    the same queue, resume logic and progress reporting. `size` may be 0 when
    the source does not tell us up front; the fetcher then trusts Content-Length
    instead of failing the size check.
    """

    url: str
    folder: str
    name: str
    size: int = 0
    headers: tuple[tuple[str, str], ...] = ()
    label: str = ""

    @property
    def header_dict(self) -> dict:
        return dict(self.headers)


def url_for(file: ModelFile | RemoteFile) -> str:
    if isinstance(file, RemoteFile):
        return file.url
    return f"{HF}/{file.repo}/resolve/main/{file.path}"


def headers_for(file: ModelFile | RemoteFile) -> dict:
    return file.header_dict if isinstance(file, RemoteFile) else {}


@dataclass
class FileState:
    file: ModelFile | RemoteFile
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
    kind: str = "model"  # model | lora
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
            "kind": self.kind,
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
        self._sidecars: dict[str, dict] = {}

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

    def enqueue_files(
        self,
        *,
        key: str,
        label: str,
        files: list[RemoteFile],
        kind: str = "lora",
        sidecars: dict[str, dict] | None = None,
    ) -> Download:
        """Queue arbitrary remote files, e.g. a CivitAI LoRA.

        `sidecars` maps a filename to metadata written next to it as
        <name>.civitai.json, so trigger words survive past the download.
        """
        pending: list[RemoteFile] = []
        already: list[RemoteFile] = []
        for f in files:
            target = self.root / f.folder / f.name
            # Without a known size, presence alone has to count as installed.
            if target.exists() and (not f.size or target.stat().st_size == f.size):
                already.append(f)
            else:
                pending.append(f)

        download = Download(
            model_id=key,
            label=label,
            kind=kind,
            files=[FileState(f) for f in pending]
            + [FileState(f, done=f.size or 1, status="done") for f in already],
        )
        self._sidecars.update(sidecars or {})
        if not pending:
            download.status = "done"
            download.finished = time.time()
        self.history[key] = download
        if pending:
            self.queue.put_nowait(download)
        self.start()
        return download

    # -- LoRAs the user installed -------------------------------------------

    def lora_path(self, name: str) -> Path:
        """Resolve a LoRA filename inside models/loras, refusing escapes."""
        folder = (self.root / "loras").resolve()
        path = (folder / name).resolve()
        if folder != path.parent or not path.name:
            raise ValueError(f"不合法的 LoRA 檔名：{name}")
        return path

    def delete_lora(self, name: str) -> bool:
        path = self.lora_path(name)
        if not path.is_file():
            return False
        path.unlink()
        for suffix in (".civitai.json", ".json"):
            meta = path.with_name(path.name + suffix)
            if meta.is_file():
                meta.unlink()
        return True

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
        headers = dict(headers_for(state.file))
        if existing:
            headers["Range"] = f"bytes={existing}-"

        for attempt in range(5):
            try:
                # No total timeout (files run to 30GB), but a stalled socket
                # must fail fast enough to retry rather than wedge the queue.
                timeout = aiohttp.ClientTimeout(total=None, sock_connect=30, sock_read=60)
                async with session.get(url_for(state.file), headers=headers, timeout=timeout) as response:
                    if existing and response.status == 416:
                        break  # already complete
                    if response.status in (401, 403):
                        raise RuntimeError(
                            f"HTTP {response.status}：這個來源需要有效的 API key"
                            f"（{state.file.name}）"
                        )
                    if response.status not in (200, 206):
                        raise RuntimeError(f"HTTP {response.status} for {state.file.name}")
                    # Learn the real size when the catalogue did not know it.
                    if not state.file.size:
                        declared = response.content_length or 0
                        if declared:
                            object.__setattr__(state.file, "size", declared + existing)
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
                headers = dict(headers_for(state.file))
                if existing:
                    headers["Range"] = f"bytes={existing}-"

        if self._cancel:
            state.status = "pending"
            return

        actual = part.stat().st_size if part.exists() else 0
        if state.file.size and actual != state.file.size:
            state.status = "error"
            state.message = f"大小不符：拿到 {actual}，應該是 {state.file.size}"
            raise RuntimeError(state.message)
        if not actual:
            state.status = "error"
            state.message = "下載到 0 位元組"
            raise RuntimeError(state.message)

        part.replace(target)
        state.status = "done"
        state.done = state.file.size or actual

        # Keep trigger words etc. next to the weights, so the UI can show them
        # for an installed LoRA without going back to CivitAI.
        if meta := self._sidecars.pop(state.file.name, None):
            import json

            target.with_name(target.name + ".civitai.json").write_text(
                json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8"
            )

    # -- LoRAs the user dropped in themselves -------------------------------

    def list_loras(self) -> list[dict]:
        folder = self.root / "loras"
        if not folder.is_dir():
            return []
        known = {f.name for m in registry.MODELS for f in m.lightning}
        out = []
        for path in sorted(folder.glob("*.safetensors")):
            entry = {
                "name": path.name,
                "size": path.stat().st_size,
                "builtin": path.name in known,
                "trained_words": [],
                "source": "",
                "base_model": "",
            }
            sidecar = path.with_name(path.name + ".civitai.json")
            if sidecar.is_file():
                import json

                try:
                    meta = json.loads(sidecar.read_text(encoding="utf-8"))
                    entry["trained_words"] = meta.get("trained_words") or []
                    entry["source"] = meta.get("url") or ""
                    entry["base_model"] = meta.get("base_model") or ""
                except (ValueError, OSError):
                    pass
            out.append(entry)
        return out

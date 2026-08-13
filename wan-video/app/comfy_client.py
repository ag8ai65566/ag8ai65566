"""Thin async client for the ComfyUI HTTP + websocket API."""

from __future__ import annotations

import asyncio
import json
import uuid
from dataclasses import dataclass

import aiohttp


class ComfyError(RuntimeError):
    pass


# Combo inputs whose choices are a live directory listing rather than a fixed
# set. /object_info is cached, so a file we uploaded seconds ago will not appear
# in it - checking those values would reject every freshly uploaded image.
DYNAMIC_COMBOS = {("LoadImage", "image"), ("LoadImageMask", "image")}


@dataclass
class OutputFile:
    filename: str
    subfolder: str
    type: str


class ComfyClient:
    def __init__(self, base_url: str) -> None:
        self.base = base_url.rstrip("/")
        self.client_id = str(uuid.uuid4())
        self._object_info: dict | None = None

    # -- lifecycle ----------------------------------------------------------

    async def wait_until_ready(self, timeout: float = 900.0) -> None:
        """ComfyUI can take a while to boot (model scan, custom nodes)."""
        deadline = asyncio.get_event_loop().time() + timeout
        last: Exception | None = None
        while asyncio.get_event_loop().time() < deadline:
            try:
                async with aiohttp.ClientSession() as s:
                    async with s.get(f"{self.base}/system_stats", timeout=10) as r:
                        if r.status == 200:
                            return
            except Exception as exc:  # noqa: BLE001 - retry on anything
                last = exc
            await asyncio.sleep(2)
        raise ComfyError(f"ComfyUI at {self.base} never became ready: {last}")

    async def system_stats(self) -> dict:
        """Includes per-device vram_total / vram_free, so the UI can report the
        real card instead of asking the user to read Task Manager."""
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.base}/system_stats", timeout=30) as r:
                r.raise_for_status()
                return await r.json()

    async def object_info(self, refresh: bool = False) -> dict:
        if self._object_info is None or refresh:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{self.base}/object_info", timeout=120) as r:
                    r.raise_for_status()
                    self._object_info = await r.json()
        return self._object_info

    def invalidate(self) -> None:
        """Drop the cached schema.

        /object_info embeds the *current* contents of every model folder. Once
        cached, a model downloaded afterwards is invisible to validate(), which
        then rejects a graph for a model that is sitting right there on disk.
        Anything that changes models/ must call this.
        """
        self._object_info = None

    async def node_classes(self) -> set[str]:
        return set((await self.object_info()).keys())

    # -- validation ---------------------------------------------------------

    async def validate(self, graph: dict) -> list[str]:
        """Check node classes and required inputs against the live schema.

        Returns a list of human-readable problems; empty means the graph should
        be accepted. Catching this here gives a far better error message than
        ComfyUI's own 400 response.
        """
        info = await self.object_info()
        problems: list[str] = []

        for node_id, node in graph.items():
            cls = node["class_type"]
            schema = info.get(cls)
            if schema is None:
                problems.append(
                    f"node {node_id}: ComfyUI has no node type '{cls}' "
                    "(missing custom node package?)"
                )
                continue

            spec = schema.get("input", {})
            required = spec.get("required", {})
            optional = spec.get("optional", {})
            known = set(required) | set(optional) | {"hidden"}
            given = set(node["inputs"])

            for missing in set(required) - given:
                problems.append(f"node {node_id} ({cls}): missing input '{missing}'")
            for unknown in given - known:
                problems.append(f"node {node_id} ({cls}): unexpected input '{unknown}'")

            # For combo inputs, check the literal value is one of the choices.
            for name, value in node["inputs"].items():
                if isinstance(value, list) and len(value) == 2 and isinstance(value[1], int):
                    continue  # a link, not a literal
                if (cls, name) in DYNAMIC_COMBOS:
                    continue
                entry = required.get(name) or optional.get(name)
                if not entry:
                    continue
                choices = entry[0]
                if not isinstance(choices, list):
                    continue
                if not choices:
                    # An empty combo means the folder ComfyUI scans for this
                    # input has no files at all, so nothing could be valid.
                    problems.append(
                        f"node {node_id} ({cls}): ComfyUI has no files to offer for "
                        f"'{name}' — '{value}' is not installed (empty model folder)"
                    )
                elif value not in choices:
                    shown = ", ".join(str(c) for c in choices[:8])
                    problems.append(
                        f"node {node_id} ({cls}): '{value}' is not a valid {name}. "
                        f"Available: {shown}{' ...' if len(choices) > 8 else ''}"
                    )

        return problems

    # -- inputs -------------------------------------------------------------

    async def upload_image(self, data: bytes, filename: str) -> str:
        """Upload into ComfyUI's input dir; returns the name LoadImage expects."""
        form = aiohttp.FormData()
        form.add_field("image", data, filename=filename, content_type="image/png")
        form.add_field("overwrite", "true")
        form.add_field("subfolder", "wan-drop")
        async with aiohttp.ClientSession() as s:
            async with s.post(f"{self.base}/upload/image", data=form, timeout=120) as r:
                if r.status != 200:
                    raise ComfyError(f"upload failed ({r.status}): {await r.text()}")
                body = await r.json()
        name = body["name"]
        sub = body.get("subfolder") or ""
        return f"{sub}/{name}" if sub else name

    # -- execution ----------------------------------------------------------

    async def queue(self, graph: dict) -> str:
        payload = {"prompt": graph, "client_id": self.client_id}
        async with aiohttp.ClientSession() as s:
            async with s.post(f"{self.base}/prompt", json=payload, timeout=120) as r:
                text = await r.text()
                if r.status != 200:
                    raise ComfyError(f"ComfyUI rejected the graph ({r.status}): {text}")
                return json.loads(text)["prompt_id"]

    async def run(self, graph: dict, on_progress=None) -> list[OutputFile]:
        """Queue the graph and wait for it, reporting progress as 0.0-1.0."""
        ws_url = self.base.replace("https://", "wss://").replace("http://", "ws://")
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(
                f"{ws_url}/ws?clientId={self.client_id}", heartbeat=30
            ) as ws:
                prompt_id = await self.queue(graph)
                async for msg in ws:
                    if msg.type is not aiohttp.WSMsgType.TEXT:
                        continue
                    event = json.loads(msg.data)
                    kind, data = event.get("type"), event.get("data", {})
                    if data.get("prompt_id") not in (None, prompt_id):
                        continue

                    if kind == "progress" and on_progress:
                        maximum = data.get("max") or 1
                        on_progress(data.get("value", 0) / maximum)
                    elif kind == "execution_error":
                        raise ComfyError(
                            f"{data.get('node_type')}: {data.get('exception_message')}"
                        )
                    elif kind == "execution_interrupted":
                        raise ComfyError("execution interrupted")
                    elif kind == "executing" and data.get("node") is None:
                        break  # this prompt is done

        return await self.outputs(prompt_id)

    async def outputs(self, prompt_id: str) -> list[OutputFile]:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.base}/history/{prompt_id}", timeout=60) as r:
                r.raise_for_status()
                history = await r.json()

        entry = history.get(prompt_id) or {}
        status = entry.get("status", {})
        if status.get("status_str") == "error":
            raise ComfyError(f"execution failed: {json.dumps(status)[:500]}")

        files: list[OutputFile] = []
        # Output keys vary by save node (images / videos / gifs), so scan them all.
        for node_output in (entry.get("outputs") or {}).values():
            for items in node_output.values():
                if not isinstance(items, list):
                    continue
                for item in items:
                    if isinstance(item, dict) and item.get("filename"):
                        files.append(
                            OutputFile(
                                filename=item["filename"],
                                subfolder=item.get("subfolder", ""),
                                type=item.get("type", "output"),
                            )
                        )
        # Drop the preview frames some nodes emit alongside the video.
        videos = [f for f in files if f.filename.lower().endswith((".mp4", ".webm", ".webp", ".gif"))]
        return videos or files

    async def download(self, out: OutputFile) -> bytes:
        params = {"filename": out.filename, "subfolder": out.subfolder, "type": out.type}
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.base}/view", params=params, timeout=300) as r:
                r.raise_for_status()
                return await r.read()

    async def interrupt(self) -> None:
        async with aiohttp.ClientSession() as s:
            await s.post(f"{self.base}/interrupt", timeout=30)

"""Rent a GPU on Runpod and use it as this app's ComfyUI.

Why this exists
---------------
The models worth using have outgrown a home graphics card. MiniMax H3 is 44GB
of weights and wants 24GB of VRAM before it stops swapping; the machine this
app was first run on has 10. No amount of software closes that gap. A rented
card does, for the minutes it is actually working.

This app is a ComfyUI front end, so the rented machine is simply *another
ComfyUI*: the same graphs, the same client, a different address. Everything
here is about getting that address to exist, getting the model files onto the
machine behind it, and - the part that matters most - making sure it stops
costing money when nobody is using it.

What was checked, and against what
----------------------------------
Every endpoint, field name and enum below was read out of Runpod's own REST
API v2 schema (``https://api.runpod.io/v2/openapi.json``, fetched 2026-11-12),
not from memory. That is not pedantry: v1 of the same API is retired on
2026-11-15, three days after this was written, and the first draft of this
module was built on it.

What was *not* checked: a real rental. This project has no Runpod account and
no GPU, so the first real boot happens on the user's own key. Two things make
that survivable - the machine reports its own boot log through the agent (see
``cloud/agent.py``), and if even the agent never comes up, the log is read
through Runpod's exec endpoint instead.

Money
-----
Three rules, each of which exists because the alternative is a bill:

* Nothing here rents a machine on its own the first time. The user picks a
  card and presses the button, with the hourly price on it.
* An idle machine is terminated after ``idle_minutes``. Storage is a network
  volume, so terminating loses nothing - the models are still there next time.
* The machine also watches for this app going away (``cloud/agent.py``'s
  dead-man switch), because the commonest way to leave a GPU running overnight
  is to close the laptop.
"""

from __future__ import annotations

import asyncio
import json
import os
import secrets
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

import aiohttp

API_DEFAULT = "https://api.runpod.io"
PROXY_DEFAULT = "https://{pod}-{port}.proxy.runpod.net"
COMFY_PORT = 8188
AGENT_PORT = 8189
MOUNT = "/workspace"
ROOT = MOUNT + "/wan"
POD_NAME = "wan-video"
VOLUME_NAME = "wan-video-models"
UA = "wan-video/1.0 (+local ComfyUI front-end)"

# What gets run on the machine. Each is a default, overridable from `.env`,
# because all three name something that will move: the image tag, the ComfyUI
# release, and the branch this repository happens to live on today.
IMAGE_DEFAULT = "runpod/comfyui:latest"
COMFY_REF_DEFAULT = "v0.45.0"
REPO_RAW_DEFAULT = ("https://raw.githubusercontent.com/ag8ai65566/ag8ai65566/"
                    "claude/local-image-to-animation-ai-375zyw/wan-video")

TIERS = ("SECURE", "COMMUNITY")
# How long each stage is allowed before we stop waiting and say so. Generous,
# because the first boot pulls an image and installs a Python environment.
PROVISION_TIMEOUT = 20 * 60
BOOT_TIMEOUT = 25 * 60
UPLOAD_CHUNK = 32 << 20


def api_key() -> str:
    """Read on every call, so pasting the key in settings works immediately."""
    return (os.environ.get("RUNPOD_API_KEY") or "").strip()


def api_base() -> str:
    return (os.environ.get("RUNPOD_API_URL") or API_DEFAULT).rstrip("/")


def proxy_url(pod_id: str, port: int) -> str:
    template = os.environ.get("RUNPOD_PROXY_TEMPLATE") or PROXY_DEFAULT
    return template.format(pod=pod_id, port=port)


def image_name() -> str:
    return (os.environ.get("RUNPOD_IMAGE") or IMAGE_DEFAULT).strip()


def comfy_ref() -> str:
    return (os.environ.get("CLOUD_COMFY_REF") or COMFY_REF_DEFAULT).strip()


def repo_raw() -> str:
    return (os.environ.get("CLOUD_REPO_RAW") or REPO_RAW_DEFAULT).strip().rstrip("/")


class CloudError(RuntimeError):
    """Something about the rented machine that the user has to know about."""


class NeedsKey(CloudError):
    pass


def _explain(status: int, body: str) -> str:
    """Turn an API refusal into a sentence about what to do.

    Runpod's own message is kept at the end: it is usually the only part that
    says *which* field or limit was the problem.
    """
    # v2 answers every refusal as {title, status, detail, errors: [str]} -
    # `errors` is where a rejected field is actually named.
    detail = ""
    try:
        data = json.loads(body)
        if isinstance(data, dict):
            parts = [str(data.get("detail") or data.get("title") or "")]
            if isinstance(data.get("errors"), list):
                parts += [str(e) for e in data["errors"][:4]]
            detail = "；".join(part for part in parts if part)
    except ValueError:
        detail = body.strip()[:300]
    tail = f"（Runpod：{detail[:400]}）" if detail else ""
    if status == 401:
        return "Runpod 不認這把 API key。到「設定」分頁重新貼一次，注意不要多貼到空白。" + tail
    if status == 403:
        return ("這把 Runpod API key 的權限不夠。建立 key 的時候要給 Pods 和 "
                "Network Volumes 的讀寫權限（或直接選 All）。" + tail)
    if status == 404:
        return "Runpod 那邊找不到這個東西，可能已經被刪掉了。" + tail
    if status == 429:
        return "Runpod 說請求太頻繁，等一下再試。" + tail
    if status in (400, 409, 422):
        return "Runpod 拒絕了這個請求。" + tail
    if status >= 500:
        return f"Runpod 那邊出錯了（HTTP {status}），不是你這邊的問題，等一下再試。" + tail
    return f"Runpod 回了 HTTP {status}。" + tail


class Api:
    """The handful of Runpod REST v2 calls this app needs."""

    async def _request(self, method: str, path: str, *, payload: dict | None = None,
                       params: dict | None = None, timeout: float = 60) -> tuple[int, str]:
        key = api_key()
        if not key:
            raise NeedsKey("還沒有填 Runpod API key。到「設定」分頁貼上。")
        headers = {"Authorization": f"Bearer {key}", "User-Agent": UA,
                   "Accept": "application/json"}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(
                        method, api_base() + path, json=payload, params=params,
                        headers=headers, timeout=timeout) as response:
                    return response.status, await response.text()
        except asyncio.TimeoutError as exc:
            raise CloudError("Runpod 的 API 沒有回應（逾時）。等一下再試。") from exc
        except aiohttp.ClientError as exc:
            raise CloudError(f"連不上 Runpod 的 API：{type(exc).__name__}。"
                             "檢查這台電腦的網路。") from exc

    async def _json(self, method: str, path: str, **kwargs):
        status, body = await self._request(method, path, **kwargs)
        if status == 204 or (200 <= status < 300 and not body.strip()):
            return {}
        if not 200 <= status < 300:
            raise CloudError(_explain(status, body))
        try:
            return json.loads(body)
        except ValueError as exc:
            raise CloudError("Runpod 回了一段看不懂的內容。") from exc

    # -- catalogue -----------------------------------------------------------

    async def gpus(self, tier: str) -> list[dict]:
        data = await self._json("GET", "/v2/catalog/gpus", params={
            "include": "AVAILABILITY", "product": "POD",
            "cloud": tier if tier in TIERS else "SECURE", "count": "1"})
        return list(data.get("gpus") or [])

    # -- volumes -------------------------------------------------------------

    async def volumes(self) -> list[dict]:
        data = await self._json("GET", "/v2/network-volumes")
        return list(data.get("networkVolumes") or []) if isinstance(data, dict) else []

    async def create_volume(self, data_center: str, size_gb: int) -> dict:
        return await self._json("POST", "/v2/network-volumes", payload={
            "dataCenter": data_center, "name": VOLUME_NAME, "size": int(size_gb)})

    async def delete_volume(self, volume_id: str) -> None:
        status, body = await self._request("DELETE", f"/v2/network-volumes/{volume_id}")
        if status not in (200, 204, 404):
            raise CloudError(_explain(status, body))

    # -- pods ----------------------------------------------------------------

    async def pod(self, pod_id: str) -> dict | None:
        status, body = await self._request("GET", f"/v2/pods/{pod_id}")
        if status == 404:
            return None
        if not 200 <= status < 300:
            raise CloudError(_explain(status, body))
        return json.loads(body)

    async def pods(self) -> list[dict]:
        data = await self._json("GET", "/v2/pods")
        return list(data.get("pods") or []) if isinstance(data, dict) else []

    async def create_pod(self, body: dict) -> dict:
        return await self._json("POST", "/v2/pods", payload=body, timeout=120)

    async def terminate(self, pod_id: str) -> None:
        status, body = await self._request("DELETE", f"/v2/pods/{pod_id}")
        if status not in (200, 204, 404):
            raise CloudError(_explain(status, body))

    async def run(self, pod_id: str, argv: list[str], seconds: int = 20) -> dict:
        """Run one command in the container. For reading a log, nothing more."""
        status, body = await self._request(
            "POST", f"/v2/pods/{pod_id}/exec",
            payload={"command": argv, "timeoutSeconds": max(1, min(seconds, 25))},
            timeout=45)
        if not 200 <= status < 300:
            return {"stdout": "", "stderr": "", "exitCode": None, "unavailable": status}
        try:
            return json.loads(body)
        except ValueError:
            return {"stdout": "", "stderr": "", "exitCode": None}


def pod_body(*, gpu_id: str, tier: str, volume_id: str, data_center: str,
             token: str, deadman_minutes: int, comfy_args: str = "") -> dict:
    """The request that rents the machine. Pure, so it can be tested.

    The image's own entrypoint starts an older ComfyUI than this app's graphs
    are written for, so it is replaced: the machine downloads this project's
    boot script and runs that instead. Two ports are published and no others -
    ComfyUI and the agent. The image also ships a file browser and a notebook
    server with default passwords; they are never exposed.
    """
    env = {
        "WAN_AGENT_TOKEN": token,
        "WAN_REPO_RAW": repo_raw(),
        "WAN_COMFY_REF": comfy_ref(),
        "WAN_ROOT": ROOT,
        "WAN_DEADMAN_MINUTES": str(max(0, int(deadman_minutes))),
    }
    if comfy_args.strip():
        env["WAN_COMFY_ARGS"] = comfy_args.strip()
    return {
        "name": POD_NAME,
        "image": image_name(),
        "cloud": tier if tier in TIERS else "SECURE",
        "gpu": {"id": gpu_id, "count": 1},
        "disk": 20,
        "dataCenterIds": [data_center],
        "mounts": {"network": [{"volumeId": volume_id, "path": MOUNT}]},
        "ports": [f"{COMFY_PORT}/http", f"{AGENT_PORT}/http"],
        "env": env,
        "entrypoint": ["bash", "-c"],
        "cmd": ['curl -fsSL --retry 5 "$WAN_REPO_RAW/cloud/bootstrap.sh" | bash'],
    }


class Agent:
    """Client for ``cloud/agent.py`` on the rented machine."""

    def __init__(self, base: str, token: str) -> None:
        self.base = base.rstrip("/")
        self.token = token

    async def _call(self, method: str, path: str, *, payload: dict | None = None,
                    data: bytes | None = None, params: dict | None = None,
                    auth: bool = True, timeout: float = 30) -> dict:
        headers = {"User-Agent": UA}
        if auth:
            headers["X-Wan-Token"] = self.token
        async with aiohttp.ClientSession() as session:
            async with session.request(method, self.base + path, json=payload, data=data,
                                       params=params, headers=headers,
                                       timeout=timeout) as response:
                text = await response.text()
                try:
                    body = json.loads(text)
                except ValueError:
                    body = {}
                if response.status == 401:
                    raise CloudError("雲端機不認這個 app 的憑證 —— 這台機器不是這個 app 開的，"
                                     "或設定檔被換過。關掉它重新開一台。")
                if response.status >= 400:
                    raise CloudError(str(body.get("error") or f"雲端機回了 HTTP {response.status}"))
                return body if isinstance(body, dict) else {}

    async def status(self) -> dict:
        return await self._call("GET", "/status", auth=False, timeout=15)

    async def ping(self) -> None:
        """Tell the machine this app is still here (its dead-man switch)."""
        await self._call("POST", "/ping", timeout=15)

    async def files(self) -> list[dict]:
        return list((await self._call("GET", "/files")).get("files") or [])

    async def downloads(self) -> dict:
        return dict((await self._call("GET", "/downloads")).get("items") or {})

    async def gpu(self) -> dict:
        return dict((await self._call("GET", "/gpu")).get("gpu") or {})

    async def log(self, name: str = "comfy", tail: int = 80) -> list[str]:
        return list((await self._call("GET", "/log", params={
            "name": name, "tail": str(tail)})).get("lines") or [])

    async def download(self, *, url: str, folder: str, name: str, size: int,
                       headers: dict) -> dict:
        return await self._call("POST", "/download", payload={
            "url": url, "folder": folder, "name": name, "size": int(size or 0),
            "headers": headers or {}})

    async def train(self, spec: dict) -> dict:
        return await self._call("POST", "/train", payload=spec, timeout=60)

    async def train_status(self) -> dict:
        return await self._call("GET", "/train", timeout=20)

    async def train_stop(self) -> dict:
        return await self._call("POST", "/train/stop", payload={}, timeout=20)

    async def fetch_file(self, folder: str, name: str, dest: Path, on_progress=None) -> int:
        """Pull a file off the machine (a trained LoRA) in slices, like upload in reverse."""
        part = dest.with_name(dest.name + ".part")
        dest.parent.mkdir(parents=True, exist_ok=True)
        offset, total = 0, None
        headers = {"User-Agent": UA, "X-Wan-Token": self.token}
        async with aiohttp.ClientSession(headers=headers) as session:
            with part.open("wb") as handle:
                while total is None or offset < total:
                    async with session.get(self.base + "/file", timeout=95, params={
                            "folder": folder, "name": name, "offset": str(offset)}) as response:
                        if response.status != 200:
                            raise CloudError(f"從雲端機抓 {name} 失敗（HTTP {response.status}）")
                        total = int(response.headers.get("X-Total-Size") or 0)
                        chunk = await response.read()
                    if not chunk:
                        break
                    handle.write(chunk)
                    offset += len(chunk)
                    if on_progress and total:
                        on_progress(offset / total)
        if total is None or offset != total:
            part.unlink(missing_ok=True)
            raise CloudError(f"{name} 只抓到一部分（{offset}/{total}），再試一次。")
        part.replace(dest)
        return offset

    async def delete(self, folder: str, name: str) -> bool:
        return bool((await self._call("POST", "/delete", payload={
            "folder": folder, "name": name})).get("deleted"))

    async def upload(self, path: Path, folder: str, name: str, on_progress=None,
                     area: str = "models") -> None:
        """Push a local file up in slices that each fit the proxy's time limit."""
        total = path.stat().st_size
        if total <= 0:
            raise CloudError(f"{path.name} 是空的，沒有東西可以上傳。")
        offset = 0
        with path.open("rb") as handle:
            while offset < total:
                handle.seek(offset)
                chunk = handle.read(UPLOAD_CHUNK)
                answer = await self._call(
                    "PUT", "/upload", data=chunk, timeout=95,
                    params={"folder": folder, "name": name, "area": area,
                            "offset": str(offset), "total": str(total)})
                received = int(answer.get("received") or 0)
                if answer.get("resync"):
                    # The machine has a different amount than we thought - a
                    # retried slice, usually. Carry on from where it really is.
                    offset = received
                    continue
                offset = received
                if on_progress:
                    on_progress(offset / total)
                if answer.get("complete"):
                    return
        raise CloudError(f"{name} 上傳到一半就停了。")


@dataclass
class State:
    """What this app remembers about the rental between restarts."""

    target: str = "local"            # "local" | "cloud": where new jobs run
    pod_id: str = ""
    agent_token: str = ""
    volume_id: str = ""
    volume_dc: str = ""
    volume_gb: int = 0
    gpu_id: str = ""
    gpu_name: str = ""
    gpu_vram: int = 0
    tier: str = "SECURE"
    cost_per_hr: float = 0.0
    idle_minutes: int = 15
    last_used: float = 0.0
    started: float = 0.0
    last_error: str = ""
    # Seconds of rented time this app has seen, and what that came to. An
    # estimate from the hourly price, labelled as one wherever it is shown -
    # the bill is Runpod's to state, not this file's.
    seconds_total: float = 0.0
    spent_total: float = 0.0
    history: list = field(default_factory=list)


class Store:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.state = State()

    def load(self) -> State:
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            raw = {}
        known = {f for f in State.__dataclass_fields__}
        self.state = State(**{k: v for k, v in (raw or {}).items() if k in known})
        if self.state.target not in ("local", "cloud"):
            self.state.target = "local"
        return self.state

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(asdict(self.state), ensure_ascii=False, indent=1),
                       encoding="utf-8")
        tmp.replace(self.path)


def best_data_center(gpu: dict) -> str:
    """Where to put the volume: wherever this card is easiest to get.

    A network volume pins every later machine to one data centre, so the
    choice is made once, from the card the user picked, by current stock.
    """
    rank = {"HIGH": 3, "MEDIUM": 2, "LOW": 1, "NONE": 0}
    centres = [c for c in (gpu.get("dataCenters") or []) if isinstance(c, dict)]
    centres.sort(key=lambda c: -rank.get(str(c.get("availability") or "NONE"), 0))
    for centre in centres:
        if rank.get(str(centre.get("availability") or "NONE"), 0) > 0:
            return str(centre.get("id") or "")
    return ""


def gpu_rows(gpus: list[dict], tier: str, data_center: str = "") -> list[dict]:
    """The catalogue as the page shows it: cheapest first, stock stated."""
    key = "secure" if tier == "SECURE" else "community"
    rows = []
    for gpu in gpus:
        if not gpu.get(key):
            continue
        price = float(((gpu.get("price") or {}).get(key)) or 0)
        centres = {str(c.get("id")): str(c.get("availability") or "NONE")
                   for c in (gpu.get("dataCenters") or []) if isinstance(c, dict)}
        stock = str(gpu.get("availability") or "NONE")
        # Once a volume exists only its data centre counts; a card that is in
        # stock everywhere else is still unavailable to this user.
        here = centres.get(data_center, "NONE") if data_center else stock
        rows.append({
            "id": gpu.get("id"), "name": gpu.get("name") or gpu.get("id"),
            "vram": int(gpu.get("memory") or 0), "price": price,
            "stock": here, "stock_anywhere": stock,
            "data_center": best_data_center(gpu),
        })
    rows.sort(key=lambda r: (r["price"] <= 0, r["price"], -r["vram"]))
    return rows


class Cloud:
    """Everything the server asks of the rental, in one place."""

    def __init__(self, store: Store) -> None:
        self.store = store
        self.api = Api()
        self.lock = asyncio.Lock()
        self._pod_cache: tuple[float, dict | None] = (0.0, None)

    @property
    def state(self) -> State:
        return self.store.state

    # -- addresses -----------------------------------------------------------

    @property
    def comfy_url(self) -> str:
        return proxy_url(self.state.pod_id, COMFY_PORT) if self.state.pod_id else ""

    def comfy(self):
        """A ComfyUI client for the machine, or None when there is none.

        One per machine rather than one per call: the client caches the
        machine's node list, and refetching that for every job would add a
        large request to each one.
        """
        if not self.state.pod_id or not self.state.agent_token:
            return None
        from comfy_client import ComfyClient   # here, so this module stays importable alone
        key = (self.comfy_url, self.state.agent_token)
        cached = getattr(self, "_comfy", None)
        if cached is None or cached[0] != key:
            self._comfy = (key, ComfyClient(self.comfy_url, self.state.agent_token))
        return self._comfy[1]

    @property
    def agent(self) -> Agent | None:
        if not self.state.pod_id or not self.state.agent_token:
            return None
        return Agent(proxy_url(self.state.pod_id, AGENT_PORT), self.state.agent_token)

    # -- lifecycle -----------------------------------------------------------

    async def pod(self, fresh: bool = False) -> dict | None:
        """The machine as Runpod sees it, cached for a few seconds."""
        if not self.state.pod_id:
            return None
        stamp, cached = self._pod_cache
        if not fresh and time.time() - stamp < 5:
            return cached
        pod = await self.api.pod(self.state.pod_id)
        if pod is None or str(pod.get("status")) == "TERMINATED":
            # Gone - deleted from the console, or Runpod reclaimed it. Forget
            # it, so the page offers to rent rather than waiting on a ghost.
            self._account(time.time())
            self.state.pod_id = ""
            self.state.agent_token = ""
            self.state.started = 0.0
            self.store.save()
            pod = None
        self._pod_cache = (time.time(), pod)
        return pod

    def _account(self, now: float) -> None:
        """Fold the run that just ended into the running total."""
        if self.state.started and self.state.cost_per_hr:
            seconds = max(0.0, now - self.state.started)
            cost = seconds / 3600.0 * self.state.cost_per_hr
            self.state.seconds_total += seconds
            self.state.spent_total += cost
            self.state.history = ([{
                "ended": now, "seconds": round(seconds), "cost": round(cost, 4),
                "gpu": self.state.gpu_name}] + list(self.state.history))[:30]

    async def rent(self, *, gpu_id: str, tier: str, volume_gb: int,
                   comfy_args: str = "") -> dict:
        """Rent a machine. Creates the volume first if there is none yet."""
        async with self.lock:
            if self.state.pod_id:
                pod = await self.pod(fresh=True)
                if pod and str(pod.get("status")) in ("EXITED", "ERROR"):
                    # Stopped (by its own dead-man switch, or out of credit) or
                    # broken. It is not running, but it is not gone either -
                    # and a stopped machine still bills for its disk. Give it
                    # back before renting the new one.
                    await self.api.terminate(self.state.pod_id)
                    self._account(time.time())
                    self.state.pod_id = ""
                    self.state.agent_token = ""
                    self.state.started = 0.0
                    self.store.save()
                elif pod:
                    raise CloudError("已經有一台雲端機了。先關掉它，再開新的。")
            tier = tier if tier in TIERS else "SECURE"
            gpus = await self.api.gpus(tier)
            chosen = next((g for g in gpus if g.get("id") == gpu_id), None)
            if chosen is None:
                raise CloudError(f"Runpod 現在的清單裡沒有這張卡：{gpu_id}")

            if not self.state.volume_id:
                centre = best_data_center(chosen)
                if not centre:
                    raise CloudError(
                        f"{chosen.get('name') or gpu_id} 現在所有資料中心都沒有庫存。"
                        "換一張卡，或晚一點再試。")
                size = max(50, min(int(volume_gb or 0), 2000))
                volume = await self.api.create_volume(centre, size)
                self.state.volume_id = str(volume.get("id") or "")
                self.state.volume_dc = str(volume.get("dataCenter") or centre)
                self.state.volume_gb = int(volume.get("size") or size)
                self.store.save()
                if not self.state.volume_id:
                    raise CloudError("Runpod 建了硬碟但沒有回傳它的編號。到 Runpod 主控台確認。")

            token = secrets.token_urlsafe(32)
            body = pod_body(
                gpu_id=gpu_id, tier=tier, volume_id=self.state.volume_id,
                data_center=self.state.volume_dc, token=token,
                deadman_minutes=max(30, self.state.idle_minutes * 2),
                comfy_args=comfy_args)
            pod = await self.api.create_pod(body)
            pod_id = str(pod.get("id") or "")
            if not pod_id:
                raise CloudError("Runpod 沒有回傳機器的編號，不確定有沒有開成功。"
                                 "到 Runpod 主控台確認，避免有一台在空轉。")
            now = time.time()
            self.state.pod_id = pod_id
            self.state.agent_token = token
            self.state.gpu_id = gpu_id
            self.state.gpu_name = str(chosen.get("name") or gpu_id)
            self.state.gpu_vram = int(chosen.get("memory") or 0)
            self.state.tier = tier
            self.state.cost_per_hr = float(pod.get("cost") or
                                           ((chosen.get("price") or {}).get(
                                               "secure" if tier == "SECURE" else "community")) or 0)
            self.state.started = now
            self.state.last_used = now
            self.state.last_error = ""
            self.store.save()
            self._pod_cache = (0.0, None)
            return pod

    async def release(self) -> None:
        """Give the machine back. The volume, and the models on it, stay."""
        async with self.lock:
            if not self.state.pod_id:
                return
            await self.api.terminate(self.state.pod_id)
            self._account(time.time())
            self.state.pod_id = ""
            self.state.agent_token = ""
            self.state.started = 0.0
            self.store.save()
            self._pod_cache = (0.0, None)

    async def drop_volume(self) -> None:
        """Delete the disk. Every model on it has to be downloaded again."""
        async with self.lock:
            if self.state.pod_id:
                raise CloudError("先把雲端機關掉，才能刪硬碟。")
            if self.state.volume_id:
                await self.api.delete_volume(self.state.volume_id)
            self.state.volume_id = ""
            self.state.volume_dc = ""
            self.state.volume_gb = 0
            self.store.save()

    def touch(self) -> None:
        self.state.last_used = time.time()

    async def idle_tick(self, busy: bool) -> bool:
        """Terminate a machine nobody has used for a while. True if it did."""
        if not self.state.pod_id or self.state.idle_minutes <= 0:
            return False
        if busy:
            self.touch()
            return False
        if time.time() - (self.state.last_used or self.state.started) < self.state.idle_minutes * 60:
            return False
        agent = self.agent
        if agent is not None:
            try:
                status = await agent.status()
                if int(status.get("downloading") or 0) > 0 or status.get("training"):
                    self.touch()          # fetching a model or training: that is work
                    return False
            except Exception:  # noqa: BLE001 - unreachable agent is not "busy"
                pass
        await self.release()
        self.state.last_error = (
            f"雲端機閒置超過 {self.state.idle_minutes} 分鐘，已經自動關掉了。"
            "模型還在硬碟上，下次開機不用重新下載。")
        self.store.save()
        return True

    # -- readiness -----------------------------------------------------------

    async def boot_log(self) -> list[str]:
        """The boot log, by whichever route still works."""
        agent = self.agent
        if agent is not None:
            try:
                return list((await agent.status()).get("log") or [])
            except Exception:  # noqa: BLE001
                pass
        if self.state.pod_id:
            answer = await self.api.run(self.state.pod_id, [
                "sh", "-c", f"tail -n 40 {ROOT}/boot.log 2>/dev/null || echo '（還沒有開機紀錄）'"])
            return [line for line in str(answer.get("stdout") or "").splitlines() if line.strip()]
        return []

    async def wait_ready(self, say=None) -> None:
        """Block until the machine can take a job, narrating the wait."""
        say = say or (lambda _text: None)
        if not self.state.pod_id:
            raise CloudError("雲端機沒有開。到「設定」分頁的「雲端 GPU」開機。")

        deadline = time.time() + PROVISION_TIMEOUT
        while True:
            pod = await self.pod(fresh=True)
            if pod is None:
                raise CloudError("雲端機不見了（可能在 Runpod 主控台被刪掉，或餘額用完）。")
            status = str(pod.get("status") or "")
            if status == "RUNNING":
                break
            if status in ("ERROR", "EXITED"):
                raise CloudError(
                    f"雲端機的狀態是 {status}，沒有在跑。到「設定」分頁把它關掉再重新開。")
            if time.time() > deadline:
                raise CloudError("等 Runpod 分配機器等太久了（超過 20 分鐘）。"
                                 "這張卡可能沒有庫存 —— 關掉它換一張。")
            say("Runpod 正在準備機器…（第一次要下載映像檔，幾分鐘）")
            await asyncio.sleep(6)

        agent = self.agent
        deadline = time.time() + BOOT_TIMEOUT
        while True:
            phase = ""
            try:
                phase = str((await agent.status()).get("phase") or "")
            except CloudError:
                raise
            except Exception:  # noqa: BLE001 - not listening yet
                phase = ""
            if phase == "ready":
                break
            if phase.startswith("failed"):
                tail = "\n".join((await self.boot_log())[-12:])
                raise CloudError(f"雲端機開機失敗：{phase[7:].strip()}\n{tail}")
            if time.time() > deadline:
                tail = "\n".join((await self.boot_log())[-12:])
                raise CloudError("雲端機開機超過 25 分鐘還沒好。最後的紀錄：\n" + tail)
            say({"": "雲端機開機中…",
                 "booting": "雲端機開機中…"}.get(phase, f"雲端機：{phase}"))
            await asyncio.sleep(5)
        self.touch()

    # -- model files ---------------------------------------------------------

    async def fetch(self, plans, say=None) -> None:
        """Put these files on the machine: downloads first, then uploads.

        ``plans`` are ``sources.Source`` objects. A download is the machine
        fetching from Hugging Face or CivitAI itself, at data-centre speed;
        all of them are started at once and the agent runs a few in parallel.
        An upload is a file only this computer has, pushed up a slice at a
        time. Raises CloudError naming the file if any of them fails.
        """
        say = say or (lambda _text: None)
        agent = self.agent
        if agent is None:
            raise CloudError("雲端機沒有開，沒辦法放模型上去。")
        downloads = [p for p in plans if not p.is_upload]
        uploads = [p for p in plans if p.is_upload]

        keys = {}
        for plan in downloads:
            answer = await agent.download(url=plan.url, folder=plan.folder, name=plan.name,
                                          size=plan.size, headers=dict(plan.headers))
            keys[str(answer.get("id") or f"{plan.folder}/{plan.name}")] = plan
        while keys:
            items = await agent.downloads()
            done_bytes = total_bytes = 0
            for key, plan in list(keys.items()):
                item = items.get(key) or {}
                status = str(item.get("status") or "")
                if status == "done":
                    keys.pop(key)
                    continue
                if status in ("error", "cancelled"):
                    raise CloudError(f"雲端機下載 {plan.name} 失敗：{item.get('error') or status}")
                done_bytes += int(item.get("done") or 0)
                total_bytes += int(item.get("total") or plan.size or 0)
            if not keys:
                break
            self.touch()               # downloading is using the machine
            share = f"{done_bytes / total_bytes * 100:.0f}%" if total_bytes else ""
            gb = f"{done_bytes / 1e9:.1f}/{total_bytes / 1e9:.1f} GB" if total_bytes else ""
            say(f"雲端機下載模型中（還有 {len(keys)} 個檔）{share} {gb}".strip())
            await asyncio.sleep(3)

        for index, plan in enumerate(uploads, 1):
            def progress(share, name=plan.name, index=index):
                self.touch()
                say(f"把你電腦上的 {name} 傳上雲端機（{index}/{len(uploads)}）{share * 100:.0f}%")
            await agent.upload(plan.local, plan.folder, plan.name, on_progress=progress)

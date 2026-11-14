"""RunPod: network volume storage over the S3-compatible API, and GPU pods over the REST API.

Flow for one training run (all from the user's own RunPod account):
1. upload the dataset, the engine's setup and training scripts, and a config to the network volume
   (s3://<volume id>/vs/jobs/<training id>/);
2. create a pod on that volume's datacenter; its start command runs bootstrap.sh, which installs the engine once
   (cached on the volume), trains, writes progress.json while it works and model.tar at the end, then removes itself;
3. the studio polls the pod and progress.json, downloads model.tar when done.json appears, and removes the pod itself
   too if the pod is still there (belt and braces: a forgotten GPU is the main way to lose money).
Keys are read from the OS credential store; they are never written to disk or logs by the studio.
"""
from __future__ import annotations

import json
import os
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx

from .. import config

REST = "https://rest.runpod.io/v1"
# S3 endpoints are per datacenter: https://s3api-<dc>.runpod.io (lower-case id; the region is the upper-case id).
# Not every datacenter offers the S3 API; the settings page lists the ones that do.
S3_FMT = "https://s3api-{dc}.runpod.io"

S3_DATACENTERS = ["EU-CZ-1", "EU-RO-1", "EUR-IS-1", "EUR-NO-1", "US-CA-2", "US-GA-2", "US-IL-1", "US-KS-2",
                  "US-MD-1", "US-MO-1", "US-MO-2", "US-NC-1", "US-NC-2", "US-NE-1", "US-WA-1"]

GPUS = {  # Secure Cloud on-demand prices from runpod.io/pricing (updated 2026-09-27); network volumes need Secure Cloud
    "NVIDIA H100 80GB HBM3": {"label": "H100 SXM 80GB", "vram": 80, "usd_h": 3.49},
    "NVIDIA H100 PCIe": {"label": "H100 PCIe 80GB", "vram": 80, "usd_h": 2.89},
    "NVIDIA A100-SXM4-80GB": {"label": "A100 SXM 80GB", "vram": 80, "usd_h": 1.59},
    "NVIDIA A100 80GB PCIe": {"label": "A100 PCIe 80GB", "vram": 80, "usd_h": 1.59},
    "NVIDIA L40S": {"label": "L40S 48GB", "vram": 48, "usd_h": 1.09},
    "NVIDIA RTX 6000 Ada Generation": {"label": "RTX 6000 Ada 48GB", "vram": 48, "usd_h": 0.84},
    "NVIDIA GeForce RTX 5090": {"label": "RTX 5090 32GB", "vram": 32, "usd_h": 0.99},
    "NVIDIA GeForce RTX 4090": {"label": "RTX 4090 24GB", "vram": 24, "usd_h": 0.74},
}

# Rough training speed relative to an A100 SXM 80GB (bf16 mixed precision; from public specs and common training
# benchmarks, not measured with these engines). Only used to carry a speed measured on one card over to a card that
# has not been measured yet; a card's own measured speed always wins.
GPU_SPEED = {
    "NVIDIA H200": 2.2,
    "NVIDIA H100 80GB HBM3": 2.0,
    "NVIDIA H100 PCIe": 1.5,
    "NVIDIA A100-SXM4-80GB": 1.0,
    "NVIDIA A100 80GB PCIe": 0.9,
    "NVIDIA GeForce RTX 5090": 0.85,
    "NVIDIA L40S": 0.8,
    "NVIDIA RTX 6000 Ada Generation": 0.8,
    "NVIDIA GeForce RTX 4090": 0.65,
}


class RunPodError(Exception):
    pass


class MissingFile(RunPodError):
    """The file is not on the volume (as opposed to: the volume could not be reached)."""


def _key() -> str:
    k = config.get_secret("runpod_api_key")
    if not k:
        raise RunPodError("尚未設定 RunPod API 金鑰（設定 → 雲端）。")
    return k


def _h() -> dict:
    return {"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"}


def _req(method: str, path: str, **kw):
    with httpx.Client(timeout=60) as c:
        r = c.request(method, REST + path, headers=_h(), **kw)
    if r.status_code >= 400:
        raise RunPodError(f"RunPod {method} {path}: {r.status_code} {r.text[:300]}")
    return r.json() if r.content else {}


def volumes() -> list[dict]:
    """The account's network volumes as RunPod lists them (id, name, dataCenterId, size)."""
    vols = _req("GET", "/networkvolumes")
    return vols if isinstance(vols, list) else vols.get("data", vols)


def check() -> dict:
    """Verify the API key and the volume; returns the account's volumes (s3: whether the studio can use one) and,
    in problem, why the volume in settings cannot be used for training ("" when it can)."""
    st = config.load_settings()
    vols = volumes()
    out = {"ok": True, "volumes": [{"id": v.get("id"), "name": v.get("name"), "dataCenterId": v.get("dataCenterId"),
                                    "size": v.get("size"), "s3": v.get("dataCenterId") in S3_DATACENTERS}
                                   for v in vols]}
    vid = st.get("runpod_volume_id")
    if vid:
        match = [v for v in out["volumes"] if v["id"] == vid]
        out["volume"] = match[0] if match else None
    out["problem"] = volume_problem(out["volumes"], vid, st.get("runpod_datacenter"))
    return out


def volume_problem(volumes: list[dict], volume_id: str | None, datacenter: str | None) -> str:
    """Why the volume in settings cannot be used for training: gone, in a datacenter without the S3 API, or set
    with another datacenter than the one it is in. "" when it can be used (or none is set yet)."""
    if not volume_id:
        return ""
    v = next((x for x in volumes if x["id"] == volume_id), None)
    if v is None:
        return (f"設定裡的網路磁碟 {volume_id} 不在你的 RunPod 帳號裡（可能已經刪除），訓練會失敗。"
                "到「設定 → 雲端 GPU」按「測試連線」，點一個可以用的磁碟。")
    dc = v.get("dataCenterId") or ""
    if dc not in S3_DATACENTERS:
        return (f"網路磁碟 {v.get('name') or volume_id} 在 {dc}，那裡沒有 S3 API，Voice Studio 沒辦法把資料傳過去。"
                "請在設定下拉選單裡的資料中心建立網路磁碟，再到設定改用它。")
    if datacenter and datacenter != dc:
        return (f"設定的資料中心 {datacenter} 和網路磁碟實際所在的 {dc} 不一樣。"
                "到「設定 → 雲端 GPU」按「測試連線」，再點一次這個磁碟。")
    return ""


def location() -> dict:
    """The volume and datacenter from settings, frozen into each training run when it starts."""
    st = config.load_settings()
    vol, dc = st.get("runpod_volume_id"), st.get("runpod_datacenter")
    if not vol or not dc:
        raise RunPodError("請先在設定裡填網路磁碟（Network Volume）ID 和它的資料中心。")
    return {"volume": vol, "datacenter": dc, "cloud": st.get("runpod_cloud_type") or "SECURE"}


def create_pod(name: str, image: str, gpu_type: str | list[str], env: dict, start_cmd: list[str], loc: dict,
               container_disk_gb: int = 80, min_ram_gb: int = 32, min_vcpu: int = 8) -> dict:
    """Rent exactly the GPU that was quoted (no silent fallback to a pricier card), or, for auto-grab, the first card
    of the person's own list that RunPod can give (gpuTypePriority "custom" keeps their order)."""
    gpus = [gpu_type] if isinstance(gpu_type, str) else list(gpu_type)
    body = {"name": name[:180], "imageName": image, "gpuTypeIds": gpus, "gpuTypePriority": "custom",
            "gpuCount": 1, "cloudType": loc.get("cloud") or "SECURE", "networkVolumeId": loc["volume"],
            "dataCenterIds": [loc["datacenter"]], "volumeMountPath": "/workspace",
            "containerDiskInGb": container_disk_gb, "minRAMPerGPU": min_ram_gb, "minVCPUPerGPU": min_vcpu,
            "env": env, "dockerStartCmd": start_cmd, "ports": ["22/tcp"]}
    return _req("POST", "/pods", json=body)


def list_pods(name: str | None = None, volume: str | None = None) -> list[dict]:
    params = {k: v for k, v in (("name", name), ("networkVolumeId", volume)) if v}
    out = _req("GET", "/pods", params=params)
    return out if isinstance(out, list) else out.get("data", [])


def studio_pods() -> list[dict]:
    """Every pod this studio started (named voice-studio-<training id>), for the orphan check."""
    return [p for p in list_pods() if str(p.get("name", "")).startswith("voice-studio-")]


def get_pod(pod_id: str) -> dict | None:
    try:
        return _req("GET", f"/pods/{pod_id}")
    except RunPodError as e:
        if " 404 " in str(e):
            return None
        raise


def remove_pod(pod_id: str) -> None:
    """Delete a pod; a pod that is already gone counts as removed. Other errors propagate."""
    try:
        _req("DELETE", f"/pods/{pod_id}")
    except RunPodError as e:
        if " 404 " not in str(e):
            raise


IN_STOCK = ("HIGH", "MEDIUM", "LOW")  # the catalog's availability levels that can be rented; "NONE" cannot


def gpu_catalog(datacenter: str | None = None) -> dict:
    """Live GPU prices and stock for pods (api.runpod.io/v2/catalog/gpus), for one datacenter when given.

    A GPU the catalog does not list for that datacenter is out of stock there ("NONE"). Only NVIDIA cards are listed
    (the engine images are CUDA). When the catalog cannot be read, the static table comes back with live=False and
    the reason, so the page can say so instead of presenting the static list as if it were the current stock."""
    st = config.load_settings()
    cloud = st.get("runpod_cloud_type") or "SECURE"
    try:
        with httpx.Client(timeout=30) as c:
            r = c.get("https://api.runpod.io/v2/catalog/gpus", headers=_h(),
                      params={"include": "AVAILABILITY", "product": "POD", "cloud": cloud})
        if r.status_code >= 400:
            raise RunPodError(f"RunPod GPU catalog: {r.status_code} {r.text[:200]}")
        out = []
        for g in r.json().get("gpus", []):
            if not str(g.get("id", "")).startswith("NVIDIA"):
                continue
            if datacenter:
                dcs = {d.get("id"): d.get("availability") for d in g.get("dataCenters") or []}
                avail = dcs[datacenter] if datacenter in dcs else "NONE"
            else:
                avail = g.get("availability")
            price = (g.get("price") or {}).get("secure" if cloud == "SECURE" else "community")
            out.append({"id": g["id"], "label": g.get("name") or g["id"], "vram": g.get("memory"),
                        "usd_h": price or None, "availability": str(avail or "NONE").upper()})
        gpus = sorted(out, key=lambda x: (x["usd_h"] is None, x["usd_h"] or 0))
        return {"live": True, "datacenter": datacenter, "error": "", "gpus": gpus}
    except Exception as e:
        reason = str(e) if isinstance(e, RunPodError) else f"{type(e).__name__}: {e}"
        return {"live": False, "datacenter": datacenter, "error": reason[:300],
                "gpus": [{"id": k, **v, "availability": None} for k, v in GPUS.items()]}


# --- S3 (network volume) ----------------------------------------------------------------------------------------

def s3(loc: dict | None = None, fast: bool = False, attempts: int | None = None, read_timeout: int | None = None):
    """fast=True (status polling) gives up quickly, so the caller's own retry and deadline logic stays in charge;
    attempts overrides how often one request is tried (a caller that retries by itself keeps it low), read_timeout
    how long a reply may take (see prepare())."""
    import boto3
    from botocore.config import Config
    ak, sk = config.get_secret("runpod_s3_access_key"), config.get_secret("runpod_s3_secret_key")
    if not ak or not sk:
        raise RunPodError("尚未設定 RunPod S3 金鑰（設定 → 雲端）。")
    dc = ((loc or {}).get("datacenter") or config.load_settings().get("runpod_datacenter") or "").strip()
    return boto3.client("s3", aws_access_key_id=ak, aws_secret_access_key=sk, region_name=dc.upper(),
                        endpoint_url=S3_FMT.format(dc=dc.lower()),
                        config=Config(signature_version="s3v4",
                                      retries={"max_attempts": attempts or (2 if fast else 8), "mode": "adaptive"},
                                      s3={"addressing_style": "path"}, connect_timeout=10 if fast else 20,
                                      read_timeout=read_timeout or (20 if fast else 120)))


def bucket(loc: dict | None = None) -> str:
    return (loc or {}).get("volume") or config.load_settings()["runpod_volume_id"]


def _missing(e: Exception) -> bool:
    from botocore.exceptions import ClientError
    return isinstance(e, ClientError) and e.response.get("Error", {}).get("Code") in ("NoSuchKey", "404", "NotFound")


def upload(local: Path, key: str, progress=None, loc: dict | None = None) -> None:
    from boto3.s3.transfer import TransferConfig
    size = local.stat().st_size
    done = [0]

    def cb(n):
        done[0] += n
        if progress:
            progress(done[0] / max(1, size))
    # parts stay far below the S3 API's 500 MB part limit
    s3(loc).upload_file(str(local), bucket(loc), key, Callback=cb,
                        Config=TransferConfig(multipart_chunksize=64 << 20, max_concurrency=4))


def put_text(key: str, text: str, loc: dict | None = None) -> None:
    s3(loc).put_object(Bucket=bucket(loc), Key=key, Body=text.encode("utf-8"))


def get_json(key: str, loc: dict | None = None, fast: bool = False) -> dict | None:
    """None only when the object does not exist; network, permission and parse errors propagate to the caller's
    retry (a file caught mid-write reads as an error, and the next poll sees it whole)."""
    try:
        obj = s3(loc, fast).get_object(Bucket=bucket(loc), Key=key)
    except Exception as e:
        if _missing(e):
            return None
        raise
    with obj["Body"] as body:
        return json.loads(body.read().decode("utf-8"))


def exists(key: str, loc: dict | None = None, fast: bool = False) -> bool:
    try:
        s3(loc, fast).head_object(Bucket=bucket(loc), Key=key)
        return True
    except Exception as e:
        if _missing(e):
            return False
        raise


def size(key: str, loc: dict | None = None) -> int:
    return int(s3(loc).head_object(Bucket=bucket(loc), Key=key)["ContentLength"])


def get_text(key: str, tail: int = 20000, loc: dict | None = None) -> str:
    try:
        obj = s3(loc).get_object(Bucket=bucket(loc), Key=key)
        return obj["Body"].read().decode("utf-8", "replace")[-tail:]
    except Exception:
        return ""


# Downloads follow RunPod's own runpodctl (network-volume download, Nov 2026): 64 MB ranges, 4 at a time, up to
# 5 minutes for RunPod to start answering a range, and a 524 from its proxy ("slow operation") is retried.
DL_PART = 64 << 20      # bytes per ranged GET
DL_WORKERS = 4          # ranges in flight at once
DL_READ_S = 300         # how long one range may wait for RunPod to start answering, or for its next bytes
DL_STALL_S = 3600       # give up only after this long without a single byte arriving (any range)
DL_BACKOFF_S = 5.0      # first pause after a failed range; doubles up to DL_BACKOFF_MAX_S
DL_BACKOFF_MAX_S = 60.0
DL_CHUNK = 1 << 20      # bytes read at a time, so progress moves while a range comes in
DL_REPORT_S = 1.0       # progress is reported at most this often
ARCHIVE_PART_MB = 512   # the pod writes model.tar / samples.tar in parts this big (bootstrap.sh: VS_PART_MB)
PREPARE_WAIT_S = 5400   # how long to wait for RunPod to get a big file ready (see prepare)
PREPARE_READ_S = 1800   # one request's patience while it does (a request that gives up may make RunPod start over)
PREPARE_TICK_S = 5.0    # how often the wait is reported and a stop request looked for
PREPARE_PAUSE_S = 10.0  # between two waiting requests


def _retryable(e: Exception) -> bool:
    """A reply that may come right if asked again (a timeout, a dropped connection, a server busy); not a refusal."""
    from botocore.exceptions import ClientError
    if isinstance(e, ClientError):
        code = str(e.response.get("Error", {}).get("Code", ""))
        status = int(e.response.get("ResponseMetadata", {}).get("HTTPStatusCode") or 0)
        return status >= 500 or code in ("SlowDown", "InternalError", "RequestTimeout", "ServiceUnavailable")
    return True


def prepare(key: str, loc: dict | None = None, check=None, note=None, wait_s: float | None = None) -> dict:
    """HEAD a file, giving RunPod the time it needs. RunPod computes and caches an MD5 checksum (the ETag) the first
    time a file that was not uploaded through its S3 API is read over S3; a model.tar of tens of GB written on the
    pod takes minutes, and a request that gives up before that never gets the answer (the next one starts over). So
    one request at a time, each allowed PREPARE_READ_S, for up to wait_s in all; note(seconds waited) reports the
    wait, check() can stop it. Raises RunPodError when the file is not there or RunPod refuses."""
    wait_s = PREPARE_WAIT_S if wait_s is None else wait_s
    c, b = s3(loc, attempts=1, read_timeout=PREPARE_READ_S), bucket(loc)
    name = key.rsplit("/", 1)[-1]
    t0 = time.time()
    while True:
        box: dict = {}

        def head(box: dict = box) -> None:
            try:
                box["head"] = c.head_object(Bucket=b, Key=key)
            except Exception as x:  # reported below
                box["error"] = x
        th = threading.Thread(target=head, daemon=True, name=f"prepare {name}")
        th.start()
        while th.is_alive():
            th.join(PREPARE_TICK_S)
            if check:
                check()  # a stop request: the waiting request is left to time out by itself
            if note and th.is_alive():
                note(int(time.time() - t0))
        if "head" in box:
            return box["head"]
        e = box["error"]
        if _missing(e):
            raise MissingFile(f"雲端沒有 {name}") from e
        if not _retryable(e):
            raise RunPodError(f"RunPod 拒絕讀取 {name}：{str(e)[:200]}") from e
        if time.time() - t0 + PREPARE_PAUSE_S >= wait_s:
            raise RunPodError(f"等了 {int(time.time() - t0) // 60} 分鐘，RunPod 還沒把 {name} 準備好：{str(e)[:160]}") from e
        if note:
            note(int(time.time() - t0))
        end = time.time() + PREPARE_PAUSE_S
        while time.time() < end:
            if check:
                check()
            time.sleep(min(1.0, PREPARE_PAUSE_S))


def archive_info(prefix: str, name: str, loc: dict | None = None, fast: bool = False) -> dict | None:
    """The manifest of an archive the pod wrote in parts (<name>.json: size and parts), or None. A run from before
    parts wrote one file, <name> itself, which only prepare() can look at without timing out."""
    return get_json(f"{prefix}/{name}.json", loc, fast)


def has_archive(prefix: str, name: str, loc: dict | None = None, fast: bool = False) -> bool:
    """Whether the pod published model.tar / samples.tar (in parts, or as one file)."""
    return archive_info(prefix, name, loc, fast) is not None or exists(f"{prefix}/{name}", loc, fast)


def locate_archive(prefix: str, name: str, loc: dict | None = None, check=None, note=None) -> tuple[list[dict], str]:
    """What to download for an archive: ([{key, size}], an identity that changes when the file does). Parts are
    small enough for RunPod to checksum on the fly; one big file of an older run first waits in prepare()."""
    info = archive_info(prefix, name, loc)
    if info is not None:
        objs = [{"key": f"{prefix}/{p['key']}", "size": int(p["size"])} for p in info["parts"]]
        return objs, "parts:" + json.dumps(info["parts"], sort_keys=True)
    head = prepare(f"{prefix}/{name}", loc, check=check, note=note)
    return [{"key": f"{prefix}/{name}", "size": int(head["ContentLength"])}], "etag:" + str(head.get("ETag") or "")


def fetch(objs: list[dict], ident: str, local: Path, progress=None, loc: dict | None = None, check=None,
          note=None, log=None) -> Path:
    """Download objects, one after the other, into one local file, in ranged pieces written into <local>.part and
    recorded in <local>.part.json as they land, so a stalled connection, a failed run or a later "recover model"
    continues where it stopped instead of fetching everything again.

    progress(fraction) follows the bytes as they arrive (at most every DL_REPORT_S). A piece that fails (a timeout,
    a 524 from RunPod's proxy, a dropped connection) is asked for again after a pause, with note(text) saying why,
    and log(text) recording it; the download gives up only when no byte at all has arrived for DL_STALL_S. check() is
    looked at before and between tries; whatever it raises (a stop request) ends the download at once, keeping the
    pieces already down. The file is moved into place only when every piece is there."""
    c, b = s3(loc, attempts=1, read_timeout=DL_READ_S), bucket(loc)  # every try is seen (and reported) here
    size = sum(o["size"] for o in objs)
    local.parent.mkdir(parents=True, exist_ok=True)
    if size == 0:
        local.write_bytes(b"")
        return local
    pieces, off = [], 0  # (key, first byte, last byte, where it goes in the local file)
    for o in objs:
        pieces += [(o["key"], a, min(o["size"], a + DL_PART) - 1, off + a) for a in range(0, o["size"], DL_PART)]
        off += o["size"]
    part, state_f = local.with_name(local.name + ".part"), local.with_name(local.name + ".part.json")
    try:
        state = json.loads(state_f.read_text(encoding="utf-8"))
    except Exception:
        state = {}
    if (state.get("size"), state.get("ident"), state.get("part")) != (size, ident, DL_PART) or not part.exists() \
            or part.stat().st_size != size:  # another file, or nothing usable yet: start over
        with open(part, "wb") as f:
            f.truncate(size)
        state = {"size": size, "ident": ident, "part": DL_PART, "done": []}
    n = len(pieces)
    done, lock, stopped = set(state["done"]), threading.Lock(), []
    got = {"bytes": sum(pieces[i][2] - pieces[i][1] + 1 for i in done if i < n), "last": time.time(), "shown": 0.0,
           "fails": 0, "t0": time.time()}

    def call(fn, *args) -> None:
        try:
            fn(*args)
        except BaseException as x:  # a callback that raises (the job's stop request): the whole download ends
            if not stopped:
                stopped.append(x)
            raise

    def report(force: bool = False) -> None:  # under lock
        if progress and (force or time.time() - got["shown"] >= DL_REPORT_S):
            got["shown"] = time.time()
            call(progress, min(1.0, got["bytes"] / size))

    def stop_check() -> None:
        if stopped:
            raise stopped[0]
        if check:
            try:
                check()
            except BaseException as x:  # not a network error: no retry, no further pieces
                stopped.append(x)
                raise

    def get(f, i: int) -> None:
        key, a, e, at = pieces[i]
        t = 0
        while True:
            stop_check()
            buf = bytearray()
            try:
                body = c.get_object(Bucket=b, Key=key, Range=f"bytes={a}-{e}")["Body"]
                while True:
                    chunk = body.read(DL_CHUNK)
                    if not chunk:
                        break
                    buf += chunk
                    with lock:
                        got["bytes"] += len(chunk)
                        got["last"] = time.time()
                        report()
                if len(buf) != e - a + 1:
                    raise OSError(f"short read: {len(buf)} of {e - a + 1} bytes")
                with lock:
                    f.seek(at)
                    f.write(buf)
                    f.flush()
                    done.add(i)
                    state_f.write_text(json.dumps({**state, "done": sorted(done)}), encoding="utf-8")
                    report(force=len(done) == n)
                return
            except Exception as x:
                if stopped:  # stopped from a callback while this piece was coming in
                    raise stopped[0] from None
                with lock:  # what came of this piece is fetched again
                    got["bytes"] -= len(buf)
                    got["fails"] += 1
                    quiet = time.time() - got["last"]
                    why = f"{type(x).__name__}: {str(x)[:160]}"
                    if log:
                        log(f"piece {i + 1}/{n} try {t + 1} failed after {len(buf)} bytes: {why}")
                    if note:
                        call(note, f"雲端這段還沒傳過來，重試中（已經 {int(quiet) // 60} 分 {int(quiet) % 60:02d} 秒沒收到資料，"
                             f"第 {got['fails']} 次重試：{why[:80]}）。RunPod 第一次讀大檔案時可能要等幾分鐘。")
                if quiet >= DL_STALL_S:
                    raise
            pause = min(DL_BACKOFF_MAX_S, DL_BACKOFF_S * 2 ** t)
            t += 1
            end = time.time() + pause
            while time.time() < end:
                stop_check()
                time.sleep(min(1.0, pause))

    todo = [i for i in range(n) if i not in done]
    with open(part, "r+b") as f, ThreadPoolExecutor(DL_WORKERS) as ex:
        errors = [x for x in (fu.exception() for fu in [ex.submit(get, f, i) for i in todo]) if x]
    if stopped:
        raise stopped[0]
    if len(done) < n:
        err = errors[0] if errors else None
        raise RunPodError(f"下載中斷（已完成 {len(done) * 100 // n}%，{DL_STALL_S // 60} 分鐘沒收到任何資料）："
                          f"{str(err)[:200]}") from err
    os.replace(part, local)
    state_f.unlink(missing_ok=True)
    return local


def download(key: str, local: Path, progress=None, loc: dict | None = None, check=None, note=None,
             log=None) -> Path:
    """One file: prepare() it (RunPod may need minutes for a big one), then fetch() it. note(seconds) reports the
    wait in prepare()."""
    head = prepare(key, loc, check=check, note=note)
    return fetch([{"key": key, "size": int(head["ContentLength"])}], "etag:" + str(head.get("ETag") or ""), local,
                 progress, loc, check, log=log)


def download_archive(prefix: str, name: str, local: Path, progress=None, loc: dict | None = None, check=None,
                     note=None, log=None) -> Path:
    objs, ident = locate_archive(prefix, name, loc, check=check, note=note)
    return fetch(objs, ident, local, progress, loc, check, log=log)


def delete_archive(prefix: str, name: str, loc: dict | None = None) -> None:
    """An archive's parts and manifest, or its one file."""
    info = archive_info(prefix, name, loc)
    for p in (info or {}).get("parts", []):
        delete(f"{prefix}/{p['key']}", loc)
    delete(f"{prefix}/{name}.json", loc)
    delete(f"{prefix}/{name}", loc)


RUN_FOLDER = re.compile(r"vs/jobs/tr_[0-9a-f]+")  # one training run's folder on the volume, nothing wider


def delete_run_folder(prefix: str, loc: dict | None = None) -> int:
    """Delete everything a training run left on the network volume (its dataset.tar, model.tar, samples, logs).
    Only a run folder: the engine environments and model cache next to it are shared by every run. Returns how
    many files were deleted."""
    prefix = prefix.strip("/")
    if not RUN_FOLDER.fullmatch(prefix):
        raise RunPodError(f"不是一次訓練的資料夾：{prefix}")
    c, b, n = s3(loc), bucket(loc), 0
    for page in c.get_paginator("list_objects_v2").paginate(Bucket=b, Prefix=prefix + "/"):
        for o in page.get("Contents") or []:
            c.delete_object(Bucket=b, Key=o["Key"])  # one by one: the volume's S3 API may not offer batch delete
            n += 1
    return n


def delete(key: str, loc: dict | None = None) -> None:
    try:
        s3(loc).delete_object(Bucket=bucket(loc), Key=key)
    except Exception as e:
        if not _missing(e):
            raise

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


class RunPodError(Exception):
    pass


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


def check() -> dict:
    """Verify the API key and the volume; returns the volume's datacenter and size."""
    st = config.load_settings()
    vols = _req("GET", "/networkvolumes")
    vols = vols if isinstance(vols, list) else vols.get("data", vols)
    out = {"ok": True, "volumes": [{"id": v.get("id"), "name": v.get("name"), "dataCenterId": v.get("dataCenterId"),
                                    "size": v.get("size")} for v in vols]}
    vid = st.get("runpod_volume_id")
    if vid:
        match = [v for v in out["volumes"] if v["id"] == vid]
        out["volume"] = match[0] if match else None
    return out


def location() -> dict:
    """The volume and datacenter from settings, frozen into each training run when it starts."""
    st = config.load_settings()
    vol, dc = st.get("runpod_volume_id"), st.get("runpod_datacenter")
    if not vol or not dc:
        raise RunPodError("請先在設定裡填網路磁碟（Network Volume）ID 和它的資料中心。")
    return {"volume": vol, "datacenter": dc, "cloud": st.get("runpod_cloud_type") or "SECURE"}


def create_pod(name: str, image: str, gpu_type: str, env: dict, start_cmd: list[str], loc: dict,
               container_disk_gb: int = 80, min_ram_gb: int = 32, min_vcpu: int = 8) -> dict:
    """Rent exactly the GPU that was quoted (no silent fallback to a pricier card)."""
    body = {"name": name[:180], "imageName": image, "gpuTypeIds": [gpu_type], "gpuTypePriority": "custom",
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


def gpu_catalog(datacenter: str | None = None) -> list[dict]:
    """Live GPU prices and stock for pods (api.runpod.io/v2/catalog/gpus); falls back to the static table."""
    st = config.load_settings()
    cloud = st.get("runpod_cloud_type") or "SECURE"
    try:
        with httpx.Client(timeout=30) as c:
            r = c.get("https://api.runpod.io/v2/catalog/gpus", headers=_h(),
                      params={"include": "AVAILABILITY", "product": "POD", "cloud": cloud})
        r.raise_for_status()
        out = []
        for g in r.json().get("gpus", []):
            dcs = {d["id"]: d.get("availability") for d in g.get("dataCenters", [])}
            if datacenter and datacenter not in dcs:
                continue
            price = (g.get("price") or {}).get("secure" if cloud == "SECURE" else "community")
            out.append({"id": g["id"], "label": g.get("name") or g["id"], "vram": g.get("memory"), "usd_h": price,
                        "availability": dcs.get(datacenter) if datacenter else g.get("availability")})
        return sorted(out, key=lambda x: (x["usd_h"] is None, x["usd_h"] or 0))
    except Exception:
        return [{"id": k, **v, "availability": None} for k, v in GPUS.items()]


# --- S3 (network volume) ----------------------------------------------------------------------------------------

def s3(loc: dict | None = None):
    import boto3
    from botocore.config import Config
    ak, sk = config.get_secret("runpod_s3_access_key"), config.get_secret("runpod_s3_secret_key")
    if not ak or not sk:
        raise RunPodError("尚未設定 RunPod S3 金鑰（設定 → 雲端）。")
    dc = ((loc or {}).get("datacenter") or config.load_settings().get("runpod_datacenter") or "").strip()
    return boto3.client("s3", aws_access_key_id=ak, aws_secret_access_key=sk, region_name=dc.upper(),
                        endpoint_url=S3_FMT.format(dc=dc.lower()),
                        config=Config(signature_version="s3v4", retries={"max_attempts": 8, "mode": "adaptive"},
                                      s3={"addressing_style": "path"}, connect_timeout=20, read_timeout=120))


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


def get_json(key: str, loc: dict | None = None) -> dict | None:
    """None only when the object does not exist; network or permission errors propagate to the caller's retry."""
    try:
        obj = s3(loc).get_object(Bucket=bucket(loc), Key=key)
    except Exception as e:
        if _missing(e):
            return None
        raise
    with obj["Body"] as body:
        raw = body.read().decode("utf-8")
    try:
        return json.loads(raw)
    except ValueError:  # caught mid-write; treat as not there yet
        return None


def exists(key: str, loc: dict | None = None) -> bool:
    try:
        s3(loc).head_object(Bucket=bucket(loc), Key=key)
        return True
    except Exception as e:
        if _missing(e):
            return False
        raise


def get_text(key: str, tail: int = 20000, loc: dict | None = None) -> str:
    try:
        obj = s3(loc).get_object(Bucket=bucket(loc), Key=key)
        return obj["Body"].read().decode("utf-8", "replace")[-tail:]
    except Exception:
        return ""


def download(key: str, local: Path, progress=None, loc: dict | None = None) -> Path:
    c = s3(loc)
    size = c.head_object(Bucket=bucket(loc), Key=key)["ContentLength"]
    done = [0]

    def cb(n):
        done[0] += n
        if progress:
            progress(done[0] / max(1, size))
    local.parent.mkdir(parents=True, exist_ok=True)
    c.download_file(bucket(loc), key, str(local), Callback=cb)
    return local


def delete(key: str, loc: dict | None = None) -> None:
    try:
        s3(loc).delete_object(Bucket=bucket(loc), Key=key)
    except Exception as e:
        if not _missing(e):
            raise

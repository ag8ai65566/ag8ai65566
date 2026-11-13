"""A stand-in for Runpod's REST API v2, for tests.

Only the calls this app makes, with the shapes read from Runpod's published
schema (https://api.runpod.io/v2/openapi.json, fetched 2026-11-12). It is
strict where the real one is strict: a pod request with a field the schema
does not have is a 400, so a typo in `runpod.pod_body` fails a test here
instead of failing the user's first rental.
"""

from __future__ import annotations

from aiohttp import web

# CreatePodRequest's properties, resolved through its allOf parts.
POD_FIELDS = {
    "args", "cloud", "cmd", "cpu", "dataCenterIds", "disk", "entrypoint", "env",
    "globalNetworking", "gpu", "image", "mounts", "name", "ports", "registry",
    "startJupyter", "startSsh", "templateId",
}
GPU_FIELDS = {"allowedCudaVersions", "count", "id", "minCudaVersion", "minRamPerGpu",
              "minVcpuCountPerGpu"}
MOUNT_FIELDS = {"global", "network", "persistent"}
NETWORK_MOUNT_FIELDS = {"path", "volumeId"}

GPUS = [
    {"id": "NVIDIA GeForce RTX 4090", "name": "RTX 4090", "memory": 24,
     "secure": True, "community": True,
     "price": {"secure": 0.69, "community": 0.34}, "availability": "HIGH",
     "dataCenters": [{"id": "EU-RO-1", "name": "Romania", "availability": "HIGH"},
                     {"id": "US-TX-3", "name": "Texas", "availability": "LOW"}]},
    {"id": "NVIDIA H100 80GB HBM3", "name": "H100 SXM", "memory": 80,
     "secure": True, "community": False,
     "price": {"secure": 2.69, "community": 0}, "availability": "LOW",
     "dataCenters": [{"id": "US-TX-3", "name": "Texas", "availability": "LOW"}]},
    {"id": "NVIDIA A40", "name": "A40", "memory": 48, "secure": True, "community": True,
     "price": {"secure": 0.40, "community": 0.35}, "availability": "NONE",
     "dataCenters": [{"id": "EU-RO-1", "name": "Romania", "availability": "NONE"}]},
]


class FakeRunpod:
    def __init__(self, key: str = "rp-test-key") -> None:
        self.key = key
        self.volumes: dict[str, dict] = {}
        self.pods: dict[str, dict] = {}
        self.pod_bodies: list[dict] = []
        self.terminated: list[str] = []
        self.calls: list[tuple[str, str]] = []
        self.next_status = "RUNNING"

    def app(self) -> web.Application:
        app = web.Application(middlewares=[self.auth])
        app.add_routes([
            web.get("/v2/catalog/gpus", self.gpus),
            web.get("/v2/network-volumes", self.list_volumes),
            web.post("/v2/network-volumes", self.create_volume),
            web.delete("/v2/network-volumes/{id}", self.delete_volume),
            web.get("/v2/pods", self.list_pods),
            web.post("/v2/pods", self.create_pod),
            web.get("/v2/pods/{id}", self.get_pod),
            web.delete("/v2/pods/{id}", self.delete_pod),
            web.post("/v2/pods/{id}/action", self.action),
            web.post("/v2/pods/{id}/exec", self.exec),
        ])
        return app

    @web.middleware
    async def auth(self, request, handler):
        self.calls.append((request.method, request.path))
        if request.headers.get("Authorization") != f"Bearer {self.key}":
            return web.json_response({"title": "Unauthorized", "status": 401,
                                      "detail": "invalid api key", "errors": []}, status=401)
        return await handler(request)

    @staticmethod
    def refuse(detail: str, errors: list[str] | None = None, status: int = 400):
        return web.json_response({"title": "Bad Request", "status": status,
                                  "detail": detail, "errors": errors or []}, status=status)

    async def gpus(self, request):
        cloud = request.query.get("cloud", "SECURE")
        key = "secure" if cloud == "SECURE" else "community"
        return web.json_response({"gpus": [g for g in GPUS if g[key]]})

    async def list_volumes(self, _request):
        return web.json_response({"networkVolumes": list(self.volumes.values())})

    async def create_volume(self, request):
        body = await request.json()
        if set(body) - {"dataCenter", "name", "size"} or not 10 <= int(body.get("size") or 0) <= 4096:
            return self.refuse("bad volume request")
        volume_id = f"vol{len(self.volumes) + 1}"
        self.volumes[volume_id] = {"id": volume_id, "name": body["name"], "size": body["size"],
                                   "dataCenter": body["dataCenter"], "type": "STANDARD"}
        return web.json_response(self.volumes[volume_id], status=201)

    async def delete_volume(self, request):
        volume_id = request.match_info["id"]
        if any(p["status"] != "TERMINATED" and volume_id in str(p["body"].get("mounts"))
               for p in self.pods.values()):
            return self.refuse("volume is attached to a pod", status=409)
        self.volumes.pop(volume_id, None)
        return web.Response(status=204)

    async def list_pods(self, _request):
        return web.json_response({"pods": [self.public(p) for p in self.pods.values()]})

    async def create_pod(self, request):
        body = await request.json()
        self.pod_bodies.append(body)
        errors = [f"unknown field: {k}" for k in sorted(set(body) - POD_FIELDS)]
        errors += [f"gpu: unknown field {k}" for k in set(body.get("gpu") or {}) - GPU_FIELDS]
        mounts = body.get("mounts") or {}
        errors += [f"mounts: unknown field {k}" for k in set(mounts) - MOUNT_FIELDS]
        for mount in mounts.get("network") or []:
            errors += [f"mounts.network: unknown field {k}" for k in set(mount) - NETWORK_MOUNT_FIELDS]
            if mount.get("volumeId") not in self.volumes:
                errors.append("mounts.network: no such volume")
        if errors:
            return self.refuse("request does not match the schema", errors)
        if not (body.get("gpu") or {}).get("id"):
            return self.refuse("gpu.id is required")
        pod_id = f"pod{len(self.pods) + 1}"
        gpu = next((g for g in GPUS if g["id"] == body["gpu"]["id"]), GPUS[0])
        tier = "secure" if body.get("cloud", "SECURE") == "SECURE" else "community"
        self.pods[pod_id] = {"id": pod_id, "status": self.next_status, "body": body,
                             "cost": gpu["price"][tier]}
        return web.json_response(self.public(self.pods[pod_id]), status=201)

    def public(self, pod: dict) -> dict:
        return {"id": pod["id"], "name": pod["body"].get("name"), "status": pod["status"],
                "cost": pod["cost"], "image": pod["body"].get("image"),
                "env": pod["body"].get("env") or {}, "runtime": None}

    async def get_pod(self, request):
        pod = self.pods.get(request.match_info["id"])
        if pod is None or pod["status"] == "TERMINATED":
            return self.refuse("pod not found", status=404)
        return web.json_response(self.public(pod))

    async def delete_pod(self, request):
        pod = self.pods.get(request.match_info["id"])
        if pod is None:
            return self.refuse("pod not found", status=404)
        pod["status"] = "TERMINATED"
        self.terminated.append(pod["id"])
        return web.Response(status=204)

    async def action(self, request):
        pod = self.pods.get(request.match_info["id"])
        if pod is None:
            return self.refuse("pod not found", status=404)
        action = (await request.json()).get("action")
        pod["status"] = {"stop": "EXITED", "start": "RUNNING", "restart": "RUNNING",
                         "terminate": "TERMINATED"}.get(action, pod["status"])
        return web.json_response(self.public(pod))

    async def exec(self, request):
        return web.json_response({"stdout": "[00:00:01] == booting\n", "stderr": "",
                                  "exitCode": 0, "timedOut": False})

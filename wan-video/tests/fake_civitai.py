"""A stand-in CivitAI for tests.

Shaped after real responses from https://civitai.com/api/v1/models, including
the two behaviours that bite in practice: 403 without a User-Agent, and 401 on
file downloads without an API key.
"""

from __future__ import annotations

from aiohttp import web

# baseModel strings taken from live CivitAI search results.
WAN22_I2V = "Wan Video 2.2 I2V-A14B"
WAN22_T2V = "Wan Video 2.2 T2V-A14B"
HUNYUAN = "Hunyuan Video"


def _model(mid, name, base, *, nsfw=False, files=None, words=None, downloads=1000):
    return {
        "id": mid,
        "name": name,
        "type": "LORA",
        "nsfw": nsfw,
        "creator": {"username": "someone"},
        "stats": {"downloadCount": downloads, "thumbsUpCount": downloads // 10},
        "tags": ["wan", "i2v"],
        "modelVersions": [
            {
                "id": mid * 10,
                "name": "v1",
                "baseModel": base,
                "trainedWords": words or [],
                "files": files
                or [
                    {
                        "name": f"{name.lower().replace(' ', '_')}.safetensors",
                        "sizeKB": 131072.0,
                        "type": "Model",
                        "primary": True,
                        "downloadUrl": f"__BASE__/api/download/models/{mid * 10}",
                    }
                ],
                "images": [
                    {"url": "https://image.example/x.jpg", "nsfwLevel": 4 if nsfw else 1, "type": "image"}
                ],
            }
        ],
    }


class FakeCivitai:
    def __init__(self, api_key: str = "") -> None:
        self.api_key = api_key
        self.searches: list[dict] = []
        self.downloads: list[str] = []
        self.payload = b"\0" * 4096
        self.base = ""

    def app(self) -> web.Application:
        app = web.Application()
        app.router.add_get("/api/v1/models", self.models)
        app.router.add_get("/api/v1/model-versions/{vid}", self.version)
        app.router.add_get("/api/download/models/{vid}", self.download)
        return app

    def _catalogue(self) -> list[dict]:
        return [
            _model(1, "Glass Kiss", WAN22_I2V, downloads=5000,
                   words=["glasskiss"],
                   files=[
                       {"name": "glass_kiss_high.safetensors", "sizeKB": 4096.0, "type": "Model",
                        "primary": True, "downloadUrl": "__BASE__/api/download/models/10"},
                       {"name": "glass_kiss_low.safetensors", "sizeKB": 4096.0, "type": "Model",
                        "primary": False, "downloadUrl": "__BASE__/api/download/models/11"},
                       # Non-weight entries must be filtered out by the client.
                       {"name": "training_data.zip", "sizeKB": 900.0, "type": "Training Data",
                        "primary": False, "downloadUrl": "__BASE__/api/download/models/12"},
                   ]),
            _model(2, "Spicy Motion", WAN22_I2V, nsfw=True, downloads=3000),
            _model(3, "T2V Only Thing", WAN22_T2V, downloads=2000),
            _model(4, "Old Hunyuan Style", HUNYUAN, downloads=900),
            # A model whose only version has no usable weight file: the client
            # must drop it rather than show an uninstallable card.
            {
                "id": 5, "name": "Broken", "type": "LORA", "nsfw": False,
                "creator": {"username": "x"}, "stats": {}, "tags": [],
                "modelVersions": [{"id": 50, "name": "v", "baseModel": WAN22_I2V,
                                   "files": [{"name": "notes.txt", "type": "Training Data",
                                              "sizeKB": 1.0, "downloadUrl": "u"}], "images": []}],
            },
        ]

    async def models(self, request: web.Request) -> web.Response:
        if "User-Agent" not in request.headers:
            return web.json_response({"error": "no UA"}, status=403)
        q = request.query
        self.searches.append(dict(q))
        bases = q.getall("baseModels", [])
        items = self._catalogue()
        if bases:
            items = [m for m in items
                     if any(v["baseModel"] in bases for v in m["modelVersions"])]
        if term := q.get("query"):
            items = [m for m in items if term.lower() in m["name"].lower()]
        if q.get("nsfw") == "true":
            items = [m for m in items if m.get("nsfw")]
        cursor = q.get("cursor")
        page = items[2:] if cursor else items[:2]
        meta = {"nextCursor": "2"} if not cursor and len(items) > 2 else {}
        body = web.json_response({"items": page, "metadata": meta})
        # Rewrite the placeholder so download URLs point back at this server.
        text = body.text.replace("__BASE__", self.base)
        return web.Response(text=text, content_type="application/json")

    async def version(self, request: web.Request) -> web.Response:
        vid = int(request.match_info["vid"])
        for m in self._catalogue():
            for v in m["modelVersions"]:
                if v["id"] == vid:
                    import json
                    return web.Response(
                        text=json.dumps(v).replace("__BASE__", self.base),
                        content_type="application/json")
        raise web.HTTPNotFound()

    async def download(self, request: web.Request) -> web.Response:
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer ") or not auth[7:]:
            return web.json_response({"error": "unauthorized"}, status=401)
        self.downloads.append(request.match_info["vid"])
        start = 0
        if (rng := request.headers.get("Range", "")).startswith("bytes="):
            start = int(rng.split("=")[1].split("-")[0])
        body = self.payload[start:]
        headers = {"Content-Length": str(len(body))}
        if start:
            headers["Content-Range"] = f"bytes {start}-{len(self.payload)-1}/{len(self.payload)}"
        return web.Response(status=206 if start else 200, body=body, headers=headers)

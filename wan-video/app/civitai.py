"""CivitAI browsing and LoRA downloads.

Two things about this API that are easy to get wrong, both verified against the
live service:

- It returns 403 to requests without a User-Agent.
- Model downloads return 401 without an API key, even for public files. Search
  works fine anonymously; only the actual download needs a key.

The `baseModels` filter takes exact strings; BASE_MODELS below lists the ones
that actually exist for video LoRAs, counted from live search results.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from urllib.parse import urlencode

import aiohttp

API = "https://civitai.com/api/v1"
UA = "wan-video/1.0 (+local ComfyUI front-end)"

# Exact CivitAI baseModel strings, with the rough number of LoRAs each had when
# this was written, so the ordering reflects where the content actually is.
BASE_MODELS = {
    "wan22_i2v": "Wan Video 2.2 I2V-A14B",   # ~383
    "wan22_t2v": "Wan Video 2.2 T2V-A14B",   # ~179
    "wan22_5b": "Wan Video 2.2 TI2V-5B",     # ~12
    "wan21_t2v": "Wan Video 14B t2v",        # ~70
    "wan21_i2v_480": "Wan Video 14B i2v 480p",
    "wan21_i2v_720": "Wan Video 14B i2v 720p",
    "wan_generic": "Wan Video",
    "hunyuan": "Hunyuan Video",              # original HunyuanVideo, not 1.5
    "ltx23": "LTXV 2.3",
}

# The URL shapes a person actually ends up with after browsing CivitAI. All of
# them were checked against the live site; the query string matters because the
# model page defaults to the *newest* version, and someone who picked an older
# one from the version tabs has `?modelVersionId=` in their address bar and
# means that one.
#
#   https://civitai.com/models/573152
#   https://civitai.com/models/573152/lustify-nsfw-checkpoint
#   https://civitai.com/models/573152?modelVersionId=3045803
#   https://civitai.com/api/download/models/3045803
#   civitai.red / civitarchive mirrors, same path shape
#   a bare number, which people paste too
URL_RE = re.compile(
    r"""(?:
          /api/download/models/(?P<download>\d+)
        | /models/(?P<model>\d+)
        | ^(?P<bare>\d+)$
        )""",
    re.VERBOSE,
)
VERSION_QUERY_RE = re.compile(r"[?&]modelVersionId=(\d+)")


@dataclass(frozen=True)
class ParsedUrl:
    """What a pasted CivitAI link points at.

    `version_id` is authoritative when present: a model page shows whichever
    version was picked, and downloading "the model" would silently hand over a
    different one - LUSTIFY's newest version is a different architecture from
    the one two tabs to the left.
    """

    model_id: int = 0
    version_id: int = 0

    @property
    def ok(self) -> bool:
        return bool(self.model_id or self.version_id)


def parse_url(text: str) -> ParsedUrl:
    """Pull a model or version id out of whatever the user pasted.

    Deliberately permissive about the host: civitai.red and the archive mirrors
    use the same path shape, and refusing them would mean telling someone their
    own working link is invalid. The id is what gets used, and it is looked up
    against the real API afterwards - so a wrong guess fails as "not found"
    rather than downloading something unexpected.
    """
    raw = (text or "").strip()
    if not raw:
        return ParsedUrl()
    version = 0
    if q := VERSION_QUERY_RE.search(raw):
        version = int(q.group(1))
    match = URL_RE.search(raw)
    if not match:
        return ParsedUrl(version_id=version)
    if got := match.group("download"):
        # A direct download link names the version outright, and beats the
        # query string if somehow both are present.
        return ParsedUrl(version_id=int(got))
    if got := match.group("model"):
        return ParsedUrl(model_id=int(got), version_id=version)
    if got := match.group("bare"):
        # A bare number is ambiguous. Treat it as a model id, which is what the
        # number in a normal CivitAI URL is.
        return ParsedUrl(model_id=int(got), version_id=version)
    return ParsedUrl(version_id=version)


SORTS = ["Most Downloaded", "Highest Rated", "Newest", "Most Liked"]
PERIODS = ["AllTime", "Year", "Month", "Week", "Day"]


class CivitaiError(RuntimeError):
    pass


class NeedsApiKey(CivitaiError):
    pass


def api_key() -> str:
    return (os.environ.get("CIVITAI_API_KEY") or "").strip()


@dataclass
class LoraFile:
    name: str
    size_kb: float
    download_url: str
    primary: bool = False

    def public(self) -> dict:
        return {
            "name": self.name,
            "size": int(self.size_kb * 1024),
            "url": self.download_url,
            "primary": self.primary,
        }


@dataclass
class Version:
    id: int
    name: str
    base_model: str
    trained_words: list[str] = field(default_factory=list)
    files: list[LoraFile] = field(default_factory=list)
    images: list[dict] = field(default_factory=list)

    def public(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "base_model": self.base_model,
            "trained_words": self.trained_words,
            "files": [f.public() for f in self.files],
            "images": self.images,
        }


@dataclass
class Item:
    id: int
    name: str
    nsfw: bool
    creator: str
    downloads: int
    likes: int
    tags: list[str]
    versions: list[Version]

    def public(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "nsfw": self.nsfw,
            "creator": self.creator,
            "downloads": self.downloads,
            "likes": self.likes,
            "tags": self.tags[:8],
            "url": f"https://civitai.com/models/{self.id}",
            "versions": [v.public() for v in self.versions],
        }


def _parse_version(raw: dict) -> Version:
    files = []
    for f in raw.get("files") or []:
        # Only weight files are useful here; skip training data, configs, etc.
        if (f.get("type") or "Model") != "Model":
            continue
        url = f.get("downloadUrl")
        name = f.get("name")
        if not url or not name:
            continue
        files.append(
            LoraFile(
                name=name,
                size_kb=float(f.get("sizeKB") or 0),
                download_url=url,
                primary=bool(f.get("primary")),
            )
        )
    images = [
        {"url": i["url"], "nsfw_level": i.get("nsfwLevel", 0), "type": i.get("type", "image")}
        for i in (raw.get("images") or [])
        if i.get("url")
    ][:4]
    return Version(
        id=raw.get("id", 0),
        name=raw.get("name") or "",
        base_model=raw.get("baseModel") or "",
        trained_words=[w for w in (raw.get("trainedWords") or []) if w][:8],
        files=files,
        images=images,
    )


def _parse_item(raw: dict) -> Item:
    stats = raw.get("stats") or {}
    versions = [_parse_version(v) for v in (raw.get("modelVersions") or [])]
    # A version with no usable weight file cannot be installed, so drop it.
    versions = [v for v in versions if v.files]
    return Item(
        id=raw.get("id", 0),
        name=raw.get("name") or "(untitled)",
        nsfw=bool(raw.get("nsfw")),
        creator=((raw.get("creator") or {}).get("username") or ""),
        downloads=int(stats.get("downloadCount") or 0),
        likes=int(stats.get("thumbsUpCount") or 0),
        tags=[t for t in (raw.get("tags") or []) if isinstance(t, str)],
        versions=versions,
    )


async def search(
    *,
    query: str = "",
    base_models: list[str] | None = None,
    nsfw: bool | None = None,
    sort: str = "Most Downloaded",
    period: str = "AllTime",
    limit: int = 24,
    cursor: str = "",
    types: str = "LORA",
) -> dict:
    params: list[tuple[str, str]] = [
        ("types", types if types in ("LORA", "Checkpoint", "TextualInversion") else "LORA"),
        ("limit", str(max(1, min(limit, 100)))),
        ("sort", sort if sort in SORTS else SORTS[0]),
        ("period", period if period in PERIODS else "AllTime"),
    ]
    if query.strip():
        params.append(("query", query.strip()))
    for base in base_models or []:
        params.append(("baseModels", base))
    if nsfw is not None:
        params.append(("nsfw", "true" if nsfw else "false"))
    if cursor:
        params.append(("cursor", cursor))

    headers = {"User-Agent": UA, "Accept": "application/json"}
    if key := api_key():
        headers["Authorization"] = f"Bearer {key}"

    url = f"{API}/models?{urlencode(params)}"
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=45)) as response:
            body = await response.text()
            if response.status == 403:
                raise CivitaiError("CivitAI 拒絕這個請求（403）。稍後再試，或設一個 API key。")
            if response.status == 429:
                raise CivitaiError("CivitAI 說請求太頻繁（429）。等一下再搜。")
            if response.status != 200:
                raise CivitaiError(f"CivitAI 回應 {response.status}：{body[:200]}")
            import json

            data = json.loads(body)

    items = [_parse_item(raw) for raw in (data.get("items") or [])]
    items = [i for i in items if i.versions]
    meta = data.get("metadata") or {}
    return {
        "items": [i.public() for i in items],
        "next_cursor": str(meta.get("nextCursor") or ""),
        "has_key": bool(api_key()),
    }


async def version(version_id: int) -> dict:
    headers = {"User-Agent": UA, "Accept": "application/json"}
    if key := api_key():
        headers["Authorization"] = f"Bearer {key}"
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(
            f"{API}/model-versions/{version_id}", timeout=aiohttp.ClientTimeout(total=45)
        ) as response:
            if response.status == 404:
                raise CivitaiError(f"找不到這個版本（{version_id}）")
            if response.status != 200:
                raise CivitaiError(f"CivitAI 回應 {response.status}")
            raw = await response.json()
    return _parse_version(raw).public()


async def resolve(text: str) -> dict:
    """Turn a pasted CivitAI link into the same shape the search results have.

    Two lookups are possible and they answer different questions. A version id
    names one file set outright. A model id names a *page*, whose versions can
    be different architectures - so the versions are all returned and the caller
    picks, rather than this quietly taking the newest.
    """
    parsed = parse_url(text)
    if not parsed.ok:
        raise CivitaiError(
            "看不懂這個連結。貼 CivitAI 上那個模型的網址就可以，"
            "像 https://civitai.com/models/573152 ——"
            "網址列直接複製整條最保險。")

    headers = {"User-Agent": UA, "Accept": "application/json"}
    if key := api_key():
        headers["Authorization"] = f"Bearer {key}"

    async def fetch(url: str) -> dict:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=45)) as response:
                if response.status == 404:
                    raise CivitaiError("CivitAI 上找不到這個東西（404）。連結對嗎？")
                if response.status == 403:
                    raise CivitaiError("CivitAI 拒絕這個請求（403）。稍後再試。")
                if response.status != 200:
                    raise CivitaiError(f"CivitAI 回應 {response.status}")
                return await response.json()

    if parsed.version_id and not parsed.model_id:
        raw = await fetch(f"{API}/model-versions/{parsed.version_id}")
        model_id = (raw.get("modelId") or 0)
        model = await fetch(f"{API}/models/{model_id}") if model_id else {}
        versions = [_parse_version(raw)]
    else:
        model = await fetch(f"{API}/models/{parsed.model_id}")
        versions = [_parse_version(v) for v in (model.get("modelVersions") or [])]
        versions = [v for v in versions if v.files]
        if parsed.version_id:
            # The user was looking at a specific version tab; put it first
            # rather than letting the newest win by default.
            versions.sort(key=lambda v: v.id != parsed.version_id)

    if not versions:
        raise CivitaiError("這個項目沒有可下載的權重檔。")

    kind = (model.get("type") or "").lower()
    return {
        "id": model.get("id") or 0,
        "name": model.get("name") or "",
        "type": model.get("type") or "",
        # LORA and Checkpoint go into different folders, and getting it wrong
        # means ComfyUI simply never lists the file. Reported so the UI can say
        # which one this is before anything is fetched.
        "kind": "checkpoint" if kind == "checkpoint" else "lora",
        "nsfw": bool(model.get("nsfw")),
        "creator": (model.get("creator") or {}).get("username", ""),
        "page_url": f"https://civitai.com/models/{model.get('id')}"
                    if model.get("id") else "",
        "asked_version": parsed.version_id,
        "versions": [v.public() for v in versions],
        "has_key": bool(api_key()),
    }


def download_headers() -> dict:
    """Headers for fetching a LoRA file. Raises if no key is configured."""
    key = api_key()
    if not key:
        raise NeedsApiKey(
            "CivitAI 下載需要 API key（搜尋不用）。到 civitai.com → 右上頭像 → "
            "Account settings → API Keys 產生一個，然後填進 .env 的 CIVITAI_API_KEY="
        )
    return {"User-Agent": UA, "Authorization": f"Bearer {key}"}

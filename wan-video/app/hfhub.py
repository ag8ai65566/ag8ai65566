"""Hugging Face as a second source: paste a link, pick the files, download.

Deliberately **not** a search. That was the agreement reached with a second
model after looking at what HF actually returns, and there were two reasons:

  * `filter=lora` is dominated by *language* model adapters. Of the eight
    most-downloaded results, six were Qwen/Gemma coder GGUFs. A search built on
    it would mostly offer things that cannot load in ComfyUI at all.
  * HF has no equivalent of CivitAI's structured `baseModel`. The information
    exists - in `cardData.base_model` and in `base_model:*` tags - but it is a
    *repo id* (`Comfy-Org/MiniMax-H3`), it is absent from search results, and
    it is sometimes the repo itself. A LoRA on the wrong base does not error,
    it quietly does nothing, so a compatibility claim we cannot stand behind is
    worse than no claim.

So this module answers a narrower question, which it can answer honestly: *the
user has a link; what is in it, and which file do they want?* Every file is
listed with its size and the declared base model, and the user ticks one.

Two safety properties, both load-bearing:

  * The download URL is built here from `repo_id + revision + path`. The browser
    never supplies a URL. Otherwise "download this" plus the user's HF token
    would be an open proxy that attaches their credentials to any host.
  * Only `.safetensors` and `.gguf` are offered. `.bin`, `.pt` and `.ckpt` are
    pickle formats that execute code on load.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import aiohttp

API = "https://huggingface.co/api"
HOST = "https://huggingface.co"
UA = "wan-video/1.0 (+local ComfyUI front-end)"

# Formats that are just tensors. Anything else can run code when it loads, and
# no amount of "but I trust this uploader" makes that a good default.
SAFE_SUFFIXES = (".safetensors", ".gguf")
PICKLE_SUFFIXES = (".bin", ".pt", ".pth", ".ckpt", ".pkl")


class HubError(RuntimeError):
    pass


class NeedsToken(HubError):
    pass


# The URL shapes a person ends up with after browsing HF. A repo id has exactly
# one slash and no scheme, which is also what people paste from a model card.
URL_RE = re.compile(
    r"""^(?:https?://(?:www\.)?huggingface\.co/)?
        (?:(?P<kind>models|datasets|spaces)/)?
        (?P<owner>[A-Za-z0-9][A-Za-z0-9._-]*)
        /(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)
        (?:/(?:tree|blob|resolve)/(?P<rev>[^/\s]+)(?P<path>/[^\s?#]*)?)?
        /?(?:[?#].*)?$""",
    re.VERBOSE,
)


@dataclass(frozen=True)
class ParsedRef:
    repo_id: str = ""
    revision: str = "main"
    path: str = ""          # a file or subfolder the link pointed at, if any

    @property
    def ok(self) -> bool:
        return bool(self.repo_id)


def parse_url(text: str) -> ParsedRef:
    """Pull a repo id (and any revision/path) out of whatever was pasted."""
    raw = (text or "").strip()
    if not raw:
        return ParsedRef()
    match = URL_RE.match(raw)
    if not match:
        return ParsedRef()
    if match.group("kind") in ("datasets", "spaces"):
        # Recognised, and deliberately refused: neither holds ComfyUI weights.
        raise HubError("這是 HuggingFace 的 dataset 或 space，不是模型。")
    repo = f"{match.group('owner')}/{match.group('name')}"
    return ParsedRef(
        repo_id=repo,
        revision=match.group("rev") or "main",
        path=(match.group("path") or "").lstrip("/"),
    )


@dataclass
class HubFile:
    path: str
    size: int
    lfs: bool = False

    @property
    def name(self) -> str:
        return self.path.rsplit("/", 1)[-1]

    @property
    def folder_hint(self) -> str:
        """Where this most likely belongs under ComfyUI's models directory.

        A hint, not a decision: the user confirms it. Guessing silently is how
        a checkpoint ends up in loras/ and never appears in either menu.
        """
        lower = self.path.lower()
        if "vae" in lower:
            return "vae"
        if "text_encoder" in lower or "clip" in lower:
            return "text_encoders"
        if "controlnet" in lower:
            return "controlnet"
        if "lora" in lower or "adapter" in lower:
            return "loras"
        if "diffusion_model" in lower or "unet" in lower:
            return "diffusion_models"
        # Under ~1GB a standalone weight file is almost always an adapter;
        # a full checkpoint is 2GB and up.
        return "loras" if self.size and self.size < 1_500_000_000 else "checkpoints"

    def public(self) -> dict:
        return {"path": self.path, "name": self.name, "size": self.size,
                "folder": self.folder_hint}


@dataclass
class HubRepo:
    repo_id: str
    revision: str
    sha: str = ""
    author: str = ""
    licence: str = ""
    pipeline: str = ""
    gated: bool = False
    base_models: list[str] = field(default_factory=list)
    base_confidence: str = "unknown"   # declared | inferred | unknown
    tags: list[str] = field(default_factory=list)
    files: list[HubFile] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    likes: int = 0
    downloads: int = 0

    def public(self) -> dict:
        return {
            "repo_id": self.repo_id, "revision": self.revision, "sha": self.sha,
            "author": self.author, "licence": self.licence,
            "pipeline": self.pipeline, "gated": self.gated,
            "base_models": self.base_models,
            "base_confidence": self.base_confidence,
            "tags": self.tags[:12],
            "files": [f.public() for f in self.files],
            "skipped": self.skipped,
            "likes": self.likes, "downloads": self.downloads,
            "page_url": f"{HOST}/{self.repo_id}",
        }


def _base_models(raw: dict) -> tuple[list[str], str]:
    """What the uploader says this was built on, and how much that is worth.

    `cardData.base_model` is the uploader's own declaration and can be a string
    or a list. The `base_model:*` tags are derived by HF from the same field, so
    they are the same evidence rather than a second source - which is why
    finding only tags is still "declared" and never "confirmed".
    """
    card = raw.get("cardData") or {}
    declared = card.get("base_model")
    out: list[str] = []
    if isinstance(declared, str):
        out = [declared]
    elif isinstance(declared, list):
        out = [str(x) for x in declared if x]
    if out:
        # A repo that lists itself first tells us nothing; drop that entry.
        out = [b for b in out if b.lower() != str(raw.get("id", "")).lower()]
        if out:
            return out, "declared"
    tagged = [t.split(":", 1)[1] for t in (raw.get("tags") or [])
              if isinstance(t, str) and t.startswith("base_model:")]
    tagged = [t.split(":", 1)[-1] for t in tagged]
    tagged = [t for t in dict.fromkeys(tagged) if t and "/" in t]
    if tagged:
        return tagged, "declared"
    return [], "unknown"


async def _get(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=45)) as response:
        if response.status == 404:
            raise HubError("HuggingFace 上找不到這個 repo（404）。名字對嗎？是不是私有的？")
        if response.status in (401, 403):
            # HF answers 401 for a repo that does not exist as well as for one
            # that needs a token: it will not confirm whether a private repo is
            # there. So the two cases are genuinely indistinguishable from here,
            # and saying only "you need to log in" sends someone hunting for a
            # token when they actually mistyped the name.
            raise NeedsToken(
                f"HuggingFace 回 {response.status} —— 這代表**兩種可能**，"
                "而且從外面分不出是哪一種："
                "①這個 repo 不存在（名字打錯了？）；"
                "②它存在但需要登入 —— 那就到那個頁面按同意授權，"
                "再到「設定」分頁貼上 Hugging Face token。"
                "先確認網址複製對了，再去弄 token。")
        if response.status != 200:
            raise HubError(f"HuggingFace 回應 {response.status}")
        return await response.json()


async def resolve(text: str, *, token: str = "") -> dict:
    """Look up a pasted link and list the weight files it holds."""
    ref = parse_url(text)
    if not ref.ok:
        raise HubError(
            "看不懂這個連結。貼 HuggingFace 的模型網址或 repo 名稱，"
            "像 https://huggingface.co/Comfy-Org/MiniMax-H3 或 Comfy-Org/MiniMax-H3。")

    headers = {"User-Agent": UA, "Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    async with aiohttp.ClientSession(headers=headers) as session:
        info = await _get(session, f"{API}/models/{ref.repo_id}?revision={ref.revision}")
        tree = await _get(
            session,
            f"{API}/models/{ref.repo_id}/tree/{ref.revision}?recursive=1&expand=1")

    files, skipped = [], []
    for entry in tree if isinstance(tree, list) else []:
        if entry.get("type") != "file":
            continue
        path = entry.get("path") or ""
        lower = path.lower()
        if lower.endswith(PICKLE_SUFFIXES):
            # Named rather than hidden: "there is a file here you cannot have,
            # and why" is more useful than pretending the repo is empty.
            skipped.append(path)
            continue
        if not lower.endswith(SAFE_SUFFIXES):
            continue
        size = (entry.get("lfs") or {}).get("size") or entry.get("size") or 0
        files.append(HubFile(path=path, size=int(size),
                             lfs=bool(entry.get("lfs"))))

    # A link that pointed into a subfolder or at one file means that part.
    if ref.path:
        narrowed = [f for f in files
                    if f.path == ref.path or f.path.startswith(ref.path.rstrip("/") + "/")]
        if narrowed:
            files = narrowed

    files.sort(key=lambda f: (-f.size, f.path))
    bases, confidence = _base_models(info)
    repo = HubRepo(
        repo_id=ref.repo_id,
        revision=ref.revision,
        sha=str(info.get("sha") or ""),
        author=str(info.get("author") or ref.repo_id.split("/")[0]),
        licence=str((info.get("cardData") or {}).get("license") or ""),
        pipeline=str(info.get("pipeline_tag") or ""),
        gated=bool(info.get("gated")),
        base_models=bases,
        base_confidence=confidence,
        tags=[t for t in (info.get("tags") or []) if isinstance(t, str)],
        files=files,
        skipped=skipped[:8],
        likes=int(info.get("likes") or 0),
        downloads=int(info.get("downloads") or 0),
    )
    if not files:
        raise HubError(
            f"{ref.repo_id} 裡沒有可以下載的權重檔"
            + (f"（有 {len(skipped)} 個 .bin/.pt，那種格式載入時會執行程式碼，這裡不收）"
               if skipped else "。"))
    return repo.public()


def download_url(repo_id: str, revision: str, path: str) -> str:
    """Build the download URL from parts the caller validated.

    Built here rather than accepted from the browser on purpose: the request
    carries the user's Hugging Face token, and a caller-supplied URL would make
    this an open proxy that attaches their credentials to any host they name.
    """
    if not repo_id or "/" not in repo_id:
        raise HubError(f"不合法的 repo：{repo_id}")
    for part, label in ((revision, "revision"), (path, "path")):
        if not part or ".." in part or part.startswith("/"):
            raise HubError(f"不合法的 {label}：{part}")
    return f"{HOST}/{repo_id}/resolve/{revision}/{path}"

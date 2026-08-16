"""Noticing that something has a newer version, without going to look.

Three separate questions, deliberately kept apart because they fail
independently and one being offline must not hide the others:

- Is this app itself behind its git remote?
- Is the ComfyUI underneath it behind?
- Do any installed LoRAs / checkpoints have a newer version on CivitAI?

The CivitAI half is the one that matters day to day. A LoRA author pushing "v2"
does not touch the file already on disk, so the only way to find out today is to
revisit every model page by hand. The `.civitai.json` sidecar written at
download time carries the page URL, which is enough to ask the API.

Everything here is best-effort: a failed check reports itself as unknown and
never blocks anything.
"""

from __future__ import annotations

import asyncio
import json
import re
import subprocess
import time
from pathlib import Path

import aiohttp
import civitai

CACHE_TTL = 6 * 3600
_cache: dict[str, tuple[float, dict]] = {}


def _cached(key: str) -> dict | None:
    hit = _cache.get(key)
    if hit and time.time() - hit[0] < CACHE_TTL:
        return hit[1]
    return None


def _store(key: str, value: dict) -> dict:
    _cache[key] = (time.time(), value)
    return value


def forget() -> None:
    _cache.clear()


# -- git ---------------------------------------------------------------------


def _git(repo: Path, *args: str, timeout: int = 30) -> tuple[bool, str]:
    try:
        done = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True, text=True, timeout=timeout,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return False, str(exc)
    return done.returncode == 0, (done.stdout or done.stderr).strip()


def git_status(repo: Path, label: str) -> dict:
    """How far behind `repo`'s upstream branch is, if it is a git checkout."""
    out = {"label": label, "ok": False, "behind": 0, "detail": "", "local": "", "remote": ""}
    if not (repo / ".git").exists():
        out["detail"] = "不是 git 目錄，沒辦法自動檢查更新"
        return out
    ok, head = _git(repo, "rev-parse", "--short", "HEAD")
    if not ok:
        out["detail"] = head
        return out
    out["local"] = head
    ok, fetched = _git(repo, "fetch", "--quiet", "origin", timeout=90)
    if not ok:
        out["detail"] = f"連不上 origin：{fetched[:120]}"
        return out
    ok, upstream = _git(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    if not ok:
        out["detail"] = "這個分支沒有設定對應的遠端分支"
        return out
    ok, count = _git(repo, "rev-list", "--count", f"HEAD..{upstream}")
    if not ok:
        out["detail"] = count
        return out
    ok, remote_head = _git(repo, "rev-parse", "--short", upstream)
    out.update(
        ok=True,
        behind=int(count or 0),
        remote=remote_head if ok else "",
        detail="已經是最新的" if int(count or 0) == 0 else f"落後 {count} 個更新",
    )
    return out


def pull(repo: Path) -> dict:
    """Fast-forward a checkout to its upstream.

    Only ever a fast-forward. ComfyUI's models/, custom_nodes/, output/, input/
    and user/ are all in its .gitignore, so a fast-forward cannot touch them -
    but a merge or a rebase could reach tracked files the user has edited, and
    then the failure lands in the middle of someone's install rather than here.
    """
    out = {"ok": False, "detail": "", "before": "", "after": ""}
    if not (repo / ".git").exists():
        out["detail"] = "這個資料夾不是 git 目錄，沒辦法自動更新"
        return out
    ok, before = _git(repo, "rev-parse", "--short", "HEAD")
    if not ok:
        out["detail"] = before
        return out
    out["before"] = before
    ok, dirty = _git(repo, "status", "--porcelain", "--untracked-files=no")
    if ok and dirty.strip():
        # Porcelain is "XY <path>", but the status pair may be one char plus a
        # space, so splitting beats a fixed slice - which ate the leading "n"
        # of "nodes.py".
        changed = [l.split(maxsplit=1)[-1] for l in dirty.splitlines()[:4] if l.strip()]
        out["detail"] = (
            "資料夾裡有被改過的檔案，先不自動更新（怕蓋掉你的修改）："
            + "、".join(changed)
        )
        return out
    ok, said = _git(repo, "pull", "--ff-only", timeout=300)
    forget()
    if not ok:
        out["detail"] = f"git pull 失敗：{said[:200]}"
        return out
    ok2, after = _git(repo, "rev-parse", "--short", "HEAD")
    out.update(ok=True, after=after if ok2 else "",
               detail="已經是最新的" if before == after else f"更新完成：{before} → {after}")
    return out


def app_updates(app_repo: Path, comfy_repo: Path) -> dict:
    key = f"git:{app_repo}:{comfy_repo}"
    if hit := _cached(key):
        return hit
    return _store(
        key,
        {
            "app": git_status(app_repo, "這個 app"),
            "comfy": git_status(comfy_repo, "ComfyUI"),
        },
    )


# -- CivitAI -----------------------------------------------------------------

_MODEL_ID = re.compile(r"/models/(\d+)")


def sidecar_for(path: Path) -> dict:
    meta = path.with_name(path.name + ".civitai.json")
    if not meta.is_file():
        return {}
    try:
        return json.loads(meta.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}


async def _latest_version(session: aiohttp.ClientSession, model_id: str) -> dict | None:
    url = f"{civitai.API}/models/{model_id}"
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as r:
            if r.status != 200:
                return None
            body = await r.json()
    except (aiohttp.ClientError, asyncio.TimeoutError, ValueError):
        return None
    versions = body.get("modelVersions") or []
    if not versions:
        return None
    newest = versions[0]
    files = [
        {
            "name": f.get("name", ""),
            "size": int((f.get("sizeKB") or 0) * 1024),
            "url": f.get("downloadUrl", ""),
        }
        for f in (newest.get("files") or [])
        if (f.get("type") or "Model") == "Model"
    ]
    return {
        "model_id": model_id,
        "model_name": body.get("name", ""),
        "version_id": newest.get("id"),
        "version_name": newest.get("name", ""),
        "published": newest.get("publishedAt", ""),
        "base_model": newest.get("baseModel", ""),
        "trained_words": newest.get("trainedWords") or [],
        "files": files,
        "page_url": f"https://civitai.com/models/{model_id}",
    }


async def civitai_updates(files: list[Path]) -> list[dict]:
    """For each file with a CivitAI sidecar, whether a newer version exists.

    "Newer" means the model's current top version produces a filename we do not
    already have on disk. Comparing filenames rather than version ids is what
    survives the sidecar being written by an older build of this app, which did
    not record the version id at all.
    """
    targets: list[tuple[Path, dict, str]] = []
    for path in files:
        meta = sidecar_for(path)
        match = _MODEL_ID.search(meta.get("url") or "")
        if match:
            targets.append((path, meta, match.group(1)))
    if not targets:
        return []

    key = "civitai:" + ",".join(sorted(m for _, _, m in targets))
    if hit := _cached(key):
        return hit["items"]

    on_disk = {p.name for p in files}
    out: list[dict] = []
    headers = {"User-Agent": civitai.UA, "Accept": "application/json"}
    async with aiohttp.ClientSession(headers=headers) as session:
        # A handful of small requests; keep it polite rather than parallel.
        seen: dict[str, dict | None] = {}
        for path, meta, model_id in targets:
            if model_id not in seen:
                seen[model_id] = await _latest_version(session, model_id)
            latest = seen[model_id]
            if not latest:
                continue
            newer = [f for f in latest["files"] if f["name"] and f["name"] not in on_disk]
            if not newer:
                continue
            out.append(
                {
                    "have": path.name,
                    "have_label": meta.get("name") or path.name,
                    "folder": path.parent.name,
                    **latest,
                    "files": newer,
                }
            )
    _store(key, {"items": out})
    return out

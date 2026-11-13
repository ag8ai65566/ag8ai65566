"""Turn a picture into a recipe for making it again.

Three kinds of answer, never blended, because they have very different standing:

1. **Exact** - what the file itself says. A1111, Forge and CivitAI write the
   prompt and every setting into the image, and name each model and LoRA with
   a hash or a CivitAI version id. Each of those is looked up on CivitAI
   (``model-versions/by-hash``, ``model-versions/{id}``), so "which LoRA" gets
   a real answer: its page, its base model, its trigger words, a download.
   ComfyUI images name files only, so those are looked up by name and labelled
   as name matches.

2. **Described** - when the file says nothing. The tagger reads the pixels into
   danbooru tags, put in the order SDXL anime checkpoints were trained on
   (who and how many, then the character, their look, the outfit, the shot,
   then the medium), with watermarks and signatures moved to the negative.

3. **Candidates** - LoRAs on CivitAI that *might* give this look. Found by
   searching the character and style tags, plus a pool of the family's most
   downloaded style LoRAs (a style is often too subtle for any tag), then
   ranked by how close each LoRA's own sample pictures are to this one. Two
   measures, blended: *content* is the cosine of the tagger's full score
   vectors (what is in the picture), *style* compares colour palette,
   saturation and line density (how it is painted) - the tagger alone is
   dominated by content, and a watercolour LoRA lost to any LoRA whose sample
   happened to show the same hair colour. Either way it is a likeness score
   between two pictures, never an identification of what made this one -
   nothing can read a LoRA out of pixels - and the page says so.

What it will not do
-------------------
* Tags that put a minor in the frame stop the whole thing (the list is
  posebook.BLOCKED_TAGS, the same one the rest of the app uses).
* A LoRA CivitAI flags as a real person (``poi``) or as depicting minors
  (``minor``) is never suggested, and one named in a file's metadata is
  reported as withheld rather than linked.
* There is no face recognition anywhere: nothing here tries to work out *who*
  is in a picture.
"""

from __future__ import annotations

import asyncio
import io
import math
from dataclasses import dataclass, field

import civitai
import posebook
import tags

# CivitAI's `baseModels` filter values for each image checkpoint family this
# app ships, so suggested LoRAs are ones that actually load on the suggested
# checkpoint. NoobAI and Illustrious share a lineage and mostly each other's
# LoRAs, so each searches the other second.
BASES = {
    "noobai": ["NoobAI", "Illustrious"],
    "illustrious": ["Illustrious", "NoobAI"],
    "pony": ["Pony"],
    "cyberrealistic-pony": ["Pony"],
    "juggernaut": ["SDXL 1.0"],
    "epicrealism-xl": ["SDXL 1.0"],
    "lustify": ["SDXL 1.0"],
    "biglust": ["SDXL 1.0"],
    "sdxl-base": ["SDXL 1.0"],
}

# Never part of a picture's content: moved to the negative so the copy does
# not grow a watermark of its own.
TO_NEGATIVE = {
    "watermark", "signature", "artist_name", "username", "web_address", "logo",
    "twitter_username", "patreon_username", "dated", "text", "english_text",
    "japanese_text", "speech_bubble", "commentary", "commentary_request",
    "translated", "jpeg_artifacts",
}
# About the upload, not the picture.
SKIP = {"highres", "absurdres", "lowres", "bad_id", "bad_pixiv_id", "md5_mismatch",
        "photoshop_(medium)", "third-party_edit", "duplicate"}
# How many and who - always first in a danbooru prompt.
COUNTS = {"1girl", "2girls", "3girls", "4girls", "5girls", "6+girls", "multiple_girls",
          "1boy", "2boys", "3boys", "multiple_boys", "1other", "solo", "no_humans"}
# Medium and style tags worth searching CivitAI with: the term on the right is
# what LoRA authors call it. A style LoRA is the most common reason a copy
# "has the right content but looks wrong".
STYLE_QUERIES = {
    "watercolor_(medium)": "watercolor", "oil_painting_(medium)": "oil painting",
    "pixel_art": "pixel art", "chibi": "chibi", "sketch": "sketch",
    "lineart": "lineart", "monochrome": "monochrome", "greyscale": "monochrome",
    "traditional_media": "traditional media", "pastel_colors": "pastel",
    "flat_color": "flat color", "cel_shading": "cel shading", "impasto": "impasto",
    "ukiyo-e": "ukiyo-e", "retro_artstyle": "retro anime", "1990s_(style)": "90s anime",
    "1980s_(style)": "80s anime", "3d": "3d render", "realistic": "realistic",
    "photorealistic": "photorealistic", "cyberpunk": "cyberpunk", "steampunk": "steampunk",
    "art_nouveau": "art nouveau", "western_comics_(style)": "western comic",
    "anime_screencap": "anime screencap", "game_cg": "game cg", "faux_traditional_media": "painterly",
    "graphite_(medium)": "pencil", "colored_pencil_(medium)": "colored pencil",
    "marker_(medium)": "marker", "ink_(medium)": "ink", "neon_lights": "neon",
    "glitch": "glitch", "vaporwave": "vaporwave", "dark_fantasy": "dark fantasy",
}
STYLE_TAGS = set(STYLE_QUERIES)
MAX_QUERIES = 4
PER_QUERY = 6
POOL = 10
MAX_CANDIDATES = 20
# How the two likeness measures are blended into one score. Measured, not
# picked: 19 of the most downloaded Illustrious style LoRAs on CivitAI
# (2026-11-13), each one's second sample picture used as the "unknown" image
# and its first sample as the candidate. Content alone put the right LoRA
# first 2 times in 10; style alone 6 in 19; 0.2-0.3 content 9 in 19, with the
# right one ranked third of 19 on average (chance: tenth). Character LoRAs are
# the reason it is not 0: there the content is the point.
CONTENT_WEIGHT = 0.3


def _space(tag: str) -> str:
    return tag.replace("_", " ").strip().lower()


def blocked(guess: tags.Guess) -> list[str]:
    """Tags in this guess that put a minor in the frame."""
    names = [n for n, _ in guess.general] + [n for n, _ in guess.characters]
    return sorted({_space(n) for n in names if _space(n) in posebook.BLOCKED_TAGS})


def blocked_text(text: str) -> list[str]:
    """The same test for a prompt read out of a file."""
    words = {w.strip().lower().replace("_", " ") for w in text.replace("\n", ",").split(",")}
    return sorted(words & posebook.BLOCKED_TAGS)


# -- 2. described -------------------------------------------------------------


def prompt_from(guess: tags.Guess) -> tuple[str, list[str]]:
    """A danbooru prompt in training order, and the tags for the negative."""
    counts, style, negative = [], [], []
    rest = []
    for name, _p in guess.general:
        if name in SKIP:
            continue
        if name in TO_NEGATIVE:
            negative.append(tags.to_prompt(name))
        elif name in COUNTS:
            counts.append(name)
        elif name in STYLE_TAGS or name.endswith("_(medium)") or name.endswith("_(style)"):
            style.append(name)
        else:
            rest.append(name)
    split = tags.split_tags(rest)
    ordered = (counts + [n for n, _ in guess.characters]
               + split["look"] + split["outfit"] + split["scene"] + split["drop"] + style)
    seen, out = set(), []
    for name in ordered:
        if name not in seen:
            seen.add(name)
            out.append(tags.to_prompt(name))
    return ", ".join(out), negative


def nearest_size(width: int, height: int, area: int = 1024 * 1024) -> tuple[int, int]:
    """The SDXL-sized canvas with this picture's shape: ~1MP, sides a multiple of 64."""
    if width <= 0 or height <= 0:
        return 1024, 1024
    ratio = width / height
    w = math.sqrt(area * ratio)
    h = w / ratio
    snap = lambda v: int(max(512, min(2048, round(v / 64) * 64)))  # noqa: E731
    return snap(w), snap(h)


def queries(guess: tags.Guess) -> list[dict]:
    """What to search CivitAI for: confident characters first, then style."""
    out: list[dict] = []
    for name, p in guess.characters:
        if p >= 0.6:
            # `rem_(re:zero)` -> "rem re:zero": the series in brackets is how
            # LoRA authors disambiguate too, so it stays in the query.
            term = tags.to_prompt(name).replace("\\(", " ").replace("\\)", " ")
            term = " ".join(term.replace("(", " ").replace(")", " ").split())
            out.append({"query": term, "why": f"角色：{tags.to_prompt(name)}", "kind": "character"})
    for name, p in guess.general:
        if name in STYLE_QUERIES and p >= 0.35:
            term = STYLE_QUERIES[name]
            if all(q["query"] != term for q in out):
                out.append({"query": term, "why": f"畫風：{tags.to_prompt(name)}", "kind": "style"})
    out = out[:MAX_QUERIES - 1]
    # Last, always: the family's most downloaded style LoRAs, for the ranker
    # to pick from by look when no tag named the style.
    out.append({"query": "", "tag": "style", "why": "熱門畫風 LoRA（比對色彩和筆觸）", "kind": "style"})
    return out


@dataclass
class Recipe:
    """Everything the image tab needs to try making the picture again."""

    exact: bool
    prompt: str
    negative: str
    model_id: str
    width: int
    height: int
    steps: int | None = None
    cfg: float | None = None
    sampler: str = ""
    scheduler: str = ""
    seed: int | None = None
    clip_skip: int | None = None
    loras: list[dict] = field(default_factory=list)
    # To come out nearly identical rather than merely alike, start from the
    # original itself: img2img at this denoise keeps its composition and
    # colours and lets the model redraw the detail.
    img2img_denoise: float = 0.45
    notes: list[str] = field(default_factory=list)

    def public(self) -> dict:
        return dict(self.__dict__)


def recipe(found, guess: tags.Guess | None, size: tuple[int, int]) -> Recipe:
    """The best recipe the evidence supports. Exact settings win over a guess."""
    model_id = tags.suggest_model(guess) if guess else "illustrious"
    if found is not None and found.prompt:
        width, height = (found.width, found.height) if found.width else nearest_size(*size)
        return Recipe(
            exact=True, prompt=found.prompt, negative=found.negative, model_id=model_id,
            width=width, height=height, steps=found.steps, cfg=found.cfg,
            sampler=found.sampler, scheduler=found.scheduler, seed=found.seed,
            clip_skip=found.clip_skip,
            loras=[{"name": l.get("name"), "strength": l.get("strength", 1.0)} for l in found.loras],
            notes=["提詞和參數是從檔案裡讀出來的，不是猜的。用同一個底模、同一組 LoRA 和種子，"
                   "結果會非常接近（不同顯卡和版本仍可能有細微差異）。"])
    if guess is None:
        return Recipe(exact=False, prompt="", negative="", model_id=model_id,
                      width=nearest_size(*size)[0], height=nearest_size(*size)[1],
                      notes=["沒有看圖分析模型，只能給尺寸。到「模型」分頁下載一個看圖分析模型。"])
    prompt, negative = prompt_from(guess)
    width, height = nearest_size(*size)
    return Recipe(
        exact=False, prompt=prompt, negative=", ".join(negative), model_id=model_id,
        width=width, height=height,
        notes=["這張圖沒有夾帶參數，提詞是看圖猜的。內容會對，畫風不一定 —— "
               "下面「找相似的 LoRA」可以補畫風；要幾乎一模一樣，用「拿原圖當起點」。"])


# -- 1. exact: resolving what a file names -------------------------------------


def _version_public(raw: dict, how: str) -> dict:
    """A CivitAI model version as the page needs it, with its safety flags."""
    model = raw.get("model") or {}
    files = raw.get("files") or []
    primary = next((f for f in files if f.get("primary")), files[0] if files else {})
    model_id = raw.get("modelId") or model.get("id")
    return {
        "how": how,
        "model_id": model_id,
        "version_id": raw.get("id"),
        "name": model.get("name") or raw.get("name") or "",
        "version": raw.get("name") or "",
        "type": str(model.get("type") or "").lower(),
        "base_model": raw.get("baseModel") or "",
        "trained_words": list(raw.get("trainedWords") or [])[:12],
        "page": f"https://civitai.com/models/{model_id}?modelVersionId={raw.get('id')}" if model_id else "",
        "file": {"name": primary.get("name") or "", "url": primary.get("downloadUrl") or raw.get("downloadUrl") or "",
                 "size": int(float(primary.get("sizeKB") or 0) * 1024)},
        "poi": bool(model.get("poi")),
        "minor": bool(model.get("minor")),
        "nsfw": bool(model.get("nsfw")),
    }


def withheld(entry: dict) -> str:
    if entry.get("poi"):
        return "CivitAI 標記這是真人肖像模型，這個 app 不提供。"
    if entry.get("minor"):
        return "CivitAI 標記這個模型涉及未成年，這個 app 不提供。"
    return ""


async def resolve(found) -> list[dict]:
    """Every model and LoRA the file names, looked up on CivitAI.

    By version id (CivitAI's own generator), then by hash (A1111/Forge), then
    by file name (ComfyUI, or an A1111 image without hashes) - each result
    says which, because a name match can be the wrong model.
    """
    wanted: list[tuple[str, str, dict]] = []   # (kind, key, context)
    for res in getattr(found, "resources", None) or []:
        wanted.append(("version", str(res["version_id"]), res))
    if getattr(found, "model_hash", ""):
        wanted.append(("hash", found.model_hash, {"type": "checkpoint", "name": found.model}))
    elif getattr(found, "model", ""):
        wanted.append(("name", found.model, {"type": "checkpoint", "name": found.model}))
    for lora in getattr(found, "loras", None) or []:
        if lora.get("hash"):
            wanted.append(("hash", lora["hash"], {"type": "lora", **lora}))
        else:
            wanted.append(("name", str(lora.get("name") or ""), {"type": "lora", **lora}))

    async def one(kind: str, key: str, context: dict) -> dict:
        base = {"asked": context.get("name") or key, "strength": context.get("strength",
                context.get("weight")), "kind": context.get("type") or ""}
        try:
            if kind == "version":
                raw = await civitai.get_json(f"model-versions/{int(key)}")
                how = "版本編號（檔案裡寫的，精確）"
            elif kind == "hash":
                raw = await civitai.get_json(f"model-versions/by-hash/{key}")
                how = "檔案雜湊（精確）"
            else:
                stem = key.replace("\\", "/").rsplit("/", 1)[-1].rsplit(".", 1)[0]
                types = "Checkpoint" if context.get("type") == "checkpoint" else "LORA"
                data = await civitai.get_json("models", [("query", stem), ("types", types),
                                                         ("limit", "3")])
                items = (data or {}).get("items") or []
                raw = None
                if items and items[0].get("modelVersions"):
                    raw = dict(items[0]["modelVersions"][0])
                    raw["model"] = {k: items[0].get(k) for k in ("id", "name", "type", "nsfw", "poi", "minor")}
                    raw["modelId"] = items[0].get("id")
                how = "檔名搜尋（可能不是同一個，請看一下頁面）"
        except Exception as exc:  # noqa: BLE001 - one lookup failing is not the whole answer
            return {**base, "found": False, "error": str(exc)}
        if not raw:
            return {**base, "found": False,
                    "error": "CivitAI 上找不到（可能是私人模型、已下架，或需要 API key 才看得到）"}
        entry = {**base, "found": True, **_version_public(raw, how)}
        if reason := withheld(entry):
            # Reported, because the file did name it, but not linked.
            entry = {**base, "found": True, "withheld": reason, "how": how,
                     "name": entry["name"], "type": entry["type"]}
        return entry

    results = await asyncio.gather(*(one(*w) for w in wanted[:12]))
    return list(results)


# -- 3. candidates: LoRAs whose own pictures look like this one ----------------


def similarity(a, b) -> float:
    """Cosine of two tagger vectors, 0..1."""
    import numpy as np

    na, nb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
    if not na or not nb:
        return 0.0
    return max(0.0, min(1.0, float(np.dot(a, b) / (na * nb))))


def style_signature(picture):
    """How a picture is painted, independent of what it shows.

    A hue/saturation/value histogram (the palette), the mean and spread of
    saturation (pastel against vivid), and edge density (clean cel lines
    against soft washes). Cheap, and blind to content on purpose.
    """
    import numpy as np
    from PIL import ImageFilter

    small = picture.convert("RGB").resize((160, 160))
    hsv = np.asarray(small.convert("HSV"), dtype=np.float32) / 255.0
    hist, _ = np.histogramdd(hsv.reshape(-1, 3), bins=(12, 4, 4),
                             range=((0, 1), (0, 1), (0, 1)))
    hist = hist.ravel() / max(1.0, hist.sum())
    edges = np.asarray(small.convert("L").filter(ImageFilter.FIND_EDGES), dtype=np.float32) / 255.0
    stats = np.array([hsv[..., 1].mean(), hsv[..., 1].std(), hsv[..., 2].mean(),
                      hsv[..., 2].std(), edges.mean() * 4, (edges > 0.25).mean() * 4])
    return hist, np.clip(stats, 0, 1)


def style_similarity(a, b) -> float:
    """0..1: palette overlap blended with how close the painting statistics are."""
    import numpy as np

    (ha, sa), (hb, sb) = a, b
    palette = float(np.minimum(ha, hb).sum())
    stats = 1.0 - float(np.abs(sa - sb).mean()) * 2
    return max(0.0, min(1.0, 0.6 * palette + 0.4 * max(0.0, stats)))


def small_image_url(url: str, width: int = 448) -> str:
    """CivitAI's CDN resizes on request; a sample never needs its original."""
    return url.replace("/original=true/", f"/width={width}/") if "/original=true/" in url else url


async def search_candidates(guess: tags.Guess, model_id: str) -> list[dict]:
    """CivitAI LoRAs worth comparing, with real-person and minor flags removed."""
    bases = BASES.get(model_id, ["SDXL 1.0"])
    found: dict[int, dict] = {}
    for q in queries(guess):
        if q.get("tag"):
            params = [("types", "LORA"), ("tag", q["tag"]), ("sort", "Most Downloaded"),
                      ("limit", str(POOL)), ("nsfw", "true")]
        else:
            params = [("types", "LORA"), ("query", q["query"]), ("limit", str(PER_QUERY)),
                      ("nsfw", "true")]
        params += [("baseModels", b) for b in bases]
        try:
            data = await civitai.get_json("models", params) or {}
        except Exception:  # noqa: BLE001 - one search failing leaves the others
            continue
        for item in data.get("items") or []:
            if item.get("poi") or item.get("minor") or item.get("id") in found:
                continue
            versions = item.get("modelVersions") or []
            if not versions:
                continue
            version = versions[0]
            images = [i for i in (version.get("images") or [])
                      if i.get("url") and not i.get("poi") and not i.get("minor")
                      and str(i.get("type") or "image") == "image"]
            raw = dict(version)
            raw["model"] = {k: item.get(k) for k in ("id", "name", "type", "nsfw", "poi", "minor")}
            raw["modelId"] = item.get("id")
            entry = _version_public(raw, "搜尋")
            entry.update({
                "why": q["why"], "query_kind": q["kind"],
                "downloads": int(((item.get("stats") or {}).get("downloadCount")) or 0),
                "samples": [small_image_url(i["url"]) for i in images[:2]],
            })
            found[item["id"]] = entry
            if len(found) >= MAX_CANDIDATES:
                break
    return list(found.values())


async def fetch_image(url: str):
    """One sample picture, as a PIL image, or None."""
    import aiohttp
    from PIL import Image

    try:
        async with aiohttp.ClientSession(headers={"User-Agent": civitai.UA}) as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                if response.status != 200:
                    return None
                data = await response.read()
        if len(data) > 12_000_000:
            return None
        picture = Image.open(io.BytesIO(data))
        picture.load()
        return picture
    except Exception:  # noqa: BLE001 - a missing sample just scores nothing
        return None


async def rank(candidates: list[dict], target, embed, target_style=None) -> list[dict]:
    """Score each candidate by its closest sample picture, best first.

    `embed` turns a PIL image into a vector (tags.vector, bound to a tagger)
    and is run in a thread: it is CPU work, a second or two per picture.
    With `target_style` (style_signature of the picture) the score blends
    content and style; without it, content alone.
    """
    loop = asyncio.get_running_loop()
    sem = asyncio.Semaphore(6)

    async def get(url):
        async with sem:
            return await fetch_image(url)

    urls = [(i, url) for i, c in enumerate(candidates) for url in c.get("samples") or []]
    pictures = await asyncio.gather(*(get(url) for _, url in urls))
    best: dict[int, tuple[float, float, float]] = {}
    for (index, _url), picture in zip(urls, pictures):
        if picture is None:
            continue
        vec = await loop.run_in_executor(None, embed, picture)
        content = similarity(target, vec)
        style = (style_similarity(target_style, style_signature(picture))
                 if target_style is not None else content)
        score = CONTENT_WEIGHT * content + (1 - CONTENT_WEIGHT) * style
        if score > best.get(index, (-1.0, 0, 0))[0]:
            best[index] = (score, content, style)
    out = []
    for index, cand in enumerate(candidates):
        if index not in best:
            continue
        score, content, style = best[index]
        out.append({**cand, "score": round(score, 3),
                    "content": round(content, 3), "style": round(style, 3),
                    # A style LoRA is used lighter than a character one: it
                    # is meant to tint, and at full strength it overrides.
                    "strength": 0.6 if cand.get("query_kind") == "style" else 0.8})
    out.sort(key=lambda c: -c["score"])
    return out


# -- closing the loop -----------------------------------------------------------


def compare(original: tags.Guess, attempt: tags.Guess, score: float) -> dict:
    """How a generated attempt differs from the picture it was meant to copy."""
    a = {n for n, p in original.general if p >= 0.5 and n not in SKIP | TO_NEGATIVE}
    b = {n for n, p in attempt.general if p >= 0.5 and n not in SKIP | TO_NEGATIVE}
    missing = sorted(a - b, key=lambda n: -dict(original.general).get(n, 0))
    extra = sorted(b - a, key=lambda n: -dict(attempt.general).get(n, 0))
    return {
        "score": round(score, 3),
        "missing": [tags.to_prompt(n) for n in missing[:15]],
        "extra": [tags.to_prompt(n) for n in extra[:15]],
        "advice": ("已經很接近了。" if score >= 0.9 else
                   "把「少了」的標籤加進提詞、「多了」的放進負面提詞，再生一次。"),
    }

"""Which artists does this picture look like - and how alike are two styles?

Why this exists
---------------
An artist tag is the strongest style lever the anime checkpoints have, and the
hardest to find: there are tens of thousands of them, and nothing about a
picture says which ones would produce it. Two things were missing - a way to
get *from a picture to candidate tags*, and a way to say *how close a
generated picture's style is to the one wanted* that is better than comparing
colour palettes.

Kaloscope 3.0 (heathcliff01/Kaloscope3.0-preview) answers both. It is a DINOv3
fine-tune trained on 6.57 million Danbooru pictures, and gives two outputs:

* ``logits`` over 44,129 artists - "which Danbooru artist tags does this look
  like". The labels are Danbooru artist tags, which is the vocabulary NoobAI,
  Illustrious and NovelAI all use.
* ``style`` - a 256-number style vector. Two pictures in the same hand have a
  high cosine whatever they depict; the model card reports 83% top-1 artist
  retrieval *across different content*.

What was checked here (2026-11-25, CPU, onnxruntime 1.28)
---------------------------------------------------------
* The ONNX export used is Mooshie/kaloscope-web's (169MB). Its repository ships
  a reference probe - a synthetic input with the expected top-5 classes and
  style vector. This module's own run of it matched exactly (same top-5, style
  dot product 1.0). ``self_check`` repeats that on the user's machine.
* On real work fetched from Danbooru - ten general-rated pictures each by
  wlop, hiten_(hitenkei) and bkub:

  - **One picture** put the right artist first 70-86% of the time, with the
    occasional wild miss (one bkub picture ranked bkub 12,151st).
  - **Several pictures pooled** (mean of the probabilities, 200 random
    subsets): two pictures 92-100%, three or more 99-100%. Averaging the
    log-probabilities instead was no better, so the plain mean is used.
  - **Style vectors**: pictures by one artist average 0.60-0.64 cosine with
    each other; other artists 0.17. Against the *centroid* of several
    reference pictures a held-out picture by the same artist scores
    0.75-0.78 (worst case 0.56-0.61, against 0.46-0.51 for a single
    reference) and other artists 0.21 - a wider, steadier gap, which is why
    a folder of references makes a better target than one picture.
  - **Mixed folders show**: wlop and bkub together average 0.38 pairwise;
    one bkub among nine hiten sat at 0.42 to the centroid while the nine
    were 0.69-0.90. Over 300 random folders per size, a single intruder
    was flagged 83% of the time among four pictures and 99-100% among five
    or more; a clean folder had a picture flagged 0-4% of the time. So the
    flag is a suggestion with the thumbnail next to it, never an automatic
    removal.

What it is not
--------------
The scores are an uncalibrated softmax with no "none of these" class, so a
picture by nobody in the list still gets a top answer - a low, flat score
means "no clear match", and the page says so. It recognises drawing styles;
it has nothing to do with recognising people.

Licence: the 3.0 model is a DINOv3 fine-tune under the DINOv3 License.
"""

from __future__ import annotations

import json
from pathlib import Path

import artists
from registry import ModelFile

REPO = "Mooshie/kaloscope-web"
FOLDER = "taggers/kaloscope3"
MODEL = ModelFile(REPO, "kaloscope3_v1_artist_web.onnx", FOLDER, 169079820)
LABELS = ModelFile(REPO, "labels_v3.json", FOLDER, 634396)
PROBE = ModelFile(REPO, "probe_ref.json", FOLDER, 2517)
FILES = (MODEL, LABELS, PROBE)
SIZE = 512
MEAN = (0.485, 0.456, 0.406)
STD = (0.229, 0.224, 0.225)
LICENCE = "DINOv3 License（Kaloscope 3.0 是 DINOv3 的微調）"

# The three artists this project does not steer towards (see artists.py): they
# are never offered as a match either.
WITHHELD = {"kedama_milk", "toraishi_666", "todoroki_masaru", "sho_(sho_lwlw)"}

_cache: dict[str, tuple] = {}


def folder(models_dir: Path) -> Path:
    return models_dir / FOLDER


def installed(models_dir: Path) -> bool:
    base = folder(models_dir)
    return (base / MODEL.name).is_file() and (base / LABELS.name).is_file()


def _load(base: Path) -> tuple:
    key = str(base)
    if key not in _cache:
        import onnxruntime as ort   # lazy: a large optional dependency

        session = ort.InferenceSession(str(base / MODEL.name), providers=["CPUExecutionProvider"])
        labels = json.loads((base / LABELS.name).read_text(encoding="utf-8"))
        _cache[key] = (session, labels)
    return _cache[key]


def labels(models_dir: Path) -> list[str]:
    """Every artist tag the model knows, for spell-checking a pasted list."""
    try:
        return json.loads((folder(models_dir) / LABELS.name).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []


def preprocess(image):
    """Exactly the reference Space's steps: transparency onto white, short side
    to 512 (bicubic), centre crop 512, ImageNet mean/std, channels first."""
    import numpy as np
    from PIL import Image

    rgba = image.convert("RGBA")
    flat = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    flat.alpha_composite(rgba)
    picture = flat.convert("RGB")
    width, height = picture.size
    scale = SIZE / min(width, height)
    new_w = SIZE if width <= height else int(width * scale)
    new_h = SIZE if height <= width else int(height * scale)
    picture = picture.resize((new_w, new_h), Image.BICUBIC)
    left, top = round((new_w - SIZE) / 2), round((new_h - SIZE) / 2)
    picture = picture.crop((left, top, left + SIZE, top + SIZE))
    array = (np.asarray(picture, dtype=np.float32) / 255.0 - np.array(MEAN, dtype=np.float32)) \
        / np.array(STD, dtype=np.float32)
    return array.transpose(2, 0, 1)[None]


def _run(tensor, base: Path):
    session, names = _load(base)
    logits, style = session.run(["logits", "style"], {"pixel_values": tensor})
    return logits[0], style[0], names


def infer(image, base: Path) -> tuple:
    """One picture: (probability per artist, style vector, the artist names)."""
    import numpy as np

    logits, vector, names = _run(preprocess(image), base)
    shifted = logits - logits.max()
    probs = np.exp(shifted) / np.exp(shifted).sum()
    return probs, vector, names


def ranked(probs, names: list[str], top: int) -> list[dict]:
    """The likeliest artists for a row of probabilities, withheld ones left out."""
    import numpy as np

    out = []
    for index in np.argsort(-probs):
        tag = names[int(index)]
        if tag in WITHHELD:
            continue
        known = artists.BY_TAG.get(tag)
        out.append({"tag": tag, "p": round(float(probs[index]), 4),
                    "zh": known.zh if known else "", "posts": known.posts if known else 0})
        if len(out) >= top:
            break
    return out


def analyse(image, base: Path, top: int = 30) -> tuple[list[dict], "object"]:
    """The most likely artists (tag, probability) and the style vector."""
    probs, vector, names = infer(image, base)
    return ranked(probs, names, top), vector


# Measured on real folders (see the module docstring): one artist's pictures
# average about 0.6 with each other, two artists mixed about 0.37.
MIXED_BELOW = 0.45
# ...and a stray picture sits far under the folder's median likeness to the
# centroid (0.42 against a median of 0.81; the lowest genuine one was 0.16 under).
OUTLIER_GAP = 0.22
MAX_REFERENCES = 60


def pool(probs_list: list, vectors: list, names: list[str], top: int = 30) -> dict:
    """Several pictures said to share one style, read as one.

    Each picture carries its own subject, pose and palette along with the
    style; averaged over a folder those cancel and the style is what is
    left. So the artist ranking is the mean of the per-picture
    probabilities, and the target for scoring is the centroid of the style
    vectors. The pictures are also checked against each other, because "they
    are all one style" is the user's claim, and one wrong picture in the
    folder pulls the centroid towards nowhere.
    """
    import numpy as np

    probs = np.mean(np.stack(probs_list), axis=0)
    stack = np.stack(vectors).astype(np.float32)
    centroid = stack.mean(axis=0)
    norm = float(np.linalg.norm(centroid))
    centroid = centroid / norm if norm else centroid
    each = [round(float(v), 3) for v in stack @ centroid]
    count = len(vectors)
    pairwise = None
    if count >= 2:
        gram = stack @ stack.T
        pairwise = round(float((gram.sum() - np.trace(gram)) / (count * (count - 1))), 3)
    median = float(np.median(each)) if each else 0.0
    outliers = [i for i, value in enumerate(each)
                if count >= 4 and value < median - OUTLIER_GAP]
    firsts = [ranked(p, names, 1)[0]["tag"] for p in probs_list]
    return {"matches": ranked(probs, names, top), "style": centroid, "each": each,
            "pairwise": pairwise, "outliers": outliers, "firsts": firsts, "count": count}


def analyse_many(images: list, base: Path, top: int = 30) -> dict:
    results = [infer(image, base) for image in images]
    return pool([r[0] for r in results], [r[1] for r in results], results[0][2], top)


def consistency(pooled: dict) -> str:
    """Whether the folder really is one style, in a sentence."""
    count, pairwise, outliers = pooled["count"], pooled["pairwise"], pooled["outliers"]
    if count < 2 or pairwise is None:
        return "只有一張圖。同畫風的圖多放幾張會準很多：三張以上，認對畫師的機率從七八成變成幾乎百分之百。"
    if outliers:
        return (f"{count} 張裡有 {len(outliers)} 張跟其他的畫風差很多（下面標出來了）。"
                "拿掉它們再判斷一次會更準。")
    if pairwise < MIXED_BELOW:
        return (f"這 {count} 張彼此不太像（一致度 {pairwise:.2f}；同一位畫師通常約 0.6）—— "
                "看起來不只一種畫風。分開成不同資料夾各自判斷，結果才有意義。")
    return f"這 {count} 張畫風一致（一致度 {pairwise:.2f}），已經合併成一個目標，比單張可靠。"


def sample(items: list, limit: int = MAX_REFERENCES) -> list:
    """At most `limit` of them, spread evenly through the list.

    A folder sorted by name is usually sorted by date too, so the first sixty
    would be one period of an artist's work; every n-th is all of it.
    """
    if len(items) <= limit:
        return list(items)
    step = len(items) / limit
    return [items[int(i * step)] for i in range(limit)]


def write_target(path: Path, vector, names: list[str]) -> None:
    """A pooled style, kept as the thing a lab scores against."""
    path.write_text(json.dumps({"style": [round(float(v), 6) for v in vector],
                                "count": len(names), "names": names[:MAX_REFERENCES]},
                               ensure_ascii=False), encoding="utf-8")


def read_target(path: Path):
    """The style vector `write_target` stored, or None if the file is not one."""
    import numpy as np

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        vector = np.asarray(data["style"], dtype=np.float32)
    except (OSError, ValueError, KeyError, TypeError):
        return None
    if vector.ndim != 1 or not vector.size or not np.isfinite(vector).all():
        return None
    norm = float(np.linalg.norm(vector))
    return vector / norm if norm else None


def style(image, base: Path):
    """Just the 256-number style vector (already unit length)."""
    return _run(preprocess(image), base)[1]


def similarity(a, b) -> float:
    """How alike two styles are, 0..1. Unrelated artists land near 0.2."""
    import numpy as np

    return max(0.0, min(1.0, float(np.dot(a, b))))


def confidence(matches: list[dict]) -> str:
    """One honest line about how much the top answer means."""
    top = matches[0]["p"] if matches else 0.0
    if top >= 0.5:
        return "很明確：畫風高度符合第一名。"
    if top >= 0.1:
        return "有方向：前幾名都值得試，通常要混兩三位才像。"
    return ("沒有明確符合的單一畫師（分數又低又平）。這張圖可能是多位畫師混出來的、LoRA 畫的，"
            "或不是這個模型認得的畫風 —— 把前面一批都丟進實驗室試，比相信第一名有用。")


def self_check(base: Path) -> dict:
    """Run the export's own reference probe on this machine."""
    import numpy as np

    try:
        ref = json.loads((base / PROBE.name).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"ok": None, "detail": "沒有參考檔，無法自我檢查"}
    c = np.arange(3, dtype=np.float32)[:, None, None]
    h = np.arange(SIZE, dtype=np.float32)[None, :, None]
    w = np.arange(SIZE, dtype=np.float32)[None, None, :]
    probe = (np.sin((c + 1) * 0.01 * h) * np.cos(0.013 * w) * 1.5).astype(np.float32)[None]
    logits, vector, _names = _run(probe, base)
    top = int(np.argmax(logits))
    dot = float(np.dot(vector, np.array(ref["v3_style"], dtype=np.float32)))
    ok = top == int(ref["v3_top5"][0]) and dot > 0.98
    return {"ok": ok, "detail": f"第一名類別 {top}（應為 {ref['v3_top5'][0]}），畫風向量吻合度 {dot:.3f}"}

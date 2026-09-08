"""Run a ComfyUI workflow the user exported, instead of one this app guessed.

Why this exists
---------------
Several catalogued models - LTX-2.3/2.5, Wan S2V, Wan Animate, MiniMax H3 -
are marked ``files_only``: the app downloads their weights but cannot generate
with them, because their official pipelines are large graphs and this project
has no GPU to check a reconstruction against. Shipping a guessed graph behind a
button would be an unverified claim wearing a feature.

An imported workflow removes the guess. The user exports **Save (API Format)**
from their own ComfyUI, where that graph demonstrably runs, and this app fills
in the image, the prompt and the seed. The graph is theirs and it already
worked; only the substitution is ours.

The format is the same shape this app already builds - ``{node_id: {class_type,
inputs, _meta}}`` - so the runner submits it unchanged.

How the slots are found
-----------------------
Mostly structurally, not by guessing at names:

* the positive and negative prompts are found by following the ``positive`` and
  ``negative`` **input names** of whatever consumes them, back to the text node
  that feeds them. A graph says which is which; we do not have to infer it from
  the words.
* the image is a ``LoadImage``-style node.
* seeds are any widget literally called ``seed`` or ``noise_seed`` - there can
  be several, and all of them get set, because a two-pass sampler with one seed
  changed and one not is a confusing half-random result.

Whatever cannot be found structurally is reported as missing rather than
guessed, and the UI asks. A wrong guess here produces a graph that runs and
ignores the prompt, which is worse than an error.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass, field

# Node classes that take the input picture, in the graphs people actually export.
IMAGE_NODES = ("LoadImage", "LoadImageMask", "LoadImageOutput", "ETN_LoadImageBase64")
# Node classes that write the result. Videos and stills both land here.
OUTPUT_NODES = ("SaveImage", "SaveAnimatedWEBP", "SaveAnimatedPNG", "SaveVideo",
                "VHS_VideoCombine", "SaveWEBM", "PreviewImage", "SaveAudio")
# Widgets that are a seed by any name.
SEED_KEYS = ("seed", "noise_seed")
# Text widgets, in the order they are usually named.
TEXT_KEYS = ("text", "prompt", "string", "value")

MAX_NODES = 400
MAX_BYTES = 2_000_000
# One widget holding a quarter-megabyte of text is not a prompt; it is either a
# mistake or something trying to be expensive to process.
MAX_STRING = 256_000
# Graphs are shallow in practice. The visited set already stops cycles; this
# stops a pathological chain from being walked forever.
MAX_DEPTH = 200


class ImportError_(ValueError):
    """Something about the file means it cannot be used."""


@dataclass
class Slot:
    """One place a value gets substituted before the graph is submitted."""

    node: str
    key: str
    class_type: str
    title: str = ""

    def public(self) -> dict:
        return {"node": self.node, "key": self.key,
                "class_type": self.class_type, "title": self.title}


@dataclass
class Detected:
    image: Slot | None = None
    positive: Slot | None = None
    negative: Slot | None = None
    seeds: list[Slot] = field(default_factory=list)
    width: Slot | None = None
    height: Slot | None = None
    outputs: list[str] = field(default_factory=list)
    nodes: list[dict] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def missing(self) -> list[str]:
        """What could not be found. Reported, never guessed around."""
        out = []
        if not self.positive:
            out.append("positive")
        if not self.outputs:
            out.append("output")
        return out

    @property
    def usable(self) -> bool:
        """Enough to run: somewhere to put a prompt, and something that saves.

        An image slot is *not* required - a text-to-video workflow is a
        legitimate thing to import, it just cannot be driven from a keyframe.
        """
        return not self.missing

    def public(self) -> dict:
        return {
            "image": self.image.public() if self.image else None,
            "positive": self.positive.public() if self.positive else None,
            "negative": self.negative.public() if self.negative else None,
            "seeds": [s.public() for s in self.seeds],
            "width": self.width.public() if self.width else None,
            "height": self.height.public() if self.height else None,
            "outputs": self.outputs,
            "nodes": self.nodes,
            "missing": self.missing,
            "usable": self.usable,
            "needs_image": self.image is not None,
            "notes": self.notes,
        }


def parse(text: str | bytes) -> dict:
    """Read an exported workflow, and say plainly when it is the wrong export.

    The UI export and the API export look similar enough that people send the
    wrong one constantly. The UI format has a top-level ``nodes`` *list*; the
    API format is a mapping of node id to node. Telling them apart is easy, and
    saying which one arrived saves the user from guessing.
    """
    raw = text.decode("utf-8", "replace") if isinstance(text, bytes) else text
    if len(raw) > MAX_BYTES:
        raise ImportError_(f"這個檔案太大（{len(raw)/1e6:.1f}MB）。工作流不該這麼大。")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ImportError_(f"這不是有效的 JSON（第 {exc.lineno} 行）。") from exc
    if not isinstance(data, dict):
        raise ImportError_("這個 JSON 最外層不是物件，不像 ComfyUI 的工作流。")
    if isinstance(data.get("nodes"), list):
        raise ImportError_(
            "這是 ComfyUI 的**畫布格式**，不是 API 格式。"
            "在 ComfyUI 裡要選 Workflow → Export (API) —— "
            "存出來的檔案最外層是節點編號，不是 nodes 清單。")
    if not data:
        raise ImportError_("這個工作流是空的。")
    if len(data) > MAX_NODES:
        raise ImportError_(f"這個工作流有 {len(data)} 個節點，超過上限 {MAX_NODES}。")
    for node_id, node in data.items():
        if not isinstance(node, dict) or "class_type" not in node:
            raise ImportError_(
                f"節點 {node_id} 沒有 class_type，這不像 API 格式的工作流。"
                "在 ComfyUI 裡要選 Workflow → Export (API)。")
        if not isinstance(node.get("inputs", {}), dict):
            raise ImportError_(f"節點 {node_id} 的 inputs 格式不對。")
        for key, value in (node.get("inputs") or {}).items():
            if isinstance(value, str) and len(value) > MAX_STRING:
                raise ImportError_(
                    f"節點 {node_id} 的 {key} 有 {len(value)//1000}KB 的文字，"
                    "這不像提詞。")
    return data


def _title(node: dict) -> str:
    return str((node.get("_meta") or {}).get("title") or node.get("class_type") or "")


def _trace_text(graph: dict, ref, seen: set[str] | None = None,
                depth: int = 0) -> Slot | None:
    """Follow a link back to the text widget that ultimately feeds it.

    A prompt is rarely wired straight into the sampler: it goes through the
    encoder, and often through conditioning nodes on the way. Following the
    link is what makes this structural rather than a guess about which
    CLIPTextEncode "looks positive".
    """
    if not (isinstance(ref, list) and ref and isinstance(ref[0], (str, int))):
        return None
    seen = seen if seen is not None else set()
    if depth > MAX_DEPTH:
        return None
    node_id = str(ref[0])
    if node_id in seen or node_id not in graph:
        return None
    seen.add(node_id)
    node = graph[node_id]
    inputs = node.get("inputs") or {}
    for key in TEXT_KEYS:
        if isinstance(inputs.get(key), str):
            return Slot(node_id, key, node.get("class_type", ""), _title(node))
    # Not a text node itself: walk its own inputs, nearest first.
    for value in inputs.values():
        found = _trace_text(graph, value, seen, depth + 1)
        if found:
            return found
    return None


def detect(graph: dict) -> Detected:
    """Find where the image, prompts, seed and size go."""
    out = Detected()
    out.nodes = [{"id": nid, "class_type": n.get("class_type", ""), "title": _title(n)}
                 for nid, n in graph.items()]

    for node_id, node in graph.items():
        cls = node.get("class_type", "")
        inputs = node.get("inputs") or {}

        if cls in IMAGE_NODES and out.image is None:
            key = "image" if "image" in inputs else next(
                (k for k, v in inputs.items() if isinstance(v, str)), "")
            if key:
                out.image = Slot(node_id, key, cls, _title(node))

        if cls in OUTPUT_NODES:
            out.outputs.append(node_id)

        for key in SEED_KEYS:
            if isinstance(inputs.get(key), (int, float)):
                out.seeds.append(Slot(node_id, key, cls, _title(node)))

        # Size, taken from whatever declares it rather than from a node name.
        for key, target in (("width", "width"), ("height", "height")):
            if isinstance(inputs.get(key), int) and getattr(out, target) is None:
                setattr(out, target, Slot(node_id, key, cls, _title(node)))

        # The one that matters: a consumer names its conditioning inputs, so the
        # graph itself says which text is positive and which is negative.
        if out.positive is None and isinstance(inputs.get("positive"), list):
            out.positive = _trace_text(graph, inputs["positive"])
        if out.negative is None and isinstance(inputs.get("negative"), list):
            out.negative = _trace_text(graph, inputs["negative"])

    # Fallback for graphs with no positive/negative naming at all (some
    # single-conditioning pipelines). One text node is unambiguous; more than
    # one is not, and is left for the user rather than picked by coin toss.
    if out.positive is None:
        texts = [Slot(nid, key, n.get("class_type", ""), _title(n))
                 for nid, n in graph.items()
                 for key in TEXT_KEYS
                 if isinstance((n.get("inputs") or {}).get(key), str)]
        if len(texts) == 1:
            out.positive = texts[0]
            out.notes.append("這個工作流只有一個文字欄位，所以直接當成提詞。")
        elif texts:
            out.notes.append(
                f"這個工作流有 {len(texts)} 個文字欄位，而且沒有標明哪個是正面提詞 —— "
                "要自己選一個。")

    if out.image is None:
        out.notes.append("這個工作流沒有輸入圖片的節點，所以它是文生影片／文生圖，"
                         "不能拿短劇的關鍵幀去驅動。")
    if len(out.seeds) > 1:
        out.notes.append(f"有 {len(out.seeds)} 個 seed 欄位，會一起設成同一個值 —— "
                         "只改其中一個會得到半隨機的結果。")
    return out


def apply(graph: dict, detected: Detected, *, image: str = "", prompt: str = "",
          negative: str | None = None, seed: int | None = None,
          width: int | None = None, height: int | None = None,
          prefix: str = "") -> dict:
    """Return a copy of the graph with this job's values substituted in.

    A copy, always: the stored workflow is the user's, and mutating it would
    mean the second generation inherits the first one's prompt.

    `prefix` is not optional in spirit. An imported graph carries whatever
    output path it was exported with - which can be absolute, can contain
    "..", and can be a fixed name that overwrites the previous run. The app
    decides where its own jobs land, so every writing node gets the caller's
    prefix and nothing else.
    """
    out = copy.deepcopy(graph)

    def put(slot: Slot | None, value) -> None:
        if slot is None or value is None:
            return
        node = out.get(slot.node)
        if node and isinstance(node.get("inputs"), dict):
            node["inputs"][slot.key] = value

    put(detected.image, image or None)
    put(detected.positive, prompt or None)
    if negative is not None:
        put(detected.negative, negative)
    for slot in detected.seeds:
        put(slot, seed)
    put(detected.width, width)
    put(detected.height, height)

    if prefix:
        keep = set(detected.outputs)
        for node_id, node in out.items():
            inputs = node.get("inputs")
            if not isinstance(inputs, dict) or "filename_prefix" not in inputs:
                continue
            if node_id in keep:
                inputs["filename_prefix"] = prefix
            else:
                # A second save branch would still write to disk even though
                # only one result is collected. Point it at the same place
                # rather than letting it choose - it cannot then escape the
                # output folder or overwrite something older.
                inputs["filename_prefix"] = f"{prefix}_extra"
    return out


def summary(detected: Detected, graph_titles: dict | None = None) -> list[dict]:
    """The detection, in words a first-time user can check.

    Deliberately phrased as "your X goes into Y", because what the user has to
    verify is the mapping, not the graph.
    """
    rows = []
    graph_titles = graph_titles or {n["id"]: (n.get("title") or n.get("class_type"))
                                    for n in detected.nodes}

    def row(label: str, slot: Slot | None, missing: str) -> None:
        # The title leads and the node id is small print. "第 17 號節點" is not
        # useful information to a first-time user; the node's own name is the
        # thing they can recognise in ComfyUI.
        rows.append({
            "label": label,
            "found": slot is not None,
            "where": (slot.title or slot.class_type) if slot else "",
            "node": (f"{slot.class_type} · 節點 {slot.node}" if slot else ""),
            "detail": missing if slot is None else "",
        })

    row("你的圖片會放進", detected.image, "這個工作流沒有輸入圖的節點")
    row("你打的提詞會進", detected.positive, "找不到提詞欄位 —— 要自己選一個")
    row("負面提詞會進", detected.negative, "沒有負面提詞欄位，會略過")
    rows.append({
        "label": "隨機種子會設在",
        "found": bool(detected.seeds),
        "where": ("、".join(s.title or s.class_type for s in detected.seeds[:3])
                  + (f" 等 {len(detected.seeds)} 處" if len(detected.seeds) > 3 else "")),
        "node": "、".join(f"節點 {s.node}" for s in detected.seeds[:4]),
        "detail": "" if detected.seeds else "找不到 seed 欄位，每次結果會一樣",
    })
    rows.append({
        "label": "成品會由這裡存出",
        "found": bool(detected.outputs),
        "where": "、".join(
            (graph_titles.get(n) or n) for n in detected.outputs[:3]) if graph_titles else "",
        "node": "、".join(f"節點 {n}" for n in detected.outputs[:4]),
        "detail": "" if detected.outputs else "找不到儲存節點，跑完不會有檔案",
    })
    return rows


# -- storage ------------------------------------------------------------------
# One JSON per model id. Small, human-readable, and trivially removable: the
# user can delete a file to forget a workflow without the app needing an
# "uninstall" path for it.

def _path(root, model_id: str):
    from pathlib import Path
    import re

    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", model_id).strip("._") or "unnamed"
    return Path(root) / f"{safe}.json"


def save(root, model_id: str, graph: dict, detected: Detected, *,
         source: str = "") -> dict:
    """Store a workflow against the model it drives."""
    from pathlib import Path

    Path(root).mkdir(parents=True, exist_ok=True)
    record = {
        "model_id": model_id,
        "source": source,
        "nodes": len(graph),
        "graph": graph,
        "slots": detected.public(),
    }
    _path(root, model_id).write_text(
        json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    return record


def load(root, model_id: str) -> dict | None:
    path = _path(root, model_id)
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def remove(root, model_id: str) -> bool:
    path = _path(root, model_id)
    if not path.is_file():
        return False
    path.unlink()
    return True


def installed(root) -> dict[str, dict]:
    """Which models have an imported workflow, and how big each one is."""
    from pathlib import Path

    out: dict[str, dict] = {}
    folder = Path(root)
    if not folder.is_dir():
        return out
    for path in sorted(folder.glob("*.json")):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        model_id = str(raw.get("model_id") or "")
        if model_id:
            out[model_id] = {"model_id": model_id, "nodes": raw.get("nodes", 0),
                             "source": raw.get("source", ""),
                             "slots": raw.get("slots") or {}}
    return out


def slots_from(raw: dict) -> Detected:
    """Rebuild the Detected record from what was stored."""
    def slot(value):
        if not isinstance(value, dict):
            return None
        return Slot(str(value.get("node") or ""), str(value.get("key") or ""),
                    str(value.get("class_type") or ""), str(value.get("title") or ""))

    stored = raw.get("slots") or {}
    got = Detected(
        image=slot(stored.get("image")),
        positive=slot(stored.get("positive")),
        negative=slot(stored.get("negative")),
        seeds=[s for s in (slot(x) for x in (stored.get("seeds") or [])) if s],
        width=slot(stored.get("width")),
        height=slot(stored.get("height")),
        outputs=[str(x) for x in (stored.get("outputs") or [])],
    )
    return got

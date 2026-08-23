"""Fixed-seed parameter sweeps: turn "I think 0.45 is right" into a measurement.

Everything this project says about *quality* is currently a guess. Not because
the reasoning is bad, but because the reasoning is all it has: no image has been
generated, so "denoise 0.4-0.6", "LoRA strength 0.8", "weight 1.2 for a thin
tag" are hypotheses wearing the clothes of settings. An outside review put it
bluntly - before a benchmark exists, adding more prompt rules has low marginal
value - and it was right.

So this builds the smallest thing that converts a hypothesis into a result:

    pick what to vary  ->  run every combination on the SAME seeds
    ->  look at them side by side  ->  score them blind  ->  read off a winner

Three design choices carry the whole thing:

**The same seeds across every variant.** A sweep where each variant gets a fresh
seed measures nothing: seed-to-seed variation in diffusion is larger than most
of the effects being looked for. Every variant runs the identical seed list, so
a difference between two variants is the parameter and not the dice.

**Provenance, recorded, not remembered.** Which checkpoint, which LoRA, which
ComfyUI - by content hash, not by filename, because filenames get reused. A
result you cannot attribute to an exact configuration is a result you cannot act
on three weeks later.

**Blind scoring, and two separate scores.** "Which is prettier" and "which is
more Suisei" are different questions, and a single aesthetic score optimises the
wrong one. So each pair is judged on a named axis, with the configuration hidden
until the vote is in.

Nothing here generates anything by itself - it expands a matrix and hands the
jobs to the normal image pipeline, so a sweep is exactly the generation you
would have run by hand, N times, without the bookkeeping mistakes.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import random
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

# A sweep is easy to make enormous by accident: four axes of four values each is
# 256 runs before seeds multiply it. The cap is a guardrail, not an opinion.
MAX_JOBS = 400
MAX_SEEDS = 16

# The axes worth sweeping, and what each one actually changes. Anything not
# listed here can still be set - it just stays fixed for the whole experiment.
AXES: dict[str, dict] = {
    "model": {"label": "底模", "kind": "choice",
              "why": "不同 checkpoint 對同一段提詞的反應差很多"},
    "lora_strength": {"label": "LoRA 強度", "kind": "number", "min": 0.0, "max": 1.4,
                      "why": "角色像不像跟畫面自由度的取捨，作者範例值不一定最好"},
    "denoise": {"label": "重繪強度", "kind": "number", "min": 0.1, "max": 1.0,
                "why": "只有放了來源圖才有意義。太低等於複製，太高等於沒放"},
    "cfg": {"label": "CFG", "kind": "number", "min": 1.0, "max": 12.0,
            "why": "提詞的服從度；太高會過曝、線條變硬"},
    "steps": {"label": "步數", "kind": "number", "min": 8, "max": 60,
              "why": "多數 checkpoint 過了某個點就不再變好，只是變慢"},
    "likeness": {"label": "官方風格偏移", "kind": "number", "min": 0.0, "max": 1.5,
                 "why": "服裝 tag 的加權；0 表示關掉"},
    "artist_weight": {"label": "畫師權重", "kind": "number", "min": 0.0, "max": 1.6,
                      "why": "0 表示不掛畫師"},
    "sampler": {"label": "Sampler", "kind": "choice",
                "why": "同 seed 換 sampler 是完全不同的圖，不是微調"},
}

# What a pair can be judged on. Kept separate on purpose: a picture can be the
# prettier one and the less accurate one at the same time, and collapsing that
# into a single score optimises for the wrong thing.
CRITERIA: dict[str, str] = {
    "likeness": "比較像本人（身份、髮色、瞳色、髮型）",
    "costume": "服裝比較對（配件、顏色、細節）",
    "anatomy": "手腳／身體比較沒壞",
    "adherence": "比較符合提詞",
    "beauty": "單純比較好看",
}


@dataclass
class Variant:
    """One cell of the matrix: the axis values, and the jobs they produced."""

    id: str
    values: dict = field(default_factory=dict)
    jobs: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        if not self.values:
            return "baseline"
        return " · ".join(f"{AXES.get(k, {}).get('label', k)}={_fmt(v)}"
                          for k, v in self.values.items())

    def public(self) -> dict:
        return {"id": self.id, "values": self.values, "jobs": list(self.jobs),
                "label": self.label}


@dataclass
class Vote:
    criterion: str
    winner: str            # variant id, or "" for "no difference"
    loser: str
    seed: int = 0
    at: float = field(default_factory=time.time)


@dataclass
class Experiment:
    id: str
    name: str = ""
    base: dict = field(default_factory=dict)     # settings held fixed
    axes: dict = field(default_factory=dict)     # axis -> list of values
    seeds: list[int] = field(default_factory=list)
    variants: list[Variant] = field(default_factory=list)
    provenance: dict = field(default_factory=dict)
    votes: list[Vote] = field(default_factory=list)
    created: float = field(default_factory=time.time)
    note: str = ""

    @property
    def job_count(self) -> int:
        return sum(len(v.jobs) for v in self.variants)

    def variant(self, variant_id: str) -> Variant | None:
        return next((v for v in self.variants if v.id == variant_id), None)

    def public(self) -> dict:
        return {
            "id": self.id, "name": self.name, "base": self.base, "axes": self.axes,
            "seeds": list(self.seeds), "created": self.created, "note": self.note,
            "variants": [v.public() for v in self.variants],
            "provenance": self.provenance,
            "votes": [asdict(v) for v in self.votes],
            "job_count": self.job_count,
            "standings": self.standings(),
        }

    # -- scoring -------------------------------------------------------------

    def standings(self) -> dict:
        """Win counts per variant per criterion, plus a simple win rate.

        Deliberately simple arithmetic rather than an Elo or Bradley-Terry fit:
        with a few dozen votes those models mostly express their own priors, and
        a number the user cannot recompute by hand is a number they cannot
        argue with. Wins, losses and ties, shown as they are.
        """
        out: dict[str, dict] = {}
        for criterion in CRITERIA:
            table: dict[str, dict] = {
                v.id: {"win": 0, "loss": 0, "tie": 0} for v in self.variants
            }
            for vote in self.votes:
                if vote.criterion != criterion:
                    continue
                if not vote.winner:
                    for side in (vote.loser,):
                        if side in table:
                            table[side]["tie"] += 1
                    continue
                if vote.winner in table:
                    table[vote.winner]["win"] += 1
                if vote.loser in table:
                    table[vote.loser]["loss"] += 1
            for row in table.values():
                played = row["win"] + row["loss"] + row["tie"]
                row["played"] = played
                row["rate"] = round(row["win"] / played, 3) if played else 0.0
            out[criterion] = table
        return out


def _fmt(value) -> str:
    if isinstance(value, float):
        return f"{value:g}"
    return str(value)


# -- building the matrix -----------------------------------------------------


def make_seeds(count: int, rng: random.Random | None = None) -> list[int]:
    """Seeds shared by every variant. Random, but fixed once for the run."""
    rng = rng or random
    count = max(1, min(int(count), MAX_SEEDS))
    return [rng.randint(0, 2**31 - 1) for _ in range(count)]


def expand(axes: dict, seeds: list[int]) -> tuple[list[Variant], str]:
    """Cartesian product of the axes -> variants. Returns (variants, warning)."""
    clean = {k: list(dict.fromkeys(v)) for k, v in axes.items()
             if k in AXES and isinstance(v, list) and v}
    if not clean:
        return [Variant(id="v0")], ""
    keys = list(clean)
    combos = list(itertools.product(*(clean[k] for k in keys)))
    total = len(combos) * max(1, len(seeds))
    warning = ""
    if total > MAX_JOBS:
        keep = max(1, MAX_JOBS // max(1, len(seeds)))
        warning = (f"這樣會產生 {total} 張圖，超過上限 {MAX_JOBS} —— "
                   f"只保留前 {keep} 組。減少軸或值的數量比較好。")
        combos = combos[:keep]
    return [Variant(id=f"v{i}", values=dict(zip(keys, combo)))
            for i, combo in enumerate(combos)], warning


def settings_for(base: dict, variant: Variant, seed: int) -> dict:
    """One concrete generation request: the fixed base plus this cell."""
    out = dict(base)
    out.update(variant.values)
    out["seed"] = seed
    return out


# -- provenance --------------------------------------------------------------

_HASH_CACHE: dict[str, str] = {}


def file_hash(path: Path) -> str:
    """SHA256, cached on (path, size, mtime).

    A checkpoint is 7GB and hashing it takes real time, so the cache matters -
    but the key includes size and mtime, because the failure this is guarding
    against is exactly a filename being reused for different weights.
    """
    try:
        stat = path.stat()
    except OSError:
        return ""
    key = f"{path}:{stat.st_size}:{int(stat.st_mtime)}"
    if key in _HASH_CACHE:
        return _HASH_CACHE[key]
    digest = hashlib.sha256()
    try:
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(4 * 1024 * 1024), b""):
                digest.update(chunk)
    except OSError:
        return ""
    _HASH_CACHE[key] = digest.hexdigest()
    return _HASH_CACHE[key]


def provenance(*, checkpoints: dict[str, Path], loras: dict[str, Path],
               comfy_commit: str = "", extra: dict | None = None) -> dict:
    """Everything needed to reproduce a run, by content rather than by name."""
    return {
        "at": time.time(),
        "checkpoints": {name: file_hash(p) for name, p in checkpoints.items()},
        "loras": {name: file_hash(p) for name, p in loras.items()},
        "comfy_commit": comfy_commit,
        **(extra or {}),
    }


# -- the store ---------------------------------------------------------------


class ExperimentStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.items: dict[str, Experiment] = {}

    def load(self) -> None:
        self.items = {}
        if not self.path.is_file():
            return
        for line in self.path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
                exp = Experiment(
                    id=raw["id"], name=raw.get("name", ""), base=raw.get("base", {}),
                    axes=raw.get("axes", {}), seeds=raw.get("seeds", []),
                    provenance=raw.get("provenance", {}),
                    created=raw.get("created", time.time()), note=raw.get("note", ""),
                    variants=[Variant(id=v["id"], values=v.get("values", {}),
                                      jobs=v.get("jobs", []))
                              for v in raw.get("variants", [])],
                    votes=[Vote(**v) for v in raw.get("votes", [])],
                )
                self.items[exp.id] = exp
            except Exception:
                continue          # one bad line must not lose the rest

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        rows = []
        for exp in self.items.values():
            rows.append(json.dumps({
                "id": exp.id, "name": exp.name, "base": exp.base, "axes": exp.axes,
                "seeds": exp.seeds, "provenance": exp.provenance,
                "created": exp.created, "note": exp.note,
                "variants": [v.public() for v in exp.variants],
                "votes": [asdict(v) for v in exp.votes],
            }, ensure_ascii=False))
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text("".join(r + "\n" for r in rows), encoding="utf-8")
        tmp.replace(self.path)

    def create(self, name: str, base: dict, axes: dict, seeds: list[int],
               provenance_: dict | None = None) -> tuple[Experiment, str]:
        variants, warning = expand(axes, seeds)
        exp = Experiment(id=uuid.uuid4().hex[:10], name=name or "未命名實驗",
                         base=base, axes=axes, seeds=seeds, variants=variants,
                         provenance=provenance_ or {})
        self.items[exp.id] = exp
        return exp, warning

    def get(self, exp_id: str) -> Experiment | None:
        return self.items.get(exp_id)

    def delete(self, exp_id: str) -> bool:
        return self.items.pop(exp_id, None) is not None

    def recent(self, limit: int = 30) -> list[Experiment]:
        return sorted(self.items.values(), key=lambda e: -e.created)[:limit]


# -- pairing for blind scoring ----------------------------------------------


def next_pair(exp: Experiment, criterion: str,
              rng: random.Random | None = None) -> dict | None:
    """Two finished jobs from different variants on the SAME seed.

    Same seed is the whole point: comparing variant A on seed 1 against variant
    B on seed 2 measures the seed. The pair is returned without variant labels;
    the caller reveals them after the vote.
    """
    rng = rng or random
    by_seed: dict[int, list[tuple[str, str]]] = {}
    for variant in exp.variants:
        for index, job in enumerate(variant.jobs):
            if index < len(exp.seeds):
                by_seed.setdefault(exp.seeds[index], []).append((variant.id, job))
    seen = {(v.criterion, tuple(sorted((v.winner, v.loser))))
            for v in exp.votes if v.criterion == criterion}
    options = []
    for seed, entries in by_seed.items():
        for (a_id, a_job), (b_id, b_job) in itertools.combinations(entries, 2):
            if a_id == b_id:
                continue
            if (criterion, tuple(sorted((a_id, b_id)))) in seen:
                continue
            options.append({"seed": seed, "a": {"variant": a_id, "job": a_job},
                            "b": {"variant": b_id, "job": b_job}})
    if not options:
        return None
    pick = rng.choice(options)
    # Randomise which side is shown first, or position bias becomes the result.
    if rng.random() < 0.5:
        pick["a"], pick["b"] = pick["b"], pick["a"]
    return pick

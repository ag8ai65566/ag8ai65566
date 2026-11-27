"""繪師實驗室: try a lot of artist tags, then let the machine mix them.

The problem
-----------
A style that someone wants is usually a *blend* of two or three artist tags
at particular weights, out of tens of thousands of possible tags. Nobody can
search that by hand: a hundred candidates already make 4,950 pairs.

What this does
--------------
1. **Solo sweep.** Every artist in a pasted list gets one picture with the
   same prompt and the same seed, so the only thing that differs between two
   pictures is the artist. (The online galleries of NovelAI artist tags are
   built the same way - nax.moe, NovelAIv4-Style-Codex.) One extra picture
   with no artist at all is the baseline.
2. **Scoring**, when a target picture was given: each result's style vector
   (kaloscope.py) against the target's. That ranks a hundred artists by how
   close each one's style is to the wanted one, with no content involved.
3. **Mixing.** The best few (or the ones the user starred) are combined in
   twos and threes; with a target, the search then goes round by round,
   keeping whatever scores best. Each round has two parts:

   * *careful* - every blend one weight step away from the best so far (each
     artist a notch up, and a notch down). Weights are a smooth dial, so
     this is a plain hill climb and it does not depend on luck;
   * *exploring* - random changes to the best few: swap one artist, add one,
     drop one, jump a weight. This is what finds a different set of artists.

   It stops when the rounds run out or two rounds in a row improve nothing.

   The first version of this was all random, and measuring it showed why
   that is wrong: over 300 runs against a known blend (a made-up score that
   peaks at one blend) it found the right artists 94-100% of the time but
   the exact weights in only 5-13%, and improved on the equal-weight blend
   at all in 33-60% - a specific helpful weight change was a 1-in-12 draw.
   With the careful part, same runs: the exact weights every time for two
   artists within three rounds. Three artists at uneven weights need more
   steps - 4% exact after three rounds, 100% after five (91% when the score
   is given +-0.03 of noise) - so the page offers five rounds by default.
   A real style score is rougher than that made-up one; these numbers are
   about the search, not about how alike the pictures end up.

Without a target there is nothing to score against, so the user's stars are
the judgement: star some, mix them, star again.

The search itself never touches ComfyUI or the style model - `run_solo` and
`run_mix` are handed submit / wait / score - so it is tested without either.
"""

from __future__ import annotations

import itertools
import json
import random
import re
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

import artists as artist_book
import kaloscope

MAX_ARTISTS = 200
CHUNK = 6                 # jobs submitted at a time, so "stop" takes effect soon
BEAM = 4                  # how many of the best blends breed the next round
MAX_SIZE = 4              # artists in one blend
WEIGHTS = (0.6, 0.8, 1.0, 1.2, 1.4)
PLATEAU = 0.004
DEFAULT_PROMPT = "1girl, solo, upper body, looking at viewer, smile, outdoors, detailed background"

_SPLIT = re.compile(r"[,\n\r\t;|、，]+")
_NAI_WEIGHT = re.compile(r"-?\d+(?:\.\d+)?::")
_WRAPPED = re.compile(r"^\((.+):\s*-?\d+(?:\.\d+)?\)$")
_PREFIX = re.compile(r"^(?:artist\s*:|by\s+|artist\s+|画师[:：]|繪師[:：]|畫師[:：])\s*", re.I)


# -- reading a pasted list -------------------------------------------------------


def normalise(token: str) -> str:
    """One pasted item as a danbooru artist tag, or '' if it is not one."""
    text = token.strip()
    text = text.replace("\\(", "(").replace("\\)", ")")
    text = text.strip("{}[] 　")
    while (match := _WRAPPED.match(text)):
        text = match.group(1).strip()
    text = _PREFIX.sub("", text).strip().strip("{}[]").strip().strip("\\").strip()
    text = re.sub(r"\s+", "_", text.lower())
    text = re.sub(r"_+", "_", text).strip("_")
    if not text or len(text) > 80 or text.isdigit():
        return ""
    fixed = artist_book.misnamed(text)
    return fixed.tag if fixed else text


def parse(text: str) -> dict:
    """A pasted blob in any of the usual spellings -> clean tags, in order.

    Understands `artist:name`, `by name`, NovelAI's `1.2::artist:name ::` and
    `{{name}}`, ComfyUI's `(artist:name:1.1)`, escaped brackets, and commas or
    new lines between items. Weights are dropped: this is a list of who to
    try, and the lab sets its own weights.
    """
    cleaned = _NAI_WEIGHT.sub("", str(text or "")).replace("::", ",")
    tags, dropped, seen = [], [], set()
    for token in _SPLIT.split(cleaned):
        tag = normalise(token)
        if not tag or tag in seen:
            continue
        seen.add(tag)
        if tag in kaloscope.WITHHELD:
            dropped.append(tag)
            continue
        tags.append(tag)
    return {"artists": tags[:MAX_ARTISTS], "dropped": dropped,
            "truncated": max(0, len(tags) - MAX_ARTISTS)}


_NAMES_ARTIST = re.compile(r"^artist\s*:", re.I)
_BY = re.compile(r"^by\s+", re.I)


def prompt_artists(prompt: str, known: set[str] | None = None) -> list[str]:
    """The artist tags a generation prompt names outright, in order.

    Why this matters: measured on 151 NoobAI images from CivitAI (2026-11-27),
    the style model put the prompt's own artist tags first for 1% of them and
    in its top five for 5% - an AI picture made "in the style of" an artist
    does not look enough like that artist's real work for it to say who. When
    the file still carries its prompt, the tags are simply written there.

    Only explicit forms count - `artist:name` (in any weighting syntax), and
    `by name` when the style model knows the name - because a bare name cannot
    be told apart from any other tag, and "by the window" is not an artist.
    """
    cleaned = _NAI_WEIGHT.sub("", str(prompt or "")).replace("::", ",")
    out: list[str] = []
    for token in _SPLIT.split(cleaned):
        bare = token.strip().replace("\\(", "(").replace("\\)", ")").strip("{}[] 　")
        while (match := _WRAPPED.match(bare)):
            bare = match.group(1).strip()
        if bare.startswith("(") and bare.endswith(")") and _NAMES_ARTIST.match(bare[1:]):
            bare = bare[1:-1].strip()
        if _NAMES_ARTIST.match(bare):
            tag = normalise(bare)
        elif _BY.match(bare) and known:
            tag = normalise(bare)
            tag = tag if tag in known else ""
        else:
            continue
        if tag and tag not in out and tag not in kaloscope.WITHHELD:
            out.append(tag)
    return out


def spellcheck(tags: list[str], known: list[str]) -> list[dict]:
    """Which of these the style model has heard of, and near misses for the rest.

    Not knowing a name is not proof it is wrong - the model only lists artists
    with enough pictures - but it is the cheapest typo check there is.
    """
    import difflib

    have = set(known)
    by_head: dict[str, list[str]] = {}
    for name in known:
        by_head.setdefault(name[:2], []).append(name)
    out = []
    for tag in tags:
        if not known or tag in have:
            out.append({"tag": tag, "known": bool(known), "suggest": []})
            continue
        pool = by_head.get(tag[:2], []) + [n for n in known if tag in n][:50]
        out.append({"tag": tag, "known": False,
                    "suggest": difflib.get_close_matches(tag, pool, n=3, cutoff=0.75)})
    return out


# -- writing tags back out -------------------------------------------------------


def _spaced(tag: str) -> str:
    return tag.replace("_", " ")


def prompt_tag(tag: str, form: str, weight: float = 1.0) -> str:
    """For this app's checkpoints: the model's own prefix, brackets escaped."""
    name = re.sub(r"([()])", r"\\\1", _spaced(tag))
    body = (form or "{tag}").replace("{tag}", name)
    return body if abs(weight - 1.0) < 0.005 else f"({body}:{round(weight, 2)})"


def prompt_for(members: list, form: str) -> str:
    return ", ".join(prompt_tag(tag, form, weight) for tag, weight in members)


def novelai_for(members: list) -> str:
    """NovelAI's spelling: `artist:` prefix, and V4+'s numeric emphasis
    (`1.2::text ::`, from docs.novelai.net/en/image/strengthening-weakening)."""
    parts = []
    for tag, weight in members:
        body = f"artist:{_spaced(tag)}"
        parts.append(body if abs(weight - 1.0) < 0.005 else f"{round(weight, 2)}::{body} ::")
    return ", ".join(parts)


# -- blends ---------------------------------------------------------------------


def key_of(members: list) -> str:
    return "|".join(f"{tag}@{round(float(weight), 2)}" for tag, weight in sorted(members))


def first_generation(pool: list[str], sizes: tuple[int, ...], count: int,
                     rank: dict[str, float], rng: random.Random) -> list[list]:
    """Equal-weight blends of the pool, the most promising first.

    With solo scores, a blend's promise is the sum of its members' scores.
    Without them every blend is as good as another, so it is a random sample -
    but a fixed one, so asking twice gives the same answer.
    """
    blends = []
    for size in sizes:
        if 2 <= size <= MAX_SIZE and size <= len(pool):
            blends += [list(c) for c in itertools.combinations(pool, size)]
    if rank:
        blends.sort(key=lambda c: (-sum(rank.get(t, 0.0) for t in c) / len(c), len(c), c))
    else:
        rng.shuffle(blends)
    return [[[tag, 1.0] for tag in blend] for blend in blends[:max(1, count)]]


def mutate(members: list, pool: list[str], rng: random.Random) -> list:
    """One small change: swap a member, add one, drop one, or shift a weight."""
    members = [list(m) for m in members]
    inside = {tag for tag, _ in members}
    outside = [t for t in pool if t not in inside]
    moves = ["weight"]
    if outside:
        moves.append("swap")
        if len(members) < MAX_SIZE:
            moves.append("add")
    if len(members) > 2:
        moves.append("drop")
    move = rng.choice(moves)
    if move == "swap":
        members[rng.randrange(len(members))] = [rng.choice(outside), 1.0]
    elif move == "add":
        members.append([rng.choice(outside), 0.8])
    elif move == "drop":
        members.pop(rng.randrange(len(members)))
    else:
        slot = rng.randrange(len(members))
        current = members[slot][1]
        options = [w for w in WEIGHTS if abs(w - current) > 0.05 and abs(w - current) <= 0.45]
        members[slot][1] = rng.choice(options or [1.0])
    return members


def neighbours(members: list) -> list[list]:
    """Every blend one weight step away: each artist a notch up, and a notch down."""
    out = []
    for slot, (_tag, weight) in enumerate(members):
        at = min(range(len(WEIGHTS)), key=lambda i: abs(WEIGHTS[i] - float(weight)))
        for step in (1, -1):
            if 0 <= at + step < len(WEIGHTS):
                child = [list(m) for m in members]
                child[slot][1] = WEIGHTS[at + step]
                out.append(child)
    return out


def next_generation(parents: list[list], pool: list[str], seen: set[str], count: int,
                    rng: random.Random) -> list[list]:
    """The next round: weight steps around the best blends, then random changes.

    `parents` is best first. Up to three quarters of the round goes to the
    untried weight neighbours of the best blend (then the runner-up's, if the
    best has none left); the rest is exploration, so a round never becomes
    all one or the other.
    """
    children: list[list] = []
    careful = count - max(1, count // 4)
    for parent in parents:
        for child in neighbours(parent):
            if len(children) >= careful:
                break
            key = key_of(child)
            if key not in seen:
                seen.add(key)
                children.append(child)
        if len(children) >= careful:
            break
    tries = 0
    while len(children) < count and parents and tries < count * 40:
        tries += 1
        child = mutate(parents[tries % len(parents)], pool, rng)
        key = key_of(child)
        if key in seen:
            continue
        seen.add(key)
        children.append(child)
    return children


# -- state -----------------------------------------------------------------------


@dataclass
class Entry:
    key: str
    artists: list            # [[tag, weight], ...]; empty for the baseline
    stage: str               # baseline | solo | mix | evolve
    gen: int = 0
    job: str = ""
    output: str = ""
    score: float | None = None
    star: bool = False
    error: str = ""


@dataclass
class Lab:
    id: str
    created: float
    base: dict               # the image tab's settings
    prompt: str
    negative: str
    form: str                # the model's artist prefix, e.g. "artist:{tag}"
    seed: int
    target: str = ""         # staged file name of the wanted style, if any
    entries: list = field(default_factory=list)
    status: str = "idle"     # idle | running | stopped | error
    phase: str = ""          # solo | mix
    message: str = ""
    gens: int = 0

    def public(self) -> dict:
        data = asdict(self)
        data.pop("base", None)
        data["model"] = self.base.get("model", "")
        for entry in data["entries"]:
            entry["text"] = prompt_for(entry["artists"], self.form)
            entry["novelai"] = novelai_for(entry["artists"])
        return data

    def find(self, key: str) -> Entry | None:
        return next((e for e in self.entries if e.key == key), None)

    def solo_rank(self) -> dict[str, float]:
        return {e.artists[0][0]: e.score for e in self.entries
                if e.stage == "solo" and e.score is not None and e.artists}

    def ranked(self, stages: tuple[str, ...]) -> list[Entry]:
        scored = [e for e in self.entries if e.stage in stages and e.score is not None]
        return sorted(scored, key=lambda e: -e.score)


def new_lab(*, base: dict, prompt: str, negative: str, form: str, seed: int, target: str) -> Lab:
    return Lab(id=uuid.uuid4().hex[:10], created=time.time(), base=dict(base),
               prompt=prompt.strip() or DEFAULT_PROMPT, negative=negative, form=form,
               seed=int(seed), target=target)


def full_prompt(lab: Lab, entry: Entry) -> str:
    """Artists first, then the test prompt: the usual place for an artist tag."""
    tags = prompt_for(entry.artists, lab.form)
    return f"{tags}, {lab.prompt}" if tags else lab.prompt


async def _generate(lab: Lab, entries: list[Entry], *, submit, wait, score, cancelled, save,
                    label: str) -> bool:
    """Run these entries through the queue in small batches. False if stopped."""
    for start in range(0, len(entries), CHUNK):
        if cancelled():
            return False
        batch = entries[start:start + CHUNK]
        done_so_far = start
        lab.message = f"{label}：{done_so_far}/{len(entries)} 張…"
        save()
        for entry in batch:
            entry.job = await submit(lab, entry)
        save()
        results = await wait([e.job for e in batch])
        for entry in batch:
            status, output, message = results.get(entry.job, ("error", "", "沒有結果"))
            entry.output = output
            if status != "done" or not output:
                entry.error = message or status
                continue
            if score is not None:
                entry.score = round(float(await score(output)), 4)
        save()
    return not cancelled()


async def run_solo(lab: Lab, tags: list[str], *, submit, wait, score, cancelled,
                   save=lambda: None) -> None:
    """One picture per artist, plus one with none."""
    lab.status, lab.phase = "running", "solo"
    try:
        have = {e.key for e in lab.entries}
        fresh = []
        if "baseline" not in have:
            fresh.append(Entry(key="baseline", artists=[], stage="baseline"))
        for tag in tags:
            members = [[tag, 1.0]]
            if key_of(members) not in have:
                fresh.append(Entry(key=key_of(members), artists=members, stage="solo"))
        lab.entries += fresh
        finished = await _generate(lab, fresh, submit=submit, wait=wait, score=score,
                                   cancelled=cancelled, save=save, label="單人試畫")
        lab.status = "idle" if finished else "stopped"
        lab.message = "" if finished else "已停止"
        if finished and fresh and all(e.error for e in fresh):
            lab.status, lab.message = "error", "一張都沒生出來：" + fresh[0].error
    except Exception as exc:  # noqa: BLE001 - reported on the page
        lab.status, lab.message = "error", f"{type(exc).__name__}: {exc}"
    finally:
        save()


async def run_mix(lab: Lab, pool: list[str], *, count: int, sizes: tuple[int, ...], rounds: int,
                  per_round: int, submit, wait, score, cancelled, save=lambda: None) -> None:
    """Blend the pool; with a score to go by, keep breeding the best blends."""
    lab.status, lab.phase = "running", "mix"
    rng = random.Random(f"{lab.id}:{lab.gens}")
    try:
        seen = {e.key for e in lab.entries}
        lab.gens += 1
        blends = [b for b in first_generation(pool, sizes, count * 3, lab.solo_rank(), rng)
                  if key_of(b) not in seen][:count]
        if not blends:
            # Everything obvious was already tried: go straight to variations.
            parents = [e.artists for e in lab.ranked(("mix", "evolve"))[:BEAM]] or \
                      [[[t, 1.0] for t in pool[:2]]]
            blends = next_generation(parents, pool, seen, count, rng)
        entries = [Entry(key=key_of(b), artists=b, stage="mix", gen=lab.gens) for b in blends]
        seen.update(e.key for e in entries)
        lab.entries += entries
        finished = await _generate(lab, entries, submit=submit, wait=wait, score=score,
                                   cancelled=cancelled, save=save, label="第一批組合")
        stalls = 0
        for round_no in range(1, max(0, rounds) + 1):
            if not finished or score is None:
                break
            before = max((e.score for e in lab.ranked(("mix", "evolve"))), default=0.0)
            parents = [e.artists for e in lab.ranked(("mix", "evolve"))[:BEAM]]
            children = next_generation(parents, pool, seen, per_round, rng)
            if not children:
                break
            lab.gens += 1
            entries = [Entry(key=key_of(c), artists=c, stage="evolve", gen=lab.gens) for c in children]
            lab.entries += entries
            finished = await _generate(lab, entries, submit=submit, wait=wait, score=score,
                                       cancelled=cancelled, save=save,
                                       label=f"自動調整第 {round_no}/{rounds} 輪")
            after = max((e.score for e in lab.ranked(("mix", "evolve"))), default=0.0)
            stalls = stalls + 1 if after < before + PLATEAU else 0
            if stalls >= 2:
                lab.message = "連續兩輪沒有更像，停在這裡。"
                break
        lab.status = "idle" if finished else "stopped"
        if not finished:
            lab.message = "已停止"
        elif not lab.message.startswith("連續"):
            lab.message = ""
    except Exception as exc:  # noqa: BLE001
        lab.status, lab.message = "error", f"{type(exc).__name__}: {exc}"
    finally:
        save()


class Store:
    """Recent labs on disk, so results outlive a restart of the app."""

    def __init__(self, path: Path, keep: int = 8) -> None:
        self.path, self.keep = path, keep
        self.labs: dict[str, Lab] = {}

    def load(self) -> None:
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return
        for item in raw if isinstance(raw, list) else []:
            try:
                entries = [Entry(**e) for e in item.pop("entries")]
                lab = Lab(**item, entries=entries)
            except (TypeError, KeyError):
                continue
            if lab.status == "running":
                lab.status, lab.message = "stopped", "app 重新啟動過，停在這裡（已經生好的都還在）"
            self.labs[lab.id] = lab

    def add(self, lab: Lab) -> None:
        self.labs[lab.id] = lab
        for old in sorted(self.labs.values(), key=lambda l: l.created)[:-self.keep]:
            self.labs.pop(old.id, None)
        self.save()

    def save(self) -> None:
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            data = [asdict(l) for l in sorted(self.labs.values(), key=lambda l: l.created)]
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            tmp.replace(self.path)
        except OSError:
            pass

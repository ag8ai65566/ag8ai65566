#!/usr/bin/env python3
"""Convert the novel-lab scene format to offline Eleven v4 request bodies."""
import argparse
import datetime
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

TAG = re.compile(r"\[([^\[\]\n]+)\]")
JAPANESE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
SCENE_ID = re.compile(r"[a-z0-9][a-z0-9_-]{0,79}")
RESERVED = {"STAGE", "SFX", "PAUSE", "ROMAJI", "GLOSS"}
MARKER = "【Sudowrite 處理】"
# Heuristics, not linguistic proof. A director must review every warning.
DUPLICATES = [
    (r"(?:laughs?(?: harder)?|laughing|giggles?|giggling|chuckles?|chuckling)",
     r"\b(?:ha(?:[\s,-]*ha)+|he(?:[\s,-]*he)+|laughs?|giggles?|chuckles?)\b"),
    (r"(?:sighs?|sighing)", r"\b(?:sighs?|sighing)\b"),
    (r"(?:gasps?|gasping)", r"\b(?:gasps?|gasping)\b"),
    (r"(?:sobs?|sobbing|crying)", r"\b(?:sobs?|sob(?:[\s,-]*sob)+)\b"),
    (r"(?:screams?|screaming)", r"\b(?:screams?|a{3,}h*)\b"),
    (r"(?:snorts?|snorting)", r"\b(?:snorts?|snorting)\b"),
    (r"(?:sneezes?|sneezing)", r"\b(?:a+h?-?choo+|sneezes?)\b"),
    (r"(?:hiccups?|hiccuping)", r"\b(?:hic+|hiccups?)\b"),
    (r"(?:coughs?|coughing)", r"\b(?:coughs?|ahem)\b"),
    (r"(?:hums?|humming)", r"\b(?:hums?|humming|hm{3,})\b"),
    (r"(?:groans?|groaning)", r"\b(?:groans?|ugh+)\b"),
    (r"(?:yawns?|yawning)", r"\b(?:yawns?)\b"),
    (r"vocal percussion", r"\b(?:vocal percussion)\b"),
]


def sound(kind, tag):
    """A sound word anywhere in the tag counts ("[dramatic gasp]", "[laughs harder]"); Claude, 2026-10-03."""
    return re.search(r"(?<![\w-])" + kind + r"(?![\w-])", tag) is not None


def norm(tag):
    return " ".join(tag.split()).casefold()


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("Duplicate JSON key: " + key)
        out[key] = value
    return out


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"),
                      object_pairs_hook=unique_object)


def sheet_policy(text):
    """Only positive sections 2, 4 and 5; never examples or Don't."""
    title = re.search(r"^# ElevenLabs v4 Performance Sheet: (.+)$", text, re.M)
    if not title:
        return None
    allowed = set()
    for number in (2, 4, 5):
        section = re.search(
            r"^## " + str(number) + r"\.[^\n]*\n(.*?)(?=^## |\Z)",
            text, re.M | re.S)
        if section:
            allowed.update(norm(t) for t in TAG.findall(section.group(1)))
    if not allowed:
        raise ValueError("No positive tag palette for " + title.group(1))
    return title.group(1).strip(), allowed


def load_policies(directory):
    policies, hashes = {}, {}
    for path in sorted(directory.glob("*.md")):
        data = path.read_bytes()
        policy = sheet_policy(data.decode("utf-8-sig"))
        if policy is None:
            continue
        name, tags = policy
        if name in policies:
            raise ValueError("Duplicate performance sheet for " + name)
        policies[name] = tags
        hashes[name] = hashlib.sha256(data).hexdigest()
    return policies, hashes


def parse_script(text):
    if MARKER in text:
        raise ValueError("HOLD: marked scene cannot enter audio conversion")
    scenes, current, last_turn = [], None, None
    ids = set()
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            if current is not None:
                current["events"].append(
                    {"kind": "NOTE", "text": line[1:].strip(), "line": number})
            continue
        if line.startswith("@@scene "):
            name = line[len("@@scene "):].strip()
            if not SCENE_ID.fullmatch(name) or name in ids:
                raise ValueError(f"Line {number}: invalid/duplicate scene ID")
            ids.add(name)
            current = {"id": name, "date": None, "events": []}
            scenes.append(current)
            last_turn = None
            continue
        if current is None:
            raise ValueError(f"Line {number}: content before @@scene")
        if line.startswith("@@date "):
            if current["date"] is not None or any(
                    e["kind"] != "NOTE" for e in current["events"]):
                raise ValueError(f"Line {number}: date must precede scene content")
            value = line[len("@@date "):].strip()
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ValueError(f"Line {number}: use YYYY-MM-DD")
            datetime.date.fromisoformat(value)
            current["date"] = value
            continue
        if " :: " not in line:
            raise ValueError(f"Line {number}: expected LABEL :: content")
        label, value = line.split(" :: ", 1)
        label, value = label.strip(), value.strip()
        if not value:
            raise ValueError(f"Line {number}: empty content")
        if label in {"ROMAJI", "GLOSS"}:
            if last_turn is None or label in last_turn:
                raise ValueError(f"Line {number}: orphan/duplicate {label}")
            last_turn[label] = value
            continue
        kind = label if label in RESERVED else "TURN"
        if kind == "PAUSE":
            if not re.fullmatch(r"\d+(?:\.\d+)?", value) or not 0 < float(value) <= 60:
                raise ValueError(f"Line {number}: PAUSE must be 0 < seconds <= 60")
        event = {"kind": kind, "speaker": label, "text": value, "line": number}
        current["events"].append(event)
        last_turn = event if kind == "TURN" else None
    if not scenes:
        raise ValueError("No scenes")
    for scene in scenes:
        if scene["date"] is None:
            raise ValueError(scene["id"] + ": missing @@date")
    return scenes


def check_text(text, allowed, location, require_tag=False):
    tags = [norm(t) for t in TAG.findall(text)]
    plain = TAG.sub("", text)
    if "[" in plain or "]" in plain:
        raise ValueError(location + ": malformed/nested brackets")
    if re.search(r"<[^>]*>", text):
        raise ValueError(location + ": XML/SSML is outside this format")
    unknown = set(tags) - allowed
    if unknown:
        raise ValueError(location + ": unlisted tags: " + ", ".join(sorted(unknown)))
    warnings = []
    if require_tag and not tags:
        raise ValueError(location + ": spoken turn needs a listed delivery tag")
    if len(tags) > 3:
        warnings.append(location + ": more than three directions")
    if not plain.strip() and not any(
            sound(kind, tag) for kind, _ in DUPLICATES for tag in tags):
        raise ValueError(location + ": delivery-only turn has no spoken text")
    for tag in tags:
        for kind, spelled in DUPLICATES:
            if sound(kind, tag) and re.search(spelled, plain, re.I):
                warnings.append(location + ": possible duplicate nonverbal " + tag)
    return warnings


def split_turn(text, maximum):
    """Preserve order and protected tags/IPA; trim only boundary whitespace."""
    protected = [(m.start(), m.end()) for m in
                 re.finditer(r"\[[^\[\]\n]+\]|/[^/\n]+/", text)]

    def safe(position):
        if any(a < position < b for a, b in protected):
            return False
        return (position == len(text) or
                (not unicodedata.combining(text[position]) and
                 text[position] != "\u200d" and text[position - 1] != "\u200d"))

    sentence = [m.end() for m in re.finditer(
        r'(?:[.!?](?:["”’])?(?=\s|$)|[。！？…](?:["”’」』])?)', text)]
    spaces = [m.end() for m in re.finditer(r"\s+", text)]
    japanese = [i for i in range(1, len(text)) if JAPANESE.search(text[i - 1:i])]
    groups = [[i for i in points if safe(i)] for points in (sentence, spaces, japanese)]
    pieces, start = [], 0
    while len(text) - start > maximum:
        cut = None
        for points in groups:
            possible = [i for i in points if start < i <= start + maximum]
            if possible:
                cut = max(possible)
                break
        if cut is None:
            raise ValueError("Unsplittable token exceeds turn limit; edit the source")
        piece = text[start:cut].strip()
        if not piece:
            raise ValueError("Cannot split an empty turn")
        pieces.append(piece)
        start = cut
        while start < len(text) and text[start].isspace():
            start += 1
    if text[start:].strip():
        pieces.append(text[start:].strip())
    return pieces


def valid_voice_id(value):
    return (isinstance(value, str) and
            re.fullmatch(r"[A-Za-z0-9_-]+", value) is not None and
            value.casefold() not in {"todo", "pending", "placeholder"})


def compile_script(text, voices, policies, *, narrator="exclude",
                   max_turn=500, seed=None, dictionaries=None, lint_only=False):
    if not isinstance(voices, dict) or any(
            not isinstance(v, str) for k, v in voices.items() if k != "_about"):
        raise ValueError("Voice map must be speaker -> voice_id strings")
    if not 80 <= max_turn <= 2000:
        raise ValueError("max_turn must be between 80 and 2000")
    if seed is not None and (type(seed) is not int or not 0 <= seed <= 4294967295):
        raise ValueError("seed must be an integer from 0 through 4294967295")
    dictionaries = [] if dictionaries is None else dictionaries
    if not isinstance(dictionaries, list) or len(dictionaries) > 3:
        raise ValueError("Dictionary locators must be a list of at most three")
    for item in dictionaries:
        if (not isinstance(item, dict) or
            set(item) != {"pronunciation_dictionary_id", "version_id"} or
            any(not isinstance(v, str) or not v.strip() for v in item.values())):
            raise ValueError("Each dictionary needs pronunciation_dictionary_id and version_id")

    products, warnings = {}, []
    for scene in parse_script(text):
        inputs, used = [], {}
        listening = [f"SCENE {scene['id']} | DATE {scene['date']}",
                     "MODEL eleven_v4 | request order below",
                     "STAGE/SFX/PAUSE/ROMAJI/GLOSS/NOTE are not synthesized."]
        for event in scene["events"]:
            kind, value, line = event["kind"], event["text"], event["line"]
            if kind != "TURN":
                listening.append(f"L{line} {kind} :: {value}")
                continue
            speaker = event["speaker"]
            location = f"{scene['id']}:L{line}:{speaker}"
            if speaker == "narrator":
                if TAG.search(value):
                    raise ValueError(location + ": narration must be untagged")
                if narrator == "exclude":
                    listening.append(f"L{line} OMITTED narrator :: {value}")
                    for key in ("ROMAJI", "GLOSS"):
                        if key in event:
                            listening.append(f"    {key} (not spoken) :: {event[key]}")
                    continue
                allowed = set()
            else:
                if speaker not in policies:
                    raise ValueError(location + ": no matching performance sheet")
                allowed = policies[speaker]
            if speaker not in voices:
                raise ValueError(location + ": missing speaker in voice map")
            voice_id = voices[speaker]
            if not valid_voice_id(voice_id):
                if not lint_only:
                    raise ValueError(location + ": unresolved/invalid voice_id")
                warnings.append(location + ": voice_id pending; lint only")
            used[speaker] = voice_id
            warnings.extend(check_text(value, allowed, location, speaker != "narrator"))
            if JAPANESE.search(TAG.sub("", value)) and "ROMAJI" not in event:
                raise ValueError(location + ": Japanese text requires ROMAJI metadata")
            pieces = split_turn(value, max_turn)
            if len(pieces) > 1:
                warnings.append(location + ": split turn; check delivery at every join")
            for index, piece in enumerate(pieces, 1):
                check_text(piece, allowed, location)
                inputs.append({"text": piece, "voice_id": voice_id})
                listening.append(
                    f"{len(inputs):03d} L{line} {speaker} part {index}/{len(pieces)}"
                    f" | voice_id={voice_id}\n    {piece}")
            for key in ("ROMAJI", "GLOSS"):
                if key in event:
                    listening.append(f"    {key} (not spoken) :: {event[key]}")
        if not inputs:
            raise ValueError(scene["id"] + ": no audio turns")
        total = sum(len(item["text"].encode("utf-16-le")) // 2 for item in inputs)
        if total > 2000:
            raise ValueError(
                f"{scene['id']}: {total} characters; split at a dramatic boundary "
                "into separate @@scene IDs, each <= 2000")
        if len(set(used.values())) > 10:
            raise ValueError(scene["id"] + ": more than ten unique voice IDs")
        if not lint_only and len(set(used.values())) != len(used):
            raise ValueError(scene["id"] + ": distinct speakers need distinct designed voices")
        body = {"model_id": "eleven_v4", "inputs": inputs}
        if seed is not None:
            body["seed"] = seed
        if dictionaries:
            body["pronunciation_dictionary_locators"] = dictionaries
        listening.append(f"TOTAL {total} characters | {len(inputs)} inputs")
        products[scene["id"]] = (body, "\n".join(listening) + "\n")
    return products, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("script", type=Path)
    ap.add_argument("--voice-map", required=True, type=Path)
    ap.add_argument("--sheets", required=True, type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--narrator", choices=("exclude", "include"), default="exclude")
    ap.add_argument("--max-turn", type=int, default=500)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--dictionaries", type=Path)
    ap.add_argument("--lint-only", action="store_true")
    ap.add_argument("--allow-warnings", action="store_true")
    args = ap.parse_args()
    try:
        if not args.sheets.is_dir():
            raise ValueError("Sheets directory does not exist")
        voices = read_json(args.voice_map)
        policies, sheet_hashes = load_policies(args.sheets)
        script = args.script.read_text(encoding="utf-8-sig")
        dictionaries = read_json(args.dictionaries) if args.dictionaries else None
        products, warnings = compile_script(
            script, voices, policies, narrator=args.narrator,
            max_turn=args.max_turn, seed=args.seed, dictionaries=dictionaries,
            lint_only=args.lint_only)
        for warning in warnings:
            print("WARNING: " + warning, file=sys.stderr)
        if warnings and not args.allow_warnings:
            raise ValueError("Review warnings; edit the script or use --allow-warnings")
        if args.lint_only:
            print(f"Lint complete: {len(products)} scene(s); no requests written")
            return 0
        if args.out is None:
            raise ValueError("--out is required unless --lint-only")
        provenance = {
            "converter_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "script_sha256": hashlib.sha256(args.script.read_bytes()).hexdigest(),
            "voice_map_sha256": hashlib.sha256(args.voice_map.read_bytes()).hexdigest(),
            "sheet_sha256": sheet_hashes,
            "narrator": args.narrator, "max_turn": args.max_turn,
            "warnings": warnings,
        }
        files = {}
        for scene_id, (body, listening) in products.items():
            files[scene_id + ".json"] = json.dumps(body, ensure_ascii=False, indent=2) + "\n"
            files[scene_id + ".listening.txt"] = (
                listening + "\nBUILD RECORD\n" +
                json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
        # Preflight every target before creating any output. Never overwrite.
        for filename in files:
            if (args.out / filename).exists():
                raise ValueError("Output already exists: " + str(args.out / filename))
        args.out.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            with (args.out / filename).open("x", encoding="utf-8", newline="\n") as fh:
                fh.write(content)
        print(f"Wrote {len(products)} request(s) and listening sheets")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

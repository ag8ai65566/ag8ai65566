#!/usr/bin/env python3
"""Validate and build a versioned delivery package (validation spec V01–V25, GPT consult round 2).

  python3 novel-lab/tools/release.py validate holoen [--phase candidate|final]
  python3 novel-lab/tools/release.py stamp-sheets holoen --reviewed "<who/what reviewed the sheets>"
  python3 novel-lab/tools/release.py build holoen [--draft]

`validate` writes projects/<slug>/research/qa/validation.json and exits 2 when a blocking check fails.
Checks that need a human/GPT review (dates, credits, quotations, scope, voice, acceptance) pass only when
the review file named in ATTEST exists; a missing review is a failure, never an automatic pass.
`build` writes projects/<slug>/delivery/<slug>-<baseline>-rNN/ (outside export/, which the exporter
clears). Without --draft it refuses to build while a blocking check fails.
"""
import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lab  # noqa: E402
import qa_packets  # noqa: E402

ROOT = lab.ROOT
BASELINE = "2026-09-30"
VOICE_FIELDS = ["Name", "Dialogue Style", "Catchphrases", "Voice & Delivery", "Audio Tags"]
CUSTOM_TRAITS = {"Catchphrases", "Voice & Delivery", "Audio Tags", "Motivation", "Relationships", "Secrets",
                 "Rules", "Sensory Details"}
EXPECT = {"characters": 18, "world": 24, "sheets": 18}
CAST_ORDER = ["Mori-Calliope", "Takanashi-Kiara", "Ninomae-Inanis", "Gawr-Gura", "Watson-Amelia",
              "IRyS", "Ouro-Kronii", "Ceres-Fauna", "Nanashi-Mumei",
              "Shiori-Novella", "Koseki-Bijou", "Nerissa-Ravencroft", "Fuwawa-Abyssgard", "Mococo-Abyssgard",
              "Elizabeth-Rose-Bloodflame", "Gigi-Murin", "Cecilia-Immergreen", "Raora-Panthera"]
WORLD_ORDER = ["VTuber-Persona-and-Lore", "hololive", "Streaming-Life",
               "hololive--Myth", "hololive--Promise", "hololive--Advent", "hololive--Justice", "FUWAMOCO",
               "TakaMori", "TakoTori", "AmeSame", "Bone-Bros", "Myth-and-Kronii-Other-Pairs", "Time-Duo",
               "Time-and-Death", "OctoClock", "Fauna-and-Mumei-Pairs", "IRyS-and-Nerissa-Pairs", "Advent-Pairs",
               "Justice-Pairs", "Cross-Branch-Friends", "Concerts-and-Live-Events", "hololive-History-to-2022",
               "hololive-History-2023-2026"]
COHORT_AUDITS = [f"research/qa/audit-{c}.md" for c in qa_packets.COHORTS]
ATTEST = {
    "V10": ["research/qa/audit-bridge-events.md"],
    # Cast-to-cast ties are compared from both sides inside the cohort audits; the bridge pass adds external people.
    "V11": ["research/qa/audit-bridge-ties-external.md"] + COHORT_AUDITS,
    "V12": COHORT_AUDITS,
    "V13": ["research/qa/voice-delivery.md"],
    "V14": COHORT_AUDITS,
    "V15": COHORT_AUDITS,
    "V19": ["research/qa/voice-delivery.md"],
    "V25": ["research/qa/release-acceptance.md"],
}
PRIVACY = re.compile(r"(?i)\b(surgery|hospital|illness|diagnos\w*|hiatus|semi-break|family emergenc\w*|"
                     r"her (mother|father|mom|dad|parents?|brother)|nationality|native (language|speaker)|"
                     r"audition\w*|vacation|days off|off-collab trip|boyfriend|girlfriend|apartment|jammies)\b")


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


def load_cards(proj):
    cards = {}
    for sub in ("characters", "world"):
        for f in sorted((proj / "bible" / sub).glob("*.md")):
            text = lab.read(f)
            cards[f.stem] = {"path": f, "sub": sub, "text": text, "meta": lab.front_matter(text),
                             "fields": lab.sw_fields(text)}
    return cards


def voice_hash(fields):
    return sha(json.dumps({k: fields.get(k, "") for k in VOICE_FIELDS}, ensure_ascii=False, sort_keys=True))


def style_block(proj):
    p = proj / "export" / "elevenlabs" / "sudowrite-style.md"
    m = re.search(r"```text\n(.*?)\n```", lab.read(p), re.S) if p.exists() else None
    return m.group(1).strip() if m else None


def norm(s):
    s = unicodedata.normalize("NFKC", s).casefold()
    return re.sub(r"[\s\-_'’.·]+", "", s)


class Results:
    def __init__(self):
        self.items = []

    def add(self, cid, status, severity, title, detail=None, locator=None, findings=None):
        self.items.append({"check_id": cid, "title": title, "status": status, "severity": severity,
                           "locator": locator, "evidence": detail or [], "finding_ids": findings or []})

    def blocking(self):
        return [r for r in self.items if r["status"] == "fail" and r["severity"] == "block"]


def check_all(proj, phase, package=None):
    R = Results()
    spec = json.loads(lab.read(lab.FIELDS_FILE))
    cards = load_cards(proj)
    chars = {k: v for k, v in cards.items() if v["sub"] == "characters"}
    world = {k: v for k, v in cards.items() if v["sub"] == "world"}
    sheets_dir = proj / "export" / "elevenlabs"
    sheets = {p.stem: p for p in sheets_dir.glob("*.md") if p.name != "sudowrite-style.md"}

    # V01 snapshot
    inputs = {}
    for p in sorted(list((proj / "bible").rglob("*.md")) + list(sheets_dir.glob("*.md")) +
                    [lab.FIELDS_FILE, ROOT / "tools" / "lab.py", ROOT / "tools" / "release.py",
                     ROOT / "tools" / "qa_packets.py", proj / "project.md"]):
        inputs[str(p.relative_to(ROOT))] = sha(p.read_bytes())
    snapshot = sha(json.dumps(inputs, sort_keys=True))
    st, det = "pass", [f"snapshot {snapshot}", f"{len(inputs)} inputs"]
    if phase == "final" and package:
        man = json.loads(lab.read(package / "manifest.json"))
        if man.get("snapshot") != snapshot:
            st, det = "fail", det + [f"candidate snapshot {man.get('snapshot')} differs"]
    R.add("V01", st, "block", "Source snapshot", det)

    # V02 inventory
    det = [f"characters {len(chars)}/{EXPECT['characters']}", f"world {len(world)}/{EXPECT['world']}",
           f"sheets {len(sheets)}/{EXPECT['sheets']}"]
    bad = (len(chars) != EXPECT["characters"] or len(world) != EXPECT["world"] or len(sheets) != EXPECT["sheets"]
           or set(sheets) != set(chars) or not {"Fuwawa-Abyssgard", "Mococo-Abyssgard"} <= set(chars))
    names = {v["fields"].get("Name") for v in cards.values()}
    leaked = [n for n in qa_packets.REFERENCE_ONLY if n in names]
    det += [f"sheet/card mismatch: {sorted(set(sheets) ^ set(chars))}"] if set(sheets) != set(chars) else []
    det += [f"reference-only people with cards: {leaked}"] if leaked else []
    R.add("V02", "fail" if bad or leaked else "pass", "block", "Authorized inventory", det)

    # V03 schema / V04 placeholders and field names
    errs, warns = [], []
    known = (set(spec["character_columns"]) | set(spec["worldbuilding_columns"]) | set(spec["story_fields"])
             | set(spec["hard_limits_words"]) | set(spec["soft_limits_words"]) | set(spec["hide_in_sudowrite"]))
    placeholders = lab.template_placeholders()
    for stem, c in cards.items():
        kind = c["meta"].get("kind")
        present = {m.group(1) for m in lab.SW_SECTION.finditer(c["text"])}
        for fld in spec["required"].get(kind, []):
            if fld not in present or not c["fields"].get(fld):
                errs.append(f"{stem}: required [SW] {fld} missing or empty")
        for fld in spec["optional"].get(kind, []):
            if fld not in present:
                errs.append(f"{stem}: optional [SW] {fld} heading missing")
        for d in lab.sw_duplicates(c["text"]):
            errs.append(f"{stem}: duplicate [SW] {d}")
        if c["fields"].get("Name") != c["meta"].get("name"):
            errs.append(f"{stem}: Name differs from front matter")
        if c["sub"] == "characters" and c["fields"].get("Role") != "Protagonist":
            errs.append(f"{stem}: Role is not Protagonist")
        for name, body in c["fields"].items():
            if body and any(ph in body for ph in placeholders):
                warns.append(f"{stem} · {name}: template placeholder text")
            if name not in known and name not in CUSTOM_TRAITS:
                warns.append(f"{stem} · {name}: unknown field")
    R.add("V03", "fail" if errs else "pass", "block", "Schema and headings", errs)
    R.add("V04", "fail" if any("placeholder" in w for w in warns) else ("warn" if warns else "pass"),
          "block", "Placeholders and field names", warns)

    # V05 CSV integrity / V06 export equality
    exp = proj / "export"
    errs5, errs6 = [], []
    parsed = {}
    for fname, sub in (("characters.csv", "characters"), ("worldbuilding.csv", "world")):
        raw = (exp / fname).read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            errs5.append(f"{fname}: not UTF-8 ({e})")
            continue
        if "�" in text:
            errs5.append(f"{fname}: replacement characters present")
        rows = list(csv.reader(io.StringIO(text, newline="")))
        head = rows[0]
        if len(set(head)) != len(head):
            errs5.append(f"{fname}: duplicate headers")
        if any(len(r) != len(head) for r in rows[1:]):
            errs5.append(f"{fname}: ragged rows")
        if len({tuple(r) for r in rows[1:]}) != len(rows) - 1:
            errs5.append(f"{fname}: duplicate rows")
        parsed[sub] = {r[0]: dict(zip(head, r)) for r in rows[1:]}
        group = chars if sub == "characters" else world
        if set(parsed[sub]) != {c["fields"]["Name"] for c in group.values()}:
            errs6.append(f"{fname}: card set differs from bible")
        for stem, c in group.items():
            row = parsed[sub].get(c["fields"]["Name"], {})
            for k, v in c["fields"].items():
                if k in row and row[k].strip() != v.strip():
                    errs6.append(f"{fname} · {stem} · {k}: differs from bible")
            single = exp / "cards" / f"{'characters' if sub == 'characters' else 'worldbuilding'}-{stem}.csv"
            if not single.exists():
                errs6.append(f"missing single-card CSV for {stem}")
            else:
                srows = list(csv.reader(io.StringIO(single.read_text(encoding="utf-8"), newline="")))
                if dict(zip(srows[0], srows[1])) != row:
                    errs6.append(f"{single.name}: differs from combined CSV")
    paste = lab.read(exp / "sudowrite-paste.md")
    for stem, c in cards.items():
        for k, v in c["fields"].items():
            if v and v not in paste:
                errs6.append(f"sudowrite-paste.md: {stem} · {k} missing or stale")
    R.add("V05", "fail" if errs5 else "pass", "block", "CSV integrity", errs5)
    R.add("V06", "fail" if errs6 else "pass", "block", "Export equality", errs6[:40])

    # V07 sizes
    hard, soft = [], []
    for stem, c in cards.items():
        for k, v in c["fields"].items():
            n = lab.count_words(v)
            if k in spec["hard_limits_words"] and n > spec["hard_limits_words"][k]:
                hard.append(f"{stem} · {k}: {n}/{spec['hard_limits_words'][k]}")
            elif k in spec["soft_limits_words"] and n > spec["soft_limits_words"][k]:
                soft.append(f"{stem} · {k}: {n}/{spec['soft_limits_words'][k]} (local target)")
    sb = style_block(proj)
    if sb and lab.count_words(sb) > spec["soft_limits_words"]["Style"]:
        soft.append(f"Style block {lab.count_words(sb)}/120 (local target)")
    R.add("V07", "fail" if hard else ("warn" if soft else "pass"), "block" if hard else "warn",
          "Sizes and platform limits", hard + soft)

    # V08 aliases
    owners = {}
    for stem, c in cards.items():
        for a in [c["fields"]["Name"]] + [x.strip() for x in re.split(r",\s*", c["fields"].get("Other Names", "")) if x.strip()]:
            owners.setdefault(norm(a), set()).add(c["fields"]["Name"])
    coll = [f"{a}: {sorted(n)}" for a, n in owners.items() if len(n) > 1]
    R.add("V08", "warn" if coll else "pass", "warn", "Alias ownership", coll)

    # V09 units
    det9, bad9 = [], []
    by_name = {c["fields"]["Name"]: c for c in chars.values()}
    for u in qa_packets.UNITS:
        unit = re.sub(r"\s*\(.*", "", u["unit"])
        if "official" not in u["evidence"] or unit == "LYRA":
            continue
        for m in u["members"]:
            c = by_name.get(m)
            core = re.sub(r"^hololive ", "", unit).lower()  # "-Promise-" also matches "hololive English -Promise- (graduated)"
            if c and core not in c["fields"].get("Groups", "").lower():
                det9.append(f"{m}: Groups lacks {unit}")
    for c in chars.values():
        for a in re.split(r",\s*", c["fields"].get("Other Names", "")):
            if any(norm(a) == norm(re.sub(r"\s*\(.*", "", u["unit"])) and len(u["members"]) > 1 for u in qa_packets.UNITS):
                bad9.append(f"{c['fields']['Name']}: multi-person unit {a} in Other Names")
    R.add("V09", "fail" if bad9 else ("warn" if det9 else "pass"), "block" if bad9 else "warn",
          "Units and retrieval coverage", bad9 + det9)

    # Review-attested checks
    def attested(cid, title, severity="block", extra=None, auto_fail=None):
        need = ATTEST[cid]
        missing = [p for p in need if not (proj / p).exists()]
        det = (auto_fail or []) + (extra or []) + (
            [f"review pending: {', '.join(missing)}"] if missing else [f"reviewed in {', '.join(need)}"])
        R.add(cid, "fail" if missing or auto_fail else "pass", severity, title, det)

    attested("V10", "Dates, zones and status")
    attested("V11", "Participants and directional facts")
    attested("V12", "Evidence records")
    import span_check
    spans = [f"{f}:{n} quotes past a shared ASR span ({r['report']} {r['ts']}): \"{q}\""
             for f, n, q, r in span_check.outside_spans(proj.name)]
    attested("V13", "Quotations and ASR", auto_fail=spans)
    cand = []
    for stem, c in cards.items():
        for k, v in c["fields"].items():
            for m in PRIVACY.finditer(v):
                cand.append(f"{stem} · {k}: …{v[max(0, m.start() - 40):m.end() + 30]}…")
    for stem, p in sheets.items():
        for m in PRIVACY.finditer(lab.read(p)):
            cand.append(f"sheet {stem}: …{m.group(0)}…")
    attested("V14", "Scope screening", extra=[f"{len(cand)} automated candidates for semantic review"] + cand[:30])
    attested("V15", "Card usability and fidelity")

    # V16 secrets
    sec = [s for s, c in cards.items() if c["fields"].get("Secrets")]
    R.add("V16", "pass" if not sec else "warn", "block", "Secrets and visibility",
          [f"nonempty Secrets (hide before generation): {sec}"] if sec else ["all Secrets empty"])

    # V17 style handoff
    errs17 = []
    if not sb:
        errs17.append("no Style block in export/elevenlabs/sudowrite-style.md")
    else:
        lead = re.search(r"# Style — paste this block first.*?```text\n(.*?)\n```", paste, re.S)
        if not lead or lead.group(1).strip() != sb:
            errs17.append("paste sheet does not lead with the identical Style block")
        if package and (package / "sudowrite" / "style.txt").exists() and lab.read(package / "sudowrite" / "style.txt").strip() != sb:
            errs17.append("style.txt differs")
        for must in ("original designed voices", "nonverbal", "narration untagged"):
            if must not in sb:
                errs17.append(f"Style block lacks: {must}")
    R.add("V17", "fail" if errs17 else "pass", "block", "Style handoff", errs17)

    # V18 performance freshness and settings
    errs18 = []
    for stem, p in sheets.items():
        t = lab.read(p)
        m = re.search(r"Source voice fields SHA-256[^`]*`([0-9a-f]{64})`", t)
        if stem in chars:
            want = voice_hash(chars[stem]["fields"])
            if not m:
                errs18.append(f"{stem}: no source hash (run stamp-sheets after reviewing the sheet)")
            elif m.group(1) != want:
                errs18.append(f"{stem}: stale (card voice fields changed since the sheet was reviewed)")
        for pct, api in re.findall(r"\*\*(\d+)%\*\* \(API `([0-9.]+)`\)", t):
            if abs(int(pct) / 100 - float(api)) > 1e-9:
                errs18.append(f"{stem}: {pct}% ≠ API {api}")
    R.add("V18", "fail" if errs18 else "pass", "block", "Performance freshness and settings", errs18)

    attested("V19", "Voice and pronunciation claims")
    R.add("V20", "not_applicable", "block", "Audio turn handoff", ["no derived turn list in this release"])

    # V21 findings and provenance
    ledger = proj / "research" / "qa" / "resolutions.md"
    open_p0 = []
    if ledger.exists():
        for line in lab.read(ledger).splitlines():
            cells = [x.strip() for x in line.strip("|").split("|")]
            if len(cells) >= 3 and re.search(r"P0", cells[0]) and not re.match(r"(applied|rejected)", cells[2]):
                open_p0.append(f"{cells[0]}: {cells[2]}")
    R.add("V21", "fail" if open_p0 or not ledger.exists() else "pass", "block", "Findings and provenance",
          open_p0 or ["no open P0 in research/qa/resolutions.md; promotions are author decisions (research/qa/promotions.md)"])

    # V22–V25 depend on a built package
    if package:
        need = ["00-START-HERE.md", "01-INDEX.md", "CHANGELOG.md", "manifest.json", "sudowrite/characters.csv",
                "sudowrite/worldbuilding.csv", "sudowrite/paste.md", "sudowrite/style.txt", "sudowrite/scene-setup.md",
                "performance/pronunciation.tsv", "performance/voice-map.example.json", "performance/test-results.csv",
                "reference/sources-and-claims.jsonl", "reference/coverage.md"]
        missing = [n for n in need if not (package / n).exists()]
        R.add("V22", "fail" if missing else "pass", "block", "Package integrity", [f"missing {missing}"] if missing else ["layout complete"])
        R.add("V23", "pass" if (package / "CHANGELOG.md").exists() else "fail", "block", "Changelog and supporting views")
        rows = list(csv.DictReader(io.StringIO(lab.read(package / "performance" / "test-results.csv")))) \
            if (package / "performance" / "test-results.csv").exists() else []
        st = "warn" if all(r["outcome"] == "not_run" for r in rows) else "pass"
        R.add("V24", st, "warn", "Runtime evidence", ["statically validated; runtime untested"] if st == "warn" else [])
    for cid, title in (("V22", "Package integrity"), ("V23", "Changelog and supporting views"), ("V24", "Runtime evidence")):
        if not any(r["check_id"] == cid for r in R.items):
            R.add(cid, "not_applicable", "block", title, ["no package yet"])
    if phase == "final":
        attested("V25", "Final acceptance and publication")
    else:
        R.add("V25", "not_applicable", "block", "Final acceptance and publication", ["candidate phase"])
    return R, snapshot, cards


def write_validation(proj, R, snapshot, phase, out=None):
    out = out or proj / "research" / "qa" / "validation.json"
    data = {"phase": phase, "checked_at": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"), "snapshot": snapshot,
            "blocking_failures": [r["check_id"] for r in R.blocking()], "results": R.items}
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in R.items:
        mark = {"pass": "✓", "fail": "✗", "warn": "⚠", "not_applicable": "·"}[r["status"]]
        print(f"{mark} {r['check_id']} {r['title']} [{r['status']}/{r['severity']}]"
              + (f" — {r['evidence'][0]}" if r["evidence"] else ""))
    return data


def cmd_validate(args):
    proj = lab.project_dir(args.slug)
    R, snapshot, _ = check_all(proj, args.phase)
    data = write_validation(proj, R, snapshot, args.phase)
    print(f"blocking failures: {data['blocking_failures'] or 'none'}")
    sys.exit(2 if data["blocking_failures"] else 0)


def cmd_stamp(args):
    proj = lab.project_dir(args.slug)
    cards = load_cards(proj)
    for p in sorted((proj / "export" / "elevenlabs").glob("*.md")):
        if p.name == "sudowrite-style.md" or p.stem not in cards:
            continue
        t = lab.read(p)
        line = (f"> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): "
                f"`{voice_hash(cards[p.stem]['fields'])}` — reviewed {dt.date.today()}: {args.reviewed}")
        t = re.sub(r"^> Source voice fields SHA-256.*$\n?", "", t, flags=re.M)
        t = re.sub(r"^(# .+\n\n)", r"\1" + line.replace("\\", "\\\\") + "\n", t, count=1)
        p.write_text(t, encoding="utf-8")
        print("stamped", p.name)


def pronunciation_rows(cards):
    rows = []
    for stem in CAST_ORDER:
        at = cards[stem]["fields"].get("Audio Tags", "")
        m = re.search(r"Pronunciation guide \(provisional, untested\): (.*?)(?:\. Not as default|\.$)", at)
        if not m:
            continue
        for pm in re.finditer(r"([^,;/()]+?)\s+(/[^/]+/)\s*(\([^)]*\))?", m.group(1)):
            rows.append([cards[stem]["fields"]["Name"], pm.group(1).strip(), pm.group(2), (pm.group(3) or "").strip("() "),
                         "provisional, untested"])
    return rows


def field_diff(old_dir, cards):
    lines = []
    for stem, c in cards.items():
        old = old_dir / c["sub"] / f"{stem}.md"
        if not old.exists():
            lines.append(f"- **{c['fields']['Name']}**: new card")
            continue
        of = lab.sw_fields(lab.read(old))
        for k in sorted(set(of) | set(c["fields"])):
            if of.get(k, "") != c["fields"].get(k, ""):
                lines.append(f"- **{c['fields']['Name']} › {k}**: {'added' if k not in of else 'removed' if k not in c['fields'] else 'changed'}")
    return lines


def mentions(cards, name_variants):
    hits = []
    for stem in WORLD_ORDER:
        if stem in cards and any(v in cards[stem]["fields"].get("Description", "") for v in name_variants):
            hits.append(cards[stem]["fields"]["Name"])
    return hits


def cmd_build(args):
    proj = lab.project_dir(args.slug)
    R, snapshot, cards = check_all(proj, "candidate")
    pre_block = R.blocking()
    if pre_block and not args.draft:
        write_validation(proj, R, snapshot, "candidate")
        sys.exit(f"blocking checks failed: {[r['check_id'] for r in pre_block]} (use --draft for a non-release candidate)")
    deliv = proj / "delivery"
    deliv.mkdir(exist_ok=True)
    prev = sorted(p for p in deliv.glob(f"{args.slug}-{BASELINE}-r*") if not p.name.endswith("-draft"))
    rev = f"r{len(prev) + 1:02d}"
    pkg = deliv / f"{args.slug}-{BASELINE}-{rev}{'-draft' if args.draft else ''}"
    if pkg.exists():
        sys.exit(f"{pkg} exists; releases are never overwritten")
    exp = proj / "export"
    (pkg / "sudowrite" / "cards").mkdir(parents=True)
    for f in ("characters.csv", "worldbuilding.csv"):
        shutil.copy2(exp / f, pkg / "sudowrite" / f)
    for f in (exp / "cards").glob("*.csv"):
        shutil.copy2(f, pkg / "sudowrite" / "cards" / f.name)
    shutil.copy2(exp / "sudowrite-paste.md", pkg / "sudowrite" / "paste.md")
    (pkg / "sudowrite" / "style.txt").write_text(style_block(proj) + "\n", encoding="utf-8")
    reg = json.loads(lab.read(proj / "research" / "qa" / "registry.json"))
    status_lines = ["| Member | State at 2026-09-30 | Debut | Graduated | Regular activities concluded |", "|---|---|---|---|---|"]
    for c in reg["cast"]:
        si = c["status_interval"]
        status_lines.append(f"| {c['name']} | {si['state_at_baseline']} | {si['debut'] or '—'} | {si['graduated'] or '—'} | {si['regular_activities_concluded'] or '—'} |")
    (pkg / "sudowrite" / "scene-setup.md").write_text(SCENE_SETUP.format(table="\n".join(status_lines)), encoding="utf-8")
    (pkg / "performance" / "sheets").mkdir(parents=True)
    for p in (exp / "elevenlabs").glob("*.md"):
        shutil.copy2(p, pkg / "performance" / "sheets" / p.name)
    with open(pkg / "performance" / "pronunciation.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["character", "term", "ipa", "note", "status"])
        w.writerows(pronunciation_rows(cards))
    (pkg / "performance" / "voice-map.example.json").write_text(json.dumps(
        {"_about": "Example only: map each character to an ORIGINAL designed voice you created (never a clone).",
         "narrator": "<your narrator voice_id>",
         **{cards[s]["fields"]["Name"]: "<original designed voice_id>" for s in CAST_ORDER}}, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(pkg / "performance" / "test-results.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["test", "release", "date", "tester", "model_or_voice", "settings", "observations", "outcome"])
        for t in ("sudowrite-import", "sudowrite-generation", "elevenlabs-3-line"):
            w.writerow([t, rev, "", "", "", "", "", "not_run"])
    (pkg / "reference" / "bible").mkdir(parents=True)
    for sub in ("characters", "world"):
        shutil.copytree(proj / "bible" / sub, pkg / "reference" / "bible" / sub)
    with open(pkg / "reference" / "sources-and-claims.jsonl", "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"_about": "Registry facts (non-exhaustive); the bible files are canonical.", "non_exhaustive": True}, ensure_ascii=False) + "\n")
        for k in ("cast", "units", "credits", "events"):
            for item in reg[k]:
                fh.write(json.dumps({"kind": k, **item}, ensure_ascii=False) + "\n")
    cov = ["# Coverage (generated)", "", "| Member | Relationships words | Quoted lines in Dialogue Style | Open questions | World cards naming her |", "|---|---|---|---|---|"]
    idx = ["# Index", "", f"Release {rev} · baseline {BASELINE} · 18 characters · 24 world elements · full cards (no compact variants).", "",
           "## Characters (Myth → Promise/Council → Advent → Justice)", "", "| Member | Status | Units (Groups) | Card | Performance sheet | World cards naming her |", "|---|---|---|---|---|---|"]
    for stem in CAST_ORDER:
        c = cards[stem]
        f = c["fields"]
        first = f["Name"].split()[0]
        wc = mentions(cards, [f["Name"], first])
        si = next(x["status_interval"] for x in reg["cast"] if x["name"] == f["Name"])
        status = si["state_at_baseline"] + (f" (graduated {si['graduated']})" if si["graduated"] else "") + \
            (f" (regular activities concluded {si['regular_activities_concluded']})" if si["regular_activities_concluded"] else "")
        idx.append(f"| {f['Name']} | {status} | {f.get('Groups', '')} | `reference/bible/characters/{stem}.md` | `performance/sheets/{stem}.md` | {', '.join(wc) or '—'} |")
        oq = c["text"].split("## Open Questions")[-1] if "## Open Questions" in c["text"] else ""
        n_oq = len(re.findall(r"^\d+\. ", oq, re.M))
        n_q = f.get("Dialogue Style", "").count(chr(34)) // 2
        cov.append(f"| {f['Name']} | {lab.count_words(f.get('Relationships', ''))} | {n_q} | {n_oq} | {len(wc)} |")
    idx += ["", "## World elements (premise → units → relationships → events)", ""]
    idx += [f"- {cards[s]['fields']['Name']} — `reference/bible/world/{s}.md`" for s in WORLD_ORDER if s in cards]
    (pkg / "01-INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    (pkg / "reference" / "coverage.md").write_text("\n".join(cov) + "\n", encoding="utf-8")
    if prev:
        diff = field_diff(prev[-1] / "reference" / "bible", cards)
        ch = [f"# Changelog — {rev}", "", f"Field-level changes since {prev[-1].name}:", ""] + (diff or ["- none"])
    else:
        ch = [f"# Changelog — {rev}", "", "Initial release: 18 character cards and 24 world elements (all new)."]
    (pkg / "CHANGELOG.md").write_text("\n".join(ch) + "\n", encoding="utf-8")
    (pkg / "00-START-HERE.md").write_text(START_HERE.format(rev=rev, baseline=BASELINE,
                                                            draft="（草稿候選版，尚未通過全部檢查）" if args.draft else ""), encoding="utf-8")
    R2, snapshot2, _ = check_all(proj, "candidate", package=pkg)
    val = write_validation(proj, R2, snapshot2, "candidate", out=pkg / "validation.json")
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    dirty = bool(subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"], capture_output=True, text=True).stdout.strip())
    files = {str(p.relative_to(pkg)): sha(p.read_bytes()) for p in sorted(pkg.rglob("*")) if p.is_file() and p.name != "manifest.json"}
    ledger = lab.read(proj / "research" / "qa" / "resolutions.md")
    manifest = {"release": rev, "draft": args.draft, "baseline": BASELINE,
                "built_at": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"), "commit": commit, "dirty_worktree": dirty,
                "snapshot": snapshot2, "counts": {"characters": 18, "world": 24, "sheets": 18},
                "promotion": "author decisions (research/qa/promotions.md); GPT reviewed each card one round; not GPT approval",
                "unresolved_findings": [l.split("|")[1].strip() for l in ledger.splitlines() if "| pending" in l or "| deferred" in l],
                "runtime_tests": "not_run (statically validated; runtime untested)",
                "validation": {"blocking_failures": val["blocking_failures"]}, "files": files}
    (pkg / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"✓ {pkg.relative_to(ROOT.parent)} (manifest sha256 {sha((pkg / 'manifest.json').read_bytes())[:16]})")


SCENE_SETUP = """# Scene setup and date worksheet

Every scene: give Sudowrite the scene date, name every participant explicitly, and name the world elements
that matter (for example FUWAMOCO, Serendipity). Detection underlines show which cards Sudowrite recognized;
recognition does not guarantee every trait is used.

The cards describe the cast at the 2026-09-30 baseline. For a scene set earlier, state the date and each
member's status at that date in the scene text, and mute later facts in a project copy before generating.
This worksheet does not change Sudowrite's context by itself.

{table}
"""

START_HERE = """# 從這裡開始 — holoen {rev}{draft}

基準日 {baseline}。這一版有 **18 張角色卡**、**24 張世界觀卡**、18 份 ElevenLabs 表演表。全部用完整卡（沒有精簡版）。
狀態：**靜態檢查通過與否見 `validation.json`；實際匯入和配音測試尚未執行（runtime untested）。**
索引：`01-INDEX.md`。改動：`CHANGELOG.md`。檔案雜湊與狀態：`manifest.json`。

## 1. 十分鐘匯入測試（請在新的、可丟棄的專案做）
1. 新建專案 `holoen-{rev}-smoke`。不要在你正在寫的專案裡測重複匯入。
2. Story Bible → Characters 標題旁 `•••` → Import → 上傳 `sudowrite/characters.csv`，確認 **18 張**。
   Worldbuilding 同樣匯入 `sudowrite/worldbuilding.csv`，確認 **24 個**。每個合併 CSV 只匯入一次。
3. 打開 Fuwawa、Mococo 和另一個角色：雙胞胎是兩張卡、`Role` 是 Protagonist、自訂特質（含 `Audio Tags`）有內容。
   找一個多行或有標點的欄位，和 `sudowrite/paste.md` 對照。打開 FUWAMOCO 和一張 History 卡。
4. 確認 Secrets 都是空的（這一版全空；以後若有內容，生成前要先按眼睛圖示隱藏）。
5. 把 `sudowrite/style.txt` 貼到 Style。測試用：Genre 填 `Light comic fantasy`，Braindump 填
   `Fuwawa Abyssgard and Mococo Abyssgard compare a map inside a fictional game.`，Synopsis 留白；設定第三人稱、過去式。
6. 新建一個章節／場景：`Scene date: 2026-09-30. Fuwawa Abyssgard and Mococo Abyssgard, the members of FUWAMOCO,
   compare a map inside a fictional game. Keep their speaking turns distinct.`
7. 看兩人和 FUWAMOCO 有沒有出現偵測底線；沒有就記下來，檢查名稱與可見性後再試。
8. 生成最短的一段：說話者分得開、對白有可用的表演標籤、敘述沒有標籤。把匯入和生成的結果分開記在
   `performance/test-results.csv`（含版本 {rev} 和使用的模型）。有問題就保留這個測試專案方便排查。

## 2. 三行原創聲音測試（ElevenLabs v4）
用兩個**你自己設計的原創聲音**（不要複製或模仿成員的真實聲音），A/B/A 輪流。以下是風格示範，不是引用：
```text
A: [calm] We can check the map again.
B: [startled] Ah! That door moved.
A: [laughs] Fuwawa, Mococo—your turn.
```
選 `eleven_v4`，用對應表演表的起始設定（UI 用百分比，API 用小數）。每行一個 turn、各自指定聲音。
聽：聲音分配對不對、語氣有沒有變、標籤有沒有被唸出來、笑聲有沒有重複、名字發音。
要測 IPA 的話，在另一份音訊稿裡**直接取代**那個名字，不要再附加一次發音。結果寫具體觀察，不要寫「全部通過」。

## 3. 寫作與歷史場景
每個場景寫明日期、登場的人（全名）、相關的世界觀元素。寫過去的時間點時，參考 `sudowrite/scene-setup.md`
的狀態表，並在專案副本裡先拿掉之後才發生的事。

## 4. 更新與回報
之後的版本請照 `CHANGELOG.md` 逐欄更新既有卡片（保留你自己的修改）；不要假設重複匯入 CSV 會合併。
回報問題時附：版本號、哪張卡哪個欄位、測試結果、最小重現步驟。測試紀錄放在發佈資料夾外面。
"""


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate"); v.add_argument("slug"); v.add_argument("--phase", choices=["candidate", "final"], default="candidate")
    s = sub.add_parser("stamp-sheets"); s.add_argument("slug"); s.add_argument("--reviewed", required=True)
    b = sub.add_parser("build"); b.add_argument("slug"); b.add_argument("--draft", action="store_true")
    a = ap.parse_args()
    {"validate": cmd_validate, "stamp-sheets": cmd_stamp, "build": cmd_build}[a.cmd](a)


if __name__ == "__main__":
    main()

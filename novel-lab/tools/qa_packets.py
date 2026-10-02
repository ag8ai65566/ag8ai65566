#!/usr/bin/env python3
"""Build the shared QA registry and per-cohort audit packets for a project.

Usage: python3 novel-lab/tools/qa_packets.py holoen

Writes projects/<slug>/research/qa/registry.json and research/qa/packets/<cohort>.md.
Packets are focus aids for GPT's cross-card audits (GPT can still open any file): each holds the
cohort's consistency-relevant [SW] fields, its dossier timelines and hard facts, and every sentence in
other files' [SW] fields that names a cohort member ("incoming claims"), each with a file › field locator.
Personality, Motivation and the voice fields (Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags) are
audited separately; the auditor can open them in the bible files.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = 55000  # soft cap per packet; GPT reads packets as files, so ~45k (consult) is a target, not a limit

COHORTS = {
    # Myth is split in two so each packet stays under the cap.
    "myth1": {
        "characters": ["Mori-Calliope", "Takanashi-Kiara", "Ninomae-Inanis"],
        "world": ["TakaMori", "TakoTori", "Myth-and-Kronii-Other-Pairs"],
    },
    "myth2": {
        "characters": ["Gawr-Gura", "Watson-Amelia"],
        "world": ["hololive--Myth", "AmeSame", "Bone-Bros"],
    },
    "promise": {
        "characters": ["Ouro-Kronii", "IRyS", "Ceres-Fauna", "Nanashi-Mumei"],
        "world": ["hololive--Promise", "Time-Duo", "Time-and-Death", "OctoClock", "Fauna-and-Mumei-Pairs",
                  "IRyS-and-Nerissa-Pairs"],
    },
    "advent": {
        "characters": ["Shiori-Novella", "Koseki-Bijou", "Nerissa-Ravencroft", "Fuwawa-Abyssgard", "Mococo-Abyssgard"],
        "world": ["hololive--Advent", "Advent-Pairs", "FUWAMOCO"],
    },
    "justice": {
        "characters": ["Elizabeth-Rose-Bloodflame", "Gigi-Murin", "Cecilia-Immergreen", "Raora-Panthera"],
        "world": ["hololive--Justice", "Justice-Pairs"],
    },
    "global": {
        "characters": [],
        "world": ["hololive", "Streaming-Life", "VTuber-Persona-and-Lore", "Cross-Branch-Friends",
                  "Concerts-and-Live-Events", "hololive-History-2023-2026", "hololive-History-to-2022"],
    },
}

# Short names a sentence may use for a member (word-boundary match). Kept conservative to avoid noise.
SHORT = {
    "Mori-Calliope": ["Calli", "Calliope", "Mori"], "Takanashi-Kiara": ["Kiara"],
    "Ninomae-Inanis": ["Ina", "Ina'nis"], "Gawr-Gura": ["Gura"], "Watson-Amelia": ["Ame", "Amelia"],
    "Ouro-Kronii": ["Kronii"], "IRyS": ["IRyS"], "Ceres-Fauna": ["Fauna"], "Nanashi-Mumei": ["Mumei"],
    "Shiori-Novella": ["Shiori"], "Koseki-Bijou": ["Bijou", "Biboo"], "Nerissa-Ravencroft": ["Nerissa"],
    "Fuwawa-Abyssgard": ["Fuwawa", "FUWAMOCO"], "Mococo-Abyssgard": ["Mococo", "FUWAMOCO"],
    "Elizabeth-Rose-Bloodflame": ["Elizabeth", "Liz"], "Gigi-Murin": ["Gigi"],
    "Cecilia-Immergreen": ["Cecilia"], "Raora-Panthera": ["Raora"],
}
UNIT_WORDS = {"myth2": ["Myth"], "promise": ["Promise", "Council"], "advent": ["Advent"], "justice": ["Justice"]}

CONSISTENCY_FIELDS = ["Groups", "Other Names", "Background", "Relationships", "Description", "Rules"]
DOSSIER_SECTIONS = ["Background Timeline", "History", "Timeline", "Hard Facts (continuity)", "Members and Status"]

# Official units confirmed in this project's sources (keep in sync with project.md "已定案的硬設定").
UNITS = [
    {"unit": "hololive -Myth-", "members": ["Mori Calliope", "Takanashi Kiara", "Ninomae Ina'nis", "Gawr Gura", "Watson Amelia"], "evidence": "official"},
    {"unit": "hololive -Promise- (from 2023-10; earlier Council and Project: HOPE)", "members": ["IRyS", "Ouro Kronii", "Hakos Baelz", "Ceres Fauna", "Nanashi Mumei"], "evidence": "official"},
    {"unit": "hololive -Advent-", "members": ["Shiori Novella", "Koseki Bijou", "Nerissa Ravencroft", "Fuwawa Abyssgard", "Mococo Abyssgard"], "evidence": "official"},
    {"unit": "hololive -Justice-", "members": ["Elizabeth Rose Bloodflame", "Gigi Murin", "Cecilia Immergreen", "Raora Panthera"], "evidence": "official"},
    {"unit": "Last Writes", "members": ["Mori Calliope", "Shiori Novella"], "evidence": "official Serendipity billing, 2026"},
    {"unit": "Octo'clock", "members": ["Ninomae Ina'nis", "Ouro Kronii"], "evidence": "official Serendipity billing, 2026"},
    {"unit": "Rocku Wawa", "members": ["Takanashi Kiara", "Koseki Bijou"], "evidence": "official Serendipity billing, 2026"},
    {"unit": "BaeRyS", "members": ["Hakos Baelz", "IRyS"], "evidence": "official Serendipity billing, 2026"},
    {"unit": "Bloodraven", "members": ["Nerissa Ravencroft", "Elizabeth Rose Bloodflame"], "evidence": "official Serendipity billing, 2026"},
    {"unit": "B.F.F", "members": ["Fuwawa Abyssgard", "Mococo Abyssgard", "Raora Panthera"], "evidence": "official Serendipity billing, 2026"},
    {"unit": "Autofister (also CCGG)", "members": ["Gigi Murin", "Cecilia Immergreen"], "evidence": "official Serendipity billing and shop, 2026"},
    {"unit": "LYRA", "members": ["Amane Kanata", "Koganei Niko", "Mori Calliope", "Ayunda Risu", "Elizabeth Rose Bloodflame"], "evidence": "mix engineer's credits (a remix-version cover of \"III\")"},
]

# Directional credits worth checking across cards (who made what for whom). Evidence as recorded in the cards.
CREDITS = [
    {"work": "LYRA \"III\" remix-version cover", "credited": ["Amane Kanata", "Koganei Niko", "Mori Calliope", "Ayunda Risu", "Elizabeth Rose Bloodflame"], "role": "vocals", "evidence": "mix engineer's credits (foriio 2122478)"},
    {"work": "Cecilia's debut stream", "credited": ["Raora Panthera"], "role": "ending screen and sweeping-scene art", "evidence": "archived debut credits p_ZQs-kgUKI"},
    {"work": "Cecilia's debut stream", "credited": ["nullrefrepro"], "role": "chat-game implementation", "evidence": "archived debut credits p_ZQs-kgUKI"},
    {"work": "Raora's debut stream", "credited": ["Cecilia Immergreen"], "role": "ending-screen and mascot-stinger animation", "evidence": "archived debut credits JW7j8tKMOfY"},
    {"work": "CCGG MADNESS", "credited": ["Cecilia Immergreen"], "role": "lyrics, direction, vocals", "evidence": "archived MV credits bTxEGwMOQQI"},
    {"work": "CCGG MADNESS", "credited": ["Gigi Murin"], "role": "vocals, lyrics help, chibi-model design", "evidence": "archived MV credits bTxEGwMOQQI"},
    {"work": "CCGG MADNESS", "credited": ["Nerissa Ravencroft"], "role": "lyrics help", "evidence": "archived MV credits bTxEGwMOQQI"},
    {"work": "Mephisto (duet cover)", "credited": ["Elizabeth Rose Bloodflame", "Banzoin Hakka"], "role": "vocals; Elizabeth produced and arranged", "evidence": "archived credits jqFPgcMt_Jo"},
    {"work": "Bright Tonight", "credited": ["IRyS", "Ouro Kronii", "Fuwawa Abyssgard", "Mococo Abyssgard", "Gigi Murin"], "role": "vocals (group release 2025-12-22)", "evidence": "official music page 685"},
    {"work": "Into The Void (non-canon motion comic)", "credited": ["Shiori Novella", "Elizabeth Rose Bloodflame", "Gigi Murin", "Nerissa Ravencroft", "Mori Calliope (episode 2)"], "role": "voice cast", "evidence": "archived episode credits"},
    {"work": "Wind-Up", "credited": ["Cecilia Immergreen"], "role": "composition and lyrics, with production help from Aethoro", "evidence": "creator interview (Siliconera)"},
    {"work": "enough", "credited": ["Gigi Murin", "FLAVORFOLEY"], "role": "vocals; composition, arrangement and mixing by FLAVORFOLEY", "evidence": "archived MV credits 3m15lUh0WP4"},
]
# People outside the 18-member cast who appear in relationship claims (reference only: no cards).
REFERENCE_ONLY = ["Hakos Baelz", "Tsukumo Sana", "Kobo Kanaeru", "Vestia Zeta", "Kureiji Ollie", "Kaela Kovalskia",
                  "Moona Hoshinova", "Ayunda Risu", "Anya Melfissa", "Pavolia Reine", "Airani Iofifteen",
                  "Ookami Mio", "Tsunomaki Watame", "Oozora Subaru", "Houshou Marine", "Inugami Korone",
                  "Omaru Polka", "Momosuzu Nene", "Kazama Iroha", "Roboco", "Tokino Sora", "Yuzuki Choco",
                  "Nekomata Okayu", "Shirakami Fubuki", "Hakui Koyori", "Akai Haato", "Hoshimachi Suisei",
                  "Usada Pekora", "Shiranui Flare", "AZKi", "Amane Kanata", "Natsuiro Matsuri", "Ichijou Ririka",
                  "Koganei Niko", "Hiodoshi Ao", "Machina X Flayon", "Jurard T Rexford", "Crimzon Ruze",
                  "Gavis Bettel", "Banzoin Hakka", "Josuiji Shinri", "Arurandeisu", "Astel Leda", "Octavio",
                  "Regis Altare", "Rikka", "Shirogane Noel"]

DATE = re.compile(r"^(?P<d>\d{4}(?:-\d{2}(?:-\d{2})?)?)(?P<rest>[^|]*)$")


def date_info(raw):
    raw = raw.strip()
    m = DATE.match(raw)
    if not m:
        return {"precision": "lore" if raw.lower().startswith("lore") else "other", "zone": None}
    d, rest = m.group("d"), m.group("rest")
    prec = {4: "year", 7: "month", 10: "day"}[len(d)]
    if re.search(r"[/–]", rest):
        prec += "-range"
    zone = re.search(r"\b(PDT|PST|EDT|EST|JST|UTC|WIB|AEST|BST|CEST)\b", rest)
    return {"precision": prec, "zone": zone.group(1) if zone else None}


SW = re.compile(r"^## \[SW\] (.+?)\n(.*?)(?=\n## |\n---|\Z)", re.S | re.M)
SEC = re.compile(r"^## (?!\[SW\])(.+?)\n(.*?)(?=\n## |\Z)", re.S | re.M)
SENT = re.compile(r"(?<=[.!?\"”])\s+(?=[A-Z\"“(])")


def front_name(text):
    m = re.search(r'^name:\s*"?(.*?)"?\s*$', text, re.M)
    return m.group(1) if m else None


def load(proj):
    files = {}
    for sub in ("characters", "world"):
        for f in sorted((proj / "bible" / sub).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            sw = {m.group(1).strip(): m.group(2).strip() for m in SW.finditer(text)}
            sec = {m.group(1).strip(): m.group(2).strip() for m in SEC.finditer(text.split("\n## [SW] Name")[0])}
            files[f.stem] = {"path": f"bible/{sub}/{f.name}", "kind": sub, "name": front_name(text), "sw": sw,
                             "sec": sec, "text": text, "sha256": hashlib.sha256(text.encode()).hexdigest()}
    return files


def iso(d):
    """'May 1, 2025' → '2025-05-01'; ISO dates pass through."""
    import datetime
    try:
        return datetime.datetime.strptime(d, "%B %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return d


def split_list(s):
    return [x.strip() for x in re.split(r",\s*", s or "") if x.strip()]


def table_rows(block):
    rows = []
    for line in (block or "").splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line) and not re.match(r"^\|\s*(Date|Person|Word)\s*\|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and re.match(r"^(\d{4}|Lore|19|20)", cells[0]):
                rows.append(cells)
    return rows


def build_registry(files, commit):
    reg = {"_schema": "registry v2: cast status intervals, world aliases, official units, directional credits, "
                      "reference-only people, events with date precision and zone (from dossier tables), alias "
                      "collisions. Bounded and non-exhaustive: the bible files stay canonical.",
           "baseline": "2026-09-30", "commit": commit, "files": {}, "cast": [], "world": [], "units": UNITS,
           "credits": CREDITS, "reference_only": REFERENCE_ONLY, "aliases": {}, "events": []}
    for stem, d in files.items():
        reg["files"][d["path"]] = d["sha256"]
        sw = d["sw"]
        if d["kind"] == "characters":
            bg = sw.get("Background", "")
            status = re.split(r"(?<=\.)\s", bg, maxsplit=2)[:2]
            debut = re.search(r"\bdebuted\b[^.]*?\bon (\d{4}-\d{2}-\d{2})", bg)
            when = r"([A-Z][a-z]+ \d{1,2}, \d{4}|\d{4}-\d{2}-\d{2})"
            grad = re.search(r"graduated (?:from [^.;:]+? )?on " + when, bg)
            concluded = re.search(r"concluded her regular activities on " + when, bg)
            state = "graduated" if grad else "affiliate" if "affiliate" in bg[:300] else "active"
            reg["cast"].append({"name": d["name"], "file": d["path"], "other_names": split_list(sw.get("Other Names")),
                                "groups": split_list(sw.get("Groups")), "status": " ".join(status),
                                "status_interval": {"state_at_baseline": state,
                                                    "debut": debut.group(1) if debut else None,
                                                    "graduated": iso(grad.group(1)) if grad else None,
                                                    "regular_activities_concluded": iso(concluded.group(1)) if concluded else None,
                                                    "source": f"{d['path']} › Background"}})
        else:
            reg["world"].append({"name": d["name"], "file": d["path"], "role": sw.get("Role"),
                                 "other_names": split_list(sw.get("Other Names"))})
        for alias in [d["name"]] + split_list(sw.get("Other Names")):
            reg["aliases"].setdefault(alias.lower(), []).append(d["name"])
        for key in ("Background Timeline", "History", "Timeline"):
            for cells in table_rows(d["sec"].get(key)):
                reg["events"].append({"date": cells[0], **date_info(cells[0]), "text": cells[1] if len(cells) > 1 else "",
                                      "evidence": cells[2] if len(cells) > 2 else "", "file": d["path"], "section": key})
    reg["alias_collisions"] = {a: n for a, n in reg["aliases"].items() if len(set(n)) > 1}
    return reg


GENERIC = {"the", "liz", "cc", "ame"}  # aliases too ambiguous to match on their own (short names cover Ame)


def cohort_patterns(cohort, files):
    words = set()
    for stem in COHORTS[cohort]["characters"]:
        words |= set(SHORT.get(stem, []))
        d = files[stem]
        words.add(d["name"])
        words |= {a for a in split_list(d["sw"].get("Other Names")) if len(a) > 3 and a.lower() not in GENERIC}
        for u in UNITS:
            if d["name"] in u["members"]:
                words.add(re.sub(r"\s*\(.*", "", u["unit"]))
    words |= set(UNIT_WORDS.get(cohort, []))
    for stem in COHORTS[cohort]["world"]:  # owned world cards' names and aliases (ADVENT audit, CONSULT-R2-001)
        words.add(files[stem]["name"])
        words |= {a for a in split_list(files[stem]["sw"].get("Other Names")) if len(a) > 3 and a.lower() not in GENERIC}
    if not words:
        return None
    return re.compile(r"(?<![\w-])(" + "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True)) + r")(?![\w-])", re.I)


def dossier_items(text):
    """Table rows and (joined, multi-line) bullets from the dossier part of a bible file, with their section."""
    dossier = text.split("\n## [SW] Name")[0]
    out, section, bullet = [], None, None
    skip = {"Sources", "Merge Record", "Open Questions", "Glossary", "Sensory Palette"}
    for line in dossier.splitlines():
        h = re.match(r"^## (.+)", line)
        if h:
            section = h.group(1).split(" (")[0].strip()
            bullet = None
            continue
        if section is None or section in skip or section.startswith("Sources"):
            continue
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            out.append((section, line.strip()))
            bullet = None
        elif re.match(r"^\s*(- |\d+\. )", line):
            out.append((section, line.strip()))
            bullet = len(out) - 1
        elif bullet is not None and line.startswith("  ") and line.strip():
            out[bullet] = (out[bullet][0], out[bullet][1] + " " + line.strip())
        else:
            bullet = None
    return out


def packet(cohort, files, reg_path, commit):
    own = COHORTS[cohort]["characters"] + COHORTS[cohort]["world"]
    head = [f"# Audit packet: {cohort}", "",
            f"Snapshot: git {commit}. Registry: `{reg_path}`. Manifest: `projects/holoen/research/qa/manifest.json`.",
            "Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open",
            "any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).", "",
            "Owned files (sha256): " + "; ".join(f"`{files[x]['path']}` {files[x]['sha256'][:12]}" for x in own), ""]
    owned = ["## 1. Owned files (consistency fields, dossier timelines and hard facts)", ""]
    for stem in own:
        d = files[stem]
        owned.append(f"### {d['name']} — `{d['path']}`")
        for fld in CONSISTENCY_FIELDS:
            if d["sw"].get(fld):
                owned.append(f"**[SW] {fld}:** {d['sw'][fld]}")
        for key in DOSSIER_SECTIONS:
            if d["sec"].get(key):
                owned.append(f"**Dossier · {key}:**\n{d['sec'][key]}")
        owned.append("")
    incoming = []
    pat = cohort_patterns(cohort, files)
    if pat:
        incoming = ["## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)",
                    f"Matched names: {pat.pattern[13:-8].replace(chr(92), '')}", ""]
        for stem, d in files.items():
            if stem in own:
                continue
            hits = []
            for fld in CONSISTENCY_FIELDS:
                for sent in SENT.split(d["sw"].get(fld) or ""):
                    if pat.search(sent):
                        hits.append(f"- `{d['path']} › [SW] {fld}`: {sent.strip()}")
            for section, item in dossier_items(d["text"]):
                if pat.search(item):
                    hits.append(f"- `{d['path']} › {section}`: {item}")
            if hits:
                incoming += [f"### from {d['name']}"] + hits + [""]
    return head, owned, incoming


def write_packets(cohort, files, qa, reg_path, commit):
    head, owned, incoming = packet(cohort, files, reg_path, commit)
    whole = "\n".join(head + owned + incoming)
    if len(whole) <= CAP or not incoming:
        parts = {f"{cohort}.md": whole}
    else:  # deterministic split: owned material, then incoming claims; nothing is truncated
        parts = {f"{cohort}.md": "\n".join(head + owned + [f"Incoming claims continue in `{cohort}-incoming.md`."]),
                 f"{cohort}-incoming.md": "\n".join([f"# Audit packet: {cohort} (incoming claims)", "",
                                                      f"Snapshot: git {commit}.", ""] + incoming)}
    for old in (qa / "packets").glob(f"{cohort}*.md"):
        if old.name not in parts and old.name.split(".")[0] in (cohort, f"{cohort}-incoming"):
            old.unlink()
    out = []
    for name, text in parts.items():
        (qa / "packets" / name).write_text(text, encoding="utf-8")
        out.append({"packet": f"research/qa/packets/{name}", "chars": len(text),
                    "sha256": hashlib.sha256(text.encode()).hexdigest()})
    return out



REF_SHORT = {"Hakos Baelz": ["Bae", "Baelz"], "Kobo Kanaeru": ["Kobo"], "Vestia Zeta": ["Zeta"],
             "Kureiji Ollie": ["Ollie"], "Kaela Kovalskia": ["Kaela"], "Moona Hoshinova": ["Moona"],
             "Ayunda Risu": ["Risu"], "Anya Melfissa": ["Anya"], "Pavolia Reine": ["Reine"],
             "Airani Iofifteen": ["Iofi"], "Ookami Mio": ["Mio"], "Tsunomaki Watame": ["Watame"],
             "Oozora Subaru": ["Subaru"], "Houshou Marine": ["Marine"], "Inugami Korone": ["Korone"],
             "Omaru Polka": ["Polka"], "Nekomata Okayu": ["Okayu"], "Akai Haato": ["Haachama"],
             "Hoshimachi Suisei": ["Suisei"], "Usada Pekora": ["Pekora"], "Tokino Sora": ["Sora"],
             "Tsukumo Sana": ["Sana"], "Crimzon Ruze": ["Ruze"], "Banzoin Hakka": ["Hakka"],
             "Koganei Niko": ["Niko"], "Amane Kanata": ["Kanata"]}


def person_patterns(files):
    pats = {}
    for stem in qa_packets_cast(files):
        d = files[stem]
        words = {d["name"]} | set(SHORT.get(stem, [])) - {"FUWAMOCO"}
        pats[d["name"]] = re.compile(r"(?<![\w-])(" + "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True)) + r")(?![\w-])")
    for name in REFERENCE_ONLY:
        words = {name} | set(REF_SHORT.get(name, []))
        pats[name] = re.compile(r"(?<![\w-])(" + "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True)) + r")(?![\w-])")
    return pats


def qa_packets_cast(files):
    return [stem for stem, d in files.items() if d["kind"] == "characters"]


def all_claims(files):
    """Every [SW] sentence (consistency fields) and dossier row/bullet, with locator."""
    for stem, d in files.items():
        for fld in CONSISTENCY_FIELDS:
            for sent in SENT.split(d["sw"].get(fld) or ""):
                if sent.strip():
                    yield f"{d['path']} › [SW] {fld}", sent.strip()
        for section, item in dossier_items(d["text"]):
            yield f"{d['path']} › {section}", item


def bridge_packets(files, reg, qa, commit):
    out = {}
    # events: registry rows grouped by month, plus status intervals
    ev = ["# Bridge packet: events", "", f"Snapshot: git {commit}. Every dated row from every bible file's dossier",
          "tables (registry events), grouped by month; then each cast member's status interval. Locators are files;",
          "search the file for the row text to see its context.", "", "## Status intervals (from Background)", ""]
    for c in reg["cast"]:
        si = c["status_interval"]
        ev.append(f"- {c['name']}: {si['state_at_baseline']}; debut {si['debut'] or '?'}; graduated {si['graduated'] or '—'}; "
                  f"regular activities concluded {si['regular_activities_concluded'] or '—'} (`{si['source']}`)")
    ev += ["", "## Dated rows by month", ""]
    by = {}
    for e in reg["events"]:
        key = e["date"][:7] if re.match(r"\d{4}-\d{2}", e["date"]) else (e["date"][:4] if re.match(r"\d{4}", e["date"]) else "undated/lore")
        by.setdefault(key, []).append(e)
    for key in sorted(by):
        ev.append(f"### {key}")
        for e in by[key]:
            ev.append(f"- {e['date']} [{e['precision']}{', ' + e['zone'] if e['zone'] else ''}] {e['text']} — `{e['file']}`"
                      + (f" ({e['evidence']})" if e["evidence"] else ""))
        ev.append("")
    out["events.md"] = "\n".join(ev)
    # ties: claims naming two people, grouped by pair
    pats = person_patterns(files)
    cast_names = {files[s]["name"] for s in qa_packets_cast(files)}
    pairs, groups = {}, {}
    for loc, text in all_claims(files):
        who = sorted(n for n, p in pats.items() if p.search(text))
        if len(who) > 3:  # group claims appear once, not under every pair
            if any(w in cast_names for w in who):
                groups[f"- `{loc}` [{', '.join(who)}]: {text}"] = True
            continue
        for i in range(len(who)):
            for j in range(i + 1, len(who)):
                a, b = who[i], who[j]
                if a in cast_names or b in cast_names:
                    pairs.setdefault((a, b), []).append(f"- `{loc}`: {text}")
    for name, sel in (("ties-cast.md", lambda a, b: a in cast_names and b in cast_names),
                      ("ties-external.md", lambda a, b: not (a in cast_names and b in cast_names))):
        lines = [f"# Bridge packet: ties ({'cast × cast' if name == 'ties-cast.md' else 'cast × reference-only people'})", "",
                 f"Snapshot: git {commit}. Every [SW] sentence and dossier row/bullet that names both people, grouped by",
                 "pair (names and short names matched; a sentence naming three people appears under each pair).", ""]
        for (a, b) in sorted(k for k in pairs if sel(*k)):
            lines.append(f"### {a} × {b}")
            lines += sorted(set(pairs[(a, b)]))
            lines.append("")
        out[name] = "\n".join(lines)
    out["ties-groups.md"] = "\n".join(["# Bridge packet: ties (claims naming four or more people)", "",
                                        f"Snapshot: git {commit}. Each listed once with the people it names.", ""] + sorted(groups))
    res = []
    for name, text in out.items():
        (qa / "packets" / name).write_text(text, encoding="utf-8")
        res.append({"packet": f"research/qa/packets/{name}", "chars": len(text), "sha256": hashlib.sha256(text.encode()).hexdigest()})
        print(f"bridge {name}: {len(text):,} chars")
    return res

PROMOTIONS_HEAD = """# Promotion provenance (holoen)

Every promotion into `bible/` is an **author decision** recorded by `lab.py promote` (the author's standing rule:
GPT reviews each card one round only, then the author decides). This is not GPT approval and not source
verification; the evidence level of each claim stays as labeled in the card. Exported from
`runs/*/author-decision.md`, newest runs last.
"""


def write_promotions(proj, qa):
    """Rebuild research/qa/promotions.md from every run's author-decision.md (runs/ is not delivered)."""
    out = [PROMOTIONS_HEAD]
    for d in sorted((proj / "runs").glob("*/author-decision.md")):
        out.append(f"\n## {d.parent.name}\n" + d.read_text(encoding="utf-8").rstrip("\n") + "\n")
    (qa / "promotions.md").write_text("".join(out), encoding="utf-8")
    return len(out) - 1


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    proj = ROOT / "projects" / sys.argv[1]
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True,
                            text=True).stdout.strip()
    files = load(proj)
    qa = proj / "research" / "qa"
    (qa / "packets").mkdir(parents=True, exist_ok=True)
    reg = build_registry(files, commit)
    (qa / "registry.json").write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"registry: {len(reg['cast'])} cast, {len(reg['world'])} world, {len(reg['events'])} events, "
          f"{len(reg['alias_collisions'])} alias collisions")
    manifest = {"built_at": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"), "commit": commit,
                "baseline": "2026-09-30", "files": reg["files"], "packets": {}}
    for cohort in COHORTS:
        parts = write_packets(cohort, files, qa, "projects/holoen/research/qa/registry.json", commit)
        manifest["packets"][cohort] = {"owns": [files[x]["path"] for x in COHORTS[cohort]["characters"] + COHORTS[cohort]["world"]],
                                       "parts": parts}
        print(f"packet {cohort}: " + ", ".join(f"{p['packet'].split('/')[-1]} {p['chars']:,}" for p in parts))
    manifest["packets"]["bridge"] = {"parts": bridge_packets(files, reg, qa, commit)}
    print(f"promotions: {write_promotions(proj, qa)} runs")
    (qa / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")

if __name__ == "__main__":
    main()

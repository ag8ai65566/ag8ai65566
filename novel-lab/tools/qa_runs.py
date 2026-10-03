#!/usr/bin/env python3
"""QA audit runs: create GPT audit runs with their inputs inline, and merge an audit's findings into the cards.

    python3 tools/qa_runs.py make cohort myth1       # or: make bridge events | bridge ties-external
    python3 tools/qa_runs.py prepare <run>           # (lab.py calls this before a QA run) rebuild + rewrite
    python3 tools/qa_runs.py apply research/qa/audit-myth1.md [--dry]
    python3 tools/qa_runs.py promote-changed --reason "Author decision (...): ..."

`make` refreshes an existing QA run that has no gpt-free.md yet instead of creating a new one, and records
qa.json so that `lab.py gpt <run> free` rebuilds the packets and the inline prompt right before the call;
GPT then reads a copy of the same working tree, so the inline packet always matches what it can open.
`apply` replaces each finding's exact old text in the latest run of the named card (`C/` = characters,
`W/` = world), appends a Merge Record note, and lists rows it could not apply (handle those by hand).
"""
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJ = ROOT / "projects" / "holoen"
RUNS = PROJ / "runs"
sys.path.insert(0, str(ROOT / "tools"))
import qa_packets  # noqa: E402

RULES = """- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind."""


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8").rstrip("\n")


def run_of(stem):
    """Latest run holding this card's final.md (by name; content changes after each edit)."""
    c = sorted(p for p in glob.glob(str(RUNS / "*" / "final.md"))
               if re.search(r"-(character|world)-" + re.escape(stem) + r"/final\.md$", p))
    return Path(c[-1]) if c else None


BRIDGE_NOTES = {
    "ties-external": """## Scope of this ties pass (Claude, 2026-10-02)

This pass covers **external participants**: people without a card (JP/ID members, DEV_IS, guests, alumni of
other branches) as they appear across all cohorts, using the packet `ties-external.md`. Cast-to-cast pairs and
claims naming more than three people are compared from both sides by the cohort audits, whose
packets hold every outgoing and incoming claim for their members (see `research/qa/audit-*.md`); a separate
cast-ties pass would repeat that work and does not fit the remaining quota. If you see a cross-cohort tie
problem the cohort audits could not have caught, report it here; say in Merge handoff whether a further pass
is needed and what it would cover.
""",
}


def make(kind, name, run=None):
    pending = [r for r in sorted(RUNS.glob(f"*-check-QA-{kind}-{name}")) if not (r / "gpt-free.md").exists()]
    if run is None and pending:
        run = pending[-1]
    elif run is None:
        subprocess.run([sys.executable, str(ROOT / "tools" / "lab.py"), "brief", "holoen", "check",
                        f"QA {kind} audit: {name}", "--name", f"QA-{kind}-{name}"], capture_output=True, text=True)
        run = sorted(RUNS.glob(f"*-check-QA-{kind}-{name}"))[-1]
    pk = f"projects/holoen/research/qa/packets/{name}.md"
    inc = f"projects/holoen/research/qa/packets/{name}-incoming.md"
    has_inc = (ROOT / inc).exists()
    pkt = pk + (f" (owned material) and {inc} (incoming claims); both are inline below" if has_inc else " (inline below)")
    tpl = read(f"framework/prompts/gpt-{kind}-audit.md")
    if kind == "bridge" and name in BRIDGE_NOTES:
        tpl = tpl.replace("Bridge: {{bridge}} — must be events or ties", "Bridge: ties (external participants only)")
        tpl += "\n\n" + BRIDGE_NOTES[name].rstrip("\n")
    tpl = (tpl.replace("{{cohort}}", name).replace("{{bridge}}", name).replace("{{packet_path}}", pkt)
           .replace("{{registry_path}}", "projects/holoen/research/qa/registry.json").replace("{{rules}}", RULES))
    assert "{{" not in tpl, re.findall(r"\{\{\w+\}\}", tpl)

    reg = json.loads(read("projects/holoen/research/qa/registry.json"))
    if kind == "cohort":
        c = qa_packets.COHORTS[name]
        stems = set(c["characters"] + c["world"])
        cast = [x for x in reg["cast"] if Path(x["file"]).stem in stems]
        names = {x["name"] for x in cast}
        world = [x for x in reg["world"] if Path(x["file"]).stem in stems]
        units = [u for u in reg["units"] if names & set(u.get("members", []))] if names else reg["units"]
        excerpt = {"baseline": reg["baseline"], "commit": reg["commit"], "cast": cast, "world": world, "units": units}
        note = "this cohort's cast and world records and its units"
    else:
        excerpt = {"baseline": reg["baseline"], "commit": reg["commit"], "units": reg["units"],
                   "reference_only": reg.get("reference_only")}
        note = "units and reference-only people"
    parts = [tpl, "", "## Inline inputs", "", "These are the exact files at the snapshot commit; do not re-open them.", "",
             "### projects/holoen/project.md (the author's constitution; Chinese)", "", read("projects/holoen/project.md"), "",
             "### framework/prompts/shared-rules.md", "", read("framework/prompts/shared-rules.md"), "",
             "### projects/holoen/research/qa/resolutions.md (finding ledger; continue numbering from it)", "",
             read("projects/holoen/research/qa/resolutions.md"), "",
             f"### Registry excerpt ({note}; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)",
             "", "```json", json.dumps(excerpt, ensure_ascii=False, indent=1), "```", "", f"### {pk}", "", read(pk)]
    if has_inc:
        parts += ["", f"### {inc}", "", read(inc)]
    text = "\n".join(parts) + "\n"
    (run / "to-gpt.free.md").write_text(text, encoding="utf-8")
    (run / "qa.json").write_text(json.dumps({"kind": kind, "name": name}) + "\n", encoding="utf-8")
    print(f"{run.relative_to(ROOT)} {len(text):,} chars")


def cells(line):
    return [p.strip().replace("\\|", "|") for p in re.split(r"(?<!\\)\|", line.strip()[1:-1])]


def apply(audit, dry):
    src = Path(audit).read_text(encoding="utf-8")
    tag = Path(audit).stem
    rows = [cells(l) for l in src.splitlines()
            if l.startswith("| ") and not l.startswith("| ID") and not l.startswith("|---")]
    done, fails = {}, []
    for c in (r for r in rows if len(r) >= 7):
        fid, _prio, _key, loc, old, _prob, new = c[:7]
        m = re.match(r"`([CW])/([^`]+)\.md`", loc)
        if not m:
            fails.append((fid, loc, "non-card target (handle by hand)"))
            continue
        p = run_of(m.group(2))
        if not p:
            fails.append((fid, loc, "no run"))
            continue
        s = p.read_text(encoding="utf-8")
        o = old.replace("<br>", "\n")
        n = "" if new.strip() == "DELETE" else new.replace("<br>", "\n")
        if s.count(o) == 1:
            s = s.replace(o, n)
        else:  # tolerate re-wrapped lines
            ms = list(re.finditer(re.escape(o).replace(r"\n", r"\n\s*").replace(" ", r"\s+"), s))
            if len(ms) != 1:
                fails.append((fid, loc, f"old text found {s.count(o)}/{len(ms)} times"))
                continue
            s = s[:ms[0].start()] + n + s[ms[0].end():]
        if not dry:
            p.write_text(s, encoding="utf-8")
        done.setdefault(p, []).append(fid)
        print("applied", fid, "→", p.parent.name)
    for p, ids in ({} if dry else done).items():
        s = p.read_text(encoding="utf-8")
        note = (f"- **{dt.date.today()}, cross-card QA audit ({tag}, research/qa/{tag}.md, GPT xhigh):** applied "
                f"{', '.join(sorted(set(ids)))}\n  (exact replacements from the audit's findings table; dispositions in "
                f"research/qa/resolutions.md).")
        i = s.find("## Merge Record\n")
        if i < 0:
            s = s.rstrip("\n") + "\n\n## Merge Record\n" + note + "\n"
        else:
            j = s.find("\n## ", i + 5)
            s = (s[:j].rstrip("\n") + "\n" + note + "\n" + s[j:]) if j > 0 else s.rstrip("\n") + "\n" + note + "\n"
        p.write_text(s, encoding="utf-8")
    for f in fails:
        print("NOT APPLIED", *f)


def promote_changed(reason):
    """Promote (as an author decision) every card run whose final.md differs from its bible copy."""
    for d in ("characters", "world"):
        for b in sorted((PROJ / "bible" / d).glob("*.md")):
            p = run_of(b.stem)
            if p and p.read_text(encoding="utf-8") != b.read_text(encoding="utf-8"):
                subprocess.run([sys.executable, str(ROOT / "tools" / "lab.py"), "promote", str(p.parent),
                                "--force", "--reason", reason], check=True)


def prepare(run):
    """Called by `lab.py gpt <run> free` for QA runs: rebuild packets, then rewrite the inline prompt."""
    run = Path(run).resolve()
    q = json.loads((run / "qa.json").read_text(encoding="utf-8"))
    subprocess.run([sys.executable, str(ROOT / "tools" / "qa_packets.py"), "holoen"], check=True,
                   stdout=subprocess.DEVNULL)
    make(q["kind"], q["name"], run)


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == "make" and a[1] in ("cohort", "bridge"):
        make(a[1], a[2])
    elif len(a) == 2 and a[0] == "prepare":
        prepare(a[1])
    elif len(a) >= 2 and a[0] == "apply":
        apply(a[1], "--dry" in a)
    elif len(a) == 3 and a[0] == "promote-changed" and a[1] == "--reason":
        promote_changed(a[2])
    else:
        sys.exit(__doc__)

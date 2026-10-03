#!/usr/bin/env python3
"""Apply a cohort or bridge QA audit's findings table to the cards, cumulatively and idempotently.

    python3 tools/audit_apply.py <run>/gpt-free.md --tag myth1 [--dry] [--only ID,..] [--skip ID,..]

Replaces `qa_runs.py apply` for audits whose locators use any of the forms GPT writes: `C/<stem>.md`,
`W/<stem>.md`, `bible/characters/<stem>.md`, `bible/world/<stem>.md`, `research/...md`, or a short name before
"›" ("Calliope ›", "TakaMori ›", "Other Pairs ›"). A row whose locator lists several files is applied to each file
that holds the old text exactly once (whitespace-tolerant). Card edits go into the latest run of the card (then
`qa_runs.py promote-changed`); research files are edited in place. A row whose replacement is already present
and whose old text is gone counts as already applied. Rows that cannot be placed are printed for hand handling,
with every row's Propagate column. IDs are recorded as <tag>:<ID>, because cohorts reused IDs before the
per-run namespaces (P1, 2026-10-03). Card finals get one Merge Record note per audit.
"""
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import lab  # noqa: E402
import qa_packets  # noqa: E402
import qa_runs  # noqa: E402

P = ROOT / "projects" / "holoen"


def names():
    """Short name → card stem, from card Names, stems, first names and the packet aliases."""
    out = {}
    for sub in ("characters", "world"):
        for f in sorted((P / "bible" / sub).glob("*.md")):
            stem = f.stem
            name = lab.sw_fields(lab.read(f)).get("Name", stem)
            for k in {stem, stem.replace("-", " "), name}:
                out[k.casefold()] = stem
            if sub == "characters":
                out.setdefault(name.split()[0].casefold(), stem)
                out.setdefault(name.split()[-1].casefold(), stem)
    for stem, al in qa_packets.SHORT.items():
        for a in al:
            out.setdefault(a.casefold(), stem)
    extra = {"other pairs": "Myth-and-Kronii-Other-Pairs", "persona and lore": "VTuber-Persona-and-Lore",
             "myth": "hololive--Myth", "promise": "hololive--Promise", "advent": "hololive--Advent",
             "justice": "hololive--Justice", "history to 2022": "hololive-History-to-2022",
             "history 2023–2026": "hololive-History-2023-2026", "history 2023-2026": "hololive-History-2023-2026"}
    out.update(extra)
    out.pop("fuwamoco", None)
    out["fuwamoco"] = "FUWAMOCO"
    return out


def resolve(loc, nm):
    paths = []
    for m in re.finditer(r"`?([CW])/([^`/\s]+)\.md|bible/(?:characters|world)/([^`/\s]+)\.md|(research/[^`\s›;]+\.md)", loc):
        if m.group(4):
            paths.append(P / m.group(4))
        else:
            stem = m.group(2) or m.group(3)
            r = qa_runs.run_of(stem)
            if r:
                paths.append(r)
    if not paths:  # short names before "›", separated by ";"
        for part in loc.split(";"):
            head = part.split("›")[0].strip().strip("`").strip()
            stem = nm.get(head.casefold())
            if stem and qa_runs.run_of(stem):
                paths.append(qa_runs.run_of(stem))
    seen, out = set(), []
    for p in paths:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def unwrap(cell):
    segs = [c.strip() for c in cell.split("<br>")]
    whole = len(segs) > 1 and segs[0].startswith("`") and segs[-1].endswith("`") and \
        not (segs[0].endswith("`") and len(segs[0]) > 1)
    out = []
    for i, c in enumerate(segs):  # each wrapped line may carry its own backticks, or one span covers them all
        if c.startswith("`") and c.endswith("`") and c.count("`") == 2 and len(c) > 1:
            c = c[1:-1]
        elif whole and i == 0:
            c = c[1:]
        elif whole and i == len(segs) - 1:
            c = c[:-1]
        out.append(c.replace("\\|", "|"))
    return "\n".join(out)


def tolerant(s, old):
    if s.count(old) == 1:
        return [(s.index(old), s.index(old) + len(old))]
    pat = r"\s+".join(re.escape(w) for w in old.split())
    return [(m.start(), m.end()) for m in re.finditer(pat, s)]


def main(audit, tag, dry, only, skip):
    text = Path(audit).read_text(encoding="utf-8")
    body = text.split("## Findings", 1)[-1]
    body = re.split(r"\n## (?:New verified|Merge handoff|Author)", body)[0]
    rows = [qa_runs.cells(l) for l in body.splitlines()
            if l.startswith("| ") and not l.startswith("| ID") and not l.startswith("|---")]
    nm = names()
    files, done, fails, already, props = {}, {}, [], [], []
    for c in rows:
        if len(c) < 7:
            continue
        fid, _prio, _key, loc, old, _prob, new = c[:7]
        if (only and fid not in only) or fid in skip:
            continue
        prop = c[8] if len(c) > 8 else ""
        if prop.strip() and prop.strip().lower() not in ("none", "none.", "—", "-"):
            props.append((fid, prop))
        if "∅" in old or not old.strip():
            fails.append((fid, loc, "addition without old text (hand)"))
            continue
        o, n = unwrap(old), ("" if new.strip() == "DELETE" else unwrap(new))
        targets = resolve(loc, nm)
        if not targets:
            fails.append((fid, loc, "no target file"))
            continue
        hit = False
        for p in targets:
            s = files.setdefault(p, p.read_text(encoding="utf-8"))
            spans = tolerant(s, o)
            if len(spans) == 1:
                a, b = spans[0]
                files[p] = s[:a] + n + s[b:]
                done.setdefault(p, []).append(fid)
                hit = True
            elif not spans and len(n.strip()) >= 8 and n in s:
                already.append((fid, p))
                hit = True
        if not hit:
            counts = [len(tolerant(files[p], o)) for p in targets]
            fails.append((fid, loc, f"old text found {counts} times in {[p.parent.name[-30:] for p in targets]}: {o[:60]!r}"))
    if not dry:
        for p, s in files.items():
            if p in done:
                if p.name == "final.md":
                    ids = sorted(set(done[p]))
                    note = (f"- **{dt.date.today()}, cross-card QA audit ({tag}, GPT xhigh), merged by Claude:** applied "
                            f"{', '.join(f'{tag}:{i}' for i in ids)} (exact replacements; dispositions in "
                            f"research/qa/audit-{tag}.md and research/qa/resolutions.md).")
                    i = s.find("## Merge Record\n")
                    j = s.find("\n## ", i + 5) if i >= 0 else -1
                    s = (s[:j].rstrip("\n") + "\n" + note + "\n" + s[j:]) if j > 0 else s.rstrip("\n") + "\n" + note + "\n"
                p.write_text(s, encoding="utf-8")
    for p, ids in done.items():
        print("applied", ", ".join(ids), "→", p.relative_to(P))
    for fid, p in already:
        print("ALREADY", fid, "→", p.relative_to(P))
    for f in fails:
        print("NOT APPLIED", *f)
    for fid, pr in props:
        print("PROPAGATE", fid, "::", pr[:200])


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or "--tag" not in a:
        sys.exit(__doc__)

    def ids(flag):
        return set(a[a.index(flag) + 1].split(",")) if flag in a else set()
    main(a[0], a[a.index("--tag") + 1], "--dry" in a, ids("--only"), ids("--skip"))

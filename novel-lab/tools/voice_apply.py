#!/usr/bin/env python3
"""Apply a task-09 voice audit's findings table (gpt-voice-audit.md format) to the cards and sheets.

    python3 tools/voice_apply.py <run>/gpt-free.md [--dry] [--only ID,ID] [--skip ID,ID]

Each row's File is `C/<stem> › <field>` (the latest run of the card, then promote-changed) or `S/<stem>` (the sheet
export/elevenlabs/<stem>.md, edited in place). Exact old text is matched once (whitespace-tolerant); several targets
joined by <br> pair in order with the replacement's targets; a single old target takes the whole replacement.
Rows that cannot be matched, and every row's "Propagate to" column, are printed for hand handling; dispositions go
into research/qa/voice-delivery.md. Card finals get a Merge Record note listing the applied IDs.
"""
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import qa_runs  # noqa: E402

P = ROOT / "projects" / "holoen"


def segs(cell):
    parts = [x.strip() for x in cell.split("<br>")]
    out = []
    for x in parts:
        if x.startswith("`") and x.endswith("`") and len(x) > 1:
            x = x[1:-1]
        out.append(x)
    return out


LAB = re.compile(r"^\*\*([a-z])\*\*(?:,[^`]*?:)?\s*`(.*)`\s*$", re.S)


def labelled(cell):
    out = {}
    for x in cell.split("<br>"):
        m = LAB.match(x.strip())
        if not m:
            return None
        out[m.group(1)] = m.group(2)
    return out


def targets(loc):
    stems = {}
    for kind, stem in re.findall(r"\b([CS])/([A-Za-z0-9+'’-]+)", loc):
        stems.setdefault(stem, set()).add(kind)
    if "corresponding S" in loc or "S §" in loc and "S/" not in loc:
        for st in stems:
            stems[st].add("S")
    paths = []
    for st, kinds in stems.items():
        if "C" in kinds and qa_runs.run_of(st):
            paths.append(qa_runs.run_of(st))
        if "S" in kinds or re.search(r"S/" + re.escape(st), loc):
            paths.append(P / "export" / "elevenlabs" / f"{st}.md")
    return [p for p in paths if p.exists()]


def target(loc):
    m = re.search(r"\b([CS])/([A-Za-z0-9+'’-]+)", loc)
    if not m:
        return None
    kind, stem = m.groups()
    return qa_runs.run_of(stem) if kind == "C" else P / "export" / "elevenlabs" / f"{stem}.md"


def replace_once(s, old, new):
    if s.count(old) == 1:
        return s.replace(old, new), True
    pat = r"\s+".join(re.escape(w) for w in old.split())
    ms = list(re.finditer(pat, s))
    if len(ms) != 1:
        return s, False
    return s[:ms[0].start()] + new + s[ms[0].end():], True


def main(audit, dry, only, skip):
    tag = Path(audit).parent.name
    rows = [qa_runs.cells(l) for l in Path(audit).read_text(encoding="utf-8").splitlines()
            if re.match(r"\|\s*VOICE-", l)]
    done, fails, props = {}, [], []
    for c in rows:
        if len(c) < 7:
            continue
        fid, _prio, member, loc, old, _prob, new = c[:7]
        prop = c[8] if len(c) > 8 else ""
        if (only and fid not in only) or fid in skip:
            continue
        lo, ln = labelled(old), labelled(new) if new.strip() != "DELETE" else None
        if lo:  # **a** `old`<br>**b** `old` … : each pair goes to every listed file that holds it exactly once
            if new.strip() == "DELETE":
                ln = {k: "" for k in lo}
            if not ln or set(ln) != set(lo):
                fails.append((fid, loc, "labelled targets do not pair (hand)"))
                continue
            files = targets(loc)
            texts = {f: f.read_text(encoding="utf-8") for f in files}
            missing = []
            for k in sorted(lo):
                hit = False
                for f in files:
                    t, ok = replace_once(texts[f], lo[k], ln[k])
                    if ok:
                        texts[f], hit = t, True
                if not hit:
                    missing.append(k)
            if missing:
                fails.append((fid, loc, f"labelled targets not found: {', '.join(missing)}"))
                continue
            for f, t in texts.items():
                if not dry:
                    f.write_text(t, encoding="utf-8")
                done.setdefault(f, []).append(fid)
            if prop and prop.strip().lower() not in ("none", "none.", "—", "-"):
                props.append((fid, prop))
            print("applied", fid, "→", ", ".join(f.relative_to(P).as_posix() for f in files))
            continue
        path = target(loc)
        if not path or not path.exists():
            fails.append((fid, loc, "no target file"))
            continue
        olds = [o for o in segs(old) if o]
        if new.strip() == "DELETE":
            news = [""] * len(olds)
        else:
            raw = segs(new)
            nonempty = [x for x in raw if x]
            news = nonempty if len(nonempty) == len(olds) else (["\n".join(raw)] if len(olds) == 1 else None)
            if news is None and len(nonempty) == 1:  # one wrapped passage given as several lines
                olds, news = ["\n".join(olds)], nonempty
        if news is None:
            fails.append((fid, loc, f"{len(olds)} old targets vs replacement shape (hand)"))
            continue
        s = path.read_text(encoding="utf-8")
        ok_all = True
        for o, n in zip(olds, news):
            s2, ok = replace_once(s, o, n)
            if not ok:
                ok_all = False
                fails.append((fid, loc, f"old text not found once: {o[:70]!r}"))
                break
            s = s2
        if not ok_all:
            continue
        if not dry:
            path.write_text(s, encoding="utf-8")
        done.setdefault(path, []).append(fid)
        if prop and prop.strip().lower() not in ("none", "none.", "—", "-"):
            props.append((fid, prop))
        print("applied", fid, "→", path.relative_to(P))
    for path, ids in ({} if dry else done).items():
        if path.name != "final.md":
            continue
        s = path.read_text(encoding="utf-8")
        note = (f"- **{dt.date.today()}, task-09 voice audit ({tag}, GPT xhigh), merged by Claude:** applied "
                f"{', '.join(ids)} (exact replacements; dispositions in research/qa/voice-delivery.md).")
        i = s.find("## Merge Record\n")
        j = s.find("\n## ", i + 5) if i >= 0 else -1
        s = (s[:j].rstrip("\n") + "\n" + note + "\n" + s[j:]) if j > 0 else s.rstrip("\n") + "\n" + note + "\n"
        path.write_text(s, encoding="utf-8")
    for f in fails:
        print("NOT APPLIED", *f)
    for fid, p in props:
        print("PROPAGATE", fid, "::", p)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    def ids(flag):
        return set(a[a.index(flag) + 1].split(",")) if flag in a else set()
    main(a[0], "--dry" in a, ids("--only"), ids("--skip"))

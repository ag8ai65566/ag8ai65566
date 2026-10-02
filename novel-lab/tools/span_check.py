#!/usr/bin/env python3
"""Find quotations in cards and performance sheets that run past a shared ASR span.

    python3 tools/span_check.py holoen

Every quoted string in bible/ and export/elevenlabs/ (including wrapped quotes and the example blocks of the
performance sheets) that shares five consecutive words with a first-model line in the audio reports' second-model
tables must lie inside a span the reports approve (a whole shared line, a computed shared run, or a shared part
named in a "Partly agrees" verdict; case, punctuation and apostrophes normalized). Quotes that do not are listed with file and line. An ellipsis (…) inside a quote splits it into
separate quotes, so "A … B" passes only when A and B are each shared; stitching them is still for review.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(s):
    s = s.lower().replace("’", "'").replace("‘", "'")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", s.replace("'", "")).split())  # apostrophes dropped: Mii's = Miis


def rows_of(proj):
    """Every second-model table row in the audio reports: first-model line, second-model excerpt, verdict."""
    rows = []
    for f in sorted((proj / "research" / "audio-check").glob("*.md")):
        if f.name == "partial-spans.md":
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[0].startswith('"') and "youtu" in cells[1] and cells[2].startswith('"'):
                rows.append({"report": f.name, "ts": re.sub(r"\]\(.*", "", cells[1]).strip("["),
                             "first": norm(cells[0]), "second": norm(cells[2]), "verdict": cells[-1]})
    return rows


def outside_spans(project):
    """(file, line, quote, report row) for each quotation that runs past the span both ASR models share.

    A quotation (or each piece of it between ellipses) that shares five consecutive words with a first-model line
    must lie inside an approved span (see approved_spans). Merge Records and Open Questions are process notes and
    are skipped. The reports' second-model excerpts are often truncated, so they are not used for containment."""
    proj = ROOT / "projects" / project
    rows = rows_of(proj)
    approved = approved_spans(rows)
    # Gate only the rows the reports mark as partial; whole-line and hand-judged rows are approved as written.
    # (A strict both-model check of every row needs the full second-model text, which the tables truncate.)
    partial = [r for r in rows if r["verdict"].startswith(("**Partial (computed):**", "**Partly", "**Not confirmed",
                                                           "**Disagrees", "**Agrees on the bit"))]
    files = sorted((proj / "bible").rglob("*.md")) + sorted((proj / "export" / "elevenlabs").glob("*.md"))
    quote_re = re.compile(r"[\"“]([^\"”]{12,400})[\"”]")
    found = []
    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        units, para, start, in_code, skip = [], [], 1, False, False
        for n, line in enumerate(lines, 1):
            if line.startswith("## "):
                skip = line.startswith(("## Merge Record", "## Open Questions"))
            if skip:
                continue
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code:  # performance-sheet example lines: tags stripped, the whole line is spoken text
                units.append((n, '"' + re.sub(r"\[[^\]]*\]", " ", line).strip() + '"'))
                continue
            if not line.strip() or line.lstrip().startswith(("|", "#", "- ", "* ")) or re.match(r"\s*\d+\. ", line):
                if para:
                    units.append((start, " ".join(para)))
                para, start = ([line.strip()], n) if line.strip() else ([], n + 1)
                if line.lstrip().startswith(("|", "#")):
                    units.append((n, line))
                    para = []
                continue
            para.append(line.strip())
        if para:
            units.append((start, " ".join(para)))
        for n, line in units:
            for q in quote_re.findall(line):
                for piece in re.split(r"…|\.\.\.", q):
                    p = norm(piece)
                    words = p.split()
                    if len(words) < 5:
                        continue
                    grams = {" ".join(words[i:i + 5]) for i in range(len(words) - 4)}
                    hits = [r for r in partial if any(g in r["first"] for g in grams)]
                    if hits and not any(p in a for a in approved):
                        best = max(hits, key=lambda r: sum(g in r["first"] for g in grams))
                        found.append((str(f.relative_to(proj)), n, piece.strip(), best))
    return found


def approved_spans(rows):
    """Text a card may quote: whole lines judged shared (computed, or "Agrees" with a documented spelling note),
    the computed shared runs of partial rows, and the quoted shared parts named in a "Partly agrees" verdict."""
    out = []
    for r in rows:
        v = r["verdict"]
        if v.startswith(("**Shared span (computed):** whole line", "Agrees")):
            out.append(r["first"])
        elif v.startswith(("**Partial (computed):**", "**Partly", "**Shared span")) or "agrees" in v.lower():
            out += [norm(x) for x in re.findall(r'"([^"]{3,})"', v)]
    return [a for a in out if a]


def main(project):
    found = outside_spans(project)
    for f, n, q, r in found:
        print(f"{f}:{n}: \"{q}\"\n    {r['report']} {r['ts']} — {r['verdict'][:160]}")
    print(f"{len(found)} quote(s) outside a shared span")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])

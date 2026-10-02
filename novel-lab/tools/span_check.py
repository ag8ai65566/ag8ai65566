#!/usr/bin/env python3
"""Find quotations in cards and performance sheets that run past a shared ASR span.

    python3 tools/span_check.py holoen

For each partial row in research/audio-check/partial-spans.md, every quoted string in bible/ and
export/elevenlabs/ that overlaps the first model's line (5+ consecutive words) must lie inside one shared run.
Quotes that do not are listed with file and line. An ellipsis (…) inside a quote splits it into separate quotes,
so "A … B" passes only when A and B each sit inside a shared run; stitching them is still a finding for review.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(s):
    return " ".join(re.sub(r"[^a-z0-9' ]+", " ", s.lower().replace("’", "'")).split())


def outside_spans(project):
    """(file, line, quote, report row) for each quotation that runs past a shared span."""
    proj = ROOT / "projects" / project
    rows = []
    for line in (proj / "research" / "audio-check" / "partial-spans.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"- `([^`]+)` \[([^\]]+)\]\(([^)]+)\): first model \"(.*)\" → shared runs (.*)$", line)
        if m:
            runs = [norm(x) for x in re.findall(r"\"([^\"]+)\"", m.group(5))]
            rows.append({"report": m.group(1), "ts": m.group(2), "first": norm(m.group(4)), "runs": runs})
    files = sorted((proj / "bible").rglob("*.md")) + sorted((proj / "export" / "elevenlabs").glob("*.md"))
    quote_re = re.compile(r"[\"“]([^\"”]{12,400})[\"”]")
    found = []
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "punctuation difference only" in line:  # a documented normalization (e.g. Miis / Mii's)
                continue
            for q in quote_re.findall(line):
                for piece in re.split(r"…|\.\.\.", q):
                    p = norm(piece)
                    if len(p.split()) < 5:
                        continue
                    for r in rows:
                        words = p.split()
                        grams = {" ".join(words[i:i + 5]) for i in range(len(words) - 4)}
                        if not any(g in r["first"] for g in grams):
                            continue
                        if any(p in run for run in r["runs"]):
                            continue
                        found.append((str(f.relative_to(proj)), n, piece.strip(), r))
    return found


def main(project):
    found = outside_spans(project)
    for f, n, q, r in found:
        print(f"{f}:{n}: \"{q}\"\n    {r['report']} {r['ts']} shared: " + " … ".join(f'"{x}"' for x in r["runs"]))
    print(f"{len(found)} quote(s) outside a shared span")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])

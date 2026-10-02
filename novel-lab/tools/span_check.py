#!/usr/bin/env python3
"""Find quotations in cards and performance sheets that run past a shared ASR span.

    python3 tools/span_check.py holoen [--write]   # --write refreshes research/qa/span-candidates.md

Every quoted string in bible/ and export/elevenlabs/ (including wrapped quotes and the example blocks of the
performance sheets) that shares five consecutive words with a first-model line in the audio reports' second-model
tables must lie inside a span the reports approve (a whole shared line, a computed shared run, or a shared part
named in a "Partly agrees" verdict; case, punctuation and apostrophes normalized). Quotes that do not are listed with file and line. An ellipsis (…) inside a quote splits it into
separate quotes, so "A … B" passes only when A and B are each shared; stitching them is still for review.
A report row gates only the files that cite its video (a performance sheet counts its card's citations).
Japanese quotations (eight or more kana/kanji) are compared by six-character runs instead of five-word runs, with
katakana folded to hiragana and punctuation, spaces and long-vowel marks dropped; romanized glosses are not gated.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(s):
    s = s.lower().replace("’", "'").replace("‘", "'")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", s.replace("'", "")).split())  # apostrophes dropped: Mii's = Miis


def cjk(s):
    """Japanese text for comparison: katakana folded to hiragana; only kana and kanji kept (no long-vowel marks)."""
    s = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)
    s = s.translate(str.maketrans("ぁぃぅぇぉ", "あいうえお"))  # ねぇ = ねえ: a spelling variant, not a wording change
    return "".join(re.findall(r"[\u3041-\u3096\u3400-\u4dbf\u4e00-\u9fff々]", s))


def rows_of(proj):
    """Every second-model table row in the audio reports: first-model line, second-model excerpt, verdict."""
    rows = []
    for f in sorted((proj / "research" / "audio-check").glob("*.md")):
        if f.name == "partial-spans.md":
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[0].startswith('"') and "youtu" in cells[1] and cells[2].startswith('"'):
                vid = re.search(r"(?:youtu\.be/|[?&]v=)([\w-]{11})", cells[1])
                rows.append({"report": f.name, "ts": re.sub(r"\]\(.*", "", cells[1]).strip("["),
                             "vid": vid.group(1) if vid else "",
                             "first": norm(cells[0]), "second": norm(cells[2]), "verdict": cells[-1],
                             "first_j": cjk(cells[0])})
    return rows


def outside_spans(project):
    """(file, line, quote, report row) for each quotation that runs past the span both ASR models share.

    A quotation (or each piece of it between ellipses) that shares five consecutive words with a first-model line
    must lie inside an approved span (see approved_spans). A row gates a file only when the file (or, for a
    performance sheet, its card) cites that row's video: a wiki quote that happens to share five words with an
    unrelated stream is not that stream's quote. Merge Records and Open Questions are process notes and are
    skipped. The reports' second-model excerpts are often truncated, so they are not used for containment."""
    proj = ROOT / "projects" / project
    rows = rows_of(proj)
    approved = approved_spans(rows)
    approved_j = approved_spans(rows, cjk)
    # Gate only the rows the reports mark as partial; whole-line and hand-judged rows are approved as written.
    # (A strict both-model check of every row needs the full second-model text, which the tables truncate.)
    partial = [r for r in rows if r["verdict"].startswith(("**Partial (computed):**", "**Partly", "**Not confirmed",
                                                           "**Disagrees", "**Agrees on the bit"))]
    files = sorted((proj / "bible").rglob("*.md")) + sorted((proj / "export" / "elevenlabs").glob("*.md"))
    quote_re = re.compile(r"[\"“「]([^\"”」]{6,400})[\"”」]")
    found = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        card = proj / "bible" / "characters" / f.name
        cited = text + (card.read_text(encoding="utf-8") if f.parent.name == "elevenlabs" and card.exists() else "")
        gating = [r for r in partial if r["vid"] and r["vid"] in cited]
        lines = text.splitlines()
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
                    pj = cjk(piece)
                    if len(pj) >= 8:  # Japanese: six-character runs
                        grams = {pj[i:i + 6] for i in range(len(pj) - 5)}
                        hits = [r for r in gating if any(g in r["first_j"] for g in grams)]
                        if hits and not any(pj in a for a in approved_j):
                            best = max(hits, key=lambda r: sum(g in r["first_j"] for g in grams))
                            found.append((str(f.relative_to(proj)), n, piece.strip(), best))
                        continue
                    p = norm(piece)
                    words = p.split()
                    if len(words) < 5:
                        continue
                    grams = {" ".join(words[i:i + 5]) for i in range(len(words) - 4)}
                    hits = [r for r in gating if any(g in r["first"] for g in grams)]
                    if hits and not any(p in a for a in approved):
                        best = max(hits, key=lambda r: sum(g in r["first"] for g in grams))
                        found.append((str(f.relative_to(proj)), n, piece.strip(), best))
    return found


def approved_spans(rows, fold=norm):
    """Text a card may quote: whole lines judged shared (computed, or "Agrees" with a documented spelling note),
    the computed shared runs of partial rows, and the quoted shared parts named in a "Partly agrees" verdict."""
    out = []
    for r in rows:
        v = r["verdict"]
        if v.startswith(("**Shared span (computed):** whole line", "Agrees")):
            out.append(r["first"] if fold is norm else r["first_j"])
        elif v.startswith(("**Partial (computed):**", "**Partly", "**Shared span")) or "agrees" in v.lower():
            out += [fold(x) for x in re.findall(r'"([^"]{3,})"', v)]
    return [a for a in out if a]


HEADER = """# Quotation span candidates for the voice audit (task 09)

Generated by `tools/span_check.py {project} --write` on {date}. Each quotation below overlaps a transcribed line
whose report verdict is partial, disputed or hand-judged, in a video the file cites, and does not sit inside a
span the checker can approve mechanically. Many are fine (the verdict text says the sentence agrees, or a second
instance was used); the voice audit decides each one and the card is trimmed or the report verdict is made explicit.

| File:line | Quotation | Report row | Verdict (shortened) |
|---|---|---|---|"""


def main(project, write=False):
    found = outside_spans(project)
    for f, n, q, r in found:
        print(f"{f}:{n}: \"{q}\"\n    {r['report']} {r['ts']} — {r['verdict'][:160]}")
    print(f"{len(found)} quote(s) outside a shared span")
    if write:
        import datetime
        cell = lambda s: s.replace("|", "\\|")
        out = [HEADER.format(project=project, date=datetime.date.today().isoformat())]
        out += [f"| `{f}:{n}` | \"{cell(q)}\" | {r['report']} {r['ts']} | {cell(r['verdict'][:160])} |"
                for f, n, q, r in found]
        path = ROOT / "projects" / project / "research" / "qa" / "span-candidates.md"
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
        print("→", path.relative_to(ROOT))


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or sys.argv[2:] not in ([], ["--write"]):
        sys.exit(__doc__)
    main(sys.argv[1], write=len(sys.argv) == 3)

from pathlib import Path
HERE = Path(__file__).parent
def load_rows():
    rows, who = [], None
    for f in sorted((HERE / "rows").glob("*.txt")):
        for n, ln in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            if not ln.strip() or ln.startswith("#"):
                continue
            if ln.startswith("@"):
                who = ln[1:].strip(); continue
            p = ln.split("|")
            assert len(p) == 8, (f.name, n, len(p), ln[:80])
            rows.append({"member": who, "type": p[0].strip(), "orig": p[1].strip(), "reading": p[2].strip(),
                         "zh": p[3].strip(), "when": p[4].strip(), "freq": p[5].strip(), "ver": p[6].strip(),
                         "src": [s.strip() for s in p[7].split(",") if s.strip()], "at": f"{f.name}:{n}"})
    return rows
if __name__ == "__main__":
    from extract import extract
    M = {m["file"]: m for m in extract()}
    who = None
    for ln in (HERE / "sources-extra.txt").read_text(encoding="utf-8").split("\n"):
        if ln.startswith("@"):
            who = ln[1:].strip()
        elif ln.strip() and not ln.startswith("#"):
            M[who]["sources"][ln.split("|")[0]] = {}
    rows = load_rows()
    print(len(rows), "rows")
    bad = [(r["member"], s, r["at"]) for r in rows for s in r["src"]
           if s.partition("@")[0] not in M[r["member"]]["sources"] and not s.startswith(("FUWAMOCO", "X "))]
    for b in bad: print("missing source", b)
    print(sorted({r["ver"] for r in rows}), sorted({r["type"] for r in rows}))

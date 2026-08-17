#!/usr/bin/env python3
"""Turn a pose-codex document into the JSON the app ships.

Run this when a new revision of a codex comes out:

    python scripts/build-posebook.py <document.txt> --id sese --name "..." \
        --out app/poses/sese-codex.json

The parse happens here rather than at app startup so the user gets the database
by updating the app, with no import step and no parsing cost per launch. The
parser itself lives in app/posebook.py, so this script is only plumbing.

It prints a summary and refuses to write a file that lost entries against the
previous build, because a parser change that silently halves the database is
exactly the failure this format invites.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))

import posebook  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("document", type=Path)
    ap.add_argument("--id", required=True)
    ap.add_argument("--name", default="")
    ap.add_argument("--source", default="")
    ap.add_argument("--note", default="")
    ap.add_argument("--advice", action="append", default=[])
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--force", action="store_true",
                    help="write even if the entry count dropped")
    args = ap.parse_args()

    text = args.document.read_text(encoding="utf-8", errors="replace")
    codex = posebook.parse_codex(text, codex_id=args.id, name=args.name,
                                 source=args.source)
    codex.note = args.note
    codex.advice = list(args.advice)

    groups = {p.group for p in codex.poses}
    sections = {(p.group, p.section) for p in codex.poses}
    variants = sum(len(p.variants) for p in codex.poses)
    artists = codex.artist_index()
    print(f"entries   {len(codex.poses)}")
    print(f"groups    {len(groups)}")
    print(f"sections  {len(sections)}")
    print(f"variants  {variants}")
    print(f"artists   {len(artists)}  top: "
          + ", ".join(f"{a['name']}({a['uses']})" for a in artists[:6]))
    print(f"skipped   {codex.skipped} entries, {codex.skipped_variants} variants")

    empty = [p.title for p in codex.poses if not any(v.prompt for v in p.variants)]
    if empty:
        print(f"WARNING: {len(empty)} entries have no usable prompt: {empty[:5]}")

    if args.out.is_file() and not args.force:
        old = json.loads(args.out.read_text(encoding="utf-8"))
        before = len(old.get("poses", []))
        if len(codex.poses) < before:
            print(f"REFUSING to write: {before} entries before, "
                  f"{len(codex.poses)} now. Pass --force if that is intended.")
            return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(posebook.to_json(codex), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {args.out} ({args.out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

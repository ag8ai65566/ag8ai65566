#!/usr/bin/env python3
"""Inline the webfonts into src/app.html and emit ledger.html.

Artifacts run under a CSP that blocks every external host, so the typefaces
have to travel inside the file as data URIs. Fetch them from npm first:

    npm i @fontsource/instrument-serif @fontsource/ibm-plex-sans @fontsource/ibm-plex-mono

Then run this from the prototype/ directory.
"""
import base64
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "node_modules" / "@fontsource"

FACES = [
    ("Instrument Serif", 400, "instrument-serif/files/instrument-serif-latin-400-normal.woff2"),
    ("Plex Sans", 400, "ibm-plex-sans/files/ibm-plex-sans-latin-400-normal.woff2"),
    ("Plex Sans", 600, "ibm-plex-sans/files/ibm-plex-sans-latin-600-normal.woff2"),
    ("Plex Mono", 400, "ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2"),
]


def main() -> int:
    src = HERE / "src" / "app.html"
    if not FONTS.exists():
        print(f"missing {FONTS} — run the npm install shown in this file's docstring", file=sys.stderr)
        return 1

    css = []
    for family, weight, rel in FACES:
        blob = (FONTS / rel).read_bytes()
        b64 = base64.b64encode(blob).decode("ascii")
        css.append(
            f'@font-face{{font-family:"{family}";font-style:normal;font-weight:{weight};'
            f'font-display:swap;src:url(data:font/woff2;base64,{b64}) format("woff2")}}'
        )

    html = src.read_text(encoding="utf-8")
    if "/*FONTFACE*/" not in html:
        print("src/app.html has no /*FONTFACE*/ marker", file=sys.stderr)
        return 1

    out = HERE / "ledger.html"
    out.write_text(html.replace("/*FONTFACE*/", "\n".join(css), 1), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

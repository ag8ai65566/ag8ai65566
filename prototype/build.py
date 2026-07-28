#!/usr/bin/env python3
"""Inline the webfonts into src/app.html and emit ledger.html.

Artifacts run under a CSP that blocks every external host, so the typefaces
have to travel inside the file as data URIs. Fetch them from npm first:

    npm i @fontsource/instrument-serif @fontsource/ibm-plex-sans @fontsource/ibm-plex-mono

Then run this from the prototype/ directory.

If ../data/restaurants.json exists its records are baked in as the seed, so the
built page opens on the real list instead of the fictional placeholders. Pass
--sample to keep the placeholders.
"""
import base64
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "node_modules" / "@fontsource"

FACES = [
    ("Instrument Serif", 400, "instrument-serif/files/instrument-serif-latin-400-normal.woff2"),
    ("Plex Sans", 400, "ibm-plex-sans/files/ibm-plex-sans-latin-400-normal.woff2"),
    ("Plex Sans", 600, "ibm-plex-sans/files/ibm-plex-sans-latin-600-normal.woff2"),
    ("Plex Mono", 400, "ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2"),
]


DATA = HERE.parent / "data" / "restaurants.json"
# Latest poll if there is one; the hand-transcribed seed until poll-omakase has run.
STATE = HERE.parent / "data" / "booking-state.json"
STATE_SEED = HERE.parent / "scraper" / "observed-seed.json"


def booking_state():
    """slug -> reading, from the freshest source available."""
    for f in (STATE, STATE_SEED):
        if f.exists():
            raw = json.loads(f.read_text(encoding="utf-8"))
            return {k: v for k, v in raw.items() if not k.startswith("_")}
    return {}


def _strip(obj):
    """Drop _comment keys so build notes don't ship inside the page."""
    if isinstance(obj, dict):
        return {k: _strip(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [_strip(v) for v in obj]
    return obj


def _seats(text):
    """'12席 （カウンター12席）' -> 12."""
    m = re.search(r"(\d+)\s*席", text or "")
    return int(m.group(1)) if m else None


def _area(address):
    m = re.search(r"東京都(.+?[区市])", address or "")
    return m.group(1) if m else "東京"


def to_seed(rec, observed=None):
    """One scraped Tabelog record in the shape the page's SEED array uses."""
    return {
        "id": rec["id"],
        "name": rec.get("name"),
        "genre": rec.get("genre"),
        "area": _area(rec.get("address")),
        "station": (rec.get("station") or "").split("\n")[0],
        "address": rec.get("address"),
        "phone": rec.get("phone"),
        "tabelog": rec.get("tabelog"),
        "score": rec.get("score"),
        "status": "wish",
        "priority": 1,
        "seats": _seats(rec.get("seats")),
        "budget": rec.get("budgetDinner"),
        "booking": {
            "platform": rec.get("bookingSource") or "unknown",
            "url": rec.get("bookingUrl"),
            "rule": rec.get("rule") or {"kind": "unknown"},
            "announcement": rec.get("announcement"),
            "alt": rec.get("bookingAlt"),
            # The platform's own published state, timestamped. Outranks the
            # inferred rule wherever it exists — see nextAction() in app.html.
            "observed": _strip(observed) if observed else None,
        },
        "lat": rec.get("lat"),
        "lng": rec.get("lng"),
        "remind": True,
    }


def real_seed():
    """(seed, trips, pending) baked from data/, or None when there is no data."""
    if not DATA.exists():
        return None
    records = json.loads(DATA.read_text(encoding="utf-8"))
    if not records:
        return None

    state = booking_state()
    by_tabelog = {v.get("tabelogId"): v for v in state.values() if v.get("tabelogId")}
    seed = [to_seed(r, by_tabelog.get(r["id"])) for r in records]

    # Restaurants that exist only on a booking platform — acá has no Tabelog
    # page, and requiring one would have quietly dropped it from the list.
    claimed = {r["id"] for r in records}
    for slug, s in state.items():
        if s.get("tabelogId") in claimed:
            continue
        seed.append({
            "id": slug,
            "name": s.get("name"),
            "genre": s.get("genre"),
            "area": s.get("area") or "東京",
            "station": "", "address": None, "phone": None, "tabelog": None,
            "score": None, "status": "wish", "priority": 1, "seats": None,
            "budget": None,
            "booking": {
                "platform": "omakase",
                "url": s.get("url") or f"https://omakase.in/r/{slug}",
                "rule": {"kind": "unknown"},
                "announcement": None,
                "alt": None,
                "observed": _strip(s),
            },
            "lat": None, "lng": None, "remind": True,
        })
    seed.sort(key=lambda s: (s["booking"]["platform"] == "none", s["name"] or ""))
    # The trip the radar counts back from. A year out, this is what decides
    # which release matters: the next one on sale is for somebody else's dinner.
    # Editable in the app.
    trips = [{
        "id": "t1", "name": "2027 年 7 月 東京",
        "start": "2027-07-05", "end": "2027-07-12", "party": 2, "plan": {},
    }]
    return json.dumps(seed, ensure_ascii=False, indent=2), json.dumps(trips, ensure_ascii=False, indent=2), "[]"


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
    html = html.replace("/*FONTFACE*/", "\n".join(css), 1)

    baked = None if "--sample" in sys.argv else real_seed()
    if baked:
        seed, trips, pending = baked
        for tag, value in (("SEED", seed), ("TRIPS", trips), ("PENDING", pending)):
            pattern = re.compile(r"/\*<<%s\*/.*?/\*%s>>\*/" % (tag, tag), re.S)
            if not pattern.search(html):
                print(f"src/app.html has no <<{tag} marker", file=sys.stderr)
                return 1
            html = pattern.sub(lambda _m, v=value: v, html, count=1)
        print(f"baked {len(json.loads(seed))} restaurants from {DATA}")
    else:
        print("using the built-in sample data" + ("" if "--sample" in sys.argv else f" (no {DATA})"))

    out = HERE / "ledger.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

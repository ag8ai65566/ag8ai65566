"""Find the panels in an existing comic page.

Given a page someone already drew, recover the rectangles its panels occupy so
the same staging can be reused with a different character.

The method is a recursive XY-cut, which is the classic way to read a page like
this: gutters are full-width or full-height runs of background, so look for
rows that are entirely background, split there, then look for such columns
inside each band, and recurse. It handles the layouts people actually draw -
a wide establishing panel over two narrower ones is two levels of the same
recursion - without needing any model.

What it does not handle is deliberately irregular art: slanted gutters, panels
that bleed off the page, insets overlapping a larger panel. Those need real
segmentation, and guessing at them would produce confident nonsense. Detection
reports a confidence, and the UI lets the layout be swapped for a stock one,
because a wrong answer the user can see and correct beats a wrong answer that
looks automatic.
"""

from __future__ import annotations

from dataclasses import dataclass

from PIL import Image

# A gutter row/column must be at least this fraction of background to count.
PURITY = 0.985
# and this thick, as a fraction of the page's short side. Below it, the "gutter"
# is usually just a pale band inside the art.
MIN_GUTTER = 0.008
# Anything smaller than this in either direction is a speck, not a panel.
MIN_PANEL = 0.06
MAX_DEPTH = 6
MAX_PANELS = 12


@dataclass
class Box:
    """A panel in page fractions (0-1), matching comics.Panel."""

    x: float
    y: float
    w: float
    h: float

    def public(self) -> dict:
        return {"x": round(self.x, 4), "y": round(self.y, 4),
                "w": round(self.w, 4), "h": round(self.h, 4)}


@dataclass
class Detected:
    boxes: list[Box]
    confidence: float = 0.0
    note: str = ""
    background: str = "light"

    def public(self) -> dict:
        return {
            "panels": [b.public() for b in self.boxes],
            "count": len(self.boxes),
            "confidence": round(self.confidence, 3),
            "note": self.note,
            "background": self.background,
        }


class Profiles:
    """Background fractions for any sub-rectangle, in constant time.

    The profiles have to be measured *within the region being cut*, not once
    over the whole page. The gutter between the two lower panels of a
    wide-over-two layout is background only inside that lower band - across the
    full page height the top panel covers it, so a page-wide column profile
    never sees a gutter there and the band is returned as one panel. Prefix
    sums along each axis make the per-region query cheap enough to do properly.
    """

    def __init__(self, mask: list[int], width: int, height: int) -> None:
        self.w, self.h = width, height
        # rows[y][x] = number of background pixels in row y, columns [0, x).
        self.rows = [0] * ((width + 1) * height)
        for y in range(height):
            base, out = y * width, y * (width + 1)
            total = 0
            for x in range(width):
                total += mask[base + x]
                self.rows[out + x + 1] = total
        # cols[x][y] = number of background pixels in column x, rows [0, y).
        self.cols = [0] * ((height + 1) * width)
        for x in range(width):
            out = x * (height + 1)
            total = 0
            for y in range(height):
                total += mask[y * width + x]
                self.cols[out + y + 1] = total

    def row(self, y: int, x0: int, x1: int) -> float:
        span = x1 - x0
        if span <= 0:
            return 1.0
        base = y * (self.w + 1)
        return (self.rows[base + x1] - self.rows[base + x0]) / span

    def col(self, x: int, y0: int, y1: int) -> float:
        span = y1 - y0
        if span <= 0:
            return 1.0
        base = x * (self.h + 1)
        return (self.cols[base + y1] - self.cols[base + y0]) / span


def _runs(profile, lo: int, hi: int, min_len: int) -> list[tuple[int, int]]:
    """Maximal runs of near-pure background inside [lo, hi)."""
    out: list[tuple[int, int]] = []
    start = None
    for i in range(lo, hi):
        if profile(i) >= PURITY:
            if start is None:
                start = i
        elif start is not None:
            if i - start >= min_len:
                out.append((start, i))
            start = None
    if start is not None and hi - start >= min_len:
        out.append((start, hi))
    return out


def _trim(profile, lo: int, hi: int) -> tuple[int, int]:
    """Drop background margin from both ends of a span."""
    while lo < hi and profile(lo) >= PURITY:
        lo += 1
    while hi > lo and profile(hi - 1) >= PURITY:
        hi -= 1
    return lo, hi


def _cut(prof: Profiles, x0, y0, x1, y1, depth, min_gap, min_w, min_h, out,
         widths=None, max_gap=0) -> None:
    x0, x1 = _trim(lambda x: prof.col(x, y0, y1), x0, x1)
    y0, y1 = _trim(lambda y: prof.row(y, x0, x1), y0, y1)
    if x1 - x0 < min_w or y1 - y0 < min_h or len(out) >= MAX_PANELS:
        return
    if depth < MAX_DEPTH:
        # Interior gutters only: a run touching an edge is margin, already
        # trimmed above, and splitting on it would recurse forever. Both
        # profiles are measured inside this region, not across the page.
        axes = (
            ("y", lambda y: prof.row(y, x0, x1), y0, y1),
            ("x", lambda x: prof.col(x, y0, y1), x0, x1),
        )
        for axis, profile, a0, a1 in axes:
            gaps = [g for g in _runs(profile, a0, a1, min_gap) if g[0] > a0 and g[1] < a1]
            # A band far wider than this page's usual gutter is not a gutter, it
            # is empty space inside the art. See _pass_widths.
            if max_gap:
                gaps = [g for g in gaps if g[1] - g[0] <= max_gap]
            if not gaps:
                continue
            if widths is not None:
                widths.extend(g[1] - g[0] for g in gaps)
            pieces, cursor = [], a0
            for start, end in gaps:
                pieces.append((cursor, start))
                cursor = end
            pieces.append((cursor, a1))
            for lo, hi in pieces:
                if axis == "y":
                    _cut(prof, x0, lo, x1, hi, depth + 1, min_gap, min_w, min_h,
                         out, widths, max_gap)
                else:
                    _cut(prof, lo, y0, hi, y1, depth + 1, min_gap, min_w, min_h,
                         out, widths, max_gap)
            return
    out.append((x0, y0, x1, y1))


GUTTER_SPREAD = 3.0


def _pass_widths(prof, width, height, min_gap, min_w, min_h):
    """Cut the page, and decide whether the cut found gutters or just flat art.

    A comic page has one gutter width by design, so the widths a correct cut
    uses come out near-identical: measured across every layout this app draws,
    the spread is 0.00-0.20. Flat areas inside a single full-bleed illustration
    also read as runs of background and get cut on, but those bands vary wildly
    - one such image was split six ways on gutters from 6px to 345px, a spread
    of 9.97.

    Rejecting the widest bands and retrying does not help, because when every
    band is accidental the median is inflated too. So an inconsistent set is
    taken as proof that the page has no panel grid, and it is returned whole.
    Saying "this looks like one picture" is right far more often than six
    confident rectangles drawn through the middle of somebody's artwork.
    """
    found: list[tuple[int, int, int, int]] = []
    widths: list[int] = []
    _cut(prof, 0, 0, width, height, 0, min_gap, min_w, min_h, found, widths)
    if len(widths) < 3:
        return found, widths, True
    ordered = sorted(widths)
    median = ordered[len(ordered) // 2]
    spread = (ordered[-1] - ordered[0]) / max(1, median)
    if spread <= GUTTER_SPREAD:
        return found, widths, True
    whole: list[tuple[int, int, int, int]] = []
    _cut(prof, 0, 0, width, height, MAX_DEPTH, min_gap, min_w, min_h, whole)
    return whole, widths, False


def detect(image: Image.Image, max_side: int = 900) -> Detected:
    """Recover the panel rectangles of a comic page."""
    page = image.convert("L")
    scale = min(1.0, max_side / max(page.size))
    if scale < 1.0:
        page = page.resize((max(1, int(page.width * scale)),
                            max(1, int(page.height * scale))), Image.BILINEAR)
    width, height = page.size
    pixels = list(page.getdata())

    # Gutters are whatever colour the page margin is - white for most comics,
    # black for a dark-background page. Read it off the border rather than
    # assuming, or every dark page detects as a single panel.
    border = (
        [pixels[x] for x in range(width)]
        + [pixels[(height - 1) * width + x] for x in range(width)]
        + [pixels[y * width] for y in range(height)]
        + [pixels[y * width + width - 1] for y in range(height)]
    )
    border.sort()
    level = border[len(border) // 2]
    dark = level < 128
    tol = 26
    mask = [1 if abs(p - level) <= tol else 0 for p in pixels]

    prof = Profiles(mask, width, height)
    short = min(width, height)
    min_gap = max(2, int(short * MIN_GUTTER))
    min_w, min_h = int(width * MIN_PANEL), int(height * MIN_PANEL)

    found, widths, gridded = _pass_widths(prof, width, height, min_gap, min_w, min_h)

    boxes = [
        Box(x0 / width, y0 / height, (x1 - x0) / width, (y1 - y0) / height)
        for x0, y0, x1, y1 in found
    ]
    boxes.sort(key=lambda b: (round(b.y, 2), b.x))

    covered = sum(b.w * b.h for b in boxes)
    note = ""
    if not boxes:
        note = "看不出格線 —— 這頁可能是滿版單張，或格子是斜的／破格的。"
    elif not gridded:
        note = ("格線寬度很不一致，看起來不是分格的頁面（比較像一張滿版圖）。"
                "當成單張處理；如果它其實有格子，請手動挑一個接近的分鏡。")
    elif len(boxes) == 1:
        note = "只找到一格，當成單張處理。"
    elif covered < 0.45:
        note = "格子偵測得不太完整，建議手動挑一個接近的分鏡。"
    return Detected(
        boxes=boxes,
        # Panels should cover most of a page; how much they do is the honest
        # measure of whether this page suited a rectangular cut at all.
        confidence=(min(1.0, covered / 0.92) if boxes else 0.0) * (1.0 if gridded else 0.4),
        note=note,
        background="dark" if dark else "light",
    )


def crops(image: Image.Image, boxes: list[Box]) -> list[Image.Image]:
    """The art inside each detected panel, for tagging."""
    out = []
    width, height = image.size
    for box in boxes:
        left, top = int(box.x * width), int(box.y * height)
        right, bottom = int((box.x + box.w) * width), int((box.y + box.h) * height)
        if right - left < 8 or bottom - top < 8:
            continue
        out.append(image.crop((left, top, right, bottom)))
    return out

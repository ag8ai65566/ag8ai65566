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
    # The page's own shape. Without it a landscape page or a 4koma strip gets
    # recomposed at the default 2:3 and none of the panels line up.
    aspect: float = 2 / 3
    reading: str = "ltr"

    def public(self) -> dict:
        return {
            "panels": [b.public() for b in self.boxes],
            "count": len(self.boxes),
            "confidence": round(self.confidence, 3),
            "note": self.note,
            "background": self.background,
            "aspect": round(self.aspect, 4),
            "reading": self.reading,
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
         widths=None) -> None:
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
            if not gaps:
                continue
            if widths is not None:
                # Kept per axis. Manga routinely uses a wide gutter between
                # rows and a narrow one between columns; comparing the two
                # against each other makes a perfectly ordinary page look
                # inconsistent and get rejected as a full-bleed illustration.
                widths[axis].extend(g[1] - g[0] for g in gaps)
            pieces, cursor = [], a0
            for start, end in gaps:
                pieces.append((cursor, start))
                cursor = end
            pieces.append((cursor, a1))
            for lo, hi in pieces:
                if axis == "y":
                    _cut(prof, x0, lo, x1, hi, depth + 1, min_gap, min_w, min_h,
                         out, widths)
                else:
                    _cut(prof, lo, y0, hi, y1, depth + 1, min_gap, min_w, min_h,
                         out, widths)
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
    widths: dict[str, list[int]] = {"x": [], "y": []}
    _cut(prof, 0, 0, width, height, 0, min_gap, min_w, min_h, found, widths)

    consistent = True
    for axis_widths in widths.values():
        if len(axis_widths) < 3:
            continue
        ordered = sorted(axis_widths)
        median = ordered[len(ordered) // 2]
        if (ordered[-1] - ordered[0]) / max(1, median) > GUTTER_SPREAD:
            consistent = False
    if consistent:
        return found, widths, True
    whole: list[tuple[int, int, int, int]] = []
    _cut(prof, 0, 0, width, height, MAX_DEPTH, min_gap, min_w, min_h, whole)
    return whole, widths, False


def detect(image: Image.Image, max_side: int = 900, reading: str = "ltr") -> Detected:
    """Recover the panel rectangles of a comic page.

    `reading` orders the panels: "rtl" for manga, which is read right-to-left
    within a row, so panel 1 is the top *right*. Getting this backwards silently
    reverses the story - the prompts land on mirrored rectangles.
    """
    page = image.convert("L")
    scale = min(1.0, max_side / max(page.size))
    if scale < 1.0:
        page = page.resize((max(1, int(page.width * scale)),
                            max(1, int(page.height * scale))), Image.BILINEAR)
    width, height = page.size
    pixels = list(page.getdata())
    short = min(width, height)
    min_gap = max(2, int(short * MIN_GUTTER))
    min_w, min_h = int(width * MIN_PANEL), int(height * MIN_PANEL)

    # Which grey is the gutter? Reading it off the page border works for a page
    # with a margin, and fails completely on a full-bleed page where the border
    # *is* artwork - the mask then treats one panel's fill as background and the
    # cut disintegrates. So several candidates are tried and the one that
    # actually yields a clean grid wins: the border median, the commonest value
    # on the page, and plain white and black for the two conventional cases.
    border = (
        [pixels[x] for x in range(width)]
        + [pixels[(height - 1) * width + x] for x in range(width)]
        + [pixels[y * width] for y in range(height)]
        + [pixels[y * width + width - 1] for y in range(height)]
    )
    border.sort()
    histogram = [0] * 256
    for value in pixels:
        histogram[value] += 1
    candidates: list[int] = []
    for level in (border[len(border) // 2], histogram.index(max(histogram)), 255, 0):
        if all(abs(level - seen) > 8 for seen in candidates):
            candidates.append(level)

    best = None
    for level in candidates:
        mask = [1 if abs(p - level) <= 26 else 0 for p in pixels]
        present = sum(mask) / len(mask)
        # A colour that barely appears cannot be the gutter. Without this a
        # blank white page "wins" on the black candidate, which finds no
        # background at all and so calls the empty page one full panel.
        if present < 0.01:
            continue
        prof = Profiles(mask, width, height)
        boxes, widths, gridded = _pass_widths(prof, width, height, min_gap, min_w, min_h)
        covered = sum((x1 - x0) * (y1 - y0) for x0, y0, x1, y1 in boxes) / (width * height)
        # A single box spanning the page is the *absence* of a cut, so it must
        # never outrank a real one - by coverage it scores a perfect 1.00 and
        # would win every time, since any genuine grid loses area to its own
        # gutters. Finding a grid at all is therefore the first term, and
        # coverage only ranks the grids against each other: that also demotes a
        # shattered cut, which covers far less of the page than a correct one.
        found_grid = gridded and len(boxes) >= 2
        score = (1.0 if found_grid else 0.0) + covered
        if best is None or score > best[0]:
            best = (score, boxes, widths, gridded, level)
        if found_grid and covered > 0.88:
            break

    if best is None:
        return Detected([], 0.0, "看不出格線 —— 這頁可能是滿版單張，或格子是斜的／破格的。",
                        "light", (width / height) if height else 2 / 3, reading)
    _, found, widths, gridded, level = best
    dark = level < 128

    boxes = [
        Box(x0 / width, y0 / height, (x1 - x0) / width, (y1 - y0) / height)
        for x0, y0, x1, y1 in found
    ]
    # Row-major, then across the row in the page's reading direction.
    right_to_left = reading == "rtl"
    boxes.sort(key=lambda b: (round(b.y, 2), -b.x if right_to_left else b.x))

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
        aspect=(image.width / image.height) if image.height else 2 / 3,
        reading="rtl" if right_to_left else "ltr",
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

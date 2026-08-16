"""Comic pages: panel layouts, page composition, and readable speech bubbles.

Three findings shaped this, all checked against real data rather than assumed.

**The checkpoints already know comics.** Illustrious and Pony are trained on
danbooru, where `comic` has 721k posts, `speech_bubble` 511k and `4koma` 116k.
There is no need for a comic-specific checkpoint - the ones already installed
draw panels natively once you use the tags they were trained on. (Searching
CivitAI for comic checkpoints turns up mostly SD1.5-era models that would be a
downgrade.) So this module adds vocabulary and composition, not a new model.

**Comics default to black and white.** 377k of those 721k `comic` posts are
also tagged `monochrome`, so a prompt that just says "comic" comes out grey
about half the time. Full colour is not something you ask for, it is something
you push against - `monochrome, greyscale` go in the negative prompt.

**A page is composed, not generated.** Asking one 1024x1024 render for a
4-panel page gives four cramped panels, wobbly hand-drawn borders and, at that
size, mush. Each panel is rendered separately at a proper ~1 megapixel SDXL
size for its own aspect ratio, then pasted into the page here. That also means
the borders are real geometry, and the dialogue is real text: SDXL cannot spell,
so any lettering it draws is gibberish, while PIL can simply write the words.
"""

from __future__ import annotations

import textwrap
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# SDXL was trained at ~1 megapixel; these are the standard buckets. A panel is
# rendered at whichever bucket is closest in aspect ratio to its slot on the
# page, then scaled down into it - so every panel is on-distribution no matter
# how thin its slot is.
SDXL_BUCKETS: list[tuple[int, int]] = [
    (640, 1536), (768, 1344), (832, 1216), (896, 1152), (1024, 1024),
    (1152, 896), (1216, 832), (1344, 768), (1536, 640),
]


@dataclass(frozen=True)
class Panel:
    """A slot on the page, in fractions of the page (0-1)."""

    x: float
    y: float
    w: float
    h: float


@dataclass(frozen=True)
class Layout:
    id: str
    label: str
    panels: tuple[Panel, ...]
    # Page shape. 4koma is tall and narrow; a spread is wide.
    aspect: float = 2 / 3
    note: str = ""

    @property
    def count(self) -> int:
        return len(self.panels)


def _grid(cols: int, rows: int) -> tuple[Panel, ...]:
    return tuple(
        Panel(c / cols, r / rows, 1 / cols, 1 / rows)
        for r in range(rows)
        for c in range(cols)
    )


LAYOUTS: list[Layout] = [
    Layout(
        id="single", label="1 格（單張）", panels=(Panel(0, 0, 1, 1),),
        aspect=2 / 3, note="就是一張圖，但套上漫畫的畫框和對白框。",
    ),
    Layout(
        id="single-wide", label="1 格（橫幅）", panels=(Panel(0, 0, 1, 1),),
        aspect=3 / 2, note="橫的單格，適合大場面或跨頁感。",
    ),
    Layout(
        id="two-v", label="2 格（上下）", panels=_grid(1, 2),
        aspect=2 / 3, note="最簡單的分鏡：一個動作、一個反應。",
    ),
    Layout(
        id="two-h", label="2 格（左右）", panels=_grid(2, 1),
        aspect=3 / 2, note="左右對照，適合兩個角色互看。",
    ),
    Layout(
        id="three-v", label="3 格（直排）", panels=_grid(1, 3),
        aspect=2 / 3, note="起承轉，節奏比 4 格快。",
    ),
    Layout(
        id="four-grid", label="4 格（田字）", panels=_grid(2, 2),
        aspect=2 / 3, note="最通用的一頁，四個鏡頭。",
    ),
    Layout(
        id="4koma", label="4 格（直排・日式四格）", panels=_grid(1, 4),
        aspect=0.42, note="經典四格漫畫。起承轉合，最後一格放結果。",
    ),
    Layout(
        id="hero-two", label="3 格（上大・下兩小）",
        panels=(Panel(0, 0, 1, 0.5), Panel(0, 0.5, 0.5, 0.5), Panel(0.5, 0.5, 0.5, 0.5)),
        aspect=2 / 3, note="第一格當定場大鏡頭，下面兩格帶細節。",
    ),
    Layout(
        id="six-grid", label="6 格（2×3）", panels=_grid(2, 3),
        aspect=2 / 3, note="一頁講完一小段。格子小，別放太複雜的畫面。",
    ),
]

BY_ID = {layout.id: layout for layout in LAYOUTS}
MAX_PANELS = max(layout.count for layout in LAYOUTS)


def get(layout_id: str) -> Layout | None:
    return BY_ID.get(layout_id)


CUSTOM_ID = "custom"


def custom_layout(panels: list[dict], aspect: float) -> Layout | None:
    """A layout read off an existing page, rather than one from the catalogue.

    Rectangles are clamped and sanity-checked here because they arrive from a
    detector working on someone's scan, not from this file's own constants.
    """
    boxes: list[Panel] = []
    for raw in panels[:MAX_PANELS]:
        try:
            x, y = float(raw["x"]), float(raw["y"])
            w, h = float(raw["w"]), float(raw["h"])
        except (KeyError, TypeError, ValueError):
            continue
        x, y = max(0.0, min(x, 0.98)), max(0.0, min(y, 0.98))
        w, h = max(0.02, min(w, 1.0 - x)), max(0.02, min(h, 1.0 - y))
        boxes.append(Panel(x, y, w, h))
    if not boxes:
        return None
    return Layout(
        id=CUSTOM_ID, label="從頁面讀到的分鏡", panels=tuple(boxes),
        aspect=max(0.2, min(aspect, 4.0)),
        note="這是從你上傳的那一頁量出來的格子。",
    )


def panel_size(panel: Panel, page_aspect: float) -> tuple[int, int]:
    """The SDXL bucket closest in shape to this panel's slot."""
    slot = (panel.w * page_aspect) / max(panel.h, 1e-6)
    return min(SDXL_BUCKETS, key=lambda wh: abs((wh[0] / wh[1]) - slot))


# -- prompt scaffolding ------------------------------------------------------

# Tags the checkpoints actually know, with danbooru post counts as of writing:
# comic 721k, speech_bubble 511k, 4koma 116k, multiple_views 266k.
PANEL_STYLE = "comic, manga style"
# 377k of the 721k `comic` posts are also `monochrome`, so full colour has to be
# asked for by excluding its opposite. Without this the page comes out grey
# about half the time however colourful the prompt is.
COLOR_NEGATIVE = "monochrome, greyscale, sketch, lineart, unfinished, sepia"
# The model spells like a toddler, and this app draws the real text afterwards,
# so any lettering it invents is pure noise on the page.
TEXT_NEGATIVE = "text, speech bubble, english text, watermark, signature, letterboxed"

HELP = {
    "layout": "分鏡＝把一頁切成幾格。每一格自己寫要畫什麼，最後拼成一頁。",
    "panel": "這一格要畫什麼。用平常的提詞就好，鏡頭感的詞很有用：`close-up`（特寫）、`from above`（俯視）、`from side`（側面）。",
    "shared": "每一格都會加上這段，用來固定角色和畫風 —— 例如 `1girl, long black hair, red dress`。不寫的話每格可能長得不一樣。",
    "color": "漫畫在訓練資料裡有一半是黑白的，所以「全彩」是靠負面詞把 `monochrome, greyscale` 排除掉。取消勾選就會變回黑白漫畫風。",
    "bubble": "對白會在畫完之後用真正的文字畫上去。AI 自己寫字一定是亂碼，所以這裡才看得懂。",
    "gutter": "格子之間的白邊。0 就是格子貼在一起。",
    "border": "畫框線的粗細。",
}

# One-line direction for what tends to work per panel, shown under the boxes.
SHOT_HINTS = [
    ("establishing shot, wide shot", "定場：先讓人看懂在哪裡"),
    ("close-up, looking at viewer", "特寫：情緒、反應"),
    ("from above, from behind", "換鏡位：避免每格都一樣"),
    ("two-shot, facing another", "兩人同框：對話戲"),
]


def scaffold(prompt: str, shared: str, prefix: str = "") -> str:
    """One panel's final positive prompt."""
    parts = [p.strip().strip(",") for p in (prefix, PANEL_STYLE, shared, prompt)]
    return ", ".join(p for p in parts if p)


def negative_for(base: str, full_color: bool = True, draw_text: bool = True) -> str:
    parts = [base.strip().strip(",")] if base and base.strip() else []
    if full_color:
        parts.append(COLOR_NEGATIVE)
    if draw_text:
        parts.append(TEXT_NEGATIVE)
    return ", ".join(p for p in parts if p)


# -- page composition --------------------------------------------------------

# PIL needs a real font file for CJK; the built-in bitmap font cannot draw it at
# all. These are the usual places, most specific first.
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\msjh.ttc",        # 微軟正黑體 - on every modern Windows
    r"C:\Windows\Fonts\msyh.ttc",        # 微軟雅黑
    r"C:\Windows\Fonts\mingliu.ttc",     # 細明體
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def find_font(size: int, extra: str = "") -> ImageFont.FreeTypeFont | None:
    for path in ([extra] if extra else []) + FONT_CANDIDATES:
        try:
            if path and Path(path).is_file():
                return ImageFont.truetype(path, size)
        except (OSError, ValueError):
            continue
    return None


@dataclass
class Bubble:
    """A line of dialogue to letter onto a panel after it is drawn."""

    text: str
    # Where on the panel, as a fraction of the panel.
    at: str = "top-left"  # top-left | top-right | bottom-left | bottom-right | top | bottom
    tail: bool = True


@dataclass
class PageStyle:
    gutter: int = 18
    border: int = 5
    margin: int = 26
    background: tuple[int, int, int] = (255, 255, 255)
    ink: tuple[int, int, int] = (17, 17, 17)
    width: int = 1600
    font_path: str = ""


ANCHORS = {
    "top-left": (0.04, 0.04, 0.0, 0.0),
    "top": (0.5, 0.04, 0.5, 0.0),
    "top-right": (0.96, 0.04, 1.0, 0.0),
    "bottom-left": (0.04, 0.96, 0.0, 1.0),
    "bottom": (0.5, 0.96, 0.5, 1.0),
    "bottom-right": (0.96, 0.96, 1.0, 1.0),
}


def _wrap(text: str, per_line: int) -> list[str]:
    """Wrap for CJK and Latin alike.

    textwrap counts characters, which is right for CJK (no spaces, uniform
    width) but breaks Latin words mid-word. Latin text goes through textwrap's
    word wrapping; anything with CJK is chopped by character count.
    """
    text = (text or "").strip()
    if not text:
        return []
    lines: list[str] = []
    for para in text.splitlines():
        para = para.strip()
        if not para:
            continue
        cjk = any("\u2e80" <= ch <= "\u9fff" or "\uac00" <= ch <= "\ud7ff" for ch in para)
        if cjk:
            width = max(4, per_line)
            lines += [para[i:i + width] for i in range(0, len(para), width)]
        else:
            lines += textwrap.wrap(para, width=max(8, int(per_line * 1.8))) or [para]
    return lines[:6]


def draw_bubble(canvas: Image.Image, box: tuple[int, int, int, int],
                bubble: Bubble, style: PageStyle) -> None:
    """Letter one bubble onto the page, inside `box` (the panel's rectangle)."""
    text = (bubble.text or "").strip()
    if not text:
        return
    px, py, pw, ph = box
    size = max(15, int(min(pw, ph) * 0.055))
    font = find_font(size, style.font_path)
    if font is None:
        return  # no usable font; silently skip rather than draw tofu

    lines = _wrap(text, per_line=max(5, int(pw * 0.6 / size)))
    if not lines:
        return

    draw = ImageDraw.Draw(canvas)
    widths, height = [], 0
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=font)
        widths.append(right - left)
        height += (bottom - top) + int(size * 0.35)
    text_w, text_h = max(widths), height
    pad_x, pad_y = int(size * 1.1), int(size * 0.8)
    bw, bh = text_w + pad_x * 2, text_h + pad_y * 2

    ax, ay, gx, gy = ANCHORS.get(bubble.at, ANCHORS["top-left"])
    cx = px + int(pw * ax) - int(bw * gx)
    cy = py + int(ph * ay) - int(bh * gy)
    cx = max(px + 6, min(cx, px + pw - bw - 6))
    cy = max(py + 6, min(cy, py + ph - bh - 6))

    if bubble.tail:
        # A stubby tail pointing at the middle of the panel, so it reads as
        # speech rather than as a caption box.
        tip = (px + pw // 2, py + ph // 2)
        base = (cx + bw // 2, cy + bh // 2)
        dx, dy = tip[0] - base[0], tip[1] - base[1]
        length = max(1.0, (dx * dx + dy * dy) ** 0.5)
        ux, uy = dx / length, dy / length
        root = (base[0] + ux * bw * 0.32, base[1] + uy * bh * 0.42)
        span = max(8, size // 2)
        draw.polygon(
            [
                (root[0] - uy * span, root[1] + ux * span),
                (root[0] + uy * span, root[1] - ux * span),
                (base[0] + ux * (bw * 0.5 + span * 2.2),
                 base[1] + uy * (bh * 0.5 + span * 2.2)),
            ],
            fill=(255, 255, 255), outline=style.ink, width=max(2, style.border // 2),
        )

    draw.rounded_rectangle(
        [cx, cy, cx + bw, cy + bh], radius=int(min(bw, bh) * 0.32),
        fill=(255, 255, 255), outline=style.ink, width=max(2, style.border // 2),
    )
    y = cy + pad_y
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=font)
        draw.text((cx + (bw - (right - left)) // 2 - left, y - top),
                  line, font=font, fill=style.ink)
        y += (bottom - top) + int(size * 0.35)


def compose(
    layout: Layout,
    panel_images: list[Image.Image],
    bubbles: list[list[Bubble]] | None = None,
    style: PageStyle | None = None,
) -> Image.Image:
    """Paste rendered panels into a page, with real borders and lettering.

    Panels are cropped to fill their slot (`ImageOps.fit` semantics) rather than
    letterboxed, because a comic page with grey bars in it stops looking like a
    comic page.
    """
    style = style or PageStyle()
    bubbles = bubbles or []
    page_w = max(512, style.width)
    page_h = max(512, int(round(page_w / layout.aspect)))
    page = Image.new("RGB", (page_w, page_h), style.background)
    draw = ImageDraw.Draw(page)

    # Gutter, border and margin are given as they should look on a 1000px-wide
    # page and scaled from there. Otherwise the same settings give chunky
    # borders on a small preview and hairlines on a 3000px export.
    scale = page_w / 1000
    margin = int(round(style.margin * scale))
    gutter = style.gutter * scale
    style = PageStyle(
        gutter=int(round(gutter)), border=max(1, int(round(style.border * scale))) if style.border else 0,
        margin=margin, background=style.background, ink=style.ink,
        width=page_w, font_path=style.font_path,
    )

    inner_w = page_w - margin * 2
    inner_h = page_h - margin * 2
    half = gutter / 2

    for index, panel in enumerate(layout.panels):
        x = style.margin + panel.x * inner_w
        y = style.margin + panel.y * inner_h
        w = panel.w * inner_w
        h = panel.h * inner_h
        # Half a gutter is taken off each shared edge, so neighbouring panels
        # end up one full gutter apart while the page margin stays even.
        left = int(round(x + (half if panel.x > 0 else 0)))
        top = int(round(y + (half if panel.y > 0 else 0)))
        right = int(round(x + w - (half if panel.x + panel.w < 0.999 else 0)))
        bottom = int(round(y + h - (half if panel.y + panel.h < 0.999 else 0)))
        box_w, box_h = max(1, right - left), max(1, bottom - top)

        if index < len(panel_images) and panel_images[index] is not None:
            art = panel_images[index].convert("RGB")
            scale = max(box_w / art.width, box_h / art.height)
            art = art.resize(
                (max(1, int(art.width * scale)), max(1, int(art.height * scale))),
                Image.LANCZOS,
            )
            ox = (art.width - box_w) // 2
            oy = (art.height - box_h) // 2
            page.paste(art.crop((ox, oy, ox + box_w, oy + box_h)), (left, top))
        else:
            draw.rectangle([left, top, right, bottom], fill=(238, 238, 238))

        for bubble in (bubbles[index] if index < len(bubbles) else []):
            draw_bubble(page, (left, top, box_w, box_h), bubble, style)

        if style.border > 0:
            draw.rectangle([left, top, right, bottom], outline=style.ink, width=style.border)

    return page


def public(layout: Layout) -> dict:
    return {
        "id": layout.id,
        "label": layout.label,
        "count": layout.count,
        "aspect": round(layout.aspect, 4),
        "note": layout.note,
        "panels": [
            {"x": p.x, "y": p.y, "w": p.w, "h": p.h} for p in layout.panels
        ],
    }

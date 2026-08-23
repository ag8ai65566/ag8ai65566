"""Style recipes: reusable rendering / lighting / composition combinations.

These are not artist imitation. Each one is a small bundle of tags that changes
how a picture is *rendered* - line, shading, palette, light, camera - and can be
dropped on top of whatever character prompt the user already has.

The seed list came from a written spec. **Every tag in it was re-checked against
danbooru's API before shipping, and 47% of the spec's tags did not exist.**
Phrases like `clean lineart`, `dramatic lighting`, `cinematic composition`,
`detailed eyes`, `rim light`, `volumetric lighting`, `cel shading` and
`detailed background` have zero danbooru posts. That does not make them useless -
CLIP reads English, and quicktags.py explains at length why a zero-post phrase
still produces an effect - but on a danbooru-trained finetune a real tag is the
sharper lever, so where a real tag means the same thing, the real tag ships and
the invented phrase is recorded in REPLACED so the substitution is auditable.

Three tag kinds are distinguished, because "zero danbooru posts" means three
completely different things:

  ``danbooru``   A real tag with a real post count. The finetune saw this exact
                 string thousands of times.
  ``caption``    Zero danbooru posts, but injected into the captions at training
                 time by the checkpoint author - the quality words, the date
                 buckets, Illustrious's `displeasing`. Verified against the model
                 card, not against danbooru. These are the strongest tokens of
                 all and the post count says nothing about them.
  ``plain``      Ordinary English with no special training. Works through CLIP
                 alone. Kept only where nothing better exists, and labelled.

One substitution is worth calling out on its own. The spec recommends the tag
``2d`` in its "Matte 2D / Anti AI Gloss" recipe. On danbooru ``2d`` is an active
alias of ``nidy`` - **an artist tag, 409 posts**. Typing it into NoobAI or
Illustrious asks for one specific artist's style, which is the opposite of what
that recipe is for. It is not shipped.

Nothing here has been generated. No image has come out of this project - there
is no GPU in the machine it was built on - so every claim about what a recipe
looks like is a claim about the tags, not about a picture.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


# --- one tag ---------------------------------------------------------------

@dataclass(frozen=True)
class Chip:
    """One tag inside a recipe.

    ``posts`` is danbooru prevalence and is meaningful only when
    ``kind == "danbooru"``; for a caption token it is 0 by definition and the
    ``source`` field says which model card the token came from instead.
    """

    tag: str
    zh: str
    category: str
    posts: int = 0
    kind: str = "danbooru"       # danbooru | caption | plain
    natural: str = ""            # spelling for a natural-language checkpoint
    source: str = ""             # for caption tokens: where it is documented
    note: str = ""

    @property
    def prompt(self) -> str:
        """danbooru stores underscores; checkpoints want spaces, parens escaped."""
        return re.sub(r"([()])", r"\\\1", self.tag.replace("_", " "))

    def emit(self, tag_style: str = "danbooru") -> str:
        if tag_style == "natural" and self.natural:
            return self.natural
        return self.prompt

    @property
    def strength(self) -> str:
        if self.kind == "caption":
            return "caption"
        if self.kind == "plain":
            return "plain"
        if self.posts >= 100000:
            return "strong"
        if self.posts >= 10000:
            return "solid"
        if self.posts >= 1000:
            return "thin"
        return "rare"

    def public(self) -> dict:
        return {
            "tag": self.prompt, "zh": self.zh, "category": self.category,
            "posts": self.posts, "kind": self.kind, "strength": self.strength,
            "natural": self.natural or self.prompt,
            "source": self.source, "note": self.note,
        }


def C(tag, zh, category, posts=0, **kw) -> Chip:
    return Chip(tag=tag, zh=zh, category=category, posts=posts, **kw)


# --- the shared vocabulary -------------------------------------------------
# Defined once so a tag cannot drift between two recipes, and so the post count
# is stated in exactly one place.

V: dict[str, Chip] = {c.tag: c for c in [
    # aesthetic / medium
    C("official_art", "官方宣傳圖", "aesthetic", 533826,
      natural="official promotional artwork"),
    C("key_visual", "主視覺立繪", "composition", 3361, natural="key visual"),
    C("anime_screenshot", "動畫截圖", "aesthetic", 15644,
      natural="a frame from a TV anime",
      note="規格書寫的 `anime screencap` 在 danbooru 是別名，正式名稱是這個。"),
    C("anime_coloring", "動畫上色", "color", 55535, natural="anime style coloring"),
    C("game_asset", "遊戲美術素材", "medium", 169726, natural="game CG artwork",
      note="`game cg` 在 danbooru 是這個 tag 的別名。它涵蓋立繪與介面素材，不只是過場 CG。"),
    C("comic", "漫畫", "medium", 724516, natural="manga page",
      note="`manga` 是它的別名。注意 Illustrious 官方範例把 `comic` 放在**負面**——它會讓畫面變成多格。"),
    C("1990s_(style)", "90 年代畫風", "aesthetic", 13043, natural="1990s anime style"),
    C("retro_artstyle", "復古畫風", "aesthetic", 24414, natural="retro anime art style"),
    C("traditional_media", "傳統媒材", "medium", 125177, natural="traditional media"),
    C("watercolor_(medium)", "水彩", "medium", 22294, natural="watercolor painting"),
    C("painting_(medium)", "繪畫", "medium", 30754, natural="painted illustration"),
    C("ink_(medium)", "墨", "medium", 974, natural="ink drawing"),
    C("paper_texture", "紙張質感", "aesthetic", 1276, natural="visible paper texture"),
    C("film_grain", "膠片顆粒", "aesthetic", 26515, natural="film grain"),
    C("cyberpunk", "賽博龐克", "aesthetic", 4348, natural="cyberpunk"),
    C("fashion", "時裝", "aesthetic", 10444, natural="fashion illustration"),

    # line / colour
    C("lineart", "線稿感", "line", 16478, natural="clean crisp lineart"),
    C("thick_outlines", "粗輪廓線", "line", 646, natural="thick bold outlines"),
    C("hatching_(texture)", "排線", "line", 13985, natural="cross-hatching"),
    C("flat_color", "平塗上色", "color", 13671, natural="flat cel shading"),
    C("muted_colors", "低飽和", "color", 9114, natural="muted desaturated colors"),
    C("pastel_colors", "粉彩色", "color", 4736, natural="soft pastel palette"),
    C("monochrome", "單色", "color", 845872, natural="monochrome"),
    C("greyscale", "灰階", "color", 684946, natural="greyscale"),
    C("screentones", "網點", "color", 5644, natural="manga screentones"),
    C("spot_color", "單點著色", "color", 62361, natural="mostly monochrome with one colour"),

    # lighting
    C("backlighting", "逆光", "lighting", 45276, natural="backlit, rim light"),
    C("sidelighting", "側光", "lighting", 12975, natural="strong side lighting"),
    C("light_rays", "光束", "lighting", 33080, natural="visible rays of light"),
    C("sunbeam", "陽光光柱", "lighting", 13261, natural="sunbeams"),
    C("dappled_sunlight", "樹影光斑", "lighting", 15030, natural="dappled sunlight"),
    C("lens_flare", "鏡頭光暈", "lighting", 50232, natural="lens flare"),
    C("bloom", "光暈溢出", "lighting", 5379, natural="soft glowing bloom"),
    C("chiaroscuro", "明暗對照", "lighting", 436, natural="chiaroscuro, harsh light and shadow"),
    C("golden_hour", "黃金時刻", "lighting", 380, natural="golden hour light"),
    C("moonlight", "月光", "lighting", 4779, natural="moonlight"),
    C("neon_lights", "霓虹燈", "lighting", 3545, natural="neon lights"),
    C("sunlight", "陽光", "lighting", 101848, natural="sunlight"),
    C("silhouette", "剪影", "lighting", 22789, natural="silhouette"),

    # camera
    C("depth_of_field", "淺景深", "camera", 124871, natural="shallow depth of field"),
    C("bokeh", "散景", "camera", 10674, natural="bokeh"),
    C("motion_blur", "動態模糊", "camera", 34656, natural="motion blur"),
    C("dutch_angle", "傾斜取鏡", "camera", 161959, natural="dutch angle"),
    C("foreshortening", "強透視縮短", "camera", 68970, natural="dramatic foreshortening"),
    C("wide_shot", "遠景", "camera", 23572, natural="wide shot"),
    C("letterboxed", "電影黑邊", "camera", 69198, natural="letterboxed cinematic framing"),
    C("close-up", "特寫", "camera", 63178, natural="close-up",
      note="Illustrious 官方明說 `close-up` 這類構圖 tag 不要濫用，容易互相打架。"),
    C("portrait", "胸上人像", "camera", 141191, natural="portrait framing"),
    C("upper_body", "上半身", "camera", 1180450, natural="upper body"),
    C("vignetting", "暗角", "camera", 2742, natural="vignette"),
    C("chromatic_aberration", "色差", "camera", 38369, natural="chromatic aberration"),

    # detail
    C("eyelashes", "睫毛", "detail", 262052, natural="detailed eyelashes"),
    C("sparkling_eyes", "亮眼／眼神光", "detail", 18499, natural="sparkling eyes with catchlights"),
    C("eye_focus", "聚焦在眼睛", "detail", 4156, natural="focus on the eyes"),
    C("blush", "臉紅", "detail", 4059319, natural="light blush"),
    C("frills", "荷葉邊", "detail", 764703, natural="frilled clothing"),
    C("lace", "蕾絲", "detail", 49229, natural="lace trim"),
    C("gold_trim", "金邊裝飾", "detail", 72940, natural="gold trim"),
    C("embroidery", "刺繡", "detail", 2082, natural="embroidery"),
    C("jewelry", "首飾", "detail", 1582638, natural="jewelry"),
    C("floating_hair", "髮絲飄動", "detail", 191933, natural="hair floating in the air"),
    C("wind_lift", "被風吹起", "detail", 18999, natural="clothes and hair lifted by wind"),
    C("hair_flowing_over", "髮絲覆蓋", "detail", 7374, natural="strands of hair falling across"),
    C("messy_hair", "凌亂髮", "detail", 91081, natural="slightly messy hair"),

    # background / atmosphere
    C("scenery", "有景色的背景", "background", 74281, natural="detailed scenery"),
    C("atmospheric_perspective", "空氣透視", "background", 359, natural="atmospheric perspective, hazy distance"),
    C("simple_background", "純色背景", "background", 2821203, natural="plain simple background"),
    C("night", "夜晚", "background", 169161, natural="at night"),
    C("sunset", "夕陽", "background", 39003, natural="sunset"),
    C("rain", "下雨", "background", 48276, natural="rain"),
    C("puddle", "水窪", "background", 8012, natural="puddles on the ground"),
    C("reflective_floor", "反光地面", "background", 4942, natural="wet reflective ground"),
    C("reflection", "倒影", "background", 55899, natural="reflections"),
    C("wet", "潮濕", "background", 193567, natural="wet"),
    C("cityscape", "城市遠景", "background", 23872, natural="cityscape"),
    C("city_lights", "城市燈光", "background", 6846, natural="city lights"),
    C("starry_sky", "星空", "background", 52714, natural="starry sky"),
    C("fog", "霧", "atmosphere", 7642, natural="fog"),
    C("embers", "飛散火星", "atmosphere", 6654, natural="drifting embers"),
    C("light_particles", "光點粒子", "atmosphere", 80463, natural="floating light particles"),
    C("sparkle", "閃光", "atmosphere", 228986, natural="sparkles"),
    C("magic", "魔法", "atmosphere", 23232, natural="magic"),
    C("magic_circle", "魔法陣", "background", 13034, natural="a magic circle"),
    C("aura", "氣場光暈", "atmosphere", 18792, natural="glowing aura"),
    C("light_trail", "光軌", "atmosphere", 6338, natural="trails of light"),
    C("glowing", "發光", "atmosphere", 137655, natural="glowing"),
    C("crystal", "水晶", "detail", 35603, natural="crystals"),
    C("dark", "昏暗", "aesthetic", 19582, natural="dark, low-key"),
    C("black_theme", "黑色主調", "color", 2341, natural="black colour scheme"),

    # composition / motion
    C("dynamic_pose", "動態姿勢", "composition", 3872, natural="dynamic action pose"),
    C("speed_lines", "速度線", "composition", 14224, natural="speed lines"),
    C("motion_lines", "動作線", "composition", 121089, natural="motion lines"),
    C("emphasis_lines", "集中線", "composition", 47015, natural="emphasis lines"),

    # negatives that are real tags
    C("3d", "3D 渲染", "negative", 29256, natural="3d render"),
    C("realistic", "寫實", "negative", 32450, natural="photorealistic"),
    C("photorealistic", "照片寫實", "negative", 1750, natural="photorealistic"),
    C("shiny_skin", "油亮皮膚", "negative", 156524, natural="glossy oily skin",
      note="規格書寫 `glossy skin`(0 張) 與 `plastic skin`(28 張)；danbooru 真正在用的是這個，156,524 張。"),
    C("sketch", "草稿感", "negative", 194140, natural="rough sketch"),
]}


# --- caption-time tokens ----------------------------------------------------
# Zero danbooru posts by construction: the checkpoint author injects them from
# score percentiles and upload dates. Verified against the model cards, quoted
# in docs/style-library.md.

QUALITY: dict[str, Chip] = {c.tag: c for c in [
    C("masterpiece", "最高品質（前 5%）", "quality", kind="caption",
      source="NoobAI-XL 1.1 model card：>95th percentile"),
    C("best_quality", "高品質（前 5-15%）", "quality", kind="caption",
      source="NoobAI-XL 1.1 model card：>85th, <=95th"),
    C("good_quality", "中上品質", "quality", kind="caption",
      source="NoobAI-XL 1.1 model card：>60th, <=85th"),
    C("normal_quality", "普通品質", "quality", kind="caption",
      source="NoobAI-XL 1.1 model card：>30th, <=60th"),
    C("worst_quality", "最低品質", "quality", kind="caption",
      source="NoobAI-XL 1.1 model card：<=30th"),
    C("bad_quality", "低品質", "quality", kind="caption",
      source="Illustrious-XL v0.1 model card 的支援品質詞"),
    C("average_quality", "中等品質", "quality", kind="caption",
      source="Illustrious-XL v0.1 model card 的支援品質詞"),
    C("displeasing", "不討喜", "quality", kind="caption",
      source="Illustrious-XL v0.1 官方負面範例"),
    C("very_displeasing", "非常不討喜", "quality", kind="caption",
      source="Illustrious-XL v0.1 官方負面範例"),
    C("absurdres", "超高解析原圖", "quality", 2945158,
      note="這個**是**真 danbooru tag（294 萬張），不是合成詞。"),
    C("highres", "高解析原圖", "quality", 8045436),
    C("lowres", "低解析原圖", "quality", 112381),
]}

# NoobAI's date buckets, straight off its model card. Exactly five, and they are
# mutually exclusive - the spec's list added a sixth ("oldest") that is not one.
ERAS: dict[str, Chip] = {c.tag: c for c in [
    C("old", "2005-2010 畫風", "era", kind="caption", source="NoobAI-XL 1.1 model card"),
    C("early", "2011-2014 畫風", "era", kind="caption", source="NoobAI-XL 1.1 model card"),
    C("mid", "2014-2017 畫風", "era", kind="caption", source="NoobAI-XL 1.1 model card"),
    C("recent", "2018-2020 畫風", "era", kind="caption", source="NoobAI-XL 1.1 model card"),
    C("newest", "2021-2024 畫風", "era", kind="caption", source="NoobAI-XL 1.1 model card"),
]}

ALL_CHIPS: dict[str, Chip] = {**V, **QUALITY, **ERAS}


# --- what was substituted, and why ------------------------------------------
# Kept as data so the spec author can audit every change in one place, and so a
# test can assert that nothing invented slipped back into a recipe.

REPLACED: dict[str, tuple[str, str]] = {
    # spec tag              -> (what ships, why)
    "2d": ("(不出貨)", "danbooru 上 `2d` 是畫師 `nidy` 的別名，409 張。打進 NoobAI 會叫出某一位畫師的風格，跟這個配方的目的正好相反。"),
    "anime screencap": ("anime screenshot", "別名，正式名稱是 anime_screenshot（15,644 張）。"),
    "game cg": ("game asset", "別名，正式名稱是 game_asset（169,726 張）。"),
    "manga": ("comic", "別名，正式名稱是 comic（724,516 張）。"),
    "clean lineart": ("lineart", "0 張。lineart 有 16,478 張。"),
    "delicate lineart": ("lineart", "0 張。"),
    "soft edges": ("(移除)", "0 張，且傳統媒材配方裡 watercolor (medium) 已經帶到這個效果。"),
    "cel shading": ("flat color", "0 張。flat_color 有 13,671 張，是 danbooru 對平塗的正式說法。"),
    "simple shading": ("flat color", "0 張。"),
    "soft shading": ("(移除)", "0 張，沒有對應的 danbooru tag。"),
    "subtle shading": ("(移除)", "0 張。"),
    "soft skin shading": ("(移除)", "0 張。"),
    "matte colors": ("muted colors", "0 張。muted_colors 有 9,114 張。"),
    "cel animation": ("anime screenshot", "0 張。"),
    "retro anime": ("retro artstyle", "0 張。retro_artstyle 有 24,414 張。"),
    "light novel illustration": ("official art", "0 張。"),
    "fashion illustration": ("fashion", "0 張。fashion 有 10,444 張。"),
    "dark fantasy": ("dark", "0 張。dark 有 19,582 張。"),
    "rim light": ("backlighting", "0 張。backlighting 有 45,276 張，是同一件事的 danbooru 說法。"),
    "rim lighting": ("backlighting", "danbooru 0 張——但**Illustrious 官方範例提詞裡有它**，所以它在那個模型上不是死詞。這裡仍用 backlighting，因為它在 NoobAI 上更保險。"),
    "warm rim light": ("backlighting", "0 張。"),
    "dramatic lighting": ("light rays / sidelighting", "0 張。改用有實體的 light_rays（33,080）或 sidelighting（12,975）。"),
    "volumetric lighting": ("light rays", "0 張。"),
    "studio lighting": ("(移除)", "0 張，且 studio 本身只有 288 張。"),
    "soft lighting": ("bloom", "0 張。bloom 有 5,379 張。"),
    "soft glow": ("bloom", "0 張。"),
    "colored lighting": ("neon lights", "0 張，在賽博配方裡實際想要的是 neon_lights（3,545）。"),
    "dynamic shadows": ("sidelighting", "0 張。"),
    "long shadows": ("(移除)", "0 張。"),
    "harsh shadows": ("(移除)", "0 張。"),
    "harsh contrast": ("(移除)", "0 張。"),
    "catchlight": ("sparkling eyes", "0 張。sparkling_eyes 有 18,499 張，眼神光就是它。"),
    "subtle highlights": ("(移除)", "0 張。"),
    "light reflecting on hair": ("(移除)", "0 張，`shiny hair` 也是 0 張。"),
    "detailed eyes": ("sparkling eyes / eye focus", "0 張。"),
    "detailed face": ("portrait", "0 張。"),
    "face focus": ("portrait", "0 張。"),
    "subtle blush": ("blush", "0 張。blush 有 405 萬張。"),
    "detailed hair strands": ("floating hair", "0 張。"),
    "flyaway hair": ("floating hair / wind lift", "0 張。"),
    "detailed fabric": ("frills / lace / embroidery", "0 張。改成講得出來的布料細節。"),
    "intricate costume": ("gold trim / frills / jewelry", "0 張。"),
    "detailed background": ("scenery", "0 張。scenery 有 74,281 張。"),
    "environmental storytelling": ("(移除)", "0 張，而且它描述的是意圖不是畫面。"),
    "clean background": ("simple background", "0 張。simple_background 有 282 萬張。"),
    "background": ("(移除)", "0 張，單獨當 tag 沒有意義。"),
    "foreground": ("(移除)", "0 張。"),
    "balanced composition": ("(移除)", "0 張。"),
    "cinematic composition": ("letterboxed / wide shot", "0 張。letterboxed（69,198）才是畫面上真的看得出來的東西。"),
    "dynamic composition": ("dynamic pose / foreshortening", "0 張。"),
    "dramatic perspective": ("foreshortening", "0 張。foreshortening 有 68,970 張。"),
    "perspective in effects": ("light trail", "0 張。"),
    "floating particles": ("light particles", "0 張。light_particles 有 80,463 張。"),
    "glowing particles": ("light particles", "0 張。"),
    "energy trails": ("light trail", "0 張。light_trail 有 6,338 張。"),
    "volumetric fog": ("fog", "0 張。fog 有 7,642 張。"),
    "wet street": ("puddle / reflective floor / wet", "0 張。"),
    "reflections": ("reflection", "0 張——差一個 s。單數 reflection 有 55,899 張。"),
    "dreamy": ("(移除)", "0 張，形容詞不是畫面。"),
    "elegant": ("(移除)", "0 張。"),
    "spot color": ("(移除)", "62,361 張是真 tag，但它的意思是「整張黑白只留一個顏色」。放進「霧面 2D」配方會把圖推向單色，跟原意相反。"),
    "glossy skin": ("shiny skin", "0 張。shiny_skin 有 156,524 張。"),
    "oily skin": ("shiny skin", "0 張。"),
    "plastic skin": ("shiny skin", "只有 28 張，太薄。"),
    "plastic": ("3d", "0 張。"),
    "cgi": ("3d", "0 張。"),
    "oversaturated": ("(移除)", "0 張。"),
    "full color": ("(移除)", "0 張。想要黑白就正面加 monochrome，不需要負面。"),
    "static pose": ("(移除)", "0 張。"),
    "newest": ("(移除，負面用法)", "它是 NoobAI 的**年代桶**（2021-2024），不是品質詞。放進負面等於排除近代畫風，在 90 年代配方裡剛好會被誤讀成對的，但理由是錯的——直接正面寫 `old` 或 `early` 才對。"),
    "worst detail": ("(移除)", "0 張，也不在任何官方 model card 裡。"),
}


# --- recipes ----------------------------------------------------------------

ANIME = ("noobai", "illustrious", "pony")
ALL_MODELS = ("noobai", "illustrious", "pony", "juggernaut", "sdxl-base")


@dataclass(frozen=True)
class Recipe:
    id: str
    zh: str
    en: str
    desc: str
    chips: tuple[str, ...]
    negative: tuple[str, ...] = ()
    models: tuple[str, ...] = ANIME
    keywords: tuple[str, ...] = ()
    note: str = ""

    def resolve(self, names: tuple[str, ...]) -> list[Chip]:
        return [ALL_CHIPS[n] for n in names]

    def prompt(self, tag_style: str = "danbooru") -> str:
        return ", ".join(c.emit(tag_style) for c in self.resolve(self.chips))

    def negative_prompt(self, tag_style: str = "danbooru") -> str:
        return ", ".join(c.emit(tag_style) for c in self.resolve(self.negative))

    def public(self, tag_style: str = "danbooru") -> dict:
        return {
            "id": self.id, "zh": self.zh, "en": self.en, "desc": self.desc,
            "models": list(self.models), "keywords": list(self.keywords),
            "note": self.note,
            "chips": [c.public() for c in self.resolve(self.chips)],
            "negative": [c.public() for c in self.resolve(self.negative)],
            "prompt": self.prompt(tag_style),
            "negative_prompt": self.negative_prompt(tag_style),
        }


RECIPES: list[Recipe] = [
    Recipe(
        "clean-anime-keyvisual", "清爽官方動畫 Key Visual", "Clean Anime Key Visual",
        "乾淨線條、動畫上色、官方宣傳圖感。先用這個把泛用的 AI 塑膠味去掉。",
        chips=("official_art", "anime_coloring", "lineart", "flat_color", "key_visual"),
        negative=("3d", "realistic", "photorealistic"),
        models=ANIME, keywords=("anime", "official", "clean", "key visual", "乾淨", "官方"),
    ),
    Recipe(
        "anime-screencap-flat", "真正動畫截圖感", "Anime Screencap / Flat Cel",
        "更像電視動畫的一格，而不是精修插畫。線粗、色平、沒有多餘打光。",
        chips=("anime_screenshot", "anime_coloring", "flat_color", "thick_outlines", "lineart"),
        negative=("3d", "realistic", "shiny_skin"),
        models=ANIME, keywords=("tv anime", "flat", "screencap", "cel", "截圖", "平塗"),
    ),
    Recipe(
        "matte-2d-no-ai-gloss", "霧面 2D／去 AI 油亮感", "Matte 2D / Anti AI Gloss",
        "專門對付常見的反光、塑膠、2.5D 感。把皮膚的高光壓掉，色彩壓低。",
        chips=("flat_color", "muted_colors", "lineart", "anime_coloring"),
        negative=("3d", "realistic", "photorealistic", "shiny_skin"),
        models=ANIME, keywords=("matte", "flat", "no gloss", "霧面", "去油亮"),
        note="規格書原本在這裡放 `2d`——那在 danbooru 是畫師 nidy 的別名，會叫出一位特定畫師，已移除。`spot color` 也移除了，它的意思是「黑白只留一色」。",
    ),
    Recipe(
        "cinematic-anime", "電影感動漫", "Cinematic Anime",
        "戲劇光線、淺景深、電影黑邊。人物之外的氣氛全靠這幾個。",
        chips=("depth_of_field", "backlighting", "light_rays", "film_grain",
               "letterboxed", "atmospheric_perspective", "lens_flare"),
        models=ANIME + ("juggernaut", "sdxl-base"),
        keywords=("cinematic", "movie", "film", "dramatic", "電影"),
    ),
    Recipe(
        "soft-light-novel", "柔和輕小說封面", "Soft Light Novel Cover",
        "柔光、細線、粉彩、漂亮的眼睛。封面插畫的路子。",
        chips=("official_art", "lineart", "pastel_colors", "bloom",
               "sparkling_eyes", "blush", "depth_of_field"),
        negative=("3d", "realistic"),
        models=("noobai", "illustrious"),
        keywords=("light novel", "soft", "pastel", "cover", "輕小說", "柔和"),
    ),
    Recipe(
        "gacha-key-art", "手遊角色 Key Art", "Gacha Character Key Art",
        "華麗服裝、金邊、首飾、光點。商業立繪那一套。",
        chips=("official_art", "key_visual", "gold_trim", "frills", "lace",
               "jewelry", "light_particles", "dynamic_pose", "scenery"),
        models=ANIME, keywords=("gacha", "key art", "手遊", "立繪", "華麗"),
    ),
    Recipe(
        "game-cg", "高質感遊戲 CG", "Game CG",
        "比電視動畫精細，但仍是 2D 動漫角色。適合有背景的整張圖。",
        chips=("game_asset", "anime_coloring", "sparkling_eyes", "eyelashes",
               "scenery", "bloom", "depth_of_field"),
        negative=("photorealistic",),
        models=ANIME, keywords=("game cg", "visual novel", "遊戲", "galgame"),
    ),
    Recipe(
        "dreamy-pastel", "夢幻粉彩", "Dreamy Pastel",
        "柔光、粉彩、散景、浮動光點。整張圖的對比壓到很低。",
        chips=("pastel_colors", "bloom", "bokeh", "backlighting", "light_particles",
               "sparkle", "depth_of_field"),
        models=ANIME, keywords=("dreamy", "pastel", "soft", "夢幻", "粉彩"),
    ),
    Recipe(
        "golden-hour", "黃金時刻逆光", "Golden Hour Backlight",
        "最省事的一組打光。只加光線不動人物，對品質的提升通常最明顯。",
        chips=("golden_hour", "sunset", "backlighting", "sunbeam",
               "atmospheric_perspective", "lens_flare"),
        models=ALL_MODELS, keywords=("golden hour", "sunset", "warm", "黃金時刻", "逆光"),
        note="`golden hour` 只有 380 張，是這一組裡最薄的一個；真正在扛的是 sunset（39,003）跟 backlighting（45,276）。",
    ),
    Recipe(
        "moonlit-blue", "月夜冷色光", "Moonlit Blue",
        "夜景人物、冷色調、藍色逆光、空氣感。",
        chips=("night", "moonlight", "backlighting", "light_rays",
               "atmospheric_perspective", "starry_sky"),
        models=ALL_MODELS, keywords=("night", "moon", "blue", "cool", "月夜", "冷色"),
    ),
    Recipe(
        "neon-cyberpunk", "霓虹賽博動漫", "Neon Cyberpunk",
        "彩色光源、雨夜反射、霓虹邊光。",
        chips=("cyberpunk", "neon_lights", "city_lights", "backlighting", "rain",
               "reflection", "depth_of_field", "light_particles", "cityscape"),
        models=ALL_MODELS, keywords=("cyberpunk", "neon", "city", "賽博", "霓虹"),
    ),
    Recipe(
        "dark-fantasy", "暗黑奇幻插畫", "Dark Fantasy",
        "高對比、煙霧、飛散火星、華麗服裝。",
        chips=("dark", "chiaroscuro", "sidelighting", "embers", "fog",
               "gold_trim", "black_theme"),
        models=ANIME, keywords=("dark", "fantasy", "gothic", "暗黑", "奇幻"),
    ),
    Recipe(
        "watercolor", "水彩動漫插畫", "Watercolor Anime",
        "傳統媒材那一組在 NoobAI 上反應通常不錯，值得單獨試。",
        chips=("watercolor_(medium)", "traditional_media", "painting_(medium)",
               "paper_texture", "muted_colors"),
        negative=("3d",),
        models=("noobai", "illustrious"),
        keywords=("watercolor", "traditional", "painting", "水彩", "傳統"),
    ),
    Recipe(
        "ink-manga", "墨線漫畫", "Ink Manga",
        "黑白、網點、排線、乾淨墨線。",
        chips=("monochrome", "greyscale", "ink_(medium)", "lineart",
               "screentones", "hatching_(texture)"),
        models=("noobai", "illustrious"),
        keywords=("manga", "monochrome", "ink", "screentone", "漫畫", "黑白"),
        note="沒有放 `comic`：它雖然是 `manga` 的正式名稱，但 Illustrious 官方範例把 comic 放在**負面**，因為它會讓畫面變成多格分鏡。想要分鏡再自己加。",
    ),
    Recipe(
        "retro-90s", "90 年代動畫", "Retro 90s Anime",
        "舊動畫截圖、膠片顆粒、低飽和。",
        chips=("1990s_(style)", "retro_artstyle", "anime_screenshot",
               "film_grain", "muted_colors", "thick_outlines"),
        models=ANIME, keywords=("90s", "retro", "vintage", "復古", "老動畫"),
        note="規格書把 `newest` 放進負面。`newest` 是 NoobAI 的年代桶（2021-2024）不是品質詞——想要舊畫風，正面直接寫 `old` 或 `early` 才是它訓練時的用法。",
    ),
    Recipe(
        "dynamic-action", "動態戰鬥構圖", "Dynamic Action",
        "姿勢、透視、鏡頭。這三個比再堆二十個 detail 形容詞有用得多。",
        chips=("dynamic_pose", "foreshortening", "dutch_angle", "motion_blur",
               "speed_lines", "motion_lines", "emphasis_lines"),
        models=ANIME, keywords=("action", "fight", "dynamic", "戰鬥", "動態"),
    ),
    Recipe(
        "beauty-closeup", "精緻人物近景", "Beauty Close-up",
        "把像素集中在臉、眼睛、皮膚。通常比 ultra detailed 那類詞有效。",
        chips=("portrait", "upper_body", "eye_focus", "sparkling_eyes",
               "eyelashes", "blush", "depth_of_field"),
        models=ALL_MODELS, keywords=("portrait", "closeup", "face", "eyes", "近景", "臉"),
        note="沒有放 `close-up`：Illustrious 官方說明白寫它跟其他構圖 tag 容易互相打架，建議不要濫用。想要更近再自己加。",
    ),
    Recipe(
        "hair-detail", "髮絲質感", "Hair Detail",
        "不要只寫 detailed hair。給它一個會動的理由，髮絲才會被畫出來。",
        chips=("floating_hair", "wind_lift", "hair_flowing_over", "messy_hair",
               "backlighting", "depth_of_field"),
        models=ANIME, keywords=("hair", "strands", "wind", "髮絲", "頭髮"),
    ),
    Recipe(
        "environmental-portrait", "人物＋高資訊背景", "Environmental Portrait",
        "不是寫 detailed background 就會有背景。要給空間層次跟具體場景。",
        chips=("scenery", "atmospheric_perspective", "depth_of_field",
               "wide_shot", "sunlight", "cityscape"),
        negative=("simple_background",),
        models=ALL_MODELS, keywords=("scenery", "environment", "background", "背景", "場景"),
    ),
    Recipe(
        "magic-effects", "魔法特效插畫", "Magic Effects",
        "用前後景的特效跟光軌把畫面填滿。",
        chips=("magic", "magic_circle", "light_particles", "light_trail",
               "glowing", "aura", "sidelighting", "crystal"),
        models=ANIME, keywords=("magic", "effects", "spell", "魔法", "特效"),
    ),
    Recipe(
        "fashion-portrait", "時裝人物插畫", "Fashion Portrait",
        "衣料、飾品、輪廓、乾淨背景。走時裝插畫而不是動畫的路子。",
        chips=("fashion", "frills", "lace", "embroidery", "jewelry",
               "upper_body", "simple_background", "sidelighting"),
        models=ALL_MODELS, keywords=("fashion", "clothes", "elegant", "時裝", "服裝"),
    ),
    Recipe(
        "rainy-cinematic", "雨夜電影感", "Rainy Cinematic",
        "雨、水窪反光、逆光、散景、顆粒。角色氛圍最好用的一組。",
        chips=("rain", "wet", "puddle", "reflective_floor", "backlighting",
               "bokeh", "film_grain", "night"),
        models=ALL_MODELS, keywords=("rain", "wet", "night", "cinematic", "雨", "夜"),
    ),
]

BY_ID = {r.id: r for r in RECIPES}


def get(recipe_id: str) -> Recipe | None:
    return BY_ID.get(recipe_id)


# --- quality presets --------------------------------------------------------
# Deliberately separate from the style recipes: a recipe changes how the picture
# looks, a quality preset is the checkpoint's own scaffolding. Mixing the two is
# how people end up with nine buzzwords they cannot explain.
#
# Every string below is quoted from a model card, not from community folklore.

@dataclass(frozen=True)
class Preset:
    id: str
    zh: str
    models: tuple[str, ...]
    positive: str
    negative: str
    source: str
    note: str = ""

    def public(self) -> dict:
        return {
            "id": self.id, "zh": self.zh, "models": list(self.models),
            "positive": self.positive, "negative": self.negative,
            "source": self.source, "note": self.note,
        }


PRESETS: list[Preset] = [
    Preset(
        "noobai-official", "NoobAI 官方建議", ("noobai",),
        "masterpiece, best quality, newest, absurdres, highres",
        "worst quality, old, early, low quality, lowres, signature, username, logo",
        "Laxhar/noobai-XL-1.1 model card 的範例提詞",
        "官方範例正面還有 `safe`、負面還有 `nsfw`，這裡兩個都拿掉了——這個工具沒有內容過濾，"
        "偷偷幫你否定掉你要的東西比預設值難看多了。要全年齡自己加 `safe`。",
    ),
    Preset(
        "illustrious-official", "Illustrious 官方建議", ("illustrious",),
        "masterpiece, best quality",
        "worst quality, bad quality, low quality, lowres, displeasing, very displeasing, "
        "bad anatomy, bad hands, scan artifacts, signature, twitter username, jpeg artifacts, "
        "extra digits, fewer digits",
        "OnomaAIResearch/Illustrious-xl-early-release-v0 model card 的範例提詞",
        "注意：base Illustrious 的官方品質詞只有 worst / bad / average / good / best quality "
        "跟 masterpiece。常看到的 `amazing quality`、`very aesthetic` **不是**它的——那是 WAI "
        "跟 Animagine 這些微調自己加的詞。官方負面本來還有 comic、monochrome、greyscale、"
        "2koma、4koma、multiple views，這裡拿掉了，不然你就畫不出黑白漫畫。",
    ),
    Preset(
        "pony-official", "Pony 官方 score 串", ("pony",),
        "score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up",
        "score_6, score_5, score_4",
        "Pony Diffusion V6 XL 官方頁",
        "官方明說「只用 score_9 的效果比完整這串弱很多」，所以六個要寫完。",
    ),
    Preset(
        "minimal", "極簡（只留一個品質詞）", ANIME,
        "masterpiece",
        "worst quality, lowres",
        "NoobAI / Illustrious 品質詞表的最上與最下一格",
        "值得一試的對照組。品質詞是從分數百分位反推出來的，堆再多也只是把同一個方向重複講；"
        "真正決定細節的常常是解析度跟步數，不是提詞長度。",
    ),
    Preset(
        "anti-gloss", "去 AI 塑膠感", ANIME,
        "anime coloring, flat color",
        "3d, realistic, photorealistic, shiny skin",
        "本專案：全部是查證過的 danbooru tag",
        "規格書這裡寫的是 `cel shading`(0 張)、`glossy skin`(0 張)、`plastic skin`(28 張)；"
        "換成 danbooru 真的在用的 flat_color(13,671) 跟 shiny_skin(156,524)。",
    ),
]

PRESET_BY_ID = {p.id: p for p in PRESETS}


def presets_for(model_id: str) -> list[Preset]:
    return [p for p in PRESETS if model_id in p.models]


def recipes_for(model_id: str = "") -> list[Recipe]:
    if not model_id:
        return list(RECIPES)
    return [r for r in RECIPES if model_id in r.models]


def search(query: str, model_id: str = "") -> list[Recipe]:
    """Match on title, description, keyword, or any tag inside the recipe."""
    q = query.strip().lower()
    pool = recipes_for(model_id)
    if not q:
        return pool
    out = []
    for r in pool:
        hay = " ".join([
            r.id, r.zh, r.en, r.desc, " ".join(r.keywords),
            " ".join(r.chips), " ".join(r.negative),
            " ".join(ALL_CHIPS[c].zh for c in r.chips),
        ]).lower().replace("_", " ")
        if q.replace("_", " ") in hay:
            out.append(r)
    return out


def public(model_id: str = "", tag_style: str = "danbooru") -> dict:
    return {
        "recipes": [r.public(tag_style) for r in recipes_for(model_id)],
        "presets": [p.public() for p in (presets_for(model_id) if model_id else PRESETS)],
        "eras": [c.public() for c in ERAS.values()],
        "replaced": [
            {"spec": k, "ships": v[0], "why": v[1]} for k, v in REPLACED.items()
        ],
        "counts": {
            "recipes": len(RECIPES), "chips": len(ALL_CHIPS),
            "replaced": len(REPLACED),
        },
    }

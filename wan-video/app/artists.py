"""Artist tags: who to name, what it changes, and whether this model listens.

An artist tag is the single strongest style lever these checkpoints have - one
token moves lighting, linework, colour and anatomy together in a way no pile of
adjectives will. It is also the one most people get wrong, in three ways this
module tries to close off.

**1. The tag is often not the name.** The codex the user imported writes
`artist:hiten` (37 entries) and `aritst:deadflow` (32) - danbooru has neither.
The real tags are `hiten_(hitenkei)` (921 posts) and `bee_(deadflow)` (1,321),
so those entries were naming nobody. Aliases bite the same way: `sho_(sho_lwlw)`
redirects to `todoroki_masaru`, `misu_kasumi` to `taromarun`.

**2. The prefix is per-model, and one model ignores artists entirely.**
NoobAI's own model card prompts `artist:john_kafka`; Illustrious uses
`by <name>`; Pony V6 **stripped artist names out of its training captions**, so
on Pony an artist tag does close to nothing no matter how it is spelt. That last
one is not a subtlety to leave the user to discover.

**3. "Famous illustrator" and "the model knows them" are different questions.**
What matters is how many of their pictures danbooru holds, because that is what
the finetune actually saw. Every entry here carries that number.

The style notes are my characterisation, but they are not guesses about who
these people are: each row also carries the tags that are *disproportionately*
common on that artist's posts, computed as lift over danbooru's global base rate
(frequency / base rate, floor of 300 posts). That is why `bkub` lists halftone
and 4koma while `wlop` lists red lips and realistic - measured, not remembered.
The UI shows those tags next to the note so the description can be checked.

Three artists were dropped from an otherwise mechanical roster: `kedama_milk`,
`toraishi_666` and `todoroki_masaru` all carry `loli` or `child` among their
most distinctive tags, and steering towards that is the one thing this project
does not do. The third is the artist the codex writes as `sho_(sho_lwlw)` (13
entries), so its redirect is left out too rather than pointing somewhere this
list will not go.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass(frozen=True)
class A:
    tag: str
    zh: str
    group: str
    posts: int
    style: str
    signals: tuple[str, ...] = ()
    codex: bool = False          # used by the pose codex the user imported

    @property
    def name(self) -> str:
        """danbooru stores underscores; a prompt wants spaces, parens escaped."""
        return re.sub(r"([()])", r"\\\1", self.tag.replace("_", " "))

    @property
    def strength(self) -> str:
        if self.posts >= 1500:
            return "strong"
        if self.posts >= 500:
            return "ok"
        return "weak"

    def emit(self, form: str) -> str:
        """`artist:{tag}` / `by {tag}` / `{tag}` -> the text to put in a prompt."""
        return (form or "{tag}").replace("{tag}", self.name)

    def public(self) -> dict:
        return {
            "tag": self.tag, "name": self.name, "zh": self.zh, "group": self.group,
            "posts": self.posts, "style": self.style, "codex": self.codex,
            "signals": [s.replace("_", " ") for s in self.signals],
            "strength": self.strength,
        }


ARTISTS: list[A] = [
    A("wlop", "WLOP", "厚塗寫實", 400,
      "厚塗油畫感，皮膚與布料質感很重，臉偏寫實、有唇部與鼻樑細節。畫面通常暗、對比強。",
      ("red_lips", "patreon_username", "realistic", "nose", "web_address", "lips", "artist_name", "watermark"), codex=True),
    A("nixeu", "Nixeu", "厚塗寫實", 412,
      "跟 WLOP 同一路的厚塗，但更乾淨、線條收得更利，膚色偏冷。",
      ("patreon_username", "realistic", "nose", "red_lips", "mole_on_breast", "star_hair_ornament", "web_address", "lips")),
    A("sakimichan", "Sakimichan", "厚塗寫實", 1019,
      "美式厚塗，妝感重（口紅、指甲油），肉感明顯，光打得很亮。",
      ("web_address", "lips", "watermark", "lipstick", "patreon_username", "makeup", "signature", "nail_polish")),
    A("ciloranko", "CilORanko", "通透插畫", 252,
      "清透水感，大量花瓣與粒子，白／黑洋裝配色，構圖偏全身帶景。法典裡用最多的畫師之一。",
      ("petals", "grey_background", "white_dress", "black_shoes", "flower", "holding_weapon", "black_dress", "white_gloves"), codex=True),
    A("rella", "Rella", "通透插畫", 495,
      "冷色調光粒子、飄髮、絕對領域，偶像／音樂 MV 那種發光質感。",
      ("copyright_notice", "black_sleeves", "light_particles", "aqua_hair", "thigh_boots", "headphones", "floating_hair", "zettai_ryouiki")),
    A("quasarcake", "Quasarcake", "通透插畫", 375,
      "精靈耳、光暈、披風，柔霧感的奇幻插畫，很適合 VTuber 立繪。",
      ("elf", "virtual_youtuber", "capelet", "floating_hair", "hair_intakes", "halo", "streaked_hair", "coat")),
    A("hito_komoru", "hito komoru", "通透插畫", 310,
      "冷白皮膚＋冰系元素，半身特寫、無表情、瀏海遮眼，氣氛很靜。",
      ("cropped_shoulders", "black_flower", "ice_wings", "ice", "portrait", "pale_skin", "eyes_visible_through_hair", "expressionless")),
    A("yoneyama_mai", "米山舞", "通透插畫", 322,
      "強景深＋黑底，飄髮與眼睫毛畫得很細，日系 MV 主視覺那一派。",
      ("sneakers", "floating_hair", "depth_of_field", "black_background", "eyelashes", "blurry", "aqua_eyes", "glasses")),
    A("atdan", "Atdan", "通透插畫", 1023,
      "亮面平塗＋高飽和，腿與腳的描寫特別多，常配蝴蝶、小鳥等點綴。",
      ("toenail_polish", "bare_legs", "legs", "feet", "toenails", "bird", "butterfly", "toes")),
    A("torino_aqua", "とりのささみ", "通透插畫", 604,
      "建築與花卉背景很多，水面反光，畫面資訊量大但配色柔。",
      ("architecture", "pink_flower", "rose", "flower", "water", "sword", "cup", "hair_flower")),
    A("hiten_(hitenkei)", "Hiten", "日系輕柔", 921,
      "強景深＋模糊背景，制服、和服、室內場景，日常感很強。法典裡最常出現的畫師。",
      ("depth_of_field", "plaid_clothes", "blurry", "off_shoulder", "indoors", "bag", "hairclip", "kimono"), codex=True),
    A("kantoku", "カントク", "日系輕柔", 2464,
      "格子裙、髮圈、斜角構圖，輕薄透明感，經典的「輕小說封面」畫風。",
      ("plaid_skirt", "plaid_clothes", "scrunchie", "one_side_up", "dutch_angle", "white_panties", "bra", ":o")),
    A("fuzichoco", "藤ちょこ", "日系輕柔", 1161,
      "和風大濃度：和服、花紋、樹與水，色彩層次多，畫面很滿。",
      ("floral_print", "kimono", "japanese_clothes", "wide_sleeves", "tree", "water", "flower", "hair_flower")),
    A("nardack", "Nardack", "日系輕柔", 1042,
      "華麗裝飾＋短裙絕對領域，花瓣與白手套，偏歐風奇幻。",
      ("ornate_clothes", "short_dress", "zettai_ryouiki", "petals", "white_thighhighs", "flower", "black_thighhighs", "white_gloves")),
    A("ask_(askzy)", "Ask", "日系輕柔", 612,
      "黑／白洋裝配武器，高跟鞋，人物站姿為主，乾淨俐落。",
      ("high_heels", "black_dress", "orange_hair", "character_name", "holding_weapon", "white_dress", "sword", "from_side")),
    A("wada_arco", "wada arco", "日系輕柔", 979,
      "立繪向（透明背景），狐耳、鎧甲、髮飾，Fate 系那種質感。",
      ("tachi-e", "transparent_background", "fox_tail", "fox_ears", "hair_intakes", "armor", "hair_ribbon", "animal_ear_fluff")),
    A("amashiro_natsuki", "天代菜月", "日系輕柔", 491,
      "貓耳＋過長袖子＋抱娃娃，柔軟毛絨感，非常適合可愛向。",
      ("grey_tail", "stuffed_cat", "eyebrows_hidden_by_hair", "sleeves_past_fingers", "cat_girl", "stuffed_animal", "cat_tail", "sleeves_past_wrists")),
    A("ayamy", "Ayamy", "日系輕柔", 1269,
      "VTuber 立繪大戶，髮飾多、虎牙、單眼遮髮，配色鮮明。",
      ("x_hair_ornament", "thigh_strap", "bra", "virtual_youtuber", "hair_over_one_eye", "white_thighhighs", "fang", "hairclip")),
    A("agnamore", "agnamore", "日系輕柔", 386,
      "淺景深＋模糊背景，光暈與過長袖，柔和居家感。",
      ("depth_of_field", "blurry_background", "halo", "white_panties", "blurry", "sleeves_past_wrists", "off_shoulder", "nail_polish")),
    A("yuugen", "yuugen", "日系輕柔", 582,
      "迷你裙＋分離袖＋長靴，綠／粉眼，標準的日系奇幻立繪。",
      ("green_eyes", "boots", "white_thighhighs", "detached_sleeves", "pink_eyes", "miniskirt", "one_eye_closed", "sword")),
    A("mika_pikazo", "Mika Pikazo", "鮮豔設計", 1117,
      "高飽和撞色、挑染髮、笑臉，塗鴉般的活潑感。",
      ("hairclip", "grin", "one_eye_closed", "streaked_hair", "shoes", "socks", ":d", "artist_name")),
    A("redjuice", "redjuice", "鮮豔設計", 490,
      "緊身衣＋科幻線條，冷色高光，Guilty Crown 那種設計感。",
      ("bodysuit", "zettai_ryouiki", "high_heels", "nail_polish", "small_breasts", "hair_flower", "flower", "pink_eyes")),
    A("huke", "huke", "鮮豔設計", 2841,
      "方形瞳孔、皮帶與金屬扣，黑岩射手的作者，硬派冷冽。",
      ("square_pupils", "green_collar", "sprite", "green_trim", "leather_belt", "ringed_eyes", "beard_stubble", "frilled_collar")),
    A("milkpanda", "milkpanda", "鮮豔設計", 2383,
      "網點背景＋粗眉＋長袖，擬人化題材多，插畫感強。",
      ("halftone_background", "short_eyebrows", "halftone", "personification", "thick_eyebrows", "antenna_hair", "puffy_long_sleeves", "sleeves_past_fingers"), codex=True),
    A("kurukurumagical", "kurukurumagical", "鮮豔設計", 1932,
      "彩色陰影、紅描邊、會動的呆毛，殘影與誇張表情，很跳。",
      ("colored_shadow", "ahoge_wag", "red_outline", "expressive_hair", "single_hair_intake", "xd", "afterimage", "headpat"), codex=True),
    A("kagematsuri", "kagematsuri", "鮮豔設計", 907,
      "唇下痣、鮑伯頭、丹寧與黑褲襪，現代寫真感。",
      ("mole_under_mouth", "denim", "twitter_username", "bob_cut", "lips", "blurry_background", "black_pantyhose", "mole")),
    A("lack", "lack", "鮮豔設計", 1341,
      "深膚色＋刀劍＋鎧甲，遮眼髮型，動作場面很強。",
      ("dark-skinned_female", "sword", "holding_sword", "dark_skin", "armor", "weapon", "hair_over_one_eye", "holding_weapon")),
    A("john_kafka", "john kafka", "鮮豔設計", 482,
      "串珠飾品、黑指甲、眼下痣，紅／黑背景，暗系時尚。",
      ("bead_necklace", "beads", "black_nails", "mole_under_eye", "ear_piercing", "red_background", "black_background", "mole"), codex=True),
    A("bkub", "ぶくぶ", "漫畫四格", 5833,
      "網點＋喊叫＋集中線的四格漫畫臉，極簡但辨識度極高。",
      ("halftone", "shouting", "talking", "emphasis_lines", "4koma", "two-tone_background", ":3", "chibi_only")),
    A("xinzoruo", "xinzoruo", "漫畫四格", 1640,
      "整頁無對白漫畫、Q 版、中式服裝，敘事型。",
      ("full_page_comic", "silent_comic", "2koma", "chibi_only", "chibi", "comic", "chinese_clothes", "3girls"), codex=True),
    A("bb_(baalbuddy)", "baalbuddy", "漫畫四格", 2974,
      "英文梗圖漫畫，長耳精靈、黑白、肌肉角色。",
      ("long_pointy_ears", "english_text", "elf", "greyscale", "meme", "monochrome", "facial_hair", "comic"), codex=True),
    A("chomoran", "chomoran", "漫畫四格", 441,
      "黑白漫畫＋頁碼＋對話框，鬼／和風題材。法典裡的常客。",
      ("page_number", "oni", "greyscale", "monochrome", "comic", "3girls", "vest", "speech_bubble"), codex=True),
    A("gaoo_(frpjx283)", "gaoo", "漫畫四格", 1258,
      "無臉男＋漫畫分鏡＋眼淚，NTR 敘事向的經典畫師。",
      ("faceless_male", "faceless", "disembodied_linked_eye", "tears", "comic", "wings", "hetero", "green_hair"), codex=True),
    A("muchi_maro", "muchi maro", "漫畫四格", 681,
      "黑眼圈、水手服、赤腳，漫畫分鏡多，帶點頹廢感。",
      ("bags_under_eyes", "sweatdrop", "barefoot", "small_breasts", "serafuku", "comic", "sweat", "pink_hair"), codex=True),
    A("asanagi", "朝凪", "成人向", 1628,
      "陷肉、虎牙、巨乳與貧乳兩極，線條粗，成人向的代表性畫師之一。",
      ("skindentation", "huge_breasts", "fangs", "covered_nipples", "fang", "white_thighhighs", "flat_chest", "armpits"), codex=True),
    A("satou_kuuki", "佐藤空気", "成人向", 1604,
      "墮落／黑化題材，緊身衣、高叉泳裝、紋身，magical girl 反轉。",
      ("corruption", "dark_persona", "pubic_tattoo", "shiny_clothes", "tachi-e", "skin_tight", "highleg_leotard", "magical_girl"), codex=True),
    A("bee_(deadflow)", "deadflow", "成人向", 1321,
      "寫實肉感＋強調血管，口交／插入的正面構圖。法典裡寫成 `deadflow`，真正的 tag 是 `bee (deadflow)`。",
      ("clothed_female_nude_male", "veiny_penis", "bar_censor", "large_penis", "veins", "fellatio", "oral", "erection"), codex=True),
    A("onono_imoko", "小野々芋子", "成人向", 681,
      "多人／輪姦題材，深膚色男性，透明背景立繪多。",
      ("gangbang", "rape", "group_sex", "dark-skinned_male", "bodysuit", "transparent_background", "tears", "vaginal"), codex=True),
    A("yd_(orange_maru)", "YD", "成人向", 1868,
      "高叉連身衣、女僕、兔女郎，長手套與高跟鞋，服裝設計感強。",
      ("highleg_leotard", "highleg", "bar_censor", "maid_headdress", "bodysuit", "leotard", "maid", "high_heels")),
    A("blushyspicy", "BlushySpicy", "成人向", 897,
      "高叉泳裝＋反光皮膚＋兔女郎，西式厚塗肉感。",
      ("highleg_leotard", "artist_name", "highleg", "shiny_skin", "playboy_bunny", "lips", "tattoo", "leotard")),
    A("shexyo", "shexyo", "成人向", 995,
      "巨臀與粗腿，身體冒煙、模糊背景，肉感非常誇張。",
      ("patreon_logo", "patreon_username", "thong_panties", "web_address", "thong", "steaming_body", "huge_ass", "blurry_background")),
    A("free_style_(yohan1754)", "free style", "成人向", 626,
      "比基尼＋散開長髮＋反光皮膚，側乳下乳的構圖很多。",
      ("hair_spread_out", "string_bikini", "underboob", "side-tie_bikini_bottom", "shiny_skin", "black_bikini", "sideboob", "stomach")),
    A("ebifurya", "えびふらい", "成人向", 6619,
      "掀衣、鼠蹊部、陷肉，一小時速繪出身，量大且穩定。",
      ("one-hour_drawing_challenge", "cropped_legs", "twitter_username", "lifting_own_clothes", "artist_name", "cropped_torso", "groin", "skindentation")),
    A("ningen_mame", "人間豆", "其他常用", 633,
      "賽馬娘題材大戶（馬耳馬尾、光環），水與藍天，柔和日常。法典常客。",
      ("pink_halo", "horse_tail", "horse_girl", "horse_ears", "halo", "water", "blue_sky", "blurry"), codex=True),
    A("modare", "modare", "其他常用", 1070,
      "光環＋白洋裝＋裸肩，室內外都有，清爽但帶點性感。法典常客。",
      ("halo", "black_skirt", "bare_shoulders", "white_dress", "outdoors", "indoors", "thighs", "sky"), codex=True),
    A("wanke", "wanke", "其他常用", 178,
      "鬼滅風格的隊服與日輪刀、蝴蝶，和風戰鬥題材。",
      ("demon_slayer_uniform", "playing_card", "card", "katana", "butterfly", "sheath", "bug", "holding_sword"), codex=True),
    A("na_tarapisu153", "na tarapisu153", "其他常用", 584,
      "能量翼、連帽外套、中性角色，暗色調帶發光。",
      ("energy_wings", "ambiguous_gender", "1other", "hood_up", "sound_effects", "hooded_jacket", "black_coat", "flying_sweatdrops"), codex=True),
    A("taromarun", "taromarun", "其他常用", 1217,
      "賽馬娘＋迷你帽＋蝴蝶結，原名 `misu kasumi` 已被 danbooru 併到這個 tag。",
      ("mini_top_hat", "mini_hat", "top_hat", "ear_bow", "horse_tail", "tracen_school_uniform", "horse_girl", "horse_ears"), codex=True),
    A("ke-ta", "ke-ta", "其他常用", 958,
      "燈籠褲、床上構圖，柔和的東方幻想（東方 Project 出身）。",
      ("white_bloomers", "bloomers", "disembodied_linked_eye", "bed_sheet", "pillow", "bed", "on_bed", "flat_chest")),
    A("kani_biimu", "かにビーム", "其他常用", 2442,
      "百合題材，校服＋雙馬尾，兩人互動構圖多。",
      ("st._michael's_school_uniform", "yuri", "two_side_up", "hair_ribbon", "2girls", "striped_clothes", "small_breasts", "panties")),
    A("saitou_naoki", "齋藤直葵", "其他常用", 603,
      "寶可夢卡牌插畫的官方畫師，透明背景＋卡片版面。",
      ("pokemon_card", "trading_card", "company_name", "card_(medium)", "copyright_notice", "poke_ball", "transparent_background", "pokemon_(creature)")),
    A("tianliang_duohe_fangdongye", "天涼多喝防凍液", "其他常用", 151,
      "腳部特寫、翻花繩、盆栽與中文字，構圖很有個人癖好。",
      ("cat's_cradle", "between_toes", "spread_toes", "flower_pot", "chinese_text", "potted_plant", "railing", "foot_focus")),
]

BY_TAG = {a.tag: a for a in ARTISTS}
GROUPS = list(dict.fromkeys(a.group for a in ARTISTS))

# What the codex (and a lot of forum copy-paste) writes, versus what danbooru
# actually has. The left-hand side names nobody at all - unlike the general-tag
# corrections in quicktags, where the paraphrase still lands somewhere useful,
# a misspelt artist is simply a different string with no artist behind it.
MISNAMED: dict[str, str] = {
    "hiten": "hiten_(hitenkei)",
    "deadflow": "bee_(deadflow)",
    "misu kasumi": "taromarun",
    "misu_kasumi": "taromarun",
    "krenz cushart": "krenz",
    "askzy": "ask_(askzy)",
    "cilo ranko": "ciloranko",
    "nin gen mame": "ningen_mame",
    "orange maru": "yd_(orange_maru)",
    "baalbuddy": "bb_(baalbuddy)",
    "judgemasterkou": "nameo_(judgemasterkou)",
    "frpjx283": "gaoo_(frpjx283)",
    "yohan1754": "free_style_(yohan1754)",
    "hitenkei": "hiten_(hitenkei)",
}


def misnamed(text: str) -> A | None:
    """The real artist for a name that names nobody, if there is one."""
    key = re.sub(r"[_\s]+", " ", (text or "").strip().lower())
    target = MISNAMED.get(key) or MISNAMED.get(key.replace(" ", "_"))
    return BY_TAG.get(target) if target else None


def search(query: str) -> list[A]:
    words = [w for w in re.split(r"\s+", (query or "").strip().lower()) if w]
    if not words:
        return list(ARTISTS)
    out = []
    for a in ARTISTS:
        hay = f"{a.tag} {a.zh} {a.group} {a.style} {' '.join(a.signals)}".lower()
        hay = hay.replace("_", " ")
        if all(w in hay for w in words):
            out.append(a)
    return out


def public() -> dict:
    return {
        "artists": [a.public() for a in ARTISTS],
        "groups": GROUPS,
        "count": len(ARTISTS),
        "misnamed": {k: BY_TAG[v].name for k, v in MISNAMED.items() if v in BY_TAG},
    }

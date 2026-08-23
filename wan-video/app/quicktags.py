"""A quick-pick list of the tags people reach for, with how well each is known.

Every tag here was checked against danbooru's own API and carries its real post
count. What that count means needs stating carefully, because the first version
of this file overclaimed and a user was right to push back on it.

**A post count is not a pass/fail.** These checkpoints are built on CLIP, which
is a language model: it understands English whether or not danbooru has a tag
for the phrase. Measured in CLIP ViT-L/14's own text space - SDXL's text encoder
1, run on CPU - the phrases that looked "dead" are nothing of the sort:

    ahegao face          vs ahegao      0.884   almost the same vector
    breasts out          vs exposed breasts 0.826
    double peace gesture vs double v    0.567
    soft lighting        vs dim lighting 0.715
    (unrelated control: 'double v' vs '1girl standing' = 0.342)

So `double peace gesture` really does produce a V sign, and `ahegao face` really
does produce ahegao. Anyone who has used them knows this, and any claim to the
contrary is simply wrong.

The reverse overclaim is worth guarding too, and a review caught it: these
numbers are a *lexical* diagnostic, not a prediction of what any U-Net does.
They come from CLIP-L's pooled vector, while SDXL's pooled embedding is taken
from OpenCLIP bigG - so this measurement is not even on the path the pooled
embedding actually travels. It is enough to disprove "zero posts means zero
effect". It is not enough to claim two spellings are interchangeable in
generation; only a fixed-seed A/B could say that, and none has been run.

**What the count does measure** is how hard the anime finetune sharpened that
exact string. NoobAI, Illustrious and Pony were trained on danbooru tag strings,
so the exact tag is a narrow, reliable lever: it lands harder, at lower weight,
with less drift into neighbouring concepts. A paraphrase lands in roughly the
right region and usually needs more weight to be as decisive. Both work; one is
sharper.

Two places where the count still says something close to pass/fail:

  * A phrase can be a *danbooru alias*, in which case the canonical form is
    strictly better - `peace_sign` is an active alias of `v`, `double_peace` of
    `double_v`, `naked` of `nude`. The alias is resolved away when the training
    captions are exported, so only the canonical string was ever trained on.
  * A tag under a few thousand posts is genuinely thin, and the finetune may
    barely distinguish it. `disgust` (4,078) is the weakest thing in this list
    and is flagged as such.

The counts are shown in the UI as **danbooru prevalence**, which is what they
actually are. A tag carried by 300,000 posts is far more likely to be a sharp
lever than one carried by 900, and seeing which is which beats guessing between
two spellings. It is still a prior, not a measurement of the checkpoint: only a
fixed-seed A/B on real generations could tell you how a given model responds,
and this project has run none.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass(frozen=True)
class T:
    """One tag: what to type, what it means, and how well the model knows it."""

    tag: str
    zh: str
    posts: int
    note: str = ""

    @property
    def prompt(self) -> str:
        """danbooru stores underscores; checkpoints want spaces, parens escaped."""
        return re.sub(r"([()])", r"\\\1", self.tag.replace("_", " "))

    @property
    def strength(self) -> str:
        """danbooru prevalence band - NOT a measure of this checkpoint's training.

        Named carefully because the loose version does not hold up: a post count
        is how common the tag is in the database today, and between that and how
        strongly a given checkpoint responds to the token sit dataset snapshot,
        dedup, caption normalisation, alias resolution, tag dropout, sampling
        weights, training steps, and whatever LoRA is stacked on top. Prevalence
        is a useful prior for picking between two spellings. It is not a
        measurement of model behaviour, and the weight advice that hangs off it
        is a heuristic, not a result.
        """
        if self.posts >= 100000:
            return "strong"
        if self.posts >= 10000:
            return "ok"
        return "weak"

    def public(self) -> dict:
        return {"tag": self.prompt, "raw": self.tag, "zh": self.zh,
                "posts": self.posts, "note": self.note, "strength": self.strength}


@dataclass(frozen=True)
class Group:
    key: str
    title: str
    tags: list[T] = field(default_factory=list)

    def public(self) -> dict:
        return {"key": self.key, "title": self.title,
                "tags": [t.public() for t in self.tags]}


GROUPS: list[Group] = [
    Group("expression", "表情 / 情緒", [
        T("ahegao", "阿嘿顏", 28089),
        T("fucked_silly", "腦袋壞掉", 10480),
        T("torogao", "陶醉臉", 12318),
        T("orgasm", "高潮", 25229),
        T("rolling_eyes", "翻白眼", 22637),
        T("upturned_eyes", "上吊眼", 6556),
        T("heavy_breathing", "喘氣", 51038),
        T("moaning", "呻吟", 17927),
        T("aroused", "興奮", 7407),
        T("naughty_face", "淫笑", 35662),
        T("seductive_smile", "誘惑笑", 15377),
        T("evil_smile", "壞笑", 22502),
        T("smirk", "得意笑", 36282),
        T("grin", "露齒笑", 351990),
        T("pout", "嘟嘴", 37548),
        T("tongue_out", "吐舌", 414080),
        T("long_tongue", "長舌", 9512),
        T("saliva", "口水", 150508),
        T("saliva_trail", "口水絲", 27837),
        T("drooling", "流口水", 79358),
        T("mouth_hold", "咬著東西", 100549),
        T("biting_own_lip", "咬唇", 7221, "alias of lip_biting"),
        T("clenched_teeth", "咬牙", 104501),
        T("blush", "臉紅", 4045195),
        T("nose_blush", "鼻樑紅", 147138),
        T("full-face_blush", "滿臉紅", 30452),
        T("embarrassed", "羞恥", 140056),
        T("crying", "哭", 113111),
        T("tears", "眼淚", 293004),
        T("crying_with_eyes_open", "睜眼流淚", 54500),
        T("trembling", "顫抖", 107175),
        T("half-closed_eyes", "半閉眼", 142124),
        T("closed_eyes", "閉眼", 1043384),
        T("empty_eyes", "空洞眼", 49598),
        T("glowing_eyes", "發光眼", 61785),
        T("constricted_pupils", "縮瞳", 20043),
        T("heart-shaped_pupils", "愛心瞳", 118968),
        T("symbol-shaped_pupils", "符號瞳", 247464),
        T("cross-eyed", "脫窗", 1556),
        T("surprised", "驚訝", 73291),
        T("scared", "害怕", 21481),
        T("angry", "生氣", 61237),
        T("screaming", "尖叫", 5603),
        T("open_mouth", "張嘴", 3459322),
        T("sweat", "流汗", 759207),
        T("sweatdrop", "汗滴", 323707),
        T("steaming_body", "身體冒煙", 41912),
        T("sleepy", "睏", 13164),
        T("exhausted", "力竭", 3666),
        T("mind_control", "精神控制", 14537),
        T("hypnosis", "催眠", 9900),
    ]),
    Group("gesture", "手勢 / 手部動作", [
        T("double_v", "雙手 V（雙剪刀手）", 42459),
        T("v", "V 手勢", 233634),
        T("peace_symbol", "和平手勢", 1636),
        T("heart_hands", "手比愛心", 40240),
        T("finger_heart", "手指愛心", 3859),
        T("thumbs_up", "讚", 19924),
        T("middle_finger", "中指", 8244),
        T("ok_sign", "OK 手勢", 5987),
        T("finger_gun", "手槍手勢", 7747),
        T("index_finger_raised", "舉一根手指", 74052),
        T("finger_to_mouth", "手指抵唇", 51806),
        T("shushing", "噓", 11759),
        T("pointing_at_viewer", "指向鏡頭", 17479),
        T("reaching_towards_viewer", "伸手向鏡頭", 36886),
        T("beckoning", "招手過來", 3542),
        T("waving", "揮手", 39998),
        T("salute", "敬禮", 20625),
        T("claw_pose", "爪子手", 28016),
        T("paw_pose", "貓爪手", 35976, "alias of cat_pose"),
        T("hands_up", "雙手舉起", 274198),
        T("arms_up", "雙臂上舉", 260265),
        T("arm_behind_head", "手放腦後", 51126),
        T("hands_on_own_hips", "手插腰", 43978, "alias of hands_on_hips"),
        T("hand_on_own_chest", "手放胸口", 88553),
        T("own_hands_together", "雙手合握", 114941),
        T("spread_arms", "張開雙臂", 28192),
        T("covering_breasts", "遮胸", 28088),
        T("covering_crotch", "遮下身", 15883),
        T("grabbing_another's_hair", "抓頭髮", 12196),
        T("grabbing_another's_breast", "抓胸", 94029),
        T("grabbing_own_breast", "自己抓胸", 24858),
        T("grabbing_another's_ass", "抓臀", 30384),
        T("grabbing_from_behind", "從背後抓住", 31776),
        T("grabbing_another's_arm", "抓手臂", 22052),
        T("grabbing_another's_chin", "抓下巴", 3006, "alias of chin_grab"),
    ]),
    Group("undress", "服裝狀態 / 脫衣", [
        T("topless_female", "上身全裸", 88094),
        T("bottomless", "下身全裸", 121620),
        T("completely_nude", "全裸", 287284),
        T("nude", "裸體", 683821, "alias of naked"),
        T("partially_undressed", "半脫", 9501),
        T("breasts_out", "露胸", 87377),
        T("one_breast_out", "露一邊", 18914),
        T("nipple_slip", "乳頭外露", 22090),
        T("areola_slip", "乳暈外露", 74819),
        T("cleavage", "胸溝", 1397767),
        T("underboob", "下乳", 126907),
        T("sideboob", "側乳", 156076),
        T("downblouse", "領口偷看", 9975),
        T("open_shirt", "襯衫敞開", 149403),
        T("open_clothes", "衣服敞開", 743668),
        T("open_kimono", "和服敞開", 19714),
        T("unbuttoned", "解開鈕扣", 21201),
        T("unzipped", "拉鍊拉開", 19126),
        T("clothes_lift", "掀衣", 284230),
        T("shirt_lift", "掀上衣", 108274),
        T("skirt_lift", "掀裙", 93966),
        T("dress_lift", "掀洋裝", 42714),
        T("bikini_top_lift", "掀比基尼上", 7294, "alias of bikini_lift"),
        T("clothes_pull", "拉開衣服", 107502),
        T("panty_pull", "拉開內褲", 58844),
        T("pantyhose_pull", "拉開褲襪", 14237),
        T("shirt_tug", "拉扯上衣", 4881),
        T("clothing_aside", "衣物撥到旁邊", 64994),
        T("panties_aside", "內褲撥到旁邊", 32968),
        T("bikini_bottom_aside", "比基尼下撥開", 9736, "alias of bikini_aside"),
        T("swimsuit_aside", "泳衣撥開", 7054),
        T("untied_bikini_top", "比基尼上鬆開", 8826),
        T("untied_panties", "內褲鬆開", 3420),
        T("no_bra", "沒穿內衣", 123320),
        T("no_panties", "沒穿內褲", 115230),
        T("see-through_clothes", "透視衣", 216382, "alias of see-through"),
        T("wet_clothes", "濕衣", 61220),
        T("wet_shirt", "濕上衣", 21183),
        T("torn_clothes", "破衣", 209377),
        T("wardrobe_malfunction", "衣服走光", 11382),
        T("undressing", "正在脫", 68297),
        T("strap_slip", "肩帶滑落", 51780),
        T("off_shoulder", "露肩", 341552),
        T("bare_shoulders", "裸肩", 1376657),
        T("bare_legs", "裸腿", 177769),
        T("clothed_female_nude_male", "女穿男裸", 59032),
        T("naked_apron", "裸體圍裙", 13154),
        T("naked_shirt", "裸體襯衫", 20312),
        T("naked_sweater", "裸體毛衣", 4090),
        T("thighhighs", "過膝襪", 1516665),
        T("garter_straps", "吊襪帶", 112839),
        T("fishnets", "網襪", 91755),
        T("thigh_strap", "腿環", 245992),
        T("gym_uniform", "體育服", 41881),
    ]),
    Group("pose", "姿勢 / 體位", [
        T("all_fours", "四肢撐地", 79804),
        T("top-down_bottom-up", "趴伏翹臀", 28344),
        T("presenting_own_body", "展示身體", 21192, "alias of presenting"),
        T("spread_legs", "張開雙腿", 346953),
        T("m_legs", "M 字腿", 17389),
        T("legs_apart", "雙腿分開", 46437),
        T("legs_up", "雙腿抬起", 46940),
        T("leg_lift", "抬一條腿", 21305, "alias of raised_leg"),
        T("knees_together_feet_apart", "內八腿", 41527),
        T("split", "劈腿", 16122),
        T("crossed_legs", "翹腳", 105380),
        T("on_back", "仰躺", 353475),
        T("on_stomach", "俯臥", 90962),
        T("on_side", "側躺", 122669),
        T("lying", "躺", 615495),
        T("fetal_position", "胎兒姿", 4811),
        T("sitting", "坐", 1295975),
        T("standing", "站", 1313971),
        T("kneeling", "跪", 155368),
        T("squatting", "蹲", 135501),
        T("bent_over", "彎腰", 83625),
        T("leaning_forward", "前傾", 160798),
        T("arched_back", "反弓背", 24601),
        T("arm_support", "手撐", 118039),
        T("straddling", "跨坐", 95935),
        T("girl_on_top", "女上", 90911),
        T("sitting_on_person", "坐在人身上", 33813),
        T("full_nelson", "全納爾遜", 4860),
        T("looking_back", "回頭看", 361250),
        T("turning_head", "轉頭", 18508),
        T("selfie", "自拍", 31474),
        T("w_arms", "W 手臂", 7499),
        T("spread_pussy", "自己撥開", 40730),
        T("breast_press", "胸部擠壓", 67734),
        T("imminent_penetration", "即將插入", 21376),
        T("restrained", "被固定", 69380),
        T("bound_arms", "手臂被綁", 22365),
        T("bound_wrists", "手腕被綁", 29453),
    ]),
    Group("view", "視角 / 構圖", [
        T("pov", "第一人稱", 196892),
        T("looking_at_viewer", "看鏡頭", 4837562),
        T("looking_away", "看別處", 34942),
        T("looking_at_another", "看對方", 428448),
        T("eye_contact", "對視", 68128),
        T("looking_down", "往下看", 137468),
        T("looking_up", "往上看", 99309),
        T("from_above", "俯視", 143979),
        T("from_below", "仰視", 117986),
        T("from_side", "側面", 331516),
        T("from_behind", "背後", 325463),
        T("straight-on", "正面平視", 59433),
        T("profile", "側臉", 179742),
        T("dutch_angle", "斜角", 161508),
        T("foreshortening", "透視壓縮", 68790),
        T("close-up", "特寫", 62981),
        T("portrait", "頭肩", 140232),
        T("upper_body", "上半身", 1175923),
        T("lower_body", "下半身", 8036),
        T("cowboy_shot", "七分身", 839535),
        T("full_body", "全身", 1261280),
        T("wide_shot", "遠景", 23479),
        T("solo_focus", "只聚焦一人", 496861),
        T("feet_out_of_frame", "腳出框", 235388),
        T("head_out_of_frame", "頭出框", 28876),
        T("out_of_frame", "出框", 43378),
        T("depth_of_field", "景深", 124681),
        T("blurry_foreground", "前景模糊", 41490),
    ]),
    Group("fluid", "體液 / 事後", [
        T("cum", "精液", 339160),
        T("cum_on_body", "身上", 126938),
        T("cum_on_breasts", "胸上", 53803),
        T("facial", "顏射", 60863),
        T("cum_in_mouth", "口內", 40402),
        T("cum_on_hair", "頭髮上", 29477),
        T("cum_on_clothes", "衣服上", 16565),
        T("cum_string", "精液絲", 12202),
        T("cumdrip", "滴落", 43126),
        T("cum_overflow", "溢出", 40212),
        T("cum_pool", "積成一灘", 6828),
        T("excessive_cum", "量過多", 3828),
        T("pussy_juice", "愛液", 151922),
        T("female_ejaculation", "女性潮吹", 15792),
        T("suggestive_fluid", "暗示性液體", 9089),
        T("lactation", "泌乳", 27642),
        T("after_sex", "事後", 51139),
        T("mutual_masturbation", "互相", 1136),
        T("wet", "濕", 192976),
        T("steam", "蒸氣", 74620),
        T("wet_hair", "濕髮", 20207),
        T("messy_hair", "亂髮", 90782),
    ]),
    Group("body", "身體特徵", [
        T("huge_breasts", "巨乳", 322120),
        T("large_breasts", "大胸", 2225385),
        T("medium_breasts", "中等", 1200506),
        T("small_breasts", "小胸", 706745),
        T("flat_chest", "平胸", 234638),
        T("nipples", "乳頭", 1126004),
        T("puffy_nipples", "腫脹乳頭", 47613),
        T("dark_nipples", "深色乳頭", 9738),
        T("covered_nipples", "衣下凸點", 201767, "alias of erect_nipples"),
        T("nipple_piercing", "乳環", 23534),
        T("navel", "肚臍", 1584315),
        T("navel_piercing", "臍環", 19042),
        T("stomach", "腹部", 412463),
        T("abs", "腹肌", 133435),
        T("collarbone", "鎖骨", 1094728),
        T("armpits", "腋下", 328205),
        T("thighs", "大腿", 822169),
        T("thick_thighs", "粗大腿", 158005),
        T("thigh_gap", "腿縫", 96707),
        T("wide_hips", "寬臀", 57323),
        T("narrow_waist", "細腰", 15948),
        T("curvy", "豐滿", 75181),
        T("toned", "結實", 59770),
        T("skindentation", "陷肉", 160511),
        T("pale_skin", "白皮膚", 72708),
        T("dark_skin", "深膚色", 402115),
        T("tan", "曬黑", 78138),
        T("tanlines", "曬痕", 41055),
        T("shiny_skin", "反光皮膚", 156084, "alias of glistening_skin"),
        T("body_blush", "身體泛紅", 8031),
        T("tattoo", "紋身", 207364),
        T("choker", "頸圈", 610964),
        T("collar", "項圈", 274683),
        T("leash", "牽繩", 37992),
        T("blindfold", "眼罩", 29853),
        T("gag", "口枷", 31106),
        T("handcuffs", "手銬", 17428),
        T("rope", "繩", 69454),
        T("hickey", "吻痕", 6100),
        T("bite_mark", "咬痕", 9788),
        T("biting", "咬", 17573),
        T("scratches", "抓痕", 5603),
        T("bruise", "瘀青", 13133),
    ]),
    Group("place", "場景 / 地點", [
        T("on_bed", "在床上", 170885),
        T("bed", "床", 136084),
        T("bedroom", "臥室", 20467),
        T("bathroom", "浴室", 16019),
        T("bathtub", "浴缸", 12913),
        T("showering", "淋浴中", 6536),
        T("shower_(place)", "淋浴間", 4118),
        T("onsen", "溫泉", 24620),
        T("pool", "泳池", 26029),
        T("beach", "海灘", 130139),
        T("classroom", "教室", 25881),
        T("school", "學校", 8784),
        T("locker_room", "更衣室", 5255),
        T("changing_room", "試衣間", 983),
        T("toilet", "廁所", 7954),
        T("kitchen", "廚房", 9646),
        T("office", "辦公室", 4201),
        T("library", "圖書館", 7055),
        T("rooftop", "屋頂", 6287),
        T("alley", "小巷", 4398),
        T("car_interior", "車內", 6039),
        T("hotel_room", "飯店房", 805),
        T("love_hotel", "賓館", 774),
        T("forest", "森林", 48634),
        T("public_indecency", "公開場合", 19550),
        T("indoors", "室內", 543684),
        T("outdoors", "室外", 798448),
        T("night", "夜晚", 168526),
    ]),
    Group("light", "光影 / 質感", [
        T("sunlight", "陽光", 101605),
        T("dappled_sunlight", "樹影斑點", 14974),
        T("sunbeam", "光束", 13238, "alias of god_rays"),
        T("backlighting", "逆光", 45176),
        T("sidelighting", "側光", 12879),
        T("underlighting", "底光", 1264),
        T("dim_lighting", "昏暗", 1288),
        T("moonlight", "月光", 4759),
        T("candlelight", "燭光", 1324),
        T("neon_lights", "霓虹", 3539),
        T("lens_flare", "鏡頭光斑", 50107),
        T("bokeh", "散景", 10659),
        T("film_grain", "顆粒", 26371),
        T("chromatic_aberration", "色散", 38221),
        T("motion_lines", "動態線", 120603),
        T("speed_lines", "速度線", 14193),
        T("emphasis_lines", "集中線", 46885),
    ]),

]

BY_TAG = {t.tag: t for g in GROUPS for t in g.tags}

# Sharper spellings. These are not "the broken name -> the working name": the
# left-hand side generally works too (see the docstring). The right-hand side is
# the string the anime finetunes were actually trained on, so it lands harder at
# lower weight - and where the left side is a danbooru alias, it is the only one
# that ever appeared in a training caption.
CORRECTIONS: dict[str, str] = {
    "double peace gesture": "double_v",
    "double peace": "double_v",
    "peace sign": "v",
    "double peace sign": "double_v",
    "ahegao face": "ahegao",
    "half naked": "topless_female",
    "half nude": "topless_female",
    "topless": "topless_female",
    "naked": "nude",
    "see-through": "see-through_clothes",
    "see through": "see-through_clothes",
    "cat pose": "paw_pose",
    "presenting": "presenting_own_body",
    "erect nipples": "covered_nipples",
    "glistening skin": "shiny_skin",
    "biting lip": "biting_own_lip",
    "lip biting": "biting_own_lip",
    "hands on hips": "hands_on_own_hips",
    "bikini aside": "bikini_bottom_aside",
    "bikini lift": "bikini_top_lift",
    "raised leg": "leg_lift",
    "god rays": "sunbeam",
    "chin grab": "grabbing_another's_chin",
    "hair grab": "grabbing_another's_hair",
    "hair pull": "grabbing_another's_hair",
    "shower": "showering",
    "teary-eyed": "tears",
    "teary eyed": "tears",
    "ass up": "top-down_bottom-up",
    "exposed breasts": "breasts_out",
    "untied bikini": "untied_bikini_top",
    "bending forward": "leaning_forward",
    # Prompt-guide vocabulary with no danbooru posts. These still do something
    # via CLIP (`soft lighting` sits at 0.715 to `dim lighting`), but the anime
    # finetunes never sharpened them, so the danbooru word is the stronger lever.
    "soft lighting": "dim_lighting",
    "cinematic lighting": "backlighting",
    "dramatic lighting": "backlighting",
    "rim lighting": "backlighting",
    "volumetric lighting": "sunbeam",
    "god ray": "sunbeam",
    "eyes rolled back": "rolling_eyes",
    "bedroom eyes": "half-closed_eyes",
    "seductive gaze": "seductive_smile",
    "sultry": "seductive_smile",
    "hand heart": "heart_hands",
}


def correction(text: str) -> T | None:
    """The sharper danbooru spelling for a phrase, if there is one."""
    key = re.sub(r"[_\s]+", " ", (text or "").strip().lower())
    target = CORRECTIONS.get(key)
    return BY_TAG.get(target) if target else None


def search(query: str, limit: int = 60) -> list[T]:
    """Tags matching every word of `query`, best-known first."""
    words = [w for w in re.split(r"\s+", (query or "").strip().lower()) if w]
    if not words:
        return []
    out = []
    for group in GROUPS:
        for t in group.tags:
            hay = f"{t.tag} {t.zh} {group.title}".lower().replace("_", " ")
            if all(w in hay for w in words):
                out.append(t)
    return sorted(out, key=lambda t: -t.posts)[:limit]


def public() -> dict:
    return {
        "favorites": [f.public() for f in FAVORITES],
        "groups": [g.public() for g in GROUPS],
        "count": sum(len(g.tags) for g in GROUPS),
        "corrections": {k: BY_TAG[v].prompt for k, v in CORRECTIONS.items()
                        if v in BY_TAG},
    }


# -- favourites ---------------------------------------------------------------
#
# The handful of tags one person reaches for every session, pinned next to the
# character picker so getting from "which Hololive member" to "doing what" is
# two clicks rather than a search.
#
# Each one carries two spellings, because the checkpoints in this app were not
# all trained on the same vocabulary:
#
#   danbooru   what NoobAI / Illustrious / Pony were conditioned on. The exact
#              tag string, which is the sharpest lever those models have.
#   natural    a plain description of the same thing, for Juggernaut and stock
#              SDXL, which never saw a danbooru tag in training.
#
# Both are real. Measured in CLIP ViT-L/14's own text space (SDXL's text encoder
# 1), `double peace gesture` sits at 0.567 cosine to `double v` against a 0.28
# baseline for unrelated text - so the natural phrase genuinely carries the
# meaning. The danbooru tag is not "the only thing that works"; it is the
# spelling the finetune sharpened, which is why it needs less weight to land.


@dataclass(frozen=True)
class Fav:
    key: str
    zh: str
    danbooru: str
    natural: str
    posts: int = 0
    note: str = ""

    def emit(self, tag_style: str = "danbooru") -> str:
        raw = self.natural if tag_style == "natural" else self.danbooru
        return re.sub(r"([()])", r"\\\1", raw.replace("_", " "))

    def public(self) -> dict:
        return {
            "key": self.key, "zh": self.zh, "posts": self.posts, "note": self.note,
            "danbooru": self.emit("danbooru"), "natural": self.emit("natural"),
        }


FAVORITES: list[Fav] = [
    Fav("v", "單手比 V", "v", "making a peace sign with one hand", 234750),
    Fav("double_v", "雙手比 V", "double_v",
        "making a peace sign with both hands", 42651,
        "你打的 `double peace gesture` 在 danbooru 上不是 tag，但它在 CLIP 裡離 double v 很近，所以有效果——只是比較鬆。"),
    Fav("breasts_out", "露胸", "breasts_out", "bare breasts, breasts exposed", 87622),
    Fav("ahegao", "阿嘿顏", "ahegao",
        "ahegao, eyes rolled back, tongue out, blissful expression", 28181,
        "`ahegao face` 跟 `ahegao` 在 CLIP 裡的相似度 0.884，幾乎是同一個向量，所以你原本那樣打也會出——這裡用 danbooru 那個更準的。"),
    Fav("ahegao_double_peace", "阿嘿顏＋雙手 V", "ahegao, double_v",
        "ahegao, tongue out, making a peace sign with both hands", 0,
        "經典組合（アヘ顔ダブルピース）。"),
    Fav("topless", "上身全裸", "topless_female", "topless, bare chest", 88273),
    Fav("bottomless", "下身全裸", "bottomless", "bottomless, nothing below the waist",
        121953, "`bottomless female` 在 danbooru 是 0 張，正式的 tag 就是 `bottomless`。"),
    Fav("horse_stance", "蹲馬步（蹲姿張腿）", "squatting, spread_legs",
        "squatting low with legs wide apart, horse stance", 136036,
        "danbooru 沒有單一的「馬步」tag（`horse stance` 只有 30 張），實務上是 squatting + spread legs。"),
    Fav("m_legs", "M 字腿", "m_legs", "lying with knees up and legs spread", 17456),
    Fav("expressionless", "無表情", "expressionless", "expressionless, blank face", 179053),
    Fav("disgust", "厭惡表情", "disgust", "disgusted expression, grimacing", 4078,
        "只有 4,078 張，是這幾個裡最弱的一個，可能要加權到 1.2 才明顯。"),
    Fav("serious", "認真表情", "serious", "serious expression", 39472),
    Fav("happy", "高興表情", "happy, smile", "happy, smiling", 137696),
]

FAV_BY_KEY = {f.key: f for f in FAVORITES}


def favorites(tag_style: str = "danbooru") -> list[dict]:
    return [{**f.public(), "tag": f.emit(tag_style)} for f in FAVORITES]

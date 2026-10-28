"""[Tags] in text to speak: emotions, ways of speaking, speech habits, roles, non-verbal sounds and pauses.

Every tag has one canonical English name (ElevenLabs-style, so the novel-lab sheets work as written), a Chinese
name for the interface, and the other names people write it with in English, Japanese and Chinese. What a tag does:
- style: an English description handed to instruction-following engines ("(nervous, tense)…" for VoxCPM2);
- emotion: the label whose reference clip (and catchphrase / sound recording) is picked for that text;
- pause: real silence of that many seconds ([pause], [停頓 1.5秒], [間]);
- a sound ([sighs], [喘氣], [笑聲] …) registered on the voice page with the person's own recordings is played from
  them (phrases.is_sound); without recordings it only colours the text after it.
Tags apply to the text after them, up to the next tag. Ways of speaking carry on to the following text of the line;
things that happen once (sounds, pauses) do not. Unknown tags are used as written, as a style description.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

GROUPS = {  # id → name in the interface, in display order
    "pos": "開心・正面", "anger": "生氣・不滿", "sad": "難過・哭腔", "fear": "害怕・緊張・驚訝",
    "shy": "害羞・撒嬌・調情", "cool": "冷淡・認真・自信", "tired": "疲倦・想睡・身體狀況",
    "volume": "音量・距離", "pace": "速度・節奏・音調", "habit": "說話習慣", "role": "角色・用途",
    "laugh": "笑聲", "cry": "哭聲", "breath": "呼吸", "sound": "其他聲音", "pause": "停頓",
}
EVENT_GROUPS = {"laugh", "cry", "breath", "sound", "pause"}  # things that happen once


@dataclass(frozen=True)
class Tag:
    key: str
    zh: str
    group: str
    style: str
    emotion: str | None
    names: tuple[str, ...]
    pause: float | None = None

    @property
    def event(self) -> bool:
        return self.group in EVENT_GROUPS


def _t(group, key, zh, style, emotion, names, pause=None) -> Tag:
    return Tag(key, zh, group, style, emotion, tuple(n.strip() for n in names.split("|") if n.strip()), pause)


CATALOGUE: list[Tag] = [
    # --- 開心・正面 ---
    _t("pos", "happy", "開心", "happy, cheerful", "happy",
       "cheerful|glad|joyful|高興|快樂|愉快|嬉しい|うれしい|嬉しそうに|楽しい|楽しそうに"),
    _t("pos", "excited", "興奮", "excited, energetic", "excited",
       "energetic|hyped|pumped|enthusiastic|high energy|激動|亢奮|嗨|興奮して|ワクワク|わくわく|ハイテンション|テンション高め"),
    _t("pos", "delighted", "驚喜", "delighted, overjoyed", "happy", "overjoyed|thrilled|欣喜|大喜び|歓喜"),
    _t("pos", "laughing", "笑著說", "laughing while speaking", "laughing",
       "laughing while talking|邊笑邊說|帶笑|笑いながら|笑って"),
    _t("pos", "smiling", "微笑著說", "smiling, warm", "happy",
       "with a smile|微笑|笑咪咪|ニコニコ|にこにこ|微笑みながら|笑顔で"),
    _t("pos", "playful", "調皮", "playful, mischievous", "teasing",
       "mischievous|impish|cheeky|頑皮|淘氣|いたずらっぽく|おちゃめ|茶目っ気たっぷりに"),
    _t("pos", "warm", "親切", "warm, friendly", "happy", "friendly|kind|溫暖|友善|和善|親しげに|フレンドリー"),
    _t("pos", "gentle", "溫柔", "gentle, tender", "soft", "tender|柔和|輕柔|優しく|やさしく|優しい声で"),
    _t("pos", "loving", "深情", "loving, affectionate", "soft",
       "affectionate|fond|寵溺|疼愛|愛おしそうに|愛情を込めて"),
    _t("pos", "grateful", "感謝", "grateful, heartfelt", "soft",
       "thankful|heartfelt|感激|感動|感謝を込めて|心を込めて"),
    _t("pos", "proud", "驕傲", "proud", "smug", "自豪|誇らしげに|誇らしく"),
    _t("pos", "relieved", "放心", "relieved, tension leaving", "neutral", "安心|安心して|ほっとして"),
    _t("pos", "hopeful", "期待", "hopeful, eager", "happy", "eager|expectant|盼望|期待して|楽しみそうに"),
    _t("pos", "amazed", "讚嘆", "amazed, in awe", "surprised",
       "impressed|in awe|awestruck|佩服|驚嘆|感心して|感嘆して"),
    _t("pos", "nostalgic", "懷念", "nostalgic, wistful", "soft", "wistful|懷舊|懐かしそうに|しみじみ"),
    _t("pos", "calm", "平靜", "calm, steady", "neutral",
       "neutral|steady|relaxed|composed|冷靜|平常|放鬆|淡定|落ち着いて|穏やか|穏やかに|普通に|リラックス"),
    # --- 生氣・不滿 ---
    _t("anger", "angry", "生氣", "angry, sharp", "angry", "mad|憤怒|怒|怒って|怒り|怒った|ムカついて"),
    _t("anger", "furious", "暴怒", "furious, seething", "angry",
       "enraged|livid|raging|大怒|抓狂|激怒|ブチギレ|キレて"),
    _t("anger", "annoyed", "不耐煩", "annoyed, irritated", "annoyed",
       "irritated|impatient|煩躁|惱火|イライラ|いらいら|イラついて"),
    _t("anger", "frustrated", "懊惱", "frustrated", "annoyed", "挫折|もどかしそうに"),
    _t("anger", "vexed", "不甘心", "vexed, bitterly frustrated", "annoyed", "不甘|悔しい|悔しそうに|くやしい"),
    _t("anger", "grumpy", "不爽", "grumpy, sullen", "annoyed", "sullen|cranky|臭臉|不機嫌|不機嫌そうに|ぶすっと"),
    _t("anger", "sulking", "賭氣", "sulking, pouting", "annoyed", "pouting|鬧彆扭|嘟嘴|拗ねて|すねて|ふくれっ面"),
    _t("anger", "complaining", "抱怨", "complaining, whiny", "annoyed",
       "whining|whiny|grumbling|發牢騷|愚痴っぽく|ぼやいて|文句を言って"),
    _t("anger", "disgusted", "嫌棄", "disgusted, repulsed", "disgusted",
       "grossed out|repulsed|噁心|厭惡|嫌悪|気持ち悪そうに|ドン引き|引いて"),
    _t("anger", "contemptuous", "鄙視", "contemptuous, looking down on them", "cold",
       "disdainful|scornful|輕蔑|不屑|見下して|軽蔑して"),
    _t("anger", "threatening", "威脅", "low, menacing, threatening", "angry",
       "menacing|兇狠|凶狠|脅すように|凄んで|ドスの効いた声で"),
    _t("anger", "jealous", "吃醋", "jealous, pouty", "annoyed", "envious|嫉妒|羨慕|ヤキモチ|嫉妬して|羨ましそうに"),
    _t("anger", "fed up", "無奈", "resigned, exasperated", "annoyed",
       "exasperated|resigned|受不了|沒轍|呆れて|あきれて|やれやれ|うんざり"),
    # --- 難過・哭腔 ---
    _t("sad", "sad", "難過", "sad, subdued", "sad", "unhappy|down|傷心|悲傷|悲しい|悲しそうに"),
    _t("sad", "melancholy", "憂鬱", "melancholy, gloomy", "sad", "gloomy|depressed|低落|沮喪|落ち込んで|しょんぼり|どんより"),
    _t("sad", "lonely", "寂寞", "lonely, forlorn", "sad", "forlorn|孤單|寂しそうに|さみしい|寂しい"),
    _t("sad", "disappointed", "失望", "disappointed, let down", "sad", "let down|失落|がっかり|残念そうに"),
    _t("sad", "regretful", "後悔", "regretful, remorseful", "sad", "remorseful|悔恨|後悔して"),
    _t("sad", "apologetic", "道歉", "apologetic, sorry", "soft", "sorry|抱歉|愧疚|申し訳なさそうに|謝りながら"),
    _t("sad", "pleading", "哀求", "pleading, begging", "sad", "begging|imploring|懇求|拜託|懇願して|すがるように"),
    _t("sad", "tearful", "哭腔", "tearful, close to tears", "crying",
       "teary|on the verge of tears|要哭了|淚眼汪汪|涙声|泣きそう|うるうる"),
    _t("sad", "crying", "哭著說", "crying while speaking", "crying", "weeping|邊哭邊說|泣きながら|泣いて"),
    _t("sad", "choked up", "哽咽", "choked up, voice breaking", "crying", "voice breaking|声を詰まらせて|涙をこらえて"),
    _t("sad", "heartbroken", "心碎", "heartbroken, devastated", "crying",
       "devastated|despairing|grief-stricken|心痛|崩潰|悲痛|絕望|絶望して|打ちひしがれて"),
    # --- 害怕・緊張・驚訝 ---
    _t("fear", "scared", "害怕", "scared, frightened", "scared", "afraid|frightened|fearful|恐懼|怖い|怖がって|怯えて|びくびく"),
    _t("fear", "terrified", "驚恐", "terrified, panicked", "scared",
       "panicked|panicking|horrified|嚇壞|恐慌|驚慌|パニック|慌てて|取り乱して"),
    _t("fear", "nervous", "緊張", "nervous, tense", "nervous", "tense|uneasy|jittery|忐忑|緊張して|ドキドキ|どきどき"),
    _t("fear", "anxious", "不安", "anxious, worried", "nervous", "worried|concerned|擔心|焦慮|心配そうに|不安そうに"),
    _t("fear", "trembling", "發抖", "shaky, trembling voice", "scared",
       "shaky|shaking|quivering|顫抖|聲音發抖|震え声|震えて|ぶるぶる"),
    _t("fear", "surprised", "驚訝", "surprised", "surprised", "意外|驚いて|びっくり|びっくりして|驚き"),
    _t("fear", "shocked", "震驚", "shocked, stunned", "surprised", "stunned|astonished|傻眼|嚇一跳|呆然|愕然|ショック|唖然"),
    _t("fear", "confused", "疑惑", "confused, puzzled", "confused",
       "puzzled|baffled|困惑|疑問|不解|一頭霧水|困惑して|戸惑って|きょとん"),
    _t("fear", "curious", "好奇", "curious, intrigued", None, "inquisitive|intrigued|感興趣|興味津々|興味深そうに"),
    _t("fear", "suspicious", "懷疑", "suspicious, doubtful", "confused",
       "doubtful|skeptical|sceptical|狐疑|半信半疑|疑って|怪しむように|ジト目"),
    # --- 害羞・撒嬌・調情 ---
    _t("shy", "embarrassed", "害羞", "embarrassed, bashful", "embarrassed",
       "bashful|shy|不好意思|難為情|臉紅|恥ずかしそうに|照れて|照れながら|恥ずかしい"),
    _t("shy", "flustered", "慌張", "flustered", "embarrassed", "手忙腳亂|慌亂|あたふた|あわあわ|動揺して"),
    _t("shy", "awkward", "尷尬", "awkward, uncomfortable", "embarrassed", "uncomfortable|気まずそうに|気まずい"),
    _t("shy", "tsundere", "傲嬌", "acting cold and annoyed while secretly pleased", "embarrassed", "ツンデレ|ツンツン"),
    _t("shy", "cute", "裝可愛", "cute, sweet and bright", "teasing",
       "adorable|可愛|賣萌|萌|かわいく|可愛く|ぶりっ子|きゃぴきゃぴ"),
    _t("shy", "coaxing", "撒嬌", "sweet, coaxing, clingy", "teasing",
       "clingy|sweet-talking|撒嬌地|甘えて|甘え声|あまえて"),
    _t("shy", "teasing", "調侃", "teasing, playful", "teasing", "ribbing|逗|捉弄|開玩笑|からかって|からかうように|いじって"),
    _t("shy", "flirty", "調情", "flirtatious, charming", "teasing", "flirtatious|coy|曖昧|撩|撩人|誘うように"),
    _t("shy", "sultry", "性感", "sultry, low and alluring", "teasing",
       "seductive|alluring|魅惑|嫵媚|色っぽく|艶っぽく|妖艶"),
    # --- 冷淡・認真・自信 ---
    _t("cool", "serious", "認真", "serious, earnest", "serious", "earnest|sincere|嚴肅|正經|真剣|真面目|まじめに|真剣に"),
    _t("cool", "stern", "嚴厲", "stern, strict", "serious", "strict|嚴格|厳しく|厳しい口調で"),
    _t("cool", "determined", "堅定", "determined, resolute", "serious",
       "resolute|decisive|firm|果斷|決心|決意を込めて|きっぱり|力強く"),
    _t("cool", "confident", "自信", "confident, self-assured", "serious",
       "assertive|self-assured|自信滿滿|篤定|自信満々|堂々と"),
    _t("cool", "smug", "得意", "smug, self-satisfied", "smug", "cocky|boastful|得意洋洋|臭屁|ドヤ|ドヤ顔|得意げ|自慢げ"),
    _t("cool", "sarcastic", "諷刺", "sarcastic, dry irony", "sarcastic",
       "ironic|snarky|酸|嘲諷|挖苦|陰陽怪氣|皮肉っぽく|嫌味っぽく"),
    _t("cool", "mocking", "嘲弄", "mocking, taunting", "sarcastic",
       "derisive|taunting|取笑|挑釁|あざ笑うように|煽るように|馬鹿にして"),
    _t("cool", "cold", "冷淡", "cold, distant", "cold", "cool|distant|aloof|icy|冷漠|高冷|冷たく|クール|そっけなく|素っ気なく"),
    _t("cool", "indifferent", "無所謂", "indifferent, uninterested", "cold",
       "uninterested|nonchalant|不在乎|隨便|無関心|どうでもよさそうに|興味なさそうに"),
    _t("cool", "deadpan", "面無表情", "deadpan, flat", "cold", "expressionless|無表情|真顔で"),
    _t("cool", "bored", "無聊", "bored, unenthusiastic", "tired", "unenthusiastic|沒勁|退屈そうに|つまらなそうに"),
    # --- 疲倦・想睡・身體狀況 ---
    _t("tired", "tired", "疲倦", "tired, low energy", "tired",
       "exhausted|weary|worn out|累|好累|疲憊|疲れて|疲れた|ぐったり|へとへと"),
    _t("tired", "sleepy", "想睡", "sleepy, drowsy", "tired", "drowsy|睏|睡意|眠そうに|眠い|うとうと|ねむい"),
    _t("tired", "groggy", "剛睡醒", "groggy, just woke up", "tired",
       "just woke up|half asleep|睡眼惺忪|迷迷糊糊|寝起き|寝ぼけて"),
    _t("tired", "lazy", "懶洋洋", "lazy, listless", "tired", "sluggish|listless|懶散|有氣無力|だるそうに|けだるく"),
    _t("tired", "drunk", "微醺", "tipsy, slightly slurred", None, "tipsy|喝醉|醉醺醺|酔っ払って|ほろ酔い"),
    _t("tired", "sick", "生病", "sick, weak and stuffy-nosed", "tired",
       "under the weather|stuffy nose|感冒|鼻音重|風邪声|鼻声|体調悪そうに"),
    _t("tired", "in pain", "痛苦", "in pain, strained", None, "hurt|pained|好痛|吃痛|痛そうに|苦しそうに"),
    # --- 音量・距離 ---
    _t("volume", "whispers", "悄悄話", "whispering", "whisper",
       "whisper|whispering|耳語|低語|說悄悄話|ささやき|ささやいて|囁いて|ひそひそ"),
    _t("volume", "breathy", "氣音", "breathy, airy voice", "whisper", "airy|吐息|吐息まじり|ウィスパーボイス"),
    _t("volume", "soft", "小聲", "soft, quiet", "soft", "quiet|quietly|softly|hushed|輕聲|輕輕地|小声|小声で|静かに"),
    _t("volume", "murmurs", "呢喃", "murmuring softly, half to themself", "soft",
       "murmur|murmuring|喃喃|喃喃自語|つぶやく|つぶやいて"),
    _t("volume", "loud", "大聲", "loud, projecting", None, "loudly|projecting|大聲說|大声で|声を張って"),
    _t("volume", "shouts", "大喊", "shouting", "shouting",
       "shout|shouting|yells|yelling|吼|喊|叫喊|叫んで|叫ぶ|怒鳴って"),
    _t("volume", "calling out", "呼喚遠處的人", "calling out to someone far away", "shouting",
       "calling|呼喚|喊人|呼びかけて|遠くに呼びかけて"),
    _t("volume", "asmr", "耳邊", "very close to the mic, intimate", "whisper",
       "close to the mic|close-mic|貼耳|耳元で|耳元|ASMR風に"),
    _t("volume", "far away", "遠處", "distant, as if from across the room", None, "distant voice|遠くから"),
    _t("volume", "muffled", "悶聲", "muffled", None, "捂著嘴|こもった声で"),
    # --- 速度・節奏・音調 ---
    _t("pace", "fast", "快速", "fast, quick pace", None, "quickly|rapidly|快|講很快|早口|早口で|速く"),
    _t("pace", "rushed", "急促", "rushed, hurried", "nervous", "hurried|hasty|in a hurry|急忙|趕時間|慌ただしく|急いで"),
    _t("pace", "slow", "慢慢說", "slow, unhurried", None, "slowly|unhurried|慢|慢慢地|ゆっくり|ゆっくりと"),
    _t("pace", "deliberate", "一字一句", "deliberate, word by word", "serious",
       "measured|word by word|enunciating|咬字清楚|一言一言|はっきりと|区切って"),
    _t("pace", "drawn out", "拖長音", "drawn-out vowels, drawling", None,
       "drawl|drawling|elongated|拖音|語尾を伸ばして|伸ばして|間延びして"),
    _t("pace", "sing-song", "唱歌似的", "sing-song, melodic", "happy", "singsong|lilting|melodic|歌うように|ルンルン"),
    _t("pace", "monotone", "平板", "monotone, flat", "cold", "平淡|沒起伏|棒読み|抑揚なく"),
    _t("pace", "emphatic", "強調", "emphatic, stressing the words", None, "emphasis|emphasizing|加重語氣|強調して|力を込めて"),
    _t("pace", "questioning", "疑問語氣", "questioning, rising intonation", "confused",
       "rising intonation|問句|尻上がりに|疑問形で"),
    _t("pace", "low voice", "低沉", "low, deep voice", None, "deep voice|low-pitched|低音|壓低聲音|低い声で|声を低くして"),
    _t("pace", "high voice", "高音", "high-pitched", None, "high-pitched|尖細|拔高|高い声で"),
    _t("pace", "falsetto", "假音", "falsetto", None, "假聲|裏声"),
    # --- 說話習慣 ---
    _t("habit", "stutters", "結巴", "stuttering, tripping over the first sounds", "nervous",
       "stuttering|stammers|stammering|口吃|結結巴巴|どもって|どもりながら|噛みながら"),
    _t("habit", "hesitant", "猶豫", "hesitant, unsure", "nervous",
       "hesitating|hesitates|unsure|吞吞吐吐|支支吾吾|欲言又止|ためらいがちに|言いよどんで|もじもじ"),
    _t("habit", "trails off", "越說越小聲", "trailing off at the end", "soft",
       "trailing off|fading out|聲音漸弱|語尾を濁して|尻すぼみ|消え入るように"),
    _t("habit", "mumbles", "含糊", "mumbling, unclear", "soft", "mumbling|mumble|嘟囔|口齒不清|もごもご|ぼそぼそ"),
    _t("habit", "mutters", "嘀咕", "muttering under the breath", "annoyed",
       "muttering|mutter|under the breath|碎碎念|小聲抱怨|ぶつぶつ|ボソッと|ぼそっと"),
    _t("habit", "thinking", "邊想邊說", "thinking aloud, pausing to think", None,
       "thinking aloud|pondering|思考|想一想|考えながら"),
    _t("habit", "to themself", "自言自語", "talking to themself", "soft",
       "to oneself|to herself|to himself|self-talk|aside|獨白|独り言|ひとりごと"),
    _t("habit", "rambling", "滔滔不絕", "rambling, talking nonstop", "excited",
       "rattling on|talking nonstop|嘮叨|碎嘴|まくし立てて|マシンガントーク"),
    _t("habit", "cut off", "話說一半", "cut off abruptly at the end", None, "interrupted|被打斷|途中で遮られて"),
    _t("habit", "casual", "隨性聊天", "casual, conversational", "neutral",
       "conversational|chatty|隨性|口語|聊天|輕鬆|雑談風に|砕けた感じで|タメ口"),
    _t("habit", "polite", "禮貌", "polite, formal", "neutral", "formal|courteous|禮貌地|客氣|正式|丁寧に|敬語で|かしこまって"),
    # --- 角色・用途 ---
    _t("role", "narration", "旁白", "narrating, clear storytelling voice", "narration",
       "narrator|narrating|念稿|ナレーション|ナレーター|語り"),
    _t("role", "storytelling", "說故事", "storytelling, engaging and expressive", "narration",
       "story time|telling a story|講故事|読み聞かせ|昔話風に"),
    _t("role", "reading aloud", "朗讀", "reading aloud, clear and even", "narration",
       "reading|recitation|唸稿|朗読|音読"),
    _t("role", "news", "新聞播報", "news anchor, crisp and neutral", "narration",
       "newscaster|news anchor|播報|主播|ニュース風に|アナウンサー風に|キャスター風に"),
    _t("role", "announcer", "廣播", "announcer, clear and projecting", "narration",
       "announcement|廣播|場內廣播|宣布|アナウンス|場内アナウンス"),
    _t("role", "commentator", "實況", "lively play-by-play commentary", "excited",
       "play-by-play|sportscaster|解說|実況|実況風に"),
    _t("role", "customer service", "客服", "polite customer-service tone", "neutral",
       "receptionist|店員|接待|接客|店員風に|営業スマイル"),
    _t("role", "teacher", "老師講解", "explaining patiently like a teacher", "narration",
       "lecturing|explaining|講課|解釋|先生っぽく|説明口調"),
    _t("role", "commercial", "廣告", "upbeat commercial voice", "excited", "advertisement|ad read|業配|CM風に|宣伝"),
    _t("role", "trailer", "預告片", "dramatic movie-trailer voice", "serious", "movie trailer|epic|史詩|予告編風に"),
    _t("role", "dramatic", "戲劇化", "dramatic, theatrical", "excited",
       "theatrical|over the top|誇張|浮誇|芝居がかって|大げさに|オーバーに"),
    _t("role", "villain", "反派", "villainous, sinister", "cold", "villainous|sinister|evil|邪惡|陰險|悪役風に|悪そうに"),
    _t("role", "heroic", "熱血", "heroic, rousing", "serious", "rousing|inspiring|英雄|激勵|鼓舞するように|ヒーロー風に"),
    _t("role", "childlike", "孩子氣", "childlike, innocent", "happy", "childish|innocent|童聲|天真|子供っぽく|あどけなく"),
    _t("role", "mature", "成熟", "mature, composed", "neutral", "grown-up|穩重|大人っぽく"),
    _t("role", "robotic", "機器人", "robotic, mechanical", "cold", "mechanical|robot|機械|ロボット風に|機械的に"),
    _t("role", "streamer greeting", "開場招呼", "bright, high-energy streamer greeting", "excited",
       "greeting|idol|開場|打招呼|偶像|配信開始|アイドル風に|挨拶"),
    # --- 笑聲 ---
    _t("laugh", "laughs", "笑聲", "with a laugh", "laughing", "laugh|laughter|笑|笑い|笑い声|哈哈|haha"),
    _t("laugh", "chuckles", "輕笑", "with a soft chuckle", "laughing", "chuckle|低笑|笑一下|くすっと|クスッ|ふふっ"),
    _t("laugh", "giggles", "咯咯笑", "giggling", "laughing", "giggle|giggling|嘻嘻|くすくす|クスクス|うふふ|えへへ"),
    _t("laugh", "snickers", "偷笑", "snickering", "teasing", "snicker|sniggers|竊笑|憋笑|ぷぷっ|にやにや|ニヤニヤ"),
    _t("laugh", "bursts out laughing", "噴笑", "bursting into laughter", "laughing",
       "bursts into laughter|cracks up|pfft|笑出來|笑場|噗哧|吹き出して|噴き出して|ぷっ"),
    _t("laugh", "laughs hard", "大笑", "laughing heartily", "laughing",
       "laughs heartily|laughing out loud|guffaws|belly laugh|哈哈大笑|爆笑|笑到不行|大爆笑"),
    _t("laugh", "wheezes", "笑到喘", "wheezing with laughter", "laughing",
       "wheezing laugh|笑到岔氣|笑到無法呼吸|引き笑い|笑いすぎて"),
    _t("laugh", "cackles", "狂笑", "cackling", "laughing", "cackle|evil laugh|maniacal laugh|怪笑|奸笑|高笑い|悪役笑い"),
    _t("laugh", "nervous laugh", "乾笑", "with a nervous laugh", "nervous",
       "laughs nervously|awkward laugh|尷尬地笑|愛想笑い|照れ笑い"),
    _t("laugh", "bitter laugh", "苦笑", "with a wry, bitter laugh", "sarcastic",
       "laughs bitterly|wry laugh|自嘲|苦笑い|自嘲気味に"),
    _t("laugh", "scoffs", "冷笑", "with a scoff", "cold", "scoff|sneers|嗤笑|哼笑|鼻で笑う|鼻笑い"),
    # --- 哭聲 ---
    _t("cry", "sobs", "抽泣", "sobbing", "crying", "sobbing|啜泣|嗚咽|しゃくり上げて|すすり泣き"),
    _t("cry", "cries", "哭聲", "crying", "crying", "cry|wails|大哭|嚎啕大哭|泣き声|号泣|うわーん"),
    _t("cry", "sniffles", "吸鼻子", "sniffling", "crying", "sniffle|sniffling|鼻をすする|ぐすっ|グスッ|ぐすん"),
    _t("cry", "whimpers", "嗚嗚", "whimpering", "crying", "whimper|whimpering|小聲哭|めそめそ"),
    # --- 呼吸 ---
    _t("breath", "sighs", "嘆氣", "with a sigh", None, "sigh|sighing|嘆息|唉聲嘆氣|ため息|ため息まじり"),
    _t("breath", "sigh of relief", "鬆一口氣", "with a sigh of relief", "neutral",
       "relieved sigh|鬆口氣|ほっと一息|安堵のため息"),
    _t("breath", "exhales", "吐氣", "with a slow exhale", None, "exhale|breathes out|呼氣|息を吐いて"),
    _t("breath", "inhales", "吸氣", "with a quick intake of breath", None,
       "inhale|breathes in|breath|吸一口氣|息を吸う|息を吸って"),
    _t("breath", "deep breath", "大口吸氣", "taking a deep breath first", None,
       "takes a deep breath|深呼吸|深吸一口氣|深呼吸して|大きく息を吸って"),
    _t("breath", "gasps", "倒抽一口氣", "with a gasp", "surprised", "gasp|sharp inhale|倒吸一口氣|抽氣|息をのむ|息を呑んで|はっと"),
    _t("breath", "panting", "喘氣", "breathless, panting", None,
       "pants|breathless|out of breath|heavy breathing|breathing heavily|huffing|喘|喘息|氣喘吁吁|上氣不接下氣|"
       "息切れ|息を切らして|はぁはぁ|ハァハァ|ぜえぜえ"),
    _t("breath", "soft panting", "嬌喘", "breathy, softly panting", "soft", "喘ぎ|甘い吐息"),
    _t("breath", "holds breath", "屏息", "holding the breath, then speaking tightly", "nervous",
       "holding breath|憋氣|息を止めて|息を殺して"),
    # --- 其他聲音 ---
    _t("sound", "coughs", "咳嗽", "with a cough", None, "cough|coughing|咳|咳咳|咳き込んで|ゴホッ|けほっ"),
    _t("sound", "clears throat", "清喉嚨", "clearing the throat first", None, "clear throat|ahem|清嗓子|咳払い|んんっ"),
    _t("sound", "sneezes", "打噴嚏", "with a sneeze", None, "sneeze|achoo|噴嚏|哈啾|くしゃみ|くしゅん|ハクション"),
    _t("sound", "sniffs", "嗅", "sniffing", None, "sniff|聞聞看|すんすん|匂いを嗅いで"),
    _t("sound", "yawns", "打哈欠", "yawning", "tired", "yawn|yawning|哈欠|呵欠|あくび|あくびしながら"),
    _t("sound", "hums", "哼歌", "humming", "happy", "humming|鼻歌|鼻歌まじり|ふんふん"),
    _t("sound", "hmm", "思考的嗯", "with a thoughtful hmm", None, "thinking hmm|嗯|うーん|んー|ふむ"),
    _t("sound", "groans", "呻吟", "groaning", None, "groan|groaning|唉唷|うめき|うめいて|うなって"),
    _t("sound", "moans", "低吟", "moaning softly", None, "moan|moaning"),
    _t("sound", "grunts", "悶哼", "with a grunt", None, "grunt|うっ|ぐっ"),
    _t("sound", "hmph", "不屑地哼", "with a dismissive hmph", "annoyed", "huffs|哼|哼一聲|ふんっ|フン"),
    _t("sound", "tsk", "嘖", "with a tongue click", "annoyed", "tch|tuts|clicks tongue|tongue click|咂嘴|舌打ち|ちっ|チッ"),
    _t("sound", "gulps", "吞口水", "with a nervous gulp", "nervous", "gulp|swallows|嚥口水|ごくり|ゴクリ|唾を飲んで"),
    _t("sound", "hiccups", "打嗝", "with a hiccup", None, "hiccup|しゃっくり|ひっく"),
    _t("sound", "screams", "尖叫", "screaming", "scared", "scream|screaming|shrieks|shriek|慘叫|悲鳴|悲鳴を上げて|きゃー|キャー|ぎゃー"),
    _t("sound", "yelps", "驚叫", "with a startled yelp", "surprised", "yelp|嚇到叫出來|ひゃっ|ひゃあ|きゃっ"),
    _t("sound", "squeals", "興奮尖叫", "squealing with delight", "excited", "squeal|歡呼尖叫|黄色い声"),
    _t("sound", "cheers", "歡呼", "cheering", "excited", "cheering|好耶|歓声|やったー"),
    _t("sound", "whistles", "吹口哨", "whistling", "happy", "whistle|口笛"),
    _t("sound", "kisses", "親親聲", "with a kiss sound", "teasing", "kiss|smooch|親親|啾|ちゅっ|チュッ"),
    # --- 停頓 ---
    _t("pause", "pause", "停頓", "", None, "beat|停一下|間|ポーズ|一拍|一拍置いて", pause=0.5),
    _t("pause", "short pause", "短停頓", "", None, "brief pause|頓一下|少し間|短い間", pause=0.25),
    _t("pause", "long pause", "長停頓", "", None, "silence|停很久|沉默|長い間|沈黙", pause=1.2),
]


def _norm(name: str) -> str:
    return re.sub(r"\s+", " ", name.replace("　", " ").strip().strip("*（）()").strip()).lower()


INDEX: dict[str, Tag] = {}
for _tag in CATALOGUE:
    for _n in (_tag.key, _tag.zh, *_tag.names):
        INDEX.setdefault(_norm(_n), _tag)

PAUSE = re.compile(r"^(?:pause|停頓|停|停一下|間|ポーズ|休止|wait)\s*[:：]?\s*(\d+(?:\.\d+)?)\s*"
                   r"(?:s|sec|secs|seconds?|秒)?$|^(\d+(?:\.\d+)?)\s*(?:s|sec|secs|seconds?|秒)$", re.IGNORECASE)
GROUP = re.compile(r"\[([^\[\]]{1,60})\]")
SPLIT = re.compile(r"[,，、]")


def lookup(name: str) -> Tag | None:
    return INDEX.get(_norm(name))


def same(a: str, b: str) -> bool:
    """Two tag names for the same thing ("喘氣" = "panting" = "はぁはぁ")."""
    if _norm(a) == _norm(b):
        return True
    ta, tb = lookup(a), lookup(b)
    return ta is not None and ta is tb


def pause_seconds(name: str) -> float | None:
    t = lookup(name)
    if t and t.pause is not None:
        return t.pause
    m = PAUSE.match(_norm(name))
    return min(10.0, float(m.group(1) or m.group(2))) if m else None


def is_event(name: str) -> bool:
    """Something that happens once (a sound, a pause), as opposed to a way of speaking that carries on."""
    t = lookup(name)
    return (t is not None and t.event) or pause_seconds(name) is not None


def style_of(name: str) -> str:
    """The English description for an engine; an unknown tag is used as written; a pause has none."""
    if pause_seconds(name) is not None:
        return ""
    t = lookup(name)
    return t.style if t else name.strip()


def emotion_of(names: list[str]) -> str | None:
    """The emotion label the tags point at: the first with one."""
    from . import emotions
    for n in names:
        t = lookup(n)
        e = t.emotion if t else emotions.from_style(n)
        if e:
            return e
    return None


def split_group(group: str) -> list[str]:
    return [t.strip() for t in SPLIT.split(group) if t.strip()]


def chunks(text: str) -> list[tuple[list[str], str]]:
    """The line as (tags, text) pieces: each [tag] starts a new piece, tags next to each other belong together,
    and tags at the very end have empty text."""
    text = text.replace("［", "[").replace("］", "]")
    out: list[tuple[list[str], str]] = []
    pos, cur = 0, []
    for m in GROUP.finditer(text):
        before = text[pos:m.start()]
        if before.strip():
            out.append((cur, before))
            cur = []
        cur = cur + split_group(m.group(1))
        pos = m.end()
    tail = text[pos:]
    if tail.strip() or cur:
        out.append((cur, tail))
    return out


def strip(text: str) -> str:
    """The text without any [tags]."""
    return re.sub(r"\s{2,}", " ", GROUP.sub(" ", text.replace("［", "[").replace("］", "]"))).strip()


def catalogue() -> dict:
    """For the interface: the groups with their tags, and the emotion labels."""
    from . import emotions
    return {"groups": [{"id": g, "name": name, "event": g in EVENT_GROUPS,
                        "tags": [{"key": t.key, "zh": t.zh, "style": t.style, "emotion": t.emotion,
                                  "names": list(t.names), "pause": t.pause} for t in CATALOGUE if t.group == g]}
                       for g, name in GROUPS.items()],
            "emotions": list(emotions.EMOTIONS.items())}


def markdown() -> str:
    """The tables in docs/14-tags.md (a test keeps the page in step with this list)."""
    from . import emotions
    out = ["### 情緒標籤（24 種）", "",
           "片段、參考片段、原音都用這些標情緒；標籤會挑對應情緒的參考片段。沒有那種情緒的參考片段時，依序改用相近的情緒，最後用平靜。", "",
           "| 代碼 | 中文 | 沒有時改用 |", "|---|---|---|"]
    for k, v in emotions.EMOTIONS.items():
        near = "、".join(emotions.EMOTIONS[x] for x in emotions.chain(k)[1:])
        out.append(f"| `{k}` | {v} | {near or '—'} |")
    for g, name in GROUPS.items():
        out += ["", f"### {name}" + ("（只在寫的位置出現一次）" if g in EVENT_GROUPS else ""), "",
                "| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |", "|---|---|---|---|---|"]
        for t in (x for x in CATALOGUE if x.group == g):
            effect = f"停 {t.pause:g} 秒" if t.pause is not None else t.style
            emo = emotions.EMOTIONS.get(t.emotion or "", "—")
            names = " ".join(f"`{n}`" for n in t.names)
            out.append(f"| `[{t.zh}]` | `[{t.key}]` | {names} | {effect} | {emo} |")
    return "\n".join(out) + "\n"

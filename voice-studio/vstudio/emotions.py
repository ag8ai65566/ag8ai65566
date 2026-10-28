"""Emotion / delivery labels for segments, reference clips and catchphrase clips.

Labels never enter the training text (neither engine's official fine-tuning format has a field for them, and
writing them into transcripts is untested); the model learns how the person sounds when angry from the audio
itself. Labels are for the person: finding clips, seeing what the data covers, and steering synthesis by picking
a reference or catchphrase clip of the right mood.
"""
from __future__ import annotations

import re

# order = keyboard shortcuts 1–9 on the review page, then the rest
EMOTIONS: dict[str, str] = {
    "neutral": "平靜", "happy": "開心", "excited": "興奮", "angry": "生氣", "sad": "難過", "soft": "小聲／溫柔",
    "laughing": "笑著說", "surprised": "驚訝", "scared": "害怕", "whisper": "悄悄話", "teasing": "撒嬌／調皮",
    "narration": "念稿／旁白", "annoyed": "不耐煩", "crying": "哭著說", "nervous": "緊張", "embarrassed": "害羞",
    "disgusted": "嫌棄", "tired": "疲倦／想睡", "shouting": "大喊", "serious": "認真", "cold": "冷淡", "smug": "得意",
    "sarcastic": "諷刺", "confused": "疑惑",
}

# words in a style hint, a [tag] or a label cell that point at a label (English, Japanese, Chinese). English words
# match whole; a trailing * also matches longer forms ("laugh*" → laughs, laughing). Known tag names are looked up
# in tags.py first; these catch free descriptions ("a bit nervous, slow").
WORDS: dict[str, tuple[str, ...]] = {
    "whisper": ("whisper*", "悄悄", "耳語", "ささや", "囁"),
    "laughing": ("laugh*", "giggl*", "chuckl*", "笑"),
    "shouting": ("shout*", "yell*", "scream*", "大喊", "吼", "叫ん", "怒鳴"),
    "crying": ("cry*", "crie*", "sob*", "tear*", "weep*", "哭", "泣"),
    "angry": ("angr*", "furious", "mad", "rage", "生氣", "憤怒", "怒"),
    "annoyed": ("annoy*", "irritat*", "impatient", "frustrat*", "grump*", "sulk*", "不耐煩", "煩", "イライラ"),
    "disgusted": ("disgust*", "gross*", "repuls*", "嫌棄", "噁心", "嫌悪"),
    "excited": ("excit*", "energetic", "hype*", "enthusias*", "興奮", "ワクワク", "テンション"),
    "happy": ("happ*", "cheer*", "bright", "joy*", "glad", "開心", "高興", "快樂", "嬉し", "楽し"),
    "sad": ("sad*", "subdued", "sorrow*", "melanchol*", "gloom*", "lonely", "難過", "悲", "寂"),
    "nervous": ("nervous*", "anxious*", "tense", "worried", "緊張", "不安", "ドキドキ"),
    "scared": ("scared", "afraid", "fear*", "terrif*", "panic*", "害怕", "恐", "怖"),
    "surprised": ("surpris*", "shock*", "gasp*", "astonish*", "驚訝", "驚", "びっくり"),
    "confused": ("confus*", "puzzl*", "baffl*", "疑惑", "困惑", "疑問", "戸惑"),
    "embarrassed": ("embarrass*", "bashful", "shy", "fluster*", "awkward", "害羞", "不好意思", "照れ", "恥ずかし"),
    "teasing": ("teas*", "playful*", "flirt*", "coax*", "cute", "撒嬌", "調皮", "甘え", "からか"),
    "smug": ("smug", "cocky", "proud", "boast*", "得意", "ドヤ"),
    "sarcastic": ("sarcas*", "ironic*", "snark*", "mock*", "諷刺", "嘲", "皮肉"),
    "cold": ("cold*", "distant", "aloof", "icy", "indifferent", "deadpan", "monoton*", "冷淡", "冷漠", "冷た", "クール"),
    "serious": ("serious*", "earnest*", "stern*", "determined", "resolute", "認真", "嚴肅", "真剣", "真面目"),
    "tired": ("tired*", "exhaust*", "sleep*", "drows*", "weary", "yawn*", "bored", "疲", "累", "想睡", "睏", "眠"),
    "soft": ("soft*", "quiet*", "gentl*", "tender*", "murmur*", "小聲", "溫柔", "優し", "小声"),
    "narration": ("narrat*", "reading", "storytell*", "念稿", "旁白", "朗讀", "ナレーション", "朗読"),
    "neutral": ("calm*", "steady", "neutral", "平靜", "冷靜", "落ち着"),
}

# the next best labels when no reference clip or recording has this one (a line marked embarrassed takes a soft
# reference before an arbitrary one); "neutral" comes last for every label
NEAR: dict[str, tuple[str, ...]] = {
    "happy": ("excited",), "excited": ("happy",), "angry": ("annoyed",), "sad": ("crying", "soft"),
    "soft": ("whisper",), "laughing": ("happy",), "surprised": ("excited",), "scared": ("nervous",),
    "whisper": ("soft",), "teasing": ("happy",), "annoyed": ("angry",), "crying": ("sad",), "nervous": ("scared",),
    "embarrassed": ("soft", "teasing"), "disgusted": ("annoyed", "angry"), "tired": ("soft", "sad"),
    "shouting": ("excited", "angry"), "serious": ("narration",), "cold": ("serious",), "smug": ("teasing", "happy"),
    "sarcastic": ("teasing", "cold"), "confused": ("surprised",),
}


def chain(e: str | None) -> list[str]:
    """The label, the nearest ones, then neutral (empty when no label is wanted)."""
    if not e:
        return []
    return list(dict.fromkeys([e, *NEAR.get(e, ()), "neutral"]))


def _find(word: str, s: str) -> int:
    if not word.isascii():
        return s.find(word)
    stem = word.rstrip("*")
    m = re.search(r"\b" + re.escape(stem) + (r"\w*" if word.endswith("*") else r"\b"), s)
    return m.start() if m else -1


def valid(e: str | None) -> str | None:
    """A known label, or None (unlabelled). Anything else is rejected by the API layer."""
    return e if e in EMOTIONS else None


def from_style(style: str | None) -> str | None:
    """The label a style hint asks for: the earliest matching word wins ("excited, then calm" → excited)."""
    if not style:
        return None
    s = style.lower()
    best: tuple[int, str] | None = None
    for emo, words in WORDS.items():
        for w in words:
            i = _find(w, s)
            if i >= 0 and (best is None or i < best[0]):
                best = (i, emo)
    return best[1] if best else None


def from_text_tags(text: str) -> str | None:
    """The label of the first [tag] in a line that points at one, e.g. "[照れて] もう…" → embarrassed."""
    from . import tags
    for g in tags.GROUP.findall((text or "").replace("［", "[").replace("］", "]")):
        e = tags.emotion_of(tags.split_group(g))
        if e:
            return e
    return None

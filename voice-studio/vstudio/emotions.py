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
    "neutral": "平靜", "happy": "開心", "excited": "興奮", "angry": "生氣", "sad": "難過", "soft": "小聲",
    "laughing": "笑著說", "surprised": "驚訝", "scared": "害怕", "whisper": "悄悄話", "teasing": "撒嬌",
    "narration": "念稿／旁白",
}

# words in a style hint or a [tag] that point at a label (English hints, ElevenLabs tags, Chinese chips).
# English words match whole; a trailing * also matches longer forms ("laugh*" → laughs, laughing).
WORDS: dict[str, tuple[str, ...]] = {
    "whisper": ("whisper*", "悄悄"),
    "laughing": ("laugh*", "giggl*", "chuckl*", "笑"),
    "angry": ("angr*", "annoy*", "sharp", "furious", "mad", "irritat*", "生氣", "怒"),
    "excited": ("excit*", "energetic", "hype*", "興奮"),
    "happy": ("happ*", "cheer*", "bright", "joy*", "開心", "高興"),
    "sad": ("sad*", "subdued", "cry*", "sorrow*", "難過", "悲"),
    "scared": ("scared", "afraid", "fear*", "nervous*", "害怕"),
    "surprised": ("surpris*", "shock*", "gasp*", "驚訝"),
    "teasing": ("teas*", "playful*", "flirt*", "撒嬌", "調皮"),
    "soft": ("soft*", "quiet*", "gentl*", "小聲", "溫柔"),
    "narration": ("narrat*", "reading", "念稿", "旁白"),
    "neutral": ("calm*", "steady", "neutral", "平靜"),
}


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


TAG = re.compile(r"\[([^\[\]]{1,40})\]")


def from_text_tags(text: str) -> str | None:
    """The label of the first [tag] in a line, e.g. "[angry] もういい！" → angry."""
    for t in TAG.findall(text or ""):
        e = from_style(t)
        if e:
            return e
    return None

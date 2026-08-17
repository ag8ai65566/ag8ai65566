"""Prompt text tricks that ComfyUI's own text box does not do.

Two separate things live here.

`expand()` implements dynamic prompts - `{red|blue|green}` picks one at random,
`{2$$a|b|c}` picks two. Automatic1111 users get this from the sd-dynamic-prompts
extension and ComfyUI users from a custom node pack; neither ships it by
default, yet it is the single cheapest way to get variety out of a batch. Each
image in a batch is expanded separately, so "one prompt, eight different
outfits" is one click rather than eight runs.

`weights_ok()` sanity-checks the attention syntax - `(word:1.3)` - that
CLIPTextEncode *does* parse but never validates. An unbalanced parenthesis
silently changes the meaning of the rest of the prompt, which is a miserable
thing to debug by staring at output images.
"""

from __future__ import annotations

import random
import re

MAX_DEPTH = 8

# {a|b|c} or {2$$a|b|c}. Innermost first, so nesting resolves outwards.
_CHOICE = re.compile(r"\{([^{}]*)\}")
_COUNT = re.compile(r"^\s*(\d+)\s*\$\$(.*)$", re.S)


def expand(text: str, rng: random.Random | None = None) -> str:
    """Resolve every {a|b|c} group in `text`.

    A group with no `|` is left alone: `{}` and `{foo}` appear in ordinary
    prompts (and in some LoRA trigger words), and eating them would corrupt a
    prompt that never asked for this feature.
    """
    rng = rng or random
    for _ in range(MAX_DEPTH):
        if "{" not in text:
            break
        replaced = False

        def one(match: re.Match) -> str:
            nonlocal replaced
            body = match.group(1)
            count = 1
            if m := _COUNT.match(body):
                count, body = int(m.group(1)), m.group(2)
            if "|" not in body:
                return match.group(0)  # not a choice group; leave verbatim
            options = [o.strip() for o in body.split("|")]
            options = [o for o in options if o] or [""]
            replaced = True
            count = max(1, min(count, len(options)))
            if count == 1:
                return rng.choice(options)
            return ", ".join(rng.sample(options, count))

        text = _CHOICE.sub(one, text)
        if not replaced:
            break
    return text


def has_wildcards(text: str) -> bool:
    return any("|" in m for m in _CHOICE.findall(text or ""))


def preview(text: str, n: int = 3, seed: int = 0) -> list[str]:
    """A few example expansions, so the UI can show what a wildcard will do."""
    rng = random.Random(seed)
    return [expand(text, rng) for _ in range(max(1, n))]


def weights_ok(text: str) -> str:
    """'' if the prompt is fine, else one plain-language complaint.

    Only parentheses are checked, because parentheses are the only weighting
    syntax ComfyUI actually parses (comfy/sd1_clip.py: `(x)` multiplies by 1.1,
    `(x:1.3)` sets 1.3, nesting multiplies). Automatic1111's `[x]` and the
    `<lora:name:1>` inline form are *not* parsed - they are encoded as literal
    words, which quietly poisons the prompt. Saying so is more useful than
    pretending they are bracket errors.
    """
    depth = 0
    escaped = re.sub(r"\\[()]", "", text or "")
    for ch in escaped:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return "提詞裡的 `)` 比 `(` 多，權重語法會被讀錯"
    if depth > 0:
        return f"提詞裡有 {depth} 個 `(` 沒關起來，權重語法會被讀錯"
    if re.search(r"<\s*lora\s*:", escaped, re.I):
        return ("ComfyUI 不吃 `<lora:名字:1>` 這種寫法，它會被當成一般文字。"
                "請改用下面的 LoRA 清單勾選。")
    for bad in re.finditer(r":\s*([0-9]*\.?[0-9]+)\s*\)", escaped):
        if float(bad.group(1)) > 2.0:
            return (f"權重 {bad.group(1)} 太高了，超過約 1.5 通常會把畫面燒壞；"
                    "1.1～1.4 才是常用範圍")
    return ""


def strip_prefix(prompt: str, prefix: str) -> str:
    """Remove a model's auto quality prefix, however it was spaced."""
    if not prefix:
        return prompt
    pattern = re.escape(prefix).replace(r"\,\ ", r"\s*,\s*")
    return re.sub(rf"^\s*{pattern}\s*,?\s*", "", prompt or "")


# Prompt syntax cheatsheet, shown in the UI instead of buried in a wiki.
SYNTAX_HELP = [
    ("(字:1.3)", "加重這個詞。1.1～1.4 是常用範圍，超過 1.5 容易把畫面燒壞。"),
    ("(字:0.7)", "減弱這個詞，但不完全拿掉。"),
    ("{紅|藍|綠}裙子", "每張隨機挑一個。一次生 8 張就有 8 種顏色。"),
    ("{2$$長髮|貓耳|眼鏡}", "從清單裡隨機挑 2 個。"),
    ("embedding:名字", "套用一個 embedding（負面詞常用，例如 easynegative）。"),
    ("\\(字\\)", "反斜線跳脫，讓括號變成畫面裡真的括號，而不是加重。"),
]

# Things people type out of A1111 habit that ComfyUI silently treats as words.
NOT_SUPPORTED = [
    ("[字]", "ComfyUI 沒有這個減弱語法，請改用 `(字:0.8)`。"),
    ("<lora:名字:1>", "ComfyUI 不吃行內 LoRA，請用下面的 LoRA 清單勾選。"),
    ("BREAK", "核心 ComfyUI 不支援，會被當成一個普通英文字編進去。"),
    # Verified by running ComfyUI 0.33's own token_weights() on it: the braces
    # come out as literal text at weight 1.0.
    ("{{字}}", "這是 NovelAI 的加重語法，ComfyUI 不吃 —— 大括號會原封不動變成提詞的一部分。"
               "要加重請用 `(字:1.3)`。"),
]

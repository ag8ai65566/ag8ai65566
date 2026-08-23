"""A health check for a prompt, run before anything is generated.

This exists because the most common reason a picture comes out badly is not the
prompt at all - it is a 512x512 canvas on a model trained at 1024x1024, or a
`score_9` string left over from a Pony prompt, or thirty negative tags copied
from a screenshot. None of those are visible by reading the prompt, so the app
should say them out loud.

Every check is a rule with a stated source. Nothing here is a model of image
quality - the app has never generated an image, there is no GPU in the machine
it was built on - so a finding says "this token belongs to a different
checkpoint" or "this canvas is a quarter of the trained area", never "this will
look bad". The difference matters: the first is checkable, the second is not.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import images
import promptmerge as pm
import styles


@dataclass
class Finding:
    id: str
    level: str            # high | warn | info
    zh: str               # the one-line message
    detail: str = ""      # why, with its source
    action: str = ""      # remove | resize | replace | none
    tags: list[str] = field(default_factory=list)
    size: tuple[int, int] | None = None

    def public(self) -> dict:
        d = {
            "id": self.id, "level": self.level, "zh": self.zh,
            "detail": self.detail, "action": self.action, "tags": self.tags,
        }
        if self.size:
            d["width"], d["height"] = self.size
        return d


# Words people stack hoping quality falls out. Two different things live here and
# the check keeps them apart: the ones a model card actually documents (they work,
# but a card lists five, not fifteen), and the ones no anime checkpoint documents
# at all (`8k`, `ultra detailed`, `masterpiece++`) which are pure cargo cult on a
# danbooru finetune.
CARD_QUALITY = {
    "masterpiece", "best quality", "good quality", "normal quality",
    "worst quality", "bad quality", "average quality", "low quality",
    "amazing quality", "very aesthetic", "displeasing", "very displeasing",
    "absurdres", "highres", "lowres", "very awa",
}
FOLKLORE_QUALITY = {
    "4k", "8k", "16k", "uhd", "ultra hd", "hd", "high resolution", "ultra detailed",
    "extremely detailed", "hyper detailed", "super detailed", "intricate details",
    "high detail", "ultra quality", "perfect quality", "top quality", "high quality",
    "award winning", "trending on artstation", "artstation", "photorealistic 8k",
    "sharp focus", "professional", "unreal engine", "octane render",
    "cinematic lighting", "studio quality",
}

# Which quality words each checkpoint's own card documents. Anything outside its
# set is another model's dialect, not an upgrade.
CARD_SET: dict[str, set[str]] = {
    "noobai": {"masterpiece", "best quality", "good quality", "normal quality",
               "worst quality", "absurdres", "highres", "lowres", "low quality"},
    "illustrious": {"masterpiece", "best quality", "good quality", "average quality",
                    "bad quality", "worst quality", "low quality", "lowres",
                    "displeasing", "very displeasing", "absurdres", "highres"},
    "pony": set(),
}

QUALITY_CEILING = 6      # more than this and it is stacking, not scaffolding
NEGATIVE_CEILING = 28    # NoobAI's own example negative has 15 tags


def _bare(tags: list[str]) -> list[str]:
    return [pm.key(t) for t in tags]


def check(
    prompt: str,
    negative: str = "",
    *,
    model_id: str = "",
    width: int = 0,
    height: int = 0,
) -> list[Finding]:
    """Every problem this can see, worst first."""
    model = images.get(model_id) if model_id else None
    pos = pm.split_tags(prompt)
    neg = pm.split_tags(negative)
    kpos, kneg = _bare(pos), _bare(neg)
    setpos, setneg = set(kpos), set(kneg)
    out: list[Finding] = []

    # -- 1. canvas size. Almost always the real answer to "why is it bad".
    if model and width and height:
        px = width * height
        native = 1024 * 1024
        if min(width, height) < 640 or px < native * 0.45:
            out.append(Finding(
                "resolution", "high",
                f"畫布 {width}×{height} 對這個模型太小了。",
                f"{model.label.split('—')[0].strip()} 是 SDXL，訓練時就是 1024×1024 左右"
                f"（約 105 萬像素）。你現在只有 {px/10000:.0f} 萬像素，大約是訓練面積的 "
                f"{px/native:.0%}。SDXL 在遠低於原生解析度時會明顯掉細節、也容易畫壞手跟臉，"
                f"這通常比再加二十個提詞影響大得多。建議改成 832×1216 或 1024×1024。",
                action="resize", size=(832, 1216),
            ))
        elif px > native * 2.6:
            out.append(Finding(
                "resolution-big", "warn",
                f"畫布 {width}×{height} 遠大於原生尺寸。",
                "SDXL 直接生成遠大於 1024² 的圖，很容易出現重複的頭或身體（雙頭、四手）。"
                "比較穩的做法是先用原生尺寸生成，再放大。",
                action="resize", size=(1024, 1024),
            ))

    # -- 2. score dialect
    scores = [t for t, k in zip(pos, kpos) if k.replace(" ", "_").startswith("score_")
              or k.startswith("score ")]
    if scores and model_id and model_id != "pony":
        out.append(Finding(
            "score-dialect", "warn",
            f"提詞裡有 {len(scores)} 個 Pony 的 score_ 標籤，這個模型用不到。",
            "`score_9` 那一串是 Pony Diffusion V6 XL 專屬的品質控制詞，"
            "是 Pony 訓練時自己加進 caption 的。NoobAI 跟 Illustrious 的 caption 沒有這些字，"
            "留著只是佔 token。",
            action="remove", tags=scores,
        ))
    if model_id == "pony" and not scores:
        out.append(Finding(
            "score-missing", "warn",
            "Pony 少了開頭那串 score_ 標籤。",
            "Pony 官方頁明講：只用 `score_9` 的效果比完整六個弱很多。"
            "完整是 `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up`。",
            action="replace", tags=pm.split_tags(styles.PRESET_BY_ID["pony-official"].positive),
        ))

    # -- 3. quality word stacking
    quality = [t for t, k in zip(pos, kpos) if k in CARD_QUALITY or k in FOLKLORE_QUALITY]
    folklore = [t for t, k in zip(pos, kpos) if k in FOLKLORE_QUALITY]
    if folklore:
        out.append(Finding(
            "folklore-quality", "warn",
            f"有 {len(folklore)} 個沒有任何模型 card 列過的品質詞。",
            "`8k`、`ultra detailed`、`trending on artstation` 這一類是從 Midjourney 跟 "
            "SD1.5 時代帶過來的，danbooru 系的微調（NoobAI / Illustrious / Pony）"
            "caption 裡完全沒有這些字。它們不會壞事，但也沒有你以為的作用，"
            "而且會稀釋真正有用的詞。",
            action="remove", tags=folklore,
        ))
    if len(quality) > QUALITY_CEILING:
        out.append(Finding(
            "quality-stack", "warn",
            f"品質詞有 {len(quality)} 個，通常 3-5 個就到頂了。",
            "品質詞是模型作者用分數百分位反推出來塞進 caption 的，"
            "NoobAI 一整張圖只會被貼到**一個**（masterpiece / best quality / … 五選一）。"
            "堆五個以上等於把同一個方向重複講，剩下的只是排擠掉你真正想要的內容詞。",
            action="none", tags=quality,
        ))
    if model_id in CARD_SET:
        foreign_q = [t for t, k in zip(pos, kpos)
                     if k in CARD_QUALITY and k not in CARD_SET[model_id]]
        if foreign_q:
            out.append(Finding(
                "foreign-quality", "info",
                f"{len(foreign_q)} 個品質詞不在這個模型的 model card 上。",
                "例如 `amazing quality`、`very aesthetic` 是 WAI、Animagine 這些**微調**"
                "自己加的詞，base Illustrious 跟 NoobAI 的 card 都沒有列。"
                "在別的模型上不是錯，只是沒有訓練支撐。",
                action="none", tags=foreign_q,
            ))

    # -- 4. negative length
    if len(neg) > NEGATIVE_CEILING:
        out.append(Finding(
            "negative-long", "info",
            f"負面提詞有 {len(neg)} 個。",
            "長負面本身不是錯——NoobAI 官方範例就有 15 個。但超過三十個以後，"
            "多半是好幾份範本疊在一起，裡面會有重複、也會有互相矛盾的詞。"
            "值得看一遍而不是無腦照抄。",
            action="none",
        ))

    # -- 5. same tag on both sides
    both = sorted(setpos & setneg)
    if both:
        out.append(Finding(
            "both-sides", "high",
            f"有 {len(both)} 個詞同時出現在正面跟負面。",
            "正負面各自送進 text encoder，同一個詞兩邊都有等於自己抵銷自己，"
            "結果會偏向哪邊沒人說得準。挑一邊。相關的詞："
            + "、".join(f"`{b}`" for b in both[:8]),
            action="none", tags=both,
        ))

    # -- 6. conflicts inside the positive prompt
    seen_pairs: set[tuple[str, str]] = set()
    for i, a in enumerate(pos):
        for b in pos[i + 1:]:
            cid = pm.conflicts_with(a, b)
            if not cid:
                continue
            pair = tuple(sorted((pm.key(a), pm.key(b))))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            c = pm.CONFLICT_BY_ID[cid]
            out.append(Finding(
                f"conflict-{cid}", "warn",
                f"`{pair[0]}` 跟 `{pair[1]}` 互相衝突。",
                c.why + "（" + c.evidence + "）",
                action="none", tags=[pair[0], pair[1]],
            ))

    # -- 7. duplicates
    dupes = sorted({k for k in kpos if k and kpos.count(k) > 1})
    if dupes:
        out.append(Finding(
            "duplicate", "info",
            f"有 {len(dupes)} 個詞重複了。",
            "重複同一個詞不等於加權（ComfyUI 是逗號分隔後各自 tokenise，"
            "重複只是多送一次同樣的 token）。真的想加強請用 `(tag:1.2)`。",
            action="none", tags=dupes,
        ))

    # -- 8. framing tags. Illustrious's card says do not overuse, not never mix.
    framing = [t for t, k in zip(pos, kpos)
               if k in {"portrait", "upper body", "cowboy shot", "full body",
                        "close-up", "wide shot", "upside-down"}]
    if len(framing) >= 3:
        out.append(Finding(
            "framing", "info",
            f"有 {len(framing)} 個構圖／取景標籤。",
            "Illustrious 的 model card 直接寫了：`close-up`、`upside-down`、`cowboy shot` "
            "這類構圖詞不要濫用，它們會互相打架、讓結果變糊。兩個以內通常最穩。"
            "（不過 danbooru 上 portrait 跟 close-up 的共現是 11 倍，"
            "所以這是提醒不是錯誤。）",
            action="none", tags=framing,
        ))

    # -- 9. artist spelling for this checkpoint
    if model:
        art = [t for t, k in zip(pos, kpos) if k.startswith("artist:") or k.startswith("by ")]
        if art and not model.artist_form:
            out.append(Finding(
                "artist-ignored", "warn",
                f"這個模型基本上不吃畫師標籤（找到 {len(art)} 個）。",
                "Pony V6 在訓練時把畫師名字從 caption 裡拿掉了，"
                "Juggernaut 跟 SDXL base 也沒有 danbooru 畫師詞彙。"
                "想要特定畫風要靠 LoRA，不是靠標籤。",
                action="none", tags=art,
            ))
        elif art and model.artist_form:
            want = "artist:" if model.artist_form.startswith("artist:") else "by "
            wrong = [t for t, k in zip(pos, kpos)
                     if (k.startswith("artist:") or k.startswith("by ")) and not k.startswith(want)]
            if wrong:
                out.append(Finding(
                    "artist-form", "info",
                    f"畫師標籤的寫法跟這個模型的 card 不一樣（{len(wrong)} 個）。",
                    f"這個模型的 card 用的是 `{model.artist_form.format(tag='name')}`。"
                    "兩種寫法都會有效果，但照 card 的寫法比較準。",
                    action="none", tags=wrong,
                ))

    # -- 10. nothing to draw
    if not pos:
        out.append(Finding("empty", "high", "提詞是空的。", "至少要有一個主體，例如 `1girl`。"))
    elif not any(k in {"1girl", "2girls", "1boy", "2boys", "1other", "multiple girls",
                       "multiple boys", "no humans", "solo"} for k in kpos):
        out.append(Finding(
            "no-subject", "info",
            "沒有 `1girl` / `1boy` / `no humans` 這種數量標籤。",
            "danbooru 系的 caption 幾乎每一張都是這個字開頭，模型很依賴它決定畫幾個人。"
            "少了它人數常常會跑掉。",
            action="none",
        ))

    order = {"high": 0, "warn": 1, "info": 2}
    out.sort(key=lambda f: order[f.level])
    return out


def summary(findings: list[Finding]) -> dict:
    highs = sum(1 for f in findings if f.level == "high")
    warns = sum(1 for f in findings if f.level == "warn")
    if highs:
        line, level = f"有 {highs} 個要先處理的問題", "high"
    elif warns:
        line, level = f"有 {warns} 個值得看一下的地方", "warn"
    elif findings:
        line, level = "大致沒問題，有幾個小提醒", "info"
    else:
        line, level = "提詞健康度：良好", "ok"
    return {
        "level": level, "line": line,
        "high": highs, "warn": warns, "info": len(findings) - highs - warns,
        "findings": [f.public() for f in findings],
    }

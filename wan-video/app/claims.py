"""Every factual claim this app makes at the user, with what backs it.

The problem this solves is one an outside review caught twice in this project.
The first time it was a danbooru ratio: five popular characters were spot-checked
at 1-3% official art and that was written down as true of all 75, when measuring
all 75 gave 0.62%-9.45%. The second time it was the short-drama feature, where
"a LoRA is ~100% consistent", "three seconds is where the model starts to break"
and "the frame-rate artifact is what gives those platforms away" were all written
as established fact in three places each - module docstring, UI copy, and the
research document - with no measurement behind any of them.

Repeating a claim in three files guarantees the three copies drift. Grading a
claim as "true" guarantees nobody asks who measured it. So both problems get the
same fix: **each claim exists once, here, and says what kind of evidence it has.**

Two things are kept deliberately separate, because collapsing them is what
produced the overconfidence in the first place:

  * ``evidence_kind`` - *who established this, and how.* An official spec and a
    number quoted from a trade article are not the same thing even when both
    are true.
  * ``policy`` - *what the product should do about it.* Severity is a product
    decision, not a property of the evidence. A hypothesis can be worth showing;
    an official spec can be worth ignoring.

Data integrity is **not** in here. "The speaker is not in this shot's cast" is
not a claim about the world that could turn out to be wrong - it is a broken
record. Those live in the validator as INTEGRITY findings, so that a bug in the
data can never be softened by a debate about evidence.

The taxonomy came out of a review round with a second model; the argument for
splitting FACT and MEASURED apart was its, and it was right.
"""

from __future__ import annotations

from dataclasses import dataclass


# -- how something came to be believed ---------------------------------------

OFFICIAL_SPEC = "OFFICIAL_SPEC"
"""Upstream states it: a model card, an official workflow, an API's own docs.

Checkable by anyone, and dated - because software specs change under you.
"""

LOCAL_MEASUREMENT = "LOCAL_MEASUREMENT"
"""Measured here, under stated conditions, with an experiment id to point at.

"I tried it and it looked better" is not this. Without a seed count, a model
hash and a written-down question it is a HYPOTHESIS with extra confidence.
"""

EXTERNAL_MEASUREMENT = "EXTERNAL_MEASUREMENT"
"""Somebody else measured it and this project has not reproduced it.

Worth quoting, worth attributing, and worth keeping the sample scope attached.
The failure mode is quietly promoting it to a law once it has been repeated a
few times.
"""

INDUSTRY_CONVENTION = "INDUSTRY_CONVENTION"
"""What the field does, with no causal claim attached.

9:16, a one-to-three-minute episode, a fifteen-character line. Deviating is not
an error; it is a deviation, and the user may well mean it.
"""

AUTHOR_RECOMMENDATION = "AUTHOR_RECOMMENDATION"
"""This project's own advice, on grounds of cost, reversibility or safety.

"Fix the still before generating the clip" is defensible without any claim about
picture quality: a still is cheap to redo and a clip is not. It has to be worded
as advice from this tool, never as a fact about the world.
"""

HYPOTHESIS = "HYPOTHESIS"
"""Plausible, unverified, and waiting for an experiment.

Everything this project believes about how a *picture* will look is in here,
because it has never generated one.
"""

EVIDENCE_KINDS = (
    OFFICIAL_SPEC, LOCAL_MEASUREMENT, EXTERNAL_MEASUREMENT,
    INDUSTRY_CONVENTION, AUTHOR_RECOMMENDATION, HYPOTHESIS,
)

EVIDENCE_ZH = {
    OFFICIAL_SPEC: "官方規格",
    LOCAL_MEASUREMENT: "本專案實測",
    EXTERNAL_MEASUREMENT: "外部實測（未重現）",
    INDUSTRY_CONVENTION: "產業慣例",
    AUTHOR_RECOMMENDATION: "本工具建議",
    HYPOTHESIS: "待驗證假說",
}

# -- what the product does about it ------------------------------------------
# Severity is decided per claim, not derived from the evidence kind.

BLOCK = "BLOCK"      # the thing cannot work as configured
WARN = "WARN"        # likely to waste the user's time
INFO = "INFO"        # worth knowing, not worth stopping for
GUIDE = "GUIDE"      # advice, shown where the choice is made
POLICIES = (BLOCK, WARN, INFO, GUIDE)


@dataclass(frozen=True)
class Claim:
    id: str
    text: str                       # the claim, stated once, in the UI's voice
    evidence_kind: str
    source: str = ""                # where it came from, in words
    urls: tuple[str, ...] = ()
    checked: str = ""               # ISO date; specs rot
    scope: str = ""                 # what it is true *of*
    limits: str = ""                # what it is explicitly not true of
    policy: str = INFO

    @property
    def badge(self) -> str:
        return EVIDENCE_ZH.get(self.evidence_kind, self.evidence_kind)

    @property
    def evidenced(self) -> bool:
        """Whether *someone* specified or measured this - not necessarily here.

        Deliberately not called `verified`. An external measurement with no
        published method is not the same standard as an official spec, and one
        boolean covering both would let a trade-article number borrow the
        credibility of a model card. The UI shows the three counts separately.
        """
        return self.evidence_kind in (OFFICIAL_SPEC, LOCAL_MEASUREMENT,
                                      EXTERNAL_MEASUREMENT)

    def public(self) -> dict:
        return {
            "id": self.id, "text": self.text, "evidence": self.evidence_kind,
            "badge": self.badge, "source": self.source, "urls": list(self.urls),
            "checked": self.checked, "scope": self.scope, "limits": self.limits,
            "policy": self.policy, "evidenced": self.evidenced,
            "upstream": self.evidence_kind == OFFICIAL_SPEC,
        }


# -- the claims --------------------------------------------------------------
# Ordered by subject. Where a claim was previously stated more strongly than the
# evidence supports, `limits` says so out loud rather than the wording just
# getting quietly softer - a reader who saw the old version deserves to know it
# changed and why.

CLAIMS: tuple[Claim, ...] = (
    # --- format conventions. Real, sourced, and not laws.
    Claim(
        id="format.vertical",
        text="豎屏短劇是 9:16 直式。",
        evidence_kind=INDUSTRY_CONVENTION,
        source="豎屏短劇的通行交付格式",
        scope="要放到短劇平台的成品",
        limits="自己看的、或要投到別的版位的，不必照這個。",
        policy=WARN,
    ),
    Claim(
        id="format.episode_length",
        text="單集慣例是 1-3 分鐘。",
        evidence_kind=INDUSTRY_CONVENTION,
        source="紅果等平台的編劇指南與公開的分集慣例",
        scope="投平台的連載短劇",
        policy=INFO,
    ),
    Claim(
        id="format.shot_median",
        text="一部 8 分鐘的成片約 117 顆鏡頭，平均 4.1 秒、中位數 3.2 秒。",
        evidence_kind=EXTERNAL_MEASUREMENT,
        source="對一部公開 AI 短劇成片的鏡頭統計",
        urls=("https://www.blocktempo.com/huangguo-ai-shortdrama-tech-stack-reverse-analysis/",),
        checked="2026-09-06",
        scope="被統計的那一部成片",
        limits="這是那部片的**剪輯節奏**，不是任何模型的故障閾值。"
               "它不能證明超過 3.2 秒畫面就會壞。",
        policy=INFO,
    ),
    Claim(
        id="format.line_length",
        text="單句台詞慣例壓在 15 字以內，一集有效台詞約 200-300 字。",
        evidence_kind=INDUSTRY_CONVENTION,
        source="短劇編劇指南",
        scope="中文豎屏短劇",
        policy=INFO,
    ),
    Claim(
        id="format.hook",
        text="開場「黃金 3 秒」：開篇 30 秒內要拋出核心衝突或懸念。",
        evidence_kind=INDUSTRY_CONVENTION,
        source="短劇編劇指南",
        scope="靠推薦流分發的連載短劇",
        limits="這是分發環境造成的慣例，不是敘事定律。",
        policy=INFO,
    ),

    # --- model specs. Checkable upstream, and dated.
    Claim(
        id="wan22.flf_uses_i2v_weights",
        text="Wan 2.2 官方的首尾幀（FLF2V）工作流用的是跟 I2V 同一份模型檔，"
             "差別在工作流與多一張結束幀，不需要另外下載模型。",
        evidence_kind=OFFICIAL_SPEC,
        source="ComfyUI 官方 Wan 2.2 工作流說明",
        urls=("https://docs.comfy.org/tutorials/video/wan/wan2_2",),
        checked="2026-09-06",
        scope="ComfyUI 官方的 Wan 2.2 14B FLF2V 工作流",
        limits="不表示所有 Wan I2V 的衍生 checkpoint 或第三方 wrapper 都相容。",
        policy=INFO,
    ),
    Claim(
        id="s2v.audio_driven",
        text="Wan 2.2 S2V 是音訊驅動的：音檔是輸入，口型在同一個 pass 產生。",
        evidence_kind=OFFICIAL_SPEC,
        source="ComfyUI 官方 Wan 2.2 S2V 說明",
        urls=("https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v",),
        checked="2026-09-06",
        scope="Wan 2.2 S2V 工作流",
        policy=INFO,
    ),
    Claim(
        id="s2v.audio_first",
        text="對白鏡頭要先做音檔再生影片：音檔是輸入，它的長度決定鏡頭長度。",
        evidence_kind=AUTHOR_RECOMMENDATION,
        source="由 s2v.audio_driven 推出的操作順序",
        scope="用 S2V 生成的對白鏡頭",
        limits="這是工序上的先後，不是畫質主張。",
        policy=GUIDE,
    ),
    Claim(
        id="s2v.vs_postsync",
        text="原生音訊驅動與事後補口型（InfiniteTalk／LatentSync）是兩條不同的工作流，"
             "輸入與返工成本不同。",
        evidence_kind=AUTHOR_RECOMMENDATION,
        source="兩者的官方說明",
        scope="工作流選擇",
        limits="**本專案沒有比較過兩者的成品品質。**"
               "先前寫成「補的永遠比原生差」是沒有證據的。",
        policy=GUIDE,
    ),
    Claim(
        id="sdxl.native_resolution",
        text="SDXL 系底模的訓練解析度在 1 百萬像素附近（約 1024×1024）。",
        evidence_kind=OFFICIAL_SPEC,
        source="SDXL 的模型說明與官方尺寸表",
        checked="2026-09-06",
        scope="SDXL 架構的底模",
        limits="偏離建議尺寸會怎樣是**未經本專案驗證的**。"
               "先前寫成「直接 1080×1920 會出雙頭」是把預測寫成了事實。",
        policy=WARN,
    ),
    Claim(
        id="video.clip_length_is_spec",
        text="影片模型的預設幀數與 fps 是規格，兩者相除就是**目前這個設定**"
             "會生成的秒數。",
        evidence_kind=OFFICIAL_SPEC,
        source="各模型的 model card 與官方工作流的預設值",
        scope="本目錄裡列出的影片模型的預設設定",
        limits="**這不是模型的硬上限。** 官方工作流的幀數是可以調的，"
               "Animate 還有延伸機制。所以「超過」代表的是「超過目前設定會生成的長度」，"
               "不是「模型做不到」。",
        policy=WARN,
    ),

    # --- the things that used to be written as fact and are not.
    Claim(
        id="consistency.lora",
        text="角色 LoRA 是維持角色一致性的候選方法之一，另外還有參考圖控制、"
             "IP-Adapter、ControlNet 與角色包。",
        evidence_kind=HYPOTHESIS,
        source="產業文章互相引用的一致性百分比",
        scope="長篇多鏡頭的角色一致性",
        limits="流傳的「85-90% / 90-95% / 接近 100%」沒有定義量測方法、"
               "資料集、角色數或合格門檻，本專案也沒有重現過。"
               "**先前把它寫成事實、還推論出「精修 40% 工時幾乎全是這筆帳」，"
               "那步推論完全沒有證據。** 要比較就用固定 seed 盲測。",
        policy=GUIDE,
    ),
    Claim(
        id="production.retouch_share",
        text="有製作方報告人工精修佔 AI 短劇總工時 40% 以上。",
        evidence_kind=EXTERNAL_MEASUREMENT,
        source="對 AI 短劇製作流程的產業分析",
        urls=("https://www.blocktempo.com/huangguo-ai-shortdrama-tech-stack-reverse-analysis/",),
        checked="2026-09-06",
        scope="被報導的那些製作團隊",
        limits="沒有公開量測定義，也不能歸因到任何單一原因。",
        policy=INFO,
    ),
    Claim(
        id="video.drift_with_length",
        text="影片模型的輸出可能隨片段變長而偏離（角色漂移、手部崩壞）。",
        evidence_kind=HYPOTHESIS,
        source="社群普遍回報，本專案未驗證",
        scope="目前這一代的本機影片模型",
        limits="**本專案沒有生成過任何影片**，所以「幾秒之後開始壞」沒有數字。"
               "先前寫的 3 秒閾值與 6 秒上限都是編出來的門檻。",
        policy=INFO,
    ),
    Claim(
        id="fps.mixed_timeline_artifact",
        text="外部分析推測：AI 短劇平台成品裡看得到的補幀痕跡，"
             "來自兩條原生幀率不同的軌道併到同一條時間線。",
        evidence_kind=HYPOTHESIS,
        source="對黃果技術架構的外部逆向分析，該文自己也說是「最合理解釋」",
        urls=("https://www.blocktempo.com/huangguo-ai-shortdrama-tech-stack-reverse-analysis/",),
        checked="2026-09-06",
        scope="那篇分析看到的成品",
        limits="從成片目測無法證明某個 artifact 必然由 24→30fps 造成，"
               "也排除不掉採樣、壓縮、模型與後期的影響。"
               "**先前在程式、UI 與文件裡把它寫成已證實的因果，那是過度推論。**",
        policy=INFO,
    ),
    Claim(
        id="fps.single_native_rate",
        text="整集只用一種原生幀率、或明確定義每條路線怎麼正規化到交付幀率，"
             "可以避免整類的幀率轉換問題。",
        evidence_kind=AUTHOR_RECOMMENDATION,
        source="幀率轉換的算術：非整數倍的轉換一定要丟幀或重取樣",
        scope="後期時間線",
        limits="這是工序建議。它避免的是**一類已知的技術問題**，"
               "不是對成品好不好看的主張。",
        policy=GUIDE,
    ),
    Claim(
        id="fps.retime_audio",
        text="把素材 retime 到別的幀率時，聲音也要一起處理，否則會失去同步。",
        evidence_kind=AUTHOR_RECOMMENDATION,
        source="retime 的定義",
        scope="任何非原生幀率的收尾",
        policy=WARN,
    ),
    Claim(
        id="workflow.fix_stills_first",
        text="先把關鍵幀修好再生成影片。",
        evidence_kind=AUTHOR_RECOMMENDATION,
        source="成本與可逆性：重生成一張圖比重生成一段影片便宜得多",
        scope="關鍵幀驅動的流程",
        limits="理由是成本，不是「這樣比較好看」。",
        policy=GUIDE,
    ),
    Claim(
        id="workflow.colour_match",
        text="同一場景的鏡頭之間，色溫與對比不一致會很明顯。",
        evidence_kind=HYPOTHESIS,
        source="剪輯的一般經驗，本專案未驗證",
        scope="後期",
        limits="先前寫成「這是 AI 感最大的來源，比補幀還明顯」——"
               "那個排序沒有任何依據。",
        policy=INFO,
    ),
)

BY_ID: dict[str, Claim] = {c.id: c for c in CLAIMS}


def get(claim_id: str) -> Claim | None:
    return BY_ID.get(claim_id)


def public() -> dict:
    return {
        "claims": [c.public() for c in CLAIMS],
        "evidence": EVIDENCE_ZH,
        "counts": {k: sum(1 for c in CLAIMS if c.evidence_kind == k)
                   for k in EVIDENCE_KINDS},
    }

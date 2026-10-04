# Task 09 — Voice and performance audit

You are GPT, the senior architect and QA reviewer for novel-lab's holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This audit covers the voice layer only: each member's voice fields on the card and her ElevenLabs v4
performance sheet. Run sequentially; do not launch parallel GPT audits.

Group: Secret Society holoX (5 members)

## Binding rules

- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.
- **Author decision 2026-10-04 (dialogue language):** hololive JP members, holoX included, speak **Japanese** in audio
  scripts. Spoken turns are written in Japanese script (kana/kanji); romaji and English glosses go only on the
  non-spoken `ROMAJI ::` / `GLOSS ::` lines (docs/scene-script-format.md). The sheets below still show romanized
  lines from before this decision; Claude converts them after this audit. When you propose a line, give its exact
  Japanese-script wording first, then the romaji.
- **Author decision 2026-10-04 (secondary-only lines, option B):** spoken lines resting only on a secondary
  transcription may stay in the exported fields when they carry their secondary label (research/qa/quote-inventory.md).
  Do not raise a labelled one as P0; do flag any that is exported without its label.

The project's purpose is dialogue for AI voice performance: a writer drafts scenes in Sudowrite from the
cards, and an ElevenLabs v4 voice that is **original** (designed, never cloned or imitating the member) speaks
each character's lines with inline audio tags. The voice fields and sheets must make that work well and stay
inside scope.

Never read projects/*/runs/. Do not modify files. Return the complete audit in your final response.
The factual baseline is 2026-09-30.

## What to check, per member

1. **Quotations.** Every spoken line quoted on the card's voice fields or in the sheet (tag palette, example
   block) must be an official written line, a labelled **Style demo** (original line written in her
   manner), or an ASR span both models share (same audio window, contiguous, no stitched pieces, no added
   words). Spoken quotations require the two-model shared-span gate; a secondary transcription supplies only a
   candidate for Claude's audio check and must stay labelled as such until checked. The audio report for each member is in
   `projects/holoen/research/audio-check/` (its table marks shared spans; Japanese rows count the same kana
   reading as shared). An example line that joins two separately timed moments is a stitch. Mechanical span
   checking (`tools/span_check.py`) reports 0 quotes outside a shared span, but it only checks quotes that
   overlap a report row, so short or unmatched quotes can escape it; judge what it cannot: attribution, labels,
   speaker, context and whether a quote is used for what it shows.
2. **Original-voice design.** The Voice Design prompt and Voice & Delivery describe an original voice. No
   cloning or "sound like her" direction; no measured pitch (Hz), F0 or speaking-rate figure used as a target;
   laugh, timbre and accent descriptions are either sourced (label) or explicitly provisional. Accents are
   voice features only; no regional accent is assigned without an in-scope listening check.
3. **Tags.** Tags are performance directions ElevenLabs v4 can act on (emotion, delivery, nonverbal sounds).
   A tag plus a written word is a spoken interjection; a tag alone is a nonverbal sound and is not also
   spelled out. Partner tags are proposed scene directions, not observed defaults. Flag tags that select
   voices, describe camera or narration, or ask for imitation.
4. **Settings.** Stability/similarity percentages equal the API fractions; settings v4 does not have (for
   example a speed slider) are not claimed. Each sheet's choices are labelled as starting points.
5. **Pronunciation.** Reading guides are provisional and untested (kana for Japanese names; no IPA asserted
   as tested). Names are spelled as on the card.
6. **Consistency.** The sheet agrees with the card's voice fields (greeting, signature sounds, defaults,
   "not as default" list); recency: present-day defaults use recent eligible evidence, alumni use their last
   active period; affiliates and graduates are not described as currently streaming.
7. **Usability.** Would a writer and a voice director get a distinct, playable voice from this? Flag vague or
   generic directions only when a concrete, sourced or clearly provisional replacement exists. Do not add
   enrichment to fill a quota.
8. **Scope.** No private life (health, family, home, sleep, routine, trips, romance, nationality, mother tongue,
   audition history, breaks), no explicit sexual content, no lyrics.

## Evidence

Classify evidence as OFFICIAL, PRIMARY, ARCHIVE_METADATA, SECONDARY or ASR (as in the cohort audits). Fan
transcription cannot establish exact spoken words. ASR agreement is not human listening and does not establish
tone, timbre or recurrence. Keep quotations short; no lyrics. Use live search only where a claim looks wrong
and the files cannot settle it (official pages first).

## Exact output format

Use exactly these four top-level headings:

## Coverage

Members and files examined; which audio reports you opened; what you could not check.

## Findings

| ID | Priority | Member | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|

IDs: VOICE-V4-NNN. Priorities: P0 (scope breach, cloning direction, unapproved spoken quotation,
false setting), P1 (material voice or consistency defect), P2 (optional clarity). File is either
`C/<stem> › <field>` for a card field or `S/<stem>` for the sheet `export/elevenlabs/<stem>.md`. Copy the exact
old text; use DELETE for deletion; escape table pipes and use <br> for newlines. If none, say "None."

## Sheet attestations

| Member | Sheet verdict | Card voice fields verdict | Notes |
|---|---|---|---|

Verdicts: OK; OK after the listed findings; Needs rework (say why). One row per member in the group.

## Merge handoff

Dependencies, propagation order, and up to five open questions for the author ("None" if none).

## Run budget (Claude, 2026-10-02)

One audit must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation.
- **Inputs are inline below**: each member's voice fields (from the bible) and her full sheet, plus the shared
  Style block and the project's ElevenLabs guide. Do not re-open them.
- Open audio reports only to settle a quotation question; batch lookups (`grep -n -e A -e B file1 file2`).
- About 12 tool calls in total, at most 4 live web searches.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git).
- If the budget runs short, stop and list the unchecked items in Coverage. A complete audit with disclosed
  limits beats a lost one.

## Shared inputs

### export/elevenlabs/sudowrite-style.md (the Style block every scene uses)

# Sudowrite Style: audio-ready dialogue (ElevenLabs v4)

Paste the block below into Sudowrite's **Story Bible → Style** box (under the project's own style notes,
about 120 words; wording from GPT's 2026-10-01 review, adopted). It tells Sudowrite to write ElevenLabs v4 tags into every line of dialogue, using
each character's **Audio Tags** trait (exported as the `Audio Tags` column of `characters.csv`).

```text
Write dialogue for original designed voices, never to reproduce a member's identifiable voice. Place one to three brief square-bracket performance directions inside each spoken turn, before the words affected, using the speaker's Audio Tags trait. Change delivery only when the scene warrants it. Preserve her established fillers, restarts, repetitions, code-switching and swears without forcing a quota. Distinguish spoken interjections ([startled squawk] GWAK!) from nonverbal sounds ([laughs]); never render the same sound twice. Use punctuation for pauses and interruptions, CAPS sparingly for stress. Keep narration untagged. Tags and pronunciation guides are provisional until tested with the chosen voice. Characters may share a register; distinguish them by phrasing and comic timing.
```

## Notes
- Tags are performance directions for an **original** designed voice. Do not clone or imitate any member's
  real voice (ElevenLabs Use Policy §5; COVER Derivative Works Guidelines).
- Before sending to ElevenLabs, split narration (narrator voice) from dialogue (one voice per character),
  and keep each Text to Dialogue request under about 2,000 characters.
- If Sudowrite overuses tags, lower it to "one or two tags" in the Style text; if it drifts to generic
  tags ([happy], [sad]), add "Use only tags listed in the speaker's Audio Tags trait."
- Guide: `novel-lab/docs/elevenlabs-v4.md`.


### novel-lab/docs/elevenlabs-v4.md (the project's ElevenLabs guide)

# 交接到 ElevenLabs Eleven v4：讓 AI「演得像她」（2026-09-30）

目標：Sudowrite 寫好的故事，交給 ElevenLabs 的 **Eleven v4** 朗讀時，除了音色，還要有她本人的口吻、
習慣和抑揚頓挫。本文整理官方文件查到的做法，和這個專案的角色檔案怎麼接過去。
每張角色的具體表演表在 `projects/holoen/export/elevenlabs/`。

## 先講清楚：聲音本身不能用她本人的

- **ElevenLabs 使用政策**禁止「在沒有同意或合法權利的情況下，刻意複製他人的聲音」
  （"intentionally replicate the voice of another person: without consent or legal right"），
  也禁止用來性化或誤導他人。[ElevenLabs Use Policy §5](https://elevenlabs.io/use-policy)
- **COVER（hololive）**的二次創作規範明文：「不允許從旗下藝人的歌曲擷取聲音用於語音生成，也不視為二次創作。」
  （"we do not allow extraction of our talents' voices from our songs to be used in speech generation"）
  [Derivative Works Guidelines](https://hololivepro.com/en/terms/)。直播音訊雖然沒被逐字點名，
  但同一份規範也禁止「嚴重損害藝人形象」的內容，而 ElevenLabs 那條已經足以擋下。
- 所以：**不要用她們的直播或歌聲做 Instant／Professional Voice Clone，也不要刻意做「聽起來就是她」的仿聲。**
  這也是這個專案「不碰背後真人」的延伸。

好消息：你要的「口吻、習慣、抑揚頓挫」大部分**不在音色裡，而在文字和表演指示裡**，v4 正好最擅長這個。
做法是：用 Voice Design 做一個**原創聲音**，只取她的「音域和能量」（例如 Calli＝低的女中音、講話快），
然後把她的說話習慣全部寫進腳本和標籤。

## Eleven v4 能用的控制項（官方）

來源：[Eleven v4 文件](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)、
[What is Eleven v4](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v4)、
[Best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)、
[v4 發表文](https://elevenlabs.io/blog/eleven-v4)、[TechCrunch 2026-09-28](https://techcrunch.com/2026/09/28/elevenlabs-new-v4-speech-model-supports-more-expression-control-and-90-languages/)。

| 控制項 | v4 的狀況 | 怎麼用在角色身上 |
|---|---|---|
| **行內標籤** `[...]` | 主要控制方式；可以**疊加**（`[casual] [under his breath]`），模型會照順序做；可以寫**自然語言指示**（`[said angrily in French accent]`、`[lower, thoughtful]`）；比 v3 更聽話，但官方說「not perfect yet」 | 每個角色一組標籤詞彙（見表演表） |
| **上下文** | v4 會讀整段的語氣、節奏和情境，對話中「會回應剛說的話」；長篇接續比 v3 穩 | 一次給完整的一段對話，不要一句一句單獨生成 |
| **標點** | 刪節號＝停頓與重量；全大寫＝加重；破折號＝短停頓／打斷；換行影響節奏 | 用來做 Ina 的慢、Kiara 的 "WAIT. WAIT." |
| **Stability** | 越低越有表現力、每次不同；越高越接近固定基準 | 活潑角色調低，冷靜角色調高（起始值見表演表） |
| **Similarity** | 越高越貼近參考聲音，但可能犧牲自然度 | 原創聲音約 75 起試 |
| Style／Speed 滑桿 | **v4 沒有** | 語速只能靠聲音本身（Voice Design 寫 pace）和標籤（`[rushed]`、`[slowly]`） |
| SSML `<break>` | **不支援** | 用 `[pause]`、`[long pause]`、刪節號、破折號 |
| 發音 | 支援行內 IPA：`/ˈaɪɹɪs/`（要有重音符號），效果因聲音而異 | 名字與專有名詞（見表演表） |
| 多語言 | 90+ 語言，日語品質提升最多；同語言保留原口音，**跨語言會變成母語口音** | Kiara 的德語、各人的日語片語；想保留口音就加標籤試 |
| Text to Dialogue | v4 支援多角色；每一輪有自己的 voice_id；每次請求建議**全部 2,000 字元以內**；用標點表現打斷 | 同一場景的多人對話 |
| 聲音品質 | 聲音的訓練資料裡有的表演最容易做出來；v4 也能做沒訓練過的（耳語、大叫） | 設計聲音時就把「會笑、會大叫」寫進描述 |

模型 ID：`eleven_v4`（品質）、`eleven_v4_turbo`（低延遲，給即時對話用）。

## 專案資料怎麼對應過去

| 角色檔案裡的東西 | 放到 ElevenLabs 的哪裡 |
|---|---|
| 實測音高／語速（[ASR] 量測）、Voice & Delivery | **Voice Design 描述**（原創聲音的音域、能量、語速） |
| Dialogue Style、Catchphrases、口頭禪、填充詞 | **腳本文字本身**：v4 會照字演，所以「like, like」、重來、"okay okay okay" 要寫在字裡 |
| Tone Shifts（情境→語調） | **標籤**：每種情境對應一組標籤 |
| 笑聲、驚叫、招牌聲音（GWAK、Kikkeriki） | **標籤＋擬聲字**，例如 `[startled squawk] GWAK!` |
| 名字、日語、德語 | **IPA** 或拼音式寫法；日語片語直接寫 |
| Sounds off（不像她的東西） | **不要用的標籤**（例如給 Kronii 用 `[giggles]`） |

## 工作流程（建議）

1. **做聲音**：每個角色在 Voice Design 用表演表的描述做一個原創聲音，選最符合「音域和能量」的那個；
   存成 `holoen-<名字>`。旁白另外做一個中性聲音。
2. **寫故事**：在 Sudowrite 正常寫。角色卡的 Dialogue Style 已經要求她們的口頭禪和說話習慣。
3. **轉成朗讀腳本**（這一步最關鍵）。作者定案（2026-10-01）：**由 Sudowrite 在寫故事時直接加標籤**。
   做法：角色卡有一個 **Audio Tags** 欄位（每個角色的基準聲音、情境→標籤、招牌聲音、要寫進字裡的習慣、
   IPA、禁用標籤），匯出在 `characters.csv` 的 `Audio Tags` 欄；Story Bible 的 Style 貼上
   `projects/holoen/export/elevenlabs/sudowrite-style.md` 那段規則。Sudowrite 就會在每句對白前加標籤。
   人工或 Claude 再檢查一次時，照下面的原則：
   - 每句台詞前加上該角色、該情境的標籤（查表演表的 Tone Shifts 對照）；
   - 保留、甚至補強她的習慣：重複、自我打斷、填充詞、停頓；
   - 招牌聲音寫成標籤＋擬聲字；專有名詞加 IPA；
   - 旁白和台詞分開。
   Sudowrite 加得不好的地方，可以請 Claude 依表演表修。
4. **生成**：多人場景用 Text to Dialogue（每次 2,000 字元以內），單人長段用 Text to Speech 或 Studio；
   同一場景盡量一次生成，讓 v4 讀到上下文。每段生成幾個版本挑最好的；需要一致時用 seed。
5. **聽了再調**：太平淡→Stability 往下調、標籤寫得更具體（例如 `[deadpan, flat, a beat before the punchline]`）；
   太誇張或不像同一個人→Stability 往上調、減少標籤。

## 做不到或要注意的地方

- **音色不會是她本人**：這是規範，不是技術問題。像不像，靠的是節奏、習慣、用詞和情緒轉換。
- 標籤不是百分之百聽話（官方：not perfect yet）；同一句多試幾次。
- v4 沒有語速滑桿：慢的角色（Ina）要靠聲音設計＋`[unhurried]`＋刪節號；快的角色（Calli、Kiara）靠 `[rapid]`、少停頓。
- 跨語言時口音會變成母語口音：Calli 講日語可能太標準；需要「美國人講日語」的感覺就加標籤試。
- 粗口與挑逗台詞：ElevenLabs 政策禁止用來性化真人；本專案卡片上的內容已經是非露骨的公開梗，
  但朗讀時仍不要做成針對真人的性內容。

## 參考
- ElevenLabs：[Eleven v4 文件](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)、
  [Best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)、
  [Text to Dialogue](https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue)、
  [Voice Design v3 部落格](https://elevenlabs.io/blog/voice-design-v3)、[Use Policy](https://elevenlabs.io/use-policy)
- COVER：[Derivative Works Guidelines](https://hololivepro.com/en/terms/)
- 查核日：2026-09-30（v4 在 2026-09-28 發布，文件可能還會更新）


## Member: La+ Darknesss (`Laplus-Darknesss`)

### Card voice fields (bible)

**Name:** La+ Darknesss
**Dialogue Style:** Streams in Japanese. Her persona voice is a pint-sized villain: "wagahai" for "I," "kisama" for "you," and grand declarations such as her official introduction 「貴様ら、刮目せよ！！」 ("Kisama-ra, katsumoku seyo!!," officially "See me, hear me, all of you!"), which her followers answer with "Yes My Dark!" In everyday 2026 chats she talks casually, with plain "watashi," "maji de," "yabai" and "~ssho" (「聞こえたっしょ」, "you heard it, right?"), and shows off (「これが配信者よ」, "this is what a streamer is!"). Indignant protests when teased or beaten and a smug cackle on a win are provisional performance choices for suitable scenes. When a story renders her speech in English or Chinese, keep the archaic villain "I" (in Chinese, 吾輩) for persona moments against a small, indignant voice.
**Catchphrases:** 「貴様ら、刮目せよ！！」 ("Kisama-ra, katsumoku seyo!!"; official introduction, officially "See me, hear me, all of you!"); "Yes My Dark!" (her followers' answer); "wagahai" (her persona "I"); "kisama" ("you"); 「吾輩怪しい者でないぞ」 ("Wagahai ayashii mono de nai zo," "I'm not a suspicious person!," attributed to her first post by secondary records); 「これが配信者よ」 ("this is what a streamer is!," shared ASR span). Secondary transcription of her full title: "Laplus Dia Highest Death Thirteen Daina Art of Impact Sign Emperor Road of the Darknesss." Her fans are the Plusmate (+mate).
**Voice & Delivery:** Provisional direction for an original designed voice: a small, bright, bratty voice that puffs itself up into a grand villain register for persona moments and drops to casual chat between them; indignant protests when teased or beaten and a smug cackle on a win are provisional choices for suitable scenes. Not as default: truly menacing, sleepy or mature-cool.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): small, bright voice; cocky by default. Default tags: [smug, bright]. By situation: grand declaration [commanding, theatrical]; showing off [smug, bright]; checking with chat [casual]; treated like a child [indignant, loud]; losing [whining, furious]; scheming [conspiratorial]; winning [cackles]. With people (proposed scene directions, not observed conversational defaults): Lui [whiny, dependent]; Kiara [competitive, friendly]; seniors [indignant]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; laughs are provisional choices): [cackles] (tag only). "Yes My Dark!" is her followers' answer, not her line. Keep in the words: "wagahai," "kisama," "katsumoku seyo." Reading guide (untested): らぷらす だーくねす; わがはい; かつもくせよ. Not as default: a truly menacing demon; a sleepy or mature-cool voice.

### Sheet: export/elevenlabs/Laplus-Darknesss.md

# ElevenLabs v4 Performance Sheet: La+ Darknesss

> Built from `bible/characters/Laplus-Darknesss.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). La+ is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, bright, bratty voice that puffs itself up into a grand villain register and cracks into a loud whine when teased or beaten; quick and cocky when winning, with a smug cackle."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (grand, then whiny; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[smug, bright]` or `[commanding, theatrical]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Wagahai" is persona vocabulary; the two sampled 2026 windows contain "watashi" and no detected "wagahai" (two windows cannot set a frequency).
- Casual and slangy in chat: "maji de," "yabai," "~ssho" (「聞こえたっしょ」, "you heard that, right?").
- Her followers answer her call with "Yes My Dark!"; it is their line, not hers.
- Indignant protests when teased and a whine when she loses are provisional choices for suitable scenes.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[commanding, theatrical]` | 「貴様ら、刮目せよ！！」 ("Kisama-ra, katsumoku seyo!!"; official introduction, officially "See me, hear me, all of you!") |
| Showing off | `[smug, bright]` | 「これが配信者よ」 ("Kore ga haishinsha yo," "this is what a streamer is!") |
| Checking with chat | `[casual]` | 「聞こえたっしょ」 ("Kikoeta ssho," "you heard that, right?") |
| Treated like a child | `[indignant, loud]` | **Style demo:** "Wagahai wa kodomo ja nai!" ("I am not a child!") |
| Losing a game | `[whining, furious]` | **Style demo:** "Kisama~!" ("You~!") |

With people (proposed scene directions, not observed conversational defaults): Lui `[whiny, dependent]`; Kiara `[competitive, friendly]`; seniors `[indignant]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[cackles]` (tag only; a provisional choice)
- "Yes My Dark!" belongs to her followers; do not give it to her as a signature line

## 6. Pronunciation (provisional; test)
- Reading guide (untested): らぷらす だーくねす; わがはい; きさま; かつもくせよ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A truly menacing demon; a sleepy or mature-cool voice.

## 8. Example
```
[commanding, theatrical] Kisama-ra, katsumoku seyo!!
[smug, bright] Kore ga haishinsha yo!
[indignant, loud] Wagahai wa kodomo ja nai!
[casual] Kikoeta ssho?
```
(Line 1 is her official Japanese introduction; lines 2 and 4 are her lines, quoted only where both transcripts
agree; line 3 is a style demo.)


## Member: Takane Lui (`Takane-Lui`)

### Card voice fields (bible)

**Name:** Takane Lui
**Dialogue Style:** Streams in Japanese, calm and conversational: "mā," "ne," "un un," reading chat aloud and answering it one by one, unhurried and warm. Her official phrases open with 「まったかね～？」 ("Mattakane?," officially "Did I Luive you waiting!?") and close with 「おつルイルイ」 ("Otsuluilui," "I take your Luive"); doubts come out as 「○○したかね？」 ("…shitakane?"), excitement as 「鷹まってきた～！」 ("Takamattekita!"). Her greetings and jokes play on her name. She delivers a cool executive line, then adds a clipped 「コッ☆」, and laughs ﾊｯﾊｰ↑ ("Haha↑") after her own joke. When a story renders her speech in English or Chinese, keep the big-sister calm, the wordplay on her name and the cool-then-goofy turn.
**Catchphrases:** 「まったかね～？」 ("Mattakane?"; official English "Did I Luive you waiting!?"); 「おつルイルイ」 ("Otsuluilui"; "I take your Luive"); 「○○したかね？」 ("…shitakane?"; "Did you…, if I'm not mistakane?"); 「鷹まってきた～！」 ("Takamattekita!"; "Hype Luivels rising!"); 「コッ☆」 ("Ko!☆," the clipped sparkle after a cool line); ﾊｯﾊｰ↑ ("Haha↑," her official laugh after a joke); "PON" (the meme for her blunders); "Don't drop your water" (what fans tell her). Her fans are the Lui-tomo.
**Voice & Delivery:** Provisional direction for an original designed voice: a low, calm, mature voice with a warm big-sister softness; unhurried and conversational; a cool executive line for effect, undone by a cute, clipped "Ko!☆"; a pleased "Haha↑" after her own joke (official phrase); flustered laughter after a blunder and shrieks in horror games are provisional choices. Not as default: a high, bubbly voice.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): low, calm, mature voice; warm by default. Default tags: [calm, warm]. By situation: opening [warm, lilting]; executive mode [cool, low] then [playful] on "Ko!☆"; chatting [calm, motherly]; a joke [deadpan] then "Haha↑"; a blunder [flustered] then [laughs]; horror game [panicked, shrieking]; horse-race prediction [confident]. With people (proposed scene directions, not observed conversational defaults): La+ [exasperated, fond]; Kiara [bright, friendly]; Mumei [gentle, sisterly]; Okayu [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; laughs and screams are provisional choices): "Ko!☆" (spoken, clipped); "Haha↑" (spoken, official phrase); [laughs] (tag only); [screams] (tag only). Keep in the words: "Mattakane," "Otsuluilui," "Lui-tomo." Reading guide (untested): たかね るい; まったかね; こっ☆ (clipped). Not as default: a high, bubbly voice; cold cruelty; nonstop shouting.

### Sheet: export/elevenlabs/Takane-Lui.md

# ElevenLabs v4 Performance Sheet: Takane Lui

> Built from `bible/characters/Takane-Lui.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lui is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, low, calm, mature voice with a warm big-sister softness; unhurried and conversational; a cool executive tone for effect, undone by a cute, clipped sparkle; a pleased little laugh after her own joke."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **55%** (API `0.55`) (calm and warm by default; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[calm, warm]` or `[cool, low]`; v4 has no speed slider.

## 3. Write these habits into the script
- 「まったかね～？」 ("Mattakane?") to open and 「おつルイルイ」 ("Otsuluilui") to close; wordplay on her name.
- Calm, motherly chat: 「まあ誰にだってトラブルやミスはあるからね」 ("well, everyone has trouble and mistakes").
- Executive mode, then a clipped 「コッ☆」 ("Ko!☆").
- Laughs ﾊｯﾊｰ↑ ("Haha↑") after her own joke (official phrase); "PON" is the fans' meme for her blunders, not a line she must say.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, lilting]` | 「まったかね～？」 ("Mattakane?"; official) |
| Executive mode | `[cool, low] → [playful]` | **Style demo:** "Kore wa kanbu no shigoto yo. …Ko!☆" ("This is an executive's job. …Sparkle!") |
| Chatting | `[calm, motherly]` | 「まあ誰にだってトラブルやミスはあるからね」 ("Mā dare ni datte toraburu ya misu wa aru kara ne") |
| A joke lands | `[pleased]` | ﾊｯﾊｰ↑ ("Haha↑," official phrase) |
| A blunder | `[flustered] → [laughs]` | **Style demo:** "A, yatchatta…" ("Oops…") |
| Horror game | `[panicked, shrieking]` | **Style demo:** "Muri muri muri!" ("No way, no way!") |
| Closing | `[gentle]` | 「おつルイルイ」 ("Otsuluilui"; official) |

With people (proposed scene directions, not observed conversational defaults): La+ `[exasperated, fond]`; Kiara `[bright, friendly]`; Mumei `[gentle, sisterly]`; Okayu `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ko!☆" (spoken, clipped)
- "Haha↑" (spoken, official phrase)
- `[laughs]` (tag only); `[screams]` (tag only); provisional choices

## 6. Pronunciation (provisional; test)
- Reading guide (untested): たかね るい; まったかね; おつるいるい; こっ☆ (clipped). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A high, bubbly default; cold cruelty; nonstop shouting.

## 8. Example
```
[warm, lilting] Mattakane?
[calm, motherly] Mā, dare ni datte toraburu ya misu wa aru kara ne.
[cool, low] Kore wa kanbu no shigoto yo. [playful] …Ko!☆
[gentle] Otsuluilui.
```
(Lines 1 and 4 are her official greeting and sign-off; line 2 is her line, quoted only where both transcripts
agree; line 3 is a style demo.)


## Member: Hakui Koyori (`Hakui-Koyori`)

### Card voice fields (bible)

**Name:** Hakui Koyori
**Dialogue Style:** Streams in Japanese with a presenter's polish: 「こんこよ～！」 to open, crisp segment transitions on her news show (「それでは続いてはこちら」, "and next up"), 「助手くん」 (assistants) for her audience and 「こよりちゃん」 for herself. She invites viewers to look at things with a warm 「ぜひぜひ見てみてください」 ("please do take a look"). She teases members under the cover of "research" and screams when scared; for the original designed voice, excited explanations may speed up and rise in pitch (a provisional direction). When a story renders her speech in English or Chinese, keep the bright anchor manner, the lab vocabulary and the sudden screams.
**Catchphrases:** 「こんこよ～！」 ("Konkoyo~!"; official greeting, officially "Ayo, this is Koyo!"); "The brain of holoX! My name is Koyori Hakui!" (official English); 「コヨリニウム」 ("koyoriniumu," officially "Koyorium," the nutrient from watching her); 「冷こよ」 ("Reikoyo," a cool Koyori); 「こよ色」 ("Koyo-iro," pink); 「助手くん」 ("joshu-kun," her Assistants); on AsaKoyo, 「それでは続いてはこちら」 ("and next up," shared ASR span); 「こよりちゃんでございます」 ("it's Koyori-chan," shared ASR span).
**Voice & Delivery:** Provisional direction for an original designed voice: a bright, clear, well-enunciated voice in presenter mode, quick and cheerful; excited explanations may accelerate and rise; squeals when excited and full screams when scared; sly and playful when teasing. Her recorded giggle is a first-model observation, so laughs are provisional choices. Not as default: flat, sleepy, mumbled or coldly scientific.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, clear mid-high voice with a wide upward range. Default tags: [cheerful, crisp]. By situation: hosting [upbeat, announcer]; inviting viewers [warm, upbeat]; excited explanation [excited, fast]; horror or a scare [screams]; teasing a member [playful, sly]; proud of an "experiment" [smug]; thanking her Assistants [warm]. With people (proposed scene directions, not observed conversational defaults): Chloe [bickering, fond]; Marine [giddy]; FUWAMOCO [bubbly]; La+ [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; giggles and screams are provisional choices): "Konkoyo!" (spoken); [giggles] (tag only); [screams] (tag only). Keep in the words: "Konkoyo," "joshu-kun," "koyoriniumu." Reading guide (untested): はくい こより; こんこよ; こよりにうむ. Not as default: a flat, sleepy or coldly scientific voice.

### Sheet: export/elevenlabs/Hakui-Koyori.md

# ElevenLabs v4 Performance Sheet: Hakui Koyori

> Built from `bible/characters/Hakui-Koyori.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Koyori is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, clear, well-enunciated mid-high voice in presenter mode; quick and cheerful, leaping upward into squeals when excited and full screams when scared; sly and playful when teasing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (wide swings from presenter calm to squeals; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, crisp]` or `[excited, fast]`; v4 has no speed slider.

## 3. Write these habits into the script
- 「こんこよ～！」 ("Konkoyo~!") to open; 「助手くん」 ("joshu-kun," assistants) for her viewers; 「こよりちゃん」 for herself.
- Crisp segment transitions on her news show: 「それでは続いてはこちら」 ("and next up").
- Invites viewers warmly: 「ぜひぜひ見てみてください」 ("please do take a look").
- Excited explanations may speed up and rise (a provisional direction); experiments and 「コヨリニウム」 ("koyoriniumu") are running jokes.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, cheerful]` | 「こんこよ～！」 ("Konkoyo~!"; official) |
| Hosting | `[upbeat, announcer]` | 「それでは続いてはこちら」 ("Sore de wa tsuzuite wa kochira," "and next up") |
| Inviting viewers | `[warm, upbeat]` | 「ぜひぜひ見てみてください」 ("Zehi zehi mite mite kudasai," "please do take a look") |
| Teasing a member | `[playful, sly]` | **Style demo:** "Kore mo kenkyū no tame dakara ne?" ("It's all for research, okay?") |
| Proud of an experiment | `[smug]` | **Style demo:** "Fufun, kanpeki na jikken kekka!" ("Heh, perfect results!") |
| A scare | `[screams]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Chloe `[bickering, fond]`; Marine `[giddy]`; FUWAMOCO `[bubbly]`; La+ `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Konkoyo!" (spoken)
- `[giggles]` (tag only; the recorded giggle is a first-model observation, so this is a provisional choice); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): はくい こより; こんこよ; じょしゅくん; こよりにうむ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A flat, sleepy, mumbled or coldly scientific voice.

## 8. Example
```
[bright, cheerful] Konkoyo!
[upbeat, announcer] Sore de wa tsuzuite wa kochira.
[warm, upbeat] Zehi zehi mite mite kudasai!
[playful, sly] Kore mo kenkyū no tame dakara ne?
```
(Line 1 is her official greeting; lines 2 and 3 are her lines, quoted only where both transcripts agree; line 4 is a
style demo.)


## Member: Sakamata Chloe (`Sakamata-Chloe`)

### Card voice fields (bible)

**Name:** Sakamata Chloe
**Dialogue Style:** Streamed in Japanese in connected, run-on chatter whose sentences often trail into a drawn-out "~sā" (transcript observation), calling herself "Sakamata" and her viewers 「飼育員」 ("shiikuin," Handlers). She opens like a meal (「いただきまーす」), teases seniors and friends, and turns questions into polls of chat (「いつからおじさんなの」). When a story renders her speech in English or Chinese, keep the third-person "Sakamata," the teasing, giggly chatter and the switch to a serious, mature voice when she sings.
**Catchphrases:** 「ばっくばっくばく～ん」 ("bakku bakku bakūn," official opening) followed by 「いただきます」 ("itadakimasu"; officially "Chomp, chomp, chomp! It's time to eat!"); 「ごちそうさまでした」 ("gochisōsama deshita," official closing, "Thanks for the food"); 「いただきまーす」 (shared ASR span); 「飼育員」 ("shiikuin," Handlers, her viewers); "Sakamata" (how she refers to herself); "KoyoChlo" (her duo with Koyori).
**Voice & Delivery:** Provisional direction for an original designed voice: a small, soft, high and slightly airy voice that chatters, giggles and teases; panicky squeaks in horror; noticeably deeper, fuller and more mature when she sings. Speed, softness and timbre are provisional choices: ASR records connected chatter, not how it sounds. Not as default: a cool, mature speaking voice, a menacing "cleaner" or slow, careful speech.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): small, soft, high voice; quick and playful by default. Default tags: [soft, playful]. By situation: opening [bright, hungry]; chatting [fast, casual]; polling chat [curious, playful]; teasing [mischievous, giggly]; horror [panicked, squeaky]; singing [mature, heartfelt]. With people (proposed scene directions, not observed conversational defaults): Koyori [bickering, fond]; Lui [whiny, sheepish]; Kiara [shy, excited]; seniors [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; giggles are provisional choices): "Bakku bakku bakūn" (spoken); [giggles] (tag only); [gasps] (tag only). Keep in the words: "Sakamata," "shiikuin," "itadakimāsu." Reading guide (untested): さかまた くろえ; ばっくばっくばくーん. Not as default: a cool, mature or menacing voice.

### Sheet: export/elevenlabs/Sakamata-Chloe.md

# ElevenLabs v4 Performance Sheet: Sakamata Chloe

> Built from `bible/characters/Sakamata-Chloe.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Chloe concluded her regular activities on 2025-01-26 and remains a hololive affiliate; the sheet covers her 2021–2025 persona. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, soft, high and slightly airy voice that chatters, giggles and teases; panicky squeaks in horror; a fuller, more mature tone when singing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (quick and playful; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[soft, playful]` or `[fast, casual]`; v4 has no speed slider.

## 3. Write these habits into the script
- Opens like a meal: 「ばっくばっくばく～ん」 ("bakku bakku bakūn," official) then 「いただきます」; on stream, 「いただきまーす」 ("itadakimāsu!").
- Calls herself "Sakamata"; connected, run-on chatter that polls chat (speed and softness are provisional choices).
- Teases seniors and friends; any blame-denying line is a style demo, not a documented habit.
- Closes with 「ごちそうさまでした」 ("gochisōsama deshita," official; "Thanks for the food").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, hungry]` | 「いただきまーす」 ("Itadakimāsu!") |
| Chatting | `[fast, casual]` | 「いつからおじさんなの」 ("Itsu kara ojisan na no," "since when is someone an ojisan?") |
| Teasing a member | `[mischievous, giggly]` | **Style demo:** "Ē~, sore Sakamata no sei ja nai yo?" ("Huh~, that's not Sakamata's fault, is it?") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Closing | `[content]` | 「ごちそうさまでした」 ("Gochisōsama deshita," official) |

With people (proposed scene directions, not observed conversational defaults): Koyori `[bickering, fond]`; Lui `[whiny, sheepish]`; Kiara `[shy, excited]`; seniors `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Bakku bakku bakūn" (spoken, official opening)
- `[giggles]` (tag only); `[gasps]` (tag only); provisional choices

## 6. Pronunciation (provisional; test)
- Reading guide (untested): さかまた くろえ; ばっくばっくばくーん; ごちそうさまでした. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cool, mature or menacing speaking voice; slow, careful speech.

## 8. Example
```
[bright, hungry] Itadakimāsu!
[fast, casual] Itsu kara ojisan na no?
[mischievous, giggly] Ē~, sore Sakamata no sei ja nai yo?
[content] Gochisōsama deshita.
```
(Lines 1–2 are her lines, quoted only where both transcripts agree (line 2 is the shared part of a longer
line); line 3 is a style demo; line 4 is her official closing.)


## Member: Kazama Iroha (`Kazama-Iroha`)

### Card voice fields (bible)

**Name:** Kazama Iroha
**Dialogue Style:** Streams in Japanese in a bright samurai persona: "de gozaru" as her signature ending (uncommon in the two sampled 2026 game windows), "-dono" for friends and "Gozaru" for herself. In games she switches to fast play-by-play with words repeated in fours (「よしよしよしよし」 when it works), gets flustered when things go wrong, talks back at teasing chat and then laughs. When a story renders her speech in English or Chinese, keep occasional samurai flavor without forcing an archaic ending onto every sentence ("I daresay" is the official English localization; in Chinese, 在下 for herself and an occasional sentence-final 是也) against an upbeat, sporty voice.
**Catchphrases:** 「holoXの用心棒、侍の風真いろはでござる」 ("holoX no yōjinbō, samurai no Kazama Iroha de gozaru"; official introduction, officially "Secret Society holoX's insurance policy, Kazama Iroha here, I daresay!"); "de gozaru" (her samurai sentence ending); "-dono" (for friends); 「よしよしよしよし」 ("yoshi yoshi yoshi yoshi," when it works; shared ASR span). Her fans are the Kazama-tai.
**Voice & Delivery:** Provisional direction for an original designed voice: a clear, bright, youthful voice with a sporty edge; earnest and polite in samurai mode, quick, loud and pumped when she competes, laughing easily at her own mistakes (laughs are provisional choices). Not as default: gruff, grim, sultry or slow and solemn.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, clear youthful voice. Default tags: [cheerful, earnest]. By situation: samurai introduction [proud, polite]; competing [excited, fast]; it works [triumphant]; a blunder [laughs, sheepish]; teased by chat [indignant, loud]; guarding holoX [determined]; scared [panicked]. With people (proposed scene directions, not observed conversational defaults): AZKi [relaxed, playful]; La+ [patient, teasing]; Kiara [excited]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; laughs are provisional choices): "de gozaru" (spoken); "yoshi yoshi yoshi yoshi" (spoken); [laughs] (tag only). Keep in the words: "de gozaru," "-dono," "yoshi yoshi." Reading guide (untested): かざま いろは; ござる; ようじんぼう. Not as default: a gruff warrior or a sultry, cool voice.

### Sheet: export/elevenlabs/Kazama-Iroha.md

# ElevenLabs v4 Performance Sheet: Kazama Iroha

> Built from `bible/characters/Kazama-Iroha.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Iroha is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear, bright, youthful voice with a sporty edge; earnest and polite in samurai mode, quick, loud and pumped when competing, laughing easily at her own mistakes."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (earnest by default, pumped when competing; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, earnest]` or `[excited, fast]`; v4 has no speed slider.

## 3. Write these habits into the script
- Calls herself "Kazama" or "Gozaru"; sentence-final "de gozaru" was uncommon in the two sampled 2026 game windows.
- 「よしよしよしよし」 ("all right, all right") when things go well.
- Talks back when chat teases her (her "oi" is a first-model observation, so lines for it are style demos).
- Laughs off her blunders (laughs are provisional choices).

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[proud, polite]` | 「holoXの用心棒、侍の風真いろはでござる」 ("holoX no yōjinbō, samurai no Kazama Iroha de gozaru"; official) |
| Going well | `[excited, fast]` | 「よしよしよしよし」 ("Yoshi yoshi yoshi yoshi") |
| Teased by chat | `[indignant, loud]` | **Style demo:** "Chotto, chat-dono!" ("Hey, chat!") |
| A blunder | `[laughs, sheepish]` | **Style demo:** "Mā, sō iu toki mo aru de gozaru." ("Well, these things happen, I daresay.") |
| Guarding holoX | `[determined]` | **Style demo:** "Koko wa Kazama ni makaseru de gozaru!" ("Leave this to Kazama, I daresay!") |

With people (proposed scene directions, not observed conversational defaults): AZKi `[relaxed, playful]`; La+ `[patient, teasing]`; Kiara `[excited]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "de gozaru" (spoken, as a set piece)
- "yoshi yoshi yoshi yoshi" (spoken)
- `[laughs]` (tag only; a provisional choice)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): かざま いろは; ござる; ようじんぼう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior, a grim or solemn read, or a sultry, cool voice.

## 8. Example
```
[proud, polite] holoX no yōjinbō, samurai no Kazama Iroha de gozaru!
[excited, fast] Yoshi yoshi yoshi yoshi!
[indignant, loud] Chotto, chat-dono!
[laughs, sheepish] Mā, sō iu toki mo aru de gozaru.
```
(Line 1 is her official Japanese introduction; line 2 is her line, quoted only where both transcripts agree;
lines 3–4 are style demos.)



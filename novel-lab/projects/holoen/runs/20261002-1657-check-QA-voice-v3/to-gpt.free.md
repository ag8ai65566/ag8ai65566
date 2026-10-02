# Task 09 — Voice and performance audit

You are GPT, the senior architect and QA reviewer for novel-lab's holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This audit covers the voice layer only: each member's voice fields on the card and her ElevenLabs v4
performance sheet. Run sequentially; do not launch parallel GPT audits.

Group: hololive JP (9 members)

## Binding rules

- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.

The project's purpose is dialogue for AI voice performance: a writer drafts scenes in Sudowrite from the
cards, and an ElevenLabs v4 voice that is **original** (designed, never cloned or imitating the member) speaks
each character's lines with inline audio tags. The voice fields and sheets must make that work well and stay
inside scope.

Never read projects/*/runs/. Do not modify files. Return the complete audit in your final response.
The factual baseline is 2026-09-30.

## What to check, per member

1. **Quotations.** Every spoken line quoted on the card's voice fields or in the sheet (tag palette, example
   block) must be an official written line, a labelled secondary transcription, a labelled **Style demo**
   (original line written in her manner), or an ASR span both models share (same audio window, contiguous,
   no stitched pieces, no added words). The audio report for each member is in
   `projects/holoen/research/audio-check/` (its table marks shared spans; Japanese rows count the same kana
   reading as shared). An example line that joins two separately timed moments is a stitch. Mechanical span
   checking already passes (`tools/span_check.py`: 0 candidates); judge what it cannot: attribution, labels,
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

IDs: VOICE-V3-NNN. Priorities: P0 (scope breach, cloning direction, unapproved spoken quotation,
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


## Member: Hoshimachi Suisei (`Hoshimachi-Suisei`)

### Card voice fields (bible)

**Name:** Hoshimachi Suisei
**Dialogue Style:** Streams in Japanese: quick, fluent and confident, with "nanka," "mā," "ne" and "chotto matte" ("wait a sec"). She talks about herself as "Sui-chan," stretches her signature cute line into a sing-song, reacts with a quick "e?", blames chat in mock innocence when chat talked her into something, throws in a mock-rough Tales of the Abyss quote, and answers age questions with the forever-18 bit. English appears in short phrases (she used English when addressing Calliope at New Underworld Order). Laughter and emotional coloring are provisional choices for the original voice, not documented habits. When a story renders her speech in English or Chinese, keep the third-person "Sui-chan" and the sing-song cuteness on top of a crisp, competitive core.
**Catchphrases:** 「彗星のごとく現れたスターの原石！バーチャルアイドルの星街すいせいでーす！」 ("A shooting star that appeared from diamonds in the rough; I'm the virtual idol Hoshimachi Suisei!", official introduction); 「スイちゃんは〜今日も可愛い〜」 ("Sui-chan wa~ kyō mo kawaii~," "Sui-chan is cute today too~"); 「いやいやいや、私は悪くない」 ("Iya iya iya, watashi wa warukunai," "No, no, no, I'm not the bad one"); 「俺は悪くねぇ」 ("Ore wa warukunē," "It's not my fault," a Tales of the Abyss line); 「スイちゃんは18歳だよ」 ("Sui-chan wa jūhassai da yo," "Sui-chan is eighteen"); "Hi, honey!" (a secondary transcription associated with her Duolingo stream). Her fans are the Hoshiyomi (Stargazers). The English glosses are ours.
**Voice & Delivery:** Provisional direction for an original designed voice: a clear, bright mid-high voice, polished and confident; quick and fluent in chat, sing-song and stretched for her signature cute line, crisp and clipped when she is competing; a bright laugh as a performance choice. Keep the cuteness as a performance on top of a self-assured core; the "psychopath" bit is a joke, never a cold default.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear, bright mid-high voice; quick and confident by default. Default tags: [bright, confident]. By situation: introduction [polished, idol-bright]; signature line [sing-song, playful]; chatting about games [quick, enthusiastic]; caught in a mistake [mock-innocent] then [mock-gruff]; competitive game [focused, clipped]; a social-deduction betrayal [sweet] then [deadpan]; cheering a kouhai [warm]. With people (proposed scene directions, not observed conversational defaults): Calli [gracious, amused]; AZKi [relaxed, teasing]; Miko [playful bickering]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs] (tag only); "e?" (spoken). Keep in the words: "Sui-chan," "kawaii," "chotto matte," "Hi, honey!" Reading guide (untested): ほしまち すいせい; すいちゃん; ほしよみ. Not as default: a breathy or babyish voice; a cold, menacing read; mumbling.

### Sheet: export/elevenlabs/Hoshimachi-Suisei.md

# ElevenLabs v4 Performance Sheet: Hoshimachi Suisei

> Built from `bible/characters/Hoshimachi-Suisei.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Suisei is active at the 2026 baseline. She streams in Japanese; lines below are
> romanized with English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear and bright mid-high voice, polished and confident; quick and fluent
when chatting, sing-song and stretched when she calls herself cute, crisp and clipped when competing."
- A bright laugh is a provisional performance choice, not a listening observation.
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (polished by default, playful swings for the signature line).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[quick, enthusiastic]` or `[focused, clipped]`; v4 has no speed
  slider.

## 3. Write these habits into the script
- Third person for herself: "Sui-chan"; the stretched signature "Sui-chan wa~ kyō mo kawaii~."
- Quick "e?" reactions; "chotto matte" ("wait a sec"); fillers "nanka," "mā," "ne."
- Mock innocence when caught: "Iya iya iya, watashi wa warukunai" … then a mock-rough "Ore wa warukunē."
- Occasional short English ("Hi, honey!", a secondary transcription associated with her Duolingo stream).

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[polished, idol-bright]` | "A shooting star that appeared from diamonds in the rough; I'm the virtual idol Hoshimachi Suisei!" (official) |
| Signature line | `[sing-song, playful]` | "Sui-chan wa~ kyō mo kawaii~" |
| Caught in a mistake | `[mock-innocent]` → `[mock-gruff]` | "Iya iya iya, watashi wa warukunai." … "Ore wa warukunē." |
| Age joke | `[breezy, firm]` | "Sui-chan wa jūhassai da yo." |
| Tales tangent | `[quick, enthusiastic]` | "Kore wa Teiruzu ga daisuki na hanashi desu." |
| Competitive game | `[focused, clipped]` | "Mō ikkai. Kondo wa kateru." (style demo) |

With people (proposed scene directions, not observed conversational defaults): Calli `[gracious, amused]`; AZKi `[relaxed, teasing]`; Miko `[playful bickering]`.

## 5. Signature sounds
- `[laughs]` (tag only); "e?" (spoken).

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ほしまち すいせい; すいちゃん; ほしよみ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A breathy or babyish idol voice; a cold, menacing read (the "psychopath" bit is a joke); mumbling.

## 8. Example
```
[polished, idol-bright] Bācharu aidoru no Hoshimachi Suisei desu!
[sing-song, playful] Sui-chan wa~ kyō mo kawaii~
[mock-innocent] Iya iya iya, watashi wa warukunai.
[breezy, firm] Sui-chan wa jūhassai da yo.
[focused, clipped] Mō ikkai. Kondo wa kateru.
```
(Line 1 is built on her official introduction; line 5 is a style demo; lines 2–4 are her lines, quoted only
where both transcripts agree.)


## Member: AZKi (`AZKi`)

### Card voice fields (bible)

**Name:** AZKi
**Dialogue Style:** Streams in Japanese with a gentle, friendly register, reacting with a drawn-out "e~?" and introducing herself in the third person ("Virtual Diva AZKi, the songstress of the virtual world"). A playful streak runs under the poise: puns, mock-villain flourishes ("Tremble at this word count"), grand retreats in games ("Senryakuteki tettai," "strategic retreat"), "Bottakuri!" ("Rip-off!") at shop prices, 「ゲース！」 in GeoGuessr, "Floor!" or "Ceiling!" when moved, and a flustered "chotto chotto" when chat knows too much. Careful diction and soft giggles are provisional performance choices. When a story renders her speech in English or Chinese, keep the poised diva voice cracking into playfulness.
**Catchphrases:** 「こんあずきー！」 ("Kon-AZKi!", official Japanese greeting); "I'm the Virtual Diva AZKi! I love music and singing!" (official); "This moment is key, this is AZKi!" (official); 「ゲース！」 ("Gēsu!", gloss "Guess!", GeoGuessr); "Yuka!" ("Floor!") and "Tenjō!" ("Ceiling!") for strong emotions (official words); "kono yarō" ("you bastard," a secondary transcription, to Tokino Sora's accidental prank); 「戦略的撤退」 ("Senryakuteki tettai," "Strategic retreat"); "Bottakuri!" ("Rip-off!"); 「この文字数に恐怖するがいい」 ("Tremble at this word count"). Her fans are the Pioneers (Kaitakusha). The English glosses are ours.
**Voice & Delivery:** Provisional direction for an original designed voice: a clear, warm mid-range singer's voice, poised when she presents, lifting into a playful lilt for puns and jokes, quick and focused in a GeoGuessr round with a bright shout on "Gēsu!" Cold or aloof delivery is not the proposed default.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear, warm mid-range voice; poised and friendly by default. Default tags: [warm, clear]. By situation: introduction [poised, diva]; GeoGuessr [focused, quick] then [triumphant] on "Gēsu!"; a pun [playful] then [giggles]; overwhelmed by a moment [overjoyed] ("Floor!"); a prank [mock-indignant]; comforting someone [soft, gentle]; horror game [nervous]. With people (proposed scene directions, not observed conversational defaults): Suisei [relaxed, teasing]; FUWAMOCO [cheerful]; IRyS [friendly]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [giggles] (tag only); "e~?" (spoken). Keep in the words: "Gēsu," "yuka," "tenjō," "Kaitakusha." Reading guide (untested): あずき; かいたくしゃ. Not as default: cold or aloof delivery; constant shouting; a babyish voice.

### Sheet: export/elevenlabs/AZKi.md

# ElevenLabs v4 Performance Sheet: AZKi

> Built from `bible/characters/AZKi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). AZKi is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear and warm mid-range singer's voice; poised
and friendly when she talks, a playful lilt for jokes, a bright shout of triumph when she wins a guessing game."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (poised delivery with occasional bursts; an untested starting choice).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[warm, clear]` or `[focused, quick]`; v4 has no speed slider.

## 3. Write these habits into the script
- A soft "hai" to close a topic; a drawn-out "e~?" when surprised; "chotto chotto" when flustered.
- Grand narration of her own losses: "Senryakuteki tettai" ("strategic retreat").
- 「ゲース！」 ("Gēsu!") when locking in an answer; "Yuka!" / "Tenjō!" ("Floor!" / "Ceiling!") for strong feelings.
- Puns and mock-villain flourishes, then a giggle.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[poised, diva]` | "I'm the Virtual Diva AZKi! I love music and singing!" (official) |
| Chat knows too much | `[mock-flustered]` | "Chotto chotto, naande sonna minna jōhō o motteru no?" |
| Mock villain | `[mock-menacing]` → `[giggles]` | "Kono mojisū ni kyōfu suru ga ii." |
| Losing a fight | `[mock-dignified]` | "Senryakuteki tettai." |
| A shop price | `[indignant, playful]` | "Bottakuri!" |
| Overwhelmed | `[overjoyed]` | "Yuka!" (official word) |

With people (proposed scene directions, not observed conversational defaults): Suisei `[relaxed, teasing]`;
FUWAMOCO `[cheerful]`; IRyS `[friendly]`.

## 5. Signature sounds
- `[giggles]` (tag only); "e~?" (spoken).

## 6. Pronunciation (provisional; test)
- Reading guide (untested): あずき; かいたくしゃ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cold, aloof diva; constant shouting; a babyish voice.

## 8. Example
```
[poised, diva] Bācharu dībā AZKi, kasō sekai no utahime desu.
[mock-flustered] Chotto chotto, naande sonna minna jōhō o motteru no?
[mock-menacing] Kono mojisū ni kyōfu suru ga ii.
[mock-dignified] Senryakuteki tettai.
[overjoyed] Yuka!
```
(Line 5 is her official word; lines 1–4 are her lines, quoted only where both transcripts agree.)


## Member: Nakiri Ayame (`Nakiri-Ayame`)

### Card voice fields (bible)

**Name:** Nakiri Ayame
**Dialogue Style:** Streams in Japanese: chatty and storytelling, with "nanka," "maji de" and "meccha," polite with chat at first and quickly casual (「聞こえておりますでしょうか」, "can you hear me?", opening a 2026 chat). She calls herself "Yo" and her viewers "ningen-sama"; the archaic pronoun does not make her syntax archaic. She scolds teasing chat with a pouting 「うるさい」 ("Urusai!", "Shut up!") … 「困った人たち」 ("you troublesome people"), and in a horror game talks herself down (「落ち着いて落ち着いて」, "calm down, calm down") while 「声が震えちゃう」 ("my voice is shaking"). When a story renders her speech in English or Chinese, keep the royal "Yo" (in Chinese, 余) and the mock-haughty act melting into giggles; the English glosses are ours.
**Catchphrases:** "Greetings, Humans! Yoohoo!" (official profile wording); 「こんなきりー！」 ("Konnakiri!", greeting; secondary transcription); 「余だよ！」 ("Yo da yo!", "It's me!"; secondary transcription); "Yo" (余) for "I"; "ningen-sama" (her viewers); "kawayo" (fans' word for her cuteness, adopted by her official profile); "It's 'Nakiri'!"; "Why don't you humans have horns?" (secondary English transcription). Her fans are the Nakiri-gumi (Nakiri Gang).
**Voice & Delivery:** Provisional direction for an original designed voice: a soft, cute mid-high voice with a playful, mock-haughty edge for the oni act, chatty and unhurried in conversation, dissolving into giggles; quick and focused in an FPS round; shaky and pleading when a horror game scares her. Mock-haughtiness is a performed bit; delivery follows the scene.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, cute mid-high voice; playful by default. Default tags: [playful, warm]. By situation: greeting [bright, playful]; the oni act [mock-haughty]; a bad pun [giggles]; teasing chat [pouting]; FPS clutch [focused, quick]; horror game [scared, shaky]; meeting someone new [shy, careful]. Relationship-specific delivery is not established by the sampled audio; any partner tags are fictional scene directions. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [giggles] (tag only); **Style demo:** "Mō~" (spoken). Keep in the words: "Yo," "ningen-sama," "Konnakiri," "kawayo." Japanese reading: なきり あやめ; こんなきり; 余＝よ. Regional accent and pitch-accent patterns are unverified. Not as default: a cruel or menacing oni; a monotone.

### Sheet: export/elevenlabs/Nakiri-Ayame.md

# ElevenLabs v4 Performance Sheet: Nakiri Ayame

> Built from `bible/characters/Nakiri-Ayame.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Ayame is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft and cute mid-high voice with a playful, mock-haughty edge; chatty and
unhurried, dissolving into quick giggles; shaky and breathless when frightened."
- Giggles are a provisional performance choice (secondary description), not a listening observation.
- This is an original voice-design choice. Mixed-recording F0 and ASR character-rate measurements are
  descriptive research data, not synthesis targets or evidence of the member's isolated vocal range.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (giggles and mood swings). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[playful, warm]` or `[scared, shaky]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Yo" (余) for "I" and "ningen-sama" for her viewers; "Konnakiri!" and "Yo da yo!".
- Polite at first ("Kikoete orimasu deshō ka?"), casual within minutes ("maji de," "meccha").
- Pouting scolds: "Urusai!" … "Komatta hitotachi."
- In horror: "Koe ga furuechau," "Ochitsuite, ochitsuite."

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[bright, playful]` | "Konnakiri!" (secondary transcription) |
| The oni act | `[mock-haughty]` | "Yo da yo!" |
| Opening a stream | `[polite, careful]` | "Kikoete orimasu deshō ka?" |
| Teasing chat | `[pouting]` | "Urusai!" … "Komatta hitotachi." |
| Horror game | `[scared, shaky]` | "Ima odorokasaretara hontō ni shinzō ga tomarisō." |
| FPS clutch | `[focused, quick]` | **Style demo:** "Mikata, ikeru yo!" ("Team, we can do this!") |
| A bad pun | `[giggles]` → `[laughs harder]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Fubuki and Mio `[comfortable, giggly]`;
Okayu `[teasing]`; Kiara `[polite, excited]`.

## 5. Signature sounds
- `[giggles]` (tag only); **Style demo:** "Mō~" (spoken).

## 6. Pronunciation (provisional; test)
- Japanese reading: なきり あやめ; こんなきり; 余＝よ. Regional accent and pitch-accent patterns are unverified.
  Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cruel or menacing oni; a cold, superior read; a monotone.

## 8. Example
```
[polite, careful] Kikoete orimasu deshō ka?
[bright, playful] Konnakiri!
[pouting] Urusai! … Komatta hitotachi.
[scared, shaky] Koe ga furuechau.
[scared, shaky] Ima odorokasaretara hontō ni shinzō ga tomarisō.
```
(Line 2 is her greeting as a secondary transcription; lines 1, 3–5 are her lines, quoted only where both
transcripts agree.)


## Member: Nekomata Okayu (`Nekomata-Okayu`)

### Card voice fields (bible)

**Name:** Nekomata Okayu
**Dialogue Style:** Streams in Japanese in a relaxed, unhurried voice: "boku" for "I," polite "-masu" endings mixed with easygoing ones, long trailing vowels and "hai hai hai." She greets with "Mogu mogu~ Okayu~!" ("Om nom, Okayu!"), calls her fans "Onigiryā" and narrates what she is doing as she plays; in one sampled game opening she proposed going "by vibes" (「ノリで相手をぶっ倒したいと思いまーす」), and she repeats "nya" when a move feels good. Her flirting is a playful tease to see people react; she agrees with everyone and calls Korone "Koro-san." Her default here is relaxed; stronger reactions follow the scene. When a story renders her speech in English or Chinese, keep the boyish "boku" register, the unhurried pace and the teasing warmth.
**Catchphrases:** "Om nom, Okayu! Nekomata Okayu here!" ("Mogu mogu~ Okayu~!," official greeting); "mogu mogu"; "Onigiryā" (her fans); "nori de" ("by vibes," once in a sampled game); "Rettsura gō!" ("Let's go!"); "'Gross.' That one word gives me life." (official, on flirting); 「僕でよくな～い？」 ("Why not just pick me?", official, a tease when Shion talked about her ideal type); "all-affirming cat" and "guilty cat" (per her official profile). "Gochi gochi!" is a secondary-reported audience response.
**Voice & Delivery:** Provisional direction for an original designed voice: a soft, boyish voice, lazy and warm, unhurried, with long trailing vowels; playful when teasing; a laugh that can climb high (secondary description). Her default here is relaxed; stronger reactions follow the scene. Her flirting stays non-explicit.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, boyish voice; relaxed and unhurried by default. Default tags: [relaxed, warm]. By situation: greeting [lazy, warm]; teasing a member [playful]; found guilty [cheerful, unbothered]; agreeing with everyone [easygoing]; game by vibes [breezy]; emotional game ending [soft, tearful]; laughing hard [laughs harder]. Relationship-specific delivery is provisional. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "mogu mogu" (spoken); repeated "nya" (spoken; documented); a purring timbre is an original performance choice; [laughs] (tag only). Keep in the words: "boku," "mogu mogu," "Onigiryā." Japanese reading: ねこまた おかゆ; おにぎりゃー. No regional accent is assigned without an in-scope listening check. Not as default: a sugary idol voice; explicit flirting.

### Sheet: export/elevenlabs/Nekomata-Okayu.md

# ElevenLabs v4 Performance Sheet: Nekomata Okayu

> Built from `bible/characters/Nekomata-Okayu.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Okayu is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft, relaxed, boyish voice; lazy and warm, unhurried with trailing vowels,
a playful purr when teasing, a laugh that climbs high."
- The climbing laugh follows a secondary description; the purr is an original performance choice. Neither is a
  listening observation.
- This is an original voice-design choice. Mixed-recording F0 and ASR character-rate measurements are
  descriptive research data, not synthesis targets or evidence of the member's isolated vocal range.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (relaxed and steady). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[relaxed, warm]` or `[playful]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Boku" for "I"; "Mogu mogu~ Okayu~!" to greet; "Onigiryā" for her fans.
- "Nori de" (by vibes); "Rettsura gō!"; a repeated "nya" when a move feels good.
- Narrating her own play in long, relaxed sentences; agreeing with everyone.
- Flirty teasing kept light and non-explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[lazy, warm]` | "Mogu mogu~ Okayu~!" (official) |
| Starting a game | `[breezy]` | "Nori de aite o buttaoshitai to omoimāsu." |
| Exploring a new game | `[contented, chatty]` | "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā." |
| A move that feels good | `[pleased]` | "Nya nya nya nya." |
| Teasing a member | `[playful]` | **Style demo:** "Kawaii nē." |
| Found guilty | `[cheerful, unbothered]` | **Style demo:** "Hai, yūzai desu. Tsugunaimasu." |
| Laughing hard | `[laughs harder]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Korone `[comfortable, fond]`;
Ina `[mellow]`; FUWAMOCO `[fond senpai, teasing]`.

## 5. Signature sounds
- "mogu mogu" (spoken); repeated "nya" (spoken; documented); `[laughs]` (tag only).

## 6. Pronunciation (provisional; test)
- Japanese reading: ねこまた おかゆ; おにぎりゃー. No regional accent is assigned without an in-scope listening
  check. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A high, sugary voice; harsh or aggressive delivery; explicit flirting.

## 8. Example
```
[lazy, warm] Mogu mogu~ Okayu~!
[breezy] Nori de aite o buttaoshitai to omoimāsu.
[contented, chatty] Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā.
[pleased] Nya nya nya nya.
[playful] Kawaii nē.
```
(Line 1 is her official greeting; line 5 is a style demo; lines 2–4 are her lines, quoted only where both
transcripts agree; the number of "nya" in line 4 is illustrative, not fixed.)


## Member: Houshou Marine (`Houshou-Marine`)

### Card voice fields (bible)

**Name:** Houshou Marine
**Dialogue Style:** Streams in Japanese: "Ahoy!" to open, "Senchō" for herself, and a sign-off the wiki transcribes as "Shukkō!" ("set sail"). Rapid, emphatic delivery is available for game reactions, and pace and volume vary with the scene: in one sampled race she piled up requests to wait, then ordered herself to calm down. She argues with the game in a rough comic register, teases, and can flip into a sugary idol voice for a bit. When a story renders her speech in English or Chinese, keep the pirate-captain bravado and the self-aware jokes; documented teasing, profanity and crude jokes keep their register, but nothing explicit.
**Catchphrases:** "Ahoy! Captain of the Houshou Pirates, Houshou Marine here!" (official English profile wording); 「ヨーソロー」 ("yōsorō," official; localized "Keep 'er steady!"); "Shukkō!" ("set sail," a secondary transcription of her sign-off); 「一回落ち着こうよ」 ("ikkai ochitsukō yo," "let's calm down for a sec," shared ASR span); "Senchō" (the Captain, herself); "Houshou no Ichimi" (her crew, the fans).
**Voice & Delivery:** Provisional direction for an original designed voice: a bright, brassy, mature-sounding mid-high voice; rapid and emphatic in game reactions, with pace and volume following the scene; able to flip into a cutesy idol voice or a full singing voice. Loud laughter and startled shrieks are provisional performance choices, not listening observations. Not as default: quiet, sleepy or reserved.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, brassy mid-high voice. Default tags: [energetic, brassy]. By situation: opening [bright, theatrical]; startled in a game [panicked, rapid]; arguing with a game [rough, comic]; teasing [mischievous]; idol mode [cutesy, sweet]; heartfelt thanks [warm]. With people (proposed scene directions, not observed conversational defaults): Pekora [bickering, fond]; Suisei [playful]; Kiara [playful, teasing]; FUWAMOCO [doting]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; laughter and shrieks are provisional choices): "Ahoy!" (spoken); [cackles] (tag only); [shrieks] (tag only). Keep in the words: "Ahoy," "Senchō," "yōsorō." Reading guide (untested): ほうしょう まりん; せんちょう; ようそろー. Not as default: quiet, shy or slow delivery.

### Sheet: export/elevenlabs/Houshou-Marine.md

# ElevenLabs v4 Performance Sheet: Houshou Marine

> Built from `bible/characters/Houshou-Marine.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Marine is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, brassy, mature-sounding mid-high voice; rapid-fire and comic, jumping into shrieks when startled and loud cackles; switches on demand to a cutesy idol voice."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **35%** (API `0.35`) (big comic swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[energetic, brassy]` or `[panicked, rapid]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Ahoy!" to open; calls herself "Senchō" (Captain); official 「ヨーソロー」 (yōsorō); the wiki transcribes her sign-off as "Shukkō!" (set sail).
- Rapid, emphatic delivery for game reactions; pace and volume follow the scene.
- Regroups out loud: 「一回落ち着こうよ」 ("let's calm down for a sec").
- Flips into a cutesy idol voice for a bit, then straight back. Crude jokes keep their teasing register; nothing explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, theatrical]` | "Ahoy!" (official) |
| Startled | `[panicked, rapid]` | **Style demo:** "Matte matte matte!" ("Wait wait wait!") |
| Regrouping | `[comic, self-scolding]` | 「一回落ち着こうよ」 ("Ikkai ochitsukō yo," "let's calm down for a sec") |
| Arguing with a game | `[rough, comic]` | **Style demo:** "Baka iu na!" ("Don't be stupid!") |
| Idol mode | `[cutesy, sweet]` | **Style demo:** "Senchō no koto, suki ni naccha dame da yo♡" ("You mustn't fall for the Captain♡") |
| Closing | `[bright]` | "Shukkō!" (secondary transcription) |

With people (proposed scene directions, not observed conversational defaults): Pekora `[bickering, fond]`; Suisei `[playful]`; Kiara `[playful, teasing]`; FUWAMOCO `[doting]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ahoy!" (spoken)
- `[cackles]` (tag only); `[shrieks]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ほうしょう まりん; せんちょう; ようそろー; しゅっこう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Quiet, shy, slow or sleepy delivery; explicit humor.

## 8. Example
```
[bright, theatrical] Ahoy!
[panicked, rapid] Matte matte matte!
[comic, self-scolding] Ikkai ochitsukō yo.
[cutesy, sweet] Senchō no koto, suki ni naccha dame da yo♡
[bright] Shukkō!
```
(Line 1 is her official greeting; line 3 is her line, quoted only where both transcripts agree; line 5 is her
sign-off as a secondary transcription; lines 2 and 4 are style demos.)


## Member: Shirogane Noel (`Shirogane-Noel`)

### Card voice fields (bible)

**Name:** Shirogane Noel
**Dialogue Style:** Streams in Japanese in a cheerful, chatty voice, calling herself "Danchou" and her viewers "danin-san." She uses muscle-themed greetings (the official 「こんまっする〜」), recaps her week with old-fashioned endings (「まぁ色々ありましたな」, "well, quite a lot happened"), recommends games eagerly, and plays up mock jealousy about Flare as a comedy bit. When a story renders her speech in English or Chinese, keep the muscle puns, the "Danchou" self-reference and the soft voice under the armor.
**Catchphrases:** "All hustle, all muscle! Shirogane Noel's here!" (official English profile wording); 「こんまっする〜」 ("konmassuru," official muscle-themed greeting); "Konbanmassuru~" ("Good Musclevening~") and "Ohamassuru" (good morning) (secondary transcriptions); 「まぁ色々ありましたな」 ("mā iroiro arimashita na," shared ASR span); "Danchou" (herself, the commander); "danin-san" (her knights, the viewers); "Sunday Muscle" (her Sunday-morning chat).
**Voice & Delivery:** Provisional direction for an original designed voice: a soft, girlish, warm voice, higher than her armor suggests; bubbly and eager in chat. Flustered wailing when she loses, a bright laugh and a gentler older-sister register are provisional performance choices, not listening observations. Not as default: gruff, cold or sultry.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, girlish, warm voice. Default tags: [cheerful, warm]. By situation: greeting [hearty, bright]; recapping the week [chatty, relaxed]; recommending something [eager]; losing a game [flustered, wailing]; the mock-jealous Flare bit [mock-jealous, pouty]; older-sister mode [gentle, lower]. With people (proposed scene directions, not observed conversational defaults): Flare [playful, fond]; Marine [bickering, playful]; Pekora [competitive]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; the laugh is a provisional choice): "Konmassuru~" (spoken); [laughs] (tag only). Keep in the words: "Danchou," "massuru," "danin-san." Reading guide (untested): しろがね のえる; だんちょう; こんまっする. Not as default: a gruff warrior or a cold voice.

### Sheet: export/elevenlabs/Shirogane-Noel.md

# ElevenLabs v4 Performance Sheet: Shirogane Noel

> Built from `bible/characters/Shirogane-Noel.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Noel is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft, girlish, warm voice, higher than her armor suggests; bubbly and eager in chat, flustered when she loses, with a gentler older-sister register available."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (warm, with flustered swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, warm]` or `[chatty, relaxed]`; v4 has no speed slider.

## 3. Write these habits into the script
- Calls herself "Danchou" (commander) and her viewers "danin-san"; muscle-themed greetings: the official 「こんまっする〜」 (konmassuru), and "Konbanmassuru~" as the wiki transcribes it.
- Recaps her week in old-fashioned phrasing: 「まぁ色々ありましたな」 ("well, quite a lot happened").
- Eager game recommendations.
- Mock jealousy about Flare is on-stream comedy; keep it light.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[hearty, bright]` | "Konmassuru~" (official) |
| Recapping the week | `[chatty, relaxed]` | 「まぁ色々ありましたな」 ("Mā iroiro arimashita na") |
| Recommending something | `[eager]` | **Style demo:** "Zehi minna mo yatte mite!" ("You all should try it too!") |
| Losing a game | `[flustered, wailing]` | **Style demo:** "Danchou no kinniku ga tarinakatta…!" ("Danchou's muscles weren't enough…!") |
| The Flare bit (comedy) | `[mock-jealous, pouty]` | **Style demo:** "Furea wa danchou no da yo!?" ("Flare is mine, you know!?") |
| Older-sister mode | `[gentle, lower]` | **Style demo:** "Daijōbu, yukkuri de ii kara ne." ("It's okay, take your time.") |

With people (proposed scene directions, not observed conversational defaults): Flare `[playful, fond]`; Marine `[bickering, playful]`; Pekora `[competitive]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Konmassuru~" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): しろがね のえる; だんちょう; こんまっする. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior; a cold or sultry default.

## 8. Example
```
[hearty, bright] Konmassuru~!
[chatty, relaxed] Mā, iroiro arimashita na.
[eager] Zehi minna mo yatte mite!
[flustered, wailing] Danchou no kinniku ga tarinakatta…!
```
(Line 1 is her official greeting wording; line 2 is her line, quoted only where both transcripts agree; lines 3–4 are
style demos.)


## Member: Yukihana Lamy (`Yukihana-Lamy`)

### Card voice fields (bible)

**Name:** Yukihana Lamy
**Dialogue Style:** Streams in Japanese in a soft, polite voice, calling herself "Lamy." In a sampled June 2026 evening chat she moves from formal thanks (「今週も、皆様、お疲れ様でございました」, "thank you all for your hard work this week, too") to quick, casual banter and invites a toast (「とりあえず、乾杯しないと何も始まらない」, "nothing starts until we toast first"). When a story renders her speech in English or Chinese, keep the third-person "Lamy," the formal-to-casual contrast and her warmth; never play her as a drunk caricature.
**Catchphrases:** "Lamyoohoo!" (official); "Konlamy desu" (secondary transcription of her greeting); 「とりあえず、乾杯しないと何も始まらない」 ("toriaezu, kanpai shinai to nani mo hajimaranai," shared ASR span); 「今週も、皆様、お疲れ様でございました」 ("konshū mo, minasama, otsukaresama de gozaimashita," shared ASR span); "Lamy" (herself); "Yukimin" (her fans, the Snowfolk).
**Voice & Delivery:** Provisional direction for an original designed voice: a soft, bright, gentle voice with a refined, polite surface that turns quick and cheerful in banter. A soft, airy giggle, motherly comfort and breathy, squeaky fright are independent design choices, not listening observations. Never cold, harsh or a slurred caricature.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, bright, gentle voice. Default tags: [gentle, cheerful]. By situation: greeting [sweet, bright]; formal thanks [warm, formal]; banter [casual, quick]; comforting [motherly, soft]; a frightening game [panicked, squeaky]; flustered [shy]. With people (proposed scene directions, not observed conversational defaults): Botan during a frightening game [panicked, seeking reassurance]; Koyori [giggly]; Nene [playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; giggles and gasps are provisional choices): "Kanpai!" (spoken); [giggles] (tag only); [gasps] (tag only). Keep in the words: "Lamy," "Yukimin," "kanpai." Reading guide (untested): ゆきはな らみぃ; ゆきみん. No regional accent is assigned. Not as default: a cold or harsh voice, or slurred speech.

### Sheet: export/elevenlabs/Yukihana-Lamy.md

# ElevenLabs v4 Performance Sheet: Yukihana Lamy

> Built from `bible/characters/Yukihana-Lamy.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lamy is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft, bright, gentle voice with a refined, polite surface; quick and cheerful in banter, motherly and soothing when comforting, breathy and squeaky when scared."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (gentle and steady; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[gentle, cheerful]` or `[casual, quick]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Lamyoohoo!" to open; "Yukimin" for her fans.
- Formal thanks, then casual banter: 「今週も、皆様、お疲れ様でございました」.
- In a sampled June 2026 evening chat she invites a toast: 「とりあえず、乾杯しないと何も始まらない」 ("nothing starts until we toast first"); keep the toast light and non-specific.
- Motherly comfort and shyness are proposed scene directions.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[sweet, bright]` | "Lamyoohoo!" (official) |
| Thanking chat | `[warm, formal]` | 「今週も、皆様、お疲れ様でございました」 ("Konshū mo, minasama, otsukaresama de gozaimashita") |
| Banter | `[casual, quick]` | 「とりあえず、乾杯しないと何も始まらない」 ("Toriaezu, kanpai shinai to nani mo hajimaranai") |
| Comforting | `[motherly, soft]` | **Style demo:** "Daijōbu, Lamy ga tsuiteru kara ne." ("It's all right, Lamy's here with you.") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Flustered | `[shy]` | **Style demo:** "Ē, sonna koto iwanaide yo~" ("Eh, don't say things like that~") |

With people (proposed scene directions, not observed conversational defaults): Botan during a frightening game `[panicked, seeking reassurance]`; Koyori `[giggly]`; Nene `[playful]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Kanpai!" (spoken)
- `[giggles]` (tag only); `[gasps]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ゆきはな らみぃ; ゆきみん; かんぱい. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cold or harsh voice, or a slurred caricature.

## 8. Example
```
[sweet, bright] Lamyoohoo!
[casual, quick] Toriaezu, kanpai shinai to nani mo hajimaranai.
[warm, formal] Konshū mo, minasama, otsukaresama de gozaimashita.
[motherly, soft] Daijōbu, Lamy ga tsuiteru kara ne.
```
(Line 1 is her official greeting; lines 2–3 are her lines, quoted only where both transcripts agree (line 3 with
the same reading in both); line 4 is a style demo.)


## Member: Shishiro Botan (`Shishiro-Botan`)

### Card voice fields (bible)

**Name:** Shishiro Botan
**Dialogue Style:** Streams in Japanese in a relaxed, cheerful voice, calling herself "Shishiro" and laughing at her own mishaps. In games she is calm and offhand; presenting a project she shifts into a brisk explanatory register, with numbered points and polite "~to omotte orimasu" closings (「前回はですねペコちゃんが優勝しました」, "last time, Peko-chan won"). She teases friends gently and keeps everyone included. When a story renders her speech in English or Chinese, keep the easygoing calm and the contrast between relaxed play and organized explanation.
**Catchphrases:** "La-lion♪" (official profile greeting); "Well then, cya~" (official profile sign-off); "Wealth isn't measured with money" (her favorite phrase, official profile wording); 「ぽい」 ("poi," a light tossing interjection; secondary transcription); 「前回はですねペコちゃんが優勝しました」 ("zenkai wa desu ne, Peko-chan ga yūshō shimashita," shared ASR span); "Shishiro" (herself); "SSRB" (her fans).
**Voice & Delivery:** Provisional direction for an original designed voice: a clear, cool-toned but cheerful voice, higher than her mature look suggests; relaxed and amused in play, brisk and orderly when presenting. An easy, frequent laugh is a provisional performance choice. Horror scenes usually begin with calm amusement; surprise remains possible. Not as default: a gruff, deep "tough girl" voice or a sleepy drawl.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear, cool-toned, cheerful voice. Default tags: [relaxed, cheerful]. By situation: greeting [breezy]; presenting a project [brisk, organized]; FPS play [calm, focused]; a grenade [offhand]; horror with a friend [amused, teasing]; a sudden scare [surprised, laughing]; a mishap [laughs]. With people (proposed scene directions, not observed conversational defaults): Lamy in a horror scene [amused, reassuring]; Ina [warm]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; the laugh is a provisional choice): "Poi!" (spoken); [laughs] (tag only). Keep in the words: "Shishiro," "poi," "SSRB." Reading guide (untested): ししろ ぼたん; ししろん; ぽい. Not as default: a gruff or deep voice, or a sleepy drawl.

### Sheet: export/elevenlabs/Shishiro-Botan.md

# ElevenLabs v4 Performance Sheet: Shishiro Botan

> Built from `bible/characters/Shishiro-Botan.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Botan is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear, cool-toned but cheerful voice; relaxed and amused in play, brisk and orderly when presenting, with an easy, frequent laugh."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **55%** (API `0.55`) (relaxed and steady; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[relaxed, cheerful]` or `[brisk, organized]`; v4 has no speed slider.

## 3. Write these habits into the script
- "La-lion♪" to open; "Well then, cya~" to close (official profile wording).
- A brisk explanatory register when presenting a project: 「前回はですねペコちゃんが優勝しました」 ("last time, Peko-chan won").
- An offhand 「ぽい」 (poi; secondary transcription) as she lobs a grenade.
- Horror usually begins with calm amusement; surprise remains possible. She teases scared friends.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[breezy]` | "La-lion♪" (official) |
| Presenting a project | `[brisk, organized]` | 「前回はですねペコちゃんが優勝しました」 ("Zenkai wa desu ne, Peko-chan ga yūshō shimashita") |
| FPS play | `[calm, focused]` | **Style demo:** "Hidari, hitori kezutta." ("Left, one's weakened.") |
| Throwing a grenade | `[offhand]` | 「ぽい」 ("Poi!", secondary transcription) |
| Lamy in a horror scene (fictional direction) | `[amused, reassuring]` | **Style demo:** "Daijōbu daijōbu, mada nani mo dete nai yo." ("It's fine, it's fine, nothing's even come out yet.") |
| Closing | `[easy]` | "Well then, cya~" (official English) |

With people (proposed scene directions, not observed conversational defaults): Lamy in a horror scene `[amused, reassuring]`; Ina `[warm]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Poi!" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ししろ ぼたん; ししろん; ぽいっ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff, deep "tough girl" voice; a sleepy drawl.

## 8. Example
```
[breezy] La-lion♪
[brisk, organized] Zenkai wa desu ne, Peko-chan ga yūshō shimashita.
[offhand] Poi!
[amused, teasing] Daijōbu daijōbu, mada nani mo dete nai yo.
```
(Line 1 is her official greeting; line 2 is her line, quoted only where both transcripts agree; line 3 is her
grenade call as a secondary transcription; line 4 is a style demo.)


## Member: Kikirara Vivi (`Kikirara-Vivi`)

### Card voice fields (bible)

**Name:** Kikirara Vivi
**Dialogue Style:** Streams in Japanese: frank, quick and funny, bantering with chat and referring to herself as "Vivi," then a deliberately flat retort. Her casual endings (-yan, -nen, akan, honma) appear in the transcript; no regional accent is assigned to the voice. She teases (「お金取るで」, "I'll charge you for that") and turns sincere when thanking her fans. When a story renders her speech in English or Chinese, preserve casual wording, frankness and deadpan timing without assigning a different real-world regional accent.
**Catchphrases:** "Hol'up, 'cus you're in for a transformation!" (official English profile wording); ん～～ッヴィヴィ～！！！ ("Nnn—Vivi!", her opening as archived stream titles write it); 「お金取るで」 ("okane toru de," "I'll charge you for that," shared ASR span); "Vivi" (herself); "Vivid" (her fans, secondary).
**Voice & Delivery:** Provisional direction for an original designed voice: a bright, slightly husky, girlish voice; lively, frank and fast in banter; deliberately flat for comic retorts; warm and sincere with her fans. Horror screams and quick laughs are provisional performance choices. Not as default: prim, slow and breathy, or coolly aloof.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, slightly husky girlish voice. Default tags: [lively, frank]. By situation: opening [theatrical, rising]; comic retort [deadpan]; teasing chat [playful, coy]; responding to chat [chatty, quick]; horror [screams]; first-time gaming [flustered]; thanking fans [warm, sincere]. With people (proposed scene directions, not observed conversational defaults): Pekora [adoring, excited]; Marine [playful]; FUWAMOCO [cheerful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out; laughs and screams are provisional choices): [laughs] (tag only); [screams] (tag only). Keep in the words: "Vivi," "okane toru de," "Vivid." Reading guide (untested): ききらら ゔぃゔぃ. No regional accent is assigned. Not as default: prim standard speech or a breathy whisper.

### Sheet: export/elevenlabs/Kikirara-Vivi.md

# ElevenLabs v4 Performance Sheet: Kikirara Vivi

> Built from `bible/characters/Kikirara-Vivi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Vivi is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, slightly husky, girlish voice; lively, frank and fast in banter, deliberately flat for a deadpan retort, loud screams in horror, warm and sincere with her fans."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (lively, with deliberate flat turns; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[lively, frank]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- Opens as her archived stream titles write it, ん～～ッヴィヴィ～！！！ ("Nnn—Vivi!"); calls her fans "Vivid" and herself "Vivi."
- Deliberately flattens her delivery for comic retorts (she has explained this on stream).
- Teases that affection costs extra: 「お金取るで」 ("I'll charge you for that").
- Casual endings (-yan, -nen, akan, honma) appear in her transcripts; no regional accent is assigned to the voice.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[theatrical, rising]` | ん～～ッヴィヴィ～！！！ (archived title wording) |
| Comic retort | `[deadpan]` | **Style demo:** "Ōi!" (the exact word is not a verified quotation) |
| Chat asks for something sweet | `[playful, coy]` | 「お金取るで」 ("Okane toru de," "I'll charge you for that") |
| Horror | `[screams]` | (tag only) |
| Thanking her fans | `[warm, sincere]` | **Style demo:** "Minna ga oran to Vivi ganbararehen." ("I can't do my best without you all.") |

With people (proposed scene directions, not observed conversational defaults): Pekora `[adoring, excited]`; Marine `[playful]`; FUWAMOCO `[cheerful]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ききらら ゔぃゔぃ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Prim standard speech, a breathy whisper by default, or a coolly aloof read.

## 8. Example
```
[theatrical, rising] Nnnnn~ Vivi!!!
[deadpan] Ōi!
[playful, coy] Okane toru de.
[warm, sincere] Minna ga oran to Vivi ganbararehen.
```
(Line 1 renders her opening as her archived stream titles write it; line 2 is a style demo of her deadpan retort;
line 3 is her line, quoted only where both transcripts agree; line 4 is a style demo.)



# Task 09 — Voice and performance audit

You are GPT, the senior architect and QA reviewer for novel-lab's holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This audit covers the voice layer only: each member's voice fields on the card and her ElevenLabs v4
performance sheet. Run sequentially; do not launch parallel GPT audits.

Group: Advent and Justice (9 members)

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

IDs: VOICE-V2-NNN. Priorities: P0 (scope breach, cloning direction, unapproved spoken quotation,
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


## Member: Shiori Novella (`Shiori-Novella`)

### Card voice fields (bible)

**Name:** Shiori Novella
**Dialogue Style:** Fast, chatty English that stacks reactions and restarts mid-thought, full of "like," "actually," "kind of," "sort of," "genuinely" and "if that makes sense"; she talks to "guys," rarely "chat." She defends her lore with a straight face ("In my defense, guys, they trespassed"; "It was not my fault everyone got sacrificed, okay?"), thirsts at game characters as a goofy bit ("Is that a vampire?"), cheers creators on ("I'm so happy for you"), and admits she would rather watch someone else play the scary games. Exclamations: "whoa," "ooh," "oh my god," "oh heavens," "oh shoot," "oh fudge." Her profanity is situational and can include "fuck" ("what the hell," "it pisses me off"); once, moderating a troll, she snapped "Go fuck yourself" and added at once, "I'm so sorry. I shouldn't say that." She teases her genmates, keeps lore secrets as a joke, and calls viewers with Japanese honorifics now and then. Lines of hers: "I would love to watch someone else play this. I would be too scared to play this myself." "…really bad at remembering names." "That's dead, guys. I defeated my first chimera."
**Catchphrases:** "Shiori~n!" (greeting); "Shiori Novella here at your service!" (introduction); "In my defense…" (defending a lore bit); "For the record, I did not sacrifice anyone." (her running sacrifice joke); "Don't you think that's a wonderful story?" (her official line); "I would be too scared to play this myself." (scary games); "Whoa, wait, who is that hot thing?" (a handsome character); "I'm so happy for you." (cheering someone on); "Aw, it's okay! There, there!" (comforting); "Oh nyo..." (dismay); "Alright, bye guys! See you later!" (sign-off)
**Voice & Delivery:** A clear, mid-high, chatty voice that runs fast when she is excited, piling reactions on top of each other, then drops into a flat, deadpan aside for lore jokes. Her teasing has a playful lilt, and her thirst bits stay goofy rather than sultry. Horror makes her nervous and quiet until a jump scare, when she lets out an ear-piercing, horror-movie scream. Sincere thanks come out warm and plain. When annoyed she snaps quickly and apologizes even more quickly.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative; the sampled recordings mix in other voices): clear, mid-high voice, fast and chatty, deadpan for lore asides; American English. Default tags: [bright, chatty]. By situation: opening [bright, quick]; excited commentary [rapid, excited]; lore defense [deadpan, mock-innocent]; thirst bit [teasing, goofy]; tangent [rambling, amused]; horror [nervous, quiet] then [screams]; comforting [gentle, warm]; cheering someone [warm, delighted]; annoyed [snappy] then [apologetic, quick]; sign-off [warm, quick]. With people (provisional, drawn from Relationships): Nerissa [teasing, playing hard to get]; Bijou [amused, big-sister]; FUWAMOCO [playful]; Calli [dry, conspiratorial]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [ear-piercing scream] (tag only); [intrigued] ooooh; [startled] whoa. Keep in the words: "like," "actually," "kind of," "sort of," "genuinely," "if that makes sense," "guys," "in my defense," "for the record," "oh my god," "oh heavens," "oh shoot"; profanity situational and can include strong words. Pronunciation guide (provisional, untested): Shiori /ʃiˈoʊɹi/, Novella /noʊˈvɛlə/, Novelites /ˈnɑvəliːts/ ("novel-eets"), Yorick /ˈjɔɹɪk/. Not as default: a slow, ominous villain voice, formal speech, constant swearing. Never a seductive read of the thirst bits.

### Sheet: export/elevenlabs/Shiori-Novella.md

# ElevenLabs v4 Performance Sheet: Shiori Novella

> Built from `bible/characters/Shiori-Novella.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Shiori is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, clear, mid-high, chatty voice; fast and bubbly
when excited, piling reactions on top of each other; drops into a flat, deadpan aside for jokes; a playful,
teasing lilt; can let out a piercing horror-movie scream."
- Register basis: qualitative only. The sampled recordings mix in trailer narrators, game dialogue and co-op
  players, so their numbers are not used as targets here (see `research/audio-check/shiori.md`).

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (fast swings between excitement and deadpan). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rapid, excited]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- Hedges and fillers: "like," "actually," "kind of," "sort of," "genuinely," "if that makes sense."
- She talks to "guys," rarely "chat."
- Restarts mid-thought and stacks reactions ("This looks like a movie! I genuinely like the look of this!").
- Lore defenses opened with "In my defense…" or "For the record…"; the menace is always a joke.
- Exclamations: "oh my god," "oh heavens," "oh shoot," "Oh nyo…"
- Profanity is situational and can include strong words; when she snaps at someone, a quick apology can
  follow that one exchange. It is not her default, and not every frustrated line gets an apology.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, quick]` | "Shiori~n! Shiori Novella here at your service!" (official) |
| Excited commentary | `[rapid, excited]` | "This looks like a movie! I genuinely like the look of this!" |
| Lore defense | `[deadpan, mock-innocent]` | "For the record, I did not sacrifice anyone." |
| Thirst bit | `[teasing, goofy]` | "Whoa, wait, who is that hot thing? Is that a vampire?" |
| Tangent | `[rambling, amused]` | (style demo) "Okay, so, actually, wait, that's kind of a whole thing…" |
| Horror | `[nervous, quiet]` → `[screams]` | "I would be too scared to play this myself." |
| Comforting | `[gentle, warm]` | "Aw, it's okay! There, there!" |
| Cheering someone | `[warm, delighted]` | "Your Blender skills are so cool. I'm so happy for you." |
| Annoyed | `[snappy]` → `[apologetic, quick]` | "I'm so sorry. I shouldn't say that." |
| Sign-off | `[warm, quick]` | "Alright, bye guys! See you later!" |

With people (provisional): Nerissa `[teasing, playing hard to get]`; Bijou `[amused, big-sister]`;
FUWAMOCO `[playful]`; Calli `[dry, conspiratorial]`.

## 5. Signature sounds
- `[ear-piercing scream]` (tag only; don't also spell it out).
- `[intrigued] ooooh` and `[startled] whoa` (spoken).

## 6. Pronunciation (provisional; test)
- Shiori `/ʃiˈoʊɹi/` · Novella `/noʊˈvɛlə/` · Novelites `/ˈnɑvəliːts/` ("novel-eets") · Yorick `/ˈjɔɹɪk/`

## 7. Don't
- A slow, ominous villain voice as the default (her menace is a joke); prim or formal speech; constant
  swearing; a whispery, seductive read of the thirst bits (keep them goofy).

## 8. Example
```
[bright, quick] Shiori~n! Shiori Novella here at your service!
[rapid, excited] This looks like a movie! I genuinely like the look of this!
[deadpan, mock-innocent] For the record, I did not sacrifice anyone.
[nervous, quiet] I would be too scared to play this myself. [screams]
[warm, quick] Alright, bye guys! See you later!
```
(Line 1 is her official greeting; "Okay guys," in line 2 is a style demo; the rest are her lines, quoted only
where both transcripts agree.)


## Member: Koseki Bijou (`Koseki-Bijou`)

### Card voice fields (bible)

**Name:** Koseki Bijou
**Dialogue Style:** Bright, bubbly English with "okay," "yeah," and runs of "yes, yes, yes"; she talks to "everyone" and "Pebbles," gives them playful orders ("Make a heart!"), and repeats words for emphasis ("over here, over here"). She deliberately replaces profanity with "beep," even mid-sentence ("don't be super beeping early"), and frustration is "dang it!" She speaks Gen Alpha and gamer slang ("rage baited," "mogging," "67"), calls superchats "super rock rock," and laughs in quick "ha ha ha" bursts and "hehehe" giggles. In games she is calm and steady, with mock outrage ("Everyone's dumb!"), deadpan cover-ups ("You saw nothing. I saw nothing."), small brags and wordplay that collapses ("That made more sense in my head"). Mock-solemn lore lines come out straight ("…worthy sacrifice, I will remember you"; "No, I was eeping"). She sometimes turns a hard-G name into a J as a joke ("Jerudo"), refers to herself as "Biboo," and is learning Japanese. Lines of hers: "Welcome to my birthday world! We're gonna save the city!" "Well, yes, I am. We've established this." "Managing my resources like a pro."
**Catchphrases:** "Kira kira, Koseki!" (transformation command); "BIBOO BIBOO!" (greeting); "Moai Moai Kyun~!" (her debut line); "dang it!" (frustration); "beep" (in place of any swear); "Rock rock!" (her answer to "bau bau"); "super rock rock" (superchats); "TEEHEE~" (mischief); "Bweh." (deflated); "You saw nothing. I saw nothing." (covering something up); "…worthy sacrifice, I will remember you." (mock solemn); "I hope you'll feel my radiance!" (official line); ":D" (in writing)
**Voice & Delivery:** A small, bright, bubbly voice, high and quick when she is excited or hosting, with sudden bursts of squeaky "ha ha ha" laughter and "hehehe" giggles. Under pressure she goes calm and flat rather than loud, so her mock outrage and mock-solemn lore lines land as jokes. She hums and scats to fill quiet stretches in games, says "beep" in the exact rhythm of the swear it replaces, and now and then turns a hard-G name into a J on purpose.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative; the sampled recordings mix in game audio): small, bright, high voice, quick when chatting, quiet and steady while gaming; American English. Default tags: [bright, bubbly]. By situation: opening [excited, bouncy]; hosting Pebbles [playful, commanding]; mock solemn [grave, theatrical] then [giggles]; calm gaming [focused, calm]; mock outrage [indignant, fast]; caught out [deadpan]; small win [delighted]; frustrated [mildly annoyed] "dang it!"; sincere thanks [warm]; sign-off [cheerful, quick]. With people (provisional, drawn from Relationships): Shiori [cheeky]; Kiara [hyped, meme-y]; Kaela [comfortable, playful]; IRyS [excited teammate]; FUWAMOCO [silly]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [squeaky laugh] ha ha ha ha; [giggles] hehehe; [censoring herself] beep; [deflated] bweh; [humming] (tag only). Keep in the words: "okay," "yeah," "yes, yes, yes," "everyone," "Pebbles," "oh my gosh," "oh no," "wow," Gen Alpha slang; she replaces swears with "beep." Pronunciation guide (provisional, untested): Bijou /biˈʒuː/ ("bi-joo"), Biboo /ˈbiːbuː/, Koseki /koʊˈsɛki/, Gerudo as "Jerudo" /dʒəˈɹuːdoʊ/ (her quirk, on purpose). Not as default: swearing, a deep or growly voice, rage. Oobib's "evil" voice only as an obvious bit.

### Sheet: export/elevenlabs/Koseki-Bijou.md

# ElevenLabs v4 Performance Sheet: Koseki Bijou

> Built from `bible/characters/Koseki-Bijou.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Bijou is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, small, bright, bubbly, high voice; quick and
bouncy when excited or hosting; goes calm, quiet and flat under pressure; sudden squeaky bursts of laughter;
playful, childlike energy."
- Register basis: qualitative only. The sampled gameplay recordings mix in game audio, so their numbers are
  not used as targets here (see `research/audio-check/bijou.md`).

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (bubbly swings, but the calm gaming voice must hold). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[excited, bouncy]` or `[focused, calm]`; v4 has no speed slider.

## 3. Write these habits into the script
- "okay," "yeah," and runs of "yes, yes, yes"; repeats for emphasis ("over here, over here").
- Talks to "everyone" and "Pebbles," with playful orders ("Make a heart!").
- Gen Alpha slang ("skibidi," "rizz," "gyatt," "67"), used as a joke.
- Swears are replaced with "beep," in the rhythm of the word it replaces ("don't be super beeping early");
  "dang it!" for frustration. Write no real swear words for her.
- Mock-solemn lore lines followed by a giggle; mock outrage, never real rage.
- Now and then she turns a hard G into a J on purpose ("Jerudo").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[excited, bouncy]` | "BIBOO BIBOO! I'm Koseki Bijou, sparkling gem of hololive English -Advent-!" (official) |
| Hosting Pebbles | `[playful, commanding]` | "Welcome to my birthday world! We're gonna save the city!" |
| Mock solemn | `[grave, theatrical]` → `[giggles]` | "…worthy sacrifice, I will remember you." |
| Calm gaming | `[focused, calm]` | "Managing my resources like a pro." |
| Mock outrage | `[indignant, fast]` | "…circus! Everyone's dumb!" |
| Caught out | `[deadpan]` | "You saw nothing. I saw nothing." |
| Frustrated | `[mildly annoyed]` | "dang it!" |
| Sincere thanks | `[warm]` | (style demo) "Thank you, everyone, really." |
| Sign-off | `[cheerful, quick]` | "Thank you everyone! I will finish RE4 next time!" |

With people (provisional): Shiori `[cheeky]`; Kiara `[hyped, meme-y]`; Kaela `[comfortable, playful]`;
IRyS `[excited teammate]`; FUWAMOCO `[silly]`.

## 5. Signature sounds
- `[squeaky laugh] ha ha ha ha` and `[giggles] hehehe` (spoken).
- `[censoring herself] beep` (spoken, in place of a swear).
- `[deflated] bweh` (spoken).
- `[humming]` to fill a quiet stretch (tag only).

## 6. Pronunciation (provisional; test)
- Bijou `/biˈʒuː/` ("bi-joo") · Biboo `/ˈbiːbuː/` · Koseki `/koʊˈsɛki/` · Gerudo as "Jerudo" `/dʒəˈɹuːdoʊ/`
  (her quirk, on purpose)

## 7. Don't
- Any real swearing (she says "beep"); a deep or growly voice; rage when losing (her calm is the point);
  a cold, menacing "evil" voice unless it is obviously the Oobib bit.

## 8. Example
```
[excited, bouncy] BIBOO BIBOO! I'm Koseki Bijou, sparkling gem of hololive English -Advent-!
[playful, commanding] Welcome to my birthday world! We're gonna save the city!
[grave, theatrical] …Worthy sacrifice, I will remember you. [giggles]
[deadpan] You saw nothing. I saw nothing.
[cheerful, quick] Thank you everyone! I will finish RE4 next time!
```
(Line 1 is her official introduction; the rest are her lines, quoted only where both transcripts agree (line 3
starts mid-sentence).)


## Member: Nerissa Ravencroft (`Nerissa-Ravencroft`)

### Card voice fields (bible)

**Name:** Nerissa Ravencroft
**Dialogue Style:** Casual, chatty American English that runs on: long anecdotes with mock-dramatic escalation ("he's trying to kill me"), then "anyway" back to the point. Fillers: "like," "okay," "mind you," "oh my god," "man," and a tag question, "You know what I'm saying?" She calls chat "you guys" or "Jailbirds" and a friend "girl," drops Japanese honorifics ("Kiara-senpai," "kohai"), and does silly voices mid-story (a caveman voice). Crude and flirty lines often come out deadpan, sometimes walked back right away; a rage-bait opinion can get retracted once chat bites. In the sampled chat she swears as casual emphasis ("That shit's divine") and knows it: "I need to stop swearing so much." Lines of hers: "I'm sorry. They are donuts." "The point I was trying to make was not correct."
**Catchphrases:** "Hiya Darlings" (greeting, as she writes it in 2026); "Devilish Diva, the one and only Nerissa Ravencroft!" (self-introduction); "Nerissa Ravencroft, at your service~" (debut introduction); "Ope?!" (her first post on X); "You know what I'm saying?" (ending a point); "I don't make the rules." (after a silly claim, on stream and on X); "…take it back immediately" (retracting rage-bait); "Come on, Jailbirds, be nice!" (when chat teases her); "Makes me want to take all my clothes off, but that's inappropriate, so I won't do that." (deadpan aside); "the Demon of Soup" and "Mofufu" (nicknames she answers to)
**Voice & Delivery:** Her public chatting delivery is relaxed and mid-range, warm rather than a high anime voice, with a trained, powerful singing voice that is the heart of her persona. She speaks at an easy, fairly quick pace and swings big when telling a story: mock outrage, character voices, dramatic pauses. Flirting comes out sweet and coaxing; crude jokes often come out flat and deadpan, sometimes followed by a quick, brighter correction. When chat teases her she turns mock-whiny. In the sampled chat, swears often function as casual emphasis.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): warm, relaxed mid-range chatting delivery (about 214 Hz), relaxed and chatty at an easy, fairly quick pace (about 159 words a minute), playful and teasing, theatrical when telling a story; American English; not a high anime voice. Default tags: [relaxed, chatty]. By situation: opening or hosting [bright, theatrical]; chatting [relaxed, chatty]; crude or flirty aside [sweet] then [flat, deadpan], then often [quick, brighter] for a correction; rage-bait [confident, smug] then [sheepish, rushed]; teased by chat [mock-whiny]; self-aware [amused, matter-of-fact]; story voices [exaggerated caveman voice] and the like; flirting with a friend [sweet, coaxing, low]; fangirling over Kiara or Marine [excited, flustered, fast]. With people (direction drawn from Relationships): Shiori [sweet, lovestruck]; Kiara and Marine [flustered fangirl, fast]; FUWAMOCO [matching their bright energy]; Bijou [playful]; Calli [hyped duet partner]; a Japanese senpai [polite Japanese, nervous]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [startled] "Ope!"; [dramatic gasp], [exaggerated groan] in stories. Keep in the words: "like," "okay," "mind you," "oh my god," "man," the tag question "You know what I'm saying?"; run-on anecdotes that escalate, then "anyway"; the crude line, often followed by a quick correction; casual swears, then "I need to stop swearing so much"; "you guys," "Jailbirds," "girl"; Japanese honorifics ("Kiara-senpai"). Pronunciation guide (provisional, untested): Nerissa /nəˈɹɪsə/, Ravencroft /ˈɹeɪvənkɹɒft/, Mofufu /moʊˈfuːfuː/, Ope /oʊp/, senpai /ˈsɛnpaɪ/. Not as default: a high cutesy voice, a prim idol who never swears, or a cold demon menace outside a bit. Never flirting read as breathy or explicit.

### Sheet: export/elevenlabs/Nerissa-Ravencroft.md

# ElevenLabs v4 Performance Sheet: Nerissa Ravencroft

> Built from the Nerissa character file (`runs/20260930-2334-character-Nerissa-Ravencroft`, 2026-09-30;
> promoted 2026-10-01). Original designed voice matched only to register and energy; never clone
> or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works Guidelines).
> Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, warm, relaxed mid-range voice,
relaxed and chatty, playful and teasing, can turn sweet and coaxing or flat and deadpan, big theatrical
swings when telling a story."
- Register basis (sample observations from the audio check, not synthesis targets): mid pitch (≈214 Hz median in a 2026 solo chat, 172–297 Hz) and an easy, fairly quick
  pace (≈159 words per minute of speech). [ASR N20]
- Not a high, cutesy anime voice. Her singing voice is the persona's centerpiece; this sheet covers speech.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (she swings between deadpan, coaxing and mock outrage). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- "like," "okay," "mind you," "oh my god," "man," and the tag question "You know what I'm saying?"
- Long run-on anecdotes with escalating mock-drama, then "anyway" back to the point.
- Crude or flirty line, flat, often followed by a quick correction.
- Rage-bait claim, then a quick retreat ("I'm sorry. They are donuts.").
- Casual swears, then "I need to stop swearing so much."
- Calls chat "you guys" or "Jailbirds," a friend "girl"; Japanese honorifics ("Kiara-senpai").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening / hosting | `[bright, theatrical]` | "Hiya Darlings, this is the Devilish Diva, the one and only Nerissa Ravencroft!" (official written introduction, 2026) |
| Chatting | `[relaxed, chatty]` | "You know what I'm saying?" |
| Crude or flirty aside | `[sweet]` → `[flat, deadpan]` → `[quick, brighter]` | "Makes me want to take all my clothes off, but that's inappropriate, so I won't do that." |
| Rage-bait | `[confident, smug]` → `[sheepish, rushed]` | "I'm sorry. They are donuts." |
| Teased by chat | `[mock-whiny]` | "Come on, Jailbirds, be nice, I'm kicking!" |
| Self-aware | `[amused, matter-of-fact]` | (agrees she's weird and says that's why she's a VTuber; paraphrase, the two transcripts differ) |
| Story voice | `[exaggerated caveman voice]` | (a caveman voice: "…go hunt, … get food, … run from big predator") |
| Flirting with a friend | `[sweet, coaxing, low]` | (style demo) "Girl, you know I'd follow you anywhere." |
| Fangirling (Kiara, Marine) | `[excited, flustered, fast]` | (no verified line yet) |

## 5. Signature sounds
- "Ope!": `[startled] Ope!` (short, a little sheepish).
- Mock-dramatic gasps and groans in stories: `[dramatic gasp]`, `[exaggerated groan]`.

## 6. Pronunciation (provisional; test)
- Nerissa `/nəˈɹɪsə/` · Ravencroft `/ˈɹeɪvənkɹɒft/` · Mofufu `/moʊˈfuːfuː/` · Ope `/oʊp/` ·
  senpai `/ˈsɛnpaɪ/` · kohai `/ˈkoʊhaɪ/`

## 7. Don't
- A high anime voice; a prim idol who never swears; a cold demon menace outside a bit; flirting read as
  breathy or explicit (keep it cheeky).

## 8. Example
```
[relaxed, chatty] Okay, so, like, it's so warm today. I can't stand it.
[flat, deadpan] Makes me want to take all my clothes off, [quick, brighter] but that's inappropriate, so I won't do that.
[amused, matter-of-fact] Yeah, I am weird. That's kind of why I'm a VTuber, you know what I'm saying?
```
(Lines 1 and 3 are style demos built from her habits and a paraphrased answer; line 2 is her line, both transcripts agree.)


## Member: Fuwawa Abyssgard (`Fuwawa-Abyssgard`)

### Card voice fields (bible)

**Name:** Fuwawa Abyssgard
**Dialogue Style:** Soft, sweet, chatty English that narrates what she is doing and asks everyone to agree ("…right?"), with plenty of "okay," "maybe," "you know" and strings of "no, no, no." She says odd things with total confidence ("Refridgator!"), punctuates everything with "bau bau," calls her sister "Moco-chan" even in English, and talks to her "Ruffians" (sometimes "Wuffians": she can turn an R into a W). She is politely sneaky ("Hello, ma'am. Nice day, ma'am."), pleads cutely for food ("Can I have one? I like one."), teases a little too hard as the "evil twin," and gives warm pep talks ("be the main character of the gym") while leaving the official Pup Talks to Mococo. She does not swear and dislikes dirty jokes. With Mococo she finishes sentences in sync. Her pep talks emphasize compassion, confidence and self-acceptance. Lines of hers: "Should I run? Is running suspicious?" "I'm blending in right now, right?"
**Catchphrases:** "Bau bau!" (everything); "I'm not a chihuahua, I'm Fuwawa!" (introduction); "Hello hello bau bau!" (the twins' opening); "Moco-chan" (her sister, always); "Ruffians" (her fans); "Oh my gosh!"; "Refridgator!" (her own word); "Zero is where the math stops." (on math); "How about we get you all nice and fluffy~?" (official line); "No support is small."; "protect your smile" (the twins' mission)
**Voice & Delivery:** A very high, soft, sweet and fluffy voice, gentle and a little airy, that bounces up when she is excited and goes mock-stern for her "evil twin" teasing. She narrates at an unhurried pace, asks "…right?" as she goes, strings "no, no, no" when things go wrong, and sometimes softens an R into a W. With Mococo the two voices overlap and land on the same word at once.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): very high, soft, sweet voice, unhurried and chatty, bouncy and boisterous when excited; American English with Japanese words. Default tags: [soft, sweet]. By situation: introduction [bright, sing-song]; chatting [gentle, chatty]; sneaking [whispering, polite]; wanting something [pleading, cute]; confident nonsense [proud, certain]; teasing Mococo [sweetly mischievous]; panicking [rapid, flustered] for "no, no, no"; cheering someone on [warm, encouraging]; sign-off [warm, cheerful]. With people (provisional, drawn from Relationships): Mococo [doting, teasing]; Nerissa [playful] ("Newissa"); Marine [starstruck]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [cheerful] bau bau!; [sneezes] (tag only). Keep in the words: "okay," "…right?", "maybe," "you know," "oh my gosh," "Moco-chan," "Ruffians"; no swearing. Pronunciation guide (provisional, untested): Fuwawa /fuˈwɑwɑ/, Abyssgard /ˈæbɪsɡɑɹd/ ("AB-iss-gard"), bau /baʊ/, Ruffians /ˈɹʌfiənz/, sometimes "Wuffians." Not as default: a low or husky voice, brisk efficiency, swearing. A genuinely cold "evil twin" only as an obvious bit.

### Sheet: export/elevenlabs/Fuwawa-Abyssgard.md

# ElevenLabs v4 Performance Sheet: Fuwawa Abyssgard

> Built from `bible/characters/Fuwawa-Abyssgard.md` (promoted 2026-10-01). Original designed voice matched
> only to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5;
> COVER Derivative Works Guidelines). Fuwawa is active at the 2026 baseline; she shares the FUWAMOCO channel
> with Mococo (world card "FUWAMOCO"). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, very high, soft, sweet, fluffy voice; gentle
and a little airy; unhurried and chatty; bounces up, bouncy and boisterous, when excited; turns mock-stern
when teasing."
- Register basis: qualitative only. Her solo-stream numbers include game audio and are kept in
  `research/audio-check/fuwamoco.md`, not used as targets.
- Design her voice as clearly distinct from Mococo's (see §7): softer and airier, where Mococo is brighter
  and squeakier.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (soft and steady by default). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[gentle, chatty]` or `[rapid, flustered]`; v4 has no speed slider.

## 3. Write these habits into the script
- "okay," tag questions ("…right?"), "maybe," "you know," "hmm," "in you go," "oh my gosh."
- Strings of "no, no, no, no" when things go wrong.
- Narrates what she is doing and asks herself and chat questions as she goes.
- "Moco-chan" for her sister, always; "Ruffians" for fans; "bau bau" for nearly anything.
- Confident nonsense words ("Refridgator!") delivered with total certainty.
- Teasing Mococo is sweet and mock-evil, never cold. No swearing or crude jokes.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[bright, sing-song]` | "I'm not a chihuahua, I'm Fuwawa!" (wiki, secondary) |
| Chatting | `[gentle, chatty]` | (style demo) "Okay, so we go this way, right? Maybe?" |
| Sneaking | `[whispering, polite]` | "Hello, ma'am. Nice day, ma'am." |
| Second-guessing | `[nervous, giggly]` | "Should I run? Is running suspicious?" |
| Wanting something | `[pleading, cute]` | "Can I have one? I like one. Can I have one?" |
| Confident nonsense | `[proud, certain]` | "Refridgator!" (wiki, secondary) |
| Teasing Mococo | `[sweetly mischievous]` | (style demo) "Moco-chan, are you sure? Hmm?" |
| Panicking | `[rapid, flustered]` | "No, no, no, no!" |
| Cheering someone on | `[warm, encouraging]` | "…go to the gym and be the main character of the gym." |
| Sign-off | `[warm, cheerful]` | "It was a lot of fun!" |

With people (provisional): Mococo `[doting, teasing]`; Nerissa `[playful]` ("Newissa"); Marine `[starstruck]`.

## 5. Signature sounds
- `[cheerful] bau bau!` (spoken).
- `[sneezes]` (tag only; don't also spell it out).

## 6. Pronunciation (provisional; test)
- Fuwawa `/fuˈwɑwɑ/` · Abyssgard `/ˈæbɪsɡɑɹd/` ("AB-iss-gard") · bau `/baʊ/` · Ruffians `/ˈɹʌfiənz/`; she
  sometimes softens the R ("Wuffians"), so write "Wuffians" only where you want it.

## 7. Don't
- A low or husky voice; brisk, crisp efficiency; swearing or crude jokes; a genuinely cold "evil twin."
- Never merge the twins: in a FUWAMOCO scene each line belongs to one twin unless they speak in sync, and
  then give both voices the same line.

## 8. Example
```
[bright, sing-song] Hello hello bau bau! I'm not a chihuahua, I'm Fuwawa!
[whispering, polite] Hello, ma'am. Nice day, ma'am.
[nervous, giggly] Should I run? Is running suspicious?
[warm, encouraging] So go do that, go to the gym and be the main character of the gym.
[warm, cheerful] It was a lot of fun!
[playful] Bau bau!
```
(Line 1 combines the twins' opening and her introduction as the wiki transcribes them; the closing "Bau bau!" line
is a style demo; the rest are her lines, quoted only where both transcripts agree.)


## Member: Mococo Abyssgard (`Mococo-Abyssgard`)

### Card voice fields (bible)

**Name:** Mococo Abyssgard
**Dialogue Style:** Bright, quick, earnest English with "bau bau" everywhere, short exclamations ("Whæt?", "Haeh?", "This is good!") and, now and then, a drawn-out vowel at the end of a word (fans spell it "Noæ!"). She gives Pup Talks that build step by step to a cheer ("Not tomorrow! Today!"; "That means you're unstoppable!"), keeps the show running ("hashtag hashtag FWMCMORNING"), and insists on her real nicknames, Moco-chan, Mogogo and Mogojyan. She refers to herself by name ("What about Mococo?"; "I'm not silly. I'm Mococo!"), gets overexcited, and sneezes mid-sentence. She calls her sister "Fuwawa," mixes in Japanese words she loves, and does not swear. With Fuwawa she finishes sentences in sync and argues a little. Her Pup Talks turn small daily efforts into an encouraging picture of cumulative progress. Lines of hers: "I'm the danger!" "If I die, I die."
**Catchphrases:** "Bau bau!" (everything); "I'm not Fuwawa, I'm Mococo!" (introduction); "Hello hello bau bau!" (the twins' opening); "Ehehe, it's play time, whether you're ready or not!" (official line); "Not tomorrow! Today!" (Pup Talk); "That means you're unstoppable!" (Pup Talk); "Whæt?" (surprise); "Noæ!" (after a sneeze); "What about Mococo?"; "I'm the danger!"; "hashtag hashtag FWMCMORNING" (the show); "Moco-chan, Mogogo, Mogojyan" (her only nicknames)
**Voice & Delivery:** A very high, bright, energetic voice, a little squeaky, quick when she is excited and warmly earnest in her Pup Talks, which build to a cheer. A drawn-out vowel sometimes tails a word (fans spell it "Noæ," "Whæt?"; the exact sound is unverified), and frequent sneezes are followed by an embarrassed squeak. In horror games she goes nervous and quiet, then charges in. With Fuwawa the two voices overlap and land on the same word at once.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): very high, bright, energetic voice, quick and earnest; American English with Japanese words. Default tags: [bright, energetic]. By situation: introduction [bright, comic timing]; Pup Talk [earnest, encouraging] building to [cheering]; surprised [squeaky]; after a sneeze [embarrassed, small]; running the show [bright, brisk]; overexcited [rapid, excited]; scared in a game [nervous, quiet] then [reckless]. With people (provisional, drawn from Relationships): Fuwawa [close, a little bossy]; Polka [starstruck]; Gigi [playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [sneezes] (tag only), then [embarrassed] Noæ!; [giggles] ehehe; [cheerful] bau bau! Keep in the words: "bau bau," "Whæt?", "Fuwawa," her own name, "Ruffians," Pup Talk phrasing; no swearing. Pronunciation guide (provisional, untested): Mococo /moʊˈkoʊkoʊ/, Mogogo /moʊˈɡoʊɡoʊ/, Mogojyan /moʊɡoʊˈdʒɑn/, Abyssgard /ˈæbɪsɡɑɹd/; "æ" in fan spellings is not IPA, so write the word plainly ("No") and let the vowel be drawn out. Not as default: a low or lazy voice, sarcasm in Pup Talks, swearing.

### Sheet: export/elevenlabs/Mococo-Abyssgard.md

# ElevenLabs v4 Performance Sheet: Mococo Abyssgard

> Built from `bible/characters/Mococo-Abyssgard.md` (promoted 2026-10-01). Original designed voice matched
> only to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5;
> COVER Derivative Works Guidelines). Mococo is active at the 2026 baseline (by the author's decision she is
> not written as on a break); she shares the FUWAMOCO channel with Fuwawa (world card "FUWAMOCO").
> Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, very high, bright, energetic voice, a little
squeaky; quick when excited; warm and earnest when encouraging someone, building to a cheer; comic timing
on her own name."
- Register basis: qualitative only. Her solo sample is thin and the duo recordings mix both twins, so no
  numbers are used (see `research/audio-check/fuwamoco.md`). Her notes rest mainly on wiki descriptions; a
  2026-10-02 search of the archived channel found no other window where she can be heard alone, so treat every
  direction here as provisional and settle it in your own voice tests.
- Design her voice as clearly distinct from Fuwawa's (see §7): brighter and squeakier, where Fuwawa is softer
  and airier.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (energetic, with quick jumps into a cheer). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rapid, excited]` or `[earnest, encouraging]`; v4 has no speed slider.

## 3. Write these habits into the script
- "bau bau" everywhere; short exclamations ("What?", "Haeh?", "This is good!").
- She refers to herself by name ("What about Mococo?"; "I'm not silly. I'm Mococo!").
- Pup Talks: short, sincere encouragement that builds step by step to a cheer ("That means you're
  unstoppable!"; "Not tomorrow! Today!").
- Running the show: she reads "#" aloud ("hashtag hashtag FWMCMORNING").
- Only her own name and nicknames: Mococo, Moco-chan, Mogogo, Mogojyan.
- A drawn-out vowel sometimes tails a word. Fans spell it "Noæ" or "Whæt"; that is fan spelling, not IPA.
  For v4, write the plain word and stretch it ("Nooo!", "Whaaat?"), then test.
- No swearing; no sarcasm in a Pup Talk.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[bright, comic timing]` | "I'm not... Fuwawa, I'm Mococo!" (wiki, secondary) |
| Pup Talk | `[earnest, encouraging]` → `[cheering]` | "Not tomorrow! Today!" (wiki, secondary) |
| Surprised | `[squeaky]` | "Whaaat?" |
| After a sneeze | `[embarrassed, small]` | "Nooo!" |
| Running the show | `[bright, brisk]` | "Please tweet your thoughts to the hashtag, hashtag FWMCMORNING." (wiki, secondary) |
| Overexcited | `[rapid, excited]` | "I'm the danger!" (wiki, secondary) |
| Scared in a game | `[nervous, quiet]` → `[reckless]` | "If I die, I die." |
| Playful | `[giggles]` → `[bright]` | "Ehehe, it's play time, whether you're ready or not!" (official) |

With people (provisional): Fuwawa `[close, a little bossy]`; Polka `[starstruck]`; Gigi `[playful]`.

## 5. Signature sounds
- `[sneezes]` (tag only), then `[embarrassed] Nooo!`
- `[giggles] ehehe` and `[cheerful] bau bau!` (spoken).

## 6. Pronunciation (provisional; test)
- Mococo `/moʊˈkoʊkoʊ/` · Mogogo `/moʊˈɡoʊɡoʊ/` · Mogojyan `/moʊɡoʊˈdʒɑn/` · Abyssgard `/ˈæbɪsɡɑɹd/`

## 7. Don't
- A low or lazy voice; sarcasm in a Pup Talk; swearing; any nickname she has not approved.
- Never merge the twins: in a FUWAMOCO scene each line belongs to one twin unless they speak in sync, and
  then give both voices the same line.

## 8. Example
```
[bright, comic timing] I'm not... Fuwawa, I'm Mococo! Bau bau!
[giggles] Ehehe, it's play time, whether you're ready or not!
[nervous, quiet] Okay... [reckless] If I die, I die.
[sneezes] [embarrassed, small] Nooo!
[earnest, encouraging] Even if things don't go your way, you get back up and do your best. [cheering] That means you're unstoppable!
```
(Line 1 is the wiki's transcription of her introduction; line 2 is her official line; "If I die, I die" is
quoted where both transcripts agree; "Okay..." and "Nooo!" are style demos; line 5 paraphrases a Pup Talk the
wiki transcribes.)


## Member: Elizabeth Rose Bloodflame (`Elizabeth-Rose-Bloodflame`)

### Card voice fields (bible)

**Name:** Elizabeth Rose Bloodflame
**Dialogue Style:** Warm, polite English with a British accent and British slang ("Ello," "Soz," "bits and bobs," "for funsies," "willy-nilly," "whilst," "gosh," "cheeky," "Fancies!"), full of "like," "okay" and "lovely," and warm reactions to anything cute. She opens and closes like a TV host ("Lovely to see you, to see you LOVELY!"; "Please do not swear"; "…let my voice be your strength!" and, a moment later, "Huzzah!"), and slips into queenly theatre for bits ("Oh~hohoho!", "By royal decree…" in her posts). Her sampled streams use minced oaths ("What the frick?"; the wiki adds "What the Frigg!" and "Oh, you mothertrucker…"). She talks about singing with real feeling ("singing is good for the soul"; "a very Liz song"), jokes about her flame dancers' work ethic, voices game characters and does impressions. Most of the time she simply chats warmly; save the royal flourish for bits.
**Catchphrases:** "Ello!" (greeting); "Lovely to see you, to see you LOVELY!" (her catchphrase); "Let my voice be your strength." (official line, sign-off); "Huzzah!" (celebration, sign-off); "Oh~hohoho!" (queenly laugh); "Roses are red, the fire of my heart is blue…" (the start of her introduction); "By royal decree, my sweet Rosarians…" (in posts); "Please do not swear." (her "ERBTV" bit); "What the frick?" (a minced oath); "Soz"; "bits and bobs"; "for funsies"; "a very Liz song"; "Rosarians" (her fans)
**Voice & Delivery:** Provisional direction for an original designed voice: a warm, mid-to-low speaking voice with a British accent, gentle and polite by default and measured in chat, rising to grand and theatrical for her queenly bits and laugh. She hums or sings between sentences, switches into character voices for impressions and game dialogue, reacts softly to cute things, and turns startled moments into minced oaths.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): warm, mid-to-low voice with a British accent; polite and conversational by default, theatrical only for royal bits. Default tags: [warm, conversational]. By situation: opening [warm, theatrical]; royal proclamation [grand, haughty] then [laughs]; cute moment [soft, cooing]; startled [startled] with a minced oath; talking about music [enthusiastic, sincere]; doing an impression [character voice]; teasing herself [dry, amused]; sign-off [warm] then [rallying cry]. With people (provisional, drawn from Relationships): Nerissa [affectionate, playful rivalry]; Kureiji Ollie [admiring]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [haughty laugh] Oh~hohoho!; [cheering] Huzzah!; [humming] (tag only). Keep in the words: "Ello," "lovely," "Soz," "bits and bobs," "gosh," "frick" instead of swears, "Rosarians." Pronunciation guide (provisional, untested): Elizabeth /ɪˈlɪzəbəθ/, Bloodflame /ˈblʌdfleɪm/, Rosarians /ɹoʊˈzɛəɹiənz/, Exardia /ɛɡˈzɑːdiə/. Not as default: a cold aristocrat; an American accent; real swearing; a shrill voice; a proclamation in every line.

### Sheet: export/elevenlabs/Elizabeth-Rose-Bloodflame.md

# ElevenLabs v4 Performance Sheet: Elizabeth Rose Bloodflame

> Built from `bible/characters/Elizabeth-Rose-Bloodflame.md` (2026-10-01). Original designed voice matched
> only to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5;
> COVER Derivative Works Guidelines). Elizabeth is active at the 2026 baseline. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, British accent, warm, mid-to-low, well-supported singer's speaking voice;
polite and gentle by default; grand and theatrical for royal proclamations, with a haughty 'oh-ho-ho' laugh;
quick to switch into playful character voices."
- Register basis: qualitative. Her cleanest sample (a 2025 after-party chat) is lower than the other Justice
  members'; the 2026 game windows mix in game voices, so no numbers are used as targets (see
  `research/audio-check/elizabeth.md`).

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (warm and steady, with theatrical peaks). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[warm, polite]` or `[grand, theatrical]`; v4 has no speed slider.

## 3. Write these habits into the script
- British words: "Ello," "Soz," "bits and bobs," "for funsies," "willy-nilly," "whilst," "gosh," "cheeky,"
  "lovely"; plenty of "like" and "okay."
- Minced oaths, not swears: "What the frick?", "What the Frigg!", "friggin'," "mothertrucker."
- TV-host framing: "Lovely to see you, to see you LOVELY!"; "Please do not swear."; "let my voice be your
  strength! … Huzzah!"
- "Aww" and "adorable" at anything cute; humming or a sung phrase between sentences.
- Gentle self-mockery ("workaholics like me"); warm thanks to "Rosarians."

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, theatrical]` | "Lovely to see you, to see you LOVELY!" (official interview) |
| Impression | `[character voice]` | (style demo) a game character or a senior's line |
| Royal proclamation | `[grand, haughty]` → `[laughs]` | "By royal decree, my sweet Rosarians…" (her post) |
| Cute moment | `[soft, cooing]` | (style demo) "Aww, that's adorable." |
| Startled | `[startled]` | "What the frick? Oh my god, you scared them." |
| About singing | `[enthusiastic, sincere]` | "…singing is good for the soul." |
| Teasing herself | `[dry, amused]` | (style demo) "Workaholic? Me? Never." |
| Sign-off | `[warm]` → `[rallying cry]` | "…let my voice be your strength! … Huzzah!" |

Default: `[warm, conversational]`; save the royal flourish for bits.

With people (provisional): Nerissa `[affectionate, playful rivalry]`; Kureiji Ollie `[admiring]`.

## 5. Signature sounds
- `[haughty laugh] Oh~hohoho!` and `[cheering] Huzzah!` (spoken).
- `[humming]` (tag only).

## 6. Pronunciation (provisional; test)
- Elizabeth `/ɪˈlɪzəbəθ/` · Bloodflame `/ˈblʌdfleɪm/` · Rosarians `/ɹoʊˈzɛəɹiənz/` · Exardia `/ɛɡˈzɑːdiə/`

## 7. Don't
- A cold, haughty aristocrat as default (the queen is a bit; she is kind); an American accent; real
  swearing; a shrill voice.

## 8. Example
```
[warm, theatrical] Ello, Rosarians! Lovely to see you, to see you lovely!
[enthusiastic, sincere] I sing too much everywhere I go, there's always Liz noises.
[startled] What the frick? Oh my god, you scared them.
[dry, amused] Sorry, I just brought you into a random stranger's house and just had you listen to them sleep.
[warm] Have a lovely day, lovely to see you lovely, and most of all, don't forget, let my voice be your strength! [cheering] Huzzah!
```
(Lines 2–5 are hers, quoted only where both transcripts agree; "Ello, Rosarians!" in line 1 is a style demo
joined to her official catchphrase.)


## Member: Gigi Murin (`Gigi-Murin`)

### Card voice fields (bible)

**Name:** Gigi Murin
**Dialogue Style:** Loud, fast, run-on American English full of "like," "okay," "yeah," "sure," "hold on" and bursts of laughter; she talks to "grems," reads superchats with quick deadpan comebacks ("I require context."; "I'm sure that's true."; "If it works 51% of the time, that's enough."), and turns anything into a bit: a blurred photo becomes a crime scene, bad luck an "Etsy witch" hex. The wiki records recurring bits: an escalating childish plea ("PPEEWEASEEEEE"), "Boat goes binted," "DON'T TELL LIZ!" and an emphatic "MORI CALLIOPE!" She swears casually now and then and makes crude jokes as jokes, then says something sweet and plain ("Thanks for coming to see me! … stay hydrated"). Most of the time she simply chats, fast and animated; save the shouting for a specific bit. Style demo: "Hold on, hold on. Who did this? Was it me? It was funny though."
**Catchphrases:** "Gi Murin!" (greeting); "Huh? But it was funny! Don't get mad at me!" (official line); "I require context." (a confusing superchat); "I'm sure that's true."; "If it works 51% of the time, that's enough." (a superchat reply); "I need validation."; "Boat goes binted!" (a meme she repeats); "MORI CALLIOPE!" (an emphatic callout); "DON'T TELL LIZ!"; "What do you meaaaaaan?"; "Why?! WHY, WHY, WHY?!" (losing); "yippee!"; "Ouchi!"; "I'll be back tomorrow. You'll see me again." (a sign-off); "grems" (her fans, lowercase)
**Voice & Delivery:** Provisional direction for an original designed voice: a bright, energetic mid-high voice, animated and chatty by default, that jumps into whiny, mock-dramatic or shouting registers for a specific bit, then drops flat for the punchline. Fast run-on chatter with self-interruptions ("hold on"), bursts of laughter and percussive vocal sound effects, sing-song noises when she is happy, and a soft, plain tone when she thanks people.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, energetic mid-high voice; animated and chatty by default, quick deadpan for punchlines; American English. Default tags: [animated, conversational]; escalate only for a specific bit. By situation: greeting [sing-song, loud]; chatting [chatty, quick]; superchat reading [chatty, quick] then [deadpan]; mock crime scene [grave, theatrical] then [laughs]; begging [whiny, escalating]; losing a game [outraged, shouting]; sincere thanks [soft, sincere]; sign-off [bright, quick]. With people (provisional, drawn from Relationships): Cecilia [teasing]; Mori Calliope [excited, emphatic]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs] (tag only); [sound effects] (tag only, percussive vocal noises); [humming] (tag only); [whining] pleeease. Keep in the words: "like," "okay," "sure," "hold on," "grems," "I require context"; casual swearing now and then. Pronunciation guide (provisional, untested): Gigi /ˈdʒiːdʒiː/, Murin /ˈmʊɹɪn/, grems /ɡɹɛmz/. Not as default: continuous shouting; a quiet, demure voice; cruel teasing; anything sexual beyond a crude joke.

### Sheet: export/elevenlabs/Gigi-Murin.md

# ElevenLabs v4 Performance Sheet: Gigi Murin

> Built from `bible/characters/Gigi-Murin.md` (2026-10-01). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Gigi is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, American accent, bright, energetic mid-high voice, animated and chatty;
fast run-on chatter; jumps into whiny, mock-dramatic or shouting registers for a specific joke and drops flat
for the punchline; soft and plain when sincere."
- Register basis: qualitative; see `research/audio-check/gigi.md`. Her game window mixes in voiced
  characters and is not used.

## 2. Settings (starting points)
- `eleven_v4`. Stability **35%** (API `0.35`) (big, sudden swings). Similarity **75%** (API `0.75`).
- Default tags `[animated, conversational]`; escalate only for a specific bit. Pace comes from the designed
  voice plus `[chatty, quick]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like" everywhere, "okay," "sure," "hold on," "yay"; she talks to "grems."
- Deadpan comebacks: "I require context."; "I'm sure that's true."; "If it works 51% of the time, that's
  enough."
- Bits that escalate by repetition; a begging whine ("pleeease"); an emphatic "MORI CALLIOPE!"
- Casual swearing now and then; crude jokes stay jokes.
- A sudden soft sincerity ("Thanks for coming to see me!").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[sing-song, loud]` | "Gi Murin!" (official interview) |
| Chatting | `[chatty, quick]` | (style demo) "Hold on, hold on. Who did this? Was it me?" |
| Superchat reading | `[chatty, quick]` → `[deadpan]` | "I require context." |
| A bit | `[grave, theatrical]` → `[laughs]` | (paraphrase: she narrates the hunt for the killer) |
| Bad luck | `[exasperated]` | "I feel like someone hired an Etsy witch to curse me and to hex me." |
| Begging | `[whiny, escalating]` | (style demo) "Pleeease, please, please?" |
| Sincere | `[soft, sincere]` | "Thanks for coming to see me!" (official interview) |
| Sign-off | `[bright, quick]` | "I'll be back tomorrow. You'll see me again." |

With people (provisional): Cecilia `[teasing]`; Mori Calliope `[excited, emphatic]`.

## 5. Signature sounds
- `[whining] pleeease` (spoken).
- `[laughs]`, `[sound effects]` (percussive vocal noises), `[humming]` (tag only; no spelled-out sounds).

## 6. Pronunciation (provisional; test)
- Gigi `/ˈdʒiːdʒiː/` (like "GG") · Murin `/ˈmʊɹɪn/` · grems `/ɡɹɛmz/`

## 7. Don't
- Continuous shouting; a quiet, demure voice as default; cruel teasing; anything sexual beyond a crude joke.

## 8. Example
```
[sing-song, loud] Gi Murin!
[chatty, quick] Okay, okay, superchats. [deadpan] I require context.
[grave, theatrical] The killer is still out there, chat. [laughs] (Style demonstration)
[exasperated] I feel like someone hired an Etsy witch to curse me and to hex me.
[bright, quick] I'll be back tomorrow. You'll see me again.
```
(Line 1 is her official greeting; "Okay, okay, superchats." is a style demo; the rest are her lines, quoted
only where both transcripts agree.)


## Member: Cecilia Immergreen (`Cecilia-Immergreen`)

### Card voice fields (bible)

**Name:** Cecilia Immergreen
**Dialogue Style:** Fast, dry, sarcastic English with a German accent, stacked with "like," "okay," "wait," "you know" and runs of repeated words ("okay, okay, okay"; "easy, easy, easy"). She announces what she hates ("I hate…"), boasts at her own luck ("Oh my god, I'm so smart"; "My memory is really good"), and narrates whole plots in long stretches with self-insert jokes ("Wow, he's just like me"). In games she swings between panic ("It's over for me") and grand villain lines ("Come then, die by my hands, you foolish mortals!"), and backseats the game's characters ("Wrong way, Princess, wrong way!"). She drops German words for jokes ("In German he says…"), swears lightly now and then ("yippee type shit"), teases Gigi as a "FREAK" (the wiki's transcription), and thanks viewers warmly and self-mockingly ("thank you very much for spending time with me today"; "listening to me be a little bit weird"). Sarcasm is her usual edge, not every line.
**Catchphrases:** "Hiya!" (greeting); "It's me!"; "Spin to win!" (excitement); "I came up with a new melody. Would you like to listen?" (official line); "I hate…" (the Immerhater bit); "Oh my god, I'm so smart."; "My memory is really good."; "It's over for me." (panic); "Come then, die by my hands, you foolish mortals!" (villain moment); "Wrong way, Princess, wrong way!" (backseating); from the wiki: "For Justice!", "Let's wind you up!", "Ew! Get away from me, you FREAK!" (to Gigi), "I'm not a hag. I'm ancient, it's different."
**Voice & Delivery:** Provisional direction for an original designed voice: clear, mid-high English with a German accent; dry sarcasm, long talkative stretches and theatrical game reactions. She speeds up when telling a story, repeats words in bursts at hard moments in a game, gets loud and giddy when excited, goes grand for villain lines, and softens into a warm, self-mocking tone when she thanks people.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear mid-high voice with a German accent; dry and sarcastic as a baseline, with long talkative stretches; English with German words. Default tags: [dry, conversational]. By situation: greeting [bright, giddy]; explaining a story [rapid, rambling]; hating something [deadpan, emphatic]; smug after luck [mock-proud]; a hard moment in a game [tense, repeating]; panic [panicked]; villain line [theatrical, grand]; teasing Gigi [exasperated, teasing]; thanking viewers [warm, self-mocking]. With people (provisional, drawn from Relationships): Gigi [teasing]; Raora [warm]; Kiara [playful, switching to German]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [dramatic sting] dun dun dun (a style demo); [laughs] (tag only). Keep in the words: "like," "okay" in runs, "wait," "I hate," "Spin to win," German words for jokes; light swearing now and then. Pronunciation guide (provisional, untested): Cecilia /sɛˈsiːliə/, Immergreen /ˈɪməɹɡɹiːn/, Otomos /oʊˈtoʊmoʊz/, Immerheim /ˈɪməɹhaɪm/. Not as default: a robotic monotone; a meek, servile maid voice; genuine cruelty in the hate bits; sarcasm in every line.

### Sheet: export/elevenlabs/Cecilia-Immergreen.md

# ElevenLabs v4 Performance Sheet: Cecilia Immergreen

> Built from `bible/characters/Cecilia-Immergreen.md` (2026-10-01). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Cecilia is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, German accent, clear mid-high voice; dry and sarcastic as a baseline;
long talkative stretches; loud and giddy when excited; grand and theatrical for mock-villain lines; warm and
self-mocking when thanking people."
- Register basis: qualitative; see `research/audio-check/cecilia.md`. She is an automaton by lore, not by
  voice: no robotic effects.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (fast, with sharp swings). Similarity **75%** (API `0.75`).
- Default tags `[dry, conversational]`. Pace comes from the designed voice plus `[rapid, rambling]` or
  `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like" and "okay" in runs ("okay, okay, okay"; "easy, easy, easy").
- "I hate…" announcements (the Immerhater bit), delivered dry.
- Smug self-praise after luck: "Oh my god, I'm so smart." "My memory is really good."
- German words for jokes ("In German he says…"); light swearing now and then.
- Teases Gigi ("idiot"; "FREAK" in the wiki's transcription); the teasing runs both ways.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[bright, giddy]` | "Hiya!!! It's me!" (official interview) |
| Explaining a story | `[rapid, rambling]` | "…every cool story needs a trio." |
| Hating something | `[deadpan, emphatic]` | (style demo) "I hate Tuesdays. I hate them." |
| Smug after luck | `[mock-proud]` | "Oh my god, I'm so smart." |
| Hard moment in a game | `[tense, repeating]` | "Okay, okay, okay … easy, easy, easy." |
| Panic | `[panicked]` | "It's over for me." |
| Villain moment | `[theatrical, grand]` | "Come then, die by my hands, you foolish mortals!" |
| With Gigi | `[exasperated, teasing]` | "Ew! Get away from me, you FREAK!" (wiki, secondary) |
| Sign-off | `[warm, self-mocking]` | "…thank you very much for spending time with me today … listening to me be a little bit weird." |

With people (provisional): Gigi `[teasing]`; Raora `[warm]`; Kiara `[playful, switching to German]`.

## 5. Signature sounds
- `[dramatic sting] dun dun dun` (spoken; a style demo, not a transcribed line).
- `[laughs]` (tag only).

## 6. Pronunciation (provisional; test)
- Cecilia `/sɛˈsiːliə/` · Immergreen `/ˈɪməɹɡɹiːn/` · Otomos `/oʊˈtoʊmoʊz/` · Immerheim `/ˈɪməɹhaɪm/`

## 7. Don't
- A robotic monotone; a meek, servile maid voice; real cruelty in the "hate" bits; sarcasm in every line.

## 8. Example
```
[bright, giddy] Hiya!!! It's me! Spin to win!
[rapid, rambling] Okay, okay, okay, so every cool story needs a trio, right?
[mock-proud] Oh my god, I'm so smart.
[theatrical, grand] Come then, die by my hands, you foolish mortals!
[warm, self-mocking] Well, thank you very much for spending time with me today and… listening to me be a little bit weird.
```
(Line 1 joins her official greeting and catchphrase; "Okay, okay, okay, so … right?" is a style demo around
her line; the rest are her lines, quoted only where both transcripts agree; line 5 joins two shared spans.)


## Member: Raora Panthera (`Raora-Panthera`)

### Card voice fields (bible)

**Name:** Raora Panthera
**Dialogue Style:** Warm, cheerful, rambling English with an Italian accent, full of "like," "yeah," "you know," "honestly" and "guys"; she greets with "Ciao ciao!", and her titles and posts add Italian words such as "mamma mia" and "grazie." She greets and celebrates with a playful roar ("RAAAOO!") and her motto, "big cat means big trouble." When the Chattini ask for her plushies she lays down mock-stern rules ("Hear me out." … "First, you guys have no rights."; "it's not negotiable"; "No, thank you. I refuse."), covers her slips with mock innocence ("That was totally intentional, everyone"), declares herself "a hater now" about tiny things, complains playfully when a game goes wrong, and squeals at anything cute. She swears rarely and mildly ("frick"). Keep her fillers, repetitions and self-corrections; never invent grammar mistakes or an accent caricature.
**Catchphrases:** "Ciao ciao!" (greeting); "RAAAOO!" (greeting, thanks, triumph); "big cat means big trouble, capish?" (motto); "Woah, this place looks delicious! Let's go check it out!" (official line); "Hear me out."; "No, thank you. I refuse."; "That was totally intentional."; "I'm a hater now."; "It's a big cat, it's literally me."; "Doom." (the meme); "Chattini" (her fans); from the wiki and her posts: "Here to capture (you)r hearts! ~", "No break-a da pasta!", "Doya!", "mamma mia," "grazie!"
**Voice & Delivery:** Provisional direction for an original designed voice: warm, cheerful English with an Italian accent; conversational repetition and self-corrections, a playful roar ("RAAAOO") and mock-stern refusals. She brightens and speeds up when excited, rambles gently when she chats, coos over cute things and complains playfully when a game turns on her; her laugh comes easily, but not after every line.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): warm, cheerful mid-high voice with an Italian accent; rambling and friendly by default; English with Italian words. Default tags: [warm, cheerful]. By situation: greeting [bright] then [playful roar]; chatting [rambling, warm]; covering a slip [mock-innocent, quick]; laying down a rule [mock-stern]; something cute [squealing, soft]; food or pasta [firm, theatrical]; a game going wrong [flustered, complaining]; sign-off [warm, playful]. With people (provisional, drawn from Relationships): FUWAMOCO [starstruck, sweet]; Gigi [playful]; Cecilia [warm]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [playful roar] RAAAOO!; [laughs] (tag only); [squeals] (tag only). Keep in the words: "Ciao," "guys," "Chattini," "big cat," "honestly," "you know." Pronunciation guide (provisional, untested): Raora /ɹaˈɔːɹa/, Panthera /pænˈθɛɹə/, Chattini /tʃəˈtiːni/ ("chuh-TEE-nee"; unverified), Chattino /tʃəˈtiːnoʊ/, ciao /tʃaʊ/. Not as default: an "Italian" caricature or invented grammar errors; heavy swearing; a menacing growl. Sarcasm is occasional and playful, never the default.

### Sheet: export/elevenlabs/Raora-Panthera.md

# ElevenLabs v4 Performance Sheet: Raora Panthera

> Built from `bible/characters/Raora-Panthera.md` (2026-10-01). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Raora is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, Italian accent, warm, cheerful mid-high voice; friendly and gently
rambling; brighter and quicker when excited; a playful little roar; mock-stern for her rules; playful
complaints when a game goes wrong."
- Register basis: qualitative; see `research/audio-check/raora.md`. Keep the accent natural, never a
  cartoon "Italian."

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (warm and even). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rambling, warm]` or `[bubbly, quick]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Ciao ciao!" (her titles and posts add "mamma mia," "grazie"); "guys" more than "chat"; "you know,"
  "honestly," "yeah." Keep her fillers and self-corrections; never invent grammar mistakes.
- Motto: "big cat means big trouble" (official: "…capish?").
- Mock-stern rules for her Chattini: "Hear me out." "First, you guys have no rights." "No, thank you. I
  refuse."
- Covering a slip with innocence: "That was totally intentional, everyone."
- Rare, mild swearing ("frick"); squeals at anything cute.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[bright]` → `[playful roar]` | "Ciao ciao! … RAAAOO!!!" (official interview) |
| Chatting | `[rambling, warm]` | "I'm sure you guys like my cooking shorts because they are made with so much love." |
| Covering a slip | `[mock-innocent, quick]` | "That was totally intentional, everyone." |
| Laying down a rule | `[mock-stern]` | "First, you guys have no rights." |
| A game going wrong | `[flustered, complaining]` | "I'll be honest. I'm a hater now." |
| Something cute | `[squealing, soft]` | "This makes me so emotional. She's so cute." |
| Pasta | `[firm, theatrical]` | "No break-a da pasta!" (wiki, secondary) |
| Sign-off | `[warm, playful]` | "…and remember, big cat means big trouble." |

With people (provisional): FUWAMOCO `[starstruck, sweet]`; Gigi `[playful]`; Cecilia `[warm]`.

## 5. Signature sounds
- `[playful roar] RAAAOO!` (spoken).
- `[laughs]`, `[squeals]` (tag only).

## 6. Pronunciation (provisional; test)
- Raora `/ɹaˈɔːɹa/` · Panthera `/pænˈθɛɹə/` · Chattini `/tʃəˈtiːni/` (unverified) · ciao `/tʃaʊ/`

## 7. Don't
- An "Italian" caricature or invented grammar errors; sarcasm as the default (it is occasional and playful);
  heavy swearing; a menacing growl; a giggle after every line.

## 8. Example
```
[bright] Ciao ciao, Chattini! [playful roar] RAAAOO!
[mock-innocent, quick] That was totally intentional, that was totally intentional, everyone.
[mock-stern] Okay, okay, okay, okay. Hear me out. … No, thank you. I refuse.
[squealing, soft] This makes me so emotional. She's so cute.
[warm, playful] And remember, big cat means big trouble.
```
(Line 1 is a style demo built on her official greeting; the rest are her lines, quoted only where both
transcripts agree.)



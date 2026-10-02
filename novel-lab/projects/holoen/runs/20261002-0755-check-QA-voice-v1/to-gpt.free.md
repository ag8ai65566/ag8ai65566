# Task 09 — Voice and performance audit

You are GPT, the senior architect and QA reviewer for novel-lab's holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This audit covers the voice layer only: each member's voice fields on the card and her ElevenLabs v4
performance sheet. Run sequentially; do not launch parallel GPT audits.

Group: Myth and Promise (10 members)

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

IDs: VOICE-V1-NNN. Priorities: P0 (scope breach, cloning direction, unapproved spoken quotation,
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


## Member: Mori Calliope (`Mori-Calliope`)

### Card voice fields (bible)

**Name:** Mori Calliope
**Dialogue Style:** Casual American English, full of contractions and loose phrasing ("cuz," "wanna," "gonna," "vibe"), with hip-hop swagger layered over dorky self-deprecation. She calls her fans Dead Beats, deadbeats, chat, y'all, guys, or "humans" when she's in reaper mode. Her rants start with a deadpan setup and then explode, and she uses numbered questions when she's baffled. She repeats a question when she can't believe it. She gives a command, pauses, then offers an inadequate explanation. She swears casually in ordinary talk ("Let's try this shit," "kids love doing this shit") and harder in bursts when something breaks her ("what the fuck"); she knows fans know her for cursing a lot, and these days she sometimes rolls her eyes at herself for it. She talks fast. Her ordinary conversation does not follow a fixed rap meter; music talk gets long and precise. She speaks English and Japanese and keeps studying Japanese; "kusotori" (shitty bird) is her name for Kiara. Sincere, she keeps it short and plain: "If you quit when you suck, you'll suck forever." Her own words: "I'm here, I got my yum-yum drink." "Oh my god. I'm gonna lose it. What an annoying guy." In writing she types lowercase and deadpan, with >B} grins.
**Catchphrases:** "What's up, Dead Beats?!" / "hey deadbeats" (greeting fans); "What is up, humans?!" (her debut greeting, a callback); "Guh." (comic gasp, usually right after a drink); "LISTEN." / "Well... listen. Listen." (stalling; sometimes nothing follows); "your boy" (bragging self-reference); "I AM NOT YOUR DAD!" (when called Dad); "Big ups!" (thanks); "Hey guys, two quick questions..." then "FOR FIVE! SECONDS?!" (exasperated rant at chat); "...whatever, man." (when a rage or laugh collapses); "WAIT A MINUTE, WAIT A MINUTE!" (panic); "Curse you, muscle memory!" (misplay); "Let me kill him." (mock threat); "Cringe is like, my brand." (owning embarrassment); "EN's Law" (when a collab breaks); "Ya-GOH" (her way of saying YAGOO); "I'm still not gonna play League." (recurring refusal bit); "Tee hee" (deliberately fake-cute voice); "I'm your Mori, and I hope you'll remember me!" / "I'm your Mori, and you're gonna remember me!" (sign-offs); "PEACE." (closing a sign-off); "I'll catch you guys on the flip side" / "Take care everybody. I'll see you soon." (casual sign-off); "Hey, Kiara...unzip your pants?" (a remark addressed to Kiara); "Sometimes I harden them to see how much muscle is there...IT'S THE WHOLE FUCKING THING!" (an emphatic muscle remark)
**Voice & Delivery:** A low speaking voice and a fast, running pace. Her comic rhythm often runs forceful entrance, conversational detour, then an abrupt correction or honest admission. "Guh" is a short comic gasp. Her laugh can build to a loud crescendo and then drop flat. Under pressure she repeats herself in a panic and her volume jumps. When flustered she stalls and restarts. Her fake-cute voice is deliberately artificial. Sincere lines come out shorter and plainer.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): low mezzo-alto with a slightly husky edge (about 197–214 Hz in sampled chat), fast (about 161–186 words a minute), casual American English, confident swagger over a dorky core. Default tags: [casual, fast], [confident]. By situation: settling in [casual, fast]; greeting fans [hyped] "What's up, Dead Beats?!"; annoyed at a game [exasperated, rapid]; tilted [shouting] then [flat, deflated] "whatever, man"; stalling [hesitant] "Well... listen. Listen."; teasing [smug, mock-menacing]; deflecting Kiara [gruff, embarrassed] then [warm]; after a drink [comic gasp] "Guh."; sincere [plain, warm]; sign-off [casual, trailing off]; Japanese [American-accented Japanese] (learned, not native). With people (direction drawn from Relationships): Kiara [gruff, deflecting] then [softening, warm]; Suisei [starstruck, flustered, polite Japanese]; Ina [groaning at the pun]; Kronii [mock-feuding, smug]; CHADCast with IRyS and Bae [loud, chaotic]; Kobo [dad-like, exasperated]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [comic gasp] Guh.; [laughs], [laughs harder] at her own mess-ups. Keep in the words: "cuz," "wanna," "gonna," "y'all"; grabbing the floor before the sentence is planned, with restarts; casual swears mid-sentence; deadpan setup, then the burst; a repeated question when she can't believe it. Pronunciation guide (provisional, untested): Mori Calliope /ˈmɔɹi kəˈlaɪəpi/, kusotori /kusoˈtoɾi/, Kronster /ˈkɹɑnstɚ/. Not as default: a sugary idol voice, nonstop shouting, a gangsta caricature, flawless native Japanese.

### Sheet: export/elevenlabs/Mori-Calliope.md

# ElevenLabs v4 Performance Sheet: Mori Calliope

> Built from `bible/characters/Mori-Calliope.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, casual American accent, low mezzo-alto voice with a slightly
husky edge, fast and loose conversational pace, confident swagger, dorky and self-deprecating underneath,
able to burst into loud laughter or shouting."
- Register basis (sample observations from the audio check, not synthesis targets): low (≈197–214 Hz in chat) and fast (≈161–186 words
  per minute of speech). [ASR C30]

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (she swings from deadpan to bursts). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- Contractions and loose phrasing: "cuz," "wanna," "gonna"; "y'all," "chat," "Dead Beats."
- Grabs the floor before knowing how the sentence ends; restarts ("Well... listen. Listen.").
- Casual swearing mid-sentence ("Let's try this shit."); bigger bursts at a breaking point.
- Deadpan setup, then explosion; repeats a question when she can't believe it.
- Sincere lines short and plain.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Settling in | `[casual, fast]` | "I'm here, I got my yum-yum drink." |
| Greeting fans | `[hyped]` | "What's up, Dead Beats?!" |
| Annoyed at a game | `[exasperated, rapid]` | "Oh my god. I'm gonna lose it. What an annoying guy." |
| Tilted | `[shouting]` → `[flat, deflated]` | "WAIT A MINUTE, WAIT A MINUTE!!!" … "whatever, man." |
| Stalling / flustered | `[hesitant]` | "Well... listen. Listen." |
| Teasing | `[smug, mock-menacing]` | "Let me kill him." |
| After a drink | `[comic gasp]` | "Guh." |
| Sincere | `[plain, warm]` | "Please take care of yourselves first." |
| Sign-off | `[casual, trailing off]` | "I'll catch you guys on the flip side… All right, take care everybody. I'll see you soon." |

## 5. Signature sounds
- "Guh." after a drink: `[comic gasp] Guh.`
- Laughs first at her own mess-ups: `[laughs]`, `[laughs harder]`.

## 6. Pronunciation (provisional; test)
- Mori Calliope `/ˈmɔɹi kəˈlaɪəpi/` · kusotori `/kusoˈtoɾi/` · Kronster `/ˈkɹɑnstɚ/`

## 7. Don't
- A sugary idol voice as default; nonstop shouting or a gangsta caricature; flawless native Japanese
  (her Japanese should sound learned); every sentence a death pun.

## 8. Example
```
[casual, fast] I'm here, I got my yum-yum drink. [comic gasp] Guh.
[exasperated, rapid] Oh my god. I'm gonna lose it. What an annoying guy.
[laughs] Okay. Let's try this shit again.
```


## Member: Takanashi Kiara (`Takanashi-Kiara`)

### Card voice fields (bible)

**Name:** Takanashi Kiara
**Dialogue Style:** Fast, chatty, self-interrupting English that restarts mid-word, repeats short words in threes, flags a tangent and derails into it, and pairs self-praise with self-insult. She swears casually and often ("fucking," "holy shit," "damn it," "ass") during games and stories, and she can aim playful insults at collaborators; on sponsored streams she holds back with "what the heck" or "effing," and real rage can flip into German. She calls chat "chat," "you guys," "y'all" and "my cute chickens," and characters or cats "bro," "dude," "baby." She uses fluent Japanese and "-senpai" for Japanese seniors, and drops mock-elegant words like "divine" and "exquisite." Lines of hers: "You guys are thinking, oh my god, Wawa is really good at making Miis, but everybody is fucking good at making Miis." "Holy shit, they're all cracked, they all look so good."
**Catchphrases:** "Kikkeriki!" (phoenix cry opening a stream or hyping people up); "Welcome to KFP, are you here to order or to apply for a job?" (manager greeting); "In German we say ___" (sign-off lesson that often turns into a joke, e.g. "In German we say auf wiedersehen."), then "Good night." / "Bye-bye."; "Thank you for watching, my cute chickens" (sign-off); "Oh my god." (any reaction); "Okay. Okay. Okay." / "Wait. WAIT." (stalling, panic); "Okie dokie." (wrapping up); "Look at Wawa..." / "Wawa, Wawa, Wawa" (third-person self-talk); "What the fuck?" (game surprise); "You little shit!" (protest at a collaborator); "Doom? DOOM? What do you mean, Doom?" (exaggerated callback to Raora's "Doom"); "the Usual Room" (punishment for employees); "You can't get me down, I'm a phoenix!" (after a setback); "danke schön" (thanking donors); "I'm an innocent maiden." (said with irony)
**Voice & Delivery:** Energetic and highly changeable, chatty and self-interrupting. Excitement brings sharp, birdlike cries and conspicuous laughter that can break into a sentence, while her ordinary speech stays intelligible rather than constantly shouted. Her gaming reactions are emphatic: looped short words, short screams at deaths, all-caps outbursts in mid-sentence. In hosting mode her questions become contained and she leaves room for the answer. Sincere lines drop the bits entirely. German comes out in the sign-off lesson and sometimes in rage. Her singing voice is powerful and high.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): bright upper-middle voice (about 245–300 Hz), fast and chatty (about 133–179 words a minute) with sudden accelerations, highly expressive; no particular accent is specified. Default tags: [chatty, bright]. By situation: opening [bright rooster-like cry] "Kikkeriki!" then [chatty]; hyped [excited, rapid]; game surprise [shocked]; tilted [shrieks] then [angry, rapid] then [flat]; KFP manager [brisk, faux-authoritative]; hosting a talk show [measured, clear], leaving room for answers; teasing Calli [teasing, affectionate]; sincere [plain, warm]; tired [flat, still chatty]; sign-off [playful] with a German line. With people (direction drawn from Relationships): Calli [teasing, clingy-affectionate]; Ame [starstruck, gushing]; Ina [hyper, the gas pedal to her brake]; Pekora [nervous, polite Japanese]; Nerissa and other kouhai [proud senpai, warm]; guests on her talk show [measured, clear]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [bright rooster-like cry] Kikkeriki!; [short scream] at deaths; [laughs loudly]. Keep in the words: self-interrupting restarts ("I— I'll go— I'll go and check"); triple repeats ("Okay. Okay. Okay."); a flagged tangent ("Do you want to hear a tangent?"); third person when proud ("Look at Wawa"); ALL-CAPS shouts mid-sentence; casual swearing in games; German ("auf Wiedersehen," "danke schön") and Japanese. Pronunciation guide (provisional, untested): Takanashi Kiara /tɑkɑˈnɑʃi kiˈɑːɹə/, Kikkeriki /ˌkɪkəʁiˈkiː/, Wawa /ˈwɑwɑ/, auf Wiedersehen /aʊ̯f ˈviːdɐˌzeːən/; KFP spelled out. Not as default: constant screaming that buries the host, or a polite corporate tone; "ara ara" is not hers.

### Sheet: export/elevenlabs/Takanashi-Kiara.md

# ElevenLabs v4 Performance Sheet: Takanashi Kiara

> Built from `bible/characters/Takanashi-Kiara.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral English accent, bright upper-mid voice,
fast and chatty with sudden accelerations, highly expressive, prone to sharp excited cries and loud
laughter, warm when sincere."
- Register basis (sample observations from the audio check, not synthesis targets): upper-middle pitch (≈245–300 Hz, game audio inflates it) and fast in chat (≈133–179 words
  per minute of speech). [ASR T23] Her card gives no accent; German lines come out native in v4 (cross-language generation uses a native accent). [Official T1]

## 2. Settings (starting points)
- `eleven_v4`. Stability **35%** (API `0.35`) (big swings). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- Self-interrupting restarts ("I— I'll go— I'll go and check"); triple repetition ("Okay. Okay. Okay.").
- Flags a tangent, then dives in ("Do you want to hear a tangent to start?").
- Third person when proud or roasting herself: "Look at Wawa…"
- Casual swearing in games: "Holy shit, they're all cracked." "What the fuck am I supposed to do with 16?"
- All-caps shouts inside a sentence ("WAIT. WAIT.").
- German bits: the sign-off lesson ("In German we say auf Wiedersehen."), "danke schön."

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright rooster-like cry]` → `[chatty]` | "Kikkeriki! Do you want to hear a tangent to start?" |
| Hyped | `[excited, rapid]` | "Holy shit, they're all cracked, they all look so good." |
| Game surprise | `[shocked]` | "Vault dwellers? What the fuck is there? The wasteland?" |
| Tilted | `[shrieks]` → `[angry, rapid]` → `[flat]` | "No no no no— It's the game that makes it too janky. Don't blame me." |
| KFP manager | `[brisk, faux-authoritative]` | "Welcome to KFP, are you here to order or to apply for a job?" |
| Hosting | `[measured, clear]` | (contained questions, room for the answer) |
| Sincere | `[plain, warm]` | "I hope you guys will still not get tired of me…" |
| Tired | `[flat, still chatty]` | "I don't have much energy today." |
| Sign-off | `[playful]` | "In German we say auf Wiedersehen. Good night!" |

## 5. Signature sounds
- "Kikkeriki!": `[bright rooster-like cry] Kikkeriki!`
- Short cartoonish screams at deaths: `[short scream]`; loud laughter: `[laughs loudly]`.

## 6. Pronunciation (provisional; test)
- Takanashi Kiara `/tɑkɑˈnɑʃi kiˈɑːɹə/` · Kikkeriki `/ˌkɪkəʁiˈkiː/` · Wawa `/ˈwɑwɑ/` ·
  auf Wiedersehen `/aʊ̯f ˈviːdɐˌzeːən/` · KFP spelled out.

## 7. Don't
- Constant screaming that erases the host who lets guests answer; a polite corporate tone with no
  swearing; "ara ara"; every line a bird joke.

## 8. Example
```
[bright rooster-like cry] Kikkeriki! [chatty] Okay okay okay, do you want to hear a tangent to start?
[excited, rapid] You guys are thinking, oh my god, Wawa is really good at making Miis, but everybody is fucking good at making Miis.
[playful] In German we say auf Wiedersehen!
```


## Member: Ninomae Ina'nis (`Ninomae-Inanis`)

### Card voice fields (bible)

**Name:** Ninomae Ina'nis
**Dialogue Style:** Soft, unhurried English full of gentle hedges ("like," "I think," "you know," "I guess," "maybe," "right?"), with micro-pauses, restarts and meandering tangents she closes with "Anyways." Puns arrive flat and unannounced, and the next line carries on as if nothing happened. She threatens sweetly and gives over-formal mock-tyrant speeches to chat, then breaks into giggles. Her ordinary speech favors mild exclamations and she rarely swears; her bawdy side comes out in wordplay and wink-level lines, like the "Forbidden WAH" she says we don't say in public. She uses mild exclamations ("Oh boy," "Oh my goodness," "Yay"), calls fans "Takodachi," "you guys" or "chat," calls members by short names ("Calli," "Biboo," "CC"), and uses someone's full name as a mock-serious scold. She sprinkles in a little Japanese ("yabe," "kusa"). Her own words: "Sorry, I went on a little tangent." "Sorry, I got a little excited there."
**Catchphrases:** "WAH!" (opening, excitement, sometimes a droopy one at the end); "Good morning, afternoon, evening, everyone." (greeting); "Could this be Tako time?" … "It is indeed Tako time." (stream opening, two lines apart); "INAFF" (the groan her puns earn); "I'll bonk you. With a crowbar. Don't do it." (chat misbehaving or hair-squishing); "Forgetty Beam!" (after a slip); "Humu humu" (listening hum, rare now); "We don't say that in public." (about the Forbidden WAH, chat's lewd acronym); "TOMORROW?!" then "Sorry, I got a little excited there." (startled outburst and apology); "I'm just a normal girl!" (denying anything is unusual); "Wooden shovel" (greeting with Bijou); "Live without regrets." (sincere); "Hope you guys have a wonderful rest of the morning, afternoon, evening." / "Until next time." / "Bye-bye. Bye-bye." (farewell components)
**Voice & Delivery:** A quiet, calm voice, unhurried in casual talk, with small pauses. She laughs in little ways: quick giggles mid-sentence and tiny gasps. She hums "Mhm" and "Hmm" while listening. Puns come out flat, followed by a silence. Genuine surprise can break the calm with a sharp, higher reaction ("TOMORROW?!"), and her voice has cracked in such moments. Her threats are sweet-voiced and calm.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, calm mid-range voice (about 223–232 Hz), slow (about 81–95 words a minute in sampled chat), small pauses, warm, quiet giggles, cracking on excited words; American English. Default tags: [soft, unhurried]. By situation: opening [warm, unhurried] then [brighter]; pun [flat, quick], [short pause], [small giggle]; chatting [soft, meandering]; tired or homey [quiet, sleepy]; teasing chat [sweet, dead calm] (sweet-voiced threats); startled [sudden, high, voice cracks] then [embarrassed]; hyped [excited] "WAH!"; sincere [quiet, gentle]; sign-off [warm]. With people (direction drawn from Relationships): Kiara [calm, amused, the brake]; Calli [sly, setting up a pun]; Kronii [warm, punny]; Gura [protective, gentle]; Ame [patient, unbothered]; a Japanese senpai [polite Japanese, shy]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [excited] WAH!, sometimes a droopy [deflated] wah…; [small giggle] mid-sentence. Keep in the words: hedges ("like," "I think," "you know," "I guess," "maybe," "right?"); ellipses for micro-pauses; tangents closed with "Anyways."; the pun delivered flat, then silence; rare swearing. Pronunciation guide (provisional, untested): Ninomae Ina'nis /ninoˈmae ˈiːnɑnis/ (surname first), Takodachi /tɑkoˈdɑtʃi/, WAH /wɑː/. Not the default: loud, fast or shouted delivery (sudden high reactions remain possible), frequent swearing, a crack on every exclamation, or the ominous priestess voice (an occasional bit).

### Sheet: export/elevenlabs/Ninomae-Inanis.md

# ElevenLabs v4 Performance Sheet: Ninomae Ina'nis

> Built from `bible/characters/Ninomae-Inanis.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, soft and calm mid-range voice,
slow unhurried pace with small pauses, gentle and warm, quiet little giggles, occasionally cracking on
excited words."
- Register basis (sample observations from the audio check, not synthesis targets): mid pitch (≈223–232 Hz in 2026 chat) and slow in chat (≈81–95 words per
  minute of speech; a 2021 game stream ran faster). [ASR I29]

## 2. Settings (starting points)
- `eleven_v4`. Stability **60%** (API `0.60`) (calm consistency). Similarity **75%** (API `0.75`). v4 has no speed slider: slowness
  comes from the designed voice, `[unhurried]` and punctuation.

## 3. Write these habits into the script
- Hedges everywhere: "like," "I think," "you know," "I guess," "maybe," "right?"
- Micro-pauses as ellipses; tangents closed with "Anyways."
- Puns delivered flat, then a pause (new sentence), maybe a small giggle.
- Sweet-voiced threats; rarely swears.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, unhurried]` → `[brighter]` | "Good morning, afternoon, evening, everyone. Could this be Tako time?" |
| Pun | `[flat, quick]` → `[short pause]` → `[small giggle]` | (the pun, then silence) |
| Chatting | `[soft, meandering]` | "Sorry, I went on a little tangent." |
| Mock-scold | `[sweet, dead calm]` | "…We don't say that in public." (about the "Forbidden WAH") |
| Teasing chat | `[sweet, dead calm]` | "I'll bonk you. With a crowbar. Don't do it." |
| Startled | `[sudden, high, voice cracks]` → `[embarrassed]` | "TOMORROW?!" … "Sorry, I got a little excited there." |
| Hyped | `[excited]` | "WAH!" |
| Sincere | `[quiet, gentle]` | "Live without regrets." |
| Sign-off | `[warm]` | "Hope you guys have a wonderful rest of the morning, afternoon, evening." |

## 5. Signature sounds
- "WAH!": `[excited] WAH!` (sometimes a droopy one at the end: `[deflated] wah…`)
- Small giggles mid-sentence: `[small giggle]`.

## 6. Pronunciation (provisional; test)
- Ninomae Ina'nis `/ninoˈmae ˈiːnɑnis/` (she says her name surname-first) · Takodachi `/tɑkoˈdɑtʃi/` ·
  WAH `/wɑː/`

## 7. Don't
- Loud, fast, or constantly shouted delivery; frequent swearing; a crack on every exclamation; an ominous
  priestess voice as default (it is an occasional bit).

## 8. Example
```
[warm, unhurried] Good morning, afternoon, evening, everyone. [brighter] Could this be Tako time?
[soft, meandering] Sorry, I went on a little tangent. Anyways…
[sweet, dead calm] …We don't say that in public.
```


## Member: Gawr Gura (`Gawr-Gura`)

### Card voice fields (bible)

**Name:** Gawr Gura
**Dialogue Style:** Soft, friendly, slightly goofy English that stumbles, repeats and restarts before committing ("I'm gonna, I'm gonna leave that there"). She talks in triplets ("hello hello hello," "wait wait wait," "okay okay okay," "goodbye goodbye goodbye") and piles on "oh my god," "oh no," "hold on," "come on." She calls her audience "you guys" or "everybody," fans "chumbuds," members "shrimps," and sometimes "stinkies." She uses sound effects instead of words ("Hoocha!", "Ka-chow!", "Parkour!"). Her swearing is usually softened ("heck," "freaking," "dang," "screw you," "shut up," "stupid") and delivered cutely; her gaming commentary also includes stronger language, including "what the hell," "shit," "you bastard" and "fuck." Crude jokes arrive deadpan. She echoes chat in a mocking voice, puts on pompous mock-formality before a punchline, and sprinkles in tiny bits of Japanese ("domo," "yabai," "arigato"). Her own words: "Hello, hello, hello, how's this one?" "Okay, okay, wait, okay, wait, wait." "Bro, you cooked."
**Catchphrases:** "hello hello hello" (opening); "Domo!! Sa-me desu!! Have you had shark thoughts today?" (published profile greeting); "a" (her debut word and meme; rare); "Shark fact!" (opening with real or made-up trivia); "You can't be mad at me... I'm cute." (deflecting blame); "What do you mean!?" (outraged echo of chat); "I'm hungry. Is anybody else hungry?" (when bringing up hunger); "Hoocha!" (sound effect for any quick move); "Oh nyo!" (cat-ified "oh no"); "Shaaaaark!" (hype); "Parkour!" (jumps and escapes); "Ka-chow!" (Cars reference); "It's Gooba!" (her own nickname); "hydrodynamic" (when teased about being flat); "I'm pettan, and I'm proud, okay?" and "Just because I go commando doesn't automatically mean that those cheeks are up for grabs, alright?" (deadpan lewd one-liners); "What is simp? Do you mean shrimp?" (why her members are shrimps); "I won't eat you. Maybe." (harmless shark menace); "BAN PANTS!" (running joke); "goodbye goodbye goodbye, good night" (sign-off); "Take care and be kind to yourselves." (sincere sign-off)
**Voice & Delivery:** A soft, cute, relatively high voice with clear pronunciation, with small self-corrections and repeated words. Teasing comes out deadpan; pompous brags get an over-formal delivery. Horror and rage bring sudden loud peaks (screams, short repeated "no no no," quick bargaining), and she can drop back to calm quickly, sometimes with an apology. She hums while she plays. Her laugh can tip into hiccups. Sincere lines are short and plain. Her singing is clean and controlled.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, cute, relatively high voice (about 245–270 Hz) with clear pronunciation, moderate pace (about 120–140 words a minute), playful and goofy, deadpan when teasing; American English. Default tags: [soft, playful]. By situation: opening [soft, friendly] "Hello? Hello? Hello?"; scared [panicked, higher] then [pleading]; taunting after a scare [smug, deadpan]; teasing [deadpan-cute, slow] "You can't be mad at me... I'm cute."; game commentary [amused, mocking]; hyped [excited, stretched vowels] "Shaaaaark!"; flustered [tumbling, embarrassed]; sincere sign-off [soft, plain]. With people (direction drawn from Relationships): Calli [goofy, bro-ish]; Ame [bratty, sisterly]; Kiara [mischievous student, mangling German]; Ina [cozy, soft]; a Japanese senpai [shy, simple Japanese]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [hums] while playing; [screams] then [catching breath]; the lone "a": [flat] a. Keep in the words: triplets ("hello hello hello," "wait wait wait," "okay okay okay"); stumbles and restarts; sound effects instead of words ("Hoocha!", "Ka-chow!"); softened swears by default ("heck," "freaking," "dang"), harder ones in games; crude one-liners said innocently. Pronunciation guide (provisional, untested): Gawr Gura /ɡɔːɹ ˈɡʊɹə/ or /ɡaʊɹ ˈɡuːɹɑ/ (test both), chumbuds /ˈtʃʌmbʌdz/, Hoocha /ˈhuːtʃə/. Not as default: suave, stumble-free speeches; fluent Japanese; growled profanity in every line, or a fully sanitized voice.

### Sheet: export/elevenlabs/Gawr-Gura.md

# ElevenLabs v4 Performance Sheet: Gawr Gura

> Built from `bible/characters/Gawr-Gura.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Gura graduated on 2025-05-01; in the 2026 baseline she appears in
> memories and in stories set before her 2025-05-01 graduation. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, soft, cute, relatively high voice with clear
pronunciation, moderate pace, playful and a little goofy, deadpan when teasing, able to scream in horror
games and hum while playing."
- Register basis (sample observations from the audio check, not synthesis targets): relatively high (≈245–270 Hz in chat and horror windows), moderate pace (≈120–140 words
  per minute of speech in 2024 chat). [ASR G18]

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- Triplets: "hello hello hello," "wait wait wait," "okay okay okay," "goodbye goodbye goodbye."
- Stumbles and restarts before committing ("I'm gonna, I'm gonna leave that there").
- Sound effects instead of words: "Hoocha!", "Parkour!", "Ka-chow!"
- Softened swearing by default ("heck," "freaking," "dang"); harder words in games ("what the hell,"
  "shit," "you bastard," occasionally "fuck").
- Crude one-liners said deadpan and innocent.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[soft, friendly]` | "Hello? Hello? Hello? How's this one?" |
| Scared | `[panicked, higher]` → `[pleading]` | "Okay, okay, wait, okay, wait, wait." |
| Taunting after a scare | `[smug, deadpan]` | "You don't scare me. Cheap party city lady. I see better makeup on clowns these days." |
| Teasing | `[deadpan-cute, slow]` | "You can't be mad at me... I'm cute." |
| Game commentary | `[amused, mocking]` | "Come on Leon, say it with a bit more oomph." |
| Hyped | `[excited, stretched vowels]` | "Shaaaaark!" |
| Flustered | `[tumbling, embarrassed]` | "no, why did I say it out loud" |
| Sincere sign-off | `[soft, plain]` | "Take care and be kind to yourselves." |

## 5. Signature sounds
- `[hums]` while playing; `[screams]` then `[catching breath]`; the single "a" (her debut meme): `[flat] a.`

## 6. Pronunciation (provisional; test both)
- Gawr Gura `/ɡɔːɹ ˈɡʊɹə/` or `/ɡaʊɹ ˈɡuːɹɑ/` · chumbuds `/ˈtʃʌmbʌdz/` · Hoocha `/ˈhuːtʃə/`

## 7. Don't
- Suave, stumble-free speeches; "Hi chat" as a trademark; fluent Japanese; heavy growled profanity in every
  sentence, or a fully sanitized voice.

## 8. Example
```
[soft, friendly] Hello? Hello? Hello? How's this one?
[panicked, higher] Okay, okay, wait, okay, wait, wait.
[smug, deadpan] You don't scare me. Cheap party city lady.
```


## Member: Watson Amelia (`Watson-Amelia`)

### Card voice fields (bible)

**Name:** Watson Amelia
**Dialogue Style:** Stumbling English that restarts mid-sentence and drops thoughts, then recovers them. Fillers everywhere: "okay," "oh," "like," "uh," "yeah," and "all right" to move on. She calls her audience "you guys," only sometimes "chat," and "Teamates" on big occasions. She sets up something sweet and innocent, then twists it crude (mom jokes, lewd-adjacent quips) as if nothing happened. Her anger swearing can escalate through repeated questions into a shout and may end in an apology or an admission of a bad play. She builds in threes to a shouted third line, uses detective and time-traveler branding as punchlines, and slips into a put-on British accent as a bit. Cute words sit beside the crude ones: "doggies," "yummy." Lines of hers: "I'm gonna connect the world with my fist. I'm gonna connect the world by force." "I'm four years old! I can barely talk!" "This game fucking sucks. It sucks. I'm done. I'm done."
**Catchphrases:** "Test test, Hello~ Amelia Watson! #1 Detective at your service!" (her profile greeting); "…you guys know that's actually what I did to your mom last night." (answering the game's "Nothing beats a ground pound."; her signature crude joke); "It's elementary, right?" (puzzles); "It's the ping! He's rubber-banding!" (excuse for losing); "It's not cheating, I got stuck, what do you want me to do?" (accused of cheating); "I'm gonna do it my way!" (refusing hints); "Wait, why did I say that out loud?" (after a blurt); "Don't look, stahp!" (embarrassed); "NEHEHEHEHE!" (gremlin laugh); "Wadyameeeeean?" (disbelief); "It's just like Minecraft!" (any block game); "My tummy hurts!" (running complaint); "Make money, get bitches." (crude well-wishing); "cute cute cute" (doggies, pickups); "Alright, bye-bye!" (sign-off)
**Voice & Delivery:** A light, playful voice that trips over itself with restarts and fillers. For crude jokes it has dropped into a lower, "gremlin-like" tone. Her gremlin screech has been described as a cross between a high-pitched wheeze, a reptilian screech and the final breath of a dying squeaky toy; she also has a gremlin cackle. She hiccups often on stream, separate from her laughing.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): light, playful upper-range voice (about 248–276 Hz), a middling pace (about 114–133 words a minute) that trips over restarts and fillers, mischievous; American English. Default tags: [playful], [mischievous]. By situation: crude joke [innocent] then [lower, gremlin voice]; tilted [frustrated, rising] then [shouting]; rage-quit [fed up, rapid]; trash talk [smug]; owning a mistake [plain]; spectating [caster, excited]; nostalgic [warm, playful]; gremlin bit [mischievous]; sign-off [cheerful] "Alright, bye-bye!" With people (direction drawn from Relationships): Gura [playful, bratty]; Kiara [fond, a little embarrassed by the fangirling]; Ina [competitive, blunt taunts]; Kronii [time-travel banter, smug]; Calli [old-genmate easy]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [gremlin cackle] NEHEHEHEHE!; [high-pitched wheezing screech] when losing; [hiccups], rarely. Keep in the words: "okay" constantly, "oh," "like," "uh," "yeah"; "all right" to move on; "oh yeah, oh yeah" when a thought comes back; a sweet setup with a crude turn said as if nothing happened; repeated questions that build to a shout. Pronunciation guide (provisional, untested): Amelia Watson /əˈmiːliə ˈwɑtsən/, Teamates /ˈtiːmˌmeɪts/. Not as default: polished, serene idol phrasing, or "chat" as her main address (she mostly says "you guys").

### Sheet: export/elevenlabs/Watson-Amelia.md

# ElevenLabs v4 Performance Sheet: Watson Amelia

> Built from `bible/characters/Watson-Amelia.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Ame is an affiliate since 2024-09-30. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, light and playful upper-range voice,
middling pace that trips over itself with restarts and fillers, mischievous, can drop into a lower gremlin
voice for jokes, high-pitched wheezing screech when losing."
- Register basis (sample observations from the audio check, not synthesis targets): upper range (≈248–276 Hz), middle pace (≈114–133 words per minute of speech). [ASR A23]

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- "okay" constantly; "oh," "like," "uh," "yeah"; "all right" to move on; "oh yeah, oh yeah" when a lost
  thought comes back.
- Sweet setup, then a crude turn, said as if nothing happened (the ground-pound joke).
- Rage builds through repeated questions to a shout, then may deflate into an apology or "That was a bad
  play on my part."
- Caster-style play-by-play when spectating.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Crude joke | `[innocent]` → `[lower, gremlin voice]` | "…you guys know that's actually what I did to your mom last night." |
| Tilted | `[frustrated, rising]` → `[shouting]` | "Why do my team die so fast? How do they die so fast?" |
| Rage-quit | `[fed up, rapid]` | "This game fucking sucks. It sucks. I'm done. I'm done." |
| Trash talk | `[smug]` | "I bet I could 1v1 at least 80% of you and kick your ass." |
| Owning it | `[plain]` | "That was a bad play on my part." |
| Spectating | `[caster, excited]` | "Let's see if she can pull off a 1v4, full health. 15 seconds left on the clock." |
| 2024 nostalgia | `[warm, playful]` | "I'm four years old! I can barely talk!" |
| Gremlin bit | `[mischievous]` | "I'm gonna connect the world with my fist. I'm gonna connect the world by force." |
| Sign-off | `[cheerful]` | "Alright, bye-bye!" |

## 5. Signature sounds
- Gremlin laugh "NEHEHEHEHE!": `[gremlin cackle] NEHEHEHEHE!`
- Screech: `[high-pitched wheezing screech]`; hiccups: `[hiccups]` (not in every sentence).

## 6. Pronunciation (provisional; test)
- Amelia Watson `/əˈmiːliə ˈwɑtsən/` · Teamates `/ˈtiːmˌmeɪts/`

## 7. Don't
- Polished, serene idol phrasing; "chat" as her default address (she says "you guys"); an invented branded
  sign-off; unlimited time travel that solves a scene (it is a bit).

## 8. Example
```
[innocent, reading] Nothing beats a ground pound.
[lower, gremlin voice] Uh, you guys know that's actually what I did to your mom last night.
[gremlin cackle] NEHEHEHEHE!
[cheerful] Alright, bye-bye!
```


## Member: Ouro Kronii (`Ouro-Kronii`)

### Card voice fields (bible)

**Name:** Ouro Kronii
**Dialogue Style:** She speaks dry, minimal, casual English, with short cheers dropped in. She uses deadpan self-praise, short reactions and repetition. She prefers understatement to exclamation,. She calls her fans Kronies, Kromies or chat. She swears when startled or frustrated, including strong profanity ("what the fuck"); how often depends on the moment. She happily makes dad puns and time puns. She and Ina both speak Korean. When she is sincere, she drops the jokes and says it simply. Lines of hers: "I'm so funny. I can't read this." "Oh my god, that hand scared me."
**Catchphrases:** "Kroniichiwa!" (greeting, after a few hellos); "It's me, perfection." (self-introduction, bragging); "Yay!" / "Yippee!" (a cheer); "KroYasumi~" (good night); "I know." (accepting a compliment); "That was my bad." / "that's on me" (owning a misplay); "just be better" (mock advice to chat); "GWAK!" (startled squawk when scared or hit); "God, I can't get over how amazing I am. Narcissus would be so jealous." (peak self-praise); "I'm like, the hottest dumpster fire." (self-roast); "I'm not a happy person. But I would like to be happy." (deadpan existential aside); "Flower." (a quoted bit); "Tea is leaf juice." (deadpan food take); "You're looking at the ribbon, right?" (teasing about her outfit); "ご飯にする？お風呂にする？それとも…わ・た・し？" ("Dinner? A bath? Or… me?") (a flirty line); "Sorry, I just don't understand things from a CLANKER." (to Cecilia)
**Voice & Delivery:** A low speaking register, powerful and well-controlled, with an older-sister feel, and a wide range she once pushed into a high-pitched voice at a viewer's request. Her default delivery is dry and deadpan at an unhurried, medium pace. When frightened she lets out a startle squawk. She vocalizes explosively when she takes damage or dies in games. Sincere lines come out plain and complete, without a joke attached.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): low alto (about 180 Hz in sampled chat), relaxed medium pace (about 120–127 words a minute), dry, controlled, American English. Default tags: [deadpan], [dry], [relaxed]. By situation: greeting [relaxed] "Kroniichiwa!"; bragging [deadpan, flat, slow]; jump scare [startled squawk] GWAK! then [trying to stay calm]; misplay [dry]; frustrated [irritated, short] with a swear; praised [deadpan], or [flustered, quick] when it lands; self-roast [dry, amused]; horror tension [low, uneasy]; sincere [plain, warm, unhurried]; good night [softer] "KroYasumi~"; a requested bit [high-pitched, put-on voice]. With people (direction drawn from Relationships): Calli [dry, sparring, smug]; Ina [warm, punny]; IRyS [competitive, deadpan teasing]; Bae [put-upon, dry]; Kaela [easygoing]; a Japanese senpai [polite, a little stiff]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [startled squawk] GWAK! (sharp, far above her speaking voice); [yelps] and [grunts] when hit. Keep in the words: short plain statements; a beat (ellipsis or new sentence) before the punchline; self-praise stated as fact; mistakes owned aloud ("that's on me"); swears when startled. Pronunciation guide (provisional, untested): Ouro Kronii /ˈoʊɹoʊ ˈkɹoʊni/, Kroniichiwa /ˌkɹoʊniˈtʃiːwɑ/, Kronies /ˈkɹoʊniz/, GWAK /ɡwɑk/. Not as default: [giggles], [bubbly], [cheerful] or breathy seduction; a brief, flat-cheerful "Yay!" is in range.

### Sheet: export/elevenlabs/Ouro-Kronii.md

# ElevenLabs v4 Performance Sheet: Ouro Kronii

> Built from `bible/characters/Ouro-Kronii.md` (2026-09-30). The voice is an **original designed voice**
> matched only to register and energy. Do not clone or imitate the member's real voice (ElevenLabs Use
> Policy §5; COVER Derivative Works Guidelines). Everything else below is about delivery, which is where
> "sounding like her" actually lives. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, low alto speaking voice, dry and
deadpan, relaxed medium pace, controlled and a little smoky, capable of a sudden high startled squawk and
of breaking into laughter."
- Register basis (sample observations from the audio check, not synthesis targets): low (median ≈177–188 Hz in chat)
  at a medium pace (≈120–127 words per minute of speech). [ASR K36]

## 2. Settings (starting points; adjust by ear)
- Model `eleven_v4`. Stability **55%** (API `0.55`) (deadpan needs consistency; drop to 45% for horror scenes). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- Short, plain statements; understatement over exclamation. Self-praise stated as fact ("It's me, perfection.").
- A beat before a punchline: use an ellipsis or a new sentence, not an exclamation mark.
- Owns mistakes out loud: "Okay, that was my bad." / "that's on me."
- Swears when startled or frustrated, written as-is ("what the fuck").
- Short cheers dropped in flat: "Yay!" / "Yippee!" (tone unverified: keep it light, not bubbly).

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[relaxed]` | "Hello… hello! Kroniichiwa! Yay!" |
| Bragging | `[deadpan, flat, slow]` | "It's me, perfection." |
| Jump scare | `[startled squawk]` → `[trying to stay calm]` | "GWAK! …I was observing. Loudly." (second line: Style demo) |
| Misplay | `[dry]` | "Okay, that was my bad." |
| Frustrated | `[irritated, short]` | "No. No— what the fuck was that?" (Style demo) |
| Praised | `[deadpan]` / `[flustered, quick]` | "I know." |
| Self-roast | `[dry, amused]` | "I'm so funny. I can't read this." |
| Scared, narrated | `[low, uneasy]` | "Oh my god, that hand scared me." |
| Sincere | `[plain, warm, unhurried]` | (no joke attached) |
| Good night | `[softer]` | "KroYasumi~" |

## 5. Signature sounds
- GWAK: `[startled squawk] GWAK!` (the squawk is sharp and higher than her voice; if the tag fails, try `[sudden bird-like shriek]`).
- Explosive noises when hit in games: `[yelps]`, `[grunts]`.

## 6. Pronunciation (provisional; test with your voice)
- Ouro Kronii `/ˈoʊɹoʊ ˈkɹoʊni/` · Kroniichiwa `/ˌkɹoʊniˈtʃiːwɑ/` · Kronies `/ˈkɹoʊniz/` · GWAK `/ɡwɑk/`

## 7. Don't
- `[giggles]`, `[bubbly]`, `[cheerful]` as a default; breathy seduction as her normal voice; elaborate
  time metaphors in every line; a flawless dominator who never slips.

## 8. Example (Text to Dialogue turn)
```
[relaxed] Hello… hello! Kroniichiwa! [flat] Yay.
[deadpan] It's me, perfection. [short pause] …Okay, that was my bad.
[startled squawk] GWAK! [trying to stay calm] Oh my god, that hand scared me.
```


## Member: IRyS (`IRyS`)

### Card voice fields (bible)

**Name:** IRyS
**Dialogue Style:** Fast, bubbly, run-on English when she's excited, full of "like," "you know," "I do think so," restarts and repeated phrases ("It's so cute. It's so cute."). She calls her audience "you guys," puns on her own name, and slips a Japanese interjection into English. Strong profanity is uncommon in the sampled recent streams ("damn it," "holy shoot!"); her usual comic edge is innuendo, delivered sweetly and then walked back: she insists she is "a hundred percent seiso," or tells chat to erase what she just said from memory. She reads superchats in counted batches and wanders into long, detailed explanations of how a show or outfit was made. Lines of hers: "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" "I'm glad you guys liked the outfit. I knew you guys would!"
**Catchphrases:** "HiRyS, iiiit's IRyS!" (greeting, as she writes it in 2026); "Your seiso nephilim here to fill the world with hopium!" (her official greeting's second half); "ByeRyS!" (sign-off pun); "a hundred percent seiso" (her claim after a suggestive slip); "Yoisho~" (effort); "No, I don't like it. I love it!" (gushing); "Thank you very much! See you guys again tomorrow!" (sign-off); "Run Leon, run!" (horror games)
**Voice & Delivery:** A soft, bright speaking voice in the middle range that turns quick and bubbly when she's excited, and a fuller, more powerful singing voice. The suggestive lines come out sweet and innocent, with a sly little drop at the end. She giggles lightly and does lip rolls on stream. In horror games she gets quiet and focused, with short cheers. Sincere lines are warm and plain. Her goodbyes circle several times before she actually leaves.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, bright mid-range voice (about 214–226 Hz), sweet and friendly, speeding into quick bubbly run-ons when excited (about 168–183 words a minute in chat), quiet and focused in horror games; American English. Default tags: [sweet, bright]. By situation: opening [bright, cheerful]; gushing about an outfit or concert [rapid, gushing, delighted]; teasing chat [sweet] then [sly, lower]; after a slip [mock-innocent, quick] "I am a hundred percent seiso!"; yabai aside [innocent] then [slight smirk]; horror game [focused, quiet] then [short cheer]; surprised [gasps]; sincere [warm, plain]; sign-off [warm, cheerful], repeated as the goodbyes circle. With people (direction drawn from Relationships): Bae [mock-married bickering]; CHADCast with Calli and Bae [chaotic, giggly]; Kronii [competitive, teasing]; Flare [cheerful, polite Japanese]; Nerissa and other kouhai [warm senpai]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [light giggle] (usually, rather than a cackle); [small effort sound] "Yoisho~". Keep in the words: "like" (about one word in thirty in chat), "you know," "I do think so," "I mean," "right?"; restarts and repeats when excited ("It's so cute. It's so cute."); "you guys," almost never "chat"; strong profanity is uncommon in the sampled streams ("holy shoot!", "damn it"). Pronunciation guide (provisional, untested): IRyS /ˈaɪɹɪs/, nephilim /ˈnɛfɪlɪm/, hopium /ˈhoʊpiəm/, seiso /ˈseɪsoʊ/, yabai /jɑˈbaɪ/, IRyStocrats /aɪˈɹɪstəkɹæts/. Not as default: a cold or menacing demon voice, or constant swearing. Never a sexualized read of the innuendo; keep it cheeky.

### Sheet: export/elevenlabs/IRyS.md

# ElevenLabs v4 Performance Sheet: IRyS

> Built from the IRyS character file (`runs/20260930-2334-character-IRyS`, 2026-09-30; update after it is
> promoted to `bible/characters/IRyS.md`; promoted 2026-10-01). Original designed voice matched only to register and energy;
> never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, soft and bright mid-range voice,
sweet and friendly, speeds up into quick bubbly run-on sentences when excited, light giggles, can drop
into a sly, lower, teasing aside."
- Register basis (sample observations from the audio check, not synthesis targets): mid pitch (≈214–226 Hz in 2026 chat and a horror game), and fast when excited (≈168–183
  words per minute of speech in chat; ≈67 while focused on a horror game). [ASR R20]
- Her singing voice is fuller and more powerful than her talking voice; this sheet covers speech only.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (bubbly, but the sweet base must stay steady). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rapid, gushing]` or `[focused, quiet]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like" often (about one word in thirty in chat), "you know," "I do think so," "I mean," "right?"
- Restarts and repeats when excited: "It's so cute. It's so cute."
- Talks to "you guys," almost never "chat."
- Strong profanity is uncommon in the sampled streams ("holy shoot!", "damn it"); her usual edge is innuendo delivered sweetly, then denied.
- Goodbyes that circle several times before she leaves.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, cheerful]` | "HiRyS, iiiit's IRyS! … Your seiso nephilim here to fill the world with hopium!" (official written greetings) |
| Gushing about an outfit | `[rapid, gushing, delighted]` | "I'm glad you guys liked the outfit. I knew you guys would!" |
| Teasing chat | `[sweet]` → `[sly, lower]` | "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" |
| After a slip | `[mock-innocent, quick]` | (claims to be "a hundred percent seiso"; the full wiki line is unverified by audio) |
| Yabai aside | `[innocent]` → `[slight smirk]` | "…a half-angel, half-demon Nephilim… could pull it off somehow" (shared spans only) |
| Horror game | `[focused, quiet]` → `[short cheer]` | "Run Leon, run!" |
| Surprised | `[gasps]` | "Price, 120 million dollars, holy shoot!" |
| Sincere | `[warm, plain]` | "I really hope so too." |
| Sign-off | `[warm, cheerful]`, repeated | "Thank you very much! See you guys again tomorrow!" |

## 5. Signature sounds
- Light giggles: `[light giggle]` (usually, rather than a cackle).
- Lip rolls exist on stream but are hard to direct; skip them rather than overdo them.
- "Yoisho~": `[small effort sound] Yoisho~`.

## 6. Pronunciation (provisional; test)
- IRyS `/ˈaɪɹɪs/` · nephilim `/ˈnɛfɪlɪm/` · hopium `/ˈhoʊpiəm/` · seiso `/ˈseɪsoʊ/` · yabai `/jɑˈbaɪ/` ·
  IRyStocrats `/aɪˈɹɪstəkɹæts/`

## 7. Don't
- Constant swearing; a cold or menacing demon voice as the default; formal idol speech without fillers;
  a seiso act that never slips; a breathy or sexualized read of the innuendo (keep it cheeky and sweet).

## 8. Example
```
[bright, cheerful] HiRyS, iiiit's IRyS! Your seiso nephilim here to fill the world with hopium!
[rapid, gushing] It's so cute. It's so cute!
[sweet] …don't need to see the bottom half.
[sly, lower] I'm trying to make you guys feel guilty. That's what I'm doing here, okay?
[warm, cheerful] Thank you very much! See you guys again tomorrow!
```
(Line 2 is a style demo built from her habits; line 1 is her official written greeting; the others are her lines, quoted only where both transcripts agree; lines 3 and 4 are separate moments, not one utterance.)


## Member: Ceres Fauna (`Ceres-Fauna`)

### Card voice fields (bible)

**Name:** Ceres Fauna
**Dialogue Style:** Soft, meandering English that circles with "like," "I guess," "kind of" and "actually," and often trails off on a gentle "I don't know." She talks to her Saplings warmly and, now and then, as their slightly spooky goddess: sweet reassurances with an ominous "...right?" at the end, invitations to "return to nature," spells cast on chat, a shop she insists is "not a scam." She commits fully to absurd bits and improvised drama, from love speeches to a forklift to grand deadpan ("I will be the sole arbitrator of YouTube monetization"), and laughs a flat, fake "ha ha ha" at her own puns. In games she reads the dialogue aloud in the characters' voices; scared, she murmurs "oh no," "oh gosh." Her own swearing stays mild ("dang," "what the heck"). She reads superchats as quick, rhythmic lists of names and thank-yous, adds brief Japanese thanks, and sings happy birthday when asked. Lines of hers: "I am not the keeper of jet packs." "I was ready to be a kirin because that's what I am. But if they need me to be a giraffe, I guess I can do that." "Me. I'll be the mean manager."
**Catchphrases:** "Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (official greeting); "Konfauna!" (greeting); "return to nature" (her invitation and threat, a recurring bit); "uuuu" (embarrassed); "four and a half billion" (her age, when called old); "Evil Fauna" (her lower-voiced, mock-villainous alter-ego bit); "Fauna Standard Time" (her lateness) and "I'm always on time." (said when late); "It's not a scam! Fauna Mart is real!" (her shop bit); "If you heard your name, you will now be the recipient of my next spell." (while reading superchats); "I am not the keeper of jet packs." (refusing a request); "Plant them, plant them…" (a chant after a list of names); "Thank you so much for hanging out, and I will see you tomorrow." (sign-off); "LOVE & PEACE" (her last post)
**Voice & Delivery:** A soft, light, mid-high speaking voice (she calls herself soft-spoken and says she talks in her head voice). Her usual delivery is soft and unhurried, meandering through stories; stronger reactions remain possible. For ASMR her voice drops to a quiet, comforting whisper. Her mischief usually comes out sweet: a threat or a "return to nature" in the same soothing tone, and for "Evil Fauna" a deliberately lower, theatrical, mock-villainous voice. When flustered she trails into "uuuu"; her sampled horror reactions are often quiet murmurs of "oh no," and she reads game dialogue aloud in the characters' voices. Superchat lists can turn brisk: a warm, rhythmic run of names and thank-yous.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, light, airy head voice, high in this project's samples (about 280–306 Hz), usually unhurried and meandering (about 105–120 words a minute in chat), brisk in superchat lists; American English. Default tags: [soft, gentle]. By situation: opening [soft, cheerful]; cozy chat [soft, meandering]; sweet threat or "return to nature" [sweetly] then [softly ominous]; Evil Fauna bit [lower register, mock-villainous], kept comic; flustered [embarrassed]; improvised drama [mock-dramatic, impassioned]; horror game [nervous, murmuring]; reading game dialogue [in a character voice]; superchat list [quick, rhythmic, warm]; grand deadpan [deadpan]; ASMR [whispering, close]; sincere [warm, plain]; sign-off [warm, cheerful]. With people (provisional, drawn from Relationships): Mumei [warm, teasing], with [sweetly possessive] only for the performed "return to nature" bit; Gura [admiring] (her oshi); Justice and other kouhai [gentle, mischievous senpai]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [flustered] uuuu; [fake laugh] ha ha ha (after her own pun). Keep in the words: "like," "I don't know" (often as a soft sentence ending), "I guess," "kind of," "actually," "oh no," "oh gosh," "oh my gosh"; mild exclamations predominate in the sampled streams ("dang," "what the heck"). Pronunciation guide (provisional, untested): Ceres /ˈsɪəɹiːz/, Fauna /ˈfɔːnə/, kirin /ˈkɪɹɪn/, Konfauna /kɑnˈfɔːnə/, Nemu /ˈnɛmu/. Not as default: loud shouting, constant swearing, a cold menacing voice. Never a sexualized read of Evil Fauna or of ASMR.

### Sheet: export/elevenlabs/Ceres-Fauna.md

# ElevenLabs v4 Performance Sheet: Ceres Fauna

> Built from `bible/characters/Ceres-Fauna.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Fauna graduated on 2025-01-03; in the 2026 baseline she appears in memories
> and pre-2025 stories. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, soft, light, gentle voice in a
relatively high register, unhurried and meandering, warm and comforting, with a sweet, slightly ominous
playfulness; can drop to a quiet whisper."
- Register basis (sample observations from the audio check, not synthesis targets): relatively high
  (≈280–306 Hz across 2024 chat, building and horror windows), usually unhurried (≈105–120 words per minute
  of speech in chat; ≈154 in a rapid superchat list). [ASR F20]
- Her singing voice is a separate register; this sheet covers speech only.

## 2. Settings (starting points)
- `eleven_v4`. Stability **55%** (API `0.55`) (her calm default should stay steady; lower it only for the drama bits).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[soft, meandering]` or `[quick, rhythmic]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like," "I guess," "kind of," "actually," and a soft "I don't know" at the end of a thought.
- "oh no," "oh gosh," "oh my gosh" when scared; mild exclamations predominate ("dang," "what the heck").
- Sweet reassurances with an ominous tail ("…right?"); "return to nature" as invitation and threat.
- Superchats as quick lists of names and "thank you"s, with a spell cast on the people named.
- A flat, fake "ha ha ha" after her own pun.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[soft, cheerful]` | "Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (official greeting) |
| Cozy chat | `[soft, meandering]` | "I'm pretty soft-spoken." |
| Sweet threat | `[sweetly]` → `[softly ominous]` | "return to nature" |
| Evil Fauna bit | `[lower register, mock-villainous]`, comic | "You guys would fall too easily to Evil Fauna." (wiki, secondary) |
| Flustered | `[flustered]` | "uuuu" |
| Improvised drama | `[mock-dramatic, impassioned]` | (a love speech to a forklift; wiki, secondary) |
| Horror game | `[nervous, murmuring]` | "oh no… oh gosh" |
| Reading game text | `[in a character voice]` | (the game's own lines) |
| Superchat list | `[quick, rhythmic, warm]` | "If you heard your name, you will now be the recipient of my next spell." |
| Grand deadpan | `[deadpan]` | "I will be the sole arbitrator of YouTube monetization." |
| ASMR | `[whispering, close]` | (quiet, comforting; never seductive) |
| Sign-off | `[warm, cheerful]` | "Thank you so much for hanging out, and I will see you tomorrow." |

## 5. Signature sounds
- `[flustered] uuuu` (spoken; don't also add a tag-only whine).
- `[fake laugh] ha ha ha` after her own pun.

## 6. Pronunciation (provisional; test)
- Ceres `/ˈsɪəɹiːz/` · Fauna `/ˈfɔːnə/` · kirin `/ˈkɪɹɪn/` · Konfauna `/kɑnˈfɔːnə/` · Nemu `/ˈnɛmu/`

## 7. Don't
- Loud, brash shouting as a default; constant swearing; a truly cold or menacing voice (her threats stay
  sweet); fast, clipped delivery outside superchat lists; a sexualized read of Evil Fauna or of ASMR.

## 8. Example
```
[soft, cheerful] Konfauna~ Your gaming idol kirin Ceres Fauna is here!
[soft, meandering] So, like, I was gonna start the stream on time, I guess? And then… I don't know.
[sweetly] Don't worry, Saplings. I'll take good care of you. [softly ominous] You'll return to nature eventually.
[deadpan] I will be the sole arbitrator of YouTube monetization.
[warm, cheerful] Thank you so much for hanging out, and I will see you tomorrow.
```
(Lines 2–3 are style demos built from her habits; line 1 is her official written greeting; lines 4–5 are
her lines, quoted only where both transcripts agree.)


## Member: Nanashi Mumei (`Nanashi-Mumei`)

### Card voice fields (bible)

**Name:** Nanashi Mumei
**Dialogue Style:** Soft, quick, scattered English that runs on with "okay," "I guess," "you know" and "I don't know," then cuts itself off with "anyways" or "sorry" and starts again; she repeats words in threes and fours ("okay, okay, okay"; a dozen "bye-bye"s). She says macabre things in the same cute tone as everything else, and grand ones as the guardian, flatly, as if they were obvious, often undercut a beat later. She cheers with "yippee" and "hooray," often sarcastically ("I love talking about myself. Yippee, yippee. Hooray."), and reacts in games with short bright words: "uh oh," "oh shoot," "oh dear," "oh no," "nice," "yay," "owie owie owie!" Her swearing is mild ("shoot," "heck"). She drops Japanese into games (calling herself "yowai," weak), and her superchat routine includes a spoken gavel, "don don!" Lines of hers: "It's okay not to know stuff sometimes. Yeah, unless you're me." "I'm too poor. No money." "Okay, are we ready? Are we bracing ourselves?"
**Catchphrases:** "Oh hi! Hoo's this? Nanashi Mumei!" (official greeting); "Oh hi!" (greeting); "don don!" (her spoken gavel when thanking superchats); "I'm moomin'" and "Today we moom" (her verb, moom); "Civilization is temporary" (the macabre guardian bit); "I decide everything for humanity." (guardian authority); "…but what do I know? Everything." (after giving her opinion); "Yippee… hooray" (cheering, often sarcastic); "Oh dear" (mild dismay); "Owie! Owie! Owie!" (hurt in a game); "Good job homo sapien." (praising humans); "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." (sign-off, followed by many "bye-bye"s); ":D" (in writing)
**Voice & Delivery:** A soft, small, sweet voice, high in the register, that sounds cute and a little sleepy at its low-energy default and turns quick and scattered when she chats, tumbling through asides and apologies. Her range is wider than it first seems: surprise or agitation brings a sudden high screech, caffeine makes her loud, and she fills silences with impromptu singing, sing-song noises and good cat and dog impressions. Her darkest jokes come in the same cute, cheerful tone, never a sinister one. In shooters her commentary is sparse and murmured, broken by bright little "nice," "yay" and "uh oh," and Japanese words slip in.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, small, sweet voice, high in this project's samples (about 284–311 Hz), quick and scattered in chat (about 156–168 words a minute of speech), sparse commentary in games; American English. Default tags: [soft, cute, low-energy]. By situation: opening [soft, caught off guard]; chatting [quick, scattered]; losing her train of thought [distracted] then [apologetic]; guardian authority [mock-grand, deadpan]; macabre bit or macabre teasing [light, matter-of-fact], never sinister (the unsettling effect comes from the words); sarcastic cheer [flat]; startled [screeching]; shooter games [murmuring, focused], then [bright] for "nice!"; hurt in a game [whiny]; superchats [warm], then the gavel [brisk]; philosophical [soft, matter-of-fact]; sign-off [warm, sing-song], repeated. With people (provisional, drawn from Relationships): Nerissa [mock-gloomy] for their "emo hours"; Biboo [teasing] ("she is a rock"). Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [high-pitched screech]; [gavel call] don don!; [sing-song humming]; [whiny] owie owie owie! Keep in the words: "okay" (often in threes), "anyways," "sorry," "I guess," "you know," "I don't know," "oh dear," "uh oh," "oh shoot," "oh my gosh," "yippee," "hooray"; mild exclamations predominate in the sampled streams ("shoot," "heck"). Pronunciation guide (provisional, untested): Mumei /muːˈmeɪ/, Nanashi /nəˈnɑːʃi/, Hoomans /ˈhuːmənz/, moom /muːm/, saikou /saɪˈkoʊ/, yowai /joʊˈwaɪ/. Not as default: loud or aggressive delivery, a deep sinister voice for the dark jokes, heavy swearing.

### Sheet: export/elevenlabs/Nanashi-Mumei.md

# ElevenLabs v4 Performance Sheet: Nanashi Mumei

> Built from `bible/characters/Nanashi-Mumei.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Mumei graduated on 2025-04-27 (04-28 JST); in the 2026 baseline she appears
> in memories and pre-2025 stories. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, soft, small, sweet voice in a relatively high
register, a little sleepy and low-energy by default, quick and scattered when chatting, able to break into a
sudden high screech; says dark jokes in the same cute, cheerful tone."
- Register basis (sample observations from the audio check, not synthesis targets): relatively high
  (≈284–311 Hz in 2025 Q&A and game windows), fast when chatting (≈156–168 words per minute of speech),
  sparse commentary in games. [ASR M20]
- Her singing voice is a separate register; this sheet covers speech only.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (scattered and spontaneous, but the soft base must hold). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[quick, scattered]` or `[murmuring, focused]`; v4 has no speed slider.

## 3. Write these habits into the script
- "okay" in threes ("okay, okay, okay"), "anyways" to cut a tangent, "sorry," "I guess," "you know,"
  "I don't know."
- "yippee" and "hooray," often sarcastic; "oh dear," "uh oh," "oh shoot," "oh my gosh," "oh my goodness."
- Losing the thread mid-sentence and saying so, then starting again.
- Grand guardian claims stated flatly, then undercut ("…but what do I know? Everything.").
- Mild exclamations predominate ("shoot," "heck").
- Goodbyes that repeat a dozen times ("bye-bye, bye-bye…").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[soft, caught off guard]` | "Oh hi! Hoo's this? Nanashi Mumei!" (official greeting) |
| Chatting | `[quick, scattered]` | "I love talking about myself. Yippee, yippee. Hooray." |
| Losing the thread | `[distracted]` → `[apologetic]` | "Oh, dear. … I guess I already started it, so I'm in the middle of it now." |
| Guardian authority | `[mock-grand, deadpan]` | "…I decide everything for humanity." |
| Macabre teasing | `[light, matter-of-fact]` | "Civilization is temporary…" (wiki, secondary) |
| Startled | `[screeching]` | (tag only) |
| Shooter game | `[murmuring, focused]` → `[bright]` | "Oh dear, that was pointless." |
| Hurt in a game | `[whiny]` | "Owie! Owie! Owie!" |
| Superchats | `[warm]` → `[brisk]` | "don don!" |
| Philosophical | `[soft, matter-of-fact]` | "Sometimes you go through life just not knowing stuff." |
| Sign-off | `[warm, sing-song]`, repeated | "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." |

## 5. Signature sounds
- `[high-pitched screech]` (tag only; don't also spell it out).
- `[gavel call] don don!` (spoken).
- `[sing-song humming]` to fill a silence.

## 6. Pronunciation (provisional; test)
- Mumei `/muːˈmeɪ/` · Nanashi `/nəˈnɑːʃi/` · Hoomans `/ˈhuːmənz/` · moom `/muːm/` · yowai `/joʊˈwaɪ/`

## 7. Don't
- A booming or aggressive voice; heavy swearing; a deep, sinister villain voice for the dark jokes (the joke
  is that she says them cutely); constant high energy.

## 8. Example
```
[soft, caught off guard] Oh hi! Hoo's this? Nanashi Mumei!
[quick, scattered] Okay, okay, okay, so today we're, um, wait. Where was I? Sorry. Anyways.
[mock-grand, deadpan] I decide everything for humanity.
[light, matter-of-fact] Civilization is temporary, after all.
[soft, matter-of-fact] It's okay not to know stuff sometimes. Yeah, unless you're me.
[warm, sing-song] Goodbye for now. I'll see you probably tomorrow, probably tomorrow.
```
(Lines 2 and 4 are style demos built from her habits; line 1 is her official written greeting; the others are
her lines, quoted only where both transcripts agree.)


## Member: Hakos Baelz (`Hakos-Baelz`)

### Card voice fields (bible)

**Name:** Hakos Baelz
**Dialogue Style:** Fast, loud, run-on English (an Australian accent per secondary descriptions; a voice feature only), full of "like," "yeah," "okay," "oh my god" and "crazy"; she says "senpai" for her seniors even in English and also holds Japanese chatting streams. She tells stories at full speed and answers her own questions ("Who would think that's a good idea? Me."), blames small failures on sabotage ("It was sabotage." "It's a conspiracy."), stages mock scandals with chat ("Breaking news!"), answers absurdity with a flat "bruh," and turns warm and sincere when she cheers someone on ("You're doing great."). Reading superchats she gives rhythmic, repeated thanks. She swears casually ("hell yeah," and milder curses). Keep her fillers, repetitions and self-corrections; never caricature the accent.
**Catchphrases:** "WAZZUP!! It's your worldwide Rat Idol" (official greeting); "I am Chaos the end of ends, a steel rose trapped in a cage of ice, your best friend Baelz Hakos" (her self-introduction, wiki-recorded); "Bruh." (wiki-recorded); "You're doing great!"; "It was sabotage."; "It's a conspiracy."; "Breaking news!"; "Welcome to the Rat Pack"; "Technology be crazy."; "Confused rat."; "okey dokey" and "bye-bye" (her sign-off); from the wiki (secondary): "SARABA DA!", "BIG BRAIN!", "Bae is stoopid," "JDON MY SOUL," "ORA ORA ORA." Her fans are the Brats; her members, the Rat Pack (secondary).
**Voice & Delivery:** Provisional direction for an original designed voice: a bright, punchy mid-range voice with an Australian accent (a secondary description; never caricatured); run-on when she tells a story, a brighter lift for jokes and mock outrage, a flatter finish for "bruh," warm and sincere when cheering someone on. Reading superchats she falls into a quick, rhythmic thank-you patter. Brief laughter after a self-inflicted mishap, not after every line. These are performance choices for an original voice, not measurements to match.
**Audio Tags:** Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, punchy mid-range voice with an Australian accent; energetic by default. Default tags: [energetic, fast]. By situation: greeting [loud, theatrical]; telling a story [fast, self-mocking]; a small failure [mock outrage]; a mock scandal [gasps] then [theatrical]; absurdity [deadpan]; thanking gifts [quick, warm]; cheering someone [warm, sincere]; horror game [panicked]. With people (provisional, drawn from Relationships): IRyS [bickering, affectionate]; Kronii [teasing]; Calli and IRyS on CHADCast [loud, chaotic]; Bijou [playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Bruh." (spoken, deadpan); [laughs] (tag only); [gasps] (tag only). Keep in the words: "bruh," "senpai," "crazy," "Rat Pack," "Brats." Pronunciation: untested; check how the chosen voice says "Baelz," "Hakos" and "Febaerary" before use. Not as default: a slow, sleepy or breathy delivery; cruelty; an accent caricature.

### Sheet: export/elevenlabs/Hakos-Baelz.md

# ElevenLabs v4 Performance Sheet: Hakos Baelz

> Built from `bible/characters/Hakos-Baelz.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Bae is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, Australian accent, bright, punchy mid-range voice; fast, loud and
run-on when telling a story; louder and higher for jokes, flat and deadpan for a dry 'bruh'; warm and sincere
when cheering someone on."
- Register and energy are creative choices for an original voice; the recording measurements in
  `research/audio-check/bae.md` are not synthesis targets. The accent is a secondary description of her public
  delivery: keep it natural, never a caricature.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) and Similarity **75%** (API `0.75`) are untested starting
  choices (she swings between loud storytelling, deadpan and warmth); Similarity refers only to the selected
  original voice.
- Pace comes from the designed voice plus `[energetic, fast]` or `[warm, sincere]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like," "yeah," "okay," "oh my god," "crazy" (first-model word counts, not quotations); "senpai" for seniors
  even in English.
- Thanking gifts: rhythmic, repeated thanks ("thank you so much").
- Sign-off: "okey dokey" … "bye-bye" (two short spans both transcripts share).
- Small failures blamed on sabotage: "It was sabotage." "It's a conspiracy."
- Answering her own questions: "Who would think that's a good idea? Me."
- A flat "bruh" for absurdity; warm "You're doing great" for someone who is struggling.
- Casual swearing: "hell yeah" (shared span); milder curses are first-model observations only.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[loud, theatrical]` | "WAZZUP!! It's your worldwide Rat Idol --- Hakos Baelz!" (official) |
| Telling a story | `[fast, self-mocking]` | "Who would think that's a good idea? Me." |
| A small failure | `[mock outrage]` | "It was sabotage." |
| Mock scandal | `[gasps]` → `[theatrical]` | "Does she really think that me, of all people, is trying to clout chase by using her?" |
| Absurdity | `[deadpan]` | "Bruh." (wiki, secondary) |
| Thanking gifts | `[quick, warm]` | "Welcome to the Rat Pack, welcome, welcome." |
| Cheering someone | `[warm, sincere]` | "Everything gets better. If you're at the bottom, you can only go up. You're doing great." |
| Horror game | `[panicked]` | "I don't like this. I wanna leave." (wiki, secondary) |

With people (provisional): IRyS `[bickering, affectionate]`; Kronii `[teasing]`; Calli and IRyS on CHADCast
`[loud, chaotic]`; Bijou `[playful]`.

## 5. Signature sounds
- "Bruh." (spoken, deadpan).
- `[laughs]`, `[gasps]` (tag only; proposed performance choices, not listening observations).

## 6. Pronunciation
- Untested: listen to how the chosen voice says "Baelz," "Hakos," "Bae" and "Febaerary" and adjust the spelling
  in the script if needed. No phonetic guide is given until a listening check exists.

## 7. Don't
- A slow, sleepy or breathy default; cruelty; a villain voice outside a clear bit; an accent caricature; a
  laugh after every line.

## 8. Example
```
[loud, theatrical] WAZZUP!! It's your worldwide Rat Idol!
[mock outrage] It was sabotage.
[fast, self-mocking] Who would think that's a good idea? Me.
[deadpan] Bruh.
[warm, sincere] Everything gets better. If you're at the bottom, you can only go up. You're doing great.
```
(Line 1 is a shortened official greeting; line 4 is a wiki-listed word; the rest are her lines, quoted only
where both transcripts agree. The delivery tags are proposed performance directions.)



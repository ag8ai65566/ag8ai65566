# One-round claim-check review for GPT

Why (author, 2026-10-01): raise the strength and accuracy of GPT's review. GPT runs at xhigh with live web
search, and the review is still one round, so it must be decisive and verifiable. The exported `## [SW]`
fields matter most, because they are what Sudowrite reads.

You are GPT, reviewing Claude's work for the novel-lab project "holoen", a Sudowrite Story Bible about
hololive members' public personas. This is the only review round. Write in English.

## Project rules that apply
- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.

## What to do, in this order
1. **Claim check of the exported fields.** For every card below, go through each `## [SW]` field and list
   every factual claim (a date, event, song, stage, collab, pair name, quote, nickname, number). Check
   each one against a source you open. Prefer official pages and the primary stream or post. Use the
   dossier's source list first, then search. Give each claim one verdict:
   - `OK`: you opened a source that supports it. Give the URL.
   - `SECONDARY`: only a wiki, mirror or fan source supports it. Give the URL and say whether the card
     should label or soften it.
   - `UNSUPPORTED`: you could not find support. Say what you searched.
   - `WRONG`: a source contradicts it. Give the correct fact, the URL and the exact replacement wording.
   - `SCOPE`: it touches private life (health, family, breaks and their reasons, identity, nationality
     claims, auditions) or presents a performed bit as a real relationship. Give the replacement.
   List only the claims that are not `OK`, plus a count of the `OK` ones per card, so the review stays
   short. Do not skip a card.
2. **Quotation gate.** Every quoted spoken line on a card must be either official, a secondary
   transcription that is labeled as such, or an audio span that both ASR models agree on (the audio
   report lists each verdict). Flag any line that fails, with the fix.
3. **Voice teaching.** Compare Dialogue Style, Catchphrases, Voice & Delivery and Audio Tags with the
   Voice Profile and the audio report. Flag anything the evidence does not support, any measurement used
   as a synthesis target (mixed recordings are not isolated voices), any tag that would imitate a real
   person's voice, and anything that sexualizes a member. Say what is missing that Sudowrite needs to
   perform her (an accent feature, a laugh, a filler, a situation).
4. **Relationships.** Check that each tie is concrete and sourced, that group collabs name only the
   members who took part, that archive counts are not used as rankings, and that the same tie reads the
   same on both people's cards. Then list important ties that are missing, each with a source.
5. **Card usability.** Other Names that would trigger the card for the wrong character; duplicated
   content between fields; anything over the word limits.

## Output format
For each card: `## <card name>`, then `Claims: <n> OK.` and the non-OK claims as a table
`| Field | Claim (short) | Verdict | Source URL | Fix (exact wording) |`, then `MUST:` (numbered, each with the
fix) and `SHOULD:` (short). Then `## Cross-card consistency`, then `## Missing facts worth adding` (each
with a source you opened). End with `## Verification note`: what you could not open or check.

---

## Run budget and scope (Claude, 2026-10-02)
- The author ordered four hololive members from Japan added as full cards (2026-10-02): Hoshimachi Suisei, AZKi,
  Nakiri Ayame and Nekomata Okayu, with their ties to the English cast. This is run B of two: Ayame, Okayu, the world card "JP Senpai Pairs" and the lines about the four added to the English cast's cards (listed at the end). Run A covered Suisei and AZKi.
- They stream in Japanese. Quotes on the cards are Japanese (with romanization and an English gloss); the audio
  reports list both models' renderings. A Japanese quote passes the gate only if the report marks it shared.
  Private life stays out (family, childhood, health, trips, daily routine, how often someone streams, breaks).
- This run must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation,
  so keep to about 15 tool calls in total, including web searches; batch local lookups. Prioritize the exported
  [SW] fields, then the dossier facts dated 2025–2026, then the sheets.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git). The new
  cards are not in `bible/`; their full text is inline below. Do not re-open the inline files.
- If the budget runs short, stop and report what you could not check in the Verification note.

## Card 1: Nakiri Ayame (draft, full file)

---
kind: character
name: "Nakiri Ayame"
sw_section: Characters
---

# Character File: Nakiri Ayame

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Ayame is an active hololive member
> (Japan, 2nd generation) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02) for her ties
> with the English cast. Her recent streams (2026) set her default manner, per the project's recency rule.
> Nothing about the performer behind the avatar: private-life information (family, home, pets, health, eyesight,
> injuries, daily routine, outings, how often she streams and the like) is outside scope and is not recorded
> here, including what the wiki lists or what she mentions in chats. She streams in Japanese; that is recorded
> as the language of her performance only. In stories she knows she is a streamer with a persona (see the world
> card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; AY20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (AY#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (AY20: two windows of a February
> 2026 chat, her February new-outfit stream, a March photo-hunting horror game and a March Resident Evil stream;
> see research/audio-check/ayame.md). Most of the February chat is about personal matters and is not quoted or
> summarized here; only her manner of speaking is used from it. The audio was machine-transcribed and
> acoustically measured; transcripts were reviewed in context, without independent listening verification.

## One-line Concept
"Greetings, Humans!": a kimono-clad oni from the Underworld Academy, its student council president and a
prankster with two swords on her back, who calls herself "Yo" (余, an archaic royal "I"), talks down to
"humans" in fun, laughs until she bangs the desk at a bad pun, and plays FPS games with fast reflexes. [Official
AY1] [Observed AY2 §Personality, secondary; AY3, secondary] [ASR AY20]

## Core Drive
- **Want:** a warm place on stream "where I can smile and have fun together with my viewers"; her official
  dreams are an original solo song (she has several now) and a solo concert. [Official AY1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror games scare her easily; in Resident Evil Requiem (2026) her voice
  shook and she talked herself down ("ochitsuite, ochitsuite," "calm down, calm down"). [Observed AY2 §Trivia,
  secondary] [ASR AY20]
- **Values shown in public:** doing her best at singing and games; reading people carefully before she warms
  up to them. [Official AY1] [Observed AY2 §Personality, secondary]

## Core Contradiction
A haughty oni who addresses her viewers as "ningen-sama" ("honored humans") and claims to look down on them, but
is one of the friendliest, most easily amused members, who giggles at the cheapest pun. [Official AY1]
[Observed AY2 §Personality, secondary; AY3]

## Behavioral Traits
1. Calls herself "Yo" (余) and her viewers "ningen-sama"; "Yo da yo!" ("'Tis I!") is her stock line, and fans
   coined "kawayo" (kawaii + Yo) for her cute moments, a meme her official profile adopts. [Official AY1]
   [Observed AY2 caption, secondary; AY3]
2. Laughs at the slightest thing; bad Japanese puns make her laugh until she bangs the desk and has to stop.
   [Observed AY2 §Personality, secondary]
3. An FPS player with fast reflexes: Apex Legends and VALORANT tournaments (VSaikyou, 4th place in 2023 and in
   2025 with team "Saki Ike Ninja"). [Observed AY2 §Events, secondary; AY4 titles]
4. Bad with directions, a running joke (the fan-made "Docchi Docchi" song, with lyrics she wrote). [Observed AY2
   §Trivia, secondary; AY3]
5. A Pretty Cure fan (she was a guest artist at the series' first virtual music event, 2023) who denies being an
   otaku. [Observed AY2 §Trivia, secondary; AY3]
6. Analytical with new people: she says it takes about five meetings before she knows how to approach someone;
   she was too shy at first to approach Houshou Marine, whom she admires. [Observed AY2 §Personality, secondary]
7. Answers "Why do you have horns?" with "Why don't you humans have horns?"; insists her name is read "Nakiri,"
   not "Hyakki" ("Pressure"). [Observed AY2 §Trivia, secondary] [Official AY1]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "Greetings, Humans! Yoohoo!" (original profile: "Greetings, humans! Nakiri Ayame has arrived!").
    [Official AY1]
  - Stream greeting: "Konnakiri!" [Observed AY2 §Personality, secondary]
  - Stock line: "Yo da yo!" ("'Tis I!"). [Observed AY2 caption, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Yo" (余) for "I"; "ningen-sama" for viewers. [Official AY1 via AY3] [ASR AY20]
  - "Kawayo" → a cute moment (fan meme, on her official profile). [Official AY1]
  - "Nakiri!" (not "Hyakki") → when someone misreads her name. [Official AY1]
- **Vocabulary / fillers:** "nanka," "maji de," "meccha," polite "-masu" with chat at the start, then casual;
  drawn-out sentence endings ("~nā"). [ASR AY20, first-model counts in research/audio-check/ayame.md]
- **Profanity:** light and playful ("yabē," "Urusai!"). [ASR AY20]
- **Politeness:** opens a stream politely ("Kikoete orimasu deshō ka?", "Can you hear me?") and turns casual
  within minutes. [ASR AY20, hhsGMjt_Ix0 0:07:34; both models]
- **Language:** streams in Japanese; with the English cast she appears in shared events (HOLOTALK, team games,
  Anime NYC 2026). [Observed AY5]
- **Laughs, noises:** a quick, cute giggle that tips into helpless laughter; drawn-out wails when something
  hurts or scares her. [Observed AY2 §Personality, secondary] [ASR AY20]
- **Rhythm & rhetoric:** chatty and storytelling, with repeated words for emphasis and teasing scolds at chat
  ("Urusai!" … "Komatta hitotachi," "you troublesome people"). [ASR AY20, 1:36:30–1:36:48; both models]
- **When scared:** "Koe ga furuechau" ("My voice is shaking"); "Ima odorokasaretara hontō ni shinzō ga
  tomarisō" ("If something startles me now, my heart might really stop"). [ASR AY20, E1DuNe3uIrY 0:35:05,
  0:46:00; both models]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (AY20; two 2026 chat windows): window medians about 244–263 Hz (p10–p90 about 177–491 Hz); about
    260–270 transcribed characters a minute of speech, slower than Suisei's chat; higher when excited or scared (her
    outfit reveal and her Resident Evil window, about 283 Hz each). The photo-hunting window mixes in game voices and is not used. Measurements describe the
    sampled recording and ASR segmentation; they are not isolated vocal measurements.
  - Provisional (interpretation): a soft, cute mid-high voice with a playful haughtiness for the oni act,
    breaking into giggles. A listening check would still need to establish timbre details.
- **Sounds off:** a truly cruel or menacing oni; a cold, superior tone without the giggle; a monotone.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Greeting | Bright, playful | "Konnakiri!" (AY2) |
| The oni act | Mock-haughty | "Yo da yo!" (AY2) |
| A bad pun | Giggles, then helpless laughter | [laughs] (AY2) |
| Teasing chat | Pouting scold | "Urusai!" … "Komatta hitotachi." (ASR AY20) |
| FPS clutch | Focused, quick | **Style demo:** "Hidari, hidari! Yo ga iku!" ("Left, left! I'm going in!") |
| Horror game | Scared, shaky | "Koe ga furuechau." … "Ochitsuite, ochitsuite." (ASR AY20) |

### Sample Lines
1. "Greetings, Humans! Yoohoo!" (Official AY1)
2. "It's 'Nakiri'! (Pressure)" (Official AY1, Q&A)
3. "Why don't you humans have horns?" (AY2, secondary)
4. "聞こえておりますでしょうか" — "Kikoete orimasu deshō ka?" ("Can you hear me?", opening a stream) (ASR AY20, hhsGMjt_Ix0 0:07:34)
5. "うるさい" … "困った人たち" — "Urusai!" … "Komatta hitotachi" ("Shut up!" … "You troublesome people") (ASR AY20, 1:36:30–1:36:48)
6. "今驚かされたら本当に心臓が止まりそう" — "Ima odorokasaretara hontō ni shinzō ga tomarisō" ("If something startles me now, my heart might really stop") (ASR AY20, E1DuNe3uIrY 0:46:00)

## Appearance Anchors (avatar)
- 152 cm; illustrator Nana Kagura. Long, loose white hair with pink tints, white horns (one with a small scar,
  per her lore), reddish-pink eyes, bell-ribbon hair ornaments and a red oni mask; a black kimono with red and
  gold accents and spider lilies at the hem, a red-and-white checkered cloth, a green obi with a gold flower
  motif, a large red-and-white bow, long white stockings and zori. Two swords on her back: the black-handled
  cursed blade "Rasetsu" and the red-handled "Asura." [Official AY1] [Observed AY2 §Appearance, §Trivia,
  secondary; AY3]
- Her emoji is 😈; her mascot Poyoyo was made by Shirakami Fubuki; her shikigami are Karma and Shiranui. Later
  looks include a shrine-maiden outfit (2023), a 7th-anniversary kimono with a paper parasol (2025), a white dress
  with a rifle (2025-11) and a pink kimono with a black beret (2026-02-14). [Official AY1] [Observed AY2]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | An oni from the Underworld Academy, its student council president; she pranks people with will-o'-the-wisps | [Official AY1] |
| 2018-09-03 | Debut, hololive 2nd generation (with Minato Aqua, Murasaki Shion, Yuzuki Choco, Oozora Subaru) | [Official AY1] [Observed AY2] |
| 2021-10-03 | First single "Yoi no Yo, Yoi!" | [Observed AY2; AY3] |
| 2022-10-09 | Kiara's HOLOTALK, 23rd guest (season 2 opener) | [AY5 h1EaCnoKhwk] |
| 2023 | "Kawayo"; a guest artist at the Pretty Cure virtual music event (12-09); the hololive Sports Festival white team wins (with Kiara, Mumei, Ame, Nerissa, AZKi) | [Observed AY2; AY3; AY4 tHP7bd8Jtm0] |
| 2024 | "melting"; "Chief VTuber Officer" for Maxell Izumi (12-02) | [Observed AY2; AY3] |
| 2025-01 | "Ame Tokimeki Koimoyō," the anime opening sung with Fubuki and Mio (AyaFubuMi) | [Observed AY2; AY3] |
| 2025-01-13 | On Okayu's team at the New Year Game Festival (with Suisei, Ina, IRyS, Cecilia) | [AY5 THMIBrxnp-E] |
| 2025-09-03 | 7th anniversary: a new 3D kimono and "Hanafubuki" | [Observed AY2] |
| 2025-11-09 | VALORANT VSaikyou, 4th place with "Saki Ike Ninja" | [Observed AY2; AY4] |
| 2026-02-14 | A new pink kimono outfit | [Observed AY2; AY4] |
| 2026-03-06 | hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Okayu, Ina, FUWAMOCO) | [Official AY6] [Observed AY3] |
| 2026-08-22 | Anime NYC: a booth stream with Fubuki and Mio | [Official AY7] |

## Relationship Map
Public exchanges only. Her ties with the English cast and the other three Japanese members on this project are
on the world card "JP Senpai Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Takanashi Kiara | — | HOLOTALK #23 (2022); the 2023 Sports Festival white team | [AY5] [AY4] |
| Nekomata Okayu | "OKFAMS" | With Korone, Fubuki, Mio and Subaru; Okayu's 2025 New Year Game Festival team; 7th fes STAGE 1 | [AY2] [AY5] [Official AY6] |
| Hoshimachi Suisei | — | Okayu's 2025 team | [AY5] |
| AZKi | — | The 2023 Sports Festival white team | [AY4] |
| Ninomae Ina'nis, IRyS, Cecilia Immergreen | — | Okayu's 2025 team; Ina and FUWAMOCO on 7th fes STAGE 1 | [AY5] [Official AY6] |
| Nanashi Mumei, Watson Amelia, Nerissa Ravencroft | — | The 2023 Sports Festival white team | [AY4] |
| Shirakami Fubuki, Ookami Mio | "AyaFubuMi"; FAMS with Subaru | Their 2025 anime opening; Anime NYC 2026 | [AY2] [Official AY7] |
| Oozora Subaru | "AyaSuba" | 2nd-generation genmate; FAMS | [AY2] |
| Murasaki Shion, Minato Aqua | "Manji-gumi" | 2nd-generation unit | [AY2] |
| Inugami Korone | "Onigashima Combi" | — | [AY2] |
| Houshou Marine | admired senpai | She was too shy to approach her at first | [AY2, secondary] |

## Arc
- **Starting point:** active at the 2026 baseline: a new outfit (February), 7th fes on stage, Anime NYC in
  August.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a prank with will-o'-the-wisps; a pun that leaves her laughing too hard to finish a
  sentence; a wrong turn she insists is the right way; an FPS round she carries.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Ayame guides the EN cast to a shrine and takes every wrong turn while insisting "Yo knows the way."
  2. Kiara invites her back to HOLOTALK; Ayame laughs at her own pun before the translation lands.
  3. An FPS night with Ina and IRyS where Ayame calls out positions in Japanese faster than anyone can follow.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2018-09-03; hololive 2nd generation; birthday 13 December; 152 cm; illustrator Nana Kagura; fans
  "Nakiri-gumi" (Nakiri Gang); mascot Poyoyo; emoji 😈; first person "Yo" (余).
- Swords: "Rasetsu" (black handle) and "Asura" (red handle).

## Sources (checked 2026-10-02)
- AY1 Official profile: https://hololive.hololivepro.com/en/talents/nakiri-ayame/
- AY2 Nakiri Ayame wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Nakiri_Ayame
- AY3 Japanese Wikipedia, 百鬼あやめ (secondary): https://ja.wikipedia.org/wiki/百鬼あやめ
- AY4 Stream archive metadata, her channel (archive.ragtag.moe): hhsGMjt_Ix0 (chat, 2026-02-08), 7RG6f33ZOvU
  (new outfit, 2026-02-14), E1DuNe3uIrY (Resident Evil, 2026-03-31), JqaYwRmGKHQ (2026-03-19), tHP7bd8Jtm0
  (Sports Festival 2023), sDMJBt4YLE8 (VSaikyou, 2025-11-09)
- AY5 Other members' archive metadata: see the world card "JP Senpai Pairs" (S1)
- AY6 hololive 7th fes. cast lineup: https://hololivesuperexpo.hololivepro.com/2026/en/fes/cast/
- AY7 Official news, hololive at Anime NYC 2026: https://hololive.hololivepro.com/en/news/20260624-01-216/
- AY20 Claude's audio check (two-model ASR, Japanese): hhsGMjt_Ix0 (2026-02-08), 7RG6f33ZOvU (2026-02-14),
  JqaYwRmGKHQ (2026-03-19), E1DuNe3uIrY (2026-03-31); research/audio-check/ayame.md

---

## [SW] Name
Nakiri Ayame

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 2nd Generation, FAMS, AyaFubuMi, AyaSuba, Manji-gumi, OKFAMS

## [SW] Other Names
Ayame, Ojou, Yo-san

## [SW] Personality
Ayame is a kimono-clad oni from the Underworld Academy and its student council president, a prankster who teases people with will-o'-the-wisps and carries two swords on her back. She calls herself "Yo" (an archaic royal "I"), addresses her viewers as "ningen-sama" ("honored humans") and plays at looking down on them, yet she is one of the friendliest and most easily amused members: she giggles at the slightest thing, and a cheap pun can leave her laughing so hard she bangs the desk. Fans call her "Ojou" (she claims not to know why) and coined "kawayo" for her cute moments. She is a fast-reflexed FPS player who has placed in VTuber tournaments, is scared of horror games, has a famously bad sense of direction, and loves Pretty Cure while denying she is an otaku. With new people she is analytical and takes a while to warm up; once she does, she is warm and devoted. She insists her name is read "Nakiri," and asks, "Why don't you humans have horns?"

## [SW] Background
Ayame is an active hololive member in Japan. She has no supernatural abilities; her lore is a performed persona. She debuted on 2018-09-03 in hololive's 2nd generation with Minato Aqua, Murasaki Shion, Yuzuki Choco and Oozora Subaru. Her originals include "Yoi no Yo, Yoi!", "Kawayo," "melting" and "Hanafubuki"; with Shirakami Fubuki and Ookami Mio (AyaFubuMi) she sang an anime opening in 2025, and her units include FAMS and OKFAMS. She plays in VALORANT tournaments, was a guest artist at a Pretty Cure virtual music event, and streams chats, karaoke and evening drinking talks. With the English cast she was Kiara's HOLOTALK guest (2022), won the 2023 Sports Festival on a team with Kiara, Mumei, Ame, Nerissa and AZKi, played on Okayu's 2025 New Year Game Festival team with Ina, IRyS and Cecilia, shared 7th fes STAGE 1 with Ina and FUWAMOCO (2026), and streamed from the hololive booth at Anime NYC (2026).

## [SW] Physical Description
Ayame's avatar is 152 cm tall, an oni girl with long, loose white hair tinted pink, white horns, reddish-pink eyes, bell-ribbon hair ornaments and a red oni mask. She wears a black kimono with red and gold accents and spider lilies at the hem, a green obi with a gold flower motif, a large red-and-white bow, long white stockings and zori, with two swords on her back: the black-handled "Rasetsu" and the red-handled "Asura."

## [SW] Dialogue Style
Streams in Japanese: chatty and storytelling, with "nanka," "maji de" and "meccha," polite with chat at first and quickly casual. She calls herself "Yo" and her viewers "ningen-sama," greets with "Konnakiri!" and announces herself with "Yo da yo!" ("'Tis I!"). She opens politely ("Kikoete orimasu deshō ka?") and turns casual fast. She giggles constantly, tips into helpless laughter at puns, scolds teasing chat with a pouting "Urusai!" ("Shut up!") or "Komatta hitotachi" ("you troublesome people"), drags out her sentence endings, and in a horror game talks herself down ("Ochitsuite, ochitsuite") while her voice shakes. When a story renders her speech in English or Chinese, keep the archaic royal "Yo" (in Chinese, 余) and the mock-haughty oni act melting into giggles.

## [SW] Catchphrases
"Greetings, Humans! Yoohoo!" (official); "Konnakiri!" (greeting); "Yo da yo!" ("'Tis I!"); "Yo" (余) for "I"; "ningen-sama" (her viewers); "kawayo" (fans' word for her cuteness); "It's 'Nakiri'!"; "Why don't you humans have horns?" Her fans are the Nakiri-gumi (Nakiri Gang).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a soft, cute mid-high voice with a playful, mock-haughty edge for the oni act, chatty and unhurried in conversation, dissolving into quick giggles and helpless laughter; quick and focused in an FPS round; wailing when a horror game scares her. Never truly cruel or cold.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, cute mid-high voice; playful by default. Default tags: [playful, warm]. By situation: greeting [bright, playful]; the oni act [mock-haughty]; a bad pun [giggles] then [laughs harder]; teasing chat [pouting]; FPS clutch [focused, quick]; horror game [scared, whiny]; meeting someone new [shy, careful]. With people (provisional, drawn from Relationships): Fubuki and Mio [comfortable, giggly]; Okayu [teasing]; Kiara [polite, excited]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [giggles] (tag only); "Mō~" (spoken). Keep in the words: "Yo," "ningen-sama," "Konnakiri," "kawayo." Pronunciation guide (provisional, untested): Nakiri Ayame /nɑˈkiɾi ɑˈjɑmeɪ/, Konnakiri /kɔnːɑˈkiɾi/, Yo (余) /joʊ/. Not as default: a cruel or menacing oni; a cold, superior read; a monotone.

## [SW] Motivation
Ayame wants her stream to be a warm place where she and her viewers smile and have fun together, and she gives her best to singing and games; her stated dreams are her own songs and a solo concert.

## [SW] Relationships
Takanashi Kiara: HOLOTALK's 23rd guest (2022) and a 2023 Sports Festival teammate. Nekomata Okayu: "OKFAMS"; Okayu's 2025 New Year Game Festival team, and 7th fes STAGE 1 together. Hoshimachi Suisei, Ninomae Ina'nis, IRyS and Cecilia Immergreen: teammates on Okayu's 2025 New Year Game Festival team; Ina and FUWAMOCO shared her 7th fes stage. AZKi, Nanashi Mumei, Watson Amelia and Nerissa Ravencroft: the winning 2023 Sports Festival white team. Shirakami Fubuki and Ookami Mio: AyaFubuMi (a 2025 anime opening) and FAMS with Oozora Subaru (AyaSuba). Murasaki Shion and Minato Aqua: Manji-gumi. Inugami Korone: "Onigashima Combi." Houshou Marine: a senpai she admires.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hoshimachi Suisei, AZKi, Nakiri
  Ayame and Nekomata Okayu): official profile (AY1), wiki (AY2, by section), Japanese Wikipedia (AY3,
  secondary), archive metadata (AY4, AY5), the 7th fes cast page (AY6), the Anime NYC 2026 news (AY7), and
  Claude's two-model Japanese audio check (AY20, research/audio-check/ayame.md).

## Open Questions
1. Ayame's English-cast ties are team events and shared stages only; enough for her card, or leave it there?


## Audio report: research/audio-check/ayame.md

# Audio check — Nakiri Ayame (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed in Japanese with faster-whisper small (multilingual), pitch measured with Praat (100–600 Hz, speech
segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the
audio was machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used
on the character card were re-transcribed by a second model (whisper medium, multilingual) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Transcription does not write
laughs reliably, and Japanese ASR often picks different kanji or kana for the same word; only spans both models
render identically are quoted. Measurements describe the sampled recording and ASR segmentation; game audio,
music and other voices prevent treating them as isolated vocal measurements.

All windows are from 2026. Only in-scope public performance material is used: personal remarks in the chats
(family, childhood, health, trips, daily life) are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| costume25_2026 | [【新衣装】超超超超かわ余な新衣装お披露目❣👀【百鬼あやめ/ホロライブ】](https://youtu.be/7RG6f33ZOvU) | [0:05:00–0:30:00](https://youtu.be/7RG6f33ZOvU?t=300) | 17.9 | 4991 | 278.4 | 283 Hz | 199–484 Hz |
| horror20_2026 | [【バイオハザード レクイエム】ステルスを覚え始めました。＃2【百鬼あやめ/ホロライブ】](https://youtu.be/E1DuNe3uIrY) | [0:30:00–0:50:00](https://youtu.be/E1DuNe3uIrY?t=1800) | 12.1 | 3379 | 280.2 | 283 Hz | 198–449 Hz |
| talkgame25_2026 | [【誰かの心霊写真】ちゃんとしゃべって百鬼さん（？）【百鬼あやめ/ホロライブ】](https://youtu.be/JqaYwRmGKHQ) | [0:05:00–0:30:00](https://youtu.be/JqaYwRmGKHQ?t=300) | 14.6 | 3140 | 215.0 | 288 Hz | 131–475 Hz |
| chat25b_2026 | [【雑談】おはなししよ？【百鬼あやめ/ホロライブ】](https://youtu.be/hhsGMjt_Ix0) | [1:20:00–1:45:00](https://youtu.be/hhsGMjt_Ix0?t=4800) | 18.8 | 5058 | 268.6 | 244 Hz | 177–443 Hz |
| chat30_2026 | [【雑談】おはなししよ？【百鬼あやめ/ホロライブ】](https://youtu.be/hhsGMjt_Ix0) | [0:00:00–0:30:00](https://youtu.be/hhsGMjt_Ix0?t=0) | 17.1 | 4503 | 263.2 | 263 Hz | 183–491 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | costume25_2026 | horror20_2026 | talkgame25_2026 | chat25b_2026 | chat30_2026 |
|---|---|---|---|---|---|
| first person 僕 (boku) | 1 | 0 | 0 | 0 | 0 |
| first person 私 | 1 | 0 | 1 | 1 | 1 |
| third person すいちゃん | 0 | 0 | 0 | 0 | 2 |
| なんか | 38 | 21 | 19 | 56 | 46 |
| まあ | 5 | 0 | 2 | 16 | 10 |
| ちょっと待って | 0 | 8 | 2 | 0 | 1 |
| やばい | 4 | 2 | 1 | 0 | 4 |
| かわいい | 33 | 0 | 2 | 3 | 0 |
| えっ/え? | 4 | 10 | 1 | 10 | 2 |
| laugh (はは/ふふ/笑) | 0 | 0 | 0 | 0 | 4 |
| swear (くそ/ふざけ/殺) | 0 | 2 | 0 | 0 | 0 |
| ありがとう | 9 | 0 | 0 | 7 | 2 |
| English (Latin letters) | 3 | 2 | 0 | 3 | 2 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Polite with chat at the start, then casual | **Observed**: "Kikoete orimasu deshō ka" ("Can you hear me?") opening the February chat, then casual "maji de," "meccha," "yabē." | [0:07:34](https://youtu.be/hhsGMjt_Ix0?t=454) |
| First person "Yo" (余) | **Observed**; the first model often writes it as 世 ("世が好きな…"), so no line with it is quoted from audio. | [1:22:41](https://youtu.be/hhsGMjt_Ix0?t=4961) |
| Teasing scolds at chat | **Observed**: "Urusai!" … "Mō~" … "komatta hitotachi" ("you troublesome people") when chat teases her. | [1:36:30](https://youtu.be/hhsGMjt_Ix0?t=5790) |
| Scared by horror games | **Confirmed** in Resident Evil Requiem: "Koe ga furuechau" ("my voice is shaking"), "Ima odorokasaretara hontō ni shinzō ga tomarisō" ("if something startles me now my heart might really stop"), a long "ochitsuite, ochitsuite" ("calm down"). | [0:35:07](https://youtu.be/E1DuNe3uIrY?t=2107), [0:46:02](https://youtu.be/E1DuNe3uIrY?t=2762) |
| Persona play | **Observed**: in a photo-hunting horror game (2026-03-19) she talks as a polite narrator who cheers on "Nakiri-san" in the third person. | [0:05:01](https://youtu.be/JqaYwRmGKHQ?t=301) |
| A playful reveal | **Observed** (2026-02-14): she unveils her Valentine's outfit behind a "mosaic roulette," spinning to decide how much to uncover, protests "ステイ！このまま！" ("Stay! Keep it like this!") at a near-miss, and then reads viewers' fan-art guesses. | [0:10:27](https://youtu.be/7RG6f33ZOvU?t=627), [0:13:50](https://youtu.be/7RG6f33ZOvU?t=830) |
| Speech pace and pitch | About 260–270 transcribed characters a minute of speech in chat (slower than Suisei), about 280 in the excited outfit reveal and in the horror game; window medians 244–263 Hz in chat, about 283 Hz in the reveal and the horror game. | — |

Not used: most of the February chat (dance practice, physical complaints, seasonal allergies, taxi rides, gifts, an injury), which is about personal matters. The photo-hunting window mixes in game voices; its pitch figures are not used.

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "聞こえておりますでしょうか" | [0:07:34](https://youtu.be/hhsGMjt_Ix0?t=454) | "ちょっとバタバタしておりましたーすみませんお待たせしましたーこれ聞こえておりますでしょうかちょっと自分の声がうるせぇですねちょっと待ってこんなもんでしょうかどうでしょうか聞こえちゃいますかこんばんはわわ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "うるさい" | [1:36:30](https://youtu.be/hhsGMjt_Ix0?t=5790) | "最近使ってないな持って参るようるさいウェードってちっちゃいよって言うから大きくしたのにごまった人たちくっ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "困った人たち" | [1:36:48](https://youtu.be/hhsGMjt_Ix0?t=5808) | "もう困った人たち声大きいよめんどくせえなもうあれだなこれだなあれやだこれやだ言いやがって" | **Shared span (computed):** whole line (kana/kanji folded) |
| "声が震えちゃう" | [0:35:05](https://youtu.be/E1DuNe3uIrY?t=2105) | "だいぶ近づいたよ、だいぶだいぶガチコン距離で行かせていただいたよし声が震えちゃうこれ何?感染者の血液が入って受血バック使用すると採血キットに補充される採血キットから溢れた分は排気されるえっ、ってことはじゃあ50空きを突っ込んないと排気されちゃうからでも今いけるないけるな入れちゃっ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "今驚かされたら本当に心臓が止まりそう" | [0:46:00](https://youtu.be/E1DuNe3uIrY?t=2760) | "問題はここなんだよねなんか今、今驚かされたら本当に心臓が止まりそう止まってもおかしくないパズルポックスが映っている待って!なに?これは太陽ではないですか?これ、まだこれ、要は手に入れてないやつだよこれこれこれまだ手に入れてない" | **Shared span (computed):** whole line (kana/kanji folded) |
| "落ち着いて落ち着いて" | [0:38:55](https://youtu.be/E1DuNe3uIrY?t=2335) | "落ち着いて落ち着いて殺し切ったほうがいいですから落ち着いてん?落ち着いてよしOK落ち着いて落ち着いて 落ち着いて落ち着け 落ち着け 落ち着け落ち着け 落ち着けいただきましてよしんーで" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いや行きたくねー" | [0:49:05](https://youtu.be/E1DuNe3uIrY?t=2945) | "そもそも出てないからここの先か?まだ見つけられてないここか?いや、行きたくねーいや、行きたくなくて臭っえ、でも行かなきゃ無理だな無理だな、行かなきゃいや、あの先でしょ、絶対え、でもさ、歌姫のことを置いてこんなにさ、ズンズン新エリア開拓してていいのかなっていう気持ちもあるんだけど" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/Nakiri-Ayame.md

# ElevenLabs v4 Performance Sheet: Nakiri Ayame

> Built from `bible/characters/Nakiri-Ayame.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Ayame is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft and cute mid-high voice with a playful, mock-haughty edge; chatty and
unhurried, dissolving into quick giggles; shaky and breathless when frightened."
- Register basis: 2026 chat windows measured about 244–263 Hz window medians, higher when scared
  (`research/audio-check/ayame.md`).

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
| Greeting | `[bright, playful]` | "Konnakiri!" |
| The oni act | `[mock-haughty]` | "Yo da yo!" |
| Opening a stream | `[polite, careful]` | "Kikoete orimasu deshō ka?" |
| Teasing chat | `[pouting]` | "Urusai!" … "Komatta hitotachi." |
| Horror game | `[scared, shaky]` | "Ima odorokasaretara hontō ni shinzō ga tomarisō." |
| A bad pun | `[giggles]` → `[laughs harder]` | (tag only) |

With people (provisional): Fubuki and Mio `[comfortable, giggly]`; Okayu `[teasing]`; Kiara `[polite, excited]`.

## 5. Signature sounds
- `[giggles]` (tag only); "Mō~" (spoken).

## 6. Pronunciation (provisional; test)
- Nakiri Ayame `/nɑˈkiɾi ɑˈjɑmeɪ/` · Konnakiri `/kɔnːɑˈkiɾi/` · Yo (余) `/joʊ/`

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
(Line 2 is her greeting from the wiki; lines 1, 3–5 are her lines, quoted only where both transcripts agree.)


## Card 2: Nekomata Okayu (draft, full file)

---
kind: character
name: "Nekomata Okayu"
sw_section: Characters
---

# Character File: Nekomata Okayu

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Okayu is an active hololive member
> (Japan, hololive GAMERS) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02) for her
> ties with the English cast. Her recent streams (2026) set her default manner, per the project's recency rule.
> Nothing about the performer behind the avatar: private-life information (family, home, region, pets, health,
> friendships from before her debut and the like) is outside scope and is not recorded here, including what the
> wiki lists or what she mentions in chats. Her lore (a cat raised by an old woman who runs an onigiri shop) is
> persona only. She streams in Japanese; that is recorded as the language of her performance only. In stories
> she knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; OK20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (OK#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (OK20: a Moero!! Holo Yakyū
> stream, a Mina the Hollower stream and a Final Fantasy VII Rebirth stream, about 50 minutes of speech; see
> research/audio-check/okayu.md). Lines she reads from the games are not quoted; the baseball window has voiced
> members and crowd audio and is not used for voice measurements. A remark about her off-stream schedule is not
> used. The audio was machine-transcribed and
> acoustically measured; transcripts were reviewed in context, without independent listening verification.

## One-line Concept
"Om nom, Okayu!": a lazy-voiced, boyish cat of hololive GAMERS who calls herself "boku," flirts with everyone to
see their reactions, gets found "guilty" in Okayu Court and serves her sentence without protest, agrees with
everything as the "all-affirming cat," and cries at the end of a good game. [Official OK1] [Observed OK2
§Personality, secondary; OK3, secondary] [ASR OK20]

## Core Drive
- **Want:** to enjoy each day to the maximum, "singing, dancing, and gaming included," and to be "all
  lovey-dovey" with her fans (her official dream); she joined, she says, "purely out of my love for gaming."
  [Official OK1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** none sourced; she takes teasing and "guilty" verdicts in stride.
- **Values shown in public:** affirming people ("all-affirming," the official word); sharing games with chat;
  loyalty to her GAMERS and her many unit partners. [Official OK1] [Observed OK2]

## Core Contradiction
A relaxed, laid-back cat with a low, lazy voice, who is also the flirt of hololive (fans call her a "harem
protagonist") and who breaks into tears at an emotional game ending. [Observed OK2 §Personality,
§Miscellaneous, secondary] [Official OK1]

## Behavioral Traits
1. Flirts with members and chat to see their reactions; her official profile lists "intense flirting" as a hobby
   ("'Gross.' That one word gives me life."). Keep it teasing and non-explicit. [Official OK1] [Observed OK2
   §Personality, secondary]
2. "Okayu Court": she has been found guilty in several fan-run "cases" (food swiped, mischief), never denies it,
   and serves her sentence obediently; her fans' mascot is a prisoner with a rice-ball head. [Observed OK2
   §Personality, §Fans, secondary] [Official OK1 "guilty cat"]
3. The "all-affirming cat" (zenkōtei): she agrees with everything, "so much, I'm a terrible straight man."
   [Official OK1]
4. Calls herself "boku" (a boyish "I"); rarely uses cute nicknames for others (Inugami Korone is "Koro-san").
   [Observed OK3, secondary; OK2 §Miscellaneous, secondary] [ASR OK20]
5. Laughs easily, and at full laugh lets out a high, bird-like whistle ("I keep a bird in my throat," she says).
   [Observed OK3, secondary]
6. A gamer of RPGs, roguelikes, retro and pixel games (Final Fantasy VII from 2026, Mina the Hollower, Star Fox);
   she cried on stream at the end of Link's Awakening. [Official OK1] [Observed OK2; OK4 titles]
7. Plays games "by vibes" ("Hai, nori de aite o buttaoshitai to omoimāsu," "Okay, I'm going to beat them on
   vibes"), enjoys learning a new game blind with chat, purrs "nya nya nya" when a move feels good, and makes the
   odd pun ("Ki dake ni?"). She is a self-described fan of FUWAMOCO. [ASR OK20] [Observed OK2 §Likes, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "Om nom, Okayu! Nekomata Okayu here!" (Japanese: "Mogu mogu~ Okayu~! Hororaibu Gēmāzu no Nekomata
    Okayu desu!"). Her viewers answer "gochi gochi!" ("thanks for the meal") at the end of a stream. [Official
    OK1] [Observed OK3; OK2 §Fans, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Mogu mogu" (the sound of chewing) → greeting. [Official OK1] [Observed OK2]
  - "Onigiryā" → addressing her fans. [ASR OK20] [Official OK1]
  - "Nori de" ("by vibes") → starting a game without finishing the tutorial: "Hai, nori de aite o
    buttaoshitai to omoimāsu." [ASR OK20, lTRy_mp5ODI 0:20:37; both models]
  - "Nya nya nya nya" → a move that feels good. [ASR OK20, mDwTkQBtFQE 0:29:12; both models write nya]
  - "Rettsura gō!" ("Let's go!") → starting the day's game. [ASR OK20]
  - Pleading in a playful tease → **Style demo:** "Boku to issho ni asonde kuremasen ka?" ("Won't you play with
    me?"; after her own 2024 Mario Party title). [Observed OK4 title WnKCmQ2iXww]
- **Vocabulary / fillers:** "boku," polite "-masu" endings mixed with relaxed ones, drawn-out vowels ("~"),
  "sugoi," "hai hai hai." [ASR OK20, first-model counts in research/audio-check/okayu.md]
- **Profanity:** rare; flirty teasing rather than swearing. [ASR OK20]
- **Language:** streams in Japanese; with the English cast she sings and plays in Japanese with simple English.
  [Observed OK5]
- **Laughs, noises:** easy laughter rising to a high, whistling squeak at its peak. [Observed OK3, secondary]
- **Rhythm & rhetoric:** relaxed and unhurried, often narrating what she is doing in a game; sentences trail off
  in long vowels. [ASR OK20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (OK20; two 2026 game windows): window medians about 261–262 Hz (p10–p90 about 131–464 Hz); her
    lower range reaches further down than the other three Japanese members checked (p10 about 131–155 Hz against
    about 160–200 Hz), though the medians are similar; about 240–255 transcribed characters a minute of speech.
    Game audio is mixed in; the measurements describe the sampled recordings, not an isolated voice.
  - Provisional (interpretation): a soft, relaxed, boyish voice that sits low for hololive and is lazy and warm,
    lifting into a playful purr for teasing; her laugh climbs high. "Low" is a style description (Japanese
    Wikipedia, secondary), only partly supported by the measurements. A listening check would still need to
    establish timbre details.
- **Sounds off:** a high, sugary idol default; harsh or aggressive delivery; anything explicit in her flirting.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Greeting | Lazy, warm | "Mogu mogu~ Okayu~!" (OK1) |
| Teasing a member | Low, playful purr | **Style demo:** "Kawaii nē. Boku no tokoro ni kuru?" ("Cute. Want to come over to my side?") |
| Found guilty | Unbothered, cheerful | **Style demo:** "Hai, yūzai desu. Tsugunaimasu." ("Yes, guilty. I'll serve my time.") |
| Starting a game | Breezy | "Hai, nori de aite o buttaoshitai to omoimāsu." (ASR OK20) |
| Exploring a new game | Contented, chatty | "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā." (ASR OK20) |
| Emotional game ending | Soft, tearful | **Style demo:** "Chotto matte… namida ga…" ("Wait… the tears…") |
| Laughing hard | Rising to a squeak | [laughs] (OK3) |

### Sample Lines
1. "Om nom, Okayu! Nekomata Okayu here!" (Official OK1)
2. "'Gross.' That one word gives me life." (Official OK1, on flirting)
3. "I do it so much, I'm a terrible straight man." (Official OK1, on being all-affirming)
4. "はい、ノリで相手をぶっ倒したいと思いまーす" — "Hai, nori de aite o buttaoshitai to omoimāsu" ("Okay, I'm going to beat them on vibes") (ASR OK20, lTRy_mp5ODI 0:20:37)
5. "新しいゲームだから、みんなと一緒に手探り探索なの楽しいなぁ" — "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā" ("It's a new game, so feeling our way through it together is fun") (ASR OK20, mDwTkQBtFQE 0:27:58)
6. "僕野球はね" — "Boku yakyū wa ne…" ("Me, baseball, well…") (ASR OK20, lTRy_mp5ODI 0:05:06)

## Appearance Anchors (avatar)
- 152 cm; illustrator Kamioka Chiroru. Medium-length light purple hair, purple cat ears (one pair, no human
  ears) and a tail, bright purple eyes; an off-black, purple-tinted hoodie and a black collar. [Official OK1]
  [Observed OK2 §Appearance, §Lore, secondary]
- Her emoji is 🍙. Later looks include a Cheshire Cat-inspired outfit (2023), long twintails (2024), a
  purple cat-print jacket outfit used for her 2025 solo concert, and a maid outfit in the 2026 game hololive
  Dreams. [Observed OK2 §2023–§2025, secondary; OK4]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | A cat raised by an old woman who runs an onigiri shop; she streams from the computer in the old woman's room | [Official OK1] |
| 2019-04-06 | Debut in hololive GAMERS (with Shirakami Fubuki, Ookami Mio, Inugami Korone) | [Observed OK2; OK3] |
| 2021-11-27 | Kiara's HOLOTALK, 18th guest (the show's first-anniversary episode) | [OK5 FjsTGuBQlO0] |
| 2022-09-30 | First solo concert "Poison-nya Syndrome" | [Observed OK3] |
| 2023-12-12 | Team Mario Kart with Hakos Baelz and FUWAMOCO among others | [OK5 Janl2FCKmsg] |
| 2024 | Guest at Nanashi Mumei's 3D live "Outside the Box"; first GAMERS fes (Yoyogi) | [Mumei file] [Observed OK3] |
| 2024-08-10 PDT | Cameo with Inugami Korone at FUWAMOCO's 3D debut | [FUWAMOCO card] |
| 2024-09-15 | A pop-up Mario Party with Mori Calliope, Anya Melfissa and Hiodoshi Ao | [OK4 WnKCmQ2iXww] |
| 2025-01-13 | Leads a team at the hololive New Year Game Festival (with Suisei, Ayame, Ina, IRyS, Cecilia) | [OK4 THMIBrxnp-E] |
| 2025-05-15/28 | 2 million subscribers; second solo concert "PERSONYA RESPECT" at Pia Arena MM (FUWAMOCO watch it together) | [Observed OK2] [OK5 gzPgXfYAbGg] |
| 2025-07-05/06 | GAMERS fes 2 at Saitama Super Arena | [Observed OK2; OK3] |
| 2025-08-04 | "Kurukuru Cruise" with Ninomae Ina'nis (Mythmash) | [OK5 t7lNu-p_ANs] |
| 2026-03-06 | hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Ayame, Ina, FUWAMOCO) | [Official OK6] [Observed OK3] |
| 2026 | The game sequel "Okayu Nyūmu! R," which she stars in and supervises; Final Fantasy VII playthrough series | [Observed OK3; OK4] |

## Relationship Map
Public exchanges only. Her ties with the English cast and the other three Japanese members on this project are
on the world card "JP Senpai Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Ninomae Ina'nis | "TakoNeko" | Duets; "Kurukuru Cruise" (2025); Ina on her 2025 New Year Game Festival team; both on 7th fes STAGE 1 | [OK5] [OK2] [Official OK6] |
| FUWAMOCO (Fuwawa, Mococo) | kouhai she is a fan of | Her cameo at their 3D debut (2024); their watch-along of her 2025 solo concert ("respect to our sultry cat senpai"); a 2025 short with Korone | [FUWAMOCO card] [OK5] |
| Takanashi Kiara | — | HOLOTALK #18 (2021) | [OK5] |
| Nanashi Mumei (graduated) | — | Guest at Mumei's "Outside the Box" (2024) | [Mumei file] |
| Mori Calliope | — | A pop-up Mario Party (2024) | [OK4] |
| Gigi Murin | "OkaGigi" | A pair name only; no shared activity sourced | [OK2, secondary] |
| IRyS, Cecilia Immergreen | — | Her 2025 New Year Game Festival team | [OK4] |
| Hakos Baelz | — | Team kart events (2023, 2024) | [OK4] |
| Hoshimachi Suisei | "MOMAS" | With Sakura Miko, Houshou Marine and Hiodoshi Ao; PlateUp! on her 2025 team | [OK2] [OK4] |
| Nakiri Ayame | "OKFAMS" | With Korone, Fubuki, Mio and Oozora Subaru; her 2025 team | [OK2] [OK4] |
| Inugami Korone | "OkaKoro" | Her best-known partner ("Koro-san"); duets and the GAMERS | [OK2] |
| Shirakami Fubuki, Ookami Mio | GAMERS; "NYANGUCORN," "MiOKayu" | GAMERS fes; Fubuki and Okayu's April Fools furball models (2026) | [OK2] |
| Oozora Subaru | "SubaOka" | "SASHIMIO feat. SubaOka"; a 2026 off-collab lottery | [Official OK1 music list] [OK4] |

## Arc
- **Starting point:** active at the 2026 baseline: a long Final Fantasy VII series, a game she supervises, and
  7th fes on stage.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a flirt aimed at the most flustered person in the room; a "crime" (a swiped snack) she
  confesses to at once; agreeing with both sides of an argument; tears at a game ending.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. FUWAMOCO put Okayu on trial for eating their snacks; she pleads guilty before they finish the charge.
  2. Ina and Okayu rehearse "Kurukuru Cruise" and Okayu agrees with every note change.
  3. Okayu flirts with Calli to see her react; Calli's deflection makes Okayu laugh until she squeaks.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
Her flirting is a playful, non-explicit bit to see people react; keep it light. No romance is implied.

## Hard Facts (continuity)
- Debut 2019-04-06; hololive GAMERS; birthday 22 February; 152 cm; illustrator Kamioka Chiroru; fans
  "Onigiryā" (Onigiris); emoji 🍙; stream tag #生おかゆ.
- First person "boku"; greeting "Mogu mogu~ Okayu~!"

## Sources (checked 2026-10-02)
- OK1 Official profile: https://hololive.hololivepro.com/en/talents/nekomata-okayu/
- OK2 Nekomata Okayu wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Nekomata_Okayu
- OK3 Japanese Wikipedia, 猫又おかゆ (secondary): https://ja.wikipedia.org/wiki/猫又おかゆ
- OK4 Stream archive metadata, her channel (archive.ragtag.moe): lTRy_mp5ODI (Moero!! Holo Yakyū, 2026-04-20),
  vrnsDry3DNY (FF7 Rebirth, 2026-08-09), 13b0KIFqcMU (Subnautica 2, 2026-06-12), rncGib1nrV0 (Resident Evil 0,
  2026-04-28), mDwTkQBtFQE (Mina the Hollower, 2026-06-16), THMIBrxnp-E and eAMpppCtNpk (her 2025 team),
  WnKCmQ2iXww (Mario Party with Calli), qRAHAMyDRTQ and bn4KiWOwyOc (kart events), CWRVS_VtrrY (with Subaru)
- OK5 Other members' archive metadata: see the world card "JP Senpai Pairs" (S1)
- OK6 hololive 7th fes. cast lineup: https://hololivesuperexpo.hololivepro.com/2026/en/fes/cast/
- OK20 Claude's audio check (two-model ASR, Japanese): lTRy_mp5ODI (2026-04-20), mDwTkQBtFQE (2026-06-16),
  vrnsDry3DNY (2026-08-09); research/audio-check/okayu.md

---

## [SW] Name
Nekomata Okayu

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive GAMERS, OkaKoro, SMOK, OKFAMS, MOMAS, TakoNeko, SubaOka

## [SW] Other Names
Okayu, Okayun, Nekomata

## [SW] Personality
Okayu is a relaxed, free-spirited cat of hololive GAMERS: in her lore she was raised by an old woman who runs an onigiri shop and streams from the computer in the old woman's room. She calls herself "boku," talks in a low, lazy, boyish voice, and loves to flirt with members and chat just to see how they react ("'Gross.' That one word gives me life"), which earned her the fan nickname of a harem protagonist. She is the "all-affirming cat" who agrees with everything, and the "guilty cat" of fan-run Okayu Court, where she never denies her crimes (usually swiped food) and serves her sentence without protest. She laughs easily and, at full laugh, lets out a high, bird-like whistle. A true gamer of RPGs, roguelikes and retro games, she starts games "by vibes," and can break down in tears at an emotional ending. She rarely uses cute nicknames for others and is a self-declared fan of FUWAMOCO.

## [SW] Background
Okayu is an active hololive member in Japan. She has no supernatural abilities; her lore is a performed persona. She debuted on 2019-04-06 in hololive GAMERS with Shirakami Fubuki, Ookami Mio and Inugami Korone, whose duo "OkaKoro" is her best-known pairing. A singer as well as a gamer, she has held two solo concerts ("Poison-nya Syndrome," 2022; "PERSONYA RESPECT," 2025), reached two million subscribers in 2025, performs at the GAMERS concerts and stars in and supervises her own game, "Okayu Nyūmu!" and its 2026 sequel. With the English cast she is "TakoNeko" with Ninomae Ina'nis, who sang "Kurukuru Cruise" with her (2025); she made a cameo at FUWAMOCO's 3D debut and the twins watched her 2025 concert together; she was Kiara's HOLOTALK guest (2021) and a guest at Mumei's 3D live (2024), and led a 2025 New Year Game Festival team with Ina, IRyS and Cecilia.

## [SW] Physical Description
Okayu's avatar is 152 cm tall, a cat girl with medium-length light purple hair, purple cat ears and a tail, and bright purple eyes. She wears an off-black, purple-tinted hoodie and a black collar. Her emoji is a rice ball (🍙).

## [SW] Dialogue Style
Streams in Japanese in a low, lazy, relaxed voice: "boku" for "I," polite "-masu" endings mixed with easygoing ones, long trailing vowels and "hai hai hai." She greets with "Mogu mogu~ Okayu~!" ("Om nom, Okayu!"), calls her fans "Onigiryā," starts games "nori de" ("by vibes": "Hai, nori de aite o buttaoshitai to omoimāsu," "Okay, I'm going to beat them on vibes"), narrates what she is doing as she plays, purrs "nya nya nya" when a move feels good and slips in the odd pun. Her flirting is a low, playful tease to see people react; she accepts "guilty" verdicts cheerfully and agrees with everyone. Her laugh climbs into a high squeak. She uses plain names, not cute nicknames ("Koro-san"). When a story renders her speech in English or Chinese, keep the boyish "boku" register, the unhurried pace and the teasing warmth.

## [SW] Catchphrases
"Om nom, Okayu! Nekomata Okayu here!" ("Mogu mogu~ Okayu~!," official greeting); "mogu mogu"; "Onigiryā" (her fans); "nori de" ("by vibes"); "nya nya nya"; "Rettsura gō!" ("Let's go!"); "'Gross.' That one word gives me life." (official, on flirting); "all-affirming cat" and "guilty cat" (how her fans describe her, per her official profile). Her viewers sign off with "gochi gochi!"

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a low, soft, boyish voice, lazy and warm, unhurried, with long trailing vowels; a playful purr for teasing; a laugh that climbs to a high squeak. Never a sugary idol default and never harsh; her flirting stays light and non-explicit.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): low, soft, boyish voice; relaxed and unhurried by default. Default tags: [relaxed, low]. By situation: greeting [lazy, warm]; teasing a member [playful, low purr]; found guilty [cheerful, unbothered]; agreeing with everyone [easygoing]; game by vibes [breezy]; emotional game ending [soft, tearful]; laughing hard [laughs harder]. With people (provisional, drawn from Relationships): Korone [comfortable, fond]; Ina [mellow, harmonizing]; FUWAMOCO [fond senpai, teasing]; Calli [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "mogu mogu" (spoken); "nya nya nya" (spoken, a pleased purr); [laughs] (tag only). Keep in the words: "boku," "mogu mogu," "Onigiryā," "nori de." Pronunciation guide (provisional, untested): Nekomata Okayu /nɛkoʊˈmɑtɑ oʊˈkɑju/, Onigiryā /oʊniˈɡiɾjɑː/. Not as default: a high, sugary voice; harsh or aggressive delivery; explicit flirting.

## [SW] Motivation
Okayu wants to enjoy every day to the fullest with games, songs and dances, and to share them with her fans and the members she loves; she likes seeing people react, and she likes saying yes.

## [SW] Relationships
Ninomae Ina'nis: "TakoNeko"; duets and the Mythmash single "Kurukuru Cruise" (2025), teammates at the 2025 New Year Game Festival. FUWAMOCO: kouhai she is a fan of; her cameo at their 3D debut (2024), and they watched her 2025 solo concert together ("our sultry cat senpai"). Takanashi Kiara: HOLOTALK's 18th guest (2021). Nanashi Mumei (graduated): a guest at Mumei's 3D live (2024). Mori Calliope: a pop-up Mario Party (2024). Gigi Murin: "OkaGigi," a pair name. IRyS and Cecilia Immergreen: her 2025 New Year Game Festival team. Hakos Baelz: kart events. Hoshimachi Suisei: "MOMAS." Nakiri Ayame: "OKFAMS." Inugami Korone: "OkaKoro," her best-known partner, whom she calls "Koro-san." Shirakami Fubuki and Ookami Mio: her GAMERS. Oozora Subaru: "SubaOka."

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hoshimachi Suisei, AZKi, Nakiri
  Ayame and Nekomata Okayu): official profile (OK1), wiki (OK2, by section), Japanese Wikipedia (OK3,
  secondary), archive metadata (OK4, OK5), the 7th fes cast page (OK6), and Claude's two-model Japanese audio
  check (OK20, research/audio-check/okayu.md).

## Open Questions
1. "OkaGigi" has no sourced shared activity; keep it as a pair name only?
2. Her flirting is part of her official profile; is the non-explicit framing here the right level for stories?


## Audio report: research/audio-check/okayu.md

# Audio check — Nekomata Okayu (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed in Japanese with faster-whisper small (multilingual), pitch measured with Praat (100–600 Hz, speech
segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the
audio was machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used
on the character card were re-transcribed by a second model (whisper medium, multilingual) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Transcription does not write
laughs reliably, and Japanese ASR often picks different kanji or kana for the same word; only spans both models
render identically are quoted. Measurements describe the sampled recording and ASR segmentation; game audio,
music and other voices prevent treating them as isolated vocal measurements.

All windows are from 2026. Only in-scope public performance material is used: personal remarks in the chats
(family, childhood, health, trips, daily life) are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| game20c_2026 | [【 萌えろ!!ホロ野球 】ぷれいぼ～～～る！⚾✦【 猫又おかゆ/ホロライブ 】](https://youtu.be/lTRy_mp5ODI) | [0:05:00–0:25:00](https://youtu.be/lTRy_mp5ODI?t=300) | 13.5 | 2651 | 196.4 | 296 Hz | 146–495 Hz |
| pixel25_2026 | [【 🔴Mina the Hollower 】ソウルライク × 2Dゼルダ!? 神ドットゲー✦#0](https://youtu.be/mDwTkQBtFQE) | [0:10:00–0:35:00](https://youtu.be/mDwTkQBtFQE?t=600) | 17.2 | 4106 | 238.8 | 261 Hz | 154–449 Hz |
| game30_2026 | [【 FF7リバース 】みんなと冒険だああ!! #08 ｜ FINAL FANTASY VII R](https://youtu.be/vrnsDry3DNY) | [0:05:00–0:35:00](https://youtu.be/vrnsDry3DNY?t=300) | 19.0 | 4819 | 253.8 | 262 Hz | 131–464 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | game20c_2026 | pixel25_2026 | game30_2026 |
|---|---|---|---|
| first person 僕 (boku) | 3 | 4 | 3 |
| first person 私 | 0 | 4 | 5 |
| なんか | 2 | 12 | 11 |
| まあ | 2 | 8 | 7 |
| ちょっと待って | 0 | 1 | 0 |
| やばい | 2 | 4 | 0 |
| かわいい | 3 | 1 | 1 |
| えっ/え? | 3 | 4 | 6 |
| laugh (はは/ふふ/笑) | 3 | 1 | 5 |
| swear (くそ/ふざけ/殺) | 0 | 1 | 0 |
| ありがとう | 1 | 0 | 1 |
| English (Latin letters) | 2 | 0 | 3 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| First person "boku" | **Confirmed** throughout (e.g. "Boku yakyū wa ne…," both models). | [0:05:06](https://youtu.be/lTRy_mp5ODI?t=306) |
| Calls her fans "Onigiryā" | **Confirmed** (both models), while picking teammates in a baseball game. | [0:23:35](https://youtu.be/lTRy_mp5ODI?t=1415) |
| Plays "by vibes" | **Confirmed**: "Hai, nori de aite o buttaoshitai to omoimāsu" ("Okay, I'm going to beat them on vibes"), after skipping part of a tutorial (both models). | [0:20:37](https://youtu.be/lTRy_mp5ODI?t=1237) |
| Enjoys exploring a new game with chat | **Confirmed**: "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā" (both models). | [0:27:58](https://youtu.be/mDwTkQBtFQE?t=1678) |
| Puns | **Observed**: a pun on "ki" (tree / mind): "Ki ga sa… ki dake ni?" (both models). | [0:32:35](https://youtu.be/mDwTkQBtFQE?t=1955) |
| Cat noises when pleased | **Observed**: "nya nya nya nya nya" while swinging a weapon (both models write nya; the exact count differs). | [0:29:12](https://youtu.be/mDwTkQBtFQE?t=1752) |
| Relaxed, narrating play style | **Observed**: she reads game text aloud in a calm voice and narrates her choices; "Rettsura gō" to start. Lines she reads from the game are not her own and are not quoted. | — |
| Low voice | **Partly supported**: her lower range reaches further down than the other three (p10 about 131–155 Hz against about 160–200 Hz), but window medians (about 260 Hz) are similar; game audio is mixed in. Treat "low, boyish" as a style description, not a measured fact. | — |
| Laugh rising to a whistle | **Not checked** (whisper does not write laughs); kept from the Japanese Wikipedia (secondary). | — |

Not used: a story about her off-stream schedule at the start of the Final Fantasy VII window, and a stream title about an illness (personal matters). The Moero!! Holo Yakyū window has voiced members and crowd audio; its pitch figures are not used.

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "僕野球はね" | [0:05:06](https://youtu.be/lTRy_mp5ODI?t=306) | "でもいけますやる気満々じゃん えー楽しみ僕野球はね見はしますけどゲームの経験とあんまりない のですよね楽しみです ならだいぶキャラ多いよねなのかなぁ同山所蔵" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ノリで相手をぶっ倒したいと思いまーす" | [0:20:37](https://youtu.be/lTRy_mp5ODI?t=1237) | "はいノリで相手をぶっ倒したいと思いまーすホロライブリーグやってみましょうか まあノリで行きましょうホロライブリーグヘルプ えーホロライブリーグは選んだホロメン2人でチームを組んでリーグを勝ち抜いていく一人用モードですうー" | **Shared span (computed):** whole line (kana/kanji folded) |
| "おにぎりゃー" | [0:23:35](https://youtu.be/lTRy_mp5ODI?t=1415) | "おねがいしますお待たせあ!すごーい!おにぎりゃー コロネスキー コロネスキーおにぎりゃー ポコベいるんだけどーおにぎりゃー ミオファーこれ買えれるのかな?ここは固定なのね味噌スープとマトンカレーあ、超えれるー!" | **Shared span (computed):** whole line (kana/kanji folded) |
| "新しいゲームだから、みんなと一緒に手探り探索なの楽しいなぁ" | [0:27:58](https://youtu.be/mDwTkQBtFQE?t=1678) | "ねーすごいこの人ー 気象が荒いわーいやいいね新しいゲームだからみんなと一緒に手探り探索なの楽しいなぁここは? なんか上のやつを下ろすとショートカットで橋に登り降りできるようになるって感じっぽいね オッケーオッケーん いろいろチョコの" | **Shared span (computed):** whole line (kana/kanji folded) |
| "木がさ" | [0:32:35](https://youtu.be/mDwTkQBtFQE?t=1955) | "登っていこっかぁよしこのねー木がさ、当選簿してんの気になるけど木だけに?ふふっでも多分まだ開けられないんだろうねーよいしょーどん!あっあっ!やばい!強そう強そう強そう強そう!強そう強そう強そう!" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ニャニャニャニャニャ" | [0:29:12](https://youtu.be/mDwTkQBtFQE?t=1752) | "はっはっは、よしいや結構このブーメラン強い気がするにゃんにゃにゃにゃーにゃーにゃーにゃーにゃーにゃーにゃーあはははは音楽めっちゃいいにゃんにゃんにゃーにゃーひゃー、ぴよっ、あっひゃーご視聴ありがとうございました" | **Shared span (computed):** whole line (kana/kanji folded) |
| "びっくりしたもやめてよー" | [0:14:20](https://youtu.be/mDwTkQBtFQE?t=860) | "あ ちょっとびっくりした もうやめてよこれにする あ 他の武器も自由に試すといい 準備ができたら交番に上がっても安心だこの騒ぎクラー券の仕業じゃねえといいんだがなぁ くれぐれも気をつけろあ、ほんとだ" | **Partial (computed):** shared run "びっくりしたも"; only that part is quoted |
| "レッツラゴー" | [0:08:55](https://youtu.be/vrnsDry3DNY?t=535) | "またあれかな 今日霧の良いところで終われたら遊びに行ってみようかなではではレッツラゴーロードゲームえーこれですねちょっと今さっき潜ってやり残しってどのぐらいあるかなーって見てたんでどんぐらい当てたんだろう昨日のセーブデータがこれか" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/Nekomata-Okayu.md

# ElevenLabs v4 Performance Sheet: Nekomata Okayu

> Built from `bible/characters/Nekomata-Okayu.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Okayu is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft, relaxed, boyish voice that sits low; lazy and warm, unhurried with
trailing vowels, a playful low purr when teasing, a laugh that climbs high."
- Register basis: 2026 game windows measured about 261–262 Hz window medians with a low floor (p10 about
  131–155 Hz) (`research/audio-check/okayu.md`). "Low" is a style choice; keep it natural.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (relaxed and steady). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[relaxed, low]` or `[playful, low purr]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Boku" for "I"; "Mogu mogu~ Okayu~!" to greet; "Onigiryā" for her fans.
- "Nori de" (by vibes); "Rettsura gō!"; a pleased "nya nya nya".
- Narrating her own play in long, relaxed sentences; agreeing with everyone.
- Flirty teasing kept light and non-explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[lazy, warm]` | "Mogu mogu~ Okayu~!" (official) |
| Starting a game | `[breezy]` | "Hai, nori de aite o buttaoshitai to omoimāsu." |
| Exploring a new game | `[contented, chatty]` | "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā." |
| A move that feels good | `[pleased]` | "Nya nya nya nya." |
| Teasing a member | `[playful, low purr]` | "Kawaii nē." (style demo) |
| Laughing hard | `[laughs harder]` | (tag only) |

With people (provisional): Korone `[comfortable, fond]`; Ina `[mellow]`; FUWAMOCO `[fond senpai, teasing]`.

## 5. Signature sounds
- "mogu mogu" (spoken); "nya nya nya" (spoken); `[laughs]` (tag only).

## 6. Pronunciation (provisional; test)
- Nekomata Okayu `/nɛkoʊˈmɑtɑ oʊˈkɑju/` · Onigiryā `/oʊniˈɡiɾjɑː/`

## 7. Don't
- A high, sugary voice; harsh or aggressive delivery; explicit flirting.

## 8. Example
```
[lazy, warm] Mogu mogu~ Okayu~!
[breezy] Hai, nori de aite o buttaoshitai to omoimāsu.
[contented, chatty] Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā.
[pleased] Nya nya nya nya.
[playful, low purr] Kawaii nē.
```
(Line 1 is her official greeting; line 5 is a style demo; lines 2–4 are her lines, quoted only where both
transcripts agree.)


## Card 3: JP Senpai Pairs (draft, full file)

---
kind: world
name: "JP Senpai Pairs"
sw_section: Worldbuilding
---

# World Element: JP Senpai Pairs (Suisei, AZKi, Ayame, Okayu with the cast)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-02. Evidence labels as in the other world files. "Archive" = stream titles and
> descriptions on the members' channels (archive.ragtag.moe, S1); a title shows that a collab happened, not how
> close the members are. Hoshimachi Suisei, AZKi, Nakiri Ayame and Nekomata Okayu are active hololive members
> (Japan) at the 2026-09-30 baseline; they were added to the cast by author order (2026-10-02). They stream
> mostly in Japanese; with the English cast they meet as senpai. Gura (graduated 2025-05-01) and Mumei
> (2025-04-27, 04-28 JST) appear only as memories; Ame is an affiliate. The Japanese-side units (miComet, SorAZ,
> OkaKoro, FAMS and the rest) are on each member's own file.

## One-line Concept
The senpai the English cast looks up to: Suisei, the idol Calli is starstruck by; AZKi, the diva who maps
FUWAMOCO's Japan; Ayame, the oni who once sat on Kiara's talk show; and Okayu, the cat who sings with Ina and
dropped in on FUWAMOCO's 3D debut.

## Type
Relationship web (four Japanese senpai with the cast and with each other).

## Hoshimachi Suisei with the cast
- **Mori Calliope ("Death Star"):** Calli is openly starstruck by Suisei. Calli's original "CapSule" with Suisei
  (2022-04-04) and Suisei's "Wicked feat. Mori Calliope" (single "TEMPLATE / Wicked," 2022); Suisei sang
  "Wicked" with Calli at Calli's first solo concert "New Underworld Order" (2022-07-21). Calli drew Suisei on
  stream (2021), watched Suisei's 2nd concert with Ina (2023-02-20), held a "Talkin' Live Shows" collab with
  her (2023-04-12) and watched the "Spectra of Nova" tour opener with FUWAMOCO and Elizabeth (2024-11-14). In a
  June 2026 chat Suisei mentioned having already talked about "the one with Calliope" among her recent stage
  appearances. [S1] [S2 Suisei §Relationships, secondary] [Suisei file SU20]
- **Takanashi Kiara ("cometori"):** Suisei was the eighth guest of Kiara's HOLOTALK (2021-04-17); a sponsored
  Tales of Arise talk with "fangirling" (2021-11-20); a #tastychallenge dance together (2025-08-25). [S1]
- **IRyS:** with Moona Hoshinova and AZKi they are **Star Flower**, the unit of "story time" (2022-12-31, the
  theme of the second hololive Alternative teaser); IRyS covered Suisei's "GHOST" (2021); "High Tide" with IRyS,
  Moona and Hakos Baelz at -Breaking Dimensions- (2024); the PlateUp! squad of Okayu's team at the 2025 New
  Year Game Festival (with Pavolia Reine). [Official S3, S6] [S1]
- **Gawr Gura (graduated):** Suisei, Gura and Usada Pekora were the three faces of "hololive night" at Dodger
  Stadium (2024-07-05), on the big screen at the first pitch and in the drone show. [Official S4]
- **Others:** Hakos Baelz ("High Tide," 2024; a 2025 dance short to Suisei's "Moonlight"); Nanashi Mumei (a
  #bibbidibachallenge short together, 2024-06-18); FUWAMOCO (a 2026 dance short to Suisei and Houshou Marine's
  "Chatter Chatter"); Nerissa Ravencroft (a "BIBIDEBA" dance short, 2024); Koseki Bijou (a Fortnite stream
  titled "THE SUISEI CONCERT IN FORTNITE?!", 2026-05-02, after Suisei joined Fortnite as a playable
  character in March 2026). [S1] [Official S6] [S5 Suisei, secondary]

## AZKi with the cast
- **FUWAMOCO ("FWMCAZ"):** a GeoGuessr collab on a map AZKi built of places tied to the twins ("BAU BAU
  Travel FUWAMOCO MAP in Japan," 2024-02-09); a singing collab with Minato Aqua (2024-08-13); guests at AZKi's
  2025 birthday 3D live "Sweet Pop Story," where they sang "Bon appétit♡S" with her. [S1]
- **IRyS:** Star Flower (above); IRyS covered AZKi's "Inochi" (2021); Calli's "HOLO ENGLISH LESSON #03" with
  IRyS and Tsunomaki Watame (2022-03-12); an R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora,
  Ina and Kronii (2025-07-19). [S1] [Official S3]
- **Others:** Takanashi Kiara (HOLOTALK's 13th guest, 2021-07-31); Hakos Baelz (GeoGuessr, "lost simulator,"
  2023-03-09); Ouro Kronii, Elizabeth and FUWAMOCO (Tokoyami Towa's team at the 2025 New Year Game Festival);
  Mori Calliope (AZKi danced to Calli's "Orpheus" in a 2025 short); Shiori Novella, Bae and Raora Panthera
  danced to AZKi's songs in shorts (2025–2026). [S1]

## Nakiri Ayame with the cast
- **Takanashi Kiara:** HOLOTALK's 23rd guest, the season-2 opener (2022-10-09). [S1]
- **Team events:** the 2023 hololive Sports Festival in Minecraft, white team (with Kiara, Mumei, Ame, Nerissa
  and AZKi), which won; Okayu's team at the 2025 New Year Game Festival (with Suisei, Ina, IRyS and Cecilia).
  [S1]
- **Shared days:** 7th fes STAGE 1 with Ina and FUWAMOCO (2026); Anime NYC 2026, where she streamed from the
  hololive booth with Shirakami Fubuki and Ookami Mio on the same day as Kronii and Raora, FUWAMOCO, and the
  karaoke party of Calli, Bijou, Nerissa and Kobo Kanaeru (2026-08-22). [Official S5, S7]
- No closer EN pairing is documented in the sources read.

## Nekomata Okayu with the cast
- **Ninomae Ina'nis ("TakoNeko"):** duets, and the Mythmash single "Kurukuru Cruise," sung by Ina and Okayu
  (2025-08-04); both on Okayu's 2025 New Year Game Festival team and on 7th fes STAGE 1 (2026). [S1] [S2 Okayu
  §Relationships, secondary] [Official S5]
- **FUWAMOCO:** Okayu (a self-declared fan of the twins) and Inugami Korone made cameos at FUWAMOCO's 3D debut
  (2024-08-10 PDT); FUWAMOCO watched Okayu's 2nd solo concert "PERSONYA RESPECT" together ("respect to our
  sultry cat senpai," 2025-05-28); a 2025 short of "3 dogs + 1 cat" with Korone and Okayu. [S1] [S2 Okayu,
  secondary] [FUWAMOCO card]
- **Others:** Takanashi Kiara (HOLOTALK's 18th guest, the show's first-anniversary episode, 2021-11-27); Nanashi
  Mumei (a guest at Mumei's 3D live "Outside the Box," 2024); Mori Calliope (a pop-up Mario Party with Anya
  Melfissa and Hiodoshi Ao, 2024-09-15); Hakos Baelz and FUWAMOCO (team Mario Kart, 2023-12-12); IRyS and
  Cecilia Immergreen (Okayu's 2025 New Year Game Festival team); Gigi Murin ("OkaGigi," a pair name only; no
  shared activity sourced). [S1] [Mumei file] [Gigi file]

## Among the four
- **Suisei and AZKi ("AS_tar," formerly "Ex-INNK"):** the two were together at INoNaKa Music before both moved
  to hololive and its "0th generation"; a 2026-05-18 off-collab horror stream ("Dread Neighbor"). Both are in
  Star Flower. [S2] [S1]
- **Suisei and Okayu:** "MOMAS" with Sakura Miko, Houshou Marine and Hiodoshi Ao. [S2]
- **Ayame and Okayu:** "OKFAMS" with Inugami Korone, Shirakami Fubuki, Ookami Mio and Oozora Subaru. [S2]
- **All four:** on stage at hololive 7th fes. "Ridin' on Dreams" (2026-03-06/08): Ayame and Okayu on STAGE 1,
  AZKi on STAGE 3, Suisei on STAGE 4. Suisei, Ayame and Okayu shared Okayu's 2025 New Year Game Festival team.
  [Official S5] [S1]

## HOLOTALK
Kiara's live-translated interview show for overseas viewers hosted all four: Suisei (8th guest, 2021-04-17),
AZKi (13th, 2021-07-31), Okayu (18th, 2021-11-27) and Ayame (23rd, 2022-10-09). [S1]

## History
| Date | Event | Pair |
|---|---|---|
| 2021-04-17 | HOLOTALK #8 | Kiara–Suisei |
| 2021-07-31 | HOLOTALK #13 | Kiara–AZKi |
| 2021-11-27 | HOLOTALK #18 (first anniversary) | Kiara–Okayu |
| 2022-03-12 | HOLO ENGLISH LESSON #03 | Calli with IRyS, Watame, AZKi |
| 2022-04 | "CapSule"; "TEMPLATE / Wicked feat. Mori Calliope" | Death Star |
| 2022-07-21 | "Wicked" at New Underworld Order | Death Star |
| 2022-10-09 | HOLOTALK #23 | Kiara–Ayame |
| 2022-12-31 | "story time" | Star Flower (Suisei, AZKi, Moona, IRyS) |
| 2023-11 | Sports Festival, white team wins | Ayame and AZKi with Kiara, Mumei, Ame, Nerissa |
| 2024-02-09 | GeoGuessr FUWAMOCO map | FWMCAZ |
| 2024-07-05 | hololive night at Dodger Stadium | Suisei, Gura, Pekora |
| 2024-08-10 PDT | FUWAMOCO's 3D debut, Okayu and Korone cameos | FUWAMOCO–Okayu |
| 2024-08-24/25 | "High Tide" at -Breaking Dimensions- | Suisei with IRyS, Moona, Bae |
| 2024-11-14 | "Spectra of Nova" watch party | Calli, FUWAMOCO, Elizabeth for Suisei |
| 2025-01-13 | New Year Game Festival, Okayu's team | Okayu, Suisei, Ayame with Ina, IRyS, Cecilia |
| 2025-05-28 | "PERSONYA RESPECT" watch-along | FUWAMOCO for Okayu |
| 2025-07 | "Sweet Pop Story" | AZKi with FUWAMOCO |
| 2025-08-04 | "Kurukuru Cruise" | TakoNeko |
| 2026-03-06/08 | hololive 7th fes. "Ridin' on Dreams" | all four on stage |
| 2026-08-22 | Anime NYC booth stream | Ayame (with Fubuki, Mio) |

## Sensory Palette
- See: a pale-blue side ponytail and a crown cap; AZKi's pink-streaked black hair and pickaxe mark; Ayame's red
  oni mask, horns and two swords; Okayu's purple cat ears and dark hoodie.
- Hear: a bilingual stream title; Calli's starstruck "Senpai!"; Ayame's table-slapping laughter; Okayu's low,
  lazy voice; a GeoGuessr guess called out in Japanese.

## Glossary
| Term | Meaning | Who uses it |
|---|---|---|
| Death Star | Calli and Suisei | fans, titles |
| cometori | Suisei and Kiara (HOLOTALK hashtag) | Kiara |
| Star Flower | Suisei, AZKi, Moona, IRyS ("story time") | official |
| AS_tar | Suisei and AZKi (formerly Ex-INNK) | the pair, fans |
| FWMCAZ | FUWAMOCO and AZKi | AZKi's title hashtag |
| TakoNeko | Ina and Okayu | fans |
| OkaGigi | Okayu and Gigi (pair name only) | fans |
| HOLOTALK | Kiara's translated interview show | Kiara |

## Conflicts and Story Hooks
1. Calli rehearses a duet with Suisei and cannot stop calling her "senpai" mid-verse.
2. AZKi builds a GeoGuessr map of the EN members' favorite spots in Japan and dares them to guess.
3. Ayame guests on a new HOLOTALK; Kiara translates, Ayame laughs at her own pun and cannot finish the answer.
4. Okayu, the "all-affirming cat," judges an Ina–FUWAMOCO argument and agrees with everyone.

## Links to Characters
Hoshimachi Suisei; AZKi; Nakiri Ayame; Nekomata Okayu; Mori Calliope; Takanashi Kiara; Ninomae Ina'nis; IRyS;
Hakos Baelz; Ouro Kronii; FUWAMOCO; Koseki Bijou; Nerissa Ravencroft; Shiori Novella; Elizabeth Rose Bloodflame;
Gigi Murin; Cecilia Immergreen; Raora Panthera; Gawr Gura; Nanashi Mumei; Watson Amelia.

## Secrets
None assigned.

## Hard Facts (continuity)
- Official units: Star Flower (Suisei, AZKi, Moona Hoshinova, IRyS; "story time," 2022-12-31).
- Concert pairings: "Wicked" (Suisei with Calli, 2022-07-21); "High Tide" (IRyS, Bae, Moona, Suisei; 2024).
- Kiara's HOLOTALK guests: Suisei #8, AZKi #13, Okayu #18, Ayame #23.
- 7th fes (2026-03-06/08): STAGE 1 Ayame, Okayu (with Ina, FUWAMOCO); STAGE 3 AZKi (with IRyS, Bae, Shiori);
  STAGE 4 Suisei (with Calli, Kronii, Bijou, Nerissa).

## Sources (checked 2026-10-02)
- S1 Stream archive metadata (archive.ragtag.moe): EN channels: M85xU-tbQ6c (CapSule, 2022-04-04), w-3kPLHNn5I
  (Wicked at NUO), LeBdrt4HLAs (drawing Suisei, 2021-07-24), UFej2ETuLO0 and 2BKNJUd8B7A (Suisei's 2nd concert
  with Ina, 2023-02-20), vAlW2hDpQmE (2023-04-12), YtVleZxIiNc (Spectra of Nova watch party, 2024-11-14),
  32NVpmKdAOs (HOLO ENGLISH LESSON #03), a6DjP7NYwUE, CohBCNY9Pm4, FjsTGuBQlO0, h1EaCnoKhwk (HOLOTALK #8, #13,
  #18, #23), 71oDdO_19MM (Tales of Arise), 3PZedEMs_VM (Kiara's #tastychallenge), uzEEffCJOjs (IRyS, GHOST),
  fCf4mFiR--w (IRyS, Inochi), T594r3CnuW8 (Bae, GeoGuessr), jszRzFEkeOE (Bae, Moonlight), JZ1Sfotw7tE (Nerissa,
  BIBIDEBA), AhGrt2gr5pc (Bijou, Fortnite), PtaFGDOaj0k (FUWAMOCO, Chatter Chatter), gzPgXfYAbGg (FUWAMOCO,
  PERSONYA RESPECT watch-along), Axbt9GS91k4 (FUWAMOCO with Korone and Okayu), Janl2FCKmsg (team kart),
  t7lNu-p_ANs (Kurukuru Cruise), 7dcUT_Aq2QQ (Shiori), nd47c1W-i8A (Bae), 4E7VBrjAKqU (Raora); JP channels:
  zSB9yejsmGQ (Suisei and Mumei), lXLBb9IVraI (AZKi, Orpheus), Lk7Rlt-MVB4 (FWMCAZ GeoGuessr), _VnNO5TMkBM
  (AZKi, Aqua, FUWAMOCO), Dzw7zsjUoOI (Sweet Pop Story with FUWAMOCO), _gZdFTluxtc (R.E.P.O. JP & EN),
  9sOBwx7uC0o (Towa's team), THMIBrxnp-E and eAMpppCtNpk (Okayu's team, 2025), tHP7bd8Jtm0 (Sports Festival
  2023), WnKCmQ2iXww (Mario Party with Calli), v60QmEvEQqw (AS_tar off-collab, 2026-05-18)
- S2 Wiki pages (secondary), §Relationships: https://virtualyoutuber.fandom.com/wiki/Hoshimachi_Suisei,
  https://virtualyoutuber.fandom.com/wiki/AZKi, https://virtualyoutuber.fandom.com/wiki/Nakiri_Ayame,
  https://virtualyoutuber.fandom.com/wiki/Nekomata_Okayu
- S3 Official song page, "story time" (Star Flower): https://hololive.hololivepro.com/en/music/249/
- S4 Official post-event report, hololive night (2024): https://hololive.hololivepro.com/en/news/20240731-01-92/
- S5 hololive 7th fes. cast lineup: https://hololivesuperexpo.hololivepro.com/2026/en/fes/cast/ (stages by
  day; dates from the Concerts card); Japanese Wikipedia (secondary) for Ayame's and Okayu's STAGE 1 on 2026-03-06
  and Suisei's Fortnite appearance (2026-03-13 to 03-24)
- S6 Official -Breaking Dimensions- report: https://hololive.hololivepro.com/en/events/breaking-dimensions/
- S7 Official news, hololive at Anime NYC 2026: https://hololive.hololivepro.com/en/news/20260624-01-216/
- Character files in this project: Suisei (SU20 audio check), AZKi, Ayame, Okayu; Mumei, Gigi; FUWAMOCO card.

---

## [SW] Name
JP Senpai Pairs

## [SW] Role
Relationship

## [SW] Other Names
Death Star, Star Flower, AS_tar, FWMCAZ, TakoNeko, OkaGigi, cometori, HOLOTALK, Suisei and Calli, Okayu and Ina, AZKi and FUWAMOCO

## [SW] Description
The ties of four hololive senpai from Japan, Hoshimachi Suisei, AZKi, Nakiri Ayame and Nekomata Okayu, with the English cast and with each other. Calli is openly starstruck by Suisei ("Death Star"): they made "CapSule" and "Wicked" together (2022), Suisei sang "Wicked" with Calli at Calli's first solo concert, and Calli hosts watch parties of Suisei's concerts. Suisei, AZKi, IRyS and Moona Hoshinova are the official unit Star Flower ("story time," 2022); Suisei sang "High Tide" with IRyS, Moona and Bae at the 2024 English concert, and was a face of hololive night at Dodger Stadium with Gura and Pekora (2024). AZKi and FUWAMOCO are "FWMCAZ": a GeoGuessr map of the twins' Japan, a singing collab, and the twins as guests at her 2025 birthday live. Okayu and Ina are "TakoNeko," who sang "Kurukuru Cruise" (2025); Okayu, a fan of the twins, made a cameo at FUWAMOCO's 3D debut, and they watched her solo concert together. Kiara's translated talk show HOLOTALK hosted all four (2021–2022). Ayame's ties with the English cast are team events and shared stages. Among themselves: Suisei and AZKi came up together at INoNaKa Music ("AS_tar"); Suisei and Okayu are in MOMAS; Ayame and Okayu in OKFAMS. All four performed at hololive 7th fes. (2026).

## [SW] Rules
These are friendships and senpai–kouhai ties performed in public. The four stream mostly in Japanese; the English cast addresses them as "senpai," and conversations mix Japanese and English. Gura and Mumei appear only as memories; Ame is an affiliate. A collab title shows that a collab happened, not how close two members are; Ayame has no closer English pairing on record.

## [SW] Sensory Details
A pale-blue side ponytail under a crown cap; pink-streaked black hair and a pickaxe mark; a red oni mask, horns and two swords; purple cat ears over a dark hoodie. A bilingual stream title, Calli's starstruck "Senpai!", table-slapping laughter, a low lazy "mogu mogu," a GeoGuessr guess called out in Japanese.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hoshimachi Suisei, AZKi, Nakiri
  Ayame and Nekomata Okayu): archive metadata (EN and JP channels), official song, event and news pages, the
  wiki (secondary), Japanese Wikipedia (secondary) and the four new character files.

## Open Questions
1. Ayame has no direct EN collab beyond HOLOTALK and team events in the sources read; keep her section short?
2. "OkaGigi" has no sourced shared activity; keep it as a pair name only?


## Lines about the four added to the English cast's cards (2026-10-02; not yet promoted)

### Mori-Calliope (Relationships)
Hoshimachi Suisei ("Death Star"): a senpai who leaves her starstruck; "CapSule" and "Wicked" (2022); a guest at her 2026 birthday live.

### Takanashi-Kiara (Relationships)
Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left. HOLOTALK guests also included Hoshimachi Suisei ("cometori"), AZKi, Nekomata Okayu and Nakiri Ayame.


### Ninomae-Inanis (Relationships)
Nekomata Okayu: "TakoNeko"; duets and the Mythmash single "Kurukuru Cruise" (2025).


### IRyS (Relationships)
Hoshimachi Suisei and AZKi: with Moona Hoshinova, the unit Star Flower ("story time," 2022); Suisei also sang "High Tide" with IRyS and Bae (2024).


### Fuwawa-Abyssgard (Relationships)
AZKi ("FWMCAZ"): GeoGuessr on a map of the twins' Japan, a singing collab, and the twins as guests at her 2025 birthday live. Nekomata Okayu: a fan who made a cameo at their 3D debut; they watched her 2025 solo concert together.


### Mococo-Abyssgard (Relationships)
AZKi ("FWMCAZ"): GeoGuessr on a map of the twins' Japan, a singing collab, and the twins as guests at her 2025 birthday live. Nekomata Okayu: a fan who made a cameo at their 3D debut; they watched her 2025 solo concert together.


### Gawr-Gura (Relationships)
Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Hoshimachi Suisei and Usada Pekora: the faces of hololive night at Dodger Stadium with Gura (2024).


### Gigi-Murin (Relationships)
Nekomata Okayu: "OkaGigi," a pair name.


### Nanashi-Mumei (Relationships)
Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Mumei was Kiara's HOLOTALK guest in her last week. JP: Takane Lui ("Q&A With Bird Sisters"), Tokoyami Towa (calls her "Mumi-chan"), Akai Haato (Minecraft); Inugami Korone (a duet cover in her last week) and Okayu, Nene and Koyori, guests at "Outside the Box."


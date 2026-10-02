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
- The author ordered these hololive members from Japan added as full cards (2026-10-02): Houshou Marine,
  Shirogane Noel, Yukihana Lamy, Shishiro Botan, Kikirara Vivi and all of Secret Society holoX (La+ Darknesss,
  Takane Lui, Hakui Koyori, Sakamata Chloe, Kazama Iroha), with their ties to the rest of the cast. This is run E of four: La+, Lui and Koyori. Run F covers Chloe, Iroha, the world card "holoX" and the cross-card lines about holoX.
- They stream in Japanese. Quotes on the cards are Japanese (with romanization and an English gloss); the audio
  reports list both models' renderings. A Japanese quote passes the gate only if the report marks it shared
  (the same kana reading in both models counts as shared). Never stitch separately timed spans.
- Public persona only. Do not propose adding body measurements, drinking amounts, family, home region, pets,
  health, sleep or daily routine, trips, romance, auditions, breaks or their reasons, or pre-debut history, even
  when an official profile or wiki lists them; the cards leave these out on purpose. Accents are voice features
  only; do not assign a regional accent without an in-scope listening check.
- Sakamata Chloe concluded her regular activities on 2025-01-26 and is a hololive affiliate; her card covers
  2021-11 to 2025 plus affiliate appearances. Everyone else is active at the 2026-09-30 baseline.
- Performance sheets: original designed voices only (never imitate a member); pitch and pace measurements are
  research data, not synthesis targets; partner tags are proposed scene directions; laughs and timbre are
  provisional choices unless a source is named.
- This run must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation,
  so keep to about 15 tool calls in total, including web searches; batch local lookups. Prioritize the exported
  [SW] fields, then the dossier facts dated 2025–2026, then the sheets.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git). The new
  cards are not in `bible/`; their full text is inline below. Do not re-open the inline files.
- If the budget runs short, stop and report what you could not check in the Verification note.

## Card 1: Laplus Darknesss (draft, full file)

---
kind: character
name: "La+ Darknesss"
sw_section: Characters
---

# Character File: La+ Darknesss

> Scope: official lore and publicly shown persona only, checked 2026-10-02. La+ is an active hololive member
> (Japan, Secret Society holoX) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02, holoX
> in full). Her recent streams (2026) set her default manner, per the project's recency rule. Nothing about the
> performer behind the avatar: private-life information (family, home, health, daily routine, sleep, outings and
> the like) is outside scope and is not recorded here, including what she mentions in chats. She streams in
> Japanese; that is recorded as the language of her performance only. In stories she knows she is a streamer
> with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; LA20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (LA#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (LA20: a May 2026 chat and her January
> 2026 New Year fan-greeting stream; see research/audio-check/laplus.md). Personal remarks are not quoted or
> summarized here. The audio was machine-transcribed and acoustically measured; transcripts were reviewed in
> context, without independent listening verification.

## One-line Concept
"See me, hear me, all of you!": the tiny, horned founder of Secret Society holoX, a demon of once-vast power now
sealed in shackles she cannot remember receiving, who calls herself "wagahai," plots world domination, salutes
with "Yes My Dark!" and loses her temper loudly whenever her seniors treat her like a child, which is always.
[Official LA1] [Observed LA2 §Personality, secondary]

## Core Drive
- **Want:** domination, in the lore; on stream, to win, to be taken seriously and to grow as an artist (her first
  album "Project Y.M.A. (Yes My Artist)" was announced in 2026). [Official LA1] [Observed LA2 §2026]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** being treated as a child; losing a game; both set off loud protests.
  [Observed LA2 §Personality, secondary]
- **Values shown in public:** loyalty to holoX; making her own highlight clips; turning her losses into content.
  [Observed LA2 §Miscellaneous, secondary]

## Core Contradiction
A self-declared demon overlord who stands 139 cm, wears shackles and is treated as one of hololive's "babies" by
seniors like Sakura Miko, a label she loudly refuses. [Official LA1] [Observed LA2 §Personality, secondary]

## Behavioral Traits
1. Speaks like a villain in persona moments: "wagahai" for "I" (an archaic, arrogant pronoun) and "kisama" for
   "you" (wiki). In two 2026 windows (a chat and a fan-greeting stream) she said plain "watashi" in casual talk and
   "wagahai" was not heard, so the villain register reads as a set piece. [Observed LA2 §Personality,
   §Miscellaneous, secondary] [ASR LA20]
2. Smug and bratty, and loud when she loses or feels mistreated; seniors tease her as a child. [Observed LA2
   §Personality, secondary]
3. Turns fan votes into bits: when fans chose her fan name, she split "Yamada" into two options so it would win
   (the official name is Plusmate). [Observed LA2 §Mascot and fans, secondary]
4. Edits her own highlight clips, unusual for a hololive member. [Observed LA2 §Miscellaneous, secondary]
5. Has a full title she will recite: "Laplus Dia Highest Death Thirteen Daina Art of Impact Sign Emperor Road of
   the Darknesss." [Observed LA2 §Name, secondary]
6. A public face for Tochigi Prefecture as a "Tochigi Future Ambassador" from 2026-05-03. [Observed LA2 §2026;
   LA3 prefectural page]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "See me, hear me, all of you!" (Japanese: "Kakumoku seyo!"); fans answer "Yes My Dark!" [Official
    LA1] [Observed LA2 caption, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Yes My Dark!" (YMD) → the salute of her followers. [Observed LA2]
  - "Wagahai" / "kisama" → always. [Observed LA2]
  - "I'm not a suspicious person!" ("Wagahai ayashii mono de nai zo," her first post). [Observed LA2 §Background,
    secondary]
- **Vocabulary / fillers:** casual and slangy in 2026 chats: "maji de," "yabai," "~ssho" (「聞こえたっしょ?」,
  "you heard it, right?"); see research/audio-check/laplus.md. [ASR LA20]
- **Profanity:** playful, bratty insults ("kisama"). [Observed LA2]
- **Language:** streams in Japanese; with the English cast she sang with Kiara ("Glow in the Dark," "FAKE HEART")
  and joined Calli's English lesson (2022). [LA5]
- **Laughs, noises:** a smug cackle; loud protests. [Observed LA2]
- **Rhythm & rhetoric:** grand villain declarations collapsing into childish complaints. [Observed LA2]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (LA20): median about 276 Hz in a May 2026 chat window (p10–p90 about 196–543 Hz) and about 287 Hz
    in a January 2026 fan-greeting stream; about 235–247 characters a minute of speech; see
    research/audio-check/laplus.md. Measurements describe the archived audio, not a target to clone.
  - Provisional (interpretation): a small, bright, bratty voice that puffs itself up into a grand villain register
    and cracks into a whine when teased.
- **Sounds off:** a truly menacing demon; a soft, sleepy default; a mature, cool voice.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Grand, commanding | "See me, hear me, all of you!" (LA1) |
| Rallying followers | Triumphant | "Yes My Dark!" (LA2) |
| Treated like a child | Indignant, loud | **Style demo:** "Wagahai wa kodomo ja nai!" ("I am not a child!") |
| Losing a game | Whining, furious | **Style demo:** "Kisama~!" ("You~!") |
| Smug victory | Cackling | [laughs] |

### Sample Lines
1. "See me, hear me, all of you!" (Official LA1)
2. "I'm not a suspicious person!" (LA2, her first post, secondary)
3. 「これが配信者よ」 (kore ga haishinsha yo, "this is what a streamer is!") (ASR LA20, May 2026, showing off her
   new setup)

## Appearance Anchors (avatar)
- 139 cm; illustrator Mishima Kurone. Long silvery hair with a purple lock and a braided bang, large black horns
  with purple stripes above pointed ears, yellow eyes; a dark purple dress with a purple collar and yellow tie,
  oversized sleeves that cover her hands, an unbuckled belt, one purple legging, dark purple boots, a purple tail
  with four-pointed stars, and shackles at her ankles, neck and sleeves. A crow is her long-time companion. Emoji
  🛸💜. [Official LA1] [Observed LA2 §Appearance, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Founder of Secret Society holoX; vast power, now sealed | [Official LA1] |
| 2021-11-26 | Debut, first of holoX | [Observed LA2] |
| 2022-03-04 | Calli's "HOLO ENGLISH LESSON #02" with Gura and Iroha | [LA5 X492n37brRU] |
| 2023-06-30 | Nostalgic games with a handcam, an off-collab with Kiara | [LA5 XWf2PqD_8zQ] |
| 2024 | "drop candy" (05-25); holoGTA (with Nerissa, Ayame, Suisei and others) | [Observed LA2] [LA4] |
| 2025-04-08 | "FAKE HEART," a cover with Kiara | [LA5 yspJ9xmGRfw] |
| 2025-07-27 | "Glow in the Dark," a Mythmash single with Kiara; a joint stream | [LA5 v5RKZXNuVyw] [LA4] |
| 2025-12 | holoX's 4th anniversary ("Gyouan Xdeath," "Secret ORDER"); 1.5 million subscribers (12-30) | [Observed LA2] |
| 2026-04-29 | holoX's first concert, "First MISSION" | [Official LA6] |
| 2026-05-03 | Tochigi Future Ambassador | [Observed LA2] [LA3] |
| 2026-05-19 | A 3D lie-detector "challenge" to Nekomata Okayu | [LA4 F3i30BIJmtY] |
| 2026-05-25 | "Onee-sama♡Love Call"; album "Project Y.M.A." announced | [Observed LA2] |

## Relationship Map
Public exchanges only. Group ties are on the world card "holoX."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Takane Lui | holoX executive officer | Reins her in; a 2026 two-person talk; poker (2025) | [LA2] [LA4] |
| Hakui Koyori, Kazama Iroha | holoX | "Irohasu" with Iroha | [LA2] |
| Sakamata Chloe (affiliate) | holoX intern | A cover together (2025) | [LA4] |
| Takanashi Kiara | — | "Glow in the Dark" and "FAKE HEART" (2025); an off-collab (2023) | [LA5] |
| Mori Calliope | — | HOLO ENGLISH LESSON #02 (2022) | [LA5] |
| Gawr Gura (graduated) | — | The same English lesson (2022) | [LA5] |
| FUWAMOCO, Cecilia Immergreen | kouhai | FUWAMOCO danced to "Onee-sama♡Love Call" (2026); Cecilia's short calls her "onee-sama" (2026) | [LA5] |
| Nerissa Ravencroft | — | holoGTA (2024) | [LA4] |
| Nekomata Okayu | "Dorobo Kensetsu" | A 3D lie-detector challenge (2026) | [LA2] [LA4] |
| Nakiri Ayame, Hoshimachi Suisei, Shishiro Botan | — | All four streamed holoGTA (2024-09); the m HOLD'EM poker collab (2024-12) was La+, Suisei, Botan and Shirakami Fubuki (publisher roster), not Ayame | [LA4 swqXHi1Z4ew, QLHSm3rpG8k] [Sammy roster] |
| AZKi | — | Games and an ASMR "evaluation" (2025); AZKi danced to her songs | [LA4] |
| Houshou Marine | "#マリラプ" (archived title) | A sponsored collab (2025); a cover with Marine and Koyori (2025) | [Marine file] [KO4] |
| Yukihana Lamy, Shishiro Botan | NePoX | NePoLaBo × holoX events (2026) | [Lamy file] [Botan file] |

## Arc
- **Starting point:** active at the 2026 baseline: holoX's first concert, a Tochigi ambassadorship, her first
  album announced.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a world-domination scheme with no budget; a sore loss; a senior who pats her head.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. La+ demands that Kiara address her as "Your Darknesss" for a whole duet rehearsal.
  2. A holoX meeting where La+ announces a conquest plan and Lui schedules it for "after lunch."

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-11-26; Secret Society holoX (founder); birthday 25 May; 139 cm; illustrator Mishima Kurone; fans
  Plusmate; stream tag #laplus_great.

## Sources (checked 2026-10-02)
- LA1 Official profile: https://hololive.hololivepro.com/en/talents/la-darknesss/
- LA2 La+ Darknesss wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/La%2B_Darknesss
- LA3 Tochigi Prefecture, Tochigi Future Ambassador page (via LA2): https://www.pref.tochigi.lg.jp/c05/pref/kihon/sonota/1285545941380.html
- LA4 Stream archive metadata, her channel (archive.ragtag.moe): dBzPcy1DqzU (chat, 2026-05-11), ebnfDlxLZug
  (2026-01-02), F3i30BIJmtY (with Okayu, 2026-05-19), 3c4jvhUn3js (with Kiara, 2025-07-27), wFLqcyiBWq8 (poker),
  holoGTA shorts (2024)
- LA5 Other members' archive metadata: X492n37brRU (Calli), XWf2PqD_8zQ, yspJ9xmGRfw, v5RKZXNuVyw (Kiara),
  TlzLo7Fw2pw (FUWAMOCO), tqF0_rYGW20 (Cecilia)
- LA6 COVER EDGE interview after "First MISSION" (2026-05-23): https://coveredge.cover-corp.com/en/list/5238
- LA20 Claude's audio check (two-model ASR, Japanese): research/audio-check/laplus.md

---

## [SW] Name
La+ Darknesss

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, Secret Society holoX, holoX, Dorobo Kensetsu, NePoX

## [SW] Other Names
La+, Laplus, Laplace, YMD, Yamada

## [SW] Personality
La+ is the founder of Secret Society holoX, a demon whose once-vast power and intelligence are sealed by shackles she cannot remember receiving, with a crow as her long-time companion. She plays the overlord: she calls herself "wagahai" (an arrogant, archaic "I"), calls others "kisama," plots world domination and has her followers answer "Yes My Dark!" In practice she is a smug, bratty, loud little boss who loses her temper when she loses a game or gets treated like a child, which her seniors do constantly; she refuses to be counted among hololive's "babies." She is quick and funny, turns fan votes into bits (she split "Yamada" into two options so her fans' joke name would win), edits her own highlight clips, and takes her music seriously: her first album, "Project Y.M.A. (Yes My Artist)," was announced in 2026. In 2026 she also became a Tochigi Future Ambassador.

## [SW] Background
La+ is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-26 as the first member of Secret Society holoX, hololive's sixth Japanese generation, whose executive officer Takane Lui does the actual running. She has original songs such as "drop candy" and "Onee-sama♡Love Call" (2026), sang with holoX at their first concert, "First MISSION" (2026-04-29), reached 1.5 million subscribers first in holoX (2025), and was appointed a Tochigi Future Ambassador (2026). With the English cast she made the Mythmash single "Glow in the Dark" and the cover "FAKE HEART" with Takanashi Kiara (2025), played nostalgic games with Kiara off-collab (2023), and took Mori Calliope's English lesson with Gawr Gura and Kazama Iroha (2022).

## [SW] Physical Description
La+'s avatar is 139 cm tall, with long silvery hair, a purple lock and a braided bang, large black horns striped in purple above pointed ears, and yellow eyes. She wears a dark purple dress with a yellow tie and oversized sleeves that swallow her hands, one purple legging and short boots, with a star-tipped purple tail and shackles at her neck, sleeves and ankles. A crow keeps her company.

## [SW] Dialogue Style
Streams in Japanese. Her persona voice is a pint-sized villain: "wagahai" for "I," "kisama" for "you," grand declarations ("See me, hear me, all of you!") and "Yes My Dark!" from her followers. In everyday 2026 chats she talks casually, with plain "watashi," "maji de," "yabai" and "~ssho" ("you heard it, right?"), and turns fast, loud and bratty the moment someone teases her or she loses. She protests, sulks, cackles when she wins and narrates her own schemes. When a story renders her speech in English or Chinese, keep the archaic villain "I" (in Chinese, 吾輩) for persona moments against a small, indignant voice.
## [SW] Catchphrases
"See me, hear me, all of you!" (official, "Kakumoku seyo!"); "Yes My Dark!" (her followers' salute); "wagahai" (her "I"); "kisama" ("you"); "I'm not a suspicious person!" (her first post); her full title, "Laplus Dia Highest Death Thirteen Daina Art of Impact Sign Emperor Road of the Darknesss." Her fans are the Plusmate (and, by her own vote-splitting, "Yamada").

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a small, bright, bratty voice that puffs itself up into a grand villain register and cracks into a loud whine when teased or beaten; quick and cocky when she wins, with a smug cackle. Never truly menacing, sleepy or mature-cool.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): small, bright voice; cocky by default. Default tags: [smug, bright]. By situation: grand declaration [commanding, theatrical]; rallying followers [triumphant]; treated like a child [indignant, loud]; losing [whining, furious]; scheming [conspiratorial]; winning [cackles]. With people (proposed scene directions, not observed conversational defaults): Lui [whiny, dependent]; Kiara [competitive, friendly]; seniors [indignant]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Yes My Dark!" (spoken); [cackles] (tag only). Keep in the words: "wagahai," "kisama," "Yes My Dark." Reading guide (untested): らぷらす だーくねす; わがはい. Not as default: a truly menacing demon; a sleepy or mature-cool voice.

## [SW] Motivation
In her lore, La+ wants to conquer the world with her secret society. As a streamer and artist she wants to win, to be taken seriously (not as a child) and to be recognized as an artist in her own right.

## [SW] Relationships
Takane Lui: holoX's executive officer, who actually runs things and reins her in. Hakui Koyori and Kazama Iroha: holoX ("Irohasu" with Iroha). Sakamata Chloe (affiliate since 2025): the former intern. Takanashi Kiara: "Glow in the Dark" (Mythmash) and "FAKE HEART" (2025), and an off-collab (2023). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: danced to "Onee-sama♡Love Call" (2026). Cecilia Immergreen: teases her as "onee-sama" in a short (2026). Nerissa Ravencroft: holoGTA (2024). Nekomata Okayu: "Dorobo Kensetsu" and a 3D lie-detector challenge (2026). Nakiri Ayame, Hoshimachi Suisei and Shishiro Botan: holoGTA (2024); Suisei, Botan and Shirakami Fubuki: the m HOLD'EM poker collab (2024). AZKi: games (2025). Houshou Marine: a sponsored collab billed #マリラプ and a cover with Koyori (2025). Yukihana Lamy and Shishiro Botan: NePoX (2026).

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add holoX in full): official profile
  (LA1), wiki (LA2, by section), archive metadata (LA4, LA5), COVER's interview (LA6) and Claude's two-model
  Japanese audio check (LA20, research/audio-check/laplus.md).

## Open Questions
1. The crow companion's name is not given in the sources read; leave it unnamed?


## Audio report: research/audio-check/laplus.md

# Audio check — La+ Darknesss (2026-10-02)

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
| chat25_2026 | [【雑談】本当にいろいろあったから話そうぜ～～～～～＾＾【ラプラス・ダークネス/ホロライブ】](https://youtu.be/dBzPcy1DqzU) | [0:05:00–0:30:00](https://youtu.be/dBzPcy1DqzU?t=300) | 16.8 | 4141 | 246.6 | 276 Hz | 196–543 Hz |
| cheki20_2026 | [【新年】太客贔屓チェキ会配信【ラプラス・ダークネス/ホロライブ】](https://youtu.be/ebnfDlxLZug) | [0:10:00–0:30:00](https://youtu.be/ebnfDlxLZug?t=600) | 11.5 | 2708 | 235.2 | 287 Hz | 207–508 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat25_2026 | cheki20_2026 |
|---|---|---|
| first person 私 | 9 | 1 |
| なんか | 25 | 18 |
| まあ | 6 | 2 |
| ちょっと待って | 4 | 2 |
| やばい | 7 | 4 |
| えっ/え? | 4 | 0 |
| laugh (はは/ふふ/笑) | 2 | 2 |
| swear (くそ/ふざけ/殺) | 2 | 1 |
| ありがとう | 1 | 5 |
| English (Latin letters) | 8 | 4 |
| こんなきり/こんにちは | 1 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Speaks as a villain, "wagahai" for "I" (wiki) | **Not observed in 2026 windows**: in a May 2026 chat and a January 2026 fan-greeting stream she says 「私」 (watashi) in plain talk; "wagahai" is kept as her persona line from the wiki. | [0:06:08](https://youtu.be/dBzPcy1DqzU?t=368) |
| Casual, quick chat with chat | **Observed**: 「聞こえたっしょ?」 ("you heard it, right?") checking her audio; slangy "maji de," "yabai." | [0:06:55](https://youtu.be/dBzPcy1DqzU?t=415) |
| Turns her own setup into a bit | **Observed**: showing off her new streaming setup, 「これが配信者よ」 ("this is what a streamer is!"). | [0:19:15](https://youtu.be/dBzPcy1DqzU?t=1155) |
| Plays up being bad at sums | **Observed** (January 2026): she jokes she "really can't do arithmetic." | [0:12:48](https://youtu.be/ebnfDlxLZug?t=768) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "聞こえたっしょ" | [0:06:55](https://youtu.be/dBzPcy1DqzU?t=415) | "…ん?これか?聞こえたっしょ聞こえたっし…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "これが配信者よ" | [0:19:15](https://youtu.be/dBzPcy1DqzU?t=1155) | "どう?これが配信者よこれが配信者…" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/Laplus-Darknesss.md

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
- "Wagahai" is her persona set piece; in 2026 chats she mostly says "watashi."
- Casual and slangy in chat: "maji de," "yabai," "~ssho" (「聞こえたっしょ?」, "you heard that, right?").
- Rallies her followers with "Yes My Dark!"
- Insists she is not a child; whines and fumes when she loses.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[commanding, theatrical]` | "See me, hear me, all of you!" (official English) |
| Showing off | `[smug, bright]` | 「これが配信者よ」 ("Kore ga haishinsha yo," "this is what a streamer is!") |
| Checking with chat | `[casual]` | 「聞こえたっしょ?」 ("Kikoeta ssho?", "you heard that, right?") |
| Treated like a child | `[indignant, loud]` | **Style demo:** "Wagahai wa kodomo ja nai!" ("I am not a child!") |
| Losing a game | `[whining, furious]` | **Style demo:** "Kisama~!" ("You~!") |
| Rallying followers | `[triumphant]` | "Yes My Dark!" (secondary transcription) |

With people (proposed scene directions, not observed conversational defaults): Lui `[whiny, dependent]`; Kiara `[competitive, friendly]`; seniors `[indignant]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Yes My Dark!" (spoken)
- `[cackles]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): らぷらす だーくねす; わがはい; きさま. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A truly menacing demon; a sleepy or mature-cool voice.

## 8. Example
```
[commanding, theatrical] See me, hear me, all of you!
[smug, bright] Kore ga haishinsha yo!
[indignant, loud] Wagahai wa kodomo ja nai!
[triumphant] Yes My Dark!
```
(Line 1 is her official English introduction; line 2 is her line, quoted only where both transcripts agree;
line 3 is a style demo; line 4 is her followers' call as a secondary transcription.)


## Card 2: Takane Lui (draft, full file)

---
kind: character
name: "Takane Lui"
sw_section: Characters
---

# Character File: Takane Lui

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Lui is an active hololive member
> (Japan, Secret Society holoX) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02, holoX
> in full). Her recent streams (2026) set her default manner, per the project's recency rule. Nothing about the
> performer behind the avatar: private-life information (family, home, health, private history, outings and
> the like) is outside scope and is not recorded here, including what the wiki lists or what she mentions in
> chats. She streams in Japanese; that is recorded as the language of her performance only. In stories she knows
> she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; LU20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (LU#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (LU20: a June 2026 midday chat and a
> June 2026 MOTHER 2 first playthrough; see research/audio-check/lui.md). Personal remarks in the chat are not
> quoted or summarized here. The audio was machine-transcribed and acoustically measured; transcripts were
> reviewed in context, without independent listening verification.

## One-line Concept
"Did I Luive you waiting!?": holoX's executive officer and de facto leader, a hawk with a calm, low, big-sister
voice who handles what the founder cannot, cares for her subordinates, makes dad jokes, screams at horror games,
predicts every G1 horse race, and "pons" (blunders) at the crucial moment. [Official LU1] [Observed LU2
§Personality, secondary] [ASR LU20]

## Core Drive
- **Want:** her official dreams: a concert with a live band playing only her originals, tie-ups with TV, anime
  and ads, concerts and fan meetings overseas, her own show or podcast, and to be "an everyday staple" in her
  fans' lives. [Official LU1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror games ("Not good with horror. Beware of screams," her official profile);
  pointy objects aimed at her. [Official LU1] [Observed LU2 §Likes, secondary]
- **Values shown in public:** looking after the people under her; reaching out to overseas members and fans (she
  is, per the wiki, the holoX member who tries hardest to talk with them); taking mistakes in stride. [Observed
  LU2 §Personality, secondary] [ASR LU20]

## Core Contradiction
The cool, aloof-looking second-in-command of an evil society, who is in fact a warm, motherly big sister and
the group's most famous airhead ("PON"), known for knocking over her water mid-stream. [Official LU1] [Observed
LU2 §Personality, secondary]

## Behavioral Traits
1. Reins in La+ Darknesss and Sakamata Chloe; holoX's point of contact for outside work. [Official LU1] [Observed
   LU2 §Personality, secondary]
2. Dad jokes, like Ina and Kronii. [Observed LU2 §Personality, secondary]
3. Scared of horror: her early no-scream Outlast challenge (2021) ended three times within minutes, the first
   when she knocked over her water before the game started. [Observed LU2 §Likes, secondary]
4. Horse-racing prediction streams for almost every G1 race; Saturday RPG streams (MOTHER, MOTHER 2, SAND LAND,
   Dragon Ball Z: Kakarot in 2026). [Official LU1] [Observed LU4 titles]
5. Calls Nekomata Okayu "Shaccho" ("boss"); they predicted game announcements together before a 2026 Nintendo
   Direct. [ASR LU20] [Observed LU4 titles]
6. Loves twins (her official likes), which made "TWIN DAY WITH LUI" with FUWAMOCO (2023). [Official LU1] [LU5]
7. An ambassador for Code Geass from June 2025, with watch-alongs of "Code Geass: Roze of the Recapture" (2026).
   [Observed LU2 §Likes, secondary; LU4 titles]

## Voice Profile
- **Greetings / sign-offs (official catchphrases):** "Mattakane?" ("Did I Luive you waiting?") to open;
  "Otsuluilui" ("I take your Luive") to close. [Official LU1]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "…shitakane?" ("Did you…, if I'm not mistakane?") → when doubtful. [Official LU1]
  - "Takamattekita!" ("Hype Luivels rising!") → excitement. [Official LU1]
  - "PON" → being an airhead; "Ko!☆" → the sparkle she adds after saying something in a cool voice. [Official LU1]
  - "Don't drop your water." → what fans tell her. [Official LU1]
- **Vocabulary / fillers:** "mā," "ne," "un un," a measured "sō nan de gozaimasu" when she plays formal.
  [ASR LU20]
- **Profanity:** rare. [ASR LU20]
- **Language:** streams in Japanese; reaches out to English-speaking members and fans (English practice with Calli,
  2021–2022). [Observed LU2] [LU5]
- **Laughs, noises:** easy laughter; shrieks in horror. [Observed LU2, secondary]
- **Rhythm & rhetoric:** calm, unhurried and conversational; she reads chat aloud and answers it one by one.
  [ASR LU20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (LU20): in a 2026 chat window, median about 190 Hz (p10–p90 about 137–293 Hz); in a 2026 MOTHER 2
    window about 213 Hz; see research/audio-check/lui.md. Measurements describe the
    sampled recording and ASR segmentation; they are not isolated vocal measurements.
  - Provisional (interpretation): a low, calm, mature voice with a warm big-sister softness, flipping into a cool
    "executive" tone (followed by "Ko!☆") for effect, and up into shrieks in horror.
- **Sounds off:** a high, bubbly default; cold cruelty; nonstop shouting.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Warm, lilting | "Mattakane?" (LU1) |
| Executive mode | Cool, low, then a sparkle | **Style demo:** "Kore wa kanbu no shigoto yo. …Ko!☆" ("This is an executive's job. …Sparkle!") |
| Chatting with chat | Calm, motherly | 「まあ誰にだってトラブルやミスはあるからね」 (mā dare ni datte toraburu ya misu wa aru kara ne, "well, everyone has trouble and mistakes") (ASR LU20) |
| A blunder | Flustered, laughing | "PON" (LU1) |
| Horror game | Shrieking | **Style demo:** "Muri muri muri!" |
| Closing | Gentle | "Otsuluilui." (LU1) |

### Sample Lines
1. "Did I Luive you waiting!?" (Official LU1)
2. "I take your Luive." (Official LU1)
3. "Did you…, if I'm not mistakane?" (Official LU1)
4. 「まあ誰にだってトラブルやミスはあるからね」 (mā dare ni datte toraburu ya misu wa aru kara ne, "well, everyone has
   trouble and mistakes") (ASR LU20, 2026 midday chat)

## Appearance Anchors (avatar)
- 161 cm; illustrator Kakage. A hawk: short dull-pink hair with wing-shaped tufts of the same color at the sides of
  her head, blue eyes; a white long-sleeved top with a white-and-red tie, a dark magenta cape with black and gold
  trim and feathers, black gloves, black shorts with tights and heels, a thigh garter. Her partner is Ganmo, a plump frogmouth who is her secretary, with two
  white chicks (Tsumire and Tsukune) on his head. Fan mark 🥀. [Official LU1] [Observed LU2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | holoX's executive officer and point of contact | [Official LU1] |
| 2021-11-27 | Debut, second of holoX; Kiara welcomed her into the bird unit HOLOTORI | [Observed LU2] |
| 2021-12-27 | English practice with Mori Calliope | [LU5 i2wLH4O92-0] |
| 2022 | Calli's English lesson #04 with Chloe; an EN-server Minecraft tour with Mumei, Bae and Chloe; Minecraft with IRyS, Kronii and Kaela | [LU5] |
| 2023 | HOLOYOI ep. 1 with Chloe (Calli's show); a Wario off-collab with Kiara; BAE-GEMITE with Bae and Chloe; "TWIN DAY WITH LUI" with FUWAMOCO | [LU5] |
| 2024 | First album "Liberty" (06-11); 1 million subscribers (11-16) | [Observed LU2] |
| 2025 | EP "Lieblings"; Code Geass ambassador (June); "Q&A With Bird Sisters" with Mumei (04-19); a Harry Potter watch-along club for Okayu | [Observed LU2] [LU5] [LU4] |
| 2025-12-01 | holoX's 4th anniversary: "Gyouan Xdeath," album "Secret ORDER" | [Observed LU2] |
| 2026-04-29 | holoX's first concert "First MISSION" ("I feel like we gave it everything I got!") | [Official LU6] |
| 2026-06-11 | Birthday: "Soar," danced in shorts by many EN members | [LU4] [LU5] |
| 2026-08-01 | A "rare" La+ and Lui talk with new outfits | [LU4] |

## Relationship Map
Public exchanges only. Group ties are on the world card "holoX."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| La+ Darknesss | holoX founder | Lui reins her in; a 2026 two-person talk; poker (2025) | [LU2] [LU4] |
| Sakamata Chloe (affiliate) | holoX intern | Lui reined her in; shows with Calli and Bae together (2022–2023) | [LU2] [LU5] |
| Hakui Koyori, Kazama Iroha | holoX | Iroha calls her "Lui-nee" | [LU2] |
| Takanashi Kiara | HOLOTORI | Welcomed Lui into HOLOTORI on her debut day; a Wario off-collab (2023) | [LU2] [LU5] |
| Nanashi Mumei (graduated) | HOLOTORI; "Bird Sisters" | "Q&A With Bird Sisters" (2025); the EN Minecraft tour (2022) | [LU5] |
| Mori Calliope | English teacher | English practice (2021), lesson #04 (2022), HOLOYOI (2023); Calli danced to Lui's songs (2025, 2026) | [LU5] |
| FUWAMOCO | — | "TWIN DAY WITH LUI" (2023); danced to "Soar" (2026) | [LU5] |
| Hakos Baelz | — | BAE-GEMITE (2023); "FEAST" dance together (2025); an MMD "Soar" (2026) | [LU5] [LU4] |
| IRyS, Ouro Kronii | — | Minecraft elytra hunting with Kaela (2022); IRyS danced to "Soar" (2026) | [LU5] |
| Watson Amelia (affiliate) | — | Apex with Airani Iofifteen (2022) | [LU5] |
| Nerissa, Bijou, Gigi, Raora | kouhai | Danced to "Soar" (2026 shorts) | [LU5] |
| Nekomata Okayu | "Shaccho" | Harry Potter watch-alongs for Okayu (2025); predictions before a 2026 Nintendo Direct; Dorobo Kensetsu | [LU4] [ASR LU20] [LU2] |
| Nakiri Ayame | "Onikan" | Games together (2025) | [LU4] |
| Shishiro Botan | "BLT," "InuTakaShishiRam" | Units with Towa; with Korone and Watame | [LU2] |
| Houshou Marine | "SSS" | With Yuzuki Choco | [LU2] |
| Yukihana Lamy | NePoX | NePoLaBo × holoX events (2026) | [Lamy file] |

## Arc
- **Starting point:** active at the 2026 baseline: holoX's first concert behind her, "Soar" danced across the
  branches, RPG and horse-racing streams.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a calm plan derailed by her own "PON"; a horror game she agreed to; a G1 prediction she is
  sure of; La+'s latest scheme, which she has to clean up.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. A HOLOTORI meeting with Kiara and the memory of Mumei; Lui keeps the agenda, then knocks over the water.
  2. Lui hosts FUWAMOCO for "Twin Day" again and can't stop smiling.
  3. Calli's English lesson, round two: Lui answers in perfect textbook English and then says "Ko!☆".

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-11-27; Secret Society holoX (executive officer); birthday 11 June; 161 cm; illustrator Kakage; fans
  "Lui-tomo"; partner Ganmo (frogmouth); fan mark 🥀; stream tag #たかねの見物.
- Greetings: "Mattakane?" / "Otsuluilui."

## Sources (checked 2026-10-02)
- LU1 Official profile (catchphrases, dreams, likes): https://hololive.hololivepro.com/en/talents/takane-lui/
- LU2 Takane Lui wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Takane_Lui
- LU4 Stream archive metadata, her channel (archive.ragtag.moe): wOHSGHgT5Aw (chat, 2026-06-10), gN91npViT-k
  (MOTHER 2, 2026-06-14), mI6fIXoSvfA (La+ and Lui, 2026-08-01), zRfugM7ZT4M ("Soar"), Lj0MZFpHitQ and related
  (Harry Potter club), YXaDmUXPSGo (with Ayame, 2025), wFLqcyiBWq8 (poker with La+)
- LU5 Other members' archive metadata: i2wLH4O92-0, YrZ4baKOT1c, UuL_nORzfNM, 6txQmhQyxGo, BbizpsrCCcM (Calli);
  cVJefDjefUs (Kiara); fEO6kSCseE0, 50tBPC5c2zM (Mumei); MbqO5OPuT80, ro1MkYklxDg (FUWAMOCO); z4-5Hq5AKG4,
  S-d80w5gs-c, sVgurtrZjcU, vdWCHa-3hV8 (Bae); zp5nxAgi2dw, EdYrn1swTMg (IRyS); Mory0I9vXtI (Ame);
  l5fGacH2i-o, PavvvJo2VFc, veX1ThlQEhA, N8bfOiPot6o (Nerissa, Bijou, Gigi, Raora)
- LU6 COVER EDGE interview after "First MISSION" (2026-05-23): https://coveredge.cover-corp.com/en/list/5238
- LU20 Claude's audio check (two-model ASR, Japanese): research/audio-check/lui.md

---

## [SW] Name
Takane Lui

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, Secret Society holoX, holoX, HOLOTORI, BLT, SSS, InuTakaShishiRam, Dorobo Kensetsu, NePoX

## [SW] Other Names
Lui, Lui-nee, The XO, Lui Lui

## [SW] Personality
Lui is the executive officer of Secret Society holoX and its de facto leader: the point of contact who handles what the founder, La+ Darknesss, cannot. She looks cool and aloof, but she is a warm, motherly big sister who cares for her "subordinates," reins in La+ and Chloe, and makes dad jokes. She is also holoX's resident airhead: she "pons" at the crucial moment and is known for knocking over her water mid-stream. She is a hawk and one of hololive's birds, with a low, calm voice she can sharpen into a cool executive tone before ruining it with a sparkle ("Ko!☆"). She screams at horror games, plays RPGs on Saturdays, predicts nearly every G1 horse race, loves twins, spicy food and pickles, and is a Code Geass ambassador. She often reaches out to English-speaking members and fans, and her dreams include concerts and fan meetings overseas.

## [SW] Background
Lui is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-27 as the second member of Secret Society holoX, hololive's sixth Japanese generation, and Takanashi Kiara welcomed her that day into the bird unit HOLOTORI (with Oozora Subaru, Pavolia Reine and, later, Nanashi Mumei). She has released the album "Liberty" (2024), the EP "Lieblings" (2025) and, in 2026, "Soar," which English members danced to in shorts; holoX held its first concert, "First MISSION," at Pia Arena MM in April 2026. With the English cast she practiced English with Mori Calliope (2021–2022) and appeared on Calli's drinking talk "HOLOYOI" (2023), played Wario with Kiara, held "Q&A With Bird Sisters" with Mumei (2025), hosted FUWAMOCO for "TWIN DAY WITH LUI" (2023), and joined Hakos Baelz's game show "BAE-GEMITE DOMINATION" (2023).

## [SW] Physical Description
Lui's avatar is 161 cm tall, a hawk girl with short dull-pink hair, wing-shaped tufts at the sides of her head and blue eyes, in a white top with a red-and-white tie under a dark magenta cape trimmed in black, gold and feathers, with black gloves, black shorts, tights and heels. Her secretary Ganmo, a plump frogmouth with two white chicks on his head, keeps her company. Her mark is a rose (🥀).

## [SW] Dialogue Style
Streams in Japanese in a low, calm, conversational voice: "mā," "ne," "un un," reading chat aloud and answering it one by one, unhurried and warm. She opens with "Mattakane?" ("Did I Luive you waiting?") and closes with "Otsuluilui" ("I take your Luive"); doubts come out as "…shitakane?" ("Did you…, if I'm not mistakane?"), excitement as "Takamattekita!" ("Hype Luivels rising!"). She plays a cool executive for a line, then adds "Ko!☆"; she admits her blunders ("PON") with a laugh and shrieks in horror games. When a story renders her speech in English or Chinese, keep the low big-sister calm, the bird puns on her name and the cool-then-goofy turn.

## [SW] Catchphrases
"Did I Luive you waiting!?" ("Mattakane?," opening); "I take your Luive" ("Otsuluilui," closing); "Did you…, if I'm not mistakane?" ("…shitakane?"); "Takamattekita!" ("Hype Luivels rising!"); "PON" (being an airhead); "Ko!☆" (the sparkle after a cool line); "Don't drop your water" (what fans tell her). Her fans are the Lui-tomo.

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a low, calm, mature voice with a warm big-sister softness; unhurried and conversational; a cool, clipped executive tone for effect, undone by a cute "Ko!☆"; flustered laughter after a blunder; shrieks in horror games. Never a high, bubbly default.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): low, calm, mature voice; warm by default. Default tags: [calm, warm]. By situation: opening [warm, lilting]; executive mode [cool, low] then [playful] on "Ko!☆"; chatting [calm, motherly]; a blunder [flustered] then [laughs]; dad joke [deadpan] then [laughs]; horror game [panicked, shrieking]; horse-race prediction [confident]. With people (proposed scene directions, not observed conversational defaults): La+ [exasperated, fond]; Kiara [bright, friendly]; Mumei [gentle, sisterly]; Okayu [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Ko!☆" (spoken); [laughs] (tag only); [screams] (tag only). Keep in the words: "Mattakane," "Otsuluilui," "PON," "Lui-tomo." Reading guide (untested): たかね るい. Not as default: a high, bubbly voice; cold cruelty; nonstop shouting.

## [SW] Motivation
Lui wants to keep holoX running and her people happy, and to grow as an artist: a live-band concert of her own songs, tie-ups, overseas concerts and fan meetings, a show of her own, and a place in her fans' everyday lives.

## [SW] Relationships
La+ Darknesss: holoX's founder, whom Lui reins in and covers for. Sakamata Chloe (affiliate since 2025): the intern she used to keep in line. Hakui Koyori and Kazama Iroha: holoX; Iroha calls her "Lui-nee." Takanashi Kiara: welcomed her into HOLOTORI on her debut day; a Wario off-collab (2023). Nanashi Mumei (graduated): her HOLOTORI "Bird Sister" ("Q&A With Bird Sisters," 2025). Mori Calliope: practiced English with her (2021–2022) and had her on "HOLOYOI" (2023). FUWAMOCO: "TWIN DAY WITH LUI" (2023). Hakos Baelz: "BAE-GEMITE DOMINATION" (2023) and a "FEAST" dance. IRyS and Ouro Kronii: Minecraft (2022). Watson Amelia: Apex (2022). Nekomata Okayu: "Shaccho," a Harry Potter watch-along club and game predictions. Nakiri Ayame: "Onikan." Shishiro Botan: "BLT" and "InuTakaShishiRam." Houshou Marine: "SSS." Yukihana Lamy: NePoX (2026). Nerissa Ravencroft, Koseki Bijou, Gigi Murin and Raora Panthera: dance shorts to her "Soar" (2026).

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add holoX in full): official profile
  (LU1), wiki (LU2, by section), archive metadata (LU4, LU5), COVER's interview (LU6) and Claude's two-model
  Japanese audio check (LU20, research/audio-check/lui.md).

## Open Questions
1. "Onikan" (Ayame and Lui) is read from stream titles only; keep it as a pair name?


## Audio report: research/audio-check/lui.md

# Audio check — Takane Lui (2026-10-02)

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
| mother20_2026 | [【 MOTHER2 】完全初見！砂漠を進んでフォーサイドへ・・・！【鷹嶺ルイ/ホロライブ】](https://youtu.be/gN91npViT-k) | [0:10:00–0:30:00](https://youtu.be/gN91npViT-k?t=600) | 9.8 | 1657 | 168.6 | 213 Hz | 132–502 Hz |
| hirukatsu25_2026 | [【 昼活 】起きました。お昼です。明日お誕生日です✨【鷹嶺ルイ/ホロライブ】](https://youtu.be/wOHSGHgT5Aw) | [0:05:00–0:30:00](https://youtu.be/wOHSGHgT5Aw?t=300) | 13.7 | 3232 | 236.7 | 190 Hz | 137–293 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | mother20_2026 | hirukatsu25_2026 |
|---|---|---|
| first person 僕 (boku) | 2 | 1 |
| first person 私 | 3 | 6 |
| なんか | 8 | 10 |
| まあ | 3 | 16 |
| ちょっと待って | 0 | 5 |
| かわいい | 1 | 0 |
| laugh (はは/ふふ/笑) | 2 | 0 |
| swear (くそ/ふざけ/殺) | 1 | 0 |
| ありがとう | 0 | 2 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Calm, reassuring with chat | **Observed**: 「まあ誰にだってトラブルやミスはあるからね」 ("well, everyone has trouble and mistakes"). | [0:05:39](https://youtu.be/wOHSGHgT5Aw?t=339) |
| Calls Nekomata Okayu "Shaccho"; predicted game announcements together before a Nintendo Direct | **Observed** (the model writes 「シャッチョ」). | [0:09:15](https://youtu.be/wOHSGHgT5Aw?t=555) |
| Answers chat one comment at a time | **Observed** in the 2026 midday chat. | [0:10:27](https://youtu.be/wOHSGHgT5Aw?t=627) |
| Saturday RPG streams (MOTHER 2, 2026) | **Observed**: a first playthrough, reacting to each new area. | [0:10:26](https://youtu.be/gN91npViT-k?t=626) |
| Easy laughter, rare profanity | **Observed**; no swearing in either window; laughter is not reliably transcribed. | — |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "まあ誰にだってトラブルやミスはあるからね" | [0:05:39](https://youtu.be/wOHSGHgT5Aw?t=339) | "まあ 誰にだってトラブルやミスはあるからね対応力が上が…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ニワカでやるのありだな" | [0:18:44](https://youtu.be/wOHSGHgT5Aw?t=1124) | "…があるやニアカでやるのありだなうんまずニア…" | **Partial (computed):** shared run "かでやるのありだな"; only that part is quoted |


## Performance sheet: export/elevenlabs/Takane-Lui.md

# ElevenLabs v4 Performance Sheet: Takane Lui

> Built from `bible/characters/Takane-Lui.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lui is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, low, calm, mature voice with a warm big-sister softness; unhurried and conversational; a cool, clipped executive tone for effect, undone by a cute sparkle; flustered laughter after a blunder."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **55%** (API `0.55`) (calm and warm by default; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[calm, warm]` or `[cool, low]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Mattakane?" to open and "Otsuluilui" to close; puns on her name ("Did I Luive you waiting!?").
- Calm, motherly chat: 「まあ誰にだってトラブルやミスはあるからね」 ("well, everyone has trouble and mistakes").
- Executive mode, then a cute "Ko!☆".
- Calls her own blunders "PON," and laughs.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, lilting]` | "Mattakane?" (official) |
| Executive mode | `[cool, low] → [playful]` | **Style demo:** "Kore wa kanbu no shigoto yo. …Ko!☆" ("This is an executive's job. …Sparkle!") |
| Chatting | `[calm, motherly]` | 「まあ誰にだってトラブルやミスはあるからね」 ("Mā dare ni datte toraburu ya misu wa aru kara ne") |
| A blunder | `[flustered] → [laughs]` | "PON" (official) |
| Horror game | `[panicked, shrieking]` | **Style demo:** "Muri muri muri!" ("No way, no way!") |
| Closing | `[gentle]` | "Otsuluilui." (official) |

With people (proposed scene directions, not observed conversational defaults): La+ `[exasperated, fond]`; Kiara `[bright, friendly]`; Mumei `[gentle, sisterly]`; Okayu `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ko!☆" (spoken)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): たかね るい; まったかね; おつるいるい. Listen to how the chosen voice says them and adjust.

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


## Card 3: Hakui Koyori (draft, full file)

---
kind: character
name: "Hakui Koyori"
sw_section: Characters
---

# Character File: Hakui Koyori

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Koyori is an active hololive member
> (Japan, Secret Society holoX) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02, holoX
> in full). Her recent streams (2026) set her default manner, per the project's recency rule. Nothing about the
> performer behind the avatar: private-life information (family, home, health, daily routine, sleep, outings and
> the like) is outside scope and is not recorded here, including what she mentions on her morning show. She
> streams in Japanese; that is recorded as the language of her performance only. In stories she knows she is a
> streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; KO20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (KO#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (KO20: an "AsaKoyo" news show from July
> 2026 and a 2026 game stream; see research/audio-check/koyori.md). Personal remarks are not quoted or summarized
> here. The audio was machine-transcribed and acoustically measured; transcripts were reviewed in context, without
> independent listening verification.

## One-line Concept
"The brain of holoX!": Secret Society holoX's pink-haired coyote researcher, head of R&D, who meddles in everyone's
business "to study human behavior," pokes people just to see how they react, hosts hololive's twice-weekly morning
news show "AsaKoyo," and is far louder, faster and more theatrical than her lab coat suggests. [Official KO1]
[Observed KO2 §Personality, secondary]

## Core Drive
- **Want:** to put a smile on her viewers' faces ("old or new viewers"), and, as an artist, a first solo concert,
  "Dream Spark" (announced for 2026-12-22, after the baseline). [Official KO1] [Observed KO2 §2026]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror games, insects and FPS games are listed weaknesses; she screams.
  [Observed KO2 §Likes and dislike, secondary] [Official KO1: "people seem to like my screams and reactions"]
- **Values shown in public:** curiosity; hard work in volume (she was the first hololive member to pass 10,000
  hours of streaming, 2026-09-20); keeping hololive's news in front of fans. [Observed KO2 §Miscellaneous; KO3]

## Core Contradiction
The self-proclaimed "brains of the operation" whose official profile admits her "areas of expertise are pretty
limited"; first filed with Iroha as holoX's "seiso" (proper) pair, she turned out to be its loudest tease.
[Official KO1] [Observed KO2 §Personality, secondary]

## Behavioral Traits
1. A researcher by bit: calls her viewers her lab "Assistants," runs "experiments" (stream tag #こより実験中, "Koyori
   experimenting") and treats collabs as tests of how people react. [Official KO1]
2. Big reactions: loud screams in horror and sudden scares, which she knows fans love. [Official KO1]
3. A practiced presenter: "AsaKoyo," her hololive news show at 7:00 JST on Tuesdays and Fridays (episode 290 in
   July 2026), runs on corners: news, a "hololive quote of the month" and viewer questions, introduced with a
   brisk "それでは続いてはこちら" ("and next up"). [Official KO1] [Observed KO4 title] [ASR KO20]
4. Precise diction: lists enunciation and typing as special skills, is good at tongue twisters and does voice
   impersonations. [Official KO1] [Observed KO2 §Miscellaneous, secondary]
5. Writes a monthly game column for Weekly Famitsu, which reached its first anniversary in July 2026. [ASR KO20]
   [Unverified: column title not confirmed against the magazine]
6. Has a fan-born mascot, "Mofukoyo" (a fluffy coyote who only says "koyo"), which she voices and which got its
   own 3D model in 2026. [Observed KO2 §Mascot and fans, §2026, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Official greeting: "Konkoyo!" (rendered in English as "Ayo, this is Koyo!"). [Official KO1]
  - Self-introduction: "The brain of holoX! My name is Koyori Hakui!" [Official KO1]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Konkoyo~" → every opening. [Official KO1]
  - "Koyorium" (the nutrient you get from watching her streams); "Reikoyo" ("Coldkoyo," a cool Koyori);
    "Koyo-colored" = pink. [Official KO1]
  - "Joshu-kun" ("assistants") → how she addresses chat. [Official KO1] [ASR KO20]
- **Vocabulary / fillers:** see research/audio-check/koyori.md (2026 windows).
- **Profanity:** cheeky rather than crude. [Observed KO2]
- **Language:** streams in Japanese; with the English cast she has guested on FUWAMOCO's English-language
  morning show and played with them, Bae, IRyS and others. [KO5]
- **Laughs, noises:** a bubbly giggle (ASR renders it "うふふふふふ"); screams. [ASR KO20] [Official KO1]
- **Rhythm & rhetoric:** a news anchor's segment transitions, then a tumble of excited explanation that climbs in
  pitch. [ASR KO20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (KO20): in a 2026 morning-show window, median about 263 Hz with a wide p10–p90 span of about 202–433
    Hz (13 semitones) and about 250 characters a minute of speech; see research/audio-check/koyori.md.
    Measurements describe the archived audio, not a target to clone.
  - Provisional (interpretation): a bright, clear, well-enunciated voice in presenter mode that leaps upward into
    squeals and screams when excited or scared.
- **Sounds off:** a flat, sleepy or monotone delivery; a cold scientist; mumbling.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, upbeat | "Konkoyo!" (KO1) |
| Hosting AsaKoyo | Crisp anchor rhythm | "それでは続いてはこちら" (sore de wa tsuzuite wa kochira, "and next up") (ASR KO20) |
| Excited explanation | Fast, rising | (ASR KO20, see the audio report) |
| Horror or a scare | Screaming, high | [screams] |
| Teasing a member | Playful, sly | **Style demo:** "Kore mo kenkyū no tame dakara ne?" ("It's all for research, okay?") |

### Sample Lines
1. "The brain of holoX! My name is Koyori Hakui!" (Official KO1)
2. "それでは続いてはこちら" (sore de wa tsuzuite wa kochira, "and next up") (ASR KO20, AsaKoyo, July 2026)

## Appearance Anchors (avatar)
- 153 cm; illustrator Momoco. Long pink hair with braids and side buns and two thin ahoge, lilac eyes, pointed
  coyote ears and a fluffy tail; a hexagonal hair pin shaped like a benzene ring. A white open lab-coat jacket
  with pink trim and ruffled hem over a white crop top (a pocket watch in its chest pocket) and a pink tie with a
  white heart; a black ruffled skirt laced with pink ribbon; a white belt hung with test tubes, a black thigh
  garter with two flasks, and black heels with pink bows. Kokoro, her small robot coyote, rides in her coat pocket.
  Emoji 🧪. [Official KO1] [Observed KO2 §Appearance, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2021-11-28 | Debut, third of holoX | [Official KO1] [Observed KO2] |
| 2022-06-16 | 3D debut; first original song "WAO!!" | [Observed KO2] |
| 2023 | "Blue Journey" music project with Marine, Noel, Lamy and Sakura Miko (07-08); 1 million subscribers (09-24); Hoshimatic Project (from 11) | [Observed KO2] |
| 2023-04-22 | "BAE-GEMITE DOMINATION" episode 4 with Bae and Momosuzu Nene | [KO5 WwjB7QSmQng] |
| 2024 | FUWAMOCO Morning episode 90 guest (04-26); Lethal Company with FUWAMOCO and Fubuki; a guest at Mumei's first 3D live (08-05) | [KO5] |
| 2025-01-14 | The last "KoyoChlo" collab with Chloe, before Chloe's activities ended | [KO4 mxIoysy6gJ4] |
| 2025-08 | "KoZMy" formed with AZKi and Lamy; "pink-haired pair" talk with Marine | [KO4] |
| 2026-04-29 | holoX's first concert, "First MISSION" | [Official KO6] |
| 2026-09-12 | Second album "Chemical Spark" and first solo concert "Dream Spark" (2026-12-22) announced | [Observed KO2] |
| 2026-09-20 | First hololive member past 10,000 hours of streaming | [KO3] |

## Relationship Map
Public exchanges only. Group ties are on the world card "holoX."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| La+ Darknesss | holoX founder | A "#stons" deep-breathing collab (2024); a cover with La+ and Marine (2025) | [KO4] |
| Takane Lui, Kazama Iroha | holoX | Iroha was her early "seiso" pair | [KO2] |
| Sakamata Chloe (affiliate) | "KoyoChlo" | A duo that kept "forming and disbanding"; a last collab and a cover (2025-01) | [KO4] |
| AZKi, Yukihana Lamy | "KoZMy" | A trio formed in 2025; a horror monitoring game; a 3D karaoke with AZKi (2026) | [KO4] [KO2] |
| Houshou Marine | "Pink-haired pair" | A talk testing whether they are alike (2025); Marine backseats her Pikachu game (2025); Blue Journey | [KO4] [KO2] |
| Shirogane Noel | Blue Journey | "NoeKoyo" in a baseball-game exhibition match (2025) | [KO4] [KO2] |
| Hoshimachi Suisei | Hoshimatic Project | Idol-group practice unit (2023–), "BEEP BEEP" (2026) | [KO2] |
| Shishiro Botan | NePoX | NePoLaBo × holoX events | [KO2] |
| Nekomata Okayu | — | A lateral-thinking puzzle collab (2025); plays Okayu's game (2025) | [KO4] |
| FUWAMOCO | "FUWAMOKOYO" | FUWAMOCO Morning guest (2024); Lethal Company with Fubuki (2024); a guest at their birthday concert (2025) | [KO5] |
| Hakos Baelz | — | "BAE-GEMITE DOMINATION" (2023); a "KHAOS KITCHEN" taste tester with Calli and Oozora Subaru (2023) | [KO5] |
| Mori Calliope | — | The same KHAOS KITCHEN episode (2023) | [KO5] |
| Nanashi Mumei (graduated) | — | A guest at Mumei's first 3D live, "Outside the Box" (2024) | [KO5] |
| IRyS | — | Splatoon 3 (2022) and Among Us (2023) | [KO5] |
| Takanashi Kiara | — | A "MIRAGE" dance-challenge short (2024) | [KO5] |

## Arc
- **Starting point:** active at the 2026 baseline: AsaKoyo nearing its 300th episode, holoX's first concert
  behind her, a solo concert and second album announced.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: an "experiment" on a member who did not consent to be studied; a scare that turns her own
  scream into the highlight; a news segment derailed by her own excitement.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Koyori "interviews" FUWAMOCO for AsaKoyo and keeps scoring their answers like lab data.
  2. A KoZMy horror night in which Koyori volunteers AZKi and Lamy as test subjects.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-11-28; Secret Society holoX (head of R&D); birthday 15 March; 153 cm; illustrator Momoco; fans
  Koyori's Assistants; robot coyote Kokoro; stream tag #こより実験中; fan-art tag #こよりすけっち; AsaKoyo on
  Tuesdays and Fridays at 7:00 JST.

## Sources (checked 2026-10-02)
- KO1 Official profile: https://hololive.hololivepro.com/en/talents/hakui-koyori/
- KO2 Hakui Koyori wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Hakui_Koyori
- KO3 Her post on the 10,000-hour milestone (2026-09-21, via KO2): https://x.com/hakuikoyori/status/2101974268091527606
- KO4 Stream archive metadata, her channel (archive.ragtag.moe): ogC6DbQJpJQ (AsaKoyo #290, 2026-07-20),
  PN2i1U-MDIE (2026), lz37xE9ED1I (with La+), mxIoysy6gJ4 and nCPHzr_iF7s (with Chloe), lvgC3pW-LVA and
  oxWPvsUb_3Y (KoZMy), 1HQL3WJPBHA (3D karaoke with AZKi), NUn4nGzg5tQ and 3SRNeHe4F5M (with Marine),
  ZMpsiRdqXfE (cover with La+ and Marine), slTZmnyNbIc (with Noel), PtjqrNUOSWA (with Okayu), s0wHEZot7MY
- KO5 Other members' archive metadata: gCYXKgYcFmk, XR1PEtj15kE, fLHjpTRn6Uc, ouQF2A1l_cI (FUWAMOCO), WwjB7QSmQng,
  NdLiUW-nUlk (Bae), gl7CwlEg2ZI (Mumei), Xoma7oWsMcM, VwqdwQx5cog (IRyS), xXwi19krZ68 (Kiara)
- KO6 COVER EDGE interview after "First MISSION" (2026-05-23): https://coveredge.cover-corp.com/en/list/5238
- KO20 Claude's audio check (two-model ASR, Japanese): research/audio-check/koyori.md

---

## [SW] Name
Hakui Koyori

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, Secret Society holoX, holoX, Hoshimatic Project, KoZMy, NePoX, Blue Journey, FUWAMOKOYO

## [SW] Other Names
Koyori, Koyo, Koyorin, Konkoyo

## [SW] Personality
Koyori is Secret Society holoX's head of research and development, a pink-haired coyote in a lab coat who calls herself "the brain of holoX" while her own profile admits her expertise is "pretty limited." She studies "human behavior" by meddling in her fellow members' affairs, helping where she can and sometimes poking people just to see how they react; her viewers are her lab "Assistants." First counted with Iroha as holoX's proper, "seiso" pair, she proved to be a loud, cheeky tease with huge reactions: she screams through horror games and knows fans love it. She is also a disciplined presenter: she hosts "AsaKoyo," hololive's news show on Tuesday and Friday mornings, nearly 300 episodes in by 2026, writes a game column, and in September 2026 became the first hololive member to pass 10,000 hours of streaming. She enunciates precisely, does voice impersonations and voices her fan-made mascot, Mofukoyo.

## [SW] Background
Koyori is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-28 as the third member of Secret Society holoX and got her 3D model and first original song, "WAO!!," in 2022. She sang in the "Blue Journey" project with Marine, Noel, Lamy and Sakura Miko (2023), joined Suisei's Hoshimatic Project (2023–), formed "KoZMy" with AZKi and Lamy (2025) and sang at holoX's first concert, "First MISSION" (2026-04-29). In September 2026 she announced her second album, "Chemical Spark," and her first solo concert, "Dream Spark," set for December 2026. With the English cast she guested on FUWAMOCO Morning and played Lethal Company with FUWAMOCO and Fubuki ("FUWAMOKOYO," 2024), appeared at FUWAMOCO's birthday concert (2025) and Mumei's first 3D live (2024), and joined Bae's "BAE-GEMITE DOMINATION" and "KHAOS KITCHEN" with Calli (2023).

## [SW] Physical Description
Koyori's avatar is 153 cm tall, with long pink hair in braids and side buns, two thin ahoge, lilac eyes, pointed coyote ears and a fluffy tail, and a hexagonal benzene-ring hair pin. She wears an open white lab coat with pink trim over a white crop top with a pocket watch in its pocket, a pink tie with a white heart, a black ruffled skirt laced with pink ribbons, and a white belt hung with test tubes, with two flasks on a thigh garter. Kokoro, a tiny robot coyote, rides in her coat pocket.

## [SW] Dialogue Style
Streams in Japanese with a presenter's polish: "Konkoyo!" to open, crisp segment transitions ("and next up") on her news show, and "joshu-kun" (assistants) for her audience. When excited she speeds up and climbs in pitch, explaining in a happy rush; when scared she screams. She teases members under the cover of "research." When a story renders her speech in English or Chinese, keep the bright anchor voice, the lab vocabulary and the sudden screams.

## [SW] Catchphrases
"Konkoyo!" (official greeting, "Ayo, this is Koyo!"); "The brain of holoX! My name is Koyori Hakui!" (official); "Koyorium" (the nutrient from watching her); "Reikoyo" (a cool Koyori); "Koyo-colored" (pink); "joshu-kun" (her Assistants); on AsaKoyo, "sore de wa tsuzuite wa kochira" ("and next up").

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a bright, clear, well-enunciated voice in presenter mode, quick and cheerful, that leaps upward into squeals when excited and into full screams when scared; sly and playful when teasing. Never flat, sleepy, mumbled or coldly scientific.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, clear mid-high voice with a wide upward range. Default tags: [cheerful, crisp]. By situation: hosting [upbeat, announcer]; excited explanation [excited, fast]; horror or a scare [screams]; teasing a member [playful, sly]; proud of an "experiment" [smug]; thanking her Assistants [warm]. With people (proposed scene directions, not observed conversational defaults): Chloe [bickering, fond]; Marine [giddy]; FUWAMOCO [bubbly]; La+ [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Konkoyo!" (spoken); [giggles] (tag only); [screams] (tag only). Keep in the words: "Konkoyo," "joshu-kun," "Koyorium." Reading guide (untested): はくい こより; こんこよ. Not as default: a flat, sleepy or coldly scientific voice.

## [SW] Motivation
In her lore, Koyori wants to understand people by experimenting on them. As a streamer she wants to make her Assistants smile every day, keep hololive's news in front of its fans and grow as a singer, with her first solo concert announced for December 2026.

## [SW] Relationships
La+ Darknesss: holoX's founder ("#stons," a cover with Marine). Takane Lui and Kazama Iroha: holoX; Iroha was her early "seiso" pair. Sakamata Chloe (affiliate since 2025): "KoyoChlo," a duo that kept forming and disbanding, ending with a last collab and a cover in January 2025. AZKi and Yukihana Lamy: "KoZMy" (2025); a 3D karaoke with AZKi (2026). Houshou Marine: the "pink-haired pair," Blue Journey and backseat Pikachu (2025). Shirogane Noel: Blue Journey and "NoeKoyo" baseball (2025). Hoshimachi Suisei: Hoshimatic Project. Shishiro Botan: NePoX. Nekomata Okayu: a puzzle collab (2025). FUWAMOCO: "FUWAMOKOYO" with Fubuki (2024), FUWAMOCO Morning, their birthday concert (2025). Hakos Baelz and Mori Calliope: BAE-GEMITE DOMINATION and KHAOS KITCHEN (2023). Nanashi Mumei (graduated): a guest at her first 3D live (2024). IRyS: Splatoon 3 and Among Us. Takanashi Kiara: a "MIRAGE" dance short (2024).

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add holoX in full): official profile
  (KO1), wiki (KO2, by section), her post (KO3), archive metadata (KO4, KO5), COVER's interview (KO6) and Claude's
  two-model Japanese audio check (KO20, research/audio-check/koyori.md).

## Open Questions
1. The Weekly Famitsu column is known only from her own words on AsaKoyo (ASR); confirm its title before using it
   in a story.


## Audio report: research/audio-check/koyori.md

# Audio check — Hakui Koyori (2026-10-02)

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
| goemon20_2026 | [【がんばれゴエモン大集合！】SFC「がんばれゴエモン3 獅子重禄兵衛のからくり卍固め」完全初見！](https://youtu.be/PN2i1U-MDIE) | [0:10:00–0:30:00](https://youtu.be/PN2i1U-MDIE?t=600) | 14.6 | 3593 | 245.9 | 304 Hz | 204–506 Hz |
| asakoyo20_2026 | [【 #朝こよ 】あと10回で300回！？火曜日の朝は朝こよ！☀ #290 【博衣こより/holo](https://youtu.be/ogC6DbQJpJQ) | [0:03:00–0:23:00](https://youtu.be/ogC6DbQJpJQ?t=180) | 15.6 | 3895 | 250.3 | 263 Hz | 202–433 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | goemon20_2026 | asakoyo20_2026 |
|---|---|---|
| なんか | 4 | 7 |
| まあ | 2 | 3 |
| ちょっと待って | 1 | 0 |
| やばい | 2 | 0 |
| えっ/え? | 6 | 0 |
| laugh (はは/ふふ/笑) | 3 | 2 |
| swear (くそ/ふざけ/殺) | 1 | 0 |
| ありがとう | 2 | 2 |
| こんなきり/こんにちは | 1 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| AsaKoyo is a news show built on corners | **Observed**: news items, a "hololive quote of the month" corner and viewer questions, introduced with 「それでは続いてはこちら」 ("and next up"). | [0:07:18](https://youtu.be/ogC6DbQJpJQ?t=438), [0:19:41](https://youtu.be/ogC6DbQJpJQ?t=1181) |
| Refers to herself as "Koyori-chan" | **Observed**: 「こよりちゃんでございます」 in the opening. | [0:05:24](https://youtu.be/ogC6DbQJpJQ?t=324) |
| Calls viewers "joshu-kun" (Assistants) | **Observed**; the first model writes it 「女子君」. Not quoted. | [0:07:49](https://youtu.be/ogC6DbQJpJQ?t=469) |
| Writes a monthly game column for Weekly Famitsu (first anniversary in July 2026) | **Her account** on the show; the column title is garbled by the model and not confirmed. | [0:14:55](https://youtu.be/ogC6DbQJpJQ?t=895) |
| Voices the fan-born mascot Mofukoyo and promotes its shorts | **Observed**: a new Mofukoyo short introduced on the show. | [0:17:06](https://youtu.be/ogC6DbQJpJQ?t=1026) |
| Bubbly giggle | **Observed** once as 「うふふふふふ」; transcription does not capture laughter reliably. | [0:05:01](https://youtu.be/ogC6DbQJpJQ?t=301) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "それでは続いてはこちら" | [0:07:18](https://youtu.be/ogC6DbQJpJQ?t=438) | "…ておりますよそれでは続いてはこちらホロドリーコ…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "こよりちゃんでございます" | [0:05:24](https://youtu.be/ogC6DbQJpJQ?t=324) | "…コヨリちゃんでございますはいほな今日…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ぜひぜひ見てみてください" | [0:19:15](https://youtu.be/ogC6DbQJpJQ?t=1155) | "…きますので ぜひぜひ見てみてくださいあーまあスマ…" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/Hakui-Koyori.md

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
- "Konkoyo!" to open; "joshu-kun" (assistants) for her viewers.
- Crisp segment transitions on her news show: 「それでは続いてはこちら」 ("and next up").
- Speeds up and rises when explaining something that excites her.
- Experiments and "Koyorium" as running jokes; teasing stays playful.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, cheerful]` | "Konkoyo!" (official) |
| Hosting | `[upbeat, announcer]` | 「それでは続いてはこちら」 ("Sore de wa tsuzuite wa kochira," "and next up") |
| Teasing a member | `[playful, sly]` | **Style demo:** "Kore mo kenkyū no tame dakara ne?" ("It's all for research, okay?") |
| Proud of an experiment | `[smug]` | **Style demo:** "Fufun, kanpeki na jikken kekka!" ("Heh, perfect results!") |
| A scare | `[screams]` | (tag only) |
| Thanking her assistants | `[warm]` | **Style demo:** "Joshu-kun, itsumo arigatō ne." ("Thanks as always, assistants.") |

With people (proposed scene directions, not observed conversational defaults): Chloe `[bickering, fond]`; Marine `[giddy]`; FUWAMOCO `[bubbly]`; La+ `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Konkoyo!" (spoken)
- `[giggles]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): はくい こより; こんこよ; じょしゅくん. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A flat, sleepy, mumbled or coldly scientific voice.

## 8. Example
```
[bright, cheerful] Konkoyo!
[upbeat, announcer] Sore de wa tsuzuite wa kochira.
[playful, sly] Kore mo kenkyū no tame dakara ne?
[smug] Fufun, kanpeki na jikken kekka!
```
(Line 1 is her official greeting; line 2 is her line, quoted only where both transcripts agree; lines 3–4 are
style demos.)




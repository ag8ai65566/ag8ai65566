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
  Takane Lui, Hakui Koyori, Sakamata Chloe, Kazama Iroha), with their ties to the rest of the cast. This is run D of four: Botan, Vivi, the world card "JP Senpai Pairs 2" and the lines about Marine, Noel, Lamy, Botan and Vivi added to the other cast cards (listed at the end). Run C covered Marine, Noel and Lamy's own cards.
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

## Card 1: Shishiro Botan (draft, full file)

---
kind: character
name: "Shishiro Botan"
sw_section: Characters
---

# Character File: Shishiro Botan

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Botan is an active hololive member
> (hololive JP, 5th generation) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02). Her
> recent streams (2026) set her default manner, per the project's recency rule. Nothing about the performer behind
> the avatar: private-life information (family, home, health, diet, daily routine, outings and food tours,
> languages she studies and the like) is outside scope and is not recorded here, including what she mentions in
> chats and what the wiki lists. She streams in Japanese; that is recorded as the language of her performance
> only. In stories she knows she is a streamer with a persona (see the world card "VTuber Persona and Lore").
> Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; BO20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (BO#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (BO20: her May 2026 announcement of the
> "#ホロ金策サバイバル2" Minecraft event and a June 2026 Forza Horizon 6 stream; see research/audio-check/botan.md).
> The audio was machine-transcribed and acoustically measured; transcripts were reviewed in context, without
> independent listening verification.

## One-line Concept
"La-lion♪": hololive's 5th-generation white lion in a sporty black tracksuit look, officially a laid-back gamer
who would rather laze around, in practice a calm, laughing FPS ace who plans ahead, runs whole server events
as their game master, and tosses grenades with an offhand "Poi!" [Official BO1] [Observed BO2 §Personality,
secondary] [BO4 titles]

## Core Drive
- **Want:** to give her viewers and fellow members a fun, well-built experience; in 2026 she ran a second
  season of her hololive-wide Minecraft money-making event as its game master, hosted the "Shishiro Cup" fighting-
  game tournament, and announced her first album, "BOTAN.EXE." [Observed BO2 §Personality, §2026, secondary; BO4
  titles] [ASR BO20]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** none sourced; horror barely scares her, "especially if the character has a
  gun." [Observed BO2 §Miscellaneous, secondary]
- **Values shown in public:** follow-through ("once she has made up her mind she will always follow through to
  the end"); a structured schedule; making sure everyone, including members who can join only one day, can enjoy
  her events. [Official BO1] [Observed BO2] [ASR BO20]

## Core Contradiction
A white lion who "prefers lazing around" by her official profile, and who is in fact a highly organized
member: weekly schedules, a self-edited debut intro, PC building, and whole events she designs and
runs. [Official BO1] [Observed BO2 §Personality, §Likes, secondary]

## Behavioral Traits
1. Laughs often, especially when something goes wrong; stays laid-back through intense play and chaos. [Observed
   BO2 §Personality, secondary]
2. "Poi!" (ぽいっ) when she lobs a grenade, calm or playful. [Observed BO2 §Miscellaneous, caption, secondary]
3. Runs projects: "#ホロ金策サバイバル" (2025) and season 2 (2026-06-01 to 06-05), a Minecraft event where members
   compete to earn the most money, with jobs (fighter, farmer, alchemist, gambler) and dungeons; she plays the
   game master and a ramen-shop owner in "Holotown." [BO4 titles] [ASR BO20]
4. Teases her friends and drags them into horror; with Yukihana Lamy, "horror date" streams where Botan stays
   calm and gently teases Lamy's screams. [Observed BO2 §Personality, §Miscellaneous, secondary]
5. Refers to herself as "Shishiro" (or "Shishiron") and turns presenter when she explains a project, with a quick
   "this part turns into explanation mode, bear with me." [ASR BO20]
6. A ramen lover in her content: "Menya Botan" in Minecraft, ramen at her 3D birthday stream, a 2026 ramen
   collaboration. [Observed BO2 §Likes, secondary] [Official BO1 news]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "La-lion♪" and "Well then, cya~" [Official BO1]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Poi!" → throwing a grenade. [Observed BO2]
  - "Shishiro" / "Shishiron" → herself. [ASR BO20] [Observed BO2 nickname]
  - "SSRB" → her fans (and their bomb-like lion mascot). [Official BO1] [Observed BO2 §Mascot]
- **Vocabulary / fillers:** "ichiō" ("for now"), "chotto," "hai," "~to omotte orimasu" when she presents; see
  research/audio-check/botan.md. [ASR BO20]
- **Profanity:** mild; easygoing. [ASR BO20]
- **Language:** streams in Japanese; with the English cast she joined Calli's HOLOYOI (2023, alcohol-free
  edition) and Bae's BAE-GEMITE DOMINATION (2023), both with Oozora Subaru. [BO5]
- **Laughs, noises:** a characteristic laugh (prized by fans, per the wiki); a giggly "fufu, hehehe" when a
  surprise is coming. [Observed BO2] [ASR BO20]
- **Rhythm & rhetoric:** very fast and organized when presenting: about 368 characters a minute of speech in a
  2026 announcement, with numbered points and polite "~to omotte orimasu" closings. [ASR BO20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (BO20): in that 2026 announcement window, median about 239 Hz (p10–p90 about 178–402 Hz, 14
    semitones) and about 368 characters a minute of speech; see research/audio-check/botan.md. Measurements
    describe the archived audio, not a target to clone.
  - Provisional (interpretation): a clear, cool-toned but cheerful voice, higher than her mature look suggests
    (fans expected a deep voice, per the wiki); relaxed in play, brisk and orderly when she presents.
- **Sounds off:** a gruff, deep "tough girl" voice; a sleepy drawl; panic in horror.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, breezy | "La-lion♪" (BO1) |
| Presenting a project | Brisk, organized | "前回はですねペコちゃんが優勝しました" (zenkai wa desu ne, Peko-chan ga yūshō shimashita, "last time, Peko-chan won") (ASR BO20) |
| Looking back | Amazed, warm | **Style demo:** "Mō ichinen ka, hayai ne." ("A year already, huh. That was fast.") |
| Throwing a grenade | Offhand | "Poi!" (BO2) |
| Teasing Lamy in horror | Calm, amused | **Style demo:** "Daijōbu daijōbu, mada nani mo dete nai yo." ("It's fine, it's fine, nothing's even come out yet.") |
| Closing | Easy | "Well then, cya~" (BO1) |

### Sample Lines
1. "La-lion♪" (Official BO1)
2. "前回はですねペコちゃんが優勝しました" (zenkai wa desu ne, Peko-chan ga yūshō shimashita, "last time, Peko-chan
   won") (ASR BO20, May 2026)

## Appearance Anchors (avatar)
- 166 cm; illustrator tomari. Long silver-white hair, lion ears and a lion's tail, grey eyes; a black sleeveless
  top with three white stripes, a black choker with a gold chain, an oversized black jacket with a fur-lined hood
  worn off the shoulders, a grey miniskirt with a lettered belt, one leg in a torn black stocking with a strap,
  and black heeled ankle boots. Her fans' mascot is a bomb-shaped lion "SSRB." [Official BO1 key art, described
  by Claude] [Observed BO2 §Mascot, secondary]
- Fans nicknamed her look "Adidas Lion" for its tracksuit-like stripes. [Observed BO2 §Miscellaneous, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2020-08-14 | Debut, hololive 5th generation; her debut intro video was her own edit | [Official BO1] [Observed BO2] |
| 2022-04-24 | Left 4 Dead 2 with IRyS | [BO5 K1wStJxm4F0] |
| 2023 | BAE-GEMITE DOMINATION #2 with Bae and Subaru (04-08); HOLOYOI #03 with Calli and Subaru (05-18); an Overwatch 2 team with IRyS, Lui, Chloe and Towa (08) | [BO5] |
| 2024-04-01 | A "furball lion" model designed by Shirakami Fubuki | [Observed BO2] |
| 2025 | 1.5 million subscribers, first of her generation (02-14); originals "Simulacre," "Gaotteko!" and "boundary"; a guest at Ina's birthday 3D live "EVERMORE" (05-21); the first "#ホロ金策サバイバル" | [Observed BO2] [BO5] [ASR BO20] |
| 2026-04 | The "Shishiro Cup" fighting-game tournament, offline; original "Tokihanate" (04-10) | [BO4] [Observed BO2] |
| 2026-06-01/05 | "#ホロ金策サバイバル2," with Botan as game master | [BO4] [ASR BO20] |
| 2026-09-19 | First album "BOTAN.EXE" announced; original "Stray & Stay" | [Observed BO2] |
| 2026-09-26/27 | NePoX events with Secret Society holoX | [LM4 Ml1tM8S40p0] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Yukihana Lamy | 5th-gen genmate; NePoLaBo | "Horror dates" where Botan stays calm and teases Lamy | [BO2] |
| Takane Lui | "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame; "BLT" | An Overwatch 2 team (2023) | [BO2] [BO5] [Lui file] |
| La+ Darknesss, Hakui Koyori, Kazama Iroha | NePoX | NePoLaBo × holoX events (2026) | [BO2] |
| Kazama Iroha | — | Built the roof of Botan's Minecraft shop (2023) | [Iroha file] |
| Sakamata Chloe (affiliate) | — | The 2023 Overwatch 2 team | [BO5] |
| La+ Darknesss, Nakiri Ayame, Hoshimachi Suisei | — | holoGTA and poker (2024) | [La+ file] |
| Takanashi Kiara | "Usada Kensetsu" (Usaken) | The Minecraft construction company of Pekora's circle | [BO2] |
| Gawr Gura (graduated) | "Apex Predators" | A pair name for their Apex play (secondary) | [BO2] |
| IRyS | — | Left 4 Dead 2 (2022); the Overwatch 2 team (2023) | [BO5] |
| Mori Calliope | — | HOLOYOI #03 with Subaru (2023) | [BO5] |
| Hakos Baelz | — | BAE-GEMITE DOMINATION #2 with Subaru (2023) | [BO5] |
| Ninomae Ina'nis | — | A guest at Ina's birthday 3D live "EVERMORE" (2025) | [BO5 I-J11Da5ONY] |

## Arc
- **Starting point:** active at the 2026 baseline: her second season of the Minecraft money-making event run, a
  fighting-game cup hosted, a first album announced.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: an event with rules so elaborate the players break them; a horror "date" that scares
  everyone but her; a grenade tossed with a cheerful "Poi!"
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Botan runs a money-making server event for the EN cast and Calli keeps buying out the ramen shop.
  2. Ina invites Botan back to a live, and Botan plans the whole stage logistics without being asked.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2020-08-14; hololive 5th generation; birthday 8 September; 166 cm; illustrator tomari; fans SSRB (first
  "Bodan"); stream tag #ぐうたらいぶ; fan-art tag #ししらーと.

## Sources (checked 2026-10-02)
- BO1 Official profile: https://hololive.hololivepro.com/en/talents/shishiro-botan/ (text and key art)
- BO2 Shishiro Botan wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Shishiro_Botan
- BO4 Stream archive metadata, her channel (archive.ragtag.moe): 9F8DKZa1L2s (event announcement, 2026-05-24),
  MSPdwwejtXU (Forza Horizon 6, 2026-06-21), KwqqkiFAh_4 and r2vb7Ibgk2M (the event, GM view), N6deX7jjPE8
  (Shishiro Cup), F697EVFrBM8
- BO5 Other members' archive metadata: EatMZc1N3VM (Calli), -0_9xCPljh0 (Bae), K1wStJxm4F0, roWKpgZsjR4 (IRyS),
  I-J11Da5ONY (Ina)
- BO20 Claude's audio check (two-model ASR, Japanese): research/audio-check/botan.md

---

## [SW] Name
Shishiro Botan

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 5th generation, NePoLaBo, holoFive, NePoX, InuTakaShishiRam, Usada Kensetsu, SubaChocoLunaTan

## [SW] Other Names
Botan, Shishiron, Shishiro, La~Lion

## [SW] Personality
Botan is hololive's white lion, who by her official profile "prefers lazing around" despite her sporty look, yet always follows through once she has decided; her favorite phrase is "Wealth isn't measured with money." On stream she is calm and laughs easily, especially when things go wrong, and she stays laid-back through the most intense play. She is a skilled FPS player who tosses grenades with an offhand "Poi!", is barely scared by horror (especially with a gun in hand), and likes dragging friends like Lamy into horror "dates" where she teases their screams. She is also highly organized: she keeps a weekly schedule, edited her own debut intro, builds PCs, and designs and runs whole events, from a hololive-wide Minecraft money-making competition to a fighting-game cup. She calls herself "Shishiro," turns into a brisk presenter when she explains a project, and makes sure everyone can enjoy it.

## [SW] Background
Botan is an active member of hololive's 5th generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2020-08-14 with Yukihana Lamy, Omaru Polka and Momosuzu Nene (together NePoLaBo), and was the first of her generation to pass 1.5 million subscribers (2025). She has released originals such as "Simulacre," "Gaotteko!" and "Tokihanate," announced her first album "BOTAN.EXE" in September 2026, ran the hololive Minecraft money-making event twice (2025, 2026) as its game master and hosted the "Shishiro Cup." With the English cast she played Left 4 Dead 2 and Overwatch 2 with IRyS, joined Calli's HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and was a guest at Ina's birthday 3D live "EVERMORE" (2025); Kiara is a fellow member of the Minecraft "Usada Kensetsu."

## [SW] Physical Description
Botan's avatar is 166 cm tall, with long silver-white hair, lion ears and a lion's tail, and grey eyes. She wears a black sleeveless top with three white stripes, a black choker with a gold chain, an oversized black jacket with a fur-lined hood slipping off her shoulders, a grey miniskirt with a lettered belt, one torn black stocking and black heeled ankle boots. Fans call the sporty stripes her "Adidas Lion" look.

## [SW] Dialogue Style
Streams in Japanese in a relaxed, cheerful voice, calling herself "Shishiro" and laughing at her own mishaps. In games she is calm and offhand ("Poi!" as a grenade flies); presenting a project she becomes fast and orderly, with numbered points, polite "I'd like to…" closings and a quick "bear with me while I explain." She teases friends gently and keeps everyone included. When a story renders her speech in English or Chinese, keep the easygoing calm, the laugh and the sudden organizer mode.

## [SW] Catchphrases
"La-lion♪" (official greeting); "Well then, cya~" (official sign-off); "Poi!" (tossing a grenade); "Wealth isn't measured with money" (her favorite phrase, official); "Shishiro" (herself); "SSRB" (her fans).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a clear, cool-toned but cheerful voice, higher than her mature look suggests; relaxed and amused in play, brisk and orderly when presenting, with an easy, frequent laugh. Never a gruff, deep "tough girl" voice, a sleepy drawl or panic in horror.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear, cool-toned, cheerful voice. Default tags: [relaxed, cheerful]. By situation: greeting [breezy]; presenting a project [brisk, organized]; FPS play [calm, focused]; a grenade [offhand] ("Poi!"); horror with a friend [amused, teasing]; a mishap [laughs]. With people (proposed scene directions, not observed conversational defaults): Lamy [teasing, protective]; Ina [warm]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Poi!" (spoken); [laughs] (tag only). Keep in the words: "Shishiro," "Poi," "SSRB." Reading guide (untested): ししろ ぼたん; ししろん. Not as default: a gruff or deep voice, or a sleepy drawl.

## [SW] Motivation
In her lore, Botan is a laid-back lion who would rather laze around. As a streamer she wants her viewers and fellow members to have a fun, well-run time, and she follows through on every project she takes on.

## [SW] Relationships
Yukihana Lamy: 5th-gen genmate and NePoLaBo partner; horror "dates" where Botan stays calm and teases Lamy. Takane Lui: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame, and "BLT." La+ Darknesss, Hakui Koyori and Kazama Iroha: NePoX (NePoLaBo × holoX). Sakamata Chloe (affiliate) and IRyS: an Overwatch 2 team (2023); IRyS also played Left 4 Dead 2 with her (2022). Takanashi Kiara: fellow member of the Minecraft "Usada Kensetsu." Gawr Gura (graduated): "Apex Predators" (a pair name). Mori Calliope: HOLOYOI #03 with Oozora Subaru (2023). Hakos Baelz: BAE-GEMITE DOMINATION #2 with Subaru (2023). Ninomae Ina'nis: a guest at Ina's birthday 3D live "EVERMORE" (2025).

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Shishiro Botan): official profile and
  key art (BO1), wiki (BO2, by section; health, diet, outings, language study and a member's relocation
  deliberately excluded), archive metadata (BO4, BO5) and Claude's two-model Japanese audio check (BO20,
  research/audio-check/botan.md).

## Open Questions
1. "Apex Predators" (with Gura) is wiki-listed; no Gura stream naming Botan was found in the archive metadata read.


## Audio report: research/audio-check/botan.md

# Audio check — Shishiro Botan (2026-10-02)

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
| talk20_2026 | [【企画告知】そろそろみんなで稼ぎませんか💰【獅白ぼたん/ホロライブ】](https://youtu.be/9F8DKZa1L2s) | [0:03:00–0:23:00](https://youtu.be/9F8DKZa1L2s?t=180) | 16.9 | 6235 | 368.3 | 239 Hz | 178–402 Hz |
| forza20_2026 | [【Forza Horizon 6】アクセル全開が四駆の基本だ！【獅白ぼたん/ホロライブ】](https://youtu.be/MSPdwwejtXU) | [0:10:00–0:30:00](https://youtu.be/MSPdwwejtXU?t=600) | 11.2 | 3202 | 286.6 | 232 Hz | 157–385 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | talk20_2026 | forza20_2026 |
|---|---|---|
| first person 私 | 5 | 6 |
| なんか | 0 | 7 |
| まあ | 13 | 2 |
| ちょっと待って | 3 | 3 |
| やばい | 0 | 3 |
| えっ/え? | 0 | 1 |
| laugh (はは/ふふ/笑) | 2 | 0 |
| ありがとう | 3 | 0 |
| English (Latin letters) | 4 | 10 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Runs a server event as its game master | **Observed**: she announces "#ホロ金策サバイバル2" (June 1–5, 2026), with jobs (fighter, farmer, alchemist, gambler) and dungeons, designed so members who can join only one day can still enjoy it. | [0:06:03](https://youtu.be/9F8DKZa1L2s?t=363), [0:10:36](https://youtu.be/9F8DKZa1L2s?t=636), [0:11:54](https://youtu.be/9F8DKZa1L2s?t=714) |
| Presents in an organized, fast register | **Observed**: numbered points, "this part turns into explanation mode, bear with me"; about 368 characters a minute of speech (a rough index). | [0:07:25](https://youtu.be/9F8DKZa1L2s?t=445) |
| Looks back on last year's event | **Observed**: 「前回はですねペコちゃんが優勝しました」 ("last time, Peko-chan won") and 「あれから1年経ってるっていうのがすごいね」. | [0:09:05](https://youtu.be/9F8DKZa1L2s?t=545), [0:09:49](https://youtu.be/9F8DKZa1L2s?t=589) |
| Refers to herself as "Shishiro" | **Observed** (「シシロ」). | [0:03:26](https://youtu.be/9F8DKZa1L2s?t=206) |
| Calm through intense play | **Observed** in a 2026 racing game. | [0:15:00](https://youtu.be/MSPdwwejtXU?t=900) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "前回はですねペコちゃんが優勝しました" | [0:09:05](https://youtu.be/9F8DKZa1L2s?t=545) | "…とではい で前回はですねぺこちゃんが優勝しましためちゃ一番稼…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "あれから1年経ってるっていうのがすごいね" | [0:09:49](https://youtu.be/9F8DKZa1L2s?t=589) | "…経っ て いる って いう の が すごい ねちょっと さ…" | **Partial (computed):** shared run "るっていうのがすごいね"; only that part is quoted |


## Performance sheet: export/elevenlabs/Shishiro-Botan.md

# ElevenLabs v4 Performance Sheet: Shishiro Botan

> Built from `bible/characters/Shishiro-Botan.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Botan is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear, cool-toned but cheerful voice; relaxed and amused in play, brisk and orderly when presenting, with an easy, frequent laugh."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **55%** (API `0.55`) (relaxed and steady; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[relaxed, cheerful]` or `[brisk, organized]`; v4 has no speed slider.

## 3. Write these habits into the script
- "La-lion♪" to open; "Well then, cya~" to close.
- Brisk, organized presenting as a game master: 「前回はですねペコちゃんが優勝しました」 ("last time, Peko-chan won").
- An offhand "Poi!" as she lobs a grenade.
- Calm and amused in horror; teases scared friends instead of panicking.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[breezy]` | "La-lion♪" (official) |
| Presenting a project | `[brisk, organized]` | 「前回はですねペコちゃんが優勝しました」 ("Zenkai wa desu ne, Peko-chan ga yūshō shimashita") |
| FPS play | `[calm, focused]` | **Style demo:** "Hidari, hitori kezutta." ("Left, one's weakened.") |
| Throwing a grenade | `[offhand]` | "Poi!" (secondary transcription) |
| Teasing Lamy in horror | `[amused, teasing]` | **Style demo:** "Daijōbu daijōbu, mada nani mo dete nai yo." ("It's fine, it's fine, nothing's even come out yet.") |
| Closing | `[easy]` | "Well then, cya~" (official English) |

With people (proposed scene directions, not observed conversational defaults): Lamy `[teasing, protective]`; Ina `[warm]`.

## 5. Signature sounds
- "Poi!" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ししろ ぼたん; ししろん; ぽいっ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff, deep "tough girl" voice; a sleepy drawl; panic in horror.

## 8. Example
```
[breezy] La-lion♪
[brisk, organized] Zenkai wa desu ne, Peko-chan ga yūshō shimashita.
[offhand] Poi!
[amused, teasing] Daijōbu daijōbu, mada nani mo dete nai yo.
```
(Line 1 is her official greeting; line 2 is her line, quoted only where both transcripts agree; line 3 is her
grenade call as a secondary transcription; line 4 is a style demo.)


## Card 2: Kikirara Vivi (draft, full file)

---
kind: character
name: "Kikirara Vivi"
sw_section: Characters
---

# Character File: Kikirara Vivi

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Vivi is an active hololive member
> (hololive DEV_IS, FLOW GLOW) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02). Her
> recent streams (2026) set her default manner, per the project's recency rule. Nothing about the performer behind
> the avatar: private-life information (family, home, health, daily routine, sleep, outings, where she streams
> from and the like) is outside scope and is not recorded here, including what she mentions in chats and stream
> titles. She streams in Japanese; her dialect is recorded as a voice feature only. In stories she knows she is a
> streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; VI20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (VI#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (VI20: a July 2026 late-night "call
> from Vivi" chat and a May 2026 Super Mario World stream; see research/audio-check/vivi.md). Personal remarks are
> not quoted or summarized here. The audio was machine-transcribed and acoustically measured; transcripts were
> reviewed in context, without independent listening verification.

## One-line Concept
"Hol'up, 'cus you're in for a transformation!": FLOW GLOW's makeup artist, a pink-and-purple-twintailed seeker of
"true beauty" who wears her feelings on her face, lets frank, dialect-flavored retorts slip out, hides from
sunlight, screams through horror games, and delivers her signature "Ōi!" deadpan on purpose. [Official VI1]
[ASR VI20]

## Core Drive
- **Want:** stated goals: a cosmetics collaboration, live concerts where she can sing her own songs and feel her
  fans' voices, and to be "a source of smiles for everyone." [Observed VI2 §Likes and dislikes, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** sunlight (her "natural enemy"), bugs and Japanese horror are listed dislikes;
  she plays horror games anyway and screams. [Official VI1] [Observed VI2, secondary; VI4 titles]
- **Values shown in public:** her fans (the Vivids); streaming steadily; beauty and cute things. [ASR VI20]
  [Observed VI2]

## Core Contradiction
A glamorous makeup artist and self-described game beginner who plays her first-ever Mario games on stream and
gets lost in HoloCure, horror and Minecraft farming, where she calls herself a "legendary farmwife." [Official
VI1] [Observed VI2 §Miscellaneous, secondary; VI4 titles]

## Behavioral Traits
1. Opens with a long, rising "Nnnnnn~ Vivi!!!" (ん～～ッヴィヴィ～～～!!!). [Observed VI2 caption, secondary; VI4
   fe4gPaYmzOw title]
2. Plays her tsukkomi flat on purpose: she explained on stream that when she retorts "Ōi!" she deliberately strips
   the emotion out, then did an "emotional version" to prove it. [ASR VI20]
3. Jokes that affection costs extra: "お金取るで" ("I'll charge you for that") when chat asks her to say something
   sweet, and saves her "words of love" for special days. [ASR VI20]
4. Close to Usada Pekora ("PekoVivi"): Pekora gifted her games (Heavy Rain, Getting Over It) and saved her items
   in Minecraft, after which Vivi called her the "legendary hero." [Observed VI2 §Miscellaneous, secondary; VI4
   titles]
5. Frequent "vertical" (portrait-format) karaoke streams; subscriber milestones reached during endurance karaoke.
   [VI4 titles] [Observed VI2 §2025, §2026, secondary]
6. Late-night themed streams such as a "call from Vivi," spoken close to the mic. [VI4 zEmPFayNEFo] [ASR VI20]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: "Hol'up, 'cus you're in for a transformation!" [Official VI1]
  - Opening: "Nnnnnn~ Vivi!!!" [Observed VI2 caption, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Ōi!" → her flat tsukkomi, constant. [ASR VI20]
  - "お金取るで" (okane toru de, "I'll charge you for that") → when chat asks for fan service. [ASR VI20]
  - "Vivid" → her fans. [Observed VI2 §Mascot and fans, secondary]
- **Vocabulary / fillers:** Kansai-flavored endings ("~yan," "~nen," "akan," "honma," "~hen"); see
  research/audio-check/vivi.md. [ASR VI20] [Official VI1 "dialect"]
- **Profanity:** frank rather than crude. [Official VI1]
- **Language:** streams in Japanese with a Kansai-style dialect (a voice feature only); with the English cast she
  played R.E.P.O. with FUWAMOCO, Bae and Ina and Gartic Phone with Kronii and Elizabeth (2025). [VI5]
- **Laughs, noises:** quick laughs; screams in horror. [VI4 titles] [ASR VI20]
- **Rhythm & rhetoric:** chatty, quick back-and-forth with chat, a punchline, then a deadpan "Ōi." [ASR VI20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (VI20): in a close-mic 2026 late-night chat, median about 275 Hz (p10–p90 about 222–406 Hz, 10
    semitones) and about 257 characters a minute of speech; see research/audio-check/vivi.md. Measurements describe
    the archived audio, not a target to clone.
  - Provisional (interpretation): a bright, slightly husky, girlish voice with a Kansai lilt; lively and frank,
    dropping to a flat deadpan for retorts.
- **Sounds off:** standard-Tokyo primness; a slow, breathy whisper as her default; a cold, aloof beauty.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Rising, theatrical | "Nnnnnn~ Vivi!!!" (VI2) |
| Retort | Deliberately flat | "Ōi!" (ASR VI20) |
| Chat asks for something sweet | Teasing, coy | "お金取るで" (okane toru de, "I'll charge you for that") (ASR VI20) |
| Horror | Screaming | [screams] |
| Thanking her fans | Warm, sincere | **Style demo:** "Minna ga oran to Vivi ganbararehen." ("I can't do my best without you all.") |

### Sample Lines
1. "Hol'up, 'cus you're in for a transformation!" (Official VI1)
2. "お金取るで" (okane toru de, "I'll charge you for that") (ASR VI20, July 2026)

## Appearance Anchors (avatar)
- 161 cm; illustrator nonco. Long twin tails in pink fading to purple, an ahoge, black bows with a sparkle
  pattern, blue eyes. A cream off-shoulder top with oversized purple sleeves over a black crop top; a black
  quilted heart-shaped bag stuffed with makeup brushes at her hip; baggy purple cargo pants, one leg pulled up over
  patterned brown tights; black lace-up boots with pink laces. Emoji 💅✨. [Official VI1 key art, described by
  Claude] [Observed VI2 infobox, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2024-11-09 | Debut with FLOW GLOW (hololive DEV_IS); first cover "Luna say maybe" | [Official VI1] [Observed VI2] |
| 2025 | FLOW GLOW songs "24K GOLD" (03-14), "LOAD" (07-09), "good enough" (09-20); 500,000 subscribers (11-30) | [Observed VI2] |
| 2025-04-14 | Gartic Phone EN + ID + JP collab with Mumei, Kronii, Ina, Elizabeth and Noel | [VI5 OMDzBQohAf8] |
| 2025-05-25 | #holoREPO with FUWAMOCO, Bae and others | [VI5] |
| 2025-07 | Games with Pekora (The Forest, Fast Food Simulator); a stream ahead of "PekoMari" | [VI4] |
| 2026 | First Super Mario Bros. 3 and Super Mario World playthroughs; 700,000 subscribers (08-11); FLOW GLOW's "magic summer" (08-18) | [VI4] [Observed VI2] |
| 2026-08-27 | First original song, "Vivid Cute" | [Observed VI2] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Usada Pekora | "PekoVivi"; the "legendary hero" | Gifted games, co-op games, Minecraft rescue | [VI2] [VI4] |
| Houshou Marine | "MVP" with Pekora | The trio unit | [VI2] |
| Shirogane Noel | — | Gartic Phone (2025) | [VI5] |
| FLOW GLOW (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya) | Unitmates | Group songs; a cover with Chihaya ("Bridal Dream," 2025) | [VI2] [VI4] |
| FUWAMOCO | — | Watched FLOW GLOW's debut (2024); #holoREPO (2025) | [VI5] |
| Hakos Baelz | — | #holoREPO (2025) | [VI5] |
| Ninomae Ina'nis | — | R.E.P.O. (2025-06-02); Gartic Phone (2025) | [VI5] |
| Ouro Kronii, Elizabeth Rose Bloodflame | — | Gartic Phone EN + ID + JP (2025) | [VI5] |
| Nanashi Mumei (graduated) | — | Hosted that Gartic Phone collab (2025) | [VI5] |
| Koseki Bijou | — | Watched FLOW GLOW's debut with FUWAMOCO (2024) | [VI5] |

## Arc
- **Starting point:** active at the 2026 baseline, almost two years in: 700,000 subscribers, her first original
  song out, FLOW GLOW's seventh song released.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a makeover nobody asked for; a horror game she insists on finishing; a deadpan "Ōi" that
  lands too hard.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Vivi does FUWAMOCO's stage makeup and charges them "Vivi prices."
  2. Pekora "rescues" Vivi again in a game, and Vivi insists on paying her back with a makeover.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2024-11-09; hololive DEV_IS, FLOW GLOW (makeup artist); birthday 27 August; 161 cm; illustrator nonco;
  fans Vivid; emoji 💅✨.

## Sources (checked 2026-10-02)
- VI1 Official profile: https://hololive.hololivepro.com/en/talents/kikirara-vivi/ (text and key art)
- VI2 Kikirara Vivi wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Kikirara_Vivi
- VI4 Stream archive metadata, her channel (archive.ragtag.moe): zEmPFayNEFo ("call from Vivi," 2026-07-27),
  p10HUmvmrfc (Super Mario World, 2026-05-13), fe4gPaYmzOw, Lz56n8fa25o, c6FTIC_vzBQ, lqidVnpl3_0, FWCkuwroMIw,
  bvEK8QBvhFo (Pekora and MVP), NGeumGspO2g and B3-3agJD9d8 (with Chihaya), m4svh5HJjLk
- VI5 Other members' archive metadata: gAj77STI2oc, Z5cpzbdsLDE (FUWAMOCO), TgMVtjXW2Ms (Bae), grBU9Dl09Ds (Ina),
  OMDzBQohAf8 (Mumei)
- VI20 Claude's audio check (two-model ASR, Japanese): research/audio-check/vivi.md

---

## [SW] Name
Kikirara Vivi

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive DEV_IS, FLOW GLOW, MVP, PekoVivi

## [SW] Other Names
Vivi

## [SW] Personality
Vivi is FLOW GLOW's makeup artist, a seeker of "true beauty" always hunting the next item for an extra glow-up. She does not hide her feelings: they show on her face, and frank, dialect-flavored remarks slip out. Her natural enemy is direct sunlight; she is happily an indoor person. On stream she is chatty, funny and quick with chat, with a signature flat "Ōi!" retort that she explains she delivers deadpan on purpose; when chat asks for something sweet she jokes "I'll charge you for that" and saves her words of love for special days. A self-described game beginner, she gets hooked on HoloCure and Minecraft farming ("legendary farmwife"), plays her first Mario games, and screams through horror games she will not quit. She adores cute things and her fans, the Vivids, and calls her senpai Usada Pekora the "legendary hero."

## [SW] Background
Vivi is an active member of FLOW GLOW (hololive DEV_IS). She has no supernatural abilities; her lore is a performed persona. She debuted on 2024-11-09 as a member of FLOW GLOW, the second unit of hololive DEV_IS, with Isaki Riona, Koganei Niko, Mizumiya Su and Rindo Chihaya. FLOW GLOW has released seven original songs, including "24K GOLD," "LOAD" and "magic summer" (2026); Vivi passed 700,000 subscribers in August 2026, often during endurance karaoke, and released her first solo original song, "Vivid Cute," on her birthday in 2026. She grew close to Usada Pekora (the "PekoVivi" pair) and is in the unit "MVP" with Pekora and Houshou Marine. With the English cast she played R.E.P.O. with FUWAMOCO, Bae and Ina and Gartic Phone with Mumei, Kronii, Ina and Elizabeth (2025); FUWAMOCO and Bijou watched FLOW GLOW's debut together.

## [SW] Physical Description
Vivi's avatar is 161 cm tall, with long twin tails that fade from pink to purple, black sparkle-patterned bows and blue eyes. She wears a cream off-shoulder top with oversized purple sleeves over a black crop top, baggy purple cargo pants with one leg pulled up over patterned tights, black lace-up boots with pink laces, and a quilted black heart-shaped bag full of makeup brushes at her hip.

## [SW] Dialogue Style
Streams in Japanese with regional dialect endings ("~yan," "~nen," "akan," "honma"): frank, quick and funny, bantering with chat, then a flat, deliberately emotionless "Ōi!" as her retort. She teases ("I'll charge you for that") and turns sincere when thanking her fans. When a story renders her speech in English or Chinese, keep a casual regional flavor without caricature, the frankness and the deadpan "Ōi."

## [SW] Catchphrases
"Hol'up, 'cus you're in for a transformation!" (official); "Nnnnnn~ Vivi!!!" (her opening); "Ōi!" (her deadpan retort); "okane toru de" ("I'll charge you for that"); "Vivid" (her fans).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a bright, slightly husky, girlish voice; lively, frank and fast in banter; deliberately flat for her "Ōi!" retort; loud screams in horror; warm and sincere with her fans. Never prim, slow and breathy by default, or coolly aloof.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, slightly husky girlish voice. Default tags: [lively, frank]. By situation: opening [theatrical, rising]; retort [deadpan]; teasing chat [playful, coy]; horror [screams]; first-time gaming [flustered]; thanking fans [warm, sincere]. With people (proposed scene directions, not observed conversational defaults): Pekora [adoring, excited]; Marine [playful]; FUWAMOCO [cheerful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Ōi!" (spoken, deadpan); [laughs] (tag only). Keep in the words: "Ōi," "okane toru de," "Vivid." Reading guide (untested): ききらら ゔぃゔぃ. Not as default: prim standard speech or a breathy whisper.

## [SW] Motivation
In her lore, Vivi wants to find true beauty and give everyone a glow-up. As a streamer and singer she wants a cosmetics collaboration, live concerts with her own songs, and to be a source of smiles for her fans.

## [SW] Relationships
Usada Pekora: "PekoVivi"; gifted her games, played co-op with her and saved her in Minecraft, so Vivi calls her the "legendary hero." Houshou Marine: the unit "MVP" with Pekora. Shirogane Noel: Gartic Phone (2025). FLOW GLOW (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya): her unit; a cover with Chihaya (2025). FUWAMOCO: watched FLOW GLOW's debut (2024); #holoREPO (2025). Hakos Baelz: #holoREPO (2025). Ninomae Ina'nis: R.E.P.O. and Gartic Phone (2025). Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone (2025). Nanashi Mumei (graduated): hosted that Gartic Phone collab. Koseki Bijou: watched FLOW GLOW's debut with FUWAMOCO.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Kikirara Vivi): official profile and
  key art (VI1), wiki (VI2, by section), archive metadata (VI4, VI5) and Claude's two-model Japanese audio check
  (VI20, research/audio-check/vivi.md).

## Open Questions
1. The wiki gives no appearance section; the avatar description is Claude's reading of the official key art.
   Confirm against a costume reveal if one is found.
2. "MVP" (Marine, Vivi, Pekora) is wiki-listed; no MVP-titled stream was found in the archive metadata read here.


## Audio report: research/audio-check/vivi.md

# Audio check — Kikirara Vivi (2026-10-02)

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
| mario20_2026 | [【 スーパーマリオワールド 】真最終回！完全初見！初めてのマリオワールドに挑戦！【#綺々羅々ヴィ](https://youtu.be/p10HUmvmrfc) | [0:10:00–0:30:00](https://youtu.be/p10HUmvmrfc?t=600) | 11.6 | 1873 | 162.0 | 351 Hz | 158–509 Hz |
| call20_2026 | [ヴィヴィから着信📞Vivi Ch. 綺々羅々ヴィヴィ - FLOW GLOW がライブ配信中！](https://youtu.be/zEmPFayNEFo) | [0:05:00–0:25:00](https://youtu.be/zEmPFayNEFo?t=300) | 14.0 | 3592 | 257.1 | 275 Hz | 222–406 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | mario20_2026 | call20_2026 |
|---|---|---|
| first person 余 (yo) | 1 | 0 |
| first person 僕 (boku) | 0 | 2 |
| なんか | 3 | 18 |
| まあ | 3 | 0 |
| ちょっと待って | 1 | 1 |
| やばい | 1 | 0 |
| かわいい | 0 | 1 |
| えっ/え? | 2 | 1 |
| ありがとう | 1 | 6 |
| English (Latin letters) | 1 | 3 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Third-person "Vivi" | **Observed** constantly (dozens of times in the late-night window). | [0:06:25](https://youtu.be/zEmPFayNEFo?t=385) |
| Deadpan "Ōi!" on purpose | **Observed**: she explains that when she retorts "ōi" she deliberately strips the emotion out, then performs an "emotional version." The models disagree on the exact words, so the explanation is paraphrased. | [0:18:22](https://youtu.be/zEmPFayNEFo?t=1102), [0:19:13](https://youtu.be/zEmPFayNEFo?t=1153) |
| "I'll charge you for that" joke | **Observed**: 「お金取るで」 when chat asks for something sweet (second model writes 「とる」; same reading). | [0:07:04](https://youtu.be/zEmPFayNEFo?t=424) |
| Kansai-style speech | **Observed**: "~yan," "~nen," "akan," "honma," "~hen" throughout. | [0:05:00](https://youtu.be/zEmPFayNEFo?t=300) |
| A game beginner on Mario | **Observed** in her 2026 Super Mario World finale. | [0:10:20](https://youtu.be/p10HUmvmrfc?t=620) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "お金取るで" | [0:07:04](https://youtu.be/zEmPFayNEFo?t=424) | "…いもちもちはお金とるでもちも…" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "誰がぼう読みや" | [0:18:06](https://youtu.be/zEmPFayNEFo?t=1086) | "…ーえ?暴読?誰が暴読や誰が暴…" | **Not confirmed** by the second model; not quoted |
| "感情抜いてます" | [0:18:22](https://youtu.be/zEmPFayNEFo?t=1102) | "…とさあ感情を抜いてますこれわかる?…" | **Partial (computed):** shared run "抜いてます"; only that part is quoted |


## Performance sheet: export/elevenlabs/Kikirara-Vivi.md

# ElevenLabs v4 Performance Sheet: Kikirara Vivi

> Built from `bible/characters/Kikirara-Vivi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Vivi is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, slightly husky, girlish voice; lively, frank and fast in banter, deliberately flat for a deadpan retort, loud screams in horror, warm and sincere with her fans."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (lively, with deliberate flat turns; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[lively, frank]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- Opens with a rising "Nnnnnn~ Vivi!!!"; calls her fans "Vivid."
- Retorts with a deliberately flat, emotionless "Ōi!"
- Teases that affection costs extra: 「お金取るで」 ("I'll charge you for that").
- Regional dialect endings live in the words ("-de," "-hen," "honma"); no accent is assigned to the voice itself.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[theatrical, rising]` | "Nnnnnn~ Vivi!!!" (secondary transcription) |
| Retort | `[deadpan]` | "Ōi!" |
| Chat asks for something sweet | `[playful, coy]` | 「お金取るで」 ("Okane toru de," "I'll charge you for that") |
| Horror | `[screams]` | (tag only) |
| Thanking her fans | `[warm, sincere]` | **Style demo:** "Minna ga oran to Vivi ganbararehen." ("I can't do my best without you all.") |

With people (proposed scene directions, not observed conversational defaults): Pekora `[adoring, excited]`; Marine `[playful]`; FUWAMOCO `[cheerful]`.

## 5. Signature sounds
- "Ōi!" (spoken, deadpan)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ききらら ゔぃゔぃ; おーい. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Prim standard speech, a breathy whisper by default, or a coolly aloof read.

## 8. Example
```
[theatrical, rising] Nnnnnn~ Vivi!!!
[deadpan] Ōi!
[playful, coy] Okane toru de.
[warm, sincere] Minna ga oran to Vivi ganbararehen.
```
(Line 1 is her opening as a secondary transcription; lines 2–3 are her lines from the sampled audio (line 3
quoted only where both transcripts agree); line 4 is a style demo.)


## World card 3: JP Senpai Pairs 2 (draft, full file)

---
kind: world
name: "JP Senpai Pairs 2"
sw_section: Worldbuilding
---

# World Element: JP Senpai Pairs 2 (Marine, Noel, Lamy, Botan, Vivi with the cast)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-02. Evidence labels as in the other world files. "Archive" = stream titles and
> descriptions on the members' channels (archive.ragtag.moe, S1); a title shows that a collab happened, not how
> close the members are. Houshou Marine, Shirogane Noel, Yukihana Lamy, Shishiro Botan and Kikirara Vivi are
> active hololive members at the 2026-09-30 baseline; they were added to the cast by author order (2026-10-02).
> They stream mostly in Japanese; with the English cast they meet as senpai. Gura (graduated 2025-05-01) and Mumei
> (2025-04-27, 04-28 JST) appear only as memories; Ame is an affiliate. Secret Society holoX's ties are on the
> world card "holoX"; the first four JP senpai (Suisei, AZKi, Ayame, Okayu) are on "JP Senpai Pairs."

## One-line Concept
More senpai the English cast meets: Marine, the pirate captain who was Kiara's first HOLOTALK guest and hosts
EN kouhai off-collabs; Noel, the knight on Calli's HOLOYOI; Lamy, the snow elf of Ina's Minecraft festivals;
Botan, the lion who runs server events and played Overwatch with IRyS; and Vivi, the DEV_IS kouhai who joined
FUWAMOCO and Bae in R.E.P.O.

## Type
Relationship web (five Japanese members with the cast and with each other).

## Houshou Marine with the cast
- **Takanashi Kiara:** Marine was the first guest of Kiara's HOLOTALK (2020-11-20, "#marinarasauce"); Kiara
  danced "MIRAGE" with her (2024) and to Marine and Kobo's "III." [S1]
- **Mori Calliope:** Calli's HOLO ENGLISH LESSON #01 with Ina and Fubuki (2022-02-19); Mario Kart with Bae and
  Pavolia Reine (2021-12-25); an off-collab "House Party with Marine & Bae" (2023-08-14); Calli played Marine's
  horror game "Truth of Beauty Witch" (2023); dance shorts to Marine's songs. [S1]
- **Hakos Baelz, Nanashi Mumei (graduated):** Bae and Mumei played Marine's horror game together (2023-08-23);
  Bae was at Calli's house party with Marine; dance covers. [S1]
- **FUWAMOCO, Nerissa Ravencroft:** a Touhou off-collab with FUWAMOCO (2024-04-30); a Mario Party Superstars
  off-collab with Nerissa and FUWAMOCO (2024-06-17); FUWAMOCO's watch-along of Marine's solo concert (2024-12-07)
  and a "Chatter Chatter" dance short (2026); Nerissa danced to "I'm Your Treasure Box." [S1]
- **Ninomae Ina'nis, Gawr Gura:** UMISEA, the ocean unit; Calli's English lesson #01 (Ina); "SHINKIRO" with Gura
  ("GuraMarine," on Marine's album). [S2 Marine §Relationships, secondary] [Official album page]
- **Elizabeth Rose Bloodflame:** "IT'S LOVE" with Marine and Inugami Korone for Elizabeth's 2026 birthday. [S1]

## Shirogane Noel with the cast
- **Takanashi Kiara:** HOLOTALK's 22nd guest (2022-03-05). [S1]
- **Mori Calliope:** HOLOYOI #02 with Shiranui Flare (2023-04-20). [S1]
- **FUWAMOCO, Hakos Baelz:** a "Yuru Holo" team Mario Kart event (2023-12-12); FUWAMOCO danced to Noel's
  "Très Bien Night" (2025). [S1]
- **Nanashi Mumei, Ina, Kronii, Elizabeth (and Kikirara Vivi):** Mumei's Gartic Phone EN + ID + JP collab
  (2025-04-14). [S1]

## Yukihana Lamy with the cast
- **Ninomae Ina'nis:** Ina's Minecraft "Usaken Summer Festival" with Lamy (2021-06-27) and an EN-server "date"
  (2021-10-20); Lamy appeared at Ina's 3D live "Pleides" (2024-12-28). [S1]

## Shishiro Botan with the cast
- **IRyS:** Left 4 Dead 2 (2022-04-24); an Overwatch 2 team for Holizontal JAM with Lui, Chloe and Towa (2023-08).
  [S1]
- **Mori Calliope, Hakos Baelz:** HOLOYOI #03 (alcohol-free edition) and BAE-GEMITE DOMINATION #2, both with
  Oozora Subaru (2023). [S1]
- **Ninomae Ina'nis:** a guest at Ina's birthday 3D live "EVERMORE" (2025-05-21). [S1]
- **Takanashi Kiara, Gawr Gura:** "Usada Kensetsu" (Kiara) and "Apex Predators" (Gura) are wiki-listed unit
  names. [S2 Botan, secondary]

## Kikirara Vivi with the cast
- **FUWAMOCO, Koseki Bijou:** watched FLOW GLOW's debut together (2024-11-08). [S1]
- **FUWAMOCO, Hakos Baelz:** #holoREPO with Roboco, Towa and Hajime (2025-05-25). [S1]
- **Ninomae Ina'nis:** R.E.P.O. with Polka, Watame, Flare and Anya (2025-06-02). [S1]
- **Mumei, Kronii, Ina, Elizabeth:** Mumei's Gartic Phone EN + ID + JP collab (2025-04-14). [S1]

## Among themselves (and with the first JP senpai)
- Marine and Noel: hololive Fantasy and "Onee-san Gumi" with Shiranui Flare; with Lamy and Inugami Korone,
  "Yakamashi Musume." Marine, Noel, Lamy, Hakui Koyori and Sakura Miko sang in the music project "Blue Journey"
  (2023). [S2]
- Lamy and Botan: NePoLaBo with Omaru Polka and Momosuzu Nene; horror "dates." [S2]
- Marine and Vivi: "MVP" with Usada Pekora (wiki-listed). [S2]
- Marine and Lamy: "Magical Girl holoWitches!" (Lamy joined in 2025). [S2]
- With the first four: Marine and Suisei sang "Chatter Chatter" (2026) and share holoALICE and MOMAS; Marine and
  Okayu share HoLOGSS and MOMAS; Noel and Suisei are in "Shiranui Kensetsu"; Noel and Ayame did an earphone
  sponsorship collab (2025); Lamy and AZKi are in KALAZ (with Amane Kanata) and KoZMy (with Koyori). [S2] [S1]

## History
| Date | Event | Who |
|---|---|---|
| 2020-11-20 | Marine is HOLOTALK's first guest | Marine, Kiara |
| 2021 | Ina's Minecraft festival and EN-server "date" | Lamy, Ina |
| 2022 | Calli's English lesson #01; HOLOTALK #22; Left 4 Dead 2 | Marine; Noel; Botan, IRyS |
| 2023 | HOLOYOI #02 and #03; BAE-GEMITE DOMINATION #2; Marine's horror game; Overwatch 2 team; Blue Journey | Noel, Botan, Calli, Bae; Marine, Mumei; Botan, IRyS |
| 2024 | Off-collabs with FUWAMOCO and Nerissa; Ina's "Pleides" | Marine; Lamy |
| 2025 | Gartic Phone EN + ID + JP; #holoREPO; Ina's "EVERMORE" | Noel, Vivi; Vivi, Bae, FUWAMOCO; Botan |
| 2026 | "Chatter Chatter"; Elizabeth's birthday cover | Marine, Suisei; Marine |

## Sensory Palette
- See: crimson twintails under a gold-trimmed pirate hat; silver hair and black armor with a mace; light-blue hair
  and a snow-flower beret; silver lion ears over a striped black top; pink-to-purple twin tails and a makeup-brush
  bag.
- Hear (proposed scene direction, not audio observations): a captain's "Ahoy!", a knight's muscle pun, a toast
  before a chat, a calm "Poi!" over gunfire, a deadpan "Ōi!"

## Glossary
- HOLOTALK: Kiara's translated talk show (Marine #1, Noel #22).
- HOLOYOI: Calli's talk series (Noel with Flare #02; Botan with Subaru #03).
- UMISEA: Marine's ocean unit with Ina, Gura and Minato Aqua.
- NePoLaBo: Lamy and Botan's 5th-generation group with Polka and Nene.
- MVP: Marine, Vivi and Pekora (wiki-listed).

## Conflicts and Story Hooks
1. Marine invites FUWAMOCO onto her "ship"; Noel insists on guarding the deck.
2. Botan runs a server event for the EN cast; Lamy hosts the after-party toast.
3. Vivi does stage makeup for Bae before a R.E.P.O. rematch.

## Links to Characters
Houshou Marine; Shirogane Noel; Yukihana Lamy; Shishiro Botan; Kikirara Vivi; Takanashi Kiara; Mori Calliope;
Ninomae Ina'nis; Hakos Baelz; IRyS; FUWAMOCO; Nerissa Ravencroft; Elizabeth Rose Bloodflame.

## Secrets
(none)

## Hard Facts (continuity)
- Marine: HOLOTALK guest #1 (2020-11-20). Noel: HOLOTALK guest #22 (2022-03-05).
- Calli's HOLOYOI: #02 Noel and Flare (2023-04-20); #03 Subaru and Botan (2023-05-18).

## Sources (checked 2026-10-02)
- S1 Stream archive metadata (archive.ragtag.moe), the members' and the EN cast's channels; IDs on the member
  files (e.g. 3HwaqbdKO1s HOLOTALK #1, toe_PmrDWBU HOLOTALK #22, bfUEbp3xk4o English lesson #01, wyrLR1CC1Co and
  EatMZc1N3VM HOLOYOI, -0_9xCPljh0 BAE-GEMITE, DY5VThfehW8 house party, RY1GkF4jMls Marine's horror game,
  x7gRHgQ0yI0 and FLL7e1-RPGo off-collabs, iwnHChZq0N8 "IT'S LOVE", a7CvRf4vFYc and Isp3UhgOAB4 (Ina and Lamy),
  K1wStJxm4F0 and roWKpgZsjR4 (IRyS and Botan), I-J11Da5ONY (Ina's EVERMORE), gAj77STI2oc, Z5cpzbdsLDE,
  TgMVtjXW2Ms, grBU9Dl09Ds, OMDzBQohAf8 (Vivi))
- S2 Member wiki pages (secondary), by section, via the fandom API: Houshou Marine, Shirogane Noel, Yukihana Lamy,
  Shishiro Botan, Kikirara Vivi
- Character files in this project: the five members above and the EN cast

---

## [SW] Name
JP Senpai Pairs 2

## [SW] Role
Relationship

## [SW] Other Names
HOLOTALK, HOLOYOI, UMISEA, MVP, NePoLaBo, Yakamashi Musume, Onee-san Gumi, Marine and Kiara, Lamy and Ina, Botan and IRyS, Vivi and FUWAMOCO

## [SW] Description
The ties of five more hololive senpai, Houshou Marine, Shirogane Noel, Yukihana Lamy, Shishiro Botan and Kikirara Vivi, with the English cast and with each other. Marine was the first guest of Kiara's talk show HOLOTALK (2020), joined Calli's first English lesson with Ina (2022), played Mario Kart and threw a house-party off-collab with Calli and Bae, inspired a horror game that Calli, Bae and Mumei played (2023), hosted off-collabs with FUWAMOCO and Nerissa (2024), and is in the ocean unit UMISEA with Ina and Gura. Noel was HOLOTALK's 22nd guest and was on Calli's HOLOYOI with Shiranui Flare (2023). Lamy joined Ina's Minecraft festivals (2021) and her 3D live (2024). Botan played Left 4 Dead 2 and Overwatch 2 with IRyS, was on HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and guested at Ina's 2025 birthday live. Vivi, from the newer DEV_IS unit FLOW GLOW, played R.E.P.O. with FUWAMOCO, Bae and Ina and Gartic Phone with Mumei, Kronii and Elizabeth (2025). Among themselves: Marine and Noel are hololive Fantasy; Marine, Noel and Lamy are "Yakamashi Musume" with Inugami Korone; Lamy and Botan are NePoLaBo; Marine, Vivi and Pekora are "MVP."

## [SW] Rules
These entries record public collaborations and senpai–kouhai ties. The five stream mostly in Japanese; the English cast addresses them as "senpai," and conversations mix Japanese and English. Gura and Mumei appear only as memories; Ame is an affiliate. A collab title shows that a collab happened, not how close two members are.

## [SW] Sensory Details
Crimson twintails under a gold-trimmed pirate hat; silver hair over black knight's armor; light-blue hair under a snow-flower beret; silver lion ears over a striped black top; pink-to-purple twin tails and a bag of makeup brushes. Proposed scene direction: a captain's "Ahoy!", a muscle pun, a toast before a chat, a calm "Poi!" over gunfire, a deadpan "Ōi!"

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Marine, Noel, Lamy, Botan and Kikirara
  Vivi): archive metadata (EN and JP channels), member wiki pages (secondary) and the five new character files.

## Open Questions
1. Lamy's EN ties in the archive are all with Ina; keep her section short?


## Lines about Marine, Noel, Lamy, Botan and Vivi on the other cast cards (2026-10-02; part promoted ahead of this review, all confirmed by it)

### Mori Calliope
Relationships field (exported):
Marine, Noel, Botan, AZKi and holoX (La+, Lui, Chloe, Iroha): her English-lesson and HOLOYOI guests (2022–2023).

Dossier rows (with sources):
| Houshou Marine, Shirogane Noel, Shishiro Botan | JP seniors | HOLO ENGLISH LESSON #01 with Marine, Ina and Fubuki (2022-02-19); Mario Kart with Marine, Bae and Reine (2021-12-25); a house-party off-collab with Marine and Bae and a playthrough of Marine's horror game (2023-08-14); HOLOYOI #02 with Noel and Flare (2023-04-20) and #03 with Botan and Subaru (2023-05-18) | [S1 bfUEbp3xk4o, Tpzbfccp_ZM, DY5VThfehW8, Mf-sAjsuSig, wyrLR1CC1Co, EatMZc1N3VM] |

### Takanashi Kiara
Relationships field (exported):
Archived episode records list HOLOTALK guests including Houshou Marine (#1), Hoshimachi Suisei ("cometori"), AZKi, Shirogane Noel, Nekomata Okayu and Nakiri Ayame. holoX: La+ Darknesss ("Glow in the Dark") and Sakamata Chloe ("WILDCARD").

Dossier rows (with sources):
| Houshou Marine, Oozora Subaru | JP seniors | Early HOLOTALK guest (Marine); first EN×JP collab (Subaru, 2020) | [Observed T2 §2020, secondary] |
| Houshou Marine, Shirogane Noel | JP seniors | HOLOTALK's first guest Marine ("#marinarasauce," 2020-11-20) and 22nd guest Noel (2022-03-05); a "MIRAGE" dance short with Marine (2024) | [S1 3HwaqbdKO1s, toe_PmrDWBU, tzVgzvV0cVo] |

### Ninomae Inanis
Relationships field (exported):
Houshou Marine: a senior artist she admires. Yukihana Lamy: Minecraft festivals and a server "date" (2021) and a "Pleides" guest (2024). Shishiro Botan: an "EVERMORE" guest (2025). Kikirara Vivi: R.E.P.O. (2025).
Dossier rows (with sources):
| Houshou Marine | JP senior | Admired artist-performer ("Marine-senpai") | [Observed—published interview I18] |
| Yukihana Lamy, Shishiro Botan, Kikirara Vivi, Shirogane Noel | JP members | Lamy: the Minecraft "Usaken Summer Festival" (2021-06-27), an EN-server "date" (2021-10-20) and a guest at "Pleides" (2024-12-28); Botan: a guest at "EVERMORE" (2025-05-21); Vivi: R.E.P.O. (2025-06-02); Noel and Vivi: Mumei's Gartic Phone (2025-04-14) | [S1 a7CvRf4vFYc, Isp3UhgOAB4, 3n9igJnSXtQ, I-J11Da5ONY, grBU9Dl09Ds, OMDzBQohAf8] |

### Gawr Gura
Relationships field (exported):
Houshou Marine: UMISEA and "SHINKIRO" ("GuraMarine"); Sakamata Chloe joined UMISEA later, per the wiki. Shishiro Botan: "Apex Predators," a secondary pair name.

Dossier rows (with sources):
| La+ Darknesss, Kazama Iroha, Shishiro Botan | JP members | HOLO ENGLISH LESSON #02 with La+ and Iroha (Calli's stream, 2022-03-04); "Apex Predators," a wiki-listed pair name with Botan | [S1 X492n37brRU] [Botan file, secondary] |
| Houshou Marine, Sakamata Chloe | UMISEA | "SHINKIRO" with Marine ("GuraMarine"); Chloe joined the unit later per the wiki | [Marine file MA2, MA5] [Chloe file CH2, secondary] |

### IRyS
Relationships field (exported):
Shishiro Botan, Takane Lui and Sakamata Chloe: an Overwatch 2 team (2023); Hakui Koyori: Splatoon 3 and Among Us.

Dossier rows (with sources):
| Shishiro Botan, Takane Lui, Sakamata Chloe, Hakui Koyori | JP members | Left 4 Dead 2 with Botan (2022-04-24); an Overwatch 2 team with Botan, Lui, Chloe and Towa (Holizontal JAM, 2023-08); Splatoon 3 (2022-10-03) and Among Us (2023-05-08) with Koyori and Chloe; Minecraft elytra hunting with Lui and Kronii (2022) | [S1 K1wStJxm4F0, roWKpgZsjR4, Xoma7oWsMcM, VwqdwQx5cog] |

### Nerissa Ravencroft
Relationships field (exported):
Houshou Marine: her other oshi.
Dossier rows (with sources):
| Fangirling (Kiara, Marine) | Fast, flustered, delighted | (no verified line; see Relationship Map) |
| Houshou Marine | JP senior and oshi |  off-collab with Marine and FUWAMOCO (2024) | [Observed N2; N3 title] |

### Ouro Kronii
Dossier rows (with sources):
| Takane Lui, Shirogane Noel, Kikirara Vivi | JP members | Minecraft elytra hunting with Lui, IRyS and Kaela (2022); Mumei's Gartic Phone EN + ID + JP with Noel and Vivi (2025-04-14) | [S1 OMDzBQohAf8; world card "holoX"] |

### Ceres Fauna
Relationships field (exported):
Shirogane Noel: a JP senior she admires.
Dossier rows (with sources):
| Shirogane Noel | JP senior | A member she admires and wanted to collab with | [Observed F2 §Trivia, secondary] |

### Nanashi Mumei
Relationships field (exported):
Shirogane Noel, Kikirara Vivi and Elizabeth Rose Bloodflame: her Gartic Phone EN + ID + JP collab (2025). Houshou Marine: Marine's horror game, played with Bae (2023).
Dossier rows (with sources):
| Sakamata Chloe, Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Chloe and Lui on Mumei's EN-server Minecraft tour with Bae (2022-02-12); Marine's horror game with Bae (2023-08-23); Noel and Vivi in Mumei's Gartic Phone EN + ID + JP (2025-04-14) | [S1 50tBPC5c2zM, RY1GkF4jMls, OMDzBQohAf8] |
| Houshou Marine | — | Played Marine's horror game with Bae (2023) | [Marine file MA5] |

### Koseki Bijou
Relationships field (exported):
Kikirara Vivi: Bijou watched FLOW GLOW's debut with FUWAMOCO (2024).
Dossier rows (with sources):
| Kikirara Vivi | DEV_IS kouhai | Bijou watched FLOW GLOW's debut with FUWAMOCO (2024-11-08) | [S1 gAj77STI2oc] |

### Fuwawa Abyssgard
Relationships field (exported):
Houshou Marine: her oshi (a Touhou off-collab). Shirogane Noel: a team Mario Kart event (2023). Kikirara Vivi: #holoREPO (2025).
Dossier rows (with sources):
| Houshou Marine | Her oshi | A Touhou off-collab (2024-04-30); Marine's solo concert watchalong (2024-12-07); a guest at their birthday concert (2025) | [Observed FW2; FW3] |
| Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Marine: a Touhou off-collab (2024-04-30), Mario Party with Nerissa (2024-06-17), a watch-along of her solo concert (2024-12-07), a "Chatter Chatter" dance short (2026); Noel: "Yuru Holo" team Mario Kart (2023-12-12) and a "Très Bien Night" dance short (2025); Vivi: FLOW GLOW's debut watch-along (2024) and #holoREPO (2025) | [S1 x7gRHgQ0yI0, FLL7e1-RPGo, zQdsLXE4ZQ8, PtaFGDOaj0k, Janl2FCKmsg, 8RjOCCH2sac, gAj77STI2oc, Z5cpzbdsLDE] |

### Mococo Abyssgard
Relationships field (exported):
Houshou Marine: a Touhou off-collab and Mario Party with Nerissa (2024). Kikirara Vivi: #holoREPO (2025). Shirogane Noel: a team Mario Kart event (2023).
Dossier rows (with sources):
| Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Marine: a Touhou off-collab (2024-04-30), Mario Party with Nerissa (2024-06-17), a watch-along of her solo concert (2024-12-07), a "Chatter Chatter" dance short (2026); Noel: "Yuru Holo" team Mario Kart (2023-12-12) and a "Très Bien Night" dance short (2025); Vivi: FLOW GLOW's debut watch-along (2024) and #holoREPO (2025) | [S1 x7gRHgQ0yI0, FLL7e1-RPGo, zQdsLXE4ZQ8, PtaFGDOaj0k, Janl2FCKmsg, 8RjOCCH2sac, gAj77STI2oc, Z5cpzbdsLDE] |
| Shirogane Noel | — | "Yuru Holo" team Mario Kart with Bae (2023) | [Noel file NO5] |

### Elizabeth Rose Bloodflame
Relationships field (exported):
Takanashi Kiara: calls her "Erby Berby." 2026 birthday-live guests: FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine and Korone. Shirogane Noel and Kikirara Vivi: Mumei's Gartic Phone EN + ID + JP collab (2025).
Dossier rows (with sources):
| Shirogane Noel, Kikirara Vivi | JP members | Mumei's Gartic Phone EN + ID + JP (2025-04-14) | [S1 OMDzBQohAf8] |
| Shirogane Noel, Kikirara Vivi | — | Gartic Phone EN + ID + JP (2025) | [Noel file NO5] [Vivi file VI5] |

### Hakos Baelz
Relationships field (exported):
Houshou Marine: Mario Kart, a house party and Marine's horror game. Kikirara Vivi: #holoREPO (2025). Shirogane Noel: a team Mario Kart event with FUWAMOCO (2023). Shishiro Botan: BAE-GEMITE DOMINATION #2 with Oozora Subaru (2023).
Dossier rows (with sources):
| Houshou Marine, Shirogane Noel, Shishiro Botan, Kikirara Vivi | JP members | Mario Kart with Marine, Calli and Reine (2021); Calli's house party with Marine (2023); Marine's horror game with Mumei (2023); BAE-GEMITE DOMINATION #2 with Botan and Subaru (2023-04-08); "Yuru Holo" team Mario Kart with Noel and FUWAMOCO (2023-12-12); #holoREPO with Vivi and FUWAMOCO (2025-05-25) | [HB3 X3pHIQAvpYU, RY1GkF4jMls, -0_9xCPljh0, Evg-T2BUIDM, TgMVtjXW2Ms] |
| Shirogane Noel, Shishiro Botan | — | "Yuru Holo" team Mario Kart with FUWAMOCO (Noel, 2023); BAE-GEMITE DOMINATION #2 with Oozora Subaru (Botan, 2023) | [Noel file NO5] [Botan file BO5] |

### Hoshimachi Suisei
Relationships field (exported):
Houshou Marine: "Chatter Chatter" (2026). Shirogane Noel: a fellow Shiranui Kensetsu member. La+ Darknesss, Nakiri Ayame and Shishiro Botan: holoGTA and poker (2024).

Dossier rows (with sources):
| Shiranui Flare, Omaru Polka, Miko, Shirogane Noel | "Shiranui Kensetsu" | Suisei is its PR director; R.E.P.O. "work shift" (2026) | [SU2] [SU4] |
| Houshou Marine | "Chatter Chatter" (2026); holoALICE, MOMAS | A duet with an original anime MV | [Marine file MA4] |
| Shirogane Noel | Shiranui Kensetsu | The Minecraft construction company with Flare, Polka and Miko | [Noel file NO2, secondary] |
| La+ Darknesss, Nakiri Ayame, Shishiro Botan | — | holoGTA and poker (2024) | [La+ file LA4] |

### AZKi
Relationships field (exported):
Hakui Koyori and Yukihana Lamy: "KoZMy" (2025), and a 3D karaoke with Koyori (2026); Lamy is also in "KALAZ" with Amane Kanata.
Dossier rows (with sources):
| Hakui Koyori, Yukihana Lamy | "KoZMy" | A trio formed in 2025; a 3D karaoke with Koyori (2026); Lamy is also in "KALAZ" with Amane Kanata | [Koyori file KO4] [Lamy file LM2] |

### Nakiri Ayame
Relationships field (exported):
Houshou Marine: a third-generation junior whom secondary accounts say Ayame admires. La+ Darknesss, Hoshimachi Suisei and Shishiro Botan: holoGTA and poker (2024). Shirogane Noel: an earphone collab (2025). (Pair and unit names other than official song credits come from secondary references.)

Dossier rows (with sources):
| Houshou Marine | a 3rd-generation junior she admires (secondary) | — | [AY2, secondary] |
| La+ Darknesss, Hoshimachi Suisei, Shishiro Botan | — | holoGTA and poker (2024) | [La+ file LA4] |
| Shirogane Noel | — | An Audio-Technica earphone collab (2025) | [Noel file NO4] |

### Nekomata Okayu
Relationships field (exported):
Houshou Marine: gave her the nickname "Okanyan."
Dossier rows (with sources):
| Houshou Marine | — | Marine gave her the nickname "Okanyan" (official profile); a joint marshmallow-reading stream on her recommended list | [Official OK1] |


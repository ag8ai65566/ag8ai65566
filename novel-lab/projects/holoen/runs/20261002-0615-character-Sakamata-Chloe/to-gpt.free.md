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
  Takane Lui, Hakui Koyori, Sakamata Chloe, Kazama Iroha), with their ties to the rest of the cast. This is run F of four: Chloe, Iroha, the world card "holoX" and the lines about the holoX members added to the other cast cards (listed at the end). Run E covered La+, Lui and Koyori's own cards.
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

## Card 1: Sakamata Chloe (draft, full file)

---
kind: character
name: "Sakamata Chloe"
sw_section: Characters
---

# Character File: Sakamata Chloe

> Scope: official lore and publicly shown persona only, 2021-11 to 2025-01 plus her affiliate appearance in 2025,
> treated as one continuous persona (no eras), checked 2026-10-02. Chloe concluded her regular activities on
> 2025-01-26 and remains a hololive affiliate (the official site lists her as "[Affiliate]"); added to the cast by
> author order (2026-10-02, holoX in full). Her last active year (2024) sets her default manner, per the project's
> recency rule. Nothing about the performer behind the avatar: private-life information (family, home, health,
> daily routine, sleep, outings, the reasons for any pause or for her conclusion, and the like) is outside scope
> and is not recorded here, including what she mentions in chats; the wiki's notes on her personal habits are
> deliberately left out. She streamed in Japanese; that is recorded as the language of her performance only. In
> stories she knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence
> labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; CH20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (CH#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2024 recordings (CH20: a 2024 chat and a 2024 game
> stream; see research/audio-check/chloe.md). Personal remarks are not quoted or summarized here. The audio was
> machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.

## One-line Concept
"Chomp, chomp, chooomp!": Secret Society holoX's orca intern, fixer and cleaner, officially "calm and composed at
all times" and guarded about her feelings, on stream a soft-voiced, fast-talking, mischievous kouhai who teases,
fumbles, sings in a surprisingly mature voice and keeps "forming and disbanding" a duo with Koyori. [Official CH1]
[Observed CH2 §Personality, secondary]

## Core Drive
- **Want (official dreams):** a solo concert on a big stage, a statue figure, a collab with an aquarium; music
  above all: composing, writing lyrics and singing. [Official CH1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror and bugs are listed dislikes, yet she played Resident Evil 7 all the way
  through as a self-described "super scaredy-cat" (2022). [Observed CH2 §Likes and dislikes, secondary; CH4 titles]
- **Values shown in public:** music; loyalty to holoX; a teasing, candid honesty with her Handlers. [Official CH1]
  [Observed CH2 §Personality, secondary]

## Core Contradiction
The intern who "carries out her orders without so much as batting an eyelid" and admits no feelings, who in
practice is soft, chatty and accident-prone, teases everyone and cannot keep a straight face. [Official CH1]
[Observed CH2 §Personality, secondary]

## Behavioral Traits
1. Opens a stream as a meal: "Chomp, chomp, chomp! It's time to eat!" and closes with "Thanks for the food";
   viewers are her "Handlers" (shiikuin, "keepers"), and a fish ＜＞＜ swims in the waiting room. [Official CH1]
2. Taunt-loving but sweet: compared by fans to Shirogane Noel, Momosuzu Nene and Tsunomaki Watame. [Observed CH2
   §Personality, secondary]
3. Prone to mistakes and accidents on stream. [Observed CH2 §Personality, secondary]
4. Chat streams wander into playful debates with chat: in a 2024 chat she polled viewers on when exactly someone
   becomes an "ojisan." [ASR CH20]
5. Talks in a soft, high, childlike voice and sings in a much more mature one. [Observed CH2 §Personality,
   secondary] [ASR CH20]
6. The fastest hololive member to 500,000 subscribers (within a week of her debut, 2021) and the first of holoX
   to 1 million (2023). [Observed CH2 §2021, §2023, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Official opening: "Chomp, chomp, chomp! It's time to eat!" (Japanese: "Bakku bakku baku~"). [Official CH1]
    [Observed CH2 caption, secondary]
  - Official closing: "Thanks for the food" (gochisōsama, also the title of her graduation live). [Official CH1]
    [Observed CH4 F9lbxgimNIE]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Bakku bakku baku~" → every opening. [Official CH1]
  - "Shiikuin" ("Handlers") → how she addresses chat. [Official CH1]
  - "Sakamata" → how she refers to herself. [ASR CH20] [Observed CH2]
- **Vocabulary / fillers:** sentences trailing in a drawn-out "~sā" ("zutto sā," "mecha kinchō shite sā");
  "muzui" ("tough") for hard questions; see research/audio-check/chloe.md. [ASR CH20]
- **Profanity:** playful teasing rather than swearing. [Observed CH2]
- **Language:** streamed in Japanese; she used basic English on the EN Minecraft server tour (2022) and in Calli's
  English lesson #04 (2022), and wrote her original song "Hurt you" in English (2022). [CH4] [CH5] [Observed CH2]
- **Laughs, noises:** a soft "fufufu," a breathy giggle. [ASR CH20]
- **Rhythm & rhetoric:** quick, run-on chatter that turns a small question into a poll of chat. [ASR CH20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (CH20): in a 2024 chat window, median about 301 Hz (p10–p90 about 217–482 Hz, 14 semitones) and
    about 309 characters a minute of speech (a rough pace index, not a basis for comparing members); see
    research/audio-check/chloe.md. Measurements describe the archived audio, not a target to clone.
  - Provisional (interpretation): a small, soft, high and slightly airy voice that chatters fast and
    teases; deeper and fuller when singing.
- **Sounds off:** a cool, mature speaking voice; a cold, menacing "cleaner"; slow, careful speech.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, hungry | "Chomp, chomp, chomp! It's time to eat!" (CH1) |
| Chatting | Soft, fast, run-on | Polling chat about "ojisan": 「いつからおじさんなの」 (itsu kara ojisan na no, "since when is someone an ojisan?") (ASR CH20, the shared part of the line) |
| Teasing a member | Sly, giggly | **Style demo:** "Ē~, sore Sakamata no sei ja nai yo?" ("Huh~, that's not Sakamata's fault, is it?") |
| Horror | Squeaking, panicked | [gasps] |
| Singing | Mature, full | (her original songs) |
| Closing | Content | "Thanks for the food" (CH1) |

### Sample Lines
1. "Chomp, chomp, chooomp!" (Official CH1)
2. 「いただきまーす」 (itadakimāsu, "let's eat!") (ASR CH20, opening a 2024 chat)

## Appearance Anchors (avatar)
- 148 cm; illustrator Parsley. Medium-length wavy gray hair with a black ahoge and a braided section streaked with
  black, black hair pins and one red pin, red eyes and a fang; at her debut she wore an eye mask, removed on
  stream. An open off-shoulder black jacket lined in red, fastened with belts; a white ruffled top with red and
  white ribbons; a black hood with white "eyes" and red plaid bows; a black collar with a silver heart charm;
  studded belts with chains; a red plaid skirt over black ruffles; torn black tights with garters; black
  platform boots with red laces; small yellow "caution" stickers everywhere. Her mascot is Inu, a small orca in a
  red-and-white "Caution" life jacket. Emoji 🎣. [Official CH1] [Observed CH2 §Appearance, §Mascot, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2021-11-29 | Debut, fourth of holoX; 500,000 subscribers within a week | [Official CH1] [Observed CH2] |
| 2022 | First original "Jinsei Reset Button Pochii w" (02-26); EN Minecraft tour with Bae, Mumei and Lui (02-12); Calli's English lesson #04 with Lui (04-16); 3D debut (06-13) | [Observed CH2] [CH5] |
| 2023 | 1 million subscribers, first in holoX (02-18); HOLOYOI #01 with Calli and Lui (03-23); "BAE-GEMITE DOMINATION" (04-29); a cover with Bae (10-30); Hoshimatic Project (11-) | [Observed CH2] [CH5] |
| 2024 | "Magical Girl holoWitches!" single (05-30); "Kanaken" 3D live with Kanata and AZKi | [Observed CH2] [CH4] |
| 2024-11-29 | Conclusion of regular activities announced; she stays an affiliate | [Observed CH2] |
| 2025-01 | Farewell week: last "KoyoChlo" collab, covers with La+ and Koyori, "WILDCARD" with Kiara (01-25) | [CH4] [CH5] |
| 2025-01-26 | Graduation live "Gochisōsama deshita"; tenth original song "Hikari Are" | [CH4] [Observed CH2] |
| 2025-04-26 | Performs "Sparkle" with Murasaki Shion at Shion's graduation live | [Observed CH2] |

## Relationship Map
Public exchanges only. Group ties are on the world card "holoX."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Takane Lui | holoX executive officer | "LuiChlo" collabs; kept her in line; Calli's lesson and HOLOYOI together | [CH4] [CH5] |
| Hakui Koyori | "KoyoChlo" | A duo that kept forming and disbanding; the last collab and covers in January 2025 | [CH4] |
| La+ Darknesss | holoX founder | Covers "Day by Days" (2022) and "Bōken no Sho ga Kiemashita!" (2025) | [CH4] |
| Kazama Iroha | holoX | Group streams; the 3rd-anniversary Q&A (2024) | [CH4] |
| AZKi | "Kanaken" with Amane Kanata | Minecraft construction "company," Chained Together and a 3D live (2024) | [CH4] [CH2] |
| Houshou Marine | UMISEA; holoWitches | A game about Marine's treasure ship (2023) | [CH2] [CH4] |
| Hoshimachi Suisei | Hoshimatic Project | Part of her farewell video series (2025) | [CH2] [CH4] |
| Yukihana Lamy | — | Rust with Kanata and Lamy (2022) | [CH4] |
| Shishiro Botan | — | An Overwatch 2 team with IRyS, Lui and Towa (2023) | [CH5] |
| Takanashi Kiara | — | "WILDCARD" cover (2025-01-25) and an origami off-collab (2023) | [CH5] |
| Hakos Baelz | — | EN Minecraft tour (2022); BAE-GEMITE DOMINATION, a Suika Game challenge and the cover "Crazy Scary Holy Fantasy" (2023) | [CH5] |
| Mori Calliope | — | HOLO ENGLISH LESSON #04 (2022) and HOLOYOI #01 (2023) | [CH5] |
| Nanashi Mumei (graduated) | — | The EN Minecraft tour (2022) | [CH5] |
| IRyS | — | Overwatch 2 team (2023); Among Us (2023) | [CH5] |
| Ninomae Ina'nis, Gawr Gura (graduated) | UMISEA (wiki-listed) | The ocean unit, joined by Chloe later per the wiki | [CH2 §Relationships, secondary] |

## Arc
- **Starting point:** the public persona; on the card date she is a hololive affiliate (regular activities ended
  2025-01-26).
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: an "accident" she swears was not her fault; teasing a senior one step too far; a sudden
  serious song that silences the room.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. KoyoChlo "re-forms" for one night to beat Koyori's latest experiment, then "disbands" on stream again.
  2. Lui catches Chloe "cleaning" the holoX base by hiding everything in one closet.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-11-29; Secret Society holoX (intern, fixer and cleaner); regular activities concluded 2025-01-26
  (affiliate); birthday 18 May; 148 cm; illustrator Parsley; fans Handlers (shiikuin); mascot Inu; stream tag
  #またまたさかまた; fan-art tag #さかまた飼育日記.

## Sources (checked 2026-10-02)
- CH1 Official profile ("[Affiliate] Sakamata Chloe"): https://hololive.hololivepro.com/en/talents/sakamata-chloe/
- CH2 Sakamata Chloe wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Sakamata_Chloe
- CH4 Stream archive metadata, her channel (archive.ragtag.moe): Myw1OMa2wvQ (chat, 2024), p-5eLuQw6C0 (2024),
  F9lbxgimNIE (graduation live), u5hBkM77dX0 (last KoyoChlo), acYx6NnoaAQ and wLQQD3Ok0Uk (covers with La+),
  mKq0e-7nnSU (cover with Koyori), t3p-hllEVIM and 2ou6x1eOpYA (Kanaken), D5kYN0ucG0k, z55R0Z8_qk0,
  p0UqJmkT1jU (holoX 3rd anniversary), OF41reZNGnw (with Suisei), 3lV_4bJm0Og (Resident Evil 7)
- CH5 Other members' archive metadata: eEGbAKvSf1Q, NK2ENvBoCcQ (Kiara), z4-5Hq5AKG4, p9_oBCK0olg, 9EAIDwXj4Jk,
  S-d80w5gs-c (Bae), YrZ4baKOT1c, UuL_nORzfNM (Calli), 50tBPC5c2zM (Mumei), roWKpgZsjR4, VwqdwQx5cog (IRyS)
- CH20 Claude's audio check (two-model ASR, Japanese): research/audio-check/chloe.md

---

## [SW] Name
Sakamata Chloe

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, Secret Society holoX, holoX, KoyoChlo, Kanaken, Hoshimatic Project, holoWitches, UMISEA

## [SW] Other Names
Chloe, Kuroe, Sakamata, Kura-tan

## [SW] Personality
Chloe is Secret Society holoX's orca intern, its fixer and cleaner. Officially she is calm and composed, follows orders without blinking and insists she has no feelings to hide; in practice she is a soft-voiced, fast-talking, mischievous kouhai who loves to tease, makes mistakes and has on-stream accidents, and dissolves into giggles. Her streams open like a meal ("Chomp, chomp, chomp! It's time to eat!") and close with "Thanks for the food," and her viewers are her Handlers. Music matters most to her: she composes, writes lyrics and sings in a far more mature voice than the one she talks in. She is a self-described scaredy-cat who still finishes horror games, a candid chatter who turns a stray question into a poll of chat, and Koyori's partner in "KoyoChlo," a duo that kept forming and disbanding. She concluded her regular activities in January 2025 and remains a hololive affiliate.

## [SW] Background
Chloe is a hololive affiliate, formerly an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-29 as the fourth member of Secret Society holoX, reached 500,000 subscribers within a week, the fastest in hololive, and was the first of holoX to reach a million (2023). She released ten original songs, joined Suisei's Hoshimatic Project, "Magical Girl holoWitches!" and the Minecraft "Kanaken" with Amane Kanata and AZKi, and concluded her regular activities with a graduation live on 2025-01-26, staying an affiliate; she later sang "Sparkle" at Murasaki Shion's graduation live (2025). With the English cast she toured the EN Minecraft server with Bae, Mumei and Lui (2022), took Calli's English lesson and appeared on HOLOYOI (2022–2023), joined Bae's "BAE-GEMITE DOMINATION" and covered "Crazy Scary Holy Fantasy" with her (2023), and covered "WILDCARD" with Kiara in her final week (2025).

## [SW] Physical Description
Chloe's avatar is 148 cm tall, with medium-length wavy gray hair, a black ahoge and a black-streaked braid, black and red hair pins, red eyes and a small fang. She wears an open, off-shoulder black jacket lined in red and strapped with belts, a white ruffled top, a black hood with white "eyes," a collar with a silver heart charm, studded chain belts, a red plaid skirt over black ruffles, torn black tights and tall red-laced platform boots, all dotted with little yellow "caution" stickers. Inu, a tiny orca in a "Caution" life jacket, is her mascot.

## [SW] Dialogue Style
Streamed in Japanese in quick, soft, run-on chatter that trails off in a drawn-out "~sā," calling herself "Sakamata" and her viewers "shiikuin" (Handlers). She teases seniors and friends, swears an accident "wasn't my fault," and turns questions into polls of chat. When a story renders her speech in English or Chinese, keep the third-person "Sakamata," the soft, giggly speed and the sudden switch to a serious, mature voice when she sings.

## [SW] Catchphrases
"Chomp, chomp, chomp! It's time to eat!" (official opening, "Bakku bakku baku~"); "Thanks for the food" (official closing, gochisōsama); "shiikuin" (Handlers, her viewers); "Sakamata" (how she refers to herself); "KoyoChlo" (her duo with Koyori).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a small, soft, high and slightly airy voice that chatters fast, giggles and teases; panicky squeaks in horror; noticeably deeper, fuller and more mature when she sings. Never a cool, mature speaking voice, a menacing "cleaner" or slow, careful speech.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): small, soft, high voice; quick and playful by default. Default tags: [soft, playful]. By situation: opening [bright, hungry]; chatting [fast, casual]; teasing [mischievous, giggly]; denying blame [innocent]; horror [panicked, squeaky]; singing [mature, heartfelt]. With people (proposed scene directions, not observed conversational defaults): Koyori [bickering, fond]; Lui [whiny, sheepish]; Kiara [shy, excited]; seniors [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Bakku bakku baku~" (spoken); [giggles] (tag only); [gasps] (tag only). Keep in the words: "Sakamata," "shiikuin," "bakku bakku." Reading guide (untested): さかまた くろえ. Not as default: a cool, mature or menacing voice.

## [SW] Motivation
In her lore, Chloe works as holoX's cleaner and does what she is told. As a streamer and artist she wanted to make music (composing, writing and singing), to hold a solo concert on a big stage, and to keep her Handlers laughing; since 2025 she is an affiliate.

## [SW] Relationships
Takane Lui: the executive officer who kept her in line ("LuiChlo"; Calli's English lesson and HOLOYOI together). Hakui Koyori: "KoyoChlo," a duo that kept forming and disbanding, ending with a last collab and covers in January 2025. La+ Darknesss: covers together (2022, 2025). Kazama Iroha: holoX. AZKi: "Kanaken" with Amane Kanata (Minecraft, a 3D live, 2024). Houshou Marine: UMISEA and holoWitches. Hoshimachi Suisei: Hoshimatic Project. Yukihana Lamy: Rust (2022). Shishiro Botan: an Overwatch 2 team (2023). Takanashi Kiara: "WILDCARD" (2025) and an origami off-collab (2023). Hakos Baelz: the EN Minecraft tour (2022), BAE-GEMITE DOMINATION and "Crazy Scary Holy Fantasy" (2023). Mori Calliope: HOLO ENGLISH LESSON #04 (2022) and HOLOYOI #01 (2023). Nanashi Mumei (graduated): the EN Minecraft tour (2022). IRyS: Overwatch 2 and Among Us (2023). Ninomae Ina'nis and Gawr Gura (graduated): UMISEA, per the wiki.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add holoX in full): official profile
  (CH1), wiki (CH2, by section; personal-habit notes deliberately excluded), archive metadata (CH4, CH5) and
  Claude's two-model Japanese audio check (CH20, research/audio-check/chloe.md).

## Open Questions
1. UMISEA's inclusion of Chloe rests on the wiki's unit lists (Chloe and Marine pages); no UMISEA stream with
   Chloe was found in the archive metadata. Keep it as a wiki-listed tie?


## Audio report: research/audio-check/chloe.md

# Audio check — Sakamata Chloe (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed in Japanese with faster-whisper small (multilingual), pitch measured with Praat (100–600 Hz, speech
segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the
audio was machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used
on the character card were re-transcribed by a second model (whisper medium, multilingual) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Transcription does not write
laughs reliably, and Japanese ASR often picks different kanji or kana for the same word; only spans both models
render identically are quoted. Measurements describe the sampled recording and ASR segmentation; game audio,
music and other voices prevent treating them as isolated vocal measurements.

All windows are from 2024, her last full year of regular activities (she concluded them on 2025-01-26). Only in-scope public performance material is used: personal remarks in the chats
(family, childhood, health, trips, daily life) are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat25_2024 | [【 雑談 】ねぇねぇおはなししよ【ホロライブ/沙花叉クロヱ】](https://youtu.be/Myw1OMa2wvQ) | [0:05:00–0:30:00](https://youtu.be/Myw1OMa2wvQ?t=300) | 19.3 | 5972 | 309.4 | 301 Hz | 217–482 Hz |
| sandtrix20_2024 | [【 Sandtrix+ 】最近流行りの砂テトリス！いっしょに20万点めざそ！【ホロライブ/沙花叉](https://youtu.be/p-5eLuQw6C0) | [0:10:00–0:30:00](https://youtu.be/p-5eLuQw6C0?t=600) | 15.2 | 4152 | 273.9 | 302 Hz | 124–478 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat25_2024 | sandtrix20_2024 |
|---|---|---|
| first person 私 | 1 | 0 |
| なんか | 81 | 52 |
| まあ | 10 | 5 |
| ちょっと待って | 0 | 1 |
| やばい | 2 | 15 |
| かわいい | 4 | 0 |
| えっ/え? | 3 | 1 |
| laugh (はは/ふふ/笑) | 5 | 1 |
| swear (くそ/ふざけ/殺) | 1 | 0 |
| English (Latin letters) | 7 | 10 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Opens a stream like a meal | **Observed**: 「いただきまーす」 ("itadakimāsu") near the start of the 2024 chat. | [0:05:49](https://youtu.be/Myw1OMa2wvQ?t=349) |
| Refers to herself as "Sakamata" | **Observed**; the first model renders it in several ways (e.g. 「坂本」), so no line with it is quoted. | [0:10:08](https://youtu.be/Myw1OMa2wvQ?t=608) |
| Turns a stray question into a poll of chat | **Observed**: asks chat when an "ojisan" becomes an "ojisan" and runs a show of hands. | [0:07:32](https://youtu.be/Myw1OMa2wvQ?t=452) |
| Drawn-out "~sā" sentence endings | **Observed**: 「ずっとさー」 … 「めっちゃ緊張してさー」 in the opening. | [0:05:59](https://youtu.be/Myw1OMa2wvQ?t=359) |
| Fast, soft chatter | **Observed**: about 309 characters a minute of speech in the chat window (a rough index). | — |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "おじさんっていつからおじさんなの" | [0:07:33](https://youtu.be/Myw1OMa2wvQ?t=453) | "…じさんってさいつからおじさんなの?自分でさあ…" | **Partial (computed):** shared run "いつからおじさんなの"; only that part is quoted |
| "いただきまーす" | [0:05:49](https://youtu.be/Myw1OMa2wvQ?t=349) | "…はこれです!いただきまーす!キノコ生え…" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/Sakamata-Chloe.md

# ElevenLabs v4 Performance Sheet: Sakamata Chloe

> Built from `bible/characters/Sakamata-Chloe.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Chloe concluded her regular activities on 2025-01-26 and remains a hololive affiliate; the sheet covers her 2021–2025 persona. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, soft, high and slightly airy voice that chatters fast, giggles and teases; panicky squeaks in horror."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (quick and playful; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[soft, playful]` or `[fast, casual]`; v4 has no speed slider.

## 3. Write these habits into the script
- Opens hungry: "Bakku bakku baku~" ("Chomp, chomp, chomp!") and 「いただきまーす」 ("let's eat!").
- Calls herself "Sakamata"; fast, run-on chatter that polls chat.
- Denies blame with innocent teasing.
- Closes with "Gochisōsama" ("Thanks for the food").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, hungry]` | 「いただきまーす」 ("Itadakimāsu!") |
| Chatting | `[fast, casual]` | 「いつからおじさんなの」 ("Itsu kara ojisan na no," "since when is someone an ojisan?") |
| Teasing a member | `[mischievous, giggly]` | **Style demo:** "Ē~, sore Sakamata no sei ja nai yo?" ("Huh~, that's not Sakamata's fault, is it?") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Closing | `[content]` | "Gochisōsama." (official, "Thanks for the food") |

With people (proposed scene directions, not observed conversational defaults): Koyori `[bickering, fond]`; Lui `[whiny, sheepish]`; Kiara `[shy, excited]`; seniors `[teasing]`.

## 5. Signature sounds
- "Bakku bakku baku~" (spoken)
- `[giggles]` (tag only); `[gasps]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): さかまた くろえ; ばっくばっくばく. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cool, mature or menacing speaking voice; slow, careful speech.

## 8. Example
```
[bright, hungry] Itadakimāsu!
[fast, casual] Itsu kara ojisan na no?
[mischievous, giggly] Ē~, sore Sakamata no sei ja nai yo?
[content] Gochisōsama.
```
(Lines 1–2 are her lines, quoted only where both transcripts agree (line 2 is the shared part of a longer
line); line 3 is a style demo; line 4 is her official closing.)


## Card 2: Kazama Iroha (draft, full file)

---
kind: character
name: "Kazama Iroha"
sw_section: Characters
---

# Character File: Kazama Iroha

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Iroha is an active hololive member
> (Japan, Secret Society holoX) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02, holoX
> in full). Her recent streams (2026) set her default manner, per the project's recency rule. Nothing about the
> performer behind the avatar: private-life information (family, home, health, daily routine, sleep, outings,
> any pause in activities and the like) is outside scope and is not recorded here, including what she mentions in
> chats. She streams in Japanese; that is recorded as the language of her performance only. In stories she knows
> she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; IR20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (IR#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (IR20: a 2026 kanji-writing game stream
> and her 2026 ELDEN RING stream; see research/audio-check/iroha.md). The audio was machine-transcribed and
> acoustically measured; transcripts were reviewed in context, without independent listening verification.

## One-line Concept
"Secret Society holoX's insurance policy, Kazama Iroha here, I daresay!": a blonde, ponytailed samurai bodyguard
from a remote mountain village who ends her sentences with "de gozaru," calls friends "-dono," is hailed as one
of hololive's most "seiso" (proper) members, and in practice is a cheerful, clumsy, muscle-brained competitor who
yells at her own mistakes and laughs them off. [Official IR1] [Observed IR2 §Personality, secondary]

## Core Drive
- **Want:** in her lore, to see and learn about the outside world, earning her keep as holoX's bodyguard; on
  stream, to clear what she starts (a kanji test, ELDEN RING's last boss) and to keep growing as a singer.
  [Official IR1] [Observed IR4 titles]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror games and bugs are listed dislikes. [Observed IR2 §Likes and dislikes,
  secondary]
- **Values shown in public:** loyalty to holoX; steady effort ("in training"); cheerfulness after a mistake.
  [Official IR1 stream tag] [ASR IR20]

## Core Contradiction
The "seiso" samurai and holoX's guardian, who is the only one in holoX's first meeting who did not claim to be the
smartest, and whose 2026 kanji-game title insists, "You may not believe it, but the girl in the thumbnail is
quite smart." [Observed IR2 §Personality, secondary; IR4 fhc67kDKU94 title]

## Behavioral Traits
1. Samurai speech: "de gozaru" ("I daresay") is her signature sentence ending and "-dono" her honorific for friends
   ("La+-dono"); in two 2026 game streams she rarely used the ending and more often called herself "Gozaru" in the
   third person ("Gozaru wa…"). [Official IR1] [Observed IR2 §Miscellaneous, secondary; IR4 titles] [ASR IR20]
2. Laughs off her own blunders in the moment (in a 2026 kanji game, after mixing up two characters). [ASR IR20]
3. Competitive and loud when she plays: "yoshi yoshi yoshi yoshi" when it goes right, a "yabai" spiral when it
   doesn't, and she argues back at chat when it teases her. [ASR IR20]
4. A steady duo partner: "AzuIro" with AZKi (covers, off-collab "summer camps," Cuphead endurance, a shared
   Minecraft village). [IR4]
5. Carries a katana named Chakimaru and travels with her tanuki companion Pokobee. [Observed IR2 §Miscellaneous,
   §Mascot, secondary] [Official IR1]
6. The last of holoX to reach a million subscribers (2024-11-19), which put all of holoX past the mark. [Observed
   IR2 §2024, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Official self-introduction: "Secret Society holoX's insurance policy, Kazama Iroha here, I daresay!"
    [Official IR1]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "de gozaru" → her signature sentence ending (rare in the 2026 game windows checked). [Observed IR2] [ASR IR20]
  - "Gozaru" → herself, in the third person. [ASR IR20]
  - "-dono" → for friends and seniors. [IR4 titles]
  - "yoshi yoshi yoshi yoshi" → when something works. [ASR IR20]
- **Vocabulary / fillers:** "mā mā mā mā," "yabai," "yoyū yoyū" ("easy, easy"); see
  research/audio-check/iroha.md. [ASR IR20]
- **Profanity:** mild ("yabe," "oi!"). [ASR IR20]
- **Language:** streams in Japanese; with the English cast she took Calli's English lesson #02 (2022) and did
  dance-challenge shorts with Kiara (2025). [IR5]
- **Laughs, noises:** a bright, open laugh; startled "e?" when something goes wrong. [ASR IR20]
- **Rhythm & rhetoric:** quick play-by-play, repeated words in fours ("yoshi yoshi yoshi yoshi," "mā mā mā mā"),
  then a calmer "de gozaru" when she remembers her role. [ASR IR20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (IR20): in a 2026 game window, median about 290 Hz with a very wide p10–p90 span (about 129–455 Hz;
    the low end likely includes game sound and laughter) and about 232 characters a minute of speech; about 295 Hz in
    a 2026 ELDEN RING window; see
    research/audio-check/iroha.md. Measurements describe the archived audio, not a target to clone.
  - Provisional (interpretation): a clear, bright, youthful voice with a sporty edge; earnest and polite in
    samurai mode, loud and quick when she competes.
- **Sounds off:** a gruff, grim warrior; a sultry or cool voice; slow, solemn speech.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Introduction | Proud, polite | "Kazama Iroha here, I daresay!" (IR1) |
| A blunder | Laughing it off | **Style demo:** "Mā, sō iu toki mo aru de gozaru." ("Well, these things happen, I daresay.") |
| Going well | Quick, pumped | "yoshi yoshi yoshi yoshi" (ASR IR20) |
| Teased by chat | Indignant, loud | "Oi!" (ASR IR20) |
| Guarding holoX | Earnest | **Style demo:** "Koko wa Kazama ni makaseru de gozaru!" ("Leave this to Kazama, I daresay!") |

### Sample Lines
1. "Secret Society holoX's insurance policy, Kazama Iroha here, I daresay!" (Official IR1)
2. 「よしよしよしよし」 (yoshi yoshi yoshi yoshi, "all right, all right") (ASR IR20, 2026)

## Appearance Anchors (avatar)
- 156 cm; illustrator Umibōzu. Short blonde hair tied in a ponytail with a leafy ribbon, blue eyes. A short white
  jacket with blue and yellow details tucked into a beige-and-blue belt hung with red cord, a teal skirt, black
  fingerless gloves, and over everything a kimono-like jacket the color of her hair with blue and green
  detailing; a katana (Chakimaru) on her back; white thigh-highs trimmed in gold and teal and samurai-style
  sandals. Her companion is Pokobee, a tanuki. [Official IR1] [Observed IR2 §Appearance, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2021-11-30 | Debut, the fifth and last of holoX | [Official IR1] [Observed IR2] |
| 2022 | Calli's English lesson #02 with La+ and Gura (03-04); VALORANT with Ame and Kobo Kanaeru ("KoMeHa," 06-04) | [IR5] |
| 2023 | AzuIro: GeoGuessr on a "Kazama map" AZKi made, covers and a first off-collab (08); Puyo Puyo Tetris coaching from Suisei (04); Hoshimatic Project (11-) | [IR4] [Observed IR2] |
| 2024 | Originals "Mahou Shoujo☆Magical GOZARU" and "Dreamy Sky" (06); a cookie-battle off-collab with FUWAMOCO (10-27); a guest at Kiara's 4th-anniversary live (10-06); 1 million subscribers (11-19) | [Observed IR2] [IR4] [IR5] |
| 2025 | AzuIro off-collab "summer camp" (Cuphead, 08); "A letter only you can read" (06-15); a guest at Kiara's birthday live and dance shorts with Kiara (07) | [IR4] [IR5] [Observed IR2] |
| 2026-04-29 | holoX's first concert, "First MISSION" | [Official IR6] |
| 2026-05-19 | Sings "CHA-LA HEAD-CHA-LA" with Elizabeth for her birthday, with Watame, Nene, Polka and FUWAMOCO | [IR5 xylll7Mp0jk] |
| 2026-06-18 | Ninth original song, "Kamazuki Entropy" | [Observed IR2] |

## Relationship Map
Public exchanges only. Group ties are on the world card "holoX."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| AZKi | "AzuIro" | Covers (2023, 2025), GeoGuessr, off-collab "summer camps," Cuphead, Mario Kart, a Minecraft village | [IR4] |
| La+ Darknesss | holoX founder; "La+-dono" | Showed her around the new holo server (2023); a cover (2024) | [IR4] |
| Takane Lui | holoX; "Lui-nee" | A cover, "Migikata no Chō" (2024) | [IR4] [Lui file] |
| Hakui Koyori | holoX | The early "seiso" pair | [IR2] |
| Sakamata Chloe (affiliate) | holoX | A cover, "Gehenna" (2025-01-26) | [IR4] |
| Hoshimachi Suisei | Hoshimatic Project | Coached her at Puyo Puyo Tetris (2023) | [IR4] [IR2] |
| Yukihana Lamy, Shishiro Botan | NePoX | Caravan Stories with Lamy (2023); built the roof of Botan's Minecraft shop (2023) | [IR4] [IR2] |
| Takanashi Kiara | — | A guest at Kiara's 3D lives (2024, 2025); "TASTY" dance shorts (2025) | [IR5] |
| Watson Amelia (affiliate) | "KoMeHa" with Kobo Kanaeru | VALORANT (2022) | [IR5] [IR2] |
| Mori Calliope, Gawr Gura (graduated) | — | HOLO ENGLISH LESSON #02 (2022) | [IR5] |
| FUWAMOCO | — | A prefecture cookie-battle off-collab (2024); "CHA-LA HEAD-CHA-LA" for Elizabeth (2026) | [IR4] [IR5] |
| Elizabeth Rose Bloodflame | — | Sang "CHA-LA HEAD-CHA-LA" for Elizabeth's 2026 birthday | [IR5] |

## Arc
- **Starting point:** active at the 2026 baseline: holoX's first concert behind her, a ninth original song, AzuIro
  ongoing.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a confident "easy, easy" right before a mistake; guarding holoX from a threat that turns out
  to be a bug; a long game she refuses to drop.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Iroha appoints herself Kiara's bodyguard for a day and takes it far too seriously.
  2. An AzuIro "summer camp" where AZKi navigates and Iroha charges ahead, de gozaru.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-11-30; Secret Society holoX (bodyguard, "insurance policy"); birthday 18 June; 156 cm; illustrator
  Umibōzu; fans Kazama-tai (Kazama Squad); companion Pokobee (tanuki); katana Chakimaru; stream tag #かざま修行中;
  fan-art tag #いろはにも絵を.

## Sources (checked 2026-10-02)
- IR1 Official profile: https://hololive.hololivepro.com/en/talents/kazama-iroha/
- IR2 Kazama Iroha wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Kazama_Iroha
- IR4 Stream archive metadata, her channel (archive.ragtag.moe): fhc67kDKU94 (kanji game, 2026), ufbZgdek7XU
  (ELDEN RING, 2026), AqJopALX_m0, mwhcZmc6-s8, ILOX1FXokwE, -im-pIdanZY, VxZVNuscS7c, 4ysmVAeb9A4, 70ZyyaBIBu0,
  XN4-n53tPHE, ox3mOwzEBWo (AzuIro), ywprejfAed4 (La+), U9tSa1hxU0M (cover with La+), oDIsQ6U71Po (with Lui),
  5zJp7oulbwc (with Chloe), 8tOoSNGa_rg (Suisei), 8-k6RzHBp3w (Lamy), 26w4y43sD8c (Botan), JgOwJ7m89Lk
  (FUWAMOCO)
- IR5 Other members' archive metadata: X492n37brRU (Calli), tGVhLibbYL0 (Ame), 0ldag8qdg6c, AQNPRJMMYY0,
  0LoG81pLS8c, f-UbyQUUykE (Kiara), xylll7Mp0jk (Elizabeth)
- IR6 COVER EDGE interview after "First MISSION" (2026-05-23): https://coveredge.cover-corp.com/en/list/5238
- IR20 Claude's audio check (two-model ASR, Japanese): research/audio-check/iroha.md

---

## [SW] Name
Kazama Iroha

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, Secret Society holoX, holoX, AzuIro, Hoshimatic Project, NePoX, KoMeHa

## [SW] Other Names
Iroha, Iroha-dono, Gozaru, Gozaru-chan

## [SW] Personality
Iroha is Secret Society holoX's bodyguard and "insurance policy," a samurai from a remote mountain village who set out with her tanuki companion Pokobee to see the world and now guards holoX to earn her keep. Her signature is the samurai ending "de gozaru"; she calls friends "-dono" and, in 2026 streams, often calls herself "Gozaru." Fans rank her among hololive's most "seiso" (proper) members, which she does not claim; on stream she is cheerful, earnest and competitive, a self-admitted muscle brain who charges ahead, chants "yoshi yoshi yoshi yoshi" when things work, argues back when chat teases her, and laughs off her own blunders. She sticks with long games to the end, is loyal to holoX and is half of the duo AzuIro with AZKi.

## [SW] Background
Iroha is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-30 as the fifth and last member of Secret Society holoX, became the last of holoX to pass a million subscribers (2024), which put the whole group over the mark, and has released nine original songs, the latest "Kamazuki Entropy" (2026). She formed the duo AzuIro with AZKi (covers, off-collab "summer camps," a shared Minecraft village), joined Suisei's Hoshimatic Project and sang at holoX's first concert, "First MISSION" (2026-04-29). With the English cast she took Calli's English lesson with La+ and Gura (2022), played VALORANT with Ame and Kobo Kanaeru as "KoMeHa," battled FUWAMOCO in a cookie quiz off-collab (2024), appeared at Kiara's 3D lives (2024, 2025) and sang "CHA-LA HEAD-CHA-LA" for Elizabeth's 2026 birthday.

## [SW] Physical Description
Iroha's avatar is 156 cm tall, with short blonde hair in a ponytail tied with a leafy ribbon and blue eyes. She wears a short white jacket with blue and yellow details, a belt hung with red cord, a teal skirt, black fingerless gloves and a kimono-like outer jacket the color of her hair, trimmed in blue and green, with a katana named Chakimaru on her back, white thigh-highs and samurai sandals. Pokobee, a small tanuki, travels with her.

## [SW] Dialogue Style
Streams in Japanese in a bright samurai persona: "de gozaru" as her signature ending (used sparingly in 2026 game streams), "-dono" for friends and "Gozaru" for herself. In games she switches to fast play-by-play with words repeated in fours ("yoshi yoshi yoshi yoshi," "mā mā mā mā"), a "yabai" spiral when things go wrong and a loud "oi!" at teasing chat, then laughs. When a story renders her speech in English or Chinese, keep the archaic samurai flavor ("I daresay"; in Chinese, 在下 or 是也) against an upbeat, sporty voice.

## [SW] Catchphrases
"Secret Society holoX's insurance policy, Kazama Iroha here, I daresay!" (official); "de gozaru" ("I daresay," her sentence ending); "-dono" (for friends); "yoshi yoshi yoshi yoshi" (when it works); "yoyū yoyū" ("easy, easy," right before it isn't). Her fans are the Kazama-tai.

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a clear, bright, youthful voice with a sporty edge; earnest and polite in samurai mode, quick, loud and pumped when she competes, laughing easily at her own mistakes. Never gruff, grim, sultry or slow and solemn.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, clear youthful voice. Default tags: [cheerful, earnest]. By situation: samurai introduction [proud, polite]; competing [excited, fast]; a blunder [laughs, sheepish]; teased by chat [indignant, loud]; guarding holoX [determined]; scared [panicked]. With people (proposed scene directions, not observed conversational defaults): AZKi [relaxed, playful]; La+ [patient, teasing]; Kiara [excited]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "de gozaru" (spoken); "Oi!" (spoken); [laughs] (tag only). Keep in the words: "de gozaru," "-dono," "yoshi yoshi." Reading guide (untested): かざま いろは; ござる. Not as default: a gruff warrior or a sultry, cool voice.

## [SW] Motivation
In her lore, Iroha left her mountain home to see and learn about the world and guards holoX to make a living. As a streamer she wants to clear what she starts, keep training ("Kazama in training"), grow as a singer and protect her friends.

## [SW] Relationships
AZKi: "AzuIro," her steady duo (covers, off-collab "summer camps," Cuphead, a Minecraft village). La+ Darknesss: holoX's founder, "La+-dono"; a cover (2024). Takane Lui: "Lui-nee"; a cover (2024). Hakui Koyori: holoX; her early "seiso" pair. Sakamata Chloe (affiliate since 2025): a cover on Chloe's last day (2025). Hoshimachi Suisei: Hoshimatic Project; coached her at Puyo Puyo Tetris (2023). Yukihana Lamy and Shishiro Botan: NePoX. Takanashi Kiara: a guest at Kiara's 3D lives (2024, 2025) and dance shorts (2025). Watson Amelia (affiliate): "KoMeHa" with Kobo Kanaeru (VALORANT, 2022). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: a cookie-quiz off-collab (2024). Elizabeth Rose Bloodflame: "CHA-LA HEAD-CHA-LA" for her 2026 birthday, with FUWAMOCO.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add holoX in full): official profile
  (IR1), wiki (IR2, by section), archive metadata (IR4, IR5), COVER's interview (IR6) and Claude's two-model
  Japanese audio check (IR20, research/audio-check/iroha.md).

## Open Questions
1. "Lui-nee" is carried from the Lui file; confirm it in Iroha's own streams?


## Audio report: research/audio-check/iroha.md

# Audio check — Kazama Iroha (2026-10-02)

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
| kanji20_2026 | [【漢字でGOGO】信じられないかもですがサムネの子はかなり賢い子です。【風真いろは/ホロライブ】](https://youtu.be/fhc67kDKU94) | [0:05:00–0:25:00](https://youtu.be/fhc67kDKU94?t=300) | 11.0 | 2548 | 232.1 | 290 Hz | 129–455 Hz |
| elden20_2026 | [【ELDENRING】ラスボス目の前にして数か月ぶりだが大丈夫だろうか【風真いろは/ホロライブ】](https://youtu.be/ufbZgdek7XU) | [0:10:00–0:30:00](https://youtu.be/ufbZgdek7XU?t=600) | 10.2 | 2495 | 243.5 | 295 Hz | 177–436 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | kanji20_2026 | elden20_2026 |
|---|---|---|
| first person 余 (yo) | 14 | 1 |
| first person 私 | 1 | 0 |
| なんか | 16 | 17 |
| まあ | 35 | 1 |
| ちょっと待って | 5 | 2 |
| やばい | 12 | 3 |
| かわいい | 2 | 0 |
| えっ/え? | 16 | 8 |
| laugh (はは/ふふ/笑) | 1 | 0 |
| こんなきり/こんにちは | 1 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| "de gozaru" as a sentence ending (wiki) | **Rare in 2026 windows**: almost no sentence-final "de gozaru" in a kanji game and an ELDEN RING stream; she does call herself 「ゴザル」 ("Gozaru") in the third person. | [0:14:30](https://youtu.be/ufbZgdek7XU?t=870), [0:17:38](https://youtu.be/ufbZgdek7XU?t=1058) |
| Laughs off her blunders | **Observed**: after mixing up 牛 and 午 she says something like "well, sometimes you're a dud like that" (the models disagree on 「ポンコツ」, so it is not quoted). | [0:05:46](https://youtu.be/fhc67kDKU94?t=346) |
| Repeats words in fours when it goes well | **Observed**: 「よしよしよしよし」. | [0:07:59](https://youtu.be/fhc67kDKU94?t=479) |
| Talks back to chat | **Observed**: a loud "oi" at chat's teasing in the kanji game. | [0:06:47](https://youtu.be/fhc67kDKU94?t=407) |
| Sticks with long games | **Observed**: returning to ELDEN RING's final area after months ("I don't remember anything"). | [0:10:11](https://youtu.be/ufbZgdek7XU?t=611) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "まあそういうポンコツもあるよね" | [0:05:46](https://youtu.be/fhc67kDKU94?t=346) | "…なっちゃったまあそういうポコツもあるよ…" | **Not confirmed** by the second model; not quoted |
| "よしよしよしよし" | [0:07:59](https://youtu.be/fhc67kDKU94?t=479) | "…やつキター!よしよしよしよし原因…原因……" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/Kazama-Iroha.md

# ElevenLabs v4 Performance Sheet: Kazama Iroha

> Built from `bible/characters/Kazama-Iroha.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Iroha is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear, bright, youthful voice with a sporty edge; earnest and polite in samurai mode, quick, loud and pumped when competing, laughing easily at her own mistakes."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (earnest by default, pumped when competing; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, earnest]` or `[excited, fast]`; v4 has no speed slider.

## 3. Write these habits into the script
- Calls herself "Kazama" or "Gozaru"; the samurai "de gozaru" is a set piece more than a 2026 habit.
- 「よしよしよしよし」 ("all right, all right") when things go well.
- A loud "Oi!" when chat teases her.
- Laughs off her blunders.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[proud, polite]` | "Kazama Iroha here, I daresay!" (official English) |
| Going well | `[excited, fast]` | 「よしよしよしよし」 ("Yoshi yoshi yoshi yoshi") |
| Teased by chat | `[indignant, loud]` | "Oi!" (observed interjection) |
| A blunder | `[laughs, sheepish]` | **Style demo:** "Mā, sō iu toki mo aru de gozaru." ("Well, these things happen, I daresay.") |
| Guarding holoX | `[determined]` | **Style demo:** "Koko wa Kazama ni makaseru de gozaru!" ("Leave this to Kazama, I daresay!") |

With people (proposed scene directions, not observed conversational defaults): AZKi `[relaxed, playful]`; La+ `[patient, teasing]`; Kiara `[excited]`.

## 5. Signature sounds
- "de gozaru" (spoken, as a set piece); "Oi!" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): かざま いろは; ござる. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior, a grim or solemn read, or a sultry, cool voice.

## 8. Example
```
[proud, polite] Kazama Iroha here, I daresay!
[excited, fast] Yoshi yoshi yoshi yoshi!
[indignant, loud] Oi!
[laughs, sheepish] Mā, sō iu toki mo aru de gozaru.
```
(Line 1 is her official English introduction; line 2 is her line, quoted only where both transcripts agree;
line 3 is an observed interjection; line 4 is a style demo.)


## World card 3: holoX (draft, full file)

---
kind: world
name: "holoX"
sw_section: Worldbuilding
---

# World Element: holoX (Secret Society holoX)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-02. Evidence labels as in the other world files. "Archive" = stream titles on the
> members' channels (archive.ragtag.moe, S1). holoX is hololive's sixth Japanese generation, presented as a
> secret society. Added to the cast by author order (2026-10-02). At the 2026-09-30 baseline its active members
> are La+ Darknesss, Takane Lui, Hakui Koyori and Kazama Iroha; Sakamata Chloe ended her regular activities on
> 2025-01-26 and remains an affiliate, so she appears as a member of the past (as Watson Amelia does for Myth).
> Members' private lives, breaks and the reasons for them are not recorded.

## One-line Concept
A self-styled evil secret society that streams: a tiny demon founder who wants world domination, a
level-headed executive officer who does the real work, a "brains of the operation" researcher, a samurai
bodyguard who says "de gozaru," and, until 2025, a sleepy orca intern who cleaned up after them.

## Type
Unit / generation (lore group with five persona roles; four active at the baseline).

## The roles (official profiles)
- **La+ Darknesss**, the founder and president ("See me, hear me, all of you!"): once vastly powerful, now
  sealed by shackles she cannot remember receiving; a crow companion. Fans: Plusmate. [Official S2]
- **Takane Lui**, the executive officer ("Did I Luive you waiting!?"): the society's point of contact and de facto
  leader, compassionate toward her subordinates, prone to blunders at the crucial moment. Fans: Lui-tomo. [Official
  S2]
- **Hakui Koyori**, head of R&D ("The brain of holoX!"): studies human behavior by meddling and sometimes messes
  with people to see their reactions; a robot coyote named Kokoro. Fans: Koyori's Assistants. [Official S2]
- **Sakamata Chloe**, the intern, fixer and cleaner ("Chomp, chomp, chooomp!"): calm on the surface, a music lover;
  an orca. Fans: Handlers. Ended regular activities 2025-01-26; affiliate. [Official S2] [S3 Chloe, secondary]
- **Kazama Iroha**, the "insurance policy" and bodyguard ("…I daresay!"): from a remote mountain area, traveling
  with her tanuki companion Pokobee to see the world. Fans: Kazama-tai. [Official S2]

## How they work together
- Debut week 2021-11-26 to 11-30, one member a night (La+, Lui, Koyori, Chloe, Iroha). [S3]
- Lui reins in La+ and Chloe; La+ is loud and smug ("wagahai") and gets teased by seniors as a child; Koyori and
  Iroha were first called the "seiso" pair; Iroha is the one who did not call herself the smartest in their first
  meeting collab. [S3, secondary]
- Group work: original songs (the sixth, "Gyouan Xdeath," 2025-12-01), the first album "Secret ORDER," and their
  first in-person concert, "First MISSION," at Pia Arena MM (2026-04-29) as a four-member unit, with new group
  uniforms. In a COVER interview after it, Lui said "I feel like we gave it everything I got!" and Koyori that she
  would "never forget the crowd's excitement." [Official S4] [S3]
- NePoX: joint events with NePoLaBo (Nene, Polka, Lamy, Botan). [S3]

## With the English cast
- **Takanashi Kiara:** welcomed Lui into the bird unit HOLOTORI on her debut day; HOLOTORI is Kiara, Lui,
  Mumei, Subaru and Reine; a Wario off-collab with Lui (2023-01-15); La+ and Kiara's Mythmash single "Glow in the
  Dark" (2025-07-27) and their "FAKE HEART" cover (2025-04-08); a nostalgic-games handcam off-collab with La+
  (2023-06-30); "WILDCARD," a cover with Chloe (2025-01-25); a #TASTYchallenge dance with Iroha (2025). [S1] [S3]
- **Nanashi Mumei (graduated):** HOLOTORI with Lui; "Q&A With Bird Sisters" (2025-04-19); an EN-server Minecraft
  tour with Lui, Chloe and Bae (2022). [S1]
- **Mori Calliope:** English practice with Lui (2021-12-27); "HOLO ENGLISH LESSON #02" with La+, Iroha and Gura
  (2022-03-04) and "#04" with Lui and Chloe (2022-04-16); "HOLOYOI" episode 1 with Lui and Chloe (2023); dance
  shorts to Lui's songs (2025, 2026). [S1]
- **FUWAMOCO:** "FUWAMOKOYO" with Shirakami Fubuki and Koyori (Lethal Company, 2024; Koyori on FUWAMOCO Morning,
  2024-04-26); "TWIN DAY WITH LUI" (2023-11-25); a cookie-battle off-collab with Iroha (2024-10-27) and Chained
  Together (2024-09-13); dance shorts to La+'s and Lui's 2026 songs. [S1]
- **Hakos Baelz:** "BAE-GEMITE DOMINATION" with Lui and Chloe (2023-04-29) and with Koyori (2023-04-22); a cover
  with Chloe ("Crazy Scary Holy Fantasy," 2023); dances to Lui's songs. [S1]
- **IRyS, Ouro Kronii:** Minecraft elytra hunting with Lui and Kaela (2022). [S1]
- **Watson Amelia (affiliate):** "KoMeHa" with Iroha and Kobo Kanaeru; Apex with Lui and Iofi (2022). [S1] [S3]
- **Ninomae Ina'nis, Gawr Gura (graduated):** UMISEA with Chloe, Minato Aqua and Houshou Marine. [S3]
- **Others:** Lui's 2026 song "Soar" was danced by IRyS, Nerissa, Bijou, Gigi, Raora, Calli, Bae and FUWAMOCO
  (2026 shorts); Cecilia teased La+ as "onee-sama" (2026 short); Nerissa met La+ in holoGTA (2024). [S1]

## With the other Japanese members on the cards
- AZKi: "Kanaken" with Chloe and Amane Kanata; "AzuIro" (Iroha), "KoZMy" (Koyori and Lamy); AZKi danced to La+'s,
  Koyori's and Lui's songs (2026). Suisei: Hoshimatic Project with Koyori, Chloe and Iroha. Okayu: "Dorobo
  Kensetsu" with La+ and Lui; La+'s lie-detector 3D challenge to Okayu (2026-05-19). Ayame: VALORANT with La+
  (2024); "#みっころおにかん" games with Lui (2025). Botan: NePoX; "BLT" with Lui and Tokoyami Towa. Marine: "SSS"
  with Lui and Yuzuki Choco; UMISEA with Chloe. Lamy: KoZMy with Koyori. [S3] [S1]

## History
| Date | Event | Who |
|---|---|---|
| 2021-11-26 to 11-30 | Debut week, one member a night | La+, Lui, Koyori, Chloe, Iroha |
| 2022-03-04 / 04-16 | Calli's English lessons #02 and #04 | La+, Iroha; Lui, Chloe |
| 2023 | HOLOYOI ep. 1 (Lui, Chloe); BAE-GEMITE episodes; Kiara's off-collabs with Lui and La+ | with Calli, Bae, Kiara |
| 2024 | FUWAMOKOYO; holoX "Drokei" escape event | Koyori; the group |
| 2025-01-26 | Chloe's graduation live; she stays an affiliate | Chloe |
| 2025-04-19 | "Q&A With Bird Sisters" | Lui, Mumei |
| 2025-07-27 | "Glow in the Dark" (Mythmash) | La+, Kiara |
| 2025-12-01 | 4th anniversary: "Gyouan Xdeath," album "Secret ORDER," concert announced | four members |
| 2026-04-29 | "First MISSION," Pia Arena MM | La+, Lui, Koyori, Iroha |

## Sensory Palette
- See: a tiny horned founder with silver hair, oversized sleeves and shackles, a crow beside her; a pink-haired
  researcher in a lab coat with test tubes at her belt; a pink-haired hawk officer in a magenta cape with a
  frogmouth secretary; a blonde samurai with a ponytail, a katana and a tanuki; a gray-haired orca girl in a hood.
- Hear: "Yes My Dark!"; "Konkoyo!"; "gozaru"; La+'s loud protests at being treated like a child; Lui's sigh.

## Glossary
| Term | Meaning | Who uses it |
|---|---|---|
| holoX | Secret Society holoX, hololive's sixth Japanese generation | everyone |
| Yes My Dark (YMD) | La+'s salute and fans' call | La+, Plusmate |
| HOLOTORI | the bird unit (Kiara, Lui, Mumei, Subaru, Reine) | the birds |
| NePoX | NePoLaBo plus holoX joint events | the nine |
| gozaru | Iroha's samurai copula ("I daresay") | Iroha |

## Conflicts and Story Hooks
1. La+ announces a world-domination scheme; Lui files it under "later," Koyori wants to test it, Iroha guards
   the door.
2. Kiara visits holoX's base for a HOLOTORI meeting and Lui has to explain why the founder is in time-out.
3. A holoX reunion where Chloe drops by as an affiliate and everyone pretends she never left the cleaning roster.

## Links to Characters
La+ Darknesss; Takane Lui; Hakui Koyori; Sakamata Chloe; Kazama Iroha; Takanashi Kiara; Nanashi Mumei; Mori
Calliope; FUWAMOCO; Hakos Baelz; IRyS; Ouro Kronii; Watson Amelia; Ninomae Ina'nis; Gawr Gura; AZKi; Hoshimachi
Suisei; Nekomata Okayu; Shishiro Botan; Yukihana Lamy; Houshou Marine.

## Secrets
None assigned.

## Hard Facts (continuity)
- Members and debut order: La+ (2021-11-26), Lui (11-27), Koyori (11-28), Chloe (11-29), Iroha (11-30).
- Chloe: regular activities ended 2025-01-26; affiliate.
- First in-person concert: "First MISSION," Pia Arena MM, 2026-04-29 (four members).

## Sources (checked 2026-10-02)
- S1 Stream archive metadata (archive.ragtag.moe), the members' and the EN cast's channels; IDs on the member
  files (e.g. v5RKZXNuVyw "Glow in the Dark," yspJ9xmGRfw "FAKE HEART," eEGbAKvSf1Q "WILDCARD," fEO6kSCseE0 "Bird
  Sisters," X492n37brRU and YrZ4baKOT1c English lessons, UuL_nORzfNM HOLOYOI, gCYXKgYcFmk FUWAMOCO Morning,
  MbqO5OPuT80 Twin Day, z4-5Hq5AKG4 and WwjB7QSmQng BAE-GEMITE, F3i30BIJmtY La+ and Okayu)
- S2 Official profiles: https://hololive.hololivepro.com/en/talents/la-darknesss/, …/takane-lui/,
  …/hakui-koyori/, …/sakamata-chloe/, …/kazama-iroha/
- S3 Member wiki pages (secondary), by section, via the fandom API: https://virtualyoutuber.fandom.com/wiki/La%2B_Darknesss
  and the pages for Takane Lui, Hakui Koyori, Sakamata Chloe and Kazama Iroha
- S4 COVER EDGE interview after "First MISSION" (2026-05-23): https://coveredge.cover-corp.com/en/list/5238;
  official concert site: https://ssholox-first-mission.hololivepro.com/

---

## [SW] Name
holoX

## [SW] Role
Organization

## [SW] Other Names
Secret Society holoX, holoX, hololive 6th Generation, NePoX, HOLOTORI

## [SW] Description
Secret Society holoX is hololive's sixth Japanese generation, a self-styled evil secret society that streams. La+ Darknesss is its tiny, loud founder, a once-mighty demon whose power is sealed, who calls herself "wagahai" and plans world domination while seniors treat her like a child; Takane Lui is the executive officer and de facto leader who does the real work, cares for her subordinates and blunders at the worst moment; Hakui Koyori runs R&D as the self-proclaimed "brains," meddling in everyone's affairs to study them; Kazama Iroha is the society's bodyguard and "insurance policy," a samurai from the mountains who says "de gozaru"; Sakamata Chloe, the orca intern who cleaned up after them, ended her regular activities in January 2025 and remains an affiliate. They debuted one a night in November 2021 and held their first in-person concert, "First MISSION," at Pia Arena MM in April 2026 as four. With the English cast: Lui is in the bird unit HOLOTORI with Kiara and Mumei ("Bird Sisters"); La+ and Kiara made "Glow in the Dark" (2025); Chloe and Kiara covered "WILDCARD"; Calli taught English to La+, Iroha, Lui and Chloe; Koyori is in "FUWAMOKOYO" with FUWAMOCO and Fubuki; Iroha is in "KoMeHa" with Ame and Kobo.

## [SW] Rules
holoX's "evil organization" is a performed lore frame; their schemes are bits. Chloe appears only as a former member and affiliate after 2025-01-26; the 2026 concert was four members. Collab titles show that a collab happened, not how close two members are.

## [SW] Sensory Details
A tiny horned founder with silver hair, oversized sleeves and shackles, a crow beside her; a pink-haired researcher in a lab coat with test tubes at her belt; a pink-haired hawk officer in a magenta cape with a frogmouth secretary; a blonde samurai ponytail, a katana and a tanuki; a gray-haired orca girl in a hood. "Yes My Dark!", "Konkoyo!", "de gozaru," and the founder's loud protests at being treated like a child.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author orders: add holoX in full): official profiles,
  archive metadata, the wiki (secondary) and COVER's interview after "First MISSION."

## Open Questions
1. Should Chloe's card describe her as an affiliate who can appear in present-day scenes, like Ame, or only in
   memories?


## Lines about the holoX members on the other cast cards (2026-10-02; promoted ahead of this review)

### Mori Calliope
Relationships field (exported):
Marine, Noel, Botan and holoX (La+, Lui, Chloe, Iroha): her English-lesson and HOLOYOI guests (2022–2023).

Dossier rows (with sources):
| Secret Society holoX (La+, Lui, Chloe, Iroha) | JP kouhai | English practice with Lui (2021-12-27); HOLO ENGLISH LESSON #02 with La+, Iroha and Gura (2022-03-04) and #04 with Lui and Chloe (2022-04-16); HOLOYOI #01 with Lui and Chloe (2023-03-23); dance shorts to Lui's songs | [S1 X492n37brRU, YrZ4baKOT1c, UuL_nORzfNM; world card "holoX"] |

### Takanashi Kiara
Relationships field (exported):
Pavolia Reine (ID) and Takane Lui: the bird unit HOLOTORI ("PavoNashi" with Reine). Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert. Archived episode records list HOLOTALK guests including Houshou Marine (#1), Hoshimachi Suisei ("cometori"), AZKi, Shirogane Noel, Nekomata Okayu and Nakiri Ayame. holoX: La+ Darknesss ("Glow in the Dark") and Sakamata Chloe ("WILDCARD").

Dossier rows (with sources):
| Secret Society holoX | JP kouhai | HOLOTORI with Lui and Mumei; La+: "FAKE HEART" (2025-04-08), the Mythmash single "Glow in the Dark" (2025-07-27) and an off-collab (2023-06-30); Chloe: an origami off-collab (2023-11-22) and the "WILDCARD" cover (2025-01-25); Iroha: guest at her 3D lives (2024, 2025) and #TASTYchallenge shorts (2025); Koyori: a "MIRAGE" dance short (2024) | [S1; world card "holoX"] |

### Gawr Gura
Relationships field (exported):
La+ Darknesss and Kazama Iroha: Calli's English lesson #02 together (2022).

Dossier rows (with sources):
| La+ Darknesss, Kazama Iroha, Shishiro Botan | JP members | HOLO ENGLISH LESSON #02 with La+ and Iroha (Calli's stream, 2022-03-04); "Apex Predators," a wiki-listed pair name with Botan | [S1 X492n37brRU] [Botan file, secondary] |

### Watson Amelia
Relationships field (exported):
Kazama Iroha: "KoMeHa" with Kobo Kanaeru (VALORANT, 2022).

Dossier rows (with sources):
| Kazama Iroha, Takane Lui | JP members | "KoMeHa" with Iroha and Kobo Kanaeru (VALORANT, 2022-06-04); Apex with Lui and Iofi (2022) | [S1 tGVhLibbYL0; world card "holoX"] |

### IRyS
Relationships field (exported):
Shishiro Botan, Takane Lui and Sakamata Chloe: an Overwatch 2 team (2023); Hakui Koyori: Splatoon 3 and Among Us.

Dossier rows (with sources):
| Shishiro Botan, Takane Lui, Sakamata Chloe, Hakui Koyori | JP members | Left 4 Dead 2 with Botan (2022-04-24); an Overwatch 2 team with Botan, Lui, Chloe and Towa (Holizontal JAM, 2023-08); Splatoon 3 (2022-10-03) and Among Us (2023-05-08) with Koyori and Chloe; Minecraft elytra hunting with Lui and Kronii (2022) | [S1 K1wStJxm4F0, roWKpgZsjR4, Xoma7oWsMcM, VwqdwQx5cog] |

### Nerissa Ravencroft
Relationships field (exported):
La+ Darknesss: holoGTA (2024) and a dance short to her "Onee-sama♡Love Call" (2026); Takane Lui: a "Soar" dance short (2026).

Dossier rows (with sources):
| Takane Lui, La+ Darknesss | JP members | Dance shorts to Lui's "Soar" (2026) and La+'s "Onee-sama♡Love Call" (2026); holoGTA with La+ (2024) | [S1 l5fGacH2i-o, ZINB546CMEw; world card "holoX"] |

### Ouro Kronii
Dossier rows (with sources):
| Takane Lui, Shirogane Noel, Kikirara Vivi | JP members | Minecraft elytra hunting with Lui, IRyS and Kaela (2022); Mumei's Gartic Phone EN + ID + JP with Noel and Vivi (2025-04-14) | [S1 OMDzBQohAf8; world card "holoX"] |

### Nanashi Mumei
Relationships field (exported):
Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Kiara hosted Mumei as HOLOTALK's 33rd guest on 2025-04-22. JP: archived uploads document her Q&A with Takane Lui, an April 2025 duet cover with Inugami Korone, and Korone, Okayu, Nene and Koyori as 2024 "Outside the Box" guests; Tokoyami Towa calls her "Mumi-chan"; Akai Haato: Minecraft. Sakamata Chloe: Mumei's EN-server Minecraft tour with Lui and Bae (2022).
Dossier rows (with sources):
| Takane Lui, Tokoyami Towa, Akai Haato | JP seniors | "【MUMEI + LUI】Q&A With Bird Sisters !!!" (2025-04-19); Towa calls her "Mumi-chan"; Minecraft "Peace & Love with HAACHAMA" (2025) | [Observed M2 infobox; M3] |
| Inugami Korone, Nekomata Okayu (GAMERS); Momosuzu Nene, Hakui Koyori | JP seniors | All four were guests at "Outside the Box" (2024-08-05); Korone and Mumei released a duet cover of "とんとんまーえ！" (2025-04-23, P6GLC_HnCUU) | [Observed M3 descriptions] |
| Sakamata Chloe, Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Chloe and Lui on Mumei's EN-server Minecraft tour with Bae (2022-02-12); Marine's horror game with Bae (2023-08-23); Noel and Vivi in Mumei's Gartic Phone EN + ID + JP (2025-04-14) | [S1 50tBPC5c2zM, RY1GkF4jMls, OMDzBQohAf8] |

### Fuwawa Abyssgard
Relationships field (exported):
Shirakami Fubuki and Hakui Koyori ("FUWAMOKOYO"): horror and Lethal Company partners. Takane Lui: "TWIN DAY WITH LUI" (2023). Kazama Iroha: a cookie-quiz off-collab (2024).
Dossier rows (with sources):
| Secret Society holoX (Koyori, Lui, Iroha, La+) | JP members | "FUWAMOKOYO" with Koyori and Fubuki (Lethal Company 2024; Koyori on FUWAMOCO Morning ep. 90, 2024-04-26; a guest at their 2025 birthday concert); "TWIN DAY WITH LUI" (2023-11-25); a cookie-quiz off-collab with Iroha (2024-10-27); dance shorts to La+'s and Lui's 2026 songs | [S1 gCYXKgYcFmk, XR1PEtj15kE, ouQF2A1l_cI, MbqO5OPuT80, JgOwJ7m89Lk] |

### Mococo Abyssgard
Relationships field (exported):
Hakui Koyori: a FUWAMOCO MORNING guest host ("FUWAMOKOYO"). Takane Lui: "TWIN DAY WITH LUI" (2023). Kazama Iroha: a cookie-quiz off-collab (2024).
Dossier rows (with sources):
| Secret Society holoX (Koyori, Lui, Iroha, La+) | JP members | "FUWAMOKOYO" with Koyori and Fubuki (Lethal Company 2024; Koyori on FUWAMOCO Morning ep. 90, 2024-04-26; a guest at their 2025 birthday concert); "TWIN DAY WITH LUI" (2023-11-25); a cookie-quiz off-collab with Iroha (2024-10-27); dance shorts to La+'s and Lui's 2026 songs | [S1 gCYXKgYcFmk, XR1PEtj15kE, ouQF2A1l_cI, MbqO5OPuT80, JgOwJ7m89Lk] |

### Elizabeth Rose Bloodflame
Relationships field (exported):
Takanashi Kiara: calls her "Erby Berby." 2026 birthday-live guests: FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine and Korone.


### Cecilia Immergreen
Relationships field (exported):
La+ Darknesss: Cecilia teased her as "onee-sama" in a 2026 short.

Dossier rows (with sources):
| La+ Darknesss | holoX senior | Cecilia teased La+ as "onee-sama" in a 2026 short | [S1 tqF0_rYGW20] |

### Raora Panthera
Dossier rows (with sources):
| Takane Lui | holoX senior | A dance short to Lui's "Soar" (2026) | [world card "holoX"] |

### Hakos Baelz
Relationships field (exported):
Natsuiro Matsuri: "Kakumei Dualism" at the 2026 fes. holoX: Sakamata Chloe ("Crazy Scary Holy Fantasy," 2023), Takane Lui and Hakui Koyori on BAE-GEMITE DOMINATION.
Dossier rows (with sources):
| Secret Society holoX (Lui, Chloe, Koyori) | JP kouhai | The EN-server Minecraft tour with Mumei, Lui and Chloe (2022-02-12); BAE-GEMITE DOMINATION #4 with Koyori and Nene (2023-04-22) and #5 with Lui and Chloe (2023-04-29); a Suika Game challenge and the "Crazy Scary Holy Fantasy" cover with Chloe (2023-10-30); KHAOS KITCHEN taste testers Koyori, Calli and Subaru (2023-11-24) | [HB3 S-d80w5gs-c, WwjB7QSmQng, z4-5Hq5AKG4, p9_oBCK0olg, 9EAIDwXj4Jk, NdLiUW-nUlk] |

### AZKi
Relationships field (exported):
Amane Kanata and Kazama Iroha: collaborators associated with KanatAZ and AzuIro ("AZUIRO BESTIE DAYS," 2025).
Dossier rows (with sources):
| Kazama Iroha | "AzuIro" (secondary label) | Frequent partner since 2022; their original "AZUIRO BESTIE DAYS" (2025-09-18) | [AZ2] [Official AZ10] |


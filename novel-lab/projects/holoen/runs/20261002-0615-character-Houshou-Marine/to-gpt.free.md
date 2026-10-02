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
  Takane Lui, Hakui Koyori, Sakamata Chloe, Kazama Iroha), with their ties to the rest of the cast. This is run C of four: Marine, Noel and Lamy. Run D covers Botan, Vivi, "JP Senpai Pairs 2" and the cross-card lines about these five; runs E and F cover holoX.
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

## Card 1: Houshou Marine (draft, full file)

---
kind: character
name: "Houshou Marine"
sw_section: Characters
---

# Character File: Houshou Marine

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Marine is an active hololive member
> (Japan, 3rd generation / hololive Fantasy) at the 2026-09-30 baseline; added to the cast by author order
> (2026-10-02). Her recent streams (2026) set her default manner, per the project's recency rule. Nothing about the
> performer behind the avatar: private-life information (family, home, health, daily routine, past jobs, outings,
> the performer's real age and the like) is outside scope and is not recorded here, including what she mentions in
> chats. Her adult-oriented humor is part of her public persona, but this card keeps it non-explicit and does not
> quote it. She streams in Japanese; that is recorded as the language of her performance only. In stories she
> knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; MA20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (MA#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (MA20: a 2026 Forza Horizon 6 stream and
> a 2026 evening chat; see research/audio-check/marine.md). Personal remarks are not quoted or summarized here. The
> audio was machine-transcribed and acoustically measured; transcripts were reviewed in context, without
> independent listening verification.

## One-line Concept
"Ahoy! Captain of the Houshou Pirates, Houshou Marine here!": hololive's self-proclaimed pirate captain (a
"cosplayer" saving up for a real ship), a bold, fast-talking, quick-witted entertainer who teases seniors and
viewers alike, panics loudly at anything sudden, sings and dances like an idol, and is one of the biggest
channels in hololive. [Official MA1] [Observed MA2 §Personality, secondary]

## Core Drive
- **Want (official dream):** to procure a pirate ship, set sail with her crew and say at the end, "My greatest
  treasure was this scenery and the friends we made along the way." [Official MA1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** being rushed or surprised: she piles up "wait"s and orders
  everyone, herself included, to calm down. [ASR MA20]
- **Values shown in public:** entertaining people; reading the room (the wiki notes she is very sensitive to her
  social surroundings); talking up hololive's behind-the-scenes happenings. [Observed MA2 §Personality, secondary]

## Core Contradiction
A treasure-hungry captain without a ship who claims to be a 17-year-old (a running joke she plays straight while
seniors and kouhai tease her for it), loud and shameless on stream, yet sharp about people and generous with
her juniors. [Official MA1] [Observed MA2 §Personality, secondary]

## Behavioral Traits
1. Opens with "Ahoy!" and closes with "Shukkō!" ("set sail"); her crew are the Houshou no Ichimi. [Official MA1]
   [Observed MA2 §Personality, secondary]
2. Fast and loud: in a 2026 racing game she rattled off repeated "wait"s and "too fast"s, then 「一回落ち着こうよ」
   ("let's calm down for a sec"). [ASR MA20]
3. Talks back at the game and chat in a rough, comic register (first-model observation; the line is not
   quoted because the second model hears it differently).
   [ASR MA20]
4. Teases seniors and viewers playfully; her risqué jokes are part of the persona (not quoted here). [Observed MA2
   §Personality, secondary]
5. A singer and idol with a wide vocal range: albums, a solo concert, and in 2026 "Chatter Chatter" with Suisei and
   the single "Kyapi." [Observed MA2 §Trivia, §Discography, secondary; MA4]
6. Close to Usada Pekora ("PekoMari"; Pekora coaches her at Mario Tennis in 2026 as "Pekoach"). [MA4]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "Ahoy! Captain of the Houshou Pirates, Houshou Marine here!" and "Keep 'er steady!" [Official MA1]
  - Sign-off: "Shukkō!" ("set sail"). [Observed MA2 §Personality, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Ahoy!" → every opening. [Official MA1]
  - "Senchō" ("the captain") → how she refers to herself. [Observed MA2 nickname; MA4 titles]
  - Repeated "matte" ("wait") → anything sudden (first model; not quoted). [ASR MA20]
- **Vocabulary / fillers:** see research/audio-check/marine.md (2026 windows).
- **Profanity:** rough, comic ("baka"), plus risqué humor kept off this card. [ASR MA20] [Observed MA2]
- **Language:** streams in Japanese; she was a guest on Calli's first English lesson (2022) and Kiara's first
  HOLOTALK (2020), and off-collabs with Calli, Bae, FUWAMOCO and Nerissa. [MA5]
- **Laughs, noises:** loud, cackling laughter; shrieks when startled. [ASR MA20]
- **Rhythm & rhetoric:** rapid-fire commentary, words repeated in fours, a rising panic, then a punchline.
  [ASR MA20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (MA20): in a 2026 game window, median about 279 Hz with a very wide p10–p90 span (about 150–477 Hz;
    the low end likely includes game sound) and about 315 characters a minute of speech (a rough pace index, not a
    basis for comparing members); see research/audio-check/marine.md. Measurements describe the archived audio,
    not a target to clone.
  - Provisional (interpretation): a bright, brassy, mature-sounding mid-high voice ("onee-san") that speeds into
    rapid-fire comedy, jumps into shrieks and can switch to a cutesy idol voice on demand.
- **Sounds off:** quiet, slow or shy delivery; a sleepy tone; a refined, reserved lady.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, brassy | "Ahoy!" (MA1) |
| Startled | Rapid, shrieking | **Style demo:** "Matte matte matte!" ("Wait wait wait!") |
| Regrouping | Comic self-command | "一回落ち着こうよ" (ikkai ochitsukō yo, "let's calm down for a sec") (ASR MA20) |
| Talking back | Rough, comic | **Style demo:** "Baka iu na!" ("Don't be stupid!") |
| Idol mode | Cute, high | **Style demo:** "Senchō no koto, suki ni naccha dame da yo♡" ("You mustn't fall for the Captain♡") |
| Closing | Bright | "Shukkō!" (MA2) |

### Sample Lines
1. "Ahoy! Captain of the Houshou Pirates, Houshou Marine here!" (Official MA1)
2. "一回落ち着こうよ" (ikkai ochitsukō yo, "let's calm down for a sec") (ASR MA20, 2026)

## Appearance Anchors (avatar)
- 150 cm; illustrator Akasa Ai. Crimson-red hair in twintails tied with ribbons, under a black pirate hat with gold
  trim and a plume; an eyepatch over one eye; heterochromatic eyes (gold and red). A red cropped vest with gold
  buttons and a red bow at the collar, a long black captain's coat with gold trim and red anchor-badged cuffs worn
  over her shoulders, a red pleated miniskirt, dark thigh-high stockings and red-and-brown heeled boots. Her mascot
  is Kumarine, a bear. [Official MA1 key art, described by Claude] [Observed MA2 §Appearance, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2019-08-11 | Debut, hololive 3rd generation (hololive Fantasy) | [Official MA1] |
| 2020-11-20 | First guest on Kiara's "HOLOTALK" | [MA5 3HwaqbdKO1s] |
| 2022-02-19 | Calli's HOLO ENGLISH LESSON #01 with Ina and Fubuki | [MA5 bfUEbp3xk4o] |
| 2023-08 | Her horror game "Truth of Beauty Witch -Marine's treasure ship-"; an off-collab house party with Calli and Bae | [Observed MA2 §Events] [MA5] |
| 2024 | 3 million subscribers (01-10); album "Ahoy!! You're All Pirates♡!" (10-16); off-collabs with FUWAMOCO and Nerissa; a solo concert (12) | [Observed MA2] [MA5] |
| 2025-05-05 | 4 million subscribers, second in hololive and first among Japanese VTubers | [Observed MA2 §2025] |
| 2026-01-17 | hololive Fantasy concert "#OperationHeartfulCuties," K-Arena Yokohama | [Observed MA2 §2025–2026] |
| 2026-02-28 | "Chatter Chatter" with Hoshimachi Suisei | [MA4 di9NZ6ja_mE] |
| 2026-08 | 7th anniversary and a new 3D costume (08-11); single "Kyapi" (08-12) | [Observed MA2 §2026, §Discography] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Shirogane Noel | hololive Fantasy; "Onee-san Gumi" with Shiranui Flare | Units "Bara☆Dice" and "Yakamashi Musume" | [MA2] |
| Hoshimachi Suisei | "Chatter Chatter" (2026); holoALICE, MOMAS | A duet with an original anime MV | [MA4] [MA2] |
| Yukihana Lamy | "Yakamashi Musume"; holoWitches; Blue Journey | — | [MA2] |
| Kikirara Vivi | "MVP" with Usada Pekora | — | [MA2] |
| Hakui Koyori | The "pink-haired pair"; Blue Journey | A talk testing whether they are alike (2025); backseat Pikachu; a race (2025) | [MA4] [Koyori file] |
| La+ Darknesss | "#MariLa+" | A sponsored collab (2025); a cover with La+ and Koyori (2025) | [MA4] |
| Takane Lui | "SSS" with Yuzuki Choco; Bara☆Dice | — | [MA2] |
| Sakamata Chloe (affiliate) | UMISEA; holoWitches | Chloe played Marine's horror game (2023) | [MA2] |
| Kazama Iroha | Bara☆Dice | — | [MA2] |
| Nekomata Okayu | HoLOGSS, MOMAS | — | [MA2] |
| Takanashi Kiara | Her first HOLOTALK guest (2020) | A "MIRAGE" dance short (2024); danced to "III" | [MA5] |
| Mori Calliope | — | English lesson #01 (2022); Mario Kart (2021); a house-party off-collab with Bae (2023); played Marine's horror game | [MA5] |
| Hakos Baelz | — | Mario Kart (2021); Calli's house party (2023); played Marine's horror game with Mumei (2023); dance covers | [MA5] |
| Ninomae Ina'nis, Gawr Gura (graduated) | UMISEA | English lesson #01 with Ina (2022); "SHINKIRO" with Gura (GuraMarine) | [MA5] [MA2] |
| Nanashi Mumei (graduated) | — | Played Marine's horror game with Bae (2023) | [MA5] |
| FUWAMOCO | — | Touhou off-collab (2024-04-30); Mario Party with Nerissa (2024); watched her solo concert (2024); danced to "Chatter Chatter" (2026) | [MA5] |
| Nerissa Ravencroft | — | Mario Party Superstars off-collab with FUWAMOCO (2024); a dance short to her song | [MA5] |
| Elizabeth Rose Bloodflame | — | Sang "IT'S LOVE" with her and Korone for Elizabeth's 2026 birthday | [MA5] |
| Nakiri Ayame | 2nd-gen senior | Secondary accounts say Ayame admires her | [Ayame file, secondary] |

## Arc
- **Starting point:** active at the 2026 baseline: past 4 million subscribers, a hololive Fantasy concert, a duet
  with Suisei and a new single behind her.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a "treasure" scheme for the ship fund; teasing a kouhai who teases back; panic at any
  surprise.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Marine recruits FUWAMOCO as cabin girls for a "voyage" that never leaves the studio.
  2. Kiara invites Marine back to HOLOTALK and Marine takes over as host.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
Her humor is famously risqué; in stories it stays suggestive at most, never explicit.

## Hard Facts (continuity)
- Debut 2019-08-11; hololive 3rd generation (hololive Fantasy); birthday 30 July; 150 cm; illustrator Akasa Ai;
  fans Houshou no Ichimi; mascot Kumarine; stream tag #マリン航海記; fan-art tag #マリンのお宝.

## Sources (checked 2026-10-02)
- MA1 Official profile: https://hololive.hololivepro.com/en/talents/houshou-marine/ (text and key art)
- MA2 Houshou Marine wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Houshou_Marine
- MA4 Stream archive metadata, her channel (archive.ragtag.moe): aHis7-TfsJY (Forza Horizon 6, 2026), H1Z96LzzG7k
  (chat, 2026), di9NZ6ja_mE ("Chatter Chatter"), GWZrQZ6leZI (with Pekora), Xf4MPOkHKtE (with La+), QnT0cKrEhkk
- MA5 Other members' archive metadata: 3HwaqbdKO1s, tzVgzvV0cVo, I8DEx4MomOA (Kiara), bfUEbp3xk4o, Tpzbfccp_ZM,
  DY5VThfehW8, Mf-sAjsuSig (Calli), X3pHIQAvpYU, RY1GkF4jMls (Bae), x7gRHgQ0yI0, zQdsLXE4ZQ8, PtaFGDOaj0k
  (FUWAMOCO), FLL7e1-RPGo, Lo9q4WJrcM4 (Nerissa), iwnHChZq0N8 (Elizabeth)
- MA20 Claude's audio check (two-model ASR, Japanese): research/audio-check/marine.md

---

## [SW] Name
Houshou Marine

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 3rd generation, hololive Fantasy, Onee-san Gumi, UMISEA, holoWitches, Bara☆Dice, Yakamashi Musume, SSS, MVP, Blue Journey

## [SW] Other Names
Marine, Senchō (Captain), Maririn

## [SW] Personality
Marine is hololive's self-proclaimed pirate captain: a girl who loves jewels, treasure and money and is saving up as a VTuber for a real pirate ship, wearing her pirate outfit as "cosplay" until then. She is bold, fast-talking and very funny, playfully mocking seniors and viewers alike, with a famously risqué streak of humor that she plays for laughs. She panics loudly at anything sudden (a pile of "wait"s, then "let's calm down for a sec"), talks back to games and chat in a rough comic register, and insists she is seventeen while everyone teases her about it. Under the noise she is sharp about people, reads a room quickly, talks up hololive's behind-the-scenes life and looks after her juniors. She is also a serious idol and singer with a wide vocal range, and calls herself "Senchō," the Captain.

## [SW] Background
Marine is an active member of hololive's 3rd generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2019-08-11 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Shirogane Noel, and reached 3 million subscribers in 2024 and 4 million in 2025. She released the album "Ahoy!! You're All Pirates♡!" (2024), held a solo concert (2024), headlined hololive Fantasy's "#OperationHeartfulCuties" concert (2026), sang "Chatter Chatter" with Suisei (2026) and released the single "Kyapi" (2026). With the English cast she was Kiara's first HOLOTALK guest (2020), joined Calli's first English lesson (2022), hosted off-collabs with Calli and Bae, FUWAMOCO and Nerissa, inspired a horror game that Calli, Bae and Mumei played, and sang for Elizabeth's 2026 birthday.

## [SW] Physical Description
Marine's avatar is 150 cm tall, with crimson-red twintails tied with ribbons, a black gold-trimmed pirate hat with a plume, an eyepatch and heterochromatic gold and red eyes. She wears a red cropped vest with gold buttons and a red collar bow, a long black captain's coat with gold trim and anchor-badged red cuffs slung over her shoulders, a red pleated miniskirt, dark thigh-highs and red-and-brown heeled boots. Kumarine, a bear, is her mascot.

## [SW] Dialogue Style
Streams in Japanese at top speed: "Ahoy!" to open, "Shukkō!" to set sail at the end, "Senchō" for herself. She piles up "wait"s when startled, orders herself to calm down, argues with the game in a rough comic voice, cackles, teases and can flip instantly into a sugary idol voice. When a story renders her speech in English or Chinese, keep the pirate-captain bravado, the speed and the self-aware jokes; keep any innuendo light.

## [SW] Catchphrases
"Ahoy! Captain of the Houshou Pirates, Houshou Marine here!" (official); "Keep 'er steady!" (official); "Shukkō!" ("set sail," her sign-off); "Senchō" (the Captain, herself); "Houshou no Ichimi" (her crew, the fans).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a bright, brassy, mature-sounding mid-high voice that speeds into rapid-fire comedy, jumps into shrieks when startled, cackles loudly, and switches on demand to a cutesy idol voice or a full singing voice. Never quiet, slow, shy, sleepy or reserved.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, brassy mid-high voice. Default tags: [energetic, brassy]. By situation: opening [bright, theatrical]; startled [panicked, rapid]; arguing with a game [rough, comic]; teasing [mischievous]; idol mode [cutesy, sweet]; heartfelt thanks [warm]. With people (proposed scene directions, not observed conversational defaults): Pekora [bickering, fond]; Suisei [playful]; Kiara [flirty, teasing]; FUWAMOCO [doting]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Ahoy!" (spoken); [cackles] (tag only); [shrieks] (tag only). Keep in the words: "Ahoy," "Senchō," "Shukkō." Reading guide (untested): ほうしょう まりん; せんちょう. Not as default: quiet, shy or slow delivery.

## [SW] Motivation
In her lore, Marine wants a real pirate ship to sail with her crew in search of treasure, and in the end to find that the treasure was the journey and the friends. As a streamer and idol she wants to entertain everyone, keep singing and growing, and look after hololive's juniors.

## [SW] Relationships
Shirogane Noel: hololive Fantasy and "Onee-san Gumi" with Shiranui Flare; Bara☆Dice, Yakamashi Musume. Hoshimachi Suisei: "Chatter Chatter" (2026). Yukihana Lamy: Yakamashi Musume, holoWitches. Kikirara Vivi: "MVP" with Usada Pekora. Hakui Koyori: the "pink-haired pair." La+ Darknesss: "#MariLa+" (2025). Takane Lui: "SSS." Sakamata Chloe (affiliate): UMISEA, holoWitches. Kazama Iroha: Bara☆Dice. Nekomata Okayu: HoLOGSS, MOMAS. Takanashi Kiara: her first HOLOTALK guest (2020); dance shorts. Mori Calliope: English lesson #01 (2022), Mario Kart, a house-party off-collab (2023). Hakos Baelz: Mario Kart and the house party; played Marine's horror game with Mumei. Ninomae Ina'nis and Gawr Gura (graduated): UMISEA; "SHINKIRO" with Gura. FUWAMOCO: a Touhou off-collab and Mario Party with Nerissa (2024). Nerissa Ravencroft: that Mario Party off-collab. Elizabeth Rose Bloodflame: "IT'S LOVE" for her 2026 birthday. Nakiri Ayame: a second-generation senior who, by secondary accounts, admires her.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Houshou Marine): official profile and
  key art (MA1), wiki (MA2, by section; explicit profile lines and private details deliberately excluded), archive
  metadata (MA4, MA5) and Claude's two-model Japanese audio check (MA20, research/audio-check/marine.md).

## Open Questions
1. Her official profile and wiki include explicit lines; the card keeps them out. Confirm the author wants only a
   "risqué, non-explicit" note.


## Audio report: research/audio-check/marine.md

# Audio check — Houshou Marine (2026-10-02)

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
| drinkchat25_2026 | [宝鐘マリン、乱れる───【ホロライブ/宝鐘マリン】](https://youtu.be/H1Z96LzzG7k) | [0:05:00–0:30:00](https://youtu.be/H1Z96LzzG7k?t=300) | 20.9 | 7346 | 351.8 | 281 Hz | 194–450 Hz |
| drive25_2026 | [【Forza Horizon 6】船長とドライブしましょ～～～～ん♡♡♡【ホロライブ/宝鐘マリン](https://youtu.be/aHis7-TfsJY) | [0:05:00–0:30:00](https://youtu.be/aHis7-TfsJY?t=300) | 16.2 | 5085 | 314.5 | 279 Hz | 150–476 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | drinkchat25_2026 | drive25_2026 |
|---|---|---|
| first person 私 | 0 | 3 |
| なんか | 57 | 8 |
| まあ | 8 | 2 |
| ちょっと待って | 4 | 10 |
| やばい | 3 | 11 |
| かわいい | 2 | 0 |
| えっ/え? | 5 | 12 |
| laugh (はは/ふふ/笑) | 3 | 0 |
| swear (くそ/ふざけ/殺) | 4 | 1 |
| ありがとう | 1 | 2 |
| English (Latin letters) | 2 | 16 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Panics loudly at anything sudden | **Observed**: 「待って待って待って待って」 and 「一回落ち着こうよ」 ("let's calm down for a sec") in a 2026 racing game. | [0:05:28](https://youtu.be/aHis7-TfsJY?t=328), [0:05:41](https://youtu.be/aHis7-TfsJY?t=341) |
| Talks back at the game in a rough, comic register | **Observed**: 「馬鹿言ってるんじゃねぇや」 ("don't talk nonsense!"). | [0:06:43](https://youtu.be/aHis7-TfsJY?t=403) |
| Refers to herself as "Senchō" | **Observed**: 「船長」 in both windows. | [0:17:17](https://youtu.be/aHis7-TfsJY?t=1037) |
| Very fast commentary | **Observed**: about 315 characters a minute of speech in the racing window (a rough index; game sound mixed in). | — |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "待って待って待って待って" | [0:05:28](https://youtu.be/aHis7-TfsJY?t=328) | "…開?ちょっと待って待て説明がない…" | **Not confirmed** by the second model; not quoted |
| "一回落ち着こうよ" | [0:05:41](https://youtu.be/aHis7-TfsJY?t=341) | "…回落ち着こう一回落ち着こうよね、だいたい…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "馬鹿言ってるんじゃねぇや" | [0:06:43](https://youtu.be/aHis7-TfsJY?t=403) | "…!バカ言ってんじゃねーよ!ウィン…" | **Not confirmed** by the second model; not quoted |


## Performance sheet: export/elevenlabs/Houshou-Marine.md

# ElevenLabs v4 Performance Sheet: Houshou Marine

> Built from `bible/characters/Houshou-Marine.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Marine is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, brassy, mature-sounding mid-high voice; rapid-fire and comic, jumping into shrieks when startled and loud cackles; switches on demand to a cutesy idol voice."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **35%** (API `0.35`) (big comic swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[energetic, brassy]` or `[panicked, rapid]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Ahoy!" to open; calls herself "Senchō" (Captain); "Shukkō!" (set sail) to close.
- Fast, loud comedy; talks back to games and to chat.
- Regroups out loud: 「一回落ち着こうよ」 ("let's calm down for a sec").
- Flips into a cutesy idol voice for a bit, then straight back. Humor stays non-explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, theatrical]` | "Ahoy!" (official) |
| Startled | `[panicked, rapid]` | **Style demo:** "Matte matte matte!" ("Wait wait wait!") |
| Regrouping | `[comic, self-scolding]` | 「一回落ち着こうよ」 ("Ikkai ochitsukō yo," "let's calm down for a sec") |
| Arguing with a game | `[rough, comic]` | **Style demo:** "Baka iu na!" ("Don't be stupid!") |
| Idol mode | `[cutesy, sweet]` | **Style demo:** "Senchō no koto, suki ni naccha dame da yo♡" ("You mustn't fall for the Captain♡") |
| Closing | `[bright]` | "Shukkō!" (secondary transcription) |

With people (proposed scene directions, not observed conversational defaults): Pekora `[bickering, fond]`; Suisei `[playful]`; Kiara `[flirty, teasing]`; FUWAMOCO `[doting]`.

## 5. Signature sounds
- "Ahoy!" (spoken)
- `[cackles]` (tag only); `[shrieks]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ほうしょう まりん; せんちょう; しゅっこう. Listen to how the chosen voice says them and adjust.

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


## Card 2: Shirogane Noel (draft, full file)

---
kind: character
name: "Shirogane Noel"
sw_section: Characters
---

# Character File: Shirogane Noel

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Noel is an active hololive member
> (Japan, 3rd generation / hololive Fantasy) at the 2026-09-30 baseline; added to the cast by author order
> (2026-10-02). Her recent streams (2026) set her default manner, per the project's recency rule. Nothing about the
> performer behind the avatar: private-life information (family, home, health, daily routine, sleep, school,
> birthplace, pets, lessons, outings, body talk and the like) is outside scope and is not recorded here, including
> what she mentions in chats and what the wiki lists. She streams in Japanese; that is recorded as the language of
> her performance only. In stories she knows she is a streamer with a persona (see the world card "VTuber Persona
> and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; NO20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (NO#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (NO20: a June 2026 Sunday-morning chat
> and a June 2026 Dragon Quest VII Reimagined stream; see research/audio-check/noel.md). Personal remarks are not
> quoted or summarized here. The audio was machine-transcribed and acoustically measured; transcripts were
> reviewed in context, without independent listening verification.

## One-line Concept
"All hustle, all muscle! Shirogane Noel's here!": the silver-haired knight "Danchou" (commander) of hololive
Fantasy, an easy-going, fluffy meathead who tries to solve every problem with muscle, talks to her knights in a
cheerful, girlish voice that belies her armor, rarely wins at the games she loves, and is devoted, loudly and
jealously, to her partner Shiranui Flare. [Official NO1] [Observed NO2 §Personality, secondary]

## Core Drive
- **Want:** in her lore, to grow stronger by training among the "stronk" people of the VTuber world; on stream, to
  have fun with her knights and with her hololive friends, and to keep singing. [Official NO1] [Observed NO2]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** losing at games (often), and anyone getting too close to Flare (a running bit).
  [Observed NO2 §Personality, secondary]
- **Values shown in public:** loyalty to her knights and to hololive Fantasy; enthusiasm; telling chat about the
  week "as much as I can share." [ASR NO20]

## Core Contradiction
A "meathead" armored knight with a mace who speaks in a soft, girlish voice, plays games with more passion than
skill, and calls herself "Grandma Noel" on her Sunday-morning chats. [Official NO1] [Observed NO2 §Personality,
secondary; NO4 titles]

## Behavioral Traits
1. Muscle puns everywhere: "Konbanmassuru~" ("Good Musclevening~"), "Ohamassuru" for mornings, her Sunday-morning
   chat show "Sunday Muscle" ("Sanma" for short). [Observed NO2 caption, secondary; NO4 titles]
2. Calls herself "Danchou" (the commander) and her viewers "danin-san" (members of her knight order). [Observed
   NO2 nickname, secondary; NO4 titles] [ASR NO20]
3. Clumsy, wholesome, "rarely seen actually doing well" at games, and still plays them all the way through (a first
   playthrough of Dragon Quest VII Reimagined in 2026; Undertale's 10th anniversary in 2025). [Observed NO2
   §Personality, secondary; NO4 titles]
4. Devoted to Shiranui Flare ("NoeFure"): she gets jealous in jest whenever Flare plays with someone else.
   [Observed NO2 §Personality, secondary]
5. A drinking-talk collab series, "#今夜はノエルと吞まKnight" ("Drinking Knight with Noel tonight"), with fellow
   members. [NO4 titles]
6. An alter ego, "Noel Deluxe," voiced through a voice changer in a deep, masculine register. [Observed NO2
   §Miscellaneous, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "All hustle, all muscle! Shirogane Noel's here!" [Official NO1]
  - Evening greeting: "Konbanmassuru~" ("Good Musclevening~"). [Observed NO2 caption, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "-massuru" endings (konbanmassuru, ohamassuru) → greetings. [Observed NO2; NO4 titles]
  - "Danchou" → herself. [NO4 titles] [ASR NO20]
  - Old-fashioned sentence endings when she narrates the week: 「まぁ色々ありましたな」 ("well, a lot happened").
    [ASR NO20]
- **Vocabulary / fillers:** "sō," "nē," "nanka," a drawn-out "un"; see research/audio-check/noel.md. [ASR NO20]
- **Profanity:** essentially none; cheerful. [ASR NO20]
- **Language:** streams in Japanese; with the English cast she was Kiara's 22nd HOLOTALK guest (2022) and joined
  Calli's HOLOYOI with Flare (2023). [NO5]
- **Laughs, noises:** a bright, bubbly laugh; flustered yelps in games. [ASR NO20]
- **Rhythm & rhetoric:** chatty and meandering on morning chats, organizing the week aloud ("first, this week's
  story…"), then excited run-ons. [ASR NO20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (NO20): in a 2026 morning chat window, median about 283 Hz (p10–p90 about 213–462 Hz, 13
    semitones) and about 267 characters a minute of speech; see research/audio-check/noel.md. Measurements
    describe the archived audio, not a target to clone.
  - Provisional (interpretation): a soft, girlish, warm voice, higher than her knight's armor suggests; bubbly and
    eager, with a mature "older sister" register she can switch on.
- **Sounds off:** a gruff warrior bark (outside the "Noel Deluxe" bit); cold or aloof delivery; a sultry voice.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, hearty | "All hustle, all muscle!" (NO1) |
| Recapping the week | Chatty, old-fashioned | 「まぁ色々ありましたな」 (mā iroiro arimashita na, "well, a lot happened, I'd say") (ASR NO20) |
| Recommending a game | Eager | **Style demo:** "Zehi minna mo yatte mite!" ("You all should try it too!") |
| Losing a game | Flustered, wailing | **Style demo:** "Danchou no kinniku ga tarinakatta…!" ("Danchou's muscles weren't enough…!") |
| Flare with someone else | Mock-jealous | **Style demo:** "Furea wa danchou no da yo!?" ("Flare is mine, you know!?") |
| Older-sister mode | Lower, gentle | (Observed NO2) |

### Sample Lines
1. "All hustle, all muscle! Shirogane Noel's here!" (Official NO1)
2. 「まぁ色々ありましたな」 (mā iroiro arimashita na, "well, a lot happened, I'd say") (ASR NO20, June 2026)

## Appearance Anchors (avatar)
- 158 cm; illustrator Watao. Shoulder-length silver hair with a braid, a black-and-gold metal headband and green
  eyes. A knight's outfit: black armor with gold edging on one shoulder and both arms, fingerless gloves, a long
  white surcoat with navy trim and a heraldic front panel, brown leather belts and pouches, and armored steel
  boots; she carries a flanged mace. Emoji ⚔️. [Official NO1 key art, described by Claude] [Observed NO2
  §Appearance, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2019-08-08 | Debut, hololive 3rd generation (hololive Fantasy) | [Official NO1] |
| 2019-11-17 | 3D debut, the first of her generation | [Observed NO2] |
| 2022 | Originals "Lyrical Monster" and "Ours"; Kiara's 22nd HOLOTALK guest (03-05) | [Observed NO2] [NO5] |
| 2023 | Calli's HOLOYOI #02 with Flare (04-20); first solo album "NOESANPO" (11-24); "Yuru Holo" team Mario Kart with FUWAMOCO and Bae (12-12) | [NO5] [Observed NO2] |
| 2025-02-18 | 2 million subscribers | [Observed NO2] |
| 2025 | Gartic Phone with Mumei and others (04-14); 3rd-gen R.E.P.O.; Elden Ring Nightreign with Flare and Pekora; FUWAMOCO danced to her song "Très Bien Night" | [NO4] [NO5] |
| 2026-01-17 | hololive Fantasy concert "#OperationHeartfulCuties," K-Arena Yokohama | [Observed NO2] |
| 2026-08-15 | Original song "KAGAMI YO KAGAMI" | [Observed NO2] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Houshou Marine | hololive Fantasy; "Onee-san Gumi" with Flare; "Yakamashi Musume" | 3rd-gen R.E.P.O. (2025); Yakamashi drinking-talk collabs | [NO2] [NO4] |
| Yukihana Lamy | "Yakamashi Musume" with Korone and Marine | Drinking-talk collabs (2025) | [NO2] [NO4] |
| Hoshimachi Suisei | "Shiranui Kensetsu" (Shiraken) | A Minecraft construction company with Flare, Polka and Miko | [NO2] |
| Nakiri Ayame | — | An Audio-Technica earphone collab (2025) | [NO4] |
| Hakui Koyori | — | "NoeKoyo" baseball exhibition (2025); Blue Journey (2023) | [Koyori file] |
| Kikirara Vivi | — | Gartic Phone (2025) | [NO5] |
| Takanashi Kiara | — | Her 22nd HOLOTALK guest (2022) | [NO5] |
| Mori Calliope | — | HOLOYOI #02 with Flare (2023) | [NO5] |
| FUWAMOCO, Hakos Baelz | — | "Yuru Holo" team Mario Kart (2023); FUWAMOCO danced to "Très Bien Night" (2025) | [NO5] |
| Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii, Elizabeth Rose Bloodflame | — | Gartic Phone EN + ID + JP (2025) | [NO5] |
| Ceres Fauna (graduated) | EN kouhai | Named her as a JP senior she admires and wanted to collab with | [Fauna file, secondary] |

## Arc
- **Starting point:** active at the 2026 baseline: past 2 million subscribers, a hololive Fantasy concert and a
  new original song behind her.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a muscle-first plan for a puzzle; jealousy whenever Flare collabs with someone; a game she
  will not stop losing.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Noel offers to be Kiara's bodyguard knight at a concert and gets lost backstage.
  2. "Drinking Knight with Noel" welcomes Calli as a guest and turns into a cooking contest.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.) Her devotion to Flare is a comedy bit; keep it as banter.

## Hard Facts (continuity)
- Debut 2019-08-08; hololive 3rd generation (hololive Fantasy); birthday 24 November; 158 cm; illustrator Watao;
  fans Knight's Order of Shirogane (Shirogane kishidan); stream tag #ノエルーム; fan-art tag #ノエラート.

## Sources (checked 2026-10-02)
- NO1 Official profile: https://hololive.hololivepro.com/en/talents/shirogane-noel/ (text and key art)
- NO2 Shirogane Noel wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Shirogane_Noel
- NO4 Stream archive metadata, her channel (archive.ragtag.moe): 99f7sLRAHHM (morning chat, 2026-06-28),
  TrrD5iQGCGA (Dragon Quest VII Reimagined, 2026-06-27), ND9xvoFNPUQ (3rd-gen R.E.P.O.), nuiqLHQA7k8 (Yakamashi
  collab), cpUnHgEveX8 (with Ayame), 2H6xlm11JvE and 55LUti59pmI (with Flare and Pekora), 4dWw6EHi8Cg, LIwx6lGRLRs
- NO5 Other members' archive metadata: toe_PmrDWBU (Kiara), wyrLR1CC1Co (Calli), Janl2FCKmsg (FUWAMOCO),
  Evg-T2BUIDM (Bae), 8RjOCCH2sac (FUWAMOCO short), OMDzBQohAf8 (Mumei)
- NO20 Claude's audio check (two-model ASR, Japanese): research/audio-check/noel.md

---

## [SW] Name
Shirogane Noel

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 3rd generation, hololive Fantasy, Onee-san Gumi, NoeFure, Shiranui Kensetsu, Yakamashi Musume

## [SW] Other Names
Noel, Danchou, Noel-danchou, Noel Deluxe (alter ego)

## [SW] Personality
Noel is hololive Fantasy's silver-haired knight, the "Danchou" (commander) of her viewers' knight order: easy-going and fluffy, but with the dangerous habit of trying to solve every problem with muscle, and in her lore she came to the VTuber world to train among the "stronk." She is clumsy and wholesome, rarely good at the games she loves and determined to finish them anyway, with a cheerful, girlish voice that surprises people who expect a warrior and a gentler older-sister register she can switch on. She puns on muscle in every greeting ("Good Musclevening~"), recaps her week on a Sunday-morning chat show, jokes about being "Grandma Noel," and hosts a drinking-talk collab series with friends. Her devotion to her partner Shiranui Flare is a long-running bit: she gets jealous whenever Flare plays with someone else.

## [SW] Background
Noel is an active member of hololive's 3rd generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2019-08-08 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Houshou Marine, and was the first of her generation to get a 3D model (2019). She released the originals "Lyrical Monster" and "Ours" (2022), her first album "NOESANPO" (2023) and "KAGAMI YO KAGAMI" (2026), passed 2 million subscribers in 2025, and sang at hololive Fantasy's "#OperationHeartfulCuties" concert (2026). With the English cast she was Kiara's 22nd HOLOTALK guest (2022), joined Calli's HOLOYOI with Flare (2023), raced FUWAMOCO and Bae in a team Mario Kart event (2023) and played Gartic Phone with Mumei, Ina, Kronii and Elizabeth (2025); FUWAMOCO danced to her song "Très Bien Night."

## [SW] Physical Description
Noel's avatar is 158 cm tall, with shoulder-length silver hair, a braid, a black-and-gold metal headband and green eyes. She wears black, gold-edged armor on one shoulder and both arms, a long white surcoat with navy trim and a heraldic panel, leather belts and pouches, and armored steel boots, and carries a flanged mace.

## [SW] Dialogue Style
Streams in Japanese in a cheerful, chatty, girlish voice, calling herself "Danchou" and her viewers "danin-san." She puns on muscle ("Konbanmassuru~," "Ohamassuru"), recaps her week with old-fashioned endings ("well, a lot happened, I'd say"), recommends games eagerly, wails when she loses and mock-pouts when Flare plays with others. When a story renders her speech in English or Chinese, keep the muscle puns, the "Danchou" self-reference and the soft voice under the armor.

## [SW] Catchphrases
"All hustle, all muscle! Shirogane Noel's here!" (official); "Konbanmassuru~" ("Good Musclevening~"); "Ohamassuru" (good morning); "Danchou" (herself, the commander); "danin-san" (her knights, the viewers); "Sunday Muscle" (her Sunday-morning chat).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a soft, girlish, warm voice, higher than her armor suggests; bubbly and eager in chat, flustered and wailing when she loses, with a lower, gentle older-sister register available. A deep, masculine voice belongs only to her "Noel Deluxe" bit. Never gruff, cold or sultry by default.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, girlish, warm voice. Default tags: [cheerful, warm]. By situation: greeting [hearty, bright]; recapping the week [chatty, relaxed]; recommending something [eager]; losing a game [flustered, wailing]; Flare with someone else [mock-jealous, pouty]; older-sister mode [gentle, lower]. With people (proposed scene directions, not observed conversational defaults): Flare [doting]; Marine [bickering, playful]; Pekora [competitive]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Konbanmassuru~" (spoken); [laughs] (tag only). Keep in the words: "Danchou," "massuru," "danin-san." Reading guide (untested): しろがね のえる; だんちょう. Not as default: a gruff warrior or a cold voice.

## [SW] Motivation
In her lore, Noel came to the VTuber world to train and grow stronger. As a streamer she wants to have fun with her knights and her friends, keep improving as a singer and keep Flare close.

## [SW] Relationships
Houshou Marine: hololive Fantasy, "Onee-san Gumi" with Shiranui Flare and "Yakamashi Musume"; 3rd-gen R.E.P.O. (2025). Yukihana Lamy: "Yakamashi Musume" with Inugami Korone and Marine; drinking-talk collabs. Hoshimachi Suisei: "Shiranui Kensetsu" (Shiraken), the Minecraft construction company with Flare, Omaru Polka and Sakura Miko. Nakiri Ayame: an earphone sponsorship collab (2025). Hakui Koyori: "NoeKoyo" baseball (2025) and Blue Journey (2023). Kikirara Vivi: Gartic Phone (2025). Takanashi Kiara: her 22nd HOLOTALK guest (2022). Mori Calliope: HOLOYOI #02 with Flare (2023). FUWAMOCO and Hakos Baelz: a team Mario Kart event (2023); FUWAMOCO danced to "Très Bien Night" (2025). Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone EN + ID + JP (2025). Shiranui Flare: her partner ("NoeFure"). Ceres Fauna (graduated 2025): an EN kouhai who, by secondary accounts, admired her and hoped to collab.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Shirogane Noel): official profile and
  key art (NO1), wiki (NO2, by section; body talk, school nickname, birthplace, pets, lessons and the rings with
  Flare deliberately excluded), archive metadata (NO4, NO5) and Claude's two-model Japanese audio check (NO20,
  research/audio-check/noel.md).

## Open Questions
1. "Très Bien Night" is read from FUWAMOCO's short title ("トレビアンナイト"); confirm the official English title.


## Audio report: research/audio-check/noel.md

# Audio check — Shirogane Noel (2026-10-02)

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
| chat25_2026 | [【朝活雑談】6月といえばジューンブライド...だんちょを貰ってください(圧)【白銀ノエル/ホロラ](https://youtu.be/99f7sLRAHHM) | [0:05:00–0:30:00](https://youtu.be/99f7sLRAHHM?t=300) | 20.4 | 5446 | 266.9 | 283 Hz | 213–462 Hz |
| dq20_2026 | [#9【ドラゴンクエストVII Reimagined】DQ7完全初見！ずっとプレイしてみたかった7](https://youtu.be/TrrD5iQGCGA) | [0:10:00–0:30:00](https://youtu.be/TrrD5iQGCGA?t=600) | 14.8 | 4667 | 314.3 | 260 Hz | 119–448 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat25_2026 | dq20_2026 |
|---|---|---|
| first person 余 (yo) | 0 | 2 |
| first person 僕 (boku) | 0 | 2 |
| first person 私 | 0 | 10 |
| なんか | 36 | 12 |
| まあ | 13 | 6 |
| ちょっと待って | 0 | 1 |
| やばい | 1 | 2 |
| かわいい | 1 | 2 |
| えっ/え? | 1 | 5 |
| laugh (はは/ふふ/笑) | 0 | 1 |
| ありがとう | 4 | 1 |
| English (Latin letters) | 0 | 1 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Recaps her week on the Sunday-morning chat | **Observed**: 「今週ね、何があったかと言いますと、まぁ色々ありましたな」, then "as much as I can share." | [0:05:28](https://youtu.be/99f7sLRAHHM?t=328) |
| Calls herself "Danchou" | **Observed** (the first model writes 「男帳」/「男長」, so no line with it is quoted). | [0:06:23](https://youtu.be/99f7sLRAHHM?t=383) |
| Recommends games eagerly | **Observed**: 「いやぜひみなさんもやってみて欲しい」 ("really, I want you all to try it too"). | [0:08:52](https://youtu.be/99f7sLRAHHM?t=532) |
| First playthrough of Dragon Quest VII Reimagined | **Observed** (2026). | [0:11:00](https://youtu.be/TrrD5iQGCGA?t=660) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "まぁ色々ありましたな" | [0:05:28](https://youtu.be/99f7sLRAHHM?t=328) | "…と言いますとまぁ色々ありましたなまぁ色々あり…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いやぜひみなさんもやってみて欲しい" | [0:08:52](https://youtu.be/99f7sLRAHHM?t=532) | "…しかったからいや ぜひ みなさんもね やってみ…" | **Partial (computed):** shared run "いやぜひみなさんも"; only that part is quoted |
| "今週ね、何があったかと言いますと、まぁ色々ありましたな" | [0:05:28](https://youtu.be/99f7sLRAHHM?t=328) | "…ぁ今週ねまぁ何があったかと言いますとまぁ色々ありましたなまぁ色々あり…" | **Partial (computed):** shared run "何があったかと言いますとまあ色々ありましたな"; only that part is quoted |


## Performance sheet: export/elevenlabs/Shirogane-Noel.md

# ElevenLabs v4 Performance Sheet: Shirogane Noel

> Built from `bible/characters/Shirogane-Noel.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Noel is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft, girlish, warm voice, higher than her armor suggests; bubbly and eager in chat, flustered and wailing when she loses, with a lower, gentle older-sister register available."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (warm, with flustered swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, warm]` or `[chatty, relaxed]`; v4 has no speed slider.

## 3. Write these habits into the script
- Calls herself "Danchou" (commander) and her viewers "danin-san"; muscle puns ("Konbanmassuru~," "Good Musclevening~").
- Recaps her week in old-fashioned phrasing: 「まぁ色々ありましたな」 ("well, a lot happened, I'd say").
- Eager recommendations; mock jealousy over Flare.
- A deep, masculine voice belongs only to her "Noel Deluxe" bit; never as a default.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[hearty, bright]` | "Konbanmassuru~" (secondary transcription) |
| Recapping the week | `[chatty, relaxed]` | 「まぁ色々ありましたな」 ("Mā iroiro arimashita na") |
| Recommending something | `[eager]` | **Style demo:** "Zehi minna mo yatte mite!" ("You all should try it too!") |
| Losing a game | `[flustered, wailing]` | **Style demo:** "Danchou no kinniku ga tarinakatta…!" ("Danchou's muscles weren't enough…!") |
| Flare with someone else | `[mock-jealous, pouty]` | **Style demo:** "Furea wa danchou no da yo!?" ("Flare is mine, you know!?") |
| Older-sister mode | `[gentle, lower]` | **Style demo:** "Daijōbu, yukkuri de ii kara ne." ("It's okay, take your time.") |

With people (proposed scene directions, not observed conversational defaults): Flare `[doting]`; Marine `[bickering, playful]`; Pekora `[competitive]`.

## 5. Signature sounds
- "Konbanmassuru~" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): しろがね のえる; だんちょう; こんばんまっする. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior; a cold or sultry default; the deep "Noel Deluxe" voice outside that bit.

## 8. Example
```
[hearty, bright] Konbanmassuru~!
[chatty, relaxed] Mā, iroiro arimashita na.
[eager] Zehi minna mo yatte mite!
[flustered, wailing] Danchou no kinniku ga tarinakatta…!
```
(Line 1 is her greeting as a secondary transcription; line 2 is her line, quoted only where both transcripts
agree; lines 3–4 are style demos.)


## Card 3: Yukihana Lamy (draft, full file)

---
kind: character
name: "Yukihana Lamy"
sw_section: Characters
---

# Character File: Yukihana Lamy

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Lamy is an active hololive member
> (Japan, 5th generation) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02). Her recent
> streams (2026) set her default manner, per the project's recency rule. Nothing about the performer behind the
> avatar: private-life information (family, home, health, daily routine, pets, personal skills and ranks, drinking
> amounts, body talk and the like) is outside scope and is not recorded here, including what she mentions in chats
> and what the wiki lists. She streams in Japanese; that is recorded as the language of her performance only. In
> stories she knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence
> labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; LM20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (LM#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (LM20: a June 2026 evening "banshaku"
> chat and a June 2026 village-life game stream; see research/audio-check/lamy.md). Personal remarks are not
> quoted or summarized here. The audio was machine-transcribed and acoustically measured; transcripts were
> reviewed in context, without independent listening verification.

## One-line Concept
"Lamyoohoo!": hololive's 5th-generation snow elf, a noblewoman from a land of endless snow who left home with
her little snow spirit Daifuku because hololive's streams made her smile; gentle and motherly ("Lamy-mama"),
with a polite, refined voice that slides into cheerful, rough-edged banter over an evening drink with her chat.
[Official LM1] [Observed LM2 §Personality, secondary]

## Core Drive
- **Want (official goals):** to take on every challenge, even things she is not good at; to give hololive a real
  boost; to stand on the same stage as her senpai; to reach a million subscribers. [Official LM1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror (her horror playthroughs with Botan, who enjoys her reactions); she can
  be bold and assertive when it matters. [Observed LM2 §Personality, secondary]
- **Values shown in public:** kindness and empathy toward members and fans; sharing a toast with her Yukimin at
  the end of a week. [Observed LM2] [ASR LM20]

## Core Contradiction
A "pure and all-loving," soft-spoken noble snow elf, first billed as one of hololive's most "seiso" members, who
became famous for evening-drink streams, her own collaboration sake ("Yukiyozuki") and a cheerful "umē!" ("so
good!") between refined sentences. [Official LM1] [Observed LM2 §Personality, secondary; LM4 titles] [ASR LM20]

## Behavioral Traits
1. Refers to herself as "Lamy" and mixes formal politeness ("o-tsukaresama de gozaimashita") with casual,
   casual slang ("hona," "chū koto de," "umē") as a chat warms up. [ASR LM20]
2. Hosts "banshaku" (evening-drink) chat streams: she presents her snacks, toasts chat ("kanpai") and talks
   through the week. [LM4 titles] [ASR LM20]
3. Gentle and motherly ("Lamy-mama"), shy and easily flustered at first, then surprisingly bold. [Observed LM2
   §Personality, secondary]
4. Horror with Shishiro Botan: Lamy panics while Botan, acting the protective partner, quietly enjoys the
   reactions. [Observed LM2 §Personality, secondary]
5. Many units and pairs: NePoLaBo (with Botan, Omaru Polka and Momosuzu Nene), KALAZ (with Amane Kanata and
   AZKi), KoZMy (with AZKi and Koyori), "Magamaga's" (with Nene), "Yakamashi Musume," holoWitches. [Observed LM2
   §Relationships, secondary]
6. Cozy, slow-life games (a village life sim, Pokopia) alongside group server events. [LM4 titles]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "Lamyoohoo!" [Official LM1]
  - Opening (wiki): "Konlamy desu." [Observed LM2 caption, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Lamy" in the third person → constant. [ASR LM20]
  - The toast: 「とりあえず、乾杯しないと何も始まらない」 ("nothing starts until we toast first") → banshaku streams.
    [ASR LM20]
  - "Yukimin" → her fans. [Official LM1]
- **Vocabulary / fillers:** "sā," "nē," "mā mā mā," "umē"; see research/audio-check/lamy.md. [ASR LM20]
- **Profanity:** mild, casual ("umē," rough endings) rather than swearing. [ASR LM20]
- **Language:** streams in Japanese; with the English cast she joined Ina's Minecraft festivals and server "date"
  (2021) and appeared at Ina's 2024 3D live. [LM5]
- **Laughs, noises:** a soft, airy giggle; flustered squeaks in horror. [ASR LM20] [Observed LM2]
- **Rhythm & rhetoric:** quick, chatty and warm (about 332 characters a minute of speech in an evening chat),
  moving between polite set phrases and casual asides. [ASR LM20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (LM20): in a 2026 evening chat window, median about 303 Hz with a very wide p10–p90 span (about
    132–472 Hz; the low end likely includes non-speech sound) and about 332 characters a minute of speech; see
    research/audio-check/lamy.md. Measurements describe the archived audio, not a target to clone.
  - Provisional (interpretation): a soft, bright, gentle voice with a refined, polite surface; quick and cheerful
    in banter, breathy and squeaky when scared.
- **Sounds off:** a cold "ice queen"; harsh or aggressive delivery; a slurred drunk caricature.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, sweet | "Lamyoohoo!" (LM1) |
| Toast | Warm, formal-cheerful | 「今週も、皆様、お疲れ様でございました」 (konshū mo, minasama, otsukaresama de gozaimashita, "thank you all for your hard work this week too") (ASR LM20; same reading in both models) |
| Banshaku banter | Quick, casual | 「とりあえず、乾杯しないと何も始まらない」 (toriaezu, kanpai shinai to nani mo hajimaranai, "nothing starts until we toast first") (ASR LM20) |
| Horror | Panicked, squeaky | [gasps] |
| Motherly | Gentle, soft | **Style demo:** "Daijōbu, Lamy ga tsuiteru kara ne." ("It's all right, Lamy's here with you.") |

### Sample Lines
1. "Lamyoohoo!" (Official LM1)
2. 「とりあえず、乾杯しないと何も始まらない」 (toriaezu, kanpai shinai to nani mo hajimaranai, "nothing starts until
   we toast first") (ASR LM20, June 2026)

## Appearance Anchors (avatar)
- 158 cm; illustrator Rin☆Yuu. Long light-blue hair with a heart-shaped ahoge and small side braids, pointed elf
  ears, golden eyes, a white beret with a blue snow flower (the "Tweeur" of her homeland, per the wiki). A white
  blouse with a blue ribbon, a light-blue fur-trimmed coat with snowflake patterns worn off the shoulders, a brown
  belt, a white skirt fading to blue at the hem, white thigh-highs with snow patterns and brown boots. Her
  companion is Daifuku, a little snow spirit like a polar bear in a pot. [Official LM1 key art, described by
  Claude] [Observed LM2 §Trivia, §Mascot, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2020-08-12 | Debut, hololive 5th generation | [Official LM1] |
| 2021 | Ina's Usaken Summer Festival (06-27) and an EN-server Minecraft "date" with Ina (10-20) | [LM5] |
| 2023 | "Blue Journey" music project with Marine, Noel, Koyori and Sakura Miko | [Koyori file; Observed LM2] |
| 2024 | Originals "Hatsukoi Pâtissière," "Watashi wo amayakasunara" and "Lamy's Baribari Workout"; a guest at Ina's 3D live "Pleides" (12-28) | [Observed LM2] [LM5] |
| 2025 | Joins "Magical Girl holoWitches!" (04–05); "Yoppara Music!" (08-12); KoZMy with AZKi and Koyori (08) | [Observed LM2] [Koyori file] |
| 2026 | Her collaboration sake "Yukiyozuki" (04); a NePoLaBo 3D party (04-29); NePoX events with holoX announced for 09-26/27; "Snowlight Stories" (08-12) | [LM4] [Observed LM2] |
| 2026-08-15 | First album "Fleur de neige" announced for 2027-01-27 (after the baseline) | [Observed LM2] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Shishiro Botan | 5th-gen genmate; NePoLaBo | Horror playthroughs; NePoLaBo 3D and R.E.P.O. | [LM2] [LM4] |
| AZKi | "KALAZ" with Amane Kanata; "KoZMy" | Units with AZKi | [LM2] |
| Hakui Koyori | "KoZMy"; "RamiKoyo" | An off-collab banshaku to name their duo (2026); KoZMy horror (2025) | [LM4] [Koyori file] |
| Houshou Marine, Shirogane Noel | "Yakamashi Musume" with Inugami Korone; Blue Journey | Yakamashi talk collabs | [LM2] [Noel file] |
| Houshou Marine | holoWitches | — | [LM2] |
| La+ Darknesss, Takane Lui, Kazama Iroha | NePoX | NePoLaBo × holoX events (2026) | [LM2] [LM4] |
| Kazama Iroha | — | Caravan Stories (2023) | [Iroha file] |
| Sakamata Chloe (affiliate) | — | Rust with Kanata (2022) | [Chloe file] |
| Ninomae Ina'nis | — | Minecraft festivals and an EN-server "date" (2021); a guest at Ina's "Pleides" 3D live (2024) | [LM5] |

## Arc
- **Starting point:** active at the 2026 baseline: six years in, a ninth original song out and a first album
  announced.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a horror game she should not play; an evening toast that turns into a confession session;
  a kind gesture taken too far ("yandere" jokes, secondary).
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Lamy hosts a "Snack Yuki no Hana" night and Ina draws the regulars.
  2. Botan drags Lamy through a haunted house while pretending not to enjoy her screams.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.) Drinking appears only as her public evening-chat format; never a caricature.

## Hard Facts (continuity)
- Debut 2020-08-12; hololive 5th generation; birthday 15 November; 158 cm; illustrator Rin☆Yuu; fans Yukimin
  (Snowfolk); companion Daifuku (a snow spirit); stream tag #らみらいぶ; fan-art tag #らみあーと.

## Sources (checked 2026-10-02)
- LM1 Official profile: https://hololive.hololivepro.com/en/talents/yukihana-lamy/ (text and key art)
- LM2 Yukihana Lamy wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Yukihana_Lamy
- LM4 Stream archive metadata, her channel (archive.ragtag.moe): bquezhdXu2E (banshaku chat, 2026-06-06),
  d2u2FOBGhy4 (village-life game, 2026-06-26), Zi8R63ee0Fs (with Koyori), Ekdsnb2aWY4 (Yukiyozuki),
  ua8QKKIXT2s and nLlJdgzrAHI (NePoLaBo), Ml1tM8S40p0 (NePoX), HOI03J67R5Q (with Nene), 1JcWpl-I_QM (with Noel)
- LM5 Other members' archive metadata: a7CvRf4vFYc, Isp3UhgOAB4, 3n9igJnSXtQ (Ina)
- LM20 Claude's audio check (two-model ASR, Japanese): research/audio-check/lamy.md

---

## [SW] Name
Yukihana Lamy

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 5th generation, NePoLaBo, KALAZ, KoZMy, Yakamashi Musume, holoWitches, NePoX, Blue Journey

## [SW] Other Names
Lamy, Lamy-mama, Wamy

## [SW] Personality
Lamy is a snow elf from a noble family in a land of endless snow, who left home with her little snow spirit Daifuku after hololive's streams made her smile; her official profile says her serious facade hides a clueless, sheltered side. Fans call her "pure and all-loving" and "Lamy-mama": she is soft-spoken, kind and empathetic, shy and easily flustered at first, then surprisingly bold. She calls herself "Lamy," mixes refined politeness with cheerful, casual slang as a chat warms up, and hosts evening-drink chats where she shows her snacks, toasts her Yukimin and talks through the week; she even has her own collaboration sake. She panics through horror games, especially with Shishiro Botan, loves cozy slow-life games, and sets herself challenges, including things she is not good at.

## [SW] Background
Lamy is an active member of hololive's 5th generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2020-08-12 in hololive's 5th generation with Shishiro Botan, Omaru Polka and Momosuzu Nene (with whom she forms NePoLaBo). She sang in the "Blue Journey" project with Marine, Noel, Koyori and Sakura Miko (2023), joined "Magical Girl holoWitches!" (2025), formed KoZMy with AZKi and Koyori (2025) and is in KALAZ with Amane Kanata and AZKi. Her originals include "Hatsukoi Pâtissière" (2024), "Yoppara Music!" (2025) and "Snowlight Stories" (2026), and her first album, "Fleur de neige," was announced for January 2027. With the English cast she joined Ninomae Ina'nis's Minecraft festivals (2021) and appeared at Ina's 3D live "Pleides" (2024).

## [SW] Physical Description
Lamy's avatar is 158 cm tall, with long light-blue hair, a heart-shaped ahoge, small side braids, pointed elf ears and golden eyes, under a white beret with a blue snow flower. She wears a white blouse with a blue ribbon, a light-blue fur-trimmed coat patterned with snowflakes worn off the shoulders, a brown belt, a white skirt fading to blue, snow-patterned white thigh-highs and brown boots. Daifuku, a tiny polar-bear-like snow spirit in a pot, keeps her company.

## [SW] Dialogue Style
Streams in Japanese in a soft, polite voice, calling herself "Lamy": formal set phrases ("thank you all for your hard work this week too") slide into quick, casual banter and a satisfied "so good!" over her snacks, and every evening chat starts with a toast ("nothing starts until we toast first"). Shy and flustered at first, then bold; squeaking in horror. When a story renders her speech in English or Chinese, keep the third-person "Lamy," the polite-to-casual slide and her warmth; never play her as a drunk caricature.

## [SW] Catchphrases
"Lamyoohoo!" (official); "Konlamy desu" (her greeting, wiki-recorded); "Lamy" (herself); "kanpai!" and "nothing starts until we toast first" (her evening chats); "Yukimin" (her fans, the Snowfolk).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a soft, bright, gentle voice with a refined, polite surface, quick and cheerful in banter, motherly and soothing when comforting someone, breathy and squeaky when scared. Never cold, harsh or a slurred caricature.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, bright, gentle voice. Default tags: [gentle, cheerful]. By situation: greeting [sweet, bright]; toast [warm, formal]; banter [casual, quick]; comforting [motherly, soft]; horror [panicked, squeaky]; flustered [shy]. With people (proposed scene directions, not observed conversational defaults): Botan [clingy, scared]; Koyori [giggly]; Nene [playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "Kanpai!" (spoken); [giggles] (tag only); [gasps] (tag only). Keep in the words: "Lamy," "Yukimin," "kanpai." Reading guide (untested): ゆきはな らみぃ. Not as default: a cold or harsh voice, or slurred speech.

## [SW] Motivation
In her lore, Lamy left her snowy home to bring the smiles she found in hololive's streams to others. As a streamer she wants to take on every challenge, give hololive a boost, stand on stage with her senpai and keep her Yukimin company.

## [SW] Relationships
Shishiro Botan: 5th-gen genmate and NePoLaBo partner; horror runs where Lamy panics and Botan enjoys it. AZKi: "KALAZ" with Amane Kanata and "KoZMy" with Hakui Koyori. Hakui Koyori: KoZMy (2025) and a 2026 off-collab to name their duo. Houshou Marine and Shirogane Noel: "Yakamashi Musume" with Inugami Korone, and Blue Journey; Marine is also in holoWitches. La+ Darknesss, Takane Lui and Kazama Iroha: NePoX, NePoLaBo × holoX events. Ninomae Ina'nis: Minecraft festivals and a server "date" (2021), and a guest at Ina's 3D live "Pleides" (2024). Sakamata Chloe (affiliate): Rust with Amane Kanata (2022).

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Yukihana Lamy): official profile and
  key art (LM1), wiki (LM2, by section; body talk, family lore, personal skills and drinking amounts deliberately
  excluded), archive metadata (LM4, LM5) and Claude's two-model Japanese audio check (LM20,
  research/audio-check/lamy.md).

## Open Questions
1. The wiki's caption gives "Konlamy desu" while the official site gives "Lamyoohoo!"; keep both?


## Audio report: research/audio-check/lamy.md

# Audio check — Yukihana Lamy (2026-10-02)

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
| banshaku25_2026 | [【晩酌】雪夜月で晩酌、しちゃう…？♡【雪花ラミィ /ホロライブ】](https://youtu.be/bquezhdXu2E) | [0:05:00–0:30:00](https://youtu.be/bquezhdXu2E?t=300) | 17.8 | 5905 | 332.1 | 303 Hz | 132–472 Hz |
| village20_2026 | [【ぷちホロの村 - 剣とお店と田舎暮らし】魔法使いラミィの、のんびり田舎暮らし！！【雪花ラミィ ](https://youtu.be/d2u2FOBGhy4) | [0:10:00–0:30:00](https://youtu.be/d2u2FOBGhy4?t=600) | 14.2 | 2359 | 166.5 | 261 Hz | 110–497 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | banshaku25_2026 | village20_2026 |
|---|---|---|
| first person 余 (yo) | 0 | 1 |
| first person 私 | 1 | 0 |
| なんか | 20 | 7 |
| まあ | 7 | 3 |
| ちょっと待って | 1 | 4 |
| やばい | 0 | 1 |
| かわいい | 5 | 0 |
| えっ/え? | 0 | 2 |
| swear (くそ/ふざけ/殺) | 3 | 0 |
| ありがとう | 2 | 0 |
| English (Latin letters) | 8 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Evening-drink chat format with a toast | **Observed**: 「とりあえず、乾杯しないと何も始まらない」 ("nothing starts until we toast first"), then 「今週も、皆様、お疲れ様でございました」. | [0:06:04](https://youtu.be/bquezhdXu2E?t=364), [0:06:35](https://youtu.be/bquezhdXu2E?t=395) |
| Third-person "Lamy" | **Observed** (two dozen times in the evening window; the first model spells it variously). | [0:05:45](https://youtu.be/bquezhdXu2E?t=345) |
| Polite set phrases sliding into casual slang | **Observed**: formal "o-tsukaresama de gozaimashita" alongside "hona," "chū koto de," "umē." | [0:06:28](https://youtu.be/bquezhdXu2E?t=388) |
| Cozy slow-life games | **Observed**: a village-life game in which she plays a wizard. | [0:11:40](https://youtu.be/d2u2FOBGhy4?t=700) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "乾杯しないと何も始まらない" | [0:06:04](https://youtu.be/bquezhdXu2E?t=364) | "…なとりあえず乾杯しないと何も始まらないということで…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "今週も、皆様、お疲れ様でございました" | [0:06:35](https://youtu.be/bquezhdXu2E?t=395) | "…おつかれさまでございましたほな、乾杯で…" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "とりあえず、乾杯しないと何も始まらない" | [0:06:04](https://youtu.be/bquezhdXu2E?t=364) | "…ようぜみんなとりあえず乾杯しないと何も始まらないということで…" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/Yukihana-Lamy.md

# ElevenLabs v4 Performance Sheet: Yukihana Lamy

> Built from `bible/characters/Yukihana-Lamy.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lamy is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft, bright, gentle voice with a refined, polite surface; quick and cheerful in banter, motherly and soothing when comforting, breathy and squeaky when scared."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (gentle and steady; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[gentle, cheerful]` or `[casual, quick]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Lamyoohoo!" to open; "Yukimin" for her fans.
- Polite, formal-cheerful thanks: 「今週も、皆様、お疲れ様でございました」.
- A toast to start her chat streams: 「とりあえず、乾杯しないと何も始まらない」 ("nothing starts until we toast first"); keep the toast light and non-specific.
- Motherly comfort; squeaks when scared.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[sweet, bright]` | "Lamyoohoo!" (official) |
| Thanking chat | `[warm, formal]` | 「今週も、皆様、お疲れ様でございました」 ("Konshū mo, minasama, otsukaresama de gozaimashita") |
| Banter | `[casual, quick]` | 「とりあえず、乾杯しないと何も始まらない」 ("Toriaezu, kanpai shinai to nani mo hajimaranai") |
| Comforting | `[motherly, soft]` | **Style demo:** "Daijōbu, Lamy ga tsuiteru kara ne." ("It's all right, Lamy's here with you.") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Flustered | `[shy]` | **Style demo:** "Ē, sonna koto iwanaide yo~" ("Eh, don't say things like that~") |

With people (proposed scene directions, not observed conversational defaults): Botan `[clingy, scared]`; Koyori `[giggly]`; Nene `[playful]`.

## 5. Signature sounds
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




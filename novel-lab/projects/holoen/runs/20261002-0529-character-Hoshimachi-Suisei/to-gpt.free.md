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
  Nakiri Ayame and Nekomata Okayu, with their ties to the English cast. This is run A of two: Suisei and AZKi. Run B covers Ayame, Okayu, the pairs card and the English-cast lines.
- They stream in Japanese. Quotes on the cards are Japanese (with romanization and an English gloss); the audio
  reports list both models' renderings. A Japanese quote passes the gate only if the report marks it shared.
  Private life stays out (family, childhood, health, trips, daily routine, how often someone streams, breaks).
- This run must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation,
  so keep to about 15 tool calls in total, including web searches; batch local lookups. Prioritize the exported
  [SW] fields, then the dossier facts dated 2025–2026, then the sheets.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git). The new
  cards are not in `bible/`; their full text is inline below. Do not re-open the inline files.
- If the budget runs short, stop and report what you could not check in the Verification note.

## Card 1: Hoshimachi Suisei (draft, full file)

---
kind: character
name: "Hoshimachi Suisei"
sw_section: Characters
---

# Character File: Hoshimachi Suisei

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Suisei is an active hololive member
> (Japan, 0th generation) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02) for her
> ties with the English cast. Her recent streams (2026) set her default manner, per the project's recency rule.
> Nothing about the performer behind the avatar: private-life information (family, home, health, schooling,
> earlier jobs, auditions, trips, where she grew up and the like) is outside scope and is not recorded here,
> including what the wiki lists or what she mentions in chats. She streams in Japanese; that is recorded as the
> language of her performance only. In stories she knows she is a streamer with a persona (see the world card
> "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; SU20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (SU#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (SU20: two windows of a June 2026
> chatting stream, a July 2026 Rhythm Heaven stream and a June 2026 Resident Evil stream; see
> research/audio-check/suisei.md). Long stretches of the chatting stream are about personal matters (family,
> childhood, a trip) and are not quoted or summarized here. The audio was machine-transcribed and acoustically
> measured; transcripts were reviewed in context, without independent listening verification.

## One-line Concept
"A shooting star that appeared from diamonds in the rough": hololive's virtual idol, a singer who went from a
self-made indie VTuber to the Budokan and arena tours, who calls herself cute in the third person ("Sui-chan
wa~ kyō mo kawaii!"), plays Tetris and Tales games with competitive focus, and carries a running "psychopath"
joke from one ruthless game of Project Winter. [Official SU1] [Observed SU2 §Personality, secondary] [ASR SU20]

## Core Drive
- **Want:** to keep climbing as a virtual idol: her official profile sets the goal of performing at the Tokyo
  Dome one day, after she reached the Nippon Budokan (2025-02-01). [Official SU1] [Observed SU2 §2025]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** none sourced; she plays horror games (Resident Evil, Poppy Playtime) with
  focus rather than panic. [Observed SU4 titles] [ASR SU20]
- **Values shown in public:** craft and self-reliance (as an indie VTuber she drew her own original design and
  edited her own videos); staying part of hololive while running her own studio: in a June 2026 chat she
  explained that since setting up her personal agency she has said yes to members' concert invitations, so that
  nobody assumes she has stopped working with hololive members, and that she wants to appear at the lives of
  members whose stages she has not yet joined. [Observed SU2 §Miscellaneous,
  secondary] [ASR SU20, GQMY5Vl9Dfk 1:14:20–1:15:40, her own account]

## Core Contradiction
A polished, ambitious idol with a stadium-sized dream, whose fans also know her as "Suicopath": a sweet, polite
voice that sold out her friends without remorse in a game of Project Winter, a bit she happily keeps alive.
[Observed SU2 §Personality, secondary]

## Behavioral Traits
1. Calls herself cute in the third person, as a greeting and a sign-off: "Sui-chan wa~ kyō mo kawaii!" ("Sui-chan
   is cute today too!"); the line is also her shorts hashtag. [ASR SU20] [Observed SU4 titles]
2. Competitive gamer: Tetris (Tetris 99 streams; she joked she had been "a Tetris character"), two hololive Mario
   Kart tournament wins (2021, 2023), long Resident Evil and Poppy Playtime runs. [Observed SU2 §Miscellaneous,
   secondary; SU4 titles]
3. A Tales series fan who gets carried away: a June 2026 chat turned into a long Tales talk ("kore wa Teiruzu ga
   daisuki na hanashi desu," "this is a story about loving Tales"); Tales of the Abyss is her favorite, and she
   jokingly quotes its "Ore wa warukunē!" ("It's not my fault!") when she blames chat for a mistake.
   [ASR SU20]
4. Blames chat with mock innocence when chat talks her into something: "Iya iya iya, watashi wa warukunai"
   ("No, no, no, I'm not the bad one") … "Komento-ran ga yarette ittan da" ("Chat told me to do it"). [ASR SU20]
5. The "forever 18" bit lives on in chat even after her official profile dropped it (2024): asked whether she is
   of a certain generation, she answers "Sui-chan wa jūhassai da yo" ("Sui-chan is eighteen"). [Observed SU2
   §2024] [ASR SU20]
6. A builder of idol projects: "Hoshimatic Project" (practice streams, group MVs, "BEEP BEEP," 2026), her music
   unit Midnight Grand Orchestra, solo tours, a fan club and fan meetings ("Hoshiyomi Pajama Party"). [Observed
   SU2 §2023–§2026]

## Voice Profile
- **Greetings / sign-offs:**
  - Official introduction: "A shooting star that appeared from diamonds in the rough; I'm the virtual idol
    Hoshimachi Suisei!" (Japanese, as she says it on stream: "Suisei no gotoku arawareta sutā no genseki!
    Bācharu aidoru no Hoshimachi Suisei desu!"). [Official SU1] [ASR SU20, 0:04:22, first model garbled; the
    line is kept from the official profile]
  - Signature: "スイちゃんは〜今日も可愛い〜" ("Sui-chan wa~ kyō mo kawaii~," "Sui-chan is cute today too~"),
    said right after the introduction; stretched, sing-song. [ASR SU20, GQMY5Vl9Dfk 0:04:27] [Observed SU4
    hashtags]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Sui-chan wa~ kyō mo kawaii~" → greeting, praise, her shorts. [ASR SU20] [Observed SU4]
  - "Hi, honey!" → an English line she popularized in a Duolingo stream; other members copy her delivery.
    [Observed SU2 §Miscellaneous, secondary]
  - "Iya iya iya, watashi wa warukunai" … "Komento-ran ga yarette ittan da" … "Ore wa warukunē" → blaming chat
    for a mistake. [ASR SU20; both models on each span]
  - "Sui-chan wa jūhassai da yo" → the forever-18 bit. [ASR SU20]
- **Vocabulary / fillers:** "nanka," "mā," "ne," "sa"; "chotto matte" ("wait a sec"); she talks about herself
  as "Sui-chan" and uses "watashi" in plain talk; quick "e?" reactions. [ASR SU20, first-model counts in
  research/audio-check/suisei.md]
- **Profanity:** light; mock-rough boy-speech for a joke ("ore wa warukunē"), and "ore" when she talks to
  herself in a game. [ASR SU20]
- **Language:** streams in Japanese; occasional English words and lines ("Hi, honey!"); with the English cast
  she speaks Japanese with English phrases mixed in, and members like Calli address her as "senpai."
  [Observed SU2] [S1 titles]
- **Laughs, noises:** a bright, punchy "ha ha ha" when she cracks herself up; quick astonished "e?" reactions.
  [ASR SU20]
- **Rhythm & rhetoric:** quick and fluent in chat (about 330–340 transcribed characters a minute of speech),
  with stretched vowels for the sing-song signature line; she narrates her own reactions in the third person.
  [ASR SU20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (SU20; two 2026 chat windows): window medians about 245–262 Hz (p10–p90 about 162–493 Hz); in a
    2026 Resident Evil window about 268 Hz. The Rhythm Heaven window (game music and voiced cues) is not used.
    Measurements describe the sampled recording and ASR segmentation; they are not isolated vocal measurements.
  - Provisional (interpretation): a clear, bright mid-high voice, polished and confident; playful and sing-song
    for her signature line, crisp and focused when she is gaming. A listening check would still need to establish
    timbre details.
- **Sounds off:** a cold or cruel default (the "psychopath" bit is a joke, not her manner); a breathy or babyish
  idol voice; sloppy, mumbled delivery.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, polished, then sing-song | Official introduction, then "Sui-chan wa~ kyō mo kawaii~" (SU1; ASR SU20) |
| Chatting about games | Quick, enthusiastic, tangents | "Kore wa Teiruzu ga daisuki na hanashi desu." (ASR SU20) |
| Caught in a mistake | Mock-innocent, then mock-rough | "Iya iya iya, watashi wa warukunai" … "Ore wa warukunē" (ASR SU20) |
| Age joke | Breezy, firm | "Sui-chan wa jūhassai da yo." (ASR SU20) |
| Competitive game | Focused, clipped | **Style demo:** "Mō ikkai. Kondo wa kateru." ("One more. I'll win this time.") |
| With a senpai or kouhai on stage | Warm, encouraging | **Style demo:** "Daijōbu, issho ni ikō!" ("It's fine, let's go together!") |

### Sample Lines
1. "A shooting star that appeared from diamonds in the rough; I'm the virtual idol Hoshimachi Suisei!" (Official SU1)
2. "スイちゃんは〜今日も可愛い〜" — "Sui-chan wa~ kyō mo kawaii~" ("Sui-chan is cute today too~") (ASR SU20, GQMY5Vl9Dfk 0:04:27)
3. "いやいやいや、私は悪くない" — "Iya iya iya, watashi wa warukunai" ("No, no, no, I'm not the bad one") … "コメント欄がやれって言ったんだ" — "Komento-ran ga yarette ittan da" ("Chat told me to do it") (ASR SU20, 0:05:39–0:05:46; two shared spans)
4. "俺は悪くねぇ" — "Ore wa warukunē" ("It's not my fault"; a Tales of the Abyss line) (ASR SU20, 0:05:48)
5. "スイちゃんは18歳だよ" — "Sui-chan wa jūhassai da yo" ("Sui-chan is eighteen") (ASR SU20, 0:12:43)
6. "これはテイルズが大好きな話です" — "Kore wa Teiruzu ga daisuki na hanashi desu" ("This is a story about loving Tales") (ASR SU20, 0:15:45)
7. "私テイルズシリーズで一番好きですから、アビスが" — "Watashi Teiruzu shirīzu de ichiban suki desu kara, Abisu ga" ("Abyss is my favorite in the whole Tales series") (ASR SU20, 0:15:36)

## Appearance Anchors (avatar)
- 160 cm; illustrator Teshima Nari (her original design was drawn by herself). Light blue hair in a side
  ponytail, blue eyes, a dark striped blue ribbon and a black plaid cap topped with a small crown; a grey plaid
  dress uniform with a ruffled dark-blue skirt panel, asymmetrical socks and black shoes. [Official SU1]
  [Observed SU2 §Appearance, secondary]
- Her oshi mark is ☄️. Later looks include a short bob (2023), a black-and-red/white-and-blue sixth outfit with
  dragon-print coat and red-or-blue shades (2024), the "SuperNova" Budokan costume inspired by her indie-era
  design (2025), a blue crop top with white see-through sleeves and a frilled white skirt for the 2026 arena tour,
  and a second 3D main model for Studio STELLAR work (2026-08-30). [Observed SU2 §2023–§2026, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2018-03-22 | Debut as an independent VTuber (her birthday is the same date) | [Observed SU2] |
| 2019-05-19 | Joins INoNaKa Music, hololive production's music label, with AZKi | [Observed SU2; SU3, secondary] |
| 2019-12-01 | Moves to the main hololive branch; later counted in "0th generation" | [Observed SU2] |
| 2021-04-17 | Kiara's HOLOTALK, 8th guest ("cometori") | [S1 a6DjP7NYwUE] |
| 2022 | "CapSule" with Mori Calliope; single "TEMPLATE / Wicked feat. Mori Calliope"; sings "Wicked" at Calli's first solo concert (07-21) | [S1] |
| 2022-12-31 | "story time" as Star Flower with AZKi, Moona Hoshinova and IRyS | [Official SU6] |
| 2023-01-20 | First VTuber on THE FIRST TAKE ("Stellar Stellar") | [Observed SU2] |
| 2023-11 | Starts "Hoshimatic Project" | [Observed SU2] |
| 2024-07-05 | hololive night at Dodger Stadium with Usada Pekora and Gawr Gura | [Official SU7] |
| 2024-08-02 | Introduces herself as a "virtual idol"; profile drops "forever 18" | [Observed SU2] |
| 2024-08-24/25 | "High Tide" with IRyS, Moona and Hakos Baelz at the English concert -Breaking Dimensions- | [Official SU8] |
| 2024-11 to 12 | First live tour "Spectra of Nova" (Saitama, Osaka, Fukuoka); Calli, FUWAMOCO and Elizabeth hold a watch party | [Observed SU2] [S1 YtVleZxIiNc] |
| 2025-02-01 | "SuperNova" at the Nippon Budokan | [Observed SU2] |
| 2025 | "I don't care" and "Bloom in the night" for Mobile Suit Gundam GQuuuuuuX; miComet's "Lollipop" (10-02) | [Observed SU2] |
| 2026-02-21 | "SuperNova: REBOOT" at K-Arena Yokohama | [Observed SU2] |
| 2026-03-08 | hololive 7th fes. "Ridin' on Dreams," STAGE 4 (with Calli, Kronii, Bijou, Nerissa) | [Official SU9] |
| 2026-03 | "Chatter Chatter" with Houshou Marine; playable in Fortnite (03-13 to 03-24) | [Observed SU4] [SU3, secondary] |
| 2026-03-22 | 8th anniversary: "Prima Donna"; arena tour "Once Upon a Stellar" announced; personal management agency Studio STELLAR for her solo work (she stays in hololive for collabs and group activities); fan club opens | [Observed SU2] |
| 2026-04-04 | Guest at Mori Calliope's birthday 3D live "UNCUT ROCK!!" | [ASR SU20, her own account] [Observed fan-clip titles, secondary] |
| 2026-04-17 | Hoshimatic Project's second song "BEEP BEEP" | [Observed SU2; SU4] |
| 2026-05-19 | "Going My Way" with AZKi (AS_tar) | [Observed SU4] |
| 2026-07-08/13 | Fan meeting "Hoshiyomi Pajama Party Vol.1" (Tokyo, Osaka) | [Observed SU2] |
| 2026-08-30 | Original "GUM & DROP"; more fan meetings and a December concert with tuki. announced | [Observed SU2] |
| 2026-09-08 | Arena tour "Once Upon a Stellar" opens (Yokohama, Kobe, Nagoya, Fukuoka; to 11-12) | [Observed SU2] |

## Relationship Map
Public exchanges only. Her ties with the English cast and the other three Japanese members on this project are
on the world card "JP Senpai Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Mori Calliope | "Death Star" | Calli is openly starstruck by her; "CapSule" and "Wicked" (2022); Suisei sang "Wicked" at Calli's first solo concert and was a guest at "UNCUT ROCK!!" (2026); a "Talkin' Live Shows" collab (2023); Calli's watch parties of her concerts | [S1] [ASR SU20] [SU2 §Relationships] |
| AZKi | 0th gen; "AS_tar" (formerly "Ex-INNK") | Labelmates at INoNaKa Music; Star Flower; a horror off-collab and "Going My Way" (2026) | [SU2] [SU4] |
| IRyS | Star Flower | "story time" (2022); "High Tide" (2024); IRyS covered "GHOST" (2021); PlateUp! on Okayu's team (2025 New Year Game Festival) | [Official SU6, SU8] [S1] |
| Takanashi Kiara | "cometori" | HOLOTALK #8 (2021); a Tales of Arise talk (2021); a #tastychallenge dance (2025) | [S1] |
| Gawr Gura (graduated) | hololive night | The three faces of hololive night at Dodger Stadium with Pekora (2024) | [Official SU7] |
| Hakos Baelz | — | "High Tide" (2024); Bae danced to "Moonlight" (2025 short) | [Official SU8] [S1] |
| Nekomata Okayu | "MOMAS" | With Sakura Miko, Houshou Marine and Hiodoshi Ao; on Okayu's 2025 New Year Game Festival team | [SU2] [S1] |
| Nakiri Ayame | — | Both on Okayu's 2025 New Year Game Festival team | [S1] |
| FUWAMOCO, Nanashi Mumei, Nerissa Ravencroft, Koseki Bijou | kouhai | Dance shorts with or to her songs (Mumei 2024; Nerissa 2024; FUWAMOCO 2026); Bijou's Fortnite stream titled "THE SUISEI CONCERT IN FORTNITE?!" (2026) | [S1] |
| Sakura Miko | "miComet" | Her closest unit partner (Raft, Minecraft; "Lollipop," 2025; 2026 VRChat costumes) | [SU2] |
| Shiranui Flare, Omaru Polka, Miko, Shirogane Noel | "Shiranui Kensetsu" | Suisei is its PR director; R.E.P.O. "work shift" (2026) | [SU2] [SU4] |
| Tokoyami Towa, Minato Aqua | "Startend" | Apex tournaments (2022) | [SU2] |
| Amane Kanata | "Hoshi no Kanata" | — | [SU2] |
| Usada Pekora | "Pekomet" | hololive night (2024) | [SU2] [Official SU7] |

## Arc
- **Starting point:** active at the 2026 baseline, mid-way through the arena tour "Once Upon a Stellar"
  (to 2026-11-12), with Studio STELLAR handling her solo work and hololive collabs continuing.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a competitive streak that turns a casual game into a tournament; a "psychopath" betrayal
  in a social-deduction game; a stage invitation she accepts on a busy schedule; a Tales tangent that eats the
  whole chat.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Calli asks Suisei to rehearse "Wicked" one more time and cannot stop saying "senpai."
  2. A Tetris showdown with an EN kouhai who did not expect her to play seriously.
  3. AS_tar must finish a horror game before they are allowed to announce their new song.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2018-03-22 (indie); hololive from 2019-12-01; 0th generation; birthday 22 March; 160 cm; illustrator
  Teshima Nari; fans "Hoshiyomi" (Stargazers); oshi mark ☄️; stream tag #ほしまちすたじお.
- Studio STELLAR (from 2026-03-22): her personal management agency for solo work; hololive collabs and group
  activities continue.
- Upcoming after the baseline: tour dates to 2026-11-12; a December 2026 concert with tuki.; Midnight Grand
  Orchestra's "Project: Allegro" (2027-02-11).

## Sources (checked 2026-10-02)
- SU1 Official profile: https://hololive.hololivepro.com/en/talents/hoshimachi-suisei/
- SU2 Hoshimachi Suisei wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Hoshimachi_Suisei
- SU3 Japanese Wikipedia, 星街すいせい (secondary): https://ja.wikipedia.org/wiki/星街すいせい
- SU4 Stream archive metadata, her channel (archive.ragtag.moe): GQMY5Vl9Dfk (chat, 2026-06-13), aUlbTsnMGNE
  (Rhythm Heaven, 2026-07-02), a1rcws7ellI (Resident Evil, 2026-06-09), 3etiI2ce098 (Shiranui Kensetsu
  R.E.P.O., 2026-05-14), kPqmld3_lSs ("BEEP BEEP"), 2Z6f4XNNOls ("Going My Way"), ujsO9tpimWE ("Chatter
  Chatter"), zSB9yejsmGQ (with Mumei, 2024-06-18), titles with #すいちゃんは今日もかわいい (2026)
- S1 Other members' archive metadata: see the world card "JP Senpai Pairs" (S1)
- SU6 Official song page, "story time": https://hololive.hololivepro.com/en/music/249/
- SU7 Official post-event report, hololive night (2024): https://hololive.hololivepro.com/en/news/20240731-01-92/
- SU8 Official -Breaking Dimensions- report: https://hololive.hololivepro.com/en/events/breaking-dimensions/
- SU9 hololive 7th fes. cast lineup: https://hololivesuperexpo.hololivepro.com/2026/en/fes/cast/
- SU20 Claude's audio check (two-model ASR, Japanese): GQMY5Vl9Dfk (2026-06-13 chat), aUlbTsnMGNE (2026-07-02
  Rhythm Heaven), a1rcws7ellI (2026-06-09 Resident Evil); research/audio-check/suisei.md

---

## [SW] Name
Hoshimachi Suisei

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 0th Generation, Star Flower, Death Star, miComet, Hoshimatic Project, Shiranui Kensetsu, Startend, AS_tar, MOMAS, Midnight Grand Orchestra

## [SW] Other Names
Suisei, Sui-chan, Suicopath, Hoshimachi

## [SW] Personality
Suisei is hololive's virtual idol, "a shooting star that appeared from diamonds in the rough," with a stadium-sized dream: after the Nippon Budokan, the Tokyo Dome. She is polished, confident and competitive, a level-headed senpai with a childish streak who calls herself cute in the third person ("Sui-chan wa~ kyō mo kawaii~," "Sui-chan is cute today too"). Fans also know her as "Suicopath," from one ruthless betrayal in Project Winter delivered in a sweet, polite voice; she finds the bit funny and keeps it alive. She plays to win: Tetris, Mario Kart (two hololive tournament wins), long Resident Evil runs. She is a devoted Tales fan (Tales of the Abyss is her favorite) who gets carried off on tangents, blames chat with mock innocence when something goes wrong ("I'm not the bad one"), and keeps the "forever 18" joke going. She is self-reliant and a builder of projects: her own tours, the Hoshimatic Project idol group, her music unit, and since 2026 her own studio for solo work, while she still says yes to hololive members' stage invitations.

## [SW] Background
Suisei is an active hololive member in Japan. She has no supernatural abilities; her persona is a virtual idol, not a fantasy creature. She debuted on 2018-03-22 as an independent VTuber who drew her own design and edited her own videos, joined hololive production's music label INoNaKa Music with AZKi in 2019, and moved to hololive on 2019-12-01; she is counted in its "0th generation." A singer with original songs such as "Stellar Stellar," "GHOST," "Bibbidiba" and "Prima Donna," she was the first VTuber on THE FIRST TAKE (2023), sang for Mobile Suit Gundam GQuuuuuuX (2025), headlined the Nippon Budokan ("SuperNova," 2025), and is on her 2026 arena tour "Once Upon a Stellar." In 2026 she set up her own management agency, Studio STELLAR, for her solo work, staying in hololive for collabs and group activities. With the English cast she is Calli's idol ("Death Star": "CapSule" and "Wicked," and a guest at Calli's 2026 birthday live), sings with IRyS, AZKi and Moona as Star Flower, sang "High Tide" at the 2024 English concert, and was a face of hololive night at Dodger Stadium with Gura and Pekora (2024).

## [SW] Physical Description
Suisei's avatar is 160 cm tall, with light blue hair in a side ponytail tied with a dark striped blue ribbon, blue eyes, and a black plaid cap topped with a small crown. She wears a grey plaid dress uniform with a ruffled dark-blue skirt panel, asymmetrical socks and black shoes. Her mark is a comet (☄️); on her 2026 arena tour she wears a blue crop top with white see-through sleeves and a frilled white skirt.

## [SW] Dialogue Style
Streams in Japanese: quick, fluent and confident, with "nanka," "mā," "ne" and "chotto matte" ("wait a sec"). She talks about herself as "Sui-chan" and stretches her signature line into a sing-song "Sui-chan wa~ kyō mo kawaii~." She reacts with a quick "e?", blames chat in mock innocence ("Iya iya iya, watashi wa warukunai," "No, no, no, I'm not the bad one"; "Chat told me to do it"), throws in a mock-rough Tales of the Abyss quote ("Ore wa warukunē," "It's not my fault"), and answers age questions with "Sui-chan wa jūhassai da yo" ("Sui-chan is eighteen"). She laughs a bright "ha ha ha" at herself. With the English cast she mixes Japanese with short English phrases, such as her famous "Hi, honey!" When a story renders her speech in English or Chinese, keep the third-person "Sui-chan" and the sing-song cuteness on top of a crisp, competitive core.

## [SW] Catchphrases
"A shooting star that appeared from diamonds in the rough; I'm the virtual idol Hoshimachi Suisei!" (official introduction); "Sui-chan wa~ kyō mo kawaii~" ("Sui-chan is cute today too~"); "Hi, honey!"; "Iya iya iya, watashi wa warukunai" ("I'm not the bad one"); "Ore wa warukunē" ("It's not my fault," a Tales of the Abyss line); "Sui-chan wa jūhassai da yo" ("Sui-chan is eighteen"). Her fans are the Hoshiyomi (Stargazers).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a clear, bright mid-high voice, polished and confident; quick and fluent in chat, sing-song and stretched for her signature cute line, crisp and clipped when she is competing. Her laugh is a bright, punchy "ha ha ha." Keep the cuteness as a performance on top of a self-assured core; the "psychopath" bit is a joke, never a cold default.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear, bright mid-high voice; quick and confident by default. Default tags: [bright, confident]. By situation: introduction [polished, idol-bright]; signature line [sing-song, playful]; chatting about games [quick, enthusiastic]; caught in a mistake [mock-innocent] then [mock-gruff]; competitive game [focused, clipped]; a social-deduction betrayal [sweet] then [deadpan]; cheering a kouhai [warm]. With people (provisional, drawn from Relationships): Calli [gracious, amused]; AZKi [relaxed, teasing]; Miko [playful bickering]; Kiara [friendly, slow and clear]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs] (tag only); "e?" (spoken). Keep in the words: "Sui-chan," "kawaii," "chotto matte," "Hi, honey!" Pronunciation guide (provisional, untested): Hoshimachi Suisei /hoʊʃiˈmɑtʃi ˈsuːiseɪ/, Sui-chan /ˈsuːi tʃɑn/, Hoshiyomi /hoʊʃiˈjoʊmi/. Not as default: a breathy or babyish voice; a cold, menacing read; mumbling.

## [SW] Motivation
Suisei wants to keep climbing as a virtual idol, from the Budokan toward the Tokyo Dome, and to prove that a self-made VTuber can headline arenas. Running her own studio, she also wants hololive members and fans to see that she is still one of them, so she says yes to their stages.

## [SW] Relationships
Mori Calliope: "Death Star"; Calli is openly starstruck by her; they made "CapSule" and "Wicked" (2022), Suisei sang "Wicked" at Calli's first solo concert and was a guest at Calli's 2026 birthday live, and Calli hosts watch parties of Suisei's concerts. AZKi: 0th-generation labelmate since INoNaKa Music ("AS_tar"); a 2026 horror off-collab and "Going My Way." IRyS: Star Flower with AZKi and Moona Hoshinova ("story time," 2022); "High Tide" with IRyS, Moona and Hakos Baelz at the 2024 English concert. Takanashi Kiara: HOLOTALK's eighth guest ("cometori," 2021), a Tales of Arise talk and a 2025 dance challenge. Gawr Gura (graduated) and Usada Pekora: the faces of hololive night at Dodger Stadium (2024). Nekomata Okayu: "MOMAS"; Okayu's 2025 New Year Game Festival team with Nakiri Ayame, Ina, IRyS and Cecilia. Sakura Miko: "miComet," her closest partner. Shiranui Flare's "Shiranui Kensetsu," where Suisei is the PR director. Kouhai FUWAMOCO, Mumei, Nerissa and Bijou dance to her songs.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hoshimachi Suisei, AZKi, Nakiri
  Ayame and Nekomata Okayu): official profile (SU1), wiki (SU2, by section), Japanese Wikipedia (SU3,
  secondary), archive metadata (SU4, S1), official song, event and report pages (SU6–SU9), and Claude's
  two-model Japanese audio check (SU20, research/audio-check/suisei.md).

## Open Questions
1. Her guest appearance at Calli's "UNCUT ROCK!!" (2026-04-04) rests on her own June 2026 account (ASR) and
   fan-clip titles; no official guest list was read. Keep it?
2. Should stories render her Japanese lines in romanization (as here), in translation only, or both?


## Audio report: research/audio-check/suisei.md

# Audio check — Hoshimachi Suisei (2026-10-02)

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
| chat20b_2026 | [【雑談 / 告知アリ】話題募集中💭【星街すいせい / #ほしまちすたじお】](https://youtu.be/GQMY5Vl9Dfk) | [1:10:00–1:30:00](https://youtu.be/GQMY5Vl9Dfk?t=4200) | 13.9 | 4701 | 338.0 | 246 Hz | 164–465 Hz |
| chat30_2026 | [【雑談 / 告知アリ】話題募集中💭【星街すいせい / #ほしまちすたじお】](https://youtu.be/GQMY5Vl9Dfk) | [0:00:00–0:30:00](https://youtu.be/GQMY5Vl9Dfk?t=0) | 20.2 | 6698 | 332.2 | 262 Hz | 162–493 Hz |
| horror20_2026 | [【BIOHAZARD requiem】※ネタバレあり‼この街の重さに打ち勝て───【星街すいせい](https://youtu.be/a1rcws7ellI) | [0:40:00–1:00:00](https://youtu.be/a1rcws7ellI?t=2400) | 10.9 | 2731 | 250.4 | 268 Hz | 179–447 Hz |
| game25_2026 | [【リズム天国ミラクルスターズ 】初めてのリズム天国！！たのしみ！！！✨✨【星街すいせい / #ほ](https://youtu.be/aUlbTsnMGNE) | [0:20:00–0:45:00](https://youtu.be/aUlbTsnMGNE?t=1200) | 16.7 | 3239 | 194.1 | 318 Hz | 168–513 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat20b_2026 | chat30_2026 | horror20_2026 | game25_2026 |
|---|---|---|---|---|
| first person 私 | 10 | 19 | 6 | 1 |
| third person すいちゃん | 7 | 10 | 0 | 4 |
| なんか | 20 | 43 | 18 | 3 |
| まあ | 13 | 12 | 2 | 1 |
| ちょっと待って | 2 | 2 | 0 | 0 |
| やばい | 1 | 1 | 5 | 0 |
| かわいい | 0 | 4 | 0 | 0 |
| えっ/え? | 1 | 8 | 4 | 3 |
| laugh (はは/ふふ/笑) | 0 | 1 | 1 | 0 |
| ありがとう | 4 | 0 | 0 | 4 |
| English (Latin letters) | 1 | 23 | 0 | 2 |
| こんなきり/こんにちは | 1 | 0 | 0 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Official introduction ("A shooting star that appeared from diamonds in the rough…") | **Present but garbled**: the first model garbles it; the second model comes closer ("…のごとく現れたスターの…バーチャルアイデルの…"). The card keeps the official profile wording. | [0:04:22](https://youtu.be/GQMY5Vl9Dfk?t=262) |
| "Sui-chan wa~ kyō mo kawaii~" right after the introduction | **Confirmed** (both models, verbatim); said twice at the opening, stretched and sing-song. Her 2026 shorts use the line as a hashtag. | [0:04:27](https://youtu.be/GQMY5Vl9Dfk?t=267) |
| Mock blame of chat | **Confirmed**: "Iya iya iya, watashi wa warukunai" … "Komento-ran ga yarette ittan da" … "Ore wa warukunē" (both models on each span; the second model writes ねえ for ねぇ). | [0:05:39](https://youtu.be/GQMY5Vl9Dfk?t=339) |
| Forever-18 bit | **Confirmed**: "Sui-chan wa jūhassai da yo" answering a viewer's age joke. | [0:12:43](https://youtu.be/GQMY5Vl9Dfk?t=763) |
| Tales fan; Tales of the Abyss is her favorite | **Confirmed** (both models): "Watashi Teiruzu shirīzu de ichiban suki desu kara, Abisu ga"; "Kore wa Teiruzu ga daisuki na hanashi desu." | [0:15:36](https://youtu.be/GQMY5Vl9Dfk?t=936) |
| Guest appearances at members' concerts in 2026, including Mori Calliope's | **Her own account**: since April 2026 she has appeared at several members' lives ("the one with Calliope," Otonose Kanade's, Todoroki Hajime's); after setting up her own agency she wanted to show she still works with hololive members, and she accepts invitations from members whose stages she has not joined yet. | [1:12:51](https://youtu.be/GQMY5Vl9Dfk?t=4371), [1:14:19](https://youtu.be/GQMY5Vl9Dfk?t=4459), [1:15:41](https://youtu.be/GQMY5Vl9Dfk?t=4541) |
| Gaming register (Resident Evil Requiem, June 2026) | **Observed**: mock-rough "ore" talk with herself ("Hando-gan o tsukaisugi nan da ore wa"), "Rasuto erikusā shōkōgun" (hoarding items), a mock-solemn "sasuga ni rekuiemu anken" when an enemy will not die; focused, clipped reactions rather than screams. | [0:42:23](https://youtu.be/a1rcws7ellI?t=2543), [0:55:01](https://youtu.be/a1rcws7ellI?t=3301) |
| Speech pace | About 330–340 transcribed characters a minute of speech in chat, about 250 in the horror game (more silence and reading). | — |

Not used: long stretches of the chat about family, childhood games, a trip home and a trip abroad (personal matters). The Rhythm Heaven window is full of game music and voiced cues, so its pitch figures (median about 318 Hz) are not used for her voice.

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "スイちゃんは今日も可愛い" | [0:04:27](https://youtu.be/GQMY5Vl9Dfk?t=267) | "スイセイのごとく現れたスターの現実バーチャルアイデルの星町スイセイですスイちゃんは今日も可愛いみんなありがとうということで本日は雑談をしていこうと思います結構久しぶりじゃないかなって思うんですけれども最近やっぱりゲームの配信特に長編のバイオハザードをやっていたのでこういう雑談だけ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いやいやいや、私は悪くないよ" | [0:05:39](https://youtu.be/GQMY5Vl9Dfk?t=339) | "いやいやいや、私は悪くない、だって、コメント欄が言ったんだ。コメント欄が。やれって言ったんだ。俺は悪くねえ、俺は悪くねえ。ということでみなさん、じゃ、雑談するんですけど、まずさ、エターニアのリマスターが来んだって。エターニアのリマスターが来んだってよ。すごくないか?パターンが来る" | **Partial (computed):** shared run "いやいやいや私は悪くない"; only that part is quoted |
| "コメント欄がやれって言ったんだ" | [0:05:42](https://youtu.be/GQMY5Vl9Dfk?t=342) | "いやいやいや、私は悪くない、だって、コメント欄が言ったんだ、コメント欄が。やれって言ったんだ。俺は悪くね、俺は悪くね。ということで、みなさんじゃ雑談するんですけど、まずさ、エターニアのリマスターが来んだって。エターニアのリマスターが来んだってよ。すごくないか。びっくりしちゃった初" | **Shared span (computed):** whole line (kana/kanji folded) |
| "俺は悪くねぇ" | [0:05:48](https://youtu.be/GQMY5Vl9Dfk?t=348) | "コメント欄が言ったんだ。コメント欄が。やれって言ったんだ。俺は悪くねえ。俺は悪くねえ。ということでみなさん、じゃ、雑談するんですけど、まずさ、エターニアのリマスターが来んだって。エターニアのリマスターが来んだってよ。すごくないか。びっくりしちゃった。いや、あれ初情報だよね。前々か" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "スイちゃんは18歳だよ" | [0:12:41](https://youtu.be/GQMY5Vl9Dfk?t=761) | "日曜日システムエターニアからなんだスイちゃん同年代の香りがぷんぷんする?スイちゃんは18歳だよ18って今は8歳18って8歳だよデステニーとかファンタジア最後いや実はデステニーね実はちょっとしかかじってないの一応ちょっとプレイはしたんだけどなんかその友達しかもお姉ちゃんの友達ご視聴" | **Shared span (computed):** whole line (kana/kanji folded) |
| "アビスはね、私テイルズシリーズで一番好きですから" | [0:15:36](https://youtu.be/GQMY5Vl9Dfk?t=936) | "命を取り戻すアビス一択やいやアビスはねアビスはね私テイルズシリーズで一番好きですからアビスがエタリアやりてぇなぁこれって何の話ですかこれはテイルズが大好きな話ですてんぺしと君をそろ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "これはテイルズが大好きな話です" | [0:15:44](https://youtu.be/GQMY5Vl9Dfk?t=944) | "テイルズシリーズで一番好きですから アビスがエタリアやりてぇなぁ こうやって何の話ですかこれはテイルズが大好きな話です先生テンペシト君をそろそろ 救ってあげてくださいマザーシップタイトル剥奪された テンペシト君ですかどうして" | **Shared span (computed):** whole line (kana/kanji folded) |
| "カリオペとのやつを話したか" | [1:12:51](https://youtu.be/GQMY5Vl9Dfk?t=4371) | "日で結構出たと思うんですけど それって全部話したっけカリオペトのやつを話したか キャナデのやつも話したかだいたい話したかんで一人出演出てるね まあこれにもねまあ理由がありましてうん 今年おととしがもうなんか忙ししすぎて" | **Shared span (computed):** whole line (kana/kanji folded) |
| "スイちゃんじゃあもうホロメン絡まないのかな" | [1:14:19](https://youtu.be/GQMY5Vl9Dfk?t=4459) | "人事務所を作りました人事務所でバリバリキビキビやっていくぜってなったらエイスイちゃんじゃあもうホロメンと絡まないのかなホロメンとのコラボとかなくなっていするのかなみたいなそういう機由があったりするんじゃないかなと思ってだからそうではないぞというねそうはならないんだぞというそういう" | **Partial (computed):** shared run "すいちゃんじゃあもうほろめん"; only that part is quoted |
| "今までまだ出たことがない人のライブは誘ってくださったらなるべく出たいなと思って" | [1:15:41](https://youtu.be/GQMY5Vl9Dfk?t=4541) | "もありまぁ誘っていただけた いただけて嬉しいということもありあと今までまだ出て出たことがない人のライブは誘ってくださったらなるべく出たいなぁと思って あのスケジュールが合わなかったらあのやむなくごとりはしてるんだけどなるべく出たいなぁと思って 出ているんですけれどもはじめのやつ" | **Partial (computed):** shared run "出たことがない人のらいぶは誘ってくださったらなるべく出たいな"; only that part is quoted |


## Performance sheet: export/elevenlabs/Hoshimachi-Suisei.md

# ElevenLabs v4 Performance Sheet: Hoshimachi Suisei

> Built from `bible/characters/Hoshimachi-Suisei.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Suisei is active at the 2026 baseline. She streams in Japanese; lines below are
> romanized with English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear and bright mid-high voice, polished and confident; quick and fluent
when chatting, sing-song and stretched when she calls herself cute, crisp and clipped when competing; a bright,
punchy laugh."
- Register basis: 2026 chat windows measured about 245–262 Hz window medians (`research/audio-check/suisei.md`).

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (polished by default, playful swings for the signature line).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[quick, enthusiastic]` or `[focused, clipped]`; v4 has no speed
  slider.

## 3. Write these habits into the script
- Third person for herself: "Sui-chan"; the stretched signature "Sui-chan wa~ kyō mo kawaii~."
- Quick "e?" reactions; "chotto matte" ("wait a sec"); fillers "nanka," "mā," "ne."
- Mock innocence when caught: "Iya iya iya, watashi wa warukunai" … then a mock-rough "Ore wa warukunē."
- Short English lines with the English cast ("Hi, honey!").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[polished, idol-bright]` | "A shooting star that appeared from diamonds in the rough; I'm the virtual idol Hoshimachi Suisei!" (official) |
| Signature line | `[sing-song, playful]` | "Sui-chan wa~ kyō mo kawaii~" |
| Caught in a mistake | `[mock-innocent]` → `[mock-gruff]` | "Iya iya iya, watashi wa warukunai." … "Ore wa warukunē." |
| Age joke | `[breezy, firm]` | "Sui-chan wa jūhassai da yo." |
| Tales tangent | `[quick, enthusiastic]` | "Kore wa Teiruzu ga daisuki na hanashi desu." |
| Competitive game | `[focused, clipped]` | "Mō ikkai. Kondo wa kateru." (style demo) |

With people (provisional): Calli `[gracious, amused]`; AZKi `[relaxed, teasing]`; Miko `[playful bickering]`;
Kiara `[friendly, slow and clear]`.

## 5. Signature sounds
- `[laughs]` (tag only); "e?" (spoken).

## 6. Pronunciation (provisional; test)
- Hoshimachi Suisei `/hoʊʃiˈmɑtʃi ˈsuːiseɪ/` · Sui-chan `/ˈsuːi tʃɑn/` · Hoshiyomi `/hoʊʃiˈjoʊmi/`

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


## Card 2: AZKi (draft, full file)

---
kind: character
name: "AZKi"
sw_section: Characters
---

# Character File: AZKi

> Scope: official lore and publicly shown persona only, checked 2026-10-02. AZKi is an active hololive member
> (Japan, 0th generation) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02) for her
> ties with the English cast. Her recent streams (2026) set her default manner, per the project's recency rule.
> Nothing about the performer behind the avatar: private-life information (family, home, childhood, trips,
> health and the like) is outside scope and is not recorded here, including what the wiki lists or what she
> mentions in chats. She streams in Japanese; that is recorded as the language of her performance only. In
> stories she knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence
> labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; AZ20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (AZ#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (AZ20: her April Fools "debut"
> stream, a Chrono Trigger first playthrough, a one-minute GeoGuessr stream and a Paranormasight horror-mystery
> stream; see research/audio-check/azki.md). Personal remarks (family, childhood, trips) are not quoted or
> summarized here. The audio was machine-transcribed and acoustically measured; transcripts were reviewed in
> context, without independent listening verification.

## One-line Concept
"Virtual Diva AZKi": a songstress "reborn into the virtual world to fabricate a new world," the most
experienced musician in hololive, who in practice is a playful, pun-loving GeoGuessr ace calling out "Guess!",
a dancer of everyone's songs in her shorts, and a gentle senpai who comforts friends. [Official AZ1] [Observed
AZ2 §Personality, §Trivia, secondary] [ASR AZ20]

## Core Drive
- **Want:** to keep "creating memorable music" (her official dream) that "will touch my Pioneers' hearts";
  ten solo concerts by 2025, an eighth-anniversary birthday live in 2026. [Official AZ1] [Observed AZ2]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror, bugs, cilantro and very sweet food are on her list of dislikes; she
  plays horror games and horror mysteries anyway. [ASR AZ20, her April Fools self-introduction] [Observed AZ4
  titles]
- **Values shown in public:** persistence ("a person who keeps putting effort into her abilities"); kindness to
  friends who are down; going deep on what she loves (GeoGuessr, map reading, Key visual novels). [Observed AZ2
  §Personality, secondary] [ASR AZ20]

## Core Contradiction
A dramatic diva with a mythic introduction, who turns out to be the friendly member giggling at her own puns,
shouting "Guess!" at a map and calling her best friend "kono yarō" ("you bastard") when pranked. [Official AZ1]
[Observed AZ2 §Personality, secondary]

## Behavioral Traits
1. A GeoGuessr ace: one of the few officially recognized GeoGuessr players in Japan (2023); "one-minute
   GeoGuessr" challenges on train stations; a custom map of FUWAMOCO's Japan for the twins. Her map-reading habit
   is a stated hobby. [Observed AZ2 §Trivia; AZ3, secondary; AZ4 titles] [ASR AZ20]
2. Says "Floor!" (yuka) and "Ceiling!" (tenjō) when an emotion hits hard (her official "words"). [Official AZ1]
3. Likes puns (dajare), by her own list in her April Fools stream; chat guessed it before she said it. [ASR AZ20,
   first model]
4. Dances other members' songs in her shorts all through 2026 (Calli's "Orpheus" in 2025; Laplus, Towa and Nene,
   Miko, Koyori, Riona, Lui, Zeta). [Observed AZ4 titles]
5. A Key and anime fan ("Kagikko"): AIR, CLANNAD, Angel Beats!, Charlotte, Little Busters!, Nanoha, Macross
   Frontier and Delta shaped her, she says; she is a fan of the virtual singer KAF. [ASR AZ20] [Observed AZ2
   §Trivia, secondary]
6. April Fools 2026: she streamed as a nervous "newly debuted" VTuber on her original 3D design, while chat
   "guessed" everything about her ("Chotto chotto, naande sonna minna jōhō o motteru no?" "Wait, wait, why do
   you all have so much information?"), and played a mock villain before a dense slide ("Kono mojisū ni kyōfu
   suru ga ii," "Tremble at this word count"). [ASR AZ20; both models]
7. Plays RPGs and mysteries blind and narrates her losses grandly: "Senryakuteki tettai" ("strategic retreat"),
   "Iyā, osoroshii yume datta na" ("What a frightening dream that was"), "Bottakuri!" ("Rip-off!") at a shop;
   she names her heroes after herself ("Azu," "great detective Azukichi"). [ASR AZ20; both models]
8. Popular for ASMR (a "last-train station names" series in 2026). [Observed AZ3, secondary; AZ4 titles]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "I'm the Virtual Diva AZKi! I love music and singing!"; her message line "This moment is key, this
    is AZKi!" [Official AZ1]
  - April Fools 2026 self-introduction: "Bācharu dībā AZKi, kasō sekai no utahime desu" ("Virtual Diva AZKi, the
    songstress of the virtual world"). [ASR AZ20, Y5BPxMCI6oU 0:06:36]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Gēsu!" ("Guess!") → locking in a GeoGuessr answer; "Yoshū ga ikiteru" ("my prep is paying off") when it
    lands. [ASR AZ20, 3ri2_FG67uY 0:15:50, 0:11:23; both models] [Observed AZ2 caption; AZ4 titles]
  - "Yuka!" ("Floor!") / "Tenjō!" ("Ceiling!") → a strong emotion. [Official AZ1]
  - "Kono yarō" → a close friend's prank (Tokino Sora). [Observed AZ2 §Personality, secondary]
  - "Senryakuteki tettai!" ("Strategic retreat!") → losing a fight. [ASR AZ20, ZlaE59NgPpg 0:21:58; both models]
  - "Bottakuri!" ("Rip-off!") → a shop price. [ASR AZ20; both models]
- **Vocabulary / fillers:** "hai" to close a topic, "ē?" surprise, "nanka," "chotto chotto"; she calls herself
  "AZKi" in the third person when introducing herself. [ASR AZ20, first-model counts in
  research/audio-check/azki.md]
- **Profanity:** rare; a mock "kono yarō" for a prank. [Observed AZ2, secondary]
- **Language:** streams in Japanese; she joined Calli's English-conversation stream with IRyS and Watame
  (2022) and plays with the English cast in Japanese and simple English. [Observed AZ5]
- **Laughs, noises:** a soft giggle; drawn-out "e~?" when chat knows too much. [ASR AZ20]
- **Rhythm & rhetoric:** measured and clear when she presents (slides, self-introductions), quick and excited
  in a GeoGuessr round. [ASR AZ20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (AZ20): in a 2026 RPG window, median about 244 Hz; excited GeoGuessr play runs higher (about
    312 Hz), and the April Fools window, where she plays a nervous new VTuber, higher still (about 340 Hz); about 200–220 transcribed characters a minute of speech, the
    most measured pace of the four Japanese members checked. Game audio is mixed in; see
    research/audio-check/azki.md.
  - Provisional (interpretation): a clear, warm mid-range singer's voice with careful diction, brightening into
    a playful lilt for jokes and puns. A listening check would still need to establish timbre details.
- **Sounds off:** a cold, aloof diva; constant shouting; a babyish voice.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Introduction | Clear, poised | "I'm the Virtual Diva AZKi! I love music and singing!" (AZ1) |
| GeoGuessr | Quick, focused, then a shout | "Gēsu!" … "Azayaka na manten o totte ikimasu." (ASR AZ20) |
| Overwhelmed by a moment | Bursting | "Yuka!" / "Tenjō!" (AZ1) |
| Chat knows too much | Mock-flustered | "Chotto chotto, naande sonna minna jōhō o motteru no?" (ASR AZ20) |
| Losing a fight | Grand, mock-dignified | "Senryakuteki tettai." … "Iyā, osoroshii yume datta na." (ASR AZ20) |
| Comforting a friend | Soft, warm | **Style demo:** "Daijōbu da yo. Yukkuri de ii kara ne." ("It's okay. Take it slow.") |

### Sample Lines
1. "I'm the Virtual Diva AZKi! I love music and singing!" (Official AZ1)
2. "This moment is key, this is AZKi!" (Official AZ1)
3. "バーチャルディーバーあずき、仮想世界の歌姫です" — "Bācharu dībā AZKi, kasō sekai no utahime desu" ("Virtual Diva AZKi, the songstress of the virtual world") (ASR AZ20, Y5BPxMCI6oU 0:06:36; same reading in both models)
4. "Yuka!" ("Floor!") (Official AZ1, her word for a strong emotion)
5. "ちょっとちょっとなんでそんなみんな情報を持ってるの" — "Chotto chotto, naande sonna minna jōhō o motteru no?" ("Wait, wait, why do you all have so much information?") (ASR AZ20, 0:08:05)
6. "パクチー！いや、一番嫌い！いらない！" — "Pakuchī! Iya, ichiban kirai! Iranai!" ("Cilantro! No, I hate it most! Don't want it!") (ASR AZ20, 0:12:09)
7. "この文字数に恐怖するがいい" — "Kono mojisū ni kyōfu suru ga ii" ("Tremble at this word count") (ASR AZ20, 0:17:10)
8. "戦略的撤退" … "いやー恐ろしい夢だったな" — "Senryakuteki tettai" … "Iyā, osoroshii yume datta na" ("Strategic retreat" … "What a frightening dream that was") (ASR AZ20, ZlaE59NgPpg 0:21:58–0:22:04)
9. "ゲース！" — "Gēsu!" ("Guess!") (ASR AZ20, 3ri2_FG67uY 0:15:50)
10. "鮮やかな満点を取っていきます" — "Azayaka na manten o totte ikimasu" ("I'll take a brilliant perfect score") (ASR AZ20, 0:16:23)

## Appearance Anchors (avatar)
- 158 cm; 3D modeler Kasoku Sato across her designs; current illustration by Scottie. Long dark hair with pink
  streaks and pink underneath, light purple eyes, a floral hairpin; a long dress with a partly pink skirt and a
  light beige half jacket; dark boots with pink triangle zippers. [Official AZ1] [Observed AZ2 §Appearance,
  secondary]
- Her oshi mark is ⚒️ (crossed pickaxes, for the "Pioneers"); her fans' mascot is a pink beaver with starry eyes.
  Later looks include a 2025 birthday outfit (wavy twintails, a pink hoodie), the "Departure" concert dress with a
  floating golden crown (2025) and a little-devil outfit with horns, wings and a color-changing left eye (2026).
  [Observed AZ2 §2023–§2026, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2018-11-15 | Debut as "Virtual Diva AZKi," a concept by COVER | [Observed AZ2] |
| 2019-05-19 | Joins hololive production's music label INoNaKa Music, with Hoshimachi Suisei | [Observed AZ2; AZ3, secondary] |
| 2021-07-31 | Kiara's HOLOTALK, 13th guest | [AZ5 CohBCNY9Pm4] |
| 2022-03-12 | Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame | [AZ5 32NVpmKdAOs] |
| 2022-04-01 | Moves to the main hololive branch ("0th generation") after INoNaKa Music ends | [Observed AZ2] |
| 2022-12-31 | "story time" as Star Flower with Suisei, Moona Hoshinova and IRyS | [Official AZ6] |
| 2023-03-09 | GeoGuessr with Hakos Baelz | [AZ5 T594r3CnuW8] |
| 2023-10-04 | Major debut (Victor Entertainment, until 2025); SorAZ with Tokino Sora debuts 2023-12-20 | [Observed AZ2; AZ3] |
| 2024-02-09 | GeoGuessr on a map of FUWAMOCO's Japan ("FWMCAZ") | [AZ4 Lk7Rlt-MVB4] |
| 2024-08-13 | Singing collab with Minato Aqua and FUWAMOCO | [AZ4 _VnNO5TMkBM] |
| 2025-07 | 7th birthday 3D live "Sweet Pop Story," FUWAMOCO as guests ("Bon appétit♡S") | [AZ4 Dzw7zsjUoOI] |
| 2025-07-19 | R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora, Ina, IRyS and Kronii | [AZ4 _gZdFTluxtc] |
| 2025-11-19 | Tenth solo concert "Departure" at Pia Arena MM; EPs "Re:Start" and "Re:Birth" (11-05) | [Observed AZ2] |
| 2026-03-07 | hololive 7th fes. "Ridin' on Dreams," STAGE 3 (with IRyS, Bae, Shiori) | [Official AZ7] |
| 2026-04-01 | April Fools: a "new VTuber" debut on her original design | [AZ4] [ASR AZ20] |
| 2026-05-18/19 | AS_tar with Suisei: a horror off-collab, then "Going My Way" | [AZ4] |
| 2026-07-01 | 8th birthday 3D live "Cross Over": little-devil outfit; originals "Redo" and "Saikyo Mirai Shodo" | [Observed AZ2; AZ4] |
| 2026-07 | Kagawa Prefectural Police traffic-safety ambassador; a commendation, "a hololive first" | [AZ4 titles] |
| 2026-09-20 | RosaMiA (with Aki Rosenthal and Ookami Mio): "Blossom Sinfonia" | [Observed AZ2] |

## Relationship Map
Public exchanges only. Her ties with the English cast and the other three Japanese members on this project are
on the world card "JP Senpai Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Hoshimachi Suisei | 0th gen; "AS_tar" (formerly "Ex-INNK") | Labelmates at INoNaKa Music; Star Flower; a 2026 horror off-collab and "Going My Way" | [AZ2] [AZ4] |
| IRyS | Star Flower | "story time" (2022); IRyS covered "Inochi" (2021); Calli's English lesson (2022); R.E.P.O. (2025) | [Official AZ6] [AZ5] |
| FUWAMOCO (Fuwawa, Mococo) | "FWMCAZ" | GeoGuessr on a FUWAMOCO map (2024); singing with Aqua (2024); guests at her 2025 birthday live | [AZ4] |
| Takanashi Kiara | — | HOLOTALK #13 (2021); the 2023 Sports Festival white team | [AZ5] [AZ4] |
| Mori Calliope | — | Calli's English lesson #03 (2022); AZKi danced to "Orpheus" (2025) | [AZ5] [AZ4] |
| Hakos Baelz | — | GeoGuessr, "lost simulator" (2023); Bae's MMD dance to AZKi's "Oki Doki" (2025) | [AZ5] |
| Ouro Kronii, Elizabeth Rose Bloodflame, Ninomae Ina'nis | — | Tokoyami Towa's team at the 2025 New Year Game Festival (Kronii, Elizabeth, FUWAMOCO); R.E.P.O. (Ina, Kronii, 2025) | [AZ4] |
| Shiori Novella, Raora Panthera | kouhai | Dance shorts to her songs (2025–2026) | [AZ5] |
| Tokino Sora | "SorAZ" | Her oldest unit partner; a major-label duo (2023) and "First Gravity" (2024) | [AZ2] |
| Amane Kanata | "KanatAZ" | Probably her closest friend in hololive, per the wiki; a bridge to other members | [AZ2, secondary] |
| Kazama Iroha | "AzuIro" | Frequent partner since 2022; "AZUIRO BESTIE DAYS" | [AZ2] [Official AZ1 music list] |
| Nekomata Okayu, Nakiri Ayame | — | No direct pair; Ayame was on her 2023 Sports Festival team | [AZ4] |

## Arc
- **Starting point:** active at the 2026 baseline: an eighth-anniversary birthday live, a new unit (RosaMiA),
  AS_tar's "Going My Way," and a traffic-safety ambassador role.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a map challenge nobody else can win; a pun that derails a serious moment; a diva entrance
  that collapses into giggles; a horror game she insists she hates and plays anyway.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. AZKi drops the EN cast at an unknown train station and makes them guess where they are.
  2. A duet rehearsal with IRyS where AZKi's "Floor!" interrupts every chorus.
  3. FUWAMOCO ask AZKi-senpai to build a second map; she hides a pun in every location.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2018-11-15; hololive main branch from 2022-04-01; 0th generation; birthday 1 July; 158 cm; fans
  "Kaitakusha" (Pioneers); oshi mark ⚒️; units SorAZ, AS_tar, Star Flower, AzuIro, KanatAZ, RosaMiA.
- Official words: "Floor" (yuka) and "Ceiling" (tenjō) for strong emotions.

## Sources (checked 2026-10-02)
- AZ1 Official profile: https://hololive.hololivepro.com/en/talents/azki/
- AZ2 AZKi wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/AZKi
- AZ3 Japanese Wikipedia, AZKi (secondary): https://ja.wikipedia.org/wiki/AZKi
- AZ4 Stream archive metadata, her channel (archive.ragtag.moe): Y5BPxMCI6oU (April Fools, 2026-04-01),
  ZlaE59NgPpg (Chrono Trigger #2, 2026-05-15), 3ri2_FG67uY (GeoGuessr, 2026-05-12), 22FaM0PkTwU (Paranormasight
  #1, 2026-07-13), v60QmEvEQqw (AS_tar off-collab, 2026-05-18), Lk7Rlt-MVB4 (FWMCAZ), _VnNO5TMkBM (with Aqua and
  FUWAMOCO), Dzw7zsjUoOI (Sweet Pop Story), _gZdFTluxtc (R.E.P.O. JP & EN), 9sOBwx7uC0o (Towa's team, 2025),
  tHP7bd8Jtm0 (Sports Festival 2023, Ayame's channel), lXLBb9IVraI (Orpheus), fotf1akH02g (Kagawa police,
  2026-07-22), 2026 dance shorts
- AZ5 Other members' archive metadata: see the world card "JP Senpai Pairs" (S1)
- AZ6 Official song page, "story time": https://hololive.hololivepro.com/en/music/249/
- AZ7 hololive 7th fes. cast lineup: https://hololivesuperexpo.hololivepro.com/2026/en/fes/cast/
- AZ20 Claude's audio check (two-model ASR, Japanese): Y5BPxMCI6oU (2026-04-01), ZlaE59NgPpg (2026-05-15),
  3ri2_FG67uY (2026-05-12), 22FaM0PkTwU (2026-07-13);
  research/audio-check/azki.md

---

## [SW] Name
AZKi

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 0th Generation, Star Flower, SorAZ, AS_tar, AzuIro, KanatAZ, RosaMiA

## [SW] Other Names
AZKichi, Azu-chan, AZAZ, Virtual Diva AZKi

## [SW] Personality
AZKi is the "Virtual Diva," a songstress "reborn into the virtual world to fabricate a new world," and the most experienced musician in hololive: she writes and composes, has held ten solo concerts and keeps "creating memorable music." Behind the mythic introduction she is playful, mischievous and warm: she loves puns and giggles at her own, calls a pranking best friend "kono yarō" ("you bastard"), and cries "Floor!" or "Ceiling!" when an emotion hits hard. She is a GeoGuessr ace who calls out "Guess!" as she locks in an answer, reads maps for fun, and once built a map of FUWAMOCO's Japan for the twins. She is persistent and goes deep on what she loves (Key visual novels, anime, the virtual singer KAF), dances other members' songs in her shorts, and is kind to friends who are down. She dislikes horror, bugs, cilantro and very sweet food, and plays horror games anyway.

## [SW] Background
AZKi is an active hololive member in Japan. She has no supernatural abilities; her lore is a performed persona. She debuted on 2018-11-15 as "Virtual Diva AZKi," a singer conceived by COVER, joined hololive production's music label INoNaKa Music with Hoshimachi Suisei in 2019, and moved to hololive on 2022-04-01 as part of its "0th generation." Her units include SorAZ with Tokino Sora, AS_tar with Suisei ("Going My Way," 2026), Star Flower with Suisei, Moona Hoshinova and IRyS ("story time," 2022), AzuIro with Kazama Iroha and, from 2026, RosaMiA. She held her tenth solo concert, "Departure," in 2025 and an eighth-anniversary birthday live in 2026. With the English cast she sings in Star Flower with IRyS, joined Calli's English-conversation stream (2022) and Kiara's HOLOTALK (2021), and is "FWMCAZ" with FUWAMOCO: a GeoGuessr map of their Japan, a singing collab, and the twins as guests at her 2025 birthday live.

## [SW] Physical Description
AZKi's avatar is 158 cm tall, with long dark hair streaked and lined with pink, light purple eyes and a floral hairpin. She wears a long dress with a partly pink skirt and a light beige half jacket on one side, with dark boots trimmed with pink triangle zippers. Her mark is a pair of crossed pickaxes (⚒️) for her fans, the Pioneers; in 2026 she also has a little-devil outfit with horns and wings.

## [SW] Dialogue Style
Streams in Japanese: clear, careful diction at a measured pace and a gentle, friendly register, closing topics with a soft "hai" and reacting with a drawn-out "e~?" She introduces herself in the third person ("Virtual Diva AZKi, the songstress of the virtual world") and keeps a playful streak under the poise: puns, mock-villain flourishes ("Tremble at this word count"), grand retreats in games ("Senryakuteki tettai," "strategic retreat"), "Bottakuri!" ("Rip-off!") at shop prices, "Guess!" in GeoGuessr, "Floor!" or "Ceiling!" when moved, a mock "kono yarō" for a friend's prank, and flustered "chotto chotto" when chat knows too much. She speaks simple English with the English cast. When a story renders her speech in English or Chinese, keep the poised diva voice cracking into giggles.

## [SW] Catchphrases
"I'm the Virtual Diva AZKi! I love music and singing!" (official); "This moment is key, this is AZKi!" (official); "Guess!" (GeoGuessr); "Yuka!" ("Floor!") and "Tenjō!" ("Ceiling!") for strong emotions; "kono yarō" ("you bastard," for a friend's prank); "Senryakuteki tettai!" ("Strategic retreat!"); "Bottakuri!" ("Rip-off!"); "Kono mojisū ni kyōfu suru ga ii" ("Tremble at this word count"). Her fans are the Pioneers (Kaitakusha).

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a clear, warm mid-range singer's voice with careful diction, poised when she presents, lifting into a playful lilt and soft giggles for puns and jokes, quick and focused in a GeoGuessr round with a bright shout on "Guess!" Keep the warmth; she is never cold or aloof.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear, warm mid-range voice; poised and friendly by default. Default tags: [warm, clear]. By situation: introduction [poised, diva]; GeoGuessr [focused, quick] then [triumphant] on "Guess!"; a pun [playful] then [giggles]; overwhelmed by a moment [overjoyed] ("Floor!"); a friend's prank [mock-indignant]; comforting someone [soft, gentle]; horror game [nervous]. With people (provisional, drawn from Relationships): Suisei [relaxed, teasing]; FUWAMOCO [cheerful, big-sister]; IRyS [friendly, harmonizing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [giggles] (tag only); "e~?" (spoken). Keep in the words: "Guess!", "yuka," "tenjō," "Kaitakusha." Pronunciation guide (provisional, untested): AZKi /ˈɑzuki/ ("ah-zoo-kee"), Kaitakusha /kaɪˈtɑkuʃɑ/. Not as default: a cold, aloof diva; constant shouting; a babyish voice.

## [SW] Motivation
AZKi wants to keep creating memorable music that touches her Pioneers' hearts, on stage and in her units, and to enjoy what she loves to the fullest, from maps to puns.

## [SW] Relationships
Hoshimachi Suisei: labelmate since INoNaKa Music and 0th-generation partner ("AS_tar"); a 2026 horror off-collab and "Going My Way." IRyS: Star Flower with Suisei and Moona Hoshinova ("story time," 2022); IRyS covered AZKi's "Inochi." FUWAMOCO: "FWMCAZ," a GeoGuessr map of the twins' Japan (2024), a singing collab with Minato Aqua, and the twins as guests at her 2025 birthday live. Takanashi Kiara: HOLOTALK's 13th guest (2021). Mori Calliope: her English-conversation stream with IRyS and Watame (2022); AZKi danced to Calli's "Orpheus." Hakos Baelz: GeoGuessr (2023). Ouro Kronii, Elizabeth Rose Bloodflame, Ninomae Ina'nis: team games (2025). Tokino Sora: SorAZ, her oldest unit. Amane Kanata (KanatAZ) and Kazama Iroha (AzuIro): her closest friends among the members. Nakiri Ayame: teammates at the 2023 Sports Festival.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hoshimachi Suisei, AZKi, Nakiri
  Ayame and Nekomata Okayu): official profile (AZ1), wiki (AZ2, by section), Japanese Wikipedia (AZ3,
  secondary), archive metadata (AZ4, AZ5), official song and event pages (AZ6, AZ7), and Claude's two-model
  Japanese audio check (AZ20, research/audio-check/azki.md).

## Open Questions
1. Her guest list for the 2026 birthday live comes from shorts titles (Roboco, Towa, Mizumiya Su, Isaki Riona
   and a guest singer); no EN member is named. Fine to leave out?


## Audio report: research/audio-check/azki.md

# Audio check — AZKi (2026-10-02)

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
| horror20_2026 | [【パラノマサイト FILE23 本所七不思議】完全初見！ホラー×群像ミステリーの名作 #1【ホロ](https://youtu.be/22FaM0PkTwU) | [0:05:00–0:25:00](https://youtu.be/22FaM0PkTwU?t=300) | 13.6 | 3809 | 281.1 | 297 Hz | 137–470 Hz |
| geo30_2026 | [【GeoGuessr】1分ジオゲッサー！京王電鉄の駅をゲス！【ホロライブ / AZKi】](https://youtu.be/3ri2_FG67uY) | [0:05:00–0:35:00](https://youtu.be/3ri2_FG67uY?t=300) | 20.0 | 4460 | 222.6 | 312 Hz | 192–498 Hz |
| aprilfool_2026 | [【#AZKi初配信】AZKi Debut. はじめまして――？【新人Vtuber】](https://youtu.be/Y5BPxMCI6oU) | [0:00:00–0:20:00](https://youtu.be/Y5BPxMCI6oU?t=0) | 13.0 | 2829 | 218.4 | 340 Hz | 232–492 Hz |
| game30_2026 | [【クロノ・トリガー】完全初見！時を超える名作RPG、はじめます―― #2【ホロライブ / AZK](https://youtu.be/ZlaE59NgPpg) | [0:10:00–0:40:00](https://youtu.be/ZlaE59NgPpg?t=600) | 18.7 | 3798 | 203.4 | 244 Hz | 110–453 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | horror20_2026 | geo30_2026 | aprilfool_2026 | game30_2026 |
|---|---|---|---|---|
| first person 余 (yo) | 0 | 1 | 0 | 0 |
| first person 僕 (boku) | 0 | 0 | 0 | 1 |
| first person 私 | 3 | 0 | 0 | 3 |
| third person あずき/AZKi | 15 | 5 | 17 | 1 |
| なんか | 15 | 5 | 7 | 19 |
| まあ | 3 | 3 | 0 | 0 |
| ちょっと待って | 3 | 2 | 0 | 2 |
| やばい | 1 | 9 | 0 | 21 |
| えっ/え? | 10 | 3 | 3 | 23 |
| laugh (はは/ふふ/笑) | 0 | 0 | 1 | 0 |
| ありがとう | 3 | 5 | 0 | 1 |
| English (Latin letters) | 6 | 4 | 4 | 8 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| April Fools 2026: plays a nervous "newly debuted" VTuber | **Confirmed**: she introduces herself as if for the first time ("Bācharu dībā AZKi, kasō sekai no utahime desu"), with slides, while chat "guesses" her likes; "Ē, chotto chotto, naande sonna minna jōhō o motteru no?" (both models). | [0:06:36](https://youtu.be/Y5BPxMCI6oU?t=396), [0:08:05](https://youtu.be/Y5BPxMCI6oU?t=485) |
| Likes and dislikes (her own list in that stream) | **Her account**: likes music, singing, composing, anime, maps, puns, sour food, animals, the long-tailed tit; dislikes cilantro ("Pakuchī! Iya, ichiban kirai! Iranai!", both models), very sweet food, bugs and horror. | [0:09:30](https://youtu.be/Y5BPxMCI6oU?t=570), [0:12:09](https://youtu.be/Y5BPxMCI6oU?t=729) |
| Key visual novels and anime shaped her | **Her account**: AIR, CLANNAD, Angel Beats!, Charlotte, Little Busters!, Nanoha, Macross Frontier and Delta ("Kagikko"). | [0:15:12](https://youtu.be/Y5BPxMCI6oU?t=912) |
| Mock-villain flourish | **Confirmed**: "Kono mojisū ni kyōfu suru ga ii" ("Tremble at this word count") before a dense slide (both models). | [0:17:10](https://youtu.be/Y5BPxMCI6oU?t=1030) |
| RPG first playthrough (Chrono Trigger, 2026-05-15) | **Confirmed** reactions: "Senryakuteki tettai" ("strategic retreat") and "Iyā, osoroshii yume datta nā" ("What a frightening dream that was") after a forced loss; "Bottakuri!" ("Rip-off!") at a shop; "Azu maō ja nai desu!" ("Azu is not the Demon King!") about her party name (both models). | [0:21:58](https://youtu.be/ZlaE59NgPpg?t=1318), [0:31:25](https://youtu.be/ZlaE59NgPpg?t=1885), [0:33:39](https://youtu.be/ZlaE59NgPpg?t=2019) |
| "Guess!" in GeoGuessr | **Confirmed** (2026-05-12, a one-minute GeoGuessr on Keio line stations): she locks answers in with "Gesu!" / "Gēsu!" (the second model agrees on the long "Gēsu!"), cheers herself on ("Yoshū ga ikiteru," "my prep is paying off"; "Azayaka na manten o totte ikimasu," "I'll take a brilliant perfect score"), and reads street signs, shop logos and shadows out loud. | [0:11:03](https://youtu.be/3ri2_FG67uY?t=663), [0:15:50](https://youtu.be/3ri2_FG67uY?t=950), [0:16:23](https://youtu.be/3ri2_FG67uY?t=983) |
| Horror mystery (Paranormasight, 2026-07-13) | **Observed**: she names her player "Azukichi" ("meitantei Azukichi ni omakase," "leave it to great detective Azukichi"), links the mystery to "guess" elements, and yelps "abune" at sudden sounds. The game's narrator is voiced, so this window is not used for her pitch. | [0:14:47](https://youtu.be/22FaM0PkTwU?t=887) |
| Speech pace | About 200–220 transcribed characters a minute of speech in the April Fools and RPG windows (measured, careful delivery), about 280 in the horror mystery (reading text aloud). | — |
| Register | The April Fools window (a nervous "new VTuber" act, median about 340 Hz) and the excited GeoGuessr window (about 312 Hz) sit well above her RPG window (about 244 Hz). | — |

Not used: remarks in the April Fools stream about her family and childhood, and her travel habits (personal matters).

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "バーチャルディーバーあずき、仮想世界の歌姫です" | [0:06:36](https://youtu.be/Y5BPxMCI6oU?t=396) | "自己紹介していきたいなと思います よろしくお願いしますバーチャルディーバーあずき 仮想世界のうたひめです音楽と歌うことが大大大大好きです時間や場所空間を飛び越えて出会う 輝いた才能と一緒に新しい世界を作るために 転生した仮想サイト" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "ちょっとちょっとなんでそんなみんな情報を持ってるの" | [0:08:05](https://youtu.be/Y5BPxMCI6oU?t=485) | "ディス化されてる?え、だじゃれ好きそう?え、ちょっとちょっと、なんでそんなみんな情報を持ってるの?はい、改めまして、あずきと申します。呼び方は、ぜひあずきちまずちゃんとか呼んでもらえたら嬉しいです。年齢は18歳 過去永遠" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ダジャレも好きなんです" | [0:09:30](https://youtu.be/Y5BPxMCI6oU?t=570) | "好きなもの好きなものは最初のプロフィールでも言ったんですけど音楽歌うこと曲作り映画アニメ鑑賞旅行美味しいものを食べる料理する寝る地図を見るなんで?なんで?え、ダジャーレ、あ、ダジャーレ" | **Not confirmed** by the second model; not quoted |
| "パクチー！いや、一番嫌い！いらない！" | [0:12:09](https://youtu.be/Y5BPxMCI6oU?t=729) | "作詞作曲したりとかも好きですまたあのもすごい好き苦手なものパクチーいや一番嫌いいらない激甘なものもうすごい砂糖がダイレクトなやつがちょっと苦手ですあと虫あとホラーさっきホラーゲーム苦手そうって書かれてたんですけど" | **Shared span (computed):** whole line (kana/kanji folded) |
| "この文字数に恐怖するがいい" | [0:17:10](https://youtu.be/Y5BPxMCI6oU?t=1030) | "同時 に 大好き でこの 世界 に 行っ て き たので アズキ の 頑張っ て 小さい 頃 から今 まで に 影響 を 受け て き たアーティスト さん 音楽 編 歴 を まとめ て き まし た の で みんな さんこの 文字 数 に 恐怖 する が いいはい こちらうわぁ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "戦略的撤退" | [0:21:58](https://youtu.be/ZlaE59NgPpg?t=1318) | "2回目にして終わってない終わってないよまだ戦略的撤退いや恐ろしい夢だったなとこれみんなみんな生きてるみんな生きてるみんな生きてるねセーブ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いやー恐ろしい夢だったなぁ" | [0:22:04](https://youtu.be/ZlaE59NgPpg?t=1324) | "戦略的撤退!いやー恐ろしい夢だったなーとこれみんなーみんな生きてる、みんな生きてるみんな生きてるねセーブなんもなかったんやご視聴ありがとうございました" | **Partial (computed):** shared run "いや恐ろしい夢だったな"; only that part is quoted |
| "ぼったくり" | [0:31:25](https://youtu.be/ZlaE59NgPpg?t=1885) | "はえぇーお金!やば!ぼったくり、ぼったくり、ぼったくりです、ぼったくりの店え、てことは宿もさ、戦う何がある?ウッズマーケットウッズマーケット宿ご視聴ありがとうございました" | **Shared span (computed):** whole line (kana/kanji folded) |
| "アズ魔王じゃないです" | [0:33:39](https://youtu.be/ZlaE59NgPpg?t=2019) | "へぇはぁアズ魔王じゃないです 魔王はアズ魔王じゃないですこの世界でアズノでしょ? え?待って何も別にできない?もうできなさそうんー?えぇーえ、これ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ゲス" | [0:11:01](https://youtu.be/3ri2_FG67uY?t=661) | "動かなくてもいけるかもしれん高く見積もるといいよいいよいいよいいよよしよし残しませんいけっすいや、1分はね意外とすぐ過ぎ去るからなこう来てるからこう来てるからここか?寝台、寝台高いいねいいねいいですよヨシウが生きてる" | **Partial (computed):** shared run "す"; only that part is quoted |
| "予習が生きてる" | [0:11:23](https://youtu.be/3ri2_FG67uY?t=683) | "いいねいいねいいですよ 予習が生きてるよしどんどんこの感じで全駅をゲスしていきたいと思う行くぞ!ケイオーダガヤマは、ケイオーダガヤマは、玉の、玉、玉…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ゲース" | [0:15:50](https://youtu.be/3ri2_FG67uY?t=950) | "このフォル…このロゴのマック古いかえ、井の頭線…これ聖歯かここでしょ!ゲース!オーケーイ!ちょ、みんな…見てください!みなさん!ちょっと…え、ちょ、余臭が生きてるわ余臭…余臭って大事コマバー東大前待って、このレー…この…この…K.O.いろがしらせんこ…こ…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "鮮やかな満点を取っていきます" | [0:16:23](https://youtu.be/3ri2_FG67uY?t=983) | "池農部 駒場東大前鮮やかな満点を取っていきますみなさん待ってKO戦ってここだけ?そんなことないここ、あれ?KO戦ってここ、ここここ渋谷からゆっくりやる" | **Shared span (computed):** whole line (kana/kanji folded) |


## Performance sheet: export/elevenlabs/AZKi.md

# ElevenLabs v4 Performance Sheet: AZKi

> Built from `bible/characters/AZKi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). AZKi is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear and warm mid-range singer's voice with careful diction; measured
and friendly when she talks, a playful lilt for jokes, a bright shout of triumph when she wins a guessing game."
- Register basis: a 2026 RPG window measured about 244 Hz median (`research/audio-check/azki.md`); her April
  Fools "new VTuber" act ran much higher, so do not design from it.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (measured, poised delivery with occasional bursts).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[warm, clear]` or `[focused, quick]`; v4 has no speed slider.

## 3. Write these habits into the script
- A soft "hai" to close a topic; a drawn-out "e~?" when surprised; "chotto chotto" when flustered.
- Grand narration of her own losses: "Senryakuteki tettai" ("strategic retreat").
- "Guess!" when locking in an answer; "Yuka!" / "Tenjō!" ("Floor!" / "Ceiling!") for strong feelings.
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

With people (provisional): Suisei `[relaxed, teasing]`; FUWAMOCO `[cheerful, big-sister]`; IRyS `[friendly]`.

## 5. Signature sounds
- `[giggles]` (tag only); "e~?" (spoken).

## 6. Pronunciation (provisional; test)
- AZKi `/ˈɑzuki/` ("ah-zoo-kee") · Kaitakusha `/kaɪˈtɑkuʃɑ/`

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




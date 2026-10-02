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
- The author ordered Hakos Baelz added (2026-10-02) and said Tsukumo Sana is not to be made; Sana appears only as
  a graduated Council genmate.
- This run must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation, so
  keep to about 15 tool calls in total, including web searches; batch local lookups. Prioritize the exported
  [SW] fields of the two new cards, then the Bae lines added to other cards (listed below), then the sheet.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git). The new
  cards are not yet in `bible/`; their full text is inline below. Do not re-open the inline files.
- Two facts rest on Bae's own words in her fes after-talk (ASR): her 2026 fes final solo ("Idol") and
  "Kakumei Dualism" with Natsuiro Matsuri. If you can open an official fes report, check them.
- If the budget runs short, stop and report what you could not check in the Verification note.

## Card 1: Hakos Baelz (character; draft, full file)

---
kind: character
name: "Hakos Baelz"
sw_section: Characters
---

# Character File: Hakos Baelz

> Scope: official lore and publicly shown persona only, checked 2026-10-02. Bae is active at the 2026-09-30
> baseline; her recent streams (2026) set her default manner, per the project's recency rule. Nothing about the
> performer behind the avatar: private-life information (where she lives, health, family, pets, school,
> nationality and the like) is outside scope and is not recorded here, including what the wiki lists. Her
> Australian accent is recorded only as a voice feature. In stories she knows she is a streamer with a
> persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; HB20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (HB#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked about 1.7 hours of archived 2026 recordings (HB20: the
> opening, middle and close of an April 2026 chatting stream, half an hour of her March 2026 fes after-talk,
> and half an hour of a Tomodachi Life stream; see research/audio-check/bae.md). Only in-scope public
> performance material is used; long stretches of the chatting stream are about personal matters and are not
> quoted. The audio was machine-transcribed and acoustically measured; transcripts were reviewed in context,
> without independent listening verification.

## One-line Concept
"Your worldwide Rat Idol": Chaos itself in the form of a cute little rat, the Council's reluctant
chairperson who would rather break every rule and watch, and on stream a loud, fast, self-mocking singer and
dancer who ends up the most "normal" one in the room, thanks every gift with "boom, boom, boom" and wants
each stage to top the last. [Official HB1] [Observed HB2 §Personality, secondary] [ASR HB20]

## Core Drive
- **Want:** to perform and keep leveling up: "I need to level up somehow," she says of planning each fes
  stage a year ahead; her official profile calls her "a performer looking for her next stage." [Official HB1]
  [ASR HB20]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror, especially paranormal horror and jump scares (she plays it anyway,
  with friends); the dark. [Official HB1] [Observed HB2 §Likes and dislikes, secondary]
- **Values shown in public:** effort she can show on stage (choreographing her own fes solo, learning to
  breakdance for it); gratitude to her chat ("thank you so much" more than once a minute while reading
  superchats); cheering people on ("you're doing great"). [ASR HB20] [Observed HB2 §Quotes, secondary]

## Core Contradiction
The primordial force of Chaos, appointed to chair the Council, who mostly watches the mayhem from the side;
the loud, bright "rat idol" who, by fan consensus, became the straight woman of her generation, "the victim of
her genmates' antics." [Official HB1 (original lore)] [Observed HB2 §Personality, secondary]

## Behavioral Traits
1. Loud, quick and self-mocking: she calls herself stupid for laughs ("Bae is stoopid," "BIG BRAIN!"),
   narrates her own disasters, and answers absurdity with "bruh." [Observed HB2 §Quotes, secondary] [ASR HB20]
2. A performer who over-prepares on purpose: at the 2026 fes she closed as the final solo act with "Idol,"
   choreographing it herself and ending in a breakdance she had started learning only a few months earlier,
   after years of fans joking that she would one day breakdance on stage. [ASR HB20, her own account]
3. Runs shows and bits: "Febaerary" (streaming every day of February up to her 29 February birthday; 2026 was
   her fifth), the "Midnight Monday Radio" talk-and-karaoke program, "BAE-CADEMY" lessons with guests, a
   24-hour "#BaeTV24" marathon of collabs (2024), dramatic readings ("BAE THEATRE"). [Observed HB2; HB3
   titles] [ASR HB20]
4. Plays along with chat's fictions: in April 2026, after her own new song got her stream archive claimed,
   she staged a mock feud with "Hakos Bells," the "artist" who claimed it, and promised an exposé. She also
   has a male alter ego, "Hayko," her "intolerable cousin." [ASR HB20] [Observed HB2 §Miscellaneous,
   secondary]
5. "Zoomer" jokes: chat teases her for not recognizing older pop culture (she thought the PS1 was a handheld);
   she plays the bit up. [Observed HB2 §Miscellaneous, secondary]
6. Scared of horror and plays it anyway: her 2022 "Month of Horrors" with Fauna, Lethal Company squads, a
   2026 Resident Evil series with Cecilia. [Observed HB3 titles] [ASR HB20]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "WAZZUP!! It's your worldwide Rat Idol --- Hakos Baelz!" [Official HB1]
  - Self-introduction (wiki-recorded): "Wazzup! I am Chaos the end of ends, a steel rose trapped in a cage of
    ice, your best friend Baelz Hakos from hololive English Promise, WITNESS ME". She still opened her April
    2026 chat with a version of it (the first model garbles it, so it is not quoted from audio).
    [Observed HB2 §Quotes, secondary] [ASR HB20, DOZ8rRVH03c 0:04:46, first model only]
  - Sign-off (2026): after plugging her newest song ("Please stream my newest song, Snake Eyes, and also my newest cover…") and
    the next collab, she leaves with a quick "okey dokey" and "bye-bye" (both models hear those words; the words
    between differ, so no full line is quoted). [ASR HB20, DOZ8rRVH03c 2:19:11–2:20:03]
  - Wiki-listed: "SARABA DA!" [Observed HB2 §Quotes, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Boom, boom, boom" → thanking each gift and superchat; about 38 times in an hour of 2026 chat, alongside
    "thank you so much" (about 128). [ASR HB20, first-model counts]
  - "Bruh." / "Everything comes back to 'Bruh'." → absurdity. [Observed HB2 §Quotes, secondary] [ASR HB20]
  - "You're doing great!" → cheering chat or a friend. [Observed HB2 §Quotes, secondary] [ASR HB20]
  - Mock outrage with a conspiracy: "It was sabotage." … "They hate promise. They hate us. It's a
    conspiracy." → a small failure on stream. [ASR HB20, DOZ8rRVH03c 0:06:53, 0:08:27; both models]
  - The "Hakos Bells" feud (2026): "Here I am trying to promote her new song." … "Does she really think
    that me, of all people, is trying to clout chase by using her?" … "Breaking news! Bae is trying to clout
    chase by…" → a running bit with chat. [ASR HB20, DOZ8rRVH03c 2:12:26–2:13:16; separate shared spans]
  - Self-answering storytelling: "Who would think that's a good idea? Me." (on putting a breakdance in the
    last 16 counts of a song) and "Okay, I guess I'm doing this now. Confused rat." [ASR HB20, sPXphrWUOQU
    0:49:26, 0:38:05; both models on the quoted spans]
  - Welcoming members: "Welcome to the Rat Pack, welcome, welcome." [ASR HB20, DOZ8rRVH03c 0:42:50; both
    models]
  - "JDON MY SOUL" (a mishearing from a telephone-game collab) and "Oui oui pp." (wiki-listed bits).
    [Observed HB2, secondary]
- **Vocabulary / fillers:** "like" (about 111 in an hour), "yeah," "okay," "crazy" ("That's crazy," about
  20), "oh my god / oh my gosh," "guys," "you know," "we'll see," "mayhaps," "yap"; "senpai" for her seniors
  even in English. [ASR HB20, first-model counts]
- **Profanity:** moderate and casual ("damn," "God damn it," "hell yeah," a joking "bitch" at her fictional
  rival), plus "frickin'" and "bruh." [ASR HB20]
- **Accent and language:** English with an Australian accent (a voice feature only); fluent Japanese on stream
  (she also holds Japanese chatting streams) and Japanese terms such as "senpai"; she refers to herself as
  "boku" in Japanese (secondary). Keep her fillers and self-corrections; never caricature the accent.
  [ASR HB20] [Observed HB3 titles; HB2 §Miscellaneous, secondary]
- **Laughs, noises:** quick bursts of laughter at her own disasters; "ORA ORA ORA" (wiki-listed); a dramatic
  gasp for a mock scandal. [Observed HB2, secondary] [ASR HB20]
- **Rhythm & rhetoric:** fast and run-on when telling a story (about 120–133 words a minute of speech in
  2026 chat), with rhetorical questions she answers herself ("Who would think that's a good idea? Me."),
  repeated words for emphasis ("so many things, so many things") and mock-dramatic narration. [ASR HB20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (HB20; three 2026 chat windows): window medians about 200–233 Hz (p10–p90 about 147–379 Hz). Measurements describe the sampled recording and ASR segmentation; they
    are not isolated vocal measurements. The Tomodachi Life window is excluded (game voices).
  - Provisional (interpretation): a bright, punchy mid-range voice that jumps up for jokes and drops into deadpan
    for "bruh"; loud and quick when excited, warm when thanking. A listening check would still need to establish
    timbre and accent details.
- **Sounds off:** a slow, sleepy or breathy default; cruelty; a menacing villain voice outside a clear bit; an
  accent caricature.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Loud, bright, theatrical | "WAZZUP!! It's your worldwide Rat Idol" (HB1) |
| Thanking gifts | Quick, warm, rhythmic | "Thank you so much … boom, boom, boom." (ASR HB20) |
| Telling a stage story | Fast, run-on, self-mocking | "Who would think that's a good idea? Me." (ASR HB20) |
| Mock scandal | Gasping, theatrical | "Does she really think that me, of all people, is trying to clout chase by using her?" (ASR HB20) |
| Absurdity | Flat, deadpan | "Bruh." (HB2; ASR HB20) |
| Cheering someone | Warm, sincere | "You're doing great!" (HB2; ASR HB20) |
| Horror game | Panicked, loud | "I don't like this. I wanna leave." (HB2, secondary) |

### Sample Lines
1. "WAZZUP!! It's your worldwide Rat Idol --- Hakos Baelz!" (Official HB1)
2. "It was sabotage." … "They hate promise. They hate us. It's a conspiracy." (ASR HB20, DOZ8rRVH03c 0:06:53, 0:08:27; two separate shared spans)
3. "Five years! Has it been five years? Oh my god, it is." (ASR HB20, 0:33:20, on her fifth Febaerary)
4. "Everything gets better. If you're at the bottom, you can only go up. You're doing great." (ASR HB20, 0:58:39, to a viewer)
5. "Does she really think that me, of all people, is trying to clout chase by using her?" (ASR HB20, 2:13:07, the "Hakos Bells" bit)
6. "They decided to put me as the final solo act this year. When I found out, guys, I was so stressed." (ASR HB20, sPXphrWUOQU 0:31:24)
7. "A lot of people have been making jokes that eventually I'm just gonna start breakdancing on stage." … "And I also was treating it as a joke and then it suddenly became not a joke." (ASR HB20, sPXphrWUOQU 0:43:15–0:43:22; two shared spans)
8. "Who would think that's a good idea? Me." (ASR HB20, sPXphrWUOQU 0:49:26)

## Appearance Anchors (avatar)
- 149 cm; illustrator Mika Pikazo. Bright red hair in two big pigtails with a white streak in the left bang;
  large pink mouse ears and a long thin tail tied with a blue ribbon; her mascot Mr. Squeaks, a small red-and-teal
  mouse, rides on her head. An off-shoulder white crop top reading "RAT," one red and one yellow oversized sleeve
  ending in teal paw mitts, a black-white-red panel skirt, mismatched legwear (a yellow-and-black stocking on
  one leg, a red sock on the other), black platform shoes and a yellow "Chaos Toy" side bag. [Official HB1]
  [Observed HB2 §Appearance, secondary]
- Her oshi mark is 🎲. Later looks include a strawberry-princess chibi model, a 2024 gothic outfit, a 2025
  strawberry loungewear outfit and a 2026 3D outfit (a black crop top with a white spark pattern) from her
  "ReCOLOR" birthday live. [Observed HB2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Chaos itself, "birthed by the world"; appointed chairperson of the Council by the gods, though she takes a hands-off approach; breaks rules and watches the aftermath; a rat by form, "chaos" by species; age unknown ("roll a dice"); born on 29 February (in fan-recorded lore, Kronii created leap years to hold her) | [Official HB1 (original lore)] [Observed HB2 §Lore, secondary] |
| 2021-08-23 JST | Debut, fifth and last of hololive English -Council- (08-22 PDT); she closed by singing "Fuwa Fuwa Time" | [Official HB1] [Observed HB2] |
| 2021-09-24 | First collab outside her generation: Keep Talking and Nobody Explodes with Takanashi Kiara | [Observed HB2; HB3 579F-lu2cKY] |
| 2022 | The CHADCast podcast with IRyS and Mori Calliope; the first "Febaerary"; first original song "PLAY DICE!" (02-28) | [Observed HB2; HB3; Calli file C12] |
| 2022-08-23 | Council's first group original song "Rise" | [Observed HB2] |
| 2022-10 | "BAE & FAUNA'S MONTH OF HORRORS" | [Observed HB2; HB3] |
| 2023-03-19 | 3D debut at hololive 4th fes. "Our Bright Parade"; her own 3D debut stream 2023-09-30 | [Observed HB2] |
| 2023-07-02 | hololive English 1st concert "-Connect the World-"; EP "Pandæmonium" (07-07) | [Observed HB2] |
| 2023-10-09 JST | hololive English -Promise- formed with IRyS, Fauna, Kronii and Mumei | [Observed HB2; Promise card] |
| 2024-02-29 | Original "RxRxR" and first album "ZODIAC" | [Observed HB2] |
| 2024-08-24/25 | -Breaking Dimensions-: "Our Promise" with Promise; "BLUE CLAPPER" with Calli, IRyS and Koseki Bijou; solo "GEKIRIN"; "High Tide" with IRyS, Moona Hoshinova and Hoshimachi Suisei | [Official HB5] |
| 2024–2025 | World Tour '24 -Soar!- performer (New York to Taipei); holoMeet ambassador 2024; World Tour '25 guest in Sydney with Kronii | [Official HB6] [Observed Concerts card] |
| 2024-11-25 | "#BaeTV24" 24-hour stream with collabs (IRyS and Raora; Kronii, Bijou and Gigi) | [Observed HB3] |
| 2024-12-14 | Promise musical "The Broken Promise" | [Observed HB2] |
| 2025-02-28 | Original "FEAST"; birthday 3D live "-KAGURA- Dance of the Gods" | [Observed HB2; HB3 viPlIHvk724] |
| 2025-08-23/24 EDT | -All for One-: "R x R x R" with Calli; "Countach" with Gigi and Kureiji Ollie; solo "La Roja (Arrange ver.)" | [Official HB5] |
| 2026-02-28 | Birthday 3D live "ReCOLOR" with a new 3D outfit; original "SNAKE EYES"; her fifth Febaerary | [Observed HB2] [ASR HB20] |
| 2026-03-06/08 | hololive 7th fes. "Ridin' on Dreams": the final solo act ("Idol," her own choreography with a breakdance finish) and "Kakumei Dualism" with Natsuiro Matsuri; a venue talk with Cecilia Immergreen | [ASR HB20, her own account] |
| 2026-04 | Resident Evil series with Cecilia on Cecilia's channel; the "Liar Dancer" cover; the "Hakos Bells" mock feud | [ASR HB20] |
| 2026-07-03/04 PDT | Serendipity: BaeRyS with IRyS ("LUVATORRRRRY!"), "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame (day 1) | [Official HB4, HB5] |
| 2026-08-23 | 5th anniversary: announces her 1st concert "REGALIA" (2026-12-01, after the baseline) and 2nd album "Mirror Mirror"; original "I found me" | [Official HB7] [Observed HB2] |
| 2026-09-07 | Branches merge into one "hololive"; her unit is hololive -Promise- | [Official HB1] |

## Relationship Map
Public exchanges only. Group-wide ties are on "hololive -Promise-"; her ties with the whole cast are on
"Hakos Baelz Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| IRyS | Promise genmate; "BaeRyS" | The running "married/divorced" bit (from a 2021 Minecraft bento); a "Gisneyland" off-collab and the "Daikirai na Hazu Datta" cover (2023); a Valentine bento handcam (2024); "High Tide" on stage (2024); Snow Bros. 2 (2025); BaeRyS at Serendipity (2026). Bae: IRyS was "the very first senpai I had ever met"; "I was blown away by her voice." IRyS: Bae "always comes up with ideas I wouldn't think of." | [Official HB4] [Observed HB3; IRyS file] |
| Mori Calliope | Myth senior; CHADCast cohost | The CHADCast podcast with IRyS (from 2022) and "Here Comes the CHADCast" (2026); "BLUE CLAPPER" with IRyS and Bijou (2024); the "R x R x R" duo at -All for One- (2025); a GriMoire watch-along (2025). Bae calls her "Cori Malliope"; fans note they share a Live2D rigger, so Bae calls her "sister" (secondary) | [Official HB5] [Observed HB3; HB2; Calli file] |
| Ouro Kronii | Council/Promise genmate | Calls Kronii "too talented, savage, and a 'tsundere granny'"; Sandwich Review (2022), Digimon Survive ("takronii and agubae," 2022), Fortnite (2024), UNO on #BaeTV24 (2024); World Tour '25 Sydney guests together; in fan lore Kronii created leap years to hold Bae's birthday | [Observed HB3; Kronii file; HB2 §Lore, secondary] |
| Ceres Fauna | Council/Promise genmate (graduated 2025-01-03) | At debut Bae called her "a natural mama, a soothing beauty, and someone who gives the best headpats"; "BAE & FAUNA'S MONTH OF HORRORS" (2022); Lethal Company "sweaty gang" with Kaela and Bijou (2024); "MUFAUBAE" with Mumei (secondary) | [Observed HB3; Fauna file; HB2] |
| Nanashi Mumei | Council/Promise genmate (graduated 2025-04-27/28) | Bae called her "the cutest voice" in Council at debut; "preYdator" (secondary); BAE-CADEMY anatomy lesson (2024), WarioWare and ASMR off-collabs (2024), Overwatch 2 (2025); Mumei's farewell-week collab with IRyS and Kronii (2025) | [Observed HB3; HB8; Mumei file] |
| Koseki Bijou | Advent kouhai; "BaeBi" | We Were Here Expeditions (2023, "baebis"), a JoJo watch-along (2024), the "#BAEBISleepover" (2024-08-11/12), UNO on #BaeTV24; "BLUE CLAPPER" on stage (2024); she made a Bijou Mii in Tomodachi Life (2026) | [Observed HB3] [Official HB5] [ASR HB20] |
| Cecilia Immergreen | Justice kouhai; "BratTea" | Their running coffee-versus-tea debate, continued at a 2026 fes venue talk they did together; a Resident Evil series on Cecilia's channel (2026); Bae jokes that Cecilia only calls her "senpai" when she wants something | [ASR HB20] [Cecilia file, secondary] |
| Gigi Murin | Justice kouhai | "Countach" with Kureiji Ollie at -All for One- (2025); a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025); UNO on #BaeTV24; Gigi's Spring Party collab with FUWAMOCO (2025) | [Official HB5] [Observed HB3; HB8] |
| Raora Panthera | Justice kouhai | Super Mario Party Jamboree with IRyS on #BaeTV24 (2024); "Amber Coin" guildmates with Kiara and Mumei in ENReco (secondary) | [Observed HB3; HB2] |
| Elizabeth Rose Bloodflame | Justice kouhai | "HELP!!" with Kobo Kanaeru at Serendipity (2026) | [Official HB5] |
| FUWAMOCO (Fuwawa, Mococo) | Advent kouhai | Gigi's Spring Party collab (2025); they danced to "bae-senpai's new song SNAKE EYES" in a 2026 short | [Observed HB8] |
| Takanashi Kiara | Myth senior | Her first collab outside her generation (Keep Talking and Nobody Explodes, 2021); World Tour '24 together; "Amber Coin" in ENReco (secondary) | [Observed HB3; HB2] [Official HB6] |
| Ninomae Ina'nis | Myth senior | The K/DA "POP/STARS" cover with Moona and Ayunda Risu (2023); a BAE-CADEMY art lesson with "Ina-sensei" (2024); Ina's AmiAmi special featuring Bae (2025); World Tour '24 together | [Observed HB3; HB8] [Official HB6] |
| Watson Amelia | Myth senior (affiliate since 2024-09-30) | Bathroom reviews ("#BaethingAme," 2022), a VRChat Holoween escape-room behind-the-scenes (2022), an Apex off-collab (2023) | [Observed HB3] |
| Gawr Gura | Myth senior (graduated 2025-05-01) | Urban Dictionary Challenge with Kronii, Mumei and Gura (2022) | [Observed HB3] |
| Kobo Kanaeru (ID) | Cross-branch | "HELP!!" with Elizabeth at Serendipity (2026) | [Official HB5] |
| Kureiji Ollie (ID), Ookami Mio (GAMERS) | Cross-branch | She calls Mio her "mom" and Ollie "another mom" (secondary); "Countach" and HoloEarth with Ollie | [Observed HB2; HB3] [Official HB5] |
| Natsuiro Matsuri (JP) | JP senior | "Kakumei Dualism" together at the 2026 fes; Bae took the T.M.Revolution part | [ASR HB20] |
| Moona Hoshinova (ID), Hoshimachi Suisei (JP), Pekora, Ayunda Risu | Cross-branch | "High Tide" with IRyS, Moona and Suisei (2024); "holorodents" with Pekora and Risu (secondary) | [Official HB5] [Observed HB2] |

## Arc
- **Starting point:** active at the 2026 baseline: a busy 2026 (the "ReCOLOR" birthday live and "SNAKE EYES,"
  the final solo at fes, Serendipity with IRyS), preparing her first solo concert "REGALIA" and album
  "Mirror Mirror."
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a stage idea that is one level too ambitious; a mock feud with a fictional rival; a
  horror game she should not have started; chaos she swears she did not cause ("It was sabotage").
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Bae rehearses a breakdance finale in a hallway and recruits Kronii as a reluctant timekeeper.
  2. BaeRyS "divorce" proceedings, with Calli presiding as CHADCast judge.
  3. "Hakos Bells" claims Bae's stream again; Bae livestreams the exposé.
  4. A coffee-versus-tea summit with Cecilia that ends with both sides ordering hot chocolate.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.) The BaeRyS "marriage" is a running comedy bit, not a real relationship; keep it as banter.

## Hard Facts (continuity)
- Debut 2021-08-23 (JST; 08-22 PDT), the last of -Council-; birthday 29 February; 149 cm; illustrator Mika
  Pikazo; fans "Brats" (also written "Baerats"); members "Rat Pack"; mascot Mr. Squeaks; oshi mark 🎲.
- Unit: hololive English -Council- (2021), -Promise- (from 2023-10-09 JST), "hololive -Promise-" since the
  2026-09-07 merger; Promise's active members at the baseline: IRyS, Kronii, Bae.
- Official stage units: BaeRyS with IRyS (Serendipity 2026); CHADCast trio with Calli and IRyS.
- Upcoming after the baseline: 1st concert "REGALIA" (2026-12-01; date from the wiki, the official site opened
  2026-09-28) and 2nd album "Mirror Mirror."

## Sources (checked 2026-10-02)
- HB1 Official profile: https://hololive.hololivepro.com/en/talents/hakos-baelz/ (original Council lore in HB2 §Profile)
- HB2 Hakos Baelz wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/Hakos_Baelz
- HB3 Stream archive metadata, her channel (archive.ragtag.moe): 579F-lu2cKY (Kiara, 2021-09-24), jWvpe0Hs5wI
  (Kronii, Mumei, Gura, 2022-08-20), xqvGnqstOAo and RuQZZlU0Vag (Kronii, 2022), bU49U1cQ02o, HjO8vHvoOsI,
  1cn8rP-tTOI (Ame, 2022–23), 9G6sya73UTc and HrT8Oon9Kxs (IRyS, 2023), pg6nLp3_KXo (IRyS, 2024-02-14),
  Osq_NSB3Fio (IRyS, 2025-04-17), K1BUHdbUIlE, eTzqNYjJzSA, GbDP3OGOZQI, rWL7HXdVYvQ (Bijou, 2023–24),
  EDUADGntHOE and T4aNVcCHSA8 (Ina, 2023–24), -DEoJhEl8ds, jTHvvjFsgUk, hP13ccUMOyg (Mumei, 2024),
  fa6iw7kpYaA (Fauna, Kaela, Bijou, 2024), Vb94AGQmsOM and NsQjJ4rv6pE (#BaeTV24, 2024-11-25), 9hADwEYOf4g
  (Gigi, 2025-02-05), 3SZgBJ8NolY (Calli's GriMoire watch-along, 2025-02-27), viPlIHvk724 (2025 birthday 3D live)
- HB4 Official Serendipity interview, IRyS and Bae (2026-06-05): https://serendipity.hololivepro.com/news/interview02
- HB5 Official concert reports: https://hololive.hololivepro.com/en/events/breaking-dimensions/,
  https://hololive.hololivepro.com/en/events/all-for-one/, https://hololive.hololivepro.com/en/events/serendipity/
- HB6 Official post-event report, World Tour '24: https://hololive.hololivepro.com/en/news/20250217-01-128/
- HB7 Official "REGALIA" concert site (opened 2026-09-28): https://regalia.hololivepro.com/
- HB8 Other members' archive metadata: -L2E0hwdYlA (Mumei, Overwatch 2, 2025-04-20), qckazzufZy4 (Gigi's
  Spring Party with FUWAMOCO and Bae, 2025-03-31), T7p6OcVMLXA (Ina's AmiAmi special, 2025-05-29),
  R3fg-ZeW69I (FUWAMOCO's SNAKE EYES short, 2026-03-20)
- HB20 Claude's audio check (two-model ASR): DOZ8rRVH03c (2026-04-07 chatting), sPXphrWUOQU (2026-03-10 fes
  after-talk), 2pn5_pZu8Q4 (2026-04-27 Tomodachi Life); research/audio-check/bae.md

---

## [SW] Name
Hakos Baelz

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Promise-, Promise, hololive English -Promise- (former branch name), hololive English -Council- (former), Council, BaeRyS, CHADCast

## [SW] Other Names
Bae, Baelz, Hakos, Rat Idol

## [SW] Personality
Bae streams as Chaos itself in the form of a cute little rat, the Council's reluctant chairperson who would rather break every rule and watch the aftermath. On stream she is loud, quick and self-mocking: she calls herself stupid for laughs, narrates her own disasters, answers absurdity with a flat "bruh," and blames small failures on sabotage and conspiracies. Fans joke that the chaos goddess became the "normal" one of her generation, the straight woman caught in her genmates' antics. She is a dedicated performer who keeps raising the bar: she choreographs her own stages, learned to breakdance for her 2026 fes solo, and plans each year's stage a year ahead. She plays along with chat's fictions, such as her 2026 mock feud with "Hakos Bells," keeps up running shows ("Febaerary," Midnight Monday Radio, BAE-CADEMY) and thanks every gift with "boom, boom, boom." She is scared of horror and jump scares and plays them anyway, loves coffee and fried cheese, and cheers people on: "You're doing great."

## [SW] Background
Bae is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her the concept of Chaos, "birthed by the world," whom the gods appointed chairperson of the Council; in fan-recorded lore she was born on 29 February and Ouro Kronii created leap years to hold her. She debuted on 2021-08-23 (JST), the last of hololive English -Council-, which became -Promise- with IRyS in October 2023; Promise's active members at the baseline are Bae, IRyS and Kronii. A singer and dancer, she has released originals such as "PLAY DICE!", "PSYCHO", "RxRxR", "FEAST" and "SNAKE EYES," the album "ZODIAC" and the EP "Pandæmonium," co-hosts the CHADCast podcast with IRyS and Mori Calliope, and holds "Febaerary," a month of daily streams before her birthday. At the English concerts she sang "GEKIRIN" solo and "BLUE CLAPPER" with the CHADCast trio and Koseki Bijou (2024), "R x R x R" with Calli and "Countach" with Gigi Murin and Kureiji Ollie (2025), and at Serendipity (2026) "LUVATORRRRRY!" with IRyS as BaeRyS and "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame. At the 2026 hololive fes she was the final solo act. In August 2026 she announced her first solo concert, "REGALIA," and her album "Mirror Mirror."

## [SW] Physical Description
Bae's avatar is 149 cm tall, with bright red hair in two big pigtails and a white streak in the left bang, large pink mouse ears and a long thin tail tied with a blue ribbon; her little red-and-teal mouse mascot, Mr. Squeaks, rides on her head. She wears an off-shoulder white crop top reading "RAT," one red and one yellow oversized sleeve ending in teal paw mitts, a black, white and red panel skirt, mismatched legwear (a yellow-and-black stocking, a red sock), black platform shoes and a yellow "Chaos Toy" side bag.

## [SW] Dialogue Style
Fast, loud, run-on English with an Australian accent, full of "like," "yeah," "okay," "oh my god" and "That's crazy"; she says "senpai" for her seniors even in English and streams fluently in Japanese too. She tells stories at full speed and answers her own questions ("Who would think that's a good idea? Me."), blames small failures on sabotage ("It was sabotage." "It's a conspiracy."), stages mock scandals with chat ("Breaking news!"), answers absurdity with a flat "bruh," and turns warm and sincere when she cheers someone on ("You're doing great."). Reading superchats she thanks each name with "thank you so much" and "boom, boom, boom." She swears casually ("damn," "God damn it," "hell yeah"). Keep her fillers, repetitions and self-corrections; never caricature the accent.

## [SW] Catchphrases
"WAZZUP!! It's your worldwide Rat Idol" (official greeting); "I am Chaos the end of ends, a steel rose trapped in a cage of ice, your best friend Baelz Hakos" (her self-introduction, wiki-recorded); "boom, boom, boom" (thanking gifts); "Bruh."; "You're doing great!"; "It was sabotage."; "It's a conspiracy."; "Breaking news!"; "That's crazy."; "Welcome to the Rat Pack"; "Technology be crazy."; "Confused rat."; from the wiki: "SARABA DA!", "BIG BRAIN!", "Bae is stoopid," "JDON MY SOUL," "ORA ORA ORA." Her fans are the Brats; her members, the Rat Pack.

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a bright, punchy mid-range voice, lower than most of her kouhai, with an Australian accent; fast and run-on when she tells a story, louder and higher for jokes, flat and deadpan for "bruh," warm and sincere when cheering someone on. Reading superchats she falls into a quick, rhythmic thank-you patter. Her laughs come in quick bursts at her own disasters, not after every line.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, punchy mid-range voice with an Australian accent; fast and loud by default. Default tags: [energetic, fast]. By situation: greeting [loud, theatrical]; telling a story [fast, self-mocking]; a small failure [mock outrage]; a mock scandal [gasps] then [theatrical]; absurdity [deadpan]; thanking gifts [quick, warm]; cheering someone [warm, sincere]; horror game [panicked]. With people (provisional, drawn from Relationships): IRyS [bickering, affectionate]; Kronii [teasing]; Calli and IRyS on CHADCast [loud, chaotic]; Bijou [playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): "boom, boom, boom" (spoken); [laughs] (tag only); [gasps] (tag only). Keep in the words: "bruh," "boom, boom," "senpai," "crazy," "Rat Pack," "Brats." Pronunciation guide (provisional, untested): Baelz /bɛlz/ ("bells"; many members say /beɪlz/), Hakos /ˈheɪkɒs/ ("hake-oss"), Bae /beɪ/, Febaerary /ˈfɛbeɪˌɛɹi/ (unverified). Not as default: a slow, sleepy or breathy delivery; cruelty; an accent caricature.

## [SW] Motivation
In her lore, Bae is Chaos itself, a chairperson who would rather break the rules and watch what happens. As a streamer and singer she wants to keep leveling up every stage, to make each performance crazier than the last, and to keep her chat laughing; she is preparing her first solo concert, "REGALIA."

## [SW] Relationships
IRyS: her BaeRyS partner, in a running "married and divorced" bit since a 2021 Minecraft bento; covers, off-collabs and "LUVATORRRRRY!" at Serendipity; Bae calls IRyS "the very first senpai I had ever met." Mori Calliope and IRyS: her CHADCast cohosts; "BLUE CLAPPER" with them and Koseki Bijou (2024); "R x R x R" with Calli (2025); she calls Calli "Cori Malliope." Ouro Kronii: Promise genmate she calls a "tsundere granny"; Sandwich Review, Digimon Survive, Fortnite. Ceres Fauna (graduated): genmate and horror partner ("Month of Horrors," 2022); Bae called her "a natural mama." Nanashi Mumei (graduated): genmate she called "the cutest voice"; BAE-CADEMY, off-collabs, Overwatch 2. Tsukumo Sana: a graduated Council genmate. Koseki Bijou: "BaeBi," a 2024 sleepover marathon, We Were Here; Bae made a Bijou Mii (2026). Cecilia Immergreen: "BratTea," a coffee-versus-tea debate; a 2026 fes talk and a Resident Evil series together. Gigi Murin: "Countach" with Kureiji Ollie (2025); a Midsummer Night's Dream reading. Elizabeth Rose Bloodflame and Kobo Kanaeru: "HELP!!" at Serendipity. Raora Panthera: Mario Party on Bae's 24-hour stream. FUWAMOCO: a 2025 spring collab with Gigi; they danced to "SNAKE EYES." Takanashi Kiara: her first collab outside Council (2021). Ninomae Ina'nis: a K/DA cover and an art lesson. Watson Amelia: bathroom reviews and Apex. Gawr Gura: an Urban Dictionary collab. Ookami Mio and Ollie: her joking "moms." Natsuiro Matsuri: "Kakumei Dualism" at the 2026 fes.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hakos Baelz; Tsukumo Sana is not
  made): official profile (HB1), wiki (HB2, by section), archive metadata (HB3, HB8), official Serendipity
  interview (HB4), official concert reports (HB5, HB6), the official REGALIA site (HB7), and Claude's two-model
  audio check (HB20, research/audio-check/bae.md).

## Open Questions
1. Her 2026 fes stages (the final solo "Idol" and "Kakumei Dualism" with Natsuiro Matsuri) rest on her own
   after-talk (ASR); the official fes report was not found. Keep them as her account?


## Card 2: Hakos Baelz Pairs (world; draft, full file)

---
kind: world
name: "Hakos Baelz Pairs"
sw_section: Worldbuilding
---

# World Element: Hakos Baelz Pairs (with the cast)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-02. Evidence labels as in the other world files. "Archive" = stream titles on the
> members' channels (archive.ragtag.moe, S1); a title shows that a collab happened, not how close the members
> are. Bae is active at the 2026-09-30 baseline. Fauna (graduated 2025-01-03), Mumei (2025-04-27, 04-28 JST),
> Gura (2025-05-01) and Sana (2022) appear only as memories; Ame is an affiliate. Group-wide Promise ties are on
> "hololive -Promise-"; IRyS's side of BaeRyS is also on IRyS's own file.

## One-line Concept
Chaos with everyone: Bae's bits and stages with the whole cast, from the BaeRyS "marriage" and the CHADCast trio
to the BaeBi sleepover, the coffee-versus-tea "BratTea" debate and her concert duets with kouhai.

## Type
Relationship web (one member with the cast).

## BaeRyS (with IRyS)
- **The bit:** a running "married" and "divorced" routine that began with a 2021 Minecraft bento; they
  "divorce" and "remarry" depending on the mood. [Observed S2 §Relationships, secondary; IRyS file]
- **Together:** a "Gisneyland" off-collab and the "Daikirai na Hazu Datta" cover (2023); a Valentine bento cooked
  on handcam (2024-02-14); HoloEarth with Kureiji Ollie (2024); a New Year's countdown off-collab watch-along
  (2024-12-31); Snow Bros. 2 (2025-04-17); Mario Party with Raora on Bae's 24-hour stream (2024-11-25). [S1]
- **On stage:** "High Tide" with Moona Hoshinova and Hoshimachi Suisei at -Breaking Dimensions- (2024); the
  official unit BaeRyS at Serendipity (2026), "LUVATORRRRRY!", their first duo stage. [Official S3]
- **In their words (2026 interview):** Bae: "I was blown away by her voice. I was so in awe of her I was a
  little intimidated"; "I really admire her easy-going nature and natural humor." IRyS: Bae "always comes up with
  ideas I wouldn't think of." [Official S4]

## CHADCast (with Mori Calliope and IRyS)
- "Chaos, Hope And Death": a podcast trio from 2022 (episodes through at least #14, 2023), with the 2026 song
  "Here Comes the CHADCast." With Koseki Bijou they sang "BLUE CLAPPER" at -Breaking Dimensions- (2024). [S1]
  [Official S3; Calli file C13]
- Calli and Bae: the "R x R x R" duo at -All for One- (2025); a GriMoire concert watch-along (2025-02-27); early
  collabs (2021). Bae calls her "Cori Malliope"; fans note they share a Live2D rigger, which is why Bae calls
  her "sister" (secondary). [Official S3] [S1] [Calli file]

## Council and Promise
- **Kronii:** "too talented, savage, and a 'tsundere granny'" (Bae on Kronii); Sandwich Review (2022), Digimon
  Survive ("takronii and agubae," 2022), Fortnite (2024), UNO on the 24-hour stream (2024); guests together at
  World Tour '25 in Sydney. In fan-recorded lore, Kronii created leap years to hold Bae's 29 February
  birthday. [S1] [Kronii file] [S2 §Lore, secondary]
- **Fauna (graduated):** "a natural mama, a soothing beauty, and someone who gives the best headpats" (Bae at
  debut); "BAE & FAUNA'S MONTH OF HORRORS" (October 2022); Lethal Company "sweaty gang" with Kaela Kovalskia and
  Bijou (2024). [S1] [Fauna file]
- **Mumei (graduated):** "the cutest voice" in Council (Bae at debut); "preYdator" and, with Fauna, "MUFAUBAE"
  (secondary); a BAE-CADEMY anatomy lesson, WarioWare and ASMR off-collabs (2024); Overwatch 2 on Mumei's
  channel (2025-04-20); Mumei's farewell-week collab with IRyS and Kronii (2025). [S1] [Mumei file]
- **Tsukumo Sana:** a Council genmate who graduated in 2022; a memory only. [S2]
- **Promise:** "Our Promise" at -Breaking Dimensions- (2024), the musical "The Broken Promise" (2024-12-14),
  Promise collabs (2025). [Official S3] [S1]

## With Advent
- **Koseki Bijou ("BaeBi"):** We Were Here Expeditions ("baebis," 2023), a JoJo watch-along (2024), the
  "#BAEBISleepover" (2024-08-11/12), UNO on the 24-hour stream; "BLUE CLAPPER" on stage (2024); Bae built a
  Bijou Mii in Tomodachi Life (2026-04-27). [S1] [Official S3] [Bae file HB20]
- **FUWAMOCO:** Gigi's "Spring Party" collab with FUWAMOCO and Bae (2025-03-31); a 2026 short of them dancing to
  "bae-senpai's new song SNAKE EYES." [S1]
- **Shiori Novella, Nerissa Ravencroft:** no direct collab documented in the sources read.

## With Justice
- **Cecilia Immergreen ("BratTea"):** a coffee-versus-tea debate, continued at a venue talk they did together at
  the 2026 fes; a Resident Evil series on Cecilia's channel (2026). Bae jokes that Cecilia only calls her "senpai"
  when she wants her to do something. [Bae file HB20] [Cecilia file, secondary]
- **Gigi Murin:** "Countach" with Kureiji Ollie at -All for One- (2025); a "BAE THEATRE" dramatic reading of A
  Midsummer Night's Dream (2025-02-05); UNO on the 24-hour stream. [Official S3] [S1]
- **Elizabeth Rose Bloodflame:** "HELP!!" with Kobo Kanaeru at Serendipity (2026). [Official S3]
- **Raora Panthera:** Super Mario Party Jamboree with IRyS on Bae's 24-hour stream (2024-11-25); ENReco guildmates
  ("Amber Coin," with Kiara and Mumei; secondary). [S1] [S2]

## With Myth
- **Takanashi Kiara:** Bae's first collab outside her generation, Keep Talking and Nobody Explodes (2021-09-24);
  World Tour '24 performers together. [S1] [Official S5]
- **Ninomae Ina'nis:** the K/DA "POP/STARS" cover with Moona and Ayunda Risu (2023); a BAE-CADEMY art lesson with
  "Ina-sensei" (2024); Ina's AmiAmi special featuring Bae (2025-05-29); World Tour '24. [S1] [Official S5]
- **Watson Amelia (affiliate):** bathroom reviews ("#BaethingAme," 2022), a VRChat Holoween escape-room
  behind-the-scenes (2022), an Apex off-collab (2023). [S1]
- **Gawr Gura (graduated):** an Urban Dictionary Challenge with Kronii, Mumei and Gura (2022). [S1]

## Beyond EN
- Kobo Kanaeru ("HELP!!"), Kureiji Ollie ("Countach," HoloEarth; Bae's joking "other mom"), Ookami Mio (her
  joking "mom"), Natsuiro Matsuri ("Kakumei Dualism" at the 2026 fes), Moona Hoshinova and Hoshimachi Suisei
  ("High Tide"), Usada Pekora and Ayunda Risu ("holorodents," secondary), Kaela Kovalskia (Lethal Company).
  [Official S3] [S2, secondary] [Bae file HB20]

## History
| Date | Event | Pair |
|---|---|---|
| 2021-09-24 | Keep Talking and Nobody Explodes | Bae–Kiara |
| 2022 | CHADCast begins; "Month of Horrors" (October) | Bae–Calli–IRyS; Bae–Fauna |
| 2023 | "Gisneyland," "Daikirai na Hazu Datta"; K/DA "POP/STARS"; We Were Here | BaeRyS; Bae–Ina; BaeBi |
| 2023-10-09 JST | -Promise- formed | Bae with IRyS, Fauna, Kronii, Mumei |
| 2024-08-11/12 | #BAEBISleepover | BaeBi |
| 2024-08-24/25 | -Breaking Dimensions-: "Our Promise," "BLUE CLAPPER," "High Tide" | Promise; CHADCast + Bijou; BaeRyS |
| 2024-11-25 | #BaeTV24 24-hour stream | with IRyS, Raora, Kronii, Bijou, Gigi |
| 2025-08-23/24 | -All for One-: "R x R x R," "Countach" | Bae–Calli; Bae–Gigi (with Ollie) |
| 2026-03 | 7th fes: venue talk; Resident Evil series (April) | Bae–Cecilia |
| 2026-07-03/04 PDT | Serendipity: BaeRyS "LUVATORRRRRY!"; "HELP!!" | BaeRyS; Bae–Elizabeth (with Kobo) |

## Sensory Palette
- See: red pigtails and a mouse on her head beside IRyS's angel and devil colors; three podcast mics for CHADCast.
- Hear: Bae's fast, loud chatter against IRyS's giggles or Kronii's deadpan; "boom, boom, boom" over a stream of
  gifts.

## Glossary
| Term | Meaning | Who uses it |
|---|---|---|
| BaeRyS | Bae and IRyS; an official Serendipity unit name | everyone |
| CHADCast | Chaos, Hope And Death: Bae, IRyS, Calli | the trio, fans |
| BaeBi | Bae and Bijou | fans, titles |
| BratTea | Bae and Cecilia (coffee versus tea) | fans |
| Brats / Rat Pack | Bae's fans / members | Bae |

## Conflicts and Story Hooks
1. A BaeRyS "divorce" hearing with Calli as the CHADCast judge.
2. Bae and Cecilia settle coffee versus tea with a blind taste test that Kronii referees.
3. A BaeBi sleepover where nobody sleeps and Bae narrates the chaos like breaking news.
4. Bae choreographs a duet for a kouhai and insists the breakdance goes in the last 16 counts.

## Links to Characters
Hakos Baelz; IRyS, Mori Calliope, Ouro Kronii, Ceres Fauna, Nanashi Mumei, Koseki Bijou, Cecilia Immergreen, Gigi
Murin, Elizabeth Rose Bloodflame, Raora Panthera, FUWAMOCO, Takanashi Kiara, Ninomae Ina'nis, Watson Amelia, Gawr
Gura.

## Secrets
None assigned.

## Hard Facts (continuity)
- Official stage units: BaeRyS (IRyS & Bae, Serendipity 2026); CHADCast is a podcast trio (Calli, IRyS, Bae).
- Concert pairings: "BLUE CLAPPER" (Calli, IRyS, Bae, Bijou; 2024); "High Tide" (IRyS, Bae, Moona, Suisei; 2024);
  "R x R x R" (Calli & Bae; 2025); "Countach" (Bae, Gigi, Ollie; 2025); "HELP!!" (Kobo, Bae, Elizabeth; 2026).

## Sources (checked 2026-10-02)
- S1 Stream archive metadata (archive.ragtag.moe), Bae's and other members' channels; the IDs are listed in Bae's
  file (HB3, HB8).
- S2 Hakos Baelz wiki page, §Relationships and §Lore (secondary): https://virtualyoutuber.fandom.com/wiki/Hakos_Baelz
- S3 Official concert reports: https://hololive.hololivepro.com/en/events/breaking-dimensions/,
  https://hololive.hololivepro.com/en/events/all-for-one/, https://hololive.hololivepro.com/en/events/serendipity/
- S4 Official Serendipity interview, IRyS and Bae (2026-06-05): https://serendipity.hololivepro.com/news/interview02
- S5 Official post-event report, World Tour '24: https://hololive.hololivepro.com/en/news/20250217-01-128/
- Character files in this project: Hakos Baelz (HB20 audio check), IRyS, Calli (C13), Kronii, Fauna, Mumei,
  Cecilia.

---

## [SW] Name
Hakos Baelz Pairs

## [SW] Role
Relationship

## [SW] Other Names
Bae and IRyS, BaeRyS, CHADCast, BaeBi, BratTea, Bae and Kronii, Bae and Calli, Bae and Cecilia

## [SW] Description
Hakos Baelz's ties with the cast. With IRyS she is BaeRyS: a running "married and divorced" bit since a 2021 Minecraft bento, covers and off-collabs, "High Tide" on stage in 2024 and their first duo stage, "LUVATORRRRRY!", at Serendipity 2026; Bae says she was "blown away" by IRyS's voice, and IRyS says Bae "always comes up with ideas I wouldn't think of." With IRyS and Mori Calliope she is CHADCast (Chaos, Hope And Death), a podcast trio since 2022 that sang "BLUE CLAPPER" with Koseki Bijou in 2024; Bae and Calli sang "R x R x R" in 2025. In Promise she calls Ouro Kronii a "tsundere granny"; with the graduated Fauna she ran a 2022 "Month of Horrors," and she called the graduated Mumei "the cutest voice." With Bijou she is "BaeBi" (a 2024 sleepover marathon); with Cecilia Immergreen, "BratTea," an endless coffee-versus-tea debate and a 2026 Resident Evil series; she sang "Countach" with Gigi Murin and Kureiji Ollie (2025) and "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame (2026), and FUWAMOCO danced to her "SNAKE EYES." Her first collab outside her generation was with Takanashi Kiara (2021).

## [SW] Rules
These are friendships and performed bits; the BaeRyS "marriage" is a comedy routine, not a romance. Fauna, Mumei, Gura and Sana appear only as memories after their graduations; Ame is an affiliate. Collab titles show that a collab happened, not how close two members are.

## [SW] Sensory Details
Red pigtails and a little mouse on her head beside IRyS's angel and devil colors; three podcast mics for CHADCast. Bae's fast, loud chatter against IRyS's giggles or Kronii's deadpan; "boom, boom, boom" over a stream of gifts.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hakos Baelz): archive metadata,
  official concert reports and interview, the wiki (secondary), and the cast files.

## Open Questions
1. Shiori and Nerissa have no documented direct collab with Bae in the sources read; leave them out?


## Bae lines added to other cards (2026-10-02; full files in `projects/holoen/bible/`, some edits not yet promoted)

### Mori-Calliope (`bible/characters/Mori-Calliope.md`)
[SW] Relationships (Bae sentences): IRyS and Hakos Baelz: her CHADCast cohosts ("Chaos, Hope, and Death"; "BLUE CLAPPER" with Bijou, 2024); Bae calls her "Cori Malliope" and sang "R x R x R" with her (2025), and IRyS joined her as the "Two Pink Women" of Silent Hill 2.
| 2022 | CHADCast begins with IRyS and Hakos Baelz. | [Observed C12] |
| IRyS, Hakos Baelz | CHADCast cohosts | A chaotic podcast trio. Bae calls her "Cori Malliope." "BLUE CLAPPER" with Bijou at -Breaking Dimensions- (2024); the "R x R x R" duo with Bae at -All for One- (2025); Bae's GriMoire watch-along (2025) | [Observed C12; C4 nickname list, secondary] |

### Takanashi-Kiara (`bible/characters/Takanashi-Kiara.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: Kiara was Bae's first collab partner outside Council (Keep Talking and Nobody Explodes, 2021).

| Hakos Baelz | Promise kouhai | Bae's first collab outside her generation, Keep Talking and Nobody Explodes (2021-09-24); World Tour '24 performers together; ENReco guildmates ("Amber Coin," secondary) | [Bae file HB3, HB5, HB8, HB20] |

### Ninomae-Inanis (`bible/characters/Ninomae-Inanis.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: a K/DA "POP/STARS" cover with Moona Hoshinova and Ayunda Risu (2023), an art lesson on Bae's stream and Ina's AmiAmi special with Bae (2025).

| Hakos Baelz | Promise kouhai | The K/DA "POP/STARS" cover with Moona and Ayunda Risu (2023); a BAE-CADEMY art lesson with "Ina-sensei" (2024); Ina's AmiAmi special featuring Bae (2025-05-29); World Tour '24 together | [Bae file HB3, HB5, HB8, HB20] |

### Gawr-Gura (`bible/characters/Gawr-Gura.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: an Urban Dictionary Challenge with Kronii and Mumei on Bae's stream (2022).

| Hakos Baelz | Council kouhai | An Urban Dictionary Challenge with Kronii and Mumei (2022-08-20, Bae's stream) | [Bae file HB3, HB5, HB8, HB20] |

### Watson-Amelia (`bible/characters/Watson-Amelia.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: bathroom reviews and a Holoween escape-room behind-the-scenes (2022), and an Apex off-collab (2023).

| Hakos Baelz | Council kouhai | Bathroom reviews ("#BaethingAme," 2022), a VRChat Holoween escape-room behind-the-scenes (2022), an Apex off-collab ("2 players. 1 champion.," 2023) | [Bae file HB3, HB5, HB8, HB20] |

### IRyS (`bible/characters/IRyS.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou.

| 2021-09-29 | The Minecraft "bento" that starts the BaeRyS married/divorced bit | [Observed R2 §Relationships] |
| 2023-10-09 | Joins hololive English -Promise- with Fauna, Kronii, Mumei and Bae | [Observed R2 §2023] |
| Hakos Baelz | Promise genmate ("BaeRyS") | The married/divorced running bit; Bae once banned her from soda for a week after a lost bet; "Gisneyland" and the "Daikirai na Hazu Datta" cover (2023); "High Tide" with Moona Hoshinova and Hoshimachi Suisei (2024); BaeRyS at Serendipity (2026) | [Observed R2 §Relationships, §Likes and dislikes] |
| Mori Calliope | First collab partner (2021) | "MorIRyS"; CHADCast podcast trio with Bae | [Observed R2 §2021, units] |

### Ouro-Kronii (`bible/characters/Ouro-Kronii.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: genmate who calls her a "tsundere granny"; Sandwich Review, Digimon Survive and Fortnite together; in fan lore Kronii created leap years to hold Bae's birthday. Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity.

| 2023-10-09 | Joins hololive English -Promise- alongside IRyS, Ceres Fauna, Nanashi Mumei and Hakos Baelz | [Official K3] |
| 2025 | Fauna (January) and Mumei (April) graduate; Promise's current members are Kronii, IRyS and Baelz | Shared history stays [Official K34] |
| Hakos Baelz | Council/Promise genmate | Bae called her "too talented, savage, and a 'tsundere granny'"; Sandwich Review (2022), Digimon Survive ("takronii and agubae," 2022), Fortnite (2024), UNO on Bae's 24-hour stream (2024); in fan-recorded lore Kronii created leap years to hold Bae's birthday. [Unverified, title only: Bae suddenly holding her hand; Kronii and IRyS scaring Bae together] | [Observed K8 §Personality, secondary; K27, K16 clip titles] |
| Nanashi Mumei (graduated) | Council genmate ("KronMei") | [Unverified, title only: the "Flower" bit with Mumei and Baelz; Mumei accidentally blowing up the Bunkeronii's entrance] | [Observed K14 clip, K8 §Quotes and §Relationships, secondary; K28 clip titles] |

### Ceres-Fauna (`bible/characters/Ceres-Fauna.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Koseki Bijou: "Coach Fauna" in Bijou's Hitman runs and a "Sweaty TryHard Gamers" squad with Bae and Kaela.
| Hakos Baelz | Genmate (6 / 12 / 7 / 2) | At debut Bae called her "a natural mama, a soothing beauty, and someone who gives the best headpats"; a month of horror games (2022); an Amnesia: The Bunker off-collab (2023) | [Observed F2; F3, F4] |

### Nanashi-Mumei (`bible/characters/Nanashi-Mumei.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: genmate and a recurring collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). IRyS: Promise unitmate from 2023; they played Overwatch together in Mumei's farewell week, then a Promise R.E.P.O. collab with IRyS, Kronii and Bae (2025-04-24).
| 2024-08-05 | 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori | [Observed M3 title, description] |
| 2025-04 | A farewell month of collabs across hololive: Overwatch with IRyS (04-22), a cover of "とんとんまーえ！" with Inugami Korone (04-23), Promise R.E.P.O. with IRyS, Kronii and Bae (04-24); last chatting stream with calls (04-26); 3D graduation stream (04-27, 04-28 JST) | [Observed M2; M3 titles] |
| Hakos Baelz | Genmate (4 / 31 / 27 / 5 / 3; a metadata count, not a ranking) | A recurring collab partner: Mad-Lib theatre (2021), an off-collab "I Found A Rat In My House!!!" (2024), "bae wants to play!!!" (Overwatch 2, 2025) | [Observed M3] |
| IRyS | Promise unitmate from 2023 (CouncilRyS before that) | They played Overwatch together in Mumei's farewell week ("【OVERWATCH 2】 the final stream !!! with @IRyS," 2025-04-22); a Promise R.E.P.O. collab with IRyS, Kronii and Bae two days later; a guest at "Outside the Box" | [Observed M3] |

### Koseki-Bijou (`bible/characters/Koseki-Bijou.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: "BaeBi" (We Were Here, a 2024 sleepover marathon); with Bae, Calli and IRyS she sang "BLUE CLAPPER" at the 2024 English concert.
| 2024-08-11 | #BAEBISleepOver with Hakos Baelz | [Observed KB3] |
| Hakos Baelz | Senior ("BaeBi") | We Were Here (2023); a JoJo watch-along (2024); #BAEBISleepOver (2024-08-11/12); UNO on Bae's #BaeTV24 stream (2024-11-25); "BLUE CLAPPER" with Bae, Calli and IRyS at -Breaking Dimensions- (2024); Bae built a Bijou Mii in Tomodachi Life (2026) | [Observed KB3; Bae archive] [Bae file HB3, HB5, HB8, HB20] |

### Fuwawa-Abyssgard (`bible/characters/Fuwawa-Abyssgard.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: a 2025 spring collab with Gigi; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES" (2026).

| Hakos Baelz | Promise senior | Gigi's "Spring Party" collab with FUWAMOCO and Bae (2025-03-31); a FUWAMOCO short dancing to "bae-senpai's new song SNAKE EYES" (2026-03-20) | [Bae file HB3, HB5, HB8, HB20] |

### Mococo-Abyssgard (`bible/characters/Mococo-Abyssgard.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: a 2025 spring collab with Gigi; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES" (2026).

| Hakos Baelz | Promise senior | Gigi's "Spring Party" collab with FUWAMOCO and Bae (2025-03-31); a FUWAMOCO short dancing to "bae-senpai's new song SNAKE EYES" (2026-03-20) | [Bae file HB3, HB5, HB8, HB20] |

### Cecilia-Immergreen (`bible/characters/Cecilia-Immergreen.md`)
[SW] Relationships (Bae sentences): Hakos Baelz ("BratTea"): an endless coffee-versus-tea debate, a venue talk together at the 2026 fes and a Resident Evil series on Cecilia's channel; Bae jokes that Cecilia only calls her "senpai" when she wants something.

| Gawr Gura, IRyS, Hakos Baelz | Seniors | Keep Talking and Nobody Explodes and The Forest with Gura (2025); Elden Ring Nightreign with IRyS and Bijou (2025); "BratTea" with Bae: a running coffee-versus-tea debate, a venue talk together at the 2026 fes, and a 2026 Resident Evil series on Cecilia's channel (Bae's own streams, ASR) | [Observed CI2, CI3] |

### Gigi-Murin (`bible/characters/Gigi-Murin.md`)
[SW] Relationships (Bae sentences): Hakos Baelz: "Countach" with Kureiji Ollie (ID) on stage (2025), a dramatic reading of A Midsummer Night's Dream on Bae's stream, and a 2025 spring collab with FUWAMOCO.
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa | [Official GG5] |
| Hakos Baelz, Kureiji Ollie (ID) | Senior; cross-branch | "Countach" at -All for One- (2025); with Bae, a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025-02-05), UNO on Bae's 24-hour stream (2024-11-25) and Gigi's Spring Party collab with FUWAMOCO (2025-03-31) | [Official GG5] [Bae file HB3, HB5, HB8, HB20] |

### Raora-Panthera (`bible/characters/Raora-Panthera.md`)
[SW] Relationships (Bae sentences): Hakos Baelz and IRyS: Super Mario Party on Bae's 24-hour stream (2024).

| Hakos Baelz, IRyS | Promise seniors | Super Mario Party Jamboree on Bae's 24-hour #BaeTV24 stream (2024-11-25); ENReco guildmates with Bae ("Amber Coin," secondary) | [Bae file HB3, HB5, HB8, HB20] |

### Elizabeth-Rose-Bloodflame (`bible/characters/Elizabeth-Rose-Bloodflame.md`)
[SW] Relationships (Bae sentences): Kobo Kanaeru and Hakos Baelz: "HELP!!" at Serendipity.
| 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |
| Kobo Kanaeru, Ayunda Risu | ID seniors | "HELP!!" with Kobo and Hakos Baelz at Serendipity (2026); Kobo calls her "Lilis" (secondary); LYRA and "ALiCE&u" with Risu | [Observed EB2] [Official EB5, EB8] |

### hololive--Promise (`bible/world/hololive--Promise.md`)
[SW] Description (Bae sentences): hololive -Promise-: IRyS, Ouro Kronii and Hakos Baelz at the 2026 baseline. IRyS ("Hope") and the four remaining Council members were billed together as "CouncilRyS" and formed Promise on 2023-10-08 PDT / 10-09 JST; Fauna (Nature, the soft kirin protective of Mumei) and Mumei (Civilization, the forgetful owl and a recurring collaborator with Bae) graduated in 2025. All five sang their unit song "Our Promise" at the 2024 English concert and staged the musical "The Broken Promise" (2024-12-14). Bae calls Kronii "too talented, savage, and a tsundere granny"; Fauna once described Kronii's "gap moe," the cute side that shows when she's flustered; IRyS has wondered aloud how Kronii sounds when she's scared. IRyS and Bae keep the "BaeRyS" bit of being "married" and "divorced," which turned "Monopoly" into a fandom euphemism, and they are also creative partners: paired for the 2026 Serendipity concert, IRyS leans on Bae's "strong vision" when she's indecisive, Bae admires IRyS's humor that makes everyone comfortable, and they call their dynamic "a can of worms" and "Complicated."

| 2021-08 | -Council- debuts (Sana, Fauna, Kronii, Mumei, Bae) | "Council" nostalgia |

### Concerts-and-Live-Events (`bible/world/Concerts-and-Live-Events.md`)
[SW] Description (Bae sentences): Los Angeles, July 3–4, built on units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia), with guests Ookami Mio, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame singing alongside EN members); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet.
| IRyS | Promise musical "The Broken Promise" (2024-12-14); 3D lives "The Devil Wears Hope" (2024-11-17), "HOPE UPON A STAR" (2025-03-16), "Racing Towards Hope" (2026-03, race-queen outfit); World Tour '25 lead; Serendipity with Hakos Baelz; first solo concert "HOPE ||: Beyond the Stars," Tokyo, 2026-10-06 | IRyS file R2, R3; S1 |
| Hakos Baelz | -Breaking Dimensions- (2024): "Our Promise," "BLUE CLAPPER" with Calli, IRyS and Bijou, solo "GEKIRIN," "High Tide"; -All for One- (2025): "R x R x R" with Calli, "Countach" with Gigi and Ollie, solo "La Roja (Arrange ver.)"; birthday 3D lives "-KAGURA- Dance of the Gods" (2025) and "ReCOLOR" (2026); final solo act at the 2026 fes ("Idol," her own choreography; her account); Serendipity: BaeRyS with IRyS, "HELP!!" with Kobo and Elizabeth; first solo concert "REGALIA" announced for 2026-12-01 (after the baseline) | S8, S9, S11; Bae file HB2, HB7, HB20 |

### Cross-Branch-Friends (`bible/world/Cross-Branch-Friends.md`)
[SW] Description (Bae sentences): Hakos Baelz calls Ookami Mio her "mom" and Kureiji Ollie "another mom," and sang "HELP!!" with Kobo Kanaeru and "Kakumei Dualism" with Natsuiro Matsuri.

- **Hakos Baelz:** calls Ookami Mio her "mom" and Kureiji Ollie "another mom" (secondary); with Ollie she


## Audio report: research/audio-check/bae.md

# Audio check — Hakos Baelz (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026. Only in-scope public performance material is used: long stretches of the April
chatting stream are about personal matters and are not quoted or summarized here. The Tomodachi Life window
mixes in game text-to-speech voices, which lifts its pitch figures; it is not used for voice measurements.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| open2026chat | [≪JUST CHATTING≫ lil yaps + thanking supas with s](https://youtu.be/DOZ8rRVH03c) | [0:00:00–0:15:00](https://youtu.be/DOZ8rRVH03c?t=0) | 8.2 | 738 | 89.6 | 200 Hz | 147–333 Hz |
| chat30_2026 | [≪JUST CHATTING≫ lil yaps + thanking supas with s](https://youtu.be/DOZ8rRVH03c) | [0:30:00–1:00:00](https://youtu.be/DOZ8rRVH03c?t=1800) | 20.5 | 2727 | 133.3 | 212 Hz | 152–345 Hz |
| close2026chat | [≪JUST CHATTING≫ lil yaps + thanking supas with s](https://youtu.be/DOZ8rRVH03c) | [2:09:10–2:21:10](https://youtu.be/DOZ8rRVH03c?t=7750) | 7.4 | 912 | 123.1 | 233 Hz | 158–379 Hz |
| festalk30_2026 | [≪FES AFTER-TALK≫ hi :)](https://youtu.be/sPXphrWUOQU) | [0:20:00–0:50:00](https://youtu.be/sPXphrWUOQU?t=1200) | 22.8 | 2736 | 120.1 | 215 Hz | 157–358 Hz |
| game30_2026 | [≪Tomodachi Life: Living the Dream≫ ONE MORE RESI](https://youtu.be/2pn5_pZu8Q4) | [0:40:00–1:10:00](https://youtu.be/2pn5_pZu8Q4?t=2400) | 20.6 | 723 | 35.0 | 278 Hz | 125–505 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Self-introduction "Wazzup! I am Chaos the end of ends, a steel rose trapped in a cage of ice…" (HB2) | **Present but garbled** in the first model at the April 2026 opening; kept from the wiki, not quoted from audio. | [0:04:46](https://youtu.be/DOZ8rRVH03c?t=286) |
| Thanks every gift ("boom, boom, boom") | **Confirmed**: about 38 "boom boom" and 128 "thank you so much" in about an hour of chat (first-model counts). | [0:32:29](https://youtu.be/DOZ8rRVH03c?t=1949) |
| "You're doing great!" (HB2) | **Confirmed** as encouragement to a viewer. | [0:58:39](https://youtu.be/DOZ8rRVH03c?t=3519) |
| "Febaerary" every year | **Confirmed**: "This year was my fifth…" (the coined word is misheard by both models). | [0:33:20](https://youtu.be/DOZ8rRVH03c?t=2000) |
| Swearing | **Moderate and casual**: "damn," "God damn it," "hell yeah," a joking "bitch" at a fictional rival; "bruh" and "frickin'." | [2:11:57](https://youtu.be/DOZ8rRVH03c?t=7917) |
| Speech rate | About 120–133 words a minute of speech in chat; fast, run-on storytelling. | — |
| 2026 fes stages (her own account) | **Her account**: the final solo act ("Idol," her own choreography ending in a breakdance) and "Kakumei Dualism" with Natsuiro Matsuri (she took the T.M.Revolution part, "Bae Aniki"); a venue talk with Cecilia where they "continued the coffee and tea debate." | [0:31:24](https://youtu.be/sPXphrWUOQU?t=1884), [0:36:03](https://youtu.be/sPXphrWUOQU?t=2163), [0:24:27](https://youtu.be/sPXphrWUOQU?t=1467) |
| Collab with Cecilia (2026) | **Confirmed**: Resident Evil "nine" continued on Cecilia's channel. | [2:19:23](https://youtu.be/DOZ8rRVH03c?t=8363) |
| The "Hakos Bells" bit | **Confirmed**: a mock feud with the "artist" whose claim hit her stream after her own new song. | [2:12:26](https://youtu.be/DOZ8rRVH03c?t=7946) |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. Cards may quote only the shared spans. Speaker attribution
rests on the stream itself (a solo stream on her own channel; viewers' superchats she reads aloud are not
attributed to her and are not quoted).

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "It was sabotage" | [0:06:53](https://youtu.be/DOZ8rRVH03c?t=413) | "One of these days the alarm will work. It was sabotage. Sabotage. Anyway, I know what you're talking about. Nothing happened this morning. What? Falsely accused. I was only trying to" | **Shared span (computed):** whole line |
| "They hate me. They hate me" | [0:07:56](https://youtu.be/DOZ8rRVH03c?t=476) | "How did you manage to get a low school than be sabotage I hate me" | **Disagrees**; not used |
| "They hate promise. They hate us. It's a conspiracy" | [0:08:27](https://youtu.be/DOZ8rRVH03c?t=507) | "All the promise have the exact same. They hate promise. They hate us. It's a conspiracy. Welcome to the stream, by the way, um, I have some food and some coffee and we're just gonna chill. We're gonna chat. And then, I have a couple of, um..." | **Shared span (computed):** whole line |
| "I may be dead" | [0:30:45](https://youtu.be/DOZ8rRVH03c?t=1845) | "Does that mean the next time you stream is the weekend? I don't know if I'm streaming on the weekend. I maybe did. I maybe did. I think the next time I'm streaming will be on Friday, cause CC and I are going to be continuing Resident Evil 9 Friday evening." | **Disagrees** ("I maybe did"); not used |
| "Five years! Has it been five years? Oh my god it is." | [0:33:20](https://youtu.be/DOZ8rRVH03c?t=2000) | "Thank you so much. Five years! Has it been five years? Oh my god, it is. This year was my fifth for Bairi." | **Shared span (computed):** whole line |
| "This year was my fifth for berry." | [0:33:25](https://youtu.be/DOZ8rRVH03c?t=2005) | "five years has it been five years oh my god it is oh this year was my fifth for berry that's crazy i've been watching you for half a" | **Shared span (computed):** whole line |
| "oh my gosh oh my gosh ew not ew at you just ew at the passage of time" | [0:33:43](https://youtu.be/DOZ8rRVH03c?t=2023) | "That's crazy Been watching you for half a decade. Oh my gosh. Oh My gosh You" | **Disagrees**; not used |
| "Welcome to the Rat Pack, welcome, welcome." | [0:42:50](https://youtu.be/DOZ8rRVH03c?t=2570) | "Welcome to the Rat Pack! Welcome, welcome. Oh, I should do a membership stream." | **Shared span (computed):** whole line |
| "everything gets better if you're at the bottom you can only go up you're doing great" | [0:58:39](https://youtu.be/DOZ8rRVH03c?t=3519) | "life and end up falling down this rabbit hole. Enjoying your singing, dancing and sometimes gaming skills. Hope everything goes your way. Thank you so much. Everything gets better. If you're at the bottom, you can only go up. You're doing great. Umm, Uvidredna thank you so much." | **Shared span (computed):** whole line |
| "Here I am trying to promote her new song. What does she do claim my video?" | [2:12:26](https://youtu.be/DOZ8rRVH03c?t=7946) | "she's jealous here i am trying to promote her new song and what does she do claim my video new beef bae vs hikki's bells yo that bae situation is crazy have you heard about the beef between bae and" | **Partial (computed):** shared runs "here i am trying to promote her new song" … "what does she do claim my video" |
| "Does she really think that me, of all people, is trying to clout chase by using her?" | [2:13:07](https://youtu.be/DOZ8rRVH03c?t=7987) | "a success i'm just trying to promote her new song does she really think that me of all people is trying to clout chase by using her breaking news bae is trying to clout chase by by by using hey kospels" | **Shared span (computed):** whole line |
| "Breaking news! Bae is trying to clout chase by using hackel spells." | [2:13:16](https://youtu.be/DOZ8rRVH03c?t=7996) | "Is trying to clout chase by using her Breaking news bae is trying to clout chase by by by using hey cos bill That's the new drama, oh my god, how mother thank you so much take off spells is just okay" | **Partial (computed):** shared runs "breaking news bae is trying to clout chase by" |
| "My next video is just exposing Heiko's spells" | [2:14:57](https://youtu.be/DOZ8rRVH03c?t=8097) | "Scandalous. My next video is just exposing Heiko's Bells." | **Partial (computed):** shared runs "my next video is just exposing heiko's" |
| "Please stream my newest song, Snake Eyes, and also my newest cover, Liar Dancer, if you haven't already." | [2:19:11](https://youtu.be/DOZ8rRVH03c?t=8351) | "And on y'all I'm gonna go take a nap Please stream my newest song snake eyes and also my newest cover light dancer if you haven't already I really like it. It's really really cute Thank you so much, I'll see you guys on Friday on CC's channel" | **Partial (computed):** shared runs "please stream my newest song snake eyes and also my newest cover" … "dancer if you haven't already" |
| "I'll see you guys on Friday on CC's channel. We're going to be continuing resident evil nine." | [2:19:23](https://youtu.be/DOZ8rRVH03c?t=8363) | "already. I really like it. It's really, really cute. Thank you so much. I'll see you guys on Friday on CC's channel. We're going to be continuing Resident Evil 9. Very fun. And then maybe next week. Before my break." | **Partial (computed):** shared runs "i'll see you guys on friday on cc's channel we're going to be continuing resident evil" |
| "Okey dokey, and I'm gonna go sweep as well. Bye-bye!" | [2:19:56](https://youtu.be/DOZ8rRVH03c?t=8396) | "Maybe not Koseki Bijou! Let's go say hi to Koseki Bijou. Okey-dokey Good night, everyone I'm gonna go to sleep as well Bye bye!" | **Partly agrees**: only "okey dokey" and "bye-bye" are shared (two-word runs); not quoted as a line |
| "What do we do? We had we continued the coffee and tea debate" | [0:24:27](https://youtu.be/sPXphrWUOQU?t=1467) | "stream it was like a live quote-unquote live stream with the people there what do we do we we had we continued the coffee and tea debate they're got attacked live by cc the venue exclusive event but" | **Partial (computed):** shared runs "what do we do we" … "had we continued the coffee and tea debate" |
| "So you see only cause me senpai when she wants me wants me to do something for her" | [0:26:03](https://youtu.be/sPXphrWUOQU?t=1563) | "Together she was like, are you sure? Thank you senpai CC only calls me senpai when she wants me wants me to do something for her Oh when she needs help And it works." | **Partial (computed):** shared runs "me senpai when she wants me wants me to do something for her" |
| "Technology be crazy." | [0:29:49](https://youtu.be/sPXphrWUOQU?t=1789) | "the new thing how was the truck it was crazy your technology crazy technology be crazy i don't know if you guys noticed watching the stream but with the box um it's it's it's two-sided you know so like in this frame su and i are facing one side and then miko and noida senpai facing the other side but in middle it's" | **Shared span (computed):** whole line |
| "They decided to put me as the final solo act this year. When I found out, guys, I was so stressed." | [0:31:24](https://youtu.be/sPXphrWUOQU?t=1884) | "and time skip forward what, like two hours? Because for some reason they decided to put me as the final solo act this year. When I found out guys, I was so stressed. I was so stressed. So it was, okay, we'll talk about that later. But first I had my unit song with Matsuri Senpai." | **Shared span (computed):** whole line |
| "yeah I was bey aniki hell yeah" | [0:36:03](https://youtu.be/sPXphrWUOQU?t=2163) | "Did you take the Team Revolution parts? Yeah! I was bae aniki, hell yeah. Man." | **Partial (computed):** shared runs "yeah i was" … "aniki hell yeah" |
| "Okay, I guess I'm doing this now confused rat" | [0:38:05](https://youtu.be/sPXphrWUOQU?t=2285) | "and then suddenly my call and response was decided for me and I was like oh okay I guess I'm doing this now Confused rat" | **Shared span (computed):** whole line |
| "I know, sue me, okay? I'm sorry. I still haven't watched Osinoko, I'm sorry." | [0:42:42](https://youtu.be/sPXphrWUOQU?t=2562) | "before me so thank you so much um i know sue me okay i'm sorry i still haven't watched oshinoko i'm sorry now i had so many things this has been in planning for ever since last fest which normally is what happens i do one fest" | **Partial (computed):** shared runs "i know sue me okay i'm sorry i still haven't watched" |
| "a lot of people have been making jokes that eventually I'm just gonna start breakdancing on stage" | [0:43:15](https://youtu.be/sPXphrWUOQU?t=2595) | "to level up somehow and i know ever since from debut a lot of people have been making jokes that eventually i'm just gonna start breakdancing on stage and i also was treating it as a joke and then it suddenly became not a joke i have started i started" | **Shared span (computed):** whole line |
| "And I also was treating it as a joke and then it suddenly became not a joke" | [0:43:22](https://youtu.be/sPXphrWUOQU?t=2602) | "A lot of people have been making jokes that eventually I'm just gonna start breakdancing on stage And I also was treating it as a joke and then it suddenly became not a joke I have started I started breakdancing lessons everyone. Oh my god" | **Shared span (computed):** whole line |
| "Why would you want the peak of that to be at the end of the performance? Who would think that's a good idea? Me" | [0:49:19](https://youtu.be/sPXphrWUOQU?t=2959) | "song when you're already tired and you're out of out of just out of power you're tired your muscles are dead everything's dead why would you want the peak of that to be at the end of the performance me who would think that's a good idea me these were the two quote unquote i think i will consider them problems because one I've never choreographed idle step before" | **Partial (computed):** shared runs "why would you want the peak of that to be at the end of the performance" … "who would think that's a good idea me" |
| "My name is Koseki Bijuu" | [0:50:30](https://youtu.be/2pn5_pZu8Q4?t=3030) | "Yay! KA-SEK-I-ME-JU! Whoa!" | **Disagrees** (game text-to-speech and a name being typed); not used |
| "Should've picked a big one. God dammit." | [1:01:40](https://youtu.be/2pn5_pZu8Q4?t=3700) | "I got a marble what was that should pick the big one god damn it all righty oh hello sorry what is going on See you soon." | **Disagrees** ("should pick the big one god damn it"); not used |


## Performance sheet: export/elevenlabs/Hakos-Baelz.md

# ElevenLabs v4 Performance Sheet: Hakos Baelz

> Built from `bible/characters/Hakos-Baelz.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Bae is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, Australian accent, bright, punchy mid-range voice; fast, loud and
run-on when telling a story; louder and higher for jokes, flat and deadpan for a dry 'bruh'; warm and sincere
when cheering someone on."
- Register basis: 2026 chat windows measured lower than most of her kouhai (window medians about 200–233 Hz;
  `research/audio-check/bae.md`). Keep the accent natural, never a caricature.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (she swings between loud storytelling, deadpan and warmth).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[energetic, fast]` or `[warm, sincere]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like," "yeah," "okay," "oh my god," "That's crazy"; "senpai" for seniors even in English.
- Thanking gifts: "thank you so much" plus "boom, boom, boom."
- Small failures blamed on sabotage: "It was sabotage." "It's a conspiracy."
- Answering her own questions: "Who would think that's a good idea? Me."
- A flat "bruh" for absurdity; warm "You're doing great" for someone who is struggling.
- Casual swearing ("damn," "God damn it," "hell yeah").

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
- "boom, boom, boom" (spoken, while thanking).
- `[laughs]`, `[gasps]` (tag only).

## 6. Pronunciation (provisional; test)
- Baelz `/bɛlz/` ("bells"; many members say `/beɪlz/`) · Hakos `/ˈheɪkɒs/` ("hake-oss") · Bae `/beɪ/` ·
  Febaerary `/ˈfɛbeɪˌɛɹi/` (unverified)

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
(Line 1 is a style demo built on her official greeting; line 4 is a wiki-listed word; the rest are her lines,
quoted only where both transcripts agree.)



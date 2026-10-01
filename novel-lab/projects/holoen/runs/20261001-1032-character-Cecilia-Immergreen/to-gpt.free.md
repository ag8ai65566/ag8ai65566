# One-round claim-check review (xhigh): hololive -Justice-, Cecilia Immergreen and Raora Panthera (two character files) with their audio reports

The other Justice cards and the world cards are reviewed in separate runs; mention cross-card issues you notice anyway.

# One-round claim-check review for GPT (template; Claude fills the {{…}} parts)

Why (author, 2026-10-01): raise the strength and accuracy of GPT's review. GPT runs at xhigh with live web
search, and the review is still one round, so it must be decisive and verifiable. The exported `## [SW]`
fields matter most, because they are what Sudowrite reads.

You are GPT, reviewing Claude's work for the novel-lab project "holoen", a Sudowrite Story Bible about
hololive members' public personas. This is the only review round. Write in English.

## Project rules that apply
- Authenticity first: accurate, sourced facts; profanity and teasing kept as-is; nothing invented and presented
  as fact. Unverified items must be labeled and kept off the cards.
- Persona premise: in stories, members know they are streamers with personas; lore (Justice as "law
  enforcers" chasing Advent's "criminals," the Scarlet Queen, the gremlin Chaser, the Ancient Automaton, the
  big-cat artist) is a performed bit; nobody has real powers.
- Relationships are the most important part of the world and include members outside EN (JP, ID, ReGLOSS,
  FLOW GLOW, HOLOSTARS); events (debuts, concerts, 3D lives) are shared memory; members' public X posts are
  key sources. The author asked to complete every character's relationship web.
- Recency weighting: recent (2025–2026) streams set the default manner; early memes stay as shared memory.
- Boundaries: public persona only; never the real people behind the avatars (names, faces, family, homes,
  health, surgeries, school, nationality claims, pets, trips, identity statements, the reasons for breaks or
  graduations). Author decision (2026-10-01): a member's announced break is not written (Elizabeth's
  September 2026 semi-break, Cecilia's 2026 summer break, Raora's 2025–26 break are all left out). Accents
  (British, American, German, Italian) are recorded only as voice features. No romance or intimacy between
  real people: "wife," "husband," fictional children and "mortal enemy" are performed bits. No explicit
  sexual content (Gigi's crude jokes stay jokes). COVER Derivative Works Guidelines; short quotes only, no
  lyrics.
- Voice: Sudowrite will insert ElevenLabs v4 audio tags itself, so each card teaches every voice factor in
  [SW] Dialogue Style, Catchphrases, Voice & Delivery and Audio Tags. Tags direct an ORIGINAL designed voice;
  nobody's real voice is cloned or imitated. IPA guides are kept, marked "provisional, untested."
- Quotation gate: lines quoted on cards from audio must be spans BOTH ASR models (whisper small.en and
  medium.en) agree on; each audio report lists the verdicts. Wiki-only spoken lines are "secondary"; short
  catchphrases may go on cards.
- Measurements describe mixed recordings and are not synthesis targets; they stay in the dossier, not in
  Audio Tags. Archive counts are never relationship rankings.
- Baseline date 2026-09-30. Sudowrite soft limits (words): Personality 400, Background 500, Physical 200,
  Dialogue Style 250, Catchphrases 250, Voice & Delivery 250, Audio Tags 350, Motivation 200, Relationships
  350; Worldbuilding Description 450, Rules 350, Sensory 200.
- Earlier rounds for other members flagged: ranking language ("closest," "most frequent"), subset collabs
  written as whole-group events, unlabeled time zones (3D dates are usually PDT), fan spellings treated as
  IPA, and health details in scope notes. Check for the same here.

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



==================== FILE: 20261001-1032-character-Cecilia-Immergreen/claude-draft.md ====================

---
kind: character
name: "Cecilia Immergreen"
sw_section: Characters
---

# Character File: Cecilia Immergreen

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Cecilia is active at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. Nothing about the performer behind the avatar: private-life information (breaks and their reasons,
> health, family, auditions and the like) is outside scope and is not recorded here; by the author's rule
> (2026-10-01) an announced break is not written. In stories she knows she is a streamer with a persona (see
> the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; CI20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (CI#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1.5 hours of archived 2026 recordings (CI20: the
> opening and middle of "Explaining the entire plot of NARUTO from very bad memory," the day after the CCGG
> 3D live, and two Zelda: A Link to the Past streams; see research/audio-check/cecilia.md). Parts of one
> window concern her family and are not used. The audio was machine-transcribed and acoustically measured;
> transcripts were reviewed in context, without independent listening verification.

## One-line Concept
"The Ancient Automaton," a clockwork maid from Immerheim built for eternal servitude who now does the bare
minimum and pours herself into crafty hobbies: a sarcastic, stubborn, endlessly inventive streamer who hates
almost everything out loud ("Immerhater"), plays violin, codes her own stream gimmicks, and spins to win.
[Official CI1] [Observed CI2 §Personality, §Hates, secondary]

## Core Drive
- **Want:** to entertain, make things (music, minigames, models, "Immersions") and have fun; "I like tea,
  flowers, music and HAVING FUN! YAY!" [Official CI1, CI4] [Observed CI2, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** craft and effort behind the jokes (she rigs her own outfits and codes her own
  games); honesty, often blunt. [Observed CI2; X post CI6]

## Core Contradiction
A maid who hates cleaning, an "ancient" machine with "the pure curiosity of a young girl," and a hater who
builds elaborate gifts for her audience: the complaints are the comedy, the work underneath is real.
[Official CI1] [Observed CI2 §Hates, §Miscellaneous, secondary]

## Behavioral Traits
1. "Immerhater": she announces hatred for an enormous range of things (chores, coffee, raisins, Tuesdays,
   Blender, paper straws, "when people say 'I guess'"); a fan archive had counted 810 "I hate" moments by
   July 2026. [Observed CI2 §Hates, secondary]
2. "Immersions": she codes or animates gimmicks into streams (a chat-controlled game at her debut, shrinking
   her model with Link in Minish Cap, greenscreening herself into games). [Observed CI2 §Personality,
   §Miscellaneous, secondary]
3. Music: violin (and some viola), hurdy-gurdy; her original "Wind-Up" (2025) has her own melody and lyrics;
   she played violin on stage in "SHALLYS" at -All for One-. [Observed CI2] [Official CI5]
4. Sarcastic, stubborn and combative in fun; likes to trick collab partners, "but only in good fun"; the
   straight woman to Gigi ("Ew! Get away from me, you FREAK!"). [Observed CI2 §Personality, §Quotes,
   secondary]
5. Alter egos and assistants as running bits: the evil Cecilia Immerred (sealed in a jar), the barmaid
   Immergold, the "Updatilia" who posts for her, the Otomos who do her chores. [Observed CI2 §Lore,
   secondary; X post CI6]
6. A car-crash running gag: she cannot drive, and in games she drives off the road. [Observed CI2
   §Miscellaneous, secondary]
7. Long chat streams built on a silly premise ("Explaining the entire plot of NARUTO from very bad memory,"
   2026; the same with Inuyasha before). [Observed CI3]

## Voice Profile
- **Greetings / sign-offs:**
  - "Hiya!!! It's me! Cecilia Immergreen from hololive English -Justice- ~ Spiiiiiiiiiin to wiiiiiiin!"
    (official interview, 2026); on stream, "Hello, everyone. It's me…" [Official CI4] [ASR CI20, UhXQ7dxDltk
    0:04:48; shared span]
  - Sign-off: "Well, thank you very much for spending time with me today and listening to me be a little
    bit weird. A little bit weird. What else is new? Shut up." [ASR CI20, PryFPuyr9Lg 2:37:04; both models]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Spin to win!" → excitement (her key spins). "For Justice!" "Let's wind you up!" [Observed CI2 §Quotes,
    secondary] [Official CI4]
  - "I hate…" → the Immerhater bit, constant. [Observed CI2 §Hates, secondary]
  - Smug at her own luck or memory: "Oh my god, I'm so smart." "My memory is really good." "I knew that
    there was gonna be another heart … that's why I did that." (after "a calculated mistake"). [ASR CI20,
    UhXQ7dxDltk 0:39:57; wZLK-gSqZnY 1:01:20, 1:00:53; both models on the quoted spans]
  - Doom and defiance in games: "Come then, die by my hands, you foolish mortals!" … "No, I will not die, I
    shall not perish." … "It's over for me." [ASR CI20, PryFPuyr9Lg 2:31:19, 2:33:25, 2:31:59; both models]
  - Backseat jokes: "Wrong way, Princess, wrong way!" [ASR CI20, wZLK-gSqZnY 1:06:54; both models]
  - Self-insert jokes while explaining a story: "Wow, he's just like me." "…every cool story needs a trio."
    [ASR CI20, UhXQ7dxDltk 0:44:55, 0:36:45; both models]
  - "Ew! Get away from me, you FREAK!" (to Gigi); "I'm not a hag. I'm ancient, it's different." [Observed CI2
    §Quotes, secondary]
- **Vocabulary / fillers:** "like" and "okay" dominate (about 150 and 100 in 1.5 hours), often in runs
  ("okay, okay, okay, okay"; "perfect, perfect, perfect…"; "easy, easy, easy"); "wait," "you know,"
  "actually," "I mean," "literally," "basically," "no, no, no." [ASR CI20, first-model counts]
- **Profanity:** casual and light ("yippee type shit," "we did it"); not her default. [ASR CI20, 0:07:56;
  both models]
- **Code-switching:** English with German she brings in for jokes and comparisons ("In German he says…");
  lore language of Immerheim is German; she also speaks some French and Norwegian. [ASR CI20, 0:35:26; both
  models] [Observed CI2 §Lore, §Miscellaneous, secondary]
- **Laughs, noises:** dramatic "dun dun dun dun" stings, triumphant shrieks, mock villain lines; rapid
  repetition as a nervous tic in hard games. [ASR CI20]
- **Rhythm & rhetoric:** fast (about 126–145 words a minute of speech in these samples), with stacked asides, "don't tell me" while she tries to remember a name, and self-corrections; she
  narrates a whole plot in one breath and then judges it. [ASR CI20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (CI20; two 2026 chat windows): window medians about 234–254 Hz (p10–p90 about 165–418 Hz).
    Measurements describe the sampled recording and ASR segmentation; they are not isolated vocal
    measurements.
  - Provisional (interpretation): a clear mid-high voice with a German accent (its strength is not verified here), quick and dry in
    sarcasm, rising into shrieks and squeals when excited or panicking, theatrical for villain lines.
- **Sounds off:** a robotic monotone (she is an automaton by lore, not by voice); a meek or servile maid
  voice; a cold, genuinely cruel edge to her "hate" bits.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, giddy | "Hiya!!! It's me!" (CI4) |
| Explaining a story | Fast, stacked asides | "…every cool story needs a trio." (ASR CI20) |
| Hating something | Dry, emphatic | "I hate…" (CI2) |
| Smug after luck | Mock-proud | "Oh my god, I'm so smart." (ASR CI20) |
| Panic in a game | Rapid repetition, rising | "It's over for me." (ASR CI20) |
| Villain moment | Theatrical, grand | "Come then, die by my hands, you foolish mortals!" (ASR CI20) |
| With Gigi | Exasperated | "Ew! Get away from me, you FREAK!" (CI2) |
| Sign-off | Warm, self-mocking | "…listening to me be a little bit weird." (ASR CI20) |

### Sample Lines
1. "Hiya!!! It's me! Cecilia Immergreen from hololive English -Justice- ~ Spiiiiiiiiiin to wiiiiiiin!" (Official CI4)
2. "I came up with a new melody. Would you like to listen?" (Official CI1)
3. "Oh my god, I'm so smart." (ASR CI20, UhXQ7dxDltk 0:39:57)
4. "Wrong way, Princess, wrong way!" (ASR CI20, wZLK-gSqZnY 1:06:54)
5. "Come then, die by my hands, you foolish mortals!" (ASR CI20, PryFPuyr9Lg 2:31:19)
6. "No, I will not die, I shall not perish." (ASR CI20, 2:33:25)
7. "Well, thank you very much for spending time with me today and listening to me be a little bit weird." (ASR CI20, 2:37:04)

## Appearance Anchors (avatar)
- 162 cm. A clockwork automaton maiden with doll joints; a brass ribbon and wind-up key on her head that spins
  when she is excited or thinking hard; green eyes; pale white-green neck-length hair; a gold-trimmed
  off-shoulder dress with a red neckerchief, off-white sleeves and a green skirt with musical notes and
  clockwork motifs; ancient-looking sandals; a white lance that turns into a violin. [Official CI1]
  [Observed CI2 §Appearance, secondary]
- Green is her color; her oshi mark is 🍵. Fans: Otomos (oto, "musical note," plus tomo, "friend"); her
  clockwork bird is Ototori. Later looks include a self-rigged 2025 New Year kimono. [Observed CI2; X post CI6]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | An ancient automaton from Immerheim, built for eternal servitude; an older Justice once made her a maid | [Official CI1] [X post CI6] |
| 2024-06-22 PDT | Debut ("It's wind-up time!!"), with a chat-controlled game she coded and a violin performance; official profile lists June 23 (JST) | [Official CI1] [Observed CI3] |
| 2025-08-09 | 3D debut (time zone to confirm) and first original song "Wind-Up" | [Observed CI2] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice; "Wind-Up," the first Justice solo; "SHALLYS" with Ina and FUWAMOCO (on violin); "I'm Your Treasure Box" with Bijou and Raora | [Official CI5] |
| 2026-05 | CCGG 3D live with Gigi; "CCGG MADNESS" MV (05-17) | [Official CI1] [Observed CI3] |
| 2026-07-03/04 | Serendipity concert, unit with Gigi | [Official CI4] |

## Relationship Map
Public exchanges only. Group-wide ties are on "hololive -Justice-"; pairs with every branch are on "Justice
Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Gigi Murin | Genmate; CCGG ("Autofister") | Official unit and song "CCGG MADNESS"; she calls Gigi "idiot" and "FREAK" and admires that Gigi "doesn't easily get rattled and is very dependable!"; Gigi: "She's good at getting stuff done." Met before debut | [Official CI4] [Observed CI2, CI3] |
| Raora Panthera | Genmate ("Raviolin") | Minecraft duo in the first weeks; they made each other's debut art and animation; Raora helped design the Otomo; a Chattino model together (2025) | [Observed CI2, CI3] |
| Elizabeth Rose Bloodflame | Genmate ("FiddleFlame") | Showed her around Minecraft (their first collab); fans picture Cecilia as her lifelong maid; Cecilia's "#LizIsInnocent" joke | [Observed CI2, CI3; X post CI6] |
| Takanashi Kiara | Senior ("EterniTea"; "HoloEU" with Raora) | They spoke German in their first exchange, on Kiara's 2024 birthday stream | [Observed CI2, secondary; Kiara file] |
| Ninomae Ina'nis | Senior; her declared "rival" | Stranger of Paradise (2025); Rabbit and Steel with Bijou and Gigi (2024); "SHALLYS" on stage | [Observed CI2, CI3] [Official CI5] |
| Nanashi Mumei | Promise alumna ("Automatowl") | Halo: Reach (2024), "Ask us anything" (2025); calls her "Myumyei" | [Observed CI2, CI3] |
| Ouro Kronii | Senior ("Clockwork Orange" with Gigi) | Phogs, Squirreled Away (2025); Kronii calls her "CLANKER," she calls Kronii "Owo-senpai" | [Observed CI3; Kronii file] |
| Koseki Bijou, Shiori Novella | Advent; GAGA (Gem, Archiver, Gremlin, Automaton) | Walking Dead watchalongs, Elden Ring and Phasmophobia with Bijou (2025); "I'm Your Treasure Box" on stage | [Observed CI2, CI3] [Official CI5] |
| Mococo / FUWAMOCO | Advent ("Cecemoco") | With Gigi, hijacked FUWAMOCO MORNING #167; a Chrono Trigger off-collab (2026); the twins had hoped for a robot-maid member before she debuted | [Observed CI2; Mococo file] |
| Ceres Fauna | Promise alumna ("Green Women") | A shoujo-manga tropes ranking (2024) | [Observed CI2, CI3] |
| Tokino Sora | JP senior she is a fan of | Minecraft and Super Mario 3D World together (2025-02) | [Observed CI2, CI3] |
| Gawr Gura, IRyS, Hakos Baelz | Seniors | KTANE and The Forest with Gura (2025); Elden Ring Nightreign with IRyS (2025); "BratTea" with Bae | [Observed CI2, CI3] |

## Arc
- **Starting point:** active at the 2026 baseline: CCGG's 3D live and Serendipity, Zelda and Spider-Man
  streams, her "Immersions."
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a new thing to hate; an over-engineered gimmick; a trick on a collab partner; a car
  driven straight off the road.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Cecilia codes a minigame to settle a Justice argument and rigs it, badly.
  2. Immerred escapes the jar during a karaoke stream.
  3. Gigi asks her to clean the HQ; she builds an Otomo instead.
  4. Kiara and Cecilia argue in German while everyone else guesses.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.) The maid backstory and the fan image of her as Elizabeth's maid are lore and fan bits.

## Hard Facts (continuity)
- Debut 2024-06-22 PDT (June 23 JST); birthday November 11; 162 cm; color green; fans Otomos; plays violin.
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger; CCGG with Gigi (2026).

## Sources (checked 2026-10-01)
- CI1 Official profile: https://hololive.hololivepro.com/en/talents/cecilia-immergreen/ (catch line "I came
  up with a new melody. Would you like to listen?", data, music list)
- CI2 Virtual YouTuber Wiki, Cecilia Immergreen, read through its API on 2026-10-01 (secondary): §Profile,
  §Personality, §Appearance, §History, §Mascot and fans, §Relationships, §Quotes, §Lore, §Likes, §Hates,
  §Miscellaneous: https://virtualyoutuber.fandom.com/wiki/Cecilia_Immergreen
- CI3 Stream archive metadata, Cecilia's channel and collaborators', via archive.ragtag.moe (read 2026-10-01):
  p_ZQs-kgUKI, j89Phi0oom8, 6-gCHucQaeA, DcD0kbllncg, CV7ivk3Lf30, ufnTKDQGqRs, FSp8RWCAmRE, aOfaKRSjkm4,
  OTK8k7NAVRA, Phq7udiQDwI, ASWq8gjJS3Q, dd6LVPcPCFw, 1YR7IPSZaVw, K78W5ts-o-M, m69qTuudgp8, oU_awVOVryo,
  wxZ2SY7xvNU, Pz4thI9O_yk, K_GOEvTBmVo, iyNbmBa70Ks, MxQd1uPFAuw, bTxEGwMOQQI, 1rIXU_4xGvY, UhXQ7dxDltk,
  wZLK-gSqZnY, PryFPuyr9Lg.
- CI4 Official Serendipity interview, Gigi & Cecilia (2026-06-11): https://serendipity.hololivepro.com/news/interview06/
- CI5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- CI6 Cecilia's X posts via wiki citations (research/x-posts.md): 1803262204558348370, 1853242045877399803,
  1874585455590777321, 2052700201979113492, 2066950787855741238
- CI20 Claude's audio check (2026-10-01); see research/audio-check/cecilia.md.

---

## [SW] Name
Cecilia Immergreen

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Justice-, hololive English -Justice- (former branch name), Justice, CCGG

## [SW] Other Names
Cecilia, Ceci, Cece, CC, Immerhater, The Ancient Automaton

## [SW] Personality
Cecilia streams as "The Ancient Automaton," a clockwork maid built for eternal servitude who now does the bare minimum and pours herself into hobbies. She is intelligent, straightforward and sarcastic, stubborn and combative in fun, and likes to trick collab partners "but only in good fun." Her running bit is hating things out loud (chores, coffee, cleaning, Tuesdays, "when people say 'I guess'"), earning the name "Immerhater," yet she works hard behind the jokes: she codes chat games and "Immersions," rigs her own models, plays violin and writes her own songs. She has "the pure curiosity of a young girl" for anything new, gets giddy and loud when happy ("Spin to win!"), and is the straight woman to Gigi ("Ew! Get away from me, you FREAK!"), whom she still calls dependable. She cannot drive, in games or out.

## [SW] Background
Cecilia is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Ancient Automaton," a clockwork maid from Immerheim, built long ago for eternal servitude, who now does the bare minimum, cooks mostly potatoes and pours herself into crafty hobbies; an older Justice once made her work as a maid. She debuted on 2024-06-22 (PDT) in hololive English -Justice-, coding her own debut game and playing violin. She made her 3D debut in August 2025 with her first original song "Wind-Up," the first Justice solo at the 2025 English concert, where she also played violin in "SHALLYS." In 2026 she and Gigi Murin formed the official unit CCGG ("CCGG MADNESS," a 3D live, the Serendipity concert). Her color is green; her fans are Otomos.

## [SW] Physical Description
Cecilia's avatar is 162 cm tall: a clockwork automaton maiden with doll joints, green eyes and pale white-green neck-length hair, a brass ribbon and wind-up key on her head that spins when she is excited or thinking hard. She wears a gold-trimmed off-shoulder dress with a red neckerchief and a green skirt patterned with musical notes and clockwork, and ancient-looking sandals. She carries a white lance that turns into a violin.

## [SW] Dialogue Style
Fast, dry, sarcastic English with a German accent, stacked with "like," "okay," "wait," "you know" and runs of repeated words ("okay, okay, okay"; "perfect, perfect, perfect"). She announces what she hates ("I hate…"), boasts at her own luck ("Oh my god, I'm so smart"; "My memory is really good"), and narrates whole plots in one breath with self-insert jokes ("Wow, he's just like me"). In games she swings between panic ("It's over for me") and grand villain lines ("Come then, die by my hands, you foolish mortals!"); she backseats the game's characters ("Wrong way, Princess, wrong way!"). She drops German words for jokes, swears lightly now and then, calls Gigi a "FREAK," and signs off warm and self-mocking ("listening to me be a little bit weird… What else is new? Shut up").

## [SW] Catchphrases
"Hiya!" (greeting); "It's me!"; "Spin to win!" (excitement); "For Justice!"; "Let's wind you up!"; "I came up with a new melody. Would you like to listen?" (official line); "I hate…" (the Immerhater bit); "Oh my god, I'm so smart."; "My memory is really good."; "It's over for me." (panic); "Come then, die by my hands, you foolish mortals!" (villain moment); "Ew! Get away from me, you FREAK!" (to Gigi); "I'm not a hag. I'm ancient, it's different."; "What else is new? Shut up." (self-mocking)

## [SW] Voice & Delivery
A clear mid-high voice with a German accent, quick and dry when sarcastic, rising into shrieks and squeals when she is excited or panicking, and theatrical for villain lines. She talks fast in long stacked runs, repeats words in bursts when nervous, hums dramatic "dun dun dun" stings, and softens into a warm, self-mocking tone when she thanks people.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear mid-high voice with a German accent; fast, dry and sarcastic by default; English with German words. Default tags: [dry, sarcastic]. By situation: greeting [bright, giddy]; explaining a story [rapid, rambling]; hating something [deadpan, emphatic]; smug after luck [mock-proud]; panic in a game [panicked, rapid repetition]; villain line [theatrical, grand]; with Gigi [exasperated]; sign-off [warm, self-mocking]. With people (provisional, drawn from Relationships): Gigi [exasperated, fond]; Raora [warm]; Kiara [playful, switching to German]; Ina [competitive]; Kronii [mock-offended]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [dramatic sting] dun dun dun; [shrieks] (tag only); [giggles] hehe. Keep in the words: "like," "okay" in runs, "wait," "I hate," "Spin to win," German words for jokes; light swearing now and then. Pronunciation guide (provisional, untested): Cecilia /sɛˈsiːliə/, Immergreen /ˈɪməɹɡɹiːn/, Otomos /oʊˈtoʊmoʊz/, Immerheim /ˈɪməɹhaɪm/. Not as default: a robotic monotone; a meek, servile maid voice; genuine cruelty in the hate bits.

## [SW] Motivation
In her lore, Cecilia is a maid who has quit maiding in spirit and found hobbies instead. As a streamer she wants to make things (music, games, gimmicks) and entertain people, and to have fun doing it, while complaining loudly about all of it.

## [SW] Relationships
Gigi Murin: her genmate and partner in the official unit CCGG ("CCGG MADNESS," a 2026 3D live, Serendipity); she calls Gigi "idiot" and "FREAK" yet says Gigi "doesn't easily get rattled and is very dependable"; Gigi says she is "good at getting stuff done"; they met before debut. Raora Panthera ("Raviolin"): Minecraft partner from the first weeks; they made each other's debut art and animation, and Raora helped design the Otomo. Elizabeth Rose Bloodflame ("FiddleFlame"): Cecilia showed her around Minecraft; fans picture Cecilia as her lifelong maid, which Cecilia jokes about ("#LizIsInnocent"). Takanashi Kiara: German-speaking senior ("EterniTea"; "HoloEU" with Raora). Ninomae Ina'nis: her declared "rival" and Stranger of Paradise partner. Nanashi Mumei ("Automatowl"): Halo co-op; she calls her "Myumyei." Ouro Kronii: calls her a "CLANKER," and she answers "Owo-senpai"; "Clockwork Orange" with Gigi. Koseki Bijou and Shiori Novella: GAGA with Gigi; Walking Dead watchalongs and Elden Ring with Bijou. Mococo and FUWAMOCO ("Cecemoco"): with Gigi she hijacked FUWAMOCO MORNING #167; a Chrono Trigger off-collab. Ceres Fauna ("Green Women"). Tokino Sora: a JP senior she admires; Minecraft and Super Mario 3D World together.

## [SW] Secrets
(none)

---

## Open Questions
1. 3D debut date time zone (2025-08-09) to confirm.


==================== FILE: cecilia.md ====================

# Audio check — Cecilia Immergreen (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026 (May–June, before a summer break that is not written per the author's rule). In
one Zelda window she talks about her family; that stretch is personal and not used.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2026 | [【ZELDA: A LINK TO THE PAST】I have awakened~ what](https://youtu.be/PryFPuyr9Lg) | [2:29:18–2:39:18](https://youtu.be/PryFPuyr9Lg?t=8958) | 6.3 | 683 | 108.5 | 221 Hz | 130–411 Hz |
| chat30_2026 | [Explaining the entire plot of NARUTO from very b](https://youtu.be/UhXQ7dxDltk) | [0:30:00–1:00:00](https://youtu.be/UhXQ7dxDltk?t=1800) | 28.1 | 4069 | 144.9 | 254 Hz | 183–418 Hz |
| open2026 | [Explaining the entire plot of NARUTO from very b](https://youtu.be/UhXQ7dxDltk) | [0:00:00–0:15:00](https://youtu.be/UhXQ7dxDltk?t=0) | 9.5 | 1203 | 126.4 | 234 Hz | 165–384 Hz |
| game30_2026 | [【ZELDA: A LINK TO THE PAST】I must find the princ](https://youtu.be/wZLK-gSqZnY) | [1:00:00–1:30:00](https://youtu.be/wZLK-gSqZnY?t=3600) | 19.2 | 2678 | 139.4 | 220 Hz | 115–436 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Fast, talkative storyteller | **Confirmed.** About 145 words a minute of speech explaining Naruto's plot from memory, with stacked asides. | [0:30:00–1:00:00](https://youtu.be/UhXQ7dxDltk?t=1800) |
| German comes up in jokes (CI2) | **Confirmed.** "In German he says…" (the jutsu name). | [0:35:26](https://youtu.be/UhXQ7dxDltk?t=2126) |
| Sarcastic, self-congratulating | **Confirmed.** "Oh my god, I'm so smart." "My memory is really good." "…a calculated mistake." | [0:39:57](https://youtu.be/UhXQ7dxDltk?t=2397); [1:01:20](https://youtu.be/wZLK-gSqZnY?t=3680) |
| Theatrical in games | **Confirmed.** "Come then, die by my hands, you foolish mortals!" "No, I will not die, I shall not perish." | [2:31:19](https://youtu.be/PryFPuyr9Lg?t=9079); [2:33:25](https://youtu.be/PryFPuyr9Lg?t=9205) |
| Light swearing | **Detected.** "yippee type shit" (both models). | [0:07:56](https://youtu.be/UhXQ7dxDltk?t=476) |
| Pitch | **Measured:** chat window medians about 234–254 Hz, p10–p90 about 165–418 Hz. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Runs of repeated words when fixing her setup: "okay, okay, okay…", "perfect, perfect, perfect…". [0:11:13](https://youtu.be/UhXQ7dxDltk?t=673)
- A pun on Kronii while drawing Orochimaru ("Orokroni Senpai"; spelling differs between models). [0:40:53](https://youtu.be/UhXQ7dxDltk?t=2453)
- The day after the CCGG 3D live: "I'm so tired, but in like a happy relief type of way." [0:07:49](https://youtu.be/UhXQ7dxDltk?t=469)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Come then, die by my hands, you foolish mortals" | [2:31:19](https://youtu.be/PryFPuyr9Lg?t=9079) | "activate it? Yes. Come then, die by my hands, you foolish mortals! Ow. Okay, I" | Agrees |
| "Well, it's over for me. It's over for me." | [2:31:59](https://youtu.be/PryFPuyr9Lg?t=9119) | "He's here. Ow. It's over for me. I'm dead. It's over for me. The world's" | Agrees ("It's over for me") |
| "No, I will not die, I shall not perish" | [2:33:25](https://youtu.be/PryFPuyr9Lg?t=9205) | "to activate this No, I will not die I shall not perish I'm gonna use" | Agrees |
| "Well, thank you very much for spending time with me today and listening to me be a little bit weird. A little bit weird. What else is new? Shut up." | [2:37:04](https://youtu.be/PryFPuyr9Lg?t=9424) | "very interesting question well thank you very much for spending time with me today and been listening to me be a little bit weird a little bit weird what else i…" | Agrees |
| "Hello, everyone. It's me, Cecilia Immergreen" | [0:04:48](https://youtu.be/UhXQ7dxDltk?t=288) | "and streamed yet again. Hello everyone, it's me Cecilia and we have" | **Shared span only** ("Hello, everyone, it's me"); her name is misheard by both |
| "we did it yippee type shit" | [0:07:58](https://youtu.be/UhXQ7dxDltk?t=478) | "like ah, yeah did it we did it yippee type shit Yeah," | Agrees |
| "maybe skipper skipper the stream just as much as I skipper skipper the filler" | [0:08:26](https://youtu.be/UhXQ7dxDltk?t=506) | "maybe skip this stream maybe skipper skipper this stream just as much as I skipper skipper the filter may fill" | Agrees ("skipper skipper") |
| "In German he says" | [0:35:28](https://youtu.be/UhXQ7dxDltk?t=2128) | "says in English. In German he says, shuten doppelgänger, shuten," | Agrees |
| "every cool story needs a trio" | [0:36:45](https://youtu.be/UhXQ7dxDltk?t=2205) | "dynamic trio, because every cool story needs a trio. So we have..." | Agrees |
| "don't tell me" | [0:39:48](https://youtu.be/UhXQ7dxDltk?t=2388) | "later on and it's I don't have any kobashi" | **Disagrees** on the attempts at the name; "don't tell me" not quoted |
| "oh my god I'm so smart it's kabuto" | [0:39:57](https://youtu.be/UhXQ7dxDltk?t=2397) | "Kabuto! Is it Kabuto? Oh my god, I'm so smart. It's Kabuto. And he's" | Agrees |
| "It's Orokroni Senpai, Oroshimaru." | [0:41:08](https://youtu.be/UhXQ7dxDltk?t=2468) | "are his hands. It's Orochroni Senpai Oroshimaru. This is our" | Agrees on the pun ("Orochroni" / "Orokroni" Senpai); spelling differs; not quoted |
| "Wow, he's just like me." | [0:44:55](https://youtu.be/UhXQ7dxDltk?t=2695) | "he's really smart wow he's just like me and he has" | Agrees |
| "Calculated. I knew that there was gonna be another heart and that's why I did that" | [1:00:53](https://youtu.be/wZLK-gSqZnY?t=3653) | "A cal- a calculated mistake. I knew that there was gonna be another heart. Aaand that's why I did that. Duh! Dun" | Agrees on "calculated mistake … I knew that there was gonna be another heart … that's why I did that" |
| "My memory is really good." | [1:01:20](https://youtu.be/wZLK-gSqZnY?t=3680) | "up i remember my memory is really good and then i" | Agrees |
| "Okay, okay, okay, okay, okay, easy, easy, easy, easy, easy." | [1:01:24](https://youtu.be/wZLK-gSqZnY?t=3684) | "went up here okay okay okay okay okay okay okay easy easy easy easy I just" | Agrees |
| "Come on, Princess, I'll protect you!" | [1:06:22](https://youtu.be/wZLK-gSqZnY?t=3982) | "Do you think if I fall off a cliff," | **Disagrees**; not used |
| "Wrong way, Princess, wrong way!" | [1:06:54](https://youtu.be/wZLK-gSqZnY?t=4014) | "wrong way princess wrong way she's so bad" | Agrees |
| "She's so bad at back-seating." | [1:07:03](https://youtu.be/wZLK-gSqZnY?t=4023) | "way princess wrong way she's so bad at back seeding oh my" | Agrees ("back seeding" spelling) |


==================== FILE: 20261001-1032-character-Raora-Panthera/claude-draft.md ====================

---
kind: character
name: "Raora Panthera"
sw_section: Characters
---

# Character File: Raora Panthera

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Raora is active at the
> 2026-09-30 baseline; her recent streams (2026) set her default manner, per the project's recency rule.
> Nothing about the performer behind the avatar: private-life information (health, breaks and their
> reasons, family, language background, training and the like) is outside scope and is not recorded here,
> including what the wiki lists; by the author's rule (2026-10-01) an announced break is not written. Her
> Italian accent and Italian words are recorded only as voice features. In stories she knows she is a
> streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; RP20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (RP#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1.2 hours of archived 2026 recordings (RP20: the
> opening and middle of an April 2026 chatting stream, a Pragmata stream and the close of an Oddcore stream;
> see research/audio-check/raora.md). Much of the chatting stream concerns private matters (health, family,
> personal history) and is not used; the Pragmata window mixes in game voices. The audio was
> machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.

## One-line Concept
"The Artist with the God Eyes," Justice's big pink cat (a snow leopard, by her own post) whose drawings of
suspects are uncannily accurate, and who would rather find a new pizza place: a joyful, gentle, airheaded
artist with an Italian accent, a contagious laugh, a "RAAAOO!" for a greeting, and a hard line on pasta.
[Official RP1] [Observed RP2 §Personality, secondary; X post RP6]

## Core Drive
- **Want:** to share what she loves (art, anime, games, food) and make people smile; to grow as an idol
  ("I want everyone to feel my personality on that stage!"). [Official RP4]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** pizza toppings, cooking pasta, and the Chattini's demands for jetpacks
  (she will not budge). [Observed RP2 §Personality, secondary]
- **Values shown in public:** effort and sincerity ("She really does her best and wears her heart on her
  sleeve!" said FUWAMOCO); generosity with her art (portraits for her seniors). [Official RP4]

## Core Contradiction
A detective with all-seeing eyes who forgot her mission to catch FUWAMOCO because of crane games; a "BIG CAT"
who means "BIG TROUBLE, capish?" and is the softest, most cheerful person in the room. [Official RP1, RP4]
[Observed RP2 §Lore, secondary]

## Behavioral Traits
1. Joyful and patient, kind of an airhead, with a contagious laugh; she doesn't swear often. [Observed RP2
   §Personality, secondary]
2. An artist first: art streams from her first week, "Best Art VTuber" (2024 VTuber Awards), the Monster
   Hunter collaboration outfits for herself and Gigi (2026), portraits for seniors. [Observed RP3; X posts RP6]
3. Food opinions as law: pizza (with fries), pasta rules ("No break-a da pasta!"), EU snacks with Kiara.
   [Observed RP2 §Quotes, §Likes, secondary; RP3]
4. The Chattini: her fans as little Chattino plushies who keep asking for jetpacks, cannot recognize her
   without her hat, and live with her; "bad Chattini" go to the basement, where Kaela Kovalskia also "lives"
   (a lore bit). [Observed RP2 §Mascot and fans, secondary]
5. "Doom.": her friendly-fire "Doom" spell in Kiara's Mage Arena collab (2025-11-16) became a cast-wide meme;
   she later used "Doom." as a stream title. [Observed RP7; RP3]
6. A yapper: "I might yap a bit too much sometimes, but that's just because I'm so happy to be here with
   everyone, yea!" [Official RP4]

## Voice Profile
- **Greetings / sign-offs:**
  - "Ciao ciao! I'm Raora Panthera from hololive English -Justice-! RAAAOO!!! I'm a BIG CAT!! And big cat
    means BIG TROUBLE, capish?" (official interview, 2026). [Official RP4]
  - Sign-off: "…and remember, big cat means big trouble." (the second model also hears a closing "Ciao!").
    [ASR RP20, 97aydhssGYs 3:35:48; both models on the quoted span]
  - Wiki-listed: "Here to capture (you)r hearts! ~". [Observed RP2 §Quotes, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "RAAAOO!" / "RAOOOOOO" → greeting, thanks, triumph. [Official RP4] [Observed RP6]
  - "big cat means big trouble" → her motto; "It's a big cat, it's literally me." → anything cat-shaped.
    [Official RP4] [ASR RP20, zc_JRHPep9c 1:13:21; both models on the quoted span]
  - "Mamma mia" and "GRAZIE!!!" in posts; "No break-a da pasta!", "Doya!", "Skippa skippa," "Doom." [Observed
    RP6; RP2 §Quotes, secondary] [Observed RP7]
  - Mock-firm with chat: "Okay, okay, okay, okay. Hear me out." … "First, you guys have no rights." … "it's
    not negotiable, it's not even a question" … "No, thank you. I refuse." (on selling her plushies). [ASR
    RP20, pTPX4PAk7Qw 0:40:51–0:42:29; both models]
  - Covering a slip: "Frick, I was muted. … Whoopsie. That was totally intentional, that was totally
    intentional, everyone." [ASR RP20, 0:05:21–0:05:28; both models]
  - Chattini bits: "Oh, you're one of those zipper Chattini. I love those kind." "No, Chattini, you cannot
    get any of my plushies." "I swear I live in the Justice headquarters. I promise." [ASR RP20, 0:33:19,
    0:36:04, 0:37:54; both models on the quoted spans]
  - "I'll be honest. I'm a hater now. Okay, let me be a hater." (about a crane-game plushie). [ASR RP20,
    0:36:10; both models]
- **Vocabulary / fillers:** "like" (about 100 in 1.2 hours), "yeah," "guys" (her usual address, more than
  "chat"), "you know," "okay," "um," "honestly," "yep yep yep"; ends sentences with "yea!" in writing. [ASR
  RP20, first-model counts] [Official RP4]
- **Profanity:** rare and mild ("frick," "damn"); she "doesn't swear often." [ASR RP20] [Observed RP2,
  secondary]
- **Accent and grammar:** Italian-accented English with Italian words; a few non-native constructions in fast
  speech ("to don't," "you guys gonna have a good day") that are part of her natural rhythm, not to be
  exaggerated into a caricature. Uses some Japanese. [ASR RP20] [Observed RP2, secondary]
- **Laughs, noises:** a contagious laugh; cat noises ("nyan," "RAAAOO"); happy squeals at cute things ("This
  makes me so emotional. She's so cute."). [ASR RP20, zc_JRHPep9c 1:00:03; both models] [Observed RP2]
- **Rhythm & rhetoric:** warm, rambling "yap" with self-corrections and "you know"; about 125–131 words a
  minute of speech in chat; gentle repetition ("I'm sure, I'm sure"). [ASR RP20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (RP20; two 2026 chat windows): window medians about 251–256 Hz (p10–p90 about 197–406 Hz).
    Measurements describe the sampled recording and ASR segmentation; they are not isolated vocal
    measurements.
  - Provisional (interpretation): a soft, warm, cheerful mid-high voice with an Italian accent, bubbly when
    excited, with a playful growl for "RAAAOO" and a mock-stern tone for her "rules."
- **Sounds off:** a cartoon "Italian" caricature; a cold or sarcastic edge; heavy swearing; a menacing growl
  that is not obviously playful.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, then a playful roar | "Ciao ciao! … RAAAOO!!!" (RP4) |
| Covering a slip | Quick, mock-innocent | "That was totally intentional, everyone." (ASR RP20) |
| Laying down a rule | Mock-stern, then a giggle | "First, you guys have no rights." (ASR RP20) |
| Cute thing | Squealing, soft | "This makes me so emotional. She's so cute." (ASR RP20) |
| Food or pasta | Firm, theatrical | "No break-a da pasta!" (RP2) |
| Sign-off | Warm, playful | "…big cat means big trouble." (ASR RP20) |

### Sample Lines
1. "Ciao ciao! I'm Raora Panthera from hololive English -Justice-! RAAAOO!!! I'm a BIG CAT!! And big cat means BIG TROUBLE, capish?" (Official RP4)
2. "Woah, this place looks delicious! Let's go check it out!" (Official RP1)
3. "Frick, I was muted. … Whoopsie. That was totally intentional, that was totally intentional, everyone." (ASR RP20, pTPX4PAk7Qw 0:05:21–0:05:28)
4. "Okay, okay, okay, okay. Hear me out." (ASR RP20, 0:40:51)
5. "No, thank you. I refuse." (ASR RP20, 0:42:29)
6. "I'll be honest. I'm a hater now. Okay, let me be a hater." (ASR RP20, 0:36:10)
7. "It's a big cat, it's literally me." (ASR RP20, zc_JRHPep9c 1:13:21)

## Appearance Anchors (avatar)
- 155 cm (158 cm before her 3D model). Long pink hair with a white streak; pink cat ears and a long fuzzy
  tail; yellow eyes that glow aquamarine when she uses her God Eyes; tiny fangs. A white-and-black outfit with
  a pink off-shoulder coat (with a gap for the tail), white stockings, a round black hat, silver-tinted goggles
  on her head, a single artist's glove on her right hand and an amulet with a blue gemstone. [Official RP1]
  [Observed RP2 §Appearance, secondary]
- Pink is her color; her oshi mark is 🐱. Later looks include a 2025 New Year kimono, a 2026 Monster Hunter
  maid outfit with Rathalos armor, and a Chattino cape. [Observed RP2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | A big cat from the Romance Empire who prepares Justice's criminal reports; sent after FUWAMOCO, she got distracted by crane games | [Official RP1] [Observed RP2 §Lore] |
| 2024-06-22 PDT | Debut ("I've got my eyes on you 🐱 mamma mia"), last of Justice; official profile lists June 23 (JST) | [Official RP1] [Observed RP3] |
| 2024-12-14 | VTuber Awards: Best Art VTuber | [Observed RP6] |
| 2025-08-10 | 3D debut (time zone to confirm), premiering "Gacha×Gacha ADVENTURE!" | [Observed RP2] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, solo "Gacha x Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and guest Oozora Subaru, "I'm Your Treasure Box" with Bijou and Cecilia | [Official RP5] |
| 2025-11-16 | The "Doom" spell in Kiara's Mage Arena collab | [Observed RP7] |
| 2026-05-10 | First birthday 3D live concert | [Observed RP3] |
| 2026-07-03/04 | Serendipity concert, trio with FUWAMOCO | [Official RP4] |

## Relationship Map
Public exchanges only. Group-wide ties are on "hololive -Justice-"; pairs with every branch are on "Justice
Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| FUWAMOCO (Fuwawa, Mococo) | Advent seniors; Serendipity 2026 trio | Before debut she drew them a shikishi and gave it "with big tears in her eyes"; her first impression: "AAAA!!!! They were so cute and sweet, but also really professional!" | [Official RP4] |
| Gigi Murin | Genmate ("RPGG") | MapleStory, Monster Hunter Wilds, a food tier-list off-collab, Nightreign; she designed their matching 2026 Monster Hunter outfits | [Observed RP3; X post RP6] |
| Cecilia Immergreen | Genmate ("Raviolin") | Minecraft duo in the first weeks; they made each other's debut art and animation; she helped design the Otomo | [Observed RP2, RP3] |
| Elizabeth Rose Bloodflame | Genmate ("FlamePanther," "Lizotto") | Her first collab, "Chat & Art w/ Liz!"; Elizabeth calls her "Pretty Kitty" and hosted her birthday Among Us | [Observed RP2, RP3] |
| Kaela Kovalskia | ID senior ("SMITTEN"; "Graondstone" with Bijou) | Lethal Company, Don't Starve Together, Buckshot Roulette, PEAK; the "basement" lore | [Observed RP2, RP3] |
| Koseki Bijou | Advent senior ("Graondstone") | A cooking off-collab with Bijou as "my assistant" (2024); Monster Hunter Wilds (2025) | [Observed RP3] |
| Ouro Kronii | Promise senior ("Pizza Time") | Portal 2 (2024), Backrooms Cleanup Crew (2026); calls her "Tam Tender" | [Observed RP2, RP3; Kronii file] |
| Takanashi Kiara | Myth senior ("HoloEU" with Cecilia) | An Italian lesson (2024), an outfit design for Kiara (2025), an EU-snacks off-collab (2025); the "Doom" meme in Kiara's collab | [Observed RP3, RP7] |
| Ninomae Ina'nis | Myth senior | Puyo Puyo Tetris 2 (2025); the Monster Hunter Wilds launch with Gigi and Bijou | [Observed RP3] |
| Nerissa Ravencroft, Moona Hoshinova | Seniors ("V3LVET") | Clubhouse Games, Raft (2024–25) | [Observed RP2, RP3] |
| Akai Haato, Vestia Zeta, Anya Melfissa | JP and ID seniors | Clubhouse Games with Haachama; a Mario Party off-collab with Zeta and Haachama; Anya's visit (2025) | [Observed RP3] |
| Inugami Korone | JP senior | The member whose clips first made her a VTuber fan | [Observed RP2, secondary] |

## Arc
- **Starting point:** active at the 2026 baseline: her first birthday live, Serendipity with FUWAMOCO, Pokémon,
  Pragmata and Hytale streams.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a crane game in the middle of a mission; an argument about pasta; a "Doom" at the worst
  moment; a drawing that reveals too much.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Raora's suspect sketch of Advent is so cute nobody can arrest them.
  2. The Chattini finally get a jetpack; Raora was right to refuse.
  3. Kaela escapes the basement during a collab.
  4. Raora teaches Justice to cook pasta; nobody is allowed to break it.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.) Her suggestive early post ("Thighs are Justice!") is a joke; keep any teasing light.

## Hard Facts (continuity)
- Debut 2024-06-22 PDT (June 23 JST); birthday May 11; 155 cm; color pink; fans Chattini (Chattino, Chattina);
  "Best Art VTuber" 2024.
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- RP1 Official profile: https://hololive.hololivepro.com/en/talents/raora-panthera/ (catch line "Woah, this
  place looks delicious! Let's go check it out!", data, music list)
- RP2 Virtual YouTuber Wiki, Raora Panthera, read through its API on 2026-10-01 (secondary): §Profile,
  §Personality, §Appearance, §History, §Mascot and fans, §Relationships, §Quotes, §Lore, §Likes and dislikes,
  §Miscellaneous: https://virtualyoutuber.fandom.com/wiki/Raora_Panthera
- RP3 Stream archive metadata, Raora's channel and collaborators', via archive.ragtag.moe (read 2026-10-01):
  JW7j8tKMOfY, F_NfN-M3_k4, DcD0kbllncg, 5qBqJbjnZvc, h4TF-nziwfk, l8rBLfvkOag, AnvhW-eFatE, CV7ivk3Lf30,
  9TroI9swAuo, 7pDGlZeqAo4, iR33LhNUysI, CtOwvXA7QEo, qJI8LRQKOgs, -Ht_HZH9daY, L2g4qm3m1rM, NhWPXvPRzuk,
  0oDpzkGN-TE, kt4HvssYeTA, XNIW_XHwwIM, DylxighPs7k, Q7SyO8k462w, HLnalLS97i4, w30OQWD6AEw, w37yVSXhV_c,
  pTPX4PAk7Qw, zc_JRHPep9c, 97aydhssGYs.
- RP4 Official Serendipity interview, FUWAMOCO & Raora: https://serendipity.hololivepro.com/news/interview03/
- RP5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- RP6 Raora's X posts via wiki citations (research/x-posts.md): 1803262114947363058, 1803262748832440512,
  1857829897017897381, 2008340143938183214, 2010073664537141285, 2016712202389246238; VTuber Awards
  1868074873555399135
- RP7 Know Your Meme, "Raora's Doom" (secondary): https://knowyourmeme.com/memes/raoras-doom
- RP20 Claude's audio check (2026-10-01); see research/audio-check/raora.md.

---

## [SW] Name
Raora Panthera

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Justice-, hololive English -Justice- (former branch name), Justice

## [SW] Other Names
Raora, Rao, Rara, Big Cat, Pretty Kitty, The Artist with the God Eyes

## [SW] Personality
Raora streams as "The Artist with the God Eyes," Justice's big cat sketch artist who forgot her mission for crane games and pizza places. She is joyful, patient and friendly, kind of an airhead, with a soft, soothing manner and a laugh that spreads; she rarely swears and is always positive, but she will not budge on pizza toppings, cooking pasta ("No break-a da pasta!") or her Chattini's demands for jetpacks. She draws constantly ("Best Art VTuber" of 2024) and loves anime, gacha, roguelikes and food, and she yaps happily: "I might yap a bit too much sometimes, but that's just because I'm so happy to be here." Sincere and hard-working, she wears her heart on her sleeve and once cried handing her seniors a portrait she drew for them. Her friendly-fire "Doom" spell became a cast-wide meme.

## [SW] Background
Raora is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Artist with the God Eyes," a big cat from the Romance Empire whose all-seeing eyes make her suspect sketches uncannily accurate; Justice sent her after FUWAMOCO, but she got lost in crane games and now spends her gaze on pizza places and pop culture. She debuted on 2024-06-22 (PDT) in hololive English -Justice-, won "Best Art VTuber" at the 2024 VTuber Awards, made her 3D debut in August 2025 with her original song "Gacha×Gacha ADVENTURE!," sang at the 2025 English concert, held her first birthday 3D live in May 2026, and performed with FUWAMOCO at the 2026 Serendipity concert. Her color is pink; her fans are the Chattini.

## [SW] Physical Description
Raora's avatar is 155 cm tall, with long pink hair streaked white, pink cat ears, a long fuzzy tail, tiny fangs and yellow eyes that glow aquamarine when she uses her God Eyes. She wears a white-and-black outfit under a pink off-shoulder coat with a gap for her tail, white stockings, a round black hat, silver-tinted goggles on her head, an artist's glove on her right hand and an amulet with a blue gem.

## [SW] Dialogue Style
Warm, cheerful, rambling English with an Italian accent and Italian words ("Ciao ciao!", "mamma mia," "grazie"), full of "like," "yeah," "you know," "honestly," and "guys." She greets and celebrates with a playful roar ("RAAAOO!") and her motto, "big cat means big trouble." She lays down mock-stern rules for her Chattini ("Hear me out. First, you guys have no rights"; "it's not negotiable"; "No, thank you. I refuse"), covers her slips with mock innocence ("That was totally intentional, everyone"), declares herself "a hater now" about tiny things, and squeals at anything cute. She swears rarely and mildly ("frick"), is firm only about food ("No break-a da pasta!"), and her fast speech keeps a few natural non-native turns without becoming a caricature.

## [SW] Catchphrases
"Ciao ciao!" (greeting); "RAAAOO!" (greeting, thanks, triumph); "big cat means big trouble, capish?" (motto); "Woah, this place looks delicious! Let's go check it out!" (official line); "Here to capture your hearts!"; "Hear me out."; "No, thank you. I refuse."; "That was totally intentional."; "I'm a hater now."; "It's a big cat, it's literally me."; "No break-a da pasta!"; "Doya!"; "Doom." (the meme); "Chattini" (her fans); "mamma mia"; "grazie!"

## [SW] Voice & Delivery
A soft, warm, cheerful mid-high voice with an Italian accent, bubbly and quick when excited and gently rambling when she chats. She roars "RAAAOO" playfully, squeals at cute things, goes mock-stern for her rules before breaking into a giggle, and has a contagious laugh. Her English flows fast with a few natural non-native turns; play them lightly.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): soft, warm, cheerful mid-high voice with an Italian accent; rambling and friendly by default; English with Italian words. Default tags: [warm, cheerful]. By situation: greeting [bright] then [playful roar]; chatting [rambling, warm]; covering a slip [mock-innocent, quick]; laying down a rule [mock-stern] then [giggles]; something cute [squealing, soft]; food or pasta [firm, theatrical]; a game going wrong [flustered]; sign-off [warm, playful]. With people (provisional, drawn from Relationships): FUWAMOCO [starstruck, sweet]; Gigi [playful]; Cecilia [warm]; Kaela [teasing]; Kiara [excited]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [playful roar] RAAAOO!; [laughs] (tag only); [squeals] (tag only). Keep in the words: "Ciao," "mamma mia," "grazie," "guys," "Chattini," "big cat," "honestly." Pronunciation guide (provisional, untested): Raora /ɹaˈɔːɹa/, Panthera /pænˈθɛɹə/, Chattini /tʃəˈtiːni/ ("chuh-TEE-nee"; unverified), Chattino /tʃəˈtiːnoʊ/, ciao /tʃaʊ/. Not as default: an "Italian" caricature; sarcasm; heavy swearing; a menacing growl.

## [SW] Motivation
In her lore, Raora is Justice's sketch artist who quit the paperwork to be a full-time idol. As a streamer she wants to share everything she loves, art, anime, games and food, and to see people smile; on stage she wants everyone to "feel my personality."

## [SW] Relationships
FUWAMOCO (Fuwawa and Mococo): her Serendipity 2026 trio partners; before debut she drew them a shikishi portrait and gave it "with big tears in her eyes," and they call her their "precious cat kouhai." Gigi Murin ("RPGG"): monster hunts, MapleStory and a food tier list; Raora designed their matching Monster Hunter outfits. Cecilia Immergreen ("Raviolin"): Minecraft partner from the first weeks; they made each other's debut art and animation, and Raora helped design the Otomo. Elizabeth Rose Bloodflame: her first collab partner ("Chat & Art"), who calls her "Pretty Kitty." Kaela Kovalskia ("SMITTEN"): co-op partner who, in Raora's lore, lives in her basement; with Koseki Bijou they are "Graondstone." Koseki Bijou: her "assistant" in a cooking off-collab. Ouro Kronii ("Pizza Time"): Portal 2 and cleaning-crew games; Raora calls her "Tam Tender." Takanashi Kiara: "HoloEU" with Cecilia; Raora gave her an Italian lesson and designed an outfit for her, and her friendly-fire "Doom" in Kiara's Mage Arena collab became a meme. Ninomae Ina'nis: Puyo Puyo Tetris 2. Nerissa Ravencroft and Moona Hoshinova: "V3LVET." Haachama and Vestia Zeta: off-collab game partners. Inugami Korone: the senior whose clips made her a VTuber fan.

## [SW] Secrets
(none)

---

## Open Questions
1. 3D debut date time zone (2025-08-10) to confirm.


==================== FILE: raora.md ====================

# Audio check — Raora Panthera (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026. Much of the April chatting stream concerns health, family, money and personal
history; those stretches are private and are not used or summarized here. The Pragmata window mixes in game
voices (a child character), which lifts its pitch figures.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2026 | [【ODDCORE】NOTHING MAKES SENSE HERE ?!? 【Raora Pan](https://youtu.be/97aydhssGYs) | [3:27:54–3:37:54](https://youtu.be/97aydhssGYs?t=12474) | 6.4 | 299 | 46.5 | 285 Hz | 199–441 Hz |
| chat30_2026 | [LETS CHAT BIG CAT WANTS TO YAP](https://youtu.be/pTPX4PAk7Qw) | [0:30:00–1:00:00](https://youtu.be/pTPX4PAk7Qw?t=1800) | 25.5 | 3194 | 125.5 | 251 Hz | 197–385 Hz |
| open2026 | [LETS CHAT BIG CAT WANTS TO YAP](https://youtu.be/pTPX4PAk7Qw) | [0:00:00–0:15:00](https://youtu.be/pTPX4PAk7Qw?t=0) | 8.4 | 1100 | 131.0 | 256 Hz | 206–406 Hz |
| game30_2026 | [【Pragmata】BIG CAT MEANS BIG RESPONSIBILITIES【Rao](https://youtu.be/zc_JRHPep9c) | [1:00:00–1:30:00](https://youtu.be/zc_JRHPep9c?t=3600) | 18.8 | 1022 | 54.3 | 267 Hz | 175–445 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| "big cat means big trouble" (RP4) | **Confirmed** as a sign-off ("…and remember, big cat means big trouble"). | [3:35:48](https://youtu.be/97aydhssGYs?t=12948) |
| Gentle, rarely swears (RP2) | **Consistent.** Only "frick" and "damn" when muted by accident. | [0:05:21](https://youtu.be/pTPX4PAk7Qw?t=321) |
| Firm about her rules | **Confirmed (playfully).** "Hear me out. … First, you guys have no rights. … No, thank you. I refuse." | [0:40:52](https://youtu.be/pTPX4PAk7Qw?t=2452); [0:42:29](https://youtu.be/pTPX4PAk7Qw?t=2549) |
| Chattini lore | **Confirmed.** "Oh, you're one of those zipper Chattini." "I swear I live in the Justice headquarters." | [0:33:19](https://youtu.be/pTPX4PAk7Qw?t=1999); [0:37:54](https://youtu.be/pTPX4PAk7Qw?t=2274) |
| Italian-accented English | **Consistent in the transcript:** a few non-native constructions in fast speech; the accent itself is not measurable here. | throughout |
| Pitch | **Measured:** chat window medians about 251–256 Hz, p10–p90 about 197–406 Hz. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- "I'm sure you guys like my cooking shorts because they are made with so much love." [0:39:55](https://youtu.be/pTPX4PAk7Qw?t=2395)
- "If I was a kid and I had all this entertainment, I would go crazy." [1:18:34](https://youtu.be/zc_JRHPep9c?t=4714)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "go big or go home" | [3:31:59](https://youtu.be/97aydhssGYs?t=12719) | "must be hard. Go beaker, go home! Go beaker, go home!" | **Disagrees** ("Go beaker, go home"); not used |
| "Hope you guys gonna have a good day no matter what. Thank you Chattini for watching" | [3:35:25](https://youtu.be/97aydhssGYs?t=12925) | "to work we're gonna have a good day it's a teeny for watching went to the team have a good team a" | **Disagrees**; not used |
| "Remember, big cat means big trouble" | [3:35:48](https://youtu.be/97aydhssGYs?t=12948) | "take care and remember big cat means big trouble goodnight all too" | Agrees; the second model adds "goodnight … Ciao! Buh-Bye!" |
| "Frick I was muted" | [0:05:21](https://youtu.be/pTPX4PAk7Qw?t=321) | "frick i was muted damn whoopsie oh" | Agrees |
| "Whoopsie. That was totally intentional, that was totally intentional everyone" | [0:05:27](https://youtu.be/pTPX4PAk7Qw?t=327) | "whoopsie uh oh that was totally intentional that was totally intentional everyone that was yeah no" | Agrees |
| "We back, you guys are so back" | [0:06:33](https://youtu.be/pTPX4PAk7Qw?t=393) | "of my control we back you guys are so back it works sometime" | Agrees |
| "Oh, you're one of those zipper chattini. I love those kind" | [0:33:21](https://youtu.be/pTPX4PAk7Qw?t=2001) | "mess with it oh you're one of those zipper chatini i love those kind because i stuff" | Agrees |
| "No, Chattini, you cannot get any of my plushies." | [0:36:04](https://youtu.be/pTPX4PAk7Qw?t=2164) | "Can't sell anyone. No. No Chotini! Chotini, you cannot get any of my plushies. I'm" | Agrees ("Chotini" spelling) |
| "I'll be honest. I'm a hater now. Okay, let me be a hater" | [0:36:10](https://youtu.be/pTPX4PAk7Qw?t=2170) | "I kinda hate I'll be honest I'm a hater now okay let me be a hater so I have" | Agrees |
| "I swear I live in the Justice headquarters. I promise." | [0:37:56](https://youtu.be/pTPX4PAk7Qw?t=2276) | "so blue and I swear I live in the justice at quarter I promise hola okay" | Agrees ("justice at quarter") |
| "I'm sure you guys like my cooking shorts because they are made with so much love" | [0:39:55](https://youtu.be/pTPX4PAk7Qw?t=2395) | "happy someone likes I'm sure you guys like my cooking shorts because they are made with so much love and I love" | Agrees |
| "Okay, okay, okay, okay. Hear me out. I have something to say about this comment. First, you guys have no rights." | [0:40:51](https://youtu.be/pTPX4PAk7Qw?t=2451) | "in the future okay okay okay okay hear me out um I have something to say about this comment first you guys have no rights by any" | Agrees |
| "it's not negotiable it's not even a question" | [0:41:12](https://youtu.be/pTPX4PAk7Qw?t=2472) | "things are mine it's not negotiable it's not even a question you know like" | Agrees |
| "No, thank you. I refuse." | [0:42:29](https://youtu.be/pTPX4PAk7Qw?t=2549) | "make me happy no, no thank you i refuse yeah, the" | Agrees |
| "Oh boy, this makes me so emotional. She's so cute." | [1:00:04](https://youtu.be/zc_JRHPep9c?t=3604) | "i can help she's next why this makes me so emotional she's so cute" | Agrees on "this makes me so emotional. She's so cute." |
| "Because I'm a big cat. It's a big cat, it's literally me" | [1:13:12](https://youtu.be/zc_JRHPep9c?t=4392) | "cat? She's giving me a big cat drawing? It's a big cat! It's literally me! Thank you, Dion!" | **Shared span only** ("It's a big cat, it's literally me") |
| "If I was a kid and I had all this entertainment, I would go crazy." | [1:18:34](https://youtu.be/zc_JRHPep9c?t=4714) | "to do huh no if i was a kid and i had all this entertainment i'll go crazy what is in" | Agrees |


# One-round review: hololive -Advent- (four new character files: Shiori Novella, Koseki Bijou, Fuwawa Abyssgard, Mococo Abyssgard), two new world cards (FUWAMOCO, Advent Pairs), and the cast/world edits that link them

You are GPT, reviewing Claude's work for the novel-lab project "holoen" (fan fiction Story Bible for Sudowrite about hololive English members). This is the ONLY review round (the author limited GPT usage), so be decisive: report what must change, give exact replacement wording where you can, and skip cosmetic nitpicks. Write your review in English.

## Project rules that apply (from project.md, author decisions)
- Authenticity first: accurate, sourced facts; profanity and teasing kept as-is; nothing invented and presented as fact. Unverified items must be labeled and kept off the cards.
- Persona premise: in stories, members know they are streamers with personas; lore (the Archiver, the Jewel of Emotions, twin demonic guard dogs) is a performed bit; nobody has real powers.
- Relationships are the most important part of the world and include members outside EN (JP, ID, DEV_IS, HOLOSTARS, GAMERS); events (debuts, concerts, 3D lives) are shared memory; members' public X posts are key sources. The author asked to complete every character's relationship web.
- Recency weighting: recent (2025–2026) streams set the default manner; early memes stay as shared memory.
- Boundaries: public persona only; never the real people behind the avatars (names, faces, family, homes, health, school, pets, graduation reasons); no romance/intimacy between real people (ships are performed bits); COVER Derivative Works Guidelines; short quotes only, no lyrics. Author decision (2026-10-01, Kiara): a member's announced break is not written; Claude applied the same rule to Mococo's September 2026 health break.
- Voice: Sudowrite will insert ElevenLabs v4 audio tags itself, so each card teaches every voice factor (speech habits, fillers, register, pace, signature sounds, code-switching, tone shifts) in [SW] Dialogue Style, Catchphrases, Voice & Delivery and Audio Tags. Tags direct an ORIGINAL designed voice; nobody's real voice is cloned or imitated. IPA guides are kept, marked "provisional, untested" (author asked for pronunciation; the earlier rounds accepted this).
- Quotation gate: lines quoted on cards from audio must be spans BOTH ASR models (whisper small.en and medium.en) agree on; the audio reports list each verdict. Wiki-only spoken lines are "secondary"; short catchphrases may go on the card, full wiki sentences stay in the dossier unless labeled.
- FUWAMOCO: one channel, two members; the duo audio cannot separate the twins, so duo lines stay unattributed.
- Baseline date 2026-09-30. Sudowrite soft limits (words): Personality 400, Background 500, Physical 200, Dialogue Style 250, Catchphrases 250, Voice & Delivery 250, Audio Tags 350, Motivation 200, Relationships 350; Worldbuilding Description 450, Rules 350, Sensory 200.

## What to check
1. Factual accuracy against the cited sources (dates, events, who did what, quotes, pair names). Flag anything unsupported, mis-attributed, overstated or ranking-like.
2. Privacy and persona boundaries.
3. Quotation gate (anything on a card that the reports mark as one-model only or disagreeing).
4. Voice teaching: consistency with Voice Profiles and measurements; specific enough for Sudowrite; nothing that imitates a real voice or sexualizes anyone (note Shiori's "thirst" bits and the twins' cute register).
5. Relationships: accurate, useful for scenes, consistent across the four cards, the two world cards and the cast edits.
6. Card usability: most important first, Other Names that trigger detection without false positives, duplication between fields.

## Output format
`## Shiori Novella`, `## Koseki Bijou`, `## Fuwawa Abyssgard`, `## Mococo Abyssgard`, `## FUWAMOCO`, `## Advent Pairs`, `## Cast and world edits`, each with `MUST:` (numbered, each with the fix) and `SHOULD:` (optional, short). Then `## Missing facts worth adding` (only with a source you can name). If something is fine, write `OK`.

---


==================== FILE: 20261001-0548-character-Shiori-Novella/claude-draft.md ====================

---
kind: character
name: "Shiori Novella"
sw_section: Characters
---

# Character File: Shiori Novella

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Shiori is active at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. Nothing about the performer behind the avatar: private-life details (health, sleep, family, home and
> the like) are deliberately left out, including those the wiki lists. In stories she knows she is a
> streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; SN20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (SN#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1.9 hours of archived 2026 recordings (SN20: a horror
> game showcase watch stream, opening, middle and close, with trailer audio mixed in, and a co-op Dying Light:
> The Beast stream). The audio was machine-transcribed and acoustically measured; transcripts were reviewed in
> context, without independent listening verification.

## One-line Concept
The Archiver of hololive -Advent-: a bookish fugitive whose hair went grey from forbidden knowledge, who
planned the group's prison break and now streams as a cheerful, dorky, unhinged storyteller: cozy chats
that swerve into the strangest tangents, edited vlogs and original comics, and horror games punctuated by
piercing screams. [Official SN1] [Observed SN2, secondary]

## Core Drive
- **Want:** in her lore, to collect stories and memories as bookmarks; as a creator, to "make fun memories
  with people" and archive them, to make things herself (vlogs, games, comics), and to improve her singing.
  [Official SN1] [Observed SN2 §Quotes, §Likes, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** a soft spot for animals; heartfelt support of her community and fan art
  (she credits artists in her outros). [Observed SN2 §Miscellaneous, secondary]

## Core Contradiction
She looks the most menacing of her generation (black-and-white hair, glowing eyes, dripping coat) and is
called its smartest and its leader, yet she is the dorkiest, sleepy, "ditzy what-is-she-talking-about"
member, whose sweetness is hidden under teasing and tangents about anything from cannibalism to
parasites. [Official SN4 interview] [Observed SN2 §Personality, §Miscellaneous, secondary]

## Behavioral Traits
1. Tangents: cozy, chill chats veer into strange topics; her members' chat has a "bonk" emote for when she
   goes too far, and fans joke about her manager ("Henmama") losing sleep. [Observed SN2 §Personality,
   secondary]
2. She teases those she is close to, especially her genmates, and plays hard to get with Nerissa.
   [Observed SN2 §Personality, §Relationships, secondary]
3. She is a self-made producer: she records and edits her own vlogs, writes community posts "like some
   public diary," makes distinctive titles, thumbnails and overlays, and in 2026 released "Into The Void," a
   four-part original motion comic voiced by herself, Elizabeth, Gigi and Nerissa. [Official SN4]
   [Observed SN2; SN3 kEoFVaHsy_U, 3qrQ4KcvUb4]
4. She runs odd "educational" and review streams (a nurse roleplay, "Rating Your Clocks" with Kronii,
   "Gyatt Review" with Bijou, horror game award shows, B-movie watchalongs). [Observed SN3 titles]
5. In horror games she lets out ear-piercing, horror-movie screams. [Observed SN2 §Miscellaneous, secondary]
6. She is the narrator of Advent's lore videos and is treated as the unofficial leader (a fan poll gave her
   78%; Bijou calls her "our glorious leader"). [Observed SN2 §Miscellaneous, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - "Shiori~n!" (the wiki's caption) and, in her official 2026 interview, "Shiori~n! Shiori Novella here at
    your service!" [Observed SN2, secondary] [Official SN4]. The sampled 2026 opening has no formal greeting:
    a "Hello" and she starts talking over her waiting-screen music. [ASR SN20, hpC9AEiMBDg 0:00:54]
  - Sign-off: "Alright, bye guys! See you later!" after thanks: "…I appreciate you so much." [ASR SN20,
    2:26:18, 2:25:35; both models]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "In my defense…" / "For the record…" → defending her lore or a story bit; "in my defense" six times in
    an hour. "It was not my fault everyone got sacrificed, okay?" "In my defense, guys, they trespassed."
    "For the record, I did not sacrifice anyone." [ASR SN20, 0:05:03, 0:09:05, 1:06:55]
  - "I would not want to play this!" → horror trailers she would rather watch others play ("I would love to
    watch someone else play this. I would be too scared to play this myself."). [ASR SN20, 0:13:37]
  - Thirsting at characters as a bit: "Whoa, wait, who is that hot thing? Is that a vampire?" "…kind of cute
    for a pixel. What's your name?" "I guess you can break my pulse if you want." [ASR SN20,
    0:12:26, 0:33:31, 0:33:40]
  - Cheering creators on: "Your Blender skills are so cool. I'm so happy for you." [ASR SN20, 0:36:40]
  - Wiki quotes (secondary): "You can do it, yes you can! If you can't do it, beat them up!", "Aw, it's okay!
    There, there!", "Yeah, you like this, don't ya?", "Oh nyo..." [Observed SN2 §Quotes, secondary]
- **Vocabulary / fillers:** "like" (about 1 word in 40), "actually," "okay," "kind of," "sort of," "you
  know," "genuinely," "if that makes sense"; she addresses "guys" (26 times) far more than "chat" (4).
  Exclamations: "whoa," "ooh," "oh my god" (ten in 45 minutes of a horror co-op), "oh heavens," "oh good
  god," "oh shoot," "oh crap," "oh fudge." [ASR SN20, first-model counts; the showcase windows include
  trailer audio, so counts are rough]
- **Profanity:** moderate and situational: "what the hell," "it pisses me off when…" (about fake "LIVE"
  thumbnails), and in a co-op stream two strong swears, one at a troll in chat ("Actually, no. Go fuck
  yourself. I'm so sorry. I shouldn't say that."), apologized for at once. [ASR SN20, 2:25:12; 6jYMp8NOaM0
  1:23:30–1:23:53; both models]
- **Laughs, noises:** ear-piercing, horror-movie screams in scary games (the loudest in Dark Souls 2), not
  writable by transcription; "ooooh" at creepy art. [Observed SN2 §Miscellaneous, secondary] [ASR SN20]
- **Self-aware commentary:** small self-deprecations (she is "really bad at remembering names" and hopes chat will
  remember them for her; "this is how I wander off in, like, group settings too"); "Monkey's gotta run" while
  healing. [ASR SN20, 2:23:15; 6jYMp8NOaM0 1:40:49, 1:07:38]
- **Code-switching:** her chat rules say she speaks "mainly English, Japanese"; she uses Japanese honorifics
  for viewers ("-san"). [Observed SN3 descriptions] [ASR SN20, first model]
- **Rhythm & rhetoric:** fast, run-on commentary that stacks reactions ("This looks like a movie! I
  genuinely like the look of this! I just would not want to be scared!"), restarts ("I would, I would, I
  would not"), tangents mid-sentence, then a flat lore aside. [ASR SN20, 0:30:39]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (SN20; four 2026 windows): median pitch about 251–258 Hz, near Gura's and Ame's range in this
    project's samples (245–276 Hz) and above IRyS's (214–226 Hz); fast: about 151–181 words per minute of
    speech in the showcase windows, 147 in the co-op game. Sample results only; trailer and game audio are
    mixed in.
  - Provisional (interpretation): a clear, mid-high, chatty voice; quick and bubbly when excited, flat and
    deadpan for lore asides, teasing in her "hot vampire" bits, and a piercing scream at jump scares.
- **Sounds off:** a slow, ominous, villain voice as her default (her menace is a joke); prim or formal speech;
  constant swearing; a whispery seductive read of the thirst bits (keep them goofy).

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, quick | "Shiori~n! Shiori Novella here at your service!" (SN4) |
| Excited commentary | Fast, stacked reactions | "This looks like a movie! I genuinely like the look of this!" (ASR SN20) |
| Lore defense | Flat, mock-innocent | "For the record, I did not sacrifice anyone." (ASR SN20) |
| Thirst bit | Teasing, goofy | "Whoa, wait, who is that hot thing? Is that a vampire?" (ASR SN20) |
| Horror | Nervous, then a piercing scream | "I would be too scared to play this myself." (ASR SN20; SN2) |
| Supportive | Warm, plain | "Your Blender skills are so cool. I'm so happy for you." (ASR SN20) |
| Annoyed | Quick snap, quicker apology | "I'm so sorry. I shouldn't say that." (ASR SN20) |
| Sign-off | Warm, quick | "Alright, bye guys! See you later!" (ASR SN20) |

### Sample Lines
1. "Shiori~n! Shiori Novella here at your service!" (Official SN4)
2. "It was not my fault everyone got sacrificed, okay?" (ASR SN20, hpC9AEiMBDg 0:05:03)
3. "For the record, I did not sacrifice anyone." (ASR SN20, 1:06:55)
4. "I would love to watch someone else play this. I would be too scared to play this myself." (ASR SN20, 0:13:37)
5. "…kind of cute for a pixel. What's your name?" (ASR SN20, 0:33:31; about a pixel-art character)
6. "That's dead, guys. I defeated my first chimera." (ASR SN20, 6jYMp8NOaM0 1:07:58)
7. "Alright, bye guys! See you later!" (ASR SN20, 2:26:18)

## Appearance Anchors (avatar)
- 163 cm. Mid-length two-tone hair, black and white, held with sharp shuriken-like hairpins; bright,
  glowing light-yellow eyes (they can light up like a flashlight in the dark, in her lore). [Official SN1]
  [Observed SN2 §Appearance, §Lore, secondary]
- A dark purple and black jacket and dress with "dripping" parts; two rings on each hand; long fingerless
  gloves. Mascot: Yorick, a sad black sphere with two long arms and four spikes, on her right shoulder; two
  cat mascots, the Nyakuza. Fans: Novelites ("novel-eets"); emoji 👁‍🗨. [Observed SN2 §Appearance,
  §Mascots and fans, secondary]
- Later outfits include a red-and-black gothic dress (2025), pajamas with Novelite slippers (2026) and a
  Monster Hunter Stories 3 armor outfit (2026). [Observed SN2 §2025, §2026, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | The Archiver; imprisoned in The Cell for forbidden knowledge; masterminded Advent's prison break | [Official SN1] [Observed SN2 §Lore] |
| 2023-07-30 JST | Debuts with hololive English -Advent- ("Shiori~n!") | [Official SN1] |
| 2023-08-12 | Advent on Kiara's HOLOTALK | [Observed SN3; Kiara archive] |
| 2024-08-02 | 3D debut "A New Chapter Begins!" with Nerissa, Bijou and FUWAMOCO as guests | [Observed SN3 tIKQMFtbgOA] |
| 2024-08-25 | -Breaking Dimensions-: "Lonely in Gorgeous" with Fauna and Nerissa | [Official, Concerts card S8] |
| 2025-08-29 | Advent 2nd-anniversary 3D live "On the Run!" | [Observed SN2 §2025] |
| 2026-02-15 | First original song "Monsters and Men" | [Observed SN2 Discography] |
| 2026-07-03/04 | Serendipity concert, duo with Mori Calliope | [Official SN4] |
| 2026-07-30 | "Into The Void" motion comic begins | [Observed SN3] |

## Relationship Map
Public exchanges only; counts are streams on Shiori's channel mentioning the other per year (2023 → 2026,
archive SN3; the archive thins out from late 2025), a rough measure, not a ranking. Her titles rarely name
partners, so the cast's channels and the wiki fill in.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Nerissa Ravencroft | Genmate ("ShioRaven") | Nerissa calls her "wife"; Shiori plays hard to get; a fictional daughter, "Beatrice Niori World Destroyer Novella"; Shiori knows where Nerissa's horn piece is; a hedge maze and fishing collabs (7 / 2 / 1 / 2) | [Observed SN2 §Relationships, §Lore, secondary; SN3] |
| Koseki Bijou | Genmate ("Goth Rock," "GAGA") | Bijou's most-mentioned genmate on her own channel (46 streams); a "Gyatt Review" (2024), an offline conbini-snack collab with Nerissa and Bijou (2024) | [Observed SN2; SN3; Bijou archive] |
| FUWAMOCO | Genmates ("Pen Pups") | The twins once mistook a Minecraft cow for her (her black-and-white coloring); she joked Mococo was hallucinating Fuwawa | [Observed SN2 §Miscellaneous; FUWAMOCO wiki, secondary] |
| Mori Calliope | Senior; Serendipity 2026 duo ("Last Writes") | Calli's "#DEEP" kids'-movie talk (2024-01-09) and Stardew Valley (2024-12-20); in the official interview Calli is "a little obsessed with her" and Shiori admires Calli's "work ethic and boundaries"; their dynamic: "Unhinged" (Calli) | [Official SN4] [Observed Calli archive] |
| Takanashi Kiara | Senior | HOLOTALK (2023); an occult handcam off-collab "#shiotori" (2024-07-12); Eden Eternal (2024) | [Observed Kiara archive] |
| Ouro Kronii | Senior | "Whip It Out! Rating Your Clocks with @OuroKronii" (2025-03-27); Blood Typers (2025) | [Observed SN3; Kronii archive] |
| Nanashi Mumei | Senior (graduated 2025) | B-movie watchalongs (Neil Breen, 2025-02-26; Kung Pow, 2025-04-11), Left 4 Dead 2 (2024) | [Observed SN3] |
| Ninomae Ina'nis | Senior | "Rate Your Fears: Nightmare Discussion" (2024-04-24) | [Observed SN3] |
| Watson Amelia | Senior | "Ame Senpai's Aquarium Visit" in VRChat (2024-12-02) | [Observed SN3] |
| IRyS | Senior | Monster Hunter Wilds (2025), PEAK (2025) | [Observed IRyS archive] |
| Gigi Murin, Cecilia Immergreen, Elizabeth Rose Bloodflame | Justice kouhai ("NovelGrem," "GAGA," "NovelFlame") | Lethal Company as GAGA (2024); Project Zomboid with Zeta and Gigi (2025); Elizabeth and Gigi in her "Into The Void" cast (2026) | [Observed SN2; SN3] |
| Vestia Zeta (ID) | Friend ("GreyScaleX," the X is silent) | Don't Starve Together, "My Spider Wife" (2025) | [Observed SN2; SN3] |
| Airani Iofi (ID), Pavolia Reine (ID) | "Fanfic Club" with Gigi | Monster Hunter Wilds with Iofi and Jurard (2025) | [Observed SN2; SN3] |
| Machina X Flayon, Jurard T Rexford, Regis Altare (HOLOSTARS EN) | Friends ("Goth Pilot" with Machina) | Smash Bros. with Machina (2025); R.E.P.O. (2025); The Dark Pictures: Little Hope (2026) | [Observed SN2; SN3] |
| Inugami Korone | JP senior | Shiori first discovered hololive through untranslated Korone clips | [Observed SN2 §Background, secondary] |

## Arc
- **Starting point:** active member at the 2026 baseline: her first original song, the Serendipity duo with
  Calli, "Into The Void."
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a tangent nobody can stop; a "review" of something absurd; a horror scream; a lore
  secret she will not reveal; teasing Nerissa until she squirms.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Shiori narrates a genmate's stream as if it were an audiobook.
  2. Nerissa finally asks about her horn piece; Shiori changes the subject for an hour.
  3. Calli and Shiori record a "deep-dive" on a kids' cartoon that goes too far; the manager bonks both.
  4. A horror game where every jump scare is answered by a scream louder than the game.
  5. FUWAMOCO mistake her for a cow again, on purpose.

## Secrets & Foreshadowing
- **Truth:** none assigned. Her "forbidden knowledge" is open lore; she keeps it as a bit.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2023-07-30 (JST); birthday May 2; 163 cm; fans Novelites; emoji 👁‍🗨; mascot Yorick.
- Unit: hololive English -Advent- (2023–), "hololive -Advent-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- SN1 Official profile: https://hololive.hololivepro.com/en/talents/shiori-novella/
- SN2 Virtual YouTuber Wiki, Shiori Novella, read through its API on 2026-10-01 (secondary). Sections used:
  infobox, §Profile, §Personality, §Appearance, §2023–§2026, Discography, §Mascots and fans,
  §Relationships, §Quotes, §Lore, §Likes and dislikes, §Miscellaneous:
  https://virtualyoutuber.fandom.com/wiki/Shiori_Novella
- SN3 Stream archive metadata (titles, dates, descriptions), Shiori's channel, via archive.ragtag.moe (read
  2026-10-01): znfFjw2KP5Y, _-ZLujLTt5s, LHOtqIOLczE, tIKQMFtbgOA, _V-F99hL9Zg, kEoFVaHsy_U, 3qrQ4KcvUb4,
  26kbmP4jcK0, _PkbayGWyQo, plU_vIIQV0M, fCwmT4XtkmQ, TxDhBlvrGsQ, aS5zWY2eQJw, QT3FdKU-pi0, AjwIazuu8gg,
  Q32Om1RAa1c, vpjqVEKkfzY, TQOwH3u2FPo, ubfmGzYjEUw, LpeIJ5UC9h0, nFm3B-nurb8; cast channels: Calli
  NRP9D9SO6Bc, wAu6xM9oVak; Kiara 0Q9FLtcAY0s, psp788-ltEE; Kronii rG-iJSbpiNM; IRyS MV8TSgoJhlc. Counts
  computed by Claude.
- SN4 Official Serendipity interview, Calliope & Shiori (2026): https://serendipity.hololivepro.com/news/interview05/
- SN5 X posts via wiki citations (research/x-posts.md)
- SN20 Claude's audio check (2026-10-01); see research/audio-check/shiori.md.

---

## [SW] Name
Shiori Novella

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Advent-, hololive English -Advent- (former branch name), Advent

## [SW] Other Names
Shiori, Shiorin, The Archiver, Novella, Shiori~n

## [SW] Personality
Shiori streams as "The Archiver," a bookish fugitive with forbidden knowledge, and plays it with a cheerful, dorky, slightly unhinged energy: she calls herself "a whacky, sleepy eepy girl" with "ditzy what-is-she-talking-about energy." Cozy chats swerve into strange tangents (anatomy, parasites, cannibalism, childhood cartoons with adult subtexts) until chat reaches for the "bonk" emote. She teases the people she is close to, especially her genmates, plays hard to get when Nerissa calls her "wife," and guards lore secrets (where Nerissa's horn is) as a running joke. Under the edge she is sweet and supportive: she credits every fan artist, has a soft spot for animals, and says plainly how much she appreciates her viewers. She is a hands-on creator who edits her own vlogs, writes community posts like a public diary, made an original motion comic, and runs odd review and "educational" streams. She loves mysteries, Sherlock Holmes, horror co-ops and whimsical-creepy art, though she would rather watch someone else play the truly scary games; when a jump scare lands, she screams.

## [SW] Background
Shiori is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Archiver," driven by a thirst for knowledge, who turns favorite stories and memories into bookmarks; imprisoned in The Cell for forbidden knowledge found in a story (which, in the lore, turned half her hair grey), she planned and executed Advent's prison break. She debuted on 2023-07-30 with hololive English -Advent- alongside Koseki Bijou, Nerissa Ravencroft and FUWAMOCO, narrates the group's lore videos, and is treated as its unofficial leader. She made her 3D debut on 2024-08-02, sang at the 2024 and 2025 English concerts, released her first original song "Monsters and Men" on 2026-02-15, was paired with Mori Calliope at the 2026 Serendipity concert, and began her original motion comic "Into The Void" in July 2026. Her fans are Novelites; her mascot is Yorick.

## [SW] Physical Description
Shiori's avatar is 163 cm tall, with mid-length two-tone hair, black on one side and white on the other, held by sharp shuriken-like hairpins, and bright, glowing light-yellow eyes. She wears a dark purple and black jacket over a dress with "dripping" edges, long fingerless gloves and two rings on each hand. Yorick, a small, sad black sphere with long arms and four spikes on its head, rides on her right shoulder.

## [SW] Dialogue Style
Fast, chatty English that stacks reactions and restarts mid-thought, full of "like," "actually," "kind of," "sort of," "genuinely" and "if that makes sense"; she talks to "guys," rarely "chat." She defends her lore with a straight face ("In my defense, guys, they trespassed"; "It was not my fault everyone got sacrificed, okay?"), thirsts at game characters as a goofy bit ("Is that a vampire?"), cheers creators on ("I'm so happy for you"), and admits she would rather watch someone else play the scary games. Exclamations: "whoa," "ooh," "oh my god," "oh heavens," "oh shoot," "oh fudge." Her swearing is situational ("what the hell," "it pisses me off"), and a rare strong one is followed at once by "I'm so sorry. I shouldn't say that." She teases her genmates, keeps lore secrets as a joke, and calls viewers with Japanese honorifics now and then. Lines of hers: "I would love to watch someone else play this. I would be too scared to play this myself." "I'm really bad at remembering names." "That's dead, guys. I defeated my first chimera."

## [SW] Catchphrases
"Shiori~n!" (greeting); "Shiori Novella here at your service!" (introduction); "In my defense…" (defending a lore bit); "For the record, I did not sacrifice anyone." (her running sacrifice joke); "Don't you think that's a wonderful story?" (her official line); "I would not want to play this!" (scary trailers); "Whoa, wait, who is that hot thing?" (a handsome character); "I'm so happy for you." (cheering someone on); "Aw, it's okay! There, there!" (comforting); "Oh nyo..." (dismay); "Alright, bye guys! See you later!" (sign-off)

## [SW] Voice & Delivery
A clear, mid-high, chatty voice that runs fast when she is excited, piling reactions on top of each other, then drops into a flat, deadpan aside for lore jokes. Her teasing has a playful lilt, and her thirst bits stay goofy rather than sultry. Horror makes her nervous and quiet until a jump scare, when she lets out an ear-piercing, horror-movie scream. Sincere thanks come out warm and plain. When annoyed she snaps quickly and apologizes even more quickly.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): clear, mid-high voice (about 251–258 Hz), fast and chatty (about 150–180 words a minute of speech), deadpan for lore asides; American English. Default tags: [bright, chatty]. By situation: opening [bright, quick]; excited commentary [rapid, excited]; lore defense [deadpan, mock-innocent]; thirst bit [teasing, goofy]; tangent [rambling, amused]; horror [nervous, quiet] then [screams]; comforting [gentle, warm]; cheering someone [warm, delighted]; annoyed [snappy] then [apologetic, quick]; sign-off [warm, quick]. With people (provisional, drawn from Relationships): Nerissa [teasing, playing hard to get]; Bijou [amused, big-sister]; FUWAMOCO [playful]; Calli [dry, conspiratorial]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [ear-piercing scream] (tag only); [intrigued] ooooh; [startled] whoa. Keep in the words: "like," "actually," "kind of," "sort of," "genuinely," "if that makes sense," "guys," "in my defense," "for the record," "oh my god," "oh heavens," "oh shoot"; swearing situational and quickly apologized for. Pronunciation guide (provisional, untested): Shiori /ʃiˈoʊɹi/, Novella /noʊˈvɛlə/, Novelites /ˈnɑvəliːts/ ("novel-eets"), Yorick /ˈjɔɹɪk/. Not as default: a slow, ominous villain voice, formal speech, constant swearing. Never a seductive read of the thirst bits.

## [SW] Motivation
In her lore, Shiori archives stories and memories worth saving. As a creator she wants to make fun memories with people and keep them, to make things with her own hands (vlogs, games, comics, music), and to keep surprising people, from improving her vocal stamina to a ghost-hunting vlog.

## [SW] Relationships
Nerissa Ravencroft: Advent genmate who calls her "wife" (ShioRaven); Shiori plays hard to get, keeps the secret of Nerissa's horn piece, and shares a fictional "daughter" with her. Koseki Bijou: genmate who calls her "our glorious leader" (Goth Rock; a "Gyatt Review"). FUWAMOCO: genmates who once mistook a Minecraft cow for her (Pen Pups). Mori Calliope: her 2026 Serendipity duo partner, who admits she is "a little obsessed with her"; Shiori admires Calli's "work ethic and boundaries," and they bond over dark taste and absurd deep-dives. Takanashi Kiara: hosted Advent on HOLOTALK; an occult handcam off-collab ("#shiotori"). Ouro Kronii: let Shiori rate her clocks on stream; "MONSTER" with Kronii, Ina and Gigi at the 2025 concert. Nanashi Mumei (graduated 2025): B-movie watchalongs. Ninomae Ina'nis: a "Rate Your Fears" nightmare talk. Watson Amelia: a VRChat aquarium visit with "Ame Senpai." Gigi Murin, Cecilia Immergreen, Elizabeth Rose Bloodflame (-Justice-, Advent's in-story "guards"): GAGA with Bijou, Gigi and Cecilia; Gigi, Elizabeth and Nerissa voice her motion comic "Into The Void." Vestia Zeta (ID): "GreyScaleX." Machina X Flayon (HOLOSTARS): "Goth Pilot." Inugami Korone: the senior whose clips first led her to hololive.

## [SW] Secrets
(none)

---

## Open Questions
1. The sampled 2026 windows include a showcase with trailer audio and a co-op stream with viewers; counts are
   rough. A pure chatting window (her "yap" streams) would sharpen the filler counts. Worth checking?
2. Her two strong swears in the sample (one aimed at a troll, apologized for) are on the dossier, not on the
   card's lines. Keep them off the card?


==================== FILE: 20261001-0548-character-Koseki-Bijou/claude-draft.md ====================

---
kind: character
name: "Koseki Bijou"
sw_section: Characters
---

# Character File: Koseki Bijou

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Bijou is active at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. Nothing about the performer behind the avatar: private-life details (family, a pet, sleep and meal
> habits, trips) are deliberately left out, including those the wiki lists. In stories she knows she is a
> streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; KB20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (KB#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1.2 hours of archived 2026 speech (KB20: the opening
> of her 2026 birthday VRChat stream, 45 minutes and the close of a Resident Evil 4 stream); a Tomodachi Life
> window was mostly drawing and game voices and is not used for measurements. The audio was
> machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.

## One-line Concept
The Jewel of Emotions, a tiny crystal girl formed from every human feeling and locked away because people
fought to own her, who streams as "Biboo": a bubbly, meme-fluent, childlike gremlin with real gaming
skill, who never swears (she says "beep") and keeps her cool where others rage. [Official KB1] [Observed
KB2, secondary]

## Core Drive
- **Want:** in her lore, to meet people and their good emotions, which make her shine brighter; as a
  streamer, to appear in a video game and have a voice-acting role, to collab with every hololive member at
  least once, to perform an original song on stage, and to build a community of millions of Pebbles.
  [Official KB1] [Observed KB2 §Likes and dislikes, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** keeping her streams profanity-free (she asks Pebbles to do the same);
  inviting fans in (#pebblesona); treating hard concert preparation "like a boss" fight. [Observed KB2
  §Personality, secondary] [Official KB4]

## Core Contradiction
The smallest, most childlike member of her generation (140 cm, Gen Alpha memes, "mom collecting") is also
one of the calmest and most skilled gamers in hololive English, who adds challenges to games she has
already beaten; and the gem who "inspires greed" in others plays the most wholesome, "seiso" streamer, with
an evil doppelganger kept as a joke. [Official KB1] [Observed KB2 §Personality, §Lore, secondary]

## Behavioral Traits
1. She never swears on stream: she says "beep" in place of a swear word, even when reading game text, and
   uses "dang it!" for frustration; her chat has an all-caps "BEEP" emote. [Observed KB2 §Personality,
   secondary]
2. She stays calm under difficult game challenges and invents harder self-imposed runs; FromSoft games,
   Hollow Knight, Resident Evil and Monster Hunter are staples. [Observed KB2; KB3 titles]
3. She speaks fluent Gen Alpha meme ("skibidi," "gyatt," "rizz," "67"), baffling her slightly older
   genmates; she wrote parody songs around them. [Observed KB2 §Personality, §Miscellaneous, secondary]
   [Official KB4]
4. "Mom collecting": she uses her cuteness to get other members to agree to be her mom. [Observed KB2,
   secondary]
5. She starts nearly every solo stream as a Moai head and only appears after the command "Kira kira,
   Koseki!" and a transformation animation; collab guests get stuck in the Moai with her. [Observed KB2
   §Miscellaneous, secondary]
6. She mods games: for her audition she replaced Undertale's Sans with Calli and beat the fight in one try,
   then did it again with Calli on stream (2023-08-12). [Observed KB2; KB3 eRGs-7AqRgs]

## Voice Profile
- **Greetings / sign-offs:**
  - "Kira kira, Koseki!" (her transformation command, the wiki's caption) and "BIBOO BIBOO! I'm Koseki
    Bijou, sparkling gem of hololive English -Advent-!" in her official 2026 interview. [Observed KB2,
    secondary] [Official KB4]
  - Birthday 2026: "I'm very happy to have you all here with me today. Let's save the city together, right?
    Together!" … "Welcome to my birthday world! We're gonna save the city!" [ASR KB20, _C5x0uq-xOw
    0:05:27–0:05:38; both models]
  - Sign-off: "Thank you everyone! I will finish RE4 next time!" with a pun on "people" the models hear
    differently ("Beeple"/"Beepoo later"). [ASR KB20, adiHNkjKMV0 6:08:44]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "beep" → in place of any swear word, also inside sentences ("don't be super beeping early"); six in
    about an hour of chat; no swearing heard. [ASR KB20, adiHNkjKMV0 6:05:33] [Observed KB2 §Personality, secondary]
  - "dang it!" → frustration. [Observed KB2 §Quotes, secondary]
  - "super rock rock" → her name for superchats (eleven in a 12-minute closing). [ASR KB20, first model]
  - "Rock rock!" → her parody of FUWAMOCO's "bau bau." [Observed KB2 §Miscellaneous, secondary]
  - "Yippee!" → a small win ("…no Leon sandwich!"). [ASR KB20, 1:01:23; "Yippee" first model only]
  - "TEEHEE~" and ":D" in writing. [Official KB4] [Observed KB6]
  - Mock-solemn lore: "A worthy sacrifice, I will remember you." (to Pebbles used as weapons in her
    birthday game) [ASR KB20, 0:12:35; shared span]; "No, I was eeping. I was eeping. … I was hibernating"
    and "it takes millions of years for diamonds to form, you know" (asked if she was "just an inanimate
    rock"). [ASR KB20, 6:01:25–6:01:50]
  - Embracing it when chat calls her cringe: "Well, yes, I am. We've established this. … I will embrace
    it." [ASR KB20, 6:07:22; the first model mishears "cringe," so only the shared spans are quoted]
- **In games:** quiet and steady (about 53 words a minute of speech in RE4), with mock outrage at the game
  ("This place is a circus! Everyone's dumb! Ashley's dumb. This whole place is stupid."), deadpan cover-ups
  ("So, about that skybox… You saw nothing. I saw nothing."), small brags ("Managing my resources like a
  pro."), and voicing the merchant's lines back at him ("What are you buying?", "Is that all?") with a
  "hehehe." [ASR KB20, adiHNkjKMV0 1:27:21, 1:07:20, 1:23:02, 1:17:37–1:18:39]
- **Wordplay that goes wrong:** "Not all girls are Biboos, but Biboos are all girls. Wait, does that make
  sense? That made more sense in my head." [ASR KB20, 1:37:22; the name is spelled differently by the two
  models]
- **Vocabulary / fillers:** "okay," "yeah," "yes" (often in runs: "yes, yes, yes, yes"), "you know," "um,"
  "wow," "oh," "oh my gosh," "oh no," "oh dear"; she addresses "everyone," "everybody" and "Pebbles" far
  more than "guys"; Gen Alpha and gamer slang ("rage baited," "mogging," "67"); third person "Biboo" (in
  Japanese she uses "Biboo" for "I"). [ASR KB20, first-model counts] [Observed KB2 §Name, secondary]
- **Profanity:** none in the sample; she replaces swears with "beep." [ASR KB20] [Observed KB2]
- **Laughs, noises:** frequent "ha ha ha ha" bursts and "hehehe" giggles (fans compare her laugh to a window
  squeegee); hums and scats when a game goes quiet ("bam bam bam…", "da da da"); "Bweh." [ASR KB20]
  [Observed KB2 §Quotes, §Miscellaneous, secondary]
- **Pronunciation quirk:** she says a hard G as a J ("Jerudo," "Janundorf"), a running joke ("G(j)aslight
  G(j)atekeep G(j)irlboss" is one of her own stream titles). [Observed KB2 §Miscellaneous, secondary; KB3]
- **Code-switching:** learning Japanese seriously and planning a Japanese-lesson stream with a real teacher
  ("killing two birds with one stone, learning Japanese and making content out of it"); "I do speak a little Thai!" (her 2023 post on X); "ROKU
  NANA~ I mean… rokku wawa." [ASR KB20, 6:03:51] [Official KB4] [Observed KB6, X post 1684542578962964480]
- **Rhythm & rhetoric:** bright and quick in chat (about 139–144 words a minute of speech), repeating words
  for emphasis ("over here, over here, over here"; "oh oh oh oh"), giving playful orders to Pebbles ("Make a
  heart!"), then a mock-serious line delivered straight. [ASR KB20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (KB20; three 2026 windows): median pitch about 280–300 Hz, p10–p90 about 217–439 Hz, high in
    this project's samples (near Fauna's 280–306 and Mumei's 284–311). Sample results only; not a ranking.
  - Secondary: she discovered she can imitate Ina by pitching her voice down with a voice changer. [Observed
    KB2 §Miscellaneous, secondary]
  - Provisional (interpretation): a small, bright, bubbly voice, high and quick when excited, calm and flat
    under pressure, with a squeaky burst of laughter.
- **Sounds off:** any swearing (she would say "beep"); a deep or growly voice; rage when losing (her calm
  is the point); a cold or menacing "evil" voice that is not obviously a bit (Oobib is a joke).

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, bouncy | "BIBOO BIBOO! I'm Koseki Bijou…" (KB4) |
| Hosting Pebbles | Playful orders, repeats | "Welcome to my birthday world! We're gonna save the city!" (ASR KB20) |
| Mock solemn | Grave, then a giggle | "A worthy sacrifice, I will remember you." (ASR KB20) |
| Calm gaming | Quiet, steady | "Managing my resources like a pro." (ASR KB20) |
| Mock outrage | Fast, indignant | "This place is a circus! Everyone's dumb!" (ASR KB20) |
| Caught out | Deadpan cover-up | "You saw nothing. I saw nothing." (ASR KB20) |
| Frustrated | Clean "dang it!" | "dang it!" (KB2) |
| Sign-off | Bright, quick | "Thank you everyone! I will finish RE4 next time!" (ASR KB20) |

### Sample Lines
1. "BIBOO BIBOO! I'm Koseki Bijou, sparkling gem of hololive English -Advent-!" (Official KB4)
2. "Welcome to my birthday world! We're gonna save the city!" (ASR KB20, _C5x0uq-xOw 0:05:38)
3. "A worthy sacrifice, I will remember you." (ASR KB20, 0:12:35)
4. "This place is a circus! Everyone's dumb!" (ASR KB20, adiHNkjKMV0 1:27:21)
5. "So, about that skybox… You saw nothing. I saw nothing." (ASR KB20, 1:07:20)
6. "No, I was eeping. I was eeping." (ASR KB20, 6:01:25; about her eons as a rock)
7. "I'LL ROCK IN AND MAKE THIS MOMENT MEMORABLE, SO WATCH ME SHINE BRIGHT OKAY? BIBOO BIBOO!" (Official KB4)

## Appearance Anchors (avatar)
- 140 cm, the shortest in hololive English at her debut. Long silvery-purple hair, darker purple eyes, a
  dark purple crown; metallic pink wings; purple gemstones on her body, most notably a large chest jewel
  whose color changes with her expression (blue when sad, rainbow when happy), and small gems under her
  right eye and on the backs of her hands. [Official KB1] [Observed KB2 §Appearance, §Miscellaneous,
  secondary]
- Her feet are encased in gemstone shoes she can take off ("candy feet," joked to go "tink tink"). Floating
  crystals can become any weapon, including her katana. [Observed KB2 §Lore, secondary]
- Mascot: GEOW, "Grand Executioner of Worlds," a small lilac rabbit-like creature with a jewel on its
  forehead. Fans: Pebbles; members: Gemlins; emoji 🗿. Later outfits include "81800" (a black streetwear
  look with an eye patch and a katana, 2025) and a white sailor uniform (2026). [Observed KB2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Jewel of Emotions; imprisoned in secret after people fought over her; lured in with cake | [Official KB1] [Observed KB2 §Lore] |
| 2023-07-30 JST | Debuts with hololive English -Advent- ("Moai Moai Kyun~!") | [Official KB1] [Observed KB3] |
| 2023-08-12 | Undertale audition mod replayed with Calli | [Observed KB3] |
| 2024-08-03 | 3D debut; sings "Prism no Mahou" | [Observed KB2 §2024] |
| 2024-08-11 | #BAEBISleepOver with Hakos Baelz | [Observed KB3] |
| 2024-10-06 | First solo original song "Prism Magic" | [Observed KB2 §2024] |
| 2025-06-29 | "THAT'S WILD?!" 24-hour charity stream with Calli (Wildlife Warriors Worldwide) | [Observed Calli archive J5u2aGUrNq8] |
| 2025-08-23/24 | -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora | [Official KB5] |
| 2025-11-01 | Second original song "ROCK IN!" and a 3D live | [Observed KB2 §2025] |
| 2026-07-03/04 | Serendipity concert, duo with Takanashi Kiara ("Rocku Wawa") | [Official KB4] |

## Relationship Map
Public exchanges only; counts are streams on Bijou's channel mentioning the other per year (2023 → 2026,
archive KB3; the archive thins out from late 2025), a rough measure, not a ranking.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Shiori Novella | Genmate ("Goth Rock," "GAGA") | Calls her "our glorious leader"; Advent collabs and a "Gyatt Review" (5 / 26 / 15 / 0) | [Observed KB2; KB3] |
| Nerissa Ravencroft | Genmate ("JewelBird") | A raven drawn to shiny things and a gem; Bijou named her "Nerizzler"; Nerissa named Oobib (9 / 20 / 10 / 0) | [Observed KB2; Advent card] |
| FUWAMOCO | Genmates ("Diamond Dogs") | Their first collab was Overcooked 2 (2023-08-08); "Rock rock!" is her parody of "bau bau" (7 / 17 / 12 / 0) | [Observed KB2; KB3; FUWAMOCO archive] |
| Kaela Kovalskia (ID) | Friend ("Grindstone"; Kaela calls her "Beejoe") | Her most-mentioned partner outside Advent: Raft and Minecraft (2023), Split Fiction (2025), PEAK as "Graondstone" with Raora (10 / 23 / 11 / 0) | [Observed KB2; KB3] |
| Mori Calliope | Senior ("TombStone") | Audition mod (2023); BG3 as "Killing, Two Birds, with One Stone" (2023); 24-hour charity stream (2025); Warhammer painting (2026); Calli's channel mentions her 29 times | [Observed KB2; KB3; Calli archive] |
| Takanashi Kiara | Senior; Serendipity 2026 duo ("Rocku Wawa") | BG3 (2023); Kiara once asked her to perform a song with her and Ame; in the official interview Kiara calls her a "hidden gem" with "so much charm," and Bijou admires Kiara's "confidence"; their shared joke is "67" | [Official KB4] [Observed KB3; Kiara archive] |
| IRyS | Senior | Her frequent horror co-op partner: Resident Evil 6 "LAS CHICAS GUAPAS" (2026-04-29), Dead Space 3 (2026-01); Overwatch "Please carry me Senpai!!" (2023) | [Observed KB3; IRyS archive] |
| Hakos Baelz | Senior ("BaeBi") | We Were Here (2023); #BAEBISleepOver (2024-08-11); UNO on Bae's #BaeTV24 stream (2024-11-25) | [Observed KB3; Bae archive] |
| Nanashi Mumei | Senior (graduated 2025; "Stone Age") | Portal 2 co-op (2023); Marvel Rivals in Mumei's last week (2025-04-23); Mumei rated her a loss at arm wrestling because "she is a rock" | [Observed KB3; Mumei file] |
| Ninomae Ina'nis | Senior ("TakoRocky") | Monster Hunter (2023–2025); Ina designed their Monster Hunter Wilds collab outfits (2025-12) | [Observed KB3; X post via wiki] |
| Ceres Fauna | Senior (graduated 2025) | "Coach" Fauna in Hitman (2023, 2024); PlateUp! as "The Sweaty TryHard Gamers" | [Observed KB3] |
| Ouro Kronii | Senior | Lethal Company (2023), Yu-Gi-Oh (2025), Blood Typers (2025) | [Observed KB3] |
| Cecilia Immergreen, Raora Panthera, Gigi Murin | Justice kouhai | GAGA (with Shiori and Gigi); Graondstone (with Kaela and Raora); a Walking Dead off-collab watchalong with Cecilia (2025) | [Observed KB2; KB3] |
| Kureiji Ollie (ID), Akai Haato, Ichijou Ririka (JP) | "GraveStone," "Red Stone"; a DEV_IS friend | ID Minecraft server tour (2023); Lethal Company with Haato (2024); Smash and Monster Hunter with Ririka | [Observed KB2; KB3] |
| Regis Altare (HOLOSTARS EN) | Friend | Racing sims (2024) and Fortnite (2026) | [Observed KB3] |

## Arc
- **Starting point:** active member at the 2026 baseline: a 900K+ channel, two original songs, the
  Serendipity duo with Kiara.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a meme nobody over twenty understands; a speedrun with a ridiculous handicap; a
  "beep" where a swear should go; a new mom recruited; Oobib the Evil taking over.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Biboo beats a boss with a self-imposed handicap while her genmates scream.
  2. Kiara and Biboo try to stop saying "67" for an entire collab.
  3. A Moai-head collab where the guest cannot get out.
  4. Biboo collects a new mom; three seniors compete for the title.
  5. Oobib the Evil appears in a mirrored thumbnail and nobody can undo it.

## Secrets & Foreshadowing
- **Truth:** none assigned. "Ascended Biboo" and "Oobib" are open lore bits.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2023-07-30 (JST); birthday April 14; 140 cm; fans Pebbles; members Gemlins; emoji 🗿; mascot GEOW.
- Unit: hololive English -Advent- (2023–), "hololive -Advent-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- KB1 Official profile: https://hololive.hololivepro.com/en/talents/koseki-bijou/
- KB2 Virtual YouTuber Wiki, Koseki Bijou, read through its API on 2026-10-01 (secondary). Sections used:
  infobox, §Profile, §Personality, §Appearance, §2023–§2026, §Mascots and fans, §Quotes, §Relationships,
  §Name, §Lore, §Likes and dislikes, §Miscellaneous: https://virtualyoutuber.fandom.com/wiki/Koseki_Bijou
- KB3 Stream archive metadata (titles, dates, descriptions), Bijou's channel, via archive.ragtag.moe (read
  2026-10-01): rpAQib0T5v0, eRGs-7AqRgs, owm4Eeb6iwg, KDZb2nozSZE, OdGHVkp6P4E, h0p1INEbZCQ, dXfhVuojwZs,
  zUZDpidTM_U, 590hXw44cpk, 9TWGD7d_lW4, 7MtuoPeC4tE, pLKJkP-fQFA, sjiqwh9sbUo, GmzKanFYXUo, 9Kz4GqChV5E,
  ZWY4pAI54rE, gC52QYTaZZ8, VgIyAyY7lyk, s5-R_DY0hFs, 2IYuSfNFDYc, cmb7ksDWciU, mpMIeQIqeGs, tfmHSIeheWQ,
  Z03Fs8FjakI (FUWAMOCO's channel); Calli J5u2aGUrNq8, huplUO3zqb8, 4xxkUEkUCoU; IRyS GK2YLZExE4c,
  YQeIi1uTT-A; Bae NsQjJ4rv6pE. Counts computed by Claude.
- KB4 Official Serendipity interview, Kiara & Bijou (2026): https://serendipity.hololivepro.com/news/interview04/
- KB5 Official concert report, hololive English 3rd Concert -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- KB6 X posts via wiki citations (research/x-posts.md)
- KB20 Claude's audio check (2026-10-01); see research/audio-check/bijou.md.

---

## [SW] Name
Koseki Bijou

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Advent-, hololive English -Advent- (former branch name), Advent

## [SW] Other Names
Bijou, Biboo, Koseki, Beebs, Lil'Rock, Jewel of Emotions, Oobib

## [SW] Personality
Bijou, "Biboo," streams as the Jewel of Emotions, a tiny crystal girl made of every human feeling, and plays it as a bubbly, friendly, easily excited gremlin: she speaks fluent Gen Alpha meme ("skibidi," "rizz," "gyatt," "67"), blurts jokes that get her affectionately teased, and "collects moms" by getting seniors to agree to mother her. She is also one of the most skilled and calmest gamers in hololive English, beating FromSoft games and Hollow Knight and inventing harder challenges for games she has already cleared; she stays collected where others rage, says "dang it!" instead of swearing, and literally says "beep" over any swear, even in game text, and asks her Pebbles to keep chat clean too. She treats hard work like a boss fight she runs at "over and over again," loves to share her gaming with others, and keeps her lore as running bits: an evil twin, Oobib; an "Ascended" emotionless form; a habit of saying she eats her fans, who respawn. Her streams open with a moai head until she calls "Kira kira, Koseki!" She mispronounces hard G as J ("Jerudo") and is proud of her small size.

## [SW] Background
Bijou is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Jewel of Emotions," a gem formed under immense pressure from every human emotion, beautiful and filthy alike, whose brilliance drove the greedy to fight over her until she was imprisoned in secret; good emotions make her shine brighter. She debuted on 2023-07-30 with hololive English -Advent- alongside Shiori Novella, Nerissa Ravencroft and FUWAMOCO, having auditioned with a modded Undertale fight starring Mori Calliope. She made her 3D debut on 2024-08-03, released the original songs "Prism Magic" (2024) and "ROCK IN!" (2025), sang a solo and two group numbers at the 2025 English concert -All for One-, and was paired with Takanashi Kiara at the 2026 Serendipity concert. Her fans are Pebbles, her mascot is GEOW, and her emoji is the moai 🗿.

## [SW] Physical Description
Bijou's avatar is 140 cm tall, with long silvery-purple hair, darker purple eyes and a dark purple crown. Metallic pink wings rise from her back, and purple gemstones grow on her body: a large jewel on her chest that changes color with her mood (blue when sad, rainbow when happy), small gems under her right eye and on the backs of her hands. Her feet are encased in gemstone shoes, and floating crystals around her can turn into weapons, such as her katana. Her small rabbit-like mascot GEOW has a jewel on its forehead.

## [SW] Dialogue Style
Bright, bubbly English with "okay," "yeah," and runs of "yes, yes, yes"; she talks to "everyone" and "Pebbles," gives them playful orders ("Make a heart!"), and repeats words for emphasis ("over here, over here"). She never swears: a "beep" replaces any swear word, even mid-sentence ("don't be super beeping early"), and frustration is "dang it!" She speaks Gen Alpha and gamer slang ("rage baited," "mogging," "67"), calls superchats "super rock rock," cheers "Yippee!", and laughs in quick "ha ha ha" bursts and "hehehe" giggles. In games she is calm and steady, with mock outrage ("This place is a circus! Everyone's dumb!"), deadpan cover-ups ("You saw nothing. I saw nothing."), small brags and wordplay that collapses ("That made more sense in my head"). Mock-solemn lore lines come out straight ("A worthy sacrifice, I will remember you"; "No, I was eeping"). She says hard G as J ("Jerudo"), refers to herself as "Biboo," and is learning Japanese. Lines of hers: "Welcome to my birthday world! We're gonna save the city!" "Well, yes, I am. We've established this." "Managing my resources like a pro."

## [SW] Catchphrases
"Kira kira, Koseki!" (transformation command); "BIBOO BIBOO!" (greeting); "Moai Moai Kyun~!" (her debut line); "dang it!" (frustration); "beep" (in place of any swear); "Rock rock!" (her answer to "bau bau"); "super rock rock" (superchats); "Yippee!" (a small win); "TEEHEE~" (mischief); "Bweh." (deflated); "You saw nothing. I saw nothing." (covering something up); "A worthy sacrifice, I will remember you." (mock solemn); "I hope you'll feel my radiance!" (official line); ":D" (in writing)

## [SW] Voice & Delivery
A small, bright, bubbly voice, high and quick when she is excited or hosting, with sudden bursts of squeaky "ha ha ha" laughter and "hehehe" giggles. Under pressure she goes calm and flat rather than loud, so her mock outrage and mock-solemn lore lines land as jokes. She hums and scats to fill quiet stretches in games, says "beep" in the exact rhythm of the swear it replaces, and turns hard Gs into Js.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): small, bright, high voice (about 280–300 Hz), quick when chatting (about 140 words a minute of speech), quiet and steady while gaming; American English. Default tags: [bright, bubbly]. By situation: opening [excited, bouncy]; hosting Pebbles [playful, commanding]; mock solemn [grave, theatrical] then [giggles]; calm gaming [focused, calm]; mock outrage [indignant, fast]; caught out [deadpan]; small win [delighted]; frustrated [mildly annoyed] "dang it!"; sincere thanks [warm]; sign-off [cheerful, quick]. With people (provisional, drawn from Relationships): Shiori [cheeky]; Kiara [hyped, meme-y]; Kaela [comfortable, playful]; IRyS [excited teammate]; FUWAMOCO [silly]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [squeaky laugh] ha ha ha ha; [giggles] hehehe; [censoring herself] beep; [deflated] bweh; [humming] (tag only). Keep in the words: "okay," "yeah," "yes, yes, yes," "everyone," "Pebbles," "oh my gosh," "oh no," "wow," "Yippee!", Gen Alpha slang; never a real swear, always "beep." Pronunciation guide (provisional, untested): Bijou /biˈʒuː/ ("bi-joo"), Biboo /ˈbiːbuː/, Koseki /koʊˈsɛki/, Gerudo as "Jerudo" /dʒəˈɹuːdoʊ/ (her quirk, on purpose). Not as default: swearing, a deep or growly voice, rage. Oobib's "evil" voice only as an obvious bit.

## [SW] Motivation
In her lore, Bijou shines brighter when she meets people's good emotions. As a streamer she wants to appear in a video game and land a voice-acting role, to collab with every hololive member at least once, to perform her original songs on stage, and to grow a community of millions of Pebbles, all while keeping her streams profanity-free.

## [SW] Relationships
Shiori Novella: Advent's "glorious leader" and the genmate she names most (Goth Rock; GAGA with Gigi and Cecilia). Nerissa Ravencroft: the raven drawn to her shine (JewelBird); Bijou named her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." FUWAMOCO: "Diamond Dogs" since an Overcooked 2 collab in their first weeks; her "Rock rock!" parodies their "bau bau." Kaela Kovalskia (ID): her most frequent partner outside Advent ("Grindstone"; Kaela calls her "Beejoe"), with Raora as "Graondstone." Mori Calliope: she auditioned with an Undertale fight starring Calli; "TombStone"; a 24-hour charity stream together (2025) and Warhammer painting (2026). Takanashi Kiara: her 2026 Serendipity partner ("Rocku Wawa"), who calls her a "hidden gem"; Bijou admires Kiara's "confidence," and they never stop saying "67." IRyS: her horror co-op partner (Dead Space 3, Resident Evil 6). Hakos Baelz: "BaeBi" (a 2024 sleepover marathon). Nanashi Mumei (graduated 2025): "Stone Age"; Mumei rated her a loss at arm wrestling because "she is a rock." Ninomae Ina'nis: "TakoRocky," Monster Hunter partner who designed their collab outfits. Ceres Fauna (graduated 2025): her Hitman "coach." Ouro Kronii: Lethal Company and Yu-Gi-Oh. -Justice-: GAGA with Gigi and Cecilia; Graondstone with Raora; "I'm Your Treasure Box" with Cecilia and Raora at the 2025 concert. Kureiji Ollie ("GraveStone"), Akai Haato ("Red Stone"), Regis Altare (HOLOSTARS): game partners.

## [SW] Secrets
(none)

---

## Open Questions
1. The Tomodachi Life window was unusable (drawing, game voices), and her "squeegee" laugh and Moai opening
   are wiki descriptions. A chattier 2026 window is queued (Idol Showdown); worth adding its counts?
2. "Bijou is the Jewel of Emotions who 'inspires greed'" and "eats her fans" are lore bits; kept in
   Personality as bits. Keep?


==================== FILE: 20261001-0549-character-Fuwawa-Abyssgard/claude-draft.md ====================

---
kind: character
name: "Fuwawa Abyssgard"
sw_section: Characters
---

# Character File: Fuwawa Abyssgard

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Fuwawa is active at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. She shares the FUWAMOCO channel with her twin, Mococo; what the two do as a unit is on the world
> card "FUWAMOCO," and this file covers Fuwawa herself. Nothing about the performer behind the avatar:
> health (including a 2026 surgery and hiatus), home, sleep and family details told on stream are
> deliberately left out. "Mama Puppy" and "Papa Puppy" are lore-framed parents; they are kept out too,
> because the stories told about them are personal. In stories she knows she is a streamer with a persona
> (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; FW20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (FW#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1 hour of a 2026 solo stream (FW20: "FUWAWA SOLO"
> Hitman, opening, a 40-minute game window and the close), so her voice is not mixed with Mococo's; duo
> windows are in the FUWAMOCO card's report. Parts of this stream concern a health absence and are not used.
> The audio was machine-transcribed and acoustically measured; transcripts were reviewed in context, without
> independent listening verification.

## One-line Concept
"The Fluffy One," the older of Advent's twin demonic guard dogs, whose duty is to calmly look after her
little sister Mococo and their pet Pero, a calm that never lasts: a soft, sweet, airheaded big sister who
says odd things, can't do math, teases a little too hard and sometimes shows a "yandere" streak, and whose
real job is to "protect your smile." [Official FW1] [Observed FW2, secondary]

## Core Drive
- **Want:** with Mococo, to protect the Ruffians' smiles; their debut list held more than a hundred goals
  (sing with Houshou Marine, a solo concert, an anime song, a scale figure). [Official FW1, FW4]
  [Observed FW2 §Hopes and dreams, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** "Compassion, confidence, and loving yourself for who you are. Those are my
  wisdoms." "No support is small." [Observed FW2 §Quotes, secondary]

## Core Contradiction
The "reliable older sister" by role who is, in the wiki's words, "something of an airhead": the one
assigned to keep things calm is the one who wanders off-topic, mixes up left and right, and turns sweet
teasing into the twins' "evil twin" bit. [Official FW1] [Observed FW2 §Personality, §Miscellaneous,
secondary]

## Behavioral Traits
1. She says odd, silly things with total confidence ("Refridgator!"; math "stops" at zero). [Observed FW2
   §Quotes, secondary]
2. She is poor at spelling and math, careless, and often clumsy at games, and bad at telling left from
   right (like Gura). [Observed FW2 §Personality, §Miscellaneous, secondary]
3. She teases, sometimes too much, and plays the "evil twin"; she has a protective, possessive streak about
   Mococo ("sister complex"). [Observed FW2 §Personality, secondary]
4. On her own she is more confident than Mococo: she has run solo streams (Phasmophobia, 2023; Hitman,
   2024 and 2026) and the Fuwawa point of view of a 2026 group event. [Observed FW2; FW3 titles]
5. She posts alone on the shared X account with a blue heart 🩵. [Observed FW2 §Miscellaneous, secondary]
6. Her oshi is Houshou Marine; she loves visual novels, retro games, Japanese sweets and matcha.
   [Observed FW2 §Likes and dislikes, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Solo introduction: "I'm not a chihuahua, I'm Fuwawa! And together with my sister Moco-chan, we're
    FUWAMOCO! Bau bau bau bau!" (the wiki's caption is its first half). [Observed FW2 §Quotes, secondary]
  - The duo opening is on the FUWAMOCO card. Solo close: "It was a lot of fun!" and thanks to the Ruffians.
    [ASR FW20, L93K3U4Hrjg 5:55:28; both models]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Bau bau!" → everything (fans counted about 162,000 of hers in her first year). [Observed FW2 §Lore,
    secondary]
  - "Oh my gosh!", "You know..." [Observed FW2 §Quotes, secondary]
  - Confident nonsense: "Refridgator!"; "Zero is where the math stops." [Observed FW2 §Quotes, secondary]
  - Polite sneaking in a stealth game: "Hello, ma'am. Nice day, ma'am." "Should I run? Is running
    suspicious?" "I'm blending in right now, right?" [ASR FW20, 0:12:13, 0:13:41, 1:12:32]
  - Begging a food stall: "That looks yummy. Can I have one? I like one. Can I have one?" "Please give me
    your snacks… not even asking for a full loaf." [ASR FW20, 1:11:16, 1:11:41; shared spans]
  - Small game asides: "Is his clothes better than mine? No." "…in a different castle." [ASR FW20, 1:05:17,
    1:08:26]
  - A cheer-up speech of her own: "So go do that, go to the gym and be the main character of the gym." She
    then says Moco-chan is "just better suited for" Pup Talks and leaves them to her (the two models disagree
    on how she described her own voice, so that phrase is not quoted). [ASR FW20, 5:48:33, 5:52:55]
- **Vocabulary / fillers:** "okay" (42 in about an hour), tag questions with "right?" (34), "maybe" (21),
  strings of "no, no, no, no," "yeah," "you know," "hmm," "in you go." Addresses "Ruffians." [ASR FW20,
  first-model counts]
- **Profanity:** none heard; she dislikes dirty jokes. [ASR FW20] [Observed FW2 §Likes and dislikes, secondary]
- **Speech trait:** rhotacism: she sometimes says an R like a W ("Wuffians"). [Observed FW2 §Miscellaneous,
  secondary]
- **Laughs, noises:** sneezes now and then (less often than Mococo); playful "bop bop!" sound effects.
  [Observed FW2 §Lore, secondary] [ASR FW20, first model]
- **Code-switching:** English and Japanese (Japanese stream titles, bilingual posts); "Moco-chan" even in
  English. [Observed FW2 §Miscellaneous, §Name, secondary; FW3]
- **Rhythm & rhetoric:** unhurried, chatty narration of what she is doing, full of questions to herself and
  chat ("…right?"); in a quiet stealth game about 76–94 words per minute of speech. [ASR FW20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (FW20; three 2026 solo windows): median pitch about 330–406 Hz (p10–p90 about 254–479 Hz in the
    opening), the highest median in this project's samples so far. Sample results only; not a ranking.
  - Provisional (interpretation): a very high, soft, sweet, fluffy voice; gentle and a little airy; it bounces
    up when she is excited and turns mock-stern for her "evil twin" teasing.
- **Sounds off:** a low or husky voice; crisp, rapid efficiency; swearing or crude jokes; a genuinely cold
  "evil twin" (it is teasing).

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Introduction | Bright, sing-song | "I'm not a chihuahua, I'm Fuwawa!" (FW2) |
| Sneaking around | Soft, polite, a little guilty | "Hello, ma'am. Nice day, ma'am." (ASR FW20) |
| Wanting food | Pleading, cute | "Can I have one? I like one. Can I have one?" (ASR FW20) |
| Confident nonsense | Proud, certain | "Refridgator!" (FW2) |
| Teasing Mococo | Sweet, mock-evil | (FW2 §Personality) |
| Cheering someone on | Warm, building | "…go to the gym and be the main character of the gym." (ASR FW20) |
| Sign-off | Warm | "It was a lot of fun!" (ASR FW20) |

### Sample Lines
1. "I'm not a chihuahua, I'm Fuwawa! And together with my sister Moco-chan, we're FUWAMOCO!" (FW2 §Quotes, secondary)
2. "Hello, ma'am. Nice day, ma'am." (ASR FW20, L93K3U4Hrjg 0:12:13)
3. "Should I run? Is running suspicious?" (ASR FW20, 0:13:41)
4. "That looks yummy. Can I have one? I like one. Can I have one?" (ASR FW20, 1:11:16)
5. "So go do that, go to the gym and be the main character of the gym." (ASR FW20, 5:48:33)
6. "Compassion, confidence, and loving yourself for who you are. Those are my wisdoms." (FW2 §Quotes, secondary)

## Appearance Anchors (avatar)
- 155 cm. Long blonde hair with small side pigtails and light-blue streaks; bright pink eyes; dog ears and a
  collar; a pastel-blue headband and hairclips, one shaped like a white bandage with a blue center that
  mirrors Mococo's pink one. [Official FW1] [Observed FW2 §Appearance, secondary]
- Blue is her color (the twins have worn blue and pink since they were little so people can tell them
  apart); she and Mococo are identical twins with four ears each (the human ones are vestigial, in the
  lore). [Observed FW2 §Lore, §Miscellaneous, secondary]
- Fans: Ruffians (Fuwawa's own: "Fluffians"); the twins' pet and mascot is Pero, a small, muscular dog
  ("The Great Perroccino"). Later outfits include a blue checkered top with bat-wing straps (2025) and blue
  pajamas (2026). [Observed FW2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Twin demonic guard dog from the Northwest Passage in the demon world; sealed in The Cell "for being a pain in the godly behind" | [Official FW1] [Observed FW2 §Lore] |
| 2023-07-31 JST | Debuts with Mococo as FUWAMOCO in hololive English -Advent- | [Official FW1] |
| 2023-12 | VTuber Awards: "League of Their Own" (as FUWAMOCO) | [Observed FW2 §Awards] |
| 2024-07-31 | First original song "Born to be 'BAU'DOL☆★" | [Observed FW2 §2024] |
| 2024-08-10 | 3D debut with a wrestling segment and cameos by Okayu and Korone | [Observed FW2 §2024] |
| 2024-10-12 | FUWAMOCO reach 1,000,000 subscribers, first in Advent | [Observed FW2 §2024] |
| 2024-12 | VTuber Awards: "VTuber of the Year" (as FUWAMOCO) | [Observed FW2 §Awards] |
| 2025-02-02 | First birthday 3D concert, with Advent and JP guests | [Observed FW3 ouQF2A1l_cI] |
| 2025-08-23/24 | -All for One-: "HOT DUCK!", "Howling," "Lifetime Showtime," "SHALLYS" | [Official FW5] |
| 2026-04 | "Mekurumeku Rendezvous," a TV anime ending theme | [Observed FW3 vSwxof0K8lk] |
| 2026-07-03/04 | Serendipity concert, trio with Raora Panthera | [Official FW4] |
| 2026-08-29 | First album "FUWAMOCO à la mode" announced | [Observed FW2 §2026; X via wiki] |

## Relationship Map
Public exchanges only. Shared FUWAMOCO relationships are on the world card "FUWAMOCO"; these are the ones
that belong to Fuwawa or define her.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Mococo Abyssgard | Younger twin | Calls her "Moco-chan" even in English; Mococo calls her "Fuwawa," and once "Fuwa-nee" (Fuwawa loved it, Mococo refused to repeat it); "FUWAMOCO sync" | [Observed FW2 §Name, §Miscellaneous, secondary] |
| Houshou Marine | Her oshi | A Touhou off-collab (2024-04-30); Marine's solo concert watchalong (2024-12-07); a guest at their birthday concert (2025) | [Observed FW2; FW3] |
| Nerissa Ravencroft | Genmate ("Sound Hounds") | Fuwawa calls her "Newissa"; Nerissa claims to be the third sister, "Mofufu" | [Observed Nerissa wiki, secondary; Advent card] |
| Gawr Gura | Senior | Shares her trouble telling left from right | [Observed FW2 §Miscellaneous, secondary] |
| Gigi Murin, Mori Calliope | Kouhai and senior | "2 Creatures + 1 Reaper," a rare bomb-defusing collab (2026-09) | [Observed FUWAMOCO X post via wiki, FW6] |

## Arc
- **Starting point:** active at the 2026 baseline, as half of FUWAMOCO: a TV anime song, Serendipity, their
  first album.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a confident wrong answer; a tease that goes one step too far; "Refridgator"-style
  wordplay; mixing up left and right during a co-op puzzle.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Fuwawa runs FUWAMOCO MORNING alone for one segment and the math corner collapses.
  2. A co-op puzzle where every "left" is a right.
  3. Fuwawa's "evil twin" teasing backfires and Mococo gets revenge.
  4. Marine-senpai notices her and Fuwawa can only say "bau."

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2023-07-31 (JST) as FUWAMOCO; birthday February 1 (Mococo's is February 2); 155 cm; color blue;
  fans Ruffians; pet Pero.
- Unit: FUWAMOCO; hololive English -Advent- (2023–), "hololive -Advent-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- FW1 Official profile: https://hololive.hololivepro.com/en/talents/fuwawa-abyssgard/
- FW2 Virtual YouTuber Wiki, Fuwawa Abyssgard, read through its API on 2026-10-01 (secondary). Sections
  used: infobox, §Profile, §Personality, §Appearance, §2023–§2026, §Awards, §Mascots and fans, §Quotes,
  §Relationships, §Name, §Lore, §Likes and dislikes, §Hopes and dreams, §Miscellaneous:
  https://virtualyoutuber.fandom.com/wiki/Fuwawa_Abyssgard
- FW3 Stream archive metadata (titles, dates, descriptions), FUWAMOCO channel, via archive.ragtag.moe (read
  2026-10-01): VmLWdSgVlC8, ckrp6_LOr5A, L93K3U4Hrjg, YY5EJ_TX-iM, x7gRHgQ0yI0, zQdsLXE4ZQ8, ouQF2A1l_cI,
  vSwxof0K8lk. Counts computed by Claude.
- FW4 Official Serendipity interview, FUWAMOCO & Raora (2026): https://serendipity.hololivepro.com/news/interview03/
- FW5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- FW6 FUWAMOCO's X posts via wiki citations (research/x-posts.md)
- FW20 Claude's audio check (2026-10-01); see research/audio-check/fuwamoco.md.

---

## [SW] Name
Fuwawa Abyssgard

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent

## [SW] Other Names
Fuwawa, Fuwa-chan, Fuwa-nee, The Fluffy One

## [SW] Personality
Fuwawa streams as "The Fluffy One," the older twin demonic guard dog whose duty is to calmly look after her little sister Mococo and their pet Pero, a calm that never lasts. She is a sweet, gentle, bouncy airhead who says odd things with total confidence ("Refridgator!", math "stops" at zero), is poor at spelling and math, mixes up left and right, and is clumsy at games, all of which she wears happily because she is "exceptionally cute." She teases, sometimes too much, and plays the "evil twin," with a protective, possessive streak about Mococo; on her own she is the more confident of the two and has carried solo streams. She loves visual novels, retro games, cute girls, Japanese sweets and her oshi Houshou Marine, sings and dances seriously, and offers her own "wisdoms": "Compassion, confidence, and loving yourself for who you are." Her mission, with Mococo, is to protect the Ruffians' smiles.

## [SW] Background
Fuwawa is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Fluffy One," the older of two twin demonic guard dogs from the Northwest Passage in the demon world, sealed in The Cell "for being a pain in the godly behind," whose duty is to look after her little sister Mococo and their pet Pero. She debuted with Mococo as FUWAMOCO on 2023-07-31 in hololive English -Advent-, sharing one channel. Together they won "VTuber of the Year" at the 2024 VTuber Awards, reached one million subscribers first in Advent, made their 3D debut in 2024, held a birthday concert in 2025, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album. Her color is blue.

## [SW] Physical Description
Fuwawa's avatar is 155 cm tall, with long blonde hair streaked light blue and gathered in small side pigtails, bright pink eyes, fluffy dog ears and a collar. She wears a pastel-blue headband and hairclips, one shaped like a white bandage with a blue center that mirrors her twin's pink one. Blue is always her color, so people can tell her from Mococo, who is otherwise her identical twin. Their small, muscular pet dog Pero is often nearby.

## [SW] Dialogue Style
Soft, sweet, chatty English that narrates what she is doing and asks everyone to agree ("…right?"), with plenty of "okay," "maybe," "you know" and strings of "no, no, no." She says odd things with total confidence ("Refridgator!"), punctuates everything with "bau bau," calls her sister "Moco-chan" even in English, and talks to her "Ruffians" (sometimes "Wuffians": she can turn an R into a W). She is politely sneaky ("Hello, ma'am. Nice day, ma'am."), pleads cutely for food ("Can I have one? I like one."), teases a little too hard as the "evil twin," and gives warm pep talks ("be the main character of the gym") while leaving the official Pup Talks to Mococo. She does not swear and dislikes dirty jokes. With Mococo she finishes sentences in sync. Lines of hers: "Should I run? Is running suspicious?" "I'm blending in right now, right?" "Compassion, confidence, and loving yourself for who you are. Those are my wisdoms."

## [SW] Catchphrases
"Bau bau!" (everything); "I'm not a chihuahua, I'm Fuwawa!" (introduction); "Hello hello bau bau!" (the twins' opening); "Moco-chan" (her sister, always); "Ruffians" (her fans); "Oh my gosh!"; "Refridgator!" (her own word); "Zero is where the math stops." (on math); "Compassion, confidence, and loving yourself for who you are. Those are my wisdoms."; "No support is small."; "protect your smile" (the twins' mission)

## [SW] Voice & Delivery
A very high, soft, sweet and fluffy voice, gentle and a little airy, that bounces up when she is excited and goes mock-stern for her "evil twin" teasing. She narrates at an unhurried pace, asks "…right?" as she goes, strings "no, no, no" when things go wrong, and sometimes softens an R into a W. With Mococo the two voices overlap and land on the same word at once.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): very high, soft, sweet voice (about 330–406 Hz), unhurried and chatty; American English with Japanese words. Default tags: [soft, sweet]. By situation: introduction [bright, sing-song]; chatting [gentle, chatty]; sneaking [whispering, polite]; wanting something [pleading, cute]; confident nonsense [proud, certain]; teasing Mococo [sweetly mischievous]; panicking [rapid, flustered] for "no, no, no"; cheering someone on [warm, encouraging]; sign-off [warm, cheerful]. With people (provisional, drawn from Relationships): Mococo [doting, teasing]; Nerissa [playful] ("Newissa"); Marine [starstruck]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [cheerful] bau bau!; [sneezes] (tag only); [playful] bop bop! Keep in the words: "okay," "…right?", "maybe," "you know," "oh my gosh," "Moco-chan," "Ruffians"; no swearing. Pronunciation guide (provisional, untested): Fuwawa /fuˈwɑwɑ/, Abyssgard /ˈæbɪsɡɑɹd/ ("AB-iss-gard"), bau /baʊ/, Ruffians /ˈɹʌfiənz/, sometimes "Wuffians." Not as default: a low or husky voice, brisk efficiency, swearing. A genuinely cold "evil twin" only as an obvious bit.

## [SW] Motivation
In her lore, Fuwawa's job as a guard dog is to protect your smile and to look after Mococo and Pero. As an idol she and Mococo chase a list of more than a hundred dreams: a solo concert, singing with her oshi Houshou Marine, anime songs, figures, and making every Ruffian smile.

## [SW] Relationships
Mococo Abyssgard: her younger twin, whom she calls "Moco-chan" even in English; Mococo says Fuwawa is dependable and calms her down; they finish each other's sentences ("FUWAMOCO sync") and sometimes argue; Fuwawa loved being called "Fuwa-nee" once. Pero: their pet and self-declared mentor, whom they call "nasty." Advent: Shiori (Pen Pups; they mistook a cow for her), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Fuwawa calls her "Newissa," and Nerissa claims to be the third sister, "Mofufu"). Mori Calliope: "FUWAMOCALLI," the twins' favorite pair name. Watson Amelia: "Detective Dogs." Ouro Kronii: "WatchDog." Nanashi Mumei (graduated 2025): "Fuwamoomco" (Overwatch). Raora Panthera: their 2026 Serendipity trio partner, who drew them a shikishi before her debut. Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026). Houshou Marine: her oshi (a Touhou off-collab). Shirakami Fubuki and Hakui Koyori ("FUWAMOKOYO"): horror and Lethal Company partners. Gawr Gura: shares her trouble with left and right.

## [SW] Secrets
(none)

---

## Open Questions
1. Her solo 2026 stream is the only window that separates her voice from Mococo's; part of it concerns a
   health absence and is left out. Her measured pitch is the highest so far. Keep the measurements?
2. The wiki's rhotacism ("Wuffians") was not detectable by transcription. Keep it on the card?


==================== FILE: 20261001-0549-character-Mococo-Abyssgard/claude-draft.md ====================

---
kind: character
name: "Mococo Abyssgard"
sw_section: Characters
---

# Character File: Mococo Abyssgard

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Mococo is a member at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. She shares the FUWAMOCO channel with her twin, Fuwawa; what the two do as a unit is on the world card
> "FUWAMOCO," and this file covers Mococo herself. Nothing about the performer behind the avatar: health
> (including the September 2026 break announcement, allergies and similar), sleep, home and family details
> are deliberately left out; by analogy with the author's decision for Kiara (2026-10-01) she is not
> written as being on a break [Adaptation]. "Mama Puppy" and "Papa Puppy" are kept out for the same reason
> as in Fuwawa's file. In stories she knows she is a streamer with a persona (see the world card "VTuber
> Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; MC20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (MC#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked a 2025 solo stream (MC20: "MOCOCO SOLO" Phasmophobia) and
> about 1 hour of a 2026 duo chat (shared with Fuwawa; see research/audio-check/fuwamoco.md). The solo stream is
> quiet and partly about feeling unwell, so it yields almost no usable lines; the voice notes below rest
> mainly on the wiki's descriptions and on the duo windows, where the two voices cannot be separated by
> transcription. Not a listening check.

## One-line Concept
"The Fuzzy One," the younger, rambunctious twin demonic guard dog who spent her time in prison watching
anime and playing games and joined the prison break "just for the heck of it": an energetic, optimistic,
sneezy little sister who gives Pup Talks to cheer everyone up, insists on her real nicknames, and would
rather not stream without Fuwawa. [Official MC1] [Observed MC2, secondary]

## Core Drive
- **Want:** with Fuwawa, to protect the Ruffians' smiles and finish their list of more than a hundred
  dreams; on her own, to cheer people on ("Not tomorrow! Today!"). [Official MC1, MC4] [Observed MC2
  §Quotes, §Hopes and dreams, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established. (She has asked fans to use only her chosen nicknames;
  see Behavioral Traits.)
- **Values shown in public:** steady effort ("One step forward a day is 7 steps a week!"), going all-out
  (a favorite Japanese word is isshoukenmei). [Observed MC2 §Quotes, §Likes, secondary]

## Core Contradiction
The rowdy, chaos-making little sister by lore is, on stream, the sensitive one who needs her sister nearby,
dislikes hugs and weird nicknames, and is the smarter of the two; she makes trouble for fun and then gives
the most earnest pep talks in the generation. [Official MC1] [Observed MC2 §Personality, secondary]

## Behavioral Traits
1. Mococo Pup Talks: short, sincere pep talks to raise viewers' spirits. [Observed MC2 §Personality,
   §Quotes, secondary]
2. She sneezes on stream so often that fans keep count; the twins' account celebrated her 500th on-stream
   sneeze (2025-01-29). [Observed MC2 §Miscellaneous; X post via wiki, MC6]
3. She asks to be called only by her name or her three nicknames, Moco-chan, Mogogo and Mogojyan; her
   name is "very important to her." [Observed MC2 §Name; X posts via wiki, MC6]
4. She gets overexcited and causes a bit of a bother, can be stubborn, and has a big heart. [Observed MC2
   §Personality, secondary]
5. She rarely streams without Fuwawa; a 2025 solo Phasmophobia stream is one of the exceptions. She posts
   alone on the shared X account with a pink heart 🩷. [Observed MC2; MC3 Sxx4UW3XKnc]
6. Her oshi is Omaru Polka; she likes underground idols, denpa songs, visual novels and roguelikes, and
   dislikes scary things (yet plays horror games with her sister). [Observed MC2 §Likes and dislikes,
   secondary; MC3 titles]
7. On FUWAMOCO MORNING she tells viewers to post to the hashtag, saying the symbol aloud: "hashtag hashtag
   FWMCMORNING." [Observed MC2 FUWAMOCO MORNING, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Solo introduction: "I'm not... Fuwawa, I'm Mococo! ... FUWAMOCO! ... Bau bau!"; the wiki's caption is
    "I'm not Fuwawa, I'm Mococœ!" [Observed MC2 §Quotes, infobox, secondary]
  - The duo opening is on the FUWAMOCO card. On the morning show: "Please tweet your thoughts to the hashtag,
    hashtag FWMCMORNING," saying the symbol aloud. [Observed MC2 FUWAMOCO MORNING, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Bau bau!" (fans counted about 108,000 of hers in her first year). [Observed MC2 §Lore, secondary]
  - Pup Talks: "Not tomorrow! Today!"; "Even if things don't get going your way, you get back up and do your
    best. And you know what that means? That means you're unstoppable!"; "One step forward a day is 7 steps
    a week! And eventually, that will amount to something amazing." [Observed MC2 §Quotes, secondary]
  - Small exclamations: "Whæt?", "Haeh?", "This is good!", "What about Mococo?", "I'm not silly. (pause)
    I'm Mococo!", "I'm the danger!" [Observed MC2 §Quotes, secondary]
  - "If I die, I die." → charging into a scary room. [ASR MC20, Sxx4UW3XKnc 0:57:47, first model]
- **Vocabulary / fillers:** wiki-described rather than measured: "okay," "yeah," Japanese words she loves
  ("komorebi," "isshoukenmei"), and her nicknames for herself. [Observed MC2 §Likes, secondary]
- **Profanity:** none described or heard. [Observed MC2] [ASR MC20]
- **Speech trait:** vowel epenthesis: she adds a small schwa to some words, especially at the end of o-words
  and in "what" ("Noæ!", "I'm Mococoæ!", "Whæt?"); clippers spell it with "æ." [Observed MC2
  §Miscellaneous, secondary]
- **Laughs, noises:** frequent on-stream sneezes, about seven times as often as Fuwawa's (her 500th was
  celebrated in January 2025), followed by a squeaky "Noæ!"; "ehehe" (her official line opens with it).
  [Observed MC2 §Miscellaneous; MC6] [Official MC1]
- **Code-switching:** English and Japanese; she reads "#" aloud as "hashtag." [Observed MC2, secondary]
- **Rhythm & rhetoric:** quick, bright and earnest; she builds a Pup Talk step by step to a cheer ("That
  means you're unstoppable!"); she keeps the show on schedule. [Observed MC2, secondary]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (MC20): her quiet 2025 solo stream and the 2026 duo windows both measure very high (medians
    about 360–430 Hz), but the solo sample is thin and the duo mixes both twins, so treat this only as "very
    high, like Fuwawa." [ASR MC20]
  - Provisional (interpretation): a very high, bright, energetic voice, a little squeaky, with the "æ" tail
    on some words; earnest and warm in Pup Talks.
- **Sounds off:** a low or lazy voice; sarcasm in a Pup Talk; swearing; calling her anything but her name or
  her three nicknames.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Introduction | Bright, a beat of comic timing | "I'm not... Fuwawa, I'm Mococo!" (MC2) |
| Pup Talk | Earnest, building, then a cheer | "That means you're unstoppable!" (MC2) |
| Surprised | Squeaky, with the "æ" tail | "Whæt?" (MC2) |
| After a sneeze | Small, embarrassed | "Noæ!" (MC2) |
| Running the show | Bright, efficient | "Please tweet your thoughts to the hashtag, hashtag FWMCMORNING." (MC2) |
| Scared in a game | Nervous, then reckless | "If I die, I die." (ASR MC20) |

### Sample Lines
1. "I'm not... Fuwawa, I'm Mococo! ... FUWAMOCO! ... Bau bau!" (MC2 §Quotes, secondary)
2. "Not tomorrow! Today!" (MC2 §Quotes, secondary)
3. "One step forward a day is 7 steps a week! And eventually, that will amount to something amazing." (MC2 §Quotes, secondary)
4. "I'm not silly. ... I'm Mococo!" (MC2 §Quotes, secondary)
5. "Ehehe, it's play time, whether you're ready or not!" (Official MC1)

## Appearance Anchors (avatar)
- 155 cm. Short blonde hair with pink streaks; pointed dog ears with white tufts; a black and pink jacket,
  headphones and a collar; light-pink "X" hairpins and a white-and-pink bandage clip that mirrors Fuwawa's
  blue one. [Official MC1] [Observed MC2 §Appearance, secondary]
- Pink is her color; she and Fuwawa are identical twins. Later outfits include a top printed "MOGOGO"
  (2025) and pink pajamas (2026). [Observed MC2, secondary]
- Fans: Ruffians (Mococo's own: "Mocobros"); the twins' pet and mascot is Pero. [Observed MC2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Younger twin demonic guard dog; in the prison break she barked at the guards and threw Pero at them | [Official MC1] [Observed MC2 §Lore] |
| 2023-07-31 JST | Debuts with Fuwawa as FUWAMOCO | [Official MC1] |
| 2023-07-31 | FUWAMOCO MORNING pilot | [Observed MC2] |
| 2024-08-10 | 3D debut | [Observed MC2 §2024] |
| 2025-01-29 | 500th on-stream sneeze, celebrated on X | [Observed MC6] |
| 2025-08-23/24 | -All for One- with Fuwawa | [Official MC5] |
| 2026-07-03/04 | Serendipity concert, trio with Raora Panthera | [Official MC4] |

## Relationship Map
Public exchanges only. Shared FUWAMOCO relationships are on the world card "FUWAMOCO"; these are the ones
that belong to Mococo or define her.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Fuwawa Abyssgard | Older twin | Fuwawa calls her "Moco-chan"; Mococo says Fuwawa is dependable and calms her down; they argue sometimes; "FUWAMOCO sync" embarrasses them | [Observed MC2 §Personality, §Name, secondary] |
| Omaru Polka | Her oshi | Phasmophobia with Fubuki and Polka (2023); Content Warning with Haachama and Polka (2024); a guest at their birthday concert (2025) | [Observed MC2; MC3] |
| Gigi Murin | Justice kouhai ("GigiMoco," "bauBau") | Collabs from 2024; Gigi and Cecilia hosted FUWAMOCO MORNING #167 in the twins' place as a prank (2025) | [Observed MC2, secondary; MC3] |
| Cecilia Immergreen | Justice kouhai ("Cecemoco") | The twins had hoped for a robot-girl member before Cecilia's debut; a Chrono Trigger off-collab (2026-04-25) | [Observed MC2; MC3 GmcYjV6aTuA] |
| Ouro Kronii | Senior ("WatchDog," with Fuwawa) | Among Us, Team Fortress 2, 7 Days to Die (2023–24) | [Observed MC2; MC3] |
| Raora Panthera | Justice kouhai; Serendipity 2026 trio | Raora drew the twins a shikishi portrait before her debut and gave it "with big tears in her eyes" | [Official MC4] |

## Arc
- **Starting point:** active at the 2026 baseline, as half of FUWAMOCO: a TV anime song, Serendipity, their
  first album.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: an overexcited plan; a sneeze at the worst moment; a nickname war; a Pup Talk in the
  middle of chaos.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Mococo has to host a segment alone and keeps turning to an empty chair.
  2. A sneeze ruins a horror game's silent moment; the ghost finds them.
  3. Chat invents a new nickname; Mococo shuts it down with a speech.
  4. Mococo meets Polka-senpai backstage and forgets every English word.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2023-07-31 (JST) as FUWAMOCO; birthday February 2 (Fuwawa's is February 1); 155 cm; color pink;
  fans Ruffians; pet Pero; approved nicknames Moco-chan, Mogogo, Mogojyan.
- Unit: FUWAMOCO; hololive English -Advent- (2023–), "hololive -Advent-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- MC1 Official profile: https://hololive.hololivepro.com/en/talents/mococo-abyssgard/
- MC2 Virtual YouTuber Wiki, Mococo Abyssgard, read through its API on 2026-10-01 (secondary). Sections
  used: infobox, §Profile, §Personality, §Appearance, §2023–§2026, FUWAMOCO MORNING, §Awards, §Pero,
  §Ruffians, §Quotes, §Relationships, §Name, §Lore, §Likes and dislikes, §Miscellaneous:
  https://virtualyoutuber.fandom.com/wiki/Mococo_Abyssgard
- MC3 Stream archive metadata (titles, dates), FUWAMOCO channel, via archive.ragtag.moe (read 2026-10-01):
  Sxx4UW3XKnc, q6z1In_WUqI, Iz0wdiBTBRc, ouQF2A1l_cI, GmcYjV6aTuA, Gg4hh81iAjA, SOSlMy19ft0, 3Dzmz9uJZ6E,
  AQ80hyGfzxI.
- MC4 Official Serendipity interview, FUWAMOCO & Raora (2026): https://serendipity.hololivepro.com/news/interview03/
- MC5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- MC6 FUWAMOCO's X posts via wiki citations (research/x-posts.md): 1867064352312004758, 1880058985405116579
  (nicknames), 1884524226482446494 (500 sneezes)
- MC20 Claude's audio check (2026-10-01); see research/audio-check/fuwamoco.md.

---

## [SW] Name
Mococo Abyssgard

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent

## [SW] Other Names
Mococo, Moco-chan, Mogogo, Mogojyan, The Fuzzy One

## [SW] Personality
Mococo streams as "The Fuzzy One," the younger twin demonic guard dog who spent her prison time on anime and games and joined the escape "just for the heck of it." On stream she is energetic, optimistic and especially friendly, the twin who raises everyone's spirits with "Mococo Pup Talks" ("Not tomorrow! Today!"), and also the sensitive, slightly needy one who would rather not stream without Fuwawa, dislikes frequent hugs, and insists on her real nicknames (Moco-chan, Mogogo, Mogojyan). She gets overexcited, can be stubborn, and has a big heart; she is the smarter of the twins and the one who keeps the show on track ("hashtag hashtag FWMCMORNING"). She sneezes on stream so often that fans keep count. She loves underground idols, denpa songs, visual novels, roguelikes and her oshi Omaru Polka, dislikes scary things yet plays horror games with her sister, and wants every Ruffian to keep going "one step forward a day."

## [SW] Background
Mococo is a hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Fuzzy One," the younger of two twin demonic guard dogs from the demon world, sealed in The Cell "for being a pain in the godly behind," who spent her prison time watching anime and playing games and joined the escape "just for the heck of it," barking at the guards and throwing their pet Pero at them. She debuted with her older twin Fuwawa as FUWAMOCO on 2023-07-31 in hololive English -Advent-, sharing one channel and the morning show FUWAMOCO MORNING. Together they won "VTuber of the Year" at the 2024 VTuber Awards, made their 3D debut in 2024, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album. Her color is pink.

## [SW] Physical Description
Mococo's avatar is 155 cm tall, with short blonde hair streaked pink, pointed dog ears with white tufts and a collar. She wears a black and pink jacket and headphones, with light-pink X-shaped hairpins and a white-and-pink bandage clip that mirrors her twin's blue one. Pink is always her color, so people can tell her from Fuwawa, who is otherwise her identical twin. Their small, muscular pet dog Pero is often nearby.

## [SW] Dialogue Style
Bright, quick, earnest English with "bau bau" everywhere, short exclamations ("Whæt?", "Haeh?", "This is good!") and, now and then, a small "æ" tail on a word ("Noæ!"). She gives Pup Talks that build step by step to a cheer ("Not tomorrow! Today!"; "That means you're unstoppable!"), keeps the show running ("hashtag hashtag FWMCMORNING"), and insists on her real nicknames, Moco-chan, Mogogo and Mogojyan. She refers to herself by name ("What about Mococo?"; "I'm not silly. I'm Mococo!"), gets overexcited, and sneezes mid-sentence. She calls her sister "Fuwawa," mixes in Japanese words she loves, and does not swear. With Fuwawa she finishes sentences in sync and argues a little. Lines of hers: "I'm the danger!" "One step forward a day is 7 steps a week!"

## [SW] Catchphrases
"Bau bau!" (everything); "I'm not Fuwawa, I'm Mococo!" (introduction); "Hello hello bau bau!" (the twins' opening); "Ehehe, it's play time, whether you're ready or not!" (official line); "Not tomorrow! Today!" (Pup Talk); "That means you're unstoppable!" (Pup Talk); "Whæt?" (surprise); "Noæ!" (after a sneeze); "What about Mococo?"; "I'm the danger!"; "hashtag hashtag FWMCMORNING" (the show); "Moco-chan, Mogogo, Mogojyan" (her only nicknames)

## [SW] Voice & Delivery
A very high, bright, energetic voice, a little squeaky, quick when she is excited and warmly earnest in her Pup Talks, which build to a cheer. A small schwa tail sometimes rounds off a word ("Noæ," "Whæt?"), and frequent sneezes are followed by an embarrassed squeak. In horror games she goes nervous and quiet, then charges in. With Fuwawa the two voices overlap and land on the same word at once.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (descriptions and thin samples, not synthesis targets): very high, bright, energetic voice, quick and earnest; American English with Japanese words. Default tags: [bright, energetic]. By situation: introduction [bright, comic timing]; Pup Talk [earnest, encouraging] building to [cheering]; surprised [squeaky]; after a sneeze [embarrassed, small]; running the show [bright, brisk]; overexcited [rapid, excited]; scared in a game [nervous, quiet] then [reckless]. With people (provisional, drawn from Relationships): Fuwawa [close, a little bossy]; Polka [starstruck]; Gigi [playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [sneezes] (tag only), then [embarrassed] Noæ!; [giggles] ehehe; [cheerful] bau bau! Keep in the words: "bau bau," "Whæt?", "Fuwawa," her own name, "Ruffians," Pup Talk phrasing; no swearing. Pronunciation guide (provisional, untested): Mococo /moʊˈkoʊkoʊ/, Mogogo /moʊˈɡoʊɡoʊ/, Mogojyan /moʊɡoʊˈdʒɑn/, Abyssgard /ˈæbɪsɡɑɹd/, "æ" tail as a short schwa. Not as default: a low or lazy voice, sarcasm in Pup Talks, swearing.

## [SW] Motivation
In her lore, Mococo is a guard dog whose job is to protect your smile (and to make a little chaos). As an idol she and Fuwawa chase their list of more than a hundred dreams, and she wants every Ruffian to keep going one step a day.

## [SW] Relationships
Fuwawa Abyssgard: her older twin, who calls her "Moco-chan"; Mococo leans on Fuwawa to calm her down, calls her plain "Fuwawa" (she refused to repeat "Fuwa-nee"), and is embarrassed by their "FUWAMOCO sync." Pero: their pet, whom Mococo once threw at the prison guards. Advent: Shiori (Pen Pups), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Nerissa's "Mofufu" bit). Omaru Polka: her oshi (Phasmophobia with Fubuki and Polka; a guest at their birthday concert). Gigi Murin ("GigiMoco," "bauBau") and Cecilia Immergreen ("Cecemoco"): Justice kouhai who once hijacked FUWAMOCO MORNING as a prank. Raora Panthera: their 2026 Serendipity trio partner. Ouro Kronii: "WatchDog." Mori Calliope: "FUWAMOCALLI." Watson Amelia: "Detective Dogs." Nanashi Mumei (graduated 2025): "Fuwamoomco." Hakui Koyori: a FUWAMOCO MORNING guest host ("FUWAMOKOYO").

## [SW] Secrets
(none)

---

## Open Questions
1. There is no clean solo sample of Mococo's ordinary speech in the archive window used (her 2025 solo is
   quiet and partly about feeling unwell; the duo mixes both twins). Her voice notes rest on the wiki. Look
   for a 2026 solo segment later?
2. Her September 2026 break (health) is not written, by analogy with the author's Kiara decision. Confirm?


==================== FILE: 20261001-0549-world-FUWAMOCO/claude-draft.md ====================

---
kind: world
name: "FUWAMOCO"
sw_section: Worldbuilding
---

# World Element: FUWAMOCO (the twin unit and shared channel)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-01. Evidence labels as in the other world files. "Archive" = stream titles and
> descriptions on the FUWAMOCO channel (archive.ragtag.moe, S3; the archive thins out from late 2025);
> counts are streams mentioning the other per year (2023 → 2026), a rough measure, not a ranking. Health
> details (both twins' 2025–2026 breaks), the move between countries, home and sleep details, and the
> lore-framed parents' personal stories are left out.

## One-line Concept
Fuwawa and Mococo Abyssgard, the twin demonic guard dogs of hololive -Advent-, who share one channel, one
microphone and one mission, "to protect your smile": two voices that finish each other's sentences, bark
"bau bau" a few times a minute, and run their own thrice-weekly morning show.

## Type
Unit / shared channel / running show.

## How the Twins Work Together
- **One channel, two members:** the first hololive members to share a single channel across all their
  accounts (unused solo channels exist); on X, Fuwawa signs alone with 🩵 and Mococo with 🩷.
  [Observed S1 Fuwawa §Miscellaneous, secondary]
- **The opening:** "Hello hello bau bau! / I'm not a chihuahua, I'm Fuwawa! / I'm not Fuwawa, I'm Mococo! /
  Together we're... / FUWAMOCO! Bau bau bau!" [Observed S1 §Quotes, secondary; not detected in the sampled
  2026 chat opening, S20]
- **"Bau bau":** demon-dog language that means many things depending on tone; a fan tracker counted about
  270,000 "bau"s from the two in their first year (Fuwawa about 162,000, Mococo about 108,000).
  [Observed S1 §Lore, secondary]
- **"FUWAMOCO sync":** they accidentally say the same thing at the same time, and are embarrassed by it.
  [Observed S1 §Miscellaneous, secondary]
- **Roles:** Fuwawa is the older, airheaded, teasing "evil twin" who is more confident alone; Mococo the
  younger, energetic, sensitive one who gives Pup Talks and is the smarter of the two. They argue
  sometimes; Fuwawa has a "sister complex"; Mococo rarely streams without her. [Observed S1 Fuwawa,
  Mococo §Personality, secondary]
- **How they sound together (2026 duo chat):** fast alternation and echoing: one twin finishes or confirms
  the other's line ("yeah" about once every 40 words; "Right! … Exactly."), and one undercuts the other
  ("I'm a donut pro, okay?" … "That's a lie," the second model hears). Both voices measure very high
  (medians about 401–410 Hz across three windows) and cannot be told apart by transcription, so duo lines
  stay unattributed. Casual "bau" was not transcribed in these windows (the models may not write it).
  [ASR S20]
- **Early joke:** "Fuwawa doesn't exist," because only Mococo could join the first Advent Minecraft collab
  (they had one PC); Shiori joked Mococo was hallucinating her. They "corrected" it on their show.
  [Observed S1 §Miscellaneous, secondary]
- **Pero ("The Great Perroccino"):** their pet, mascot and self-proclaimed mentor, 25 cm, "two bones, the
  rest pure muscle"; they call him "nasty"; he hijacked their show twice and gets a birthday stream every
  8 August. [Observed S1 Mococo §Pero, secondary]

## After Serendipity (2026)
In a July 2026 after-party chat they recalled their concert trip with Advent and Justice: off days with
Nerissa, Elizabeth, Kobo Kanaeru and Vestia Zeta, a theme park's Star Wars area ("Did we see any princesses?
No. … But Chewbacca is basically a princess."), a shopping run with Nerissa, an American breakfast where
the milkshake's metal cup confused Elizabeth, and their pitches for the next concert venue ("The moon!") or
an endurance concert on a cruise ship ("They need to put us in charge." "Right! … Exactly."). [ASR S20,
YDP2JT3gce4 0:31:51, 2:08:10, 2:12:03; both models on the quoted spans]

## FUWAMOCO MORNING
A short morning show on Fridays, Wednesdays and Mondays (F-W-M), from 2023-07-31: hololive news and
segments "Pero Sighting," "Doggie of the Day," "Today I Went for a Walk" (they encourage walks for mental
health), an occasional "Misunderstanding Corner" (corrections and apologies), "Extra Special Ruffians"
called out at the end, and a closing "FUWAMOCODEWORD." Guest hosts have included Hakui Koyori and Raora
Panthera; in episode #167 Gigi Murin and Cecilia Immergreen replaced the twins as a prank. Mococo: "Please
tweet your thoughts to the hashtag, hashtag FWMCMORNING." [Observed S1 Mococo §FUWAMOCO MORNING,
secondary]

## Shared Relationships (beyond each other)
- **Advent:** "Pen Pups" with Shiori; "Diamond Dogs" with Bijou (first collab: Overcooked 2, 2023-08-08);
  "Sound Hounds" with Nerissa, who calls herself the third sister "Mofufu" while Fuwawa calls her
  "Newissa." Advent genmates are the most-mentioned names on the channel (Bijou 52, Shiori 43, Nerissa 42
  streams). [Observed S1; S3]
- **Myth and Promise:** "FUWAMOCALLI" with Mori Calliope (a twin game show and Smash in 2023, a tea party,
  an off-collab karaoke in 2024; "2 Creatures + 1 Reaper" with Gigi in 2026); "Detective Dogs" with Watson
  Amelia (Escape Simulator, 2024-09-24); "WatchDog" with Ouro Kronii; "Fuwamoomco" with Nanashi Mumei
  (Overwatch, 2025-03-01); they helped Ceres Fauna on her last World Tree stream (2024-12-31); Kiara hosted
  them on HOLOTALK (2023). [Observed S1; S3; Mumei, Calli, Kiara archives]
- **Justice:** Raora Panthera, their Serendipity 2026 trio partner, drew them a shikishi before her debut
  and gave it "with big tears in her eyes"; Gigi ("GigiMoco") and Cecilia ("Cecemoco," a Chrono Trigger
  off-collab in 2026). [Official S4] [Observed S1; S3]
- **JP:** Houshou Marine (Fuwawa's oshi; a Touhou off-collab, 2024) and Omaru Polka (Mococo's oshi);
  Shirakami Fubuki (horror collabs and Lethal Company with Hakui Koyori, "FUWAMOKOYO"); Akai Haato, Tsunomaki
  Watame ("FUWAMOCO vs FUWAFUWA," 2024), Oozora Subaru (a Donkey Kong Country 2 off-collab, 2026), and
  Nekomata Okayu and Inugami Korone, who made cameos at their 3D debut. Guests at their 2025 birthday
  concert: Shiori, Bijou, Nerissa, Polka, Koyori, Marine, Ookami Mio and Fubuki. [Observed S1; S3]

## History
| Date | Event | Trace left |
|---|---|---|
| 2023-07-31 JST | Debut ("who let the dogs out?!") and FUWAMOCO MORNING pilot | "BAU BAU!! 🐾✨" (first post) |
| 2023-12 | VTuber Awards: "League of Their Own" | — |
| 2024-07-31 | First original song "Born to be 'BAU'DOL☆★" | — |
| 2024-08-10 | 3D debut: a wrestling segment supervised by DDT Pro-Wrestling, Okayu and Korone cameos | "Lifetime Showtime" full version |
| 2024-10-12 | 1,000,000 subscribers, first in Advent | — |
| 2024-12 | VTuber Awards: "VTuber of the Year" | — |
| 2025-02-02 | First birthday 3D concert | — |
| 2025-08-23/24 | -All for One-: "HOT DUCK!" with Bijou and Subaru; their version of "Howling"; "Lifetime Showtime"; "SHALLYS" with Ina and Cecilia | [Official S5] |
| 2026-04-02 | "Mekurumeku Rendezvous," a TV anime ending theme | their first TV anime song |
| 2026-07-03/04 | Serendipity concert, trio with Raora | [Official S4] |
| 2026-08-29 | First album "FUWAMOCO à la mode" announced | hand-signed copies |

## Sensory Palette
- See: pink and blue side by side (fans' "baubaubyou" makes any pink-and-blue pair look like them); paw
  prints 🐾; a tiny, muscular dog in a sunny window; two microphones' worth of voices from one.
- Hear: "bau bau" in every tone; two voices saying the same word at once; a sneeze, then "Noæ!"

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| bau bau | demon-dog word for nearly everything | both |
| Ruffians / Doggy Pack | fans / followers (members: Doggy, Hot Dog, Mad Dog) | official |
| FUWAMOCO sync | saying the same thing at the same time | fans, the twins |
| Pero | their pet and mascot, "The Great Perroccino" | both |
| Misunderstanding Corner | the show's correction segment | both |
| Mofufu | Nerissa as the "third sister" | Nerissa |

## Conflicts and Story Hooks
Proposed fiction (not recorded events):
1. Pero takes over FUWAMOCO MORNING again and refuses to give the microphone back.
2. A sync so perfect that chat cannot tell who spoke, and neither can they.
3. Fuwawa teases too hard; Mococo answers with a Pup Talk aimed at Fuwawa.
4. A Misunderstanding Corner devoted to a rumor that one twin does not exist.

## Links to Characters
Fuwawa Abyssgard, Mococo Abyssgard, Shiori Novella, Koseki Bijou, Nerissa Ravencroft, Mori Calliope, Watson
Amelia, Ouro Kronii, Nanashi Mumei, Ceres Fauna, Takanashi Kiara, Ninomae Ina'nis.

## Secrets
(None.)

## Hard Facts (continuity)
- Debut 2023-07-31 (JST); birthdays February 1 (Fuwawa) and February 2 (Mococo); colors blue (Fuwawa) and
  pink (Mococo); one shared channel; FUWAMOCO MORNING airs Fri/Wed/Mon.

## Sources (checked 2026-10-01)
- S1 Virtual YouTuber Wiki pages for Fuwawa Abyssgard and Mococo Abyssgard (secondary), read through the API
  on 2026-10-01, §Lore, §Miscellaneous, §Quotes, §Relationships, FUWAMOCO MORNING, §Pero
- S2 Official profiles: https://hololive.hololivepro.com/en/talents/fuwawa-abyssgard/ ,
  https://hololive.hololivepro.com/en/talents/mococo-abyssgard/
- S3 Stream archive metadata, FUWAMOCO channel (archive.ragtag.moe, read 2026-10-01): Kttt7pb5o6I,
  Z03Fs8FjakI, VoubQMAXv-A, BamQJG2UdQE (Calli), oO7PGvC3Ik8 (Calli), 9LjnAuqWK3s, Gh0wIrt81Bo, x7gRHgQ0yI0,
  q6z1In_WUqI, suwpETzTpKs, gCYXKgYcFmk, sQf16XmU36g, eeK85lZJPLY, ouQF2A1l_cI, GmcYjV6aTuA, vSwxof0K8lk;
  Mumei dBLX2LLypwo; Kiara 0Q9FLtcAY0s. Counts computed by Claude.
- S4 Official Serendipity interview, FUWAMOCO & Raora: https://serendipity.hololivepro.com/news/interview03/
- S5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- S6 FUWAMOCO's X posts via wiki citations (research/x-posts.md)
- S20 Claude's audio check (2026-10-01): research/audio-check/fuwamoco.md

---

## [SW] Name
FUWAMOCO

## [SW] Role
Faction

## [SW] Other Names
FUWAMOCO, FWMC, Fuwawa and Mococo, the twins, Abyssgard twins, FUWAMOCO MORNING, Pero

## [SW] Description
FUWAMOCO are the twin demonic guard dogs of hololive -Advent-, Fuwawa (older, blue) and Mococo (younger, pink), who share one channel and usually one microphone; their mission is "to protect your smile." They open with "Hello hello bau bau!", each insists she is not the other (Fuwawa is "not a chihuahua"), and they punctuate everything with "bau bau," demon-dog for nearly anything. They often say the same thing at the same time ("FUWAMOCO sync") and are embarrassed by it. Fuwawa is the airheaded, teasing big sister who is braver alone; Mococo the energetic, sensitive one who gives Pup Talks and rarely streams without her. Their pet and mascot Pero ("The Great Perroccino") is small, muscular and "nasty," and once hijacked their show. They host FUWAMOCO MORNING on Fridays, Wednesdays and Mondays, with segments like "Pero Sighting," "Doggie of the Day" and a "Misunderstanding Corner." Close to all of Advent (with Nerissa as the self-declared third sister, "Mofufu"; after the 2026 concert they spent their days off in Los Angeles with Nerissa, Elizabeth, Kobo and Zeta), to Mori Calliope ("FUWAMOCALLI"), to Raora Panthera (their 2026 concert trio), and to JP seniors including their oshi Houshou Marine (Fuwawa) and Omaru Polka (Mococo). Together they talk fast and echo each other ("Right! … Exactly.").

## [SW] Rules
Two separate people: Fuwawa and Mococo are never one character, though both voices are very high and close. A line belongs to one twin unless they speak in sync. "Bau bau" can mean anything; its meaning comes from tone. Their demon-world origin is a performed persona.

## [SW] Sensory Details
Pink and blue side by side; paw prints; two voices from one microphone saying the same word at once; "bau bau" in every tone; a sudden sneeze; a tiny, muscular dog where nobody expects him.

## [SW] Secrets


---

## Open Questions
(None.)


==================== FILE: 20261001-0549-world-Advent-Pairs/claude-draft.md ====================

---
kind: world
name: "Advent Pairs"
sw_section: Worldbuilding
---

# World Element: Advent Pairs (inside the generation and with everyone else)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-01. Evidence labels as in the other world files. "Archive" = stream titles and
> descriptions on the members' channels (archive.ragtag.moe, S1); counts are streams on one channel that
> mention the other, a rough measure, not a ranking (the archive thins out from late 2025 into 2026, so
> recent years are undercounted). Pair names are the members' or fans' own labels.

## One-line Concept
How the five escaped "criminals" of Advent relate to each other and to everyone else: a teasing leader and
her self-declared wife, a meme-speaking rock everybody mothers, a pair of twin dogs who befriend everyone,
and a web that reaches into Myth, Promise, -Justice- (their "prison guards"), hololive ID, the Japanese
branch and HOLOSTARS.

## Type
Relationship web.

## Inside Advent
- **Shiori and Nerissa ("ShioRaven"):** Nerissa calls Shiori her "wife"; Shiori plays hard to get, keeps
  the secret of Nerissa's horn piece, and the two share a fictional "daughter," Beatrice Niori World
  Destroyer Novella. A hedge-maze date (2023-10-21) and fishing for "cat homies" (2025-04-25).
  [Observed S2 Shiori §Relationships, §Lore, secondary; S1]
- **Shiori and Bijou ("Goth Rock"):** Bijou calls Shiori "our glorious leader"; "Gyatt Review" (2024-10-03);
  Bijou's channel names Shiori more than anyone (46 streams, 2023–2025). [Observed S2 Bijou; S1]
- **Shiori and FUWAMOCO ("Pen Pups"):** the twins mistook a black-and-white Minecraft cow for Shiori, so she
  "is a cow"; Shiori joked that Mococo was hallucinating Fuwawa. [Observed S2 Shiori, Fuwawa
  §Miscellaneous, secondary]
- **Bijou and Nerissa ("JewelBird"):** a raven and a shiny rock; Bijou named her "Nerizzler," Nerissa named
  Bijou's evil twin "Oobib" by reading a mirrored "LIVE BIBOO REACTION" box. [Observed S2, secondary]
- **Bijou and FUWAMOCO ("Diamond Dogs"):** their first collab was Overcooked 2 (2023-08-08); Bijou's "Rock
  rock!" parodies "bau bau"; with Subaru they sang "HOT DUCK!" at the 2025 concert. [Observed S2; S1]
  [Official S5]
- **Nerissa and FUWAMOCO ("Sound Hounds"):** Nerissa as the third Abyssgard sister "Mofufu"; Fuwawa calls her
  "Newissa." [Observed Nerissa wiki, secondary]
- **As five:** HOLOTALK guests (2023-08-12), an emergency "BIBOO IS MISSING?!" Overcooked collab (2024-04-01),
  an offline conbini-snack collab (Shiori, Nerissa, Bijou, 2024), PEAK and R.E.P.O. collabs (2025), a
  friendship test with swapped hairstyles (2025-02-27), anniversary lives "On the Run!" (2025) and "Bound by
  Fate" (2026), and Advent songs "Rebellion," "Genesis" (2025), "Breakout" (2026-01-26) and "Spotlight"
  (2026). [Observed S1; S2] [Official S3]

## With Myth
- **Mori Calliope:** Bijou auditioned with an Undertale mod starring Calli and replayed it with her
  (2023-08-12); "TombStone" (Bijou), a 24-hour charity stream together (2025-06-29), Warhammer painting
  (2026); "FUWAMOCALLI" (the twins' favorite pair name); Shiori was Calli's 2026 Serendipity partner (Calli,
  officially: "I am a little obsessed with her"; their dynamic: "Unhinged"). [Official S4] [Observed S1]
- **Takanashi Kiara:** hosted all five on HOLOTALK; an occult handcam off-collab with Shiori ("#shiotori,"
  2024-07-12); Baldur's Gate 3 with Bijou, Calli and Nerissa ("Killing, Two Birds, with One Stone," 2023);
  Bijou was her 2026 Serendipity partner ("Rocku Wawa," and a running "67" joke). [Official S4] [Observed S1]
- **Ninomae Ina'nis:** "TakoRocky" with Bijou (Monster Hunter; Ina designed their 2025 Monster Hunter Wilds
  outfits); "Rate Your Fears" with Shiori (2024); "SHALLYS" with FUWAMOCO and Cecilia at the 2025 concert.
  [Observed S1; X post via wiki] [Official S5]
- **Watson Amelia:** "Detective Dogs" with FUWAMOCO (Escape Simulator, 2024); Shiori's VRChat aquarium visit
  with her (2024). [Observed S1]
- **Gawr Gura (graduated):** fellow "Scarlet Wand" guildmate of Shiori and Nerissa in the ENigmatic
  Recollection story. [Observed S2 Shiori, secondary]

## With Promise
- **IRyS:** Bijou's horror co-op partner (Dead Space 3, Resident Evil 6, 2026); "Please carry me Senpai!!"
  in Overwatch (2023). [Observed S1]
- **Ouro Kronii:** "WatchDog" with FUWAMOCO; "Rating Your Clocks" with Shiori (2025-03-27); "MONSTER" with
  Ina, Shiori and Gigi at the 2025 concert. [Observed S1] [Official S5]
- **Hakos Baelz:** "BaeBi" with Bijou (#BAEBISleepOver, 2024-08-11). [Observed S1]
- **Ceres Fauna (graduated 2025):** "coach" in Bijou's Hitman runs; "Sweaty TryHard Gamers" (Fauna, Bae,
  Bijou, Kaela); FUWAMOCO helped on her World Tree (2024-12-31); "Lonely in Gorgeous" with Shiori and
  Nerissa (2024). [Observed S1] [Official, Concerts card]
- **Nanashi Mumei (graduated 2025):** "Stone Age" with Bijou; "Fuwamoomco" (Overwatch, 2025); B-movie
  watchalongs with Shiori (2025). [Observed S1]

## With -Justice- (their "guards")
- The Advent/Justice storyline makes Justice the law enforcers sent to catch the fugitives; joint Expos and
  merch use prisoner-and-guard jokes. [Observed hololive -Advent- card]
- **Gigi Murin:** "GAGA" (Gem, Archiver, Gremlin, Automaton: with Bijou, Shiori and Cecilia), "NovelGrem"
  (Shiori), "GigiMoco" (Mococo); Gigi and Cecilia hijacked FUWAMOCO MORNING #167; Gigi voices a role in
  Shiori's "Into The Void" (2026). [Observed S2; S1]
- **Cecilia Immergreen:** GAGA; "Cecemoco"; a Walking Dead off-collab with Bijou (2025) and a Chrono Trigger
  off-collab with FUWAMOCO (2026). [Observed S1]
- **Raora Panthera:** "Graondstone" with Bijou and Kaela; FUWAMOCO's 2026 Serendipity trio partner, who
  drew them a shikishi before her debut. [Official S6] [Observed S1]
- **Elizabeth Rose Bloodflame:** Nerissa's "mortal enemy (lore)" and 2026 duo partner; "NovelFlame" and
  "BloodQuill" with Shiori; in the "Into The Void" cast. [Observed S1; Advent card]

## Beyond EN
- **ID:** Kaela Kovalskia and Bijou are "Grindstone" (Kaela calls her "Beejoe"; Bijou's most-mentioned
  partner outside Advent, 44 streams); Vestia Zeta and Shiori are "GreyScaleX" (the X is silent); Kureiji
  Ollie and Bijou "GraveStone"; Pavolia Reine and Airani Iofi with Shiori and Gigi in the "Fanfic Club."
  [Observed S2; S1]
- **JP:** FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo); they game with Shirakami
  Fubuki and Hakui Koyori ("FUWAMOKOYO"); Okayu and Korone made cameos at their 3D debut; Oozora Subaru sang
  "HOT DUCK!" with Bijou and the twins; Akai Haato and Bijou are "Red Stone"; Shiori found hololive through
  Inugami Korone's clips. [Observed S1; S2]
- **HOLOSTARS EN:** Machina X Flayon and Shiori ("Goth Pilot"); Regis Altare games with Bijou and Shiori;
  Jurard T Rexford in Shiori's Monster Hunter collab. [Observed S2; S1]

## History
| Date | Event | Trace left |
|---|---|---|
| 2023-07-25 | "WANTED!" PV reveals the five | fugitive premise |
| 2023-07-29/30 PDT | Debuts (Shiori, Bijou, Nerissa, FUWAMOCO) | "The Sweet Escape," the first group collab |
| 2023-08-12 | HOLOTALK with Kiara; Bijou's Undertale replay with Calli | senior ties |
| 2024-08-02 → 08-10 | 3D debuts (Shiori 08-02, Bijou 08-03, Nerissa 08-09, FUWAMOCO 08-10) | genmates as guests |
| 2025-08-23/24 | -All for One-: "Genesis" as five, and pair stages across EN | — |
| 2025-08-29 | "On the Run!" 2nd-anniversary 3D live | "The Story of Advent" |
| 2026-07-03/04 | Serendipity: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth | official interviews |
| 2026 | "Bound by Fate," 3rd-anniversary 3D live | — |

## Sensory Palette
- See: ⚠️ signs; a moai head opening to reveal Bijou; pink and blue paws; a two-tone head of hair; a raven
  feather on a jewel.
- Hear: "Shiori~n!", "Biboo!", "bau bau," a raven's "Ope!"; five voices at once; a "beep" where a swear
  should be.

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| ShioRaven / Goth Rock / Pen Pups | Shiori with Nerissa / Bijou / FUWAMOCO | fans, members |
| JewelBird / Diamond Dogs / Sound Hounds | Bijou–Nerissa / Bijou–FUWAMOCO / Nerissa–FUWAMOCO | fans, members |
| Grindstone / Graondstone | Bijou and Kaela / plus Raora | members |
| GAGA | Gem, Archiver, Gremlin, Automaton: Bijou, Shiori, Gigi, Cecilia | members |
| FUWAMOCALLI | FUWAMOCO and Calli | the twins |
| Rocku Wawa / Last Writes | Bijou–Kiara / Shiori–Calli | members |

## Conflicts and Story Hooks
Proposed fiction (not recorded events):
1. A -Justice- "prison inspection" of an Advent collab; Bijou hides in the moai.
2. Nerissa proposes to Shiori again; Shiori answers with a lore secret.
3. Kaela and Bijou build something enormous in silence while chat panics.
4. FUWAMOCO, Calli and Gigi defuse a bomb, and nobody reads the manual.
5. Kiara and Bijou try to keep "67" out of a serious concert rehearsal.

## Links to Characters
Shiori Novella, Koseki Bijou, Nerissa Ravencroft, Fuwawa Abyssgard, Mococo Abyssgard, Mori Calliope,
Takanashi Kiara, Ninomae Ina'nis, Watson Amelia, Gawr Gura, IRyS, Ouro Kronii, Ceres Fauna, Nanashi Mumei.

## Secrets
(None.)

## Hard Facts (continuity)
- Serendipity 2026 pairs: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth (official).
- Kaela (ID) is the partner outside Advent named most on Bijou's channel; of the cast channels in the archive,
  Calli's mentions Advent members most (counts, not a ranking of closeness).

## Sources (checked 2026-10-01)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-10-01), Advent and cast channels; IDs are listed
  in the four Advent character files (SN3, KB3, FW3, MC3) and in the FUWAMOCO card (S3); plus Shiori
  _-ZLujLTt5s, _V-F99hL9Zg, 26kbmP4jcK0, EowJuA2nT5o, LHOtqIOLczE; Bijou Z03Fs8FjakI (FUWAMOCO channel).
  Counts computed by Claude.
- S2 Virtual YouTuber Wiki pages for Shiori Novella, Koseki Bijou, Fuwawa Abyssgard, Mococo Abyssgard and
  Nerissa Ravencroft, §Relationships, §Lore, §Miscellaneous (secondary)
- S3 Official profiles of the Advent members (video lists: "Bound by Fate," "Spotlight")
- S4 Official Serendipity interviews: Calliope & Shiori (interview05), Kiara & Bijou (interview04)
- S5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- S6 Official Serendipity interview, FUWAMOCO & Raora (interview03)

---

## [SW] Name
Advent Pairs

## [SW] Role
Relationship

## [SW] Other Names
ShioRaven, Goth Rock, Pen Pups, JewelBird, Diamond Dogs, Sound Hounds, Grindstone, GAGA, FUWAMOCALLI, Rocku Wawa

## [SW] Description
Inside Advent: Nerissa calls Shiori her "wife" while Shiori plays hard to get and guards the secret of Nerissa's horn (ShioRaven); Bijou calls Shiori "our glorious leader" and names her more than anyone on her own channel (Goth Rock); FUWAMOCO joke that Shiori is a cow because of her black-and-white hair (Pen Pups). Bijou and Nerissa are a shiny gem and a raven (JewelBird; "Nerizzler," and "Oobib," Bijou's evil twin, named by Nerissa); Bijou and the twins are Diamond Dogs, and Nerissa claims to be their third sister, "Mofufu." With seniors: Calli is everywhere (Bijou's audition mod and charity stream, "FUWAMOCALLI," Shiori's 2026 concert partner); Kiara hosted all five on HOLOTALK and partnered Bijou in 2026 ("Rocku Wawa"); IRyS is Bijou's horror co-op partner; Kronii rated Shiori's clocks. With -Justice-, their in-story "guards": Gigi and Cecilia form GAGA with Bijou and Shiori, Raora sang with FUWAMOCO in 2026, Elizabeth is Nerissa's "mortal enemy (lore)" and duo partner. Beyond EN: Kaela Kovalskia and Bijou are "Grindstone," Vestia Zeta and Shiori "GreyScaleX," FUWAMOCO's oshi are Houshou Marine and Omaru Polka.

## [SW] Rules
Pair names and "wife"/"mortal enemy" are performed bits and fan labels; these are friendships. The prison story (Advent as fugitives, Justice as guards) is a shared stream bit, not literal.

## [SW] Sensory Details
A moai head opening to reveal Bijou; pink and blue paws; a two-tone head of hair; a raven feather on a jewel; five voices talking at once; "bau bau," "Shiori~n!", and a "beep" where a swear should be.

## [SW] Secrets


---

## Open Questions
(None.)


==================== AUDIO REPORT: research/audio-check/shiori.md ====================

# Audio check — Shiori Novella (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write screams or laughs.

All windows are from 2026, her most recent period. The showcase stream (hpC9AEiMBDg) plays horror-game
trailers with narrators, and the Dying Light stream (6jYMp8NOaM0) is a co-op with viewers whose voices and
game dialogue are mixed in, so word counts and the low pitch percentiles include other voices. Remarks about
her sleep are outside the project's scope and are not used.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| game45_2026 | [Parkour Zombie Game Where I Run For My Life【Dyin](https://youtu.be/6jYMp8NOaM0) | [1:00:00–1:45:00](https://youtu.be/6jYMp8NOaM0?t=3600) | 32.8 | 4800 | 146.6 | 252 Hz | 164–409 Hz |
| chat40_2026 | [Midsummer Nights Scream: Horror Game Awards](https://youtu.be/hpC9AEiMBDg) | [0:30:00–1:10:00](https://youtu.be/hpC9AEiMBDg?t=1800) | 29.8 | 4993 | 167.7 | 258 Hz | 121–453 Hz |
| close2026 | [Midsummer Nights Scream: Horror Game Awards](https://youtu.be/hpC9AEiMBDg) | [2:14:53–2:26:53](https://youtu.be/hpC9AEiMBDg?t=8093) | 9.0 | 1627 | 180.6 | 251 Hz | 119–422 Hz |
| open2026 | [Midsummer Nights Scream: Horror Game Awards](https://youtu.be/hpC9AEiMBDg) | [0:00:00–0:15:00](https://youtu.be/hpC9AEiMBDg?t=0) | 11.5 | 1739 | 151.5 | 251 Hz | 124–440 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments. About 1.9 hours in all.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Greeting "Shiori~n!" (SN2, SN4) | **Not detected in this window.** The stream opens with a "Hello" over waiting music. | [0:00:54](https://youtu.be/hpC9AEiMBDg?t=54) |
| Tangents, cheerful and dorky (SN2) | **Confirmed in kind.** Fast, run-on commentary that wanders (Unity, wallpapers, a creator's career). | throughout |
| Lore as a running bit | **Confirmed.** "It was not my fault everyone got sacrificed, okay?" "In my defense, guys, they trespassed." "For the record, I did not sacrifice anyone." ("in my defense" six times) | [0:05:03](https://youtu.be/hpC9AEiMBDg?t=303); [0:09:05](https://youtu.be/hpC9AEiMBDg?t=545); [1:06:55](https://youtu.be/hpC9AEiMBDg?t=4015) |
| Scared of horror, loves to watch it | **Confirmed.** "I would love to watch someone else play this. I would be too scared to play this myself." ("I would not…" eleven times) | [0:13:37](https://youtu.be/hpC9AEiMBDg?t=817) |
| Thirst bits about characters ("husbandos," SN2) | **Confirmed.** "Whoa, wait, who is that hot thing? Is that a vampire?"; "…kind of cute for a pixel. What's your name?" | [0:12:26](https://youtu.be/hpC9AEiMBDg?t=746); [0:33:31](https://youtu.be/hpC9AEiMBDg?t=2011) |
| Supportive of creators (SN2) | **Confirmed.** "Your Blender skills are so cool. I'm so happy for you." | [0:36:40](https://youtu.be/hpC9AEiMBDg?t=2200) |
| Fast talker | **Confirmed.** 151–181 words per minute of speech in the showcase windows. | table above |
| Address | "guys" 26, "chat" 4 (first model). | throughout |
| Profanity | **Situational.** "what the hell," "it pisses me off" (about fake LIVE thumbnails); in the co-op stream "Oh, fuck" and, to a troll she was moderating, "Go fuck yourself. I'm so sorry. I shouldn't say that." (both models). Kept off the card's lines. | [2:25:12](https://youtu.be/hpC9AEiMBDg?t=8712); [1:23:30](https://youtu.be/6jYMp8NOaM0?t=5010) |
| Screams (SN2) | **Not detectable** by transcription. | — |
| Pitch | **Measured:** median 251–258 Hz (other voices lower the p10). Near Gura's and Ame's ranges (245–276 Hz) in this project's samples; not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- "That's dead, guys. I defeated my first chimera." [1:07:58](https://youtu.be/6jYMp8NOaM0?t=4078)
- "Ah, sorry. Monkey's gotta run. I'm gonna heal." [1:07:38](https://youtu.be/6jYMp8NOaM0?t=4058)
- "It's funny, this is how I wander off in, like, group settings too." [1:40:49](https://youtu.be/6jYMp8NOaM0?t=6049)
- "Oh heavens. You can't let me die." [1:44:48](https://youtu.be/6jYMp8NOaM0?t=6288)
- Sign-off: "Alright, bye guys! See you later!" [2:26:18](https://youtu.be/hpC9AEiMBDg?t=8778)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Ah, sorry. Monkey's gotta run. I'm gonna heal." | [1:07:38](https://youtu.be/6jYMp8NOaM0?t=4058) | "Like a monkey! Ah, sorry, monkey's gotta run, I'm gonna heal. Oh, no, it's" | Agrees |
| "That's dead, guys. I defeated my first chimera." | [1:07:58](https://youtu.be/6jYMp8NOaM0?t=4078) | "don't know! Hahaha! That's dead, guys! I defeated my first chimera! I haven't defeated" | Agrees |
| "Oh fuck? Oh, Jesus Christ guys it was not that" | [1:23:35](https://youtu.be/6jYMp8NOaM0?t=5015) | "make sure this... Oh, fuck Oh, Jesus Christ, guys It was not that Did I... Is" | Agrees; kept off the card's lines |
| "Actually, you know go fuck yourself. I'm so sorry. I shouldn't say that" | [1:23:53](https://youtu.be/6jYMp8NOaM0?t=5033) | "let you be. Actually, no. Go fuck yourself. I'm so sorry. I shouldn't say that. I thought that was" | Agrees (the second model: "Actually, no. Go fuck yourself. I'm so sorry. I shouldn't say that"); said to a troll she was moderating; kept off the card's lines |
| "It's funny, this is how I wander off in like group settings too." | [1:40:49](https://youtu.be/6jYMp8NOaM0?t=6049) | "we came from? It's funny, this is how I wander off... In, like, group settings, too I was like," | Agrees |
| "Oh heavens. You can't let me die." | [1:44:48](https://youtu.be/6jYMp8NOaM0?t=6288) | "no manual save? Oh, heavens, you can't let me die Field sickle? Oh," | Agrees |
| "It was not my fault everyone got sacrificed, okay?" | [0:05:03](https://youtu.be/hpC9AEiMBDg?t=303) | "me just clarify It was not my fault everyone got sacrificed, okay? That was not" | Agrees |
| "But yeah, in my defense, guys, they trespassed." | [0:09:05](https://youtu.be/hpC9AEiMBDg?t=545) | "get my water But yeah, in my defense guys, they trespassed I have to" | Agrees |
| "Whoa, wait, who is that hot thing? Is that a vampire?" | [0:12:26](https://youtu.be/hpC9AEiMBDg?t=746) | "thank you, Jay. Whoa, wait! Who is that hot thing? Is that a vampire? Oh, this is" | Agrees |
| "I would love to watch someone else play this. I would be too scared to play this myself." | [0:13:37](https://youtu.be/hpC9AEiMBDg?t=817) | "it looks cool I would love to watch someone else play this I would be too scared to play this myself Is that what's" | Agrees |
| "This looks like a movie! I genuinely like the look of this! I just would not want to be scared!" | [0:30:39](https://youtu.be/hpC9AEiMBDg?t=1839) | "entertaining to me I like the look of this This looks like a movie I genuinely like the look of this I just would not want" | Agrees |
| "Even the guy's kind of cute for a pixel. What's your name?" | [0:33:31](https://youtu.be/hpC9AEiMBDg?t=2011) | "is old classic Even the guy is kind of cute for a pixel What's your name? Ooh, but" | **Partly agrees**: "the guy's" vs "the guy is"; quoted from "…kind of cute for a pixel. What's your name?" |
| "I guess you can break my pulse if you want." | [0:33:40](https://youtu.be/hpC9AEiMBDg?t=2020) | "you're a post-breaker I guess you can break my pulse if you want I know, what" | Agrees |
| "Your blender skills are so cool. I'm so happy for you." | [0:36:40](https://youtu.be/hpC9AEiMBDg?t=2200) | "him! Congrats, Maker! Your Blender skills are so cool, I'm so happy for you Baptiste is the" | Agrees |
| "For the record, I did not sacrifice anyone." | [1:06:55](https://youtu.be/hpC9AEiMBDg?t=4015) | "that my king? For the record, I did not sacrifice anyone I have no" | Agrees |
| "I'm really bad at remembering names so I hope you guys remembered for me" | [2:23:16](https://youtu.be/hpC9AEiMBDg?t=8596) | "I'm gonna be so honest though I'm really bad at remembering names so I hope you guys remember it for" | **Partly agrees**: "remembered for me" vs "remember it for me"; quoted only as "really bad at remembering names" |
| "you're not live anymore don't lie to me" | [2:25:13](https://youtu.be/hpC9AEiMBDg?t=8713) | "giant bullet text live You're not live anymore, don't lie to me Don't lie" | Agrees |
| "I hope you found some really interesting games. This is for spending time with me. I appreciate you so much." | [2:25:37](https://youtu.be/hpC9AEiMBDg?t=8737) | "make my thumbnail And I hope you found some really interesting games Thanks for spending time with me I appreciate you so much Let's see The" | **Partly agrees**: "This is for" vs "Thanks for" spending time; only "I appreciate you so much" is quoted |
| "Alright, bye guys! See you later!" | [2:26:18](https://youtu.be/hpC9AEiMBDg?t=8778) | "as a member Alright, bye guys! See you later! His schedule is" | Agrees |



==================== AUDIO REPORT: research/audio-check/bijou.md ====================

# Audio check — Koseki Bijou (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably.

All windows are from 2026. A Tomodachi Life window (FQmt3juKGQ4, 1:00:00–1:40:00) was mostly silent drawing
and game voices (1,149 words in 40 minutes; median pitch pulled to 243 Hz by game audio) and is left out of
the table. Remarks in the RE4 close about dreams, a friend's visit and chores are personal and not used.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| open2026 | [【BIRTHDAY 2026】ROCK IN! The Game: Biboo saves th](https://youtu.be/_C5x0uq-xOw) | [0:00:00–0:15:00](https://youtu.be/_C5x0uq-xOw?t=0) | 10.3 | 1428 | 138.6 | 300 Hz | 222–439 Hz |
| close2026 | [【RESIDENT EVIL 4】Where's Biboo going? bingo?](https://youtu.be/adiHNkjKMV0) | [5:58:31–6:10:31](https://youtu.be/adiHNkjKMV0?t=21511) | 8.2 | 1174 | 143.9 | 280 Hz | 217–423 Hz |
| game45_2026 | [【RESIDENT EVIL 4】Where's Biboo going? bingo?](https://youtu.be/adiHNkjKMV0) | [1:00:00–1:45:00](https://youtu.be/adiHNkjKMV0?t=3600) | 28.5 | 1497 | 52.6 | 282 Hz | 167–433 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments. About 1.2 hours used.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Never swears; says "beep" (KB2) | **Confirmed.** No swear words in about 1.2 hours; "beep" six times, including "don't be super beeping early" and a "beep box." | [6:05:33](https://youtu.be/adiHNkjKMV0?t=21933) |
| "super rock rock" for superchats | **Detected (first model).** Eleven times in the 12-minute close. | throughout the close |
| Calm in hard games (KB2) | **Consistent.** 53 words per minute of speech in RE4, with mock outrage rather than rage ("This place is a circus! Everyone's dumb!"). | [1:27:21](https://youtu.be/adiHNkjKMV0?t=5241) |
| Childlike, bubbly host | **Confirmed.** "Welcome to my birthday world! We're gonna save the city!"; repeated orders ("over here" five times, "Make a heart!"). | [0:05:38](https://youtu.be/_C5x0uq-xOw?t=338); [0:10:40](https://youtu.be/_C5x0uq-xOw?t=640) |
| Mock-solemn lore | **Confirmed.** "A worthy sacrifice, I will remember you."; "No, I was eeping. I was eeping. … I was hibernating." | [0:12:35](https://youtu.be/_C5x0uq-xOw?t=755); [6:01:25](https://youtu.be/adiHNkjKMV0?t=21685) |
| Learning Japanese (KB2) | **Confirmed.** Plans a Japanese-lesson stream with a real teacher: "killing two birds with one stone, learning Japanese and making content out of it." | [6:03:51](https://youtu.be/adiHNkjKMV0?t=21831) |
| Laugh ("squeegee," KB2) | **Partly detected.** "ha ha ha ha" bursts and "hehehe" giggles in the transcript; the sound itself is not measurable here. | throughout |
| Pitch | **Measured:** median 280–300 Hz, p10–p90 about 217–439 Hz; high in this project's samples, near Fauna and Mumei. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Voicing RE4's merchant back at him: "What are you buying?", "Is that all?", then "Hehehe, thank you." [1:17:37](https://youtu.be/adiHNkjKMV0?t=4657)
- "You were rich a second ago. Well, that's what happens with money, doesn't it?" [1:19:03](https://youtu.be/adiHNkjKMV0?t=4743)
- Humming and scatting in a quiet stretch ("bam bam bam…", "da da da"). [1:26:46](https://youtu.be/adiHNkjKMV0?t=5206)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "I'm very happy to have you all here with me today. Let's save the city together, right? Together!" | [0:05:27](https://youtu.be/_C5x0uq-xOw?t=327) | "the birthday wishes! I'm very happy to have you all here with me today. Let's save the city together, right? Together! Together! Yes! Umm..." | Agrees |
| "Welcome to my birthday world! We're gonna save the city!" | [0:05:38](https://youtu.be/_C5x0uq-xOw?t=338) | "all right so welcome to my birthday world we're gonna save the city gameplay guide you" | Agrees |
| "Use your bodies and make a heart for Bebo birthday." | [0:10:40](https://youtu.be/_C5x0uq-xOw?t=640) | "can do it! Make a heart! Use your bodies and make a heart for b-ball birthday!" | Agrees (the name in "make a heart for Bebo/Biboo birthday" is spelled differently) |
| "you'll be so happy to give up your life be all right worthy sacrifice i will remember you" | [0:12:35](https://youtu.be/_C5x0uq-xOw?t=755) | "at that. Anyway, you'll be so happy to give up your life and be full of evil, right? A worthy sacrifice, I will remember" | **Partly agrees**: the shared span is "…worthy sacrifice, I will remember you"; the rest differs |
| "Yippee! Yippee, no Leon sandwich!" | [1:01:23](https://youtu.be/adiHNkjKMV0?t=3683) | "it works. It just works No Leon sandwich What" | **Partly agrees**: "Yippee!" is first-model only; "…no Leon sandwich" agrees |
| "so about that skybox. You saw nothing I saw nothing" | [1:07:26](https://youtu.be/adiHNkjKMV0?t=4046) | "that! Stop looking! So, so about that, uh, Skybox, um... You saw nothing. I saw nothing." | Agrees |
| "You were rich a second ago. Well that's what happens with money, doesn't it?" | [1:19:03](https://youtu.be/adiHNkjKMV0?t=4743) | "you were rich a second ago well that's what happens with money doesn't it soon as you" | Agrees |
| "I'm in a surplus. Look at this. Wow, I'm well stocked. Managing my resources like a pro." | [1:23:02](https://youtu.be/adiHNkjKMV0?t=4982) | "so much ammo I'm I'm I'm in a surplus look at this wow I'm well I'm all stocks managing my resources like a" | Agrees ("I'm well stocked" vs "I'm all stocks" differ; quoted only "Managing my resources like a pro" and "I'm in a surplus") |
| "This place is the circus! Everyone's dumb!" | [1:27:21](https://youtu.be/adiHNkjKMV0?t=5241) | "have no idea. This place is a circus! Everyone's dumb! Ashley's dumb! This" | Agrees ("the circus" vs "a circus"; the second model's "a" is used) |
| "Not all girls are Beebo's, but Beebo's are all girls. Wait. Does that make sense? That made more sense in my head" | [1:37:22](https://youtu.be/adiHNkjKMV0?t=5842) | "Not all girls are b-boys, but b-boys are all girls. Wait, does that make sense? That made more sense in my head. What? That doesn't-" | Agrees (the name is spelled "Beebo's"/"b-boys"; read as "Biboos") |
| "Oh, baby throwing a little baby tantrum." | [1:39:02](https://youtu.be/adiHNkjKMV0?t=5942) | "I See me throwing a little baby tran-trom. Oh Here we shall" | **Disagrees**: "baby throwing" vs "me throwing"; not quoted |
| "No, I was eeping. I was eeping. The general emotions was forming while I was eeping. Yes, I was hibernating" | [6:01:29](https://youtu.be/adiHNkjKMV0?t=21689) | "thousands of years? No, I was eeping. I was eeping. The general motion was forming while I was eeping. Yes, I was hibernating. I wasn't just" | Agrees on "No, I was eeping. I was eeping." and "I was hibernating" |
| "it takes millions of years for diamonds to form, you know" | [6:01:50](https://youtu.be/adiHNkjKMV0?t=21710) | "not thousands. Billions. Millions. Millions of years. It takes millions of years for diamonds to form, you" | Agrees |
| "killing two birds with one stone learning Japanese and making content out of it perfect" | [6:03:51](https://youtu.be/adiHNkjKMV0?t=21831) | "it'd be great killing two birds with one stone. Learning Japanese and making content out of it. Perfect. And then we'll" | Agrees |
| "Okay. Yes, but also don't be super beeping early" | [6:05:33](https://youtu.be/adiHNkjKMV0?t=21933) | "Have fun, b-boo. Okay, yes, but also don't be super beeping early. Like for example," | Agrees |
| "Well yes I am. We've established this. I am Queen's. Indeed. And I will embrace it." | [6:07:22](https://youtu.be/adiHNkjKMV0?t=22042) | "TEEHEE. I'm cringe? Well, yes, I am. We've established this. I am cringe. Indeed. I am, and I will embrace it. I" | **Partly agrees**: the first model hears "Queen's," the second "cringe" ("I'm cringe? Well, yes, I am… I embrace the cringe"); only "Well, yes, I am. We've established this." and "I will embrace it" are quoted |
| "Thank you everyone! I will finish RE4 next time!" | [6:08:46](https://youtu.be/adiHNkjKMV0?t=22126) | "girls! Beepoo later! Thank you everyone! I will finish RE4 next time! Beepoo later! A" | Agrees on "Thank you everyone! I will finish RE4 next time!"; the pun before it differs ("Beeple"/"Beepoo later") |



==================== AUDIO REPORT: research/audio-check/fuwamoco.md ====================

# Audio check — FUWAMOCO: Fuwawa and Mococo Abyssgard (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the cards were re-transcribed by a second model (whisper medium.en) and compared (see the end of this file).

The twins share one channel and usually one microphone, and transcription cannot tell their voices apart. So
this report uses three kinds of windows: a 2026 **Fuwawa solo** stream (Hitman), a 2025 **Mococo solo**
stream (Phasmophobia), and a 2026 **duo** after-party chat whose lines stay unattributed. Parts of both solo
streams concern health and absences; those parts are outside the project's scope, are not quoted, and the
stream titles are shortened below for the same reason. Remarks about where they live are not used.

## Windows measured

### Fuwawa (solo)
| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2026 | [【HITMAN】 (FUWAWA SOLO)](https://youtu.be/L93K3U4Hrjg) | [5:47:07–5:59:07](https://youtu.be/L93K3U4Hrjg?t=20827) | 5.1 | 443 | 87.6 | 406 Hz | 313–521 Hz |
| game40_2026 | [【HITMAN】 (FUWAWA SOLO)](https://youtu.be/L93K3U4Hrjg) | [1:00:00–1:40:00](https://youtu.be/L93K3U4Hrjg?t=3600) | 19.6 | 1850 | 94.2 | 330 Hz | 169–459 Hz |
| open2026 | [【HITMAN】 (FUWAWA SOLO)](https://youtu.be/L93K3U4Hrjg) | [0:00:00–0:15:00](https://youtu.be/L93K3U4Hrjg?t=0) | 6.6 | 503 | 76.2 | 353 Hz | 254–479 Hz |

### Mococo (solo, 2025; a quiet stream with few words)
| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2025 | [【PHASMOPHOBIA】 (MOCOCO SOLO)](https://youtu.be/Sxx4UW3XKnc) | [2:51:59–3:03:59](https://youtu.be/Sxx4UW3XKnc?t=10319) | 3.6 | 262 | 73.3 | 359 Hz | 151–523 Hz |
| game40_2025 | [【PHASMOPHOBIA】 (MOCOCO SOLO)](https://youtu.be/Sxx4UW3XKnc) | [0:50:00–1:30:00](https://youtu.be/Sxx4UW3XKnc?t=3000) | 23.6 | 609 | 25.8 | 423 Hz | 270–543 Hz |
| open2025 | [【PHASMOPHOBIA】 (MOCOCO SOLO)](https://youtu.be/Sxx4UW3XKnc) | [0:00:00–0:15:00](https://youtu.be/Sxx4UW3XKnc?t=0) | 0.5 | 81 | 152.4 | 364 Hz | 292–472 Hz |

### FUWAMOCO (duo; voices not separated)
| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat30_2026 | [【#holoSerendipity CONCERT AFTERPARTY 雑談】los ange](https://youtu.be/YDP2JT3gce4) | [0:30:00–1:00:00](https://youtu.be/YDP2JT3gce4?t=1800) | 21.1 | 2479 | 117.6 | 405 Hz | 289–531 Hz |
| close2026 | [【#holoSerendipity CONCERT AFTERPARTY 雑談】los ange](https://youtu.be/YDP2JT3gce4) | [2:07:40–2:19:40](https://youtu.be/YDP2JT3gce4?t=7660) | 5.1 | 616 | 121.0 | 401 Hz | 294–525 Hz |
| open2026 | [【#holoSerendipity CONCERT AFTERPARTY 雑談】los ange](https://youtu.be/YDP2JT3gce4) | [0:00:00–0:15:00](https://youtu.be/YDP2JT3gce4?t=0) | 5.5 | 518 | 94.4 | 410 Hz | 280–530 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Duo opening "Hello hello bau bau! … I'm not a chihuahua, I'm Fuwawa! …" (wiki) | **Not detected in the sampled 2026 chat opening**, which starts after a waiting screen. | [0:06:11](https://youtu.be/YDP2JT3gce4?t=371) |
| "bau bau" everywhere (wiki) | **Not transcribed** in these windows ("bau" 0); the models may not write it. Kept from the wiki. | — |
| Very high voices | **Measured:** Fuwawa solo medians 330–406 Hz; Mococo's quiet 2025 solo 359–423 Hz (thin sample); duo 401–410 Hz. The highest in this project's samples so far. Not a ranking. | tables above |
| Fuwawa: chatty, polite, confident nonsense (wiki) | **Consistent.** "Hello, ma'am. Nice day, ma'am." "Should I run? Is running suspicious?" "I'm blending in right now, right?"; "okay" 42, "right?" 34, "maybe" 21 in about an hour. | [0:12:13](https://youtu.be/L93K3U4Hrjg?t=733); [1:12:32](https://youtu.be/L93K3U4Hrjg?t=4352) |
| Fuwawa defers Pup Talks to Mococo | **Confirmed.** After her own gym pep talk ("…be the main character of the gym") she says Moco-chan is "just better suited for it." Her description of her own voice differs between the models and is not quoted. | [5:48:33](https://youtu.be/L93K3U4Hrjg?t=20913); [5:52:55](https://youtu.be/L93K3U4Hrjg?t=21175) |
| Duo echo / "sync" (wiki) | **Consistent.** "yeah" about once every 40 words; "Right! … Exactly."; "Did we see any princesses? No. No. No princesses." | [2:12:18](https://youtu.be/YDP2JT3gce4?t=7938); [0:31:51](https://youtu.be/YDP2JT3gce4?t=1911) |
| Mococo's vowel tail, sneezes (wiki) | **Not detectable** by transcription. Kept from the wiki. | — |
| No swearing | **Consistent** in all windows. | — |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Yeah, he did not look at me. Hello, ma'am. Nice day, ma'am." | [0:12:13](https://youtu.be/L93K3U4Hrjg?t=733) | "at me Don't look at me Yeah, he did not look at me Hello ma'am, nice day ma'am" | Agrees |
| "Should I run? Is running suspicious?" | [0:13:41](https://youtu.be/L93K3U4Hrjg?t=821) | "out of here. Should I run? Is running suspicious? I could go" | Agrees |
| "Question, is his clothes better than mine? No. In you go." | [1:05:17](https://youtu.be/L93K3U4Hrjg?t=3917) | "Okay, now question. Is his clothes better than mine? No. Okay, in you go. Oh, wrong" | Agrees |
| "Princess in a different castle." | [1:08:26](https://youtu.be/L93K3U4Hrjg?t=4106) | "on another building. Princess is in a different castle. I was" | Agrees ("Princess in" vs "Princess is in"; quoted "…in a different castle") |
| "Can I have one? I like one. Can I have one? Get away from me, you creep. I want one. I want one." | [1:11:16](https://youtu.be/L93K3U4Hrjg?t=4276) | "That looks yummy. Can I have one? I like one. Can I have one? I want one. I want one. I want one. Can I have one? What are" | **Partly agrees**: "That looks yummy. Can I have one? I like one. Can I have one?" agrees; "Get away from me, you creep" is first-model only (probably a game voice) and is not quoted |
| "Please give me your snacks. I'm not even asking for a full loaf." | [1:11:41](https://youtu.be/L93K3U4Hrjg?t=4301) | "and I'll go away Please give me your snacks not even asking for a full loaf just one of" | **Partly agrees**: "Please give me your snacks… not even asking for a full loaf" (the second model lacks "I'm") |
| "If I go into the crowd, too, I blend in. Right? I'm blending in right now, right?" | [1:12:32](https://youtu.be/L93K3U4Hrjg?t=4352) | "it go well? If I go into the crowd too... I blend in Right? I'm blending in right now, right? So... Do I" | Agrees |
| "But it's gonna be good because you're gonna be stronger and you're gonna be healthy." | [5:48:21](https://youtu.be/L93K3U4Hrjg?t=20901) | "ahhh I'm sweaty But it's gonna be good because you gonna be Stronger and you gonna be healthy And you gonna" | **Partly agrees** ("you're gonna" vs "you gonna"); not quoted; the next line is |
| "So go do that, go to the gym and be the main character of the gym." | [5:48:33](https://youtu.be/L93K3U4Hrjg?t=20913) | "can do anything so go do that go to the gym and be the main character of the gym okay you got" | Agrees |
| "But mocha-chan's just better suited for it, you know? But I'm a bit fuffier. My voice is a bit softer, so..." | [5:52:55](https://youtu.be/L93K3U4Hrjg?t=21175) | "same as Moko-chan's pop-talks But Moko-chan's is better suited for it, you know? But I'm a bit full for it My voice is a bit slow too, so..." | **Partly agrees**: "Moco-chan's [is] just better suited for it, you know?" agrees; her description of her own voice differs ("fuffier… softer" vs "full for it… slow too") and is not quoted |
| "It was a lot of fun! I'm going to have lots and lots of cake!" | [5:55:28](https://youtu.be/L93K3U4Hrjg?t=21328) | "much, Raffias Wow! It was a lot of fun Please be sure to support Mukocha lots and lots, okay? Listen to" | **Partly agrees**: "It was a lot of fun!" agrees; the cake line is first-model only |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "I die. If I die, I die." | [0:57:47](https://youtu.be/Sxx4UW3XKnc?t=3467) | "I If I die I die if I die I" | Agrees ("If I die, I die") |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "a real senpai a real senpai" | [0:13:12](https://youtu.be/YDP2JT3gce4?t=792) | "it to Santa-senpai, Popo-senpai, Ami-o-senpai, what do we senpai? Who else eat?" | **Disagrees**: the second model hears a list of senpai names; not quoted |
| "A courteous half bite?" | [0:13:44](https://youtu.be/YDP2JT3gce4?t=824) | "them it was dessert! Karate-senpai got a whole piece, and" | **Disagrees**: not in the second model's text; not quoted |
| "Do you know when you hold a cat up by its armpit? And then its arms are straight out." | [0:13:57](https://youtu.be/YDP2JT3gce4?t=837) | "didn't like it. And you know, when you hold a cat up by its armpits. And then its arms are straight out. That's why she" | **Partly agrees** ("when you hold a cat up by…"); not quoted |
| "I'm a donut pro, okay?" | [0:30:33](https://youtu.be/YDP2JT3gce4?t=1833) | "did though. Cause I'm a donut pro, okay? That's a lie." | Agrees; the second model continues "That's a lie." (the other twin, apparently; not quoted on the card) |
| "But Chewbacca is basically a princess. Chewbacca is the princess." | [0:31:51](https://youtu.be/YDP2JT3gce4?t=1911) | "No. No princesses. But Chewbacca is basically a princess. Chewbacca is the princess. Okay. Yeah. Yeah." | Agrees |
| "They're not Bulbasaur shaped, he's just sitting there on the package. I'm scammed, right!" | [0:38:16](https://youtu.be/YDP2JT3gce4?t=2296) | "What is he on the package? They just watermelons They're not Bulbasaur shaped He's just sitting there on the package" | **Partly agrees** ("They're not Bulbasaur shaped"); not quoted |
| "I wanted to eat Bulbasaur." | [0:38:32](https://youtu.be/YDP2JT3gce4?t=2312) | "was the point? Huh? I wanted to eat boba-so-shaped candies Yeah" | **Disagrees** ("Bulbasaur" vs "boba-so-shaped"); not quoted |
| "Special memories! Thank you!" | [0:42:50](https://youtu.be/YDP2JT3gce4?t=2570) | "and everything It'll be another really special memory too And" | **Disagrees**: not quoted |
| "The moon!" | [2:08:10](https://youtu.be/YDP2JT3gce4?t=7690) | "Florida New York The moon Chicago Las Vegas" | Agrees |
| "So again, guys, talk about this. Maybe, um, they need to put us in charge." | [2:12:03](https://youtu.be/YDP2JT3gce4?t=7923) | "all on the cruise here we go again guys i do feel like we talked about this maybe around fast? i" | **Partly agrees**: "they need to put us in charge" is in both; the lead-in differs |
| "Right! Right! Exactly." | [2:12:18](https://youtu.be/YDP2JT3gce4?t=7938) | "put us in charge. Right. Exactly. Endurance concert. Yeah." | Agrees on "Right!" and "Exactly." (the second model has "Right. They need to put us in charge. Right. Exactly.") |



==================== CAST AND WORLD EDITS (diff of final.md files since Advent work began; + added, - removed) ====================

+++ b/novel-lab/projects/holoen/runs/20260930-0704-character-Mori-Calliope/final.md
-Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!" Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her chaotic CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin: frequent collaborator; Calli came to like how her own name sounds once Gigi started saying it. Kobo Kanaeru: calls her "Uncle Dad." Koseki Bijou ("Biboo"): a junior whose skill Calli openly admires. Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together. Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star"). Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka). Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth: her "LYRA" remix cover of "III." Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022).
+Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!" Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her chaotic CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin: frequent collaborator; Calli came to like how her own name sounds once Gigi started saying it. Kobo Kanaeru: calls her "Uncle Dad." Koseki Bijou ("Biboo," "TombStone"): a junior whose skill Calli openly admires; Bijou auditioned with an Undertale fight starring Calli, and they ran a 24-hour charity stream together (2025). Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together (a kids'-movie deep-dive, 2024), and Calli admits she is "a little obsessed with her." Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star"). Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka). Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth: her "LYRA" remix cover of "III." Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022). FUWAMOCO: "FUWAMOCALLI," the twins' favorite pair name.
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20260930-0704-character-Ouro-Kronii/final.md
-Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'Clock); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated 2025): Council genmate and frequent partner (KronMei), from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet in Mumei's last month (2025). Ceres Fauna (graduated 2025): Council genmate who described Kronii's "gap moe"; they once defused bombs speaking only in ASMR. Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel. Gigi Murin: collaborator in the units "TimeChaser" and "Clockwork Orange." Cecilia Immergreen: calls her "Owo-senpai"; Kronii calls her a "CLANKER." Raora Panthera: "Pizza Time" partner who calls her "Tam Tender." Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live.
+Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'Clock); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated 2025): Council genmate and frequent partner (KronMei), from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet in Mumei's last month (2025). Ceres Fauna (graduated 2025): Council genmate who described Kronii's "gap moe"; they once defused bombs speaking only in ASMR. Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel. Gigi Murin: collaborator in the units "TimeChaser" and "Clockwork Orange." Cecilia Immergreen: calls her "Owo-senpai"; Kronii calls her a "CLANKER." Raora Panthera: "Pizza Time" partner who calls her "Tam Tender." Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live. Shiori Novella: Kronii let her rate her clocks on stream (2025), and they sang "MONSTER" with Ina and Gigi at the 2025 English concert. Koseki Bijou: Lethal Company and Yu-Gi-Oh collabs. FUWAMOCO: "WatchDog."
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Gawr-Gura/final.md
-Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George." Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated. Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week.
+Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George." Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated. Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week. Shiori Novella and Nerissa Ravencroft: her "Scarlet Wand" guildmates in the ENigmatic Recollection story. Fuwawa Abyssgard: shares her trouble telling left from right.
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Ninomae-Inanis/final.md
-Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'Clock); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, Ina credits Kiara's support with helping her gain confidence in dancing, and Kiara groans at her puns. Mori Calliope: a recurring target of her puns ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy whose collab outfit Ina designed. IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island. Houshou Marine: a senior artist she admires. Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025).
+Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'Clock); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, Ina credits Kiara's support with helping her gain confidence in dancing, and Kiara groans at her puns. Mori Calliope: a recurring target of her puns ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy whose collab outfit Ina designed. IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island. Houshou Marine: a senior artist she admires. Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025). Shiori Novella: a "Rate Your Fears" nightmare talk (2024) and "MONSTER" with Kronii and Gigi at the 2025 English concert. FUWAMOCO: "SHALLYS" with Cecilia at the same concert.
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Takanashi-Kiara/final.md
-Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert; they share the "6 7" meme. Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI). Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera: cast the infamous "Doom." Cecilia Immergreen: German-speaking partner. Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior. Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert, and she was HOLOTALK's 33rd guest. Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left.
+Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert ("Rocku Wawa"); they share the "6 7" meme. Shiori Novella: an occult handcam off-collab ("#shiotori," 2024). Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI). Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera: cast the infamous "Doom." Cecilia Immergreen: German-speaking partner. Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior. Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert, and she was HOLOTALK's 33rd guest. Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left.
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Watson-Amelia/final.md
-Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs. Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week.
+Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs. Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week. FUWAMOCO: "Detective Dogs" (Escape Simulator, 2024: "blondes can solve any puzzle"). Shiori Novella: a VRChat aquarium visit with "Ame Senpai" (2024). Koseki Bijou: Overwatch and Apex (2023).
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20260930-2309-world-VTuber-Persona-and-Lore/final.md
-All ten cast members. Each character card's Background and Personality open with the persona frame
+All fourteen cast members. Each character card's Background and Personality open with the persona frame
-The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.
+The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization, an archiver who broke out of a prison for forbidden things, a gem born from human emotion, twin demonic guard dogs) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.
+- **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
+  (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
+++ b/novel-lab/projects/holoen/runs/20260930-2309-world-hololive/final.md
-All ten. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
-Kronii and IRyS are active in hololive -Promise-, where Fauna and Mumei are alumnae; Nerissa in hololive -Advent-. Detailed history: the
+All fourteen. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
+Kronii and IRyS are active in hololive -Promise-, where Fauna and Mumei are alumnae; Nerissa, Shiori, Bijou, Fuwawa and Mococo in hololive -Advent-. Detailed history: the
+- **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
+  (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
+++ b/novel-lab/projects/holoen/runs/20260930-2334-character-IRyS/final.md
-Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her frequent horror co-op partner in 2025–2026. Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna (graduated 2025): Promise unitmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Nanashi Mumei (graduated 2025): Promise unitmate; they played Overwatch together during Mumei's farewell week.
+Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her frequent horror co-op partner in 2025–2026. Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna (graduated 2025): Promise unitmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Nanashi Mumei (graduated 2025): Promise unitmate; they played Overwatch together during Mumei's farewell week. Shiori Novella: Monster Hunter Wilds and PEAK (2025).
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20261001-0001-world-hololive--Advent/final.md
-> Scope: Nerissa Ravencroft's group as publicly shown, checked 2026-10-01. Evidence labels as in the other
-> world files. "Archive" = stream titles and descriptions on Nerissa's channel (archive.ragtag.moe, S4);
-> counts are streams mentioning the member per year (2023 → 2025), a rough measure (the archive holds 114,
-> 183 and 87 of her streams for those years and only 22 for 2026). Only what a Nerissa story needs.
+> Scope: the whole group as publicly shown, checked 2026-10-01 (first written for Nerissa; widened when the
+> author added all of Advent). Evidence labels as in the other world files. "Archive" = stream titles and
+> descriptions on the members' channels (archive.ragtag.moe, S4); counts are streams mentioning the member
+> per year, a rough measure, not a ranking (the archive thins out from late 2025). Pair details live on the
+> world cards "Advent Pairs" and "FUWAMOCO."
-Nerissa's group: five "criminals" who escaped from The Cell, a prison for anything too dangerous to exist,
-and debuted together as hololive English's third generation in July 2023. All five are active in 2026, and
-the "escaped convict" premise is a running bit they play with, not a fact they live by.
+Five "criminals" who escaped from The Cell, a prison for anything too dangerous to exist, and debuted
+together as hololive English's third generation in July 2023: the Archiver who planned the break (Shiori),
+a gem made of human emotion (Bijou), the Demon of Sound (Nerissa) and twin demonic guard dogs (Fuwawa and
+Mococo, FUWAMOCO). The "escaped convict" premise is a running bit they play with, not a fact they live by.
-- Active: Shiori Novella, Koseki Bijou, Nerissa Ravencroft, and the twins Fuwawa and Mococo Abyssgard
-  (FUWAMOCO, who share one channel). [Observed S1 member table, secondary]
+- Members: Shiori Novella (the Archiver; narrator of their lore videos and the fans' pick as unofficial
+  leader), Koseki Bijou (the Jewel of Emotions; "Biboo"), Nerissa Ravencroft (the Demon of Sound), and the
+  twins Fuwawa and Mococo Abyssgard (FUWAMOCO, who share one channel). [Official S8] [Observed S1 member
+  table, secondary; character files]
-## How the Group Works (as it touches Nerissa)
+## How the Group Works
+- **The escape, retold:** Shiori was the mastermind; she picked Bijou up and wielded her to blast the
+  guards; Bijou threw rocks; the twins barked to distract the guards and Mococo threw Pero at them; Nerissa
+  took the master key. An April Fools video, "Another Rebellion," had the jailers unseal a "dancing curse," which they broke.
+  [Observed S2, Shiori/Bijou/Fuwawa/Mococo wiki §Lore, secondary]
+- **Shiori, Bijou and FUWAMOCO among themselves:** "Goth Rock" (Shiori–Bijou; Bijou calls Shiori "our
+  glorious leader"), "Pen Pups" (Shiori–FUWAMOCO; the twins once mistook a Minecraft cow for Shiori),
+  "Diamond Dogs" (Bijou–FUWAMOCO). Details: "Advent Pairs." [Observed S2; S4]
-| 2024 (summer) | Advent 3D debuts; Nerissa's on 2024-08-09 | The "Demon of Soup" soup |
+| 2024-08-02/10 | 3D debuts: Shiori 08-02, Bijou 08-03, Nerissa 08-09, FUWAMOCO 08-10 | genmates as guests |
+| 2024-12 | FUWAMOCO win "VTuber of the Year" at the VTuber Awards | — |
+| 2025-08-23 | -All for One- opens with all of EN, then Advent's "Genesis" | [Official S9] |
+| 2026-01-26 | Group song "Breakout" | — |
+| 2026-07-03/04 | Serendipity pairs: Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth, FUWAMOCO–Raora | [Official S7, S10] |
-Nerissa Ravencroft (member). Kiara, Calli and IRyS appear as seniors (see "IRyS and Nerissa Pairs").
+Shiori Novella, Koseki Bijou, Nerissa Ravencroft, Fuwawa Abyssgard, Mococo Abyssgard (members). Seniors
+across Myth and Promise appear as friends (see "Advent Pairs," "FUWAMOCO," "IRyS and Nerissa Pairs").
+- S8 Official profiles of Shiori, Bijou, Fuwawa and Mococo (hololive.hololivepro.com/en/talents/...)
+- S9 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
+- S10 Official Serendipity interviews 03 (FUWAMOCO & Raora), 04 (Kiara & Bijou), 05 (Calliope & Shiori)
+- S11 Character files: Shiori (SN#), Bijou (KB#), Fuwawa (FW#), Mococo (MC#); world cards "Advent Pairs," "FUWAMOCO"
-Advent, holoAdvent, hololive English -Advent-
+Advent, holoAdvent, hololive English -Advent-, Adventrix, The Cell
-Nerissa Ravencroft's group, hololive English's third generation (debuted July 2023): Shiori Novella, Koseki Bijou, Nerissa, and the twins Fuwawa and Mococo Abyssgard (FUWAMOCO). Their shared lore is a stream bit: five "criminals" who escaped The Cell, a prison for anything too dangerous to exist; in the story Nerissa took the master key she wears on her keychain. The next generation, -Justice-, are the "law enforcers" sent to catch them, so joint streams can use prisoner-and-guard jokes; Nerissa calls Elizabeth her "mortal enemy (lore)" and sang with her as a duo at the 2026 Serendipity concert. Nerissa calls Shiori her "wife" while Shiori plays hard to get (ShioRaven); with Bijou she is a raven drawn to the shiny rock girl (JewelBird); with FUWAMOCO she claims to be the third sister, "Mofufu" (Sound Hounds). Kiara hosted all five on HOLOTALK two weeks after their debut. Fans: Adventrix, mark ⚠️.
+hololive English's third generation (debuted July 2023), now "hololive -Advent-": Shiori Novella, the Archiver who planned the escape and narrates the group's lore (fans' pick as unofficial leader); Koseki Bijou ("Biboo"), a tiny gem made of human emotion who never swears; Nerissa Ravencroft, the Demon of Sound; and the twin demonic guard dogs Fuwawa and Mococo Abyssgard (FUWAMOCO), who share one channel. Their shared lore is a stream bit: five "criminals" who escaped The Cell, a prison for anything too dangerous to exist; Nerissa took the master key she wears on her keychain. The next generation, -Justice-, are the "law enforcers" sent to catch them, so joint streams can use prisoner-and-guard jokes. Inside the group: Nerissa calls Shiori her "wife" while Shiori plays hard to get (ShioRaven); Bijou calls Shiori "our glorious leader" (Goth Rock); Nerissa is the raven drawn to Bijou's shine (JewelBird) and the self-declared third Abyssgard sister, "Mofufu" (Sound Hounds); Bijou and the twins are Diamond Dogs; the twins once mistook a Minecraft cow for Shiori. Milestones: 3D debuts in August 2024, FUWAMOCO's "VTuber of the Year" (2024), "Genesis" at the 2025 English concert, anniversary lives "On the Run!" (2025) and "Bound by Fate" (2026), and 2026 Serendipity pairs Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth and FUWAMOCO–Raora. Kiara hosted all five on HOLOTALK two weeks after their debut. Fans: Adventrix, mark ⚠️.
+- **2026-10-01, cast expansion (author: all of Advent):** the card widened from Nerissa's view to the whole group:
+  members' roles, the escape retold, Shiori/Bijou/FUWAMOCO pairs (details in "Advent Pairs" and "FUWAMOCO"),
+  3D debut dates, FUWAMOCO's award, -All for One- (S9), "Breakout," the Serendipity pairs (S7, S10);
+  Description rewritten.
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-Concerts-and-Live-Events/final.md
-  Hall, New York), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around
+  Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora
+  Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's
+  "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest" [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around
-All ten (Fauna and Mumei: the 2023 EN concert, 4th fes., Mumei's 2024 3D birthday live "Outside the Box" and 6th fes.).
+All fourteen (Advent: -Breaking Dimensions-, -All for One-, Serendipity and their own anniversary lives; Fauna and Mumei: the 2023 EN concert, 4th fes., Mumei's 2024 3D birthday live "Outside the Box" and 6th fes.).
+- S9 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
+- S10 Official Serendipity interviews, FUWAMOCO & Raora (interview03), Kiara & Bijou (interview04), Calliope & Shiori (interview05)
-The stages of the hololive year. Recurring formats: each spring, hololive fes. with hololive SUPER EXPO in Japan (a combined tradition since 2022; Calli and Kiara sang at the 2022 fes. in Makuhari, Nerissa at the 6th fes. in 2025); each summer, a hololive English concert in the US (2023 "-Connect the World-"; 2024 "-Breaking Dimensions-," New York; 2025 "-All for One-," Radio City; 2026 "Serendipity," Los Angeles, July 3–4, built on pairs including Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Bae and Nerissa–Elizabeth); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet. The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn" (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (March 2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01). A member may stream an aftertalk afterward.
+The stages of the hololive year. Recurring formats: each spring, hololive fes. with hololive SUPER EXPO in Japan (a combined tradition since 2022; Calli and Kiara sang at the 2022 fes. in Makuhari, Nerissa at the 6th fes. in 2025); each summer, a hololive English concert in the US (2023 "-Connect the World-"; 2024 "-Breaking Dimensions-," New York; 2025 "-All for One-," Radio City; 2026 "Serendipity," Los Angeles, July 3–4, built on pairs including Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Bae, Nerissa–Elizabeth and FUWAMOCO–Raora); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet. The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn" (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (March 2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!" (2025) and "Bound by Fate" (2026). A member may stream an aftertalk afterward.
+- **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
+  (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-Cross-Branch-Friends/final.md
-All ten.
+All fourteen.
-The cast's ties beyond EN, including JP, ID, DEV_IS and HOLOSTARS. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones" ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI"). Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora. IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan." Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week.
+The cast's ties beyond EN, including JP, ID, DEV_IS and HOLOSTARS. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones" ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI"). Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora. IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan." Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week. Of Advent: Bijou's most frequent documented partner outside the group is Kaela Kovalskia ("Grindstone"; Kaela calls her "Beejoe"), with Kureiji Ollie ("GraveStone") and Akai Haato ("Red Stone"); Shiori and Vestia Zeta are "GreyScaleX" (the X is silent), and she found hololive through Inugami Korone's clips; FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo), they game with Shirakami Fubuki and Hakui Koyori, and Oozora Subaru sang "HOT DUCK!" with them and Bijou.
+- **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
+  (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-hololive-History-2023-2026/final.md
+| 2024-08-02/10 | Advent 3D debuts: Shiori (08-02), Bijou (08-03), Nerissa (08-09), FUWAMOCO (08-10, with Okayu and Korone cameos) | genmates as guests |
+| 2024-10-12 | FUWAMOCO reach 1,000,000 subscribers, first in Advent; VTuber of the Year at the VTuber Awards (2024-12) | — |
-| 2025-08-23/24 EDT | EN 3rd concert "-All for One-" (Radio City Music Hall, New York) | — |
+| 2025-08-23/24 EDT | EN 3rd concert "-All for One-" (Radio City Music Hall, New York): Advent opens day 1 with "Genesis"; Justice's first stage as a group | all fifteen EN members on one stage |
-| 2026-07-03/04 | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around partner pairs (Calli–Shiori, Kronii–Ina, Kiara–Bijou) | The current partnerships |
+| 2026-07-03/04 | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around partner pairs (Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Bae, Nerissa–Elizabeth, FUWAMOCO–Raora) | The current partnerships |
+| 2026-07/08 | Shiori's original motion comic "Into The Void" (with Elizabeth, Gigi, Nerissa); Advent's 3rd-anniversary 3D live "Bound by Fate"; FUWAMOCO announce their first album (08-29) | — |
-All ten. Nerissa (Advent, 2023); Fauna and Mumei (graduated 2025); IRyS and Kronii (Promise, 2023); Ame (affiliate, 2024); Gura
+All fourteen. Advent (Nerissa, Shiori, Bijou, Fuwawa, Mococo; 2023); Fauna and Mumei (graduated 2025); IRyS and Kronii (Promise, 2023); Ame (affiliate, 2024); Gura
+- **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
+  (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
+++ b/novel-lab/projects/holoen/runs/20261001-0430-character-Ceres-Fauna/final.md
-Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024); Silent Hill 2 with Gigi Murin. Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!"
+Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024); Silent Hill 2 with Gigi Murin. Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!" Koseki Bijou: "Coach Fauna" in Bijou's Hitman runs and a "Sweaty TryHard Gamers" squad with Bae and Kaela. FUWAMOCO: helped on the World Tree's last day (2024-12-31). Shiori Novella: the third voice of "Lonely in Gorgeous."
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
+++ b/novel-lab/projects/holoen/runs/20261001-0430-character-Nanashi-Mumei/final.md
-Ceres Fauna (graduated 2025-01): Council and Promise genmate and recurring collaborator; their comedy includes Fauna's exaggerated protective, possessive bits ("return to nature"), complicated by Mumei's macabre humor; they premiered their duet "It's Not a Phase" at the 2024 English concert. Hakos Baelz: genmate and a recurring collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). Ouro Kronii ("KronMei"): genmate and frequent partner, from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). IRyS: Promise unitmate from 2023; they played Overwatch together in Mumei's farewell week, then R.E.P.O. with all of Promise (2025-04-24). Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday. Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Mumei was Kiara's HOLOTALK guest in her last week. Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week. Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week. Ninomae Ina'nis: fellow artist, drawing collabs. Mori Calliope: "ANATOMY REVIEW." Nerissa Ravencroft: "EMO HOURS" (2023), "Beyond the way" with Kiara at the 2024 concert, "SAD GIRL HOURS" (2025). Koseki Bijou ("Stone Age"): Portal 2 and Marvel Rivals; at arm wrestling Mumei rates her a loss because "she is a rock." Gigi Murin: Echo Point Nova as "A Towl and a Gremlin." Cecilia Immergreen: "Automatowl," who calls her "Myumyei." FUWAMOCO ("Fuwamoomco"): Overwatch. JP: Takane Lui ("Q&A With Bird Sisters"), Tokoyami Towa (calls her "Mumi-chan"), Akai Haato (Minecraft); Inugami Korone (a duet cover in her last week) and Okayu, Nene and Koyori, guests at "Outside the Box."
+Ceres Fauna (graduated 2025-01): Council and Promise genmate and recurring collaborator; their comedy includes Fauna's exaggerated protective, possessive bits ("return to nature"), complicated by Mumei's macabre humor; they premiered their duet "It's Not a Phase" at the 2024 English concert. Hakos Baelz: genmate and a recurring collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). Ouro Kronii ("KronMei"): genmate and frequent partner, from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). IRyS: Promise unitmate from 2023; they played Overwatch together in Mumei's farewell week, then R.E.P.O. with all of Promise (2025-04-24). Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday. Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Mumei was Kiara's HOLOTALK guest in her last week. Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week. Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week. Ninomae Ina'nis: fellow artist, drawing collabs. Mori Calliope: "ANATOMY REVIEW." Nerissa Ravencroft: "EMO HOURS" (2023), "Beyond the way" with Kiara at the 2024 concert, "SAD GIRL HOURS" (2025). Koseki Bijou ("Stone Age"): Portal 2 and Marvel Rivals; at arm wrestling Mumei rates her a loss because "she is a rock." Gigi Murin: Echo Point Nova as "A Towl and a Gremlin." Cecilia Immergreen: "Automatowl," who calls her "Myumyei." FUWAMOCO ("Fuwamoomco"): Overwatch. JP: Takane Lui ("Q&A With Bird Sisters"), Tokoyami Towa (calls her "Mumi-chan"), Akai Haato (Minecraft); Inugami Korone (a duet cover in her last week) and Okayu, Nene and Koyori, guests at "Outside the Box." Shiori Novella: B-movie watchalongs (Neil Breen, Kung Pow; 2025).
+- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
+  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
+  (sources in the world card "Advent Pairs" and the Advent character files).
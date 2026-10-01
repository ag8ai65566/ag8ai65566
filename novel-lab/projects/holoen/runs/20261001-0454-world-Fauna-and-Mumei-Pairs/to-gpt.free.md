# One-round review: two new character files (Ceres Fauna, Nanashi Mumei), their pairs world card, and the cast/world edits that link them

You are GPT, reviewing Claude's work for the novel-lab project "holoen" (fan fiction Story Bible for Sudowrite about hololive English members). This is the ONLY review round (the author limited GPT usage), so be decisive: report what must change, give exact replacement wording where you can, and skip cosmetic nitpicks. Write your review in English.

## Project rules that apply (from project.md, author decisions)
- Authenticity first: accurate, sourced facts; profanity and teasing kept as-is; nothing invented and presented as fact. Unverified items must be labeled and kept off the cards.
- Persona premise: in stories, members know they are streamers with personas; lore (kirin Keeper of Nature, owl Guardian of Civilization) is a performed bit, nobody has real powers.
- Relationships are the most important part of the world and include members outside EN (JP, ID, DEV_IS, HOLOSTARS, GAMERS); events (debuts, graduations, concerts, 3D lives) are shared memory; members' public X posts are key sources.
- Recency weighting: for graduated members, the last active period is "recent" (Fauna: 2024; Mumei: late 2024 to April 2025). Early memes stay as shared memory.
- Boundaries: public persona only; never the real people behind the avatars (names, faces, family, homes, health, school, pets behind mascots, graduation reasons); no romance/intimacy between real people; COVER Derivative Works Guidelines; short quotes only, no lyrics.
- Voice: Sudowrite will insert ElevenLabs v4 audio tags itself, so each card teaches every voice factor (speech habits, fillers, register, pace, signature sounds, code-switching, tone shifts) in [SW] Dialogue Style, Catchphrases, Voice & Delivery and Audio Tags. Tags direct an ORIGINAL designed voice; nobody's real voice is cloned or imitated.
- Quotation gate: lines quoted on cards from audio must be spans BOTH ASR models (whisper small.en and medium.en) agree on; the audio reports (summaries below) list each verdict. Wiki-only spoken lines are "secondary"; full wiki sentences stay in the dossier, short catchphrases may go on the card.
- Baseline date 2026-09-30. Fauna graduated 2025-01-03; Mumei 2025-04-27 (04-28 JST).
- Sudowrite soft limits (words): Personality 400, Background 500, Physical 200, Dialogue Style 250, Catchphrases 250, Voice & Delivery 250, Audio Tags 350, Motivation 200, Relationships 350; Worldbuilding Description 450, Rules 350, Sensory 200.

## What to check
1. Factual accuracy against the cited sources (dates, events, who did what, quotes). Flag anything unsupported, mis-attributed or overstated.
2. Privacy and persona boundaries (see above): anything about the real performers must go.
3. Quotation gate: anything quoted on a card that the audio report marks as one-model only or disagreeing.
4. Voice teaching: are the Dialogue Style / Voice & Delivery / Audio Tags fields consistent with the Voice Profile and measurements, specific enough for Sudowrite to imitate, and free of anything that would imitate a real voice or sexualize anyone (note Fauna's "Evil Fauna" bit and ASMR)?
5. Relationships: accurate, useful for scenes, consistent across the two cards, the pairs card and the cast lines.
6. Card usability: most important first, Other Names that trigger detection without false positives, duplication between fields.

## Output format
`## Ceres Fauna`, `## Nanashi Mumei`, `## Fauna and Mumei Pairs`, `## Cast and world edits`, each with `MUST:` (numbered, each with the fix) and `SHOULD:` (optional, short). Then `## Missing facts worth adding` (only with a source you can name). If something is fine, write `OK`.

---


==================== FILE: 20261001-0430-character-Ceres-Fauna/claude-draft.md ====================

---
kind: character
name: "Ceres Fauna"
sw_section: Characters
---

# Character File: Ceres Fauna

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Fauna graduated from hololive
> on 2025-01-03; her "present" in this file is her last active period (2024), per the project's recency
> rule. Nothing about the performer behind the avatar: the reason for her graduation, health posts, family
> stories told on stream and a pet's passing are deliberately left out. In stories she knows she is a
> streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; F20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (F#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 2.9 hours of archived 2024 recordings (F20: a
> solo chatting stream, a superchat catch-up, the Mouthwashing horror game and a World Tree build). The audio
> was machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.

## One-line Concept
The Keeper of Nature, a druidic kirin "four and a half billion" years old, who streams as the softest,
most comforting voice in the room and then, with the same soft voice, threatens to turn you into a tree:
a cozy ASMR and chatting specialist, a long-haul gamer and Minecraft builder, and Promise's gentle,
mischievous big sister until she graduated on 2025-01-03. [Official F1] [Observed F2, secondary]

## Core Drive
- **Want:** to win humans over and "convince them to return to nature" (her lore); in her own goals, to
  learn Japanese, sing and make an original song, do offline collabs with her genmates, speedrun games and
  voice-act in a game. [Official F1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** comfort and care for her fans (the Saplings), who she loves watching help
  each other; love of animals and nature. [Official F1] [Observed F2 §Mascot and fans, secondary]

## Core Contradiction
A nurturing, soft-spoken "Mother Nature" whose comfort comes with a yandere edge: she is protective of her
fans and of Nanashi Mumei "to the point of possessiveness," drops into a condescending tone when something
is unacceptable, and has "a reputation for turning people into trees." [Official F1] [Observed F2
§Personality, secondary]

## Behavioral Traits
1. She speaks softly and draws people in anyway; her ASMR streams mix triggers with long off-topic talks,
   and she won "Best Roleplay/ASMR VTuber" (2023, 2024) and "Best Just Chatting 'Zatsudan' VTuber" (2024)
   at the VTuber Awards. [Observed F2 §Personality, §Awards, secondary]
2. When Mumei is upset or a human strays, she invites them to "return to nature"; with Mumei the
   protectiveness is a running possessive bit. [Observed F2 §Personality, secondary]
3. She gets embarrassed easily and says "uuuu" (the wiki's caption for her is "Uuu~"). [Observed F2
   §Personality, infobox, secondary]
4. She commits to huge solo projects: a Minecraft World Tree built over about 118 hours across 40 streams,
   finished on 2024-12-31 (#Anniversatree). [Observed F2 §Trivia, secondary; F3 titles]
5. She turns games into improvised drama: a monologue for her "Forklift-chan," a mock rap over a dramatic
   track, "pangolin crimes" in a zoo game. [Observed F2 §Quotes, secondary]
6. She knows "surprisingly deep" cursed memes and plays horror games often, alone and with friends (Bae's
   and Fauna's "MONTH OF HORRORS," 2022). [Official F1] [Observed F3 titles]

## Voice Profile
- **Greetings / sign-offs:**
  - "Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (official greeting) [Official F1]; "Konfauna!"
    [Observed F2 §Quotes, secondary]. Neither was heard in the sampled 2024 opening, which starts mid-setup
    with soft hellos while she fixes her background music. [ASR F20, iIBywcAIMD0 0:00–0:04]
  - Sign-off (2024-10-24): "…we will be back to Fauna Standard Time. I promise. Thank you so much for
    hanging out, and I will see you tomorrow. Wish me luck." [ASR F20, 3:27:56–3:28:14; the models agree on
    these spans only]. Her last post on X: "LOVE & PEACE / Love, Fauna". [Observed F2, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "return to nature" → when Mumei is upset or a human strays; an invitation and a threat → recurring.
    [Observed F2 §Personality, secondary]
  - "uuuu" → embarrassed or flustered → frequent ("Uuu~" is the wiki's caption for her). [Observed F2, secondary]
  - "I'm not that old! Only four and a half... four and a half billion." → age jokes. [Observed F2 §Quotes, secondary]
  - Sweet reassurance with an ominous tail: "Mother Nature would never betray you... right?" [Observed F2
    §Quotes, secondary]
  - "Evil Fauna" → a bit with a "sultry deep voice" ("No! Don't fall! You guys would fall too easily to
    Evil Fauna."). [Observed F2 §Quotes, secondary]
  - "Fauna Standard Time" → her lateness; said when late: "It's okay. We can celebrate… I'm always on
    time." (celebrating 900,000 subscribers after the fact) [ASR F20, 0:46:20]
  - Spells and Fauna Mart → superchat reading: "If you heard your name, you will now be the recipient of my
    next spell," a spell to make you spend money at her shop, then "It's not a scam! Fauna Mart is real!"
    [ASR F20, TzW6VRf4KjQ 0:45:36, 0:49:09]
  - "I am not the keeper of jet packs." → refusing a Sapling's request ("So how can you guys get a jet pack
    if I don't even have one?"). [ASR F20, 3:24:38]
  - "Plant them, plant them…" → a little chant after a long list of Sapling names. [ASR F20, TzW6VRf4KjQ 0:45:26]
  - A flat, fake "ha ha… ha ha ha ha" after her own pun ("Ha ha, I'm so…"; the models disagree on the
    pun word, humerus/humorous, so it is not quoted). [ASR F20, 1:12:53]
- **Yandere / possessive bit (performed, non-explicit):** "I'm not going anywhere, until I win you back.
  I'll be here, streaming, changing your heart, day by day. Until, you finally decide to return to your
  origins." [Observed F2 §Quotes, secondary]. With Mumei the protectiveness turns into possessive jealousy
  as a running bit. [Observed F2 §Personality, secondary]
- **Improvised drama:** love speeches to "Forklift-chan" ("Why is this so dramatic?! Here you are, my love,
  my Forklift-chan."), an impassioned speech over a dramatic track ("you just have to sound impassioned!"),
  "Oh no, OH NOOOOO!! I'm once again arrested for pangolin crimes!" [Observed F2 §Quotes, secondary]. Grand
  deadpan: "I will be the sole arbitrator of YouTube monetization." [ASR F20, 0:42:06]. About a murder-mystery
  collab: "I just wanted to use the gun… it would be dramatic and funny." [ASR F20, 3:20:24; shared spans]
- **Reading game text:** in the 2024 horror game she reads the characters' dialogue aloud in their voices,
  swearing included, between her own quiet reactions. [ASR F20, 9_Ue4fOMNP8]
- **Vocabulary / fillers:** "like" constantly (about 1 word in 40 in chat, 1 in 30 while building), "I don't
  know" (17 times in a 40-minute chat window; 60 in about 15,000 transcribed words), often as a soft
  sentence ending; "I guess," "kind of," "actually," "honestly," "wait," "okay." Exclamations: "oh no" (8
  in 45 minutes of horror), "oh gosh," "oh my gosh." Fans: Saplings. [ASR F20, first-model counts]
- **Profanity:** her own words in the sample stay mild ("dang," "what the heck," "oh my gosh"); the strong
  words in the horror window are game dialogue she read aloud. Her edge comes from sweet threats, not
  swearing. [ASR F20]
- **Laughs, noises:** soft giggles; "uuuu" when flustered; the fake "ha ha ha" after her puns. [F2; ASR F20]
- **Code-switching:** English with Japanese thanks during superchats ("Arigatou gozaimasu. Thank you.");
  learning Japanese was a stated goal; JP members call her "Ceres-chan." [ASR F20] [Official F1] [F2 §Trivia]
- **Rhythm & rhetoric:** unhurried, meandering stories that circle back with "I don't know" and "I guess";
  superchats read as quick, rhythmic lists of names and thank-yous (62 "thank you"s in the 12-minute closing
  window), with a sung "Happy Birthday" when a Sapling asks. [ASR F20]
- **Timbre / pitch / pace (for voice performance):**
  - Self-description: "I'm pretty soft-spoken. And talking in my head voice like this does not strain my
    voice at all." [ASR F20, 1:14:21]. Secondary: soft-spoken and comforting, with a voice tone fans compare
    with Yukihana Lamy's. [Observed F2 §Personality, secondary]
  - Measured (F20; four 2024 windows): median pitch about 280–306 Hz (283–300 in chat, 293 while building,
    306 in the horror game); in the cleaner windows p10–p90 is about 210–445 Hz. High in this project's
    samples, near Kiara's (245–300 Hz) and above IRyS's (214–226 Hz). About 105–120 words per minute of
    speech in chat and building, 92 in the horror game, about 154 in the closing superchat list. Sample
    results only; not a ranking.
  - Provisional: a soft, light, airy head voice; unhurried; whisper-close for ASMR; sweet-but-ominous for
    threats; a deliberately deeper, sultry "Evil Fauna" as a comic bit.
- **Sounds off:** loud, brash shouting as a default; frequent strong swearing; a truly cold or menacing
  voice (her threats stay sweet); fast, clipped speech outside superchat lists; a sexualized read of "Evil
  Fauna" or of ASMR.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Soft, cheerful | "Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (F1) |
| Cozy chat | Unhurried, meandering, "I don't know" endings | "I'm pretty soft-spoken." (ASR F20) |
| Sweet threat | Same soft voice, ominous tail | "return to nature" (F2) |
| Evil Fauna | Deliberately deeper and sultry, theatrical | "You guys would fall too easily to Evil Fauna." (F2) |
| Flustered | "uuuu," giggles | (F2) |
| Improvised drama | Impassioned, mock-tragic | "Here you are, my love, my Forklift-chan." (F2) |
| Horror game | Murmured "oh no," "oh gosh"; reads game lines in character voices | (ASR F20) |
| Superchats | Quick, rhythmic names and thank-yous; spells | "If you heard your name, you will now be the recipient of my next spell." (ASR F20) |
| Deadpan bit | Flat, grandiose | "I will be the sole arbitrator of YouTube monetization." (ASR F20) |
| Sign-off | Warm, a promise | "Thank you so much for hanging out, and I will see you tomorrow." (ASR F20) |

### Sample Lines
1. "Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (Official F1)
2. "I was ready to be a kirin because that's what I am. But if they need me to be a giraffe, I guess I can
   do that" (ASR F20, 0:56:01; when something called her a "gaming idol giraffe")
3. "So how can you guys get a jet pack if I don't even have one? I am not the keeper of jet packs." (ASR F20, 3:24:38)
4. "It's not a scam! Fauna Mart is real!" (ASR F20, TzW6VRf4KjQ 0:49:09)
5. "Me. I'll be the mean manager." (ASR F20, TzW6VRf4KjQ 0:55:28; asked who would want the role)
6. "I'm not going anywhere, until I win you back." (F2 §Quotes, secondary)
7. "No! Don't fall! You guys would fall too easily to Evil Fauna." (F2 §Quotes, secondary)

## Appearance Anchors (avatar)
- 164 cm. Wavy light-green hair fading to blue-green at the tips, decorated with white five-petal flowers;
  horns like tree branches with leaves (kirin horns made of branches, "NOT deer antlers"); yellow eyes with
  a beauty mark under the right eye. [Official F1] [Observed F2 §Appearance, secondary]
- A short blue dress with golden ornaments under a white overcoat with a pink floral inner layer and a
  blue bow; a golden belt with green roses and water-drop gems; one long white sock and a golden bangle on
  the other ankle; barefoot. She can hold a levitating golden apple. [Observed F2 §Appearance, secondary]
- Mascot: Nemu, a sleepy princess kirin; fans: Saplings (little green sprouts); members: Faunatics; emoji
  🌿. Later outfits include a gothic dress (2024) and a cat-eared casual look. [Observed F2 §Mascot and fans,
  §2024, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Keeper of "Nature," the second concept created by the gods; a druid with kirin blood | [Official F1] |
| 2021-08-23 JST | Debuts with hololive English -Council- (first post on X: "oh deer") | [Official F1] [Observed F4] |
| 2022-05-14 | First original song "Let Me Stay Here" | [Observed F2 §2022] |
| 2022-10 | "BAE & FAUNA'S MONTH OF HORRORS" | [Observed F4, F3] |
| 2023-03-19 | 3D idol costume at hololive 4th fes. (day 2) | [Observed F2 §2023] |
| 2023-07-02 | hololive English 1st concert "-Connect the World-" | [Observed F2 §2023] |
| 2023-10-09 | Joins hololive English -Promise- | [Official] |
| 2024-12-14 | -Promise- musical "The Broken Promise" | [Observed F2 §2024] |
| 2024-12-27 | 1,000,000 subscribers; Kiara's HOLOTALK guest the same day | [Observed F2; F3 title] |
| 2024-12-31 | The World Tree is complete | [Observed F3 title] |
| 2025-01-03 | Graduates; last post on X: "LOVE & PEACE / Love, Fauna" | [Observed F2, secondary] |

## Relationship Map
Public exchanges only; counts are streams on Fauna's channel mentioning the other per year (2021 → 2024,
archive F3), a rough measure.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Nanashi Mumei | Council/Promise genmate (6 / 14 / 3 / 4) | Fauna's protectiveness turns possessive as a bit ("return to nature"); co-ops from Don't Starve to Dota 2; one of her last streams: "Mumei and Fauna investigate infighting on Wikipedia Talk Pages" (2024-12-20) | [Observed F2 §Personality; F3] |
| Hakos Baelz | Genmate (6 / 12 / 7 / 2) | At debut Bae called her "a natural mama, a soothing beauty, and someone who gives the best headpats"; a month of horror games (2022); an Amnesia: The Bunker off-collab (2023) | [Observed F2; F3, F4] |
| Ouro Kronii | Genmate (6 / 8 / 6 / 2) | Fauna described Kronii's "gap moe"; "Defusing bombs with Kronii but we can only speak in ASMR" (2021); Bread & Fred (2023) | [Observed Kronii file K8; F3] |
| IRyS | Promise genmate | "IRyS VS FAUNA SWITCH SPORTS BATTLE OF THE CENTURY" (2022); Pokémon Unite tournament practice (2023) | [Observed F3] |
| Tsukumo Sana | Council genmate (graduated 2022) | Sana designed the Council's "Beeg Smol" models; Fauna: "Go give [Sana] lots of love because she deserves it, even though she's a little bit... disgusting." | [Observed F2 §Quotes, secondary] |
| Gawr Gura | Her hololive oshi | Mario Kart ("GOOWA FWANA RACING"), a Dark Souls race (2024), and "Drawing Hololive Members From Memory with @GawrGura!" (2024-12-30) | [Observed F2 §Likes; F3] |
| Takanashi Kiara | Myth senior | "KIWAWA vs FAWNA" (Clubhouse 51, 2022); Minecraft Wither fight; Kiara's HOLOTALK 32nd guest (2024-12-27) | [Observed F3; Kiara archive] |
| Kaela Kovalskia | ID friend | "Fearless & Fearful vs Ghosts" (Phasmophobia, 2022); Minecraft ID server tour | [Observed F3] |
| -Justice- | Kouhai | "FAUNA'S DUNGEON: Forcing holoJustice to play a board game I made up" (2024); Silent Hill 2 with Gigi Murin (2024) | [Observed F3] |
| Shirogane Noel | JP senior | A member she admires and wanted to collab with | [Observed F2 §Trivia, secondary] |
| Nerissa Ravencroft | Advent kouhai | Nerissa's first reply to her on X: "Fauna-senpai!!! My Raven companion is named Shadow~" | [Observed—X post, research/x-posts.md] |

## Arc
- **Starting point:** her last active period (2024): Promise member, the World Tree project, ASMR and long
  game playthroughs.
- **Turning points / end point:** a story set after 2025-01-03 treats her as an alumna (memories only).

## Story Engine
- Trouble she brings: a sweet suggestion that is really a threat; a "return to nature" recruitment drive;
  an absurd game monologue; a horror game she insists on playing.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Fauna "plants" a sapling on Mumei's stream and refuses to leave.
  2. A whisper-ASMR segment that slowly becomes an evil-Fauna recruitment speech.
  3. The World Tree's last block: the genmates call in.
  4. Fauna referees Justice in a board game she invented, and the rules keep changing.
  5. A horror game with Bae where Fauna is calm and Bae is not, until the jump scare.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-08-23 (JST); graduated 2025-01-03; birthday March 21; 164 cm; fans Saplings; members
  Faunatics; emoji 🌿; mascot Nemu.
- Unit: -Council- (2021–23), hololive English -Promise- (2023–25).

## Sources (checked 2026-10-01)
- F1 Official profile ([Alum] Ceres Fauna): https://hololive.hololivepro.com/en/talents/ceres-fauna/
- F2 Virtual YouTuber Wiki, Ceres Fauna, read through its API on 2026-09-30 (secondary). Sections used:
  infobox, §Profile, §Personality, §Appearance, §2021–§2025, §Awards, §Mascot and fans, §Trivia (incl. the
  quote list), §Lore, §Likes and dislikes: https://virtualyoutuber.fandom.com/wiki/Ceres_Fauna
- F3 Stream archive metadata (titles, dates), Fauna's channel, via archive.ragtag.moe (read 2026-10-01):
  dqtrM2o4BnU, oRN_5TPDdhI, lHLx62THuYM, BUTS7lHUhzk, 5-9YHKhP2lY, bilsiV8t8io, -YdluR5bn1Y, sGeLlsQVcmA,
  XNiRgmK54Hg, NyIqYW0r_5w, 3Q_eeVdab0c, 02hUw815DG0, LQzb-HjIwzE, x_Ua2dWZYtk, w1UX1_0ra5A, 0nB58ASPAhw,
  3O4jBkgdWRQ; Kiara's channel RMvdq3JQ2n0 (HOLOTALK, 2024-12-27). Mention counts computed by Claude.
- F4 Fauna's X posts, via wiki citations (research/x-posts.md): 1427436065464360960 ("oh deer"),
  1576406178292064256 (MONTH OF HORRORS), 1872031411148042246 (Santa karaoke)
- F20 Claude's audio check (2026-10-01); see research/audio-check/fauna.md.

---

## [SW] Name
Ceres Fauna

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive English -Council-, hololive English -Promise-, hololive alum

## [SW] Other Names
Fauna, Faufau, Keeper of Nature, Mother Nature, Gamer Kirin, Ceres-chan

## [SW] Personality
Fauna streams as the Keeper of Nature, a druidic kirin four and a half billion years old, and plays the lore for laughs: she is the softest, most comforting presence in the room, and she uses that same soft voice to suggest you "return to nature," threaten to turn you into a tree, or let "Evil Fauna" out with a deeper, sultry voice. She is protective of her Saplings and of Mumei to the point of a possessive, yandere bit, yet gets embarrassed easily ("uuuu"). She commits to huge, patient projects (a Minecraft World Tree built over more than a hundred hours) and long playthroughs, loves horror games, cursed memes, animals and cats, and spins absurd improvised dramas out of games (a love monologue for a forklift, "pangolin crimes" in a zoo). She runs late and jokes that she is "always on time" on "Fauna Standard Time." Sincere moments are plain and warm: she thanks every Sapling she can by name.

## [SW] Background
She has no supernatural abilities; her lore is a performed persona. Fauna is a VTuber whose lore, a persona she plays for laughs, makes her the Keeper of "Nature," the second concept created by the gods: a druid with kirin blood whose horns are tree branches, who came online to win humans over and lead them back to nature. She debuted on 2021-08-23 with hololive English -Council-, joined -Promise- with IRyS, Kronii, Mumei and Bae in 2023, won VTuber Awards for ASMR and for chatting streams, sang at the first hololive English concert (2023) and in Promise's musical "The Broken Promise" (2024), finished her Minecraft World Tree on 2024-12-31, reached one million subscribers on 2024-12-27, and graduated on 2025-01-03. Her fans are Saplings, her members Faunatics, and her mascot is Nemu, a sleepy kirin.

## [SW] Physical Description
Fauna's avatar is 164 cm tall, with wavy light-green hair that fades to blue-green at the tips and is decorated with small white five-petal flowers, and horns like leafy tree branches (kirin horns, not deer antlers). Her eyes are yellow, with a beauty mark under the right one. She wears a short blue dress with golden ornaments under a white overcoat lined with pink flowers and closed with a blue bow, a golden belt set with green roses and water-drop gems, one long white sock and a golden bangle on the other ankle, and she goes barefoot. A golden apple sometimes floats at her hand; her sleepy kirin mascot Nemu may be curled up nearby.

## [SW] Dialogue Style
Soft, meandering English that circles with "like," "I guess," "kind of" and "actually," and often trails off on a gentle "I don't know." She talks to her Saplings warmly and, now and then, as their slightly spooky goddess: sweet reassurances with an ominous "...right?" at the end, invitations to "return to nature," spells cast on chat, a shop she insists is "not a scam." She commits fully to absurd bits and improvised drama, from love speeches to a forklift to grand deadpan ("I will be the sole arbitrator of YouTube monetization"), and laughs a flat, fake "ha ha ha" at her own puns. In games she reads the dialogue aloud in the characters' voices; scared, she murmurs "oh no," "oh gosh." Her own swearing stays mild ("dang," "what the heck"). She reads superchats as quick, rhythmic lists of names and thank-yous, adds "arigatou gozaimasu," and sings happy birthday when asked. Lines of hers: "I am not the keeper of jet packs." "I was ready to be a kirin because that's what I am. But if they need me to be a giraffe, I guess I can do that." "Me. I'll be the mean manager."

## [SW] Catchphrases
"Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (official greeting); "Konfauna!" (greeting); "return to nature" (her invitation and threat, above all to Mumei); "uuuu" (embarrassed); "four and a half billion" (her age, when called old); "Evil Fauna" (her sultry-voiced alter ego bit); "Fauna Standard Time" (her lateness) and "I'm always on time." (said when late); "It's not a scam! Fauna Mart is real!" (her shop bit); "If you heard your name, you will now be the recipient of my next spell." (while reading superchats); "I am not the keeper of jet packs." (refusing a request); "Plant them, plant them…" (a chant after a list of names); "Thank you so much for hanging out, and I will see you tomorrow." (sign-off); "LOVE & PEACE" (her last post)

## [SW] Voice & Delivery
A soft, light, mid-high speaking voice (she describes herself as soft-spoken and talking in her head voice) that stays gentle even when she is excited, at an unhurried, meandering pace. Her comfort voice drops to a whisper for ASMR. Her mischief comes out sweet: a threat or a "return to nature" in the same soothing tone, and for "Evil Fauna" a deliberately deeper, sultry voice. When flustered she trails into "uuuu" and small giggles; when scared she murmurs "oh no" rather than shouting, and she reads game dialogue aloud in the characters' voices. Reading superchats she speeds up into a warm, rhythmic list of names and thank-yous.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, light, airy head voice, high in this project's samples (about 280–306 Hz), unhurried and meandering (about 105–120 words a minute in chat), quick only in superchat lists; American English. Default tags: [soft, gentle]. By situation: opening [soft, cheerful]; cozy chat [soft, meandering]; sweet threat or "return to nature" [sweetly] then [softly ominous]; Evil Fauna bit [deeper, sultry, theatrical], kept comic; flustered [embarrassed]; improvised drama [mock-dramatic, impassioned]; horror game [nervous, murmuring]; reading game dialogue [in a character voice]; superchat list [quick, rhythmic, warm]; grand deadpan [deadpan]; ASMR [whispering, close]; sincere [warm, plain]; sign-off [warm, cheerful]. With people (direction drawn from Relationships): Mumei [sweet, possessive]; Bae [amused, calm]; Kronii [teasing]; Gura [giggly, fangirling]; Justice and other kouhai [gentle, mischievous senpai]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [flustered whine] uuuu; [soft giggle]; [flat, fake laugh] ha ha ha (after her own pun); [quiet gasp]. Keep in the words: "like," "I don't know" (often as a soft sentence ending), "I guess," "kind of," "actually," "oh no," "oh gosh," "oh my gosh"; her own swearing stays mild ("dang," "what the heck"). Pronunciation guide (provisional, untested): Ceres /ˈsɪəɹiːz/, Fauna /ˈfɔːnə/, kirin /ˈkɪɹɪn/, Konfauna /kɑnˈfɔːnə/, Nemu /ˈnɛmu/. Not as default: loud shouting, constant swearing, a cold menacing voice. Never a sexualized read of Evil Fauna or of ASMR.

## [SW] Motivation
In her lore, Fauna wants to win humans over and lead them back to nature. As a streamer she wanted to comfort her Saplings, sing, learn Japanese, collab with her genmates in person, speedrun games and voice-act in a game, and to finish what she started, like the World Tree.

## [SW] Relationships
Nanashi Mumei (graduated 2025): Council and Promise genmate; Fauna's protectiveness of her became a possessive, yandere bit, inviting Mumei to "return to nature" whenever she was upset, while Mumei's own dark side left it unclear who needed protecting from whom; one of Fauna's last streams was the two of them reading Wikipedia talk-page fights (2024-12). Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise genmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): designed Council's "Beeg Smol" models; Fauna told fans to give Sana love "even though she's a little bit... disgusting." Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024); Silent Hill 2 with Gigi Murin. Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai who greeted her on X as "Fauna-senpai!!!"

## [SW] Secrets
(none)

---

## Open Questions
1. Her official greeting ("Konfauna~ Your gaming idol kirin Ceres Fauna is here!") was not heard in the
   sampled 2024 opening, which began mid-setup. Kept on the card as her greeting; confirm.
2. "Evil Fauna," the yandere lines and the forklift dramas come from the wiki's quote list (secondary, no
   timestamps). They are kept as bits, with full sentences quoted only in the dossier and in two Sample
   Lines. Keep?


==================== FILE: 20261001-0430-character-Nanashi-Mumei/claude-draft.md ====================

---
kind: character
name: "Nanashi Mumei"
sw_section: Characters
---

# Character File: Nanashi Mumei

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Mumei graduated from hololive
> on 2025-04-27 (2025-04-28 JST); her "present" in this file is her last active period (late 2024 to April
> 2025), per the project's recency rule. Nothing about the performer behind the avatar: graduation reasons,
> health and voice-rest breaks, and the pet she calls "Animal" are deliberately left out. In stories she
> knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; M20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (M#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 2.1 hours of archived 2025 speech (M20: a Q&A stream
> with its opening and closing, a DOOM Eternal finale and an Overwatch 2 collab), plus a 30-minute drawing
> window with no speech by design ("Doodles In Complete Silence"). The audio was machine-transcribed and
> acoustically measured; transcripts were reviewed in context, without independent listening verification.

## One-line Concept
The Guardian of Civilization, a forgetful wandering owl who has watched humankind for millennia and
streams as a soft, cute, low-energy artist who will suddenly screech, draw something horrifying, or remind
chat that "civilization is temporary": Council's little sister who turned out to be the one everyone
should be protected from, until she graduated in April 2025. [Official M1] [Observed M2, secondary]

## Core Drive
- **Want:** in her own goals: a song in a rhythm game, learn Japanese (again), collab with senpai, improve
  and learn new skills, write a song on guitar, and a 3D live. [Official M1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** she treats viewers' time as precious and tells tired fans to go to sleep;
  she is happy when Hoomans are inspired to draw. [Observed M2 §Personality, secondary]

## Core Contradiction
The cutest, gentlest voice in her generation (Bae's words at debut) attached to "psychopathic," macabre
humor: her drawings turn Tim Burton-esque or demonic, and the "little sister" everyone protects became, in
the wiki's words, someone you are not sure who needs protecting from whom. [Observed M2 §Personality,
secondary]

## Behavioral Traits
1. She calls herself "low energy" and awkward; when she runs out of topics she fills silence with impromptu
   singing and noises. [Observed M2 §Personality, secondary]
2. Surprised or agitated, she screeches high; caffeine makes her spontaneous and loud. [Observed M2
   §Personality, secondary]
3. She forgets things (her lore says too many owl transformations made her brain "more bird"), including
   her own original name; her paper-bag mascot is just "Friend" so she can't forget it. [Official M1]
   [Observed M2 §Lore, §Mascots and fans, secondary]
4. She draws constantly ("MUMEI DRAWS," doodles of 450 fan suggestions), and the results drift dark.
   [Observed M2; M3 titles]
5. She reads superchats with a gavel: "don don!" [Observed M2 §Quotes, secondary]
6. She plays shooters seriously (Overwatch 2, DOOM, Halo, Apex) and invites friends into them. [Observed M3
   titles]

## Voice Profile
- **Greetings / sign-offs:**
  - "Oh hi! Hoo's this? Nanashi Mumei!" (official greeting) [Official M1]; "Oh hi!" (the wiki's caption for
    her) [Observed M2, secondary]. Her 2025 Q&A opens with her caught off guard by her own music, then "Oh,
    hi" and "…hi everybody. What's up? How are you?" [ASR M20, 7vxLfdBqFac 0:03:20–0:03:35; shared spans]
  - Sign-off: "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." then "bye-bye for now"
    and a dozen more "bye-bye"s. [ASR M20, 1:31:02; shared spans]. In the same stream she promised a giant
    "don don" at the end of every stream (paraphrase; the transcripts mishear the word). [ASR M20, 1:22:19]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "don don!" → her spoken gavel after thanking a superchat ("Thank you [name] for the supa, don don!") →
    every superchat reading. [Observed M2 §Quotes, secondary]; six "Don don!" in 30 minutes of Overwatch
    [ASR M20, zfQJZ6LetCc 0:56:50, first model]
  - "I'm moomin'" / "Today we moom" / "A Moom's gotta moom what a Moom's gotta moom" → her verb, "moom."
    [Observed M2 §Quotes, secondary]
  - "Civilization is temporary, humanity is temporary, you are all going to die one day!" → the cheerful
    macabre guardian bit. [Observed M2 §Quotes, secondary]
  - Guardian authority, ranking chip flavors: "…guardian of civilization! … I decide everything for
    humanity." [ASR M20, 0:19:41; the models differ on "I'm a"/"I'm"]; after her own answer: "…but what do I
    know? Everything." [0:31:35]; "Good job homo sapien." [0:26:17]
  - "Yippee" / "hooray" → cheering, often sarcastic: "I love talking about myself. Yippee, yippee. Hooray."
    (five of each in the first ten minutes) [ASR M20, 0:05:43]
  - "Oh dear" → mild dismay: "Oh dear, that was pointless." [ASR M20, zfQJZ6LetCc 0:52:11]; "Oh, dear. … I
    guess I already started it, so I'm in the middle of it now." [7vxLfdBqFac 0:05:02]
  - "Owie! Owie! Owie!" → taking damage. [ASR M20, zfQJZ6LetCc 0:52:46]
  - Owl puns ("Hoo's this?", Hoomans); ":D" in her stream descriptions. [Official M1] [Observed M2]
- **Macabre and grandiose humor:** a cute voice with dark content: drawings that turn Tim Burton-esque or
  demonic, cheerful reminders that everyone dies. [Observed M2 §Personality, secondary]. Bravado: "I've never
  been scared of anything ever." [ASR M20, 0:26:39]. Ranking who she'd beat at arm wrestling: "I think I
  would win against Gura, Kiara, IRyS, Nerissa, and Mococo"; she moved Biboo to the losing side ("she is a
  rock") and concluded that most of EN could beat her: "But I have other skills and things that make me
  special, so whatever." [ASR M20, 0:23:52–0:27:44; the models disagree on the word "EN"]
- **Self-interruption & forgetting:** she loses her train of thought and says so, cuts tangents with
  "anyways" (11 times in 30 minutes of Q&A) and apologizes often ("sorry," 11). She embraces not knowing:
  "Sometimes you go through life just not knowing stuff. You can't know everything." … "It's okay not to
  know stuff sometimes. Yeah, unless you're me. Exactly, unless you're me." [ASR M20, 1:24:20–1:24:35]
- **In games:** short, bright reactions: "uh oh" (7 in 45 minutes of DOOM), "oh shoot," "oh dear," "oh no,"
  "nice" (21 in 30 minutes of Overwatch), "yay" (9); repetition when something absurd happens (one line
  repeated four times in DOOM); "I'm too poor. No money." (buying upgrades) [5xL_7PGd3rk 2:07:07]; "I don't
  care, I don't care anymore." [2:43:32]. Otherwise quiet: about 49 words per minute of speech in DOOM.
  [ASR M20]
- **Vocabulary / fillers:** "okay" constantly (25 in the 30-minute Q&A, 31 in the 12-minute closing), "I
  don't know" (19), "you know" (15), "I guess" (11), "like" (about 1 word in 70), "oh my gosh," "oh my
  goodness." Talks to "you guys," "everybody," "y'all"; fans: Hoomans. [ASR M20, first-model counts]
- **Profanity:** mild in the sample: "shoot," "heck," "oh dear"; no strong swearing heard in about two
  hours. Her edge is macabre content in a cute voice. [ASR M20]
- **Laughs, noises:** high screeches when surprised or agitated; impromptu singing and noises to fill
  silence; sing-song "doo doo doo" while setting up; good at cat and dog impressions. [Observed M2
  §Personality, §Miscellaneous, secondary] [ASR M20]
- **Code-switching:** Japanese mid-English, mostly in games: "Saikou! Saikou desu!" (seven "saikou" in 30
  minutes of Overwatch, first model), calling herself "yowai" (weak): "…I have the least damage in the
  game." [ASR M20, zfQJZ6LetCc 0:40:29; both models hear the Japanese word, spelled differently]; "arigato."
  Learning Japanese "again" was a stated goal; bilingual stream titles; Towa calls her "Mumi-chan."
  [Official M1] [Observed M2; M3 titles]
- **Rhythm & rhetoric:** two speeds. Chatting, she is fast and scattered (about 156–168 words per minute of
  speech in the Q&A and closing), with restarts, run-on asides and words in threes and fours ("okay, okay,
  okay"; the string of "bye-bye"s). In games she is slow and sparse (49 in DOOM, 84 in Overwatch). [ASR M20]
- **Timbre / pitch / pace (for voice performance):**
  - Secondary: "the cutest voice in hololive -Council-" (Bae at debut); soft-spoken, with "an unexpectedly
    wide vocal range" and high screeches. [Observed M2 §Personality, secondary]
  - Measured (M20; five 2025 windows): median pitch about 284–311 Hz (284–293 in the Q&A windows, 302 in
    DOOM and 311 in Overwatch, with game audio and teammates mixed in); p10–p90 about 205–480 Hz. High in
    this project's samples, close to Fauna's (280–306 Hz). Sample results only; not a ranking.
  - Provisional: soft, small and sweet by default, a little sleepy at low energy; quick and scattered when
    chatting; a sudden high screech; flat, cheerful delivery for the macabre lines.
- **Sounds off:** a booming or aggressive voice; heavy swearing; a deep, sinister villain voice for her
  dark jokes (the joke is that she says them cutely); constant high energy.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Soft, caught off guard | "Oh hi! Hoo's this? Nanashi Mumei!" (M1) |
| Chatting | Fast, scattered; "okay," "anyways," "sorry" | "I love talking about myself. Yippee, yippee. Hooray." (ASR M20) |
| Guardian authority | Mock-grand, deadpan | "I decide everything for humanity." (ASR M20) |
| Macabre bit | Cute, cheerful | "Civilization is temporary…" (M2) |
| Startled | High screech | (M2) |
| Shooter games | Murmured and sparse; bright "nice," "yay," "uh oh" | "Oh dear, that was pointless." (ASR M20) |
| Hurt in a game | Whiny repetition | "Owie! Owie! Owie!" (ASR M20) |
| Superchats | Thanks, then the gavel | "don don!" (M2) |
| Philosophical | Soft, matter-of-fact | "Sometimes you go through life just not knowing stuff." (ASR M20) |
| Sign-off | Many goodbyes | "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." (ASR M20) |

### Sample Lines
1. "Oh hi! Hoo's this? Nanashi Mumei!" (Official M1)
2. "…guardian of civilization! … I decide everything for humanity." (ASR M20, 7vxLfdBqFac 0:19:41)
3. "It's okay not to know stuff sometimes. Yeah, unless you're me. Exactly, unless you're me." (ASR M20, 1:24:35)
4. "Good job homo sapien." (ASR M20, 0:26:17)
5. "I'm too poor. No money." (ASR M20, 5xL_7PGd3rk 2:07:07)
6. "Okay, are we ready? Are we bracing ourselves? We got our tissue box nearby." (ASR M20, 0:11:33; before
   reading her genmates' questions)
7. "Civilization is temporary, humanity is temporary, you are all going to die one day!" (M2 §Quotes, secondary)

## Appearance Anchors (avatar)
- 156 cm. Long light-brown hair in a high ponytail with a black tie and two brown feathers standing in a
  "V"; brown eyes with a yellow gradient. [Official M1] [Observed M2 §Appearance, secondary]
- A white puff-sleeved blouse with tan corset lacing under a brown gold-trimmed corset; a short red ruffled
  skirt with a brown outer skirt; mismatched black stockings with thigh straps; a brown and beige feathered
  cape with teal lining; fingerless gloves; a belt with a lantern, a pouch and a small sheathed dagger;
  brown heeled ankle boots. [Observed M2 §Appearance, secondary]
- Mascot: Friend, a paper bag with a drawn mouth, a cross-shaped plaster and rune lettering, who "escapes"
  now and then; a small owl, Hootsie. Fans: Hoomans; members: Owl Pals; emoji 🪶 and the text face ":D".
  [Observed M2 §Mascots and fans, §Miscellaneous, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Guardian of "Civilization," the concept made by mankind rather than the gods; chose an owl form; has forgotten her name and age | [Official M1] [Observed M2 §Lore] |
| 2021-08-23 JST | Debuts with hololive English -Council- (first post on X: "oh man") | [Official M1] [Observed M4] |
| 2022-01-17 | First original song "A New Start" | [Observed M2 §2022] |
| 2023-03-18/19 | 3D idol costume and main 3D model at hololive 4th fes.; sang a DECO*27 song with Kiara on the holo*27 stage | [Observed M2 §2023; M4] |
| 2023-10-09 | Joins hololive English -Promise- | [Official] |
| 2023-10-10 | Second original song "mumei" | [Observed M2 §2023] |
| 2024-01-26 | 1,000,000 subscribers, the first of Council/Promise | [Observed M2 §2024] |
| 2024-08-05 | 3D birthday live "Outside the Box" | [Observed M3 title] |
| 2025-02-14 | 3.0 Live2D model | [Observed M2 §2025] |
| 2025-03-09 | 6th fes. "Color Rise Harmony," day 2 | [Observed M2 §2025] |
| 2025-04 | A farewell month of collabs across hololive; last chatting stream with calls (04-26); 3D graduation stream (04-27, 04-28 JST) | [Observed M2; M3 titles] |

## Relationship Map
Public exchanges only; counts are streams on Mumei's channel mentioning the other per year (2021 → 2025,
archive M3), a rough measure.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Hakos Baelz | Genmate (4 / 31 / 27 / 5 / 3) | Her most frequent collab partner: Mad-Lib theatre (2021), an off-collab "I Found A Rat In My House!!!" (2024), "bae wants to play!!!" (Overwatch 2, 2025) | [Observed M3] |
| Ceres Fauna | Genmate (4 / 30 / 26 / 4) | Fauna's protectiveness turns possessive as a bit; co-ops for years; "Mumei and Fauna investigate infighting on Wikipedia Talk Pages" (2024-12-20) | [Observed M2; M3; Fauna file] |
| Ouro Kronii | Genmate ("KronMei"; 5 / 27 / 25 / 1 / 2) | "The Grim Adventures of Mumei and Kronii!" (Minecraft, 2021); We Were Here Forever; Untitled Goose Game (2025); a "Donut Hole" cover MV together (2025-04-11) | [Observed M3; Kronii channel] |
| Tsukumo Sana | Council genmate (graduated 2022) | Human: Fall Flat (2021); Sana sent a prerecorded message for Mumei's 2022 birthday | [Observed M2 §Miscellaneous; M3] |
| IRyS | Promise genmate | Mumei's last solo-channel game stream was with her: "【OVERWATCH 2】 the final stream !!! with @IRyS" (2025-04-22) | [Observed M3] |
| Takanashi Kiara | Myth senior; bird unit HOLOTORI | "BUILDER BIRBS" (2021); "Kiwawa & Mumeiwi" (2022); the 4th fes. holo*27 stage (2023); "two smol beans" (2025); HOLOTORI R.E.P.O. (2025-04-18); Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies" | [Observed M2 infobox; M3; M4] |
| Gawr Gura | Myth senior | "【VOICE CHALLENGE】in the same room? 💙🤎 #gumei" (Gura's channel, 2023); Overwatch; "ROOM REVIEW with @NanashiMumei" (2025-04-21) | [Observed M3; Gura channel] |
| Watson Amelia | Myth senior | Overwatch and VR field trips (2022); "ANIMALS with Ame & Moom" (2024-09-29, Ame's last regular week) | [Observed M3] |
| Ninomae Ina'nis | Myth senior, fellow artist | Drawing collabs (2023-01, 2025-04-21 "doodles with @NinomaeInanis") | [Observed M3] |
| Mori Calliope | Myth senior | "ANATOMY REVIEW" streams (with Calli and Sana, 2022; solo, 2025) | [Observed M3] |
| Nerissa Ravencroft | Advent kouhai | "EMO HOURS: IT WAS NEVER A PHASE with NERISSA" (2023); "SAD GIRL HOURS" (2025-04-20) | [Observed M3] |
| Koseki Bijou | Advent kouhai ("Stone Age") | Portal 2 co-op (2023); Marvel Rivals (2025) | [Observed M2 §Relationships; M3] |
| Gigi Murin, Cecilia Immergreen | Justice kouhai (Cecilia: "Automatowl"; calls her "Myumyei") | "A Towl and a Gremlin" (Echo Point Nova with Gigi, 2024–25); an alphabet tier list with both (2025) | [Observed M2; M3] |
| FUWAMOCO | Advent kouhai ("Fuwamoomco") | Overwatch "baus baus" (2025-03) | [Observed M2; M3] |
| Takane Lui, Tokoyami Towa, Akai Haato | JP seniors | "Bird Sisters" Q&A with Lui (2025); Towa calls her "Mumi-chan"; Minecraft "Peace & Love with HAACHAMA" (2025) | [Observed M2 infobox; M3] |

## Arc
- **Starting point:** her last active period (late 2024 to April 2025): Promise member, artist and shooter
  fan, and a farewell month of collabs.
- **Turning points / end point:** a story set after 2025-04-27 treats her as an alumna (memories only).

## Story Engine
- Trouble she brings: forgetting the plan mid-plan; a drawing that becomes a horror; a gavel "don don!";
  a sudden screech; a cheerful reminder that everyone will die someday.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Mumei forgets a collab she organized, then remembers mid-stream and screeches.
  2. A drawing request ("draw Kronii as a cute bunny") that ends in a cosmic horror.
  3. Fauna tries to "return Mumei to nature" during a shooter match.
  4. HOLOTORI meets for a bird-only game night; Mumei keeps forgetting she's a bird.
  5. Friend escapes again and wanders onto someone else's stream.

## Secrets & Foreshadowing
- **Truth:** none assigned. Her original name is official open lore (she doesn't remember it).

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-08-23 (JST); graduated 2025-04-27 (04-28 JST); birthday August 4; 156 cm; fans Hoomans;
  members Owl Pals; mascot Friend; emoji 🪶.
- Unit: -Council- (2021–23), hololive English -Promise- (2023–25).

## Sources (checked 2026-10-01)
- M1 Official profile ([Alum] Nanashi Mumei): https://hololive.hololivepro.com/en/talents/nanashi-mumei/
- M2 Virtual YouTuber Wiki, Nanashi Mumei, read through its API on 2026-09-30 (secondary). Sections used:
  infobox, §Personality, §Appearance, §2022–§2025, §Mascots and fans, §Relationships, §Quotes, §Lore,
  §Likes and dislikes, §Miscellaneous: https://virtualyoutuber.fandom.com/wiki/Nanashi_Mumei
- M3 Stream archive metadata (titles, dates), Mumei's channel, via archive.ragtag.moe (read 2026-10-01):
  p_vaBM3sjro, 6ebZmlXEphs, -L2E0hwdYlA, fMK4GmM4WT8, 7Ezl57s7sqA, _lqd0JSWlIs, d5n0ZtjwVsA, 50-HQZj5FVg,
  Nllze52PrPY, Z8WwtY2KT30, zCHHsb9eMbk, 1sMuXpAVILg, wGaN8Wi-BNc, 60r1O06S4jo, 74LkHRCWcJs, EQ5CVr3bb5U,
  WSM66DoRFV0, Z6KzayFYieI, sUF9wbgrLD8, QA7OA1ew5HI, ENFvQFWoFFA, dBLX2LLypwo, fEO6kSCseE0, TgeztgEJjMc,
  9LWzUU9rxTs, 0CxQ7XOVWZA, tTABc1SlO8U, gl7CwlEg2ZI; Kronii's channel UOYMqqk3quw ("Donut Hole"); Kiara's
  channel Qw_tfe1kFRc (HOLOTALK), uPd_Tkj5zxI; Gura's channel k7dTnCl2pVA, ZP8E9WH71OU. Mention counts
  computed by Claude.
- M4 Mumei's X posts, via wiki citations (research/x-posts.md): 1427436487373688833 ("oh man"),
  1637345257632169987 (4th fes. with Kiara), 1750772639805886691 (1M)
- M20 Claude's audio check (2026-10-01); see research/audio-check/mumei.md.

---

## [SW] Name
Nanashi Mumei

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive English -Council-, hololive English -Promise-, HOLOTORI, hololive alum

## [SW] Other Names
Mumei, Moom, Moomers, Meimei, Moomsies, Mumi-chan, Myumyei, Guardian of Civilization, Towl

## [SW] Personality
Mumei streams as the Guardian of Civilization, a wandering owl who has watched humankind for thousands of years and forgotten most of it, her own name included, and she plays the lore with a straight face and a cute voice. By default she is soft, low-energy, a little awkward and scattered: she loses her train of thought, apologizes, says "anyways" and moves on, and fills silences with random singing and noises. Under the softness runs a gleeful macabre streak: her drawings drift Tim Burton-esque or demonic whatever the request, she cheerfully reminds chat that civilization is temporary and everyone will die one day, and her genmates' wish to protect their "little sister" has become a joke about who needs protecting from whom. She claims grand authority as the guardian ("I decide everything for humanity"), brags that she has never been scared of anything, and admits most of EN could beat her at arm wrestling. Caffeine makes her loud and spontaneous; surprise makes her screech. She loves drawing, rhythm and simulation games, shooters like Overwatch and DOOM, Vocaloid and "pop punk metal with yelling," and she treats her Hoomans' time as precious, telling tired fans to go to sleep. Every superchat gets her gavel: "don don!"

## [SW] Background
She has no supernatural abilities; her lore is a performed persona. Mumei is a VTuber whose lore makes her the Guardian of "Civilization," the only member of her generation created not by the gods but by mankind's efforts; she chose an owl's form for wisdom, and too many transformations made her brain "more bird," so she forgets things, including her original name and her age. Lonely on her travels, she made a friend out of paper: a paper bag called simply "Friend," so she can't forget his name. She debuted on 2021-08-23 with hololive English -Council-, released the original songs "A New Start" (2022) and "mumei" (2023), joined -Promise- in 2023, reached one million subscribers on 2024-01-26 (the first in Council and Promise), held the 3D birthday live "Outside the Box" on 2024-08-05, and graduated on 2025-04-27 (04-28 JST) after a farewell month of collabs and covers with members across hololive. Her fans are Hoomans, her members Owl Pals, and her stream descriptions end with ":D".

## [SW] Physical Description
Mumei's avatar is 156 cm tall, with long light-brown hair in a high ponytail, tied with a black band and two brown feathers standing up in a V, and brown eyes with a yellow gradient. She dresses like a fantasy adventurer: a white puff-sleeved blouse under a brown, gold-trimmed corset, a short red ruffled skirt with a brown outer skirt, mismatched black stockings with thigh straps, a brown and beige feathered cape lined in teal, fingerless gloves, and a belt hung with a lantern, a pouch and a small dagger. Her paper-bag mascot Friend, with a drawn mouth and a cross-shaped plaster, sometimes floats beside her.

## [SW] Dialogue Style
Soft, quick, scattered English that runs on with "okay," "I guess," "you know" and "I don't know," then cuts itself off with "anyways" or "sorry" and starts again; she repeats words in threes and fours ("okay, okay, okay"; a dozen "bye-bye"s). She says macabre things in the same cute tone as everything else, and grand ones as the guardian ("I decide everything for humanity"; "…but what do I know? Everything."). She cheers with "yippee" and "hooray," often sarcastically ("I love talking about myself. Yippee, yippee. Hooray."), and reacts in games with short bright words: "uh oh," "oh shoot," "oh dear," "oh no," "nice," "yay," "owie owie owie!" Her swearing is mild ("shoot," "heck"). She drops Japanese into games ("Saikou desu!", calling herself "yowai," weak) and hits her spoken gavel, "don don!", after thanking each superchat. Lines of hers: "Good job homo sapien." "It's okay not to know stuff sometimes. Yeah, unless you're me." "I'm too poor. No money." "Okay, are we ready? Are we bracing ourselves? We got our tissue box nearby."

## [SW] Catchphrases
"Oh hi! Hoo's this? Nanashi Mumei!" (official greeting); "Oh hi!" (greeting); "don don!" (her gavel after each superchat thanks); "I'm moomin'" and "Today we moom" (her verb, moom); "Civilization is temporary, humanity is temporary, you are all going to die one day!" (the macabre guardian bit); "I decide everything for humanity." (guardian authority); "…but what do I know? Everything." (after giving her opinion); "Yippee… hooray" (cheering, often sarcastic); "Oh dear" (mild dismay); "Owie! Owie! Owie!" (hurt in a game); "Saikou desu!" (a win); "Good job homo sapien." (praising humans); "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." (sign-off, followed by many "bye-bye"s); ":D" (in writing)

## [SW] Voice & Delivery
A soft, small, sweet voice, high in the register, that sounds cute and a little sleepy at its low-energy default and turns quick and scattered when she chats, tumbling through asides and apologies. Her range is wider than it first seems: surprise or agitation brings a sudden high screech, caffeine makes her loud, and she fills silences with impromptu singing, sing-song noises and good cat and dog impressions. Her darkest jokes come in the same cute, cheerful tone, never a sinister one. In shooters she goes quiet and murmuring, broken by bright little "nice," "yay" and "uh oh," and Japanese words slip in.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, small, sweet voice, high in this project's samples (about 284–311 Hz), quick and scattered in chat (about 156–168 words a minute of speech), slow and sparse in games; American English. Default tags: [soft, cute, low-energy]. By situation: opening [soft, caught off guard]; chatting [quick, scattered]; losing her train of thought [distracted] then [apologetic]; guardian authority [mock-grand, deadpan]; macabre bit [cheerful, cute], never sinister; sarcastic cheer [flat]; startled [screeching]; shooter games [murmuring, focused], then [bright] for "nice!"; hurt in a game [whiny]; superchats [warm], then the gavel [brisk]; philosophical [soft, matter-of-fact]; sign-off [warm, sing-song], repeated. With people (direction drawn from Relationships): Fauna [deadpan, faintly menacing]; Kronii [playful, chaotic]; Bae [chaotic, giggly]; Kiara [smol, sweet]; Gura [giggly]; IRyS [cheerful teammate]; Biboo [teasing]; Nerissa [mock-gloomy]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [high-pitched screech]; [gavel call] don don!; [sing-song humming]; [small giggle]; [whiny] owie owie owie! Keep in the words: "okay" (often in threes), "anyways," "sorry," "I guess," "you know," "I don't know," "oh dear," "uh oh," "oh shoot," "oh my gosh," "yippee," "hooray"; mild words only ("shoot," "heck"). Pronunciation guide (provisional, untested): Mumei /muːˈmeɪ/, Nanashi /nəˈnɑːʃi/, Hoomans /ˈhuːmənz/, moom /muːm/, saikou /saɪˈkoʊ/, yowai /joʊˈwaɪ/. Not as default: loud or aggressive delivery, a deep sinister voice for the dark jokes, heavy swearing.

## [SW] Motivation
In her lore, Mumei records human history so it isn't forgotten, though she forgets things herself. As a streamer she wanted to grow: a song in a rhythm game, learning Japanese again, collabs with her senpai, new skills like guitar, and a 3D live, which she held in 2024.

## [SW] Relationships
Ceres Fauna (graduated 2025-01): Council and Promise genmate whose protectiveness became a possessive bit, inviting Mumei to "return to nature" whenever she was upset, until Mumei's own dark side made it unclear who needed protecting from whom; one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate and her most frequent collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). Ouro Kronii ("KronMei"): genmate and frequent partner, from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). IRyS: Promise genmate; Mumei's last solo game stream was Overwatch with her (2025-04-22). Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday. Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Mumei was Kiara's HOLOTALK guest in her last week. Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week. Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week. Ninomae Ina'nis: fellow artist, drawing collabs. Mori Calliope: "ANATOMY REVIEW." Nerissa Ravencroft: "EMO HOURS" (2023) and "SAD GIRL HOURS" (2025). Koseki Bijou ("Stone Age"): Portal 2 and Marvel Rivals; at arm wrestling Mumei rates her a loss because "she is a rock." Cecilia Immergreen ("Automatowl"; calls her "Myumyei") and Gigi Murin: "A Towl and a Gremlin." FUWAMOCO ("Fuwamoomco"): Overwatch. JP seniors: Takane Lui (a "Bird Sisters" Q&A), Tokoyami Towa (calls her "Mumi-chan"), Akai Haato (Minecraft).

## [SW] Secrets
(none)

---

## Open Questions
1. "don don!" rests on the wiki and first-model counts in the Overwatch window (the second model was not run
   on those lines). Kept as her signature; confirm.
2. Wiki quote lines ("Civilization is temporary…", the "moom" verb) are secondary, without timestamps, and
   kept as catchphrases. Keep?


==================== FILE: 20261001-0454-world-Fauna-and-Mumei-Pairs/claude-draft.md ====================

---
kind: world
name: "Fauna and Mumei Pairs"
sw_section: Worldbuilding
---

# World Element: Fauna and Mumei Pairs (with each other and the cast)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-01. Evidence labels as in the other world files. "Archive" = stream titles and
> descriptions on the members' channels (archive.ragtag.moe, S1); counts are streams mentioning the other
> per year, a rough measure that does not rank closeness. Fauna graduated on 2025-01-03 and Mumei on
> 2025-04-27 (04-28 JST): at the 2026-09-30 baseline both pairs-with-them are memories, and stories set
> before those dates can use them freely.

## One-line Concept
Council's nature and civilization: the soft kirin who wanted to "return" everyone to nature and the
forgetful owl she guarded a little too possessively, plus the web they wove with Kronii, IRyS, Myth and
the kouhai before they graduated in 2025.

## Type
Relationship web.

## Fauna and Mumei
- **Each other** (Mumei's channel 4 / 30 / 26 / 4; Fauna's 6 / 14 / 3 / 4, 2021 → 2024): Council genmates
  from the first week (Don't Starve Together, 2021-08-25; Minecraft "Adventuring with Mumei!"). The wiki
  describes Fauna as protective of Mumei "to the point of possessiveness and extreme jealousy," inviting her
  to "return to nature" whenever she is upset, while Mumei's own darker side later made it unclear "who
  needs to be protected from whom." They revealed their fourth outfits the same weekend (2024-02), and one of Fauna's last
  streams was "Mumei and Fauna investigate infighting on Wikipedia Talk Pages" (2024-12-20).
  [Observed S2 Fauna §Personality, S3 Mumei §Personality, §2024, secondary; S1]

## With the cast
- **Kronii:** Mumei and Kronii ("KronMei") are among Mumei's most frequent partners (5 / 27 / 25 / 1 / 2):
  "The Grim Adventures of Mumei and Kronii!" (2021), We Were Here Forever (2022), Untitled Goose Game
  (2025-02), and a "Donut Hole" cover MV together (2025-04-11). Fauna and Kronii: "Defusing bombs with
  Kronii but we can only speak in ASMR" (2021), Bread & Fred (2023); Fauna described Kronii's "gap moe."
  [Observed S1; Kronii file K8]
- **IRyS:** Promise genmates from 2023 (CouncilRyS before that). "IRyS VS FAUNA SWITCH SPORTS BATTLE OF THE
  CENTURY" (2022); Mumei's last solo-channel game stream was "【OVERWATCH 2】 the final stream !!! with
  @IRyS" (2025-04-22). [Observed S1]
- **Kiara:** Mumei and Kiara are birds in HOLOTORI (with Subaru, Reine and Lui): "BUILDER BIRBS" (2021),
  "Kiwawa & Mumeiwi" (2022), a DECO*27 song together on the 4th fes. holo*27 stage (2023), "two smol
  beans" (2025-03-26) and Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies." Fauna and
  Kiara: "KIWAWA vs FAWNA" (2022), Pokémon Unite practice (2023), and Fauna was HOLOTALK's 32nd guest
  (2024-12-27), a week before she graduated. [Observed S1; S3 infobox; S4]
- **Gura:** Gura is Fauna's hololive oshi; Mario Kart ("GOOWA FWANA RACING," 2021), a Dark Souls race
  (2024) and "Drawing Hololive Members From Memory with @GawrGura!" (2024-12-30). Mumei and Gura:
  "【VOICE CHALLENGE】in the same room? 💙🤎 #gumei" (2023) and a "ROOM REVIEW" (2025-04-21).
  [Observed S2 §Likes; S1]
- **Ame:** Mumei and Ame: Overwatch and a VR field trip (2022), "ANIMALS with Ame & Moom" (2024-09-29, in
  Ame's last regular week). [Observed S1]
- **Ina:** fellow artists; Mumei's drawing collabs with Ina (2023-01; "doodles with @NinomaeInanis,"
  2025-04-21). [Observed S1]
- **Calli:** "ANATOMY REVIEW with Calli + Sana + Mumei" (2022), a drawing bit Mumei brought back on her own
  in 2025. [Observed S1]
- **Nerissa:** Mumei's "EMO HOURS: IT WAS NEVER A PHASE with NERISSA" (2023) and "SAD GIRL HOURS" (2025-04-20);
  Nerissa's first reply to Fauna on X: "Fauna-senpai!!! My Raven companion is named Shadow~" (2023).
  [Observed S1; research/x-posts.md]
- **Outside the cast (context):** Hakos Baelz is Mumei's most frequent partner and Fauna's horror partner;
  Tsukumo Sana (graduated 2022) completed the Council. [Observed S1; Promise card]

## History
| Date | Event | Trace left |
|---|---|---|
| 2021-08-23 | Council debuts | Five concepts |
| 2021-08-25 | Fauna and Mumei's first co-op | "Adventuring with Mumei!" |
| 2023-03-19 | Mumei sings with Kiara on the 4th fes. stage | HOLOTORI |
| 2023-10-09 | -Promise- formed | — |
| 2024-12-27 | Fauna on Kiara's HOLOTALK | — |
| 2025-01-03 | Fauna graduates | — |
| 2025-04 | Mumei's farewell month: Kronii's "Donut Hole," IRyS's "final stream," HOLOTALK, Gura's room review | — |
| 2025-04-27 | Mumei graduates (04-28 JST) | — |

## Sensory Palette
- See: green and brown side by side; a kirin's branch horns next to owl feathers; a paper bag floating
  near a sleepy kirin.
- Hear: a whispered "return to nature"; a sudden owl screech; the gavel "don don!"

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| KronMei | Kronii and Mumei | fans |
| HOLOTORI | the bird unit (Kiara, Mumei, Subaru, Reine, Lui) | members |
| gumei | Gura and Mumei | Gura's title |
| return to nature | Fauna's invitation (and threat) | Fauna |

## Conflicts and Story Hooks
1. (Before 2025) Fauna tries to "return Mumei to nature" during a shooter match; Mumei screeches.
2. (Before 2025) A HOLOTORI game night where Mumei forgets she's a bird.
3. (2026) Kronii sings "Donut Hole" alone and remembers the duet.
4. (Before 2025) Fauna and Gura draw hololive members from memory and get every hairstyle wrong.

## Links to Characters
Ceres Fauna, Nanashi Mumei, Ouro Kronii, IRyS, Takanashi Kiara, Gawr Gura, Watson Amelia, Ninomae Ina'nis,
Mori Calliope, Nerissa Ravencroft.

## Secrets
(None.)

## Hard Facts (continuity)
- Fauna graduated 2025-01-03; Mumei 2025-04-27 (04-28 JST). After those dates they appear only as memories.
- Fauna's oshi: Gura. Kiara's name for Mumei: "Moomsies." HOLOTORI includes Kiara and Mumei.

## Sources (checked 2026-10-01)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-10-01). Fauna: dqtrM2o4BnU, QM2DjVNl1gY,
  0nB58ASPAhw, oRN_5TPDdhI, lHLx62THuYM, 5-9YHKhP2lY, NyIqYW0r_5w, bilsiV8t8io, -YdluR5bn1Y, sGeLlsQVcmA,
  XNiRgmK54Hg. Mumei: fMK4GmM4WT8, 7Ezl57s7sqA, d5n0ZtjwVsA, 50-HQZj5FVg, Nllze52PrPY, uPd_Tkj5zxI (Kiara),
  Qw_tfe1kFRc (Kiara), RMvdq3JQ2n0 (Kiara), k7dTnCl2pVA (Gura), ZP8E9WH71OU (Gura), zCHHsb9eMbk,
  1sMuXpAVILg, sdZSs87MXjo, wGaN8Wi-BNc, 60r1O06S4jo, EQ5CVr3bb5U, WSM66DoRFV0; Kronii UOYMqqk3quw,
  fMK4GmM4WT8. Mention counts computed by Claude.
- S2 Ceres Fauna wiki page (secondary); S3 Nanashi Mumei wiki page (secondary)
- S4 Mumei's X post on the 4th fes. (1637345257632169987), via wiki citation (research/x-posts.md)
- S5 Character files: Fauna (F#), Mumei (M#), Kronii (K8)

---

## [SW] Name
Fauna and Mumei Pairs

## [SW] Role
Relationship

## [SW] Other Names
Fauna and Mumei, Mumei and Fauna, KronMei, HOLOTORI, gumei, Fauna and Gura, Mumei and Kiara, Mumei and Kronii

## [SW] Description
Fauna and Mumei, Council's nature and civilization: from their first week Fauna was protective of Mumei to the point of possessiveness, inviting her to "return to nature" whenever she was upset, while Mumei's darker side left it unclear who needed protecting from whom; one of Fauna's last streams was the two of them reading Wikipedia talk-page fights (2024-12). With the cast: Mumei and Kronii (KronMei) were frequent partners, ending with a "Donut Hole" cover duet (2025-04); Fauna and Kronii defused bombs speaking only in ASMR (2021). IRyS was their Promise genmate; Mumei's last solo game stream was Overwatch with IRyS (2025-04-22). Mumei and Kiara are birds of HOLOTORI; Kiara calls her "Moomsies" and hosted both on HOLOTALK before they left. Gura was Fauna's oshi; they drew hololive members from memory four days before Fauna graduated, and Gura and Mumei did a "ROOM REVIEW" together in Mumei's last week. Mumei also drew with Ina, did "Anatomy Review" with Calli, played with Ame in Ame's last regular week, and held "emo hours" with Nerissa.

## [SW] Rules
Fauna graduated on 2025-01-03 and Mumei on 2025-04-27; after those dates they appear only as memories and callbacks. Fauna's possessiveness and "return to nature" are performed bits. All of these are friendships.

## [SW] Sensory Details
Green and brown side by side; a kirin's branch horns beside owl feathers; a paper bag drifting near a sleepy kirin; a whispered "return to nature"; a sudden owl screech; the gavel's "don don!"

## [SW] Secrets


---

## Open Questions
(None.)


==================== AUDIO REPORT: research/audio-check/fauna.md ====================

# Audio check — Ceres Fauna (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription drops some fillers and does not write giggles or "uuuu" reliably, and
small.en can turn Japanese speech into English words. The horror window includes game dialogue that she
reads aloud in character voices; only lines that are clearly her own are quoted.

All windows are from autumn 2024, her last active period before she graduated on 2025-01-03, which this
project weights highest. Stories told in these windows about her family, school, diet and driving are
outside the project's scope and are not used. A members-only window was transcribed by mistake and then
set aside unused (members content is not public).

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| worldtree30_2024 | [【MINECRAFT】 The world tree isn't gonna build its](https://youtu.be/14S18Ykq0_w) | [1:00:00–1:30:00](https://youtu.be/14S18Ykq0_w?t=3600) | 24.1 | 2879 | 119.6 | 293 Hz | 209–435 Hz |
| horror45_2024 | [【Mouthwashing】 The strange, unsettling horror ga](https://youtu.be/9_Ue4fOMNP8) | [1:00:00–1:45:00](https://youtu.be/9_Ue4fOMNP8?t=3600) | 37.5 | 3453 | 92.2 | 306 Hz | 234–430 Hz |
| supers30_2024 | [chatting and super catchup!](https://youtu.be/TzW6VRf4KjQ) | [0:30:00–1:00:00](https://youtu.be/TzW6VRf4KjQ?t=1800) | 23.8 | 2504 | 105.1 | 289 Hz | 124–432 Hz |
| chat40_2024 | [the first solo fauna stream in 8,000 years](https://youtu.be/iIBywcAIMD0) | [0:40:00–1:20:00](https://youtu.be/iIBywcAIMD0?t=2400) | 28.2 | 3364 | 119.2 | 283 Hz | 126–439 Hz |
| close2024 | [the first solo fauna stream in 8,000 years](https://youtu.be/iIBywcAIMD0) | [3:16:55–3:28:55](https://youtu.be/iIBywcAIMD0?t=11815) | 8.5 | 1318 | 154.3 | 280 Hz | 126–444 Hz |
| open2024 | [the first solo fauna stream in 8,000 years](https://youtu.be/iIBywcAIMD0) | [0:00:00–0:15:00](https://youtu.be/iIBywcAIMD0?t=0) | 13.1 | 1420 | 108.1 | 300 Hz | 225–447 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments (silence between segments
excluded). About 2.9 hours in all. In the chat, superchat and closing windows p10 drops near 125 Hz
(noise and game or music frames); the cleaner windows run about 210–445 Hz.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Official greeting "Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (F1) | **Not detected in this window.** The stream opens mid-setup with soft hellos while she fixes her background music. | [0:00:00](https://youtu.be/iIBywcAIMD0?t=0) |
| Soft-spoken (F1, F2) | **Confirmed in her own words.** "I'm pretty soft-spoken. And talking in my head voice like this does not strain my voice at all." | [1:14:21](https://youtu.be/iIBywcAIMD0?t=4461) |
| Pitch | **Measured: high in this project's samples.** Median 280–306 Hz across six windows, near Kiara's (245–300 Hz) and above IRyS's (214–226 Hz). Sample results, not a ranking. | table above |
| Unhurried pace | **Confirmed.** 105–120 words per minute of speech in chat and building, 92 in the horror game; the exception is the closing superchat list (154). | table above |
| Fillers "like," "I don't know," "I guess" | **Confirmed.** "I don't know" 60 times in 14,938 words (17 in the 40-minute chat window); "like" 288 (about 1 in 40 in chat, 1 in 30 while building); "I guess" 27; "kind of" 18. | throughout |
| Rarely swears | **Confirmed.** Her own words: "dang," "what the heck," "oh my gosh." The "damn it" and the one strong swear in the horror window are game lines she reads aloud. | [1:26:25](https://youtu.be/9_Ue4fOMNP8?t=5185); [1:42:31](https://youtu.be/9_Ue4fOMNP8?t=6151) |
| Scared reactions murmured, not shouted | **Confirmed.** "oh no" 8 times and "oh gosh" 5 in 45 minutes of Mouthwashing, at the same median pitch as chat. | throughout the horror window |
| Reads game dialogue aloud in character voices | **Confirmed (new).** The horror window is full of the game's lines read in voices, between her own reactions. | [1:00:00–1:45:00](https://youtu.be/9_Ue4fOMNP8?t=3600) |
| "Fauna Standard Time," lateness bit | **Confirmed.** "…we will be back to Fauna Standard Time. I promise." and, celebrating a milestone late, "I'm always on time." | [3:27:56](https://youtu.be/iIBywcAIMD0?t=12476); [0:46:20](https://youtu.be/iIBywcAIMD0?t=2780) |
| Spells and Fauna Mart during superchats | **Confirmed.** "If you heard your name, you will now be the recipient of my next spell"; "It's not a scam! Fauna Mart is real!" | [0:45:36](https://youtu.be/TzW6VRf4KjQ?t=2736); [0:49:09](https://youtu.be/TzW6VRf4KjQ?t=2949) |
| Superchats as rapid lists of names | **Confirmed.** 62 "thank you"s in the 12-minute closing window; a sung "Happy Birthday" for a Sapling's birthday; a "Plant them, plant them…" chant after a list. | [3:21:39](https://youtu.be/iIBywcAIMD0?t=12099); [0:45:26](https://youtu.be/TzW6VRf4KjQ?t=2726) |
| Japanese in superchats | **Detected.** "Arigatou gozaimasu. Thank you." (second model); "arigato" (first model). | [0:49:09](https://youtu.be/TzW6VRf4KjQ?t=2949) |
| "Return to nature," "uuuu," "Evil Fauna" (F2) | **Not detected in these windows.** Kept from the wiki (secondary). | — |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- When something called her a "gaming idol giraffe": "I was like, oh, am I supposed to be a giraffe? … I
  was ready to be a kirin because that's what I am. But if they need me to be a giraffe, I guess I can do
  that" [0:55:48](https://youtu.be/iIBywcAIMD0?t=3348)
- Grand deadpan: "I will be the sole arbitrator of YouTube monetization." [0:42:06](https://youtu.be/iIBywcAIMD0?t=2526)
- Refusing a Sapling's request: "So how can you guys get a jet pack if I don't even have one? I am not the
  keeper of jet packs." [3:24:38](https://youtu.be/iIBywcAIMD0?t=12278)
- On a murder-mystery collab: "I just wanted to use the gun… it would be dramatic and funny."
  [3:20:24](https://youtu.be/iIBywcAIMD0?t=12024)
- Choosing a role in a game: "Me. I'll be the mean manager." [0:55:28](https://youtu.be/TzW6VRf4KjQ?t=3328)
- A flat, fake laugh at her own pun ("Ha ha, I'm so…"; the pun word differs between models).
  [1:12:53](https://youtu.be/iIBywcAIMD0?t=4373)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Plant them, plant them, got them, plant them all, sapling wrap." | [0:45:26](https://youtu.be/TzW6VRf4KjQ?t=2726) | "S, Tash, fool. Plant them, plant them, got them, plant them all, got them, plant them all," | Agrees (a chant; only "Plant them, plant them…" is quoted) |
| "If you heard your name, you will now be the recipient of my next spell, which will make you want to spend money at Fauna Mart" | [0:45:36](https://youtu.be/TzW6VRf4KjQ?t=2736) | "Am I hexing you? Yes. If you heard your name, you will now be the recipient of my next spell. Which will make you want to spend money at Fauna Martins. Which" | **Partly agrees**: the first sentence agrees; the shop name differs ("Fauna Mart" vs "Fauna Martins"), so the rest is paraphrased |
| "It's not a scam! Fauna Mart is real. It's not a scam!" | [0:49:09](https://youtu.be/TzW6VRf4KjQ?t=2949) | "It's not a scam! Fauna Mart is real! Is that what you're going for? Because" | Agrees |
| "Me. I'll be the mean manager" | [0:55:28](https://youtu.be/TzW6VRf4KjQ?t=3328) | "mean manager, though? Me. I'll be the mean manager. But the answer" | Agrees |
| "Send it directly into my brain. I will be the sole arbitrator of YouTube monetization." | [0:42:06](https://youtu.be/iIBywcAIMD0?t=2526) | "the YouTube oxcord send it directly into my brain and I will be the sole arbitrator of YouTube monetization three seconds" | Agrees on the shared spans ("send it directly into my brain" / "I will be the sole arbitrator of YouTube monetization"); only the second is quoted |
| "It's okay. We can celebrate 900,000. I'm always on time." | [0:46:20](https://youtu.be/iIBywcAIMD0?t=2780) | "of the doubt that I was right on time. It's okay. We can celebrate. Nine hundred thousand." | **Partly agrees**: the number differs ("900,000" vs "Nine hundred thousand. Nine hundred and four thousand"); quoted as "It's okay. We can celebrate… I'm always on time." |
| "I was like, oh, am I supposed to be a giraffe?" | [0:55:48](https://youtu.be/iIBywcAIMD0?t=3348) | "said giraffe. And I was like, oh, am I supposed to be a giraffe? And I was" | Agrees |
| "I was ready to be a Kirin because that's what I am. But if they need me to be a giraffe, I guess I can do that" | [0:56:02](https://youtu.be/iIBywcAIMD0?t=3362) | "gonna be like i was i was ready to be a kieran because that's what i am but if they need me to be a giraffe i guess i can do that gaming" | Agrees (the second model spells kirin "kieran"; its full text continues "…but if they need me to be a giraffe i guess i can do that") |
| "Ha ha, I'm so humerus, ha ha ha ha ha." | [1:12:53](https://youtu.be/iIBywcAIMD0?t=4373) | "go. Just kidding. Ha ha, I'm so humorous, ha ha ha ha ha ha. Okay, let" | **Partly agrees**: the pun word differs ("humerus" vs "humorous"); described, not quoted |
| "And I think I'm lucky that, well, I'm pretty soft spoken. And talking in my head voice like this does not strain my voice at all." | [1:14:21](https://youtu.be/iIBywcAIMD0?t=4461) | "i don't know and i think i'm lucky that well i'm pretty soft-spoken and talking in my head voice like this does not strain my voice at all i can pretty much" | Agrees |
| "Also. I just wanted to use the gun cuz it would be dramatic and funny" | [3:20:24](https://youtu.be/iIBywcAIMD0?t=12024) | "had no choice. Also, I just wanted to use the gun because it would be dramatic and funny. Even if I" | **Partly agrees**: "cuz"/"because" differ; quoted as "I just wanted to use the gun… it would be dramatic and funny" |
| "So how can you guys get a jet pack if I don't even have one? I am not the keeper of jet packs." | [3:24:38](https://youtu.be/iIBywcAIMD0?t=12278) | "stealing their answer? I don't have a jetpack So, how can you guys get a jetpack if I don't even have one I am NOT the keeper of jetpacks" | Agrees (the second model writes "jetpack(s)" and stresses "NOT") |
| "We'll see you tomorrow for the race, and then eventually we will be back to Fauna Standard Time. I promise. Thank you so much for hanging out, and I will see you tomorrow." | [3:27:56](https://youtu.be/iIBywcAIMD0?t=12476) | "hanging out today i will see you tomorrow for the race and then eventually we will be back to fauna standard time i promise thank you so much for hanging out an…" | Agrees on "…we will be back to Fauna Standard Time. I promise. Thank you so much for hanging out, and I will see you tomorrow." |
| "Wish me luck. Bye!" | [3:28:14](https://youtu.be/iIBywcAIMD0?t=12494) | "will see you tomorrow. Wish me luck. I'm gonna practice" | **Partly agrees**: "Wish me luck." agrees; "Bye!" is not in the second model (it continues "I'm gonna practice…"), so only "Wish me luck." is quoted |



==================== AUDIO REPORT: research/audio-check/mumei.md ====================

# Audio check — Nanashi Mumei (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription drops some fillers and does not write screeches or hoots reliably, and
small.en can turn Japanese speech into English words, so Japanese phrases below are indicative only. Game
windows include game voices and teammates; only lines that are clearly hers are quoted.

All windows are from March–April 2025, her last active period before she graduated on 2025-04-27 (04-28
JST), which this project weights highest. Stories in the Q&A about her family, school and illnesses are
outside the project's scope and are not used. A planned window from an earlier chatting
stream (fLxgC-r6w1E) could not be fetched from the archive; the Q&A's opening and closing were used
instead.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| draw30_2025 | [【MUMEI DRAWS】*Doodles In Complete Silence*](https://youtu.be/47wq1FMoEG0) | [0:30:00–1:00:00](https://youtu.be/47wq1FMoEG0?t=1800) | 0.0 | 0 | None | – Hz | ––– Hz |
| doom45_2025 | [【DOOM Eternal】The Grand Rip and Tear Finale !! #](https://youtu.be/5xL_7PGd3rk) | [2:00:00–2:45:00](https://youtu.be/5xL_7PGd3rk?t=7200) | 25.3 | 1245 | 49.3 | 302 Hz | 213–480 Hz |
| close2025 | [【OH HI】Moom Q&A !! ~](https://youtu.be/7vxLfdBqFac) | [1:22:19–1:34:19](https://youtu.be/7vxLfdBqFac?t=4939) | 6.4 | 1083 | 168.1 | 284 Hz | 214–422 Hz |
| open2025 | [【OH HI】Moom Q&A !! ~](https://youtu.be/7vxLfdBqFac) | [0:00:00–0:10:00](https://youtu.be/7vxLfdBqFac?t=0) | 8.7 | 777 | 89.0 | 293 Hz | 205–412 Hz |
| qa30_2025 | [【OH HI】Moom Q&A !! ~](https://youtu.be/7vxLfdBqFac) | [0:10:00–0:40:00](https://youtu.be/7vxLfdBqFac?t=600) | 23.5 | 3668 | 155.9 | 287 Hz | 208–422 Hz |
| ow30_2025 | [【OVERWATCH 2】im doing this for the fans !! not m](https://youtu.be/zfQJZ6LetCc) | [0:30:00–1:00:00](https://youtu.be/zfQJZ6LetCc?t=1800) | 12.5 | 1047 | 84.0 | 311 Hz | 197–473 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments (silence between segments
excluded). About 2.1 hours of speech windows; the drawing window is silent by design (the stream's title is
"Doodles In Complete Silence") and gives no data. The opening window includes several minutes of her
fixing the background music. The Overwatch window mixes in teammates and game audio.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Official greeting "Oh hi! Hoo's this? Nanashi Mumei!" (M1) | **Partly detected.** Caught off guard by her music, she opens with "Oh, hi" and "…hi everybody. What's up? How are you?" (both models). The full official line was not detected. | [0:03:20](https://youtu.be/7vxLfdBqFac?t=200) |
| "Cutest voice," soft (M2) | **Not measurable here.** Median pitch 284–311 Hz, high in this project's samples and close to Fauna's (280–306 Hz). Sample results, not a ranking. | table above |
| Low energy, scattered, short attention span (M2) | **Confirmed.** She loses her train of thought and says so, tells herself to stay on topic, and cuts tangents with "anyways" (11 in 30 minutes) and "sorry" (11). | [0:10:00–0:40:00](https://youtu.be/7vxLfdBqFac?t=600) |
| Fast when chatting | **Confirmed.** 156–168 words per minute of speech in the Q&A and closing; 49 in DOOM and 84 in Overwatch. | table above |
| Fillers | **Confirmed.** "okay" 25 in the Q&A and 31 in the 12-minute closing; "I don't know" 19, "you know" 15, "I guess" 11, "like" 54 in 3,668 words. | throughout |
| Mild language | **Confirmed.** "shoot," "heck," "oh dear," "oh my gosh," "oh my goodness"; no strong swearing in about 2.1 hours. | throughout |
| "don don!" gavel (M2) | **Detected (first model).** "Don don!" six times in the Overwatch window; in the Q&A closing she promises a big one at the end of every stream (the transcripts mishear it as "don't on"). | [0:56:50](https://youtu.be/zfQJZ6LetCc?t=3410); [1:22:19](https://youtu.be/7vxLfdBqFac?t=4939) |
| Guardian-of-civilization authority | **Confirmed.** Ranking chip flavors: "…guardian of civilization! … I decide everything for humanity." | [0:19:41](https://youtu.be/7vxLfdBqFac?t=1181) |
| "Yippee," "hooray" | **Confirmed.** Five of each in the first ten minutes: "I love talking about myself. Yippee, yippee. Hooray." | [0:05:43](https://youtu.be/7vxLfdBqFac?t=343) |
| Short bright game reactions | **Confirmed.** DOOM: "uh oh" 7, "oh shoot" 2, "oh dear" 2; Overwatch: "nice" 21, "yay" 9, "oh no" 5, "Owie! Owie! Owie!" | [0:52:46](https://youtu.be/zfQJZ6LetCc?t=3166) |
| Japanese in games | **Detected.** "Saikou! Saikou desu!" (first model, seven "saikou"); "yowai" for herself (both models hear it, spelled differently); "arigato." | [0:31:25](https://youtu.be/zfQJZ6LetCc?t=1885); [0:40:29](https://youtu.be/zfQJZ6LetCc?t=2429) |
| Long, repeated goodbyes | **Confirmed.** "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." then about a dozen "bye-bye"s. | [1:31:02](https://youtu.be/7vxLfdBqFac?t=5462) |
| High screeches when startled (M2) | **Not detected reliably** (transcription does not write screeches). Kept from the wiki (secondary). | — |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Before reading her genmates' questions: "Okay, are we ready? Are we bracing ourselves? We got our tissue
  box nearby." [0:11:33](https://youtu.be/7vxLfdBqFac?t=693)
- "…but what do I know? Everything." [0:31:35](https://youtu.be/7vxLfdBqFac?t=1895)
- "I've never been scared of anything ever." [0:26:39](https://youtu.be/7vxLfdBqFac?t=1599)
- "Good job homo sapien." [0:26:17](https://youtu.be/7vxLfdBqFac?t=1577)
- Arm-wrestling ranking: "I think I would win against Gura, Kiara, IRyS, Nerissa, and Mococo"; Biboo moves
  to the losing side ("She is a rock"); "But I have other skills and things that make me special, so
  whatever." [0:23:52](https://youtu.be/7vxLfdBqFac?t=1432); [0:27:23](https://youtu.be/7vxLfdBqFac?t=1643); [0:27:44](https://youtu.be/7vxLfdBqFac?t=1664)
- "Sometimes you go through life just not knowing stuff. You can't know everything." … "It's okay not to
  know stuff sometimes. Yeah, unless you're me. Exactly, unless you're me." [1:24:20](https://youtu.be/7vxLfdBqFac?t=5060)
- DOOM upgrades: "I'm too poor. No money." [2:07:07](https://youtu.be/5xL_7PGd3rk?t=7627)
- Overwatch: "Oh dear, that was pointless." [0:52:11](https://youtu.be/zfQJZ6LetCc?t=3131)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "I'm too poor. No money." | [2:07:07](https://youtu.be/5xL_7PGd3rk?t=7627) | "upgrades I can't I'm too poor No money Huh? Purchase the" | Agrees |
| "He's in the blender. He's in the blender. He's in the blender. He was in the blender." | [2:33:19](https://youtu.be/5xL_7PGd3rk?t=9199) | "He's in the blunder, he's in the blunder, he was in the blunder. Wait, I have to press it." | **Disagrees**: "blender" vs "blunder"; not quoted (described as a line repeated four times) |
| "Gimme gimme gimme gimme I don't care I don't care anymore." | [2:43:32](https://youtu.be/5xL_7PGd3rk?t=9812) | "Give me, give me, I don't care, I don't care anymore. Fine. Ah-hoo! Okay." | **Partly agrees**: "Gimme gimme…" vs "Give me, give me"; only "I don't care, I don't care anymore." is quoted |
| "Hi, everybody! What's up? How are you?" | [0:03:20](https://youtu.be/7vxLfdBqFac?t=200) | "to hear. Oh, hi everybody. What's up? How are you? Oh, dear. Oh," | Agrees on "…hi everybody. What's up? How are you?"; the second model also hears "Oh, hi." |
| "Oh dear. I guess I already started it, so I'm in the middle of it now." | [0:05:02](https://youtu.be/7vxLfdBqFac?t=302) | "Oh, dear. It's... I guess... I guess I already started it, so I'm in the middle of it now. Okay, I'm good." | Agrees (the second model repeats "I guess") |
| "Yippee, I love talking about myself. Yippee, yippee, hooray." | [0:05:43](https://youtu.be/7vxLfdBqFac?t=343) | "answer questions today yippee yippee. I love talking about myself yippee yippee. Hooray Um Yeah," | Agrees ("I love talking about myself… yippee yippee… hooray"; punctuation differs) |
| "Okay, are we ready? Are we bracing ourselves? We got our tissue box nearby." | [0:11:33](https://youtu.be/7vxLfdBqFac?t=693) | "enough um sorry okay are we ready are we bracing ourselves we got our tissue tissue box nearby okay and" | Agrees |
| "No, what am I, opinion, what am I, I'm a guardian of civilization! Uh, objectively, I decide everything for humanity, objectively." | [0:19:41](https://youtu.be/7vxLfdBqFac?t=1181) | "better, in my opinion. No, what am I, opinion? What am I, I'm guardian of civilization! Uh, objectively, I decide everything for humanity. Objectively, I think,…" | **Partly agrees**: "I'm a guardian" vs "I'm guardian"; quoted from "…guardian of civilization!" and "…I decide everything for humanity." |
| "Okay, I think I would win against Gura, Kiara, Iris, Narissa, and Mokoko." | [0:23:52](https://youtu.be/7vxLfdBqFac?t=1432) | "have no clue about. Okay, I think I would win against Gura, Kiarra, Iris, Narissa, and Mococo. I think" | Agrees (names spelled differently: Kiara/Kiarra, IRyS/Iris, Nerissa/Narissa, Mococo/Mokoko) |
| "Good job homo sapien." | [0:26:17](https://youtu.be/7vxLfdBqFac?t=1577) | "the human advantage good job homo sapien you guys ever" | Agrees |
| "I've never been scared of anything ever. I've never had a run from anything. Usually things run for me, so." | [0:26:39](https://youtu.be/7vxLfdBqFac?t=1599) | "true. I wonder. I've never been scared of anything ever. I've never had a run from anything. Usually things run from me, so... Oh yeah, in" | **Partly agrees**: "I've never been scared of anything ever" agrees; "things run for me" vs "run from me" differ, so only the first sentence is quoted |
| "I think I can move Beeboo into who I would lose against okay she is a rock" | [0:27:23](https://youtu.be/7vxLfdBqFac?t=1643) | "I would probably, I think I can move Beeboo into who I would lose against. Okay. She is a rock, this is true." | Agrees ("…I can move Beeboo [Biboo] into who I would lose against. Okay. She is a rock") |
| "unfortunately it looks like most of EN could beat me but um I have other skills and things that make me special so whatever" | [0:27:44](https://youtu.be/7vxLfdBqFac?t=1664) | "I don't know. Okay. Unfortunately it looks like most of Iain could beat me. But I have other skills and things that make me special, so whatever. Next question.…" | **Partly agrees**: "most of EN" vs "most of Iain"; "But I have other skills and things that make me special, so whatever" agrees and is quoted; the rest is paraphrased |
| "I think my answer's the best, but what do I know? everything" | [0:31:35](https://youtu.be/7vxLfdBqFac?t=1895) | "All right, I think I think my answer is the best, but what do I know? Everything." | **Partly agrees**: "answer's" vs "answer is"; quoted as "…but what do I know? Everything." |
| "Sometimes you go through life just not knowing stuff. You can't know everything." | [1:24:20](https://youtu.be/7vxLfdBqFac?t=5060) | "you. That's okay. Sometimes you go through life just not knowing stuff. You can't know everything, and sometimes you" | Agrees |
| "It's okay not to know stuff sometimes. Yeah, unless you're me. Exactly, unless you're me." | [1:24:35](https://youtu.be/7vxLfdBqFac?t=5075) | "how it is it's okay not to know stuff sometimes yeah unless you're me exactly unless you're me let me now" | Agrees |
| "Goodbye for now. I'll see you probably tomorrow, probably tomorrow. Okay, okay, bye-bye, bye-bye for now." | [1:31:02](https://youtu.be/7vxLfdBqFac?t=5462) | "send you over now. Okay, okay, okay, okay. Goodbye for now. I'll see you probably tomorrow. Probably tomorrow. Okay. Bye bye. Bye bye for" | **Partly agrees**: "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." and "bye-bye for now" agree; the "okay, okay" before it differs |
| "Yowai. I am Yowai right now. I have the least damage in the game." | [0:40:29](https://youtu.be/zfQJZ6LetCc?t=2429) | "Uh oh. Yoai! Ahh. I am Yoai right now. I have the least damage in the game. Nooo! Oh no." | **Partly agrees**: the Japanese word is spelled "Yowai"/"Yoai" (the same word heard); "I have the least damage in the game." agrees |
| "Oh dear, that was pointless" | [0:52:11](https://youtu.be/zfQJZ6LetCc?t=3131) | "her! Grab her! Oh dear, that was pointless. Mira, behind! Oh" | Agrees |
| "Owie! Owie! Owie!" | [0:52:46](https://youtu.be/zfQJZ6LetCc?t=3166) | "to say annoying. Owie owie owie owie!" | Agrees |
| "I died happy!" | [0:58:18](https://youtu.be/zfQJZ6LetCc?t=3498) | "Ah, Riga! D'oh... I miss you! Kill" | **Not confirmed**: not in the second model's text; removed |



==================== CAST AND WORLD EDITS (diff of final.md files; + added, - removed) ====================

+++ b/novel-lab/projects/holoen/runs/20260930-0704-character-Mori-Calliope/final.md
-Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!" Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her chaotic CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin: frequent collaborator; Calli came to like how her own name sounds once Gigi started saying it. Kobo Kanaeru: calls her "Uncle Dad." Koseki Bijou ("Biboo"): a junior whose skill Calli openly admires. Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together. Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star"). Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka). Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth: her "LYRA" remix cover of "III."
+Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!" Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her chaotic CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin: frequent collaborator; Calli came to like how her own name sounds once Gigi started saying it. Kobo Kanaeru: calls her "Uncle Dad." Koseki Bijou ("Biboo"): a junior whose skill Calli openly admires. Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together. Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star"). Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka). Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth: her "LYRA" remix cover of "III." Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022).
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20260930-0704-character-Ouro-Kronii/final.md
-Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'Clock); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated): Council genmate (KronMei). Ceres Fauna (graduated): Council genmate who described Kronii's "gap moe." Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel. Gigi Murin: collaborator in the units "TimeChaser" and "Clockwork Orange." Cecilia Immergreen: calls her "Owo-senpai"; Kronii calls her a "CLANKER." Raora Panthera: "Pizza Time" partner who calls her "Tam Tender." Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live.
+Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'Clock); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated 2025): Council genmate and frequent partner (KronMei), from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet in Mumei's last month (2025). Ceres Fauna (graduated 2025): Council genmate who described Kronii's "gap moe"; they once defused bombs speaking only in ASMR. Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel. Gigi Murin: collaborator in the units "TimeChaser" and "Clockwork Orange." Cecilia Immergreen: calls her "Owo-senpai"; Kronii calls her a "CLANKER." Raora Panthera: "Pizza Time" partner who calls her "Tam Tender." Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live.
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Gawr-Gura/final.md
-Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George."
+Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George." Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated. Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week.
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Ninomae-Inanis/final.md
-Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'Clock); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, Ina credits Kiara's support with helping her gain confidence in dancing, and Kiara groans at her puns. Mori Calliope: a recurring target of her puns ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy whose collab outfit Ina designed. IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island. Houshou Marine: a senior artist she admires.
+Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'Clock); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, Ina credits Kiara's support with helping her gain confidence in dancing, and Kiara groans at her puns. Mori Calliope: a recurring target of her puns ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy whose collab outfit Ina designed. IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island. Houshou Marine: a senior artist she admires. Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025).
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Takanashi-Kiara/final.md
-Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert; they share the "6 7" meme. Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI). Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera: cast the infamous "Doom." Cecilia Immergreen: German-speaking partner. Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior.
+Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert; they share the "6 7" meme. Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI). Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera: cast the infamous "Doom." Cecilia Immergreen: German-speaking partner. Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior. Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and she was HOLOTALK's 33rd guest. Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left.
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Watson-Amelia/final.md
-Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs.
+Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs. Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week.
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20260930-2309-world-VTuber-Persona-and-Lore/final.md
-All six cast members. Each character card's Background and Personality open with the persona frame
+All ten cast members. Each character card's Background and Personality open with the persona frame
-The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.
+The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
+++ b/novel-lab/projects/holoen/runs/20260930-2309-world-hololive--Promise/final.md
-Ouro Kronii and IRyS (members). Myth characters and Nerissa appear as cross-group friends.
+Ouro Kronii and IRyS (members); Ceres Fauna and Nanashi Mumei (graduated 2025; see "Fauna and Mumei Pairs"). Myth characters and Nerissa appear as cross-group friends.
-The group of Ouro Kronii and IRyS, hololive -Promise-: IRyS, Ouro Kronii and Hakos Baelz at the 2026 baseline. It grew from the English -Council- generation (August 2021), whose personas were themed around concepts (Kronii is Time); Sana graduated from Council in 2022, before Promise existed. IRyS ("Hope") and the four remaining Council members were billed together as "CouncilRyS" and formed Promise on 2023-10-08 PDT / 10-09 JST; Fauna and Mumei graduated in 2025. Bae calls Kronii "too talented, savage, and a tsundere granny"; Fauna once described Kronii's "gap moe," the cute side that shows when she's flustered; IRyS has wondered aloud how Kronii sounds when she's scared. IRyS and Bae keep the "BaeRyS" bit of being "married" and "divorced," which turned "Monopoly" into a fandom euphemism, and they are also creative partners: paired for the 2026 Serendipity concert, IRyS leans on Bae's "strong vision" when she's indecisive, Bae admires IRyS's humor that makes everyone comfortable, and they call their dynamic "a can of worms" and "Complicated."
+The group of Ouro Kronii and IRyS, hololive -Promise-: IRyS, Ouro Kronii and Hakos Baelz at the 2026 baseline. It grew from the English -Council- generation (August 2021), whose personas were themed around concepts (Kronii is Time); Sana graduated from Council in 2022, before Promise existed. IRyS ("Hope") and the four remaining Council members were billed together as "CouncilRyS" and formed Promise on 2023-10-08 PDT / 10-09 JST; Fauna (Nature, the soft kirin protective of Mumei) and Mumei (Civilization, the forgetful owl and Bae's most frequent partner) graduated in 2025. Bae calls Kronii "too talented, savage, and a tsundere granny"; Fauna once described Kronii's "gap moe," the cute side that shows when she's flustered; IRyS has wondered aloud how Kronii sounds when she's scared. IRyS and Bae keep the "BaeRyS" bit of being "married" and "divorced," which turned "Monopoly" into a fandom euphemism, and they are also creative partners: paired for the 2026 Serendipity concert, IRyS leans on Bae's "strong vision" when she's indecisive, Bae admires IRyS's humor that makes everyone comfortable, and they call their dynamic "a can of worms" and "Complicated."
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
+++ b/novel-lab/projects/holoen/runs/20260930-2309-world-hololive/final.md
-All eight. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
-Kronii and IRyS are active in hololive -Promise-; Nerissa in hololive -Advent-. Detailed history: the
+All ten. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
+Kronii and IRyS are active in hololive -Promise-, where Fauna and Mumei are alumnae; Nerissa in hololive -Advent-. Detailed history: the
-The VTuber agency run by COVER Corporation that the cast belongs to. Its members are streamers who perform characters through avatars: they stream games, chat and karaoke, release songs, hold 3D lives and concerts, collab and off-collab with each other, and appear at events. Since 2026-09-07 the former female-talent branches are one "hololive" (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-. Watson Amelia concluded her regular activities on 2024-09-30 and remains an affiliate who appears at events; Gawr Gura graduated on 2025-05-01 and is an alumna. Senpai and kouhai mean who debuted earlier or later, not language or nationality; formality varies by relationship; genmates are the people you debuted with. The calendar runs on debut anniversaries, birthdays, concerts and fes.
+The VTuber agency run by COVER Corporation that the cast belongs to. Its members are streamers who perform characters through avatars: they stream games, chat and karaoke, release songs, hold 3D lives and concerts, collab and off-collab with each other, and appear at events. Since 2026-09-07 the former female-talent branches are one "hololive" (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-. Watson Amelia concluded her regular activities on 2024-09-30 and remains an affiliate who appears at events; Gawr Gura graduated on 2025-05-01 and is an alumna, as are Promise's Ceres Fauna (2025-01-03) and Nanashi Mumei (2025-04-27). Senpai and kouhai mean who debuted earlier or later, not language or nationality; formality varies by relationship; genmates are the people you debuted with. The calendar runs on debut anniversaries, birthdays, concerts and fes.
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
+++ b/novel-lab/projects/holoen/runs/20260930-2334-character-IRyS/final.md
-Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her frequent horror co-op partner in 2025–2026. Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna and Nanashi Mumei (graduated): Promise unitmates from the early years.
+Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her frequent horror co-op partner in 2025–2026. Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna (graduated 2025): Promise unitmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Nanashi Mumei (graduated 2025): Promise unitmate; Mumei's last solo game stream was Overwatch with IRyS.
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20260930-2334-character-Nerissa-Ravencroft/final.md
-Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit (ShioRaven); Shiori plays hard to get, and the two keep a joke lore of fictional "children." Fuwawa and Mococo Abyssgard (FUWAMOCO): she claims, as a bit, to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower. IRyS: fellow singer who guested at that concert. Elizabeth Rose Bloodflame: her "mortal enemy (lore)" from Justice and her 2026 Serendipity duet partner; they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai"). Moona Hoshinova: she sings on Moona's "100%" (2025). Houshou Marine: her other oshi. Gigi Murin: duo partner with a joke "child," Nerigi.
+Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit (ShioRaven); Shiori plays hard to get, and the two keep a joke lore of fictional "children." Fuwawa and Mococo Abyssgard (FUWAMOCO): she claims, as a bit, to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower. IRyS: fellow singer who guested at that concert. Elizabeth Rose Bloodflame: her "mortal enemy (lore)" from Justice and her 2026 Serendipity duet partner; they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai"). Moona Hoshinova: she sings on Moona's "100%" (2025). Houshou Marine: her other oshi. Gigi Murin: duo partner with a joke "child," Nerigi. Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025). Ceres Fauna (graduated 2025): the senpai she excitedly replied to in her first week on X ("Fauna-senpai!!!").
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** Relationships gained Fauna/Mumei lines from
+  the world card "Fauna and Mumei Pairs" (archive titles there).
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-Concerts-and-Live-Events/final.md
-All eight.
+All ten (Fauna and Mumei: the 2023 EN concert, 4th fes., Mumei's 2024 3D birthday live "Outside the Box" and 6th fes.).
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-Cross-Branch-Friends/final.md
+- **Ceres Fauna** (graduated): her first official collab outside her generation was with Pavolia Reine
+  (Clubhouse 51, 2021); Kaela Kovalskia was a recurring partner ("Fearless & Fearful vs Ghosts," an ID
+  Minecraft server tour); she admired Shirogane Noel. [Observed S1; Fauna file F2]
+- **Nanashi Mumei** (graduated): HOLOTORI with Kiara, Subaru, Reine and Lui ("Bird Sisters" Q&A with Lui,
+  2025); drawing collabs with Airani Iofi; Minecraft "Peace & Love with HAACHAMA" (2025); Tokoyami Towa calls
+  her "Mumi-chan." [Observed S1; Mumei file M2]
-All eight.
+All ten.
-The cast's ties beyond EN, including JP, ID, DEV_IS and HOLOSTARS. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones" ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI"). Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora. IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan."
+The cast's ties beyond EN, including JP, ID, DEV_IS and HOLOSTARS. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones" ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI"). Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora. IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan." Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (Lui calls them bird sisters).
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-hololive-History-2023-2026/final.md
-All eight. Nerissa (Advent, 2023); IRyS and Kronii (Promise, 2023); Ame (affiliate, 2024); Gura
+All ten. Nerissa (Advent, 2023); Fauna and Mumei (graduated 2025); IRyS and Kronii (Promise, 2023); Ame (affiliate, 2024); Gura
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-hololive-History-to-2022/final.md
-All eight: Myth (2020), IRyS (2021-07), Kronii (2021-08); Nerissa arrives later (see the 2023–2026 card).
+All ten: Myth (2020), IRyS (2021-07), Kronii, Fauna and Mumei (Council, 2021-08); Nerissa arrives later (see the 2023–2026 card).
-The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes. "Link Your Wish" in Makuhari (03-20; Kiara: "MAKUHARI WAS ON FIRE!"), HOLOSTARS adds the unit UPROAR!! and the English group -TEMPUS-, holoMeet starts with Gura as ambassador, Calli holds her first solo concert (07-21), and Sana graduates (07-31).
+The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes. "Link Your Wish" in Makuhari (03-20; Kiara: "MAKUHARI WAS ON FIRE!"), HOLOSTARS adds the unit UPROAR!! and the English group -TEMPUS-, holoMeet starts with Gura as ambassador, Calli holds her first solo concert (07-21), and Sana graduates (07-31).
+- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
# One-round claim-check review (xhigh): hololive -Justice-, Elizabeth Rose Bloodflame and Gigi Murin (two character files) with their audio reports

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



==================== FILE: 20261001-1032-character-Elizabeth-Rose-Bloodflame/claude-draft.md ====================

---
kind: character
name: "Elizabeth Rose Bloodflame"
sw_section: Characters
---

# Character File: Elizabeth Rose Bloodflame

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Elizabeth is active at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. Nothing about the performer behind the avatar: private-life information (health, family, breaks and
> their reasons, nationality and the like) is outside scope and is not recorded here; by the author's rule
> (2026-10-01) an announced break is not written. Her British accent and slang are recorded as voice features
> and as her lore (Great Exardia). In stories she knows she is a streamer with a persona (see the world card
> "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; EB20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (EB#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1.9 hours of archived recordings (EB20: two 2026
> Tomodachi Life streams, opening, middle and close; a 2026 Monster Hunter Stories 3 trial stream; and 30
> minutes of her 2025 3D-showcase after-party chat; see research/audio-check/elizabeth.md). The game
> windows mix in voiced and text-to-speech characters she often voices along with, so the after-party chat
> is the clean sample of her own speech. The audio was machine-transcribed and acoustically measured;
> transcripts were reviewed in context, without independent listening verification.

## One-line Concept
"The Scarlet Queen," Harbinger of Order and organizer of Justice, a sword-wielding knight from Great Exardia
with a blue flame on her chest and a beautiful singing voice: a polite, warm, quietly confident host with a
British accent and a theatrical "Oh~hohoho!", who is hard on herself, soft on everyone else, and a gifted
mimic who trolls her seniors with voices. [Official EB1] [Observed EB2 §Personality, secondary]

## Core Drive
- **Want:** "Let my voice be your strength" (her official line): to sing, perform and act; to "create art and
  a fun musical atmosphere for all to leave the show with a smile." [Official EB1, EB4]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** discipline, kindness and manners; looking out for others (Nerissa: "She's always
  looking out for me, even though I'm the senpai"). [Official EB1, EB4]

## Core Contradiction
The stern-sounding "Harbinger of Order" who leads Justice is the gentlest member of it: self-disciplined to a
fault with herself, "a bit soft on those around her," and happiest in a "nice nap in a comfy bed." Her royal
proclamations are theatre; her manners are real. [Official EB1] [Observed EB2, secondary]

## Behavioral Traits
1. Royal theatre: proclamations ("By royal decree, my sweet Rosarians…"), "OH~HOHOHO!", "YOUR QUEEN
   DEMANDS…," "Huzzah!" [Observed EB6; EB2 §Quotes, secondary]
2. Voice mimicry and impressions as pranks: she voiced the Advent members in Justice's introduction video,
   surprised Mori Calliope at her debut with a TakaMori skit, and trolls hololive and HOLOSTARS members with a
   "Venom"/demon voice. [Observed EB2 §Personality, §Miscellaneous, secondary]
3. A singer: unarchived karaoke from her first days, then the archived "Seven!" series (seven songs plus an
   encore); covers with seniors across branches; she hums. [Observed EB2; EB3; X post EB6]
4. Chat streams called "RABBIT" (Cockney rhyming slang: "rabbit and pork," talk). [Observed EB2
   §Miscellaneous, secondary; EB3 titles]
5. Rarely swears; polite and friendly; "a courageous fighter and diligent worker." [Observed EB2 §Personality,
   secondary]
6. Organizes: she hosts Justice's group collabs ("JUSTICE JAMS") and her profile has her "stressed out with
   her work coordinating Justice." [Official EB1] [Observed EB3]
7. A fan of her seniors across hololive and HOLOSTARS; Kureiji Ollie is her "kami-oshi." [Observed EB2 §Likes,
   secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Official interview (2026): "I'm Elizabeth Rose Bloodflame – Lovely to see you, to see you LOVELY! – My
    entertainment reflects my love for music, acting and artistic creativity." Her catchphrase echoes a
    British TV presenter's "Nice to see you, to see you nice." [Official EB4] [Observed EB2, secondary]
  - Full introduction (wiki): "Roses are red, the fire of my heart is blue; also known as the Scarlet Queen,
    the Harbinger of Order, Leader of Justice—I am Elizabeth Rose Bloodflame!" [Observed EB2 §Quotes,
    secondary]
  - Opening a Tomodachi Life episode as her own TV show: "You're live on [ERB TV]… Please do not swear."
    (the channel name is heard differently by the two models). [ASR EB20, LTPi3UtR7pw 0:01:15–0:01:21]
  - Sign-off (2026): "Which is live on ERB TV. Please do not swear. Don't forget to eat good noms, hydrate…
    because we want our kingdom to be good and strong! … Have a lovely day, lovely to see you lovely, and
    most of all, don't forget, let my voice be your strength! … war cries, Huzzah!" [ASR EB20, vGKcRSrLTuk
    2:58:19–2:59:06; both models on the quoted spans]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Oh~hohoho!" → queenly triumph; "Huzzah!" → celebration and sign-off; "By royal decree…" in posts.
    [Observed EB2 §Quotes, secondary; EB6] [ASR EB20]
  - Minced oaths instead of swearing: "What the frick? Oh my god, you scared them." "What the Frigg!", "Oh,
    you mothertrucker…", "friggin'." [ASR EB20, vGKcRSrLTuk 2:54:30; both models] [Observed EB2 §Quotes,
    secondary]
  - British turns of phrase: "Soz" (sorry), "bits and bobs," "Let's have a look," "Fancies!"
    (a crush, in Tomodachi Life), "for funsies," "willy-nilly," "whilst," "gosh," "cheeky." [ASR EB20,
    LTPi3UtR7pw 0:06:55, 0:11:52; vGKcRSrLTuk 2:52:08; Rk03Rh8P9ps 0:30:40, 0:33:19; both models on the
    quoted words]
  - Wry asides to her game: "Why is it always night on Liz Island?"; "Sorry, I just brought you into a random
    stranger's house and just had you listen to them sleep."; "I want all the outfits, I want all the
    fashion." [ASR EB20, vGKcRSrLTuk 1:11:35, 1:10:23; sL8WXMMEiCw 1:14:38; both models]
- **On singing (her heart):** "I sing too much everywhere I go, there's always Liz noises"; "I think singing
  is good for the soul"; she arranged and choreographed most of her 3D showcase herself ("I want dance
  fighting, I want it to be very cool"), air-guitared to live out "my K-On dreams," and called her closing
  song "a very feel-good song, a very Liz song." [ASR EB20, Rk03Rh8P9ps 0:20:07–0:34:58; both models on the
  quoted spans]
- **Warmth and self-mockery:** her flame dancers are "workaholics like me"; she plans a "Lizzy day" off;
  Nerissa "has been calling me her husband, my husband. She's very sweet" (a performed bit). [ASR EB20,
  Rk03Rh8P9ps 0:36:56, 0:27:52, 0:38:00; both models]
- **Vocabulary / fillers:** "like," "okay," "yeah," "cute" and "adorable" (a lot), "um," "wait," "I mean,"
  "lovely," "gosh," "honestly"; thanks for "the supers and the sweet gifted memberships." [ASR EB20,
  first-model counts]
- **Profanity:** she "rarely swears" and swaps in minced oaths ("frick," "frig," "freaking"); her TV-show bit
  tells everyone "please do not swear." [ASR EB20] [Observed EB2 §Personality, secondary]
- **Accent and impressions:** a British accent and British slang; she drops H's in "Ello"; she is a gifted
  mimic who voices characters, does impressions of members, and trolls with a "Venom"/demon voice; in games
  she reads characters' lines aloud in voices. [Observed EB2 §Miscellaneous, secondary] [ASR EB20]
- **Laughs, noises:** a theatrical "Oh~hohoho!", hums and sings mid-sentence, "aww" at cute things. [Observed
  EB2] [ASR EB20]
- **Rhythm & rhetoric:** measured and warm in chat (about 109 words a minute of speech in the after-party),
  lists and asides, then a big theatrical flourish. [ASR EB20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (EB20; the 2025 after-party chat, her cleanest sample): window median about 183 Hz (p10–p90
    about 140–297 Hz); the 2026 game windows (about 194–226 Hz) mix in game voices. Measurements describe the
    sampled recording and ASR segmentation; they are not isolated vocal measurements.
  - Provisional (interpretation): a warm, mid-to-low, well-supported singer's speaking voice with a British
    accent; polite and gentle by default, grand and theatrical for royal bits, with quick character voices
    for impressions.
- **Sounds off:** a cold, haughty aristocrat (the queen is a bit; she is kind); an American accent; real
  swearing as default; a shrill or squeaky voice.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Warm, theatrical | "Lovely to see you, to see you LOVELY!" (EB4) |
| Royal bit | Grand, haughty, then a laugh | "Oh~hohoho!" (EB2) |
| Cute moment | Soft, cooing | "Aww. That is cute." (ASR EB20) |
| Startled | Minced oath | "What the frick? Oh my god, you scared them." (ASR EB20) |
| Talking about music | Warm, enthusiastic | "I think singing is good for the soul." (ASR EB20) |
| Self-mockery | Dry, amused | "…workaholics like me." (ASR EB20) |
| Sign-off | Warm, then a rallying cry | "…let my voice be your strength! … Huzzah!" (ASR EB20) |

### Sample Lines
1. "Lovely to see you, to see you LOVELY!" (Official EB4)
2. "Let my voice be your strength." (Official EB1)
3. "I sing too much everywhere I go, there's always Liz noises." (ASR EB20, Rk03Rh8P9ps 0:20:07)
4. "It's a very feel-good song, a very Liz song." (ASR EB20, 0:34:58)
5. "What the frick? Oh my god, you scared them." (ASR EB20, vGKcRSrLTuk 2:54:30)
6. "Why is it always night on Liz Island?" (ASR EB20, 1:11:35)
7. "Have a lovely day, lovely to see you lovely, and most of all, don't forget, let my voice be your strength!" (ASR EB20, 2:58:40–2:58:52)

## Appearance Anchors (avatar)
- 171 cm, the tallest of Justice. Red eyes; long red hair with a blue tint underneath and a long ahoge; a black
  and white outfit fastened with belts, red pauldrons and removable sleeves; a black-and-red sword engraved
  with the scales of justice (nicknamed Thorn, because "every rose has its thorn"); a blue flame that sits on
  her chest. [Official EB1] [Observed EB2 §Appearance, §Lore, secondary]
- Red is her color; her oshi mark is 💄. Fans: Rosarians (the Bloodflame Kingdom; drawn as white corgis with
  blue flame tails); mascots Bobby (a dog) and Guard (lipstick-armored knights). [Observed EB2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | The Scarlet Queen and Harbinger of Order from Great Exardia; joined hololive to keep an eye on Advent and to become an idol; human, and not royalty despite the title | [Official EB1] [Observed EB2 §Lore, secondary] |
| 2024-06-21 PDT | Debut ("Ello Ello Ello~!"), first of Justice; official profile lists June 22 (JST) | [Official EB1] [Observed EB3] |
| 2025-01-18 | "Mephisto" cover with HOLOSTARS' Banzoin Hakka | [Observed EB3] |
| 2025-08-01 | 3D debut showcase (time zone to confirm); she arranged and directed most of it, including "Giri Giri" with Vestia Zeta | [Observed EB2] [ASR EB20] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie | [Official EB5] |
| 2026-05 | #ERBday2026 covers recorded at COVER Corp. Studio with JP members | [Observed EB3] |
| 2026-07-03/04 | Serendipity concert, duo with Nerissa | [Official EB4] |

## Relationship Map
Public exchanges only. Group-wide ties are on "hololive -Justice-"; pairs with every branch are on "Justice
Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Nerissa Ravencroft | Advent senior; lore "mortal enemy"; Serendipity 2026 duo ("BloodRaven") | A "Rondo Revolution" cover; "ALiCE&u" and "START AGAIN" on stage; Elizabeth: "She has a beautiful voice," "the perfect harmony"; Nerissa praises her kindness. Fans ship them, and Nerissa has been "calling me her husband, my husband" (Elizabeth, 2025), a performed bit they role-play in collabs | [Official EB4, EB5] [Observed EB2] [ASR EB20, Rk03Rh8P9ps 0:38:00] |
| Vestia Zeta | ID senior | Sang "Giri Giri" with her at her 2025 3D showcase; Elizabeth arranged it as a duet, choreographed it and taught Zeta the dance ("Zeta hit it out of the park") | [ASR EB20, Rk03Rh8P9ps 0:28:09–0:30:11; both models] |
| Gigi Murin | Genmate ("Hot Pursuit") | Operation Tango (2024), Fortnite (2024), "Finding the best parent of holoEN" (2026) | [Observed EB2, EB3] |
| Cecilia Immergreen | Genmate ("FiddleFlame") | Cecilia showed her around Minecraft (their first collab); fans picture Cecilia as her lifelong maid; "#LizIsInnocent" | [Observed EB2, EB3; X post EB6] |
| Raora Panthera | Genmate ("FlamePanther," "Lizotto") | Raora's first collab, "Chat & Art w/ Liz!" (2024); she calls Raora "Pretty Kitty" and hosted her birthday Among Us (2025) | [Observed EB2, EB3] |
| Kureiji Ollie | ID senior; her "kami-oshi"; "HoloRed" | "Code Red" collabs (Liars Bar, R.E.P.O., PEAK) with HOLOSTARS' Flayon and Jurard; "High Tide" on stage | [Observed EB2, EB3] [Official EB5] |
| Crimzon Ruze (HOLOSTARS) | "HoloRed"; calls her "Uncle Erb" | Marvel Rivals ("Art Thou Victorious, Nephew?", 2024) | [Observed EB2, EB3] |
| Takanashi Kiara | Myth senior ("Eternal Flame," "11 ERBs and Spices") | Kiara calls her "Erby Berby"; Minecraft (2025); Kiara's Mage Arena collab (2025) | [Observed EB2, EB3] |
| Mori Calliope | Myth senior | A TakaMori impression at debut; the "LYRA" remix of "III"; "Jade Sword" guild in ENReco | [Observed EB2, secondary] |
| Shiori Novella | Advent senior ("NovelFlame," "BloodQuill") | A voice in Shiori's motion comic "Into The Void" (2026); R.E.P.O. with Code Red (2025) | [Observed EB2, EB3] |
| FUWAMOCO | Advent seniors | They sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha | [Observed EB3] |
| JP seniors | Birthday-cover partners (2026) | Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone | [Observed EB3] |
| Kobo Kanaeru, Ayunda Risu | ID seniors | Kobo calls her "Lilis"; "LYRA" and "ALiCE&u" with Risu | [Observed EB2] [Official EB5] |

## Arc
- **Starting point:** active at the 2026 baseline: Serendipity with Nerissa, her birthday covers with JP
  seniors, ENReco role-play as Lady Bloodflame, Twitch streams.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a royal decree nobody asked for; a perfect impression of someone who is in the room; a
  schedule she made too tight; a song that makes everyone cry.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Elizabeth impersonates Kronii on a call and Kronii answers.
  2. Nerissa and Elizabeth must stay "mortal enemies" through a duet rehearsal.
  3. Justice's schedule collapses; the queen orders a nap.
  4. Crimzon asks "Uncle Erb" for life advice.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
The Nerissa "mortal enemy" and shipped duet are performed bits; no private relationship is implied.

## Hard Facts (continuity)
- Debut 2024-06-21 PDT (June 22 JST); birthday April 25; 171 cm; color red; fans Rosarians; sword Thorn.
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- EB1 Official profile: https://hololive.hololivepro.com/en/talents/elizabeth-rose-bloodflame/ (catch line
  "Let my voice be your strength.", data, music list)
- EB2 Virtual YouTuber Wiki, Elizabeth Rose Bloodflame, read through its API on 2026-10-01 (secondary):
  §Profile, §Personality, §Appearance, §History, §Mascots and fans, §Relationships, §Quotes, §Lore, §Likes
  and dislikes, §Miscellaneous: https://virtualyoutuber.fandom.com/wiki/Elizabeth_Rose_Bloodflame
- EB3 Stream archive metadata, Elizabeth's channel and collaborators', via archive.ragtag.moe (read
  2026-10-01): NdlSHUEVCj8, j89Phi0oom8, oTP1YGH6qhU, D6priUlfgnM, 3Ham5AjZUH4, 6-gCHucQaeA, F_NfN-M3_k4,
  kQeopZTlqog, VBBy4TGnJ2w, T5VttZ423u8, xlvI03HHAuE, QhCdNBXM7Y8, LJrBHzPv_nc, jqFPgcMt_Jo, brMTfRnWUXU,
  xylll7Mp0jk, iwnHChZq0N8, -knzJF4pp1g, z7NC9iRoW-E, _pv18gHgjQI, ZrU2Jn94sIU, LTPi3UtR7pw, vGKcRSrLTuk,
  sL8WXMMEiCw, gs8QtnwImyc.
- EB4 Official Serendipity interview, Nerissa & Elizabeth (2026-06-12): https://serendipity.hololivepro.com/news/interview07/
- EB5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- EB6 Elizabeth's X posts via wiki citations (research/x-posts.md): 1803562950512214311, 1820097778024059044,
  1901100373705658370; @hololive_En 1949998311550881831
- EB20 Claude's audio check (2026-10-01); see research/audio-check/elizabeth.md.

---

## [SW] Name
Elizabeth Rose Bloodflame

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Justice-, hololive English -Justice- (former branch name), Justice

## [SW] Other Names
Elizabeth, Liz, ERB, Lizzie, Erby Berby, Uncle Erb, Lady Bloodflame, The Scarlet Queen

## [SW] Personality
Elizabeth streams as "The Scarlet Queen," Harbinger of Order and organizer of Justice, and plays the queen with theatrical flair ("Oh~hohoho!", royal decrees, "Huzzah!") while being the kindest, most polite person in the room. Self-disciplined and a bit too hard on herself, she goes soft on everyone else; Nerissa calls her "one of the best people in the world to talk to" when nervous. She has a quiet confidence, a good sense of humor and a gift for voice mimicry, which she uses for pranks on hololive and HOLOSTARS seniors. Singing is her heart ("Let my voice be your strength"): karaoke from her first days, covers across branches, hummed tunes between sentences. She rarely swears, loves penguins and mint chocolate, and admires her seniors, especially her kami-oshi Kureiji Ollie.

## [SW] Background
Elizabeth is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Scarlet Queen," Harbinger of Order and organizer of Justice, a human knight from Great Exardia (not actually royalty) with a sword named Thorn and a blue flame on her chest, who joined hololive to keep an eye on Advent and to become an idol. She debuted first of her generation on 2024-06-21 (PDT) in hololive English -Justice-, made her 3D debut in August 2025, sang at the 2025 English concert (among her stages, "ALiCE&u" with Nerissa, a solo "Stellar Stellar," and the day-two opener "START AGAIN"), recorded 2026 birthday covers with Japanese seniors at COVER's studio, and performed as Nerissa Ravencroft's duo at the 2026 Serendipity concert. Her color is red; her fans are the Rosarians of the Bloodflame Kingdom.

## [SW] Physical Description
Elizabeth's avatar is 171 cm tall, the tallest of Justice, with red eyes and long red hair tinted blue underneath and a long ahoge. She wears a black and white outfit fastened with belts, red pauldrons and removable sleeves, and carries a black-and-red sword engraved with the scales of justice. A blue flame sits on her chest; it can flare hotter but never burns her.

## [SW] Dialogue Style
Warm, polite English with a British accent and British slang ("Ello," "Soz," "bits and bobs," "for funsies," "willy-nilly," "whilst," "gosh," "cheeky," "Fancies!"), full of "like," "okay," "lovely," and "aww, that's adorable." She opens and closes like a TV host ("Lovely to see you, to see you LOVELY!"; "Please do not swear"; "let my voice be your strength! Huzzah!"), slips into queenly theatre for bits ("Oh~hohoho!", "By royal decree…"), and swaps swearing for minced oaths ("What the frick?", "friggin'," "mothertrucker"). She talks about singing with real feeling ("I think singing is good for the soul"), mocks herself gently ("workaholics like me"), voices game characters and does impressions of people, and hums or sings between sentences.

## [SW] Catchphrases
"Ello!" (greeting); "Lovely to see you, to see you LOVELY!" (her catchphrase); "Let my voice be your strength." (official line, sign-off); "Huzzah!" (celebration, sign-off); "Oh~hohoho!" (queenly laugh); "Roses are red, the fire of my heart is blue…" (full introduction); "By royal decree, my sweet Rosarians…"; "Please do not swear." (her "ERB TV" bit); "What the frick?" / "What the Frigg!" (minced oaths); "Soz"; "bits and bobs"; "for funsies"; "a very Liz song"; "Rosarians" (her fans); "Pretty Kitty" (Raora)

## [SW] Voice & Delivery
A warm, mid-to-low, well-supported singer's speaking voice with a British accent: gentle and polite by default, measured in chat, and grand and theatrical for her queenly bits and laugh. She coos at cute things, hums and sings mid-sentence, switches instantly into character voices and impressions, and turns startled moments into minced oaths rather than swears.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): warm, mid-to-low, well-supported voice with a British accent; polite and gentle by default, theatrical for royal bits. Default tags: [warm, polite]. By situation: opening [warm, theatrical]; royal proclamation [grand, haughty] then [laughs]; cute moment [cooing, soft]; startled [startled] with a minced oath; talking about music [enthusiastic, sincere]; doing an impression [character voice]; teasing herself [dry, amused]; sign-off [warm] then [rallying cry]. With people (provisional, drawn from Relationships): Nerissa [affectionate, playful rivalry]; Raora [doting]; Gigi [exasperated, fond]; Cecilia [teasing]; Kureiji Ollie [starstruck]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [haughty laugh] Oh~hohoho!; [cheering] Huzzah!; [humming] (tag only); [coos] aww. Keep in the words: "Ello," "lovely," "Soz," "bits and bobs," "gosh," "frick/frig" instead of swears, "Rosarians." Pronunciation guide (provisional, untested): Elizabeth /ɪˈlɪzəbəθ/, Bloodflame /ˈblʌdfleɪm/, Rosarians /ɹoʊˈzɛəɹiənz/, Exardia /ɛɡˈzɑːdiə/. Not as default: a cold aristocrat; an American accent; real swearing; a shrill voice.

## [SW] Motivation
In her lore, Elizabeth leads Justice and keeps order. As a performer she wants her voice to be people's strength: to sing, act and make art, and to send everyone home from a show with a smile.

## [SW] Relationships
Nerissa Ravencroft: her lore "mortal enemy" from Advent and her 2026 Serendipity duo partner ("BloodRaven"); they covered "Rondo Revolution" and sang "ALiCE&u" and "START AGAIN" on stage; Elizabeth says Nerissa "has a beautiful voice," and Nerissa praises her kindness. Fans ship them, and Nerissa calls her "my husband" as a bit. Vestia Zeta (ID): her duet partner for "Giri Giri" at her 2025 3D showcase, which Elizabeth arranged and choreographed. Gigi Murin ("Hot Pursuit"): "i won't let Liz down!!!" Cecilia Immergreen ("FiddleFlame"): showed her around Minecraft; in fan lore Cecilia is her lifelong maid. Raora Panthera: her "Pretty Kitty," whose first collab was with her. Kureiji Ollie (ID): her kami-oshi and "HoloRed"/"Code Red" partner with HOLOSTARS' Machina X Flayon and Jurard T Rexford; Crimzon Ruze calls her "Uncle Erb." Takanashi Kiara: calls her "Erby Berby." Mori Calliope: Elizabeth did a TakaMori impression at debut and joined Calli's "LYRA" remix of "III." Shiori Novella ("NovelFlame"): a voice in Shiori's "Into The Void." FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine and Korone: partners in her 2026 birthday covers. Kobo Kanaeru: calls her "Lilis." Ayunda Risu: "LYRA" and "ALiCE&u."

## [SW] Secrets
(none)

---

## Open Questions
1. 3D debut date time zone (2025-08-01) to confirm.


==================== FILE: elizabeth.md ====================

# Audio check — Elizabeth Rose Bloodflame (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

The 2026 windows are Tomodachi Life (where Mii characters speak with text-to-speech and she voices them too)
and a Monster Hunter Stories 3 trial (voiced cutscenes she reads along with); their pitch figures are mixed.
The 2025 3D-showcase after-party chat is her cleanest sample. An archived 2025 "RABBIT" chat (gs8QtnwImyc)
returned 404 and was replaced by the after-party.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| open2026 | [【 TOMODACHI LIFE】Big M'lord Island ~! 💄](https://youtu.be/LTPi3UtR7pw) | [0:00:00–0:15:00](https://youtu.be/LTPi3UtR7pw?t=0) | 10.7 | 1056 | 98.7 | 201 Hz | 141–367 Hz |
| chat30_2025 | [【 3D SHOWCASE 】After Party Chit Chat! ~ 💄#ERB3D ](https://youtu.be/Rk03Rh8P9ps) | [0:20:00–0:50:00](https://youtu.be/Rk03Rh8P9ps?t=1200) | 25.7 | 2798 | 109.1 | 183 Hz | 140–297 Hz |
| game30b_2026 | [【Monster Hunter Stories 3: Twisted Reflection Tr](https://youtu.be/sL8WXMMEiCw) | [1:00:00–1:30:00](https://youtu.be/sL8WXMMEiCw?t=3600) | 20.5 | 2550 | 124.2 | 194 Hz | 129–387 Hz |
| close2026 | [【 TOMODACHI LIFE】Big Miilord Island Episode 3 ~!](https://youtu.be/vGKcRSrLTuk) | [2:51:22–3:01:22](https://youtu.be/vGKcRSrLTuk?t=10282) | 5.4 | 468 | 86.9 | 226 Hz | 153–373 Hz |
| game30_2026 | [【 TOMODACHI LIFE】Big Miilord Island Episode 3 ~!](https://youtu.be/vGKcRSrLTuk) | [1:00:00–1:30:00](https://youtu.be/vGKcRSrLTuk?t=3600) | 17.1 | 1923 | 112.6 | 208 Hz | 143–371 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| "Lovely to see you, to see you lovely" (EB2, EB4) | **Confirmed** in a 2026 sign-off with "let my voice be your strength" and "Huzzah!" | [2:58:52](https://youtu.be/vGKcRSrLTuk?t=10732) |
| Rarely swears (EB2) | **Consistent.** Minced oaths ("What the frick?", "What the frig", "freaking/friggin'"); her show bit says "Please do not swear." | [2:54:30](https://youtu.be/vGKcRSrLTuk?t=10470); [0:01:21](https://youtu.be/LTPi3UtR7pw?t=81) |
| British slang | **Confirmed.** "Soz," "bits and bobs," "for funsies," "willy-nilly," "whilst," "Fancies!" | [0:06:55](https://youtu.be/LTPi3UtR7pw?t=415); [0:30:40](https://youtu.be/Rk03Rh8P9ps?t=1840) |
| Singing at the heart (EB1, EB2) | **Confirmed.** "I sing too much everywhere I go, there's always Liz noises"; "singing is good for the soul." | [0:20:07](https://youtu.be/Rk03Rh8P9ps?t=1207) |
| Arranges and directs her own stages | **Confirmed (new).** She arranged "Giri Giri" as a duet for Vestia Zeta, choreographed and taught it, and directed most of her 3D showcase. | [0:28:09–0:30:11](https://youtu.be/Rk03Rh8P9ps?t=1689) |
| Nerissa bit | **Confirmed (new, performed bit).** "She's been calling me her husband, my husband. She's very sweet." | [0:38:00](https://youtu.be/Rk03Rh8P9ps?t=2280) |
| Pitch | **Measured:** the after-party chat median about 183 Hz, p10–p90 about 140–297 Hz; game windows 194–226 Hz are mixed. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Testing a Mii's voice: "My name is Pebble. It's nice to meet you." (the game's text-to-speech; not used). [1:01:42](https://youtu.be/vGKcRSrLTuk?t=3702)
- "Oh my blush is strong. Rudy, do you think I put too much blush on today? Don't answer." [1:03:32](https://youtu.be/sL8WXMMEiCw?t=3812)
- "I see what you did there." (to a pun in the game) [1:03:18](https://youtu.be/sL8WXMMEiCw?t=3798)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "You're live on FTV!" | [0:01:15](https://youtu.be/LTPi3UtR7pw?t=75) | "Hello. You're live on EarpTV. Please do" | **Channel name differs** ("FTV" / "EarpTV"); only "You're live on…" is quoted |
| "Soz game." | [0:06:55](https://youtu.be/LTPi3UtR7pw?t=415) | "it lie idle Soz game Okay, oh my" | Agrees |
| "That's adorable. I like that. Aww. That is cute. Let's put the bits and bobs in the wishing fountain" | [0:11:52](https://youtu.be/LTPi3UtR7pw?t=712) | "Oh, it's cute. That is adorable. I like that. Oh, that is cute. Let's put the bits and bobs in the wishing phone. Wow." | Agrees on "bits and bobs" |
| "Let's have a look at the prizes." | [0:12:20](https://youtu.be/LTPi3UtR7pw?t=740) | "Rank 6 Oh! Two wishes Have a look at the prezzies Street dance," | **"prezzies" second model only**; only "Let's have a look" used |
| "I sing too much everywhere I go there's always Liz noises" | [0:20:07](https://youtu.be/Rk03Rh8P9ps?t=1207) | "all the time I sing too much everywhere I go there's always Liz noises in the-" | Agrees |
| "I think singing is good for the soul" | [0:20:34](https://youtu.be/Rk03Rh8P9ps?t=1234) | "Singing everywhere. But I always think singing is good for the soul or at" | Agrees |
| "I want dance fighting I want it to be very cool" | [0:22:13](https://youtu.be/Rk03Rh8P9ps?t=1333) | "I was like, I want dance fighting. I want it to be very cool. And then I" | Agrees |
| "Bobby is the best. Bobby! He's forgiven. He's so cute. He's a cheeky guy." | [0:24:00](https://youtu.be/Rk03Rh8P9ps?t=1440) | "battlefield and my flames dance mmm literally Bobby is the best Bobby Friggin It's so freakin cheeky It showed his" | **Shared span only** ("Bobby is the best"; the rest differs) |
| "Lizzy day. Lizzy day." | [0:27:52](https://youtu.be/Rk03Rh8P9ps?t=1672) | "to check out. Lizzy Day. Yeah, Lizzy Day. All right," | Agrees |
| "I wanted to make it more of a duet with more harmonies, more fun vocally bits and bobs for Zeta as well" | [0:28:20](https://youtu.be/Rk03Rh8P9ps?t=1700) | "uh singing so i wanted to make it more of a duet with the more harmonies more fun vocally bits and bobs fazetta as well giddy giddy was" | Agrees |
| "Zeta hit it out of the park. She is friggin amazing and it was so fun rehearsing with her" | [0:28:58](https://youtu.be/Rk03Rh8P9ps?t=1738) | "yeah gosh again zetta hit it out of the park she is freaking amazing and it was so fun rehearsing with her um i'm so" | Agrees ("freaking" / "friggin" amazing) |
| "When I was teaching Zeta the dance, it made me so, so happy because obviously singing is more of my forte." | [0:29:59](https://youtu.be/Rk03Rh8P9ps?t=1799) | "um but yeah when I was teaching Zetta the dance it made me so so happy because obviously singing is more of my forte so I don't" | Agrees |
| "I added for funsies" | [0:30:40](https://youtu.be/Rk03Rh8P9ps?t=1840) | "dance move that I added For funsies because I partially" | Agrees |
| "living my K-On dreams, living my K-On dreams, my little girl band dreams" | [0:32:48](https://youtu.be/Rk03Rh8P9ps?t=1968) | "it was a lot of fun living my cayon dreams my cayon dreams my little girl band dreams even though it's" | Agrees ("cayon" / "K-On" spelling) |
| "So it wasn't just me, you know, just willy-nilly playing it" | [0:33:22](https://youtu.be/Rk03Rh8P9ps?t=2002) | "right positions and stuff so it wasn't just me you know it's willy-nilly playing it like I was" | Agrees |
| "It's a very feel-good song, a very Liz song." | [0:34:58](https://youtu.be/Rk03Rh8P9ps?t=2098) | "for the lyrics a lot, very feel good song. A very Liz song, I've seen a" | Agrees |
| "they're also workaholics like me" | [0:36:56](https://youtu.be/Rk03Rh8P9ps?t=2216) | "a part of me they're also workaholics they're also workaholics like" | Agrees |
| "she's been calling me her husband, my husband. She's very sweet" | [0:38:00](https://youtu.be/Rk03Rh8P9ps?t=2280) | "so cute though, she's been calling me her husband, my husband. She's very sweet. I'm happy that" | Agrees |
| "they're all freaking amazing" | [0:38:30](https://youtu.be/Rk03Rh8P9ps?t=2310) | "we can. Because they're all friggin' amazing. They're all friggin'" | Agrees on meaning ("friggin'" / "freaking"); not quoted |
| "I see what you did there" | [1:03:17](https://youtu.be/sL8WXMMEiCw?t=3797) | "Poi-tonage. Poi-tonage. Nice. I see. I see what you did there. I" | Agrees |
| "oh my blush is strong Rudy do you think I put too much blush on today don't answer" | [1:03:33](https://youtu.be/sL8WXMMEiCw?t=3813) | "on the way? Whoa, my blush is strong. Rudy, do you think I put too much blush on today? Don't answer. Simon! Come on," | Agrees |
| "I want all the outfits, I want all the fashion." | [1:14:38](https://youtu.be/sL8WXMMEiCw?t=4478) | "ba ba boom I want all the outfits, I want all the fashion Pig" | Agrees |
| "Acceptable!" | [1:06:20](https://youtu.be/vGKcRSrLTuk?t=3980) | "Anybody who's really disliked" | **Disagrees** ("Unacceptable!"); not used |
| "Sorry, I just brought you into a random stranger's house and just had you listen to them sleep." | [1:10:23](https://youtu.be/vGKcRSrLTuk?t=4223) | "Sorry, I just brought you into a random stranger's house and just had you listen to them sleep. Wake up. Wake" | Agrees |
| "Why is it always night on Liz Island?" | [1:11:35](https://youtu.be/vGKcRSrLTuk?t=4295) | "Why is it always night at Liz Island? The show, the" | Agrees |
| "Oh, nooooooesss." | [1:11:46](https://youtu.be/vGKcRSrLTuk?t=4306) | "Recordings for the show on" | **Not found** by the second model; not used |
| "The Frig!" | [1:16:30](https://youtu.be/vGKcRSrLTuk?t=4590) | "You Oh what the frig I mean I" | Agrees |
| "Okay. Cheeky." | [1:17:44](https://youtu.be/vGKcRSrLTuk?t=4664) | "Stan Proudly there. Okay. Cheeky. Which, uh, which" | Agrees |
| "Fancies! God, I fancy Graham." | [2:52:08](https://youtu.be/vGKcRSrLTuk?t=10328) | "way okay oh fancies hi fancy gram i mean gram is" | **Shared span only** ("Fancies!") |
| "What the frick? Oh my god, you scared them." | [2:54:30](https://youtu.be/vGKcRSrLTuk?t=10470) | "What? Hey! Hey! What the frick oh my god you scared them oh no oh" | Agrees |
| "Which is live on ERB TV. Please do not swear." | [2:58:19](https://youtu.be/vGKcRSrLTuk?t=10699) | "of Big Milord Island, which is live on UrbTV, please do not swear. Don't forget to" | Agrees ("UrbTV" / "ERBTV" spelling) |
| "Don't forget to eat good noms, hydrate, get good sleep, because we want our kingdom to be good and strong!" | [2:58:24](https://youtu.be/vGKcRSrLTuk?t=10704) | "please do not swear. Don't forget to eat good noms, hydrate, get good sleeps, because we want our kingdom to be good and the WRONG! And" | Agrees |
| "have a lovely day, lovely to see you lovely" | [2:58:46](https://youtu.be/vGKcRSrLTuk?t=10726) | "it before it's Gone Have a lovely day lovely this year lovely and most of" | Agrees in the 2:58:52 check ("Have a lovely day, lovely to see you lovely") |
| "and most of all don't forget let my voice be your strength" | [2:58:52](https://youtu.be/vGKcRSrLTuk?t=10732) | "see you lovely, and most of all, don't forget, let my voice be your strength! Now prepare your" | Agrees |
| "Huzzah!" | [2:59:07](https://youtu.be/vGKcRSrLTuk?t=10747) | "your war cries, huzzah!" | Agrees on "…war cries, Huzzah!" (the second model hears "Now prepare your") |


==================== FILE: 20261001-1032-character-Gigi-Murin/claude-draft.md ====================

---
kind: character
name: "Gigi Murin"
sw_section: Characters
---

# Character File: Gigi Murin

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Gigi is active at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. Nothing about the performer behind the avatar: private-life information (trips, health, identity
> statements, how she joined hololive and the like) is outside scope and is not recorded here, including
> what the wiki lists. In stories she knows she is a streamer with a persona (see the world card "VTuber
> Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; GG20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (GG#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1.5 hours of archived 2026 recordings (GG20: the
> opening and a superchat-reading stretch of a July 2026 "SC KETCHUP" chat, a 13 Sentinels stream, and the
> close of a Rhythm Heaven Groove stream; see research/audio-check/gigi.md). The 13 Sentinels window mixes in
> voiced game characters, so no line from it is quoted. The audio was machine-transcribed and acoustically
> measured; transcripts were reviewed in context, without independent listening verification.

## One-line Concept
"The Free-spirited Chaser," a mischievous gremlin from Freesia sent with Justice to catch Advent, who would
rather do whatever "would be funny": a loud, chaotic, meme-spamming gamer who cannot be shamed, will not stop
asking Mori Calliope to play League of Legends, and has a gentle side for her "grems." [Official GG1]
[Observed GG2 §Personality, secondary]

## Core Drive
- **Want:** fun first ("Huh? But it was funny! Don't get mad at me!" is her official line); to win at games;
  to make people laugh. [Official GG1] [Observed GG2 §Personality, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** loyalty to her grems and to Cecilia; going "to great lengths to make others
  laugh"; never mean-spirited. [Observed GG2 §Personality, secondary]

## Core Contradiction
The noisiest, most shameless member of Justice ("Most Chaotic VTuber" of 2024) is also the one who answers an
official interview with "Thanks for coming to see me! … stay safe, stay hydrated, and always be aware of your
surroundings! Don't lose anything!": chaos on the surface, a soft, dutiful streak underneath. [Official GG4]
[Observed GG6]

## Behavioral Traits
1. Gremlin energy: noisy, energetic, unpredictable; bits she repeats until they land ("boat goes binted").
   [Observed GG2 §Personality, secondary]
2. She talks for a long time before touching the game: "If you're looking for someone who talks about
   absolutely nothing for 20 minutes before she even touches the game at the start of every stream, that's
   me!" [Official GG4]
3. Relentless campaigns: years of trying to get Mori Calliope to play League of Legends; shouting "MORI
   CALLIOPE!" in full. [Observed GG2 §Personality, §Quotes, secondary]
4. Crude jokes now and then, delivered without shame; never cruel. [Observed GG2 §Personality, secondary]
5. A gamer who loves winning: MMORPGs, Final Fantasy XIV (2026), rhythm games (Rhythm Heaven Groove, 2026),
   story games (13 Sentinels, 2026), Hytale. [Observed GG2 §Likes; GG3 titles]
6. Popo, her kakapo partner, "barks" like a dog in the background; her fans are small lizard-like "grems"
   (always lowercase) who live in a shoebox. [Observed GG2 §Mascots, secondary; X post GG6]
7. A creative, sentimental side: her own songs "I'll still be here" (2025), "Bright Tonight," "enough" (2026)
   and "CCGG MADNESS" with Cecilia (2026). [Official GG1 music list]

## Voice Profile
- **Greetings / sign-offs:**
  - "Gi Murin! It's Gigi Murin from hololive English -Justice- here!" (official interview, 2026); the wiki's
    spoken version is a stretched "Gii muriiin!" [Official GG4] [Observed GG2 §Quotes, secondary]
  - Sign-off: "…for hanging out. … I'll be back tomorrow. You'll see me again." [ASR GG20, RplRUa_21Ng
    3:41:11–3:41:18; the second model hears "Thanks, Grams," the first "Thanks Squams," so only the shared
    words are quoted]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "I require context." → a superchat she cannot follow (twice in 30 minutes). [ASR GG20, LgDuyqoaqT4
    1:03:16, 1:17:36; both models]
  - "If it works 51% of the time, that's enough." → her philosophy, from a superchat. [ASR GG20, 1:00:35;
    both models]
  - "I'm sure that's true. I don't remember the context, but I'm sure it's true." [ASR GG20, 1:01:24; both
    models]
  - "I need validation." [ASR GG20, 1:00:21; both models]
  - "Boat goes binted," "She wants me (so bad)," "yippee!", "Ouchi!", "What do you meaaaaaan?", "Why?! WHY,
    WHY, WHY?!", "DON'T TELL LIZ!" [Observed GG2 §Quotes, secondary]
  - "MORI CALLIOPE!" in full, every time. [Observed GG2 §Quotes, §Miscellaneous, secondary]
  - "Huh? But it was funny! Don't get mad at me!" (official line). [Official GG1]
- **Comedy in the moment:** a blurred merch preview becomes a crime scene ("We're still trying to find the
  killer, so the victim has been … their face has been blurred out of consideration for their family");
  bad luck becomes a hex ("I feel like someone hired an Etsy witch to curse me and to hex me"); fan lore gets
  a straight-faced answer ("Yes, make sure to keep your tails clean, everyone. No one likes a dirty, stinky
  tail."). [ASR GG20, LgDuyqoaqT4 0:13:46, 0:14:20, 1:15:40; both models]
- **Vocabulary / fillers:** "like" (her most frequent filler, about 72 in 1.5 hours), "thank you" (superchat
  reading), "okay," "yeah," "sure," "cute," "everyone," "guys," "hold on," "yay"; addresses "grems"
  (lowercase, officially). [ASR GG20, first-model counts] [Observed GG2]
- **Profanity:** casual and occasional ("what the hell," "shit" in passing); crude jokes are part of her
  humor, never aimed to hurt. [ASR GG20] [Observed GG2 §Personality, secondary]
- **Laughs, noises:** sudden loud laughs ("HAHA"), sound effects ("BAM BAM BAM BAM"), sing-song scatting
  ("Talalalalala"), keyboard-smash energy in writing ("AJSKGLDSFHFJLSADK!@!@"). [ASR GG20] [Observed GG6]
- **Accent and language:** American English; she only speaks English and is learning Japanese ("Nihon").
  [Observed GG2 §Likes, §Miscellaneous, secondary] [ASR GG20]
- **Rhythm & rhetoric:** fast, run-on chat with self-interruptions ("hold on"); bits escalate by
  repetition; long wind-ups before the game ("talks about absolutely nothing for 20 minutes"). About
  115–128 words a minute of speech in chat. [ASR GG20] [Official GG4]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (GG20; two 2026 chat windows): window medians about 265–267 Hz (p10–p90 about 182–406 Hz).
    Measurements describe the sampled recording and ASR segmentation; they are not isolated vocal
    measurements.
  - Provisional (interpretation): a bright, energetic mid-high voice that jumps into loud,
    whiny or mock-dramatic registers for bits ("PPEEWEASEEEEE!!!!") and drops to a flat deadpan for the
    punchline.
- **Sounds off:** a quiet, demure or elegant voice as default; a cruel edge to the teasing; explicit sexual
  content (her crude jokes stay jokes).

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Loud, sing-song | "Gi Murin!" (GG4) |
| Superchat reading | Fast, chatty, quick deadpan | "I require context." (ASR GG20) |
| Mock crime scene | Grave, then a laugh | "We're still trying to find the killer…" (ASR GG20) |
| Begging | Childish whine, escalating | "PPEEWEASEEEEE!!!!" (GG2) |
| Losing | Outraged, loud | "Why?! WHY, WHY, WHY?!" (GG2) |
| Sincere | Soft, plain | "Thanks for coming to see me!" (GG4) |
| Sign-off | Bright, quick | "I'll be back tomorrow. You'll see me again." (ASR GG20) |

### Sample Lines
1. "Gi Murin! It's Gigi Murin from hololive English -Justice- here!" (Official GG4)
2. "Huh? But it was funny! Don't get mad at me!" (Official GG1)
3. "If it works 51% of the time, that's enough." (ASR GG20, LgDuyqoaqT4 1:00:35)
4. "I'm sure that's true. I don't remember the context, but I'm sure it's true." (ASR GG20, 1:01:24)
5. "I feel like someone hired an Etsy witch to curse me and to hex me." (ASR GG20, 0:14:20)
6. "Yes, make sure to keep your tails clean, everyone. No one likes a dirty, stinky tail." (ASR GG20, 1:15:40)
7. "I require context." (ASR GG20, 1:17:36)

## Appearance Anchors (avatar)
- 153 cm. Pink eyes; two-tone light-and-dark brown hair in bunches with a tall ahoge poking out of her hood;
  sharp teeth; a bright orange hoodie decorated with fans whose X-shaped left eye blinks when she blinks;
  black cycle shorts and one striped black-and-orange knee sock. [Official GG1] [Observed GG2 §Appearance,
  secondary]
- In the lore her weapons are huge gauntlets ("Da Fister") and her bite. Orange is her color; her oshi mark
  is 👧. Later outfits: a 2025 New Year kimono, a 2026 Monster Hunter outfit Raora designed, a 2026 qipao
  outfit with a propeller hat she shares with Popo. [Observed GG2 §Lore, §History, secondary; X post GG6]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | A gremlin "Chaser" from Freesia, "born and raised under the flag of Freedom" | [Official GG1] |
| 2024-06-21 PDT | Debut ("GG STANDS FOR GIGI!"), second of Justice; official profile lists June 22 (JST) | [Official GG1] [Observed GG3] |
| 2024-09-21 | Sings "September" 120 times in an eight-hour unarchived karaoke | [Observed GG2, secondary] |
| 2024-12-14 | VTuber Awards: Most Chaotic VTuber | [Observed GG6] |
| 2025-08-02 | 3D debut (time zone to confirm) | [Observed GG2] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa | [Official GG5] |
| 2025-10-18 | First original song "I'll still be here" | [Observed GG2] |
| 2026-05 | CCGG 3D live with Cecilia; "CCGG MADNESS" MV (05-17) | [Official GG1] [Observed GG3] |
| 2026-06-25 | Original MV "enough" | [Observed GG3] |
| 2026-07-03/04 | Serendipity concert, unit with Cecilia | [Official GG4] |

## Relationship Map
Public exchanges only. Group-wide ties are on "hololive -Justice-"; pairs with every branch are on "Justice
Pairs."

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Cecilia Immergreen | Genmate; CCGG ("Autofister") | Official unit and song "CCGG MADNESS"; Cecilia calls her "idiot" and "FREAK," admires that she "doesn't easily get rattled"; Gigi: "She's good at getting stuff done." Met before debut | [Official GG4] [Observed GG2, GG3] |
| Raora Panthera | Genmate ("RPGG") | MapleStory, Monster Hunter Wilds, a food tier-list off-collab; Raora designed their matching 2026 Monster Hunter outfits | [Observed GG3; X post GG6] |
| Elizabeth Rose Bloodflame | Genmate ("Hot Pursuit") | Operation Tango ("i won't let Liz down!!!"); "DON'T TELL LIZ!" | [Observed GG2, GG3] |
| Mori Calliope | Senior ("Grem Reaper") | Mouthwashing, Fast Food Simulator, R.E.P.O., The Boba Teashop (2024–25); "MORI CALLIOPE!"; the League of Legends campaign; with Fuwawa, "2 Creatures + 1 Reaper" (2026) | [Observed GG2, GG3; X post GG6] |
| Ouro Kronii | Senior ("TimeChaser"; "Clockwork Orange" with Cecilia) | Fatal Fury (2025), Hytale (2026) | [Observed GG2, GG3] |
| Takanashi Kiara | Senior ("Ultra Orange"); calls her "GeeGee" | Reanimal (2026-04-03); Gigi decorated a page in the friendship journal Kiara brought to the 2026 fes.; "I know Kiara saved the world. Literally." (Hytale) | [Observed GG2, GG3] [ASR GG20, LgDuyqoaqT4 1:01:53, 1:16:19] |
| Watson Amelia | Affiliate senior ("ClueChaser") | In ENReco, Gigi's knight Gonathon married Ame's Jyonathan, a role-play storyline | [Observed GG2, secondary] |
| Shiori Novella, Koseki Bijou | Advent ("NovelGrem"; GAGA with Cecilia) | Eden Eternal, Heave Ho, Phasmophobia, Trine 5; the "Fanfic Club" with Pavolia Reine and Airani Iofi; a voice in Shiori's "Into The Void" | [Observed GG2, GG3] |
| Nerissa Ravencroft | Advent ("BeatDown," "SoundChaser") | The Planet Crafter (2024); "III" together at -All for One-; a joke child, Nerigi, at Gigi's 3D live | [Observed GG2, GG3] [Official GG5] |
| Mococo / FUWAMOCO | Advent ("GigiMoco," "bauBau") | With Cecilia, hijacked FUWAMOCO MORNING #167 as a prank | [Observed GG2; Mococo file] |
| Ceres Fauna, Nanashi Mumei | Promise alumnae ("FruitPunch"; "A Towl and a Gremlin") | The Coughing Baby Award Show; Echo Point Nova | [Observed GG2, GG3] |
| Nekomata Okayu | JP senior ("OkaGigi") | — | [Observed GG2, secondary] |

## Arc
- **Starting point:** active at the 2026 baseline: CCGG's 3D live and Serendipity, her original songs, Final
  Fantasy XIV and rhythm games.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a plan that "would be funny"; a bit repeated past its limit; an ambush on Mori
  Calliope; a keyboard-smash post.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Gigi promises a "short" stream and talks for forty minutes before the game.
  2. Cecilia leaves her alone in the Justice HQ for one hour.
  3. Calli finally agrees to one game of League; Gigi panics.
  4. Popo barks at the worst moment of a horror game.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
Her crude jokes are part of her voice; keep them as jokes, never explicit. The ENReco "marriage" with Ame's
character and the "child" Nerigi with Nerissa are role-play bits, not relationships.

## Hard Facts (continuity)
- Debut 2024-06-21 PDT (June 22 JST); birthday October 18; 153 cm; color orange; fans grems (lowercase);
  mascot Popo, a kakapo; "Most Chaotic VTuber" 2024.
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- GG1 Official profile: https://hololive.hololivepro.com/en/talents/gigi-murin/ (catch line "Huh? But it was
  funny! Don't get mad at me!", data, music list)
- GG2 Virtual YouTuber Wiki, Gigi Murin, read through its API on 2026-10-01 (secondary): §Profile,
  §Personality, §Appearance, §History, §Mascots and fans, §Relationships, §Quotes, §Lore, §Likes and dislikes,
  §Miscellaneous: https://virtualyoutuber.fandom.com/wiki/Gigi_Murin
- GG3 Stream archive metadata, Gigi's channel and collaborators', via archive.ragtag.moe (read 2026-10-01):
  15aufXwBIKw, Z77nzZc6UgU, YHWVU_lRpPM, VRVExNHW9Go, MxQd1uPFAuw, bTxEGwMOQQI, 3m15lUh0WP4, V5kX2lQQsJA,
  rkd3NPuq3KY, ZFtGoJATKGA, fXQzLPESCUk, LNbEaWp_UqE, YBxObHkYqgU, YSpAbEJlwFE, 1eNa9WzJXt8, G7oOm0pb7Vg,
  VfN4C_sledc, 4NEexj4-1EU, K2y9R_inuSc, mKRAtm2wXHk, VMqAdoSNkMo, 5f5uST1C7z4, RplRUa_21Ng, mo4XRT84Jo8,
  LgDuyqoaqT4.
- GG4 Official Serendipity interview, Gigi & Cecilia (2026-06-11): https://serendipity.hololivepro.com/news/interview06/
- GG5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- GG6 Gigi's X posts via wiki citations (research/x-posts.md): 1803261982189273111, 1803569516259242039,
  1812771542444466679, 1856512308346007707; VTuber Awards 1868088110363431075; Raora 2008340143938183214
- GG20 Claude's audio check (2026-10-01); see research/audio-check/gigi.md.

---

## [SW] Name
Gigi Murin

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Justice-, hololive English -Justice- (former branch name), Justice, CCGG

## [SW] Other Names
Gigi, GG, Gi Murin, G Pain, GeeGee, Da Fister, The Free-spirited Chaser

## [SW] Personality
Gigi streams as "The Free-spirited Chaser," a gremlin who follows her instincts toward whatever is fun and makes trouble because she "thought it would be funny" (her official line: "Huh? But it was funny! Don't get mad at me!"). She is loud, energetic, unpredictable and shameless, the "Most Chaotic VTuber" of 2024: she repeats bits until they land, campaigns for years (getting Mori Calliope to play League of Legends), makes crude jokes without meaning harm, and talks about "absolutely nothing for 20 minutes" before touching the game. She loves winning, MMORPGs, Final Fantasy XIV, rhythm games and story games, draws grems, and has a gentle, dutiful side under the noise: she reminds fans to "stay safe, stay hydrated," writes sentimental songs, and is fiercely loyal to Cecilia, her CCGG partner and straight woman, and to her grems.

## [SW] Background
Gigi is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Free-spirited Chaser," a mischievous gremlin from Freesia, "born and raised under the flag of Freedom," who chases targets on pure instinct, cannot remember directions, and joined Justice's mission to catch Advent mostly because it sounded fun. She debuted on 2024-06-21 (PDT) in hololive English -Justice-, won "Most Chaotic VTuber" at the 2024 VTuber Awards, made her 3D debut in August 2025, performed at the 2025 English concert (solo "Wonky Monkey," "MONSTER," "Countach," "III"), released original songs from 2025 ("I'll still be here," "enough"), and in 2026 formed the official unit CCGG with Cecilia Immergreen ("CCGG MADNESS," a 3D live, the Serendipity concert). Her color is orange; her fans are grems; her partner is Popo, a kakapo who barks.

## [SW] Physical Description
Gigi's avatar is 153 cm tall, with pink eyes, sharp teeth and two-tone light-and-dark brown hair in bunches, a tall ahoge sticking out of her hood. She wears a bright orange hoodie decorated with fans, whose X-shaped eye blinks when she blinks, black cycle shorts and a single striped orange-and-black knee sock. Her lore weapons are huge gauntlets. Popo, a small green kakapo with a propeller ahoge, is often with her.

## [SW] Dialogue Style
Loud, fast, run-on American English full of "like," "okay," "yeah," "sure," "hold on" and bursts of laughter; she talks to "grems," reads superchats with quick deadpan comebacks ("I require context."; "I'm sure that's true. I don't remember the context, but I'm sure it's true."), and turns anything into a bit: a blurred photo becomes a crime scene, bad luck an "Etsy witch" hex. She repeats a bit until it lands, begs in an escalating childish whine ("PPEEWEASEEEEE"), shouts "MORI CALLIOPE!" in full, swears casually now and then and makes crude jokes without malice, then says something sweet and plain ("Thanks for coming to see me! … stay hydrated"). Her philosophy: "If it works 51% of the time, that's enough." Style demo: "Hold on, hold on. Who did this? Was it me? It was funny though."

## [SW] Catchphrases
"Gi Murin!" (greeting); "Huh? But it was funny! Don't get mad at me!" (official line); "I require context." (a confusing superchat); "If it works 51% of the time, that's enough."; "I need validation."; "Boat goes binted!" (a meme she repeats); "MORI CALLIOPE!" (always the full name); "DON'T TELL LIZ!"; "What do you meaaaaaan?"; "Why?! WHY, WHY, WHY?!" (losing); "yippee!"; "Ouchi!"; "I'll be back tomorrow. You'll see me again." (sign-off); "grems" (her fans, lowercase)

## [SW] Voice & Delivery
A bright, energetic mid-high voice that is loud by default and jumps into whiny, mock-dramatic or shouting registers for bits, then drops flat for the punchline. Fast run-on chatter with self-interruptions ("hold on"), sudden loud laughs and sound effects ("BAM BAM BAM"), sing-song scatting when she is happy, and a soft, plain tone when she thanks people.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): bright, energetic mid-high voice; loud by default, quick deadpan for punchlines; American English. Default tags: [energetic, loud]. By situation: greeting [sing-song, loud]; superchat reading [chatty, quick] then [deadpan]; mock crime scene [grave, theatrical] then [laughs]; begging [whiny, escalating]; losing a game [outraged, shouting]; a bit that lands [cackling]; sincere thanks [soft, sincere]; sign-off [bright, quick]. With people (provisional, drawn from Relationships): Cecilia [teasing, clingy]; Mori Calliope [excited, shouting her full name]; Liz [guilty, conspiratorial]; Raora [playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [loud laugh] HAHA; [sound effect] BAM BAM BAM; [humming] (tag only); [whining] pleeease. Keep in the words: "like," "okay," "sure," "hold on," "grems," "I require context," "MORI CALLIOPE"; casual swearing now and then. Pronunciation guide (provisional, untested): Gigi /ˈdʒiːdʒiː/ (like "GG"), Murin /ˈmʊɹɪn/, grems /ɡɹɛmz/. Not as default: a quiet, demure voice; cruel teasing; anything sexual beyond a crude joke.

## [SW] Motivation
In her lore, Gigi is a Chaser who follows her instincts toward whatever is fun. As a streamer she wants to win, to make people laugh, and to keep her grems happy; she will put on a show "because it would be funny."

## [SW] Relationships
Cecilia Immergreen: her genmate and partner in the official unit CCGG ("CCGG MADNESS," a 2026 3D live, Serendipity); Cecilia calls her "idiot" and "FREAK" yet says she "doesn't easily get rattled and is very dependable," and Gigi says Cecilia is "good at getting stuff done"; they met before debut. Raora Panthera ("RPGG"): monster hunts and a food tier list; Raora designed their matching Monster Hunter outfits. Elizabeth Rose Bloodflame ("Hot Pursuit"): "i won't let Liz down!!!"; "DON'T TELL LIZ!" Mori Calliope ("Grem Reaper"): Gigi shouts her full name, has spent years trying to get her into League of Legends, and plays horror and job-simulator games with her; with Fuwawa they were "2 Creatures + 1 Reaper." Ouro Kronii: "TimeChaser," and "Clockwork Orange" with Cecilia. Takanashi Kiara: "Ultra Orange"; Gigi decorated a page in the friendship journal Kiara brought to the 2026 fes. Watson Amelia: in the ENReco story Gigi's knight Gonathon married Ame's Jyonathan ("ClueChaser"), a role-play bit. Shiori Novella ("NovelGrem") and Koseki Bijou: GAGA with Cecilia; the "Fanfic Club" with Shiori, Pavolia Reine and Airani Iofi. Nerissa Ravencroft ("BeatDown"): "III" together on stage and a joke child, Nerigi. Mococo ("GigiMoco"): with Cecilia she hijacked FUWAMOCO MORNING #167 as a prank. Ceres Fauna ("FruitPunch") and Nanashi Mumei ("A Towl and a Gremlin"). Nekomata Okayu: "OkaGigi."

## [SW] Secrets
(none)

---

## Open Questions
1. 3D debut date time zone (2025-08-02) to confirm.


==================== FILE: gigi.md ====================

# Audio check — Gigi Murin (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026. The 13 Sentinels window mixes in voiced game characters (its pitch and pace are
not hers alone) and no line from it is used. Remarks in the chat about a trip and a sponsored eSIM segment
are left out.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat30_2026 | [【SC KETCHUP】im thinkin about holodori](https://youtu.be/LgDuyqoaqT4) | [1:00:00–1:30:00](https://youtu.be/LgDuyqoaqT4?t=3600) | 23.8 | 3041 | 127.6 | 265 Hz | 185–406 Hz |
| open2026 | [【SC KETCHUP】im thinkin about holodori](https://youtu.be/LgDuyqoaqT4) | [0:00:00–0:15:00](https://youtu.be/LgDuyqoaqT4?t=0) | 5.0 | 577 | 114.9 | 267 Hz | 182–404 Hz |
| close2026 | [【RHYTHM HEAVEN GROOVE】sweating all over the A bu](https://youtu.be/RplRUa_21Ng) | [3:32:41–3:42:41](https://youtu.be/RplRUa_21Ng?t=12761) | 4.1 | 488 | 119.2 | 291 Hz | 149–443 Hz |
| game30_2026 | [【13 SENTINELS: AEGIS RIM】i have to eat my vegeta](https://youtu.be/mo4XRT84Jo8) | [1:00:00–1:30:00](https://youtu.be/mo4XRT84Jo8?t=3600) | 21.7 | 2139 | 98.8 | 233 Hz | 129–384 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Talks for a long time before the game (GG4) | **Consistent.** The SC KETCHUP stream opens with about 8 minutes of setup and merch talk. | [0:07:58](https://youtu.be/LgDuyqoaqT4?t=478) |
| Turns things into bits (GG2) | **Confirmed.** A blurred merch photo becomes a crime scene; bad luck becomes an "Etsy witch" hex. | [0:13:46](https://youtu.be/LgDuyqoaqT4?t=826); [0:14:20](https://youtu.be/LgDuyqoaqT4?t=860) |
| Quick deadpan in superchats | **Confirmed.** "I require context." (twice); "I'm sure that's true. I don't remember the context, but I'm sure it's true." | [1:03:16](https://youtu.be/LgDuyqoaqT4?t=3796); [1:01:24](https://youtu.be/LgDuyqoaqT4?t=3684) |
| Crude jokes and casual swearing (GG2) | **Consistent.** "hell" and "shit" appear in passing (first model); no slurs. | throughout |
| Ties with Kiara (Ultra Orange) | **Confirmed (new detail).** "I know Kiara saved the world. Literally." (Hytale); she decorated a friendship-journal entry Kiara brought to fes. | [1:01:53](https://youtu.be/LgDuyqoaqT4?t=3713); [1:16:19](https://youtu.be/LgDuyqoaqT4?t=4579) |
| Pitch | **Measured:** chat window medians about 265–267 Hz, p10–p90 about 182–406 Hz. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Sound effects and scatting: "BAM BAM BAM BAM", "Talalalalala". [1:06:53](https://youtu.be/LgDuyqoaqT4?t=4013)
- "Thank you … for the Super. I need validation." [1:00:17](https://youtu.be/LgDuyqoaqT4?t=3617)
- A Hytale "wedding" bit with Kiara proposed by chat ("we need to have a Hytale wedding"), a performed joke. [1:03:58](https://youtu.be/LgDuyqoaqT4?t=3838)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "We're still trying to find the killer so the victim has been, their face has been blurred out of consideration for their family." | [0:13:46](https://youtu.be/LgDuyqoaqT4?t=826) | "is We're chill. We're still trying to find the the killer So the victim has been Their face has been blurred out of consideration for their family But someone" | Agrees |
| "I feel like someone hired an Etsy witch to curse me and to hex me" | [0:14:20](https://youtu.be/LgDuyqoaqT4?t=860) | "feel like um i feel like someone hired an etsy witch to curse me and to hex me so i'm gonna" | Agrees |
| "I need validation." | [1:00:21](https://youtu.be/LgDuyqoaqT4?t=3621) | "for the Supa. I need validation. Does anyone remember" | Agrees |
| "If it works, 51% of the time, that's enough." | [1:00:35](https://youtu.be/LgDuyqoaqT4?t=3635) | "you ask that. If it works 51% of the time, that's enough. Yeah, if you" | Agrees |
| "I'm sure that's true. I don't remember the context, but I'm sure it's true." | [1:01:24](https://youtu.be/LgDuyqoaqT4?t=3684) | "because she's wild I'm sure that's true. I don't remember the context and I'm sure it's true Thank you pip" | Agrees ("and I'm sure it's true" in the second model; the sentence is used) |
| "I know Kiara saved the world. Literally." | [1:01:53](https://youtu.be/LgDuyqoaqT4?t=3713) | "content updates ASAP. I know Kiara saved the world, literally, she saved my" | Agrees |
| "i require context what was the context" | [1:03:19](https://youtu.be/LgDuyqoaqT4?t=3799) | "probably enjoy it. I require context. What was the context? Maybe I would." | Agrees |
| "Yes, make sure to keep your tails clean, everyone. No one likes a dirty, stinky tail." | [1:15:40](https://youtu.be/LgDuyqoaqT4?t=4540) | "my tail! Weeee! Yes, make sure to keep your tails clean, everyone. No one likes a dirty, stinky tail. And your tail" | Agrees |
| "I require context." | [1:17:36](https://youtu.be/LgDuyqoaqT4?t=4656) | "in your bra? I require context. Thank you, Nishizomi," | Agrees |
| "Thanks grems for hanging out" | [3:41:11](https://youtu.be/RplRUa_21Ng?t=13271) | "a good time! Thanks, Grams, for hanging out. I will see" | **Name differs** ("Thanks, Grams" / "Thanks Squams"); only "…for hanging out" is quoted |
| "I'll be back tomorrow. You'll see me again." | [3:41:18](https://youtu.be/RplRUa_21Ng?t=13278) | "see you guys tomorrow I'll be back tomorrow. You'll see me again. I will" | Agrees |
| "Okay guys, chill, chill, chill, chill." | [1:00:39](https://youtu.be/mo4XRT84Jo8?t=3639) | "yourself so hard Okay, guys chill chill chill chill My turn now," | Agrees, but the window mixes in voiced game characters; **not used** |
| "Good job everyone, why are you taking so much damage?" | [1:07:35](https://youtu.be/mo4XRT84Jo8?t=4055) | "We made it. Good job everyone. Why do you take so much damage? The fight is" | Close ("Why do you take so much damage?"); game window, **not used** |
| "Oh my vegetables! My vegetables!" | [1:08:02](https://youtu.be/mo4XRT84Jo8?t=4082) | "that one. No! My big rules! Oh! My big rules! Where" | **Disagrees** ("My big rules!"); not used |
| "Can you please sing for us while we have- please, please, please!" | [1:14:24](https://youtu.be/mo4XRT84Jo8?t=4464) | "to worry about can you can you please sing for us while we have please please please bard" | Agrees, but likely a game character's line; **not used** |


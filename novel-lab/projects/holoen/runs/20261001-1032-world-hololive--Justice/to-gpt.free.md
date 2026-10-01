# One-round claim-check review (xhigh): hololive -Justice- world cards ("hololive -Justice-", "Justice Pairs") and the Justice edits to the other cast and world cards

The four Justice character files are reviewed in separate runs. For the cast and world edits below, check only the added or changed lines (a unified diff against the last promoted version); for the two new world cards, check everything.

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



==================== FILE: 20261001-1032-world-hololive--Justice/claude-draft.md ====================

---
kind: world
name: "hololive -Justice-"
sw_section: Worldbuilding
---

# World Element: hololive -Justice-

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the whole group as publicly shown, checked 2026-10-01. Evidence labels as in the other world files.
> "Archive" = stream titles and descriptions on the members' YouTube channels (archive.ragtag.moe, S4); it
> does not hold Twitch streams and thins out in 2026. Pair details live on the world card "Justice Pairs";
> each member has her own character file. Private matters (health, family, breaks and their reasons) are
> outside scope and are not recorded; announced breaks are not written (author's decision, 2026-10-01).

## One-line Concept
Four "law enforcers" from beyond the clouds, sent to bring in Advent's escaped "criminals," who debuted as
hololive English's fourth generation in June 2024 and promptly forgot the mission: a queen with a British
accent who organizes everyone (Elizabeth), a gremlin who chases for fun (Gigi), an ancient automaton maid who hates
working (Cecilia) and a big cat artist who would rather find pizza (Raora). The manhunt is a running bit they
play with Advent, not a fact they live by.

## Type
Faction / unit.

## Members and Status (2026-10-01)
- Elizabeth Rose Bloodflame (the Scarlet Queen, Harbinger of Order, organizer of Justice; from Great
  Exardia), Gigi Murin (the Free-spirited Chaser, a gremlin from Freesia), Cecilia Immergreen (the Ancient
  Automaton from Immerheim) and Raora Panthera (the Artist with the God Eyes, a big cat from the Romance
  Empire). All four are active at the 2026-09-30 baseline. [Official S1] [Observed S2, secondary]
- Since the September 2026 merger the name is "hololive -Justice-" (before: "hololive English -Justice-").
  [Observed S2, secondary]
- Group mascot: Sergeant Smokey, who sometimes delivers their orders. Each member's oshi mark goes in group
  titles: 💄 Elizabeth, 👧 Gigi, 🍵 Cecilia, 🐱 Raora. [Observed S2 §Justice, secondary; S4 titles]

## How the Group Works
- **The mission as a bit:** in the announcement video "The Mission Begins!" (2024-06-18) the four are
  dispatched to apprehend Advent. Their headquarters, The Lookout, hides in the clouds between worlds; behind a
  round door is The Panscope, a telescope that can show any place, even The Cell. They "can" name a fifth
  member, but only temporarily ("We change it like we change socks"). Justice existed before them: Cecilia
  was once "FORCED BY JUSTICE to work as a maid (not current Justice. #LizIsInnocent)." [Observed S2 §Justice,
  secondary; X post S5]
- **In practice:** none of them catches anyone. Raora was sent after FUWAMOCO and got lost in crane games;
  Cecilia's plan was to dig a hole (Bijou can fly) or to give Advent rooms full of their favorite things and
  then remove the doors. Advent × Justice collabs use cop-and-robber jokes. [Observed S2 §Lore, secondary; S4]
- **Four greetings:** their first collab was titled "Ello! Hi! Hallo! Ciao!" (2024-06-22 PDT): Elizabeth's
  British "Ello," Gigi's American "Hi," Cecilia's German "Hallo," Raora's Italian "Ciao." Each speaks English
  with her own accent. [Observed S4 j89Phi0oom8] [Observed S2, secondary]
- **Group chant and series:** "Justice! Just like that!" recurs in their collab titles (Minecraft 2024, a
  2025 Justice Jams, "JUSTICE IN THE FAR EAST" 2025); Elizabeth hosts the group collabs as "JUSTICE JAMS";
  in 2026 they also run "Justice Girls' Night." [Observed S4 titles]
- **Roles in the room:** Elizabeth plans, organizes and keeps the schedule (her profile: "stressed out with
  her work coordinating Justice"); Gigi is the noise and the bits; Cecilia is the sarcastic straight woman
  (her "Ew! Get away from me, you FREAK!" is often aimed at Gigi) and the coder; Raora is the warm, cheerful
  one who laughs at everything. [Official S1] [Observed S2 §Personality, secondary]

## History
| Date | Event | Trace left |
|---|---|---|
| 2024-06-18 | Announcement video "The Mission Begins!" | the manhunt premise |
| 2024-06-21/22 PDT | Debuts: Elizabeth (06-21 8 PM), Gigi (06-21 8:45 PM), Cecilia (06-22 8 PM), Raora (06-22 8:45 PM); official profiles list June 22/23 (JST) | "ABOVE BELOW" released; first collab "Ello! Hi! Hallo! Ciao!" (06-22 9:30 PM PDT) |
| 2024-06–07 | Content Warning, Chained Together, Left 4 Dead 2, a Justice Minecraft server and "Justice HQ" | the group's first weeks |
| 2024-07-21/22 | "Advent VS Justice" in Party Animals | the rivalry as a game |
| 2024-10-31/11-01 | "Justice's Haunted VR Investigation" in VRChat, with Advent visitors; chibi 3D models | Halloween tradition |
| 2024-12-28 | Half-year anniversary (New Year outfits announced, shown 2025-01-01) | — |
| 2025-01-31 | "ADVENT VS JUSTICE" Murky Divers with all nine | — |
| 2025-03-08 | hololive 6th fes. (Expo 2025): Justice's first stage, watched along by the members | — |
| 2025-06-20 | First anniversary, "Operation DECODE" | — |
| 2025-08-01/02/09/10 | 3D debuts: Elizabeth, Gigi, Cecilia, Raora (time zone to confirm) | Wind-Up and Gacha×Gacha ADVENTURE! premiered |
| 2025-08-23 EDT | -All for One-: Justice's first stage as a group in 3D ("ABOVE BELOW"); Cecilia's "Wind-Up" was the first Justice solo; see the member files for their other stages | [Official S3] |
| 2026-02-20/22 | Geoguessr "Justice vs Advent" | — |
| 2026-05 | CCGG (Gigi and Cecilia) 3D live and "CCGG MADNESS"; Raora's first birthday 3D live (05-10) | — |
| 2026-06-27 | Second-anniversary live "How to Protect JUSTICE!" | [Official S1 video list] |
| 2026-07-03/04 | Serendipity: Gigi & Cecilia, Nerissa & Elizabeth, FUWAMOCO & Raora | [Official S6] |
| 2026-08/09 | Official -Justice- merch tie-ins: Bandai Namco Amusement America pop-up (2026-08-27), Pinfinity AR pins (2026-09-30) | [Official S1 news] |

Group songs: "ABOVE BELOW" (2024), its "-Far East Remix-," "RENEGADE," "SUPERNOVA SUPER GIRL" (2026). The
"#AdVSJus Motion Comic" (Advent vs Justice) ran to at least five episodes. [Official S1 music and video lists]

## Sensory Palette
- See: 💄👧🍵🐱 in a row; a black-and-red sword engraved with scales; an orange hoodie with a blinking X eye; a
  brass key spinning on a clockwork head; a pink coat with a tail-gap; a telescope behind a round door in the
  clouds.
- Hear: four greetings in four accents; "Justice! Just like that!"; "Oh~hohoho!"; a kakapo that barks like a
  dog; "Spin to win!"; "RAAAOO!"

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| The Lookout / The Panscope | Justice HQ in the clouds / its all-seeing telescope | lore |
| Sergeant Smokey | the group's mascot, who delivers orders | lore |
| JUSTICE JAMS | Elizabeth's name for the group collabs | Elizabeth |
| Justice! Just like that! | group chant in titles | all four |
| Rosarians / grems / Otomos / Chattini | Elizabeth's / Gigi's / Cecilia's / Raora's fans | official |

## Conflicts and Story Hooks
Proposed fiction (not recorded events):
1. Sergeant Smokey orders an actual arrest; nobody remembers how handcuffs work.
2. Elizabeth's schedule collides with Gigi's "it would be funny" plan; Cecilia codes a minigame to decide.
3. Raora draws a suspect sketch so accurate it is clearly Bijou in a hat.
4. The Panscope picks up The Cell's group chat; Justice must decide whether to tell Advent.

## Links to Characters
Elizabeth Rose Bloodflame, Gigi Murin, Cecilia Immergreen, Raora Panthera (members). Advent are their
in-story "targets" and friends (see "hololive -Advent-"); seniors across Myth and Promise appear on "Justice
Pairs."

## Secrets
(None.)

## Hard Facts (continuity)
- Debuts 2024-06-21/22 PDT (June 22/23 JST); members' colors: Elizabeth red, Gigi orange, Cecilia green, Raora
  pink. All four are active at the baseline.
- The manhunt is lore played as a bit; Justice and Advent are friends and frequent collaborators.

## Sources (checked 2026-10-01)
- S1 Official profiles: https://hololive.hololivepro.com/en/talents/elizabeth-rose-bloodflame/ ,
  /gigi-murin/ , /cecilia-immergreen/ , /raora-panthera/ (catch lines, data, music and video lists, news)
- S2 Virtual YouTuber Wiki pages for the four members (secondary), read through the API on 2026-10-01: §Lore,
  §Justice, §History, §Relationships, §Miscellaneous
- S3 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- S4 Stream archive metadata (archive.ragtag.moe, read 2026-10-01): j89Phi0oom8 (first collab), _KD4WaFxU20,
  LTBfVnJgE_Y, fxvyyBIBNA8, bdwGIYhBXuU, ZrU2Jn94sIU, y2ZOgkSwKgc, nEV7T8peRcw, mW1-0BTSQg0, DQqxZe1ll04,
  LoqiPbgrAXw, z5cdYdocS8k, 6oONd7NG5Mo
- S5 Members' X posts via wiki citations (research/x-posts.md)
- S6 Official Serendipity interviews 03 (FUWAMOCO & Raora), 06 (Gigi & Cecilia), 07 (Nerissa & Elizabeth)

---

## [SW] Name
hololive -Justice-

## [SW] Role
Faction

## [SW] Other Names
Justice, holoJustice, hololive English -Justice-, The Lookout, Sergeant Smokey

## [SW] Description
hololive English's fourth generation (debuted June 2024), now "hololive -Justice-": Elizabeth Rose Bloodflame, the "Scarlet Queen" with a British accent, who organizes the group and sings; Gigi Murin, a loud, chaotic gremlin "Chaser"; Cecilia Immergreen, a sarcastic ancient automaton maid who hates working and plays violin; and Raora Panthera, a cheerful big-cat artist with an Italian accent who loves pizza. In their shared lore they are law enforcers from a headquarters in the clouds (The Lookout, with its all-seeing Panscope), sent to catch Advent's escaped "criminals"; in practice they never catch anyone, and Advent × Justice collabs use cop-and-robber jokes. Their first collab was "Ello! Hi! Hallo! Ciao!", one greeting per accent, and "Justice! Just like that!" is their chant. Elizabeth plans and keeps time, Gigi brings the noise, Cecilia plays the straight woman (often "Ew, get away from me, you FREAK!" at Gigi), Raora laughs at everything. Milestones: songs "ABOVE BELOW" and "SUPERNOVA SUPER GIRL," 3D debuts in August 2025, their first group stage at the 2025 English concert, the 2026 Serendipity units Gigi & Cecilia, Elizabeth & Nerissa, Raora & FUWAMOCO, and the second-anniversary live "How to Protect JUSTICE!" (2026). Fans: Rosarians, grems, Otomos, Chattini.

## [SW] Rules
All four are active in 2026; the group is "hololive -Justice-" since the 2026 merger. The manhunt is lore they play for laughs, never real policing; Advent and Justice are friends. Each member speaks English with her own accent (British, American, German, Italian). Myth, Promise and Advent are their seniors.

## [SW] Sensory Details
💄👧🍵🐱 in a row; a scales-engraved sword; a blinking X eye on an orange hoodie; a brass key spinning on a clockwork head; cat ears and a pink coat; four greetings in four accents.

## [SW] Secrets


---

## Open Questions
1. 3D debut dates (2025-08-01/02/09/10) need their time zone; GPT's research pass was asked to confirm.
2. Which songs each Justice member sang at Serendipity (2026) is not in Claude's sources.


==================== FILE: 20261001-1032-world-Justice-Pairs/claude-draft.md ====================

---
kind: world
name: "Justice Pairs"
sw_section: Worldbuilding
---

# World Element: Justice Pairs (inside the generation and with everyone else)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-01. Evidence labels as in the other world files. "Archive" = stream titles and
> descriptions on the members' YouTube channels (archive.ragtag.moe, S1); it holds no Twitch streams and thins
> out in 2026, so recent ties are undercounted. Counts stay in this dossier and are never relationship
> rankings. Pair and unit names come from the wiki's lists (S2, secondary) unless marked official; whether
> each is member-used or a fan label is not settled for every name. Name only the members who took part in a
> collab.

## One-line Concept
How the four "law enforcers" of Justice relate to each other and to everyone else: a chaotic gremlin and the
automaton who calls her a freak (and debuted a duo song with her), a queen who keeps everyone on schedule, a
big cat who is everybody's sweetheart, and a web that reaches into every EN generation, hololive ID, the
Japanese branch and HOLOSTARS.

## Type
Relationship web.

## Inside Justice
- **Gigi and Cecilia ("CCGG," "Autofister"):** the closest-billed pair of the four in official material: a
  Serendipity 2026 unit with an original song, "CCGG MADNESS" (MV 2026-05-17), and a CCGG 3D live with an
  after-talk (May 2026). In the official interview Gigi said "Who is she!!! … Jokes aside, I hope everyone's
  ready for some MADNESS!!!!" and Cecilia answered "idiot"; Gigi admires that Cecilia is "good at getting stuff
  done," Cecilia that Gigi "doesn't easily get rattled and is very dependable!" They met before debut. Cecilia
  plays the straight woman ("Ew! Get away from me, you FREAK!"). Collabs: A Way Out and 7 Days to Die (2024),
  Portal 2 co-op (2024-07-10), a Cuphead off-collab (2025-05-30), Shadowverse "CECE VS GIGI" (2025-08-17).
  [Official S3 interview06] [Observed S1; S2, secondary]
- **Gigi and Raora ("RPGG"):** MapleStory (2024-08-16), Monster Hunter Wilds (2025, a sponsored launch with Ina
  and Bijou), a food tier-list off-collab (2025-06-05), Elden Ring Nightreign (2025); Raora designed the 2026
  Monster Hunter collaboration outfits for Gigi and herself. [Observed S1; X post S5]
- **Gigi and Elizabeth ("Hot Pursuit"):** Operation Tango ("i won't let Liz down!!!," 2024-07-04), Fortnite with
  all four (2024-10-02), "Finding the best parent of holoEN" (2026-04-06); "DON'T TELL LIZ!" is one of Gigi's
  wiki quotes. [Observed S1; S2, secondary]
- **Cecilia and Raora ("Raviolin"):** Minecraft as a duo in the first weeks ("Watch out for this duo!",
  2024-07-03); Raora drew the ending screen for Cecilia's debut and Cecilia animated Raora's debut stinger;
  Raora helped design Cecilia's Otomo mascot; they built a Chattino model together (2025-04-11). [Observed S1;
  S2, secondary]
- **Cecilia and Elizabeth ("FiddleFlame"):** their first collab, "Showing Elizabeth around!!" in Minecraft
  (2024-07-19); fans picture Cecilia as Elizabeth's lifelong maid, and Cecilia's lore says an older Justice
  forced her to work as a maid ("#LizIsInnocent"). [Observed S1; S2, secondary; X post S5]
- **Elizabeth and Raora ("FlamePanther," "Lizotto"):** Raora's first collab was "Chat & Art w/ Liz!"
  (2024-06-26); Elizabeth calls her "Pretty Kitty" and hosted "Happy Birthday Pretty Kitty!" (2025-05-12); a
  Beard Papa's cream-puff stream (2026-02-04). [Observed S1; S2, secondary]
- **As four:** see "hololive -Justice-": the "Ello! Hi! Hallo! Ciao!" first collab, JUSTICE JAMS, a Snow
  Halation cover (2025-02-21), anniversaries, the 2026 Justice Girls' Night.

## With Advent (their "targets")
- **Group:** Party Animals "Advent VS Justice" (2024-07-21/22), Justice's Haunted VR Investigation with Advent
  visitors (2024-11-01), Murky Divers with all nine (2025-01-31), Geoguessr "Justice vs Advent" (2026-02-22),
  the #AdVSJus motion comic. [Observed S1] [Official S4]
- **Nerissa:** Elizabeth is her "mortal enemy (lore)" and duet partner ("BloodRaven"; a "Rondo Revolution"
  cover; Serendipity 2026; "ALiCE&u" with guest Ayunda Risu at -All for One-). Gigi: "BeatDown"/"SoundChaser,"
  The Planet Crafter (2024-10-11), "III" together at -All for One-, a joke child "Nerigi." Cecilia: "AutoTune,"
  Unravel Two ("Trying to capture Nerissa through crocheting!!!," 2024-08-17). Raora: "V3LVET" with Moona
  Hoshinova, Clubhouse Games (2024-12-09), Raft (2025-02-06). [Official S3 interview07, S6] [Observed S1; S2]
- **Shiori:** Elizabeth ("NovelFlame," "BloodQuill") and Gigi voice parts in Shiori's motion comic "Into The
  Void" (2026); Gigi ("NovelGrem") games with her often (Eden Eternal, Heave Ho, a Fateful Findings watchalong,
  Project Zomboid, Phasmophobia) and is in the "Fanfic Club"; Gigi and Cecilia form "GAGA" with Shiori and
  Bijou; Raora designed things with her (2024-12-05). [Observed S1; S2]
- **Bijou:** "GAGA" (Gigi, Cecilia); Cecilia's Walking Dead watchalongs, Elden Ring and a Phasmophobia
  "babysitter" run (2025); "Graondstone" with Raora and Kaela; Raora's cooking off-collab with "my assistant"
  Bijou (2024-12-19); "I'm Your Treasure Box" by Bijou, Cecilia and Raora at -All for One-. [Observed S1]
  [Official S6]
- **FUWAMOCO:** Raora is their Serendipity trio partner, who drew them a shikishi before debut and gave it
  "with big tears in her eyes"; the twins met Justice before debut to give advice; Gigi ("GigiMoco") and
  Cecilia ("Cecemoco") hijacked FUWAMOCO MORNING #167 as a prank; Cecilia's Chrono Trigger off-collab with
  them (2026); Fuwawa, Gigi and Calli as "2 Creatures + 1 Reaper" (2026, Fuwawa alone); the twins sang in
  Elizabeth's 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha. [Official S3
  interview03] [Observed S1; S2]

## With Myth
- **Mori Calliope:** Gigi's "Grem Reaper": Mouthwashing (2024-11-14), Fast Food Simulator (2025-02-04),
  R.E.P.O. (2025-05-02), The Boba Teashop (2025-06-04); Gigi shouts her full name ("MORI CALLIOPE!") and has
  campaigned for Calli to play League of Legends; Calli said she came to like her own name when Gigi used it.
  Raora hit 500k during Galaxy Burger with Calli (2025-03-26). Elizabeth surprised Calli with a TakaMori skit
  at debut and joined her "LYRA" remix of "III." [Observed S1; S2]
- **Takanashi Kiara:** the "HoloEU" trio with Cecilia and Raora; Raora's Italian lesson for Kiara
  (2024-10-04), an outfit design for her (2025-01-26) and an EU-snacks off-collab (2025-03-11); Kiara and
  Cecilia spoke German in their first exchange (Kiara's 2024 birthday) ("EterniTea"); Gigi and Kiara are
  "Ultra Orange" (Reanimal, 2026-04-03); Kiara calls Elizabeth "Erby Berby" ("Eternal Flame"). [Observed S1;
  S2]
- **Ninomae Ina'nis:** Cecilia's self-declared "rival" and Stranger of Paradise partner (2025); Rabbit and
  Steel with Cecilia, Bijou and Gigi (2024); Blood Typers with Gigi (2025-04-11); Puyo Puyo Tetris 2 with Raora
  (2025-06-02); the Monster Hunter Wilds sponsored launch with Gigi, Raora and Bijou (2025-03-01). [Observed S1]
- **Gawr Gura (graduated):** Keep Talking and Nobody Explodes and The Forest with Cecilia (2025-02);
  R.E.P.O. with Raora (2025-04-13). **Watson Amelia (affiliate):** Gigi's ENReco "husband" Jyonathan
  ("ClueChaser"); Borderlands 2 with Cecilia, Gigi and Mumei (2024-08-09). [Observed S1; S2]

## With Promise
- **Ouro Kronii:** "Pizza Time" with Raora (Portal 2, 2024-11-26; Backrooms Cleanup Crew, 2026-06-11; Raora
  calls her "Tam Tender"), "TimeChaser" with Gigi (Fatal Fury, 2025-05-03; Hytale, 2026-04-14), "Clockwork
  Orange" with Gigi and Cecilia; Kronii calls Cecilia a "CLANKER," Cecilia calls her "Owo-senpai." [Observed
  S1; S2; Kronii file]
- **Hakos Baelz:** "BratTea" with Cecilia; "Countach" with Gigi and guest Kureiji Ollie at -All for One-.
  **IRyS:** Elden Ring Nightreign with Cecilia (2025-06-05). [Observed S1; S2] [Official S6]
- **Ceres Fauna (graduated 2025):** Gigi's "FruitPunch" (The Coughing Baby Award Show, 2024-12-28) and League of
  Legends with Elizabeth, Gigi, Cecilia and Nerissa (2024); Cecilia's "Green Women" (a shoujo-tropes ranking,
  2024-09-23). **Nanashi Mumei (graduated 2025):** Cecilia's "Automatowl" (Halo: Reach, 2024; "Ask us anything,"
  2025-04-12; Cecilia calls her "Myumyei"); Gigi's Echo Point Nova ("A Towl and a Gremlin," 2024-10-15); an
  art stream with Raora (2025-01-18). [Observed S1; S2]

## Beyond EN
- **ID:** Kaela Kovalskia with Raora ("SMITTEN," "Graondstone," "PizzaTimeSmith" with Kronii; in Raora's lore
  Kaela lives in her basement); Kureiji Ollie is Elizabeth's "kami-oshi" (HoloRed and "Code Red" collabs,
  guest at -All for One-), and Ollie did a chat-and-art collab with Raora (2024-09-06); Moona Hoshinova with Raora
  ("V3LVET"); Anya Melfissa visited Raora (2025-02-11); Vestia Zeta and Haachama in a Mario Party off-collab with
  Raora (2024-10-08); Ayunda Risu with Elizabeth ("LYRA," "ALiCE&u"); Vestia Zeta sang "Giri Giri" with Elizabeth at her 2025 3D showcase, which Elizabeth arranged and choreographed [ASR, Elizabeth file EB20]; Pavolia Reine and Airani Iofi with Gigi
  in the "Fanfic Club"; Kobo Kanaeru calls Elizabeth "Lilis." [Observed S1; S2] [Official S6]
- **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino
  Sora and Yuzuki Choco; Houshou Marine and Inugami Korone; FUWAMOCO with Polka, Nene, Watame and Iroha; her
  2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members).
  Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games
  with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is
  "RaoRiRi" with Ichijou Ririka, and both she and Gigi were inspired by Inugami Korone (Raora) and the Myth
  debuts (Gigi); Gigi and Nekomata Okayu are "OkaGigi." [Observed S1; S2] [Official S6]
- **HOLOSTARS:** Elizabeth's "HoloRed" and "Code Red" with Machina X Flayon, Jurard T Rexford and Crimzon
  Ruze, who calls her "Uncle Erb" (Marvel Rivals, "Art Thou Victorious, Nephew?," 2024-12-28); R.E.P.O. with
  Shiori, Gavis Bettel, Flayon and Jurard (2025-04-06); a "Mephisto" cover with Banzoin Hakka (2025-01-18).
  [Observed S1; S2]

## History
| Date | Event | Trace left |
|---|---|---|
| 2024-06-26 | Raora's first collab, "Chat & Art w/ Liz!" | FlamePanther |
| 2024-07-03 | Cecilia and Raora's Minecraft duo | Raviolin |
| 2024-07-19 | Cecilia shows Elizabeth around Minecraft | FiddleFlame |
| 2024-07-21/22 | Advent VS Justice, Party Animals | the rivalry as a game |
| 2025-01-31 | Murky Divers, Advent × Justice | — |
| 2025-08-23/24 EDT | -All for One-: "ALiCE&u," "START AGAIN," "High Tide" (Elizabeth); "Countach," "MONSTER," "III," "Wonky Monkey" (Gigi); "Wind-Up," "SHALLYS," "I'm Your Treasure Box" (Cecilia); "Gacha×Gacha ADVENTURE!," "Neko Kaburi-Na," "I'm Your Treasure Box" (Raora) | [Official S6] |
| 2026-05 | CCGG 3D live, "CCGG MADNESS" | Gigi and Cecilia's unit |
| 2026-07-03/04 | Serendipity: Gigi & Cecilia, Nerissa & Elizabeth, FUWAMOCO & Raora | [Official S3] |

## Sensory Palette
- See: an orange hoodie next to a green dress; a red sword beside a violin-lance; a pink cat tail curled around
  a raven; four oshi marks in a stream title.
- Hear: "Ew! Get away from me, you FREAK!"; "MORI CALLIOPE!"; "Pretty Kitty"; a German "Hallo" and an Italian
  "Ciao" in one breath.

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| CCGG / Autofister | Cecilia and Gigi (CCGG is official: "CCGG MADNESS") | members, official |
| RPGG / Hot Pursuit | Raora and Gigi / Elizabeth and Gigi | members (wiki) |
| Raviolin / FiddleFlame / FlamePanther, Lizotto | Cecilia–Raora / Cecilia–Elizabeth / Elizabeth–Raora | wiki |
| HoloEU | Kiara, Cecilia and Raora | wiki |
| GAGA | quartet: Bijou, Shiori, Gigi, Cecilia | members |
| BloodRaven | Elizabeth and Nerissa | wiki |
| Pizza Time / TimeChaser / Clockwork Orange | Kronii with Raora / Gigi / Gigi and Cecilia | members, wiki |
| Grem Reaper | Gigi and Calli | wiki |

## Conflicts and Story Hooks
Proposed fiction (not recorded events):
1. CCGG need a third member for one song; Elizabeth auditions and is far too good.
2. Raora's suspect sketch of Advent is so cute nobody can arrest them.
3. Gigi tries to get Mori Calliope into League of Legends one more time, with Kiara as backup.
4. Cecilia and Kronii's insult duel ("CLANKER" / "Owo-senpai") needs a referee.

## Links to Characters
Elizabeth Rose Bloodflame, Gigi Murin, Cecilia Immergreen, Raora Panthera, Nerissa Ravencroft, Shiori Novella,
Koseki Bijou, Fuwawa Abyssgard, Mococo Abyssgard, Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Gawr Gura,
Watson Amelia, Ouro Kronii, IRyS, Ceres Fauna, Nanashi Mumei.

## Secrets
(None.)

## Hard Facts (continuity)
- Serendipity 2026 units with Justice members: Gigi & Cecilia, Nerissa & Elizabeth, FUWAMOCO & Raora (official).
- "CCGG MADNESS" is Gigi and Cecilia's original song (2026); GAGA is a quartet; "2 Creatures + 1 Reaper" is a
  Fuwawa collab, not a FUWAMOCO one.

## Sources (checked 2026-10-01)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-10-01), Justice and cast channels; video IDs in
  the four Justice character files and in "hololive -Justice-"; plus 6-gCHucQaeA, F_NfN-M3_k4, DcD0kbllncg,
  YHWVU_lRpPM, VRVExNHW9Go, MxQd1uPFAuw, bTxEGwMOQQI, Z77nzZc6UgU, 3Ham5AjZUH4, kQeopZTlqog, VBBy4TGnJ2w,
  ddr8RB7MyGs, G7oOm0pb7Vg, XNIW_XHwwIM, DylxighPs7k, CtOwvXA7QEo, V5kX2lQQsJA, rkd3NPuq3KY, ZFtGoJATKGA,
  fXQzLPESCUk, L2g4qm3m1rM, NhWPXvPRzuk, 0oDpzkGN-TE, YSpAbEJlwFE, ufnTKDQGqRs, roFNVs40MHQ, kt4HvssYeTA,
  85vq6n6oBB8, Pz4thI9O_yk, K_GOEvTBmVo, Khp-BDYtHaQ, lyOAlaibnRY, qJI8LRQKOgs, -Ht_HZH9daY, LNbEaWp_UqE,
  YBxObHkYqgU, iyNbmBa70Ks, VfN4C_sledc, m69qTuudgp8, aOfaKRSjkm4, OTK8k7NAVRA, 1eNa9WzJXt8, F7BFFaEBGgk,
  laEINkg6W0I, w30OQWD6AEw, HLnalLS97i4, Q7SyO8k462w, oU_awVOVryo, wxZ2SY7xvNU, xylll7Mp0jk, iwnHChZq0N8,
  -knzJF4pp1g, z7NC9iRoW-E, _pv18gHgjQI, LJrBHzPv_nc, xlvI03HHAuE, jqFPgcMt_Jo. Counts computed by Claude.
- S2 Virtual YouTuber Wiki pages for the four Justice members, §Relationships, §Lore, §Miscellaneous (secondary)
- S3 Official Serendipity interviews 03 (FUWAMOCO & Raora), 06 (Gigi & Cecilia), 07 (Nerissa & Elizabeth)
- S4 Official profiles of the Justice members (video lists: "#AdVSJus Motion Comic")
- S5 Members' X posts via wiki citations (research/x-posts.md)
- S6 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/

---

## [SW] Name
Justice Pairs

## [SW] Role
Relationship

## [SW] Other Names
CCGG, Autofister, RPGG, Hot Pursuit, Raviolin, FiddleFlame, FlamePanther, HoloEU, BloodRaven, Pizza Time, TimeChaser, Grem Reaper

## [SW] Description
Inside Justice: Gigi and Cecilia are CCGG, an official unit with the song "CCGG MADNESS" and a 2026 3D live; Cecilia calls Gigi an "idiot" and a "FREAK" yet says she "doesn't easily get rattled and is very dependable," and Gigi says Cecilia is "good at getting stuff done." Raora and Gigi (RPGG) hunt monsters and rank food; Raora designed matching Monster Hunter outfits for them. Elizabeth calls Raora "Pretty Kitty" (Raora's first collab was with her); Cecilia showed Elizabeth around Minecraft, and in Cecilia's lore an older Justice made her a maid ("#LizIsInnocent"). With Advent, their in-story "targets": Elizabeth is Nerissa's lore "mortal enemy" and duet partner; Gigi and Cecilia form the quartet GAGA with Shiori and Bijou; Raora sang with FUWAMOCO at Serendipity 2026 and is Bijou and Kaela's "Graondstone." With seniors: Gigi shouts "MORI CALLIOPE!" and keeps trying to get Calli into League of Legends; Kiara, Cecilia and Raora are HoloEU (German and Italian lessons, EU snacks); Cecilia calls Ina her rival; Kronii is Raora's "Pizza Time" partner, Gigi's "TimeChaser," and calls Cecilia a "CLANKER" ("Owo-senpai" back); Cecilia is Mumei's "Automatowl." Beyond EN: Kureiji Ollie is Elizabeth's kami-oshi; Kaela "lives" in Raora's basement (a lore bit); Elizabeth sings covers with JP members and plays with HOLOSTARS (HoloRed with Flayon, Jurard and Crimzon, who calls her "Uncle Erb"); Cecilia games with Tokino Sora; Gigi and Okayu are OkaGigi.

## [SW] Rules
Collaboration and unit names identify public creative partnerships; some are official (CCGG), others member-used or fan labels. "Wife," "husband," fictional children, the maid backstory and "mortal enemy" are performed jokes or lore and establish no private relationship. The manhunt between Justice and Advent is shared fiction. Name only the members who took part in a collab.

## [SW] Sensory Details
An orange hoodie beside a green dress; a red sword and a violin-lance; a pink cat tail; four oshi marks in a stream title; "Ew! Get away from me, you FREAK!"; a German "Hallo" and an Italian "Ciao."

## [SW] Secrets


---

## Open Questions
1. Which of the wiki's pair names are member-used and which are fan labels is not settled for every name;
   GPT's research pass was asked to check them.
2. Twitch-era and 2026 collabs are missing from the archive; GPT's research may add them.


==================== CAST AND WORLD EDITS (git diff of final.md files) ====================

```diff
diff --git a/novel-lab/projects/holoen/runs/20260930-0704-character-Mori-Calliope/final.md b/novel-lab/projects/holoen/runs/20260930-0704-character-Mori-Calliope/final.md
index 6687a41..6e8bed5 100644
--- a/novel-lab/projects/holoen/runs/20260930-0704-character-Mori-Calliope/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-0704-character-Mori-Calliope/final.md
@@ -441,7 +441,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 Calli wants to keep improving her music, reach bigger stages and make work people remember, and in her lore that is how she harvests souls. She wants her Dead Beats to take care of themselves first and to look after the people around them.
 
 ## [SW] Relationships
-Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!" Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her chaotic CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin: frequent collaborator; Calli came to like how her own name sounds once Gigi started saying it. Kobo Kanaeru: calls her "Uncle Dad." Koseki Bijou ("Biboo," "TombStone"): a junior whose skill Calli openly admires; Bijou auditioned with an Undertale fight starring Calli, and they ran a 24-hour charity stream together (2025). Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together (a kids'-movie deep-dive, 2024), and Calli admits she is "a little obsessed with her." Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star"). Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka). Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth: her "LYRA" remix cover of "III." Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022). FUWAMOCO: "FUWAMOCALLI," a pair name the twins particularly like.
+Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!" Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her chaotic CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin ("Grem Reaper"): horror and job-simulator collabs; Gigi shouts "MORI CALLIOPE!", and Calli came to like her own name once Gigi used it. Kobo Kanaeru: calls her "Uncle Dad." Koseki Bijou ("Biboo," "TombStone"): a junior whose skill Calli openly admires; Bijou auditioned with an Undertale fight starring Calli, and they ran a 24-hour charity stream together (2025). Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together, and Calli admits she is "a little obsessed with her." Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star"). Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka). Elizabeth Rose Bloodflame, Koganei Niko, Ayunda Risu and Amane Kanata: her "LYRA" remix of "III." Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022). FUWAMOCO: "FUWAMOCALLI," a pair name the twins particularly like.
 
 ## [SW] Secrets
 (none)
@@ -570,6 +570,9 @@ Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusot
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** "the twins' favorite pair name" replaced by "a pair name the twins particularly like."
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. Should Groups keep "hololive English (former branch name)", or be current-only as GPT prefers? The
diff --git a/novel-lab/projects/holoen/runs/20260930-0704-character-Ouro-Kronii/final.md b/novel-lab/projects/holoen/runs/20260930-0704-character-Ouro-Kronii/final.md
index 2397153..121fa72 100644
--- a/novel-lab/projects/holoen/runs/20260930-0704-character-Ouro-Kronii/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-0704-character-Ouro-Kronii/final.md
@@ -385,7 +385,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 Kronii wants to entertain her Kronies with games, singing and voice work, and to give performances worthy of their support. She plays at being flawless, and her Warden persona treats disorder as an enemy, and she admits, dryly, that she would like to be happy.
 
 ## [SW] Relationships
-Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'Clock); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated 2025): Council genmate and frequent partner (KronMei), from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet in Mumei's last month (2025). Ceres Fauna (graduated 2025): Council genmate who described Kronii's "gap moe"; they once defused bombs speaking only in ASMR. Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel. Gigi Murin: collaborator in the units "TimeChaser" and "Clockwork Orange." Cecilia Immergreen: calls her "Owo-senpai"; Kronii calls her a "CLANKER." Raora Panthera: "Pizza Time" partner who calls her "Tam Tender." Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live. Shiori Novella: they hosted "Rating Your Clocks" together (2025), and they sang "MONSTER" with Ina and Gigi at the 2025 English concert. Koseki Bijou: Lethal Company and Yu-Gi-Oh collabs. FUWAMOCO: "WatchDog."
+Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'Clock); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated 2025): Council genmate and frequent partner (KronMei), from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet in Mumei's last month (2025). Ceres Fauna (graduated 2025): Council genmate who described Kronii's "gap moe"; they once defused bombs speaking only in ASMR. Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel. Gigi Murin: collaborator in the units "TimeChaser" and "Clockwork Orange." Cecilia Immergreen: calls her "Owo-senpai"; Kronii calls her a "CLANKER." Raora Panthera: "Pizza Time" partner who calls her "Tam Tender." Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live. Shiori Novella: they hosted "Rating Your Clocks" together (2025), and they sang "MONSTER" with Ina and Gigi at the 2025 English concert. Koseki Bijou: Lethal Company and Yu-Gi-Oh collabs. FUWAMOCO: "WatchDog." Raora Panthera: Portal 2 (2024) and Backrooms Cleanup Crew (2026) as "Pizza Time."
 
 ## [SW] Secrets
 (none)
@@ -517,6 +517,9 @@ Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'Clock); "
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** the clocks entry corrected to "they hosted 'Rating Your Clocks' together" (no claim whose clocks).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. Should Groups keep "Council (former unit name)", or be current-only as GPT prefers? (Current choice:
diff --git a/novel-lab/projects/holoen/runs/20260930-1113-character-Gawr-Gura/final.md b/novel-lab/projects/holoen/runs/20260930-1113-character-Gawr-Gura/final.md
index 4437ef1..a182f47 100644
--- a/novel-lab/projects/holoen/runs/20260930-1113-character-Gawr-Gura/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Gawr-Gura/final.md
@@ -379,7 +379,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 Gura wants to have fun (games, songs, snacks) and share it with her chumbuds. Her apex-predator boasting is a persona bit; games, songs and audience interaction drive her public activities.
 
 ## [SW] Relationships
-Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George." Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated. Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week. Shiori Novella and Nerissa Ravencroft: her "Scarlet Wand" guildmates in the ENigmatic Recollection story.
+Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George." Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated. Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week. Shiori Novella and Nerissa Ravencroft: her "Scarlet Wand" guildmates in the ENigmatic Recollection story. Cecilia Immergreen: Keep Talking and Nobody Explodes and The Forest (2025). Raora Panthera: R.E.P.O. (2025).
 
 ## [SW] Secrets
 (none)
@@ -472,6 +472,9 @@ Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** the Fuwawa entry removed (a shared difficulty is not a relationship).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. "Fuck" is attested once in the 4.4-hour Resident Evil 2 audio of 2021 (both models hear it; the
diff --git a/novel-lab/projects/holoen/runs/20260930-1113-character-Ninomae-Inanis/final.md b/novel-lab/projects/holoen/runs/20260930-1113-character-Ninomae-Inanis/final.md
index 1b67f9d..68cd7aa 100644
--- a/novel-lab/projects/holoen/runs/20260930-1113-character-Ninomae-Inanis/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Ninomae-Inanis/final.md
@@ -384,7 +384,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her lore, Ina delivers sanity checks on humanity. In her own public words, she wants to give her viewers a better day, make art and music, grow as a performer and give back through charity, and she loves groan-inducing wordplay.
 
 ## [SW] Relationships
-Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'Clock); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, Ina credits Kiara's support with helping her gain confidence in dancing, and Kiara groans at her puns. Mori Calliope: a recurring target of her puns ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy ("TakoRocky") whose collab outfit Ina designed; with IRyS they starred at hololive night at Dodger Stadium (2025). IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island. Houshou Marine: a senior artist she admires. Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025). Shiori Novella: a "Rate Your Fears" nightmare talk (2024) and "MONSTER" with Kronii and Gigi at the 2025 English concert. FUWAMOCO: "SHALLYS" with Cecilia at the same concert.
+Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'Clock); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, Ina credits Kiara's support with helping her gain confidence in dancing, and Kiara groans at her puns. Mori Calliope: a recurring target of her puns ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy ("TakoRocky") whose collab outfit Ina designed; with IRyS they starred at hololive night at Dodger Stadium (2025). IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island. Houshou Marine: a senior artist she admires. Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025). Shiori Novella: a "Rate Your Fears" nightmare talk (2024) and "MONSTER" with Kronii and Gigi at the 2025 English concert. FUWAMOCO: "SHALLYS" with Cecilia at the same concert. Cecilia Immergreen: her self-declared rival and Stranger of Paradise partner (2025). Gigi Murin and Raora Panthera: Blood Typers with Gigi, Puyo Puyo Tetris 2 with Raora, and a sponsored Monster Hunter Wilds launch with both and Bijou (2025).
 
 ## [SW] Secrets
 (none)
@@ -477,6 +477,9 @@ Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'Clock); "two
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** missing fact adopted: hololive night at Dodger Stadium, 2025-07-05, with Bijou and IRyS (official report, https://hololive.hololivepro.com/en/news/20250731-01-353/).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. Which of her song narratives (MECONOPSIS's protective duty, TAKO∞TAKOVER's takeover) should a story
diff --git a/novel-lab/projects/holoen/runs/20260930-1113-character-Takanashi-Kiara/final.md b/novel-lab/projects/holoen/runs/20260930-1113-character-Takanashi-Kiara/final.md
index c65669b..dab83e6 100644
--- a/novel-lab/projects/holoen/runs/20260930-1113-character-Takanashi-Kiara/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Takanashi-Kiara/final.md
@@ -395,7 +395,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her KFP persona, Kiara plays the ambitious fast-food CEO; as a performer, she wants to entertain, connect audiences across languages and deliver ambitious shows, and she hopes new people will keep joining KFP.
 
 ## [SW] Relationships
-Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert ("Rocku Wawa"); they share the "6 7" meme. Shiori Novella: an occult handcam off-collab ("#shiotori," 2024). Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI). Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera: cast the infamous "Doom." Cecilia Immergreen: German-speaking partner. Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior. Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert, and she was HOLOTALK's 33rd guest. Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left.
+Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert ("Rocku Wawa"); they share the "6 7" meme. Shiori Novella: an occult handcam off-collab ("#shiotori," 2024). Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI). Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera and Cecilia Immergreen: "HoloEU" (Italian lessons, German chats); Raora's friendly-fire "Doom" in Kiara's Mage Arena collab became a meme. Gigi Murin: "Ultra Orange." Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior. Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert. Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left.
 
 ## [SW] Secrets
 (none)
@@ -495,6 +495,9 @@ Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long cal
 - **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. Should the card quote one crude line verbatim (for example "I'm an innocent maiden." as irony), or is
diff --git a/novel-lab/projects/holoen/runs/20260930-1113-character-Watson-Amelia/final.md b/novel-lab/projects/holoen/runs/20260930-1113-character-Watson-Amelia/final.md
index 6f2b5db..445a67a 100644
--- a/novel-lab/projects/holoen/runs/20260930-1113-character-Watson-Amelia/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-1113-character-Watson-Amelia/final.md
@@ -388,7 +388,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 Ame wants to crack every case and every game her own way, make entertaining experiments for her Teamates, and help her friends, whether that means fixing their tech, building something new with them or raising money for a good cause.
 
 ## [SW] Relationships
-Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs. Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week. FUWAMOCO: "Detective Dogs" (Escape Simulator, 2024: "blondes can solve any puzzle"). Shiori Novella: a VRChat aquarium visit with "Ame Senpai" (2024). Koseki Bijou: Overwatch and Apex (2023).
+Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs. Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week. FUWAMOCO: "Detective Dogs" (Escape Simulator, 2024: "blondes can solve any puzzle"). Shiori Novella: a VRChat aquarium visit with "Ame Senpai" (2024). Koseki Bijou: Overwatch and Apex (2023). Gigi Murin: in the ENigmatic Recollection story Gigi's knight Gonathon married Ame's Jyonathan ("ClueChaser"), a role-play bit. Cecilia Immergreen and Gigi: Borderlands 2 with Mumei (2024).
 
 ## [SW] Secrets
 (none)
@@ -480,6 +480,9 @@ Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeS
 - **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. Corroborated by audio (both models): the ground-pound joke, the time-travel reveal, the VALORANT rage
diff --git a/novel-lab/projects/holoen/runs/20260930-2309-world-VTuber-Persona-and-Lore/final.md b/novel-lab/projects/holoen/runs/20260930-2309-world-VTuber-Persona-and-Lore/final.md
index 8e1687f..6770967 100644
--- a/novel-lab/projects/holoen/runs/20260930-2309-world-VTuber-Persona-and-Lore/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-2309-world-VTuber-Persona-and-Lore/final.md
@@ -103,7 +103,7 @@ Premise / rule of the setting (how reality works in these stories).
 5. A sincere moment arrives mid-bit, and the member steps out of the persona to say it plainly.
 
 ## Links to Characters
-All fourteen cast members. Each character card's Background and Personality open with the persona frame
+All eighteen cast members. Each character card's Background and Personality open with the persona frame
 ("streams as…", "her lore says…").
 
 ## Secrets
@@ -133,7 +133,7 @@ Premise
 VTuber lore, hololive persona, kayfabe, in-character, canonically
 
 ## [SW] Description
-The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization, an archiver who broke out of a prison for forbidden things, a gem born from human emotion, twin demonic guard dogs) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.
+The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization, an archiver who broke out of a prison for forbidden things, a gem born from human emotion, twin demonic guard dogs, Justice's queen, gremlin, ancient automaton and big-cat artist sent to catch them) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.
 
 ## [SW] Rules
 No one has supernatural powers. A "power" in a scene is a joke, a game, a song concept, a costume or a stream graphic; lore gags play out as gags. A member may improvise or contradict lore within a bit; an improvised joke does not automatically rewrite historical facts or permanent continuity. Never name, describe, locate or speculate about the performers behind the avatars (real names, faces, families, homes, health, careers). Public availability does not override this: identities, homes, families, health, private relationships and other prohibited personal details stay outside the story. Ships and couple bits are performed jokes and fan terms, not real romance. Characters are depicted using their public avatar designs; floating books, halos and similar elements are visual conventions, model effects or staged props, not abilities.
@@ -160,6 +160,9 @@ An avatar mirroring every head tilt; chat flooding with emotes when a lore joke
 - **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
 - **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
   (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
+- **2026-10-01, cast expansion (author: Justice, and complete the world):** Justice members and events added
+  (official -All for One- report, Serendipity interviews 03/06/07, official profiles, archive metadata; see
+  "hololive -Justice-" and "Justice Pairs").
 
 ## Open Questions
 1. Off-stream scenes show members as their avatar selves (a fan-fiction convention). If the author ever
diff --git a/novel-lab/projects/holoen/runs/20260930-2309-world-hololive/final.md b/novel-lab/projects/holoen/runs/20260930-2309-world-hololive/final.md
index fce0e8d..f05af6d 100644
--- a/novel-lab/projects/holoen/runs/20260930-2309-world-hololive/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-2309-world-hololive/final.md
@@ -90,8 +90,8 @@ Faction / organization (and workplace).
 5. A schedule collision turns two members' streams into an impromptu collab.
 
 ## Links to Characters
-All fourteen. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
-Kronii and IRyS are active in hololive -Promise-, where Fauna and Mumei are alumnae; Nerissa, Shiori, Bijou, Fuwawa and Mococo in hololive -Advent-. Detailed history: the
+All eighteen. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
+Kronii and IRyS are active in hololive -Promise-, where Fauna and Mumei are alumnae; Nerissa, Shiori, Bijou, Fuwawa and Mococo in hololive -Advent-; Elizabeth, Gigi, Cecilia and Raora in hololive -Justice-. Detailed history: the
 cards "hololive History to 2022," "hololive History 2023-2026" and "Concerts and Live Events."
 
 ## Secrets
@@ -148,6 +148,9 @@ A "Starting soon" screen; a superchat chime; a concert LED wall behind a 3D avat
 - **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
 - **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
   (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
+- **2026-10-01, cast expansion (author: Justice, and complete the world):** Justice members and events added
+  (official -All for One- report, Serendipity interviews 03/06/07, official profiles, archive metadata; see
+  "hololive -Justice-" and "Justice Pairs").
 
 ## Open Questions
 (None. The baseline date 2026-09-30 is fixed by the author.)
diff --git a/novel-lab/projects/holoen/runs/20260930-2334-character-IRyS/final.md b/novel-lab/projects/holoen/runs/20260930-2334-character-IRyS/final.md
index f3f374e..0663ba3 100644
--- a/novel-lab/projects/holoen/runs/20260930-2334-character-IRyS/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-2334-character-IRyS/final.md
@@ -262,7 +262,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 IRyS wants to deliver hope through her songs and reach bigger stages: after her first full album, "DANGERyS" (2026), comes her first solo concert in Tokyo, and someday an anime song. She wants to collab with every member of hololive and keep her fans' spirits up.
 
 ## [SW] Relationships
-Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina they starred at hololive night at Dodger Stadium (2025). Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna (graduated 2025): Promise unitmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Nanashi Mumei (graduated 2025): Promise unitmate; they played Overwatch together during Mumei's farewell week. Shiori Novella: Monster Hunter Wilds and PEAK (2025).
+Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina they starred at hololive night at Dodger Stadium (2025). Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna (graduated 2025): Promise unitmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Nanashi Mumei (graduated 2025): Promise unitmate; they played Overwatch together during Mumei's farewell week. Shiori Novella: Monster Hunter Wilds and PEAK (2025). Gigi Murin: a "Cerulean Cup" guildmate in the ENigmatic Recollection story. Cecilia Immergreen: Elden Ring Nightreign (2025).
 
 ## [SW] Secrets
 (none)
@@ -297,6 +297,9 @@ Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** "frequent" replaced by the concrete games; missing fact adopted: hololive night at Dodger Stadium, 2025-07-05, with Bijou and Ina (official report, https://hololive.hololivepro.com/en/news/20250731-01-353/).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. The wiki calls her speaking voice "high-pitched"; in this project's 2026 sample it measures mid-range.
diff --git a/novel-lab/projects/holoen/runs/20260930-2334-character-Nerissa-Ravencroft/final.md b/novel-lab/projects/holoen/runs/20260930-2334-character-Nerissa-Ravencroft/final.md
index e65c01a..f70bbef 100644
--- a/novel-lab/projects/holoen/runs/20260930-2334-character-Nerissa-Ravencroft/final.md
+++ b/novel-lab/projects/holoen/runs/20260930-2334-character-Nerissa-Ravencroft/final.md
@@ -263,7 +263,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 Nerissa wants to sing for audiences, develop her music and acting, collaborate across hololive and improve her Japanese. Her lore echoes this ambition through the Demon of Sound's desire to sing.
 
 ## [SW] Relationships
-Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit (ShioRaven); Shiori plays hard to get, and the two keep a joke lore of fictional "children." Fuwawa and Mococo Abyssgard (FUWAMOCO; "Sound Hounds"): she claims, as a bit, to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower. IRyS: fellow singer who guested at that concert. Elizabeth Rose Bloodflame: her "mortal enemy" in their lore (a performed rivalry) from Justice and her 2026 Serendipity duet partner; they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai"). Moona Hoshinova: she sings on Moona's "100%" (2025). Houshou Marine: her other oshi. Gigi Murin: duo partner with a joke "child," Nerigi. Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025); with Kiara they sang "Beyond the way" at the 2024 English concert. Ceres Fauna (graduated 2025): the senpai she excitedly replied to on her first day on X ("Fauna-senpai!!!"); with Shiori they sang "Lonely in Gorgeous" at the same concert.
+Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit (ShioRaven); Shiori plays hard to get, and the two keep a joke lore of fictional "children." Fuwawa and Mococo Abyssgard (FUWAMOCO; "Sound Hounds"): she claims, as a bit, to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower. IRyS: fellow singer who guested at that concert. Elizabeth Rose Bloodflame: her "mortal enemy" in their lore (a performed rivalry) from Justice and her 2026 Serendipity duet partner; they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai"). Moona Hoshinova: she sings on Moona's "100%" (2025). Houshou Marine: her other oshi. Gigi Murin: duo partner with a joke "child," Nerigi. Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025); with Kiara they sang "Beyond the way" at the 2024 English concert. Ceres Fauna (graduated 2025): the senpai she excitedly replied to on her first day on X ("Fauna-senpai!!!"); with Shiori they sang "Lonely in Gorgeous" at the same concert. Cecilia Immergreen: "AutoTune" (Unravel Two, 2024). Raora Panthera: "V3LVET" with Moona; Clubhouse Games and Raft (2024–25).
 
 ## [SW] Secrets
 (none)
@@ -296,6 +296,9 @@ Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit
   Mumei and Kiara, and with Fauna and Shiori, added (official -Breaking Dimensions- report, checked by
   Claude); the X reply dated to her first day on X (2023-07-25, research/x-posts.md).
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** Advent entries reconciled with the finalized pair names (Sound Hounds; "Oobib") and the performed-bit framing ("mortal enemy" in their lore).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. Her laughter, "Ope!" and her fangirling with Kiara were not captured by the audio check (whisper does
diff --git a/novel-lab/projects/holoen/runs/20261001-0018-world-Concerts-and-Live-Events/final.md b/novel-lab/projects/holoen/runs/20261001-0018-world-Concerts-and-Live-Events/final.md
index c2618ce..5e501bb 100644
--- a/novel-lab/projects/holoen/runs/20261001-0018-world-Concerts-and-Live-Events/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-Concerts-and-Live-Events/final.md
@@ -31,9 +31,9 @@ Recurring events / culture.
   [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music
   Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora
   Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's
-  "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest" [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around
+  "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group stage, "ABOVE BELOW"; Cecilia's "Wind-Up," the first Justice solo, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around
   partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and
-  Nerissa–Elizabeth Rose Bloodflame), each with a published interview. Dates are US local time.
+  Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Dates are US local time.
   [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
 - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo
   Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before
@@ -91,7 +91,7 @@ Recurring events / culture.
 5. A tour stop in Sydney: Kronii joins Calli, IRyS and Nerissa as a guest.
 
 ## Links to Characters
-All fourteen (Advent: -Breaking Dimensions-, -All for One-, Serendipity and their own anniversary lives; Fauna and Mumei: the 2023 EN concert, 4th fes., Mumei's 2024 3D birthday live "Outside the Box" and 6th fes.).
+All eighteen (Justice: -All for One-, Serendipity, their 3D and anniversary lives; Advent: -Breaking Dimensions-, -All for One-, Serendipity and their own anniversary lives; Fauna and Mumei: the 2023 EN concert, 4th fes., Mumei's 2024 3D birthday live "Outside the Box" and 6th fes.).
 
 ## Secrets
 (None.)
@@ -111,7 +111,7 @@ All fourteen (Advent: -Breaking Dimensions-, -All for One-, Serendipity and thei
 - S7 Official post-event report, World Tour '24 (2025-02-17): https://hololive.hololivepro.com/en/news/20250217-01-128/
 - S8 Official concert report, -Breaking Dimensions-: https://hololive.hololivepro.com/en/events/breaking-dimensions/
 - S9 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
-- S10 Official Serendipity interviews, FUWAMOCO & Raora (interview03), Kiara & Bijou (interview04), Calliope & Shiori (interview05)
+- S10 Official Serendipity interviews, FUWAMOCO & Raora (interview03), Kiara & Bijou (interview04), Calliope & Shiori (interview05), Gigi & Cecilia (interview06)
 - S4 Character files in this project (C6, C11, C19; T10–T12; I7, I20; K4, K33; R2, R3, R20; N2, N3; G5)
 
 ---
@@ -126,7 +126,7 @@ Culture
 fes, hololive fes, SUPER EXPO, EN concert, Serendipity, world tour, 3D live, birthday live, aftertalk
 
 ## [SW] Description
-The stages of the hololive year. Recurring formats: each spring, hololive fes. with hololive SUPER EXPO in Japan (a combined tradition since 2022; Calli and Kiara sang at the 2022 fes. in Makuhari, Nerissa at the 6th fes. in 2025); each summer, a hololive English concert in the US (2023 "-Connect the World-"; 2024 "-Breaking Dimensions-," New York; 2025 "-All for One-," Radio City; 2026 "Serendipity," Los Angeles, July 3–4, built on pairs including Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Bae, Nerissa–Elizabeth and FUWAMOCO–Raora); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet. The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn" (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (March 2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); hololive night at Dodger Stadium with Ina, IRyS and Bijou (2025-07-05); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!" (2025) and "Bound by Fate" (2026). A member may stream an aftertalk afterward.
+The stages of the hololive year. Recurring formats: each spring, hololive fes. with hololive SUPER EXPO in Japan (a combined tradition since 2022; Calli and Kiara sang at the 2022 fes. in Makuhari, Nerissa at the 6th fes. in 2025); each summer, a hololive English concert in the US (2023 "-Connect the World-"; 2024 "-Breaking Dimensions-," New York; 2025 "-All for One-," Radio City; 2026 "Serendipity," Los Angeles, July 3–4, built on pairs including Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Bae, Nerissa–Elizabeth, FUWAMOCO–Raora and Gigi–Cecilia); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet. The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn" (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (March 2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); hololive night at Dodger Stadium with Ina, IRyS and Bijou (2025-07-05); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!" (2025) and "Bound by Fate" (2026); Justice's first group stage at -All for One- (2025), CCGG's 3D live, Raora's first birthday live (2026) and Justice's second-anniversary live "How to Protect JUSTICE!" (2026). A member may stream an aftertalk afterward.
 
 ## [SW] Rules
 Concerts are told through the avatar performance and the members' talk before and after (nerves, rehearsals, interviews, aftertalks), never the performers' physical bodies. Some guests are announced, others are surprises. US concert dates are local time; streamed lives may differ by a day between the Americas and Japan. IRyS's solo concert has not happened yet at the 2026-09-30 baseline.
@@ -157,6 +157,9 @@ Glowsticks in member colors; an LED wall; a new 3D outfit's reveal; a call-and-r
 - **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
   (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** missing fact adopted: hololive night at Dodger Stadium (2025-07-05; https://hololive.hololivepro.com/en/news/20250731-01-353/).
+- **2026-10-01, cast expansion (author: Justice, and complete the world):** Justice members and events added
+  (official -All for One- report, Serendipity interviews 03/06/07, official profiles, archive metadata; see
+  "hololive -Justice-" and "Justice Pairs").
 
 ## Open Questions
 1. Which characters performed at the four EN concerts (2023–2025 line-ups) was not checked; only
diff --git a/novel-lab/projects/holoen/runs/20261001-0018-world-Cross-Branch-Friends/final.md b/novel-lab/projects/holoen/runs/20261001-0018-world-Cross-Branch-Friends/final.md
index 132cbab..aa27827 100644
--- a/novel-lab/projects/holoen/runs/20261001-0018-world-Cross-Branch-Friends/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-Cross-Branch-Friends/final.md
@@ -100,7 +100,7 @@ Relationship web.
 5. Kiara and Reine plan another "vacation" in VR.
 
 ## Links to Characters
-All fourteen.
+All eighteen.
 
 ## Secrets
 (None.)
@@ -133,7 +133,7 @@ Relationship
 Death Star, MoRikka, LYRA, Holodeath, PavoNashi, HOLOTORI, UMISEA, HoloJEI, TakoNeko, K.I.R.A, OKFAIR, Star Flower, IRySora, soranii, Apex Predators, KoMeHa, BLUE·MEGAMISAMA, V3LVET
 
 ## [SW] Description
-The cast's ties beyond EN, including JP, ID, DEV_IS and HOLOSTARS. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones" ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI"). Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora. IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan." Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week. Of Advent: Bijou and Kaela Kovalskia are "Grindstone" (Kaela calls her "Beejoe"; Raft, Minecraft, Split Fiction), with Kureiji Ollie ("GraveStone"), Akai Haato ("Red Stone") and Ichijou Ririka (ReGLOSS; Smash Bros.) as game partners; Shiori and Vestia Zeta are the official duo "GreyScaleX" (the X is silent; "Purrfect Pair" merchandise, 2026), Pavolia Reine and Airani Iofi join her "Fanfic Club," and she found hololive through Inugami Korone's clips; FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo), they game with Shirakami Fubuki and Hakui Koyori, and Oozora Subaru sang "HOT DUCK!" with them and Bijou.
+The cast's ties beyond EN, including JP, ID, DEV_IS and HOLOSTARS. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones" ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI"). Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora. IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan." Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week. Of Advent: Bijou and Kaela Kovalskia are "Grindstone" (Kaela calls her "Beejoe"; Raft, Minecraft, Split Fiction), with Kureiji Ollie ("GraveStone"), Akai Haato ("Red Stone") and Ichijou Ririka (ReGLOSS; Smash Bros.) as game partners; Shiori and Vestia Zeta are the official duo "GreyScaleX" (the X is silent; "Purrfect Pair" merchandise, 2026), Pavolia Reine and Airani Iofi join her "Fanfic Club," and she found hololive through Inugami Korone's clips; FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo), they game with Shirakami Fubuki and Hakui Koyori, and Oozora Subaru sang "HOT DUCK!" with them and Bijou. Of Justice: Kureiji Ollie is Elizabeth's kami-oshi (and her "HoloRed" partner with HOLOSTARS' Flayon, Jurard and Crimzon Ruze, who calls her "Uncle Erb"); Elizabeth's 2026 birthday covers featured Subaru, Roboco, Sora, Choco, Marine, Korone, Polka, Nene, Watame and Iroha; Kaela Kovalskia "lives" in Raora's basement (a lore bit; "SMITTEN"); Raora games with Haachama and Zeta and is "RaoRiRi" with Ririka; Cecilia plays with Tokino Sora; Gigi and Okayu are "OkaGigi."
 
 ## [SW] Rules
 Senpai and kouhai describe relative seniority, not language or nationality; forms of address and levels of formality vary by relationship. Unit lineups belong to their period: graduates and affiliates are not current regular partners. Members of other agencies are only brief, friendly mentions.
@@ -167,6 +167,9 @@ A bilingual stream title with both names; a senpai's plush on a shelf; a starstr
 - **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
   (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** the archive-derived ranking ("most frequent documented partner") replaced by concrete activities; GreyScaleX identified as an official duo (official shop, 2026-09-05); Ririka (ReGLOSS) and the Fanfic Club carried into the exported Description.
+- **2026-10-01, cast expansion (author: Justice, and complete the world):** Justice members and events added
+  (official -All for One- report, Serendipity interviews 03/06/07, official profiles, archive metadata; see
+  "hololive -Justice-" and "Justice Pairs").
 
 ## Open Questions
 (None.)
diff --git a/novel-lab/projects/holoen/runs/20261001-0018-world-hololive-History-2023-2026/final.md b/novel-lab/projects/holoen/runs/20261001-0018-world-hololive-History-2023-2026/final.md
index 2a866a5..470ebb2 100644
--- a/novel-lab/projects/holoen/runs/20261001-0018-world-hololive-History-2023-2026/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0018-world-hololive-History-2023-2026/final.md
@@ -54,6 +54,10 @@ Historical events.
 | 2025-05-02 | ENReco chapter 2 "The Chains of Fate" | — |
 | 2025-07-05 | hololive night at Dodger Stadium, Los Angeles, the second hololive–Dodgers collaboration: Ina, IRyS and Bijou | a stadium sing-along |
 | 2025-07-16 | hololive RECORDS label launched | — |
+| 2025-08-01/02/09/10 | Justice 3D debuts: Elizabeth, Gigi, Cecilia ("Wind-Up"), Raora ("Gacha×Gacha ADVENTURE!") | Justice's first group stage follows at -All for One- |
+| 2025-11-16 | Raora's friendly-fire "Doom" spell in Kiara's Mage Arena collab becomes a meme | a callback for the whole cast |
+| 2026-05 | Gigi and Cecilia's CCGG 3D live and "CCGG MADNESS"; Raora's first birthday 3D live (05-10) | — |
+| 2026-06-27 | Justice's second-anniversary live "How to Protect JUSTICE!" | — |
 | 2025-08-23/24 EDT | EN 3rd concert "-All for One-" (Radio City Music Hall, New York): day 1 opens with the all-member "All for One," followed by Advent's "Genesis"; Justice's first stage as a group | all fifteen EN members on one stage |
 | 2025-08-29 | Advent 2nd-anniversary live "On the Run!" ("The Story of Advent") | Nerissa's group milestone |
 | 2025-10-03 | Hiodoshi Ao (ReGLOSS) leaves | — |
@@ -63,7 +67,7 @@ Historical events.
 | 2026-03-06/08 | SUPER EXPO 2026 and 7th fes. "Ridin' on Dreams" | — |
 | 2026-03-27/28 | Kiara and Ina's duo concert "Drawn to Dawn" (Los Angeles) | TakoTori on stage |
 | 2026-05-24 | ENReco chapter 3 "Broken Bonds" | — |
-| 2026-07-03/04 | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around partner pairs (Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Bae, Nerissa–Elizabeth, FUWAMOCO–Raora) | The current partnerships |
+| 2026-07-03/04 | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around partner pairs (Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Bae, Nerissa–Elizabeth, FUWAMOCO–Raora, Gigi–Cecilia) | The current partnerships |
 | 2026-07/08 | Shiori's original motion comic "Into The Void" (with Elizabeth, Gigi, Nerissa); Advent's 3rd-anniversary 3D live "Bound by Fate"; FUWAMOCO announce their first album (08-29) | — |
 | 2026-07-23 | Rhythm game "hololive Dreams" released | — |
 | 2026-09-07 | "hololive Next": the female-talent branches unify under **hololive**; new logo; members to get updated designs (Tokino Sora first); "hololive raku" app; TV anime "Odeholo"; 10th-anniversary countdown | The present-day setting |
@@ -99,7 +103,7 @@ Historical events.
 5. IRyS's nerves before her first solo concert in Tokyo.
 
 ## Links to Characters
-All fourteen. Advent (Nerissa, Shiori, Bijou, Fuwawa, Mococo; 2023); Fauna and Mumei (graduated 2025); IRyS and Kronii (Promise, 2023); Ame (affiliate, 2024); Gura
+All eighteen. Justice (Elizabeth, Gigi, Cecilia, Raora; 2024); Advent (Nerissa, Shiori, Bijou, Fuwawa, Mococo; 2023); Fauna and Mumei (graduated 2025); IRyS and Kronii (Promise, 2023); Ame (affiliate, 2024); Gura
 (graduated, 2025); Calli, IRyS and Nerissa (World Tour '25); Kiara and Ina (Drawn to Dawn); Kronii, Ina,
 Kiara and Calli (Serendipity pairs).
 
@@ -132,7 +136,7 @@ Event
 recent hololive history, the merger, the 2025 graduations, holoEN's later generations
 
 ## [SW] Description
-The recent past behind the present. 2023: Advent debuts (Nerissa, Shiori, Bijou, FUWAMOCO, July); DEV_IS opens with ReGLOSS; IRyS and the Council become -Promise- (October); EN holds its 1st concert. 2024: Justice debuts (June) as the "law enforcers" hunting Advent; the ENigmatic Recollection fantasy story starts (IRyS's guild "Cerulean Cup," Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); EN's 3rd concert at Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; EN's 4th concert "Serendipity" in Los Angeles (pairs Calli–Shiori, Kronii–Ina, Kiara–Bijou); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
+The recent past behind the present. 2023: Advent debuts (Nerissa, Shiori, Bijou, FUWAMOCO, July); DEV_IS opens with ReGLOSS; IRyS and the Council become -Promise- (October); EN holds its 1st concert. 2024: Justice debuts (June) as the "law enforcers" hunting Advent; the ENigmatic Recollection fantasy story starts (IRyS's guild "Cerulean Cup," Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); EN's 3rd concert at Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; EN's 4th concert "Serendipity" in Los Angeles (pairs Calli–Shiori, Kronii–Ina, Kiara–Bijou, Gigi–Cecilia and more; Justice's second-anniversary live "How to Protect JUSTICE!"); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
 
 ## [SW] Rules
 After 2026-09-07 members say "from hololive"; old group names survive as units. Affiliates may appear at events; graduates appear only as memories. ENReco is a fictional story the members play in, separate from their persona lore.
@@ -161,6 +165,9 @@ The new 2026 hololive logo; a world-tour poster of city names; Advent's "WANTED!
 - **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
   (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
 - **2026-10-01, from GPT one-round review of the Advent cast edits (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, high):** concert opening corrected (day one opened with the all-member "All for One," then "Genesis"); 3D debut dates labeled PDT; missing fact adopted: hololive night at Dodger Stadium (2025-07-05; https://hololive.hololivepro.com/en/news/20250731-01-353/).
+- **2026-10-01, cast expansion (author: Justice, and complete the world):** Justice members and events added
+  (official -All for One- report, Serendipity interviews 03/06/07, official profiles, archive metadata; see
+  "hololive -Justice-" and "Justice Pairs").
 
 ## Open Questions
 (None. Serendipity pairs for IRyS and Nerissa were found: see "Concerts and Live Events.")
diff --git a/novel-lab/projects/holoen/runs/20261001-0430-character-Ceres-Fauna/final.md b/novel-lab/projects/holoen/runs/20261001-0430-character-Ceres-Fauna/final.md
index 1b7f79e..5816526 100644
--- a/novel-lab/projects/holoen/runs/20261001-0430-character-Ceres-Fauna/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0430-character-Ceres-Fauna/final.md
@@ -287,7 +287,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her lore, Fauna wants to win humans over and lead them back to nature. As a streamer she wanted to comfort her Saplings, sing, learn Japanese, collab with her genmates in person, speedrun games and voice-act in a game, and to finish what she started, like the World Tree.
 
 ## [SW] Relationships
-Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024); Silent Hill 2 with Gigi Murin. Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!" Koseki Bijou: "Coach Fauna" in Bijou's Hitman runs and a "Sweaty TryHard Gamers" squad with Bae and Kaela. FUWAMOCO: helped on the World Tree's last day (2024-12-31). Shiori Novella: the third voice of "Lonely in Gorgeous."
+Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024); Silent Hill 2 with Gigi Murin. Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!" Koseki Bijou: "Coach Fauna" in Bijou's Hitman runs and a "Sweaty TryHard Gamers" squad with Bae and Kaela. FUWAMOCO: helped on the World Tree's last day (2024-12-31). Shiori Novella: the third voice of "Lonely in Gorgeous." Cecilia Immergreen: "Green Women" (a shoujo-tropes ranking, 2024). Gigi Murin: "FruitPunch" (a Coughing Baby Award Show, 2024).
 
 ## [SW] Secrets
 (none)
@@ -328,6 +328,9 @@ Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collab
 - **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. "Evil Fauna," the yandere lines and the forklift dramas come from the wiki's quote list (secondary, no
diff --git a/novel-lab/projects/holoen/runs/20261001-0430-character-Nanashi-Mumei/final.md b/novel-lab/projects/holoen/runs/20261001-0430-character-Nanashi-Mumei/final.md
index 85366c7..6b93f8d 100644
--- a/novel-lab/projects/holoen/runs/20261001-0430-character-Nanashi-Mumei/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0430-character-Nanashi-Mumei/final.md
@@ -294,7 +294,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her lore, Mumei records human history so it isn't forgotten, though she forgets things herself. As a streamer she wanted to grow: a song in a rhythm game, learning Japanese again, collabs with her senpai, new skills like guitar, and a 3D live, which she held in 2024.
 
 ## [SW] Relationships
-Ceres Fauna (graduated 2025-01): Council and Promise genmate and recurring collaborator; their comedy includes Fauna's exaggerated protective, possessive bits ("return to nature"), complicated by Mumei's macabre humor; they premiered their duet "It's Not a Phase" at the 2024 English concert. Hakos Baelz: genmate and a recurring collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). Ouro Kronii ("KronMei"): genmate and frequent partner, from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). IRyS: Promise unitmate from 2023; they played Overwatch together in Mumei's farewell week, then R.E.P.O. with all of Promise (2025-04-24). Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday. Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Mumei was Kiara's HOLOTALK guest in her last week. Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week. Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week. Ninomae Ina'nis: fellow artist, drawing collabs. Mori Calliope: "ANATOMY REVIEW." Nerissa Ravencroft: "EMO HOURS" (2023), "Beyond the way" with Kiara at the 2024 concert, "SAD GIRL HOURS" (2025). Koseki Bijou ("Stone Age"): Portal 2 and Marvel Rivals; at arm wrestling Mumei rates her a loss because "she is a rock." Gigi Murin: Echo Point Nova as "A Towl and a Gremlin." Cecilia Immergreen: "Automatowl," who calls her "Myumyei." FUWAMOCO ("Fuwamoomco"): Overwatch. JP: Takane Lui ("Q&A With Bird Sisters"), Tokoyami Towa (calls her "Mumi-chan"), Akai Haato (Minecraft); Inugami Korone (a duet cover in her last week) and Okayu, Nene and Koyori, guests at "Outside the Box." Shiori Novella: B-movie watchalongs (Neil Breen, Kung Pow; 2025).
+Ceres Fauna (graduated 2025-01): Council and Promise genmate and recurring collaborator; their comedy includes Fauna's exaggerated protective, possessive bits ("return to nature"), complicated by Mumei's macabre humor; they premiered their duet "It's Not a Phase" at the 2024 English concert. Hakos Baelz: genmate and a recurring collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). Ouro Kronii ("KronMei"): genmate and frequent partner, from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). IRyS: Promise unitmate from 2023; they played Overwatch together in Mumei's farewell week, then R.E.P.O. with all of Promise (2025-04-24). Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday. Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Mumei was Kiara's HOLOTALK guest in her last week. Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week. Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week. Ninomae Ina'nis: fellow artist, drawing collabs. Mori Calliope: "ANATOMY REVIEW." Nerissa Ravencroft: "EMO HOURS" (2023), "Beyond the way" with Kiara at the 2024 concert, "SAD GIRL HOURS" (2025). Koseki Bijou ("Stone Age"): Portal 2 and Marvel Rivals; at arm wrestling Mumei rates her a loss because "she is a rock." Gigi Murin: Echo Point Nova as "A Towl and a Gremlin." Cecilia Immergreen: "Automatowl," who calls her "Myumyei." FUWAMOCO ("Fuwamoomco"): Overwatch. JP: Takane Lui ("Q&A With Bird Sisters"), Tokoyami Towa (calls her "Mumi-chan"), Akai Haato (Minecraft); Inugami Korone (a duet cover in her last week) and Okayu, Nene and Koyori, guests at "Outside the Box." Shiori Novella: B-movie watchalongs (Neil Breen, Kung Pow; 2025). Raora Panthera: an art stream ("a cat and an owl walk into a room," 2025).
 
 ## [SW] Secrets
 (none)
@@ -337,6 +337,9 @@ Ceres Fauna (graduated 2025-01): Council and Promise genmate and recurring colla
 - **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
   Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
   (sources in the world card "Advent Pairs" and the Advent character files).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. Wiki quote lines ("Civilization is temporary…", the "moom" verb) are secondary, without timestamps; the
diff --git a/novel-lab/projects/holoen/runs/20261001-0548-character-Koseki-Bijou/final.md b/novel-lab/projects/holoen/runs/20261001-0548-character-Koseki-Bijou/final.md
index 0f7d1a3..9762589 100644
--- a/novel-lab/projects/holoen/runs/20261001-0548-character-Koseki-Bijou/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0548-character-Koseki-Bijou/final.md
@@ -287,7 +287,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her lore, Bijou shines brighter when she meets people's good emotions. As a streamer she wants to appear in a video game and land a voice-acting role, to collab with every hololive member at least once, to perform her original songs on stage, and to grow a community of millions of Pebbles, all while keeping her streams profanity-free.
 
 ## [SW] Relationships
-Shiori Novella: Advent's "glorious leader" in Bijou's affectionate bit (Goth Rock; a "Gyatt Review"; GAGA with Gigi and Cecilia). Nerissa Ravencroft: the raven drawn to her shine (JewelBird); Bijou named her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." FUWAMOCO: "Diamond Dogs" since an Overcooked 2 collab in their first weeks; her "Rock rock!" parodies their "bau bau." Kaela Kovalskia (ID): "Grindstone" (Kaela calls her "Beejoe"): Raft, Minecraft, Split Fiction, and with Raora "Graondstone." Mori Calliope: she auditioned with an Undertale fight starring Calli; "TombStone"; a 24-hour charity stream together (2025) and Warhammer painting (2026). Takanashi Kiara: her 2026 Serendipity partner ("Rocku Wawa"), who calls her a "hidden gem" and encouraged her through hard choreography for a song with Kiara and Ame; Bijou admires Kiara's "confidence," and they keep saying "67." IRyS: her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina, they headlined hololive night at Dodger Stadium (2025). Hakos Baelz: "BaeBi" (a 2024 sleepover marathon). Nanashi Mumei (graduated 2025): "Stone Age"; Mumei rated her a loss at arm wrestling because "she is a rock." Ninomae Ina'nis: "TakoRocky," Monster Hunter partner who designed their collab outfits. Watson Amelia: Overwatch and Apex (2023). Ceres Fauna (graduated 2025): her Hitman "coach." Ouro Kronii: Lethal Company and Yu-Gi-Oh. -Justice-: GAGA with Gigi and Cecilia; Graondstone with Raora; "I'm Your Treasure Box" with Cecilia and Raora at the 2025 concert. Kureiji Ollie ("GraveStone"), Akai Haato ("Red Stone"), Regis Altare (HOLOSTARS): game partners. Ichijou Ririka (ReGLOSS): Smash Bros. with a loser's punishment and Monster Hunter.
+Shiori Novella: Advent's "glorious leader" in Bijou's affectionate bit (Goth Rock; a "Gyatt Review"; GAGA with Gigi and Cecilia). Nerissa Ravencroft: the raven drawn to her shine (JewelBird); Bijou named her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." FUWAMOCO: "Diamond Dogs" since an Overcooked 2 collab in their first weeks; her "Rock rock!" parodies their "bau bau." Kaela Kovalskia (ID): "Grindstone" (Kaela calls her "Beejoe"): Raft, Minecraft, Split Fiction, and with Raora "Graondstone." Mori Calliope: she auditioned with an Undertale fight starring Calli; "TombStone"; a 24-hour charity stream together (2025) and Warhammer painting (2026). Takanashi Kiara: her 2026 Serendipity partner ("Rocku Wawa"), who calls her a "hidden gem" and encouraged her through hard choreography for a song with Kiara and Ame; Bijou admires Kiara's "confidence," and they keep saying "67." IRyS: her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina, they headlined hololive night at Dodger Stadium (2025). Hakos Baelz: "BaeBi" (a 2024 sleepover marathon). Nanashi Mumei (graduated 2025): "Stone Age"; Mumei rated her a loss at arm wrestling because "she is a rock." Ninomae Ina'nis: "TakoRocky," Monster Hunter partner who designed their collab outfits. Watson Amelia: Overwatch and Apex (2023). Ceres Fauna (graduated 2025): her Hitman "coach." Ouro Kronii: Lethal Company and Yu-Gi-Oh. -Justice-: GAGA with Gigi and Cecilia; Graondstone with Raora; "I'm Your Treasure Box" with Cecilia and Raora at the 2025 concert. Kureiji Ollie ("GraveStone"), Akai Haato ("Red Stone"), Regis Altare (HOLOSTARS): game partners. Ichijou Ririka (ReGLOSS): Smash Bros. with a loser's punishment and Monster Hunter. Cecilia Immergreen: Walking Dead watchalongs and Elden Ring (2025). Raora Panthera: a cooking off-collab with Bijou as "my assistant" (2024).
 
 ## [SW] Secrets
 (none)
@@ -315,6 +315,9 @@ Shiori Novella: Advent's "glorious leader" in Bijou's affectionate bit (Goth Roc
 - **Not adopted, with reason:** "super rock rock" stays: besides the first-model counts, both models hear it
   in one verified clip (6:01:22; the second writes "super rock, rock").
 - **Promotion:** author decision; GPT reviewed one round only (author's instruction).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. The Tomodachi Life window was unusable (drawing, game voices), and her "squeegee" laugh and Moai opening
diff --git a/novel-lab/projects/holoen/runs/20261001-0548-character-Shiori-Novella/final.md b/novel-lab/projects/holoen/runs/20261001-0548-character-Shiori-Novella/final.md
index fcfa8c4..a38f2cb 100644
--- a/novel-lab/projects/holoen/runs/20261001-0548-character-Shiori-Novella/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0548-character-Shiori-Novella/final.md
@@ -268,7 +268,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her lore, Shiori archives stories and memories worth saving. As a creator she wants to make fun memories with people and keep them, to make things with her own hands (vlogs, games, comics, music), and to keep surprising people, from improving her vocal stamina to a ghost-hunting vlog.
 
 ## [SW] Relationships
-Nerissa Ravencroft: Advent genmate and partner in the performed ShioRaven "wife" bit; Shiori plays hard to get. Their fictional daughter and the secret of Nerissa's horn piece belong to their shared character jokes. Koseki Bijou: genmate who calls her "our glorious leader" (Goth Rock; a "Gyatt Review"). FUWAMOCO: genmates who once mistook a Minecraft cow for her (Pen Pups). Mori Calliope: her 2026 Serendipity duo partner, who admits she is "a little obsessed with her"; Shiori admires Calli's "work ethic and boundaries," and they bond over dark taste and absurd deep-dives. Takanashi Kiara: hosted Advent on HOLOTALK; an occult handcam off-collab ("#shiotori"). Ouro Kronii: they hosted "Rating Your Clocks" together (2025) and sang "MONSTER" with Ina and Gigi at the 2025 concert. IRyS: Monster Hunter Wilds and PEAK (2025). Ceres Fauna (graduated 2025): with Nerissa, "Lonely in Gorgeous" at the 2024 English concert. Nanashi Mumei (graduated 2025): B-movie watchalongs. Ninomae Ina'nis: a "Rate Your Fears" nightmare talk. Watson Amelia: a VRChat aquarium visit with "Ame Senpai." Gigi Murin, Cecilia Immergreen, Elizabeth Rose Bloodflame (-Justice-, Advent's in-story "guards"): GAGA with Bijou, Gigi and Cecilia; Gigi, Elizabeth and Nerissa voice her motion comic "Into The Void." Vestia Zeta (ID): "GreyScaleX," an official duo unit with "Purrfect Pair" merchandise (2026). Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club." HOLOSTARS: Machina X Flayon ("Goth Pilot"), Jurard T Rexford and Regis Altare in co-op games. Inugami Korone: the senior whose clips first led her to hololive.
+Nerissa Ravencroft: Advent genmate and partner in the performed ShioRaven "wife" bit; Shiori plays hard to get. Their fictional daughter and the secret of Nerissa's horn piece belong to their shared character jokes. Koseki Bijou: genmate who calls her "our glorious leader" (Goth Rock; a "Gyatt Review"). FUWAMOCO: genmates who once mistook a Minecraft cow for her (Pen Pups). Mori Calliope: her 2026 Serendipity duo partner, who admits she is "a little obsessed with her"; Shiori admires Calli's "work ethic and boundaries," and they bond over dark taste and absurd deep-dives. Takanashi Kiara: hosted Advent on HOLOTALK; an occult handcam off-collab ("#shiotori"). Ouro Kronii: they hosted "Rating Your Clocks" together (2025) and sang "MONSTER" with Ina and Gigi at the 2025 concert. IRyS: Monster Hunter Wilds and PEAK (2025). Ceres Fauna (graduated 2025): with Nerissa, "Lonely in Gorgeous" at the 2024 English concert. Nanashi Mumei (graduated 2025): B-movie watchalongs. Ninomae Ina'nis: a "Rate Your Fears" nightmare talk. Watson Amelia: a VRChat aquarium visit with "Ame Senpai." Gigi Murin, Cecilia Immergreen, Elizabeth Rose Bloodflame (-Justice-, Advent's in-story "guards"): GAGA with Bijou, Gigi and Cecilia; Gigi, Elizabeth and Nerissa voice her motion comic "Into The Void." Vestia Zeta (ID): "GreyScaleX," an official duo unit with "Purrfect Pair" merchandise (2026). Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club." HOLOSTARS: Machina X Flayon ("Goth Pilot"), Jurard T Rexford and Regis Altare in co-op games. Inugami Korone: the senior whose clips first led her to hololive. Raora Panthera: a design collab (2024) and Blood Typers (2025). Elizabeth: "NovelFlame."
 
 ## [SW] Secrets
 (none)
@@ -292,6 +292,9 @@ Nerissa Ravencroft: Advent genmate and partner in the performed ShioRaven "wife"
 - **Missing facts adopted (checked by Claude 2026-10-01):** GreyScaleX's official "Purrfect Pair" duo
   merchandise, orders from 2026-09-05 (SN6).
 - **Promotion:** author decision; GPT reviewed one round only (author's instruction).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. The sampled 2026 windows include a showcase with trailer audio and a co-op stream with viewers; counts are
diff --git a/novel-lab/projects/holoen/runs/20261001-0549-character-Fuwawa-Abyssgard/final.md b/novel-lab/projects/holoen/runs/20261001-0549-character-Fuwawa-Abyssgard/final.md
index c687438..551a36a 100644
--- a/novel-lab/projects/holoen/runs/20261001-0549-character-Fuwawa-Abyssgard/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0549-character-Fuwawa-Abyssgard/final.md
@@ -245,7 +245,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her lore, Fuwawa's job as a guard dog is to protect your smile and to look after Mococo and Pero. As an idol she and Mococo chase a list of more than a hundred dreams: a solo concert, singing with her oshi Houshou Marine, anime songs, figures, and making every Ruffian smile.
 
 ## [SW] Relationships
-Mococo Abyssgard: her younger twin, whom she calls "Moco-chan" even in English; Mococo says Fuwawa is dependable and calms her down; they finish each other's sentences ("FUWAMOCO sync") and sometimes argue; Fuwawa loved being called "Fuwa-nee" once. Pero, "The Great Perroccino": their fictional dog mascot and self-proclaimed mentor; they call him "nasty" in their public bits. Advent: Shiori (Pen Pups; they mistook a cow for her), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Fuwawa calls her "Newissa," and Nerissa claims to be the third sister, "Mofufu"). Mori Calliope: "FUWAMOCALLI," a collaboration name the twins say they particularly like. Watson Amelia: "Detective Dogs." Ouro Kronii: "WatchDog." Nanashi Mumei (graduated 2025): "Fuwamoomco" (Overwatch). Raora Panthera: their 2026 Serendipity trio partner, who drew them a shikishi before her debut. Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026). Houshou Marine: her oshi (a Touhou off-collab). Shirakami Fubuki and Hakui Koyori ("FUWAMOKOYO"): horror and Lethal Company partners.
+Mococo Abyssgard: her younger twin, whom she calls "Moco-chan" even in English; Mococo says Fuwawa is dependable and calms her down; they finish each other's sentences ("FUWAMOCO sync") and sometimes argue; Fuwawa loved being called "Fuwa-nee" once. Pero, "The Great Perroccino": their fictional dog mascot and self-proclaimed mentor; they call him "nasty" in their public bits. Advent: Shiori (Pen Pups; they mistook a cow for her), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Fuwawa calls her "Newissa," and Nerissa claims to be the third sister, "Mofufu"). Mori Calliope: "FUWAMOCALLI," a collaboration name the twins say they particularly like. Watson Amelia: "Detective Dogs." Ouro Kronii: "WatchDog." Nanashi Mumei (graduated 2025): "Fuwamoomco" (Overwatch). Raora Panthera: their 2026 Serendipity trio partner, who drew them a shikishi before her debut. Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026). Houshou Marine: her oshi (a Touhou off-collab). Shirakami Fubuki and Hakui Koyori ("FUWAMOKOYO"): horror and Lethal Company partners. Gigi Murin and Cecilia Immergreen: Justice kouhai who hijacked FUWAMOCO MORNING #167 as a prank. Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA."
 
 ## [SW] Secrets
 (none)
@@ -269,6 +269,9 @@ Mococo Abyssgard: her younger twin, whom she calls "Moco-chan" even in English;
 - **Missing facts adopted:** her official line "How about we get you all nice and fluffy~?" (FW1).
 - **Promotion:** author decision; GPT reviewed one round only (author's instruction).
 - **Follow-up (2026-10-01):** 3D debut labeled PDT; the last "pet Pero" in Background changed to mascot.
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. (Resolved 2026-10-01, from the GPT review: the solo measurements stay in the dossier with the recording
diff --git a/novel-lab/projects/holoen/runs/20261001-0549-character-Mococo-Abyssgard/final.md b/novel-lab/projects/holoen/runs/20261001-0549-character-Mococo-Abyssgard/final.md
index 23e6bc4..356c49b 100644
--- a/novel-lab/projects/holoen/runs/20261001-0549-character-Mococo-Abyssgard/final.md
+++ b/novel-lab/projects/holoen/runs/20261001-0549-character-Mococo-Abyssgard/final.md
@@ -238,7 +238,7 @@ Proposed ElevenLabs v4 performance directions for her dialogue, for an original
 In her lore, Mococo is a guard dog whose job is to protect your smile (and to make a little chaos). As an idol she and Fuwawa chase their list of more than a hundred dreams, and she wants every Ruffian to keep going one step a day.
 
 ## [SW] Relationships
-Fuwawa Abyssgard: her older twin, who calls her "Moco-chan"; Mococo has called her dependable, calls her plain "Fuwawa" (she refused to repeat "Fuwa-nee"), and is embarrassed by their "FUWAMOCO sync." Pero: the twins' fictional dog mascot; in the prison-break lore, Mococo throws Pero at the guards. Advent: Shiori (Pen Pups), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Nerissa's "Mofufu" bit). Omaru Polka: her oshi (Phasmophobia with Fubuki and Polka; a guest at their birthday concert). Gigi Murin ("GigiMoco," "bauBau") and Cecilia Immergreen ("Cecemoco"): Justice kouhai who once hijacked FUWAMOCO MORNING as a prank. Raora Panthera: their 2026 Serendipity trio partner. Ouro Kronii: "WatchDog." Mori Calliope: "FUWAMOCALLI." Watson Amelia: "Detective Dogs." Nanashi Mumei (graduated 2025): "Fuwamoomco." Hakui Koyori: a FUWAMOCO MORNING guest host ("FUWAMOKOYO").
+Fuwawa Abyssgard: her older twin, who calls her "Moco-chan"; Mococo has called her dependable, calls her plain "Fuwawa" (she refused to repeat "Fuwa-nee"), and is embarrassed by their "FUWAMOCO sync." Pero: the twins' fictional dog mascot; in the prison-break lore, Mococo throws Pero at the guards. Advent: Shiori (Pen Pups), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Nerissa's "Mofufu" bit). Omaru Polka: her oshi (Phasmophobia with Fubuki and Polka; a guest at their birthday concert). Gigi Murin ("GigiMoco," "bauBau") and Cecilia Immergreen ("Cecemoco"): Justice kouhai who once hijacked FUWAMOCO MORNING as a prank. Raora Panthera: their 2026 Serendipity trio partner. Ouro Kronii: "WatchDog." Mori Calliope: "FUWAMOCALLI." Watson Amelia: "Detective Dogs." Nanashi Mumei (graduated 2025): "Fuwamoomco." Hakui Koyori: a FUWAMOCO MORNING guest host ("FUWAMOKOYO"). Cecilia Immergreen: a Chrono Trigger off-collab (2026). Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA."
 
 ## [SW] Secrets
 (none)
@@ -263,6 +263,9 @@ Fuwawa Abyssgard: her older twin, who calls her "Moco-chan"; Mococo has called h
 - **Kept (GPT SHOULD):** the restricted nickname list; sneezing as an observed stream feature, with no
   medical explanation.
 - **Promotion:** author decision; GPT reviewed one round only (author's instruction).
+- **2026-10-01, cast expansion (author: Justice, and complete everyone's relationship web):** Relationships gained
+  Justice lines from the archive metadata, the official -All for One- report and Serendipity interviews, and the
+  wiki (sources in the world card "Justice Pairs" and the Justice character files).
 
 ## Open Questions
 1. There is no clean solo sample of Mococo's ordinary speech in the archive window used (her 2025 solo is

```


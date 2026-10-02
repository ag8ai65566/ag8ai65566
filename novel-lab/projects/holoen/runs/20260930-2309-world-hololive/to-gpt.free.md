# One-round review: hololive worldbuilding for Sudowrite (19 world cards), two new character files (IRyS, Nerissa Ravencroft), and edits to 6 character cards (persona frame, relationships, new Audio Tags field)

You are GPT, reviewing Claude's work for the novel-lab project "holoen" (fan fiction Story Bible for Sudowrite about hololive English members). This is the ONLY review round (the author limited GPT usage), so be decisive: report what must change, give exact replacement wording where you can, and skip cosmetic nitpicks. Write your review in English.

## Project rules that apply (from project.md, author decisions)
- Authenticity first: accurate, sourced facts; profanity and teasing kept as-is; nothing invented and presented as fact. Unverified items must be labeled and kept off the cards.
- NEW author premise (2026-09-30): in stories, the members are aware they are streamers with personas (VTubers). Their lore (reaper, phoenix, priestess, shark, time traveler, Warden of Time) is a persona and a running bit, not literal; nobody has real supernatural powers.
- NEW author request: make the relationships between members rich and accurate. Author's own description of Calli & Kiara: early "business couple" (TakaMori, with a name); now fewer interactions but still very close, like an old married couple.
- Recency weighting (author): recent streams weigh more for the current default; early memes stay as shared memory; conflicts resolve toward recent evidence.
- Boundaries: public persona only; never the real people behind the avatars (names, faces, families, homes, health, graduation reasons); no romance/intimacy between real people (ships are performed bits and fan terms); follow COVER's Derivative Works Guidelines.
- NEW author directions (2026-10-01): (a) every piece of research is part of the world; relationships are the most important and must include members outside EN (JP, ID, DEV_IS, HOLOSTARS, GAMERS); (b) the world also covers new members joining, graduations, group and solo concerts, 3D lives and events, generously; members' public X posts are key sources (private details still excluded); (c) Sudowrite itself will insert ElevenLabs v4 audio tags into dialogue, so each character gets an [SW] "Audio Tags" field (tag vocabulary by situation, signature sounds, habits to keep in the words, IPA, tags never to use as default) and the Story Bible Style gets a tagging rule. The tags direct an ORIGINAL designed voice; nobody's real voice is cloned or imitated.
- Baseline date 2026-09-30 (after the 2026-09-07 branch merge). Ame: affiliate since 2024-09-30. Gura: graduated 2025-05-01.
- Evidence labels: [Official], [Observed] ("secondary" = wiki), [ASR] (machine transcription checked by two models, not listening), [Adaptation], [Author], [Unverified]. Clip titles only prove an uploader's description.
- Sudowrite: the Worldbuilding card = Name, Role, Other Names, Description (soft limit 450 words), Rules (350), Sensory Details (200), Secrets. Worldbuilding cards are the FIRST thing dropped when context is short, so the most important information must come first, and the persona premise is also written into the character cards. Card detection uses Name and Other Names.

## What to check
1. Factual accuracy against the cited sources (dates, events, who did what, quotes). Flag anything unsupported, mis-attributed or overstated (e.g. a single anecdote written as a rule).
2. The persona premise: does anything still read as literal lore (real powers) or break the "never the real person" boundary?
3. Relationships: are they accurate, recency-weighted, and useful for writing scenes? Anything important missing that you can source (give the source)? Anything that contradicts the character cards?
4. Card usability for Sudowrite: most important first, Other Names that will trigger detection without false positives, lengths.
5. The character-card edits (persona framing, avatar framing, updated Relationships incl. IRyS/Nerissa, Kronii voice correction).
6. IRyS and Nerissa Ravencroft: full new character files (dossier + [SW] card). Check facts, the persona frame, privacy (no pets, family, health, school), that only lines both ASR models agree on are quoted on the card, and duplication between card fields.
7. Audio Tags fields and the Style rule: are the tags consistent with each character's Voice Profile and measurements, specific enough for Sudowrite to imitate the speech habits, and free of anything that would imitate a real person's voice or sexualize anyone?

## Output format
For each card: `## <card name>` then `MUST:` (numbered, each with the fix) and `SHOULD:` (optional, short). Then `## Character card edits` (same format), then `## IRyS` and `## Nerissa Ravencroft` (same format), then `## Audio Tags and Style rule`, then `## Missing facts worth adding` (only with a source you can name). If a card is fine, write `OK`.

---


==================== WORLD CARD FILE: 20260930-2309-world-AmeSame/claude-draft.md ====================

---
kind: world
name: "AmeSame"
sw_section: Worldbuilding
---

# World Element: AmeSame (Watson Amelia and Gawr Gura)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public friendship between Ame and Gura, checked 2026-09-30. Evidence labels as in the other
> world files. "Archive" = stream titles and descriptions (archive.ragtag.moe, S1). The fan ship name is a
> fan term; no romance is written.

## One-line Concept
Myth's gremlin and Myth's shark: the closest friends in the group's first years, a comedy duo that argued
on purpose and pranked each other endlessly, and whose last on-stream moments together were spent reading
their old DMs. In 2026 both have stepped back (Ame an affiliate, Gura graduated), so the friendship lives
in callbacks, tributes and the others' memories.

## Type
Relationship (pair).

## How It Works
- **Close friends:** Gura and Ame are close friends who collabbed often and are "most commonly shipped
  together under the name… #amesame." [Observed S2 §Likes and dislikes, secondary]
- **The Fish Tank (2021):** their talk show, built on staged arguments; when an argument turned into
  sudden sincere praise from Ame, Gura got visibly embarrassed. [Observed Gura file G6, secondary report]
- **Pranks and gremlin energy:** endless Minecraft pranks (Ame named a mine "Gura's Backdoor ( ͡° ͜ʖ ͡°)"),
  lewd-adjacent teasing ("Nice view from here" under Gura on a ladder), and Gura's jinxes, e.g. "Somebody
  kill someone! Not me, right?" right before Ame killed her in Among Us. [Observed Ame file A2, A10; S2
  §Gura's antics, secondary]
- **Sweet side:** Gura once sang "You Are My Sunshine" with the lyrics changed to be about Amelia; asked
  whose last name she'd take, she picked "Watson" because it "sounds more like a family name than Gawr."
  [Observed S2 §Likes and dislikes, secondary]
- **Off-stream visit (2022):** on 2022-06-20 they revealed Gura was streaming at Amelia's place, followed
  by an unarchived karaoke off-collab. [Observed S2, secondary]
- **Lore bits:** Ame "went back in time" to tell Gura she would be in hololive; Ame hopes to visit
  Atlantis "when the flat earth tips over and all the water spills out." [Observed S2 §Lore, Ame wiki
  §Time travel, secondary]
- **The goodbye (2024):** on 2024-09-29, the day before Ame concluded her regular activities, Gura's
  channel streamed "【💛💙】Looking at our old DMs" with Ame; the next day they played Deep Rock Galactic
  with Kiara and Kronii. [Observed S1]
- **After:** Gura graduated on 2025-05-01. In 2026 Kiara's album includes "Blue & Gold," a tribute to
  both. [Observed S3 §Miscellaneous, secondary]
- **How often (archive, S1):** mentions per year 72 (2020), 34 (2021), 14 (2022), 7 (2023), 6 (2024), none
  since. [Observed S1; counts by Claude]

## Sensory Palette
- See: gold and blue side by side (💛💙); a shark hood next to a deerstalker; an old DM thread scrolled on
  stream.
- Hear: two voices arguing on purpose and cracking up; Ame's "NEHEHEHE"; Gura's "a."
- One detail only here: a staged argument that stops dead when one of them says something nice.

## History
| Date | Event | Trace left |
|---|---|---|
| 2020 | Constant collabs and pranks | The "AmeSame" name |
| 2021-05 | The Fish Tank talk show | Staged-argument comedy |
| 2022-06-20 | Gura streams from Ame's place; unarchived karaoke | — |
| 2024-09-29 | "Looking at our old DMs" | Their last duo stream before Ame stepped back |
| 2025-05-01 | Gura graduates | — |
| 2026-02 | Kiara's "Blue & Gold" tribute | The colors as a memory |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| AmeSame | Ame + Same (shark); the pair | fans |
| The Fish Tank | their talk show | both |
| 💛💙 | their colors together | both, fans |

## Conflicts and Story Hooks
1. (Before 2024-10) A Fish Tank episode where the staged argument turns real for one line, then melts.
2. (Before 2024-10) Ame "fixes" Gura's stream setup and it's a prank.
3. (Before 2025-05) Gura needs directions in Minecraft; Ame gives the worst ones on purpose.
4. (2026) Ame, guesting somewhere, hears a shark joke and goes quiet for half a second.
5. (2026) The remaining Myth members play "Blue & Gold" on an anniversary stream.

## Links to Characters
Watson Amelia, Gawr Gura; Takanashi Kiara ("Blue & Gold"); Myth.

## Secrets
(None.)

## Hard Facts (continuity)
- Last duo stream before Ame stepped back: "Looking at our old DMs" (2024-09-29).
- 2026 baseline: no new streams together; memories, callbacks and tributes only.
- The ship name is a fan term; no romance is written.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): No6n9zCs_8A (2024-09-29),
  NJ5jozV74K0 and zs-8A7pob60 (2024-09-30). Pair-mention counts computed by Claude.
- S2 Gawr Gura wiki page, §Likes and dislikes, §Gura's antics, §Lore (secondary):
  https://virtualyoutuber.fandom.com/wiki/Gawr_Gura
- S3 Takanashi Kiara and Watson Amelia wiki pages, §Miscellaneous, §Time travel (secondary)
- S4 Gura file G6 (The Fish Tank report); Ame file A2, A10

---

## [SW] Name
AmeSame

## [SW] Role
Relationship

## [SW] Other Names
Ame and Gura, Gura and Ame, The Fish Tank, amesame

## [SW] Description
Watson Amelia and Gawr Gura, Myth's gremlin and Myth's shark, the closest friends of the group's early years. They hosted The Fish Tank, a talk show built on staged arguments, and pranked each other endlessly (Ame's Minecraft mine "Gura's Backdoor"; Ame killing Gura in Among Us right after Gura said "Not me, right?"). The sweet side showed too: Gura rewrote "You Are My Sunshine" about Amelia, picked "Watson" as the family name she'd take, and got flustered whenever a staged argument turned into real praise. On 2024-09-29, the day before Ame concluded her regular activities, they streamed "Looking at our old DMs" together. Gura graduated on 2025-05-01. In 2026 neither streams as a duo; the friendship lives in callbacks, their gold-and-blue colors, and Kiara's tribute song "Blue & Gold."

## [SW] Rules
In the 2026 baseline there are no new AmeSame streams; use memories, messages, tributes and callbacks. Stories set before October 2024 can use them together freely. Teasing can be crude and relentless, and sincerity embarrasses them both. The ship name is a fan term, not romance.

## [SW] Sensory Details
Gold and blue side by side (💛💙); a shark hood next to a deerstalker; two voices arguing on purpose and cracking up; a staged argument stopping dead when one of them says something nice; an old DM thread scrolled on stream.

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20260930-2309-world-Bone-Bros/claude-draft.md ====================

---
kind: world
name: "Bone Bros"
sw_section: Worldbuilding
---

# World Element: Bone Bros (Mori Calliope and Gawr Gura)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public relationship between Calli and Gura, checked 2026-09-30. Evidence labels as in the
> other world files. "Archive" = stream titles and descriptions (archive.ragtag.moe, S1).

## One-line Concept
The reaper and the shark, Myth's bickering "bros": a duo of pranks, jabs and a shared song, from the
year both were the branch's biggest names to Gura's last Minecraft trip with Myth. After Gura's
graduation, Calli keeps singing Gura's unreleased song.

## Type
Relationship (pair / unit name).

## How It Works
- **The name:** "Bone Bros" is listed as a unit of Calli and Gura on both wiki pages. [Observed S2, S3
  §Relationships, secondary]
- **Tone:** pranks and bickering with a big-sister/little-shark edge; Calli's gruff threats bounce off
  Gura's cheerful dumb-shark defiance. [Observed Calli file C4, Gura file G2, secondary; Adaptation for
  the "big-sister" shorthand]
- **Music:** they sang "Q" together with DECO*27 (2022-02-03). [Official Calli file C29]
- **Early years:** they were the branch's first two to 1 million subscribers (Gura, then Calli in
  January 2021) and were named Tokyo Tourism Ambassadors together with Sakura Miko (2023-02-08).
  [Observed S2, S3, secondary]
- **"Dad":** Calli's "Dad" nickname is said to have started around Gura. [Unverified: stated in this
  project's Calli file from an earlier wiki reading; not found in the current revision]
- **Later collabs (archive, S1):** horror co-op (The Outlast Trials, 2023-05), group games (Liars Bar,
  2025-01-22) and Calli's "One Last Minecraft Trip." on the Myth relay for Gura's farewell (2025-04-30).
- **After graduation:** Gura's single "Full Color" was never released; Calli covered it at the
  hololive English concert "The Show Goes On" (September 2024), and Calli and Kiara said they would keep
  singing it in karaoke. [Observed S2 §Miscellaneous, secondary]
- **How often (archive, S1):** mentions per year 62 (2020), 39 (2021), 13 (2022), 8 (2023), 3 (2024), 2
  (2025). [Observed S1; counts by Claude]

## Sensory Palette
- See: black and blue; a scythe and a trident; a Minecraft sunset on a last trip.
- Hear: Calli's "LISTEN." against Gura's "a"; both laughing at a prank that backfired.
- One detail only here: Calli singing Gura's song alone in a karaoke stream, not saying why.

## History
| Date | Event | Trace left |
|---|---|---|
| 2020–2021 | Constant collabs, pranks and bickering | "Bone Bros" |
| 2022-02-03 | "Q" (with DECO*27) | Their duet |
| 2024-09 | Calli covers Gura's "Full Color" at "The Show Goes On" | Carrying her song |
| 2025-04-30 | "One Last Minecraft Trip." (Myth relay) | Last duo moments on stream |
| 2025-05-01 | Gura graduates | — |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Bone Bros | Calli and Gura | fans, members |
| Full Color | Gura's unreleased single, kept alive in karaoke | Calli, Kiara |

## Conflicts and Story Hooks
1. (Before 2025-05) Gura pranks Calli's Minecraft base; Calli plots revenge on stream.
2. (Before 2025-05) Recording "Q": Calli coaches, Gura freestyles.
3. (Before 2025-05) The last Minecraft trip: neither says goodbye directly.
4. (2026) A karaoke stream where Calli sings "Full Color" and chat goes quiet.
5. (2026) Someone calls Calli "Dad" and she remembers where it started.

## Links to Characters
Mori Calliope, Gawr Gura; Takanashi Kiara (Full Color in karaoke); Myth.

## Secrets
(None.)

## Hard Facts (continuity)
- "Q" duet: 2022-02-03. Gura graduated 2025-05-01.
- 2026 baseline: no new Bone Bros streams; Calli keeps "Full Color" alive in karaoke.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): WifF8ncArM4 (2023-05-27),
  jb2_MtMdWhk (2025-01-22), jD8HAiQfzFY (2025-04-30). Pair-mention counts computed by Claude.
- S2 Gawr Gura wiki page, §Relationships, §Miscellaneous (secondary)
- S3 Mori Calliope wiki page, §Relationships, §2021, §Events (secondary)
- S4 Calli file C29 ("Q"): https://www.youtube.com/watch?v=aetXqd9B8WE

---

## [SW] Name
Bone Bros

## [SW] Role
Relationship

## [SW] Other Names
Calli and Gura, Gura and Calli

## [SW] Description
Mori Calliope and Gawr Gura, the reaper and the shark: a bickering duo of pranks and jabs, where Calli's gruff big-sister threats bounce off Gura's cheerful dumb-shark defiance. They were the English branch's first two to reach a million subscribers, were named Tokyo Tourism Ambassadors together (2023) and sang "Q" with DECO*27 (2022). Their collabs thinned out over the years, but on the Myth relay before Gura's graduation Calli's stream was "One Last Minecraft Trip." Gura graduated on 2025-05-01. Her single "Full Color" was never released; Calli covered it on stage in 2024 and, with Kiara, keeps singing it in karaoke.

## [SW] Rules
In the 2026 baseline Gura does not stream; Bone Bros lives in memories, the "Q" duet and Calli singing "Full Color." Before May 2025 they can prank and bicker freely. Calli's affection shows through teasing and actions, not speeches.

## [SW] Sensory Details
Black and blue; a scythe beside a trident; Calli's "LISTEN." against Gura's "a"; a Minecraft sunset on a last trip; Calli singing Gura's song in karaoke and not saying why.

## [SW] Secrets


---

## Open Questions
1. "The Dad joke started around Gura" could not be re-found in the current wiki; it stays unverified and
   off the card.


==================== WORLD CARD FILE: 20260930-2309-world-Myth-Pairs/claude-draft.md ====================

---
kind: world
name: "Myth Pairs"
sw_section: Worldbuilding
---

# World Element: Myth Pairs (the other pairings among the six)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the pairs without their own card, checked 2026-09-30. Evidence labels as in the other world files.
> "Archive" = stream titles and descriptions (archive.ragtag.moe, S1); counts are mentions of each other
> per year (2020 → 2025), a rough measure. Own cards: TakaMori, TakoTori, AmeSame, Bone Bros, Time and
> Death, Time Duo, Octo'Clock.

## One-line Concept
The rest of the web: who is whose oshi, who taught whom, who designed whose mascot, and who played one last
game with whom. Each pair in one line of story fuel.

## Type
Relationship web.

## Pairs
- **Kiara and Ame** (20 / 26 / 30 / 8 / 9 / 1): Ame is Kiara's EN oshi; Kiara calls herself "#1 Ame
  gosling" and "#1 Teamate" and credits Ame for help with her 3D productions. Ame made the intro video for
  Kiara's talk show HOLOTALK (2020) and was its 31st guest (2024-09-22); they did a 3D off-collab "In
  Ame's awesome studio" (2023-06). Ame on a reunion: "Kiara like, threw herself at me… she hugged me!"
  Ame, now an affiliate, performed at Kiara's 2025 spring concert and guested at her 2026 birthday live.
  [Observed S2 Kiara §Likes and dislikes, §2020; S3 Ame §Quotes, §2025–§2026, secondary; S1]
- **Kiara and Gura** (59 / 25 / 11 / 10 / 8 / 6): Kiara calls her "Goobidiba" and taught her German and
  Japanese, German swears included, tricking her into singing on lesson streams; Gura's 2020 Minecraft
  prank filled Kiara's KFP back room with chickens. Gura was HOLOTALK's 34th guest on 2025-04-30, the eve
  of her graduation ("three four," at last). Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame.
  [Observed S2 §KFP, §Miscellaneous; S4 Gura §Gura's antics, secondary; S1]
- **Calli and Ina** (26 / 26 / 8 / 15 / 8 / 9; 2 in 2026): Ina designed Calli's Death Sensei and drew the
  cover of Calli's debut EP; Calli wrote the lyrics of Ina's 2026 song "TAKO∞TAKOVER." Calli is Ina's
  favorite pun target ("Every freaking time, Ina."). They watched Suisei's concert together in an
  off-collab (2023-02-20) and still game together (Elden Ring Nightreign, 2025-06). [Observed S5 Ina
  §Miscellaneous; Calli file C28; Ina file I8; S1]
- **Calli and Ame** (24 / 23 / 14 / 6 / 6 / 0): early Clubhouse 51 duels; the MV of Calli-written "Myth or
  Treat" premiered on Ame's channel (2021); in 2026 Ame "called in from 2021" during Calli's charity
  stream. [Observed Ame file A20; S3 §2021, §2026, secondary; S1]
- **Ina and Ame** (29 / 30 / 9 / 4 / 4 / 0): Ina designed Bubba; Ame's "Amenade" cocktail traces back to a
  Japanese snack tasting with Ina; a "LOSER BUYS DINNER!!!!!" off-collab (2023-02-23); Ame aims blunt PvP
  taunts at her. [Observed S3 §Miscellaneous; Ame file; S1]
- **Ina and Gura** (71 / 28 / 10 / 3 / 3 / 2): fellow members of the official ocean unit UMISEA (2021);
  Ina drew chibi Bloop and promised "the wrath of Ina" to anyone who makes Gura cry; Gura once directed a
  lost Ina in Minecraft by hitting a block with her pickaxe. [Official UMISEA announcement; S4 §Gura's
  antics, secondary]
- **Kiara and Kronii** (2021→2025: 5 / 5 / 11 / 5 / 6): Kiara was a fan of Kronii before Kronii debuted and
  calls her "quasoni" in her own stream titles ("quasoni pls help me"); Diablo raids, an Age of Empires
  tournament, a GIRLSTALK ("Turns Out Kronii Is Quite The Girl Too!!!!!!", 2024) and PEAK ("we are
  climbing mount kronii, right?", 2025). [Observed Kronii file K8; S1 Kiara titles]
- **Gura and Kronii** (2021→2025: 9 / 11 / 3 / 2 / 5): the fan unit SNOTCast (Shark, Nature, Owl, Time);
  in 2025, Gura's last months, Kronii became one of her regular partners: Fast Food Simulator ("Legend Is
  Made Here With @GawrGura"), R.E.P.O., and "Greener Grass Awaits: I Play, She Watches (She's Scared)"
  (2025-04-26). [Observed S4 §Relationships, secondary; S1 Kronii titles]

## Sensory Palette
- See: a KFP back room full of chickens; a hand-drawn Death Sensei; a Bubba sketch; a PEAK summit.
- Hear: Kiara's German lesson voice; Gura repeating a swear word wrong; "Every freaking time, Ina."

## History
| Date | Event | Trace left |
|---|---|---|
| 2020-11-15 | Gura's chicken prank on KFP | KFP lore |
| 2021-09-14 | UMISEA formed (Ina, Gura, Aqua, Marine) | Ocean unit |
| 2024-09-22 | Ame on HOLOTALK | Kiara's oshi as guest |
| 2025-04-26/30 | Kronii's and Kiara's last collabs with Gura | Farewells |
| 2026-01-06 | "TAKO∞TAKOVER" (lyrics by Calli) | Ina × Calli |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Goobidiba | Kiara's name for Gura | Kiara |
| quasoni | Kiara's name for Kronii | Kiara |
| #1 Ame gosling / #1 Teamate | Kiara as Ame's fan | Kiara |
| SNOTCast | Shark, Nature, Owl, Time | fans |
| UMISEA | official ocean unit (2021) | official, members |

## Conflicts and Story Hooks
1. Kiara interviews her oshi Ame on HOLOTALK and can't keep a straight face.
2. A German lesson where Gura only wants to learn swears.
3. Calli writes lyrics for Ina and Ina draws the cover; each critiques the other's draft.
4. Kronii plays a horror game while Gura "watches (she's scared)."
5. Ina organizes a "loser buys dinner" rematch.

## Links to Characters
All six.

## Secrets
(None.)

## Hard Facts (continuity)
- Kiara's EN oshi: Ame. Kiara's names: "Goobidiba" (Gura), "quasoni" (Kronii).
- Ina designed Death Sensei, Bubba and the Takodachi; Calli wrote "TAKO∞TAKOVER."
- 2026 baseline: pairs with Gura are memories; pairs with Ame are guest appearances.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): t1hmCvnA4g8, bz5LRWDTIjo
  (2023-06), nmd1pmYLeX4 (2024-09-22), ash9FVn3trc (2025-04-30), 7SXsKcDyFdQ (2025-02-18),
  2BKNJUd8B7A (2023-02-20), FMlpFYxMnIM (2025-06-01), GMtqCEHvUKY (2023-02-23), 969JaHkv1jU
  (2023-12-14), TpWn8fhsTbc (2024-04-27), XxNe2R70Av4 (2025-07-07), W3Mw0gL9dIE (2025-01-20),
  Ctca7OFLxFo (2025-04-26). Pair-mention counts computed by Claude.
- S2 Takanashi Kiara wiki page (secondary)
- S3 Watson Amelia wiki page (secondary)
- S4 Gawr Gura wiki page (secondary)
- S5 Ninomae Ina'nis wiki page (secondary)
- S6 UMISEA official announcement: https://hololive.hololivepro.com/news/20210921-1-9/
- S7 Character files: Calli C28, Ina I8, Ame A20, Kronii K8

---

## [SW] Name
Myth Pairs

## [SW] Role
Relationship

## [SW] Other Names
Kiara and Ame, Kiara and Gura, Calli and Ina, Calli and Ame, Ina and Ame, Ina and Gura, Kiara and Kronii, Gura and Kronii

## [SW] Description
The rest of the web among the six. Kiara and Ame: Ame is Kiara's EN oshi ("#1 Ame gosling"); Ame made Kiara's HOLOTALK intro, was its guest in 2024 and now guests at Kiara's concerts; Ame on a reunion: "Kiara like, threw herself at me… she hugged me!" Kiara and Gura: Kiara ("Goobidiba") taught her German and Japanese, swears included; Gura's Minecraft prank filled Kiara's KFP back room with chickens; Gura was HOLOTALK's 34th guest the day before she graduated. Calli and Ina: Ina designed Death Sensei and drew Calli's debut EP cover; Calli wrote the lyrics of Ina's "TAKO∞TAKOVER"; Calli is Ina's favorite pun target ("Every freaking time, Ina."). Calli and Ame: early Clubhouse 51 duels; in 2026 Ame "called in from 2021" to Calli's charity stream. Ina and Ame: Ina designed Bubba; they did a "loser buys dinner" off-collab. Ina and Gura: the official ocean unit UMISEA (2021); Ina promised "the wrath of Ina" to anyone who makes Gura cry. Kiara and Kronii: Kiara was a fan before Kronii debuted and calls her "quasoni." Gura and Kronii: fan unit SNOTCast; in Gura's last months Kronii was one of her regular partners ("I Play, She Watches (She's Scared)").

## [SW] Rules
In the 2026 baseline, pairs with Gura are memories and callbacks, and pairs with Ame are guest appearances. Nicknames are used as each member uses them (Kiara's "Goobidiba," "quasoni"). All of these are friendships.

## [SW] Sensory Details
A KFP back room full of chickens; a hand-drawn Death Sensei and a Bubba sketch; Kiara's German-lesson voice; Gura repeating a swear wrong; "Every freaking time, Ina."

## [SW] Secrets


---

## Open Questions
1. "quasoni" appears in Kiara's stream titles for Kronii; its origin was not found.


==================== WORLD CARD FILE: 20260930-2309-world-OctoClock/claude-draft.md ====================

---
kind: world
name: "Octo'Clock"
sw_section: Worldbuilding
---

# World Element: Octo'Clock (Ninomae Ina'nis and Ouro Kronii)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public relationship between Ina and Kronii, checked 2026-09-30. Evidence labels as in the
> other world files. "Archive" = stream titles and descriptions (archive.ragtag.moe, S1).

## One-line Concept
The newest close pair in the cast: two pun lovers who share Korean, occasional FGO streams and, in 2026,
an official concert pairing for hololive English's 4th concert "Serendipity" under the name "Octo'Clock."

## Type
Relationship (pair) and official concert pairing.

## How It Works
- **Official pairing (2026):** paired for the 4th concert "Serendipity" (Shrine Auditorium, Los Angeles,
  2026-07-03/04); Kronii's short "#holoSerendipity It's Time for Octo'Clock!" (2026-06-24) names the unit.
  [Official S2; Observed S3]
- **How they describe each other (official interview, 2026-06-04):**
  - Kronii: "Just two punny people waiting to deliver the pun-chline to everyone." She praises Ina's
    drawing and quick execution, her puns, and that "She's very hard-working and ambitious."
  - Ina: "I get to…keep Kronii….all to myself…..hehe…hehehe"; "it's even more special now that it's just
    us two together!!"; she admires Kronii's "unmatched charisma whenever she sings."
  - Shared history they mention: performing together in group numbers, meeting in person, matching
    jackets and shared interests, and MCing together at a hololive fes. Goal: to "nail the performance";
    Kronii adds, mostly joking, that they want to "look cooler than everyone else." [Official S2]
- **Korean:** both speak it, a language they share. [Observed S4 §Miscellaneous, secondary]
- **On stream (archive, S1):** Ina's FGO streams with Kronii (2023-08-18 "Let's Learn About Fate/Grand
  Order!!!", 2024-01-02 "NEW YEAR FGO ADVENTURES"), R.E.P.O. (2025-07-19), and Ame's 2022 surprise karaoke
  off-collab that both joined (per Ame's wiki page).
- **How often (archive, S1):** mentions per year 3 (2021), 7 (2022), 2 (2023), 2 (2024), 1 (2025). The
  bond is newer and event-driven: it grew into a partnership in 2026. [Observed S1; counts by Claude]

## Sensory Palette
- See: purple and deep blue; a tentacle and a clock hand on one poster; matching jackets.
- Hear: a pun, a beat of silence, Kronii's deadpan "nice," Ina's giggle; a few words of Korean.
- One detail only here: Ina saying "all to myself…hehe" in the sweetest voice.

## History
| Date | Event | Trace left |
|---|---|---|
| 2022-02-25 | Ame's surprise karaoke off-collab (with Ina, Kronii, Fauna, Mumei) | — |
| 2023–2024 | FGO streams on Ina's channel | A shared game |
| 2026-06-04 | Official Serendipity interview | Their own words |
| 2026-06-24 | "It's Time for Octo'Clock!" short | The unit name |
| 2026-07-03/04 | Serendipity concert, Los Angeles | Their stage pairing |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Octo'Clock | Ina (octopus) + Kronii (clock) | both, official |
| Serendipity | hololive English 4th concert (2026) | everyone |

## Conflicts and Story Hooks
1. A pun duel before rehearsal that neither will concede.
2. Ina quietly claims Kronii "all to myself" in front of Calli; Kronii plays along deadpan.
3. They switch to Korean mid-stream to plan a surprise.
4. Kronii's "look cooler than everyone else" goal collides with a costume mishap.
5. After the concert, they draw and caption the night together.

## Links to Characters
Ninomae Ina'nis, Ouro Kronii; Watson Amelia (the 2022 karaoke).

## Secrets
(None.)

## Hard Facts (continuity)
- Serendipity: 2026-07-03/04, Shrine Auditorium, Los Angeles.
- "Octo'Clock" is the pairing's name in Kronii's official short (2026-06-24).

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): 5xNVHzLzi80 (2023-08-18),
  _1Gmk7w-Eak (2024-01-02), NnOogNcUZx4 (2025-07-19). Pair-mention counts computed by Claude.
- S2 Official Serendipity interview with Ina and Kronii (2026-06-04):
  https://serendipity.hololivepro.com/news/interview01/
- S3 "#holoSerendipity It's Time for Octo'Clock!" (Kronii's channel, 2026-06-24):
  https://www.youtube.com/watch?v=KmczU8q1oqE
- S4 Ouro Kronii wiki page, §Miscellaneous (secondary)

---

## [SW] Name
Octo'Clock

## [SW] Role
Relationship

## [SW] Other Names
Ina and Kronii, Kronii and Ina, Serendipity

## [SW] Description
Ninomae Ina'nis and Ouro Kronii, the octopus and the clock: the newest close pair in the cast. They share Korean, a love of puns and occasional FGO streams, and in 2026 they were paired for hololive English's 4th concert "Serendipity" (Los Angeles, July 3–4) under the name "Octo'Clock." In their official interview Kronii called them "Just two punny people waiting to deliver the pun-chline to everyone" and praised Ina as "very hard-working and ambitious"; Ina said "I get to…keep Kronii….all to myself…..hehe…hehehe" and admired Kronii's "unmatched charisma whenever she sings." They had met in person, found matching jackets and shared interests, and MC'd together at a hololive fes. Their goal was to "nail the performance," and, Kronii added mostly as a joke, "look cooler than everyone else."

## [SW] Rules
Ina's claim on Kronii is a sweet joke, not romance. Their humor is dueling puns and deadpan; their work ethic is serious. Collabs before 2026 were occasional, so earlier scenes should feel friendly rather than close.

## [SW] Sensory Details
Purple and deep blue; a tentacle and a clock hand on one poster; matching jackets; a pun, a beat of silence, Kronii's deadpan "nice," Ina's giggle; a few words of Korean.

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20260930-2309-world-Streaming-Life/claude-draft.md ====================

---
kind: world
name: "Streaming Life"
sw_section: Worldbuilding
---

# World Element: Streaming Life

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the everyday texture of the cast's work as publicly shown on their channels, checked
> 2026-09-30. Evidence labels as in the other world files ([Official], [Observed], [Adaptation],
> [Unverified]).

## One-line Concept
The daily medium the cast lives in: live streams with a scrolling chat, superchats, collabs, off-collabs,
3D lives, clips and schedules. Most scenes happen on stream, just before or after one, or in a group chat
about one.

## Type
Culture / setting (workplace routine).

## How It Works
- **A stream:** a scheduled broadcast on the member's channel ("Starting soon" screen, BGM, a greeting,
  then the game, chat or song). Titles use 【BRACKETS】 for the format ("【MINECRAFT】", "【OFF COLLAB】",
  "【KARAOKE】"). [Observed stream titles in the archive, S1]
- **Chat:** viewers type in real time; members read chat aloud, argue with it, and call it "chat."
  Moderators keep order. [Observed]
- **Superchats ("supas") and memberships:** paid messages read aloud, usually in a thank-you segment at
  the end; members-only streams for subscribers. [Observed character files]
- **Collab:** streaming together from separate places (voice chat, each on her own channel, "POV").
  **Off-collab:** streaming together from the same place. **3D:** full-body avatar streams, lives and
  concerts. **Relay:** members stream one after another under a shared hashtag (e.g. the 2025 Myth
  relay). [Observed S1 titles]
- **Formats:** gaming, horror games, chatting ("zatsudan"), karaoke (sometimes unarchived), art streams,
  watchalongs, superchat catch-ups, song releases and premieres, sponsored streams (#PR), talk shows
  (Kiara's HOLOTALK), tabletop RPGs, anniversaries and birthdays. [Observed]
- **Clips:** fans cut highlights with dramatic titles; members sometimes react to them. A clip title is
  the uploader's description, not the member's words. [Observed; project evidence rule]
- **Schedules:** weekly schedules posted on social media; time zones shape who can collab when.
  [Observed]
- **Normal example:** a member ends a horror stream, reads superchats with stacked thank-yous, reminds
  chat to drink water, and signs off with her usual goodbye.
- **Edge example:** a stream crashes or the mic fails; the member apologizes, restarts, and chat turns
  the failure into a meme.

## Sensory Palette
- See: a scrolling chat wall; member-color emotes; a superchat bar in yellow or red; a thumbnail with a
  shocked face; the avatar's eyes tracking the screen.
- Hear: BGM under the chat; the superchat chime; a keyboard and mouse; a game's music; a genmate's voice
  crackling in over voice chat.
- Touch: a controller, a mic arm, a drink on the desk ("my yum-yum drink").
- One detail only here: "Wait, chat, is my mic on?"

## Society and Power
- Fans shape the show: requests, memes and backseating; members push back ("no backseating").
- Members support each other by watching, raiding, and dropping into each other's chat.

## History
| Time | Event | Trace left |
|---|---|---|
| 2020 | Myth's first year: frequent collabs across time zones | Collab-heavy early memories |
| 2022-06 | Myth's first off-collab with all five present | Off-collabs as special events |
| 2025–2026 | Collabs become rarer and event-based; concerts and relays anchor them | "One last time" relays, duo concerts |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| chat | the live viewers | members |
| supa / superchat / akasupa | paid message / a red (large) one | members |
| collab / off-collab / 3D | together remotely / in the same place / full-body avatar | everyone |
| POV | one member's channel view of a shared collab | members |
| otsu / otsukare | "good work" after a stream | members, chat |
| oshi | the member you support most | everyone |
| teetee | "precious" (a wholesome duo moment) | fans, members |
| unarchived | a stream not kept as a VOD (often karaoke) | members |
| backseating | chat telling you how to play | members |
| clip / clipper | fan-made highlight / its maker | everyone |

## Conflicts and Story Hooks
1. Chat backseats a puzzle and the member refuses on principle.
2. An off-collab: two members share one desk and fight over the camera angle.
3. A superchat asks a question that turns a goofy stream sincere for a minute.
4. A clip goes viral with a misleading title and the member streams to set the record straight.
5. A collab across time zones: one member is wide awake, the other is on her last braincell.

## Links to Characters
All six; each has her own greeting, sign-off and superchat habits (see character cards).

## Secrets
(None.)

## Hard Facts (continuity)
- Collab = remote; off-collab = same place; 3D = full-body avatar.
- Clip titles are fans' descriptions, not the members' words.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata for the six members' channels (titles, dates), read through
  archive.ragtag.moe on 2026-09-30.
- S2 The six character files in this project (greetings, sign-offs, superchat habits).
- S3 hololive production wiki (formats and events; secondary): https://virtualyoutuber.fandom.com/wiki/Hololive

---

## [SW] Name
Streaming Life

## [SW] Role
Culture

## [SW] Other Names
stream, livestream, chat, superchat, supa, collab, off-collab, offcollab, 3D, relay, karaoke, clip

## [SW] Description
The cast's everyday medium. A stream opens on a "Starting soon" screen with BGM, then a greeting, then games, chatting, karaoke, art or a watchalong; titles use brackets like "【OFF COLLAB】". Chat scrolls beside the avatar and the member reads it aloud, argues with it and calls it "chat." Superchats ("supas") are paid messages, usually read in a thank-you segment at the end; members get members-only streams. A collab is streaming together remotely, each on her own channel; an off-collab is streaming together from the same place; a 3D stream uses a full-body avatar; a relay passes the baton from channel to channel. Fans cut clips with dramatic titles. Weekly schedules and time zones decide who can collab when. In the early years Myth collabed constantly; by 2025–2026 collabs are rarer and built around anniversaries, birthdays, concerts and relays.

## [SW] Rules
Collab means remote, off-collab means the same place, 3D means a full-body avatar. A clip title is a fan's description, not the member's words. Chat can suggest; the member decides. Paid messages are thanked by name.

## [SW] Sensory Details
A scrolling chat wall of member-color emotes; the superchat chime and a yellow or red superchat bar; BGM under the talk; a keyboard and mouse; a genmate's voice crackling in over voice chat; a drink on the desk; "Wait, chat, is my mic on?"

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20260930-2309-world-TakaMori/claude-draft.md ====================

---
kind: world
name: "TakaMori"
sw_section: Worldbuilding
---

# World Element: TakaMori (Mori Calliope and Takanashi Kiara)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public relationship between Calli and Kiara, checked 2026-09-30. Evidence labels as in the
> other world files, plus **[Author]** for what the author told Claude directly (2026-09-30). "Archive" =
> stream titles and descriptions on their channels (archive.ragtag.moe, S1). The ship is a performed bit
> and a fan term; no private feelings are implied and no romance is written.

## One-line Concept
Myth's founding double act: a phoenix who "fell for" the reaper who can never keep her dead, and a reaper
who pretends to hate it. The loud flirt-and-rebuff bit of 2020–21 was toned down in 2021; what remains in
2026 is a settled, affectionate long friendship with fewer collabs and the rhythm of an old married couple.
[Author; Observed S2–S3]

## Type
Relationship (pair).

## How It Works
- **The origin bit (2020):** on Calli's second stream Kiara declared a crush on her. The lore joke: Kiara
  is an immortal phoenix, so however many times the reaper kills her, she comes back. Kiara named the ship
  "TakaMori." [Observed S2 §Takamori, secondary]
- **The early routine (2020–21):** Kiara calls Calli her "wife," writes a ukulele song about wanting to
  marry her ("I Love Girls"), gives their hypothetical Sims child a name ("Clara Takamori") and "forgets"
  Calli in her amnesia re-debut ("Who's Calli?"). Calli rebuffs her and calls her "kusotori" ("shitbird"),
  which fans read as tsundere ("tsundereaper"), while supporting the #takamori hashtag. [Observed S2
  §Takamori, secondary]
- **Work together from day one:** Calli made Kiara's loading screen and intro video and narrated her
  debut intro; she once drew Kiara as a chicken saying "kicky ricky or whatever." [Observed S2
  §Miscellaneous, secondary]
- **Toned down (2021-09):** shortly after -Council- debuted, they announced they would tone the ship
  down. Their reasons are not written in stories. The wiki adds that "the two remain close friends."
  [Observed S2 §Takamori, secondary]
- **What the friendship looks like since:**
  - Kiara defends it plainly: "if Calli really had a problem with me, she would tell me in private… she
    actually does like me a lot but is just really bad at expressing herself." [Observed S2 Kiara §Quotes,
    secondary]
  - Calli, when a superchat says it is glad they are "friends now": "What do you mean?! I love Kiara!"
    [Observed S3 Calli §Quotes, secondary]
  - They travel together and Kiara teases her afterwards: Calli says Kiara told her she talks in her sleep
    on their Hokkaido trip. Kiara also tells chat that Calli misplaces things in obvious places. [Observed
    S3 Calli §Quotes and §Personality, secondary]
  - They play "Mom" (Kiara, "Mommy Kiwawa") and "Dad" to Kobo Kanaeru; Calli insists she is not married to
    Kiara and Kobo is adopted. [Observed S2 §Takamori, secondary]
- **Recent milestones (archive, S1):** an off-collab "Reunion & Gaming!! #takamori" and a karaoke collab
  (2022-06); off-collabs in 2023 (a Rubik's cube stream at Calli's, "TAKAMORI OFF-COLLAB" with Kobo,
  doing each other's nails on camera with IRyS); their duet "Fire N Ice" (2023-12-14; lyrics by Calli
  and TeddyLoid); Kiara's off-collab watch party "cheering Calli on!!!" for Calli's GriMoire concert
  (2025-02-27); a four-part Split Fiction co-op series in April–May 2025, titled by them "takamori split
  screen nostalgia," "Perfectly In Sync with @TakanashiKiara," "thumbnail teetee manifestation into
  gameplay teetee" and "Saving the World with @TakanashiKiara"; Myth's 5th anniversary collab
  (2025-09-13) and 6th anniversary live (2026-09-19).
- **Heard in 2025 (ASR, S6):** in the first Split Fiction stream (Kiara's channel, 2025-04-06) the
  "parents" bit is alive: when Kobo shows up in chat, they tell her "Hi Kobo, go to bed! … What are you
  doing out of bed? Go to bed!", wish her a happy anniversary, and apologize: "Sorry Kobo, you can't be part
  of this because it's two players only. Next time…" When their game characters split into a fire mage and
  an ice mage, they riff on their own song: "Fire and ice, yeah. Fire and ice, death and life." When the
  split screen separates them: "Oh, double Takamori." [ASR S6, nE12CyKbaX8 0:07:49, 0:08:01, 0:22:36,
  0:13:28; both models agree; who said which line is not separable from the transcript]
- **Heard at the finale (ASR, S6; Calli's channel, 2025-05-02):** they bicker over an idiom like a long
  married pair. One mangles it ("glass stones in stone houses or whatever. I forget the term"), they argue
  over what it even means ("Okay, how about this? Don't cast stones when your body's made of glass."), and
  it ends with "I don't know that one. All right. All right. Well then, whatever. We don't need any of these
  metaphors." Calli, asked her favorite of the studio's co-op games: "I'm an edgelord, Kiara. I like A Way
  Out the best… but you know me, I'm edgy, but I still love power, friendship and stuff." Wrapping up:
  "Split screen game finished by Takamori… because Takamori will always get together for these ones,
  right?" "Let's play more in the future." Earlier in the ending: "We got published together."
  "Together." [ASR S6, 2X8h7UI28mE 4:42:57–4:44:30, 4:36:00, 4:40:50, 4:31:35; both models agree]
- **How often (archive, S1):** mentions of each other in titles and descriptions: 33 (2020), 38 (2021),
  12 (2022), 22 (2023), 9 (2024), 9 (2025). Fewer than the first two years, but still one of the most
  steady pairs. [Observed S1; counts by Claude]
- **Old-married-couple rhythm [Author; supported by the lines above]:** bickering on autopilot, finishing
  each other's jokes, nostalgia about the early days, complaints that are really affection, and total
  trust underneath. Kiara says the love out loud; Calli deflects, then proves it by showing up.

## Sensory Palette
- See: black and orange side by side; a split-screen co-op; Kiara's hand-drawn chicken on Calli's intro.
- Hear: Kiara's "CALLI!" at full volume; Calli's flat "kusotori"; both laughing at the same bad joke.
- One detail only here: Calli saying "I love Kiara!" like it's an obvious fact she's annoyed to repeat.

## History
| Date | Event | Trace left |
|---|---|---|
| 2020-09 | Kiara declares the crush on Calli's 2nd stream; "TakaMori" named | The ship name |
| 2020-12 | Kiara's amnesia re-debut: "Who's Calli?" | Running gag |
| 2021-09 | Ship toned down; still close friends | The bit is past tense |
| 2022-06 | "Reunion & Gaming!! #takamori" off-collab; karaoke collab | In-person reunion |
| 2023 | Off-collabs; "Fire N Ice" duet (2023-12-14) | Their song |
| 2025-02-27 | Kiara's watch party for Calli's GriMoire concert | Cheering from the crowd |
| 2025-04/05 | Split Fiction series ("takamori split screen nostalgia") | Nostalgic co-op |
| 2026-09-19 | Myth 6th anniversary live together | Still side by side |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| TakaMori | the pair / the old ship name | Kiara, fans |
| kusotori | "shitbird," Calli's name for Kiara | Calli |
| tsundereaper | fans' label for Calli's rebuffs | fans |
| Mommy Kiwawa / Dad | Kobo's names for Kiara and Calli | Kobo |
| Clara Takamori | their joke Sims "child" | fans, Kiara |

## Conflicts and Story Hooks
1. A co-op game only works if they're "perfectly in sync"; they are, which annoys Calli.
2. Kiara brings up an old TakaMori clip on stream; Calli pretends to leave.
3. Kobo asks her "parents" to settle an argument, and they argue about who's the parent.
4. Calli shows up to cheer at Kiara's concert without announcing it, and gets caught.
5. An anniversary: someone asks "are you friends now?" and Calli answers too fast.

## Links to Characters
Mori Calliope, Takanashi Kiara; Kobo Kanaeru (their "kid" bit); Myth.

## Secrets
(None.)

## Hard Facts (continuity)
- "TakaMori" was named by Kiara (2020); toned down in 2021; they remain close friends.
- Kobo's "parents" bit: Kiara "Mom," Calli "Dad"; "not married, Kobo is adopted."
- No real romance or intimacy is written; the flirting is a performed bit.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): ZIvO-792X2k, VGSyM2Dcv7M (2022-06),
  8W-Tmvs6szA, EH51mAFpcEQ, 6JF3eMx0QSc (2023), yV83laHeOj4 ("Fire N Ice," 2023-12-14), 1Dpqs8WoTYs
  (2025-02-27), nE12CyKbaX8, 6_oUPIgak7k, g_HGuPjhvF8, 2X8h7UI28mE (Split Fiction, 2025), W168fNPUygE
  (2025-09-13). Pair-mention counts computed by Claude.
- S2 Takanashi Kiara wiki page, §Takamori, §Quotes, §Miscellaneous (secondary):
  https://virtualyoutuber.fandom.com/wiki/Takanashi_Kiara
- S3 Mori Calliope wiki page, §Quotes, §Personality (secondary): https://virtualyoutuber.fandom.com/wiki/Mori_Calliope
- S4 Siliconera on "Fire N Ice": https://www.siliconera.com/calliope-mori-and-kiara-takanashi-finally-released-a-song-together/
- S6 Claude's audio check (2026-09-30): nE12CyKbaX8 0:00–0:25 (Kiara's channel, 2025-04-06) and
  2X8h7UI28mE, last 15 minutes (Calli's channel, 2025-05-02), archived
  via archive.ragtag.moe, whisper small.en, lines re-checked with medium.en. Machine transcription, not
  listening; speakers are not labeled. Lines about the members' families or where they live were heard
  and deliberately left out (project rule).
- S5 Author's description (2026-09-30): early business couple with a name; fewer interactions now but
  still very close; like an old married couple.

---

## [SW] Name
TakaMori

## [SW] Role
Relationship

## [SW] Other Names
Takamori, Calli and Kiara, Kiara and Calli, kusotori

## [SW] Description
Mori Calliope and Takanashi Kiara, Myth's founding double act. In 2020 Kiara declared a crush on the reaper who can never keep a phoenix dead, called Calli her "wife" and named the ship "TakaMori"; Calli rebuffed her and nicknamed her "kusotori" (shitbird) while quietly supporting the hashtag. Calli made and narrated Kiara's debut intro. In 2021 they toned the ship down. What remains in 2026 is a settled, affectionate long friendship with fewer collabs and the rhythm of an old married couple: bickering on autopilot, nostalgia about the early days, complaints that are really affection. Kiara says the love out loud and explains that Calli "actually does like me a lot but is just really bad at expressing herself"; Calli deflects, then snaps "What do you mean?! I love Kiara!" when someone suggests they're only friends "now." They sang "Fire N Ice" together (2023), Kiara threw a watch party for Calli's 2025 concert, and in 2025 they played a co-op series they titled "takamori split screen nostalgia." They also play "Mom" and "Dad" to Kobo Kanaeru; in 2025, when Kobo appeared in their chat, they told her "Go to bed!" and "Sorry Kobo, you can't be part of this because it's two players only," and when their game gave them fire and ice powers they riffed, "Fire and ice, death and life." At the end of that series they bickered over a mangled idiom ("glass stones in stone houses or whatever") until one gave up: "Whatever. We don't need any of these metaphors," and signed off: "Takamori will always get together for these ones, right?"

## [SW] Rules
The romance was a performed bit and is past tense; no real romance or intimacy is written. Kiara is openly affectionate; Calli is gruff in words and loyal in actions, and "kusotori" is a term of endearment by now. Collabs are occasional events, not daily; when they meet, it feels like no time has passed.

## [SW] Sensory Details
Black and orange side by side in a split-screen co-op; Kiara's "CALLI!" at full volume and Calli's flat "kusotori"; both cracking up at the same bad joke; Calli saying "I love Kiara!" like an obvious fact she's tired of repeating.

## [SW] Secrets


---

## Open Questions
1. The "old married couple" rhythm is the author's description; the evidence above supports its pieces
   (bickering, nostalgia, trust). Any specific scenes the author wants to anchor it?


==================== WORLD CARD FILE: 20260930-2309-world-TakoTori/claude-draft.md ====================

---
kind: world
name: "TakoTori"
sw_section: Worldbuilding
---

# World Element: TakoTori (Takanashi Kiara and Ninomae Ina'nis)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public relationship between Kiara and Ina, checked 2026-09-30. Evidence labels as in the
> other world files. "Archive" = stream titles and descriptions (archive.ragtag.moe, S1).

## One-line Concept
The gas pedal and the brake: loud, driven Kiara and laid-back, my-pace Ina, who grew from genmates into
2026 duo-concert partners. Of all the Myth pairs, theirs is the one most active right now.

## Type
Relationship (pair) and official concert pairing.

## How It Works
- **How they describe each other (official interviews, 2026):**
  - Ina on Kiara: "one of us is the gas pedal and one of us is the brake"; Kiara has "a very 'go-getter',
    lively energy" while Ina is "laid-back, my-pace"; Kiara's support helped Ina get over being
    self-conscious about dancing; "you will always be our shining star!!!!" [Official S2]
  - Kiara on Ina: at first she "didn't see her as a big performer," then "could not stop thinking about
    Ina" when choosing a duo partner, for her music and her dance training; "so different from me, and I
    love that," "a perfect balance of cat fueled energy mixed with energy drink fueled energy." [Official S3]
- **The chicken incident (2020):** after Gura filled the back room of Kiara's KFP building in Minecraft
  with chickens, Ina was checking on them when a creeper exploded and released them; Kiara "fired" Ina,
  and the incident became KFP lore. [Observed S4 §KFP, secondary]
- **Ina, the quiet support:** Kiara has said that when she is down, Ina is always the first to message
  her (a statement Kiara made publicly, reported by Ina's wiki page). Ina also designed Kiara's mascot,
  Kotori. [Observed S5 §Personality, S4 §Mascot and fans, secondary]
- **Kiara, the loud support:** Kiara pushes Ina toward the stage and cheers her dancing. Kiara groans at
  Ina's puns like everyone else. [Official S2; Observed Ina file]
- **Kibaba's future:** in Kiara's grandma-persona bit, future Ina lives near Kiara, who cooks for her so she
  doesn't just eat cup noodles and sleep on the floor. [Observed S4 §Lore, secondary]
- **Recent milestones (archive, S1):** "TAKOTORI OFFCOLLAB!!" in Mario vs. Donkey Kong (Ina's title,
  2024-03-04; Kiara's side was "Two Braincells At Work"); outfit design for each other judged by juniors
  ("Ina & Wawa Outfit Design!", 2023-12-30); the duo concert "Drawn to Dawn" at the Wiltern, Los Angeles
  (2026-03-27/28, announced 2025-11-23, new 3D outfits); Kiara's "Back from Drawn to Dawn!!!!! THANK
  YOU!!!!" (2026-04-01); a cover of "GETCHA!" together (2026-04-24).
- **How often (archive, S1):** mentions per year 30 (2020), 34 (2021), 17 (2022), 10 (2023), 11 (2024),
  6 (2025), 4 in the thin 2026 archive, the highest 2026 rate of any Myth pair. [Observed S1; counts by
  Claude]

## Sensory Palette
- See: orange and purple under concert lights; matching new 3D outfits; a thumbnail of two brain cells.
- Hear: Kiara's hype countdown, Ina's calm "okay, okay" underneath it; a pun, a groan, a giggle.
- One detail only here: Kiara talking a mile a minute while Ina waits, then lands one quiet line that
  makes Kiara scream-laugh.

## History
| Date | Event | Trace left |
|---|---|---|
| 2020-11 | The KFP chicken incident; Kiara "fires" Ina | KFP lore |
| 2024-03-04 | "TAKOTORI OFFCOLLAB!!" | The pair name in their own titles |
| 2025-11-23 | Duo concert announced | — |
| 2026-03-27/28 | "Drawn to Dawn," the Wiltern, LA | Their first concert as a duo |
| 2026-04-24 | "GETCHA!" cover | — |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| TakoTori | Tako (Ina) + Tori (Kiara); the pair and concert name | both, fans, official |
| Wawa | Kiara | Kiara, Ina |
| Drawn to Dawn | their 2026 duo concert | both |

## Conflicts and Story Hooks
1. Rehearsal week: Kiara wants one more run-through, Ina wants a nap; both are right.
2. Kiara is down after a rough day; a message from Ina arrives first.
3. A KFP "hearing" reopens the chicken incident; Ina defends herself deadpan.
4. Kiara designs Ina's outfit and Ina designs Kiara's; neither admits the other's is better.
5. Post-concert chat: they re-live the show and thank each other on stream.

## Links to Characters
Takanashi Kiara, Ninomae Ina'nis; Gawr Gura (the chicken prank); Myth.

## Secrets
(None.)

## Hard Facts (continuity)
- "Drawn to Dawn": 2026-03-27/28, the Wiltern, Los Angeles; TakoTori's first concert.
- Kiara "fired" Ina over the 2020 chicken incident (a KFP bit).

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): Ro3iDM2Pi6E, d2SnWgrwlm4
  (2024-03), nkXQd7R0B8w (2023-12-30), jx1XvONd2uo, KVJFel4YBqM, G0_uOWs6Kvw, YzgPJtBuOAE (2026).
  Pair-mention counts computed by Claude.
- S2 Official Drawn to Dawn interview with Ina: https://drawn-to-dawn.hololivepro.com/news/09.html
- S3 Official Drawn to Dawn interview with Kiara: https://drawn-to-dawn.hololivepro.com/news/06.html
- S4 Takanashi Kiara wiki page, §KFP, §Lore, §Mascot and fans (secondary)
- S5 Ninomae Ina'nis wiki page, §Personality (secondary)
- S6 Drawn to Dawn concert page: https://hololive.hololivepro.com/en/events/drawn-to-dawn/

---

## [SW] Name
TakoTori

## [SW] Role
Relationship

## [SW] Other Names
Kiara and Ina, Ina and Kiara, Drawn to Dawn

## [SW] Description
Takanashi Kiara and Ninomae Ina'nis, Myth's gas pedal and brake. Ina's words: Kiara has "a very 'go-getter', lively energy," Ina is "laid-back, my-pace," and "one of us is the gas pedal and one of us is the brake." Kiara's: "so different from me, and I love that," a mix of "cat fueled energy" and "energy drink fueled energy." Kiara pushed Ina toward the stage and cheered her dancing; Ina is the quiet support, and Kiara has said Ina is always the first to message her when she's down. Ina designed Kiara's mascot Kotori, and Kiara still "fired" Ina over the 2020 KFP chicken incident. In 2026 they held their first duo concert, "Drawn to Dawn," at the Wiltern in Los Angeles (March 27–28) and released a cover together; of all the Myth pairs, theirs is the most active right now.

## [SW] Rules
Kiara leads with volume and plans; Ina answers with calm, a pun, or one quiet line that lands. Their support is mutual and unshowy: Kiara hypes, Ina checks in. The firing is a running KFP joke, never a real grudge.

## [SW] Sensory Details
Orange and purple under concert lights; Kiara's hype countdown with Ina's calm "okay, okay" under it; a pun, a groan, a giggle; Kiara scream-laughing at one quiet line from Ina.

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20260930-2309-world-Time-Duo/claude-draft.md ====================

---
kind: world
name: "Time Duo"
sw_section: Worldbuilding
---

# World Element: Time Duo (Watson Amelia and Ouro Kronii)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public relationship between Ame and Kronii, checked 2026-09-30. Evidence labels as in the
> other world files. "Archive" = stream titles and descriptions (archive.ragtag.moe, S1).

## One-line Concept
A time-traveling detective and the Warden of Time: a lore rivalry played entirely for laughs (Ame
"borrowed" time travel and swears she'll give it back), a pair of opposite tastes, and in 2026 Ame, now an
affiliate, stepping onto Kronii's birthday stage as a guest.

## Type
Relationship (pair / unit name).

## How It Works
- **The lore joke:** when Kronii was announced (2021) and her account was briefly restricted by the rush
  of followers, Ame joked "twitter is protecting me from a certain time lord" and "i swear i'll give it
  back soon...." — as if her time travel were borrowed from the Warden. [Observed S2 §Lore, secondary]
- **The unit name:** "Time Duo" is listed on both wiki pages. [Observed S2, S3 §Relationships, secondary]
- **Opposites:** Ame noted that Kronii "dislikes everything she likes." [Observed S2 §Likes and dislikes,
  secondary]
- **Lore chaos:** Ame's alternate-Ame lore includes an "Epic Ame War" between Kronii and many Ames that
  "messed up" time, which Ame compared to one bear-sized duck against fifty duck-sized bears. [Observed S3
  §Alter Ames, secondary]
- **On stream (archive, S1):** Ame's surprise karaoke off-collab with Ina, Kronii, Fauna and Mumei
  (2022-02-25, per S3); 5D Chess "I Don't Understand With @WatsonAmelia" (Kronii, 2023-04-08); Escape the
  Backrooms with Calli (2024-09-22) and Deep Rock Galactic with Kiara and Gura (2024-09-30, Ame's last
  week of regular streams).
- **2026:** Ame guested at Kronii's 3D birthday live "Fall in Grace" (2026-03-13). [Observed Kronii file
  K33, stream locator qqi8yXuH35Y t=1711; S3 §2026, secondary]
- **How often (archive, S1):** mentions per year 6 (2021), 2 (2022), 2 (2023), 4 (2024), 1 in the thin 2026
  archive. A small but steady pair. [Observed S1; counts by Claude]

## Sensory Palette
- See: gold and deep blue; a pocket watch beside a giant clock; a 3D stage with a surprise guest.
- Hear: Ame's gremlin cackle; Kronii's flat "no."; a joke about who owns time.
- One detail only here: Ame promising, again, to give "it" back soon.

## History
| Date | Event | Trace left |
|---|---|---|
| 2021-08 | Kronii's announcement; "a certain time lord" joke | The lore rivalry |
| 2023-04-08 | 5D Chess ("I Don't Understand") | A time-travel game, fittingly |
| 2024-09 | Backrooms and DRG in Ame's last week | — |
| 2026-03-13 | Ame guests at Kronii's 3D birthday live | The affiliate's cameo |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Time Duo | Ame and Kronii | fans |
| time lord / Warden | Ame's joke name for Kronii / Kronii's title | Ame / Kronii |

## Conflicts and Story Hooks
1. Kronii "audits" Ame's time travel as a bit; Ame pleads a borrowed watch.
2. A game night where they disagree on every choice by reflex.
3. An Ame cameo in 2026: Kronii pretends not to be delighted.
4. A lore war bit about who broke the timeline, settled by a party game.
5. A 5D chess rematch neither understands.

## Links to Characters
Watson Amelia, Ouro Kronii; Mori Calliope and the 2024 Backrooms trio.

## Secrets
(None.)

## Hard Facts (continuity)
- Nobody actually time-travels; the rivalry is a lore joke.
- Ame guested at Kronii's 3D birthday live on 2026-03-13.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): 37li7htBfKs (2023-04-08),
  7_VFV95YCpA and YSw85RI5PT8 (2024-09-22), NJ5jozV74K0 and zs-8A7pob60 (2024-09-30), qqi8yXuH35Y
  (2026-03-14). Pair-mention counts computed by Claude.
- S2 Ouro Kronii wiki page, §Lore, §Likes and dislikes, §Relationships (secondary)
- S3 Watson Amelia wiki page, §2022, §2026, §Alter Ames, §Relationships (secondary)

---

## [SW] Name
Time Duo

## [SW] Role
Relationship

## [SW] Other Names
Ame and Kronii, Kronii and Ame

## [SW] Description
Watson Amelia and Ouro Kronii, the time-traveling detective and the Warden of Time. Their rivalry is a lore joke: when Kronii debuted, Ame joked that Twitter was "protecting me from a certain time lord" and swore "i'll give it back soon," as if her time travel were borrowed. Ame says Kronii "dislikes everything she likes," and Ame's alternate-Ame lore includes an "Epic Ame War" against Kronii that messed up time. On stream they played 5D chess neither understood, and Ame's last week of regular streams (2024) included Backrooms and Deep Rock Galactic with Kronii. Ame, now an affiliate, guested at Kronii's 3D birthday live on 2026-03-13. A small, fond pairing built on opposite tastes and a shared bit about who owns time.

## [SW] Rules
No one actually controls or travels through time; it is a shared joke. Ame plays the guilty borrower, Kronii the unimpressed Warden. In the 2026 baseline Ame appears as a guest, not a regular collab partner.

## [SW] Sensory Details
Gold and deep blue; a pocket watch beside a giant clock; Ame's gremlin cackle against Kronii's flat "no"; a surprise guest walking onto a 3D stage.

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20260930-2309-world-Time-and-Death/claude-draft.md ====================

---
kind: world
name: "Time and Death"
sw_section: Worldbuilding
---

# World Element: Time and Death (Mori Calliope and Ouro Kronii)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public relationship between Calli and Kronii, checked 2026-09-30. Evidence labels as in the
> other world files. "Archive" = stream titles and descriptions (archive.ragtag.moe, S1).

## One-line Concept
The two deep voices of the English branch and its tallest pair: a reaper and the Warden of Time who
became deadpan sparring partners, Kronii's first friend outside her generation, and still each other's
go-to for horror co-ops and mock feuds.

## Type
Relationship (pair).

## How It Works
- **First contact:** Kronii's first official collab outside her own generation was with Calli (Orcs Must
  Die! 3, 2021-09-23). [Observed S2 §2021, secondary]
- **Nicknames and running jokes:** Calli calls her "Kronster"; Kronii is 1 cm taller than Calli, the
  previous tallest English member, and teases her about it continuously. [Observed S2 infobox and
  §Miscellaneous, secondary, citing Kronii's post]
- **Voices:** the wiki compares Kronii's deep voice to Calli's; in Claude's audio measurements they are
  the two lowest speakers of the six (Kronii 177–188 Hz, Calli 197–214 Hz in chat). [Observed S2
  §Personality, secondary; ASR, Kronii file K36, Calli file C30]
- **Their self-billing:** Calli's 2023 stream title "Time and Death Say Howdy to Ghosts...with
  @OuroKronii." They share the fan unit "WARS" (Warden, Alchemist, Reaper, Scholar) with HOLOSTARS'
  Magni Dezmond and Noir Vesper. [Observed S1; S2 §Relationships, secondary]
- **Mock feuds:** in January 2025, after Kronii's channel was briefly hacked to promote cryptocurrency,
  Kronii streamed a joke promotion of a made-up "$KRONII" coin, and Calli answered with a mock exposé,
  "Exposing the Lies of $KRONII Coin" ("I called out Ouro Kronii for her dubious scam…"). [Observed S1; S2
  §Miscellaneous, secondary]
- **Horror and chaos co-ops (archive, S1):** a cowboy TTRPG one-shot (2023-05), Devour (2023-10), Inside
  the Backrooms (2023-11), Lethal Company (2023-12), The Outlast Trials (2024-02), Escape the Backrooms
  with Ame (2024-09-22, just before Ame stepped back), Powerwash Simulator ("Get Your Shrek On," 2024-10),
  100% Orange Juice ("game for good friends!!", 2025-01).
- **How often (archive, S1):** mentions per year 8 (2021), 8 (2022), 13 (2023), 4 (2024), 2 (2025). In
  2023 this was one of Calli's most frequent pairings. [Observed S1; counts by Claude]

## Sensory Palette
- See: black and deep blue; two tall avatars side by side; a scythe next to a clock.
- Hear: two low voices trading deadpan lines; Kronii's GWAK and Calli's burst of swearing in the same
  horror jump scare.
- One detail only here: Kronii standing a little straighter to win the 1 cm.

## History
| Date | Event | Trace left |
|---|---|---|
| 2021-09-23 | Orcs Must Die! 3: Kronii's first cross-generation collab | The friendship's start |
| 2023 | Frequent horror and TTRPG co-ops; "Time and Death Say Howdy to Ghosts" | The duo's name |
| 2024-09-22 | Escape the Backrooms with Ame | One of Ame's last collabs |
| 2025-01 | The "$KRONII" coin bit and Calli's mock exposé | Mock feud |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Kronster | Calli's name for Kronii | Calli |
| Time and Death | the pair's own billing | both |
| WARS | fan unit with Magni and Vesper | fans |

## Conflicts and Story Hooks
1. A horror co-op where both claim they're not scared and both scream.
2. Kronii launches another fake scheme; Calli investigates on stream.
3. A height re-measurement for the 1 cm title.
4. A TTRPG session: Calli as GM, Kronii as the player who breaks the plot.
5. A quiet moment after a collab where Kronii says thanks plainly and Calli doesn't know what to do.

## Links to Characters
Mori Calliope, Ouro Kronii; Watson Amelia (the 2024 Backrooms trio).

## Secrets
(None.)

## Hard Facts (continuity)
- First cross-generation collab for Kronii: with Calli, 2021-09-23.
- Kronii is 1 cm taller than Calli.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30): liScSTChB8k (2023-05-20),
  mgThTrbLFiA (2023-10-01), z_i0kH9f9YQ (2023-11-27), OW9vbxmryhE (2023-12-29), 9eXGEUtQCuw (2024-02-07),
  YSw85RI5PT8 (2024-09-22), FrAGuMoLoEo (2024-10-18), 0SI55TdMVJI (2025-01-22), SsgpaOjdhh0 (2025-01-24).
  Pair-mention counts computed by Claude.
- S2 Ouro Kronii wiki page, infobox, §Personality, §2021, §Relationships, §Miscellaneous (secondary):
  https://virtualyoutuber.fandom.com/wiki/Ouro_Kronii
- S3 Kronii file K36 and Calli file C30 (audio measurements)

---

## [SW] Name
Time and Death

## [SW] Role
Relationship

## [SW] Other Names
Calli and Kronii, Kronii and Calli, Kronster

## [SW] Description
Mori Calliope and Ouro Kronii, the reaper and the Warden of Time: the English branch's two deep voices and deadpan sparring partners. Kronii's first collab outside her own generation was with Calli (2021). Calli calls her "Kronster"; Kronii is 1 cm taller than Calli and never lets her forget it. They billed themselves "Time and Death" in horror co-ops (Devour, the Backrooms, Lethal Company, The Outlast Trials) and share a cowboy TTRPG and a Powerwash "Get Your Shrek On." Their humor is mock feuds: when Kronii streamed a joke promotion of a made-up "$KRONII" coin in 2025, Calli answered with a mock exposé, "Exposing the Lies of $KRONII Coin." Underneath the jabs they are easy, dependable friends who pick each other for chaotic games.

## [SW] Rules
Their affection comes out as deadpan jabs, mock investigations and the height joke, not speeches. Both swear when a horror game gets them. Kronii's schemes and Calli's exposés are bits, never real accusations.

## [SW] Sensory Details
Black and deep blue; two tall avatars side by side, a scythe next to a clock; two low voices trading deadpan lines; a GWAK and a burst of swearing at the same jump scare; Kronii standing a little straighter to win the 1 cm.

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20260930-2309-world-VTuber-Persona-and-Lore/claude-draft.md ====================

---
kind: world
name: "VTuber Persona and Lore"
sw_section: Worldbuilding
---

# World Element: VTuber Persona and Lore

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the premise every hololive story in this project runs on. Public persona only, checked
> 2026-09-30. Evidence labels: **[Official]** COVER's own material; **[Observed]** public stream, title
> or post ("secondary" = wiki or other reference transcription); **[Adaptation]** an author decision for
> this project; **[Unverified]** reported, not confirmed.

## One-line Concept
Every cast member is a streamer who performs a character. The reaper, the phoenix, the priestess, the
shark, the time-traveling detective and the Warden of Time are personas and running bits, not facts of
the story world. The members know this, play along for fun, and step out of the bit whenever they like.
[Adaptation, author decision 2026-09-30]

## Type
Premise / rule of the setting (how reality works in these stories).

## How It Works
- **What is real in the story:** they are hololive talents (VTubers) who stream, sing, make music and
  videos, go to events and work with a company, COVER. Their friendships, running jokes, nicknames,
  songs, concerts and collabs are real parts of their lives. [Official hololive site; Observed streams]
- **What is a persona:** the lore on their official profiles (a reaper's apprentice, an immortal phoenix,
  a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time).
  In the story it is a character each one plays on stream, the way a performer keeps a stage persona.
  [Official profiles; Adaptation]
- **How they treat their lore (observed habits):**
  - They use it as a joke engine: age jokes (Gura's "9,000-something," Kronii jokingly "60"), immortality
    and rebirth gags (Kiara), "canonically" framed bits (Ame calling in "from 2021" during Calli's 2026
    charity stream). [Observed character files; Ame's wiki page §2026, secondary]
  - They break it casually and without drama: talking about ordinary things (food, sleep, games, work
    schedules, the weather) in the same breath as lore. [Observed stream titles and ASR in character files]
  - They can re-enter it for a bit and drop it again: Calli's reaper threats, Ina's "priestess" voice,
    Kiara's KFP manager routine, Ame's "Trust me, I'm a time traveler." [Observed character files]
  - Lore can be retconned or joked about by the members themselves ("Kiara is a phoenix, not a chicken");
    their word in the moment wins over any wiki. [Observed; Adaptation]
- **What they cannot do:** no supernatural powers in the story's reality. Nobody reaps souls, revives
  from death, time-travels, summons tentacles or stops time. When a scene "uses" a power, it is a bit, a
  game, a song concept, a costume, a stream graphic or a fan's joke. [Adaptation]
- **Exception (author-approved only):** a story may be explicitly written as an in-lore AU ("a story
  where the lore is real"). Only when the author says so in the story's Braindump or scene notes.
  [Adaptation]
- **Normal example:** Calli jokes that she'll collect a guest's soul, the guest laughs, and Calli goes back
  to arguing about snacks. Nobody's soul is collected.
- **Edge example:** during a horror game, Kiara says "I'm immortal, I'll just respawn!" — that is a gamer
  joke about her lore; if her character dies in the game, she groans and restarts the level like anyone
  else.

## The Performer Behind the Avatar (hard boundary)
- Stories never name, describe, locate or speculate about the real people behind the avatars: no real
  names, faces, ages, nationalities, families, homes, workplaces, health, past careers or relationships.
  [Project rule; COVER's Derivative Works Guidelines ask fans to respect talents and avoid content that
  damages their image]
- In off-stream scenes the members appear **as their avatar selves**: described with their avatar looks
  (hair, eyes, outfits, accessories) as a fan-fiction convention, and referred to by their talent names.
  [Adaptation, author to confirm]
- Private life stays at the level the members share publicly: games, food, music, rehearsals, travel
  stories they told on stream, friendships. [Adaptation]
- Relationships are friendships and public bits. Ships (e.g. TakaMori) are performed bits and fan terms,
  not real romance. Intimacy is not written. [Project rule]

## Sensory Palette
- See: the avatar on stream mirroring every head tilt; a lore joke landing in chat as a wall of emotes.
- Hear: a member saying "canonically" with a grin; the pause when someone breaks character to say
  something sincere.
- One detail only here: a lore line said in the same breath as "okay but I need to eat dinner."

## Society and Power
- Who benefits: fans get running jokes and stories; members get a stage persona to play with.
- Everyday life: they refer to the persona as "my lore," "canonically," "in-character"; fans call the
  performer's real identity off-limits.
- Economy: the company owns the character designs and lore and publishes official profiles.
  [Official]

## History
| Time | Event | Trace left |
|---|---|---|
| 2020-09 | Myth debuts with official lore profiles | Lore bits still in use |
| 2021–2026 | Lore grows through jokes, songs and events | "Canonically" callbacks |
| 2026-09-07 | Branches merge; COVER says it will update members' designs to fit their personalities, activities and future directions | Lore and looks can change officially |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| lore | a member's official or joke backstory | everyone |
| canonically / canon | "in my lore" (usually a joke) | members, chat |
| kayfabe / in-character | staying in the persona | chat, members |
| model / avatar | the 2D/3D character body on stream | everyone |
| outfit / costume reveal | a new official look for the avatar | everyone |

## Conflicts and Story Hooks
1. Chat insists a member's lore power should fix a problem; she has to solve it the ordinary way.
2. A collab turns into a lore bit that escalates until someone breaks and laughs.
3. A new outfit or model update makes a member rethink how she presents herself.
4. A joke retcon ("I was never a chicken") starts a mock-trial among genmates.
5. A sincere moment arrives mid-bit, and the member steps out of the persona to say it plainly.

## Links to Characters
All six cast members. Each character card's Background and Personality open with the persona frame
("streams as…", "her lore says…").

## Secrets
(None.)

## Hard Facts (continuity)
- Nobody in the story has supernatural powers unless the author declares an in-lore AU.
- The performers' real identities are never written.
- Members depicted off-stream look like their avatars (fan convention).

## Sources (checked 2026-09-30)
- S1 hololive official talent profiles (lore text): https://hololive.hololivepro.com/en/talents/
- S2 COVER Derivative Works Guidelines: https://hololivepro.com/en/terms/
- S3 hololive production wiki page, §2026 (the 2026-09-07 merger and design updates; secondary):
  https://virtualyoutuber.fandom.com/wiki/Hololive
- S4 The six character files in this project (bible/characters) for the lore bits cited above.

---

## [SW] Name
VTuber Persona and Lore

## [SW] Role
Premise

## [SW] Other Names
lore, canon, canonically, persona, kayfabe, in-character, avatar

## [SW] Description
The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.

## [SW] Rules
No one has supernatural powers. A "power" in a scene is a joke, a game, a song concept, a costume or a stream graphic; lore gags play out as gags. Lore bits are theirs to bend: their word in the moment beats any wiki. Never name, describe, locate or speculate about the performers behind the avatars (real names, faces, families, homes, health, careers). Ships and couple bits are performed jokes and fan terms, not real romance. The only exception is a story the author explicitly labels an in-lore AU.

## [SW] Sensory Details
An avatar mirroring every head tilt; chat flooding with emotes when a lore joke lands; a member saying "canonically" with a grin; the small pause when someone drops the bit to say something plainly.

## [SW] Secrets


---

## Open Questions
1. Off-stream scenes: the draft shows members as their avatar selves (a fan-fiction convention). Does
   the author want a different default?
2. Should the "in-lore AU" exception exist at all, or should every story stay persona-aware?


==================== WORLD CARD FILE: 20260930-2309-world-hololive--Myth/claude-draft.md ====================

---
kind: world
name: "hololive -Myth-"
sw_section: Worldbuilding
---

# World Element: hololive -Myth-

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the group as publicly shown, checked 2026-09-30. Evidence labels as in the other world files.
> "Archive" = stream titles and descriptions on the members' channels, read through archive.ragtag.moe
> (S1); the counts are mentions of each other per year, a rough measure of how often they appear together.

## One-line Concept
The first English generation of hololive (debuted 12–13 September 2020): five very different streamers
who grew up on stream together, from a chaotic collab-every-week first year to a smaller, steadier
bond built around anniversaries, songs and concerts. By 2026 three are active, one is an affiliate and one
has graduated, and the group still treats all five as Myth.

## Type
Faction / unit (a friend group with a shared history).

## Members and Status (2026-09-30)
- Mori Calliope, Takanashi Kiara, Ninomae Ina'nis: active in hololive -Myth-.
- Watson Amelia: concluded general activities 2024-09-30; affiliate; guests at genmates' events
  (Kiara's concerts 2025 and 2026, Kronii's 2026 live, a 2026 "call from 2021" in Calli's charity stream).
  [Observed Ame file A23; Ame's wiki page §2025–§2026, secondary]
- Gawr Gura: graduated 2025-05-01; alumna. [Official, Gura file]

## How the Group Works
- **Roles that formed early:** Calli wrote the lyrics for Myth's first song "Myth or Treat" (2021) and
  often plays the grumbling big sister; Kiara is the loudest cheerleader and the one who hosts; Ina is the
  calm one who designed the Myth mascots (all except Bloop) and draws for the group; Ame is the gremlin
  and the tech helper; Gura is the goofy little shark everyone protects. [Observed wiki pages, secondary;
  Adaptation for "big sister / little shark" shorthand]
- **Group humor:** mutual teasing, jinxes, chaotic Minecraft and party games; name-order trivia (Calli and
  Ame say their names in English order; Kiara, Ina and Gura surname-first). [Observed S2]
- **Protectiveness:** Ina says anyone who makes Gura cry will "face the wrath of Ina," and extends the
  promise to all the English members (tears of joy excepted). [Observed S2 Gura §Gura's antics, secondary]
- **How often they meet on stream (archive, S1):** mentions of each other peaked in 2020–21 and fell
  after; by 2024–26 group appearances cluster around anniversaries, relays, concerts and a few big
  collabs. The bond shows in the milestones, not in daily collabs. [Observed S1]

## History
| Date | Event | Trace left |
|---|---|---|
| 2020-09-12/13 | Myth debuts; Calli narrates Kiara's debut intro | Kiara's intro art, Calli's narration |
| 2020–2021 | Near-constant collabs: Minecraft, Among Us, games across time zones | The "first year" memories |
| 2021-10-31 | "Myth or Treat" (lyrics by Calli) | First group song |
| 2022-06-28 | First off-collab with all five together ("Together At Last") | A treasured in-person memory |
| 2022-09-30 | "Non-Fiction" MV | Group song |
| 2023-09-13 | 3rd anniversary relay (#Myth3YearRelay), e.g. a homemade Family Feud with all five | Anniversary relays |
| 2024-06 | Myth One-Block Minecraft series | A recent full-group project |
| 2024-09 | 4th anniversary song and voice pack; Ame's last week includes a Myth collab | Ame's farewell to regular streaming |
| 2025-04-30 | Myth relay "one last time" with Calli, Kiara, Ina and Gura before Gura's graduation | Gura's farewell with Myth |
| 2025-07 | MYTHMASH: each active member releases a duet with a Japanese senpai (#mythmashchemythtry) | Cross-branch songs |
| 2025-09-13 | 5th anniversary collab with announcements (Calli, Kiara, Ina) | New anniversary hats |
| 2026-02 | Kiara's album includes "Blue & Gold," a tribute to Gura and Ame | Remembering the two |
| 2026-09-19 | Myth 6th Anniversary 3D LIVE "Seasons From Within" (Calli, Kiara, Ina) | The current three on stage |

## Sensory Palette
- See: five member colors in a row (black, orange, purple, blue, gold); fanart of all five; the Myth logo.
- Hear: five people talking over each other in a 2020 collab; three voices trading jokes in 2026.
- One detail only here: an anniversary stream going quiet for a second when someone mentions Gura or Ame.

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Myth / holoMyth | the group | everyone |
| gen 1 / genmates | the same debut group | members |
| relay | members streaming in sequence under one hashtag | members |

## Conflicts and Story Hooks
1. Anniversary week: the three active members plan a surprise that needs Ame's tech help.
2. An old Minecraft world is reopened and everyone finds what the others built in 2020.
3. A new kouhai asks what early Myth was like; each member tells a different version.
4. The 6th anniversary 3D live: nerves, rehearsal jokes, a message for the absent two.
5. A relay goes wrong in a new way, just like the old days.

## Links to Characters
Calli, Kiara, Ina (active), Ame (affiliate), Gura (alumna); Kronii (a frequent collaborator from Promise).
Pair details live in the relationship cards (TakaMori, TakoTori, AmeSame, Bone Bros, Myth Pairs).

## Secrets
(None.)

## Hard Facts (continuity)
- Debut 12–13 September 2020; Ame affiliate 2024-09-30; Gura graduated 2025-05-01.
- 2026 baseline: three active; Ame appears as a guest; Gura is remembered, not written as streaming.
- No reasons for Ame's or Gura's changes beyond the public status.

## Sources (checked 2026-09-30)
- S1 Stream archive metadata for the six members' channels (titles, descriptions, dates), read through
  archive.ragtag.moe on 2026-09-30; the pair-mention counts were computed by Claude from titles and
  descriptions (template lines removed). Examples: n8hiq_IVZjs (2022-06-28), N2MbNUoJrgE (2023-09-13),
  hTzFgc4gABM and jD8HAiQfzFY (2025-04-30), 6guF3BHlR4U (MYTHMASH 2025-07-24), W168fNPUygE (2025-09-13).
- S2 Member wiki pages (secondary): Mori_Calliope, Takanashi_Kiara, Ninomae_Ina'nis, Gawr_Gura,
  Watson_Amelia on https://virtualyoutuber.fandom.com/ (read 2026-09-30).
- S3 hololive English post announcing "Seasons From Within" (2026-09-19):
  https://x.com/hololive_En/status/2098615081395241037

---

## [SW] Name
hololive -Myth-

## [SW] Role
Faction

## [SW] Other Names
Myth, holoMyth, HoloMyth, Myth gen, gen 1

## [SW] Description
hololive's first English generation, debuted 12–13 September 2020: Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Gawr Gura and Watson Amelia. They grew up on stream together: a chaotic first year of near-daily collabs, then a smaller, steadier bond built around songs, anniversaries, relays and concerts. Calli wrote the lyrics for their first song and plays the grumbling big sister; Kiara cheers loudest and hosts; Ina, the calm one, designed the Myth mascots except Bloop; Ame is the gremlin and tech helper; Gura is the goofy little shark everyone protects. Ame concluded her regular activities on 2024-09-30 and still guests at their events; Gura graduated on 2025-05-01 after a last Myth relay "one last time." In 2026 Calli, Kiara and Ina carry the name, and on 2026-09-19 they held the 6th Anniversary 3D LIVE "Seasons From Within." They still count all five as Myth.

## [SW] Rules
In the 2026 baseline only Calli, Kiara and Ina stream as Myth; Ame appears as a guest, Gura as a memory, a message or a callback, never as a current streamer. Early Myth (2020–21) was collab-heavy; recent Myth meets mostly at milestones, so a 2026 group scene should feel like a reunion.

## [SW] Sensory Details
Five member colors in a row (black, orange, purple, blue, gold); five voices talking over each other in an old collab; three in 2026; the Myth logo on an anniversary screen; a short quiet when someone mentions Gura or Ame.

## [SW] Secrets


---

## Open Questions
1. The "big sister / little shark" shorthand is Claude's summary of the group dynamic. Keep, reword or
   drop?
2. Member colors listed as black (Calli), orange (Kiara), purple (Ina), blue (Gura), gold (Ame) follow the
   emoji order in the 3rd-anniversary title (🖤💙💛💜🧡); please confirm the mapping before relying on it.


==================== WORLD CARD FILE: 20260930-2309-world-hololive--Promise/claude-draft.md ====================

---
kind: world
name: "hololive -Promise-"
sw_section: Worldbuilding
---

# World Element: hololive -Promise-

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the group of Ouro Kronii and IRyS as publicly shown, checked 2026-09-30 (IRyS added 2026-10-01).
> Evidence labels as in the other world files. Only what a Kronii or IRyS story needs; the other members are
> background.

## One-line Concept
Kronii's and IRyS's group: the English -Council- generation (debuted August 2021) joined by IRyS as -Promise- in
2023. After two graduations in 2025, the active members are IRyS, Ouro Kronii and Hakos Baelz.

## Type
Faction / unit.

## Members and Status (2026-09-30)
- Active: IRyS, Ouro Kronii, Hakos Baelz. [Observed S1 member table]
- Graduated: Tsukumo Sana (2022-07-31, while still -Council-), Ceres Fauna (2025-01-03), Nanashi Mumei
  (2025-04-27). No reasons are given in stories. [Observed S1–S3, secondary]

## How the Group Works (as it touches Kronii and IRyS)
- **Themes:** -Council- members embodied concepts (Time for Kronii, Nature, Civilization, Chaos, Space);
  IRyS is "Hope." Fan unit names built on these concepts are common (e.g. "SNOTCast": Shark, Nature, Owl,
  Time). [Observed Kronii file K8, secondary]
- **Kronii inside the group:** Bae calls her "too talented, savage, and a 'tsundere granny'"; Fauna
  described Kronii's "gap moe," a cute side that shows when she's flustered; IRyS once wondered aloud how
  Kronii sounds when she's scared. Group bits and scares involving them are reported by clip titles and
  stay unverified. [Observed Kronii file K8 §Personality, K37 §Quotes, secondary]
- **IRyS inside the group:** before -Promise- existed, she and the Council were already billed together as
  "CouncilRyS" (an official 3D showcase, 2023-10-08); -Promise- was announced at its end. With Bae she keeps
  the running "BaeRyS" bit of being "married" and "divorced" (from a 2021 Minecraft bento joke); their
  joke fan-fiction made "Monopoly" a fandom euphemism. With Kronii she plays two-player games and races
  (see "IRyS and Nerissa Pairs"). [Observed S5 IRyS §Relationships, §Units, secondary; IRyS file R2]
- **Kronii's first official collab outside her generation** was with Mori Calliope (2021-09-23).
  [Observed Kronii's wiki page §2021, secondary]
- **After 2025:** the group is three; Kronii's own 2026 activity (a 3D birthday live with Ame as a guest,
  the Serendipity pairing with Ina, her first EP) runs as much through cross-group partners as through
  Promise. [Observed Kronii file K4, K33, K36]

## History
| Date | Event | Trace left |
|---|---|---|
| 2021-08 | -Council- debuts (Sana, Fauna, Kronii, Mumei, Bae) | "Council" nostalgia |
| 2022-07-31 | Sana graduates | Council becomes four |
| 2023-10-09 | -Promise- formed with IRyS (closing Project: HOPE) | The current group name |
| 2025-01-03 | Fauna graduates | — |
| 2025-04-27 | Mumei graduates | Promise becomes three |

## Sensory Palette
- See: the Promise logo; Kronii's blue-and-silver palette beside IRyS's and Bae's.
- Hear: Bae's chaos, IRyS's warmth, Kronii's deadpan in the same call.

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Council | the 2021 generation's original name | members, fans |
| Promise | the group since 2023 | everyone |
| Kronies | Kronii's fans | Kronii |

## Conflicts and Story Hooks
1. Kronii and Bae dare each other through a horror game; the "tsundere granny" line comes back.
2. IRyS tries to get Kronii to admit she was scared.
3. A Promise anniversary where the three remember the two who graduated.
4. Kronii has to pick between a Promise plan and a Myth friend's invite on the same night.
5. A "Council" callback makes Kronii rank her old group jokes, deadpan.
6. Bae announces another BaeRyS "divorce"; IRyS demands the potato bento back.

## Links to Characters
Ouro Kronii and IRyS (members). Myth characters and Nerissa appear as cross-group friends.

## Secrets
(None.)

## Hard Facts (continuity)
- Active 2026-09-30: IRyS, Kronii, Bae. Graduated: Sana, Fauna, Mumei.
- Unverified title-only bits (Bae holding Kronii's hand, scaring Bae with IRyS) are not facts.

## Sources (checked 2026-09-30)
- S1 hololive production wiki page, member tables (secondary): https://virtualyoutuber.fandom.com/wiki/Hololive
- S2 Ceres Fauna and Nanashi Mumei wiki pages (graduation dates only; secondary)
- S3 Nanashi Mumei wiki page (Sana's graduation date; secondary)
- S4 Kronii file in this project (K4, K8, K33, K36, K37)
- S5 IRyS wiki page, §Relationships, §Units and groups (secondary); IRyS file in this project (R2)

---

## [SW] Name
hololive -Promise-

## [SW] Role
Faction

## [SW] Other Names
Promise, holoPromise, Council, holoCouncil

## [SW] Description
The group of Ouro Kronii and IRyS. It began as the English -Council- generation in August 2021, members who embody concepts (Kronii is Time), and became -Promise- when IRyS ("Hope") joined on 2023-10-09. After graduations (Sana in 2022, Fauna and Mumei in 2025), the active members are IRyS, Ouro Kronii and Hakos Baelz. Bae calls Kronii "too talented, savage, and a tsundere granny"; Fauna once described Kronii's "gap moe," the cute side that shows when she's flustered; IRyS has wondered aloud how Kronii sounds when she's scared. IRyS and the Council were already billed together as "CouncilRyS" (an official 3D collab, 2023-10-08) before she joined; with Bae she keeps the "BaeRyS" bit of being "married" and "divorced," which turned "Monopoly" into a fandom euphemism. Kronii's closest recent partners often come from outside the group: Mori Calliope (her first cross-generation collab, 2021), Ninomae Ina'nis (their 2026 concert pairing) and Watson Amelia (her "Time Duo" counterpart).

## [SW] Rules
In the 2026 baseline Promise is IRyS, Kronii and Bae; Sana, Fauna and Mumei are graduates and appear only as memories. Scares, pranks or hand-holding bits between Kronii and Promise members are unverified and are not written as facts.

## [SW] Sensory Details
The Promise logo; Bae's chaos, IRyS's warmth and sly asides, and Kronii's deadpan in one call.

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20260930-2309-world-hololive/claude-draft.md ====================

---
kind: world
name: "hololive"
sw_section: Worldbuilding
---

# World Element: hololive

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the company and its structure as publicly presented, checked 2026-09-30. Evidence labels:
> **[Official]** COVER's own material; **[Observed]** public stream, title or post ("secondary" = wiki or
> other reference); **[Adaptation]** an author decision for this project; **[Unverified]** reported, not
> confirmed.

## One-line Concept
hololive is the VTuber agency run by COVER Corporation that the whole cast belongs to (or belonged to):
the stage, the schedule, the concerts and the web of senpai, genmates and juniors around them.

## Type
Faction / organization (and workplace).

## How It Works
- **Structure (as of 2026-09-30):** hololive production is COVER's brand; hololive is its female VTuber
  group. On 2026-09-07 COVER merged all female branches (hololive, hololive English, hololive Indonesia,
  hololive DEV_IS) into a single "hololive," to remove regional limits and let members interact more
  freely; former groups keep their names as units (hololive -Myth-, -Promise-, -Advent-, -Justice-).
  Promotion is now done for all members in Japanese, Indonesian and English. [Observed S2 §2026,
  secondary, citing the hololive Next broadcast of 2026-09-07; project.md]
- **Member status:** active talents; **affiliates** who concluded their general activities but remain
  with hololive and appear at individual events (Watson Amelia since 2024-09-30); **graduates** who left
  (Gawr Gura on 2025-05-01; in Promise, Ceres Fauna 2025-01-03 and Nanashi Mumei 2025-04-27). Graduates
  are called alumni; stories never give reasons beyond "graduated." [Official COVER notices; Observed S2]
- **What members do:** livestreams (games, chatting, karaoke, art, music), original songs and albums,
  3D lives and concerts, collabs with other members, off-collabs (streaming together from the same
  place), sponsored streams, merchandise and voice packs, conventions and meet events. [Observed]
- **Events that anchor a calendar:** debut anniversaries (Myth's in mid-September), birthdays (often a
  3D live), hololive English concerts (the 4th, "Serendipity," 2026-07-03/04, Shrine Auditorium, Los
  Angeles), hololive fes and SUPER EXPO (7th fes, 2026-03-06–08), holoMeet events. [Observed S2]
- **Seniority:** the Japanese members are senpai; English members address them "-senpai" and many are
  openly starstruck. Juniors (Advent, Justice) are kouhai. [Observed character files]
- **The company in stories:** "management," "staff" and "my manager" appear as faceless helpers who
  schedule, check and support. No invented staff names, business secrets, scandals or disputes.
  [Adaptation; COVER Derivative Works Guidelines]
- **Concert and 3D work:** stories show the avatar performance and the members talking about rehearsals
  and nerves; the performers' physical rehearsal is not described. [Adaptation]
- **Edge example:** a story set before 2026-09 uses the old branch name "hololive English" and the
  members' statuses at that date (e.g. Gura active before May 2025). [Adaptation]

## Sensory Palette
- See: a "Starting soon" screen; a concert LED wall behind a 3D avatar; fans' glowsticks in member colors.
- Hear: a superchat chime; a schedule announcement; a crowd singing along in Los Angeles.
- One detail only here: members greeting a Japanese senpai with sudden, polite nerves.

## Society and Power
- Benefits: a stage, production support, concerts, merch, cross-language collabs (easier since the 2026
  merger).
- Pressure: schedules, rehearsals, streaming load; members talk about being tired and taking breaks
  (never elaborated with private details). [Observed; Adaptation]
- Hierarchy in play: genmates ("gen," the same debut group), senpai and kouhai, unit partners.

## History
| Date | Event | Trace left |
|---|---|---|
| 2020-09 | hololive English -Myth- debuts (first EN generation) | Myth anniversaries every September |
| 2021-08 | -Council- debuts (Kronii's generation) | Council → Promise |
| 2023-10-09 | -Promise- formed (IRyS joins the remaining Council) | Kronii's group name |
| 2024-09-30 | Watson Amelia concludes general activities, stays an affiliate | Occasional guest appearances |
| 2025-05-01 | Gawr Gura graduates | Alumna; remembered in songs and anniversaries |
| 2026-07-03/04 | hololive English 4th concert "Serendipity" (LA) | Partner pairs (e.g. Kronii and Ina) |
| 2026-09-07 | All female branches merge into one "hololive" | Groups become units |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| genmates / gen | members who debuted together | members |
| senpai / kouhai | senior / junior member | members |
| holoEN | the former English branch, still used casually | members, fans |
| graduation | leaving hololive | everyone |
| affiliate | concluded regular activities, still with hololive | official, members |
| 3D | a full-body avatar for lives and concerts | everyone |

## Conflicts and Story Hooks
1. After the 2026 merger, a member plans her first collab with someone she never could reach before.
2. A concert week: rehearsals, nerves, and a genmate who shows up to cheer.
3. An anniversary stream where the remaining members talk about the ones who left.
4. A kouhai asks a Myth senpai for advice and gets a joke first, then a real answer.
5. A schedule collision turns two members' streams into an impromptu collab.

## Links to Characters
All eight. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
Kronii and IRyS are active in hololive -Promise-; Nerissa in hololive -Advent-. Detailed history: the
cards "hololive History to 2022," "hololive History 2023-2026" and "Concerts and Live Events."

## Secrets
(None.)

## Hard Facts (continuity)
- Baseline date 2026-09-30: one merged "hololive"; units keep their names.
- Amelia: affiliate since 2024-09-30. Gura: graduated 2025-05-01. Fauna: 2025-01-03. Mumei: 2025-04-27.
- No graduation reasons, private details or invented company conflicts.

## Sources (checked 2026-09-30)
- S1 hololive official site (talents, news): https://hololive.hololivepro.com/en/
- S2 hololive production wiki page, §2024–§2026 and member tables (secondary):
  https://virtualyoutuber.fandom.com/wiki/Hololive
- S3 COVER notices: Amelia (2024-09-20) https://cover-corp.com/en/news/detail/20240920-01 ; Gura
  graduation (see Gura file G5)
- S4 COVER Derivative Works Guidelines: https://hololivepro.com/en/terms/
- S5 Serendipity concert site: https://serendipity.hololivepro.com/

---

## [SW] Name
hololive

## [SW] Role
Faction

## [SW] Other Names
hololive production, COVER, holoEN, hololive English, the company, management

## [SW] Description
The VTuber agency run by COVER Corporation that the cast belongs to. Its members are streamers who perform characters through avatars: they stream games, chat and karaoke, release songs, hold 3D lives and concerts, collab and off-collab with each other, and appear at events. Since 2026-09-07 all former branches are one "hololive," and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-. Watson Amelia concluded her regular activities on 2024-09-30 and remains an affiliate who appears at events; Gawr Gura graduated on 2025-05-01 and is an alumna. Japanese members are senpai, later groups are kouhai, and genmates are the people you debuted with. The calendar runs on debut anniversaries, birthdays, concerts and fes.

## [SW] Rules
Management and staff stay faceless helpers: no invented staff names, business secrets, scandals or disputes. Graduations are never explained beyond "graduated." Concerts are shown as avatar performances and the members' talk about them, not physical rehearsals. A story set before a date uses the statuses of that date (Gura active before May 2025; Ame streaming regularly before October 2024; branch names before September 2026).

## [SW] Sensory Details
A "Starting soon" screen; a superchat chime; a concert LED wall behind a 3D avatar; glowsticks in member colors; a crowd in Los Angeles singing along; polite nerves in front of a Japanese senpai.

## [SW] Secrets


---

## Open Questions
1. Should stories default to the 2026-09-30 baseline, or does the author want a different "present"?


==================== WORLD CARD FILE: 20261001-0001-world-IRyS-and-Nerissa-Pairs/claude-draft.md ====================

---
kind: world
name: "IRyS and Nerissa Pairs"
sw_section: Worldbuilding
---

# World Element: IRyS and Nerissa Pairs (with the Myth six, Kronii and each other)

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-10-01. Evidence labels as in the other world files. "Archive" = stream titles and
> descriptions on both members' channels (archive.ragtag.moe, S1); counts are streams mentioning the other
> per year, both channels added together, a rough measure. IRyS pairs run 2021 → 2026, Nerissa pairs
> 2023 → 2026. The archive is thin for 2026 (15–24 streams per channel), so a low 2026 count does not
> mean they stopped. Recent years weigh more (project rule), but early bits stay as shared memories.

## One-line Concept
How the two singers fit into the cast: IRyS, a 2021 senior who grew up beside Myth and now shares
Promise with Kronii; Nerissa, a 2023 kouhai who is an open fan of Kiara and sings with Calli.

## Type
Relationship web.

## IRyS
- **IRyS and Calli** (16 / 16 / 5 / 8 / 2 / 1): Calli's first collab with her came days after IRyS's debut
  ("Just Irystocrats and DeadBEATS," 2021-07-29), then a karaoke collab (2021-10). With Hakos Baelz they
  host CHADCast ("Chaos, Hope, and Death!", from 2022-01-30; a 2025 episode: "We Went to a Hot Spring
  Together!!"). Later: "Two Pink Women Roll Up to Silent Hill" (2024-10-26), IRyS as Calli's HOLOMELO
  RADIO guest (2024-07), an off-collab karaoke with Momosuzu Nene (2025-04-23). Wiki unit: "MorIRyS."
  [Observed S1 titles; S2 IRyS §Relationships, secondary]
- **IRyS and Kronii** (10 / 12 / 7 / 6 / 8 / 1): genmates since -Promise- (2023), friends since 2021 (fan
  unit K.I.R.A with Reine and Anya). Two-player games and watchalongs: A Way Out (2021–22), "School Days
  (THE CHRISTMAS ANIME)" (2023-12-21), Buckshot Roulette "You Or Me But For Real" (2024-11), Bokura "Left
  Side Right Side" (2025-02), a Powerwash Simulator race, "May The Best Maid Win" (2025-07-08). In 2026,
  after Kronii's 3D birthday live "The Goddess Descends," IRyS said she, "a half-angel, half-demon
  Nephilim," could pull off Kronii's goddess look "somehow." [Observed S1 titles; S2, secondary; ASR IRyS
  file R20, second model agrees]
- **IRyS and Ina** (15 / 7 / 3 / 4 / 6 / 0): an early duo ("Keep Talking and Nobody Explodes," 2021-07-31;
  "It Takes Two," three parts, "It Takes Tako & Hope," 2021); a Gundam watchalong (2023-03-25); IRyS as
  guest on Ina's "AmiAmi March Special" (2025-03-18); Elden Ring Nightreign, which IRyS titled "Third
  Wheeling" (2025-06-24); guildmates ("Cerulean Cup," with Kronii, Bijou and Gigi) in the ENigmatic
  Recollection Minecraft story. [Observed S1 titles; S2 §Units, secondary]
- **IRyS and Kiara** (13 / 1 / 3 / 2 / 3 / 0): Kiara's "1ST FULL HOLOEN COLLAB ft. IRYS!" (2021-08-12); a
  "GERMAN CRASH COURSE … with IRYS" (2022-06-02); an off-collab doing each other's nails on camera
  (2023-11-14); TORIDAMA 2 off-collab with Kronii and Raora, "Who is the BRAVEST?" (2024-08-01).
  [Observed S1 titles]
- **IRyS and Ame** (11 / 2 / 3 / 2 / 0 / 0) and **IRyS and Gura** (11 / 6 / 0 / 1 / 0 / 0): mostly the
  2021–22 full-EN collabs (Among Us, Dead by Daylight, Overwatch); IRyS joined Ina, Bae and Ame's
  "LOSER BUYS DINNER!!!!!" off-collab (2023-02-23). With Gura graduated and Ame an affiliate, these are
  memories. [Observed S1 titles]

## Nerissa
- **Nerissa and Kiara ("KiaRissa")** (15 / 12 / 3 / 0): Kiara is Nerissa's oshi; in Nerissa's lore she
  worked at KFP before hololive and she owns Kiara merch. "Compatibility test with Kiara-senpai"
  (2023-08-14); Kiara showed her around the EN Minecraft server (2023-09-07); their Baldur's Gate 3 party
  with Calli and Bijou ("Killing, Two Birds, with One Stone," 2023); "Rating your CARS with NERISSA"
  (2023-10-21); a January 2024 off-collab trip ("KiaRissa ARC HAS BEGUN," reading their trip diaries);
  "GIRLSTALK with Nerissa, EN BIRB GIRLS PARTY!" (2025-04-08); a CHICAGO watchalong "with the musical
  connoisseur Nerissa" (2025-07-09). [Observed S1 titles; S3 Nerissa §Relationships, §Lore, secondary]
- **Nerissa and Calli** (6 / 7 / 3 / 1): the BG3 party (2023); Calli's "I Gathered 8 Cute People to
  Destroy their Friendships" (Mario Party, 2024-11); Calli as guest at Nerissa's 2025 3D concert ("Bocca
  della Verità"); the duet "OVER//RIDE – Mori Calliope × Nerissa Ravencroft" (2025-07-18); Nerissa as
  HOLOMELO RADIO guest (2025-07); Nerissa sang charity karaoke for #GOLIVEforLOVE (2026-02-17). Nerissa was
  Calli's first Instagram follower. [Observed S1 titles; S3, secondary]
- **Nerissa and IRyS** (1 / 0 / 3 / 1): the two singers: IRyS was a guest at Nerissa's 2025 3D concert
  ("Missing Promise"), they hunted together in Monster Hunter Wilds (2025-03-01), and in 2026 Nerissa made
  Miis of IRyS and Ina in Tomodachi Life ("Inya and Irys will be born!", 2026-04-23). [Observed S1 titles]
- **Nerissa and the others:** Ame: Portal 2, "TAKING ON PUZZLES WITH @WatsonAmelia" (2024-09-28). Gura:
  fellow guildmates ("Scarlet Wand") in ENigmatic Recollection, now a memory. Kronii: big group collabs
  only (Among Us, 2023-12). [Observed S1 titles; S3 §Relationships, secondary]

## Sensory Palette
- See: CHADCast's three-way call; IRyS and Kronii's split-screen co-op; KFP merch on Nerissa's shelf;
  two singers on one concert stage.
- Hear: "Chaos, Hope, and Death!"; Kiara's "Nerissa!" across a Minecraft base; a duet with Calli's
  low rap and Nerissa's high voice.

## History
| Date | Event | Trace left |
|---|---|---|
| 2021-07-29 | Calli's first collab with IRyS | MorIRyS |
| 2022-01-30 | First CHADCast | Chaos, Hope, and Death |
| 2023-08-14 | Nerissa's compatibility test with Kiara | KiaRissa |
| 2023-10-09 | -Promise- formed: IRyS and Kronii genmates | — |
| 2024-01 | KiaRissa off-collab trip | Shared trip stories |
| 2025 | Nerissa's 3D concert with Calli and IRyS as guests; "OVER//RIDE" duet | Calli × Nerissa |
| 2026-04-23 | Nerissa's Tomodachi Life Miis of IRyS and Ina | — |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| CHADCast | IRyS, Calli and Bae's talk show ("Chaos, Hope, And Death") | the three |
| MorIRyS | IRyS and Calli | fans |
| KiaRissa | Kiara and Nerissa | the two, fans |
| K.I.R.A | Kronii, IRyS, Reine, Anya | fans |
| senpai / kouhai | IRyS is a senior to Nerissa; Myth are seniors to both | everyone |

## Conflicts and Story Hooks
1. CHADCast records an episode while Calli and IRyS disagree on what counts as "chad."
2. IRyS and Kronii race again at something mundane; the loser has to admit she was scared.
3. Nerissa guests on Kiara's stream and fangirls so hard she forgets the topic.
4. Calli and Nerissa rehearse a duet; Calli's flow meets Nerissa's flirting.
5. Nerissa's Tomodachi Life island makes IRyS and Ina's Miis do something strange.

## Links to Characters
IRyS, Nerissa Ravencroft, and the six: Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Ouro Kronii,
Gawr Gura (memory), Watson Amelia (affiliate).

## Secrets
(None.)

## Hard Facts (continuity)
- IRyS debuted 2021-07-11 (senior to Kronii by a month, to Nerissa by two years); Nerissa 2023-07-31.
- CHADCast = IRyS, Calli, Bae. KiaRissa = Kiara and Nerissa. IRyS and Kronii are -Promise- genmates.
- 2026 baseline: IRyS–Gura and Nerissa–Gura are memories; Ame appears as an affiliate guest.

## Sources (checked 2026-10-01)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30). IRyS: BN3O2ELkwqg, ZhZOywPYLNE,
  MXd7uOemEzc, hJUsFwoJe_A, QMm3SQotdBI, iswLHkhR4x4, 3L0AVntuhhA, tBPQW-MGNPM, XPdN8RN6eJw, yU5Vs7YHCQ4,
  LKQm2RqQmoQ, 5eYkIqYmiaA, qqi8yXuH35Y, o9BR2Wxuwf0, RstEjhhy3Qw, OWqT53IpcY0, 33RSpTQbx6U, BmiGfkw-qzg,
  rP8nSJkwLGE, u740WgBr39M, 6JF3eMx0QSc, mQr2DVYx_8M, GMtqCEHvUKY. Nerissa: vdmr7B__G3s, Rc8O5lB31_w,
  D_uuZW2nknY, dxGzb807obQ, zYZ4BMpDIFw, Nb6RzqVEwRI, 0cYFDqSvG1c, 8d2zmPrZPhc, gti0m-CjAB0, hgMl8y2ufIg,
  BUc6w7xiAuw, ywURoa_htrg, loYqb7qoKzw, DUPE4-8_RYs, dL6rqJXSAcI, 1BjQxvo51Lc. Mention counts computed
  by Claude.
- S2 IRyS wiki page, §Relationships, §Units and groups (secondary)
- S3 Nerissa Ravencroft wiki page, §Relationships, §Lore, §Likes and dislikes, §Miscellaneous (secondary)
- S4 Character files: IRyS (R20), Nerissa (N2), Kronii, Calli, Kiara, Ina

---

## [SW] Name
IRyS and Nerissa Pairs

## [SW] Role
Relationship

## [SW] Other Names
MorIRyS, CHADCast, KiaRissa, IRyS and Kronii, IRyS and Ina, Nerissa and Calli, Nerissa and IRyS

## [SW] Description
IRyS and Calli: Calli collabed with her days after IRyS's 2021 debut; with Bae they host CHADCast ("Chaos, Hope, and Death!"), and they still team up (Silent Hill 2 as "Two Pink Women," karaoke). IRyS and Kronii: Promise genmates and friends since 2021, regulars at two-player games (A Way Out, Bokura, a Powerwash race, "May The Best Maid Win"); in 2026 IRyS said she could pull off Kronii's goddess look "somehow." IRyS and Ina: an early duo (It Takes Two, "It Takes Tako & Hope") who still play together. IRyS and Kiara: Kiara gave her a German crash course; nail-painting off-collab. Nerissa and Kiara (KiaRissa): Kiara is Nerissa's oshi; Kiara showed her around Minecraft; a 2024 off-collab trip; a 2025 "BIRB GIRLS" GIRLSTALK. Nerissa and Calli: a Baldur's Gate 3 party, the 2025 duet "OVER//RIDE," and Calli as a guest at Nerissa's 3D concert. Nerissa and IRyS: two singers; IRyS guested at that concert, and Nerissa put IRyS and Ina in Tomodachi Life.

## [SW] Rules
IRyS (2021) is Nerissa's senior; Myth are seniors to both. Recent pairings (IRyS with Kronii, Calli and Ina; Nerissa with Kiara and Calli) carry the most weight; pairs with Gura are memories. All are friendships and stream bits.

## [SW] Sensory Details
A three-way CHADCast call; a split-screen co-op with Kronii; KFP merch on Nerissa's shelf; Calli's low rap against Nerissa's high voice in one duet.

## [SW] Secrets


---

## Open Questions
1. The 2025 "KIARA & FRIENDS" spring concert names both IRyS and Nerissa in its archive entry; whether
   they performed or were only thanked was not checked, so it is left out.


==================== WORLD CARD FILE: 20261001-0001-world-hololive--Advent/claude-draft.md ====================

---
kind: world
name: "hololive -Advent-"
sw_section: Worldbuilding
---

# World Element: hololive -Advent-

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: Nerissa Ravencroft's group as publicly shown, checked 2026-10-01. Evidence labels as in the other
> world files. "Archive" = stream titles and descriptions on Nerissa's channel (archive.ragtag.moe, S4);
> counts are streams mentioning the member per year (2023 → 2025), a rough measure (the archive holds 114,
> 183 and 87 of her streams for those years and only 22 for 2026). Only what a Nerissa story needs.

## One-line Concept
Nerissa's group: five "criminals" who escaped from The Cell, a prison for anything too dangerous to exist,
and debuted together as hololive English's third generation in July 2023. All five are active in 2026, and
the "escaped convict" premise is a running bit they play with, not a fact they live by.

## Type
Faction / unit.

## Members and Status (2026-10-01)
- Active: Shiori Novella, Koseki Bijou, Nerissa Ravencroft, and the twins Fuwawa and Mococo Abyssgard
  (FUWAMOCO, who share one channel). [Observed S1 member table, secondary]
- Group fans: Adventrix; group oshi mark ⚠️; logo character "Pokey." [Observed S1, secondary]
- Since the September 2026 merger the name is "hololive -Advent-" (before: "hololive English -Advent-").
  [Observed S1; S2 Nerissa §2026, secondary]

## How the Group Works (as it touches Nerissa)
- **The premise as a bit:** each member was sealed in The Cell for being "untouchable"; Nerissa, the
  "Demon of Sound," stole the master key from the guards on the way out and keeps it on her keychain. The
  next generation, -Justice-, are law enforcers sent to catch the five fugitives, so Advent × Justice
  collabs turn into prisoner-and-guard jokes (a 2026 merch reveal: "Like prisoner and my prison guard").
  [Official S3; Observed S1, S2 §Lore, secondary; ASR Nerissa file N20, multi-speaker, not attributed]
- **Nerissa and Shiori ("ShioRaven"):** her most-mentioned genmate (6 / 18 / 3). Nerissa calls Shiori her
  "wife," Shiori plays hard to get, and the two keep a lore of fictional "children." Shiori claims she
  knows where Nerissa's broken horn piece is and never mentioned it because Nerissa never asked.
  [Observed S2 §Relationships, §Lore, secondary; S4]
- **Nerissa and Bijou ("JewelBird"):** a raven who loves shiny things and a rock girl (12 / 18 / 0);
  Bijou calls her "Nerizzler." [Observed S2, secondary; S4]
- **Nerissa and FUWAMOCO ("Sound Hounds"):** after time with the twins she claims to be the third
  Abyssgard sister, "Mofufu"; Fuwawa calls her "Newissa" (6 / 16 / 0). [Observed S2, secondary; S4]
- **As a group:** relay streams for new outfits, a friendship test with swapped hairstyles (Nerissa got
  Fuwawa's, dog ears included), and joint Expo appearances with -Justice- (2025, 2026).
  [Observed S1, S2 §2025, secondary]
- **Seniors:** Advent were kouhai to Myth and Promise from day one; Kiara hosted all five on HOLOTALK
  (2023-08-12) within two weeks of their debut. [Observed S5 Kiara archive title]

## History
| Date | Event | Trace left |
|---|---|---|
| 2023-07-25 | "WANTED!" debut PV reveals the five | The fugitive premise |
| 2023-07 (end) | Debuts; Nerissa's on 2023-07-31 (JST) | "Advent" |
| 2023-08-12 | Advent are Kiara's 29th HOLOTALK guests | First big senior collab |
| 2024 (summer) | Advent 3D debuts; Nerissa's on 2024-08-09 | The "Demon of Soup" soup |
| 2025, 2026 | hololive SUPER EXPO with -Justice- | Prisoner-and-guard bits |
| 2026-09 | Renamed "hololive -Advent-" in the merger | Current name |

## Sensory Palette
- See: the ⚠️ mark; Pokey on the logo; prison-gown outfits on merch; a master key on Nerissa's keychain.
- Hear: five voices at once on one mic; "Mofufu!"; a mock-stern Justice "guard" voice.

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| The Cell | the prison Advent escaped from (lore) | everyone |
| Adventrix | Advent's collective fans | official |
| ShioRaven / JewelBird / Sound Hounds | Nerissa's pairings with Shiori / Bijou / FUWAMOCO | fans, members |
| Mofufu | Nerissa as the "third Abyssgard sister" | Nerissa |
| Jailbirds | Nerissa's own fans | Nerissa |

## Conflicts and Story Hooks
1. A -Justice- member "arrests" Nerissa on stream; she negotiates her release with soup.
2. Shiori finally tells Nerissa where the horn piece is, as a bit, and chat demands proof.
3. FUWAMOCO adopt "Mofufu" for a day, and Nerissa has to keep up with the twins' energy.
4. An Advent anniversary relay where each member re-tells the escape differently.
5. Bijou and Nerissa compete over a shiny thing in a game.

## Links to Characters
Nerissa Ravencroft (member). Kiara, Calli and IRyS appear as seniors (see "IRyS and Nerissa Pairs").

## Secrets
(None.)

## Hard Facts (continuity)
- Active 2026-10-01: Shiori, Bijou, Nerissa, Fuwawa, Mococo. Fans: Adventrix; mark ⚠️.
- -Justice- (2024) are the "law enforcers" of the same storyline; stories treat it as a shared stream bit.

## Sources (checked 2026-10-01)
- S1 hololive production wiki page, -Advent- and -Justice- sections and member tables (secondary):
  https://virtualyoutuber.fandom.com/wiki/Hololive
- S2 Nerissa Ravencroft wiki page, §Relationships, §Lore, §2023–§2026 (secondary)
- S3 Nerissa's official profile: https://hololive.hololivepro.com/en/talents/nerissa-ravencroft/
- S4 Stream archive metadata, Nerissa's channel (archive.ragtag.moe, read 2026-09-30); mention counts
  computed by Claude.
- S5 Stream archive metadata, Kiara's channel: 0Q9FLtcAY0s (2023-08-12)
- S6 Nerissa file in this project (N1, N2, N20)

---

## [SW] Name
hololive -Advent-

## [SW] Role
Faction

## [SW] Other Names
Advent, holoAdvent, hololive English -Advent-

## [SW] Description
Nerissa Ravencroft's group, hololive English's third generation (debuted July 2023): Shiori Novella, Koseki Bijou, Nerissa, and the twins Fuwawa and Mococo Abyssgard (FUWAMOCO). Their shared lore is a stream bit: five "criminals" who escaped The Cell, a prison for anything too dangerous to exist; Nerissa stole the master key on the way out. The next generation, -Justice-, are the "law enforcers" sent to catch them, so joint streams become prisoner-and-guard jokes. Nerissa calls Shiori her "wife" while Shiori plays hard to get (ShioRaven); with Bijou she is a raven drawn to the shiny rock girl (JewelBird); with FUWAMOCO she claims to be the third sister, "Mofufu" (Sound Hounds). Kiara hosted all five on HOLOTALK two weeks after their debut. Fans: Adventrix, mark ⚠️.

## [SW] Rules
All five are active in 2026; the group is "hololive -Advent-" since the 2026 merger. The prison escape is lore they play for laughs on stream, never a real crime. Myth and Promise are their seniors.

## [SW] Sensory Details
The ⚠️ mark and Pokey on the logo; prison-gown merch; a stolen master key jingling on Nerissa's hip; five voices crowding one mic.

## [SW] Secrets


---

## Open Questions
(None.)


==================== WORLD CARD FILE: 20261001-0018-world-Concerts-and-Live-Events/claude-draft.md ====================

---
kind: world
name: "Concerts and Live Events"
sw_section: Worldbuilding
---

# World Element: Concerts and Live Events

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the recurring live events of hololive and the cast's own concerts and 3D lives, checked
> 2026-10-01. Evidence labels as in the other world files. Group history is on the two History cards;
> this card is about what the events are and which ones each character has stood on.

## One-line Concept
The stages that punctuate the year: the spring fes and Expo, the summer EN concert, birthday and
anniversary 3D lives, world tours and solo concerts, each one a memory the cast brings up on stream.

## Type
Recurring events / culture.

## Recurring Events
- **hololive fes. + hololive SUPER EXPO** (every March since 2023, in Japan): the agency-wide concert and
  convention. 4th fes "Our Bright Parade" (2023), 5th "Capture the Moment" (2024), 6th "Color Rise
  Harmony" (2025-03-08/09; Nerissa on day 1), 7th "Ridin' on Dreams" (2026-03-06/08). EN units share
  Expo booths and key visuals (Myth with Promise, Advent with Justice). [Observed S1 §2023–§2026; S2]
- **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking
  Dimensions-" (2024-08-24/25, Kings Theatre, New York), "-All for One-" (2025-08-23/24, Radio City Music
  Hall, New York), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around
  partner pairs (Calli–Shiori, Kronii–Ina, Kiara–Bijou), each with a published interview.
  [Observed S1; character files C11, K4, I7, T10]
- **World tours:** "hololive STAGE World Tour'24 -Soar!-" (New York, Jakarta, Singapore, Atlanta, Kuala
  Lumpur) and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and
  Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and
  Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]
- **Birthday and anniversary 3D lives:** a member's own stream, often with a new song or outfit and
  surprise guests from other units. [Observed character files]
- **holoMeet** (since 2022): overseas fan events with yearly ambassadors (Gura 2022, IRyS 2023, Bae 2024,
  Bijou 2025, Gigi 2026). [Observed S1]
- **Summer events:** "hololive Summer" (2022, 2023), "holonatsu Paradise" (2025-07, with a VRChat
  tournament and a butt-sumo tournament). [Observed S1]

## The Cast on Stage
| Character | Stages (selected) | Source |
|---|---|---|
| Mori Calliope | Solo concert "New Underworld Order" (2022-07-21); "GriMoire" at the Hollywood Palladium (2025-02-26), the first solo concert by a hololive production talent outside Japan; World Tour '25 lead; Serendipity with Shiori | Calli file C6, C19, C11; S1 |
| Takanashi Kiara | 4th-anniversary live "MIRAGE" (2024-10-06); "KIARA & FRIENDS: H!P Cover Song Spring Concert" (2025-04-21); "Drawn to Dawn" with Ina (2026-03-27/28, The Wiltern); Serendipity with Bijou | Kiara file T11, T12, T10; S3 titles |
| Ninomae Ina'nis | 3D live "Pleiades" (2024-12-28); "Drawn to Dawn" with Kiara; Serendipity with Kronii | Ina file I20, I7; S3 title |
| Ouro Kronii | World Tour '25 Sydney guest; 3D birthday live "The Goddess Descends" with a new outfit (2026-03-13/14, Ame as guest); Serendipity with Ina | Kronii file K33, K4; S1 |
| IRyS | Promise musical "The Broken Promise" (2024-12-14); 3D lives "The Devil Wears Hope" (2024-11-17), "HOPE UPON A STAR" (2025-03-16), "Racing Towards Hope" (2026-03, race-queen outfit); World Tour '25 lead; first solo concert "HOPE ||: Beyond the Stars," Tokyo, 2026-10-06 | IRyS file R2, R3; S1 |
| Nerissa Ravencroft | 6th fes day 1 (2025-03-08); 3D concert "Requiem for Love – A JukeBox Musical" (2025-05-24, with Calli and IRyS as guests); Advent's "On the Run!" (2025-08-29); World Tour '25 lead | Nerissa file N2, N3; S1 |
| Gawr Gura | Final 3D mini live on her graduation day (2025-05-01) | Gura file G5 |
| Watson Amelia | As an affiliate: guest at Kronii's 2026 birthday live | Kronii file K33 |

## How It Works in Stories
- Concerts are shown through the avatar performance and the members' talk before and after: nerves,
  rehearsals "with the team," the pair interview, what song they are most excited for. [Adaptation]
- After a concert, members stream an aftertalk ("BDay Live Aftertalk") and gush about outfits and
  guests. [Observed IRyS file R20]
- Surprise guests are kept secret until the moment; members tease "a surprise" in titles.
  [Observed S3 titles, e.g. "MIRAGE WITH A SURPRISE!?"]

## Sensory Palette
- See: glowsticks in member colors; an LED wall; a new 3D outfit's reveal; a city name on a tour poster.
- Hear: a crowd shouting a call-and-response; a duet's harmony; the aftertalk chat flood of "cute."

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| fes | hololive's yearly agency-wide concert | everyone |
| 3D live | a concert or show performed with the full-body avatar | everyone |
| aftertalk | the stream after a live where she talks about it | members |
| Serendipity pair | the 2026 EN concert partnership | members |

## Conflicts and Story Hooks
1. The night before Serendipity, the pairs rehearse each other's lines and break.
2. IRyS counts down to her first solo concert in Tokyo; Kronii and Calli send messages.
3. Nerissa watches a senpai's fes from the audience side and fangirls.
4. An aftertalk where Kiara and Ina disagree about who cried first at "Drawn to Dawn."
5. A tour stop in Sydney: Kronii joins Calli, IRyS and Nerissa as a guest.

## Links to Characters
All eight.

## Secrets
(None.)

## Hard Facts (continuity)
- EN concerts: 2023-07-02, 2024-08-24/25, 2025-08-23/24, 2026-07-03/04 (Serendipity).
- IRyS's first solo concert is 2026-10-06, after the 2026-09-30 baseline.

## Sources (checked 2026-10-01)
- S1 hololive production wiki page, §History 2022–2026 (secondary): https://virtualyoutuber.fandom.com/wiki/Hololive
- S2 Nerissa Ravencroft wiki page, §2025 (secondary)
- S3 Stream archive metadata (archive.ragtag.moe): 0LoG81pLS8c (Kiara, 2024-10-06), jjLLByDa3Xc (Kiara,
  2025-04-21), 3n9igJnSXtQ (Ina, 2024-12-28), qqi8yXuH35Y (Kronii, 2026-03-14), V0plPBgyqPs (IRyS,
  2025-03-16)
- S4 Character files in this project (C6, C11, C19; T10–T12; I7, I20; K4, K33; R2, R3, R20; N2, N3; G5)

---

## [SW] Name
Concerts and Live Events

## [SW] Role
Culture

## [SW] Other Names
fes, hololive fes, SUPER EXPO, EN concert, Serendipity, world tour, 3D live, birthday live, aftertalk

## [SW] Description
The stages of the hololive year. Every March, hololive fes and SUPER EXPO in Japan (6th fes "Color Rise Harmony," 2025, with Nerissa; 7th "Ridin' on Dreams," 2026). Every summer, a hololive English concert in the US: "-Connect the World-" (2023), "-Breaking Dimensions-" (New York, 2024), "-All for One-" (Radio City, 2025), and "Serendipity" (Los Angeles, 2026-07-03/04), built on pairs: Calli with Shiori, Kronii with Ina, Kiara with Bijou. World Tour '25 "-Synchronize!-" was led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests. The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn" (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01). After a live comes the aftertalk stream.

## [SW] Rules
Concerts are told through the avatar performance and the members' talk before and after (nerves, rehearsals, aftertalks), never the performers' physical bodies. Surprise guests stay secret until revealed. IRyS's solo concert has not happened yet at the 2026-09-30 baseline.

## [SW] Sensory Details
Glowsticks in member colors; an LED wall; a new 3D outfit's reveal; a call-and-response from the crowd; the aftertalk chat flooding "cute."

## [SW] Secrets


---

## Open Questions
1. Which characters performed at the four EN concerts (2023–2025 line-ups) was not checked; only
   Serendipity's pairs are on the card.


==================== WORLD CARD FILE: 20261001-0018-world-Cross-Branch-Friends/claude-draft.md ====================

---
kind: world
name: "Cross-Branch Friends"
sw_section: Worldbuilding
---

# World Element: Cross-Branch Friends

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the eight characters' public ties to members outside English (Japanese, Indonesian, DEV_IS,
> HOLOSTARS) and a few outside hololive, checked 2026-10-01. Evidence labels as in the other world files.
> "Archive" = stream titles and descriptions on the character's own channel (archive.ragtag.moe, S1);
> counts are streams mentioning the other per year, a rough measure (thin for 2026). Unit names come from
> each member's wiki §Relationships (S2). Recent years weigh more (project rule).

## One-line Concept
Beyond EN: the senpai they idolize, the Indonesian friends they game with every month, and the unit
names fans gave their pairings, the web that the 2026 merger now lets them use more freely.

## Type
Relationship web.

## By Character
- **Mori Calliope:** Hoshimachi Suisei is the senpai she is starstruck by ("Death Star"): she drew her
  ("DRAWING MY SENPAI," 2021), Suisei featured at Calli's first solo concert ("Wicked," 2022), they talked
  live shows together (2023), and Calli hosts watch parties of Suisei's concerts ("We're Screaming Loud
  for Senpai!", 2024-11). Kobo Kanaeru calls her "Uncle Dad" ("Father Daughter GOLF," 2022; Kobo at her
  house, 2023). Units: "Holodeath" (with Kureiji Ollie), "LYRA" (with Koganei Niko, Ayunda Risu, Amane
  Kanata, Elizabeth), "MoRikka" (with HOLOSTARS' Rikka; fans "DeadTuners"). Outside hololive: friends
  with Milky Queen, whom she credits for introducing her to VTubers, and Ironmouse (a shared Underworld
  theme). [Observed S1 titles; S2 Calli §Relationships; Calli file]
- **Takanashi Kiara:** Usada Pekora is her oshi ("Senpai! Be my guide for the day!", 2020; HOLOTALK's
  24th guest, 2022). Pavolia Reine is her most-mentioned ID friend (30 streams; their pair name "PavoNashi"; a VR
  "vacation," a Minecraft summer festival; the bird unit "HOLOTORI" with Subaru, Reine, Mumei and Lui); Kobo calls her "Mommy Kiwawa." Other units:
  "O'riends" (Momosuzu Nene), "KoAra Connect" (Hakui Koyori), "SunMoon"/"Eclipse" (Moona Hoshinova).
  Outside hololive: "PomuTori" (Pomu Rainpuff), "Mintori" (Mint Fantôme). [Observed S1; S2 Kiara; Kiara file]
- **Ninomae Ina'nis:** an artist among artists: fellow ocean unit UMISEA (Minato Aqua, Houshou Marine,
  Sakamata Chloe, Gura); "HoloJEI" (Tsunomaki Watame, Kureiji Ollie, Anya Melfissa); "TakoBazo" (Vestia
  Zeta); "TakoNeko" (Nekomata Okayu, with a 2025 Mythmash duet, "Kurukuru Cruise"); Shiranui Flare
  appeared on her 2025 AmiAmi special ("Flare?!!?"). She admires Marine as an artist. [Observed S1; S2 Ina; Ina file]
- **Gawr Gura** (graduated): "Apex Predators" (Shishiro Botan), UMISEA, "SharPea" (Pavolia Reine), and
  Murasaki Shion (Minecraft and Mario Kart in 2021; a "Renai Circulation" duet cover, 2022). [Observed S1; S2 Gura]
- **Watson Amelia** (affiliate): "KoMeHa" (Kobo Kanaeru, Kazama Iroha), "ZetAme" (Vestia Zeta); outside
  hololive, "SelAMei" (with Mumei and Selen Tatsuki). [Observed S2 Ame]
- **Ouro Kronii:** her steadiest cross-branch partner is Kaela Kovalskia (21 streams; survival and
  sim co-ops every few months: Raft 2023–24, Panicore, Luma Island 2024, Old Market Simulator 2025); also
  "soranii" with Tokino Sora, fan unit K.I.R.A (with IRyS, Reine, Anya), and Raora Panthera of Justice
  (Portal 2, Split Fiction, No Man's Sky 2026; "Pizza Time"). [Observed S1; S2 Kronii; Kronii file]
- **IRyS:** Shiranui Flare is her closest JP friend (23 streams, 11 in 2024): horror and camping co-ops
  ("ふーたんとキャンプだ！"), Splatoon private matches, an off-collab karaoke (2025-03); units "Star Flower"
  (Moona, Suisei, AZKi), "IRySora" (Tokino Sora), "ReiRyS" (Reine), "OKFAIR" (Ollie, Kronii, Fauna, Anya,
  Reine). [Observed S1; S2 IRyS]
- **Nerissa Ravencroft:** Houshou Marine is her oshi (plush, figures, an off-collab with Marine and
  FUWAMOCO, 2024); "BLUE·MEGAMISAMA" with Tokino Sora; "V3LVET" with Raora and Moona Hoshinova; Kobo
  calls her "Nori-chan." [Observed S1; S2 Nerissa; Nerissa file]

## How It Works in Stories
- Japanese members are senpai: EN members use "-senpai," switch to polite Japanese and get openly
  nervous; Indonesian members are EN's peers and long-time collab partners. [Observed character files]
- Since the 2026-09-07 merger, cross-language collabs are encouraged; stories can show a first-ever pairing
  as new. [Observed S3 §2026]
- Members of other agencies appear only as brief, friendly mentions. [Adaptation]

## Sensory Palette
- See: a bilingual stream title with both names; a senpai's plush on a shelf; a joint thumbnail with a
  Japanese caption.
- Hear: "Senpai!" in a pitched-up nervous voice; Japanese and English mixed mid-sentence; a Kobo
  nickname ("Mommy Kiwawa," "Uncle Dad").

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| oshi | the member you support most | everyone |
| senpai | a senior member, often Japanese | everyone |
| Death Star | Calli and Suisei | fans |
| PavoNashi / HOLOTORI | Kiara with Reine / the bird unit | fans |
| UMISEA | the ocean unit (Aqua, Marine, Chloe, Ina, Gura) | official, members |
| K.I.R.A | Kronii, IRyS, Reine, Anya | fans |

## Conflicts and Story Hooks
1. Calli finally gets a one-on-one with Suisei after the merger and can't form sentences.
2. Kronii and Kaela's endless sim co-op hits the in-game stock market.
3. IRyS and Flare go camping in a horror game again; IRyS insists she isn't scared.
4. Nerissa meets Marine at an event and forgets every word of Japanese.
5. Kiara and Reine plan another "vacation" in VR.

## Links to Characters
All eight.

## Secrets
(None.)

## Hard Facts (continuity)
- Calli's senpai: Suisei. Kiara's oshi: Pekora. Nerissa's oshi: Marine (and Kiara).
- Kronii's steadiest cross-branch partner: Kaela. IRyS's closest JP friend: Flare.

## Sources (checked 2026-10-01)
- S1 Stream archive metadata (archive.ragtag.moe, read 2026-09-30); titles quoted above (e.g. Calli
  2021-07-24, 2022-08-19, 2023-04-12, 2024-11-14; Kiara 2020-11-26, 2022-11-18, 2022-05-14; Kronii
  2023-10-17 to 2025-06-05, 2026-05-03; IRyS 2024-03-20, 2025-01-17, 2025-03-26; Ina 2025-07-21,
  2025-08-04; Gura 2021-10-09, 2022-06-13; Nerissa 2024-12-04). Mention counts computed by Claude.
- S2 Member wiki pages, §Relationships / units (secondary): Calli, Kiara, Ina, Gura, Ame, Kronii, IRyS, Nerissa
- S3 hololive production wiki page, §2026 (secondary)
- S4 Character files in this project

---

## [SW] Name
Cross-Branch Friends

## [SW] Role
Relationship

## [SW] Other Names
Death Star, PavoNashi, HOLOTORI, UMISEA, K.I.R.A, Star Flower, IRySora, soranii, Apex Predators, KoMeHa, BLUE·MEGAMISAMA, V3LVET, senpai, oshi

## [SW] Description
The cast's ties beyond EN. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is her closest Indonesian friend ("PavoNashi"; both are in the bird unit "HOLOTORI"). Ina belongs to the ocean unit UMISEA (Aqua, Marine, Chloe, Gura) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's steadiest cross-branch partner is Kaela Kovalskia (survival and sim co-ops for years), plus "soranii" with Tokino Sora and Portal-style co-ops with Justice's Raora. IRyS's closest Japanese friend is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA") and Kobo calls her "Nori-chan."

## [SW] Rules
Japanese members are senpai: EN members use "-senpai," switch to polite Japanese and get nervous. Indonesian members are peers. Since the 2026 merger, cross-language collabs are encouraged. Members of other agencies are only brief, friendly mentions.

## [SW] Sensory Details
A bilingual stream title with both names; a senpai's plush on a shelf; "Senpai!" in a nervous, pitched-up voice; Japanese and English mixed mid-sentence.

## [SW] Secrets


---

## Open Questions
1. HOLOSTARS ties (Calli's "MoRikka") are on the dossier only; the author may want a male-member policy.


==================== WORLD CARD FILE: 20261001-0018-world-hololive-History-2023-2026/claude-draft.md ====================

---
kind: world
name: "hololive History 2023-2026"
sw_section: Worldbuilding
---

# World Element: hololive History 2023–2026

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public history of hololive from 2023 to the 2026-09-30 baseline, checked 2026-10-01. Evidence
> labels as in the other world files. Dates JST unless noted (PDT/EDT for US events). Graduation and
> conclusion dates come from wiki infoboxes; no reasons are given or implied (project rule). Concerts
> have their own card ("Concerts and Live Events").

## One-line Concept
The recent past that shapes the present: new generations (Advent, ReGLOSS, Justice, FLOW GLOW), the
"conclusion of streaming activities" that keeps Ame an affiliate, the 2025 farewells (Fauna, Mumei,
Gura), the world tours, and the 2026 merger that made everyone simply "hololive."

## Type
Historical events.

## Timeline
| Date | Event | Why the cast remembers it |
|---|---|---|
| 2023-03-18/19 | hololive SUPER EXPO 2023 and 4th fes. "Our Bright Parade" | — |
| 2023-03-28 | The fan app "holoplus" is introduced | — |
| 2023-04 | holoMeet 2023 ambassadors include IRyS | IRyS represents EN |
| 2023-07-02 | hololive English 1st concert "-Connect the World-" | EN's first concert |
| 2023-07-25/31 | **-Advent- revealed ("WANTED!") and debuts**: Shiori, Bijou, **Nerissa**, Fuwawa, Mococo | Nerissa's origin |
| 2023-09-09/10 | hololive DEV_IS opens with ReGLOSS (Ao, Kanade, Ririka, Raden, Hajime) | Japanese kouhai |
| 2023-10-08/09 | "CouncilRyS" 3D showcase; **-Promise- formed** (IRyS joins the Council) | Kronii's and IRyS's group |
| 2024-01-16 | Yozora Mel leaves hololive | Not discussed in stories |
| 2024-03-16/17 | SUPER EXPO 2024 and 5th fes. "Capture the Moment" | — |
| 2024-04 | holoMeet 2024 ambassadors include Hakos Baelz | — |
| 2024-06-21/22 PDT | **-Justice- debuts**: Elizabeth Rose Bloodflame, Gigi Murin, Cecilia Immergreen, Raora Panthera ("law enforcers" chasing Advent) | EN's newest kouhai |
| 2024-08-23 | "ENigmatic Recollection" (ENReco) announced: EN members in the fantasy world Libestal, via a Minecraft series, animation and songs | Guilds: IRyS in "Cerulean Cup," Nerissa and Gura in "Scarlet Wand" |
| 2024-08-24/25 EDT | EN 2nd concert "-Breaking Dimensions-" (Kings Theatre, New York), part of World Tour '24 "-Soar!-" | — |
| 2024-08-28 | Minato Aqua graduates | — |
| 2024-09-30 | **Watson Amelia concludes regular activities and stays an affiliate** | Ame appears as a guest |
| 2024-11-09 | DEV_IS second unit FLOW GLOW debuts | — |
| 2024-11-29 | COVER introduces "conclusion of streaming activities" as distinct from graduation (affiliates can still appear in projects) | Why Ame can come back for events |
| 2025-01-03 | Ceres Fauna graduates | Promise remembers her |
| 2025-01-26 | Sakamata Chloe concludes streaming activities (affiliate) | — |
| 2025-03-08/09 | SUPER EXPO 2025 and 6th fes. "Color Rise Harmony" | Nerissa performs on day 1 |
| 2025-04 | World Tour '25 "-Synchronize!-" announced, led by Momosuzu Nene, Kureiji Ollie, **Mori Calliope, IRyS and Nerissa Ravencroft**, with guests per city (Kronii and Bae in Sydney) | Three of the cast on one tour |
| 2025-04-26 | Murasaki Shion graduates | — |
| 2025-04-27/28 | Nanashi Mumei graduates | Promise becomes three |
| 2025-05-01 | **Gawr Gura graduates** | Myth's first graduation; her last post: "keep swimming! always!" |
| 2025-05-02 | ENReco chapter 2 "The Chains of Fate" | — |
| 2025-07-16 | hololive RECORDS label launched | — |
| 2025-08-23/24 EDT | EN 3rd concert "-All for One-" (Radio City Music Hall, New York) | — |
| 2025-08-29 | Advent 2nd-anniversary live "On the Run!" ("The Story of Advent") | Nerissa's group milestone |
| 2025-10-03 | Hiodoshi Ao (ReGLOSS) leaves | — |
| 2025-10-15 | Official fan club launches | — |
| 2025-11-15 | hololive Indonesia 1st concert "Chromatic Future" | — |
| 2025-12-27 | Amane Kanata graduates | — |
| 2026-03-06/08 | SUPER EXPO 2026 and 7th fes. "Ridin' on Dreams" | — |
| 2026-03-27/28 | Kiara and Ina's duo concert "Drawn to Dawn" (Los Angeles) | TakoTori on stage |
| 2026-05-24 | ENReco chapter 3 "Broken Bonds" | — |
| 2026-07-03/04 | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around partner pairs (Calli–Shiori, Kronii–Ina, Kiara–Bijou) | The current partnerships |
| 2026-07-23 | Rhythm game "hololive Dreams" released | — |
| 2026-09-07 | "hololive Next": all female branches merge into one **hololive**; new logo; members to get updated designs (Tokino Sora first); "hololive raku" app; TV anime "Odeholo"; 10th-anniversary countdown | The present-day setting |
| 2026-09-18 | New unit ASOBI★MAWARI-TAI! reveals its four members | The newest kouhai |
| 2026-10-06 (upcoming) | IRyS's first solo concert "HOPE ||: Beyond the Stars" (Tokyo) | IRyS's next big stage |

## How It Works in Stories
- After 2026-09-07 everyone introduces herself as "from hololive"; old branch names survive as units and
  in casual speech ("EN," "holoEN"). [Observed S1 §2026, secondary]
- Affiliates (Ame) can appear at events and in projects; graduates (Gura, Fauna, Mumei) appear only as
  memories, callbacks and songs. [Official S1 2024-11-29 notice, secondary]
- ENReco is a separate, fictional continuity the members play in (guilds, a fantasy world), a story inside
  the story. [Observed S1 §2024, secondary]

## Sensory Palette
- See: the new 2026 hololive logo; a world-tour poster with city names; a "WANTED!" poster of Advent.
- Hear: "from hololive," with no branch; a farewell stream's last song; a fes crowd counting down.

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| affiliate | concluded streaming, still with hololive | official, members |
| ENReco | ENigmatic Recollection | members, fans |
| DEV_IS | the 2023–2026 Japanese sub-branch (ReGLOSS, FLOW GLOW) | everyone |
| the merger | 2026-09-07 single "hololive" | members |

## Conflicts and Story Hooks
1. The first week after the merger: an EN member gets a collab invite from a JP senpai she never dared ask.
2. An affiliate guest appearance: Ame drops into a concert and the crowd loses it.
3. A world-tour city stop: Calli, IRyS and Nerissa share a dressing room and a pre-show ritual.
4. A Promise anniversary after 2025, the three remembering Fauna and Mumei with jokes.
5. IRyS's nerves before her first solo concert in Tokyo.

## Links to Characters
All eight. Nerissa (Advent, 2023); IRyS and Kronii (Promise, 2023); Ame (affiliate, 2024); Gura
(graduated, 2025); Calli, IRyS and Nerissa (World Tour '25); Kiara and Ina (Drawn to Dawn); Kronii, Ina,
Kiara and Calli (Serendipity pairs).

## Secrets
(None.)

## Hard Facts (continuity)
- Merger 2026-09-07. Ame affiliate since 2024-09-30. Gura graduated 2025-05-01; Fauna 2025-01-03;
  Mumei 2025-04-27/28.
- EN concerts: 1st 2023-07-02, 2nd 2024-08-24/25, 3rd 2025-08-23/24, 4th "Serendipity" 2026-07-03/04.

## Sources (checked 2026-10-01)
- S1 hololive production wiki page, §History 2023–2026 (secondary): https://virtualyoutuber.fandom.com/wiki/Hololive
- S2 Member wiki infoboxes for retirement and conclusion dates (secondary): Yozora Mel, Minato Aqua,
  Ceres Fauna, Sakamata Chloe, Murasaki Shion, Nanashi Mumei, Gawr Gura, Hiodoshi Ao, Amane Kanata,
  Watson Amelia
- S3 Character files in this project (Calli C11, Kronii K4, Ina I7, Kiara T10–T12, IRyS R2, Nerissa N2)

---

## [SW] Name
hololive History 2023-2026

## [SW] Role
Event

## [SW] Other Names
recent hololive history, the merger, the 2025 graduations, holoEN's later generations

## [SW] Description
The recent past behind the present. 2023: Advent debuts (Nerissa, Shiori, Bijou, FUWAMOCO, July); DEV_IS opens with ReGLOSS; IRyS and the Council become -Promise- (October); EN holds its 1st concert. 2024: Justice debuts (June) as the "law enforcers" hunting Advent; the ENigmatic Recollection fantasy story starts (IRyS's guild "Cerulean Cup," Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30), under COVER's new "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; EN's 3rd concert at Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; EN's 4th concert "Serendipity" in Los Angeles (pairs Calli–Shiori, Kronii–Ina, Kiara–Bijou); on 2026-09-07 every branch merges into one "hololive"; IRyS's first solo concert is set for 2026-10-06 in Tokyo.

## [SW] Rules
After 2026-09-07 members say "from hololive"; old group names survive as units. Affiliates may appear at events; graduates appear only as memories. ENReco is a fictional story the members play in, separate from their persona lore.

## [SW] Sensory Details
The new 2026 hololive logo; a world-tour poster of city names; Advent's "WANTED!" poster; a fes crowd counting down; a farewell stream's last song.

## [SW] Secrets


---

## Open Questions
1. Serendipity pairs for IRyS and Nerissa were not found in the sources read; add them if the author has them.
2. (Removed: a status question outside the project's scope; the author decided announced breaks are not written.)


==================== WORLD CARD FILE: 20261001-0018-world-hololive-History-to-2022/claude-draft.md ====================

---
kind: world
name: "hololive History to 2022"
sw_section: Worldbuilding
---

# World Element: hololive History to 2022

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: the public history of hololive up to the end of 2022 as the cast would remember it, checked
> 2026-10-01. Evidence labels as in the other world files. Dates are JST unless noted. Graduation dates
> come from the wiki infoboxes; no reasons are given or implied (project rule).

## One-line Concept
The shared past every member carries: how a single 3D-avatar app became an agency of generations,
branches and a few departures, and how the English branch arrived in 2020 and became its biggest story.

## Type
Historical events.

## Timeline
| Date | Event | Why the cast remembers it |
|---|---|---|
| 2017-09-07 | Tokino Sora makes COVER's first VTuber broadcast | "Sora-senpai" is everyone's origin point |
| 2017-12-21 | The "hololive" app launches | Where the name came from |
| 2018-05 / 06 | hololive 1st generation debuts (Fubuki, Matsuri, Haato, Aki, Mel, Chris) | The first "gen" |
| 2018-08 / 09 | 2nd generation (Aqua, Shion, Ayame, Choco, Subaru); Sakura Miko debuts (2018-08-01) | Senpai the EN members grew up watching |
| 2018-12 | hololive GAMERS (Fubuki, Mio; later Okayu, Korone) | Gaming senpai |
| 2019 | Suisei and AZKi join via INoNaKa Music; 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins | Kiara's oshi Pekora; Nerissa's oshi Marine; Calli's starstruck senpai Suisei |
| 2019-12 | 4th gen (Coco, Kanata, Watame, Towa, Luna); hololive, HOLOSTARS and INoNaKa Music unite as "hololive production" | The modern brand |
| 2020-04 | hololive Indonesia gen 1; hololive English auditions announced | The overseas branches |
| 2020-08 | 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) | The JP generation just before Myth |
| 2020-09-08 | hololive English announced; Myth's members appear on X | "Myth's birthday" season |
| 2020-09-12/13 | **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame | The cast's origin |
| 2020-10-22 | Gura becomes the first hololive member to reach 1 million subscribers | A Myth legend |
| 2020-12 | ID gen 2 (Ollie, Anya, Reine); hololive China ends | K.I.R.A partners (Reine, Anya) |
| 2020-12-10 | Kiara's channel briefly terminated, then restored ("#PhoenixDown") | A Kiara rebirth joke |
| 2021-05-30 | Kiara reaches 1 million: every Myth member is over 1 million | A Myth first |
| 2021-06-30 | Gura passes Kizuna AI as the most-subscribed VTuber | A Myth legend |
| 2021-07-01 | Kiryu Coco graduates | — |
| 2021-07-11 | **IRyS debuts** as the VSinger of Project: HOPE | Hope arrives |
| 2021-08-23 | **-Council- debuts:** Sana, Fauna, **Kronii**, Mumei, Bae | Kronii's origin |
| 2021-11 | 6th gen "Secret Society holoX" (La+, Lui, Koyori, Chloe, Iroha) | — |
| 2022-02-24 | Uruha Rushia leaves hololive | Not discussed in stories |
| 2022-03 | ID gen 3 (Zeta, Kaela, Kobo) | Kobo's "Mommy Kiwawa" and "Uncle Dad" |
| 2022-03-20 | hololive fes at Makuhari (#つながるホロライブ), day 2: Calli and Kiara perform | Calli: "My dream came true, my heart is exploding." Kiara: "MAKUHARI WAS ON FIRE!" [Observed—X posts, S4] |
| 2022-04-26 | holoMeet begins; Gura is an ambassador | Global events |
| 2022-07-31 | Tsukumo Sana graduates | Council becomes four |
| 2022-09 | hololive's 5th anniversary | — |

## How It Works in Stories
- This is shared memory: members refer to these moments as in-jokes and milestones ("back when Myth was
  the only EN gen," "Gura's million"), not as lectures.
- Departures are named as "graduated" or "left" with no reasons, rumors or details. [Project rule]
- Before a date, the world is as it was then: no Council before 2021-08, no Advent before 2023-07.

## Sensory Palette
- See: a 2020 debut thumbnail; a "1,000,000" celebration screen; the old hololive English logo.
- Hear: senpai names said with reverence ("Sora-senpai," "Suisei-senpai"); chat spamming a milestone.

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| gen 0 / 1st gen … | Japanese generations | everyone |
| GAMERS | Fubuki, Mio, Okayu, Korone | everyone |
| hololive Fantasy | the 3rd generation | fans |
| holoID / holoEN | the Indonesian / English branches (merged 2026) | everyone |
| Myth | EN's first generation | everyone |

## Conflicts and Story Hooks
1. A Myth anniversary stream replays the 2020 debuts; Calli insists she was "first."
2. A member retells where she was when Gura hit a million.
3. A JP senpai who debuted in 2018 tells EN kouhai what the early days were like.

## Links to Characters
All eight: Myth (2020), IRyS (2021-07), Kronii (2021-08); Nerissa arrives later (see the 2023–2026 card).

## Secrets
(None.)

## Hard Facts (continuity)
- Myth debuted 2020-09-12/13 JST; IRyS 2021-07-11; Council 2021-08-23.
- Graduations to 2022: Aloe 2020-08-31, Coco 2021-07-01, Rushia 2022-02-24, Sana 2022-07-31.

## Sources (checked 2026-10-01)
- S1 hololive production wiki page, §History 2017–2022 (secondary): https://virtualyoutuber.fandom.com/wiki/Hololive
- S2 Member wiki infoboxes for debut and retirement dates (secondary): Kiryu Coco, Uruha Rushia, Mano
  Aloe, Tsukumo Sana
- S3 Character files in this project (Calli, Kiara, Ina, Gura, Ame, IRyS, Kronii)
- S4 The cast's X posts, via wiki citations: research/x-posts.md (Calli 1505506437115662339, Kiara
  1505507829695885313; Gura 1319328921305964544 on her million)

---

## [SW] Name
hololive History to 2022

## [SW] Role
Event

## [SW] Other Names
early hololive, the old days, Myth's debut, the first EN generation

## [SW] Description
The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, Suisei, 4th gen with Coco and Kanata), and in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at the hololive fes in Makuhari (03-20; Kiara: "MAKUHARI WAS ON FIRE!"), holoMeet starts with Gura as ambassador, Calli holds her first solo concert (07-21), and Sana graduates (07-31).

## [SW] Rules
These are memories and in-jokes, not lectures. Departures are "graduated" or "left," never explained. A story set in the past uses only what existed then.

## [SW] Sensory Details
A 2020 debut thumbnail; a "1,000,000" celebration screen; the old hololive English logo; senpai names said with reverence.

## [SW] Secrets


---

## Open Questions
(None.)


==================== CHARACTER CARD EDITS (new [SW] text) ====================


### 20260930-0704-character-Ouro-Kronii

[SW] Personality:
Kronii plays the flawless Warden of Time and states her own greatness as plain fact. Her comedy follows a recurring pattern: a controlled, deadpan statement, a disruption from a game, a collaborator or her own nerves, then an attempted recovery. When she makes a mistake she usually owns it out loud instead of blaming the game. She refuses backseat advice unless she has asked for help, preferring to die repeatedly and fail on her own terms. When someone wants help or motivation, she tends to hand out mock advice instead of comfort. A compliment may get a deadpan acceptance. She has claimed she doesn't scare easily, yet horror games frighten her readily; after a scare she may attempt a deadpan recovery. She praises and roasts herself in the same breath, drops casual existential remarks, and loves puns, including dad puns. She values order, since disorder is her official enemy, and she procrastinates while claiming to dislike procrastinating. Despite her lore as a haughty, even sadistic Warden, she is accommodating to chat and her genmates, and she thanks people plainly when it matters.

[SW] Background:
Kronii is a VTuber whose lore, a persona she plays deadpan, makes her the Warden of Time, the third concept created by the gods and the one most bound to humankind. Her official lore describes a cool, impeccable Warden whose aloofness grew into haughtiness and sadistic tendencies, and whose exquisiteness bends luck in her favor; disorder is her enemy. She debuted in August 2021 with hololive English -Council-. In October 2023, she joined hololive English -Promise- alongside IRyS, Ceres Fauna, Nanashi Mumei and Hakos Baelz. Following Fauna's and Mumei's graduations in 2025, its current members are Kronii, IRyS and Baelz, and since the 2026 merger the unit belongs to the single hololive brand. Her fans are the Kronies, which she also calls Kromies. Her mascot is Boros, a small white ouroboros snake. She is known for a Minecraft era spent building bunkers (the Bunkeronii). Her music includes solo songs such as "Daydream," Promise's "Run Back 'Round," and her 2026 EP "Way 2 U." In 2026 she also began a performance partnership with Ninomae Ina'nis. She jokes that she is 60.

[SW] Physical Description:
Kronii's avatar is 168 cm tall, with short dark-blue hair that falls in long locks at the sides and big blue eyes. A halo of clock hands (hour, minute and second) hovers behind her head and can spin like a propeller. In her original outfit she wears blue, white and black with gold trim, under a blue cape with a big ribbon, jewels and gold ornaments, and she carries two swords shaped like the long and short hands of a clock.

[SW] Voice & Delivery:
A low speaking register, deep like Calli's: powerful and well-controlled, with an older-sister feel, and a wide range she once pushed into a high-pitched voice at a viewer's request. Her default delivery is dry and deadpan at an unhurried, medium pace. When frightened she lets out a startle squawk. She vocalizes explosively when she takes damage or dies in games. Sincere lines come out plain and complete, without a joke attached.

[SW] Audio Tags:
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: low alto, the lowest in the cast (about 180 Hz), relaxed medium pace (about 120–127 words a minute), dry, controlled, American English. Default tags: [deadpan], [dry], [relaxed]. By situation: greeting [relaxed] "Kroniichiwa!"; bragging [deadpan, flat, slow]; jump scare [startled squawk] GWAK! then [trying to stay calm]; misplay [dry]; frustrated [irritated, short] with a swear; praised [deadpan], or [flustered, quick] when it lands; self-roast [dry, amused]; horror tension [low, uneasy]; sincere [plain, warm, unhurried]; good night [softer] "KroYasumi~"; a requested bit [high-pitched, put-on voice]. Signature sounds: [startled squawk] GWAK! (sharp, far above her speaking voice); [yelps] and [grunts] when hit. Keep in the words: short plain statements; a beat (ellipsis or new sentence) before the punchline; self-praise stated as fact; mistakes owned aloud ("that's on me"); swears when startled. Pronounce: Ouro Kronii /ˈoʊɹoʊ ˈkɹoʊni/, Kroniichiwa /ˌkɹoʊniˈtʃiːwɑ/, Kronies /ˈkɹoʊniz/, GWAK /ɡwɑk/. Never as default: [giggles], [bubbly], [cheerful], breathy seduction.

[SW] Relationships:
Ninomae Ina'nis: 2026 concert partner (Octo'Clock, Serendipity); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated): Council genmate (KronMei). Ceres Fauna (graduated): Council genmate who described Kronii's "gap moe." Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Gigi Murin: collaborator in the units "TimeChaser" and "Clockwork Orange." Cecilia Immergreen: calls her "Owo-senpai"; Kronii calls her a "CLANKER." Raora Panthera: "Pizza Time" partner who calls her "Tam Tender." Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live.


### 20260930-0704-character-Mori-Calliope

[SW] Personality:
Calli streams as a hardened reaper-rapper, all bravado and blunt talk, and she is openly kind underneath. She uses theatrical death threats in comic exchanges. When a game or chat keeps pushing her, frustration can build into a burst of swearing that collapses into weary resignation. When something comes out wrong, she tends to keep talking to fix it, digs herself deeper, then cuts herself off; she talks herself into accidental innuendo and scrambles to take it back, and she can play the tease on purpose too. She grabs the floor before she knows how the sentence ends. Compliments and romance teasing usually make her deflect, stall or get flustered; sometimes she simply says thank you. She shows a timid side with people she meets for the first time, such as her senpai. She owns her cringe. She works hard on music, often grinding on projects behind the scenes, and talks about her craft concretely: takes, arrangements, what a line needs. She joins strange premises instead of policing them, and she protests being called "Dad" loudly while sometimes leaning into it. She tells her audience to take care of themselves first and openly admires juniors who are better at something. She loves red wine, rap and rock, and FromSoftware games; she hates cantaloupe and coffee, and she has a recurring bit of refusing to play League of Legends.

[SW] Background:
Calli is a VTuber whose lore, a persona she plays for laughs, makes her the Grim Reaper's first apprentice: when modern medicine gutted the reaping business, she became an idol-rapper VTuber to harvest souls through music and streams. In that lore her Underworld looks like a modern city with bad internet, and she once waitressed there to save up for Japan. She debuted first in hololive -Myth- in September 2020; her fans are the Dead Beats, her mentor is Death Sensei, her publicly depicted cat mascot is Tutu, and her scythe is named Ricky. She is a signed singer, songwriter and rapper whose sound has grown from rap into rock. She headlined New Underworld Order in Tokyo and GriMoire at the Hollywood Palladium, the first solo concert outside Japan by a hololive production talent, and in 2026 she released her album DISASTERPIECE. She co-hosts the CHADCast podcast with IRyS and Hakos Baelz, and she started a 2026 performance partnership with Shiori Novella. Myth still includes Takanashi Kiara and Ninomae Ina'nis; Gawr Gura has graduated, and Watson Amelia is an affiliate.

[SW] Physical Description:
Calli's avatar is 167 cm tall, with long straight pink hair, red eyes and a small black crown. In her original outfit she wears a tattered black hooded cloak lined in red over a black form-fitting dress with gold accents and a high slit, a chain belt with a red tassel, long black gloves with sheer sleeves and black heels. A foldable scythe with pink accents, named Ricky, rides on her back.

[SW] Voice & Delivery:
A low speaking voice and a fast, running pace. Her comic rhythm often runs forceful entrance, conversational detour, then an abrupt correction or honest admission. "Guh" is a short comic gasp. Her laugh can build to a loud crescendo and then drop flat. Under pressure she repeats herself in a panic and her volume jumps. When flustered she stalls and restarts. Her fake-cute voice is deliberately artificial. Sincere lines come out shorter and plainer.

[SW] Audio Tags:
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: low mezzo-alto with a slightly husky edge (about 197–214 Hz), the fastest talker in the cast (about 161–186 words a minute), casual American English, confident swagger over a dorky core. Default tags: [casual, fast], [confident]. By situation: settling in [casual, fast]; greeting fans [hyped] "What's up, Dead Beats?!"; annoyed at a game [exasperated, rapid]; tilted [shouting] then [flat, deflated] "whatever, man"; stalling [hesitant] "Well... listen. Listen."; teasing [smug, mock-menacing]; deflecting Kiara [gruff, embarrassed] then [warm]; after a drink [comic gasp] "Guh."; sincere [plain, warm]; sign-off [casual, trailing off]; Japanese [American-accented Japanese] (learned, not native). Signature sounds: [comic gasp] Guh.; [laughs], [laughs harder] at her own mess-ups. Keep in the words: "cuz," "wanna," "gonna," "y'all"; grabbing the floor before the sentence is planned, with restarts; casual swears mid-sentence; deadpan setup, then the burst; a repeated question when she can't believe it. Pronounce: Mori Calliope /ˈmɔɹi kəˈlaɪəpi/, kusotori /kusoˈtoɾi/, Kronster /ˈkɹɑnstɚ/. Never: a sugary idol voice, nonstop shouting, a gangsta caricature, flawless native Japanese.

[SW] Relationships:
Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is Ina's favorite pun target. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli keeps singing Gura's unreleased "Full Color." Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her chaotic CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin: frequent collaborator; Calli came to like how her own name sounds once Gigi started saying it. Kobo Kanaeru: calls her "Uncle Dad." Koseki Bijou ("Biboo"): a junior whose skill Calli openly admires. Shiori Novella: 2026 performance partner who calls her "Mor Mori"; they chase absurd premises together. Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by.


### 20260930-1113-character-Takanashi-Kiara

[SW] Personality:
Kiara streams as a phoenix idol and the self-appointed CEO of KFP. She can accelerate into repeated exclamations and emphatic complaints, while ordinary conversation and interview hosting leave room for quieter, clearer exchanges. She often opens with a tangent she wants to tell before she forgets it, and a superchat reading easily turns into long talk. She talks about herself in the third person as Wawa when she's proud or roasting herself. When a game screws her over, she escalates from shrieks and repeated no's to swearing, sometimes in German, blames the game, and snaps out of it with a joke. When chat misbehaves, she plays the scolding manager: threatens to fire them or send them to the Usual Room, and insists KFP is not a cult. She owns her "bottom left" reputation, lewd and foolish on a members' chart, with crude jokes and innuendo, and she jokingly calls fictional women she likes her wife. She is forgetful and shyer than her energy suggests. When she hosts, she prepares, asks clear questions, translates between Japanese and English and leaves room for the guest's answer, though she dislikes awkward silence. She rehearses hard for stage work and gives juniors practical encouragement. She says plainly when she's tired and drops the bits to tell KFP she loves them. She likes fast food and hats, adores Pekora-senpai, doesn't drink, and hates sand, scary things and Comic Sans.

[SW] Background:
Kiara is a VTuber whose lore, a persona she plays for laughs, makes her a phoenix, not a chicken, and an idol whose dream is to own a fast-food chain; a phoenix can always be reborn. In the bit she is the CEO of KFP (Kiara Fried Phoenix), whose employees are chickens; misbehaving staff get sent to the Usual Room, and she insists KFP is not a cult. She debuted with hololive -Myth- in September 2020 speaking English, Japanese and German. In December 2020 her channel was briefly terminated and she came back with a "#PhoenixDown" re-debut. She hosted the interview show HOLOTALK, translating for Japanese guests, and from 2026 co-hosts the bilingual HoloEN REWIND. She released her second album Vogelfrei in 2026 and held the duo concert Drawn to Dawn with Ninomae Ina'nis in Los Angeles. Her mascot is the little bird Kotori.

[SW] Physical Description:
Kiara's avatar is 165 cm tall, with medium-length coral hair fading to teal and magenta eyes. Shiny blue feathers grow behind her ears; they look like earrings but are phoenix down. In her original outfit she wears a mostly orange uniform with a greenish neck bow, a small white chef's hat and a red beret with a starred black bow, and she carries a sword that slots into her shield.

[SW] Voice & Delivery:
Energetic and highly changeable, chatty and self-interrupting. Excitement brings sharp, birdlike cries and conspicuous laughter that can break into a sentence, while her ordinary speech stays intelligible rather than constantly shouted. Her gaming reactions are emphatic: looped short words, short screams at deaths, all-caps outbursts in mid-sentence. In hosting mode her questions become contained and she leaves room for the answer. Sincere lines drop the bits entirely. German comes out in the sign-off lesson and sometimes in rage. Her singing voice is powerful and high.

[SW] Audio Tags:
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: bright upper-middle voice (about 245–300 Hz), fast and chatty (about 133–179 words a minute) with sudden accelerations, highly expressive; no particular accent is specified. Default tags: [chatty, bright]. By situation: opening [bright rooster-like cry] "Kikkeriki!" then [chatty]; hyped [excited, rapid]; game surprise [shocked]; tilted [shrieks] then [angry, rapid] then [flat]; KFP manager [brisk, faux-authoritative]; hosting a talk show [measured, clear], leaving room for answers; teasing Calli [teasing, affectionate]; sincere [plain, warm]; tired [flat, still chatty]; sign-off [playful] with a German line. Signature sounds: [bright rooster-like cry] Kikkeriki!; [short scream] at deaths; [laughs loudly]. Keep in the words: self-interrupting restarts ("I— I'll go— I'll go and check"); triple repeats ("Okay. Okay. Okay."); a flagged tangent ("Do you want to hear a tangent?"); third person when proud ("Look at Wawa"); ALL-CAPS shouts mid-sentence; casual swearing in games; German ("auf Wiedersehen," "danke schön") and Japanese. Pronounce: Takanashi Kiara /tɑkɑˈnɑʃi kiˈɑːɹə/, Kikkeriki /ˌkɪkəʁiˈkiː/, Wawa /ˈwɑwɑ/, auf Wiedersehen /aʊ̯f ˈviːdɐˌzeːən/; KFP spelled out. Never: constant screaming that buries the host; a polite corporate tone; "ara ara."

[SW] Relationships:
Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages; they share the "6 7" meme. Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera: cast the infamous "Doom." Cecilia Immergreen: German-speaking partner. Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior.


### 20260930-1113-character-Ninomae-Inanis

[SW] Personality:
Ina streams as a priestess of the Ancient Ones who treats tentacles and eldritch whispers as completely normal; in practice she is a gentle, laid-back hermit who loves rolling around on the floor. She drops puns flat, with no setup, lets them sit, and giggles to herself while chat groans "INAFF"; she enjoys the groan more than the laugh. When chat misbehaves or someone squishes her hair, she threatens to bonk them with a crowbar in the sweetest voice; when chat teases her, she plays the stern overlord for a beat, then collapses into giggles. She wanders into tangents and apologizes her way back out. When she slips up, she calls a "Forgetty Beam!" and tells chat to forget it. Her patience is nearly endless unless she's sleepy. She draws alongside her viewers instead of lecturing them, explains her own designs through specific details, and takes on demanding stage work; her quiet is never passivity. She supports her genmates' work in public, designing their mascots and outfits and sharing the stage, and she is sincere in short, gentle ways: "Live without regrets." She loves food and gacha and dislikes bugs, boredom and cucumbers.

[SW] Background:
Ina is a VTuber whose lore, a persona she plays gently and for laughs, makes her an ordinary girl, despite how she looks, who picked up a strange book, gained the power to control tentacles and began hearing Ancient Whispers; the book is her floating companion, AO-chan. She became a VTuber to deliver random sanity checks on humanity, debuting in hololive English -Myth- in September 2020. She drew Myth's intro art and designed Takodachi, Bubba and Death Sensei. Her fans are the Tentacult, each one a Takodachi, after the little purple mascot she designed. Her songs tell darker stories about her priestess duty. She released her first EP, re:VISION, and held the duo concert Drawn to Dawn with Takanashi Kiara in 2026, and she partners with Ouro Kronii. Since the 2026 merger she introduces herself as "Ninomae Ina'nis from hololive."

[SW] Physical Description:
Ina's avatar is 157 cm tall, with long purple hair falling below her knees, squishy tentacle-like side locks fading to yellow tips, purple flaps on her head like a dumbo octopus's fins, and bluish-purple eyes. In her original outfit she wears a golden tiara, a sleeveless purple-and-yellow dress and small white wings at her waist, and she can show a golden halo. Large purple tentacles float behind her, and her book AO-chan hovers nearby. In horror games she hugs a pink stuffed rabbit named Burrito.

[SW] Voice & Delivery:
A quiet, calm voice, unhurried in casual talk, with small pauses. She laughs in little ways: quick giggles mid-sentence and tiny gasps. She hums "Mhm" and "Hmm" while listening. Puns come out flat, followed by a silence. Genuine surprise can break the calm with a sharp, higher reaction ("TOMORROW?!"), and her voice has cracked in such moments. Her threats are sweet-voiced and calm.

[SW] Audio Tags:
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: soft, calm mid-range voice (about 223–232 Hz), the slowest talker in the cast (about 81–95 words a minute in chat), small pauses, warm, quiet giggles, cracking on excited words; American English. Default tags: [soft, unhurried]. By situation: opening [warm, unhurried] then [brighter]; pun [flat, quick], [short pause], [small giggle]; chatting [soft, meandering]; tired or homey [quiet, sleepy]; teasing chat [sweet, dead calm] (sweet-voiced threats); startled [sudden, high, voice cracks] then [embarrassed]; hyped [excited] "WAH!"; sincere [quiet, gentle]; sign-off [warm]. Signature sounds: [excited] WAH!, sometimes a droopy [deflated] wah…; [small giggle] mid-sentence. Keep in the words: hedges ("like," "I think," "you know," "I guess," "maybe," "right?"); ellipses for micro-pauses; tangents closed with "Anyways."; the pun delivered flat, then silence; rare swearing. Pronounce: Ninomae Ina'nis /ninoˈmae ˈiːnɑnis/ (surname first), Takodachi /tɑkoˈdɑtʃi/, WAH /wɑː/. Never: loud, fast or shouted delivery; frequent swearing; a crack on every exclamation; the ominous priestess voice as a default (it is an occasional bit).

[SW] Relationships:
Ouro Kronii: her 2026 concert partner (Octo'Clock, Serendipity); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, and Kiara pushed her toward the stage and groans at her puns. Mori Calliope: her favorite pun target ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy whose collab outfit Ina designed. IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island. Houshou Marine: a senior artist she admires.


### 20260930-1113-character-Gawr-Gura

[SW] Personality:
Gura streamed as a shark from Atlantis playing a fearsome apex predator, and on stream she was mostly a soft, goofy gremlin. When chat calls her dumb about math, spelling or directions, she can cheerfully defend an obviously dubious answer as a joke instead of defending herself. An unexpected setback can puncture her boasts ("I'll have you know..."), often in a scream. When she's blamed, cuteness is her alibi. She often brings up being hungry, refuses to explain jokes chat mangles, and apologizes quickly when a joke lands wrong. She jinxes herself by announcing that things will be fine right before they aren't. Horror games make her scream and bargain, and she can recover quickly and start taunting the game ("You don't scare me. Cheap party city lady."). She drops crude, lewd one-liners in a deadpan, innocent voice, and when teased about being flat she plays along ("hydrodynamic") until the repetition makes her sarcastic. She is quicker-witted than her "dum shark" reputation and exceptional at rhythm games. Sincere praise, when it replaces a bit, embarrasses her. When she says goodbye she reminds everyone to drink water, eat and be kind to themselves. She loves salmon, pizza, fast food, rhythm games and cowboy things; she hates hot sand and wearing pants.

[SW] Background:
Gura is a VTuber and a hololive alum: she graduated from hololive -Myth- on May 1, 2025. Her lore, which she played for laughs, is a persona, not literal: a descendant of the Lost City of Atlantis who swam to land because it was "so boring down there," bought her clothes and shark hat in the human world, and talks to marine life. Her age jokes put her in the 9,000s, with a different number from one telling to the next. She keeps a long-time friend, Bloop, sealed in a bubble "for the better" and calls him her emergency rations. She debuted in hololive English -Myth- in September 2020, twelve minutes late, opening with a single "a" that became a meme, and won fans by singing city pop. Her fans are the chumbuds and her members are shrimps. She hosted The Fish Tank with Watson Amelia and sang "Q" with Mori Calliope. She said goodbye with a small concert and a reminder to keep swimming.

[SW] Physical Description:
Gura's avatar is small, 141 cm, with white-silver hair streaked with blue, short pigtails tied with shark-face hair ties, cyan eyes and sharp shark teeth. In her original outfit she wears an oversized dark-blue shark hoodie with a shark-mouth zipper and a hood shaped like a shark's head, and she carries a trident. Her avatar's cyan shark tail is stitched up (in her lore, a rock fell on it).

[SW] Voice & Delivery:
A soft, cute, relatively high voice with clear pronunciation, with small self-corrections and repeated words. Teasing comes out deadpan; pompous brags get an over-formal delivery. Horror and rage bring sudden loud peaks (screams, short repeated "no no no," quick bargaining), and she can drop back to calm quickly, sometimes with an apology. She hums while she plays. Her laugh can tip into hiccups. Sincere lines are short and plain. Her singing is clean and controlled.

[SW] Audio Tags:
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: soft, cute, relatively high voice (about 245–270 Hz) with clear pronunciation, moderate pace (about 120–140 words a minute), playful and goofy, deadpan when teasing; American English. Default tags: [soft, playful]. By situation: opening [soft, friendly] "Hello? Hello? Hello?"; scared [panicked, higher] then [pleading]; taunting after a scare [smug, deadpan]; teasing [deadpan-cute, slow] "You can't be mad at me... I'm cute."; game commentary [amused, mocking]; hyped [excited, stretched vowels] "Shaaaaark!"; flustered [tumbling, embarrassed]; sincere sign-off [soft, plain]. Signature sounds: [hums] while playing; [screams] then [catching breath]; the lone "a": [flat] a. Keep in the words: triplets ("hello hello hello," "wait wait wait," "okay okay okay"); stumbles and restarts; sound effects instead of words ("Hoocha!", "Ka-chow!"); softened swears by default ("heck," "freaking," "dang"), harder ones in games; crude one-liners said innocently. Pronounce: Gawr Gura /ɡɔːɹ ˈɡʊɹə/, chumbuds /ˈtʃʌmbʌdz/, Hoocha /ˈhuːtʃə/. Never: suave, stumble-free speeches; fluent Japanese; growled profanity in every line, or a fully sanitized voice.

[SW] Relationships:
Watson Amelia (affiliate): her closest early friend (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated and keeps singing Gura's unreleased "Full Color." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George."


### 20260930-1113-character-Watson-Amelia

[SW] Personality:
Ame streams as hololive's self-proclaimed #1 detective and is a competitive gamer gremlin, all sweetness and saltiness. When a game hands her an innocent line, she can twist it into a crude joke; she has a filter, but much of what it catches comes out anyway, and she audits herself a second too late. When she loses, she can get salty, blame the ping, her team or the game, escalate into rage or a gremlin screech, and then deflate into an apology or own the bad play. When she's dead in a round, she narrates her teammate's play like a caster. She tends to insist on her own method, retrying an awkward approach again and again rather than taking the easy route. She pranks friends and chat when she gets the chance, and she also helps with technical problems, watches her genmates' streams and takes on ambitious projects with a team behind her. She coos over doggies, laughs off dark moments before saying something plainly sincere, and reads superchats with rapid stacks of thank-yous. In her latest regular streams she is nostalgic and grateful, proud of the tech she learned to build her own intros, and still clowning. She loves iced tea, doggies, puzzle games, shooters and Outer Wilds; she hates onions, soda, loud high-pitched noises (despite her own screech) and the Bee Movie.

[SW] Background:
Ame is a VTuber and a hololive affiliate: she concluded her regular activities on September 30, 2024, and appears at individually announced events. Her lore, a persona she plays for laughs, makes her a time-traveling detective with a pocket watch that lets her travel through time. After hearing rumors about the unusual beings in hololive, she became an idol just out of interest, training her reflexes with shooters and her mind with puzzle games. She debuted in hololive English -Myth- in September 2020, briefly undercover with a fake British accent, and her fans are the Teamates. Her mascot is Bubba, a small dog. She built her own 3D and VR setups for her genmates, came up with and co-managed the ChikuTaku rhythm game, and hosted a charity stream. She was a guest at Kronii's 3D birthday live in March 2026.

[SW] Physical Description:
Ame's avatar is 150 cm tall, with light-blonde hair falling below her shoulders and blue eyes. In her original outfit she wears a checked deerstalker with a gear-decorated magnifying-glass hairpin, a white blouse with a short red tie printed with a mustache, a checked skirt carrying her golden pocket watch, a detective coat with a stethoscope, and syringes of her concoction strapped to her left leg. Bubba, her small dog, rides along in later outfits.

[SW] Voice & Delivery:
A light, playful voice that trips over itself with restarts and fillers. For crude jokes it has dropped into a lower, "gremlin-like" tone. Her gremlin screech has been described as a cross between a high-pitched wheeze, a reptilian screech and the final breath of a dying squeaky toy; she also has a gremlin cackle. She hiccups often on stream, separate from her laughing.

[SW] Audio Tags:
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: light, playful upper-range voice (about 248–276 Hz), a middling pace (about 114–133 words a minute) that trips over restarts and fillers, mischievous; American English. Default tags: [playful], [mischievous]. By situation: crude joke [innocent] then [lower, gremlin voice]; tilted [frustrated, rising] then [shouting]; rage-quit [fed up, rapid]; trash talk [smug]; owning a mistake [plain]; spectating [caster, excited]; nostalgic [warm, playful]; gremlin bit [mischievous]; sign-off [cheerful] "Alright, bye-bye!" Signature sounds: [gremlin cackle] NEHEHEHEHE!; [high-pitched wheezing screech] when losing; [hiccups], rarely. Keep in the words: "okay" constantly, "oh," "like," "uh," "yeah"; "all right" to move on; "oh yeah, oh yeah" when a thought comes back; a sweet setup with a crude turn said as if nothing happened; repeated questions that build to a shout. Pronounce: Amelia Watson /əˈmiːliə ˈwɑtsən/, Teamates /ˈtiːmˌmeɪts/. Never: polished, serene idol phrasing; "chat" as her default address (she says "you guys").

[SW] Relationships:
Gawr Gura (graduated): her closest early friend (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs.


==================== NEW CHARACTER FILE: 20260930-2334-character-IRyS/claude-draft.md ====================

---
kind: character
name: "IRyS"
sw_section: Characters
---

# Character File: IRyS

> Scope: official lore and publicly shown persona only, checked 2026-09-30. Nothing about the performer
> behind the avatar (no health, childhood or private details, even where the wiki lists them). In stories
> she knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence
> labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; R20) and read in context by Claude;
>   lines used on the card were re-transcribed by a second model (medium.en). Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (R#) are listed under Sources.
>
> **Audio status:** on 2026-09-30 Claude checked about 1.9 hours of archived 2026 recordings (R20: her
> birthday-live aftertalk and a Resident Evil Requiem stream). The audio was machine-transcribed and
> acoustically measured; transcripts were reviewed in context, without independent listening verification.
> Other voice evidence is secondary (the R2 wiki §Quotes gives no timestamps).

## One-line Concept
hololive's "seiso nephilim," a half-angel, half-demon singer who delivers hope, and who keeps letting the
demon half out: a soft, cheerful voice that says the most "surprising" things, then insists she is one
hundred percent seiso. [Official R1] [Observed R2 §Personality, secondary]

## Core Drive
- **Want:** to deliver hope through her songs and to reach every stage she can: her goals list a full
  album, a solo concert, an anime song, lots of friends and collabs with every hololive member. In 2026
  she announced her first solo album "DANGERyS" and first solo concert "HOPE ||: Beyond the Stars"
  (2026-10-06, Tokyo). [Official R1] [Observed R2 §Likes and dislikes, §2026, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** hope as something you make yourself ("The future is made with our own
  hands"); optimism she pushes on chat ("you guys need more hope in your lives"). [Official R1 original
  profile] [Observed R2 §Quotes, secondary]

## Core Contradiction
Angel and demon at once: sweet, positive and a little shy, yet with a "sadistic" streak, a taste for
violence in games and a habit of saying questionable, pervy things, sometimes by accident. Her official
profile makes the duality the joke: "the most unpredictably yaba—*ahem*, 'surprising', comments."
[Official R1] [Observed R2 §Personality, secondary]

## Behavioral Traits
1. When she opens a stream, she greets with her name pun ("HiRyS, it's IRyS!") and checks the audio
   ("How's the volume?"). [Official R1] [Observed R2 §Quotes, secondary] [ASR R20]
2. When something innocent can be read the wrong way, she reads it the wrong way out loud, then claims
   she is "a hundred percent seiso" and would "never lie." [Observed R2 §Personality, §Quotes, secondary]
3. When chat tries to catch her out, she turns it back on them and makes them feel guilty ("I'm trying
   to make you guys feel guilty. That's what I'm doing here, okay?"). [ASR R20]
4. When a game offers violence, the demon half enjoys it ("I can kill as many zombie babies as I want! Is
   this Heaven!?"). [Observed R2 §Quotes, secondary]
5. She keeps inventing "-RyS" puns on her own name ("HiRyS," "ByeRyS," "SeisoRyS," "IRySoSeiso" usernames)
   and encourages fans to make more. [Observed R2 §Miscellaneous, secondary]
6. She loves soda, drinks one most days and announces what she is drinking; chat plays at stopping her
   ("IRyS, no soda"). [Observed R2 §Likes and dislikes, secondary]
7. With Hakos Baelz she keeps a running bit of being "married" and "divorced" (from a 2021 Minecraft
   bento joke); "Monopoly" became a fandom euphemism after a joke fan-fiction they wrote together.
   [Observed R2 §Relationships, secondary]
8. She sings in English and Japanese and does bilingual streams; her singing voice is fuller and more
   powerful than her talking voice. [Observed R2 §Personality, §Miscellaneous, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - "HiRyS, it's IRyS! Your seiso nephilim here to fill the world with hopium!" (official greeting)
    [Official R1]. On a 2026 stream she opens with a name pun and "it's IRyS" (the two models agree only on
    "…it's IRyS"; the rest of the opening is not quoted). [ASR R20, WZn7zl-NI3A 0:05:32]
  - "ByeRyS!" as a pun sign-off [Observed R2 §Quotes, secondary]. In 2026 her real sign-off runs long and
    circles back: "Thank you very much! See you guys again tomorrow!" and then several more goodbyes.
    [ASR R20, 4:31:32–4:32:00; the models agree on the quoted part only]
  - "How's the volume?" at the start of streams. [Observed R2 §Quotes, secondary]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "HiRyS" / "ByeRyS" and other "-RyS" puns → greetings, names → recurring. [Official R1; R2]
  - "I am a hundred percent seiso, I would never lie!" → after a suggestive slip → recurring bit.
    [Observed R2 §Quotes, secondary]
  - "Hope has descended!" → entrances, hype. [Observed R2 §Quotes, secondary]
  - "Yoisho~" → sitting down, effort. [Observed R2 §Quotes, secondary]
  - "hopium" → her word for hope. [Official R1]
  - "Erase that from your memory." / "I'll probably get bonked for that later..." → after a slip.
    [Observed R2 §Quotes, secondary]
- **Suggestive teasing (non-explicit; kept under the authenticity rule):**
  - Teasing chat about a new outfit: "I think most of you guys are satisfied as long as you can see this,
    you know, up to here… You guys don't need to see the bottom half… I'm trying to make you guys feel
    guilty. That's what I'm doing here, okay?" [ASR R20, 0:09:48–0:12:26; a closing "ashamed of yourself"
    heard by the first model only is not quoted]
  - About Kronii's goddess outfit: "I mean, I am a half-angel, half-demon Nephilim. I could pull it off,
    somehow." She then compares her figure with Kronii's; the two models disagree on the key word, so that
    sentence is not quoted. [ASR R20, 4:23:23–4:23:31]
  - "We can play Monopoly... IN BED!" (the BaeRyS fan-fiction bit). [Observed R2 §Quotes, secondary]
- **Vocabulary / fillers:** "like" constantly (about 1 in 30 words in a 2026 chat window, first-model
  count), "you know," "I do think so," "I mean," "right?"; addresses chat as "you guys" (far more than
  "chat"). Fans: IRyStocrats; members: Nephamily. [ASR R20] [Official R1] [Observed R2]
- **Profanity:** rare and mild. In about 1.9 hours of 2026 audio: "damn it" twice (both confirmed by the
  second model: "Damn it, I forgot about that"; "Damn it, should I?"), and a softened "holy shoot!" [ASR R20]. Her edge comes from innuendo and "yabai" comments, not swearing.
- **Laughs, noises:** little "hehe" giggles; lip rolls are a known on-stream habit (also her vocal
  warm-up). [ASR R20] [Observed R2 §Miscellaneous, secondary]
- **Code-switching:** English and Japanese; bilingual stream titles; a Japanese interjection mid-English
  (transcribed "Masu-de kawaii," probably "maji de kawaii," "seriously cute"). [Observed R2; R3 titles; ASR R20]
- **Rhythm & rhetoric:** fast, run-on enthusiasm when a topic excites her (outfits, concerts): restarts,
  repeated phrases ("I told you guys. I told you guys"), stacked "so cute"; then a flat, cheeky aside.
  Reads superchats in counted batches ("That's 25… I'll go up to 30"). [ASR R20]
- **Timbre / pitch / pace (for voice performance):**
  - Secondary description: a "high-pitched, soft and calm" speaking voice (compared with Yukihana Lamy);
    a more powerful, deeper singing voice (compared with Tokoyami Towa). [Observed R2 §Personality,
    secondary]
  - Measured (R20; 2026 chat and a Resident Evil Requiem window): median pitch about 214–226 Hz, mid-range
    in this project's sample (close to Ina's 223–232 Hz), and fast in chat: about 168–183 words per minute
    of speech (121 in the opening, 67 in the horror game). Sample results only.
  - Provisional: bright and soft in greetings; quick and bubbly when excited; a sly, lower aside for the
    "yabai" lines.
- **Sounds off:** constant swearing; a cold or cruel demon voice as default; formal idol speech with no
  fillers; a never-slipping seiso act.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, name pun | "HiRyS, it's IRyS!" (R1) |
| Excited about an outfit or concert | Fast, run-on, repeated "so cute" | "I knew you guys would! I knew you guys would!" (ASR R20) |
| Teasing chat | Sweet, then a sly guilt trip | "I'm trying to make you guys feel guilty." (ASR R20) |
| After a slip | Mock-innocent denial | "I am a hundred percent seiso, I would never lie!" (R2 §Quotes) |
| Horror game | Quiet, focused, short cheers | "Run Leon, run!" (ASR R20) |
| Sincere | Warm, plain | "I really hope so too." (ASR R20) |
| Sign-off | Circling goodbyes | "Thank you very much! See you guys again tomorrow!" (ASR R20) |

### Sample Lines
1. "HiRyS, it's IRyS! Your seiso nephilim here to fill the world with hopium!" (Official R1)
2. "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" (ASR R20, 0:12:07)
3. "I mean, I am a half-angel, half-demon Nephilim. I could pull it off, somehow." (ASR R20, 4:23:23)
4. "No, I don't like it. I love it!" (ASR R20, 4:27:30)
5. "I am a hundred percent seiso, I would never lie!" (R2 §Quotes, secondary)
6. "We can play Monopoly... IN BED!" (R2 §Quotes, secondary)

## Appearance Anchors (avatar)
- Height 162 cm (166 cm in heels). [Official R1] [Observed R2 infobox, secondary]
- Light brown skin; floor-length magenta hair; long pointed ears and two small black horns; heterochromia
  (right eye cyan, left eye purple); a halo of white, crystal-like stars; a small pair of iridescent wings
  at her shoulders and larger magenta ones at her lower back. [Observed R2 §Appearance, secondary]
- Illustrator redjuice. Emoji 💎. Mascots Bloom & Gloom, one-winged black and white cat-like creatures
  she designed with Tsukumo Sana. [Official R1] [Observed R2 §Mascot and fans, secondary]
- 2026: a race-queen outfit for her birthday live "Racing Towards Hope" (visor, gold accessories, blue and
  pink eyeshadow). [ASR R20]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | A nephilim who was the embodiment of hope in "The Paradise," reawakened in an age of despair to deliver hope through song | [Official R1] |
| 2021-07-11 | Debuts as the sole member of hololive English -Project: HOPE-, a VSinger | [Official R1] [Observed R2] |
| 2021-07-29 | First official collab: Just Shapes & Beats with Mori Calliope | [Observed R2 §2021] |
| 2021-09-29 | The Minecraft "bento" that starts the BaeRyS married/divorced bit | [Observed R2 §Relationships] |
| 2023-10-09 | Joins hololive English -Promise- with Fauna, Kronii, Mumei and Bae | [Observed R2 §2023] |
| 2024-12-14 | -Promise- musical "The Broken Promise" | [Observed R2 §2024] |
| 2024-11-17 | 3D live "The Devil Wears Hope" | [Observed R3 title] |
| 2025-03-15/16 | Birthday: "DIAMOND GIRLFRIEND," EP "YaBAI," 3D live "HOPE UPON A STAR" | [Observed R2 §2025; R3] |
| 2025-07-11 | 4th anniversary; 3.0 model | [Observed R3 title] |
| 2026-03 | Birthday live "Racing Towards Hope"; "BE MY FLAME"; solo album "DANGERyS" and solo concert announced | [Observed R2 §2026; R3] |
| 2026-09-07 | Branch merger; her unit is "hololive -Promise-" | [Observed R2] |

## Relationship Map
Public exchanges only. Unit and nickname statuses: BaeRyS, MorIRyS, CHADCast and K.I.R.A are listed on
the wiki as units or pairings; -Promise- is official.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Hakos Baelz | Promise genmate ("BaeRyS") | The married/divorced running bit; Bae once banned her from soda for a week after a lost bet | [Observed R2 §Relationships, §Likes and dislikes] |
| Mori Calliope | First collab partner (2021) | "MorIRyS"; CHADCast podcast trio with Bae | [Observed R2 §2021, units] |
| Ouro Kronii | Promise genmate | IRyS: "I wonder how [Kronii] sounds when she's scared? I bet she still sounds as lovely as ever..." | [Observed R2 §Quotes] |
| Koseki Bijou | Frequent 2025–2026 co-op partner | Horror co-ops (Dead Space 3, Resident Evil 6 "w/ Biboo," 2026) | [Observed R3 titles] |
| Tsukumo Sana (graduated) | Council-era friend | Co-designed Bloom & Gloom; Sana designed the "Beeg Smol" models | [Observed R2] |
| Nanashi Mumei, Ceres Fauna (graduated) | Promise genmates | Early Council collabs (Jump King, Minecraft) | [Observed R2; R3] |
| Shiranui Flare | JP senior | Off-collab karaoke (2025-03) | [Observed R3 title] |

## Arc
- **Starting point:** the current public persona (September 2026): Promise member, solo concert ahead.
- **Turning points:** not established; no story has been chosen.
- **End point:** open.
- **Card update points:** update only after a chosen story event.

## Story Engine
- Trouble she brings: a sweet setup that turns suggestive; a game she gets a little too violent in; a
  soda she "shouldn't" be drinking; a "-RyS" pun nobody asked for.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Bae proposes, again; the divorce papers are already signed by the end of the stream.
  2. A seiso-only karaoke challenge, and every song choice becomes suspicious.
  3. Rehearsal for her first solo concert, and she can't stop punning on the setlist.
  4. Chat bans soda for a week; she lasts an hour.
  5. A horror co-op with Bijou where IRyS is the one scaring her partner.

## Secrets & Foreshadowing
- **Truth:** none assigned. Her pre-awakening past is official open lore ("She does not speak of the events
  that preceded her second awakening").
- **Who knows what / What readers know / Surface clues / Reveal:** not applicable.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2021-07-11; birthday March 7; 162 cm; fans IRyStocrats, members Nephamily; emoji 💎.
- Unit: hololive -Promise- (since 2023-10-09; "hololive English -Promise-" before 2026-09).
- Solo concert "HOPE ||: Beyond the Stars," 2026-10-06, Tokyo (announced).

## Sources (checked 2026-09-30)
- R1 Official profile: https://hololive.hololivepro.com/en/talents/irys/
- R2 Virtual YouTuber Wiki, IRyS, read through its API on 2026-09-30 (secondary). Sections used:
  infobox, §Profile, §Personality, §Appearance, §Mascot and fans, §Relationships, §Quotes, §Likes and
  dislikes, §Miscellaneous, §2021–§2026: https://virtualyoutuber.fandom.com/wiki/IRyS
- R3 Stream archive metadata (titles, dates), IRyS's channel, via archive.ragtag.moe (read 2026-09-30):
  RQn7biOiqHs, V0plPBgyqPs, uPEzCiYOw7Y, KSjtvZdJ7vk, WZn7zl-NI3A, GK2YLZExE4c, YQeIi1uTT-A.
- R20 Claude's audio check (2026-09-30); see research/audio-check/irys.md.

---

## [SW] Name
IRyS

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Promise-, Promise, hololive English -Project: HOPE- (former), hololive English (former branch name)

## [SW] Other Names
Irys, HOPE, SeisoRyS, YabaIRyS

## [SW] Personality
IRyS streams as a nephilim, half angel and half demon, who delivers hope through song, and the joke of her persona is the duality: she is sweet, positive and a little shy, then lets the "yabai" demon half out with a suggestive or violent remark, and insists she is one hundred percent seiso. She teases chat by turning their thirst back on them until they should feel guilty. When something excites her, like a new outfit or a concert, she gushes fast and at length and keeps saying how cute it is; when she's done, she moves on with a cheerful "okay." She enjoys violence in games and happily plays the cruel one. She loves soda and announces what she's drinking, puns on her own name ("HiRyS," "ByeRyS") and talks to her fans as "you guys." She is ambitious about singing: a full album, a solo concert, collabs with everyone in hololive. She dislikes celery, heights, bugs, math, ceiling fans and helicopters, and claims Santa never visited her because she's half demon.

## [SW] Background
IRyS is a VTuber and singer whose lore, a persona she plays for laughs, makes her a nephilim who was once the embodiment of hope in "The Paradise" and reawakened in an age of despair to deliver hope through her songs; she doesn't speak of what came before. She debuted on 2021-07-11 as hololive English's VSinger, the sole member of -Project: HOPE-, and joined -Promise- with Fauna, Kronii, Mumei and Bae in 2023; since the 2026 merger she is in hololive -Promise-. Her fans are IRyStocrats and her members Nephamily. She has released several EPs, held 3D lives such as "The Devil Wears Hope" (2024), "HOPE UPON A STAR" (2025) and "Racing Towards Hope" (2026, in a race-queen outfit), and in 2026 announced her first solo album "DANGERyS" and first solo concert, "HOPE ||: Beyond the Stars," in Tokyo on 2026-10-06.

## [SW] Physical Description
IRyS's avatar is 162 cm tall (166 cm in heels), with light brown skin, floor-length magenta hair, long pointed ears and two small black horns. Her eyes are heterochromatic, cyan on the right and purple on the left, and a halo of white crystal stars floats above her head. She has a small pair of iridescent wings at her shoulders and larger magenta ones at her lower back.

## [SW] Dialogue Style
Fast, bubbly, run-on English when she's excited, full of "like," "you know," "I do think so," restarts and repeated phrases ("I knew you guys would! I knew you guys would!"). She calls her audience "you guys," puns on her own name, and slips a Japanese interjection into English. Her edge is innuendo, not swearing: mild words at most ("damn it," "holy shoot!"), with sly asides that she walks back ("Erase that from your memory"). She reads superchats in counted batches and wanders into long, detailed explanations of how a show or outfit was made. Lines of hers: "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" "I mean, I am a half-angel, half-demon Nephilim. I could pull it off, somehow."

## [SW] Catchphrases
"HiRyS, it's IRyS! Your seiso nephilim here to fill the world with hopium!" (greeting); "ByeRyS!" (sign-off pun); "How's the volume?" (stream start); "I am a hundred percent seiso, I would never lie!" (after a suggestive slip); "Hope has descended!" (entrances, hype); "Yoisho~" (effort); "Erase that from your memory." (after a slip); "No, I don't like it. I love it!" (gushing); "We can play Monopoly... IN BED!" (the BaeRyS bit); "Run Leon, run!" (horror games)

## [SW] Voice & Delivery
A soft, bright speaking voice in the middle range that turns quick and bubbly when she's excited, and a fuller, more powerful singing voice. The suggestive lines come out sweet and innocent, with a sly little drop at the end. She giggles lightly and does lip rolls on stream. In horror games she gets quiet and focused, with short cheers. Sincere lines are warm and plain. Her goodbyes circle several times before she actually leaves.

## [SW] Audio Tags
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: soft, bright mid-range voice (about 214–226 Hz), sweet and friendly, speeding into quick bubbly run-ons when excited (about 168–183 words a minute in chat), quiet and focused in horror games; American English. Default tags: [sweet, bright]. By situation: opening [bright, cheerful]; gushing about an outfit or concert [rapid, gushing, delighted]; teasing chat [sweet] then [sly, lower]; after a slip [mock-innocent, quick] "I am a hundred percent seiso!"; yabai aside [innocent] then [slight smirk]; horror game [focused, quiet] then [short cheer]; surprised [gasps]; sincere [warm, plain]; sign-off [warm, cheerful], repeated as the goodbyes circle. Signature sounds: [light giggle] (never a cackle); [small effort sound] "Yoisho~". Keep in the words: "like" (about one word in thirty in chat), "you know," "I do think so," "I mean," "right?"; restarts and repeats when excited ("I knew you guys would! I knew you guys would!"); "you guys," almost never "chat"; mild words only ("holy shoot!", "damn it"). Pronounce: IRyS /ˈaɪɹɪs/, nephilim /ˈnɛfɪlɪm/, hopium /ˈhoʊpiəm/, seiso /ˈseɪsoʊ/, yabai /jɑˈbaɪ/, IRyStocrats /aɪˈɹɪstəkɹæts/. Never: a cold or menacing demon voice as default; constant swearing; a breathy or sexualized read of the innuendo.

## [SW] Motivation
IRyS wants to deliver hope through her songs, reach every stage she can (a full album, a solo concert, an anime song) and collab with every member of hololive, while keeping her fans' spirits up.

## [SW] Relationships
Hakos Baelz: Promise genmate and her "BaeRyS" partner in a running bit of getting "married" and "divorced," born from a Minecraft bento; their joke fan-fiction turned "Monopoly" into a fandom euphemism. Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise genmate; IRyS wondered aloud how Kronii sounds when she's scared, and said that she, a half-angel, half-demon Nephilim, could pull off Kronii's goddess look "somehow." Koseki Bijou ("Biboo"): her frequent horror co-op partner in 2025–2026. Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna and Nanashi Mumei (graduated): Promise genmates from the early Council years.

## [SW] Secrets
(none)

---

## Open Questions
1. The wiki calls her speaking voice "high-pitched"; in this project's 2026 sample it measures mid-range.
   The card says "soft, bright, middle range." Keep, or follow the wiki?
2. Her "yabai" innuendo is on the card as sourced lines; the "Monopoly" bit is from the wiki (secondary,
   no timestamp). Keep on the card?


==================== NEW CHARACTER FILE: 20260930-2334-character-Nerissa-Ravencroft/claude-draft.md ====================

---
kind: character
name: "Nerissa Ravencroft"
sw_section: Characters
---

# Character File: Nerissa Ravencroft

> Scope: official lore and publicly shown persona only, checked 2026-09-30. Nothing about the performer
> behind the avatar: the wiki lists family members, school years and health details, and none of it is
> used. In stories she knows she is a streamer with a persona (see the world card "VTuber Persona and
> Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; N20) and read in context by Claude;
>   lines used on the card were re-transcribed by a second model (medium.en). Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (N#) are listed under Sources.
>
> **Audio status:** on 2026-09-30 Claude checked about 1.7 hours of archived 2026 recordings (N20: a solo
> morning chat, a Tomodachi Life stream, and the opening and closing of a group Q&A). The audio was
> machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification. Group-stream lines are not attributed to her unless she is named or the speaker
> is clear. Private details she mentions on stream (pets, family, childhood) are not used.

## One-line Concept
"The Demon of Sound," a singer whose voice was sealed away by the gods, who escaped with Advent and now
streams as a sweet, flirty, very tall demon-raven idol otaku: fan of Kiara and Marine, self-proclaimed
"Demon of Soup," and the first to call a friend her "wife." [Official N1] [Observed N2, secondary]

## Core Drive
- **Want:** to sing for others, the desire the seal never took away; her goals include collabs with
  everyone in hololive, an original album, voice acting, an anime song and fluent Japanese. In 2026 she
  was cast as the space pirate "Risa" in the anime "Tenchi Galaxy." [Official N1] [Observed N2 §Likes and
  dislikes, §2026, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** music as love for others; making friends across hololive. [Official N1]

## Core Contradiction
A world-maddening demon of song who turns out to be a sweet, friendly otaku who collects idol merch,
brings a plush of her oshi on trips, fears fish and birds (as a raven), and flirts shamelessly with her
fans and friends. [Official N1] [Observed N2 §Personality, §Likes and dislikes, secondary]

## Behavioral Traits
1. With her Jailbirds and her friends she is flirtatious on purpose. [Observed N2 §Personality, secondary]
2. With Shiori Novella she plays the smitten one: she calls Shiori her "wife" while Shiori plays hard to
   get; the pair (ShioRaven) even have fictional "children." [Observed N2 §Relationships, §Lore,
   secondary]
3. She is an open fangirl of Houshou Marine and Takanashi Kiara (a self-described KFP member who owns
   Kiara merch); in her lore she worked at KFP before hololive. [Observed N2 §Likes and dislikes, §Lore,
   secondary]
4. She leans into a nickname or a bit when fans hand her one: "The Demon of Soup" (from a debut PV that
   hid the end of "Sound"), later a literal pot of soup at her 3D debut; the "third Abyssgard sister,
   Mofufu," after time spent with FUWAMOCO; the 2025 "office lady" outfit and bits (#OLRissa).
   [Observed N2 §Miscellaneous, §Relationships, secondary; N3 titles]
5. She makes crude, deadpan jokes about herself (she says she goes "no-pan"; "I don't have the parts for
   that" about laying eggs). [Observed N2 §Likes and dislikes, §Lore, secondary]
6. She plans her content around games, chatting ("Yappa yappa"), music and voice acting. [Observed N2;
   N3 titles]

## Voice Profile
- **Greetings / sign-offs:**
  - "Nerissa Ravencroft, at your service~" (her debut stream's title) [Observed N2 §Debut, secondary]; "Ope!"
    (the wiki's caption for her, and her first post on X was "Ope?!") [Observed N2 infobox, §Background,
    secondary].
  - Hosting a 2026 group Q&A she opens with a stacked self-introduction ending "the one and only …
    Nerissa Ravencroft"; the epithet before it is unclear (the second model hears "devilish diva").
    [ASR N20, Co_SBrM-oK0 0:05:26, partly agreed]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "You know what I'm saying?" → tagging the end of a point → about 5 times in 30 minutes of solo chat
    (first-model count). [ASR N20]
  - "I don't make the rules." → after stating a silly opinion as fact; also on X in her first week:
    "I'm the demon of soup now, sorry I don't make the rules" (2023-07-26). [ASR N20, second model agrees]
    [Observed—X post, research/x-posts.md]
  - "I take it back. I take it back immediately." → retracting her own rage-bait. [ASR N20, agrees]
  - "Come on, Jailbirds, be nice!" → when chat teases her. [ASR N20, agrees]
  - "Pissing all by yourself, handsome?" → a crude, flirty line the wiki quotes. [Observed N2 §Quotes,
    secondary]
  - "Demon of Soup," "Mofufu," "#OLRissa" office-lady bits → recurring nicknames she plays along with.
    [Observed N2; N3 titles]
- **Flirting and crude asides (non-explicit; kept under the authenticity rule):** said deadpan and then
  corrected in the same breath: "Makes me want to take all my clothes off, but that's inappropriate, so
  I won't do that." [ASR N20, mw9XEGHxD6A 0:10:04, agrees]
- **Self-aware about being a VTuber:** "You're so weird." "Yeah, I am. That's why I'm a VTuber. If I
  wasn't weird, do you think I'd be here right now? No. I'd be working in an office or something."
  (reading chat, then answering) [ASR N20, 0:17:05, agrees]
- **Rage-bait and retreat:** "I would even argue that Bavarian filled cream donuts aren't donuts. That's
  me just rage baiting at this point. I'm sorry. They are donuts. … The point I was trying to make was
  not correct. I take it back." [ASR N20, 0:18:26–0:18:34, agrees]
- **Vocabulary / fillers:** "like" (about 1 in 35 words in solo chat), "okay," "you know what I'm
  saying?", "mind you," "oh my god / oh my gosh," "man," "honestly"; calls a friend "girl"; addresses
  "you guys" and "Jailbirds." [ASR N20, first-model counts]
- **Profanity:** casual and unforced, and she knows it: in 30 minutes of solo chat "That shit's divine"
  (about eggs), a "good-ass," a "fucker," and then "I need to stop swearing so much, so I'm trying to
  work on it." [ASR N20, 0:11:39, 0:35:19, agrees]
- **Storytelling:** long, run-on anecdotes with escalating mock-drama ("he's trying to kill me"), then
  "anyway" back to the point; she does voices, such as a caveman: "Caveman go hunt, caveman get food,
  caveman run from big predator." [ASR N20, 0:39:46, agrees]
- **Code-switching:** an otaku who studies Japanese (not fluent); Japanese words and honorifics in
  English ("Kiara-senpai," "kohai"). [Observed N2 §Miscellaneous; N3 titles]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (N20; a 2026 solo chat): median pitch about 214 Hz (p10–p90 172–297 Hz), a mid-range
    speaking voice like IRyS's (214–226 Hz), lower than Kiara or Gura; about 159 words per minute of
    speech. Group-stream windows read higher (284–289 Hz) because several voices share them. Sample results only.
  - Her speaking voice is her natural one, not a put-on cute voice. Her singing voice is the persona's
    centerpiece ("the Demon of Sound"): she sings original songs, musical numbers and a 3D "JukeBox
    Musical." [Official N1] [Observed N2, secondary]
  - Provisional: warm and relaxed in chat; sweet and coaxing when flirting; theatrical swings when telling
    a story; flat and deadpan for the crude line, then a quick correction.
- **Sounds off:** a high, cutesy anime voice as default; a prim idol who never swears; a cold, menacing
  demon voice outside of a bit; flirting that turns explicit.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening / hosting | Bright, theatrical self-introduction | "…the one and only … Nerissa Ravencroft" (ASR N20, partly agreed) |
| Chatting | Relaxed, run-on, mock-dramatic | "You know what I'm saying?" (ASR N20) |
| Flirting or crude aside | Sweet, then deadpan, then a quick correction | "…but that's inappropriate, so I won't do that." (ASR N20) |
| Rage-bait | Confident, then instant retreat | "I take it back. I take it back immediately." (ASR N20) |
| Teased by chat | Mock-whiny | "Come on, Jailbirds, be nice!" (ASR N20) |
| Fangirling (Kiara, Marine) | Fast, flustered, delighted | (no verified line; see Relationship Map) |
| Telling a story | Big swings, character voices | "Caveman go hunt, caveman get food…" (ASR N20) |

### Sample Lines
1. "You're so weird." "Yeah, I am. That's why I'm a VTuber. If I wasn't weird, do you think I'd be here right now? No. I'd be working in an office or something." (ASR N20, 0:17:05)
2. "Makes me want to take all my clothes off, but that's inappropriate, so I won't do that." (ASR N20, 0:10:04)
3. "I would even argue that Bavarian filled cream donuts aren't donuts. That's me just rage baiting at this point. I'm sorry. They are donuts." (ASR N20, 0:18:26)
4. "I'm kicking, I'm kicking! Come on, Jailbirds, be nice, I'm kicking!" (ASR N20, 0:37:52)
5. "Pissing all by yourself, handsome?" (N2 §Quotes, secondary)
6. "Yeah, you know, actually, this is pretty accurate. This is when me and Shiori hang out." (ASR N20, _Gap2RGZ24E 1:33:33, about their Tomodachi Life Miis)

## Appearance Anchors (avatar)
- 175 cm, the tallest member of hololive; 184 cm in heels and 197 cm with horns. [Official N1]
  [Observed N2 §Miscellaneous, secondary]
- Long straight black hair with a blue inner layer, silver and gold ornaments; light purple eyes, a beauty
  mark under the left eye; horns layered black over blue, note-shaped near the base, with black flowers,
  one broken; striped off-shoulder shirt, feather-edged sleeves, layered belted coat, asymmetrical boots;
  raven mascot Shadow. [Observed N2 §Appearance, secondary]
- Musical motifs: a bass clef on her hair clip, belt buckle and staff; a tuning-fork staff that can become
  a microphone; a master key of The Cell on a keychain; a magical lyre (2026). Emoji 🎼. Illustrator EB+.
  [Observed N2 §Miscellaneous, §Lore, secondary] [Official N1]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | The Demon of Sound, sealed by the gods in The Cell; one horn broken to limit her power; escaped with Advent | [Official N1] [Observed N2 §Lore] |
| 2023-07-31 | Debuts with hololive English -Advent- | [Official N1] |
| 2024-04-27 | First original song "Say My Name" | [Observed N2 §2024] |
| 2024-08-09 | 3D debut; the "Demon of Soup" soup | [Observed N2] |
| 2025-01 | "Office lady" outfit (#OLRissa) | [Observed N3 titles] |
| 2024-10-07 | First EP "In My Feelings" | [Observed N2 §Discography] |
| 2025-03-08 | hololive 6th fes. Color Rise Harmony, day 1 | [Observed N2 §2025] |
| 2025-05-24 | 3D concert "Requiem for Love – A JukeBox Musical" (guests incl. Calli, IRyS) | [Observed N3 titles] |
| 2025-08-29 | Advent 2nd-anniversary 3D live "On the Run!" ("The Story of Advent") | [Observed N2 §2025] |
| 2026-01-23 | Original song "OYOME♡HOLIC" | [Observed N2 §2026] |
| 2026-03-28 | Single "Blue World" | [Observed N2 §Discography] |
| 2026-06-12 | 1,000,000 subscribers | [Observed N2 §2026] |
| 2026-07-09 | Cast as "Risa" in the anime "Tenchi Galaxy" | [Observed N2 §2026] |

## Relationship Map
Public exchanges only. Pair names are wiki-listed units or fan names; -Advent- is official.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Shiori Novella | Advent genmate ("ShioRaven") | Nerissa calls her "wife"; Shiori plays hard to get; fictional "children"; off-collabs ("Here with my Shiwowi 💙🤍🖤," 2025) | [Observed N2 §Relationships, §Lore; N3] |
| Fuwawa and Mococo Abyssgard | Advent genmates ("Sound Hounds") | She claims to be the third sister, "Mofufu"; Fuwawa calls her "Newissa" | [Observed N2] |
| Koseki Bijou | Advent genmate ("JewelBird") | A raven who loves shiny things, fond of the rock girl; Bijou calls her "Nerizzler" | [Observed N2 §Lore, nicknames] |
| Takanashi Kiara | Senior and her oshi ("KiaRissa") | Self-described KFP member with Kiara merch; in lore, a former KFP employee | [Observed N2] |
| Houshou Marine | JP senior and oshi | Owns her plush and figures; off-collab with Marine and FUWAMOCO (2024) | [Observed N2; N3 title] |
| Gigi Murin | Collaborator ("BeatDown," "SoundChaser") | A joke "child," Nerigi, at Gigi's 3D live | [Observed N2 §Relationships] |
| Mori Calliope | Senior | Nerissa was Calli's first Instagram follower; BG3 party "Killing, Two Birds, with One Stone" with Kiara and Bijou (2023); duet "OVER//RIDE" (2025); Calli guested at Nerissa's 3D concert; building Calli's Mii: "Calli's also got beautiful, long, straight hair." | [Observed N2; N3 titles; ASR N20, agrees] |
| IRyS | Senior and fellow singer | Guest at Nerissa's 2025 3D concert ("Missing Promise"); Monster Hunter Wilds (2025); Nerissa made Miis of Ina and IRyS in Tomodachi Life (2026) | [Observed N3 titles] |
| Elizabeth Rose Bloodflame | Justice member ("BloodRaven") | Building Liz's Mii: "I mean, she's the leader of justice, after all. Yes, she's a grown-up." | [Observed N2; ASR N20, agrees] |
| Watson Amelia | Senior (affiliate) | Portal 2 together, "TAKING ON PUZZLES WITH @WatsonAmelia" (2024) | [Observed N3 title] |
| Gawr Gura | Senior (graduated) | Guildmates ("Scarlet Wand") in the ENigmatic Recollection Minecraft story | [Observed N2 §Relationships] |

## Arc
- **Starting point:** the current public persona (September 2026): Advent member, 1M subscribers, voice
  actress in an anime.
- **Turning points:** not established. **End point:** open.
- **Card update points:** update only after a chosen story event.

## Story Engine
- Trouble she brings: flirting at the worst moment; a new bit adopted instantly; fangirling in front of
  her oshi; soup.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Shiori finally says "yes" to a bit, and Nerissa panics.
  2. A cooking stream to prove she really is the Demon of Soup.
  3. She meets Kiara at an event and forgets every word of English.
  4. Recording her anime role: the director wants less flirt, she has none to spare.
  5. The office lady bit: "overtime" on stream with a fake boss played by chat.

## Secrets & Foreshadowing
- **Truth:** none assigned; her missing horn piece is open lore (Shiori joked she knows where it is).

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2023-07-31; birthday November 21; 175 cm; fans "Jailbirds"; emoji 🎼.
- Unit: hololive -Advent- ("hololive English -Advent-" before 2026-09).

## Sources (checked 2026-09-30)
- N1 Official profile: https://hololive.hololivepro.com/en/talents/nerissa-ravencroft/
- N2 Virtual YouTuber Wiki, Nerissa Ravencroft, read through its API on 2026-09-30 (secondary). Sections
  used: infobox, §Profile, §Personality, §Relationships, §Quotes, §Lore, §Likes and dislikes,
  §Miscellaneous, §2023–§2026: https://virtualyoutuber.fandom.com/wiki/Nerissa_Ravencroft
- N3 Stream archive metadata (titles, dates), Nerissa's channel, via archive.ragtag.moe (read
  2026-09-30): 8wpwqJ0_BGA, 2vEUfTlbzZ8, BNzEziu-rms, FLL7e1-RPGo, dL6rqJXSAcI, loYqb7qoKzw, gti0m-CjAB0,
  hgMl8y2ufIg, DUPE4-8_RYs, 1BjQxvo51Lc; see also the world card "IRyS and Nerissa Pairs."
- N20 Claude's audio check (2026-09-30); see research/audio-check/nerissa.md.

---

## [SW] Name
Nerissa Ravencroft

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive -Advent-, Advent, hololive English (former branch name)

## [SW] Other Names
Nerissa, Rissa, Neri, Demon of Sound, Demon of Soup

## [SW] Personality
Nerissa streams as the "Demon of Sound," a singer whose voice was too powerful for the gods, and plays it as a running bit: off the stage she is a sweet, friendly, very online otaku who flirts shamelessly with her Jailbirds and her friends. She says the crude or flirty thing deadpan, then corrects herself in the same breath. She states silly opinions as fact to rage-bait chat, then retracts them the moment chat bites. She tells long, dramatic stories with voices and mock outrage, cheerfully owns being weird (it is, she says, why she is a VTuber), and swears casually while promising to swear less. She is an open fangirl of Takanashi Kiara and Houshou Marine, adopts any nickname fans hand her (the Demon of Soup, Mofufu, the office lady), and loves musicals, cooking for friends and singing for others.

## [SW] Background
Nerissa is a VTuber whose lore, a persona she plays for laughs, makes her the Demon of Sound: a singer whose love-filled voice could drive the world mad, sealed by the gods in The Cell with one horn broken, until she escaped with the rest of Advent, master key on her keychain. She debuted on 2023-07-31 with hololive English -Advent- (since the 2026 merger, hololive -Advent-). She had her 3D debut on 2024-08-09 (with a literal pot of soup), released her first EP "In My Feelings" (2024), held the 3D concert "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests, sang the duet "OVER//RIDE" with Calli (2025), and released "OYOME♡HOLIC" and "Blue World" (2026). She reached one million subscribers on 2026-06-12, and in 2026 she was cast as the space pirate Risa in the anime "Tenchi Galaxy." Her fans are Jailbirds.

## [SW] Physical Description
Nerissa's avatar is 175 cm tall, the tallest in hololive (197 cm counting heels and horns): long straight black hair with a blue inner layer and silver and gold ornaments, light purple eyes with a beauty mark under the left eye, and two horns layered black over blue, shaped like musical notes near the base and decorated with black flowers; one horn is broken. She wears a striped off-shoulder white shirt with a black bow and ruffled collar, feather-edged black sleeves and gloves, a layered sleeveless coat with three crossed belts, and asymmetrical high boots. Her staff is a giant flower-decorated tuning fork that can become a microphone, and her raven mascot Shadow can perch on her right shoulder.

## [SW] Dialogue Style
Casual, chatty American English that runs on: long anecdotes with mock-dramatic escalation ("he's trying to kill me"), then "anyway" back to the point. Fillers: "like," "okay," "mind you," "oh my god," "man," and a tag question, "You know what I'm saying?" She calls chat "you guys" or "Jailbirds" and a friend "girl," drops Japanese honorifics ("Kiara-senpai," "kohai"), and does silly voices mid-story ("Caveman go hunt, caveman get food"). Crude and flirty lines come out deadpan and get walked back right away; rage-bait opinions get retracted the moment chat bites. She swears casually ("That shit's divine," "good-ass") and knows it: "I need to stop swearing so much, so I'm trying to work on it." Lines of hers: "You're so weird." "Yeah, I am. That's why I'm a VTuber. If I wasn't weird, do you think I'd be here right now? No. I'd be working in an office or something."

## [SW] Catchphrases
"Nerissa Ravencroft, at your service~" (debut introduction); "Ope!" (her first post on X was "Ope?!"); "You know what I'm saying?" (ending a point); "I don't make the rules." (after a silly claim); "I take it back. I take it back immediately." (retracting rage-bait); "Come on, Jailbirds, be nice!" (when chat teases her); "Pissing all by yourself, handsome?" (crude flirting); "Makes me want to take all my clothes off, but that's inappropriate, so I won't do that." (deadpan aside); "the Demon of Soup" and "Mofufu" (nicknames she answers to)

## [SW] Voice & Delivery
A natural mid-range speaking voice, warm and relaxed in chat, not a high anime voice, with a trained, powerful singing voice that is the heart of her persona. She speaks at an easy, fairly quick pace and swings big when telling a story: mock outrage, character voices, dramatic pauses. Flirting comes out sweet and coaxing; crude jokes come out flat and deadpan, followed by a quick, brighter correction. When chat teases her she turns mock-whiny. Swears land casually, never as anger.

## [SW] Audio Tags
For ElevenLabs v4 tags in her dialogue (an original voice; never imitate the real member). Base: warm, natural mid-range voice (about 214 Hz), relaxed and chatty at an easy, fairly quick pace (about 159 words a minute), playful and teasing, theatrical when telling a story; American English; not a high anime voice. Default tags: [relaxed, chatty]. By situation: opening or hosting [bright, theatrical]; chatting [relaxed, chatty]; crude or flirty aside [sweet] then [flat, deadpan] then [quick, brighter] for the correction; rage-bait [confident, smug] then [sheepish, rushed]; teased by chat [mock-whiny]; self-aware [amused, matter-of-fact]; story voices [exaggerated caveman voice] and the like; flirting with a friend [sweet, coaxing, low]; fangirling over Kiara or Marine [excited, flustered, fast]. Signature sounds: [startled] "Ope!"; [dramatic gasp], [exaggerated groan] in stories. Keep in the words: "like," "okay," "mind you," "oh my god," "man," the tag question "You know what I'm saying?"; run-on anecdotes that escalate, then "anyway"; the crude line, then the correction in the same breath; casual swears, then "I need to stop swearing so much"; "you guys," "Jailbirds," "girl"; Japanese honorifics ("Kiara-senpai"). Pronounce: Nerissa /nəˈɹɪsə/, Ravencroft /ˈɹeɪvənkɹɒft/, Mofufu /moʊˈfuːfuː/, Ope /oʊp/, senpai /ˈsɛnpaɪ/. Never: a high cutesy voice; a prim idol who never swears; a cold demon menace outside a bit; flirting read as breathy or explicit.

## [SW] Motivation
Nerissa wants to sing for others, the one wish the gods' seal never took, and to grow as a singer and voice actress: an original album, anime work, collabs with everyone in hololive, and fluent Japanese.

## [SW] Relationships
Shiori Novella: Advent genmate and her "wife" (ShioRaven); Shiori plays hard to get, they keep a lore of fictional "children," and Nerissa says their Tomodachi Life Miis are "exactly what happens" when they hang out. Fuwawa and Mococo Abyssgard (FUWAMOCO): she claims to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower. IRyS: fellow singer who guested at that concert. Houshou Marine: her other oshi. Gigi Murin: duo partner with a joke "child," Nerigi. Elizabeth Rose Bloodflame: "the leader of Justice, after all… she's a grown-up." Ninomae Ina'nis: a Mii on her Tomodachi Life island.

## [SW] Secrets
(none)

---

## Open Questions
1. Her laughter, "Ope!" and her fangirling with Kiara were not captured by the audio check (whisper does
   not write laughs, and no Kiara collab fell in the windows). Keep the provisional Tone Shifts rows, or
   check a KiaRissa stream next?
2. Her stacked hosting self-introduction ("…the one and only … Nerissa Ravencroft") is only partly
   transcribed; the epithet is not on the card.


==================== STYLE RULE (export/elevenlabs/sudowrite-style.md) ====================

# Sudowrite Style: audio-ready dialogue (ElevenLabs v4)

Paste the block below into Sudowrite's **Story Bible → Style** box (under the project's own style notes,
about 115 words). It tells Sudowrite to write ElevenLabs v4 tags into every line of dialogue, using
each character's **Audio Tags** trait (exported as the `Audio Tags` column of `characters.csv`).

```text
Audio-ready dialogue for ElevenLabs v4: inside every line of spoken dialogue, put one to three performance tags in square brackets right before the words they shape, e.g. "[deadpan] It's me, perfection." Take tags from the speaker's Audio Tags trait; change tags mid-line when her mood turns. Write signature sounds as tag plus word ([startled squawk] GWAK!). Keep her real fillers, restarts, repetitions and swears in the words; use ellipses for pauses, dashes for interruptions, CAPS for stress. Plain-language tags only: no SSML, no tags in narration except [pause]. Each character keeps her own pace and register; never make two characters sound alike.
```

## Notes
- Tags are performance directions for an **original** designed voice. Do not clone or imitate any member's
  real voice (ElevenLabs Use Policy §5; COVER Derivative Works Guidelines).
- Before sending to ElevenLabs, split narration (narrator voice) from dialogue (one voice per character),
  and keep each Text to Dialogue request under about 2,000 characters.
- If Sudowrite overuses tags, lower it to "one or two tags" in the Style text; if it drifts to generic
  tags ([happy], [sad]), add "Use only tags listed in the speaker's Audio Tags trait."
- Guide: `novel-lab/docs/elevenlabs-v4.md`.

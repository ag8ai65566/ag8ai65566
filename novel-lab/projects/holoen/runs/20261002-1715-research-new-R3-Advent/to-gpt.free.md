# Task 10 — New material: hololive -Advent- (5 members)

You are GPT, the senior researcher and QA reviewer for novel-lab's holoen project. Use the project-required
GPT-6 model at xhigh with live web search. Work read-only and answer in English. This is one task in a sequential
queue; do not launch parallel GPT work. Never read projects/*/runs/. Do not modify files; return the complete
result in your final response. The factual baseline is 2026-09-30 (today is 2026-10-02).

## Binding rules

- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.
- Never propose (even when an official profile or wiki lists it): body measurements, drinking amounts, family,
  home or home region, pets, health, sleep or daily routine, trips, romance, audition history, breaks or their
  reasons, pre-debut history or the performer behind the persona. A Merge Record that says "private details
  deliberately excluded" means a topic was left out on purpose: do not re-propose it.
- No explicit sexual content, no lyrics, no long quotes. Spoken quotations are not accepted from you: list them
  as candidates for Claude's two-model audio check (video, timestamp, approximate words). Official written
  lines (profiles, post text, titles) may be quoted short with their source.
- No member rankings or comparisons. Partner tags and voice directions are proposed scene directions for
  original designed voices, never imitation; no pitch, F0 or speaking-rate targets.
- Evidence classes: OFFICIAL (hololive/COVER pages, official accounts), PRIMARY (the member's own stream title,
  description or post), ARCHIVE_METADATA, SECONDARY (wiki, fan sites; label it), ASR (Claude's audio reports).
  Fan transcription cannot establish exact spoken words.

## Goal

The author wants new, sourced material for these members' cards: what the cards lack that helps a writer put
each member in a scene and give her a playable voice. Priorities, in order: (1) corrections to wrong or outdated
claims; (2) her present-day manner and running bits from 2025–2026 streams (recency weighting; alumni and
affiliates: their last active period); (3) 2025–2026 milestones, songs, concerts, official lore updates;
(4) documented interactions with the other cast members (list below), above all pairs the relationship web
lacks; (5) recurring segments, catchphrases and in-jokes with their official or primary source. Skip trivia that
does not change how a scene plays.

The cast: Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Gawr Gura (graduated), Watson Amelia (affiliate),
IRyS, Ouro Kronii, Ceres Fauna (graduated), Nanashi Mumei (graduated), Hakos Baelz, Shiori Novella, Koseki Bijou,
Nerissa Ravencroft, Fuwawa and Mococo Abyssgard (FUWAMOCO), Elizabeth Rose Bloodflame, Gigi Murin, Cecilia
Immergreen, Raora Panthera, Hoshimachi Suisei, AZKi, Nakiri Ayame, Nekomata Okayu, Houshou Marine, Shirogane Noel,
Yukihana Lamy, Shishiro Botan, Kikirara Vivi, La+ Darknesss, Takane Lui, Hakui Koyori, Sakamata Chloe (affiliate
since 2025-01-26), Kazama Iroha. COVER unified its female branches as "hololive" on 2026-09-07.

## Method
1. Read the member's block below (exported fields plus the 2025–2026 history rows already on the card); open the
   full card only to check the dossier or the Merge Record's exclusions.
2. Search official sources first (hololive talent and music pages, hololivepro.com news, COVER press, official X
   accounts), then the member's own stream titles and descriptions, then secondary sources (label them).
3. Propose only what is new or corrects the card; at most about 8 proposals per member. Give exact English text
   that fits the card's voice; for [SW] fields note that Relationships is capped at 350 words (many cards are at
   the cap: propose a dossier row instead, or say which clause it should replace).

## Exact output format (these headings, in this order)

## Coverage
Members examined, sources opened, what you could not check.

## Proposals
| ID | Priority | Member | Target | Proposed text (exact) | Why it helps scenes or voice | Evidence URL + class + checked date | Event date |
|---|---|---|---|---|---|---|---|
IDs NEW-R3-NNN. Priority P1 (material: correction-adjacent, present-day manner, major 2025–2026
event), P2 (useful enrichment), P3 (optional). Target is `C/<stem> › <field>` for an exported field or
`D/<stem> › <section>` for the dossier. Escape table pipes; use <br> for newlines.

## Corrections
| ID | Member | Exact old text | Problem | Exact replacement | Evidence URL + class + checked date |
|---|---|---|---|---|---|
IDs FIX-R3-NNN. Copy the old text exactly. "None." if none.

## Cast ties found
| Pair | Interaction | Date | Evidence URL + class | Fills a one-way tie or an empty pair? |
|---|---|---|---|---|

## After the baseline (author decision)
Items dated 2026-10-01 or later, or announcements of future events, listed separately.

## Quotation candidates for Claude's audio check
| Member | Video URL | Timestamp | Approximate words | What it would show |
|---|---|---|---|---|

## Merge handoff
Dependencies, propagation to other cards, up to five questions for the author ("None" if none).

## Run budget
One task must finish inside one quota window (about 200k tokens); every tool call re-sends the conversation.
Batch local lookups (`rg -n -e A -e B files`), prefer official pages, and stop at about 20 tool calls.
Your working directory is a copy of the project taken when this run started (no `runs/`, no git). If the
budget runs short, stop and list what you could not check under Coverage; a complete answer with disclosed
limits beats a lost one.

## Current one-way ties (from research/qa/relationship-web.md)

## One-way ties (4)

- Kikirara Vivi names Ouro Kronii; Ouro Kronii's Relationships does not name Kikirara Vivi.
- Raora Panthera names IRyS; IRyS's Relationships does not name Raora Panthera.
- Shirogane Noel names Ouro Kronii; Ouro Kronii's Relationships does not name Shirogane Noel.
- Shishiro Botan names Takanashi Kiara; Takanashi Kiara's Relationships does not name Shishiro Botan.

## Members

### Shiori Novella (`Shiori-Novella`; promoted (bible))

**Name:** Shiori Novella
**Groups:** hololive -Advent-, hololive English -Advent- (former branch name), Advent, Last Writes
**Other Names:** Shiori, Shiorin, The Archiver, Shiori Novella, Shiori~n
**Personality:** Shiori streams as "The Archiver," a bookish fugitive with forbidden knowledge, and plays it with a cheerful, dorky, slightly unhinged energy: she calls herself "a whacky, sleepy eepy girl" with "ditzy what-is-she-talking-about energy." Cozy chats swerve into strange tangents (anatomy, parasites, cannibalism, childhood cartoons with adult subtexts) until chat reaches for the "bonk" emote. She teases the people she is close to, especially her genmates, plays hard to get when Nerissa calls her "wife," and guards lore secrets (where Nerissa's horn is) as a running joke. Under the edge she is sweet and supportive: she credits fan artists in her outros, has a soft spot for animals, and says plainly how much she appreciates her viewers. She is a hands-on creator who edits her own vlogs, writes community posts like a public diary, made an original motion comic, and runs odd review and "educational" streams. She loves mysteries, Sherlock Holmes, horror co-ops and whimsical-creepy art, though she would rather watch someone else play the truly scary games; when a jump scare lands, she screams.
**Background:** Shiori is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Archiver," driven by a thirst for knowledge, who turns favorite stories and memories into bookmarks; imprisoned in The Cell for forbidden knowledge found in a story (which, in the lore, turned half her hair grey), she planned and executed Advent's prison break. She debuted on 2023-07-30 (JST) with hololive English -Advent-, narrates the group's lore videos, and is jokingly called its leader. She made her 3D debut on 2024-08-02 (PDT), sang at the 2024 and 2025 English concerts, released her first original song "Monsters and Men" on 2026-02-15, was paired with Mori Calliope at the 2026 Serendipity concert, and began her original motion comic "Into The Void" in July 2026. Her fans are Novelites; her mascot is Yorick.
**Dialogue Style:** Fast, chatty English that stacks reactions and restarts mid-thought, full of "like," "actually," "kind of," "sort of," "genuinely" and "if that makes sense"; she talks to "guys," rarely "chat." She defends her lore with a straight face ("In my defense, guys, they trespassed"; "It was not my fault everyone got sacrificed, okay?"), thirsts at game characters as a goofy bit ("Is that a vampire?"), cheers creators on ("I'm so happy for you"), and admits she would rather watch someone else play the scary games. Exclamations: "whoa," "ooh," "oh my god," "oh heavens," "oh shoot," "oh fudge." Her profanity is situational and can include "fuck" ("what the hell," "it pisses me off"); once, moderating a troll, she snapped "Go fuck yourself" and added at once, "I'm so sorry. I shouldn't say that." She teases her genmates, keeps lore secrets as a joke, and calls viewers with Japanese honorifics now and then. Lines of hers: "I would love to watch someone else play this. I would be too scared to play this myself." "…really bad at remembering names." "That's dead, guys. I defeated my first chimera."
**Catchphrases:** "Shiori~n!" (greeting); "Shiori Novella here at your service!" (introduction); "In my defense…" (defending a lore bit); "For the record, I did not sacrifice anyone." (her running sacrifice joke); "Don't you think that's a wonderful story?" (her official line); "I would be too scared to play this myself." (scary games); "Whoa, wait, who is that hot thing?" (a handsome character); "I'm so happy for you." (cheering someone on); "Aw, it's okay! There, there!" (comforting); "Oh nyo..." (dismay); "Alright, bye guys! See you later!" (sign-off)
**Relationships:** Nerissa Ravencroft: Advent genmate and partner in the performed ShioRaven "wife" bit; Shiori plays hard to get. Their fictional daughter and the secret of Nerissa's horn piece belong to their shared character jokes. Koseki Bijou: genmate who calls her "our glorious leader" (Goth Rock; a "Gyatt Review"). FUWAMOCO: genmates who once mistook a Minecraft cow for her (Pen Pups). Mori Calliope: her 2026 Serendipity partner in Last Writes ("When My Devil Rises"), who admits she is "a little obsessed with her"; Shiori admires Calli's "work ethic and boundaries," and they bond over dark taste and absurd deep-dives. Takanashi Kiara: hosted Advent on HOLOTALK; an occult handcam off-collab ("#shiotori"). Ouro Kronii: they hosted "Rating Your Clocks" together (2025) and sang "MONSTER" with Ina and Gigi at the 2025 concert. IRyS: Monster Hunter Wilds and PEAK (2025). Ceres Fauna (graduated 2025): with Nerissa, "Lonely in Gorgeous" at the 2024 English concert. Nanashi Mumei (graduated 2025): B-movie watchalongs. Ninomae Ina'nis: a "Rate Your Fears" nightmare talk. Watson Amelia: a VRChat aquarium visit with "Ame Senpai." Gigi Murin, Cecilia Immergreen, Elizabeth Rose Bloodflame (-Justice-, Advent's in-story "guards"): GAGA with Bijou, Gigi and Cecilia; Gigi, Elizabeth ("NovelFlame") and Nerissa voice her non-canon motion comic "Into The Void." Raora Panthera: a 2024 outfit-design collab and Blood Typers with Kronii and Bijou (2025). Cecilia and Vestia Zeta: "Break It Down" at Serendipity. Vestia Zeta (ID): "GreyScaleX," an official duo unit with "Purrfect Pair" merchandise (2026). Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club." HOLOSTARS: Machina X Flayon ("Goth Pilot"), Jurard T Rexford and Regis Altare in co-op games. Gawr Gura (graduated): a fellow "Scarlet Wand" guildmate in ENigmatic Recollection, with Nerissa.

Dossier history rows dated 2025–2026 (already on the card):
| 2025-08-29 | Advent 2nd-anniversary 3D live "On the Run!" | [Observed SN2 §2025] |
| 2026-02-15 | First original song "Monsters and Men" | [Observed SN2 Discography] |
| 2026-07-03/04 | Serendipity concert, duo with Mori Calliope | [Official SN4] |
| 2026-07-30 | "Into The Void" motion comic begins | [Observed SN3] |

Full card: projects/holoen/bible/characters/Shiori-Novella.md (Merge Record lists deliberate exclusions).

### Koseki Bijou (`Koseki-Bijou`; promoted (bible))

**Name:** Koseki Bijou
**Groups:** hololive -Advent-, hololive English -Advent- (former branch name), Advent, Rocku Wawa
**Other Names:** Bijou, Biboo, Koseki, Beebs, Beejoe, Lil'Rock, Jewel of Emotions, Oobib
**Personality:** Bijou, "Biboo," streams as the Jewel of Emotions, a tiny crystal girl made of every human feeling, and plays it as a bubbly, friendly, easily excited gremlin: she speaks fluent Gen Alpha meme ("skibidi," "rizz," "gyatt," "67"), blurts jokes that get her affectionately teased, and "collects moms" by getting seniors to agree to mother her. She tackles difficult action games (FromSoft games, Hollow Knight) and sets additional challenges after clearing them; she generally stays collected, but also performs mock outrage. She deliberately replaces profanity with "beep," including when reading game text, says "dang it!" for frustration, and asks Pebbles to avoid profanity too. She treats hard work like a boss fight she runs at "over and over again," loves to share her gaming with others, and keeps her lore as running bits: an evil twin, Oobib; an "Ascended" emotionless form; a habit of saying she eats her fans, who respawn. Her streams open with a moai head until she calls "Kira kira, Koseki!" She sometimes gives a hard-G name a J sound as a running joke ("Jerudo") and is proud of her small size.
**Background:** Bijou is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Jewel of Emotions," a gem formed under immense pressure from every human emotion, beautiful and filthy alike, whose brilliance drove the greedy to fight over her until she was imprisoned in secret; good emotions make her shine brighter. She debuted on 2023-07-30 (JST) with hololive English -Advent-. She made her 3D debut on 2024-08-03 (PDT), released the original songs "Prism no Mahou" ("Prism Magic," 2024) and "ROCK IN!" (2025), starred with Ina and IRyS at hololive night at Dodger Stadium (2025), sang a solo and two group numbers at the 2025 English concert -All for One-, and was paired with Takanashi Kiara at the 2026 Serendipity concert. Her fans are Pebbles, her mascot is GEOW, and her emoji is the moai 🗿.
**Dialogue Style:** Bright, bubbly English with "okay," "yeah," and runs of "yes, yes, yes"; she talks to "everyone" and "Pebbles," gives them playful orders ("Make a heart!"), and repeats words for emphasis ("over here, over here"). She deliberately replaces profanity with "beep," even mid-sentence ("don't be super beeping early"), and frustration is "dang it!" She speaks Gen Alpha and gamer slang ("rage baited," "mogging," "67"), calls superchats "super rock rock," and laughs in quick "ha ha ha" bursts and "hehehe" giggles. In games she is calm and steady, with mock outrage ("Everyone's dumb!"), deadpan cover-ups ("You saw nothing. I saw nothing."), small brags and wordplay that collapses ("That made more sense in my head"). Mock-solemn lore lines come out straight ("…worthy sacrifice, I will remember you"; "No, I was eeping"). She sometimes turns a hard-G name into a J as a joke ("Jerudo"), refers to herself as "Biboo," and is learning Japanese. Lines of hers: "Welcome to my birthday world! We're gonna save the city!" "Well, yes, I am. We've established this." "Managing my resources like a pro."
**Catchphrases:** "Kira kira, Koseki!" (transformation command); "BIBOO BIBOO!" (greeting); "Moai Moai Kyun~!" (her debut line); "dang it!" (frustration); "beep" (in place of any swear); "Rock rock!" (her answer to "bau bau"); "super rock rock" (superchats); "TEEHEE~" (mischief); "Bweh." (deflated); "You saw nothing. I saw nothing." (covering something up); "…worthy sacrifice, I will remember you." (mock solemn); "I hope you'll feel my radiance!" (official line); ":D" (in writing)
**Relationships:** Shiori Novella: Advent's "glorious leader" in Bijou's affectionate bit (Goth Rock; a "Gyatt Review"; GAGA with Gigi and Cecilia). Nerissa Ravencroft: the raven drawn to her shine (JewelBird); Bijou named her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." FUWAMOCO: "Diamond Dogs" since an Overcooked 2 collab in their first weeks; her "Rock rock!" parodies their "bau bau." Kaela Kovalskia (ID): "Grindstone" (Kaela calls her "Beejoe"): Raft, Minecraft, Split Fiction, and with Raora "Graondstone." Mori Calliope: they played Bijou's Undertale mod starring Calli together (2023); "TombStone"; a 24-hour charity stream together (2025) and Warhammer painting (2026). Takanashi Kiara: her 2026 Serendipity partner ("Rocku Wawa"), who calls her a "hidden gem" and encouraged her through hard choreography for a song with Kiara and Ame; Bijou admires Kiara's "confidence," and they keep saying "67." IRyS: her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina, they headlined hololive night at Dodger Stadium (2025). Hakos Baelz: "BaeBi" (We Were Here, a 2024 sleepover marathon); with Bae, Calli and IRyS she sang "BLUE CLAPPER" at the 2024 English concert. Nanashi Mumei (graduated 2025): "Stone Age"; Mumei rated her a loss at arm wrestling because "she is a rock." Ninomae Ina'nis: "TakoRocky," Monster Hunter partner who designed their collab outfits. Watson Amelia: Overwatch and Apex (2023). Ceres Fauna (graduated 2025): her Hitman "coach." Ouro Kronii: Lethal Company and Yu-Gi-Oh. -Justice-: GAGA with Gigi and Cecilia; Graondstone with Raora; "I'm Your Treasure Box" with Cecilia and Raora at the 2025 concert; Cecilia's Walking Dead watchalongs and a 2025 Elden Ring stream Bijou joined partway; Raora's 2024 cooking off-collab, billed with Bijou as her assistant. Kureiji Ollie ("GraveStone"), Akai Haato ("Red Stone"), Regis Altare (HOLOSTARS): game partners. Ichijou Ririka (ReGLOSS): Smash Bros. with a loser's punishment and Monster Hunter. At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS. Kikirara Vivi: Bijou watched Vivi's FLOW GLOW debut with FUWAMOCO (2024). Hoshimachi Suisei: Bijou watched her Fortnite concert on stream (2026).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-06-29 | "THAT'S WILD?!" 24-hour charity stream with Calli (Wildlife Warriors Worldwide) | [Observed Calli archive J5u2aGUrNq8] |
| 2025-07-05 | hololive night at Dodger Stadium with Ina and IRyS: a stadium sing-along and the first VTuber stream from the stadium | [Official KB9] |
| 2025-08-23/24 | -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora | [Official KB5] |
| 2025-11-01 | Second original song "ROCK IN!" and a 3D live | [Observed KB2 §2025] |
| 2026-07-03/04 | Serendipity concert, duo with Takanashi Kiara ("Rocku Wawa") | [Official KB4] |

Full card: projects/holoen/bible/characters/Koseki-Bijou.md (Merge Record lists deliberate exclusions).

### Nerissa Ravencroft (`Nerissa-Ravencroft`; promoted (bible))

**Name:** Nerissa Ravencroft
**Groups:** hololive -Advent-, Advent, hololive English (former branch name), Bloodraven
**Other Names:** Nerissa, Rissa, Neri, Demon of Sound, Demon of Soup
**Personality:** Nerissa streams as the "Demon of Sound," a singer whose voice was too powerful for the gods, and plays it as a running bit: off the stage she is a sweet, friendly, very online otaku who flirts shamelessly with her Jailbirds and her friends. She often says the crude or flirty thing deadpan, sometimes correcting herself in the same breath. She will state a silly opinion as fact to rage-bait chat, then take it back once chat bites. She tells long, dramatic stories with voices and mock outrage, cheerfully owns being weird (it is, she says, why she is a VTuber), and swears casually while promising to swear less. She is an open fangirl of Takanashi Kiara and Houshou Marine, adopts any nickname fans hand her (the Demon of Soup, Mofufu, the office lady), and loves musicals and singing for audiences.
**Background:** She has no supernatural abilities; her lore is a performed persona. Nerissa is a VTuber whose lore, a persona she plays for laughs, makes her the Demon of Sound: a singer whose love-filled voice could drive the world mad, sealed by the gods in The Cell with one horn broken, until she escaped with the rest of Advent, master key on her keychain. She debuted on 2023-07-31 with hololive English -Advent- (since the 2026 merger, hololive -Advent-). She had her 3D debut on 2024-08-09 PDT (with a literal pot of soup), released her first EP "In My Feelings" (2024-08-08), held the 3D concert "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests, sang the duet "OVER//RIDE" with Calli (2025), and released "OYOME♡HOLIC" and "Blue World" (2026). She reached one million subscribers on 2026-06-12, and in 2026 she was cast as the space pirate Risa in the anime "Tenchi Galaxy." Her fans are Jailbirds.
**Dialogue Style:** Casual, chatty American English that runs on: long anecdotes with mock-dramatic escalation ("he's trying to kill me"), then "anyway" back to the point. Fillers: "like," "okay," "mind you," "oh my god," "man," and a tag question, "You know what I'm saying?" She calls chat "you guys" or "Jailbirds" and a friend "girl," drops Japanese honorifics ("Kiara-senpai," "kohai"), and does silly voices mid-story (a caveman voice). Crude and flirty lines often come out deadpan, sometimes walked back right away; a rage-bait opinion can get retracted once chat bites. In the sampled chat she swears as casual emphasis ("That shit's divine") and knows it: "I need to stop swearing so much." Lines of hers: "I'm sorry. They are donuts." "The point I was trying to make was not correct."
**Catchphrases:** "Hiya Darlings" (greeting, as she writes it in 2026); "Devilish Diva, the one and only Nerissa Ravencroft!" (self-introduction); "Nerissa Ravencroft, at your service~" (debut introduction); "Ope?!" (her first post on X); "You know what I'm saying?" (ending a point); "I don't make the rules." (after a silly claim, on stream and on X); "…take it back immediately" (retracting rage-bait); "Come on, Jailbirds, be nice!" (when chat teases her); "Makes me want to take all my clothes off, but that's inappropriate, so I won't do that." (deadpan aside); "the Demon of Soup" and "Mofufu" (nicknames she answers to)
**Relationships:** Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit (ShioRaven); Shiori plays hard to get, and the two keep a joke lore of fictional "children." Fuwawa and Mococo Abyssgard (FUWAMOCO; "Sound Hounds"): she claims, as a bit, to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, and they held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower. IRyS: fellow singer who guested at that concert. Elizabeth Rose Bloodflame: her "mortal enemy" in their lore (a performed rivalry) from Justice and her 2026 Serendipity unit partner in Bloodraven ("Cruel Angel's Thesis"); they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai"). Moona Hoshinova: she sings on Moona's "100%" (2025). Houshou Marine: one of her oshis (secondary); Mario Party Superstars with FUWAMOCO (2024). Gigi Murin: duo partner with a joke "child," Nerigi. Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025); with Kiara they sang "Beyond the way" at the 2024 English concert. Ceres Fauna (graduated 2025): "Fauna-senpai!!!" on her first day on X; with Shiori they sang "Lonely in Gorgeous" at the same concert. Cecilia Immergreen: Unravel Two (2024; "AutoTune," a secondary pair name). Raora Panthera: Clubhouse Games (2024); with Moona, Raft and Monster Hunter Wilds as "V3LVET" (2025). Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii at Serendipity. Gawr Gura (graduated): a "Scarlet Wand" guildmate in ENigmatic Recollection, with Shiori. La+ Darknesss: holoGTA (2024) and a dance short to her "Onee-sama♡Love Call" (2026); Takane Lui: a "Soar" dance short (2026). Ninomae Ina'nis: on her Tomodachi Life island with IRyS. Hoshimachi Suisei: a "BIBIDEBA" dance short (2024). Nakiri Ayame, Nanashi Mumei and Watson Amelia: the 2023 Sports Festival white team.

Dossier history rows dated 2025–2026 (already on the card):
| 2025-01 | "Office lady" outfit (#OLRissa) | [Observed N3 titles] |
| 2025-03-08 | hololive 6th fes. Color Rise Harmony, day 1 | [Observed N2 §2025] |
| 2025-05-24 | 3D concert "Requiem for Love – A JukeBox Musical" (guests incl. Calli, IRyS) | [Observed N3 titles] |
| 2025-08-29 | Advent 2nd-anniversary 3D live "On the Run!" ("The Story of Advent") | [Observed N2 §2025] |
| 2026-01-23 | Original song "OYOME♡HOLIC" | [Observed N2 §2026] |
| 2026-03-28 | Single "Blue World" | [Observed N2 §Discography] |
| 2026-06-12 | 1,000,000 subscribers | [Observed N2 §2026] |
| 2026-07-09 | Cast as "Risa" in the anime "Tenchi Galaxy" | [Observed N2 §2026] |

Full card: projects/holoen/bible/characters/Nerissa-Ravencroft.md (Merge Record lists deliberate exclusions).

### Fuwawa Abyssgard (`Fuwawa-Abyssgard`; promoted (bible))

**Name:** Fuwawa Abyssgard
**Groups:** FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent, B.F.F
**Other Names:** Fuwawa, Fuwa-chan, Fuwa-nee, The Fluffy One, Fluffy One
**Personality:** Fuwawa streams as "The Fluffy One," the older twin demonic guard dog whose duty is to calmly look after her little sister Mococo and their mascot Pero, a calm that never lasts. She is a sweet, gentle, bouncy airhead who says odd things with total confidence ("Refridgator!", math "stops" at zero), is poor at spelling and math, mixes up left and right, and is clumsy at games, all of which she wears happily because she is "exceptionally cute." She teases Mococo, sometimes too much, and plays an "evil twin" role in their public comedy; she also hosts solo streams, such as Hitman. The official profile calls her bouncy, boisterous and chatty. She loves visual novels, retro games, cute girls, Japanese sweets and her oshi Houshou Marine, sings and dances seriously, and her pep talks emphasize compassion, confidence and self-acceptance. Her mission, with Mococo, is to protect the Ruffians' smiles.
**Background:** Fuwawa is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Fluffy One," the older of two twin demonic guard dogs from the Northwest Passage in the demon world, sealed in The Cell "for being a pain in the godly behind," whose duty is to look after her little sister Mococo and Pero, their dog mascot. She debuted with Mococo as FUWAMOCO on 2023-07-31 in hololive English -Advent-, sharing one channel. Together they won "VTuber of the Year" at the 2024 VTuber Awards, reached one million subscribers first in Advent, made their 3D debut in August 2024, held a birthday concert in 2025, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album. Her color is blue.
**Dialogue Style:** Soft, sweet, chatty English that narrates what she is doing and asks everyone to agree ("…right?"), with plenty of "okay," "maybe," "you know" and strings of "no, no, no." She says odd things with total confidence ("Refridgator!"), punctuates everything with "bau bau," calls her sister "Moco-chan" even in English, and talks to her "Ruffians" (sometimes "Wuffians": she can turn an R into a W). She is politely sneaky ("Hello, ma'am. Nice day, ma'am."), pleads cutely for food ("Can I have one? I like one."), teases a little too hard as the "evil twin," and gives warm pep talks ("be the main character of the gym") while leaving the official Pup Talks to Mococo. She does not swear and dislikes dirty jokes. With Mococo she finishes sentences in sync. Her pep talks emphasize compassion, confidence and self-acceptance. Lines of hers: "Should I run? Is running suspicious?" "I'm blending in right now, right?"
**Catchphrases:** "Bau bau!" (everything); "I'm not a chihuahua, I'm Fuwawa!" (introduction); "Hello hello bau bau!" (the twins' opening); "Moco-chan" (her sister, always); "Ruffians" (her fans); "Oh my gosh!"; "Refridgator!" (her own word); "Zero is where the math stops." (on math); "How about we get you all nice and fluffy~?" (official line); "No support is small."; "protect your smile" (the twins' mission)
**Relationships:** Mococo Abyssgard: her younger twin, whom she calls "Moco-chan" even in English; Mococo says Fuwawa is dependable and calms her down; they finish each other's sentences ("FUWAMOCO sync") and sometimes argue; Fuwawa loved being called "Fuwa-nee" once. Pero, "The Great Perroccino": their fictional dog mascot and self-proclaimed mentor; they call him "nasty" in their public bits. Advent: Shiori (Pen Pups; they mistook a cow for her), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Fuwawa calls her "Newissa," and Nerissa claims to be the third sister, "Mofufu"). Mori Calliope: "FUWAMOCALLI," a collaboration name the twins say they particularly like. Watson Amelia: "Detective Dogs." Ouro Kronii: "WatchDog." Nanashi Mumei (graduated 2025): "Fuwamoomco" (Overwatch). Raora Panthera: their 2026 Serendipity unit partner in B.F.F, who drew them a shikishi before her debut. Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026). Houshou Marine: her oshi (secondary); a Touhou off-collab (2024). Shirakami Fubuki and Hakui Koyori ("FUWAMOKOYO"): horror and Lethal Company partners. Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity. Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA." Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity. Hakos Baelz: Gigi's 2025 Spring Party; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES" (2026). IRyS, Gigi and Kronii: "Bright Tonight" (2025). Ceres Fauna (graduated): FUWAMOCO helped on the World Tree's last day (2024-12-31). AZKi: a FUWAMOCO-themed GeoGuessr collaboration ("FWMCAZ"); secondary records also document a singing stream with Minato Aqua and the twins' guest appearance at her 2025 birthday live. Nekomata Okayu: secondary accounts report her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; archived metadata documents the twins' 2025 watch-along of her concert. Takane Lui: "TWIN DAY WITH LUI" (2023). Kazama Iroha: a cookie-quiz off-collab (2024). Shirogane Noel: a team Mario Kart event (2023). Kikirara Vivi: #holoREPO (2025). Hoshimachi Suisei: Puyo Puyo coaching (2026). Nakiri Ayame: the 7th fes. stage (2026).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-02-02 | First birthday 3D concert, with Advent and JP guests | [Observed FW3 ouQF2A1l_cI] |
| 2025-08-23/24 | -All for One-: "HOT DUCK!", "Howling," "Lifetime Showtime," "SHALLYS" | [Official FW5] |
| 2026-04 | "Mekurumeku Rendezvous," a TV anime ending theme | [Observed FW3 vSwxof0K8lk] |
| 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Mococo and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) | [Official FW4; Serendipity report] |
| 2026-08-29 | First album "FUWAMOCO à la mode" announced | [Observed FW2 §2026; X via wiki] |

Full card: projects/holoen/bible/characters/Fuwawa-Abyssgard.md (Merge Record lists deliberate exclusions).

### Mococo Abyssgard (`Mococo-Abyssgard`; promoted (bible))

**Name:** Mococo Abyssgard
**Groups:** FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent, B.F.F
**Other Names:** Mococo, Moco-chan, Mogogo, Mogojyan, The Fuzzy One
**Personality:** Mococo streams as "The Fuzzy One," the younger twin demonic guard dog who spent her prison time on anime and games and joined the escape "just for the heck of it." On stream she is energetic, optimistic and especially friendly, the twin who raises everyone's spirits with "Mococo Pup Talks" ("Not tomorrow! Today!"), and insists on her real nicknames (Moco-chan, Mogogo, Mogojyan). She brings energetic reactions and earnest Pup Talks to the duo, keeps recurring show segments moving ("hashtag hashtag FWMCMORNING"), and sometimes argues with Fuwawa. Most of her streams are shared with her sister, though she has also streamed solo. She gets overexcited, can be stubborn, and has a big heart. She sneezes on stream so often that fans keep count. She loves underground idols, denpa songs, visual novels, roguelikes and her oshi Omaru Polka, dislikes scary things yet plays horror games with her sister, and wants every Ruffian to keep going "one step forward a day."
**Background:** Mococo is a hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Fuzzy One," the younger of two twin demonic guard dogs from the demon world, sealed in The Cell "for being a pain in the godly behind," who spent her prison time watching anime and playing games and joined the escape "just for the heck of it," barking at the guards and throwing Pero, the twins' dog mascot, at them. She debuted with her older twin Fuwawa as FUWAMOCO on 2023-07-31 in hololive English -Advent-, sharing one channel and the morning show FUWAMOCO MORNING. Together they won "VTuber of the Year" at the 2024 VTuber Awards, made their 3D debut in August 2024, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album. Her color is pink.
**Dialogue Style:** Bright, quick, earnest English with "bau bau" everywhere, short exclamations ("Whæt?", "Haeh?", "This is good!") and, now and then, a drawn-out vowel at the end of a word (fans spell it "Noæ!"). She gives Pup Talks that build step by step to a cheer ("Not tomorrow! Today!"; "That means you're unstoppable!"), keeps the show running ("hashtag hashtag FWMCMORNING"), and insists on her real nicknames, Moco-chan, Mogogo and Mogojyan. She refers to herself by name ("What about Mococo?"; "I'm not silly. I'm Mococo!"), gets overexcited, and sneezes mid-sentence. She calls her sister "Fuwawa," mixes in Japanese words she loves, and does not swear. With Fuwawa she finishes sentences in sync and argues a little. Her Pup Talks turn small daily efforts into an encouraging picture of cumulative progress. Lines of hers: "I'm the danger!" "If I die, I die."
**Catchphrases:** "Bau bau!" (everything); "I'm not Fuwawa, I'm Mococo!" (introduction); "Hello hello bau bau!" (the twins' opening); "Ehehe, it's play time, whether you're ready or not!" (official line); "Not tomorrow! Today!" (Pup Talk); "That means you're unstoppable!" (Pup Talk); "Whæt?" (surprise); "Noæ!" (after a sneeze); "What about Mococo?"; "I'm the danger!"; "hashtag hashtag FWMCMORNING" (the show); "Moco-chan, Mogogo, Mogojyan" (her only nicknames)
**Relationships:** Fuwawa Abyssgard: her older twin, who calls her "Moco-chan"; Mococo has called her dependable, calls her plain "Fuwawa" (she refused to repeat "Fuwa-nee"), and is embarrassed by their "FUWAMOCO sync." Pero: the twins' fictional dog mascot; in the prison-break lore, Mococo throws Pero at the guards. Advent: Shiori (Pen Pups), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Nerissa's "Mofufu" bit). Omaru Polka: her oshi (Phasmophobia with Fubuki and Polka; a guest at their birthday concert). Gigi Murin ("GigiMoco," "bauBau") and Cecilia Immergreen ("Cecemoco"): Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Cecilia is also Mococo's Chrono Trigger partner, including 2026 off-collabs; Gigi sang "Bright Tonight" and "MAKE IT, BREAK IT" with the twins. Raora Panthera: their 2026 Serendipity unit partner in B.F.F. Ouro Kronii: "WatchDog." Mori Calliope: "FUWAMOCALLI." Watson Amelia: "Detective Dogs." Nanashi Mumei (graduated 2025): "Fuwamoomco." Hakui Koyori: a FUWAMOCO MORNING guest host ("FUWAMOKOYO"). Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA." Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity. Hakos Baelz: Gigi's 2025 Spring Party with FUWAMOCO and Bae; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES" (2026). IRyS, Gigi and Kronii: "Bright Tonight" (2025). Ceres Fauna (graduated): FUWAMOCO helped on the World Tree's last day (2024-12-31). AZKi: a FUWAMOCO-themed GeoGuessr collaboration ("FWMCAZ"); secondary records also document a singing stream with Minato Aqua and the twins' guest appearance at her 2025 birthday live. Nekomata Okayu: secondary accounts report her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; archived metadata documents the twins' 2025 watch-along of her concert. Houshou Marine: archived metadata records a Touhou off-collab and Mario Party with Nerissa (2024). Takane Lui: "TWIN DAY WITH LUI" (2023). Kazama Iroha: a cookie-quiz off-collab (2024). Kikirara Vivi: #holoREPO (2025). Shirogane Noel: a team Mario Kart event (2023). Hoshimachi Suisei: a "Chatter Chatter" dance short and Puyo Puyo Tetris 2 coaching (2026). Nakiri Ayame: the 7th fes. stage with Okayu and Ina (2026).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-01-29 | 500th on-stream sneeze, celebrated on X | [Observed MC6] |
| 2025-08-23/24 | -All for One- with Fuwawa | [Official MC5] |
| 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Fuwawa and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) | [Official MC4; Serendipity report] |

Full card: projects/holoen/bible/characters/Mococo-Abyssgard.md (Merge Record lists deliberate exclusions).

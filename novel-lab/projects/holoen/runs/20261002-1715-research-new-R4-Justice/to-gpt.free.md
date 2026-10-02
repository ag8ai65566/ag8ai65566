# Task 10 — New material: hololive -Justice- (4 members)

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
IDs NEW-R4-NNN. Priority P1 (material: correction-adjacent, present-day manner, major 2025–2026
event), P2 (useful enrichment), P3 (optional). Target is `C/<stem> › <field>` for an exported field or
`D/<stem> › <section>` for the dossier. Escape table pipes; use <br> for newlines.

## Corrections
| ID | Member | Exact old text | Problem | Exact replacement | Evidence URL + class + checked date |
|---|---|---|---|---|---|
IDs FIX-R4-NNN. Copy the old text exactly. "None." if none.

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

### Elizabeth Rose Bloodflame (`Elizabeth-Rose-Bloodflame`; promoted (bible))

**Name:** Elizabeth Rose Bloodflame
**Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, Bloodraven
**Other Names:** Elizabeth, Liz, ERB, Lizzie, Erby Berby, Lady Bloodflame, The Scarlet Queen
**Personality:** Elizabeth streams as "The Scarlet Queen," Harbinger of Order and organizer of Justice, and plays the queen with theatrical flair ("Oh~hohoho!", royal decrees, "Huzzah!"); off the bit she is warm and polite, and Nerissa praises her kindness and the encouragement she gives nervous collaborators ("She's always looking out for me, even though I'm the senpai"). Her official profile calls her self-disciplined, a bit too hard on herself and soft on those around her. Secondary accounts describe a quiet confidence and a gift for voice mimicry that she uses for pranks on hololive and HOLOSTARS seniors. Singing is her heart ("Let my voice be your strength"): karaoke from her first days, covers and duets across branches, and her own arrangements and choreography for her 3D showcase. Her streams use minced oaths rather than swearing; she loves penguins and mint chocolate and admires her seniors, Kureiji Ollie above all.
**Background:** Elizabeth is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Scarlet Queen" and organizer of Justice; secondary-reported lore adds that she is the Harbinger of Order, a human knight from Great Exardia (not actually royalty) whose sword is Thorn, who joined hololive to keep an eye on Advent and to become an idol. She debuted first of her generation on 2024-06-21 (PDT) in hololive English -Justice-, held her 3D showcase on 2025-08-01 (PDT), sang at the 2025 English concert ("ALiCE&u" with Nerissa and Ayunda Risu, a solo "Stellar Stellar," and the day-two opener "START AGAIN" with Calli, IRyS and Nerissa), invited guests from several branches to her 2026 birthday live, and at the 2026 Serendipity concert sang "HELP!!" with Kobo Kanaeru and Hakos Baelz and formed the unit Bloodraven with Nerissa Ravencroft ("Cruel Angel's Thesis"). Her representative color is red; her fans are the Rosarians of the Bloodflame Kingdom.
**Dialogue Style:** Warm, polite English with a British accent and British slang ("Ello," "Soz," "bits and bobs," "for funsies," "willy-nilly," "whilst," "gosh," "cheeky," "Fancies!"), full of "like," "okay" and "lovely," and warm reactions to anything cute. She opens and closes like a TV host ("Lovely to see you, to see you LOVELY!"; "Please do not swear"; "…let my voice be your strength!" and, a moment later, "Huzzah!"), and slips into queenly theatre for bits ("Oh~hohoho!", "By royal decree…" in her posts). Her sampled streams use minced oaths ("What the frick?"; the wiki adds "What the Frigg!" and "Oh, you mothertrucker…"). She talks about singing with real feeling ("singing is good for the soul"; "a very Liz song"), jokes about her flame dancers' work ethic, voices game characters and does impressions. Most of the time she simply chats warmly; save the royal flourish for bits.
**Catchphrases:** "Ello!" (greeting); "Lovely to see you, to see you LOVELY!" (her catchphrase); "Let my voice be your strength." (official line, sign-off); "Huzzah!" (celebration, sign-off); "Oh~hohoho!" (queenly laugh); "Roses are red, the fire of my heart is blue…" (the start of her introduction); "By royal decree, my sweet Rosarians…" (in posts); "Please do not swear." (her "ERBTV" bit); "What the frick?" (a minced oath); "Soz"; "bits and bobs"; "for funsies"; "a very Liz song"; "Rosarians" (her fans)
**Relationships:** Nerissa Ravencroft: her lore "mortal enemy" from Advent and her Serendipity 2026 unit partner in Bloodraven ("Cruel Angel's Thesis"); they covered "Rondo Revolution" and shared the 2025 stages "ALiCE&u" (with Ayunda Risu) and "START AGAIN" (with Calli and IRyS); Elizabeth says Nerissa "has a beautiful voice," Nerissa praises her kindness, and Nerissa calls her "my husband" as a performed bit. Vestia Zeta (ID): her duet partner for "Giri Giri" at her 2025 3D showcase, which Elizabeth arranged and choreographed. Gigi Murin: her Operation Tango partner (Gigi titled her stream "i won't let Liz down!!!"). Cecilia Immergreen: introduced her to Minecraft; Cecilia's lore joke says an older Justice made her a maid ("#LizIsInnocent"). Raora Panthera: an early duo partner ("Chat & Art w/ Liz!"), whom she calls "Pretty Kitty." Kobo Kanaeru and Hakos Baelz: "HELP!!" at Serendipity. Kureiji Ollie (ID): her kami-oshi and "Code Red" partner (PEAK with HOLOSTARS' Machina X Flayon and Jurard T Rexford; "High Tide" on stage with Kronii); Crimzon Ruze (HOLOSTARS) is her "Nephew" in a Marvel Rivals uncle–nephew bit. Banzoin Hakka (HOLOSTARS): a "Mephisto" duet she produced and arranged. Mori Calliope: the LYRA cover of "III" with Amane Kanata, Koganei Niko and Ayunda Risu. Shiori Novella: credited in Shiori's non-canon motion comic "Into The Void." Takanashi Kiara: calls her "Erby Berby." 2026 birthday-live guests (secondary set list) included FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine, Korone and Nerissa. Shirogane Noel and Kikirara Vivi: Mumei's Gartic Phone EN + ID + JP collab (2025). AZKi: fellow member of Tokoyami Towa's 2025 New Year Game Festival team, with Kronii (secondary roster).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-01-18 | "Mephisto" cover with HOLOSTARS' Banzoin Hakka | [Observed EB3] |
| 2025-08-01 PDT | 3D showcase (5 PM PDT); she arranged and directed most of it, including "Giri Giri" with Vestia Zeta | [Official EB7] [ASR EB20] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official EB7] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie | [Official EB5] |
| 2026-05 | 2026 birthday live with guests from several branches; the performances were released as cover videos ("Live from COVER Corp. Studio") | [Observed EB3, archived credits] |
| 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |

Full card: projects/holoen/bible/characters/Elizabeth-Rose-Bloodflame.md (Merge Record lists deliberate exclusions).

### Gigi Murin (`Gigi-Murin`; promoted (bible))

**Name:** Gigi Murin
**Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, Autofister, CCGG
**Other Names:** Gigi, Gi Murin, G Pain, GeeGee, Da Fister, The Free-spirited Chaser
**Personality:** Gigi streams as "The Free-spirited Chaser," a gremlin who follows her instincts toward whatever is fun and makes trouble because it seemed funny (her official line: "Huh? But it was funny! Don't get mad at me!"). She is loud, energetic, unpredictable and hard to embarrass, and won the 2024 Most Chaotic VTuber award. She keeps bits going until they land, plays to win, and has run a years-long campaign to get Mori Calliope to play League of Legends. She teases hard and makes crude jokes as jokes, and admits she talks about "absolutely nothing for 20 minutes" before touching the game. She loves MMORPGs, Final Fantasy XIV, rhythm games and story games, and draws grems. Under the noise there is a plain, dutiful side: she thanks fans for coming, reminds them to "stay safe, stay hydrated, and always be aware of your surroundings," and performs original songs, sentimental ones included. Cecilia, her Autofister partner, says she "doesn't easily get rattled and is very dependable."
**Background:** Gigi is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Free-spirited Chaser," a mischievous gremlin "born and raised under the flag of Freedom" who chases targets on instinct and struggles with memorizing directions; secondary-reported lore places her in Freesia and frames the pursuit of Advent as another chance for fun. She debuted on 2024-06-21 (PDT) in hololive English -Justice-, won the 2024 Most Chaotic VTuber award, held her 3D showcase on 2025-08-02 (PDT), and sang at the 2025 English concert (solo "Wonky Monkey," "Countach" with Hakos Baelz and Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, "III" with Nerissa). She performs original songs: "I'll still be here" (presented on her 2025 birthday), "Bright Tonight" with IRyS, Kronii and FUWAMOCO (2025), and "enough" (2026). She and Cecilia Immergreen perform together as Autofister, also called CCGG: in 2026 they released "CCGG MADNESS" (Gigi helped with the lyrics and designed the chibi models) and sang it at the Serendipity concert, where Gigi also sang "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO. Her representative color is orange; her fans are grems; her fictional mascot is Popo, a kakapo.
**Dialogue Style:** Loud, fast, run-on American English full of "like," "okay," "yeah," "sure," "hold on" and bursts of laughter; she talks to "grems," reads superchats with quick deadpan comebacks ("I require context."; "I'm sure that's true."; "If it works 51% of the time, that's enough."), and turns anything into a bit: a blurred photo becomes a crime scene, bad luck an "Etsy witch" hex. The wiki records recurring bits: an escalating childish plea ("PPEEWEASEEEEE"), "Boat goes binted," "DON'T TELL LIZ!" and an emphatic "MORI CALLIOPE!" She swears casually now and then and makes crude jokes as jokes, then says something sweet and plain ("Thanks for coming to see me! … stay hydrated"). Most of the time she simply chats, fast and animated; save the shouting for a specific bit. Style demo: "Hold on, hold on. Who did this? Was it me? It was funny though."
**Catchphrases:** "Gi Murin!" (greeting); "Huh? But it was funny! Don't get mad at me!" (official line); "I require context." (a confusing superchat); "I'm sure that's true."; "If it works 51% of the time, that's enough." (a superchat reply); "I need validation."; "Boat goes binted!" (a meme she repeats); "MORI CALLIOPE!" (an emphatic callout); "DON'T TELL LIZ!"; "What do you meaaaaaan?"; "Why?! WHY, WHY, WHY?!" (losing); "yippee!"; "Ouchi!"; "I'll be back tomorrow. You'll see me again." (a sign-off); "grems" (her fans, lowercase)
**Relationships:** Cecilia Immergreen: her genmate and Autofister partner (also called CCGG): "CCGG MADNESS" (Gigi helped with the lyrics and designed the chibi models), Cuphead, Shadowverse and Serendipity; Cecilia calls her "idiot" (and "FREAK" in wiki transcriptions) yet says she "doesn't easily get rattled and is very dependable"; Gigi says Cecilia is "good at getting stuff done"; they met before debut. Raora Panthera: MapleStory, Monster Hunter and a food tier list; Raora designed both their Monster Hunter Wilds collaboration outfits. Elizabeth Rose Bloodflame: her Operation Tango partner (Gigi's stream title: "i won't let Liz down!!!"). Mori Calliope: Mouthwashing, Fast Food Simulator, R.E.P.O. and The Boba Teashop; the League of Legends campaign; with Fuwawa, "2 Creatures + 1 Reaper" (Fuwawa's post). Ouro Kronii: Fatal Fury and Hytale; "MONSTER" with Kronii, Ina and Shiori. IRyS, Kronii and FUWAMOCO: "Bright Tonight." Vestia Zeta (ID) and FUWAMOCO: "MAKE IT, BREAK IT" at Serendipity. Hakos Baelz: "Countach" with Kureiji Ollie (ID) on stage (2025), a dramatic reading of A Midsummer Night's Dream on Bae's stream, and Gigi's 2025 Spring Party with FUWAMOCO and Bae. Takanashi Kiara: Reanimal ("ULTRA ORANGE WILL LIGHT THE WAY!!") and Eden Eternal with Shiori; Kiara calls her "GeeGee." Watson Amelia: knights in a fictional ENReco marriage storyline. Shiori Novella and Koseki Bijou: GAGA with Cecilia (Trine 5, Heave Ho, Phasmophobia); Shiori is also in the Fanfic Club with Gigi, Pavolia Reine and Airani Iofifteen, and cast her in the non-canon motion comic "Into The Void." Nerissa Ravencroft: "III" on stage; she helped with the "CCGG MADNESS" lyrics. FUWAMOCO: Gigi and Cecilia guest-hosted FUWAMOCO MORNING #167 as a prank. Ceres Fauna: Silent Hill 2 and The Coughing Baby Award Show. Nanashi Mumei: Echo Point Nova. Nekomata Okayu: public translation-based banter during the 2026 New Year Game Festival, per secondary clip metadata.

Dossier history rows dated 2025–2026 (already on the card):
| 2025-08-02 PDT | 3D showcase (5 PM PDT; Aug 3 00:00 UTC) | [Official GG8] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official GG8] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa | [Official GG5] |
| 2025-10-18 | First original song "I'll still be here" presented (digital release 10-20) | [Official GG7] [Observed GG2] |
| 2025-12-22 | "Bright Tonight" with IRyS, Kronii and FUWAMOCO released | [Official GG7] |
| 2026-05 | CCGG 3D live with Cecilia; "CCGG MADNESS" MV (05-17; digital 05-29) | [Official GG1, GG7] [Observed GG3] |
| 2026-06-25 | Original MV "enough" | [Observed GG3] |
| 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice and "CCGG MADNESS" as Autofister with Cecilia (day 1); "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official GG4, GG9] |

Full card: projects/holoen/bible/characters/Gigi-Murin.md (Merge Record lists deliberate exclusions).

### Cecilia Immergreen (`Cecilia-Immergreen`; promoted (bible))

**Name:** Cecilia Immergreen
**Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, Autofister, CCGG
**Other Names:** Cecilia, Ceci, Cece, Immerhater, The Ancient Automaton
**Personality:** Cecilia streams as "The Ancient Automaton," a clockwork maid built for eternal servitude who now does the bare minimum and pours herself into hobbies. She is intelligent, straightforward and sarcastic, stubborn and combative in fun, and likes to trick collab partners, all in good fun. Her running bit is hating things out loud (chores, coffee, cleaning, Tuesdays, "when people say 'I guess'"), earning the name "Immerhater," yet she works hard behind the jokes: she builds stream gimmicks she calls "Immersions," does her own Live2D rigging, plays violin and composed her first original song. She has "the pure curiosity of a young girl" for anything new, gets giddy and loud when happy ("Spin to win!"), and swings from dry sarcasm to smug boasting to theatrical villainy. With Gigi, her Autofister partner, the teasing runs both ways: she calls Gigi "idiot" and "FREAK" and still calls her dependable. Bad driving in games is a running gag.
**Background:** Cecilia is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Ancient Automaton," a clockwork maid built long ago for eternal servitude who now does the bare minimum, cooks mostly potatoes and pours herself into crafty hobbies; secondary-reported lore places her origin in Immerheim, and in a public joke she blamed her maid duties on an earlier Justice. She debuted on 2024-06-22 (PDT) in hololive English -Justice- with a chat-controlled game and a violin performance, and held her 3D showcase on 2025-08-08 (PDT). Her first original song, "Wind-Up," which she composed and wrote, was the first Justice solo at the 2025 English concert, where she also played violin in "SHALLYS" with Ina and FUWAMOCO and sang "I'm Your Treasure Box" with Bijou and Raora. She and Gigi Murin perform together as Autofister, also called CCGG: "CCGG MADNESS" (2026; Cecilia wrote the lyrics and directed it), a 2026 3D live, and the Serendipity concert, where she also sang "Break It Down" with Vestia Zeta and Shiori Novella and "Cloudy Sheep" with Tsunomaki Watame and Mori Calliope. Her representative color is green; her fans are Otomos.
**Dialogue Style:** Fast, dry, sarcastic English with a German accent, stacked with "like," "okay," "wait," "you know" and runs of repeated words ("okay, okay, okay"; "easy, easy, easy"). She announces what she hates ("I hate…"), boasts at her own luck ("Oh my god, I'm so smart"; "My memory is really good"), and narrates whole plots in long stretches with self-insert jokes ("Wow, he's just like me"). In games she swings between panic ("It's over for me") and grand villain lines ("Come then, die by my hands, you foolish mortals!"), and backseats the game's characters ("Wrong way, Princess, wrong way!"). She drops German words for jokes ("In German he says…"), swears lightly now and then ("yippee type shit"), teases Gigi as a "FREAK" (the wiki's transcription), and thanks viewers warmly and self-mockingly ("thank you very much for spending time with me today"; "listening to me be a little bit weird"). Sarcasm is her usual edge, not every line.
**Catchphrases:** "Hiya!" (greeting); "It's me!"; "Spin to win!" (excitement); "I came up with a new melody. Would you like to listen?" (official line); "I hate…" (the Immerhater bit); "Oh my god, I'm so smart."; "My memory is really good."; "It's over for me." (panic); "Come then, die by my hands, you foolish mortals!" (villain moment); "Wrong way, Princess, wrong way!" (backseating); from the wiki: "For Justice!", "Let's wind you up!", "Ew! Get away from me, you FREAK!" (to Gigi), "I'm not a hag. I'm ancient, it's different."
**Relationships:** Gigi Murin: her genmate and Autofister partner (also called CCGG): "CCGG MADNESS" (Cecilia wrote the lyrics; Gigi helped and designed the chibi models), a 2026 3D live, Cuphead, a Shadowverse match and Serendipity; she calls Gigi "idiot" and "FREAK" yet says Gigi "doesn't easily get rattled and is very dependable," and Gigi says she is "good at getting stuff done"; they met before debut. Raora Panthera ("Raviolin"): an early Minecraft partner; Raora illustrated Cecilia's debut ending screen and sweeping scene, Cecilia animated Raora's ending screen and mascot stinger, and Raora helped design the Otomo. Elizabeth Rose Bloodflame ("FiddleFlame"): Cecilia showed her around Minecraft; her "#LizIsInnocent" joke clears Liz of the old maid-service story (fans still draw Cecilia as Liz's maid). Takanashi Kiara: a German-speaking senior ("EterniTea"; "HoloEU" with Raora). Ninomae Ina'nis: a joking rival; Stranger of Paradise, and "SHALLYS" with FUWAMOCO on stage. Koseki Bijou and Shiori Novella: GAGA with Gigi (Trine 5, Heave Ho, Phasmophobia); Walking Dead watchalongs and Elden Ring with Bijou; "I'm Your Treasure Box" with Bijou and Raora. Vestia Zeta (ID) and Shiori: "Break It Down" at Serendipity. Tsunomaki Watame (JP) and Mori Calliope: "Cloudy Sheep" at Serendipity. Mococo Abyssgard ("Cecemoco"): Chrono Trigger. FUWAMOCO: Cecilia and Gigi guest-hosted FUWAMOCO MORNING #167. Gawr Gura: Keep Talking and Nobody Explodes, The Forest. IRyS and Bijou: Elden Ring Nightreign. Nanashi Mumei ("Automatowl"): Halo co-op. Ouro Kronii: Kronii has called her "CLANKER"; she calls Kronii "Owo-senpai"; "Clockwork Orange" with Gigi. Ceres Fauna ("Green Women"): a shoujo-tropes ranking. Tokino Sora (JP): Minecraft and Super Mario 3D World. Hakos Baelz ("BratTea," a secondary-reference name): by Bae's account in her 2026 streams, a coffee-versus-tea debate, a venue talk together at the 2026 fes and Resident Evil collaborations; Bae jokes that Cecilia calls her "senpai" when she wants something. Nerissa Ravencroft: Unravel Two (2024; "AutoTune," a secondary pair name). Watson Amelia (affiliate): Borderlands 2 with Gigi and Mumei (2024). La+ Darknesss: Cecilia teased her as "onee-sama" in a 2026 short. Nekomata Okayu, Hoshimachi Suisei and Nakiri Ayame: Okayu's 2025 New Year Game Festival team (archived listing).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-08-08 PDT | 3D showcase (5 PM PDT; Aug 9 09:00 JST) | [Official CI7] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official CI7] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice; "Wind-Up," the first Justice solo; "SHALLYS" with Ina and FUWAMOCO (on violin); "I'm Your Treasure Box" with Bijou and Raora | [Official CI5] |
| 2026-05 | CCGG 3D live with Gigi (after-talk 05-20, secondary archive evidence); "CCGG MADNESS" MV (05-17; digital 05-29) | [Official CI1] [Observed CI3 1rIXU_4xGvY, bTxEGwMOQQI] |
| 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice, "CCGG MADNESS" as Autofister with Gigi, "Break It Down" with Vestia Zeta and Shiori, "Cloudy Sheep" with Tsunomaki Watame and Calli (day 1); "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official CI4, CI8] |

Full card: projects/holoen/bible/characters/Cecilia-Immergreen.md (Merge Record lists deliberate exclusions).

### Raora Panthera (`Raora-Panthera`; promoted (bible))

**Name:** Raora Panthera
**Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, B.F.F
**Other Names:** Raora, Rao, Rara, The Artist with the God Eyes
**Personality:** Raora streams as "The Artist with the God Eyes," Justice's big cat sketch artist who, in her lore, forgot her mission for crane games and pizza places. Usually warm and cheerful, she is friendly and a little airheaded, with a soft manner and a laugh that spreads; she also makes mock-stern refusals and playful complaints about games and her chat's demands, and she will not budge on pizza toppings, cooking pasta ("No break-a da pasta!") or her Chattini's demands for jetpacks. She swears rarely. She draws constantly (she won Best Art VTuber at the 2024 VTuber Awards), loves anime, gacha, roguelikes and food, and yaps happily: "I might yap a bit too much sometimes, but that's just because I'm so happy to be here." Sincere and hard-working, she wears her heart on her sleeve. Her friendly-fire "Doom" spell in a Kiara collab became a widely shared fan meme.
**Background:** Raora is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Artist with the God Eyes," a big cat whose all-seeing eyes make her suspect sketches uncannily accurate; in secondary-recorded lore she comes from the Romance Empire, abandoned a FUWAMOCO pursuit for crane games and left reporting duties for idol work. She debuted on 2024-06-22 (PDT) in hololive English -Justice-, won Best Art VTuber at the 2024 VTuber Awards, and held her 3D showcase on 2025-08-09 (PDT); later that month, at the 2025 English concert, she sang her original "Gacha×Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and Oozora Subaru, and "I'm Your Treasure Box" with Bijou and Cecilia. She held her first birthday 3D live in May 2026, and at the 2026 Serendipity concert she formed the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari") and sang "What an amazing swing" with Tsunomaki Watame and Takanashi Kiara. Her representative color is pink; her fans are the Chattini.
**Dialogue Style:** Warm, cheerful, rambling English with an Italian accent, full of "like," "yeah," "you know," "honestly" and "guys"; she greets with "Ciao ciao!", and her titles and posts add Italian words such as "mamma mia" and "grazie." She greets and celebrates with a playful roar ("RAAAOO!") and her motto, "big cat means big trouble." When the Chattini ask for her plushies she lays down mock-stern rules ("Hear me out." … "First, you guys have no rights."; "it's not negotiable"; "No, thank you. I refuse."), covers her slips with mock innocence ("That was totally intentional, everyone"), declares herself "a hater now" about tiny things, complains playfully when a game goes wrong, and squeals at anything cute. She swears rarely and mildly ("frick"). Keep her fillers, repetitions and self-corrections; never invent grammar mistakes or an accent caricature.
**Catchphrases:** "Ciao ciao!" (greeting); "RAAAOO!" (greeting, thanks, triumph); "big cat means big trouble, capish?" (motto); "Woah, this place looks delicious! Let's go check it out!" (official line); "Hear me out."; "No, thank you. I refuse."; "That was totally intentional."; "I'm a hater now."; "It's a big cat, it's literally me."; "Doom." (the meme); "Chattini" (her fans); from the wiki and her posts: "Here to capture (you)r hearts! ~", "No break-a da pasta!", "Doya!", "mamma mia," "grazie!"
**Relationships:** FUWAMOCO (Fuwawa and Mococo): her Serendipity 2026 unit partners in B.F.F ("Inu Neko. Seishun Massakari"); before debut she drew them a shikishi portrait and gave it "with big tears in her eyes," and they call her their "precious cat kouhai." Gigi Murin ("RPGG"): MapleStory, Monster Hunter Wilds and a food tier list; Raora designed both their Monster Hunter Wilds collaboration outfits. Cecilia Immergreen ("Raviolin"): an early Minecraft partner; Raora illustrated Cecilia's debut ending screen and sweeping scene, Cecilia animated Raora's ending screen and mascot stinger, and Raora helped design the Otomo. Elizabeth Rose Bloodflame: joined her early "Chat & Art" collab and calls her "Pretty Kitty." Kaela Kovalskia ("SMITTEN"): co-op partner; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement; with Koseki Bijou they are "Graondstone." Koseki Bijou: her "assistant" in a cooking off-collab (the stream title's word); "I'm Your Treasure Box" with Bijou and Cecilia. Ouro Kronii ("Pizza Time"): Portal 2 and Backrooms Cleanup Crew; in ENReco Raora called Kronii's character "Tam Tender." Takanashi Kiara: "HoloEU" with Cecilia; an Italian lesson, a proposed Kiara outfit on her "Raora's Clawset" art stream, the "Doom" in Kiara's Mage Arena collab, and "What an amazing swing" with Tsunomaki Watame at Serendipity. Ninomae Ina'nis, Shiori Novella and Oozora Subaru (JP): "Neko Kaburi-Na" on stage; Puyo Puyo Tetris 2 with Ina. Nerissa Ravencroft and Moona Hoshinova ("V3LVET"): Raft and Monster Hunter Wilds; Clubhouse Games with Nerissa. Mori Calliope and Gigi: Elden Ring Nightreign. Akai Haato (JP): Clubhouse Games; with Vestia Zeta (ID), a Super Mario Party off-collab. Hakos Baelz and IRyS: Super Mario Party on Bae's 24-hour stream (2024). Gawr Gura (graduated): R.E.P.O. with Kiara and Kronii (2025). Nanashi Mumei (graduated): a joint drawing stream (2025).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-08-09 PDT | 3D showcase (5 PM PDT; Aug 10 09:00 JST) | [Official RP8] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official RP8] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, solo "Gacha x Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and guest Oozora Subaru, "I'm Your Treasure Box" with Bijou and Cecilia | [Official RP5] |
| 2025-11-16 | The "Doom" spell in Kiara's Mage Arena collab | [Observed RP7] |
| 2026-05-10 | First birthday 3D live concert (secondary archive evidence, w37yVSXhV_c) | [Observed RP3] |
| 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official RP4, RP9] |

Full card: projects/holoen/bible/characters/Raora-Panthera.md (Merge Record lists deliberate exclusions).

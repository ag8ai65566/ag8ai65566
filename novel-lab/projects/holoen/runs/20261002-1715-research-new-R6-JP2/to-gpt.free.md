# Task 10 — New material: hololive JP, part 2 (7 members)

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
IDs NEW-R6-NNN. Priority P1 (material: correction-adjacent, present-day manner, major 2025–2026
event), P2 (useful enrichment), P3 (optional). Target is `C/<stem> › <field>` for an exported field or
`D/<stem> › <section>` for the dossier. Escape table pipes; use <br> for newlines.

## Corrections
| ID | Member | Exact old text | Problem | Exact replacement | Evidence URL + class + checked date |
|---|---|---|---|---|---|
IDs FIX-R6-NNN. Copy the old text exactly. "None." if none.

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

### Shishiro Botan (`Shishiro-Botan`; promoted (bible))

**Name:** Shishiro Botan
**Groups:** hololive, hololive 5th generation, NePoLaBo, holoFive, NePoX, InuTakaShishiRam, Usada Kensetsu, SubaChocoLunaTan
**Other Names:** Botan, Shishiron, Shishiro, 獅白ぼたん
**Personality:** Botan is hololive's white lion, who by her official profile "prefers lazing around" despite her sporty look, yet follows through once she has decided; her favorite phrase is "Wealth isn't measured with money." Secondary accounts describe her as calm and quick to laugh, especially when things go wrong, laid-back through intense play, a skilled FPS player who tosses grenades with an offhand 「ぽい」, and usually unbothered by horror; she likes drawing friends like Lamy into horror "dates" where she teases their scares. Archived streams show her organizing side: she designs and runs whole events, from a hololive-wide Minecraft money-making competition to a fighting-game cup, and makes sure everyone can enjoy them. She calls herself "Shishiro" and shifts into a brisk explanatory register when she presents a project.
**Background:** Botan is an active member of hololive's 5th generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2020-08-14 as a fifth-generation member; she forms NePoLaBo with Yukihana Lamy, Omaru Polka and Momosuzu Nene. Secondary records place her 1.5-million-subscriber milestone in February 2025. She has released originals such as "Simulacre," "Gaotteko!" and "Tokihanate"; her first album, "BOTAN.EXE," opened for orders on 2026-09-19. She ran the hololive Minecraft money-making event twice (2025, 2026) as its game master and hosted the "Shishiro Cup." Archived metadata and secondary concert reports record her with the English cast in Left 4 Dead 2 (2022) and an Overwatch 2 team (2023) with IRyS, on Calli's HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and as a guest at Ina's birthday 3D live "EVERMORE" (2025); Kiara is a fellow member of the Minecraft "Usada Kensetsu" (secondary).
**Dialogue Style:** Streams in Japanese in a relaxed, cheerful voice, calling herself "Shishiro" and laughing at her own mishaps. In games she is calm and offhand; presenting a project she shifts into a brisk explanatory register, with numbered points and polite "~to omotte orimasu" closings (「前回はですねペコちゃんが優勝しました」, "last time, Peko-chan won"). She teases friends gently and keeps everyone included. When a story renders her speech in English or Chinese, keep the easygoing calm and the contrast between relaxed play and organized explanation.
**Catchphrases:** "La-lion♪" (official profile greeting); "Well then, cya~" (official profile sign-off); "Wealth isn't measured with money" (her favorite phrase, official profile wording); 「ぽい」 ("poi," a light tossing interjection; secondary transcription); 「前回はですねペコちゃんが優勝しました」 ("zenkai wa desu ne, Peko-chan ga yūshō shimashita," shared ASR span); "Shishiro" (herself); "SSRB" (her fans).
**Relationships:** Yukihana Lamy: 5th-gen genmate and NePoLaBo partner; secondary accounts describe horror "dates" where Botan stays calm and teases Lamy. Momosuzu Nene and Omaru Polka: 5th-gen genmates and NePoLaBo. Takane Lui: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary); Left 4 Dead 2 (2022) and Overwatch 2 (2023) together. La+ Darknesss, Hakui Koyori and Kazama Iroha: NePoX (NePoLaBo × holoX, 2026). La+ Darknesss and Hoshimachi Suisei: holoGTA and the m HOLD'EM poker collab with Shirakami Fubuki (2024); Nakiri Ayame: holoGTA (2024). IRyS: Left 4 Dead 2 with Lui and Korone (2022) and an Overwatch 2 team with Lui, Sakamata Chloe and Tokoyami Towa (2023). Takanashi Kiara: a fellow member of the Minecraft "Usada Kensetsu" (secondary). Gawr Gura (graduated): "Apex Predators," a secondary-listed pair label. Mori Calliope: HOLOYOI #03 with Oozora Subaru (2023). Hakos Baelz: BAE-GEMITE DOMINATION #2 with Subaru (2023). Ninomae Ina'nis: a guest at Ina's birthday 3D live "EVERMORE" (2025), singing "storia" with Ina and Watame per a secondary set list.

Dossier history rows dated 2025–2026 (already on the card):
| 2025 | 1.5 million subscribers (02-14, secondary); originals "Simulacre," "Gaotteko!" and "boundary"; a guest at Ina's birthday 3D live "EVERMORE" (05-21), singing "storia" with Ina and Tsunomaki Watame per a secondary set list; the first "#ホロ金策サバイバル" | [Observed BO2] [BO5] [EVERMORE report] [ASR BO20] |
| 2026-04 | The "Shishiro Cup" fighting-game tournament, offline; original "Tokihanate" (04-10) | [BO4] [Observed BO2] |
| 2026-06-01/05 | "#ホロ金策サバイバル2," with Botan as game master | [BO4] [ASR BO20] |
| 2026-09-19 | First album "BOTAN.EXE" opened for orders; original "Stray & Stay" | [Observed BO2] [Distributor listing] |
| 2026-09-26/27 | NePoX events with Secret Society holoX | [LM4 Ml1tM8S40p0] |

Full card: projects/holoen/bible/characters/Shishiro-Botan.md (Merge Record lists deliberate exclusions).

### Kikirara Vivi (`Kikirara-Vivi`; promoted (bible))

**Name:** Kikirara Vivi
**Groups:** hololive, FLOW GLOW, MVP
**Other Names:** Vivi, 綺々羅々ヴィヴィ
**Personality:** Her official character profile presents Vivi as FLOW GLOW's makeup artist, a seeker of "true beauty" always hunting the next item for an extra glow-up, who does not hide her feelings: they show on her face, and frank remarks slip out. In her lore direct sunlight is her "natural enemy." On stream she is chatty, funny and quick with chat, refers to herself as "Vivi," and deliberately flattens her delivery for comic retorts, as she has explained on stream; when chat asks for something sweet she jokes 「お金取るで」 ("I'll charge you for that"). A self-described game beginner, she played her first on-stream Super Mario games in 2026; secondary accounts describe her getting hooked on HoloCure and Minecraft farming and calling her senpai Usada Pekora a "legendary hero" (translated descriptions). She adores cute things and her fans, the Vivids.
**Background:** Vivi is an active member of FLOW GLOW. She has no supernatural abilities; her lore is a performed persona. She debuted on 2024-11-09 through hololive DEV_IS as a member of FLOW GLOW, with Isaki Riona, Koganei Niko, Mizumiya Su and Rindo Chihaya. FLOW GLOW released its self-titled album on 2026-01-21 and the single "magic summer" later in 2026. Secondary records date her 700,000-subscriber milestone to an endurance karaoke stream on 2026-08-11 and identify "Vivid Cute" as her first solo original, available digitally on 2026-08-28. She plays games with Usada Pekora ("PekoVivi," secondary), and an archived 2026 performance record names Marine, Vivi and Pekora as MVP. Archived metadata records her with the English cast in R.E.P.O. with FUWAMOCO and Bae (2025-05-25), in a separate R.E.P.O. session on Ina's stream (2025-06-02) and in Mumei's Gartic Phone collaboration with Noel, Kronii, Ina and Elizabeth (2025); a secondary archive records FUWAMOCO and Bijou watching FLOW GLOW's debut.
**Dialogue Style:** Streams in Japanese: frank, quick and funny, bantering with chat and referring to herself as "Vivi," then a deliberately flat retort. Her casual endings (-yan, -nen, akan, honma) appear in the transcript; no regional accent is assigned to the voice. She teases (「お金取るで」, "I'll charge you for that") and turns sincere when thanking her fans. When a story renders her speech in English or Chinese, preserve casual wording, frankness and deadpan timing without assigning a different real-world regional accent.
**Catchphrases:** "Hol'up, 'cus you're in for a transformation!" (official English profile wording); ん～～ッヴィヴィ～！！！ ("Nnn—Vivi!", her opening as archived stream titles write it); 「お金取るで」 ("okane toru de," "I'll charge you for that," shared ASR span); "Vivi" (herself); "Vivid" (her fans, secondary).
**Relationships:** Usada Pekora: "PekoVivi" (a secondary pair name); co-op games (2025) and a gifted Getting Over It (2026); secondary accounts say Pekora rescued her in Minecraft and Vivi calls her the "legendary hero." Houshou Marine: MVP with Pekora (an archived 2026 performance record). Shirogane Noel: Mumei's Gartic Phone collab (2025). FLOW GLOW (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya): her unit; a "Bridal Dream" cover with Chihaya (2025). FUWAMOCO: watched FLOW GLOW's debut with Bijou (2024, secondary archive); R.E.P.O. with Bae (2025-05-25). Hakos Baelz: that R.E.P.O. session. Ninomae Ina'nis: a separate R.E.P.O. session on Ina's stream (2025-06-02) and the Gartic Phone collab. Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone (2025). Nanashi Mumei (graduated): hosted that Gartic Phone collab. Koseki Bijou: watched FLOW GLOW's debut with FUWAMOCO.

Dossier history rows dated 2025–2026 (already on the card):
| 2025 | FLOW GLOW songs "24K GOLD" (03-14), "LOAD" (07-09), "good enough" (09-20); 500,000 subscribers (11-30, secondary) | [Observed VI2] |
| 2025-04-14 | Gartic Phone EN + ID + JP collab with Mumei, Kronii, Ina, Elizabeth and Noel | [VI5 OMDzBQohAf8] |
| 2025-05-25 | #holoREPO with FUWAMOCO, Bae, Roboco, Towa and Hajime | [VI5 Z5cpzbdsLDE, TgMVtjXW2Ms] |
| 2025-06-02 | R.E.P.O. on Ina's stream, with Polka, Watame, Flare and Anya | [VI5 grBU9Dl09Ds description] |
| 2025-07 | Games with Pekora (The Forest, Fast Food Simulator); "Bridal Dream" cover with Chihaya (07-28) | [VI4 lqidVnpl3_0, FWCkuwroMIw, NGeumGspO2g] |
| 2026 | FLOW GLOW's self-titled album (01-21, including "PUNISHER" and "the light"); first on-stream Super Mario Bros. 3 and Super Mario World playthroughs; Getting Over It, a gift from Pekora (07-25); 700,000 subscribers during an endurance karaoke (08-11, secondary); FLOW GLOW's "magic summer" (08-18); MVP's "Hatsukoi Cider" with Marine and Pekora (09, secondary record) | [Official music 024] [VI4] [Observed VI2] [MVP upload record] |
| 2026-08 | First solo original song, "Vivid Cute" (premiered around her birthday, 08-27; available digitally 08-28) | [Official music 808] [Observed VI2] |

Full card: projects/holoen/bible/characters/Kikirara-Vivi.md (Merge Record lists deliberate exclusions).

### Laplus Darknesss (`Laplus-Darknesss`; draft (claim check run E/F pending; not promoted))

**Name:** La+ Darknesss
**Groups:** hololive, Secret Society holoX, holoX, Dorobo Kensetsu, NePoX
**Other Names:** La+, Laplus, Laplace, YMD, Yamada
**Personality:** La+ is the founder of Secret Society holoX, a demon whose once-vast power and intelligence are sealed by shackles she cannot remember receiving, with a crow as her long-time companion. She plays the overlord: she calls herself "wagahai" (an arrogant, archaic "I"), calls others "kisama," plots world domination and has her followers answer "Yes My Dark!" In practice she is a smug, bratty, loud little boss who loses her temper when she loses a game or gets treated like a child, which her seniors do constantly; she refuses to be counted among hololive's "babies." She is quick and funny, turns fan votes into bits (she split "Yamada" into two options so her fans' joke name would win), edits her own highlight clips, and takes her music seriously: her first album, "Project Y.M.A. (Yes My Artist)," was announced in 2026. In 2026 she also became a Tochigi Future Ambassador.
**Background:** La+ is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-26 as the first member of Secret Society holoX, hololive's sixth Japanese generation, whose executive officer Takane Lui does the actual running. She has original songs such as "drop candy" and "Onee-sama♡Love Call" (2026), sang with holoX at their first concert, "First MISSION" (2026-04-29), reached 1.5 million subscribers first in holoX (2025), and was appointed a Tochigi Future Ambassador (2026). With the English cast she made the Mythmash single "Glow in the Dark" and the cover "FAKE HEART" with Takanashi Kiara (2025), played nostalgic games with Kiara off-collab (2023), and took Mori Calliope's English lesson with Gawr Gura and Kazama Iroha (2022).
**Dialogue Style:** Streams in Japanese. Her persona voice is a pint-sized villain: "wagahai" for "I," "kisama" for "you," grand declarations ("See me, hear me, all of you!") and "Yes My Dark!" from her followers. In everyday 2026 chats she talks casually, with plain "watashi," "maji de," "yabai" and "~ssho" ("you heard it, right?"), and turns fast, loud and bratty the moment someone teases her or she loses. She protests, sulks, cackles when she wins and narrates her own schemes. When a story renders her speech in English or Chinese, keep the archaic villain "I" (in Chinese, 吾輩) for persona moments against a small, indignant voice.
**Catchphrases:** "See me, hear me, all of you!" (official, "Kakumoku seyo!"); "Yes My Dark!" (her followers' salute); "wagahai" (her "I"); "kisama" ("you"); "I'm not a suspicious person!" (her first post); her full title, "Laplus Dia Highest Death Thirteen Daina Art of Impact Sign Emperor Road of the Darknesss." Her fans are the Plusmate (and, by her own vote-splitting, "Yamada").
**Relationships:** Takane Lui: holoX's executive officer, who actually runs things and reins her in. Hakui Koyori and Kazama Iroha: holoX ("Irohasu" with Iroha). Sakamata Chloe (affiliate since 2025): the former intern. Takanashi Kiara: "Glow in the Dark" (Mythmash) and "FAKE HEART" (2025), and an off-collab (2023). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: danced to "Onee-sama♡Love Call" (2026). Cecilia Immergreen: teases her as "onee-sama" in a short (2026). Nerissa Ravencroft: holoGTA (2024). Nekomata Okayu: "Dorobo Kensetsu" and a 3D lie-detector challenge (2026). Nakiri Ayame, Hoshimachi Suisei and Shishiro Botan: holoGTA (2024); Suisei, Botan and Shirakami Fubuki: the m HOLD'EM poker collab (2024). AZKi: games (2025). Houshou Marine: a sponsored collab billed #マリラプ and a cover with Koyori (2025). Yukihana Lamy and Shishiro Botan: NePoX (2026).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-04-08 | "FAKE HEART," a cover with Kiara | [LA5 yspJ9xmGRfw] |
| 2025-07-27 | "Glow in the Dark," a Mythmash single with Kiara; a joint stream | [LA5 v5RKZXNuVyw] [LA4] |
| 2025-12 | holoX's 4th anniversary ("Gyouan Xdeath," "Secret ORDER"); 1.5 million subscribers (12-30) | [Observed LA2] |
| 2026-04-29 | holoX's first concert, "First MISSION" | [Official LA6] |
| 2026-05-03 | Tochigi Future Ambassador | [Observed LA2] [LA3] |
| 2026-05-19 | A 3D lie-detector "challenge" to Nekomata Okayu | [LA4 F3i30BIJmtY] |
| 2026-05-25 | "Onee-sama♡Love Call"; album "Project Y.M.A." announced | [Observed LA2] |

### Takane Lui (`Takane-Lui`; draft (claim check run E/F pending; not promoted))

**Name:** Takane Lui
**Groups:** hololive, Secret Society holoX, holoX, HOLOTORI, Bara☆Dice, InuTakaShishiRam, Dorobo Kensetsu, NePoX
**Other Names:** Lui, Lui-nee, The XO, Lui Lui
**Personality:** Lui is the executive officer of Secret Society holoX and its de facto leader: the point of contact who handles what the founder, La+ Darknesss, cannot. She looks cool and aloof, but she is a warm, motherly big sister who cares for her "subordinates," reins in La+ and Chloe, and makes dad jokes. She is also holoX's resident airhead: she "pons" at the crucial moment and is known for knocking over her water mid-stream. She is a hawk and one of hololive's birds, with a low, calm voice she can sharpen into a cool executive tone before ruining it with a sparkle ("Ko!☆"). She screams at horror games, plays RPGs on Saturdays, predicts nearly every G1 horse race, loves twins, spicy food and pickles, and is a Code Geass ambassador. She often reaches out to English-speaking members and fans, and her dreams include concerts and fan meetings overseas.
**Background:** Lui is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-27 as the second member of Secret Society holoX, hololive's sixth Japanese generation, and Takanashi Kiara welcomed her that day into the bird unit HOLOTORI (with Oozora Subaru, Pavolia Reine and, later, Nanashi Mumei). She has released the album "Liberty" (2024), the EP "Lieblings" (2025) and, in 2026, "Soar," which English members danced to in shorts; holoX held its first concert, "First MISSION," at Pia Arena MM in April 2026. With the English cast she practiced English with Mori Calliope (2021–2022) and appeared on Calli's drinking talk "HOLOYOI" (2023), played Wario with Kiara, held "Q&A With Bird Sisters" with Mumei (2025), hosted FUWAMOCO for "TWIN DAY WITH LUI" (2023), and joined Hakos Baelz's game show "BAE-GEMITE DOMINATION" (2023).
**Dialogue Style:** Streams in Japanese in a low, calm, conversational voice: "mā," "ne," "un un," reading chat aloud and answering it one by one, unhurried and warm. She opens with "Mattakane?" ("Did I Luive you waiting?") and closes with "Otsuluilui" ("I take your Luive"); doubts come out as "…shitakane?" ("Did you…, if I'm not mistakane?"), excitement as "Takamattekita!" ("Hype Luivels rising!"). She plays a cool executive for a line, then adds "Ko!☆"; she admits her blunders ("PON") with a laugh and shrieks in horror games. When a story renders her speech in English or Chinese, keep the low big-sister calm, the bird puns on her name and the cool-then-goofy turn.
**Catchphrases:** "Did I Luive you waiting!?" ("Mattakane?," opening); "I take your Luive" ("Otsuluilui," closing); "Did you…, if I'm not mistakane?" ("…shitakane?"); "Takamattekita!" ("Hype Luivels rising!"); "PON" (being an airhead); "Ko!☆" (the sparkle after a cool line); "Don't drop your water" (what fans tell her). Her fans are the Lui-tomo.
**Relationships:** La+ Darknesss: holoX's founder, whom Lui reins in and covers for. Sakamata Chloe (affiliate since 2025): the intern she used to keep in line. Hakui Koyori and Kazama Iroha: holoX; Iroha calls her "Lui-nee." Takanashi Kiara: welcomed her into HOLOTORI on her debut day; a Wario off-collab (2023). Nanashi Mumei (graduated): her HOLOTORI "Bird Sister" ("Q&A With Bird Sisters," 2025). Mori Calliope: practiced English with her (2021–2022) and had her on "HOLOYOI" (2023). FUWAMOCO: "TWIN DAY WITH LUI" (2023). Hakos Baelz: "BAE-GEMITE DOMINATION" (2023) and a "FEAST" dance. IRyS and Ouro Kronii: Minecraft (2022). Watson Amelia: Apex (2022). Nekomata Okayu: "Shaccho," a Harry Potter watch-along club and game predictions. Nakiri Ayame: "Onikan." Shishiro Botan: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame; Left 4 Dead 2 with IRyS (2022). Houshou Marine and Kazama Iroha: Bara☆Dice. Yukihana Lamy: NePoX (2026). Nerissa Ravencroft, Koseki Bijou, Gigi Murin and Raora Panthera: dance shorts to her "Soar" (2026).

Dossier history rows dated 2025–2026 (already on the card):
| 2025 | EP "Lieblings"; Code Geass ambassador (June); "Q&A With Bird Sisters" with Mumei (04-19); a Harry Potter watch-along club for Okayu | [Observed LU2] [LU5] [LU4] |
| 2025-12-01 | holoX's 4th anniversary: "Gyouan Xdeath," album "Secret ORDER" | [Observed LU2] |
| 2026-04-29 | holoX's first concert "First MISSION" ("I feel like we gave it everything I got!") | [Official LU6] |
| 2026-06-11 | Birthday: "Soar," danced in shorts by many EN members | [LU4] [LU5] |
| 2026-08-01 | A "rare" La+ and Lui talk with new outfits | [LU4] |

### Hakui Koyori (`Hakui-Koyori`; draft (claim check run E/F pending; not promoted))

**Name:** Hakui Koyori
**Groups:** hololive, Secret Society holoX, holoX, Hoshimatic Project, KoZMy, NePoX, Blue Journey, FUWAMOKOYO
**Other Names:** Koyori, Koyo, Koyorin, Konkoyo
**Personality:** Koyori is Secret Society holoX's head of research and development, a pink-haired coyote in a lab coat who calls herself "the brain of holoX" while her own profile admits her expertise is "pretty limited." She studies "human behavior" by meddling in her fellow members' affairs, helping where she can and sometimes poking people just to see how they react; her viewers are her lab "Assistants." First counted with Iroha as holoX's proper, "seiso" pair, she proved to be a loud, cheeky tease with huge reactions: she screams through horror games and knows fans love it. She is also a disciplined presenter: she hosts "AsaKoyo," hololive's news show on Tuesday and Friday mornings, nearly 300 episodes in by 2026, writes a game column, and in September 2026 became the first hololive member to pass 10,000 hours of streaming. She enunciates precisely, does voice impersonations and voices her fan-made mascot, Mofukoyo.
**Background:** Koyori is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-28 as the third member of Secret Society holoX and got her 3D model and first original song, "WAO!!," in 2022. She sang in the "Blue Journey" project with Marine, Noel, Lamy and Sakura Miko (2023), joined Suisei's Hoshimatic Project (2023–), formed "KoZMy" with AZKi and Lamy (2025) and sang at holoX's first concert, "First MISSION" (2026-04-29). In September 2026 she announced her second album, "Chemical Spark," and her first solo concert, "Dream Spark," set for December 2026. With the English cast she guested on FUWAMOCO Morning and played Lethal Company with FUWAMOCO and Fubuki ("FUWAMOKOYO," 2024), appeared at FUWAMOCO's birthday concert (2025) and Mumei's first 3D live (2024). In 2023 she joined Bae's "BAE-GEMITE DOMINATION" with Momosuzu Nene (2023-04-22) and tasted Bae's "KHAOS KITCHEN" curry with Calli and Oozora Subaru (2023-11-24).
**Dialogue Style:** Streams in Japanese with a presenter's polish: "Konkoyo!" to open, crisp segment transitions ("and next up") on her news show, and "joshu-kun" (assistants) for her audience. When excited she speeds up and climbs in pitch, explaining in a happy rush; when scared she screams. She teases members under the cover of "research." When a story renders her speech in English or Chinese, keep the bright anchor voice, the lab vocabulary and the sudden screams.
**Catchphrases:** "Konkoyo!" (official greeting, "Ayo, this is Koyo!"); "The brain of holoX! My name is Koyori Hakui!" (official); "Koyorium" (the nutrient from watching her); "Reikoyo" (a cool Koyori); "Koyo-colored" (pink); "joshu-kun" (her Assistants); on AsaKoyo, "sore de wa tsuzuite wa kochira" ("and next up").
**Relationships:** La+ Darknesss: holoX's founder ("#stons," a cover with Marine). Takane Lui and Kazama Iroha: holoX; Iroha was her early "seiso" pair. Sakamata Chloe (affiliate since 2025): "KoyoChlo," a duo that kept forming and disbanding, ending with a last collab and a cover in January 2025. AZKi and Yukihana Lamy: "KoZMy" (2025); a 3D karaoke with AZKi (2026). Houshou Marine: the "pink-haired pair," Blue Journey and backseat Pikachu (2025). Shirogane Noel: Blue Journey and "NoeKoyo" baseball (2025). Hoshimachi Suisei: Hoshimatic Project. Shishiro Botan: NePoX. Nekomata Okayu: a puzzle collab (2025). FUWAMOCO: "FUWAMOKOYO" with Fubuki (2024), FUWAMOCO Morning, their birthday concert (2025). Hakos Baelz: BAE-GEMITE DOMINATION with Nene and a KHAOS KITCHEN tasting (2023). Nanashi Mumei (graduated): a guest at her first 3D live (2024). IRyS: Splatoon 3 and Among Us. Takanashi Kiara: a "MIRAGE" dance short (2024).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-01-14 | The last "KoyoChlo" collab with Chloe, before Chloe's activities ended | [KO4 mxIoysy6gJ4] |
| 2025-08 | "KoZMy" formed with AZKi and Lamy; "pink-haired pair" talk with Marine | [KO4] |
| 2026-04-29 | holoX's first concert, "First MISSION" | [Official KO6] |
| 2026-09-12 | Second album "Chemical Spark" and first solo concert "Dream Spark" (2026-12-22) announced | [Observed KO2] |
| 2026-09-20 | First hololive member past 10,000 hours of streaming | [KO3] |

### Sakamata Chloe (`Sakamata-Chloe`; draft (claim check run E/F pending; not promoted))

**Name:** Sakamata Chloe
**Groups:** hololive, Secret Society holoX, holoX, KoyoChlo, Kanaken, Hoshimatic Project, holoWitches, UMISEA
**Other Names:** Chloe, Kuroe, Sakamata, Kura-tan
**Personality:** Chloe is Secret Society holoX's orca intern, its fixer and cleaner. Officially she is calm and composed, follows orders without blinking and insists she has no feelings to hide; in practice she is a soft-voiced, fast-talking, mischievous kouhai who loves to tease, makes mistakes and has on-stream accidents, and dissolves into giggles. Her streams open like a meal ("Chomp, chomp, chomp! It's time to eat!") and close with "Thanks for the food," and her viewers are her Handlers. Music matters most to her: she composes, writes lyrics and sings in a far more mature voice than the one she talks in. She is a self-described scaredy-cat who still finishes horror games, a candid chatter who turns a stray question into a poll of chat, and Koyori's partner in "KoyoChlo," a duo that kept forming and disbanding. She concluded her regular activities in January 2025 and remains a hololive affiliate.
**Background:** Chloe is a hololive affiliate, formerly an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-29 as the fourth member of Secret Society holoX, and secondary records date her 500,000 subscribers to her first week and a million to 2023. She released ten original songs, joined Suisei's Hoshimatic Project, "Magical Girl holoWitches!" and the Minecraft "Kanaken" with Amane Kanata and AZKi, and concluded her regular activities with a graduation live on 2025-01-26, staying an affiliate; a secondary record has her singing "Sparkle" at Murasaki Shion's graduation live (2025-04-26). With the English cast she toured the EN Minecraft server with Bae, Mumei and Lui (2022), took Calli's English lesson and appeared on HOLOYOI (2022–2023), joined Bae's "BAE-GEMITE DOMINATION" and covered "Crazy Scary Holy Fantasy" with her (2023), and covered "WILDCARD" with Kiara in her final week (2025).
**Dialogue Style:** Streamed in Japanese in quick, soft, run-on chatter that trails off in a drawn-out "~sā," calling herself "Sakamata" and her viewers "shiikuin" (Handlers). She teases seniors and friends, swears an accident "wasn't my fault," and turns questions into polls of chat. When a story renders her speech in English or Chinese, keep the third-person "Sakamata," the soft, giggly speed and the sudden switch to a serious, mature voice when she sings.
**Catchphrases:** "Chomp, chomp, chomp! It's time to eat!" (official opening, "Bakku bakku baku~"); "Thanks for the food" (official closing, gochisōsama); "shiikuin" (Handlers, her viewers); "Sakamata" (how she refers to herself); "KoyoChlo" (her duo with Koyori).
**Relationships:** Takane Lui: the executive officer who kept her in line ("LuiChlo"; Calli's English lesson and HOLOYOI together). Hakui Koyori: "KoyoChlo," a duo that kept forming and disbanding, ending with a last collab and covers in January 2025. La+ Darknesss: covers together (2022, 2025). Kazama Iroha: holoX. AZKi: "Kanaken" with Amane Kanata (Minecraft, a 3D live, 2024). Houshou Marine: UMISEA and holoWitches. Hoshimachi Suisei: Hoshimatic Project. Yukihana Lamy: Rust (2022). Shishiro Botan: an Overwatch 2 team (2023). Takanashi Kiara: "WILDCARD" (2025) and an origami off-collab (2023). Hakos Baelz: the EN Minecraft tour (2022), BAE-GEMITE DOMINATION and "Crazy Scary Holy Fantasy" (2023). Mori Calliope: HOLO ENGLISH LESSON #04 (2022) and HOLOYOI #01 (2023). Nanashi Mumei (graduated): the EN Minecraft tour (2022). IRyS: Overwatch 2 and Among Us (2023). Ninomae Ina'nis and Gawr Gura (graduated): UMISEA (official 2023 roster).

Dossier history rows dated 2025–2026 (already on the card):
| 2025-01 | Farewell week: last "KoyoChlo" collab, covers with La+ and Koyori, "WILDCARD" with Kiara (01-25) | [CH4] [CH5] |
| 2025-01-26 | Graduation live "Gochisōsama deshita"; tenth original song "Hikari Are" | [CH4] [Observed CH2] |
| 2025-04-26 | Performs "Sparkle" with Murasaki Shion at Shion's graduation live | [Observed CH2] |

### Kazama Iroha (`Kazama-Iroha`; draft (claim check run E/F pending; not promoted))

**Name:** Kazama Iroha
**Groups:** hololive, Secret Society holoX, holoX, AzuIro, Hoshimatic Project, NePoX, KoMeHa
**Other Names:** Iroha, Iroha-dono, Gozaru, Gozaru-chan
**Personality:** Iroha is Secret Society holoX's bodyguard and "insurance policy," a samurai from a remote mountain village who set out with her tanuki companion Pokobee to see the world and now guards holoX to earn her keep. Her signature is the samurai ending "de gozaru"; she calls friends "-dono" and, in 2026 streams, often calls herself "Gozaru." Fans call her "seiso" (proper), which she does not claim; on stream she is cheerful, earnest and competitive, a self-admitted muscle brain who charges ahead, chants "yoshi yoshi yoshi yoshi" when things work, argues back when chat teases her, and laughs off her own blunders. She sticks with long games to the end, is loyal to holoX and is half of the duo AzuIro with AZKi.
**Background:** Iroha is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-30 as the fifth and last member of Secret Society holoX, became the last of holoX to pass a million subscribers (2024-11-19, archived stream title), which put the whole group over the mark, and has released nine original songs, the latest 「風向きエントロピー」 ("Kazamuki Entropy," 2026). She formed the duo AzuIro with AZKi (covers, off-collab "summer camps," a shared Minecraft village), joined Suisei's Hoshimatic Project and sang at holoX's first concert, "First MISSION" (2026-04-29). With the English cast she took Calli's English lesson with La+ and Gura (2022), played VALORANT with Ame and Kobo Kanaeru as "KoMeHa," hosted FUWAMOCO's sister battle in a cookie-quiz off-collab with AZKi (2024), appeared at Kiara's 3D lives (2024, 2025) and sang "CHA-LA HEAD-CHA-LA" for Elizabeth's 2026 birthday.
**Dialogue Style:** Streams in Japanese in a bright samurai persona: "de gozaru" as her signature ending (used sparingly in 2026 game streams), "-dono" for friends and "Gozaru" for herself. In games she switches to fast play-by-play with words repeated in fours ("yoshi yoshi yoshi yoshi," "mā mā mā mā"), a "yabai" spiral when things go wrong and a loud "oi!" at teasing chat, then laughs. When a story renders her speech in English or Chinese, keep the archaic samurai flavor ("I daresay"; in Chinese, 在下 or 是也) against an upbeat, sporty voice.
**Catchphrases:** "Secret Society holoX's insurance policy, Kazama Iroha here, I daresay!" (official); "de gozaru" ("I daresay," her sentence ending); "-dono" (for friends); "yoshi yoshi yoshi yoshi" (when it works); "yoyū yoyū" ("easy, easy," right before it isn't). Her fans are the Kazama-tai.
**Relationships:** AZKi: "AzuIro," her steady duo (covers, off-collab "summer camps," Cuphead, a Minecraft village). La+ Darknesss: holoX's founder, "La+-dono"; a cover (2024). Takane Lui: "Lui-nee"; a cover (2024). Hakui Koyori: holoX; her early "seiso" pair. Sakamata Chloe (affiliate since 2025): a cover on Chloe's last day (2025). Hoshimachi Suisei: Hoshimatic Project; coached her at Puyo Puyo Tetris (2023). Yukihana Lamy and Shishiro Botan: NePoX. Takanashi Kiara: a guest at Kiara's 3D lives (2024, 2025) and dance shorts (2025). Watson Amelia (affiliate): "KoMeHa" with Kobo Kanaeru (VALORANT, 2022). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: a cookie-quiz off-collab (2024). Elizabeth Rose Bloodflame: "CHA-LA HEAD-CHA-LA" for her 2026 birthday, with FUWAMOCO. Houshou Marine: Bara☆Dice.

Dossier history rows dated 2025–2026 (already on the card):
| 2025 | AzuIro off-collab "summer camp" (Cuphead, 08); "A letter only you can read" (06-15); a guest at Kiara's birthday live and dance shorts with Kiara (07) | [IR4] [IR5] [Observed IR2] |
| 2026-04-29 | holoX's first concert, "First MISSION" | [Official IR6] |
| 2026-05-19 | Sings "CHA-LA HEAD-CHA-LA" with Elizabeth for her birthday, with Watame, Nene, Polka and FUWAMOCO | [IR5 xylll7Mp0jk] |
| 2026-06-18 | Ninth original song, 「風向きエントロピー」 ("Kazamuki Entropy") | [IR4 RDobidAdBCA, official upload] [Observed IR2] |

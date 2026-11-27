# Review request for Gemini Neon — holoen r02, packet A

> 給作者：把這整個檔案交給 Gemini Neon（桌面版），請它照下面的指示審查；它的回覆整段貼回給 Claude 即可。

You are the independent second reviewer of a Sudowrite story bible about hololive VTubers. Claude (an AI model) researched
and wrote the material below alone on 2026-11-27; nobody else has checked it yet. Your job is to find what is wrong,
unsupported, misattributed or out of scope, with evidence, so that Claude can fix it. Today is 2026-11-27. The project's
baseline date is 2026-09-30; facts after it are allowed when dated.

## Project rules (the material must follow these; flag any breach)
1. **Public persona only.** No private-life information about the performers: family, pets, home, health, daily
   routine, sleep, breaks or hiatuses and their reasons, travel, where they stream from. A stream title that mentions
   such a thing is still out of scope.
2. **Every important fact needs a source** (official hololive / COVER pages first: hololive.hololivepro.com profiles,
   music pages, news; then archived stream titles; then reputable news). Unverified items must be labelled as such.
   Fan wikis are secondary at best. Recent evidence outweighs old.
3. **Quoted speech from streams** may be quoted only where both speech-recognition models agree (see the audio-check
   reports in the materials: a "Partial (computed)" verdict approves only the quoted shared run; "Agrees (spelling)"
   approves the whole line; "Not confirmed" approves nothing). Written lines (official profile, the member's own
   titles or descriptions) may be quoted when labelled as written or official.
4. **Japanese members' spoken lines** are written in Japanese, with a romanization and an English gloss.
5. **Performance sheets** describe an original designed voice for ElevenLabs; they must never claim to imitate or
   clone the real member. Pitch and pace figures are research context, not targets.
6. The `## [SW] ...` sections are what Sudowrite receives; the rest of each dossier is the research behind them.
   Role is always "Protagonist" by author decision.

## What to check, in priority order
1. Factual errors: dates, names, song titles and release dates, unit membership, who took part in a collab, status
   (active, graduated, affiliate). Verify against the cited sources where you can open them.
2. Claims the cited source does not support, or that generalize too far from it ("always," "every," "known for").
3. Scope or privacy breaches (rule 1).
4. Misattributed lines: a chat response presented as the member's line, a game character's line presented as hers,
   an English official translation presented as her own words.
5. Inconsistencies: a dossier versus its own [SW] fields; one card versus another card about the same event; a card
   versus its performance sheet.
6. Japanese text: wrong kana/kanji, wrong romanization, wrong or misleading English gloss.
7. Important omissions a novelist would need, but only if you can give a source.

## Scope of packet A
The seven character cards added in r02 (FLOW GLOW: Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya; hololive
GAMERS: Shirakami Fubuki, Ookami Mio, Inugami Korone), the FLOW GLOW and hololive GAMERS world cards, their seven
ElevenLabs performance sheets, the two audio-check reports and Claude's two self-check audits. Outfit descriptions are
checked image by image in packet B; here, check that the dossier and its Physical Description agree.
Useful official starting points: https://hololive.hololivepro.com/en/talents/ (each member's page has a profile, data,
a gallery and, for Fubuki, a Q&A), https://hololive.hololivepro.com/en/music/ (release dates), and the official FLOW
GLOW page https://hololive.hololivepro.com/special/13902/.


## Do not
- Rewrite style or restructure the files; suggest the smallest fix.
- Add facts without a source, or private details of any kind.
- Treat a fan wiki or a clip channel as official.
- Mark something wrong only because you cannot open its source; list it under "Could not verify" instead.

## Reply format (please follow exactly; Claude will merge it mechanically)
First line, exactly one of: `VERDICT: APPROVE` or `VERDICT: CHANGES`.

Then a Markdown table, one row per finding, most severe first:

| # | File | Section or field | Exact text (copy it) | Problem | Evidence (URL, or why) | Severity | Proposed fix |
|---|---|---|---|---|---|---|---|

Severity: **P0** = wrong or out of scope, must fix; **P1** = unsupported, misleading or inconsistent, should fix;
**P2** = suggestion. Then a section `## Could not verify` (claims you could not confirm or refute, with what you
tried), and `## Notes` (anything else, briefly). Reply in English; keep Japanese quotes as they are.

## Materials

### FILE: `bible/characters/Isaki-Riona.md`

````markdown
---
kind: character
name: "Isaki Riona"
sw_section: Characters
---

# Character File: Isaki Riona

> Scope: official lore and publicly shown persona only, checked 2026-11-27. Riona is an active hololive member
> (FLOW GLOW's leader; she debuted through hololive DEV_IS, which COVER restructured in a 2026-09-07 announcement,
> so DEV_IS is not listed as a current separate affiliation) at the 2026-09-30 baseline; added to the cast by
> author order (2026-11-27: complete all FLOW GLOW members). Her recent streams (2026) set her default manner, per
> the project's recency rule. Nothing about the performer behind the avatar: private-life information (family,
> home, health, daily routine, sleep, outings, where she streams from and the like) is outside scope and is not
> recorded here, including what she mentions in chats and stream titles. She streams in Japanese. In stories she
> knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title, description or post; "(secondary)" means the wording comes from a news
>   report or another secondary source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; RI20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (RI#) are listed under Sources.
>
> **Audio status:** on 2026-11-27 Claude checked two archived October 2026 morning game streams (RI20,
> research/audio-check/flowglow.md). Personal remarks are not quoted or summarized here. The audio was
> machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
"I'll do what I like and live how I want to!" (official English profile wording): FLOW GLOW's leader, a stoic,
fiercely competitive girl who keeps a poker face so nobody looks down on her but melts for small animals and loves
shonen manga; on stream she is loud, quick to laugh and openly delighted, and her channel welcomes viewers home
with 「おかえりおな〜！」. [Official RI1, RI2] [RI4 descriptions] [ASR RI20]

## Core Drive
- **Want:** to live by expressing herself (「表現することで生きていきたい！」, "I want to live by expressing
  myself!", her channel description) and to do what she likes in her own way (official line); she lists singing,
  dance and rap as what she loves. [Official RI1] [RI4 descriptions]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** she hates losing (official); she bills herself as weak at horror and plays it
  anyway (a "horror-weak duo" 3D VR Phasmophobia stream, 2026-03-19). [Official RI1] [RI4 tVW9fz36RLk]
- **Values shown in public:** her fans, the Isaki Union; her unit; her senpai, Calli above all. [RI4] [ASR RI20]

## Core Contradiction
A leader who works at looking tough and cool so nobody underestimates her, yet melts for small animals, gushes
about "my beloved Calli-senpai," and asks her chat to soften any prickly comment by adding 「好きだよ」 ("I love
you"). [Official RI1] [RI4]

## Behavioral Traits
1. Treats her channel as home: her descriptions open 「おかえりおな〜！🏠」 (okaeri-ona, "welcome home" fused with
   her name), invite viewers to 「ちょっと我が家でゆっくりしていくんだよ！♡」 ("stay a while at my place!") and add
   「今日もお疲れ様！人間生活頑張ってるね！？」 ("Good work today! Doing your best at being human?!"); she also says
   the welcome aloud at the start of a stream (one ASR model heard it). [RI4 descriptions] [ASR RI20, one model]
2. A channel glossary in her descriptions: commenters who use prickly words are asked to add 「好きだよ」 at the
   end; 「デモス」 means 「でも、好きだよ」 ("but I love you"), and 「お控えなすってごめんなさい」 is her polite "please
   don't." [RI4 descriptions]
3. Opens with a formal request, 「それでは挨拶をさせてください」 ("Allow me to greet you"), then a rap-style intro
   with an English "in da house" and her title as FLOW GLOW's leader. [ASR RI20]
4. Morning game streams in 2026 (#ホロドリ): she cheers, screams with joy when a rare card drops and ticks off
   senpai cards by name; before she leaves she cheers her viewers on for their day. [ASR RI20] [RI4 titles]
5. Signs off with "bye-bye" and a coined "otsu-Riona"; her ending video then parodies a calm mindfulness guide that
   walks the viewer through breathing before telling them to post with the fans' hashtag, subscribe and comment.
   [ASR RI20]
6. Calli: 「大好きなカリオペ先輩」 ("my beloved Calli-senpai") in her stream titles. [RI4]
7. Her first solo single, "Ring my name" (2026-05-30), became a dance short shared by many senpai. [Official RI3]
   [RI4, RI5]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: "I'll do what I like and live how I want to!" / 「やりたいように、私は私らしく生き抜いていくんです！」
    [Official RI1, RI2]
  - Welcome: 「おかえりおな〜！」 (okaeri-ona; written in her descriptions; heard spoken by the second model only).
    [RI4] [ASR RI20]
  - Opening: 「それでは挨拶をさせてください」 (shared span, 2026-10-15), then "in da house" and "FLOW GLOW's leader,
    Isaki Riona." [ASR RI20]
  - Sign-off: 「バイバーイ！」; "otsu-Riona" (おつりおな; both models heard a near-match, so it is not quoted as a
    verified line); in morning streams 「みんなも今日一日頑張ってね」「応援してるよ」 ("you all do your best today too";
    "I'm rooting for you"; shared spans, 2026-10-15). [ASR RI20]
- **Catchphrases & bits:** 「デモス」 / 「好きだよ」 (glossary); 「大好きなカリオペ先輩」; the Isaki Union (響咲連合)
  for her fans; #リオNOW (streams), #リオナート (fan art); fan mark 🎤👑. [Official RI1] [RI4]
- **Vocabulary / fillers:** 「よし」, 「OK」, 「えーっとね」, 「めっちゃ」, 「マジ」, long rising 「やったぁぁ」 and
  「かわいいぃぃ」 (first-model observations); a few casual forms such as 「いくで」 appear; no regional accent is
  assigned. [ASR RI20]
- **Profanity:** none observed in the windows checked.
- **Language:** streams in Japanese with English flourishes ("in da house," "OK").
- **Laughs, noises:** squeals and joyful screams at a lucky pull (first-model observation); laughter is a design
  choice.
- **Rhythm & rhetoric:** quick, bright chatter, polite set phrases at the start and end, explosive celebration in
  between. [ASR RI20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (RI20): in two 2026 morning game streams (game audio present), median about 256–273 Hz (p10–p90 about
    184–458 Hz) and about 276–327 characters a minute of speech. Measurements describe the archived audio, not a
    target to clone.
  - Provisional (interpretation): a clear, bright mid-high voice with a confident, slightly cool edge that breaks
    into gleeful shouting.
- **Sounds off:** a timid, breathy whisper as her default; a cold voice that never warms; slow, drowsy delivery.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Formal, then hype | 「それでは挨拶をさせてください」 (ASR RI20) |
| A rare pull | Ecstatic, shouting | **Style demo:** 「きたきたきた！やったぁぁ！」 |
| Losing | Frustrated, competitive | **Style demo:** 「悔しい！もう一回！」 ("So frustrating! One more!") |
| Cheering viewers off | Warm, encouraging | 「みんなも今日一日頑張ってね」 (ASR RI20) |
| With Calli | Adoring, excited | **Style demo:** 「カリオペ先輩、大好きです！」 |

### Sample Lines
1. "I'll do what I like and live how I want to!" (Official RI1)
2. 「それでは挨拶をさせてください」 (soredewa aisatsu o sasete kudasai, "Allow me to greet you") (ASR RI20, October 2026)
3. 「みんなも今日一日頑張ってね」「応援してるよ」 ("You all do your best today too." "I'm rooting for you.") (ASR RI20)

## Appearance Anchors (avatar)
160 cm; illustrator Shirabii (しらび). Long silver-grey hair and crimson eyes. Emoji 🎤👑. The official profile
gallery (checked 2026-11-27) shows three outfits; descriptions are Claude's reading of those images:
- **Original outfit (debut, 2024-11):** hair in a high side ponytail tied with a black ribbon; a cropped black
  jacket with red lining worn off the shoulders; a white cropped top with chain details and a black choker; a black
  belt; black-and-white panelled flared trousers with knee cutouts; black lace-up boots with white toes; a pink
  microphone topped with a small crown. [Official RI1 gallery 01_a, 02]
- **Black-and-pink stage outfit:** twin tails tied with pink ribbons and a tiny black crown; a black-and-magenta
  corset top with chains and detached sleeves; a black pleated skirt layered with pink and white and a long pink
  sash; one fishnet leg with a ribbon garter and one striped sock; chunky black boots trimmed with pink fur.
  [Official RI1 gallery 01_b]
- **New Year outfit (revealed 2026-01-02, her first):** a pale-pink floral kimono-style dress that falls in
  ruffled tiers, with a big pink bow at the waist; hair braided into a side ponytail with a cream bow; white
  lace-up boots. The gallery image matches the silhouette in the reveal stream's thumbnail. [Official RI1 gallery
  03] [RI4 HTHdI209UXU]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2024-11-09 | Debut (first in the FLOW GLOW relay) through hololive DEV_IS; "FG ROADSTER" | [Official RI1, RI3; S4 on the FLOW GLOW card] |
| 2024-11 to 12 | ちーむ変態ジェントルマン with Chihaya and Niko (Chained Together; a first off-collab); "Gimme×Gimme" with Niko (2024-12-03) | [RI4 i25b--m63UU, DBN-VVm-pRs, y-nFLZtmLQ4] |
| 2025 | Gang Beasts with Nene, Lamy and Chihaya (01-20); a watch-along of Calli's live (02-27); Minecraft with Lui (03-17); MYRIAD DEATH as Calli (04-11); holoRUST with Koyori (04-28); "あの夏が飽和する" with Niko (10-23) | [RI4] [RI5] |
| 2025-11-23 | FLOW GLOW's 3D debut live, "MAKE IT, BREAK IT" | [FLOW GLOW card S6] |
| 2026-01-02 | First New Year outfit | [RI4 HTHdI209UXU] |
| 2026-02-03 | Self-3D karaoke with AZKi, Koyori and Niko (#せくちー3Dカラオケ) | [RI5 1HQL3WJPBHA] |
| 2026-03-07 | FLOW GLOW's festival debut, hololive 7th fes. STAGE3 | [FLOW GLOW card S8] |
| 2026-05-27 | A 3D birthday stream with guests (Super Mario Party Jamboree) | [RI4 CO2OhYWst5g] |
| 2026-05-30 | First solo single, "Ring my name"; dance shorts by Calli, Nerissa, AZKi, Bijou, Botan, and with IRyS, Pekora and Towa on her channel (06–07) | [Official RI3] [RI4] [RI5] |
| 2026-06-07 | RoARiS (Roboco, AZKi, Su, Riona) play Momotetsu 2 | [RI4 jG-EPYQ4V9g] |
| 2026-07 | Guest at AZKi's 2026 birthday 3D live ("星座になれたら") | [RI5 M1mZrusy-xY] |
| 2026-09-12 | Clubhouse Games with Calli on Riona's channel | [RI4 hhOim_G0kns] |
| 2026-11-24 | Second solo single, "Reverberate" | [Official RI3] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Kikirara Vivi, Koganei Niko, Mizumiya Su, Rindo Chihaya | Unitmates; Riona is the leader | Group songs, the 3D live, the 2026 album | [Official] [RI4] |
| Koganei Niko | Duet partner | "Gimme×Gimme" (2024), "あの夏が飽和する" (2025), "逆様" (official listing); ちーむ変態ジェントルマン with Chihaya | [RI4] [RI5] [Official listing] |
| Rindo Chihaya | Unitmate | ちーむ変態ジェントルマン; Gang Beasts with Lamy and Nene (2025) | [RI4] [RI5] |
| Mizumiya Su | Unitmate | RoARiS with Roboco and AZKi (2026); both guests at AZKi's 2026 birthday live | [RI4] [RI5] |
| Mori Calliope | Her "beloved Calli-senpai" | Clubhouse Games (2026-09-12); MYRIAD DEATH played as Calli (2025); a watch-along of Calli's live (2025); "Ring my name" dance shorts on both channels (2026) | [RI4] [RI5 rAR9fgHBKwI] |
| IRyS | Senpai | A "Ring my name" dance short together (2026-07-22) | [RI4 uLvilDwP6HE] |
| Nerissa Ravencroft, Koseki Bijou | Senpai | Danced "Ring my name" in their own shorts (2026) | [RI5] |
| AZKi | Senpai | RoARiS (Momotetsu 2, 2026); the 2026 self-3D karaoke; a guest song at AZKi's 2026 birthday live; a dance short together (2026-07-15) | [RI4] [RI5] |
| Hakui Koyori | Senpai | holoRUST together (2025); the 2026 self-3D karaoke | [RI4] [RI5] |
| Takane Lui | Senpai | Minecraft gold/zombie-piglin trap (2025-03-17, on both channels) | [RI4] [RI5 pB3e3SzBjJ8] |
| Yukihana Lamy | Senpai | Gang Beasts with Nene and Chihaya (2025-01-20) | [RI5 EsfZ7Ny4aPA] |
| Houshou Marine, Shishiro Botan | Senpai | Riona danced Marine's song in a short (2025-12-14); Botan danced "Ring my name" (2026) | [RI4] [RI5] |
| Inugami Korone, Shirakami Fubuki (GAMERS) | Senpai | #ころリオ first collab and off-collab with Korone (2025-01-22); a Mario Party with Fubuki, Niko and Polka (2026, Niko's channel); #フブミオ大予想, FLOW GLOW's profiles predicted by Fubuki and Mio (2024-11-09) | [Korone channel QaGy1nHjRIQ, sze_5XnmD9w] [RI5 cWjY92rdma4] [Fubuki channel iJpIGu5HuGY] |

## Arc
- **Starting point:** active at the 2026 baseline, two years in: FLOW GLOW's leader with a festival debut, two solo
  singles and a song that her senpai danced to.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a competition she refuses to lose; a cool front that cracks the moment something small and
  fluffy appears; leading the unit somewhere she has not checked the route to.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Riona challenges Calli to a rematch of a Clubhouse Games mini-game and practises in secret.
  2. A stray kitten at NOW RAWDING wrecks Riona's poker face in front of the whole unit.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2024-11-09 through hololive DEV_IS; FLOW GLOW (leader); birthday 29 May; 160 cm; illustrator Shirabii;
  fans Isaki Union (響咲連合); tags #リオNOW, #リオナート; emoji 🎤👑.

## Sources (checked 2026-11-27)
- RI1 Official profile (text, data and gallery): https://hololive.hololivepro.com/en/talents/isaki-riona/
- RI2 Official FLOW GLOW page (Japanese profile and tagline): https://hololive.hololivepro.com/special/13902/
- RI3 Official music: https://hololive.hololivepro.com/en/music/756/ ("Ring my name," 2026-05-30), …/851/
  ("Reverberate," 2026-11-24), …/495/ ("FG ROADSTER"), …/024/ (album "FLOW GLOW")
- RI4 Her channel's archive metadata (archive.ragtag.moe; titles and the description template): WJz-YOx6fsE and
  uH9AFj1qbyA (descriptions; October 2026 streams), HTHdI209UXU (New Year outfit), CO2OhYWst5g (3D birthday),
  tVW9fz36RLk (Phasmophobia), hhOim_G0kns, LRSvK1ePA8o, 4Zb0JEy3bw4 and IAom9MDoVxs (Calli), uLvilDwP6HE (IRyS),
  zdUzvl-Tz50 (AZKi), PA4F02G7AjM (Pekora), KeNc8WhPiQU (Towa), tPJslEdszIQ (Marine's song), jG-EPYQ4V9g (RoARiS),
  l50dJY8DxqM (Koyori), vk-xMnnHkbE (Lui), i25b--m63UU, DBN-VVm-pRs and JBGGZ7tNe4E (with Chihaya and Niko),
  y-nFLZtmLQ4 ("Gimme×Gimme")
- RI5 Other channels' archive metadata: 1HQL3WJPBHA (Koyori's 3D karaoke), rAR9fgHBKwI (Calli), Ts1v3xM-YG8
  (Nerissa), 83cZEqTVdOQ and M1mZrusy-xY (AZKi), mTSUnQ-0h1E (Bijou), z6V93vfXrWk (Botan), pB3e3SzBjJ8 (Lui),
  EsfZ7Ny4aPA (Lamy), h32hZjqOHGk ("あの夏が飽和する," Niko's channel), cWjY92rdma4 (a Mario Party with Fubuki,
  Polka and Niko, Niko's channel)
- RI20 Claude's audio check (two-model ASR, Japanese): research/audio-check/flowglow.md
- Official video listing on her profile: xMRwvFGy8Q4 ("逆様," with Niko)

## [SW] Name
Isaki Riona

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, FLOW GLOW

## [SW] Other Names
Riona, 響咲リオナ

## [SW] Personality
Her official profile presents Riona as FLOW GLOW's leader: extremely stoic and a sore loser who keeps a poker face so nobody looks down on her, but whose heart melts for small animals, and a shonen-manga fan far more hot-blooded than her cool look suggests. She says she wants to live by expressing herself, and she loves singing, dance and rap. On stream she is loud, quick to laugh and openly delighted: she screams with joy at a lucky pull, ticks off her favourite senpai by name and cheers her viewers on before she leaves. She treats her channel as home and welcomes viewers back to it, and she asks commenters to soften any prickly remark by adding "I love you." She is an unabashed fan of her senpai, above all Mori Calliope, her "beloved Calli-senpai." She calls herself weak at horror and plays it anyway. Her fans are the Isaki Union.

## [SW] Background
Riona is an active member of FLOW GLOW. She has no supernatural abilities; her lore is a performed persona. She debuted on 2024-11-09 through hololive DEV_IS as the leader of FLOW GLOW, with Koganei Niko, Mizumiya Su, Rindo Chihaya and Kikirara Vivi; the debut song "FG ROADSTER" gives each of them a rap verse. FLOW GLOW held its 3D debut live, "MAKE IT, BREAK IT," on 2025-11-23, released the album "FLOW GLOW" on 2026-01-21 and made its festival debut at hololive 7th fes. on 2026-03-07. Riona revealed her first New Year outfit on 2026-01-02, celebrated her birthday in 3D with guests in May 2026 and released her first solo single, "Ring my name," on 2026-05-30; Mori Calliope, Nerissa Ravencroft, IRyS, Koseki Bijou and AZKi danced to it in shorts. She sang as a guest at AZKi's 2026 birthday live, and her second solo single, "Reverberate," followed on 2026-11-24.

## [SW] Physical Description
Riona's avatar is 160 cm tall, with long silver-grey hair and crimson eyes. Original outfit: a high side ponytail tied with a black ribbon, a cropped black jacket with red lining worn off the shoulders over a white crop top with chains and a black choker, black-and-white panelled flared trousers with knee cutouts, black lace-up boots and a pink microphone topped with a small crown. Stage outfit: twin tails with pink ribbons and a tiny black crown, a black-and-magenta corset top with chains and detached sleeves, a layered black-and-pink pleated skirt with a long pink sash, one fishnet leg and one striped sock, and chunky black boots trimmed with pink fur. New Year outfit (2026): a pale-pink floral kimono-style dress in ruffled tiers with a big pink bow at the waist, her hair braided into a side ponytail with a cream bow, and white lace-up boots.

## [SW] Dialogue Style
Streams in Japanese: bright, fast and openly excited, with polite set phrases at the edges. She opens with 「それでは挨拶をさせてください」 ("Allow me to greet you") and a rap-style "in da house" intro, celebrates a lucky pull at full volume, and sends viewers off with 「みんなも今日一日頑張ってね」 ("you all do your best today too"). English flourishes ("OK," "in da house") pepper her speech; no regional accent is assigned. When a story renders her speech in English or Chinese, keep the cool-leader front that keeps cracking into loud, warm enthusiasm.

## [SW] Catchphrases
"I'll do what I like and live how I want to!" (official English; 「やりたいように、私は私らしく生き抜いていくんです！」); 「おかえりおな〜！」 ("Okaeri-ona~!", "welcome home," her channel welcome); 「それでは挨拶をさせてください」 ("Allow me to greet you"); 「バイバーイ！」 and "otsu-Riona" to sign off; 「デモス」 ("demosu," short for 「でも、好きだよ」, "but I love you," her channel's softener for prickly comments); 「大好きなカリオペ先輩」 ("my beloved Calli-senpai"); "Isaki Union" (響咲連合, her fans).

## [SW] Voice & Delivery
Direction for an original designed voice: a clear, bright mid-high voice with a confident, slightly cool edge; brisk and polite in her set phrases, exploding into gleeful shouts and squeals when something goes her way, frustrated and fiery when she loses, warm when she cheers her viewers on. Not as default: timid, breathy, drowsy or coldly flat.

## [SW] Audio Tags
Dialogue language for audio scripts: Japanese. Write her spoken turns in Japanese script; romaji and English go only on ROMAJI/GLOSS lines. ElevenLabs v4 performance directions for an original designed voice; never imitate the real member. Register: clear, bright mid-high voice with a confident edge. Default tags: [bright, energetic]. By situation: opening [formal, upbeat]; a lucky pull [ecstatic, shouting]; losing [frustrated]; horror [scared]; cheering viewers [warm, encouraging]; leading the unit [confident]. With people: Calli [adoring, excited]; Niko [playful]; Chihaya [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [squeals] (tag only); [laughs] (tag only). Keep in the words: 「おかえりおな」 (okaeri-ona), 「響咲連合」 (Isaki Union), 「好きだよ」 (suki da yo). Reading: いさき りおな. No regional accent is assigned. Not as default: a timid whisper or a flat, cold read.

## [SW] Motivation
In her lore, Riona wants to do what she likes and live as herself, and to lead FLOW GLOW without ever being looked down on. As a streamer and singer, she wants to live by expressing herself through song, dance and rap.

## [SW] Relationships
FLOW GLOW (Koganei Niko, Mizumiya Su, Rindo Chihaya, Kikirara Vivi): her unit, which she leads. Koganei Niko: duets "Gimme×Gimme," "あの夏が飽和する" and "逆様"; with Rindo Chihaya they are the self-styled "team hentai gentlemen." Mizumiya Su: RoARiS with Roboco and AZKi (2026). Mori Calliope: her "beloved Calli-senpai"; Clubhouse Games together (2026), MYRIAD DEATH played as Calli and "Ring my name" dance shorts. IRyS: a "Ring my name" dance short together (2026). Nerissa Ravencroft and Koseki Bijou: danced "Ring my name." AZKi: RoARiS, a self-3D karaoke with Hakui Koyori and Niko (2026) and a guest song at AZKi's 2026 birthday live. Hakui Koyori: holoRUST (2025) and that karaoke. Takane Lui: Minecraft (2025). Yukihana Lamy: Gang Beasts (2025). Inugami Korone: #ころリオ, a first collab and an off-collab (2025). Shirakami Fubuki: a Mario Party with Niko and Omaru Polka (2026) and a pre-debut "delusion profile" stream about FLOW GLOW (2024).

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Voice & Delivery and Audio Tags are performance directions for an original designed voice. Timbre, laughter and
  delivery are design choices unless a listening source is named in the Voice Profile; ASR supports wording, not
  vocal quality or recurrence; partner tags are optional scene directions, not observed defaults; the kana reading
  is untested; recorded pitch and speaking-rate figures are research context only, never synthesis targets.
- 「おかえりおな〜！」, the glossary items and 「今日もお疲れ様！人間生活頑張ってるね！？」: her description template
  (written). 「おかえりおな」 spoken: the second ASR model only. 「それでは挨拶をさせてください」 and 「みんなも今日一日
  頑張ってね」: shared ASR spans. "otsu-Riona": both models heard a near-match (おちによな / オチリオナ), so the card
  gives it in romaji, not as a verified quotation.
- "逆様": the official video listing on her profile (undated here). The dance shorts: archived titles; a short
  published on a channel does not establish who performed the motion.
- Outfits: Claude's reading of the official gallery images; the New Year outfit's identification rests on the
  gallery image and the reveal-stream silhouette.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Korone (QaGy1nHjRIQ, sze_5XnmD9w), Fubuki (cWjY92rdma4, iJpIGu5HuGY).

## Merge Record
- **2026-11-27, Claude only (author order: complete all FLOW GLOW members):** official profile, gallery and music
  pages, the official FLOW GLOW page, archive metadata and a two-model ASR check (RI20). Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. The release date of "逆様" is not established here.
2. Her exact spoken opening after 「それでは挨拶をさせてください」 differs between the two ASR models beyond "in da
   house" and the FLOW GLOW leader title.
````

### FILE: `bible/characters/Koganei-Niko.md`

````markdown
---
kind: character
name: "Koganei Niko"
sw_section: Characters
---

# Character File: Koganei Niko

> Scope: official lore and publicly shown persona only, checked 2026-11-27. Niko is an active hololive member
> (FLOW GLOW; she debuted through hololive DEV_IS, which COVER restructured in a 2026-09-07 announcement, so DEV_IS
> is not listed as a current separate affiliation) at the 2026-09-30 baseline; added to the cast by author order
> (2026-11-27: complete all FLOW GLOW members). Her recent streams (2026) set her default manner, per the project's
> recency rule. Nothing about the performer behind the avatar: private-life information (family, home, health,
> daily routine, sleep, outings, where she streams from and the like) is outside scope and is not recorded here,
> including what she mentions in chats and stream titles. She streams in Japanese. In stories she knows she is a streamer with a persona (see the world card
> "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title, description or post; "(secondary)" means the wording comes from a news
>   report or another secondary source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; NK20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (NK#) are listed under Sources.
>
> **Audio status:** on 2026-11-27 Claude checked two archived 2026 episodes of her Saturday-morning talk show 朝ガオ
> (NK20, research/audio-check/flowglow.md). Personal remarks are not quoted or summarized here. The audio was
> machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
"If you can't bring yourself to a smile, just say my name!" (official English profile wording): FLOW GLOW's
jokester, a tall blonde "tiger" who would give anything to make people laugh, bulldozes through a bit or breaks
character if it ends in laughter, calls herself 「ニコたん」 and makes anime-style comedy shorts about her own
imagined life. [Official NK1, NK2] [NK4] [ASR NK20]

## Core Drive
- **Want:** to make people smile; officially she would give her whole life for it. [Official NK1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** weak against mornings and soft on animals (official), yet she hosts a
  Saturday-morning show. [Official NK1] [NK4]
- **Values shown in public:** laughter, her fans (Niko Stans), her unit. [Official NK1] [ASR NK20]

## Core Contradiction
A 172 cm streetwear "tiger" with orange shades who plays the clown on purpose: she will wreck her own cool image,
apologize at length in mock-formal Japanese, or narrate herself as a cartoon, as long as it gets a laugh.
[Official NK1] [NK4 titles] [ASR NK20]

## Behavioral Traits
1. Calls herself 「ニコたん」 (Nikotan), dozens of times a stream; the same sound, written 「ニコ担」, is her fans'
   name (Niko Stan). Debut title: 「ニコたんが来たァ!」 ("Nikotan's here!"). [ASR NK20] [Official NK1] [NK4 f7vPMO3NxLY]
2. Signs off with a call: 「それでは、ニコたんが帰宅でよろしくお願いします」 then 「ニコたんが〜、帰宅〜！」 ("Nikotan
   is going ho~me!") and 「バイバ〜イ」; both ASR models heard "kitaku" (written 来たく by both; 帰宅 is our reading).
   [ASR NK20]
3. Hosts 朝ガオ, a Saturday-morning talk show with a weekly talk theme (named 2026-06-06; vol.14 on 2026-09-12).
   [NK4 titles] [ASR NK20]
4. Makes anime-style comedy shorts (#ニコたんアニメ, #虎のいる生活; over a hundred since 2024-11), each labelled as
   her own fantasy and fiction. [NK4 titles and descriptions]
5. Apologizes in exaggerated formal Japanese when a bit goes wrong, then drops straight back into casual banter and
   「ほんまにごめん」 ("really sorry"). [ASR NK20]
6. Sings in LYRA's "III" with Calli, Elizabeth, Ayunda Risu and Amane Kanata, and in "Magia" with Calli and Nerissa
   (2026-08-28). [Credits on Calli's and Elizabeth's cards] [NK4 5ccqXCOshHc]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: "If you can't bring yourself to a smile, just say my name!" / 「笑えない時は、ニコたんの名を
    呼ぶがいいさ！」 [Official NK1, NK2]
  - Arrival: 「ニコたんが来たァ!」 (debut title) and 「ニコたん参上！」 ("Nikotan has arrived!", a 2025 title). [NK4]
  - Sign-off: 「それでは、ニコたんが帰宅でよろしくお願いします」 → 「ニコたんが〜、帰宅〜！」 → 「バイバ〜イ」
    (2026-08-08 and 2026-09-12). [ASR NK20]
- **Catchphrases & bits:** 「ニコたん」 for herself; 「ニコ担」 (Niko Stan) for her fans; #ニコたん配信中 (streams),
  #ニコたん描いたん (fan art); fan mark ☺️🐅. [Official NK1]
- **Vocabulary / fillers:** 「なんか」, 「マジで」, 「ほんま」, rough-affectionate retorts such as 「ちゃんとしろや」
  (first-model observations); no regional accent is assigned. [ASR NK20]
- **Profanity:** none observed in the windows checked.
- **Language:** streams in Japanese.
- **Laughs, noises:** big laughs and comic wails are design choices.
- **Rhythm & rhetoric:** fast, self-mocking patter that swings between mock-formal speeches and blunt casual
  speech. [ASR NK20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (NK20): in two 2026 morning talk shows (opening music in one window), median about 263–292 Hz
    (p10–p90 about 180–477 Hz) and about 281–376 characters a minute of speech. Measurements describe the archived
    audio, not a target to clone.
  - Provisional (interpretation): a relaxed, slightly husky mid-range voice that goes theatrical for a bit.
- **Sounds off:** a delicate, breathy voice; prim formality held for a whole scene; cold aloofness.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| A bit gone wrong | Mock-formal, theatrical | **Style demo:** 「誠に申し訳ございませんでした。」 ("I most humbly apologize.") |
| Casual banter | Loose, self-mocking | 「ほんまにごめん」 ("really sorry") (ASR NK20) |
| Signing off | Chant, playful | 「ニコたんが〜、帰宅〜！」 ("Nikotan is going ho~me!") (ASR NK20) |
| Horror (with Lui watching) | Panicked, loud | **Style demo:** 「ルイ先輩、無言にならないでぇ！」 |
| Thanking her fans | Warm | **Style demo:** 「ニコ担、いつもありがとね。」 |

### Sample Lines
1. "If you can't bring yourself to a smile, just say my name!" (Official NK1)
2. 「ニコたんが〜、帰宅〜！」 (Nikotan ga, kitaku!, "Nikotan is going ho~me!") (ASR NK20, 2026)

## Appearance Anchors (avatar)
172 cm; illustrator TETSUKAZU (鉄一). Long blonde hair with a black streak along the crown and green eyes. Emoji
☺️🐅. The official profile gallery (checked 2026-11-27) shows three outfits; descriptions are Claude's reading of
those images:
- **Original outfit (debut, 2024-11):** round orange-tinted glasses; an oversized dark-grey varsity jacket with
  beige sleeves, orange lining and embroidered tiger paws with green claws; a black crop top with a sheer mesh hem;
  light-grey ripped drawstring sweatpants; a long thin dark strap hanging behind her like a tail; patterned lace-up
  boots; rings on her fingers. [Official NK1 gallery 01_a, 02]
- **Tiger stage outfit:** a high blonde ponytail; a black zip-up crop top with orange-patterned mesh sleeves and
  long black gloves; a studded belt with a tiger-head buckle, chains and claw charms; a torn khaki wrap over flowing
  black trousers printed with orange tiger stripes and a tiger. [Official NK1 gallery 01_b]
- **Japanese-style outfit:** a short bob with two round buns like ears, sunglasses pushed up on her head; a black
  kimono-style robe embroidered with a tiger and waves, a beige tiger-striped shawl, a green jade pendant and chains;
  black platform boots. Its reveal stream is not in the archive checked. [Official NK1 gallery 03]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2024-11-09 | Debut (second in the FLOW GLOW relay) through hololive DEV_IS; "FG ROADSTER" | [Official NK1; FLOW GLOW card S4] |
| 2024-11 to 12 | #ニコたんアニメ shorts begin (11-12); #にこすぅ with Su (11-24); ちーむ変態ジェントルマン with Chihaya and Riona; "Gimme×Gimme" with Riona (12-03); #にこらみ晩酌, an off-collab with Lamy (12-22) | [NK4] [NK5] |
| 2025 | Chained Together practice with Usada Pekora ("兎虎兎虎," 01-10); Minecraft with Lui (03-02); Shadow Corridor with Lui watching (04-05, 04-19); holoRUST on "Team AZKi" (05-02); ELDEN RING NIGHTREIGN with Ichijou Ririka and Chihaya (06); "ポケットにファンタジー" with Su (06-29); "あの夏が飽和する" with Riona (10-23) | [NK4] |
| 2025-11-23 | FLOW GLOW's 3D debut live | [FLOW GLOW card S6] |
| 2026-02-03 | Self-3D karaoke with AZKi, Koyori and Riona | [NK5 1HQL3WJPBHA] |
| 2026-02-05 | A 3D stream with guests for "Niko Day" (2/5, read ni-ko) | [NK4 ixSOcbeAEh0] |
| 2026-03-07 | FLOW GLOW's festival debut, hololive 7th fes. STAGE3 | [FLOW GLOW card S8] |
| 2026-06-06 | Her morning show is named 朝ガオ; a Mario Party with Shirakami Fubuki, Omaru Polka and Riona | [NK4 I1ktduXA5uw, cWjY92rdma4] |
| 2026-07-26 | First solo single, "星炎" (Seien) | [Official NK3] |
| 2026-08-28 | "Magia" with Calli and Nerissa | [NK4 5ccqXCOshHc] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Isaki Riona, Mizumiya Su, Rindo Chihaya, Kikirara Vivi | Unitmates | Group songs, the 3D live, the 2026 album | [Official] |
| Isaki Riona | Duet partner | "Gimme×Gimme," "あの夏が飽和する," "逆様"; ちーむ変態ジェントルマン with Chihaya; the 2026 3D karaoke | [NK4] [NK5] |
| Mizumiya Su | Unitmate | #にこすぅ (Keep Talking and Nobody Explodes, 2024); "ポケットにファンタジー" (2025) | [NK4] |
| Rindo Chihaya | Unitmate | ELDEN RING NIGHTREIGN with Ichijou Ririka (2025); ちーむ変態ジェントルマン | [NK4] |
| Kikirara Vivi | Unitmate | SuperBunnyMan (#ヴィヴィガー, 2024); Minecraft (2025) | [NK4] [Vivi's channel hcwGC_8aT04] |
| Mori Calliope | Senpai | LYRA's "III" (with Elizabeth, Risu and Kanata); "Magia" with Nerissa (2026) | [Calli card] [NK4] |
| Elizabeth Rose Bloodflame | Senpai | LYRA's "III" | [Elizabeth card] |
| Nerissa Ravencroft | Senpai | "Magia" with Calli (2026-08-28) | [NK4] |
| Takane Lui | Senpai | Minecraft (2025-03-02, on both channels); Lui watched over her Shadow Corridor runs (2025-04); shorts on Lui's channel about Niko (2025) | [NK4] [NK5 IvzEZcBdmNk, oT0bf4SP4vk] |
| AZKi | Senpai | holoRUST on "Team AZKi" (2025); the 2026 3D karaoke | [NK4] [NK5] |
| Hakui Koyori | Senpai | The 2026 self-3D karaoke | [NK5] |
| Yukihana Lamy | Senpai | #にこらみ晩酌, an off-collab drinking stream on Lamy's channel (2024-12-22) | [NK5 Ig_Ba2h9DZc] |
| Shirakami Fubuki (GAMERS) | Senpai | Phasmophobia with Chihaya and Polka on Fubuki's channel (2025-04-20); FLOW GLOW's profiles predicted by Fubuki and Mio before the debut (2024-11-09) | [Fubuki channel yVdTbPCJytw, iJpIGu5HuGY] |

## Arc
- **Starting point:** active at the 2026 baseline: FLOW GLOW's jokester with a morning show, a solo single and a
  long-running series of comedy shorts.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a bit she will not abandon even when it is clearly failing; a fake anime trailer about her
  friends; a morning show that goes off the rails.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Niko turns the unit's road trip into a #ニコたんアニメ episode and casts everyone without asking.
  2. Lui "supervises" Niko through a horror game and refuses to say a word.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2024-11-09 through hololive DEV_IS; FLOW GLOW (jokester); birthday 25 July; 172 cm; illustrator
  TETSUKAZU; fans Niko Stan (ニコ担); tags #ニコたん配信中, #ニコたん描いたん; emoji ☺️🐅.

## Sources (checked 2026-11-27)
- NK1 Official profile (text, data and gallery): https://hololive.hololivepro.com/en/talents/koganei-niko/
- NK2 Official FLOW GLOW page (Japanese profile and tagline): https://hololive.hololivepro.com/special/13902/
- NK3 Official music: https://hololive.hololivepro.com/en/music/781/ ("星炎"/"Seien," 2026-07-26)
- NK4 Her channel's archive metadata (archive.ragtag.moe): f7vPMO3NxLY (debut), 7UaG-JGAdIs ("ニコたん参上！"),
  I1ktduXA5uw, TywtWkIafGw, eQI6BwAzBxY, 7NOhe2tKZLA and MmkPfYSIJ0s (朝ガオ), #ニコたんアニメ titles from 2024-11-12,
  gHLbsdnSxjQ (Pekora), sQus1Fyzb9w, hlb4XXjpf4M and Rz4XltKC8RY (Lui), h8KKOCakmGY (ELDEN RING NIGHTREIGN),
  QCMtwotxvxY ("ポケットにファンタジー"), h32hZjqOHGk ("あの夏が飽和する"), ixSOcbeAEh0 (Niko Day 3D), cWjY92rdma4 (Mario
  Party), vcls9KWmwLo ("星炎"), 5ccqXCOshHc ("Magia")
- NK5 Other channels' archive metadata: 1HQL3WJPBHA (Koyori's 3D karaoke), IvzEZcBdmNk and oT0bf4SP4vk (Lui),
  Ig_Ba2h9DZc (Lamy), y-nFLZtmLQ4 ("Gimme×Gimme," Riona's channel), i25b--m63UU (Chihaya and Riona)
- NK20 Claude's audio check (two-model ASR, Japanese): research/audio-check/flowglow.md
- Official video listing on her profile: xMRwvFGy8Q4 ("逆様," with Riona)

## [SW] Name
Koganei Niko

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, FLOW GLOW, LYRA

## [SW] Other Names
Niko, Nikotan, 虎金妃笑虎, ニコたん

## [SW] Personality
Her official profile presents Niko as FLOW GLOW's jokester: so passionate about making people smile that she would give her whole life to it, and happy to bulldoze through a bit or break character as long as it ends in laughter. She is weak against mornings and soft on animals, yet hosts a Saturday-morning talk show. On stream she calls herself "Nikotan," swings from long mock-formal apologies to blunt, casual banter, laughs at herself first, and turns her own imagined life into anime-style comedy shorts that she labels as pure fantasy. She is warm with her fans, the Niko Stans, and with her unit, and loud and helpless in horror games when a senpai is watching.

## [SW] Background
Niko is an active member of FLOW GLOW. She has no supernatural abilities; her lore is a performed persona. She debuted on 2024-11-09 through hololive DEV_IS as FLOW GLOW's jokester, with Isaki Riona, Mizumiya Su, Rindo Chihaya and Kikirara Vivi. Since 2024-11 she has posted over a hundred anime-style comedy shorts. FLOW GLOW held its 3D debut live on 2025-11-23, released its first album on 2026-01-21 and made its festival debut at hololive 7th fes. on 2026-03-07. Niko held a 3D "Niko Day" stream on 2026-02-05, named her Saturday-morning talk show 朝ガオ in June 2026 and released her first solo single, "星炎" (Seien), on 2026-07-26. She sang LYRA's "III" with Mori Calliope, Elizabeth Rose Bloodflame, Ayunda Risu and Amane Kanata, and "Magia" with Calli and Nerissa Ravencroft (2026-08-28).

## [SW] Physical Description
Niko's avatar is 172 cm tall, with long blonde hair with a black streak along the crown and green eyes. Original outfit: round orange-tinted glasses, an oversized dark-grey varsity jacket with beige sleeves, orange lining and embroidered tiger paws with green claws, a black crop top with a sheer mesh hem, light-grey ripped drawstring sweatpants, a long thin dark strap hanging behind her like a tail and patterned lace-up boots. Tiger stage outfit: a high ponytail, a black zip-up crop top with orange-patterned mesh sleeves and long black gloves, a studded tiger-head belt with chains and claw charms, and a torn khaki wrap over flowing black trousers printed with orange tiger stripes. Japanese-style outfit: a short bob with two round buns like ears and sunglasses pushed up, a black kimono-style robe embroidered with a tiger and waves, a beige tiger-striped shawl, a green jade pendant and black platform boots.

## [SW] Dialogue Style
Streams in Japanese: loose, fast and self-mocking, calling herself 「ニコたん」. She switches without warning between exaggerated formal apologies and blunt casual speech (「ほんまにごめん」, "really sorry"), throws herself into a bit and signs off with a chant, 「ニコたんが〜、帰宅〜！」 ("Nikotan is going ho~me!"). No regional accent is assigned. When a story renders her speech in English or Chinese, keep the comedian's timing, the third-person "Nikotan" and the sudden drops from pomp to bluntness.

## [SW] Catchphrases
"If you can't bring yourself to a smile, just say my name!" (official English; 「笑えない時は、ニコたんの名を呼ぶがいいさ！」); 「ニコたんが来たァ!」 ("Nikotan's here!") and 「ニコたん参上！」 ("Nikotan has arrived!"); 「それでは、ニコたんが帰宅でよろしくお願いします」 then 「ニコたんが〜、帰宅〜！」 ("Nikotan is going ho~me!") and 「バイバ〜イ」 to sign off; 「ニコたん」 (herself); 「ニコ担」 ("Niko Stan," her fans, said the same way as her nickname).

## [SW] Voice & Delivery
Direction for an original designed voice: a relaxed, slightly husky mid-range voice built for comedy; deadpan-to-theatrical swings, pompous when she apologizes, blunt and quick in banter, loud and panicky in horror, warm with her fans. Not as default: a delicate breathy voice, sustained prim formality or cold aloofness.

## [SW] Audio Tags
Dialogue language for audio scripts: Japanese. Write her spoken turns in Japanese script; romaji and English go only on ROMAJI/GLOSS lines. ElevenLabs v4 performance directions for an original designed voice; never imitate the real member. Register: relaxed, slightly husky mid-range voice. Default tags: [playful, casual]. By situation: a bit gone wrong [mock-formal, theatrical]; banter [deadpan]; signing off [chanting, cheerful]; horror [panicked]; thanking her fans [warm]; a morning show [groggy, upbeat]. With people: Riona [teasing]; Lui [whiny, pleading]; Su [goofy]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs] (tag only); [wails] (tag only). Keep in the words: 「ニコたん」 (Nikotan), 「ニコ担」 (Niko Stan), 「帰宅」 (kitaku). Reading: こがねい にこ. No regional accent is assigned. Not as default: a breathy, delicate or coldly aloof read.

## [SW] Motivation
In her lore, Niko wants to make everyone smile, whatever it costs her dignity. As a streamer and singer, she wants her shows, songs and comedy shorts to give her fans a laugh when they need one.

## [SW] Relationships
FLOW GLOW (Isaki Riona, Mizumiya Su, Rindo Chihaya, Kikirara Vivi): her unit. Isaki Riona: duets "Gimme×Gimme," "あの夏が飽和する" and "逆様"; with Rindo Chihaya they are the self-styled "team hentai gentlemen." Mizumiya Su: #にこすぅ and "ポケットにファンタジー." Chihaya: ELDEN RING NIGHTREIGN with Ichijou Ririka (2025). Kikirara Vivi: SuperBunnyMan and Minecraft. Mori Calliope and Elizabeth Rose Bloodflame: fellow LYRA vocalists on "III" (with Ayunda Risu and Amane Kanata). Calli and Nerissa Ravencroft: "Magia" (2026). Takane Lui: Minecraft and horror runs Lui supervised (2025). AZKi: holoRUST's "Team AZKi" and a self-3D karaoke with Hakui Koyori and Riona (2026). Yukihana Lamy: an off-collab drinking stream (2024). Shirakami Fubuki: Phasmophobia with Chihaya and Omaru Polka (2025) and a Mario Party with Polka and Riona (2026).

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Voice & Delivery and Audio Tags are performance directions for an original designed voice. Timbre, laughter and
  delivery are design choices unless a listening source is named in the Voice Profile; ASR supports wording, not
  vocal quality or recurrence; partner tags are optional scene directions, not observed defaults; the kana reading
  is untested; recorded pitch and speaking-rate figures are research context only, never synthesis targets.
- Sign-off: both ASR models heard 「ニコたんが…来たく」 in two episodes (2026-08-08, 2026-09-12); the card writes
  帰宅 (kitaku, "going home") as our reading of the sound. 「ほんまにごめん」: shared span. 「ニコたんが来たァ!」 and
  「ニコたん参上！」: archived titles (written).
- "LYRA": the mix engineer's credits (on Calli's and Elizabeth's cards). "Magia," duets and collabs: archived titles;
  "逆様": the official video listing (undated here).
- Outfits: Claude's reading of the official gallery images.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki's Phasmophobia (yVdTbPCJytw) and #フブミオ大予想 (iJpIGu5HuGY).

## Merge Record
- **2026-11-27, Claude only (author order: complete all FLOW GLOW members):** official profile, gallery and music
  pages, the official FLOW GLOW page, archive metadata and a two-model ASR check (NK20). Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. The release date of "逆様" and the reveal date of the Japanese-style outfit are not established here.
2. Her spoken opening was not captured in the two windows checked (opening music covered it).
````

### FILE: `bible/characters/Mizumiya-Su.md`

````markdown
---
kind: character
name: "Mizumiya Su"
sw_section: Characters
---

# Character File: Mizumiya Su

> Scope: official lore and publicly shown persona only, checked 2026-11-27. Su is an active hololive member
> (FLOW GLOW; she debuted through hololive DEV_IS, which COVER restructured in a 2026-09-07 announcement, so DEV_IS
> is not listed as a current separate affiliation) at the 2026-09-30 baseline; added to the cast by author order
> (2026-11-27: complete all FLOW GLOW members). Recent streams set her default manner, per the project's recency
> rule. Nothing about the performer behind the avatar: private-life information (family, home, health, daily
> routine, sleep, outings, where she streams from and the like) is outside scope and is not recorded here,
> including what she mentions in chats and stream titles. She streams in Japanese. In stories she knows she is a
> streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title, description or post; "(secondary)" means the wording comes from a news
>   report, an encyclopedia or another secondary source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; SU20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (SU#) are listed under Sources.
>
> **Audio status:** on 2026-11-27 Claude checked two archived August 2025 chat streams (a morning chat and a
> late-night chat; SU20, research/audio-check/flowglow.md); no 2026 chat window was checked, so her 2026 manner rests
> on titles. Personal remarks are not quoted or summarized here. The audio was machine-transcribed and acoustically
> measured; transcripts were reviewed in context, without independent listening verification.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
"Is your Su-charge at 100%?" (official English profile wording): FLOW GLOW's tiny publicity manager, a
light-blue-haired girl who wants to be loved and praised, posts on social media with her mouth full, asks the gods
to make her a little taller, opens every stream with 「しゅぴしゅわ〜」 and calls herself 「水宮」. [Official SU1, SU2]
[ASR SU20]

## Core Drive
- **Want:** love and praise (official); in her lore, after wishing the world were kinder she found her friends,
  "so not all hope is lost." [Official SU1]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** her height: she asks the gods to make her taller; her stream and fan-art tags
  (#すう成長中, "Su is growing"; #すくすく枢, "Su growing up healthy") play on it. [Official SU1]
- **Values shown in public:** her fans (Su-risu), whom she thanks one by one; her unit; her senpai. [ASR SU20]

## Core Contradiction
A publicity manager who promotes everything, herself included, and bills herself as a newcomer whose love is
"heavy" (愛が重い, a 2024 title), yet is the smallest member of the unit and wants to be bigger. [Official SU1]
[SU4 gtmy9wF-uy8]

## Behavioral Traits
1. Opens with her official line, 「しゅぴしゅわ〜！すうの充電たりてる？」, then introduces herself as FLOW GLOW's
   publicity manager, 「宣伝担当、水宮枢です」, and 「お願いします」; in morning streams she adds 「グッドモーニング」 and
   「いい朝ですね」. [Official SU1, SU2] [ASR SU20]
2. Calls herself 「水宮」 (Mizumiya, her surname) far more than 「すう」 (about thirty times in four windows).
   [ASR SU20]
3. Thanks viewers by name, one after another; 「ありがとう」 is her most frequent word in the windows checked.
   [ASR SU20]
4. Ends with 「今日はこの辺で終わりたいと思います」, leads chat in a group "otsu" on 「いきますよー、せーの！」 and closes
   with 「おやすみだよー」 and 「バイバーイ」. [ASR SU20]
5. Dance shorts as a chibi "mini-Mizumiya" (みにみや, 2026). [SU4 titles]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: "Is your Su-charge at 100%?" / 「しゅぴしゅわー　すうの充電たりてる？」 [Official SU1, SU2]
  - Opening: 「しゅぴしゅわ〜！すうの充電たりてる？」 + 「宣伝担当、水宮枢です」 (both models; the coined
    「しゅぴしゅわ」 as a near-match, the rest as shared spans, 2025-08). [ASR SU20]
  - Sign-off: 「いきますよー、せーの！」 → group "otsu~" (the word after "otsu" differs between the models) →
    「おやすみだよー」 → 「バイバーイ」. [ASR SU20]
- **Catchphrases & bits:** 「しゅぴしゅわ」; 「すうの充電」 ("Su-charge"); 「水宮」 for herself; Su-risu (すうりす) for
  her fans; #すう成長中 (streams), #すくすく枢 (fan art; AI-made fan art only under #AIすくすく枢); fan mark 💬🔁💙.
  [Official SU1] [SU4 descriptions]
- **Vocabulary / fillers:** 「めっちゃ」, 「なんか」, 「おいしょ」, 「マジで」, English greetings such as "Good
  morning" (first-model observations); no regional accent is assigned. [ASR SU20]
- **Profanity:** none observed in the windows checked.
- **Language:** streams in Japanese with English greetings.
- **Laughs, noises:** a soft giggle is a design choice.
- **Rhythm & rhetoric:** bubbly and chatty, small grunts of effort (「おいしょ」), a stream of thank-yous.
  [ASR SU20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (SU20): in two 2025 chat streams, median about 288–312 Hz (p10–p90 about 131–491 Hz, a wide spread
    that includes background audio) and about 259–371 characters a minute of speech. Measurements describe the
    archived audio, not a target to clone.
  - Provisional (interpretation): a light, high, sweet voice with a playful bounce.
- **Sounds off:** a low, mature, sultry voice; cool aloofness; slow monotone.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bubbly, bright | 「すうの充電たりてる？」 (Official SU1; ASR SU20) |
| Reading superchats | Grateful, quick | **Style demo:** 「ありがとう！ありがとうね！」 |
| Promoting something | Upbeat, salesy | **Style demo:** 「みんな、これ見てってね！」 ("Everyone, check this out!") |
| Teased about her height | Pouting | **Style demo:** 「すう、成長中だもん！」 ("I'm still growing!") |
| Signing off | Sleepy, sweet | 「おやすみだよー」 (ASR SU20) |

### Sample Lines
1. "Is your Su-charge at 100%?" (Official SU1)
2. 「宣伝担当、水宮枢です」 (senden tantō, Mizumiya Su desu, "I'm Mizumiya Su, publicity manager") (ASR SU20, 2025)
3. 「いきますよー、せーの！」 (ikimasu yo, sēno!, "Here we go, ready, set!") (ASR SU20)

## Appearance Anchors (avatar)
145 cm (official profile; an encyclopedia records 151 cm before 2025-11-26, secondary); illustrator Bukurote
(ぶくろて). Light-blue hair to the shoulders with pink streaks and a lightning-bolt ahoge, blue eyes and a small fang.
Emoji 💬🔁💙. The official profile gallery (checked 2026-11-27) shows three outfits; descriptions are Claude's
reading of those images:
- **Original outfit (debut, 2024-11):** two small pink-and-blue braids and a blue hair clip; a black choker; an
  oversized white zip-up jacket with black ribbon lacing down the sleeves and pom-pom drawstrings; a light-blue
  graphic T-shirt worn as a dress, torn at the hem; a pink smartphone on a chain across her body; a black thigh
  strap and ankle strap; light-blue slouch socks with white bows; chunky white sneakers. [Official SU1 gallery 01_a, 02]
- **Black-and-blue frilled outfit:** hair in two pink-and-blue buns under a black lace headdress hung with charms;
  a black off-shoulder ruffled top with gingham trim and light-blue lacing; frilly black shorts; fingerless gloves;
  striped leg warmers; black platform boots. [Official SU1 gallery 01_b]
- **Japanese-style candy outfit:** twin braided tails tied with pink bows and candy hair ornaments; a white frilled
  pinafore with a lightning-bolt brooch over light-blue and pink candy-patterned kimono sleeves and a tiered skirt;
  pink platform shoes. Its reveal stream is not in the archive checked. [Official SU1 gallery 03]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2024-11-09 | Debut (third in the FLOW GLOW relay) through hololive DEV_IS; "FG ROADSTER" | [Official SU1; FLOW GLOW card S4] |
| 2024-11 to 12 | #にこすぅ with Niko (11-24); "らぶきゅん♡うぉんてっど" with Vivi (12-05); "レイメイ" with Chihaya (12-06) | [SU4] |
| 2025 | #こよすう, a first one-on-one collab with Koyori (02-02); #すうはあ with Akai Haato (04); a first birthday stream calling her senpai (06-16); Marine's "pet" collab (06-29); "ポケットにファンタジー" with Niko (06-29); ぶんしゅぴ with Todoroki Hajime (07-14); a ちはすう off-collab (08-03); "Beyond the way" with Chihaya (08-17) | [SU4] [SU5] |
| 2025-11-23 | FLOW GLOW's 3D debut live | [FLOW GLOW card S6] |
| 2026-03-07 | FLOW GLOW's festival debut, hololive 7th fes. STAGE3 | [FLOW GLOW card S8] |
| 2026-06 | RoARiS (Roboco, AZKi, Su, Riona) play Momotetsu 2 (06-07); すうヴィヴィ drive in Forza Horizon 6 with Vivi (06-06) | [SU4] [Riona's channel jG-EPYQ4V9g] |
| 2026-06-17 | First solo single, "うみゃうにゃはっぴーらいふ" (Umyaunyahappylife) | [Official SU3] |
| 2026-07 | Guest at AZKi's 2026 birthday 3D live ("トウキョウ・シャンディ・ランデブ") | [SU5 fqGI67bRcXQ] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Isaki Riona, Koganei Niko, Rindo Chihaya, Kikirara Vivi | Unitmates | Group songs, the 3D live, the 2026 album | [Official] |
| Kikirara Vivi | Duet partner | "らぶきゅん♡うぉんてっど" (2024), "クリームで会いにいけますか" (official listing); a Forza Horizon 6 drive (2026) | [SU4] [Official listing] |
| Rindo Chihaya | Duet partner | "レイメイ" (2024), "Beyond the way" (2025); a ちはすう off-collab (2025) | [SU4] |
| Koganei Niko | Unitmate | #にこすぅ (2024); "ポケットにファンタジー" (2025) | [SU4] |
| Isaki Riona | Unitmate | RoARiS with Roboco and AZKi (2026) | [Riona's channel] |
| AZKi | Senpai | RoARiS (2026); a guest song at AZKi's 2026 birthday live | [SU5] |
| Hakui Koyori | Senpai | #こよすう, their first one-on-one collab (2025-02-02) | [SU5 f4K54Fc-ghM] |
| Houshou Marine | Senpai | A collab on Marine's channel in which Su makes Marine her "pet" (2025-06-29) | [SU5 zpG2xKGK_Jo] |

## Arc
- **Starting point:** active at the 2026 baseline: FLOW GLOW's publicity manager with a solo single and a steady
  run of duets with her unitmates.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a promotion campaign that gets out of hand; posting something before the unit agreed to it;
  insisting she has grown since last week.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Su live-posts the unit's road trip and accidentally reveals a surprise for Riona.
  2. Marine tries to reverse their "pet" arrangement; Su refuses.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2024-11-09 through hololive DEV_IS; FLOW GLOW (publicity manager); birthday 16 June; 145 cm; illustrator
  Bukurote; fans Su-risu (すうりす); tags #すう成長中, #すくすく枢; emoji 💬🔁💙.

## Sources (checked 2026-11-27)
- SU1 Official profile (text, data and gallery): https://hololive.hololivepro.com/en/talents/mizumiya-su/
- SU2 Official FLOW GLOW page (Japanese profile and tagline): https://hololive.hololivepro.com/special/13902/
- SU3 Official music: https://hololive.hololivepro.com/en/music/763/ ("Umyaunyahappylife," 2026-06-17)
- SU4 Her channel's archive metadata (archive.ragtag.moe; titles and descriptions): wWFk5Oms1wg (debut; description
  「しゅぴしゅわ〜すうの充電たりてる…❔♡」), 8fyVCoPWMb8 and ZIkex-Hye6E (2025 chats), gtmy9wF-uy8 ("heavy love"
  title), FfbAJcQu7G8 and zKA2G6hX9iI (with Vivi), nUjFJBb6MDA and PcSLoke_mH8 (with Chihaya), 7RAHdEtY7Fo (ちはすう),
  DDKaJ1cbM8Y (#すうはあ), VN2Wrg3qJoI (ぶんしゅぴ), rFw9SwoIVD8 (birthday 2025), ypxnG-t-dmc (すうヴィヴィ),
  2ZpVq1kGxBk and dNPMppKpWSY (dance shorts), QCMtwotxvxY ("ポケットにファンタジー," Niko's channel)
- SU5 Other channels' archive metadata: f4K54Fc-ghM (#こよすう, Koyori), zpG2xKGK_Jo (Marine), fqGI67bRcXQ (AZKi's
  2026 birthday live short), jG-EPYQ4V9g (RoARiS, Riona's channel)
- SU6 Japanese Wikipedia, "水宮枢" (secondary; height history), checked during the 2026-11-27 research
- SU20 Claude's audio check (two-model ASR, Japanese): research/audio-check/flowglow.md
- Official video listing on her profile: _ypWJ0IitYA ("クリームで会いにいけますか," with Vivi)

## [SW] Name
Mizumiya Su

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, FLOW GLOW

## [SW] Other Names
Su, 水宮枢, Mizumiya

## [SW] Personality
Her official profile presents Su as FLOW GLOW's publicity manager: determined to be loved and praised, she posts on social media with her mouth full of something delicious. She once wished the world were a kinder place and then found the friends she has now; she thanks the gods for them and asks to be made a little taller. On stream she is bubbly and chatty, calls herself "Mizumiya," thanks her viewers one by one and promotes her unit at every chance. She jokes that her love is "heavy," pouts about her height and leads her chat in a group goodbye at the end of each stream. Her fans are the Su-risu.

## [SW] Background
Su is an active member of FLOW GLOW. She has no supernatural abilities; her lore is a performed persona. She debuted on 2024-11-09 through hololive DEV_IS as FLOW GLOW's publicity manager, with Isaki Riona, Koganei Niko, Rindo Chihaya and Kikirara Vivi. She has recorded duets with each of her unitmates: with Vivi ("らぶきゅん♡うぉんてっど," "クリームで会いにいけますか"), with Chihaya ("レイメイ," "Beyond the way") and with Niko ("ポケットにファンタジー"). FLOW GLOW held its 3D debut live on 2025-11-23, released its first album on 2026-01-21 and made its festival debut at hololive 7th fes. on 2026-03-07. Su released her first solo single, "うみゃうにゃはっぴーらいふ" (Umyaunyahappylife), on 2026-06-17 and sang as a guest at AZKi's 2026 birthday live.

## [SW] Physical Description
Su's avatar is 145 cm tall, with light-blue shoulder-length hair streaked with pink, a lightning-bolt ahoge, blue eyes and a small fang. Original outfit: two small pink-and-blue braids and a blue hair clip, a black choker, an oversized white zip-up jacket with black ribbon lacing down the sleeves, a torn light-blue graphic T-shirt worn as a dress, a pink smartphone on a chain across her body, black thigh and ankle straps, light-blue slouch socks with white bows and chunky white sneakers. Frilled outfit: two pink-and-blue buns under a black lace headdress hung with charms, a black off-shoulder ruffled top with gingham trim and blue lacing, frilly black shorts, striped leg warmers and black platform boots. Japanese-style candy outfit: twin braids with pink bows and candy ornaments, a white frilled pinafore over light-blue and pink candy-patterned kimono sleeves and a tiered skirt, and pink platform shoes.

## [SW] Dialogue Style
Streams in Japanese: bubbly, quick and sweet, calling herself 「水宮」 (Mizumiya). She opens with 「しゅぴしゅわ〜！すうの充電たりてる？」 and 「宣伝担当、水宮枢です」, scatters English greetings ("Good morning") and a stream of 「ありがとう」, and ends with 「いきますよー、せーの！」, a group goodbye and 「おやすみだよー」. No regional accent is assigned. When a story renders her speech in English or Chinese, keep the bouncy promo energy, the surname self-reference and the pouting when she is called small.

## [SW] Catchphrases
"Is your Su-charge at 100%?" (official English; 「しゅぴしゅわ〜！すうの充電たりてる？」, "Shupi-shuwa~! Sū no jūden tariteru?"); 「宣伝担当、水宮枢です」 ("I'm Mizumiya Su, publicity manager"); 「いきますよー、せーの！」 ("Here we go, ready, set!") before the group goodbye; 「おやすみだよー」 ("Good night~"); "Mizumiya" (herself); "Su-risu" (すうりす, her fans); 「すう成長中」 ("Su is growing," her stream tag).

## [SW] Voice & Delivery
Direction for an original designed voice: a light, high, sweet voice with a playful bounce; bright and quick when she opens or promotes, grateful and rapid when thanking viewers, pouty when teased, soft and sleepy when she says good night. Not as default: a low, sultry or mature voice, cool aloofness or a slow monotone.

## [SW] Audio Tags
Dialogue language for audio scripts: Japanese. Write her spoken turns in Japanese script; romaji and English go only on ROMAJI/GLOSS lines. ElevenLabs v4 performance directions for an original designed voice; never imitate the real member. Register: light, high, sweet voice. Default tags: [bubbly, sweet]. By situation: opening [bright, upbeat]; thanking viewers [grateful, quick]; promoting [upbeat, salesy]; teased about her height [pouting]; signing off [sleepy, soft]; a duet partner's turn [cheerful]. With people: Vivi [giggly]; Chihaya [cheerful]; Marine [bossy, playful]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [giggles] (tag only); 「おいしょ」 ("oisho," spoken). Keep in the words: 「しゅぴしゅわ」 (shupi-shuwa), 「すうの充電」 (Sū no jūden), 「すうりす」 (Su-risu). Reading: みずみや すう. No regional accent is assigned. Not as default: a low, sultry or flat read.

## [SW] Motivation
In her lore, Su wants to be loved and praised, and a little taller. As a streamer and singer, she wants to spread the word about FLOW GLOW and keep her fans' "Su-charge" full.

## [SW] Relationships
FLOW GLOW (Isaki Riona, Koganei Niko, Rindo Chihaya, Kikirara Vivi): her unit. Kikirara Vivi: duets "らぶきゅん♡うぉんてっど" and "クリームで会いにいけますか"; a Forza Horizon 6 drive (2026). Rindo Chihaya: duets "レイメイ" and "Beyond the way"; a ちはすう off-collab (2025). Koganei Niko: #にこすぅ and "ポケットにファンタジー." Isaki Riona: RoARiS with Roboco and AZKi (2026). AZKi: RoARiS and a guest song at AZKi's 2026 birthday live. Hakui Koyori: #こよすう, their first one-on-one collab (2025). Houshou Marine: a collab in which Su made Marine her "pet" (2025).

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Voice & Delivery and Audio Tags are performance directions for an original designed voice. Timbre, laughter and
  delivery are design choices unless a listening source is named in the Voice Profile; ASR supports wording, not
  vocal quality or recurrence; partner tags are optional scene directions, not observed defaults; the kana reading
  is untested; recorded pitch and speaking-rate figures are research context only, never synthesis targets.
- Opening: 「しゅぴしゅわ」 is the official spelling; both models heard a near-match (シピシワー / シュピシュワー).
  「スーの充電足りてる」, 「宣伝担当水宮枢です」 (the models write 数 or スー for 枢; same reading), 「いきますよー、
  せーの」 and 「おやすみだよー」: shared spans. The word after the group "otsu" differs between the models and is not
  quoted.
- 「水宮」 as self-reference: counted in the first-model transcripts. "Heavy love": a 2024 archived title. Height
  history: an encyclopedia (secondary).
- "クリームで会いにいけますか": the official video listing (undated here). Outfits: Claude's reading of the official
  gallery images.

## Merge Record
- **2026-11-27, Claude only (author order: complete all FLOW GLOW members):** official profile, gallery and music
  pages, the official FLOW GLOW page, archive metadata and a two-model ASR check (SU20). Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. A 2026 chat window should be checked to confirm her current manner (the two windows checked are from 2025).
2. The release date of "クリームで会いにいけますか" and the Japanese-style outfit's reveal are not established here.
````

### FILE: `bible/characters/Rindo-Chihaya.md`

````markdown
---
kind: character
name: "Rindo Chihaya"
sw_section: Characters
---

# Character File: Rindo Chihaya

> Scope: official lore and publicly shown persona only, checked 2026-11-27. Chihaya is an active hololive member
> (FLOW GLOW; she debuted through hololive DEV_IS, which COVER restructured in a 2026-09-07 announcement, so DEV_IS
> is not listed as a current separate affiliation) at the 2026-09-30 baseline; added to the cast by author order
> (2026-11-27: complete all FLOW GLOW members). Recent streams set her default manner, per the project's recency
> rule. Nothing about the performer behind the avatar: private-life information (family, home, health, daily
> routine, sleep, outings, where she streams from and the like) is outside scope and is not recorded here,
> including what she mentions in chats and stream titles; the official profile's family line is not carried onto
> the card. She streams in Japanese. In stories she knows she is a streamer with a persona (see the world card
> "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title, description or post; "(secondary)" means the wording comes from a news
>   report or another secondary source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; CH20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (CH#) are listed under Sources.
>
> **Audio status:** on 2026-11-27 Claude checked two archived August 2025 late-night chat streams (CH20,
> research/audio-check/flowglow.md); no 2026 chat window was checked, so her 2026 manner rests on titles. Personal
> remarks are not quoted or summarized here. The audio was machine-transcribed and acoustically measured; transcripts
> were reviewed in context, without independent listening verification.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
"Won't you come with me to chase greater heights and see the scenery from high above?" (official English profile
wording): FLOW GLOW's DJ and driver, a self-proclaimed 300-horsepower talker with no brakes, earnest and curious,
a beginner DJ in big headphones who loves nothing more than driving her friends in her car, and who calls herself
「ちは」. [Official CH1, CH2] [CH4] [ASR CH20]

## Core Drive
- **Want:** to take her friends somewhere new; officially, what matters most to her now is driving her buddies in
  her beloved car (in FLOW GLOW's lore, the car Fugutarō carries the whole unit). [Official CH1, CH2]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** none stated; she is officially a newcomer as a DJ who is growing fast.
  [Official CH1]
- **Values shown in public:** her fans (Chihanic), her unit, long talks with chat. [ASR CH20]

## Core Contradiction
A car-loving DJ with spiked sleeves and a checkered cap who is, by her official profile, earnest to the core:
the punk look and the 300-horsepower talk sit on top of a polite girl who thanks everyone for staying up with her.
[Official CH1] [ASR CH20]

## Behavioral Traits
1. Calls herself 「ちは」 (Chiha) and writes playful verb-plus-「だよ」 titles: 「歌うだよ〜」 ("singing, y'know~"),
   「やるだよ〜」, 「おはよだよ〜」 ("mornin', y'know~"), 「お疲れ様だよ〜」. [CH4 titles] [ASR CH20]
2. Opens a chat with a string of 「こんばんはー」 and announces 「雑談でございます」 ("this is a chat stream"). [ASR CH20]
3. Talks without brakes: long, fast stretches about whatever happened lately, playful whining, then sudden sincerity
   when she thanks chat. [Official CH1] [ASR CH20]
4. Closes politely: 「ということでお疲れ様でした、遅くまでお付き合いありがとうございました」 ("So, good work today;
   thank you for staying up so late with me"), then 「おやすみなさーい」 and 「いい夢見てね」 ("sweet dreams").
   [ASR CH20]
5. Cars and racing: a long run of Shutoko Battle (首都高バトル) streams from its pre-release play (2025-01-22), a
   racing-wheel stream (2025-07-15), and Forza with Su. [CH4 titles]
6. Plays trombone: Suisei's "ビビデバ" on trombone (2025-01-15); covers Suisei's "ムーンライト" (2024-12-28).
   [CH4 titles]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: "Won't you come with me to chase greater heights…?" / 「ねえ、いっしょに向こう側の景色を見に行か
    ない？」 ("Hey, won't you come see the view from the other side with me?") [Official CH1, CH2]
  - Self-introduction (channel descriptions): 「ホロライブDEV_ISからデビューした FLOWGLOWのDJ兼運転手 輪堂千速です！」
    ("I'm Rindo Chihaya, FLOW GLOW's DJ and driver, debuted from hololive DEV_IS!"). [CH4 descriptions]
  - Opening: 「こんばんはー」 and 「雑談でございます」 (shared spans, 2025-08; the full sentence differs by one mora
    between the models). [ASR CH20]
  - Sign-off: 「ということでお疲れ様でした、遅くまでお付き合いありがとうございました」 (shared span), 「いい夢見てね」,
    「おやすみなさーい」; in a 2025 anniversary chat, 「夢見てね、みんなのおかげで9ヶ月でした」 ("sweet dreams; I made
    it nine months thanks to you all", shared) and 「ニックたち大好きだよ」 ("I love you, Nicks"; the models spell the
    fan name differently). [ASR CH20]
- **Catchphrases & bits:** 「ちは」 for herself; Chihanic / ニック (from "mechanic") for her fans; #おしゃべりん堂
  (streams), #もはやちはや (fan art); fan mark 🎧🔧. [Official CH1] [CH4 descriptions]
- **Vocabulary / fillers:** 「なんか」, 「ちょっと待って」, 「マジで」, 「やだやだ」 (first-model observations); no regional
  accent is assigned. [ASR CH20]
- **Profanity:** none observed in the windows checked.
- **Language:** streams in Japanese.
- **Laughs, noises:** a bubbling laugh at her own jokes (first-model 「ふふふ」 and 「あははは」); its sound is a design
  choice.
- **Rhythm & rhetoric:** rapid, run-on chat with laughter, then polite set phrases at the start and end. [ASR CH20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (CH20): in two 2025 late-night chats, median about 209–291 Hz (p10–p90 about 150–443 Hz) and about
    287–326 characters a minute of speech. Measurements describe the archived audio, not a target to clone.
  - Provisional (interpretation): a clear, lively mid-range voice with a cool edge that softens at night.
- **Sounds off:** a shy whisper; a slow, hesitant delivery; a cold, terse voice.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening a chat | Bright, casual | 「こんばんはー」…「雑談でございます」 (ASR CH20) |
| Talking fast | Rapid, laughing | **Style demo:** 「ちょっと待って、聞いて聞いて！」 ("Wait, listen, listen!") |
| Racing | Fired up, focused | **Style demo:** 「全開でいくよ！」 ("Going full throttle!") |
| Signing off | Polite, soft | 「遅くまでお付き合いありがとうございました」 (ASR CH20) |
| To her fans | Warm, affectionate | 「いい夢見てね」 ("sweet dreams") (ASR CH20) |

### Sample Lines
1. "Won't you come with me to chase greater heights and see the scenery from high above?" (Official CH1)
2. 「ということでお疲れ様でした、遅くまでお付き合いありがとうございました」 (to iu koto de otsukaresama deshita, osoku
   made otsukiai arigatō gozaimashita) (ASR CH20, 2025)

## Appearance Anchors (avatar)
168 cm; illustrator toridamono (トリダモノ). Shoulder-length black hair with a teal streak and a white streak, and
crimson eyes. Emoji 🎧🔧. The official profile gallery (checked 2026-11-27) shows three outfits; descriptions are
Claude's reading of those images:
- **Original outfit (debut, 2024-11):** a black-and-grey checkered cap with a blue wrench clip; big DJ headphones
  around her neck; a black choker; an off-shoulder black dress with a teal flame emblem and white sleeves studded
  with spikes, with jagged hems; a belt with a pouch; a thigh harness; black chunky boots with spikes and leg
  warmers; a blue wrench in hand. [Official CH1 gallery 01_a, 02]
- **Racing stage outfit:** a black bustier with teal accents; an oversized white-and-black racing jacket with teal
  stripes slipping off her shoulders; a black studded mini skirt over bike shorts; one black thigh-high; black boots
  with teal soles; a silver microphone. [Official CH1 gallery 01_b]
- **Japanese-style outfit:** a white kimono top patterned with black-and-white checks like a racing flag, with red
  accents; a dark-green hakama with a high slit; a large white flower and gold ornaments in her hair; black gloves
  and black boots. Its reveal stream is not in the archive checked. [Official CH1 gallery 03]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2024-11-09 | Debut (fourth in the FLOW GLOW relay) through hololive DEV_IS; "FG ROADSTER" | [Official CH1; FLOW GLOW card S4] |
| 2024-11 to 12 | ちーむ変態ジェントルマン with Riona and Niko; "レイメイ" with Su (12-06); a talk collab with Sakamata Chloe (12-12); Chained Together with Tokoyami Towa (12-28) | [CH4] |
| 2025 | Shutoko Battle from its pre-release play (01-22); Gang Beasts with Nene, Lamy and Riona (01-20); Minecraft with Okayu (02-20) and a voice-impression game with her (03-24); horse racing with Lui (02-23); ELDEN RING NIGHTREIGN with Ichijou Ririka and Niko (06); a birthday party stream (07-08); "Bridal Dream" with Vivi (07-28); a ちはすう off-collab (08-03); "Beyond the way" with Su (08-17) | [CH4] [CH5] |
| 2025-11-23 | FLOW GLOW's 3D debut live | [FLOW GLOW card S6] |
| 2026-03-07 | FLOW GLOW's festival debut, hololive 7th fes. STAGE3 | [FLOW GLOW card S8] |
| 2026-07-08 | A 3D birthday live (announced the day before) | [CH4 EpJTd9Xlvlk] |
| 2026-07-09 | First solo single, "Flat out" | [Official CH3] |
| 2026-09-20 | "打上花火" with Okayu | [CH4 UGQfq16yY1A] |
| 2026-10-30 | Second solo single, "果てない旅" (HatenaiTabi) | [Official CH3] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Isaki Riona, Koganei Niko, Mizumiya Su, Kikirara Vivi | Unitmates; she drives the unit in its lore | Group songs, the 3D live, the 2026 album | [Official] |
| Isaki Riona, Koganei Niko | ちーむ変態ジェントルマン | Chained Together and a "butt-bat" penalty off-collab (2024); a watch-along of Calli's live (2025) | [CH4] [Riona's channel] |
| Mizumiya Su | Duet partner | "レイメイ" (2024), "Beyond the way" (2025); a ちはすう off-collab (2025) | [CH4] |
| Kikirara Vivi | Duet partner | "Bridal Dream" (2025-07-28) | [Vivi's card] |
| Nekomata Okayu | Senpai | Minecraft (2025-02-20, on both channels); a voice-impression game (2025-03-24); "打上花火" (2026-09-20) | [CH4] [CH5 ScqzxDtCIoY] |
| Sakamata Chloe | Senpai | A talk collab on Chihaya's channel (2024-12-12) | [CH4 FgSn_JCgKyk] |
| Takane Lui | Senpai | A February Stakes horse-racing stream on Lui's channel (2025-02-23) | [CH5 Lh7LPWpmCEI] |
| Yukihana Lamy | Senpai | Gang Beasts with Nene and Riona (2025-01-20) | [CH5 EsfZ7Ny4aPA] |
| Hoshimachi Suisei | Senpai | Chihaya covered "ムーンライト" and played "ビビデバ" on trombone | [CH4] |
| Mori Calliope | Senpai | A watch-along of Calli's live with Riona and Niko (2025-02-27) | [Riona's channel 4Zb0JEy3bw4] |
| Shirakami Fubuki, Inugami Korone (GAMERS) | Senpai | Phasmophobia with Fubuki, Niko and Polka (2025-04-20); R.E.P.O. on Korone's channel (2026-06-29) | [Fubuki channel yVdTbPCJytw] [Korone channel G6r_oZBgD3E] |

## Arc
- **Starting point:** active at the 2026 baseline: FLOW GLOW's DJ and driver with a 3D birthday live and two solo
  singles in 2026.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a story that never ends; a detour "for the view"; a playlist she insists on DJing in the car.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Chihaya drives the unit to a sunrise spot and talks the whole way there.
  2. Okayu borrows Fugutarō's passenger seat and Chihaya tries to impress her with a perfect playlist.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2024-11-09 through hololive DEV_IS; FLOW GLOW (DJ and driver); birthday 8 July; 168 cm; illustrator
  toridamono; fans Chihanic (ニック); tags #おしゃべりん堂, #もはやちはや; emoji 🎧🔧.

## Sources (checked 2026-11-27)
- CH1 Official profile (text, data and gallery): https://hololive.hololivepro.com/en/talents/rindo-chihaya/
- CH2 Official FLOW GLOW page (Japanese profile, tagline and the car Fugutarō): https://hololive.hololivepro.com/special/13902/
- CH3 Official music: https://hololive.hololivepro.com/en/music/772/ ("Flat out," 2026-07-09), …/850/
  ("HatenaiTabi," 2026-10-30)
- CH4 Her channel's archive metadata (archive.ragtag.moe; titles and the description template): esR2XM9FuTw
  (debut), kNFiSEYSUeo and dtVUhrM1cPQ (2025 chats), fjuIKHuNYBc, LbZFVEwvfJI and bp0j9u9Wqus ("…だよ" titles),
  xwnYkyOPOP4 (Shutoko Battle), iZW9-DTSQfc (racing wheel), nREYWWmVVls and xqwCq0AZXeg (Suisei's songs),
  h1OY5HGdGKo and PcSLoke_mH8 (with Su), FgSn_JCgKyk (Chloe), TC-_5MpYfkc (Towa), IYBdcw4wWuA and DcfVi2rf1oc
  (Okayu), CZn61Egrj6w (ELDEN RING NIGHTREIGN), WrwdZp6xILU (birthday 2025), EpJTd9Xlvlk (3D birthday live),
  UGQfq16yY1A ("打上花火")
- CH5 Other channels' archive metadata: ScqzxDtCIoY (Okayu), Lh7LPWpmCEI (Lui), EsfZ7Ny4aPA (Lamy), i25b--m63UU and
  DBN-VVm-pRs (Riona's channel), 7RAHdEtY7Fo (Su's channel)
- CH20 Claude's audio check (two-model ASR, Japanese): research/audio-check/flowglow.md

## [SW] Name
Rindo Chihaya

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, FLOW GLOW

## [SW] Other Names
Chihaya, Chiha, 輪堂千速

## [SW] Personality
Her official profile presents Chihaya as FLOW GLOW's DJ and driver: a self-proclaimed 300-horsepower driver whom nobody can brake once she starts talking or singing, still a beginner DJ but growing fast thanks to her earnestness and curiosity, and happiest driving her friends around in her beloved car. On stream she calls herself "Chiha," talks at full speed, laughs at her own jokes and whines playfully at chat, then turns sincere and polite when she thanks people for staying up with her. She loves cars and racing games, plays trombone and sings at every chance. Her fans are the Chihanic.

## [SW] Background
Chihaya is an active member of FLOW GLOW. She has no supernatural abilities; her lore is a performed persona. She debuted on 2024-11-09 through hololive DEV_IS as FLOW GLOW's DJ and driver, with Isaki Riona, Koganei Niko, Mizumiya Su and Kikirara Vivi; in the unit's lore her customized car, Fugutarō, carries all five. She streamed Shutoko Battle from its pre-release play in January 2025, sang duets with Su and Vivi, and joined Riona and Niko as the self-styled "team hentai gentlemen." FLOW GLOW held its 3D debut live on 2025-11-23, released its first album on 2026-01-21 and made its festival debut at hololive 7th fes. on 2026-03-07. Chihaya held a 3D birthday live on 2026-07-08 and released the solo singles "Flat out" (2026-07-09) and "果てない旅" (2026-10-30).

## [SW] Physical Description
Chihaya's avatar is 168 cm tall, with shoulder-length black hair streaked with teal and white, and crimson eyes. Original outfit: a black-and-grey checkered cap with a blue wrench clip, big DJ headphones around her neck, a black choker, an off-shoulder black dress with a teal flame emblem and white spiked sleeves with jagged hems, a belt with a pouch, a thigh harness and black chunky spiked boots; she carries a blue wrench. Racing stage outfit: a black bustier with teal accents under an oversized white-and-black racing jacket with teal stripes, a studded black mini skirt over bike shorts, one black thigh-high and black boots with teal soles. Japanese-style outfit: a white kimono top checked like a racing flag with red accents, a dark-green slit hakama, a large white flower in her hair, black gloves and black boots.

## [SW] Dialogue Style
Streams in Japanese: fast, chatty and laughing, calling herself 「ちは」 and writing titles with a playful verb-plus-「だよ」 (「歌うだよ〜」). She opens with a string of 「こんばんはー」 and 「雑談でございます」 ("this is a chat stream"), talks without brakes, and closes politely with 「遅くまでお付き合いありがとうございました」 and 「いい夢見てね」. No regional accent is assigned. When a story renders her speech in English or Chinese, keep the nonstop, cheerful rush that drops into sincere, polite thanks.

## [SW] Catchphrases
"Won't you come with me to chase greater heights and see the scenery from high above?" (official English; 「ねえ、いっしょに向こう側の景色を見に行かない？」); 「FLOWGLOWのDJ兼運転手、輪堂千速です！」 ("I'm Rindo Chihaya, FLOW GLOW's DJ and driver!"); 「ということでお疲れ様でした、遅くまでお付き合いありがとうございました」; 「いい夢見てね」 ("sweet dreams"); 「ニックたち大好きだよ」 ("I love you, Nicks"); "Chiha" (herself); "Chihanic" / ニック (her fans, from "mechanic").

## [SW] Voice & Delivery
Direction for an original designed voice: a clear, lively mid-range voice with a cool edge; rapid and laughing in chat, fired up in races and on the mic, softening into polite warmth at the end of a late stream. Not as default: a shy whisper, a slow hesitant delivery or a cold, terse voice.

## [SW] Audio Tags
Dialogue language for audio scripts: Japanese. Write her spoken turns in Japanese script; romaji and English go only on ROMAJI/GLOSS lines. ElevenLabs v4 performance directions for an original designed voice; never imitate the real member. Register: clear, lively mid-range voice with a cool edge. Default tags: [lively, chatty]. By situation: opening [casual, bright]; a long story [rapid, laughing]; racing [fired up]; DJing [confident, hype]; signing off [polite, soft]; to her fans [warm, affectionate]. With people: Su [cheerful]; Okayu [adoring]; Riona [teasing]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs] (tag only); 「ちょっと待って」 ("chotto matte," spoken). Keep in the words: 「ちは」 (Chiha), 「ニック」 (Nick), 「ふぐ太郎」 (Fugutarō). Reading: りんどう ちはや. No regional accent is assigned. Not as default: a shy whisper or a cold, terse read.

## [SW] Motivation
In her lore, Chihaya wants to drive her friends somewhere new and see the view from the other side together. As a streamer and singer, she wants to grow into a full-fledged DJ and keep talking, singing and racing with her fans.

## [SW] Relationships
FLOW GLOW (Isaki Riona, Koganei Niko, Mizumiya Su, Kikirara Vivi): her unit, which she drives around in its lore. Riona and Niko: the self-styled "team hentai gentlemen" (2024). Mizumiya Su: duets "レイメイ" and "Beyond the way" and a ちはすう off-collab. Kikirara Vivi: the duet "Bridal Dream" (2025). Nekomata Okayu: Minecraft and a voice-impression game (2025) and the cover "打上花火" (2026). Sakamata Chloe: a talk collab (2024). Takane Lui: a horse-racing stream (2025). Yukihana Lamy: Gang Beasts (2025). Hoshimachi Suisei: Chihaya covered her songs, one on trombone. Mori Calliope: Chihaya watched Calli's live with Riona and Niko (2025). Shirakami Fubuki: Phasmophobia with Niko and Omaru Polka (2025). Inugami Korone: R.E.P.O. (2026).

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Voice & Delivery and Audio Tags are performance directions for an original designed voice. Timbre, laughter and
  delivery are design choices unless a listening source is named in the Voice Profile; ASR supports wording, not
  vocal quality or recurrence; partner tags are optional scene directions, not observed defaults; the kana reading
  is untested; recorded pitch and speaking-rate figures are research context only, never synthesis targets.
- Shared ASR spans (both models verbatim): 「こんばんはー」, 「雑談でございます」 (the first model has one different mora
  in between), 「ということでお疲れ様でした、遅くまでお付き合いありがとうございました」, 「夢見てね、みんなのおかげで9ヶ月でした」; 「いい夢見てね」 shared;
  「ニックたち大好きだよ」: the models write ニク / ニック. The self-introduction and the 「…だよ」 titles: written
  (descriptions and titles).
- Shutoko Battle, the racing wheel, trombone and covers: archived titles. Outfits: Claude's reading of the official
  gallery images.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki (yVdTbPCJytw), Korone (G6r_oZBgD3E).

## Merge Record
- **2026-11-27, Claude only (author order: complete all FLOW GLOW members):** official profile, gallery and music
  pages, the official FLOW GLOW page, archive metadata and a two-model ASR check (CH20). Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. A 2026 chat window should be checked to confirm her current manner (the two windows checked are from 2025).
2. The Japanese-style outfit's reveal date is not established here.
````

### FILE: `bible/characters/Shirakami-Fubuki.md`

````markdown
---
kind: character
name: "Shirakami Fubuki"
sw_section: Characters
---

# Character File: Shirakami Fubuki

> Scope: official lore and publicly shown persona only, checked 2026-11-27. Fubuki is an active member of hololive
> (1st generation and hololive GAMERS) at the 2026-09-30 baseline; added to the cast by author order (2026-11-27:
> complete hololive GAMERS). Her recent streams (2026) set her default manner, per the project's recency rule.
> Nothing about the performer behind the avatar: private-life information (family, home, health, daily routine,
> sleep, travel, where she streams from and the like) is outside scope and is not recorded here, including what she
> mentions in chats and stream titles. She streams in Japanese. In stories she knows she is a streamer with a persona
> (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title, description or post; "(secondary)" means the wording comes from a news
>   report or another secondary source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; FB20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (FB#) are listed under Sources.
>
> **Audio status:** on 2026-11-27 Claude checked five archived 2026 solo streams (a birthday-live thank-you talk, an
> event chat, a pre-debut "delusion profile" stream and two game streams) and one collab used only for measurement
> (FB20, research/audio-check/gamers.md). Personal remarks are not quoted or summarized here. The audio was
> machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent listening
> verification.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
「こんこんきーつね！白上フブキです！」 ("Good foxy day! I'm Shirakami Fubuki!", official): a white-haired,
animal-eared otaku fox who loves talking with people and aims to become a top otaku idol while enjoying every day;
1st generation and GAMERS, the senpai who leads collabs, writes off a game over with "F" and insists she is a fox,
not a cat. [Official FB1, FB2] [FB4] [ASR FB20]

## Core Drive
- **Want:** her official dreams: lots of concerts with the other members, her own solo album (released 2025), her
  own Nendoroid, more MC experience and "lots of fun things" with her fans. [Official FB1, FB3]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** being called a cat out of the blue: the cat joke is welcome when she does
  something cat-like ("You're a cat, ain't ya!"), but out of context she'd be sad and "show my pro wrestling moves on
  you all" (official Q&A). [Official FB1, FB2]
- **Values shown in public:** her fans, the Sukonbu; her many collab groups; welcoming new groups of
  kouhai. [Official FB1] [FB4] [ASR FB20]

## Core Contradiction
A self-styled top otaku idol whose royal "FBKINGDOM" concerts sell her as a fox queen, yet on stream she is the
chatty, self-mocking friend who greets with "Hi, Friends!", answers "Wife" with "Friends!" and keeps a rude alter
ego, Kurokami Fubuki, for the lines she would never say herself. [Official FB1, FB3] [FB4]

## Behavioral Traits
1. Calls herself 「白上」 (Shirakami) in the third person (official Q&A wording; about ten times in the transcribed
   windows). [Official FB2] [ASR FB20]
2. A stream vocabulary of her own (official Q&A): 「はじまんぼう」 and 「はじまんた」 to start a stream; 「おはこん」,
   「ひるこん」, 「よるこん」 and 「こんこんきーつね！」 as greetings; 「おつこーん」 to end; "F" and "R.I.P." at a game
   over; "Hi, Friends!" as her signature greeting, with "Friends!" as the answer to "Wife" (and the hybrid
   "WIFriends"); 「～じゃい！」 and 「～やんけ！」 as verbal habits. [Official FB1, FB2]
3. Closes with a set formula: 「といったところで」 or 「ということで」, "that's where we'll end today," then
   「ではでは」 and her sign-off. [ASR FB20]
4. The welcoming senpai: before a new group debuts she guesses their profiles from the teasers (ReGLOSS in 2023;
   FLOW GLOW with Mio, #フブミオ大予想, 2024; アソビ★まわり隊, 2026), watches their first streams with her viewers and
   takes newcomers ghost-hunting; in 2026 she told the newcomers not to be swayed by 「このキツネの先輩」 ("this fox
   senpai") but to stream their own way. [FB4 q7323AMTEk4, iJpIGu5HuGY, _vvbn7kgqj4, -pAnDesg9A4, yVdTbPCJytw]
   [ASR FB20]
5. Kurokami Fubuki (黒上フブキ): "another me" with a completely different personality and speech, a 3D body but no
   2D one (she appears as a still image), a birthday on 6 September and fans she calls "Servants"; she has her own
   streams and covers. [Official FB1, FB2] [FB4 qvIZWqp-TMY, az_1XUeg_CU]
6. Mascots and companions (official Q&A): Vice-Manager Intelligence Unicorn, a corn with no gender who helps with
   streams and says "boku"; Oruyanke, a bamboo shoot with fox ears; Fubu-chun, one of the GAMERS birds; Miteiru, who
   is always staring; Fubzilla (フブラ). Her fan mark is a corn because a fox says "kon kon." [Official FB1, FB2]
7. Long-running game series and group events in 2026: an alchemist run in an event survival server
   (#ホロ金策サバイバル2), R.E.P.O., ARK, Star Fox and Hollow Knight: Silksong. [FB4]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: 「こんこんきーつね！白上フブキです！」 / "Good foxy day! I'm Shirakami Fubuki!" [Official FB1, FB2]
  - Openings heard (FB20): her name, 「白上でーす！」, with a near-match of "Hi, Friends!" in both models; the
    evening form 「こんばんきーつね」 was heard by the second model only, once. [ASR FB20]
  - Closing: 「といったところで」 ("with that said"; both models, the first dropping the small っ), 「ということで、
    今日はこの辺りで終わっていこうと思います」 ("so, I think we'll end around here today"; both models, 2026-09-18),
    「ではでは」 and 「今日もありがとうございました」 ("thank you for today too"; shared span, 2026-10-11). [ASR FB20]
  - Sign-off: 「おつこーん」 (official spelling; heard as おつこん in three streams by the second model and as
    near-matches by the first, so the official spelling is used). [Official FB1, FB2] [ASR FB20]
- **Catchphrases & bits:** see trait 2; 「ねこやんけ」 ("you're a cat, ain't ya") is the viewers' joke, 「キツネです！」
  ("I'm a fox!") her answer; Sukonbu (すこん部) for her fans; #フブキch (streams), #絵フブキ (fan art). [Official FB1,
  FB2]
- **Vocabulary / fillers:** 「なんか」 (often), 「ちょっと」, 「かわいい」, polite 「～でございます」 in set phrases, English
  bits ("Hi, Friends!", "F"). [ASR FB20] [Official FB1]
- **Profanity:** none observed in the windows checked; rough talk is Kurokami's register (a 2023 Kurokami stream
  carries a "harsh language" warning in its title). [FB4 dB3MemZf6AI]
- **Language:** streams in Japanese with English bits. No regional accent is assigned; 「～じゃい」 and 「～やんけ」 are
  her official verbal habits, not an accent.
- **Laughs, noises:** quick bursts of laughter are a design choice; none was measured.
- **Rhythm & rhetoric:** fast, chatty and well organized: she announces each part of a stream, recaps for latecomers
  and closes with her set formula. [ASR FB20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (FB20): in five 2026 solo streams, median about 302–354 Hz (p10–p90 about 137–533 Hz) and about
    264–394 characters a minute of speech (game audio present in two). Measurements describe the archived audio, not
    a target to clone.
  - Provisional (interpretation): a bright, clear, high voice, quick and lively, that can drop into a gruff, joking
    「～じゃい！」 register.
- **Sounds off:** a slow, sleepy drawl as her default; a cold, aloof voice; Kurokami's rough register in Fubuki's own
  lines.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Opening | Bright, quick | 「こんこんきーつね！白上フブキです！」 (official) |
| Called a cat | Indignant, comic | 「キツネです！」 (official Q&A) |
| Game over | Deadpan, then laughing | "F." (official Q&A) |
| Advising kouhai | Warm, sincere | 「このキツネの先輩の言葉に流されず、ぜひ自分らしく配信をしてほしいです」 (ASR FB20) |
| Closing | Orderly, warm | 「ということで、今日はこの辺りで終わっていこうと思います」 (ASR FB20) |

### Sample Lines
1. 「こんこんきーつね！白上フブキです！」 (konkon kītsune! Shirakami Fubuki desu!, "Good foxy day! I'm Shirakami
   Fubuki!") (Official FB2)
2. 「このキツネの先輩の言葉に流されず、ぜひ自分らしく配信をしてほしいです」 (kono kitsune no senpai no kotoba ni
   nagasarezu, zehi jibunrashiku haishin o shite hoshii desu, "Don't be swayed by this fox senpai's words; please
   stream your own way") (ASR FB20, September 2026)
3. 「今日もありがとうございました」 (kyō mo arigatō gozaimashita, "Thank you for today too"), after 「ではでは」 and her
   sign-off (ASR FB20, October 2026)

## Appearance Anchors (avatar)
155 cm; illustrator Nagishiro Mito (凪白みと). Long white hair with a small side braid, white fox ears with black
inner tufts, cyan eyes and a white fox tail that darkens to black at the tip, marked with a small star. The official
profile gallery (checked 2026-11-27) shows nine outfits; descriptions are Claude's reading of those images:
- **Original outfit** (gallery 01–02): a white open-front top with a black-lined sailor collar and a light-blue
  neckerchief with a round clasp; detached wide white sleeves tied with light-blue ribbons; a bare midriff; black
  belted shorts; a black thigh-high on one leg and a black thigh strap on the other; black slouch boots with gold
  buckles. [Official FB1 gallery]
- **First new outfit (announced 2019-12-22; the announcement thumbnail shows the same frilled green skirt)** (gallery
  03): a black headband with a small light-blue ribbon, an oversized off-white top with a lace-trimmed collar and a
  big white bow, a dark-green skirt with a white frilled hem, black tights and black boots. [Official FB1 gallery]
  [FB4 pra4uMLmucA]
- **Hakama outfit** (gallery 04): a red flower hair ornament with tassels, a white kimono top whose wide sleeves fade
  to light blue with white blossoms, a navy-and-blue hakama scattered with white blossoms, a navy obi with a ribbon
  and a gold chain, and black lace-up boots. [Official FB1 gallery]
- **"TEK" outfit (named in a 2024-08-05 stream that brought it back, whose thumbnail shows it)** (gallery 05): a white
  technical coat with a fur-trimmed hood, a white scarf, "FOX" lettering and orange accents on the sleeves, long
  blue-and-white ribbons, black shorts, a black thigh band and white-and-black high-top sneakers. [Official FB1
  gallery] [FB4 IDX0gKhahFg]
- **Western-style outfit (worn in a 2020-10-06 stream titled for her new outfit; a 2024-05-27 stream welcomed it back
  as her "Western-style outfit")** (gallery 06): a small black top hat with a gold ornament, a navy double-breasted
  coat dress trimmed in gold, a navy bow with a blue rose brooch, a grey frilled skirt, white tights and grey boots.
  [Official FB1 gallery] [FB4 ta-ajhcaz7Q, JPnG3WsdSp8]
- **Hoodie-and-glasses outfit** (gallery 07): a black headband with small cross-shaped pins, black-rimmed glasses, an
  oversized black zip hoodie with a small "xxx" logo, black socks and hamburger-shaped slippers. [Official FB1
  gallery]
- **Apron-and-pass outfit (revealed 2024-08-09; the reveal silhouette's looped braids and wide sleeves match)**
  (gallery 08): looped braids, a navy dress with wide teal sleeves patterned with gold clovers, a white frilled apron
  with an orange heart-shaped pouch, a lanyard pass, a round clear-window shoulder bag, white tights patterned with
  gold clovers and navy plaid boots. [Official FB1 gallery] [FB4 tnOsA0krATc]
- **Royal outfit (her first solo live, FBKINGDOM "ANTHEM," 2025; a 2025-03-06 watch-along of the live shows it)**
  (gallery 09): a small gold crown, braided hair, a navy coat with gold epaulettes and star chains over a white
  high-collared shirt, a white fur-trimmed mantle lined in red, a blue jewel brooch, a navy skirt with gold stars and
  white thigh-high boots with gold heart garters. [Official FB1 gallery] [FB4 Dc8pLckDSYQ]
- **School-style outfit** (gallery 10): a dark knit vest with brooches over a striped white shirt and a mustard tie, a
  navy plaid pleated skirt with a chain and a white flower charm, navy knee socks and brown loafers. [Official FB1
  gallery]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2018-06-01 | Debut (hololive 1st generation) | [Official FB1] |
| 2018-12-06 | hololive GAMERS unit video (she is in both groups) | [GAMERS card G2 DPZbSlHcdfo] |
| 2019-09-07 | Kurokami Fubuki's first solo stream | [FB4 qvIZWqp-TMY] |
| 2019-12-22 | First new outfit announced | [FB4 pra4uMLmucA] |
| 2022-02-19 | Mori Calliope's HOLO ENGLISH LESSON #01 with Houshou Marine and Ninomae Ina'nis | [Marine and Calli cards] |
| 2022-10-05 | Original "KONKON Beats" | [FB4 c2hbKnXIa_c] |
| 2023-03-21 | "インターネットサバイバー" featuring La+ Darknesss | [FB4 g_6-sM3t760] |
| 2023-10-05 | Birthday 3D live and the original "LETTER☆彡" | [FB4 7995orE5Enc, I7CY960FEPo] |
| 2024-01-02 | "OniOniKonKonWaon" (AyaFubuMi, with Mio and Nakiri Ayame) | [Official FB3] |
| 2024-05-22 | "We are GAMERS!!!!" | [Official FB3] |
| 2024-08-09 | Apron-and-pass outfit revealed | [FB4 tnOsA0krATc] |
| 2024-10-05 | Birthday 3D live, #FBKINGDOMPROLOGUE; "SUPERNOVA" | [FB4 -a68MSMFuuM, 0RG7iNERF4s] |
| 2024-11-09 | #フブミオ大予想: FLOW GLOW's profiles predicted with Mio | [FB4 iJpIGu5HuGY] |
| 2025-01-15 | First album, FBKINGDOM "Blessing" | [Official FB3] |
| 2025-02-02 | "ワンダーフューチャー！" featuring Mio, Nekomata Okayu and Inugami Korone | [FB4 n7ZLEzbubJs] [Official FB3] |
| 2025-02-13 | First solo live, FBKINGDOM "ANTHEM" (Pia Arena MM) | [Official FB6] [Secondary FB7] [FB4 w07Qooj0L_c, Dc8pLckDSYQ] |
| 2025-04-20 | Phasmophobia with Omaru Polka, Koganei Niko and Rindo Chihaya | [FB4 yVdTbPCJytw] |
| 2025-10 | "faint sunset" and "Necchu Syndrome" as Magical Girl holoWitches! | [Official FB3] |
| 2026-02-21 | "Vivid Stampede!!!!" (BAKATARE CIRCUS) | [Official FB3] |
| 2026-03-21 | "Irowanioedomo" (AyaFubuMi) | [Official FB3] |
| 2026-04-02 | "KemomomomomoMof！" (NYANGUCORN, with Okayu) | [Official FB3] |
| 2026-09-18 | Pre-debut "delusion profiles" for アソビ★まわり隊 | [FB4 _vvbn7kgqj4] |
| 2026-10-05 | Birthday 3D live, 「ふぉっくするーむ!!」; "FOXXXROOM" (released 10-06) | [FB4 62AgiXDP3tU] [Official FB3] |
| 2026-11-05 | "Kami-Tsumo Dora Dora Densetsu" with Aki Rosenthal, Marine and Ichijou Ririka | [Official FB3] |
| 2026-11-14 | "Gokuraku Gokigen Enbiyori" (AyaFubuMi) | [Official FB3] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Ookami Mio, Nekomata Okayu, Inugami Korone | GAMERS unitmates | Unit songs; "ワンダーフューチャー！" featuring all three (2025) | [Official FB3] [GAMERS card] |
| Ookami Mio | "FubuMio" (#フブミオ); FAMS | #フブミオ大予想 (2024), We Were Here Expeditions (2024), a joint announcement (2026-04-21); AyaFubuMi | [FB4 iJpIGu5HuGY, rP9TVq9WhdQ, uUFOhSEntNQ] [Mio card] |
| Nekomata Okayu | "NYANGUCORN" | "Pale" cover and Carry The Glass (2025-07-27); "KemomomomomoMof！" (2026); Okayu's "elementary school retest" (2025-05-20) | [FB4 DNIi7lJ58Z8, 9VUUpT_Ta7k, -6YJuLPnnTM] [Official FB3] |
| Inugami Korone | #フブころちゃん | A friendship game (2022-07-06); a Mario Maker 2 course for Korone's sixth anniversary (2025-04-13) | [FB4 -6xMbpbxuyc, BgV_YObYXYM] |
| Nakiri Ayame | "AyaFubuMi" with Mio; FAMS | Three originals (2024, 2026); MUSIC VERSE Fes. (2024-06-09); Fubuki created Ayame's companion Poyoyo (Ayame card) | [Official FB3] [FB4 eB_t5BRj--c] [Ayame card] |
| Houshou Marine | "BABACORN" | A #BABACORN call-in (2023-03-16); Cubic Stars (2023); Content Warning with Shishiro Botan and Oozora Subaru (2024); "Kami-Tsumo Dora Dora Densetsu" (2026); Calli's English lesson (2022) | [FB4 pmMqFJm9bHc, LR9JXY2c7xI, U33SciUF0WQ] [Official FB3] [Marine card] |
| Hakui Koyori | #こんこんこよーて | New Year card-pack openings (2024-01-04, 2025-01-04); EDF5 with Botan (2022); Lethal Company with FUWAMOCO (2024-03-09); White Cat Golf with Yukihana Lamy (2022) | [FB4 cFwsRVbUQaQ, 8dZ9atjf4WA, KtzsKY807hY, Rfq9c8h3LPY] [Koyori card] |
| FUWAMOCO (Fuwawa, Mococo) | — | Lethal Company with Koyori (2024); Phasmophobia with Polka (2023) | [FUWAMOCO cards] |
| Takane Lui | — | Virtual-On and mahjong off-collabs (2025-03-14, 2025-04-01, the mahjong with Mio); Galaxy Burger with Mio and Okayu (2024); a ZIGZAG dance short (2025) | [FB4 AnhxVnLpGR0, 80Se1st9Zyk, YT4yL2_3-Rw, 7cseBNYCrkM] |
| La+ Darknesss | — | "インターネットサバイバー" featuring La+ (2023); the m HOLD'EM roster with Suisei and Botan (2024) | [FB4 g_6-sM3t760] [La+ card] |
| Hoshimachi Suisei | — | A watch-along of Suisei's Budokan live (2025-02-01); the m HOLD'EM roster (2024) | [FB4 XYztoXM9Xiw] [Suisei card] |
| AZKi | — | Overcooked! 2 with Omaru Polka (2023-05-03) | [FB4 iiBvt2jd8ro] |
| Shirogane Noel, Kazama Iroha | — | A cup-noodle tasting with Aki Rosenthal (2024-05-17); #めぇぷるしろっぷう with Iroha and Tsunomaki Watame (2023) | [FB4 fQmhewlBr80, s18jJY5MbzM] |
| Mori Calliope, Ninomae Ina'nis | — | HOLO ENGLISH LESSON #01 (2022-02-19) | [Calli and Marine cards] |
| Koganei Niko, Rindo Chihaya, Isaki Riona | Senpai | Phasmophobia with Niko and Chihaya (2025-04-20); a Mario Party with Niko and Riona (2026); FLOW GLOW's profiles predicted before their debut (2024) | [FB4 yVdTbPCJytw, iJpIGu5HuGY] [Niko card] |

## Arc
- **Starting point:** active at the 2026 baseline, eight years in: an album, a first solo live, birthday 3D lives
  and a new original ("FOXXXROOM") in October 2026.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a new collab group every week; a "delusion profile" that turns out embarrassingly accurate; a
  cat joke at the wrong moment; Kurokami Fubuki saying what Fubuki won't.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Fubuki has to MC an event alone, and Vice-Manager Unicorn's advice is all corn puns.
  2. A kouhai calls her a cat on her first day, and Fubuki must decide whether to bring out the wrestling moves.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2018-06-01; hololive 1st generation and hololive GAMERS; birthday 5 October; 155 cm; illustrator Nagishiro
  Mito; fans Sukonbu (すこん部); tags #フブキch, #絵フブキ; fan mark a corn; first album FBKINGDOM "Blessing"
  (2025-01-15); first solo live FBKINGDOM "ANTHEM" (2025-02-13, Pia Arena MM).

## Sources (checked 2026-11-27)
- FB1 Official profile (English; text, data, Q&A and gallery):
  https://hololive.hololivepro.com/en/talents/shirakami-fubuki/
- FB2 Official profile (Japanese; tagline and Q&A): https://hololive.hololivepro.com/talents/shirakami-fubuki/
- FB3 Official music: https://hololive.hololivepro.com/en/music/014/ (FBKINGDOM "Blessing," 2025-01-15), …/831/
  ("FOXXXROOM," 2026-10-06), …/839/ ("Kami-Tsumo Dora Dora Densetsu," with Aki Rosenthal, Houshou Marine and Ichijou
  Ririka, 2026-11-05), …/383/, …/705/ and …/864/ (AyaFubuMi, 2024-01-02, 2026-03-21, 2026-11-14), …/708/ ("Vivid
  Stampede!!!!," BAKATARE CIRCUS, 2026-02-21), …/737/ ("KemomomomomoMof！," NYANGUCORN, 2026-04-02), …/654/ and …/658/
  (Magical Girl holoWitches!, 2025-10-18 and 10-25), …/420/ and …/591/ (GAMERS)
- FB4 Her channel's archive metadata (archive.ragtag.moe; titles): 0kjXUGCIoZU, GSMyPNRANvc, avWvfYnaOQE,
  _vvbn7kgqj4, gbCsK3KnVVE and zTD4n-B41u4 (the audio windows), qvIZWqp-TMY, az_1XUeg_CU and dB3MemZf6AI (Kurokami),
  pra4uMLmucA, IDX0gKhahFg, ta-ajhcaz7Q, JPnG3WsdSp8, tnOsA0krATc and Dc8pLckDSYQ (outfits), c2hbKnXIa_c,
  7995orE5Enc, I7CY960FEPo, -a68MSMFuuM, 0RG7iNERF4s, n7ZLEzbubJs, w07Qooj0L_c and 62AgiXDP3tU (songs and lives),
  q7323AMTEk4, iJpIGu5HuGY, -pAnDesg9A4 and yVdTbPCJytw (newcomers), rP9TVq9WhdQ and uUFOhSEntNQ (Mio),
  DNIi7lJ58Z8, 9VUUpT_Ta7k and -6YJuLPnnTM (Okayu), -6xMbpbxuyc and BgV_YObYXYM (Korone), eB_t5BRj--c (Ayame),
  pmMqFJm9bHc, LR9JXY2c7xI and U33SciUF0WQ (Marine), cFwsRVbUQaQ, 8dZ9atjf4WA, KtzsKY807hY and Rfq9c8h3LPY (Koyori),
  AnhxVnLpGR0, 80Se1st9Zyk, YT4yL2_3-Rw and 7cseBNYCrkM (Lui), g_6-sM3t760 (La+), XYztoXM9Xiw (Suisei),
  iiBvt2jd8ro (AZKi), fQmhewlBr80 and s18jJY5MbzM (Noel, Iroha)
- FB6 Official announcement of the first solo live (2024-11-08): https://hololivepro.com/news_en/20241108-01-130
- FB7 Live report (secondary news, Famitsu, February 2025): https://www.famitsu.com/article/202502/33968
- FB20 Claude's audio check (two-model ASR, Japanese): research/audio-check/gamers.md

## [SW] Name
Shirakami Fubuki

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 1st Generation, hololive GAMERS, FubuMio, AyaFubuMi, FAMS, OKFAMS, NYANGUCORN, BABACORN, Bakatare-domo, holoWitches

## [SW] Other Names
Fubuki, Fubu-chan, Shirakami, 白上フブキ

## [SW] Personality
Her official profile presents Fubuki as a white-haired, animal-eared otaku fox who loves talking with people, is happy when someone gives her the time of day, and aims to become a top otaku idol while enjoying every day. On stream she is quick, chatty and well organized, calls herself "Shirakami," and has a vocabulary of her own: "Hi, Friends!" (and "Friends!" when someone says "Wife"), "F" at a game over, and gruff "-jai!" and "-yanke!" endings for comic effect. She is a fox, not a cat: the cat joke is fine when she acts cat-like, but out of the blue it earns a threat of pro-wrestling moves. A generous senpai, she guesses new groups' profiles before their debut, watches their first streams and tells newcomers to stream their own way. Her rude alter ego, Kurokami Fubuki, says what she won't. Her fans are the Sukonbu.

## [SW] Background
Fubuki is an active member of hololive's 1st generation and of hololive GAMERS. She has no supernatural abilities; her lore is a performed persona. She debuted on 2018-06-01 and joined GAMERS when the unit was introduced in December 2018. Her alter ego Kurokami Fubuki began her own streams in 2019, and Fubuki has added outfits, originals and collab groups ever since: FubuMio with Ookami Mio, AyaFubuMi with Mio and Nakiri Ayame, NYANGUCORN with Nekomata Okayu and BABACORN with Houshou Marine. Her birthday 3D lives grew into "FBKINGDOM": the 2024 one was billed as its prologue, her first album, FBKINGDOM "Blessing," came out on 2025-01-15, and her first solo live, FBKINGDOM "ANTHEM," followed on 2025-02-13 at Pia Arena MM. In 2026 she celebrated her birthday with the 3D live 「ふぉっくするーむ!!」 and the original "FOXXXROOM," and sang "Kami-Tsumo Dora Dora Densetsu" with Aki Rosenthal, Marine and Ichijou Ririka.

## [SW] Physical Description
Fubuki's avatar is 155 cm, with long white hair and a small side braid, white fox ears with black inner tufts, cyan eyes and a white fox tail that darkens to black at the tip. Original outfit: a white open-front top with a black-lined sailor collar and a light-blue neckerchief, detached wide sleeves tied with blue ribbons, a bare midriff, black shorts, one black thigh-high and one thigh strap, and black slouch boots. Other outfits in the official gallery: First new outfit (2019): a black headband, an oversized off-white top with a big bow, a dark-green frilled skirt; Hakama outfit: a red flower ornament, blossom-patterned blue sleeves and hakama; "TEK" outfit: a white technical coat with a fur-trimmed hood, a white scarf, long blue ribbons; Western-style outfit: a tiny top hat, a navy gold-trimmed coat dress, a blue rose; Hoodie-and-glasses outfit: black glasses, a black zip hoodie, hamburger slippers; Apron-and-pass outfit (2024): looped braids, teal clover sleeves, a white apron, a lanyard pass; Royal outfit (2025): a small gold crown, a navy coat with epaulettes, a red-lined white fur mantle; School-style outfit: a knit vest, a mustard tie, a navy plaid skirt.

## [SW] Dialogue Style
Streams in Japanese, fast and well organized, with English bits. She calls herself "Shirakami," greets with 「こんこんきーつね！白上フブキです！」 or "Hi, Friends!", and has set words for every moment (「はじまんぼう」 to start, "F" at a game over, 「おつこーん」 to end). Comic indignation comes out as gruff 「～じゃい！」 and 「～やんけ！」 endings. She closes in an orderly way: 「ということで、今日はこの辺りで終わっていこうと思います」, then 「ではでは」. With kouhai she is warm and sincere. No regional accent is assigned. When a story renders her speech in English or Chinese, keep the quick, friendly chatter, the self-mocking "Shirakami" and the comic gruffness.

## [SW] Catchphrases
「こんこんきーつね！白上フブキです！」 ("Good foxy day! I'm Shirakami Fubuki!", official); "Hi, Friends!" (her signature greeting; "Wife?" "Friends!"; "WIFriends"); 「おはこん」, 「ひるこん」, 「よるこん」 (morning, noon and evening greetings); 「はじまんぼう」 / 「はじまんた」 (to start a stream); 「おつこーん」 (her sign-off); "F" and "R.I.P." (a game over); 「～じゃい！」 / 「～やんけ！」 (her verbal habits); 「キツネです！」 ("I'm a fox!", to 「ねこやんけ」); 「といったところで」 ("with that said," her closing); "Sukonbu" (すこん部, her fans).

## [SW] Voice & Delivery
Direction for an original designed voice: a bright, clear, high voice; quick and lively, organized like an MC; dropping into a gruff, comic register for 「～じゃい！」; warm and sincere with kouhai; deadpan for "F," then laughing. Not as default: a slow, sleepy drawl, an aloof coolness or Kurokami's rough voice.

## [SW] Audio Tags
Dialogue language for audio scripts: Japanese. Write her spoken turns in Japanese script; romaji and English go only on ROMAJI/GLOSS lines. ElevenLabs v4 performance directions for an original designed voice; never imitate the real member. Register: bright, clear, high voice; quick and lively. Default tags: [cheerful, energetic]. By situation: opening [bright, upbeat]; called a cat [indignant, comic]; game over [deadpan]; advising kouhai [warm, sincere]; closing [warm, orderly]; FBKINGDOM stage [regal, playful]. With people: Mio [playful, affectionate]; Okayu [teasing]; Marine [rowdy]; kouhai [encouraging]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs] (tag only). Keep in the words: 「白上」 (Shirakami), 「こんこんきーつね」 (konkon kītsune), 「すこん部」 (Sukonbu), "Hi, Friends!" Reading: しらかみ ふぶき. No regional accent is assigned. Not as default: a sleepy drawl or a cold, aloof read.

## [SW] Motivation
In her lore, Fubuki is an otaku fox who wants to become a top otaku idol while enjoying every day. As a streamer and singer, she wants to hold lots of concerts with the other members, get more MC experience, do lots of fun things with her fans and welcome new kouhai.

## [SW] Relationships
hololive GAMERS (Ookami Mio, Nekomata Okayu, Inugami Korone): her unit; her "ワンダーフューチャー！" features all three (2025). Ookami Mio: FubuMio; they predicted FLOW GLOW's profiles before their debut (2024); AyaFubuMi with Nakiri Ayame (three originals, 2024–2026). Nekomata Okayu: NYANGUCORN ("KemomomomomoMof！," 2026). Inugami Korone: #フブころちゃん and a Mario Maker course for Korone's sixth anniversary (2025). Nakiri Ayame: AyaFubuMi and FAMS; Fubuki created Ayame's companion Poyoyo. Houshou Marine: BABACORN; "Kami-Tsumo Dora Dora Densetsu" (2026). Hakui Koyori: #こんこんこよーて New Year card-pack openings; Lethal Company with FUWAMOCO (2024); White Cat Golf with Koyori and Yukihana Lamy (2022). FUWAMOCO: horror and Lethal Company partners. Shishiro Botan: Content Warning with Marine (2024) and EDF5 with Koyori (2022). Takane Lui: Virtual-On and mahjong off-collabs (2025). La+ Darknesss: "インターネットサバイバー" featuring La+ (2023). Hoshimachi Suisei: watched Suisei's Budokan live with her viewers (2025). AZKi: Overcooked! 2 (2023). Shirogane Noel and Kazama Iroha: a cup-noodle tasting (2024). Mori Calliope: a guest in Calli's HOLO ENGLISH LESSON #01 with Marine (2022). Koganei Niko and Rindo Chihaya: Phasmophobia (2025); Isaki Riona: a Mario Party with Niko (2026).

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Voice & Delivery and Audio Tags are performance directions for an original designed voice. Timbre, laughter and
  delivery are design choices unless a listening source is named in the Voice Profile; ASR supports wording, not
  vocal quality or recurrence; partner tags are optional scene directions, not observed defaults; the kana reading
  is untested; recorded pitch and speaking-rate figures are research context only, never synthesis targets.
- The tagline, the stream vocabulary (はじまんぼう, おはこん, おつこーん, "Hi, Friends!", "F," ～じゃい, ～やんけ), the cat
  joke, Kurokami Fubuki, Vice-Manager Unicorn and the mascots: the official profile's Q&A (English and Japanese).
- 「といったところで」, 「ということで、今日はこの辺りで終わっていこうと思います」, 「ではでは」, 「今日もありがとうございました」 and the
  advice to newcomers: both ASR models (spelling differences only; see FB20). "Hi, Friends!" and "otsukon" in her
  streams: near-matches in both models, so the card uses the official spellings. 「こんばんきーつね」: the second model
  only.
- The newcomer streams: archived titles (ReGLOSS 2023, FLOW GLOW 2024, アソビ★まわり隊 2026).
- FubuMio, NYANGUCORN, BABACORN, AyaFubuMi, FAMS: official music credits, the official Q&A or archived titles.
  "Bakatare-domo" (バカタレ共, with Shiranui Flare and Tsunomaki Watame): the official Q&A. The m HOLD'EM roster: the
  Suisei, La+ and Botan cards (a publisher roster; a joint broadcast is not established).
- Outfits: Claude's reading of the official gallery images. Dates rest on thumbnails or silhouettes as stated in
  each label; the "TEK" and "Western-style" names come from her stream titles.

## Merge Record
- **2026-11-27, Claude only (author order: complete hololive GAMERS):** official profiles (with the Q&A), gallery and
  music pages, archive metadata and a two-model ASR check (FB20). Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. Her spoken 「こんこんきーつね」 was not captured by both models in the checked windows (the openings are partly
   covered by music); the card relies on the official profile.
2. Reveal dates for the hakama, hoodie-and-glasses and school-style outfits, and the first reveal of the "TEK" outfit,
   are not established here.
````

### FILE: `bible/characters/Ookami-Mio.md`

````markdown
---
kind: character
name: "Ookami Mio"
sw_section: Characters
---

# Character File: Ookami Mio

> Scope: official lore and publicly shown persona only, checked 2026-11-27. Mio is an active member of hololive
> GAMERS at the 2026-09-30 baseline; added to the cast by author order (2026-11-27: complete hololive GAMERS). Her
> recent streams (2026) set her default manner, per the project's recency rule. Nothing about the performer behind
> the avatar: private-life information (family, home, health, daily routine, sleep, travel, where she streams from
> and the like) is outside scope and is not recorded here, including what she mentions in chats and stream titles.
> She streams in Japanese. In stories she knows she is a streamer with a persona (see the world card "VTuber Persona
> and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title, description or post; "(secondary)" means the wording comes from a news
>   report or another secondary source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; MI20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (MI#) are listed under Sources.
>
> **Audio status:** on 2026-11-27 Claude checked two archived 2026 streams, a #朝ミオ morning show and a quiet
> late-night chat (MI20, research/audio-check/gamers.md). Personal remarks are not quoted or summarized here. The
> audio was machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
「こんばんみぉーん！大神ミオだよ～！」 ("Hellooowl! It is Ookami Mio!", official): a black-haired wolf girl who
turned up from nowhere, haunts shrines and loves games; GAMERS' calm, steady centre, who reads the whole cast's
fortunes with tarot every New Year and has hosted a Monday-morning show, #朝ミオ, since 2021. [Official MI1, MI2]
[MI4] [ASR MI20]

## Core Drive
- **Want:** to share good times with her fans, the Mio-fam, through songs, games and a regular morning show; her
  anniversaries are celebrated with concerts and albums ("Night walk," 2023; "My Sparkle," 2025). [Official MI3]
  [MI4]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** she calls her horror playthroughs 「本当に怖い」 ("really scary") in the titles
  and plays them anyway (BIOHAZARD RE:2, 2026). [MI4]
- **Values shown in public:** her fans; GAMERS and her long collab partners (Fubuki above all, as FubuMio); keeping
  each show's corners and rituals. [MI4] [MI5] [ASR MI20]

## Core Contradiction
A mysterious shrine wolf who "appeared from nowhere" and plays a grand fortune-teller, "Big God Mion"
(ビッグゴッドミオーン), yet her default voice is the gentle, steady one that greets the week every Monday morning,
reads out her viewers' posts and wishes them a good day. [Official MI1] [MI4] [ASR MI20]

## Behavioral Traits
1. Calls herself 「うち」 (uchi): about twenty times in four transcribed windows; her greeting stacks it,
   「うちうち、うちだよ」 (written in a 2021 stream title; heard by the second model in both 2026 openings). [MI4
   ZlefjbcT758] [ASR MI20]
2. #朝ミオ ("Morning Mio"), her Monday-morning show since early 2021 (a first-anniversary episode in 2022; more
   than two hundred archived episodes): she opens with 「おはみぉーん！」, reads viewers' posts on a weekly theme
   (for example favourite ramen, photos welcome) and closes by wishing everyone a good day. [MI4 yF3tD2_waP4,
   v49bZ8yH0I0] [ASR MI20]
3. A fortune-teller bit: "Big God Mion's House of Fortunes" (ビッグゴッドミオーンの占いの館), tarot readings for
   callers and an every-New-Year reading of hololive members (2020 onward; a 2025 call-in edition). [MI4
   w-Mv31HMwLk, 6l32Ku8bSAU, 77ft8GAGq2w]
4. Singing streams (more than a hundred archived 歌枠) and long-running Minecraft; in 2026 she plays Pawapro's
   high-school baseball mode as "群馬県わおーん高校" (#ホロ甲2026), a horror run of BIOHAZARD RE:2 and the hololive
   card game #ホロドリ. [MI4]
5. Calm late-night chats (a 2026-09-18 chat billed as quiet, "for late night"): an unhurried, low-key voice. [MI4
   3b1W_NGeIgs] [ASR MI20]
6. FubuMio: she and Fubuki predicted FLOW GLOW's profiles before their debut (#フブミオ大予想, 2024-11-09) and hold
   joint announcements (#フブミオ重大告知, 2026-04-21). [MI5 iJpIGu5HuGY, uUFOhSEntNQ]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: 「こんばんみぉーん！大神ミオだよ～！」 / "Hellooowl! It is Ookami Mio!" [Official MI1, MI2]
  - Morning: 「おはみぉーん！」 (written in more than a hundred of her stream titles; both ASR models heard a near-match,
    おはみよ / オハ見用); her stacked 「うちうち、うちだよ」 (written in a 2021 title; the second model heard it in both 2026 openings) and
    「大神ミオだよ」. [MI4] [ASR MI20]
  - Sign-off: 「それではまた明日ねー」 ("well then, see you tomorrow"; shared span, 2026-10-11), and after a late chat
    「また明日会いましょう、じゃあねー」 ("let's meet again tomorrow, bye"; shared span, 2026-09-18), each followed by
    a coined "otsu-mion" (both models heard a near-match, おつみよう / おつみよー, so it is given in romaji, not as a
    verified quotation). [ASR MI20]
- **Catchphrases & bits:** 「おはみぉーん」 / 「こんばんみぉーん」; 「うち」; "Big God Mion" and her House of Fortunes;
  #朝ミオ; Mio-fam (ミオファ, short for みおーんファミリー) for her fans; #ミオかわいい (streams), #みおーん絵 (fan art).
  [Official MI1, MI2] [MI4]
- **Vocabulary / fillers:** 「なんか」, 「まあ」, 「ちょっと」, polite 「よろしくお願いします」 in the show's corners
  (first-model observations). [ASR MI20]
- **Profanity:** none observed in the windows checked.
- **Language:** streams in Japanese; a few English loanwords. No regional accent is assigned.
- **Laughs, noises:** a soft laugh is a design choice; no laughter was measured.
- **Rhythm & rhetoric:** even and conversational; a morning-radio structure (opening, corner, theme for next week,
  goodbye). [ASR MI20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (MI20): in a 2026 morning show, median about 248 Hz (p10–p90 about 130–446 Hz) and about 271 characters
    a minute of speech in its closing talk; in a deliberately quiet late-night chat, median about 197–203 Hz (p10–p90
    about 164–282 Hz) and 276–305 characters a minute. Measurements describe the archived audio, not a target to
    clone.
  - Provisional (interpretation): a warm, mellow mid-range voice, gentle and composed, brightening when she sings or
    plays.
- **Sounds off:** a shrill, hyper idol voice as her default; a cold, clipped voice; frantic speed.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Morning show opening | Bright, unhurried | 「おはみぉーん！」 (her titles) |
| Reading viewers' posts | Warm, attentive | **Style demo:** 「おー、おいしそう！ありがとう〜」 ("Ooh, that looks tasty! Thank you~") |
| Tarot reading | Hushed, grand, playful | **Style demo:** 「ビッグゴッドミオーンが占ってしんぜよう」 ("Big God Mion shall read your fortune") |
| Horror game | Tense, startled | **Style demo:** 「待って待って、こわいこわい！」 ("Wait, wait, scary, scary!") |
| Saying goodbye | Gentle | 「それではまた明日ねー」 (ASR MI20) |

### Sample Lines
1. 「こんばんみぉーん！大神ミオだよ～！」 (konbanmyōn! Ōkami Mio da yo~!, "Hellooowl! It's Ookami Mio!") (Official MI2)
2. 「それではまた明日ねー」 (soredewa mata ashita ne, "Well then, see you tomorrow") (ASR MI20, October 2026)
3. 「また明日会いましょう、じゃあねー」 (mata ashita aimashō, jā ne, "Let's meet again tomorrow. Bye!") (ASR MI20,
   September 2026)

## Appearance Anchors (avatar)
160 cm; illustrator Izumi Sai (泉彩). Long black hair with a red streak and a yellow-orange hair clip, black wolf
ears with white inner fur, amber eyes and a large black wolf tail with a white tip. The official profile gallery
(checked 2026-11-27) shows eight outfits; descriptions are Claude's reading of those images:
- **Original outfit** (gallery 01–02): a red choker; a black sleeveless crop top with a white sailor collar and a
  red tie; detached black sleeves lined in red; a twisted white-and-red rope with gold bells; a black pleated skirt
  with red lacing and purple flower prints; white thigh-highs tied with red ribbons; black thong sandals with red
  straps. [Official MI1 gallery]
- **Hoodie outfit (room wear; a 2022-01-09 morning show revealed its "2.0" version, and the title and thumbnail
  art match)** (gallery 03): red-rimmed glasses, a black choker, a white-and-black split hoodie with white paw prints,
  black shorts, black tights and white sneakers with red laces. [Official MI1 gallery] [MI4 Wfp02kj-7Qk]
- **Japanese-style maid outfit** (gallery 04): a frilled white maid headdress, round glasses, a high ponytail tied
  with a red ribbon, a red kimono with pink cherry blossoms under a white frilled apron, cuffs tied with red cord,
  black tights and brown boots. [Official MI1 gallery]
- **Autumn casual outfit** (gallery 05): a navy beret, a single braid, a white lace-collared blouse, a beige knit
  cardigan, a navy skirt with a red stripe and brown ankle boots. [Official MI1 gallery]
- **Playing-card outfit (revealed 2022-12-06; the reveal silhouette's twin tails and bow match)** (gallery 06): twin
  tails with a red-and-white bow and a red rose, a red ruffled collar with a black lace choker, white puff sleeves, a
  red bustier and a black corset laced in gold, long black gloves, a skirt hem hung with playing cards and black
  thigh-high boots. [Official MI1 gallery] [MI4 Wjxkl2m9zro]
- **Hooded outfit** (gallery 07): a black hood with wolf ears lined in red, a black crop top with a white sailor
  collar and red neckerchief, a black jacket with wide sleeves and red-and-white tassels, black shorts with red
  lacing, a leg band, white slouch socks and black shoes. [Official MI1 gallery]
- **Green capelet outfit** (gallery 08): a green capelet with gold paw buttons and a black bow, a grey ruffled blouse
  with black ribbon ties on the sleeves, a green skirt with a grey plaid panel, black tights and black shoes.
  [Official MI1 gallery]
- **School-style outfit** (gallery 09): a brown cable-knit sweater with a crest badge and star pins over a white
  collar and mustard tie, a red plaid pleated skirt with a chain and a small purple plush charm, black tights and
  brown lace-up boots. [Official MI1 gallery]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2018-12-06 | hololive GAMERS unit video | [GAMERS card G2 DPZbSlHcdfo] |
| 2018-12-07 | Debut | [Official MI1] |
| 2019-06-16 | 3D debut stream | [MI4 T-4B_hiiRlQ] |
| 2020-10-30 | Model "version 2.0" | [MI4 wTWaEyojbgY] |
| 2020-12-07 | Second-anniversary 3D live | [MI4 mmUVwNut2-Y] |
| 2021 | #朝ミオ begins (first-anniversary episode in February 2022) | [MI4 yF3tD2_waP4] |
| 2022-12-06 | Playing-card outfit revealed | [MI4 Wjxkl2m9zro] |
| 2022-12-07 | Fourth-anniversary live, "Mio Forest night party," and the original "夜光通信" | [MI4 0WLlmgirGD8, eZWjYWcQ4Xo] |
| 2023-12-07 | Fifth-anniversary live "ナイトループ" and first album "Night walk" | [MI4 YqPVwYLcvrY] [Official MI3] |
| 2024-01-02 | "OniOniKonKonWaon" with Fubuki and Ayame (AyaFubuMi) | [Official MI3] |
| 2024-05-22 | "We are GAMERS!!!!" | [Official MI3] |
| 2024-08-20 | 3D birthday live, "晴れ時々にわかミオ" | [MI4 VzecQUmB1sY] |
| 2024-11-09 | #フブミオ大予想: FLOW GLOW's profiles predicted before their debut, with Fubuki | [MI5 iJpIGu5HuGY] |
| 2024-12-21 | AyaFubuMi year-end nabe party and the "不純矛盾" cover | [MI4 KEArX1o9sEY, ShGnwuuTMIM] |
| 2025-02-07 | Mochi-pounding off-collab with FUWAMOCO | [MI4 fQaE6-usUjg] |
| 2025-07-03 | "To Be Continued…." (GAMERS) | [Official MI3] |
| 2025-08-20 | Second album, "My Sparkle" | [Official MI2 news, MI3] |
| 2025-09-10 | First solo live, "Our Sparkle" (Pia Arena MM) | [Official MI2 news] [MI4 DsASp5oBG4M] |
| 2026-03-21 | "Irowanioedomo" (AyaFubuMi) | [Official MI3] |
| 2026-07-03/04 | Serendipity concert: "Night Loop" with IRyS and Koseki Bijou; "Dottabatta Chindouchuu" with Ninomae Ina'nis and FUWAMOCO | [Official MI6] |
| 2026-09-21 | RosaMiA (with Aki Rosenthal and AZKi): "Blossom Sinfonia" | [Official MI3] [AZKi card] |
| 2026-11-14 | "Gokuraku Gokigen Enbiyori" (AyaFubuMi) | [Official MI3] |
| 2026-11-21 | Single "Beginner's High" | [Official MI3] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Shirakami Fubuki, Nekomata Okayu, Inugami Korone | GAMERS unitmates | Unit songs ("We are GAMERS!!!!," "To Be Continued…."); "ワンダーフューチャー！" (Fubuki feat. the other three, 2025) | [Official MI3] [GAMERS card] |
| Shirakami Fubuki | "FubuMio" | #フブミオ大予想 (2024-11-09), We Were Here Expeditions (2024-04-25), #フブミオ重大告知 (2026-04-21); Mio watched Fubuki's first solo live with her viewers (2025-02-13) | [MI5 iJpIGu5HuGY, rP9TVq9WhdQ, uUFOhSEntNQ] [MI4 TzrX8eBHEGQ] |
| Nekomata Okayu | "MiOKayu" covers; "OKFAMS" | "神或アルゴリズム" (2025-08-21); "Monster" as OKFAMS (2021); a watch-along of Okayu's solo live (2022) | [MI4 grN8TN-eLk4, cbKfZy5Jpgk, WmGPYGBzCv4] |
| Inugami Korone | #ふたりは神様MaxDOG (GAMERS card) | Korone held a Mio-only call-in for Mio's sixth anniversary (2024-12-09) | [MI5 5t4dWBqm07M] |
| Nakiri Ayame | "AyaFubuMi" with Fubuki | "OniOniKonKonWaon" (2024), "Irowanioedomo" and "Gokuraku Gokigen Enbiyori" (2026); a 2024 nabe party; the 2025 anime opening; Anime NYC 2026 | [Official MI3] [MI4] [Ayame card] |
| AZKi | RosaMiA with Aki Rosenthal | Mio's first GeoGuessr with AZKi (2024-12-29); a marshmallow chat (2025-08-18); "Blossom Sinfonia" (2026) | [MI4 GDOn9JNBAGA, cX-Wir_k3cE] [Official MI3] |
| Takane Lui | — | holoGTA (2024-09-20); a ZIGZAG dance short together (2025-08-18) | [MI4 UX52XaorEfY, Rjwd8WGH2kY] |
| FUWAMOCO (Fuwawa, Mococo) | — | Mochi-pounding off-collab (2025-02-07); "Dottabatta Chindouchuu" with Ina at Serendipity (2026) | [MI4 fQaE6-usUjg] [Official MI6] |
| IRyS, Koseki Bijou | — | "Night Loop" together at Serendipity (2026) | [Official MI6] |
| Ninomae Ina'nis | — | "Dottabatta Chindouchuu" at Serendipity (2026) | [Official MI6] |
| Hakos Baelz | — | Bae's joking "moms" bit names Mio (secondary, on Bae's card) | [Bae card, secondary] |

## Arc
- **Starting point:** active at the 2026 baseline, nearly eight years in: two albums, a first solo live (2025), a
  new single in November 2026, and a morning show still running.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a tarot reading whose result everyone takes far too seriously; a Monday-morning theme that
  floods her with viewers' photos; a baseball save file she refuses to reset.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Big God Mion reads Fubuki's fortune live, and the cards keep predicting disaster.
  2. A #朝ミオ guest shows up unannounced, and Mio has to run the corner as a two-person radio show.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2018-12-07; hololive GAMERS; birthday 20 August; 160 cm; illustrator Izumi Sai; fans Mio-fam (ミオファ);
  tags #ミオかわいい, #みおーん絵; albums "Night walk" (2023) and "My Sparkle" (2025); first solo live "Our Sparkle"
  (2025-09-10).

## Sources (checked 2026-11-27)
- MI1 Official profile (English; text, data and gallery): https://hololive.hololivepro.com/en/talents/ookami-mio/
- MI2 Official profile (Japanese; tagline, and the news items listed on it: the second album and "Our Sparkle,"
  2025-03-13; the solo-live venue, 2025-05-04): https://hololive.hololivepro.com/talents/ookami-mio/
- MI3 Official music: https://hololive.hololivepro.com/en/music/353/ ("Night walk," 2023-12-07), …/018/ ("My
  Sparkle," 2025-08-20), …/447/ ("Shoushin Ryokou," 2024-08-21), …/798/ ("Beginner's High," 2026-11-21), …/813/
  ("Blossom Sinfonia," RosaMiA, 2026-09-21), …/420/ ("We are GAMERS!!!!," 2024-05-22), …/591/ ("To Be Continued
  . . . .," 2025-07-03), …/383/, …/705/ and …/864/ (AyaFubuMi, 2024-01-02, 2026-03-21, 2026-11-14)
- MI4 Her channel's archive metadata (archive.ragtag.moe; titles): v49bZ8yH0I0 and 3b1W_NGeIgs (the audio windows),
  ZlefjbcT758 (a 2021 title written 【うちうち、うちだよ】), T-4B_hiiRlQ (3D debut), wTWaEyojbgY (2.0), mmUVwNut2-Y, 0WLlmgirGD8,
  eZWjYWcQ4Xo, YqPVwYLcvrY and VzecQUmB1sY (lives and songs), yF3tD2_waP4 (#朝ミオ anniversary), Wfp02kj-7Qk and
  Wjxkl2m9zro (outfit reveals), w-Mv31HMwLk, 6l32Ku8bSAU and 77ft8GAGq2w (fortune-telling), DsASp5oBG4M ("Our
  Sparkle" announcement), KEArX1o9sEY and ShGnwuuTMIM (AyaFubuMi), GDOn9JNBAGA and cX-Wir_k3cE (AZKi), fQaE6-usUjg
  (FUWAMOCO), UX52XaorEfY and Rjwd8WGH2kY (Lui), grN8TN-eLk4, cbKfZy5Jpgk and WmGPYGBzCv4 (Okayu), TzrX8eBHEGQ
  (Fubuki's solo live watch-along)
- MI5 Other channels' archive metadata: iJpIGu5HuGY (#フブミオ大予想), rP9TVq9WhdQ and uUFOhSEntNQ (FubuMio), on
  Fubuki's channel; 5t4dWBqm07M (Korone's call-in for Mio's sixth anniversary)
- MI6 Official Serendipity concert report: https://hololive.hololivepro.com/en/events/serendipity/
- MI20 Claude's audio check (two-model ASR, Japanese): research/audio-check/gamers.md

## [SW] Name
Ookami Mio

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive GAMERS, FubuMio, AyaFubuMi, FAMS, OKFAMS, RosaMiA

## [SW] Other Names
Mio, Mio-sha, Big God Mion, 大神ミオ

## [SW] Personality
Her official profile presents Mio as a black-haired wolf girl who appeared from nowhere, often shows up around shrines and loves games. On stream she is the calm, steady centre of hololive GAMERS: gentle, composed and quietly funny, the voice that greets the week on her Monday-morning show, reads out her viewers' posts and wishes them a good day. She calls herself "uchi." She plays a grand fortune-teller, "Big God Mion," who reads tarot for callers and for the whole of hololive every New Year. She sings often, plays long games (Minecraft, a high-school baseball save she runs as "Gunma Waon High"), and calls her horror playthroughs "really scary" before playing them anyway. With Shirakami Fubuki she is half of FubuMio, and she sings with Fubuki and Nakiri Ayame as AyaFubuMi. Her fans are the Mio-fam.

## [SW] Background
Mio is an active member of hololive GAMERS. She has no supernatural abilities; her lore is a performed persona. She debuted on 2018-12-07, the day after the GAMERS unit video, and joined Shirakami Fubuki, later Nekomata Okayu and Inugami Korone, in the unit. Her 3D debut came in 2019, and her Monday-morning show, #朝ミオ, began in 2021. She marked her anniversaries with concerts and originals, released her first album, "Night walk," on 2023-12-07 and her second, "My Sparkle," on 2025-08-20, and held her first solo live, "Our Sparkle," on 2025-09-10. With Fubuki and Nakiri Ayame she sings as AyaFubuMi, and at the 2026 Serendipity concert she sang with IRyS, Koseki Bijou, Ninomae Ina'nis and FUWAMOCO. Her single "Beginner's High" followed on 2026-11-21.

## [SW] Physical Description
Mio's avatar is 160 cm, with long black hair streaked red, a yellow-orange hair clip, black wolf ears with white inner fur, amber eyes and a big black wolf tail tipped white. Original outfit: a red choker, a black crop top with a white sailor collar and red tie, detached black sleeves lined red, a white-and-red rope with gold bells, a black pleated skirt with red lacing, white thigh-highs tied with red ribbons and black sandals with red straps. Other outfits in the official gallery: Hoodie outfit (room wear): red-rimmed glasses, a white-and-black hoodie with paw prints, black shorts; Japanese-style maid outfit: a frilled maid headdress, round glasses, a red cherry-blossom kimono under a white apron; Autumn casual outfit: a navy beret, a single braid, a beige cardigan over a white blouse; Playing-card outfit (2022): twin tails with a red-and-white bow and rose, a black corset laced in gold, a skirt hem hung with playing cards; Hooded outfit: a wolf-eared black hood, a sailor-collared crop top, a wide-sleeved jacket with tassels; Green capelet outfit: a green capelet with paw buttons over a grey blouse; School-style outfit: a brown sweater, a mustard tie, a red plaid skirt.

## [SW] Dialogue Style
Streams in Japanese in a warm, even voice: "uchi" for "I," gentle polite phrasing in her show's corners, and calm, unhurried late-night talk. She opens with 「おはみぉーん！」 in the morning or 「こんばんみぉーん！大神ミオだよ～！」 at night, stacking 「うちうち、うちだよ」 (written in her titles) before her name, and closes with 「それではまた明日ねー」 ("see you tomorrow") and a coined "otsu-mion." As Big God Mion she slips into a grand, playful oracle voice. No regional accent is assigned. When a story renders her speech in English or Chinese, keep the gentle composure, the "uchi" warmth and the steady radio-host rhythm.

## [SW] Catchphrases
「こんばんみぉーん！大神ミオだよ～！」 ("Hellooowl! It is Ookami Mio!", official); 「おはみぉーん！」 (her morning greeting, written in her titles); 「うちうち、うちだよ」 (written in a 2021 title; "It's me, me, me!"); 「それではまた明日ねー」 ("Well then, see you tomorrow"); "otsu-mion" (her coined sign-off); "Big God Mion" (ビッグゴッドミオーン, her fortune-teller persona); #朝ミオ ("Morning Mio"); "Mio-fam" (ミオファ, her fans).

## [SW] Voice & Delivery
Direction for an original designed voice: a warm, mellow mid-range voice, gentle and composed; even, conversational pacing like a morning radio host; softer and lower for late-night talk; grand and theatrical as the fortune-teller; bright when she sings or wins; startled squeaks in horror games. Not as default: shrill hyper-idol energy, coldness or frantic speed.

## [SW] Audio Tags
Dialogue language for audio scripts: Japanese. Write her spoken turns in Japanese script; romaji and English go only on ROMAJI/GLOSS lines. ElevenLabs v4 performance directions for an original designed voice; never imitate the real member. Register: warm, mellow mid-range voice; calm by default. Default tags: [warm, gentle]. By situation: morning opening [bright, cheerful]; reading posts [attentive, warm]; tarot reading [mysterious, playful]; horror [nervous]; late-night chat [soft, calm]; saying goodbye [gentle]. With people: Fubuki [playful, teasing]; Korone [amused]; Okayu [relaxed]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs softly] (tag only). Keep in the words: 「うち」 (uchi), 「おはみぉーん」 (ohamyōn), 「ミオファ」 (Mio-fam). Reading: おおかみ みお. No regional accent is assigned. Not as default: a shrill idol voice or a cold, clipped read.

## [SW] Motivation
In her lore, Mio is a wolf girl who appeared from nowhere and keeps watch around shrines. As a streamer and singer, she wants to spend good, steady time with her fans, keep her morning show going and share her songs.

## [SW] Relationships
hololive GAMERS (Shirakami Fubuki, Nekomata Okayu, Inugami Korone): her unit; "We are GAMERS!!!!" and "To Be Continued…." Shirakami Fubuki: FubuMio; they predicted FLOW GLOW's profiles before their debut (2024) and hold joint announcements; AyaFubuMi with Nakiri Ayame ("OniOniKonKonWaon," 2024; "Irowanioedomo" and "Gokuraku Gokigen Enbiyori," 2026). Nekomata Okayu: MiOKayu covers ("神或アルゴリズム," 2025) and OKFAMS. Inugami Korone: "ふたりは神様MaxDOG"; Korone hosted a call-in for Mio's sixth anniversary (2024). AZKi: GeoGuessr (2024), a marshmallow chat (2025) and RosaMiA with Aki Rosenthal ("Blossom Sinfonia," 2026). Takane Lui: holoGTA (2024) and a ZIGZAG dance short (2025). FUWAMOCO: a mochi-pounding off-collab (2025) and "Dottabatta Chindouchuu" with Ninomae Ina'nis at Serendipity (2026). IRyS and Koseki Bijou: "Night Loop" at Serendipity (2026). Hakos Baelz: names Mio in her joking "moms" bit.

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Voice & Delivery and Audio Tags are performance directions for an original designed voice. Timbre, laughter and
  delivery are design choices unless a listening source is named in the Voice Profile; ASR supports wording, not
  vocal quality or recurrence; partner tags are optional scene directions, not observed defaults; the kana reading
  is untested; recorded pitch and speaking-rate figures are research context only, never synthesis targets.
- 「こんばんみぉーん！大神ミオだよ～！」: the official Japanese profile. 「おはみぉーん」: her stream titles (written);
  both ASR models heard a near-match. 「うちうち、うちだよ」 (written: a 2021 title) was heard by the second model in
  both 2026 openings; the first model heard a shorter form in each (see MI20). 「それではまた明日ねー」 and 「また明日会いましょう、じゃあねー」: shared ASR
  spans. "otsu-mion": a near-match in both models, given in romaji.
- "Big God Mion" and the House of Fortunes: stream titles (2019–2025). "Mio-sha": Korone's title for Mio's
  anniversary call-in. "MiOKayu": the Okayu card. "#ふたりは神様MaxDOG": the GAMERS world card.
- The Serendipity stages: the official concert report, as already recorded on the IRyS, Bijou, Ina and FUWAMOCO
  cards. RosaMiA's membership: the AZKi card and the official music page's artist label.
- Outfits: Claude's reading of the official gallery images. The room-wear identification rests on the 2022 title
  and its thumbnail art; the playing-card outfit's date rests on the reveal-stream silhouette.

## Merge Record
- **2026-11-27, Claude only (author order: complete hololive GAMERS):** official profiles, gallery and music pages,
  archive metadata and a two-model ASR check (MI20). Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. The exact start date of #朝ミオ (the first-anniversary episode is dated February 2022).
2. Reveal dates for the other gallery outfits are not established here.
3. A spoken check of 「こんばんみぉーん」 in 2026 (the late-night window's greeting is a near-match in both models).
````

### FILE: `bible/characters/Inugami-Korone.md`

````markdown
---
kind: character
name: "Inugami Korone"
sw_section: Characters
---

# Character File: Inugami Korone

> Scope: official lore and publicly shown persona only, checked 2026-11-27. Korone is an active member of hololive
> GAMERS at the 2026-09-30 baseline; added to the cast by author order (2026-11-27: complete hololive GAMERS). Her
> recent streams (2026) set her default manner, per the project's recency rule. Nothing about the performer behind
> the avatar: private-life information (family, home, health, daily routine, sleep, travel, where she streams from
> and the like) is outside scope and is not recorded here, including what she mentions in chats and stream titles.
> She streams in Japanese. In stories she knows she is a streamer with a persona (see the world card "VTuber Persona
> and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title, description or post; "(secondary)" means the wording comes from a news
>   report or another secondary source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; KO20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (KO#) are listed under Sources.
>
> **Audio status:** on 2026-11-27 Claude checked two archived 2026 streams, the first episode of her morning show
> and a game stream (KO20, research/audio-check/gamers.md). Personal remarks are not quoted or summarized here. The
> audio was machine-transcribed and acoustically measured; transcripts were reviewed in context, without independent
> listening verification.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
「ぉぁょ~！ゆびゆび～」 ("Ello! Fingers! Give me your fingers!", official): a dog from a city bakery who plays games
while minding the shop; GAMERS' tireless player, who clears old games in marathon endurance streams, demands her
viewers' fingers and in 2026 started a morning show of her own. [Official KO1, KO2] [KO4] [ASR KO20]

## Core Drive
- **Want:** to play games to the end, old and new, with her viewers along for the ride; "ド★初見" (completely
  first-time) playthroughs and "クリア耐久" (play-until-cleared) streams fill her archive. [KO4]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** she plays horror often and loudly, in solo runs and in group collabs. [KO4]
- **Values shown in public:** her fans, the Koronesky; GAMERS and Okayu above all (OkaKoro); old consoles and the
  games she grew up with as a persona theme (SEGA, Super Famicom, Saturn). [Official KO1] [KO4]

## Core Contradiction
A bakery shop-dog with a cute, high voice and a lazy morning drawl who turns into an unstoppable marathon gamer:
she will stream a game for most of a day to see the credits. [Official KO1] [KO4] [ASR KO20]

## Behavioral Traits
1. The finger bit: her official greeting asks for fingers (「ゆびゆび～」, "Give me your fingers!"), and her titles
   keep the joke going. [Official KO1, KO2] [KO4]
2. Endurance and retro play: "セガガガ" played until cleared for SEGA's sixtieth anniversary (2020-07-23 and 24,
   two marathon streams), a Super Donkey Kong clear (2024), and in 2026 Saturn Bomberman and a Super Famicom
   platformer, all billed "ド★初見." [KO4 E4yz96XAtdg, M4clvou7I00, 27N1_I21YQo, dQFvlxqx44E, 1IuOKoNqWug]
3. 朝ころ ("Morning Korone"), a morning show begun 2026-05-03, billed 「朝のぉぁょ~！」: she opens with 「はい、
   おはよー」 and ends the first episode by narrating herself in the third person, 「なんか朝枠もいいなって思う
   ころねなのであった」 ("and so Korone thought a morning slot is kind of nice, too"). [KO4 Zlnqxdwg5Io] [ASR KO20]
4. Film work in 2026: narration and commentary for a film promotion (2026-01-14), a talk with Houshou Marine after
   interviewing a film director (2026-03-19) and a review with a director interview (2026-10-06). [KO4 8h60xVu58bM,
   x3V1BH5tT-4, JLALCjMzjTM]
5. "ころね支店" ("the Korone branch"): how she titles her side of a group collab streamed from her channel. [KO4]
6. Anniversary eves with a drink-in-hand countdown (2023, 2025, 2026) and anniversary lives (a fourth-anniversary
   live in 2023; a "3D and puppet live" in 2025). [KO4 sh0j8Fl-wGg, o3JeicqyVG0, ASwjM25ax58]

## Voice Profile
- **Greetings / sign-offs:**
  - Official line: 「ぉぁょ~！ゆびゆび～」 / "Ello! Fingers! Give me your fingers!" [Official KO1, KO2]
  - Morning show: 「はい、おはよー」 ("OK, mornin'"; both models, written おはよう / おはよー), billed 「朝のぉぁょ~！」.
    [KO4] [ASR KO20]
  - Ending: 「楽しかった！」 and the third-person 「なんか朝枠もいいなって思うころねなのであった」 (both models, 2026-05-03;
    one model writes 朝訳 for 朝枠). [ASR KO20]
- **Catchphrases & bits:** 「ゆび」 (fingers); 「ド★初見」; 「ころね支店」; ころさん ("Koro-san," Okayu's name for her,
  also used in titles); Koronesky (ころねすきー) for her fans; #生神もんざえもん (streams), #できたてころね (fan art).
  [Official KO1, KO2] [KO4]
- **Vocabulary / fillers:** 「ちょっと待って」, 「なんか」, 「マジ」, repeated 「待てよ待てよ」 while waiting for a game to
  load (first-model observations). [ASR KO20]
- **Profanity:** none observed in the windows checked.
- **Language:** streams in Japanese; English flourishes in her official English line ("Ello!"). No regional accent
  is assigned.
- **Laughs, noises:** loud, delighted laughter is a design choice; none was measured.
- **Rhythm & rhetoric:** quick back-and-forth with chat, repetition when tension builds, long stretches of
  play-by-play. [ASR KO20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (KO20): in two 2026 streams, median about 295–321 Hz in three windows (p10–p90 about 204–463 Hz; a
    fourth, closing window with game audio throughout measured 257 Hz) and about 203–261 characters a minute of
    speech. Measurements describe the archived audio, not a target to clone.
  - Provisional (interpretation): a high, bright, bouncy voice with a lazy, drawling morning register and a tendency
    to stretch vowels when excited.
- **Sounds off:** a cool, low, deadpan voice as her default; a breathy whisper; slow solemnity.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Morning show | Drowsy, cheerful | 「はい、おはよー」 (ASR KO20) |
| Waiting for a game to load | Suspicious, repetitive | **Style demo:** 「待てよ待てよ、まだ油断できない」 ("Wait, wait, can't let my guard down yet") |
| Clearing an old game | Triumphant, loud | **Style demo:** 「クリアしたああああ！」 ("I cleared it!") |
| Horror | Screaming, laughing | **Style demo:** 「無理無理無理！」 ("No no no!") |
| Wrapping up | Content, narrating herself | 「なんか朝枠もいいなって思うころねなのであった」 (ASR KO20) |

### Sample Lines
1. 「ぉぁょ~！ゆびゆび～」 (oayo~! yubi yubi~, "Ello! Fingers! Give me your fingers!") (Official KO2)
2. 「はい、おはよー」 (hai, ohayō, "OK, mornin'") (ASR KO20, May 2026)
3. 「なんか朝枠もいいなって思うころねなのであった」 (nanka asawaku mo ii natte omou Korone na no de atta, "And so Korone
   thought a morning slot is kind of nice, too") (ASR KO20, May 2026)

## Appearance Anchors (avatar)
156 cm; illustrator Fukahire (フカヒレ). Brown hair in two long braids, floppy brown dog ears, bone-shaped hair
clips, red eyes and a brown dog tail. The official profile gallery (checked 2026-11-27) shows nine outfits;
descriptions are Claude's reading of those images:
- **Original outfit** (gallery 01–02): a red dog collar with a bone tag; a yellow jacket worn open, with colourful
  bow buttons on the sleeves; a white button-front sundress with multicoloured buttons and a navy hem; red leg
  warmers; white sneakers with pink laces. [Official KO1 gallery]
- **Beret outfit** (gallery 03): a red beret, small yellow hair bows, an orange plaid bow at the collar, a white
  blouse, a dark-brown capelet trimmed in gold, a dark-red skirt with gold patterns and white frills, brown knee
  socks and brown loafers. [Official KO1 gallery]
- **Japanese-style outfit** (gallery 04): red-and-white cord bows in her hair, a floating lavender shawl, a short
  white kimono top trimmed navy under a long yellow over-kimono patterned with red flowers and checks, a red obi with
  a white flower knot, white socks with pom-poms and red-thonged geta. [Official KO1 gallery]
- **Dog-hood outfit** (gallery 05): a pink zip hoodie with a white dog-face hood, "DOGGO" lettering and bone
  patches, a black tank top with dog prints, denim shorts, pink-and-white striped leg warmers and slippers.
  [Official KO1 gallery]
- **Sonic collaboration outfit (shown 2022-06-24 in an ambassador-commemoration stream; the image carries ©SEGA)**
  (gallery 06): a blue Sonic hoodie with spines and ears on the hood and a yellow front, blue-tinted hair and green
  eyes, white gloves, red sneakers and a Knuckles plush in her arms. [Official KO1 gallery] [KO4 QeqfCtJ-chw]
- **Alice-style outfit (revealed 2023-07-07; the reveal silhouette's bow and skirt match)** (gallery 07): a black
  ribbon headband, twin tails, a choker with a heart-lock pendant, a light-blue puff-sleeved dress under a white
  frilled apron, black harness straps with a small bottle charm, fishnet tights and black lace-up boots. [Official
  KO1 gallery] [KO4 Lidmb9yq8d8]
- **Viking-style outfit** (gallery 08): a horned helmet trimmed in gold, a gem pendant, a brown leather top with a
  shoulder guard, fur-trimmed arm wraps, a belt with a pouch, a red fur-trimmed skirt with a zigzag border, black
  thigh-highs and fur-topped boots. [Official KO1 gallery]
- **Jumpsuit outfit (revealed 2024-10-01 for her birthday; the reveal silhouette and the next day's thumbnail
  match)** (gallery 09): a yellow hooded jumpsuit with dog ears on the hood, white sleeves, a red badge and a paw
  badge, a white buckled belt, dog-face patches on the legs and chunky white sneakers. [Official KO1 gallery] [KO4
  mEPiE7V0lxg, SwUnrugQ9VM]
- **Horror-parody outfit** (gallery 10): a hockey mask pushed to the side of her head, braids with red bows, a red
  choker, a yellow-and-white striped T-shirt, denim overall shorts, red socks, blue sneakers and a toy-like chainsaw
  lettered "DooG" and splashed red. [Official KO1 gallery]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2019-04-13 | Debut (hololive GAMERS) | [Official KO1] [KO4 Qap7HFEx_oM] |
| 2019-09-14 | 3D debut stream | [KO4 I9m2C_Vx1j4] |
| 2020-04-01 | OkaKoro's first-anniversary cover, "ヒャダインのじょーじょーゆーじょー" | [KO4 MiuFIzr8bR0] |
| 2020-07-23/24 | "セガガガ" played until cleared, for SEGA's sixtieth anniversary | [KO4 E4yz96XAtdg, M4clvou7I00] |
| 2020-11-27 | Keep Talking and Nobody Explodes in Japanese and English with Mori Calliope | [KO4 yk2kdHkzI48] |
| 2021-04-01 | OkaKoro's second-anniversary 3D live | [KO4 v8tFy6_6R84] |
| 2022-06-24 | Sonic outfit shown in an ambassador-commemoration stream | [KO4 QeqfCtJ-chw] |
| 2023-04-14 | "Wonky Monkey" | [Official KO3] |
| 2023-07-07 | Alice-style outfit revealed | [KO4 Lidmb9yq8d8] |
| 2023-11-21 | "BITE! KAMU! BITE!" with Hakos Baelz | [Official KO3] |
| 2024-10-01 | Birthday reveal of the jumpsuit outfit; "Mad POPCORN World!" (10-02) | [KO4 mEPiE7V0lxg] [Official KO3] |
| 2024-12-06 | "Mikkorone × Yatteyanyo!!" with Sakura Miko | [Official KO3] |
| 2025-01-22 | #ころリオ, a first collab and off-collab with Isaki Riona | [KO4 QaGy1nHjRIQ, sze_5XnmD9w] |
| 2025-04-13 | Sixth-anniversary "3D and puppet live" | [KO4 ASwjM25ax58] |
| 2025-10-02 | "Mafiosa" | [Official KO3] |
| 2026-03-19 | A talk with Marine after interviewing a film director | [KO4 x3V1BH5tT-4] |
| 2026-04-18 | #ふたりは神様MaxDOG 3D off-collab with Mio (a horror game) | [KO4 yc7Iy-RACXY] |
| 2026-05-03 | First episode of 朝ころ | [KO4 Zlnqxdwg5Io] |
| 2026-07-25 | "Gimmick Gimmick Entertainment" (hololive IDOL PROJECT) | [Official KO3] |
| 2026-08-05 | Plays SPAGHET, a game Kikirara Vivi gave her | [KO4 LriXEkMQGAc] |
| 2026-09-29 | Machine Party as #いぬたかししらむ (with Lui, Botan and Tsunomaki Watame) | [KO4 Wc1kJDN-xtQ] |
| 2026-10-01 | Birthday (#戌神ころね生誕祭2026) | [KO4 HMDpQW57xC0] |

## Relationship Map
Public exchanges only.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Nekomata Okayu | "OkaKoro"; Okayu calls her "Koro-san" | More than thirty #おかころ titles: anniversary covers and a 3D live (2020, 2021), a Famicom World Championship practice off-collab (2024) | [KO4 MiuFIzr8bR0, v8tFy6_6R84, 45RJh43m6vI] [Okayu card] |
| Ookami Mio | #ふたりは神様MaxDOG | A 3D off-collab horror game (2026-04-18); a Mio-only call-in for Mio's sixth anniversary (2024-12-09) | [KO4 yc7Iy-RACXY, 5t4dWBqm07M] |
| Shirakami Fubuki | GAMERS | #フブころちゃん (2022-07-06); Fubuki's Mario Maker 2 course for Korone's sixth anniversary (2025-04-13) | [KO5 -6xMbpbxuyc, BgV_YObYXYM] |
| Nakiri Ayame | "Onigashima combo" (#鬼ヶ島コンビ) | Clubhouse Games five-match (2025-01-16); a ReGLOSS 3D live watch-along with Ayame and Lui (2024-09-28) | [KO4 myqzgEEnV1I, 1Q48E6vFA6Y] |
| Houshou Marine, Shirogane Noel, Yukihana Lamy | "Yakamashi Musume" | Cuphead and R.E.P.O. as #やかまし娘 (2025); a film talk with Marine (2026); "IT'S LOVE" with Marine for Elizabeth's birthday (2026); a Star Wars club with Noel and Himemori Luna (2025) | [KO4 Xx6XUFllIO8, RjIUPjfdhSY, x3V1BH5tT-4, VNJNilMuHZk] [Marine card] |
| AZKi | — | School 666 with AZKi, Momosuzu Nene and Lamy (2026-05-27); a group chat on Lamy's channel (#あずらみころ, 2026-09-18) | [KO4 ktEBw4nBpMs] [Lamy card] |
| Takane Lui, Shishiro Botan | #いぬたかししらむ with Tsunomaki Watame | Machine Party (2026-09-29); Left 4 Dead 2 with IRyS (2022); #ルイころ (2025) | [KO4 Wc1kJDN-xtQ] [Botan, Lui and IRyS cards] [GAMERS card] |
| Hakui Koyori | — | A manzai together (2022-12-15); Splatoon 3 with IRyS and Watame (2022) | [KO4 hNqFWgDcvXM] [Koyori card] |
| Hakos Baelz | Duet partner | "BITE! KAMU! BITE!" (2023-11-21) | [Official KO3] |
| Mori Calliope | — | A bilingual Keep Talking and Nobody Explodes (2020-11-27) | [KO4 yk2kdHkzI48] |
| Nanashi Mumei (graduated) | — | A guest at Mumei's "Outside the Box" (2024); the duet cover "とんとんまーえ！" (2025-04-23) | [Mumei card] |
| FUWAMOCO | — | A cameo with Okayu at their 3D debut (2024) | [FUWAMOCO cards] |
| Elizabeth Rose Bloodflame | — | A guest at her 2026 birthday live; "IT'S LOVE" with Marine (2026) | [Elizabeth card] |
| Isaki Riona | — | #ころリオ, first collab and off-collab (2025-01-22) | [KO4 QaGy1nHjRIQ] |
| Rindo Chihaya | — | R.E.P.O. (2026-06-29) | [KO4 G6r_oZBgD3E] |
| Kikirara Vivi | — | Vivi gave her the game SPAGHET (2026) | [KO4 LriXEkMQGAc] |

## Arc
- **Starting point:** active at the 2026 baseline, seven years in: a steady run of originals, film-promotion work and
  a new morning show.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: an endurance stream that refuses to end; a demand for everyone's fingers; an old console
  nobody else knows how to set up.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Korone challenges Okayu to clear a 1990s platformer before the bakery opens.
  2. A film director she interviewed asks for a cameo, and Korone insists on doing her own stunts.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2019-04-13; hololive GAMERS; birthday 1 October; 156 cm; illustrator Fukahire; fans Koronesky (ころねすきー);
  tags #生神もんざえもん, #できたてころね.

## Sources (checked 2026-11-27)
- KO1 Official profile (English; text, data and gallery): https://hololive.hololivepro.com/en/talents/inugami-korone/
- KO2 Official profile (Japanese; tagline): https://hololive.hololivepro.com/talents/inugami-korone/
- KO3 Official music: https://hololive.hololivepro.com/en/music/281/ ("Wonky Monkey," 2023-04-14), …/334/ ("Kawaiko
  Check!," 2023-09-24), …/354/ ("BITE! KAMU! BITE!," with Hakos Baelz, 2023-11-21), …/414/ ("TROUBLE 'WAN'DER!,"
  2024-04-14), …/480/ ("Mad POPCORN World!," 2024-10-02), …/509/ ("Mikkorone × Yatteyanyo!!," with Sakura Miko,
  2024-12-06), …/651/ ("Mafiosa," 2025-10-02), …/578/ (Aki Rosenthal's "MUSICAL Fantasia of Bremen," 2025-06-02,
  listed on Korone's profile), …/785/ ("Gimmick Gimmick Entertainment," 2026-07-25), …/420/ and …/591/ (GAMERS)
- KO4 Her channel's archive metadata (archive.ragtag.moe; titles): Zlnqxdwg5Io and alUDRkSYyc8 (the audio windows),
  Qap7HFEx_oM, I9m2C_Vx1j4, MiuFIzr8bR0, v8tFy6_6R84, 45RJh43m6vI (OkaKoro), E4yz96XAtdg and M4clvou7I00 (セガガガ),
  27N1_I21YQo, dQFvlxqx44E and 1IuOKoNqWug (endurance and retro), yk2kdHkzI48 (Calli), QeqfCtJ-chw, Lidmb9yq8d8,
  mEPiE7V0lxg and SwUnrugQ9VM (outfits), ASwjM25ax58, o3JeicqyVG0 and sh0j8Fl-wGg (anniversaries), 8h60xVu58bM, x3V1BH5tT-4 and
  JLALCjMzjTM (film work), yc7Iy-RACXY and 5t4dWBqm07M (Mio), myqzgEEnV1I and 1Q48E6vFA6Y (Ayame), Xx6XUFllIO8 and
  RjIUPjfdhSY (#やかまし娘), VNJNilMuHZk (Noel), ktEBw4nBpMs (School 666), Wc1kJDN-xtQ (#いぬたかししらむ),
  hNqFWgDcvXM (Koyori), QaGy1nHjRIQ and sze_5XnmD9w (#ころリオ), G6r_oZBgD3E (Chihaya), LriXEkMQGAc (Vivi),
  HMDpQW57xC0 (birthday 2026)
- KO5 Other channels' archive metadata: -6xMbpbxuyc and BgV_YObYXYM (Fubuki's channel)
- KO20 Claude's audio check (two-model ASR, Japanese): research/audio-check/gamers.md

## [SW] Name
Inugami Korone

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive GAMERS, OkaKoro, Yakamashi Musume, OKFAMS

## [SW] Other Names
Korone, Koro-san, 戌神ころね

## [SW] Personality
Her official profile presents Korone as a dog from a bakery in the city who plays games in her free time while minding the shop. On stream she is bright, bouncy and relentless: she plays games to the very end, old and new, in "completely first-time" playthroughs and marathon play-until-cleared streams, and she loves old consoles. Her signature bit is asking her viewers for their fingers. She screams and laughs her way through horror, narrates her own triumphs, and in 2026 started a morning show, where she sounds drowsy and cheerful and once ended by narrating herself in the third person. With Nekomata Okayu she is OkaKoro; with Ookami Mio she runs "ふたりは神様MaxDOG"; with Houshou Marine, Shirogane Noel and Yukihana Lamy she is one of the Yakamashi Musume. In 2026 she also took on film-promotion work. Her fans are the Koronesky.

## [SW] Background
Korone is an active member of hololive GAMERS. She has no supernatural abilities; her lore is a performed persona. She debuted on 2019-04-13, a week after Nekomata Okayu, and made her 3D debut in September 2019. She became known for endurance streams, including a play-until-cleared marathon of "セガガガ" for SEGA's sixtieth anniversary (2020), and for bilingual fun with Mori Calliope (2020). She has released originals such as "Wonky Monkey" (2023) and "Mafiosa" (2025), a duet with Hakos Baelz ("BITE! KAMU! BITE!," 2023) and one with Sakura Miko (2024), and she celebrated her sixth anniversary with a 3D and puppet live (2025). In 2026 she interviewed film directors, played a horror game in 3D with Ookami Mio and began her morning show on 2026-05-03.

## [SW] Physical Description
Korone's avatar is 156 cm, with brown hair in two long braids, floppy brown dog ears, bone-shaped hair clips, red eyes and a brown dog tail. Original outfit: a red dog collar with a bone tag, an open yellow jacket with colourful bow buttons, a white button-front sundress with a navy hem, red leg warmers and white sneakers. Other outfits in the official gallery: Beret outfit: a red beret, a dark-brown capelet, a dark-red frilled skirt; Japanese-style outfit: a floating lavender shawl, a yellow over-kimono with red flowers, a red obi; Dog-hood outfit: a pink hoodie with a white dog-face hood, denim shorts, striped leg warmers; Sonic collaboration outfit (2022): a blue Sonic hoodie, green eyes, a Knuckles plush; Alice-style outfit (2023): a black ribbon, a light-blue dress under a white apron, fishnet tights; Viking-style outfit: a horned helmet, a leather top, a fur-trimmed red skirt; Jumpsuit outfit (2024): a yellow dog-eared hooded jumpsuit with white sleeves; Horror-parody outfit: a hockey mask on her head, denim overalls, a toy chainsaw lettered "DooG."

## [SW] Dialogue Style
Streams in Japanese: quick, bright and playful, with repetition when tension rises (「待てよ待てよ」) and long play-by-play while she plays. Her greeting asks for fingers (「ぉぁょ~！ゆびゆび～」); on her morning show she opens with a drowsy 「はい、おはよー」, and she can wrap up by narrating herself in the third person (「…ころねなのであった」). English flourishes such as "Ello!" appear in her official English line. No regional accent is assigned. When a story renders her speech in English or Chinese, keep the playful repetition, the finger jokes and the gamer's single-mindedness.

## [SW] Catchphrases
「ぉぁょ~！ゆびゆび～」 ("Ello! Fingers! Give me your fingers!", official); 「ゆび」 ("fingers," her running bit); 「はい、おはよー」 (her morning-show opening); 「…ころねなのであった」 ("and so it was, for Korone," her third-person wrap-up); 「ド★初見」 ("completely first-time"); 「ころね支店」 ("the Korone branch," her channel's side of a collab); "Koro-san" (Okayu's name for her); "Koronesky" (ころねすきー, her fans).

## [SW] Voice & Delivery
Direction for an original designed voice: a high, bright, bouncy voice; drowsy and drawling in the morning; quick, repetitive and suspicious while waiting on a game; loud and triumphant at a clear; screaming and laughing in horror; warm and content when she wraps up. Not as default: a cool, low deadpan, a breathy whisper or slow solemnity.

## [SW] Audio Tags
Dialogue language for audio scripts: Japanese. Write her spoken turns in Japanese script; romaji and English go only on ROMAJI/GLOSS lines. ElevenLabs v4 performance directions for an original designed voice; never imitate the real member. Register: high, bright, bouncy voice. Default tags: [playful, energetic]. By situation: morning show [sleepy, cheerful]; waiting on a game [suspicious]; a clear [triumphant, shouting]; horror [screaming]; wrapping up [content, warm]; asking for fingers [mischievous]. With people: Okayu [playful, affectionate]; Mio [teasing]; Marine [rowdy]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [laughs] (tag only); [screams] (tag only). Keep in the words: 「ゆび」 (yubi), 「ころね」 (Korone), 「ころねすきー」 (Koronesky). Reading: いぬがみ ころね. No regional accent is assigned. Not as default: a cool deadpan or a breathy whisper.

## [SW] Motivation
In her lore, Korone is a bakery dog who plays games between customers. As a streamer, she wants to play games to the end with her viewers, keep her old favourites alive and have fun loudly.

## [SW] Relationships
hololive GAMERS (Shirakami Fubuki, Ookami Mio, Nekomata Okayu): her unit. Nekomata Okayu: OkaKoro; Okayu calls her "Koro-san"; anniversary covers, a 3D live and off-collabs. Ookami Mio: "ふたりは神様MaxDOG," including a 3D horror off-collab (2026). Shirakami Fubuki: #フブころちゃん (2022) and a Mario Maker course for Korone's sixth anniversary (2025). Nakiri Ayame: the "Onigashima combo." Houshou Marine, Shirogane Noel and Yukihana Lamy: Yakamashi Musume; a film talk with Marine (2026). AZKi: School 666 with Lamy and Momosuzu Nene (2026). Takane Lui and Shishiro Botan: #いぬたかししらむ with Tsunomaki Watame (2026). Hakui Koyori: a manzai (2022). Hakos Baelz: the duet "BITE! KAMU! BITE!" (2023). Mori Calliope: a bilingual bomb-defusal game (2020). Nanashi Mumei (graduated): the cover "とんとんまーえ！" (2025). FUWAMOCO: a cameo at their 3D debut (2024). Elizabeth Rose Bloodflame: a guest at her 2026 birthday live. Isaki Riona: #ころリオ (2025). Rindo Chihaya: R.E.P.O. (2026). Kikirara Vivi: gave her the game SPAGHET (2026).

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Voice & Delivery and Audio Tags are performance directions for an original designed voice. Timbre, laughter and
  delivery are design choices unless a listening source is named in the Voice Profile; ASR supports wording, not
  vocal quality or recurrence; partner tags are optional scene directions, not observed defaults; the kana reading
  is untested; recorded pitch and speaking-rate figures are research context only, never synthesis targets.
- 「ぉぁょ~！ゆびゆび～」: the official Japanese profile. 「はい、おはよー」 and 「なんか朝枠もいいなって思うころねなので
  あった」: both ASR models (spelling differences only). 「ド★初見」 and 「ころね支店」: her stream titles.
- The film work: archived titles (the films and directors are named in the titles; not summarized further here).
- Ties already on other cards (Marine, Lamy, Noel, AZKi, Botan, Lui, IRyS, Koyori, Mumei, FUWAMOCO, Elizabeth) are
  cited from those cards; Yakamashi Musume follows the Marine and Lamy cards.
- Outfits: Claude's reading of the official gallery images. The Sonic outfit's date rests on the stream title and
  the ©SEGA mark; the Alice-style and jumpsuit outfits' dates on the reveal silhouettes (and, for the jumpsuit, the
  next day's thumbnail).

## Merge Record
- **2026-11-27, Claude only (author order: complete hololive GAMERS):** official profiles, gallery and music pages,
  archive metadata and a two-model ASR check (KO20). Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. Her spoken greeting outside the morning show was not captured in the two windows (game audio and music cover
   the openings).
2. What the 2022 "ambassador" title refers to is not established here.
3. Reveal dates for the other gallery outfits are not established here.
````

### FILE: `bible/world/FLOW-GLOW.md`

````markdown
---
kind: world
name: "FLOW GLOW"
sw_section: Worldbuilding
---

# World Element: FLOW GLOW

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-11-27; added by author order (2026-11-27: complete all FLOW GLOW members). Evidence labels
> as in the other world files. "Archive" = stream titles and descriptions on the members' and other members'
> channels (archive.ragtag.moe, S1; its copy of these channels ends around 2026-10-21). FLOW GLOW is a five-member
> music unit that debuted through hololive DEV_IS, which COVER restructured in a 2026-09-07 announcement, so DEV_IS
> is not listed as a current separate affiliation (as on Vivi's card). Nothing about the performers behind the
> avatars: private-life information is outside scope and is not recorded here.
>
> **External review pending (Gemini Neon).** This card was researched and written by Claude alone (2026-11-27). The
> author decided on 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending
> (research/qa/external-review/).

## One-line Concept
A five-girl hip-hop and pop unit that debuted together: a stoic leader who hates losing, a jokester who will
break character for a laugh, a tiny publicity manager who wants love and praise, a DJ who drives the group's car,
and a makeup artist who hunts beauty. Officially, their skills are unpolished and their trust is still incomplete,
but they acknowledge what each of them carries. [Official S2, S3, S4]

## Type
Unit (music artist group; five persona roles; all five active at the baseline).

## The roles (official profiles)
- **Isaki Riona**, the leader ("I'll do what I like and live how I want to!"): stoic, a sore loser, a poker face
  so nobody looks down on her, but she melts for small animals; a shonen-manga fan. Fans: Isaki Union. [Official S2]
- **Koganei Niko**, the jokester ("If you can't bring yourself to a smile, just say my name!"): will give anything
  to make people smile; bulldozing or breaking character is fine if it ends in laughter; weak against mornings.
  Fans: Niko Stan (ニコ担). [Official S2]
- **Mizumiya Su**, the publicity manager ("Is your Su-charge at 100%?"): wants love and praise and posts on social
  media with her mouth full; found the friends she has now just as she wished the world were kinder; asks the gods
  to make her a little taller. Fans: Su-risu. [Official S2]
- **Rindo Chihaya**, the DJ and driver ("Won't you come with me…?"): a self-proclaimed 300-horsepower driver with
  no brakes when she talks or sings; a beginner DJ, earnest and curious; her favourite thing is driving her
  friends in her car. Fans: Chihanic (her channel writes ニック, from "mechanic"). [Official S2] [S1 descriptions]
- **Kikirara Vivi**, the makeup artist ("Hol'up, 'cus you're in for a transformation!"): a seeker of beauty whose
  frank words come out in dialect; sunlight is her natural enemy. Fans: Vivid. [Official S2, S4]

## Their world (official lore)
- **NOW RAWDING** (ナウ ローディング): FLOW GLOW's hangout, a former café with an event space that they rent. The
  owner lets them use it freely; each member has brought in her own things, so it has become a mixed, very
  personal space. [Official S3]
- **Fugutarō** (ふぐ太郎): Chihaya's beloved car. It carries FLOW GLOW on most of their trips and tours, is big
  enough for all five, and is heavily customized, with a large-displacement engine and a rear roof that opens.
  [Official S3]
- Their debut pop-up, "FLOW GLOW HOUSE," was held in Harajuku, "where their hideout is located," 2024-11-13 to
  11-17. [Official S4]

## How they work together
- Debut relay on 2024-11-09 (from 3:00 AM PST): Riona, Niko, Su, Chihaya, then Vivi, followed by a cover-song
  relay; the unit's first stream was on 2024-11-10 (PST) on the official FLOW GLOW channel. [Official S4]
- Debut song "FG ROADSTER" (video premiere 2024-11-08 PST; release 2024-11-09): a hip-hop beat with traditional
  Japanese instruments, a verse for each member's rap, and a hook sung together; its lyricist says it was
  inspired by the Tesla Roadster still orbiting the sun. [Official S4, S5]
- Pairs and trios named in their own titles: "team hentai gentlemen" (ちーむ変態ジェントルマン: Chihaya, Riona and
  Niko, Chained Together and a "butt-bat" penalty first off-collab, 2024-11); #にこすぅ (Niko and Su, 2024-11-24);
  ちはすう (Chihaya and Su, an off-collab, 2025-08-03); すうヴィヴィ (Su and Vivi, 2026-06-06); a #FGオフコラボ
  gyoza party (2024-12-27). [S1]
- Duets: "Gimme×Gimme" (Riona and Niko, 2024-12-03), "あの夏が飽和する" (Niko and Riona, 2025-10-23) and "逆様" (Riona
  and Niko); "レイメイ" (Su and Chihaya, 2024-12-06) and "Beyond the way" (2025-08-17); "らぶきゅん♡うぉんてっど"
  (Su and Vivi, 2024-12-05) and "クリームで会いにいけますか" (Su and Vivi); "ポケットにファンタジー" (Niko and Su,
  2025-06-29); "Bridal Dream" (Vivi and Chihaya, 2025-07-28). [S1] [Official video listing S2]

## With the English cast
- **Mori Calliope:** Riona calls her "my beloved Calli-senpai" in her titles: a Clubhouse Games collab on Riona's
  channel (2026-09-12), Riona playing MYRIAD DEATH as Calli (2025-04-11), a watch-along of Calli's live with
  Chihaya and Niko (2025-02-27); Calli and Riona dance "Ring my name" (Calli's short 2026-06-19, Riona's
  2026-07-02). Niko sang in LYRA's "III" with Calli and Elizabeth and in "Magia" with Calli and Nerissa
  (2026-08-28). [S1]
- **Nerissa Ravencroft:** "Magia" with Calli and Niko (2026-08-28); a "Ring my name" dance short (2026-06-23). [S1]
- **Elizabeth Rose Bloodflame:** LYRA with Niko; Gartic Phone with Vivi (2025). [S1, LYRA credits on Elizabeth's card]
- **IRyS, Koseki Bijou:** "Ring my name" dance shorts (IRyS with Riona 2026-07-22; Bijou 2026-06-18). [S1]
- **FUWAMOCO, Bijou:** watched FLOW GLOW's debut (2024-11-08 PST); FUWAMOCO, Bae, Ina, Kronii, Elizabeth and Mumei
  played with Vivi (2025; see her card). [S1]

## With the other Japanese members on the cards
- **AZKi:** RoARiS, a Momotetsu 2 group with Roboco, Su and Riona (2026-06-07); a four-person self-3D karaoke with
  Koyori, Riona and Niko (#せくちー3Dカラオケ, 2026-02-03); Riona and Su sang as guests at AZKi's 2026 birthday 3D
  live; Niko played holoRUST on "Team AZKi" (2025); AZKi danced "Ring my name" (2026-06-25); Vivi: GeoGuessr and a
  3D pun battle (2026). [S1]
- **Hakui Koyori:** the 2026 3D karaoke; #こよすう, a first one-on-one collab with Su (2025-02-02); holoRUST with
  Riona (2025). [S1]
- **Takane Lui:** Minecraft with Niko ("End date," 2025-03-02) and with Riona (a gold trap, 2025-03-17); Lui watched
  over Niko's Shadow Corridor runs (2025-04); horse racing with Chihaya (February Stakes, 2025-02-23). [S1]
- **Nekomata Okayu:** watched the debut with Korone (2024-11-09); Minecraft (2025-02-20), a voice-impression game
  (2025-03-24) and the cover "打上花火" (2026-09-20) with Chihaya. [S1]
- **Houshou Marine:** a collab in which Su makes Marine her "pet" (2025-06-29); MVP with Vivi and Pekora (2026). [S1]
- **Yukihana Lamy:** #にこらみ晩酌, an off-collab with Niko (2024-12-22); Gang Beasts with Nene, Riona and Chihaya
  (2025-01-20). [S1]
- **Sakamata Chloe:** a talk collab on Chihaya's channel (2024-12-12). **Shishiro Botan:** a "Ring my name" dance
  short (2026-06-19). **Hoshimachi Suisei:** Chihaya covered "ムーンライト" (2024-12-28) and played "ビビデバ" on
  trombone (2025-01-15); Suisei taught Vivi Tetris (2026). [S1]

## History
| Date | Event | Source |
|---|---|---|
| 2024-11-07 | Debut announced (DEV_IS's second unit) | [Official S4] |
| 2024-11-08 (PST) | "FG ROADSTER" video premiere | [Official S4] |
| 2024-11-09 | Debut relay; "FG ROADSTER" released | [Official S4, S5] |
| 2024-11-10 (PST) | First unit stream, official FLOW GLOW channel | [Official S4] |
| 2024-11-13 to 11-17 | FLOW GLOW HOUSE pop-up, Harajuku | [Official S4] |
| 2024-12-10 | "FG ROADSTER (Solo ver.)" | [Official S5] |
| 2025-03-14 | "24K GOLD" | [Official S5] |
| 2025-07-09 | "LOAD" | [Official S5] |
| 2025-09-21 | "good enough" | [Official S5] |
| 2025-11-10 | "stay by my side" | [Official S5] |
| 2025-11-23 | 3D debut live, "MAKE IT, BREAK IT" | [Secondary S6] [Official #FG3Dライブ videos S2] |
| 2025-11-24 | "MAKE IT, BREAK IT" released | [Official S5] |
| 2026-01-21 | First album, "FLOW GLOW" | [Official S5] |
| 2026-03-07 | Festival debut: hololive 7th fes. "Ridin' on Dreams," STAGE3 at Makuhari Messe, opening with "MAKE IT, BREAK IT" (AZKi and Noel were on the same stage) | [Secondary S8] [Official video listing S2] |
| 2026-05-30 to 2026-11-24 | Solo singles: Riona "Ring my name" (05-30) and "Reverberate" (11-24); Su "うみゃうにゃはっぴーらいふ" (06-17); Chihaya "Flat out" (07-09) and "果てない旅" (10-30); Niko "星炎" (07-26); Vivi "Vivid Cute" (08-28) | [Official S5] |
| 2026-08-19 | "magic summer" | [Official S5] |
| 2026-09-07 | COVER's DEV_IS restructuring announcement | [Official S7] |
| 2026-11-10 | Second anniversary (#FG2周年): "BOUNCE BACK！" | [Official S5, S2 listing] |

## Sensory Palette
- See: a silver side ponytail and a crown-topped pink microphone; long blonde hair, round orange glasses and a
  tiger-embroidered varsity jacket; a tiny girl with light-blue hair, pink braids and a pink phone on a chain; black
  hair with teal and white streaks, big DJ headphones and a checkered cap; pink-to-purple twin tails and a heart bag
  full of makeup brushes. A rented café hangout crowded with five people's things; a huge customized car with an
  opening roof.
- Hear: hip-hop verses, a hook shouted together; 「しゅぴしゅわ〜」; Chihaya's nonstop talk; Vivi's dialect.

## Glossary
| Term | Meaning | Who uses it |
|---|---|---|
| FG | FLOW GLOW (#FG2周年, #FGオフコラボ) | everyone |
| NOW RAWDING | their rented café hangout (official lore) | FLOW GLOW |
| Fugutarō (ふぐ太郎) | Chihaya's car (official lore) | FLOW GLOW |
| FLOMIE | the unit's fans (unit fan name, secondary) | fans |
| ちーむ変態ジェントルマン | Chihaya, Riona and Niko's self-named team (2024 titles) | those three |
| RoARiS | Roboco, AZKi, Riona and Su (2026 Momotetsu title) | those four |

## Conflicts and Story Hooks
1. Chihaya drives all five to a gig in Fugutarō; Riona insists on leading the route, Niko narrates it like a
   comedy show, Su films everything for social media and Vivi fixes everyone's makeup in the back seat.
2. NOW RAWDING has five people's stuff and no rules; someone's prized item goes missing on the day of a shoot.
3. (Proposed fiction) Calli drops by the café for Riona's "beloved senpai" visit and ends up judging a rap battle.

## Links to Characters
Isaki Riona; Koganei Niko; Mizumiya Su; Rindo Chihaya; Kikirara Vivi; Mori Calliope; Nerissa Ravencroft; Elizabeth
Rose Bloodflame; IRyS; Koseki Bijou; FUWAMOCO; AZKi; Hakui Koyori; Takane Lui; Nekomata Okayu; Houshou Marine;
Yukihana Lamy; Sakamata Chloe; Shishiro Botan; Hoshimachi Suisei.

## Secrets
None assigned.

## Hard Facts (continuity)
- Members (debut relay order, 2024-11-09): Isaki Riona (leader), Koganei Niko (jokester), Mizumiya Su (publicity),
  Rindo Chihaya (DJ and driver), Kikirara Vivi (makeup).
- 3D debut live 2025-11-23; first album "FLOW GLOW" 2026-01-21; second anniversary 2026-11 with "BOUNCE BACK！".

## Sources (checked 2026-11-27)
- S1 Stream archive metadata (archive.ragtag.moe), the members' and other members' channels: i25b--m63UU and
  DBN-VVm-pRs (ちーむ変態ジェントルマン), y-nFLZtmLQ4 ("Gimme×Gimme"), h32hZjqOHGk ("あの夏が飽和する"), h1OY5HGdGKo
  ("レイメイ"), PcSLoke_mH8 ("Beyond the way"), zKA2G6hX9iI ("らぶきゅん♡うぉんてっど"), QCMtwotxvxY ("ポケットにファンタジー"),
  NGeumGspO2g ("Bridal Dream"), L_bZXIcegzc (gyoza party), 7RAHdEtY7Fo (ちはすう), ypxnG-t-dmc (すうヴィヴィ),
  hhOim_G0kns, LRSvK1ePA8o, 4Zb0JEy3bw4, IAom9MDoVxs and rAR9fgHBKwI (Calli), 5ccqXCOshHc ("Magia"), Ts1v3xM-YG8
  (Nerissa), uLvilDwP6HE (IRyS), mTSUnQ-0h1E (Bijou), gAj77STI2oc (FUWAMOCO watch-along), jG-EPYQ4V9g (RoARiS),
  1HQL3WJPBHA (3D karaoke), M1mZrusy-xY and fqGI67bRcXQ (AZKi's 2026 birthday live shorts), 7UaG-JGAdIs (Team AZKi),
  83cZEqTVdOQ (AZKi dance), f4K54Fc-ghM (#こよすう), l50dJY8DxqM (holoRUST with Koyori), IvzEZcBdmNk, pB3e3SzBjJ8,
  hlb4XXjpf4M and Lh7LPWpmCEI (Lui), rlylHqns09w, IYBdcw4wWuA, DcfVi2rf1oc and UGQfq16yY1A (Okayu), zpG2xKGK_Jo
  (Marine), Ig_Ba2h9DZc and EsfZ7Ny4aPA (Lamy), FgSn_JCgKyk (Chloe), z6V93vfXrWk (Botan), xqwCq0AZXeg and
  nREYWWmVVls (Suisei songs)
- S2 Official profiles and their video listings: https://hololive.hololivepro.com/en/talents/isaki-riona/,
  …/koganei-niko/, …/mizumiya-su/, …/rindo-chihaya/, …/kikirara-vivi/ (listed videos: xMRwvFGy8Q4 "逆様,"
  _ypWJ0IitYA "クリームで会いにいけますか," 4SVMkcrPtT8 and JQgTOnJ17fk #FG3Dライブ, L3-VtHNm9oA 7th fes. STAGE3,
  48hUYLrV8bE #FG2周年)
- S3 Official FLOW GLOW page (Japanese; profiles, NOW RAWDING, ふぐ太郎): https://hololive.hololivepro.com/special/13902/
- S4 Official debut announcement (2024-11-07): https://hololive.hololivepro.com/en/news/20241107-01-108/
- S5 Official music catalog: https://hololive.hololivepro.com/en/music/495/ (FG ROADSTER), …/512/, …/550/, …/583/,
  …/638/, …/671/, …/675/, …/024/ (album), …/804/ (magic summer), …/861/ (BOUNCE BACK！), solos …/756/, …/851/,
  …/763/, …/772/, …/850/, …/781/, …/808/
- S6 Report on the 3D debut live (secondary news): https://dengekionline.com/article/202511/58688
- S7 DEV_IS restructuring announcement: https://hololivepro.com/news_en/20260907-01-266/
- S8 STAGE3 photo report, hololive 7th fes. (secondary news, 2026-03-07): https://game.watch.impress.co.jp/docs/kikaku/2091478.html

---

## [SW] Name
FLOW GLOW

## [SW] Role
Organization

## [SW] Other Names
FG, フロウグロウ

## [SW] Description
FLOW GLOW is a five-member music unit that debuted on 2024-11-09 through hololive DEV_IS, which COVER restructured in 2026. Officially their skills are unpolished and their trust incomplete, but they acknowledge each other's strengths. Isaki Riona is the stoic, competitive leader who melts for small animals; Koganei Niko is the jokester who will break character for a laugh; Mizumiya Su is the tiny publicity manager who wants love and praise; Rindo Chihaya is the DJ and self-proclaimed 300-horsepower driver; Kikirara Vivi is the makeup artist who hunts beauty. In their lore they hang out at NOW RAWDING, a rented former café crowded with everyone's things, and travel in Fugutarō, Chihaya's huge customized car with an opening roof. Their debut song "FG ROADSTER" gives every member a rap verse. They held a 3D debut live, "MAKE IT, BREAK IT," on 2025-11-23, released the album "FLOW GLOW" on 2026-01-21, appeared at hololive 7th fes. in 2026, released "magic summer" and solo singles for all five in 2026, and marked their second anniversary with "BOUNCE BACK！" (2026-11-10). Inside the unit they pair off for covers and collabs: Riona and Niko ("Gimme×Gimme," "逆様"), Su and Chihaya ("レイメイ"), Su and Vivi ("クリームで会いにいけますか"), Vivi and Chihaya ("Bridal Dream"); Chihaya, Riona and Niko call themselves "team hentai gentlemen." With the English cast: Riona calls Calli her "beloved Calli-senpai" (a Clubhouse Games collab, 2026); Niko sang LYRA's "III" with Calli and Elizabeth and "Magia" with Calli and Nerissa; Calli, Nerissa, IRyS and Bijou danced to Riona's "Ring my name"; FUWAMOCO and Bijou watched their debut. With Japanese seniors: AZKi (RoARiS, a 3D karaoke with Koyori, Riona and Niko, and guest spots for Riona and Su at her 2026 birthday live), Lui, Okayu, Marine, Lamy and Chloe.

## [SW] Rules
FLOW GLOW's café hangout, the car and the role lore are performed frames; the members are streamers. DEV_IS was restructured in 2026, so stories set after 2026-09-07 should not treat it as a separate branch. Collab titles show that a collab happened, not how close two members are; cover partners are listed per song. Pre-debut life and the performers' private lives are outside the cards.

## [SW] Sensory Details
A silver side ponytail and a crown-topped pink microphone; long blonde hair, round orange glasses and a tiger-embroidered varsity jacket; a tiny girl with light-blue hair, pink braids and a pink phone on a chain; black hair with teal and white streaks, big DJ headphones and a checkered cap; pink-to-purple twin tails and a heart bag full of makeup brushes (official key art). A rented café crowded with five people's things; a huge customized car with a roof that opens. Fan marks 🎤👑 ☺️🐅 💬🔁💙 🎧🔧 💅✨.

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- NOW RAWDING, Fugutarō and the roles: the official FLOW GLOW page (S3). Debut, pop-up and song facts: the official
  announcement (S4). Release dates: the official catalog (S5). The 3D debut live date: a news report (S6) plus the
  official #FG3Dライブ videos. The 7th fes. appearance: a news photo report (S8) and the official video listing on Niko's profile page.
- "逆様" and "クリームで会いにいけますか": official video listings (undated in this check; the archive copy ends
  before them). The unit fan name FLOMIE is secondary (an earlier research report) and stays in the Glossary only.
- Collabs and dance shorts: archived titles; a dance short published on a channel does not establish who
  performed the motion.

## Merge Record
- **2026-11-27, Claude only (author order: complete FLOW GLOW):** official profiles, the official FLOW GLOW page,
  the debut announcement, the music catalog and the archive. Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. The release dates of "逆様" and "クリームで会いにいけますか" are not established here.
2. The unit fan name (FLOMIE) needs an official source before it goes on the card.
````

### FILE: `bible/world/hololive-GAMERS.md`

````markdown
---
kind: world
name: "hololive GAMERS"
sw_section: Worldbuilding
---

# World Element: hololive GAMERS

> Research dossier above; the Sudowrite Worldbuilding card is under the `## [SW]` headings.
>
> Scope: checked 2026-11-27; added by author order (2026-11-27: complete hololive GAMERS). Evidence labels as in the
> other world files. "Archive" = stream titles on the members' channels (archive.ragtag.moe, G2; its copy ends around
> 2026-10-21). Nothing about the performers behind the avatars: private-life information is outside scope and is not
> recorded here.
>
> **External review pending (Gemini Neon).** Researched and written by Claude alone (2026-11-27). The author decided on
> 2026-11-27 not to use the Codex/GPT review; a re-review by Gemini Neon (desktop) is pending (research/qa/external-review/).

## One-line Concept
hololive's gaming unit of four animal-eared girls: a white otaku fox, a black-haired wolf who haunts shrines, a
lazy-voiced cat and a bakery dog, who have played games, done radio and held arena fan festivals together since
2018. [Official G1] [G2]

## Type
Unit (four members, all active at the baseline; Fubuki also belongs to hololive's 1st generation).

## The members (official profiles)
- **Shirakami Fubuki** ("Good foxy day! I'm Shirakami Fubuki!" / 「こんこんきーつね！白上フブキです！」): a white-haired,
  animal-eared otaku fox who loves talking with people and aims to be a top otaku idol. 1st generation and GAMERS.
  Fans: Sukonbu (すこん部). [Official G1]
- **Ookami Mio** ("Hellooowl! It is Ookami Mio!" / 「こんばんみぉーん！大神ミオだよ～！」): a black-haired wolf girl who
  appeared from nowhere, often shows up around shrines and loves games. Fans: Mio-fam (ミオファ). [Official G1]
- **Nekomata Okayu** (see her card): a relaxed, boyish cat; "Mogu mogu~ Okayu~!" Fans: Onigiryā. [Okayu's card]
- **Inugami Korone** ("Ello! Fingers! Give me your fingers!" / 「ぉぁょ~！ゆびゆび～」): a dog from a bakery in the city
  who plays games in her free time while minding the shop. Fans: Koronesky (ころねすきー). [Official G1]

## How they work together
- Unit PV on 2018-12-06; Mio debuted the next day (2018-12-07); Okayu (2019-04-06) and Korone (2019-04-13) joined
  as the newest members. A monthly radio show, ほろらじゲーマーズ, ran in 2019. [G2 DPZbSlHcdfo, 2pfFq7E7keg] [Okayu's card]
- Group games: Overcooked! 2 (2019), Phasmophobia (2020, 2022), Earth Defense Force 5 and Splatoon 3 festivals
  (2022), a game of Life (2023), an off-collab eating educational candy "bugs" (2024-08-16). [G2]
- Live events: the first real fan event, "超超超超ゲーマーズ," in May 2024 at Yoyogi National Gymnasium (reported sold
  out); a formation-anniversary 3D live in 2024 with "We are GAMERS !!!!"; "hololive GAMERS fes. 超超超超ゲーマーズ2"
  at Saitama Super Arena on 2025-07-05 and 07-06 (guests included Nakiri Ayame). [G2 aWE92xAcyrk, 8Y1fLns6KY0,
  0u8ZTalXGEc, u1mdfpWU8wE, tJeo9zWQUrc] [Secondary G3]
- Songs: "To Be Continued…." (all four; official MV listing) and Fubuki's original "ワンダーフューチャー！" featuring
  Mio, Okayu and Korone (2025-02-02). A White Cat Project collaboration added the GAMERS in 2026. [Official G1
  listing] [G2 n7ZLEzbubJs, g9O_ctXThLE]
- Pairs inside the unit: FubuMio (#フブミオ, Fubuki and Mio); OkaKoro (#おかころ, Okayu and Korone); #ふたりは神様MaxDOG
  (Mio and Korone); NYANGUCORN (にゃんぐこーん, Okayu and Fubuki covers, 2025); Mio and Okayu covers ("おとなの掟,"
  2021; "神或アルゴリズム," 2025). [G2] [Okayu's card]

## With the English cast
- **Mori Calliope:** Korone and Calli played Keep Talking and Nobody Explodes in Japanese and English (2020-11-27). [G2 yk2kdHkzI48]
- **FUWAMOCO:** Mio's off-collab mochi-pounding stream with the twins (2025-02-07); Okayu and Korone appeared at their
  3D debut (2024); a Lethal Company session with Fubuki and Koyori (2024). [G2 fQaE6-usUjg] [FUWAMOCO and Koyori cards]

## With the other members on the cards
- **Nakiri Ayame:** いろはにほへっとあやふぶみ (AyaFubuMi) with Fubuki and Mio (official MVs, a 2024 nabe party and
  "不純矛盾"); #鬼ヶ島コンビ with Korone (2021, 2025); a guest at GAMERS fes 2. [Official G1 listing] [G2]
- **Houshou Marine:** BABACORN with Fubuki (a duet credited "白上フブキ&宝鐘マリン"); horror and puzzle collabs. [G2]
- **AZKi:** Mio's first GeoGuessr, a Gunma "sightseeing" trip with AZKi (2024-12-29); a marshmallow chat (2025-08-18); School 666 with Korone (2026). [G2]
- **Takane Lui:** #ルイころ with Korone (2025); holoGTA and a ZIGZAG dance with Mio (2024, 2025); mahjong and
  Virtual-On off-collabs with Fubuki (2025). [G2]
- **Yukihana Lamy:** Yakamashi Musume (#やかまし娘) and #ころらみ with Korone. **Hakui Koyori:** Phasmophobia with Fubuki
  (2022) and a manzai with Korone (2022). [G2]
- **FLOW GLOW:** #ころリオ, Korone and Riona's first collab and off-collab (2025-01-22); Fubuki took Niko and Chihaya
  ghost-hunting in Phasmophobia (2025-04-20); Korone and Chihaya in R.E.P.O. (2026); Vivi gifted Korone a game (2026). [G2]

## History
| Date | Event | Source |
|---|---|---|
| 2018-06-01 | Fubuki debuts (1st generation) | [Official G1] |
| 2018-12-06 | hololive GAMERS unit PV | [G2 DPZbSlHcdfo] |
| 2018-12-07 | Mio debuts | [Official G1] |
| 2019-04-06, 04-13 | Okayu and Korone debut | [Official G1] |
| 2019 | ほろらじゲーマーズ radio; GAMERS 3D streams | [G2] |
| 2024-05 | First fan event, "超超超超ゲーマーズ," Yoyogi National Gymnasium | [G2 8Y1fLns6KY0] [Secondary G3] |
| 2024 | Formation-anniversary 3D live ("We are GAMERS !!!!") | [G2 0u8ZTalXGEc] |
| 2025-02-02 | "ワンダーフューチャー！" (Fubuki feat. Mio, Okayu, Korone) | [G2 n7ZLEzbubJs] |
| 2025-07-05 to 07-06 | "hololive GAMERS fes. 超超超超ゲーマーズ2," Saitama Super Arena | [Secondary G3] [G2] |
| 2026-08-31 | White Cat Project collaboration with the GAMERS | [G2 g9O_ctXThLE] |

## Sensory Palette
- See: four animal-eared girls side by side: a white fox with a black-tipped tail and a blue neckerchief, a
  black-haired wolf with a red streak, bells and shrine colors, a lavender cat in a grey hoodie with an onigiri, and a
  brown-braided dog in a yellow jacket and red leg warmers.
- Hear: 「こんこんきーつね！」, 「こんばんみぉーん！」, "Mogu mogu~ Okayu~!", 「ぉぁょ~！ゆびゆび～」; four voices panicking
  in a ghost hunt.

## Glossary
| Term | Meaning | Who uses it |
|---|---|---|
| GAMERS / ゲマズ | hololive GAMERS | everyone |
| フブミオ (FubuMio) | Fubuki and Mio | fans, the two |
| おかころ (OkaKoro) | Okayu and Korone | fans, the two |
| ふたりは神様MaxDOG | Mio and Korone's collab series | the two |
| あやふぶみ (AyaFubuMi) | Ayame, Fubuki and Mio | the three |
| 超ゲマズ | the GAMERS fan festivals | everyone |

## Conflicts and Story Hooks
1. A GAMERS ghost hunt where the bravest-sounding member is the first to run.
2. Korone's bakery needs four shop-minders for a day; Okayu naps, Mio reads tarot for customers, Fubuki streams it.
3. (Proposed fiction) Calli rematches Korone in a bilingual bomb-defusal game, with Mio translating.

## Links to Characters
Shirakami Fubuki; Ookami Mio; Nekomata Okayu; Inugami Korone; Nakiri Ayame; Houshou Marine; AZKi; Takane Lui; Yukihana
Lamy; Hakui Koyori; Mori Calliope; FUWAMOCO; Isaki Riona; Koganei Niko; Rindo Chihaya; Kikirara Vivi.

## Secrets
None assigned.

## Hard Facts (continuity)
- Members: Shirakami Fubuki (debut 2018-06-01; also 1st generation), Ookami Mio (2018-12-07), Nekomata Okayu
  (2019-04-06), Inugami Korone (2019-04-13).
- Fan festivals: May 2024 (Yoyogi) and 2025-07-05/06 (Saitama Super Arena).

## Sources (checked 2026-11-27)
- G1 Official profiles (English and Japanese) and their video listings:
  https://hololive.hololivepro.com/en/talents/shirakami-fubuki/, …/ookami-mio/, …/inugami-korone/,
  …/nekomata-okayu/; https://hololive.hololivepro.com/talents/shirakami-fubuki/ (Japanese) and the same for Mio and
  Korone (listed MVs: C-01aqf-oU8 "To Be Continued…," tzJm1yDe-YU and 0uPLtOQIlEk AyaFubuMi)
- G2 Stream archive metadata (archive.ragtag.moe): DPZbSlHcdfo, 2pfFq7E7keg, TDVRKtrmM-4, bg-rl4-VpTc, aWE92xAcyrk,
  8Y1fLns6KY0, 0u8ZTalXGEc, u1mdfpWU8wE, tJeo9zWQUrc, n7ZLEzbubJs, g9O_ctXThLE, yk2kdHkzI48 (Korone × Calli),
  fQaE6-usUjg (Mio × FUWAMOCO), GDOn9JNBAGA and cX-Wir_k3cE (Mio × AZKi), ktEBw4nBpMs (School 666), 4LDafBjiNdg
  (#ルイころ), UX52XaorEfY and Rjwd8WGH2kY (Mio × Lui), Xx6XUFllIO8 (#やかまし娘), hNqFWgDcvXM (manzai with Koyori),
  X19WWvT2jnk (Fubuki × Koyori), KEArX1o9sEY and ShGnwuuTMIM (AyaFubuMi), myqzgEEnV1I (#鬼ヶ島コンビ), QaGy1nHjRIQ
  (#ころリオ), yVdTbPCJytw (Fubuki with Niko and Chihaya), G6r_oZBgD3E (R.E.P.O.), LriXEkMQGAc (Vivi's gift),
  f7PhrnJWuuY and DNIi7lJ58Z8 (NYANGUCORN), ESM-OniA96w and grN8TN-eLk4 (Mio and Okayu covers)
- G3 GAMERS fes 2 announcement reports (secondary news): https://game.watch.impress.co.jp/docs/news/2026736.html ;
  https://www.inside-games.jp/article/2025/03/18/165422.html

---

## [SW] Name
hololive GAMERS

## [SW] Role
Organization

## [SW] Other Names
GAMERS, ゲマズ, ホロライブゲーマーズ

## [SW] Description
hololive GAMERS is hololive's gaming unit of four animal-eared girls, introduced with a unit video in December 2018. Shirakami Fubuki, a white-haired otaku fox who also belongs to the 1st generation, loves talking with people and wants to be a top otaku idol; Ookami Mio, a black-haired wolf girl who turned up from nowhere and haunts shrines, debuted on 2018-12-07; Nekomata Okayu, a relaxed, boyish cat, and Inugami Korone, a dog who minds a city bakery and games in her free time, debuted in April 2019. Together they ran a radio show in 2019, panic through ghost hunts and party games, and hold fan festivals: "超超超超ゲーマーズ" at Yoyogi National Gymnasium in May 2024 and "超超超超ゲーマーズ2" at Saitama Super Arena on 2025-07-05 and 07-06. They sing "To Be Continued…." and "We are GAMERS !!!!", and Fubuki's "ワンダーフューチャー！" features the other three (2025). Inside the unit: FubuMio (Fubuki and Mio), OkaKoro (Okayu and Korone), Mio and Korone's "ふたりは神様MaxDOG" and Okayu and Fubuki's NYANGUCORN covers. Outside it: Fubuki and Mio sing with Nakiri Ayame as AyaFubuMi, Korone and Ayame are the "Onigashima combo," Fubuki and Houshou Marine are BABACORN, and Korone is one of the Yakamashi Musume with Marine, Shirogane Noel and Yukihana Lamy. With the English cast, Korone played a bilingual bomb-defusal game with Mori Calliope (2020) and Mio held a mochi-pounding off-collab with FUWAMOCO (2025).

## [SW] Rules
The animal personas (fox, wolf, cat, dog) are performed lore; the members are streamers. Fubuki belongs to both the 1st generation and GAMERS. Pair names describe collab series, not exclusive relationships; collab titles show that a collab happened, not how close two members are. Festival guest lists are dated.

## [SW] Sensory Details
A white fox girl with a black-tipped tail, a white off-shoulder sailor top and a blue neckerchief; a black-haired wolf girl with a red streak, a red choker, bells and black-and-red shrine colors; a lavender cat in a grey-and-purple hoodie with an onigiri emblem; a brown-braided dog in a yellow jacket and red leg warmers with a bone clip (official key art). Greetings: 「こんこんきーつね！」, 「こんばんみぉーん！」, "Mogu mogu~ Okayu~!" and 「ぉぁょ~！ゆびゆび～」.

## [SW] Secrets
(none)

---

## Card Evidence Notes (r02, 2026-11-27)

- Profiles and greetings: official pages (English and Japanese). Unit events, songs and pairs: archived titles; the
  festival dates and venues: secondary news reports plus the members' archived recap streams. Ayame as a guest at
  GAMERS fes 2: a secondary report.
- Yakamashi Musume membership follows the Marine and Lamy cards (Marine, Noel, Lamy and Korone).

## Merge Record
- **2026-11-27, Claude only (author order: complete hololive GAMERS):** official profiles, archive metadata and news
  reports. Codex/GPT review dropped by the author (2026-11-27); a re-review by Gemini Neon (desktop) is pending.

## Open Questions
1. The exact date of the 2024 Yoyogi festival and of the formation-anniversary 3D live are not pinned here.
````

### FILE: `export/elevenlabs/Isaki-Riona.md`

````markdown
# ElevenLabs v4 Performance Sheet: Isaki Riona

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `7bbfb5e36dc890544ef7becf61f3965986ec535a13e24ab53a3179f43abaf7dc` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Isaki-Riona.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Riona is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear, bright mid-high voice with a confident, slightly cool edge; brisk and polite in set phrases, bursting into gleeful shouts when something goes her way, fiery when she loses, warm when she cheers people on."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, squeals and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (bright with big emotional swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[bright, energetic]` or `[formal, upbeat]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Welcomes viewers home: 「おかえりおな〜！」 (okaeri-ona); opens formally with 「それでは挨拶をさせてください」.
- Celebrates lucky moments at full volume; hates losing.
- Cheers people on before she leaves: 「みんなも今日一日頑張ってね」「応援してるよ」.
- Softens a sharp remark with 「好きだよ」 ("I love you"); calls Calli 「大好きなカリオペ先輩」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[bright, energetic]` | **Style demo:** 「よし、今日もいくよ！」 ("Okay, here we go today too!") |
| Opening | `[formal, upbeat]` | 「それでは挨拶をさせてください」 ("Allow me to greet you") |
| A lucky pull | `[ecstatic, shouting]` | **Style demo:** 「きたきたきた！やったぁぁ！」 |
| Losing | `[frustrated]` | **Style demo:** 「悔しい！もう一回！」 ("So frustrating! One more!") |
| Horror | `[scared]` | **Style demo:** 「無理無理無理！」 ("No no no!") |
| Cheering viewers | `[warm, encouraging]` | 「みんなも今日一日頑張ってね」 ("You all do your best today too") |
| Leading the unit | `[confident]` | **Style demo:** 「FLOW GLOW、いくよ！」 |

With people (proposed scene directions, not observed conversational defaults): Calli `[adoring, excited]`; Niko `[playful]`; Chihaya `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[squeals]` (tag only); `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): いさき りおな; おかえりおな; いさきれんごう (響咲連合). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A timid, breathy whisper, a drowsy delivery or a flat, cold read.

## 8. Example
```
[formal, upbeat] それでは挨拶をさせてください。
ROMAJI :: Soredewa aisatsu o sasete kudasai.
[ecstatic, shouting] きたきたきた！やったぁぁ！
ROMAJI :: Kita kita kita! Yattaa!
[warm, encouraging] みんなも今日一日頑張ってね。
ROMAJI :: Minna mo kyō ichinichi ganbatte ne.
```
(Lines 1 and 3 are shared ASR spans; line 2 is a Style demo. ROMAJI lines are reading aids and are not spoken.)
````

### FILE: `export/elevenlabs/Koganei-Niko.md`

````markdown
# ElevenLabs v4 Performance Sheet: Koganei Niko

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `0d88b2f464d933473ee1d90049b80e09f7ed92e3bf72237bfb6d7dfdf2ab1b56` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Koganei-Niko.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Niko is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, relaxed, slightly husky mid-range voice built for comedy; swings from pompous mock-formality to blunt, quick banter; loud and panicky when scared; warm with her fans."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, wails and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **35%** (API `0.35`) (comic swings between registers; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[playful, casual]` or `[mock-formal, theatrical]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Calls herself 「ニコたん」; her fans are 「ニコ担」 (said the same way).
- Swings from exaggerated formal apologies to blunt casual speech (「ほんまにごめん」).
- Signs off with a chant: 「ニコたんが〜、帰宅〜！」 then 「バイバ〜イ」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[playful, casual]` | **Style demo:** 「ニコたんだよ〜」 ("It's Nikotan~") |
| A bit gone wrong | `[mock-formal, theatrical]` | **Style demo:** 「誠に申し訳ございませんでした。」 ("I most humbly apologize.") |
| Banter | `[deadpan]` | 「ほんまにごめん」 ("Really sorry") |
| Signing off | `[chanting, cheerful]` | 「ニコたんが〜、帰宅〜！」 ("Nikotan is going ho~me!") |
| Horror | `[panicked]` | **Style demo:** 「ちょっ、待って待って！」 ("Wait, wait!") |
| Thanking her fans | `[warm]` | **Style demo:** 「ニコ担、いつもありがとね。」 |
| A morning show | `[groggy, upbeat]` | **Style demo:** 「おはよ〜、朝ガオの時間だよ」 |

With people (proposed scene directions, not observed conversational defaults): Riona `[teasing]`; Lui `[whiny, pleading]`; Su `[goofy]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); `[wails]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): こがねい にこ; にこたん; きたく (帰宅). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A delicate, breathy voice, prim formality held for a whole scene, or a coldly aloof read.

## 8. Example
```
[mock-formal, theatrical] 誠に申し訳ございませんでした。
ROMAJI :: Makoto ni mōshiwake gozaimasen deshita.
[deadpan] ほんまにごめん。
ROMAJI :: Honma ni gomen.
[chanting, cheerful] ニコたんが〜、帰宅〜！
ROMAJI :: Nikotan ga, kitaku!
```
(Line 1 is a Style demo; line 2 is a shared ASR span; line 3 follows the sign-off both models heard, with 帰宅 as our reading. ROMAJI lines are reading aids and are not spoken.)
````

### FILE: `export/elevenlabs/Mizumiya-Su.md`

````markdown
# ElevenLabs v4 Performance Sheet: Mizumiya Su

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `12ba35496115cd8c17eaf2951f82060fb47ae06b5df1dd1beac4c0bc8890f2b6` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Mizumiya-Su.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Su is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, light, high, sweet voice with a playful bounce; bright and quick when promoting or thanking people, pouty when teased, soft and sleepy when saying good night."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Giggles and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (sweet and steady with playful lifts; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[bubbly, sweet]` or `[sleepy, soft]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Opens with 「しゅぴしゅわ〜！すうの充電たりてる？」 and 「宣伝担当、水宮枢です」.
- Calls herself 「水宮」 (her surname) more than 「すう」; thanks people one by one.
- Leads a group goodbye: 「いきますよー、せーの！」, then 「おやすみだよー」.
- Pouts when called small. No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[bubbly, sweet]` | **Style demo:** 「水宮ね、それめっちゃ好き！」 ("Mizumiya really loves that!") |
| Opening | `[bright, upbeat]` | 「しゅぴしゅわ〜！すうの充電たりてる？」 (official line) |
| Thanking viewers | `[grateful, quick]` | **Style demo:** 「ありがとう！ありがとうね！」 |
| Promoting | `[upbeat, salesy]` | **Style demo:** 「みんな、これ見てってね！」 ("Everyone, check this out!") |
| Teased about her height | `[pouting]` | **Style demo:** 「すう、成長中だもん！」 ("I'm still growing!") |
| Signing off | `[sleepy, soft]` | 「おやすみだよー」 ("Good night~") |
| A duet partner's turn | `[cheerful]` | **Style demo:** 「次、ヴィヴィの番！」 |

With people (proposed scene directions, not observed conversational defaults): Vivi `[giggly]`; Chihaya `[cheerful]`; Marine `[bossy, playful]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[giggles]` (tag only); 「おいしょ」 ("oisho," spoken)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): みずみや すう; しゅぴしゅわ; すうりす. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A low, sultry or mature voice, cool aloofness, or a slow monotone.

## 8. Example
```
[bright, upbeat] しゅぴしゅわ〜！すうの充電たりてる？
ROMAJI :: Shupi-shuwa! Sū no jūden tariteru?
[grateful, quick] ありがとう！ありがとうね！
ROMAJI :: Arigatō! Arigatō ne!
[sleepy, soft] おやすみだよー。
ROMAJI :: Oyasumi da yo.
```
(Line 1 is her official line; line 2 is a Style demo; line 3 is a shared ASR span. ROMAJI lines are reading aids and are not spoken.)
````

### FILE: `export/elevenlabs/Rindo-Chihaya.md`

````markdown
# ElevenLabs v4 Performance Sheet: Rindo Chihaya

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `f6adc967df590e0ac30f814937563ab7f325ea2945fc03f81b025b94f0896f05` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Rindo-Chihaya.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Chihaya is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear, lively mid-range voice with a cool edge; rapid, laughing chatter, fired up for racing and DJing, softening into polite warmth late at night."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (fast and lively with soft endings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[lively, chatty]` or `[polite, soft]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Calls herself 「ちは」; opens a chat with 「こんばんはー」 and 「雑談でございます」.
- Talks without brakes, laughing, then turns polite: 「遅くまでお付き合いありがとうございました」, 「いい夢見てね」.
- Loves cars and racing; calls her fans 「ニック」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[lively, chatty]` | **Style demo:** 「ちはね、今日めっちゃ話したいことあるの！」 |
| Opening | `[casual, bright]` | 「こんばんはー」 ("Good evening~") |
| A long story | `[rapid, laughing]` | **Style demo:** 「ちょっと待って、聞いて聞いて！」 ("Wait, listen, listen!") |
| Racing | `[fired up]` | **Style demo:** 「全開でいくよ！」 ("Going full throttle!") |
| DJing | `[confident, hype]` | **Style demo:** 「みんな、声出していこう！」 |
| Signing off | `[polite, soft]` | 「遅くまでお付き合いありがとうございました」 |
| To her fans | `[warm, affectionate]` | 「いい夢見てね」 ("Sweet dreams") |

With people (proposed scene directions, not observed conversational defaults): Su `[cheerful]`; Okayu `[adoring]`; Riona `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); 「ちょっと待って」 ("chotto matte," spoken)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): りんどう ちはや; ちは; ふぐたろう (ふぐ太郎). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A shy whisper, a slow hesitant delivery, or a cold, terse read.

## 8. Example
```
[casual, bright] こんばんはー。
ROMAJI :: Konbanwa.
[rapid, laughing] ちょっと待って、聞いて聞いて！
ROMAJI :: Chotto matte, kiite kiite!
[polite, soft] ということでお疲れ様でした。遅くまでお付き合いありがとうございました。
ROMAJI :: To iu koto de otsukaresama deshita. Osoku made otsukiai arigatō gozaimashita.
[warm, affectionate] いい夢見てね。
ROMAJI :: Ii yume mite ne.
```
(Lines 1, 3 and 4 are shared ASR spans; line 2 is a Style demo. ROMAJI lines are reading aids and are not spoken.)
````

### FILE: `export/elevenlabs/Shirakami-Fubuki.md`

````markdown
# ElevenLabs v4 Performance Sheet: Shirakami Fubuki

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `a56948f6a420ca7fb1720a2467720b41aaefa4911b9adc54f556f9d843863d23` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Shirakami-Fubuki.md` (2026-11-27). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Fubuki is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, bright, clear, high voice; quick, lively and well organized like a cheerful MC; dropping into a gruff, comic register for a joke; warm and sincere when she gives advice; deadpan for a game over, then laughing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter and timbre are provisional choices for the original voice, not listening observations.
- Kurokami Fubuki, her alter ego, is a separate character with a rough register; do not use it for Fubuki's lines.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (lively but orderly; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, energetic]` or `[warm, orderly]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken; her English bits such as "Hi, Friends!" may be written in katakana,
  ハイ、フレンズ！). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- Calls herself 「白上」 (Shirakami); greets 「こんこんきーつね！白上フブキです！」 (official) or "Hi, Friends!".
- Her own words for each moment (official Q&A): 「はじまんぼう」 to start, 「おはこん」/「よるこん」 as greetings, "F" at a game over, 「おつこーん」 to end.
- Comic indignation in gruff 「～じゃい！」 / 「～やんけ！」 endings; 「キツネです！」 ("I'm a fox!") if called a cat.
- Closes in order: 「ということで、今日はこの辺りで終わっていこうと思います」, then 「ではでは」 and 「おつこーん」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[cheerful, energetic]` | **Style demo:** 「はい、今日もやっていきましょー！」 ("OK, let's get going today too!") |
| Opening | `[bright, upbeat]` | 「こんこんきーつね！白上フブキです！」 (official) |
| Called a cat | `[indignant, comic]` | 「キツネです！」 (official Q&A) |
| Game over | `[deadpan]` | **Style demo:** 「はい、F。」 ("Yep. F.") |
| Advising kouhai | `[warm, sincere]` | 「このキツネの先輩の言葉に流されず、ぜひ自分らしく配信をしてほしいです」 |
| Closing | `[warm, orderly]` | 「ということで、今日はこの辺りで終わっていこうと思います」 |
| FBKINGDOM stage | `[regal, playful]` | **Style demo:** 「フブキングダムへようこそ！」 ("Welcome to FBKINGDOM!") |

With people (proposed scene directions, not observed conversational defaults): Mio `[playful, affectionate]`; Okayu `[teasing]`; Marine `[rowdy]`; kouhai `[encouraging]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): しらかみ ふぶき; こんこんきーつね; すこんぶ (すこん部); おつこーん; はじまんぼう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A slow, sleepy drawl, a cold, aloof read or Kurokami Fubuki's rough voice.

## 8. Example
```
[bright, upbeat] こんこんきーつね！白上フブキです！
ROMAJI :: Konkon kītsune! Shirakami Fubuki desu!
[warm, sincere] このキツネの先輩の言葉に流されず、ぜひ自分らしく配信をしてほしいです。
ROMAJI :: Kono kitsune no senpai no kotoba ni nagasarezu, zehi jibunrashiku haishin o shite hoshii desu.
[warm, orderly] ということで、今日はこの辺りで終わっていこうと思います。
ROMAJI :: To iu koto de, kyō wa kono atari de owatte ikō to omoimasu.
```
(Line 1 is her official greeting; lines 2 and 3 are lines both ASR models heard. ROMAJI lines are reading aids and are not spoken.)
````

### FILE: `export/elevenlabs/Ookami-Mio.md`

````markdown
# ElevenLabs v4 Performance Sheet: Ookami Mio

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `d3d412d03fa23abf783afc6aecc896360e494b64606704e89b92a66c0ba09ccc` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Ookami-Mio.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Mio is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, warm, mellow mid-range voice, gentle and composed; even, conversational pacing like a friendly morning radio host; softer and lower late at night; grand and theatrical when she plays a fortune-teller; bright when she sings or wins."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **55%** (API `0.55`) (calm and steady by default; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[warm, gentle]` or `[soft, calm]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Calls herself 「うち」 (uchi); greets 「おはみぉーん！」 in the morning and 「こんばんみぉーん！大神ミオだよ～！」 (official) at night, stacking 「うちうち、うちだよ」 (written in her titles) before her name.
- Runs her morning show like radio: a corner reading viewers' posts, next week's theme, then goodbye.
- Signs off 「それではまた明日ねー」 or 「また明日会いましょう、じゃあねー」, then "otsu-mion" (spell it おつみぉーん in a script; untested).
- As "Big God Mion" she reads tarot in a grand, playful oracle voice.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[warm, gentle]` | **Style demo:** 「今日もゆっくりしていってね」 ("Take it easy here today too") |
| Morning opening | `[bright, cheerful]` | 「おはみぉーん！」 (her titles) |
| Reading posts | `[attentive, warm]` | **Style demo:** 「おー、おいしそう！ありがとう〜」 ("Ooh, that looks tasty! Thank you~") |
| Tarot reading | `[mysterious, playful]` | **Style demo:** 「ビッグゴッドミオーンが占ってしんぜよう」 ("Big God Mion shall read your fortune") |
| Horror | `[nervous]` | **Style demo:** 「待って待って、こわいこわい！」 ("Wait, wait, scary, scary!") |
| Late-night chat | `[soft, calm]` | **Style demo:** 「今日はまったりいこうね」 ("Let's take it slow tonight") |
| Saying goodbye | `[gentle]` | 「それではまた明日ねー」 ("Well then, see you tomorrow") |

With people (proposed scene directions, not observed conversational defaults): Fubuki `[playful, teasing]`; Korone `[amused]`; Okayu `[relaxed]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs softly]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): おおかみ みお; うち; おはみぉーん (ohamyōn); こんばんみぉーん (konbanmyōn); ミオファ (Mio-fam). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A shrill, hyper idol voice, a cold, clipped read or frantic speed.

## 8. Example
```
[bright, cheerful] おはみぉーん！
ROMAJI :: Ohamyōn!
[mysterious, playful] ビッグゴッドミオーンが占ってしんぜよう。
ROMAJI :: Biggu Goddo Mion ga uranatte shinzeyō.
[gentle] それではまた明日ねー。
ROMAJI :: Soredewa mata ashita ne.
```
(Line 1 is her written greeting; line 2 is a Style demo; line 3 is a shared ASR span. ROMAJI lines are reading aids and are not spoken.)
````

### FILE: `export/elevenlabs/Inugami-Korone.md`

````markdown
# ElevenLabs v4 Performance Sheet: Inugami Korone

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `cf8f32d96cf5bd7d4f5005175b3fe6cba398dec1ad43a89cb53af625471901c5` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Inugami-Korone.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Korone is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, high, bright, bouncy voice; drowsy and drawling in the morning; quick, playful and repetitive when tension builds; loud and triumphant when she wins; screaming and laughing through horror; warm and content when she wraps up."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, screams and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (playful with big swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[playful, energetic]` or `[sleepy, cheerful]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Greets by asking for fingers: 「ぉぁょ~！ゆびゆび～」 (official).
- On her morning show: a drowsy 「はい、おはよー」.
- Repeats herself when tension builds (「待てよ待てよ」) and plays a game to the very end.
- Can wrap up by narrating herself in the third person: 「…ころねなのであった」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[playful, energetic]` | **Style demo:** 「よーし、今日もやるぞ～！」 ("Alright, let's do this today too!") |
| Morning show | `[sleepy, cheerful]` | 「はい、おはよー」 ("OK, mornin'") |
| Waiting on a game | `[suspicious]` | **Style demo:** 「待てよ待てよ、まだ油断できない」 ("Wait, wait, can't let my guard down yet") |
| A clear | `[triumphant, shouting]` | **Style demo:** 「クリアしたああああ！」 ("I cleared it!") |
| Horror | `[screaming]` | **Style demo:** 「無理無理無理！」 ("No no no!") |
| Asking for fingers | `[mischievous]` | 「ぉぁょ~！ゆびゆび～」 (official) |
| Wrapping up | `[content, warm]` | 「なんか朝枠もいいなって思うころねなのであった」 ("And so Korone thought a morning slot is kind of nice, too") |

With people (proposed scene directions, not observed conversational defaults): Okayu `[playful, affectionate]`; Mio `[teasing]`; Marine `[rowdy]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): いぬがみ ころね; ゆび; ころねすきー (Koronesky); ぉぁょ (oayo, a stylized おはよう). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cool, low deadpan, a breathy whisper or slow solemnity.

## 8. Example
```
[mischievous] ぉぁょ~！ゆびゆび～！
ROMAJI :: Oayo~! Yubi yubi~!
[sleepy, cheerful] はい、おはよー。
ROMAJI :: Hai, ohayō.
[content, warm] なんか朝枠もいいなって思う、ころねなのであった。
ROMAJI :: Nanka asawaku mo ii natte omou, Korone na no de atta.
```
(Line 1 is her official greeting; lines 2 and 3 are lines both ASR models heard. ROMAJI lines are reading aids and are not spoken.)
````

### FILE: `research/audio-check/flowglow.md`

````markdown
# Audio check — FLOW GLOW: Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya (2026-11-27)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment), the first
8 minutes and the last 7 minutes of two streams per member, transcribed in Japanese with faster-whisper small
(multilingual), pitch measured with Praat (100–600 Hz, speech segments only). Tools and limits:
`novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was machine-transcribed and
acoustically measured, and the transcripts were reviewed in context. Lines used on the character cards were
re-transcribed by a second model (whisper medium, multilingual, a 30-second clip around the line) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Japanese ASR often picks different
kanji or kana for the same word, and both models mishear names and coined words; only spans both models render the
same way are quoted, and coined words heard as near-matches are reported in romaji. Opening music and game audio
cover some greetings, so "not heard" does not mean "not said". Measurements describe the sampled recording and ASR
segmentation; game audio, music and singing prevent treating them as isolated vocal measurements.

Riona's and Niko's windows are from 2026; Su's and Chihaya's are from August 2025 (no 2026 chat stream of theirs was
picked by the selection rule), so their 2026 manner rests on titles. Only in-scope public performance material is
used: personal remarks in the chats are not quoted or summarized here, and stream labels are neutral.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| riona_open_uH9A | [2026-10-15 morning game stream — Isaki Riona](https://youtu.be/uH9AFj1qbyA) | [0:00:00–0:08:00](https://youtu.be/uH9AFj1qbyA?t=0) | 2.6 | 725 | 276.1 | 273 Hz | 118–444 Hz |
| riona_end_uH9A | (same stream) | [0:59:06–1:06:06](https://youtu.be/uH9AFj1qbyA?t=3546) | 3.2 | 1038 | 327.3 | 270 Hz | 197–458 Hz |
| riona_open_WJz- | [2026-10-20 morning game stream — Isaki Riona](https://youtu.be/WJz-YOx6fsE) | [0:00:00–0:08:00](https://youtu.be/WJz-YOx6fsE?t=0) | 2.6 | 787 | 298.9 | 256 Hz | 184–360 Hz |
| riona_end_WJz- | (same stream) | [0:57:46–1:04:46](https://youtu.be/WJz-YOx6fsE?t=3466) | 3.5 | 1108 | 321.1 | 273 Hz | 190–416 Hz |
| niko_open_7NOh | [2026-08-08 朝ガオ episode — Koganei Niko](https://youtu.be/7NOhe2tKZLA) | [0:00:00–0:08:00](https://youtu.be/7NOhe2tKZLA?t=0) | 3.8 | 1070 | 281.0 | 292 Hz | 207–425 Hz |
| niko_end_7NOh | (same stream) | [0:52:53–0:59:53](https://youtu.be/7NOhe2tKZLA?t=3173) | 3.7 | 1115 | 298.0 | 263 Hz | 180–428 Hz |
| niko_open_MmkP | [2026-09-12 朝ガオ vol.14 — Koganei Niko](https://youtu.be/MmkPfYSIJ0s) | [0:00:00–0:08:00](https://youtu.be/MmkPfYSIJ0s?t=0) | 3.1 | 377 | 121.9 | 336 Hz | 208–547 Hz |
| niko_end_MmkP | (same stream) | [0:52:12–0:59:12](https://youtu.be/MmkPfYSIJ0s?t=3132) | 5.1 | 1935 | 375.8 | 286 Hz | 194–477 Hz |
| su_open_8fyV | [2025-08-22 morning chat — Mizumiya Su](https://youtu.be/8fyVCoPWMb8) | [0:00:00–0:08:00](https://youtu.be/8fyVCoPWMb8?t=0) | 5.0 | 1288 | 258.8 | 288 Hz | 131–432 Hz |
| su_end_8fyV | (same stream) | [2:14:30–2:21:30](https://youtu.be/8fyVCoPWMb8?t=8070) | 4.4 | 1470 | 334.9 | 301 Hz | 149–480 Hz |
| su_open_ZIke | [2025-08-09 late-night chat — Mizumiya Su](https://youtu.be/ZIkex-Hye6E) | [0:00:00–0:08:00](https://youtu.be/ZIkex-Hye6E?t=0) | 4.9 | 1579 | 323.4 | 312 Hz | 156–471 Hz |
| su_end_ZIke | (same stream) | [2:25:34–2:32:34](https://youtu.be/ZIkex-Hye6E?t=8734) | 3.8 | 1417 | 370.9 | 308 Hz | 152–491 Hz |
| chihaya_open_kNFi | [2025-08-21 late-night chat — Rindo Chihaya](https://youtu.be/kNFiSEYSUeo) | [0:00:00–0:08:00](https://youtu.be/kNFiSEYSUeo?t=0) | 3.7 | 1192 | 326.3 | 248 Hz | 168–443 Hz |
| chihaya_end_kNFi | (same stream) | [2:29:50–2:36:50](https://youtu.be/kNFiSEYSUeo?t=8990) | 4.2 | 1213 | 287.4 | 291 Hz | 198–427 Hz |
| chihaya_open_dtVU | [2025-08-09 chat — Rindo Chihaya](https://youtu.be/dtVUhrM1cPQ) | [0:00:00–0:08:00](https://youtu.be/dtVUhrM1cPQ?t=0) | 3.9 | 1176 | 301.1 | 208 Hz | 150–302 Hz |
| chihaya_end_dtVU | (same stream; mostly singing) | [2:23:12–2:30:12](https://youtu.be/dtVUhrM1cPQ?t=8592) | 4.1 | 544 | 131.7 | 220 Hz | 173–301 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech
segments; it is a rough pace index for comparing windows, not a mora count. niko_open_MmkP is mostly opening music
(121.9 characters a minute) and chihaya_end_dtVU is mostly singing; both are excluded from the ranges on the cards.

## Marker counts (first model, four windows per member)

| Marker | Riona | Niko | Su | Chihaya |
|---|---|---|---|---|
| ニコたん (self) | 0 | 23 | 0 | 0 |
| 水宮 (self) | 0 | 0 | 30 | 0 |
| すう/スー | 0 | 0 | 12 | 0 |
| ちは (self) | 0 | 0 | 0 | 4 |
| リオナ | 3 | 0 | 0 | 0 |
| ほんま | 1 | 2 | 0 | 0 |
| めっちゃ | 3 | 1 | 18 | 4 |
| マジ | 4 | 4 | 5 | 5 |
| なんか | 4 | 15 | 24 | 20 |
| ちょっと待って | 4 | 0 | 0 | 7 |
| ありがとう | 10 | 6 | 57 | 7 |
| かわいい | 6 | 3 | 8 | 1 |
| English (Latin letters) | 5 | 10 | 36 | 2 |

## Claims checked

| Claim in the files | Result (in the machine transcripts) | Evidence (ASR, archived audio) |
|---|---|---|
| Riona welcomes viewers with "okaeri-ona" | **Observed by the second model only** (twice, just before her greeting); the first model's transcript starts after it. Her descriptions write 「おかえりおな〜！」. | [0:03:40](https://youtu.be/uH9AFj1qbyA?t=220) |
| Riona's formal opening | **Observed**: 「それでは挨拶をさせてください」, then "in da house" and FLOW GLOW's leader with her name (the name is misheard differently by each model). | [0:03:42](https://youtu.be/uH9AFj1qbyA?t=222) |
| Riona's sign-off | **Observed**: "bye-bye," a coined "otsu-Riona" (near-match in both models), and in morning streams a cheer for the viewers' day. | [1:04:03](https://youtu.be/uH9AFj1qbyA?t=3843), [1:02:51](https://youtu.be/WJz-YOx6fsE?t=3771) |
| Riona's ending video | **Observed** in both streams: a calm "mindfulness" voice-over that ends by asking viewers to post with the fans' hashtag, subscribe and comment. Paraphrased, not quoted. | [1:03:00](https://youtu.be/WJz-YOx6fsE?t=3780) |
| Niko calls herself "Nikotan" | **Observed** about two dozen times. | [0:58:22](https://youtu.be/MmkPfYSIJ0s?t=3502) |
| Niko's sign-off call | **Observed** in both episodes: "Nikotan ga… kitaku" (both models write 来たく), then "bye-bye." | [0:58:26](https://youtu.be/7NOhe2tKZLA?t=3506), [0:58:22](https://youtu.be/MmkPfYSIJ0s?t=3502) |
| Su's opening | **Observed** in both streams: the coined "shupi-shuwa" (near-match), "Su-charge" and "publicity manager Mizumiya Su." | [0:01:35](https://youtu.be/8fyVCoPWMb8?t=95), [0:01:20](https://youtu.be/ZIkex-Hye6E?t=80) |
| Su calls herself "Mizumiya" | **Observed** about thirty times. | [0:03:36](https://youtu.be/8fyVCoPWMb8?t=216) |
| Su's group goodbye | **Observed** in both streams: "Here we go, ready, set!" then a group "otsu~"; the word after "otsu" differs between the models; "good night." | [2:20:04](https://youtu.be/8fyVCoPWMb8?t=8404), [2:31:12](https://youtu.be/ZIkex-Hye6E?t=9072) |
| Chihaya calls herself "Chiha" | **Observed** (the first model sometimes writes 自派). | [0:06:46](https://youtu.be/kNFiSEYSUeo?t=406), [2:34:11](https://youtu.be/kNFiSEYSUeo?t=9251) |
| Chihaya's polite sign-off | **Observed** in one stream verbatim in both models; "sweet dreams" in both streams. | [2:36:04](https://youtu.be/kNFiSEYSUeo?t=9364), [2:29:17](https://youtu.be/dtVUhrM1cPQ?t=8957) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "それでは挨拶をさせてください" | [0:03:42](https://youtu.be/uH9AFj1qbyA?t=222) | "…かえりょうなーそれでは、あいさつをさせてくださいわたしのもとに…" | Agrees (spelling): the second model writes あいさつ in kana; same words. |
| "フログローのりだ いさきにゃんなねーす" | [0:03:48](https://youtu.be/uH9AFj1qbyA?t=228) | "…インダハンスフログロウのリーダー、いさきりょうなでーす…" | **Partly agrees:** both models hear "in da house" before it and FLOW GLOW's leader with her name; the name is misheard differently, so the line is reported, not quoted |
| "おちにょらでした" | [1:04:03](https://youtu.be/uH9AFj1qbyA?t=3843) | "…バイバーイおつによらでしたーありがと…" | **Not confirmed** as a quotation: both models hear a near-match of a coined sign-off; reported in romaji as "otsu-Riona" |
| "おちによなー" | [1:02:51](https://youtu.be/WJz-YOx6fsE?t=3771) | "…バイバーイありがとーオチリオナーありがとー…" | **Not confirmed** as a quotation: a near-match, as above |
| "ありがとうみんなも今日一日頑張ってね" | [1:04:06](https://youtu.be/uH9AFj1qbyA?t=3846) | "…ありがとみんなも今日一日頑張ってね応援してるよバイバーイ…" | **Partial (computed):** shared run "みんなも今日一日頑張ってね" |
| "応援してるよ" | [1:04:08](https://youtu.be/uH9AFj1qbyA?t=3848) | "…今日一日頑張ってね応援してるよバイバーイ…" | **Shared span (computed):** whole line |
| "それではニコタンが来たくてよろしくお願いします" | [0:58:26](https://youtu.be/7NOhe2tKZLA?t=3506) | "…それではにこたんが来たくでよろしくお願いしますにこたんが来たくバイバーイ…" | Agrees (spelling): both models write 来たく for "kitaku"; the card writes 帰宅 ("going home") as our reading; one model has the particle て, the other で. |
| "それじゃあ2個担が来たくでお願いします" | [0:58:22](https://youtu.be/MmkPfYSIJ0s?t=3502) | "…それじゃあにこたんが来たーくでお願いしますにこたんがー来たーくーばいばーい" | Agrees (spelling): the first model writes 2個担 (read "niko-tan," like ニコたん); both write 来たく. |
| "ほんまにごめん" | [0:58:01](https://youtu.be/7NOhe2tKZLA?t=3481) | "…ほんまにごめんほんまにごめん…" | **Shared span (computed):** whole line |
| "シピシワースーの充電足りてる?" | [0:01:35](https://youtu.be/8fyVCoPWMb8?t=95) | "…シュピシュワースーの充電足りてる…" | **Partial (computed):** shared run "すの充電足りてる"; the coined opening is a near-match (シピシワー / シュピシュワー); the card uses the official spelling |
| "…依頼宣伝担当水宮数です" | [0:01:39](https://youtu.be/8fyVCoPWMb8?t=99) | "…フローグルの依頼宣伝担当水宮数ですお願いします…" | Agrees (spelling): both models write 水宮数 for 水宮枢 (same reading すう); the card quotes 「宣伝担当、水宮枢です」. |
| "いきますよーせーのー" | [2:20:04](https://youtu.be/8fyVCoPWMb8?t=8404) | "…いきますよ、せーのおつ…" | **Shared span (computed):** whole line |
| "おつすれお願いします!" | [2:31:12](https://youtu.be/ZIkex-Hye6E?t=9072) | "…お手伝いお願いします!いきますよーせーの!おうつー…" | **Not confirmed**: the word after "otsu" differs (おつすれ / お手伝い; おつすめ in the other stream); not quoted |
| "おやすみだよー!" | [2:31:16](https://youtu.be/ZIkex-Hye6E?t=9076) | "…おやすみだよーバイバーイ!" | **Shared span (computed):** whole line |
| "こんばんはーということ自雑談でございます" | [0:03:32](https://youtu.be/kNFiSEYSUeo?t=212) | "…こんばんはということで雑談でございますちょっと遅れちゃって…" | **Partial (computed):** shared runs "こんばんはということ" and "雑談でございます"; one mora differs between the models, so only the shared parts are quoted |
| "ということでお疲れ様でした" | [2:36:04](https://youtu.be/kNFiSEYSUeo?t=9364) | "…ということでお疲れ様でした遅くまでお付き合いありがとうございましたまたねー…" | **Shared span (computed):** whole line |
| "遅くまでお付き合いありがとうございました" | [2:36:05](https://youtu.be/kNFiSEYSUeo?t=9365) | "…ということでお疲れ様でした遅くまでお付き合いありがとうございましたまたねー…" | **Shared span (computed):** whole line |
| "いい夢見てね" | [2:36:19](https://youtu.be/kNFiSEYSUeo?t=9379) | "…出てくるといいねいい夢見てねおや…" | **Shared span (computed):** whole line |
| "夢見てね、みんなのおかげで9ヶ月でした" | [2:29:17](https://youtu.be/dtVUhrM1cPQ?t=8957) | "…夢見てねーみんなのおかげで9ヶ月でした1周年までもっともっと…" | **Shared span (computed):** whole line |
| "ニクたち大好きだよ" | [2:29:32](https://youtu.be/dtVUhrM1cPQ?t=8972) | "…これからもよろしくお願いしますニックたち大好きだよ…" | Agrees (spelling): the second model writes ニック, her fans' name; the first writes ニク. |

Per-line output of the second model: scratch file `jconfirm` run of 2026-11-27 (14 clips); the excerpts above are
copied from it, trimmed to the quoted line and cleared of personal remarks.
````

### FILE: `research/audio-check/gamers.md`

````markdown
# Audio check — hololive GAMERS: Shirakami Fubuki, Ookami Mio, Inugami Korone (2026-11-27)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment), the first
8 minutes and the last 7 minutes of each stream, transcribed in Japanese with faster-whisper small (multilingual),
pitch measured with Praat (100–600 Hz, speech segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`.
**This is not a listening check**: the audio was machine-transcribed and acoustically measured, and the transcripts
were reviewed in context. Lines used on the character cards were re-transcribed by a second model (whisper medium,
multilingual, a 30-second clip around the line) and compared after folding katakana to hiragana and dropping
punctuation (see the end of this file). Japanese ASR often picks different kanji or kana for the same word, and both
models mishear names and coined words; only spans both models render the same way are quoted, and coined words heard
as near-matches are reported in romaji or in the member's own written spelling (official profile, stream titles).
Opening music and game audio cover some greetings, so "not heard" does not mean "not said". Measurements describe the
sampled recording and ASR segmentation; game audio, music and singing prevent treating them as isolated vocal
measurements.

All windows are from 2026. Fubuki has six streams (five solo, one collab with Omaru Polka, used for measurement
only), because her first picks did not capture a clean greeting; Mio and Korone have two each. Only in-scope public
performance material is used: personal remarks in the chats are not quoted or summarized here, and stream labels are
neutral.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| fubuki_open_0kjX | [2026-10-05 birthday-live thank-you talk — Shirakami Fubuki](https://youtu.be/0kjXUGCIoZU) | [0:00:00–0:08:00](https://youtu.be/0kjXUGCIoZU?t=0) | 5.8 | 1976 | 341.3 | 336 Hz | 223–508 Hz |
| fubuki_end_0kjX | (same stream) | [1:07:52–1:14:52](https://youtu.be/0kjXUGCIoZU?t=4072) | 5.6 | 2189 | 393.6 | 324 Hz | 233–506 Hz |
| fubuki_open_GSMy | [2026-06-03 event pep-rally chat — Shirakami Fubuki](https://youtu.be/GSMyPNRANvc) | [0:00:00–0:08:00](https://youtu.be/GSMyPNRANvc?t=0) | 4.9 | 1627 | 332.0 | 326 Hz | 198–478 Hz |
| fubuki_end_GSMy | (same stream) | [1:04:35–1:11:35](https://youtu.be/GSMyPNRANvc?t=3875) | 5.5 | 1954 | 355.4 | 321 Hz | 222–505 Hz |
| fubuki_open_avWv | [2026-06-26 Star Fox stream — Shirakami Fubuki](https://youtu.be/avWvfYnaOQE) | [0:00:00–0:08:00](https://youtu.be/avWvfYnaOQE?t=0) | 2.0 | 539 | 273.3 | 302 Hz | 138–493 Hz |
| fubuki_end_avWv | (same stream) | [2:12:17–2:19:17](https://youtu.be/avWvfYnaOQE?t=7937) | 3.7 | 1103 | 301.8 | 306 Hz | 150–505 Hz |
| fubuki_open__vvb | [2026-09-18 pre-debut "delusion profile" stream — Shirakami Fubuki](https://youtu.be/_vvbn7kgqj4) | [0:00:00–0:08:00](https://youtu.be/_vvbn7kgqj4?t=0) | 3.0 | 916 | 306.3 | 350 Hz | 243–522 Hz |
| fubuki_end__vvb | (same stream) | [1:53:24–2:00:24](https://youtu.be/_vvbn7kgqj4?t=6804) | 5.3 | 1521 | 286.1 | 354 Hz | 236–533 Hz |
| fubuki_open_gbCs | [2026-10-11 Hollow Knight: Silksong #2 — Shirakami Fubuki](https://youtu.be/gbCsK3KnVVE) | [0:00:00–0:08:00](https://youtu.be/gbCsK3KnVVE?t=0) | 3.1 | 815 | 264.3 | 326 Hz | 218–515 Hz |
| fubuki_end_gbCs | (same stream) | [2:21:18–2:28:18](https://youtu.be/gbCsK3KnVVE?t=8478) | 3.6 | 1084 | 305.0 | 315 Hz | 137–501 Hz |
| fubuki_open_zTD4 | [2026-09-15 chill radio collab with Omaru Polka — Shirakami Fubuki](https://youtu.be/zTD4n-B41u4) | [0:00:00–0:08:00](https://youtu.be/zTD4n-B41u4?t=0) | 4.9 | 1762 | 360.7 | 318 Hz | 205–505 Hz |
| fubuki_end_zTD4 | (same stream) | [1:49:02–1:56:02](https://youtu.be/zTD4n-B41u4?t=6542) | 5.9 | 2436 | 411.3 | 288 Hz | 204–474 Hz |
| mio_open_v49b | [2026-10-11 #朝ミオ morning show — Ookami Mio](https://youtu.be/v49bZ8yH0I0) | [0:00:00–0:08:00](https://youtu.be/v49bZ8yH0I0?t=0) | 5.7 | 1019 | 178.9 | 248 Hz | 130–396 Hz |
| mio_end_v49b | (same stream) | [1:04:40–1:11:40](https://youtu.be/v49bZ8yH0I0?t=3880) | 3.9 | 1060 | 271.4 | 249 Hz | 167–446 Hz |
| mio_open_3b1W | [2026-09-18 quiet late-night chat — Ookami Mio](https://youtu.be/3b1W_NGeIgs) | [0:00:00–0:08:00](https://youtu.be/3b1W_NGeIgs?t=0) | 3.9 | 1076 | 275.9 | 203 Hz | 171–282 Hz |
| mio_end_3b1W | (same stream) | [1:21:40–1:28:40](https://youtu.be/3b1W_NGeIgs?t=4900) | 3.3 | 998 | 304.7 | 197 Hz | 164–267 Hz |
| korone_open_Zlnq | [2026-05-03 朝ころ first episode — Inugami Korone](https://youtu.be/Zlnqxdwg5Io) | [0:00:00–0:08:00](https://youtu.be/Zlnqxdwg5Io?t=0) | 4.7 | 956 | 203.2 | 301 Hz | 204–454 Hz |
| korone_end_Zlnq | (same stream) | [0:53:34–1:00:34](https://youtu.be/Zlnqxdwg5Io?t=3214) | 3.3 | 787 | 238.2 | 321 Hz | 235–452 Hz |
| korone_open_alUD | [2026-10-20 game stream — Inugami Korone](https://youtu.be/alUDRkSYyc8) | [0:00:00–0:08:00](https://youtu.be/alUDRkSYyc8?t=0) | 4.2 | 1105 | 261.4 | 295 Hz | 204–463 Hz |
| korone_end_alUD | (same stream) | [2:01:53–2:08:53](https://youtu.be/alUDRkSYyc8?t=7313) | 5.1 | 1077 | 209.9 | 257 Hz | 117–441 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech
segments; it is a rough pace index for comparing windows, not a mora count. mio_open_v49b is partly opening music
(178.9 characters a minute) and is excluded from the pace range on Mio's card; the late-night chat is billed as a
quiet stream, so its narrow pitch range reflects the format. korone_end_alUD has game audio throughout (its low p10
is not her voice alone). fubuki_*_zTD4 is a two-person collab and is not used for her ranges.

## Marker counts (first model)

| Marker | Fubuki (10 windows) | Mio (4) | Korone (4) |
|---|---|---|---|
| 白上 / 白紙 / しらかみ (Fubuki's self-reference; 白紙 is the first model's spelling of しらかみ) | 10 | 0 | 0 |
| うち (Mio's "I") | — | 20 | 2 |
| ころね / コロネ | 0 | 0 | 1 |
| ではではでは | 4 | 0 | 0 |
| なんか | 47 | 16 | 13 |
| ちょっと待って | 4 | 0 | 7 |
| ありがとう | 11 | 4 | 10 |
| めっちゃ | 4 | 1 | 0 |
| マジ | 4 | 0 | 2 |
| かわいい | 8 | 0 | 0 |
| English (Latin letters) | 16 | 11 | 12 |

Fubuki's うち count (12) is not shown: in her windows it is the ordinary word ("our," "inside"), not a pronoun.

## Claims checked

| Claim in the files | Result (in the machine transcripts) | Evidence (ASR, archived audio) |
|---|---|---|
| Fubuki calls herself 白上 (Shirakami) | **Observed**: about ten times (the first model writes 白紙, the second しらかみ; both are the reading Shirakami). Her official Q&A uses 白上 the same way. | [0:02:03](https://youtu.be/0kjXUGCIoZU?t=123), [0:03:53](https://youtu.be/gbCsK3KnVVE?t=233) |
| Fubuki's greetings | **Partly observed**: her name plus 「でーす」 in both models; "Hi, Friends!" heard as a near-match by both (ハイフレーンズー / ハイフレーズ / はーいフェーズ); the evening 「こんばんきーつねー」 heard by the second model only, once. Her official profile lists 「こんこんきーつね！」, "Hi, Friends!" and the others; the card relies on that. | [0:02:03](https://youtu.be/0kjXUGCIoZU?t=123), [0:03:53](https://youtu.be/gbCsK3KnVVE?t=233) |
| Fubuki's closing formula | **Observed** in three streams: 「といったところで」 / 「ということで」 + "today we'll end around here," then 「ではでは」. | [1:13:15](https://youtu.be/0kjXUGCIoZU?t=4395), [1:59:37](https://youtu.be/_vvbn7kgqj4?t=7177), [2:27:12](https://youtu.be/gbCsK3KnVVE?t=8832) |
| Fubuki's sign-off "otsukon" | **Observed as a near-match** in four streams: the second model writes おつこん (でした / でございました) three times and オスコン once; the first model writes おつこみ, おつかん, おつとん. The official profile spells it 「おつこーん」. | [1:14:19](https://youtu.be/0kjXUGCIoZU?t=4459), [1:11:25](https://youtu.be/GSMyPNRANvc?t=4285), [2:27:12](https://youtu.be/gbCsK3KnVVE?t=8832) |
| Fubuki's advice to the newcomers | **Observed** in both models: don't be swayed by "this fox senpai," stream your own way. | [1:58:45](https://youtu.be/_vvbn7kgqj4?t=7125) |
| Mio calls herself うち | **Observed** about twenty times; her greeting stacks it (the second model hears 「うちうちうちだよ」 in both streams; the first model 「すっちうち うちだよ」 once and 「うちだよー」 once). Her 2021 title writes 「うちうち、うちだよ」. | [0:01:52](https://youtu.be/v49bZ8yH0I0?t=112), [0:01:56](https://youtu.be/3b1W_NGeIgs?t=116) |
| Mio's greetings | **Observed as near-matches**: the morning 「おはみぉーん」 (おはみよー / オハ見用) and the evening 「こんばんみぉーん」 (こんばんみょーん / こんばんみよ). Her titles write 「おはみぉーん」; the official profile 「こんばんみぉーん！大神ミオだよ～！」. | [0:01:59](https://youtu.be/v49bZ8yH0I0?t=119), [0:01:59](https://youtu.be/3b1W_NGeIgs?t=119) |
| Mio's sign-offs | **Observed**: 「それではまた明日ねー」 and 「また明日会いましょう、じゃあねー」, each followed by a coined "otsu-mion" (a near-match in both models). | [1:10:36](https://youtu.be/v49bZ8yH0I0?t=4236), [1:26:44](https://youtu.be/3b1W_NGeIgs?t=5204) |
| Mio's morning-show format | **Observed**: a corner reading viewers' posts on a weekly theme, the theme for next week, then goodbye. Paraphrased, not quoted. | [1:10:00](https://youtu.be/v49bZ8yH0I0?t=4200) |
| Korone's morning opening | **Observed**: 「はい、おはよー」 in both models. | [0:01:50](https://youtu.be/Zlnqxdwg5Io?t=110) |
| Korone narrates herself in the third person | **Observed** once, in both models, at the end of the first 朝ころ. | [0:59:55](https://youtu.be/Zlnqxdwg5Io?t=3595) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "朝みょでーす すっちうち うちだよ 大神みょだよー おはみよー" | [0:01:50](https://youtu.be/v49bZ8yH0I0?t=110) | "…朝見用ですウチウチウチだよオオカミ見用だよオハ見用…" | **Partly agrees:** both models hear "うちうちだよ" and her name with "だよ" (both mishear ミオ); the second model hears three うち; the coined greeting is a near-match (おはみよー / オハ見用), so the card uses the spelling of her titles, 「おはみぉーん」, and her 2021 title for 「うちうち、うちだよ」 |
| "それではまた明日ねー おつみよう" | [1:10:36](https://youtu.be/v49bZ8yH0I0?t=4236) | "…来週のアサミオもよろしくお願いいたしますそれでは また明日ねーおつみよー" | **Partial (computed):** shared run "それではまた明日ね"; the coined sign-off is a near-match (おつみよう / おつみよー), reported in romaji as "otsu-mion" |
| "うちだよー おかみみよだよー こんばんみょーん" | [0:01:56](https://youtu.be/3b1W_NGeIgs?t=116) | "…うちうちうちだよオオカミミオだよこんばんみよ今日はまったりしっとり行きたいと思います" | **Partly agrees:** both models hear "うちだよ", her name with "だよ" and a near-match of the evening greeting (こんばんみょーん / こんばんみよ); the card uses the official spelling 「こんばんみぉーん！大神ミオだよ～！」 |
| "ということで皆さんありがとうございました また明日会いましょう じゃあねー おつみようー" | [1:26:40](https://youtu.be/3b1W_NGeIgs?t=5200) | "…よろしくお願いしますということで皆さんありがとうございましたまた明日会いましょうじゃあねおつみよー" | **Partial (computed):** shared run "ということで皆さんありがとうございましたまた明日会いましょうじゃあね"; the coined sign-off is a near-match (おつみようー / おつみよー) |
| "はいおはよう おはよう" | [0:01:50](https://youtu.be/Zlnqxdwg5Io?t=110) | "はい、おはよーおはよー…" | Agrees (spelling): おはよう / おはよー, a long-vowel spelling; same words. |
| "楽しかった! なんか朝訳もいいなって思う コロネなのであった" | [0:59:52](https://youtu.be/Zlnqxdwg5Io?t=3592) | "…みんな、朝ありがとうね、楽しかったなんか朝枠もいいなって思うコロネなのであった…" | Agrees (spelling): the first model writes 朝訳 for 朝枠 ("morning slot," same reading); both write コロネ, which the card writes ころね, the spelling of her name. |
| "撮っていた白紙でーす! ハイフレーンズー!" | [0:02:03](https://youtu.be/0kjXUGCIoZU?t=123) | "はい!明日配信予約を取っていたしらかみでーす!ハイフレーズ!…" | **Partly agrees:** both models hear her name (白紙 / しらかみ, read Shirakami) with "でーす" and a near-match of "Hi, Friends!" (ハイフレーンズー / ハイフレーズ); her official profile lists "Hi, Friends!" as her signature greeting; reported, not quoted from ASR |
| "はい!ではではでは! おつこみです!" | [1:14:19](https://youtu.be/0kjXUGCIoZU?t=4459) | "…はいではではでは落ちコンでしたおやすみなさーい" | **Partly agrees:** shared "はいではではでは"; the sign-off is a near-match (おつこみです / 落ちコンでした); her official profile spells it 「おつこーん」 |
| "はい、といたところで 今日はこの辺で終わっていこうかなと思っております" | [1:13:15](https://youtu.be/0kjXUGCIoZU?t=4395) | "…といったところで今日はこの辺で終わっていこうかなと思っておりまーす…" | **Partial (computed):** shared run "ところで今日はこの辺で終わっていこうかなと思っており"; the first model drops the small っ of といったところで ("with that said"), so the card quotes 「といったところで」 as the second model and the other streams have it |
| "おつかん!" | [1:11:25](https://youtu.be/GSMyPNRANvc?t=4285) | "…アルケミストの定めを背負って頑張りましょー!オスコンでしたー!" | **Not confirmed** as a quotation: both models hear a near-match of "otsukon" (おつかん / オスコン) |
| "白紙でーす はい! さて、シルクソングを続きやっていこうと思います!" | [0:03:53](https://youtu.be/gbCsK3KnVVE?t=233) | "はいみなさんどうもこんばんきーつねー 白紙でーすはーいフェーズさてシルクソング続きやっていこうと思います…" | **Partly agrees:** both models hear "白紙でーす" (her name, Shirakami) and "続きやっていこうと思います"; only the second model hears the greeting before it, 「はいみなさんどうもこんばんきーつねー」, and a near-match of "Hi, Friends!" after it, so the evening greeting is reported, not quoted as verified |
| "といたところで皆さんおつとんでございました また次回一かじかやろうと思います" | [2:27:12](https://youtu.be/gbCsK3KnVVE?t=8832) | "…といったところで皆さんおつこんでございましたまた次回、いちかじかやろうと思いますではでは、おつこんでした今日もありがとうございました…" | **Partly agrees:** shared "でございましたまた次回"; the sign-off word is a near-match in the first model (おつとん) and おつこん in the second, which also hears "ではでは、おつこんでした" |
| "ではでは 今日もありがとうございました" | [2:27:19](https://youtu.be/gbCsK3KnVVE?t=8839) | "…ではでは、おつこんでした今日もありがとうございました…" | **Partial (computed):** shared runs "ではでは" and "今日もありがとうございました" |
| "ということで、今日はこの辺りで終わっていこうと思います" | [1:59:37](https://youtu.be/_vvbn7kgqj4?t=7177) | "…ということで今日はこのあたりで終わっていこうと思います勝手に妄想プロフィール楽しかったです…ではではおつこんでした" | Agrees (spelling): 辺り / あたり; same words. The second model also hears "ではではおつこんでした" after it. |
| "このキツネの先輩の言葉に流されず是非自分らしく配信をしてほしいです" | [1:58:45](https://youtu.be/_vvbn7kgqj4?t=7125) | "新人の諸君遊び回り隊の諸君この配信を見ていたらこのキツネの先輩の言葉に流されずぜひ自分らしく配信をしてほしいです…" | Agrees (spelling): 是非 / ぜひ; same words. |

Per-line output of the second model: scratch files `jconfirm` runs of 2026-11-27 (15 clips); the excerpts above are
copied from them, trimmed to the quoted line and cleared of personal remarks.
````

### FILE: `research/qa/audit-flowglow.md`

````markdown
# Cohort audit: flowglow (Riona, Niko, Su, Chihaya, FLOW GLOW; Claude self-check 2026-11-27; Gemini Neon review pending)

**What this file is.** The other cohort audits are GPT cross-card audits merged by Claude. This one is not: the
FLOW GLOW cards were added on the author's order of 2026-11-27, and the Codex login that the framework uses for GPT
was blocked in this session, so Claude researched, wrote and checked them alone. The file records the checks Claude
ran and what they found, so that V11, V12, V14 and V15 have a written review to point to. On 2026-11-27 the
author decided not to use the Codex/GPT audit and to have Gemini Neon (desktop) re-review the work instead; the
packets are in `research/qa/external-review/`, and Gemini's findings will be merged here.

Scope: `bible/characters/Isaki-Riona.md`, `Koganei-Niko.md`, `Mizumiya-Su.md`, `Rindo-Chihaya.md`,
`bible/world/FLOW-GLOW.md`, their performance sheets, `research/audio-check/flowglow.md`, and the FLOW GLOW lines
added to ten existing cards (Calli, Nerissa, Marine, Lamy, AZKi, Koyori, Okayu, Lui, Chloe, Vivi).

## Checks run

| Check | How | Result |
|---|---|---|
| Dates and status (V10-type) | Each date traced to the official debut announcement, the official music catalog (release dates read from each entry), archived titles, or a named news report | All five members active; debut 2024-11-09 (PST relay start noted); 3D debut live 2025-11-23 (news report plus official #FG3Dライブ videos); festival debut 2026-03-07 (news report plus official listing). Vivi's dossier dates for "good enough" (09-20 → 2025-09-21) and "magic summer" (08-18 → 2026-08-19) corrected to the official release dates. |
| Participants and direction (V11) | Every tie checked from both channels where the archive has both; `tools/web_check.py` for coverage | Ten existing cards now name the FLOW GLOW members they share collabs with. Five ties stay one-way and are coverage notes, not errors: Riona → IRyS, Bijou, Nerissa (dance shorts of her song); Chihaya → Suisei (covers of Suisei's songs), Calli (a watch-along). Covers are credited per song; a dance short on a channel does not establish who performed the motion. |
| Evidence records (V12) | Each [SW] claim matched to a dossier line with a source ID | Every claim has an official page, an archive ID, a row in the audio report or a named secondary source. Secondary-only items are labelled (the unit fan name FLOMIE stays off the cards; Su's height history is marked secondary). A song the earlier research note listed for 2025-02-05 is not in the official catalog and is not used. |
| Quotations and ASR (V13) | `tools/span_check.py holoen` | 0 quotations outside a shared span. Two quotes were tightened during this check: Chihaya's opening is quoted only in the parts both models share; a joined Riona quote was split into its two shared spans. Coined words heard as near-matches ("otsu-Riona," the word after Su's group "otsu") are not quoted as verified lines. |
| Scope screening (V14) | The release PRIVACY pattern plus a manual scan of the new files for family, pets, health, sleep, breaks and routine words | 0 automated candidates. Private details were deliberately excluded from the cards, the dossiers and the audio report (neutral stream labels; personal remarks neither quoted nor summarized). |
| Usability and fidelity (V15) | Field lengths against `framework/sudowrite-fields.json`; Japanese dialogue rule; palettes | All new fields inside the soft limits; Relationships edits on existing cards kept inside 350 words (Calli and Nerissa trimmed). Spoken lines are Japanese with romaji and an English gloss; Audio Tags declare Japanese dialogue; V20 palette check passes. |

## Dispositions (self-review findings)

- **Unverified items removed or confirmed.** "逆様" (Riona × Niko) and "クリームで会いにいけますか" (Su × Vivi) were
  confirmed from the official video listings on their profiles (undated here). The 7th fes. appearance was confirmed
  with a news photo report. The unit fan name stays secondary and off the cards.
- **Scope.** Routine details from stream titles and the official profile's household line were kept off the cards;
  scope notes use the project's generic wording.
- **Outfits.** Each member's three outfits are Claude's reading of the official gallery images; Riona's New Year
  outfit is matched to its reveal silhouette. The other members' Japanese-style outfits are not dated.

## Open items

1. Gemini Neon re-review (author decision 2026-11-27; packets A and B in `research/qa/external-review/`).
2. A 2026 chat window for Su and for Chihaya (their checked windows are from August 2025).
3. Release dates for "逆様" and "クリームで会いにいけますか"; reveal dates for the Japanese-style outfits.
````

### FILE: `research/qa/audit-gamers.md`

````markdown
# Cohort audit: gamers (Fubuki, Mio, Korone, hololive GAMERS; Claude self-check 2026-11-27; Gemini Neon review pending)

**What this file is.** The other cohort audits are GPT cross-card audits merged by Claude. This one is not: the
GAMERS cards were added on the author's order of 2026-11-27 ("追加人物, 把gamers補完"), and the Codex login that the
framework uses for GPT was blocked in this session, so Claude researched, wrote and checked them alone. The file
records the checks Claude ran and what they found, so that V11, V12, V14 and V15 have a written review to point to.
On 2026-11-27 the author decided not to use the Codex/GPT audit and to have Gemini Neon (desktop) re-review the
work instead; the packets are in `research/qa/external-review/`, and Gemini's findings will be merged here. Nekomata Okayu stays in the "jp" cohort, where her card was first audited.

Scope: `bible/characters/Shirakami-Fubuki.md`, `Ookami-Mio.md`, `Inugami-Korone.md`, `bible/world/hololive-GAMERS.md`,
their performance sheets, `research/audio-check/gamers.md`, and the GAMERS lines added to existing cards (Okayu, Ayame,
Marine, AZKi, Lui, Lamy, Koyori, Calli, Fuwawa, Mococo, Riona, Niko, Chihaya, Vivi, Botan, Suisei, La+, Noel, Iroha,
Bae; Groups on Okayu and Marine).

## Checks run

| Check | How | Result |
|---|---|---|
| Dates and status (V10-type) | Each date traced to the official profile (debut, birthday, height, unit), the official music catalog (release dates read from each entry), archived titles, or a named news report | All three active. Debuts 2018-06-01, 2018-12-07, 2019-04-13 (official). Albums: FBKINGDOM "Blessing" 2025-01-15, "Night walk" 2023-12-07, "My Sparkle" 2025-08-20 (official music pages). Fubuki's first solo live 2025-02-13 at Pia Arena MM (official announcement plus a Famitsu report; the archive titles agree). Mio's "Our Sparkle" 2025-09-10 (official news headline on her profile). Korone's originals dated from the official catalog. |
| Participants and direction (V11) | Each tie checked against full archive titles (member lists in the title brackets) on the channel that hosted it; `tools/web_check.py` for coverage | Twenty existing cards now name the GAMERS members they share collabs with. Title keyword matches that were false positives (ルイージ for Lui, ビビリ / ビビッド for Vivi, ジジイ for Gigi, ニコラ for Niko, 優しい彗星 for Suisei, ホロぐら for Gura) were discarded. Three new one-way ties were closed (Riona→Mio rephrased, Lamy↔Fubuki added, Fubuki→Ina rephrased; the English-lesson tie stays in Fubuki's map with its sources); the five remaining one-way ties are the FLOW GLOW coverage notes recorded in audit-flowglow.md. |
| Evidence records (V12) | Each [SW] claim matched to a dossier line with a source ID | Every claim has an official page, an archive ID, a row in the audio report or a named secondary source. Fubuki's stream vocabulary, cat joke, Kurokami Fubuki, Vice-Manager Unicorn and mascots come from her official Q&A (English and Japanese). Units added to `tools/qa_packets.py` carry their evidence (hololive GAMERS, AyaFubuMi, NYANGUCORN and RosaMiA from official profiles or music credits; FAMS and OKFAMS from Fubuki's official Q&A). |
| Quotations and ASR (V13) | `tools/span_check.py holoen` | 0 quotations outside a shared span. Lines heard as near-matches by both models (Mio's 「おはみぉーん」 and "otsu-mion," Fubuki's "Hi, Friends!" and "otsukon") are given in the members' own written spellings (titles, official profile) or in romaji, labelled as such. Mio's 「うちうち、うちだよ」 is labelled as written (a 2021 title) wherever it appears. A Fubuki sample line that joined 「ではでは」 to 「今日もありがとうございました」 across an intervening sign-off was split. |
| Scope screening (V14) | The release PRIVACY pattern plus a manual scan of the new files for family, pets, health, sleep, breaks, travel, home and routine words | 0 automated candidates. Removed: "at Mio's" (a home location from a title) on the world card. Not used: personal remarks from the transcribed chats, personal items in some stream titles, the official profile's snack and drink lines. Stream labels in the audio report are neutral. |
| Usability and fidelity (V15) | Field lengths against `framework/sudowrite-fields.json`; Japanese dialogue rule; palettes | All new fields inside the soft limits; Relationships on edited cards at or under 350 (Calli trimmed by three short phrases to stay at 350). Spoken lines are Japanese with romaji and an English gloss; Audio Tags declare Japanese dialogue; the V20 palette check passes. |

## Dispositions (self-review findings)

- **Outfit dates.** Dated only where a reveal title, hashtag, thumbnail or silhouette ties the gallery image to a
  date: Fubuki 2019-12-22 (thumbnail), 2024-08-09 (silhouette), the "TEK" outfit's 2024-08-05 return and the royal
  outfit's 2025 solo live (thumbnails), the Western-style outfit by 2020-10-06 (thumbnail); Mio 2022-12-06
  (silhouette) and her room wear's 2022-01-09 "2.0" (title and thumbnail art); Korone 2022-06-24 (title and ©SEGA),
  2023-07-07 and 2024-10-01 (silhouettes). The rest are undated.
- **Kurokami Fubuki** is described from the official Q&A as a separate persona; she has no card and her rough register
  is excluded from Fubuki's voice direction.
- **Groups alignment.** "holoWitches" follows the Marine card's spelling for the official artist "Magical Girl
  holoWitches!"; BABACORN was added to Marine's Groups and NYANGUCORN to Okayu's, each with an evidence note.

## Open items

1. Gemini Neon re-review (author decision 2026-11-27; packets A and B in `research/qa/external-review/`).
2. A spoken check of Fubuki's 「こんこんきーつね」 and of Korone's greeting outside her morning show (both are covered by
   music or game audio in the checked windows; the cards rely on the official profiles).
3. Reveal dates for the undated gallery outfits; what Korone's 2022 "ambassador" title refers to.
````

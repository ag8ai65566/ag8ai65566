## 本資料包包含的檔案
- project.md（sha256 d0f5c8402dcb）
- bible/characters/IRyS.md（sha256 4fb35ef5dc61）
- bible/characters/Nerissa-Ravencroft.md（sha256 aa61d24bfbcb）

## 因篇幅沒有附上的檔案（需要時在「待確認」提出）
- bible/characters/Gawr-Gura.md
- bible/characters/Mori-Calliope.md
- bible/characters/Ninomae-Inanis.md
- bible/characters/Ouro-Kronii.md
- bible/characters/Takanashi-Kiara.md
- bible/characters/Watson-Amelia.md
- bible/world/AmeSame.md
- bible/world/Bone-Bros.md
- bible/world/Concerts-and-Live-Events.md
- bible/world/Cross-Branch-Friends.md
- bible/world/IRyS-and-Nerissa-Pairs.md
- bible/world/Myth-and-Kronii-Other-Pairs.md
- bible/world/OctoClock.md
- bible/world/Streaming-Life.md
- bible/world/TakaMori.md
- bible/world/TakoTori.md
- bible/world/Time-Duo.md
- bible/world/Time-and-Death.md
- bible/world/VTuber-Persona-and-Lore.md
- bible/world/hololive--Advent.md
- bible/world/hololive--Myth.md
- bible/world/hololive--Promise.md
- bible/world/hololive-History-2023-2026.md
- bible/world/hololive-History-to-2022.md
- bible/world/hololive.md

---

# project.md（sha256 d0f5c8402dcb）

---
title: "hololive EN 角色設定集"
lang: en
web_search: live
---

# hololive EN 角色設定集

> 這份檔案是整個專案的「憲法」。Claude 和 GPT 每次工作都會先讀它。

## 基本
- 性質：以 hololive（原 hololive English）成員的**公開角色人設**為基礎的同人角色設定集，
  給 Sudowrite 寫同人小說／短文用，之後也要交給 AI 做**聲音演出**。
- 這個專案的重點：**聲音**——口頭禪、招呼語、常用詞彙、語氣詞與笑聲、語言混用、
  不同情境下的語調變化。其他段落為這個重點服務。
- 篇幅：每位成員一張 Characters 卡（CSV 匯入）＋一份完整調查檔案。
- 時間基準：2026-09-30。2026-09-07 起 hololive 把 EN／ID／DEV_IS 分部合併成單一「hololive」品牌，
  原本的組別名保留（例：hololive -Myth-、-Promise-、-Advent-、-Justice-）。卡片寫目前狀態。

## 語言
- **全部用英文**：Sudowrite 卡片和調查檔案都寫英文，連段落標題也翻成英文（`## [SW]`
  開頭的標題與 front matter 保持原樣）。成員本人說英文，口頭禪與語感照原文才準，
  Sudowrite 也以英文最穩定。日文等混用的詞照原文保留（附英文註解）。
- 「待確認」與「合併紀錄」也用英文；Claude 回報給作者時再用中文摘要。

## 範圍與界線（以真人為基礎的角色）
- 只用**官方設定（lore）**與**直播、影片、社群上公開呈現的言行**。
- 不寫、不推測背後真人的身分、本名、長相、過去的活動、私生活。
- 不做親密關係或性方面的推測（「親密關係與界線」段一律寫「（無）」）。
- 不抄歌詞、不貼長篇逐字稿；口頭禪與短句引用即可。
- 每條重要資訊附來源與查核日期；查不到的標「未證實」。自創的示範台詞要標「風格示範」。

## 最高原則：真實（作者 2026-09-30 定案）
- **這個專案最重要的是「像本人」。** 粗口、挑逗梗、低級笑話、迷因式台詞都照原樣保留，
  **不清理、不淡化、不美化**。把 "fuck" 寫成 "f***"、把 "ara ara" 拿掉，都算錯誤。
- 真實也代表準確：只寫查得到的口癖；查不到的標「未證實」，不要為了豐富而編造成「官方口癖」。
  自創的示範台詞一定標「風格示範」。
- **不分時期**：從出道到現在視為同一個連續的角色，早期梗（例：Calli 的 "What is up, humans?!"、
  叫 Kiara "kusotori"）和近期梗都當成角色的共同記憶保留在卡片裡，不要標成「早期限定」。
- **近期權重**（作者 2026-09-30 定案）：人會慢慢改變，但不會變太多。描述「現在的預設說話方式」
  （常用詞、語氣、頻率、人設重心）時，**越近期的直播證據權重越高**；早期梗仍照「不分時期」保留為
  共同記憶。早期與近期證據衝突時以近期為準，並在調查檔案註明是哪個時期、怎麼變。
  已畢業／轉為 affiliate 的成員，以最後一段活躍期為「近期」。
- **Role 一律 Protagonist**（作者定案）。
- GPT 推理強度（作者定案，省額度）：寫初稿 Extra High，審稿與驗收 High。
- **完整優先**：卡片可以寫到建議長度上限附近，把有來源的口癖、語氣、互動盡量放進去；
  但最重要的資訊放在每欄最前面（Sudowrite 上下文不夠時會先丟角色卡）。

## 世界觀與人際關係（作者 2026-10-01 定案）
- **蒐集任何資料時，都當成完善世界觀的一部分。** 成員之間的人際關係最重要也最複雜，要大量資料補足，
  而且不限 EN：JP、ID、DEV_IS、holostars、GAMERS 等其他分部成員的互動也算。
- 世界觀不只人際關係，也包括：新成員加入、畢業、團體與個人演唱會、3D 直播、Expo／fes 等活動、
  官方企劃與重大公告。這些都是角色的「共同記憶」，**不要吝嗇，盡量完善**。
- 成員在 X（Twitter）的公開發文是關鍵來源（只用公開帖文；短引文；不碰私人生活細節）。
- GPT 額度用完時，Claude 自己盡量完善，不必等。
- 目標是完成 EN 全體成員；**目前名單以外的成員要等作者下令才做**。

## 聲音（給 Sudowrite 加 ElevenLabs 標籤，作者 2026-10-01 定案）
- 作者打算讓 **Sudowrite 在寫故事時自己加上 ElevenLabs v4 的表演標籤**。
- 所以每個角色的說話方式、性格、口癖、口音、語速、音域、笑聲與招牌聲音、情境語氣轉換、
  發音，凡是影響「聲音」的因素，都要**鉅細靡遺**教給 Sudowrite，讓它生成時能完美模仿。

## 語氣與風格
- 卡片寫成 Sudowrite 能照著演的具體行為與說話方式，不要寫成粉絲百科式的年表。
- 同一個梗只寫一次，放在最適合的欄位。

## 成員清單（2026-09-30，目前在籍）
- Myth：Mori Calliope、Takanashi Kiara、Ninomae Ina'nis
- Promise（原 Council）：IRyS、Ouro Kronii、Hakos Baelz
- Advent：Shiori Novella、Koseki Bijou、Nerissa Ravencroft、FUWAMOCO（Fuwawa、Mococo）
- Justice：Elizabeth Rose Bloodflame、Gigi Murin、Cecilia Immergreen、Raora Panthera
- 已畢業：Gawr Gura、Tsukumo Sana、Ceres Fauna、Nanashi Mumei
- 停止活動、保留 affiliate：Watson Amelia（2024-09-30 起）
- 已完成（2026-10-01）：Myth 五人、Ouro Kronii、IRyS、Nerissa Ravencroft。其餘成員等作者下令。

## 已定案的硬設定
- （收錄進 bible 後，重要的硬事實抄一行在這裡）


---

# bible/characters/IRyS.md（sha256 4fb35ef5dc61）

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
  - "HiRyS, it's IRyS! Your seiso nephilim here to fill the world with hopium!" (official greeting);
    written in 2026 as "HiRyS, iiiit's IRyS from hololive English -Promise-! I am (probably) the embodiment
    of HOPE, a seiso half angel – half demon nephilim here to bring hope to the world through song!!"
    [Official R21]. Neither is ASR-confirmed; both are written sources.
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
  - Teasing chat about a new outfit: "I think most of you guys are satisfied as long as you can see this…
    up to here… You guys don't need to see the bottom half… I'm trying to make you guys feel
    guilty. That's what I'm doing here, okay?" [ASR R20, 0:09:48–0:12:26; a closing "ashamed of yourself"
    heard by the first model only is not quoted]
  - About Kronii's goddess outfit, she calls herself "a half-angel, half-demon Nephilim" who "could pull it
    off somehow" (the two models differ on "I am" / "I have" and on repetitions, so only these spans are
    quoted). She then compares her figure with Kronii's; the two models disagree on the key word, so that
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
| Excited about an outfit or concert | Fast, run-on, repeated "so cute" | "It's so cute. It's so cute." (ASR R20, both models) |
| Teasing chat | Sweet, then a sly guilt trip | "I'm trying to make you guys feel guilty." (ASR R20) |
| After a slip | Mock-innocent denial | "I am a hundred percent seiso, I would never lie!" (R2 §Quotes) |
| Horror game | Quiet, focused, short cheers | "Run Leon, run!" (ASR R20) |
| Sincere | Warm, plain | "I really hope so too." (ASR R20) |
| Sign-off | Circling goodbyes | "Thank you very much! See you guys again tomorrow!" (ASR R20) |

### Sample Lines
1. "HiRyS, it's IRyS! Your seiso nephilim here to fill the world with hopium!" (Official R1)
2. "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" (ASR R20, 0:12:07)
3. "I'm glad you guys liked the outfit. I knew you guys would!" (ASR R20, 4:27:19)
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
- R21 Official Serendipity interview with IRyS and Bae (2026-06-05): https://serendipity.hololivepro.com/news/interview02
- R22 Official music page, "DANGERyS" (on sale 2026-07-12): https://hololive.hololivepro.com/en/music/754/

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
Irys, SeisoRyS, YabaIRyS

## [SW] Personality
IRyS streams as a nephilim, half angel and half demon, who delivers hope through song, and the joke of her persona is the duality: she is sweet, positive and a little shy, then lets the "yabai" demon half out with a suggestive or violent remark, and insists she is one hundred percent seiso. She teases chat by turning their thirst back on them until they should feel guilty. When something excites her, like a new outfit or a concert, she gushes fast and at length and keeps saying how cute it is; when she's done, she moves on with a cheerful "okay." She enjoys violence in games and happily plays the cruel one. She loves soda and announces what she's drinking, puns on her own name ("HiRyS," "ByeRyS") and talks to her fans as "you guys." She is ambitious about singing: her first full album came out in 2026, her first solo concert is next, and she wants to collab with everyone in hololive. She dislikes celery, heights, bugs, math, ceiling fans and helicopters, and claims Santa never visited her because she's half demon.

## [SW] Background
She has no supernatural abilities; her lore is a performed persona. IRyS is a VTuber and singer whose lore, a persona she plays for laughs, makes her a nephilim who was once the embodiment of hope in "The Paradise" and reawakened in an age of despair to deliver hope through her songs; she doesn't speak of what came before. She debuted on 2021-07-11 as hololive English's VSinger, the sole member of -Project: HOPE-, and joined -Promise- with Fauna, Kronii, Mumei and Bae in 2023; since the 2026 merger she is in hololive -Promise-. Her fans are IRyStocrats and her members Nephamily. She has released several EPs, held 3D lives such as "The Devil Wears Hope" (2024), "HOPE UPON A STAR" (2025) and "Racing Towards Hope" (2026, in a race-queen outfit), released her first full-length album, "DANGERyS," on 2026-07-12; her first solo concert, "HOPE ||: Beyond the Stars," is scheduled in Tokyo for 2026-10-06.

## [SW] Physical Description
IRyS's avatar is 162 cm tall (166 cm in heels), with light brown skin, floor-length magenta hair, long pointed ears and two small black horns. Her eyes are heterochromatic, cyan on the right and purple on the left, and a halo of white crystal stars floats above her head. She has a small pair of iridescent wings at her shoulders and larger magenta ones at her lower back.

## [SW] Dialogue Style
Fast, bubbly, run-on English when she's excited, full of "like," "you know," "I do think so," restarts and repeated phrases ("It's so cute. It's so cute."). She calls her audience "you guys," puns on her own name, and slips a Japanese interjection into English. Strong profanity is uncommon in the sampled recent streams ("damn it," "holy shoot!"); her usual comic edge is innuendo, delivered sweetly and then walked back: she insists she is "a hundred percent seiso," or tells chat to erase what she just said from memory. She reads superchats in counted batches and wanders into long, detailed explanations of how a show or outfit was made. Lines of hers: "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" "I'm glad you guys liked the outfit. I knew you guys would!"

## [SW] Catchphrases
"HiRyS, iiiit's IRyS!" (greeting, as she writes it in 2026); "Your seiso nephilim here to fill the world with hopium!" (her official greeting's second half); "ByeRyS!" (sign-off pun); "a hundred percent seiso" (her claim after a suggestive slip); "Yoisho~" (effort); "No, I don't like it. I love it!" (gushing); "Thank you very much! See you guys again tomorrow!" (sign-off); "Run Leon, run!" (horror games)

## [SW] Voice & Delivery
A soft, bright speaking voice in the middle range that turns quick and bubbly when she's excited, and a fuller, more powerful singing voice. The suggestive lines come out sweet and innocent, with a sly little drop at the end. She giggles lightly and does lip rolls on stream. In horror games she gets quiet and focused, with short cheers. Sincere lines are warm and plain. Her goodbyes circle several times before she actually leaves.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, bright mid-range voice (about 214–226 Hz), sweet and friendly, speeding into quick bubbly run-ons when excited (about 168–183 words a minute in chat), quiet and focused in horror games; American English. Default tags: [sweet, bright]. By situation: opening [bright, cheerful]; gushing about an outfit or concert [rapid, gushing, delighted]; teasing chat [sweet] then [sly, lower]; after a slip [mock-innocent, quick] "I am a hundred percent seiso!"; yabai aside [innocent] then [slight smirk]; horror game [focused, quiet] then [short cheer]; surprised [gasps]; sincere [warm, plain]; sign-off [warm, cheerful], repeated as the goodbyes circle. With people (direction drawn from Relationships): Bae [mock-married bickering]; CHADCast with Calli and Bae [chaotic, giggly]; Kronii [competitive, teasing]; Flare [cheerful, polite Japanese]; Nerissa and other kouhai [warm senpai]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [light giggle] (usually, rather than a cackle); [small effort sound] "Yoisho~". Keep in the words: "like" (about one word in thirty in chat), "you know," "I do think so," "I mean," "right?"; restarts and repeats when excited ("It's so cute. It's so cute."); "you guys," almost never "chat"; strong profanity is uncommon in the sampled streams ("holy shoot!", "damn it"). Pronunciation guide (provisional, untested): IRyS /ˈaɪɹɪs/, nephilim /ˈnɛfɪlɪm/, hopium /ˈhoʊpiəm/, seiso /ˈseɪsoʊ/, yabai /jɑˈbaɪ/, IRyStocrats /aɪˈɹɪstəkɹæts/. Not as default: a cold or menacing demon voice, or constant swearing. Never a sexualized read of the innuendo; keep it cheeky.

## [SW] Motivation
IRyS wants to deliver hope through her songs and reach bigger stages: after her first full album, "DANGERyS" (2026), comes her first solo concert in Tokyo, and someday an anime song. She wants to collab with every member of hololive and keep her fans' spirits up.

## [SW] Relationships
Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her frequent horror co-op partner in 2025–2026. Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna and Nanashi Mumei (graduated): Promise unitmates from the early years.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-09-30): official profile (R1), wiki (R2, by section),
  archive metadata (R3), Claude's two-model audio check (R20).
- **From GPT one-round review (runs/20260930-2309-world-hololive/gpt-free.md, 2026-10-01, high), adopted:**
  - career state updated: "DANGERyS" released 2026-07-12 (official page R22, checked by Claude
    2026-10-01); the solo concert is scheduled for 2026-10-06; the "full album" goal removed from
    Motivation and Personality;
  - "HOPE" removed from Other Names;
  - ASR quotation gate tightened: the nephilim sentence is quoted only in the spans both models share;
    "you know" removed from the outfit-tease quote (second model lacks it); the doubled "I knew you guys
    would!" removed (one model only). "No, I don't like it. I love it!" stays: the second model's full
    text contains it ("No, I don't like it. I love it."), the report's excerpt was truncated (fixed);
  - wiki-only spoken lines kept in the dossier (secondary) and paraphrased on the card ("a hundred percent
    seiso," erasing a slip from memory); "We can play Monopoly... IN BED!" removed from the card;
  - "mild words only" replaced by "strong profanity is uncommon in the sampled recent streams";
  - Relationships expanded: Bae's 2026 Serendipity partnership from the official interview (R21), Flare,
    Ina and Nerissa.
- **SHOULD adopted:** exact catchphrases kept in Catchphrases; quotes reduced elsewhere. The 2026 written
  greeting "HiRyS, iiiit's IRyS" added from the official interview.
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).

## Open Questions
1. The wiki calls her speaking voice "high-pitched"; in this project's 2026 sample it measures mid-range.
   The card says "soft, bright, middle range." Keep, or follow the wiki?
2. Her "yabai" innuendo is on the card as sourced lines; the "Monopoly" bit is from the wiki (secondary,
   no timestamp). Keep on the card?


---

# bible/characters/Nerissa-Ravencroft.md（sha256 aa61d24bfbcb）

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
  - Written self-introduction (2026): "Hiya Darlings, this is hololive English -Advent-'s Devilish Diva, the
    one and only Nerissa Ravencroft!" [Official N21]. Hosting a 2026 group Q&A on stream she opens with a
    similar stacked introduction ("…the one and only … Nerissa Ravencroft"; partly transcribed).
    [ASR N20, Co_SBrM-oK0 0:05:26, partly agreed]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "You know what I'm saying?" → tagging the end of a point → about 5 times in 30 minutes of solo chat
    (first-model count). [ASR N20]
  - "I don't make the rules." → after stating a silly opinion as fact; also on X in her first week:
    "I'm the demon of soup now, sorry I don't make the rules" (2023-07-26). [ASR N20, second model agrees]
    [Observed—X post, research/x-posts.md]
  - "…take it back immediately" → retracting her own rage-bait (the models differ on "I" / "I'd"). [ASR N20]
  - "Come on, Jailbirds, be nice!" → when chat teases her. [ASR N20, agrees]
  - "Pissing all by yourself, handsome?" → a crude, flirty line the wiki quotes. [Observed N2 §Quotes,
    secondary]
  - "Demon of Soup," "Mofufu," "#OLRissa" office-lady bits → recurring nicknames she plays along with.
    [Observed N2; N3 titles]
- **Flirting and crude asides (non-explicit; kept under the authenticity rule):** said deadpan and then
  corrected in the same breath: "Makes me want to take all my clothes off, but that's inappropriate, so
  I won't do that." [ASR N20, mw9XEGHxD6A 0:10:04, agrees]
- **Self-aware about being a VTuber:** reading chat's "You're so weird," she agrees ("Yeah, I am") and
  says that is why she is a VTuber; otherwise she'd "be working in [an] office or something." (The two
  models differ in small words, so only the shared spans are quoted.) [ASR N20, 0:17:05]
- **Rage-bait and retreat:** "I would even argue that Bavarian filled cream donuts aren't donuts. That's
  me just rage baiting at this point. I'm sorry. They are donuts. … The point I was trying to make was
  not correct." Then she takes it back ("I take it back" in one model, "I'd take it back" in the other).
  [ASR N20, 0:18:26–0:18:34]
- **Vocabulary / fillers:** "like" (about 1 in 35 words in solo chat), "okay," "you know what I'm
  saying?", "mind you," "oh my god / oh my gosh," "man," "honestly"; calls a friend "girl"; addresses
  "you guys" and "Jailbirds." [ASR N20, first-model counts]
- **Profanity:** casual and unforced, and she knows it: in 30 minutes of solo chat "That shit's divine"
  (about eggs), a "good-ass," a "fucker," and then "I need to stop swearing so much, so I'm trying to
  work on it." [ASR N20, 0:11:39, 0:35:19, agrees]
- **Storytelling:** long, run-on anecdotes with escalating mock-drama ("he's trying to kill me"), then
  "anyway" back to the point; she does voices, such as a caveman voice ("…go hunt, … get food, … run from big predator";
  "cavemen" in one model, "caveman" in the other). [ASR N20, 0:39:46]
- **Code-switching:** an otaku who studies Japanese (not fluent); Japanese words and honorifics in
  English ("Kiara-senpai," "kohai"). [Observed N2 §Miscellaneous; N3 titles]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (N20; a 2026 solo chat): median pitch about 214 Hz (p10–p90 172–297 Hz), a mid-range
    speaking voice like IRyS's (214–226 Hz), lower than Kiara or Gura; about 159 words per minute of
    speech. Group-stream windows read higher (284–289 Hz) because several voices share them. Sample results only.
  - Her public chatting delivery is relaxed and mid-range, not a high, cute voice. Her singing voice is the persona's
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
| Opening / hosting | Bright, theatrical self-introduction | "Hiya Darlings" … "the one and only Nerissa Ravencroft!" (Official N21, written) |
| Chatting | Relaxed, run-on, mock-dramatic | "You know what I'm saying?" (ASR N20) |
| Flirting or crude aside | Sweet, then deadpan, then a quick correction | "…but that's inappropriate, so I won't do that." (ASR N20) |
| Rage-bait | Confident, then a quick retreat | "I'm sorry. They are donuts." (ASR N20) |
| Teased by chat | Mock-whiny | "Come on, Jailbirds, be nice!" (ASR N20) |
| Fangirling (Kiara, Marine) | Fast, flustered, delighted | (no verified line; see Relationship Map) |
| Telling a story | Big swings, character voices | (a caveman voice; see Voice Profile) |

### Sample Lines
1. "Hiya Darlings, this is hololive English -Advent-'s Devilish Diva, the one and only Nerissa Ravencroft!" (Official N21, written)
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
| 2024-08-08 | First EP "In My Feelings" | [Official N22] |
| 2025-01 | "Office lady" outfit (#OLRissa) | [Observed N3 titles] |
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
| Elizabeth Rose Bloodflame | Justice member ("BloodRaven"); her 2026 Serendipity duo partner | Her "mortal enemy (lore)"; their "Rondo Revolution" cover; World Tour '24 panels together; Nerissa praises her "kindness and encouraging attitude" ("She's always looking out for me, even though I'm the senpai"); building Liz's Mii: "she's the leader of justice after all" | [Official N21; S7 tour report via world card; ASR N20] |
| Moona Hoshinova | ID senior ("V3LVET" with Raora) | Featured on Moona's "100% (feat. Nerissa Ravencroft)" (2025-02-16); Keep Talking and Nobody Explodes together (2024) | [Official N23; N3 title] |
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
- N21 Official Serendipity interview with Nerissa and Elizabeth (2026-06-12): https://serendipity.hololivepro.com/news/interview07/
- N22 Official music page, "In My Feelings" (on sale 2024-08-08): https://hololive.hololivepro.com/en/music/455/
- N23 Official music page, "100% (feat. Nerissa Ravencroft)" (2025-02-16): https://hololive.hololivepro.com/music/533/

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
Nerissa streams as the "Demon of Sound," a singer whose voice was too powerful for the gods, and plays it as a running bit: off the stage she is a sweet, friendly, very online otaku who flirts shamelessly with her Jailbirds and her friends. She often says the crude or flirty thing deadpan, sometimes correcting herself in the same breath. She will state a silly opinion as fact to rage-bait chat, then take it back once chat bites. She tells long, dramatic stories with voices and mock outrage, cheerfully owns being weird (it is, she says, why she is a VTuber), and swears casually while promising to swear less. She is an open fangirl of Takanashi Kiara and Houshou Marine, adopts any nickname fans hand her (the Demon of Soup, Mofufu, the office lady), and loves musicals, cooking for friends and singing for others.

## [SW] Background
She has no supernatural abilities; her lore is a performed persona. Nerissa is a VTuber whose lore, a persona she plays for laughs, makes her the Demon of Sound: a singer whose love-filled voice could drive the world mad, sealed by the gods in The Cell with one horn broken, until she escaped with the rest of Advent, master key on her keychain. She debuted on 2023-07-31 with hololive English -Advent- (since the 2026 merger, hololive -Advent-). She had her 3D debut on 2024-08-09 (with a literal pot of soup), released her first EP "In My Feelings" (2024-08-08), held the 3D concert "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests, sang the duet "OVER//RIDE" with Calli (2025), and released "OYOME♡HOLIC" and "Blue World" (2026). She reached one million subscribers on 2026-06-12, and in 2026 she was cast as the space pirate Risa in the anime "Tenchi Galaxy." Her fans are Jailbirds.

## [SW] Physical Description
Nerissa's avatar is 175 cm tall, the tallest in hololive (197 cm counting heels and horns): long straight black hair with a blue inner layer and silver and gold ornaments, light purple eyes with a beauty mark under the left eye, and two horns layered black over blue, shaped like musical notes near the base and decorated with black flowers; one horn is broken. She wears a striped off-shoulder white shirt with a black bow and ruffled collar, feather-edged black sleeves and gloves, a layered sleeveless coat with three crossed belts, and asymmetrical high boots. Her staff is a giant flower-decorated tuning fork that can become a microphone, and her raven mascot Shadow can perch on her right shoulder.

## [SW] Dialogue Style
Casual, chatty American English that runs on: long anecdotes with mock-dramatic escalation ("he's trying to kill me"), then "anyway" back to the point. Fillers: "like," "okay," "mind you," "oh my god," "man," and a tag question, "You know what I'm saying?" She calls chat "you guys" or "Jailbirds" and a friend "girl," drops Japanese honorifics ("Kiara-senpai," "kohai"), and does silly voices mid-story (a caveman voice). Crude and flirty lines often come out deadpan, sometimes walked back right away; a rage-bait opinion can get retracted once chat bites. In the sampled chat she swears as casual emphasis ("That shit's divine") and knows it: "I need to stop swearing so much." Lines of hers: "That's me just rage baiting at this point. I'm sorry. They are donuts." "The point I was trying to make was not correct."

## [SW] Catchphrases
"Hiya Darlings" (greeting, as she writes it in 2026); "Devilish Diva, the one and only Nerissa Ravencroft!" (self-introduction); "Nerissa Ravencroft, at your service~" (debut introduction); "Ope?!" (her first post on X); "You know what I'm saying?" (ending a point); "I don't make the rules." (after a silly claim, on stream and on X); "…take it back immediately" (retracting rage-bait); "Come on, Jailbirds, be nice!" (when chat teases her); "Makes me want to take all my clothes off, but that's inappropriate, so I won't do that." (deadpan aside); "the Demon of Soup" and "Mofufu" (nicknames she answers to)

## [SW] Voice & Delivery
Her public chatting delivery is relaxed and mid-range, warm rather than a high anime voice, with a trained, powerful singing voice that is the heart of her persona. She speaks at an easy, fairly quick pace and swings big when telling a story: mock outrage, character voices, dramatic pauses. Flirting comes out sweet and coaxing; crude jokes often come out flat and deadpan, sometimes followed by a quick, brighter correction. When chat teases her she turns mock-whiny. In the sampled chat, swears often function as casual emphasis.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): warm, relaxed mid-range chatting delivery (about 214 Hz), relaxed and chatty at an easy, fairly quick pace (about 159 words a minute), playful and teasing, theatrical when telling a story; American English; not a high anime voice. Default tags: [relaxed, chatty]. By situation: opening or hosting [bright, theatrical]; chatting [relaxed, chatty]; crude or flirty aside [sweet] then [flat, deadpan], then often [quick, brighter] for a correction; rage-bait [confident, smug] then [sheepish, rushed]; teased by chat [mock-whiny]; self-aware [amused, matter-of-fact]; story voices [exaggerated caveman voice] and the like; flirting with a friend [sweet, coaxing, low]; fangirling over Kiara or Marine [excited, flustered, fast]. With people (direction drawn from Relationships): Shiori [sweet, lovestruck]; Kiara and Marine [flustered fangirl, fast]; FUWAMOCO [matching their bright energy]; Bijou [playful]; Calli [hyped duet partner]; a Japanese senpai [polite Japanese, nervous]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [startled] "Ope!"; [dramatic gasp], [exaggerated groan] in stories. Keep in the words: "like," "okay," "mind you," "oh my god," "man," the tag question "You know what I'm saying?"; run-on anecdotes that escalate, then "anyway"; the crude line, often followed by a quick correction; casual swears, then "I need to stop swearing so much"; "you guys," "Jailbirds," "girl"; Japanese honorifics ("Kiara-senpai"). Pronunciation guide (provisional, untested): Nerissa /nəˈɹɪsə/, Ravencroft /ˈɹeɪvənkɹɒft/, Mofufu /moʊˈfuːfuː/, Ope /oʊp/, senpai /ˈsɛnpaɪ/. Not as default: a high cutesy voice, a prim idol who never swears, or a cold demon menace outside a bit. Never flirting read as breathy or explicit.

## [SW] Motivation
Nerissa wants to sing for audiences, develop her music and acting, collaborate across hololive and improve her Japanese. Her lore echoes this ambition through the Demon of Sound's desire to sing.

## [SW] Relationships
Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit (ShioRaven); Shiori plays hard to get, and the two keep a joke lore of fictional "children." Fuwawa and Mococo Abyssgard (FUWAMOCO): she claims, as a bit, to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, they took a 2024 off-collab trip and held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower. IRyS: fellow singer who guested at that concert. Elizabeth Rose Bloodflame: her "mortal enemy (lore)" from Justice and her 2026 Serendipity duet partner; they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai"). Moona Hoshinova: she sings on Moona's "100%" (2025). Houshou Marine: her other oshi. Gigi Murin: duo partner with a joke "child," Nerigi.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-09-30): official profile (N1), wiki (N2, by section),
  archive metadata (N3), Claude's two-model audio check (N20), X posts (research/x-posts.md).
- **From GPT one-round review (runs/20260930-2309-world-hololive/gpt-free.md, 2026-10-01, high), adopted:**
  - "In My Feelings" dated 2024-08-08 (official page N22, checked by Claude 2026-10-01; the wiki's date was
    wrong) and the timeline reordered;
  - exact quotations limited to spans both models share: the VTuber answer paraphrased with short shared
    spans; "I take it back" (one model) vs "I'd take it back" (the other) quoted only as "…take it back
    immediately"; the caveman voice described, not quoted; chat's "You're so weird" marked as chat text;
  - the wiki-only crude pickup line kept in the dossier (secondary) and removed from Catchphrases;
  - "her speaking voice is her natural one" replaced by "her public chatting delivery is relaxed and
    mid-range"; "never as anger" replaced by "swears often function as casual emphasis"; the "always
    corrects" rule softened to "often/sometimes";
  - Motivation rewritten without literal gods or imprisonment (GPT's wording);
  - the Elizabeth Mii quote replaced on the card with their Serendipity partnership, from the official
    interview (N21); "wife," "children" and "Mofufu" kept as public bits; the Tomodachi comparison removed
    from the card.
- **SHOULD adopted:** "Hiya Darlings" and "Devilish Diva" from the official interview (N21) replace the
  unclear group-stream introduction on the card. Moona's "100%" (N23) added.
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).

## Open Questions
1. Her laughter, "Ope!" and her fangirling with Kiara were not captured by the audio check (whisper does
   not write laughs, and no Kiara collab fell in the windows). Keep the provisional Tone Shifts rows, or
   check a KiaRissa stream next?
2. Her stacked hosting self-introduction ("…the one and only … Nerissa Ravencroft") is only partly
   transcribed; the epithet is not on the card.

## 本資料包包含的檔案
- project.md（sha256 8945d4e511c5）
- bible/characters/Ceres-Fauna.md（sha256 dd1e7e596402）
- bible/world/AmeSame.md（sha256 03602b5cf2fd）
- bible/world/Bone-Bros.md（sha256 3456a63d5263）
- bible/world/Myth-and-Kronii-Other-Pairs.md（sha256 12e7d39a7dbb）

## 因篇幅沒有附上的檔案（需要時在「待確認」提出）
- bible/characters/Gawr-Gura.md
- bible/characters/IRyS.md
- bible/characters/Mori-Calliope.md
- bible/characters/Nanashi-Mumei.md
- bible/characters/Nerissa-Ravencroft.md
- bible/characters/Ninomae-Inanis.md
- bible/characters/Ouro-Kronii.md
- bible/characters/Takanashi-Kiara.md
- bible/characters/Watson-Amelia.md
- bible/world/Concerts-and-Live-Events.md
- bible/world/Cross-Branch-Friends.md
- bible/world/Fauna-and-Mumei-Pairs.md
- bible/world/IRyS-and-Nerissa-Pairs.md
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

# project.md（sha256 8945d4e511c5）

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
- 已完成（2026-10-01）：Myth 五人、Ouro Kronii、IRyS、Nerissa Ravencroft、Ceres Fauna、Nanashi Mumei。
  其餘成員等作者下令。
- 作者下令（2026-10-01）：做 **Advent 整團**（Shiori Novella、Koseki Bijou、FUWAMOCO 的 Fuwawa Abyssgard 與
  Mococo Abyssgard；Nerissa 已完成），並**補完所有人物的關係網和世界觀**。額度用完時務必設定時間自動繼續。
  FUWAMOCO 是雙胞胎、同一頻道：聲音不同，所以做兩張角色卡，另做一張 FUWAMOCO 世界觀卡。

## 已定案的硬設定
- （收錄進 bible 後，重要的硬事實抄一行在這裡）


---

# bible/characters/Ceres-Fauna.md（sha256 dd1e7e596402）

---
kind: character
name: "Ceres Fauna"
sw_section: Characters
---

# Character File: Ceres Fauna

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Fauna graduated from hololive
> on 2025-01-03; her "present" in this file is her last active period (2024), per the project's recency
> rule. Nothing about the performer behind the avatar: the reason for her graduation and private-life
> details (health, family, school and the like) are deliberately left out. In stories she knows she is a
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
  - "Evil Fauna" → an alter-ego bit; the wiki's quote describes her using "the sultry deep voice" ("No!
    Don't fall! You guys would fall too easily to Evil Fauna."). On the card this is directed as a
    deliberately lower, theatrical, mock-villainous voice, kept comic. [Observed F2 §Quotes, secondary]
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
- **Laughs, noises:** "uuuu" when flustered [F2, secondary]; a fake "ha ha ha" after her puns (the words
  are transcribed; the flat delivery is Claude's reading, provisional) [ASR F20].
- **Code-switching:** English with brief Japanese thanks during superchats ("arigato"; one model hears
  "Arigatou gozaimasu");
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
  - Provisional (interpretation, not measured): a soft, light head voice; usually unhurried; quiet and
    comforting for ASMR; sweet-but-ominous for threats; a deliberately lower, theatrical "Evil Fauna" as a
    comic bit. Stronger reactions remain possible.
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
| Evil Fauna | Deliberately lower, theatrical, mock-villainous; kept comic | "You guys would fall too easily to Evil Fauna." (F2) |
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
| 2024-08-24/25 | hololive English 2nd concert -Breaking Dimensions-: premieres "It's Not a Phase" with Mumei and sings "Mayonaka no Door" solo (day 1); "Lonely in Gorgeous" with Shiori and Nerissa (day 2) | [Official F5] |
| 2024-12-14 | -Promise- musical "The Broken Promise" | [Observed F2 §2024] |
| 2024-12-22 | "It's Not a Phase" (Mumei & Fauna) released | [Official F6] |
| 2024-12-27 | 1,000,000 subscribers; Kiara's HOLOTALK guest the same day | [Observed F2; F3 title] |
| 2024-12-31 | The World Tree is complete | [Observed F3 title] |
| 2025-01-03 | Graduates; last post on X: "LOVE & PEACE / Love, Fauna" | [Observed F2, secondary] |

## Relationship Map
Public exchanges only; counts are streams on Fauna's channel mentioning the other per year (2021 → 2024,
archive F3), a rough measure.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Nanashi Mumei | Council/Promise genmate (6 / 14 / 3 / 4) | Recurring collaborator from debut week (Don't Starve Together, 2021-08-25); their comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); their original duet "It's Not a Phase" premiered at -Breaking Dimensions- (2024-08-24) and was released 2024-12-22; one of her last streams: "Mumei and Fauna investigate infighting on Wikipedia Talk Pages" (2024-12-20) | [Observed F2 §Personality, secondary; F3] [Official F5, F6] |
| Hakos Baelz | Genmate (6 / 12 / 7 / 2) | At debut Bae called her "a natural mama, a soothing beauty, and someone who gives the best headpats"; a month of horror games (2022); an Amnesia: The Bunker off-collab (2023) | [Observed F2; F3, F4] |
| Ouro Kronii | Genmate (6 / 8 / 6 / 2) | Fauna described Kronii's "gap moe"; "Defusing bombs with Kronii but we can only speak in ASMR" (2021); Bread & Fred (2023) | [Observed Kronii file K8; F3] |
| IRyS | Promise unitmate from 2023 (CouncilRyS before that) | "IRyS VS FAUNA SWITCH SPORTS BATTLE OF THE CENTURY" (2022); Pokémon Unite tournament practice (2023) | [Observed F3] |
| Tsukumo Sana | Council genmate (graduated 2022) | Sana designed the Council's "Beeg Smol" models; Fauna: "Go give [Sana] lots of love because she deserves it, even though she's a little bit... disgusting." | [Observed F2 §Quotes, secondary] |
| Gawr Gura | Her hololive oshi | Mario Kart ("GOOWA FWANA RACING"), a Dark Souls race (2024), and "Drawing Hololive Members From Memory with @GawrGura!" (2024-12-30) | [Observed F2 §Likes; F3] |
| Takanashi Kiara | Myth senior | "KIWAWA vs FAWNA" (Clubhouse 51, 2022); Minecraft Wither fight; Kiara's HOLOTALK 32nd guest (2024-12-27) | [Observed F3; Kiara archive] |
| Kaela Kovalskia | ID friend | "Fearless & Fearful vs Ghosts" (Phasmophobia, 2022); Minecraft ID server tour | [Observed F3] |
| -Justice- | Kouhai | "FAUNA'S DUNGEON: Forcing holoJustice to play a board game I made up" (2024); Silent Hill 2 with Gigi Murin (2024) | [Observed F3] |
| Shirogane Noel | JP senior | A member she admires and wanted to collab with | [Observed F2 §Trivia, secondary] |
| Nerissa Ravencroft | Advent kouhai | Fauna, Shiori and Nerissa sang "Lonely in Gorgeous" at -Breaking Dimensions- (2024-08-25); a 2023 reply from Nerissa on X: "Fauna-senpai!!! My Raven companion is named Shadow~" | [Official F5] [Observed—X post via wiki citation, research/x-posts.md] |

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
- F5 Official concert report, hololive English 2nd Concert -Breaking Dimensions-: https://hololive.hololivepro.com/en/events/breaking-dimensions/
- F6 Official music page, "It's Not a Phase" (2024-12-22): https://hololive.hololivepro.com/en/music/517/
- F20 Claude's audio check (2026-10-01); see research/audio-check/fauna.md.

---

## [SW] Name
Ceres Fauna

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive alum, hololive English -Promise- (graduated), hololive English -Council- (former unit)

## [SW] Other Names
Fauna, Faufau, Fawna, Keeper of Nature, Mother Nature, Gamer Kirin, Ceres-chan

## [SW] Personality
Fauna streams as the Keeper of Nature, a druidic kirin four and a half billion years old, and plays the lore for laughs: she is the softest, most comforting presence in the room, and she uses that same soft voice to suggest you "return to nature," threaten to turn you into a tree, or let "Evil Fauna" out in a deliberately lower, theatrical voice. She dotes on her Saplings, and her comedy with Mumei includes exaggerated protective, possessive bits; she gets embarrassed easily ("uuuu"). She commits to huge, patient projects (a Minecraft World Tree built over more than a hundred hours) and long playthroughs, loves horror games, cursed memes, animals and cats, and spins absurd improvised dramas out of games (a love monologue for a forklift, "pangolin crimes" in a zoo). She runs late and jokes that she is "always on time" on "Fauna Standard Time." Sincere moments are plain and warm: she thanks every Sapling she can by name.

## [SW] Background
Fauna is a hololive alum: she graduated on 2025-01-03. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore, a persona she plays for laughs, makes her the Keeper of "Nature," the second concept created by the gods: a druid with kirin blood whose horns are tree branches, who came online to win humans over and lead them back to nature. She debuted on 2021-08-23 with hololive English -Council-, joined -Promise- with IRyS, Kronii, Mumei and Bae in 2023, won VTuber Awards for ASMR and for chatting streams, sang at both hololive English concerts (2023, and 2024, where she and Mumei premiered their duet "It's Not a Phase") and in Promise's musical "The Broken Promise" (2024), reached one million subscribers on 2024-12-27, and finished her Minecraft World Tree on 2024-12-31, days before graduating. Her fans are Saplings, her members Faunatics, and her mascot is Nemu, a sleepy kirin.

## [SW] Physical Description
Fauna's avatar is 164 cm tall, with wavy light-green hair that fades to blue-green at the tips and is decorated with small white five-petal flowers, and horns like leafy tree branches (kirin horns, not deer antlers). Her eyes are yellow, with a beauty mark under the right one. She wears a short blue dress with golden ornaments under a white overcoat lined with pink flowers and closed with a blue bow, a golden belt set with green roses and water-drop gems, one long white sock and a golden bangle on the other ankle, and she goes barefoot. A golden apple sometimes floats at her hand; her sleepy kirin mascot Nemu may be curled up nearby.

## [SW] Dialogue Style
Soft, meandering English that circles with "like," "I guess," "kind of" and "actually," and often trails off on a gentle "I don't know." She talks to her Saplings warmly and, now and then, as their slightly spooky goddess: sweet reassurances with an ominous "...right?" at the end, invitations to "return to nature," spells cast on chat, a shop she insists is "not a scam." She commits fully to absurd bits and improvised drama, from love speeches to a forklift to grand deadpan ("I will be the sole arbitrator of YouTube monetization"), and laughs a flat, fake "ha ha ha" at her own puns. In games she reads the dialogue aloud in the characters' voices; scared, she murmurs "oh no," "oh gosh." Her own swearing stays mild ("dang," "what the heck"). She reads superchats as quick, rhythmic lists of names and thank-yous, adds brief Japanese thanks, and sings happy birthday when asked. Lines of hers: "I am not the keeper of jet packs." "I was ready to be a kirin because that's what I am. But if they need me to be a giraffe, I guess I can do that." "Me. I'll be the mean manager."

## [SW] Catchphrases
"Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (official greeting); "Konfauna!" (greeting); "return to nature" (her invitation and threat, a recurring bit); "uuuu" (embarrassed); "four and a half billion" (her age, when called old); "Evil Fauna" (her lower-voiced, mock-villainous alter-ego bit); "Fauna Standard Time" (her lateness) and "I'm always on time." (said when late); "It's not a scam! Fauna Mart is real!" (her shop bit); "If you heard your name, you will now be the recipient of my next spell." (while reading superchats); "I am not the keeper of jet packs." (refusing a request); "Plant them, plant them…" (a chant after a list of names); "Thank you so much for hanging out, and I will see you tomorrow." (sign-off); "LOVE & PEACE" (her last post)

## [SW] Voice & Delivery
A soft, light, mid-high speaking voice (she calls herself soft-spoken and says she talks in her head voice). Her usual delivery is soft and unhurried, meandering through stories; stronger reactions remain possible. For ASMR her voice drops to a quiet, comforting whisper. Her mischief usually comes out sweet: a threat or a "return to nature" in the same soothing tone, and for "Evil Fauna" a deliberately lower, theatrical, mock-villainous voice. When flustered she trails into "uuuu"; her sampled horror reactions are often quiet murmurs of "oh no," and she reads game dialogue aloud in the characters' voices. Superchat lists can turn brisk: a warm, rhythmic run of names and thank-yous.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (sample observations, not synthesis targets): soft, light, airy head voice, high in this project's samples (about 280–306 Hz), usually unhurried and meandering (about 105–120 words a minute in chat), brisk in superchat lists; American English. Default tags: [soft, gentle]. By situation: opening [soft, cheerful]; cozy chat [soft, meandering]; sweet threat or "return to nature" [sweetly] then [softly ominous]; Evil Fauna bit [lower register, mock-villainous], kept comic; flustered [embarrassed]; improvised drama [mock-dramatic, impassioned]; horror game [nervous, murmuring]; reading game dialogue [in a character voice]; superchat list [quick, rhythmic, warm]; grand deadpan [deadpan]; ASMR [whispering, close]; sincere [warm, plain]; sign-off [warm, cheerful]. With people (provisional, drawn from Relationships): Mumei [warm, teasing], with [sweetly possessive] only for the performed "return to nature" bit; Gura [admiring] (her oshi); Justice and other kouhai [gentle, mischievous senpai]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [flustered] uuuu; [fake laugh] ha ha ha (after her own pun). Keep in the words: "like," "I don't know" (often as a soft sentence ending), "I guess," "kind of," "actually," "oh no," "oh gosh," "oh my gosh"; mild exclamations predominate in the sampled streams ("dang," "what the heck"). Pronunciation guide (provisional, untested): Ceres /ˈsɪəɹiːz/, Fauna /ˈfɔːnə/, kirin /ˈkɪɹɪn/, Konfauna /kɑnˈfɔːnə/, Nemu /ˈnɛmu/. Not as default: loud shouting, constant swearing, a cold menacing voice. Never a sexualized read of Evil Fauna or of ASMR.

## [SW] Motivation
In her lore, Fauna wants to win humans over and lead them back to nature. As a streamer she wanted to comfort her Saplings, sing, learn Japanese, collab with her genmates in person, speedrun games and voice-act in a game, and to finish what she started, like the World Tree.

## [SW] Relationships
Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024); Silent Hill 2 with Gigi Murin. Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!"

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-01): official profile (F1, greeting re-checked
  2026-10-01), wiki (F2, by section), archive metadata (F3), X posts via wiki citations (F4), Claude's
  two-model audio check (F20, research/audio-check/fauna.md; a members-only window was set aside unused).
- **From GPT one-round review (runs/20261001-0454-world-Fauna-and-Mumei-Pairs/gpt-free.md, 2026-10-01,
  high), adopted:**
  - "sultry" removed from every performance direction: Evil Fauna is now "deliberately lower, theatrical,
    mock-villainous," tag [lower register, mock-villainous]; the wiki's word stays attributed in the dossier;
  - the Mumei dynamic made situational (GPT's wording): exaggerated protective/possessive bits, with the
    possessive tag reserved for the "return to nature" bit; "above all to Mumei" removed;
  - "arigatou gozaimasu" (second model only) replaced by "brief Japanese thanks";
  - the wiki-only Sana sentence paraphrased on the card (GPT's wording); full quote kept in the dossier;
  - absolute voice rules replaced by defaults (GPT's wording: "usual delivery… stronger reactions remain
    possible"; "mild exclamations predominate in the sampled streams");
  - interpretations separated from ASR evidence: giggles and gasp removed from Signature sounds; the flat
    fake laugh and the head-voice description marked provisional in the dossier; partner directions cut to
    those with an interaction source (Mumei bit, Gura as oshi, Justice kouhai);
  - Background opens with her alum status; Groups list Promise as graduated and Council as a former unit;
    IRyS described as a Promise unitmate (not genmate);
  - "Fawna" added to Other Names (her "KIWAWA vs FAWNA" title);
  - scope statement no longer names a specific private loss.
- **Missing facts adopted (checked by Claude 2026-10-01 on the official pages):** "It's Not a Phase,"
  Fauna and Mumei's duet premiered at -Breaking Dimensions- (day 1, 2024-08-24) and released 2024-12-22
  (F5, F6); "Lonely in Gorgeous" with Shiori and Nerissa (day 2); her solo "Mayonaka no Door" (day 1).
- **Not adopted, with reason:**
  - "I'm always on time" kept: the second model's full text contains it ("…Nine hundred and four thousand.
    I'm always on time."); the report's excerpt was truncated and its verdict now quotes the full text.
  - The provisional IPA guide stays in Audio Tags, marked "provisional, untested," as on the eight cards
    already promoted (the earlier GPT round accepted it so labeled) and because the author asked for
    pronunciation to be taught; the ElevenLabs sheet repeats it with the same label.
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).

## Open Questions
1. "Evil Fauna," the yandere lines and the forklift dramas come from the wiki's quote list (secondary, no
   timestamps). They are kept as bits, with full sentences quoted only in the dossier and in two Sample
   Lines. Keep?


---

# bible/world/AmeSame.md（sha256 03602b5cf2fd）

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
Myth's gremlin and Myth's shark: close Myth friends and frequent early collaborators, a comedy duo that
argued on purpose and pranked each other endlessly, and whose last on-stream moments together were spent
reading their old DMs. At the 2026 baseline Ame is an affiliate and Gura has graduated; their shared
streaming history supplies callbacks and memories.

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
- **Off-collab (2022):** they held an off-collab in June 2022, including an unarchived karaoke.
  [Observed S2, secondary]
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
| 2022-06 | An off-collab; unarchived karaoke | — |
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
- 2026 baseline: Ame is an affiliate and Gura has graduated; their history supplies callbacks and
  memories. Graduation establishes nothing about their private contact.
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
Watson Amelia and Gawr Gura, Myth's gremlin and Myth's shark, close Myth friends and frequent early collaborators. They hosted The Fish Tank, a talk show built on staged arguments, and pranked each other endlessly (Ame's Minecraft mine "Gura's Backdoor"; Ame killing Gura in Among Us right after Gura said "Not me, right?"). The sweet side showed too: Gura rewrote "You Are My Sunshine" about Amelia, picked "Watson" as the family name she'd take, and got flustered whenever a staged argument turned into real praise. On 2024-09-29, the day before Ame concluded her regular activities, they streamed "Looking at our old DMs" together. Gura graduated on 2025-05-01. At the 2026 baseline Ame is an affiliate and Gura has graduated; their shared history lives on in callbacks, their gold-and-blue colors, and Kiara's tribute song "Blue & Gold."

## [SW] Rules
At the 2026-09-30 baseline, Ame is an affiliate and Gura has graduated. Their shared streaming history supplies callbacks and memories; graduation does not establish anything about their subsequent private contact. Stories set before October 2024 can use them together freely. Teasing can be crude and relentless, and Gura has become flustered when Ame turns teasing into praise. The ship name is a fan term, not romance.

## [SW] Sensory Details
Gold and blue side by side (💛💙); a shark hood next to a deerstalker; two voices arguing on purpose and cracking up; Gura going flustered when a staged argument turns into praise; an old DM thread scrolled on stream.

## [SW] Secrets


---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-09-30), built from the wiki pages, archive metadata (S1)
  and the Gura and Ame character files.
- **From GPT one-round review (runs/20260930-2309-world-hololive/gpt-free.md, 2026-10-01, high), adopted:** "closest friends" ranking replaced by "close Myth friends and frequent early
  collaborators" (also in both character cards); the home detail removed (now "an off-collab in June
  2022"); the baseline rule rewritten so it does not claim anything about private contact; the
  "sincerity embarrasses them both" rule narrowed to the cited case (Gura flustered by Ame's praise).
- **SHOULD adopted:** the "stopping dead" sensory detail replaced with the sourced fluster.
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).

## Open Questions
(None.)


---

# bible/world/Bone-Bros.md（sha256 3456a63d5263）

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
The reaper and the shark (their personas), Myth's bickering "bros": a duo of pranks, jabs and a shared
song, from the year both were the branch's biggest names to Gura's last Minecraft trip with Myth. Calli
has performed Gura's unreleased song and said she would keep singing it.

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
- **"Full Color":** Gura's single was never released; Calli performed it at hololive English -Myth-'s
  fourth-anniversary concert "The Show Goes On!" (September 2024), and Calli and Kiara said they would
  keep singing it in karaoke. [Observed S2 §Miscellaneous, secondary; archived official broadcast
  CDljbqawDkw]
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
| 2024-09 | Calli performs Gura's "Full Color" at Myth's 4th-anniversary concert "The Show Goes On!" | Carrying her song |
| 2025-04-30 | "One Last Minecraft Trip." (Myth relay) | Last duo moments on stream |
| 2025-05-01 | Gura graduates | — |

## Glossary
| Word | Meaning | Who says it |
|---|---|---|
| Bone Bros | Calli and Gura | fans, members |
| Full Color | Gura's unreleased single; Calli and Kiara said they'd keep singing it | Calli, Kiara |

## Conflicts and Story Hooks
1. (Before 2025-05) Gura pranks Calli's Minecraft base; Calli plots revenge on stream.
2. (Proposed fiction, before 2025-05) Calli and Gura look back on their published duet "Q" on stream.
3. (Before 2025-05) The last Minecraft trip: neither says goodbye directly.
4. (2026) A karaoke stream where Calli sings "Full Color" and chat goes quiet.
5. (2026) Calli sings "Full Color" at a karaoke stream and tells chat why.

## Links to Characters
Mori Calliope, Gawr Gura; Takanashi Kiara (Full Color in karaoke); Myth.

## Secrets
(None.)

## Hard Facts (continuity)
- "Q" duet: 2022-02-03. Gura graduated 2025-05-01.
- 2026 baseline: Gura has graduated; Calli performed "Full Color" in 2024 and said she would keep singing it.

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
Mori Calliope and Gawr Gura, the reaper and the shark: a bickering duo of pranks and jabs, where Calli's gruff big-sister threats bounce off Gura's cheerful dumb-shark defiance. They were the English branch's first two to reach a million subscribers, were named Tokyo Tourism Ambassadors together (2023) and sang "Q" with DECO*27 (2022). Their collabs thinned out over the years, but on the Myth relay before Gura's graduation Calli's stream was "One Last Minecraft Trip." Gura graduated on 2025-05-01. Her single "Full Color" was never released; Calli performed it at Myth's fourth-anniversary concert "The Show Goes On!" (2024) and, with Kiara, said she would keep singing it.

## [SW] Rules
At the 2026 baseline Gura has graduated; Bone Bros lives in memories, the "Q" duet and "Full Color." Before May 2025 they can prank and bicker freely. Calli's affection tends to show through teasing and actions more than speeches.

## [SW] Sensory Details
Black and blue; a scythe beside a trident; Calli's "LISTEN." against Gura's "a"; a Minecraft sunset on a last trip; Calli singing Gura's song in karaoke and not saying why.

## [SW] Secrets


---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-09-30) from wiki pages, archive metadata (S1) and the
  Calli and Gura files.
- **From GPT one-round review (runs/20260930-2309-world-hololive/gpt-free.md, 2026-10-01, high), adopted:** "Full Color" event corrected to Myth's fourth-anniversary concert "The Show
  Goes On!" (September 2024, archived official broadcast); "keeps singing" replaced by the documented 2024
  performance plus the stated intention (also in the Calli and Gura cards); the "Dad" origin hook removed
  (the origin is unverified); the "Q" recording-roles hook relabeled as proposed fiction about the
  published duet.
- **SHOULD adopted:** persona qualifier on "the reaper and the shark"; "not speeches" softened to a tendency.
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).

## Open Questions
1. "The Dad joke started around Gura" could not be re-found in the current wiki; it stays unverified and
   off the card.


---

# bible/world/Myth-and-Kronii-Other-Pairs.md（sha256 12e7d39a7dbb）

---
kind: world
name: "Myth and Kronii: Other Pairs"
sw_section: Worldbuilding
---

# World Element: Myth and Kronii: Other Pairs (pairs among the five Myth members and Kronii without their own card)

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
  cover of Calli's debut EP; Calli wrote the lyrics of Ina's 2026 song "TAKO∞TAKOVER." Calli is a recurring
  target of Ina's puns ("Every freaking time, Ina."). They watched Suisei's concert together in an
  off-collab (2023-02-20) and still game together (Elden Ring Nightreign, 2025-06). [Observed S5 Ina
  §Miscellaneous; Calli file C28; Ina file I8; S1]
- **Calli and Ame** (24 / 23 / 14 / 6 / 6 / 0): early Clubhouse 51 duels; the MV of Calli-written "Myth or
  Treat" premiered on Ame's channel (2021); in 2026 Ame "called in from 2021" during Calli's charity
  stream. [Observed Ame file A20; S3 §2021, §2026, secondary; S1]
- **Ina and Ame** (29 / 30 / 9 / 4 / 4 / 0): Ina designed Bubba; Ame's "Amenade" cocktail traces back to a
  Japanese snack tasting with Ina; a "LOSER BUYS DINNER!!!!!" off-collab (2023-02-23); Ame aims blunt PvP
  taunts at her. [Observed S3 §Miscellaneous; Ame file; S1]
- **Ina and Gura** (71 / 28 / 10 / 3 / 3 / 2): fellow members of the official ocean unit UMISEA (September 2021);
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
| 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |
| 2024-09-22 | Ame on HOLOTALK | Kiara's oshi as guest |
| 2025-04-26/30 | Kronii's and Kiara's last collabs with Gura | Farewells |
| 2026-01-08 | "TAKO∞TAKOVER" digital release (lyrics by Calli) | Ina × Calli |

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
All six (the five Myth members and Kronii).

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
Myth and Kronii: Other Pairs

## [SW] Role
Relationship

## [SW] Other Names
Kiara and Ame, Ame and Kiara, Kiara and Gura, Gura and Kiara, Calli and Ina, Ina and Calli, Calli and Ame, Ame and Calli, Ina and Ame, Ame and Ina, Ina and Gura, Gura and Ina, Kiara and Kronii, Kronii and Kiara, Gura and Kronii, Kronii and Gura

## [SW] Description
The rest of the web among the five Myth members and Kronii. Kiara and Ame: Ame is Kiara's EN oshi ("#1 Ame gosling"); Ame made Kiara's HOLOTALK intro, was its guest in 2024 and now guests at Kiara's concerts; Ame on a reunion: "Kiara like, threw herself at me… she hugged me!" Kiara and Gura: Kiara calls Gura "Goobidiba" and taught her German and Japanese, swears included; Gura's Minecraft prank filled Kiara's KFP back room with chickens; Gura was HOLOTALK's 34th guest the day before she graduated. Calli and Ina: Ina designed Death Sensei and drew Calli's debut EP cover; Calli wrote the lyrics of Ina's "TAKO∞TAKOVER"; Calli is a recurring target of Ina's puns ("Every freaking time, Ina."). Calli and Ame: early Clubhouse 51 duels; in 2026 Ame "called in from 2021" to Calli's charity stream. Ina and Ame: Ina designed Bubba; they did a "loser buys dinner" off-collab. Ina and Gura: the official ocean unit UMISEA (2021); Ina promised "the wrath of Ina" to anyone who makes Gura cry. Kiara and Kronii: Kiara was a fan before Kronii debuted and calls her "quasoni." Gura and Kronii: fan unit SNOTCast; in Gura's last months Kronii was one of her regular partners ("I Play, She Watches (She's Scared)").

## [SW] Rules
In the 2026 baseline, pairs with Gura are memories and callbacks, and pairs with Ame are guest appearances. Nicknames are used as each member uses them (Kiara's "Goobidiba," "quasoni"). All of these are friendships.

## [SW] Sensory Details
A KFP back room full of chickens; a hand-drawn Death Sensei and a Bubba sketch; Kiara's German-lesson voice; Gura repeating a swear wrong; "Every freaking time, Ina."

## [SW] Secrets


---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-09-30): archive metadata (S1) with per-year counts,
  wiki pages, and the character files.
- **From GPT one-round review (runs/20260930-2309-world-hololive/gpt-free.md, 2026-10-01, high), adopted:** renamed "Myth and Kronii: Other Pairs" (Kronii is not Myth); "Goobidiba"
  attributed correctly (Kiara's name for Gura); "TAKO∞TAKOVER" dated 2026-01-08 per the official music
  page (checked by Claude 2026-10-01); UMISEA dated "September 2021" per the 2021-09-21 announcement.
- **Also:** "favorite pun target" softened to "a recurring target of Ina's puns" (GPT's character-card
  note); reversed pair names added to Other Names (SHOULD).
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).

## Open Questions
1. "quasoni" appears in Kiara's stream titles for Kronii; its origin was not found.

## 本資料包包含的檔案
- project.md（sha256 c958a950ad99）
- bible/characters/Ceres-Fauna.md（sha256 8b6bb0af69b5）
- bible/characters/Fuwawa-Abyssgard.md（sha256 65d87ad37465）

## 因篇幅沒有附上的檔案（需要時在「待確認」提出）
- bible/characters/Gawr-Gura.md
- bible/characters/IRyS.md
- bible/characters/Koseki-Bijou.md
- bible/characters/Mococo-Abyssgard.md
- bible/characters/Mori-Calliope.md
- bible/characters/Nanashi-Mumei.md
- bible/characters/Nerissa-Ravencroft.md
- bible/characters/Ninomae-Inanis.md
- bible/characters/Ouro-Kronii.md
- bible/characters/Shiori-Novella.md
- bible/characters/Takanashi-Kiara.md
- bible/characters/Watson-Amelia.md
- bible/world/Advent-Pairs.md
- bible/world/AmeSame.md
- bible/world/Bone-Bros.md
- bible/world/Concerts-and-Live-Events.md
- bible/world/Cross-Branch-Friends.md
- bible/world/FUWAMOCO.md
- bible/world/Fauna-and-Mumei-Pairs.md
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

# project.md（sha256 c958a950ad99）

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
- GPT 推理強度（作者定案 2026-10-01，取代先前的「審稿 High」）：**所有階段一律 Extra High（xhigh）**，提高審查力度與準確性。
- 發揮 GPT 的長處（作者 2026-10-01 要求；Claude 的做法）：GPT 擅長即時網路搜尋、逐條核對來源、找出缺漏與矛盾。
  所以每團開工時先給 GPT 一個**獨立查證研究**任務（`framework/prompts/gpt-research-sourced.md`：每條附開過的網址、
  分官方／一手／二手、關係只寫具體合作、稽核既有卡片裡提到這團的句子），Claude 同時做存檔、wiki、雙模型音檔與卡片；
  草稿完成後 GPT 仍只審**一輪**（xhigh、逐條核對）。研究任務要**依序跑、不要並行**（並行會一起被額度中斷）。
- **完整優先**：卡片可以寫到建議長度上限附近，把有來源的口癖、語氣、互動盡量放進去；
  但最重要的資訊放在每欄最前面（Sudowrite 上下文不夠時會先丟角色卡）。

## 世界觀與人際關係（作者 2026-10-01 定案）
- **蒐集任何資料時，都當成完善世界觀的一部分。** 成員之間的人際關係最重要也最複雜，要大量資料補足，
  而且不限 EN：JP、ID、DEV_IS、holostars、GAMERS 等其他分部成員的互動也算。
- 世界觀不只人際關係，也包括：新成員加入、畢業、團體與個人演唱會、3D 直播、Expo／fes 等活動、
  官方企劃與重大公告。這些都是角色的「共同記憶」，**不要吝嗇，盡量完善**。
- 成員在 X（Twitter）的公開發文是關鍵來源（只用公開帖文；短引文；不碰私人生活細節）。
- GPT 額度用完時，Claude 自己盡量完善，不必等。`lab.py` 會以 exit 75 結束並把重置時間與待重跑指令寫進
  `novel-lab/.gpt-quota.json`；Claude 用 send_later 排在重置時間回來跑 `lab.py gpt-resume`（依序重跑）。
  Claude 自己的額度用完時，靠每小時一次的自動續做排程回來（作者 2026-10-01：雙方額度用完都要排程，時間到就繼續）。
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
- 已完成（2026-10-01）：Myth 五人、Ouro Kronii、IRyS、Ceres Fauna、Nanashi Mumei、**Advent 全員**（Shiori Novella、
  Koseki Bijou、Nerissa Ravencroft、Fuwawa Abyssgard、Mococo Abyssgard）。其餘成員（Justice 等）等作者下令。
- 作者下令（2026-10-01）：Advent 做完後接著做 **Justice**（Elizabeth Rose Bloodflame、Gigi Murin、Cecilia Immergreen、
  Raora Panthera），同樣補完所有人的關係網與世界觀。成員宣布的休息與其原因一律不寫。
- 作者下令（2026-10-01）：做 **Advent 整團**（Shiori Novella、Koseki Bijou、FUWAMOCO 的 Fuwawa Abyssgard 與
  Mococo Abyssgard；Nerissa 已完成），並**補完所有人物的關係網和世界觀**。額度用完時務必設定時間自動繼續。
  FUWAMOCO 是雙胞胎、同一頻道：聲音不同，所以做兩張角色卡，另做一張 FUWAMOCO 世界觀卡。
  宣布的休息一律不寫（也不寫成休息中）。

## 已定案的硬設定
- （收錄進 bible 後，重要的硬事實抄一行在這裡）


---

# bible/characters/Ceres-Fauna.md（sha256 8b6bb0af69b5）

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
Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024); Silent Hill 2 with Gigi Murin. Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!" Koseki Bijou: "Coach Fauna" in Bijou's Hitman runs and a "Sweaty TryHard Gamers" squad with Bae and Kaela. FUWAMOCO: helped on the World Tree's last day (2024-12-31). Shiori Novella: the third voice of "Lonely in Gorgeous."

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
- **2026-10-01, cast expansion (author: Advent, and complete everyone's relationship web):** Relationships gained
  Advent lines from the archive metadata, the official -All for One- report and the Serendipity interviews
  (sources in the world card "Advent Pairs" and the Advent character files).

## Open Questions
1. "Evil Fauna," the yandere lines and the forklift dramas come from the wiki's quote list (secondary, no
   timestamps). They are kept as bits, with full sentences quoted only in the dossier and in two Sample
   Lines. Keep?


---

# bible/characters/Fuwawa-Abyssgard.md（sha256 65d87ad37465）

---
kind: character
name: "Fuwawa Abyssgard"
sw_section: Characters
---

# Character File: Fuwawa Abyssgard

> Scope: official lore and publicly shown persona only, checked 2026-10-01. Fuwawa is active at the
> 2026-09-30 baseline; her recent streams (2025–2026) set her default manner, per the project's recency
> rule. She shares the FUWAMOCO channel with her twin, Mococo; what the two do as a unit is on the world
> card "FUWAMOCO," and this file covers Fuwawa herself. Nothing about the performer behind the avatar:
> private-life information is outside scope and is not recorded here. "Mama Puppy" and "Papa Puppy" are
> kept out for the same reason. In stories she knows she is a streamer with a persona
> (see the world card "VTuber Persona and Lore"). Evidence labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference transcription, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed (whisper small.en; FW20) and read in context by Claude;
>   lines quoted on the card were re-transcribed by a second model (medium.en) and only shared spans are
>   quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Lines we wrote ourselves are marked **Style demo**. Source IDs (FW#) are listed under Sources.
>
> **Audio status:** on 2026-10-01 Claude checked about 1 hour of a 2026 solo stream (FW20: "FUWAWA SOLO"
> Hitman, opening, a 40-minute game window and the close), so her voice is not mixed with Mococo's; duo
> windows are in the FUWAMOCO card's report. Parts of this stream concern private matters and are not used.
> The audio was machine-transcribed and acoustically measured; transcripts were reviewed in context, without
> independent listening verification.

## One-line Concept
"The Fluffy One," the older of Advent's twin demonic guard dogs, whose duty is to calmly look after her
little sister Mococo and their pet Pero, a calm that never lasts: a soft, sweet, airheaded big sister who
says odd things, can't do math, teases a little too hard and sometimes shows a "yandere" streak, and whose
real job is to "protect your smile." [Official FW1] [Observed FW2, secondary]

## Core Drive
- **Want:** with Mococo, to protect the Ruffians' smiles; their debut list held more than a hundred goals
  (sing with Houshou Marine, a solo concert, an anime song, a scale figure). [Official FW1, FW4]
  [Observed FW2 §Hopes and dreams, secondary]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** Not established.
- **Values shown in public:** "Compassion, confidence, and loving yourself for who you are. Those are my
  wisdoms." "No support is small." [Observed FW2 §Quotes, secondary]

## Core Contradiction
The "reliable older sister" by role who is, in the wiki's words, "something of an airhead": the one
assigned to keep things calm is the one who wanders off-topic, mixes up left and right, and turns sweet
teasing into the twins' "evil twin" bit. [Official FW1] [Observed FW2 §Personality, §Miscellaneous,
secondary]

## Behavioral Traits
1. She says odd, silly things with total confidence ("Refridgator!"; math "stops" at zero). [Observed FW2
   §Quotes, secondary]
2. She is poor at spelling and math, careless, and often clumsy at games, and bad at telling left from
   right (like Gura). [Observed FW2 §Personality, §Miscellaneous, secondary]
3. She teases Mococo, sometimes too much, and plays an "evil twin" role in their public comedy.
   [Observed FW2 §Personality, secondary]
4. She also hosts solo streams (Phasmophobia, 2023; Hitman, 2024 and 2026) and streamed her own point of
   view of a 2026 group event. [Observed FW3 titles]
5. She posts alone on the shared X account with a blue heart 🩵. [Observed FW2 §Miscellaneous, secondary]
6. Her oshi is Houshou Marine; she loves visual novels, retro games, Japanese sweets and matcha.
   [Observed FW2 §Likes and dislikes, secondary]

## Voice Profile
- **Greetings / sign-offs:**
  - Solo introduction: "I'm not a chihuahua, I'm Fuwawa! And together with my sister Moco-chan, we're
    FUWAMOCO! Bau bau bau bau!" (the wiki's caption is its first half). [Observed FW2 §Quotes, secondary]
  - The duo opening is on the FUWAMOCO card. Solo close: "It was a lot of fun!" and thanks to the Ruffians.
    [ASR FW20, L93K3U4Hrjg 5:55:28; both models]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - "Bau bau!" → everything (fans counted about 162,000 of hers in her first year). [Observed FW2 §Lore,
    secondary]
  - "Oh my gosh!", "You know..." [Observed FW2 §Quotes, secondary]
  - Confident nonsense: "Refridgator!"; "Zero is where the math stops." [Observed FW2 §Quotes, secondary]
  - Polite sneaking in a stealth game: "Hello, ma'am. Nice day, ma'am." "Should I run? Is running
    suspicious?" "I'm blending in right now, right?" [ASR FW20, 0:12:13, 0:13:41, 1:12:32]
  - Begging a food stall: "That looks yummy. Can I have one? I like one. Can I have one?" "Please give me
    your snacks… not even asking for a full loaf." [ASR FW20, 1:11:16, 1:11:41; shared spans]
  - Small game asides: "Is his clothes better than mine? No." "…in a different castle." [ASR FW20, 1:05:17,
    1:08:26]
  - A cheer-up speech of her own: "So go do that, go to the gym and be the main character of the gym." She
    then says Moco-chan is "just better suited for" Pup Talks and leaves them to her (the two models disagree
    on how she described her own voice, so that phrase is not quoted). [ASR FW20, 5:48:33, 5:52:55]
- **Vocabulary / fillers:** "okay" (42 in about an hour), tag questions with "right?" (34), "maybe" (21),
  strings of "no, no, no, no," "yeah," "you know," "hmm," "in you go." Addresses "Ruffians." [ASR FW20,
  first-model counts]
- **Profanity:** none heard; she dislikes dirty jokes. [ASR FW20] [Observed FW2 §Likes and dislikes, secondary]
- **Speech trait:** rhotacism: she sometimes says an R like a W ("Wuffians"). [Observed FW2 §Miscellaneous,
  secondary]
- **Laughs, noises:** sneezes now and then (less often than Mococo); playful sound effects ("bop bop!" in the
  first model only).
  [Observed FW2 §Lore, secondary] [ASR FW20, first model]
- **Code-switching:** English and Japanese (Japanese stream titles, bilingual posts); "Moco-chan" even in
  English. [Observed FW2 §Miscellaneous, §Name, secondary; FW3]
- **Rhythm & rhetoric:** unhurried, chatty narration of what she is doing, full of questions to herself and
  chat ("…right?"); in a quiet stealth game about 76–94 words per minute of speech. [ASR FW20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (FW20; three 2026 solo windows): window medians about 330–406 Hz (p10–p90 about 254–479 Hz in
    the opening). Measurements describe the sampled recording and ASR segmentation (game audio is mixed in);
    they are not isolated vocal measurements. Not a ranking.
  - Provisional (interpretation): a very high, soft, sweet, fluffy voice; gentle and a little airy; it bounces
    up when she is excited and turns mock-stern for her "evil twin" teasing.
- **Sounds off:** a low or husky voice; crisp, rapid efficiency; swearing or crude jokes; a genuinely cold
  "evil twin" (it is teasing).

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Introduction | Bright, sing-song | "I'm not a chihuahua, I'm Fuwawa!" (FW2) |
| Sneaking around | Soft, polite, a little guilty | "Hello, ma'am. Nice day, ma'am." (ASR FW20) |
| Wanting food | Pleading, cute | "Can I have one? I like one. Can I have one?" (ASR FW20) |
| Confident nonsense | Proud, certain | "Refridgator!" (FW2) |
| Teasing Mococo | Sweet, mock-evil | (FW2 §Personality) |
| Cheering someone on | Warm, building | "…go to the gym and be the main character of the gym." (ASR FW20) |
| Sign-off | Warm | "It was a lot of fun!" (ASR FW20) |

### Sample Lines
1. "I'm not a chihuahua, I'm Fuwawa! And together with my sister Moco-chan, we're FUWAMOCO!" (FW2 §Quotes, secondary)
2. "Hello, ma'am. Nice day, ma'am." (ASR FW20, L93K3U4Hrjg 0:12:13)
3. "Should I run? Is running suspicious?" (ASR FW20, 0:13:41)
4. "That looks yummy. Can I have one? I like one. Can I have one?" (ASR FW20, 1:11:16)
5. "So go do that, go to the gym and be the main character of the gym." (ASR FW20, 5:48:33)
6. "Compassion, confidence, and loving yourself for who you are. Those are my wisdoms." (FW2 §Quotes, secondary wiki transcription)
7. "How about we get you all nice and fluffy~?" (Official FW1)

## Appearance Anchors (avatar)
- 155 cm. Long blonde hair with small side pigtails and light-blue streaks; bright pink eyes; dog ears and a
  collar; a pastel-blue headband and hairclips, one shaped like a white bandage with a blue center that
  mirrors Mococo's pink one. [Official FW1] [Observed FW2 §Appearance, secondary]
- Blue distinguishes Fuwawa's avatar styling from Mococo's pink; in the lore they are identical twins with
  four ears each (the human ones are vestigial). [Observed FW2 §Lore, §Miscellaneous, secondary]
- Fans: Ruffians (Fuwawa's own: "Fluffians"); the twins' fictional dog mascot is Pero, small and muscular
  ("The Great Perroccino"). Later outfits include a blue checkered top with bat-wing straps (2025) and blue
  pajamas (2026). [Observed FW2, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| Lore | Twin demonic guard dog from the Northwest Passage in the demon world; sealed in The Cell "for being a pain in the godly behind" | [Official FW1] [Observed FW2 §Lore] |
| 2023-07-31 JST | Debuts with Mococo as FUWAMOCO in hololive English -Advent- | [Official FW1] |
| 2023-12 | VTuber Awards: "League of Their Own" (as FUWAMOCO) | [Observed FW2 §Awards] |
| 2024-07-31 | First original song "Born to be 'BAU'DOL☆★" | [Observed FW2 §2024] |
| 2024-08-10 PDT | 3D debut with a wrestling segment and cameos by Okayu and Korone | [Observed FW2 §2024] |
| 2024-10-12 | FUWAMOCO reach 1,000,000 subscribers, first in Advent | [Observed FW2 §2024] |
| 2024-12 | VTuber Awards: "VTuber of the Year" (as FUWAMOCO) | [Observed FW2 §Awards] |
| 2025-02-02 | First birthday 3D concert, with Advent and JP guests | [Observed FW3 ouQF2A1l_cI] |
| 2025-08-23/24 | -All for One-: "HOT DUCK!", "Howling," "Lifetime Showtime," "SHALLYS" | [Official FW5] |
| 2026-04 | "Mekurumeku Rendezvous," a TV anime ending theme | [Observed FW3 vSwxof0K8lk] |
| 2026-07-03/04 | Serendipity concert, trio with Raora Panthera | [Official FW4] |
| 2026-08-29 | First album "FUWAMOCO à la mode" announced | [Observed FW2 §2026; X via wiki] |

## Relationship Map
Public exchanges only. Shared FUWAMOCO relationships are on the world card "FUWAMOCO"; these are the ones
that belong to Fuwawa or define her.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Mococo Abyssgard | Younger twin | Calls her "Moco-chan" even in English; Mococo calls her "Fuwawa," and once "Fuwa-nee" (Fuwawa loved it, Mococo refused to repeat it); "FUWAMOCO sync" | [Observed FW2 §Name, §Miscellaneous, secondary] |
| Houshou Marine | Her oshi | A Touhou off-collab (2024-04-30); Marine's solo concert watchalong (2024-12-07); a guest at their birthday concert (2025) | [Observed FW2; FW3] |
| Nerissa Ravencroft | Genmate ("Sound Hounds") | Fuwawa calls her "Newissa"; Nerissa claims to be the third sister, "Mofufu" | [Observed Nerissa wiki, secondary; Advent card] |
| Gigi Murin, Mori Calliope | Kouhai and senior | "2 Creatures + 1 Reaper," a rare bomb-defusing collab (2026-09) | [Observed FUWAMOCO X post via wiki, FW6] |

## Arc
- **Starting point:** active at the 2026 baseline, as half of FUWAMOCO: a TV anime song, Serendipity, their
  first album.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a confident wrong answer; a tease that goes one step too far; "Refridgator"-style
  wordplay; mixing up left and right during a co-op puzzle.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. Fuwawa runs FUWAMOCO MORNING alone for one segment and the math corner collapses.
  2. A co-op puzzle where every "left" is a right.
  3. Fuwawa's "evil twin" teasing backfires and Mococo gets revenge.
  4. Marine-senpai notices her and Fuwawa can only say "bau."

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2023-07-31 (JST) as FUWAMOCO; birthday February 1 (Mococo's is February 2); 155 cm; color blue;
  fans Ruffians; fictional mascot Pero.
- Unit: FUWAMOCO; hololive English -Advent- (2023–), "hololive -Advent-" since the 2026-09 merger.

## Sources (checked 2026-10-01)
- FW1 Official profile: https://hololive.hololivepro.com/en/talents/fuwawa-abyssgard/
- FW2 Virtual YouTuber Wiki, Fuwawa Abyssgard, read through its API on 2026-10-01 (secondary). Sections
  used: infobox, §Profile, §Personality, §Appearance, §2023–§2026, §Awards, §Mascots and fans, §Quotes,
  §Relationships, §Name, §Lore, §Likes and dislikes, §Hopes and dreams, §Miscellaneous:
  https://virtualyoutuber.fandom.com/wiki/Fuwawa_Abyssgard
- FW3 Stream archive metadata (titles, dates, descriptions), FUWAMOCO channel, via archive.ragtag.moe (read
  2026-10-01): VmLWdSgVlC8, ckrp6_LOr5A, L93K3U4Hrjg, YY5EJ_TX-iM, x7gRHgQ0yI0, zQdsLXE4ZQ8, ouQF2A1l_cI,
  vSwxof0K8lk. Counts computed by Claude.
- FW4 Official Serendipity interview, FUWAMOCO & Raora (2026): https://serendipity.hololivepro.com/news/interview03/
- FW5 Official concert report, -All for One-: https://hololive.hololivepro.com/en/events/all-for-one/
- FW6 FUWAMOCO's X posts via wiki citations (research/x-posts.md)
- FW20 Claude's audio check (2026-10-01); see research/audio-check/fuwamoco.md.

---

## [SW] Name
Fuwawa Abyssgard

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent

## [SW] Other Names
Fuwawa, Fuwa-chan, Fuwa-nee, The Fluffy One, Fluffy One

## [SW] Personality
Fuwawa streams as "The Fluffy One," the older twin demonic guard dog whose duty is to calmly look after her little sister Mococo and their mascot Pero, a calm that never lasts. She is a sweet, gentle, bouncy airhead who says odd things with total confidence ("Refridgator!", math "stops" at zero), is poor at spelling and math, mixes up left and right, and is clumsy at games, all of which she wears happily because she is "exceptionally cute." She teases Mococo, sometimes too much, and plays an "evil twin" role in their public comedy; she also hosts solo streams, such as Hitman. The official profile calls her bouncy, boisterous and chatty. She loves visual novels, retro games, cute girls, Japanese sweets and her oshi Houshou Marine, sings and dances seriously, and her pep talks emphasize compassion, confidence and self-acceptance. Her mission, with Mococo, is to protect the Ruffians' smiles.

## [SW] Background
Fuwawa is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Fluffy One," the older of two twin demonic guard dogs from the Northwest Passage in the demon world, sealed in The Cell "for being a pain in the godly behind," whose duty is to look after her little sister Mococo and Pero, their dog mascot. She debuted with Mococo as FUWAMOCO on 2023-07-31 in hololive English -Advent-, sharing one channel. Together they won "VTuber of the Year" at the 2024 VTuber Awards, reached one million subscribers first in Advent, made their 3D debut in August 2024, held a birthday concert in 2025, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album. Her color is blue.

## [SW] Physical Description
Fuwawa's avatar is 155 cm tall, with long blonde hair streaked light blue and gathered in small side pigtails, bright pink eyes, fluffy dog ears and a collar. She wears a pastel-blue headband and hairclips, one shaped like a white bandage with a blue center that mirrors her twin's pink one. Blue is always her color, so people can tell her from Mococo, who is otherwise her identical twin. Pero, "The Great Perroccino," their small, muscular fictional dog mascot, appears in their bits.

## [SW] Dialogue Style
Soft, sweet, chatty English that narrates what she is doing and asks everyone to agree ("…right?"), with plenty of "okay," "maybe," "you know" and strings of "no, no, no." She says odd things with total confidence ("Refridgator!"), punctuates everything with "bau bau," calls her sister "Moco-chan" even in English, and talks to her "Ruffians" (sometimes "Wuffians": she can turn an R into a W). She is politely sneaky ("Hello, ma'am. Nice day, ma'am."), pleads cutely for food ("Can I have one? I like one."), teases a little too hard as the "evil twin," and gives warm pep talks ("be the main character of the gym") while leaving the official Pup Talks to Mococo. She does not swear and dislikes dirty jokes. With Mococo she finishes sentences in sync. Her pep talks emphasize compassion, confidence and self-acceptance. Lines of hers: "Should I run? Is running suspicious?" "I'm blending in right now, right?"

## [SW] Catchphrases
"Bau bau!" (everything); "I'm not a chihuahua, I'm Fuwawa!" (introduction); "Hello hello bau bau!" (the twins' opening); "Moco-chan" (her sister, always); "Ruffians" (her fans); "Oh my gosh!"; "Refridgator!" (her own word); "Zero is where the math stops." (on math); "How about we get you all nice and fluffy~?" (official line); "No support is small."; "protect your smile" (the twins' mission)

## [SW] Voice & Delivery
A very high, soft, sweet and fluffy voice, gentle and a little airy, that bounces up when she is excited and goes mock-stern for her "evil twin" teasing. She narrates at an unhurried pace, asks "…right?" as she goes, strings "no, no, no" when things go wrong, and sometimes softens an R into a W. With Mococo the two voices overlap and land on the same word at once.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): very high, soft, sweet voice, unhurried and chatty, bouncy and boisterous when excited; American English with Japanese words. Default tags: [soft, sweet]. By situation: introduction [bright, sing-song]; chatting [gentle, chatty]; sneaking [whispering, polite]; wanting something [pleading, cute]; confident nonsense [proud, certain]; teasing Mococo [sweetly mischievous]; panicking [rapid, flustered] for "no, no, no"; cheering someone on [warm, encouraging]; sign-off [warm, cheerful]. With people (provisional, drawn from Relationships): Mococo [doting, teasing]; Nerissa [playful] ("Newissa"); Marine [starstruck]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [cheerful] bau bau!; [sneezes] (tag only). Keep in the words: "okay," "…right?", "maybe," "you know," "oh my gosh," "Moco-chan," "Ruffians"; no swearing. Pronunciation guide (provisional, untested): Fuwawa /fuˈwɑwɑ/, Abyssgard /ˈæbɪsɡɑɹd/ ("AB-iss-gard"), bau /baʊ/, Ruffians /ˈɹʌfiənz/, sometimes "Wuffians." Not as default: a low or husky voice, brisk efficiency, swearing. A genuinely cold "evil twin" only as an obvious bit.

## [SW] Motivation
In her lore, Fuwawa's job as a guard dog is to protect your smile and to look after Mococo and Pero. As an idol she and Mococo chase a list of more than a hundred dreams: a solo concert, singing with her oshi Houshou Marine, anime songs, figures, and making every Ruffian smile.

## [SW] Relationships
Mococo Abyssgard: her younger twin, whom she calls "Moco-chan" even in English; Mococo says Fuwawa is dependable and calms her down; they finish each other's sentences ("FUWAMOCO sync") and sometimes argue; Fuwawa loved being called "Fuwa-nee" once. Pero, "The Great Perroccino": their fictional dog mascot and self-proclaimed mentor; they call him "nasty" in their public bits. Advent: Shiori (Pen Pups; they mistook a cow for her), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Fuwawa calls her "Newissa," and Nerissa claims to be the third sister, "Mofufu"). Mori Calliope: "FUWAMOCALLI," a collaboration name the twins say they particularly like. Watson Amelia: "Detective Dogs." Ouro Kronii: "WatchDog." Nanashi Mumei (graduated 2025): "Fuwamoomco" (Overwatch). Raora Panthera: their 2026 Serendipity trio partner, who drew them a shikishi before her debut. Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026). Houshou Marine: her oshi (a Touhou off-collab). Shirakami Fubuki and Hakui Koyori ("FUWAMOKOYO"): horror and Lethal Company partners.

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-01): official profile (FW1), wiki (FW2, by section),
  archive metadata (FW3), official Serendipity interview (FW4), -All for One- report (FW5), X posts via wiki
  (FW6), Claude's two-model audio check of her 2026 solo stream (FW20, research/audio-check/fuwamoco.md).
- **From GPT one-round review (runs/20261001-0549-world-Advent-Pairs/gpt-free.md, 2026-10-01, high), adopted:**
  - private information removed from the dossier too: the scope note no longer names a private matter; the
    childhood-clothing note replaced by "blue distinguishes Fuwawa's avatar styling from Mococo's pink";
  - possessiveness reframed as public comedy and the confidence comparison removed (GPT's wording);
  - the full "Compassion, confidence…" sentence labeled as a secondary wiki transcription in the dossier and
    paraphrased on the card; "bop bop!" removed from Audio Tags (first model only);
  - the Gura entry removed (a shared difficulty is not a relationship), here and in Gura's card;
  - Pero framed as a fictional mascot throughout; "FUWAMOCALLI" as a name the twins "particularly like";
  - her lively side restored from the official profile ("bouncy and boisterous"); measurements kept in the
    dossier with the recording caveat, removed from Audio Tags; the "highest" claim removed.
- **Missing facts adopted:** her official line "How about we get you all nice and fluffy~?" (FW1).
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).
- **Follow-up (2026-10-01):** 3D debut labeled PDT; the last "pet Pero" in Background changed to mascot.

## Open Questions
1. (Resolved 2026-10-01, from the GPT review: the solo measurements stay in the dossier with the recording
   caveat and out of Audio Tags; parts of that stream about private matters are not used.)
2. The wiki's rhotacism ("Wuffians") was not detectable by transcription. Keep it on the card?

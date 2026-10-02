## 本資料包包含的檔案
- project.md（sha256 2eb9e51f1afc）
- bible/world/hololive.md（sha256 e80cfcc0d0d0）
- bible/characters/AZKi.md（sha256 bc7717aedd73）
- bible/world/AmeSame.md（sha256 03602b5cf2fd）

## 因篇幅沒有附上的檔案（需要時在「待確認」提出）
- bible/characters/Cecilia-Immergreen.md
- bible/characters/Ceres-Fauna.md
- bible/characters/Elizabeth-Rose-Bloodflame.md
- bible/characters/Fuwawa-Abyssgard.md
- bible/characters/Gawr-Gura.md
- bible/characters/Gigi-Murin.md
- bible/characters/Hakos-Baelz.md
- bible/characters/Hoshimachi-Suisei.md
- bible/characters/Houshou-Marine.md
- bible/characters/IRyS.md
- bible/characters/Koseki-Bijou.md
- bible/characters/Mococo-Abyssgard.md
- bible/characters/Mori-Calliope.md
- bible/characters/Nakiri-Ayame.md
- bible/characters/Nanashi-Mumei.md
- bible/characters/Nekomata-Okayu.md
- bible/characters/Nerissa-Ravencroft.md
- bible/characters/Ninomae-Inanis.md
- bible/characters/Ouro-Kronii.md
- bible/characters/Raora-Panthera.md
- bible/characters/Shiori-Novella.md
- bible/characters/Shirogane-Noel.md
- bible/characters/Takanashi-Kiara.md
- bible/characters/Watson-Amelia.md
- bible/characters/Yukihana-Lamy.md
- bible/world/Advent-Pairs.md
- bible/world/Bone-Bros.md
- bible/world/Concerts-and-Live-Events.md
- bible/world/Cross-Branch-Friends.md
- bible/world/FUWAMOCO.md
- bible/world/Fauna-and-Mumei-Pairs.md
- bible/world/Hakos-Baelz-Pairs.md
- bible/world/IRyS-and-Nerissa-Pairs.md
- bible/world/JP-Senpai-Pairs.md
- bible/world/Justice-Pairs.md
- bible/world/Myth-and-Kronii-Other-Pairs.md
- bible/world/OctoClock.md
- bible/world/Streaming-Life.md
- bible/world/TakaMori.md
- bible/world/TakoTori.md
- bible/world/Time-Duo.md
- bible/world/Time-and-Death.md
- bible/world/VTuber-Persona-and-Lore.md
- bible/world/hololive--Advent.md
- bible/world/hololive--Justice.md
- bible/world/hololive--Myth.md
- bible/world/hololive--Promise.md
- bible/world/hololive-History-2023-2026.md
- bible/world/hololive-History-to-2022.md

---

# project.md（sha256 2eb9e51f1afc）

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
- **GPT 重任務與討論（作者 2026-10-01 下午）**：作者重置了 GPT 額度，另有一張重置券（10/4 到期），10/4 前盡量用滿，但要合理有效率。
  做法：把專案全貌交給 GPT（`runs/20261001-1557-check-Project-Consult`），請它設計後續流程、提出交付給作者的最佳形式（Sudowrite／ElevenLabs）、
  列出跨卡與結構問題，並和 Claude 討論（第 1 輪 GPT 提案 → Claude 回覆 → 第 2 輪 GPT 定案）；之後依序跑議定的重任務
  （全卷交叉一致性審計、舊卡近期補完、世界年表完整性）。卡片審查仍是**每張一輪**；這些是全卷層級的新任務，不重審同一張卡的同一批主張。
  額度用完時照舊排程（`.gpt-quota.json`＋send_later），時間到自動跑。
- 標籤語法那一句（「tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound」）是給 Sudowrite 的**寫法約定**，
  不是對 ElevenLabs 輸出的保證；所有卡片一致使用，實際效果仍要用選定的聲音測試（GPT 2026-10-01 審查提醒）。
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
- hololive JP（作者指定，2026-10-02）：Hoshimachi Suisei、AZKi（0th gen）、Nakiri Ayame（2nd gen）、Nekomata Okayu（GAMERS）
  ——四人已收錄（2026-10-02，GPT 一輪 A／B 後作者裁決）。第二批（Marine、Noel、Lamy、Botan、Vivi、holoX 五人）卡片與表演表
  已完成，GPT 一輪 C–F 排隊中，審查後收錄。
- 已完成（2026-10-01）：Myth 五人、Ouro Kronii、IRyS、Ceres Fauna、Nanashi Mumei、**Advent 全員**（Shiori Novella、
  Koseki Bijou、Nerissa Ravencroft、Fuwawa Abyssgard、Mococo Abyssgard）、**Justice 全員**（Elizabeth Rose Bloodflame、Gigi Murin、
  Cecilia Immergreen、Raora Panthera；2026-10-01）。
- 作者下令（2026-10-02，第三則）：JP 四人做好後，接著做 **Houshou Marine、Shirogane Noel、Yukihana Lamy、Shishiro Botan**
  與 **holoX 全員**（La+ Darknesss、Takane Lui、Hakui Koyori、Sakamata Chloe、Kazama Iroha），做法同上（完整卡＋表演表＋
  關係網，重點是和 EN 成員與已收錄成員的關係），另做 holoX 團體世界觀卡；「別閒下來」——不要停工等待。
- 作者下令（2026-10-02，第四則）：第二批**追加 Kikirara Vivi**（hololive DEV_IS FLOW GLOW），做法相同。
- 作者下令（2026-10-02，第二則）：加入 hololive JP 的 **Hoshimachi Suisei、AZKi、Nakiri Ayame、Nekomata Okayu**，
  做法同 Bae：完整角色卡＋ElevenLabs 表演表＋關係網（重點是和 EN 成員的關係），另做一張 **JP Senpai Pairs** 世界觀卡。
  她們主要用日語直播：卡片仍用英文寫，日語口頭禪附羅馬拼音與英譯；音檔核對改用多語模型（small／medium）。
  不寫母語、國籍、休息與其原因（Ayame 的直播頻率也不寫）。
- 作者下令（2026-10-02）：加入 **Hakos Baelz**（Promise），同樣補完所有人的關係網與世界觀；**不做 Tsukumo Sana**
  （她只以已畢業的過去成員出現在別人的卡片裡）。
- 作者下令（2026-10-01）：Advent 做完後接著做 **Justice**（Elizabeth Rose Bloodflame、Gigi Murin、Cecilia Immergreen、
  Raora Panthera），同樣補完所有人的關係網與世界觀。成員宣布的休息與其原因一律不寫。
- 作者下令（2026-10-01）：做 **Advent 整團**（Shiori Novella、Koseki Bijou、FUWAMOCO 的 Fuwawa Abyssgard 與
  Mococo Abyssgard；Nerissa 已完成），並**補完所有人物的關係網和世界觀**。額度用完時務必設定時間自動繼續。
  FUWAMOCO 是雙胞胎、同一頻道：聲音不同，所以做兩張角色卡，另做一張 FUWAMOCO 世界觀卡。
  宣布的休息一律不寫（也不寫成休息中）。

## 已定案的硬設定
- （收錄進 bible 後，重要的硬事實抄一行在這裡）
- Justice 3D showcase：Elizabeth 2025-08-01、Gigi 08-02、Cecilia 08-08、Raora 08-09（皆 17:00 PDT），團體 3D 聯動 08-16 PDT（官方排程）。
- Serendipity（2026-07-03/04 PDT）官方 unit：Last Writes（Calli＋Shiori）、Octo'clock（Ina＋Kronii）、Rocku Wawa（Kiara＋Bijou）、BaeRyS（IRyS＋Bae）、
  Bloodraven（Nerissa＋Elizabeth）、B.F.F（FUWAMOCO＋Raora）、Autofister（Gigi＋Cecilia）。
- LYRA＝Kanata、Niko、Calli、Risu、Elizabeth 五人的 "III" remix 翻唱（不是 Calli 的 remix）。團曲拼法依官方音樂頁："SUPERNOVA SUPER GIRL"。


---

# bible/world/hololive.md（sha256 e80cfcc0d0d0）

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
- **Structure (as of 2026-09-30):** hololive production is COVER's brand, which also includes the male
  group HOLOSTARS; hololive is its female VTuber group. On 2026-09-07 COVER unified the former
  female-talent branches (hololive, hololive English, hololive Indonesia, hololive DEV_IS) under a single
  "hololive," an organizational and branding change it described as removing regional limits; members had
  already collaborated across branches for years; former groups keep their names as units (hololive -Myth-, -Promise-, -Advent-, -Justice-).
  Promotion is now done for all members in Japanese, Indonesian and English. [Official S6] [Observed S2
  §2026, secondary, citing the hololive Next broadcast of 2026-09-07; project.md]
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
- **Seniority:** senpai and kouhai describe relative seniority (who debuted first), not language or
  nationality; forms of address and levels of formality vary by relationship. Many EN members are openly
  starstruck by particular senpai (Calli by Suisei, Kiara by Pekora). [Observed character files]
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
- One detail only here: a member starstruck in front of her favorite senpai.

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
| 2026-09-07 | The female-talent branches unify under "hololive" | Groups become units |

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
1. After the 2026 merger, a member plans a collab with a senpai she has always admired.
2. A concert week: rehearsals, nerves, and a genmate who shows up to cheer.
3. An anniversary stream where the remaining members talk about the ones who left.
4. A kouhai asks a Myth senpai for advice and gets a joke first, then a real answer.
5. A schedule collision turns two members' streams into an impromptu collab.

## Links to Characters
All eighteen project cast members. Calli, Kiara and Ina are active in hololive -Myth-; Ame is an affiliate; Gura is an alumna;
Kronii and IRyS are active in hololive -Promise-, where Fauna and Mumei are alumnae; Nerissa, Shiori, Bijou, Fuwawa and Mococo in hololive -Advent-; Elizabeth, Gigi, Cecilia and Raora in hololive -Justice-. Detailed history: the
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
- S6 Official announcement (2026-09-07), "Renewal 2: One 'hololive' Beyond Regional and Group Boundaries":
  https://hololive.hololivepro.com/en/news/20260907-01-234/

---

## [SW] Name
hololive

## [SW] Role
Faction

## [SW] Other Names
hololive production, COVER, holoEN, hololive English

## [SW] Description
The VTuber agency run by COVER Corporation that the cast belongs to. Its members are streamers who perform characters through avatars: they stream games, chat and karaoke, release songs, hold 3D lives and concerts, collab and off-collab with each other, and appear at events. Since 2026-09-07 the former female-talent branches are one "hololive" (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-. Watson Amelia concluded her regular activities on 2024-09-30 and remains an affiliate who appears at events; Gawr Gura graduated on 2025-05-01 and is an alumna, as are Promise's Ceres Fauna (2025-01-03) and Nanashi Mumei (2025-04-27). Senpai and kouhai mean only who debuted earlier or later; formality varies by relationship; genmates are the people you debuted with. The calendar runs on debut anniversaries, birthdays, concerts and fes.

## [SW] Rules
Management and staff stay faceless helpers: no invented staff names, business secrets, scandals or disputes. Graduations are never explained beyond "graduated." Concerts are shown as avatar performances and the members' talk about them, not physical rehearsals. A story set before a date uses the statuses of that date (Gura active before May 2025; Ame streaming regularly before October 2024; branch names before September 2026).

## [SW] Sensory Details
A "Starting soon" screen; a superchat chime; a concert LED wall behind a 3D avatar; glowsticks in member colors; a crowd in Los Angeles singing along; a member starstruck in front of her favorite senpai.

## [SW] Secrets


---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-09-30) from official pages, the wiki and COVER
  notices; IRyS and Nerissa added 2026-10-01.
- **From GPT one-round review (runs/20260930-2309-world-hololive/gpt-free.md, 2026-10-01, high), adopted:** the seniority rule replaced with GPT's wording (seniority, not language or
  nationality; formality varies); "all former branches" corrected to "the former female-talent branches,"
  with hololive production also including HOLOSTARS; the merger described as an organizational/branding
  change (cross-branch collabs existed for years); "the company" and "management" removed from Other
  Names; the date open question removed (the author fixed 2026-09-30).
- **Promotion:** author decision; GPT reviewed one round only (author's instruction).
- **2026-10-01, cast expansion (author: add Fauna and Mumei):** links and lines updated for the ten characters.
- **2026-10-01, cast expansion (author: Advent, and complete the world):** Advent members and events added
  (official -All for One- report, Serendipity interviews, archive metadata; see "Advent Pairs" and "FUWAMOCO").
- **2026-10-01, cast expansion (author: Justice, and complete the world):** Justice members and events added
  (official -All for One- report, Serendipity interviews 03/06/07, official profiles, archive metadata; see
  "hololive -Justice-" and "Justice Pairs").
- **2026-10-01, from GPT one-round review of the Justice cast edits (runs/20261001-1032-world-hololive--Justice/
  gpt-free.md, xhigh), with facts checked by Claude against the official Serendipity report and 3D schedule:** "All eighteen" → "All eighteen project cast members" (an internal cast count, not hololive's size).
- **2026-10-01, P1 fix from the GPT project consult (runs/20261001-1557-check-Project-Consult/gpt-free.md):** the
  2026-09-07 restructuring now cites COVER's official announcement (S6, read by Claude 2026-10-01: "we will
  transcend regional and group boundaries and bring everything together as one 'hololive'"); the wiki stays
  as secondary detail.
- **2026-10-02, scope wording (Claude):** the senpai/kouhai definition no longer names language or nationality, even in the negative (scope screening V14).

## Open Questions
(None. The baseline date 2026-09-30 is fixed by the author.)


---

# bible/characters/AZKi.md（sha256 bc7717aedd73）

---
kind: character
name: "AZKi"
sw_section: Characters
---

# Character File: AZKi

> Scope: official lore and publicly shown persona only, checked 2026-10-02. AZKi is an active hololive member
> (Japan, 0th generation) at the 2026-09-30 baseline; added to the cast by author order (2026-10-02) for her
> ties with the English cast. Her recent streams (2026) set her default manner, per the project's recency rule.
> Nothing about the performer behind the avatar: private-life information (family, home, childhood, trips,
> health and the like) is outside scope and is not recorded here, including what the wiki lists or what she
> mentions in chats. She streams in Japanese; that is recorded as the language of her performance only. In
> stories she knows she is a streamer with a persona (see the world card "VTuber Persona and Lore"). Evidence
> labels:
> - **[Official]** COVER's own profile, site, announcement or publication.
> - **[Observed]** public stream, title or post; "(secondary)" means the wording comes from a wiki or
>   reference source, not an audio check made here.
> - **[ASR]** archived audio, machine-transcribed in Japanese (whisper small, multilingual; AZ20) and read in
>   context by Claude; lines quoted on the card were re-transcribed by a second model (whisper medium) and only
>   spans both models share are quoted. Not a listening check.
> - **[Adaptation]** an author decision for this project. **[Unverified]** reported, not confirmed.
>
> Quotes are given in Japanese with a romanization and an English gloss; the gloss is ours. Lines we wrote
> ourselves are marked **Style demo**. Source IDs (AZ#) are listed under Sources.
>
> **Audio status:** on 2026-10-02 Claude checked archived 2026 recordings (AZ20: her April Fools "debut"
> stream, a Chrono Trigger first playthrough, a one-minute GeoGuessr stream and a Paranormasight horror-mystery
> stream; see research/audio-check/azki.md). Personal remarks (family, childhood, trips) are not quoted or
> summarized here. The audio was machine-transcribed and acoustically measured; transcripts were reviewed in
> context, without independent listening verification.

## One-line Concept
"Virtual Diva AZKi": a songstress "reborn into the virtual world to fabricate a new world," a singer and
songwriter who in practice is a playful, pun-loving GeoGuessr ace calling out "Gēsu!" ("Guess!"), a dancer of
everyone's songs in her shorts, and, in fan summaries, a senpai who comforts fellow members. [Official AZ1] [Observed
AZ2 §Personality, §Trivia, secondary] [ASR AZ20]

## Core Drive
- **Want:** to keep "creating memorable music" (her official dream) that "will touch my Pioneers' hearts";
  she headlined "Departure" at Pia Arena MM (2025) and held "AZKi 8th Birthday Live 'Cross Over'" on 2026-07-01
  ("eighth" counts her birthday events; her debut anniversary is in November). [Official AZ1, AZ8] [Observed AZ2]
- **Need / wound / lie / deepest fear:** Not applicable (existing public persona). None is assigned.
- **Boundary and breaking point:** horror, bugs, cilantro and very sweet food are on her list of dislikes; she
  plays horror games and horror mysteries anyway. [ASR AZ20, her April Fools self-introduction] [Observed AZ4
  titles]
- **Values shown in public (fan summaries, secondary):** persistence ("a person who keeps putting effort into her
  abilities"); comforting fellow members; going deep on what she loves (GeoGuessr, map reading, Key visual novels). [Observed AZ2
  §Personality, secondary] [ASR AZ20]

## Core Contradiction
A dramatic diva with a mythic introduction, who turns out to be the friendly member giggling at her own puns,
shouting "Gēsu!" at a map and, per a secondary transcription, answering Tokino Sora's accidental prank with
"kono yarō" ("you bastard"). [Official AZ1] [Observed AZ2 §Personality, secondary]

## Behavioral Traits
1. A GeoGuessr ace: one of the few officially recognized GeoGuessr players in Japan (2023); "one-minute
   GeoGuessr" challenges on train stations; a FUWAMOCO-themed GeoGuessr map played with the twins (2024, archived
   metadata). Her map-reading habit is a stated hobby. [Observed AZ2 §Trivia; AZ3, secondary; AZ4 titles] [ASR AZ20]
2. Says "Floor!" (yuka) and "Ceiling!" (tenjō) when an emotion hits hard (her official "words"). [Official AZ1]
3. Likes puns (dajare), by her own list in her April Fools stream; chat guessed it before she said it. [ASR AZ20,
   first model]
4. Dances other members' songs in her shorts (Calli's "Orpheus," 2025-10-09, archived metadata lXLBb9IVraI; in 2026 Laplus, Towa and Nene,
   Miko, Koyori, Riona, Lui, Zeta). [Observed AZ4 titles]
5. A Key and anime fan ("Kagikko"): AIR, CLANNAD, Angel Beats!, Charlotte, Little Busters!, Nanoha, Macross
   Frontier and Delta shaped her, she says (ASR); per the wiki she is a fan of the virtual singer KAF. [ASR AZ20]
   [Observed AZ2 §Trivia, secondary]
6. April Fools 2026: she streamed as a nervous "newly debuted" VTuber on her original 3D design, while chat
   "guessed" everything about her ("Chotto chotto, naande sonna minna jōhō o motteru no?" "Wait, wait, why do
   you all have so much information?"), and played a mock villain before a dense slide ("Kono mojisū ni kyōfu
   suru ga ii," "Tremble at this word count"). [ASR AZ20; both models]
7. Plays RPGs and mysteries blind and narrates her losses grandly: "Senryakuteki tettai" ("strategic retreat"),
   "Iyā, osoroshii yume datta na" ("What a frightening dream that was"), "Bottakuri!" ("Rip-off!") at a shop;
   she names her heroes after herself ("Azu," "great detective Azukichi"). [ASR AZ20; both models]
8. Popular for ASMR (a "last-train station names" series in 2026). [Observed AZ3, secondary; AZ4 titles]

## Voice Profile
- **Greetings / sign-offs:**
  - Official: "I'm the Virtual Diva AZKi! I love music and singing!"; her message line "This moment is key, this
    is AZKi!" [Official AZ1]
  - Official Japanese greeting: 「こんあずきー！」 ("Kon-AZKi!", a greeting pun on "konnichiwa"). [Official AZ9]
  - April Fools 2026 self-introduction: "Bācharu dībā AZKi, kasō sekai no utahime desu" ("Virtual Diva AZKi, the
    songstress of the virtual world"). [ASR AZ20, Y5BPxMCI6oU 0:06:36]
- **Catchphrases & bits (verbatim → trigger → estimated frequency):**
  - 「ゲース！」 ("Gēsu!", gloss "Guess!") → locking in a GeoGuessr answer; "Yoshū ga ikiteru" ("my prep is paying off") when it
    lands. [ASR AZ20, 3ri2_FG67uY 0:15:50, 0:11:23; both models] [Observed AZ2 caption; AZ4 titles]
  - "Yuka!" ("Floor!") / "Tenjō!" ("Ceiling!") → a strong emotion. [Official AZ1]
  - "Kono yarō" ("you bastard") → a secondary transcription of her reaction to Tokino Sora's accidental prank.
    [Observed AZ2 §Personality, secondary]
  - "Senryakuteki tettai!" ("Strategic retreat!") → losing a fight. [ASR AZ20, ZlaE59NgPpg 0:21:58; both models]
  - "Bottakuri!" ("Rip-off!") → a shop price. [ASR AZ20; both models]
- **Vocabulary / fillers:** "hai," "ē?" surprise, "nanka," "chotto chotto"; she calls herself
  "AZKi" in the third person when introducing herself. [ASR AZ20, first-model counts in
  research/audio-check/azki.md]
- **Profanity:** rare; a mock "kono yarō" for a prank. [Observed AZ2, secondary]
- **Language:** streams in Japanese; she participated in Calliope's English lesson with IRyS and Watame (2022,
  archived metadata). [Observed AZ5]
- **Laughs, noises:** a drawn-out "e~?" when chat knows too much (ASR). A soft giggle is a provisional performance
  choice; transcription does not capture laughter reliably. [ASR AZ20]
- **Rhythm & rhetoric:** steady when she presents (slides, self-introductions), quick and excited in a GeoGuessr
  round. [ASR AZ20]
- **Timbre / pitch / pace (for voice performance):**
  - Measured (AZ20): in a 2026 RPG window, median about 244 Hz; excited GeoGuessr play runs higher (about
    312 Hz), and the April Fools window, where she plays a nervous new VTuber, higher still (about 340 Hz); about 200–220 transcribed characters a minute of speech (different games and reading loads make this
    no basis for comparing members). Game audio is mixed in; see research/audio-check/azki.md. These are
    mixed-recording estimates, not synthesis targets.
  - Provisional (interpretation): a clear, warm mid-range singer's voice, brightening into a playful lilt for
    jokes and puns; diction and giggles are performance choices, not listening observations. A listening check would still need to establish timbre details.
- **Sounds off (not the proposed default):** cold or aloof delivery; constant shouting; a babyish voice.

### Tone Shifts
The middle column is provisional voice direction unless a source is named.

| Situation | Tone / pitch / pace | Characteristic phrasing |
|---|---|---|
| Introduction | Clear, poised | "I'm the Virtual Diva AZKi! I love music and singing!" (AZ1) |
| GeoGuessr | Quick, focused, then a shout | 「ゲース！」 ("Gēsu!") … "Azayaka na manten o totte ikimasu." (ASR AZ20) |
| Overwhelmed by a moment | Bursting | "Yuka!" / "Tenjō!" (AZ1) |
| Chat knows too much | Mock-flustered | "Chotto chotto, naande sonna minna jōhō o motteru no?" (ASR AZ20) |
| Losing a fight | Grand, mock-dignified | "Senryakuteki tettai." … "Iyā, osoroshii yume datta na." (ASR AZ20) |
| Comforting a friend | Soft, warm | **Style demo:** "Daijōbu da yo. Yukkuri de ii kara ne." ("It's okay. Take it slow.") |

### Sample Lines
1. "I'm the Virtual Diva AZKi! I love music and singing!" (Official AZ1)
2. "This moment is key, this is AZKi!" (Official AZ1)
3. "バーチャルディーバーあずき、仮想世界の歌姫です" — "Bācharu dībā AZKi, kasō sekai no utahime desu" ("Virtual Diva AZKi, the songstress of the virtual world") (ASR AZ20, Y5BPxMCI6oU 0:06:36; same reading in both models)
4. "Yuka!" ("Floor!") (Official AZ1, her word for a strong emotion)
5. "ちょっとちょっとなんでそんなみんな情報を持ってるの" — "Chotto chotto, naande sonna minna jōhō o motteru no?" ("Wait, wait, why do you all have so much information?") (ASR AZ20, 0:08:05)
6. "パクチー！いや、一番嫌い！いらない！" — "Pakuchī! Iya, ichiban kirai! Iranai!" ("Cilantro! No, I hate it most! Don't want it!") (ASR AZ20, 0:12:09)
7. "この文字数に恐怖するがいい" — "Kono mojisū ni kyōfu suru ga ii" ("Tremble at this word count") (ASR AZ20, 0:17:10)
8. "戦略的撤退" … "いやー恐ろしい夢だったな" — "Senryakuteki tettai" … "Iyā, osoroshii yume datta na" ("Strategic retreat" … "What a frightening dream that was") (ASR AZ20, ZlaE59NgPpg 0:21:58–0:22:04)
9. "ゲース！" — "Gēsu!" ("Guess!") (ASR AZ20, 3ri2_FG67uY 0:15:50)
10. "鮮やかな満点を取っていきます" — "Azayaka na manten o totte ikimasu" ("I'll take a brilliant perfect score") (ASR AZ20, 0:16:23)

## Appearance Anchors (avatar)
- 158 cm; 3D modeler Kasoku Sato across her designs; current illustration by Scottie. Long dark hair with pink
  streaks and pink underneath, light purple eyes, a floral hairpin; a long dress with a partly pink skirt and a
  light beige half jacket; dark boots with pink triangle zippers. Height official; the rest a secondary
  description. [Official AZ1] [Observed AZ2 §Appearance, secondary]
- Her fan mark is ⚒️ (for the "Pioneers"); her fans' mascot is a pink beaver with starry eyes.
  Later looks include a 2025 birthday outfit (wavy twintails, a pink hoodie), the "Departure" concert dress with a
  floating golden crown (2025) and a little-devil outfit with horns, wings and a color-changing left eye (2026).
  [Observed AZ2 §2023–§2026, secondary]

## Background Timeline
| Date | Event | Relevance |
|---|---|---|
| 2018-11-15 | Debut as "Virtual Diva AZKi" | [Observed AZ2; AZ3, secondary] |
| 2019-05-19 | Joins hololive production's music label INoNaKa Music, with Hoshimachi Suisei | [Observed AZ2; AZ3, secondary] |
| 2021-07-31 | Kiara's HOLOTALK, 13th guest | [AZ5 CohBCNY9Pm4] |
| 2022-03-12 | Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame | [AZ5 32NVpmKdAOs] |
| 2022-04 | Transfers from INoNaKa Music to hololive's main group ("0th generation") | [Observed AZ2; AZ3, secondary historical reference] |
| 2022-12-31 | "story time" as Star Flower with Suisei, Moona Hoshinova and IRyS | [Official AZ6] |
| 2023-03-09 | GeoGuessr with Hakos Baelz | [AZ5 T594r3CnuW8] |
| 2023-10-04 | Major debut (Victor Entertainment, until 2025); SorAZ with Tokino Sora debuts 2023-12-20 | [Observed AZ2; AZ3] |
| 2024-02-09 | A FUWAMOCO-themed GeoGuessr map with the twins ("FWMCAZ") | [AZ4 Lk7Rlt-MVB4, archived metadata] |
| 2024-08-13 | Singing collab with Minato Aqua and FUWAMOCO | [AZ4 _VnNO5TMkBM] |
| 2025-07 | 7th birthday 3D live "Sweet Pop Story"; FUWAMOCO appeared ("Bon appétit♡S"; secondary setlist) | [AZ4 Dzw7zsjUoOI] [secondary setlist] |
| 2025-07-19 | R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora, Ina, IRyS and Kronii (the description's lineup) | [AZ4 _gZdFTluxtc] |
| 2025-09-18 | "AZUIRO BESTIE DAYS" with Kazama Iroha (official digital release) | [Official AZ10] |
| 2025-11-19 | Solo concert "Departure" at Pia Arena MM (the wiki counts it as her tenth); EPs "Re:Start" and "Re:Birth" (11-05) | [Official AZ8] [Observed AZ2, secondary count] |
| 2026-03-07 | hololive 7th fes. "Ridin' on Dreams," STAGE 3 (with IRyS, Bae, Shiori) | [Official AZ7] |
| 2026-04-01 | April Fools: a "new VTuber" debut on her original design | [AZ4] [ASR AZ20] |
| 2026-05-18/19 | AS_tar with Suisei: a horror off-collab, then "Going My Way" | [AZ4] |
| 2026-07-01 | "AZKi 8th Birthday Live 'Cross Over'": little-devil outfit; she performed Konomi Suzuki's "Redo"; IRyS appears in the archived short metadata ("A Cruel Angel's Thesis"; secondary setlist); "Saikyo Mirai Shodo" (credited to AZKi and Konomi Suzuki) released digitally 07-02 | [Observed AZ2; AZ4] [Official AZ11] [secondary setlist] |
| 2026-07 | Kagawa Prefectural Police traffic-safety ambassador; a commendation, "a hololive first" | [AZ4 titles] |
| 2026-09-20/21 | RosaMiA (with Aki Rosenthal and Ookami Mio): "Blossom Sinfonia," premiered 09-20 (reported), official digital release 09-21 | [Observed AZ2] [Official AZ12] |

## Relationship Map
Public exchanges only. Her ties with the English cast and the other three Japanese members on this project are
on the world card "JP Senpai Pairs." Unit and pair labels (AS_tar, AzuIro, KanatAZ) and RosaMiA's roster are
public labels from a secondary reference; song credits are official.

| Person | Public relationship | What happens on stream | Source |
|---|---|---|---|
| Hoshimachi Suisei | 0th gen; "AS_tar" (formerly "Ex-INNK") | Labelmates at INoNaKa Music; Star Flower; a 2026 horror off-collab and "Going My Way" | [AZ2] [AZ4] |
| IRyS | Star Flower | "story time" (2022); IRyS's "Inochi" cover (2021-07-18, archived); Calli's English lesson (2022); R.E.P.O. JP & EN (2025); "A Cruel Angel's Thesis" at Cross Over (2026, secondary) | [Official AZ6] [AZ5] |
| FUWAMOCO (Fuwawa, Mococo) | "FWMCAZ" | A FUWAMOCO-themed GeoGuessr map (2024); singing with Aqua (2024); appeared at her 2025 birthday live (secondary setlist) | [AZ4] |
| Takanashi Kiara | — | HOLOTALK #13 (2021-07-31, archived); the 2023 Sports Festival white team | [AZ5] [AZ4] |
| Mori Calliope | — | Calli's English lesson #03 (2022-03-12, archived); AZKi's "Orpheus" dance short (2025-10-09) | [AZ5] [AZ4] |
| Hakos Baelz | — | GeoGuessr, "lost simulator" (2023); Bae's MMD dance to AZKi's "Oki Doki" (2025) | [AZ5] |
| Ouro Kronii, Elizabeth Rose Bloodflame | — | Fellow members of Tokoyami Towa's 2025 New Year Game Festival team (secondary roster) | [AZ4] |
| Ninomae Ina'nis, Ouro Kronii, IRyS | — | R.E.P.O. "JP & EN" (2025-07-19); Elizabeth was not in it | [AZ4 _gZdFTluxtc] |
| Shiori Novella, Raora Panthera | kouhai | Dance shorts to her songs (2025–2026) | [AZ5] |
| Tokino Sora | "SorAZ" | Her SorAZ partner; a major-label duo (2023) and "First Gravity" (2024) | [AZ2] |
| Amane Kanata | "KanatAZ" (secondary label) | A collaborator associated with KanatAZ | [AZ2, secondary] |
| Kazama Iroha | "AzuIro" (secondary label) | Frequent partner since 2022; their original "AZUIRO BESTIE DAYS" (2025-09-18) | [AZ2] [Official AZ10] |
| Nekomata Okayu, Nakiri Ayame | — | No direct pair; Ayame was on her 2023 Sports Festival white team (Ayame's stream description) | [AZ4 tHP7bd8Jtm0] |
| Hakui Koyori, Yukihana Lamy | "KoZMy" | A trio formed in 2025; a 3D karaoke with Koyori (2026); Lamy is also in "KALAZ" with Amane Kanata | [Koyori file KO4] [Lamy file LM2] |
| Sakamata Chloe (affiliate) | "Kanaken" with Amane Kanata | Minecraft construction "company," Chained Together and a 3D live (2024) | [Chloe file CH4] |
| La+ Darknesss | — | Games and an ASMR "evaluation" (2025) | [La+ file LA4] |

## Arc
- **Starting point:** active at the 2026 baseline: her 8th birthday live "Cross Over," a new unit (RosaMiA),
  AS_tar's "Going My Way," and a traffic-safety ambassador role.
- **Turning points / end point:** open.

## Story Engine
- Trouble she brings: a map challenge nobody else can win; a pun that derails a serious moment; a diva entrance
  that collapses into giggles; a horror game she insists she hates and plays anyway.
- Scene seeds ([Unverified] proposed fiction, awaiting author approval):
  1. AZKi drops the EN cast at an unknown train station and makes them guess where they are.
  2. A duet rehearsal with IRyS where AZKi's "Floor!" interrupts every chorus.
  3. FUWAMOCO ask AZKi-senpai to build a second map; she hides a pun in every location.

## Secrets & Foreshadowing
- **Truth:** none assigned.

## Intimacy & Boundaries (non-explicit)
(None.)

## Hard Facts (continuity)
- Debut 2018-11-15; hololive main branch from 2022-04-01; 0th generation; birthday 1 July; 158 cm; fans
  "Kaitakusha" (Pioneers); oshi mark ⚒️; units SorAZ, AS_tar, Star Flower, AzuIro, KanatAZ, RosaMiA.
- Official words: "Floor" (yuka) and "Ceiling" (tenjō) for strong emotions.

## Sources (checked 2026-10-02)
- AZ1 Official profile: https://hololive.hololivepro.com/en/talents/azki/
- AZ2 AZKi wiki page (secondary), by section, read via the fandom API: https://virtualyoutuber.fandom.com/wiki/AZKi
- AZ3 Japanese Wikipedia, AZKi (secondary): https://ja.wikipedia.org/wiki/AZKi
- AZ4 Stream archive metadata, her channel (archive.ragtag.moe): Y5BPxMCI6oU (April Fools, 2026-04-01),
  ZlaE59NgPpg (Chrono Trigger #2, 2026-05-15), 3ri2_FG67uY (GeoGuessr, 2026-05-12), 22FaM0PkTwU (Paranormasight
  #1, 2026-07-13), v60QmEvEQqw (AS_tar off-collab, 2026-05-18), Lk7Rlt-MVB4 (FWMCAZ), _VnNO5TMkBM (with Aqua and
  FUWAMOCO), Dzw7zsjUoOI (Sweet Pop Story), _gZdFTluxtc (R.E.P.O. JP & EN), 9sOBwx7uC0o (Towa's team, 2025),
  tHP7bd8Jtm0 (Sports Festival 2023, Ayame's channel), lXLBb9IVraI (Orpheus), fotf1akH02g (Kagawa police,
  2026-07-22), 2026 dance shorts
- AZ5 Other members' archive metadata: see the world card "JP Senpai Pairs" (S1)
- AZ6 Official song page, "story time": https://hololive.hololivepro.com/en/music/249/
- AZ7 hololive 7th fes. cast lineup: https://hololivesuperexpo.hololivepro.com/2026/en/fes/cast/
- AZ8 Official "Departure" concert report: https://hololive.hololivepro.com/events/departure/; "Cross Over" event
  listing: https://hololive-tsuushin.com/last-schedule/7-1azki-8th/ (secondary); debut-anniversary statement:
  https://hololive.hololivepro.com/news/20221111-01-101/
- AZ9 Official profile, Japanese: https://hololive.hololivepro.com/talents/azki/
- AZ10 Official song page, "AZUIRO BESTIE DAYS": https://hololive.hololivepro.com/en/music/642/
- AZ11 Official song page, "Saikyo Mirai Shodo": https://hololive.hololivepro.com/en/music/768/; "Redo" performance
  listing: https://holo3d-live.com/azki/id340596/ (secondary)
- AZ12 Official song page, "Blossom Sinfonia": https://hololive.hololivepro.com/en/music/813/
- AZ20 Claude's audio check (two-model ASR, Japanese): Y5BPxMCI6oU (2026-04-01), ZlaE59NgPpg (2026-05-15),
  3ri2_FG67uY (2026-05-12), 22FaM0PkTwU (2026-07-13);
  research/audio-check/azki.md

---

## [SW] Name
AZKi

## [SW] Role
Protagonist

## [SW] Pronouns
she/her

## [SW] Groups
hololive, hololive 0th Generation, Star Flower, SorAZ, AS_tar, AzuIro, KanatAZ, RosaMiA

## [SW] Other Names
AZKichi, Azukichi, Azu-chan, AZAZ, AzuAzu, Virtual Diva AZKi

## [SW] Personality
AZKi is the "Virtual Diva," a songstress "reborn into the virtual world to fabricate a new world," and a singer and songwriter who keeps "creating memorable music"; she headlined "Departure" at Pia Arena MM in 2025. Behind the mythic introduction she is playful and warm: she loves puns, cries "Floor!" or "Ceiling!" when an emotion hits hard, and, in a secondary transcription, answered Tokino Sora's accidental prank with "kono yarō" ("you bastard"). She is a GeoGuessr ace who calls out "Gēsu!" ("Guess!") as she locks in an answer, reads maps for fun, and played a FUWAMOCO-themed map with the twins. Fan summaries describe her comforting fellow members and going deep on what she loves (Key visual novels, anime); she dances other members' songs in her shorts. She dislikes horror, bugs, cilantro and very sweet food, and plays horror games anyway.

## [SW] Background
AZKi is an active member of hololive Generation 0. She has no supernatural abilities; her lore is a performed persona. She debuted in 2018 as "Virtual Diva AZKi," joined hololive production's music label INoNaKa Music with Hoshimachi Suisei in 2019, and transferred to hololive's main group in April 2022 (secondary historical reference). Her units include SorAZ with Tokino Sora, AS_tar with Suisei ("Going My Way," 2026), Star Flower with Suisei, Moona Hoshinova and IRyS ("story time," 2022), AzuIro with Kazama Iroha ("AZUIRO BESTIE DAYS," 2025) and, from 2026, RosaMiA. She headlined "Departure" at Pia Arena MM in 2025 and held her 8th birthday live, "Cross Over," on 2026-07-01. With the English cast she sings in Star Flower with IRyS, took Calli's English lesson (2022), was Kiara's 13th HOLOTALK guest (2021), and played a FUWAMOCO-themed GeoGuessr map with the twins (2024), who also appeared at her 2025 birthday live.

## [SW] Physical Description
AZKi's avatar is 158 cm tall, with long dark hair streaked and lined with pink, light purple eyes and a floral hairpin. She wears a long dress with a partly pink skirt and a light beige half jacket on one side, with dark boots trimmed with pink triangle zippers. Her fan mark is ⚒️, for her fans, the Pioneers; in 2026 she also has a little-devil outfit with horns and wings.

## [SW] Dialogue Style
Streams in Japanese with a gentle, friendly register, reacting with a drawn-out "e~?" and introducing herself in the third person ("Virtual Diva AZKi, the songstress of the virtual world"). A playful streak runs under the poise: puns, mock-villain flourishes ("Tremble at this word count"), grand retreats in games ("Senryakuteki tettai," "strategic retreat"), "Bottakuri!" ("Rip-off!") at shop prices, 「ゲース！」 in GeoGuessr, "Floor!" or "Ceiling!" when moved, and a flustered "chotto chotto" when chat knows too much. Careful diction and soft giggles are provisional performance choices. When a story renders her speech in English or Chinese, keep the poised diva voice cracking into playfulness.

## [SW] Catchphrases
「こんあずきー！」 ("Kon-AZKi!", official Japanese greeting); "I'm the Virtual Diva AZKi! I love music and singing!" (official); "This moment is key, this is AZKi!" (official); 「ゲース！」 ("Gēsu!", gloss "Guess!", GeoGuessr); "Yuka!" ("Floor!") and "Tenjō!" ("Ceiling!") for strong emotions (official words); "kono yarō" ("you bastard," a secondary transcription, to Tokino Sora's accidental prank); 「戦略的撤退」 ("Senryakuteki tettai," "Strategic retreat"); "Bottakuri!" ("Rip-off!"); 「この文字数に恐怖するがいい」 ("Tremble at this word count"). Her fans are the Pioneers (Kaitakusha). The English glosses are ours.

## [SW] Voice & Delivery
Provisional direction for an original designed voice: a clear, warm mid-range singer's voice, poised when she presents, lifting into a playful lilt for puns and jokes, quick and focused in a GeoGuessr round with a bright shout on "Gēsu!" Cold or aloof delivery is not the proposed default.

## [SW] Audio Tags
Proposed ElevenLabs v4 performance directions for her dialogue, for an original designed voice (never imitate the real member); test them with the chosen voice. Register (qualitative): clear, warm mid-range voice; poised and friendly by default. Default tags: [warm, clear]. By situation: introduction [poised, diva]; GeoGuessr [focused, quick] then [triumphant] on "Gēsu!"; a pun [playful] then [giggles]; overwhelmed by a moment [overjoyed] ("Floor!"); a prank [mock-indignant]; comforting someone [soft, gentle]; horror game [nervous]. With people (proposed scene directions, not observed conversational defaults): Suisei [relaxed, teasing]; FUWAMOCO [cheerful]; IRyS [friendly]. Signature sounds (tag plus a written word = a spoken interjection; a tag alone = a nonverbal sound, not also spelled out): [giggles] (tag only); "e~?" (spoken). Keep in the words: "Gēsu," "yuka," "tenjō," "Kaitakusha." Reading guide (untested): あずき; かいたくしゃ. Not as default: cold or aloof delivery; constant shouting; a babyish voice.

## [SW] Motivation
AZKi wants to keep creating memorable music that touches her Pioneers' hearts, on stage and in her units, and to enjoy what she loves to the fullest, from maps to puns.

## [SW] Relationships
Hoshimachi Suisei: labelmate since INoNaKa Music and 0th-generation partner ("AS_tar"); a 2026 horror off-collab and "Going My Way." IRyS: Star Flower with Suisei and Moona Hoshinova ("story time," 2022); IRyS covered AZKi's "Inochi" (2021); R.E.P.O. (2025); "A Cruel Angel's Thesis" at AZKi's 2026 birthday live. FUWAMOCO: "FWMCAZ," a FUWAMOCO-themed GeoGuessr map (2024), a singing collab with Minato Aqua, and an appearance at her 2025 birthday live. Takanashi Kiara: HOLOTALK's 13th guest (2021); the 2023 Sports Festival white team. Mori Calliope: her English lesson with IRyS and Tsunomaki Watame (2022); AZKi's "Orpheus" dance short (2025). Hakos Baelz: GeoGuessr (2023). Ouro Kronii and Elizabeth Rose Bloodflame: fellow members of Tokoyami Towa's 2025 New Year Game Festival team. Ninomae Ina'nis and Kronii: R.E.P.O. "JP & EN" (2025). Tokino Sora: her SorAZ partner. Amane Kanata and Kazama Iroha: collaborators associated with KanatAZ and AzuIro ("AZUIRO BESTIE DAYS," 2025). Nakiri Ayame: 2023 Sports Festival teammate. Hakui Koyori and Yukihana Lamy: "KoZMy" (2025), and a 3D karaoke with Koyori (2026); Lamy is also in "KALAZ" with Amane Kanata. Sakamata Chloe: "Kanaken" with Kanata (Minecraft and a 3D live, 2024). La+ Darknesss: games (2025).

## [SW] Secrets
(none)

---

## Merge Record
- **Structure and evidence:** Claude's draft (2026-10-02, author order: add Hoshimachi Suisei, AZKi, Nakiri
  Ayame and Nekomata Okayu): official profile (AZ1, AZ9), wiki (AZ2, by section), Japanese Wikipedia (AZ3,
  secondary), archive metadata (AZ4, AZ5), official song and event pages (AZ6–AZ12), and Claude's two-model
  Japanese audio check (AZ20, research/audio-check/azki.md).
- **GPT one-round claim check (2026-10-02, xhigh, live search; run A in runs/20261002-0529-character-Hoshimachi-Suisei/gpt-free.md),
  merged by Claude:**
  - Applied: the birthday/anniversary conflation is corrected everywhere ("AZKi 8th Birthday Live 'Cross Over'"
    on 2026-07-01; her debut anniversary is in November); "most experienced musician" and the ten-concert
    count are removed from the exported fields; "kono yarō" is labeled a secondary transcription about Tokino
    Sora's accidental prank, without "best friend"; the FUWAMOCO map is "a FUWAMOCO-themed map played with the
    twins," not a map she built; "an active hololive member in Japan" → "an active member of hololive
    Generation 0"; the INoNaKa transfer carries a secondary label; appearance and fan summaries are labeled
    secondary; "hai," giggles and careful diction are provisional; the English-cast language default is
    narrowed to Calli's English lesson; Sora/Kanata/Iroha rankings removed; the festival team (Kronii,
    Elizabeth) and the R.E.P.O. lineup (Ina, Kronii, IRyS) separated; "Redo" is Konomi Suzuki's song she
    performed, "Saikyo Mirai Shodo" is credited to AZKi and Konomi Suzuki (2026-07-02); the 244 Hz register
    basis and the cross-member pace ranking removed; 「ゲース！」 is given in Japanese with its gloss; partner tags
    are proposed directions, "harmonizing" removed; IPA replaced by kana; "never cold or aloof" softened; the
    IRyS appearance at Cross Over replaces the old open question; the official Japanese greeting 「こんあずきー！」
    added (confirmed on the official Japanese profile); Azukichi and AzuAzu added to Other Names.
  - Kept, with Claude's verification in the archive's metadata (the reviewer could not open these pages):
    HOLOTALK #13 (CohBCNY9Pm4, 2021-07-31), GeoGuessr with Bae (T594r3CnuW8, 2023-03-09), the "Orpheus" dance
    short (lXLBb9IVraI, 2025-10-09) and the 2023 Sports Festival white team with Ayame and Kiara (tHP7bd8Jtm0,
    Ayame's description lists AZKi).
  - The audio report's second-model excerpts are trimmed to the needed performance spans.
- **2026-10-02, cast expansion (author: add Marine, Noel, Lamy, Botan, Secret Society holoX and Kikirara Vivi), reciprocal ties:** Koyori and Lamy (KoZMy, KALAZ), Chloe (Kanaken) and La+ added (sources in the new member files).

## Open Questions
1. IRyS appears in the archived Cross Over short metadata ("A Cruel Angel's Thesis"); attach the primary short
   when accessible.


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

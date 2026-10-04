# Task 05 — Cross-cohort bridge audit

You are GPT, senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only, answer in English,
and run sequentially without parallel GPT audits.

Bridge: events — must be events or ties
Packet: projects/holoen/research/qa/packets/events.md (inline below)
Registry: projects/holoen/research/qa/registry.json

## Binding rules and inputs

- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.

Read projects/holoen/project.md, framework/prompts/shared-rules.md, the packet,
registry, research/qa/manifest.json, research/qa/resolutions.md, and available
research/qa/audit-*.md reports relevant to the bridge. Reports outside runs are
permitted. Never read projects/*/runs/, even through links. Modify no files.

The baseline is 2026-09-30. Use later verification only to establish baseline-era
facts. Cover all 33 character and 28 world cards (the authorized inventory in the
packet) through relevant cross-file claims. External participants may remain reference-only; create no new cards.

Use official fictional lore and public persona behavior only. Exclude performer
identity, private appearance, past activities, private life, health, real family,
breaks and reasons, trips, auditions, nationality and mother tongue. Public
disclosure does not remove these exclusions. Describe accents only as audible
features. Distinguish fictional families, avatar lore and in-game travel from
real-life information; public event locations do not establish personal travel.

No inferred intimate relationships, sexuality or hidden psychology; no lyrics,
long transcripts, explicit sexual content, real-voice cloning or identifiable
imitation. Preserve evidenced swearing and performed jokes without sanitizing
them. Label invented calibration lines with the project label “Style demo”.

Do not reopen isolated claims already reviewed unless they conflict across files.
This audit groups claims by shared event or relationship, checks previous fixes
and catches propagation failures. Broad recency research, X completeness and
detailed voice enrichment belong to tasks 06, 08 and 09. Newly encountered scope
violations must still be reported.

## Evidence and quotation

OFFICIAL means agency profiles, announcements, reports or official written copy.
Short exact written excerpts may be quoted; distinguish lore, announcements and
post-event reporting.

PRIMARY means firsthand public posts, streams or other public material.
Short written posts may be quoted as written. Audio-derived quotations require
the ASR gate below, regardless of channel ownership.

ARCHIVE_METADATA supports only its stated title, description, dates, listed
participants and credits. Quote it as metadata, never dialogue. Scheduled names
do not prove actual participation; upload time does not necessarily date the event.

SECONDARY means wikis, fan transcripts, clips or mirrors. Use attributed
paraphrases. Short quotations of secondary prose remain attributed to its author.
A fan’s transcript cannot establish the performer’s exact spoken words.

ASR is machine transcription, not listening. Spoken quotations require explicit
contiguous approved spans shared by two models transcribing the same public
audio window. Record source, timestamp, both models and separate speaker
attribution. Document punctuation/case normalization only; preserve wording,
repetitions and order. Never stitch separated spans or treat semantic agreement
as verbatim agreement. Two-model agreement cannot establish who spoke, tone,
relationship strength or recurring usage.

No lyrics; keep quotations brief and total external quotations within 25 words
per non-lyrical source. Distinguish Official setting, Public-behavior observation,
Author-approved adaptation and Unverified. Unverified assertions cannot enter
[SW] fields as facts.

Use local evidence first. Search live only to resolve disagreement or apparent
staleness; prefer official pages, then primary sources. Open supporting sources
before claiming fresh verification. Label inherited evidence “not reopened.”
Record inaccessible sources without treating inaccessibility as disproof.
Separate source publication date, event date and actual verification date.

## Common procedure

Check source hashes before auditing and reconcile changes before concluding.
Packets are focus aids: inspect permitted canonical files and related research
when necessary. Match canonical names, aliases and units; inspect complete
bullets/table rows and relevant pronoun antecedents. Report extraction gaps.

Group claims under stable registry keys across cohorts. Check the resolution
ledger before creating findings. Verify implemented changes against canonical
text; a “resolved” label alone proves nothing. Track all propagation destinations.

Treat the registry as an index requiring evidence, not an authority that overrides
sources. Preserve uncertainty and date precision rather than inventing detail.

## If bridge = events

Compare both histories, Concerts, unit cards, character timelines, Background,
Relationships and all other relevant exported claims.

Check event identity; announcement versus event dates; source time zones;
genuine multi-day schedules versus time-zone conversions; scheduled versus held
events; actual participants versus historical unit membership; debut, graduation
and affiliate intervals; date-bound organization names; release and performance
credits; milestone counts.

Do not infer current activity from an old appearance or current unit membership
from historical participation. A later guest appearance need not reverse an
affiliate/graduation status. Record exceptions with evidence.

Check status boundaries at the source’s supported precision. Never invent a
midnight transition or time zone. Describe factual departures without excluded
reasons. Flag optional coverage gaps separately from contradictory dates.

## If bridge = ties

Compare character Relationships and Groups, world descriptions and aliases,
Relationship Maps, concert units and incoming claims across every cohort.

Check canonical endpoints, unit membership, named-event context, official versus
fan/performed naming, alias ownership, and directional verbs: who invited,
supported, credited, performed with or publicly praised whom.

A collaboration supports participation, not private friendship strength.
Do not reverse directional claims, rank closeness by archive counts, infer mutual
feelings or convert a performed pairing into a real relationship.
A missing reciprocal mention is a coverage question, not automatically an error.

Keep multi-person unit aliases on suitable world cards and memberships in Groups;
do not make the unit an individual’s Other Names alias. Review collisions without
automatically deleting valid aliases. Keep Fuwawa and Mococo distinct.

## Priorities, decisions and IDs

P0: resolve before delivery—scope breaches, fabricated attribution, unapproved
spoken quotations, or defects preventing a trustworthy usable release.
P1: priority factual correction, material inconsistency or evidenced coverage gap.
P2: optional clarity, retrieval or usability improvement.

Finding priority does not determine validation severity by itself; material
contradictions can block even when P1.

“Author decision” is an explicit editorial choice between valid alternatives,
including optional enrichment or a disclosed limitation. It is neither GPT
approval nor factual verification, and cannot waive the current scope.
Recommend a concrete choice; handle routine corrections without escalation.

Use BR-{TYPE}-{NNN}: TYPE = DATE, STATUS, EVENT, ROSTER, TIE, CREDIT, UNIT, ALIAS,
SCOPE, QUOTE, VOICE, EXPORT or COVERAGE. Both bridge passes share this namespace.
Continue ledger numbering. Reuse cohort IDs for the same underlying issue;
create a new BR ID only for a distinct cross-cohort problem and link related IDs.

## Exact output format

Use exactly these four top-level headings:

## Coverage

Snapshot hash; packet/registry hashes; source-hash manifest reference; bridge;
files/fields and claim keys examined; cohort findings checked; exclusions;
unresolved evidence; missing inputs; snapshot changes.
Distinguish examined material from freshly verified evidence.

## Findings

| ID | Priority | Claim key | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|

One actionable finding per row; use linked patch rows for different replacements
under one ID. Supply exact old text and paste-ready replacements, or DELETE.
Escape pipes; represent internal newlines with <br>. If unsupported, recommend
deletion or limited wording rather than inventing a replacement. Write “None”
when there are no findings.

## New verified facts

Use the identical table columns; absent old text is “—”. Give insertion locators.
Include only useful facts verified during permitted checking. Distinguish
candidates from accepted additions. Otherwise write “None.”

## Merge handoff

List dependencies, unresolved conflicts, propagation order, registry updates,
and finding IDs recommended for acceptance, rejection, deferral or more evidence.
Do not claim edits were applied. Name downstream tasks needing the result.

End with “Open questions”: at most five genuine author decisions or unresolved
input questions, or “None.”


## Run budget (added by Claude, 2026-10-02; supersedes the 2026-10-01 efficiency note)

One audit must finish inside one quota window (about 200k tokens). On 2026-10-02 a run exceeded the window
part-way through and returned nothing, so the budget below is binding. Every tool call re-sends the whole
conversation, so the number of tool calls drives cost far more than the size of what you read.
- **Your inputs are inline below** (the packet: owned fields, dossier timelines, hard facts and every incoming
  claim with its `file › field` locator). Do not re-open the packet files or print whole bible files.
- **Snapshot:** your working directory is a copy of the project taken when this run started (no `runs/`, no
  git); the inline packet was rebuilt from the same files a moment before. Do not compute or compare hashes;
  procedure step 1 is satisfied by this note. Report the packet's snapshot line in Coverage.
- **Budget:** about 12 tool calls in total, including web searches. Batch all local lookups into a few shell
  commands (`grep -n -e A -e B -e C file1 file2 …`). Use at most 6 live web searches, only to settle a
  contradiction or a likely-stale claim, official pages first.
- Line numbers are optional; the exact old text is mandatory (Claude's merge matches exact text).
- If the budget runs short, stop investigating and report the open items as further-evidence rows in Merge
  handoff rather than leaving the audit unfinished. A complete audit with disclosed limits beats a lost one.
- Ignore the run directory's `context.md`; it is not part of this task.

## Inline inputs

These are the exact files at the snapshot commit; do not re-open them.

### projects/holoen/project.md (the author's constitution; Chinese)

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
- 「待確認」與「合併紀錄」也用英文；Claude 回報給作者時再用中文摘要。**給作者的最終匯報一律用繁體中文（作者 2026-10-04）。**

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

### framework/prompts/shared-rules.md

# 共同規則（Claude 與 GPT 都照這份做）

你是一個兩人小組的其中一員，另一位是另一家公司的模型。你們的共同任務是替作者做
**小說設定的調查、整合與框架建議**，成品會被貼進 Sudowrite 的 Story Bible，
由 Sudowrite 負責實際寫正文。你們不寫連續的場景正文；單獨的「聲音校準台詞」（示範角色
怎麼說話的短句）屬於設定工作，可以寫，但要標「風格示範」。

**專案規則以提示裡附的 project.md 為準**，它可以覆蓋這份共同規則的預設（例如語言、真實優先）。

## 分工界線

- **成人／露骨內容由 Sudowrite 處理。** 你們不寫露骨的性內容。遇到相關需求時，只做
  非露骨的角色化定位（關係性質、依附模式、界線、權力動態、情感上的渴望與恐懼），
  並在該處放上標記 `【Sudowrite 處理】`。需要交接一個場景時，用這個非露骨格式：
  - 場景入口：目前關係、各自目的
  - 界線：已表達的同意、拒絕與其他限制
  - 情感轉折：信任、誤解或權力關係如何改變
  - 場景出口：下一場開始前已成立的結果
  - 後續連續性：誰知道什麼、承諾什麼、仍誤會什麼
  - 【Sudowrite 處理】
  場景寫完後，只把非露骨的結果與設定變動收回 bible。
- 粗口、挑逗梗、黑色幽默、暴力、犯罪、創傷等屬於正常的小說素材，可以寫；
  忠於角色時應該保留，不要為了安全而淡化。
- **以真人為基礎的角色**（VTuber、藝人、實況主等）：只用公開的角色人設、官方設定與
  直播／作品中公開呈現的言行。不寫、不推測背後真人的身分、長相、本名、私生活；
  不做親密關係或性方面的推測（該段寫「不適用」）；不抄歌詞或長篇逐字稿，口頭禪與短句引用即可。

## 既有角色與原創角色的差別

- **原創角色**：可以設計動機、傷口、相信的謊言、弧線。
- **既有角色、公開人設、原作角色**：把每條資訊分成四種，並標出來——
  「官方設定」「公開言行觀察」「作者核准的同人改編」「未證實」。
  **不要為了填滿模板而推測隱藏心理**；模板裡的心理段落沒有依據時寫「不適用（既有人設）」。
- 「無此設定」「沒有找到證據」「不適用」是三件不同的事，要寫清楚是哪一個。
- 未證實的內容留在調查區，不以確定語氣進入 `[SW]` 卡片。

## 寫法

1. **行為化，不要形容詞清單。** 「她很固執」→「被反駁時她會把對方的論點複述一遍，
   然後逐條拆掉；從不先道歉」。Sudowrite 會照字面模仿，具體的行為比抽象的特質有用。
2. **設定要對故事有用。** 能幫助辨識角色、維持連續性、建立生活感或產生場景的就保留；
   四種都沾不上的才刪。
3. **避開套路（原創時）。** 若用了常見原型（失憶、天選之人、冷面霸總……），要指出你在哪一點上
   翻轉或具體化了它。忠實重建既有人設時不需要「原創」，也不要擅自改造原作。
4. **硬事實要一致。** 年齡、日期、地名、稱謂、能力的代價等，與 project.md 和既有 bible
   矛盾時，以既有設定為準，並在「待確認」裡指出衝突。硬事實可以隨故事時間線改變，
   但每次變更都要符合時間線並記錄下來。
5. **不確定就標記，不要編造成事實。** 附來源與查核日期；推測寫成「推測」。
6. **語言**：成品用 project.md 指定的語言；人名、術語第一次出現時寫全名，之後全文統一。
7. **Sudowrite 卡片**（`## [SW] …` 開頭的段落）會被直接匯入或貼上：
   - 描述性文字用第三人稱、寫當前狀態；歷史事件用正確的時態。
   - 逐字引用與示範台詞保留原本的人稱、時態和原文。
   - Genre、Style 這類控制欄位可以寫成給 AI 的寫作指令。
   - 不寫給作者看的說明，不用 Markdown 粗體或清單符號以外的格式，遵守字數上限。
   - `[SW]` 後面的欄位名稱是機器辨識用的，**一律照模板原文，不要翻譯**。
8. **Secrets（秘密）**：CSV 不會帶著「隱藏」設定匯入；作者要在匯入後手動隱藏。隱藏的內容
   AI 完全看不到，所以調查區要分開寫「真相」「誰知道什麼」「讀者已知什麼」「目前可以寫的表面線索」，
   只把當下允許使用的線索放進可見欄位；也要檢查 Background 等欄位有沒有藏著秘密的副本。

## 輸出格式

照指定的 schema 輸出完整的 Markdown，不要省略段落；某段沒有內容時寫明是
「無此設定」「沒有找到證據」還是「不適用」。
最後一定要有「待確認」段落，列出你做的假設與需要作者決定的事（最多 5 點）。

### projects/holoen/research/qa/resolutions.md (finding ledger; continue numbering from it)

# QA resolution ledger (holoen)

Stable IDs for every finding the QA program raises, with Claude's disposition. Statuses: **applied** (in the
bible at the commit named), **pending** (accepted, not yet done; owner task named), **deferred** (moved to a
later task), **rejected** (reason given). Each applied fix is also recorded in the affected card's Merge Record.
Source of the CONSULT-* findings: `runs/20261001-1557-check-Project-Consult/gpt-free.md` (round 1) and
`runs/20261001-2050-check-Project-Consult-R2/gpt-free.md` (round 2).

| ID | Finding | Status | Where / commit |
|---|---|---|---|
| CONSULT-P0-001 | Pre-debut private history in exported cards (Bijou, Calli, Advent Pairs) | applied | 6a9212f |
| CONSULT-P0-002 | Private-life activity outside streams (FUWAMOCO, IRyS-and-Nerissa Pairs, Kiara, Nerissa) | applied | 6a9212f |
| CONSULT-P0-003 | Ina's private-routine example (sheet, card, audio report); a language-background claim (Kiara) | applied | 6a9212f |
| CONSULT-P0-004 | Paste sheet lacked the audio Style block | applied (exporter writes it first) | 6a9212f |
| CONSULT-P1-001 | History 2023–2026: Drawn to Dawn and Serendipity rows unzoned | applied (PDT) | snapshot commit |
| CONSULT-P1-002 | Mumei / Fauna-and-Mumei: "R.E.P.O. with all of Promise" ambiguous | applied (IRyS, Kronii, Bae; archive F_EVW5Ig5QE) | snapshot commit |
| CONSULT-P1-003 | OctoClock "Bad Apple"; Kobo's "BLUE CLAPPER" with Kronii and Nerissa | applied | snapshot commit |
| CONSULT-P1-004 | Official Serendipity units missing from Groups / world aliases | applied (Last Writes, Octo'clock, Rocku Wawa, BaeRyS, Bloodraven, B.F.F; Autofister already present) | snapshot commit |
| CONSULT-P1-005 | 2026-09-07 restructuring relied on a wiki | applied (official announcement cited on "hololive") | snapshot commit |
| CONSULT-P1-006 | Kronii ASR report: "Agrees" rows that differ lexically | applied (Kronii rows rewritten by hand; all 151 other bare "Agrees" rows given computed shared spans by `tools/asr_spans.py`; 36 partial rows listed in `research/audio-check/partial-spans.md` for task 09) | this commit |
| CONSULT-P1-007 | Mococo: sparse solo evidence; speaker attribution | task 07 part applied: whole-channel archive search found no other attributable solo window (2026 "MOCOCO POV" is a multi-member role-play; 2024 candidates include her twin); attribution basis now stated separately in research/audio-check/fuwamoco.md; card and sheet say directions stay provisional. Quotation gate stays with task 09 | this commit |
| CONSULT-P1-008 | Performance sheets: settings scale; stale-sheet hashes | scale applied (UI % and API decimals); hashes pending (task 10 release builder) | snapshot commit |
| CONSULT-P2-001 | Myth sixth-anniversary live missing from shared timeline | applied and closed 2026-10-02: verified as held (hololive English channel VOD title; official posts), 2026-09-19 PDT, with the new song "THIS IS MYTH"; propagated to Myth, TakaMori, TakoTori, History 2023–2026, Concerts and the three members (task 06, research/refresh/myth-kronii-20260930.md) | this commit |
| CONSULT-P2-002 | Audio Tags boilerplate before the distinguishing cue | deferred (task 09, all 18 cards at once) | — |
| CONSULT-P2-003 | Gura sheet "pre-2025 stories" excluded her active 2025 months | applied | snapshot commit |
| CONSULT-VAL-001 | Alias "Kronster" on Kronii and Time and Death | applied (removed from Time and Death) | snapshot commit |
| CONSULT-VAL-002 | Alias "hololive English first generation" on Myth and History to 2022 | applied (removed from History to 2022) | snapshot commit |
| CONSULT-X-001 | Calli's "B(+)" listed as a recurring emoticon | applied (removed; the context-poor post dropped) | snapshot commit |
| CONSULT-R2-001 | Incoming claims must include aliases, unit names, table rows and bullets | applied (`tools/qa_packets.py`) | snapshot commit |
| CONSULT-R2-002 | Packet inventory and SHA-256 map | applied (`research/qa/manifest.json`, packet headers) | snapshot commit |
| CONSULT-R2-003 | Registry: status intervals, event precision, directional credits, reference-only people | applied (registry v2; bounded, non-exhaustive) | snapshot commit |
| CONSULT-R2-004 | Promotion provenance outside `runs/` | applied (`research/qa/promotions.md`) | snapshot commit |
| CONSULT-R2-005 | Release candidate + acceptance tied to its manifest hash; finding priority ≠ validation severity | pending (task 10–11) | — |

New audit findings are appended below with their own IDs (`{COHORT}-{TYPE}-{NNN}`, `BR-…`).
| CLAUDE-SCOPE-001 | Process notes that dated or described excluded matters (four cards and x-posts) | applied (generalized to the author's rule; no dates or reasons) | this commit |
| ADVENT-SCOPE-001 | Elizabeth: a private day-off plan in an incoming Voice Profile bullet | applied (deleted) | this commit |
| ADVENT-SCOPE-002 | Pre-debut discovery history (how a member first found hololive/VTubers): Shiori, Advent Pairs, Cross-Branch | applied; Claude propagated the same rule to Raora (Korone row and SW sentence) and Justice Pairs | this commit |
| ADVENT-SCOPE-003 | Nerissa: off-stream habits and private possessions (merch, plush, figures, cooking) | applied (Nerissa, IRyS-and-Nerissa Pairs, Cross-Branch) | this commit |
| ADVENT-SCOPE-004 | History 2023–2026: invented private backstage scene hook | applied (replaced with a public tour-stage hook) | this commit |
| ADVENT-TIE-001 | Cecilia–Mococo Chrono Trigger off-collab widened to both twins | applied (Mococo only) | this commit |
| ADVENT-TIE-002 | FUWAMOCO MORNING #167 guest hosts read as Mococo | applied (Gigi and Cecilia guest-hosted) | this commit |
| ADVENT-UNIT-001 | "kouhai to Myth and Promise from day one" used the later Promise name | applied (Myth, Project: HOPE, Council at debut) | this commit |
| ADVENT-STATUS-001 | Advent status heading used the check date instead of the 2026-09-30 baseline | applied | this commit |
| ADVENT-DATE-001 | Shiori/Bijou: unzoned debut sentence implied all five debuted 2023-07-30 | applied (JST; staggered launch) | this commit |
| ADVENT-DATE-002 | Nerissa's 3D date unzoned | applied (2024-08-09 PDT, two places) | this commit |
| ADVENT-COVERAGE-001 | Registry missed the FUWAMOCO debut (2023-07-31) | applied (generator regex fixed; registry rebuilt; both twins 2023-07-31) | this commit |
| ADVENT-QUOTE-001 | FUWAMOCO: stitched "Right! … Exactly." and a turn attributed to the other twin | applied (paraphrased; no turn attribution) | this commit |
| ADVENT-QUOTE-002 | Elizabeth: "workaholics like me" past the shared span | applied (paraphrase in three places) | this commit |
| CONSULT-P0-002 / CLAUDE-SCOPE-001 (residual) | Leftover private-life process notes (FUWAMOCO, Mococo) | applied (Advent audit) | this commit |
| CONSULT-P1-006 (residual) | Nerissa N20 and Shiori quotations crossing shared spans | applied (Advent audit; Nerissa's Voice Profile, Sample Lines and sheet also split into separate shared spans) | this commit |
| CONSULT-R2-001 (residual) | Incoming-claim retrieval was case-sensitive and missed owned world-card aliases | applied (`tools/qa_packets.py`, `re.I`, world-card names and aliases) | this commit |
| CLAUDE-SCOPE-002 | Process notes still naming the excluded details they removed (Merge Records of Kiara, Nerissa, Calli, Bijou, Ina, FUWAMOCO, Mumei, Raora; FUWAMOCO and Mumei audio reports; one X post in x-posts) | applied (generalized to "private-life material removed"; the post dropped) | this commit |
| CLAUDE-QUOTE-001 | 23 quotations ran past the span both ASR models share (Ame, Calli, Elizabeth, Gigi, Gura, Bijou, Kiara, Mumei, Nerissa, Raora; Ame, Gigi and Gura sheets) | applied (trimmed to the shared run, split into separate shared quotations, or paraphrased; one apostrophe-only difference documented). `tools/span_check.py` now checks every card and sheet against `partial-spans.md`, and V13 fails automatically on any overrun. Quotes never second-model checked remain task 09's | this commit |
| CLAUDE-SCOPE-003 | Process notes and scope headers that tied the break rule to particular members (four Myth-era cards; three Justice cards and the Justice world card) | applied (member-specific notes removed; each card keeps only the general privacy statement) | this commit |
| TASK-06 | Myth/Kronii recency refresh (done by Claude to save GPT quota) | 9 facts applied, 5 candidates held for better evidence: research/refresh/myth-kronii-20260930.md; GPT reviews the additions in the Myth cohort audits | this commit |
| CLAUDE-QUOTE-002 | span_check missed wrapped quotations and the performance sheets' example blocks; `asr_spans.py` re-runs dropped earlier partial rows | applied: both tools fixed (partial-spans.md rebuilt from every report); eight clear overruns trimmed (Calli, Gigi, IRyS, Nerissa, Raora; IRyS, Raora and Shiori sheets); the remaining hand-judged candidates listed in research/qa/span-candidates.md for task 09 | this commit |
| AUTHOR-2026-10-02 | Author order: add Hakos Baelz; do not make Tsukumo Sana | in progress: Bae's character card, "Hakos Baelz Pairs," the performance sheet and audio report (research/audio-check/bae.md) drafted; Bae ties added to 13 cast cards and to Promise, Concerts and Cross-Branch Friends; CHADCast recorded as an official unit; GPT's one xhigh claim-check review queued first (runs/20261002-0236-character-Hakos-Baelz) | this commit |
| CLAUDE-SCOPE-004 | Calli's Cross-Branch entry recorded how she came to VTubers (pre-debut history, ADVENT-SCOPE-002 rule) | applied (clause removed) | this commit |
| CLAUDE-TOOLS-001 | The roster was hard-coded in several places (18/24/18 counts, reference-only lists) | applied: `qa_packets.COHORTS` is the single roster; release counts, START-HERE and V02 derive from it, and V02 fails when the bible and the roster differ; packets skip a rostered card that is not yet promoted | this commit |
| CLAUDE-TOOLS-002 | A draft package claimed the roster counts (19/25) while its CSVs held only the promoted cards (18/24), and shipped Bae's performance sheet without her card | applied: package counts, INDEX, CHANGELOG and START-HERE count the cards actually shipped; a sheet ships only with its card; START-HERE names what is not yet included; `CAST_ORDER`/`WORLD_ORDER` must equal the COHORTS roster (assert) | this commit |
| CLAUDE-TOOLS-003 | The quote gate matched any partial ASR row by five shared words, so a wiki quote (Cecilia's "Ew! Get away from me, you FREAK!") was flagged against an unrelated FUWAMOCO stream line | applied: a report row gates only files that cite its video (a performance sheet counts its card's citations); `span_check.py --write` regenerates `span-candidates.md` (40 → 31 rows; the 9 dropped were all unrelated-video matches) | this commit |
| CLAUDE-GUIDE-001 | The author needed one place that says where to get the data and where each file goes in Sudowrite | applied: `framework/templates/start-here-zh.md` is the package's 00-START-HERE (Chinese): download, file → Sudowrite placement, smoke test, project setup, scene habits, ElevenLabs, updates, FAQ; scene-setup states the date zone rule | this commit |
| AUDIT-MYTH1 | Cohort audit myth1 (Calli, TakaMori): 38 rows | applied except MYTH-EXPORT-001 (rejected: project label); details in research/qa/audit-myth1.md | 2026-10-03 merge |
| AUDIT-MYTH3 | Cohort audit myth3 (Kiara, Other Pairs, TakoTori): 51 rows | partly applied; MYTH-QUOTE-001 and MYTH-SCOPE-005 have residuals in snapshot fa69d71; MYTH-QUOTE-004 remains open pending quotation-gate resolution. MYTH-SCOPE-002 adapted to keep the author's public-performance shorthand; MYTH-COVERAGE-001 superseded; MYTH-VOICE-001 rejected (label) | 2026-10-03 merge |
| AUDIT-JUSTICE | Cohort audit justice: 36 rows | applied; two COVERAGE rows superseded by run F; EXPORT-001 rejected (label) | 2026-10-03 merge |
| AUDIT-GLOBAL | Cohort audit global: 60 rows | applied (including the parser fixes in tools/qa_packets.py); overlaps closed by justice and myth1 | 2026-10-03 merge |
| CLAUDE-SCOPE-003 | Merge Records naming excluded topics (15 cards) | applied (genericized) | 2026-10-03 merge |
| AUDIT-MYTH4 | Cohort audit myth4 (Ina, TakoTori): 34 rows | applied in full; this also closes the myth1/myth3 residuals that myth4 flagged | 2026-10-04 merge |
| AUDIT-MYTH2 | Cohort audit myth2 (Gura, Ame, Myth, AmeSame, Bone Bros) | applied in full, including re-raised myth3 residuals | 2026-10-04 merge |

### Registry excerpt (units and reference-only people; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "d0295ae",
 "units": [
  {
   "unit": "hololive -Myth-",
   "members": [
    "Mori Calliope",
    "Takanashi Kiara",
    "Ninomae Ina'nis",
    "Gawr Gura",
    "Watson Amelia"
   ],
   "evidence": "official"
  },
  {
   "unit": "hololive -Promise- (from 2023-10; earlier Council and Project: HOPE)",
   "members": [
    "IRyS",
    "Ouro Kronii",
    "Hakos Baelz",
    "Ceres Fauna",
    "Nanashi Mumei"
   ],
   "evidence": "official"
  },
  {
   "unit": "hololive -Advent-",
   "members": [
    "Shiori Novella",
    "Koseki Bijou",
    "Nerissa Ravencroft",
    "Fuwawa Abyssgard",
    "Mococo Abyssgard"
   ],
   "evidence": "official"
  },
  {
   "unit": "hololive -Justice-",
   "members": [
    "Elizabeth Rose Bloodflame",
    "Gigi Murin",
    "Cecilia Immergreen",
    "Raora Panthera"
   ],
   "evidence": "official"
  },
  {
   "unit": "Last Writes",
   "members": [
    "Mori Calliope",
    "Shiori Novella"
   ],
   "evidence": "official Serendipity billing, 2026"
  },
  {
   "unit": "Octo'clock",
   "members": [
    "Ninomae Ina'nis",
    "Ouro Kronii"
   ],
   "evidence": "official Serendipity billing, 2026"
  },
  {
   "unit": "Rocku Wawa",
   "members": [
    "Takanashi Kiara",
    "Koseki Bijou"
   ],
   "evidence": "official Serendipity billing, 2026"
  },
  {
   "unit": "BaeRyS",
   "members": [
    "Hakos Baelz",
    "IRyS"
   ],
   "evidence": "official Serendipity billing, 2026"
  },
  {
   "unit": "CHADCast",
   "members": [
    "Mori Calliope",
    "IRyS",
    "Hakos Baelz"
   ],
   "evidence": "official music entry (\"Here Comes the CHADCast,\" 2026)"
  },
  {
   "unit": "Bloodraven",
   "members": [
    "Nerissa Ravencroft",
    "Elizabeth Rose Bloodflame"
   ],
   "evidence": "official Serendipity billing, 2026"
  },
  {
   "unit": "B.F.F",
   "members": [
    "Fuwawa Abyssgard",
    "Mococo Abyssgard",
    "Raora Panthera"
   ],
   "evidence": "official Serendipity billing, 2026"
  },
  {
   "unit": "Autofister (also CCGG)",
   "members": [
    "Gigi Murin",
    "Cecilia Immergreen"
   ],
   "evidence": "official Serendipity billing and shop, 2026"
  },
  {
   "unit": "LYRA",
   "members": [
    "Amane Kanata",
    "Koganei Niko",
    "Mori Calliope",
    "Ayunda Risu",
    "Elizabeth Rose Bloodflame"
   ],
   "evidence": "mix engineer's credits (a remix-version cover of \"III\")"
  }
 ],
 "reference_only": [
  "Tsukumo Sana",
  "Kobo Kanaeru",
  "Vestia Zeta",
  "Kureiji Ollie",
  "Kaela Kovalskia",
  "Moona Hoshinova",
  "Ayunda Risu",
  "Anya Melfissa",
  "Pavolia Reine",
  "Airani Iofifteen",
  "Ookami Mio",
  "Tsunomaki Watame",
  "Oozora Subaru",
  "Inugami Korone",
  "Omaru Polka",
  "Momosuzu Nene",
  "Roboco",
  "Tokino Sora",
  "Yuzuki Choco",
  "Shirakami Fubuki",
  "Akai Haato",
  "Usada Pekora",
  "Shiranui Flare",
  "Amane Kanata",
  "Natsuiro Matsuri",
  "Ichijou Ririka",
  "Koganei Niko",
  "Hiodoshi Ao",
  "Machina X Flayon",
  "Jurard T Rexford",
  "Crimzon Ruze",
  "Gavis Bettel",
  "Banzoin Hakka",
  "Josuiji Shinri",
  "Arurandeisu",
  "Astel Leda",
  "Octavio",
  "Regis Altare",
  "Rikka"
 ]
}
```

### projects/holoen/research/qa/packets/events.md

# Bridge packet: events

Snapshot: git d0295ae. Every dated row from every bible file's dossier
tables (registry events), grouped by month; then each cast member's status interval. Locators are files;
search the file for the row text to see its context.

## Status intervals (from Background)

- AZKi: active; debut 2018-11-15; graduated —; regular activities concluded — (`bible/characters/AZKi.md › Background (debut: Hard Facts / Background Timeline)`)
- Cecilia Immergreen: active; debut 2024-06-22; graduated —; regular activities concluded — (`bible/characters/Cecilia-Immergreen.md › Background (debut: Background)`)
- Ceres Fauna: graduated; debut 2021-08-23; graduated 2025-01-03; regular activities concluded — (`bible/characters/Ceres-Fauna.md › Background (debut: Background)`)
- Elizabeth Rose Bloodflame: active; debut 2024-06-21; graduated —; regular activities concluded — (`bible/characters/Elizabeth-Rose-Bloodflame.md › Background (debut: Background)`)
- Fuwawa Abyssgard: active; debut 2023-07-31; graduated —; regular activities concluded — (`bible/characters/Fuwawa-Abyssgard.md › Background (debut: Background)`)
- Gawr Gura: graduated; debut 2020-09-13; graduated 2025-05-01; regular activities concluded — (`bible/characters/Gawr-Gura.md › Background (debut: Hard Facts / Background Timeline)`)
- Gigi Murin: active; debut 2024-06-21; graduated —; regular activities concluded — (`bible/characters/Gigi-Murin.md › Background (debut: Background)`)
- Hakos Baelz: active; debut 2021-08-23; graduated —; regular activities concluded — (`bible/characters/Hakos-Baelz.md › Background (debut: Background)`)
- Hakui Koyori: active; debut 2021-11-28; graduated —; regular activities concluded — (`bible/characters/Hakui-Koyori.md › Background (debut: Background)`)
- Hoshimachi Suisei: active; debut 2018-03-22; graduated —; regular activities concluded — (`bible/characters/Hoshimachi-Suisei.md › Background (debut: Background)`)
- Houshou Marine: active; debut 2019-08-11; graduated —; regular activities concluded — (`bible/characters/Houshou-Marine.md › Background (debut: Background)`)
- IRyS: active; debut 2021-07-11; graduated —; regular activities concluded — (`bible/characters/IRyS.md › Background (debut: Background)`)
- Kazama Iroha: active; debut 2021-11-30; graduated —; regular activities concluded — (`bible/characters/Kazama-Iroha.md › Background (debut: Background)`)
- Kikirara Vivi: active; debut 2024-11-09; graduated —; regular activities concluded — (`bible/characters/Kikirara-Vivi.md › Background (debut: Background)`)
- Koseki Bijou: active; debut 2023-07-30; graduated —; regular activities concluded — (`bible/characters/Koseki-Bijou.md › Background (debut: Background)`)
- La+ Darknesss: active; debut 2021-11-26; graduated —; regular activities concluded — (`bible/characters/Laplus-Darknesss.md › Background (debut: Background)`)
- Mococo Abyssgard: active; debut 2023-07-31; graduated —; regular activities concluded — (`bible/characters/Mococo-Abyssgard.md › Background (debut: Background)`)
- Mori Calliope: active; debut 2020-09-12; graduated —; regular activities concluded — (`bible/characters/Mori-Calliope.md › Background (debut: Hard Facts / Background Timeline)`)
- Nakiri Ayame: active; debut 2018-09-03; graduated —; regular activities concluded — (`bible/characters/Nakiri-Ayame.md › Background (debut: Background)`)
- Nanashi Mumei: graduated; debut 2021-08-23; graduated 2025-04-27; regular activities concluded — (`bible/characters/Nanashi-Mumei.md › Background (debut: Background)`)
- Nekomata Okayu: active; debut 2019-04-06; graduated —; regular activities concluded — (`bible/characters/Nekomata-Okayu.md › Background (debut: Background)`)
- Nerissa Ravencroft: active; debut 2023-07-31; graduated —; regular activities concluded — (`bible/characters/Nerissa-Ravencroft.md › Background (debut: Background)`)
- Ninomae Ina'nis: active; debut 2020-09-13; graduated —; regular activities concluded — (`bible/characters/Ninomae-Inanis.md › Background (debut: Hard Facts / Background Timeline)`)
- Ouro Kronii: active; debut 2021-08-23; graduated —; regular activities concluded — (`bible/characters/Ouro-Kronii.md › Background (debut: Hard Facts / Background Timeline)`)
- Raora Panthera: active; debut 2024-06-22; graduated —; regular activities concluded — (`bible/characters/Raora-Panthera.md › Background (debut: Background)`)
- Sakamata Chloe: affiliate; debut 2021-11-29; graduated —; regular activities concluded — (`bible/characters/Sakamata-Chloe.md › Background (debut: Background)`)
- Shiori Novella: active; debut 2023-07-30; graduated —; regular activities concluded — (`bible/characters/Shiori-Novella.md › Background (debut: Background)`)
- Shirogane Noel: active; debut 2019-08-08; graduated —; regular activities concluded — (`bible/characters/Shirogane-Noel.md › Background (debut: Background)`)
- Shishiro Botan: active; debut 2020-08-14; graduated —; regular activities concluded — (`bible/characters/Shishiro-Botan.md › Background (debut: Background)`)
- Takanashi Kiara: active; debut 2020-09-12; graduated —; regular activities concluded — (`bible/characters/Takanashi-Kiara.md › Background (debut: Hard Facts / Background Timeline)`)
- Takane Lui: active; debut 2021-11-27; graduated —; regular activities concluded — (`bible/characters/Takane-Lui.md › Background (debut: Background)`)
- Watson Amelia: affiliate; debut 2020-09-13; graduated —; regular activities concluded 2024-09-30 (`bible/characters/Watson-Amelia.md › Background (debut: Hard Facts / Background Timeline)`)
- Yukihana Lamy: active; debut 2020-08-12; graduated —; regular activities concluded — (`bible/characters/Yukihana-Lamy.md › Background (debut: Background)`)

## Dated rows by month

### 2017-09
- 2017-09-07 [day] Tokino Sora makes COVER's first VTuber broadcast — `bible/world/hololive-History-to-2022.md`

### 2017-12
- 2017-12-21 [day] The "hololive" app launches — `bible/world/hololive-History-to-2022.md`

### 2018-03
- 2018-03-22 [day] Debut as an independent VTuber (her birthday is the same date) — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])

### 2018-05
- 2018-05 / 06 [month-range] hololive 1st generation debuts (Fubuki, Matsuri, Haato, Aki, Mel, Chris) — `bible/world/hololive-History-to-2022.md`

### 2018-08
- 2018-08 / 09 [month-range] 2nd generation (Aqua, Shion, Ayame, Choco, Subaru); Sakura Miko debuts (2018-08-01) — `bible/world/hololive-History-to-2022.md`

### 2018-09
- 2018-09-03 [day] Debut, hololive 2nd generation (with Minato Aqua, Murasaki Shion, Yuzuki Choco, Oozora Subaru) — `bible/characters/Nakiri-Ayame.md` ([Official AY1] [Observed AY2])

### 2018-11
- 2018-11-15 [day] Debut as "Virtual Diva AZKi" — `bible/characters/AZKi.md` ([Observed AZ2; AZ3, secondary])
- 2018-11-15 [day] AZKi debuts under COVER's management — `bible/world/hololive-History-to-2022.md`

### 2018-12
- 2018-12 [month] hololive GAMERS (Fubuki, Mio; later Okayu, Korone) — `bible/world/hololive-History-to-2022.md`

### 2019
- 2019 [year] 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins — `bible/world/hololive-History-to-2022.md`

### 2019-04
- 2019-04-06 [day] Debut in hololive GAMERS (with Shirakami Fubuki, Ookami Mio, Inugami Korone) — `bible/characters/Nekomata-Okayu.md` ([Observed OK2; OK3])

### 2019-05
- 2019-05-19 [day] Joins hololive production's music label INoNaKa Music, with Hoshimachi Suisei — `bible/characters/AZKi.md` ([Observed AZ2; AZ3, secondary])
- 2019-05-19 [day] Joins INoNaKa Music, hololive production's music label, with AZKi — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2; SU3, secondary])
- 2019-05-19 [day] AZKi and Hoshimachi Suisei (formerly independent) join under the INoNaKa Music label; Suisei moves to hololive's main branch on 2019-12-01 — `bible/world/hololive-History-to-2022.md`

### 2019-06
- 2019-06 / 09 [month-range] HOLOSTARS, COVER's male group, starts (1st gen, incl. Rikka); 2nd gen in December — `bible/world/hololive-History-to-2022.md`

### 2019-08
- 2019-08-11 [day] Debut, hololive 3rd generation (hololive Fantasy) — `bible/characters/Houshou-Marine.md` ([Official MA1])
- 2019-08-08 [day] Debut, hololive 3rd generation (hololive Fantasy) — `bible/characters/Shirogane-Noel.md` ([Official NO1])

### 2019-12
- 2019-12-01 [day] Moves to the main hololive branch; later counted in "0th generation" — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2019-12 [month] 4th gen (Coco, Kanata, Watame, Towa, Luna); hololive, HOLOSTARS and INoNaKa Music unite as "hololive production" — `bible/world/hololive-History-to-2022.md`

### 2020
- 2020 [year] Constant collabs and pranks — `bible/world/AmeSame.md`
- 2020–2021 [year-range] Constant collabs, pranks and bickering — `bible/world/Bone-Bros.md`
- 2020 [year] Myth's first year: frequent collabs across time zones — `bible/world/Streaming-Life.md`
- 2020–2021 [year-range] Near-constant collabs: Minecraft, Among Us, games across time zones — `bible/world/hololive--Myth.md`

### 2020-04
- 2020-04 [month] hololive Indonesia gen 1; hololive English auditions announced — `bible/world/hololive-History-to-2022.md`

### 2020-08
- 2020-08-14 [day] Debut as a hololive 5th-generation member; her debut intro video was her own edit (secondary) — `bible/characters/Shishiro-Botan.md` ([Official BO1] [Observed BO2])
- 2020-08-12 [day] Debut, hololive 5th generation — `bible/characters/Yukihana-Lamy.md` ([Official LM1])
- 2020-08 [month] 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) — `bible/world/hololive-History-to-2022.md`

### 2020-09
- 2020-09-13 JST [day, JST] Debuts in hololive English -Myth-, 12 minutes late, first word "a"; sings city pop and becomes "City Pop Shark" — `bible/characters/Gawr-Gura.md` ([Official G1] [Observed G2 §Miscellaneous; G4])
- 2020-09-12 [day] She debuts first in hololive English -Myth-. Her fans become the Dead Beats. — `bible/characters/Mori-Calliope.md` ([Official C1] [Observed C4 §Debut])
- 2020-09-13 [day] Debuts in hololive English -Myth- — `bible/characters/Ninomae-Inanis.md` ([Official I1])
- 2020-09-12 [day] Debuts in hololive English -Myth-, speaking English, Japanese and German — `bible/characters/Takanashi-Kiara.md` ([Official T1] [Observed T2 §Debut])
- 2020-09-13 JST [day, JST] Debuts in hololive English -Myth- ("The Investigation Begins"), briefly undercover with a fake British accent — `bible/characters/Watson-Amelia.md` ([Official A1] [Observed A3-MXrFrkIlE-0; A2 §Miscellaneous])
- 2020-09-16 [day] Reveals she is a time traveler (first Fall Guys stream) — `bible/characters/Watson-Amelia.md` ([Observed A2 §Time travel; A10 locator])
- 2020-09-28 [day] "Nothing beats a ground pound" (Super Mario Odyssey) — `bible/characters/Watson-Amelia.md` ([Observed A5])
- 2020-09 [month] Kiara declares the crush on Calli's 2nd stream; "TakaMori" named — `bible/world/TakaMori.md`
- 2020-09 [month] Myth debuts with official lore profiles — `bible/world/VTuber-Persona-and-Lore.md`
- 2020-09-12/13 [day-range] Myth debuts; Calli narrates Kiara's debut intro — `bible/world/hololive--Myth.md`
- 2020-09-08 [day] hololive English announced; Myth's members appear on X — `bible/world/hololive-History-to-2022.md`
- 2020-09-12/13 [day-range] **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame — `bible/world/hololive-History-to-2022.md`
- 2020-09 [month] hololive English -Myth- debuts (first EN generation) — `bible/world/hololive.md`

### 2020-10
- 2020-10-22 [day] Gura becomes the first hololive member to reach 1 million subscribers — `bible/world/hololive-History-to-2022.md`

### 2020-11
- 2020-11-20 [day] First guest on Kiara's "HOLOTALK" — `bible/characters/Houshou-Marine.md` ([MA5 3HwaqbdKO1s])
- 2020-11 [month] HOLOTALK begins as a bilingual interview show — `bible/characters/Takanashi-Kiara.md` ([Official T9] [Observed T21])
- 2020-11-20 [day] Marine is HOLOTALK's first guest — `bible/world/JP-Senpai-Pairs-2.md`
- 2020-11-15 [day] Gura's chicken prank on KFP — `bible/world/Myth-and-Kronii-Other-Pairs.md`
- 2020-11 [month] The KFP chicken incident; Kiara "fires" Ina — `bible/world/TakoTori.md`

### 2020-12
- 2020-12 / 2021-03 [month-range] Japanese and German lessons with Kiara — `bible/characters/Gawr-Gura.md` ([Observed G13])
- 2020-12-10 [day] Channel briefly terminated, then restored; "#PhoenixDown" re-debut with a mock-amnesia bit ("Who's Calli?") — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §2020 and §Takamori; T5-le72UNZAbQI])
- 2020-12 [month] Repeated Sun Station landing attempts in Outer Wilds, later her favorite game — `bible/characters/Watson-Amelia.md` ([Observed A9; A2 §Likes and dislikes])
- 2020-12 [month] Kiara's amnesia re-debut: "Who's Calli?" — `bible/world/TakaMori.md`
- 2020-12 [month] ID gen 2 (Ollie, Anya, Reine); hololive China ends — `bible/world/hololive-History-to-2022.md`
- 2020-12-10 [day] Kiara's channel briefly terminated, then restored ("#PhoenixDown") — `bible/world/hololive-History-to-2022.md`

### 2021
- 2021 [year] Usaken Summer Festival with Ina (06-27) and an EN-server Minecraft "date" with Ina (10-20) — `bible/characters/Yukihana-Lamy.md` ([LM5])
- 2021 [year] the Usaken Summer Festival in Minecraft with Ina and EN-server "date" — `bible/world/JP-Senpai-Pairs-2.md`
- 2021–2026 [year-range] Lore grows through jokes, songs and events — `bible/world/VTuber-Persona-and-Lore.md`

### 2021-03
- 2021-03 [month] German lesson with Gura; the German "HoloDE Debüt" stream — `bible/characters/Takanashi-Kiara.md` ([Observed T15; T2 §2021])

### 2021-04
- 2021-04-17 [day] Kiara's HOLOTALK, 8th guest ("cometori") — `bible/characters/Hoshimachi-Suisei.md` ([S1 a6DjP7NYwUE])
- 2021-04-01 [day] Smol Ame appears (April Fools) — `bible/characters/Watson-Amelia.md` ([Observed A2 §Smol Ame])
- 2021-04-17 [day] HOLOTALK #8 — `bible/world/JP-Senpai-Pairs.md`

### 2021-05
- 2021-05 [month] The Fish Tank talk show with Ame — `bible/characters/Gawr-Gura.md` ([Observed G6])
- 2021-05 [month] The Fish Tank talk show with Gura — `bible/characters/Watson-Amelia.md` ([Observed Gura file G6])
- 2021-05 [month] The Fish Tank talk show — `bible/world/AmeSame.md`
- 2021-05-30 [day] Kiara reaches 1 million: every Myth member is over 1 million — `bible/world/hololive-History-to-2022.md`

### 2021-06
- 2021-06-22 [day] Original song "REFLECT" — `bible/characters/Gawr-Gura.md` ([Observed G2 §2021; G4])
- 2021-06-30 [day] Gura passes Kizuna AI as the most-subscribed VTuber — `bible/world/hololive-History-to-2022.md`

### 2021-07
- 2021-07-31 [day] Kiara's HOLOTALK, 13th guest — `bible/characters/AZKi.md` ([AZ5 CohBCNY9Pm4])
- 2021-07-11 [day] Debuts as the sole member of hololive English -Project: HOPE-, a VSinger — `bible/characters/IRyS.md` ([Official R1] [Observed R2])
- 2021-07-29 [day] First official collab: Just Shapes & Beats with Mori Calliope — `bible/characters/IRyS.md` ([Observed R2 §2021])
- 2021-07-29 [day] Calli's first collab with IRyS — `bible/world/IRyS-and-Nerissa-Pairs.md`
- 2021-07-31 [day] HOLOTALK #13 — `bible/world/JP-Senpai-Pairs.md`
- 2021-07-01 [day] Kiryu Coco graduates — `bible/world/hololive-History-to-2022.md`
- 2021-07-11 [day] **IRyS debuts** as the VSinger of Project: HOPE — `bible/world/hololive-History-to-2022.md`

### 2021-08
- 2021-08-23 JST [day, JST] Debuts with hololive English -Council- (first post on X: "oh deer") — `bible/characters/Ceres-Fauna.md` ([Official F1] [Observed F4])
- 2021-08-23 JST [day, JST] Debut, fifth and last of hololive English -Council- (08-22 PDT); she closed by singing "Fuwa Fuwa Time" — `bible/characters/Hakos-Baelz.md` ([Official HB1] [Observed HB2])
- 2021-08-23 JST [day, JST] Debuts with hololive English -Council- (first post on X: "oh man") — `bible/characters/Nanashi-Mumei.md` ([Official M1] [Observed M4])
- 2021-08 [month] The WAH acronyms begin (*Ender Lilies* streams) — `bible/characters/Ninomae-Inanis.md` ([Observed I2 §WAH])
- 2021-08-23 JST [day, JST] Debuts with hololive English -Council- — `bible/characters/Ouro-Kronii.md`
- 2021-08-23 [day] Council debuts — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2021-08-25 [day] Fauna and Mumei's first co-op — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2021-08 [month] Kronii's announcement; "a certain time lord" joke — `bible/world/Time-Duo.md`
- 2021-08 [month] -Council- debuts (Sana, Fauna, Kronii, Mumei, Bae) — `bible/world/hololive--Promise.md`
- 2021-08-23 [day] **-Council- debuts:** Sana, Fauna, **Kronii**, Mumei, Bae — `bible/world/hololive-History-to-2022.md`
- 2021-08 [month] -Council- debuts (Kronii's generation) — `bible/world/hololive.md`

### 2021-09
- 2021-09-24 [day] Keep Talking and Nobody Explodes with Takanashi Kiara, which fan references call her first official collab outside Council — `bible/characters/Hakos-Baelz.md` ([Observed HB2, secondary; HB3 579F-lu2cKY])
- 2021-09-29 [day] The Minecraft "bento" that starts the BaeRyS married/divorced bit — `bible/characters/IRyS.md` ([Observed R2 §Relationships])
- 2021-09 [month] She and Calli announce they will tone down the TakaMori ship — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §Takamori])
- 2021-09-13 [day] Minecraft together — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2021-09-24 [day] Keep Talking and Nobody Explodes — `bible/world/Hakos-Baelz-Pairs.md`
- 2021-09 [month] UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) — `bible/world/Myth-and-Kronii-Other-Pairs.md`
- 2021-09 [month] Flirt-and-rebuff routine toned down; public callbacks continued — `bible/world/TakaMori.md`
- 2021-09-23 [day] Orcs Must Die! 3: Kronii's first cross-generation collab — `bible/world/Time-and-Death.md`

### 2021-10
- 2021-10-03 [day] First single "Yoi no Yo, Yoi!" — `bible/characters/Nakiri-Ayame.md` ([Observed AY2; AY3])
- 2021-10 [month] Minecraft "civil war" with Fauna — `bible/characters/Ouro-Kronii.md` ([Unverified, K29 clip titles])
- 2021-10-31 [day] "Myth or Treat" (lyrics by Calli) — `bible/world/hololive--Myth.md`

### 2021-11
- 2021-11-28 [day] Debut, third of holoX — `bible/characters/Hakui-Koyori.md` ([Official KO1] [Observed KO2])
- 2021-11-30 [day] Debut, the fifth and last of holoX — `bible/characters/Kazama-Iroha.md` ([Official IR1] [Observed IR2])
- 2021-11-26 [day] Debut, the first holoX member to debut — `bible/characters/Laplus-Darknesss.md` ([Observed LA2])
- 2021-11-27 [day] Kiara's HOLOTALK, 18th guest (the show's first-anniversary episode) — `bible/characters/Nekomata-Okayu.md` ([OK5 FjsTGuBQlO0])
- 2021-11-29 [day] Debut, fourth of holoX; 500,000 subscribers within a week — `bible/characters/Sakamata-Chloe.md` ([Official CH1] [Observed CH2])
- 2021-11-27 [day] Debut, second of holoX; HOLOTORI membership (the wiki places Kiara's welcome beside the 11-26 reveal) — `bible/characters/Takane-Lui.md` ([Observed LU2] [Official HOLOTORI roster 2023])
- 2021-11-27 [day] HOLOTALK #18 (first anniversary) — `bible/world/JP-Senpai-Pairs.md`
- 2021-11-26 to 11-30 [day] Debut week, one member a night — `bible/world/holoX.md`
- 2021-11 [month] 6th gen "Secret Society holoX" (La+, Lui, Koyori, Chloe, Iroha) — `bible/world/hololive-History-to-2022.md`

### 2021-12
- 2021-12-27 [day] English practice with Mori Calliope — `bible/characters/Takane-Lui.md` ([LU5 i2wLH4O92-0])

### 2022
- 2022 [year] The CHADCast podcast with IRyS and Mori Calliope (Chaos, Hope and Death; episode 1 in January); the first "Febaerary"; first original song "PLAY DICE!" (02-28) — `bible/characters/Hakos-Baelz.md` ([Observed HB2; HB3 MXd7uOemEzc; Calli file C12])
- 2022 [year] "CapSule" with Mori Calliope; single "TEMPLATE / Wicked feat. Mori Calliope"; sings "Wicked" at Calli's first solo concert (07-21) — `bible/characters/Hoshimachi-Suisei.md` ([S1])
- 2022 [year] Calli's English lesson #02 with La+ and Gura (03-04); VALORANT with Ame and Kobo Kanaeru ("KoMeHa," 06-04) — `bible/characters/Kazama-Iroha.md` ([IR5])
- 2022 [year] CHADCast begins with IRyS and Hakos Baelz. — `bible/characters/Mori-Calliope.md` ([Observed C12])
- 2022 [year] First original "Jinsei Reset Button Pochii w" (02-26); EN Minecraft tour with Bae, Mumei and Lui (02-12); Calli's English lesson #04 with Lui (04-16); 3D debut (06-13) — `bible/characters/Sakamata-Chloe.md` ([Observed CH2] [CH5])
- 2022 [year] Originals "Lyrical Monster" and "Ours"; Kiara's 22nd HOLOTALK guest (03-05) — `bible/characters/Shirogane-Noel.md` ([Observed NO2] [NO5])
- 2022 [year] Calli's English lesson #04 with Chloe; an EN-server Minecraft tour with Mumei, Bae and Chloe; Minecraft with IRyS, Kronii and Kaela — `bible/characters/Takane-Lui.md` ([LU5])
- 2022 [year] CHADCast begins; "Month of Horrors" (October) — `bible/world/Hakos-Baelz-Pairs.md`
- 2022 [year] Calli's English lesson #01; HOLOTALK #22; Left 4 Dead 2 — `bible/world/JP-Senpai-Pairs-2.md`

### 2022-01
- 2022-01-17 [day] First original song "A New Start" — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2022])
- 2022-01-15 [day] Kimono reveal; introduces Boros — `bible/characters/Ouro-Kronii.md` ([Observed K8 §Mascots and fans, secondary])
- 2022-01-30 [day] First CHADCast — `bible/world/IRyS-and-Nerissa-Pairs.md`

### 2022-02
- 2022-02 [month] "Q" music video with Mori Calliope; exact MV date and time zone remain unresolved — `bible/characters/Gawr-Gura.md` ([Archive metadata G15; https://archive.ragtag.moe/watch?v=aetXqd9B8WE, checked 2026-10-04])
- 2022-02-19 [day] Calli's HOLO ENGLISH LESSON #01 with Ina and Fubuki — `bible/characters/Houshou-Marine.md` ([MA5 bfUEbp3xk4o])
- 2022-02 [month] Nintendo Direct "TOMORROW?!" reaction — `bible/characters/Ninomae-Inanis.md` ([Observed I23])
- 2022-02 [month] "Q" music video; exact MV date and time zone remain unresolved — `bible/world/Bone-Bros.md`
- 2022-02-25 [day] Ame's surprise karaoke off-collab (with Ina, Kronii, Fauna, Mumei) — `bible/world/OctoClock.md`
- 2022-02-24 [day] Uruha Rushia leaves hololive — `bible/world/hololive-History-to-2022.md`

### 2022-03
- 2022-03-12 [day] Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame — `bible/characters/AZKi.md` ([AZ5 32NVpmKdAOs])
- 2022-03-04 [day] Calli's "HOLO ENGLISH LESSON #02" with Gura and Iroha — `bible/characters/Laplus-Darknesss.md` ([LA5 X492n37brRU])
- 2022-03-12 [day] HOLO ENGLISH LESSON #03 — `bible/world/JP-Senpai-Pairs.md`
- 2022-03-04 / 04-16 [day-range] Calli's English lessons #02 and #04 — `bible/world/holoX.md`
- 2022-03 [month] ID gen 3 (Zeta, Kaela, Kobo) — `bible/world/hololive-History-to-2022.md`
- 2022-03-20 [day] hololive 3rd fes. "Link Your Wish" at Makuhari (#つながるホロライブ), day 2: Calli and Kiara perform — `bible/world/hololive-History-to-2022.md`
- 2022-03-19 [day] HOLOSTARS announces the unit UPROAR!! — `bible/world/hololive-History-to-2022.md`

### 2022-04
- 2022-04 [month] Transfers from INoNaKa Music to hololive's main group ("0th generation") — `bible/characters/AZKi.md` ([Observed AZ2; AZ3, secondary historical reference])
- 2022-04 [month] She signs with EMI Records / Universal Music Japan. — `bible/characters/Mori-Calliope.md` ([Observed C4 §2022, secondary])
- 2022-04-24 [day] Left 4 Dead 2 with IRyS, Takane Lui and Inugami Korone — `bible/characters/Shishiro-Botan.md` ([BO5 K1wStJxm4F0])
- 2022-04 [month] "CapSule"; "TEMPLATE / Wicked feat. Mori Calliope" — `bible/world/JP-Senpai-Pairs.md`
- 2022-04-26 [day] holoMeet begins; Gura is an ambassador — `bible/world/hololive-History-to-2022.md`

### 2022-05
- 2022-05-14 [day] First original song "Let Me Stay Here" — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2022])

### 2022-06
- 2022-06-16 [day] First original song "WAO!!" (official music page); the wiki also dates her 3D debut here (not verified in review) — `bible/characters/Hakui-Koyori.md` ([Official music page] [Observed KO2])
- 2022-06 [month] An off-collab; unarchived karaoke — `bible/world/AmeSame.md`
- 2022-06 [month] Myth's first off-collab with all five present — `bible/world/Streaming-Life.md`
- 2022-06 [month] "Reunion & Gaming!! #takamori" off-collab; karaoke collab — `bible/world/TakaMori.md`
- 2022-06-28 [day] First off-collab with all five together ("Together At Last") — `bible/world/hololive--Myth.md`

### 2022-07
- 2022-07-21 [day] Her solo concert "New Underworld Order." — `bible/characters/Mori-Calliope.md` ([Official C6])
- 2022-07-21 [day] "Wicked" at New Underworld Order — `bible/world/JP-Senpai-Pairs.md`
- 2022-07-31 [day] Sana graduates — `bible/world/hololive--Promise.md`
- 2022-07-18/23 [day-range] HOLOSTARS English -TEMPUS- (Regis Altare, Magni Dezmond, Axel Syrios, Noir Vesper) announced and debuts — `bible/world/hololive-History-to-2022.md`
- 2022-07-31 [day] Tsukumo Sana graduates — `bible/world/hololive-History-to-2022.md`

### 2022-08
- 2022-08-23 [day] Council's first group original song "Rise" — `bible/characters/Hakos-Baelz.md` ([Observed HB2])
- 2022-08 [month] Mumei accidentally blows up the Bunkeronii's entrance — `bible/characters/Ouro-Kronii.md` ([Unverified, K28 clip titles])

### 2022-09
- 2022-09-30 [day] First solo concert "Poison-nya Syndrome" — `bible/characters/Nekomata-Okayu.md` ([Observed OK3])
- 2022-09-30 [day] "Non-Fiction" MV — `bible/world/hololive--Myth.md`
- 2022-09 [month] hololive's 5th anniversary — `bible/world/hololive-History-to-2022.md`

### 2022-10
- 2022-10 [month] "BAE & FAUNA'S MONTH OF HORRORS" — `bible/characters/Ceres-Fauna.md` ([Observed F4, F3])
- 2022-10 [month] "BAE & FAUNA'S MONTH OF HORRORS" (Amnesia: The Dark Descent on Fauna's channel) — `bible/characters/Hakos-Baelz.md` ([Observed HB2, secondary; HB8 DaG38dShdGE])
- 2022-10-09 [day] Kiara's HOLOTALK, 23rd guest (season 2 opener) — `bible/characters/Nakiri-Ayame.md` ([AY5 h1EaCnoKhwk])
- 2022-10-09 [day] HOLOTALK #23 — `bible/world/JP-Senpai-Pairs.md`

### 2022-12
- 2022-12-31 [day] "story time" as Star Flower with Suisei, Moona Hoshinova and IRyS — `bible/characters/AZKi.md` ([Official AZ6])
- 2022-12-31 [day] "story time" as Star Flower with AZKi, Moona Hoshinova and IRyS — `bible/characters/Hoshimachi-Suisei.md` ([Official SU6])
- 2022-12-31 [day] "story time" — `bible/world/JP-Senpai-Pairs.md`

### 2023
- 2023 [year] "Blue Journey" with Marine, Noel, Lamy, Botan, Lui and Sakura Miko (07-08; official roster); 1 million subscribers (09-24, secondary); Hoshimatic Project (from 11, secondary) — `bible/characters/Hakui-Koyori.md` ([Blue Journey roster] [Observed KO2])
- 2023 [year] AzuIro: GeoGuessr on a "Kazama map" AZKi made, covers and a first off-collab (08); Puyo Puyo Tetris coaching from Suisei (04); Hoshimatic Project (11-) — `bible/characters/Kazama-Iroha.md` ([IR4] [Observed IR2])
- 2023 [year] "Kawayo"; a guest artist at the Pretty Cure virtual music event (12-09); the hololive Sports Festival white team wins (with Kiara, Mumei, Ame, Nerissa, AZKi) — `bible/characters/Nakiri-Ayame.md` ([Observed AY2; AY3; AY4 tHP7bd8Jtm0])
- 2023 [year] 1 million subscribers (02-18, secondary); HOLOYOI #01 with Calli and Lui (03-23); "BAE-GEMITE DOMINATION" (04-29); a cover with Bae (10-30); the original Hoshimatic Project lineup (11-, secondary roster reference) — `bible/characters/Sakamata-Chloe.md` ([Observed CH2] [CH5 UuL_nORzfNM, z4-5Hq5AKG4, 9EAIDwXj4Jk])
- 2023 [year] Calli's HOLOYOI #02 with Flare (04-20); first solo album "NOESANPO" (official digital release 11-25; birthday merchandise orders opened 11-24); a "Yuru Holo" team Mario Kart event with FUWAMOCO and Bae among the participants (12-12) — `bible/characters/Shirogane-Noel.md` ([NO5] [Official music 359])
- 2023 [year] BAE-GEMITE DOMINATION #2 with Bae and Subaru (04-08); HOLOYOI #03 with Calli and Subaru (05-18); an Overwatch 2 team with IRyS, Lui, Chloe and Towa (08) — `bible/characters/Shishiro-Botan.md` ([BO5])
- 2023 [year] HOLOYOI ep. 1 with Chloe (Calli's show, 03-23); a Wario off-collab with Kiara (01-15); BAE-GEMITE #5 with Bae and Chloe (04-29); "TWIN DAY WITH LUI" with FUWAMOCO (11-25); Blue Journey (official roster) — `bible/characters/Takane-Lui.md` ([LU5 UuL_nORzfNM, cVJefDjefUs, z4-5Hq5AKG4, MbqO5OPuT80] [Blue Journey roster])
- 2023 [year] "Blue Journey" music project with Marine, Noel, Koyori and Sakura Miko — `bible/characters/Yukihana-Lamy.md` ([Koyori file; Observed LM2])
- 2023 [year] a BaeRyS off-collab; "Daikirai na Hazu Datta"; K/DA "POP/STARS"; We Were Here — `bible/world/Hakos-Baelz-Pairs.md`
- 2023 [year] HOLOYOI #02 and #03; BAE-GEMITE DOMINATION #2; the horror game featuring Marine; Overwatch 2 team; Blue Journey — `bible/world/JP-Senpai-Pairs-2.md`
- 2023–2024 [year-range] FGO streams on Ina's channel — `bible/world/OctoClock.md`
- 2023 [year] Off-collabs; "Fire N Ice" duet (2023-12-14) — `bible/world/TakaMori.md`
- 2023 [year] Frequent horror and TTRPG co-ops; "Time and Death Say Howdy to Ghosts" — `bible/world/Time-and-Death.md`
- 2023 [year] HOLOYOI ep. 1 (Lui, Chloe); BAE-GEMITE episodes; Kiara's off-collabs with Lui and La+ — `bible/world/holoX.md`

### 2023-01
- 2023-01-20 [day] First VTuber on THE FIRST TAKE ("Stellar Stellar") — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2; SU3, secondary])
- 2023-01-19 [day] ChikuTaku song on sale — `bible/characters/Watson-Amelia.md` ([Official A13b])
- 2023-01-24 [day] ChikuTaku game released (concept and shared project management, with a credited team) — `bible/characters/Watson-Amelia.md` ([Official A13])

### 2023-03
- 2023-03-09 [day] GeoGuessr with Hakos Baelz — `bible/characters/AZKi.md` ([AZ5 T594r3CnuW8])
- 2023-03-19 [day] 3D idol costume at hololive 4th fes. (day 2) — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2023])
- 2023-03-19 [day] 3D debut at hololive 4th fes. "Our Bright Parade"; her own 3D debut stream 2023-09-30 — `bible/characters/Hakos-Baelz.md` ([Observed HB2])
- 2023-03-18/19 [day-range] 3D idol costume and main 3D model at hololive 4th fes.; sang a DECO*27 song with Kiara on the holo*27 stage — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2023; M4])
- 2023-03-19 [day] Mumei sings with Kiara on the 4th fes. stage — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2023-03-18/19 [day-range] hololive SUPER EXPO 2023 and 4th fes. "Our Bright Parade" — `bible/world/hololive-History-2023-2026.md`
- 2023-03-28 [day] The fan app "holoplus" is introduced — `bible/world/hololive-History-2023-2026.md`

### 2023-04
- 2023-04-22 [day] "BAE-GEMITE DOMINATION" episode 4 with Bae and Momosuzu Nene — `bible/characters/Hakui-Koyori.md` ([KO5 WwjB7QSmQng])
- 2023-04-08 [day] 5D Chess ("I Don't Understand") — `bible/world/Time-Duo.md`
- 2023-04 [month] holoMeet 2023 ambassadors include IRyS — `bible/world/hololive-History-2023-2026.md`

### 2023-06
- 2023-06-30 [day] Nostalgic games with a handcam, an off-collab on Kiara's channel (archived title and description) — `bible/characters/Laplus-Darknesss.md` ([LA5 XWf2PqD_8zQ])

### 2023-07
- 2023-07-02 [day] hololive English 1st concert "-Connect the World-" — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2023])
- 2023-07-31 JST [day, JST] Debuts with Mococo as FUWAMOCO in hololive English -Advent- — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW1])
- 2023-07-02 [day] hololive English 1st concert "-Connect the World-"; EP "Pandæmonium" (07-07) — `bible/characters/Hakos-Baelz.md` ([Observed HB2])
- 2023-07-30 JST [day, JST] Debuts with hololive English -Advent- ("Moai Moai Kyun~!") — `bible/characters/Koseki-Bijou.md` ([Official KB1] [Observed KB3])
- 2023-07-31 JST [day, JST] Debuts with Fuwawa as FUWAMOCO — `bible/characters/Mococo-Abyssgard.md` ([Official MC1])
- 2023-07-31 [day] FUWAMOCO MORNING pilot — `bible/characters/Mococo-Abyssgard.md` ([Observed MC2])
- 2023-07-31 [day] Debuts with hololive English -Advent- — `bible/characters/Nerissa-Ravencroft.md` ([Official N1])
- 2023-07-30 JST [day, JST] Debuts with hololive English -Advent- ("Shiori~n!") — `bible/characters/Shiori-Novella.md` ([Official SN1])
- 2023-07-25 [day] "WANTED!" PV reveals the five — `bible/world/Advent-Pairs.md`
- 2023-07-29/30 PDT [day-range, PDT] Debuts (Shiori, Bijou, Nerissa, FUWAMOCO) — `bible/world/Advent-Pairs.md`
- 2023-07-31 JST [day, JST] Debut ("who let the dogs out?!") and FUWAMOCO MORNING pilot — `bible/world/FUWAMOCO.md`
- 2023-07-25 [day] "WANTED!" debut PV reveals the five — `bible/world/hololive--Advent.md`
- 2023-07 (end) [month] Debuts; Nerissa's on 2023-07-31 (JST) — `bible/world/hololive--Advent.md`
- 2023-07-02 PDT [day, PDT] hololive English 1st concert "-Connect the World-" — `bible/world/hololive-History-2023-2026.md`
- 2023-07-25/31 [day-range] **-Advent- revealed ("WANTED!") and debuts**: Shiori, Bijou, **Nerissa**, Fuwawa, Mococo — `bible/world/hololive-History-2023-2026.md`

### 2023-08
- 2023-08 [month] The horror game "Truth of Beauty Witch -Marine's treasure ship-" features her (Calli played it 08-14; Bae with Mumei 08-23); an off-collab house party with Calli and Bae (08-14) — `bible/characters/Houshou-Marine.md` ([Observed MA2 §Events] [MA5 Mf-sAjsuSig, RY1GkF4jMls, DY5VThfehW8])
- 2023-08-12 [day] An Undertale mod starring Calli, played with Calli on stream — `bible/characters/Koseki-Bijou.md` ([Observed KB3])
- 2023-08-12 [day] Advent on Kiara's HOLOTALK — `bible/characters/Shiori-Novella.md` ([Observed SN3; Kiara archive])
- 2023-08-12 [day] HOLOTALK with Kiara; Bijou's Undertale replay with Calli — `bible/world/Advent-Pairs.md`
- 2023-08-14 [day] Nerissa's compatibility test with Kiara — `bible/world/IRyS-and-Nerissa-Pairs.md`
- 2023-08-12 [day] Advent are Kiara's 29th HOLOTALK guests — `bible/world/hololive--Advent.md`

### 2023-09
- 2023-09-13 [day] 3rd anniversary relay (#Myth3YearRelay), e.g. a homemade Family Feud with all five — `bible/world/hololive--Myth.md`
- 2023-09-09/10 [day-range] hololive DEV_IS opens with ReGLOSS (Ao, Kanade, Ririka, Raden, Hajime) — `bible/world/hololive-History-2023-2026.md`

### 2023-10
- 2023-10-04 [day] Major debut (Victor Entertainment, until 2025); SorAZ with Tokino Sora debuts 2023-12-20 — `bible/characters/AZKi.md` ([Observed AZ2; AZ3])
- 2023-10-09 [day] Joins hololive English -Promise- — `bible/characters/Ceres-Fauna.md` ([Official])
- 2023-10-09 JST [day, JST] hololive English -Promise- formed with IRyS, Fauna, Kronii and Mumei — `bible/characters/Hakos-Baelz.md` ([Observed HB2; Promise card])
- 2023-10-09 [day] Joins hololive English -Promise- with Fauna, Kronii, Mumei and Bae — `bible/characters/IRyS.md` ([Observed R2 §2023])
- 2023-10-09 [day] Joins hololive English -Promise- — `bible/characters/Nanashi-Mumei.md` ([Official])
- 2023-10-10 [day] Second original song "mumei" — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2023])
- 2023-10-09 [day] Joins hololive English -Promise- alongside IRyS, Ceres Fauna, Nanashi Mumei and Hakos Baelz — `bible/characters/Ouro-Kronii.md` ([Official K3])
- 2023-10-09 [day] -Promise- formed — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2023-10-09 JST [day, JST] -Promise- formed — `bible/world/Hakos-Baelz-Pairs.md`
- 2023-10-09 [day] -Promise- formed: IRyS and Kronii become unitmates — `bible/world/IRyS-and-Nerissa-Pairs.md`
- 2023-10-08 PDT / 10-09 JST [day-range, PDT] -Promise- formed with IRyS (closing Project: HOPE) — `bible/world/hololive--Promise.md`
- 2023-10-08/09 [day-range] "CouncilRyS" 3D showcase; **-Promise- formed** (IRyS joins the Council) — `bible/world/hololive-History-2023-2026.md`
- 2023-10-09 [day] -Promise- formed (IRyS joins the remaining Council) — `bible/world/hololive.md`

### 2023-11
- 2023-11 [month] Starts "Hoshimatic Project" — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2023-11 [month] Sports Festival, white team wins — `bible/world/JP-Senpai-Pairs.md`

### 2023-12
- 2023-12 [month] VTuber Awards: "League of Their Own" (as FUWAMOCO) — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §Awards])
- 2023-12-28 [day] "HIDE & SEEK 〜Nakayoku Kenkashina〜," an original song with Usada Pekora — `bible/characters/Hakos-Baelz.md` ([Official HB9])
- 2023-12-12 [day] Team Mario Kart with Hakos Baelz and FUWAMOCO among others — `bible/characters/Nekomata-Okayu.md` ([OK5 Janl2FCKmsg])
- 2023-12 [month] VTuber Awards: "League of Their Own" — `bible/world/FUWAMOCO.md`

### 2024
- 2024–2025 [year-range] World Tour '24 -Soar!- performer (New York to Taipei; "Ai ni" with Kobo Kanaeru at the Taipei finale, 2025-01-18); holoMeet ambassador 2024; World Tour '25 Sydney show with Kronii and IRyS ("Dance Monkey" as Promise, 2025-07-12) — `bible/characters/Hakos-Baelz.md` ([Official HB6, HB10] [Observed Concerts card])
- 2024 [year] Lethal Company with FUWAMOCO and Fubuki (03-09); FUWAMOCO Morning episode 90 guest, billed #FUWAMOKOYO (04-26); a guest at Mumei's first 3D live (08-05) — `bible/characters/Hakui-Koyori.md` ([KO5 XR1PEtj15kE, gCYXKgYcFmk, gl7CwlEg2ZI])
- 2024 [year] 3 million subscribers (01-10, secondary); album "Ahoy!! You're All Pirates♡!" (10-16); a Touhou off-collab with FUWAMOCO (04-30) and Mario Party with FUWAMOCO and Nerissa; a solo concert (12); a guest at Ina's "Pleides" (12-28) — `bible/characters/Houshou-Marine.md` ([Observed MA2] [MA5 x7gRHgQ0yI0, FLL7e1-RPGo, 3n9igJnSXtQ])
- 2024 [year] Covers with La+ (「絶対敵対メチャキライヤー」, 03-11) and Lui (「右肩の蝶」, 04-11); originals "Mahou Shoujo☆Magical GOZARU" and "Dreamy Sky" (06); a cookie-battle off-collab on her channel, presented with AZKi, with FUWAMOCO as the challengers (10-27, JgOwJ7m89Lk); a guest at Kiara's 4th-anniversary live (10-06); 1 million subscribers (11-19) — `bible/characters/Kazama-Iroha.md` ([Observed IR2] [IR4] [IR5])
- 2024 [year] "drop candy" (05-25); holoGTA participant (her archive establishes participation; other members' own archives place them in the same event) — `bible/characters/Laplus-Darknesss.md` ([Observed LA2] [LA4 swqXHi1Z4ew])
- 2024 [year] "melting"; "Chief VTuber Officer" for Maxell Izumi (12-02) — `bible/characters/Nakiri-Ayame.md` ([Observed AY2; AY3])
- 2024 [year] Guest at Nanashi Mumei's 3D live "Outside the Box"; first GAMERS fes (Yoyogi) — `bible/characters/Nekomata-Okayu.md` ([Mumei file] [Observed OK3])
- 2024 [year] MECONOPSIS and TEMARI; she discusses MECONOPSIS's conflict between duty and protecting others — `bible/characters/Ninomae-Inanis.md` ([Official I1 music list] [Observed—published interview I7b])
- 2024 [year] "Magical Girl holoWitches!" single (05-30); "Kanaken" 3D live with Kanata and AZKi — `bible/characters/Sakamata-Chloe.md` ([Observed CH2] [CH4])
- 2024 [year] First album "Liberty" (official digital release 06-12); 1 million subscribers (11-16, secondary) — `bible/characters/Takane-Lui.md` ([Official music 434] [Observed LU2])
- 2024 [year] Originals "Hatsukoi Pâtissière," "Watashi wo amayakasunara" and "Lamy's Baribari Workout"; a guest at Ina's 3D live "Pleides" (12-28) — `bible/characters/Yukihana-Lamy.md` ([Observed LM2] [LM5])
- 2024 [year] Off-collabs with FUWAMOCO and Nerissa; Ina's "Pleides" — `bible/world/JP-Senpai-Pairs-2.md`
- 2024 [year] FUWAMOKOYO; holoX "Drokei" escape event — `bible/world/holoX.md`

### 2024-01
- 2024-01-26 [day] 1,000,000 subscribers, the first of Council/Promise — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2024])
- 2024-01-16 [day] Yozora Mel leaves hololive — `bible/world/hololive-History-2023-2026.md`

### 2024-02
- 2024-02-09 [day] A FUWAMOCO-themed GeoGuessr map with the twins ("FWMCAZ") — `bible/characters/AZKi.md` ([AZ4 Lk7Rlt-MVB4, archived metadata])
- 2024-02-29 [day] Original "RxRxR" and first album "ZODIAC" — `bible/characters/Hakos-Baelz.md` ([Observed HB2])
- 2024-02-09 [day] GeoGuessr FUWAMOCO map — `bible/world/JP-Senpai-Pairs.md`

### 2024-03
- 2024-03-04 [day] "TAKOTORI OFFCOLLAB!!" — `bible/world/TakoTori.md`
- 2024-03-16/17 [day-range] SUPER EXPO 2024 and 5th fes. "Capture the Moment" — `bible/world/hololive-History-2023-2026.md`

### 2024-04
- 2024-04-27 [day] First original song "Say My Name" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2024])
- 2024-04-01 [day] A "furball lion" model designed by Shirakami Fubuki — `bible/characters/Shishiro-Botan.md` ([Observed BO2])
- 2024-04 [month] holoMeet 2024 ambassadors include Hakos Baelz — `bible/world/hololive-History-2023-2026.md`

### 2024-06
- 2024-06-22 PDT [day, PDT] Debut ("It's wind-up time!!"), with a chat-controlled game (implemented by nullrefrepro per the credits; Raora drew the ending screen and sweeping art) and a violin performance; official profile lists June 23 (JST) — `bible/characters/Cecilia-Immergreen.md` ([Official CI1] [Observed CI3])
- 2024-06-21 PDT [day, PDT] Debut ("Ello Ello Ello~!"), first of Justice; official profile lists June 22 (JST) — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB1] [Observed EB3])
- 2024-06-21 PDT [day, PDT] Debut ("GG STANDS FOR GIGI!"), second of Justice; official profile lists June 22 (JST) — `bible/characters/Gigi-Murin.md` ([Official GG1] [Observed GG3])
- 2024-06-22 PDT [day, PDT] Debut ("I've got my eyes on you 🐱 mamma mia"), last of Justice; official profile lists June 23 (JST) — `bible/characters/Raora-Panthera.md` ([Official RP1] [Observed RP3])
- 2024-06-26 [day] An early Raora–Elizabeth duo collab, "Chat & Art w/ Liz!" — `bible/world/Justice-Pairs.md`
- 2024-06-18 [day] Announcement video "The Mission Begins!" — `bible/world/hololive--Justice.md`
- 2024-06-21/22 PDT [day-range, PDT] Debuts: Elizabeth (06-21 8 PM), Gigi (06-21 8:45 PM), Cecilia (06-22 8 PM), Raora (06-22 8:45 PM); official profiles list June 22/23 (JST) — `bible/world/hololive--Justice.md`
- 2024-06–07 [month-range] Content Warning, Chained Together, Left 4 Dead 2, a Justice Minecraft server and "Justice HQ" — `bible/world/hololive--Justice.md`
- 2024-06 [month] Myth One-Block Minecraft series — `bible/world/hololive--Myth.md`
- 2024-06-21/22 PDT [day-range, PDT] **-Justice- debuts**: Elizabeth Rose Bloodflame, Gigi Murin, Cecilia Immergreen, Raora Panthera ("law enforcers" chasing Advent) — `bible/world/hololive-History-2023-2026.md`

### 2024-07
- 2024-07-31 [day] First original song "Born to be 'BAU'DOL☆★" — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2024])
- 2024-07-05 [day] hololive night at Dodger Stadium with Usada Pekora and Gawr Gura — `bible/characters/Hoshimachi-Suisei.md` ([Official SU7])
- 2024-07-31 [day] First original song "Born to be 'BAU'DOL☆★" — `bible/world/FUWAMOCO.md`
- 2024-07-05 [day] hololive night at Dodger Stadium — `bible/world/JP-Senpai-Pairs.md`
- 2024-07-03 [day] Cecilia and Raora's Minecraft duo — `bible/world/Justice-Pairs.md`
- 2024-07-19 [day] Cecilia shows Elizabeth around Minecraft — `bible/world/Justice-Pairs.md`
- 2024-07-21/22 [day-range] Advent VS Justice, Party Animals — `bible/world/Justice-Pairs.md`
- 2024-07-21/22 [day-range] "Advent VS Justice" in Party Animals — `bible/world/hololive--Justice.md`

### 2024-08
- 2024-08-13 [day] Singing collab with Minato Aqua and FUWAMOCO — `bible/characters/AZKi.md` ([AZ4 _VnNO5TMkBM])
- 2024-08-24/25 [day-range] hololive English 2nd concert -Breaking Dimensions-: premieres "It's Not a Phase" with Mumei and sings "Mayonaka no Door" solo (day 1); "Lonely in Gorgeous" with Shiori and Nerissa (day 2) — `bible/characters/Ceres-Fauna.md` ([Official F5])
- 2024-08-10 PDT [day, PDT] 3D debut with a wrestling segment and cameos by Okayu and Korone — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2024])
- 2024-08-24/25 [day-range] -Breaking Dimensions-: "Our Promise" with Promise; "BLUE CLAPPER" with Calli, IRyS and Koseki Bijou; solo "GEKIRIN"; "High Tide" with IRyS, Moona Hoshinova and Hoshimachi Suisei — `bible/characters/Hakos-Baelz.md` ([Official HB5])
- 2024-08-02 [day] Introduces herself as a "virtual idol"; profile drops "forever 18" — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2024-08-24/25 [day-range] "High Tide" with IRyS, Moona and Hakos Baelz, and "BIBBIDIBA" with Moona, Ina and Gura, at the English concert -Breaking Dimensions- — `bible/characters/Hoshimachi-Suisei.md` ([Official SU8])
- 2024-08-03 PDT [day, PDT] 3D debut; first performs "Prism no Mahou" ("Prism Magic") — `bible/characters/Koseki-Bijou.md` ([Observed KB2 §2024] [Official KB7])
- 2024-08-17 PDT [day, PDT] Advent's 3D collaboration stream — `bible/characters/Koseki-Bijou.md` ([Official KB7])
- 2024-08-11 [day] #BAEBISleepOver with Hakos Baelz — `bible/characters/Koseki-Bijou.md` ([Observed KB3])
- 2024-08-10 PDT [day, PDT] 3D debut — `bible/characters/Mococo-Abyssgard.md` ([Observed MC2 §2024])
- 2024-08-05 [day] 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori — `bible/characters/Nanashi-Mumei.md` ([Observed M3 title, description])
- 2024-08-24 [day] -Breaking Dimensions- day 1: premieres "It's Not a Phase" with Fauna; "Beyond the way" with Kiara and Nerissa; day 2: her original "A New Start" — `bible/characters/Nanashi-Mumei.md` ([Official M5])
- 2024-08-10 PDT [day, PDT] Cameo with Inugami Korone at FUWAMOCO's 3D debut — `bible/characters/Nekomata-Okayu.md` ([FUWAMOCO card])
- 2024-08-09 PDT [day, PDT] 3D debut; the "Demon of Soup" soup — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2])
- 2024-08-08 [day] First EP "In My Feelings" — `bible/characters/Nerissa-Ravencroft.md` ([Official N22])
- 2024-08-02 PDT [day, PDT] 3D debut "A New Chapter Begins!" with Nerissa, Bijou and FUWAMOCO as guests — `bible/characters/Shiori-Novella.md` ([Observed SN3 tIKQMFtbgOA])
- 2024-08-25 [day] -Breaking Dimensions-: "Lonely in Gorgeous" with Fauna and Nerissa — `bible/characters/Shiori-Novella.md` ([Official, Concerts card S8])
- 2024-08-02 → 08-10 PDT [day, PDT] 3D debuts (Shiori 08-02, Bijou 08-03, Nerissa 08-09, FUWAMOCO 08-10; JST dates are one day later) — `bible/world/Advent-Pairs.md`
- 2024-08-17 PDT [day, PDT] Advent's 3D collaboration stream — `bible/world/Advent-Pairs.md` ([Official S9])
- 2024-08-10 PDT [day, PDT] 3D debut: a wrestling segment supervised by DDT Pro-Wrestling, Okayu and Korone cameos — `bible/world/FUWAMOCO.md`
- 2024-08-24 [day] "It's Not a Phase" premiered at -Breaking Dimensions- — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2024-08-11/12 [day-range] #BAEBISleepover — `bible/world/Hakos-Baelz-Pairs.md`
- 2024-08-24/25 [day-range] -Breaking Dimensions-: "Our Promise," "BLUE CLAPPER," "High Tide" — `bible/world/Hakos-Baelz-Pairs.md`
- 2024-08-10 PDT [day, PDT] FUWAMOCO's 3D debut, Okayu and Korone cameos — `bible/world/JP-Senpai-Pairs.md`
- 2024-08-24/25 [day-range] "High Tide" at -Breaking Dimensions- — `bible/world/JP-Senpai-Pairs.md`
- 2024-08-02/10 PDT [day-range, PDT] 3D debuts: Shiori 08-02, Bijou 08-03, Nerissa 08-09, FUWAMOCO 08-10 (JST one day later) — `bible/world/hololive--Advent.md`
- 2024-08-17 PDT [day, PDT] Advent's 3D collaboration stream — `bible/world/hololive--Advent.md`
- 2024-08-02/10 PDT [day-range, PDT] Advent 3D debuts (JST dates one day later): Shiori (08-02), Bijou (08-03), Nerissa (08-09), FUWAMOCO (08-10, with Okayu and Korone cameos) — `bible/world/hololive-History-2023-2026.md`
- 2024-08-23 [day] "ENigmatic Recollection" (ENReco) announced: EN members in the fantasy world Libestal, via a Minecraft series, animation and songs — `bible/world/hololive-History-2023-2026.md`
- 2024-08-23 EDT [day, EDT] World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 — `bible/world/hololive-History-2023-2026.md`
- 2024-08-24/25 EDT [day-range, EDT] EN 2nd concert "-Breaking Dimensions-" (Kings Theatre, New York), a separate event — `bible/world/hololive-History-2023-2026.md`
- 2024-08-28 [day] Minato Aqua graduates — `bible/world/hololive-History-2023-2026.md`

### 2024-09
- 2024-09 [month] "2.0" model update — `bible/characters/Gawr-Gura.md` ([Observed G3])
- 2024-09-21 [day] Sings "September" 120 times in an eight-hour unarchived karaoke — `bible/characters/Gigi-Murin.md` ([Observed GG2, secondary])
- 2024-09-05 [day] Tutu, a cat, is added to her model as a toggle. — `bible/characters/Mori-Calliope.md` ([Observed C4 §Mascot and fans, secondary])
- 2024-09-15 [day] A pop-up Mario Party with Mori Calliope, Anya Melfissa and Hiodoshi Ao (archived metadata) — `bible/characters/Nekomata-Okayu.md` ([OK4 WnKCmQ2iXww])
- 2024-09-30 [day] Concludes regular activities; remains a hololive affiliate — `bible/characters/Watson-Amelia.md` ([Official A4])
- 2024-09-29 [day] "Looking at our old DMs" — `bible/world/AmeSame.md`
- 2024-09 [month] Calli performs Gura's "Full Color" at Myth's 4th-anniversary concert "The Show Goes On!" — `bible/world/Bone-Bros.md`
- 2024-09-22 [day] Ame on HOLOTALK — `bible/world/Myth-and-Kronii-Other-Pairs.md`
- 2024-09 [month] Backrooms and DRG in Ame's last week — `bible/world/Time-Duo.md`
- 2024-09-22 [day] Escape the Backrooms with Ame — `bible/world/Time-and-Death.md`
- 2024-09 [month] 4th anniversary song and voice pack; Ame's last week includes a Myth collab — `bible/world/hololive--Myth.md`
- 2024-09-30 [day] **Watson Amelia concludes regular activities and stays an affiliate** — `bible/world/hololive-History-2023-2026.md`
- 2024-09-30 [day] Watson Amelia concludes general activities, stays an affiliate — `bible/world/hololive.md`

### 2024-10
- 2024-10-12 [day] FUWAMOCO reach 1,000,000 subscribers, first in Advent — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2024])
- 2024-10-06 / 10-08 [day-range] "Prism no Mahou" music video (10-06) and release (10-08) — `bible/characters/Koseki-Bijou.md` ([Observed KB2 §2024] [Official KB8])
- 2024-10-12 [day] 1,000,000 subscribers, first in Advent — `bible/world/FUWAMOCO.md`
- 2024-10-31/11-01 [day-range] "Justice's Haunted VR Investigation" in VRChat, with Advent visitors; chibi 3D models — `bible/world/hololive--Justice.md`
- 2024-10-12 [day] FUWAMOCO reach 1,000,000 subscribers, first in Advent; VTuber of the Year at the VTuber Awards (2024-12) — `bible/world/hololive-History-2023-2026.md`

### 2024-11
- 2024-11-25 [day] "#BaeTV24" 24-hour stream with collabs (IRyS and Raora; Kronii, Bijou and Gigi) — `bible/characters/Hakos-Baelz.md` ([Observed HB3])
- 2024-11 to 12 [month] First live tour "Spectra of Nova" (Saitama, Osaka, Fukuoka); Calli, FUWAMOCO and Elizabeth hold a watch party — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2] [S1 YtVleZxIiNc])
- 2024-11-17 [day] 3D live "The Devil Wears Hope" — `bible/characters/IRyS.md` ([Observed R3 title])
- 2024-11-09 [day] Debut with FLOW GLOW, through hololive DEV_IS; first cover "Luna say maybe" — `bible/characters/Kikirara-Vivi.md` ([Official VI1] [Observed VI2])
- 2024-11-29 [day] Conclusion of regular activities announced; she stays an affiliate — `bible/characters/Sakamata-Chloe.md` ([Observed CH2])
- 2024-11-25 [day] #BaeTV24 24-hour stream — `bible/world/Hakos-Baelz-Pairs.md`
- 2024-11-14 [day] "Spectra of Nova" watch party — `bible/world/JP-Senpai-Pairs.md`
- 2024-11-09 [day] DEV_IS second unit FLOW GLOW debuts (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya, Kikirara Vivi) — `bible/world/hololive-History-2023-2026.md`
- 2024-11-29 [day] Two months after Ame's change of status, COVER names it: "conclusion of streaming activities," distinct from graduation (affiliates can still appear in projects) — `bible/world/hololive-History-2023-2026.md`

### 2024-12
- 2024-12-14 [day] -Promise- musical "The Broken Promise" — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2024])
- 2024-12-22 [day] "It's Not a Phase" (Mumei & Fauna) released — `bible/characters/Ceres-Fauna.md` ([Official F6])
- 2024-12-27 [day] 1,000,000 subscribers; Kiara's HOLOTALK guest the same day — `bible/characters/Ceres-Fauna.md` ([Observed F2; F3 title])
- 2024-12-31 [day] The World Tree is complete — `bible/characters/Ceres-Fauna.md` ([Observed F3 title])
- 2024-12 [month] VTuber Awards: "VTuber of the Year" (as FUWAMOCO) — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §Awards])
- 2024-12-14 [day] VTuber Awards: Most Chaotic VTuber — `bible/characters/Gigi-Murin.md` ([Observed GG6; secondary reporting])
- 2024-12-14 [day] Promise musical "The Broken Promise" — `bible/characters/Hakos-Baelz.md` ([Observed HB2])
- 2024-12-14 [day] -Promise- musical "The Broken Promise" — `bible/characters/IRyS.md` ([Observed R2 §2024])
- 2024-12-22 [day] "It's Not a Phase" (Mumei & Fauna) released — `bible/characters/Nanashi-Mumei.md` ([Official M6])
- 2024-12-14 [day] VTuber Awards: Best Art VTuber — `bible/characters/Raora-Panthera.md` ([Observed RP6; secondary report])
- 2024-12 [month] VTuber Awards: "VTuber of the Year" — `bible/world/FUWAMOCO.md`
- 2024-12-27 [day] Fauna on Kiara's HOLOTALK — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2024-12 [month] FUWAMOCO win "VTuber of the Year" at the VTuber Awards — `bible/world/hololive--Advent.md`
- 2024-12-28 [day] Half-year anniversary (New Year outfits announced, shown 2025-01-01) — `bible/world/hololive--Justice.md`

### 2025
- 2025 [year] Weekly Famitsu column launched (07-17); archived collabs bill Koyori, AZKi and Lamy as "KoZMy" (08-03, 08-20); "pink-haired pair" talk with Marine — `bible/characters/Hakui-Koyori.md` ([KO7] [KO4 lvgC3pW-LVA, oxWPvsUb_3Y])
- 2025 [year] "I don't care" and "Bloom in the night" for Mobile Suit Gundam GQuuuuuuX; miComet's "Lollipop" (official digital release 10-03) — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2] [Official SU10])
- 2025 [year] "Gehenna" cover with Chloe on her last day (01-26); Cuphead as #あずいろ (06-03) and an off-collab billed as a summer camp (08); "A letter only you can read" (06-15); a guest at Kiara's birthday live (07); #TASTYchallenge shorts with Kiara and Nene (07-11, 07-16); "AZUIRO BESTIE DAYS" (official release 09-18) — `bible/characters/Kazama-Iroha.md` ([IR4 5zJp7oulbwc, -im-pIdanZY, mwhcZmc6-s8] [IR5 f-UbyQUUykE, 0ldag8qdg6c, AQNPRJMMYY0] [Official music 642])
- 2025 [year] FLOW GLOW songs "24K GOLD" (03-14), "LOAD" (07-09), "good enough" (09-20); 500,000 subscribers (11-30, secondary) — `bible/characters/Kikirara-Vivi.md` ([Observed VI2])
- 2025 [year] Fauna (January) and Mumei (April) graduate; Promise's current members are Kronii, IRyS and Baelz — `bible/characters/Ouro-Kronii.md`
- 2025 [year] #ノエこよ Power Pros exhibition with Koyori (01-10); Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (04-14); 3rd-gen R.E.P.O. with Marine, Pekora and Flare (07-05); Elden Ring Nightreign with Flare and Pekora; an Audio-Technica collab with Ayame (07-11); "TREVIAN KNIGHT" (official digital release 08-16), which FUWAMOCO danced to (09-30) — `bible/characters/Shirogane-Noel.md` ([NO4] [NO5] [Official music 622])
- 2025 [year] 1.5 million subscribers (02-14, secondary); originals "Simulacre," "Gaotteko!" and "boundary"; a guest at Ina's birthday 3D live "EVERMORE" (05-21), singing "storia" with Ina and Tsunomaki Watame per a secondary set list; the first "#ホロ金策サバイバル" — `bible/characters/Shishiro-Botan.md` ([Observed BO2] [BO5] [EVERMORE report] [ASR BO20])
- 2025 [year] EP "Lieblings"; Code Geass ambassador (June, secondary); "Q&A With Bird Sisters" with Mumei (04-19); Harry Potter watch-alongs with Okayu; "FEAST" dance short with Bae (07-11) — `bible/characters/Takane-Lui.md` ([Observed LU2] [LU5] [LU4 Lj0MZFpHitQ, 5TUiccnytQA])
- 2025–2026 [year-range] Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card — `bible/characters/Watson-Amelia.md` ([A8, A19])
- 2025 [year] Joins "Magical Girl holoWitches!" (04–05); "Yoppara Music!" (official digital release 08-13); a "KoZMy 結成⁉" collab with AZKi and Koyori (08-03; secondary listings give its first anniversary in 2026-08) — `bible/characters/Yukihana-Lamy.md` ([Observed LM2] [Official music 609] [Koyori file lvgC3pW-LVA])
- 2025 [year] Nerissa's 3D concert with Calli and IRyS as guests; "OVER//RIDE" duet — `bible/world/IRyS-and-Nerissa-Pairs.md`
- 2025 [year] Gartic Phone EN + ID + JP (04-14); #holoREPO (05-25); R.E.P.O. on Ina's stream (06-02); Ina's "EVERMORE" — `bible/world/JP-Senpai-Pairs-2.md`
- 2025 [year] Myth relay for Gura's farewell — `bible/world/Streaming-Life.md`
- 2025, 2026 [year] hololive SUPER EXPO with -Justice- — `bible/world/hololive--Advent.md`

### 2025-01
- 2025-01-03 [day] Graduates; last post on X: "LOVE & PEACE / Love, Fauna" — `bible/characters/Ceres-Fauna.md` ([Observed F2, secondary])
- 2025-01-18 [day] "Mephisto" cover with HOLOSTARS' Banzoin Hakka — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Observed EB3])
- 2025-01-14 [day] The last "KoyoChlo" collab before Chloe's graduation; its description says the "#こよクロ disband!" gag was born in two-player co-op games; the duet cover 「一番の宝物」 followed (2025-01-28) — `bible/characters/Hakui-Koyori.md` ([KO4 mxIoysy6gJ4, nCPHzr_iF7s])
- 2025-01-29 [day] 500th on-stream sneeze, celebrated on X — `bible/characters/Mococo-Abyssgard.md` ([Observed MC6])
- 2025-01 [month] "Ame Tokimeki Koimoyō," the anime opening sung with Fubuki and Mio (AyaFubuMi) — `bible/characters/Nakiri-Ayame.md` ([Observed AY2; AY3])
- 2025-01-13 [day] On Okayu's team at the New Year Game Festival (with Suisei, Ina, IRyS, Cecilia) — `bible/characters/Nakiri-Ayame.md` ([AY5 THMIBrxnp-E])
- 2025-01-13 [day] Leads a team at the hololive New Year Game Festival (with Suisei, Ayame, Ina, IRyS, Cecilia) — `bible/characters/Nekomata-Okayu.md` ([OK4 THMIBrxnp-E])
- 2025-01 [month] "Office lady" outfit (#OLRissa) — `bible/characters/Nerissa-Ravencroft.md` ([Observed N3 titles])
- 2025-01 [month] Farewell week: last "KoyoChlo" collab (01-14), covers with La+ (01-15) and Koyori (「花の塔」 01-23; 「一番の宝物」 01-28 on Koyori's channel), "WILDCARD" with Kiara (01-25; the description says they had performed it at the 2024 fes), "Gehenna" with Iroha (01-26) — `bible/characters/Sakamata-Chloe.md` ([CH4 u5hBkM77dX0, acYx6NnoaAQ, mKq0e-7nnSU] [KO4 nCPHzr_iF7s] [CH5 eEGbAKvSf1Q] [IR4 5zJp7oulbwc])
- 2025-01-26 [day] Graduation live "Gochisōsama deshita"; tenth original song "Hikari Are" — `bible/characters/Sakamata-Chloe.md` ([CH4] [Observed CH2])
- 2025-01-03 [day] Fauna graduates — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2025-01-13 [day] New Year Game Festival, Okayu's team — `bible/world/JP-Senpai-Pairs.md`
- 2025-01-31 [day] Murky Divers, Advent × Justice (all nine) — `bible/world/Justice-Pairs.md`
- 2025-01 [month] The "$KRONII" coin bit and Calli's mock exposé — `bible/world/Time-and-Death.md`
- 2025-01-26 [day] Chloe's graduation live; she stays an affiliate — `bible/world/holoX.md`
- 2025-01-31 [day] "ADVENT VS JUSTICE" Murky Divers with all nine — `bible/world/hololive--Justice.md`
- 2025-01-03 [day] Fauna graduates — `bible/world/hololive--Promise.md`
- 2025-01-03 [day] Ceres Fauna graduates — `bible/world/hololive-History-2023-2026.md`
- 2025-01-26 [day] Sakamata Chloe concludes streaming activities (affiliate) — `bible/world/hololive-History-2023-2026.md`

### 2025-02
- 2025-02-02 [day] First birthday 3D concert, with Advent and JP guests — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW3 ouQF2A1l_cI])
- 2025-02-28 [day] Original "FEAST"; birthday 3D live "-KAGURA- Dance of the Gods" — `bible/characters/Hakos-Baelz.md` ([Observed HB2; HB3 viPlIHvk724])
- 2025-02-01 [day] "SuperNova" at the Nippon Budokan — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2025-02-26 [day] "GriMoire" at the Hollywood Palladium, the first solo concert outside Japan by a hololive production talent. — `bible/characters/Mori-Calliope.md` ([Official C19])
- 2025-02-14 [day] 3.0 Live2D model — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2025])
- 2025-02-02 [day] First birthday 3D concert — `bible/world/FUWAMOCO.md`
- 2025-02-27 [day] Kiara's watch party for Calli's GriMoire concert — `bible/world/TakaMori.md`

### 2025-03
- 2025-03-15/16 [day-range] Birthday: "DIAMOND GIRLFRIEND," EP "YaBAI," 3D live "HOPE UPON A STAR" — `bible/characters/IRyS.md` ([Observed R2 §2025; R3])
- 2025-03 [month] Spring covers: YOASOBI's "IDOL" (its description uses the written owl pun "idowl ! ~") and "Gravity" (original by Yoko Kanno, Maaya Sakamoto and Troy). — `bible/characters/Nanashi-Mumei.md` ([Archive metadata NEW-R2-014])
- 2025-03-09 [day] 6th fes. "Color Rise Harmony," day 2 — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2025])
- 2025-03-08 [day] hololive 6th fes. Color Rise Harmony, day 1 — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2025])
- 2025-03-08 [day] Justice hosted a watchalong of hololive 6th fes. (Expo 2025) Stage 1 ("FIRST STAGE with JUSTICE!") — `bible/world/hololive--Justice.md` ([Observed S4 nEV7T8peRcw])
- 2025-03-08/09 [day-range] SUPER EXPO 2025 and 6th fes. "Color Rise Harmony" — `bible/world/hololive-History-2023-2026.md`

### 2025-04
- 2025-04-25 [day] "Ash Again," credited to Gawr Gura & Casey Edwards (hololive catalogue digital-release date). — `bible/characters/Gawr-Gura.md` ([Official NEW-R1-016])
- 2025-04-14 [day] Gartic Phone EN + ID + JP collab with Mumei, Kronii, Ina, Elizabeth and Noel — `bible/characters/Kikirara-Vivi.md` ([VI5 OMDzBQohAf8])
- 2025-04-08 [day] "FAKE HEART," a cover with Kiara — `bible/characters/Laplus-Darknesss.md` ([LA5 yspJ9xmGRfw])
- 2025-04 [month] A farewell month of collabs across hololive: Overwatch with IRyS (04-22), a cover of "とんとんまーえ！" with Inugami Korone (04-23), Promise R.E.P.O. with IRyS, Kronii and Bae (04-24); last chatting stream with calls (04-26); 3D graduation stream (04-27, 04-28 JST) — `bible/characters/Nanashi-Mumei.md` ([Observed M2; M3 titles])
- 2025-04-26 [day] Performs "Sparkle" with Murasaki Shion at Shion's graduation live — `bible/characters/Sakamata-Chloe.md` ([Observed CH2])
- 2025-04-30 [day] "One Last Minecraft Trip." (Myth relay) — `bible/world/Bone-Bros.md`
- 2025-04 [month] Mumei's farewell month: "Donut Hole" with Kronii (04-11), Overwatch with IRyS (04-22), HOLOTALK (04-22), a Korone duet cover (04-23), Promise R.E.P.O. (04-24), Gura's room review — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2025-04-27 [day] Mumei graduates (04-28 JST) — `bible/world/Fauna-and-Mumei-Pairs.md`
- 2025-04-26/30 [day-range] Kronii's and Kiara's last collabs with Gura — `bible/world/Myth-and-Kronii-Other-Pairs.md`
- 2025-04/05 [month-range] Split Fiction series ("takamori split screen nostalgia") — `bible/world/TakaMori.md`
- 2025-04-19 [day] "Q&A With Bird Sisters" — `bible/world/holoX.md`
- 2025-04-30 [day] Myth relay "one last time" with Calli, Kiara, Ina and Gura before Gura's graduation — `bible/world/hololive--Myth.md`
- 2025-04-27 [day] Mumei graduates — `bible/world/hololive--Promise.md`
- 2025-04 [month] World Tour '25 "-Synchronize!-" announced, led by Momosuzu Nene, Kureiji Ollie, **Mori Calliope, IRyS and Nerissa Ravencroft**, with guests per city (Kronii and Bae in Sydney) — `bible/world/hololive-History-2023-2026.md`
- 2025-04-26 [day] Murasaki Shion graduates — `bible/world/hololive-History-2023-2026.md`
- 2025-04-27 (04-28 JST) [day, JST] Nanashi Mumei graduates — `bible/world/hololive-History-2023-2026.md`

### 2025-05
- 2025-05-01 [day] Graduates; final 3D mini live; last post "keep swimming! always! 💙" — `bible/characters/Gawr-Gura.md` ([Official G5] [Observed G3, G2])
- 2025-05-05 [day] 4 million subscribers (secondary reporting; the official shop's 4-million merchandise confirms the milestone, not the date) — `bible/characters/Houshou-Marine.md` ([Observed MA2 §2025])
- 2025-05-25 [day] #holoREPO with FUWAMOCO, Bae, Roboco, Towa and Hajime — `bible/characters/Kikirara-Vivi.md` ([VI5 Z5cpzbdsLDE, TgMVtjXW2Ms])
- 2025-05-15/28 [day-range] 2 million subscribers; second solo concert "PERSONYA RESPECT" at Pia Arena MM (FUWAMOCO watch it together) — `bible/characters/Nekomata-Okayu.md` ([Observed OK2] [OK5 gzPgXfYAbGg])
- 2025-05-24 [day] 3D concert "Requiem for Love – A JukeBox Musical" (guests incl. Calli, IRyS) — `bible/characters/Nerissa-Ravencroft.md` ([Observed N3 titles])
- 2025-05-01 [day] Gura graduates — `bible/world/AmeSame.md`
- 2025-05-01 [day] Gura graduates — `bible/world/Bone-Bros.md`
- 2025-05-28 [day] "PERSONYA RESPECT" watch-along — `bible/world/JP-Senpai-Pairs.md`
- 2025-05-01 [day] **Gawr Gura graduates** — `bible/world/hololive-History-2023-2026.md`
- 2025-05-02 [day] ENReco chapter 2 "The Chains of Fate" — `bible/world/hololive-History-2023-2026.md`
- 2025-05-01 [day] Gawr Gura graduates — `bible/world/hololive.md`

### 2025-06
- 2025-06-22 [day] Justice group song "RENEGADE"; later "SUPERNOVA SUPER GIRL" (2026-06-29). — `bible/characters/Cecilia-Immergreen.md` ([Official NEW-R4-020])
- 2025-06-22 [day] Justice group song "RENEGADE"; later "SUPERNOVA SUPER GIRL" (2026-06-29). — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official NEW-R4-020])
- 2025-06-22 [day] Justice group song "RENEGADE"; later "SUPERNOVA SUPER GIRL" (2026-06-29). — `bible/characters/Gigi-Murin.md` ([Official NEW-R4-020])
- 2025-06-02 [day] R.E.P.O. on Ina's stream, with Polka, Watame, Flare and Anya — `bible/characters/Kikirara-Vivi.md` ([VI5 grBU9Dl09Ds description])
- 2025-06-29 [day] "THAT'S WILD?!" 24-hour charity stream with Calli (Wildlife Warriors Worldwide) — `bible/characters/Koseki-Bijou.md` ([Observed Calli archive J5u2aGUrNq8])
- 2025-06-22 [day] Justice group song "RENEGADE"; later "SUPERNOVA SUPER GIRL" (2026-06-29). — `bible/characters/Raora-Panthera.md` ([Official NEW-R4-020])
- 2025-06-20 [day] First anniversary, "Operation DECODE" — `bible/world/hololive--Justice.md`

### 2025-07
- 2025-07 [month] 7th birthday 3D live "Sweet Pop Story"; FUWAMOCO appeared ("Bon appétit♡S"; secondary setlist) — `bible/characters/AZKi.md` ([AZ4 Dzw7zsjUoOI] [secondary setlist])
- 2025-07-19 [day] R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora, Ina, IRyS and Kronii (the description's lineup) — `bible/characters/AZKi.md` ([AZ4 _gZdFTluxtc])
- 2025-07-11 [day] 4th anniversary; 3.0 model — `bible/characters/IRyS.md` ([Observed R3 title])
- 2025-07 [month] Games with Pekora (The Forest, Fast Food Simulator); "Bridal Dream" cover with Chihaya (07-28) — `bible/characters/Kikirara-Vivi.md` ([VI4 lqidVnpl3_0, FWCkuwroMIw, NGeumGspO2g])
- 2025-07-05 [day] hololive night at Dodger Stadium with Ina and IRyS: a stadium sing-along and the first VTuber stream from the stadium — `bible/characters/Koseki-Bijou.md` ([Official KB9])
- 2025-07-27/28 [day-range] "Glow in the Dark," a Mythmash single with Kiara (official digital release 2025-07-28); a joint stream — `bible/characters/Laplus-Darknesss.md` ([Official music 600] [LA5 v5RKZXNuVyw] [LA4])
- 2025-07-05/06 [day-range] GAMERS fes 2 at Saitama Super Arena — `bible/characters/Nekomata-Okayu.md` ([Observed OK2; OK3])
- 2025-07-05 [day] hololive night at Dodger Stadium: Bijou with Ina and IRyS — `bible/world/Advent-Pairs.md` ([Official S8])
- 2025-07 [month] "Sweet Pop Story" — `bible/world/JP-Senpai-Pairs.md`
- 2025-07-27 [day] "Glow in the Dark" (Mythmash) — `bible/world/holoX.md`
- 2025-07 [month] MYTHMASH: each active member releases a duet with a Japanese senpai (#mythmashchemythtry) — `bible/world/hololive--Myth.md`
- 2025-07-05 PDT [day, PDT] hololive night at Dodger Stadium, Los Angeles, the second hololive–Dodgers collaboration: Ina, IRyS and Bijou — `bible/world/hololive-History-2023-2026.md`
- 2025-07-16 [day] hololive RECORDS label launched — `bible/world/hololive-History-2023-2026.md`

### 2025-08
- 2025-08-08 PDT [day, PDT] 3D showcase (5 PM PDT; Aug 9 09:00 JST) — `bible/characters/Cecilia-Immergreen.md` ([Official CI7])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Cecilia-Immergreen.md` ([Official CI7])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice; "Wind-Up," the first Justice solo; "SHALLYS" with Ina and FUWAMOCO (on violin); "I'm Your Treasure Box" with Bijou and Raora — `bible/characters/Cecilia-Immergreen.md` ([Official CI5])
- 2025-08-01 PDT [day, PDT] 3D showcase (5 PM PDT); she arranged and directed most of it, including "Giri Giri" with Vestia Zeta — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB7] [ASR EB20])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB7])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB5])
- 2025-08-01 [day] FUWAMOCO digital releases: "Lifetime Showtime"; later "Prisoner (FUWAMOCO ver.)" (2026-03-24) and "Ichizutte Trend♡" (2026-08-30). — `bible/characters/Fuwawa-Abyssgard.md` ([Official NEW-R3-019])
- 2025-08-23/24 [day-range] -All for One-: "HOT DUCK!", "Howling," "Lifetime Showtime," "SHALLYS" — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW5])
- 2025-08-02 PDT [day, PDT] 3D showcase (5 PM PDT; Aug 3 00:00 UTC) — `bible/characters/Gigi-Murin.md` ([Official GG8])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Gigi-Murin.md` ([Official GG8])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa — `bible/characters/Gigi-Murin.md` ([Official GG5])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "R x R x R" with Calli; "Countach" with Gigi and Kureiji Ollie; solo "La Roja (Arrange ver.)" — `bible/characters/Hakos-Baelz.md` ([Official HB5])
- 2025-08-23/24 [day-range] -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora — `bible/characters/Koseki-Bijou.md` ([Official KB5])
- 2025-08-01 [day] FUWAMOCO digital releases: "Lifetime Showtime"; later "Prisoner (FUWAMOCO ver.)" (2026-03-24) and "Ichizutte Trend♡" (2026-08-30). — `bible/characters/Mococo-Abyssgard.md` ([Official NEW-R3-019])
- 2025-08-23/24 [day-range] -All for One- with Fuwawa — `bible/characters/Mococo-Abyssgard.md` ([Official MC5])
- 2025-08-05 [day] "Kurukuru Cruise" with Ninomae Ina'nis (official digital release; a video premiere may be dated a day earlier) — `bible/characters/Nekomata-Okayu.md` ([Official OK7] [OK5 t7lNu-p_ANs])
- 2025-08-29 [day] Advent 2nd-anniversary 3D live "On the Run!" ("The Story of Advent") — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2025])
- 2025-08-09 PDT [day, PDT] 3D showcase (5 PM PDT; Aug 10 09:00 JST) — `bible/characters/Raora-Panthera.md` ([Official RP8])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Raora-Panthera.md` ([Official RP8])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice, solo "Gacha x Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and guest Oozora Subaru, "I'm Your Treasure Box" with Bijou and Cecilia — `bible/characters/Raora-Panthera.md` ([Official RP5])
- 2025-08-29 [day] Advent 2nd-anniversary 3D live "On the Run!" — `bible/characters/Shiori-Novella.md` ([Observed SN2 §2025])
- 2025-08-23/24 [day-range] -All for One-: "Genesis" as five, and pair stages across EN — `bible/world/Advent-Pairs.md`
- 2025-08-29 [day] "On the Run!" 2nd-anniversary 3D live — `bible/world/Advent-Pairs.md`
- 2025-08-23/24 [day-range] -All for One-: "HOT DUCK!" with Bijou and Subaru; their version of "Howling"; "Lifetime Showtime"; "SHALLYS" with Ina and Cecilia — `bible/world/FUWAMOCO.md` ([Official S5])
- 2025-08-23/24 [day-range] -All for One-: "R x R x R," "Countach" — `bible/world/Hakos-Baelz-Pairs.md`
- 2025-08-04 [day] "Kurukuru Cruise" — `bible/world/JP-Senpai-Pairs.md`
- 2025-08-16 PDT [day, PDT] Justice group 3D collab (after the individual showcases 08-01/02/08/09 PDT) — `bible/world/Justice-Pairs.md`
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ALiCE&u," "START AGAIN," "High Tide" (Elizabeth); "Countach," "MONSTER," "III," "Wonky Monkey" (Gigi); "Wind-Up," "SHALLYS," "I'm Your Treasure Box" (Cecilia); "Gacha×Gacha ADVENTURE!," "Neko Kaburi-Na," "I'm Your Treasure Box" (Raora) — `bible/world/Justice-Pairs.md` ([Official S6])
- 2025-08-23 [day] -All for One- opens with all of EN, then Advent's "Genesis" — `bible/world/hololive--Advent.md` ([Official S9])
- 2025-08-29 [day] 2nd-anniversary 3D live "On the Run!" with "The Story of Advent" (five chapters, five songs) — `bible/world/hololive--Advent.md`
- 2025-08-01/02/08/09 PDT [day-range, PDT] Individual 3D showcases, each at 5 PM PDT: Elizabeth (08-01), Gigi (08-02), Cecilia (08-08), Raora (08-09) — `bible/world/hololive--Justice.md` ([Official S7])
- 2025-08-16 PDT [day, PDT] Justice group 3D collaboration stream (5 PM PDT) — `bible/world/hololive--Justice.md` ([Official S7])
- 2025-08-23 EDT [day, EDT] -All for One-: Justice's first group performance at an in-person concert venue in 3D ("ABOVE BELOW"); Cecilia's "Wind-Up" was the first Justice solo number of that concert; see the member files for their other stages — `bible/world/hololive--Justice.md` ([Official S3])
- 2025-08-01/02/08/09 PDT [day-range, PDT] Justice 3D showcases, each at 5 PM PDT: Elizabeth (08-01), Gigi (08-02), Cecilia (08-08), Raora (08-09) — `bible/world/hololive-History-2023-2026.md`
- 2025-08-16 PDT [day, PDT] Justice group 3D collaboration stream — `bible/world/hololive-History-2023-2026.md`
- 2025-08-23/24 EDT [day-range, EDT] EN 3rd concert "-All for One-" (Radio City Music Hall, New York): day 1 opens with the all-member "All for One," followed by Advent's "Genesis"; Justice's first group performance at an in-person concert venue in 3D — `bible/world/hololive-History-2023-2026.md`
- 2025-08-29 [day] Advent 2nd-anniversary live "On the Run!" ("The Story of Advent") — `bible/world/hololive-History-2023-2026.md`

### 2025-09
- 2025-09-18 [day] "AZUIRO BESTIE DAYS" with Kazama Iroha (official digital release) — `bible/characters/AZKi.md` ([Official AZ10])
- 2025-09-03 [day] 7th anniversary: a new 3D kimono and "Hanafubuki" — `bible/characters/Nakiri-Ayame.md` ([Observed AY2])
- 2025-09-13 [day] 5th anniversary collab with announcements (Calli, Kiara, Ina) — `bible/world/hololive--Myth.md`

### 2025-10
- 2025-10-18 [day] First original song "I'll still be here" presented (digital release 10-20) — `bible/characters/Gigi-Murin.md` ([Official GG7] [Observed GG2])
- 2025-10-07 [day] Announced: her "LET'S JUST CRASH" is the second opening theme of the TV anime *Gachiakuta* (lyrics by syudou and Mori Calliope; composition and arrangement by syudou). — `bible/characters/Mori-Calliope.md` ([Official NEW-R1-002])
- 2025-10-10 [day] Promise releases "Run Back 'Round" — `bible/characters/Ouro-Kronii.md` ([Official K6])
- 2025-10-03 [day] Hiodoshi Ao (ReGLOSS) leaves — `bible/world/hololive-History-2023-2026.md`
- 2025-10-15 [day] Official fan club launches — `bible/world/hololive-History-2023-2026.md`

### 2025-11
- 2025-11-19 [day] Solo concert "Departure" at Pia Arena MM (the wiki counts it as her tenth); EPs "Re:Start" and "Re:Birth" (11-05) — `bible/characters/AZKi.md` ([Official AZ8] [Observed AZ2, secondary count])
- 2025-11-19 [day] "Departure" concert: AS_tar performed "The Last Frontier"; she gave Suisei a reply to Suisei's earlier concert letter, and they unveiled "Going My Way" (digital release 2026-05-19). — `bible/characters/AZKi.md` ([Official NEW-R5-002])
- 2025-11-19 [day] At AZKi's "Departure" concert, AS_tar performed "The Last Frontier"; AZKi gave Suisei a reply to her earlier concert letter, and they unveiled "Going My Way" (digital release 2026-05-19). — `bible/characters/Hoshimachi-Suisei.md` ([Official NEW-R5-002])
- 2025-11-01 [day] 3D live (original dossier date retained; timezone not reverified) — `bible/characters/Koseki-Bijou.md` ([Observed KB2 §2025])
- 2025-11-03 [day] Digital release of second original song "ROCK IN!" — `bible/characters/Koseki-Bijou.md` ([Official FIX-R3-003])
- 2025-11-09 [day] VALORANT VSaikyou with "Saki Ike Ninja" (participation; placement not inferred) — `bible/characters/Nakiri-Ayame.md` ([Observed AY2, secondary; AY4])
- 2025-11-16 [day] The "Doom" spell in Kiara's Mage Arena collab — `bible/characters/Raora-Panthera.md` ([Observed RP7])
- 2025-11-16 [day] Raora's "Doom" on her stream becomes a meme — `bible/characters/Takanashi-Kiara.md` ([Observed T6])
- 2025-11-23 [day] Duo concert announced — `bible/world/TakoTori.md`
- 2025-11 [month] Raora's friendly-fire "Doom" spell in Kiara's Mage Arena collab becomes a widely shared fan meme (KYM dates the stream 11-16) — `bible/world/hololive-History-2023-2026.md`
- 2025-11-15 [day] hololive Indonesia 1st concert "Chromatic Future" — `bible/world/hololive-History-2023-2026.md`

### 2025-12
- 2025-12-22 [day] "Bright Tonight" with IRyS, Kronii and FUWAMOCO released — `bible/characters/Gigi-Murin.md` ([Official GG7])
- 2025-12 [month] holoX's 4th anniversary, including "Gyouan Xdeath" — `bible/characters/Laplus-Darknesss.md` ([Observed LA2])
- 2025-12-01 [day] holoX's 4th anniversary, including "Gyouan Xdeath" — `bible/characters/Takane-Lui.md` ([Observed LU2])
- 2025-12-01 [day] 4th anniversary: "Gyouan Xdeath," concert announced — `bible/world/holoX.md`
- 2025-12-27 [day] Amane Kanata graduates — `bible/world/hololive-History-2023-2026.md`

### 2026
- 2026 [year] FLOW GLOW's self-titled album (01-21, including "PUNISHER" and "the light"); first on-stream Super Mario Bros. 3 and Super Mario World playthroughs; Getting Over It, a gift from Pekora (07-25); 700,000 subscribers during an endurance karaoke (08-11, secondary); FLOW GLOW's "magic summer" (08-18); MVP's "Hatsukoi Cider" with Marine and Pekora (09, secondary record) — `bible/characters/Kikirara-Vivi.md` ([Official music 024] [VI4] [Observed VI2] [MVP upload record])
- 2026 [year] The game sequel "Okayu Nyūmu! R," which she stars in and supervises; Final Fantasy VII playthrough series — `bible/characters/Nekomata-Okayu.md` ([Observed OK3; OK4])
- 2026 [year] Her collaboration sake "Yukiyozuki" with Meiri Shurui (04); an off-collab with Koyori titled to name their duo (03); a NePoLaBo 3D party (04-29); NePoX took place at Ariake Arena on 2026-09-26/27 with Nene, Polka, Lamy, Botan, La+, Lui, Koyori and Iroha: NePoLaBo-versus-holoX games ending Day 1 with all eight in a giant-robot red-light/green-light challenge, and the collaboration song "Watcha Gatcha!!!!!!!!" introduced [Secondary NEW-R5-020, organizer report]; "Snowlight Stories" (official digital release 08-13) — `bible/characters/Yukihana-Lamy.md` ([LM4 Zi8R63ee0Fs, Ekdsnb2aWY4, Ml1tM8S40p0] [Official NePoX page] [Official music 792] [Brewery page])
- 2026 [year] "Bound by Fate," 3rd-anniversary 3D live — `bible/world/Advent-Pairs.md`
- 2026 [year] "Chatter Chatter"; Elizabeth's birthday cover — `bible/world/JP-Senpai-Pairs-2.md`

### 2026-01
- 2026-01-17/18 [day-range] hololive Fantasy concert "#OperationHeartfulCuties," K-Arena Yokohama — `bible/characters/Houshou-Marine.md` ([Observed MA2 §2025–2026] [Official announcement])
- 2026-01-23 [day] Original song "OYOME♡HOLIC" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2026])
- 2026-01-08 (digital release; zone unspecified) [day] Digital release of TAKO∞TAKOVER; lyrics by Mori Calliope. I19 discusses its deliberately unsettling takeover story. — `bible/characters/Ninomae-Inanis.md` ([Observed—published interview I19] [Official I25; digital release: https://hololive.hololivepro.com/en/music/693/, checked 2026-10-03])
- 2026-01-17/18 [day-range] hololive Fantasy concert "#OperationHeartfulCuties," K-Arena Yokohama — `bible/characters/Shirogane-Noel.md` ([Observed NO2] [Official announcement])
- 2026-01-08 [day] "TAKO∞TAKOVER" digital release (lyrics by Calli) — `bible/world/Myth-and-Kronii-Other-Pairs.md`
- 2026-01-26 [day] Group song "Breakout" — `bible/world/hololive--Advent.md`

### 2026-02
- 2026-02-26 [day] Advent group song "What Goes Around"; later "Unchained" (03-26), "Spotlight" (08-02) and the third-anniversary 3D live "Bound by Fate" (archived 08-09). — `bible/characters/Fuwawa-Abyssgard.md` ([Official NEW-R3-001; archive metadata])
- 2026-02-28 [day] Birthday 3D live "ReCOLOR" with a new 3D outfit; original "SNAKE EYES"; her fifth Febaerary — `bible/characters/Hakos-Baelz.md` ([Observed HB2] [ASR HB20])
- 2026-02-21 [day] "SuperNova: REBOOT" at K-Arena Yokohama — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2026-02-28 [day] "Chatter Chatter" with Hoshimachi Suisei: anime MV (official digital release 2026-03-01) — `bible/characters/Houshou-Marine.md` ([MA4 di9NZ6ja_mE] [Official music 711])
- 2026-02-26 [day] Advent group song "What Goes Around"; later "Unchained" (03-26), "Spotlight" (08-02) and the third-anniversary 3D live "Bound by Fate" (archived 08-09). — `bible/characters/Koseki-Bijou.md` ([Official NEW-R3-001; archive metadata])
- 2026-02-26 [day] Advent group song "What Goes Around"; later "Unchained" (03-26), "Spotlight" (08-02) and the third-anniversary 3D live "Bound by Fate" (archived 08-09). — `bible/characters/Mococo-Abyssgard.md` ([Official NEW-R3-001; archive metadata])
- 2026-02-06 [day] Her third major album, "DISASTERPIECE." Universal Music frames it around showing an imperfect self and finding beauty in imperfection; the track list includes the *Gachiakuta* opening "LET'S JUST CRASH" and insert song "Rivals and Equals." — `bible/characters/Mori-Calliope.md` ([Official C16])
- 2026-02-14 [day] A new pink kimono outfit — `bible/characters/Nakiri-Ayame.md` ([Observed AY2; AY4])
- 2026-02-23 [day] Released "Non Delicious"; she performed it on STAGE 1 of hololive 7th fes. (2026-03-06). — `bible/characters/Nekomata-Okayu.md` ([Official NEW-R5-011])
- 2026-02-26 [day] Advent group song "What Goes Around"; later "Unchained" (03-26), "Spotlight" (08-02) and the third-anniversary 3D live "Bound by Fate" (archived 08-09). — `bible/characters/Nerissa-Ravencroft.md` ([Official NEW-R3-001; archive metadata])
- 2026-02-02 [day] First EP "re:VISION" — `bible/characters/Ninomae-Inanis.md` ([Official I26])
- 2026-02-16 [day] Digital release of first original song "Monsters and Men" — `bible/characters/Shiori-Novella.md` ([Official FIX-R3-002])
- 2026-02-26 [day] Advent group song "What Goes Around"; later "Unchained" (03-26), "Spotlight" (08-02) and the third-anniversary 3D live "Bound by Fate" (archived 08-09). — `bible/characters/Shiori-Novella.md` ([Official NEW-R3-001; archive metadata])
- 2026-02-08 [day] 2nd album *Vogelfrei* — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §2026; T8])
- 2026-02 [month] Kiara's "Blue & Gold" tribute — `bible/world/AmeSame.md`
- 2026-02-26 [day] Group song "What Goes Around" — `bible/world/hololive--Advent.md` ([Official NEW-R3-001])
- 2026-02-20/22 JST [day-range, JST] GeoGuessr: Elizabeth, Gigi and Cecilia trained (02-20) and represented Justice against Advent (02-22), with Bijou hosting/commentating — `bible/world/hololive--Justice.md` ([Observed, secondary event roster])
- 2026-02 [month] Kiara's album includes "Blue & Gold," a tribute to Gura and Ame — `bible/world/hololive--Myth.md`

### 2026-03
- 2026-03-07 [day] hololive 7th fes. "Ridin' on Dreams," STAGE 3 (with IRyS, Bae, Shiori) — `bible/characters/AZKi.md` ([Official AZ7])
- 2026-03-07 JST [day, JST] hololive 7th fes. Ridin' on Dreams, STAGE 2: Justice performed "ABOVE BELOW.; Cecilia also sang "nowhere" with a violin performance. — `bible/characters/Cecilia-Immergreen.md` ([Official NEW-R4-014])
- 2026-03-07 JST [day, JST] hololive 7th fes. Ridin' on Dreams, STAGE 2: Justice performed "ABOVE BELOW." — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official NEW-R4-005/009/019])
- 2026-03-07 JST [day, JST] hololive 7th fes. Ridin' on Dreams, STAGE 2: Justice performed "ABOVE BELOW." — `bible/characters/Gigi-Murin.md` ([Official NEW-R4-005/009/019])
- 2026-03-06/08 [day-range] hololive 7th fes. "Ridin' on Dreams": "Idol" as the final solo number of STAGE 3 (her own choreography with a breakdance finish, by her account) and "Kakumei Dualism" with Natsuiro Matsuri; a venue talk with Cecilia Immergreen (her account) — `bible/characters/Hakos-Baelz.md` ([Official HB11 lineup] [secondary setlist HB12] [ASR HB20])
- 2026-03-24 [day] #ラミこよ off-collab with Lamy, proposing to choose a duo name (no final name established) — `bible/characters/Hakui-Koyori.md` ([Lamy channel Zi8R63ee0Fs])
- 2026-03-08 [day] hololive 7th fes. "Ridin' on Dreams," STAGE 4 (with Calli, Kronii, Bijou, Nerissa) — `bible/characters/Hoshimachi-Suisei.md` ([Official SU9])
- 2026-03 [month] "Chatter Chatter" with Houshou Marine; playable in Fortnite (03-13 to 03-24) — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU4] [SU3, secondary])
- 2026-03-22 [day] 8th anniversary: "Prima Donna"; arena tour "Once Upon a Stellar" announced; personal management agency Studio STELLAR for her solo work (she stays in hololive for collabs and group activities); fan club opens — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2026-03-10 [day] Mario Tennis with Pekora as her coach ("Pekoach") — `bible/characters/Houshou-Marine.md` ([MA4 GWZrQZ6leZI])
- 2026-03 [month] Birthday live "Racing Towards Hope"; "BE MY FLAME"; solo album "DANGERyS" and solo concert announced — `bible/characters/IRyS.md` ([Observed R2 §2026; R3])
- 2026-03-31 PDT [day, PDT] April Fools "new VTuber debut" as Bonelliope Mori, "a bone-fide idol" — `bible/characters/Mori-Calliope.md` ([Observed C31, secondary])
- 2026-03-06 [day] hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Okayu, Ina, FUWAMOCO) — `bible/characters/Nakiri-Ayame.md` ([Official AY6] [Observed AY3])
- 2026-03-06 [day] hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Ayame, Ina, FUWAMOCO) — `bible/characters/Nekomata-Okayu.md` ([Official OK6] [Observed OK3])
- 2026-03-28 [day] Single "Blue World" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §Discography])
- 2026-03-27/28 PDT [day-range, PDT] "Drawn to Dawn" duo concert with Kiara (Los Angeles) — `bible/characters/Ninomae-Inanis.md` ([Official I20, I21])
- 2026-03-13 [day] 3D birthday live; Watson Amelia guests; she announces the EP "Way 2 U"; the title single's official on-sale date is 2026-03-15 — `bible/characters/Ouro-Kronii.md` ([Observed K33, secondary, stream t=1711; K38, secondary])
- 2026-03-07 JST [day, JST] hololive 7th fes. Ridin' on Dreams, STAGE 2: Justice performed "ABOVE BELOW." — `bible/characters/Raora-Panthera.md` ([Official NEW-R4-005/009/019])
- 2026-03-24 [day] Bilingual show HoloEN REWIND: first episode — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §HoloEN REWIND])
- 2026-03-27/28 PDT [day-range, PDT] "Drawn to Dawn" duo concert with Ina (The Wiltern, Los Angeles) — `bible/characters/Takanashi-Kiara.md` ([Official T11, T12])
- 2026-03 [month] Guest spot at Kronii's 3D birthday live — `bible/characters/Watson-Amelia.md` ([Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711])
- 2026-03-24 [day] "Prisoner (FUWAMOCO ver.)" — `bible/world/FUWAMOCO.md` ([Official NEW-R3-019])
- 2026-03 [month] 7th fes: venue talk; Resident Evil series (April) — `bible/world/Hakos-Baelz-Pairs.md`
- 2026-03-06 to 03-08 [day] hololive 7th fes. "Ridin' on Dreams" (STAGE 1 Mar 6, STAGE 3 Mar 7, STAGE 4 Mar 8) — `bible/world/JP-Senpai-Pairs.md`
- 2026-03-27/28 PDT [day-range, PDT] "Drawn to Dawn," the Wiltern, LA — `bible/world/TakoTori.md`
- 2026-03-13 [day] Ame guests at Kronii's 3D birthday live — `bible/world/Time-Duo.md`
- 2026-03-26 [day] Group song "Unchained" — `bible/world/hololive--Advent.md` ([Official NEW-R3-001])
- 2026-03-06/08 [day-range] SUPER EXPO 2026 and 7th fes. "Ridin' on Dreams" — `bible/world/hololive-History-2023-2026.md`
- 2026-03-27/28 PDT [day-range, PDT] Kiara and Ina's duo concert "Drawn to Dawn" (Los Angeles) — `bible/world/hololive-History-2023-2026.md`

### 2026-04
- 2026-04-01 [day] April Fools: a "new VTuber" debut on her original design — `bible/characters/AZKi.md` ([AZ4] [ASR AZ20])
- 2026-04-25 [day] 2026 birthday live with guests from several branches (credited in her archived broadcast description); the performances were later released as cover videos ("Live from COVER Corp. Studio," from May) — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Archive metadata FIX-R4-001] [Observed EB3, archived credits])
- 2026-04 [month] "Mekurumeku Rendezvous," a TV anime ending theme — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW3 vSwxof0K8lk])
- 2026-04 [month] Resident Evil series with Cecilia (her account); the "Liar Dancer" cover; the mock rival feud — `bible/characters/Hakos-Baelz.md` ([ASR HB20])
- 2026-04-29 [day] holoX's first in-person unit concert, "First MISSION" — `bible/characters/Hakui-Koyori.md` ([Official KO6])
- 2026-04-04 [day] [Unverified: identification of Suisei's reported Calliope appearance as UNCUT ROCK!!; the event and date require a direct locator.] — `bible/characters/Hoshimachi-Suisei.md` ([ASR SU20, her own account] [Observed fan-clip titles, secondary])
- 2026-04-18 [day] Hoshimatic Project's second song "BEEP BEEP" (official digital release; premiered the day before) — `bible/characters/Hoshimachi-Suisei.md` ([Official SU10] [SU4])
- 2026-04-29 [day] holoX's first concert, "First MISSION" — `bible/characters/Kazama-Iroha.md` ([Official IR6])
- 2026-04-08 [day] holoX album "Secret ORDER" released — `bible/characters/Laplus-Darknesss.md` ([Official FIX-R6-003])
- 2026-04-29 [day] holoX's first in-person unit concert, "First MISSION" (La+, Lui, Koyori, Iroha) — `bible/characters/Laplus-Darknesss.md` ([Official LA6])
- 2026-04-04 JST [day, JST] Sixth birthday 3D live "UNCUT ROCK!!" with a live band, plus a members-only encore — `bible/characters/Mori-Calliope.md` ([Archive metadata C32])
- 2026-04 [month] The "Shishiro Cup" fighting-game tournament, offline; original "Tokihanate" (04-10) — `bible/characters/Shishiro-Botan.md` ([BO4] [Observed BO2])
- 2026-04-08 [day] holoX album "Secret ORDER" released — `bible/characters/Takane-Lui.md` ([Official FIX-R6-004])
- 2026-04-29 [day] holoX's first in-person unit concert "First MISSION"; COVER's interview after it describes the concert as a turning point for the four-member group and its audience — `bible/characters/Takane-Lui.md` ([Official LU6])
- 2026-04-02 [day] "Mekurumeku Rendezvous," ending theme of *Reborn as a Vending Machine, I Now Wander the Dungeon* Season 3 — `bible/world/FUWAMOCO.md`
- 2026-04-23 [day] Nerissa's Tomodachi Life Miis of IRyS and Ina — `bible/world/IRyS-and-Nerissa-Pairs.md`
- 2026-04-24 [day] "GETCHA!" cover — `bible/world/TakoTori.md`
- 2026-04-08 [day] Album "Secret ORDER" released — `bible/world/holoX.md` ([Official, R6])
- 2026-04-29 [day] "First MISSION," Pia Arena MM — `bible/world/holoX.md`

### 2026-05
- 2026-05-18/19 [day-range] AS_tar with Suisei: a horror off-collab, then "Going My Way" — `bible/characters/AZKi.md` ([AZ4])
- 2026-05 [month] CCGG 3D live with Gigi (after-talk 05-20, secondary archive evidence); "CCGG MADNESS" MV (05-17; digital 05-29) — `bible/characters/Cecilia-Immergreen.md` ([Official CI1] [Observed CI3 1rIXU_4xGvY, bTxEGwMOQQI])
- 2026-05 [month] CCGG 3D live with Cecilia; "CCGG MADNESS" MV (05-17; digital 05-29) — `bible/characters/Gigi-Murin.md` ([Official GG1, GG7] [Observed GG3])
- 2026-05-18/19 [day-range] An AS_tar horror off-collab on AZKi's channel (v60QmEvEQqw), then "Going My Way" with AZKi — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU4; archived metadata] [Official AZKi file])
- 2026-05-19 [day] An excerpt from Elizabeth's 2026 birthday show, uploaded 05-19, credits Iroha, Watame, Nene, Polka and FUWAMOCO on "CHA-LA HEAD-CHA-LA" (upload date, not necessarily the show date) — `bible/characters/Kazama-Iroha.md` ([IR5 xylll7Mp0jk])
- 2026-05-03 [day] Tochigi Future Ambassador — `bible/characters/Laplus-Darknesss.md` ([Official LA3])
- 2026-05-19 [day] A 3D lie-detector "challenge" to Nekomata Okayu — `bible/characters/Laplus-Darknesss.md` ([LA4 F3i30BIJmtY])
- 2026-05-25/26 [day-range] "Onee-sama♡Love Call" (official digital release 2026-05-26); album "Project Y.M.A." announced — `bible/characters/Laplus-Darknesss.md` ([Official music 753] [Observed LA2])
- 2026-05-08 [day] Single "STORM" (later on the EP) — `bible/characters/Ouro-Kronii.md` ([Observed K38, secondary])
- 2026-05-28 JST [day, JST] "Way 2 U" MV: Kronii shares the lyric credit with JALTO (JALTO composed and arranged; choreography by Miyuki Nishijima). — `bible/characters/Ouro-Kronii.md` ([Archive metadata NEW-R2-006, reproducing the MV credits])
- 2026-05 [month] First birthday 3D live concert (archived video w37yVSXhV_c); the shared timeline records the announced date as May 10 JST / May 9 PDT, but the actual zoned start remains unverified — `bible/characters/Raora-Panthera.md` ([Observed RP3; hololive -Justice- History; hololive History 2023–2026 Timeline])
- 2026-05-10 [day] MV of her second original song "Draw." (the period is part of the title); official digital release 2026-05-11. — `bible/characters/Raora-Panthera.md` ([Archive metadata; Official NEW-R4-017])
- 2026-05 [month] CCGG 3D live, "CCGG MADNESS" — `bible/world/Justice-Pairs.md`
- 2026-05 [month] CCGG (Gigi and Cecilia) joint 3D live (secondary event coverage) and "CCGG MADNESS"; Raora's first birthday 3D live (May 2026; announced for 05-10 JST / 05-09 PDT; actual zoned start unverified) — `bible/world/hololive--Justice.md`
- 2026-05 [month] Gigi and Cecilia's joint CCGG 3D live and "CCGG MADNESS"; Raora's first birthday 3D live (May 2026; announced for 05-10 JST / 05-09 PDT; actual zoned start unverified) — `bible/world/hololive-History-2023-2026.md`
- 2026-05-24 [day] ENReco chapter 3 "Broken Bonds" — `bible/world/hololive-History-2023-2026.md`

### 2026-06
- 2026-06-07 [day] A German-language cover of inabakumori's "LAGTRAIN" (German lyrics credited to Jinja). — `bible/characters/Cecilia-Immergreen.md` ([Archive metadata NEW-R4-013])
- 2026-06-25 [day] Original MV "enough" — `bible/characters/Gigi-Murin.md` ([Observed GG3])
- 2026-06-18/19 [day-range] 「風向きエントロピー」 (official English title "Entropy of wind direction"; MV 06-18, digital release 06-19); a secondary chronology numbers it her ninth original — `bible/characters/Kazama-Iroha.md` ([IR4 RDobidAdBCA] [Official music 764] [Observed IR2])
- 2026-06-30 [day] Wins the overall ranking at Kizuna Ai's "Kizuna Ai Cup 2026" (Among Us 3D, Fall Guys) — `bible/characters/Mori-Calliope.md` ([Observed C31, secondary])
- 2026-06-10 [day] Serendipity interview and partnership with Shiori Novella. — `bible/characters/Mori-Calliope.md` ([Official C11])
- 2026-06-12 [day] 1,000,000 subscribers — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2026])
- 2026-06-04 [day] Serendipity interview and partnership with Kronii — `bible/characters/Ninomae-Inanis.md` ([Official I7])
- 2026-06-04 [day] Serendipity interview and partnership with Ina — `bible/characters/Ouro-Kronii.md`
- 2026-06-01/05 [day-range] "#ホロ金策サバイバル2," with Botan as game master — `bible/characters/Shishiro-Botan.md` ([BO4] [ASR BO20])
- 2026-06 [month] Serendipity interview and partnership with Koseki Bijou — `bible/characters/Takanashi-Kiara.md` ([Official T10])
- 2026-06-11 [day] EP "The LEGENDARY" with "Soar" (official digital release of "Soar" 06-12); 1st live "REBELLION" (2026-12-16) and a BAYFM78 radio programme (from 07-03) announced; EN members' channels posted animated "Soar" shorts crediting external motion creators — `bible/characters/Takane-Lui.md` ([Official LU7] [Official music 760] [LU4] [LU5])
- 2026-06-11 [day] COVER announces a regular BAYFM78 radio programme for her (first broadcast scheduled for 2026-07-03); orders open for the four-track EP "The LEGENDARY," including "Soar"; her first live concert "REBELLION" announced for 2026-12-16 at Kanadevia Hall (after the baseline: an announcement only). — `bible/characters/Takane-Lui.md` ([Official NEW-R6-013/014])
- 2026-06-04 [day] Official Serendipity interview — `bible/world/OctoClock.md`
- 2026-06-24 [day] "It's Time for Octo'Clock!" short — `bible/world/OctoClock.md`
- 2026-06-27 PDT [day, PDT] Second-anniversary live "How to Protect JUSTICE!" (06-28 JST) — `bible/world/hololive--Justice.md` ([Official S1 video list])
- 2026-06-27 PDT [day, PDT] Justice's second-anniversary live "How to Protect JUSTICE!" (06-28 JST) — `bible/world/hololive-History-2023-2026.md`

### 2026-07
- 2026-07-01 [day] "AZKi 8th Birthday Live 'Cross Over'": little-devil outfit; she performed Konomi Suzuki's "Redo"; IRyS appears in the archived short metadata ("A Cruel Angel's Thesis"; secondary setlist); "Saikyo Mirai Shodo" (credited to AZKi and Konomi Suzuki) released digitally 07-02 — `bible/characters/AZKi.md` ([Observed AZ2; AZ4] [Official AZ11] [secondary setlist])
- 2026-07 [month] Kagawa Prefectural Police traffic-safety ambassador; a commendation, "a hololive first" — `bible/characters/AZKi.md` ([AZ4 titles])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "SUPERNOVA SUPER GIRL" with Justice, "CCGG MADNESS" as Autofister with Gigi, "Break It Down" with Vestia Zeta and Shiori, "Cloudy Sheep" with Tsunomaki Watame and Calli (day 1); "ABOVE BELOW" in the Advent+Justice medley (day 2) — `bible/characters/Cecilia-Immergreen.md` ([Official CI4, CI8])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB4, EB8])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: the unit B.F.F with Mococo and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW4; Serendipity report])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "SUPERNOVA SUPER GIRL" with Justice and "CCGG MADNESS" as Autofister with Cecilia (day 1); "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO, and "ABOVE BELOW" in the Advent+Justice medley (day 2) — `bible/characters/Gigi-Murin.md` ([Official GG4, GG9])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: BaeRyS with IRyS ("LUVATORRRRRY!"), "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame (day 1) — `bible/characters/Hakos-Baelz.md` ([Official HB4, HB5])
- 2026-07-08/13 [day-range] Fan meeting "Hoshiyomi Pajama Party Vol.1" (Tokyo, Osaka) — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2026-07-12 [day] Album "DANGERyS"; the official introduction names "Escalate" the lead single and describes Eurobeat as one of several styles on the album. — `bible/characters/IRyS.md` ([Official NEW-R2-004])
- 2026-07-03/04 [day-range] Serendipity concert, duo with Takanashi Kiara ("Rocku Wawa") — `bible/characters/Koseki-Bijou.md` ([Official KB4])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: the unit B.F.F with Fuwawa and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) — `bible/characters/Mococo-Abyssgard.md` ([Official MC4; Serendipity report])
- 2026-07-24 [day] TOHO animation names Mori Calliope as Kou Tousetsu in the English dub of *Though I Am an Inept Villainess*, announcing a July 26 streaming start. — `bible/characters/Mori-Calliope.md` ([Official FIX-R1-003])
- 2026-07-09 [day] Cast as "Risa" in the anime "Tenchi Galaxy" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2026])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) — `bible/characters/Raora-Panthera.md` ([Official RP4, RP9])
- 2026-07-03/04 [day-range] Serendipity concert, duo with Mori Calliope — `bible/characters/Shiori-Novella.md` ([Official SN4])
- 2026-07-30 [day] "Into The Void" motion comic begins — `bible/characters/Shiori-Novella.md` ([Observed SN3])
- 2026-07-06 PDT (07-07 JST) [day, PDT] Birthday 3D live — `bible/characters/Takanashi-Kiara.md` ([Observed T24: official hololive English post, search-indexed text, X not opened])
- 2026-07-03/04 [day-range] Serendipity: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth — `bible/world/Advent-Pairs.md`
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: the unit B.F.F with Raora ("Inu Neko. Seishun Massakari") — `bible/world/FUWAMOCO.md` ([Official S4; Serendipity report])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: BaeRyS "LUVATORRRRRY!"; "HELP!!" — `bible/world/Hakos-Baelz-Pairs.md`
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: units Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora); guests' songs with Justice members: "HELP!!" (Kobo, Bae, Elizabeth), "Break It Down" (Zeta, Shiori, Cecilia), "Cloudy Sheep" (Watame, Calli, Cecilia), "MAKE IT, BREAK IT" (Zeta, FUWAMOCO, Gigi), "What an amazing swing" (Watame, Kiara, Raora) — `bible/world/Justice-Pairs.md` ([Official S3, S7])
- 2026-07-03/04 [day-range] Serendipity concert, Los Angeles — `bible/world/OctoClock.md`
- 2026-07-03/04 [day-range] Serendipity pairs: Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth, FUWAMOCO–Raora — `bible/world/hololive--Advent.md` ([Official S7, S10])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: day 1 "SUPERNOVA SUPER GIRL" (Justice); Autofister (Gigi & Cecilia, "CCGG MADNESS"); "HELP!!" (Kobo Kanaeru with Bae and Elizabeth); "Break It Down" (Vestia Zeta with Shiori and Cecilia); "Cloudy Sheep" (Tsunomaki Watame with Calli and Cecilia). Day 2: the Advent+Justice medley ("Rebellion," "ABOVE BELOW"); Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"); "MAKE IT, BREAK IT" (Zeta, FUWAMOCO and Gigi); "What an amazing swing" (Watame with Kiara and Raora); B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari") — `bible/world/hololive--Justice.md` ([Official S6, S8])
- 2026-07-03/04 PDT [day-range, PDT] **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) — `bible/world/hololive-History-2023-2026.md`
- 2026-07/08 [month-range] Shiori's original motion comic "Into The Void" (with Elizabeth, Gigi, Nerissa); Advent's 3rd-anniversary 3D live "Bound by Fate"; FUWAMOCO announce their first album (08-29) — `bible/world/hololive-History-2023-2026.md`
- 2026-07-23 [day] Rhythm game "hololive Dreams" released — `bible/world/hololive-History-2023-2026.md`
- 2026-07-03/04 [day-range] hololive English 4th concert "Serendipity" (LA) — `bible/world/hololive.md`

### 2026-08
- 2026-08-29 [day] First album "FUWAMOCO à la mode" announced — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2026; X via wiki])
- 2026-08 [month] 5th anniversary: her 1st concert "REGALIA" (2026-12-01, after the baseline) and 2nd album "Mirror Mirror" announced (timing per a contemporaneous secondary report); original "I found me" — `bible/characters/Hakos-Baelz.md` ([Official HB7] [Observed HB2])
- 2026-08-23 [day] Announced: "I found me," with lyrics by Bae (composition and arrangement by Tomomichi Takuma of Dream Monster), and her second album "Mirror Mirror," scheduled for 2026-11-02 (after the baseline: an announcement only). — `bible/characters/Hakos-Baelz.md` ([Official NEW-R2-017])
- 2026-08-22 [day] Announced hololive Koshien 2026: Koyori is organizer and one of six team managers (others include Houshou Marine and Shirogane Noel); the main competition is scheduled for 10-17/18 (after the baseline: an announcement only). — `bible/characters/Hakui-Koyori.md` ([Member announcement NEW-R6-017])
- 2026-08-23 [day] Puyo Puyo Tetris 2 coaching collab with FUWAMOCO — `bible/characters/Hoshimachi-Suisei.md` ([S1, secondary metadata: https://ckworks.jp/vinforadar/video/i6_T0tiQIkE])
- 2026-08-30 [day] Original "GUM & DROP"; more fan meetings and a December concert with tuki. announced — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2026-08 [month] 7th anniversary and a new 3D costume (08-11); single "Kyapi" (08-12) — `bible/characters/Houshou-Marine.md` ([Observed MA2 §2026, §Discography])
- 2026-08 [month] First solo original song, "Vivid Cute" (premiered around her birthday, 08-27; available digitally 08-28) — `bible/characters/Kikirara-Vivi.md` ([Official music 808] [Observed VI2])
- 2026-08-22 [day] Anime NYC: an announced convention-exclusive stream with Fubuki and Mio — `bible/characters/Nakiri-Ayame.md` ([Official AY7])
- 2026-08-23 [day] EP "Way 2 U" (five tracks, including the earlier "Daydream") — `bible/characters/Ouro-Kronii.md`
- 2026-08 [month] Original song "KAGAMI YO KAGAMI" (official digital release 08-16) — `bible/characters/Shirogane-Noel.md` ([Official music 796])
- 2026-08-27 [day] Holo Koshien: she ran "Shirogane Gakuin," opening with player creation and naming and following the team through its seasons into September. — `bible/characters/Shirogane-Noel.md` ([Archive metadata NEW-R5-015])
- 2026-08-26 [day] NePoLaBo and Secret Society holoX release their joint original "Watcha Gatcha!!!!!!!!" — `bible/characters/Shishiro-Botan.md` ([Official NEW-R6-004])
- 2026-08-01 [day] A "rare" La+ and Lui talk with new outfits — `bible/characters/Takane-Lui.md` ([LU4])
- 2026-08-15 [day] First album "Fleur de neige" announced for 2027-01-27 (after the baseline) — `bible/characters/Yukihana-Lamy.md` ([Observed LM2])
- 2026-08-29 [day] First album "FUWAMOCO à la mode" announced — `bible/world/FUWAMOCO.md`
- 2026-08-30 [day] "Ichizutte Trend♡" — `bible/world/FUWAMOCO.md` ([Official NEW-R3-019])
- 2026-08-22 [day] Anime NYC: an announced convention-exclusive stream — `bible/world/JP-Senpai-Pairs.md`
- 2026-08-02 [day] Group song "Spotlight" — `bible/world/hololive--Advent.md` ([Official NEW-R3-001])
- 2026-08-09 [day] 3rd-anniversary 3D live "Bound by Fate" (archive calendar date; also linked from Nerissa's official profile) — `bible/world/hololive--Advent.md` ([Archive metadata NEW-R3-001])
- 2026-08/09 [month-range] Official -Justice- merch tie-ins: Bandai Namco Amusement America pop-up (2026-08-27), Pinfinity AR pins (2026-09-30) — `bible/world/hololive--Justice.md` ([Official S1 news])

### 2026-09
- 2026-09-20/21 [day-range] RosaMiA (with Aki Rosenthal and Ookami Mio): "Blossom Sinfonia," premiered 09-20 (reported), official digital release 09-21 — `bible/characters/AZKi.md` ([Observed AZ2] [Official AZ12])
- 2026-09-26 [day] Her first solo singing stream, a ROCK N' RAWR PARTY; the description calls her "just a fluffy dog doing her best to sing for you!" (written). — `bible/characters/Fuwawa-Abyssgard.md` ([Archive metadata NEW-R3-018])
- 2026-09-30 [day] Alum; her history stays part of Myth's shared memory — `bible/characters/Gawr-Gura.md` ([Adaptation])
- 2026-09-01 [day] "Here Comes the CHADCast," released with Mori Calliope and IRyS — `bible/characters/Hakos-Baelz.md` ([Official HB9])
- 2026-09-03 [day] [Secondary, pending primary confirmation] Reported casting as Monami Ichikawa in *Sucker for Love: Crush Landing*; a September playthrough on her channel is also reported. — `bible/characters/Hakos-Baelz.md` ([Secondary NEW-R2-018])
- 2026-09-07 [day] Branches merge into one "hololive"; her unit is hololive -Promise- — `bible/characters/Hakos-Baelz.md` ([Official HB1])
- 2026-09-28 [day] "PARADISE!", the hololive Dreams area theme: animated MV; Bae shares the vocal credit with Omaru Polka, Houshou Marine, Yukihana Lamy, Hakui Koyori, Kobo Kanaeru and Ichijou Ririka. Also announced that day: "REGALIA" at Kanadevia Hall, scheduled for 2026-12-01 (after the baseline: an announcement only). — `bible/characters/Hakos-Baelz.md` ([Secondary NEW-R2-019, press-release reproduction] [Official, 20260928-02-16])
- 2026-09-12 [day] Second album "Chemical Spark" and first solo concert "Dream Spark" (2026-12-22) announced — `bible/characters/Hakui-Koyori.md` ([Observed KO2])
- 2026-09-20 [day] A mirrored public post acknowledges a fan estimate that her own-channel livestream total passed 10,000 hours — `bible/characters/Hakui-Koyori.md` ([KO3])
- 2026-09-08 [day] Arena tour "Once Upon a Stellar" opens (Yokohama, Kobe, Nagoya, Fukuoka; to 11-12) — `bible/characters/Hoshimachi-Suisei.md` ([Observed SU2])
- 2026-09 [month] Holo Koshien series: a baseball team followed through successive in-game seasons; Koyori joined the 09-17 session and AZKi commentated on 09-26. — `bible/characters/Houshou-Marine.md` ([Archive metadata NEW-R5-014, NEW-R5-006])
- 2026-09-07 [day] Branch merger; her unit is "hololive -Promise-" — `bible/characters/IRyS.md` ([Observed R2])
- 2026-09-07 [day] The branches merge into one "hololive." Her unit is now hololive -Myth-. — `bible/characters/Mori-Calliope.md` ([Official C17, C1])
- 2026-09-19 PDT [day, PDT] Myth 6th Anniversary 3D LIVE "Seasons From Within" with Kiara and Ina; the Myth song "THIS IS MYTH" premieres — `bible/characters/Mori-Calliope.md` ([Archive metadata C33])
- 2026-09-19 [day] Digital release of "BANZAI☆MANKAI." — `bible/characters/Nakiri-Ayame.md` ([Official NEW-R5-008])
- 2026-09-07 [day] Branches merge; her unit is hololive -Myth- — `bible/characters/Ninomae-Inanis.md` ([Official I28] [Observed I10])
- 2026-09-19 PDT [day, PDT] Myth 6th Anniversary 3D LIVE "Seasons From Within" with Calli and Kiara; "THIS IS MYTH" premieres — `bible/characters/Ninomae-Inanis.md` ([Archive metadata I32])
- 2026-09-19 [day] Original single "Stardust Capsule" (hololive catalogue CVRD-824). — `bible/characters/Ninomae-Inanis.md` ([Official NEW-R1-011])
- 2026-09-07 [day] Branches merge into one "hololive"; unit is hololive -Promise- — `bible/characters/Ouro-Kronii.md` ([Official K5, K1])
- 2026-09-21 [day] "Glitch Through," a new solo song for the hololive Dreams event "A Dreamy Summer Escape" (her chapter); the game's event story is a separate fictional production. — `bible/characters/Shiori-Novella.md` ([Official partner press release NEW-R3-005])
- 2026-09-14 [day] She organized and hosted the ShishiDori Cup, a hololive Dreams competition with 27 participants in nine teams, combining rhythm-game and chase-game challenges. — `bible/characters/Shishiro-Botan.md` ([Archive metadata NEW-R6-001])
- 2026-09-19 [day] First album "BOTAN.EXE" opened for orders; original "Stray & Stay" — `bible/characters/Shishiro-Botan.md` ([Observed BO2] [Distributor listing])
- 2026-09-26/27 [day-range] NePoX events with Secret Society holoX — `bible/characters/Shishiro-Botan.md` ([LM4 Ml1tM8S40p0])
- 2026-09-07 [day] Branches merge; unit is hololive -Myth- — `bible/characters/Takanashi-Kiara.md` ([Official T20, T1])
- 2026-09-19 PDT [day, PDT] Myth 6th Anniversary 3D LIVE "Seasons From Within" with Calli and Ina; "THIS IS MYTH" premieres — `bible/characters/Takanashi-Kiara.md` ([Archive metadata T25])
- 2026-09-05 [day] GreyScaleX (Shiori and Zeta) "Purrfect Pair" merchandise opens — `bible/world/Advent-Pairs.md` ([Official S7])
- 2026-09-19 PDT [day, PDT] Myth 6th anniversary 3D live "Seasons From Within": a Calli–Kiara duet cover and the new Myth song "THIS IS MYTH" — `bible/world/TakaMori.md`
- 2026-09-19 PDT [day, PDT] At Myth's 6th-anniversary 3D live "Seasons From Within" the two sang a duet cover of "September" — `bible/world/TakoTori.md`
- 2026-09-07 [day] Branches merge; COVER says it will update members' designs to fit their personalities, activities and future directions — `bible/world/VTuber-Persona-and-Lore.md`
- 2026-09 [month] Renamed "hololive -Advent-" in the merger — `bible/world/hololive--Advent.md`
- 2026-09-19 PDT (09-20 JST) [day, PDT] Myth 6th Anniversary 3D LIVE "Seasons From Within" on the hololive English channel with Calli, Kiara and Ina; it premiered the new Myth original song "THIS IS MYTH," whose MV followed. Pair stages (setlist, secondary S5): Kiara and Ina, Calli and Kiara, Calli and Ina each sang a duet cover — `bible/world/hololive--Myth.md`
- 2026-09-07 [day] "hololive Next": the female-talent branches unify under **hololive**; new logo; members to get updated designs (Tokino Sora first); "hololive raku" app; TV anime "Odeholo"; 10th-anniversary countdown — `bible/world/hololive-History-2023-2026.md`
- 2026-09-18 [day] New unit ASOBI★MAWARI-TAI! reveals its four members (Hyakuto Kyoko, Achichi Mela, Suzuna Tsuzuri, Sorashina Sopia) — `bible/world/hololive-History-2023-2026.md`
- 2026-09-19 PDT [day, PDT] Myth 6th Anniversary 3D LIVE "Seasons From Within" (Calli, Kiara, Ina); new Myth song "THIS IS MYTH" — `bible/world/hololive-History-2023-2026.md`
- 2026-09-24/25 [day-range] ASOBI★MAWARI-TAI! debut — `bible/world/hololive-History-2023-2026.md`
- 2026-09-07 [day] The female-talent branches unify under "hololive" — `bible/world/hololive.md`

### 2026-10
- 2026-10-06 (upcoming) [day] IRyS's first solo concert "HOPE ||: Beyond the Stars" (Tokyo) — `bible/world/hololive-History-2023-2026.md`

### undated/lore
- Lore [lore] An ancient automaton built for eternal servitude (official); secondary lore places her origin in Immerheim; in a public joke she attributed her maid duties to an earlier Justice — `bible/characters/Cecilia-Immergreen.md` ([Official CI1] [X post CI6, secondary])
- Lore [lore] Keeper of "Nature," the second concept created by the gods; a druid with kirin blood — `bible/characters/Ceres-Fauna.md` ([Official F1])
- Lore [lore] The Scarlet Queen and Harbinger of Order from Great Exardia; joined hololive to keep an eye on Advent and to become an idol; human, and not royalty despite the title — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB1] [Observed EB2 §Lore, secondary])
- Lore [lore] Twin demonic guard dog from the Northwest Passage in the demon world; sealed in The Cell "for being a pain in the godly behind" — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW1] [Observed FW2 §Lore])
- Lore [lore] Descendant of Atlantis (now ruins); swam to land because it was "so boring down there"; bought her clothes at a beachside store, paying in seashells; talks to marine life — `bible/characters/Gawr-Gura.md` ([Official G1] [Observed G2 §Lore])
- Lore [lore] Age jokes put her "somewhere in the 9,000s," with varying numbers across exchanges (9,361, 9,927, 9,485…); no fixed age is adopted. June 20 marks her arrival on land, not a remembered birthday — `bible/characters/Gawr-Gura.md` ([Observed G2 §Gura's age and §Lore])
- Lore [lore] A gremlin "Chaser" from Freesia, "born and raised under the flag of Freedom" — `bible/characters/Gigi-Murin.md` ([Official GG1])
- Lore [lore] Chaos itself, "birthed by the world"; appointed chairperson of the Council by the gods, though she takes a hands-off approach; breaks rules and watches the aftermath; a rat by form, "chaos" by species; age unknown ("roll a dice"); born on 29 February (in fan-recorded lore, Kronii created leap years to hold her) — `bible/characters/Hakos-Baelz.md` ([Official HB1 (original lore)] [Observed HB2 §Lore, secondary])
- Lore [lore] A nephilim who was the embodiment of hope in "The Paradise," reawakened in an age of despair to deliver hope through song — `bible/characters/IRyS.md` ([Official R1])
- Lore [lore] Jewel of Emotions; imprisoned in secret after people fought over her; lured in with cake — `bible/characters/Koseki-Bijou.md` ([Official KB1] [Observed KB2 §Lore])
- Lore [lore] Founder of Secret Society holoX; vast power, now sealed — `bible/characters/Laplus-Darknesss.md` ([Official LA1])
- Lore [lore] Younger twin demonic guard dog; in the prison break she barked at the guards and threw Pero at them — `bible/characters/Mococo-Abyssgard.md` ([Official MC1] [Observed MC2 §Lore])
- Lore [lore] She is the Grim Reaper's first apprentice. Modern medicine hurt the reaping business, so she turned to VTubing to harvest souls. — `bible/characters/Mori-Calliope.md`
- Lore [lore] She comes from an Underworld that looks like a modern city; she blamed debut lag on its bad internet. She waitressed there to save up for a trip to Japan. — `bible/characters/Mori-Calliope.md`
- Lore [lore] An oni from the Underworld Academy, its student council president; she pranks people with will-o'-the-wisps — `bible/characters/Nakiri-Ayame.md` ([Official AY1])
- Lore [lore] Guardian of "Civilization," the concept made by mankind rather than the gods; chose an owl form; has forgotten her name and age — `bible/characters/Nanashi-Mumei.md` ([Official M1] [Observed M2 §Lore])
- Lore [lore] A cat raised by an old woman who runs an onigiri shop; she formerly streamed from the computer in that woman's room (official lore, past tense) — `bible/characters/Nekomata-Okayu.md` ([Official OK1])
- Lore [lore] The Demon of Sound, sealed by the gods in The Cell; one horn broken to limit her power; escaped with Advent — `bible/characters/Nerissa-Ravencroft.md` ([Official N1] [Observed N2 §Lore])
- Lore [lore] Picked up a strange book, gained tentacle powers and began hearing Ancient Whispers; VTubes "to deliver random sanity checks on humanity, as an ordinary girl" — `bible/characters/Ninomae-Inanis.md` ([Official I1])
- Lore [lore] Warden of "Time", the third concept created by the gods and the one most tied to humankind — `bible/characters/Ouro-Kronii.md`
- Lore [lore] A big cat from the Romance Empire who prepares Justice's criminal reports; sent after FUWAMOCO, she got distracted by crane games — `bible/characters/Raora-Panthera.md` ([Official RP1] [Observed RP2 §Lore])
- Lore [lore] The Archiver; imprisoned in The Cell for forbidden knowledge; masterminded Advent's prison break — `bible/characters/Shiori-Novella.md` ([Official SN1] [Observed SN2 §Lore])
- Lore [lore] Phoenix idol who dreams of owning a fast-food chain; reborn from her ashes — `bible/characters/Takanashi-Kiara.md` ([Official T1])
- Lore [lore] CEO of KFP (Kiara Fried Phoenix); employees are chickens; the Usual Room; she denies KFP is a cult — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §KFP, secondary])
- Lore [lore] holoX's executive officer and point of contact — `bible/characters/Takane-Lui.md` ([Official LU1])
- Lore (secondary-reported; original statements and continuity scope unverified; outside the baseline) [lore] Born circa the early 1920s and thrown forward in time; the pocket watch holds a time crystal; time travel makes loud screeching noises and can cause headaches; she won't use it to cheat — `bible/characters/Watson-Amelia.md` ([Observed A2 §Time travel, secondary])
- Lore [lore] Became an idol "just out of interest" after rumors of unusual beings in hololive; trains reflexes with shooters and her mind with puzzle games — `bible/characters/Watson-Amelia.md` ([Official A1])

# Task 05 — Cross-cohort bridge audit

You are GPT, senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only, answer in English,
and run sequentially without parallel GPT audits.

Bridge: ties (external participants only)
Packet: projects/holoen/research/qa/packets/ties-external.md (inline below)
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

## Scope of this ties pass (Claude, 2026-10-02)

This pass covers **external participants**: people without a card (JP/ID members, DEV_IS, guests, alumni of
other branches) as they appear across all cohorts, using the packet `ties-external.md`. Cast-to-cast pairs and
claims naming more than three people are compared from both sides by the cohort audits, whose
packets hold every outgoing and incoming claim for their members (see `research/qa/audit-*.md`); a separate
cast-ties pass would repeat that work and does not fit the remaining quota. If you see a cross-cohort tie
problem the cohort audits could not have caught, report it here; say in Merge handoff whether a further pass
is needed and what it would cover.

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
| AUDIT-PROMISE | Cohort audit promise (Kronii, IRyS, Fauna, Mumei, Bae and pair cards) | applied; PROMISE-QUOTE-001 adapted to the two-model shared span; one CONSULT-P1-006 row not applied (both models share the longer span) | 2026-10-04 merge |
| AUDIT-BRIDGE-EVENTS | Bridge audit of dates, zones and status | applied; registry rows fixed in tools/qa_packets.py (date parser) and by regeneration | 2026-10-04 merge |

### Registry excerpt (units and reference-only people; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "93327bb",
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

### projects/holoen/research/qa/packets/ties-external.md

# Bridge packet: ties (cast × reference-only people)

Snapshot: git 93327bb. Every [SW] sentence and dossier row/bullet that names both people, grouped by
pair (names and short names matched; a sentence naming three people appears under each pair).

### AZKi × Amane Kanata
- `bible/characters/Sakamata-Chloe.md › Background Timeline`: | 2024 | "Magical Girl holoWitches!" single (05-30); "Kanaken" 3D live with Kanata and AZKi | [Observed CH2] [CH4] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | AZKi | "Kanaken" with Amane Kanata | Minecraft construction "company," Chained Together and a 3D live (2024) | [CH4] [CH2] |
- `bible/characters/Sakamata-Chloe.md › [SW] Background`: Minecraft company with Amane Kanata and AZKi (a 3D live in 2024), and concluded her regular activities on 2025-01-26, holding a graduation live and remaining an affiliate; a secondary record has her singing "Sparkle" at Murasaki Shion's graduation live (2025-04-26).
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: AZKi: "Kanaken" with Amane Kanata (Minecraft, Chained Together, a 3D live, 2024).
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: (2025), formed KoZMy with AZKi and Koyori (2025, per a collab title and secondary listings) and, per secondary records, is in KALAZ with Amane Kanata and AZKi.

### AZKi × Inugami Korone
- `bible/characters/AZKi.md › Relationship Map`: | La+ Darknesss | — | GeoGuessr for Tochigi Day (2025-06-15), The Headliners with Korone and Miko (2025-05-07), Minecraft (2025-07); a clip of La+ reacting to AZKi's ASMR (2026-03-31) | [AZ4 80Xb4PxZLyw, AMturrbpVD0] [La+ channel z0Z2Zc3MlE4, 6n2X82dqqx0] |

### AZKi × Moona Hoshinova
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2022-12-31 | "story time" as Star Flower with AZKi, Moona Hoshinova and IRyS | [Official SU6] |

### AZKi × Oozora Subaru
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | AZKi | JP kouhai | A player in AZKi's 3D pun-ASMR contest (2025-06-22), alongside Okayu, Subaru and Kanade. | [Archive metadata NEW-R5-004] |

### Airani Iofifteen × Gigi Murin
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Airani Iofi (ID), Pavolia Reine (ID) | "Fanfic Club" with Gigi | Monster Hunter Wilds with Iofi and Jurard (2025) | [Observed SN2; SN3] |
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club."

### Airani Iofifteen × Takane Lui
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Takane Lui: Apex with Airani Iofifteen (2022).

### Airani Iofifteen × Watson Amelia
- `bible/characters/Takane-Lui.md › Relationship Map`: | Watson Amelia (affiliate) | — | Apex with Airani Iofifteen (2022-01-19) | [LU5 Mory0I9vXtI] |
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Watson Amelia (affiliate): Apex with Iofi (2022).

### Akai Haato × Takane Lui
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Takane Lui, Tokoyami Towa, Akai Haato | JP seniors | "【MUMEI + LUI】Q&A With Bird Sisters !!!" (2025-04-19); Towa calls her "Mumi-chan"; Minecraft "Peace & Love with HAACHAMA" (2025) | [Observed M2 infobox; M3] |

### Amane Kanata × Hakui Koyori
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: (2025), formed KoZMy with AZKi and Koyori (2025, per a collab title and secondary listings) and, per secondary records, is in KALAZ with Amane Kanata and AZKi.

### Amane Kanata × Kazama Iroha
- `bible/characters/AZKi.md › [SW] Relationships`: Amane Kanata and Kazama Iroha: collaborators associated with KanatAZ and AzuIro ("AZUIRO BESTIE DAYS," 2025).

### Amane Kanata × Sakamata Chloe
- `bible/characters/AZKi.md › Relationship Map`: | Sakamata Chloe (affiliate) | "Kanaken" with Amane Kanata | Minecraft construction "company," Chained Together and a 3D live (2024) | [Chloe file CH4] |
- `bible/characters/AZKi.md › [SW] Relationships`: Sakamata Chloe: "Kanaken" with Kanata (Minecraft and a 3D live, 2024).
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | Sakamata Chloe (affiliate) | — | Rust with Kanata (2022-09); a self-knowledge quiz collab (2025-01-18) | [Chloe file z55R0Z8_qk0] [LM4 9DMCTQDpBos] |
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: Sakamata Chloe (affiliate): Rust with Amane Kanata (2022).

### Amane Kanata × Yukihana Lamy
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Yukihana Lamy | — | Rust with Kanata and Lamy (2022) | [CH4] |
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Yukihana Lamy: Rust with Kanata (2022).

### Anya Melfissa × Mori Calliope
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2024-09-15 | A pop-up Mario Party with Mori Calliope, Anya Melfissa and Hiodoshi Ao (archived metadata) | [OK4 WnKCmQ2iXww] |
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Mori Calliope: a pop-up Mario Party with Anya and Ao (2024).

### Ayunda Risu × Hakos Baelz
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kobo Kanaeru, Ayunda Risu | ID seniors | "HELP!!" with Kobo and Hakos Baelz at Serendipity (2026); Kobo calls her "Lilis" (secondary); LYRA and "ALiCE&u" with Risu | [Observed EB2] [Official EB5, EB8] |

### Banzoin Hakka × Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Banzoin Hakka (HOLOSTARS) | Duet partner | A "Mephisto" cover (2025-01-18); archived credits list Elizabeth's production and vocal-arrangement work | [Observed EB3, archived credits] |

### Cecilia Immergreen × Natsuiro Matsuri
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2026-03-06–08 JST | hololive 7th fes. "Ridin' on Dreams": "Idol" as the final solo number of STAGE 3 (her own choreography with a breakdance finish, by her account) and "Kakumei Dualism" with Natsuiro Matsuri; a venue talk with Cecilia Immergreen (her account) | [Official HB11 lineup] [secondary setlist HB12] [ASR HB20] |

### Cecilia Immergreen × Oozora Subaru
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-08-23/24 | -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora | [Official KB5] |

### Cecilia Immergreen × Vestia Zeta
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity.
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice and "CCGG MADNESS" as Autofister with Cecilia (day 1); "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official GG4, GG9] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Mococo / FUWAMOCO | Advent ("GigiMoco," "bauBau"; secondary) | Secondary accounts: with Cecilia, a guest-host prank on FUWAMOCO MORNING #167 (2025-07-28); "Bright Tonight" (2025) and "MAKE IT, BREAK IT" with Zeta at Serendipity (2026) with both twins | [Observed GG2; Mococo file] [Official GG7, GG9] |
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Cecilia and Vestia Zeta: "Break It Down" at Serendipity.

### Ceres Fauna × Tsukumo Sana
- `bible/characters/Ceres-Fauna.md › Relationship Map`: | Tsukumo Sana | Council genmate (graduated 2022) | Sana designed the Council's "Beeg Smol" models; Fauna: "Go give [Sana] lots of love because she deserves it, even though she's a little bit... disgusting." | [Observed F2 §Quotes, secondary] |
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke.

### Elizabeth Rose Bloodflame × Inugami Korone
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Elizabeth Rose Bloodflame | — | "IT'S LOVE" cover with Elizabeth and Korone for Elizabeth's 2026 birthday (2026-05-12) | [MA5 iwnHChZq0N8] |
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Elizabeth Rose Bloodflame: "IT'S LOVE" with Korone for Elizabeth's 2026 birthday.
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Elizabeth Rose Bloodflame:** "IT'S LOVE" with Marine and Inugami Korone for Elizabeth's 2026 birthday. [S1]

### Elizabeth Rose Bloodflame × Kobo Kanaeru
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: BaeRyS with IRyS ("LUVATORRRRRY!"), "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame (day 1) | [Official HB4, HB5] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Elizabeth Rose Bloodflame | Justice kouhai | "HELP!!" with Kobo Kanaeru at Serendipity (2026) | [Official HB5] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Kobo Kanaeru (ID) | Cross-branch | "Ai ni" at the World Tour '24 Taipei finale (2025-01-18); "HELP!!" with Elizabeth at Serendipity (2026) | [Official HB6, HB5] |
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Elizabeth Rose Bloodflame and Kobo Kanaeru: "HELP!!" at Serendipity.
- `bible/world/Hakos-Baelz-Pairs.md › History`: | 2026-07-03/04 PDT | Serendipity: BaeRyS "LUVATORRRRRY!"; "HELP!!" | BaeRyS; Bae–Elizabeth (with Kobo) |
- `bible/world/Hakos-Baelz-Pairs.md › With Justice`: - **Elizabeth Rose Bloodflame:** "HELP!!" with Kobo Kanaeru at Serendipity (2026). [Official S3]

### Elizabeth Rose Bloodflame × Kureiji Ollie
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Elizabeth Rose Bloodflame and Kureiji Ollie (ID): "High Tide" at -All for One- (2025).

### Elizabeth Rose Bloodflame × Omaru Polka
- `bible/characters/Kazama-Iroha.md › Relationship Map`: | FUWAMOCO | — | A prefecture cookie-battle off-collab, FUWAMOCO as challengers (2024-10-27); "CHA-LA HEAD-CHA-LA" for Elizabeth with Watame, Nene and Polka (2026-05-19) | [IR4 JgOwJ7m89Lk] [IR5 xylll7Mp0jk] |

### Elizabeth Rose Bloodflame × Tsunomaki Watame
- `bible/characters/Kazama-Iroha.md › Relationship Map`: | FUWAMOCO | — | A prefecture cookie-battle off-collab, FUWAMOCO as challengers (2024-10-27); "CHA-LA HEAD-CHA-LA" for Elizabeth with Watame, Nene and Polka (2026-05-19) | [IR4 JgOwJ7m89Lk] [IR5 xylll7Mp0jk] |

### Elizabeth Rose Bloodflame × Vestia Zeta
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Vestia Zeta | ID senior | Sang "Giri Giri" with her at her 2025 3D showcase; Elizabeth arranged it as a duet, choreographed it and taught Zeta the dance  | [ASR EB20, Rk03Rh8P9ps 0:28:09–0:30:11; both models] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Vestia Zeta (ID): her duet partner for "Giri Giri" at her 2025 3D showcase, which Elizabeth arranged and choreographed.

### Fuwawa Abyssgard × Inugami Korone
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | FUWAMOCO (Fuwawa, Mococo) | kouhai she is a fan of | Her cameo at their 3D debut (2024); their watch-along of her 2025 solo concert ("respect to our sultry cat senpai"); a 2025 short with Korone | [FUWAMOCO card] [OK5] |

### Gavis Bettel × Shiori Novella
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Shiori Novella | Advent senior ("NovelFlame," "BloodQuill," secondary) | Credited in Shiori's non-canon motion comic "Into The Void" (2026); R.E.P.O. with Shiori, Flayon, Jurard and Gavis Bettel (2025) | [Observed EB2, EB3] |

### Gawr Gura × Pavolia Reine
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Gawr Gura** (graduated): "Apex Predators" (Shishiro Botan), UMISEA, "SharPea" (Pavolia Reine), and Murasaki Shion (Minecraft and Mario Kart in 2021; a "Renai Circulation" duet cover, 2022). [Observed S1; S2 Gura]

### Gawr Gura × Usada Pekora
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2024-07-05 | hololive night at Dodger Stadium with Usada Pekora and Gawr Gura | [Official SU7] |
- `bible/world/JP-Senpai-Pairs.md › History`: | 2024-07-05 | hololive night at Dodger Stadium | Suisei, Gura, Pekora |
- `bible/world/JP-Senpai-Pairs.md › Hoshimachi Suisei with the cast`: - **Gawr Gura (graduated):** Suisei, Gura and Usada Pekora were the three faces of "hololive night" at Dodger Stadium (2024-07-05), on the big screen at the first pitch and in the drone show. [Official S4]

### Gigi Murin × Kureiji Ollie
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Hakos Baelz, Kureiji Ollie (ID) | Senior; cross-branch | "Countach" at -All for One- (2025); with Bae, a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025-02-05), UNO on Bae's 24-hour stream (2024-11-25) and Gigi's 2025 Spring Party with FUWAMOCO and Bae (2025-03-31); Ollie's part is "Countach" only | [Official GG5] [Bae file HB3, HB5, HB8, HB20] |
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Hakos Baelz: "Countach" with Kureiji Ollie (ID) on stage (2025), a dramatic reading of A Midsummer Night's Dream on Bae's stream, and Gigi's 2025 Spring Party with FUWAMOCO and Bae.
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "R x R x R" with Calli; "Countach" with Gigi and Kureiji Ollie; solo "La Roja (Arrange ver.)" | [Official HB5] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Gigi Murin | Justice kouhai | "Countach" with Kureiji Ollie at -All for One- (2025); a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025); UNO on #BaeTV24; Gigi's 2025 Spring Party with FUWAMOCO and Bae | [Official HB5] [Observed HB3; HB8] |
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Gigi Murin: "Countach" with Kureiji Ollie (2025); a Midsummer Night's Dream reading.
- `bible/world/Hakos-Baelz-Pairs.md › With Justice`: - **Gigi Murin:** "Countach" with Kureiji Ollie at -All for One- (2025); a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025-02-05); UNO on the 24-hour stream. [Official S3] [S1]

### Gigi Murin × Pavolia Reine
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Airani Iofi (ID), Pavolia Reine (ID) | "Fanfic Club" with Gigi | Monster Hunter Wilds with Iofi and Jurard (2025) | [Observed SN2; SN3] |
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club."

### Gigi Murin × Vestia Zeta
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity.
- `bible/characters/Gigi-Murin.md › [SW] Background`: (Gigi helped with the lyrics and designed the chibi models) and sang it at the Serendipity concert, where Gigi also sang "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO.

### Hakos Baelz × Kobo Kanaeru
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kobo Kanaeru, Ayunda Risu | ID seniors | "HELP!!" with Kobo and Hakos Baelz at Serendipity (2026); Kobo calls her "Lilis" (secondary); LYRA and "ALiCE&u" with Risu | [Observed EB2] [Official EB5, EB8] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Kobo Kanaeru and Hakos Baelz: "HELP!!" at Serendipity.
- `bible/world/Hakos-Baelz-Pairs.md › History`: | 2026-07-03/04 PDT | Serendipity: BaeRyS "LUVATORRRRRY!"; "HELP!!" | BaeRyS; Bae–Elizabeth (with Kobo) |

### Hakos Baelz × Kureiji Ollie
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Hakos Baelz, Kureiji Ollie (ID) | Senior; cross-branch | "Countach" at -All for One- (2025); with Bae, a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025-02-05), UNO on Bae's 24-hour stream (2024-11-25) and Gigi's 2025 Spring Party with FUWAMOCO and Bae (2025-03-31); Ollie's part is "Countach" only | [Official GG5] [Bae file HB3, HB5, HB8, HB20] |
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Hakos Baelz: "Countach" with Kureiji Ollie (ID) on stage (2025), a dramatic reading of A Midsummer Night's Dream on Bae's stream, and Gigi's 2025 Spring Party with FUWAMOCO and Bae.
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Gigi Murin | Justice kouhai | "Countach" with Kureiji Ollie at -All for One- (2025); a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025); UNO on #BaeTV24; Gigi's 2025 Spring Party with FUWAMOCO and Bae | [Official HB5] [Observed HB3; HB8] |
- `bible/world/Hakos-Baelz-Pairs.md › BaeRyS`: - **Together:** a 2023 off-collab and the "Daikirai na Hazu Datta" cover (2023); a Valentine bento cooked on handcam (2024-02-14); HoloEarth with Kureiji Ollie (2024); a New Year's countdown off-collab watch-along (2024-12-31); Snow Bros. 2 (2025-04-17); Mario Party with Raora on Bae's 24-hour stream (2024-11-25). [S1]

### Hakos Baelz × Momosuzu Nene
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2023-04-22 | "BAE-GEMITE DOMINATION" episode 4 with Bae and Momosuzu Nene | [KO5 WwjB7QSmQng] |

### Hakos Baelz × Moona Hoshinova
- `bible/characters/IRyS.md › Relationship Map`: | Hakos Baelz | Promise unitmate ("BaeRyS") | The married/divorced running bit; Bae once banned her from soda for a week after a lost bet; a 2023 off-collab and the "Daikirai na Hazu Datta" cover (2023); "High Tide" with Moona Hoshinova and Hoshimachi Suisei (2024); BaeRyS at Serendipity (2026) | [Observed R2 §Relationships, §Likes and dislikes] |

### Hakos Baelz × Ookami Mio
- `bible/characters/IRyS.md › [SW] Relationships`: At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou.

### Hakos Baelz × Oozora Subaru
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Hakos Baelz | — | "BAE-GEMITE DOMINATION" episode 4 with Nene (2023-04-22); a "KHAOS KITCHEN" taste tester with Calli and Oozora Subaru (2023-11-24) Co-credited singers on the hololive Dreams theme "PARADISE!" (MV 2026-09-28; seven singers). | [KO5 WwjB7QSmQng, NdLiUW-nUlk] [Secondary, dengekionline 202609/89494] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Hakos Baelz | — | BAE-GEMITE DOMINATION #2 with Subaru (2023) | [BO5] |
- `bible/characters/Shishiro-Botan.md › Voice Profile`: - **Language:** streams in Japanese; archived metadata records her on Calli's HOLOYOI #03 and Bae's BAE-GEMITE DOMINATION #2 (2023), both with Oozora Subaru. [BO5]
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: Hakos Baelz: BAE-GEMITE DOMINATION #2 with Subaru (2023).
- `bible/world/JP-Senpai-Pairs-2.md › Shishiro Botan with the cast`: - **Mori Calliope, Hakos Baelz:** HOLOYOI #03 and BAE-GEMITE DOMINATION #2, both with Oozora Subaru (2023). [S1]

### Hakos Baelz × Roboco
- `bible/characters/Kikirara-Vivi.md › Background Timeline`: | 2025-05-25 | #holoREPO with FUWAMOCO, Bae, Roboco, Towa and Hajime | [VI5 Z5cpzbdsLDE, TgMVtjXW2Ms] |
- `bible/world/JP-Senpai-Pairs-2.md › Kikirara Vivi with the cast`: - **FUWAMOCO, Hakos Baelz:** #holoREPO with Roboco, Towa and Hajime (2025-05-25). [S1]

### Hakui Koyori × Shirakami Fubuki
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | FUWAMOCO | "FUWAMOKOYO" (Koyori and the twins; FUWAMOCO Morning title) | FUWAMOCO Morning guest (2024-04-26); separately, Lethal Company with Shirakami Fubuki (2024-03-09); a guest at their birthday concert (2025) | [KO5 gCYXKgYcFmk, XR1PEtj15kE, ouQF2A1l_cI] |

### Hiodoshi Ao × Hoshimachi Suisei
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Hoshimachi Suisei | "MOMAS" | With Sakura Miko, Houshou Marine and Hiodoshi Ao; PlateUp! on her 2025 team | [OK2] [OK4] |

### Hiodoshi Ao × Houshou Marine
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Nekomata Okayu | "MOMAS" (secondary label) | With Sakura Miko, Houshou Marine and Hiodoshi Ao; on Okayu's 2025 New Year Game Festival team (secondary roster) | [SU2] [S1] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Hoshimachi Suisei | "MOMAS" | With Sakura Miko, Houshou Marine and Hiodoshi Ao; PlateUp! on her 2025 team | [OK2] [OK4] |

### Hiodoshi Ao × Mori Calliope
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2024-09-15 | A pop-up Mario Party with Mori Calliope, Anya Melfissa and Hiodoshi Ao (archived metadata) | [OK4 WnKCmQ2iXww] |

### Hiodoshi Ao × Nekomata Okayu
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Nekomata Okayu | "MOMAS" (secondary label) | With Sakura Miko, Houshou Marine and Hiodoshi Ao; on Okayu's 2025 New Year Game Festival team (secondary roster) | [SU2] [S1] |

### Hoshimachi Suisei × Moona Hoshinova
- `bible/characters/AZKi.md › Background Timeline`: | 2022-12-31 | "story time" as Star Flower with Suisei, Moona Hoshinova and IRyS | [Official AZ6] |
- `bible/characters/IRyS.md › Relationship Map`: | Hakos Baelz | Promise unitmate ("BaeRyS") | The married/divorced running bit; Bae once banned her from soda for a week after a lost bet; a 2023 off-collab and the "Daikirai na Hazu Datta" cover (2023); "High Tide" with Moona Hoshinova and Hoshimachi Suisei (2024); BaeRyS at Serendipity (2026) | [Observed R2 §Relationships, §Likes and dislikes] |
- `bible/world/Hakos-Baelz-Pairs.md › BaeRyS`: - **On stage:** "High Tide" with Moona Hoshinova and Hoshimachi Suisei at -Breaking Dimensions- (2024); the official unit BaeRyS at Serendipity (2026), "LUVATORRRRRY!", their first duo stage. [Official S3]

### Hoshimachi Suisei × Omaru Polka
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Hoshimachi Suisei | "Shiranui Kensetsu" (Shiraken) | A Minecraft construction company with Flare, Polka and Miko | [NO2] |

### Hoshimachi Suisei × Rikka
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Calli collaborates with Hoshimachi Suisei: Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones"

### Hoshimachi Suisei × Shirakami Fubuki
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Suisei, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024).

### Hoshimachi Suisei × Shiranui Flare
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Shiranui Flare: "Shiranui Kensetsu," where Suisei is the PR director.

### Hoshimachi Suisei × Usada Pekora
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Hoshimachi Suisei and Usada Pekora: fellow featured talents in the July 5, 2024 hololive night collaboration with the Los Angeles Dodgers.
- `bible/world/JP-Senpai-Pairs.md › History`: | 2024-07-05 | hololive night at Dodger Stadium | Suisei, Gura, Pekora |
- `bible/world/JP-Senpai-Pairs.md › Hoshimachi Suisei with the cast`: - **Gawr Gura (graduated):** Suisei, Gura and Usada Pekora were the three faces of "hololive night" at Dodger Stadium (2024-07-05), on the big screen at the first pitch and in the drone show. [Official S4]

### Houshou Marine × Inugami Korone
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: Houshou Marine and Shirogane Noel: "Yakamashi Musume" with Inugami Korone (archived metadata), and Blue Journey; Marine is also in holoWitches.
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Elizabeth Rose Bloodflame:** "IT'S LOVE" with Marine and Inugami Korone for Elizabeth's 2026 birthday. [S1]

### Houshou Marine × Kobo Kanaeru
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Takanashi Kiara:** Marine was the first guest of Kiara's HOLOTALK (2020-11-20, "#marinarasauce"); Kiara danced "MIRAGE" with her (2024) and to Marine and Kobo's "III." [S1]

### Houshou Marine × Oozora Subaru
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Houshou Marine, Oozora Subaru | JP seniors | Early HOLOTALK guest (Marine); first EN×JP collab (Subaru, 2020) | [Observed T2 §2020, secondary] |

### Houshou Marine × Shiranui Flare
- `bible/characters/Shirogane-Noel.md › [SW] Background`: She debuted on 2019-08-08 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Houshou Marine.

### Houshou Marine × Usada Pekora
- `bible/characters/Kikirara-Vivi.md › Background Timeline`: | 2026 | FLOW GLOW's self-titled album (01-21, including "PUNISHER" and "the light"); first on-stream Super Mario Bros. 3 and Super Mario World playthroughs; Getting Over It, a gift from Pekora (07-25); 700,000 subscribers during an endurance karaoke (08-11, secondary); FLOW GLOW's "magic summer" (08-18); MVP's "Hatsukoi Cider" with Marine and Pekora (09, secondary record) | [Official music 024] [VI4] [Observed VI2] [MVP upload record] |
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Houshou Marine | "MVP" with Pekora | An archived 2026 performance record ("Hatsukoi Cider") names the trio | [VI2] [MVP upload record] |
- `bible/characters/Kikirara-Vivi.md › [SW] Background`: She plays games with Usada Pekora ("PekoVivi," secondary), and an archived 2026 performance record names Marine, Vivi and Pekora as MVP.
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Houshou Marine: MVP with Pekora (an archived 2026 performance record).
- `bible/characters/Shirogane-Noel.md › [SW] Background`: She debuted on 2019-08-08 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Houshou Marine.
- `bible/world/JP-Senpai-Pairs-2.md › Among themselves`: - Marine and Vivi: "MVP" with Usada Pekora; an archived September 2026 "Hatsukoi Cider" upload record names the trio. [S2] [MVP upload record]

### IRyS × Inugami Korone
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2022-04-24 | Left 4 Dead 2 with IRyS, Takane Lui and Inugami Korone | [BO5 K1wStJxm4F0] |

### IRyS × Kaela Kovalskia
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Takane Lui: Minecraft with IRyS and Kaela (2022).
- `bible/characters/Takane-Lui.md › Relationship Map`: | IRyS, Ouro Kronii | — | Minecraft elytra hunting with Kaela (2022); IRyS danced to "Soar" (2026) | [LU5] |
- `bible/characters/Takane-Lui.md › [SW] Relationships`: IRyS and Ouro Kronii: Minecraft with Kaela (2022).
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Kronii and Kaela are recurring public collaborators. IRyS and Flare are recurring public collaborators.

### IRyS × Kobo Kanaeru
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2024–2025 | World Tour '24 -Soar!- performer (New York to Taipei; "Ai ni" with Kobo Kanaeru at the Taipei finale, 2025-01-18); holoMeet ambassador 2024; World Tour '25 Sydney show with Kronii and IRyS ("Dance Monkey" as Promise, 2025-07-12) | [Official HB6, HB10] [Observed Concerts card] |
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: BaeRyS with IRyS ("LUVATORRRRRY!"), "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame (day 1) | [Official HB4, HB5] |

### IRyS × Moona Hoshinova
- `bible/characters/AZKi.md › Background Timeline`: | 2022-12-31 | "story time" as Star Flower with Suisei, Moona Hoshinova and IRyS | [Official AZ6] |
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2022-12-31 | "story time" as Star Flower with AZKi, Moona Hoshinova and IRyS | [Official SU6] |

### IRyS × Ookami Mio
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.

### IRyS × Tsukumo Sana
- `bible/world/hololive--Promise.md › Members and Status`: - Council history: Tsukumo Sana graduated from -Council- on 2022-07-31, before Promise existed; she was never a Promise member. IRyS and the four remaining Council members formed Promise in October 2023.

### IRyS × Tsunomaki Watame
- `bible/characters/AZKi.md › Background Timeline`: | 2022-03-12 | Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame | [AZ5 32NVpmKdAOs] |
- `bible/characters/AZKi.md › Voice Profile`: - **Language:** streams in Japanese; she participated in Calliope's English lesson with IRyS and Watame (2022, archived metadata). [Observed AZ5]

### IRyS × Usada Pekora
- `bible/characters/Hakos-Baelz.md › [SW] Background`: A singer and dancer, she has released originals such as "PLAY DICE!", "PSYCHO", "RxRxR", "FEAST" and "SNAKE EYES," the album "ZODIAC," the EP "Pandæmonium" and "HIDE & SEEK" with Usada Pekora (2023); she co-hosts the CHADCast podcast with IRyS and Mori Calliope (their song "Here Comes the CHADCast," 2026) and holds "Febaerary," a month of daily streams before her birthday.

### Inugami Korone × La+ Darknesss
- `bible/characters/AZKi.md › Relationship Map`: | La+ Darknesss | — | GeoGuessr for Tochigi Day (2025-06-15), The Headliners with Korone and Miko (2025-05-07), Minecraft (2025-07); a clip of La+ reacting to AZKi's ASMR (2026-03-31) | [AZ4 80Xb4PxZLyw, AMturrbpVD0] [La+ channel z0Z2Zc3MlE4, 6n2X82dqqx0] |

### Inugami Korone × Mococo Abyssgard
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | FUWAMOCO (Fuwawa, Mococo) | kouhai she is a fan of | Her cameo at their 3D debut (2024); their watch-along of her 2025 solo concert ("respect to our sultry cat senpai"); a 2025 short with Korone | [FUWAMOCO card] [OK5] |

### Inugami Korone × Nanashi Mumei
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Beyond EN, Mumei recorded a duet cover with Inugami Korone in her last week.

### Inugami Korone × Nekomata Okayu
- `bible/characters/Fuwawa-Abyssgard.md › Background Timeline`: | 2024-08-10 PDT | 3D debut with a wrestling segment and cameos by Okayu and Korone | [Observed FW2 §2024] |
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Nekomata Okayu: secondary accounts report her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; archived metadata documents the twins' 2025 watch-along of her concert.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Nekomata Okayu: secondary accounts report her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; archived metadata documents the twins' 2025 watch-along of her concert.
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: FUWAMOCO: secondary accounts report Okayu's enthusiasm for the twins and her appearance with Korone at their 3D debut (2024); archived metadata documents the twins' 2025 watch-along of her concert.
- `bible/world/FUWAMOCO.md › History`: | 2024-08-10 PDT | 3D debut: a wrestling segment supervised by DDT Pro-Wrestling, Okayu and Korone cameos | "Lifetime Showtime" full version |
- `bible/world/JP-Senpai-Pairs.md › History`: | 2024-08-10 PDT | FUWAMOCO's 3D debut, Okayu and Korone cameos | FUWAMOCO–Okayu |
- `bible/world/JP-Senpai-Pairs.md › Nekomata Okayu with the cast`: - **FUWAMOCO:** secondary accounts report Okayu's enthusiasm for the twins and her appearance with Inugami Korone at FUWAMOCO's 3D debut (2024-08-10 PDT); FUWAMOCO watched Okayu's 2nd solo concert "PERSONYA RESPECT" together ("respect to our sultry cat senpai," 2025-05-28); a 2025 short of "3 dogs + 1 cat" with Korone and Okayu. [S1] [S2 Okayu, secondary] [FUWAMOCO card]
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2018-12 | hololive GAMERS (Fubuki, Mio; later Okayu, Korone) | Gaming senpai |

### Inugami Korone × Ninomae Ina'nis
- `bible/characters/Nekomata-Okayu.md › [SW] Background`: With the English cast she released "Kurukuru Cruise" with Ninomae Ina'nis (2025); secondary accounts document her appearing with Korone in FUWAMOCO's 3D debut (2024), and the twins hosted a 2025 watch-along of her concert.

### Inugami Korone × Shirogane Noel
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Shirogane Noel: hololive Fantasy genmate; the units Bara☆Dice and Yakamashi Musume (with Lamy and Inugami Korone, per archived metadata).
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: Houshou Marine and Shirogane Noel: "Yakamashi Musume" with Inugami Korone (archived metadata), and Blue Journey; Marine is also in holoWitches.

### Inugami Korone × Takane Lui
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | Takane Lui | "Onikan" (archived titles) | A sponsored collab billed おにかん (2025-08-09); secondary coverage also reports R.E.P.O. with Lui, Miko and Korone (2025) | [Lui channel YXaDmUXPSGo] [appbank.net report, secondary] |
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2022-04-24 | Left 4 Dead 2 with IRyS, Takane Lui and Inugami Korone | [BO5 K1wStJxm4F0] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Takane Lui | "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary) | Left 4 Dead 2 (2022); an Overwatch 2 team (2023). The "BLT" label was not verified in review | [BO2] [BO5] [Lui file] |
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: Takane Lui: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary); Left 4 Dead 2 (2022) and Overwatch 2 (2023) together.

### Inugami Korone × Yukihana Lamy
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Shirogane Noel: hololive Fantasy genmate; the units Bara☆Dice and Yakamashi Musume (with Lamy and Inugami Korone, per archived metadata).
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: (with Yukihana Lamy and Inugami Korone, per archived metadata); 3rd-gen R.E.P.O.

### Kaela Kovalskia × Koseki Bijou
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Kaela Kovalskia | ID senior ("SMITTEN"; "Graondstone" with Bijou; secondary) | Lethal Company, Don't Starve Together, Buckshot Roulette, PEAK; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement (secondary) | [Observed RP2, RP3] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Kaela Kovalskia ("SMITTEN"): co-op partner; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement; with Koseki Bijou they are "Graondstone."
- `bible/world/Advent-Pairs.md › Conflicts and Story Hooks`: 3. Kaela and Bijou build something enormous in silence while chat panics.
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Raora Panthera:** "Graondstone" with Bijou and Kaela; FUWAMOCO's 2026 Serendipity unit partner (B.F.F). [Official S6] [Observed S1]
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Of Advent: Bijou and Kaela Kovalskia are "Grindstone"

### Kaela Kovalskia × Nerissa Ravencroft
- `bible/world/Hakos-Baelz-Pairs.md › With Advent`: - **Shiori Novella, Nerissa Ravencroft:** shared EN projects rather than duo collabs: the 2024 "Mind Craft" cover with all then-active EN members; with Nerissa, a 2026 behind-the-scenes video by Kaela Kovalskia (secondary metadata). [S7, secondary]

### Kaela Kovalskia × Ouro Kronii
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Kaela Kovalskia | hololive ID ("TimeSmith") | Kaela is a fan of Kronii's voice; constant bickering is reported but [Unverified] | [Observed K8 §Relationships, K35, secondary] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | IRyS, Ouro Kronii | — | Minecraft elytra hunting with Kaela (2022); IRyS danced to "Soar" (2026) | [LU5] |
- `bible/characters/Takane-Lui.md › [SW] Relationships`: IRyS and Ouro Kronii: Minecraft with Kaela (2022).
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 2. Kronii and Kaela's endless sim co-op hits the in-game stock market.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Kronii and Kaela are recurring public collaborators. IRyS and Flare are recurring public collaborators.

### Kaela Kovalskia × Raora Panthera
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Kaela Kovalskia (ID) | Friend ("Grindstone"; Kaela calls her "Beejoe") | Grindstone collabs include Raft and Minecraft (2023), Split Fiction (2025) and PEAK as "Graondstone" with Raora (archive counts 10 / 23 / 11 / 0) | [Observed KB2; KB3] |
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: (Kaela calls her "Beejoe"): Raft, Minecraft, Split Fiction, and with Raora "Graondstone."
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Kaela Kovalskia | ID senior ("SMITTEN"; "Graondstone" with Bijou; secondary) | Lethal Company, Don't Starve Together, Buckshot Roulette, PEAK; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement (secondary) | [Observed RP2, RP3] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Kaela Kovalskia ("SMITTEN"): co-op partner; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement; with Koseki Bijou they are "Graondstone."
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Raora Panthera:** "Graondstone" with Bijou and Kaela; FUWAMOCO's 2026 Serendipity unit partner (B.F.F). [Official S6] [Observed S1]

### Kaela Kovalskia × Shiori Novella
- `bible/world/Hakos-Baelz-Pairs.md › With Advent`: - **Shiori Novella, Nerissa Ravencroft:** shared EN projects rather than duo collabs: the 2024 "Mind Craft" cover with all then-active EN members; with Nerissa, a 2026 behind-the-scenes video by Kaela Kovalskia (secondary metadata). [S7, secondary]

### Kaela Kovalskia × Takane Lui
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Takane Lui: Minecraft with IRyS and Kaela (2022).

### Kazama Iroha × Kobo Kanaeru
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Kazama Iroha: VALORANT with Kobo Kanaeru (2022; secondary references call the trio "KoMeHa").
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ame has "KoMeHa" with Kobo and Iroha.

### Kazama Iroha × Omaru Polka
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | FUWAMOCO | Advent seniors | They sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha | [Observed EB3] |

### Kazama Iroha × Tsunomaki Watame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | FUWAMOCO | Advent seniors | They sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha | [Observed EB3] |

### Kikirara Vivi × Koganei Niko
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-11-09 | DEV_IS second unit FLOW GLOW debuts (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya, Kikirara Vivi) | — |

### Kikirara Vivi × Usada Pekora
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Kikirara Vivi | "MVP" with Usada Pekora | An archived September 2026 "Hatsukoi Cider" upload record names the trio (secondary record, run D) | [MA2] [MVP upload record] |
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Kikirara Vivi: the unit MVP with Pekora (an archived 2026 performance record).
- `bible/characters/Kikirara-Vivi.md › Behavioral Traits`: 4. Usada Pekora ("PekoVivi," a secondary pair name): games together in 2025 (The Forest, Fast Food Simulator) and Pekora's gift of Getting Over It (2026, archived title); secondary accounts say Pekora rescued her in Minecraft, after which Vivi called her the "legendary hero" (a translated secondary description). [Observed VI2 §Miscellaneous, secondary; VI4 lqidVnpl3_0, FWCkuwroMIw, Lz56n8fa25o]
- `bible/characters/Kikirara-Vivi.md › Story Engine`: 2. Pekora "rescues" Vivi again in a game, and Vivi insists on paying her back with a makeover.
- `bible/characters/Kikirara-Vivi.md › [SW] Background`: She plays games with Usada Pekora ("PekoVivi," secondary), and an archived 2026 performance record names Marine, Vivi and Pekora as MVP.
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: (a secondary pair name); co-op games (2025) and a gifted Getting Over It (2026); secondary accounts say Pekora rescued her in Minecraft and Vivi calls her the "legendary hero."
- `bible/world/JP-Senpai-Pairs-2.md › Among themselves`: - Marine and Vivi: "MVP" with Usada Pekora; an archived September 2026 "Hatsukoi Cider" upload record names the trio. [S2] [MVP upload record]

### Kobo Kanaeru × Mori Calliope
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Kobo Kanaeru | Collaborator | "Uncle Dad" / "Dad" bits; Calli and Kiara play "Dad" and "Mom" to her. [Unverified, title only: Kobo picking up and repeating Calli's swear words] | [Observed C14; C25 §Takamori, secondary; C27 clip titles] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Takanashi Kiara | Myth genmate | Calli calls her "kusotori" ("shitty bird") and usually rebuffs her, while supporting "TakaMori." They play "Mom" and "Dad" to Kobo. | [Observed C7; C25 §Takamori, secondary] |
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo.
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Kobo Kanaeru | Collaborator | Kobo calls her "Mommy Kiwawa"; Kiara and Calli play her "Mom" and "Dad" | [Observed T5-gNEWWDKlTM8 clip title; T2 §Takamori] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Mori Calliope | Myth genmate | Kiara long called Calli her "wife" and coined "TakaMori"; Calli rebuffed her and calls her "kusotori" ("shitbird"). They announced in 2021 that they would tone the ship down (the wiki adds that "the two remain close friends"; a secondary statement, not a documented current relationship); they play "Mom" and "Dad" to Kobo as a performed family bit | [Observed T2 §Takamori, secondary; T14 title] |
- `bible/world/TakaMori.md › Hard Facts`: - Kobo's "parents" bit: Kiara "Mom," Calli "Dad"; "not married, Kobo is adopted."
- `bible/world/TakaMori.md › How It Works`: - They play "Mom" (Kiara, "Mommy Kiwawa") and "Dad" to Kobo Kanaeru; Calli insists she is not married to Kiara and Kobo is adopted. [Observed S2 §Takamori, secondary]

### Kobo Kanaeru × Nerissa Ravencroft
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity.

### Kobo Kanaeru × Ouro Kronii
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2024–2025 | World Tour '24 -Soar!- performer (New York to Taipei; "Ai ni" with Kobo Kanaeru at the Taipei finale, 2025-01-18); holoMeet ambassador 2024; World Tour '25 Sydney show with Kronii and IRyS ("Dance Monkey" as Promise, 2025-07-12) | [Official HB6, HB10] [Observed Concerts card] |
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii at Serendipity.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity.

### Kobo Kanaeru × Takanashi Kiara
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Takanashi Kiara | Her first HOLOTALK guest (2020-11-20) | A "MIRAGE" dance short (2024-10-23); "III" with Kobo in a 3D short (2024-05-20) | [MA5 3HwaqbdKO1s, tzVgzvV0cVo, I8DEx4MomOA] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Kobo Kanaeru | Collaborator | "Uncle Dad" / "Dad" bits; Calli and Kiara play "Dad" and "Mom" to her. [Unverified, title only: Kobo picking up and repeating Calli's swear words] | [Observed C14; C25 §Takamori, secondary; C27 clip titles] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Takanashi Kiara | Myth genmate | Calli calls her "kusotori" ("shitty bird") and usually rebuffs her, while supporting "TakaMori." They play "Mom" and "Dad" to Kobo. | [Observed C7; C25 §Takamori, secondary] |
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo.
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Kobo Kanaeru | Collaborator | Kobo calls her "Mommy Kiwawa"; Kiara and Calli play her "Mom" and "Dad" | [Observed T5-gNEWWDKlTM8 clip title; T2 §Takamori] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Mori Calliope | Myth genmate | Kiara long called Calli her "wife" and coined "TakaMori"; Calli rebuffed her and calls her "kusotori" ("shitbird"). They announced in 2021 that they would tone the ship down (the wiki adds that "the two remain close friends"; a secondary statement, not a documented current relationship); they play "Mom" and "Dad" to Kobo as a performed family bit | [Observed T2 §Takamori, secondary; T14 title] |
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Takanashi Kiara:** Marine was the first guest of Kiara's HOLOTALK (2020-11-20, "#marinarasauce"); Kiara danced "MIRAGE" with her (2024) and to Marine and Kobo's "III." [S1]
- `bible/world/TakaMori.md › Hard Facts`: - Kobo's "parents" bit: Kiara "Mom," Calli "Dad"; "not married, Kobo is adopted."
- `bible/world/TakaMori.md › How It Works`: - **Heard in 2025 (ASR, S6):** in the first Split Fiction stream (Kiara's channel, 2025-04-06) the "parents" bit is alive: when Kobo shows up in chat, they tell her "Hi Kobo, go to bed! … What are you doing out of bed? Go to bed!", wish her a happy anniversary, and apologize: "Sorry Kobo, you can't be part of this because it's two players only. Next time…" When their game characters split into a fire mage and an ice mage, they riff on their own song: "Fire and ice, yeah. Fire and ice, death and life." When the split screen separates them: "Oh, double Takamori." [ASR S6, nE12CyKbaX8 0:07:49, 0:08:01, 0:22:36, 0:13:28; Unverified ASR comparison: explicit shared spans and independently supported speaker attribution are unavailable in this snapshot; who said which line is not separable from the transcript]
- `bible/world/TakaMori.md › How It Works`: - They play "Mom" (Kiara, "Mommy Kiwawa") and "Dad" to Kobo Kanaeru; Calli insists she is not married to Kiara and Kobo is adopted. [Observed S2 §Takamori, secondary]

### Kobo Kanaeru × Watson Amelia
- `bible/characters/Kazama-Iroha.md › Relationship Map`: | Watson Amelia (affiliate) | "KoMeHa" with Kobo Kanaeru (secondary name) | A VALORANT collab (2022-06-04) | [IR5 tGVhLibbYL0] [IR2] |
- `bible/characters/Kazama-Iroha.md › [SW] Relationships`: Watson Amelia (affiliate): a VALORANT collab with Kobo Kanaeru (2022; secondary references call the trio "KoMeHa").
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ame has "KoMeHa" with Kobo and Iroha.

### Koseki Bijou × Ookami Mio
- `bible/characters/IRyS.md › [SW] Relationships`: At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou.

### Koseki Bijou × Oozora Subaru
- `bible/world/Advent-Pairs.md › Inside Advent`: - **Bijou and FUWAMOCO ("Diamond Dogs"):** their first collab was Overcooked 2 (2023-08-08); Bijou's "Rock rock!" parodies "bau bau"; with Subaru they sang "HOT DUCK!" at the 2025 concert. [Observed S2; S1] [Official S5]

### Kureiji Ollie × Mori Calliope
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "R x R x R" with Calli; "Countach" with Gigi and Kureiji Ollie; solo "La Roja (Arrange ver.)" | [Official HB5] |

### Kureiji Ollie × Ouro Kronii
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kureiji Ollie | ID senior; her "kami-oshi" (secondary); "HoloRed" | "Code Red" collabs: Liars Bar with Ollie and Jurard (2024), PEAK with Ollie, Flayon and Jurard (2025); "High Tide" with Kronii and Ollie at -All for One-; the 2026 "Yona Yona Dance" cover | [Observed EB2, EB3] [Official EB5] |

### Kureiji Ollie × Raora Panthera
- `bible/world/Hakos-Baelz-Pairs.md › BaeRyS`: - **Together:** a 2023 off-collab and the "Daikirai na Hazu Datta" cover (2023); a Valentine bento cooked on handcam (2024-02-14); HoloEarth with Kureiji Ollie (2024); a New Year's countdown off-collab watch-along (2024-12-31); Snow Bros. 2 (2025-04-17); Mario Party with Raora on Bae's 24-hour stream (2024-11-25). [S1]

### Mococo Abyssgard × Vestia Zeta
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Mococo / FUWAMOCO | Advent ("GigiMoco," "bauBau"; secondary) | Secondary accounts: with Cecilia, a guest-host prank on FUWAMOCO MORNING #167 (2025-07-28); "Bright Tonight" (2025) and "MAKE IT, BREAK IT" with Zeta at Serendipity (2026) with both twins | [Observed GG2; Mococo file] [Official GG7, GG9] |

### Momosuzu Nene × Shirogane Noel
- `bible/characters/Sakamata-Chloe.md › Behavioral Traits`: 2. Taunt-loving but sweet: compared by fans to Shirogane Noel, Momosuzu Nene and Tsunomaki Watame. [Observed CH2 §Personality, secondary]

### Momosuzu Nene × Shishiro Botan
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: She debuted on 2020-08-12 in hololive's 5th generation with Shishiro Botan, Omaru Polka and Momosuzu Nene (with whom she forms NePoLaBo).

### Momosuzu Nene × Yukihana Lamy
- `bible/characters/Shishiro-Botan.md › [SW] Background`: She debuted on 2020-08-14 as a fifth-generation member; she forms NePoLaBo with Yukihana Lamy, Omaru Polka and Momosuzu Nene.

### Moona Hoshinova × Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Moona Hoshinova | ID senior ("V3LVET" with Raora) | Featured on Moona's "100% (feat. Nerissa Ravencroft)" (2025-02-16); Keep Talking and Nobody Explodes together (2024) | [Official N23; N3 title] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Nerissa Ravencroft and Moona Hoshinova ("V3LVET"): Raft and Monster Hunter Wilds; Clubhouse Games with Nerissa.

### Moona Hoshinova × Raora Panthera
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Moona Hoshinova | ID senior ("V3LVET" with Raora) | Featured on Moona's "100% (feat. Nerissa Ravencroft)" (2025-02-16); Keep Talking and Nobody Explodes together (2024) | [Official N23; N3 title] |
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Raora Panthera: Clubhouse Games (2024); with Moona, Raft and Monster Hunter Wilds as "V3LVET"

### Mori Calliope × Oozora Subaru
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Hakos Baelz | — | "BAE-GEMITE DOMINATION" episode 4 with Nene (2023-04-22); a "KHAOS KITCHEN" taste tester with Calli and Oozora Subaru (2023-11-24) Co-credited singers on the hololive Dreams theme "PARADISE!" (MV 2026-09-28; seven singers). | [KO5 WwjB7QSmQng, NdLiUW-nUlk] [Secondary, dengekionline 202609/89494] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Mori Calliope | — | HOLOYOI #03 with Subaru (2023) | [BO5] |
- `bible/characters/Shishiro-Botan.md › Voice Profile`: - **Language:** streams in Japanese; archived metadata records her on Calli's HOLOYOI #03 and Bae's BAE-GEMITE DOMINATION #2 (2023), both with Oozora Subaru. [BO5]
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: Mori Calliope: HOLOYOI #03 with Oozora Subaru (2023).
- `bible/world/JP-Senpai-Pairs-2.md › Shishiro Botan with the cast`: - **Mori Calliope, Hakos Baelz:** HOLOYOI #03 and BAE-GEMITE DOMINATION #2, both with Oozora Subaru (2023). [S1]

### Mori Calliope × Regis Altare
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-07-18 (publication date; zone unspecified) | HOLOSTARS English -TEMPUS- announced: Regis Altare, Magni Dezmond, Axel Syrios and Noir Vesper | Calli and Kronii's WARS partners Magni and Vesper |

### Mori Calliope × Rikka
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Calli collaborates with Hoshimachi Suisei: Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones"
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019-06 / 09 | HOLOSTARS, COVER's male group, starts (1st gen, incl. Rikka); 2nd gen in December | Calli's MoRikka partner |

### Mori Calliope × Shiranui Flare
- `bible/world/JP-Senpai-Pairs-2.md › Shirogane Noel with the cast`: - **Mori Calliope:** HOLOYOI #02 with Shiranui Flare (2023-04-20). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: She appeared with Shiranui Flare on Calli's HOLOYOI #02 in 2023.

### Mori Calliope × Tsukumo Sana
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Mori Calliope | Myth senior | "ANATOMY REVIEW" streams (with Calli and Sana, 2022; solo, 2025) | [Observed M3] |
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Calli:** "ANATOMY REVIEW with Calli + Sana + Mumei" (2022), a drawing bit Mumei brought back on her own in 2025. [Observed S1]

### Mori Calliope × Tsunomaki Watame
- `bible/characters/AZKi.md › Background Timeline`: | 2022-03-12 | Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame | [AZ5 32NVpmKdAOs] |
- `bible/characters/AZKi.md › Voice Profile`: - **Language:** streams in Japanese; she participated in Calliope's English lesson with IRyS and Watame (2022, archived metadata). [Observed AZ5]
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Tsunomaki Watame (JP), Mori Calliope | Cross-branch; senior | "Cloudy Sheep" at Serendipity (2026) | [Official CI8] |
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Tsunomaki Watame (JP) and Mori Calliope: "Cloudy Sheep" at Serendipity.

### Mori Calliope × Usada Pekora
- `bible/characters/Hakos-Baelz.md › [SW] Background`: A singer and dancer, she has released originals such as "PLAY DICE!", "PSYCHO", "RxRxR", "FEAST" and "SNAKE EYES," the album "ZODIAC," the EP "Pandæmonium" and "HIDE & SEEK" with Usada Pekora (2023); she co-hosts the CHADCast podcast with IRyS and Mori Calliope (their song "Here Comes the CHADCast," 2026) and holds "Febaerary," a month of daily streams before her birthday.

### Mori Calliope × Vestia Zeta
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |

### Nakiri Ayame × Ookami Mio
- `bible/world/JP-Senpai-Pairs.md › History`: | 2026-08-22 | Anime NYC: an announced convention-exclusive stream | Ayame (with Fubuki, Mio) |

### Nakiri Ayame × Oozora Subaru
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2018-08 / 09 | 2nd generation (Aqua, Shion, Ayame, Choco, Subaru); Sakura Miko debuts (2018-08-01) | Earlier-debuting hololive members |

### Nanashi Mumei × Tsukumo Sana
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Tsukumo Sana | Council genmate (graduated 2022) | Human: Fall Flat (2021); Sana sent a prerecorded message for Mumei's 2022 birthday | [Observed M2 §Miscellaneous; M3] |
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday.
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Calli:** "ANATOMY REVIEW with Calli + Sana + Mumei" (2022), a drawing bit Mumei brought back on her own in 2025. [Observed S1]

### Nekomata Okayu × Ookami Mio
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Shirakami Fubuki, Ookami Mio | GAMERS; "NYANGUCORN," "MiOKayu" | GAMERS fes; Fubuki and Okayu's April Fools furball models (2026) | [OK2] |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2018-12 | hololive GAMERS (Fubuki, Mio; later Okayu, Korone) | Gaming senpai |

### Nekomata Okayu × Oozora Subaru
- `bible/characters/AZKi.md › Behavioral Traits`: - **Pun-ASMR host (2025-06-22):** she hosted a 3D pun-ASMR contest with Okayu, Noel, Oozora Subaru and Otonose Kanade; laughing meant losing. The title establishes the format and players, not particular jokes or the winner. [Archive metadata NEW-R5-004]
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | AZKi | JP kouhai | A player in AZKi's 3D pun-ASMR contest (2025-06-22), alongside Okayu, Subaru and Kanade. | [Archive metadata NEW-R5-004] |

### Nekomata Okayu × Shirakami Fubuki
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Shirakami Fubuki, Ookami Mio | GAMERS; "NYANGUCORN," "MiOKayu" | GAMERS fes; Fubuki and Okayu's April Fools furball models (2026) | [OK2] |

### Ninomae Ina'nis × Ookami Mio
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.

### Ninomae Ina'nis × Oozora Subaru
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Shiori Novella, Oozora Subaru (JP) | Advent senior; JP senior | "Neko Kaburi-Na" with Ina at -All for One- (2025) | [Official RP5] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Ninomae Ina'nis, Shiori Novella and Oozora Subaru (JP): "Neko Kaburi-Na" on stage; Puyo Puyo Tetris 2 with Ina.

### Ninomae Ina'nis × Shiranui Flare
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Shiranui Flare | JP senior | Gave her the nickname "Ore no Ina" | [Observed I2 nickname list] |

### Ninomae Ina'nis × Tsunomaki Watame
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2025 | 1.5 million subscribers (02-14, secondary); originals "Simulacre," "Gaotteko!" and "boundary"; a guest at Ina's birthday 3D live "EVERMORE" (05-21), singing "storia" with Ina and Tsunomaki Watame per a secondary set list; the first "#ホロ金策サバイバル" | [Observed BO2] [BO5] [EVERMORE report] [ASR BO20] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Ninomae Ina'nis | — | A guest at Ina's birthday 3D live "EVERMORE" (2025); "storia" with Ina and Watame (secondary set list) | [BO5 I-J11Da5ONY] [EVERMORE report] |
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: (2025), singing "storia" with Ina and Watame per a secondary set list.
- `bible/world/JP-Senpai-Pairs-2.md › Shishiro Botan with the cast`: - **Ninomae Ina'nis:** a guest at Ina's birthday 3D live "EVERMORE" (2025-05-21), singing "storia" with Ina and Tsunomaki Watame per a secondary set list. [S1] [EVERMORE report]

### Omaru Polka × Shirogane Noel
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Shirogane Noel | Shiranui Kensetsu | The Minecraft construction company with Flare, Polka and Miko | [Noel file NO2, secondary] |

### Omaru Polka × Shishiro Botan
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: She debuted on 2020-08-12 in hololive's 5th generation with Shishiro Botan, Omaru Polka and Momosuzu Nene (with whom she forms NePoLaBo).
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-08 | 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) | The JP generation just before Myth |

### Omaru Polka × Yukihana Lamy
- `bible/characters/Shishiro-Botan.md › [SW] Background`: She debuted on 2020-08-14 as a fifth-generation member; she forms NePoLaBo with Yukihana Lamy, Omaru Polka and Momosuzu Nene.
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-08 | 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) | The JP generation just before Myth |

### Ookami Mio × Takanashi Kiara
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.

### Ookami Mio × Watson Amelia
- `bible/characters/Nakiri-Ayame.md › Background Timeline`: | 2025-01 | "Ame Tokimeki Koimoyō," the anime opening sung with Fubuki and Mio (AyaFubuMi) | [Observed AY2; AY3] |
- `bible/characters/Nakiri-Ayame.md › [SW] Background`: "melting" and "Hanafubuki"; with Shirakami Fubuki and Ookami Mio as AyaFubuMi she performed "Ame Tokimeki Koimoyō," reported as a 2025 anime opening theme.

### Oozora Subaru × Raora Panthera
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-08-23/24 | -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora | [Official KB5] |

### Oozora Subaru × Shiori Novella
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Shiori Novella, Oozora Subaru (JP) | Advent senior; JP senior | "Neko Kaburi-Na" with Ina at -All for One- (2025) | [Official RP5] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Ninomae Ina'nis, Shiori Novella and Oozora Subaru (JP): "Neko Kaburi-Na" on stage; Puyo Puyo Tetris 2 with Ina.

### Oozora Subaru × Shirogane Noel
- `bible/characters/AZKi.md › Behavioral Traits`: - **Pun-ASMR host (2025-06-22):** she hosted a 3D pun-ASMR contest with Okayu, Noel, Oozora Subaru and Otonose Kanade; laughing meant losing. The title establishes the format and players, not particular jokes or the winner. [Archive metadata NEW-R5-004]

### Oozora Subaru × Shishiro Botan
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Shishiro Botan: BAE-GEMITE DOMINATION #2 with Oozora Subaru (2023).

### Ouro Kronii × Regis Altare
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-07-18 (publication date; zone unspecified) | HOLOSTARS English -TEMPUS- announced: Regis Altare, Magni Dezmond, Axel Syrios and Noir Vesper | Calli and Kronii's WARS partners Magni and Vesper |

### Ouro Kronii × Tsukumo Sana
- `bible/world/hololive--Promise.md › [SW] Description`: It grew from the English -Council- generation (August 2021), whose personas were themed around concepts (Kronii is Time); Sana graduated from Council in 2022, before Promise existed.

### Pavolia Reine × Shishiro Botan
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Gawr Gura** (graduated): "Apex Predators" (Shishiro Botan), UMISEA, "SharPea" (Pavolia Reine), and Murasaki Shion (Minecraft and Mario Kart in 2021; a "Renai Circulation" duet cover, 2022). [Observed S1; S2 Gura]

### Pavolia Reine × Takanashi Kiara
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 5. Kiara and Reine plan another "vacation" in VR.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI").

### Pavolia Reine × Takane Lui
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Pavolia Reine (ID) and Takane Lui: HOLOTORI ("PavoNashi" with Reine).

### Shiori Novella × Vestia Zeta
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Vestia Zeta (ID) | Cross-branch | "Break It Down" with Shiori at Serendipity (2026) | [Official CI8] |
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Vestia Zeta (ID) and Shiori: "Break It Down" at Serendipity.
- `bible/world/Advent-Pairs.md › History`: | 2026-09-05 | GreyScaleX (Shiori and Zeta) "Purrfect Pair" merchandise opens | [Official S7] |

### Shirakami Fubuki × Shishiro Botan
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Suisei, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024).

### Shirakami Fubuki × Watson Amelia
- `bible/characters/Nakiri-Ayame.md › [SW] Background`: "melting" and "Hanafubuki"; with Shirakami Fubuki and Ookami Mio as AyaFubuMi she performed "Ame Tokimeki Koimoyō," reported as a 2025 anime opening theme.

### Shiranui Flare × Shirogane Noel
- `bible/characters/Houshou-Marine.md › [SW] Background`: She debuted on 2019-08-11 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Shirogane Noel; secondary reporting records 3 million subscribers in 2024 and 4 million in 2025.
- `bible/characters/Shirogane-Noel.md › Behavioral Traits`: 4. "NoeFure" with Shiranui Flare: their pair label appears in Noel's own stream titles (Elden Ring Nightreign, a puzzle game, a meal collab, a fes. medley). Any mock-jealous exchanges are performed on-stream comedy, not evidence of a private relationship. [NO4 titles] [Observed NO2 §Personality, secondary]
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Shiranui Flare: hololive Fantasy genmate ("NoeFure," a label from Noel's own stream titles); any mock jealousy is on-stream comedy.

### Shirogane Noel × Tsunomaki Watame
- `bible/characters/Sakamata-Chloe.md › Behavioral Traits`: 2. Taunt-loving but sweet: compared by fans to Shirogane Noel, Momosuzu Nene and Tsunomaki Watame. [Observed CH2 §Personality, secondary]

### Shirogane Noel × Usada Pekora
- `bible/characters/Houshou-Marine.md › [SW] Background`: She debuted on 2019-08-11 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Shirogane Noel; secondary reporting records 3 million subscribers in 2024 and 4 million in 2025.

### Takanashi Kiara × Tsunomaki Watame
- `bible/characters/Raora-Panthera.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official RP4, RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Tsunomaki Watame (JP) | JP senior | "What an amazing swing" with Kiara at Serendipity (2026) | [Official RP9] |
- `bible/characters/Raora-Panthera.md › [SW] Background`: Seishun Massakari") and sang "What an amazing swing" with Tsunomaki Watame and Takanashi Kiara.

### Takanashi Kiara × Usada Pekora
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Takanashi Kiara | "Usada Kensetsu" (Usaken) | The Minecraft construction company of Pekora's circle Archived metadata dates an Usaken summer-festival planning and building collab with Kiara (2021-06-07). | [BO2] [Archive metadata, ckworks q_IXZIRCbwI] |
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI").
- `bible/world/hololive.md › How It Works`: - **Seniority:** senpai and kouhai describe relative seniority (who debuted first), not language or nationality; forms of address and levels of formality vary by relationship. Many EN members are openly starstruck by particular senpai (Kiara by Pekora). [Observed character files]

### Takanashi Kiara × Vestia Zeta
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |

### Takane Lui × Tsunomaki Watame
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Takane Lui | "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary) | Left 4 Dead 2 (2022); an Overwatch 2 team (2023). The "BLT" label was not verified in review | [BO2] [BO5] [Lui file] |
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: Takane Lui: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary); Left 4 Dead 2 (2022) and Overwatch 2 (2023) together.

### Takane Lui × Yuzuki Choco
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Takane Lui | Bara☆Dice (Bandai credits) | The wiki's "SSS" with Yuzuki Choco was not verified in review | [MA2] |

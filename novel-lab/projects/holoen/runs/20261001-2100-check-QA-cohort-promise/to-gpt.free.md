# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: promise
Packet: projects/holoen/research/qa/packets/promise.md (owned material) and projects/holoen/research/qa/packets/promise-incoming.md (incoming claims); both are inline below
Registry: projects/holoen/research/qa/registry.json

## Binding rules

- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.

Read projects/holoen/project.md and framework/prompts/shared-rules.md.
The supplied task’s stricter scope restrictions also apply. Read the packet,
registry, research/qa/manifest.json and research/qa/resolutions.md when present.
A missing required input is a coverage gap, never permission to invent its contents.

Never read projects/*/runs/, including files linked from otherwise permitted files.
Do not modify files. Return the complete audit in your final response.

The factual baseline is 2026-09-30. Later verification may establish what was true
by that date; it must not silently advance the baseline.

Use only official fictional lore and publicly presented persona behavior.
Exclude the performer’s identity, appearance, past activities, private life,
health, real family, breaks or their reasons, trips, audition history, nationality
and mother tongue—even when publicly discussed. Accents may be described only
as audible voice features. Preserve clearly fictional families, avatar lore,
in-game travel and public event locations without inferring personal travel.

Do not infer intimacy, sexuality, private closeness or hidden psychology.
Preserve supported swearing, crude jokes and performed bits without sanitizing
them or presenting them as real relationships. No lyrics, long transcripts,
explicit sexual material, voice cloning or identifiable real-voice imitation.
Original calibration lines must carry the project label “Style demo” (equivalent to
“Style demonstration”; do not file findings that only change one label to the other).

## Ownership and scope

Use the packet inventory to resolve exact paths. Primary ownership is:

- Myth (four audits: myth1 Calliope with TakaMori; myth3 Kiara with Myth-and-Kronii Other
  Pairs; myth4 Ina with TakoTori; myth2 Gura and Amelia with Myth, AmeSame and Bone Bros).
- Promise: Kronii, IRyS, Fauna, Mumei, Baelz; Promise, Time Duo, Time and Death,
  OctoClock, Fauna-and-Mumei Pairs, IRyS-and-Nerissa Pairs, Hakos-Baelz Pairs.
- Advent: Shiori, Bijou, Nerissa, Fuwawa, Mococo; Advent, Advent Pairs, FUWAMOCO.
- Justice: Elizabeth, Gigi, Cecilia, Raora; Justice, Justice Pairs.
- JP: Suisei, AZKi, Ayame, Okayu; JP Senpai Pairs.
- JP2: Marine, Noel, Lamy, Botan, Vivi; JP Senpai Pairs 2.
- holoX: La+, Lui, Koyori, Chloe, Iroha; holoX.
- Global: hololive, Streaming Life, VTuber Persona and Lore, Cross-Branch Friends,
  Concerts and Live Events, both History cards.

Together these cover the authorized 33 character and 28 world cards (the packet
inventory is authoritative). Other external participants may be referenced; do
not create their character cards. If a card your cohort owns is missing from the
packet, report coverage as INCOMPLETE instead of auditing a reduced roster.

Audit the selected cohort’s complete [SW] fields, Relationship Map, Background
Timeline and Hard Facts, plus incoming claims from every other card. Inspect
relevant source passages when needed. Packets are navigation aids, not exclusive
evidence. Search permitted bible files using canonical names, aliases and units;
include table rows, bullets and antecedents needed to interpret pronouns.

Prioritize dates, status, rosters, participants, credits, units, aliases and
directional relationships. Compare outgoing and incoming claims. Missing
reciprocal coverage is not automatically a contradiction.

Do not re-litigate previously reviewed isolated claims unless another file
contradicts them. Log apparent staleness for task 06 or 08; investigate it here
only where necessary to settle current consistency. Flag newly encountered
scope violations immediately. Detailed voice enrichment belongs to task 09.

## Evidence and quotation rules

Classify evidence, independently from claim status:

- OFFICIAL: agency profiles, announcements, event reports and official written
  copy. Quote only short exact written excerpts; distinguish lore from public
  factual announcements. An official video is not automatically a transcript.
- PRIMARY: a member’s public post, stream or other firsthand public material.
  Written posts may be quoted briefly as written. Spoken quotations require
  the ASR gate below. Distinguish performed bits from assertions.
- ARCHIVE_METADATA: title, description, timestamps and explicitly listed credits
  or participants. Quote brief metadata as metadata, never as spoken dialogue.
  Upload dates and scheduled rosters do not alone prove event dates or attendance.
- SECONDARY: wikis, fan transcripts, clips and mirrors. Attribute paraphrases.
  Short quotations of a secondary author’s prose must remain attributed to that
  author; fan transcription cannot establish a member’s exact spoken words.
- ASR: machine transcription of identified public audio. A spoken quote must
  match an explicit contiguous approved span shared by both models for the same
  audio window, with independently supported speaker attribution. Record both
  model names, timestamp, source and approved span. Punctuation/case normalization
  may be documented; never delete repetitions, alter words or stitch separated
  spans. “Agrees” without an explicit span is insufficient. Agreement is not
  human listening and does not establish speaker identity, tone or recurrence.

Keep quotations short; quote no lyrics and no more than 25 words from any one
external non-lyrical source in this audit. Prefer paraphrase plus locators.
Separate Official setting, Public-behavior observation, Author-approved adaptation
and Unverified. Unsupported assertions do not become facts in [SW] fields.

Use existing cited evidence first. Use live search only where files disagree or
a claim appears stale. Prefer official pages, then primary material. Open the
supporting page before claiming fresh verification. Label inherited evidence
“not reopened”; record inaccessible sources and distinguish absence of evidence
from disproof. Give actual checked dates, separately from event dates.

## Procedure and priority

1. Verify packet and registry hashes against their source inventory. Report
   missing, truncated or changed inputs. Reconcile changed passages or mark the
   affected coverage incomplete; never claim a clean audit of mixed snapshots.
2. Group related assertions under existing registry keys. Compare dates with
   zones, status at the relevant date, membership, attendance, unit evidence level,
   naming and directional credits. Keep announcements separate from held events.
3. Preserve older supported bits as shared memory. Use recent eligible evidence
   for present speaking defaults; alumni use their last active period. Historical
   scene status must not be inferred from the present-day roster.
4. Produce minimal exact patches and enumerate every affected file/field.
   Do not rewrite entire cards or add enrichment merely to fill a quota.

Priorities:
P0 — must resolve before delivery: scope breaches, fabricated attribution,
unapproved spoken quotations, or defects preventing a trustworthy usable release.
P1 — priority factual correction, material consistency issue or evidenced coverage gap.
P2 — optional clarity, retrieval or usability improvement.

Priority is separate from release-gate severity. A material contradiction can
block validation even when assigned P1.

“Author decision” means an explicit editorial choice between valid alternatives,
such as optional compression or accepting a disclosed evidence limitation.
It is not model approval, source verification, or permission to override binding
scope. Give a concrete question and recommendation. Do not escalate routine fixes.

IDs: {COHORT}-{TYPE}-{NNN}, with COHORT = this run's cohort in capitals (MYTH1, MYTH2, MYTH3,
MYTH4, PROMISE, ADVENT, JUSTICE, JP, JP2, HOLOX or GLOBAL), so separately queued audits never share IDs.
Use TYPE = DATE, STATUS, EVENT, ROSTER, TIE, CREDIT, UNIT, ALIAS, SCOPE, QUOTE,
VOICE, EXPORT or COVERAGE. Continue numbering from the resolution ledger.
Reuse existing IDs for the same finding; never renumber or duplicate it.
Claim keys identify facts; finding IDs identify problems.

## Exact output format

Use exactly these four top-level headings:

## Coverage

Snapshot hash; packet/registry hashes; source-hash manifest reference; files and
fields examined; incoming-claim search coverage; exclusions; unresolved evidence;
missing inputs; snapshot changes. Distinguish “examined” from “freshly verified.”

## Findings

| ID | Priority | Claim key | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|

Use one actionable finding per row. For multi-file changes, add linked patch rows
under the same ID. Copy exact old text; use DELETE for deletion. Preserve field
names and provide paste-ready replacement prose. Escape table pipes and use <br>
for internal newlines. If evidence cannot support replacement facts, propose
deletion or appropriately limited wording. If there are no findings, say “None.”

## New verified facts

Use the same table columns. Use “—” for absent old text and an exact insertion
locator. Include only directly useful facts verified during permitted checking;
otherwise write “None.” Distinguish a sourced candidate from an accepted addition.

## Merge handoff

List dependencies, unresolved conflicts, propagation order, and existing finding
IDs recommended for acceptance, rejection, deferral or further evidence. These
are recommendations, not claims that Claude merged them. Identify required
registry/packet regeneration and downstream audit owners.

End this section with “Open questions” containing at most five genuine author
decisions or unresolved input questions; write “None” when there are none.


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

### Registry excerpt (this cohort's cast and world records and its units; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "ebbab25",
 "cast": [
  {
   "name": "Ceres Fauna",
   "file": "bible/characters/Ceres-Fauna.md",
   "other_names": [
    "Fauna",
    "Faufau",
    "Fawna",
    "Keeper of Nature",
    "Mother Nature",
    "Gamer Kirin",
    "Ceres-chan"
   ],
   "groups": [
    "hololive alum",
    "hololive English -Promise- (graduated)",
    "hololive English -Council- (former unit)"
   ],
   "status": "Fauna is a hololive alum: she graduated on 2025-01-03. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "graduated",
    "debut": "2021-08-23",
    "graduated": "2025-01-03",
    "regular_activities_concluded": null,
    "source": "bible/characters/Ceres-Fauna.md › Background (debut: Background)"
   }
  },
  {
   "name": "Hakos Baelz",
   "file": "bible/characters/Hakos-Baelz.md",
   "other_names": [
    "Bae",
    "Baelz",
    "Hakos",
    "Rat Idol"
   ],
   "groups": [
    "hololive -Promise-",
    "Promise",
    "hololive English -Promise- (former branch name)",
    "hololive English -Council- (former)",
    "Council",
    "BaeRyS",
    "CHADCast"
   ],
   "status": "Bae is an active hololive member. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-08-23",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Hakos-Baelz.md › Background (debut: Background)"
   }
  },
  {
   "name": "IRyS",
   "file": "bible/characters/IRyS.md",
   "other_names": [
    "Irys",
    "SeisoRyS",
    "YabaIRyS"
   ],
   "groups": [
    "hololive -Promise-",
    "Promise",
    "hololive English -Project: HOPE- (former)",
    "hololive English (former branch name)",
    "BaeRyS",
    "CHADCast"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. IRyS is a VTuber and singer whose lore, a persona she plays for laughs, makes her a nephilim who was once the embodiment of hope in \"The Paradise\" and reawakened in an age of despair to deliver hope through her songs; she doesn't speak of what came before.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-07-11",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/IRyS.md › Background (debut: Background)"
   }
  },
  {
   "name": "Nanashi Mumei",
   "file": "bible/characters/Nanashi-Mumei.md",
   "other_names": [
    "Mumei",
    "Moom",
    "Moomers",
    "Meimei",
    "Moomsies",
    "Mumi-chan",
    "Guardian of Civilization",
    "Towl"
   ],
   "groups": [
    "hololive alum",
    "hololive English -Promise- (graduated)",
    "hololive English -Council- (former unit)",
    "HOLOTORI"
   ],
   "status": "Mumei is a hololive alum: she graduated on 2025-04-27 (04-28 JST). She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "graduated",
    "debut": "2021-08-23",
    "graduated": "2025-04-27",
    "regular_activities_concluded": null,
    "source": "bible/characters/Nanashi-Mumei.md › Background (debut: Background)"
   }
  },
  {
   "name": "Ouro Kronii",
   "file": "bible/characters/Ouro-Kronii.md",
   "other_names": [
    "Kronii",
    "Warden of Time",
    "オーロ・クロニー",
    "Kronini",
    "Kroniicopter",
    "Kronster",
    "Tam Tender",
    "Owo-senpai"
   ],
   "groups": [
    "hololive",
    "hololive -Promise-",
    "Promise",
    "Council (former unit name)",
    "Octo'clock"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. Kronii is a VTuber whose lore, a persona she plays deadpan, makes her the Warden of Time, the third concept created by the gods and the one most bound to humankind.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-08-23",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Ouro-Kronii.md › Background (debut: Hard Facts / Background Timeline)"
   }
  }
 ],
 "world": [
  {
   "name": "Fauna and Mumei Pairs",
   "file": "bible/world/Fauna-and-Mumei-Pairs.md",
   "role": "Relationship",
   "other_names": [
    "Fauna and Mumei",
    "Mumei and Fauna",
    "It's Not a Phase",
    "KronMei",
    "gumei",
    "Fauna and Gura",
    "Mumei and Kiara",
    "Mumei and Kronii"
   ]
  },
  {
   "name": "Hakos Baelz Pairs",
   "file": "bible/world/Hakos-Baelz-Pairs.md",
   "role": "Relationship",
   "other_names": [
    "Bae and IRyS",
    "BaeRyS",
    "CHADCast",
    "BaeBi",
    "BratTea",
    "Bae and Kronii",
    "Bae and Calli",
    "Bae and Cecilia"
   ]
  },
  {
   "name": "IRyS and Nerissa Pairs",
   "file": "bible/world/IRyS-and-Nerissa-Pairs.md",
   "role": "Relationship",
   "other_names": [
    "MorIRyS",
    "CHADCast",
    "KiaRissa",
    "IRyS and Kronii",
    "IRyS and Ina",
    "Nerissa and Calli",
    "Nerissa and IRyS"
   ]
  },
  {
   "name": "Octo'Clock",
   "file": "bible/world/OctoClock.md",
   "role": "Relationship",
   "other_names": [
    "Ina and Kronii",
    "Kronii and Ina",
    "Octo'clock",
    "Octo'Clock"
   ]
  },
  {
   "name": "Time Duo",
   "file": "bible/world/Time-Duo.md",
   "role": "Relationship",
   "other_names": [
    "Ame and Kronii",
    "Kronii and Ame"
   ]
  },
  {
   "name": "Time and Death",
   "file": "bible/world/Time-and-Death.md",
   "role": "Relationship",
   "other_names": [
    "Calli and Kronii",
    "Kronii and Calli"
   ]
  },
  {
   "name": "hololive -Promise-",
   "file": "bible/world/hololive--Promise.md",
   "role": "Faction",
   "other_names": [
    "hololive -Promise-",
    "holoPromise",
    "hololive Council",
    "holoCouncil",
    "CouncilRyS",
    "BaeRyS"
   ]
  }
 ],
 "units": [
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
   "unit": "Octo'clock",
   "members": [
    "Ninomae Ina'nis",
    "Ouro Kronii"
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
  }
 ]
}
```

### projects/holoen/research/qa/packets/promise.md

# Audit packet: promise

Snapshot: git ebbab25. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Ouro-Kronii.md` 4dffa89f761b; `bible/characters/IRyS.md` 868c53e2e031; `bible/characters/Ceres-Fauna.md` 80c27935baac; `bible/characters/Nanashi-Mumei.md` 76cb7d253ec8; `bible/characters/Hakos-Baelz.md` c4e2bef9231c; `bible/world/hololive--Promise.md` b80a53219f8b; `bible/world/Time-Duo.md` 329fef0a8daa; `bible/world/Time-and-Death.md` e1239bb9b626; `bible/world/OctoClock.md` 6407b5c4a155; `bible/world/Fauna-and-Mumei-Pairs.md` 537910125c8d; `bible/world/IRyS-and-Nerissa-Pairs.md` 1a33b27ee01c; `bible/world/Hakos-Baelz-Pairs.md` ed9cffbde495

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Ouro Kronii — `bible/characters/Ouro-Kronii.md`
**[SW] Groups:** hololive, hololive -Promise-, Promise, Council (former unit name), Octo'clock
**[SW] Other Names:** Kronii, Warden of Time, オーロ・クロニー, Kronini, Kroniicopter, Kronster, Tam Tender, Owo-senpai
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. Kronii is a VTuber whose lore, a persona she plays deadpan, makes her the Warden of Time, the third concept created by the gods and the one most bound to humankind. Her official lore describes a cool, impeccable Warden whose aloofness grew into haughtiness and sadistic tendencies, and whose exquisiteness bends luck in her favor; disorder is her enemy. She debuted in August 2021 with hololive English -Council-. In October 2023, she joined hololive English -Promise- alongside IRyS, Ceres Fauna, Nanashi Mumei and Hakos Baelz. Following Fauna's and Mumei's graduations in 2025, its current members are Kronii, IRyS and Baelz, and since the 2026 merger the unit belongs to the single hololive brand. Her fans are the Kronies, which she also calls Kromies. Her mascot is Boros, a small white ouroboros snake. She is known for a Minecraft era spent building bunkers (the Bunkeronii). Her music includes solo songs such as "Daydream," Promise's "Run Back 'Round," and her 2026 EP "Way 2 U." In 2026 she also began a performance partnership with Ninomae Ina'nis. She jokes that she is 60.
**[SW] Relationships:** Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "Just two punny people," and both speak Korean. Hakos Baelz: genmate whom Bae called a "tsundere granny" (per the wiki); Sandwich Review, Digimon Survive, Fortnite and "Dance Monkey" in Sydney (2025); in fan lore Kronii created leap years for Bae's birthday. IRyS: Promise unitmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who wondered how Kronii sounds when scared. Nanashi Mumei (graduated 2025): Council genmate and frequent partner (KronMei), from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). AZKi: R.E.P.O. "JP & EN" with Ina and IRyS (2025). Ceres Fauna (graduated 2025): Council genmate who described Kronii's "gap moe"; they once defused bombs speaking only in ASMR. Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: Raft, Luma Island, Old Market Simulator; 2024 World Tour panel. Kikirara Vivi and Shirogane Noel: Mumei's Gartic Phone (2025). Takane Lui: Minecraft with IRyS and Kaela (2022). Gigi Murin: Fatal Fury and Hytale ("TimeChaser"; "Clockwork Orange" with Cecilia), "MONSTER" on stage and "Bright Tonight" (2025). Cecilia Immergreen: Cecilia calls her "Owo-senpai," and Kronii has called Cecilia a "CLANKER." Raora Panthera: "Pizza Time" partner (Portal 2, 2024; Backrooms Cleanup Crew, 2026), who used "Tam Tender" for Kronii's ENReco character. Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live. Shiori Novella: "Rating Your Clocks" together (2025) and "MONSTER" with Ina and Gigi on stage (2025). Koseki Bijou: Lethal Company and Yu-Gi-Oh. FUWAMOCO: "WatchDog." Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity. Elizabeth Rose Bloodflame and Kureiji Ollie (ID): "High Tide" at -All for One- (2025).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | Warden of "Time", the third concept created by the gods and the one most tied to humankind | Supervisory, haughty office [Official K2] |
| 2021-08-23 JST | Debuts with hololive English -Council- | Fans become Kronies [Official K1] |
| 2021-10 | Minecraft "civil war" with Fauna | [Unverified, K29 clip titles] |
| 2022-01-15 | Kimono reveal; introduces Boros | [Observed K8 §Mascots and fans, secondary] |
| 2022-08 | Mumei accidentally blows up the Bunkeronii's entrance | [Unverified, K28 clip titles] |
| 2023-10-09 | Joins hololive English -Promise- alongside IRyS, Ceres Fauna, Nanashi Mumei and Hakos Baelz | [Official K3] |
| 2025 | Fauna (January) and Mumei (April) graduate; Promise's current members are Kronii, IRyS and Baelz | Shared history stays [Official K34] |
| 2025-10-10 | Promise releases "Run Back 'Round" | [Official K6] |
| 2026-03-13 | 3D birthday live; Watson Amelia guests; she announces the EP "Way 2 U"; the title single's official on-sale date is 2026-03-15 | [Observed K33, secondary, stream t=1711; K38, secondary] |
| 2026-05-08 | Single "STORM" (later on the EP) | [Observed K38, secondary] |
| 2026-05-28 JST | "Way 2 U" MV: Kronii shares the lyric credit with JALTO (JALTO composed and arranged; choreography by Miyuki Nishijima). | [Archive metadata NEW-R2-006, reproducing the MV credits] |
| 2026-06-04 | Serendipity interview and partnership with Ina | Puns, appreciation, performance goals [Official K4] |
| 2026-08-23 | EP "Way 2 U" (five tracks, including the earlier "Daydream") | Adds to earlier solo music [Official K7] |
| 2026-09-07 | Branches merge into one "hololive"; unit is hololive -Promise- | [Official K5, K1] |
**Dossier · Hard Facts (continuity):**
- Birthday March 14 (pi day); height 168 cm; debut 2021-08-23 JST; unit hololive -Promise-. [Official K1]
- Fans Kronies (and Kromies); mascot Boros; membership tiers Second / Minute / Hour. [Observed K8
  §Mascots and fans, secondary]
- Age: the "∞" entry is secondary-reported [Unverified as official]. She calls herself 60. [Observed K8
  infobox and §Mascots and fans, secondary]
- Minecraft base: the Bunkeronii. [Observed K37 §Relationships, secondary; K28 clip titles]
- Aliases: Kronini, Kroniicopter, Kronster (by Calli), Tam Tender (by Raora), Owo-senpai (by
  Cecilia). Performed identities are excluded from matching unless a story uses them: Ouro Krono
  (-Ministry- persona, goodbye "Kronovoir") and Tam Gandr (ENreco). [Observed K8 nickname list,
  §Name and §Miscellaneous, secondary]

### IRyS — `bible/characters/IRyS.md`
**[SW] Groups:** hololive -Promise-, Promise, hololive English -Project: HOPE- (former), hololive English (former branch name), BaeRyS, CHADCast
**[SW] Other Names:** Irys, SeisoRyS, YabaIRyS
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. IRyS is a VTuber and singer whose lore, a persona she plays for laughs, makes her a nephilim who was once the embodiment of hope in "The Paradise" and reawakened in an age of despair to deliver hope through her songs; she doesn't speak of what came before. She debuted on 2021-07-11 as hololive English's VSinger, the sole member of -Project: HOPE-, and joined -Promise- with Fauna, Kronii, Mumei and Bae in 2023; since the 2026 merger she is in hololive -Promise-. Her fans are IRyStocrats and her members Nephamily. She has released several EPs, held 3D lives such as "The Devil Wears Hope" (2024), "HOPE UPON A STAR" (2025) and "Racing Towards Hope" (2026, in a race-queen outfit), released her first full-length album, "DANGERyS," on 2026-07-12; her first solo concert, "HOPE ||: Beyond the Stars," is scheduled in Tokyo for 2026-10-06.
**[SW] Relationships:** Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced," and a creative partner: in their 2026-06-05 pre-concert interview IRyS said she relies on Bae's creative direction when she's indecisive and called their dynamic "a can of worms" (Bae: "Complicated XD"), and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable. Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring collaborator (horror camping, Splatoon, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina they starred at hololive night at Dodger Stadium (2025). Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna (graduated 2025): Promise unitmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Nanashi Mumei (graduated 2025): Promise unitmate; Overwatch in her farewell week. Shiori Novella: Monster Hunter Wilds and PEAK (2025). Gigi Murin: ENReco Cerulean Cup guildmate. Raora Panthera: Mario Party Jamboree with Bae (2024). Nekomata Okayu and Nakiri Ayame: Okayu's 2025 New Year Game Festival team. Cecilia Immergreen: Elden Ring Nightreign with Bijou (2025). Gigi Murin, Ouro Kronii and FUWAMOCO: "Bright Tonight" (2025). Elizabeth Rose Bloodflame: "START AGAIN" with Calli and Nerissa at the 2025 concert. At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou. Takanashi Kiara: a friend since 2021 who gave her a German crash course. Hoshimachi Suisei and AZKi: with Moona Hoshinova, the unit Star Flower ("story time," 2022); Suisei also performed "High Tide" with her, Bae and Moona at Breaking Dimensions (2024). Shishiro Botan, Takane Lui, Sakamata Chloe and Tokoyami Towa: an Overwatch 2 team (2023); Hakui Koyori: Splatoon 3 and Among Us.
**Dossier · Background Timeline:**
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
| 2026-07-12 | Album "DANGERyS"; the official introduction names "Escalate" the lead single and describes Eurobeat as one of several styles on the album. | [Official NEW-R2-004] |
| 2026-09-07 | Branch merger; her unit is "hololive -Promise-" | [Observed R2] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-07-11; birthday March 7; 162 cm; fans IRyStocrats, members Nephamily; emoji 💎.
- Unit: hololive -Promise- (since 2023-10-09; "hololive English -Promise-" before 2026-09).
- Solo concert "HOPE ||: Beyond the Stars," 2026-10-06, Tokyo (announced).

### Ceres Fauna — `bible/characters/Ceres-Fauna.md`
**[SW] Groups:** hololive alum, hololive English -Promise- (graduated), hololive English -Council- (former unit)
**[SW] Other Names:** Fauna, Faufau, Fawna, Keeper of Nature, Mother Nature, Gamer Kirin, Ceres-chan
**[SW] Background:** Fauna is a hololive alum: she graduated on 2025-01-03. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore, a persona she plays for laughs, makes her the Keeper of "Nature," the second concept created by the gods: a druid with kirin blood whose horns are tree branches, who came online to win humans over and lead them back to nature. She debuted on 2021-08-23 with hololive English -Council-, joined -Promise- with IRyS, Kronii, Mumei and Bae in 2023, won VTuber Awards for ASMR and for chatting streams, sang at both hololive English concerts (2023, and 2024, where she and Mumei premiered their duet "It's Not a Phase") and in Promise's musical "The Broken Promise" (2024), reached one million subscribers on 2024-12-27, and finished her Minecraft World Tree on 2024-12-31, days before graduating. Her fans are Saplings, her members Faunatics, and her mascot is Nemu, a sleepy kirin.
**[SW] Relationships:** Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who, per a fan reference, praised her maternal persona at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024). Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!" Koseki Bijou: "Coach Fauna" in Bijou's Hitman runs and a "Sweaty TryHard Gamers" squad with Bae and Kaela. FUWAMOCO: helped on the World Tree's last day (2024-12-31). Shiori Novella: the third voice of "Lonely in Gorgeous." Cecilia Immergreen: a book and shoujo-manga tropes ranking (2024; "Green Women"). Gigi Murin: Silent Hill 2 and the 2024 Coughing Baby Award Show ("FruitPunch," a secondary pair name). Mori Calliope: her five-player Dota 2 collab with Bijou, Nerissa and Kobo (2024).
**Dossier · Background Timeline:**
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
**Dossier · Hard Facts (continuity):**
- Debut 2021-08-23 (JST); graduated 2025-01-03; birthday March 21; 164 cm; fans Saplings; members
  Faunatics; emoji 🌿; mascot Nemu.
- Unit: -Council- (2021–23), hololive English -Promise- (2023–25).

### Nanashi Mumei — `bible/characters/Nanashi-Mumei.md`
**[SW] Groups:** hololive alum, hololive English -Promise- (graduated), hololive English -Council- (former unit), HOLOTORI
**[SW] Other Names:** Mumei, Moom, Moomers, Meimei, Moomsies, Mumi-chan, Guardian of Civilization, Towl
**[SW] Background:** Mumei is a hololive alum: she graduated on 2025-04-27 (04-28 JST). She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her the Guardian of "Civilization," the only member of her generation created not by the gods but by mankind's efforts; she chose an owl's form for wisdom, and too many transformations made her brain "more bird," so she forgets things, including her original name and her age. Lonely on her travels, she made a friend out of paper: a paper bag called simply "Friend," so she can't forget his name. She debuted on 2021-08-23 with hololive English -Council-, released the original songs "A New Start" (2022) and "mumei" (2023), joined -Promise- in 2023, reached one million subscribers on 2024-01-26 (the first in Council and Promise), held the 3D birthday live "Outside the Box" on 2024-08-05, premiered the duet "It's Not a Phase" with Fauna at the 2024 English concert, and spent her last month in collabs and covers with members across hololive. Her fans are Hoomans, her members Owl Pals, and her stream descriptions end with ":D".
**[SW] Relationships:** Ceres Fauna (graduated 2025-01): Council and Promise genmate and recurring collaborator; their comedy includes Fauna's exaggerated protective, possessive bits ("return to nature"), complicated by Mumei's macabre humor; they premiered their duet "It's Not a Phase" at the 2024 English concert. Hakos Baelz: genmate and a recurring collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). Ouro Kronii ("KronMei"): genmate and frequent partner, from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). IRyS: Promise unitmate from 2023; Overwatch in Mumei's farewell week, then Promise R.E.P.O. (2025-04-24). Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday. Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song at the 4th fes. (2023), and Kiara hosted Mumei as HOLOTALK's 33rd guest on 2025-04-22. Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week. Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week. Ninomae Ina'nis: fellow artist, drawing collabs. Mori Calliope: "ANATOMY REVIEW." Nerissa Ravencroft: "EMO HOURS" (2023), "Beyond the way" with Kiara at the 2024 concert, "SAD GIRL HOURS" (2025). Koseki Bijou ("Stone Age"): Portal 2 and Marvel Rivals; at arm wrestling Mumei rates her a loss because "she is a rock." Gigi Murin: Echo Point Nova as "A Towl and a Gremlin." Cecilia Immergreen: Halo co-op ("Automatowl"). FUWAMOCO ("Fuwamoomco"): Overwatch. JP: archived uploads document her Q&A with Takane Lui, an April 2025 duet cover with Inugami Korone, and Korone, Okayu, Nene and Koyori as 2024 "Outside the Box" guests; Tokoyami Towa calls her "Mumi-chan"; Akai Haato: Minecraft; Nakiri Ayame: the 2023 Sports Festival white team. Shiori Novella: B-movie watchalongs (Neil Breen, Kung Pow; 2025). Raora Panthera: a joint drawing stream (2025). Sakamata Chloe: Mumei's EN-server Minecraft tour with Lui and Bae (2022). Shirogane Noel, Kikirara Vivi and Elizabeth Rose Bloodflame: her Gartic Phone EN + ID + JP collab (2025). Houshou Marine: Mumei and Bae played "Truth of Beauty Witch," the horror game featuring Marine (2023). Hoshimachi Suisei: a #bibbidibachallenge short (2024).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | Guardian of "Civilization," the concept made by mankind rather than the gods; chose an owl form; has forgotten her name and age | [Official M1] [Observed M2 §Lore] |
| 2021-08-23 JST | Debuts with hololive English -Council- (first post on X: "oh man") | [Official M1] [Observed M4] |
| 2022-01-17 | First original song "A New Start" | [Observed M2 §2022] |
| 2023-03-18/19 | 3D idol costume and main 3D model at hololive 4th fes.; sang a DECO*27 song with Kiara on the holo*27 stage | [Observed M2 §2023; M4] |
| 2023-10-09 | Joins hololive English -Promise- | [Official] |
| 2023-10-10 | Second original song "mumei" | [Observed M2 §2023] |
| 2024-01-26 | 1,000,000 subscribers, the first of Council/Promise | [Observed M2 §2024] |
| 2024-08-05 | 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori | [Observed M3 title, description] |
| 2024-08-24 | -Breaking Dimensions- day 1: premieres "It's Not a Phase" with Fauna; "Beyond the way" with Kiara and Nerissa; day 2: her original "A New Start" | [Official M5] |
| 2024-12-22 | "It's Not a Phase" (Mumei & Fauna) released | [Official M6] |
| 2025-02-14 | 3.0 Live2D model | [Observed M2 §2025] |
| 2025-03 | Spring covers: YOASOBI's "IDOL" (its description uses the written owl pun "idowl ! ~") and "Gravity" (original by Yoko Kanno, Maaya Sakamoto and Troy). | [Archive metadata NEW-R2-014] |
| 2025-03-09 | 6th fes. "Color Rise Harmony," day 2 | [Observed M2 §2025] |
| 2025-04 | A farewell month of collabs across hololive: Overwatch with IRyS (04-22), a cover of "とんとんまーえ！" with Inugami Korone (04-23), Promise R.E.P.O. with IRyS, Kronii and Bae (04-24); last chatting stream with calls (04-26); 3D graduation stream (04-27, 04-28 JST) | [Observed M2; M3 titles] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-08-23 (JST); graduated 2025-04-27 (04-28 JST); birthday August 4; 156 cm; fans Hoomans;
  members Owl Pals; mascot Friend; emoji 🪶.
- Unit: -Council- (2021–23), hololive English -Promise- (2023–25).

### Hakos Baelz — `bible/characters/Hakos-Baelz.md`
**[SW] Groups:** hololive -Promise-, Promise, hololive English -Promise- (former branch name), hololive English -Council- (former), Council, BaeRyS, CHADCast
**[SW] Other Names:** Bae, Baelz, Hakos, Rat Idol
**[SW] Background:** Bae is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her the concept of Chaos, "birthed by the world," whom the gods appointed chairperson of the Council. Her official birthday is 29 February; fan-recorded lore credits Ouro Kronii with creating leap years for her. She debuted on 2021-08-23 (JST), the last of hololive English -Council-, which became -Promise- with IRyS in October 2023; Promise's active members at the baseline are Bae, IRyS and Kronii. A singer and dancer, she has released originals such as "PLAY DICE!", "PSYCHO", "RxRxR", "FEAST" and "SNAKE EYES," the album "ZODIAC," the EP "Pandæmonium" and "HIDE & SEEK" with Usada Pekora (2023); she co-hosts the CHADCast podcast with IRyS and Mori Calliope (their song "Here Comes the CHADCast," 2026) and holds "Febaerary," a month of daily streams before her birthday. On stage she sang "GEKIRIN" solo and "BLUE CLAPPER" with the CHADCast trio and Koseki Bijou (2024), "Ai ni" with Kobo Kanaeru (2025), "Dance Monkey" as Promise in Sydney (2025), "R x R x R" with Calli and "Countach" with Gigi Murin and Kureiji Ollie (2025), and at Serendipity (2026) "LUVATORRRRRY!" with IRyS as BaeRyS and "HELP!!" with Kobo and Elizabeth Rose Bloodflame. At the 2026 hololive fes she performed "Idol" as the final solo number of STAGE 3. In August 2026 her first solo concert, "REGALIA," and her album "Mirror Mirror" were announced.
**[SW] Relationships:** IRyS: her BaeRyS partner in a performed "married and divorced" routine that fan references trace to a Minecraft bento exchange; covers, off-collabs, "Here Comes the CHADCast" and "LUVATORRRRRY!" at Serendipity; Bae calls IRyS "the very first senpai I had ever met," and IRyS calls their dynamic "a can of worms." Mori Calliope and IRyS: her CHADCast cohosts; "BLUE CLAPPER" with them and Koseki Bijou (2024); "R x R x R" with Calli (2025); secondary references record her nickname "Cori Malliope." Ouro Kronii: Promise genmate; Sandwich Review, Digimon Survive, Fortnite; "Dance Monkey" in Sydney (2025). Ceres Fauna (graduated): genmate and horror partner (Amnesia, 2022–2023). Nanashi Mumei (graduated): genmate; BAE-CADEMY, off-collabs, Overwatch 2. Tsukumo Sana: a graduated Council genmate. Koseki Bijou: "BaeBi," a 2024 sleepover marathon, We Were Here. Cecilia Immergreen: "BratTea"; by Bae's account a coffee-versus-tea debate, a 2026 fes talk and Resident Evil together. Gigi Murin: "Countach" with Kureiji Ollie (2025); a Midsummer Night's Dream reading. Elizabeth Rose Bloodflame and Kobo Kanaeru: "HELP!!" at Serendipity. Raora Panthera: Mario Party on Bae's 24-hour stream. FUWAMOCO: Gigi's 2025 Spring Party; they danced to "SNAKE EYES." Takanashi Kiara: Keep Talking and Nobody Explodes (2021). Ninomae Ina'nis: a K/DA cover and an art lesson. Watson Amelia: bathroom reviews and Apex. Gawr Gura: the Urban Dictionary Challenge. Usada Pekora: "HIDE & SEEK" (2023). Ookami Mio and Ollie: her joking "moms" (secondary). Natsuiro Matsuri: "Kakumei Dualism" at the 2026 fes. holoX: Sakamata Chloe ("Crazy Scary Holy Fantasy," 2023), Takane Lui (episode 5, with Chloe) and Hakui Koyori (episode 4, with Nene) on BAE-GEMITE DOMINATION. Houshou Marine: Mario Kart (2021) and Calli's house party (2023); Bae and Mumei played "Truth of Beauty Witch," the horror game featuring Marine. Kikirara Vivi: #holoREPO (2025). Shirogane Noel: a team Mario Kart event with FUWAMOCO (2023). Shishiro Botan: BAE-GEMITE DOMINATION #2 with Oozora Subaru (2023). Hoshimachi Suisei: "High Tide" with IRyS and Moona at Breaking Dimensions (2024) and Bae's "Moonlight" dance cover (2025). AZKi: GeoGuessr (2023). Nekomata Okayu: team kart events (2023, 2024).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | Chaos itself, "birthed by the world"; appointed chairperson of the Council by the gods, though she takes a hands-off approach; breaks rules and watches the aftermath; a rat by form, "chaos" by species; age unknown ("roll a dice"); born on 29 February (in fan-recorded lore, Kronii created leap years to hold her) | [Official HB1 (original lore)] [Observed HB2 §Lore, secondary] |
| 2021-08-23 JST | Debut, fifth and last of hololive English -Council- (08-22 PDT); she closed by singing "Fuwa Fuwa Time" | [Official HB1] [Observed HB2] |
| 2021-09-24 | Keep Talking and Nobody Explodes with Takanashi Kiara, which fan references call her first official collab outside Council | [Observed HB2, secondary; HB3 579F-lu2cKY] |
| 2022 | The CHADCast podcast with IRyS and Mori Calliope (Chaos, Hope and Death; episode 1 in January); the first "Febaerary"; first original song "PLAY DICE!" (02-28) | [Observed HB2; HB3 MXd7uOemEzc; Calli file C12] |
| 2022-08-23 | Council's first group original song "Rise" | [Observed HB2] |
| 2022-10 | "BAE & FAUNA'S MONTH OF HORRORS" (Amnesia: The Dark Descent on Fauna's channel) | [Observed HB2, secondary; HB8 DaG38dShdGE] |
| 2023-03-19 | 3D debut at hololive 4th fes. "Our Bright Parade"; her own 3D debut stream 2023-09-30 | [Observed HB2] |
| 2023-07-02 | hololive English 1st concert "-Connect the World-"; EP "Pandæmonium" (07-07) | [Observed HB2] |
| 2023-10-09 JST | hololive English -Promise- formed with IRyS, Fauna, Kronii and Mumei | [Observed HB2; Promise card] |
| 2023-12-28 | "HIDE & SEEK 〜Nakayoku Kenkashina〜," an original song with Usada Pekora | [Official HB9] |
| 2024-02-29 | Original "RxRxR" and first album "ZODIAC" | [Observed HB2] |
| 2024-08-24/25 | -Breaking Dimensions-: "Our Promise" with Promise; "BLUE CLAPPER" with Calli, IRyS and Koseki Bijou; solo "GEKIRIN"; "High Tide" with IRyS, Moona Hoshinova and Hoshimachi Suisei | [Official HB5] |
| 2024–2025 | World Tour '24 -Soar!- performer (New York to Taipei; "Ai ni" with Kobo Kanaeru at the Taipei finale, 2025-01-18); holoMeet ambassador 2024; World Tour '25 Sydney show with Kronii and IRyS ("Dance Monkey" as Promise, 2025-07-12) | [Official HB6, HB10] [Observed Concerts card] |
| 2024-11-25 | "#BaeTV24" 24-hour stream with collabs (IRyS and Raora; Kronii, Bijou and Gigi) | [Observed HB3] |
| 2024-12-14 | Promise musical "The Broken Promise" | [Observed HB2] |
| 2025-02-28 | Original "FEAST"; birthday 3D live "-KAGURA- Dance of the Gods" | [Observed HB2; HB3 viPlIHvk724] |
| 2025-08-23/24 EDT | -All for One-: "R x R x R" with Calli; "Countach" with Gigi and Kureiji Ollie; solo "La Roja (Arrange ver.)" | [Official HB5] |
| 2026-02-28 | Birthday 3D live "ReCOLOR" with a new 3D outfit; original "SNAKE EYES"; her fifth Febaerary | [Observed HB2] [ASR HB20] |
| 2026-03-06/08 | hololive 7th fes. "Ridin' on Dreams": "Idol" as the final solo number of STAGE 3 (her own choreography with a breakdance finish, by her account) and "Kakumei Dualism" with Natsuiro Matsuri; a venue talk with Cecilia Immergreen (her account) | [Official HB11 lineup] [secondary setlist HB12] [ASR HB20] |
| 2026-04 | Resident Evil series with Cecilia (her account); the "Liar Dancer" cover; the mock rival feud | [ASR HB20] |
| 2026-07-03/04 PDT | Serendipity: BaeRyS with IRyS ("LUVATORRRRRY!"), "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame (day 1) | [Official HB4, HB5] |
| 2026-08 | 5th anniversary: her 1st concert "REGALIA" (2026-12-01, after the baseline) and 2nd album "Mirror Mirror" announced (timing per a contemporaneous secondary report); original "I found me" | [Official HB7] [Observed HB2] |
| 2026-08-23 | Announced: "I found me," with lyrics by Bae (composition and arrangement by Tomomichi Takuma of Dream Monster), and her second album "Mirror Mirror," scheduled for 2026-11-02 (after the baseline: an announcement only). | [Official NEW-R2-017] |
| 2026-09-01 | "Here Comes the CHADCast," released with Mori Calliope and IRyS | [Official HB9] |
| 2026-09-03 | [Secondary, pending primary confirmation] Reported casting as Monami Ichikawa in *Sucker for Love: Crush Landing*; a September playthrough on her channel is also reported. | [Secondary NEW-R2-018] |
| 2026-09-07 | Branches merge into one "hololive"; her unit is hololive -Promise- | [Official HB1] |
| 2026-09-28 | "PARADISE!", the hololive Dreams area theme: animated MV; Bae shares the vocal credit with Omaru Polka, Houshou Marine, Yukihana Lamy, Hakui Koyori, Kobo Kanaeru and Ichijou Ririka. Also announced that day: "REGALIA" at Kanadevia Hall, scheduled for 2026-12-01 (after the baseline: an announcement only). | [Secondary NEW-R2-019, press-release reproduction] [Official, 20260928-02-16] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-08-23 (JST; 08-22 PDT), the last of -Council-; birthday 29 February; 149 cm; illustrator Mika
  Pikazo; fans "Brats" (also written "Baerats"); members "Rat Pack"; mascot Mr. Squeaks; oshi mark 🎲.
- Unit: hololive English -Council- (2021), -Promise- (from 2023-10-09 JST), "hololive -Promise-" since the
  2026-09-07 merger; Promise's active members at the baseline: IRyS, Kronii, Bae.
- Official stage units: BaeRyS with IRyS (Serendipity 2026); CHADCast trio with Calli and IRyS.
- Upcoming after the baseline: 1st concert "REGALIA" (2026-12-01, per the official announcement) and 2nd album
  "Mirror Mirror."

### hololive -Promise- — `bible/world/hololive--Promise.md`
**[SW] Other Names:** hololive -Promise-, holoPromise, hololive Council, holoCouncil, CouncilRyS, BaeRyS
**[SW] Description:** hololive -Promise-: IRyS, Ouro Kronii and Hakos Baelz at the 2026 baseline. It grew from the English -Council- generation (August 2021), whose personas were themed around concepts (Kronii is Time); Sana graduated from Council in 2022, before Promise existed. IRyS ("Hope") and the four remaining Council members were billed together as "CouncilRyS" and formed Promise on 2023-10-08 PDT / 10-09 JST; Fauna (Nature, the soft kirin protective of Mumei) and Mumei (Civilization, the forgetful owl and a recurring collaborator with Bae) graduated in 2025. All five sang their unit song "Our Promise" at the 2024 English concert and staged the musical "The Broken Promise" (December 2024). Bae has described Kronii as a "tsundere granny" (per the wiki); Fauna once described Kronii's "gap moe," the cute side that shows when she's flustered; IRyS has wondered aloud how Kronii sounds when she's scared. IRyS and Bae keep up the performed "BaeRyS" routine of being "married" and "divorced," and they are also creative partners: in a pre-concert interview for Serendipity (2026), IRyS said she leans on Bae's "strong vision" when she's indecisive, Bae said she admires IRyS's humor that makes everyone comfortable, and IRyS called their dynamic "a can of worms" ("Complicated XD," Bae answered).
**[SW] Rules:** At the 2026 baseline Promise is IRyS, Kronii and Bae; Fauna and Mumei are Promise graduates and Sana a Council graduate, appearing only as memories. Unit names (Council, Promise) describe groups, not real powers or concepts.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2021-08 | -Council- debuts (Sana, Fauna, Kronii, Mumei, Bae) | "Council" nostalgia |
| 2022-07-31 | Sana graduates | Council becomes four |
| 2023-10-08 PDT / 10-09 JST | -Promise- formed with IRyS (closing Project: HOPE) | The current group name |
| 2025-01-03 | Fauna graduates | — |
| 2025-04-27 | Mumei graduates | Promise becomes three |
**Dossier · Hard Facts (continuity):**
- Active 2026-09-30: IRyS, Kronii, Bae. Graduated: Fauna, Mumei (from Promise); Sana (from Council, 2022).
- Unverified title-only bits (Bae holding Kronii's hand, scaring Bae with IRyS) are not facts.

### Time Duo — `bible/world/Time-Duo.md`
**[SW] Other Names:** Ame and Kronii, Kronii and Ame
**[SW] Description:** Watson Amelia and Ouro Kronii, the time-traveling detective and the Warden of Time. Their rivalry is a lore joke: when Kronii debuted, Ame joked that Twitter was "protecting me from a certain time lord" and swore "i'll give it back soon," as if her time travel were borrowed. Ame has joked that Kronii "dislikes everything she likes," and Ame's alternate-Ame lore includes an "Epic Ame War" against Kronii that messed up time. On stream they played 5D chess neither understood, and Ame's last week of regular streams (2024) included Backrooms and Deep Rock Galactic with Kronii. Ame, now an affiliate, guested at Kronii's March 2026 birthday live, "The Goddess Descends." A small, fond pairing built on teasing and a shared bit about who owns time.
**[SW] Rules:** No one actually controls or travels through time; it is a shared joke. Ame plays the guilty borrower, Kronii the unimpressed Warden. In the 2026 baseline Ame appears as a guest, not a regular collab partner.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2021-08 | Kronii's announcement; "a certain time lord" joke | The lore rivalry |
| 2023-04-08 | 5D Chess ("I Don't Understand") | A time-travel game, fittingly |
| 2024-09 | Backrooms and DRG in Ame's last week | — |
| 2026-03-13 | Ame guests at Kronii's 3D birthday live | The affiliate's cameo |
**Dossier · Hard Facts (continuity):**
- Nobody actually time-travels; the rivalry is a lore joke.
- Ame guested at Kronii's 3D birthday live on 2026-03-13.

### Time and Death — `bible/world/Time-and-Death.md`
**[SW] Other Names:** Calli and Kronii, Kronii and Calli
**[SW] Description:** Mori Calliope and Ouro Kronii, the reaper and the Warden of Time: two low-voiced, deadpan sparring partners. Kronii's first official collaboration partner outside her own generation was Calli (2021). Calli calls her "Kronster"; their avatar heights are 168 cm and 167 cm, and Kronii never lets her forget the one centimeter. They billed themselves "Time and Death" in horror co-ops (Devour, the Backrooms, Lethal Company, The Outlast Trials) and share a cowboy TTRPG and a Powerwash "Get Your Shrek On." Their humor is mock feuds: when Kronii streamed a joke promotion of a made-up "$KRONII" coin in 2025, Calli answered with a mock exposé, "Exposing the Lies of $KRONII Coin" (a parody, not a real coin). They have collaborated repeatedly in horror and chaotic multiplayer games.
**[SW] Rules:** Their affection tends to come out as deadpan jabs, mock investigations and the height joke. Both swear when a horror game gets them. Kronii's schemes and Calli's exposés are bits, never real accusations.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2021-09-23 | Orcs Must Die! 3: Kronii's first cross-generation collab | The friendship's start |
| 2023 | Frequent horror and TTRPG co-ops; "Time and Death Say Howdy to Ghosts" | The duo's name |
| 2024-09-22 | Escape the Backrooms with Ame | One of Ame's last collabs |
| 2025-01 | The "$KRONII" coin bit and Calli's mock exposé | Mock feud |
**Dossier · Hard Facts (continuity):**
- First cross-generation collab for Kronii: with Calli, 2021-09-23.
- Kronii is 1 cm taller than Calli.

### Octo'Clock — `bible/world/OctoClock.md`
**[SW] Other Names:** Ina and Kronii, Kronii and Ina, Octo'clock, Octo'Clock
**[SW] Description:** Ninomae Ina'nis and Ouro Kronii, the octopus and the clock: longstanding collaborators whose 2026 Serendipity pairing foregrounds their shared puns, interests and performance work. They share Korean, a love of puns and occasional FGO streams, and in 2026 they were paired for hololive English's 4th concert "Serendipity" (Los Angeles, July 3–4) under the name "Octo'Clock" (the official report spells it "Octo'clock"), performing "Bad Apple." In their official interview Kronii called them "Just two punny people waiting to deliver the pun-chline to everyone" and praised Ina as "very hard-working and ambitious"; Ina said "I get to…keep Kronii….all to myself…..hehe…hehehe" and admired Kronii's "unmatched charisma whenever she sings." They had discussed shared interests and MC'd together at a hololive fes. Their goal was to "nail the performance," and, Kronii added mostly as a joke, "look cooler than everyone else."
**[SW] Rules:** Ina's claim on Kronii is a sweet joke, not romance. Their humor is dueling puns and deadpan; their work ethic is serious. Their stream collabs before 2026 were occasional (group numbers, FGO, R.E.P.O.), alongside shared stage work.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2022-02-25 | Ame's surprise karaoke off-collab (with Ina, Kronii, Fauna, Mumei) | — |
| 2023–2024 | FGO streams on Ina's channel | A shared game |
| 2026-06-04 | Official Serendipity interview | Their own words |
| 2026-06-24 | "It's Time for Octo'Clock!" short | The unit name |
| 2026-07-03/04 | Serendipity concert, Los Angeles | Their stage pairing |
**Dossier · Hard Facts (continuity):**
- Serendipity: 2026-07-03/04, Shrine Auditorium, Los Angeles.
- "Octo'Clock" is the pairing's name in Kronii's official short (2026-06-24).

### Fauna and Mumei Pairs — `bible/world/Fauna-and-Mumei-Pairs.md`
**[SW] Other Names:** Fauna and Mumei, Mumei and Fauna, It's Not a Phase, KronMei, gumei, Fauna and Gura, Mumei and Kiara, Mumei and Kronii
**[SW] Description:** Fauna and Mumei, Council's nature and civilization, collaborated during Council's debut week and remained recurring creative partners. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature") and Mumei's unexpectedly macabre responses. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights (2024-12). With the cast: Mumei and Kronii (KronMei) were frequent partners, including a "Donut Hole" cover duet (2025-04); Fauna and Kronii defused bombs speaking only in ASMR (2021). IRyS was their Promise unitmate; she and Mumei played Overwatch in Mumei's farewell week, then a Promise R.E.P.O. collab with IRyS, Kronii and Bae. Mumei and Kiara are birds of HOLOTORI; Kiara calls her "Moomsies" and hosted both on HOLOTALK before they left. Gura was Fauna's oshi; they drew hololive members from memory four days before Fauna graduated, and Gura and Mumei did a "ROOM REVIEW" together in Mumei's last week. Mumei also drew with Ina, did "Anatomy Review" with Calli, played with Ame in Ame's last regular week, and held "emo hours" with Nerissa; at the 2024 concert Mumei sang with Kiara and Nerissa, and Fauna with Shiori and Nerissa. Beyond EN, Mumei recorded a duet cover with Inugami Korone in her last week.
**[SW] Rules:** Fauna graduated on 2025-01-03 and Mumei on 2025-04-27 (04-28 JST); by this project's continuity rule, after those dates they appear only as memories and callbacks. Fauna's possessiveness and "return to nature" are performed bits. All of these are friendships.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2021-08-23 | Council debuts | Five concepts |
| 2021-08-25 | Fauna and Mumei's first co-op | Don't Starve Together: "Surviving in the wilderness with Mumei!" |
| 2021-09-13 | Minecraft together | "Adventuring with Mumei!" |
| 2023-03-19 | Mumei sings with Kiara on the 4th fes. stage | HOLOTORI |
| 2023-10-09 | -Promise- formed | — |
| 2024-08-24 | "It's Not a Phase" premiered at -Breaking Dimensions- | their duet (released 2024-12-22) |
| 2024-12-27 | Fauna on Kiara's HOLOTALK | — |
| 2025-01-03 | Fauna graduates | — |
| 2025-04 | Mumei's farewell month: "Donut Hole" with Kronii (04-11), Overwatch with IRyS (04-22), HOLOTALK (04-22), a Korone duet cover (04-23), Promise R.E.P.O. (04-24), Gura's room review | — |
| 2025-04-27 | Mumei graduates (04-28 JST) | — |
**Dossier · Hard Facts (continuity):**
- Fauna graduated 2025-01-03; Mumei 2025-04-27 (04-28 JST). After those dates they appear only as memories.
- Fauna's oshi: Gura. Kiara's name for Mumei: "Moomsies." HOLOTORI includes Kiara and Mumei.

### IRyS and Nerissa Pairs — `bible/world/IRyS-and-Nerissa-Pairs.md`
**[SW] Other Names:** MorIRyS, CHADCast, KiaRissa, IRyS and Kronii, IRyS and Ina, Nerissa and Calli, Nerissa and IRyS
**[SW] Description:** IRyS and Calli: Calli collabed with her on July 29, 2021, eighteen days after IRyS's debut; with Bae they host CHADCast ("Chaos, Hope, and Death!"), and they still team up (Silent Hill 2 as "Two Pink Women," karaoke). IRyS and Kronii: Promise unitmates since 2023 and friends since 2021, regulars at two-player games (A Way Out, Bokura, a Powerwash race, "May The Best Maid Win"); in 2026 IRyS said she could pull off Kronii's goddess look "somehow." IRyS and Ina: an early duo (It Takes Two, "It Takes Tako & Hope") who still play together. IRyS and Kiara: Kiara gave her a German crash course; nail-painting off-collab. Nerissa and Kiara (KiaRissa): Kiara is Nerissa's oshi; Kiara showed her around Minecraft; a 2025 "BIRB GIRLS" GIRLSTALK. Nerissa and Calli: a Baldur's Gate 3 party, the 2025 duet "OVER//RIDE," and Calli as a guest at Nerissa's 3D concert. Nerissa and IRyS: two singers; IRyS guested at that concert, and Nerissa put IRyS and Ina in Tomodachi Life.
**[SW] Rules:** IRyS (2021) is Nerissa's senior; Myth are seniors to both. Recent pairings (IRyS with Kronii, Calli and Ina; Nerissa with Kiara and Calli) carry the most weight; pairs with Gura are memories. All are friendships and stream bits.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2021-07-29 | Calli's first collab with IRyS | MorIRyS |
| 2022-01-30 | First CHADCast | Chaos, Hope, and Death |
| 2023-08-14 | Nerissa's compatibility test with Kiara | KiaRissa |
| 2023-10-09 | -Promise- formed: IRyS and Kronii become unitmates | — |
| 2025 | Nerissa's 3D concert with Calli and IRyS as guests; "OVER//RIDE" duet | Calli × Nerissa |
| 2026-04-23 | Nerissa's Tomodachi Life Miis of IRyS and Ina | — |
**Dossier · Hard Facts (continuity):**
- IRyS debuted 2021-07-11 (senior to Kronii by a month, to Nerissa by two years); Nerissa 2023-07-31.
- CHADCast = IRyS, Calli, Bae. KiaRissa = Kiara and Nerissa. IRyS and Kronii are -Promise- unitmates; they debuted separately.
- 2026 baseline: IRyS–Gura and Nerissa–Gura are memories; Ame appears as an affiliate guest.

### Hakos Baelz Pairs — `bible/world/Hakos-Baelz-Pairs.md`
**[SW] Other Names:** Bae and IRyS, BaeRyS, CHADCast, BaeBi, BratTea, Bae and Kronii, Bae and Calli, Bae and Cecilia
**[SW] Description:** Hakos Baelz's ties with the cast. With IRyS she is BaeRyS: a performed "married and divorced" routine that fan references trace to a Minecraft bento exchange, covers and off-collabs, "High Tide" with Moona Hoshinova and Hoshimachi Suisei on stage in 2024, and their first duo stage, "LUVATORRRRRY!", at Serendipity 2026; in a pre-concert interview Bae says she was "blown away" by IRyS's voice, and IRyS admires Bae's creativity and calls their dynamic "a can of worms." With IRyS and Mori Calliope she is CHADCast (Chaos, Hope and Death), a podcast trio archived from January 2022, with the song "Here Comes the CHADCast" (2026); they sang "BLUE CLAPPER" with Koseki Bijou in 2024, and Bae and Calli sang "R x R x R" in 2025. In Promise she plays games with Ouro Kronii (Sandwich Review, Fortnite) and sang "Dance Monkey" with Kronii and IRyS in Sydney (2025); with the graduated Fauna she played Amnesia ("Month of Horrors," 2022), and the graduated Mumei joined her lessons and off-collabs. With Bijou she is "BaeBi" (a 2024 sleepover marathon); with Cecilia Immergreen, "BratTea," a coffee-versus-tea debate by Bae's account; she sang "Countach" with Gigi Murin and Kureiji Ollie (2025) and "HELP!!" with Kobo Kanaeru and Elizabeth Rose Bloodflame (2026), and FUWAMOCO danced to her "SNAKE EYES." Fan references call Keep Talking and Nobody Explodes with Takanashi Kiara (2021) her first official collab outside Council.
**[SW] Rules:** These entries record public collaborations and performed bits; the BaeRyS "marriage" is a comedy routine, not a romance. Fauna, Mumei, Gura and Sana appear only as memories after their graduations; Ame is an affiliate. Collab titles show that a collab happened, not how close two members are.
**Dossier · History:**
| Date | Event | Pair |
|---|---|---|
| 2021-09-24 | Keep Talking and Nobody Explodes | Bae–Kiara |
| 2022 | CHADCast begins; "Month of Horrors" (October) | Bae–Calli–IRyS; Bae–Fauna |
| 2023 | a BaeRyS off-collab; "Daikirai na Hazu Datta"; K/DA "POP/STARS"; We Were Here | BaeRyS; Bae–Ina; BaeBi |
| 2023-10-09 JST | -Promise- formed | Bae with IRyS, Fauna, Kronii, Mumei |
| 2024-08-11/12 | #BAEBISleepover | BaeBi |
| 2024-08-24/25 | -Breaking Dimensions-: "Our Promise," "BLUE CLAPPER," "High Tide" | Promise; CHADCast + Bijou; BaeRyS |
| 2024-11-25 | #BaeTV24 24-hour stream | with IRyS, Raora, Kronii, Bijou, Gigi |
| 2025-08-23/24 | -All for One-: "R x R x R," "Countach" | Bae–Calli; Bae–Gigi (with Ollie) |
| 2026-03 | 7th fes: venue talk; Resident Evil series (April) | Bae–Cecilia |
| 2026-07-03/04 PDT | Serendipity: BaeRyS "LUVATORRRRRY!"; "HELP!!" | BaeRyS; Bae–Elizabeth (with Kobo) |
**Dossier · Hard Facts (continuity):**
- Official stage units: BaeRyS (IRyS & Bae, Serendipity 2026); CHADCast is a podcast trio (Calli, IRyS, Bae).
- Concert pairings: "BLUE CLAPPER" (Calli, IRyS, Bae, Bijou; 2024); "High Tide" (IRyS, Bae, Moona, Suisei; 2024);
  "R x R x R" (Calli & Bae; 2025); "Countach" (Bae, Gigi, Ollie; 2025); "HELP!!" (Kobo, Bae, Elizabeth; 2026).

Incoming claims continue in `promise-incoming.md`.

### projects/holoen/research/qa/packets/promise-incoming.md

# Audit packet: promise (incoming claims)

Snapshot: git ebbab25.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: ardian of Civilization|IRyS and Nerissa Pairs|Fauna and Mumei Pairs|hololive -Promise-|Hakos Baelz Pairs|Nerissa and Calli|Calli and Kronii|It's Not a Phase|Nerissa and IRyS|Keeper of Nature|Mumei and Kronii|hololive Council|Kronii and Calli|IRyS and Kronii|Mumei and Kiara|Mumei and Fauna|Bae and Cecilia|Fauna and Mumei|Warden of Time|Kronii and Ame|Fauna and Gura|Bae and Kronii|Time and Death|Ame and Kronii|Ina and Kronii|Kronii and Ina|Mother Nature|Nanashi Mumei|Bae and Calli|IRyS and Ina|Kroniicopter|Bae and IRyS|holoPromise|Ceres Fauna|Ouro Kronii|Hakos Baelz|holoCouncil|Gamer Kirin|Ceres-chan|Tam Tender|Octo'Clock|Octo'clock|Owo-senpai|CouncilRyS|Mumi-chan|Time Duo|オーロ・クロニー|CHADCast|KiaRissa|YabaIRyS|SeisoRyS|Rat Idol|Kronster|Moomsies|Kronini|Promise|MorIRyS|Council|Moomers|KronMei|BratTea|Faufau|BaeRyS|Meimei|Kronii|Baelz|Fauna|Mumei|BaeBi|gumei|Hakos|Fawna|IRyS|Irys|Moom|Towl|Bae)(

### from AZKi
- `bible/characters/AZKi.md › [SW] Background`: Her units include SorAZ with Tokino Sora, AS_tar with Suisei ("Going My Way," 2026), Star Flower with Suisei, Moona Hoshinova and IRyS ("story time," 2022), AzuIro with Kazama Iroha ("AZUIRO BESTIE DAYS," 2025) and, from 2026, RosaMiA.
- `bible/characters/AZKi.md › [SW] Background`: With the English cast she sings in Star Flower with IRyS, took Calli's English lesson (2022), was Kiara's 13th HOLOTALK guest (2021), and played a FUWAMOCO-themed GeoGuessr map with the twins (2024), who also appeared at her 2025 birthday live.
- `bible/characters/AZKi.md › [SW] Relationships`: IRyS: Star Flower with Suisei and Moona Hoshinova ("story time," 2022); IRyS covered AZKi's "Inochi"
- `bible/characters/AZKi.md › [SW] Relationships`: Mori Calliope: her English lesson with IRyS and Tsunomaki Watame (2022); AZKi's "Orpheus" dance short (2025).
- `bible/characters/AZKi.md › [SW] Relationships`: Hakos Baelz: GeoGuessr (2023).
- `bible/characters/AZKi.md › [SW] Relationships`: Ouro Kronii and Elizabeth Rose Bloodflame: fellow members of Tokoyami Towa's 2025 New Year Game Festival team.
- `bible/characters/AZKi.md › [SW] Relationships`: Ninomae Ina'nis and Kronii: R.E.P.O.
- `bible/characters/AZKi.md › Voice Profile`: - **Language:** streams in Japanese; she participated in Calliope's English lesson with IRyS and Watame (2022, archived metadata). [Observed AZ5]
- `bible/characters/AZKi.md › Background Timeline`: | 2022-03-12 | Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame | [AZ5 32NVpmKdAOs] |
- `bible/characters/AZKi.md › Background Timeline`: | 2022-12-31 | "story time" as Star Flower with Suisei, Moona Hoshinova and IRyS | [Official AZ6] |
- `bible/characters/AZKi.md › Background Timeline`: | 2023-03-09 | GeoGuessr with Hakos Baelz | [AZ5 T594r3CnuW8] |
- `bible/characters/AZKi.md › Background Timeline`: | 2025-07-19 | R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora, Ina, IRyS and Kronii (the description's lineup) | [AZ4 _gZdFTluxtc] |
- `bible/characters/AZKi.md › Background Timeline`: | 2026-03-07 | hololive 7th fes. "Ridin' on Dreams," STAGE 3 (with IRyS, Bae, Shiori) | [Official AZ7] |
- `bible/characters/AZKi.md › Background Timeline`: | 2026-07-01 | "AZKi 8th Birthday Live 'Cross Over'": little-devil outfit; she performed Konomi Suzuki's "Redo"; IRyS appears in the archived short metadata ("A Cruel Angel's Thesis"; secondary setlist); "Saikyo Mirai Shodo" (credited to AZKi and Konomi Suzuki) released digitally 07-02 | [Observed AZ2; AZ4] [Official AZ11] [secondary setlist] |
- `bible/characters/AZKi.md › Relationship Map`: | IRyS | Star Flower | "story time" (2022); IRyS's "Inochi" cover (2021-07-18, archived); Calli's English lesson (2022); R.E.P.O. JP & EN (2025); "A Cruel Angel's Thesis" at Cross Over (2026, secondary) | [Official AZ6] [AZ5] |
- `bible/characters/AZKi.md › Relationship Map`: | Hakos Baelz | — | GeoGuessr, "lost simulator" (2023); Bae's MMD dance to AZKi's "Oki Doki" (2025) | [AZ5] |
- `bible/characters/AZKi.md › Relationship Map`: | Ouro Kronii, Elizabeth Rose Bloodflame | — | Fellow members of Tokoyami Towa's 2025 New Year Game Festival team (secondary roster) | [AZ4] |
- `bible/characters/AZKi.md › Relationship Map`: | Ninomae Ina'nis, Ouro Kronii, IRyS | — | R.E.P.O. "JP & EN" (2025-07-19); Elizabeth was not in it | [AZ4 _gZdFTluxtc] |
- `bible/characters/AZKi.md › Story Engine`: 2. A duet rehearsal with IRyS where AZKi's "Floor!" interrupts every chorus.

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: IRyS and Bijou: Elden Ring Nightreign.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Nanashi Mumei ("Automatowl"): Halo co-op.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Ouro Kronii: Kronii has called her "CLANKER"; she calls Kronii "Owo-senpai"; "Clockwork Orange" with Gigi.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Ceres Fauna ("Green Women"): a shoujo-tropes ranking.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Hakos Baelz ("BratTea," a secondary-reference name): by Bae's account in her 2026 streams, a coffee-versus-tea debate, a venue talk together at the 2026 fes and Resident Evil collaborations; Bae jokes that Cecilia calls her "senpai" when she wants something.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Watson Amelia (affiliate): Borderlands 2 with Gigi and Mumei (2024).
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Nanashi Mumei | Promise alumna ("Automatowl," secondary) | Halo: Reach (2024), "Ask us anything" (2025); the nickname "Myumyei" is unverified and not used | [Observed CI2, CI3] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Ouro Kronii | Senior ("Clockwork Orange" with Gigi; secondary) | Phogs, Squirreled Away (2025); Kronii has called her "CLANKER"; she calls Kronii "Owo-senpai" (secondary transcriptions; not a call-and-response) | [Observed CI3; Kronii file] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Ceres Fauna | Promise alumna ("Green Women") | A shoujo-manga tropes ranking (2024) | [Observed CI2, CI3] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Gawr Gura, IRyS, Hakos Baelz | Seniors | Keep Talking and Nobody Explodes and The Forest with Gura (2025); Elden Ring Nightreign with IRyS and Bijou (2025); "BratTea" with Bae: a running coffee-versus-tea debate, a venue talk together at the 2026 fes, and a 2026 Resident Evil series on Cecilia's channel (Bae's own streams, ASR) | [Observed CI2, CI3] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Nekomata Okayu, Hoshimachi Suisei, Nakiri Ayame | JP seniors | Listed with Ina and IRyS among the members of Okayu's 2025 New Year Game Festival team (archived team listing) | [Okayu file OK4] [Ayame file AY5] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Background`: She debuted first of her generation on 2024-06-21 (PDT) in hololive English -Justice-, held her 3D showcase on 2025-08-01 (PDT), sang at the 2025 English concert ("ALiCE&u" with Nerissa and Ayunda Risu, a solo "Stellar Stellar," and the day-two opener "START AGAIN" with Calli, IRyS and Nerissa), invited guests from several branches to her 2026 birthday live, and at the 2026 Serendipity concert sang "HELP!!" with Kobo Kanaeru and Hakos Baelz and formed the unit Bloodraven with Nerissa Ravencroft ("Cruel Angel's Thesis").
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: (with Calli and IRyS); Elizabeth says Nerissa "has a beautiful voice,"
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Kobo Kanaeru and Hakos Baelz: "HELP!!" at Serendipity.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Kureiji Ollie (ID): her kami-oshi and "Code Red" partner (PEAK with HOLOSTARS' Machina X Flayon and Jurard T Rexford; "High Tide" on stage with Kronii); Crimzon Ruze (HOLOSTARS) is her "Nephew" in a Marvel Rivals uncle–nephew bit.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Shirogane Noel and Kikirara Vivi: Mumei's Gartic Phone EN + ID + JP collab (2025).
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: AZKi: fellow member of Tokoyami Towa's 2025 New Year Game Festival team, with Kronii (secondary roster).
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Ninomae Ina'nis: co-players in Mumei's cross-branch Gartic Phone (2025).
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie | [Official EB5] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Nerissa Ravencroft | Advent senior; lore "mortal enemy"; Serendipity 2026 unit Bloodraven | A "Rondo Revolution" cover; "ALiCE&u" (with Ayunda Risu) and "START AGAIN" (with Calli and IRyS) at -All for One-; "Cruel Angel's Thesis" as Bloodraven (2026); Elizabeth: "She has a beautiful voice," "the perfect harmony"; Nerissa praises her kindness. Nerissa has been "calling me her husband, my husband" (Elizabeth, 2025), a performed bit | [Official EB4, EB5] [Observed EB2] [ASR EB20, Rk03Rh8P9ps 0:38:00] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kureiji Ollie | ID senior; her "kami-oshi" (secondary); "HoloRed" | "Code Red" collabs: Liars Bar with Ollie and Jurard (2024), PEAK with Ollie, Flayon and Jurard (2025); "High Tide" with Kronii and Ollie at -All for One-; the 2026 "Yona Yona Dance" cover | [Observed EB2, EB3] [Official EB5] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kobo Kanaeru, Ayunda Risu | ID seniors | "HELP!!" with Kobo and Hakos Baelz at Serendipity (2026); Kobo calls her "Lilis" (secondary); LYRA and "ALiCE&u" with Risu | [Observed EB2] [Official EB5, EB8] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Shirogane Noel, Kikirara Vivi | JP members | Mumei's Gartic Phone EN + ID + JP (2025-04-14) | [Shirogane Noel file NO5; Kikirara Vivi file VI5; archive metadata OMDzBQohAf8, inherited and not reopened] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | AZKi | — | Fellow members of Tokoyami Towa's 2025 New Year Game Festival team, with Kronii (secondary roster) | [AZKi file AZ4] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Ninomae Ina'nis | Myth senior | Co-players in Mumei's Gartic Phone EN + ID + JP, Day 2 (2025-04-14). | [Archive metadata TIE-014] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Story Engine`: 1. Elizabeth impersonates Kronii on a call and Kronii answers.

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Ouro Kronii: "WatchDog."
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "Fuwamoomco"
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Hakos Baelz: Gigi's 2025 Spring Party; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES"
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: IRyS, Gigi and Kronii: "Bright Tonight"
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Ceres Fauna (graduated): FUWAMOCO helped on the World Tree's last day (2024-12-31).
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Hakos Baelz | Promise senior | Archived metadata: Gigi's 2025 Spring Party with FUWAMOCO and Bae (2025-03-31); a FUWAMOCO short dancing to "bae-senpai's new song SNAKE EYES" (2026-03-20) | [Bae file HB3, HB5, HB8, HB20] |

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Raora Panthera: R.E.P.O. with Kiara and Kronii (2025).
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Hakos Baelz: an Urban Dictionary Challenge with Kronii and Mumei on Bae's stream (2022).
- `bible/characters/Gawr-Gura.md › Voice Profile`: - Measured (G18; chat and horror windows, with game audio mixed in): median pitch about 245–270 Hz (Kronii's chat windows 177–188 Hz); about 120–140 words per minute of speech in the 2024 chat. Sample results only; they do not establish a general ranking among genmates. (The earlier caption-timing estimate is withdrawn.)
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ceres Fauna, Nanashi Mumei, Ouro Kronii | Council members ("SNOTCast") | Shared podcast-style collabs; Kronii rivalry and "senpai tax" bits are reported but [Unverified] (title-level only) | [Observed G2 §Relationships; G8b titles] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | IRyS | Promise member | Sincere praise of IRyS's new look (clip title) | [Observed G8b title] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Hakos Baelz | Council kouhai | An Urban Dictionary Challenge with Kronii and Mumei (2022-08-20, Bae's stream; archived metadata jWvpe0Hs5wI) | [Bae file HB3, HB5, HB8, HB20] |

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Background`: "Countach" with Hakos Baelz and Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, "III" with Nerissa).
- `bible/characters/Gigi-Murin.md › [SW] Background`: (presented on her 2025 birthday), "Bright Tonight" with IRyS, Kronii and FUWAMOCO (2025), and "enough"
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Ouro Kronii: Fatal Fury and Hytale; "MONSTER" with Kronii, Ina and Shiori.
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: IRyS, Kronii and FUWAMOCO: "Bright Tonight."
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Hakos Baelz: "Countach" with Kureiji Ollie (ID) on stage (2025), a dramatic reading of A Midsummer Night's Dream on Bae's stream, and Gigi's 2025 Spring Party with FUWAMOCO and Bae.
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Ceres Fauna: Silent Hill 2 and The Coughing Baby Award Show.
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Nanashi Mumei: Echo Point Nova.
- `bible/characters/Gigi-Murin.md › Behavioral Traits`: 7. A creative, sentimental side: she performs original songs: "I'll still be here" (presented 2025-10-18, digital 10-20), "Bright Tonight" (a group release with IRyS, Kronii and FUWAMOCO, 2025-12-22), "enough" (2026-06-25; composed by FLAVORFOLEY) and "CCGG MADNESS" with Cecilia (MV 2026-05-17, digital 05-29; lyrics by Cecilia with help from Nerissa and Gigi; chibi-model design by Gigi). [Official GG1 music list, GG7] [Observed GG3 credits]
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa | [Official GG5] |
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2025-12-22 | "Bright Tonight" with IRyS, Kronii and FUWAMOCO released | [Official GG7] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Ouro Kronii | Senior ("TimeChaser"; "Clockwork Orange" with Cecilia; secondary pair names) | Fatal Fury (2025), Hytale (2026); "MONSTER" at -All for One-; "Bright Tonight" (2025) | [Observed GG2, GG3] [Official GG5, GG7] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Hakos Baelz, Kureiji Ollie (ID) | Senior; cross-branch | "Countach" at -All for One- (2025); with Bae, a "BAE THEATRE" dramatic reading of A Midsummer Night's Dream (2025-02-05), UNO on Bae's 24-hour stream (2024-11-25) and Gigi's 2025 Spring Party with FUWAMOCO and Bae (2025-03-31); Ollie's part is "Countach" only | [Official GG5] [Bae file HB3, HB5, HB8, HB20] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | IRyS | Senior | "Bright Tonight" (2025) | [Official GG7] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Ceres Fauna, Nanashi Mumei | Promise alumnae ("FruitPunch"; "A Towl and a Gremlin"; secondary) | Fauna: The Coughing Baby Award Show; Mumei: Echo Point Nova | [Observed GG2, GG3] |

### from Hakui Koyori
- `bible/characters/Hakui-Koyori.md › [SW] Background`: (2024), and guest appearances at FUWAMOCO's birthday concert (2025) and Mumei's first 3D live (2024).
- `bible/characters/Hakui-Koyori.md › [SW] Background`: In 2023 she joined Bae's "BAE-GEMITE DOMINATION" with Momosuzu Nene and tasted Bae's "KHAOS KITCHEN" curry with Calli and Oozora Subaru.
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: Hakos Baelz: BAE-GEMITE DOMINATION with Nene and a KHAOS KITCHEN tasting (2023).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: Nanashi Mumei (graduated): a guest at her first 3D live (2024).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: IRyS: Splatoon 3 (2022) and Among Us (2023).
- `bible/characters/Hakui-Koyori.md › Voice Profile`: - **Language:** streams in Japanese; with the English cast she has guested on FUWAMOCO's English-language morning show and played with them, Bae, IRyS and others. [KO5]
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2023-04-22 | "BAE-GEMITE DOMINATION" episode 4 with Bae and Momosuzu Nene | [KO5 WwjB7QSmQng] |
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2024 | Lethal Company with FUWAMOCO and Fubuki (03-09); FUWAMOCO Morning episode 90 guest, billed #FUWAMOKOYO (04-26); a guest at Mumei's first 3D live (08-05) | [KO5 XR1PEtj15kE, gCYXKgYcFmk, gl7CwlEg2ZI] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Hakos Baelz | — | "BAE-GEMITE DOMINATION" episode 4 with Nene (2023-04-22); a "KHAOS KITCHEN" taste tester with Calli and Oozora Subaru (2023-11-24) Co-credited singers on the hololive Dreams theme "PARADISE!" (MV 2026-09-28; seven singers). | [KO5 WwjB7QSmQng, NdLiUW-nUlk] [Secondary, dengekionline 202609/89494] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Nanashi Mumei (graduated) | — | A guest at Mumei's first 3D live, "Outside the Box" (2024) | [KO5] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | IRyS | — | Splatoon 3 with Watame and Korone (2022-10-03) and an Among Us lobby with Chloe and others (2023-05-08) | [KO5 Xoma7oWsMcM, VwqdwQx5cog] |

### from Hoshimachi Suisei
- `bible/characters/Hoshimachi-Suisei.md › [SW] Background`: With the English cast she made "CapSule" and "Wicked" with Calli (2022) and sang "Wicked" at Calli's first solo concert, sings with IRyS, AZKi and Moona as Star Flower, sang "High Tide" and "BIBBIDIBA" at the 2024 English concert, and was a face of hololive night at Dodger Stadium with Gura and Pekora (2024).
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: IRyS: Star Flower with AZKi and Moona Hoshinova ("story time," 2022); "High Tide" with IRyS, Moona and Hakos Baelz at the 2024 English concert.
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Hakos Baelz: a "Moonlight" dance cover (2025).
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Nanashi Mumei (graduated): a #bibbidibachallenge short (2024).
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Nekomata Okayu: "MOMAS"; Okayu's 2025 New Year Game Festival team with Nakiri Ayame, Ina, IRyS and Cecilia, among others.
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2022-12-31 | "story time" as Star Flower with AZKi, Moona Hoshinova and IRyS | [Official SU6] |
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2024-08-24/25 | "High Tide" with IRyS, Moona and Hakos Baelz, and "BIBBIDIBA" with Moona, Ina and Gura, at the English concert -Breaking Dimensions- | [Official SU8] |
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2026-03-08 | hololive 7th fes. "Ridin' on Dreams," STAGE 4 (with Calli, Kronii, Bijou, Nerissa) | [Official SU9] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | IRyS | Star Flower | "story time" (2022); "High Tide" (2024); IRyS covered "GHOST" (2021); on Okayu's 2025 New Year Game Festival team (secondary roster) | [Official SU6, SU8] [S1] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Hakos Baelz | — | "High Tide" (2024); Bae's "Moonlight" dance cover (2025-01-07) | [Official SU8] [S1] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Nanashi Mumei (graduated) | kouhai | A #bibbidibachallenge short together on Suisei's channel (2024-06-18) | [SU4 zSB9yejsmGQ] |

### from Houshou Marine
- `bible/characters/Houshou-Marine.md › [SW] Background`: Archived metadata records her with the English cast as Kiara's first HOLOTALK guest (2020), on Calli's first English lesson (2022), at an off-collab house party with Calli and Bae (2023), in off-collabs with FUWAMOCO and Nerissa (2024) and as a guest at Ina's "Pleides"
- `bible/characters/Houshou-Marine.md › [SW] Background`: (2024); she features in the horror game "Truth of Beauty Witch," which Calli, and Bae with Mumei, played, and she sang for Elizabeth's 2026 birthday.
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Mori Calliope: Calli's English lesson #01 (2022), Mario Kart (2021) and a house-party off-collab with Bae (2023).
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Hakos Baelz: that Mario Kart and house party; Bae and Mumei played the horror game featuring Marine (2023).
- `bible/characters/Houshou-Marine.md › Voice Profile`: - **Language:** streams in Japanese; archived metadata records her as a guest on Calli's first English lesson (2022) and Kiara's first HOLOTALK (2020), and joining off-collabs with Calli and Bae (2023), FUWAMOCO and Nerissa (2024). [MA5]
- `bible/characters/Houshou-Marine.md › Background Timeline`: | 2023-08 | The horror game "Truth of Beauty Witch -Marine's treasure ship-" features her (Calli played it 08-14; Bae with Mumei 08-23); an off-collab house party with Calli and Bae (08-14) | [Observed MA2 §Events] [MA5 Mf-sAjsuSig, RY1GkF4jMls, DY5VThfehW8] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Mori Calliope | — | English lesson #01 (2022); Mario Kart with Bae and Reine (2021); a house-party off-collab with Bae (2023); Calli played the horror game featuring Marine on her own stream (2023) | [MA5 bfUEbp3xk4o, X3pHIQAvpYU, DY5VThfehW8, Mf-sAjsuSig] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Hakos Baelz | — | Mario Kart (2021); the house party (2023); Bae and Mumei played the horror game featuring Marine (2023); dance covers Co-credited singers on the hololive Dreams theme "PARADISE!" (MV 2026-09-28; seven singers). | [MA5] [Secondary, dengekionline 202609/89494] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Nanashi Mumei (graduated) | — | Played the horror game featuring Marine with Bae (2023) | [MA5 RY1GkF4jMls] |

### from Kikirara Vivi
- `bible/characters/Kikirara-Vivi.md › [SW] Background`: Archived metadata records her with the English cast in R.E.P.O. with FUWAMOCO and Bae (2025-05-25), in a separate R.E.P.O. session on Ina's stream (2025-06-02) and in Mumei's Gartic Phone collaboration with Noel, Kronii, Ina and Elizabeth (2025); a secondary archive records FUWAMOCO and Bijou watching FLOW GLOW's debut.
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Shirogane Noel: Mumei's Gartic Phone collab (2025).
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: FUWAMOCO: watched FLOW GLOW's debut with Bijou (2024, secondary archive); R.E.P.O. with Bae (2025-05-25).
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Hakos Baelz: that R.E.P.O. session.
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone (2025).
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Nanashi Mumei (graduated): hosted that Gartic Phone collab.
- `bible/characters/Kikirara-Vivi.md › Voice Profile`: - **Language:** streams in Japanese (a voice feature only); archived metadata records R.E.P.O. with FUWAMOCO and Bae (2025-05-25), a separate R.E.P.O. session on Ina's stream (2025-06-02) and Mumei's Gartic Phone collab with Noel, Kronii, Ina and Elizabeth (2025). [VI5]
- `bible/characters/Kikirara-Vivi.md › Background Timeline`: | 2025-04-14 | Gartic Phone EN + ID + JP collab with Mumei, Kronii, Ina, Elizabeth and Noel | [VI5 OMDzBQohAf8] |
- `bible/characters/Kikirara-Vivi.md › Background Timeline`: | 2025-05-25 | #holoREPO with FUWAMOCO, Bae, Roboco, Towa and Hajime | [VI5 Z5cpzbdsLDE, TgMVtjXW2Ms] |
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Hakos Baelz | — | #holoREPO (2025) | [VI5] |
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Ouro Kronii, Elizabeth Rose Bloodflame | — | Gartic Phone EN + ID + JP (2025) | [VI5] |
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Nanashi Mumei (graduated) | — | Hosted that Gartic Phone collab (2025) | [VI5] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Background`: (2025), starred with Ina and IRyS at hololive night at Dodger Stadium (2025), sang a solo and two group numbers at the 2025 English concert -All for One-, and was paired with Takanashi Kiara at the 2026 Serendipity concert.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: IRyS: her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina, they headlined hololive night at Dodger Stadium (2025).
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Hakos Baelz: "BaeBi"
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: (We Were Here, a 2024 sleepover marathon); with Bae, Calli and IRyS she sang "BLUE CLAPPER" at the 2024 English concert.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "Stone Age"; Mumei rated her a loss at arm wrestling because "she is a rock."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Ceres Fauna (graduated 2025): her Hitman "coach."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Ouro Kronii: Lethal Company and Yu-Gi-Oh. -Justice-: GAGA with Gigi and Cecilia; Graondstone with Raora; "I'm Your Treasure Box" with Cecilia and Raora at the 2025 concert; Cecilia's Walking Dead watchalongs and a 2025 Elden Ring stream Bijou joined partway; Raora's 2024 cooking off-collab, billed with Bijou as her assistant.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2024-08-11 | #BAEBISleepOver with Hakos Baelz | [Observed KB3] |
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-07-05 | hololive night at Dodger Stadium with Ina and IRyS: a stadium sing-along and the first VTuber stream from the stadium | [Official KB9] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | IRyS | Senior | Her frequent horror co-op partner: Resident Evil 6 "LAS CHICAS GUAPAS" (2026-04-29), Dead Space 3 (2026-01); Overwatch "Please carry me Senpai!!" (2023) IRyS hosted a joint *Gundam 0080* watchalong (2026-09-05). | [Observed KB3; IRyS archive] [Archive metadata, holosubs IRyS listing] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Hakos Baelz | Senior ("BaeBi") | We Were Here (2023); a JoJo watch-along (2024); #BAEBISleepOver (2024-08-11/12); UNO on Bae's #BaeTV24 stream (2024-11-25); "BLUE CLAPPER" with Bae, Calli and IRyS at -Breaking Dimensions- (2024) Co-credited vocalists (with the other two) on "Freaky Deaky Love" (2026-05-31). | [Observed KB3; Bae archive] [Bae file HB3, HB5, HB8, HB20] [Official NEW-R3-007] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Nanashi Mumei | Senior (graduated 2025; "Stone Age") | Portal 2 co-op (2023); Marvel Rivals in Mumei's last week (2025-04-23); Mumei rated her a loss at arm wrestling because "she is a rock" | [Observed KB3; Mumei file] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Ceres Fauna | Senior (graduated 2025) | "Coach" Fauna in Hitman (2023, 2024); PlateUp! as "The Sweaty TryHard Gamers" | [Observed KB3] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Ouro Kronii | Senior | Lethal Company (2023), Yu-Gi-Oh (2025), Blood Typers (2025) | [Observed KB3] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Cecilia Immergreen, Raora Panthera, Gigi Murin | Justice kouhai | GAGA (with Shiori and Gigi); Graondstone (with Kaela and Raora); a Walking Dead off-collab watchalong with Cecilia (2025) Raora is a co-credited vocalist (with Kiara and Bae) on "Freaky Deaky Love" (2026-05-31). | [Observed KB2; KB3] [Official NEW-R3-007] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Ouro Kronii: "WatchDog."
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "Fuwamoomco."
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Hakos Baelz: Gigi's 2025 Spring Party with FUWAMOCO and Bae; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES"
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: IRyS, Gigi and Kronii: "Bright Tonight"
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Ceres Fauna (graduated): FUWAMOCO helped on the World Tree's last day (2024-12-31).
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Ouro Kronii | Senior ("WatchDog," with Fuwawa) | Among Us, Team Fortress 2, 7 Days to Die (2023–24) | [Observed MC2; MC3] |
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Hakos Baelz | Promise senior | Archived metadata: Gigi's 2025 Spring Party with FUWAMOCO and Bae (2025-03-31); a FUWAMOCO short dancing to "bae-senpai's new song SNAKE EYES" (2026-03-20) | [Bae file HB3, HB5, HB8, HB20] |

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Groups`: hololive, hololive -Myth-, Myth, CHADCast, hololive English (former branch name), Last Writes
- `bible/characters/Mori-Calliope.md › [SW] Background`: She co-hosts the CHADCast podcast with IRyS and Hakos Baelz, and she started a 2026 performance partnership with Shiori Novella.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: IRyS and Hakos Baelz: her CHADCast cohosts ("Chaos, Hope, and Death"; "BLUE CLAPPER" with Bijou, 2024; "Here Comes the CHADCast," 2026); Bae sang "R x R x R" with her (2025); IRyS joined her as the "Two Pink Women" of Silent Hill 2.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022).
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Ceres Fauna: Fauna's five-player Dota 2 collab (2024).
- `bible/characters/Mori-Calliope.md › Voice Profile`: - Measured (C30, chat windows): median pitch 197–214 Hz, the second lowest of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz). The wiki's hololive-wide ranking was not measured. She is the fastest talker of the six: about 161–186 words per minute of speech while chatting (Kronii 120–127, Ina 81–95). Approximate values for relative comparison.
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2022 | CHADCast begins with IRyS and Hakos Baelz. | [Observed C12] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | IRyS, Hakos Baelz | CHADCast cohosts | A chaotic podcast trio (archived from January 2022); their song "Here Comes the CHADCast" (2026-09-01). Secondary references record Bae's nickname for her, "Cori Malliope." "BLUE CLAPPER" with Bijou at -Breaking Dimensions- (2024); the "R x R x R" duo with Bae at -All for One- (2025); Bae's GriMoire watch-along (2025) Calli and IRyS (with Nerissa, Momosuzu Nene and Kureiji Ollie) are credited singers on "LIVE IT LOUD!" (2025-06-25). | [Observed C12; C4 nickname list, secondary] [Official NEW-R1-005] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Ouro Kronii | Fellow EN | Calli calls her "Kronster." Running bit: the 1 cm height difference. | [Observed C21-jVfm_LhwTHQ clip title; Kronii's wiki page, secondary] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Houshou Marine, Shirogane Noel, Shishiro Botan | JP seniors | HOLO ENGLISH LESSON #01 with Marine, Ina and Fubuki (2022-02-19); Mario Kart with Marine, Bae and Reine (2021-12-25); a house-party off-collab with Marine and Bae and a playthrough of Marine's horror game (2023-08-14); HOLOYOI #02 with Noel and Flare (2023-04-20) and #03 with Botan and Subaru (2023-05-18) | [S1 bfUEbp3xk4o, Tpzbfccp_ZM, DY5VThfehW8, Mf-sAjsuSig, wyrLR1CC1Co, EatMZc1N3VM] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Ceres Fauna | Council | Fauna's five-player Dota 2 session with Calli, Bijou, Nerissa and Kobo (2024-01-27 JST). | [Member upload, indexed TIE-010] |

### from Nakiri Ayame
- `bible/characters/Nakiri-Ayame.md › [SW] Background`: With the English cast, archived metadata identifies her as Kiara's 23rd HOLOTALK guest (2022-10-09), places her on the 2023 Sports Festival white team with Kiara, Mumei, Ame, Nerissa and AZKi (her stream title celebrates its win), and lists her with Suisei, Ina, IRyS and Cecilia among the members of Okayu's 2025 New Year Game Festival team; she shared 7th fes STAGE 1 with Ina and FUWAMOCO (2026), and the official Anime NYC 2026 announcement listed her, Fubuki and Mio for an August 22 convention-exclusive stream.
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: Hoshimachi Suisei, Ninomae Ina'nis, IRyS and Cecilia Immergreen: listed among the members of Okayu's 2025 New Year Game Festival team; Ina and FUWAMOCO shared her 7th fes stage.
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: AZKi, Nanashi Mumei, Watson Amelia and Nerissa Ravencroft: the 2023 Sports Festival white team.
- `bible/characters/Nakiri-Ayame.md › Background Timeline`: | Lore | An oni from the Underworld Academy, its student council president; she pranks people with will-o'-the-wisps | [Official AY1] |
- `bible/characters/Nakiri-Ayame.md › Background Timeline`: | 2023 | "Kawayo"; a guest artist at the Pretty Cure virtual music event (12-09); the hololive Sports Festival white team wins (with Kiara, Mumei, Ame, Nerissa, AZKi) | [Observed AY2; AY3; AY4 tHP7bd8Jtm0] |
- `bible/characters/Nakiri-Ayame.md › Background Timeline`: | 2025-01-13 | On Okayu's team at the New Year Game Festival (with Suisei, Ina, IRyS, Cecilia) | [AY5 THMIBrxnp-E] |
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | Ninomae Ina'nis, IRyS, Cecilia Immergreen | — | Okayu's 2025 team; Ina and FUWAMOCO on 7th fes STAGE 1 | [AY5] [Official AY6] |
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | Nanashi Mumei, Watson Amelia, Nerissa Ravencroft | — | The 2023 Sports Festival white team | [AY4] |
- `bible/characters/Nakiri-Ayame.md › Story Engine`: 3. An FPS night with Ina and IRyS where Ayame calls out positions in Japanese faster than anyone can follow.

### from Nekomata Okayu
- `bible/characters/Nekomata-Okayu.md › [SW] Background`: Archived stream metadata documents her as Kiara's 18th HOLOTALK guest (2021), a guest at Mumei's 3D live (2024), a pop-up Mario Party with Calli, Anya and Ao (2024) and her 2025 New Year Game Festival team with Ina, IRyS and Cecilia among its members.
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Nanashi Mumei (graduated): a guest at Mumei's 3D live (2024).
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: IRyS and Cecilia Immergreen: members of her 2025 New Year Game Festival team.
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Hakos Baelz: kart events.
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2023-12-12 | Team Mario Kart with Hakos Baelz and FUWAMOCO among others | [OK5 Janl2FCKmsg] |
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2024 | Guest at Nanashi Mumei's 3D live "Outside the Box"; first GAMERS fes (Yoyogi) | [Mumei file] [Observed OK3] |
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2025-01-13 | Leads a team at the hololive New Year Game Festival (with Suisei, Ayame, Ina, IRyS, Cecilia) | [OK4 THMIBrxnp-E] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Nanashi Mumei (graduated) | — | Guest at Mumei's "Outside the Box" (2024) | [Mumei file] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | IRyS, Cecilia Immergreen | — | Her 2025 New Year Game Festival team IRyS: [Secondary, performance unchecked: a setlist records Okayu singing "JANE DOE" with IRyS at IRyS's 2026 birthday live, RACING TOWARDS HOPE (2026-03-21).] | [OK4] [Secondary NEW-R5-013] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Hakos Baelz | — | Team kart events (2023, 2024) | [OK4] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Background`: (2025) with Calli and IRyS as guests, sang the duet "OVER//RIDE" with Calli (2025), and released "OYOME♡HOLIC" and "Blue World"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, and they held a 2025 "BIRB GIRLS"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: IRyS: fellow singer who guested at that concert.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025); with Kiara they sang "Beyond the way" at the 2024 English concert.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Ceres Fauna (graduated 2025): "Fauna-senpai!!!" on her first day on X; with Shiori they sang "Lonely in Gorgeous" at the same concert.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii at Serendipity.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Ninomae Ina'nis: on her Tomodachi Life island with IRyS.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Nakiri Ayame, Nanashi Mumei and Watson Amelia: the 2023 Sports Festival white team.
- `bible/characters/Nerissa-Ravencroft.md › Voice Profile`: - Measured (N20; a 2026 solo chat): median pitch about 214 Hz (p10–p90 172–297 Hz), a mid-range speaking voice like IRyS's (214–226 Hz), lower than Kiara or Gura; about 159 words per minute of speech. Group-stream windows read higher (284–289 Hz) because several voices share them. Sample results only.
- `bible/characters/Nerissa-Ravencroft.md › Background Timeline`: | 2025-05-24 | 3D concert "Requiem for Love – A JukeBox Musical" (guests incl. Calli, IRyS) | [Observed N3 titles] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Takanashi Kiara | Senior and her oshi ("KiaRissa") | Self-described KFP member; in lore, a former KFP employee | [Observed N2] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Mori Calliope | Senior | Nerissa was Calli's first Instagram follower; BG3 party "Killing, Two Birds, with One Stone" with Kiara and Bijou (2023); duet "OVER//RIDE" (2025); Calli guested at Nerissa's 3D concert; building Calli's Mii: "Calli's also got beautiful, long, straight hair." Credited singers together (with IRyS, Nene and Ollie) on "LIVE IT LOUD!" (2025-06-25). A Bananagrams handcam collaboration (2026-09-18; individual jokes unchecked). | [Observed N2; N3 titles; ASR N20, agrees] [Official, music/592] [Archive metadata NEW-R3-013] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | IRyS | Senior and fellow singer | Guest at Nerissa's 2025 3D concert ("Missing Promise"); Monster Hunter Wilds (2025); Nerissa made Miis of Ina and IRyS in Tomodachi Life (2026) | [Observed N3 titles] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Nakiri Ayame | JP senior | The 2023 Sports Festival white team, with Mumei and Ame | [Ayame file AY4] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Raora Panthera | Justice kouhai | Co-presenters (with IRyS) of the official Serendipity merchandise infomercial (May 2026). | [Archive metadata, ckworks ew00E7t4Dow] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Octo'clock
- `bible/characters/Ninomae-Inanis.md › [SW] Background`: She released her first EP, re:VISION, and held the duo concert Drawn to Dawn with Takanashi Kiara in 2026, sang at Myth's 6th-anniversary 3D live with Calli and Kiara, which premiered the Myth song "THIS IS MYTH," and she partners with Ouro Kronii.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Koseki Bijou: "wooden shovel" buddy ("TakoRocky") whose collab outfit Ina designed; with IRyS they starred at Dodger Stadium's hololive night (2025).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put both on her Tomodachi Life island.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Shiori Novella: a "Rate Your Fears" nightmare talk (2024); "MONSTER" with Kronii and Gigi on stage (2025).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Hakos Baelz: a K/DA "POP/STARS" cover (2023), a stream art lesson (2024) and Ina's AmiAmi special (2025).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Shirogane Noel, Kikirara Vivi and Elizabeth Rose Bloodflame: Mumei's Gartic Phone (2025).
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **Code-switching:** English-dominant, with sparse Japanese reaction words: "yabe," "kusa," "seiso," "hazukashii," "warau na," "kouhai." She reads and sometimes answers Japanese chat, and she is improving her Japanese. She shares Korean with Kronii. [Observed I2 §Quotes and §Likes and dislikes; Kronii file K8 §Miscellaneous, secondary] "Marine-senpai" for a senior she admires. [Observed—published interview I18]
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **How she addresses people:** "you guys," "everyone," "chat," and fans as "Takodachi" (the official fan name is the Tentacult). Members by first or short name ("Calli," "Kiara," "Ame," "Gura," "Kronii," "Bae," "Biboo," "CC"); a full name signals a mock-serious scold. New members are "kouhais." She gives her own name surname-first. [Official I1] [Observed I3 captions; I2 §Mascot and fans]
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - Measured (I29, 2026 chat): median pitch 223–232 Hz, in the middle of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz), so "mid" rather than "low"; about 81–95 words per minute of speech in that one 2026 chat stream (Kronii 120–127, Calli 161–186 in their chat windows). A 2021 game stream measures 210–214 Hz and 68–116 words per minute (its opening chat 116). Sample results only; they do not establish a general ranking among genmates.
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026-06-04 | Serendipity interview and partnership with Kronii | [Official I7] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Ouro Kronii | Serendipity partner (interview 2026-06-04; unit name "Octo'Clock" in a 2026-06-24 short, I30) | A pun duo; they share Korean; Ina: "I get to... keep Kronii... all to myself... hehe" | [Official I7] [Observed Kronii file K8 §Miscellaneous] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Hakos Baelz | Promise kouhai | Archived metadata: the K/DA "POP/STARS" cover with Moona and Ayunda Risu (2023); a BAE-CADEMY art lesson with "Ina-sensei" (2024); Ina's AmiAmi special featuring Bae (2025-05-29); World Tour '24 together | [Bae file HB3, HB5, HB8, HB20] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Yukihana Lamy, Shishiro Botan, Kikirara Vivi, Shirogane Noel | JP members | Lamy: the Minecraft "Usaken Summer Festival" (2021-06-27), an EN-server "date" (2021-10-20) and a guest at "Pleides" (2024-12-28); Botan: a guest at "EVERMORE" (2025-05-21); Vivi: R.E.P.O. (2025-06-02); Noel and Vivi: Mumei's Gartic Phone (2025-04-14) | [S1 a7CvRf4vFYc, Isp3UhgOAB4, 3n9igJnSXtQ, I-J11Da5ONY, grBU9Dl09Ds, OMDzBQohAf8] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Elizabeth Rose Bloodflame | Justice kouhai | Co-players in Mumei's Gartic Phone EN + ID + JP, Day 2 (2025-04-14). | [Archive metadata TIE-014] |
- `bible/characters/Ninomae-Inanis.md › Story Engine`: 4. Kronii refuses to react to a pun, and the next conversation becomes a contest. (GPT)

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Ouro Kronii ("Pizza Time"): Portal 2 and Backrooms Cleanup Crew; in ENReco Raora called Kronii's character "Tam Tender."
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Hakos Baelz and IRyS: Super Mario Party on Bae's 24-hour stream (2024).
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Gawr Gura (graduated): R.E.P.O. with Kiara and Kronii (2025).
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Nanashi Mumei (graduated): a joint drawing stream (2025).
- `bible/characters/Raora-Panthera.md › Voice Profile`: - Chattini bits: She sorts a chatter into a type of Chattini, then: "I love those kind." "No, Chattini, you cannot get any of my plushies." "I swear I live in the Justice headquarters. I promise." [ASR RP20, 0:33:19, 0:36:04, 0:37:54; both models on the quoted spans]
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Ouro Kronii | Promise senior ("Pizza Time") | Portal 2 (2024-11-26, "w/ KRONII!! #PizzaTime"), Backrooms Cleanup Crew (2026); in ENReco she called Kronii's character "Tam Tender" (secondary transcription) | [Observed RP2, RP3; Kronii file] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Nerissa Ravencroft, Moona Hoshinova | Seniors ("V3LVET," secondary) | Clubhouse Games with Nerissa (2024-12-09); Raft with both (2025-02-06); Monster Hunter Wilds as V3LVET (Nerissa's title, 2025-03-25) Raora co-presented the official Serendipity merchandise infomercial with Nerissa and IRyS (May 2026). | [Observed RP2, RP3; Nerissa archive] [Archive metadata NEW-R4-016] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Hakos Baelz, IRyS | Promise seniors | Super Mario Party Jamboree on Bae's #BaeTV24 marathon (November 2024); ENReco guildmates in "Amber Coin": Raora, Bae, Kiara and Mumei (secondary) With IRyS (and Nerissa) she co-presented the official Serendipity merchandise infomercial (May 2026). | [Bae file HB3, HB5, HB8, HB20] [Archive metadata NEW-R4-016] |

### from Sakamata Chloe
- `bible/characters/Sakamata-Chloe.md › [SW] Background`: With the English cast, archived channel metadata documents an EN-server Minecraft tour with Bae, Mumei and Lui (2022), Calli's English lesson #04 (2022) and HOLOYOI #01 (2023), Bae's "BAE-GEMITE DOMINATION" and the cover "Crazy Scary Holy Fantasy" with her (2023), and "WILDCARD" with Kiara in her final week (2025).
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Hakos Baelz: the EN Minecraft tour (2022), BAE-GEMITE DOMINATION and "Crazy Scary Holy Fantasy"
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Nanashi Mumei (graduated): the EN Minecraft tour (2022).
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: IRyS: Overwatch 2 and Among Us (2023).
- `bible/characters/Sakamata-Chloe.md › Background Timeline`: | 2022 | First original "Jinsei Reset Button Pochii w" (02-26); EN Minecraft tour with Bae, Mumei and Lui (02-12); Calli's English lesson #04 with Lui (04-16); 3D debut (06-13) | [Observed CH2] [CH5] |
- `bible/characters/Sakamata-Chloe.md › Background Timeline`: | 2023 | 1 million subscribers (02-18, secondary); HOLOYOI #01 with Calli and Lui (03-23); "BAE-GEMITE DOMINATION" (04-29); a cover with Bae (10-30); the original Hoshimatic Project lineup (11-, secondary roster reference) | [Observed CH2] [CH5 UuL_nORzfNM, z4-5Hq5AKG4, 9EAIDwXj4Jk] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Shishiro Botan | — | An Overwatch 2 team with IRyS, Lui and Towa (2023) | [CH5] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Hakos Baelz | — | EN Minecraft tour (2022); BAE-GEMITE DOMINATION, a Suika Game challenge and the cover "Crazy Scary Holy Fantasy" (2023) | [CH5] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Nanashi Mumei (graduated) | — | The EN Minecraft tour (2022) | [CH5] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | IRyS | — | Overwatch 2 team (2023); Among Us (2023) | [CH5] |

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Ouro Kronii: they hosted "Rating Your Clocks" together (2025) and sang "MONSTER" with Ina and Gigi at the 2025 concert.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: IRyS: Monster Hunter Wilds and PEAK (2025).
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Ceres Fauna (graduated 2025): with Nerissa, "Lonely in Gorgeous" at the 2024 English concert.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): B-movie watchalongs.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Raora Panthera: a 2024 outfit-design collab and Blood Typers with Kronii and Bijou (2025).
- `bible/characters/Shiori-Novella.md › Behavioral Traits`: 4. She runs odd "educational" and review streams (a nurse roleplay, "Rating Your Clocks" with Kronii, "Gyatt Review" with Bijou, horror game award shows, B-movie watchalongs). [Observed SN3 titles]
- `bible/characters/Shiori-Novella.md › Background Timeline`: | 2024-08-25 | -Breaking Dimensions-: "Lonely in Gorgeous" with Fauna and Nerissa | [Official, Concerts card S8] |
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Ouro Kronii | Senior | They hosted "Whip It Out! Rating Your Clocks with @OuroKronii" together (2025-03-27; viewers' submissions); Blood Typers (2025) | [Observed SN3; Kronii archive] |
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Nanashi Mumei | Senior (graduated 2025) | B-movie watchalongs (Neil Breen, 2025-02-26; Kung Pow, 2025-04-11), Left 4 Dead 2 (2024) | [Observed SN3] |
- `bible/characters/Shiori-Novella.md › Relationship Map`: | IRyS | Senior | Monster Hunter Wilds (2025), PEAK (2025) | [Observed IRyS archive] |

### from Shirogane Noel
- `bible/characters/Shirogane-Noel.md › [SW] Background`: Archived metadata records her with the English cast as Kiara's 22nd HOLOTALK guest (2022), a guest with Flare on Calli's HOLOYOI #02 (2023), a participant with FUWAMOCO and Bae in a team Mario Kart event (2023) and in Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (2025); FUWAMOCO danced to "TREVIAN KNIGHT."
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: FUWAMOCO and Hakos Baelz: a team Mario Kart event (2023); FUWAMOCO danced to "TREVIAN KNIGHT"
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone EN + ID + JP (2025).
- `bible/characters/Shirogane-Noel.md › Background Timeline`: | 2023 | Calli's HOLOYOI #02 with Flare (04-20); first solo album "NOESANPO" (official digital release 11-25; birthday merchandise orders opened 11-24); a "Yuru Holo" team Mario Kart event with FUWAMOCO and Bae among the participants (12-12) | [NO5] [Official music 359] |
- `bible/characters/Shirogane-Noel.md › Background Timeline`: | 2025 | #ノエこよ Power Pros exhibition with Koyori (01-10); Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (04-14); 3rd-gen R.E.P.O. with Marine, Pekora and Flare (07-05); Elden Ring Nightreign with Flare and Pekora; an Audio-Technica collab with Ayame (07-11); "TREVIAN KNIGHT" (official digital release 08-16), which FUWAMOCO danced to (09-30) | [NO4] [NO5] [Official music 622] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | FUWAMOCO, Hakos Baelz | — | Participants in the "Yuru Holo" team Mario Kart event (2023; not necessarily one team); FUWAMOCO danced to "TREVIAN KNIGHT" (2025-09-30) | [NO5 Evg-T2BUIDM, 8RjOCCH2sac] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii, Elizabeth Rose Bloodflame | — | Gartic Phone EN + ID + JP (2025) | [NO5] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Ceres Fauna (graduated) | EN kouhai | Secondary accounts (Fauna's wiki trivia) say Fauna admired her and wanted to collab; not verified in review and no collab recorded, so it stays out of the exported fields | [Fauna file F2, secondary] |

### from Shishiro Botan
- `bible/characters/Shishiro-Botan.md › [SW] Background`: Archived metadata and secondary concert reports record her with the English cast in Left 4 Dead 2 (2022) and an Overwatch 2 team (2023) with IRyS, on Calli's HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and as a guest at Ina's birthday 3D live "EVERMORE"
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: IRyS: Left 4 Dead 2 with Lui and Korone (2022) and an Overwatch 2 team with Lui, Sakamata Chloe and Tokoyami Towa (2023).
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: Hakos Baelz: BAE-GEMITE DOMINATION #2 with Subaru (2023).
- `bible/characters/Shishiro-Botan.md › Voice Profile`: - **Language:** streams in Japanese; archived metadata records her on Calli's HOLOYOI #03 and Bae's BAE-GEMITE DOMINATION #2 (2023), both with Oozora Subaru. [BO5]
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2022-04-24 | Left 4 Dead 2 with IRyS, Takane Lui and Inugami Korone | [BO5 K1wStJxm4F0] |
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2023 | BAE-GEMITE DOMINATION #2 with Bae and Subaru (04-08); HOLOYOI #03 with Calli and Subaru (05-18); an Overwatch 2 team with IRyS, Lui, Chloe and Towa (08) | [BO5] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | IRyS | — | Left 4 Dead 2 with Lui and Korone (2022); the Overwatch 2 team with Lui, Chloe and Towa (2023) | [BO5 K1wStJxm4F0, roWKpgZsjR4] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Hakos Baelz | — | BAE-GEMITE DOMINATION #2 with Subaru (2023) | [BO5] |

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); they held a 2025 "BIRB GIRLS"
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: IRyS: friend since 2021; Kiara gave her a German crash course.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Ceres Fauna (graduated 2025): HOLOTALK's 32nd guest (December 2024).
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Hakos Baelz: Keep Talking and Nobody Explodes (2021).
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Ouro Kronii | Promise member ("Sundial", fan term) | Kiara announced she was a fan before Kronii debuted; a language exchange is reported by a clip title but remains unverified | [Observed T2 §Relationships; Kronii file K17] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Nanashi Mumei (graduated) | Council member | Kiara coached her "Kikkeriki" | [Observed T5-eivcnjk6yeE clip title] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Hakos Baelz | Promise kouhai | Keep Talking and Nobody Explodes (2021-09-24), which fan references call Bae's first official collab outside Council; World Tour '24 performers together; ENReco guildmates ("Amber Coin," secondary) | [Bae file HB3, HB5, HB8, HB20] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Secret Society holoX | JP kouhai | HOLOTORI with Lui and Mumei; La+: "FAKE HEART" (2025-04-08), the Mythmash single "Glow in the Dark" (premiere 2025-07-27; official digital release 2025-07-28) and an off-collab (2023-06-30); Chloe: an origami off-collab (2023-11-22) and the "WILDCARD" cover (2025-01-25); Iroha: a credited guest at her 4th-anniversary live (2024) and birthday live (2025), and #TASTYchallenge shorts with Nene (2025-07-11, 07-16); Koyori: a "MIRAGE" dance short (2024-12-27) | [S1 v5RKZXNuVyw, eEGbAKvSf1Q, 0LoG81pLS8c, f-UbyQUUykE, 0ldag8qdg6c, AQNPRJMMYY0, xXwi19krZ68] |

### from Takane Lui
- `bible/characters/Takane-Lui.md › [SW] Background`: She debuted on 2021-11-27 as the second member of Secret Society holoX, hololive's sixth Japanese generation, and belongs to the bird unit HOLOTORI, whose documented 2023 lineup was Lui, Takanashi Kiara, Oozora Subaru, Pavolia Reine and Nanashi Mumei.
- `bible/characters/Takane-Lui.md › [SW] Background`: With the English cast, archived metadata records English practice with Mori Calliope (2021), Calli's lesson #04 with Chloe (2022), Calli's "HOLOYOI" episode 1 with Chloe (2023), a Wario off-collab with Kiara (2023), "TWIN DAY WITH LUI" with FUWAMOCO (2023), Hakos Baelz's "BAE-GEMITE DOMINATION" episode 5 with Chloe (2023) and "Q&A With Bird Sisters" with Mumei (2025).
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Nanashi Mumei (graduated): HOLOTORI; "Q&A With Bird Sisters"
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Hakos Baelz: "BAE-GEMITE DOMINATION"
- `bible/characters/Takane-Lui.md › [SW] Relationships`: IRyS and Ouro Kronii: Minecraft with Kaela (2022).
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Shishiro Botan: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (2023, archived title); Left 4 Dead 2 with IRyS and Korone (2022); Blue Journey.
- `bible/characters/Takane-Lui.md › Behavioral Traits`: 2. Dad jokes, like Ina and Kronii. [Observed LU2 §Personality, secondary]
- `bible/characters/Takane-Lui.md › Background Timeline`: | 2022 | Calli's English lesson #04 with Chloe; an EN-server Minecraft tour with Mumei, Bae and Chloe; Minecraft with IRyS, Kronii and Kaela | [LU5] |
- `bible/characters/Takane-Lui.md › Background Timeline`: | 2023 | HOLOYOI ep. 1 with Chloe (Calli's show, 03-23); a Wario off-collab with Kiara (01-15); BAE-GEMITE #5 with Bae and Chloe (04-29); "TWIN DAY WITH LUI" with FUWAMOCO (11-25); Blue Journey (official roster) | [LU5 UuL_nORzfNM, cVJefDjefUs, z4-5Hq5AKG4, MbqO5OPuT80] [Blue Journey roster] |
- `bible/characters/Takane-Lui.md › Background Timeline`: | 2025 | EP "Lieblings"; Code Geass ambassador (June, secondary); "Q&A With Bird Sisters" with Mumei (04-19); Harry Potter watch-alongs with Okayu; "FEAST" dance short with Bae (07-11) | [Observed LU2] [LU5] [LU4 Lj0MZFpHitQ, 5TUiccnytQA] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Sakamata Chloe (affiliate) | holoX intern | Lui reined her in; shows with Calli and Bae together (2022–2023) | [LU2] [LU5] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Nanashi Mumei (graduated) | HOLOTORI; "Bird Sisters" | "Q&A With Bird Sisters" (2025); the EN Minecraft tour (2022) | [LU5] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Hakos Baelz | — | BAE-GEMITE #5 (2023); a "FEAST" dance short on Lui's channel (2025-07-11); an MMD "Soar" (2026) | [LU5] [LU4 5TUiccnytQA] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | IRyS, Ouro Kronii | — | Minecraft elytra hunting with Kaela (2022); IRyS danced to "Soar" (2026) | [LU5] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Shishiro Botan | "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame | A Minecraft collab under that name (2023-04-18, archived title on Botan's channel); Left 4 Dead 2 with IRyS and Korone (2022); the 2023 Overwatch 2 team; Blue Journey (official roster) | [LU2] [Botan file 4-NEM2HrUVA, K1wStJxm4F0] [Blue Journey roster] |
- `bible/characters/Takane-Lui.md › Story Engine`: 1. A historical HOLOTORI scene with Kiara and Mumei; Lui keeps the agenda, then knocks over the water.

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Background`: She was a guest at Kronii's 3D birthday live in March 2026.
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live.
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week.
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Cecilia Immergreen and Gigi: Borderlands 2 with Mumei (2024).
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Hakos Baelz: bathroom reviews and a Holoween escape-room behind-the-scenes (2022), and an Apex off-collab (2023).
- `bible/characters/Watson-Amelia.md › Voice Profile`: - **How she addresses people:** "you guys" by default; "chat" occasionally; "Teamates" (one m, official) on big occasions; members "Investigators." Members by name ("Gura," "Calli," "Ina," "Kiara," "Kronii"); Bubba, her dog mascot. She gives her name in English order, "Amelia Watson." [Official A1] [Observed A3 captions; A2 §Mascots and fans]
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2026-03 | Guest spot at Kronii's 3D birthday live | [Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711] |
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Ouro Kronii | Promise member ("Time Duo") | Time traveler vs. Warden of Time; Ame guested at Kronii's 2026 3D birthday live | [Observed A2 §Relationships; Kronii file K33] |
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Hakos Baelz | Council kouhai | Archived metadata: "BATHROOM REVIEWS" ("#BaethingAme," 2022-05-07), a VRChat Holoween escape-room behind-the-scenes (2022), an Apex off-collab ("2 players. 1 champion.," 2023) | [Bae file HB3, HB5, HB8, HB20] |
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Nakiri Ayame | JP senior | The 2023 Sports Festival white team, with Mumei and Nerissa | [Ayame file AY4] |

### from Yukihana Lamy
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | Hakos Baelz | EN (Promise) | Co-credited singers on the hololive Dreams theme "PARADISE!" (MV 2026-09-28; seven singers); a shared recording project. | [Secondary, dengekionline 202609/89494] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › [SW] Description`: With seniors: Mori Calliope starred in Bijou's Undertale mod and did a 24-hour charity stream with her, shares "FUWAMOCALLI" with the twins (a collaboration name they say they particularly like), and was Shiori's 2026 concert partner; Kiara hosted all five on HOLOTALK, encouraged Bijou through hard choreography, and partnered her in 2026 ("Rocku Wawa"); IRyS is Bijou's horror co-op partner, and Bijou, Ina and IRyS starred at hololive night at Dodger Stadium (2025); Shiori and Kronii hosted "Rating Your Clocks" together in March 2025.
- `bible/world/Advent-Pairs.md › With Myth`: - **Ninomae Ina'nis:** "TakoRocky" with Bijou (Monster Hunter; Ina designed their 2025 Monster Hunter Wilds outfits); "Rate Your Fears" with Shiori (2024); "SHALLYS" with FUWAMOCO and Cecilia at the 2025 concert; with Bijou and IRyS, starred at hololive night at Dodger Stadium (2025-07-05). [Observed S1; X post via wiki] [Official S5, S8]
- `bible/world/Advent-Pairs.md › With Promise`: - **IRyS:** Bijou's horror co-op partner (Dead Space 3, Resident Evil 6, 2026); "Please carry me Senpai!!" in Overwatch (2023); hololive night at Dodger Stadium with Bijou and Ina (2025-07-05); Monster Hunter Wilds and PEAK with Shiori (2025). [Observed S1] [Official S8]
- `bible/world/Advent-Pairs.md › With Promise`: - **Ouro Kronii:** "WatchDog" with FUWAMOCO; Shiori and Kronii hosted "Rating Your Clocks" together (2025-03-27, AjwIazuu8gg; the description credits help with collecting submissions); "MONSTER" with Ina, Shiori and Gigi at the 2025 concert. [Observed S1] [Official S5]
- `bible/world/Advent-Pairs.md › With Promise`: - **Hakos Baelz:** "BaeBi" with Bijou (#BAEBISleepOver, 2024-08-11). [Observed S1]
- `bible/world/Advent-Pairs.md › With Promise`: - **Ceres Fauna (graduated 2025):** "coach" in Bijou's Hitman runs; "Sweaty TryHard Gamers" (Fauna, Bae, Bijou, Kaela); FUWAMOCO helped on her World Tree (2024-12-31); "Lonely in Gorgeous" with Shiori and Nerissa (2024). [Observed S1] [Official, Concerts card]
- `bible/world/Advent-Pairs.md › With Promise`: - **Nanashi Mumei (graduated 2025):** "Stone Age" with Bijou; "Fuwamoomco" (Overwatch, 2025); B-movie watchalongs with Shiori (2025). [Observed S1]
- `bible/world/Advent-Pairs.md › History`: | 2025-07-05 | hololive night at Dodger Stadium: Bijou with Ina and IRyS | [Official S8] |
- `bible/world/Advent-Pairs.md › Hard Facts`: - Shiori and Kronii hosted "Rating Your Clocks" together (March 2025). GAGA is a quartet; GreyScaleX is an official duo unit (Shiori, Zeta). "Fuwawa, Calli and Gigi" (2026) is a Fuwawa collab, not a FUWAMOCO one.

### from AmeSame
- `bible/world/AmeSame.md › How It Works`: - **The goodbye (2024):** on 2024-09-29, the day before Ame concluded her regular activities, Gura's channel streamed "【💛💙】Looking at our old DMs" with Ame; the next day they played Deep Rock Galactic with Kiara and Kronii. [Observed S1]

### from Concerts and Live Events
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: Los Angeles, July 3–4, built on units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia), with guests Ookami Mio, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame singing alongside EN members); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet.
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (March 2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical"
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); hololive night at Dodger Stadium with Ina, IRyS and Bijou (2025-07-05); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!"
- `bible/world/Concerts-and-Live-Events.md › [SW] Rules`: IRyS's solo concert has not happened yet at the 2026-09-30 baseline.
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive fes. + hololive SUPER EXPO** (spring, in Japan; the combined fes./EXPO tradition dates to 2022, while fes. itself is older): the agency-wide concert and convention. 3rd fes "Link Your Wish" (2022-03, Makuhari; Calli and Kiara performed on day 2, per their X posts), 4th fes "Our Bright Parade" (2023), 5th "Capture the Moment" (2024), 6th "Color Rise Harmony" (2025-03-08/09; Nerissa on day 1), 7th "Ridin' on Dreams" (2026-03-06/08). EN units share Expo booths and key visuals (Myth with Promise, Advent with Justice). [Observed S1 §2023–§2026; S2]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous"; Promise's unit song "Our Promise"; "BLUE CLAPPER" by the CHADCast trio (Calli, IRyS, Bae) with Bijou; Bae's solo "GEKIRIN"; "High Tide" by IRyS, Bae, Moona Hoshinova and Hoshimachi Suisei [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; "R x R x R" by Calli and Bae; "Countach" by Bae, Gigi and guest Kureiji Ollie; Bae's solo "La Roja (Arrange ver.)"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before and separate from "-Breaking Dimensions-"), Jakarta (11-09), Singapore (11-30, with a pre-concert panel of Kaela Kovalskia and Ouro Kronii), Atlanta (12-15, a panel of Nerissa and Elizabeth Rose Bloodflame), Kuala Lumpur (12-21, Nerissa and Elizabeth again) and Taipei (2025-01-18, the finale) [Official S7]; and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **holoMeet** (since 2022): overseas fan events with yearly ambassadors (Gura 2022, IRyS 2023, Bae 2024, Bijou 2025, Gigi 2026). [Observed S1]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive night at Dodger Stadium (2025-07-05, Los Angeles):** the second hololive–Dodgers collaboration, starring Ina, IRyS and Bijou, with a stadium sing-along during the game. [Official, https://hololive.hololivepro.com/en/news/20250731-01-353/]
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ninomae Ina'nis | 3D live "Pleides" (2024-12-28); "Drawn to Dawn" with Kiara; World Tour '24 performer; Serendipity with Kronii; "Seasons From Within" | Ina file I20, I7; S3 title |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ouro Kronii | World Tour '24 Singapore pre-concert panel with Kaela Kovalskia; World Tour '25 Sydney guest; 3D birthday live "The Goddess Descends" with a new outfit (2026-03-13/14, Ame as guest); Serendipity with Ina | Kronii file K33, K4; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | IRyS | Promise musical "The Broken Promise" (2024-12-14); 3D lives "The Devil Wears Hope" (2024-11-17), "HOPE UPON A STAR" (2025-03-16), "Racing Towards Hope" (2026-03, race-queen outfit); World Tour '25 lead; Serendipity with Hakos Baelz; first solo concert "HOPE \|\|: Beyond the Stars," Tokyo, 2026-10-06 | IRyS file R2, R3; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Nerissa Ravencroft | 6th fes day 1 (2025-03-08); 3D concert "Requiem for Love – A JukeBox Musical" (2025-05-24, with Calli and IRyS as guests); Advent's "On the Run!" (2025-08-29); World Tour '24 panels with Elizabeth (Atlanta, Kuala Lumpur); World Tour '25 lead; Serendipity with Elizabeth | Nerissa file N2, N3; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Watson Amelia | As an affiliate: guest at Kronii's 2026 birthday live | Kronii file K33 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Hakos Baelz | -Breaking Dimensions- (2024): "Our Promise," "BLUE CLAPPER" with Calli, IRyS and Bijou, solo "GEKIRIN," "High Tide"; -All for One- (2025): "R x R x R" with Calli, "Countach" with Gigi and Ollie, solo "La Roja (Arrange ver.)"; birthday 3D lives "-KAGURA- Dance of the Gods" (2025) and "ReCOLOR" (2026); "Idol" as the final solo number of STAGE 3 at the 2026 fes (secondary setlist; the choreography and breakdance finale are her account); Serendipity: BaeRyS with IRyS, "HELP!!" with Kobo and Elizabeth; first solo concert "REGALIA" scheduled for 2026-12-01 (after the baseline; official announcement) | S8, S9, S11; Bae file HB2, HB7, HB11, HB12, HB20 |
- `bible/world/Concerts-and-Live-Events.md › How It Works in Stories`: - After a concert, a member may stream an aftertalk ("BDay Live Aftertalk") and gush about outfits and guests. [Observed IRyS file R20]
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 2. IRyS counts down to her first solo concert in Tokyo; Kronii and Calli send messages.
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 5. A tour stop in Sydney: Kronii joins Calli, IRyS and Nerissa as a guest.
- `bible/world/Concerts-and-Live-Events.md › Hard Facts`: - IRyS's first solo concert is 2026-10-06, after the 2026-09-30 baseline.

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower").
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Hakos Baelz jokingly calls Ookami Mio and Kureiji Ollie her "moms," sang "HELP!!" with Kobo Kanaeru and Elizabeth, and "Kakumei Dualism" with Natsuiro Matsuri at the 2026 fes.
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Takanashi Kiara:** Usada Pekora is her oshi ("Senpai! Be my guide for the day!", 2020; HOLOTALK's 24th guest, 2022). Pavolia Reine is a recurring collaborator on her channel (30 streams; their pair name "PavoNashi"; a VR "vacation," a Minecraft summer festival; the bird unit "HOLOTORI" with Subaru, Reine, Mumei and Lui); Kobo calls her "Mommy Kiwawa." Other units: "O'riends" (Momosuzu Nene), "KoAra Connect" (Hakui Koyori), "SunMoon"/"Eclipse" (Moona Hoshinova). Outside hololive: "PomuTori" (Pomu Rainpuff), "Mintori" (Mint Fantôme). [Observed S1; S2 Kiara; Kiara file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Watson Amelia** (affiliate): "KoMeHa" (Kobo Kanaeru, Kazama Iroha), "ZetAme" (Vestia Zeta); outside hololive, "SelAMei" (with Mumei and Selen Tatsuki). [Observed S2 Ame]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ouro Kronii:** Kaela Kovalskia is a recurring cross-branch collaborator (21 streams; survival and sim co-ops every few months: Raft 2023–24, Panicore, Luma Island 2024, Old Market Simulator 2025; together at a pre-concert panel in Singapore on World Tour '24 [Official S6]); also "soranii" with Tokino Sora, fan unit K.I.R.A (with IRyS, Reine, Anya), and Raora Panthera of Justice (Portal 2, Split Fiction, No Man's Sky 2026; "Pizza Time"). [Observed S1; S2 Kronii; Kronii file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **IRyS:** Shiranui Flare is a recurring collaborator (23 streams, 11 in 2024): horror and camping co-ops ("ふーたんとキャンプだ！"), Splatoon private matches, an off-collab karaoke (2025-03); units "Star Flower" (Moona, Suisei, AZKi), "IRySora" (Tokino Sora), "ReiRyS" (Reine), "OKFAIR" (Ollie, Kronii, Fauna, Anya, Reine). [Observed S1; S2 IRyS]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ceres Fauna** (graduated): her first official collab outside her generation was with Pavolia Reine (Clubhouse 51, 2021-10-12, per the wiki; Minecraft "WITH REINE," 2022-01-19, ronEFZPwxqc); Kaela Kovalskia was a recurring partner ("Fearless & Fearful vs Ghosts," an ID Minecraft server tour); she admired Shirogane Noel. [Observed S1; Fauna file F2 §2021, §Trivia, secondary]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Nanashi Mumei** (graduated): HOLOTORI with Kiara, Subaru, Reine and Lui ("【MUMEI + LUI】Q&A With Bird Sisters !!!," 2025-04-19, fEO6kSCseE0); drawing collabs with Airani Iofi ("Doodles with IOFI," 2022-04-14, 2dWx7xg48xc; "SWIMSUITS!! with IOFI!," 2023-01-30, XCXF08GMUHY); a duet cover of "とんとんまーえ！" with Inugami Korone (2025-04-23, P6GLC_HnCUU), and Okayu, Korone, Nene and Koyori as guests at her 3D live "Outside the Box" (2024-08-05, gl7CwlEg2ZI); Minecraft "Peace & Love with HAACHAMA" (2025); Tokoyami Towa calls her "Mumi-chan." [Observed S1; Mumei file M2]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Hakos Baelz:** secondary references record her performed maternal-role jokes with Ookami Mio and Kureiji Ollie (her "mom" and "another mom"); with Ollie she sang "Countach" (with Gigi, -All for One- 2025) and played HoloEarth (2024); "HELP!!" with Kobo Kanaeru and Elizabeth at Serendipity (2026); "High Tide" with IRyS, Moona Hoshinova and Hoshimachi Suisei (-Breaking Dimensions- 2024); "Kakumei Dualism" with Natsuiro Matsuri in STAGE 3 of the 2026 fes (a secondary setlist; also her after-talk); Reanimal with Tokoyami Towa (2026); Lethal Company with Kaela Kovalskia (2023–24). Units (secondary): "holorodents" with Usada Pekora and Ayunda Risu; "RoBaelz" with HOLOSTARS' Yukoku Roberu. [Bae file HB2, HB3, HB5, HB20]
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 2. Kronii and Kaela's endless sim co-op hits the in-game stock market.
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 3. IRyS and Flare go camping in a horror game again; IRyS insists she isn't scared.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Kronii and Kaela are recurring public collaborators. IRyS and Flare are recurring public collaborators.

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Myth and Promise:** "FUWAMOCALLI" with Mori Calliope (a twin game show and Smash in 2023, a tea party, an off-collab karaoke in 2024); Fuwawa also joined Mori Calliope and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"; Fuwawa's post, not a twin appearance); "Detective Dogs" with Watson Amelia (Escape Simulator, 2024-09-24); "WatchDog" with Ouro Kronii; "Fuwamoomco" with Nanashi Mumei (Overwatch, 2025-03-01); they helped Ceres Fauna on her last World Tree stream (2024-12-31); Kiara hosted them on HOLOTALK (2023). [Observed S1; S3; Mumei, Calli, Kiara archives]

### from JP Senpai Pairs 2
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Other Names`: Marine and Kiara, Noel and Calliope, Lamy and Ina, Botan and IRyS, Vivi and FUWAMOCO
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: Marine was the first guest of Kiara's talk show HOLOTALK (2020), joined Calli's first English lesson with Ina (2022), played Mario Kart with Calli and Bae (2021) and joined their house-party off-collab (2023), joined off-collabs with FUWAMOCO and Nerissa (2024), and was a guest at Ina's 3D live "Pleides"
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: (2024); Calli, and Bae with Mumei, played "Truth of Beauty Witch," a horror game featuring Marine (2023); Marine, Ina and Gura were in the ocean unit UMISEA.
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: Botan played Left 4 Dead 2 and Overwatch 2 with IRyS, was on HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and guested at Ina's 2025 birthday live.
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: Vivi, a FLOW GLOW member, played R.E.P.O. with FUWAMOCO and Bae and, separately, on Ina's stream, and Gartic Phone with Mumei, Kronii, Ina and Elizabeth (2025).
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Rules`: Gura and Mumei appear only as memories; Ame is an affiliate.
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Mori Calliope:** Calli's HOLO ENGLISH LESSON #01 with Ina and Fubuki (2022-02-19); Mario Kart with Bae and Pavolia Reine (2021-12-25); an off-collab "House Party with Marine & Bae" (2023-08-14); Calli played "Truth of Beauty Witch," the horror game featuring Marine, on her own stream (2023); dance shorts to Marine's songs. [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Hakos Baelz, Nanashi Mumei (graduated):** Bae played the horror game featuring Marine with Mumei (2023-08-23; a game connection, not a collab with Marine); Bae was at the house party with Marine; dance covers. [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Shirogane Noel with the cast`: - **FUWAMOCO, Hakos Baelz:** a "Yuru Holo" team Mario Kart event (2023-12-12); FUWAMOCO danced to Noel's "TREVIAN KNIGHT" (2025). [S1] [Official music 622]
- `bible/world/JP-Senpai-Pairs-2.md › Shirogane Noel with the cast`: - **Nanashi Mumei, Ina, Kronii, Elizabeth (and Kikirara Vivi):** Mumei's Gartic Phone EN + ID + JP collab (2025-04-14). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Shishiro Botan with the cast`: - **IRyS:** Left 4 Dead 2 with Lui and Inugami Korone (2022-04-24); an Overwatch 2 team for Holizontal JAM with Lui, Chloe and Towa (2023-08). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Shishiro Botan with the cast`: - **Mori Calliope, Hakos Baelz:** HOLOYOI #03 and BAE-GEMITE DOMINATION #2, both with Oozora Subaru (2023). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Kikirara Vivi with the cast`: - **FUWAMOCO, Hakos Baelz:** #holoREPO with Roboco, Towa and Hajime (2025-05-25). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Kikirara Vivi with the cast`: - **Mumei, Kronii, Ina, Elizabeth:** Mumei's Gartic Phone EN + ID + JP collab (2025-04-14). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › History`: | 2022 | Calli's English lesson #01; HOLOTALK #22; Left 4 Dead 2 | Marine; Noel; Botan, IRyS |
- `bible/world/JP-Senpai-Pairs-2.md › History`: | 2023 | HOLOYOI #02 and #03; BAE-GEMITE DOMINATION #2; the horror game featuring Marine; Overwatch 2 team; Blue Journey | Noel, Botan, Calli, Bae; Calli, Bae, Mumei; Botan, IRyS |
- `bible/world/JP-Senpai-Pairs-2.md › History`: | 2025 | Gartic Phone EN + ID + JP (04-14); #holoREPO (05-25); R.E.P.O. on Ina's stream (06-02); Ina's "EVERMORE" | Noel, Vivi; Vivi, Bae, FUWAMOCO; Vivi, Ina; Botan |
- `bible/world/JP-Senpai-Pairs-2.md › Conflicts and Story Hooks`: 3. Vivi does stage makeup for Bae before a R.E.P.O. rematch.

### from JP Senpai Pairs
- `bible/world/JP-Senpai-Pairs.md › [SW] Description`: Suisei, AZKi, IRyS and Moona Hoshinova are the official unit Star Flower ("story time," 2022); Suisei sang "High Tide" with IRyS, Moona and Hakos Baelz and "BIBBIDIBA" with Moona, Ina and Gura at the 2024 English concert, and was a face of hololive night at Dodger Stadium with Gura and Pekora (2024).
- `bible/world/JP-Senpai-Pairs.md › [SW] Rules`: Gura and Mumei appear only as memories; Ame is an affiliate.
- `bible/world/JP-Senpai-Pairs.md › Hoshimachi Suisei with the cast`: - **IRyS:** with Moona Hoshinova and AZKi they are **Star Flower**, the unit of "story time" (2022-12-31, the theme of the second hololive Alternative teaser); IRyS covered Suisei's "GHOST" (2021); "High Tide" with IRyS, Moona and Hakos Baelz at -Breaking Dimensions- (2024); the PlateUp! squad of Okayu's team at the 2025 New Year Game Festival (with Pavolia Reine). [Official S3, S6] [S1]
- `bible/world/JP-Senpai-Pairs.md › Hoshimachi Suisei with the cast`: - **Others:** Hakos Baelz ("High Tide," 2024; a 2025 dance short to Suisei's "Moonlight"); Nanashi Mumei (a #bibbidibachallenge short together, 2024-06-18); FUWAMOCO (a 2026 dance short to Suisei and Houshou Marine's "Chatter Chatter"); Nerissa Ravencroft (a "BIBIDEBA" dance short, 2024); Koseki Bijou (a Fortnite stream titled "THE SUISEI CONCERT IN FORTNITE?!", 2026-05-02, after Suisei joined Fortnite as a playable character in March 2026). [S1] [Official S6] [S5 Suisei, secondary]
- `bible/world/JP-Senpai-Pairs.md › AZKi with the cast`: - **IRyS:** Star Flower (above); IRyS covered AZKi's "Inochi" (2021); Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame (2022-03-12); an R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora, Ina and Kronii (2025-07-19). [S1] [Official S3]
- `bible/world/JP-Senpai-Pairs.md › AZKi with the cast`: - **Others:** Takanashi Kiara (HOLOTALK's 13th guest, 2021-07-31); Hakos Baelz (GeoGuessr, "lost simulator," 2023-03-09); Ouro Kronii, Elizabeth and FUWAMOCO (Tokoyami Towa's team at the 2025 New Year Game Festival); Mori Calliope (AZKi danced to Calli's "Orpheus" in a 2025 short); Shiori Novella, Bae and Raora Panthera danced to AZKi's songs in shorts (2025–2026). [S1]
- `bible/world/JP-Senpai-Pairs.md › Nakiri Ayame with the cast`: - **Team events:** the 2023 hololive Sports Festival in Minecraft, white team (Ayame's stream description lists Kiara, Mumei, Ame, Nerissa and AZKi; its title celebrates the win); Okayu's team at the 2025 New Year Game Festival (with Suisei, Ina, IRyS and Cecilia). [S1]
- `bible/world/JP-Senpai-Pairs.md › Nakiri Ayame with the cast`: - **Shared billing:** 7th fes STAGE 1 with Ina and FUWAMOCO (2026-03-06); the official Anime NYC 2026 announcement listed her, Shirakami Fubuki and Ookami Mio for an August 22 convention-exclusive stream, the same day as streams by Kronii and Raora, FUWAMOCO, and Calli, Bijou, Nerissa and Kobo Kanaeru (a booking, not a location). [Official S5, S7]
- `bible/world/JP-Senpai-Pairs.md › Nekomata Okayu with the cast`: - **Others:** Takanashi Kiara (HOLOTALK's 18th guest, the show's first-anniversary episode, 2021-11-27); Nanashi Mumei (a guest at Mumei's 3D live "Outside the Box," 2024); Mori Calliope (a pop-up Mario Party with Anya Melfissa and Hiodoshi Ao, 2024-09-15); Hakos Baelz and FUWAMOCO (team Mario Kart, 2023-12-12); IRyS and Cecilia Immergreen (Okayu's 2025 New Year Game Festival team); Gigi Murin (public translation-based banter during the 2026 New Year Game Festival, secondary clip metadata). [S1] [Mumei file] [Gigi file]
- `bible/world/JP-Senpai-Pairs.md › History`: | 2022-03-12 | HOLO ENGLISH LESSON #03 | Calli with IRyS, Watame, AZKi |
- `bible/world/JP-Senpai-Pairs.md › History`: | 2022-12-31 | "story time" | Star Flower (Suisei, AZKi, Moona, IRyS) |
- `bible/world/JP-Senpai-Pairs.md › History`: | 2023-11 | Sports Festival, white team wins | Ayame and AZKi with Kiara, Mumei, Ame, Nerissa |
- `bible/world/JP-Senpai-Pairs.md › History`: | 2024-08-24/25 | "High Tide" at -Breaking Dimensions- | Suisei with IRyS, Moona, Bae |
- `bible/world/JP-Senpai-Pairs.md › History`: | 2025-01-13 | New Year Game Festival, Okayu's team | Okayu, Suisei, Ayame with Ina, IRyS, Cecilia |
- `bible/world/JP-Senpai-Pairs.md › Hard Facts`: - Official units: Star Flower (Suisei, AZKi, Moona Hoshinova, IRyS; "story time," 2022-12-31).
- `bible/world/JP-Senpai-Pairs.md › Hard Facts`: - Concert pairings: "Wicked" (Suisei with Calli, 2022-07-21); "High Tide" (IRyS, Bae, Moona, Suisei; 2024).
- `bible/world/JP-Senpai-Pairs.md › Hard Facts`: - 7th fes (March 6–8, 2026; STAGE 1 Mar 6, STAGE 3 Mar 7, STAGE 4 Mar 8): STAGE 1 Ayame, Okayu (with Ina, FUWAMOCO); STAGE 3 AZKi (with IRyS, Bae, Shiori); STAGE 4 Suisei (with Calli, Kronii, Bijou, Nerissa).

### from Justice Pairs
- `bible/world/Justice-Pairs.md › [SW] Description`: With seniors: Gigi repeatedly uses Calli's full name and jokes about getting her into League of Legends; within HoloEU, Raora teaches Kiara Italian and Cecilia speaks German with her; Cecilia plays up a rivalry with Ina; Kronii is Raora's "Pizza Time" collaborator and Gigi's Fatal Fury and Hytale partner, and secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai"; Automatowl names Cecilia and Mumei.
- `bible/world/Justice-Pairs.md › With Advent`: - **Shiori:** Elizabeth ("NovelFlame," "BloodQuill"; secondary) and Gigi voice parts in Shiori's non-canon motion comic "Into The Void" (2026; episode 2 also credits Calli); Gigi ("NovelGrem") games with her often (Heave Ho, a Fateful Findings watchalong, Project Zomboid, Phasmophobia; Eden Eternal was Kiara, Shiori and Gigi); the "Fanfic Club" (Gigi, Shiori, Pavolia Reine, Airani Iofifteen) is a separate group from "GAGA" (Gigi, Cecilia, Shiori, Bijou); Raora: a 2024 outfit-design collab (2024-12-05) and Blood Typers with Kronii and Bijou (2025-06-10); Cecilia: "Break It Down" with Vestia Zeta at Serendipity; Gigi: "MONSTER" with Ina and Kronii at -All for One-. [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Advent`: - **FUWAMOCO:** Raora is their Serendipity unit partner in B.F.F (official billing, "Inu Neko. Seishun Massakari"); Gigi and Cecilia guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit ("GigiMoco" and "Cecemoco" are pair labels with Mococo); Cecilia played Chrono Trigger with Mococo, including 2026 off-collabs; Gigi sang "Bright Tonight" (2025) with the twins, IRyS and Kronii, and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity; Fuwawa, Gigi and Calli as "2 Creatures + 1 Reaper" (2026, Fuwawa alone); the twins sang in Elizabeth's 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha. [Official S3 interview03] [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Myth`: - **Ninomae Ina'nis:** Cecilia's Stranger of Paradise partner (2025), with a rivalry bit Cecilia plays up (secondary); "SHALLYS" with Cecilia and FUWAMOCO, "MONSTER" with Gigi, Kronii and Shiori, "Neko Kaburi-Na" with Raora, Shiori and Oozora Subaru (all at -All for One-); Rabbit and Steel with Cecilia, Bijou and Gigi (2024); Blood Typers with Gigi (2025-04-11); Puyo Puyo Tetris 2 with Raora (2025-06-02); the Monster Hunter Wilds sponsored launch with Gigi, Raora and Bijou (2025-03-01). [Observed S1]
- `bible/world/Justice-Pairs.md › With Myth`: - **Gawr Gura (graduated):** Keep Talking and Nobody Explodes and The Forest with Cecilia (2025-02); R.E.P.O. with Raora, Kiara and Kronii (2025-04-13). **Watson Amelia (affiliate):** in ENReco's role-play story, Gigi's Gonathon and Ame's Jyonathan marry (secondary; "ClueChaser"); Borderlands 2 with Cecilia, Gigi and Mumei (2024-08-09). [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Promise`: - **Ouro Kronii:** "Pizza Time" with Raora (Portal 2, 2024-11-26; Backrooms Cleanup Crew, 2026-06-11; in ENReco Raora used "Tam Tender" for Kronii's character, secondary), "TimeChaser" with Gigi (Fatal Fury, 2025-05-03; Hytale, 2026-04-14), "Clockwork Orange" with Gigi and Cecilia; secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai" nickname; "Bright Tonight" and "MONSTER" with Gigi. [Observed S1; S2; Kronii file] [Official S6]
- `bible/world/Justice-Pairs.md › With Promise`: - **Hakos Baelz:** "BratTea" with Cecilia; "Countach" with Gigi and guest Kureiji Ollie at -All for One-. **IRyS:** Elden Ring Nightreign with Cecilia and Bijou (2025-06-05); "Bright Tonight" with Gigi (2025); "START AGAIN" with Elizabeth at -All for One-. [Observed S1; S2] [Official S6]
- `bible/world/Justice-Pairs.md › With Promise`: - **Ceres Fauna (graduated 2025):** Gigi's "FruitPunch" (Silent Hill 2; The Coughing Baby Award Show, 2024-12-28) and League of Legends with Elizabeth, Gigi, Cecilia and Nerissa (2024); Cecilia's "Green Women" (a shoujo-tropes ranking, 2024-09-23). **Nanashi Mumei (graduated 2025):** Cecilia's "Automatowl" (Halo: Reach, 2024; "Ask us anything," 2025-04-12; the nickname "Myumyei" is unverified); Gigi's Echo Point Nova ("A Towl and a Gremlin," 2024-10-15); an art stream with Raora (2025-01-18). [Observed S1; S2]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **ID:** Kaela Kovalskia with Raora ("SMITTEN," "Graondstone," "PizzaTimeSmith" with Kronii; in Raora's lore Kaela lives in her basement); Kureiji Ollie is Elizabeth's "kami-oshi" per public-profile wikis (collabs with HOLOSTARS members in varying lineups, including Code Red games; "High Tide" with Kronii at -All for One-), and Ollie did a chat-and-art collab with Raora (2024-09-06); Moona Hoshinova with Raora ("V3LVET"); Anya Melfissa joined Raora for a public off-collab (2025; archived video w30OQWD6AEw); Vestia Zeta and Haachama in a Mario Party off-collab with Raora (2024-10-08); Ayunda Risu with Elizabeth ("LYRA," "ALiCE&u"); Vestia Zeta sang "Giri Giri" with Elizabeth at her 2025 3D showcase, which Elizabeth arranged and choreographed [ASR, Elizabeth file EB20]; Pavolia Reine and Airani Iofi with Gigi in the "Fanfic Club"; Kobo Kanaeru calls Elizabeth "Lilis" (secondary) and sang "HELP!!" with Elizabeth and Bae at Serendipity; Vestia Zeta also sang "Break It Down" with Cecilia and Shiori and "MAKE IT, BREAK IT" with Gigi and FUWAMOCO at Serendipity. [Observed S1; S2] [Official S6, S7]
- `bible/world/Justice-Pairs.md › History`: | 2026-07-03/04 PDT | Serendipity: units Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora); guests' songs with Justice members: "HELP!!" (Kobo, Bae, Elizabeth), "Break It Down" (Zeta, Shiori, Cecilia), "Cloudy Sheep" (Watame, Calli, Cecilia), "MAKE IT, BREAK IT" (Zeta, FUWAMOCO, Gigi), "What an amazing swing" (Watame, Kiara, Raora) | [Official S3, S7] |
- `bible/world/Justice-Pairs.md › Conflicts and Story Hooks`: 4. Cecilia and Kronii's insult duel ("CLANKER" / "Owo-senpai") needs a referee.

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Other Names`: Kiara and Ame, Ame and Kiara, Kiara and Gura, Gura and Kiara, Calli and Ina, Ina and Calli, Calli and Ame, Ame and Calli, Ina and Ame, Ame and Ina, Ina and Gura, Gura and Ina, Kiara and Kronii, Kronii and Kiara, Gura and Kronii, Kronii and Gura
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: The rest of the web among the five Myth members and Kronii.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Kiara and Kronii: Kiara was a fan before Kronii debuted and calls her "quasoni."
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Gura and Kronii: fan unit SNOTCast; in Gura's last months Kronii was one of her regular partners ("I Play, She Watches (She's Scared)").
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Kiara and Kronii** (2021→2025: 5 / 5 / 11 / 5 / 6): Kiara was a fan of Kronii before Kronii debuted and calls her "quasoni" in her own stream titles ("quasoni pls help me"); Diablo raids, an Age of Empires tournament, a GIRLSTALK ("Turns Out Kronii Is Quite The Girl Too!!!!!!", 2024) and PEAK ("we are climbing mount kronii, right?", 2025). [Observed Kronii file K8; S1 Kiara titles]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Gura and Kronii** (2021→2025: 9 / 11 / 3 / 2 / 5): the fan unit SNOTCast (Shark, Nature, Owl, Time); in 2025, Gura's last months, Kronii became one of her regular partners: Fast Food Simulator ("Legend Is Made Here With @GawrGura"), R.E.P.O., and "Greener Grass Awaits: I Play, She Watches (She's Scared)" (2025-04-26). [Observed S4 §Relationships, secondary; S1 Kronii titles]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2025-04-26/30 | Kronii's and Kiara's last collabs with Gura | Farewells |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Conflicts and Story Hooks`: 4. Kronii plays a horror game while Gura "watches (she's scared)."
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Hard Facts`: - Kiara's EN oshi: Ame. Kiara's names: "Goobidiba" (Gura), "quasoni" (Kronii).

### from TakaMori
- `bible/world/TakaMori.md › How It Works`: - **Recent milestones (archive, S1):** an off-collab "Reunion & Gaming!! #takamori" and a karaoke collab (2022-06); off-collabs in 2023 (a Rubik's cube stream, "TAKAMORI OFF-COLLAB" with Kobo, doing each other's nails on camera with IRyS); their duet "Fire N Ice" (2023-12-14; lyrics by Calli and TeddyLoid); Kiara's off-collab watch party "cheering Calli on!!!" for Calli's GriMoire concert (2025-02-27); a four-part Split Fiction co-op series in April–May 2025, titled by them "takamori split screen nostalgia," "Perfectly In Sync with @TakanashiKiara," "thumbnail teetee manifestation into gameplay teetee" and "Saving the World with @TakanashiKiara"; Myth's 5th anniversary collab (2025-09-13) and the 6th anniversary 3D live "Seasons From Within" (2026-09-19 PDT), where the two sang a duet cover together (setlist, secondary S7) and premiered "THIS IS MYTH" with Ina.

### from VTuber Persona and Lore
- `bible/world/VTuber-Persona-and-Lore.md › [SW] Description`: Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization, an archiver who broke out of a prison for forbidden things, a gem born from human emotion, twin demonic guard dogs, Justice's queen, gremlin, ancient automaton and big-cat artist sent to catch Advent) is a persona and a running joke, not a fact of the story world, and they know it.
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - **What is a persona:** the lore on their official profiles (a reaper's apprentice, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time). In the story it is a character each one plays on stream, the way a performer keeps a stage persona. [Official profiles; Adaptation]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They use it as a joke engine: age jokes (Gura's "9,000-something," Kronii jokingly "60"), immortality and rebirth gags (Kiara), reported time-travel callbacks whose event and segment locators still require verification. [Observed character files; Ame's wiki page §2026, secondary]

### from holoX
- `bible/world/holoX.md › [SW] Description`: With the English cast, archived uploads document Lui in the bird unit HOLOTORI with Kiara and Mumei (and Lui and Mumei's "Q&A With Bird Sisters"); "Glow in the Dark" by La+ and Kiara (2025); Chloe and Kiara's "WILDCARD" cover; Calli's English lessons with La+ and Iroha (#02) and Lui and Chloe (#04); Koyori's "FUWAMOKOYO" morning-show guest spot with FUWAMOCO and a separate Lethal Company session with them and Fubuki; and Iroha's VALORANT collab with Ame and Kobo (secondary name "KoMeHa").
- `bible/world/holoX.md › With the English cast`: - **Takanashi Kiara:** welcomed Lui into the bird unit HOLOTORI on her debut day; HOLOTORI is Kiara, Lui, Mumei, Subaru and Reine; a Wario off-collab with Lui (2023-01-15); La+ and Kiara's Mythmash single "Glow in the Dark" (2025-07-27) and their "FAKE HEART" cover (2025-04-08); a nostalgic-games handcam off-collab with La+ (2023-06-30); "WILDCARD," a cover with Chloe (2025-01-25); a #TASTYchallenge dance with Iroha (2025). [S1] [S3]
- `bible/world/holoX.md › With the English cast`: - **Nanashi Mumei (graduated):** HOLOTORI with Lui; "Q&A With Bird Sisters" (2025-04-19); an EN-server Minecraft tour with Lui, Chloe and Bae (2022). [S1]
- `bible/world/holoX.md › With the English cast`: - **Hakos Baelz:** "BAE-GEMITE DOMINATION" with Lui and Chloe (2023-04-29) and with Koyori (2023-04-22); a cover with Chloe ("Crazy Scary Holy Fantasy," 2023); dances to Lui's songs. [S1]
- `bible/world/holoX.md › With the English cast`: - **IRyS, Ouro Kronii:** Minecraft elytra hunting with Lui and Kaela (2022). [S1]
- `bible/world/holoX.md › With the English cast`: - **Others:** Lui's 2026 song "Soar" was danced by IRyS, Nerissa, Bijou, Gigi, Raora, Calli, Bae and FUWAMOCO (2026 shorts); Cecilia teased La+ as "onee-sama" (2026 short); Nerissa met La+ in holoGTA (2024). [S1]
- `bible/world/holoX.md › History`: | 2023 | HOLOYOI ep. 1 (Lui, Chloe); BAE-GEMITE episodes; Kiara's off-collabs with Lui and La+ | with Calli, Bae, Kiara |
- `bible/world/holoX.md › History`: | 2025-04-19 | "Q&A With Bird Sisters" | Lui, Mumei |

### from hololive -Advent-
- `bible/world/hololive--Advent.md › [SW] Rules`: Myth and Promise are their seniors.
- `bible/world/hololive--Advent.md › How the Group Works`: - **Seniors:** Advent debuted after Myth, Project: HOPE and Council; the latter two were later organized as Promise. Kiara hosted all five on HOLOTALK (2023-08-12) within two weeks of their debut. [Observed S5 Kiara archive title]

### from hololive -Justice-
- `bible/world/hololive--Justice.md › [SW] Description`: (2026); individual 3D showcases on August 1, 2, 8 and 9, 2025 (PDT) and a group 3D stream on August 16; their first in-person concert performance in 3D at the 2025 English concert; at the 2026 Serendipity concert the units Autofister (Gigi and Cecilia), Bloodraven (Elizabeth and Nerissa) and B.F.F (Raora and FUWAMOCO), with Elizabeth also singing alongside Kobo Kanaeru and Hakos Baelz, Cecilia alongside Vestia Zeta and Shiori and alongside Tsunomaki Watame and Calli, Gigi with Zeta and FUWAMOCO, and Raora with Watame and Kiara; and the second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive--Justice.md › [SW] Rules`: Myth, Promise and Advent are their seniors.
- `bible/world/hololive--Justice.md › History`: | 2026-07-03/04 PDT | Serendipity: day 1 "SUPERNOVA SUPER GIRL" (Justice); Autofister (Gigi & Cecilia, "CCGG MADNESS"); "HELP!!" (Kobo Kanaeru with Bae and Elizabeth); "Break It Down" (Vestia Zeta with Shiori and Cecilia); "Cloudy Sheep" (Tsunomaki Watame with Calli and Cecilia). Day 2: the Advent+Justice medley ("Rebellion," "ABOVE BELOW"); Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"); "MAKE IT, BREAK IT" (Zeta, FUWAMOCO and Gigi); "What an amazing swing" (Watame with Kiara and Raora); B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari") | [Official S6, S8] |

### from hololive -Myth-
- `bible/world/hololive--Myth.md › Members and Status`: - Watson Amelia: concluded general activities 2024-09-30; affiliate; guests at genmates' events (Kiara's concerts 2025 and 2026, Kronii's 2026 live, a reported cameo in Calli's 2026 charity stream, with its segment locator unverified). [Observed Ame file A23; Ame's wiki page §2025–§2026, secondary]

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: The recent past behind the present. 2023: Advent debuts (Nerissa, Shiori, Bijou, FUWAMOCO, July); DEV_IS opens with ReGLOSS; IRyS and the Council become -Promise- (October); EN holds its 1st concert. 2024: Justice debuts (June) as the "law enforcers" hunting Advent; the ENigmatic Recollection fantasy story starts (IRyS's guild "Cerulean Cup,"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05 PDT); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: (June); EN's 4th concert "Serendipity" in Los Angeles (July), built on units such as Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS, Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2023-04 | holoMeet 2023 ambassadors include IRyS | IRyS represents EN |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2023-10-08/09 | "CouncilRyS" 3D showcase; **-Promise- formed** (IRyS joins the Council) | Kronii's and IRyS's group |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-04 | holoMeet 2024 ambassadors include Hakos Baelz | — |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 | "ENigmatic Recollection" (ENReco) announced: EN members in the fantasy world Libestal, via a Minecraft series, animation and songs | Guilds: IRyS in "Cerulean Cup," Nerissa and Gura in "Scarlet Wand" |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 EDT | World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 | — |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-01-03 | Ceres Fauna graduates | Promise remembers her |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-04 | World Tour '25 "-Synchronize!-" announced, led by Momosuzu Nene, Kureiji Ollie, **Mori Calliope, IRyS and Nerissa Ravencroft**, with guests per city (Kronii and Bae in Sydney) | Three of the cast on one tour |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-04-27 (04-28 JST) | Nanashi Mumei graduates | Promise becomes three |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-07-05 PDT | hololive night at Dodger Stadium, Los Angeles, the second hololive–Dodgers collaboration: Ina, IRyS and Bijou | a stadium sing-along |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-07-03/04 PDT | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) | The current partnerships |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-10-06 (upcoming) | IRyS's first solo concert "HOPE \|\|: Beyond the Stars" (Tokyo) | IRyS's next big stage |
- `bible/world/hololive-History-2023-2026.md › How It Works in Stories`: - Affiliates (Ame) can appear at events and in projects; graduates (Gura, Fauna, Mumei) appear only as memories, callbacks and songs. [Official S1 2024-11-29 notice, secondary]
- `bible/world/hololive-History-2023-2026.md › Conflicts and Story Hooks`: 3. During a fictional public tour panel, Calli, IRyS and Nerissa compare their stage personas.
- `bible/world/hololive-History-2023-2026.md › Conflicts and Story Hooks`: 4. A Promise anniversary after 2025, the three remembering Fauna and Mumei with jokes.
- `bible/world/hololive-History-2023-2026.md › Conflicts and Story Hooks`: 5. IRyS's nerves before her first solo concert in Tokyo.
- `bible/world/hololive-History-2023-2026.md › Hard Facts`: - Merger 2026-09-07. Ame affiliate since 2024-09-30. Gura graduated 2025-05-01; Fauna 2025-01-03; Mumei 2025-04-27 (04-28 JST).

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2021-07-11 | **IRyS debuts** as the VSinger of Project: HOPE | Hope arrives |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2021-08-23 | **-Council- debuts:** Sana, Fauna, **Kronii**, Mumei, Bae | Kronii's origin |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-07-18/23 | HOLOSTARS English -TEMPUS- (Regis Altare, Magni Dezmond, Axel Syrios, Noir Vesper) announced and debuts | Calli and Kronii's WARS partners Magni and Vesper |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-07-31 | Tsukumo Sana graduates | Council becomes four |
- `bible/world/hololive-History-to-2022.md › How It Works in Stories`: - Before a date, the world is as it was then: no Council before 2021-08, no Advent before 2023-07.
- `bible/world/hololive-History-to-2022.md › Hard Facts`: - Myth debuted 2020-09-12/13 JST; IRyS 2021-07-11; Council 2021-08-23.

### from hololive
- `bible/world/hololive.md › [SW] Description`: (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-.
- `bible/world/hololive.md › [SW] Description`: Watson Amelia concluded her regular activities on 2024-09-30 and remains an affiliate who appears at events; Gawr Gura graduated on 2025-05-01 and is an alumna, as are Promise's Ceres Fauna (2025-01-03) and Nanashi Mumei (2025-04-27).
- `bible/world/hololive.md › How It Works`: - **Member status:** active talents; **affiliates** who concluded their general activities but remain with hololive and appear at individual events (Watson Amelia since 2024-09-30); **graduates** who left (Gawr Gura on 2025-05-01; in Promise, Ceres Fauna 2025-01-03 and Nanashi Mumei 2025-04-27). Graduates are called alumni; stories never give reasons beyond "graduated." [Official COVER notices; Observed S2]
- `bible/world/hololive.md › History`: | 2021-08 | -Council- debuts (Kronii's generation) | Council → Promise |
- `bible/world/hololive.md › History`: | 2023-10-09 | -Promise- formed (IRyS joins the remaining Council) | Kronii's group name |
- `bible/world/hololive.md › History`: | 2026-07-03/04 | hololive English 4th concert "Serendipity" (LA) | Partner pairs (e.g. Kronii and Ina) |
- `bible/world/hololive.md › Hard Facts`: - Amelia: affiliate since 2024-09-30. Gura: graduated 2025-05-01. Fauna: 2025-01-03. Mumei: 2025-04-27.

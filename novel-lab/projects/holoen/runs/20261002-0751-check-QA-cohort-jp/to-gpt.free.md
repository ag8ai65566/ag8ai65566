# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: jp
Packet: projects/holoen/research/qa/packets/jp.md (owned material) and projects/holoen/research/qa/packets/jp-incoming.md (incoming claims); both are inline below
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
| AUDIT-MYTH2 | Cohort audit myth2 (Gura, Ame, Myth, AmeSame, Bone Bros) | applied in full, including re-raised myth3 residuals | 2026-10-04 merge |
| AUDIT-PROMISE | Cohort audit promise (Kronii, IRyS, Fauna, Mumei, Bae and pair cards) | applied; PROMISE-QUOTE-001 adapted to the two-model shared span; one CONSULT-P1-006 row not applied (both models share the longer span) | 2026-10-04 merge |
| AUDIT-BRIDGE-EVENTS | Bridge audit of dates, zones and status | applied; registry rows fixed in tools/qa_packets.py (date parser) and by regeneration | 2026-10-04 merge |

### Registry excerpt (this cohort's cast and world records and its units; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "0b372b1",
 "cast": [
  {
   "name": "AZKi",
   "file": "bible/characters/AZKi.md",
   "other_names": [
    "AZKichi",
    "Azukichi",
    "Azu-chan",
    "AZAZ",
    "AzuAzu",
    "Virtual Diva AZKi"
   ],
   "groups": [
    "hololive",
    "hololive 0th Generation",
    "Star Flower",
    "SorAZ",
    "AS_tar",
    "AzuIro",
    "KanatAZ",
    "RosaMiA"
   ],
   "status": "AZKi is an active member of hololive Generation 0. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2018-11-15",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/AZKi.md › Background (debut: Hard Facts / Background Timeline)"
   }
  },
  {
   "name": "Hoshimachi Suisei",
   "file": "bible/characters/Hoshimachi-Suisei.md",
   "other_names": [
    "Suisei",
    "Sui-chan",
    "Suicopath",
    "Hoshimachi"
   ],
   "groups": [
    "hololive",
    "hololive 0th Generation",
    "Star Flower",
    "miComet",
    "Hoshimatic Project",
    "Shiranui Kensetsu",
    "Startend",
    "AS_tar",
    "MOMAS",
    "Midnight Grand Orchestra"
   ],
   "status": "Suisei is an active member of hololive Generation 0. She has no supernatural abilities; her persona is a virtual idol, not a fantasy creature.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2018-03-22",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Hoshimachi-Suisei.md › Background (debut: Background)"
   }
  },
  {
   "name": "Nakiri Ayame",
   "file": "bible/characters/Nakiri-Ayame.md",
   "other_names": [
    "Ayame",
    "Ojou",
    "Yo-san"
   ],
   "groups": [
    "hololive",
    "hololive 2nd Generation",
    "FAMS",
    "AyaFubuMi",
    "AyaSuba",
    "Manji-gumi",
    "OKFAMS"
   ],
   "status": "Ayame is an active member of hololive's 2nd generation. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2018-09-03",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Nakiri-Ayame.md › Background (debut: Background)"
   }
  },
  {
   "name": "Nekomata Okayu",
   "file": "bible/characters/Nekomata-Okayu.md",
   "other_names": [
    "Okayu",
    "Okayun",
    "Okanyan"
   ],
   "groups": [
    "hololive",
    "hololive GAMERS",
    "OkaKoro",
    "SMOK",
    "OKFAMS",
    "MOMAS",
    "TakoNeko",
    "SubaOka"
   ],
   "status": "Okayu is an active member of hololive GAMERS. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2019-04-06",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Nekomata-Okayu.md › Background (debut: Background)"
   }
  }
 ],
 "world": [
  {
   "name": "JP Senpai Pairs",
   "file": "bible/world/JP-Senpai-Pairs.md",
   "role": "Relationship",
   "other_names": [
    "AS_tar",
    "FWMCAZ",
    "TakoNeko",
    "Suisei and Calli",
    "Okayu and Ina",
    "AZKi and FUWAMOCO",
    "Ayame and Kiara"
   ]
  }
 ],
 "units": []
}
```

### projects/holoen/research/qa/packets/jp.md

# Audit packet: jp

Snapshot: git 0b372b1. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Hoshimachi-Suisei.md` cc7453e0e0dc; `bible/characters/AZKi.md` f9ef7601a752; `bible/characters/Nakiri-Ayame.md` 675a9db7cbb2; `bible/characters/Nekomata-Okayu.md` 80148bfc0586; `bible/world/JP-Senpai-Pairs.md` 26d530531779

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Hoshimachi Suisei — `bible/characters/Hoshimachi-Suisei.md`
**[SW] Groups:** hololive, hololive 0th Generation, Star Flower, miComet, Hoshimatic Project, Shiranui Kensetsu, Startend, AS_tar, MOMAS, Midnight Grand Orchestra
**[SW] Other Names:** Suisei, Sui-chan, Suicopath, Hoshimachi
**[SW] Background:** Suisei is an active member of hololive Generation 0. She has no supernatural abilities; her persona is a virtual idol, not a fantasy creature. She debuted on 2018-03-22 as an independent VTuber who, by secondary accounts, drew her own design and edited her own videos, joined hololive production's music label INoNaKa Music with AZKi in 2019, and moved to hololive on 2019-12-01. A singer with original songs such as "Stellar Stellar," "GHOST," "Bibbidiba" and "Prima Donna," she was the first VTuber on THE FIRST TAKE (2023), sang for Mobile Suit Gundam GQuuuuuuX (2025), headlined the Nippon Budokan ("SuperNova," 2025), and is on her 2026 arena tour "Once Upon a Stellar." In 2026 she set up her own management agency, Studio STELLAR, for her solo work, staying in hololive for collabs and group activities. With the English cast she made "CapSule" and "Wicked" with Calli (2022) and sang "Wicked" at Calli's first solo concert, sings with IRyS, AZKi and Moona as Star Flower, sang "High Tide" and "BIBBIDIBA" at the 2024 English concert, and was a face of hololive night at Dodger Stadium with Gura and Pekora (2024).
**[SW] Relationships:** Mori Calliope: collaborators on "CapSule" and "Wicked" (2022), including their performance at Calli's concert New Underworld Order, and Calli hosted a watch party of Suisei's first tour. AZKi: 0th-generation labelmate since INoNaKa Music ("AS_tar"); a 2026 horror off-collab and "Going My Way." IRyS: Star Flower with AZKi and Moona Hoshinova ("story time," 2022); "High Tide" with IRyS, Moona and Hakos Baelz at the 2024 English concert. Ninomae Ina'nis and Gawr Gura (graduated): "BIBBIDIBA" with Moona at that concert; Gura and Usada Pekora were fellow featured talents in the July 5, 2024 hololive night collaboration with the Los Angeles Dodgers. Takanashi Kiara: HOLOTALK #8 and a Tales of Arise discussion (2021); a dance-challenge short (2025). Hakos Baelz: a "Moonlight" dance cover (2025). FUWAMOCO: a "Chatter Chatter" dance short and Puyo Puyo Tetris 2 coaching (2026). Nanashi Mumei (graduated): a #bibbidibachallenge short (2024). Nerissa Ravencroft: a "BIBIDEBA" dance short (2024). Koseki Bijou: watched her Fortnite concert on stream (2026). Nekomata Okayu: "MOMAS"; Okayu's 2025 New Year Game Festival team with Nakiri Ayame, Ina, IRyS and Cecilia, among others. Sakura Miko: her miComet partner. Shiranui Flare: "Shiranui Kensetsu," where Suisei is the PR director. Hakui Koyori and Kazama Iroha: her Hoshimatic Project ("BEEP BEEP," 2026); Sakamata Chloe was in its earlier lineup (secondary); she coached Iroha at Puyo Puyo Tetris (2023). Houshou Marine: "Chatter Chatter" (2026). Shirogane Noel: a fellow Shiranui Kensetsu member. La+ Darknesss, Nakiri Ayame and Shishiro Botan: holoGTA (2024); La+, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024). Kikirara Vivi: taught her Tetris (2026).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2018-03-22 | Debut as an independent VTuber (her birthday is the same date) | [Observed SU2] |
| 2019-05-19 | Joins INoNaKa Music, hololive production's music label, with AZKi | [Observed SU2; SU3, secondary] |
| 2019-12-01 | Moves to the main hololive branch; later counted in "0th generation" | [Observed SU2] |
| 2021-04-17 | Kiara's HOLOTALK, 8th guest ("cometori") | [S1 a6DjP7NYwUE] |
| 2022 | "CapSule" with Mori Calliope; single "TEMPLATE / Wicked feat. Mori Calliope"; sings "Wicked" at Calli's first solo concert (07-21) | [S1] |
| 2022-12-31 | "story time" as Star Flower with AZKi, Moona Hoshinova and IRyS | [Official SU6] |
| 2023-01-20 | First VTuber on THE FIRST TAKE ("Stellar Stellar") | [Observed SU2; SU3, secondary] |
| 2023-11 | Starts "Hoshimatic Project" | [Observed SU2] |
| 2024-07-05 | hololive night at Dodger Stadium with Usada Pekora and Gawr Gura | [Official SU7] |
| 2024-08-02 | Introduces herself as a "virtual idol"; profile drops "forever 18" | [Observed SU2] |
| 2024-08-24/25 | "High Tide" with IRyS, Moona and Hakos Baelz, and "BIBBIDIBA" with Moona, Ina and Gura, at the English concert -Breaking Dimensions- | [Official SU8] |
| 2024-11 to 12 | First live tour "Spectra of Nova" (Saitama, Osaka, Fukuoka); Calli, FUWAMOCO and Elizabeth hold a watch party | [Observed SU2] [S1 YtVleZxIiNc] |
| 2025-02-01 | "SuperNova" at the Nippon Budokan | [Observed SU2] |
| 2025 | "I don't care" and "Bloom in the night" for Mobile Suit Gundam GQuuuuuuX; miComet's "Lollipop" (official digital release 10-03) | [Observed SU2] [Official SU10] |
| 2025-11-19 | At AZKi's "Departure" concert, AS_tar performed "The Last Frontier"; AZKi gave Suisei a reply to her earlier concert letter, and they unveiled "Going My Way" (digital release 2026-05-19). | [Official NEW-R5-002] |
| 2026-02-21 | "SuperNova: REBOOT" at K-Arena Yokohama | [Observed SU2] |
| 2026-03-08 | hololive 7th fes. "Ridin' on Dreams," STAGE 4 (with Calli, Kronii, Bijou, Nerissa) | [Official SU9] |
| 2026-03 | "Chatter Chatter" with Houshou Marine; playable in Fortnite (03-13 to 03-24) | [Observed SU4] [SU3, secondary] |
| 2026-03-22 | 8th anniversary: "Prima Donna"; arena tour "Once Upon a Stellar" announced; personal management agency Studio STELLAR for her solo work (she stays in hololive for collabs and group activities); fan club opens | [Observed SU2] |
| 2026-04-04 | [Unverified: identification of Suisei's reported Calliope appearance as UNCUT ROCK!!; the event and date require a direct locator.] | [ASR SU20, her own account] [Observed fan-clip titles, secondary] |
| 2026-04-18 | Hoshimatic Project's second song "BEEP BEEP" (official digital release; premiered the day before) | [Official SU10] [SU4] |
| 2026-05-18/19 | An AS_tar horror off-collab on AZKi's channel (v60QmEvEQqw), then "Going My Way" with AZKi | [Observed SU4; archived metadata] [Official AZKi file] |
| 2026-07-08/13 | Fan meeting "Hoshiyomi Pajama Party Vol.1" (Tokyo, Osaka) | [Observed SU2] |
| 2026-08-23 | Puyo Puyo Tetris 2 coaching collab with FUWAMOCO | [S1, secondary metadata: https://ckworks.jp/vinforadar/video/i6_T0tiQIkE] |
| 2026-08-30 | Original "GUM & DROP"; more fan meetings and a December concert with tuki. announced | [Observed SU2] |
| 2026-09-08 | Arena tour "Once Upon a Stellar" opens (Yokohama, Kobe, Nagoya, Fukuoka; to 11-12) | [Observed SU2] |
**Dossier · Hard Facts (continuity):**
- Debut 2018-03-22 (indie); hololive from 2019-12-01; 0th generation; birthday 22 March; 160 cm; illustrator
  Teshima Nari; fans "Hoshiyomi" (Stargazers); oshi mark ☄️; stream tag #ほしまちすたじお.
- Studio STELLAR (from 2026-03-22): her personal management agency for solo work; hololive collabs and group
  activities continue.
- Upcoming after the baseline: tour dates to 2026-11-12; a December 2026 concert with tuki.; Midnight Grand
  Orchestra's "Project: Allegro" (2027-02-11).

### AZKi — `bible/characters/AZKi.md`
**[SW] Groups:** hololive, hololive 0th Generation, Star Flower, SorAZ, AS_tar, AzuIro, KanatAZ, RosaMiA
**[SW] Other Names:** AZKichi, Azukichi, Azu-chan, AZAZ, AzuAzu, Virtual Diva AZKi
**[SW] Background:** AZKi is an active member of hololive Generation 0. She has no supernatural abilities; her lore is a performed persona. She debuted in 2018 as "Virtual Diva AZKi," joined hololive production's music label INoNaKa Music with Hoshimachi Suisei in 2019, and transferred to hololive's main group in April 2022 (secondary historical reference). Her units include SorAZ with Tokino Sora, AS_tar with Suisei ("Going My Way," 2026), Star Flower with Suisei, Moona Hoshinova and IRyS ("story time," 2022), AzuIro with Kazama Iroha ("AZUIRO BESTIE DAYS," 2025) and, from 2026, RosaMiA. She headlined "Departure" at Pia Arena MM in 2025 and held her 8th birthday live, "Cross Over," on 2026-07-01. With the English cast she sings in Star Flower with IRyS, took Calli's English lesson (2022), was Kiara's 13th HOLOTALK guest (2021), and played a FUWAMOCO-themed GeoGuessr map with the twins (2024), who also appeared at her 2025 birthday live.
**[SW] Relationships:** Hoshimachi Suisei: labelmate since INoNaKa Music and 0th-generation partner ("AS_tar"); a 2026 horror off-collab and "Going My Way." IRyS: Star Flower with Suisei and Moona Hoshinova ("story time," 2022); IRyS covered AZKi's "Inochi" (2021); R.E.P.O. (2025); "A Cruel Angel's Thesis" at AZKi's 2026 birthday live. FUWAMOCO: "FWMCAZ," a FUWAMOCO-themed GeoGuessr map (2024), a singing collab with Minato Aqua, and an appearance at her 2025 birthday live. Takanashi Kiara: HOLOTALK's 13th guest (2021); the 2023 Sports Festival white team. Mori Calliope: her English lesson with IRyS and Tsunomaki Watame (2022); AZKi's "Orpheus" dance short (2025). Hakos Baelz: GeoGuessr (2023). Ouro Kronii and Elizabeth Rose Bloodflame: fellow members of Tokoyami Towa's 2025 New Year Game Festival team. Ninomae Ina'nis and Kronii: R.E.P.O. "JP & EN" (2025). Tokino Sora: her SorAZ partner. Amane Kanata and Kazama Iroha: collaborators associated with KanatAZ and AzuIro ("AZUIRO BESTIE DAYS," 2025). Nakiri Ayame: 2023 Sports Festival teammate. Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!" (2025), and a 3D karaoke with Koyori, Isaki Riona and Koganei Niko (2026); Lamy is also in "KALAZ" with Amane Kanata (secondary). Sakamata Chloe: "Kanaken" with Kanata (Minecraft and a 3D live, 2024). La+ Darknesss: GeoGuessr for Tochigi Day and other games (2025). Nekomata Okayu: Mario Kart World practice for Team Wind (2026-01-16) and AZKi's pun-ASMR contest (2025), with Shirogane Noel also playing. Houshou Marine: AZKi supplied soothing commentary for Marine's Holo Koshien stream (2026). Kikirara Vivi: GeoGuessr on Vivi's channel (2026).
**Dossier · Background Timeline:**
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
| 2025-11-19 | "Departure" concert: AS_tar performed "The Last Frontier"; she gave Suisei a reply to Suisei's earlier concert letter, and they unveiled "Going My Way" (digital release 2026-05-19). | [Official NEW-R5-002] |
| 2026-03-07 | hololive 7th fes. "Ridin' on Dreams," STAGE 3 (with IRyS, Bae, Shiori) | [Official AZ7] |
| 2026-04-01 | April Fools: a "new VTuber" debut on her original design | [AZ4] [ASR AZ20] |
| 2026-05-18/19 | AS_tar with Suisei: a horror off-collab, then "Going My Way" | [AZ4] |
| 2026-07-01 | "AZKi 8th Birthday Live 'Cross Over'": little-devil outfit; she performed Konomi Suzuki's "Redo"; IRyS appears in the archived short metadata ("A Cruel Angel's Thesis"; secondary setlist); "Saikyo Mirai Shodo" (credited to AZKi and Konomi Suzuki) released digitally 07-02 | [Observed AZ2; AZ4] [Official AZ11] [secondary setlist] |
| 2026-07 | Kagawa Prefectural Police traffic-safety ambassador; a commendation, "a hololive first" | [AZ4 titles] |
| 2026-09-20/21 | RosaMiA (with Aki Rosenthal and Ookami Mio): "Blossom Sinfonia," premiered 09-20 (reported), official digital release 09-21 | [Observed AZ2] [Official AZ12] |
**Dossier · Hard Facts (continuity):**
- Debut 2018-11-15; hololive main branch from 2022-04-01; 0th generation; birthday 1 July; 158 cm; fans
  "Kaitakusha" (Pioneers); oshi mark ⚒️; units SorAZ, AS_tar, Star Flower, AzuIro, KanatAZ, RosaMiA.
- Official words: "Floor" (yuka) and "Ceiling" (tenjō) for strong emotions.

### Nakiri Ayame — `bible/characters/Nakiri-Ayame.md`
**[SW] Groups:** hololive, hololive 2nd Generation, FAMS, AyaFubuMi, AyaSuba, Manji-gumi, OKFAMS
**[SW] Other Names:** Ayame, Ojou, Yo-san
**[SW] Background:** Ayame is an active member of hololive's 2nd generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2018-09-03; her 2nd-generation groupmates were Minato Aqua, Murasaki Shion, Yuzuki Choco and Oozora Subaru. Her originals include "Yoi no Yo, Yoi!", "Kawayo," "melting" and "Hanafubuki"; with Shirakami Fubuki and Ookami Mio as AyaFubuMi she performed "Ame Tokimeki Koimoyō," reported as a 2025 anime opening theme. Fubuki created her companion Poyoyo. Archived titles document VALORANT tournament participation; she was a guest artist at a Pretty Cure virtual music event and streams chats, karaoke and evening talks. With the English cast, archived metadata identifies her as Kiara's 23rd HOLOTALK guest (2022-10-09), places her on the 2023 Sports Festival white team with Kiara, Mumei, Ame, Nerissa and AZKi (her stream title celebrates its win), and lists her with Suisei, Ina, IRyS and Cecilia among the members of Okayu's 2025 New Year Game Festival team; she shared 7th fes STAGE 1 with Ina and FUWAMOCO (2026), and the official Anime NYC 2026 announcement listed her, Fubuki and Mio for an August 22 convention-exclusive stream.
**[SW] Relationships:** Takanashi Kiara: her 23rd HOLOTALK guest (2022, archived metadata) and a 2023 Sports Festival white-team teammate. Nekomata Okayu: "OKFAMS" (secondary); Okayu's 2025 New Year Game Festival team, and 7th fes STAGE 1 together. Hoshimachi Suisei, Ninomae Ina'nis, IRyS and Cecilia Immergreen: listed among the members of Okayu's 2025 New Year Game Festival team; Ina and FUWAMOCO shared her 7th fes stage. AZKi, Nanashi Mumei, Watson Amelia and Nerissa Ravencroft: the 2023 Sports Festival white team. Shirakami Fubuki and Ookami Mio: AyaFubuMi (a reported 2025 anime opening); Fubuki created her companion Poyoyo; FAMS with Oozora Subaru (AyaSuba). Murasaki Shion and Minato Aqua: Manji-gumi. Inugami Korone: "Onigashima Combi." Houshou Marine: a third-generation junior whom secondary accounts say Ayame admires. La+ Darknesss, Hoshimachi Suisei and Shishiro Botan: holoGTA (2024). Takane Lui: "Onikan" (archived titles, 2025). Shirogane Noel: an Audio-Technica sponsored stream (2025-07-11). (Pair and unit names other than official song credits come from secondary references.)
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | An oni from the Underworld Academy, its student council president; she pranks people with will-o'-the-wisps | [Official AY1] |
| 2018-09-03 | Debut, hololive 2nd generation (with Minato Aqua, Murasaki Shion, Yuzuki Choco, Oozora Subaru) | [Official AY1] [Observed AY2] |
| 2021-10-03 | First single "Yoi no Yo, Yoi!" | [Observed AY2; AY3] |
| 2022-10-09 | Kiara's HOLOTALK, 23rd guest (season 2 opener) | [AY5 h1EaCnoKhwk] |
| 2023 | "Kawayo"; a guest artist at the Pretty Cure virtual music event (12-09); the hololive Sports Festival white team wins (with Kiara, Mumei, Ame, Nerissa, AZKi) | [Observed AY2; AY3; AY4 tHP7bd8Jtm0] |
| 2024 | "melting"; "Chief VTuber Officer" for Maxell Izumi (12-02) | [Observed AY2; AY3] |
| 2025-01 | "Ame Tokimeki Koimoyō," the anime opening sung with Fubuki and Mio (AyaFubuMi) | [Observed AY2; AY3] |
| 2025-01-13 | On Okayu's team at the New Year Game Festival (with Suisei, Ina, IRyS, Cecilia) | [AY5 THMIBrxnp-E] |
| 2025-09-03 | 7th anniversary: a new 3D kimono and "Hanafubuki" | [Observed AY2] |
| 2025-11-09 | VALORANT VSaikyou with "Saki Ike Ninja" (participation; placement not inferred) | [Observed AY2, secondary; AY4] |
| 2026-02-14 | A new pink kimono outfit | [Observed AY2; AY4] |
| 2026-03-06 | hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Okayu, Ina, FUWAMOCO) | [Official AY6] [Observed AY3] |
| 2026-08-22 | Anime NYC: an announced convention-exclusive stream with Fubuki and Mio | [Official AY7] |
| 2026-09-19 | Digital release of "BANZAI☆MANKAI." | [Official NEW-R5-008] |
**Dossier · Hard Facts (continuity):**
- Debut 2018-09-03; hololive 2nd generation; birthday 13 December; 152 cm; illustrator Nana Kagura; fans
  "Nakiri-gumi" (Nakiri Gang); mascot Poyoyo; emoji 😈; first person "Yo" (余).
- Swords: "Rasetsu" (black handle) and "Asura" (red handle).

### Nekomata Okayu — `bible/characters/Nekomata-Okayu.md`
**[SW] Groups:** hololive, hololive GAMERS, OkaKoro, SMOK, OKFAMS, MOMAS, TakoNeko, SubaOka
**[SW] Other Names:** Okayu, Okayun, Okanyan
**[SW] Background:** Okayu is an active member of hololive GAMERS. She has no supernatural abilities; her lore is a performed persona. She debuted on 2019-04-06 and belongs to hololive GAMERS with Shirakami Fubuki, Ookami Mio and Inugami Korone. Secondary event histories record solo concerts in 2022 and 2025, GAMERS concert appearances and two million subscribers in May 2025; secondary coverage credits her as the star and supervisor of "Okayu Nyūmu!", and its 2026 sequel's publisher supports her starring role. With the English cast she released "Kurukuru Cruise" with Ninomae Ina'nis (2025); secondary accounts document her appearing with Korone in FUWAMOCO's 3D debut (2024), and the twins hosted a 2025 watch-along of her concert. Archived stream metadata documents her as Kiara's 18th HOLOTALK guest (2021), a guest at Mumei's 3D live (2024), a pop-up Mario Party with Calli, Anya and Ao (2024) and her 2025 New Year Game Festival team with Ina, IRyS and Cecilia among its members.
**[SW] Relationships:** Ninomae Ina'nis: their pairing is called "TakoNeko" in secondary references; they released "Kurukuru Cruise" together (2025) and were teammates at the 2025 New Year Game Festival. FUWAMOCO: secondary accounts report Okayu's enthusiasm for the twins and her appearance with Korone at their 3D debut (2024); archived metadata documents the twins' 2025 watch-along of her concert. Takanashi Kiara: HOLOTALK's 18th guest (2021). Nanashi Mumei (graduated): a guest at Mumei's 3D live (2024). Mori Calliope: a pop-up Mario Party with Anya and Ao (2024). Gigi Murin: public translation-based banter during the 2026 New Year Game Festival (secondary clip metadata). IRyS and Cecilia Immergreen: members of her 2025 New Year Game Festival team. Hakos Baelz: kart events. Houshou Marine: gave her the nickname "Okanyan." Hoshimachi Suisei: "MOMAS." Nakiri Ayame: "OKFAMS." Inugami Korone: her OkaKoro collaborator and fellow GAMERS member ("Koro-san"). Shirakami Fubuki and Ookami Mio: her GAMERS. Hakui Koyori: a lateral-thinking puzzle collab (2025). La+ Darknesss: "Dorobo Kensetsu" and a 3D lie-detector challenge (2026). Takane Lui: Harry Potter watch-alongs (2025). ("Dorobo Kensetsu" comes from secondary references.) AZKi: Mario Kart World practice for Team Wind (2026-01-16) and AZKi's pun-ASMR contest (2025), where Shirogane Noel also played. Kikirara Vivi: a 2026 collab on Vivi's channel. Sakamata Chloe: chorus on her "Bling-Bang-Bang-Born" cover (2025). Yukihana Lamy: a "Lukewarm" duet cover (2024).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | A cat raised by an old woman who runs an onigiri shop; she formerly streamed from the computer in that woman's room (official lore, past tense) | [Official OK1] |
| 2019-04-06 | Debut in hololive GAMERS (with Shirakami Fubuki, Ookami Mio, Inugami Korone) | [Observed OK2; OK3] |
| 2021-11-27 | Kiara's HOLOTALK, 18th guest (the show's first-anniversary episode) | [OK5 FjsTGuBQlO0] |
| 2022-09-30 | First solo concert "Poison-nya Syndrome" | [Observed OK3] |
| 2023-12-12 | Team Mario Kart with Hakos Baelz and FUWAMOCO among others | [OK5 Janl2FCKmsg] |
| 2024 | Guest at Nanashi Mumei's 3D live "Outside the Box"; first GAMERS fes (Yoyogi) | [Mumei file] [Observed OK3] |
| 2024-08-10 PDT | Cameo with Inugami Korone at FUWAMOCO's 3D debut | [FUWAMOCO card] |
| 2024-09-15 | A pop-up Mario Party with Mori Calliope, Anya Melfissa and Hiodoshi Ao (archived metadata) | [OK4 WnKCmQ2iXww] |
| 2025-01-13 | Leads a team at the hololive New Year Game Festival (with Suisei, Ayame, Ina, IRyS, Cecilia) | [OK4 THMIBrxnp-E] |
| 2025-05-15/28 | 2 million subscribers; second solo concert "PERSONYA RESPECT" at Pia Arena MM (FUWAMOCO watch it together) | [Observed OK2] [OK5 gzPgXfYAbGg] |
| 2025-07-05/06 | GAMERS fes 2 at Saitama Super Arena | [Observed OK2; OK3] |
| 2025-08-05 | "Kurukuru Cruise" with Ninomae Ina'nis (official digital release; a video premiere may be dated a day earlier) | [Official OK7] [OK5 t7lNu-p_ANs] |
| 2026-02-23 | Released "Non Delicious"; she performed it on STAGE 1 of hololive 7th fes. (2026-03-06). | [Official NEW-R5-011] |
| 2026-03-06 | hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Ayame, Ina, FUWAMOCO) | [Official OK6] [Observed OK3] |
| 2026 | The game sequel "Okayu Nyūmu! R," which she stars in and supervises; Final Fantasy VII playthrough series | [Observed OK3; OK4] |
**Dossier · Hard Facts (continuity):**
- Debut 2019-04-06; hololive GAMERS; birthday 22 February; 152 cm; illustrator Kamioka Chiroru; fans
  "Onigiryā" (Onigiris); emoji 🍙; stream tag #生おかゆ.
- First person "boku"; greeting "Mogu mogu~ Okayu~!"

### JP Senpai Pairs — `bible/world/JP-Senpai-Pairs.md`
**[SW] Other Names:** AS_tar, FWMCAZ, TakoNeko, Suisei and Calli, Okayu and Ina, AZKi and FUWAMOCO, Ayame and Kiara
**[SW] Description:** The ties of four members of hololive's historical JP roster, Hoshimachi Suisei, AZKi, Nakiri Ayame and Nekomata Okayu, with the English cast and with each other. Suisei and Calli: collaborators on "CapSule" and "Wicked" (2022) and a performance at Calli's concert New Underworld Order; archived uploads document Calli's watch-alongs of Suisei's concerts. Suisei, AZKi, IRyS and Moona Hoshinova are the official unit Star Flower ("story time," 2022); Suisei sang "High Tide" with IRyS, Moona and Hakos Baelz and "BIBBIDIBA" with Moona, Ina and Gura at the 2024 English concert, and was a face of hololive night at Dodger Stadium with Gura and Pekora (2024). AZKi and FUWAMOCO: a FUWAMOCO-themed GeoGuessr collaboration (2024), a singing stream with Minato Aqua, and the twins' guest appearance at her 2025 birthday live (secondary). Okayu and Ina released "Kurukuru Cruise" (2025); secondary accounts call them "TakoNeko" and document Okayu's appearances around FUWAMOCO. Archived episode records list all four as guests on Kiara's translated talk show HOLOTALK (2021–2022). Ayame's ties with the English cast are HOLOTALK, team events and shared festival billing. Among themselves: Suisei and AZKi are "AS_tar" ("Going My Way," 2026); secondary references list MOMAS (Suisei, Okayu) and OKFAMS (Ayame, Okayu). All four were billed at hololive 7th fes. (March 2026).
**[SW] Rules:** These entries record public collaborations and senpai–kouhai ties. Same billing, same team, same song, a watch-along and a direct conversation are different kinds of evidence; none implies another. Language use depends on the event; HOLOTALK uses live translation. Gura and Mumei appear only as memories; Ame is an affiliate. A collab title shows that a collab happened, not how close two members are.
**Dossier · History:**
| Date | Event | Pair |
|---|---|---|
| 2021-04-17 | HOLOTALK #8 | Kiara–Suisei |
| 2021-07-31 | HOLOTALK #13 | Kiara–AZKi |
| 2021-11-27 | HOLOTALK #18 (first anniversary) | Kiara–Okayu |
| 2022-03-12 | HOLO ENGLISH LESSON #03 | Calli with IRyS, Watame, AZKi |
| 2022-04 | "CapSule"; "TEMPLATE / Wicked feat. Mori Calliope" | Death Star |
| 2022-07-21 | "Wicked" at New Underworld Order | Death Star |
| 2022-10-09 | HOLOTALK #23 | Kiara–Ayame |
| 2022-12-31 | "story time" | Star Flower (Suisei, AZKi, Moona, IRyS) |
| 2023-11 | Sports Festival, white team wins | Ayame and AZKi with Kiara, Mumei, Ame, Nerissa |
| 2024-02-09 | GeoGuessr FUWAMOCO map | FWMCAZ |
| 2024-07-05 | hololive night at Dodger Stadium | Suisei, Gura, Pekora |
| 2024-08-10 PDT | FUWAMOCO's 3D debut, Okayu and Korone cameos | FUWAMOCO–Okayu |
| 2024-08-24/25 | "High Tide" at -Breaking Dimensions- | Suisei with IRyS, Moona, Bae |
| 2024-11-14 | "Spectra of Nova" watch party | Calli, FUWAMOCO, Elizabeth for Suisei |
| 2025-01-13 | New Year Game Festival, Okayu's team | Okayu, Suisei, Ayame with Ina, IRyS, Cecilia |
| 2025-05-28 | "PERSONYA RESPECT" watch-along | FUWAMOCO for Okayu |
| 2025-07 | "Sweet Pop Story" | AZKi with FUWAMOCO |
| 2025-08-05 (digital release; zone unspecified) | "Kurukuru Cruise," by Ninomae Ina'nis and Nekomata Okayu | TakoNeko; official catalog 604, checked 2026-10-04 |
| 2026-03-06 to 03-08 | hololive 7th fes. "Ridin' on Dreams" (STAGE 1 Mar 6, STAGE 3 Mar 7, STAGE 4 Mar 8) | all four on stage |
| 2026-08-22 | Anime NYC: an announced convention-exclusive stream | Ayame (with Fubuki, Mio) |
**Dossier · Hard Facts (continuity):**
- Official units: Star Flower (Suisei, AZKi, Moona Hoshinova, IRyS; "story time," 2022-12-31).
- Concert pairings: "Wicked" (Suisei with Calli, 2022-07-21); "High Tide" (IRyS, Bae, Moona, Suisei; 2024).
- Kiara's HOLOTALK guests: Suisei #8, AZKi #13, Okayu #18, Ayame #23.
- 7th fes (March 6–8, 2026; STAGE 1 Mar 6, STAGE 3 Mar 7, STAGE 4 Mar 8): STAGE 1 Ayame, Okayu (with Ina, FUWAMOCO); STAGE 3 AZKi (with IRyS, Bae, Shiori);
  STAGE 4 Suisei (with Calli, Kronii, Bijou, Nerissa).

Incoming claims continue in `jp-incoming.md`.

### projects/holoen/research/qa/packets/jp-incoming.md

# Audit packet: jp (incoming claims)

Snapshot: git 0b372b1.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: shimachi Suisei|AZKi and FUWAMOCO|Virtual Diva AZKi|Suisei and Calli|Ayame and Kiara|JP Senpai Pairs|Nekomata Okayu|Okayu and Ina|Nakiri Ayame|Hoshimachi|Suicopath|Sui-chan|Azukichi|Azu-chan|TakoNeko|AZKichi|Okanyan|Suisei|Okayun|Yo-san|FWMCAZ|AzuAzu|AS_tar|Ayame|Okayu|AZKi|Ojou|AZAZ)(

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Nekomata Okayu, Hoshimachi Suisei and Nakiri Ayame: Okayu's 2025 New Year Game Festival team (archived listing).
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Nekomata Okayu, Hoshimachi Suisei, Nakiri Ayame | JP seniors | Listed with Ina and IRyS among the members of Okayu's 2025 New Year Game Festival team (archived team listing) | [Okayu file OK4] [Ayame file AY5] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: AZKi: fellow member of Tokoyami Towa's 2025 New Year Game Festival team, with Kronii (secondary roster).
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | AZKi | — | Fellow members of Tokoyami Towa's 2025 New Year Game Festival team, with Kronii (secondary roster) | [AZKi file AZ4] |

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: AZKi: a FUWAMOCO-themed GeoGuessr collaboration ("FWMCAZ"); secondary records also document a singing stream with Minato Aqua and the twins' guest appearance at her 2025 birthday live.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Nekomata Okayu: secondary accounts report her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; archived metadata documents the twins' 2025 watch-along of her concert.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Hoshimachi Suisei: Puyo Puyo coaching (2026).
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Nakiri Ayame: the 7th fes. stage (2026).
- `bible/characters/Fuwawa-Abyssgard.md › Background Timeline`: | 2024-08-10 PDT | 3D debut with a wrestling segment and cameos by Okayu and Korone | [Observed FW2 §2024] |
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Secret Society holoX (Koyori, Lui, Iroha, La+) | JP members | "FUWAMOKOYO" with Koyori (FUWAMOCO Morning ep. 90, 2024-04-26); Lethal Company with Koyori and Fubuki (2024-03-09); Koyori a guest at their 2025 birthday concert; "TWIN DAY WITH LUI" (2023-11-25); a cookie-quiz off-collab presented by Iroha and AZKi, the twins as challengers (2024-10-27); dance shorts to La+'s and Lui's 2026 songs | [S1 gCYXKgYcFmk, XR1PEtj15kE, ouQF2A1l_cI, MbqO5OPuT80, JgOwJ7m89Lk] |
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Hoshimachi Suisei | JP senior | A "Chatter Chatter" dance short (2026-03-31); Puyo Puyo Tetris 2 coaching (2026, secondary metadata) | [Suisei file S1] |

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Hoshimachi Suisei and Usada Pekora: fellow featured talents in the July 5, 2024 hololive night collaboration with the Los Angeles Dodgers.

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Nekomata Okayu: public translation-based banter during the 2026 New Year Game Festival, per secondary clip metadata.
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Nekomata Okayu | JP senior ("OkaGigi," secondary pair name) | Translation-based banter during the 2026 New Year Game Festival (secondary clip metadata, https://ckworks.jp/vinforadar/video/kirinuki/Nme9QhN3i2s); its relationship jokes are a comedy bit, and its dialogue is not quoted | [Observed GG2, secondary] |

### from Hakos Baelz
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Hoshimachi Suisei: "High Tide" with IRyS and Moona at Breaking Dimensions (2024) and Bae's "Moonlight" dance cover (2025).
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: AZKi: GeoGuessr (2023).
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Nekomata Okayu: team kart events (2023, 2024).
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2024-08-24/25 | -Breaking Dimensions-: "Our Promise" with Promise; "BLUE CLAPPER" with Calli, IRyS and Koseki Bijou; solo "GEKIRIN"; "High Tide" with IRyS, Moona Hoshinova and Hoshimachi Suisei | [Official HB5] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Moona Hoshinova (ID), Hoshimachi Suisei (JP), Usada Pekora (JP), Ayunda Risu (ID) | Cross-branch | "High Tide" with IRyS, Moona and Suisei (2024); "HIDE & SEEK 〜Nakayoku Kenkashina〜" with Pekora (2023); "holorodents" with Pekora and Risu (secondary) | [Official HB5, HB9] [Observed HB2] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Hoshimachi Suisei, AZKi, Nekomata Okayu | JP seniors | "High Tide" with Suisei, IRyS and Moona (2024) and a "Moonlight" dance cover (2025); GeoGuessr with AZKi (2023); team kart events with Okayu (2023, 2024) | [Suisei file SU8, S1] [AZKi file AZ5] [Okayu file OK4] |

### from Hakui Koyori
- `bible/characters/Hakui-Koyori.md › [SW] Background`: She sang in "Blue Journey" with Marine, Noel, Lamy, Botan, Lui and Sakura Miko (2023); secondary records place her in Suisei's Hoshimatic Project from 2023; archived 2025 collabs bill her, AZKi and Lamy as "KoZMy."
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: AZKi and Yukihana Lamy: "KoZMy"
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: (archived 2025 titles); a 3D karaoke with AZKi (2026); a #ラミこよ off-collab with Lamy (2026).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: Hoshimachi Suisei: Hoshimatic Project (secondary).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: Nekomata Okayu: a lateral-thinking puzzle collab she hosted (2025).
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2025 | Weekly Famitsu column launched (07-17); archived collabs bill Koyori, AZKi and Lamy as "KoZMy" (08-03, 08-20); "pink-haired pair" talk with Marine | [KO7] [KO4 lvgC3pW-LVA, oxWPvsUb_3Y] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | AZKi, Yukihana Lamy | "KoZMy" (archived titles) | Archived 2025 collabs bill the trio as KoZMy (formation talk 08-03, a horror monitoring game 08-20); a four-person 3D karaoke with AZKi (2026-02-03, not a KoZMy event); a #ラミこよ off-collab with Lamy (2026-03-24) Lamy: "Snow halation" together on STAGE 1 of hololive 7th fes. (2026-03-06). | [KO4 lvgC3pW-LVA, oxWPvsUb_3Y, 1HQL3WJPBHA] [Lamy channel Zi8R63ee0Fs] [Official, 7th fes. STAGE 1 report] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Hoshimachi Suisei | Hoshimatic Project | Idol-group practice unit (2023–), "BEEP BEEP" (2026) | [KO2] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Nekomata Okayu | — | A lateral-thinking puzzle collab hosted by Koyori, with Shion, Okayu and Chloe (2025-01-07); plays Okayu's game (2025) | [KO4 PtjqrNUOSWA] |
- `bible/characters/Hakui-Koyori.md › Story Engine`: 2. A KoZMy horror night in which Koyori volunteers AZKi and Lamy as test subjects.

### from Houshou Marine
- `bible/characters/Houshou-Marine.md › [SW] Background`: (2024), held a solo concert (2024), performed in hololive Fantasy's "#OperationHeartfulCuties" concert (2026), released "Chatter Chatter" with Suisei (2026) and the single "Kyapi"
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Hoshimachi Suisei: "Chatter Chatter"
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Nekomata Okayu: Marine gave her the nickname "Okanyan"
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: (Okayu's official profile).
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Nakiri Ayame: a second-generation senior.
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: AZKi: commentary for her Holo Koshien stream (2026).
- `bible/characters/Houshou-Marine.md › Behavioral Traits`: 5. A singer and idol: albums, a solo concert (2024), and in 2026 "Chatter Chatter" with Suisei (official digital release 2026-03-01; anime MV 2026-02-28) and the single "Kyapi." [Observed MA2 §Discography, secondary; MA4]
- `bible/characters/Houshou-Marine.md › Background Timeline`: | 2026-02-28 | "Chatter Chatter" with Hoshimachi Suisei: anime MV (official digital release 2026-03-01) | [MA4 di9NZ6ja_mE] [Official music 711] |
- `bible/characters/Houshou-Marine.md › Background Timeline`: | 2026-09 | Holo Koshien series: a baseball team followed through successive in-game seasons; Koyori joined the 09-17 session and AZKi commentated on 09-26. | [Archive metadata NEW-R5-014, NEW-R5-006] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Hoshimachi Suisei | "Chatter Chatter" (2026) | A duet with an original anime MV. The wiki's holoALICE and MOMAS labels were not verified in review They performed "Chatter Chatter" together on STAGE 4 of hololive 7th fes. (2026-03-08). | [MA4] [MA2] [Official NEW-R5-003] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Nekomata Okayu | — | Marine gave her the nickname "Okanyan"; Okayu's official profile recommends their marshmallow-reading stream. The wiki's HoLOGSS and MOMAS labels were not verified in review | [Okayu file OK1] [MA2] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Nakiri Ayame | 2nd-gen senior | Ayame's card records secondary accounts that she admires Marine; no Marine-side source | [Ayame file, secondary] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | AZKi | JP kouhai | AZKi supplied commentary for Marine's Holo Koshien stream; the title billed it as soothing (2026-09-26). | [Archive metadata NEW-R5-006] |
- `bible/characters/Houshou-Marine.md › Arc`: - **Starting point:** active at the 2026 baseline: a hololive Fantasy concert, a duet with Suisei and a new single behind her.

### from IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: Nekomata Okayu and Nakiri Ayame: Okayu's 2025 New Year Game Festival team.
- `bible/characters/IRyS.md › [SW] Relationships`: Hoshimachi Suisei and AZKi: with Moona Hoshinova, the unit Star Flower ("story time," 2022); Suisei also performed "High Tide" with her, Bae and Moona at Breaking Dimensions (2024).
- `bible/characters/IRyS.md › Relationship Map`: | Hakos Baelz | Promise unitmate ("BaeRyS") | The married/divorced running bit; Bae once banned her from soda for a week after a lost bet; a 2023 off-collab and the "Daikirai na Hazu Datta" cover (2023); "High Tide" with Moona Hoshinova and Hoshimachi Suisei (2024); BaeRyS at Serendipity (2026) | [Observed R2 §Relationships, §Likes and dislikes] |
- `bible/characters/IRyS.md › Relationship Map`: | Nekomata Okayu | JP senior | [Secondary, performance unchecked: a setlist records Okayu singing "JANE DOE" with IRyS at RACING TOWARDS HOPE (2026-03-21).] | [Secondary, holo3d-live setlist] |

### from Kazama Iroha
- `bible/characters/Kazama-Iroha.md › [SW] Background`: She formed the duo AzuIro with AZKi (covers, the 2025 song "AZUIRO BESTIE DAYS," off-collabs), sings in Suisei's Hoshimatic Project (credited on "BEEP BEEP," 2026) and performed at holoX's first in-person unit concert, "First MISSION"
- `bible/characters/Kazama-Iroha.md › [SW] Background`: With the English cast, archived channel metadata documents Calli's English lesson #02 with La+ and Gura (2022), a VALORANT collab with Ame and Kobo Kanaeru (2022), the cookie-battle off-collab she and AZKi presented with FUWAMOCO as challengers (2024), credited guest spots at Kiara's 2024 and 2025 lives, and a credit on "CHA-LA HEAD-CHA-LA" from Elizabeth's 2026 birthday show.
- `bible/characters/Kazama-Iroha.md › [SW] Relationships`: AZKi: "AzuIro," her steady duo (covers, "AZUIRO BESTIE DAYS" in 2025, Cuphead and off-collabs billed as summer camps).
- `bible/characters/Kazama-Iroha.md › [SW] Relationships`: Hoshimachi Suisei: Hoshimatic Project ("BEEP BEEP," 2026); coached her at Puyo Puyo Tetris (2023).
- `bible/characters/Kazama-Iroha.md › [SW] Relationships`: FUWAMOCO: challengers in the cookie battle she and AZKi presented (2024).
- `bible/characters/Kazama-Iroha.md › Behavioral Traits`: 4. A steady duo partner: "AzuIro" with AZKi (covers; the official song "AZUIRO BESTIE DAYS," released 2025-09-18; a Cuphead off-collab billed as a summer camp; GeoGuessr and Mario Kart). [IR4] [Official music 642]
- `bible/characters/Kazama-Iroha.md › Background Timeline`: | 2023 | AzuIro: GeoGuessr on a "Kazama map" AZKi made, covers and a first off-collab (08); Puyo Puyo Tetris coaching from Suisei (04); Hoshimatic Project (11-) | [IR4] [Observed IR2] |
- `bible/characters/Kazama-Iroha.md › Background Timeline`: | 2024 | Covers with La+ (「絶対敵対メチャキライヤー」, 03-11) and Lui (「右肩の蝶」, 04-11); originals "Mahou Shoujo☆Magical GOZARU" and "Dreamy Sky" (06); a cookie-battle off-collab on her channel, presented with AZKi, with FUWAMOCO as the challengers (10-27, JgOwJ7m89Lk); a guest at Kiara's 4th-anniversary live (10-06); 1 million subscribers (11-19) | [Observed IR2] [IR4] [IR5] |
- `bible/characters/Kazama-Iroha.md › Relationship Map`: | AZKi | "AzuIro" | Covers (2023, 2025), the official song "AZUIRO BESTIE DAYS" (2025-09-18), GeoGuessr, Cuphead (2025-06-03) and an off-collab billed as a summer camp, Mario Kart; co-presenter of the cookie battle (2024-10-27). The "shared Minecraft village" was dropped (its cited ID is the Cuphead stream) They performed "AZUIRO BESTIE DAYS" on STAGE 3 of hololive 7th fes. (2026-03-07); AZKi's encouragement in the MC left Iroha tearful. Their joint original "AZUIRO BESTIE DAYS" (2025-09-18). | [IR4 VxZVNuscS7c, -im-pIdanZY, mwhcZmc6-s8, JgOwJ7m89Lk] [Official music 642] [Official, 7th fes. report] [Official NEW-R6-021] |
- `bible/characters/Kazama-Iroha.md › Relationship Map`: | Hoshimachi Suisei | Hoshimatic Project | Coached her at Puyo Puyo Tetris (2023) | [IR4] [IR2] |
- `bible/characters/Kazama-Iroha.md › Story Engine`: 2. An AzuIro "summer camp" where AZKi navigates and Iroha charges ahead, de gozaru.

### from Kikirara Vivi
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: AZKi: GeoGuessr (2026).
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Hoshimachi Suisei: taught her Tetris on Vivi's channel (2026).
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Nekomata Okayu: a 2026 collab billed with a mock-scandalized "やーらし."
- `bible/characters/Kikirara-Vivi.md › Voice Profile`: - **Mock-scandalized title bit (written, 2026-08-25):** her collab with Okayu uses やーらし (yārashi, "lewd!") as its comic framing; spoken wording and delivery unverified. [Archive metadata NEW-R6-005]
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | AZKi | JP senior | A GeoGuessr collab billed as Vivi's first zero-distance guessing session with AZKi (2026-08-22). | [Archive metadata NEW-R6-006] |
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Hoshimachi Suisei | JP senior | Vivi hosted a Puyo Puyo Tetris session asking Suisei to teach her Tetris (2026-08-29). | [Archive metadata NEW-R6-007] |
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Nekomata Okayu | JP senior | A collab framed around the mock-scandalized title word やーらし (2026-08-25). | [Archive metadata NEW-R6-005] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Hoshimachi Suisei: Bijou watched her Fortnite concert on stream (2026).
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Hoshimachi Suisei | JP senior | Watched her Fortnite concert on stream ("THE SUISEI CONCERT IN FORTNITE?!", 2026) | [Suisei file S1 AhGrt2gr5pc] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Nekomata Okayu | JP senior | Credited participants together (with Kiara, Ina, Kobo and Todoroki Hajime) in the official purple-themed 3D variety program #パープル争奪戦 (2026-07-23). | [Archive metadata NEW-R3-008] |

### from La+ Darknesss
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Nerissa Ravencroft, Nakiri Ayame, Hoshimachi Suisei and Shishiro Botan: fellow holoGTA participants (2024).
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Suisei, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024).
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Nekomata Okayu: a 3D lie-detector challenge (2026); secondary references group them in "Dorobo Kensetsu."
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: AZKi: games and an ASMR "evaluation"
- `bible/characters/Laplus-Darknesss.md › Background Timeline`: | 2026-05-19 | A 3D lie-detector "challenge" to Nekomata Okayu | [LA4 F3i30BIJmtY] |
- `bible/characters/Laplus-Darknesss.md › Relationship Map`: | Nekomata Okayu | "Dorobo Kensetsu" (secondary) | A 3D lie-detector challenge (2026, archived metadata) | [LA2] [LA4] |
- `bible/characters/Laplus-Darknesss.md › Relationship Map`: | Nakiri Ayame, Hoshimachi Suisei, Shishiro Botan | — | Fellow holoGTA participants (2024-09; each archive establishes participation, not specific exchanges); Sammy's m HOLD'EM collaboration (2024) featured La+, Suisei, Botan and Shirakami Fubuki (publisher roster, not Ayame; a joint broadcast is not established) | [LA4 swqXHi1Z4ew, QLHSm3rpG8k] [Sammy announcement] |
- `bible/characters/Laplus-Darknesss.md › Relationship Map`: | AZKi | — | Games and an ASMR "evaluation" (2025); AZKi danced to her songs | [LA4] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: AZKi: a FUWAMOCO-themed GeoGuessr collaboration ("FWMCAZ"); secondary records also document a singing stream with Minato Aqua and the twins' guest appearance at her 2025 birthday live.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Nekomata Okayu: secondary accounts report her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; archived metadata documents the twins' 2025 watch-along of her concert.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Hoshimachi Suisei: a "Chatter Chatter" dance short and Puyo Puyo Tetris 2 coaching (2026).
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Nakiri Ayame: the 7th fes. stage with Okayu and Ina (2026).
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Secret Society holoX (Koyori, Lui, Iroha, La+) | JP members | "FUWAMOKOYO" with Koyori (FUWAMOCO Morning ep. 90, 2024-04-26); Lethal Company with Koyori and Fubuki (2024-03-09); Koyori a guest at their 2025 birthday concert; "TWIN DAY WITH LUI" (2023-11-25); a cookie-quiz off-collab presented by Iroha and AZKi, the twins as challengers (2024-10-27); dance shorts to La+'s and Lui's 2026 songs | [S1 gCYXKgYcFmk, XR1PEtj15kE, ouQF2A1l_cI, MbqO5OPuT80, JgOwJ7m89Lk] |
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Hoshimachi Suisei | JP senior | A "Chatter Chatter" dance short (2026-03-31); Puyo Puyo Tetris 2 coaching (2026, secondary metadata) | [Suisei file S1] |

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Hoshimachi Suisei: "Wicked" and, per archived uploads, "CapSule"
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Nekomata Okayu: Mario Party (2024, archived).
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: English-lesson guests Marine, AZKi, La+, Iroha, Lui and Chloe (2022); HOLOYOI guests Lui, Chloe, Noel and Botan (2023).
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Hoshimachi Suisei | JP senpai ("Death Star," fan-wiki pair name, dossier only) | "CapSule" (2022-04-04, archived upload M85xU-tbQ6c) and "Wicked feat. Mori Calliope" (2022); Suisei sang "Wicked" at New Underworld Order. The fan-wiki "starstruck" reaction and a reported Suisei guest spot at "UNCUT ROCK!!" (2026-04-04) were not verified in review and stay out of exported fields. | [Observed C4 §Relationships, secondary; C21-jlzD-jHtv9Y clip title] |

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: JP: archived uploads document her Q&A with Takane Lui, an April 2025 duet cover with Inugami Korone, and Korone, Okayu, Nene and Koyori as 2024 "Outside the Box" guests; Tokoyami Towa calls her "Mumi-chan"; Akai Haato: Minecraft; Nakiri Ayame: the 2023 Sports Festival white team.
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Hoshimachi Suisei: a #bibbidibachallenge short (2024).
- `bible/characters/Nanashi-Mumei.md › Background Timeline`: | 2024-08-05 | 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori | [Observed M3 title, description] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Inugami Korone, Nekomata Okayu (GAMERS); Momosuzu Nene, Hakui Koyori | JP seniors | All four were guests at "Outside the Box" (2024-08-05); Korone and Mumei released a duet cover of "とんとんまーえ！" (2025-04-23, P6GLC_HnCUU) | [Observed M3 descriptions] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Hoshimachi Suisei | JP senior | A #bibbidibachallenge short on Suisei's channel (2024-06-18) | [Suisei file SU4 zSB9yejsmGQ] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Hoshimachi Suisei: a "BIBIDEBA" dance short (2024).
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Nakiri Ayame, Nanashi Mumei and Watson Amelia: the 2023 Sports Festival white team.
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Hoshimachi Suisei | JP senior | A "BIBIDEBA" dance short (2024-11-04) | [Suisei file S1 JZ1Sfotw7tE] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Nakiri Ayame | JP senior | The 2023 Sports Festival white team, with Mumei and Ame | [Ayame file AY4] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Hoshimachi Suisei: "BIBBIDIBA"
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Nekomata Okayu ("TakoNeko," a secondary pair name): "Kurukuru Cruise"
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: (2025) and her 2025 New Year Game Festival team, with Nakiri Ayame.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: AZKi: R.E.P.O.
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Nekomata Okayu | JP senior | They performed "Kurukuru Cruise" together on STAGE 1 of hololive 7th fes. (2026-03-06). | [Official, 7th fes. STAGE 1 report] |

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: AZKi: R.E.P.O.

### from Sakamata Chloe
- `bible/characters/Sakamata-Chloe.md › [SW] Background`: She took part in the original lineup of Suisei's Hoshimatic Project (secondary roster reference), "Magical Girl holoWitches!" and the "Kanaken"
- `bible/characters/Sakamata-Chloe.md › [SW] Background`: Minecraft company with Amane Kanata and AZKi (a 3D live in 2024), and concluded her regular activities on 2025-01-26, holding a graduation live and remaining an affiliate; a secondary record has her singing "Sparkle" at Murasaki Shion's graduation live (2025-04-26).
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: AZKi: "Kanaken" with Amane Kanata (Minecraft, Chained Together, a 3D live, 2024).
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Hoshimachi Suisei: the original Hoshimatic Project lineup (secondary); a farewell video together (2025).
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Nekomata Okayu: chorus on her "Bling-Bang-Bang-Born" cover (2025).
- `bible/characters/Sakamata-Chloe.md › Background Timeline`: | 2024 | "Magical Girl holoWitches!" single (05-30); "Kanaken" 3D live with Kanata and AZKi | [Observed CH2] [CH4] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | AZKi | "Kanaken" with Amane Kanata | Minecraft construction "company," Chained Together and a 3D live (2024) | [CH4] [CH2] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Hoshimachi Suisei | Original Hoshimatic Project lineup (secondary roster reference; not on the 2026 "BEEP BEEP" credits) | 「沙花叉クロヱと星街すいせい」, part of her farewell video series (2025-01-22) | [CH2] [CH4 OF41reZNGnw] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Nekomata Okayu | JP senior | Credited among the chorus contributors to Chloe's "Bling-Bang-Bang-Born" cover (2025-01-24), with La+, Koyori and AZKi. | [Archive metadata NEW-R6-019] |

### from Shirogane Noel
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Hoshimachi Suisei: "Shiranui Kensetsu"
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Nakiri Ayame: an Audio-Technica sponsorship collab (2025).
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: AZKi and Nekomata Okayu: fellow players in AZKi's 3D pun-ASMR contest (2025).
- `bible/characters/Shirogane-Noel.md › Background Timeline`: | 2025 | #ノエこよ Power Pros exhibition with Koyori (01-10); Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (04-14); 3rd-gen R.E.P.O. with Marine, Pekora and Flare (07-05); Elden Ring Nightreign with Flare and Pekora; an Audio-Technica collab with Ayame (07-11); "TREVIAN KNIGHT" (official digital release 08-16), which FUWAMOCO danced to (09-30) | [NO4] [NO5] [Official music 622] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Hoshimachi Suisei | "Shiranui Kensetsu" (Shiraken) | A Minecraft construction company with Flare, Polka and Miko | [NO2] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Nakiri Ayame | — | An Audio-Technica earphone collab (2025) | [NO4] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | AZKi | JP kouhai | A player in AZKi's 3D pun-ASMR contest (2025-06-22), alongside Okayu, Subaru and Kanade. | [Archive metadata NEW-R5-004] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Nekomata Okayu | JP senior | Fellow players in AZKi's 3D pun-ASMR contest (2025-06-22); a group activity, not a pair collab. | [Archive metadata NEW-R5-004] |

### from Shishiro Botan
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: La+ Darknesss and Hoshimachi Suisei: holoGTA and, with Shirakami Fubuki, the m HOLD'EM poker collaboration (2024); Nakiri Ayame: holoGTA (2024).
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | La+ Darknesss, Nakiri Ayame, Hoshimachi Suisei | — | All four streamed holoGTA (2024-09); Sammy's m HOLD'EM collaboration (2024) featured La+, Suisei, Botan and Shirakami Fubuki, not Ayame (publisher roster; a joint broadcast is not established) | [BO4 jd7Bp0prwiI] [La+ file QLHSm3rpG8k] [Sammy roster] |

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: HOLOTALK guests include Houshou Marine (#1), Hoshimachi Suisei ("cometori"), AZKi, Shirogane Noel, Nekomata Okayu and Nakiri Ayame. holoX: La+ ("Glow in the Dark"), Chloe ("WILDCARD"), Koyori ("MIRAGE") and Iroha (a guest at her 2024 and 2025 lives).

### from Takane Lui
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Nekomata Okayu: Harry Potter watch-alongs (2025); secondary references list both in "Dorobo Kensetsu."
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Nakiri Ayame: "Onikan"
- `bible/characters/Takane-Lui.md › Behavioral Traits`: 5. Predicted game announcements before a 2026 Nintendo Direct; the first model renders her name for Nekomata Okayu as 「シャッチョ」 ("Shaccho"), unconfirmed by the second model, so it is not quoted. [ASR LU20, first model only] [Observed LU4 titles]
- `bible/characters/Takane-Lui.md › Background Timeline`: | 2025 | EP "Lieblings"; Code Geass ambassador (June, secondary); "Q&A With Bird Sisters" with Mumei (04-19); Harry Potter watch-alongs with Okayu; "FEAST" dance short with Bae (07-11) | [Observed LU2] [LU5] [LU4 Lj0MZFpHitQ, 5TUiccnytQA] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Nekomata Okayu | — | Harry Potter watch-alongs (2025); predictions before a 2026 Nintendo Direct; "Dorobo Kensetsu" (secondary); "Shaccho" is a first-model rendering only | [LU4] [ASR LU20] [LU2] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Nakiri Ayame | "Onikan" (archived titles) | Games and a sponsored collab billed おにかん (2025-08-09) | [LU4 YXaDmUXPSGo] |

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Nakiri Ayame and Nerissa Ravencroft: 2023 Sports Festival white-team teammates.
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Nakiri Ayame | JP senior | The 2023 Sports Festival white team, with Mumei and Nerissa | [Ayame file AY4] |

### from Yukihana Lamy
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: (2025), formed KoZMy with AZKi and Koyori (2025, per a collab title and secondary listings) and, per secondary records, is in KALAZ with Amane Kanata and AZKi.
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: AZKi: her KoZMy cover partner with Hakui Koyori on "Ai♡Scream!"
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: Nekomata Okayu: a "Lukewarm" duet cover (2024).
- `bible/characters/Yukihana-Lamy.md › Behavioral Traits`: 5. Units and pairs: NePoLaBo (with Botan, Omaru Polka and Momosuzu Nene); KALAZ (with Amane Kanata and AZKi, secondary); KoZMy (with AZKi and Koyori; a 2025-08-03 collab titled "KoZMy 結成⁉"); "Magamaga's" (with Nene, secondary); "Yakamashi Musume" (archived metadata); holoWitches. [Observed LM2 §Relationships, secondary] [Koyori file lvgC3pW-LVA]
- `bible/characters/Yukihana-Lamy.md › Background Timeline`: | 2025 | Joins "Magical Girl holoWitches!" (04–05); "Yoppara Music!" (official digital release 08-13); a "KoZMy 結成⁉" collab with AZKi and Koyori (08-03; secondary listings give its first anniversary in 2026-08) | [Observed LM2] [Official music 609] [Koyori file lvgC3pW-LVA] |
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | AZKi | "KALAZ" with Amane Kanata (secondary); "KoZMy" | Units with AZKi An impromptu group chat with AZKi and Inugami Korone on Lamy's channel (#あずらみころ, 2026-09-18). | [LM2] [hololiveinfo KALAZ entry] [Archive metadata NEW-R5-005] |
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | Nekomata Okayu | JP senior | A "Lukewarm" duet cover on Okayu's channel (2024-02-01). | [Member-upload title TIE-004] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › Beyond EN`: - **JP:** FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo); they game with Shirakami Fubuki and Hakui Koyori ("FUWAMOKOYO"); Okayu and Korone made cameos at their 3D debut; Oozora Subaru sang "HOT DUCK!" with Bijou and the twins; Akai Haato and Bijou are "Red Stone"; Ichijou Ririka (ReGLOSS, originally DEV_IS) played Smash Bros. with Bijou with a loser's punishment. [Observed S1; S2]

### from Concerts and Live Events
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous"; Promise's unit song "Our Promise"; "BLUE CLAPPER" by the CHADCast trio (Calli, IRyS, Bae) with Bijou; Bae's solo "GEKIRIN"; "High Tide" by IRyS, Bae, Moona Hoshinova and Hoshimachi Suisei [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; "R x R x R" by Calli and Bae; "Countach" by Bae, Gigi and guest Kureiji Ollie; Bae's solo "La Roja (Arrange ver.)"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before and separate from "-Breaking Dimensions-"), Jakarta (11-09), Singapore (11-30, with a pre-concert panel of Kaela Kovalskia and Ouro Kronii), Atlanta (12-15, a panel of Nerissa and Elizabeth Rose Bloodflame), Kuala Lumpur (12-21, Nerissa and Elizabeth again) and Taipei (2025-01-18, the finale) [Official S7]; and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Calli collaborates with Hoshimachi Suisei: Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones"
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ina appears with Aqua, Marine, Chloe and Gura in UMISEA's official 2023 roster and released "Kurukuru Cruise" with Nekomata Okayu (2025).
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower").
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Mori Calliope:** Calli drew Hoshimachi Suisei ("DRAWING MY SENPAI," 2021), Suisei featured at Calli's first solo concert ("Wicked," 2022), they talked live shows together (2023), and Calli hosts watch parties of Suisei's concerts ("We're Screaming Loud for Senpai!", 2024-11). Kobo Kanaeru calls her "Uncle Dad" ("Father Daughter GOLF," 2022; an in-person cooking-and-gaming collab, 2023). Units: "Holodeath" (with Kureiji Ollie); "LYRA," a five-singer cover of "III" with Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth (Kanata has since graduated); "MoRikka" with HOLOSTARS' Rikka (their song "spiral tones," 2021; fans "DeadTuners") [Official music entry S5]. Outside hololive: friends with Milky Queen and Ironmouse (a shared Underworld theme). [Observed S1 titles; S2 Calli §Relationships; Calli file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ninomae Ina'nis:** an artist among artists: the ocean unit UMISEA (formed 2021 with Minato Aqua, Houshou Marine and Gura; Chloe appears in the official 2023 roster; Aqua and Gura have graduated and Chloe is an affiliate); "HoloJEI" (Tsunomaki Watame, Kureiji Ollie, Anya Melfissa); "TakoBazo" (Vestia Zeta); "TakoNeko" (Nekomata Okayu, a secondary pair name; "Kurukuru Cruise," 2025; see "JP Senpai Pairs"); Shiranui Flare appeared on her 2025 AmiAmi special ("Flare?!!?"). She admires Marine as an artist. [Observed S1; S2 Ina; Ina file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **IRyS:** Shiranui Flare is a recurring collaborator (23 streams, 11 in 2024): horror and camping co-ops ("ふーたんとキャンプだ！"), Splatoon private matches, an off-collab karaoke (2025-03); units "Star Flower" (Moona, Suisei, AZKi), "IRySora" (Tokino Sora), "ReiRyS" (Reine), "OKFAIR" (Ollie, Kronii, Fauna, Anya, Reine). [Observed S1; S2 IRyS]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Nanashi Mumei** (graduated): HOLOTORI with Kiara, Subaru, Reine and Lui ("【MUMEI + LUI】Q&A With Bird Sisters !!!," 2025-04-19, fEO6kSCseE0); drawing collabs with Airani Iofi ("Doodles with IOFI," 2022-04-14, 2dWx7xg48xc; "SWIMSUITS!! with IOFI!," 2023-01-30, XCXF08GMUHY); a duet cover of "とんとんまーえ！" with Inugami Korone (2025-04-23, P6GLC_HnCUU), and Okayu, Korone, Nene and Koyori as guests at her 3D live "Outside the Box" (2024-08-05, gl7CwlEg2ZI); Minecraft "Peace & Love with HAACHAMA" (2025); Tokoyami Towa calls her "Mumi-chan." [Observed S1; Mumei file M2]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Hakos Baelz:** secondary references record her performed maternal-role jokes with Ookami Mio and Kureiji Ollie (her "mom" and "another mom"); with Ollie she sang "Countach" (with Gigi, -All for One- 2025) and played HoloEarth (2024); "HELP!!" with Kobo Kanaeru and Elizabeth at Serendipity (2026); "High Tide" with IRyS, Moona Hoshinova and Hoshimachi Suisei (-Breaking Dimensions- 2024); "Kakumei Dualism" with Natsuiro Matsuri in STAGE 3 of the 2026 fes (a secondary setlist; also her after-talk); Reanimal with Tokoyami Towa (2026); Lethal Company with Kaela Kovalskia (2023–24). Units (secondary): "holorodents" with Usada Pekora and Ayunda Risu; "RoBaelz" with HOLOSTARS' Yukoku Roberu. [Bae file HB2, HB3, HB5, HB20]
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 1. Calli hosts another watch party for Suisei's concert and loses her composure on the high note.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Calli's senpai: Suisei. Kiara's oshi: Pekora. Nerissa's oshi: Marine (and Kiara).

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **JP:** Houshou Marine (Fuwawa's oshi; a Touhou off-collab, 2024) and Omaru Polka (Mococo's oshi); Shirakami Fubuki (horror collabs and Lethal Company with Hakui Koyori, "FUWAMOKOYO"); Akai Haato, Tsunomaki Watame ("FUWAMOCO vs FUWAFUWA," 2024), Oozora Subaru (a Donkey Kong Country 2 off-collab, 2026), and Nekomata Okayu and Inugami Korone, who made cameos at their 3D debut. Guests at their 2025 birthday concert: Shiori, Bijou, Nerissa, Polka, Koyori, Marine, Ookami Mio and Fubuki. [Observed S1; S3]
- `bible/world/FUWAMOCO.md › History`: | 2024-08-10 PDT | 3D debut: a wrestling segment supervised by DDT Pro-Wrestling, Okayu and Korone cameos | "Lifetime Showtime" full version |

### from Fauna and Mumei Pairs
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Other collaborators:** Hakos Baelz is a recurring collaborator of both (Fauna's horror partner); Tsukumo Sana (graduated 2022) completed the Council; Inugami Korone recorded a duet cover with Mumei (2025-04-23) and, with Okayu, Nene and Koyori, guested at "Outside the Box" (2024-08-05). [Observed S1; Promise card]

### from Hakos Baelz Pairs
- `bible/world/Hakos-Baelz-Pairs.md › [SW] Description`: With IRyS she is BaeRyS: a performed "married and divorced" routine that fan references trace to a Minecraft bento exchange, covers and off-collabs, "High Tide" with Moona Hoshinova and Hoshimachi Suisei on stage in 2024, and their first duo stage, "LUVATORRRRRY!", at Serendipity 2026; in a pre-concert interview Bae says she was "blown away" by IRyS's voice, and IRyS admires Bae's creativity and calls their dynamic "a can of worms."
- `bible/world/Hakos-Baelz-Pairs.md › BaeRyS`: - **On stage:** "High Tide" with Moona Hoshinova and Hoshimachi Suisei at -Breaking Dimensions- (2024); the official unit BaeRyS at Serendipity (2026), "LUVATORRRRRY!", their first duo stage. [Official S3]
- `bible/world/Hakos-Baelz-Pairs.md › Beyond EN`: - Kobo Kanaeru ("HELP!!"), Kureiji Ollie ("Countach," HoloEarth; Bae's joking "other mom"), Ookami Mio (her joking "mom"), Natsuiro Matsuri ("Kakumei Dualism" at the 2026 fes), Moona Hoshinova and Hoshimachi Suisei ("High Tide"), Usada Pekora and Ayunda Risu ("holorodents," secondary), Kaela Kovalskia (Lethal Company). [Official S3] [S2, secondary] [Bae file HB20]
- `bible/world/Hakos-Baelz-Pairs.md › Hard Facts`: - Concert pairings: "BLUE CLAPPER" (Calli, IRyS, Bae, Bijou; 2024); "High Tide" (IRyS, Bae, Moona, Suisei; 2024); "R x R x R" (Calli & Bae; 2025); "Countach" (Bae, Gigi, Ollie; 2025); "HELP!!" (Kobo, Bae, Elizabeth; 2026).

### from JP Senpai Pairs 2
- `bible/world/JP-Senpai-Pairs-2.md › Among themselves`: - With the first four: Marine and Suisei released "Chatter Chatter" (2026); Marine gave Okayu the nickname "Okanyan" (Okayu's official profile); Noel and Suisei are in "Shiranui Kensetsu" (official unit roster); Noel and Ayame did an Audio-Technica sponsored stream (2025-07-11); Botan streamed holoGTA with Suisei and Ayame (2024) and joined the m HOLD'EM poker collab with Suisei (2024); Lamy and AZKi are in KoZMy (with Koyori) and, per secondary references, KALAZ (with Amane Kanata). The wiki's holoALICE, MOMAS and HoLOGSS labels were not verified in review. [S2] [S1] [Official]
- `bible/world/JP-Senpai-Pairs-2.md › History`: | 2026 | "Chatter Chatter"; Elizabeth's birthday cover | Marine, Suisei; Marine |

### from Justice Pairs
- `bible/world/Justice-Pairs.md › Beyond EN`: - **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone ("IT'S LOVE," iwnHChZq0N8, credits read by Claude); FUWAMOCO with Polka, Nene, Watame and Iroha; her 2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members). Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is "RaoRiRi" with Ichijou Ririka; "OkaGigi" is a secondary pair label for Gigi and Nekomata Okayu; secondary clip metadata records translation-based banter during the 2026 New Year Game Festival. It does not establish exact dialogue or a private relationship. Tsunomaki Watame sang "Cloudy Sheep" with Calli and Cecilia and "What an amazing swing" with Kiara and Raora at Serendipity. FLOW GLOW: Koganei Niko sang with Elizabeth in LYRA. [Observed S1; S2] [Official S6, S7]

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Calli and Ina** (26 / 26 / 8 / 15 / 8 / 9; 2 in 2026): Ina designed Calli's Death Sensei and drew the cover of Calli's debut EP; Calli wrote the lyrics of Ina's 2026 song "TAKO∞TAKOVER." Calli is a recurring target of Ina's puns. They watched Suisei's concert together in an off-collab (2023-02-20) and still game together (Elden Ring Nightreign, 2025-06). [Observed S5 Ina §Miscellaneous; Calli file C28; Ina file I8; S1]

### from holoX
- `bible/world/holoX.md › With the other Japanese members on the cards`: - AZKi: "Kanaken" with Chloe and Amane Kanata; "AzuIro" (Iroha), "KoZMy" (Koyori and Lamy); AZKi danced to La+'s, Koyori's and Lui's songs (2026). Suisei: Hoshimatic Project with Koyori, Chloe and Iroha. Okayu: "Dorobo Kensetsu" with La+ and Lui; La+'s lie-detector 3D challenge to Okayu (2026-05-19). Ayame: VALORANT with La+ (2024); "#みっころおにかん" games with Lui (2025). Botan: NePoX; "InuTakaShishiRam" with Lui, Korone and Watame (Minecraft, 2023). Marine: Bara☆Dice with Lui and Iroha (Bandai credits); UMISEA with Chloe. Lamy: KoZMy with Koyori. [S3] [S1]

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-02/10 PDT | Advent 3D debuts (JST dates one day later): Shiori (08-02), Bijou (08-03), Nerissa (08-09), FUWAMOCO (08-10, with Okayu and Korone cameos) | genmates as guests |

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2018-08 / 09 | 2nd generation (Aqua, Shion, Ayame, Choco, Subaru); Sakura Miko debuts (2018-08-01) | Earlier-debuting hololive members |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2018-12 | hololive GAMERS (Fubuki, Mio; later Okayu, Korone) | Gaming senpai |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2018-11-15 | AZKi debuts under COVER's management | — |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019-05-19 | AZKi and Hoshimachi Suisei (formerly independent) join under the INoNaKa Music label; Suisei moves to hololive's main branch on 2019-12-01 | Calli's collaborator Hoshimachi Suisei |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019 | 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins | Kiara's oshi Pekora; Nerissa's oshi Marine; Calli's collaborator Hoshimachi Suisei |

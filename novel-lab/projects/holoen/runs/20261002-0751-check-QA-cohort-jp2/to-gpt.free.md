# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: jp2
Packet: projects/holoen/research/qa/packets/jp2.md (owned material) and projects/holoen/research/qa/packets/jp2-incoming.md (incoming claims); both are inline below
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
| AUDIT-BRIDGE-TIES-EXTERNAL | Bridge audit of ties with external participants (rosters, credits, Groups, quotations, packet coverage) | applied in full; the TakaMori finale bullet paraphrased under MYTH-QUOTE-001; the generator now recovers each card owner in her own relationship rows | 2026-10-04 merge |

### Registry excerpt (this cohort's cast and world records and its units; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "e8bdd89",
 "cast": [
  {
   "name": "Houshou Marine",
   "file": "bible/characters/Houshou-Marine.md",
   "other_names": [
    "Marine",
    "Senchō",
    "Senchou",
    "Sencho",
    "Maririn",
    "宝鐘マリン"
   ],
   "groups": [
    "hololive",
    "hololive 3rd generation",
    "hololive Fantasy",
    "UMISEA",
    "holoWitches",
    "Bara☆Dice",
    "Yakamashi Musume",
    "Blue Journey",
    "MVP"
   ],
   "status": "Marine is an active member of hololive's 3rd generation. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2019-08-11",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Houshou-Marine.md › Background (debut: Background)"
   }
  },
  {
   "name": "Kikirara Vivi",
   "file": "bible/characters/Kikirara-Vivi.md",
   "other_names": [
    "Vivi",
    "綺々羅々ヴィヴィ"
   ],
   "groups": [
    "hololive",
    "FLOW GLOW",
    "MVP"
   ],
   "status": "Vivi is an active member of FLOW GLOW. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2024-11-09",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Kikirara-Vivi.md › Background (debut: Background)"
   }
  },
  {
   "name": "Shirogane Noel",
   "file": "bible/characters/Shirogane-Noel.md",
   "other_names": [
    "Noel",
    "Danchou",
    "Danchō",
    "Noel-danchou",
    "Noel Deluxe",
    "白銀ノエル"
   ],
   "groups": [
    "hololive",
    "hololive 3rd generation",
    "hololive Fantasy",
    "NoeFure",
    "Bara☆Dice",
    "Shiranui Kensetsu",
    "Yakamashi Musume",
    "Blue Journey"
   ],
   "status": "Noel is an active member of hololive's 3rd generation. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2019-08-08",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Shirogane-Noel.md › Background (debut: Background)"
   }
  },
  {
   "name": "Shishiro Botan",
   "file": "bible/characters/Shishiro-Botan.md",
   "other_names": [
    "Botan",
    "Shishiron",
    "Shishiro",
    "獅白ぼたん"
   ],
   "groups": [
    "hololive",
    "hololive 5th generation",
    "NePoLaBo",
    "holoFive",
    "NePoX",
    "InuTakaShishiRam",
    "Usada Kensetsu",
    "SubaChocoLunaTan"
   ],
   "status": "Botan is an active member of hololive's 5th generation. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2020-08-14",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Shishiro-Botan.md › Background (debut: Background)"
   }
  },
  {
   "name": "Yukihana Lamy",
   "file": "bible/characters/Yukihana-Lamy.md",
   "other_names": [
    "Lamy",
    "Lamy-mama",
    "Wamy",
    "雪花ラミィ"
   ],
   "groups": [
    "hololive",
    "hololive 5th generation",
    "NePoLaBo",
    "KALAZ",
    "KoZMy",
    "Yakamashi Musume",
    "holoWitches",
    "NePoX",
    "Blue Journey"
   ],
   "status": "Lamy is an active member of hololive's 5th generation. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2020-08-12",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Yukihana-Lamy.md › Background (debut: Background)"
   }
  }
 ],
 "world": [
  {
   "name": "JP Senpai Pairs 2",
   "file": "bible/world/JP-Senpai-Pairs-2.md",
   "role": "Relationship",
   "other_names": [
    "Marine and Kiara",
    "Noel and Calliope",
    "Lamy and Ina",
    "Botan and IRyS",
    "Vivi and FUWAMOCO"
   ]
  }
 ],
 "units": []
}
```

### projects/holoen/research/qa/packets/jp2.md

# Audit packet: jp2

Snapshot: git e8bdd89. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Houshou-Marine.md` 363cad47c8c7; `bible/characters/Shirogane-Noel.md` 383c370fae8f; `bible/characters/Yukihana-Lamy.md` bd7bdb48bd86; `bible/characters/Shishiro-Botan.md` 40c78f4b1201; `bible/characters/Kikirara-Vivi.md` e3dae5035b02; `bible/world/JP-Senpai-Pairs-2.md` aeeee4dd9074

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Houshou Marine — `bible/characters/Houshou-Marine.md`
**[SW] Groups:** hololive, hololive 3rd generation, hololive Fantasy, UMISEA, holoWitches, Bara☆Dice, Yakamashi Musume, Blue Journey, MVP
**[SW] Other Names:** Marine, Senchō, Senchou, Sencho, Maririn, 宝鐘マリン
**[SW] Background:** Marine is an active member of hololive's 3rd generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2019-08-11 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Shirogane Noel; secondary reporting records 3 million subscribers in 2024 and 4 million in 2025. She released the album "Ahoy!! You're All Pirates♡!" (2024), held a solo concert (2024), performed in hololive Fantasy's "#OperationHeartfulCuties" concert (2026), released "Chatter Chatter" with Suisei (2026) and the single "Kyapi" (2026). Archived metadata records her with the English cast as Kiara's first HOLOTALK guest (2020), on Calli's first English lesson (2022), at an off-collab house party with Calli and Bae (2023), in off-collabs with FUWAMOCO and Nerissa (2024) and as a guest at Ina's "Pleides" (2024); she features in the horror game "Truth of Beauty Witch," which Calli, and Bae with Mumei, played, and she sang for Elizabeth's 2026 birthday.
**[SW] Relationships:** Usada Pekora: hololive Fantasy genmate ("PekoMari," a secondary pair name); in 2026 Pekora coached her at Mario Tennis ("Pekoach"). Shirogane Noel: hololive Fantasy genmate; Bara☆Dice with Takane Lui, Shiranui Flare, Momosuzu Nene and Kazama Iroha; separately, Yakamashi Musume with Yukihana Lamy and Inugami Korone. Hoshimachi Suisei: "Chatter Chatter" (2026). Kikirara Vivi: the unit MVP with Pekora (an archived 2026 performance record). Yukihana Lamy: Yakamashi Musume, holoWitches and Blue Journey. Hakui Koyori: "#頭ピンク組," the pink-haired pair of their archived titles (a race and a talk testing whether they are alike, 2025); Blue Journey. La+ Darknesss: a sponsored collab billed #マリラプ and a cover with Koyori (2025). Takane Lui and Kazama Iroha: Bara☆Dice. Sakamata Chloe (affiliate): UMISEA and holoWitches. Nekomata Okayu: Marine gave her the nickname "Okanyan" (Okayu's official profile). Takanashi Kiara: her first HOLOTALK guest (2020) and dance shorts ("MIRAGE," "III," 2024). Mori Calliope: Calli's English lesson #01 (2022), Mario Kart (2021) and a house-party off-collab with Bae (2023). Hakos Baelz: that Mario Kart and house party; Bae and Mumei played the horror game featuring Marine (2023). Ninomae Ina'nis and Gawr Gura (graduated): UMISEA; English lesson #01 with Ina and a guest spot at Ina's "Pleides" (2024); "SHINKIRO" with Gura (2023). FUWAMOCO: a Touhou off-collab and Mario Party Superstars with Nerissa (2024). Nerissa Ravencroft: that Mario Party off-collab. Elizabeth Rose Bloodflame: "IT'S LOVE" with Korone for Elizabeth's 2026 birthday. Nakiri Ayame: a second-generation senior. AZKi: commentary for her Holo Koshien stream (2026).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2019-08-11 | Debut, hololive 3rd generation (hololive Fantasy) | [Official MA1] |
| 2020-11-20 | First guest on Kiara's "HOLOTALK" | [MA5 3HwaqbdKO1s] |
| 2022-02-19 | Calli's HOLO ENGLISH LESSON #01 with Ina and Fubuki | [MA5 bfUEbp3xk4o] |
| 2023-08 | The horror game "Truth of Beauty Witch -Marine's treasure ship-" features her (Calli played it 08-14; Bae with Mumei 08-23); an off-collab house party with Calli and Bae (08-14) | [Observed MA2 §Events] [MA5 Mf-sAjsuSig, RY1GkF4jMls, DY5VThfehW8] |
| 2024 | 3 million subscribers (01-10, secondary); album "Ahoy!! You're All Pirates♡!" (10-16); a Touhou off-collab with FUWAMOCO (04-30) and Mario Party with FUWAMOCO and Nerissa; a solo concert (12); a guest at Ina's "Pleides" (12-28) | [Observed MA2] [MA5 x7gRHgQ0yI0, FLL7e1-RPGo, 3n9igJnSXtQ] |
| 2025-05-05 | 4 million subscribers (secondary reporting; the official shop's 4-million merchandise confirms the milestone, not the date) | [Observed MA2 §2025] |
| 2026-01-17/18 | hololive Fantasy concert "#OperationHeartfulCuties," K-Arena Yokohama | [Observed MA2 §2025–2026] [Official announcement] |
| 2026-02-28 | "Chatter Chatter" with Hoshimachi Suisei: anime MV (official digital release 2026-03-01) | [MA4 di9NZ6ja_mE] [Official music 711] |
| 2026-03-10 | Mario Tennis with Pekora as her coach ("Pekoach") | [MA4 GWZrQZ6leZI] |
| 2026-08 | 7th anniversary and a new 3D costume (08-11); single "Kyapi" (08-12) | [Observed MA2 §2026, §Discography] |
| 2026-09 | Holo Koshien series: a baseball team followed through successive in-game seasons; Koyori joined the 09-17 session and AZKi commentated on 09-26. | [Archive metadata NEW-R5-014, NEW-R5-006] |
**Dossier · Hard Facts (continuity):**
- Debut 2019-08-11; hololive 3rd generation (hololive Fantasy); birthday 30 July; 150 cm; illustrator Akasa Ai;
  fans Houshou no Ichimi; mascot Kumarine; stream tag #マリン航海記; fan-art tag #マリンのお宝.

### Shirogane Noel — `bible/characters/Shirogane-Noel.md`
**[SW] Groups:** hololive, hololive 3rd generation, hololive Fantasy, NoeFure, Bara☆Dice, Shiranui Kensetsu, Yakamashi Musume, Blue Journey
**[SW] Other Names:** Noel, Danchou, Danchō, Noel-danchou, Noel Deluxe, 白銀ノエル
**[SW] Background:** Noel is an active member of hololive's 3rd generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2019-08-08 in hololive's 3rd generation, the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Houshou Marine. She released the originals "Lyrical Monster" and "Ours" (2022), her first album "NOESANPO" (2023), "TREVIAN KNIGHT" (2025) and "KAGAMI YO KAGAMI" (2026), and sang at hololive Fantasy's "#OperationHeartfulCuties" concert (2026). Archived metadata records her with the English cast as Kiara's 22nd HOLOTALK guest (2022), a guest with Flare on Calli's HOLOYOI #02 (2023), a participant with FUWAMOCO and Bae in a team Mario Kart event (2023) and in Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (2025); FUWAMOCO danced to "TREVIAN KNIGHT."
**[SW] Relationships:** Houshou Marine: hololive Fantasy genmate; Bara☆Dice with Takane Lui, Shiranui Flare, Momosuzu Nene and Kazama Iroha; separately, Yakamashi Musume with Yukihana Lamy and Inugami Korone; 3rd-gen R.E.P.O. (2025). Shiranui Flare: hololive Fantasy genmate ("NoeFure," a label from Noel's own stream titles); any mock jealousy is on-stream comedy. Yukihana Lamy: Yakamashi Musume and drinking-talk collabs. Hoshimachi Suisei: "Shiranui Kensetsu" (Shiraken), the Minecraft construction company with Flare, Omaru Polka and Sakura Miko. Nakiri Ayame: an Audio-Technica sponsorship collab (2025). Hakui Koyori: "#ノエこよ," a Power Pros baseball exhibition (2025), and Blue Journey (2023). Takane Lui and Kazama Iroha: Bara☆Dice. Kikirara Vivi: Gartic Phone (2025). Takanashi Kiara: her 22nd HOLOTALK guest (2022). Mori Calliope: HOLOYOI #02 with Flare (2023). FUWAMOCO and Hakos Baelz: a team Mario Kart event (2023); FUWAMOCO danced to "TREVIAN KNIGHT" (2025). Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone EN + ID + JP (2025). AZKi and Nekomata Okayu: fellow players in AZKi's 3D pun-ASMR contest (2025).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2019-08-08 | Debut, hololive 3rd generation (hololive Fantasy) | [Official NO1] |
| 2022 | Originals "Lyrical Monster" and "Ours"; Kiara's 22nd HOLOTALK guest (03-05) | [Observed NO2] [NO5] |
| 2023 | Calli's HOLOYOI #02 with Flare (04-20); first solo album "NOESANPO" (official digital release 11-25; birthday merchandise orders opened 11-24); a "Yuru Holo" team Mario Kart event with FUWAMOCO and Bae among the participants (12-12) | [NO5] [Official music 359] |
| 2025 | #ノエこよ Power Pros exhibition with Koyori (01-10); Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (04-14); 3rd-gen R.E.P.O. with Marine, Pekora and Flare (07-05); Elden Ring Nightreign with Flare and Pekora; an Audio-Technica collab with Ayame (07-11); "TREVIAN KNIGHT" (official digital release 08-16), which FUWAMOCO danced to (09-30) | [NO4] [NO5] [Official music 622] |
| 2026-01-17/18 | hololive Fantasy concert "#OperationHeartfulCuties," K-Arena Yokohama | [Observed NO2] [Official announcement] |
| 2026-08 | Original song "KAGAMI YO KAGAMI" (official digital release 08-16) | [Official music 796] |
| 2026-08-27 | Holo Koshien: she ran "Shirogane Gakuin," opening with player creation and naming and following the team through its seasons into September. | [Archive metadata NEW-R5-015] |
**Dossier · Hard Facts (continuity):**
- Debut 2019-08-08; hololive 3rd generation (hololive Fantasy); birthday 24 November; 158 cm; illustrator Watao;
  fans Knight's Order of Shirogane (Shirogane kishidan); stream tag #ノエルーム; fan-art tag #ノエラート.

### Yukihana Lamy — `bible/characters/Yukihana-Lamy.md`
**[SW] Groups:** hololive, hololive 5th generation, NePoLaBo, KALAZ, KoZMy, Yakamashi Musume, holoWitches, NePoX, Blue Journey
**[SW] Other Names:** Lamy, Lamy-mama, Wamy, 雪花ラミィ
**[SW] Background:** Lamy is an active member of hololive's 5th generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2020-08-12 in hololive's 5th generation with Shishiro Botan, Omaru Polka and Momosuzu Nene (with whom she forms NePoLaBo). She sang in the "Blue Journey" project with Marine, Noel, Koyori and Sakura Miko (2023), joined "Magical Girl holoWitches!" (2025), formed KoZMy with AZKi and Koyori (2025, per a collab title and secondary listings) and, per secondary records, is in KALAZ with Amane Kanata and AZKi. Her originals include "Hatsukoi Pâtissière" (2024), "Yoppara Music !" (2025) and "Snowlight Stories" (2026), and her first album, "Fleur de neige," was announced for January 2027. Archived metadata records her with the English cast at the Usaken Summer Festival in Minecraft with Ina and a Minecraft collab billed as a "date" (2021), and as a guest at Ina's 3D live "Pleides" (2024).
**[SW] Relationships:** Shishiro Botan: 5th-gen genmate and NePoLaBo partner; secondary accounts describe horror runs where Lamy is scared and Botan stays calm. Momosuzu Nene and Omaru Polka: 5th-gen genmates and NePoLaBo (a 3D party, 2026); "Magamaga's" with Nene (secondary). AZKi: her KoZMy cover partner with Hakui Koyori on "Ai♡Scream!" (2025); also "KALAZ" with Amane Kanata (secondary). Hakui Koyori: KoZMy (2025) and a March 2026 off-collab titled to name their duo. Houshou Marine and Shirogane Noel: "Yakamashi Musume" with Inugami Korone (archived metadata), and Blue Journey; Marine is also in holoWitches. La+ Darknesss, Takane Lui, Kazama Iroha and Hakui Koyori: NePoX, the 2026 NePoLaBo × holoX events. Ninomae Ina'nis: a Minecraft festival and a Minecraft collab billed as a "date" (2021), and a guest at Ina's 3D live "Pleides" (2024). Sakamata Chloe (affiliate): Rust with Amane Kanata (2022). Nekomata Okayu: a "Lukewarm" duet cover (2024). Gawr Gura, Watson Amelia and Mori Calliope: co-players in the Myth × fifth-generation Among Us collab (2020).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2020-08-12 | Debut, hololive 5th generation | [Official LM1] |
| 2021 | Usaken Summer Festival with Ina (06-27) and an EN-server Minecraft "date" with Ina (10-20) | [LM5] |
| 2023 | "Blue Journey" music project with Marine, Noel, Koyori and Sakura Miko | [Koyori file; Observed LM2] |
| 2024 | Originals "Hatsukoi Pâtissière," "Watashi wo amayakasunara" and "Lamy's Baribari Workout"; a guest at Ina's 3D live "Pleides" (12-28) | [Observed LM2] [LM5] |
| 2025 | Joins "Magical Girl holoWitches!" (04–05); "Yoppara Music!" (official digital release 08-13); a "KoZMy 結成⁉" collab with AZKi and Koyori (08-03; secondary listings give its first anniversary in 2026-08) | [Observed LM2] [Official music 609] [Koyori file lvgC3pW-LVA] |
| 2026 | Her collaboration sake "Yukiyozuki" with Meiri Shurui (04); an off-collab with Koyori titled to name their duo (03); a NePoLaBo 3D party (04-29); NePoX took place at Ariake Arena on 2026-09-26/27 with Nene, Polka, Lamy, Botan, La+, Lui, Koyori and Iroha: NePoLaBo-versus-holoX games ending Day 1 with all eight in a giant-robot red-light/green-light challenge, and the collaboration song "Watcha Gatcha!!!!!!!!" introduced [Secondary NEW-R5-020, organizer report]; "Snowlight Stories" (official digital release 08-13) | [LM4 Zi8R63ee0Fs, Ekdsnb2aWY4, Ml1tM8S40p0] [Official NePoX page] [Official music 792] [Brewery page] |
| 2026-08-15 | First album "Fleur de neige" announced for 2027-01-27 (after the baseline) | [Observed LM2] |
**Dossier · Hard Facts (continuity):**
- Debut 2020-08-12; hololive 5th generation; birthday 15 November; 158 cm; illustrator Rin☆Yuu; fans Yukimin
  (Snowfolk); companion Daifuku (a snow spirit); stream tag #らみらいぶ; fan-art tag #らみあーと.

### Shishiro Botan — `bible/characters/Shishiro-Botan.md`
**[SW] Groups:** hololive, hololive 5th generation, NePoLaBo, holoFive, NePoX, InuTakaShishiRam, Usada Kensetsu, SubaChocoLunaTan
**[SW] Other Names:** Botan, Shishiron, Shishiro, 獅白ぼたん
**[SW] Background:** Botan is an active member of hololive's 5th generation. She has no supernatural abilities; her lore is a performed persona. She debuted on 2020-08-14 as a fifth-generation member; she forms NePoLaBo with Yukihana Lamy, Omaru Polka and Momosuzu Nene. Secondary records place her 1.5-million-subscriber milestone in February 2025. She has released originals such as "Simulacre," "Gaotteko!" and "Tokihanate"; her first album, "BOTAN.EXE," opened for orders on 2026-09-19. She ran the hololive Minecraft money-making event twice (2025, 2026) as its game master and hosted the "Shishiro Cup." Archived metadata and secondary concert reports record her with the English cast in Left 4 Dead 2 (2022) and an Overwatch 2 team (2023) with IRyS, on Calli's HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and as a guest at Ina's birthday 3D live "EVERMORE" (2025); Kiara is a fellow member of the Minecraft "Usada Kensetsu" (secondary).
**[SW] Relationships:** Yukihana Lamy: 5th-gen genmate and NePoLaBo partner; secondary accounts describe horror "dates" where Botan stays calm and teases Lamy. Momosuzu Nene and Omaru Polka: 5th-gen genmates and NePoLaBo. Takane Lui: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary); Left 4 Dead 2 (2022) and Overwatch 2 (2023) together. La+ Darknesss, Hakui Koyori and Kazama Iroha: NePoX (NePoLaBo × holoX, 2026). La+ Darknesss and Hoshimachi Suisei: holoGTA and, with Shirakami Fubuki, the m HOLD'EM poker collaboration (2024); Nakiri Ayame: holoGTA (2024). IRyS: Left 4 Dead 2 with Lui and Korone (2022) and an Overwatch 2 team with Lui, Sakamata Chloe and Tokoyami Towa (2023). Takanashi Kiara: a fellow member of the Minecraft "Usada Kensetsu" (secondary) and an Among Us co-player in the Myth × fifth-generation collab (2020), with Watson Amelia. Gawr Gura (graduated): "Apex Predators," a secondary-listed pair label. Mori Calliope: HOLOYOI #03 with Oozora Subaru (2023). Hakos Baelz: BAE-GEMITE DOMINATION #2 with Subaru (2023). Ninomae Ina'nis: a guest at Ina's birthday 3D live "EVERMORE" (2025), singing "storia" with Ina and Watame per a secondary set list. Nerissa Ravencroft: a guest at her birthday 3D live "Stray&Stay" (2026).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2020-08-14 | Debut as a hololive 5th-generation member; her debut intro video was her own edit (secondary) | [Official BO1] [Observed BO2] |
| 2022-04-24 | Left 4 Dead 2 with IRyS, Takane Lui and Inugami Korone | [BO5 K1wStJxm4F0] |
| 2023 | BAE-GEMITE DOMINATION #2 with Bae and Subaru (04-08); HOLOYOI #03 with Calli and Subaru (05-18); an Overwatch 2 team with IRyS, Lui, Chloe and Towa (08) | [BO5] |
| 2024-04-01 | A "furball lion" model designed by Shirakami Fubuki | [Observed BO2] |
| 2025 | 1.5 million subscribers (02-14, secondary); originals "Simulacre," "Gaotteko!" and "boundary"; a guest at Ina's birthday 3D live "EVERMORE" (05-21), singing "storia" with Ina and Tsunomaki Watame per a secondary set list; the first "#ホロ金策サバイバル" | [Observed BO2] [BO5] [EVERMORE report] [ASR BO20] |
| 2026-04 | The "Shishiro Cup" fighting-game tournament, offline; original "Tokihanate" (04-10) | [BO4] [Observed BO2] |
| 2026-06-01/05 | "#ホロ金策サバイバル2," with Botan as game master | [BO4] [ASR BO20] |
| 2026-08-26 | NePoLaBo and Secret Society holoX release their joint original "Watcha Gatcha!!!!!!!!" | [Official NEW-R6-004] |
| 2026-09-14 | She organized and hosted the ShishiDori Cup, a hololive Dreams competition with 27 participants in nine teams, combining rhythm-game and chase-game challenges. | [Archive metadata NEW-R6-001] |
| 2026-09-19 | First album "BOTAN.EXE" opened for orders; original "Stray & Stay" | [Observed BO2] [Distributor listing] |
| 2026-09-26/27 | NePoX events with Secret Society holoX | [LM4 Ml1tM8S40p0] |
**Dossier · Hard Facts (continuity):**
- Debut 2020-08-14; hololive 5th generation; birthday 8 September; 166 cm; illustrator tomari; fans SSRB (first
  "Bodan"); stream tag #ぐうたらいぶ; fan-art tag #ししらーと.

### Kikirara Vivi — `bible/characters/Kikirara-Vivi.md`
**[SW] Groups:** hololive, FLOW GLOW, MVP
**[SW] Other Names:** Vivi, 綺々羅々ヴィヴィ
**[SW] Background:** Vivi is an active member of FLOW GLOW. She has no supernatural abilities; her lore is a performed persona. She debuted on 2024-11-09 through hololive DEV_IS as a member of FLOW GLOW, with Isaki Riona, Koganei Niko, Mizumiya Su and Rindo Chihaya. FLOW GLOW released its self-titled album on 2026-01-21 and the single "magic summer" later in 2026. Secondary records date her 700,000-subscriber milestone to an endurance karaoke stream on 2026-08-11 and identify "Vivid Cute" as her first solo original, available digitally on 2026-08-28. She plays games with Usada Pekora ("PekoVivi," secondary), and an archived 2026 performance record names Marine, Vivi and Pekora as MVP. Archived metadata records her with the English cast in R.E.P.O. with FUWAMOCO and Bae (2025-05-25), in a separate R.E.P.O. session on Ina's stream (2025-06-02) and in Mumei's Gartic Phone collaboration with Noel, Kronii, Ina and Elizabeth (2025); a secondary archive records FUWAMOCO and Bijou watching FLOW GLOW's debut.
**[SW] Relationships:** Usada Pekora: "PekoVivi" (a secondary pair name); co-op games (2025) and a gifted Getting Over It (2026); secondary accounts say Pekora rescued her in Minecraft and Vivi calls her the "legendary hero." Houshou Marine: MVP with Pekora (an archived 2026 performance record). Shirogane Noel: Mumei's Gartic Phone collab (2025). FLOW GLOW (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya): her unit; a "Bridal Dream" cover with Chihaya (2025). FUWAMOCO: watched FLOW GLOW's debut with Bijou (2024, secondary archive); R.E.P.O. with Bae (2025-05-25). Hakos Baelz: that R.E.P.O. session. Ninomae Ina'nis: a separate R.E.P.O. session on Ina's stream (2025-06-02) and the Gartic Phone collab. Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone (2025). Nanashi Mumei (graduated): hosted that Gartic Phone collab. Koseki Bijou: watched FLOW GLOW's debut with FUWAMOCO. AZKi: GeoGuessr (2026). Hoshimachi Suisei: taught her Tetris on Vivi's channel (2026). Nekomata Okayu: a 2026 collab billed with a mock-scandalized "やーらし."
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2024-11-09 | Debut with FLOW GLOW, through hololive DEV_IS; first cover "Luna say maybe" | [Official VI1] [Observed VI2] |
| 2025 | FLOW GLOW songs "24K GOLD" (03-14), "LOAD" (07-09), "good enough" (09-20); 500,000 subscribers (11-30, secondary) | [Observed VI2] |
| 2025-04-14 | Gartic Phone EN + ID + JP collab with Mumei, Kronii, Ina, Elizabeth and Noel | [VI5 OMDzBQohAf8] |
| 2025-05-25 | #holoREPO with FUWAMOCO, Bae, Roboco, Towa and Hajime | [VI5 Z5cpzbdsLDE, TgMVtjXW2Ms] |
| 2025-06-02 | R.E.P.O. on Ina's stream, with Polka, Watame, Flare and Anya | [VI5 grBU9Dl09Ds description] |
| 2025-07 | Games with Pekora (The Forest, Fast Food Simulator); "Bridal Dream" cover with Chihaya (07-28) | [VI4 lqidVnpl3_0, FWCkuwroMIw, NGeumGspO2g] |
| 2026 | FLOW GLOW's self-titled album (01-21, including "PUNISHER" and "the light"); first on-stream Super Mario Bros. 3 and Super Mario World playthroughs; Getting Over It, a gift from Pekora (07-25); 700,000 subscribers during an endurance karaoke (08-11, secondary); FLOW GLOW's "magic summer" (08-18); MVP's "Hatsukoi Cider" with Marine and Pekora (09, secondary record) | [Official music 024] [VI4] [Observed VI2] [MVP upload record] |
| 2026-08 | First solo original song, "Vivid Cute" (premiered around her birthday, 08-27; available digitally 08-28) | [Official music 808] [Observed VI2] |
**Dossier · Hard Facts (continuity):**
- Debut 2024-11-09 through hololive DEV_IS; FLOW GLOW (makeup artist); birthday 27 August; 161 cm; illustrator nonco;
  fans Vivid; emoji 💅✨.

### JP Senpai Pairs 2 — `bible/world/JP-Senpai-Pairs-2.md`
**[SW] Other Names:** Marine and Kiara, Noel and Calliope, Lamy and Ina, Botan and IRyS, Vivi and FUWAMOCO
**[SW] Description:** The public ties of five more hololive members, Houshou Marine, Shirogane Noel, Yukihana Lamy, Shishiro Botan and Kikirara Vivi, with the English cast and with each other. Archived channel metadata records the following. Marine was the first guest of Kiara's talk show HOLOTALK (2020), joined Calli's first English lesson with Ina (2022), played Mario Kart with Calli and Bae (2021) and joined their house-party off-collab (2023), joined off-collabs with FUWAMOCO and Nerissa (2024), and was a guest at Ina's 3D live "Pleides" (2024); Calli, and Bae with Mumei, played "Truth of Beauty Witch," a horror game featuring Marine (2023); Marine, Ina and Gura were in the ocean unit UMISEA. Noel was HOLOTALK's 22nd guest in 2022. She appeared with Shiranui Flare on Calli's HOLOYOI #02 in 2023. Lamy joined the Usaken Summer Festival in Minecraft with Ina and a "date"-billed Minecraft stream (2021) and her 3D live (2024). Botan played Left 4 Dead 2 and Overwatch 2 with IRyS, was on HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and guested at Ina's 2025 birthday live. Vivi, a FLOW GLOW member, played R.E.P.O. with FUWAMOCO and Bae and, separately, on Ina's stream, and Gartic Phone with Mumei, Kronii, Ina and Elizabeth (2025). Among themselves: Marine and Noel are hololive Fantasy; Marine, Noel and Lamy are "Yakamashi Musume" with Inugami Korone; Lamy and Botan are NePoLaBo; Marine, Vivi and Pekora are "MVP."
**[SW] Rules:** These entries record public collaborations. Seniority depends on the pairing: Marine, Noel, Lamy and Botan are senpai to the English cast, while Vivi is a kouhai to the EN members listed here. The five stream mostly in Japanese; language use varies by collaboration. Gura and Mumei appear only as memories; Ame is an affiliate. A collab title shows that a collab happened, not how close two members are; a playthrough of a game featuring a member is not a collab with her.
**Dossier · History:**
| Date | Event | Who |
|---|---|---|
| 2020-11-20 | Marine is HOLOTALK's first guest | Marine, Kiara |
| 2021 | the Usaken Summer Festival in Minecraft with Ina and EN-server "date" | Lamy, Ina |
| 2022 | Calli's English lesson #01; HOLOTALK #22; Left 4 Dead 2 | Marine; Noel; Botan, IRyS |
| 2023 | HOLOYOI #02 and #03; BAE-GEMITE DOMINATION #2; the horror game featuring Marine; Overwatch 2 team; Blue Journey | Noel, Botan, Calli, Bae; Calli, Bae, Mumei; Botan, IRyS |
| 2024 | Off-collabs with FUWAMOCO and Nerissa; Ina's "Pleides" | Marine; Lamy, Marine |
| 2025 | Gartic Phone EN + ID + JP (04-14); #holoREPO (05-25); R.E.P.O. on Ina's stream (06-02); Ina's "EVERMORE" | Noel, Vivi; Vivi, Bae, FUWAMOCO; Vivi, Ina; Botan |
| 2026 | "Chatter Chatter"; Elizabeth's birthday cover | Marine, Suisei; Marine |
**Dossier · Hard Facts (continuity):**
- Marine: HOLOTALK guest #1 (2020-11-20). Noel: HOLOTALK guest #22 (2022-03-05).
- Calli's HOLOYOI: #02 Noel and Flare (2023-04-20); #03 Subaru and Botan (2023-05-18).

Incoming claims continue in `jp2-incoming.md`.

### projects/holoen/research/qa/packets/jp2-incoming.md

# Audit packet: jp2 (incoming claims)

Snapshot: git e8bdd89.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names:  Senpai Pairs 2|Noel and Calliope|Vivi and FUWAMOCO|Marine and Kiara|Houshou Marine|Shishiro Botan|Botan and IRyS|Shirogane Noel|Yukihana Lamy|Kikirara Vivi|Lamy and Ina|Noel-danchou|Noel Deluxe|Lamy-mama|Shishiron|Shishiro|綺々羅々ヴィヴィ|Maririn|Senchou|Danchou|Danchō|Marine|Senchō|Sencho|獅白ぼたん|雪花ラミィ|Botan|宝鐘マリン|白銀ノエル|Noel|Vivi|Lamy|Wamy)(

### from AZKi
- `bible/characters/AZKi.md › [SW] Relationships`: Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!"
- `bible/characters/AZKi.md › [SW] Relationships`: (2025), and a 3D karaoke with Koyori, Isaki Riona and Koganei Niko (2026); Lamy is also in "KALAZ" with Amane Kanata (secondary).
- `bible/characters/AZKi.md › [SW] Relationships`: Nekomata Okayu: Mario Kart World practice for Team Wind (2026-01-16) and AZKi's pun-ASMR contest (2025), with Shirogane Noel also playing.
- `bible/characters/AZKi.md › [SW] Relationships`: Houshou Marine: AZKi supplied soothing commentary for Marine's Holo Koshien stream (2026).
- `bible/characters/AZKi.md › [SW] Relationships`: Kikirara Vivi: GeoGuessr on Vivi's channel (2026).
- `bible/characters/AZKi.md › Behavioral Traits`: - **Pun-ASMR host (2025-06-22):** she hosted a 3D pun-ASMR contest with Okayu, Noel, Oozora Subaru and Otonose Kanade; laughing meant losing. The title establishes the format and players, not particular jokes or the winner. [Archive metadata NEW-R5-004]
- `bible/characters/AZKi.md › Relationship Map`: | Shirogane Noel | JP senior | A player in AZKi's 3D pun-ASMR contest (2025-06-22). | [Archive metadata NEW-R5-004] |
- `bible/characters/AZKi.md › Relationship Map`: | Houshou Marine | JP senior | AZKi supplied commentary for Marine's Holo Koshien stream; the title billed it as soothing (2026-09-26). | [Archive metadata NEW-R5-006] |
- `bible/characters/AZKi.md › Relationship Map`: | Hakui Koyori, Yukihana Lamy | "KoZMy" (secondary references; a 2025-08-03 "KoZMy 結成⁉" collab title) | A 3D karaoke with Koyori, Isaki Riona and Koganei Niko (2026-02-03, not a KoZMy event); Lamy is also in "KALAZ" with Amane Kanata (secondary) Lamy: an impromptu group chat with Lamy and Inugami Korone on Lamy's channel (#あずらみころ, 2026-09-18). | [Koyori file KO4 lvgC3pW-LVA, 1HQL3WJPBHA] [Lamy file LM2] [Archive metadata NEW-R5-005] |
- `bible/characters/AZKi.md › Relationship Map`: | Kikirara Vivi | — | A GeoGuessr collab on Vivi's channel (2026-08-22). | [Archive metadata, holostats dzO2LaVBmMY] |

### from Ceres Fauna
- `bible/characters/Ceres-Fauna.md › Voice Profile`: - Self-description: "I'm pretty soft-spoken. And talking in my head voice like this does not strain my voice at all." [ASR F20, 1:14:21]. Secondary: soft-spoken and comforting, with a voice tone fans compare with Yukihana Lamy's. [Observed F2 §Personality, secondary]
- `bible/characters/Ceres-Fauna.md › Relationship Map`: | Shirogane Noel | JP senior | Wiki trivia says Fauna admired her and wanted to collab (secondary; not verified in review, no collab recorded) | [Observed F2 §Trivia, secondary] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Her April 25, 2026 birthday-live guests included FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine, Korone and Nerissa.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Shirogane Noel and Kikirara Vivi: Mumei's Gartic Phone EN + ID + JP collab (2025).
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | JP seniors | Birthday-cover partners (2026) | Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone | [Observed EB3] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Shirogane Noel, Kikirara Vivi | JP members | Mumei's Gartic Phone EN + ID + JP (2025-04-14) | [Shirogane Noel file NO5; Kikirara Vivi file VI5; archive metadata OMDzBQohAf8, inherited and not reopened] |

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Houshou Marine: her oshi (secondary); a Touhou off-collab (2024).
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Shirogane Noel: a team Mario Kart event (2023).
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Kikirara Vivi: #holoREPO (2025).
- `bible/characters/Fuwawa-Abyssgard.md › Core Drive`: - **Want:** with Mococo, to protect the Ruffians' smiles; their debut list held more than a hundred goals (sing with Houshou Marine, a solo concert, an anime song, a scale figure). [Official FW1, FW4] [Observed FW2 §Hopes and dreams, secondary]
- `bible/characters/Fuwawa-Abyssgard.md › Behavioral Traits`: 6. Her oshi is Houshou Marine; she loves visual novels, retro games, Japanese sweets and matcha. [Observed FW2 §Likes and dislikes, secondary]
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Houshou Marine | Her oshi (secondary) | A Touhou off-collab (2024-04-30, archived x7gRHgQ0yI0); Marine's solo concert watchalong (2024-12-07); a guest at their birthday concert (2025) | [Observed FW2; FW3] |
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Marine: a Touhou off-collab (2024-04-30), Mario Party with Nerissa (2024-06-17), a watch-along of her solo concert (2024-12-07), a "Chatter Chatter" dance short (2026); Noel: "Yuru Holo" team Mario Kart (2023-12-12) and a "Très Bien Night" dance short (2025); Vivi: FLOW GLOW's debut watch-along (2024) and #holoREPO (2025) | [S1 x7gRHgQ0yI0, FLL7e1-RPGo, zQdsLXE4ZQ8, PtaFGDOaj0k, Janl2FCKmsg, 8RjOCCH2sac, gAj77STI2oc, Z5cpzbdsLDE] |

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Background`: Her lore, which she played for laughs, is a persona, not literal: a descendant of the Lost City of Atlantis who swam to land because it was "so boring down there," bought her clothes and shark hat in the human world, and talks to marine life.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Houshou Marine: UMISEA and "SHINKIRO"
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Shishiro Botan: "Apex Predators," a secondary pair name.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Yukihana Lamy: the Myth × fifth-generation Among Us collab (2020).
- `bible/characters/Gawr-Gura.md › Background Timeline`: | Lore | Descendant of Atlantis (now ruins); swam to land because it was "so boring down there"; bought her clothes at a beachside store, paying in seashells; talks to marine life | [Official G1] [Observed G2 §Lore] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate; fellow member of the official unit UMISEA (2021, with Aqua and Marine; the wiki also lists Chloe) | Ina drew chibi Bloop and performed a protective mock-threat bit about Gura; co-op games The final Myth relay's Gang Beasts segment ran on Ina's channel (reported 2025-04-30). | [Observed G2 §Gura's antics and §Mascots and fans; G16] [Official G17] [Secondary NEW-R1-017] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | La+ Darknesss, Kazama Iroha, Shishiro Botan | JP members | HOLO ENGLISH LESSON #02 with La+ and Iroha (Calli's stream, 2022-03-04); "Apex Predators," a wiki-listed pair name with Botan | [S1 X492n37brRU] [Botan file, secondary] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Houshou Marine, Sakamata Chloe | UMISEA (official 2023 roster: Aqua, Marine, Chloe, Gura, Ina) | "SHINKIRO" with Marine (anime MV on Marine's channel, 2023-11-12, credited to both; the "GuraMarine" pair name is wiki-listed only) | [Marine file MA4 9ehwhQJ50gs] [Official UMISEA roster] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Yukihana Lamy | JP fifth generation | Co-players in Nene's Myth × fifth-generation Among Us collab (2020-10-24). | [Archive metadata TIE-034 to 038] |

### from Hakos Baelz
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Houshou Marine: Mario Kart (2021) and Calli's house party (2023); Bae and Mumei played "Truth of Beauty Witch," the horror game featuring Marine.
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Kikirara Vivi: #holoREPO (2025).
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Shirogane Noel: a team Mario Kart event with FUWAMOCO (2023).
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Shishiro Botan: BAE-GEMITE DOMINATION #2 with Oozora Subaru (2023).
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2026-09-28 | "PARADISE!", the hololive Dreams area theme: animated MV; Bae shares the vocal credit with Omaru Polka, Houshou Marine, Yukihana Lamy, Hakui Koyori, Kobo Kanaeru and Ichijou Ririka. Also announced that day: "REGALIA" at Kanadevia Hall, scheduled for 2026-12-01 (after the baseline: an announcement only). | [Secondary NEW-R2-019, press-release reproduction] [Official, 20260928-02-16] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Houshou Marine, Shirogane Noel, Shishiro Botan, Kikirara Vivi | JP members | Mario Kart with Marine, Calli and Reine (2021); Calli's house party with Marine (2023); Marine's horror game with Mumei (2023); BAE-GEMITE DOMINATION #2 with Botan and Subaru (2023-04-08); "Yuru Holo" team Mario Kart with Noel and FUWAMOCO (2023-12-12); #holoREPO with Vivi and FUWAMOCO (2025-05-25). Marine and Bae are co-credited vocalists on "PARADISE!" (MV 2026-09-28). | [HB3 X3pHIQAvpYU, RY1GkF4jMls, -0_9xCPljh0, Evg-T2BUIDM, TgMVtjXW2Ms] [Secondary NEW-R2-019] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Yukihana Lamy | JP senior | Co-credited singers on the hololive Dreams theme "PARADISE!" (MV 2026-09-28); a shared recording project, not a particular conversation. | [Secondary NEW-R2-019] |

### from Hakui Koyori
- `bible/characters/Hakui-Koyori.md › [SW] Background`: She sang in "Blue Journey" with Marine, Noel, Lamy, Botan, Lui and Sakura Miko (2023); secondary records place her in Suisei's Hoshimatic Project from 2023; archived 2025 collabs bill her, AZKi and Lamy as "KoZMy."
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: La+ Darknesss: holoX's founder; a sponsored "#stons" collab (2024) and a cover with Marine (2025).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: AZKi and Yukihana Lamy: "KoZMy"
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: (archived 2025 titles); a 3D karaoke with AZKi (2026); a #ラミこよ off-collab with Lamy (2026).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: Houshou Marine: archived titles bill them as the "pink-haired pair"; Blue Journey; Marine backseats her Pikachu game (2025).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: Shirogane Noel: Blue Journey and "NoeKoyo" baseball (2025).
- `bible/characters/Hakui-Koyori.md › [SW] Relationships`: Shishiro Botan: NePoX and Blue Journey.
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2023 | "Blue Journey" with Marine, Noel, Lamy, Botan, Lui and Sakura Miko (07-08; official roster); 1 million subscribers (09-24, secondary); Hoshimatic Project (from 11, secondary) | [Blue Journey roster] [Observed KO2] |
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2025 | Weekly Famitsu column launched (07-17); archived collabs bill Koyori, AZKi and Lamy as "KoZMy" (08-03, 08-20); "pink-haired pair" talk with Marine | [KO7] [KO4 lvgC3pW-LVA, oxWPvsUb_3Y] |
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2026-03-24 | #ラミこよ off-collab with Lamy, proposing to choose a duo name (no final name established) | [Lamy channel Zi8R63ee0Fs] |
- `bible/characters/Hakui-Koyori.md › Background Timeline`: | 2026-08-22 | Announced hololive Koshien 2026: Koyori is organizer and one of six team managers (others include Houshou Marine and Shirogane Noel); the main competition is scheduled for 10-17/18 (after the baseline: an announcement only). | [Member announcement NEW-R6-017] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | La+ Darknesss | holoX founder | A sponsored "#stons" deep-breathing collab (2024-12-16); a cover with La+ and Marine (2025) Their duet "SUKIDEKA!!~BIGLOVE????~" (2025-11-21). | [KO4 lz37xE9ED1I, ZMpsiRdqXfE] [Official NEW-R6-011] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | AZKi, Yukihana Lamy | "KoZMy" (archived titles) | Archived 2025 collabs bill the trio as KoZMy (formation talk 08-03, a horror monitoring game 08-20); a four-person 3D karaoke with AZKi (2026-02-03, not a KoZMy event); a #ラミこよ off-collab with Lamy (2026-03-24) Lamy: "Snow halation" together on STAGE 1 of hololive 7th fes. (2026-03-06). | [KO4 lvgC3pW-LVA, oxWPvsUb_3Y, 1HQL3WJPBHA] [Lamy channel Zi8R63ee0Fs] [Official, 7th fes. STAGE 1 report] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Houshou Marine | "Pink-haired pair" | A talk testing whether they are alike (2025); Marine backseats her Pikachu game (2025); Blue Journey She joined Marine's Holo Koshien session (2026-09-17). | [KO4] [KO2] [Archive metadata, ckworks 73sl-3cOp2E] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Shirogane Noel | Blue Journey | "NoeKoyo" in a baseball-game exhibition match (2025) | [KO4] [KO2] |
- `bible/characters/Hakui-Koyori.md › Relationship Map`: | Shishiro Botan | NePoX; Blue Journey | NePoLaBo × holoX events (official 2026 roster); Blue Journey (official roster) | [KO2] [NePoX roster] [Blue Journey roster] |
- `bible/characters/Hakui-Koyori.md › Story Engine`: 2. A KoZMy horror night in which Koyori volunteers AZKi and Lamy as test subjects.

### from Hoshimachi Suisei
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Houshou Marine: "Chatter Chatter"
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Shirogane Noel: a fellow Shiranui Kensetsu member.
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: La+ Darknesss, Nakiri Ayame and Shishiro Botan: holoGTA (2024); La+, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024).
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Kikirara Vivi: taught her Tetris (2026).
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2026-03 | "Chatter Chatter" with Houshou Marine; playable in Fortnite (03-13 to 03-24) | [Observed SU4] [SU3, secondary] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Nekomata Okayu | "MOMAS" (secondary label) | With Sakura Miko, Houshou Marine and Hiodoshi Ao; on Okayu's 2025 New Year Game Festival team (secondary roster) | [SU2] [S1] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Shiranui Flare, Omaru Polka, Miko, Shirogane Noel | "Shiranui Kensetsu" | Suisei is its PR director; R.E.P.O. "work shift" (2026) | [SU2] [SU4] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Houshou Marine | "Chatter Chatter" (2026) | A duet with an original anime MV (official release page 711); the wiki's holoALICE and MOMAS labels were not verified in review They performed "Chatter Chatter" together on STAGE 4 of hololive 7th fes. (2026-03-08). | [Marine file MA4] [Official NEW-R5-003] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Shirogane Noel | Shiranui Kensetsu | The Minecraft construction company with Flare, Polka and Miko | [Noel file NO2, secondary] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | La+ Darknesss, Nakiri Ayame, Shishiro Botan | — | All four streamed holoGTA (2024-09); Sammy's m HOLD'EM collaboration (2024) featured Suisei, La+, Botan and Shirakami Fubuki (publisher roster; a joint broadcast is not established) | [SU4 2v4DYYf7hB0] [Sammy roster] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Kikirara Vivi | — | Taught Vivi Tetris on Vivi's channel (2026-08-29). | [Archive metadata, ckworks qHC9c62GCpc] |

### from IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: Shishiro Botan, Takane Lui, Sakamata Chloe and Tokoyami Towa: an Overwatch 2 team (2023); Hakui Koyori: Splatoon 3 and Among Us.
- `bible/characters/IRyS.md › Voice Profile`: - Secondary description: a "high-pitched, soft and calm" speaking voice (compared with Yukihana Lamy); a more powerful, deeper singing voice (compared with Tokoyami Towa). [Observed R2 §Personality, secondary]
- `bible/characters/IRyS.md › Relationship Map`: | Shishiro Botan, Takane Lui, Sakamata Chloe, Hakui Koyori | JP members | Left 4 Dead 2 with Botan, Lui and Inugami Korone (2022-04-24); an Overwatch 2 team with Botan, Lui, Chloe and Towa (Holizontal JAM, 2023-08); Splatoon 3 with Koyori, Watame and Korone (2022-10-03); an Among Us lobby with Koyori, Chloe and others (2023-05-08); Minecraft elytra hunting with Lui and Kronii (2022) | [S1 K1wStJxm4F0, roWKpgZsjR4, Xoma7oWsMcM, VwqdwQx5cog] |

### from Kazama Iroha
- `bible/characters/Kazama-Iroha.md › [SW] Relationships`: Yukihana Lamy and Shishiro Botan: NePoX.
- `bible/characters/Kazama-Iroha.md › [SW] Relationships`: Houshou Marine and Shirogane Noel: fellow Bara☆Dice vocalists (distributor credits).
- `bible/characters/Kazama-Iroha.md › Relationship Map`: | Yukihana Lamy, Shishiro Botan | NePoX | Caravan Stories with Lamy (2023); built the roof of Botan's Minecraft shop (2023) | [IR4] [IR2] |
- `bible/characters/Kazama-Iroha.md › Relationship Map`: | Kikirara Vivi, Koseki Bijou | Kouhai and EN | Fellow commentators (Lamy hosting) on the 2026-01-15 SUPER EXPO 2026 / 7th fes. information programme (secondary report). | [Secondary NEW-R6-008] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Kikirara Vivi: Bijou watched Vivi's FLOW GLOW debut with FUWAMOCO (2024).
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Kikirara Vivi | FLOW GLOW kouhai | Bijou watched FLOW GLOW's debut with FUWAMOCO (2024-11-09; a watch-along, not a collab with Vivi) | [S1 gAj77STI2oc] [Official debut schedule] |

### from La+ Darknesss
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Nerissa Ravencroft, Nakiri Ayame, Hoshimachi Suisei and Shishiro Botan: fellow holoGTA participants (2024).
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Suisei, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024).
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Houshou Marine: a sponsored collab billed #マリラプ and a cover with Koyori (2025).
- `bible/characters/Laplus-Darknesss.md › [SW] Relationships`: Yukihana Lamy and Shishiro Botan: NePoX (2026).
- `bible/characters/Laplus-Darknesss.md › Relationship Map`: | Nakiri Ayame, Hoshimachi Suisei, Shishiro Botan | — | Fellow holoGTA participants (2024-09; each archive establishes participation, not specific exchanges); Sammy's m HOLD'EM collaboration (2024) featured La+, Suisei, Botan and Shirakami Fubuki (publisher roster, not Ayame; a joint broadcast is not established) | [LA4 swqXHi1Z4ew, QLHSm3rpG8k] [Sammy announcement] |
- `bible/characters/Laplus-Darknesss.md › Relationship Map`: | Houshou Marine | "#マリラプ" (archived title) | A sponsored collab (2025); a cover with Marine and Koyori (2025) | [Marine file] [KO4] |
- `bible/characters/Laplus-Darknesss.md › Relationship Map`: | Yukihana Lamy, Shishiro Botan | NePoX | NePoLaBo × holoX events (2026) | [Lamy file] [Botan file] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Houshou Marine: archived metadata records a Touhou off-collab and Mario Party with Nerissa (2024).
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Kikirara Vivi: #holoREPO (2025).
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Shirogane Noel: a team Mario Kart event (2023).
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Marine: a Touhou off-collab (2024-04-30), Mario Party with Nerissa (2024-06-17), a watch-along of her solo concert (2024-12-07), a "Chatter Chatter" dance short (2026); Noel: "Yuru Holo" team Mario Kart (2023-12-12) and a "Très Bien Night" dance short (2025); Vivi: FLOW GLOW's debut watch-along (2024) and #holoREPO (2025) | [S1 x7gRHgQ0yI0, FLL7e1-RPGo, zQdsLXE4ZQ8, PtaFGDOaj0k, Janl2FCKmsg, 8RjOCCH2sac, gAj77STI2oc, Z5cpzbdsLDE] |

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: English-lesson guests Marine, AZKi, La+, Iroha, Lui and Chloe (2022); HOLOYOI guests Lui, Chloe, Noel and Botan (2023).
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Yukihana Lamy: the Myth × fifth-generation Among Us collab (2020).
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Houshou Marine, Shirogane Noel, Shishiro Botan | JP seniors | HOLO ENGLISH LESSON #01 with Marine, Ina and Fubuki (2022-02-19); Mario Kart with Marine, Bae and Reine (2021-12-25); a house-party off-collab with Marine and Bae and a playthrough of Marine's horror game (2023-08-14); HOLOYOI #02 with Noel and Flare (2023-04-20) and #03 with Botan and Subaru (2023-05-18) | [S1 bfUEbp3xk4o, Tpzbfccp_ZM, DY5VThfehW8, Mf-sAjsuSig, wyrLR1CC1Co, EatMZc1N3VM] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Yukihana Lamy | JP fifth generation | Co-players in Nene's Myth × fifth-generation Among Us collab (2020-10-24). | [Archive metadata TIE-034 to 038] |

### from Nakiri Ayame
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: Houshou Marine: a third-generation junior whom secondary accounts say Ayame admires.
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: La+ Darknesss, Hoshimachi Suisei and Shishiro Botan: holoGTA (2024).
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: Shirogane Noel: an Audio-Technica sponsored stream (2025-07-11).
- `bible/characters/Nakiri-Ayame.md › Behavioral Traits`: 6. Secondary accounts describe her taking time to become comfortable with unfamiliar collaborators; she admires Houshou Marine, a third-generation junior. [Observed AY2 §Personality, secondary]
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | Houshou Marine | a 3rd-generation junior she admires (secondary) | — | [AY2, secondary] |
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | La+ Darknesss, Hoshimachi Suisei, Shishiro Botan | — | All four streamed holoGTA (2024-09); Ayame was not in the m HOLD'EM poker collab | [AY4 1iz9AxcgvPg] [Sammy roster] |
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | Shirogane Noel | — | An Audio-Technica sponsored stream (2025-07-11, archived metadata) | [Noel file NO4 cpUnHgEveX8] |

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Shirogane Noel, Kikirara Vivi and Elizabeth Rose Bloodflame: her Gartic Phone EN + ID + JP collab (2025).
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Houshou Marine: Mumei and Bae played "Truth of Beauty Witch," the horror game featuring Marine (2023).
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Sakamata Chloe, Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Chloe and Lui on Mumei's EN-server Minecraft tour with Bae (2022-02-12); Marine's horror game with Bae (2023-08-23); Noel and Vivi in Mumei's Gartic Phone EN + ID + JP (2025-04-14) | [S1 50tBPC5c2zM, RY1GkF4jMls, OMDzBQohAf8] |

### from Nekomata Okayu
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Houshou Marine: gave her the nickname "Okanyan."
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: ("Dorobo Kensetsu" comes from secondary references.) AZKi: Mario Kart World practice for Team Wind (2026-01-16) and AZKi's pun-ASMR contest (2025), where Shirogane Noel also played.
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Kikirara Vivi: a 2026 collab on Vivi's channel.
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Yukihana Lamy: a "Lukewarm" duet cover (2024).
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Houshou Marine | — | Marine gave her the nickname "Okanyan" (official profile); a joint marshmallow-reading stream on her recommended list | [Official OK1] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Hoshimachi Suisei | "MOMAS" | With Sakura Miko, Houshou Marine and Hiodoshi Ao; PlateUp! on her 2025 team | [OK2] [OK4] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Shirogane Noel | JP senior | Fellow players in AZKi's 3D pun-ASMR contest (2025-06-22); a group activity, not a pair collab. | [Archive metadata NEW-R5-004] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Kikirara Vivi | — | A 2026-08-25 collab on Vivi's channel framed around やーらし. | [Archive metadata, ckworks jlt6HHrZnpE] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Yukihana Lamy | JP kouhai | A "Lukewarm" duet cover on Okayu's channel (2024-02-01). | [Member-upload title TIE-004] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Houshou Marine: one of her oshis (secondary); Mario Party Superstars with FUWAMOCO (2024).
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Shishiro Botan: a guest at her birthday live "Stray&Stay"
- `bible/characters/Nerissa-Ravencroft.md › Behavioral Traits`: 3. She is an open fangirl of Houshou Marine and Takanashi Kiara (a self-described KFP member); in her lore she worked at KFP before hololive. [Observed N2 §Likes and dislikes, §Lore, secondary]
- `bible/characters/Nerissa-Ravencroft.md › Voice Profile`: | Fangirling (Kiara, Marine) | Fast, flustered, delighted | (no verified line; see Relationship Map) |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Houshou Marine | JP senior and oshi |  off-collab with Marine and FUWAMOCO (2024) | [Observed N2; N3 title] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Shishiro Botan | — | A credited guest at Botan's birthday 3D live "Stray&Stay" (2026-09-19). | [Archive metadata, yutura cI535pJp-TQ] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Houshou Marine and Sakamata Chloe: UMISEA.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Yukihana Lamy: a Minecraft festival and "date"-billed collab (2021) and a "Pleides" guest (2024).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Shishiro Botan: an "EVERMORE" guest (2025).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Shirogane Noel, Kikirara Vivi and Elizabeth Rose Bloodflame: Mumei's Gartic Phone (2025).
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate; fellow member of the official unit UMISEA (2021, with Minato Aqua and Houshou Marine; the wiki also lists Sakamata Chloe) [Official I31] | Secondary accounts describe Ina's protective mock-threat bit about Gura; Ina drew chibi Bloop; a prank war is reported but [Unverified] | [Observed I2 §Relationships; Gura file G2 §Gura's antics and §Mascots and fans] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Houshou Marine | JP senior; UMISEA (official 2023 roster) | Admired artist-performer ("Marine-senpai," 2022 interview, not reopened in review); Marine guested at "Pleides" (2024) | [Observed—published interview I18] [Official UMISEA roster] [S1 3n9igJnSXtQ] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Yukihana Lamy, Shishiro Botan, Kikirara Vivi, Shirogane Noel | JP members | Lamy: the Minecraft "Usaken Summer Festival" (2021-06-27), an EN-server "date" (2021-10-20) and a guest at "Pleides" (2024-12-28); Botan: a guest at "EVERMORE" (2025-05-21); Vivi: R.E.P.O. (2025-06-02); Noel and Vivi: Mumei's Gartic Phone (2025-04-14) | [S1 a7CvRf4vFYc, Isp3UhgOAB4, 3n9igJnSXtQ, I-J11Da5ONY, grBU9Dl09Ds, OMDzBQohAf8] |

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Kikirara Vivi and Shirogane Noel: Mumei's Gartic Phone (2025).
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Takane Lui, Shirogane Noel, Kikirara Vivi | JP members | Minecraft elytra hunting with Lui, IRyS and Kaela (2022); Mumei's Gartic Phone EN + ID + JP with Noel and Vivi (2025-04-14) (archived upload credits) | [S1 zp5nxAgi2dw, OMDzBQohAf8] |

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Yukihana Lamy, Houshou Marine | — | Team Bird teammates at the New Year Game Festival 2026 (2026-01-24; a team roster, no specific exchange). | [Secondary TIE-039 to 043] |

### from Sakamata Chloe
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Houshou Marine: UMISEA (official 2023 roster) and holoWitches.
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Yukihana Lamy: Rust with Kanata (2022).
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Shishiro Botan: an Overwatch 2 team (2023).
- `bible/characters/Sakamata-Chloe.md › Behavioral Traits`: 2. Taunt-loving but sweet: compared by fans to Shirogane Noel, Momosuzu Nene and Tsunomaki Watame. [Observed CH2 §Personality, secondary]
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Houshou Marine | UMISEA (official 2023 roster); holoWitches | A game about Marine's treasure ship (2023) | [CH2] [CH4] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Yukihana Lamy | — | Rust with Kanata and Lamy (2022) | [CH4] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Shishiro Botan | — | An Overwatch 2 team with IRyS, Lui and Towa (2023) | [CH5] |
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Ninomae Ina'nis, Gawr Gura (graduated) | UMISEA | The ocean unit's official 2023 roster: Aqua, Marine, Chloe, Gura and Ina | [Official UMISEA roster https://hololivesummer2023.hololivepro.com/unit/umisea/] |

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Yukihana Lamy, Houshou Marine | — | Team Bird teammates at the New Year Game Festival 2026 (2026-01-24; a team roster, no specific exchange). | [Secondary TIE-039 to 043] |

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Shishiro Botan: fellow builders in Botan's Minecraft "Usada Kensetsu"
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: HOLOTALK guests include Houshou Marine (#1), Hoshimachi Suisei ("cometori"), AZKi, Shirogane Noel, Nekomata Okayu and Nakiri Ayame. holoX: La+ ("Glow in the Dark"), Chloe ("WILDCARD"), Koyori ("MIRAGE") and Iroha (a guest at her 2024 and 2025 lives).
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Houshou Marine, Oozora Subaru | JP seniors | Early HOLOTALK guest (Marine); first EN×JP collab (Subaru, 2020) | [Observed T2 §2020, secondary] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Houshou Marine, Shirogane Noel | JP seniors | HOLOTALK's first guest Marine ("#marinarasauce," 2020-11-20) and 22nd guest Noel (2022-03-05); a "MIRAGE" dance short with Marine (2024) | [S1 3HwaqbdKO1s, toe_PmrDWBU, tzVgzvV0cVo] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Shishiro Botan | JP senpai | A fellow builder in Botan's Minecraft "Usada Kensetsu"; she joined the Usaken summer-festival planning and building collab (2021-06-07), and contemporary viewers describe Botan checking on Kiara's building team. | [Archive metadata NEW-R1-009; secondary clip record] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Yukihana Lamy | — | Team Bird teammates at the New Year Game Festival 2026 (2026-01-24; a team roster, no specific exchange). | [Secondary TIE-039 to 043] |

### from Takane Lui
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Shishiro Botan: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (2023, archived title); Left 4 Dead 2 with IRyS and Korone (2022); Blue Journey.
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Houshou Marine, Shirogane Noel and Kazama Iroha: Bara☆Dice (with Flare and Nene).
- `bible/characters/Takane-Lui.md › [SW] Relationships`: Yukihana Lamy: NePoX (2026).
- `bible/characters/Takane-Lui.md › Relationship Map`: | Shishiro Botan | "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame | A Minecraft collab under that name (2023-04-18, archived title on Botan's channel); Left 4 Dead 2 with IRyS and Korone (2022); the 2023 Overwatch 2 team; Blue Journey (official roster) | [LU2] [Botan file 4-NEM2HrUVA, K1wStJxm4F0] [Blue Journey roster] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Houshou Marine, Shirogane Noel | Bara☆Dice (Bandai credits, with Flare, Nene and Iroha); Blue Journey (official roster) | The wiki's "SSS" with Yuzuki Choco was not found in the archive titles | [LU2] [Bandai credits] [Blue Journey roster] |
- `bible/characters/Takane-Lui.md › Relationship Map`: | Yukihana Lamy | NePoX | NePoLaBo × holoX events (2026) | [Lamy file] |

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Shishiro Botan and Yukihana Lamy: the Myth × fifth-generation Among Us collab (2020).
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Shishiro Botan, Yukihana Lamy | JP fifth generation | Co-players in Nene's Myth × fifth-generation Among Us collab (2020-10-24). | [Archive metadata TIE-034 to 038] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › [SW] Description`: Beyond EN: Bijou and Kaela Kovalskia's Grindstone collabs include Raft, Minecraft and Split Fiction; Vestia Zeta and Shiori are the official duo GreyScaleX ("Purrfect Pair" merchandise, 2026); Pavolia Reine and Airani Iofi join Shiori and Gigi in the "Fanfic Club"; FUWAMOCO's oshi are Houshou Marine and Omaru Polka.
- `bible/world/Advent-Pairs.md › Beyond EN`: - **JP:** FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo); archived game metadata lists Shirakami Fubuki and Hakui Koyori with the twins; "FUWAMOKOYO" labels Koyori and the twins in FUWAMOCO MORNING #90; Okayu and Korone made cameos at their 3D debut; Oozora Subaru sang "HOT DUCK!" with Bijou and the twins; Akai Haato and Bijou are "Red Stone"; Ichijou Ririka (ReGLOSS, originally DEV_IS) played Smash Bros. with Bijou with a loser's punishment. [Observed S1; S2]

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ina appears with Aqua, Marine, Chloe and Gura in UMISEA's official 2023 roster and released "Kurukuru Cruise" with Nekomata Okayu (2025).
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Secondary references call Gura and Shishiro Botan "Apex Predators"; Gura released a duet cover with Murasaki Shion.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Nerissa's oshi is Houshou Marine; she pairs with Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan."
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: (the X is silent; "Purrfect Pair" merchandise, 2026), Reine and Airani Iofi join her "Fanfic Club"; FUWAMOCO's oshi are Marine (Fuwawa) and Omaru Polka (Mococo), they game with Shirakami Fubuki and Hakui Koyori, and Oozora Subaru sang "HOT DUCK!" with them and Bijou.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Of Justice: Ollie is Elizabeth's kami-oshi, and Elizabeth plays with her and HOLOSTARS members in varying lineups (Code Red games; Marvel Rivals with Crimzon Ruze, her "Nephew" in an uncle–nephew bit); Elizabeth's 2026 birthday covers featured Subaru, Roboco, Sora, Choco, Marine, Korone, Polka, Nene, Watame and Iroha; Kaela appears in Raora's fictional basement bit ("SMITTEN"); Raora played Clubhouse Games with Haachama and Super Mario Party with Haachama and Zeta, and is "RaoRiRi" with Ririka; Cecilia plays games with Sora; at Serendipity, Kobo, Zeta and Tsunomaki Watame sang with Elizabeth, Gigi, Cecilia and Raora.
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ninomae Ina'nis:** an artist among artists: the ocean unit UMISEA (formed 2021 with Minato Aqua, Houshou Marine and Gura; Chloe appears in the official 2023 roster; Aqua and Gura have graduated and Chloe is an affiliate); "HoloJEI" (Tsunomaki Watame, Kureiji Ollie, Anya Melfissa); "TakoBazo" (Vestia Zeta); "TakoNeko" (Nekomata Okayu, a secondary pair name; "Kurukuru Cruise," 2025; see "JP Senpai Pairs"); Shiranui Flare appeared on her 2025 AmiAmi special ("Flare?!!?"). She admires Marine as an artist. [Observed S1; S2 Ina; Ina file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Gawr Gura** (graduated): "Apex Predators" (Shishiro Botan), UMISEA, "SharPea" (Pavolia Reine), and Murasaki Shion (Minecraft and Mario Kart in 2021; a "Renai Circulation" duet cover, 2022). [Observed S1; S2 Gura]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ceres Fauna** (graduated): her first official collab outside her generation was with Pavolia Reine (Clubhouse 51, 2021-10-12, per the wiki; Minecraft "WITH REINE," 2022-01-19, ronEFZPwxqc); Kaela Kovalskia was a recurring partner ("Fearless & Fearful vs Ghosts," an ID Minecraft server tour); she admired Shirogane Noel. [Observed S1; Fauna file F2 §2021, §Trivia, secondary]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Nerissa Ravencroft:** Houshou Marine is her oshi (an off-collab with Marine and FUWAMOCO, 2024); "BLUE·MEGAMISAMA" with Tokino Sora; "V3LVET" with Raora and Moona Hoshinova; Kobo calls her "Nori-chan." With Moona she has a released song, "100% (feat. Nerissa Ravencroft)" (2025-02-16) [Official S7]. [Observed S1; S2 Nerissa; Nerissa file]
- `bible/world/Cross-Branch-Friends.md › How It Works in Stories`: - Senpai and kouhai describe relative seniority (who debuted first) and nothing else; forms of address and levels of formality vary by relationship. Some EN members are openly starstruck by particular senpai (Kiara by Pekora, Nerissa by Marine). [Observed character files]
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 4. Nerissa meets Marine at an event and forgets every word of Japanese.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Calli's senpai: Suisei. Kiara's oshi: Pekora. Nerissa's oshi: Marine (and Kiara).

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › [SW] Description`: Close to all of Advent (with Nerissa as the self-declared third sister, "Mofufu"), to Mori Calliope ("FUWAMOCALLI," a collaboration name the twins say they particularly like), to Raora Panthera (B.F.F, their 2026 concert unit), and to JP seniors including their oshi Houshou Marine (Fuwawa) and Omaru Polka (Mococo).
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **JP:** Houshou Marine (Fuwawa's oshi; a Touhou off-collab, 2024) and Omaru Polka (Mococo's oshi); Shirakami Fubuki (horror collabs and Lethal Company with Hakui Koyori, "FUWAMOKOYO"); Akai Haato, Tsunomaki Watame ("FUWAMOCO vs FUWAFUWA," 2024), Oozora Subaru (a Donkey Kong Country 2 off-collab, 2026), and Nekomata Okayu and Inugami Korone, who made cameos at their 3D debut. Guests at their 2025 birthday concert: Shiori, Bijou, Nerissa, Polka, Koyori, Marine, Ookami Mio and Fubuki. [Observed S1; S3]

### from JP Senpai Pairs
- `bible/world/JP-Senpai-Pairs.md › Hoshimachi Suisei with the cast`: - **Others:** Hakos Baelz ("High Tide," 2024; a 2025 dance short to Suisei's "Moonlight"); Nanashi Mumei (a #bibbidibachallenge short together, 2024-06-18); FUWAMOCO (a 2026 dance short to Suisei and Houshou Marine's "Chatter Chatter"); Nerissa Ravencroft (a "BIBIDEBA" dance short, 2024); Koseki Bijou (a Fortnite stream titled "THE SUISEI CONCERT IN FORTNITE?!", 2026-05-02, after Suisei joined Fortnite as a playable character in March 2026). [S1] [Official S6] [S5 Suisei, secondary]
- `bible/world/JP-Senpai-Pairs.md › Among the four`: - **Suisei and Okayu:** "MOMAS" (secondary) with Sakura Miko, Houshou Marine and Hiodoshi Ao. [S2]

### from Justice Pairs
- `bible/world/Justice-Pairs.md › Beyond EN`: - **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone ("IT'S LOVE," iwnHChZq0N8, credits read by Claude); FUWAMOCO with Polka, Nene, Watame and Iroha; her 2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members). Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is "RaoRiRi" with Ichijou Ririka; "OkaGigi" is a secondary pair label for Gigi and Nekomata Okayu; secondary clip metadata records translation-based banter during the 2026 New Year Game Festival. It does not establish exact dialogue or a private relationship. Tsunomaki Watame sang "Cloudy Sheep" with Calli and Cecilia and "What an amazing swing" with Kiara and Raora at Serendipity. FLOW GLOW: Koganei Niko sang with Elizabeth in LYRA. [Observed S1; S2] [Official S6, S7]

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |

### from holoX
- `bible/world/holoX.md › How they work together`: - NePoX: NePoLaBo (Nene, Polka, Lamy, Botan) × holoX; the 2026 event roster is the eight active members (Chloe is not on it), and the joint song "Watcha Gatcha!!!!!!!!" was released 2026-08-26. Membership and rosters are dated. [S3] [Official NePoX 2026 roster] [Official music 801]
- `bible/world/holoX.md › With the English cast`: - **Ninomae Ina'nis, Gawr Gura (graduated):** UMISEA with Chloe, Minato Aqua and Houshou Marine (official 2023 roster). [Official UMISEA roster https://hololivesummer2023.hololivepro.com/unit/umisea/]
- `bible/world/holoX.md › With the other Japanese members on the cards`: - AZKi: "Kanaken" with Chloe and Amane Kanata; "AzuIro" (Iroha), "KoZMy" (Koyori and Lamy); AZKi danced to La+'s, Koyori's and Lui's songs (2026). Suisei: Hoshimatic Project with Koyori, Chloe and Iroha. Okayu: "Dorobo Kensetsu" with La+ and Lui; La+'s lie-detector 3D challenge to Okayu (2026-05-19). Ayame: VALORANT with La+ (2024); "#みっころおにかん" games with Lui (2025). Botan: NePoX; "InuTakaShishiRam" with Lui, Korone and Watame (Minecraft, 2023). Marine: Bara☆Dice with Lui and Iroha (Bandai credits); UMISEA with Chloe. Lamy: KoZMy with Koyori. [S3] [S1]

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-11-09 | DEV_IS second unit FLOW GLOW debuts (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya, Kikirara Vivi) | — |

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019 | 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins | Kiara's oshi Pekora; Nerissa's oshi Marine; Calli's collaborator Hoshimachi Suisei |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-08 | 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) | The JP generation just before Myth |

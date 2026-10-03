# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: myth4
Packet: projects/holoen/research/qa/packets/myth4.md (owned material) and projects/holoen/research/qa/packets/myth4-incoming.md (incoming claims); both are inline below
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
| AUDIT-MYTH3 | Cohort audit myth3 (Kiara, Other Pairs, TakoTori): 51 rows | applied; MYTH-SCOPE-002 adapted to keep the author's public-performance shorthand; MYTH-COVERAGE-001 superseded; MYTH-VOICE-001 rejected (label) | 2026-10-03 merge |
| AUDIT-JUSTICE | Cohort audit justice: 36 rows | applied; two COVERAGE rows superseded by run F; EXPORT-001 rejected (label) | 2026-10-03 merge |
| AUDIT-GLOBAL | Cohort audit global: 60 rows | applied (including the parser fixes in tools/qa_packets.py); overlaps closed by justice and myth1 | 2026-10-03 merge |
| CLAUDE-SCOPE-003 | Merge Records naming excluded topics (15 cards) | applied (genericized) | 2026-10-03 merge |

### Registry excerpt (this cohort's cast and world records and its units; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "fa69d71",
 "cast": [
  {
   "name": "Ninomae Ina'nis",
   "file": "bible/characters/Ninomae-Inanis.md",
   "other_names": [
    "Ina",
    "Ina'nis",
    "Inya",
    "Ninomanyo Inya'nis",
    "一伊那尓栖"
   ],
   "groups": [
    "hololive",
    "hololive -Myth-",
    "Myth",
    "hololive English (former branch name)",
    "Octo'clock"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. Ina is a VTuber whose lore, a persona she plays gently and for laughs, makes her an ordinary girl, despite how she looks, who picked up a strange book, gained the power to control tentacles and began hearing Ancient Whispers; the book is her floating companion, AO-chan.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2020-09-13",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Ninomae-Inanis.md › Background (debut: Hard Facts / Background Timeline)"
   }
  }
 ],
 "world": [
  {
   "name": "TakoTori",
   "file": "bible/world/TakoTori.md",
   "role": "Relationship",
   "other_names": [
    "Kiara and Ina",
    "Ina and Kiara",
    "Drawn to Dawn"
   ]
  }
 ],
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
   "unit": "Octo'clock",
   "members": [
    "Ninomae Ina'nis",
    "Ouro Kronii"
   ],
   "evidence": "official Serendipity billing, 2026"
  }
 ]
}
```

### projects/holoen/research/qa/packets/myth4.md

# Audit packet: myth4

Snapshot: git fa69d71. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Ninomae-Inanis.md` 45ccf8a3589f; `bible/world/TakoTori.md` c3f8a29470c0

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Ninomae Ina'nis — `bible/characters/Ninomae-Inanis.md`
**[SW] Groups:** hololive, hololive -Myth-, Myth, hololive English (former branch name), Octo'clock
**[SW] Other Names:** Ina, Ina'nis, Inya, Ninomanyo Inya'nis, 一伊那尓栖
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. Ina is a VTuber whose lore, a persona she plays gently and for laughs, makes her an ordinary girl, despite how she looks, who picked up a strange book, gained the power to control tentacles and began hearing Ancient Whispers; the book is her floating companion, AO-chan. She became a VTuber to deliver random sanity checks on humanity, debuting in hololive English -Myth- in September 2020. She drew Myth's intro art and designed Takodachi, Bubba and Death Sensei. Her fans are the Tentacult, each one a Takodachi, after the little purple mascot she designed. Her songs tell darker stories about her priestess duty. She released her first EP, re:VISION, and held the duo concert Drawn to Dawn with Takanashi Kiara in 2026, sang at Myth's 6th-anniversary 3D live with Calli and Kiara, which premiered the Myth song "THIS IS MYTH," and she partners with Ouro Kronii. Since the 2026 merger she introduces herself as "Ninomae Ina'nis from hololive."
**[SW] Relationships:** Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself. Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, credits Kiara's support for her confidence in dancing, and Kiara groans at her puns. Mori Calliope: a recurring target of her puns (Calli's exasperated reaction to Ina's puns); Ina designed Death Sensei, and Calli wrote lyrics for Ina's song. Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin. Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry. Koseki Bijou: "wooden shovel" buddy ("TakoRocky") whose collab outfit Ina designed; with IRyS they starred at Dodger Stadium's hololive night (2025). IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put both on her Tomodachi Life island. Houshou Marine: UMISEA. Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025). Shiori Novella: a "Rate Your Fears" nightmare talk (2024); "MONSTER" with Kronii and Gigi on stage (2025). FUWAMOCO: "SHALLYS" with Cecilia on the same stage. Cecilia Immergreen: Stranger of Paradise partner (2025), who plays up a rivalry. Gigi Murin and Raora Panthera: Blood Typers with Gigi, Puyo Puyo Tetris 2 with Raora, and a sponsored Monster Hunter Wilds launch with both and Bijou (2025). Ookami Mio (GAMERS): "Dottabatta Chindouchuu" with FUWAMOCO at Serendipity. Hoshimachi Suisei: "BIBBIDIBA" (2024). Hakos Baelz: a K/DA "POP/STARS" cover with Moona Hoshinova and Ayunda Risu (2023), a stream art lesson (2024) and Ina's AmiAmi special (2025). Nekomata Okayu ("TakoNeko," a secondary pair name): "Kurukuru Cruise" (2025) and her 2025 New Year Game Festival team, with Nakiri Ayame. Yukihana Lamy: a Minecraft festival and "date"-billed collab (2021) and a "Pleides" guest (2024). Shishiro Botan: an "EVERMORE" guest (2025). Shirogane Noel and Kikirara Vivi: Mumei's Gartic Phone (2025). AZKi: R.E.P.O. "JP & EN" (2025).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | Picked up a strange book, gained tentacle powers and began hearing Ancient Whispers; VTubes "to deliver random sanity checks on humanity, as an ordinary girl" | [Official I1] |
| 2020-09-13 | Debuts in hololive English -Myth- | [Official I1] |
| Ongoing | Illustrator: drew Myth's intro art; designed the Takodachi [I2 §Mascot and fans], Bubba [Ame file A2 §Mascots and fans] and Death Sensei [Calli file C4 §Mascot and fans] (the wiki says all Myth mascots except Bloop); she drew chibi Bloop artwork, but Bloop's original design is not hers [Gura file G2] | [Observed I2 §Miscellaneous and §Mascot and fans, secondary] |
| 2021-08 | The WAH acronyms begin (*Ender Lilies* streams) | [Observed I2 §WAH] |
| 2022-02 | Nintendo Direct "TOMORROW?!" reaction | [Observed I23] |
| 2024 | MECONOPSIS and TEMARI; she discusses MECONOPSIS's conflict between duty and protecting others | [Official I1 music list] [Observed—published interview I7b] |
| 2026-02-02 | First EP "re:VISION" | [Official I26] |
| 2026-03-27/28 PDT | "Drawn to Dawn" duo concert with Kiara (Los Angeles) | [Official I20, I21] |
| 2026-06-04 | Serendipity interview and partnership with Kronii | [Official I7] |
| 2026-01-08 (digital release; zone unspecified) | Digital release of TAKO∞TAKOVER; lyrics by Mori Calliope. I19 discusses its deliberately unsettling takeover story. | [Observed—published interview I19] [Official I25; digital release: https://hololive.hololivepro.com/en/music/693/, checked 2026-10-03] |
| 2026-09-07 | Branches merge; she is "Ninomae Ina'nis from hololive," unit hololive -Myth- | [Official I28] [Observed I10] |
| 2026-09-19 PDT | Myth 6th Anniversary 3D LIVE "Seasons From Within" with Calli and Kiara; "THIS IS MYTH" premieres | [Archive metadata I32] |
| 2026-09-19 | Original single "Stardust Capsule" (hololive catalogue CVRD-824). | [Official NEW-R1-011] |
**Dossier · Hard Facts (continuity):**
- Birthday May 20; height 157 cm; debut 2020-09-13; unit hololive -Myth-; illustrator Kuroboshi Kouhaku
  (whom she calls "papa"). [Official I1] [Observed I2 infobox]
- Fans: the Tentacult (official), individually Takodachi; hashtags #TAKOTIME #タコタイム (streams),
  #inART #いなート (fan art). [Official I1]
- Nicknames: Ina, Tako, Inya, Ninomanyo Inya'nis, Punchou, "Ore no Ina" (by Flare). Persona family jokes:
  Mama'nis, Papa'nis (never real family details). [Observed I2 infobox and §Miscellaneous]
- Likes: food (garlic, burgers over pancakes), drawing, gaming, reading, the soft drink "Dr. Oopsie."
  Dislikes: bugs, being bored, cucumbers ("They smell like cucumbers."). [Observed I2 §Likes and
  dislikes and §Quotes, secondary]

### TakoTori — `bible/world/TakoTori.md`
**[SW] Other Names:** Kiara and Ina, Ina and Kiara, Drawn to Dawn
**[SW] Description:** Takanashi Kiara and Ninomae Ina'nis, Myth's gas pedal and brake. Ina's words: Kiara has "a very 'go-getter', lively energy," Ina is "laid-back, my-pace," and "one of us is the gas pedal and one of us is the brake." Kiara's: "so different from me, and I love that," a mix of "cat fueled energy" and "energy drink fueled energy." Ina credits Kiara's support with helping her gain confidence in dancing. Ina designed Kiara's mascot Kotori, and Kiara still "fired" Ina over the 2020 KFP chicken incident. Their recent shared work includes the 2026 duo concert "Drawn to Dawn" (The Wiltern, Los Angeles, March 27–28 PDT) and a joint cover.
**[SW] Rules:** Kiara leads with volume and plans; Ina answers with calm, a pun, or one quiet line that lands. Their public collaborations include concerts and game streams. The firing is a running KFP joke, never a real grudge.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2020-11 | The KFP chicken incident; Kiara "fires" Ina | KFP lore |
| 2024-03-04 | "TAKOTORI OFFCOLLAB!!" | The pair name in their own titles |
| 2025-11-23 | Duo concert announced | — |
| 2026-03-27/28 PDT | "Drawn to Dawn," the Wiltern, LA | Their first concert as a duo |
| 2026-04-24 | "GETCHA!" cover | — |
| 2026-09-19 PDT | At Myth's 6th-anniversary 3D live "Seasons From Within" the two sang a duet cover of "September" | Setlist, secondary [S7] |
**Dossier · Hard Facts (continuity):**
- "Drawn to Dawn": 2026-03-27/28, the Wiltern, Los Angeles; TakoTori's first concert.
- Kiara "fired" Ina over the 2020 chicken incident (a KFP bit).

Incoming claims continue in `myth4-incoming.md`.

### projects/holoen/research/qa/packets/myth4-incoming.md

# Audit packet: myth4 (incoming claims)

Snapshot: git fa69d71.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: nomanyo Inya'nis|hololive -Myth-|Ninomae Ina'nis|Drawn to Dawn|Kiara and Ina|Ina and Kiara|Octo'clock|TakoTori|Ina'nis|一伊那尓栖|Inya|Ina)(

### from AZKi
- `bible/characters/AZKi.md › [SW] Relationships`: Ninomae Ina'nis and Kronii: R.E.P.O.
- `bible/characters/AZKi.md › Background Timeline`: | 2025-07-19 | R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora, Ina, IRyS and Kronii (the description's lineup) | [AZ4 _gZdFTluxtc] |
- `bible/characters/AZKi.md › Relationship Map`: | Ninomae Ina'nis, Ouro Kronii, IRyS | — | R.E.P.O. "JP & EN" (2025-07-19); Elizabeth was not in it | [AZ4 _gZdFTluxtc] |

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Background`: Her first original song, "Wind-Up," which she composed and wrote, was the first Justice solo at the 2025 English concert, where she also played violin in "SHALLYS" with Ina and FUWAMOCO and sang "I'm Your Treasure Box" with Bijou and Raora.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Ninomae Ina'nis: a joking rival; Stranger of Paradise, and "SHALLYS" with FUWAMOCO on stage.
- `bible/characters/Cecilia-Immergreen.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice; "Wind-Up," the first Justice solo; "SHALLYS" with Ina and FUWAMOCO (on violin); "I'm Your Treasure Box" with Bijou and Raora | [Official CI5] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Ninomae Ina'nis | Senior; a joking rival (secondary accounts) | Stranger of Paradise (2025); Rabbit and Steel with Bijou and Gigi (2024); "SHALLYS" on stage She framed a May 2026 music-making stream as preparing a tune for her rival's approaching birthday (title wording; Ina's participation not established). | [Observed CI2, CI3] [Official CI5] [Archive metadata NEW-R4-011] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | FUWAMOCO (both twins) | Advent | With Gigi, guest-hosted FUWAMOCO MORNING #167 (secondary); "SHALLYS" with Ina at -All for One-; the twins had hoped for a robot-maid member before she debuted | [Observed CI2; Mococo file] [Official CI5] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Nekomata Okayu, Hoshimachi Suisei, Nakiri Ayame | JP seniors | Listed with Ina and IRyS among the members of Okayu's 2025 New Year Game Festival team (archived team listing) | [Okayu file OK4] [Ayame file AY5] |

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Groups`: hololive -Myth- (graduated), hololive alum, Myth, hololive English (former branch name)
- `bible/characters/Gawr-Gura.md › [SW] Background`: Gura is a VTuber and a hololive alum: she graduated from hololive -Myth- on May 1, 2025.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina."
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate; fellow member of the official unit UMISEA (2021, with Aqua and Marine; the wiki also lists Chloe) | Ina drew chibi Bloop and warns that anyone who makes Gura cry faces "the wrath of Ina"; co-op games The final Myth relay's Gang Beasts segment ran on Ina's channel (reported 2025-04-30). | [Observed G2 §Gura's antics and §Mascots and fans; G16] [Official G17] [Secondary NEW-R1-017] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Houshou Marine, Sakamata Chloe | UMISEA (official 2023 roster: Aqua, Marine, Chloe, Gura, Ina) | "SHINKIRO" with Marine (anime MV on Marine's channel, 2023-11-12, credited to both; the "GuraMarine" pair name is wiki-listed only) | [Marine file MA4 9ehwhQJ50gs] [Official UMISEA roster] |

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Background`: "Countach" with Hakos Baelz and Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, "III" with Nerissa).
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Ouro Kronii: Fatal Fury and Hytale; "MONSTER" with Kronii, Ina and Shiori.
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa | [Official GG5] |

### from Hakos Baelz
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Ninomae Ina'nis: a K/DA cover and an art lesson.
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Ninomae Ina'nis | Myth senior | Archived metadata: the K/DA "POP/STARS" cover with Moona and Ayunda Risu (2023), a BAE-CADEMY art lesson with "Ina-sensei" (2024) and Ina's AmiAmi special featuring Bae (2025); World Tour '24 together | [Observed HB3; HB8] [Official HB6] |

### from Hoshimachi Suisei
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Ninomae Ina'nis and Gawr Gura (graduated): "BIBBIDIBA" with Moona at that concert; Gura and Usada Pekora were fellow featured talents in the July 5, 2024 hololive night collaboration with the Los Angeles Dodgers.
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Nekomata Okayu: "MOMAS"; Okayu's 2025 New Year Game Festival team with Nakiri Ayame, Ina, IRyS and Cecilia, among others.
- `bible/characters/Hoshimachi-Suisei.md › Background Timeline`: | 2024-08-24/25 | "High Tide" with IRyS, Moona and Hakos Baelz, and "BIBBIDIBA" with Moona, Ina and Gura, at the English concert -Breaking Dimensions- | [Official SU8] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Gawr Gura (graduated) | hololive night | The three faces of hololive night at Dodger Stadium with Pekora (2024); "BIBBIDIBA" with Moona and Ina at -Breaking Dimensions- (2024) | [Official SU7, SU8] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Ninomae Ina'nis | — | "BIBBIDIBA" with Moona and Gura at -Breaking Dimensions- (2024); Okayu's 2025 New Year Game Festival team (secondary) | [Official SU8] [S1] |

### from Houshou Marine
- `bible/characters/Houshou-Marine.md › [SW] Background`: Archived metadata records her with the English cast as Kiara's first HOLOTALK guest (2020), on Calli's first English lesson (2022), at an off-collab house party with Calli and Bae (2023), in off-collabs with FUWAMOCO and Nerissa (2024) and as a guest at Ina's "Pleides"
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Ninomae Ina'nis and Gawr Gura (graduated): UMISEA; English lesson #01 with Ina and a guest spot at Ina's "Pleides"
- `bible/characters/Houshou-Marine.md › Background Timeline`: | 2022-02-19 | Calli's HOLO ENGLISH LESSON #01 with Ina and Fubuki | [MA5 bfUEbp3xk4o] |
- `bible/characters/Houshou-Marine.md › Background Timeline`: | 2024 | 3 million subscribers (01-10, secondary); album "Ahoy!! You're All Pirates♡!" (10-16); a Touhou off-collab with FUWAMOCO (04-30) and Mario Party with FUWAMOCO and Nerissa; a solo concert (12); a guest at Ina's "Pleides" (12-28) | [Observed MA2] [MA5 x7gRHgQ0yI0, FLL7e1-RPGo, 3n9igJnSXtQ] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Minato Aqua (graduated) | UMISEA | The ocean unit's official roster: Aqua, Marine, Chloe, Gura and Ina | [Official UMISEA roster] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Ninomae Ina'nis, Gawr Gura (graduated) | UMISEA | English lesson #01 with Ina (2022); a guest at Ina's 3D live "Pleides" (2024); "SHINKIRO" with Gura (anime MV 2023-11-12, credited "宝鐘マリン・Gawr Gura") | [MA5 3n9igJnSXtQ] [MA4 9ehwhQJ50gs] |

### from IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her.
- `bible/characters/IRyS.md › [SW] Relationships`: Koseki Bijou ("Biboo"): her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina they starred at hololive night at Dodger Stadium (2025).
- `bible/characters/IRyS.md › Voice Profile`: - Measured (R20; 2026 chat and a Resident Evil Requiem window): median pitch about 214–226 Hz, mid-range in this project's sample (close to Ina's 223–232 Hz), and fast in chat: about 168–183 words per minute of speech (121 in the opening, 67 in the horror game). Sample results only.

### from Kikirara Vivi
- `bible/characters/Kikirara-Vivi.md › [SW] Background`: Archived metadata records her with the English cast in R.E.P.O. with FUWAMOCO and Bae (2025-05-25), in a separate R.E.P.O. session on Ina's stream (2025-06-02) and in Mumei's Gartic Phone collaboration with Noel, Kronii, Ina and Elizabeth (2025); a secondary archive records FUWAMOCO and Bijou watching FLOW GLOW's debut.
- `bible/characters/Kikirara-Vivi.md › [SW] Relationships`: Ninomae Ina'nis: a separate R.E.P.O. session on Ina's stream (2025-06-02) and the Gartic Phone collab.
- `bible/characters/Kikirara-Vivi.md › Voice Profile`: - **Language:** streams in Japanese (a voice feature only); archived metadata records R.E.P.O. with FUWAMOCO and Bae (2025-05-25), a separate R.E.P.O. session on Ina's stream (2025-06-02) and Mumei's Gartic Phone collab with Noel, Kronii, Ina and Elizabeth (2025). [VI5]
- `bible/characters/Kikirara-Vivi.md › Background Timeline`: | 2025-04-14 | Gartic Phone EN + ID + JP collab with Mumei, Kronii, Ina, Elizabeth and Noel | [VI5 OMDzBQohAf8] |
- `bible/characters/Kikirara-Vivi.md › Background Timeline`: | 2025-06-02 | R.E.P.O. on Ina's stream, with Polka, Watame, Flare and Anya | [VI5 grBU9Dl09Ds description] |
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Ninomae Ina'nis | — | R.E.P.O. (2025-06-02); Gartic Phone (2025) | [VI5] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Background`: (2025), starred with Ina and IRyS at hololive night at Dodger Stadium (2025), sang a solo and two group numbers at the 2025 English concert -All for One-, and was paired with Takanashi Kiara at the 2026 Serendipity concert.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: IRyS: her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina, they headlined hololive night at Dodger Stadium (2025).
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Ninomae Ina'nis: "TakoRocky,"
- `bible/characters/Koseki-Bijou.md › Voice Profile`: - Secondary: she discovered she can imitate Ina by pitching her voice down with a voice changer. [Observed KB2 §Miscellaneous, secondary]
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-07-05 | hololive night at Dodger Stadium with Ina and IRyS: a stadium sing-along and the first VTuber stream from the stadium | [Official KB9] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Ninomae Ina'nis | Senior ("TakoRocky") | Monster Hunter (2023–2025); Ina designed their Monster Hunter Wilds collab outfits (2025-12) Monster Hunter Wilds outfit project: Bijou chose Gore Magala, Ina Nu Udra. | [Observed KB3; X post via wiki] [Secondary, Siliconera interview] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Nekomata Okayu | JP senior | Credited participants together (with Kiara, Ina, Kobo and Todoroki Hajime) in the official purple-themed 3D variety program #パープル争奪戦 (2026-07-23). | [Archive metadata NEW-R3-008] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Nakiri Ayame: the 7th fes. stage with Okayu and Ina (2026).

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Groups`: hololive, hololive -Myth-, Myth, CHADCast, hololive English (former branch name), Last Writes
- `bible/characters/Mori-Calliope.md › [SW] Background`: She debuted first in hololive -Myth- in September 2020; her fans are the Dead Beats, her mentor is Death Sensei, her publicly depicted cat mascot is Tutu, and her scythe is named Ricky.
- `bible/characters/Mori-Calliope.md › [SW] Background`: She headlined New Underworld Order in Tokyo and GriMoire at the Hollywood Palladium, the first solo concert outside Japan by a hololive production talent, and in 2026 she released her album DISASTERPIECE, held her sixth birthday 3D live "UNCUT ROCK!!" with a live band, and sang with Kiara and Ina at Myth's 6th-anniversary 3D live, which premiered the Myth song "THIS IS MYTH."
- `bible/characters/Mori-Calliope.md › [SW] Background`: Myth still includes Takanashi Kiara and Ninomae Ina'nis; Gawr Gura has graduated, and Watson Amelia is an affiliate.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote lyrics for Ina's TAKO∞TAKOVER and is a recurring target of Ina's puns.
- `bible/characters/Mori-Calliope.md › Voice Profile`: - Measured (C30, chat windows): median pitch 197–214 Hz, the second lowest of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz). The wiki's hololive-wide ranking was not measured. She is the fastest talker of the six: about 161–186 words per minute of speech while chatting (Kronii 120–127, Ina 81–95). Approximate values for relative comparison.
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2026-09-07 | The branches merge into one "hololive." Her unit is now hololive -Myth-. | [Official C17, C1] |
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2026-09-19 PDT | Myth 6th Anniversary 3D LIVE "Seasons From Within" with Kiara and Ina; the Myth song "THIS IS MYTH" premieres | [Archive metadata C33] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate | Ina designed Death Sensei. Calli wrote the lyrics for Ina's TAKO∞TAKOVER. [Unverified, title only: a running bit of a shinigami afraid of a tako] | [Observed C4 §Mascot and fans, secondary] [Official C28] [C21-eRObYMLdPfw clip title] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Houshou Marine, Shirogane Noel, Shishiro Botan | JP seniors | HOLO ENGLISH LESSON #01 with Marine, Ina and Fubuki (2022-02-19); Mario Kart with Marine, Bae and Reine (2021-12-25); a house-party off-collab with Marine and Bae and a playthrough of Marine's horror game (2023-08-14); HOLOYOI #02 with Noel and Flare (2023-04-20) and #03 with Botan and Subaru (2023-05-18) | [S1 bfUEbp3xk4o, Tpzbfccp_ZM, DY5VThfehW8, Mf-sAjsuSig, wyrLR1CC1Co, EatMZc1N3VM] |
- `bible/characters/Mori-Calliope.md › Hard Facts`: - Birthday April 4 (4/4: "shi" is also "death"). Height 167 cm. Debut 2020-09-12. Unit: hololive -Myth-. [Official C1] [Observed C4 §Miscellaneous, secondary]
- `bible/characters/Mori-Calliope.md › Hard Facts`: - Fans: Dead Beats. Fan mark 💀. Mascot: Death Sensei (designed by Ina). Scythe: Ricky. Cat on her model: Tutu. [Official C1] [Observed C4 §Mascot and fans and §Personality, secondary]

### from Nakiri Ayame
- `bible/characters/Nakiri-Ayame.md › [SW] Background`: With the English cast, archived metadata identifies her as Kiara's 23rd HOLOTALK guest (2022-10-09), places her on the 2023 Sports Festival white team with Kiara, Mumei, Ame, Nerissa and AZKi (her stream title celebrates its win), and lists her with Suisei, Ina, IRyS and Cecilia among the members of Okayu's 2025 New Year Game Festival team; she shared 7th fes STAGE 1 with Ina and FUWAMOCO (2026), and the official Anime NYC 2026 announcement listed her, Fubuki and Mio for an August 22 convention-exclusive stream.
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: Hoshimachi Suisei, Ninomae Ina'nis, IRyS and Cecilia Immergreen: listed among the members of Okayu's 2025 New Year Game Festival team; Ina and FUWAMOCO shared her 7th fes stage.
- `bible/characters/Nakiri-Ayame.md › Background Timeline`: | 2025-01-13 | On Okayu's team at the New Year Game Festival (with Suisei, Ina, IRyS, Cecilia) | [AY5 THMIBrxnp-E] |
- `bible/characters/Nakiri-Ayame.md › Background Timeline`: | 2026-03-06 | hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Okayu, Ina, FUWAMOCO) | [Official AY6] [Observed AY3] |
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | Ninomae Ina'nis, IRyS, Cecilia Immergreen | — | Okayu's 2025 team; Ina and FUWAMOCO on 7th fes STAGE 1 | [AY5] [Official AY6] |
- `bible/characters/Nakiri-Ayame.md › Story Engine`: 3. An FPS night with Ina and IRyS where Ayame calls out positions in Japanese faster than anyone can follow.

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Ninomae Ina'nis: fellow artist, drawing collabs.
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Ninomae Ina'nis | Myth senior, fellow artist | Drawing collabs (2023-01, 2025-04-21 "doodles with @NinomaeInanis") | [Observed M3] |

### from Nekomata Okayu
- `bible/characters/Nekomata-Okayu.md › [SW] Background`: With the English cast she released "Kurukuru Cruise" with Ninomae Ina'nis (2025); secondary accounts document her appearing with Korone in FUWAMOCO's 3D debut (2024), and the twins hosted a 2025 watch-along of her concert.
- `bible/characters/Nekomata-Okayu.md › [SW] Background`: Archived stream metadata documents her as Kiara's 18th HOLOTALK guest (2021), a guest at Mumei's 3D live (2024), a pop-up Mario Party with Calli, Anya and Ao (2024) and her 2025 New Year Game Festival team with Ina, IRyS and Cecilia among its members.
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Ninomae Ina'nis: their pairing is called "TakoNeko" in secondary references; they released "Kurukuru Cruise" together (2025) and were teammates at the 2025 New Year Game Festival.
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2025-01-13 | Leads a team at the hololive New Year Game Festival (with Suisei, Ayame, Ina, IRyS, Cecilia) | [OK4 THMIBrxnp-E] |
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2025-08-05 | "Kurukuru Cruise" with Ninomae Ina'nis (official digital release; a video premiere may be dated a day earlier) | [Official OK7] [OK5 t7lNu-p_ANs] |
- `bible/characters/Nekomata-Okayu.md › Background Timeline`: | 2026-03-06 | hololive 7th fes. "Ridin' on Dreams," STAGE 1 (with Ayame, Ina, FUWAMOCO) | [Official OK6] [Observed OK3] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Ninomae Ina'nis | "TakoNeko" (secondary) | "Kurukuru Cruise" (2025); Ina on her 2025 New Year Game Festival team; both on 7th fes STAGE 1 | [OK5] [OK2] [Official OK6, OK7] |
- `bible/characters/Nekomata-Okayu.md › Story Engine`: 2. Ina and Okayu rehearse "Kurukuru Cruise" and Okayu agrees with every note change.

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Ninomae Ina'nis: on her Tomodachi Life island with IRyS.
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | IRyS | Senior and fellow singer | Guest at Nerissa's 2025 3D concert ("Missing Promise"); Monster Hunter Wilds (2025); Nerissa made Miis of Ina and IRyS in Tomodachi Life (2026) | [Observed N3 titles] |

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Groups`: hololive, hololive -Promise-, Promise, Council (former unit name), Octo'clock
- `bible/characters/Ouro-Kronii.md › [SW] Background`: In 2026 she also began a performance partnership with Ninomae Ina'nis.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "Just two punny people," and both speak Korean.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: "JP & EN" with Ina and IRyS (2025).
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Shiori Novella: "Rating Your Clocks" together (2025) and "MONSTER" with Ina and Gigi on stage (2025).
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Dad puns and time puns; she trades puns with Ina. [Official K4] [Observed K22]
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Korean: she speaks it fluently, a language she shares with Ina [Observed K8 §Miscellaneous, secondary]; a language exchange with Kiara is reported by a clip title [Unverified, K17]. Rare outside those exchanges (estimate).
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Colleagues: by name or short form (Ina, Bae, IRyS).
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Measured (K36, chat windows): median pitch 177–188 Hz, the lowest of the six files measured the same way (Calli 197–214 Hz; Gura and Ame about 250–270 Hz); about 120–127 words per minute of speech, mid-paced (Calli 161–186, Ina 81–95). Approximate values for relative comparison.
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - **Stage host (official interview, 2026-06):** she recalls enjoying an earlier concert MC segment with Ina and anticipates the audience's response to their unit entrance. Scene direction (proposed): as emcee she actively invites audience participation. [Official NEW-R2-008]
- `bible/characters/Ouro-Kronii.md › Background Timeline`: | 2026-06-04 | Serendipity interview and partnership with Ina | Puns, appreciation, performance goals [Official K4] |
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Ninomae Ina'nis | Serendipity partner (2026); longtime friend | They trade puns; both speak Korean | [Official K4] [Observed K8 §Miscellaneous, secondary] |

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › [SW] Background`: "Neko Kaburi-Na" with Ina, Shiori and Oozora Subaru, and "I'm Your Treasure Box" with Bijou and Cecilia.
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Ninomae Ina'nis, Shiori Novella and Oozora Subaru (JP): "Neko Kaburi-Na" on stage; Puyo Puyo Tetris 2 with Ina.
- `bible/characters/Raora-Panthera.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, solo "Gacha x Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and guest Oozora Subaru, "I'm Your Treasure Box" with Bijou and Cecilia | [Official RP5] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Ninomae Ina'nis | Myth senior | Puyo Puyo Tetris 2 (2025); the Monster Hunter Wilds launch with Gigi and Bijou; "Neko Kaburi-Na" with Shiori and Oozora Subaru at -All for One- | [Observed RP3] [Official RP5] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Shiori Novella, Oozora Subaru (JP) | Advent senior; JP senior | "Neko Kaburi-Na" with Ina at -All for One- (2025) | [Official RP5] |

### from Sakamata Chloe
- `bible/characters/Sakamata-Chloe.md › [SW] Relationships`: Ninomae Ina'nis and Gawr Gura (graduated): UMISEA (official 2023 roster).
- `bible/characters/Sakamata-Chloe.md › Relationship Map`: | Ninomae Ina'nis, Gawr Gura (graduated) | UMISEA | The ocean unit's official 2023 roster: Aqua, Marine, Chloe, Gura and Ina | [Official UMISEA roster https://hololivesummer2023.hololivepro.com/unit/umisea/] |

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Ouro Kronii: they hosted "Rating Your Clocks" together (2025) and sang "MONSTER" with Ina and Gigi at the 2025 concert.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Ninomae Ina'nis: a "Rate Your Fears" nightmare talk.
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Ninomae Ina'nis | Senior | "Rate Your Fears: Nightmare Discussion" (2024-04-24) | [Observed SN3] |

### from Shirogane Noel
- `bible/characters/Shirogane-Noel.md › [SW] Background`: Archived metadata records her with the English cast as Kiara's 22nd HOLOTALK guest (2022), a guest with Flare on Calli's HOLOYOI #02 (2023), a participant with FUWAMOCO and Bae in a team Mario Kart event (2023) and in Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (2025); FUWAMOCO danced to "TREVIAN KNIGHT."
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone EN + ID + JP (2025).
- `bible/characters/Shirogane-Noel.md › Background Timeline`: | 2025 | #ノエこよ Power Pros exhibition with Koyori (01-10); Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (04-14); 3rd-gen R.E.P.O. with Marine, Pekora and Flare (07-05); Elden Ring Nightreign with Flare and Pekora; an Audio-Technica collab with Ayame (07-11); "TREVIAN KNIGHT" (official digital release 08-16), which FUWAMOCO danced to (09-30) | [NO4] [NO5] [Official music 622] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii, Elizabeth Rose Bloodflame | — | Gartic Phone EN + ID + JP (2025) | [NO5] |

### from Shishiro Botan
- `bible/characters/Shishiro-Botan.md › [SW] Background`: Archived metadata and secondary concert reports record her with the English cast in Left 4 Dead 2 (2022) and an Overwatch 2 team (2023) with IRyS, on Calli's HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and as a guest at Ina's birthday 3D live "EVERMORE"
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: Ninomae Ina'nis: a guest at Ina's birthday 3D live "EVERMORE"
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: (2025), singing "storia" with Ina and Watame per a secondary set list.
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2025 | 1.5 million subscribers (02-14, secondary); originals "Simulacre," "Gaotteko!" and "boundary"; a guest at Ina's birthday 3D live "EVERMORE" (05-21), singing "storia" with Ina and Tsunomaki Watame per a secondary set list; the first "#ホロ金策サバイバル" | [Observed BO2] [BO5] [EVERMORE report] [ASR BO20] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Ninomae Ina'nis | — | A guest at Ina's birthday 3D live "EVERMORE" (2025); "storia" with Ina and Watame (secondary set list) | [BO5 I-J11Da5ONY] [EVERMORE report] |
- `bible/characters/Shishiro-Botan.md › Story Engine`: 2. Ina invites Botan back to a live, and Botan plans the whole stage logistics without being asked.

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Rocku Wawa
- `bible/characters/Takanashi-Kiara.md › [SW] Background`: She debuted with hololive -Myth- in September 2020 speaking English, Japanese and German.
- `bible/characters/Takanashi-Kiara.md › [SW] Background`: She released her second album Vogelfrei in 2026 and held the duo concert Drawn to Dawn with Ninomae Ina'nis in Los Angeles, a birthday 3D live in July, and Myth's 6th-anniversary 3D live with Calli and Ina, which premiered the Myth song "THIS IS MYTH."
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal.
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: 3. "So actually, tomorrow, Calli, Ina, Wawa…" (ASR T23, 2:39:41; she goes on to "lots of people in Hytale")
- `bible/characters/Takanashi-Kiara.md › Appearance Anchors`: - Mascot: Kotori, a little bird designed by Ina. Two "phoenix cats," Chonkers (orange) and Smoothie (turquoise), appear as model accessories; they stay off the card. [Observed T2 §Mascot and fans, secondary]
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2026-03-27/28 PDT | "Drawn to Dawn" duo concert with Ina (The Wiltern, Los Angeles) | [Official T11, T12] |
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2026-09-07 | Branches merge; unit is hololive -Myth- | [Official T20, T1] |
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2026-09-19 PDT | Myth 6th Anniversary 3D LIVE "Seasons From Within" with Calli and Ina; "THIS IS MYTH" premieres | [Archive metadata T25] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate ("TakoTori") | Duo concert 2026; Kiara "fired" Ina over the 2020 chicken incident.  | [Official T11, T12] [Observed T2 §KFP; T22 §Personality, secondary] |
- `bible/characters/Takanashi-Kiara.md › Hard Facts`: - Birthday July 6; height 165 cm; debut 2020-09-12; unit hololive -Myth-; illustrator huke. [Official T1]

### from Takane Lui
- `bible/characters/Takane-Lui.md › Behavioral Traits`: 2. Dad jokes, like Ina and Kronii. [Observed LU2 §Personality, secondary]

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Groups`: hololive (affiliate), hololive -Myth- (affiliate), Myth, hololive English (former branch name)
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her.
- `bible/characters/Watson-Amelia.md › Voice Profile`: - "Ina... prepare to get FUCKED!" (a PvP threat; censored in source and in clip A14's title)
- `bible/characters/Watson-Amelia.md › Voice Profile`: - **How she addresses people:** "you guys" by default; "chat" occasionally; "Teamates" (one m, official) on big occasions; members "Investigators." Members by name ("Gura," "Calli," "Ina," "Kiara," "Kronii"); Bubba, her dog mascot. She gives her name in English order, "Amelia Watson." [Official A1] [Observed A3 captions; A2 §Mascots and fans]
- `bible/characters/Watson-Amelia.md › Voice Profile`: - Measured (A23; Mario, VALORANT and 2024 chat windows, with game audio mixed in): median pitch about 248–276 Hz; about 114–133 words per minute of speech. For comparison only, Calli's chat windows measured 161–186 and Ina's 81–95. Sample results; they do not establish a general ranking. [ASR A23]
- `bible/characters/Watson-Amelia.md › Appearance Anchors`: - Mascot: Bubba, a small dog designed by Ina. [Observed A2 §Mascots and fans]
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate and gaming collaborator | Ina designed Bubba; Ame can aim blunt competitive taunts at her ("Ina... prepare to get fucked!", a PvP threat; wording inferred from a censored title) | [Observed A2 §Mascots and fans and §Quotes; A14] |

### from Yukihana Lamy
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: Archived metadata records her with the English cast at Ina's Minecraft festival and a Minecraft collab billed as a "date"
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: (2021), and as a guest at Ina's 3D live "Pleides"
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: Ninomae Ina'nis: a Minecraft festival and a Minecraft collab billed as a "date"
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: (2021), and a guest at Ina's 3D live "Pleides"
- `bible/characters/Yukihana-Lamy.md › Voice Profile`: - **Language:** streams in Japanese; archived metadata records her at Ina's Minecraft festival and a Minecraft collab billed as a "date" (2021) and as a guest at Ina's 2024 3D live. [LM5]
- `bible/characters/Yukihana-Lamy.md › Background Timeline`: | 2021 | Ina's Usaken Summer Festival (06-27) and an EN-server Minecraft "date" with Ina (10-20) | [LM5] |
- `bible/characters/Yukihana-Lamy.md › Background Timeline`: | 2024 | Originals "Hatsukoi Pâtissière," "Watashi wo amayakasunara" and "Lamy's Baribari Workout"; a guest at Ina's 3D live "Pleides" (12-28) | [Observed LM2] [LM5] |
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | Ninomae Ina'nis | — | A Minecraft festival appearance and a Minecraft collab billed as a "date" (2021); a guest at Ina's "Pleides" 3D live (2024) | [LM5 a7CvRf4vFYc, Isp3UhgOAB4, 3n9igJnSXtQ] |
- `bible/characters/Yukihana-Lamy.md › Story Engine`: 1. Lamy hosts a "Snack Yuki no Hana" night and Ina draws the regulars.

### from Advent Pairs
- `bible/world/Advent-Pairs.md › [SW] Description`: With seniors: Mori Calliope starred in Bijou's Undertale mod and did a 24-hour charity stream with her, shares "FUWAMOCALLI" with the twins (a collaboration name they say they particularly like), and was Shiori's 2026 concert partner; Kiara hosted all five on HOLOTALK, encouraged Bijou through hard choreography, and partnered her in 2026 ("Rocku Wawa"); IRyS is Bijou's horror co-op partner, and Bijou, Ina and IRyS starred at hololive night at Dodger Stadium (2025); Shiori and Kronii hosted "Rating Your Clocks" together in March 2025.
- `bible/world/Advent-Pairs.md › With Myth`: - **Ninomae Ina'nis:** "TakoRocky" with Bijou (Monster Hunter; Ina designed their 2025 Monster Hunter Wilds outfits); "Rate Your Fears" with Shiori (2024); "SHALLYS" with FUWAMOCO and Cecilia at the 2025 concert; with Bijou and IRyS, starred at hololive night at Dodger Stadium (2025-07-05). [Observed S1; X post via wiki] [Official S5, S8]
- `bible/world/Advent-Pairs.md › With Promise`: - **IRyS:** Bijou's horror co-op partner (Dead Space 3, Resident Evil 6, 2026); "Please carry me Senpai!!" in Overwatch (2023); hololive night at Dodger Stadium with Bijou and Ina (2025-07-05); Monster Hunter Wilds and PEAK with Shiori (2025). [Observed S1] [Official S8]
- `bible/world/Advent-Pairs.md › With Promise`: - **Ouro Kronii:** "WatchDog" with FUWAMOCO; Shiori and Kronii hosted "Rating Your Clocks" together (2025-03-27, AjwIazuu8gg; the description credits help with collecting submissions); "MONSTER" with Ina, Shiori and Gigi at the 2025 concert. [Observed S1] [Official S5]
- `bible/world/Advent-Pairs.md › History`: | 2025-07-05 | hololive night at Dodger Stadium: Bijou with Ina and IRyS | [Official S8] |

### from Concerts and Live Events
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: Los Angeles, July 3–4, built on units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia), with guests Ookami Mio, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame singing alongside EN members); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet.
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn"
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); hololive night at Dodger Stadium with Ina, IRyS and Bijou (2025-07-05); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!"
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous"; Promise's unit song "Our Promise"; "BLUE CLAPPER" by the CHADCast trio (Calli, IRyS, Bae) with Bijou; Bae's solo "GEKIRIN"; "High Tide" by IRyS, Bae, Moona Hoshinova and Hoshimachi Suisei [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; "R x R x R" by Calli and Bae; "Countach" by Bae, Gigi and guest Kureiji Ollie; Bae's solo "La Roja (Arrange ver.)"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before and separate from "-Breaking Dimensions-"), Jakarta (11-09), Singapore (11-30, with a pre-concert panel of Kaela Kovalskia and Ouro Kronii), Atlanta (12-15, a panel of Nerissa and Elizabeth Rose Bloodflame), Kuala Lumpur (12-21, Nerissa and Elizabeth again) and Taipei (2025-01-18, the finale) [Official S7]; and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive night at Dodger Stadium (2025-07-05, Los Angeles):** the second hololive–Dodgers collaboration, starring Ina, IRyS and Bijou, with a stadium sing-along during the game. [Official, https://hololive.hololivepro.com/en/news/20250731-01-353/]
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Takanashi Kiara | 4th-anniversary live "MIRAGE" (2024-10-06); "KIARA & FRIENDS: H!P Cover Song Spring Concert" (2025-04-21); "Drawn to Dawn" with Ina (2026-03-27/28 PDT, The Wiltern); World Tour '24 performer; Serendipity with Bijou; birthday 3D live (2026-07-06 PDT); "Seasons From Within" | Kiara file T11, T12, T10; S3 titles |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ninomae Ina'nis | 3D live "Pleiades" (2024-12-28); "Drawn to Dawn" with Kiara; World Tour '24 performer; Serendipity with Kronii; "Seasons From Within" | Ina file I20, I7; S3 title |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ouro Kronii | World Tour '24 Singapore pre-concert panel with Kaela Kovalskia; World Tour '25 Sydney guest; 3D birthday live "The Goddess Descends" with a new outfit (2026-03-13/14, Ame as guest); Serendipity with Ina | Kronii file K33, K4; S1 |
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 4. An aftertalk where Kiara and Ina disagree about who cried first at "Drawn to Dawn."

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and released "Kurukuru Cruise" with Nekomata Okayu (2025).
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ninomae Ina'nis:** an artist among artists: the ocean unit UMISEA (formed 2021 with Minato Aqua, Houshou Marine and Gura; Chloe joined later; Aqua and Gura have graduated and Chloe is an affiliate, so the unit is history more than a current lineup); "HoloJEI" (Tsunomaki Watame, Kureiji Ollie, Anya Melfissa); "TakoBazo" (Vestia Zeta); "TakoNeko" (Nekomata Okayu, a secondary pair name; "Kurukuru Cruise," 2025; see "JP Senpai Pairs"); Shiranui Flare appeared on her 2025 AmiAmi special ("Flare?!!?"). She admires Marine as an artist. [Observed S1; S2 Ina; Ina file]

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › History`: | 2025-08-23/24 | -All for One-: "HOT DUCK!" with Bijou and Subaru; their version of "Howling"; "Lifetime Showtime"; "SHALLYS" with Ina and Cecilia | [Official S5] |

### from Fauna and Mumei Pairs
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Mumei also drew with Ina, did "Anatomy Review" with Calli, played with Ame in Ame's last regular week, and held "emo hours" with Nerissa; at the 2024 concert Mumei sang with Kiara and Nerissa, and Fauna with Shiori and Nerissa.
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Ina:** fellow artists; Mumei's drawing collabs with Ina (2023-01; "doodles with @NinomaeInanis," 2025-04-21). [Observed S1]

### from Hakos Baelz Pairs
- `bible/world/Hakos-Baelz-Pairs.md › With Myth`: - **Ninomae Ina'nis:** the K/DA "POP/STARS" cover with Moona and Ayunda Risu (2023); a BAE-CADEMY art lesson with "Ina-sensei" (2024); Ina's AmiAmi special featuring Bae (2025-05-29); World Tour '24. [S1] [Official S5]
- `bible/world/Hakos-Baelz-Pairs.md › History`: | 2023 | a BaeRyS off-collab; "Daikirai na Hazu Datta"; K/DA "POP/STARS"; We Were Here | BaeRyS; Bae–Ina; BaeBi |

### from IRyS and Nerissa Pairs
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Other Names`: MorIRyS, CHADCast, KiaRissa, IRyS and Kronii, IRyS and Ina, Nerissa and Calli, Nerissa and IRyS
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: IRyS and Ina: an early duo (It Takes Two, "It Takes Tako & Hope") who still play together.
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: Nerissa and IRyS: two singers; IRyS guested at that concert, and Nerissa put IRyS and Ina in Tomodachi Life.
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Rules`: Recent pairings (IRyS with Kronii, Calli and Ina; Nerissa with Kiara and Calli) carry the most weight; pairs with Gura are memories.
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Ina** (15 / 7 / 3 / 4 / 6 / 0): an early duo ("Keep Talking and Nobody Explodes," 2021-07-31; "It Takes Two," three parts, "It Takes Tako & Hope," 2021); a Gundam watchalong (2023-03-25); IRyS as guest on Ina's "AmiAmi March Special" (2025-03-18); Elden Ring Nightreign, which IRyS titled "Third Wheeling" (2025-06-24); guildmates ("Cerulean Cup," with Kronii, Bijou and Gigi) in the ENigmatic Recollection Minecraft story. [Observed S1 titles; S2 §Units, secondary]
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Ame** (11 / 2 / 3 / 2 / 0 / 0) and **IRyS and Gura** (11 / 6 / 0 / 1 / 0 / 0): mostly the 2021–22 full-EN collabs (Among Us, Dead by Daylight, Overwatch); IRyS joined Ina, Bae and Ame's "LOSER BUYS DINNER!!!!!" off-collab (2023-02-23). With Gura graduated and Ame an affiliate, these are memories. [Observed S1 titles]
- `bible/world/IRyS-and-Nerissa-Pairs.md › Nerissa`: - **Nerissa and IRyS** (1 / 0 / 3 / 1): the two singers: IRyS was a guest at Nerissa's 2025 3D concert ("Missing Promise"), they hunted together in Monster Hunter Wilds (2025-03-01), and in 2026 Nerissa made Miis of IRyS and Ina in Tomodachi Life ("Inya and Irys will be born!", 2026-04-23). [Observed S1 titles]
- `bible/world/IRyS-and-Nerissa-Pairs.md › History`: | 2026-04-23 | Nerissa's Tomodachi Life Miis of IRyS and Ina | — |
- `bible/world/IRyS-and-Nerissa-Pairs.md › Conflicts and Story Hooks`: 5. Nerissa's Tomodachi Life island makes IRyS and Ina's Miis do something strange.

### from JP Senpai Pairs 2
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Other Names`: Marine and Kiara, Noel and Calliope, Lamy and Ina, Botan and IRyS, Vivi and FUWAMOCO
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: Marine was the first guest of Kiara's talk show HOLOTALK (2020), joined Calli's first English lesson with Ina (2022), played Mario Kart with Calli and Bae (2021) and joined their house-party off-collab (2023), joined off-collabs with FUWAMOCO and Nerissa (2024), and was a guest at Ina's 3D live "Pleides"
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: (2024); Calli, and Bae with Mumei, played "Truth of Beauty Witch," a horror game featuring Marine (2023); Marine, Ina and Gura were in the ocean unit UMISEA.
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: Lamy joined Ina's Minecraft festival and a "date"-billed Minecraft stream (2021) and her 3D live (2024).
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: Botan played Left 4 Dead 2 and Overwatch 2 with IRyS, was on HOLOYOI and Bae's BAE-GEMITE DOMINATION with Oozora Subaru (2023), and guested at Ina's 2025 birthday live.
- `bible/world/JP-Senpai-Pairs-2.md › [SW] Description`: Vivi, a FLOW GLOW member, played R.E.P.O. with FUWAMOCO and Bae and, separately, on Ina's stream, and Gartic Phone with Mumei, Kronii, Ina and Elizabeth (2025).
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Mori Calliope:** Calli's HOLO ENGLISH LESSON #01 with Ina and Fubuki (2022-02-19); Mario Kart with Bae and Pavolia Reine (2021-12-25); an off-collab "House Party with Marine & Bae" (2023-08-14); Calli played "Truth of Beauty Witch," the horror game featuring Marine, on her own stream (2023); dance shorts to Marine's songs. [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Ninomae Ina'nis, Gawr Gura:** UMISEA, the ocean unit (official 2023 roster: Minato Aqua, Marine, Sakamata Chloe, Gura and Ina); Calli's English lesson #01 (Ina); a guest at Ina's "Pleides" (2024); "SHINKIRO" with Gura (anime MV on Marine's channel, 2023-11-12, credited to both). The "GuraMarine" pair name is wiki-listed only. [Official UMISEA roster] [S1 9ehwhQJ50gs, 3n9igJnSXtQ] [S2 Marine §Relationships, secondary]
- `bible/world/JP-Senpai-Pairs-2.md › Shirogane Noel with the cast`: - **Nanashi Mumei, Ina, Kronii, Elizabeth (and Kikirara Vivi):** Mumei's Gartic Phone EN + ID + JP collab (2025-04-14). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Yukihana Lamy with the cast`: - **Ninomae Ina'nis:** archived metadata records Ina and Lamy's 2021 "Usaken Summer Festival" stream (06-27) and a separate EN-server stream billed as a "date" (10-20, the stream's own premise); secondary concert records and Ina's archived guest list put Lamy at Ina's 3D live "Pleides" (2024-12-28). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Shishiro Botan with the cast`: - **Ninomae Ina'nis:** a guest at Ina's birthday 3D live "EVERMORE" (2025-05-21), singing "storia" with Ina and Tsunomaki Watame per a secondary set list. [S1] [EVERMORE report]
- `bible/world/JP-Senpai-Pairs-2.md › Kikirara Vivi with the cast`: - **Ninomae Ina'nis:** R.E.P.O. with Polka, Watame, Flare and Anya (2025-06-02). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Kikirara Vivi with the cast`: - **Mumei, Kronii, Ina, Elizabeth:** Mumei's Gartic Phone EN + ID + JP collab (2025-04-14). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › History`: | 2021 | Ina's Minecraft festival and EN-server "date" | Lamy, Ina |
- `bible/world/JP-Senpai-Pairs-2.md › History`: | 2024 | Off-collabs with FUWAMOCO and Nerissa; Ina's "Pleides" | Marine; Lamy, Marine |
- `bible/world/JP-Senpai-Pairs-2.md › History`: | 2025 | Gartic Phone EN + ID + JP (04-14); #holoREPO (05-25); R.E.P.O. on Ina's stream (06-02); Ina's "EVERMORE" | Noel, Vivi; Vivi, Bae, FUWAMOCO; Vivi, Ina; Botan |

### from JP Senpai Pairs
- `bible/world/JP-Senpai-Pairs.md › [SW] Other Names`: AS_tar, FWMCAZ, TakoNeko, Suisei and Calli, Okayu and Ina, AZKi and FUWAMOCO, Ayame and Kiara
- `bible/world/JP-Senpai-Pairs.md › [SW] Description`: Suisei, AZKi, IRyS and Moona Hoshinova are the official unit Star Flower ("story time," 2022); Suisei sang "High Tide" with IRyS, Moona and Hakos Baelz and "BIBBIDIBA" with Moona, Ina and Gura at the 2024 English concert, and was a face of hololive night at Dodger Stadium with Gura and Pekora (2024).
- `bible/world/JP-Senpai-Pairs.md › [SW] Description`: Okayu and Ina released "Kurukuru Cruise"
- `bible/world/JP-Senpai-Pairs.md › Hoshimachi Suisei with the cast`: - **Mori Calliope ("Death Star," secondary):** Calli's own card describes her as starstruck by Suisei (secondary; the pair name and reaction stay here in the dossier). Calli's original "CapSule" with Suisei (2022-04-04) and Suisei's "Wicked feat. Mori Calliope" (single "TEMPLATE / Wicked," 2022); Suisei sang "Wicked" with Calli at Calli's first solo concert "New Underworld Order" (2022-07-21). Calli drew Suisei on stream (2021), watched Suisei's 2nd concert with Ina (2023-02-20), held a "Talkin' Live Shows" collab with her (2023-04-12) and watched the "Spectra of Nova" tour opener with FUWAMOCO and Elizabeth (2024-11-14). In a June 2026 chat Suisei mentioned having already talked about "the one with Calliope" among her recent stage appearances. [S1] [S2 Suisei §Relationships, secondary] [Suisei file SU20]
- `bible/world/JP-Senpai-Pairs.md › AZKi with the cast`: - **IRyS:** Star Flower (above); IRyS covered AZKi's "Inochi" (2021); Calli's "HOLO ENGLISH LESSON #03" with IRyS and Tsunomaki Watame (2022-03-12); an R.E.P.O. "JP & EN" collab with Shiranui Flare, Usada Pekora, Ina and Kronii (2025-07-19). [S1] [Official S3]
- `bible/world/JP-Senpai-Pairs.md › Nakiri Ayame with the cast`: - **Team events:** the 2023 hololive Sports Festival in Minecraft, white team (Ayame's stream description lists Kiara, Mumei, Ame, Nerissa and AZKi; its title celebrates the win); Okayu's team at the 2025 New Year Game Festival (with Suisei, Ina, IRyS and Cecilia). [S1]
- `bible/world/JP-Senpai-Pairs.md › Nakiri Ayame with the cast`: - **Shared billing:** 7th fes STAGE 1 with Ina and FUWAMOCO (2026-03-06); the official Anime NYC 2026 announcement listed her, Shirakami Fubuki and Ookami Mio for an August 22 convention-exclusive stream, the same day as streams by Kronii and Raora, FUWAMOCO, and Calli, Bijou, Nerissa and Kobo Kanaeru (a booking, not a location). [Official S5, S7]
- `bible/world/JP-Senpai-Pairs.md › Nekomata Okayu with the cast`: - **Ninomae Ina'nis ("TakoNeko," secondary):** they released "Kurukuru Cruise" together (official digital release 2025-08-05); both on Okayu's 2025 New Year Game Festival team and on 7th fes STAGE 1 (2026). [S1] [S2 Okayu §Relationships, secondary] [Official S5]
- `bible/world/JP-Senpai-Pairs.md › History`: | 2025-01-13 | New Year Game Festival, Okayu's team | Okayu, Suisei, Ayame with Ina, IRyS, Cecilia |
- `bible/world/JP-Senpai-Pairs.md › Conflicts and Story Hooks`: 4. Okayu, the "all-affirming cat," judges an Ina–FUWAMOCO argument and agrees with everyone.
- `bible/world/JP-Senpai-Pairs.md › Hard Facts`: - 7th fes (March 6–8, 2026; STAGE 1 Mar 6, STAGE 3 Mar 7, STAGE 4 Mar 8): STAGE 1 Ayame, Okayu (with Ina, FUWAMOCO); STAGE 3 AZKi (with IRyS, Bae, Shiori); STAGE 4 Suisei (with Calli, Kronii, Bijou, Nerissa).

### from Justice Pairs
- `bible/world/Justice-Pairs.md › [SW] Description`: With seniors: Gigi repeatedly uses Calli's full name and jokes about getting her into League of Legends; within HoloEU, Raora teaches Kiara Italian and Cecilia speaks German with her; Cecilia plays up a rivalry with Ina; Kronii is Raora's "Pizza Time" collaborator and Gigi's Fatal Fury and Hytale partner, and secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai"; Automatowl names Cecilia and Mumei.
- `bible/world/Justice-Pairs.md › Inside Justice`: - **Gigi and Raora ("RPGG"):** MapleStory (2024-08-16), Monster Hunter Wilds (2025, a sponsored launch with Ina and Bijou), a food tier-list off-collab (2025-06-05), Elden Ring Nightreign (2025); Raora designed the 2026 Monster Hunter collaboration outfits for Gigi and herself. [Observed S1; X post S5]
- `bible/world/Justice-Pairs.md › With Advent`: - **Shiori:** Elizabeth ("NovelFlame," "BloodQuill"; secondary) and Gigi voice parts in Shiori's non-canon motion comic "Into The Void" (2026; episode 2 also credits Calli); Gigi ("NovelGrem") games with her often (Heave Ho, a Fateful Findings watchalong, Project Zomboid, Phasmophobia; Eden Eternal was Kiara, Shiori and Gigi); the "Fanfic Club" (Gigi, Shiori, Pavolia Reine, Airani Iofifteen) is a separate group from "GAGA" (Gigi, Cecilia, Shiori, Bijou); Raora: a 2024 outfit-design collab (2024-12-05) and Blood Typers with Kronii and Bijou (2025-06-10); Cecilia: "Break It Down" with Vestia Zeta at Serendipity; Gigi: "MONSTER" with Ina and Kronii at -All for One-. [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Myth`: - **Ninomae Ina'nis:** Cecilia's Stranger of Paradise partner (2025), with a rivalry bit Cecilia plays up (secondary); "SHALLYS" with Cecilia and FUWAMOCO, "MONSTER" with Gigi, Kronii and Shiori, "Neko Kaburi-Na" with Raora, Shiori and Oozora Subaru (all at -All for One-); Rabbit and Steel with Cecilia, Bijou and Gigi (2024); Blood Typers with Gigi (2025-04-11); Puyo Puyo Tetris 2 with Raora (2025-06-02); the Monster Hunter Wilds sponsored launch with Gigi, Raora and Bijou (2025-03-01). [Observed S1]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone ("IT'S LOVE," iwnHChZq0N8, credits read by Claude); FUWAMOCO with Polka, Nene, Watame and Iroha; her 2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members). Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is "RaoRiRi" with Ichijou Ririka; "OkaGigi" is a secondary pair label for Gigi and Nekomata Okayu; secondary clip metadata records translation-based banter during the 2026 New Year Game Festival. It does not establish exact dialogue or a private relationship. Tsunomaki Watame sang "Cloudy Sheep" with Calli and Cecilia and "What an amazing swing" with Kiara and Raora at Serendipity. FLOW GLOW: Koganei Niko sang with Elizabeth in LYRA. [Observed S1; S2] [Official S6, S7]

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Other Names`: Kiara and Ame, Ame and Kiara, Kiara and Gura, Gura and Kiara, Calli and Ina, Ina and Calli, Calli and Ame, Ame and Calli, Ina and Ame, Ame and Ina, Ina and Gura, Gura and Ina, Kiara and Kronii, Kronii and Kiara, Gura and Kronii, Kronii and Gura
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Calli and Ina: Ina designed Death Sensei and drew Calli's debut EP cover; Calli wrote the lyrics of Ina's "TAKO∞TAKOVER"; Calli is a recurring target of Ina's puns ("Every freaking time, Ina.").
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Ina and Ame: Ina designed Bubba; they did a "loser buys dinner" off-collab.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Ina and Gura: the official ocean unit UMISEA (2021); Ina promised "the wrath of Ina" to anyone who makes Gura cry.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Calli and Ina** (26 / 26 / 8 / 15 / 8 / 9; 2 in 2026): Ina designed Calli's Death Sensei and drew the cover of Calli's debut EP; Calli wrote the lyrics of Ina's 2026 song "TAKO∞TAKOVER." Calli is a recurring target of Ina's puns ("Every freaking time, Ina."). They watched Suisei's concert together in an off-collab (2023-02-20) and still game together (Elden Ring Nightreign, 2025-06). [Observed S5 Ina §Miscellaneous; Calli file C28; Ina file I8; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Ina and Ame** (29 / 30 / 9 / 4 / 4 / 0): Ina designed Bubba; Ame's "Amenade" cocktail traces back to a Japanese snack tasting with Ina; a "LOSER BUYS DINNER!!!!!" off-collab (2023-02-23); Ame aims blunt PvP taunts at her. [Observed S3 §Miscellaneous; Ame file; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Ina and Gura** (71 / 28 / 10 / 3 / 3 / 2): fellow members of the official ocean unit UMISEA (September 2021); Ina drew chibi Bloop and promised "the wrath of Ina" to anyone who makes Gura cry; Gura once directed a lost Ina in Minecraft by hitting a block with her pickaxe. [Official UMISEA announcement; S4 §Gura's antics, secondary]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2026-01-08 | "TAKO∞TAKOVER" digital release (lyrics by Calli) | Ina × Calli |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Conflicts and Story Hooks`: 3. Calli writes lyrics for Ina and Ina draws the cover; each critiques the other's draft.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Conflicts and Story Hooks`: 5. Ina organizes a "loser buys dinner" rematch.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Hard Facts`: - Ina designed Death Sensei, Bubba and the Takodachi; Calli wrote the lyrics for "TAKO∞TAKOVER."

### from Octo'Clock
- `bible/world/OctoClock.md › [SW] Other Names`: Ina and Kronii, Kronii and Ina, Octo'clock, Octo'Clock
- `bible/world/OctoClock.md › [SW] Description`: Ninomae Ina'nis and Ouro Kronii, the octopus and the clock: longstanding collaborators whose 2026 Serendipity pairing foregrounds their shared puns, interests and performance work.
- `bible/world/OctoClock.md › [SW] Description`: (Los Angeles, July 3–4) under the name "Octo'Clock"
- `bible/world/OctoClock.md › [SW] Description`: (the official report spells it "Octo'clock"), performing "Bad Apple."
- `bible/world/OctoClock.md › [SW] Description`: In their official interview Kronii called them "Just two punny people waiting to deliver the pun-chline to everyone" and praised Ina as "very hard-working and ambitious"; Ina said "I get to…keep Kronii….all to myself…..hehe…hehehe" and admired Kronii's "unmatched charisma whenever she sings."
- `bible/world/OctoClock.md › [SW] Rules`: Ina's claim on Kronii is a sweet joke, not romance.
- `bible/world/OctoClock.md › How It Works`: - **Official pairing (2026):** paired for the 4th concert "Serendipity" (Shrine Auditorium, Los Angeles, 2026-07-03/04); Kronii's short "#holoSerendipity It's Time for Octo'Clock!" (2026-06-24) names the unit. [Official S2; Observed S3]
- `bible/world/OctoClock.md › How It Works`: - Kronii: "Just two punny people waiting to deliver the pun-chline to everyone." She praises Ina's drawing and quick execution, her puns, and that "She's very hard-working and ambitious."
- `bible/world/OctoClock.md › How It Works`: - Ina: "I get to…keep Kronii….all to myself…..hehe…hehehe"; "it's even more special now that it's just us two together!!"; she admires Kronii's "unmatched charisma whenever she sings."
- `bible/world/OctoClock.md › How It Works`: - **On stream (archive, S1):** Ina's FGO streams with Kronii (2023-08-18 "Let's Learn About Fate/Grand Order!!!", 2024-01-02 "NEW YEAR FGO ADVENTURES"), R.E.P.O. (2025-07-19), and Ame's 2022 surprise karaoke off-collab that both joined (per Ame's wiki page).
- `bible/world/OctoClock.md › History`: | 2022-02-25 | Ame's surprise karaoke off-collab (with Ina, Kronii, Fauna, Mumei) | — |
- `bible/world/OctoClock.md › History`: | 2023–2024 | FGO streams on Ina's channel | A shared game |
- `bible/world/OctoClock.md › History`: | 2026-06-24 | "It's Time for Octo'Clock!" short | The unit name |
- `bible/world/OctoClock.md › Conflicts and Story Hooks`: 2. Ina quietly claims Kronii "all to myself" in front of Calli; Kronii plays along deadpan.
- `bible/world/OctoClock.md › Hard Facts`: - "Octo'Clock" is the pairing's name in Kronii's official short (2026-06-24).

### from TakaMori
- `bible/world/TakaMori.md › How It Works`: - **Recent milestones (archive, S1):** an off-collab "Reunion & Gaming!! #takamori" and a karaoke collab (2022-06); off-collabs in 2023 (a Rubik's cube stream, "TAKAMORI OFF-COLLAB" with Kobo, doing each other's nails on camera with IRyS); their duet "Fire N Ice" (2023-12-14; lyrics by Calli and TeddyLoid); Kiara's off-collab watch party "cheering Calli on!!!" for Calli's GriMoire concert (2025-02-27); a four-part Split Fiction co-op series in April–May 2025, titled by them "takamori split screen nostalgia," "Perfectly In Sync with @TakanashiKiara," "thumbnail teetee manifestation into gameplay teetee" and "Saving the World with @TakanashiKiara"; Myth's 5th anniversary collab (2025-09-13) and the 6th anniversary 3D live "Seasons From Within" (2026-09-19 PDT), where the two sang a duet cover together (setlist, secondary S7) and premiered "THIS IS MYTH" with Ina.

### from Time Duo
- `bible/world/Time-Duo.md › How It Works`: - **On stream (archive, S1):** Ame's surprise karaoke off-collab with Ina, Kronii, Fauna and Mumei (2022-02-25, per S3); 5D Chess "I Don't Understand With @WatsonAmelia" (Kronii, 2023-04-08); Escape the Backrooms with Calli (2024-09-22) and Deep Rock Galactic with Kiara and Gura (2024-09-30, Ame's last week of regular streams).

### from VTuber Persona and Lore
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They can re-enter it for a bit and drop it again: Calli's reaper threats, Ina's "priestess" voice, Kiara's KFP manager routine, Ame's time-traveler jokes [Observed character files]

### from holoX
- `bible/world/holoX.md › With the English cast`: - **Ninomae Ina'nis, Gawr Gura (graduated):** UMISEA with Chloe, Minato Aqua and Houshou Marine (official 2023 roster). [Official UMISEA roster https://hololivesummer2023.hololivepro.com/unit/umisea/]

### from hololive -Myth-
- `bible/world/hololive--Myth.md › [SW] Other Names`: Myth, holoMyth, HoloMyth, hololive -Myth-, hololive English first generation
- `bible/world/hololive--Myth.md › [SW] Description`: At the September 2026 baseline, Calli, Kiara and Ina are active members of hololive -Myth-; Ame is an affiliate and Gura is a graduate.
- `bible/world/hololive--Myth.md › [SW] Description`: All five belong to Myth's shared history. hololive's first English generation debuted 12–13 September 2020: Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Gawr Gura and Watson Amelia.
- `bible/world/hololive--Myth.md › [SW] Description`: Calli wrote the lyrics for their first song and often plays the grumbling big sister; Kiara cheers loudest and hosts; Ina, the calm one, designed the Myth mascots except Bloop; Ame is often the gremlin and tech helper; Gura is the goofy little shark.
- `bible/world/hololive--Myth.md › [SW] Description`: On 2026-09-19 Calli, Kiara and Ina held the 6th Anniversary 3D LIVE "Seasons From Within" and premiered a new Myth song, "THIS IS MYTH."
- `bible/world/hololive--Myth.md › [SW] Rules`: At the 2026 baseline Calli, Kiara and Ina are the active members; Ame can appear as an affiliate guest; Gura appears as a memory or callback, never as a current streamer.
- `bible/world/hololive--Myth.md › Members and Status`: - Mori Calliope, Takanashi Kiara, Ninomae Ina'nis: active in hololive -Myth-.
- `bible/world/hololive--Myth.md › How the Group Works`: - **Roles that formed early:** Calli wrote the lyrics for Myth's first song "Myth or Treat" (2021) and often plays the grumbling big sister; Kiara is the loudest cheerleader and the one who hosts; Ina is the calm one who designed the Myth mascots (all except Bloop) and draws for the group; Ame is the gremlin and the tech helper; Gura is the goofy little shark everyone protects. [Observed wiki pages, secondary; Adaptation for "big sister / little shark" shorthand]
- `bible/world/hololive--Myth.md › How the Group Works`: - **Group humor:** mutual teasing, jinxes, chaotic Minecraft and party games; name-order trivia (Calli and Ame say their names in English order; Kiara, Ina and Gura surname-first). [Observed S2]
- `bible/world/hololive--Myth.md › How the Group Works`: - **Protectiveness:** Ina says anyone who makes Gura cry will "face the wrath of Ina," and extends the promise to all the English members (tears of joy excepted). [Observed S2 Gura §Gura's antics, secondary]
- `bible/world/hololive--Myth.md › History`: | 2025-04-30 | Myth relay "one last time" with Calli, Kiara, Ina and Gura before Gura's graduation | Gura's farewell with Myth |
- `bible/world/hololive--Myth.md › History`: | 2025-09-13 | 5th anniversary collab with announcements (Calli, Kiara, Ina) | New anniversary hats |
- `bible/world/hololive--Myth.md › History`: | 2026-09-19 PDT (09-20 JST) | Myth 6th Anniversary 3D LIVE "Seasons From Within" on the hololive English channel with Calli, Kiara and Ina; it premiered the new Myth original song "THIS IS MYTH," whose MV followed. Pair stages (setlist, secondary S5): Kiara and Ina, Calli and Kiara, Calli and Ina each sang a duet cover | The current three on stage together [S3, S4; S5] |

### from hololive -Promise-
- `bible/world/hololive--Promise.md › How the Group Works`: - **After 2025:** the group is three. Kronii's 2026 activity includes a 3D birthday live with Ame as a guest, the Serendipity pairing with Ina and her EP. [Observed Kronii file K4, K33, K36]

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05 PDT); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: (June); EN's 4th concert "Serendipity" in Los Angeles (July), built on units such as Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS, Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 EDT | World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 | — |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-07-05 PDT | hololive night at Dodger Stadium, Los Angeles, the second hololive–Dodgers collaboration: Ina, IRyS and Bijou | a stadium sing-along |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-03-27/28 PDT | Kiara and Ina's duo concert "Drawn to Dawn" (Los Angeles) | TakoTori on stage |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-07-03/04 PDT | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) | The current partnerships |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-09-19 PDT | Myth 6th Anniversary 3D LIVE "Seasons From Within" (Calli, Kiara, Ina); new Myth song "THIS IS MYTH" | — |

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-09-12/13 | **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame | The cast's origin |

### from hololive
- `bible/world/hololive.md › [SW] Description`: (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-.
- `bible/world/hololive.md › How It Works`: - **Structure (as of 2026-09-30):** hololive production is COVER's brand, which also includes the male group HOLOSTARS; hololive is its female VTuber group. On 2026-09-07 COVER unified the former female-talent branches (hololive, hololive English, hololive Indonesia, hololive DEV_IS) under a single "hololive," an organizational and branding change it described as removing regional limits; members had already collaborated across branches for years; former groups keep their names as units (hololive -Myth-, -Promise-, -Advent-, -Justice-). Promotion is now done for all members in Japanese, Indonesian and English. [Official S6] [Observed S2 §2026, secondary, citing the hololive Next broadcast of 2026-09-07; project.md]
- `bible/world/hololive.md › History`: | 2026-07-03/04 | hololive English 4th concert "Serendipity" (LA) | Partner pairs (e.g. Kronii and Ina) |

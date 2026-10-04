# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: holox
Packet: projects/holoen/research/qa/packets/holox.md (owned material) and projects/holoen/research/qa/packets/holox-incoming.md (incoming claims); both are inline below
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
- **語音台詞的語言（作者 2026-10-04 定案）：hololive JP 的成員（含 holoX 與 DEV_IS 的 Vivi，共 14 人）在 ElevenLabs
  語音腳本裡念日文。**說出口的台詞用日文字（假名、漢字）寫，羅馬拼音和英文翻譯只放在不唸的 `ROMAJI`／`GLOSS` 行。
  卡片的 Audio Tags 與表演表第 2 節寫明「Dialogue language: Japanese」，轉換器會擋下沒有日文字的 JP 成員台詞。
  EN 成員維持英文（可夾日文詞）。卡片本身仍用英文寫。

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
- **只有二手轉錄的台詞（作者 2026-10-04 選 B）：**`research/qa/quote-inventory.md` 列的 93 句（粉絲 wiki 等二手轉錄、
  沒有兩模型 ASR 確認）保留在匯出欄位，作者以例外放行；來源標籤保留在卡片的 dossier。V13 以此清單為作者例外。
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
| AUDIT-JP | Cohort audit jp (Suisei, AZKi, Ayame, Okayu, JP Senpai Pairs) | applied in full; exclusion-note wording generalized across all audio reports; JP-QUOTE-001 deferred to the project-wide quotation pass (voice-delivery.md, blocks V13) | 2026-10-04 merge |
| AUDIT-JP2 | Cohort audit jp2 (Marine, Noel, Lamy, Botan, Vivi, JP Senpai Pairs 2) | applied; AZKi seniority rows keep the neutral jp label (she joined hololive in 2022), Okayu→Noel set to JP kouhai; Fauna scope redaction done by hand in the audio report | 2026-10-04 merge |
| QUOTE-INVENTORY | 93 exported spoken lines resting only on secondary transcriptions (jp:JP-QUOTE-001 and the project-wide pass) | **author decision 2026-10-04: B**, kept as an author exception; three lines upgraded by two-model checks (Shukkō, Ohamassuru, Bruh) | 2026-10-04 |

### Registry excerpt (this cohort's cast and world records and its units; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "17521e0",
 "cast": [
  {
   "name": "Hakui Koyori",
   "file": "bible/characters/Hakui-Koyori.md",
   "other_names": [
    "Koyori",
    "Koyo",
    "Koyorin",
    "博衣こより"
   ],
   "groups": [
    "hololive",
    "Secret Society holoX",
    "holoX",
    "Hoshimatic Project",
    "KoZMy",
    "NePoX",
    "Blue Journey"
   ],
   "status": "Koyori is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-11-28",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Hakui-Koyori.md › Background (debut: Background)"
   }
  },
  {
   "name": "Kazama Iroha",
   "file": "bible/characters/Kazama-Iroha.md",
   "other_names": [
    "Iroha",
    "Iroha-dono",
    "Gozaru",
    "Gozaru-chan",
    "風真いろは"
   ],
   "groups": [
    "hololive",
    "Secret Society holoX",
    "holoX",
    "AzuIro",
    "Hoshimatic Project",
    "NePoX",
    "Bara☆Dice"
   ],
   "status": "Iroha is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-11-30",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Kazama-Iroha.md › Background (debut: Background)"
   }
  },
  {
   "name": "La+ Darknesss",
   "file": "bible/characters/Laplus-Darknesss.md",
   "other_names": [
    "La+",
    "Laplus",
    "YMD",
    "ラプラス・ダークネス"
   ],
   "groups": [
    "hololive",
    "Secret Society holoX",
    "holoX",
    "NePoX"
   ],
   "status": "La+ is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-11-26",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Laplus-Darknesss.md › Background (debut: Background)"
   }
  },
  {
   "name": "Sakamata Chloe",
   "file": "bible/characters/Sakamata-Chloe.md",
   "other_names": [
    "Chloe",
    "Kuroe",
    "Sakamata",
    "Kura-tan",
    "沙花叉クロヱ"
   ],
   "groups": [
    "hololive",
    "Secret Society holoX (until 2025)",
    "holoX",
    "KoyoChlo",
    "Kanaken",
    "holoWitches",
    "UMISEA"
   ],
   "status": "Chloe is a hololive affiliate, formerly an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "affiliate",
    "debut": "2021-11-29",
    "graduated": null,
    "regular_activities_concluded": "2025-01-26",
    "source": "bible/characters/Sakamata-Chloe.md › Background (debut: Background)"
   }
  },
  {
   "name": "Takane Lui",
   "file": "bible/characters/Takane-Lui.md",
   "other_names": [
    "Lui",
    "Lui-nee",
    "Lui Lui",
    "鷹嶺ルイ",
    "ルイルイ"
   ],
   "groups": [
    "hololive",
    "Secret Society holoX",
    "holoX",
    "HOLOTORI",
    "Bara☆Dice",
    "Blue Journey",
    "InuTakaShishiRam",
    "NePoX"
   ],
   "status": "Lui is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-11-27",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Takane-Lui.md › Background (debut: Background)"
   }
  }
 ],
 "world": [
  {
   "name": "holoX",
   "file": "bible/world/holoX.md",
   "role": "Organization",
   "other_names": [
    "Secret Society holoX",
    "秘密結社holoX",
    "hololive 6th Generation"
   ]
  }
 ],
 "units": []
}
```

### projects/holoen/research/qa/packets/holox.md

# Audit packet: holox

Snapshot: git 17521e0. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Laplus-Darknesss.md` 4f243197ccfe; `bible/characters/Takane-Lui.md` 015a3f014ba3; `bible/characters/Hakui-Koyori.md` 2335e184a0f0; `bible/characters/Sakamata-Chloe.md` a3555ab23cbe; `bible/characters/Kazama-Iroha.md` 85fd36cc6c01; `bible/world/holoX.md` 37017b831e12

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### La+ Darknesss — `bible/characters/Laplus-Darknesss.md`
**[SW] Groups:** hololive, Secret Society holoX, holoX, NePoX
**[SW] Other Names:** La+, Laplus, YMD, ラプラス・ダークネス
**[SW] Background:** La+ is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-26 as the first member of Secret Society holoX, hololive's sixth Japanese generation, whose executive officer Takane Lui does the actual running. Her songs include "drop candy" (2024) and "Onee-sama♡Love Call" (released 2026-05-26). She performed at holoX's first in-person unit concert, "First MISSION" (2026-04-29), and Tochigi Prefecture appointed her a Tochigi Future Ambassador (2026-05-03). With the English cast, archived metadata records the Mythmash single "Glow in the Dark" (released 2025-07-28) and the cover "FAKE HEART" (2025) with Takanashi Kiara, a nostalgic-games off-collab on Kiara's channel (2023), and Mori Calliope's English lesson #02 with Gawr Gura and Kazama Iroha (2022).
**[SW] Relationships:** Takane Lui: holoX's executive officer, who actually runs things and reins her in. Hakui Koyori and Kazama Iroha: holoX; secondary references call her pairing with Iroha "Irohasu." Sakamata Chloe (affiliate since 2025): the former intern; covers together (2022, 2025). Takanashi Kiara: "Glow in the Dark" (Mythmash) and "FAKE HEART" (2025), and a nostalgic-games off-collab (2023). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: archived shorts of them performing to "Onee-sama♡Love Call" (2026). Cecilia Immergreen: an "ONEE-SAMA!" short about her (2026). Nerissa Ravencroft, Nakiri Ayame, Hoshimachi Suisei and Shishiro Botan: fellow holoGTA participants (2024). Suisei, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024). Nekomata Okayu: a 3D lie-detector challenge (2026); secondary references group them in "Dorobo Kensetsu." AZKi: games and an ASMR "evaluation" (2025). Houshou Marine: a sponsored collab billed #マリラプ and a cover with Koyori (2025). Yukihana Lamy and Shishiro Botan: NePoX (2026).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | Founder of Secret Society holoX; vast power, now sealed | [Official LA1] |
| 2021-11-26 | Debut, the first holoX member to debut | [Observed LA2] |
| 2022-03-04 | Calli's "HOLO ENGLISH LESSON #02" with Gura and Iroha | [LA5 X492n37brRU] |
| 2023-06-30 | Nostalgic games with a handcam, an off-collab on Kiara's channel (archived title and description) | [LA5 XWf2PqD_8zQ] |
| 2024 | "drop candy" (05-25); holoGTA participant (her archive establishes participation; other members' own archives place them in the same event) | [Observed LA2] [LA4 swqXHi1Z4ew] |
| 2025-04-08 | "FAKE HEART," a cover with Kiara | [LA5 yspJ9xmGRfw] |
| 2025-07-27/28 | "Glow in the Dark," a Mythmash single with Kiara (official digital release 2025-07-28); a joint stream | [Official music 600] [LA5 v5RKZXNuVyw] [LA4] |
| 2025-12 | holoX's 4th anniversary, including "Gyouan Xdeath" | [Observed LA2] |
| 2026-04-08 | holoX album "Secret ORDER" released | [Official FIX-R6-003] |
| 2026-04-29 | holoX's first in-person unit concert, "First MISSION" (La+, Lui, Koyori, Iroha) | [Official LA6] |
| 2026-05-03 | Tochigi Future Ambassador | [Official LA3] |
| 2026-05-19 | A 3D lie-detector "challenge" to Nekomata Okayu | [LA4 F3i30BIJmtY] |
| 2026-05-25/26 | "Onee-sama♡Love Call" (official digital release 2026-05-26); album "Project Y.M.A." announced | [Official music 753] [Observed LA2] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-11-26; Secret Society holoX (founder); birthday 25 May; 139 cm; illustrator Mishima Kurone; fans
  Plusmate; stream tag #laplus_great.

### Takane Lui — `bible/characters/Takane-Lui.md`
**[SW] Groups:** hololive, Secret Society holoX, holoX, HOLOTORI, Bara☆Dice, Blue Journey, InuTakaShishiRam, NePoX
**[SW] Other Names:** Lui, Lui-nee, Lui Lui, 鷹嶺ルイ, ルイルイ
**[SW] Background:** Lui is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-27 as the second member of Secret Society holoX, hololive's sixth Japanese generation, and belongs to the bird unit HOLOTORI, whose documented 2023 lineup was Lui, Takanashi Kiara, Oozora Subaru, Pavolia Reine and Nanashi Mumei. She released the album "Liberty" (2024), the EP "Lieblings" (2025) and the EP "The LEGENDARY" with "Soar" (2026-06), and performed at holoX's first in-person unit concert, "First MISSION," at Pia Arena MM (2026-04-29). In June 2026 COVER announced her BAYFM78 radio programme and her 1st live, "REBELLION," set for 2026-12-16 at Kanadevia Hall. With the English cast, archived metadata records English practice with Mori Calliope (2021), Calli's lesson #04 with Chloe (2022), Calli's "HOLOYOI" episode 1 with Chloe (2023), a Wario off-collab with Kiara (2023), "TWIN DAY WITH LUI" with FUWAMOCO (2023), Hakos Baelz's "BAE-GEMITE DOMINATION" episode 5 with Chloe (2023) and "Q&A With Bird Sisters" with Mumei (2025). Several English members' channels posted animated "Soar" shorts (2026).
**[SW] Relationships:** La+ Darknesss: holoX's founder, whom Lui reins in and covers for. Sakamata Chloe (affiliate since 2025): the intern she used to keep in line. Hakui Koyori and Kazama Iroha: holoX; secondary references record "Lui-nee" as Iroha's address for her. Takanashi Kiara: HOLOTORI; a Wario off-collab (2023). Nanashi Mumei (graduated): HOLOTORI; "Q&A With Bird Sisters" (2025). Mori Calliope: English practice (2021), lesson #04 (2022), "HOLOYOI" (2023). FUWAMOCO: "TWIN DAY WITH LUI" (2023). Hakos Baelz: "BAE-GEMITE DOMINATION" (2023) and a "FEAST" dance short (2025). IRyS and Ouro Kronii: Minecraft with Kaela (2022). Watson Amelia (affiliate): Apex with Iofi (2022). Nekomata Okayu: Harry Potter watch-alongs (2025); secondary references list both in "Dorobo Kensetsu." Nakiri Ayame: "Onikan" (archived titles, 2025). Shishiro Botan: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (2023, archived title); Left 4 Dead 2 with IRyS and Korone (2022); Blue Journey. Houshou Marine, Shirogane Noel and Kazama Iroha: Bara☆Dice (with Flare and Nene). Yukihana Lamy: NePoX (2026). Nerissa Ravencroft, Koseki Bijou, Gigi Murin and Raora Panthera: animated "Soar" shorts (2026).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | holoX's executive officer and point of contact | [Official LU1] |
| 2021-11-27 | Debut, second of holoX; HOLOTORI membership (the wiki places Kiara's welcome beside the 11-26 reveal) | [Observed LU2] [Official HOLOTORI roster 2023] |
| 2021-12-27 | English practice with Mori Calliope | [LU5 i2wLH4O92-0] |
| 2022 | Calli's English lesson #04 with Chloe; an EN-server Minecraft tour with Mumei, Bae and Chloe; Minecraft with IRyS, Kronii and Kaela | [LU5] |
| 2023 | HOLOYOI ep. 1 with Chloe (Calli's show, 03-23); a Wario off-collab with Kiara (01-15); BAE-GEMITE #5 with Bae and Chloe (04-29); "TWIN DAY WITH LUI" with FUWAMOCO (11-25); Blue Journey (official roster) | [LU5 UuL_nORzfNM, cVJefDjefUs, z4-5Hq5AKG4, MbqO5OPuT80] [Blue Journey roster] |
| 2024 | First album "Liberty" (official digital release 06-12); 1 million subscribers (11-16, secondary) | [Official music 434] [Observed LU2] |
| 2025 | EP "Lieblings"; Code Geass ambassador (June, secondary); "Q&A With Bird Sisters" with Mumei (04-19); Harry Potter watch-alongs with Okayu; "FEAST" dance short with Bae (07-11) | [Observed LU2] [LU5] [LU4 Lj0MZFpHitQ, 5TUiccnytQA] |
| 2025-12-01 | holoX's 4th anniversary, including "Gyouan Xdeath" | [Observed LU2] |
| 2026-04-08 | holoX album "Secret ORDER" released | [Official FIX-R6-004] |
| 2026-04-29 | holoX's first in-person unit concert "First MISSION"; COVER's interview after it describes the concert as a turning point for the four-member group and its audience | [Official LU6] |
| 2026-06-11 | EP "The LEGENDARY" with "Soar" (official digital release of "Soar" 06-12); 1st live "REBELLION" (2026-12-16) and a BAYFM78 radio programme (from 07-03) announced; EN members' channels posted animated "Soar" shorts crediting external motion creators | [Official LU7] [Official music 760] [LU4] [LU5] |
| 2026-06-11 | COVER announces a regular BAYFM78 radio programme for her (first broadcast scheduled for 2026-07-03); orders open for the four-track EP "The LEGENDARY," including "Soar"; her first live concert "REBELLION" announced for 2026-12-16 at Kanadevia Hall (after the baseline: an announcement only). | [Official NEW-R6-013/014] |
| 2026-08-01 | A "rare" La+ and Lui talk with new outfits | [LU4] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-11-27; Secret Society holoX (executive officer); birthday 11 June; 161 cm; illustrator Kakage; fans
  "Lui-tomo"; partner Ganmo (frogmouth); fan mark 🥀; stream tag #たかねの見物.
- Greetings: "Mattakane?" / "Otsuluilui."

### Hakui Koyori — `bible/characters/Hakui-Koyori.md`
**[SW] Groups:** hololive, Secret Society holoX, holoX, Hoshimatic Project, KoZMy, NePoX, Blue Journey
**[SW] Other Names:** Koyori, Koyo, Koyorin, 博衣こより
**[SW] Background:** Koyori is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-28 as the third member of Secret Society holoX and released her first original song, "WAO!!," in 2022. She sang in "Blue Journey" with Marine, Noel, Lamy, Botan, Lui and Sakura Miko (2023); secondary records place her in Suisei's Hoshimatic Project from 2023; archived 2025 collabs bill her, AZKi and Lamy as "KoZMy." She performed at holoX's first in-person unit concert, "First MISSION" (2026-04-29), and in September 2026 announced her second album, "Chemical Spark," and her first solo concert, "Dream Spark," for December 2026. With the English cast, archived titles and descriptions record Lethal Company with FUWAMOCO and Shirakami Fubuki (2024), a FUWAMOCO Morning guest spot billed "FUWAMOKOYO" (2024), and guest appearances at FUWAMOCO's birthday concert (2025) and Mumei's first 3D live (2024). In 2023 she joined Bae's "BAE-GEMITE DOMINATION" with Momosuzu Nene and tasted Bae's "KHAOS KITCHEN" curry with Calli and Oozora Subaru.
**[SW] Relationships:** La+ Darknesss: holoX's founder; a sponsored "#stons" collab (2024) and a cover with Marine (2025). Takane Lui and Kazama Iroha: holoX; Lui: Blue Journey (2023). Sakamata Chloe (affiliate since 2025): "KoyoChlo," a running "disband!" gag from their co-op games; their last collab before Chloe's graduation and the duet cover 「一番の宝物」 (January 2025). AZKi and Yukihana Lamy: "KoZMy" (archived 2025 titles); a 3D karaoke with AZKi (2026); a #ラミこよ off-collab with Lamy (2026). Houshou Marine: archived titles bill them as the "pink-haired pair"; Blue Journey; Marine backseats her Pikachu game (2025). Shirogane Noel: Blue Journey and "NoeKoyo" baseball (2025). Hoshimachi Suisei: Hoshimatic Project (secondary). Shishiro Botan: NePoX and Blue Journey. Nekomata Okayu: a lateral-thinking puzzle collab she hosted (2025). FUWAMOCO: "FUWAMOKOYO" on FUWAMOCO Morning (2024), Lethal Company with them and Shirakami Fubuki (2024), their birthday concert (2025). Hakos Baelz: BAE-GEMITE DOMINATION with Nene and a KHAOS KITCHEN tasting (2023). Nanashi Mumei (graduated): a guest at her first 3D live (2024). IRyS: Splatoon 3 (2022) and Among Us (2023). Takanashi Kiara: a "MIRAGE" dance short (2024).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2021-11-28 | Debut, third of holoX | [Official KO1] [Observed KO2] |
| 2022-06-16 | First original song "WAO!!" (official music page); the wiki also dates her 3D debut here (not verified in review) | [Official music page] [Observed KO2] |
| 2023 | "Blue Journey" with Marine, Noel, Lamy, Botan, Lui and Sakura Miko (07-08; official roster); 1 million subscribers (09-24, secondary); Hoshimatic Project (from 11, secondary) | [Blue Journey roster] [Observed KO2] |
| 2023-04-22 | "BAE-GEMITE DOMINATION" episode 4 with Bae and Momosuzu Nene | [KO5 WwjB7QSmQng] |
| 2024 | Lethal Company with FUWAMOCO and Fubuki (03-09); FUWAMOCO Morning episode 90 guest, billed #FUWAMOKOYO (04-26); a guest at Mumei's first 3D live (08-05) | [KO5 XR1PEtj15kE, gCYXKgYcFmk, gl7CwlEg2ZI] |
| 2025-01-14 | The last "KoyoChlo" collab before Chloe's graduation; its description says the "#こよクロ disband!" gag was born in two-player co-op games; the duet cover 「一番の宝物」 followed (2025-01-28) | [KO4 mxIoysy6gJ4, nCPHzr_iF7s] |
| 2025 | Weekly Famitsu column launched (07-17); archived collabs bill Koyori, AZKi and Lamy as "KoZMy" (08-03, 08-20); "pink-haired pair" talk with Marine | [KO7] [KO4 lvgC3pW-LVA, oxWPvsUb_3Y] |
| 2026-03-24 | #ラミこよ off-collab with Lamy, proposing to choose a duo name (no final name established) | [Lamy channel Zi8R63ee0Fs] |
| 2026-04-29 | holoX's first in-person unit concert, "First MISSION" | [Official KO6] |
| 2026-08-22 | Announced hololive Koshien 2026: Koyori is organizer and one of six team managers (others include Houshou Marine and Shirogane Noel); the main competition is scheduled for 10-17/18 (after the baseline: an announcement only). | [Member announcement NEW-R6-017] |
| 2026-09-12 | Second album "Chemical Spark" and first solo concert "Dream Spark" (2026-12-22) announced | [Observed KO2] |
| 2026-09-20 | A mirrored public post acknowledges a fan estimate that her own-channel livestream total passed 10,000 hours | [KO3] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-11-28; Secret Society holoX (head of R&D); birthday 15 March; 153 cm; illustrator Momoco; fans
  Koyori's Assistants; robot coyote Kokoro; stream tag #こより実験中; fan-art tag #こよりすけっち; AsaKoyo on
  Tuesdays and Fridays at 7:00 JST.

### Sakamata Chloe — `bible/characters/Sakamata-Chloe.md`
**[SW] Groups:** hololive, Secret Society holoX (until 2025), holoX, KoyoChlo, Kanaken, holoWitches, UMISEA
**[SW] Other Names:** Chloe, Kuroe, Sakamata, Kura-tan, 沙花叉クロヱ
**[SW] Background:** Chloe is a hololive affiliate, formerly an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-29 as the fourth member of Secret Society holoX, and secondary records date her 500,000 subscribers to her first week and a million to 2023. A secondary chronology lists ten numbered original-song releases by January 2025. She took part in the original lineup of Suisei's Hoshimatic Project (secondary roster reference), "Magical Girl holoWitches!" and the "Kanaken" Minecraft company with Amane Kanata and AZKi (a 3D live in 2024), and concluded her regular activities on 2025-01-26, holding a graduation live and remaining an affiliate; a secondary record has her singing "Sparkle" at Murasaki Shion's graduation live (2025-04-26). After 2025-01-26 she is an affiliate rather than part of holoX's four-member performing lineup. With the English cast, archived channel metadata documents an EN-server Minecraft tour with Bae, Mumei and Lui (2022), Calli's English lesson #04 (2022) and HOLOYOI #01 (2023), Bae's "BAE-GEMITE DOMINATION" and the cover "Crazy Scary Holy Fantasy" with her (2023), and "WILDCARD" with Kiara in her final week (2025).
**[SW] Relationships:** Takane Lui: holoX's executive officer; secondary accounts describe Lui reining her in; "LuiChlo" collabs, Calli's English lesson and HOLOYOI together. Hakui Koyori: "KoyoChlo," a duo with a running "disband!" gag; their last collab and two covers in January 2025. La+ Darknesss: covers together (2022, 2025). Kazama Iroha: holoX; the duet cover "Gehenna" on her last day (2025-01-26). AZKi: "Kanaken" with Amane Kanata (Minecraft, Chained Together, a 3D live, 2024). Houshou Marine: UMISEA (official 2023 roster) and holoWitches. Hoshimachi Suisei: the original Hoshimatic Project lineup (secondary); a farewell video together (2025). Yukihana Lamy: Rust with Kanata (2022). Shishiro Botan: an Overwatch 2 team (2023). Takanashi Kiara: "WILDCARD," performed at the 2024 fes and released as a cover in her final week (2025), and an origami off-collab (2023). Hakos Baelz: the EN Minecraft tour (2022), BAE-GEMITE DOMINATION and "Crazy Scary Holy Fantasy" (2023). Mori Calliope: HOLO ENGLISH LESSON #04 (2022) and HOLOYOI #01 (2023). Nanashi Mumei (graduated): the EN Minecraft tour (2022). IRyS: Overwatch 2 and Among Us (2023). Ninomae Ina'nis and Gawr Gura (graduated): UMISEA (official 2023 roster). Nekomata Okayu: chorus on her "Bling-Bang-Bang-Born" cover (2025). Fuwawa and Mococo Abyssgard: a "Gimme Chocolate!!" cover together (2024).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2021-11-29 | Debut, fourth of holoX; 500,000 subscribers within a week | [Official CH1] [Observed CH2] |
| 2022 | First original "Jinsei Reset Button Pochii w" (02-26); EN Minecraft tour with Bae, Mumei and Lui (02-12); Calli's English lesson #04 with Lui (04-16); 3D debut (06-13) | [Observed CH2] [CH5] |
| 2023 | 1 million subscribers (02-18, secondary); HOLOYOI #01 with Calli and Lui (03-23); "BAE-GEMITE DOMINATION" (04-29); a cover with Bae (10-30); the original Hoshimatic Project lineup (11-, secondary roster reference) | [Observed CH2] [CH5 UuL_nORzfNM, z4-5Hq5AKG4, 9EAIDwXj4Jk] |
| 2024 | "Magical Girl holoWitches!" single (05-30); "Kanaken" 3D live with Kanata and AZKi | [Observed CH2] [CH4] |
| 2024-11-29 | Conclusion of regular activities announced for 2025-01-26; she will remain a hololive production affiliate afterward | [Observed CH2] |
| 2025-01 | Farewell week: last "KoyoChlo" collab (01-14), covers with La+ (01-15) and Koyori (「花の塔」 01-23; 「一番の宝物」 01-28 on Koyori's channel), "WILDCARD" with Kiara (01-25; the description says they had performed it at the 2024 fes), "Gehenna" with Iroha (01-26) | [CH4 u5hBkM77dX0, acYx6NnoaAQ, mKq0e-7nnSU] [KO4 nCPHzr_iF7s] [CH5 eEGbAKvSf1Q] [IR4 5zJp7oulbwc] |
| 2025-01-26 | Graduation live "Gochisōsama deshita"; tenth original song "Hikari Are" | [CH4] [Observed CH2] |
| 2025-04-26 | Performs "Sparkle" with Murasaki Shion at Shion's graduation live | [Observed CH2] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-11-29; Secret Society holoX (intern, fixer and cleaner); regular activities concluded 2025-01-26
  (affiliate); birthday 18 May; 148 cm; illustrator Parsley; fans Handlers (shiikuin); mascot Inu; stream tag
  #またまたさかまた; fan-art tag #さかまた飼育日記.

### Kazama Iroha — `bible/characters/Kazama-Iroha.md`
**[SW] Groups:** hololive, Secret Society holoX, holoX, AzuIro, Hoshimatic Project, NePoX, Bara☆Dice
**[SW] Other Names:** Iroha, Iroha-dono, Gozaru, Gozaru-chan, 風真いろは
**[SW] Background:** Iroha is an active member of Secret Society holoX. She has no supernatural abilities; her lore is a performed persona. She debuted on 2021-11-30 as the fifth and last member of Secret Society holoX; archived stream titles mark her as the last of holoX to pass a million subscribers (2024-11-19), and a secondary chronology numbers 「風向きエントロピー」 ("Entropy of wind direction," 2026) as her ninth original. She formed the duo AzuIro with AZKi (covers, the 2025 song "AZUIRO BESTIE DAYS," off-collabs), sings in Suisei's Hoshimatic Project (credited on "BEEP BEEP," 2026) and performed at holoX's first in-person unit concert, "First MISSION" (2026-04-29). With the English cast, archived channel metadata documents Calli's English lesson #02 with La+ and Gura (2022), a VALORANT collab with Ame and Kobo Kanaeru (2022), the cookie-battle off-collab she and AZKi presented with FUWAMOCO as challengers (2024), credited guest spots at Kiara's 2024 and 2025 lives, and a credit on "CHA-LA HEAD-CHA-LA" from Elizabeth's 2026 birthday show.
**[SW] Relationships:** AZKi: "AzuIro," her steady duo (covers, "AZUIRO BESTIE DAYS" in 2025, Cuphead and off-collabs billed as summer camps). La+ Darknesss: holoX's founder; a cover together (2024). Takane Lui: a cover together (2024); secondary references record "Lui-nee" as her address for Lui. Hakui Koyori: holoX genmate. Sakamata Chloe (affiliate since 2025): the duet cover "Gehenna" on Chloe's last day (2025). Hoshimachi Suisei: Hoshimatic Project ("BEEP BEEP," 2026); coached her at Puyo Puyo Tetris (2023). Yukihana Lamy and Shishiro Botan: NePoX. Houshou Marine and Shirogane Noel: fellow Bara☆Dice vocalists (distributor credits). Takanashi Kiara: a credited guest at Kiara's 2024 and 2025 lives; #TASTYchallenge shorts with Nene (2025). Watson Amelia (affiliate): a VALORANT collab with Kobo Kanaeru (2022; secondary references call the trio "KoMeHa"). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: challengers in the cookie battle she and AZKi presented (2024). Elizabeth Rose Bloodflame: "CHA-LA HEAD-CHA-LA" from her 2026 birthday show, with FUWAMOCO.
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| 2021-11-30 | Debut, the fifth and last of holoX | [Official IR1] [Observed IR2] |
| 2022 | Calli's English lesson #02 with La+ and Gura (03-04); VALORANT with Ame and Kobo Kanaeru ("KoMeHa," 06-04) | [IR5] |
| 2023 | AzuIro: GeoGuessr on a "Kazama map" AZKi made, covers and a first off-collab (08); Puyo Puyo Tetris coaching from Suisei (04); Hoshimatic Project (11-) | [IR4] [Observed IR2] |
| 2024 | Covers with La+ (「絶対敵対メチャキライヤー」, 03-11) and Lui (「右肩の蝶」, 04-11); originals "Mahou Shoujo☆Magical GOZARU" and "Dreamy Sky" (06); a cookie-battle off-collab on her channel, presented with AZKi, with FUWAMOCO as the challengers (10-27, JgOwJ7m89Lk); a guest at Kiara's 4th-anniversary live (10-06); 1 million subscribers (11-19) | [Observed IR2] [IR4] [IR5] |
| 2025 | "Gehenna" cover with Chloe on her last day (01-26); Cuphead as #あずいろ (06-03) and an off-collab billed as a summer camp (08); "A letter only you can read" (06-15); a guest at Kiara's birthday live (07); #TASTYchallenge shorts with Kiara and Nene (07-11, 07-16); "AZUIRO BESTIE DAYS" (official release 09-18) | [IR4 5zJp7oulbwc, -im-pIdanZY, mwhcZmc6-s8] [IR5 f-UbyQUUykE, 0ldag8qdg6c, AQNPRJMMYY0] [Official music 642] |
| 2026-04-29 | holoX's first concert, "First MISSION" | [Official IR6] |
| 2026-05-19 | An excerpt from Elizabeth's 2026 birthday show, uploaded 05-19, credits Iroha, Watame, Nene, Polka and FUWAMOCO on "CHA-LA HEAD-CHA-LA" (upload date, not necessarily the show date) | [IR5 xylll7Mp0jk] |
| 2026-06-18/19 | 「風向きエントロピー」 (official English title "Entropy of wind direction"; MV 06-18, digital release 06-19); a secondary chronology numbers it her ninth original | [IR4 RDobidAdBCA] [Official music 764] [Observed IR2] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-11-30; Secret Society holoX (bodyguard, "insurance policy"); birthday 18 June; 156 cm; illustrator
  Umibōzu; fans Kazama-tai (Kazama Squad); companion Pokobee (tanuki); katana Chakimaru; stream tag #かざま修行中;
  fan-art tag #いろはにも絵を.

### holoX — `bible/world/holoX.md`
**[SW] Other Names:** Secret Society holoX, 秘密結社holoX, hololive 6th Generation
**[SW] Description:** Secret Society holoX is hololive's sixth Japanese generation, a self-styled evil secret society that streams. In their official lore, La+ Darknesss is the founder, a demon whose vast powers are sealed; her archived channel introduction uses "wagahai" and performs a world-conquest boast. Takane Lui is the executive officer and point of contact who does the real work and cares for her subordinates; Hakui Koyori runs R&D as the self-proclaimed "brains," meddling in everyone's affairs to study them; Kazama Iroha is the society's bodyguard and "insurance policy," a samurai who says "de gozaru." Sakamata Chloe, the orca intern who cleaned up after them, ended her regular activities on 2025-01-26 and is now a hololive affiliate rather than part of the four-member performing lineup. They debuted one a night in November 2021 and held their first in-person unit concert, "First MISSION," at Pia Arena MM on 2026-04-29 as four; with NePoLaBo they form NePoX ("Watcha Gatcha!!!!!!!!," 2026). With the English cast, archived uploads document Lui in the bird unit HOLOTORI with Kiara and Mumei (and Lui and Mumei's "Q&A With Bird Sisters"); "Glow in the Dark" by La+ and Kiara (2025); Chloe and Kiara's "WILDCARD" cover; Calli's English lessons with La+ and Iroha (#02) and Lui and Chloe (#04); Koyori's "FUWAMOKOYO" morning-show guest spot with FUWAMOCO and a separate Lethal Company session with them and Fubuki; and Iroha's VALORANT collab with Ame and Kobo (secondary name "KoMeHa").
**[SW] Rules:** holoX's "evil organization" is a performed lore frame; their schemes are bits. After 2025-01-26 Chloe is a hololive affiliate rather than an active member of holoX's four-member performing lineup; affiliates can appear at individual events. The 2026 concert was four members. Collab titles show that a collab happened, not how close two members are; event rosters are dated.
**Dossier · History:**
| Date | Event | Who |
|---|---|---|
| 2021-11-26 to 11-30 | Debut week, one member a night | La+, Lui, Koyori, Chloe, Iroha |
| 2022-03-04 | Calli's English lesson #02 | La+, Iroha; archive X492n37brRU |
| 2022-04-16 | Calli's English lesson #04 | Lui, Chloe; archive YrZ4baKOT1c |
| 2023 | HOLOYOI ep. 1 (Lui, Chloe); BAE-GEMITE episodes; Kiara's off-collabs with Lui and La+ | with Calli, Bae, Kiara |
| 2024 | FUWAMOKOYO; holoX "Drokei" escape event | Koyori; the group |
| 2025-01-26 | Chloe's graduation live; she stays an affiliate | Chloe |
| 2025-04-19 | "Q&A With Bird Sisters" | Lui, Mumei |
| 2025-07-27 | "Glow in the Dark" video premiere (Mythmash; inherited date, zone unspecified) | La+, Kiara; Kiara Relationship Map and archive v5RKZXNuVyw |
| 2025-07-28 (digital release; zone unspecified) | "Glow in the Dark" digital release | La+, Kiara; official catalog 600, checked 2026-10-04 |
| 2025-12-01 | 4th anniversary: "Gyouan Xdeath," concert announced | four members |
| 2026-04-08 | Album "Secret ORDER" released | [Official, R6] |
| 2026-04-29 | "First MISSION," Pia Arena MM | La+, Lui, Koyori, Iroha |
**Dossier · Hard Facts (continuity):**
- Members and debut order: La+ (2021-11-26), Lui (11-27), Koyori (11-28), Chloe (11-29), Iroha (11-30).
- Chloe: regular activities ended 2025-01-26; affiliate.
- First in-person concert: "First MISSION," Pia Arena MM, 2026-04-29 (four members).

Incoming claims continue in `holox-incoming.md`.

### projects/holoen/research/qa/packets/holox-incoming.md

# Audit packet: holox (incoming claims)

Snapshot: git 17521e0.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: lolive 6th Generation|Secret Society holoX|Sakamata Chloe|La+ Darknesss|Hakui Koyori|Kazama Iroha|Gozaru-chan|ラプラス・ダークネス|Iroha-dono|Takane Lui|秘密結社holoX|Kura-tan|Sakamata|Lui-nee|Lui Lui|Koyorin|Koyori|沙花叉クロヱ|Laplus|Gozaru|風真いろは|Kuroe|holoX|Chloe|博衣こより|Iroha|Koyo|鷹嶺ルイ|ルイルイ|Lui|La+)(

### from AZKi
- `bible/characters/AZKi.md › [SW] Background`: Her units include SorAZ with Tokino Sora, AS_tar with Suisei ("Going My Way," 2026), Star Flower with Suisei, Moona Hoshinova and IRyS ("story time," 2022), AzuIro with Kazama Iroha ("AZUIRO BESTIE DAYS," 2025) and, from 2026, RosaMiA.
- `bible/characters/AZKi.md › [SW] Relationships`: Amane Kanata and Kazama Iroha: collaborators associated with KanatAZ and AzuIro ("AZUIRO BESTIE DAYS," 2025).
- `bible/characters/AZKi.md › [SW] Relationships`: Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!"
- `bible/characters/AZKi.md › [SW] Relationships`: Koyori also joined AZKi, Isaki Riona and Koganei Niko for a four-person 3D karaoke (2026); Lamy is also in "KALAZ" with Amane Kanata (secondary).
- `bible/characters/AZKi.md › [SW] Relationships`: Sakamata Chloe: "Kanaken" with Kanata (Minecraft and a 3D live, 2024).
- `bible/characters/AZKi.md › [SW] Relationships`: La+ Darknesss: GeoGuessr for Tochigi Day and other games (2025).
- `bible/characters/AZKi.md › Behavioral Traits`: 4. Dances other members' songs in her shorts (Calli's "Orpheus," 2025-10-09, archived metadata lXLBb9IVraI; in 2026 Laplus, Towa and Nene, Miko, Koyori, Riona, Lui, Zeta). [Observed AZ4 titles]
- `bible/characters/AZKi.md › Background Timeline`: | 2025-09-18 | "AZUIRO BESTIE DAYS" with Kazama Iroha (official digital release) | [Official AZ10] |
- `bible/characters/AZKi.md › Relationship Map`: | Kazama Iroha | "AzuIro" (secondary label) | Frequent partner since 2022; their original "AZUIRO BESTIE DAYS" (2025-09-18) They performed "AZUIRO BESTIE DAYS" on STAGE 3 of hololive 7th fes. (2026-03-07), with linked little fingers and a shared heart gesture; AZKi's encouragement in the MC left Iroha tearful. | [AZ2] [Official AZ10] [Official NEW-R5-007] |
- `bible/characters/AZKi.md › Relationship Map`: | Hakui Koyori, Yukihana Lamy | "KoZMy" (secondary references; a 2025-08-03 "KoZMy 結成⁉" collab title) | A 3D karaoke with Koyori, Isaki Riona and Koganei Niko (2026-02-03, not a KoZMy event); Lamy is also in "KALAZ" with Amane Kanata (secondary) Lamy: an impromptu group chat with Lamy and Inugami Korone on Lamy's channel (#あずらみころ, 2026-09-18). | [Koyori file KO4 lvgC3pW-LVA, 1HQL3WJPBHA] [Lamy file LM2] [Archive metadata NEW-R5-005] |
- `bible/characters/AZKi.md › Relationship Map`: | Sakamata Chloe (affiliate) | "Kanaken" with Amane Kanata | Minecraft construction "company," Chained Together and a 3D live (2024) | [Chloe file CH4] |
- `bible/characters/AZKi.md › Relationship Map`: | La+ Darknesss | — | GeoGuessr for Tochigi Day (2025-06-15), The Headliners with Korone and Miko (2025-05-07), Minecraft (2025-07); a clip of La+ reacting to AZKi's ASMR (2026-03-31) | [AZ4 80Xb4PxZLyw, AMturrbpVD0] [La+ channel z0Z2Zc3MlE4, 6n2X82dqqx0] |

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: La+ Darknesss: a 2026 short titled "ONEE-SAMA!
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | La+ Darknesss | holoX senior | A 2026 short titled "ONEE-SAMA! (Laplus-senpai... onee-sama.. janai)" (archived title, not verified dialogue) | [S1 tqF0_rYGW20] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Her April 25, 2026 birthday-live guests included FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine, Korone and Nerissa.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | FUWAMOCO | Advent seniors | They sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha | [Observed EB3] |

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Hakui Koyori: "FUWAMOKOYO" on FUWAMOCO MORNING (2024).
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Takane Lui: "TWIN DAY WITH LUI"
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Kazama Iroha: a cookie-quiz off-collab (2024).
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: La+ Darknesss: a dance short to her song (2026).
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Sakamata Chloe: a "Gimme Chocolate!!" cover (2024).
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Secret Society holoX (Koyori, Lui, Iroha, La+) | JP members | "FUWAMOKOYO" with Koyori (FUWAMOCO Morning ep. 90, 2024-04-26); Lethal Company with Koyori and Fubuki (2024-03-09); Koyori a guest at their 2025 birthday concert; "TWIN DAY WITH LUI" (2023-11-25); a cookie-quiz off-collab presented by Iroha and AZKi, the twins as challengers (2024-10-27); dance shorts to La+'s and Lui's 2026 songs | [S1 gCYXKgYcFmk, XR1PEtj15kE, ouQF2A1l_cI, MbqO5OPuT80, JgOwJ7m89Lk] |
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Sakamata Chloe | JP senior (holoX) | A cover of BABYMETAL's "Gimme Chocolate!!" with Chloe (2024-02). | [Archive metadata, ragtag m5c9WfWUBZE] |

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: La+ Darknesss and Kazama Iroha: Calli's English lesson #02 together (2022).
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: (2023); UMISEA's official 2023 roster also includes Sakamata Chloe.
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate; fellow member of the official unit UMISEA (2021, with Aqua and Marine; the wiki also lists Chloe) | Ina drew chibi Bloop and performed a protective mock-threat bit about Gura; co-op games The final Myth relay's Gang Beasts segment ran on Ina's channel (reported 2025-04-30). | [Observed G2 §Gura's antics and §Mascots and fans; G16] [Official G17] [Secondary NEW-R1-017] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | La+ Darknesss, Kazama Iroha, Shishiro Botan | JP members | HOLO ENGLISH LESSON #02 with La+ and Iroha (Calli's stream, 2022-03-04); "Apex Predators," a wiki-listed pair name with Botan | [S1 X492n37brRU] [Botan file, secondary] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Houshou Marine, Sakamata Chloe | UMISEA (official 2023 roster: Aqua, Marine, Chloe, Gura, Ina) | "SHINKIRO" with Marine (anime MV on Marine's channel, 2023-11-12, credited to both; the "GuraMarine" pair name is wiki-listed only) | [Marine file MA4 9ehwhQJ50gs] [Official UMISEA roster] |

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Takane Lui: an animated "Soar" short on her channel (2026).

### from Hakos Baelz
- `bible/characters/Hakos-Baelz.md › [SW] Relationships`: Natsuiro Matsuri: "Kakumei Dualism" at the 2026 fes. holoX: Sakamata Chloe ("Crazy Scary Holy Fantasy," 2023), Takane Lui (episode 5, with Chloe) and Hakui Koyori (episode 4, with Nene) on BAE-GEMITE DOMINATION.
- `bible/characters/Hakos-Baelz.md › Background Timeline`: | 2026-09-28 | "PARADISE!", the hololive Dreams area theme: animated MV; Bae shares the vocal credit with Omaru Polka, Houshou Marine, Yukihana Lamy, Hakui Koyori, Kobo Kanaeru and Ichijou Ririka. Also announced that day: "REGALIA" at Kanadevia Hall, scheduled for 2026-12-01 (after the baseline: an announcement only). | [Secondary NEW-R2-019, press-release reproduction] [Official, 20260928-02-16] |
- `bible/characters/Hakos-Baelz.md › Relationship Map`: | Secret Society holoX (Lui, Chloe, Koyori) | JP kouhai | The EN-server Minecraft tour with Mumei, Lui and Chloe (2022-02-12); BAE-GEMITE DOMINATION #4 with Koyori and Nene (2023-04-22) and #5 with Lui and Chloe (2023-04-29); a Suika Game challenge and the "Crazy Scary Holy Fantasy" cover with Chloe (2023-10-30); KHAOS KITCHEN taste testers Koyori, Calli and Subaru (2023-11-24) Koyori is a co-credited singer on "PARADISE!" (2026-09-28). | [HB3 S-d80w5gs-c, WwjB7QSmQng, z4-5Hq5AKG4, p9_oBCK0olg, 9EAIDwXj4Jk, NdLiUW-nUlk] [Secondary NEW-R2-019] |

### from Hoshimachi Suisei
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: Hakui Koyori and Kazama Iroha: her Hoshimatic Project ("BEEP BEEP," 2026); Sakamata Chloe was in its earlier lineup (secondary); she coached Iroha at Puyo Puyo Tetris (2023).
- `bible/characters/Hoshimachi-Suisei.md › [SW] Relationships`: La+ Darknesss, Nakiri Ayame and Shishiro Botan: holoGTA (2024); La+, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024).
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | Hakui Koyori, Sakamata Chloe, Kazama Iroha | Hoshimatic Project | Her idol-group practice unit (2023–); Koyori and Iroha are among the nine credited "BEEP BEEP" vocalists (2026), Chloe was in the earlier lineup (secondary roster); she coached Iroha at Puyo Puyo Tetris (2023-04-11) | [Official BEEP BEEP credits] [Koyori file KO2] [Iroha file IR4 8tOoSNGa_rg] |
- `bible/characters/Hoshimachi-Suisei.md › Relationship Map`: | La+ Darknesss, Nakiri Ayame, Shishiro Botan | — | All four streamed holoGTA (2024-09); Sammy's m HOLD'EM collaboration (2024) featured Suisei, La+, Botan and Shirakami Fubuki (publisher roster; a joint broadcast is not established) | [SU4 2v4DYYf7hB0] [Sammy roster] |

### from Houshou Marine
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Shirogane Noel: hololive Fantasy genmate; Bara☆Dice with Takane Lui, Shiranui Flare, Momosuzu Nene and Kazama Iroha; separately, Yakamashi Musume with Yukihana Lamy and Inugami Korone.
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Hakui Koyori: "#頭ピンク組," the pink-haired pair of their archived titles (a race and a talk testing whether they are alike, 2025); Blue Journey.
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: La+ Darknesss: a sponsored collab billed #マリラプ and a cover with Koyori (2025).
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Takane Lui and Kazama Iroha: Bara☆Dice.
- `bible/characters/Houshou-Marine.md › [SW] Relationships`: Sakamata Chloe (affiliate): UMISEA and holoWitches.
- `bible/characters/Houshou-Marine.md › Background Timeline`: | 2026-09 | Holo Koshien series: a baseball team followed through successive in-game seasons; Koyori joined the 09-17 session and AZKi commentated on 09-26. | [Archive metadata NEW-R5-014, NEW-R5-006] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Hakui Koyori | "#頭ピンク組" (the pink-haired pair, archived titles); Blue Journey | A talk testing whether they are alike and a Gorogoro Mountain race (2025-07); backseat Pikachu (2025-08) Koyori joined her Holo Koshien session (2026-09-17). | [MA4 QnT0cKrEhkk] [Koyori file KO4] [Archive metadata NEW-R5-014] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | La+ Darknesss | "#マリラプ" (archived title) | A sponsored collab (2025-07); a cover with La+ and Koyori (2025-08) | [MA4 Xf4MPOkHKtE] [Koyori file] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Takane Lui | Bara☆Dice (Bandai credits) | The wiki's "SSS" with Yuzuki Choco was not verified in review | [MA2] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Sakamata Chloe (affiliate) | UMISEA; holoWitches | Chloe played Marine's horror game (2023) | [MA2] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Kazama Iroha | Bara☆Dice | — | [MA2] |
- `bible/characters/Houshou-Marine.md › Relationship Map`: | Minato Aqua (graduated) | UMISEA | The ocean unit's official roster: Aqua, Marine, Chloe, Gura and Ina | [Official UMISEA roster] |

### from IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: Shishiro Botan, Takane Lui, Sakamata Chloe and Tokoyami Towa: an Overwatch 2 team (2023); Hakui Koyori: Splatoon 3 and Among Us.
- `bible/characters/IRyS.md › Relationship Map`: | Shishiro Botan, Takane Lui, Sakamata Chloe, Hakui Koyori | JP members | Left 4 Dead 2 with Botan, Lui and Inugami Korone (2022-04-24); an Overwatch 2 team with Botan, Lui, Chloe and Towa (Holizontal JAM, 2023-08); Splatoon 3 with Koyori, Watame and Korone (2022-10-03); an Among Us lobby with Koyori, Chloe and others (2023-05-08); Minecraft elytra hunting with Lui and Kronii (2022) | [S1 K1wStJxm4F0, roWKpgZsjR4, Xoma7oWsMcM, VwqdwQx5cog] |

### from Kikirara Vivi
- `bible/characters/Kikirara-Vivi.md › Relationship Map`: | Yukihana Lamy | JP senior | Lamy hosted, and Vivi, Iroha and Bijou commentated, the 2026-01-15 SUPER EXPO 2026 / 7th fes. information programme (secondary report). | [Secondary NEW-R6-008] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Takane Lui: an animated "Soar" short on her channel (2026).

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Hakui Koyori: special guest on FUWAMOCO MORNING ("FUWAMOKOYO," 2024).
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: La+ Darknesss: a dance short to her song (2026).
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Takane Lui: "TWIN DAY WITH LUI"
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Kazama Iroha: a cookie-quiz off-collab (2024).
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Sakamata Chloe: a "Gimme Chocolate!!" cover (2024).
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Secret Society holoX (Koyori, Lui, Iroha, La+) | JP members | "FUWAMOKOYO" with Koyori (FUWAMOCO Morning ep. 90, 2024-04-26); Lethal Company with Koyori and Fubuki (2024-03-09); Koyori a guest at their 2025 birthday concert; "TWIN DAY WITH LUI" (2023-11-25); a cookie-quiz off-collab presented by Iroha and AZKi, the twins as challengers (2024-10-27); dance shorts to La+'s and Lui's 2026 songs | [S1 gCYXKgYcFmk, XR1PEtj15kE, ouQF2A1l_cI, MbqO5OPuT80, JgOwJ7m89Lk] |
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Sakamata Chloe | JP senior (holoX) | A cover of BABYMETAL's "Gimme Chocolate!!" with Chloe (2024-02). | [Archive metadata, ragtag m5c9WfWUBZE] |

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: English-lesson guests Marine, AZKi, La+, Iroha, Lui and Chloe (2022); HOLOYOI guests Lui, Chloe, Noel and Botan (2023).
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Secret Society holoX (La+, Lui, Chloe, Iroha) | JP kouhai | English practice with Lui (2021-12-27); HOLO ENGLISH LESSON #02 with La+, Iroha and Gura (2022-03-04) and #04 with Lui and Chloe (2022-04-16); HOLOYOI #01 with Lui and Chloe (2023-03-23); dance shorts to Lui's songs | [S1 X492n37brRU, YrZ4baKOT1c, UuL_nORzfNM; world card "holoX"] |

### from Nakiri Ayame
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: La+ Darknesss, Hoshimachi Suisei and Shishiro Botan: holoGTA (2024).
- `bible/characters/Nakiri-Ayame.md › [SW] Relationships`: Takane Lui: "Onikan"
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | La+ Darknesss, Hoshimachi Suisei, Shishiro Botan | — | All four streamed holoGTA (2024-09); Ayame was not in the m HOLD'EM poker collab | [AY4 1iz9AxcgvPg] [Sammy roster] |
- `bible/characters/Nakiri-Ayame.md › Relationship Map`: | Takane Lui | "Onikan" (archived titles) | A sponsored collab billed おにかん (2025-08-09); secondary coverage also reports R.E.P.O. with Lui, Miko and Korone (2025) | [Lui channel YXaDmUXPSGo] [appbank.net report, secondary] |

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: JP: archived uploads document her Q&A with Takane Lui, an April 2025 duet cover with Inugami Korone, and Korone, Okayu, Nene and Koyori as 2024 "Outside the Box" guests; Tokoyami Towa calls her "Mumi-chan"; Akai Haato: Minecraft; Nakiri Ayame: the 2023 Sports Festival white team.
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Sakamata Chloe: Mumei's EN-server Minecraft tour with Lui and Bae (2022).
- `bible/characters/Nanashi-Mumei.md › Background Timeline`: | 2024-08-05 | 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori | [Observed M3 title, description] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Takane Lui, Tokoyami Towa, Akai Haato | JP seniors | "【MUMEI + LUI】Q&A With Bird Sisters !!!" (2025-04-19); Towa calls her "Mumi-chan"; Minecraft "Peace & Love with HAACHAMA" (2025) | [Observed M2 infobox; M3] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Inugami Korone, Nekomata Okayu (GAMERS); Momosuzu Nene, Hakui Koyori | JP seniors | All four were guests at "Outside the Box" (2024-08-05); Korone and Mumei released a duet cover of "とんとんまーえ！" (2025-04-23, P6GLC_HnCUU) | [Observed M3 descriptions] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Sakamata Chloe, Houshou Marine, Shirogane Noel, Kikirara Vivi | JP members | Chloe and Lui on Mumei's EN-server Minecraft tour with Bae (2022-02-12); Marine's horror game with Bae (2023-08-23); Noel and Vivi in Mumei's Gartic Phone EN + ID + JP (2025-04-14) | [S1 50tBPC5c2zM, RY1GkF4jMls, OMDzBQohAf8] |

### from Nekomata Okayu
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Hakui Koyori: a lateral-thinking puzzle collab (2025).
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: La+ Darknesss: "Dorobo Kensetsu" and a 3D lie-detector challenge (2026).
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Takane Lui: Harry Potter watch-alongs (2025).
- `bible/characters/Nekomata-Okayu.md › [SW] Relationships`: Sakamata Chloe: Okayu contributed chorus vocals to Chloe's "Bling-Bang-Bang-Born" cover (2025).
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Hakui Koyori | — | A lateral-thinking puzzle collab hosted by Koyori, with Shion, Okayu and Chloe (2025-01-07) | [Koyori channel PtjqrNUOSWA] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | La+ Darknesss | "Dorobo Kensetsu" | A 3D lie-detector challenge (2026) | [La+ file LA2, LA4] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Takane Lui | — | Harry Potter watch-alongs to introduce Okayu to the series (2025-11-24 and others); "Shaccho" is a first-model ASR rendering whose direction is unconfirmed, so it is not used | [Lui channel Lj0MZFpHitQ] |
- `bible/characters/Nekomata-Okayu.md › Relationship Map`: | Sakamata Chloe | — | Chorus on Chloe's "Bling-Bang-Bang-Born" cover (2025-01-24). | [Archive metadata, ragtag wxnTKRkpePs] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: La+ Darknesss: both in holoGTA (2024); a dance short to her "Onee-sama♡Love Call"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: (2026); Takane Lui: a "Soar" dance short (2026).
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Takane Lui, La+ Darknesss | JP members | Dance shorts to Lui's "Soar" (2026) and La+'s "Onee-sama♡Love Call" (2026); both took part in holoGTA (2024; a direct exchange is not established) | [S1 l5fGacH2i-o, ZINB546CMEw] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Houshou Marine and Sakamata Chloe: UMISEA.
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate; fellow member of the official unit UMISEA (2021, with Minato Aqua and Houshou Marine; the wiki also lists Sakamata Chloe) [Official I31] | Secondary accounts describe Ina's protective mock-threat bit about Gura; Ina drew chibi Bloop; a prank war is reported but [Unverified] | [Observed I2 §Relationships; Gura file G2 §Gura's antics and §Mascots and fans] |

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Takane Lui: Minecraft with IRyS and Kaela (2022).
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Takane Lui, Shirogane Noel, Kikirara Vivi | JP members | Minecraft elytra hunting with Lui, IRyS and Kaela (2022); Mumei's Gartic Phone EN + ID + JP with Noel and Vivi (2025-04-14) (archived upload credits) | [S1 zp5nxAgi2dw, OMDzBQohAf8] |

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Takane Lui: an animated "Soar" short on her channel (2026).
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Takane Lui | holoX senior | An animated "Soar" short on Raora's channel (2026-06-22) | [S1 N8bfOiPot6o] |

### from Shirogane Noel
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Houshou Marine: hololive Fantasy genmate; Bara☆Dice with Takane Lui, Shiranui Flare, Momosuzu Nene and Kazama Iroha; separately, Yakamashi Musume with Yukihana Lamy and Inugami Korone; 3rd-gen R.E.P.O.
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Hakui Koyori: "#ノエこよ," a Power Pros baseball exhibition (2025), and Blue Journey (2023).
- `bible/characters/Shirogane-Noel.md › [SW] Relationships`: Takane Lui and Kazama Iroha: Bara☆Dice.
- `bible/characters/Shirogane-Noel.md › Background Timeline`: | 2025 | #ノエこよ Power Pros exhibition with Koyori (01-10); Gartic Phone with Mumei, Ina, Kronii, Elizabeth and Vivi (04-14); 3rd-gen R.E.P.O. with Marine, Pekora and Flare (07-05); Elden Ring Nightreign with Flare and Pekora; an Audio-Technica collab with Ayame (07-11); "TREVIAN KNIGHT" (official digital release 08-16), which FUWAMOCO danced to (09-30) | [NO4] [NO5] [Official music 622] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Hakui Koyori | "#ノエこよ" (archived title) | A Power Pros baseball exhibition match (2025-01-10); Blue Journey (2023) | [Koyori file slTZmnyNbIc] [Official Blue Journey roster] |
- `bible/characters/Shirogane-Noel.md › Relationship Map`: | Takane Lui, Kazama Iroha | Bara☆Dice (Bandai credits) | — | [Bandai credits] |

### from Shishiro Botan
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: Takane Lui: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary); Left 4 Dead 2 (2022) and Overwatch 2 (2023) together.
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: La+ Darknesss, Hakui Koyori and Kazama Iroha: NePoX (NePoLaBo × holoX, 2026).
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: La+ Darknesss and Hoshimachi Suisei: holoGTA and, with Shirakami Fubuki, the m HOLD'EM poker collaboration (2024); Nakiri Ayame: holoGTA (2024).
- `bible/characters/Shishiro-Botan.md › [SW] Relationships`: IRyS: Left 4 Dead 2 with Lui and Korone (2022) and an Overwatch 2 team with Lui, Sakamata Chloe and Tokoyami Towa (2023).
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2022-04-24 | Left 4 Dead 2 with IRyS, Takane Lui and Inugami Korone | [BO5 K1wStJxm4F0] |
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2023 | BAE-GEMITE DOMINATION #2 with Bae and Subaru (04-08); HOLOYOI #03 with Calli and Subaru (05-18); an Overwatch 2 team with IRyS, Lui, Chloe and Towa (08) | [BO5] |
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2026-08-26 | NePoLaBo and Secret Society holoX release their joint original "Watcha Gatcha!!!!!!!!" | [Official NEW-R6-004] |
- `bible/characters/Shishiro-Botan.md › Background Timeline`: | 2026-09-26/27 | NePoX events with Secret Society holoX | [LM4 Ml1tM8S40p0] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Takane Lui | "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (secondary) | Left 4 Dead 2 (2022); an Overwatch 2 team (2023). The "BLT" label was not verified in review | [BO2] [BO5] [Lui file] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | La+ Darknesss, Hakui Koyori, Kazama Iroha | NePoX | NePoLaBo × holoX events (2026) The Shishiro Cup offline programme billed Botan and La+ on opposing sides of its East–West team competition (announced 2026-02-02 for 04-12). | [BO2] [Official NEW-R6-003] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Kazama Iroha | — | Built the roof of Botan's Minecraft shop (2023) | [Iroha file] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | Sakamata Chloe (affiliate) | — | The 2023 Overwatch 2 team | [BO5] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | La+ Darknesss, Nakiri Ayame, Hoshimachi Suisei | — | All four streamed holoGTA (2024-09); Sammy's m HOLD'EM collaboration (2024) featured La+, Suisei, Botan and Shirakami Fubuki, not Ayame (publisher roster; a joint broadcast is not established) | [BO4 jd7Bp0prwiI] [La+ file QLHSm3rpG8k] [Sammy roster] |
- `bible/characters/Shishiro-Botan.md › Relationship Map`: | IRyS | — | Left 4 Dead 2 with Lui and Korone (2022); the Overwatch 2 team with Lui, Chloe and Towa (2023) | [BO5 K1wStJxm4F0, roWKpgZsjR4] |

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Pavolia Reine (ID) and Takane Lui: HOLOTORI ("PavoNashi" with Reine).
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: HOLOTALK guests include Houshou Marine (#1), Hoshimachi Suisei ("cometori"), AZKi, Shirogane Noel, Nekomata Okayu and Nakiri Ayame. holoX: La+ ("Glow in the Dark"), Chloe ("WILDCARD"), Koyori ("MIRAGE") and Iroha (a guest at her 2024 and 2025 lives).
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Secret Society holoX | JP kouhai | HOLOTORI with Lui and Mumei; La+: "FAKE HEART" (2025-04-08), the Mythmash single "Glow in the Dark" (premiere 2025-07-27; official digital release 2025-07-28) and an off-collab (2023-06-30); Chloe: an origami off-collab (2023-11-22) and the "WILDCARD" cover (2025-01-25); Iroha: a credited guest at her 4th-anniversary live (2024) and birthday live (2025), and #TASTYchallenge shorts with Nene (2025-07-11, 07-16); Koyori: a "MIRAGE" dance short (2024-12-27) | [S1 v5RKZXNuVyw, eEGbAKvSf1Q, 0LoG81pLS8c, f-UbyQUUykE, 0ldag8qdg6c, AQNPRJMMYY0, xXwi19krZ68] |

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Kazama Iroha: VALORANT with Kobo Kanaeru (2022; secondary references call the trio "KoMeHa").
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Takane Lui: Apex with Airani Iofifteen (2022).
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Kazama Iroha, Takane Lui | JP members | "KoMeHa" with Iroha and Kobo Kanaeru (VALORANT, 2022-06-04); Apex with Lui and Iofi (2022-01-19) | [S1 tGVhLibbYL0, Mory0I9vXtI] |

### from Yukihana Lamy
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: She sang in the "Blue Journey" project with Marine, Noel, Koyori and Sakura Miko (2023), joined "Magical Girl holoWitches!"
- `bible/characters/Yukihana-Lamy.md › [SW] Background`: (2025), formed KoZMy with AZKi and Koyori (2025, per a collab title and secondary listings) and, per secondary records, is in KALAZ with Amane Kanata and AZKi.
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: AZKi: her KoZMy cover partner with Hakui Koyori on "Ai♡Scream!"
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: Hakui Koyori: KoZMy (2025) and a March 2026 off-collab titled to name their duo.
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: La+ Darknesss, Takane Lui, Kazama Iroha and Hakui Koyori: NePoX, the 2026 NePoLaBo × holoX events.
- `bible/characters/Yukihana-Lamy.md › [SW] Relationships`: Sakamata Chloe (affiliate): Rust with Amane Kanata (2022).
- `bible/characters/Yukihana-Lamy.md › Behavioral Traits`: 5. Units and pairs: NePoLaBo (with Botan, Omaru Polka and Momosuzu Nene); KALAZ (with Amane Kanata and AZKi, secondary); KoZMy (with AZKi and Koyori; a 2025-08-03 collab titled "KoZMy 結成⁉"); "Magamaga's" (with Nene, secondary); "Yakamashi Musume" (archived metadata); holoWitches. [Observed LM2 §Relationships, secondary] [Koyori file lvgC3pW-LVA]
- `bible/characters/Yukihana-Lamy.md › Background Timeline`: | 2023 | "Blue Journey" music project with Marine, Noel, Koyori and Sakura Miko | [Koyori file; Observed LM2] |
- `bible/characters/Yukihana-Lamy.md › Background Timeline`: | 2025 | Joins "Magical Girl holoWitches!" (04–05); "Yoppara Music!" (official digital release 08-13); a "KoZMy 結成⁉" collab with AZKi and Koyori (08-03; secondary listings give its first anniversary in 2026-08) | [Observed LM2] [Official music 609] [Koyori file lvgC3pW-LVA] |
- `bible/characters/Yukihana-Lamy.md › Background Timeline`: | 2026 | Her collaboration sake "Yukiyozuki" with Meiri Shurui (04); an off-collab with Koyori titled to name their duo (03); a NePoLaBo 3D party (04-29); NePoX took place at Ariake Arena on 2026-09-26/27 with Nene, Polka, Lamy, Botan, La+, Lui, Koyori and Iroha: NePoLaBo-versus-holoX games ending Day 1 with all eight in a giant-robot red-light/green-light challenge, and the collaboration song "Watcha Gatcha!!!!!!!!" introduced [Secondary NEW-R5-020, organizer report]; "Snowlight Stories" (official digital release 08-13) | [LM4 Zi8R63ee0Fs, Ekdsnb2aWY4, Ml1tM8S40p0] [Official NePoX page] [Official music 792] [Brewery page] |
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | Hakui Koyori | "KoZMy"; NePoX | A March 2026 off-collab whose title proposes naming their duo (the chosen name is not established); KoZMy horror (2025) They performed "Snow halation" together on STAGE 1 of hololive 7th fes. (2026-03-06). | [LM4 Zi8R63ee0Fs] [Koyori file] [Official NEW-R5-019] |
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | La+ Darknesss, Takane Lui, Kazama Iroha | NePoX | NePoLaBo × holoX events (2026; billed roster of eight, Chloe not included) | [LM4 Ml1tM8S40p0] [Official NePoX page] |
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | Kazama Iroha | — | Caravan Stories (2023) | [Iroha file] |
- `bible/characters/Yukihana-Lamy.md › Relationship Map`: | Sakamata Chloe (affiliate) | — | Rust with Kanata (2022-09); a self-knowledge quiz collab (2025-01-18) | [Chloe file z55R0Z8_qk0] [LM4 9DMCTQDpBos] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › Beyond EN`: - **JP:** FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo); archived game metadata lists Shirakami Fubuki and Hakui Koyori with the twins; "FUWAMOKOYO" labels Koyori and the twins in FUWAMOCO MORNING #90; Okayu and Korone made cameos at their 3D debut; Oozora Subaru sang "HOT DUCK!" with Bijou and the twins; Akai Haato and Bijou are "Red Stone"; Ichijou Ririka (ReGLOSS, originally DEV_IS) played Smash Bros. with Bijou with a loser's punishment. [Observed S1; S2]

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ina appears with Aqua, Marine, Chloe and Gura in UMISEA's official 2023 roster and released "Kurukuru Cruise" with Nekomata Okayu (2025).
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Amelia played VALORANT with Kobo and Kazama Iroha (2022; "KoMeHa" in secondary references).
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: (the X is silent; "Purrfect Pair" merchandise, 2026), Reine and Airani Iofi join her "Fanfic Club"; FUWAMOCO's oshi are Marine (Fuwawa) and Omaru Polka (Mococo), they game with Shirakami Fubuki and Hakui Koyori, and Oozora Subaru sang "HOT DUCK!" with them and Bijou.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Of Justice: Ollie is Elizabeth's kami-oshi, and Elizabeth plays with her and HOLOSTARS members in varying lineups (Code Red games; Marvel Rivals with Crimzon Ruze, her "Nephew" in an uncle–nephew bit); Elizabeth's 2026 birthday covers featured Subaru, Roboco, Sora, Choco, Marine, Korone, Polka, Nene, Watame and Iroha; Kaela appears in Raora's fictional basement bit ("SMITTEN"); Raora played Clubhouse Games with Haachama and Super Mario Party with Haachama and Zeta, and is "RaoRiRi" with Ririka; Cecilia plays games with Sora; at Serendipity, Kobo, Zeta and Tsunomaki Watame sang with Elizabeth, Gigi, Cecilia and Raora.
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Takanashi Kiara:** Usada Pekora is her oshi ("Senpai! Be my guide for the day!", 2020; HOLOTALK's 24th guest, 2022). Pavolia Reine is a recurring collaborator on her channel (30 streams; their pair name "PavoNashi"; a VR "vacation," a Minecraft summer festival; the bird unit "HOLOTORI" with Subaru, Reine, Mumei and Lui); Kobo calls her "Mommy Kiwawa." Other units: "O'riends" (Momosuzu Nene), "KoAra Connect" (Hakui Koyori), "SunMoon"/"Eclipse" (Moona Hoshinova). Outside hololive: "PomuTori" (Pomu Rainpuff), "Mintori" (Mint Fantôme). [Observed S1; S2 Kiara; Kiara file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ninomae Ina'nis:** an artist among artists: the ocean unit UMISEA (formed 2021 with Minato Aqua, Houshou Marine and Gura; Chloe appears in the official 2023 roster; Aqua and Gura have graduated and Chloe is an affiliate); "HoloJEI" (Tsunomaki Watame, Kureiji Ollie, Anya Melfissa); "TakoBazo" (Vestia Zeta); "TakoNeko" (Nekomata Okayu, a secondary pair name; "Kurukuru Cruise," 2025; see "JP Senpai Pairs"); Shiranui Flare appeared on her 2025 AmiAmi special ("Flare?!!?"). She admires Marine as an artist. [Observed S1; S2 Ina; Ina file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Watson Amelia** (affiliate): "KoMeHa" (Kobo Kanaeru, Kazama Iroha), "ZetAme" (Vestia Zeta); outside hololive, "SelAMei" (with Mumei and Selen Tatsuki). [Observed S2 Ame]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Nanashi Mumei** (graduated): HOLOTORI with Kiara, Subaru, Reine and Lui ("【MUMEI + LUI】Q&A With Bird Sisters !!!," 2025-04-19, fEO6kSCseE0); drawing collabs with Airani Iofi ("Doodles with IOFI," 2022-04-14, 2dWx7xg48xc; "SWIMSUITS!! with IOFI!," 2023-01-30, XCXF08GMUHY); a duet cover of "とんとんまーえ！" with Inugami Korone (2025-04-23, P6GLC_HnCUU), and Okayu, Korone, Nene and Koyori as guests at her 3D live "Outside the Box" (2024-08-05, gl7CwlEg2ZI); Minecraft "Peace & Love with HAACHAMA" (2025); Tokoyami Towa calls her "Mumi-chan." [Observed S1; Mumei file M2]

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **JP:** Houshou Marine (Fuwawa's oshi; a Touhou off-collab, 2024) and Omaru Polka (Mococo's oshi); Shirakami Fubuki (horror collabs and Lethal Company with Hakui Koyori, "FUWAMOKOYO"); Akai Haato, Tsunomaki Watame ("FUWAMOCO vs FUWAFUWA," 2024), Oozora Subaru (a Donkey Kong Country 2 off-collab, 2026), and Nekomata Okayu and Inugami Korone, who made cameos at their 3D debut. Guests at their 2025 birthday concert: Shiori, Bijou, Nerissa, Polka, Koyori, Marine, Ookami Mio and Fubuki. [Observed S1; S3]

### from Fauna and Mumei Pairs
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Kiara:** Mumei and Kiara are birds in HOLOTORI (with Subaru, Reine and Lui): "BUILDER BIRBS" (2021), "Kiwawa & Mumeiwi" (2022), a DECO*27 song together on the 4th fes. holo*27 stage (2023), "two smol beans" (2025-03-26) and Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies." Fauna and Kiara: "KIWAWA vs FAWNA" (2022), Pokémon Unite practice (2023), and Fauna was HOLOTALK's 32nd guest (2024-12-27), a week before she graduated. [Observed S1; S3 infobox; S4]
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Other collaborators:** Hakos Baelz is a recurring collaborator of both (Fauna's horror partner); Tsukumo Sana (graduated 2022) completed the Council; Inugami Korone recorded a duet cover with Mumei (2025-04-23) and, with Okayu, Nene and Koyori, guested at "Outside the Box" (2024-08-05). [Observed S1; Promise card]

### from JP Senpai Pairs 2
- `bible/world/JP-Senpai-Pairs-2.md › Houshou Marine with the cast`: - **Ninomae Ina'nis, Gawr Gura:** UMISEA, the ocean unit (official 2023 roster: Minato Aqua, Marine, Sakamata Chloe, Gura and Ina); Calli's English lesson #01 (Ina); a guest at Ina's "Pleides" (2024); "SHINKIRO" with Gura (anime MV on Marine's channel, 2023-11-12, credited to both). The "GuraMarine" pair name is wiki-listed only. [Official UMISEA roster] [S1 9ehwhQJ50gs, 3n9igJnSXtQ] [S2 Marine §Relationships, secondary]
- `bible/world/JP-Senpai-Pairs-2.md › Shishiro Botan with the cast`: - **IRyS:** Left 4 Dead 2 with Lui and Inugami Korone (2022-04-24); an Overwatch 2 team for Holizontal JAM with Lui, Chloe and Towa (2023-08). [S1]
- `bible/world/JP-Senpai-Pairs-2.md › Among themselves`: - Marine and Noel: hololive Fantasy and Bara☆Dice (Bandai credits); with Lamy and Inugami Korone, "Yakamashi Musume" (archived metadata). The wiki's "Onee-san Gumi" with Shiranui Flare was not verified in review. Marine, Noel, Lamy, Hakui Koyori and Sakura Miko sang in the music project "Blue Journey" (2023). [S2]
- `bible/world/JP-Senpai-Pairs-2.md › Among themselves`: - With the first four: Marine and Suisei released "Chatter Chatter" (2026); Marine gave Okayu the nickname "Okanyan" (Okayu's official profile); Noel and Suisei are in "Shiranui Kensetsu" (official unit roster); Noel and Ayame did an Audio-Technica sponsored stream (2025-07-11); Botan streamed holoGTA with Suisei and Ayame (2024) and joined the m HOLD'EM poker collab with Suisei (2024); Lamy and AZKi are in KoZMy (with Koyori) and, per secondary references, KALAZ (with Amane Kanata). The wiki's holoALICE, MOMAS and HoLOGSS labels were not verified in review. [S2] [S1] [Official]

### from Justice Pairs
- `bible/world/Justice-Pairs.md › With Advent`: - **FUWAMOCO:** Raora is their Serendipity unit partner in B.F.F (official billing, "Inu Neko. Seishun Massakari"); Gigi and Cecilia guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit ("GigiMoco" and "Cecemoco" are pair labels with Mococo); Cecilia played Chrono Trigger with Mococo, including 2026 off-collabs; Gigi sang "Bright Tonight" (2025) with the twins, IRyS and Kronii, and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity; Fuwawa, Gigi and Calli as "2 Creatures + 1 Reaper" (2026, Fuwawa alone); the twins sang in Elizabeth's 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha. [Official S3 interview03] [Observed S1; S2]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone ("IT'S LOVE," iwnHChZq0N8, credits read by Claude); FUWAMOCO with Polka, Nene, Watame and Iroha; her 2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members). Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is "RaoRiRi" with Ichijou Ririka; "OkaGigi" is a secondary pair label for Gigi and Nekomata Okayu; secondary clip metadata records translation-based banter during the 2026 New Year Game Festival. It does not establish exact dialogue or a private relationship. Tsunomaki Watame sang "Cloudy Sheep" with Calli and Cecilia and "What an amazing swing" with Kiara and Raora at Serendipity. FLOW GLOW: Koganei Niko sang with Elizabeth in LYRA. [Observed S1; S2] [Official S6, S7]

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-01-26 | Sakamata Chloe concludes streaming activities (affiliate) | — |

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2021-11 | 6th gen "Secret Society holoX" (La+, Lui, Koyori, Chloe, Iroha) | — |

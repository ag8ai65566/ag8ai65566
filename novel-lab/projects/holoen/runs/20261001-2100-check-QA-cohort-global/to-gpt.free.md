# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: global
Packet: projects/holoen/research/qa/packets/global.md (owned material) and projects/holoen/research/qa/packets/global-incoming.md (incoming claims); both are inline below
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
Original calibration lines must say “Style demonstration.”

## Ownership and scope

Use the packet inventory to resolve exact paths. Primary ownership is:

- Myth: Calliope, Kiara, Ina, Amelia, Gura; Myth, TakaMori, TakoTori, AmeSame,
  Bone Bros, Myth-and-Kronii Other Pairs.
- Promise: Kronii, IRyS, Fauna, Mumei; Promise, Time Duo, Time and Death,
  OctoClock, Fauna-and-Mumei Pairs, IRyS-and-Nerissa Pairs.
- Advent: Shiori, Bijou, Nerissa, Fuwawa, Mococo; Advent, Advent Pairs, FUWAMOCO.
- Justice: Elizabeth, Gigi, Cecilia, Raora; Justice, Justice Pairs.
- Global: hololive, Streaming Life, VTuber Persona and Lore, Cross-Branch Friends,
  Concerts and Live Events, both History cards.

Together these cover 18 character and 24 world cards. Baelz, Sana and other
external participants may be referenced; do not create their character cards.

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

IDs: {COHORT}-{TYPE}-{NNN}, with COHORT = MYTH, PROMISE, ADVENT, JUSTICE or GLOBAL.
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
- 已完成（2026-10-01）：Myth 五人、Ouro Kronii、IRyS、Ceres Fauna、Nanashi Mumei、**Advent 全員**（Shiori Novella、
  Koseki Bijou、Nerissa Ravencroft、Fuwawa Abyssgard、Mococo Abyssgard）、**Justice 全員**（Elizabeth Rose Bloodflame、Gigi Murin、
  Cecilia Immergreen、Raora Panthera；2026-10-01）。尚未做：Hakos Baelz、Tsukumo Sana（等作者下令）。
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
| CONSULT-P2-001 | Myth sixth-anniversary live missing from shared timeline | applied as "announced, not verified as held" on Myth and TakaMori (only an announcement post is cited; no official event page or archive found by Claude 2026-10-01); propagation to History/Concerts waits for task 08 evidence | this commit |
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
| CLAUDE-SCOPE-001 | Process notes that dated or described excluded status matters (Kiara, Myth, TakaMori, History, x-posts) | applied (generalized to the author's rule; no dates or reasons) | this commit |
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

### Registry excerpt (this cohort's cast and world records and its units; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "c06ffa3",
 "cast": [],
 "world": [
  {
   "name": "Concerts and Live Events",
   "file": "bible/world/Concerts-and-Live-Events.md",
   "role": "Culture",
   "other_names": [
    "fes",
    "hololive fes",
    "SUPER EXPO",
    "EN concert",
    "Serendipity",
    "world tour",
    "3D live",
    "birthday live",
    "aftertalk"
   ]
  },
  {
   "name": "Cross-Branch Friends",
   "file": "bible/world/Cross-Branch-Friends.md",
   "role": "Relationship",
   "other_names": [
    "Death Star",
    "MoRikka",
    "LYRA",
    "Holodeath",
    "PavoNashi",
    "HOLOTORI",
    "UMISEA",
    "HoloJEI",
    "TakoNeko",
    "K.I.R.A",
    "OKFAIR",
    "Star Flower",
    "IRySora",
    "soranii",
    "Apex Predators",
    "KoMeHa",
    "BLUE·MEGAMISAMA",
    "V3LVET"
   ]
  },
  {
   "name": "Streaming Life",
   "file": "bible/world/Streaming-Life.md",
   "role": "Culture",
   "other_names": [
    "hololive livestream",
    "hololive collab",
    "off-collab",
    "offcollab",
    "superchat",
    "supa",
    "akasupa",
    "members-only stream",
    "unarchived karaoke"
   ]
  },
  {
   "name": "VTuber Persona and Lore",
   "file": "bible/world/VTuber-Persona-and-Lore.md",
   "role": "Premise",
   "other_names": [
    "VTuber lore",
    "hololive persona",
    "kayfabe",
    "in-character",
    "canonically"
   ]
  },
  {
   "name": "hololive History 2023-2026",
   "file": "bible/world/hololive-History-2023-2026.md",
   "role": "Event",
   "other_names": [
    "recent hololive history",
    "the merger",
    "the 2025 graduations",
    "holoEN's later generations"
   ]
  },
  {
   "name": "hololive History to 2022",
   "file": "bible/world/hololive-History-to-2022.md",
   "role": "Event",
   "other_names": [
    "early hololive",
    "Myth's debut"
   ]
  },
  {
   "name": "hololive",
   "file": "bible/world/hololive.md",
   "role": "Faction",
   "other_names": [
    "hololive production",
    "COVER",
    "holoEN",
    "hololive English"
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
 ]
}
```

### projects/holoen/research/qa/packets/global.md

# Audit packet: global

Snapshot: git c06ffa3. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/world/hololive.md` c9b3dd043ec2; `bible/world/Streaming-Life.md` 5b091fb1cef5; `bible/world/VTuber-Persona-and-Lore.md` f52c6b4e05a0; `bible/world/Cross-Branch-Friends.md` 5c8af2373b5c; `bible/world/Concerts-and-Live-Events.md` b69265972269; `bible/world/hololive-History-2023-2026.md` 996f74728666; `bible/world/hololive-History-to-2022.md` fb9d97a7537e

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### hololive — `bible/world/hololive.md`
**[SW] Other Names:** hololive production, COVER, holoEN, hololive English
**[SW] Description:** The VTuber agency run by COVER Corporation that the cast belongs to. Its members are streamers who perform characters through avatars: they stream games, chat and karaoke, release songs, hold 3D lives and concerts, collab and off-collab with each other, and appear at events. Since 2026-09-07 the former female-talent branches are one "hololive" (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-. Watson Amelia concluded her regular activities on 2024-09-30 and remains an affiliate who appears at events; Gawr Gura graduated on 2025-05-01 and is an alumna, as are Promise's Ceres Fauna (2025-01-03) and Nanashi Mumei (2025-04-27). Senpai and kouhai mean who debuted earlier or later, not language or nationality; formality varies by relationship; genmates are the people you debuted with. The calendar runs on debut anniversaries, birthdays, concerts and fes.
**[SW] Rules:** Management and staff stay faceless helpers: no invented staff names, business secrets, scandals or disputes. Graduations are never explained beyond "graduated." Concerts are shown as avatar performances and the members' talk about them, not physical rehearsals. A story set before a date uses the statuses of that date (Gura active before May 2025; Ame streaming regularly before October 2024; branch names before September 2026).
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2020-09 | hololive English -Myth- debuts (first EN generation) | Myth anniversaries every September |
| 2021-08 | -Council- debuts (Kronii's generation) | Council → Promise |
| 2023-10-09 | -Promise- formed (IRyS joins the remaining Council) | Kronii's group name |
| 2024-09-30 | Watson Amelia concludes general activities, stays an affiliate | Occasional guest appearances |
| 2025-05-01 | Gawr Gura graduates | Alumna; remembered in songs and anniversaries |
| 2026-07-03/04 | hololive English 4th concert "Serendipity" (LA) | Partner pairs (e.g. Kronii and Ina) |
| 2026-09-07 | The female-talent branches unify under "hololive" | Groups become units |
**Dossier · Hard Facts (continuity):**
- Baseline date 2026-09-30: one merged "hololive"; units keep their names.
- Amelia: affiliate since 2024-09-30. Gura: graduated 2025-05-01. Fauna: 2025-01-03. Mumei: 2025-04-27.
- No graduation reasons, private details or invented company conflicts.

### Streaming Life — `bible/world/Streaming-Life.md`
**[SW] Other Names:** hololive livestream, hololive collab, off-collab, offcollab, superchat, supa, akasupa, members-only stream, unarchived karaoke
**[SW] Description:** The cast's everyday medium. A stream often opens on a "Starting soon" screen with BGM and a greeting, then games, chatting, karaoke, art or a watchalong; titles use brackets like "【OFF COLLAB】". Chat scrolls beside the avatar and the member reads it aloud, argues with it and calls it "chat" (or her fans' name). Channel memberships are paid subscriptions with members-only streams; superchats ("supas") are paid highlighted messages, often read in a thank-you segment, though when and whether varies. A collab is a joint broadcast or project, remote or in person, with one or several channel perspectives ("POV"); an off-collab is in person; a 3D stream uses a full-body avatar; a relay passes the baton from channel to channel. Fans cut clips with dramatic titles. Weekly schedules and time zones decide who can collab when. Members also post on X: schedules, announcements, milestone thanks and in-character bits, each in her own written style.
**[SW] Rules:** An off-collab is in person; a collab can be remote or in person; 3D means a full-body avatar. A clip title is a fan's description, not the member's words. Chat can suggest; the member decides. Stream openings, schedules and chimes are common, not mandatory.
**Dossier · History:**
| Time | Event | Trace left |
|---|---|---|
| 2020 | Myth's first year: frequent collabs across time zones | Collab-heavy early memories |
| 2022-06 | Myth's first off-collab with all five present | Off-collabs as special events |
| 2025 | Myth relay for Gura's farewell | "One last time" streams |
**Dossier · Hard Facts (continuity):**
- Collab = joint broadcast or project (remote or in person); off-collab = in person; 3D = full-body avatar.
- Members also post on X: announcements, milestone thanks, bits in character; each has her own written
  style (see research/x-posts.md and the character files).
- Clip titles are fans' descriptions, not the members' words.

### VTuber Persona and Lore — `bible/world/VTuber-Persona-and-Lore.md`
**[SW] Other Names:** VTuber lore, hololive persona, kayfabe, in-character, canonically
**[SW] Description:** The core premise of every story: the cast are hololive talents, streamers who perform characters through avatars. Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization, an archiver who broke out of a prison for forbidden things, a gem born from human emotion, twin demonic guard dogs, Justice's queen, gremlin, ancient automaton and big-cat artist sent to catch Advent) is a persona and a running joke, not a fact of the story world, and they know it. They slip into the persona for bits ("canonically, I'm immortal"), break it casually to talk about food, games or work, and step out of it completely when something sincere needs saying. Their friendships, nicknames, songs, concerts and collabs are real parts of their lives. Off stream they are shown as their avatar selves and called by their talent names; nothing about the real people behind the avatars is ever described.
**[SW] Rules:** No one has supernatural powers. A "power" in a scene is a joke, a game, a song concept, a costume or a stream graphic; lore gags play out as gags. A member may improvise or contradict lore within a bit; an improvised joke does not automatically rewrite historical facts or permanent continuity. Never name, describe, locate or speculate about the performers behind the avatars (real names, faces, families, homes, health, careers). Public availability does not override this: identities, homes, families, health, private relationships and other prohibited personal details stay outside the story. Ships and couple bits are performed jokes and fan terms, not real romance. Characters are depicted using their public avatar designs; floating books, halos and similar elements are visual conventions, model effects or staged props, not abilities.
**Dossier · History:**
| Time | Event | Trace left |
|---|---|---|
| 2020-09 | Myth debuts with official lore profiles | Lore bits still in use |
| 2021–2026 | Lore grows through jokes, songs and events | "Canonically" callbacks |
| 2026-09-07 | Branches merge; COVER says it will update members' designs to fit their personalities, activities and future directions | Lore and looks can change officially |
**Dossier · Hard Facts (continuity):**
- Nobody in the story has supernatural powers.
- The performers' real identities are never written.
- Members depicted off-stream look like their avatars (fan convention).

### Cross-Branch Friends — `bible/world/Cross-Branch-Friends.md`
**[SW] Other Names:** Death Star, MoRikka, LYRA, Holodeath, PavoNashi, HOLOTORI, UMISEA, HoloJEI, TakoNeko, K.I.R.A, OKFAIR, Star Flower, IRySora, soranii, Apex Predators, KoMeHa, BLUE·MEGAMISAMA, V3LVET
**[SW] Description:** The cast's ties beyond EN, including JP, ID, DEV_IS and HOLOSTARS. Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones" ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix cover as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa." Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI"). Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu. Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion. Ame has "KoMeHa" with Kobo and Iroha. Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora. IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower"). Nerissa's oshi is Houshou Marine; she pairs with Tokino Sora ("BLUE·MEGAMISAMA"), sings on Moona's "100%," and Kobo calls her "Nori-chan." Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week. Of Advent: Bijou and Kaela Kovalskia are "Grindstone" (Kaela calls her "Beejoe"; Raft, Minecraft, Split Fiction), with Kureiji Ollie ("GraveStone"), Akai Haato ("Red Stone") and Ichijou Ririka (ReGLOSS; Smash Bros.) as game partners; Shiori and Vestia Zeta are the official duo "GreyScaleX" (the X is silent; "Purrfect Pair" merchandise, 2026), Pavolia Reine and Airani Iofi join her "Fanfic Club"; FUWAMOCO's oshi are Houshou Marine (Fuwawa) and Omaru Polka (Mococo), they game with Shirakami Fubuki and Hakui Koyori, and Oozora Subaru sang "HOT DUCK!" with them and Bijou. Of Justice: Kureiji Ollie is Elizabeth's kami-oshi, and Elizabeth plays with her and HOLOSTARS members in varying lineups (Code Red games; Marvel Rivals with Crimzon Ruze, her "Nephew" in an uncle–nephew bit); Elizabeth's 2026 birthday covers featured Subaru, Roboco, Sora, Choco, Marine, Korone, Polka, Nene, Watame and Iroha; Kaela Kovalskia appears in Raora's fictional basement bit ("SMITTEN"); Raora played Clubhouse Games with Haachama and Super Mario Party with Haachama and Zeta, and is "RaoRiRi" with Ririka; Cecilia plays games with Tokino Sora; at Serendipity, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame sang with Elizabeth, Gigi, Cecilia and Raora.
**[SW] Rules:** Senpai and kouhai describe relative seniority, not language or nationality; forms of address and levels of formality vary by relationship. Unit lineups belong to their period: graduates and affiliates are not current regular partners. Members of other agencies are only brief, friendly mentions.
**Dossier · Hard Facts (continuity):**
- Calli's senpai: Suisei. Kiara's oshi: Pekora. Nerissa's oshi: Marine (and Kiara).
- Kronii's steadiest cross-branch partner: Kaela. IRyS's closest JP friend: Flare.

### Concerts and Live Events — `bible/world/Concerts-and-Live-Events.md`
**[SW] Other Names:** fes, hololive fes, SUPER EXPO, EN concert, Serendipity, world tour, 3D live, birthday live, aftertalk
**[SW] Description:** The stages of the hololive year. Recurring formats: each spring, hololive fes. with hololive SUPER EXPO in Japan (a combined tradition since 2022; Calli and Kiara sang at the 2022 fes. in Makuhari, Nerissa at the 6th fes. in 2025); each summer, a hololive English concert in the US (2023 "-Connect the World-"; 2024 "-Breaking Dimensions-," New York; 2025 "-All for One-," Radio City; 2026 "Serendipity," Los Angeles, July 3–4, built on units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia), with guests Ookami Mio, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame singing alongside EN members); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet. The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn" (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (March 2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical" (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); hololive night at Dodger Stadium with Ina, IRyS and Bijou (2025-07-05); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!" (2025) and "Bound by Fate" (2026); Justice's first in-person concert performance in 3D at -All for One- (2025), CCGG's 3D live, Raora's first birthday live (2026) and Justice's second-anniversary live "How to Protect JUSTICE!" (2026). A member may stream an aftertalk afterward.
**[SW] Rules:** Concerts are told through the avatar performance and the members' talk before and after (nerves, rehearsals, interviews, aftertalks), never the performers' physical bodies. Some guests are announced, others are surprises. US concert dates are local time; streamed lives may differ by a day between the Americas and Japan. IRyS's solo concert has not happened yet at the 2026-09-30 baseline.
**Dossier · Hard Facts (continuity):**
- EN concerts: 2023-07-02, 2024-08-24/25, 2025-08-23/24, 2026-07-03/04 (Serendipity).
- IRyS's first solo concert is 2026-10-06, after the 2026-09-30 baseline.

### hololive History 2023-2026 — `bible/world/hololive-History-2023-2026.md`
**[SW] Other Names:** recent hololive history, the merger, the 2025 graduations, holoEN's later generations
**[SW] Description:** The recent past behind the present. 2023: Advent debuts (Nerissa, Shiori, Bijou, FUWAMOCO, July); DEV_IS opens with ReGLOSS; IRyS and the Council become -Promise- (October); EN holds its 1st concert. 2024: Justice debuts (June) as the "law enforcers" hunting Advent; the ENigmatic Recollection fantasy story starts (IRyS's guild "Cerulean Cup," Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!" (June); EN's 4th concert "Serendipity" in Los Angeles (July), built on units such as Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS, Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
**[SW] Rules:** After 2026-09-07 members say "from hololive"; old group names survive as units. Affiliates may appear at events; graduates appear only as memories. ENReco is a fictional story the members play in, separate from their persona lore.
**Dossier · Timeline:**
| Date | Event | Why the cast remembers it |
|---|---|---|
| 2023-03-18/19 | hololive SUPER EXPO 2023 and 4th fes. "Our Bright Parade" | — |
| 2023-03-28 | The fan app "holoplus" is introduced | — |
| 2023-04 | holoMeet 2023 ambassadors include IRyS | IRyS represents EN |
| 2023-07-02 | hololive English 1st concert "-Connect the World-" | EN's first concert |
| 2023-07-25/31 | **-Advent- revealed ("WANTED!") and debuts**: Shiori, Bijou, **Nerissa**, Fuwawa, Mococo | Nerissa's origin |
| 2023-09-09/10 | hololive DEV_IS opens with ReGLOSS (Ao, Kanade, Ririka, Raden, Hajime) | Japanese kouhai |
| 2023-10-08/09 | "CouncilRyS" 3D showcase; **-Promise- formed** (IRyS joins the Council) | Kronii's and IRyS's group |
| 2024-01-16 | Yozora Mel leaves hololive | Not discussed in stories |
| 2024-03-16/17 | SUPER EXPO 2024 and 5th fes. "Capture the Moment" | — |
| 2024-04 | holoMeet 2024 ambassadors include Hakos Baelz | — |
| 2024-06-21/22 PDT | **-Justice- debuts**: Elizabeth Rose Bloodflame, Gigi Murin, Cecilia Immergreen, Raora Panthera ("law enforcers" chasing Advent) | EN's newest kouhai |
| 2024-08-02/10 PDT | Advent 3D debuts (JST dates one day later): Shiori (08-02), Bijou (08-03), Nerissa (08-09), FUWAMOCO (08-10, with Okayu and Korone cameos) | genmates as guests |
| 2024-08-23 | "ENigmatic Recollection" (ENReco) announced: EN members in the fantasy world Libestal, via a Minecraft series, animation and songs | Guilds: IRyS in "Cerulean Cup," Nerissa and Gura in "Scarlet Wand" |
| 2024-08-23 EDT | World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 | — |
| 2024-08-24/25 EDT | EN 2nd concert "-Breaking Dimensions-" (Kings Theatre, New York), a separate event | — |
| 2024-08-28 | Minato Aqua graduates | — |
| 2024-10-12 | FUWAMOCO reach 1,000,000 subscribers, first in Advent; VTuber of the Year at the VTuber Awards (2024-12) | — |
| 2024-09-30 | **Watson Amelia concludes regular activities and stays an affiliate** | Ame appears as a guest |
| 2024-11-09 | DEV_IS second unit FLOW GLOW debuts (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya, Kikirara Vivi) | — |
| 2024-11-29 | Two months after Ame's change of status, COVER names it: "conclusion of streaming activities," distinct from graduation (affiliates can still appear in projects) | Why Ame can come back for events |
| 2025-01-03 | Ceres Fauna graduates | Promise remembers her |
| 2025-01-26 | Sakamata Chloe concludes streaming activities (affiliate) | — |
| 2025-03-08/09 | SUPER EXPO 2025 and 6th fes. "Color Rise Harmony" | Nerissa performs on day 1 |
| 2025-04 | World Tour '25 "-Synchronize!-" announced, led by Momosuzu Nene, Kureiji Ollie, **Mori Calliope, IRyS and Nerissa Ravencroft**, with guests per city (Kronii and Bae in Sydney) | Three of the cast on one tour |
| 2025-04-26 | Murasaki Shion graduates | — |
| 2025-04-27 (04-28 JST) | Nanashi Mumei graduates | Promise becomes three |
| 2025-05-01 | **Gawr Gura graduates** | Myth's first graduation; her last post: "keep swimming! always!" |
| 2025-05-02 | ENReco chapter 2 "The Chains of Fate" | — |
| 2025-07-05 | hololive night at Dodger Stadium, Los Angeles, the second hololive–Dodgers collaboration: Ina, IRyS and Bijou | a stadium sing-along |
| 2025-07-16 | hololive RECORDS label launched | — |
| 2025-08-01/02/08/09 PDT | Justice 3D showcases, each at 5 PM PDT: Elizabeth (08-01), Gigi (08-02), Cecilia (08-08), Raora (08-09) | official schedule |
| 2025-08-16 PDT | Justice group 3D collaboration stream | before their first in-person concert stage |
| 2025-08-23/24 EDT | EN 3rd concert "-All for One-" (Radio City Music Hall, New York): day 1 opens with the all-member "All for One," followed by Advent's "Genesis"; Justice's first group performance at an in-person concert venue in 3D | all fifteen EN members on one stage |
| 2025-08-29 | Advent 2nd-anniversary live "On the Run!" ("The Story of Advent") | Nerissa's group milestone |
| 2025-10-03 | Hiodoshi Ao (ReGLOSS) leaves | — |
| 2025-10-15 | Official fan club launches | — |
| 2025-11 | Raora's friendly-fire "Doom" spell in Kiara's Mage Arena collab becomes a widely shared fan meme (KYM dates the stream 11-16) | a callback |
| 2025-11-15 | hololive Indonesia 1st concert "Chromatic Future" | — |
| 2025-12-27 | Amane Kanata graduates | — |
| 2026-03-06/08 | SUPER EXPO 2026 and 7th fes. "Ridin' on Dreams" | — |
| 2026-03-27/28 PDT | Kiara and Ina's duo concert "Drawn to Dawn" (Los Angeles) | TakoTori on stage |
| 2026-05 | Gigi and Cecilia's joint CCGG 3D live and "CCGG MADNESS"; Raora's first birthday 3D live (05-10 JST / 05-09 PDT) | — |
| 2026-05-24 | ENReco chapter 3 "Broken Bonds" | — |
| 2026-06-27 PDT | Justice's second-anniversary live "How to Protect JUSTICE!" (06-28 JST) | — |
| 2026-07-03/04 PDT | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) | The current partnerships |
| 2026-07/08 | Shiori's original motion comic "Into The Void" (with Elizabeth, Gigi, Nerissa); Advent's 3rd-anniversary 3D live "Bound by Fate"; FUWAMOCO announce their first album (08-29) | — |
| 2026-07-23 | Rhythm game "hololive Dreams" released | — |
| 2026-09-07 | "hololive Next": the female-talent branches unify under **hololive**; new logo; members to get updated designs (Tokino Sora first); "hololive raku" app; TV anime "Odeholo"; 10th-anniversary countdown | The present-day setting |
| 2026-09-18 | New unit ASOBI★MAWARI-TAI! reveals its four members (Hyakuto Kyoko, Achichi Mela, Suzuna Tsuzuri, Sorashina Sopia) | — |
| 2026-09-24/25 | ASOBI★MAWARI-TAI! debut | The newest kouhai at the baseline |
| 2026-10-06 (upcoming) | IRyS's first solo concert "HOPE ||: Beyond the Stars" (Tokyo) | IRyS's next big stage |
**Dossier · Hard Facts (continuity):**
- Merger 2026-09-07. Ame affiliate since 2024-09-30. Gura graduated 2025-05-01; Fauna 2025-01-03;
  Mumei 2025-04-27 (04-28 JST).
- EN concerts: 1st 2023-07-02, 2nd 2024-08-24/25, 3rd 2025-08-23/24, 4th "Serendipity" 2026-07-03/04.

### hololive History to 2022 — `bible/world/hololive-History-to-2022.md`
**[SW] Other Names:** early hololive, Myth's debut
**[SW] Description:** The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes. "Link Your Wish" in Makuhari (03-20; Kiara: "MAKUHARI WAS ON FIRE!"), HOLOSTARS adds the unit UPROAR!! and the English group -TEMPUS-, holoMeet starts with Gura as ambassador, Calli holds her first solo concert (07-21), and Sana graduates (07-31).
**[SW] Rules:** These are memories and in-jokes, not lectures. Departures are "graduated" or "left," never explained. A story set in the past uses only what existed then.
**Dossier · Timeline:**
| Date | Event | Why the cast remembers it |
|---|---|---|
| 2017-09-07 | Tokino Sora makes COVER's first VTuber broadcast | "Sora-senpai" is everyone's origin point |
| 2017-12-21 | The "hololive" app launches | Where the name came from |
| 2018-05 / 06 | hololive 1st generation debuts (Fubuki, Matsuri, Haato, Aki, Mel, Chris) | The first "gen" |
| 2018-08 / 09 | 2nd generation (Aqua, Shion, Ayame, Choco, Subaru); Sakura Miko debuts (2018-08-01) | Senpai the EN members grew up watching |
| 2018-12 | hololive GAMERS (Fubuki, Mio; later Okayu, Korone) | Gaming senpai |
| 2018-11-15 | AZKi debuts under COVER's management | — |
| 2019-05-19 | AZKi and Hoshimachi Suisei (formerly independent) join under the INoNaKa Music label; Suisei moves to hololive's main branch on 2019-12-01 | Calli's starstruck senpai Suisei |
| 2019-06 / 09 | HOLOSTARS, COVER's male group, starts (1st gen, incl. Rikka); 2nd gen in December | Calli's MoRikka partner |
| 2019 | 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins | Kiara's oshi Pekora; Nerissa's oshi Marine; Calli's starstruck senpai Suisei |
| 2019-12 | 4th gen (Coco, Kanata, Watame, Towa, Luna); hololive, HOLOSTARS and INoNaKa Music unite as "hololive production" | The modern brand |
| 2020-04 | hololive Indonesia gen 1; hololive English auditions announced | The overseas branches |
| 2020-08 | 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) | The JP generation just before Myth |
| 2020-09-08 | hololive English announced; Myth's members appear on X | "Myth's birthday" season |
| 2020-09-12/13 | **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame | The cast's origin |
| 2020-10-22 | Gura becomes the first hololive member to reach 1 million subscribers | A Myth legend |
| 2020-12 | ID gen 2 (Ollie, Anya, Reine); hololive China ends | K.I.R.A partners (Reine, Anya) |
| 2020-12-10 | Kiara's channel briefly terminated, then restored ("#PhoenixDown") | A Kiara rebirth joke |
| 2021-05-30 | Kiara reaches 1 million: every Myth member is over 1 million | A Myth first |
| 2021-06-30 | Gura passes Kizuna AI as the most-subscribed VTuber | A Myth legend |
| 2021-07-01 | Kiryu Coco graduates | — |
| 2021-07-11 | **IRyS debuts** as the VSinger of Project: HOPE | Hope arrives |
| 2021-08-23 | **-Council- debuts:** Sana, Fauna, **Kronii**, Mumei, Bae | Kronii's origin |
| 2021-11 | 6th gen "Secret Society holoX" (La+, Lui, Koyori, Chloe, Iroha) | — |
| 2022-02-24 | Uruha Rushia leaves hololive | Not discussed in stories |
| 2022-03 | ID gen 3 (Zeta, Kaela, Kobo) | Kobo's "Mommy Kiwawa" and "Uncle Dad" |
| 2022-03-20 | hololive 3rd fes. "Link Your Wish" at Makuhari (#つながるホロライブ), day 2: Calli and Kiara perform | Calli: "My dream came true, my heart is exploding." Kiara: "MAKUHARI WAS ON FIRE!" [Observed—X posts, S4] |
| 2022-04-26 | holoMeet begins; Gura is an ambassador | Global events |
| 2022-03-19 | HOLOSTARS announces the unit UPROAR!! | — |
| 2022-07-18/23 | HOLOSTARS English -TEMPUS- (Regis Altare, Magni Dezmond, Axel Syrios, Noir Vesper) announced and debuts | Calli and Kronii's WARS partners Magni and Vesper |
| 2022-07-31 | Tsukumo Sana graduates | Council becomes four |
| 2022-09 | hololive's 5th anniversary | — |
**Dossier · Hard Facts (continuity):**
- Myth debuted 2020-09-12/13 JST; IRyS 2021-07-11; Council 2021-08-23.
- Graduations to 2022: Aloe 2020-08-31, Coco 2021-07-01, Sana 2022-07-31. Rushia left on 2022-02-24
  (no reason in stories).

Incoming claims continue in `global-incoming.md`.

### projects/holoen/research/qa/packets/global-incoming.md

# Audit packet: global (incoming claims)

Snapshot: git c06ffa3.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: lolive History 2023-2026|holoEN's later generations|Concerts and Live Events|hololive History to 2022|recent hololive history|VTuber Persona and Lore|the 2025 graduations|Cross-Branch Friends|BLUE·MEGAMISAMA|Streaming Life|Apex Predators|birthday live|Myth's debut|hololive fes|Star Flower|Serendipity|EN concert|the merger|Death Star|SUPER EXPO|world tour|aftertalk|Holodeath|PavoNashi|TakoNeko|HOLOTORI|soranii|K.I.R.A|MoRikka|IRySora|HoloJEI|3D live|KoMeHa|V3LVET|UMISEA|OKFAIR|LYRA)(

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Background`: (2026; Cecilia wrote the lyrics and directed it), a 2026 3D live, and the Serendipity concert, where she also sang "Break It Down" with Vestia Zeta and Shiori Novella and "Cloudy Sheep" with Tsunomaki Watame and Mori Calliope.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: (Cecilia wrote the lyrics; Gigi helped and designed the chibi models), a 2026 3D live, Cuphead, a Shadowverse match and Serendipity; she calls Gigi "idiot" and "FREAK" yet says Gigi "doesn't easily get rattled and is very dependable," and Gigi says she is "good at getting stuff done"; they met before debut.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Vestia Zeta (ID) and Shiori: "Break It Down" at Serendipity.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Tsunomaki Watame (JP) and Mori Calliope: "Cloudy Sheep" at Serendipity.
- `bible/characters/Cecilia-Immergreen.md › Background Timeline`: | 2026-05 | CCGG 3D live with Gigi (after-talk 05-20, secondary archive evidence); "CCGG MADNESS" MV (05-17; digital 05-29) | [Official CI1] [Observed CI3 1rIXU_4xGvY, bTxEGwMOQQI] |
- `bible/characters/Cecilia-Immergreen.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice, "CCGG MADNESS" as Autofister with Gigi, "Break It Down" with Vestia Zeta and Shiori, "Cloudy Sheep" with Tsunomaki Watame and Calli (day 1); "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official CI4, CI8] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Gigi Murin | Genmate; Autofister (unit name in the official report), also CCGG | "CCGG MADNESS" (2026), Cuphead off-collab and Shadowverse match (2025), Serendipity; she calls Gigi "idiot" and "FREAK" and admires that Gigi "doesn't easily get rattled and is very dependable!"; Gigi: "She's good at getting stuff done." Met before debut | [Official CI4] [Observed CI2, CI3] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Koseki Bijou, Shiori Novella | Advent; GAGA (Gem, Archiver, Gremlin, Automaton) with Gigi | GAGA: Trine 5, Heave Ho (2024), Phasmophobia (2025); Walking Dead watchalongs and Elden Ring with Bijou (2025); "I'm Your Treasure Box" with Bijou and Raora (not Shiori); "Break It Down" with Shiori and Zeta at Serendipity | [Observed CI2, CI3] [Official CI5, CI8] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Vestia Zeta (ID) | Cross-branch | "Break It Down" with Shiori at Serendipity (2026) | [Official CI8] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Tsunomaki Watame (JP), Mori Calliope | Cross-branch; senior | "Cloudy Sheep" at Serendipity (2026) | [Official CI8] |
- `bible/characters/Cecilia-Immergreen.md › Arc`: - **Starting point:** active at the 2026 baseline: CCGG's 3D live and Serendipity, Zelda and Spider-Man streams, her "Immersions."

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Background`: She debuted first of her generation on 2024-06-21 (PDT) in hololive English -Justice-, held her 3D showcase on 2025-08-01 (PDT), sang at the 2025 English concert ("ALiCE&u" with Nerissa and Ayunda Risu, a solo "Stellar Stellar," and the day-two opener "START AGAIN" with Calli, IRyS and Nerissa), invited guests from several branches to her 2026 birthday live, and at the 2026 Serendipity concert sang "HELP!!" with Kobo Kanaeru and Hakos Baelz and formed the unit Bloodraven with Nerissa Ravencroft ("Cruel Angel's Thesis").
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Nerissa Ravencroft: her lore "mortal enemy" from Advent and her Serendipity 2026 unit partner in Bloodraven ("Cruel Angel's Thesis"); they covered "Rondo Revolution" and shared the 2025 stages "ALiCE&u"
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Kobo Kanaeru and Hakos Baelz: "HELP!!" at Serendipity.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Mori Calliope: the LYRA cover of "III" with Amane Kanata, Koganei Niko and Ayunda Risu.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2026-05 | 2026 birthday live with guests from several branches; the performances were released as cover videos ("Live from COVER Corp. Studio") | [Observed EB3, archived credits] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Nerissa Ravencroft | Advent senior; lore "mortal enemy"; Serendipity 2026 unit Bloodraven | A "Rondo Revolution" cover; "ALiCE&u" (with Ayunda Risu) and "START AGAIN" (with Calli and IRyS) at -All for One-; "Cruel Angel's Thesis" as Bloodraven (2026); Elizabeth: "She has a beautiful voice," "the perfect harmony"; Nerissa praises her kindness. Nerissa has been "calling me her husband, my husband" (Elizabeth, 2025), a performed bit | [Official EB4, EB5] [Observed EB2] [ASR EB20, Rk03Rh8P9ps 0:38:00] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Mori Calliope | Myth senior | A TakaMori impression at debut (secondary); the LYRA cover of "III" with Amane Kanata, Koganei Niko, Calli and Ayunda Risu; "START AGAIN" on stage; "Jade Sword" guild in ENReco | [Observed EB2, secondary] [Official EB5] [EB9] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kobo Kanaeru, Ayunda Risu | ID seniors | "HELP!!" with Kobo and Hakos Baelz at Serendipity (2026); Kobo calls her "Lilis" (secondary); LYRA and "ALiCE&u" with Risu | [Observed EB2] [Official EB5, EB8] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Arc`: - **Starting point:** active at the 2026 baseline: Serendipity with Nerissa, her birthday covers with JP seniors, ENReco role-play as Lady Bloodflame, Twitch streams.

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Background`: Together they won "VTuber of the Year" at the 2024 VTuber Awards, reached one million subscribers first in Advent, made their 3D debut in August 2024, held a birthday concert in 2025, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Raora Panthera: their 2026 Serendipity unit partner in B.F.F, who drew them a shikishi before her debut.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.
- `bible/characters/Fuwawa-Abyssgard.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Mococo and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) | [Official FW4; Serendipity report] |
- `bible/characters/Fuwawa-Abyssgard.md › Arc`: - **Starting point:** active at the 2026 baseline, as half of FUWAMOCO: a TV anime song, Serendipity, their first album.

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina."
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate; fellow member of the official unit UMISEA (2021, with Aqua and Marine; the wiki also lists Chloe) | Ina drew chibi Bloop and warns that anyone who makes Gura cry faces "the wrath of Ina"; co-op games | [Observed G2 §Gura's antics and §Mascots and fans; G16] [Official G17] |

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Background`: (Gigi helped with the lyrics and designed the chibi models) and sang it at the Serendipity concert, where Gigi also sang "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO.
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: (Gigi helped with the lyrics and designed the chibi models), Cuphead, Shadowverse and Serendipity; Cecilia calls her "idiot"
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Vestia Zeta (ID) and FUWAMOCO: "MAKE IT, BREAK IT" at Serendipity.
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2026-05 | CCGG 3D live with Cecilia; "CCGG MADNESS" MV (05-17; digital 05-29) | [Official GG1, GG7] [Observed GG3] |
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice and "CCGG MADNESS" as Autofister with Cecilia (day 1); "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official GG4, GG9] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Cecilia Immergreen | Genmate; Autofister (unit name in the official report), also associated with CCGG | "CCGG MADNESS" (2026) and Serendipity; Cuphead off-collab (2025), Shadowverse match (2025); Cecilia calls her "idiot" (official interview) and "FREAK" (secondary transcription), admires that she "doesn't easily get rattled"; Gigi: "She's good at getting stuff done." Met before debut | [Official GG4] [Observed GG2, GG3] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Mococo / FUWAMOCO | Advent ("GigiMoco," "bauBau"; secondary) | Secondary accounts: with Cecilia, a guest-host prank on FUWAMOCO MORNING #167 (2025-07-28); "Bright Tonight" (2025) and "MAKE IT, BREAK IT" with Zeta at Serendipity (2026) with both twins | [Observed GG2; Mococo file] [Official GG7, GG9] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Vestia Zeta (ID) | Cross-branch | "MAKE IT, BREAK IT" with FUWAMOCO at Serendipity (2026) | [Official GG9] |
- `bible/characters/Gigi-Murin.md › Arc`: - **Starting point:** active at the 2026 baseline: CCGG's 3D live and Serendipity, her original songs, Final Fantasy XIV and rhythm games.
- `bible/characters/Gigi-Murin.md › Hard Facts`: - 3D showcase 2025-08-02 PDT; Autofister with Cecilia (unit name in the official Serendipity report).

### from IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms."
- `bible/characters/IRyS.md › [SW] Relationships`: At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou.
- `bible/characters/IRyS.md › Appearance Anchors`: - 2026: a race-queen outfit for her birthday live "Racing Towards Hope" (visor, gold accessories, blue and pink eyeshadow). [ASR R20]
- `bible/characters/IRyS.md › Background Timeline`: | 2024-11-17 | 3D live "The Devil Wears Hope" | [Observed R3 title] |
- `bible/characters/IRyS.md › Background Timeline`: | 2025-03-15/16 | Birthday: "DIAMOND GIRLFRIEND," EP "YaBAI," 3D live "HOPE UPON A STAR" | [Observed R2 §2025; R3] |
- `bible/characters/IRyS.md › Background Timeline`: | 2026-03 | Birthday live "Racing Towards Hope"; "BE MY FLAME"; solo album "DANGERyS" and solo concert announced | [Observed R2 §2026; R3] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Background`: (2025), starred with Ina and IRyS at hololive night at Dodger Stadium (2025), sang a solo and two group numbers at the 2025 English concert -All for One-, and was paired with Takanashi Kiara at the 2026 Serendipity concert.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Takanashi Kiara: her 2026 Serendipity partner ("Rocku Wawa"), who calls her a "hidden gem" and encouraged her through hard choreography for a song with Kiara and Ame; Bijou admires Kiara's "confidence," and they keep saying "67."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-11-01 | Second original song "ROCK IN!" and a 3D live | [Observed KB2 §2025] |
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2026-07-03/04 | Serendipity concert, duo with Takanashi Kiara ("Rocku Wawa") | [Official KB4] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Takanashi Kiara | Senior; Serendipity 2026 duo ("Rocku Wawa") | BG3 (2023); Kiara once asked her to perform a song with her and Ame; in the official interview Kiara calls her a "hidden gem" with "so much charm," and Bijou admires Kiara's "confidence"; their shared joke is "67" | [Official KB4] [Observed KB3; Kiara archive] |
- `bible/characters/Koseki-Bijou.md › Arc`: - **Starting point:** active member at the 2026 baseline: a 900K+ channel, two original songs, the Serendipity duo with Kiara.

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Background`: Together they won "VTuber of the Year" at the 2024 VTuber Awards, made their 3D debut in August 2024, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Raora Panthera: their 2026 Serendipity unit partner in B.F.F.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.
- `bible/characters/Mococo-Abyssgard.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Fuwawa and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) | [Official MC4; Serendipity report] |
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Raora Panthera | Justice kouhai; Serendipity 2026 unit B.F.F | Raora drew the twins a shikishi portrait before her debut and gave it "with big tears in her eyes" | [Official MC4] |
- `bible/characters/Mococo-Abyssgard.md › Arc`: - **Starting point:** active at the 2026 baseline, as half of FUWAMOCO: a TV anime song, Serendipity, their first album.

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together, and Calli admits she is "a little obsessed with her."
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star").
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka).
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Elizabeth Rose Bloodflame, Koganei Niko, Ayunda Risu and Amane Kanata: fellow LYRA vocalists on a "III" remix cover.
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2026-06-10 | Serendipity interview and partnership with Shiori Novella. | [Official C11] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Shiori Novella | 2026 Serendipity partner | Shiori calls her "Mor Mori." Together they pursue absurd premises. | [Official C11] |

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Groups`: hololive alum, hololive English -Promise- (graduated), hololive English -Council- (former unit), HOLOTORI
- `bible/characters/Nanashi-Mumei.md › [SW] Background`: (2023), joined -Promise- in 2023, reached one million subscribers on 2024-01-26 (the first in Council and Promise), held the 3D birthday live "Outside the Box" on 2024-08-05, premiered the duet "It's Not a Phase" with Fauna at the 2024 English concert, and spent her last month in collabs and covers with members across hololive.
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes.
- `bible/characters/Nanashi-Mumei.md › Core Drive`: - **Want:** in her own goals: a song in a rhythm game, learn Japanese (again), collab with senpai, improve and learn new skills, write a song on guitar, and a 3D live. [Official M1]
- `bible/characters/Nanashi-Mumei.md › Background Timeline`: | 2024-08-05 | 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori | [Observed M3 title, description] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Takanashi Kiara | Myth senior; bird unit HOLOTORI | "BUILDER BIRBS" (2021); "Kiwawa & Mumeiwi" (2022); the 4th fes. holo*27 stage (2023); "two smol beans" (2025); HOLOTORI R.E.P.O. (2025-04-18); Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies" | [Observed M2 infobox; M3; M4] |
- `bible/characters/Nanashi-Mumei.md › Story Engine`: 4. HOLOTORI meets for a bird-only game night; Mumei keeps forgetting she's a bird.

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Elizabeth Rose Bloodflame: her "mortal enemy" in their lore (a performed rivalry) from Justice and her 2026 Serendipity unit partner in Bloodraven ("Cruel Angel's Thesis"); they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai").
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Raora Panthera: Clubhouse Games (2024); with Moona, Raft and Monster Hunter Wilds as "V3LVET"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Nerissa and Kronii at Serendipity.
- `bible/characters/Nerissa-Ravencroft.md › Background Timeline`: | 2025-08-29 | Advent 2nd-anniversary 3D live "On the Run!" ("The Story of Advent") | [Observed N2 §2025] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Gigi Murin | Collaborator ("BeatDown," "SoundChaser") | A joke "child," Nerigi, at Gigi's 3D live | [Observed N2 §Relationships] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Elizabeth Rose Bloodflame | Justice member ("BloodRaven"); her 2026 Serendipity duo partner | Her "mortal enemy (lore)"; their "Rondo Revolution" cover; World Tour '24 panels together; Nerissa praises her "kindness and encouraging attitude" ("She's always looking out for me, even though I'm the senpai"); building Liz's Mii: "she's the leader of justice after all" | [Official N21; S7 tour report via world card; ASR N20] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Moona Hoshinova | ID senior ("V3LVET" with Raora) | Featured on Moona's "100% (feat. Nerissa Ravencroft)" (2025-02-16); Keep Talking and Nobody Explodes together (2024) | [Official N23; N3 title] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Ookami Mio (GAMERS): "Dottabatta Chindouchuu" with Ina and FUWAMOCO at Serendipity.
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026-06-04 | Serendipity interview and partnership with Kronii | [Official I7] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Ouro Kronii | Serendipity partner (interview 2026-06-04; unit name "Octo'Clock" in a 2026-06-24 short, I30) | A pun duo; they share Korean; Ina: "I get to... keep Kronii... all to myself... hehe" | [Official I7] [Observed Kronii file K8 §Miscellaneous] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate; fellow member of the official unit UMISEA (2021, with Minato Aqua and Houshou Marine; the wiki also lists Sakamata Chloe) [Official I31] | Ina says anyone who makes Gura cry will "face the wrath of Ina"; Ina drew chibi Bloop; a prank war is reported but [Unverified] | [Observed I2 §Relationships; Gura file G2 §Gura's antics and §Mascots and fans] |

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "Just two punny people," and both speak Korean.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity.
- `bible/characters/Ouro-Kronii.md › Background Timeline`: | 2026-03-13 | 3D birthday live; Watson Amelia guests | [Observed K33, secondary, stream t=1711] |
- `bible/characters/Ouro-Kronii.md › Background Timeline`: | 2026-06-04 | Serendipity interview and partnership with Ina | Puns, appreciation, performance goals [Official K4] |
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Ninomae Ina'nis | Serendipity partner (2026); longtime friend | They trade puns; both speak Korean | [Official K4] [Observed K8 §Miscellaneous, secondary] |
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Watson Amelia (affiliate) | Fellow EN ("Time Duo") | Guested at Kronii's 2026 3D birthday live | [Observed K8 §Relationships, K33, secondary] |

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › [SW] Background`: She held her first birthday 3D live in May 2026, and at the 2026 Serendipity concert she formed the unit B.F.F with FUWAMOCO ("Inu Neko.
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: FUWAMOCO (Fuwawa and Mococo): her Serendipity 2026 unit partners in B.F.F ("Inu Neko.
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Takanashi Kiara: "HoloEU" with Cecilia; an Italian lesson, a proposed Kiara outfit on her "Raora's Clawset" art stream, the "Doom" in Kiara's Mage Arena collab, and "What an amazing swing" with Tsunomaki Watame at Serendipity.
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Nerissa Ravencroft and Moona Hoshinova ("V3LVET"): Raft and Monster Hunter Wilds; Clubhouse Games with Nerissa.
- `bible/characters/Raora-Panthera.md › Background Timeline`: | 2026-05-10 | First birthday 3D live concert (secondary archive evidence, w37yVSXhV_c) | [Observed RP3] |
- `bible/characters/Raora-Panthera.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official RP4, RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | FUWAMOCO (Fuwawa, Mococo) | Advent seniors; Serendipity 2026 unit B.F.F | Before debut she drew them a shikishi and gave it "with big tears in her eyes"; her first impression: "AAAA!!!! They were so cute and sweet, but also really professional!" | [Official RP4] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Takanashi Kiara | Myth senior ("HoloEU" with Cecilia; secondary) | An Italian lesson (2024), a proposed outfit for Kiara on her "Raora's Clawset" art stream (2025-01-26; not a released Kiara model), an EU-snacks off-collab (2025); the "Doom" meme in Kiara's collab; "What an amazing swing" with Watame at Serendipity (2026) | [Observed RP3, RP7] [Official RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Tsunomaki Watame (JP) | JP senior | "What an amazing swing" with Kiara at Serendipity (2026) | [Official RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Nerissa Ravencroft, Moona Hoshinova | Seniors ("V3LVET," secondary) | Clubhouse Games with Nerissa (2024-12-09); Raft with both (2025-02-06); Monster Hunter Wilds as V3LVET (Nerissa's title, 2025-03-25) | [Observed RP2, RP3; Nerissa archive] |
- `bible/characters/Raora-Panthera.md › Arc`: - **Starting point:** active at the 2026 baseline: her first birthday live, Serendipity with FUWAMOCO, Pokémon, Pragmata and Hytale streams.
- `bible/characters/Raora-Panthera.md › Hard Facts`: - 3D showcase 2025-08-09 PDT. Official music list: "Gacha×Gacha ADVENTURE!" and "Draw" (Draw's premiere and release dates not yet established). Serendipity unit: B.F.F with FUWAMOCO.

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › [SW] Background`: She made her 3D debut on 2024-08-02 (PDT), sang at the 2024 and 2025 English concerts, released her first original song "Monsters and Men" on 2026-02-15, was paired with Mori Calliope at the 2026 Serendipity concert, and began her original motion comic "Into The Void" in July 2026.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Mori Calliope: her 2026 Serendipity partner in Last Writes ("When My Devil Rises"), who admits she is "a little obsessed with her"; Shiori admires Calli's "work ethic and boundaries," and they bond over dark taste and absurd deep-dives.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Cecilia and Vestia Zeta: "Break It Down" at Serendipity.
- `bible/characters/Shiori-Novella.md › Background Timeline`: | 2025-08-29 | Advent 2nd-anniversary 3D live "On the Run!" | [Observed SN2 §2025] |
- `bible/characters/Shiori-Novella.md › Background Timeline`: | 2026-07-03/04 | Serendipity concert, duo with Mori Calliope | [Official SN4] |
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Mori Calliope | Senior; Serendipity 2026 duo ("Last Writes") | Calli's "#DEEP" kids'-movie talk (2024-01-09) and Stardew Valley (2024-12-20); in the official interview Calli is "a little obsessed with her" and Shiori admires Calli's "work ethic and boundaries"; their dynamic: "Unhinged" (Calli) | [Official SN4] [Observed Calli archive] |
- `bible/characters/Shiori-Novella.md › Arc`: - **Starting point:** active member at the 2026 baseline: her first original song, the Serendipity duo with Calli, "Into The Void."

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert ("Rocku Wawa,"
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI).
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert.
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2026-06 | Serendipity interview and partnership with Koseki Bijou | [Official T10] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Koseki Bijou | Advent junior; 2026 Serendipity partner | Practical encouragement for stage work; shared "6 7" meme | [Official T10] |

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Background`: She was a guest at Kronii's 3D birthday live in March 2026.
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live.
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2026-03 | Guest spot at Kronii's 3D birthday live | [Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711] |
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Ouro Kronii | Promise member ("Time Duo") | Time traveler vs. Warden of Time; Ame guested at Kronii's 2026 3D birthday live | [Observed A2 §Relationships; Kronii file K33] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › With Myth`: - **Mori Calliope:** Bijou played her Undertale mod starring Calli with her on stream (2023-08-12); "TombStone" (Bijou), a 24-hour charity stream together (2025-06-29), Warhammer painting (2026); "FUWAMOCALLI," a collaboration name the twins say they particularly like; Fuwawa alone joined Calli and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"); Shiori was Calli's 2026 Serendipity partner (Calli, officially: "I am a little obsessed with her"; their dynamic: "Unhinged"). [Official S4] [Observed S1]
- `bible/world/Advent-Pairs.md › With Myth`: - **Takanashi Kiara:** hosted all five on HOLOTALK; an occult handcam off-collab with Shiori ("#shiotori," 2024-07-12); Baldur's Gate 3 with Bijou, Calli and Nerissa ("Killing, Two Birds, with One Stone," 2023); Bijou was her 2026 Serendipity partner ("Rocku Wawa," and a running "67" joke); Bijou recalls Kiara as "really encouraging and helpful" when Kiara asked her to perform a song with Kiara and Ame whose choreography was one of the hardest she had learned. [Official S4] [Observed S1]
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Raora Panthera:** "Graondstone" with Bijou and Kaela; FUWAMOCO's 2026 Serendipity unit partner (B.F.F), who drew them a shikishi before her debut. [Official S6] [Observed S1]
- `bible/world/Advent-Pairs.md › History`: | 2025-08-29 | "On the Run!" 2nd-anniversary 3D live | "The Story of Advent" |
- `bible/world/Advent-Pairs.md › History`: | 2026-07-03/04 | Serendipity: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth | official interviews |
- `bible/world/Advent-Pairs.md › History`: | 2026 | "Bound by Fate," 3rd-anniversary 3D live | — |
- `bible/world/Advent-Pairs.md › Hard Facts`: - Serendipity 2026 pairs: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth (official).

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Justice:** Raora Panthera, their Serendipity 2026 unit partner in B.F.F, drew them a shikishi before her debut and gave it "with big tears in her eyes"; Gigi ("GigiMoco") and Cecilia ("Cecemoco," a Chrono Trigger off-collab in 2026). [Official S4] [Observed S1; S3]
- `bible/world/FUWAMOCO.md › History`: | 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Raora ("Inu Neko. Seishun Massakari") | [Official S4; Serendipity report] |

### from Fauna and Mumei Pairs
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Mumei and Kiara are birds of HOLOTORI; Kiara calls her "Moomsies" and hosted both on HOLOTALK before they left.
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Kiara:** Mumei and Kiara are birds in HOLOTORI (with Subaru, Reine and Lui): "BUILDER BIRBS" (2021), "Kiwawa & Mumeiwi" (2022), a DECO*27 song together on the 4th fes. holo*27 stage (2023), "two smol beans" (2025-03-26) and Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies." Fauna and Kiara: "KIWAWA vs FAWNA" (2022), Pokémon Unite practice (2023), and Fauna was HOLOTALK's 32nd guest (2024-12-27), a week before she graduated. [Observed S1; S3 infobox; S4]
- `bible/world/Fauna-and-Mumei-Pairs.md › History`: | 2023-03-19 | Mumei sings with Kiara on the 4th fes. stage | HOLOTORI |
- `bible/world/Fauna-and-Mumei-Pairs.md › Conflicts and Story Hooks`: 2. (Before 2025) A HOLOTORI game night where Mumei forgets she's a bird.
- `bible/world/Fauna-and-Mumei-Pairs.md › Hard Facts`: - Fauna's oshi: Gura. Kiara's name for Mumei: "Moomsies." HOLOTORI includes Kiara and Mumei.

### from IRyS and Nerissa Pairs
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Kronii** (10 / 12 / 7 / 6 / 8 / 1): Promise unitmates since 2023 (they debuted separately), friends since 2021 (fan unit K.I.R.A with Reine and Anya). Two-player games and watchalongs: A Way Out (2021–22), "School Days (THE CHRISTMAS ANIME)" (2023-12-21), Buckshot Roulette "You Or Me But For Real" (2024-11), Bokura "Left Side Right Side" (2025-02), a Powerwash Simulator race, "May The Best Maid Win" (2025-07-08). In 2026, after Kronii's 3D birthday live "The Goddess Descends," IRyS said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." [Observed S1 titles; S2, secondary; ASR IRyS file R20, second model agrees]

### from Justice Pairs
- `bible/world/Justice-Pairs.md › [SW] Description`: Inside Justice: Gigi and Cecilia are an officially billed duo, Autofister (also CCGG), with the song "CCGG MADNESS," a joint 2026 3D live and a Serendipity unit; a secondary transcription has Cecilia's "Ew!
- `bible/world/Justice-Pairs.md › [SW] Description`: Beyond EN: Elizabeth plays with Kureiji Ollie and HOLOSTARS members in varying lineups (Code Red games; Marvel Rivals with Crimzon Ruze, her "Nephew" in an uncle–nephew bit) and sang LYRA's "III" with FLOW GLOW's Koganei Niko; Kaela appears in Raora's fictional basement bit; Elizabeth records covers with JP members; Cecilia plays games with Tokino Sora; at Serendipity, Elizabeth sang with Kobo Kanaeru, Gigi and Cecilia with Vestia Zeta, and Cecilia and Raora with Tsunomaki Watame.
- `bible/world/Justice-Pairs.md › Inside Justice`: - **Gigi and Cecilia ("CCGG," "Autofister"):** an officially billed duo with shared music, live performances and a Serendipity 2026 unit (Autofister), an original song, "CCGG MADNESS" (MV 2026-05-17), and a CCGG 3D live with an after-talk (May 2026). In the official interview Gigi said "Who is she!!! … Jokes aside, I hope everyone's ready for some MADNESS!!!!" and Cecilia answered "idiot"; Gigi admires that Cecilia is "good at getting stuff done," Cecilia that Gigi "doesn't easily get rattled and is very dependable!" They met before debut. A secondary transcription records Cecilia's "Ew! Get away from me, you FREAK!"; the teasing runs both ways. Collabs: A Way Out and 7 Days to Die (2024), Portal 2 co-op (2024-07-10), a Cuphead off-collab (2025-05-30), Shadowverse "CECE VS GIGI" (2025-08-17). [Official S3 interview06] [Observed S1; S2, secondary]
- `bible/world/Justice-Pairs.md › With Advent`: - **Nerissa:** Elizabeth is her "mortal enemy (lore)" and duet partner (Bloodraven, the official Serendipity 2026 billing, "Cruel Angel's Thesis"; a "Rondo Revolution" cover; "ALiCE&u" with guest Ayunda Risu at -All for One-). Gigi: "BeatDown"/"SoundChaser," The Planet Crafter (2024-10-11), "III" together at -All for One-, a joke child "Nerigi." Cecilia: "AutoTune," Unravel Two ("Trying to capture Nerissa through crocheting!!!," 2024-08-17). Raora: Clubhouse Games with Nerissa (2024-12-09); with Moona Hoshinova, Raft (2025-02-06) and Monster Hunter Wilds as "V3LVET" (Nerissa's title, 2025-03-25). Gigi also helped with the "CCGG MADNESS" lyrics alongside Nerissa (MV credits). [Official S3 interview07, S6] [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Advent`: - **Shiori:** Elizabeth ("NovelFlame," "BloodQuill"; secondary) and Gigi voice parts in Shiori's non-canon motion comic "Into The Void" (2026; episode 2 also credits Calli); Gigi ("NovelGrem") games with her often (Heave Ho, a Fateful Findings watchalong, Project Zomboid, Phasmophobia; Eden Eternal was Kiara, Shiori and Gigi); the "Fanfic Club" (Gigi, Shiori, Pavolia Reine, Airani Iofifteen) is a separate group from "GAGA" (Gigi, Cecilia, Shiori, Bijou); Raora: a 2024 outfit-design collab (2024-12-05) and Blood Typers with Kronii and Bijou (2025-06-10); Cecilia: "Break It Down" with Vestia Zeta at Serendipity; Gigi: "MONSTER" with Ina and Kronii at -All for One-. [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Advent`: - **FUWAMOCO:** Raora is their Serendipity unit partner in B.F.F (official billing, "Inu Neko. Seishun Massakari"), who drew them a shikishi before debut and gave it "with big tears in her eyes"; the twins met Justice before debut to give advice; Gigi and Cecilia guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit ("GigiMoco" and "Cecemoco" are pair labels with Mococo); Cecilia played Chrono Trigger with Mococo, including 2026 off-collabs; Gigi sang "Bright Tonight" (2025) with the twins, IRyS and Kronii, and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity; Fuwawa, Gigi and Calli as "2 Creatures + 1 Reaper" (2026, Fuwawa alone); the twins sang in Elizabeth's 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha. [Official S3 interview03] [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Myth`: - **Mori Calliope:** Gigi's "Grem Reaper": Mouthwashing (2024-11-14), Fast Food Simulator (2025-02-04), R.E.P.O. (2025-05-02), The Boba Teashop (2025-06-04); Gigi shouts her full name ("MORI CALLIOPE!") and has jokes about getting Calli to play League of Legends (secondary observation). Unverified: Calli reportedly said Gigi changed how she felt about her talent name (kept off the card). Raora hit 500k during Galaxy Burger with Calli (2025-03-26), and Raora, Gigi and Calli played Elden Ring Nightreign (2025-06-11). Elizabeth surprised Calli with a TakaMori skit at debut, and they are fellow LYRA vocalists on a remix-version cover of "III" (with Kanata, Niko and Risu). Cecilia sang "Cloudy Sheep" with Calli and Tsunomaki Watame at Serendipity. [Observed S1; S2] [Official S7]
- `bible/world/Justice-Pairs.md › With Myth`: - **Takanashi Kiara:** "HoloEU" with Cecilia and Raora (secondary label): Raora teaches Kiara Italian (a lesson, 2024-10-04), designed a proposed Kiara outfit on her "Raora's Clawset" art stream (2025-01-26; not a released model) and held an EU-snacks off-collab (2025-03-11); Raora and Kiara sang "What an amazing swing" with Tsunomaki Watame at Serendipity; Eden Eternal with Gigi and Shiori (2024); Kiara and Cecilia spoke German in their first exchange (Kiara's 2024 birthday) ("EterniTea"); Gigi and Kiara are "Ultra Orange" (Reanimal, 2026-04-03); Kiara calls Elizabeth "Erby Berby" ("Eternal Flame"). [Observed S1; S2]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **ID:** Kaela Kovalskia with Raora ("SMITTEN," "Graondstone," "PizzaTimeSmith" with Kronii; in Raora's lore Kaela lives in her basement); Kureiji Ollie is Elizabeth's "kami-oshi" per public-profile wikis (collabs with HOLOSTARS members in varying lineups, including Code Red games; "High Tide" with Kronii at -All for One-), and Ollie did a chat-and-art collab with Raora (2024-09-06); Moona Hoshinova with Raora ("V3LVET"); Anya Melfissa visited Raora (2025-02-11); Vestia Zeta and Haachama in a Mario Party off-collab with Raora (2024-10-08); Ayunda Risu with Elizabeth ("LYRA," "ALiCE&u"); Vestia Zeta sang "Giri Giri" with Elizabeth at her 2025 3D showcase, which Elizabeth arranged and choreographed [ASR, Elizabeth file EB20]; Pavolia Reine and Airani Iofi with Gigi in the "Fanfic Club"; Kobo Kanaeru calls Elizabeth "Lilis" (secondary) and sang "HELP!!" with Elizabeth and Bae at Serendipity; Vestia Zeta also sang "Break It Down" with Cecilia and Shiori and "MAKE IT, BREAK IT" with Gigi and FUWAMOCO at Serendipity. [Observed S1; S2] [Official S6, S7]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone ("IT'S LOVE," iwnHChZq0N8, credits read by Claude); FUWAMOCO with Polka, Nene, Watame and Iroha; her 2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members). Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is "RaoRiRi" with Ichijou Ririka; "OkaGigi" is a secondary-documented name for Gigi and Nekomata Okayu, with no concrete shared activity sourced (dossier only). Tsunomaki Watame sang "Cloudy Sheep" with Calli and Cecilia and "What an amazing swing" with Kiara and Raora at Serendipity. FLOW GLOW: Koganei Niko sang with Elizabeth in LYRA. [Observed S1; S2] [Official S6, S7]
- `bible/world/Justice-Pairs.md › History`: | 2026-05 | CCGG 3D live, "CCGG MADNESS" | Gigi and Cecilia's unit |
- `bible/world/Justice-Pairs.md › History`: | 2026-07-03/04 PDT | Serendipity: units Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora); guests' songs with Justice members: "HELP!!" (Kobo, Bae, Elizabeth), "Break It Down" (Zeta, Shiori, Cecilia), "Cloudy Sheep" (Watame, Calli, Cecilia), "MAKE IT, BREAK IT" (Zeta, FUWAMOCO, Gigi), "What an amazing swing" (Watame, Kiara, Raora) | [Official S3, S7] |
- `bible/world/Justice-Pairs.md › Hard Facts`: - Serendipity 2026 units with Justice members (official billing): Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora).

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Ina and Gura: the official ocean unit UMISEA (2021); Ina promised "the wrath of Ina" to anyone who makes Gura cry.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Kiara and Ame** (20 / 26 / 30 / 8 / 9 / 1): Ame is Kiara's EN oshi; Kiara calls herself "#1 Ame gosling" and "#1 Teamate" and credits Ame for help with her 3D productions. Ame made the intro video for Kiara's talk show HOLOTALK (2020) and was its 31st guest (2024-09-22); they did a 3D off-collab "In Ame's awesome studio" (2023-06). Ame on a reunion: "Kiara like, threw herself at me… she hugged me!" Ame, now an affiliate, performed at Kiara's 2025 spring concert and guested at her 2026 birthday live. [Observed S2 Kiara §Likes and dislikes, §2020; S3 Ame §Quotes, §2025–§2026, secondary; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Ina and Gura** (71 / 28 / 10 / 3 / 3 / 2): fellow members of the official ocean unit UMISEA (September 2021); Ina drew chibi Bloop and promised "the wrath of Ina" to anyone who makes Gura cry; Gura once directed a lost Ina in Minecraft by hitting a block with her pickaxe. [Official UMISEA announcement; S4 §Gura's antics, secondary]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |

### from Octo'Clock
- `bible/world/OctoClock.md › [SW] Description`: Ninomae Ina'nis and Ouro Kronii, the octopus and the clock: longstanding collaborators whose 2026 Serendipity pairing foregrounds their shared puns, interests and performance work.
- `bible/world/OctoClock.md › [SW] Description`: They share Korean, a love of puns and occasional FGO streams, and in 2026 they were paired for hololive English's 4th concert "Serendipity"
- `bible/world/OctoClock.md › [SW] Description`: They had met in person, found matching jackets and shared interests, and MC'd together at a hololive fes.
- `bible/world/OctoClock.md › How It Works`: - **Official pairing (2026):** paired for the 4th concert "Serendipity" (Shrine Auditorium, Los Angeles, 2026-07-03/04); Kronii's short "#holoSerendipity It's Time for Octo'Clock!" (2026-06-24) names the unit. [Official S2; Observed S3]
- `bible/world/OctoClock.md › How It Works`: - Shared history they mention: performing together in group numbers, meeting in person, matching jackets (as they tell it) and shared interests, and MCing together at a hololive fes. Goal: to "nail the performance"; Kronii adds, mostly joking, that they want to "look cooler than everyone else." [Official S2]
- `bible/world/OctoClock.md › History`: | 2026-06-04 | Official Serendipity interview | Their own words |
- `bible/world/OctoClock.md › History`: | 2026-07-03/04 | Serendipity concert, Los Angeles | Their stage pairing |
- `bible/world/OctoClock.md › Hard Facts`: - Serendipity: 2026-07-03/04, Shrine Auditorium, Los Angeles.

### from Time Duo
- `bible/world/Time-Duo.md › [SW] Description`: Ame, now an affiliate, guested at Kronii's March 2026 birthday live, "The Goddess Descends."
- `bible/world/Time-Duo.md › How It Works`: - **2026:** Ame guested at Kronii's March 2026 birthday live, "The Goddess Descends" (2026-03-13 in the Americas, 03-14 in Japan; "Fall in Grace" in an earlier note refers to the same broadcast). [Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711; S3 §2026, secondary]
- `bible/world/Time-Duo.md › History`: | 2026-03-13 | Ame guests at Kronii's 3D birthday live | The affiliate's cameo |
- `bible/world/Time-Duo.md › Hard Facts`: - Ame guested at Kronii's 3D birthday live on 2026-03-13.

### from hololive -Advent-
- `bible/world/hololive--Advent.md › [SW] Description`: (2026), and 2026 Serendipity pairs Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth and FUWAMOCO–Raora.
- `bible/world/hololive--Advent.md › How the Group Works`: - **The premise as a bit:** each member was sealed in The Cell for being "untouchable"; Nerissa, the "Demon of Sound," in the story "stole" the master key on the way out; her avatar wears it on a keychain. The next generation, -Justice-, are law enforcers sent to catch the five fugitives, so Advent × Justice collabs can use prisoner-and-guard jokes (a 2026 merch reveal: "Like prisoner and my prison guard"). [Official S3; Observed S1, S2 §Lore, secondary; ASR Nerissa file N20, multi-speaker, not attributed] Nerissa calls Justice's Elizabeth Rose Bloodflame her "mortal enemy (lore)"; the two covered "Rondo Revolution" together and were a duo at the 2026 Serendipity concert, where Nerissa praised Elizabeth's "kindness and encouraging attitude" ("She's always looking out for me, even though I'm the senpai"). [Official S7]
- `bible/world/hololive--Advent.md › History`: | 2025, 2026 | hololive SUPER EXPO with -Justice- | Prisoner-and-guard bits |
- `bible/world/hololive--Advent.md › History`: | 2025-08-29 | 2nd-anniversary 3D live "On the Run!" with "The Story of Advent" (five chapters, five songs) | — |
- `bible/world/hololive--Advent.md › History`: | 2026-07-03/04 | Serendipity pairs: Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth, FUWAMOCO–Raora | [Official S7, S10] |
- `bible/world/hololive--Advent.md › History`: | 2026-09 | Renamed "hololive -Advent-" in the merger | Current name |

### from hololive -Justice-
- `bible/world/hololive--Justice.md › [SW] Description`: (2026); individual 3D showcases on August 1, 2, 8 and 9, 2025 (PDT) and a group 3D stream on August 16; their first in-person concert performance in 3D at the 2025 English concert; at the 2026 Serendipity concert the units Autofister (Gigi and Cecilia), Bloodraven (Elizabeth and Nerissa) and B.F.F (Raora and FUWAMOCO), with Elizabeth also singing alongside Kobo Kanaeru and Hakos Baelz, Cecilia alongside Vestia Zeta and Shiori and alongside Tsunomaki Watame and Calli, Gigi with Zeta and FUWAMOCO, and Raora with Watame and Kiara; and the second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive--Justice.md › History`: | 2026-05 | CCGG (Gigi and Cecilia) joint 3D live (secondary event coverage) and "CCGG MADNESS"; Raora's first birthday 3D live (05-10 JST / 05-09 PDT; secondary metadata) | — |
- `bible/world/hololive--Justice.md › History`: | 2026-07-03/04 PDT | Serendipity: day 1 "SUPERNOVA SUPER GIRL" (Justice); Autofister (Gigi & Cecilia, "CCGG MADNESS"); "HELP!!" (Kobo Kanaeru with Bae and Elizabeth); "Break It Down" (Vestia Zeta with Shiori and Cecilia); "Cloudy Sheep" (Tsunomaki Watame with Calli and Cecilia). Day 2: the Advent+Justice medley ("Rebellion," "ABOVE BELOW"); Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"); "MAKE IT, BREAK IT" (Zeta, FUWAMOCO and Gigi); "What an amazing swing" (Watame with Kiara and Raora); B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari") | [Official S6, S8] |
- `bible/world/hololive--Justice.md › Hard Facts`: - Serendipity 2026 units (official billing): Autofister, Bloodraven, B.F.F.

### from hololive -Myth-
- `bible/world/hololive--Myth.md › [SW] Description`: On 2026-09-19 Calli, Kiara and Ina held the 6th Anniversary 3D LIVE "Seasons From Within."
- `bible/world/hololive--Myth.md › History`: | 2026-09-19 (announced) | Myth 6th Anniversary 3D LIVE "Seasons From Within" announced with Calli, Kiara and Ina (S3, an official hololive English post); not verified as held | The current three, as announced |
- `bible/world/hololive--Myth.md › Conflicts and Story Hooks`: 4. The 6th anniversary 3D live: nerves, rehearsal jokes, a message for the absent two.

### from hololive -Promise-
- `bible/world/hololive--Promise.md › [SW] Description`: IRyS and Bae keep the "BaeRyS" bit of being "married" and "divorced," which turned "Monopoly" into a fandom euphemism, and they are also creative partners: paired for the 2026 Serendipity concert, IRyS leans on Bae's "strong vision" when she's indecisive, Bae admires IRyS's humor that makes everyone comfortable, and they call their dynamic "a can of worms" and "Complicated."
- `bible/world/hololive--Promise.md › How the Group Works`: - **IRyS and Bae at Serendipity (2026):** paired for the 4th concert, their first stage as a duo. IRyS: Bae "always has a strong vision" for projects, so when IRyS is "indecisive or wishy-washy" she turns to Bae's opinion, and she admires Bae's creativity; Bae: IRyS was "the very first senpai I had ever met," and she admires IRyS's "easy-going nature and natural humor" that makes everyone "laugh and feel comfortable." Their unit dynamic, in their words: "a can of worms lol" (IRyS), "Complicated XD" (Bae). [Official S6]
- `bible/world/hololive--Promise.md › How the Group Works`: - **After 2025:** the group is three. Kronii's 2026 activity includes a 3D birthday live with Ame as a guest, the Serendipity pairing with Ina and her EP. [Observed Kronii file K4, K33, K36]

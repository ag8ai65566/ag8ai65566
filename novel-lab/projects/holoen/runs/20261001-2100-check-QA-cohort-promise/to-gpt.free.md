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
- **Snapshot:** your working directory is a clean checkout of the packets' snapshot commit, made by Claude for
  this run. Do not run git and do not compute or compare hashes; procedure step 1 is satisfied by this note.
  Report the snapshot commit in Coverage.
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
    "source": "bible/characters/Ceres-Fauna.md › Background"
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
    "BaeRyS"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. IRyS is a VTuber and singer whose lore, a persona she plays for laughs, makes her a nephilim who was once the embodiment of hope in \"The Paradise\" and reawakened in an age of despair to deliver hope through her songs; she doesn't speak of what came before.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2021-07-11",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/IRyS.md › Background"
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
    "Myumyei",
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
    "source": "bible/characters/Nanashi-Mumei.md › Background"
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
    "debut": null,
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Ouro-Kronii.md › Background"
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
  }
 ]
}
```

### projects/holoen/research/qa/packets/promise.md

# Audit packet: promise

Snapshot: git c06ffa3. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Ouro-Kronii.md` fd6dfc4140b5; `bible/characters/IRyS.md` a87383909b3a; `bible/characters/Ceres-Fauna.md` 58177a0ddea1; `bible/characters/Nanashi-Mumei.md` 6e7d1d1f7ba0; `bible/world/hololive--Promise.md` 0d2fcd380c0a; `bible/world/Time-Duo.md` 329fef0a8daa; `bible/world/Time-and-Death.md` e1239bb9b626; `bible/world/OctoClock.md` 5f0169e12e8b; `bible/world/Fauna-and-Mumei-Pairs.md` 537910125c8d; `bible/world/IRyS-and-Nerissa-Pairs.md` 2d7d1c266294

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Ouro Kronii — `bible/characters/Ouro-Kronii.md`
**[SW] Groups:** hololive, hololive -Promise-, Promise, Council (former unit name), Octo'clock
**[SW] Other Names:** Kronii, Warden of Time, オーロ・クロニー, Kronini, Kroniicopter, Kronster, Tam Tender, Owo-senpai
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. Kronii is a VTuber whose lore, a persona she plays deadpan, makes her the Warden of Time, the third concept created by the gods and the one most bound to humankind. Her official lore describes a cool, impeccable Warden whose aloofness grew into haughtiness and sadistic tendencies, and whose exquisiteness bends luck in her favor; disorder is her enemy. She debuted in August 2021 with hololive English -Council-. In October 2023, she joined hololive English -Promise- alongside IRyS, Ceres Fauna, Nanashi Mumei and Hakos Baelz. Following Fauna's and Mumei's graduations in 2025, its current members are Kronii, IRyS and Baelz, and since the 2026 merger the unit belongs to the single hololive brand. Her fans are the Kronies, which she also calls Kromies. Her mascot is Boros, a small white ouroboros snake. She is known for a Minecraft era spent building bunkers (the Bunkeronii). Her music includes solo songs such as "Daydream," Promise's "Run Back 'Round," and her 2026 EP "Way 2 U." In 2026 she also began a performance partnership with Ninomae Ina'nis. She jokes that she is 60.
**[SW] Relationships:** Ninomae Ina'nis: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "Just two punny people," and both speak Korean. Hakos Baelz: genmate who calls her a "tsundere granny." IRyS: Promise genmate and two-player rival (A Way Out, Bokura, a Powerwash "Best Maid" race) who once wondered aloud how Kronii sounds when she's scared, and in 2026 said she could pull off Kronii's goddess look "somehow." Nanashi Mumei (graduated 2025): Council genmate and frequent partner (KronMei), from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet in Mumei's last month (2025). Ceres Fauna (graduated 2025): Council genmate who described Kronii's "gap moe"; they once defused bombs speaking only in ASMR. Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster," Kronii teases her about being 1 cm taller, and they bill themselves "Time and Death" in horror co-ops and mock feuds. Kaela Kovalskia: a recurring cross-branch co-op partner for years (Raft, Luma Island, Old Market Simulator) and her partner at a 2024 World Tour panel. Gigi Murin: Fatal Fury and Hytale ("TimeChaser"; "Clockwork Orange" with Cecilia), "MONSTER" on stage and "Bright Tonight" (2025). Cecilia Immergreen: Cecilia calls her "Owo-senpai," and Kronii has called Cecilia a "CLANKER." Raora Panthera: "Pizza Time" partner (Portal 2, 2024; Backrooms Cleanup Crew, 2026), who used "Tam Tender" for Kronii's ENReco character. Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni." Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months. Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live. Shiori Novella: they hosted "Rating Your Clocks" together (2025), and they sang "MONSTER" with Ina and Gigi at the 2025 English concert. Koseki Bijou: Lethal Company and Yu-Gi-Oh collabs. FUWAMOCO: "WatchDog." Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity.
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
| 2026-03-13 | 3D birthday live; Watson Amelia guests | [Observed K33, secondary, stream t=1711] |
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
**[SW] Groups:** hololive -Promise-, Promise, hololive English -Project: HOPE- (former), hololive English (former branch name), BaeRyS
**[SW] Other Names:** Irys, SeisoRyS, YabaIRyS
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. IRyS is a VTuber and singer whose lore, a persona she plays for laughs, makes her a nephilim who was once the embodiment of hope in "The Paradise" and reawakened in an age of despair to deliver hope through her songs; she doesn't speak of what came before. She debuted on 2021-07-11 as hololive English's VSinger, the sole member of -Project: HOPE-, and joined -Promise- with Fauna, Kronii, Mumei and Bae in 2023; since the 2026 merger she is in hololive -Promise-. Her fans are IRyStocrats and her members Nephamily. She has released several EPs, held 3D lives such as "The Devil Wears Hope" (2024), "HOPE UPON A STAR" (2025) and "Racing Towards Hope" (2026, in a race-queen outfit), released her first full-length album, "DANGERyS," on 2026-07-12; her first solo concert, "HOPE ||: Beyond the Stars," is scheduled in Tokyo for 2026-10-06.
**[SW] Relationships:** Hakos Baelz: Promise unitmate, her "BaeRyS" partner in a running bit of getting "married" and "divorced" (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms." Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae. Ouro Kronii: Promise unitmate and two-player rival; IRyS wondered aloud how Kronii sounds when she's scared, and said she, "a half-angel, half-demon Nephilim," could pull off Kronii's goddess look "somehow." Shiranui Flare: a recurring Japanese collaborator (horror camping, Splatoon matches, karaoke). Ninomae Ina'nis: an early duo partner (It Takes Two) who still games with her. Nerissa Ravencroft: Advent kouhai and fellow singer; IRyS guested at Nerissa's 2025 3D concert. Koseki Bijou ("Biboo"): her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina they starred at hololive night at Dodger Stadium (2025). Tsukumo Sana (graduated): co-designed her mascots Bloom & Gloom. Ceres Fauna (graduated 2025): Promise unitmate and Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Nanashi Mumei (graduated 2025): Promise unitmate; they played Overwatch together during Mumei's farewell week. Shiori Novella: Monster Hunter Wilds and PEAK (2025). Gigi Murin: a "Cerulean Cup" guildmate in the ENigmatic Recollection story. Cecilia Immergreen: Elden Ring Nightreign with Bijou (2025). Gigi Murin, Ouro Kronii and FUWAMOCO: "Bright Tonight" (2025). Elizabeth Rose Bloodflame: "START AGAIN" with Calli and Nerissa at the 2025 concert. At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou.
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
| 2026-09-07 | Branch merger; her unit is "hololive -Promise-" | [Observed R2] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-07-11; birthday March 7; 162 cm; fans IRyStocrats, members Nephamily; emoji 💎.
- Unit: hololive -Promise- (since 2023-10-09; "hololive English -Promise-" before 2026-09).
- Solo concert "HOPE ||: Beyond the Stars," 2026-10-06, Tokyo (announced).

### Ceres Fauna — `bible/characters/Ceres-Fauna.md`
**[SW] Groups:** hololive alum, hololive English -Promise- (graduated), hololive English -Council- (former unit)
**[SW] Other Names:** Fauna, Faufau, Fawna, Keeper of Nature, Mother Nature, Gamer Kirin, Ceres-chan
**[SW] Background:** Fauna is a hololive alum: she graduated on 2025-01-03. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore, a persona she plays for laughs, makes her the Keeper of "Nature," the second concept created by the gods: a druid with kirin blood whose horns are tree branches, who came online to win humans over and lead them back to nature. She debuted on 2021-08-23 with hololive English -Council-, joined -Promise- with IRyS, Kronii, Mumei and Bae in 2023, won VTuber Awards for ASMR and for chatting streams, sang at both hololive English concerts (2023, and 2024, where she and Mumei premiered their duet "It's Not a Phase") and in Promise's musical "The Broken Promise" (2024), reached one million subscribers on 2024-12-27, and finished her Minecraft World Tree on 2024-12-31, days before graduating. Her fans are Saplings, her members Faunatics, and her mascot is Nemu, a sleepy kirin.
**[SW] Relationships:** Nanashi Mumei (graduated 2025): Council and Promise genmate and recurring collaborator. Their public comedy includes Fauna's exaggerated protective and possessive bits ("return to nature"); Mumei's macabre humor complicates the apparent protector/protected roles. They premiered their original duet "It's Not a Phase" at the 2024 English concert (released 2024-12-22), and one of Fauna's last streams was the two of them reading Wikipedia talk-page fights. Hakos Baelz: genmate who called her "a natural mama" at debut; her horror partner ("BAE & FAUNA'S MONTH OF HORRORS," 2022; an Amnesia: The Bunker off-collab, 2023). Ouro Kronii: genmate; they defused bombs speaking only in ASMR (2021), and Fauna praised Kronii's "gap moe." IRyS: Promise unitmate from 2023 and an earlier CouncilRyS collaborator; Switch Sports rival ("BATTLE OF THE CENTURY," 2022). Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke. Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated. Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA" (2022); Fauna was Kiara's HOLOTALK guest a week before graduating. Kaela Kovalskia (ID): Phasmophobia and Minecraft together. -Justice-: kouhai she made play a board game she invented (2024). Shirogane Noel: a JP senior she admires. Nerissa Ravencroft: Advent kouhai; with Shiori they sang "Lonely in Gorgeous" at the 2024 English concert, and Nerissa greets her on X as "Fauna-senpai!!!" Koseki Bijou: "Coach Fauna" in Bijou's Hitman runs and a "Sweaty TryHard Gamers" squad with Bae and Kaela. FUWAMOCO: helped on the World Tree's last day (2024-12-31). Shiori Novella: the third voice of "Lonely in Gorgeous." Cecilia Immergreen: a book and shoujo-manga tropes ranking (2024; "Green Women"). Gigi Murin: Silent Hill 2 and the 2024 Coughing Baby Award Show ("FruitPunch," a secondary pair name).
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
**[SW] Other Names:** Mumei, Moom, Moomers, Meimei, Moomsies, Mumi-chan, Myumyei, Guardian of Civilization, Towl
**[SW] Background:** Mumei is a hololive alum: she graduated on 2025-04-27 (04-28 JST). She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her the Guardian of "Civilization," the only member of her generation created not by the gods but by mankind's efforts; she chose an owl's form for wisdom, and too many transformations made her brain "more bird," so she forgets things, including her original name and her age. Lonely on her travels, she made a friend out of paper: a paper bag called simply "Friend," so she can't forget his name. She debuted on 2021-08-23 with hololive English -Council-, released the original songs "A New Start" (2022) and "mumei" (2023), joined -Promise- in 2023, reached one million subscribers on 2024-01-26 (the first in Council and Promise), held the 3D birthday live "Outside the Box" on 2024-08-05, premiered the duet "It's Not a Phase" with Fauna at the 2024 English concert, and spent her last month in collabs and covers with members across hololive. Her fans are Hoomans, her members Owl Pals, and her stream descriptions end with ":D".
**[SW] Relationships:** Ceres Fauna (graduated 2025-01): Council and Promise genmate and recurring collaborator; their comedy includes Fauna's exaggerated protective, possessive bits ("return to nature"), complicated by Mumei's macabre humor; they premiered their duet "It's Not a Phase" at the 2024 English concert. Hakos Baelz: genmate and a recurring collab partner (Mad-Lib theatre in 2021, Overwatch in 2025). Ouro Kronii ("KronMei"): genmate and frequent partner, from "The Grim Adventures of Mumei and Kronii!" (2021) to a "Donut Hole" cover duet (2025-04). IRyS: Promise unitmate from 2023; they played Overwatch together in Mumei's farewell week, then a Promise R.E.P.O. collab with IRyS, Kronii and Bae (2025-04-24). Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday. Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes. (2023), and Mumei was Kiara's HOLOTALK guest in her last week. Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week. Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week. Ninomae Ina'nis: fellow artist, drawing collabs. Mori Calliope: "ANATOMY REVIEW." Nerissa Ravencroft: "EMO HOURS" (2023), "Beyond the way" with Kiara at the 2024 concert, "SAD GIRL HOURS" (2025). Koseki Bijou ("Stone Age"): Portal 2 and Marvel Rivals; at arm wrestling Mumei rates her a loss because "she is a rock." Gigi Murin: Echo Point Nova as "A Towl and a Gremlin." Cecilia Immergreen: Halo co-op ("Automatowl"). FUWAMOCO ("Fuwamoomco"): Overwatch. JP: Takane Lui ("Q&A With Bird Sisters"), Tokoyami Towa (calls her "Mumi-chan"), Akai Haato (Minecraft); Inugami Korone (a duet cover in her last week) and Okayu, Nene and Koyori, guests at "Outside the Box." Shiori Novella: B-movie watchalongs (Neil Breen, Kung Pow; 2025). Raora Panthera: a joint drawing stream (2025).
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
| 2025-03-09 | 6th fes. "Color Rise Harmony," day 2 | [Observed M2 §2025] |
| 2025-04 | A farewell month of collabs across hololive: Overwatch with IRyS (04-22), a cover of "とんとんまーえ！" with Inugami Korone (04-23), Promise R.E.P.O. with IRyS, Kronii and Bae (04-24); last chatting stream with calls (04-26); 3D graduation stream (04-27, 04-28 JST) | [Observed M2; M3 titles] |
**Dossier · Hard Facts (continuity):**
- Debut 2021-08-23 (JST); graduated 2025-04-27 (04-28 JST); birthday August 4; 156 cm; fans Hoomans;
  members Owl Pals; mascot Friend; emoji 🪶.
- Unit: -Council- (2021–23), hololive English -Promise- (2023–25).

### hololive -Promise- — `bible/world/hololive--Promise.md`
**[SW] Other Names:** hololive -Promise-, holoPromise, hololive Council, holoCouncil, CouncilRyS, BaeRyS
**[SW] Description:** The group of Ouro Kronii and IRyS, hololive -Promise-: IRyS, Ouro Kronii and Hakos Baelz at the 2026 baseline. It grew from the English -Council- generation (August 2021), whose personas were themed around concepts (Kronii is Time); Sana graduated from Council in 2022, before Promise existed. IRyS ("Hope") and the four remaining Council members were billed together as "CouncilRyS" and formed Promise on 2023-10-08 PDT / 10-09 JST; Fauna (Nature, the soft kirin protective of Mumei) and Mumei (Civilization, the forgetful owl and a recurring collaborator with Bae) graduated in 2025. Bae calls Kronii "too talented, savage, and a tsundere granny"; Fauna once described Kronii's "gap moe," the cute side that shows when she's flustered; IRyS has wondered aloud how Kronii sounds when she's scared. IRyS and Bae keep the "BaeRyS" bit of being "married" and "divorced," which turned "Monopoly" into a fandom euphemism, and they are also creative partners: paired for the 2026 Serendipity concert, IRyS leans on Bae's "strong vision" when she's indecisive, Bae admires IRyS's humor that makes everyone comfortable, and they call their dynamic "a can of worms" and "Complicated."
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
**[SW] Description:** Ninomae Ina'nis and Ouro Kronii, the octopus and the clock: longstanding collaborators whose 2026 Serendipity pairing foregrounds their shared puns, interests and performance work. They share Korean, a love of puns and occasional FGO streams, and in 2026 they were paired for hololive English's 4th concert "Serendipity" (Los Angeles, July 3–4) under the name "Octo'Clock" (the official report spells it "Octo'clock"), performing "Bad Apple." In their official interview Kronii called them "Just two punny people waiting to deliver the pun-chline to everyone" and praised Ina as "very hard-working and ambitious"; Ina said "I get to…keep Kronii….all to myself…..hehe…hehehe" and admired Kronii's "unmatched charisma whenever she sings." They had met in person, found matching jackets and shared interests, and MC'd together at a hololive fes. Their goal was to "nail the performance," and, Kronii added mostly as a joke, "look cooler than everyone else."
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
| 2023-10-09 | -Promise- formed: IRyS and Kronii genmates | — |
| 2025 | Nerissa's 3D concert with Calli and IRyS as guests; "OVER//RIDE" duet | Calli × Nerissa |
| 2026-04-23 | Nerissa's Tomodachi Life Miis of IRyS and Ina | — |
**Dossier · Hard Facts (continuity):**
- IRyS debuted 2021-07-11 (senior to Kronii by a month, to Nerissa by two years); Nerissa 2023-07-31.
- CHADCast = IRyS, Calli, Bae. KiaRissa = Kiara and Nerissa. IRyS and Kronii are -Promise- genmates.
- 2026 baseline: IRyS–Gura and Nerissa–Gura are memories; Ame appears as an affiliate guest.

Incoming claims continue in `promise-incoming.md`.

### projects/holoen/research/qa/packets/promise-incoming.md

# Audit packet: promise (incoming claims)

Snapshot: git c06ffa3.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: ardian of Civilization|IRyS and Nerissa Pairs|Fauna and Mumei Pairs|hololive -Promise-|Nerissa and Calli|Calli and Kronii|Kronii and Calli|It's Not a Phase|hololive Council|Mumei and Kronii|Nerissa and IRyS|Keeper of Nature|Mumei and Kiara|Mumei and Fauna|IRyS and Kronii|Fauna and Mumei|Time and Death|Warden of Time|Kronii and Ame|Ina and Kronii|Kronii and Ina|Ame and Kronii|Fauna and Gura|Mother Nature|Nanashi Mumei|IRyS and Ina|Kroniicopter|Ceres Fauna|Ouro Kronii|Gamer Kirin|holoPromise|holoCouncil|Octo'Clock|Tam Tender|Ceres-chan|CouncilRyS|Octo'clock|Owo-senpai|Mumi-chan|Time Duo|SeisoRyS|YabaIRyS|KiaRissa|Moomsies|オーロ・クロニー|Kronster|CHADCast|Myumyei|Council|KronMei|MorIRyS|Kronini|Moomers|Promise|Faufau|Meimei|BaeRyS|Kronii|Fawna|Mumei|Fauna|gumei|Irys|IRyS|Moom|Towl)(

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: IRyS and Bijou: Elden Ring Nightreign.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Nanashi Mumei ("Automatowl"): Halo co-op.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Ouro Kronii: Kronii has called her "CLANKER"; she calls Kronii "Owo-senpai"; "Clockwork Orange" with Gigi.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Ceres Fauna ("Green Women"): a shoujo-tropes ranking.
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Nanashi Mumei | Promise alumna ("Automatowl," secondary) | Halo: Reach (2024), "Ask us anything" (2025); the nickname "Myumyei" is unverified and not used | [Observed CI2, CI3] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Ouro Kronii | Senior ("Clockwork Orange" with Gigi; secondary) | Phogs, Squirreled Away (2025); Kronii has called her "CLANKER"; she calls Kronii "Owo-senpai" (secondary transcriptions; not a call-and-response) | [Observed CI3; Kronii file] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Ceres Fauna | Promise alumna ("Green Women") | A shoujo-manga tropes ranking (2024) | [Observed CI2, CI3] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Gawr Gura, IRyS, Hakos Baelz | Seniors | Keep Talking and Nobody Explodes and The Forest with Gura (2025); Elden Ring Nightreign with IRyS and Bijou (2025); "BratTea" with Bae (secondary) | [Observed CI2, CI3] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Background`: She debuted first of her generation on 2024-06-21 (PDT) in hololive English -Justice-, held her 3D showcase on 2025-08-01 (PDT), sang at the 2025 English concert ("ALiCE&u" with Nerissa and Ayunda Risu, a solo "Stellar Stellar," and the day-two opener "START AGAIN" with Calli, IRyS and Nerissa), invited guests from several branches to her 2026 birthday live, and at the 2026 Serendipity concert sang "HELP!!" with Kobo Kanaeru and Hakos Baelz and formed the unit Bloodraven with Nerissa Ravencroft ("Cruel Angel's Thesis").
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: (with Calli and IRyS); Elizabeth says Nerissa "has a beautiful voice,"
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Kureiji Ollie (ID): her kami-oshi and "Code Red" partner (PEAK with HOLOSTARS' Machina X Flayon and Jurard T Rexford; "High Tide" on stage with Kronii); Crimzon Ruze (HOLOSTARS) is her "Nephew" in a Marvel Rivals uncle–nephew bit.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie | [Official EB5] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Nerissa Ravencroft | Advent senior; lore "mortal enemy"; Serendipity 2026 unit Bloodraven | A "Rondo Revolution" cover; "ALiCE&u" (with Ayunda Risu) and "START AGAIN" (with Calli and IRyS) at -All for One-; "Cruel Angel's Thesis" as Bloodraven (2026); Elizabeth: "She has a beautiful voice," "the perfect harmony"; Nerissa praises her kindness. Nerissa has been "calling me her husband, my husband" (Elizabeth, 2025), a performed bit | [Official EB4, EB5] [Observed EB2] [ASR EB20, Rk03Rh8P9ps 0:38:00] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kureiji Ollie | ID senior; her "kami-oshi" (secondary); "HoloRed" | "Code Red" collabs: Liars Bar with Ollie and Jurard (2024), PEAK with Ollie, Flayon and Jurard (2025); "High Tide" with Kronii and Ollie at -All for One-; the 2026 "Yona Yona Dance" cover | [Observed EB2, EB3] [Official EB5] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Story Engine`: 1. Elizabeth impersonates Kronii on a call and Kronii answers.

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Ouro Kronii: "WatchDog."
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "Fuwamoomco"

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Raora Panthera: R.E.P.O. with Kiara and Kronii (2025).
- `bible/characters/Gawr-Gura.md › Voice Profile`: - Measured (G18; chat and horror windows, with game audio mixed in): median pitch about 245–270 Hz (Kronii's chat windows 177–188 Hz); about 120–140 words per minute of speech in the 2024 chat. Sample results only; they do not establish a general ranking among genmates. (The earlier caption-timing estimate is withdrawn.)
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ceres Fauna, Nanashi Mumei, Ouro Kronii | Council members ("SNOTCast") | Shared podcast-style collabs; Kronii rivalry and "senpai tax" bits are reported but [Unverified] (title-level only) | [Observed G2 §Relationships; G8b titles] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | IRyS | Promise member | Sincere praise of IRyS's new look (clip title) | [Observed G8b title] |

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Background`: "Countach" with Hakos Baelz and Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, "III" with Nerissa).
- `bible/characters/Gigi-Murin.md › [SW] Background`: (presented on her 2025 birthday), "Bright Tonight" with IRyS, Kronii and FUWAMOCO (2025), and "enough"
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Ouro Kronii: Fatal Fury and Hytale; "MONSTER" with Kronii, Ina and Shiori.
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: IRyS, Kronii and FUWAMOCO: "Bright Tonight."
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Ceres Fauna: Silent Hill 2 and The Coughing Baby Award Show.
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Nanashi Mumei: Echo Point Nova.
- `bible/characters/Gigi-Murin.md › Behavioral Traits`: 7. A creative, sentimental side: she performs original songs: "I'll still be here" (presented 2025-10-18, digital 10-20), "Bright Tonight" (a group release with IRyS, Kronii and FUWAMOCO, 2025-12-22), "enough" (2026-06-25; composed by FLAVORFOLEY) and "CCGG MADNESS" with Cecilia (MV 2026-05-17, digital 05-29; lyrics by Cecilia with help from Nerissa and Gigi; chibi-model design by Gigi). [Official GG1 music list, GG7] [Observed GG3 credits]
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa | [Official GG5] |
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2025-12-22 | "Bright Tonight" with IRyS, Kronii and FUWAMOCO released | [Official GG7] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Ouro Kronii | Senior ("TimeChaser"; "Clockwork Orange" with Cecilia; secondary pair names) | Fatal Fury (2025), Hytale (2026); "MONSTER" at -All for One-; "Bright Tonight" (2025) | [Observed GG2, GG3] [Official GG5, GG7] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | IRyS | Senior | "Bright Tonight" (2025) | [Official GG7] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Ceres Fauna, Nanashi Mumei | Promise alumnae ("FruitPunch"; "A Towl and a Gremlin"; secondary) | Fauna: The Coughing Baby Award Show; Mumei: Echo Point Nova | [Observed GG2, GG3] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Background`: (2025), starred with Ina and IRyS at hololive night at Dodger Stadium (2025), sang a solo and two group numbers at the 2025 English concert -All for One-, and was paired with Takanashi Kiara at the 2026 Serendipity concert.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: IRyS: her horror co-op partner (Dead Space 3, Resident Evil 6); with Ina, they headlined hololive night at Dodger Stadium (2025).
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "Stone Age"; Mumei rated her a loss at arm wrestling because "she is a rock."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Ceres Fauna (graduated 2025): her Hitman "coach."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Ouro Kronii: Lethal Company and Yu-Gi-Oh. -Justice-: GAGA with Gigi and Cecilia; Graondstone with Raora; "I'm Your Treasure Box" with Cecilia and Raora at the 2025 concert; Cecilia's Walking Dead watchalongs and a 2025 Elden Ring stream Bijou joined partway; Raora's 2024 cooking off-collab, billed with Bijou as her assistant.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-07-05 | hololive night at Dodger Stadium with Ina and IRyS: a stadium sing-along and the first VTuber stream from the stadium | [Official KB9] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | IRyS | Senior | Her frequent horror co-op partner: Resident Evil 6 "LAS CHICAS GUAPAS" (2026-04-29), Dead Space 3 (2026-01); Overwatch "Please carry me Senpai!!" (2023) | [Observed KB3; IRyS archive] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Nanashi Mumei | Senior (graduated 2025; "Stone Age") | Portal 2 co-op (2023); Marvel Rivals in Mumei's last week (2025-04-23); Mumei rated her a loss at arm wrestling because "she is a rock" | [Observed KB3; Mumei file] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Ceres Fauna | Senior (graduated 2025) | "Coach" Fauna in Hitman (2023, 2024); PlateUp! as "The Sweaty TryHard Gamers" | [Observed KB3] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Ouro Kronii | Senior | Lethal Company (2023), Yu-Gi-Oh (2025), Blood Typers (2025) | [Observed KB3] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Ouro Kronii: "WatchDog."
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "Fuwamoomco."
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Ouro Kronii | Senior ("WatchDog," with Fuwawa) | Among Us, Team Fortress 2, 7 Days to Die (2023–24) | [Observed MC2; MC3] |

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Groups`: hololive, hololive -Myth-, Myth, CHADCast, hololive English (former branch name), Last Writes
- `bible/characters/Mori-Calliope.md › [SW] Background`: She co-hosts the CHADCast podcast with IRyS and Hakos Baelz, and she started a 2026 performance partnership with Shiori Novella.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: IRyS and Hakos Baelz: her CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022).
- `bible/characters/Mori-Calliope.md › Voice Profile`: - Measured (C30, chat windows): median pitch 197–214 Hz, the second lowest of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz). The wiki's hololive-wide ranking was not measured. She is the fastest talker of the six: about 161–186 words per minute of speech while chatting (Kronii 120–127, Ina 81–95). Approximate values for relative comparison.
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2022 | CHADCast begins with IRyS and Hakos Baelz. | [Observed C12] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | IRyS, Hakos Baelz | CHADCast cohosts | A chaotic podcast trio. Bae calls her "Cori Malliope." | [Observed C12; C4 nickname list, secondary] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Ouro Kronii | Fellow EN | Calli calls her "Kronster." Running bit: the 1 cm height difference. | [Observed C21-jVfm_LhwTHQ clip title; Kronii's wiki page, secondary] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Background`: (2025) with Calli and IRyS as guests, sang the duet "OVER//RIDE" with Calli (2025), and released "OYOME♡HOLIC" and "Blue World"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, and they held a 2025 "BIRB GIRLS"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: IRyS: fellow singer who guested at that concert.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025); with Kiara they sang "Beyond the way" at the 2024 English concert.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Ceres Fauna (graduated 2025): the senpai she excitedly replied to on her first day on X ("Fauna-senpai!!!"); with Shiori they sang "Lonely in Gorgeous" at the same concert.
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Nerissa and Kronii at Serendipity.
- `bible/characters/Nerissa-Ravencroft.md › Voice Profile`: - Measured (N20; a 2026 solo chat): median pitch about 214 Hz (p10–p90 172–297 Hz), a mid-range speaking voice like IRyS's (214–226 Hz), lower than Kiara or Gura; about 159 words per minute of speech. Group-stream windows read higher (284–289 Hz) because several voices share them. Sample results only.
- `bible/characters/Nerissa-Ravencroft.md › Background Timeline`: | 2025-05-24 | 3D concert "Requiem for Love – A JukeBox Musical" (guests incl. Calli, IRyS) | [Observed N3 titles] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Takanashi Kiara | Senior and her oshi ("KiaRissa") | Self-described KFP member; in lore, a former KFP employee | [Observed N2] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | IRyS | Senior and fellow singer | Guest at Nerissa's 2025 3D concert ("Missing Promise"); Monster Hunter Wilds (2025); Nerissa made Miis of Ina and IRyS in Tomodachi Life (2026) | [Observed N3 titles] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Octo'clock
- `bible/characters/Ninomae-Inanis.md › [SW] Background`: She released her first EP, re:VISION, and held the duo concert Drawn to Dawn with Takanashi Kiara in 2026, and she partners with Ouro Kronii.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Ouro Kronii: her partner for the 2026 Serendipity concert (as Octo'clock, "Bad Apple"); "two punny people" who share Korean, and Ina jokes about keeping Kronii all to herself.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Koseki Bijou: "wooden shovel" buddy ("TakoRocky") whose collab outfit Ina designed; with IRyS they starred at hololive night at Dodger Stadium (2025).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: IRyS: early duo partner (It Takes Two, "It Takes Tako & Hope") who still games with her; Nerissa Ravencroft put them both in her Tomodachi Life island.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): a fellow artist who drew with her on stream (2023, 2025).
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Shiori Novella: a "Rate Your Fears" nightmare talk (2024) and "MONSTER" with Kronii and Gigi at the 2025 English concert.
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **Code-switching:** English-dominant, with sparse Japanese reaction words: "yabe," "kusa," "seiso," "hazukashii," "warau na," "kouhai." She reads and sometimes answers Japanese chat, and she is improving her Japanese. She shares Korean with Kronii. [Observed I2 §Quotes and §Likes and dislikes; Kronii file K8 §Miscellaneous, secondary] "Marine-senpai" for a senior she admires. [Observed—published interview I18]
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **How she addresses people:** "you guys," "everyone," "chat," and fans as "Takodachi" (the official fan name is the Tentacult). Members by first or short name ("Calli," "Kiara," "Ame," "Gura," "Kronii," "Bae," "Biboo," "CC"); a full name signals a mock-serious scold. New members are "kouhais." She gives her own name surname-first. [Official I1] [Observed I3 captions; I2 §Mascot and fans]
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - Measured (I29, 2026 chat): median pitch 223–232 Hz, in the middle of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz), so "mid" rather than "low"; about 81–95 words per minute of speech in that one 2026 chat stream (Kronii 120–127, Calli 161–186 in their chat windows). A 2021 game stream measures 210–214 Hz and 68–116 words per minute (its opening chat 116). Sample results only; they do not establish a general ranking among genmates.
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026-06-04 | Serendipity interview and partnership with Kronii | [Official I7] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Ouro Kronii | Serendipity partner (interview 2026-06-04; unit name "Octo'Clock" in a 2026-06-24 short, I30) | A pun duo; they share Korean; Ina: "I get to... keep Kronii... all to myself... hehe" | [Official I7] [Observed Kronii file K8 §Miscellaneous] |
- `bible/characters/Ninomae-Inanis.md › Story Engine`: 4. Kronii refuses to react to a pun, and the next conversation becomes a contest. (GPT)

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Ouro Kronii ("Pizza Time"): Portal 2 and Backrooms Cleanup Crew; in ENReco Raora called Kronii's character "Tam Tender."
- `bible/characters/Raora-Panthera.md › Voice Profile`: - Chattini bits: "Oh, you're one of those zipper Chattini. I love those kind." "No, Chattini, you cannot get any of my plushies." "I swear I live in the Justice headquarters. I promise." [ASR RP20, 0:33:19, 0:36:04, 0:37:54; both models on the quoted spans]
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Ouro Kronii | Promise senior ("Pizza Time") | Portal 2 (2024-11-26, "w/ KRONII!! #PizzaTime"), Backrooms Cleanup Crew (2026); in ENReco she called Kronii's character "Tam Tender" (secondary transcription) | [Observed RP2, RP3; Kronii file] |

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

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they held a 2025 "BIRB GIRLS"
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left.
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Ouro Kronii | Promise member ("Sundial", fan term) | Kiara announced she was a fan before Kronii debuted; language exchange | [Observed T2 §Relationships; Kronii file K17] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Nanashi Mumei (graduated) | Council member | Kiara coached her "Kikkeriki" | [Observed T5-eivcnjk6yeE clip title] |

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Background`: She was a guest at Kronii's 3D birthday live in March 2026.
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live.
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week.
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Cecilia Immergreen and Gigi: Borderlands 2 with Mumei (2024).
- `bible/characters/Watson-Amelia.md › Voice Profile`: - **How she addresses people:** "you guys" by default; "chat" occasionally; "Teamates" (one m, official) on big occasions; members "Investigators." Members by name ("Gura," "Calli," "Ina," "Kiara," "Kronii"); Bubba, her dog mascot. She gives her name in English order, "Amelia Watson." [Official A1] [Observed A3 captions; A2 §Mascots and fans]
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2026-03 | Guest spot at Kronii's 3D birthday live | [Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711] |
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Ouro Kronii | Promise member ("Time Duo") | Time traveler vs. Warden of Time; Ame guested at Kronii's 2026 3D birthday live | [Observed A2 §Relationships; Kronii file K33] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › [SW] Description`: With seniors: Mori Calliope starred in Bijou's Undertale mod and did a 24-hour charity stream with her, shares "FUWAMOCALLI" with the twins (a collaboration name they say they particularly like), and was Shiori's 2026 concert partner; Kiara hosted all five on HOLOTALK, encouraged Bijou through hard choreography, and partnered her in 2026 ("Rocku Wawa"); IRyS is Bijou's horror co-op partner, and Bijou, Ina and IRyS starred at hololive night at Dodger Stadium (2025); Shiori and Kronii hosted "Rating Your Clocks" together in March 2025.
- `bible/world/Advent-Pairs.md › With Myth`: - **Ninomae Ina'nis:** "TakoRocky" with Bijou (Monster Hunter; Ina designed their 2025 Monster Hunter Wilds outfits); "Rate Your Fears" with Shiori (2024); "SHALLYS" with FUWAMOCO and Cecilia at the 2025 concert; with Bijou and IRyS, starred at hololive night at Dodger Stadium (2025-07-05). [Observed S1; X post via wiki] [Official S5, S8]
- `bible/world/Advent-Pairs.md › With Promise`: - **IRyS:** Bijou's horror co-op partner (Dead Space 3, Resident Evil 6, 2026); "Please carry me Senpai!!" in Overwatch (2023); hololive night at Dodger Stadium with Bijou and Ina (2025-07-05); Monster Hunter Wilds and PEAK with Shiori (2025). [Observed S1] [Official S8]
- `bible/world/Advent-Pairs.md › With Promise`: - **Ouro Kronii:** "WatchDog" with FUWAMOCO; Shiori and Kronii hosted "Rating Your Clocks" together (2025-03-27, AjwIazuu8gg; the description credits help with collecting submissions); "MONSTER" with Ina, Shiori and Gigi at the 2025 concert. [Observed S1] [Official S5]
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
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous" [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before and separate from "-Breaking Dimensions-"), Jakarta (11-09), Singapore (11-30, with a pre-concert panel of Kaela Kovalskia and Ouro Kronii), Atlanta (12-15, a panel of Nerissa and Elizabeth Rose Bloodflame), Kuala Lumpur (12-21, Nerissa and Elizabeth again) and Taipei (2025-01-18, the finale) [Official S7]; and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **holoMeet** (since 2022): overseas fan events with yearly ambassadors (Gura 2022, IRyS 2023, Bae 2024, Bijou 2025, Gigi 2026). [Observed S1]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive night at Dodger Stadium (2025-07-05, Los Angeles):** the second hololive–Dodgers collaboration, starring Ina, IRyS and Bijou, with a stadium sing-along during the game. [Official, https://hololive.hololivepro.com/en/news/20250731-01-353/]
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ninomae Ina'nis | 3D live "Pleiades" (2024-12-28); "Drawn to Dawn" with Kiara; World Tour '24 performer; Serendipity with Kronii | Ina file I20, I7; S3 title |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ouro Kronii | World Tour '24 Singapore pre-concert panel with Kaela Kovalskia; World Tour '25 Sydney guest; 3D birthday live "The Goddess Descends" with a new outfit (2026-03-13/14, Ame as guest); Serendipity with Ina | Kronii file K33, K4; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | IRyS | Promise musical "The Broken Promise" (2024-12-14); 3D lives "The Devil Wears Hope" (2024-11-17), "HOPE UPON A STAR" (2025-03-16), "Racing Towards Hope" (2026-03, race-queen outfit); World Tour '25 lead; Serendipity with Hakos Baelz; first solo concert "HOPE ||: Beyond the Stars," Tokyo, 2026-10-06 | IRyS file R2, R3; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Nerissa Ravencroft | 6th fes day 1 (2025-03-08); 3D concert "Requiem for Love – A JukeBox Musical" (2025-05-24, with Calli and IRyS as guests); Advent's "On the Run!" (2025-08-29); World Tour '24 panels with Elizabeth (Atlanta, Kuala Lumpur); World Tour '25 lead; Serendipity with Elizabeth | Nerissa file N2, N3; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Watson Amelia | As an affiliate: guest at Kronii's 2026 birthday live | Kronii file K33 |
- `bible/world/Concerts-and-Live-Events.md › How It Works in Stories`: - After a concert, a member may stream an aftertalk ("BDay Live Aftertalk") and gush about outfits and guests. [Observed IRyS file R20]
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 2. IRyS counts down to her first solo concert in Tokyo; Kronii and Calli send messages.
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 5. A tour stop in Sydney: Kronii joins Calli, IRyS and Nerissa as a guest.
- `bible/world/Concerts-and-Live-Events.md › Hard Facts`: - IRyS's first solo concert is 2026-10-06, after the 2026-09-30 baseline.

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: IRyS's recurring Japanese collaborator is Shiranui Flare (horror camping, Splatoon, karaoke), and she sings with Moona, Suisei and AZKi ("Star Flower").
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Before graduating, Fauna's recurring ID partner was Kaela, and Mumei flew with HOLOTORI (she hosted a Q&A with Lui titled "Q&A With Bird Sisters") and recorded a duet cover with Inugami Korone in her last week.
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Takanashi Kiara:** Usada Pekora is her oshi ("Senpai! Be my guide for the day!", 2020; HOLOTALK's 24th guest, 2022). Pavolia Reine is a recurring collaborator on her channel (30 streams; their pair name "PavoNashi"; a VR "vacation," a Minecraft summer festival; the bird unit "HOLOTORI" with Subaru, Reine, Mumei and Lui); Kobo calls her "Mommy Kiwawa." Other units: "O'riends" (Momosuzu Nene), "KoAra Connect" (Hakui Koyori), "SunMoon"/"Eclipse" (Moona Hoshinova). Outside hololive: "PomuTori" (Pomu Rainpuff), "Mintori" (Mint Fantôme). [Observed S1; S2 Kiara; Kiara file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Watson Amelia** (affiliate): "KoMeHa" (Kobo Kanaeru, Kazama Iroha), "ZetAme" (Vestia Zeta); outside hololive, "SelAMei" (with Mumei and Selen Tatsuki). [Observed S2 Ame]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ouro Kronii:** Kaela Kovalskia is a recurring cross-branch collaborator (21 streams; survival and sim co-ops every few months: Raft 2023–24, Panicore, Luma Island 2024, Old Market Simulator 2025; together at a pre-concert panel in Singapore on World Tour '24 [Official S6]); also "soranii" with Tokino Sora, fan unit K.I.R.A (with IRyS, Reine, Anya), and Raora Panthera of Justice (Portal 2, Split Fiction, No Man's Sky 2026; "Pizza Time"). [Observed S1; S2 Kronii; Kronii file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **IRyS:** Shiranui Flare is a recurring collaborator (23 streams, 11 in 2024): horror and camping co-ops ("ふーたんとキャンプだ！"), Splatoon private matches, an off-collab karaoke (2025-03); units "Star Flower" (Moona, Suisei, AZKi), "IRySora" (Tokino Sora), "ReiRyS" (Reine), "OKFAIR" (Ollie, Kronii, Fauna, Anya, Reine). [Observed S1; S2 IRyS]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ceres Fauna** (graduated): her first official collab outside her generation was with Pavolia Reine (Clubhouse 51, 2021-10-12, per the wiki; Minecraft "WITH REINE," 2022-01-19, ronEFZPwxqc); Kaela Kovalskia was a recurring partner ("Fearless & Fearful vs Ghosts," an ID Minecraft server tour); she admired Shirogane Noel. [Observed S1; Fauna file F2 §2021, §Trivia, secondary]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Nanashi Mumei** (graduated): HOLOTORI with Kiara, Subaru, Reine and Lui ("【MUMEI + LUI】Q&A With Bird Sisters !!!," 2025-04-19, fEO6kSCseE0); drawing collabs with Airani Iofi ("Doodles with IOFI," 2022-04-14, 2dWx7xg48xc; "SWIMSUITS!! with IOFI!," 2023-01-30, XCXF08GMUHY); a duet cover of "とんとんまーえ！" with Inugami Korone (2025-04-23, P6GLC_HnCUU), and Okayu, Korone, Nene and Koyori as guests at her 3D live "Outside the Box" (2024-08-05, gl7CwlEg2ZI); Minecraft "Peace & Love with HAACHAMA" (2025); Tokoyami Towa calls her "Mumi-chan." [Observed S1; Mumei file M2]
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 2. Kronii and Kaela's endless sim co-op hits the in-game stock market.
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 3. IRyS and Flare go camping in a horror game again; IRyS insists she isn't scared.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Kronii's steadiest cross-branch partner: Kaela. IRyS's closest JP friend: Flare.

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Myth and Promise:** "FUWAMOCALLI" with Mori Calliope (a twin game show and Smash in 2023, a tea party, an off-collab karaoke in 2024); Fuwawa also joined Mori Calliope and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"; Fuwawa's post, not a twin appearance); "Detective Dogs" with Watson Amelia (Escape Simulator, 2024-09-24); "WatchDog" with Ouro Kronii; "Fuwamoomco" with Nanashi Mumei (Overwatch, 2025-03-01); they helped Ceres Fauna on her last World Tree stream (2024-12-31); Kiara hosted them on HOLOTALK (2023). [Observed S1; S3; Mumei, Calli, Kiara archives]

### from Justice Pairs
- `bible/world/Justice-Pairs.md › [SW] Description`: With seniors: Gigi repeatedly uses Calli's full name and jokes about getting her into League of Legends; within HoloEU, Raora teaches Kiara Italian and Cecilia speaks German with her; Cecilia plays up a rivalry with Ina; Kronii is Raora's "Pizza Time" collaborator and Gigi's Fatal Fury and Hytale partner, and secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai"; Automatowl names Cecilia and Mumei.
- `bible/world/Justice-Pairs.md › With Advent`: - **Shiori:** Elizabeth ("NovelFlame," "BloodQuill"; secondary) and Gigi voice parts in Shiori's non-canon motion comic "Into The Void" (2026; episode 2 also credits Calli); Gigi ("NovelGrem") games with her often (Heave Ho, a Fateful Findings watchalong, Project Zomboid, Phasmophobia; Eden Eternal was Kiara, Shiori and Gigi); the "Fanfic Club" (Gigi, Shiori, Pavolia Reine, Airani Iofifteen) is a separate group from "GAGA" (Gigi, Cecilia, Shiori, Bijou); Raora: a 2024 outfit-design collab (2024-12-05) and Blood Typers with Kronii and Bijou (2025-06-10); Cecilia: "Break It Down" with Vestia Zeta at Serendipity; Gigi: "MONSTER" with Ina and Kronii at -All for One-. [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Advent`: - **FUWAMOCO:** Raora is their Serendipity unit partner in B.F.F (official billing, "Inu Neko. Seishun Massakari"), who drew them a shikishi before debut and gave it "with big tears in her eyes"; the twins met Justice before debut to give advice; Gigi and Cecilia guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit ("GigiMoco" and "Cecemoco" are pair labels with Mococo); Cecilia played Chrono Trigger with Mococo, including 2026 off-collabs; Gigi sang "Bright Tonight" (2025) with the twins, IRyS and Kronii, and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity; Fuwawa, Gigi and Calli as "2 Creatures + 1 Reaper" (2026, Fuwawa alone); the twins sang in Elizabeth's 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha. [Official S3 interview03] [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Myth`: - **Ninomae Ina'nis:** Cecilia's Stranger of Paradise partner (2025), with a rivalry bit Cecilia plays up (secondary); "SHALLYS" with Cecilia and FUWAMOCO, "MONSTER" with Gigi, Kronii and Shiori, "Neko Kaburi-Na" with Raora, Shiori and Oozora Subaru (all at -All for One-); Rabbit and Steel with Cecilia, Bijou and Gigi (2024); Blood Typers with Gigi (2025-04-11); Puyo Puyo Tetris 2 with Raora (2025-06-02); the Monster Hunter Wilds sponsored launch with Gigi, Raora and Bijou (2025-03-01). [Observed S1]
- `bible/world/Justice-Pairs.md › With Myth`: - **Gawr Gura (graduated):** Keep Talking and Nobody Explodes and The Forest with Cecilia (2025-02); R.E.P.O. with Raora, Kiara and Kronii (2025-04-13). **Watson Amelia (affiliate):** in ENReco's role-play story, Gigi's Gonathon and Ame's Jyonathan marry (secondary; "ClueChaser"); Borderlands 2 with Cecilia, Gigi and Mumei (2024-08-09). [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Promise`: - **Ouro Kronii:** "Pizza Time" with Raora (Portal 2, 2024-11-26; Backrooms Cleanup Crew, 2026-06-11; in ENReco Raora used "Tam Tender" for Kronii's character, secondary), "TimeChaser" with Gigi (Fatal Fury, 2025-05-03; Hytale, 2026-04-14), "Clockwork Orange" with Gigi and Cecilia; secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai" nickname; "Bright Tonight" and "MONSTER" with Gigi. [Observed S1; S2; Kronii file] [Official S6]
- `bible/world/Justice-Pairs.md › With Promise`: - **Hakos Baelz:** "BratTea" with Cecilia; "Countach" with Gigi and guest Kureiji Ollie at -All for One-. **IRyS:** Elden Ring Nightreign with Cecilia and Bijou (2025-06-05); "Bright Tonight" with Gigi (2025); "START AGAIN" with Elizabeth at -All for One-. [Observed S1; S2] [Official S6]
- `bible/world/Justice-Pairs.md › With Promise`: - **Ceres Fauna (graduated 2025):** Gigi's "FruitPunch" (Silent Hill 2; The Coughing Baby Award Show, 2024-12-28) and League of Legends with Elizabeth, Gigi, Cecilia and Nerissa (2024); Cecilia's "Green Women" (a shoujo-tropes ranking, 2024-09-23). **Nanashi Mumei (graduated 2025):** Cecilia's "Automatowl" (Halo: Reach, 2024; "Ask us anything," 2025-04-12; the nickname "Myumyei" is unverified); Gigi's Echo Point Nova ("A Towl and a Gremlin," 2024-10-15); an art stream with Raora (2025-01-18). [Observed S1; S2]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **ID:** Kaela Kovalskia with Raora ("SMITTEN," "Graondstone," "PizzaTimeSmith" with Kronii; in Raora's lore Kaela lives in her basement); Kureiji Ollie is Elizabeth's "kami-oshi" per public-profile wikis (collabs with HOLOSTARS members in varying lineups, including Code Red games; "High Tide" with Kronii at -All for One-), and Ollie did a chat-and-art collab with Raora (2024-09-06); Moona Hoshinova with Raora ("V3LVET"); Anya Melfissa visited Raora (2025-02-11); Vestia Zeta and Haachama in a Mario Party off-collab with Raora (2024-10-08); Ayunda Risu with Elizabeth ("LYRA," "ALiCE&u"); Vestia Zeta sang "Giri Giri" with Elizabeth at her 2025 3D showcase, which Elizabeth arranged and choreographed [ASR, Elizabeth file EB20]; Pavolia Reine and Airani Iofi with Gigi in the "Fanfic Club"; Kobo Kanaeru calls Elizabeth "Lilis" (secondary) and sang "HELP!!" with Elizabeth and Bae at Serendipity; Vestia Zeta also sang "Break It Down" with Cecilia and Shiori and "MAKE IT, BREAK IT" with Gigi and FUWAMOCO at Serendipity. [Observed S1; S2] [Official S6, S7]
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
- `bible/world/TakaMori.md › How It Works`: - **Recent milestones (archive, S1):** an off-collab "Reunion & Gaming!! #takamori" and a karaoke collab (2022-06); off-collabs in 2023 (a Rubik's cube stream, "TAKAMORI OFF-COLLAB" with Kobo, doing each other's nails on camera with IRyS); their duet "Fire N Ice" (2023-12-14; lyrics by Calli and TeddyLoid); Kiara's off-collab watch party "cheering Calli on!!!" for Calli's GriMoire concert (2025-02-27); a four-part Split Fiction co-op series in April–May 2025, titled by them "takamori split screen nostalgia," "Perfectly In Sync with @TakanashiKiara," "thumbnail teetee manifestation into gameplay teetee" and "Saving the World with @TakanashiKiara"; Myth's 5th anniversary collab (2025-09-13) and the announced 6th anniversary live (2026-09-19; not verified as held).

### from VTuber Persona and Lore
- `bible/world/VTuber-Persona-and-Lore.md › [SW] Description`: Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization, an archiver who broke out of a prison for forbidden things, a gem born from human emotion, twin demonic guard dogs, Justice's queen, gremlin, ancient automaton and big-cat artist sent to catch Advent) is a persona and a running joke, not a fact of the story world, and they know it.
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - **What is a persona:** the lore on their official profiles (a reaper's apprentice, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time). In the story it is a character each one plays on stream, the way a performer keeps a stage persona. [Official profiles; Adaptation]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They use it as a joke engine: age jokes (Gura's "9,000-something," Kronii jokingly "60"), immortality and rebirth gags (Kiara), "canonically" framed bits (Ame calling in "from 2021" during Calli's 2026 charity stream). [Observed character files; Ame's wiki page §2026, secondary]

### from hololive -Advent-
- `bible/world/hololive--Advent.md › [SW] Rules`: Myth and Promise are their seniors.
- `bible/world/hololive--Advent.md › How the Group Works`: - **Seniors:** Advent debuted after Myth, Project: HOPE and Council; the latter two were later organized as Promise. Kiara hosted all five on HOLOTALK (2023-08-12) within two weeks of their debut. [Observed S5 Kiara archive title]

### from hololive -Justice-
- `bible/world/hololive--Justice.md › [SW] Rules`: Myth, Promise and Advent are their seniors.

### from hololive -Myth-
- `bible/world/hololive--Myth.md › Members and Status`: - Watson Amelia: concluded general activities 2024-09-30; affiliate; guests at genmates' events (Kiara's concerts 2025 and 2026, Kronii's 2026 live, a 2026 "call from 2021" in Calli's charity stream). [Observed Ame file A23; Ame's wiki page §2025–§2026, secondary]
- `bible/world/hololive--Myth.md › How the Group Works`: - **Protectiveness:** Ina says anyone who makes Gura cry will "face the wrath of Ina," and extends the promise to all the English members (tears of joy excepted). [Observed S2 Gura §Gura's antics, secondary]

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: The recent past behind the present. 2023: Advent debuts (Nerissa, Shiori, Bijou, FUWAMOCO, July); DEV_IS opens with ReGLOSS; IRyS and the Council become -Promise- (October); EN holds its 1st concert. 2024: Justice debuts (June) as the "law enforcers" hunting Advent; the ENigmatic Recollection fantasy story starts (IRyS's guild "Cerulean Cup,"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: (June); EN's 4th concert "Serendipity" in Los Angeles (July), built on units such as Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS, Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2023-04 | holoMeet 2023 ambassadors include IRyS | IRyS represents EN |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2023-10-08/09 | "CouncilRyS" 3D showcase; **-Promise- formed** (IRyS joins the Council) | Kronii's and IRyS's group |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 | "ENigmatic Recollection" (ENReco) announced: EN members in the fantasy world Libestal, via a Minecraft series, animation and songs | Guilds: IRyS in "Cerulean Cup," Nerissa and Gura in "Scarlet Wand" |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-01-03 | Ceres Fauna graduates | Promise remembers her |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-04 | World Tour '25 "-Synchronize!-" announced, led by Momosuzu Nene, Kureiji Ollie, **Mori Calliope, IRyS and Nerissa Ravencroft**, with guests per city (Kronii and Bae in Sydney) | Three of the cast on one tour |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-04-27 (04-28 JST) | Nanashi Mumei graduates | Promise becomes three |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-07-05 | hololive night at Dodger Stadium, Los Angeles, the second hololive–Dodgers collaboration: Ina, IRyS and Bijou | a stadium sing-along |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-07-03/04 PDT | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) | The current partnerships |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-10-06 (upcoming) | IRyS's first solo concert "HOPE ||: Beyond the Stars" (Tokyo) | IRyS's next big stage |
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

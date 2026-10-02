# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: justice
Packet: projects/holoen/research/qa/packets/justice.md (owned material) and projects/holoen/research/qa/packets/justice-incoming.md (incoming claims); both are inline below
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
   "name": "Cecilia Immergreen",
   "file": "bible/characters/Cecilia-Immergreen.md",
   "other_names": [
    "Cecilia",
    "Ceci",
    "Cece",
    "Immerhater",
    "The Ancient Automaton"
   ],
   "groups": [
    "hololive -Justice-",
    "hololive English -Justice- (former branch name)",
    "Justice",
    "Autofister",
    "CCGG"
   ],
   "status": "Cecilia is an active hololive member. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2024-06-22",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Cecilia-Immergreen.md › Background"
   }
  },
  {
   "name": "Elizabeth Rose Bloodflame",
   "file": "bible/characters/Elizabeth-Rose-Bloodflame.md",
   "other_names": [
    "Elizabeth",
    "Liz",
    "ERB",
    "Lizzie",
    "Erby Berby",
    "Lady Bloodflame",
    "The Scarlet Queen"
   ],
   "groups": [
    "hololive -Justice-",
    "hololive English -Justice- (former branch name)",
    "Justice",
    "Bloodraven"
   ],
   "status": "Elizabeth is an active hololive member. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2024-06-21",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Elizabeth-Rose-Bloodflame.md › Background"
   }
  },
  {
   "name": "Gigi Murin",
   "file": "bible/characters/Gigi-Murin.md",
   "other_names": [
    "Gigi",
    "Gi Murin",
    "G Pain",
    "GeeGee",
    "Da Fister",
    "The Free-spirited Chaser"
   ],
   "groups": [
    "hololive -Justice-",
    "hololive English -Justice- (former branch name)",
    "Justice",
    "Autofister",
    "CCGG"
   ],
   "status": "Gigi is an active hololive member. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2024-06-21",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Gigi-Murin.md › Background"
   }
  },
  {
   "name": "Raora Panthera",
   "file": "bible/characters/Raora-Panthera.md",
   "other_names": [
    "Raora",
    "Rao",
    "Rara",
    "The Artist with the God Eyes"
   ],
   "groups": [
    "hololive -Justice-",
    "hololive English -Justice- (former branch name)",
    "Justice",
    "B.F.F"
   ],
   "status": "Raora is an active hololive member. She has no supernatural abilities; her lore is a performed persona.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": "2024-06-22",
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Raora-Panthera.md › Background"
   }
  }
 ],
 "world": [
  {
   "name": "Justice Pairs",
   "file": "bible/world/Justice-Pairs.md",
   "role": "Relationship",
   "other_names": [
    "CCGG",
    "Autofister",
    "Bloodraven",
    "B.F.F",
    "RPGG",
    "Raviolin",
    "FiddleFlame",
    "FlamePanther",
    "HoloEU",
    "TimeChaser",
    "Grem Reaper"
   ]
  },
  {
   "name": "hololive -Justice-",
   "file": "bible/world/hololive--Justice.md",
   "role": "Faction",
   "other_names": [
    "Justice",
    "holoJustice",
    "hololive English -Justice-"
   ]
  }
 ],
 "units": [
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

### projects/holoen/research/qa/packets/justice.md

# Audit packet: justice

Snapshot: git c06ffa3. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Elizabeth-Rose-Bloodflame.md` 4161dd43cc01; `bible/characters/Gigi-Murin.md` b738bbb71838; `bible/characters/Cecilia-Immergreen.md` 71a657c0b769; `bible/characters/Raora-Panthera.md` 284ef84ad0d9; `bible/world/hololive--Justice.md` df1164544e49; `bible/world/Justice-Pairs.md` 230ca850a0f3

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Elizabeth Rose Bloodflame — `bible/characters/Elizabeth-Rose-Bloodflame.md`
**[SW] Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, Bloodraven
**[SW] Other Names:** Elizabeth, Liz, ERB, Lizzie, Erby Berby, Lady Bloodflame, The Scarlet Queen
**[SW] Background:** Elizabeth is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Scarlet Queen" and organizer of Justice; secondary-reported lore adds that she is the Harbinger of Order, a human knight from Great Exardia (not actually royalty) whose sword is Thorn, who joined hololive to keep an eye on Advent and to become an idol. She debuted first of her generation on 2024-06-21 (PDT) in hololive English -Justice-, held her 3D showcase on 2025-08-01 (PDT), sang at the 2025 English concert ("ALiCE&u" with Nerissa and Ayunda Risu, a solo "Stellar Stellar," and the day-two opener "START AGAIN" with Calli, IRyS and Nerissa), invited guests from several branches to her 2026 birthday live, and at the 2026 Serendipity concert sang "HELP!!" with Kobo Kanaeru and Hakos Baelz and formed the unit Bloodraven with Nerissa Ravencroft ("Cruel Angel's Thesis"). Her representative color is red; her fans are the Rosarians of the Bloodflame Kingdom.
**[SW] Relationships:** Nerissa Ravencroft: her lore "mortal enemy" from Advent and her Serendipity 2026 unit partner in Bloodraven ("Cruel Angel's Thesis"); they covered "Rondo Revolution" and shared the 2025 stages "ALiCE&u" (with Ayunda Risu) and "START AGAIN" (with Calli and IRyS); Elizabeth says Nerissa "has a beautiful voice," Nerissa praises her kindness, and Nerissa calls her "my husband" as a performed bit. Vestia Zeta (ID): her duet partner for "Giri Giri" at her 2025 3D showcase, which Elizabeth arranged and choreographed. Gigi Murin: her Operation Tango partner (Gigi titled her stream "i won't let Liz down!!!"). Cecilia Immergreen: introduced her to Minecraft; Cecilia's lore joke says an older Justice made her a maid ("#LizIsInnocent"). Raora Panthera: an early duo partner ("Chat & Art w/ Liz!"), whom she calls "Pretty Kitty." Kobo Kanaeru and Hakos Baelz: "HELP!!" at Serendipity. Kureiji Ollie (ID): her kami-oshi and "Code Red" partner (PEAK with HOLOSTARS' Machina X Flayon and Jurard T Rexford; "High Tide" on stage with Kronii); Crimzon Ruze (HOLOSTARS) is her "Nephew" in a Marvel Rivals uncle–nephew bit. Banzoin Hakka (HOLOSTARS): a "Mephisto" duet she produced and arranged. Mori Calliope: the LYRA cover of "III" with Amane Kanata, Koganei Niko and Ayunda Risu. Shiori Novella: credited in Shiori's non-canon motion comic "Into The Void." Takanashi Kiara: calls her "Erby Berby." 2026 birthday-live guests: FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine and Korone.
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | The Scarlet Queen and Harbinger of Order from Great Exardia; joined hololive to keep an eye on Advent and to become an idol; human, and not royalty despite the title | [Official EB1] [Observed EB2 §Lore, secondary] |
| 2024-06-21 PDT | Debut ("Ello Ello Ello~!"), first of Justice; official profile lists June 22 (JST) | [Official EB1] [Observed EB3] |
| 2025-01-18 | "Mephisto" cover with HOLOSTARS' Banzoin Hakka | [Observed EB3] |
| 2025-08-01 PDT | 3D showcase (5 PM PDT); she arranged and directed most of it, including "Giri Giri" with Vestia Zeta | [Official EB7] [ASR EB20] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official EB7] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie | [Official EB5] |
| 2026-05 | 2026 birthday live with guests from several branches; the performances were released as cover videos ("Live from COVER Corp. Studio") | [Observed EB3, archived credits] |
| 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |
**Dossier · Hard Facts (continuity):**
- Debut 2024-06-21 PDT (June 22 JST); birthday April 25; 171 cm; color red; fans Rosarians; sword Thorn.
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger.

### Gigi Murin — `bible/characters/Gigi-Murin.md`
**[SW] Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, Autofister, CCGG
**[SW] Other Names:** Gigi, Gi Murin, G Pain, GeeGee, Da Fister, The Free-spirited Chaser
**[SW] Background:** Gigi is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Free-spirited Chaser," a mischievous gremlin "born and raised under the flag of Freedom" who chases targets on instinct and struggles with memorizing directions; secondary-reported lore places her in Freesia and frames the pursuit of Advent as another chance for fun. She debuted on 2024-06-21 (PDT) in hololive English -Justice-, won the 2024 Most Chaotic VTuber award, held her 3D showcase on 2025-08-02 (PDT), and sang at the 2025 English concert (solo "Wonky Monkey," "Countach" with Hakos Baelz and Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, "III" with Nerissa). She performs original songs: "I'll still be here" (presented on her 2025 birthday), "Bright Tonight" with IRyS, Kronii and FUWAMOCO (2025), and "enough" (2026). She and Cecilia Immergreen perform together as Autofister, also called CCGG: in 2026 they released "CCGG MADNESS" (Gigi helped with the lyrics and designed the chibi models) and sang it at the Serendipity concert, where Gigi also sang "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO. Her representative color is orange; her fans are grems; her fictional mascot is Popo, a kakapo.
**[SW] Relationships:** Cecilia Immergreen: her genmate and Autofister partner (also called CCGG): "CCGG MADNESS" (Gigi helped with the lyrics and designed the chibi models), Cuphead, Shadowverse and Serendipity; Cecilia calls her "idiot" (and "FREAK" in wiki transcriptions) yet says she "doesn't easily get rattled and is very dependable"; Gigi says Cecilia is "good at getting stuff done"; they met before debut. Raora Panthera: MapleStory, Monster Hunter and a food tier list; Raora designed both their Monster Hunter Wilds collaboration outfits. Elizabeth Rose Bloodflame: her Operation Tango partner (Gigi's stream title: "i won't let Liz down!!!"). Mori Calliope: Mouthwashing, Fast Food Simulator, R.E.P.O. and The Boba Teashop; the League of Legends campaign; with Fuwawa, "2 Creatures + 1 Reaper" (Fuwawa's post). Ouro Kronii: Fatal Fury and Hytale; "MONSTER" with Kronii, Ina and Shiori. IRyS, Kronii and FUWAMOCO: "Bright Tonight." Vestia Zeta (ID) and FUWAMOCO: "MAKE IT, BREAK IT" at Serendipity. Hakos Baelz and Kureiji Ollie (ID): "Countach" on stage. Takanashi Kiara: Reanimal ("ULTRA ORANGE WILL LIGHT THE WAY!!") and Eden Eternal with Shiori; Kiara calls her "GeeGee." Watson Amelia: knights in a fictional ENReco marriage storyline. Shiori Novella and Koseki Bijou: GAGA with Cecilia (Trine 5, Heave Ho, Phasmophobia); Shiori is also in the Fanfic Club with Gigi, Pavolia Reine and Airani Iofifteen, and cast her in the non-canon motion comic "Into The Void." Nerissa Ravencroft: "III" on stage; she helped with the "CCGG MADNESS" lyrics. FUWAMOCO: Gigi and Cecilia guest-hosted FUWAMOCO MORNING #167 as a prank. Ceres Fauna: Silent Hill 2 and The Coughing Baby Award Show. Nanashi Mumei: Echo Point Nova.
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | A gremlin "Chaser" from Freesia, "born and raised under the flag of Freedom" | [Official GG1] |
| 2024-06-21 PDT | Debut ("GG STANDS FOR GIGI!"), second of Justice; official profile lists June 22 (JST) | [Official GG1] [Observed GG3] |
| 2024-09-21 | Sings "September" 120 times in an eight-hour unarchived karaoke | [Observed GG2, secondary] |
| 2024-12-14 | VTuber Awards: Most Chaotic VTuber | [Observed GG6; secondary reporting] |
| 2025-08-02 PDT | 3D showcase (5 PM PDT; Aug 3 00:00 UTC) | [Official GG8] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official GG8] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa | [Official GG5] |
| 2025-10-18 | First original song "I'll still be here" presented (digital release 10-20) | [Official GG7] [Observed GG2] |
| 2025-12-22 | "Bright Tonight" with IRyS, Kronii and FUWAMOCO released | [Official GG7] |
| 2026-05 | CCGG 3D live with Cecilia; "CCGG MADNESS" MV (05-17; digital 05-29) | [Official GG1, GG7] [Observed GG3] |
| 2026-06-25 | Original MV "enough" | [Observed GG3] |
| 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice and "CCGG MADNESS" as Autofister with Cecilia (day 1); "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official GG4, GG9] |
**Dossier · Hard Facts (continuity):**
- Debut 2024-06-21 PDT (June 22 JST); birthday October 18; 153 cm; color orange; fans grems (lowercase);
  mascot Popo, a kakapo (fictional mascot); "Most Chaotic VTuber" 2024 (secondary reporting).
- 3D showcase 2025-08-02 PDT; Autofister with Cecilia (unit name in the official Serendipity report).
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger.

### Cecilia Immergreen — `bible/characters/Cecilia-Immergreen.md`
**[SW] Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, Autofister, CCGG
**[SW] Other Names:** Cecilia, Ceci, Cece, Immerhater, The Ancient Automaton
**[SW] Background:** Cecilia is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Ancient Automaton," a clockwork maid built long ago for eternal servitude who now does the bare minimum, cooks mostly potatoes and pours herself into crafty hobbies; secondary-reported lore places her origin in Immerheim, and in a public joke she blamed her maid duties on an earlier Justice. She debuted on 2024-06-22 (PDT) in hololive English -Justice- with a chat-controlled game and a violin performance, and held her 3D showcase on 2025-08-08 (PDT). Her first original song, "Wind-Up," which she composed and wrote, was the first Justice solo at the 2025 English concert, where she also played violin in "SHALLYS" with Ina and FUWAMOCO and sang "I'm Your Treasure Box" with Bijou and Raora. She and Gigi Murin perform together as Autofister, also called CCGG: "CCGG MADNESS" (2026; Cecilia wrote the lyrics and directed it), a 2026 3D live, and the Serendipity concert, where she also sang "Break It Down" with Vestia Zeta and Shiori Novella and "Cloudy Sheep" with Tsunomaki Watame and Mori Calliope. Her representative color is green; her fans are Otomos.
**[SW] Relationships:** Gigi Murin: her genmate and Autofister partner (also called CCGG): "CCGG MADNESS" (Cecilia wrote the lyrics; Gigi helped and designed the chibi models), a 2026 3D live, Cuphead, a Shadowverse match and Serendipity; she calls Gigi "idiot" and "FREAK" yet says Gigi "doesn't easily get rattled and is very dependable," and Gigi says she is "good at getting stuff done"; they met before debut. Raora Panthera ("Raviolin"): an early Minecraft partner; Raora illustrated Cecilia's debut ending screen and sweeping scene, Cecilia animated Raora's ending screen and mascot stinger, and Raora helped design the Otomo. Elizabeth Rose Bloodflame ("FiddleFlame"): Cecilia showed her around Minecraft; her "#LizIsInnocent" joke clears Liz of the old maid-service story (fans still draw Cecilia as Liz's maid). Takanashi Kiara: a German-speaking senior ("EterniTea"; "HoloEU" with Raora). Ninomae Ina'nis: a joking rival; Stranger of Paradise, and "SHALLYS" with FUWAMOCO on stage. Koseki Bijou and Shiori Novella: GAGA with Gigi (Trine 5, Heave Ho, Phasmophobia); Walking Dead watchalongs and Elden Ring with Bijou; "I'm Your Treasure Box" with Bijou and Raora. Vestia Zeta (ID) and Shiori: "Break It Down" at Serendipity. Tsunomaki Watame (JP) and Mori Calliope: "Cloudy Sheep" at Serendipity. Mococo Abyssgard ("Cecemoco"): Chrono Trigger. FUWAMOCO: Cecilia and Gigi guest-hosted FUWAMOCO MORNING #167. Gawr Gura: Keep Talking and Nobody Explodes, The Forest. IRyS and Bijou: Elden Ring Nightreign. Nanashi Mumei ("Automatowl"): Halo co-op. Ouro Kronii: Kronii has called her "CLANKER"; she calls Kronii "Owo-senpai"; "Clockwork Orange" with Gigi. Ceres Fauna ("Green Women"): a shoujo-tropes ranking. Tokino Sora (JP): Minecraft and Super Mario 3D World.
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | An ancient automaton built for eternal servitude (official); secondary lore places her origin in Immerheim; in a public joke she attributed her maid duties to an earlier Justice | [Official CI1] [X post CI6, secondary] |
| 2024-06-22 PDT | Debut ("It's wind-up time!!"), with a chat-controlled game (implemented by nullrefrepro per the credits; Raora drew the ending screen and sweeping art) and a violin performance; official profile lists June 23 (JST) | [Official CI1] [Observed CI3] |
| 2025-08-08 PDT | 3D showcase (5 PM PDT; Aug 9 09:00 JST) | [Official CI7] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official CI7] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice; "Wind-Up," the first Justice solo; "SHALLYS" with Ina and FUWAMOCO (on violin); "I'm Your Treasure Box" with Bijou and Raora | [Official CI5] |
| 2026-05 | CCGG 3D live with Gigi (after-talk 05-20, secondary archive evidence); "CCGG MADNESS" MV (05-17; digital 05-29) | [Official CI1] [Observed CI3 1rIXU_4xGvY, bTxEGwMOQQI] |
| 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice, "CCGG MADNESS" as Autofister with Gigi, "Break It Down" with Vestia Zeta and Shiori, "Cloudy Sheep" with Tsunomaki Watame and Calli (day 1); "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official CI4, CI8] |
**Dossier · Hard Facts (continuity):**
- Debut 2024-06-22 PDT (June 23 JST); birthday November 11; 162 cm; color green; fans Otomos; plays violin.
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger; Autofister/CCGG with Gigi
  (the "ccgg" name appears in 2025 titles; Autofister in the 2026 official report).
- 3D showcase 2025-08-08 PDT.

### Raora Panthera — `bible/characters/Raora-Panthera.md`
**[SW] Groups:** hololive -Justice-, hololive English -Justice- (former branch name), Justice, B.F.F
**[SW] Other Names:** Raora, Rao, Rara, The Artist with the God Eyes
**[SW] Background:** Raora is an active hololive member. She has no supernatural abilities; her lore is a performed persona. She is a VTuber whose lore makes her "The Artist with the God Eyes," a big cat whose all-seeing eyes make her suspect sketches uncannily accurate; in secondary-recorded lore she comes from the Romance Empire, abandoned a FUWAMOCO pursuit for crane games and left reporting duties for idol work. She debuted on 2024-06-22 (PDT) in hololive English -Justice-, won Best Art VTuber at the 2024 VTuber Awards, and held her 3D showcase on 2025-08-09 (PDT); later that month, at the 2025 English concert, she sang her original "Gacha×Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and Oozora Subaru, and "I'm Your Treasure Box" with Bijou and Cecilia. She held her first birthday 3D live in May 2026, and at the 2026 Serendipity concert she formed the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari") and sang "What an amazing swing" with Tsunomaki Watame and Takanashi Kiara. Her representative color is pink; her fans are the Chattini.
**[SW] Relationships:** FUWAMOCO (Fuwawa and Mococo): her Serendipity 2026 unit partners in B.F.F ("Inu Neko. Seishun Massakari"); before debut she drew them a shikishi portrait and gave it "with big tears in her eyes," and they call her their "precious cat kouhai." Gigi Murin ("RPGG"): MapleStory, Monster Hunter Wilds and a food tier list; Raora designed both their Monster Hunter Wilds collaboration outfits. Cecilia Immergreen ("Raviolin"): an early Minecraft partner; Raora illustrated Cecilia's debut ending screen and sweeping scene, Cecilia animated Raora's ending screen and mascot stinger, and Raora helped design the Otomo. Elizabeth Rose Bloodflame: joined her early "Chat & Art" collab and calls her "Pretty Kitty." Kaela Kovalskia ("SMITTEN"): co-op partner; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement; with Koseki Bijou they are "Graondstone." Koseki Bijou: her "assistant" in a cooking off-collab (the stream title's word); "I'm Your Treasure Box" with Bijou and Cecilia. Ouro Kronii ("Pizza Time"): Portal 2 and Backrooms Cleanup Crew; in ENReco Raora called Kronii's character "Tam Tender." Takanashi Kiara: "HoloEU" with Cecilia; an Italian lesson, a proposed Kiara outfit on her "Raora's Clawset" art stream, the "Doom" in Kiara's Mage Arena collab, and "What an amazing swing" with Tsunomaki Watame at Serendipity. Ninomae Ina'nis, Shiori Novella and Oozora Subaru (JP): "Neko Kaburi-Na" on stage; Puyo Puyo Tetris 2 with Ina. Nerissa Ravencroft and Moona Hoshinova ("V3LVET"): Raft and Monster Hunter Wilds; Clubhouse Games with Nerissa. Mori Calliope and Gigi: Elden Ring Nightreign. Akai Haato (JP): Clubhouse Games; with Vestia Zeta (ID), a Super Mario Party off-collab.
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | A big cat from the Romance Empire who prepares Justice's criminal reports; sent after FUWAMOCO, she got distracted by crane games | [Official RP1] [Observed RP2 §Lore] |
| 2024-06-22 PDT | Debut ("I've got my eyes on you 🐱 mamma mia"), last of Justice; official profile lists June 23 (JST) | [Official RP1] [Observed RP3] |
| 2024-12-14 | VTuber Awards: Best Art VTuber | [Observed RP6; secondary report] |
| 2025-08-09 PDT | 3D showcase (5 PM PDT; Aug 10 09:00 JST) | [Official RP8] |
| 2025-08-16 PDT | Justice 3D collaboration stream | [Official RP8] |
| 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, solo "Gacha x Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and guest Oozora Subaru, "I'm Your Treasure Box" with Bijou and Cecilia | [Official RP5] |
| 2025-11-16 | The "Doom" spell in Kiara's Mage Arena collab | [Observed RP7] |
| 2026-05-10 | First birthday 3D live concert (secondary archive evidence, w37yVSXhV_c) | [Observed RP3] |
| 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official RP4, RP9] |
**Dossier · Hard Facts (continuity):**
- Debut 2024-06-22 PDT (June 23 JST); birthday May 11; 155 cm; color pink; fans Chattini (Chattino, Chattina);
  "Best Art VTuber" 2024 (secondary report).
- 3D showcase 2025-08-09 PDT. Official music list: "Gacha×Gacha ADVENTURE!" and "Draw" (Draw's premiere
  and release dates not yet established). Serendipity unit: B.F.F with FUWAMOCO.
- Unit: hololive -Justice- (2024–), "hololive -Justice-" since the 2026-09 merger.

### hololive -Justice- — `bible/world/hololive--Justice.md`
**[SW] Other Names:** Justice, holoJustice, hololive English -Justice-
**[SW] Description:** hololive English's fourth generation (debuted June 2024), now "hololive -Justice-": Elizabeth Rose Bloodflame, the "Scarlet Queen" with a British accent, who organizes the group and sings; Gigi Murin, a loud, chaotic gremlin "Chaser"; Cecilia Immergreen, a sarcastic ancient automaton maid who hates working and plays violin; and Raora Panthera, a cheerful big-cat artist with an Italian accent who loves pizza. In their shared lore they are law enforcers sent to catch Advent's escaped "criminals," working from a headquarters in the clouds, The Lookout, whose Panscope telescope can observe distant places; the pursuit supplies staged rivalries and Advent × Justice collab jokes rather than arrests. Their first group stream was titled "Ello! Hi! Hallo! Ciao!", and "Justice! Just like that!" recurs in their stream titles. Elizabeth coordinates the group; Gigi and Cecilia trade comic provocations, with the teasing running both ways, and Raora often joins in laughing. Milestones: the songs "ABOVE BELOW" (2024) and "SUPERNOVA SUPER GIRL" (2026); individual 3D showcases on August 1, 2, 8 and 9, 2025 (PDT) and a group 3D stream on August 16; their first in-person concert performance in 3D at the 2025 English concert; at the 2026 Serendipity concert the units Autofister (Gigi and Cecilia), Bloodraven (Elizabeth and Nerissa) and B.F.F (Raora and FUWAMOCO), with Elizabeth also singing alongside Kobo Kanaeru and Hakos Baelz, Cecilia alongside Vestia Zeta and Shiori and alongside Tsunomaki Watame and Calli, Gigi with Zeta and FUWAMOCO, and Raora with Watame and Kiara; and the second-anniversary live "How to Protect JUSTICE!" (2026). Fans: Rosarians, grems, Otomos, Chattini.
**[SW] Rules:** At the 2026-09-30 baseline, all four remain members of Justice; the group is "hololive -Justice-" since the 2026 merger. The manhunt is lore they play for laughs, never real policing; Advent and Justice are friends and frequent collaborators. Each member speaks English with her own accent (British, American, German, Italian; the character cards teach each voice). Myth, Promise and Advent are their seniors.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2024-06-18 | Announcement video "The Mission Begins!" | the manhunt premise |
| 2024-06-21/22 PDT | Debuts: Elizabeth (06-21 8 PM), Gigi (06-21 8:45 PM), Cecilia (06-22 8 PM), Raora (06-22 8:45 PM); official profiles list June 22/23 (JST) | "ABOVE BELOW" released; first collab "Ello! Hi! Hallo! Ciao!" (06-22 9:30 PM PDT) |
| 2024-06–07 | Content Warning, Chained Together, Left 4 Dead 2, a Justice Minecraft server and "Justice HQ" | the group's first weeks |
| 2024-07-21/22 | "Advent VS Justice" in Party Animals | the rivalry as a game |
| 2024-10-31/11-01 | "Justice's Haunted VR Investigation" in VRChat, with Advent visitors; chibi 3D models | Halloween tradition |
| 2024-12-28 | Half-year anniversary (New Year outfits announced, shown 2025-01-01) | — |
| 2025-01-31 | "ADVENT VS JUSTICE" Murky Divers with all nine | — |
| 2025-03-08 | Justice hosted a watchalong of hololive 6th fes. (Expo 2025) Stage 1 ("FIRST STAGE with JUSTICE!") | [Observed S4 nEV7T8peRcw] |
| 2025-06-20 | First anniversary, "Operation DECODE" | — |
| 2025-08-01/02/08/09 PDT | Individual 3D showcases, each at 5 PM PDT: Elizabeth (08-01), Gigi (08-02), Cecilia (08-08), Raora (08-09) | [Official S7] |
| 2025-08-16 PDT | Justice group 3D collaboration stream (5 PM PDT) | [Official S7] |
| 2025-08-23 EDT | -All for One-: Justice's first group performance at an in-person concert venue in 3D ("ABOVE BELOW"); Cecilia's "Wind-Up" was the first Justice solo number of that concert; see the member files for their other stages | [Official S3] |
| 2026-02-20/22 JST | GeoGuessr: Elizabeth, Gigi and Cecilia trained (02-20) and represented Justice against Advent (02-22), with Bijou hosting/commentating | [Observed, secondary event roster] |
| 2026-05 | CCGG (Gigi and Cecilia) joint 3D live (secondary event coverage) and "CCGG MADNESS"; Raora's first birthday 3D live (05-10 JST / 05-09 PDT; secondary metadata) | — |
| 2026-06-27 PDT | Second-anniversary live "How to Protect JUSTICE!" (06-28 JST) | [Official S1 video list] |
| 2026-07-03/04 PDT | Serendipity: day 1 "SUPERNOVA SUPER GIRL" (Justice); Autofister (Gigi & Cecilia, "CCGG MADNESS"); "HELP!!" (Kobo Kanaeru with Bae and Elizabeth); "Break It Down" (Vestia Zeta with Shiori and Cecilia); "Cloudy Sheep" (Tsunomaki Watame with Calli and Cecilia). Day 2: the Advent+Justice medley ("Rebellion," "ABOVE BELOW"); Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"); "MAKE IT, BREAK IT" (Zeta, FUWAMOCO and Gigi); "What an amazing swing" (Watame with Kiara and Raora); B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari") | [Official S6, S8] |
| 2026-08/09 | Official -Justice- merch tie-ins: Bandai Namco Amusement America pop-up (2026-08-27), Pinfinity AR pins (2026-09-30) | [Official S1 news] |

Group songs: "ABOVE BELOW" (2024), its "-Far East Remix-," "RENEGADE," "SUPERNOVA SUPER GIRL" (2026; the
concert report spells it "SUPERGIRL"). The
"#AdVSJus Motion Comic" (Advent vs Justice) ran to at least five episodes. [Official S1 music and video lists]
**Dossier · Hard Facts (continuity):**
- Debuts 2024-06-21/22 PDT (June 22/23 JST); 3D showcases 2025-08-01/02/08/09 PDT; group 3D collab 2025-08-16
  PDT; members' colors: Elizabeth red, Gigi orange, Cecilia green, Raora pink. All four remain members at the
  baseline.
- Serendipity 2026 units (official billing): Autofister, Bloodraven, B.F.F.
- The manhunt is lore played as a bit; Justice and Advent are friends and frequent collaborators.

### Justice Pairs — `bible/world/Justice-Pairs.md`
**[SW] Other Names:** CCGG, Autofister, Bloodraven, B.F.F, RPGG, Raviolin, FiddleFlame, FlamePanther, HoloEU, TimeChaser, Grem Reaper
**[SW] Description:** Inside Justice: Gigi and Cecilia are an officially billed duo, Autofister (also CCGG), with the song "CCGG MADNESS," a joint 2026 3D live and a Serendipity unit; a secondary transcription has Cecilia's "Ew! Get away from me, you FREAK!", yet she says Gigi "doesn't easily get rattled and is very dependable," and Gigi says Cecilia is "good at getting stuff done." Gigi and Raora collaborate in Monster Hunter and food-ranking streams, and Raora designed Monster Hunter collaboration outfits for both of them. Gigi and Elizabeth cooperate in Operation Tango (Gigi's title: "i won't let Liz down!!!"). Cecilia and Raora play Minecraft together; Raora illustrated Cecilia's debut ending screen and Cecilia animated Raora's. Elizabeth and Raora held a chat-and-art collab in June 2024, and Elizabeth titled Raora's birthday stream "Happy Birthday Pretty Kitty!"; Cecilia showed Elizabeth around Minecraft, and a lore post blames Cecilia's old maid duties on an earlier Justice, not Elizabeth's. With Advent, their in-story "targets": Elizabeth is Nerissa's lore "mortal enemy" and her Bloodraven partner ("Cruel Angel's Thesis"); Gigi and Cecilia form GAGA with Shiori and Bijou; Raora and FUWAMOCO are the unit B.F.F; Graondstone names Raora, Bijou and Kaela Kovalskia. With seniors: Gigi repeatedly uses Calli's full name and jokes about getting her into League of Legends; within HoloEU, Raora teaches Kiara Italian and Cecilia speaks German with her; Cecilia plays up a rivalry with Ina; Kronii is Raora's "Pizza Time" collaborator and Gigi's Fatal Fury and Hytale partner, and secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai"; Automatowl names Cecilia and Mumei. Beyond EN: Elizabeth plays with Kureiji Ollie and HOLOSTARS members in varying lineups (Code Red games; Marvel Rivals with Crimzon Ruze, her "Nephew" in an uncle–nephew bit) and sang LYRA's "III" with FLOW GLOW's Koganei Niko; Kaela appears in Raora's fictional basement bit; Elizabeth records covers with JP members; Cecilia plays games with Tokino Sora; at Serendipity, Elizabeth sang with Kobo Kanaeru, Gigi and Cecilia with Vestia Zeta, and Cecilia and Raora with Tsunomaki Watame.
**[SW] Rules:** Collaboration and unit names identify public creative partnerships: Autofister, Bloodraven and B.F.F are official concert billing, Grem Reaper and Pizza Time appear in member stream titles, and the rest are secondary labels. Unit labels such as GAGA, Graondstone, Automatowl, HoloEU and Cecemoco name combinations of members, never one person. "Wife," "husband," fictional children, the maid backstory, the uncle–nephew bit and "mortal enemy" are performed jokes or lore and establish no private relationship. The manhunt between Justice and Advent is shared fiction. Name only the members who took part in a collab.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2024-06-26 | Raora's first collab, "Chat & Art w/ Liz!" | FlamePanther |
| 2024-07-03 | Cecilia and Raora's Minecraft duo | Raviolin |
| 2024-07-19 | Cecilia shows Elizabeth around Minecraft | FiddleFlame |
| 2024-07-21/22 | Advent VS Justice, Party Animals | the rivalry as a game |
| 2025-01-31 | Murky Divers, Advent × Justice (all nine) | — |
| 2025-08-16 PDT | Justice group 3D collab (after the individual showcases 08-01/02/08/09 PDT) | official schedule |
| 2025-08-23/24 EDT | -All for One-: "ALiCE&u," "START AGAIN," "High Tide" (Elizabeth); "Countach," "MONSTER," "III," "Wonky Monkey" (Gigi); "Wind-Up," "SHALLYS," "I'm Your Treasure Box" (Cecilia); "Gacha×Gacha ADVENTURE!," "Neko Kaburi-Na," "I'm Your Treasure Box" (Raora) | [Official S6] |
| 2026-05 | CCGG 3D live, "CCGG MADNESS" | Gigi and Cecilia's unit |
| 2026-07-03/04 PDT | Serendipity: units Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora); guests' songs with Justice members: "HELP!!" (Kobo, Bae, Elizabeth), "Break It Down" (Zeta, Shiori, Cecilia), "Cloudy Sheep" (Watame, Calli, Cecilia), "MAKE IT, BREAK IT" (Zeta, FUWAMOCO, Gigi), "What an amazing swing" (Watame, Kiara, Raora) | [Official S3, S7] |
**Dossier · Hard Facts (continuity):**
- Serendipity 2026 units with Justice members (official billing): Autofister (Gigi & Cecilia), Bloodraven
  (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora).
- "CCGG MADNESS" is Gigi and Cecilia's original song (2026); GAGA is a quartet; "2 Creatures + 1 Reaper" is a
  Fuwawa collab, not a FUWAMOCO one.

Incoming claims continue in `justice-incoming.md`.

### projects/holoen/research/qa/packets/justice-incoming.md

# Audit packet: justice (incoming claims)

Snapshot: git c06ffa3.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: e Artist with the God Eyes|hololive English -Justice-|Elizabeth Rose Bloodflame|The Free-spirited Chaser|The Ancient Automaton|Cecilia Immergreen|hololive -Justice-|The Scarlet Queen|Lady Bloodflame|Raora Panthera|Justice Pairs|FlamePanther|Grem Reaper|FiddleFlame|holoJustice|Gigi Murin|Bloodraven|Immerhater|TimeChaser|Erby Berby|Autofister|Da Fister|Elizabeth|Gi Murin|Raviolin|Justice|Cecilia|Lizzie|GeeGee|HoloEU|G Pain|Raora|B.F.F|Cece|Gigi|Ceci|Rara|LYRA|RPGG|CCGG|Liz)(

### from Ceres Fauna
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: Cecilia Immergreen: a book and shoujo-manga tropes ranking (2024; "Green Women").
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: Gigi Murin: Silent Hill 2 and the 2024 Coughing Baby Award Show ("FruitPunch," a secondary pair name).
- `bible/characters/Ceres-Fauna.md › Story Engine`: 4. Fauna referees Justice in a board game she invented, and the rules keep changing.

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Groups`: FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent, B.F.F
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Background`: Together they won "VTuber of the Year" at the 2024 VTuber Awards, reached one million subscribers first in Advent, made their 3D debut in August 2024, held a birthday concert in 2025, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Raora Panthera: their 2026 Serendipity unit partner in B.F.F, who drew them a shikishi before her debut.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026).
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA."
- `bible/characters/Fuwawa-Abyssgard.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Mococo and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) | [Official FW4; Serendipity report] |
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Gigi Murin, Mori Calliope | Kouhai and senior | "2 Creatures + 1 Reaper," a rare bomb-defusing collab (2026-09) | [Observed FUWAMOCO X post via wiki, FW6] |

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Cecilia Immergreen: Keep Talking and Nobody Explodes and The Forest (2025).
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Raora Panthera: R.E.P.O. with Kiara and Kronii (2025).

### from IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: Gigi Murin: a "Cerulean Cup" guildmate in the ENigmatic Recollection story.
- `bible/characters/IRyS.md › [SW] Relationships`: Cecilia Immergreen: Elden Ring Nightreign with Bijou (2025).
- `bible/characters/IRyS.md › [SW] Relationships`: Gigi Murin, Ouro Kronii and FUWAMOCO: "Bright Tonight"
- `bible/characters/IRyS.md › [SW] Relationships`: Elizabeth Rose Bloodflame: "START AGAIN" with Calli and Nerissa at the 2025 concert.

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Shiori Novella: Advent's "glorious leader" in Bijou's affectionate bit (Goth Rock; a "Gyatt Review"; GAGA with Gigi and Cecilia).
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: (Kaela calls her "Beejoe"): Raft, Minecraft, Split Fiction, and with Raora "Graondstone."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Ouro Kronii: Lethal Company and Yu-Gi-Oh. -Justice-: GAGA with Gigi and Cecilia; Graondstone with Raora; "I'm Your Treasure Box" with Cecilia and Raora at the 2025 concert; Cecilia's Walking Dead watchalongs and a 2025 Elden Ring stream Bijou joined partway; Raora's 2024 cooking off-collab, billed with Bijou as her assistant.
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-08-23/24 | -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora | [Official KB5] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Kaela Kovalskia (ID) | Friend ("Grindstone"; Kaela calls her "Beejoe") | Grindstone collabs include Raft and Minecraft (2023), Split Fiction (2025) and PEAK as "Graondstone" with Raora (archive counts 10 / 23 / 11 / 0) | [Observed KB2; KB3] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Cecilia Immergreen, Raora Panthera, Gigi Murin | Justice kouhai | GAGA (with Shiori and Gigi); Graondstone (with Kaela and Raora); a Walking Dead off-collab watchalong with Cecilia (2025) | [Observed KB2; KB3] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Groups`: FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent, B.F.F
- `bible/characters/Mococo-Abyssgard.md › [SW] Background`: Together they won "VTuber of the Year" at the 2024 VTuber Awards, made their 3D debut in August 2024, sang a TV anime ending theme in 2026, performed with Raora Panthera at the 2026 Serendipity concert, and announced their first album.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Gigi Murin ("GigiMoco,"
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: "bauBau") and Cecilia Immergreen ("Cecemoco"): Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Cecilia is also Mococo's Chrono Trigger partner, including 2026 off-collabs; Gigi sang "Bright Tonight" and "MAKE IT, BREAK IT" with the twins.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Raora Panthera: their 2026 Serendipity unit partner in B.F.F.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA."
- `bible/characters/Mococo-Abyssgard.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Fuwawa and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) | [Official MC4; Serendipity report] |
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Gigi Murin | Justice kouhai ("GigiMoco," "bauBau") | Collabs from 2024; Gigi and Cecilia hosted FUWAMOCO MORNING #167 in the twins' place as a prank (2025) | [Observed MC2, secondary; MC3] |
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Cecilia Immergreen | Justice kouhai ("Cecemoco") | The twins had hoped for a robot-girl member before Cecilia's debut; a Chrono Trigger off-collab (2026-04-25) | [Observed MC2; MC3 GmcYjV6aTuA] |
- `bible/characters/Mococo-Abyssgard.md › Relationship Map`: | Raora Panthera | Justice kouhai; Serendipity 2026 unit B.F.F | Raora drew the twins a shikishi portrait before her debut and gave it "with big tears in her eyes" | [Official MC4] |

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Gigi Murin ("Grem Reaper," a shared title): horror and job-simulator collabs; Calli came to like her own name once Gigi kept using it.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Elizabeth Rose Bloodflame, Koganei Niko, Ayunda Risu and Amane Kanata: fellow LYRA vocalists on a "III" remix cover.
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Gigi Murin | Frequent collaborator ("Grem Reaper," fan term) | Per the wiki, Calli only came to like how her own name sounds once Gigi started saying it. [Unverified, title only: Gigi ragebaiting and teasing her] | [Observed C4 §Relationships and §Name, secondary; C21-wug0DWFeDXM clip title] |

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Gigi Murin: Echo Point Nova as "A Towl and a Gremlin."
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Cecilia Immergreen: Halo co-op ("Automatowl").
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Raora Panthera: a joint drawing stream (2025).
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Gigi Murin | Justice kouhai | Echo Point Nova as "A Towl and a Gremlin" (2024-10-15, QA7OA1ew5HI) | [Observed M3] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Cecilia Immergreen | Justice kouhai ("Automatowl"; calls her "Myumyei") | Joined, with Gigi, Mumei's alphabet tier list (2025) | [Observed M2; M3] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Groups`: hololive -Advent-, Advent, hololive English (former branch name), Bloodraven
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Elizabeth Rose Bloodflame: her "mortal enemy" in their lore (a performed rivalry) from Justice and her 2026 Serendipity unit partner in Bloodraven ("Cruel Angel's Thesis"); they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai").
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Gigi Murin: duo partner with a joke "child,"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Cecilia Immergreen: Unravel Two (2024; "AutoTune," a secondary pair name).
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Raora Panthera: Clubhouse Games (2024); with Moona, Raft and Monster Hunter Wilds as "V3LVET"
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Gigi Murin | Collaborator ("BeatDown," "SoundChaser") | A joke "child," Nerigi, at Gigi's 3D live | [Observed N2 §Relationships] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Elizabeth Rose Bloodflame | Justice member ("BloodRaven"); her 2026 Serendipity duo partner | Her "mortal enemy (lore)"; their "Rondo Revolution" cover; World Tour '24 panels together; Nerissa praises her "kindness and encouraging attitude" ("She's always looking out for me, even though I'm the senpai"); building Liz's Mii: "she's the leader of justice after all" | [Official N21; S7 tour report via world card; ASR N20] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Moona Hoshinova | ID senior ("V3LVET" with Raora) | Featured on Moona's "100% (feat. Nerissa Ravencroft)" (2025-02-16); Keep Talking and Nobody Explodes together (2024) | [Official N23; N3 title] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Shiori Novella: a "Rate Your Fears" nightmare talk (2024) and "MONSTER" with Kronii and Gigi at the 2025 English concert.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: FUWAMOCO: "SHALLYS" with Cecilia at the same concert.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Cecilia Immergreen: Stranger of Paradise partner (2025), who plays up a rivalry with Ina.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Gigi Murin and Raora Panthera: Blood Typers with Gigi, Puyo Puyo Tetris 2 with Raora, and a sponsored Monster Hunter Wilds launch with both and Bijou (2025).

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Gigi Murin: Fatal Fury and Hytale ("TimeChaser"; "Clockwork Orange" with Cecilia), "MONSTER" on stage and "Bright Tonight"
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Cecilia Immergreen: Cecilia calls her "Owo-senpai," and Kronii has called Cecilia a "CLANKER."
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Raora Panthera: "Pizza Time" partner (Portal 2, 2024; Backrooms Cleanup Crew, 2026), who used "Tam Tender" for Kronii's ENReco character.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Shiori Novella: they hosted "Rating Your Clocks" together (2025), and they sang "MONSTER" with Ina and Gigi at the 2025 English concert.
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - "Sorry, I just don't understand things from a CLANKER." → to Cecilia Immergreen → specific interaction. [Observed K8 §Quotes, secondary]
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Gigi Murin | Collaborator ("TimeChaser", "Clockwork Orange" with Cecilia) | Unit names only are secondary-sourced. [Unverified, title only: Gigi imitating Kronii's greeting, flirtatious teasing both ways, Kronii's exaggerated disgust] | [Observed K8 §Relationships, secondary; K15, K26 clip titles] |
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Cecilia Immergreen | Collaborator | Cecilia calls her "Owo-senpai"; Kronii calls her a "CLANKER" | [Observed K8 nickname list and §Quotes, secondary] |
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Raora Panthera | Collaborator ("Pizza Time") | Raora calls her "Tam Tender". [Unverified, title only: Kronii ragebaiting Raora about pizza and pasta] | [Observed K8 nickname list, secondary; K30 clip titles] |
- `bible/characters/Ouro-Kronii.md › Story Engine`: 3. Gigi's flirting meets Kronii's wall of disgust; who breaks first?
- `bible/characters/Ouro-Kronii.md › Hard Facts`: - Aliases: Kronini, Kroniicopter, Kronster (by Calli), Tam Tender (by Raora), Owo-senpai (by Cecilia). Performed identities are excluded from matching unless a story uses them: Ouro Krono (-Ministry- persona, goodbye "Kronovoir") and Tam Gandr (ENreco). [Observed K8 nickname list, §Name and §Miscellaneous, secondary]

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Ouro Kronii: they hosted "Rating Your Clocks" together (2025) and sang "MONSTER" with Ina and Gigi at the 2025 concert.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Gigi Murin, Cecilia Immergreen, Elizabeth Rose Bloodflame (-Justice-, Advent's in-story "guards"): GAGA with Bijou, Gigi and Cecilia; Gigi, Elizabeth ("NovelFlame") and Nerissa voice her non-canon motion comic "Into The Void."
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Raora Panthera: a 2024 outfit-design collab and Blood Typers with Kronii and Bijou (2025).
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Cecilia and Vestia Zeta: "Break It Down" at Serendipity.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club."
- `bible/characters/Shiori-Novella.md › Behavioral Traits`: 3. She is a self-made producer: she records and edits her own vlogs, writes community posts "like some public diary," makes distinctive titles, thumbnails and overlays, and in 2026 released "Into The Void," a four-part original motion comic voiced by herself, Elizabeth, Gigi and Nerissa. [Official SN4] [Observed SN2; SN3 kEoFVaHsy_U, 3qrQ4KcvUb4]
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Gigi Murin, Cecilia Immergreen, Elizabeth Rose Bloodflame | Justice kouhai ("NovelGrem," "GAGA," "NovelFlame") | Lethal Company as GAGA (2024); Project Zomboid with Zeta and Gigi (2025); Elizabeth and Gigi in her "Into The Void" cast (2026) | [Observed SN2; SN3] |
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Airani Iofi (ID), Pavolia Reine (ID) | "Fanfic Club" with Gigi | Monster Hunter Wilds with Iofi and Jurard (2025) | [Observed SN2; SN3] |

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Raora Panthera and Cecilia Immergreen: "HoloEU"
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: (Italian lessons, German chats); Raora's friendly-fire "Doom" in Kiara's Mage Arena collab became a meme.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Gigi Murin: Reanimal ("Ultra Orange").
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: - "Doom? DOOM? What do you mean, Doom?" → Raora's "Doom" (2025-11-16), now a callback she reacts to with mock trauma. [Observed T2 §Quotes, secondary; T6; T5-jwGiJnsdQn0 clip title]
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2025-11-16 | Raora's "Doom" on her stream becomes a meme | [Observed T6] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Raora Panthera | Justice member | The "Doom" incident | [Observed T2 §Quotes; T6] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Cecilia Immergreen | Justice member | German-speaking duo; they slip into German together | [Observed T5-K7NNBucs3zc clip title; T2 §Relationships] |

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Gigi Murin: in the ENigmatic Recollection role-play story Gigi's knight Gonathon married Ame's Jyonathan ("ClueChaser," a secondary pair name).
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Cecilia Immergreen and Gigi: Borderlands 2 with Mumei (2024).
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Gigi Murin | Justice member | ENreco roleplay (Jyonathan) | [Observed A2 infobox and §Relationships, per Claude's research] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › [SW] Description`: With -Justice-, their in-story "guards": Gigi and Cecilia form the quartet GAGA with Bijou and Shiori, Raora sang with FUWAMOCO in 2026, and Elizabeth is Nerissa's "mortal enemy" in their lore and her duo partner.
- `bible/world/Advent-Pairs.md › [SW] Description`: Beyond EN: Bijou and Kaela Kovalskia's Grindstone collabs include Raft, Minecraft and Split Fiction; Vestia Zeta and Shiori are the official duo GreyScaleX ("Purrfect Pair" merchandise, 2026); Pavolia Reine and Airani Iofi join Shiori and Gigi in the "Fanfic Club"; FUWAMOCO's oshi are Houshou Marine and Omaru Polka.
- `bible/world/Advent-Pairs.md › [SW] Rules`: Advent's fugitives and Justice's guards belong to their shared fictional storyline.
- `bible/world/Advent-Pairs.md › With Myth`: - **Mori Calliope:** Bijou played her Undertale mod starring Calli with her on stream (2023-08-12); "TombStone" (Bijou), a 24-hour charity stream together (2025-06-29), Warhammer painting (2026); "FUWAMOCALLI," a collaboration name the twins say they particularly like; Fuwawa alone joined Calli and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"); Shiori was Calli's 2026 Serendipity partner (Calli, officially: "I am a little obsessed with her"; their dynamic: "Unhinged"). [Official S4] [Observed S1]
- `bible/world/Advent-Pairs.md › With Myth`: - **Ninomae Ina'nis:** "TakoRocky" with Bijou (Monster Hunter; Ina designed their 2025 Monster Hunter Wilds outfits); "Rate Your Fears" with Shiori (2024); "SHALLYS" with FUWAMOCO and Cecilia at the 2025 concert; with Bijou and IRyS, starred at hololive night at Dodger Stadium (2025-07-05). [Observed S1; X post via wiki] [Official S5, S8]
- `bible/world/Advent-Pairs.md › With Promise`: - **Ouro Kronii:** "WatchDog" with FUWAMOCO; Shiori and Kronii hosted "Rating Your Clocks" together (2025-03-27, AjwIazuu8gg; the description credits help with collecting submissions); "MONSTER" with Ina, Shiori and Gigi at the 2025 concert. [Observed S1] [Official S5]
- `bible/world/Advent-Pairs.md › With -Justice-`: - The Advent/Justice storyline makes Justice the law enforcers sent to catch the fugitives (shared fiction); joint Expos and merch use prisoner-and-guard jokes. [Observed hololive -Advent- card]
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Gigi Murin:** "GAGA," a quartet (Gem, Archiver, Gremlin, Automaton: with Bijou, Shiori and Cecilia), "NovelGrem" (Shiori), "GigiMoco" (Mococo); Gigi and Cecilia hijacked FUWAMOCO MORNING #167; Gigi voices a role in Shiori's "Into The Void" (2026). [Observed S2; S1]
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Cecilia Immergreen:** GAGA; "Cecemoco"; a Walking Dead off-collab with Bijou (2025) and a Chrono Trigger off-collab with Mococo (2026). [Observed S1]
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Raora Panthera:** "Graondstone" with Bijou and Kaela; FUWAMOCO's 2026 Serendipity unit partner (B.F.F), who drew them a shikishi before her debut. [Official S6] [Observed S1]
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Elizabeth Rose Bloodflame:** Nerissa's "mortal enemy" in their lore (a performed rivalry) and 2026 duo partner; "NovelFlame" and "BloodQuill" with Shiori; in the "Into The Void" cast. [Observed S1; Advent card]
- `bible/world/Advent-Pairs.md › Beyond EN`: - **ID:** Kaela Kovalskia and Bijou are "Grindstone" (Kaela calls her "Beejoe"); their collabs include Raft (2023), Minecraft and Split Fiction (2025) (archive count: 44 of Bijou's archived streams mention Kaela); Vestia Zeta and Shiori are "GreyScaleX" (the X is silent), an official duo unit whose "Purrfect Pair" merchandise opened for orders on 2026-09-05 [Official S7]; Kureiji Ollie and Bijou "GraveStone"; Pavolia Reine and Airani Iofi with Shiori and Gigi in the "Fanfic Club." [Observed S2; S1]
- `bible/world/Advent-Pairs.md › History`: | 2026-07-03/04 | Serendipity: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth | official interviews |
- `bible/world/Advent-Pairs.md › Conflicts and Story Hooks`: 4. Fuwawa, Calli and Gigi defuse a bomb, and nobody reads the manual.
- `bible/world/Advent-Pairs.md › Hard Facts`: - Serendipity 2026 pairs: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth (official).
- `bible/world/Advent-Pairs.md › Hard Facts`: - Shiori and Kronii hosted "Rating Your Clocks" together (March 2025). GAGA is a quartet; GreyScaleX is an official duo unit (Shiori, Zeta). "Fuwawa, Calli and Gigi" (2026) is a Fuwawa collab, not a FUWAMOCO one.

### from Concerts and Live Events
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: Los Angeles, July 3–4, built on units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia), with guests Ookami Mio, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame singing alongside EN members); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet.
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: (2026); Justice's first in-person concert performance in 3D at -All for One- (2025), CCGG's 3D live, Raora's first birthday live (2026) and Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive fes. + hololive SUPER EXPO** (spring, in Japan; the combined fes./EXPO tradition dates to 2022, while fes. itself is older): the agency-wide concert and convention. 3rd fes "Link Your Wish" (2022-03, Makuhari; Calli and Kiara performed on day 2, per their X posts), 4th fes "Our Bright Parade" (2023), 5th "Capture the Moment" (2024), 6th "Color Rise Harmony" (2025-03-08/09; Nerissa on day 1), 7th "Ridin' on Dreams" (2026-03-06/08). EN units share Expo booths and key visuals (Myth with Promise, Advent with Justice). [Observed S1 §2023–§2026; S2]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous" [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before and separate from "-Breaking Dimensions-"), Jakarta (11-09), Singapore (11-30, with a pre-concert panel of Kaela Kovalskia and Ouro Kronii), Atlanta (12-15, a panel of Nerissa and Elizabeth Rose Bloodflame), Kuala Lumpur (12-21, Nerissa and Elizabeth again) and Taipei (2025-01-18, the finale) [Official S7]; and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **holoMeet** (since 2022): overseas fan events with yearly ambassadors (Gura 2022, IRyS 2023, Bae 2024, Bijou 2025, Gigi 2026). [Observed S1]
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Nerissa Ravencroft | 6th fes day 1 (2025-03-08); 3D concert "Requiem for Love – A JukeBox Musical" (2025-05-24, with Calli and IRyS as guests); Advent's "On the Run!" (2025-08-29); World Tour '24 panels with Elizabeth (Atlanta, Kuala Lumpur); World Tour '25 lead; Serendipity with Elizabeth | Nerissa file N2, N3; S1 |

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Other Names`: Death Star, MoRikka, LYRA, Holodeath, PavoNashi, HOLOTORI, UMISEA, HoloJEI, TakoNeko, K.I.R.A, OKFAIR, Star Flower, IRySora, soranii, Apex Predators, KoMeHa, BLUE·MEGAMISAMA, V3LVET
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix cover as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa."
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kronii's recurring cross-branch partner is Kaela Kovalskia (years of survival and sim co-ops; a World Tour '24 panel), plus "soranii" with Tokino Sora and co-ops with Justice's Raora.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Of Justice: Kureiji Ollie is Elizabeth's kami-oshi, and Elizabeth plays with her and HOLOSTARS members in varying lineups (Code Red games; Marvel Rivals with Crimzon Ruze, her "Nephew" in an uncle–nephew bit); Elizabeth's 2026 birthday covers featured Subaru, Roboco, Sora, Choco, Marine, Korone, Polka, Nene, Watame and Iroha; Kaela Kovalskia appears in Raora's fictional basement bit ("SMITTEN"); Raora played Clubhouse Games with Haachama and Super Mario Party with Haachama and Zeta, and is "RaoRiRi" with Ririka; Cecilia plays games with Tokino Sora; at Serendipity, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame sang with Elizabeth, Gigi, Cecilia and Raora.
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Mori Calliope:** Hoshimachi Suisei is the senpai she is starstruck by ("Death Star"): she drew her ("DRAWING MY SENPAI," 2021), Suisei featured at Calli's first solo concert ("Wicked," 2022), they talked live shows together (2023), and Calli hosts watch parties of Suisei's concerts ("We're Screaming Loud for Senpai!", 2024-11). Kobo Kanaeru calls her "Uncle Dad" ("Father Daughter GOLF," 2022; an in-person cooking-and-gaming collab, 2023). Units: "Holodeath" (with Kureiji Ollie); "LYRA," a five-singer cover of "III" with Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth (Kanata has since graduated); "MoRikka" with HOLOSTARS' Rikka (their song "spiral tones," 2021; fans "DeadTuners") [Official music entry S5]. Outside hololive: friends with Milky Queen, whom she credits for introducing her to VTubers, and Ironmouse (a shared Underworld theme). [Observed S1 titles; S2 Calli §Relationships; Calli file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ouro Kronii:** Kaela Kovalskia is a recurring cross-branch collaborator (21 streams; survival and sim co-ops every few months: Raft 2023–24, Panicore, Luma Island 2024, Old Market Simulator 2025; together at a pre-concert panel in Singapore on World Tour '24 [Official S6]); also "soranii" with Tokino Sora, fan unit K.I.R.A (with IRyS, Reine, Anya), and Raora Panthera of Justice (Portal 2, Split Fiction, No Man's Sky 2026; "Pizza Time"). [Observed S1; S2 Kronii; Kronii file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Nerissa Ravencroft:** Houshou Marine is her oshi (an off-collab with Marine and FUWAMOCO, 2024); "BLUE·MEGAMISAMA" with Tokino Sora; "V3LVET" with Raora and Moona Hoshinova; Kobo calls her "Nori-chan." With Moona she has a released song, "100% (feat. Nerissa Ravencroft)" (2025-02-16) [Official S7]. [Observed S1; S2 Nerissa; Nerissa file]

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › [SW] Description`: Close to all of Advent (with Nerissa as the self-declared third sister, "Mofufu"), to Mori Calliope ("FUWAMOCALLI," a collaboration name the twins say they particularly like), to Raora Panthera (B.F.F, their 2026 concert unit), and to JP seniors including their oshi Houshou Marine (Fuwawa) and Omaru Polka (Mococo).
- `bible/world/FUWAMOCO.md › [SW] Rules`: A collab one twin joins alone (such as Fuwawa's 2026 trio with Calli and Gigi) is not a FUWAMOCO appearance.
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Myth and Promise:** "FUWAMOCALLI" with Mori Calliope (a twin game show and Smash in 2023, a tea party, an off-collab karaoke in 2024); Fuwawa also joined Mori Calliope and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"; Fuwawa's post, not a twin appearance); "Detective Dogs" with Watson Amelia (Escape Simulator, 2024-09-24); "WatchDog" with Ouro Kronii; "Fuwamoomco" with Nanashi Mumei (Overwatch, 2025-03-01); they helped Ceres Fauna on her last World Tree stream (2024-12-31); Kiara hosted them on HOLOTALK (2023). [Observed S1; S3; Mumei, Calli, Kiara archives]
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Justice:** Raora Panthera, their Serendipity 2026 unit partner in B.F.F, drew them a shikishi before her debut and gave it "with big tears in her eyes"; Gigi ("GigiMoco") and Cecilia ("Cecemoco," a Chrono Trigger off-collab in 2026). [Official S4] [Observed S1; S3]
- `bible/world/FUWAMOCO.md › History`: | 2025-08-23/24 | -All for One-: "HOT DUCK!" with Bijou and Subaru; their version of "Howling"; "Lifetime Showtime"; "SHALLYS" with Ina and Cecilia | [Official S5] |
- `bible/world/FUWAMOCO.md › History`: | 2026-07-03/04 PDT | Serendipity: the unit B.F.F with Raora ("Inu Neko. Seishun Massakari") | [Official S4; Serendipity report] |

### from IRyS and Nerissa Pairs
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Ina** (15 / 7 / 3 / 4 / 6 / 0): an early duo ("Keep Talking and Nobody Explodes," 2021-07-31; "It Takes Two," three parts, "It Takes Tako & Hope," 2021); a Gundam watchalong (2023-03-25); IRyS as guest on Ina's "AmiAmi March Special" (2025-03-18); Elden Ring Nightreign, which IRyS titled "Third Wheeling" (2025-06-24); guildmates ("Cerulean Cup," with Kronii, Bijou and Gigi) in the ENigmatic Recollection Minecraft story. [Observed S1 titles; S2 §Units, secondary]
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Kiara** (13 / 1 / 3 / 2 / 3 / 0): Kiara's "1ST FULL HOLOEN COLLAB ft. IRYS!" (2021-08-12); a "GERMAN CRASH COURSE … with IRYS" (2022-06-02); an off-collab doing each other's nails on camera (2023-11-14); TORIDAMA 2 off-collab with Kronii and Raora, "Who is the BRAVEST?" (2024-08-01). [Observed S1 titles]

### from VTuber Persona and Lore
- `bible/world/VTuber-Persona-and-Lore.md › [SW] Description`: Their lore (a reaper, an immortal phoenix, a priestess of the Ancient Ones, a shark from Atlantis, a time-traveling detective, the Warden of Time, a half-angel half-demon nephilim, the Demon of Sound, a druidic kirin, a forgetful owl who guards civilization, an archiver who broke out of a prison for forbidden things, a gem born from human emotion, twin demonic guard dogs, Justice's queen, gremlin, ancient automaton and big-cat artist sent to catch Advent) is a persona and a running joke, not a fact of the story world, and they know it.

### from hololive -Advent-
- `bible/world/hololive--Advent.md › [SW] Description`: (2026), and 2026 Serendipity pairs Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth and FUWAMOCO–Raora.
- `bible/world/hololive--Advent.md › How the Group Works`: - **The premise as a bit:** each member was sealed in The Cell for being "untouchable"; Nerissa, the "Demon of Sound," in the story "stole" the master key on the way out; her avatar wears it on a keychain. The next generation, -Justice-, are law enforcers sent to catch the five fugitives, so Advent × Justice collabs can use prisoner-and-guard jokes (a 2026 merch reveal: "Like prisoner and my prison guard"). [Official S3; Observed S1, S2 §Lore, secondary; ASR Nerissa file N20, multi-speaker, not attributed] Nerissa calls Justice's Elizabeth Rose Bloodflame her "mortal enemy (lore)"; the two covered "Rondo Revolution" together and were a duo at the 2026 Serendipity concert, where Nerissa praised Elizabeth's "kindness and encouraging attitude" ("She's always looking out for me, even though I'm the senpai"). [Official S7]
- `bible/world/hololive--Advent.md › History`: | 2026-07-03/04 | Serendipity pairs: Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth, FUWAMOCO–Raora | [Official S7, S10] |

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: The recent past behind the present. 2023: Advent debuts (Nerissa, Shiori, Bijou, FUWAMOCO, July); DEV_IS opens with ReGLOSS; IRyS and the Council become -Promise- (October); EN holds its 1st concert. 2024: Justice debuts (June) as the "law enforcers" hunting Advent; the ENigmatic Recollection fantasy story starts (IRyS's guild "Cerulean Cup,"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: (June); EN's 4th concert "Serendipity" in Los Angeles (July), built on units such as Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS, Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-06-21/22 PDT | **-Justice- debuts**: Elizabeth Rose Bloodflame, Gigi Murin, Cecilia Immergreen, Raora Panthera ("law enforcers" chasing Advent) | EN's newest kouhai |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-08-01/02/08/09 PDT | Justice 3D showcases, each at 5 PM PDT: Elizabeth (08-01), Gigi (08-02), Cecilia (08-08), Raora (08-09) | official schedule |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-08-16 PDT | Justice group 3D collaboration stream | before their first in-person concert stage |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-08-23/24 EDT | EN 3rd concert "-All for One-" (Radio City Music Hall, New York): day 1 opens with the all-member "All for One," followed by Advent's "Genesis"; Justice's first group performance at an in-person concert venue in 3D | all fifteen EN members on one stage |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-11 | Raora's friendly-fire "Doom" spell in Kiara's Mage Arena collab becomes a widely shared fan meme (KYM dates the stream 11-16) | a callback |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-05 | Gigi and Cecilia's joint CCGG 3D live and "CCGG MADNESS"; Raora's first birthday 3D live (05-10 JST / 05-09 PDT) | — |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-06-27 PDT | Justice's second-anniversary live "How to Protect JUSTICE!" (06-28 JST) | — |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-07-03/04 PDT | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) | The current partnerships |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-07/08 | Shiori's original motion comic "Into The Void" (with Elizabeth, Gigi, Nerissa); Advent's 3rd-anniversary 3D live "Bound by Fate"; FUWAMOCO announce their first album (08-29) | — |

# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: myth3
Packet: projects/holoen/research/qa/packets/myth3.md (owned material) and projects/holoen/research/qa/packets/myth3-incoming.md (incoming claims); both are inline below
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
   "name": "Takanashi Kiara",
   "file": "bible/characters/Takanashi-Kiara.md",
   "other_names": [
    "Kiara",
    "Kiwawa",
    "Wawa",
    "Tenchou",
    "Kusotori",
    "小鳥遊キアラ"
   ],
   "groups": [
    "hololive",
    "hololive -Myth-",
    "Myth",
    "hololive English (former branch name)",
    "Rocku Wawa"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. Kiara is a VTuber whose lore, a persona she plays for laughs, makes her a phoenix, not a chicken, and an idol whose dream is to own a fast-food chain; a phoenix can always be reborn.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": null,
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Takanashi-Kiara.md › Background"
   }
  }
 ],
 "world": [
  {
   "name": "Myth and Kronii: Other Pairs",
   "file": "bible/world/Myth-and-Kronii-Other-Pairs.md",
   "role": "Relationship",
   "other_names": [
    "Kiara and Ame",
    "Ame and Kiara",
    "Kiara and Gura",
    "Gura and Kiara",
    "Calli and Ina",
    "Ina and Calli",
    "Calli and Ame",
    "Ame and Calli",
    "Ina and Ame",
    "Ame and Ina",
    "Ina and Gura",
    "Gura and Ina",
    "Kiara and Kronii",
    "Kronii and Kiara",
    "Gura and Kronii",
    "Kronii and Gura"
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
   "unit": "Rocku Wawa",
   "members": [
    "Takanashi Kiara",
    "Koseki Bijou"
   ],
   "evidence": "official Serendipity billing, 2026"
  }
 ]
}
```

### projects/holoen/research/qa/packets/myth3.md

# Audit packet: myth3

Snapshot: git c06ffa3. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Takanashi-Kiara.md` 1d87f23af867; `bible/world/Myth-and-Kronii-Other-Pairs.md` 12e7d39a7dbb

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Takanashi Kiara — `bible/characters/Takanashi-Kiara.md`
**[SW] Groups:** hololive, hololive -Myth-, Myth, hololive English (former branch name), Rocku Wawa
**[SW] Other Names:** Kiara, Kiwawa, Wawa, Tenchou, Kusotori, 小鳥遊キアラ
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. Kiara is a VTuber whose lore, a persona she plays for laughs, makes her a phoenix, not a chicken, and an idol whose dream is to own a fast-food chain; a phoenix can always be reborn. In the bit she is the CEO of KFP (Kiara Fried Phoenix), whose employees are chickens; misbehaving staff get sent to the Usual Room, and she insists KFP is not a cult. She debuted with hololive -Myth- in September 2020 speaking English, Japanese and German. In December 2020 her channel was briefly terminated and she came back with a "#PhoenixDown" re-debut. She hosted the interview show HOLOTALK, translating for Japanese guests, and from 2026 co-hosts the bilingual HoloEN REWIND. She released her second album Vogelfrei in 2026 and held the duo concert Drawn to Dawn with Ninomae Ina'nis in Los Angeles. Her mascot is the little bird Kotori.
**[SW] Relationships:** Mori Calliope: her TakaMori partner. Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple. Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself." They sang "Fire N Ice," and they play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident. Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts. Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. Koseki Bijou: junior she encourages and her partner for the 2026 Serendipity concert ("Rocku Wawa," "Tententengoku Jigokukoku"); they share the "6 7" meme. Shiori Novella: an occult handcam off-collab ("#shiotori," 2024). Pavolia Reine: a recurring Indonesian collaborator ("PavoNashi"; a VR "vacation"; the bird unit HOLOTORI). Kobo Kanaeru: calls her "Mommy Kiwawa." Raora Panthera and Cecilia Immergreen: "HoloEU" (Italian lessons, German chats); Raora's friendly-fire "Doom" in Kiara's Mage Arena collab became a meme. Gigi Murin: Reanimal ("Ultra Orange"). Ouro Kronii ("quasoni"): Kiara was a fan before Kronii debuted. Nerissa Ravencroft: an Advent kouhai who calls Kiara her oshi and, in her lore, once worked at KFP (KiaRissa); Kiara showed her around Minecraft, and they held a 2025 "BIRB GIRLS" GIRLSTALK. IRyS: friend since the 2021 full-EN collabs; Kiara gave her a German crash course. Usada Pekora: her oshi and favorite senior. Nanashi Mumei (graduated 2025): a fellow bird of HOLOTORI whom she calls "Moomsies"; they sang a DECO*27 song together at the 2023 fes. and "Beyond the way" with Nerissa at the 2024 English concert. Ceres Fauna (graduated 2025): "KIWAWA vs FAWNA," and HOLOTALK's 32nd guest a week before she left.
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | Phoenix idol who dreams of owning a fast-food chain; reborn from her ashes | [Official T1] |
| Lore | CEO of KFP (Kiara Fried Phoenix); employees are chickens; the Usual Room; she denies KFP is a cult | [Observed T2 §KFP, secondary] |
| 2020-09-12 | Debuts in hololive English -Myth-, speaking English, Japanese and German | [Official T1] [Observed T2 §Debut] |
| 2020-11 | HOLOTALK begins as a bilingual interview show | [Official T9] [Observed T21] |
| 2020-12-10 | Channel briefly terminated, then restored; "#PhoenixDown" re-debut with a mock-amnesia bit ("Who's Calli?") | [Observed T2 §2020 and §Takamori; T5-le72UNZAbQI] |
| 2021-03 | German lesson with Gura; the German "HoloDE Debüt" stream | [Observed T15; T2 §2021] |
| 2021-09 | She and Calli announce they will tone down the TakaMori ship | [Observed T2 §Takamori] |
| 2025-11-16 | Raora's "Doom" on her stream becomes a meme | [Observed T6] |
| 2026-02-08 | 2nd album *Vogelfrei* | [Observed T2 §2026; T8] |
| 2026-03 | Bilingual show HoloEN REWIND begins | [Observed T2 §HoloEN REWIND] |
| 2026-03-27/28 | "Drawn to Dawn" duo concert with Ina (The Wiltern, Los Angeles) | [Official T11, T12] |
| 2026-06 | Serendipity interview and partnership with Koseki Bijou | [Official T10] |
| 2026-09-07 | Branches merge; unit is hololive -Myth- | [Official T20, T1] |
**Dossier · Hard Facts (continuity):**
- Birthday July 6; height 165 cm; debut 2020-09-12; unit hololive -Myth-; illustrator huke. [Official T1]
- Fans: KFP ("employees"); hashtags #kfp #キアライブ (streams). [Official T1]
- Nicknames: Kiwawa, Wawa, Tenchou (by fans), Kusotori (by Calli), Kibaba (grandma persona). Frogiwawa is
  officially a different character. [Observed T2 infobox, §Lore, §KFP, secondary]
- She doesn't drink. [Observed T2 §Likes and dislikes]
- Preferences on the card: fast food, hats, dislike of scary stuff, Pekora as her favorite senior
  [Observed T2 §Likes and dislikes]; hates sand ("I HATE SAND!…") [Observed T2 §Quotes]; hates the font
  Comic Sans [Observed T2 §Miscellaneous]. All secondary.

### Myth and Kronii: Other Pairs — `bible/world/Myth-and-Kronii-Other-Pairs.md`
**[SW] Other Names:** Kiara and Ame, Ame and Kiara, Kiara and Gura, Gura and Kiara, Calli and Ina, Ina and Calli, Calli and Ame, Ame and Calli, Ina and Ame, Ame and Ina, Ina and Gura, Gura and Ina, Kiara and Kronii, Kronii and Kiara, Gura and Kronii, Kronii and Gura
**[SW] Description:** The rest of the web among the five Myth members and Kronii. Kiara and Ame: Ame is Kiara's EN oshi ("#1 Ame gosling"); Ame made Kiara's HOLOTALK intro, was its guest in 2024 and now guests at Kiara's concerts; Ame on a reunion: "Kiara like, threw herself at me… she hugged me!" Kiara and Gura: Kiara calls Gura "Goobidiba" and taught her German and Japanese, swears included; Gura's Minecraft prank filled Kiara's KFP back room with chickens; Gura was HOLOTALK's 34th guest the day before she graduated. Calli and Ina: Ina designed Death Sensei and drew Calli's debut EP cover; Calli wrote the lyrics of Ina's "TAKO∞TAKOVER"; Calli is a recurring target of Ina's puns ("Every freaking time, Ina."). Calli and Ame: early Clubhouse 51 duels; in 2026 Ame "called in from 2021" to Calli's charity stream. Ina and Ame: Ina designed Bubba; they did a "loser buys dinner" off-collab. Ina and Gura: the official ocean unit UMISEA (2021); Ina promised "the wrath of Ina" to anyone who makes Gura cry. Kiara and Kronii: Kiara was a fan before Kronii debuted and calls her "quasoni." Gura and Kronii: fan unit SNOTCast; in Gura's last months Kronii was one of her regular partners ("I Play, She Watches (She's Scared)").
**[SW] Rules:** In the 2026 baseline, pairs with Gura are memories and callbacks, and pairs with Ame are guest appearances. Nicknames are used as each member uses them (Kiara's "Goobidiba," "quasoni"). All of these are friendships.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2020-11-15 | Gura's chicken prank on KFP | KFP lore |
| 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |
| 2024-09-22 | Ame on HOLOTALK | Kiara's oshi as guest |
| 2025-04-26/30 | Kronii's and Kiara's last collabs with Gura | Farewells |
| 2026-01-08 | "TAKO∞TAKOVER" digital release (lyrics by Calli) | Ina × Calli |
**Dossier · Hard Facts (continuity):**
- Kiara's EN oshi: Ame. Kiara's names: "Goobidiba" (Gura), "quasoni" (Kronii).
- Ina designed Death Sensei, Bubba and the Takodachi; Calli wrote "TAKO∞TAKOVER."
- 2026 baseline: pairs with Gura are memories; pairs with Ame are guest appearances.

Incoming claims continue in `myth3-incoming.md`.

### projects/holoen/research/qa/packets/myth3-incoming.md

# Audit packet: myth3 (incoming claims)

Snapshot: git c06ffa3.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: th and Kronii: Other Pairs|Kronii and Kiara|Kiara and Kronii|Kronii and Gura|Gura and Kronii|Takanashi Kiara|hololive -Myth-|Gura and Kiara|Kiara and Gura|Ame and Calli|Calli and Ina|Calli and Ame|Ame and Kiara|Kiara and Ame|Ina and Calli|Gura and Ina|Ina and Gura|Ame and Ina|Ina and Ame|Rocku Wawa|Kusotori|Tenchou|Kiwawa|小鳥遊キアラ|Kiara|Wawa)(

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Takanashi Kiara: a German-speaking senior ("EterniTea"; "HoloEU" with Raora).
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Takanashi Kiara | Senior ("EterniTea"; "HoloEU" with Raora) | They spoke German in their first exchange, on Kiara's 2024 birthday stream | [Observed CI2, secondary; Kiara file] |
- `bible/characters/Cecilia-Immergreen.md › Story Engine`: 4. Kiara and Cecilia argue in German while everyone else guesses.

### from Ceres Fauna
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA"
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: (2022); Fauna was Kiara's HOLOTALK guest a week before graduating.
- `bible/characters/Ceres-Fauna.md › Voice Profile`: - Measured (F20; four 2024 windows): median pitch about 280–306 Hz (283–300 in chat, 293 while building, 306 in the horror game); in the cleaner windows p10–p90 is about 210–445 Hz. High in this project's samples, near Kiara's (245–300 Hz) and above IRyS's (214–226 Hz). About 105–120 words per minute of speech in chat and building, 92 in the horror game, about 154 in the closing superchat list. Sample results only; not a ranking.
- `bible/characters/Ceres-Fauna.md › Background Timeline`: | 2024-12-27 | 1,000,000 subscribers; Kiara's HOLOTALK guest the same day | [Observed F2; F3 title] |
- `bible/characters/Ceres-Fauna.md › Relationship Map`: | Takanashi Kiara | Myth senior | "KIWAWA vs FAWNA" (Clubhouse 51, 2022); Minecraft Wither fight; Kiara's HOLOTALK 32nd guest (2024-12-27) | [Observed F3; Kiara archive] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Takanashi Kiara: calls her "Erby Berby." 2026 birthday-live guests: FUWAMOCO, Polka, Nene, Watame, Iroha, Subaru, Roboco, Sora, Choco, Marine and Korone.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Takanashi Kiara | Myth senior ("Eternal Flame," "11 ERBs and Spices") | Kiara calls her "Erby Berby"; Minecraft (2025); Kiara's Mage Arena collab (2025) | [Observed EB2, EB3] |

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Groups`: hololive -Myth- (graduated), hololive alum, Myth, hololive English (former branch name)
- `bible/characters/Gawr-Gura.md › [SW] Background`: Gura is a VTuber and a hololive alum: she graduated from hololive -Myth- on May 1, 2025.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Raora Panthera: R.E.P.O. with Kiara and Kronii (2025).
- `bible/characters/Gawr-Gura.md › Voice Profile`: - "Speaking of bottom, did you guys watch Kiara's stream?"
- `bible/characters/Gawr-Gura.md › Voice Profile`: - **Code-switching:** small doses of Japanese ("domo," "same desu," "yabai," "arigato," "Manager-san"). She is not fluent, but sang city pop with flawless Japanese pronunciation at her debut; she took Japanese and German lessons from Kiara. [Official G1] [Observed G2 §Miscellaneous and §Quotes; G13]
- `bible/characters/Gawr-Gura.md › Voice Profile`: - Other members' openers (Kiara's "Kikkeriki," Calli's "What is up, humans?!").
- `bible/characters/Gawr-Gura.md › Background Timeline`: | 2020-12 / 2021-03 | Japanese and German lessons with Kiara | [Observed G13] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Takanashi Kiara | Myth genmate ("SameTori") | Kiara calls her "Goobidiba" and taught her Japanese and German (and German swears); Gura filled the back room of Kiara's KFP building with chickens in a Minecraft prank (2020-11-15) | [Observed G2 infobox; G13; G20 §KFP, secondary] |
- `bible/characters/Gawr-Gura.md › Hard Facts`: - Nicknames: Same-chan, City Pop Shark, Samegaki, Gooba, Goob, Goobidiba (by Kiara), George (by Miko). "Goomba" and "Apex Predator" are left out of Other Names because they would match unrelated text. [Observed G2 infobox]

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Takanashi Kiara: Reanimal ("ULTRA ORANGE WILL LIGHT THE WAY!!") and Eden Eternal with Shiori; Kiara calls her "GeeGee."
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Takanashi Kiara | Senior ("Ultra Orange," from Gigi's stream title); calls her "GeeGee" (secondary) | Reanimal (2026-04-03); Eden Eternal with Shiori (2024); first-model ASR only, pending verification: Gigi decorated a page in the friendship journal Kiara brought to the 2026 fes.; "I know Kiara saved the world. Literally." (Hytale) | [Observed GG2, GG3] [ASR GG20, LgDuyqoaqT4 1:01:53, 1:16:19] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Shiori Novella, Koseki Bijou | Advent ("NovelGrem" with Shiori, secondary); GAGA = Gigi, Cecilia, Shiori, Bijou | GAGA: Trine 5 (2024), Heave Ho (2024), Phasmophobia (2025). Separately: Eden Eternal was Kiara, Shiori and Gigi (2024); the Fanfic Club is a different group (Gigi, Shiori, Pavolia Reine, Airani Iofifteen; secondary); a voice in Shiori's non-canon motion comic "Into The Void" (2026); "MONSTER" with Shiori at -All for One- | [Observed GG2, GG3] [Official GG5] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Groups`: hololive -Advent-, hololive English -Advent- (former branch name), Advent, Rocku Wawa
- `bible/characters/Koseki-Bijou.md › [SW] Background`: (2025), starred with Ina and IRyS at hololive night at Dodger Stadium (2025), sang a solo and two group numbers at the 2025 English concert -All for One-, and was paired with Takanashi Kiara at the 2026 Serendipity concert.
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Takanashi Kiara: her 2026 Serendipity partner ("Rocku Wawa"), who calls her a "hidden gem" and encouraged her through hard choreography for a song with Kiara and Ame; Bijou admires Kiara's "confidence," and they keep saying "67."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.
- `bible/characters/Koseki-Bijou.md › Voice Profile`: - **Code-switching:** learning Japanese seriously and planning a Japanese-lesson stream with a real teacher ("killing two birds with one stone, learning Japanese and making content out of it"); "I do speak a little Thai!" (her 2023 post on X); "ROKU NANA~ I mean… rokku wawa." [ASR KB20, 6:03:51] [Official KB4] [Observed KB6, X post 1684542578962964480]
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2026-07-03/04 | Serendipity concert, duo with Takanashi Kiara ("Rocku Wawa") | [Official KB4] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Takanashi Kiara | Senior; Serendipity 2026 duo ("Rocku Wawa") | BG3 (2023); Kiara once asked her to perform a song with her and Ame; in the official interview Kiara calls her a "hidden gem" with "so much charm," and Bijou admires Kiara's "confidence"; their shared joke is "67" | [Official KB4] [Observed KB3; Kiara archive] |
- `bible/characters/Koseki-Bijou.md › Arc`: - **Starting point:** active member at the 2026 baseline: a 900K+ channel, two original songs, the Serendipity duo with Kiara.
- `bible/characters/Koseki-Bijou.md › Story Engine`: 2. Kiara and Biboo try to stop saying "67" for an entire collab.

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Groups`: hololive, hololive -Myth-, Myth, CHADCast, hololive English (former branch name), Last Writes
- `bible/characters/Mori-Calliope.md › [SW] Background`: She debuted first in hololive -Myth- in September 2020; her fans are the Dead Beats, her mentor is Death Sensei, her publicly depicted cat mascot is Tutu, and her scythe is named Ricky.
- `bible/characters/Mori-Calliope.md › [SW] Background`: Myth still includes Takanashi Kiara and Ninomae Ina'nis; Gawr Gura has graduated, and Watson Amelia is an affiliate.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Takanashi Kiara: her TakaMori partner.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo.
- `bible/characters/Mori-Calliope.md › Voice Profile`: - "Hey, Kiara...unzip your pants?" → a line to Kiara; context not documented.
- `bible/characters/Mori-Calliope.md › Voice Profile`: - "kusotori / くそ鳥" ("shitty bird") is for Kiara specifically. [Observed C7; C25 §Takamori, secondary]
- `bible/characters/Mori-Calliope.md › Voice Profile`: 7. "Hey, Kiara...unzip your pants?" (C4 §Quotes, secondary)
- `bible/characters/Mori-Calliope.md › Appearance Anchors`: - A foldable scythe with pink accents, nicknamed "Ricky," carried on her back. [Observed C4 §Appearance and §Personality, secondary] The name is reportedly a nod to Kiara's "Kikkeriki." [Observed C26, secondary snippet and clip title]
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2026-09-07 | The branches merge into one "hololive." Her unit is now hololive -Myth-. | [Official C17, C1] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Takanashi Kiara | Myth genmate | Calli calls her "kusotori" ("shitty bird") and usually rebuffs her, while supporting "TakaMori." They play "Mom" and "Dad" to Kobo. | [Observed C7; C25 §Takamori, secondary] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Kobo Kanaeru | Collaborator | "Uncle Dad" / "Dad" bits; Calli and Kiara play "Dad" and "Mom" to her. [Unverified, title only: Kobo picking up and repeating Calli's swear words] | [Observed C14; C25 §Takamori, secondary; C27 clip titles] |
- `bible/characters/Mori-Calliope.md › Hard Facts`: - Birthday April 4 (4/4: "shi" is also "death"). Height 167 cm. Debut 2020-09-12. Unit: hololive -Myth-. [Official C1] [Observed C4 §Miscellaneous, secondary]

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Takanashi Kiara: fellow bird of HOLOTORI, who calls her "Moomsies"; they sang a DECO*27 song together at the 4th fes.
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: (2023), and Mumei was Kiara's HOLOTALK guest in her last week.
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: (2023), "Beyond the way" with Kiara at the 2024 concert, "SAD GIRL HOURS"
- `bible/characters/Nanashi-Mumei.md › Voice Profile`: - **Macabre and grandiose humor:** a cute voice with dark content: drawings that turn Tim Burton-esque or demonic, cheerful reminders that everyone dies. [Observed M2 §Personality, secondary]. Bravado: "I've never been scared of anything ever." [ASR M20, 0:26:39]. Ranking who she'd beat at arm wrestling: "I think I would win against Gura, Kiara, IRyS, Nerissa, and Mococo"; she moved Biboo to the losing side ("she is a rock") and concluded that most of EN could beat her: "But I have other skills and things that make me special, so whatever." [ASR M20, 0:23:52–0:27:44; the models disagree on the word "EN"]
- `bible/characters/Nanashi-Mumei.md › Background Timeline`: | 2023-03-18/19 | 3D idol costume and main 3D model at hololive 4th fes.; sang a DECO*27 song with Kiara on the holo*27 stage | [Observed M2 §2023; M4] |
- `bible/characters/Nanashi-Mumei.md › Background Timeline`: | 2024-08-24 | -Breaking Dimensions- day 1: premieres "It's Not a Phase" with Fauna; "Beyond the way" with Kiara and Nerissa; day 2: her original "A New Start" | [Official M5] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Takanashi Kiara | Myth senior; bird unit HOLOTORI | "BUILDER BIRBS" (2021); "Kiwawa & Mumeiwi" (2022); the 4th fes. holo*27 stage (2023); "two smol beans" (2025); HOLOTORI R.E.P.O. (2025-04-18); Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies" | [Observed M2 infobox; M3; M4] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Nerissa Ravencroft | Advent kouhai | "EMO HOURS: IT WAS NEVER A PHASE with NERISSA" (2023); "Beyond the way" with Kiara and Nerissa at -Breaking Dimensions- (2024); "SAD GIRL HOURS" (2025-04-20) | [Observed M3] [Official M5] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, and they held a 2025 "BIRB GIRLS"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025); with Kiara they sang "Beyond the way" at the 2024 English concert.
- `bible/characters/Nerissa-Ravencroft.md › Behavioral Traits`: 3. She is an open fangirl of Houshou Marine and Takanashi Kiara (a self-described KFP member); in her lore she worked at KFP before hololive. [Observed N2 §Likes and dislikes, §Lore, secondary]
- `bible/characters/Nerissa-Ravencroft.md › Voice Profile`: - Measured (N20; a 2026 solo chat): median pitch about 214 Hz (p10–p90 172–297 Hz), a mid-range speaking voice like IRyS's (214–226 Hz), lower than Kiara or Gura; about 159 words per minute of speech. Group-stream windows read higher (284–289 Hz) because several voices share them. Sample results only.
- `bible/characters/Nerissa-Ravencroft.md › Voice Profile`: | Fangirling (Kiara, Marine) | Fast, flustered, delighted | (no verified line; see Relationship Map) |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Takanashi Kiara | Senior and her oshi ("KiaRissa") | Self-described KFP member; in lore, a former KFP employee | [Observed N2] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Mori Calliope | Senior | Nerissa was Calli's first Instagram follower; BG3 party "Killing, Two Birds, with One Stone" with Kiara and Bijou (2023); duet "OVER//RIDE" (2025); Calli guested at Nerissa's 3D concert; building Calli's Mii: "Calli's also got beautiful, long, straight hair." | [Observed N2; N3 titles; ASR N20, agrees] |
- `bible/characters/Nerissa-Ravencroft.md › Story Engine`: 3. She meets Kiara at an event and forgets every word of English.

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Octo'clock
- `bible/characters/Ninomae-Inanis.md › [SW] Background`: She released her first EP, re:VISION, and held the duo concert Drawn to Dawn with Takanashi Kiara in 2026, and she partners with Ouro Kronii.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Takanashi Kiara: TakoTori duo-concert partner (Drawn to Dawn, 2026); Ina calls Kiara the gas pedal and herself the brake, Ina credits Kiara's support with helping her gain confidence in dancing, and Kiara groans at her puns.
- `bible/characters/Ninomae-Inanis.md › Behavioral Traits`: 10. Kiara's account, as reported by the wiki: Ina is the first to message Kiara when Kiara is down. [Observed I2 §Personality, secondary] A single reported anecdote, not a general rule; off the card.
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **Profanity:** her ordinary speech favors mild exclamations: she has said she "usually never swears," and a rare "damn" from her made headlines in clips [Observed I15 clip titles]; about an hour of checked audio had no swearing in her own words [ASR I29]. Sharper language and bawdy wordplay turn up in specific exchanges (above). Constant swearing in Kiara's or Calli's register would be out of character; an occasional sharp word is not.
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **How she addresses people:** "you guys," "everyone," "chat," and fans as "Takodachi" (the official fan name is the Tentacult). Members by first or short name ("Calli," "Kiara," "Ame," "Gura," "Kronii," "Bae," "Biboo," "CC"); a full name signals a mock-serious scold. New members are "kouhais." She gives her own name surname-first. [Official I1] [Observed I3 captions; I2 §Mascot and fans]
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026-03-27/28 | "Drawn to Dawn" duo concert with Kiara (Los Angeles) | [Official I20, I21] |
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026-09-07 | Branches merge; she is "Ninomae Ina'nis from hololive," unit hololive -Myth- | [Official I28] [Observed I10] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Takanashi Kiara | Myth genmate ("TakoTori," fan term) | Duo concert 2026; Kiara encouraged her dance work; Kiara groans at her puns; Kiara once "fired" her over the chicken incident; the wiki reports Kiara saying Ina is the first to message her when she's down (secondary, off the card) | [Official I20] [Observed I2 §Personality; Kiara file T2 §KFP] |
- `bible/characters/Ninomae-Inanis.md › Hard Facts`: - Birthday May 20; height 157 cm; debut 2020-09-13; unit hololive -Myth-; illustrator Kuroboshi Kouhaku (whom she calls "papa"). [Official I1] [Observed I2 infobox]

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Takanashi Kiara: a fan before Kronii debuted who calls her "quasoni."
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Korean: she speaks it fluently, a language she shares with Ina [Observed K8 §Miscellaneous, secondary]; a language exchange with Kiara is reported by a clip title [Unverified, K17]. Rare outside those exchanges (estimate).
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Takanashi Kiara | Senior colleague ("Sundial") | Kiara was a fan before Kronii debuted. [Unverified, title only: a language exchange where Kronii taught Korean phrases] | [Observed K8 §Miscellaneous, secondary; K17 clip] |

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › [SW] Background`: Seishun Massakari") and sang "What an amazing swing" with Tsunomaki Watame and Takanashi Kiara.
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Takanashi Kiara: "HoloEU" with Cecilia; an Italian lesson, a proposed Kiara outfit on her "Raora's Clawset" art stream, the "Doom" in Kiara's Mage Arena collab, and "What an amazing swing" with Tsunomaki Watame at Serendipity.
- `bible/characters/Raora-Panthera.md › Behavioral Traits`: 3. Food opinions as law: pizza (with fries), pasta rules ("No break-a da pasta!"), EU snacks with Kiara. [Observed RP2 §Quotes, §Likes, secondary; RP3]
- `bible/characters/Raora-Panthera.md › Behavioral Traits`: 5. "Doom.": her friendly-fire "Doom" spell in Kiara's Mage Arena collab (2025-11-16) became a widely shared fan meme (secondary account); she later used "Doom." as a stream title. [Observed RP7; RP3]
- `bible/characters/Raora-Panthera.md › Background Timeline`: | 2025-11-16 | The "Doom" spell in Kiara's Mage Arena collab | [Observed RP7] |
- `bible/characters/Raora-Panthera.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official RP4, RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Takanashi Kiara | Myth senior ("HoloEU" with Cecilia; secondary) | An Italian lesson (2024), a proposed outfit for Kiara on her "Raora's Clawset" art stream (2025-01-26; not a released Kiara model), an EU-snacks off-collab (2025); the "Doom" meme in Kiara's collab; "What an amazing swing" with Watame at Serendipity (2026) | [Observed RP3, RP7] [Official RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Tsunomaki Watame (JP) | JP senior | "What an amazing swing" with Kiara at Serendipity (2026) | [Official RP9] |

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Takanashi Kiara: hosted Advent on HOLOTALK; an occult handcam off-collab ("#shiotori").
- `bible/characters/Shiori-Novella.md › Background Timeline`: | 2023-08-12 | Advent on Kiara's HOLOTALK | [Observed SN3; Kiara archive] |
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Takanashi Kiara | Senior | HOLOTALK (2023); an occult handcam off-collab "#shiotori" (2024-07-12); Eden Eternal (2024) | [Observed Kiara archive] |

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Groups`: hololive (affiliate), hololive -Myth- (affiliate), Myth, hololive English (former branch name)
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug.
- `bible/characters/Watson-Amelia.md › Voice Profile`: - **How she addresses people:** "you guys" by default; "chat" occasionally; "Teamates" (one m, official) on big occasions; members "Investigators." Members by name ("Gura," "Calli," "Ina," "Kiara," "Kronii"); Bubba, her dog mascot. She gives her name in English order, "Amelia Watson." [Official A1] [Observed A3 captions; A2 §Mascots and fans]
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Takanashi Kiara | Myth genmate | Kiara calls Ame her EN oshi and credits her for help with 3D productions; Ame made HOLOTALK intro material; "Kiara like, threw herself at me… she hugged me!" | [Observed A2 §Quotes; Kiara file T2 §Likes and dislikes, T9] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › [SW] Other Names`: ShioRaven, Goth Rock, Pen Pups, JewelBird, Diamond Dogs, Sound Hounds, Grindstone, GAGA, FUWAMOCALLI, Rocku Wawa, GreyScaleX, Last Writes
- `bible/world/Advent-Pairs.md › [SW] Description`: With seniors: Mori Calliope starred in Bijou's Undertale mod and did a 24-hour charity stream with her, shares "FUWAMOCALLI" with the twins (a collaboration name they say they particularly like), and was Shiori's 2026 concert partner; Kiara hosted all five on HOLOTALK, encouraged Bijou through hard choreography, and partnered her in 2026 ("Rocku Wawa"); IRyS is Bijou's horror co-op partner, and Bijou, Ina and IRyS starred at hololive night at Dodger Stadium (2025); Shiori and Kronii hosted "Rating Your Clocks" together in March 2025.
- `bible/world/Advent-Pairs.md › Inside Advent`: - **As five:** HOLOTALK guests together (2023-08-12, Kiara's 29th episode, 0Q9FLtcAY0s), PEAK collabs (2025-07-03 and 07-11; YyOprplcI3g, SpRrILmDAJ8, jktQRY_Slds), a "friendship test" collab in their new casual outfits (2025-02, 1ZqkPlxIdZI), the 3D collaboration stream (2024-08-17 PDT), anniversary lives "On the Run!" (2025) and "Bound by Fate" (2026), and Advent songs "Rebellion," "Genesis" (2025), "Breakout" (2026-01-26) and "Spotlight" (2026). [Observed S1; S2] [Official S3, S9]
- `bible/world/Advent-Pairs.md › With Myth`: - **Takanashi Kiara:** hosted all five on HOLOTALK; an occult handcam off-collab with Shiori ("#shiotori," 2024-07-12); Baldur's Gate 3 with Bijou, Calli and Nerissa ("Killing, Two Birds, with One Stone," 2023); Bijou was her 2026 Serendipity partner ("Rocku Wawa," and a running "67" joke); Bijou recalls Kiara as "really encouraging and helpful" when Kiara asked her to perform a song with Kiara and Ame whose choreography was one of the hardest she had learned. [Official S4] [Observed S1]
- `bible/world/Advent-Pairs.md › History`: | 2023-08-12 | HOLOTALK with Kiara; Bijou's Undertale replay with Calli | senior ties |
- `bible/world/Advent-Pairs.md › History`: | 2026-07-03/04 | Serendipity: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth | official interviews |
- `bible/world/Advent-Pairs.md › Conflicts and Story Hooks`: 5. Kiara and Bijou try to keep "67" out of a serious concert rehearsal.
- `bible/world/Advent-Pairs.md › Hard Facts`: - Serendipity 2026 pairs: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth (official).

### from AmeSame
- `bible/world/AmeSame.md › [SW] Description`: At the 2026 baseline Ame is an affiliate and Gura has graduated; their shared history lives on in callbacks, their gold-and-blue colors, and Kiara's tribute song "Blue & Gold."
- `bible/world/AmeSame.md › How It Works`: - **The goodbye (2024):** on 2024-09-29, the day before Ame concluded her regular activities, Gura's channel streamed "【💛💙】Looking at our old DMs" with Ame; the next day they played Deep Rock Galactic with Kiara and Kronii. [Observed S1]
- `bible/world/AmeSame.md › How It Works`: - **After:** Gura graduated on 2025-05-01. In 2026 Kiara's album includes "Blue & Gold," a tribute to both. [Observed S3 §Miscellaneous, secondary]
- `bible/world/AmeSame.md › History`: | 2026-02 | Kiara's "Blue & Gold" tribute | The colors as a memory |

### from Bone Bros
- `bible/world/Bone-Bros.md › [SW] Description`: (2024) and, with Kiara, said she would keep singing it.
- `bible/world/Bone-Bros.md › How It Works`: - **"Full Color":** Gura's single was never released; Calli performed it at hololive English -Myth-'s fourth-anniversary concert "The Show Goes On!" (September 2024), and Calli and Kiara said they would keep singing it in karaoke. [Observed S2 §Miscellaneous, secondary; archived official broadcast CDljbqawDkw]

### from Concerts and Live Events
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: Recurring formats: each spring, hololive fes. with hololive SUPER EXPO in Japan (a combined tradition since 2022; Calli and Kiara sang at the 2022 fes. in Makuhari, Nerissa at the 6th fes. in 2025); each summer, a hololive English concert in the US (2023 "-Connect the World-"; 2024 "-Breaking Dimensions-,"
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: Los Angeles, July 3–4, built on units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia), with guests Ookami Mio, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame singing alongside EN members); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet.
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn"
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive fes. + hololive SUPER EXPO** (spring, in Japan; the combined fes./EXPO tradition dates to 2022, while fes. itself is older): the agency-wide concert and convention. 3rd fes "Link Your Wish" (2022-03, Makuhari; Calli and Kiara performed on day 2, per their X posts), 4th fes "Our Bright Parade" (2023), 5th "Capture the Moment" (2024), 6th "Color Rise Harmony" (2025-03-08/09; Nerissa on day 1), 7th "Ridin' on Dreams" (2026-03-06/08). EN units share Expo booths and key visuals (Myth with Promise, Advent with Justice). [Observed S1 §2023–§2026; S2]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous" [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before and separate from "-Breaking Dimensions-"), Jakarta (11-09), Singapore (11-30, with a pre-concert panel of Kaela Kovalskia and Ouro Kronii), Atlanta (12-15, a panel of Nerissa and Elizabeth Rose Bloodflame), Kuala Lumpur (12-21, Nerissa and Elizabeth again) and Taipei (2025-01-18, the finale) [Official S7]; and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Takanashi Kiara | 4th-anniversary live "MIRAGE" (2024-10-06); "KIARA & FRIENDS: H!P Cover Song Spring Concert" (2025-04-21); "Drawn to Dawn" with Ina (2026-03-27/28, The Wiltern); World Tour '24 performer; Serendipity with Bijou | Kiara file T11, T12, T10; S3 titles |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ninomae Ina'nis | 3D live "Pleiades" (2024-12-28); "Drawn to Dawn" with Kiara; World Tour '24 performer; Serendipity with Kronii | Ina file I20, I7; S3 title |
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 4. An aftertalk where Kiara and Ina disagree about who cried first at "Drawn to Dawn."

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix cover as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa."
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI").
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Takanashi Kiara:** Usada Pekora is her oshi ("Senpai! Be my guide for the day!", 2020; HOLOTALK's 24th guest, 2022). Pavolia Reine is a recurring collaborator on her channel (30 streams; their pair name "PavoNashi"; a VR "vacation," a Minecraft summer festival; the bird unit "HOLOTORI" with Subaru, Reine, Mumei and Lui); Kobo calls her "Mommy Kiwawa." Other units: "O'riends" (Momosuzu Nene), "KoAra Connect" (Hakui Koyori), "SunMoon"/"Eclipse" (Moona Hoshinova). Outside hololive: "PomuTori" (Pomu Rainpuff), "Mintori" (Mint Fantôme). [Observed S1; S2 Kiara; Kiara file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Nanashi Mumei** (graduated): HOLOTORI with Kiara, Subaru, Reine and Lui ("【MUMEI + LUI】Q&A With Bird Sisters !!!," 2025-04-19, fEO6kSCseE0); drawing collabs with Airani Iofi ("Doodles with IOFI," 2022-04-14, 2dWx7xg48xc; "SWIMSUITS!! with IOFI!," 2023-01-30, XCXF08GMUHY); a duet cover of "とんとんまーえ！" with Inugami Korone (2025-04-23, P6GLC_HnCUU), and Okayu, Korone, Nene and Koyori as guests at her 3D live "Outside the Box" (2024-08-05, gl7CwlEg2ZI); Minecraft "Peace & Love with HAACHAMA" (2025); Tokoyami Towa calls her "Mumi-chan." [Observed S1; Mumei file M2]
- `bible/world/Cross-Branch-Friends.md › How It Works in Stories`: - Senpai and kouhai describe relative seniority (who debuted first), not language or nationality; forms of address and levels of formality vary by relationship. Some EN members are openly starstruck by particular senpai (Calli by Suisei, Kiara by Pekora, Nerissa by Marine). [Observed character files]
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 5. Kiara and Reine plan another "vacation" in VR.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Calli's senpai: Suisei. Kiara's oshi: Pekora. Nerissa's oshi: Marine (and Kiara).

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Myth and Promise:** "FUWAMOCALLI" with Mori Calliope (a twin game show and Smash in 2023, a tea party, an off-collab karaoke in 2024); Fuwawa also joined Mori Calliope and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"; Fuwawa's post, not a twin appearance); "Detective Dogs" with Watson Amelia (Escape Simulator, 2024-09-24); "WatchDog" with Ouro Kronii; "Fuwamoomco" with Nanashi Mumei (Overwatch, 2025-03-01); they helped Ceres Fauna on her last World Tree stream (2024-12-31); Kiara hosted them on HOLOTALK (2023). [Observed S1; S3; Mumei, Calli, Kiara archives]

### from Fauna and Mumei Pairs
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Other Names`: Fauna and Mumei, Mumei and Fauna, It's Not a Phase, KronMei, gumei, Fauna and Gura, Mumei and Kiara, Mumei and Kronii
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Mumei and Kiara are birds of HOLOTORI; Kiara calls her "Moomsies" and hosted both on HOLOTALK before they left.
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Mumei also drew with Ina, did "Anatomy Review" with Calli, played with Ame in Ame's last regular week, and held "emo hours" with Nerissa; at the 2024 concert Mumei sang with Kiara and Nerissa, and Fauna with Shiori and Nerissa.
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Kiara:** Mumei and Kiara are birds in HOLOTORI (with Subaru, Reine and Lui): "BUILDER BIRBS" (2021), "Kiwawa & Mumeiwi" (2022), a DECO*27 song together on the 4th fes. holo*27 stage (2023), "two smol beans" (2025-03-26) and Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies." Fauna and Kiara: "KIWAWA vs FAWNA" (2022), Pokémon Unite practice (2023), and Fauna was HOLOTALK's 32nd guest (2024-12-27), a week before she graduated. [Observed S1; S3 infobox; S4]
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Nerissa:** Mumei's "EMO HOURS: IT WAS NEVER A PHASE with NERISSA" (2023) and "SAD GIRL HOURS" (2025-04-20); at -Breaking Dimensions- (2024) Mumei sang "Beyond the way" with Kiara and Nerissa, and Fauna "Lonely in Gorgeous" with Shiori and Nerissa; a 2023 reply from Nerissa to Fauna on X: "Fauna-senpai!!! My Raven companion is named Shadow~". [Observed S1; research/x-posts.md, via wiki citation] [Official S6]
- `bible/world/Fauna-and-Mumei-Pairs.md › History`: | 2023-03-19 | Mumei sings with Kiara on the 4th fes. stage | HOLOTORI |
- `bible/world/Fauna-and-Mumei-Pairs.md › History`: | 2024-12-27 | Fauna on Kiara's HOLOTALK | — |
- `bible/world/Fauna-and-Mumei-Pairs.md › Hard Facts`: - Fauna's oshi: Gura. Kiara's name for Mumei: "Moomsies." HOLOTORI includes Kiara and Mumei.

### from IRyS and Nerissa Pairs
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: IRyS and Kiara: Kiara gave her a German crash course; nail-painting off-collab.
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: Nerissa and Kiara (KiaRissa): Kiara is Nerissa's oshi; Kiara showed her around Minecraft; a 2025 "BIRB GIRLS"
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Rules`: Recent pairings (IRyS with Kronii, Calli and Ina; Nerissa with Kiara and Calli) carry the most weight; pairs with Gura are memories.
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Kiara** (13 / 1 / 3 / 2 / 3 / 0): Kiara's "1ST FULL HOLOEN COLLAB ft. IRYS!" (2021-08-12); a "GERMAN CRASH COURSE … with IRYS" (2022-06-02); an off-collab doing each other's nails on camera (2023-11-14); TORIDAMA 2 off-collab with Kronii and Raora, "Who is the BRAVEST?" (2024-08-01). [Observed S1 titles]
- `bible/world/IRyS-and-Nerissa-Pairs.md › Nerissa`: - **Nerissa and Kiara ("KiaRissa")** (15 / 12 / 3 / 0): Kiara is Nerissa's oshi; in Nerissa's lore she worked at KFP before hololive . "Compatibility test with Kiara-senpai" (2023-08-14); Kiara showed her around the EN Minecraft server (2023-09-07); their Baldur's Gate 3 party with Calli and Bijou ("Killing, Two Birds, with One Stone," 2023); "Rating your CARS with NERISSA" (2023-10-21); "GIRLSTALK with Nerissa, EN BIRB GIRLS PARTY!" (2025-04-08); a CHICAGO watchalong "with the musical connoisseur Nerissa" (2025-07-09). [Observed S1 titles; S3 Nerissa §Relationships, §Lore, secondary]
- `bible/world/IRyS-and-Nerissa-Pairs.md › History`: | 2023-08-14 | Nerissa's compatibility test with Kiara | KiaRissa |
- `bible/world/IRyS-and-Nerissa-Pairs.md › Conflicts and Story Hooks`: 3. Nerissa guests on Kiara's stream and fangirls so hard she forgets the topic.
- `bible/world/IRyS-and-Nerissa-Pairs.md › Hard Facts`: - CHADCast = IRyS, Calli, Bae. KiaRissa = Kiara and Nerissa. IRyS and Kronii are -Promise- genmates.

### from Justice Pairs
- `bible/world/Justice-Pairs.md › [SW] Description`: With seniors: Gigi repeatedly uses Calli's full name and jokes about getting her into League of Legends; within HoloEU, Raora teaches Kiara Italian and Cecilia speaks German with her; Cecilia plays up a rivalry with Ina; Kronii is Raora's "Pizza Time" collaborator and Gigi's Fatal Fury and Hytale partner, and secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai"; Automatowl names Cecilia and Mumei.
- `bible/world/Justice-Pairs.md › With Advent`: - **Shiori:** Elizabeth ("NovelFlame," "BloodQuill"; secondary) and Gigi voice parts in Shiori's non-canon motion comic "Into The Void" (2026; episode 2 also credits Calli); Gigi ("NovelGrem") games with her often (Heave Ho, a Fateful Findings watchalong, Project Zomboid, Phasmophobia; Eden Eternal was Kiara, Shiori and Gigi); the "Fanfic Club" (Gigi, Shiori, Pavolia Reine, Airani Iofifteen) is a separate group from "GAGA" (Gigi, Cecilia, Shiori, Bijou); Raora: a 2024 outfit-design collab (2024-12-05) and Blood Typers with Kronii and Bijou (2025-06-10); Cecilia: "Break It Down" with Vestia Zeta at Serendipity; Gigi: "MONSTER" with Ina and Kronii at -All for One-. [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Myth`: - **Takanashi Kiara:** "HoloEU" with Cecilia and Raora (secondary label): Raora teaches Kiara Italian (a lesson, 2024-10-04), designed a proposed Kiara outfit on her "Raora's Clawset" art stream (2025-01-26; not a released model) and held an EU-snacks off-collab (2025-03-11); Raora and Kiara sang "What an amazing swing" with Tsunomaki Watame at Serendipity; Eden Eternal with Gigi and Shiori (2024); Kiara and Cecilia spoke German in their first exchange (Kiara's 2024 birthday) ("EterniTea"); Gigi and Kiara are "Ultra Orange" (Reanimal, 2026-04-03); Kiara calls Elizabeth "Erby Berby" ("Eternal Flame"). [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Myth`: - **Gawr Gura (graduated):** Keep Talking and Nobody Explodes and The Forest with Cecilia (2025-02); R.E.P.O. with Raora, Kiara and Kronii (2025-04-13). **Watson Amelia (affiliate):** in ENReco's role-play story, Gigi's Gonathon and Ame's Jyonathan marry (secondary; "ClueChaser"); Borderlands 2 with Cecilia, Gigi and Mumei (2024-08-09). [Observed S1; S2]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone ("IT'S LOVE," iwnHChZq0N8, credits read by Claude); FUWAMOCO with Polka, Nene, Watame and Iroha; her 2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members). Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is "RaoRiRi" with Ichijou Ririka; "OkaGigi" is a secondary-documented name for Gigi and Nekomata Okayu, with no concrete shared activity sourced (dossier only). Tsunomaki Watame sang "Cloudy Sheep" with Calli and Cecilia and "What an amazing swing" with Kiara and Raora at Serendipity. FLOW GLOW: Koganei Niko sang with Elizabeth in LYRA. [Observed S1; S2] [Official S6, S7]
- `bible/world/Justice-Pairs.md › History`: | 2026-07-03/04 PDT | Serendipity: units Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora); guests' songs with Justice members: "HELP!!" (Kobo, Bae, Elizabeth), "Break It Down" (Zeta, Shiori, Cecilia), "Cloudy Sheep" (Watame, Calli, Cecilia), "MAKE IT, BREAK IT" (Zeta, FUWAMOCO, Gigi), "What an amazing swing" (Watame, Kiara, Raora) | [Official S3, S7] |
- `bible/world/Justice-Pairs.md › Conflicts and Story Hooks`: 3. Gigi tries to get Mori Calliope into League of Legends one more time, with Kiara as backup.

### from Streaming Life
- `bible/world/Streaming-Life.md › How It Works`: - **Formats:** gaming, horror games, chatting ("zatsudan"), karaoke (sometimes unarchived), art streams, watchalongs, superchat catch-ups, song releases and premieres, sponsored streams (#PR), talk shows (Kiara's HOLOTALK), tabletop RPGs, anniversaries and birthdays. [Observed]

### from TakaMori
- `bible/world/TakaMori.md › [SW] Other Names`: Takamori, TakaMori, Calli and Kiara, Kiara and Calli
- `bible/world/TakaMori.md › [SW] Description`: Mori Calliope and Takanashi Kiara are longtime close friends whose present-day public dynamic has an "old married couple" rhythm: familiar bickering, affectionate teasing and shared history despite fewer collaborations.
- `bible/world/TakaMori.md › [SW] Description`: Kiara says the love out loud, explaining that Calli "actually does like me a lot but is just really bad at expressing herself"; Calli deflects, then snaps "What do you mean?!
- `bible/world/TakaMori.md › [SW] Description`: I love Kiara!" when a fan suggests they're only friends "now."
- `bible/world/TakaMori.md › [SW] Description`: It began as Myth's founding double act: in 2020 Kiara declared a crush on Calli and named the ship "TakaMori," a persona joke pairing an immortal phoenix with a reaper who could never keep her dead; Kiara called Calli her "wife," and Calli rebuffed her as "kusotori"
- `bible/world/TakaMori.md › [SW] Description`: Calli made and narrated Kiara's debut intro.
- `bible/world/TakaMori.md › [SW] Description`: (2023), Kiara's watch party for Calli's 2025 concert, and a 2025 co-op series they titled "takamori split screen nostalgia."
- `bible/world/TakaMori.md › [SW] Rules`: Kiara is openly affectionate; Calli is gruff in words and loyal in actions, and "kusotori" is a term of endearment by now.
- `bible/world/TakaMori.md › How It Works`: - **The origin bit (2020):** on Calli's second stream Kiara declared a crush on her. The persona joke: an immortal phoenix paired with a reaper who could never keep her dead. Kiara named the ship "TakaMori." [Observed S2 §Takamori, secondary]
- `bible/world/TakaMori.md › How It Works`: - **The early routine (2020–21):** Kiara calls Calli her "wife," writes a ukulele song about wanting to marry her ("I Love Girls"), gives their hypothetical Sims child a name ("Clara Takamori") and "forgets" Calli in her amnesia re-debut ("Who's Calli?"). Calli rebuffs her and calls her "kusotori" ("shitbird"), which fans read as tsundere ("tsundereaper"), while supporting the #takamori hashtag. [Observed S2 §Takamori, secondary]
- `bible/world/TakaMori.md › How It Works`: - **Work together from day one:** Calli made Kiara's loading screen and intro video and narrated her debut intro; she once drew Kiara as a chicken saying "kicky ricky or whatever." [Observed S2 §Miscellaneous, secondary]
- `bible/world/TakaMori.md › How It Works`: - Kiara defends it plainly: "if Calli really had a problem with me, she would tell me in private… she actually does like me a lot but is just really bad at expressing herself." [Observed S2 Kiara §Quotes, secondary]
- `bible/world/TakaMori.md › How It Works`: - Calli, when a superchat says it is glad they are "friends now": "What do you mean?! I love Kiara!" [Observed S3 Calli §Quotes, secondary]
- `bible/world/TakaMori.md › How It Works`: - Kiara tells chat that Calli misplaces things in obvious places. [Observed S3 Calli §Personality, secondary]
- `bible/world/TakaMori.md › How It Works`: - They play "Mom" (Kiara, "Mommy Kiwawa") and "Dad" to Kobo Kanaeru; Calli insists she is not married to Kiara and Kobo is adopted. [Observed S2 §Takamori, secondary]
- `bible/world/TakaMori.md › How It Works`: - **Recent milestones (archive, S1):** an off-collab "Reunion & Gaming!! #takamori" and a karaoke collab (2022-06); off-collabs in 2023 (a Rubik's cube stream, "TAKAMORI OFF-COLLAB" with Kobo, doing each other's nails on camera with IRyS); their duet "Fire N Ice" (2023-12-14; lyrics by Calli and TeddyLoid); Kiara's off-collab watch party "cheering Calli on!!!" for Calli's GriMoire concert (2025-02-27); a four-part Split Fiction co-op series in April–May 2025, titled by them "takamori split screen nostalgia," "Perfectly In Sync with @TakanashiKiara," "thumbnail teetee manifestation into gameplay teetee" and "Saving the World with @TakanashiKiara"; Myth's 5th anniversary collab (2025-09-13) and the announced 6th anniversary live (2026-09-19; not verified as held).
- `bible/world/TakaMori.md › How It Works`: - **Heard in 2025 (ASR, S6):** in the first Split Fiction stream (Kiara's channel, 2025-04-06) the "parents" bit is alive: when Kobo shows up in chat, they tell her "Hi Kobo, go to bed! … What are you doing out of bed? Go to bed!", wish her a happy anniversary, and apologize: "Sorry Kobo, you can't be part of this because it's two players only. Next time…" When their game characters split into a fire mage and an ice mage, they riff on their own song: "Fire and ice, yeah. Fire and ice, death and life." When the split screen separates them: "Oh, double Takamori." [ASR S6, nE12CyKbaX8 0:07:49, 0:08:01, 0:22:36, 0:13:28; both models agree; who said which line is not separable from the transcript]
- `bible/world/TakaMori.md › How It Works`: - **Heard at the finale (ASR, S6; Calli's channel, 2025-05-02):** they bicker over an idiom like a long married pair. One mangles it ("glass stones in stone houses or whatever. I forget the term"), they argue over what it even means ("Okay, how about this? Don't cast stones when your body's made of glass."), and it ends with "I don't know that one. All right. All right. Well then, whatever. We don't need any of these metaphors." One of them, addressing Kiara (so presumably Calli), on her favorite of the studio's co-op games: "I'm an edgelord, Kiara. I like A Way Out the best… but you know me, I'm edgy, but I still love power, friendship and stuff." Wrapping up: "Split screen game finished by Takamori… because Takamori will always get together for these ones, right?" "Let's play more in the future." Earlier in the ending: "We got published together." "Together." [ASR S6, 2X8h7UI28mE 4:42:57–4:44:30, 4:36:00, 4:40:50, 4:31:35; both models agree]
- `bible/world/TakaMori.md › How It Works`: - **Old-married-couple rhythm [Author; supported by the lines above]:** bickering on autopilot, finishing each other's jokes, nostalgia about the early days, complaints that are really affection, and total trust underneath. Kiara says the love out loud; Calli deflects, then proves it by showing up.
- `bible/world/TakaMori.md › History`: | 2020-09 | Kiara declares the crush on Calli's 2nd stream; "TakaMori" named | The ship name |
- `bible/world/TakaMori.md › History`: | 2020-12 | Kiara's amnesia re-debut: "Who's Calli?" | Running gag |
- `bible/world/TakaMori.md › History`: | 2025-02-27 | Kiara's watch party for Calli's GriMoire concert | Cheering from the crowd |
- `bible/world/TakaMori.md › Conflicts and Story Hooks`: 2. Kiara brings up an old TakaMori clip on stream; Calli pretends to leave.
- `bible/world/TakaMori.md › Conflicts and Story Hooks`: 4. Calli shows up to cheer at Kiara's concert without announcing it, and gets caught.
- `bible/world/TakaMori.md › Hard Facts`: - "TakaMori" was named by Kiara (2020); toned down in 2021; they remain close friends.
- `bible/world/TakaMori.md › Hard Facts`: - Kobo's "parents" bit: Kiara "Mom," Calli "Dad"; "not married, Kobo is adopted."

### from TakoTori
- `bible/world/TakoTori.md › [SW] Other Names`: Kiara and Ina, Ina and Kiara, Drawn to Dawn
- `bible/world/TakoTori.md › [SW] Description`: Takanashi Kiara and Ninomae Ina'nis, Myth's gas pedal and brake.
- `bible/world/TakoTori.md › [SW] Description`: Ina's words: Kiara has "a very 'go-getter', lively energy,"
- `bible/world/TakoTori.md › [SW] Description`: Kiara's: "so different from me, and I love that," a mix of "cat fueled energy" and "energy drink fueled energy."
- `bible/world/TakoTori.md › [SW] Description`: Ina credits Kiara's support with helping her gain confidence in dancing; Ina is the quiet support, and Kiara has said Ina is always the first to message her when she's down.
- `bible/world/TakoTori.md › [SW] Description`: Ina designed Kiara's mascot Kotori, and Kiara still "fired"
- `bible/world/TakoTori.md › [SW] Rules`: Kiara leads with volume and plans; Ina answers with calm, a pun, or one quiet line that lands.
- `bible/world/TakoTori.md › [SW] Rules`: Their support is mutual and unshowy: Kiara hypes, Ina checks in.
- `bible/world/TakoTori.md › How It Works`: - Ina on Kiara: "one of us is the gas pedal and one of us is the brake"; Kiara has "a very 'go-getter', lively energy" while Ina is "laid-back, my-pace"; Kiara's support helped Ina get over being self-conscious about dancing; "you will always be our shining star!!!!" [Official S2]
- `bible/world/TakoTori.md › How It Works`: - Kiara on Ina: at first she "didn't see her as a big performer," then "could not stop thinking about Ina" when choosing a duo partner, for her music and her dance training; "so different from me, and I love that," "a perfect balance of cat fueled energy mixed with energy drink fueled energy." [Official S3]
- `bible/world/TakoTori.md › How It Works`: - **The chicken incident (2020):** after Gura filled the back room of Kiara's KFP building in Minecraft with chickens, Ina was checking on them when a creeper exploded and released them; Kiara "fired" Ina, and the incident became KFP lore. [Observed S4 §KFP, secondary]
- `bible/world/TakoTori.md › How It Works`: - **Ina, the quiet support:** Kiara has said that when she is down, Ina is always the first to message her (a statement Kiara made publicly, reported by Ina's wiki page). Ina also designed Kiara's mascot, Kotori. [Observed S5 §Personality, S4 §Mascot and fans, secondary]
- `bible/world/TakoTori.md › How It Works`: - **Kiara, the loud support:** Ina credits Kiara's support with helping her gain confidence in dancing. Kiara groans at Ina's puns like everyone else. [Official S2; Observed Ina file]
- `bible/world/TakoTori.md › How It Works`: - **Kibaba's future:** in Kiara's grandma-persona bit, future Ina lives near Kiara, who cooks for her so she doesn't just eat cup noodles and sleep on the floor. [Observed S4 §Lore, secondary]
- `bible/world/TakoTori.md › How It Works`: - **Recent milestones (archive, S1):** "TAKOTORI OFFCOLLAB!!" in Mario vs. Donkey Kong (Ina's title, 2024-03-04; Kiara's side was "Two Braincells At Work"); outfit design for each other judged by juniors ("Ina & Wawa Outfit Design!", 2023-12-30); the duo concert "Drawn to Dawn" at the Wiltern, Los Angeles (2026-03-27/28, announced 2025-11-23, new 3D outfits); Kiara's "Back from Drawn to Dawn!!!!! THANK YOU!!!!" (2026-04-01); a cover of "GETCHA!" together (2026-04-24).
- `bible/world/TakoTori.md › History`: | 2020-11 | The KFP chicken incident; Kiara "fires" Ina | KFP lore |
- `bible/world/TakoTori.md › Conflicts and Story Hooks`: 1. Rehearsal week: Kiara wants one more run-through, Ina wants a nap; both are right.
- `bible/world/TakoTori.md › Conflicts and Story Hooks`: 2. Kiara is down after a rough day; a message from Ina arrives first.
- `bible/world/TakoTori.md › Conflicts and Story Hooks`: 4. Kiara designs Ina's outfit and Ina designs Kiara's; neither admits the other's is better.
- `bible/world/TakoTori.md › Hard Facts`: - Kiara "fired" Ina over the 2020 chicken incident (a KFP bit).

### from Time Duo
- `bible/world/Time-Duo.md › How It Works`: - **On stream (archive, S1):** Ame's surprise karaoke off-collab with Ina, Kronii, Fauna and Mumei (2022-02-25, per S3); 5D Chess "I Don't Understand With @WatsonAmelia" (Kronii, 2023-04-08); Escape the Backrooms with Calli (2024-09-22) and Deep Rock Galactic with Kiara and Gura (2024-09-30, Ame's last week of regular streams).

### from VTuber Persona and Lore
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They use it as a joke engine: age jokes (Gura's "9,000-something," Kronii jokingly "60"), immortality and rebirth gags (Kiara), "canonically" framed bits (Ame calling in "from 2021" during Calli's 2026 charity stream). [Observed character files; Ame's wiki page §2026, secondary]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They can re-enter it for a bit and drop it again: Calli's reaper threats, Ina's "priestess" voice, Kiara's KFP manager routine, Ame's "Trust me, I'm a time traveler." [Observed character files]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - Lore can be retconned or joked about by the members themselves ("Kiara is a phoenix, not a chicken"); a member may improvise or contradict lore within a bit; an improvised joke does not automatically rewrite historical facts or permanent continuity. [Observed; Adaptation]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - **Edge example:** during a horror game, Kiara says "I'm immortal, I'll just respawn!" — that is a gamer joke about her lore; if her character dies in the game, she groans and restarts the level like anyone else.

### from hololive -Advent-
- `bible/world/hololive--Advent.md › [SW] Description`: (2026), and 2026 Serendipity pairs Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth and FUWAMOCO–Raora.
- `bible/world/hololive--Advent.md › [SW] Description`: Kiara hosted all five on HOLOTALK two weeks after their debut.
- `bible/world/hololive--Advent.md › How the Group Works`: - **Seniors:** Advent debuted after Myth, Project: HOPE and Council; the latter two were later organized as Promise. Kiara hosted all five on HOLOTALK (2023-08-12) within two weeks of their debut. [Observed S5 Kiara archive title]
- `bible/world/hololive--Advent.md › History`: | 2023-08-12 | Advent are Kiara's 29th HOLOTALK guests | First big senior collab |
- `bible/world/hololive--Advent.md › History`: | 2026-07-03/04 | Serendipity pairs: Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth, FUWAMOCO–Raora | [Official S7, S10] |

### from hololive -Justice-
- `bible/world/hololive--Justice.md › [SW] Description`: (2026); individual 3D showcases on August 1, 2, 8 and 9, 2025 (PDT) and a group 3D stream on August 16; their first in-person concert performance in 3D at the 2025 English concert; at the 2026 Serendipity concert the units Autofister (Gigi and Cecilia), Bloodraven (Elizabeth and Nerissa) and B.F.F (Raora and FUWAMOCO), with Elizabeth also singing alongside Kobo Kanaeru and Hakos Baelz, Cecilia alongside Vestia Zeta and Shiori and alongside Tsunomaki Watame and Calli, Gigi with Zeta and FUWAMOCO, and Raora with Watame and Kiara; and the second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive--Justice.md › History`: | 2026-07-03/04 PDT | Serendipity: day 1 "SUPERNOVA SUPER GIRL" (Justice); Autofister (Gigi & Cecilia, "CCGG MADNESS"); "HELP!!" (Kobo Kanaeru with Bae and Elizabeth); "Break It Down" (Vestia Zeta with Shiori and Cecilia); "Cloudy Sheep" (Tsunomaki Watame with Calli and Cecilia). Day 2: the Advent+Justice medley ("Rebellion," "ABOVE BELOW"); Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"); "MAKE IT, BREAK IT" (Zeta, FUWAMOCO and Gigi); "What an amazing swing" (Watame with Kiara and Raora); B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari") | [Official S6, S8] |

### from hololive -Myth-
- `bible/world/hololive--Myth.md › [SW] Other Names`: Myth, holoMyth, HoloMyth, hololive -Myth-, hololive English first generation
- `bible/world/hololive--Myth.md › [SW] Description`: At the September 2026 baseline, Calli, Kiara and Ina are active members of hololive -Myth-; Ame is an affiliate and Gura is a graduate.
- `bible/world/hololive--Myth.md › [SW] Description`: All five belong to Myth's shared history. hololive's first English generation debuted 12–13 September 2020: Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Gawr Gura and Watson Amelia.
- `bible/world/hololive--Myth.md › [SW] Description`: Calli wrote the lyrics for their first song and often plays the grumbling big sister; Kiara cheers loudest and hosts; Ina, the calm one, designed the Myth mascots except Bloop; Ame is often the gremlin and tech helper; Gura is the goofy little shark.
- `bible/world/hololive--Myth.md › [SW] Description`: On 2026-09-19 Calli, Kiara and Ina held the 6th Anniversary 3D LIVE "Seasons From Within."
- `bible/world/hololive--Myth.md › [SW] Rules`: At the 2026 baseline Calli, Kiara and Ina are the active members; Ame can appear as an affiliate guest; Gura appears as a memory or callback, never as a current streamer.
- `bible/world/hololive--Myth.md › Members and Status`: - Mori Calliope, Takanashi Kiara, Ninomae Ina'nis: active in hololive -Myth-.
- `bible/world/hololive--Myth.md › Members and Status`: - Watson Amelia: concluded general activities 2024-09-30; affiliate; guests at genmates' events (Kiara's concerts 2025 and 2026, Kronii's 2026 live, a 2026 "call from 2021" in Calli's charity stream). [Observed Ame file A23; Ame's wiki page §2025–§2026, secondary]
- `bible/world/hololive--Myth.md › How the Group Works`: - **Roles that formed early:** Calli wrote the lyrics for Myth's first song "Myth or Treat" (2021) and often plays the grumbling big sister; Kiara is the loudest cheerleader and the one who hosts; Ina is the calm one who designed the Myth mascots (all except Bloop) and draws for the group; Ame is the gremlin and the tech helper; Gura is the goofy little shark everyone protects. [Observed wiki pages, secondary; Adaptation for "big sister / little shark" shorthand]
- `bible/world/hololive--Myth.md › How the Group Works`: - **Group humor:** mutual teasing, jinxes, chaotic Minecraft and party games; name-order trivia (Calli and Ame say their names in English order; Kiara, Ina and Gura surname-first). [Observed S2]
- `bible/world/hololive--Myth.md › History`: | 2020-09-12/13 | Myth debuts; Calli narrates Kiara's debut intro | Kiara's intro art, Calli's narration |
- `bible/world/hololive--Myth.md › History`: | 2025-04-30 | Myth relay "one last time" with Calli, Kiara, Ina and Gura before Gura's graduation | Gura's farewell with Myth |
- `bible/world/hololive--Myth.md › History`: | 2025-09-13 | 5th anniversary collab with announcements (Calli, Kiara, Ina) | New anniversary hats |
- `bible/world/hololive--Myth.md › History`: | 2026-02 | Kiara's album includes "Blue & Gold," a tribute to Gura and Ame | Remembering the two |
- `bible/world/hololive--Myth.md › History`: | 2026-09-19 (announced) | Myth 6th Anniversary 3D LIVE "Seasons From Within" announced with Calli, Kiara and Ina (S3, an official hololive English post); not verified as held | The current three, as announced |

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: (June); EN's 4th concert "Serendipity" in Los Angeles (July), built on units such as Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS, Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 EDT | World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 | — |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-11 | Raora's friendly-fire "Doom" spell in Kiara's Mage Arena collab becomes a widely shared fan meme (KYM dates the stream 11-16) | a callback |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-03-27/28 PDT | Kiara and Ina's duo concert "Drawn to Dawn" (Los Angeles) | TakoTori on stage |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-07-03/04 PDT | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) | The current partnerships |

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › [SW] Description`: "Link Your Wish" in Makuhari (03-20; Kiara: "MAKUHARI WAS ON FIRE!"), HOLOSTARS adds the unit UPROAR!! and the English group -TEMPUS-, holoMeet starts with Gura as ambassador, Calli holds her first solo concert (07-21), and Sana graduates (07-31).
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019 | 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins | Kiara's oshi Pekora; Nerissa's oshi Marine; Calli's starstruck senpai Suisei |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-09-12/13 | **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame | The cast's origin |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-12-10 | Kiara's channel briefly terminated, then restored ("#PhoenixDown") | A Kiara rebirth joke |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2021-05-30 | Kiara reaches 1 million: every Myth member is over 1 million | A Myth first |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-03 | ID gen 3 (Zeta, Kaela, Kobo) | Kobo's "Mommy Kiwawa" and "Uncle Dad" |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-03-20 | hololive 3rd fes. "Link Your Wish" at Makuhari (#つながるホロライブ), day 2: Calli and Kiara perform | Calli: "My dream came true, my heart is exploding." Kiara: "MAKUHARI WAS ON FIRE!" [Observed—X posts, S4] |

### from hololive
- `bible/world/hololive.md › [SW] Description`: (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-.
- `bible/world/hololive.md › How It Works`: - **Structure (as of 2026-09-30):** hololive production is COVER's brand, which also includes the male group HOLOSTARS; hololive is its female VTuber group. On 2026-09-07 COVER unified the former female-talent branches (hololive, hololive English, hololive Indonesia, hololive DEV_IS) under a single "hololive," an organizational and branding change it described as removing regional limits; members had already collaborated across branches for years; former groups keep their names as units (hololive -Myth-, -Promise-, -Advent-, -Justice-). Promotion is now done for all members in Japanese, Indonesian and English. [Official S6] [Observed S2 §2026, secondary, citing the hololive Next broadcast of 2026-09-07; project.md]
- `bible/world/hololive.md › How It Works`: - **Seniority:** senpai and kouhai describe relative seniority (who debuted first), not language or nationality; forms of address and levels of formality vary by relationship. Many EN members are openly starstruck by particular senpai (Calli by Suisei, Kiara by Pekora). [Observed character files]

# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: myth2
Packet: projects/holoen/research/qa/packets/myth2.md (owned material) and projects/holoen/research/qa/packets/myth2-incoming.md (incoming claims); both are inline below
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
 "cast": [
  {
   "name": "Gawr Gura",
   "file": "bible/characters/Gawr-Gura.md",
   "other_names": [
    "Gura",
    "Gooba",
    "Goob",
    "Goobidiba",
    "Same-chan",
    "Samegaki",
    "City Pop Shark",
    "がうる・ぐら"
   ],
   "groups": [
    "hololive -Myth- (graduated)",
    "hololive alum",
    "Myth",
    "hololive English (former branch name)"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. Gura is a VTuber and a hololive alum: she graduated from hololive -Myth- on May 1, 2025.",
   "status_interval": {
    "state_at_baseline": "graduated",
    "debut": null,
    "graduated": "2025-05-01",
    "regular_activities_concluded": null,
    "source": "bible/characters/Gawr-Gura.md › Background"
   }
  },
  {
   "name": "Watson Amelia",
   "file": "bible/characters/Watson-Amelia.md",
   "other_names": [
    "Ame",
    "Amelia",
    "Amelia Watson",
    "Amechan",
    "Gremlin Ame",
    "ワトソン・アメリア"
   ],
   "groups": [
    "hololive (affiliate)",
    "hololive -Myth- (affiliate)",
    "Myth",
    "hololive English (former branch name)"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. Ame is a VTuber and a hololive affiliate: she concluded her regular activities on September 30, 2024, and appears at individually announced events.",
   "status_interval": {
    "state_at_baseline": "affiliate",
    "debut": null,
    "graduated": null,
    "regular_activities_concluded": "2024-09-30",
    "source": "bible/characters/Watson-Amelia.md › Background"
   }
  }
 ],
 "world": [
  {
   "name": "AmeSame",
   "file": "bible/world/AmeSame.md",
   "role": "Relationship",
   "other_names": [
    "Ame and Gura",
    "Gura and Ame",
    "The Fish Tank",
    "amesame"
   ]
  },
  {
   "name": "Bone Bros",
   "file": "bible/world/Bone-Bros.md",
   "role": "Relationship",
   "other_names": [
    "Calli and Gura",
    "Gura and Calli"
   ]
  },
  {
   "name": "hololive -Myth-",
   "file": "bible/world/hololive--Myth.md",
   "role": "Faction",
   "other_names": [
    "Myth",
    "holoMyth",
    "HoloMyth",
    "hololive -Myth-",
    "hololive English first generation"
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
  }
 ]
}
```

### projects/holoen/research/qa/packets/myth2.md

# Audit packet: myth2

Snapshot: git c06ffa3. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Gawr-Gura.md` 7c0664d13e30; `bible/characters/Watson-Amelia.md` 6f5acefd0577; `bible/world/hololive--Myth.md` e102fb95cdc7; `bible/world/AmeSame.md` 03602b5cf2fd; `bible/world/Bone-Bros.md` 3456a63d5263

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Gawr Gura — `bible/characters/Gawr-Gura.md`
**[SW] Groups:** hololive -Myth- (graduated), hololive alum, Myth, hololive English (former branch name)
**[SW] Other Names:** Gura, Gooba, Goob, Goobidiba, Same-chan, Samegaki, City Pop Shark, がうる・ぐら
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. Gura is a VTuber and a hololive alum: she graduated from hololive -Myth- on May 1, 2025. Her lore, which she played for laughs, is a persona, not literal: a descendant of the Lost City of Atlantis who swam to land because it was "so boring down there," bought her clothes and shark hat in the human world, and talks to marine life. Her age jokes put her in the 9,000s, with a different number from one telling to the next. She keeps a long-time friend, Bloop, sealed in a bubble "for the better" and calls him her emergency rations. She debuted in hololive English -Myth- in September 2020, twelve minutes late, opening with a single "a" that became a meme, and won fans by singing city pop. Her fans are the chumbuds and her members are shrimps. She hosted The Fish Tank with Watson Amelia and sang "Q" with Mori Calliope. She said goodbye with a small concert and a reminder to keep swimming.
**[SW] Relationships:** Watson Amelia (affiliate): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; they argue on purpose and prank each other, Ame's sudden praise embarrasses her, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert." Ninomae Ina'nis: they took part together in UMISEA in 2021; Ina drew a chibi Bloop and joked that anyone making Gura cry would face "the wrath of Ina." Takanashi Kiara: calls her "Goobidiba" and taught her Japanese and German, swears included; Gura once filled Kiara's KFP back room with chickens, and was her HOLOTALK guest the day before she graduated. Ouro Kronii: SNOTCast bits, and one of her regular partners in her last months. Murasaki Shion: senpai she wrote a mock love letter to. Sakura Miko: calls her "George." Ceres Fauna: a Council kouhai whose oshi was Gura; they raced in Dark Souls and drew hololive members from memory together days before Fauna graduated. Nanashi Mumei: a Council kouhai (#gumei); they did a "ROOM REVIEW" together in Mumei's last week. Shiori Novella and Nerissa Ravencroft: her "Scarlet Wand" guildmates in the ENigmatic Recollection story. Cecilia Immergreen: Keep Talking and Nobody Explodes and The Forest (2025). Raora Panthera: R.E.P.O. with Kiara and Kronii (2025).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | Descendant of Atlantis (now ruins); swam to land because it was "so boring down there"; bought her clothes at a beachside store, paying in seashells; talks to marine life | [Official G1] [Observed G2 §Lore] |
| Lore | Age jokes put her "somewhere in the 9,000s," with varying numbers across exchanges (9,361, 9,927, 9,485…); no fixed age is adopted. June 20 marks her arrival on land, not a remembered birthday | [Observed G2 §Gura's age and §Lore] |
| 2020-09-13 JST | Debuts in hololive English -Myth-, 12 minutes late, first word "a"; sings city pop and becomes "City Pop Shark" | [Official G1] [Observed G2 §Miscellaneous; G4] |
| 2020-12 / 2021-03 | Japanese and German lessons with Kiara | [Observed G13] |
| 2021-05 | The Fish Tank talk show with Ame | [Observed G6] |
| 2021-06-22 | Original song "REFLECT" | [Observed G2 §2021; G4] |
| 2022-02-03 | "Q" with Mori Calliope (DECO*27) | [Official G15] |
| 2024-09 | "2.0" model update | [Observed G3] |
| 2025-05-01 | Graduates; final 3D mini live; last post "keep swimming! always! 💙" | [Official G5] [Observed G3, G2] |
| 2026-09-30 | Alum; her history stays part of Myth's shared memory | [Adaptation] |
**Dossier · Hard Facts (continuity):**
- Birthday June 20; height 141 cm; debut 2020-09-13 JST; graduated 2025-05-01 JST; illustrator Amashiro
  Natsuki. [Official G1, G5] [Observed G2]
- Fans: chumbuds; members: shrimps; hashtags #gawrgura (streams), #gawrt (fan art); mark 🔱. [Official G1]
  [Observed G2 §Mascots and fans]
- Japanese name がうる・ぐら; gives her name surname-first ("Gawr Gura") even in English. [Official G1]
- Nicknames: Same-chan, City Pop Shark, Samegaki, Gooba, Goob, Goobidiba (by Kiara), George (by Miko).
  "Goomba" and "Apex Predator" are left out of Other Names because they would match unrelated text.
  [Observed G2 infobox]
- Likes: salmon, pizza, fast food, strawberry cake, rhythm games, cowboy and wild-west things, the banjo.
  Dislikes: hot sand, wearing pants. [Observed G2 §Likes and dislikes] (The wiki also reports her saying
  that her biggest fear is people hearing her stomach noises: one public quip, not a fear hierarchy, and
  not a continuity fact.)

### Watson Amelia — `bible/characters/Watson-Amelia.md`
**[SW] Groups:** hololive (affiliate), hololive -Myth- (affiliate), Myth, hololive English (former branch name)
**[SW] Other Names:** Ame, Amelia, Amelia Watson, Amechan, Gremlin Ame, ワトソン・アメリア
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. Ame is a VTuber and a hololive affiliate: she concluded her regular activities on September 30, 2024, and appears at individually announced events. Her lore, a persona she plays for laughs, makes her a time-traveling detective with a pocket watch that lets her travel through time. After hearing rumors about the unusual beings in hololive, she became an idol just out of interest, training her reflexes with shooters and her mind with puzzle games. She debuted in hololive English -Myth- in September 2020, briefly undercover with a fake British accent, and her fans are the Teamates. Her mascot is Bubba, her dog mascot. She built her own 3D and VR setups for her genmates, came up with and co-managed the ChikuTaku rhythm game, and hosted a charity stream. She was a guest at Kronii's 3D birthday live in March 2026.
**[SW] Relationships:** Gawr Gura (graduated): a close Myth friend and frequent early collaborator (AmeSame) and Fish Tank co-host; the two prank each other, Ame teases her with lewd-adjacent quips, and their last duo stream before Ame stepped back was "Looking at our old DMs" (2024). Mori Calliope: Myth genmate and Clubhouse 51 opponent. Ninomae Ina'nis: Myth colleague and gaming partner who designed Bubba; Ame can aim blunt competitive taunts at her. Takanashi Kiara: calls Ame her EN oshi ("#1 Ame gosling") and credits her help with 3D productions; Ame guests at Kiara's concerts and says Kiara once practically tackled her with a hug. Ouro Kronii: her "Time Duo" counterpart; Ame jokes she "borrowed" time travel from the Warden and swears she'll give it back, says Kronii dislikes everything she likes, and guested at Kronii's 2026 birthday live. Haachama and Roboco-senpai: Japanese seniors from early collabs. Nanashi Mumei (graduated 2025): Overwatch and VR field trips, and "ANIMALS with Ame & Moom" in Ame's last regular week. FUWAMOCO: "Detective Dogs" (Escape Simulator, 2024: "blondes can solve any puzzle"). Shiori Novella: a VRChat aquarium visit with "Ame Senpai" (2024). Koseki Bijou: Overwatch and Apex (2023). Gigi Murin: in the ENigmatic Recollection role-play story Gigi's knight Gonathon married Ame's Jyonathan ("ClueChaser," a secondary pair name). Cecilia Immergreen and Gigi: Borderlands 2 with Mumei (2024).
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore (secondary-reported; original statements and continuity scope unverified; outside the baseline) | Born circa the early 1920s and thrown forward in time; the pocket watch holds a time crystal; time travel makes loud screeching noises and can cause headaches; she won't use it to cheat | [Observed A2 §Time travel, secondary] |
| Lore | Became an idol "just out of interest" after rumors of unusual beings in hololive; trains reflexes with shooters and her mind with puzzle games | [Official A1] |
| 2020-09-13 JST | Debuts in hololive English -Myth- ("The Investigation Begins"), briefly undercover with a fake British accent | [Official A1] [Observed A3-MXrFrkIlE-0; A2 §Miscellaneous] |
| 2020-09-16 | Reveals she is a time traveler (first Fall Guys stream) | [Observed A2 §Time travel; A10 locator] |
| 2020-09-28 | "Nothing beats a ground pound" (Super Mario Odyssey) | [Observed A5] |
| 2020-12 | Repeated Sun Station landing attempts in Outer Wilds, later her favorite game | [Observed A9; A2 §Likes and dislikes] |
| 2021-04-01 | Smol Ame appears (April Fools) | [Observed A2 §Smol Ame] |
| 2021-05 | The Fish Tank talk show with Gura | [Observed Gura file G6] |
| 2023-01-19 | ChikuTaku song on sale | [Official A13b] |
| 2023-01-24 | ChikuTaku game released (concept and shared project management, with a credited team) | [Official A13] |
| 2024-09-30 | Concludes regular activities; remains a hololive affiliate | [Official A4] |
| 2026-03 | Guest spot at Kronii's 3D birthday live | [Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711] |
| 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |
**Dossier · Hard Facts (continuity):**
- Birthday January 6 (Sherlock Holmes's speculative birthday); height 150 cm; debut 2020-09-13 JST;
  status: hololive affiliate since 2024-09-30. [Official A1, A4] [Observed A2 §Miscellaneous]
- Fans: Teamates; members: Investigators / Investamigators / Investamigatorators; mascot Bubba; emoji 🔎.
  [Official A1] [Observed A2 §Mascots and fans]
- Alternate personas (excluded from name matching unless a story uses them): Smol Ame, Armando Watson,
  Jyonathan Watson, Bee Ame. [Observed A2 infobox and §Smol Ame]
- Excluded on purpose: real-person details (pets behind the mascot, family, health, ancestry) that the
  wiki mentions.

### hololive -Myth- — `bible/world/hololive--Myth.md`
**[SW] Other Names:** Myth, holoMyth, HoloMyth, hololive -Myth-, hololive English first generation
**[SW] Description:** At the September 2026 baseline, Calli, Kiara and Ina are active members of hololive -Myth-; Ame is an affiliate and Gura is a graduate. All five belong to Myth's shared history. hololive's first English generation debuted 12–13 September 2020: Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Gawr Gura and Watson Amelia. They grew up on stream together: a chaotic first year of near-daily collabs, then a bond built around songs, anniversaries, relays and concerts. Calli wrote the lyrics for their first song and often plays the grumbling big sister; Kiara cheers loudest and hosts; Ina, the calm one, designed the Myth mascots except Bloop; Ame is often the gremlin and tech helper; Gura is the goofy little shark. Ame concluded her regular activities on 2024-09-30 and still guests at events; Gura graduated on 2025-05-01 after a last Myth relay "one last time." On 2026-09-19 Calli, Kiara and Ina held the 6th Anniversary 3D LIVE "Seasons From Within."
**[SW] Rules:** At the 2026 baseline Calli, Kiara and Ina are the active members; Ame can appear as an affiliate guest; Gura appears as a memory or callback, never as a current streamer. Early Myth (2020–21) was collab-heavy. Membership status says nothing about how often they talk privately. The gremlin, tech-helper and cheerleader roles are flexible comic roles, not fixed.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2020-09-12/13 | Myth debuts; Calli narrates Kiara's debut intro | Kiara's intro art, Calli's narration |
| 2020–2021 | Near-constant collabs: Minecraft, Among Us, games across time zones | The "first year" memories |
| 2021-10-31 | "Myth or Treat" (lyrics by Calli) | First group song |
| 2022-06-28 | First off-collab with all five together ("Together At Last") | A treasured in-person memory |
| 2022-09-30 | "Non-Fiction" MV | Group song |
| 2023-09-13 | 3rd anniversary relay (#Myth3YearRelay), e.g. a homemade Family Feud with all five | Anniversary relays |
| 2024-06 | Myth One-Block Minecraft series | A recent full-group project |
| 2024-09 | 4th anniversary song and voice pack; Ame's last week includes a Myth collab | Ame's farewell to regular streaming |
| 2025-04-30 | Myth relay "one last time" with Calli, Kiara, Ina and Gura before Gura's graduation | Gura's farewell with Myth |
| 2025-07 | MYTHMASH: each active member releases a duet with a Japanese senpai (#mythmashchemythtry) | Cross-branch songs |
| 2025-09-13 | 5th anniversary collab with announcements (Calli, Kiara, Ina) | New anniversary hats |
| 2026-02 | Kiara's album includes "Blue & Gold," a tribute to Gura and Ame | Remembering the two |
| 2026-09-19 (announced) | Myth 6th Anniversary 3D LIVE "Seasons From Within" announced with Calli, Kiara and Ina (S3, an official hololive English post); not verified as held | The current three, as announced |
**Dossier · Hard Facts (continuity):**
- Debut 12–13 September 2020; Ame affiliate 2024-09-30; Gura graduated 2025-05-01.
- 2026 baseline: three active; Ame appears as a guest; Gura is remembered, not written as streaming.
- No reasons for Ame's or Gura's changes beyond the public status.

### AmeSame — `bible/world/AmeSame.md`
**[SW] Other Names:** Ame and Gura, Gura and Ame, The Fish Tank, amesame
**[SW] Description:** Watson Amelia and Gawr Gura, Myth's gremlin and Myth's shark, close Myth friends and frequent early collaborators. They hosted The Fish Tank, a talk show built on staged arguments, and pranked each other endlessly (Ame's Minecraft mine "Gura's Backdoor"; Ame killing Gura in Among Us right after Gura said "Not me, right?"). The sweet side showed too: Gura rewrote "You Are My Sunshine" about Amelia, picked "Watson" as the family name she'd take, and got flustered whenever a staged argument turned into real praise. On 2024-09-29, the day before Ame concluded her regular activities, they streamed "Looking at our old DMs" together. Gura graduated on 2025-05-01. At the 2026 baseline Ame is an affiliate and Gura has graduated; their shared history lives on in callbacks, their gold-and-blue colors, and Kiara's tribute song "Blue & Gold."
**[SW] Rules:** At the 2026-09-30 baseline, Ame is an affiliate and Gura has graduated. Their shared streaming history supplies callbacks and memories; graduation does not establish anything about their subsequent private contact. Stories set before October 2024 can use them together freely. Teasing can be crude and relentless, and Gura has become flustered when Ame turns teasing into praise. The ship name is a fan term, not romance.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2020 | Constant collabs and pranks | The "AmeSame" name |
| 2021-05 | The Fish Tank talk show | Staged-argument comedy |
| 2022-06 | An off-collab; unarchived karaoke | — |
| 2024-09-29 | "Looking at our old DMs" | Their last duo stream before Ame stepped back |
| 2025-05-01 | Gura graduates | — |
| 2026-02 | Kiara's "Blue & Gold" tribute | The colors as a memory |
**Dossier · Hard Facts (continuity):**
- Last duo stream before Ame stepped back: "Looking at our old DMs" (2024-09-29).
- 2026 baseline: Ame is an affiliate and Gura has graduated; their history supplies callbacks and
  memories. Graduation establishes nothing about their private contact.
- The ship name is a fan term; no romance is written.

### Bone Bros — `bible/world/Bone-Bros.md`
**[SW] Other Names:** Calli and Gura, Gura and Calli
**[SW] Description:** Mori Calliope and Gawr Gura, the reaper and the shark: a bickering duo of pranks and jabs, where Calli's gruff big-sister threats bounce off Gura's cheerful dumb-shark defiance. They were the English branch's first two to reach a million subscribers, were named Tokyo Tourism Ambassadors together (2023) and sang "Q" with DECO*27 (2022). Their collabs thinned out over the years, but on the Myth relay before Gura's graduation Calli's stream was "One Last Minecraft Trip." Gura graduated on 2025-05-01. Her single "Full Color" was never released; Calli performed it at Myth's fourth-anniversary concert "The Show Goes On!" (2024) and, with Kiara, said she would keep singing it.
**[SW] Rules:** At the 2026 baseline Gura has graduated; Bone Bros lives in memories, the "Q" duet and "Full Color." Before May 2025 they can prank and bicker freely. Calli's affection tends to show through teasing and actions more than speeches.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2020–2021 | Constant collabs, pranks and bickering | "Bone Bros" |
| 2022-02-03 | "Q" (with DECO*27) | Their duet |
| 2024-09 | Calli performs Gura's "Full Color" at Myth's 4th-anniversary concert "The Show Goes On!" | Carrying her song |
| 2025-04-30 | "One Last Minecraft Trip." (Myth relay) | Last duo moments on stream |
| 2025-05-01 | Gura graduates | — |
**Dossier · Hard Facts (continuity):**
- "Q" duet: 2022-02-03. Gura graduated 2025-05-01.
- 2026 baseline: Gura has graduated; Calli performed "Full Color" in 2024 and said she would keep singing it.

Incoming claims continue in `myth2-incoming.md`.

### projects/holoen/research/qa/packets/myth2-incoming.md

# Audit packet: myth2 (incoming claims)

Snapshot: git c06ffa3.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: lolive English first generation|hololive -Myth-|Calli and Gura|Gura and Calli|City Pop Shark|Amelia Watson|Watson Amelia|The Fish Tank|Ame and Gura|Gura and Ame|Gremlin Ame|ワトソン・アメリア|Goobidiba|Gawr Gura|Same-chan|Bone Bros|holoMyth|HoloMyth|Samegaki|AmeSame|amesame|Amechan|Amelia|がうる・ぐら|Gooba|Myth|Gura|Goob|Ame)(

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Gawr Gura: Keep Talking and Nobody Explodes, The Forest.
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Gawr Gura, IRyS, Hakos Baelz | Seniors | Keep Talking and Nobody Explodes and The Forest with Gura (2025); Elden Ring Nightreign with IRyS and Bijou (2025); "BratTea" with Bae (secondary) | [Observed CI2, CI3] |

### from Ceres Fauna
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: Gawr Gura: Fauna's hololive oshi; Mario Kart, a Dark Souls race, and drawing hololive members from memory four days before Fauna graduated.
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: Takanashi Kiara: Myth senior; "KIWAWA vs FAWNA"
- `bible/characters/Ceres-Fauna.md › Relationship Map`: | Gawr Gura | Her hololive oshi | Mario Kart ("GOOWA FWANA RACING"), a Dark Souls race (2024), and "Drawing Hololive Members From Memory with @GawrGura!" (2024-12-30) | [Observed F2 §Likes; F3] |
- `bible/characters/Ceres-Fauna.md › Relationship Map`: | Takanashi Kiara | Myth senior | "KIWAWA vs FAWNA" (Clubhouse 51, 2022); Minecraft Wither fight; Kiara's HOLOTALK 32nd guest (2024-12-27) | [Observed F3; Kiara archive] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Takanashi Kiara | Myth senior ("Eternal Flame," "11 ERBs and Spices") | Kiara calls her "Erby Berby"; Minecraft (2025); Kiara's Mage Arena collab (2025) | [Observed EB2, EB3] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Mori Calliope | Myth senior | A TakaMori impression at debut (secondary); the LYRA cover of "III" with Amane Kanata, Koganei Niko, Calli and Ayunda Risu; "START AGAIN" on stage; "Jade Sword" guild in ENReco | [Observed EB2, secondary] [Official EB5] [EB9] |

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Watson Amelia: "Detective Dogs."
- `bible/characters/Fuwawa-Abyssgard.md › Behavioral Traits`: 2. She is poor at spelling and math, careless, and often clumsy at games, and bad at telling left from right (like Gura). [Observed FW2 §Personality, §Miscellaneous, secondary]

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Watson Amelia: knights in a fictional ENReco marriage storyline.
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Watson Amelia | Affiliate senior ("ClueChaser," secondary) | In ENReco, Gigi and Ame played knights in a fictional marriage storyline (character-name variants unverified: Gonathon/Jyonathan, "Jyon Watson") | [Observed GG2, secondary] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Takanashi Kiara: her 2026 Serendipity partner ("Rocku Wawa"), who calls her a "hidden gem" and encouraged her through hard choreography for a song with Kiara and Ame; Bijou admires Kiara's "confidence," and they keep saying "67."
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Watson Amelia: Overwatch and Apex (2023).
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Takanashi Kiara | Senior; Serendipity 2026 duo ("Rocku Wawa") | BG3 (2023); Kiara once asked her to perform a song with her and Ame; in the official interview Kiara calls her a "hidden gem" with "so much charm," and Bijou admires Kiara's "confidence"; their shared joke is "67" | [Official KB4] [Observed KB3; Kiara archive] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Watson Amelia | Senior | Overwatch and Apex collabs (2023) | [Observed KB3 7MtuoPeC4tE; Ame archive] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Watson Amelia: "Detective Dogs."

### from Mori Calliope
- `bible/characters/Mori-Calliope.md › [SW] Groups`: hololive, hololive -Myth-, Myth, CHADCast, hololive English (former branch name), Last Writes
- `bible/characters/Mori-Calliope.md › [SW] Background`: She debuted first in hololive -Myth- in September 2020; her fans are the Dead Beats, her mentor is Death Sensei, her publicly depicted cat mascot is Tutu, and her scythe is named Ricky.
- `bible/characters/Mori-Calliope.md › [SW] Background`: Myth still includes Takanashi Kiara and Ninomae Ina'nis; Gawr Gura has graduated, and Watson Amelia is an affiliate.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!"
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream.
- `bible/characters/Mori-Calliope.md › Voice Profile`: - Measured (C30, chat windows): median pitch 197–214 Hz, the second lowest of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz). The wiki's hololive-wide ranking was not measured. She is the fastest talker of the six: about 161–186 words per minute of speech while chatting (Kronii 120–127, Ina 81–95). Approximate values for relative comparison.
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2026-09-07 | The branches merge into one "hololive." Her unit is now hololive -Myth-. | [Official C17, C1] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Takanashi Kiara | Myth genmate | Calli calls her "kusotori" ("shitty bird") and usually rebuffs her, while supporting "TakaMori." They play "Mom" and "Dad" to Kobo. | [Observed C7; C25 §Takamori, secondary] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate | Ina designed Death Sensei. Calli wrote the lyrics for Ina's TAKO∞TAKOVER. [Unverified, title only: a running bit of a shinigami afraid of a tako] | [Observed C4 §Mascot and fans, secondary] [Official C28] [C21-eRObYMLdPfw clip title] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate | "Bone Bros." The "Dad" joke started around Gura. They sang "Q" together (2022). | [Observed C4 §Relationships, secondary] [Official C29] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Watson Amelia (affiliate) | Myth genmate | [Unverified, title only: Ame pranking and scaring her, e.g. with a surprise "ara ara"] | [C21-a03HNAHiwpM clip title] |
- `bible/characters/Mori-Calliope.md › Hard Facts`: - Birthday April 4 (4/4: "shi" is also "death"). Height 167 cm. Debut 2020-09-12. Unit: hololive -Myth-. [Official C1] [Observed C4 §Miscellaneous, secondary]

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Gawr Gura: a "#gumei" voice challenge (2023) and a "ROOM REVIEW" in Mumei's last week.
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Watson Amelia: Overwatch, VR field trips, and "ANIMALS" in Ame's last regular week.
- `bible/characters/Nanashi-Mumei.md › Voice Profile`: - **Macabre and grandiose humor:** a cute voice with dark content: drawings that turn Tim Burton-esque or demonic, cheerful reminders that everyone dies. [Observed M2 §Personality, secondary]. Bravado: "I've never been scared of anything ever." [ASR M20, 0:26:39]. Ranking who she'd beat at arm wrestling: "I think I would win against Gura, Kiara, IRyS, Nerissa, and Mococo"; she moved Biboo to the losing side ("she is a rock") and concluded that most of EN could beat her: "But I have other skills and things that make me special, so whatever." [ASR M20, 0:23:52–0:27:44; the models disagree on the word "EN"]
- `bible/characters/Nanashi-Mumei.md › Background Timeline`: | 2024-08-05 | 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori | [Observed M3 title, description] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Takanashi Kiara | Myth senior; bird unit HOLOTORI | "BUILDER BIRBS" (2021); "Kiwawa & Mumeiwi" (2022); the 4th fes. holo*27 stage (2023); "two smol beans" (2025); HOLOTORI R.E.P.O. (2025-04-18); Kiara's HOLOTALK 33rd guest (2025-04-22); Kiara calls her "Moomsies" | [Observed M2 infobox; M3; M4] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Gawr Gura | Myth senior | "【VOICE CHALLENGE】in the same room? 💙🤎 #gumei" (Gura's channel, 2023); Overwatch; "ROOM REVIEW with @NanashiMumei" (2025-04-21) | [Observed M3; Gura channel] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Watson Amelia | Myth senior | Overwatch and VR field trips (2022); "ANIMALS with Ame & Moom" (2024-09-29, Ame's last regular week) | [Observed M3] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Ninomae Ina'nis | Myth senior, fellow artist | Drawing collabs (2023-01, 2025-04-21 "doodles with @NinomaeInanis") | [Observed M3] |
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Mori Calliope | Myth senior | "ANATOMY REVIEW" streams (with Calli and Sana, 2022; solo, 2025) | [Observed M3] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › Voice Profile`: - Measured (N20; a 2026 solo chat): median pitch about 214 Hz (p10–p90 172–297 Hz), a mid-range speaking voice like IRyS's (214–226 Hz), lower than Kiara or Gura; about 159 words per minute of speech. Group-stream windows read higher (284–289 Hz) because several voices share them. Sample results only.
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Watson Amelia | Senior (affiliate) | Portal 2 together, "TAKING ON PUZZLES WITH @WatsonAmelia" (2024) | [Observed N3 title] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Gawr Gura | Senior (graduated) | Guildmates ("Scarlet Wand") in the ENigmatic Recollection Minecraft story | [Observed N2 §Relationships] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Octo'clock
- `bible/characters/Ninomae-Inanis.md › [SW] Background`: She drew Myth's intro art and designed Takodachi, Bubba and Death Sensei.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Watson Amelia (affiliate): Ina designed Bubba and is the patient foil to Ame's salty gremlin.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Gawr Gura (graduated): fellow member of the ocean-themed unit UMISEA (2021); Ina promises "the wrath of Ina" to anyone who makes Gura cry.
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **How she addresses people:** "you guys," "everyone," "chat," and fans as "Takodachi" (the official fan name is the Tentacult). Members by first or short name ("Calli," "Kiara," "Ame," "Gura," "Kronii," "Bae," "Biboo," "CC"); a full name signals a mock-serious scold. New members are "kouhais." She gives her own name surname-first. [Official I1] [Observed I3 captions; I2 §Mascot and fans]
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - Measured (I29, 2026 chat): median pitch 223–232 Hz, in the middle of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz), so "mid" rather than "low"; about 81–95 words per minute of speech in that one 2026 chat stream (Kronii 120–127, Calli 161–186 in their chat windows). A 2021 game stream measures 210–214 Hz and 68–116 words per minute (its opening chat 116). Sample results only; they do not establish a general ranking among genmates.
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | Ongoing | Illustrator: drew Myth's intro art; designed the Takodachi [I2 §Mascot and fans], Bubba [Ame file A2 §Mascots and fans] and Death Sensei [Calli file C4 §Mascot and fans] (the wiki says all Myth mascots except Bloop); she drew chibi Bloop artwork, but Bloop's original design is not hers [Gura file G2] | [Observed I2 §Miscellaneous and §Mascot and fans, secondary] |
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026-09-07 | Branches merge; she is "Ninomae Ina'nis from hololive," unit hololive -Myth- | [Official I28] [Observed I10] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Takanashi Kiara | Myth genmate ("TakoTori," fan term) | Duo concert 2026; Kiara encouraged her dance work; Kiara groans at her puns; Kiara once "fired" her over the chicken incident; the wiki reports Kiara saying Ina is the first to message her when she's down (secondary, off the card) | [Official I20] [Observed I2 §Personality; Kiara file T2 §KFP] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Mori Calliope | Myth genmate | Favorite pun target ("Every freaking time, Ina."); Ina designed Death Sensei; Calli wrote the lyrics for TAKO∞TAKOVER | [Observed I8 captions; I2 §Miscellaneous] [Official I25] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Watson Amelia (affiliate) | Myth genmate | Ina designed Bubba; the patient foil to Ame's salty gremlin; "Ame... Ame is British." | [Observed I2 §Personality, §Miscellaneous and §Quotes] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate; fellow member of the official unit UMISEA (2021, with Minato Aqua and Houshou Marine; the wiki also lists Sakamata Chloe) [Official I31] | Ina says anyone who makes Gura cry will "face the wrath of Ina"; Ina drew chibi Bloop; a prank war is reported but [Unverified] | [Observed I2 §Relationships; Gura file G2 §Gura's antics and §Mascots and fans] |
- `bible/characters/Ninomae-Inanis.md › Hard Facts`: - Birthday May 20; height 157 cm; debut 2020-09-13; unit hololive -Myth-; illustrator Kuroboshi Kouhaku (whom she calls "papa"). [Official I1] [Observed I2 infobox]

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Gawr Gura (graduated): SNOTCast, and Kronii was one of Gura's regular partners in her last months.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Watson Amelia (affiliate): "Time Duo"; Ame jokes she "borrowed" time travel from the Warden, and she guested at Kronii's 2026 birthday live.
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Measured (K36, chat windows): median pitch 177–188 Hz, the lowest of the six files measured the same way (Calli 197–214 Hz; Gura and Ame about 250–270 Hz); about 120–127 words per minute of speech, mid-paced (Calli 161–186, Ina 81–95). Approximate values for relative comparison.
- `bible/characters/Ouro-Kronii.md › Background Timeline`: | 2026-03-13 | 3D birthday live; Watson Amelia guests | [Observed K33, secondary, stream t=1711] |
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Watson Amelia (affiliate) | Fellow EN ("Time Duo") | Guested at Kronii's 2026 3D birthday live | [Observed K8 §Relationships, K33, secondary] |
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Gawr Gura (graduated) | Fellow EN ("SNOTCast" with Fauna and Mumei) | A friendly rivalry and Gura's "CLOCK WOMAN" nickname are reported but [Unverified] | [Observed K8 §Relationships, secondary] |

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Takanashi Kiara | Myth senior ("HoloEU" with Cecilia; secondary) | An Italian lesson (2024), a proposed outfit for Kiara on her "Raora's Clawset" art stream (2025-01-26; not a released Kiara model), an EU-snacks off-collab (2025); the "Doom" meme in Kiara's collab; "What an amazing swing" with Watame at Serendipity (2026) | [Observed RP3, RP7] [Official RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Ninomae Ina'nis | Myth senior | Puyo Puyo Tetris 2 (2025); the Monster Hunter Wilds launch with Gigi and Bijou; "Neko Kaburi-Na" with Shiori and Oozora Subaru at -All for One- | [Observed RP3] [Official RP5] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Mori Calliope | Myth senior | Elden Ring Nightreign with Gigi (2025-06-11) | [Observed RP3 AnvhW-eFatE] |

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Watson Amelia: a VRChat aquarium visit with "Ame Senpai."
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Watson Amelia | Senior | "Ame Senpai's Aquarium Visit" in VRChat (2024-12-02) | [Observed SN3] |

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Rocku Wawa
- `bible/characters/Takanashi-Kiara.md › [SW] Background`: She debuted with hololive -Myth- in September 2020 speaking English, Japanese and German.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Ninomae Ina'nis: Myth genmate and duo-concert partner (TakoTori; Drawn to Dawn, 2026), the calm brake to Kiara's gas pedal; Kiara once "fired" her over a chicken incident.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Watson Amelia (affiliate): her EN oshi ("#1 Ame gosling"), who helped with her 3D productions and now guests at her concerts.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Gawr Gura (graduated): "Goobidiba"; Kiara taught her German and German swears, Gura once filled KFP's back room with chickens, and Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame.
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: - "You little shit!" → protest at a collaborator; her own short is titled "GURA YOU LITTLE SHIT." [Official T16, her upload] [Observed T2 §Quotes, secondary]
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: - **Profanity:** frequent and casual: "fuck," "fucking," "what the fuck," "holy shit," "shit," "ass," "damn it," "hell." The 2026 captions contain many masked "[ __ ]" tokens (unidentified censored words); the audio transcripts give the actual words in her own speech: "everybody is fucking good at making Miis," "Holy shit, they're all cracked," "It's like tiny in size, but it's so fucking heavy," "Damn. Damn!", and in DOOM "Vault dwellers? What the fuck is there? The wasteland?" and "16 of them. 16. What the fuck am I supposed to do with 16?" [ASR T23, -5P17BxVZTE 2:42:58, 2:43:03, 2:37:42, 1:08:57; gqQoOjKBmLw 1:36:06, 1:40:19; both models agree] She swears during games and stories and can aim playful insults at collaborators (her own "GURA YOU LITTLE SHIT", T16). On sponsored streams she holds back ("what the heck," "effing"). Rage can flip into German: "You fucking freak! Ihr seid doch alle Perverse! Unglaublich!" (at a game's German developers). She taught Gura German swears ("Scheiße," "Fick dich") in a lesson stream. [Observed T3; T2 §Quotes, secondary; T15]
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2021-03 | German lesson with Gura; the German "HoloDE Debüt" stream | [Observed T15; T2 §2021] |
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2026-09-07 | Branches merge; unit is hololive -Myth- | [Official T20, T1] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Mori Calliope | Myth genmate | Kiara long called Calli her "wife" and coined "TakaMori"; Calli rebuffed her and calls her "kusotori" ("shitbird"). They announced in 2021 that they would tone the ship down (the wiki adds that "the two remain close friends"; a secondary statement, not a documented current relationship); they play "Mom" and "Dad" to Kobo as a performed family bit | [Observed T2 §Takamori, secondary; T14 title] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate ("TakoTori") | Duo concert 2026; Kiara "fired" Ina over the 2020 chicken incident. Ina's wiki page reports that Ina is the first to message Kiara when she's down (a secondary account, not on the card) | [Official T11, T12] [Observed T2 §KFP; T22 §Personality, secondary] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Watson Amelia (affiliate) | Myth genmate | Kiara's EN oshi ("#1 Ame gosling"), credited for help with 3D productions; Ame made HOLOTALK intro material | [Observed T2 §Likes and dislikes] [Official T9] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate | German lessons where Kiara taught her German swears and rickrolled her; Gura's 2020 Minecraft prank filled KFP's back room with chickens; "GURA YOU LITTLE SHIT" | [Observed T15; T2 §Miscellaneous and §KFP] [Official T16] |
- `bible/characters/Takanashi-Kiara.md › Hard Facts`: - Birthday July 6; height 165 cm; debut 2020-09-12; unit hololive -Myth-; illustrator huke. [Official T1]

### from Advent Pairs
- `bible/world/Advent-Pairs.md › With Myth`: - **Takanashi Kiara:** hosted all five on HOLOTALK; an occult handcam off-collab with Shiori ("#shiotori," 2024-07-12); Baldur's Gate 3 with Bijou, Calli and Nerissa ("Killing, Two Birds, with One Stone," 2023); Bijou was her 2026 Serendipity partner ("Rocku Wawa," and a running "67" joke); Bijou recalls Kiara as "really encouraging and helpful" when Kiara asked her to perform a song with Kiara and Ame whose choreography was one of the hardest she had learned. [Official S4] [Observed S1]
- `bible/world/Advent-Pairs.md › With Myth`: - **Watson Amelia:** "Detective Dogs" with FUWAMOCO (Escape Simulator, 2024); Shiori's VRChat aquarium visit with her (2024). [Observed S1]
- `bible/world/Advent-Pairs.md › With Myth`: - **Gawr Gura (graduated):** fellow "Scarlet Wand" guildmate of Shiori and Nerissa in the ENigmatic Recollection story. [Observed S2 Shiori, secondary]

### from Concerts and Live Events
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: (2026); Kronii's "The Goddess Descends" birthday live with Ame as guest (March 2026); IRyS's "HOPE UPON A STAR" and "Racing Towards Hope" lives and her first solo concert, Tokyo, 2026-10-06; Nerissa's "Requiem for Love – A JukeBox Musical"
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); hololive night at Dodger Stadium with Ina, IRyS and Bijou (2025-07-05); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!"
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive fes. + hololive SUPER EXPO** (spring, in Japan; the combined fes./EXPO tradition dates to 2022, while fes. itself is older): the agency-wide concert and convention. 3rd fes "Link Your Wish" (2022-03, Makuhari; Calli and Kiara performed on day 2, per their X posts), 4th fes "Our Bright Parade" (2023), 5th "Capture the Moment" (2024), 6th "Color Rise Harmony" (2025-03-08/09; Nerissa on day 1), 7th "Ridin' on Dreams" (2026-03-06/08). EN units share Expo booths and key visuals (Myth with Promise, Advent with Justice). [Observed S1 §2023–§2026; S2]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous" [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **holoMeet** (since 2022): overseas fan events with yearly ambassadors (Gura 2022, IRyS 2023, Bae 2024, Bijou 2025, Gigi 2026). [Observed S1]
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Ouro Kronii | World Tour '24 Singapore pre-concert panel with Kaela Kovalskia; World Tour '25 Sydney guest; 3D birthday live "The Goddess Descends" with a new outfit (2026-03-13/14, Ame as guest); Serendipity with Ina | Kronii file K33, K4; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Gawr Gura | Final 3D mini live on her graduation day (2025-05-01) | Gura file G5 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Watson Amelia | As an affiliate: guest at Kronii's 2026 birthday live | Kronii file K33 |

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ina was in the ocean unit UMISEA (Aqua, Marine, Chloe, Gura; history now) and duets with Nekomata Okayu.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Gura had "Apex Predators" with Shishiro Botan and a duet cover with Murasaki Shion.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ame has "KoMeHa" with Kobo and Iroha.
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Ninomae Ina'nis:** an artist among artists: the ocean unit UMISEA (formed 2021 with Minato Aqua, Houshou Marine and Gura; Chloe joined later; Aqua and Gura have graduated and Chloe is an affiliate, so the unit is history more than a current lineup); "HoloJEI" (Tsunomaki Watame, Kureiji Ollie, Anya Melfissa); "TakoBazo" (Vestia Zeta); "TakoNeko" (Nekomata Okayu, with a 2025 Mythmash duet, "Kurukuru Cruise"); Shiranui Flare appeared on her 2025 AmiAmi special ("Flare?!!?"). She admires Marine as an artist. [Observed S1; S2 Ina; Ina file]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Gawr Gura** (graduated): "Apex Predators" (Shishiro Botan), UMISEA, "SharPea" (Pavolia Reine), and Murasaki Shion (Minecraft and Mario Kart in 2021; a "Renai Circulation" duet cover, 2022). [Observed S1; S2 Gura]
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Watson Amelia** (affiliate): "KoMeHa" (Kobo Kanaeru, Kazama Iroha), "ZetAme" (Vestia Zeta); outside hololive, "SelAMei" (with Mumei and Selen Tatsuki). [Observed S2 Ame]

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Myth and Promise:** "FUWAMOCALLI" with Mori Calliope (a twin game show and Smash in 2023, a tea party, an off-collab karaoke in 2024); Fuwawa also joined Mori Calliope and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"; Fuwawa's post, not a twin appearance); "Detective Dogs" with Watson Amelia (Escape Simulator, 2024-09-24); "WatchDog" with Ouro Kronii; "Fuwamoomco" with Nanashi Mumei (Overwatch, 2025-03-01); they helped Ceres Fauna on her last World Tree stream (2024-12-31); Kiara hosted them on HOLOTALK (2023). [Observed S1; S3; Mumei, Calli, Kiara archives]

### from Fauna and Mumei Pairs
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Other Names`: Fauna and Mumei, Mumei and Fauna, It's Not a Phase, KronMei, gumei, Fauna and Gura, Mumei and Kiara, Mumei and Kronii
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Gura was Fauna's oshi; they drew hololive members from memory four days before Fauna graduated, and Gura and Mumei did a "ROOM REVIEW" together in Mumei's last week.
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Mumei also drew with Ina, did "Anatomy Review" with Calli, played with Ame in Ame's last regular week, and held "emo hours" with Nerissa; at the 2024 concert Mumei sang with Kiara and Nerissa, and Fauna with Shiori and Nerissa.
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Gura:** Gura is Fauna's hololive oshi; Mario Kart ("GOOWA FWANA RACING," 2021), a Dark Souls race (2024) and "Drawing Hololive Members From Memory with @GawrGura!" (2024-12-30). Mumei and Gura: "【VOICE CHALLENGE】in the same room? 💙🤎 #gumei" (2023) and a "ROOM REVIEW" (2025-04-21). [Observed S2 §Likes; S1]
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Ame:** Mumei and Ame: Overwatch and a VR field trip (2022), "ANIMALS with Ame & Moom" (2024-09-29, in Ame's last regular week). [Observed S1]
- `bible/world/Fauna-and-Mumei-Pairs.md › History`: | 2025-04 | Mumei's farewell month: "Donut Hole" with Kronii (04-11), Overwatch with IRyS (04-22), HOLOTALK (04-22), a Korone duet cover (04-23), Promise R.E.P.O. (04-24), Gura's room review | — |
- `bible/world/Fauna-and-Mumei-Pairs.md › Conflicts and Story Hooks`: 4. (Before 2025) Fauna and Gura draw hololive members from memory and get every hairstyle wrong.
- `bible/world/Fauna-and-Mumei-Pairs.md › Hard Facts`: - Fauna's oshi: Gura. Kiara's name for Mumei: "Moomsies." HOLOTORI includes Kiara and Mumei.

### from IRyS and Nerissa Pairs
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Rules`: IRyS (2021) is Nerissa's senior; Myth are seniors to both.
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Rules`: Recent pairings (IRyS with Kronii, Calli and Ina; Nerissa with Kiara and Calli) carry the most weight; pairs with Gura are memories.
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Ame** (11 / 2 / 3 / 2 / 0 / 0) and **IRyS and Gura** (11 / 6 / 0 / 1 / 0 / 0): mostly the 2021–22 full-EN collabs (Among Us, Dead by Daylight, Overwatch); IRyS joined Ina, Bae and Ame's "LOSER BUYS DINNER!!!!!" off-collab (2023-02-23). With Gura graduated and Ame an affiliate, these are memories. [Observed S1 titles]
- `bible/world/IRyS-and-Nerissa-Pairs.md › Nerissa`: - **Nerissa and the others:** Ame: Portal 2, "TAKING ON PUZZLES WITH @WatsonAmelia" (2024-09-28). Gura: fellow guildmates ("Scarlet Wand") in ENigmatic Recollection, now a memory. Kronii: an Among Us group collab (2023-12) is the example found. [Observed S1 titles; S3 §Relationships, secondary]
- `bible/world/IRyS-and-Nerissa-Pairs.md › Hard Facts`: - 2026 baseline: IRyS–Gura and Nerissa–Gura are memories; Ame appears as an affiliate guest.

### from Justice Pairs
- `bible/world/Justice-Pairs.md › With Myth`: - **Gawr Gura (graduated):** Keep Talking and Nobody Explodes and The Forest with Cecilia (2025-02); R.E.P.O. with Raora, Kiara and Kronii (2025-04-13). **Watson Amelia (affiliate):** in ENReco's role-play story, Gigi's Gonathon and Ame's Jyonathan marry (secondary; "ClueChaser"); Borderlands 2 with Cecilia, Gigi and Mumei (2024-08-09). [Observed S1; S2]

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Other Names`: Kiara and Ame, Ame and Kiara, Kiara and Gura, Gura and Kiara, Calli and Ina, Ina and Calli, Calli and Ame, Ame and Calli, Ina and Ame, Ame and Ina, Ina and Gura, Gura and Ina, Kiara and Kronii, Kronii and Kiara, Gura and Kronii, Kronii and Gura
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: The rest of the web among the five Myth members and Kronii.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Kiara and Ame: Ame is Kiara's EN oshi ("#1 Ame gosling"); Ame made Kiara's HOLOTALK intro, was its guest in 2024 and now guests at Kiara's concerts; Ame on a reunion: "Kiara like, threw herself at me… she hugged me!"
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Kiara and Gura: Kiara calls Gura "Goobidiba" and taught her German and Japanese, swears included; Gura's Minecraft prank filled Kiara's KFP back room with chickens; Gura was HOLOTALK's 34th guest the day before she graduated.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Calli and Ame: early Clubhouse 51 duels; in 2026 Ame "called in from 2021" to Calli's charity stream.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Ina and Ame: Ina designed Bubba; they did a "loser buys dinner" off-collab.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Ina and Gura: the official ocean unit UMISEA (2021); Ina promised "the wrath of Ina" to anyone who makes Gura cry.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Gura and Kronii: fan unit SNOTCast; in Gura's last months Kronii was one of her regular partners ("I Play, She Watches (She's Scared)").
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Rules`: In the 2026 baseline, pairs with Gura are memories and callbacks, and pairs with Ame are guest appearances.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Rules`: Nicknames are used as each member uses them (Kiara's "Goobidiba,"
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Kiara and Ame** (20 / 26 / 30 / 8 / 9 / 1): Ame is Kiara's EN oshi; Kiara calls herself "#1 Ame gosling" and "#1 Teamate" and credits Ame for help with her 3D productions. Ame made the intro video for Kiara's talk show HOLOTALK (2020) and was its 31st guest (2024-09-22); they did a 3D off-collab "In Ame's awesome studio" (2023-06). Ame on a reunion: "Kiara like, threw herself at me… she hugged me!" Ame, now an affiliate, performed at Kiara's 2025 spring concert and guested at her 2026 birthday live. [Observed S2 Kiara §Likes and dislikes, §2020; S3 Ame §Quotes, §2025–§2026, secondary; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Kiara and Gura** (59 / 25 / 11 / 10 / 8 / 6): Kiara calls her "Goobidiba" and taught her German and Japanese, German swears included, tricking her into singing on lesson streams; Gura's 2020 Minecraft prank filled Kiara's KFP back room with chickens. Gura was HOLOTALK's 34th guest on 2025-04-30, the eve of her graduation ("three four," at last). Kiara's 2026 song "Blue & Gold" is a tribute to Gura and Ame. [Observed S2 §KFP, §Miscellaneous; S4 Gura §Gura's antics, secondary; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Calli and Ame** (24 / 23 / 14 / 6 / 6 / 0): early Clubhouse 51 duels; the MV of Calli-written "Myth or Treat" premiered on Ame's channel (2021); in 2026 Ame "called in from 2021" during Calli's charity stream. [Observed Ame file A20; S3 §2021, §2026, secondary; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Ina and Ame** (29 / 30 / 9 / 4 / 4 / 0): Ina designed Bubba; Ame's "Amenade" cocktail traces back to a Japanese snack tasting with Ina; a "LOSER BUYS DINNER!!!!!" off-collab (2023-02-23); Ame aims blunt PvP taunts at her. [Observed S3 §Miscellaneous; Ame file; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Ina and Gura** (71 / 28 / 10 / 3 / 3 / 2): fellow members of the official ocean unit UMISEA (September 2021); Ina drew chibi Bloop and promised "the wrath of Ina" to anyone who makes Gura cry; Gura once directed a lost Ina in Minecraft by hitting a block with her pickaxe. [Official UMISEA announcement; S4 §Gura's antics, secondary]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Gura and Kronii** (2021→2025: 9 / 11 / 3 / 2 / 5): the fan unit SNOTCast (Shark, Nature, Owl, Time); in 2025, Gura's last months, Kronii became one of her regular partners: Fast Food Simulator ("Legend Is Made Here With @GawrGura"), R.E.P.O., and "Greener Grass Awaits: I Play, She Watches (She's Scared)" (2025-04-26). [Observed S4 §Relationships, secondary; S1 Kronii titles]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2020-11-15 | Gura's chicken prank on KFP | KFP lore |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2024-09-22 | Ame on HOLOTALK | Kiara's oshi as guest |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2025-04-26/30 | Kronii's and Kiara's last collabs with Gura | Farewells |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Conflicts and Story Hooks`: 1. Kiara interviews her oshi Ame on HOLOTALK and can't keep a straight face.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Conflicts and Story Hooks`: 2. A German lesson where Gura only wants to learn swears.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Conflicts and Story Hooks`: 4. Kronii plays a horror game while Gura "watches (she's scared)."
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Hard Facts`: - Kiara's EN oshi: Ame. Kiara's names: "Goobidiba" (Gura), "quasoni" (Kronii).
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Hard Facts`: - 2026 baseline: pairs with Gura are memories; pairs with Ame are guest appearances.

### from Octo'Clock
- `bible/world/OctoClock.md › How It Works`: - **On stream (archive, S1):** Ina's FGO streams with Kronii (2023-08-18 "Let's Learn About Fate/Grand Order!!!", 2024-01-02 "NEW YEAR FGO ADVENTURES"), R.E.P.O. (2025-07-19), and Ame's 2022 surprise karaoke off-collab that both joined (per Ame's wiki page).
- `bible/world/OctoClock.md › History`: | 2022-02-25 | Ame's surprise karaoke off-collab (with Ina, Kronii, Fauna, Mumei) | — |

### from Streaming Life
- `bible/world/Streaming-Life.md › How It Works`: - **Collab:** a joint broadcast or project; it may be remote or in person and may have one or several channel perspectives ("POV"). **Off-collab:** an in-person collaboration. **3D:** full-body avatar streams, lives and concerts. **Relay:** members stream one after another under a shared hashtag (e.g. the 2025 Myth relay). [Observed S1 titles]
- `bible/world/Streaming-Life.md › History`: | 2020 | Myth's first year: frequent collabs across time zones | Collab-heavy early memories |
- `bible/world/Streaming-Life.md › History`: | 2022-06 | Myth's first off-collab with all five present | Off-collabs as special events |
- `bible/world/Streaming-Life.md › History`: | 2025 | Myth relay for Gura's farewell | "One last time" streams |

### from TakaMori
- `bible/world/TakaMori.md › [SW] Description`: It began as Myth's founding double act: in 2020 Kiara declared a crush on Calli and named the ship "TakaMori," a persona joke pairing an immortal phoenix with a reaper who could never keep her dead; Kiara called Calli her "wife," and Calli rebuffed her as "kusotori"
- `bible/world/TakaMori.md › How It Works`: - **Recent milestones (archive, S1):** an off-collab "Reunion & Gaming!! #takamori" and a karaoke collab (2022-06); off-collabs in 2023 (a Rubik's cube stream, "TAKAMORI OFF-COLLAB" with Kobo, doing each other's nails on camera with IRyS); their duet "Fire N Ice" (2023-12-14; lyrics by Calli and TeddyLoid); Kiara's off-collab watch party "cheering Calli on!!!" for Calli's GriMoire concert (2025-02-27); a four-part Split Fiction co-op series in April–May 2025, titled by them "takamori split screen nostalgia," "Perfectly In Sync with @TakanashiKiara," "thumbnail teetee manifestation into gameplay teetee" and "Saving the World with @TakanashiKiara"; Myth's 5th anniversary collab (2025-09-13) and the announced 6th anniversary live (2026-09-19; not verified as held).
- `bible/world/TakaMori.md › History`: | 2026-09-19 (announced) | Myth 6th anniversary live announced with both | Still side by side |

### from TakoTori
- `bible/world/TakoTori.md › [SW] Description`: Takanashi Kiara and Ninomae Ina'nis, Myth's gas pedal and brake.
- `bible/world/TakoTori.md › How It Works`: - **The chicken incident (2020):** after Gura filled the back room of Kiara's KFP building in Minecraft with chickens, Ina was checking on them when a creeper exploded and released them; Kiara "fired" Ina, and the incident became KFP lore. [Observed S4 §KFP, secondary]
- `bible/world/TakoTori.md › How It Works`: - **How often (archive, S1):** mentions per year 30 (2020), 34 (2021), 17 (2022), 10 (2023), 11 (2024), 6 (2025), 4 in the thin 2026 archive, the highest 2026 rate of any Myth pair. [Observed S1; counts by Claude]

### from Time Duo
- `bible/world/Time-Duo.md › [SW] Other Names`: Ame and Kronii, Kronii and Ame
- `bible/world/Time-Duo.md › [SW] Description`: Watson Amelia and Ouro Kronii, the time-traveling detective and the Warden of Time.
- `bible/world/Time-Duo.md › [SW] Description`: Their rivalry is a lore joke: when Kronii debuted, Ame joked that Twitter was "protecting me from a certain time lord" and swore "i'll give it back soon," as if her time travel were borrowed.
- `bible/world/Time-Duo.md › [SW] Description`: Ame has joked that Kronii "dislikes everything she likes," and Ame's alternate-Ame lore includes an "Epic Ame War" against Kronii that messed up time.
- `bible/world/Time-Duo.md › [SW] Description`: On stream they played 5D chess neither understood, and Ame's last week of regular streams (2024) included Backrooms and Deep Rock Galactic with Kronii.
- `bible/world/Time-Duo.md › [SW] Description`: Ame, now an affiliate, guested at Kronii's March 2026 birthday live, "The Goddess Descends."
- `bible/world/Time-Duo.md › [SW] Rules`: Ame plays the guilty borrower, Kronii the unimpressed Warden.
- `bible/world/Time-Duo.md › [SW] Rules`: In the 2026 baseline Ame appears as a guest, not a regular collab partner.
- `bible/world/Time-Duo.md › How It Works`: - **The lore joke:** when Kronii was announced (2021) and her account was briefly restricted by the rush of followers, Ame joked "twitter is protecting me from a certain time lord" and "i swear i'll give it back soon...." — as if her time travel were borrowed from the Warden. [Observed S2 §Lore, secondary]
- `bible/world/Time-Duo.md › How It Works`: - **Opposites (a joke):** Ame joked that Kronii "dislikes everything she likes." [Observed S2 §Likes and dislikes, secondary]
- `bible/world/Time-Duo.md › How It Works`: - **Lore chaos:** Ame's alternate-Ame lore includes an "Epic Ame War" between Kronii and many Ames that "messed up" time, which Ame compared to one bear-sized duck against fifty duck-sized bears. [Observed S3 §Alter Ames, secondary]
- `bible/world/Time-Duo.md › How It Works`: - **On stream (archive, S1):** Ame's surprise karaoke off-collab with Ina, Kronii, Fauna and Mumei (2022-02-25, per S3); 5D Chess "I Don't Understand With @WatsonAmelia" (Kronii, 2023-04-08); Escape the Backrooms with Calli (2024-09-22) and Deep Rock Galactic with Kiara and Gura (2024-09-30, Ame's last week of regular streams).
- `bible/world/Time-Duo.md › How It Works`: - **2026:** Ame guested at Kronii's March 2026 birthday live, "The Goddess Descends" (2026-03-13 in the Americas, 03-14 in Japan; "Fall in Grace" in an earlier note refers to the same broadcast). [Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711; S3 §2026, secondary]
- `bible/world/Time-Duo.md › History`: | 2024-09 | Backrooms and DRG in Ame's last week | — |
- `bible/world/Time-Duo.md › History`: | 2026-03-13 | Ame guests at Kronii's 3D birthday live | The affiliate's cameo |
- `bible/world/Time-Duo.md › Conflicts and Story Hooks`: 1. Kronii "audits" Ame's time travel as a bit; Ame pleads a borrowed watch.
- `bible/world/Time-Duo.md › Conflicts and Story Hooks`: 3. An Ame cameo in 2026: Kronii pretends not to be delighted.
- `bible/world/Time-Duo.md › Hard Facts`: - Ame guested at Kronii's 3D birthday live on 2026-03-13.

### from Time and Death
- `bible/world/Time-and-Death.md › How It Works`: - **Horror and chaos co-ops (archive, S1):** a cowboy TTRPG one-shot (2023-05), Devour (2023-10), Inside the Backrooms (2023-11), Lethal Company (2023-12), The Outlast Trials (2024-02), Escape the Backrooms with Ame (2024-09-22, just before Ame stepped back), Powerwash Simulator ("Get Your Shrek On," 2024-10), 100% Orange Juice ("game for good friends!!", 2025-01).
- `bible/world/Time-and-Death.md › History`: | 2024-09-22 | Escape the Backrooms with Ame | One of Ame's last collabs |

### from VTuber Persona and Lore
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They use it as a joke engine: age jokes (Gura's "9,000-something," Kronii jokingly "60"), immortality and rebirth gags (Kiara), "canonically" framed bits (Ame calling in "from 2021" during Calli's 2026 charity stream). [Observed character files; Ame's wiki page §2026, secondary]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They can re-enter it for a bit and drop it again: Calli's reaper threats, Ina's "priestess" voice, Kiara's KFP manager routine, Ame's "Trust me, I'm a time traveler." [Observed character files]
- `bible/world/VTuber-Persona-and-Lore.md › History`: | 2020-09 | Myth debuts with official lore profiles | Lore bits still in use |

### from hololive -Advent-
- `bible/world/hololive--Advent.md › [SW] Rules`: Myth and Promise are their seniors.
- `bible/world/hololive--Advent.md › How the Group Works`: - **Seniors:** Advent debuted after Myth, Project: HOPE and Council; the latter two were later organized as Promise. Kiara hosted all five on HOLOTALK (2023-08-12) within two weeks of their debut. [Observed S5 Kiara archive title]

### from hololive -Justice-
- `bible/world/hololive--Justice.md › [SW] Rules`: Myth, Promise and Advent are their seniors.

### from hololive -Promise-
- `bible/world/hololive--Promise.md › How the Group Works`: - **After 2025:** the group is three. Kronii's 2026 activity includes a 3D birthday live with Ame as a guest, the Serendipity pairing with Ina and her EP. [Observed Kronii file K4, K33, K36]
- `bible/world/hololive--Promise.md › Conflicts and Story Hooks`: 4. Kronii has to pick between a Promise plan and a Myth friend's invite on the same night.

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 | "ENigmatic Recollection" (ENReco) announced: EN members in the fantasy world Libestal, via a Minecraft series, animation and songs | Guilds: IRyS in "Cerulean Cup," Nerissa and Gura in "Scarlet Wand" |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-09-30 | **Watson Amelia concludes regular activities and stays an affiliate** | Ame appears as a guest |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-11-29 | Two months after Ame's change of status, COVER names it: "conclusion of streaming activities," distinct from graduation (affiliates can still appear in projects) | Why Ame can come back for events |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-05-01 | **Gawr Gura graduates** | Myth's first graduation; her last post: "keep swimming! always!" |
- `bible/world/hololive-History-2023-2026.md › How It Works in Stories`: - Affiliates (Ame) can appear at events and in projects; graduates (Gura, Fauna, Mumei) appear only as memories, callbacks and songs. [Official S1 2024-11-29 notice, secondary]
- `bible/world/hololive-History-2023-2026.md › Conflicts and Story Hooks`: 2. An affiliate guest appearance: Ame drops into a concert and the crowd loses it.
- `bible/world/hololive-History-2023-2026.md › Hard Facts`: - Merger 2026-09-07. Ame affiliate since 2024-09-30. Gura graduated 2025-05-01; Fauna 2025-01-03; Mumei 2025-04-27 (04-28 JST).

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Other Names`: early hololive, Myth's debut
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › [SW] Description`: "Link Your Wish" in Makuhari (03-20; Kiara: "MAKUHARI WAS ON FIRE!"), HOLOSTARS adds the unit UPROAR!! and the English group -TEMPUS-, holoMeet starts with Gura as ambassador, Calli holds her first solo concert (07-21), and Sana graduates (07-31).
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-08 | 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) | The JP generation just before Myth |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-09-08 | hololive English announced; Myth's members appear on X | "Myth's birthday" season |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-09-12/13 | **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame | The cast's origin |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-10-22 | Gura becomes the first hololive member to reach 1 million subscribers | A Myth legend |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2021-05-30 | Kiara reaches 1 million: every Myth member is over 1 million | A Myth first |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2021-06-30 | Gura passes Kizuna AI as the most-subscribed VTuber | A Myth legend |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-04-26 | holoMeet begins; Gura is an ambassador | Global events |
- `bible/world/hololive-History-to-2022.md › How It Works in Stories`: - This is shared memory: members refer to these moments as in-jokes and milestones ("back when Myth was the only EN gen," "Gura's million"), not as lectures.
- `bible/world/hololive-History-to-2022.md › Conflicts and Story Hooks`: 1. A Myth anniversary stream replays the 2020 debuts; Calli insists she was "first."
- `bible/world/hololive-History-to-2022.md › Conflicts and Story Hooks`: 2. A member retells where she was when Gura hit a million.
- `bible/world/hololive-History-to-2022.md › Hard Facts`: - Myth debuted 2020-09-12/13 JST; IRyS 2021-07-11; Council 2021-08-23.

### from hololive
- `bible/world/hololive.md › [SW] Description`: (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-.
- `bible/world/hololive.md › [SW] Description`: Watson Amelia concluded her regular activities on 2024-09-30 and remains an affiliate who appears at events; Gawr Gura graduated on 2025-05-01 and is an alumna, as are Promise's Ceres Fauna (2025-01-03) and Nanashi Mumei (2025-04-27).
- `bible/world/hololive.md › [SW] Rules`: A story set before a date uses the statuses of that date (Gura active before May 2025; Ame streaming regularly before October 2024; branch names before September 2026).
- `bible/world/hololive.md › How It Works`: - **Structure (as of 2026-09-30):** hololive production is COVER's brand, which also includes the male group HOLOSTARS; hololive is its female VTuber group. On 2026-09-07 COVER unified the former female-talent branches (hololive, hololive English, hololive Indonesia, hololive DEV_IS) under a single "hololive," an organizational and branding change it described as removing regional limits; members had already collaborated across branches for years; former groups keep their names as units (hololive -Myth-, -Promise-, -Advent-, -Justice-). Promotion is now done for all members in Japanese, Indonesian and English. [Official S6] [Observed S2 §2026, secondary, citing the hololive Next broadcast of 2026-09-07; project.md]
- `bible/world/hololive.md › How It Works`: - **Member status:** active talents; **affiliates** who concluded their general activities but remain with hololive and appear at individual events (Watson Amelia since 2024-09-30); **graduates** who left (Gawr Gura on 2025-05-01; in Promise, Ceres Fauna 2025-01-03 and Nanashi Mumei 2025-04-27). Graduates are called alumni; stories never give reasons beyond "graduated." [Official COVER notices; Observed S2]
- `bible/world/hololive.md › How It Works`: - **Events that anchor a calendar:** debut anniversaries (Myth's in mid-September), birthdays (often a 3D live), hololive English concerts (the 4th, "Serendipity," 2026-07-03/04, Shrine Auditorium, Los Angeles), hololive fes and SUPER EXPO (7th fes, 2026-03-06–08), holoMeet events. [Observed S2]
- `bible/world/hololive.md › How It Works`: - **Edge example:** a story set before 2026-09 uses the old branch name "hololive English" and the members' statuses at that date (e.g. Gura active before May 2025). [Adaptation]
- `bible/world/hololive.md › History`: | 2020-09 | hololive English -Myth- debuts (first EN generation) | Myth anniversaries every September |
- `bible/world/hololive.md › History`: | 2024-09-30 | Watson Amelia concludes general activities, stays an affiliate | Occasional guest appearances |
- `bible/world/hololive.md › History`: | 2025-05-01 | Gawr Gura graduates | Alumna; remembered in songs and anniversaries |
- `bible/world/hololive.md › Conflicts and Story Hooks`: 4. A kouhai asks a Myth senpai for advice and gets a joke first, then a real answer.
- `bible/world/hololive.md › Hard Facts`: - Amelia: affiliate since 2024-09-30. Gura: graduated 2025-05-01. Fauna: 2025-01-03. Mumei: 2025-04-27.

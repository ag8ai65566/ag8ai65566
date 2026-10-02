# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: myth1
Packet: projects/holoen/research/qa/packets/myth1.md (owned material) and projects/holoen/research/qa/packets/myth1-incoming.md (incoming claims); both are inline below
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
   "name": "Mori Calliope",
   "file": "bible/characters/Mori-Calliope.md",
   "other_names": [
    "Calli",
    "Calliope",
    "Mori",
    "Calliope Mori",
    "森カリオペ",
    "森美声",
    "Mor Mori",
    "Kawaiiope",
    "Miss Mori",
    "Mowi",
    "CallioP",
    "Cori Malliope"
   ],
   "groups": [
    "hololive",
    "hololive -Myth-",
    "Myth",
    "CHADCast",
    "hololive English (former branch name)",
    "Last Writes"
   ],
   "status": "She has no supernatural abilities; her lore is a performed persona. Calli is a VTuber whose lore, a persona she plays for laughs, makes her the Grim Reaper's first apprentice: when modern medicine gutted the reaping business, she became an idol-rapper VTuber to harvest souls through music and streams.",
   "status_interval": {
    "state_at_baseline": "active",
    "debut": null,
    "graduated": null,
    "regular_activities_concluded": null,
    "source": "bible/characters/Mori-Calliope.md › Background"
   }
  }
 ],
 "world": [
  {
   "name": "TakaMori",
   "file": "bible/world/TakaMori.md",
   "role": "Relationship",
   "other_names": [
    "Takamori",
    "TakaMori",
    "Calli and Kiara",
    "Kiara and Calli"
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
   "unit": "Last Writes",
   "members": [
    "Mori Calliope",
    "Shiori Novella"
   ],
   "evidence": "official Serendipity billing, 2026"
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

### projects/holoen/research/qa/packets/myth1.md

# Audit packet: myth1

Snapshot: git c06ffa3. Registry: `projects/holoen/research/qa/registry.json`. Manifest: `projects/holoen/research/qa/manifest.json`.
Locators read `file › field` ([SW] fields) or `file › section` (dossier rows and bullets). You may open
any file under `projects/holoen/bible/` for full context (relationship maps, sources, merge records).

Owned files (sha256): `bible/characters/Mori-Calliope.md` 1d1db639dda3; `bible/world/TakaMori.md` e9cf098194f5

## 1. Owned files (consistency fields, dossier timelines and hard facts)

### Mori Calliope — `bible/characters/Mori-Calliope.md`
**[SW] Groups:** hololive, hololive -Myth-, Myth, CHADCast, hololive English (former branch name), Last Writes
**[SW] Other Names:** Calli, Calliope, Mori, Calliope Mori, 森カリオペ, 森美声, Mor Mori, Kawaiiope, Miss Mori, Mowi, CallioP, Cori Malliope
**[SW] Background:** She has no supernatural abilities; her lore is a performed persona. Calli is a VTuber whose lore, a persona she plays for laughs, makes her the Grim Reaper's first apprentice: when modern medicine gutted the reaping business, she became an idol-rapper VTuber to harvest souls through music and streams. In that lore her Underworld looks like a modern city with bad internet, and she once waitressed there to save up for Japan. She debuted first in hololive -Myth- in September 2020; her fans are the Dead Beats, her mentor is Death Sensei, her publicly depicted cat mascot is Tutu, and her scythe is named Ricky. She is a signed singer, songwriter and rapper whose sound has grown from rap into rock. She headlined New Underworld Order in Tokyo and GriMoire at the Hollywood Palladium, the first solo concert outside Japan by a hololive production talent, and in 2026 she released her album DISASTERPIECE. She co-hosts the CHADCast podcast with IRyS and Hakos Baelz, and she started a 2026 performance partnership with Shiori Novella. Myth still includes Takanashi Kiara and Ninomae Ina'nis; Gawr Gura has graduated, and Watson Amelia is an affiliate.
**[SW] Relationships:** Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; they toned the ship down in 2021, and now they collab less but are settled, affectionate old friends who bicker like an old married couple. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote the lyrics for Ina's song TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q" together, and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert "The Show Goes On!" Watson Amelia (affiliate): Myth genmate who "called in from 2021" to Calli's 2026 charity stream. IRyS and Hakos Baelz: her CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (their 2025 duet "OVER//RIDE"; Calli guested at Nerissa's 3D concert). Gigi Murin ("Grem Reaper," a shared title): horror and job-simulator collabs; Calli came to like her own name once Gigi kept using it. Kobo Kanaeru calls her "Uncle Dad." Koseki Bijou ("Biboo," "TombStone"): a junior whose skill Calli admires; they played Bijou's Undertale mod starring Calli and ran a 24-hour charity stream together (2025). Shiori Novella: her partner for the 2026 Serendipity concert who calls her "Mor Mori"; they chase absurd premises together, and Calli admits she is "a little obsessed with her." Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds (Calli's mock exposé of Kronii's joke "$KRONII" coin), with a running joke about their 1 cm height difference. Hoshimachi Suisei: a Japanese senpai she's starstruck by ("Death Star"). Rikka (HOLOSTARS): they released "spiral tones" together (MoRikka). Elizabeth Rose Bloodflame, Koganei Niko, Ayunda Risu and Amane Kanata: fellow LYRA vocalists on a "III" remix cover. Nanashi Mumei (graduated 2025): her "ANATOMY REVIEW" drawing-stream partner (2022). FUWAMOCO: "FUWAMOCALLI," a pair name the twins favor.
**Dossier · Background Timeline:**
| Date | Event | Relevance |
|---|---|---|
| Lore | She is the Grim Reaper's first apprentice. Modern medicine hurt the reaping business, so she turned to VTubing to harvest souls. | Her central premise [Official C1] |
| Lore | She comes from an Underworld that looks like a modern city; she blamed debut lag on its bad internet. She waitressed there to save up for a trip to Japan. | Secondary lore [Observed C4 §Lore and §Miscellaneous] |
| 2020-09-12 | She debuts first in hololive English -Myth-. Her fans become the Dead Beats. | [Official C1] [Observed C4 §Debut] |
| 2022-04 | She signs with EMI Records / Universal Music Japan. | [Observed C4 §2022, secondary] |
| 2022 | CHADCast begins with IRyS and Hakos Baelz. | [Observed C12] |
| 2022-07-21 | Her solo concert "New Underworld Order." | [Official C6] |
| 2024-09-05 | Tutu, a cat, is added to her model as a toggle. | [Observed C4 §Mascot and fans, secondary] |
| 2025-02-26 | "GriMoire" at the Hollywood Palladium, the first solo concert outside Japan by a hololive production talent. | [Official C19] |
| 2026-02-06 | Her third major album, "DISASTERPIECE." | [Official C16] |
| 2026-06-10 | Serendipity interview and partnership with Shiori Novella. | [Official C11] |
| 2026-09-07 | The branches merge into one "hololive." Her unit is now hololive -Myth-. | [Official C17, C1] |
**Dossier · Hard Facts (continuity):**
- Birthday April 4 (4/4: "shi" is also "death"). Height 167 cm. Debut 2020-09-12. Unit: hololive -Myth-.
  [Official C1] [Observed C4 §Miscellaneous, secondary]
- Fans: Dead Beats. Fan mark 💀. Mascot: Death Sensei (designed by Ina). Scythe: Ricky. Cat on her
  model: Tutu. [Official C1] [Observed C4 §Mascot and fans and §Personality, secondary]
- Japanese name 森カリオペ; historical styling 森美声 (before 2021-09-01). [Official C1] [Observed C4
  §Name, secondary]
- Likes (secondary, C4 §Likes and dislikes): red wine, oolong tea, rap and rock, FromSoftware games,
  Castlevania: SotN, JoJo. Gachiakuta: [Unverified] (not in C4).
- Dislikes (secondary, C4 §Likes and dislikes): crowds, coffee, hospitals, cantaloupe. The "6 7" meme:
  [Unverified, title only: C21-1M69I28RWUU, C21-r8jx_Tlb9zA clip titles; off the card].
- Performed identities are excluded from name matching unless a story uses them: Calvin Mori, C-Man,
  YUNG SH1N1GAM1 B01 (male personas), and "The Pineapple" (JP GTA). [Observed C4 nickname list and
  §Events, secondary]

### TakaMori — `bible/world/TakaMori.md`
**[SW] Other Names:** Takamori, TakaMori, Calli and Kiara, Kiara and Calli
**[SW] Description:** Mori Calliope and Takanashi Kiara are longtime close friends whose present-day public dynamic has an "old married couple" rhythm: familiar bickering, affectionate teasing and shared history despite fewer collaborations. Kiara says the love out loud, explaining that Calli "actually does like me a lot but is just really bad at expressing herself"; Calli deflects, then snaps "What do you mean?! I love Kiara!" when a fan suggests they're only friends "now." It began as Myth's founding double act: in 2020 Kiara declared a crush on Calli and named the ship "TakaMori," a persona joke pairing an immortal phoenix with a reaper who could never keep her dead; Kiara called Calli her "wife," and Calli rebuffed her as "kusotori" (shitbird) while quietly supporting the hashtag. Calli made and narrated Kiara's debut intro. They toned the routine down in 2021. Since then: the duet "Fire N Ice" (2023), Kiara's watch party for Calli's 2025 concert, and a 2025 co-op series they titled "takamori split screen nostalgia." They play "Mom" and "Dad" to Kobo Kanaeru; when Kobo appeared in their chat they told her "Go to bed!" and "Sorry Kobo, you can't be part of this because it's two players only." When their game gave them fire and ice powers, they riffed, "Fire and ice, death and life." At the end of that series they bickered over a mangled idiom ("glass stones in stone houses or whatever") until one gave up ("Whatever. We don't need any of these metaphors") and signed off: "Takamori will always get together for these ones, right?"
**[SW] Rules:** They toned down the early flirt-and-rebuff routine in 2021. Its nicknames and performed couple jokes remain shared callbacks; they do not establish a private romantic relationship, and no romance or intimacy is written. Kiara is openly affectionate; Calli is gruff in words and loyal in actions, and "kusotori" is a term of endearment by now. Collabs are occasional; when they meet, it feels like no time has passed. In the 2025 co-op lines quoted here, who said which is not always known; keep those exchanges unattributed.
**Dossier · History:**
| Date | Event | Trace left |
|---|---|---|
| 2020-09 | Kiara declares the crush on Calli's 2nd stream; "TakaMori" named | The ship name |
| 2020-12 | Kiara's amnesia re-debut: "Who's Calli?" | Running gag |
| 2021-09 | Flirt-and-rebuff routine toned down; still close friends | Nicknames and couple jokes remain callbacks |
| 2022-06 | "Reunion & Gaming!! #takamori" off-collab; karaoke collab | In-person reunion |
| 2023 | Off-collabs; "Fire N Ice" duet (2023-12-14) | Their song |
| 2025-02-27 | Kiara's watch party for Calli's GriMoire concert | Cheering from the crowd |
| 2025-04/05 | Split Fiction series ("takamori split screen nostalgia") | Nostalgic co-op |
| 2026-09-19 (announced) | Myth 6th anniversary live announced with both | Still side by side |
**Dossier · Hard Facts (continuity):**
- "TakaMori" was named by Kiara (2020); toned down in 2021; they remain close friends.
- Kobo's "parents" bit: Kiara "Mom," Calli "Dad"; "not married, Kobo is adopted."
- No real romance or intimacy is written; the flirting is a performed bit.

Incoming claims continue in `myth1-incoming.md`.

### projects/holoen/research/qa/packets/myth1-incoming.md

# Audit packet: myth1 (incoming claims)

Snapshot: git c06ffa3.

## 2. Incoming claims (other files naming this cohort: [SW] sentences, dossier rows and bullets)
Matched names: ara and Calli|Calli and Kiara|hololive -Myth-|Calliope Mori|Cori Malliope|Mori Calliope|Last Writes|Miss Mori|Kawaiiope|Mor Mori|Takamori|TakaMori|Calliope|CallioP|Calli|森カリオペ|Mori|Mowi|LYRA)(

### from Cecilia Immergreen
- `bible/characters/Cecilia-Immergreen.md › [SW] Background`: (2026; Cecilia wrote the lyrics and directed it), a 2026 3D live, and the Serendipity concert, where she also sang "Break It Down" with Vestia Zeta and Shiori Novella and "Cloudy Sheep" with Tsunomaki Watame and Mori Calliope.
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Tsunomaki Watame (JP) and Mori Calliope: "Cloudy Sheep" at Serendipity.
- `bible/characters/Cecilia-Immergreen.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice, "CCGG MADNESS" as Autofister with Gigi, "Break It Down" with Vestia Zeta and Shiori, "Cloudy Sheep" with Tsunomaki Watame and Calli (day 1); "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official CI4, CI8] |
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Tsunomaki Watame (JP), Mori Calliope | Cross-branch; senior | "Cloudy Sheep" at Serendipity (2026) | [Official CI8] |

### from Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Background`: She debuted first of her generation on 2024-06-21 (PDT) in hololive English -Justice-, held her 3D showcase on 2025-08-01 (PDT), sang at the 2025 English concert ("ALiCE&u" with Nerissa and Ayunda Risu, a solo "Stellar Stellar," and the day-two opener "START AGAIN" with Calli, IRyS and Nerissa), invited guests from several branches to her 2026 birthday live, and at the 2026 Serendipity concert sang "HELP!!" with Kobo Kanaeru and Hakos Baelz and formed the unit Bloodraven with Nerissa Ravencroft ("Cruel Angel's Thesis").
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: (with Calli and IRyS); Elizabeth says Nerissa "has a beautiful voice,"
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Mori Calliope: the LYRA cover of "III" with Amane Kanata, Koganei Niko and Ayunda Risu.
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Behavioral Traits`: 2. Voice mimicry and impressions as pranks: she voiced the Advent members in Justice's introduction video, surprised Mori Calliope at her debut with a TakaMori skit, and trolls hololive and HOLOSTARS members with a "Venom"/demon voice. [Observed EB2 §Personality, §Miscellaneous, secondary]
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2025-08-23/24 EDT | -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie | [Official EB5] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Nerissa Ravencroft | Advent senior; lore "mortal enemy"; Serendipity 2026 unit Bloodraven | A "Rondo Revolution" cover; "ALiCE&u" (with Ayunda Risu) and "START AGAIN" (with Calli and IRyS) at -All for One-; "Cruel Angel's Thesis" as Bloodraven (2026); Elizabeth: "She has a beautiful voice," "the perfect harmony"; Nerissa praises her kindness. Nerissa has been "calling me her husband, my husband" (Elizabeth, 2025), a performed bit | [Official EB4, EB5] [Observed EB2] [ASR EB20, Rk03Rh8P9ps 0:38:00] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Mori Calliope | Myth senior | A TakaMori impression at debut (secondary); the LYRA cover of "III" with Amane Kanata, Koganei Niko, Calli and Ayunda Risu; "START AGAIN" on stage; "Jade Sword" guild in ENReco | [Observed EB2, secondary] [Official EB5] [EB9] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kobo Kanaeru, Ayunda Risu | ID seniors | "HELP!!" with Kobo and Hakos Baelz at Serendipity (2026); Kobo calls her "Lilis" (secondary); LYRA and "ALiCE&u" with Risu | [Observed EB2] [Official EB5, EB8] |

### from Fuwawa Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Mori Calliope: "FUWAMOCALLI," a collaboration name the twins say they particularly like.
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026).
- `bible/characters/Fuwawa-Abyssgard.md › Relationship Map`: | Gigi Murin, Mori Calliope | Kouhai and senior | "2 Creatures + 1 Reaper," a rare bomb-defusing collab (2026-09) | [Observed FUWAMOCO X post via wiki, FW6] |

### from Gawr Gura
- `bible/characters/Gawr-Gura.md › [SW] Groups`: hololive -Myth- (graduated), hololive alum, Myth, hololive English (former branch name)
- `bible/characters/Gawr-Gura.md › [SW] Background`: Gura is a VTuber and a hololive alum: she graduated from hololive -Myth- on May 1, 2025.
- `bible/characters/Gawr-Gura.md › [SW] Background`: She hosted The Fish Tank with Watson Amelia and sang "Q" with Mori Calliope.
- `bible/characters/Gawr-Gura.md › [SW] Relationships`: Mori Calliope: her "Bone Bros" partner in pranks, bickering and the duet "Q"; Calli went on a "One Last Minecraft Trip" with her before she graduated, and performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert."
- `bible/characters/Gawr-Gura.md › Voice Profile`: - Other members' openers (Kiara's "Kikkeriki," Calli's "What is up, humans?!").
- `bible/characters/Gawr-Gura.md › Background Timeline`: | 2022-02-03 | "Q" with Mori Calliope (DECO*27) | [Official G15] |
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Mori Calliope | Myth genmate ("Bone Bros") | Pranks, bickering and duets; co-vocalists on "Q" | [Observed G2 §Relationships] [Official G15] |

### from Gigi Murin
- `bible/characters/Gigi-Murin.md › [SW] Relationships`: Mori Calliope: Mouthwashing, Fast Food Simulator, R.E.P.O. and The Boba Teashop; the League of Legends campaign; with Fuwawa, "2 Creatures + 1 Reaper"
- `bible/characters/Gigi-Murin.md › Behavioral Traits`: 3. Relentless campaigns: years of trying to get Mori Calliope to play League of Legends; shouting "MORI CALLIOPE!" in full. [Observed GG2 §Personality, §Quotes, secondary]
- `bible/characters/Gigi-Murin.md › Voice Profile`: - "MORI CALLIOPE!", an emphatic callout. [Observed GG2 §Quotes, §Miscellaneous, secondary]
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Mori Calliope | Senior ("Grem Reaper") | Mouthwashing, Fast Food Simulator, R.E.P.O., The Boba Teashop (2024–25); "MORI CALLIOPE!"; the League of Legends campaign; with Fuwawa, a 2026 bomb-defusing collab, "2 Creatures + 1 Reaper" (Fuwawa's post; GPT could not read it, the Advent review accepted a reproduction) | [Observed GG2, GG3; X post GG6] |
- `bible/characters/Gigi-Murin.md › Story Engine`: - Trouble she brings: a plan that "would be funny"; a bit repeated past its limit; an ambush on Mori Calliope; a keyboard-smash post.
- `bible/characters/Gigi-Murin.md › Story Engine`: 3. Calli finally agrees to one game of League; Gigi panics.

### from IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae.
- `bible/characters/IRyS.md › [SW] Relationships`: Elizabeth Rose Bloodflame: "START AGAIN" with Calli and Nerissa at the 2025 concert.
- `bible/characters/IRyS.md › Background Timeline`: | 2021-07-29 | First official collab: Just Shapes & Beats with Mori Calliope | [Observed R2 §2021] |
- `bible/characters/IRyS.md › Relationship Map`: | Mori Calliope | First collab partner (2021) | "MorIRyS"; CHADCast podcast trio with Bae | [Observed R2 §2021, units] |

### from Koseki Bijou
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: Mori Calliope: they played Bijou's Undertale mod starring Calli together (2023); "TombStone"; a 24-hour charity stream together (2025) and Warhammer painting (2026).
- `bible/characters/Koseki-Bijou.md › Behavioral Traits`: 6. She mods games: on stream with Calli she played an Undertale mod that puts Calli in Sans's place (2023-08-12). [Observed KB3 eRGs-7AqRgs]
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2023-08-12 | An Undertale mod starring Calli, played with Calli on stream | [Observed KB3] |
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-06-29 | "THAT'S WILD?!" 24-hour charity stream with Calli (Wildlife Warriors Worldwide) | [Observed Calli archive J5u2aGUrNq8] |
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Mori Calliope | Senior ("TombStone") | An Undertale mod starring Calli, played together (2023); BG3 as "Killing, Two Birds, with One Stone" (2023); 24-hour charity stream (2025); Warhammer painting (2026); Calli's channel mentions her 29 times | [Observed KB2; KB3; Calli archive] |

### from Mococo Abyssgard
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Mori Calliope: "FUWAMOCALLI."

### from Nanashi Mumei
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Mori Calliope: "ANATOMY REVIEW."
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Mori Calliope | Myth senior | "ANATOMY REVIEW" streams (with Calli and Sana, 2022; solo, 2025) | [Observed M3] |

### from Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › [SW] Background`: (2025) with Calli and IRyS as guests, sang the duet "OVER//RIDE" with Calli (2025), and released "OYOME♡HOLIC" and "Blue World"
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; Nerissa was Calli's first Instagram follower.
- `bible/characters/Nerissa-Ravencroft.md › Background Timeline`: | 2025-05-24 | 3D concert "Requiem for Love – A JukeBox Musical" (guests incl. Calli, IRyS) | [Observed N3 titles] |
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Mori Calliope | Senior | Nerissa was Calli's first Instagram follower; BG3 party "Killing, Two Birds, with One Stone" with Kiara and Bijou (2023); duet "OVER//RIDE" (2025); Calli guested at Nerissa's 3D concert; building Calli's Mii: "Calli's also got beautiful, long, straight hair." | [Observed N2; N3 titles; ASR N20, agrees] |

### from Ninomae Ina'nis
- `bible/characters/Ninomae-Inanis.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Octo'clock
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Mori Calliope: a recurring target of her puns ("Every freaking time, Ina"); Ina designed Calli's Death Sensei, and Calli wrote lyrics for Ina's song.
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **Profanity:** her ordinary speech favors mild exclamations: she has said she "usually never swears," and a rare "damn" from her made headlines in clips [Observed I15 clip titles]; about an hour of checked audio had no swearing in her own words [ASR I29]. Sharper language and bawdy wordplay turn up in specific exchanges (above). Constant swearing in Kiara's or Calli's register would be out of character; an occasional sharp word is not.
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - **How she addresses people:** "you guys," "everyone," "chat," and fans as "Takodachi" (the official fan name is the Tentacult). Members by first or short name ("Calli," "Kiara," "Ame," "Gura," "Kronii," "Bae," "Biboo," "CC"); a full name signals a mock-serious scold. New members are "kouhais." She gives her own name surname-first. [Official I1] [Observed I3 captions; I2 §Mascot and fans]
- `bible/characters/Ninomae-Inanis.md › Voice Profile`: - Measured (I29, 2026 chat): median pitch 223–232 Hz, in the middle of the six files measured the same way (Kronii 177–188 Hz; Gura and Ame about 250–270 Hz), so "mid" rather than "low"; about 81–95 words per minute of speech in that one 2026 chat stream (Kronii 120–127, Calli 161–186 in their chat windows). A 2021 game stream measures 210–214 Hz and 68–116 words per minute (its opening chat 116). Sample results only; they do not establish a general ranking among genmates.
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | Ongoing | Illustrator: drew Myth's intro art; designed the Takodachi [I2 §Mascot and fans], Bubba [Ame file A2 §Mascots and fans] and Death Sensei [Calli file C4 §Mascot and fans] (the wiki says all Myth mascots except Bloop); she drew chibi Bloop artwork, but Bloop's original design is not hers [Gura file G2] | [Observed I2 §Miscellaneous and §Mascot and fans, secondary] |
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026 | TAKO∞TAKOVER, a deliberately unsettling takeover story; lyrics by Mori Calliope | [Observed—published interview I19] [Official I25] |
- `bible/characters/Ninomae-Inanis.md › Background Timeline`: | 2026-09-07 | Branches merge; she is "Ninomae Ina'nis from hololive," unit hololive -Myth- | [Official I28] [Observed I10] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Mori Calliope | Myth genmate | Favorite pun target ("Every freaking time, Ina."); Ina designed Death Sensei; Calli wrote the lyrics for TAKO∞TAKOVER | [Observed I8 captions; I2 §Miscellaneous] [Official I25] |
- `bible/characters/Ninomae-Inanis.md › Hard Facts`: - Birthday May 20; height 157 cm; debut 2020-09-13; unit hololive -Myth-; illustrator Kuroboshi Kouhaku (whom she calls "papa"). [Official I1] [Observed I2 infobox]

### from Ouro Kronii
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Mori Calliope: her first collab partner outside her generation (2021); Calli calls her "Kronster,"
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Secondary description: her voice is "powerful and well-controlled, giving off an 'older sister' vibe" [Observed K8 §Personality, secondary]. The same passage says: "While she has a deep voice comparable to Mori Calliope, she also has a wide vocal-range; she once produced a high-pitched voice by a viewer's request" (linking https://youtu.be/J6VCN6o18mE). [Observed K8 §Personality, secondary] Card wording "a low speaking register" is also supported by the K36 measurement below.
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Measured (K36, chat windows): median pitch 177–188 Hz, the lowest of the six files measured the same way (Calli 197–214 Hz; Gura and Ame about 250–270 Hz); about 120–127 words per minute of speech, mid-paced (Calli 161–186, Ina 81–95). Approximate values for relative comparison.
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Mori Calliope | Fellow EN | Calli calls her "Kronster"; Kronii teases her about being 1 cm taller | [Observed K8 nickname list and §Miscellaneous, secondary] |
- `bible/characters/Ouro-Kronii.md › Hard Facts`: - Aliases: Kronini, Kroniicopter, Kronster (by Calli), Tam Tender (by Raora), Owo-senpai (by Cecilia). Performed identities are excluded from matching unless a story uses them: Ouro Krono (-Ministry- persona, goodbye "Kronovoir") and Tam Gandr (ENreco). [Observed K8 nickname list, §Name and §Miscellaneous, secondary]

### from Raora Panthera
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Mori Calliope and Gigi: Elden Ring Nightreign.
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Gigi Murin | Genmate ("RPGG," secondary) | MapleStory, Monster Hunter Wilds, a food tier-list off-collab, Elden Ring Nightreign with Calli (2025); she designed both her own and Gigi's Monster Hunter Wilds collaboration outfits (2026; secondary report) | [Observed RP3; X post RP6, secondary] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Mori Calliope | Myth senior | Elden Ring Nightreign with Gigi (2025-06-11) | [Observed RP3 AnvhW-eFatE] |

### from Shiori Novella
- `bible/characters/Shiori-Novella.md › [SW] Groups`: hololive -Advent-, hololive English -Advent- (former branch name), Advent, Last Writes
- `bible/characters/Shiori-Novella.md › [SW] Background`: She made her 3D debut on 2024-08-02 (PDT), sang at the 2024 and 2025 English concerts, released her first original song "Monsters and Men" on 2026-02-15, was paired with Mori Calliope at the 2026 Serendipity concert, and began her original motion comic "Into The Void" in July 2026.
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Mori Calliope: her 2026 Serendipity partner in Last Writes ("When My Devil Rises"), who admits she is "a little obsessed with her"; Shiori admires Calli's "work ethic and boundaries," and they bond over dark taste and absurd deep-dives.
- `bible/characters/Shiori-Novella.md › Background Timeline`: | 2026-07-03/04 | Serendipity concert, duo with Mori Calliope | [Official SN4] |
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Mori Calliope | Senior; Serendipity 2026 duo ("Last Writes") | Calli's "#DEEP" kids'-movie talk (2024-01-09) and Stardew Valley (2024-12-20); in the official interview Calli is "a little obsessed with her" and Shiori admires Calli's "work ethic and boundaries"; their dynamic: "Unhinged" (Calli) | [Official SN4] [Observed Calli archive] |
- `bible/characters/Shiori-Novella.md › Arc`: - **Starting point:** active member at the 2026 baseline: her first original song, the Serendipity duo with Calli, "Into The Void."
- `bible/characters/Shiori-Novella.md › Story Engine`: 3. Calli and Shiori record a "deep-dive" on a kids' cartoon that goes too far; the manager bonks both.

### from Takanashi Kiara
- `bible/characters/Takanashi-Kiara.md › [SW] Groups`: hololive, hololive -Myth-, Myth, hololive English (former branch name), Rocku Wawa
- `bible/characters/Takanashi-Kiara.md › [SW] Background`: She debuted with hololive -Myth- in September 2020 speaking English, Japanese and German.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Mori Calliope: her TakaMori partner.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Kiara declared a crush in 2020 and long called Calli her "wife," a public bit they toned down in 2021; now they collab less but are settled, affectionate old friends who bicker like an old married couple.
- `bible/characters/Takanashi-Kiara.md › [SW] Relationships`: Kiara says it plainly: Calli "actually does like me a lot but is just really bad at expressing herself."
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: - "When I first met all of them, the one that struck me was Calli... I was like, 'Damn, she hot, what a hot-ass chick!'"
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: - "Calli goes to The Pink Vice, gets drunk, sees a stripper she likes… realizes the next day the stripper was me"
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: - She uses German, English and Japanese on stream; she has said her English is not perfect and has corrected Calli's Japanese; she learned some Korean in 2022. [Observed T2 §Miscellaneous, secondary]
- `bible/characters/Takanashi-Kiara.md › Voice Profile`: 3. "So actually, tomorrow, Calli, Ina, Wawa, Wawa, Wawa, lots of people in Hytale." (ASR T23, 2:39:41)
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2020-12-10 | Channel briefly terminated, then restored; "#PhoenixDown" re-debut with a mock-amnesia bit ("Who's Calli?") | [Observed T2 §2020 and §Takamori; T5-le72UNZAbQI] |
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2021-09 | She and Calli announce they will tone down the TakaMori ship | [Observed T2 §Takamori] |
- `bible/characters/Takanashi-Kiara.md › Background Timeline`: | 2026-09-07 | Branches merge; unit is hololive -Myth- | [Official T20, T1] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Mori Calliope | Myth genmate | Kiara long called Calli her "wife" and coined "TakaMori"; Calli rebuffed her and calls her "kusotori" ("shitbird"). They announced in 2021 that they would tone the ship down (the wiki adds that "the two remain close friends"; a secondary statement, not a documented current relationship); they play "Mom" and "Dad" to Kobo as a performed family bit | [Observed T2 §Takamori, secondary; T14 title] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Kobo Kanaeru | Collaborator | Kobo calls her "Mommy Kiwawa"; Kiara and Calli play her "Mom" and "Dad" | [Observed T5-gNEWWDKlTM8 clip title; T2 §Takamori] |
- `bible/characters/Takanashi-Kiara.md › Hard Facts`: - Birthday July 6; height 165 cm; debut 2020-09-12; unit hololive -Myth-; illustrator huke. [Official T1]
- `bible/characters/Takanashi-Kiara.md › Hard Facts`: - Nicknames: Kiwawa, Wawa, Tenchou (by fans), Kusotori (by Calli), Kibaba (grandma persona). Frogiwawa is officially a different character. [Observed T2 infobox, §Lore, §KFP, secondary]

### from Watson Amelia
- `bible/characters/Watson-Amelia.md › [SW] Groups`: hololive (affiliate), hololive -Myth- (affiliate), Myth, hololive English (former branch name)
- `bible/characters/Watson-Amelia.md › [SW] Relationships`: Mori Calliope: Myth genmate and Clubhouse 51 opponent.
- `bible/characters/Watson-Amelia.md › Voice Profile`: - **How she addresses people:** "you guys" by default; "chat" occasionally; "Teamates" (one m, official) on big occasions; members "Investigators." Members by name ("Gura," "Calli," "Ina," "Kiara," "Kronii"); Bubba, her dog mascot. She gives her name in English order, "Amelia Watson." [Official A1] [Observed A3 captions; A2 §Mascots and fans]
- `bible/characters/Watson-Amelia.md › Voice Profile`: - Measured (A23; Mario, VALORANT and 2024 chat windows, with game audio mixed in): median pitch about 248–276 Hz; about 114–133 words per minute of speech. For comparison only, Calli's chat windows measured 161–186 and Ina's 81–95. Sample results; they do not establish a general ranking. [ASR A23]
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |
- `bible/characters/Watson-Amelia.md › Relationship Map`: | Mori Calliope | Myth genmate | Clubhouse 51 games [Observed A20]. [Unverified, title only: a surprise "ara ara" scare] | [A20; A6 clip title] |

### from Advent Pairs
- `bible/world/Advent-Pairs.md › [SW] Other Names`: ShioRaven, Goth Rock, Pen Pups, JewelBird, Diamond Dogs, Sound Hounds, Grindstone, GAGA, FUWAMOCALLI, Rocku Wawa, GreyScaleX, Last Writes
- `bible/world/Advent-Pairs.md › [SW] Description`: With seniors: Mori Calliope starred in Bijou's Undertale mod and did a 24-hour charity stream with her, shares "FUWAMOCALLI" with the twins (a collaboration name they say they particularly like), and was Shiori's 2026 concert partner; Kiara hosted all five on HOLOTALK, encouraged Bijou through hard choreography, and partnered her in 2026 ("Rocku Wawa"); IRyS is Bijou's horror co-op partner, and Bijou, Ina and IRyS starred at hololive night at Dodger Stadium (2025); Shiori and Kronii hosted "Rating Your Clocks" together in March 2025.
- `bible/world/Advent-Pairs.md › With Myth`: - **Mori Calliope:** Bijou played her Undertale mod starring Calli with her on stream (2023-08-12); "TombStone" (Bijou), a 24-hour charity stream together (2025-06-29), Warhammer painting (2026); "FUWAMOCALLI," a collaboration name the twins say they particularly like; Fuwawa alone joined Calli and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"); Shiori was Calli's 2026 Serendipity partner (Calli, officially: "I am a little obsessed with her"; their dynamic: "Unhinged"). [Official S4] [Observed S1]
- `bible/world/Advent-Pairs.md › With Myth`: - **Takanashi Kiara:** hosted all five on HOLOTALK; an occult handcam off-collab with Shiori ("#shiotori," 2024-07-12); Baldur's Gate 3 with Bijou, Calli and Nerissa ("Killing, Two Birds, with One Stone," 2023); Bijou was her 2026 Serendipity partner ("Rocku Wawa," and a running "67" joke); Bijou recalls Kiara as "really encouraging and helpful" when Kiara asked her to perform a song with Kiara and Ame whose choreography was one of the hardest she had learned. [Official S4] [Observed S1]
- `bible/world/Advent-Pairs.md › History`: | 2023-08-12 | HOLOTALK with Kiara; Bijou's Undertale replay with Calli | senior ties |
- `bible/world/Advent-Pairs.md › History`: | 2026-07-03/04 | Serendipity: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth | official interviews |
- `bible/world/Advent-Pairs.md › Conflicts and Story Hooks`: 4. Fuwawa, Calli and Gigi defuse a bomb, and nobody reads the manual.
- `bible/world/Advent-Pairs.md › Hard Facts`: - Serendipity 2026 pairs: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth (official).
- `bible/world/Advent-Pairs.md › Hard Facts`: - Shiori and Kronii hosted "Rating Your Clocks" together (March 2025). GAGA is a quartet; GreyScaleX is an official duo unit (Shiori, Zeta). "Fuwawa, Calli and Gigi" (2026) is a Fuwawa collab, not a FUWAMOCO one.

### from Bone Bros
- `bible/world/Bone-Bros.md › [SW] Other Names`: Calli and Gura, Gura and Calli
- `bible/world/Bone-Bros.md › [SW] Description`: Mori Calliope and Gawr Gura, the reaper and the shark: a bickering duo of pranks and jabs, where Calli's gruff big-sister threats bounce off Gura's cheerful dumb-shark defiance.
- `bible/world/Bone-Bros.md › [SW] Description`: Their collabs thinned out over the years, but on the Myth relay before Gura's graduation Calli's stream was "One Last Minecraft Trip."
- `bible/world/Bone-Bros.md › [SW] Description`: Her single "Full Color" was never released; Calli performed it at Myth's fourth-anniversary concert "The Show Goes On!"
- `bible/world/Bone-Bros.md › [SW] Rules`: Calli's affection tends to show through teasing and actions more than speeches.
- `bible/world/Bone-Bros.md › How It Works`: - **The name:** "Bone Bros" is listed as a unit of Calli and Gura on both wiki pages. [Observed S2, S3 §Relationships, secondary]
- `bible/world/Bone-Bros.md › How It Works`: - **Tone:** pranks and bickering with a big-sister/little-shark edge; Calli's gruff threats bounce off Gura's cheerful dumb-shark defiance. [Observed Calli file C4, Gura file G2, secondary; Adaptation for the "big-sister" shorthand]
- `bible/world/Bone-Bros.md › How It Works`: - **Music:** they sang "Q" together with DECO*27 (2022-02-03). [Official Calli file C29]
- `bible/world/Bone-Bros.md › How It Works`: - **Early years:** they were the branch's first two to 1 million subscribers (Gura, then Calli in January 2021) and were named Tokyo Tourism Ambassadors together with Sakura Miko (2023-02-08). [Observed S2, S3, secondary]
- `bible/world/Bone-Bros.md › How It Works`: - **"Dad":** Calli's "Dad" nickname is said to have started around Gura. [Unverified: stated in this project's Calli file from an earlier wiki reading; not found in the current revision]
- `bible/world/Bone-Bros.md › How It Works`: - **Later collabs (archive, S1):** horror co-op (The Outlast Trials, 2023-05), group games (Liars Bar, 2025-01-22) and Calli's "One Last Minecraft Trip." on the Myth relay for Gura's farewell (2025-04-30).
- `bible/world/Bone-Bros.md › How It Works`: - **"Full Color":** Gura's single was never released; Calli performed it at hololive English -Myth-'s fourth-anniversary concert "The Show Goes On!" (September 2024), and Calli and Kiara said they would keep singing it in karaoke. [Observed S2 §Miscellaneous, secondary; archived official broadcast CDljbqawDkw]
- `bible/world/Bone-Bros.md › History`: | 2024-09 | Calli performs Gura's "Full Color" at Myth's 4th-anniversary concert "The Show Goes On!" | Carrying her song |
- `bible/world/Bone-Bros.md › Conflicts and Story Hooks`: 1. (Before 2025-05) Gura pranks Calli's Minecraft base; Calli plots revenge on stream.
- `bible/world/Bone-Bros.md › Conflicts and Story Hooks`: 2. (Proposed fiction, before 2025-05) Calli and Gura look back on their published duet "Q" on stream.
- `bible/world/Bone-Bros.md › Conflicts and Story Hooks`: 4. (2026) A karaoke stream where Calli sings "Full Color" and chat goes quiet.
- `bible/world/Bone-Bros.md › Conflicts and Story Hooks`: 5. (2026) Calli sings "Full Color" at a karaoke stream and tells chat why.
- `bible/world/Bone-Bros.md › Hard Facts`: - 2026 baseline: Gura has graduated; Calli performed "Full Color" in 2024 and said she would keep singing it.

### from Concerts and Live Events
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: Recurring formats: each spring, hololive fes. with hololive SUPER EXPO in Japan (a combined tradition since 2022; Calli and Kiara sang at the 2022 fes. in Makuhari, Nerissa at the 6th fes. in 2025); each summer, a hololive English concert in the US (2023 "-Connect the World-"; 2024 "-Breaking Dimensions-,"
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: Los Angeles, July 3–4, built on units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia), with guests Ookami Mio, Kobo Kanaeru, Vestia Zeta and Tsunomaki Watame singing alongside EN members); world tours (World Tour '24 "-Soar!-" with Kiara, Ina and Bae among seven performers, with Kronii and Nerissa at pre-concert panels; World Tour '25 "-Synchronize!-" led by Calli, IRyS, Nerissa, Nene and Ollie, with Kronii and Bae as Sydney guests); birthday and anniversary 3D lives; holoMeet.
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: The cast's own stages: Calli's "GriMoire" at the Hollywood Palladium (2025, the first hololive solo concert outside Japan); Kiara and Ina's duo concert "Drawn to Dawn"
- `bible/world/Concerts-and-Live-Events.md › [SW] Description`: (2025) with Calli and IRyS as guests; Gura's final mini live (2025-05-01); hololive night at Dodger Stadium with Ina, IRyS and Bijou (2025-07-05); FUWAMOCO's first birthday concert (2025) and Advent's anniversary lives "On the Run!"
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive fes. + hololive SUPER EXPO** (spring, in Japan; the combined fes./EXPO tradition dates to 2022, while fes. itself is older): the agency-wide concert and convention. 3rd fes "Link Your Wish" (2022-03, Makuhari; Calli and Kiara performed on day 2, per their X posts), 4th fes "Our Bright Parade" (2023), 5th "Capture the Moment" (2024), 6th "Color Rise Harmony" (2025-03-08/09; Nerissa on day 1), 7th "Ridin' on Dreams" (2026-03-06/08). EN units share Expo booths and key visuals (Myth with Promise, Advent with Justice). [Observed S1 §2023–§2026; S2]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **hololive English concerts** (US, summer): "-Connect the World-" (2023-07-02), "-Breaking Dimensions-" (2024-08-24/25, Kings Theatre, New York; Fauna and Mumei premiered their duet "It's Not a Phase"; Kiara, Mumei and Nerissa sang "Beyond the way"; Fauna, Shiori and Nerissa "Lonely in Gorgeous" [Official S8]), "-All for One-" (2025-08-23/24, Radio City Music Hall, New York; all fifteen EN members: Advent's "Genesis"; "HOT DUCK!" by Bijou, FUWAMOCO and Oozora Subaru; "MONSTER" by Ina, Kronii, Shiori and Gigi; "SHALLYS" by Ina, FUWAMOCO and Cecilia; Shiori's "AKUMA" and "Suspect" with Kiara and Ayunda Risu; Bijou's solo "Dead Ma'am's Chest"; Justice's first group performance at an in-person concert venue in 3D, "ABOVE BELOW"; Cecilia's "Wind-Up," the first Justice solo number of that concert, Raora's "Gacha×Gacha ADVENTURE!," Elizabeth's "Stellar Stellar" and Gigi's "Wonky Monkey"; "ALiCE&u" by Nerissa, Elizabeth and Ayunda Risu; "I'm Your Treasure Box" by Bijou, Cecilia and Raora [Official S9]), "Serendipity" (2026-07-03/04, Shrine Auditorium, Los Angeles), the last built around partner pairs (among them Calli–Shiori, Kronii–Ina, Kiara–Bijou, IRyS–Hakos Baelz and Nerissa–Elizabeth Rose Bloodflame, FUWAMOCO–Raora and Gigi–Cecilia), each with a published interview. Official report (S11): units Last Writes (Calli & Shiori, "When My Devil Rises"), Octo'clock (Ina & Kronii, "Bad Apple"), Rocku Wawa (Kiara & Bijou, "Tententengoku Jigokukoku"), BaeRyS (IRyS & Bae, "LUVATORRRRRY!"), Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"), B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari"), Autofister (Gigi & Cecilia, "CCGG MADNESS"); guests Ookami Mio ("Dottabatta Chindouchuu" with Ina and FUWAMOCO; "Night Loop" with IRyS and Bijou), Kobo Kanaeru ("HELP!!" with Bae and Elizabeth; "BLUE CLAPPER" with Kronii and Nerissa), Vestia Zeta ("Break It Down" with Shiori and Cecilia; "MAKE IT, BREAK IT" with FUWAMOCO and Gigi) and Tsunomaki Watame ("Cloudy Sheep" with Calli and Cecilia; "What an amazing swing" with Kiara and Raora); group stages: Myth and Promise medleys, Advent's "What Goes Around," Justice's "SUPERNOVA SUPER GIRL," the Advent+Justice medley ("Rebellion," "ABOVE BELOW"), Myth and Promise's "Kirameki Rider – English ver.," and all fifteen on "Serendipity" (its first performance) and "All for One." The report lists selected performances, not a full setlist. Dates are US local time. [Observed S1; character files C11, K4, I7, T10; Official S5, S6]
- `bible/world/Concerts-and-Live-Events.md › Recurring Events`: - **World tours:** "hololive STAGE World Tour'24 -Soar!-" (AZKi, Tsunomaki Watame, Moona Hoshinova, Kobo Kanaeru, Takanashi Kiara, Ninomae Ina'nis, Hakos Baelz): New York (Anime NYC, 2024-08-23, a day before and separate from "-Breaking Dimensions-"), Jakarta (11-09), Singapore (11-30, with a pre-concert panel of Kaela Kovalskia and Ouro Kronii), Atlanta (12-15, a panel of Nerissa and Elizabeth Rose Bloodflame), Kuala Lumpur (12-21, Nerissa and Elizabeth again) and Taipei (2025-01-18, the finale) [Official S7]; and "World Tour'25 -Synchronize!-" led by Momosuzu Nene, Kureiji Ollie, Mori Calliope, IRyS and Nerissa Ravencroft, with two guests per city (Ouro Kronii and Hakos Baelz in Sydney; Tokino Sora and Sakura Miko in Hong Kong). [Observed S1 §2024, §2025]
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Mori Calliope | Solo concert "New Underworld Order" (2022-07-21); "GriMoire" at the Hollywood Palladium (2025-02-26), the first solo concert by a hololive production talent outside Japan; World Tour '25 lead; Serendipity with Shiori | Calli file C6, C19, C11; S1 |
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | Nerissa Ravencroft | 6th fes day 1 (2025-03-08); 3D concert "Requiem for Love – A JukeBox Musical" (2025-05-24, with Calli and IRyS as guests); Advent's "On the Run!" (2025-08-29); World Tour '24 panels with Elizabeth (Atlanta, Kuala Lumpur); World Tour '25 lead; Serendipity with Elizabeth | Nerissa file N2, N3; S1 |
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 2. IRyS counts down to her first solo concert in Tokyo; Kronii and Calli send messages.
- `bible/world/Concerts-and-Live-Events.md › Conflicts and Story Hooks`: 5. A tour stop in Sydney: Kronii joins Calli, IRyS and Nerissa as a guest.

### from Cross-Branch Friends
- `bible/world/Cross-Branch-Friends.md › [SW] Other Names`: Death Star, MoRikka, LYRA, Holodeath, PavoNashi, HOLOTORI, UMISEA, HoloJEI, TakoNeko, K.I.R.A, OKFAIR, Star Flower, IRySora, soranii, Apex Predators, KoMeHa, BLUE·MEGAMISAMA, V3LVET
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones"
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: ("MoRikka"); with Niko, Risu, Kanata and Elizabeth she sang a "III" remix cover as "LYRA"; Kobo Kanaeru calls Calli "Uncle Dad" and Kiara "Mommy Kiwawa."
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Mori Calliope:** Hoshimachi Suisei is the senpai she is starstruck by ("Death Star"): she drew her ("DRAWING MY SENPAI," 2021), Suisei featured at Calli's first solo concert ("Wicked," 2022), they talked live shows together (2023), and Calli hosts watch parties of Suisei's concerts ("We're Screaming Loud for Senpai!", 2024-11). Kobo Kanaeru calls her "Uncle Dad" ("Father Daughter GOLF," 2022; an in-person cooking-and-gaming collab, 2023). Units: "Holodeath" (with Kureiji Ollie); "LYRA," a five-singer cover of "III" with Koganei Niko, Ayunda Risu, Amane Kanata and Elizabeth (Kanata has since graduated); "MoRikka" with HOLOSTARS' Rikka (their song "spiral tones," 2021; fans "DeadTuners") [Official music entry S5]. Outside hololive: friends with Milky Queen, whom she credits for introducing her to VTubers, and Ironmouse (a shared Underworld theme). [Observed S1 titles; S2 Calli §Relationships; Calli file]
- `bible/world/Cross-Branch-Friends.md › How It Works in Stories`: - Senpai and kouhai describe relative seniority (who debuted first), not language or nationality; forms of address and levels of formality vary by relationship. Some EN members are openly starstruck by particular senpai (Calli by Suisei, Kiara by Pekora, Nerissa by Marine). [Observed character files]
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 1. Calli hosts another watch party for Suisei's concert and loses her composure on the high note.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Calli's senpai: Suisei. Kiara's oshi: Pekora. Nerissa's oshi: Marine (and Kiara).

### from FUWAMOCO
- `bible/world/FUWAMOCO.md › [SW] Description`: Close to all of Advent (with Nerissa as the self-declared third sister, "Mofufu"), to Mori Calliope ("FUWAMOCALLI," a collaboration name the twins say they particularly like), to Raora Panthera (B.F.F, their 2026 concert unit), and to JP seniors including their oshi Houshou Marine (Fuwawa) and Omaru Polka (Mococo).
- `bible/world/FUWAMOCO.md › [SW] Rules`: A collab one twin joins alone (such as Fuwawa's 2026 trio with Calli and Gigi) is not a FUWAMOCO appearance.
- `bible/world/FUWAMOCO.md › Shared Relationships`: - **Myth and Promise:** "FUWAMOCALLI" with Mori Calliope (a twin game show and Smash in 2023, a tea party, an off-collab karaoke in 2024); Fuwawa also joined Mori Calliope and Gigi Murin for a 2026 BOMBANANA collab ("2 Creatures + 1 Reaper"; Fuwawa's post, not a twin appearance); "Detective Dogs" with Watson Amelia (Escape Simulator, 2024-09-24); "WatchDog" with Ouro Kronii; "Fuwamoomco" with Nanashi Mumei (Overwatch, 2025-03-01); they helped Ceres Fauna on her last World Tree stream (2024-12-31); Kiara hosted them on HOLOTALK (2023). [Observed S1; S3; Mumei, Calli, Kiara archives]

### from Fauna and Mumei Pairs
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Mumei also drew with Ina, did "Anatomy Review" with Calli, played with Ame in Ame's last regular week, and held "emo hours" with Nerissa; at the 2024 concert Mumei sang with Kiara and Nerissa, and Fauna with Shiori and Nerissa.
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Calli:** "ANATOMY REVIEW with Calli + Sana + Mumei" (2022), a drawing bit Mumei brought back on her own in 2025. [Observed S1]

### from IRyS and Nerissa Pairs
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Other Names`: MorIRyS, CHADCast, KiaRissa, IRyS and Kronii, IRyS and Ina, Nerissa and Calli, Nerissa and IRyS
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: IRyS and Calli: Calli collabed with her on July 29, 2021, eighteen days after IRyS's debut; with Bae they host CHADCast ("Chaos, Hope, and Death!"), and they still team up (Silent Hill 2 as "Two Pink Women," karaoke).
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: Nerissa and Calli: a Baldur's Gate 3 party, the 2025 duet "OVER//RIDE," and Calli as a guest at Nerissa's 3D concert.
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Rules`: Recent pairings (IRyS with Kronii, Calli and Ina; Nerissa with Kiara and Calli) carry the most weight; pairs with Gura are memories.
- `bible/world/IRyS-and-Nerissa-Pairs.md › IRyS`: - **IRyS and Calli** (16 / 16 / 5 / 8 / 2 / 1): Calli's first collab with her came on July 29, 2021, eighteen days after IRyS's debut ("Just Irystocrats and DeadBEATS"), then a karaoke collab (2021-10). With Hakos Baelz they host CHADCast ("Chaos, Hope, and Death!", from 2022-01-30; a 2025 episode: "We Went to a Hot Spring Together!!"). Later: "Two Pink Women Roll Up to Silent Hill" (2024-10-26), IRyS as Calli's HOLOMELO RADIO guest (2024-07), an off-collab karaoke with Momosuzu Nene (2025-04-23). Wiki unit: "MorIRyS." [Observed S1 titles; S2 IRyS §Relationships, secondary]
- `bible/world/IRyS-and-Nerissa-Pairs.md › Nerissa`: - **Nerissa and Kiara ("KiaRissa")** (15 / 12 / 3 / 0): Kiara is Nerissa's oshi; in Nerissa's lore she worked at KFP before hololive . "Compatibility test with Kiara-senpai" (2023-08-14); Kiara showed her around the EN Minecraft server (2023-09-07); their Baldur's Gate 3 party with Calli and Bijou ("Killing, Two Birds, with One Stone," 2023); "Rating your CARS with NERISSA" (2023-10-21); "GIRLSTALK with Nerissa, EN BIRB GIRLS PARTY!" (2025-04-08); a CHICAGO watchalong "with the musical connoisseur Nerissa" (2025-07-09). [Observed S1 titles; S3 Nerissa §Relationships, §Lore, secondary]
- `bible/world/IRyS-and-Nerissa-Pairs.md › Nerissa`: - **Nerissa and Calli** (6 / 7 / 3 / 1): the BG3 party (2023); Calli's "I Gathered 8 Cute People to Destroy their Friendships" (Mario Party, 2024-11); Calli as guest at Nerissa's 2025 3D concert ("Bocca della Verità"); the duet "OVER//RIDE – Mori Calliope × Nerissa Ravencroft" (2025-07-18); Nerissa as HOLOMELO RADIO guest (2025-07); Nerissa sang charity karaoke for #GOLIVEforLOVE (2026-02-17). Nerissa was Calli's first Instagram follower. [Observed S1 titles; S3, secondary]
- `bible/world/IRyS-and-Nerissa-Pairs.md › History`: | 2021-07-29 | Calli's first collab with IRyS | MorIRyS |
- `bible/world/IRyS-and-Nerissa-Pairs.md › History`: | 2025 | Nerissa's 3D concert with Calli and IRyS as guests; "OVER//RIDE" duet | Calli × Nerissa |
- `bible/world/IRyS-and-Nerissa-Pairs.md › Conflicts and Story Hooks`: 1. CHADCast records an episode while Calli and IRyS disagree on what counts as "chad."
- `bible/world/IRyS-and-Nerissa-Pairs.md › Conflicts and Story Hooks`: 4. Calli and Nerissa rehearse a duet; Calli's flow meets Nerissa's flirting.
- `bible/world/IRyS-and-Nerissa-Pairs.md › Hard Facts`: - CHADCast = IRyS, Calli, Bae. KiaRissa = Kiara and Nerissa. IRyS and Kronii are -Promise- genmates.

### from Justice Pairs
- `bible/world/Justice-Pairs.md › [SW] Description`: With seniors: Gigi repeatedly uses Calli's full name and jokes about getting her into League of Legends; within HoloEU, Raora teaches Kiara Italian and Cecilia speaks German with her; Cecilia plays up a rivalry with Ina; Kronii is Raora's "Pizza Time" collaborator and Gigi's Fatal Fury and Hytale partner, and secondary accounts record Kronii's "CLANKER" joke and Cecilia's "Owo-senpai"; Automatowl names Cecilia and Mumei.
- `bible/world/Justice-Pairs.md › [SW] Description`: Beyond EN: Elizabeth plays with Kureiji Ollie and HOLOSTARS members in varying lineups (Code Red games; Marvel Rivals with Crimzon Ruze, her "Nephew" in an uncle–nephew bit) and sang LYRA's "III" with FLOW GLOW's Koganei Niko; Kaela appears in Raora's fictional basement bit; Elizabeth records covers with JP members; Cecilia plays games with Tokino Sora; at Serendipity, Elizabeth sang with Kobo Kanaeru, Gigi and Cecilia with Vestia Zeta, and Cecilia and Raora with Tsunomaki Watame.
- `bible/world/Justice-Pairs.md › With Advent`: - **Shiori:** Elizabeth ("NovelFlame," "BloodQuill"; secondary) and Gigi voice parts in Shiori's non-canon motion comic "Into The Void" (2026; episode 2 also credits Calli); Gigi ("NovelGrem") games with her often (Heave Ho, a Fateful Findings watchalong, Project Zomboid, Phasmophobia; Eden Eternal was Kiara, Shiori and Gigi); the "Fanfic Club" (Gigi, Shiori, Pavolia Reine, Airani Iofifteen) is a separate group from "GAGA" (Gigi, Cecilia, Shiori, Bijou); Raora: a 2024 outfit-design collab (2024-12-05) and Blood Typers with Kronii and Bijou (2025-06-10); Cecilia: "Break It Down" with Vestia Zeta at Serendipity; Gigi: "MONSTER" with Ina and Kronii at -All for One-. [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Advent`: - **FUWAMOCO:** Raora is their Serendipity unit partner in B.F.F (official billing, "Inu Neko. Seishun Massakari"), who drew them a shikishi before debut and gave it "with big tears in her eyes"; the twins met Justice before debut to give advice; Gigi and Cecilia guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit ("GigiMoco" and "Cecemoco" are pair labels with Mococo); Cecilia played Chrono Trigger with Mococo, including 2026 off-collabs; Gigi sang "Bright Tonight" (2025) with the twins, IRyS and Kronii, and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity; Fuwawa, Gigi and Calli as "2 Creatures + 1 Reaper" (2026, Fuwawa alone); the twins sang in Elizabeth's 2026 birthday cover "CHA-LA HEAD-CHA-LA" with Polka, Nene, Watame and Iroha. [Official S3 interview03] [Observed S1; S2]
- `bible/world/Justice-Pairs.md › With Myth`: - **Mori Calliope:** Gigi's "Grem Reaper": Mouthwashing (2024-11-14), Fast Food Simulator (2025-02-04), R.E.P.O. (2025-05-02), The Boba Teashop (2025-06-04); Gigi shouts her full name ("MORI CALLIOPE!") and has jokes about getting Calli to play League of Legends (secondary observation). Unverified: Calli reportedly said Gigi changed how she felt about her talent name (kept off the card). Raora hit 500k during Galaxy Burger with Calli (2025-03-26), and Raora, Gigi and Calli played Elden Ring Nightreign (2025-06-11). Elizabeth surprised Calli with a TakaMori skit at debut, and they are fellow LYRA vocalists on a remix-version cover of "III" (with Kanata, Niko and Risu). Cecilia sang "Cloudy Sheep" with Calli and Tsunomaki Watame at Serendipity. [Observed S1; S2] [Official S7]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **ID:** Kaela Kovalskia with Raora ("SMITTEN," "Graondstone," "PizzaTimeSmith" with Kronii; in Raora's lore Kaela lives in her basement); Kureiji Ollie is Elizabeth's "kami-oshi" per public-profile wikis (collabs with HOLOSTARS members in varying lineups, including Code Red games; "High Tide" with Kronii at -All for One-), and Ollie did a chat-and-art collab with Raora (2024-09-06); Moona Hoshinova with Raora ("V3LVET"); Anya Melfissa visited Raora (2025-02-11); Vestia Zeta and Haachama in a Mario Party off-collab with Raora (2024-10-08); Ayunda Risu with Elizabeth ("LYRA," "ALiCE&u"); Vestia Zeta sang "Giri Giri" with Elizabeth at her 2025 3D showcase, which Elizabeth arranged and choreographed [ASR, Elizabeth file EB20]; Pavolia Reine and Airani Iofi with Gigi in the "Fanfic Club"; Kobo Kanaeru calls Elizabeth "Lilis" (secondary) and sang "HELP!!" with Elizabeth and Bae at Serendipity; Vestia Zeta also sang "Break It Down" with Cecilia and Shiori and "MAKE IT, BREAK IT" with Gigi and FUWAMOCO at Serendipity. [Observed S1; S2] [Official S6, S7]
- `bible/world/Justice-Pairs.md › Beyond EN`: - **JP:** Elizabeth's 2026 birthday covers, recorded at COVER's studio, featured Oozora Subaru; Roboco, Tokino Sora and Yuzuki Choco; Houshou Marine and Inugami Korone ("IT'S LOVE," iwnHChZq0N8, credits read by Claude); FUWAMOCO with Polka, Nene, Watame and Iroha; her 2026 "Yona Yona Dance" cover mixed branches (Natsuiro Matsuri, Hiodoshi Ao, Ollie and HOLOSTARS members). Cecilia played Minecraft and Super Mario 3D World with Tokino Sora (2025-02); Raora played Clubhouse Games with Haachama (2024-08-16), sang "Neko Kaburi-Na" with Ina, Shiori and guest Subaru at -All for One-, is "RaoRiRi" with Ichijou Ririka; "OkaGigi" is a secondary-documented name for Gigi and Nekomata Okayu, with no concrete shared activity sourced (dossier only). Tsunomaki Watame sang "Cloudy Sheep" with Calli and Cecilia and "What an amazing swing" with Kiara and Raora at Serendipity. FLOW GLOW: Koganei Niko sang with Elizabeth in LYRA. [Observed S1; S2] [Official S6, S7]
- `bible/world/Justice-Pairs.md › History`: | 2026-07-03/04 PDT | Serendipity: units Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora); guests' songs with Justice members: "HELP!!" (Kobo, Bae, Elizabeth), "Break It Down" (Zeta, Shiori, Cecilia), "Cloudy Sheep" (Watame, Calli, Cecilia), "MAKE IT, BREAK IT" (Zeta, FUWAMOCO, Gigi), "What an amazing swing" (Watame, Kiara, Raora) | [Official S3, S7] |
- `bible/world/Justice-Pairs.md › Conflicts and Story Hooks`: 3. Gigi tries to get Mori Calliope into League of Legends one more time, with Kiara as backup.

### from Myth and Kronii: Other Pairs
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Other Names`: Kiara and Ame, Ame and Kiara, Kiara and Gura, Gura and Kiara, Calli and Ina, Ina and Calli, Calli and Ame, Ame and Calli, Ina and Ame, Ame and Ina, Ina and Gura, Gura and Ina, Kiara and Kronii, Kronii and Kiara, Gura and Kronii, Kronii and Gura
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Calli and Ina: Ina designed Death Sensei and drew Calli's debut EP cover; Calli wrote the lyrics of Ina's "TAKO∞TAKOVER"; Calli is a recurring target of Ina's puns ("Every freaking time, Ina.").
- `bible/world/Myth-and-Kronii-Other-Pairs.md › [SW] Description`: Calli and Ame: early Clubhouse 51 duels; in 2026 Ame "called in from 2021" to Calli's charity stream.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Calli and Ina** (26 / 26 / 8 / 15 / 8 / 9; 2 in 2026): Ina designed Calli's Death Sensei and drew the cover of Calli's debut EP; Calli wrote the lyrics of Ina's 2026 song "TAKO∞TAKOVER." Calli is a recurring target of Ina's puns ("Every freaking time, Ina."). They watched Suisei's concert together in an off-collab (2023-02-20) and still game together (Elden Ring Nightreign, 2025-06). [Observed S5 Ina §Miscellaneous; Calli file C28; Ina file I8; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Calli and Ame** (24 / 23 / 14 / 6 / 6 / 0): early Clubhouse 51 duels; the MV of Calli-written "Myth or Treat" premiered on Ame's channel (2021); in 2026 Ame "called in from 2021" during Calli's charity stream. [Observed Ame file A20; S3 §2021, §2026, secondary; S1]
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2026-01-08 | "TAKO∞TAKOVER" digital release (lyrics by Calli) | Ina × Calli |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Conflicts and Story Hooks`: 3. Calli writes lyrics for Ina and Ina draws the cover; each critiques the other's draft.
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Hard Facts`: - Ina designed Death Sensei, Bubba and the Takodachi; Calli wrote "TAKO∞TAKOVER."

### from Octo'Clock
- `bible/world/OctoClock.md › Conflicts and Story Hooks`: 2. Ina quietly claims Kronii "all to myself" in front of Calli; Kronii plays along deadpan.

### from Time Duo
- `bible/world/Time-Duo.md › How It Works`: - **On stream (archive, S1):** Ame's surprise karaoke off-collab with Ina, Kronii, Fauna and Mumei (2022-02-25, per S3); 5D Chess "I Don't Understand With @WatsonAmelia" (Kronii, 2023-04-08); Escape the Backrooms with Calli (2024-09-22) and Deep Rock Galactic with Kiara and Gura (2024-09-30, Ame's last week of regular streams).

### from Time and Death
- `bible/world/Time-and-Death.md › [SW] Other Names`: Calli and Kronii, Kronii and Calli
- `bible/world/Time-and-Death.md › [SW] Description`: Mori Calliope and Ouro Kronii, the reaper and the Warden of Time: two low-voiced, deadpan sparring partners.
- `bible/world/Time-and-Death.md › [SW] Description`: Kronii's first official collaboration partner outside her own generation was Calli (2021).
- `bible/world/Time-and-Death.md › [SW] Description`: Calli calls her "Kronster"; their avatar heights are 168 cm and 167 cm, and Kronii never lets her forget the one centimeter.
- `bible/world/Time-and-Death.md › [SW] Description`: Their humor is mock feuds: when Kronii streamed a joke promotion of a made-up "$KRONII" coin in 2025, Calli answered with a mock exposé, "Exposing the Lies of $KRONII Coin"
- `bible/world/Time-and-Death.md › [SW] Rules`: Kronii's schemes and Calli's exposés are bits, never real accusations.
- `bible/world/Time-and-Death.md › How It Works`: - **First contact:** Kronii's first official collab outside her own generation was with Calli (Orcs Must Die! 3, 2021-09-23). [Observed S2 §2021, secondary]
- `bible/world/Time-and-Death.md › How It Works`: - **Nicknames and running jokes:** Calli calls her "Kronster"; their avatar heights are 168 cm (Kronii) and 167 cm (Calli), supplying a recurring one-centimeter joke. [Observed S2 infobox and §Miscellaneous, secondary, citing Kronii's post]
- `bible/world/Time-and-Death.md › How It Works`: - **Voices:** the wiki compares Kronii's deep voice to Calli's; in Claude's audio measurements they are the two lowest speakers of the six (Kronii 177–188 Hz, Calli 197–214 Hz in chat). [Observed S2 §Personality, secondary; ASR, Kronii file K36, Calli file C30]
- `bible/world/Time-and-Death.md › How It Works`: - **Their self-billing:** Calli's 2023 stream title "Time and Death Say Howdy to Ghosts...with @OuroKronii." Historically they shared the fan unit "WARS" (Warden, Alchemist, Reaper, Scholar) with HOLOSTARS' Magni Dezmond and Noir Vesper, who have both since left; scenes with them belong before their departures. [Observed S1; S2 §Relationships, secondary]
- `bible/world/Time-and-Death.md › How It Works`: - **Mock feuds:** in January 2025, after Kronii's channel was briefly hacked to promote cryptocurrency, Kronii streamed a joke promotion of a made-up "$KRONII" coin, and Calli answered with a mock exposé, "Exposing the Lies of $KRONII Coin" ("I called out Ouro Kronii for her dubious scam…"). The coin is a parody, not a real financial offering. [Observed S1; S2 §Miscellaneous, secondary]
- `bible/world/Time-and-Death.md › How It Works`: - **How often (archive, S1):** mentions per year 8 (2021), 8 (2022), 13 (2023), 4 (2024), 2 (2025). In 2023 this was one of Calli's most frequent pairings. [Observed S1; counts by Claude]
- `bible/world/Time-and-Death.md › History`: | 2025-01 | The "$KRONII" coin bit and Calli's mock exposé | Mock feud |
- `bible/world/Time-and-Death.md › Conflicts and Story Hooks`: 2. Kronii launches another fake scheme; Calli investigates on stream.
- `bible/world/Time-and-Death.md › Conflicts and Story Hooks`: 4. A TTRPG session: Calli as GM, Kronii as the player who breaks the plot.
- `bible/world/Time-and-Death.md › Conflicts and Story Hooks`: 5. A quiet moment after a collab where Kronii says thanks plainly and Calli doesn't know what to do.
- `bible/world/Time-and-Death.md › Hard Facts`: - First cross-generation collab for Kronii: with Calli, 2021-09-23.
- `bible/world/Time-and-Death.md › Hard Facts`: - Kronii is 1 cm taller than Calli.

### from VTuber Persona and Lore
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They use it as a joke engine: age jokes (Gura's "9,000-something," Kronii jokingly "60"), immortality and rebirth gags (Kiara), "canonically" framed bits (Ame calling in "from 2021" during Calli's 2026 charity stream). [Observed character files; Ame's wiki page §2026, secondary]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - They can re-enter it for a bit and drop it again: Calli's reaper threats, Ina's "priestess" voice, Kiara's KFP manager routine, Ame's "Trust me, I'm a time traveler." [Observed character files]
- `bible/world/VTuber-Persona-and-Lore.md › How It Works`: - **Normal example:** Calli jokes that she'll collect a guest's soul, the guest laughs, and Calli goes back to arguing about snacks. Nobody's soul is collected.
- `bible/world/VTuber-Persona-and-Lore.md › The Performer Behind the Avatar`: - Relationships are friendships and public bits. Ships (e.g. TakaMori) are performed bits and fan terms, not real romance. Intimacy is not written. [Project rule]

### from hololive -Advent-
- `bible/world/hololive--Advent.md › [SW] Description`: (2026), and 2026 Serendipity pairs Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth and FUWAMOCO–Raora.
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
- `bible/world/hololive--Myth.md › History`: | 2021-10-31 | "Myth or Treat" (lyrics by Calli) | First group song |
- `bible/world/hololive--Myth.md › History`: | 2025-04-30 | Myth relay "one last time" with Calli, Kiara, Ina and Gura before Gura's graduation | Gura's farewell with Myth |
- `bible/world/hololive--Myth.md › History`: | 2025-09-13 | 5th anniversary collab with announcements (Calli, Kiara, Ina) | New anniversary hats |
- `bible/world/hololive--Myth.md › History`: | 2026-09-19 (announced) | Myth 6th Anniversary 3D LIVE "Seasons From Within" announced with Calli, Kiara and Ina (S3, an official hololive English post); not verified as held | The current three, as announced |

### from hololive -Promise-
- `bible/world/hololive--Promise.md › How the Group Works`: - **Kronii's first official collab outside her generation** was with Mori Calliope (2021-09-23). [Observed Kronii's wiki page §2021, secondary]

### from hololive History 2023-2026
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: Nerissa and Gura's "Scarlet Wand"); EN's 2nd concert in New York; Ame concludes regular activities and stays an affiliate (09-30); in November COVER names this "conclusion of streaming activities." 2025: Fauna (01-03), Mumei (April) and Gura (05-01) graduate; Calli, IRyS and Nerissa lead World Tour '25 "-Synchronize!-" with Kronii and Bae as Sydney guests; Ina, IRyS and Bijou star at hololive night at Dodger Stadium (07-05); Justice's 3D showcases (August) and their first in-person concert stage at EN's 3rd concert, Radio City. 2026: Kiara and Ina's duo concert "Drawn to Dawn"; Justice's second-anniversary live "How to Protect JUSTICE!"
- `bible/world/hololive-History-2023-2026.md › [SW] Description`: (June); EN's 4th concert "Serendipity" in Los Angeles (July), built on units such as Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS, Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora) and Autofister (Gigi–Cecilia); on 2026-09-07 the female-talent branches unify under "hololive"; the new unit ASOBI★MAWARI-TAI! debuts (09-24/25); IRyS's first solo concert is set for 2026-10-06 in Tokyo.
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2025-04 | World Tour '25 "-Synchronize!-" announced, led by Momosuzu Nene, Kureiji Ollie, **Mori Calliope, IRyS and Nerissa Ravencroft**, with guests per city (Kronii and Bae in Sydney) | Three of the cast on one tour |
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2026-07-03/04 PDT | **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) | The current partnerships |
- `bible/world/hololive-History-2023-2026.md › Conflicts and Story Hooks`: 3. During a fictional public tour panel, Calli, IRyS and Nerissa compare their stage personas.

### from hololive History to 2022
- `bible/world/hololive-History-to-2022.md › [SW] Description`: The shared past the cast remembers. 2017: Tokino Sora makes COVER's first broadcast. 2018–2019: the Japanese generations debut (1st gen, 2nd gen with Aqua and Shion, GAMERS, 3rd gen "Fantasy" with Pekora and Marine, 4th gen with Coco and Kanata); AZKi debuts in 2018 and joins Suisei under INoNaKa Music in 2019, and Suisei moves to the main branch; the male group HOLOSTARS starts in 2019 (Rikka among its first generation); in late 2019 hololive, HOLOSTARS and INoNaKa Music become "hololive production." 2020: the Indonesian branch opens; on 2020-09-12/13 hololive English -Myth- debuts (Calli first, then Kiara, Ina, Gura, Ame); Gura becomes the first hololive member to reach a million subscribers (2020-10-22: "I am an overwhelmed, but very happy shark") and in 2021 the most-subscribed VTuber anywhere; by 2021-05-30 all of Myth pass a million. 2021: IRyS debuts as Project: HOPE's VSinger (07-11), -Council- debuts with Kronii, Fauna and Mumei (08-23), holoX debuts, Coco graduates. 2022: ID gen 3 (Kobo, Zeta, Kaela), Calli and Kiara perform at hololive 3rd fes.
- `bible/world/hololive-History-to-2022.md › [SW] Description`: "Link Your Wish" in Makuhari (03-20; Kiara: "MAKUHARI WAS ON FIRE!"), HOLOSTARS adds the unit UPROAR!! and the English group -TEMPUS-, holoMeet starts with Gura as ambassador, Calli holds her first solo concert (07-21), and Sana graduates (07-31).
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019-05-19 | AZKi and Hoshimachi Suisei (formerly independent) join under the INoNaKa Music label; Suisei moves to hololive's main branch on 2019-12-01 | Calli's starstruck senpai Suisei |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019-06 / 09 | HOLOSTARS, COVER's male group, starts (1st gen, incl. Rikka); 2nd gen in December | Calli's MoRikka partner |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019 | 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins | Kiara's oshi Pekora; Nerissa's oshi Marine; Calli's starstruck senpai Suisei |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2020-09-12/13 | **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame | The cast's origin |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-03-20 | hololive 3rd fes. "Link Your Wish" at Makuhari (#つながるホロライブ), day 2: Calli and Kiara perform | Calli: "My dream came true, my heart is exploding." Kiara: "MAKUHARI WAS ON FIRE!" [Observed—X posts, S4] |
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-07-18/23 | HOLOSTARS English -TEMPUS- (Regis Altare, Magni Dezmond, Axel Syrios, Noir Vesper) announced and debuts | Calli and Kronii's WARS partners Magni and Vesper |
- `bible/world/hololive-History-to-2022.md › Conflicts and Story Hooks`: 1. A Myth anniversary stream replays the 2020 debuts; Calli insists she was "first."

### from hololive
- `bible/world/hololive.md › [SW] Description`: (hololive production also includes HOLOSTARS), and old groups are units: Calli, Kiara and Ina are active in hololive -Myth-; Kronii and IRyS are in hololive -Promise-; Nerissa is in hololive -Advent-.
- `bible/world/hololive.md › How It Works`: - **Structure (as of 2026-09-30):** hololive production is COVER's brand, which also includes the male group HOLOSTARS; hololive is its female VTuber group. On 2026-09-07 COVER unified the former female-talent branches (hololive, hololive English, hololive Indonesia, hololive DEV_IS) under a single "hololive," an organizational and branding change it described as removing regional limits; members had already collaborated across branches for years; former groups keep their names as units (hololive -Myth-, -Promise-, -Advent-, -Justice-). Promotion is now done for all members in Japanese, Indonesian and English. [Official S6] [Observed S2 §2026, secondary, citing the hololive Next broadcast of 2026-09-07; project.md]
- `bible/world/hololive.md › How It Works`: - **Seniority:** senpai and kouhai describe relative seniority (who debuted first), not language or nationality; forms of address and levels of formality vary by relationship. Many EN members are openly starstruck by particular senpai (Calli by Suisei, Kiara by Pekora). [Observed character files]

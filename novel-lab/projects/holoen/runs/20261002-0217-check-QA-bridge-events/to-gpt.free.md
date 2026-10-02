# Task 05 — Cross-cohort bridge audit

You are GPT, senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only, answer in English,
and run sequentially without parallel GPT audits.

Bridge: events — must be events or ties
Packet: projects/holoen/research/qa/packets/events.md (inline below)
Registry: projects/holoen/research/qa/registry.json

## Binding rules and inputs

- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.

Read projects/holoen/project.md, framework/prompts/shared-rules.md, the packet,
registry, research/qa/manifest.json, research/qa/resolutions.md, and available
research/qa/audit-*.md reports relevant to the bridge. Reports outside runs are
permitted. Never read projects/*/runs/, even through links. Modify no files.

The baseline is 2026-09-30. Use later verification only to establish baseline-era
facts. Cover all 18 character and 24 world cards through relevant cross-file
claims. External participants may remain reference-only; create no new cards.

Use official fictional lore and public persona behavior only. Exclude performer
identity, private appearance, past activities, private life, health, real family,
breaks and reasons, trips, auditions, nationality and mother tongue. Public
disclosure does not remove these exclusions. Describe accents only as audible
features. Distinguish fictional families, avatar lore and in-game travel from
real-life information; public event locations do not establish personal travel.

No inferred intimate relationships, sexuality or hidden psychology; no lyrics,
long transcripts, explicit sexual content, real-voice cloning or identifiable
imitation. Preserve evidenced swearing and performed jokes without sanitizing
them. Label invented calibration lines “Style demonstration.”

Do not reopen isolated claims already reviewed unless they conflict across files.
This audit groups claims by shared event or relationship, checks previous fixes
and catches propagation failures. Broad recency research, X completeness and
detailed voice enrichment belong to tasks 06, 08 and 09. Newly encountered scope
violations must still be reported.

## Evidence and quotation

OFFICIAL means agency profiles, announcements, reports or official written copy.
Short exact written excerpts may be quoted; distinguish lore, announcements and
post-event reporting.

PRIMARY means firsthand public posts, streams or other public material.
Short written posts may be quoted as written. Audio-derived quotations require
the ASR gate below, regardless of channel ownership.

ARCHIVE_METADATA supports only its stated title, description, dates, listed
participants and credits. Quote it as metadata, never dialogue. Scheduled names
do not prove actual participation; upload time does not necessarily date the event.

SECONDARY means wikis, fan transcripts, clips or mirrors. Use attributed
paraphrases. Short quotations of secondary prose remain attributed to its author.
A fan’s transcript cannot establish the performer’s exact spoken words.

ASR is machine transcription, not listening. Spoken quotations require explicit
contiguous approved spans shared by two models transcribing the same public
audio window. Record source, timestamp, both models and separate speaker
attribution. Document punctuation/case normalization only; preserve wording,
repetitions and order. Never stitch separated spans or treat semantic agreement
as verbatim agreement. Two-model agreement cannot establish who spoke, tone,
relationship strength or recurring usage.

No lyrics; keep quotations brief and total external quotations within 25 words
per non-lyrical source. Distinguish Official setting, Public-behavior observation,
Author-approved adaptation and Unverified. Unverified assertions cannot enter
[SW] fields as facts.

Use local evidence first. Search live only to resolve disagreement or apparent
staleness; prefer official pages, then primary sources. Open supporting sources
before claiming fresh verification. Label inherited evidence “not reopened.”
Record inaccessible sources without treating inaccessibility as disproof.
Separate source publication date, event date and actual verification date.

## Common procedure

Check source hashes before auditing and reconcile changes before concluding.
Packets are focus aids: inspect permitted canonical files and related research
when necessary. Match canonical names, aliases and units; inspect complete
bullets/table rows and relevant pronoun antecedents. Report extraction gaps.

Group claims under stable registry keys across cohorts. Check the resolution
ledger before creating findings. Verify implemented changes against canonical
text; a “resolved” label alone proves nothing. Track all propagation destinations.

Treat the registry as an index requiring evidence, not an authority that overrides
sources. Preserve uncertainty and date precision rather than inventing detail.

## If bridge = events

Compare both histories, Concerts, unit cards, character timelines, Background,
Relationships and all other relevant exported claims.

Check event identity; announcement versus event dates; source time zones;
genuine multi-day schedules versus time-zone conversions; scheduled versus held
events; actual participants versus historical unit membership; debut, graduation
and affiliate intervals; date-bound organization names; release and performance
credits; milestone counts.

Do not infer current activity from an old appearance or current unit membership
from historical participation. A later guest appearance need not reverse an
affiliate/graduation status. Record exceptions with evidence.

Check status boundaries at the source’s supported precision. Never invent a
midnight transition or time zone. Describe factual departures without excluded
reasons. Flag optional coverage gaps separately from contradictory dates.

## If bridge = ties

Compare character Relationships and Groups, world descriptions and aliases,
Relationship Maps, concert units and incoming claims across every cohort.

Check canonical endpoints, unit membership, named-event context, official versus
fan/performed naming, alias ownership, and directional verbs: who invited,
supported, credited, performed with or publicly praised whom.

A collaboration supports participation, not private friendship strength.
Do not reverse directional claims, rank closeness by archive counts, infer mutual
feelings or convert a performed pairing into a real relationship.
A missing reciprocal mention is a coverage question, not automatically an error.

Keep multi-person unit aliases on suitable world cards and memberships in Groups;
do not make the unit an individual’s Other Names alias. Review collisions without
automatically deleting valid aliases. Keep Fuwawa and Mococo distinct.

## Priorities, decisions and IDs

P0: resolve before delivery—scope breaches, fabricated attribution, unapproved
spoken quotations, or defects preventing a trustworthy usable release.
P1: priority factual correction, material inconsistency or evidenced coverage gap.
P2: optional clarity, retrieval or usability improvement.

Finding priority does not determine validation severity by itself; material
contradictions can block even when P1.

“Author decision” is an explicit editorial choice between valid alternatives,
including optional enrichment or a disclosed limitation. It is neither GPT
approval nor factual verification, and cannot waive the current scope.
Recommend a concrete choice; handle routine corrections without escalation.

Use BR-{TYPE}-{NNN}: TYPE = DATE, STATUS, EVENT, ROSTER, TIE, CREDIT, UNIT, ALIAS,
SCOPE, QUOTE, VOICE, EXPORT or COVERAGE. Both bridge passes share this namespace.
Continue ledger numbering. Reuse cohort IDs for the same underlying issue;
create a new BR ID only for a distinct cross-cohort problem and link related IDs.

## Exact output format

Use exactly these four top-level headings:

## Coverage

Snapshot hash; packet/registry hashes; source-hash manifest reference; bridge;
files/fields and claim keys examined; cohort findings checked; exclusions;
unresolved evidence; missing inputs; snapshot changes.
Distinguish examined material from freshly verified evidence.

## Findings

| ID | Priority | Claim key | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|

One actionable finding per row; use linked patch rows for different replacements
under one ID. Supply exact old text and paste-ready replacements, or DELETE.
Escape pipes; represent internal newlines with <br>. If unsupported, recommend
deletion or limited wording rather than inventing a replacement. Write “None”
when there are no findings.

## New verified facts

Use the identical table columns; absent old text is “—”. Give insertion locators.
Include only useful facts verified during permitted checking. Distinguish
candidates from accepted additions. Otherwise write “None.”

## Merge handoff

List dependencies, unresolved conflicts, propagation order, registry updates,
and finding IDs recommended for acceptance, rejection, deferral or more evidence.
Do not claim edits were applied. Name downstream tasks needing the result.

End with “Open questions”: at most five genuine author decisions or unresolved
input questions, or “None.”


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

### Registry excerpt (units and reference-only people; query `projects/holoen/research/qa/registry.json` with `jq` for the rest)

```json
{
 "baseline": "2026-09-30",
 "commit": "c06ffa3",
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
 ],
 "reference_only": [
  "Hakos Baelz",
  "Tsukumo Sana",
  "Kobo Kanaeru",
  "Vestia Zeta",
  "Kureiji Ollie",
  "Kaela Kovalskia",
  "Moona Hoshinova",
  "Ayunda Risu",
  "Anya Melfissa",
  "Pavolia Reine",
  "Airani Iofifteen",
  "Ookami Mio",
  "Tsunomaki Watame",
  "Oozora Subaru",
  "Houshou Marine",
  "Inugami Korone",
  "Omaru Polka",
  "Momosuzu Nene",
  "Kazama Iroha",
  "Roboco",
  "Tokino Sora",
  "Yuzuki Choco",
  "Nekomata Okayu",
  "Shirakami Fubuki",
  "Hakui Koyori",
  "Akai Haato",
  "Hoshimachi Suisei",
  "Usada Pekora",
  "Shiranui Flare",
  "AZKi",
  "Amane Kanata",
  "Natsuiro Matsuri",
  "Ichijou Ririka",
  "Koganei Niko",
  "Hiodoshi Ao",
  "Machina X Flayon",
  "Jurard T Rexford",
  "Crimzon Ruze",
  "Gavis Bettel",
  "Banzoin Hakka",
  "Josuiji Shinri",
  "Arurandeisu",
  "Astel Leda",
  "Octavio",
  "Regis Altare",
  "Rikka",
  "Shirogane Noel"
 ]
}
```

### projects/holoen/research/qa/packets/events.md

# Bridge packet: events

Snapshot: git c06ffa3. Every dated row from every bible file's dossier
tables (registry events), grouped by month; then each cast member's status interval. Locators are files;
search the file for the row text to see its context.

## Status intervals (from Background)

- Cecilia Immergreen: active; debut 2024-06-22; graduated —; regular activities concluded — (`bible/characters/Cecilia-Immergreen.md › Background`)
- Ceres Fauna: graduated; debut 2021-08-23; graduated 2025-01-03; regular activities concluded — (`bible/characters/Ceres-Fauna.md › Background`)
- Elizabeth Rose Bloodflame: active; debut 2024-06-21; graduated —; regular activities concluded — (`bible/characters/Elizabeth-Rose-Bloodflame.md › Background`)
- Fuwawa Abyssgard: active; debut 2023-07-31; graduated —; regular activities concluded — (`bible/characters/Fuwawa-Abyssgard.md › Background`)
- Gawr Gura: graduated; debut ?; graduated 2025-05-01; regular activities concluded — (`bible/characters/Gawr-Gura.md › Background`)
- Gigi Murin: active; debut 2024-06-21; graduated —; regular activities concluded — (`bible/characters/Gigi-Murin.md › Background`)
- IRyS: active; debut 2021-07-11; graduated —; regular activities concluded — (`bible/characters/IRyS.md › Background`)
- Koseki Bijou: active; debut 2023-07-30; graduated —; regular activities concluded — (`bible/characters/Koseki-Bijou.md › Background`)
- Mococo Abyssgard: active; debut 2023-07-31; graduated —; regular activities concluded — (`bible/characters/Mococo-Abyssgard.md › Background`)
- Mori Calliope: active; debut ?; graduated —; regular activities concluded — (`bible/characters/Mori-Calliope.md › Background`)
- Nanashi Mumei: graduated; debut 2021-08-23; graduated 2025-04-27; regular activities concluded — (`bible/characters/Nanashi-Mumei.md › Background`)
- Nerissa Ravencroft: active; debut 2023-07-31; graduated —; regular activities concluded — (`bible/characters/Nerissa-Ravencroft.md › Background`)
- Ninomae Ina'nis: active; debut ?; graduated —; regular activities concluded — (`bible/characters/Ninomae-Inanis.md › Background`)
- Ouro Kronii: active; debut ?; graduated —; regular activities concluded — (`bible/characters/Ouro-Kronii.md › Background`)
- Raora Panthera: active; debut 2024-06-22; graduated —; regular activities concluded — (`bible/characters/Raora-Panthera.md › Background`)
- Shiori Novella: active; debut 2023-07-30; graduated —; regular activities concluded — (`bible/characters/Shiori-Novella.md › Background`)
- Takanashi Kiara: active; debut ?; graduated —; regular activities concluded — (`bible/characters/Takanashi-Kiara.md › Background`)
- Watson Amelia: affiliate; debut ?; graduated —; regular activities concluded 2024-09-30 (`bible/characters/Watson-Amelia.md › Background`)

## Dated rows by month

### 2017-09
- 2017-09-07 [day] Tokino Sora makes COVER's first VTuber broadcast — `bible/world/hololive-History-to-2022.md` ("Sora-senpai" is everyone's origin point)

### 2017-12
- 2017-12-21 [day] The "hololive" app launches — `bible/world/hololive-History-to-2022.md` (Where the name came from)

### 2018-05
- 2018-05 / 06 [month-range] hololive 1st generation debuts (Fubuki, Matsuri, Haato, Aki, Mel, Chris) — `bible/world/hololive-History-to-2022.md` (The first "gen")

### 2018-08
- 2018-08 / 09 [month-range] 2nd generation (Aqua, Shion, Ayame, Choco, Subaru); Sakura Miko debuts (2018-08-01) — `bible/world/hololive-History-to-2022.md` (Senpai the EN members grew up watching)

### 2018-11
- 2018-11-15 [day] AZKi debuts under COVER's management — `bible/world/hololive-History-to-2022.md` (—)

### 2018-12
- 2018-12 [month] hololive GAMERS (Fubuki, Mio; later Okayu, Korone) — `bible/world/hololive-History-to-2022.md` (Gaming senpai)

### 2019
- 2019 [year] 3rd gen "hololive Fantasy" (Pekora, Rushia, Marine, Flare, Noel); hololive China begins — `bible/world/hololive-History-to-2022.md` (Kiara's oshi Pekora; Nerissa's oshi Marine; Calli's starstruck senpai Suisei)

### 2019-05
- 2019-05-19 [day] AZKi and Hoshimachi Suisei (formerly independent) join under the INoNaKa Music label; Suisei moves to hololive's main branch on 2019-12-01 — `bible/world/hololive-History-to-2022.md` (Calli's starstruck senpai Suisei)

### 2019-06
- 2019-06 / 09 [month-range] HOLOSTARS, COVER's male group, starts (1st gen, incl. Rikka); 2nd gen in December — `bible/world/hololive-History-to-2022.md` (Calli's MoRikka partner)

### 2019-12
- 2019-12 [month] 4th gen (Coco, Kanata, Watame, Towa, Luna); hololive, HOLOSTARS and INoNaKa Music unite as "hololive production" — `bible/world/hololive-History-to-2022.md` (The modern brand)

### 2020
- 2020 [year] Constant collabs and pranks — `bible/world/AmeSame.md` (The "AmeSame" name)
- 2020–2021 [year-range] Constant collabs, pranks and bickering — `bible/world/Bone-Bros.md` ("Bone Bros")
- 2020 [year] Myth's first year: frequent collabs across time zones — `bible/world/Streaming-Life.md` (Collab-heavy early memories)
- 2020–2021 [year-range] Near-constant collabs: Minecraft, Among Us, games across time zones — `bible/world/hololive--Myth.md` (The "first year" memories)

### 2020-04
- 2020-04 [month] hololive Indonesia gen 1; hololive English auditions announced — `bible/world/hololive-History-to-2022.md` (The overseas branches)

### 2020-08
- 2020-08 [month] 5th gen (Lamy, Nene, Botan, Polka; Aloe graduated the same month) — `bible/world/hololive-History-to-2022.md` (The JP generation just before Myth)

### 2020-09
- 2020-09-13 JST [day, JST] Debuts in hololive English -Myth-, 12 minutes late, first word "a"; sings city pop and becomes "City Pop Shark" — `bible/characters/Gawr-Gura.md` ([Official G1] [Observed G2 §Miscellaneous; G4])
- 2020-09-12 [day] She debuts first in hololive English -Myth-. Her fans become the Dead Beats. — `bible/characters/Mori-Calliope.md` ([Official C1] [Observed C4 §Debut])
- 2020-09-13 [day] Debuts in hololive English -Myth- — `bible/characters/Ninomae-Inanis.md` ([Official I1])
- 2020-09-12 [day] Debuts in hololive English -Myth-, speaking English, Japanese and German — `bible/characters/Takanashi-Kiara.md` ([Official T1] [Observed T2 §Debut])
- 2020-09-13 JST [day, JST] Debuts in hololive English -Myth- ("The Investigation Begins"), briefly undercover with a fake British accent — `bible/characters/Watson-Amelia.md` ([Official A1] [Observed A3-MXrFrkIlE-0; A2 §Miscellaneous])
- 2020-09-16 [day] Reveals she is a time traveler (first Fall Guys stream) — `bible/characters/Watson-Amelia.md` ([Observed A2 §Time travel; A10 locator])
- 2020-09-28 [day] "Nothing beats a ground pound" (Super Mario Odyssey) — `bible/characters/Watson-Amelia.md` ([Observed A5])
- 2020-09 [month] Kiara declares the crush on Calli's 2nd stream; "TakaMori" named — `bible/world/TakaMori.md` (The ship name)
- 2020-09 [month] Myth debuts with official lore profiles — `bible/world/VTuber-Persona-and-Lore.md` (Lore bits still in use)
- 2020-09-12/13 [day-range] Myth debuts; Calli narrates Kiara's debut intro — `bible/world/hololive--Myth.md` (Kiara's intro art, Calli's narration)
- 2020-09-08 [day] hololive English announced; Myth's members appear on X — `bible/world/hololive-History-to-2022.md` ("Myth's birthday" season)
- 2020-09-12/13 [day-range] **Myth debuts:** Calli (first), Kiara, Ina, Gura, Ame — `bible/world/hololive-History-to-2022.md` (The cast's origin)
- 2020-09 [month] hololive English -Myth- debuts (first EN generation) — `bible/world/hololive.md` (Myth anniversaries every September)

### 2020-10
- 2020-10-22 [day] Gura becomes the first hololive member to reach 1 million subscribers — `bible/world/hololive-History-to-2022.md` (A Myth legend)

### 2020-11
- 2020-11 [month] HOLOTALK begins as a bilingual interview show — `bible/characters/Takanashi-Kiara.md` ([Official T9] [Observed T21])
- 2020-11-15 [day] Gura's chicken prank on KFP — `bible/world/Myth-and-Kronii-Other-Pairs.md` (KFP lore)
- 2020-11 [month] The KFP chicken incident; Kiara "fires" Ina — `bible/world/TakoTori.md` (KFP lore)

### 2020-12
- 2020-12 / 2021-03 [month-range] Japanese and German lessons with Kiara — `bible/characters/Gawr-Gura.md` ([Observed G13])
- 2020-12-10 [day] Channel briefly terminated, then restored; "#PhoenixDown" re-debut with a mock-amnesia bit ("Who's Calli?") — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §2020 and §Takamori; T5-le72UNZAbQI])
- 2020-12 [month] Repeated Sun Station landing attempts in Outer Wilds, later her favorite game — `bible/characters/Watson-Amelia.md` ([Observed A9; A2 §Likes and dislikes])
- 2020-12 [month] Kiara's amnesia re-debut: "Who's Calli?" — `bible/world/TakaMori.md` (Running gag)
- 2020-12 [month] ID gen 2 (Ollie, Anya, Reine); hololive China ends — `bible/world/hololive-History-to-2022.md` (K.I.R.A partners (Reine, Anya))
- 2020-12-10 [day] Kiara's channel briefly terminated, then restored ("#PhoenixDown") — `bible/world/hololive-History-to-2022.md` (A Kiara rebirth joke)

### 2021
- 2021–2026 [year-range] Lore grows through jokes, songs and events — `bible/world/VTuber-Persona-and-Lore.md` ("Canonically" callbacks)

### 2021-03
- 2021-03 [month] German lesson with Gura; the German "HoloDE Debüt" stream — `bible/characters/Takanashi-Kiara.md` ([Observed T15; T2 §2021])

### 2021-04
- 2021-04-01 [day] Smol Ame appears (April Fools) — `bible/characters/Watson-Amelia.md` ([Observed A2 §Smol Ame])

### 2021-05
- 2021-05 [month] The Fish Tank talk show with Ame — `bible/characters/Gawr-Gura.md` ([Observed G6])
- 2021-05 [month] The Fish Tank talk show with Gura — `bible/characters/Watson-Amelia.md` ([Observed Gura file G6])
- 2021-05 [month] The Fish Tank talk show — `bible/world/AmeSame.md` (Staged-argument comedy)
- 2021-05-30 [day] Kiara reaches 1 million: every Myth member is over 1 million — `bible/world/hololive-History-to-2022.md` (A Myth first)

### 2021-06
- 2021-06-22 [day] Original song "REFLECT" — `bible/characters/Gawr-Gura.md` ([Observed G2 §2021; G4])
- 2021-06-30 [day] Gura passes Kizuna AI as the most-subscribed VTuber — `bible/world/hololive-History-to-2022.md` (A Myth legend)

### 2021-07
- 2021-07-11 [day] Debuts as the sole member of hololive English -Project: HOPE-, a VSinger — `bible/characters/IRyS.md` ([Official R1] [Observed R2])
- 2021-07-29 [day] First official collab: Just Shapes & Beats with Mori Calliope — `bible/characters/IRyS.md` ([Observed R2 §2021])
- 2021-07-29 [day] Calli's first collab with IRyS — `bible/world/IRyS-and-Nerissa-Pairs.md` (MorIRyS)
- 2021-07-01 [day] Kiryu Coco graduates — `bible/world/hololive-History-to-2022.md` (—)
- 2021-07-11 [day] **IRyS debuts** as the VSinger of Project: HOPE — `bible/world/hololive-History-to-2022.md` (Hope arrives)

### 2021-08
- 2021-08-23 JST [day, JST] Debuts with hololive English -Council- (first post on X: "oh deer") — `bible/characters/Ceres-Fauna.md` ([Official F1] [Observed F4])
- 2021-08-23 JST [day, JST] Debuts with hololive English -Council- (first post on X: "oh man") — `bible/characters/Nanashi-Mumei.md` ([Official M1] [Observed M4])
- 2021-08 [month] The WAH acronyms begin (*Ender Lilies* streams) — `bible/characters/Ninomae-Inanis.md` ([Observed I2 §WAH])
- 2021-08-23 JST [day, JST] Debuts with hololive English -Council- — `bible/characters/Ouro-Kronii.md` (Fans become Kronies [Official K1])
- 2021-08-23 [day] Council debuts — `bible/world/Fauna-and-Mumei-Pairs.md` (Five concepts)
- 2021-08-25 [day] Fauna and Mumei's first co-op — `bible/world/Fauna-and-Mumei-Pairs.md` (Don't Starve Together: "Surviving in the wilderness with Mumei!")
- 2021-08 [month] Kronii's announcement; "a certain time lord" joke — `bible/world/Time-Duo.md` (The lore rivalry)
- 2021-08 [month] -Council- debuts (Sana, Fauna, Kronii, Mumei, Bae) — `bible/world/hololive--Promise.md` ("Council" nostalgia)
- 2021-08-23 [day] **-Council- debuts:** Sana, Fauna, **Kronii**, Mumei, Bae — `bible/world/hololive-History-to-2022.md` (Kronii's origin)
- 2021-08 [month] -Council- debuts (Kronii's generation) — `bible/world/hololive.md` (Council → Promise)

### 2021-09
- 2021-09-29 [day] The Minecraft "bento" that starts the BaeRyS married/divorced bit — `bible/characters/IRyS.md` ([Observed R2 §Relationships])
- 2021-09 [month] She and Calli announce they will tone down the TakaMori ship — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §Takamori])
- 2021-09-13 [day] Minecraft together — `bible/world/Fauna-and-Mumei-Pairs.md` ("Adventuring with Mumei!")
- 2021-09 [month] UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) — `bible/world/Myth-and-Kronii-Other-Pairs.md` (Ocean unit)
- 2021-09 [month] Flirt-and-rebuff routine toned down; still close friends — `bible/world/TakaMori.md` (Nicknames and couple jokes remain callbacks)
- 2021-09-23 [day] Orcs Must Die! 3: Kronii's first cross-generation collab — `bible/world/Time-and-Death.md` (The friendship's start)

### 2021-10
- 2021-10 [month] Minecraft "civil war" with Fauna — `bible/characters/Ouro-Kronii.md` ([Unverified, K29 clip titles])
- 2021-10-31 [day] "Myth or Treat" (lyrics by Calli) — `bible/world/hololive--Myth.md` (First group song)

### 2021-11
- 2021-11 [month] 6th gen "Secret Society holoX" (La+, Lui, Koyori, Chloe, Iroha) — `bible/world/hololive-History-to-2022.md` (—)

### 2022
- 2022 [year] CHADCast begins with IRyS and Hakos Baelz. — `bible/characters/Mori-Calliope.md` ([Observed C12])

### 2022-01
- 2022-01-17 [day] First original song "A New Start" — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2022])
- 2022-01-15 [day] Kimono reveal; introduces Boros — `bible/characters/Ouro-Kronii.md` ([Observed K8 §Mascots and fans, secondary])
- 2022-01-30 [day] First CHADCast — `bible/world/IRyS-and-Nerissa-Pairs.md` (Chaos, Hope, and Death)

### 2022-02
- 2022-02-03 [day] "Q" with Mori Calliope (DECO*27) — `bible/characters/Gawr-Gura.md` ([Official G15])
- 2022-02 [month] Nintendo Direct "TOMORROW?!" reaction — `bible/characters/Ninomae-Inanis.md` ([Observed I23])
- 2022-02-03 [day] "Q" (with DECO*27) — `bible/world/Bone-Bros.md` (Their duet)
- 2022-02-25 [day] Ame's surprise karaoke off-collab (with Ina, Kronii, Fauna, Mumei) — `bible/world/OctoClock.md` (—)
- 2022-02-24 [day] Uruha Rushia leaves hololive — `bible/world/hololive-History-to-2022.md` (Not discussed in stories)

### 2022-03
- 2022-03 [month] ID gen 3 (Zeta, Kaela, Kobo) — `bible/world/hololive-History-to-2022.md` (Kobo's "Mommy Kiwawa" and "Uncle Dad")
- 2022-03-20 [day] hololive 3rd fes. "Link Your Wish" at Makuhari (#つながるホロライブ), day 2: Calli and Kiara perform — `bible/world/hololive-History-to-2022.md` (Calli: "My dream came true, my heart is exploding." Kiara: "MAKUHARI WAS ON FIRE!" [Observed—X posts, S4])
- 2022-03-19 [day] HOLOSTARS announces the unit UPROAR!! — `bible/world/hololive-History-to-2022.md` (—)

### 2022-04
- 2022-04 [month] She signs with EMI Records / Universal Music Japan. — `bible/characters/Mori-Calliope.md` ([Observed C4 §2022, secondary])
- 2022-04-26 [day] holoMeet begins; Gura is an ambassador — `bible/world/hololive-History-to-2022.md` (Global events)

### 2022-05
- 2022-05-14 [day] First original song "Let Me Stay Here" — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2022])

### 2022-06
- 2022-06 [month] An off-collab; unarchived karaoke — `bible/world/AmeSame.md` (—)
- 2022-06 [month] Myth's first off-collab with all five present — `bible/world/Streaming-Life.md` (Off-collabs as special events)
- 2022-06 [month] "Reunion & Gaming!! #takamori" off-collab; karaoke collab — `bible/world/TakaMori.md` (In-person reunion)
- 2022-06-28 [day] First off-collab with all five together ("Together At Last") — `bible/world/hololive--Myth.md` (A treasured in-person memory)

### 2022-07
- 2022-07-21 [day] Her solo concert "New Underworld Order." — `bible/characters/Mori-Calliope.md` ([Official C6])
- 2022-07-31 [day] Sana graduates — `bible/world/hololive--Promise.md` (Council becomes four)
- 2022-07-18/23 [day-range] HOLOSTARS English -TEMPUS- (Regis Altare, Magni Dezmond, Axel Syrios, Noir Vesper) announced and debuts — `bible/world/hololive-History-to-2022.md` (Calli and Kronii's WARS partners Magni and Vesper)
- 2022-07-31 [day] Tsukumo Sana graduates — `bible/world/hololive-History-to-2022.md` (Council becomes four)

### 2022-08
- 2022-08 [month] Mumei accidentally blows up the Bunkeronii's entrance — `bible/characters/Ouro-Kronii.md` ([Unverified, K28 clip titles])

### 2022-09
- 2022-09-30 [day] "Non-Fiction" MV — `bible/world/hololive--Myth.md` (Group song)
- 2022-09 [month] hololive's 5th anniversary — `bible/world/hololive-History-to-2022.md` (—)

### 2022-10
- 2022-10 [month] "BAE & FAUNA'S MONTH OF HORRORS" — `bible/characters/Ceres-Fauna.md` ([Observed F4, F3])

### 2023
- 2023–2024 [year-range] FGO streams on Ina's channel — `bible/world/OctoClock.md` (A shared game)
- 2023 [year] Off-collabs; "Fire N Ice" duet (2023-12-14) — `bible/world/TakaMori.md` (Their song)
- 2023 [year] Frequent horror and TTRPG co-ops; "Time and Death Say Howdy to Ghosts" — `bible/world/Time-and-Death.md` (The duo's name)

### 2023-01
- 2023-01-19 [day] ChikuTaku song on sale — `bible/characters/Watson-Amelia.md` ([Official A13b])
- 2023-01-24 [day] ChikuTaku game released (concept and shared project management, with a credited team) — `bible/characters/Watson-Amelia.md` ([Official A13])

### 2023-03
- 2023-03-19 [day] 3D idol costume at hololive 4th fes. (day 2) — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2023])
- 2023-03-18/19 [day-range] 3D idol costume and main 3D model at hololive 4th fes.; sang a DECO*27 song with Kiara on the holo*27 stage — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2023; M4])
- 2023-03-19 [day] Mumei sings with Kiara on the 4th fes. stage — `bible/world/Fauna-and-Mumei-Pairs.md` (HOLOTORI)
- 2023-03-18/19 [day-range] hololive SUPER EXPO 2023 and 4th fes. "Our Bright Parade" — `bible/world/hololive-History-2023-2026.md` (—)
- 2023-03-28 [day] The fan app "holoplus" is introduced — `bible/world/hololive-History-2023-2026.md` (—)

### 2023-04
- 2023-04-08 [day] 5D Chess ("I Don't Understand") — `bible/world/Time-Duo.md` (A time-travel game, fittingly)
- 2023-04 [month] holoMeet 2023 ambassadors include IRyS — `bible/world/hololive-History-2023-2026.md` (IRyS represents EN)

### 2023-07
- 2023-07-02 [day] hololive English 1st concert "-Connect the World-" — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2023])
- 2023-07-31 JST [day, JST] Debuts with Mococo as FUWAMOCO in hololive English -Advent- — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW1])
- 2023-07-30 JST [day, JST] Debuts with hololive English -Advent- ("Moai Moai Kyun~!") — `bible/characters/Koseki-Bijou.md` ([Official KB1] [Observed KB3])
- 2023-07-31 JST [day, JST] Debuts with Fuwawa as FUWAMOCO — `bible/characters/Mococo-Abyssgard.md` ([Official MC1])
- 2023-07-31 [day] FUWAMOCO MORNING pilot — `bible/characters/Mococo-Abyssgard.md` ([Observed MC2])
- 2023-07-31 [day] Debuts with hololive English -Advent- — `bible/characters/Nerissa-Ravencroft.md` ([Official N1])
- 2023-07-30 JST [day, JST] Debuts with hololive English -Advent- ("Shiori~n!") — `bible/characters/Shiori-Novella.md` ([Official SN1])
- 2023-07-25 [day] "WANTED!" PV reveals the five — `bible/world/Advent-Pairs.md` (fugitive premise)
- 2023-07-29/30 PDT [day-range, PDT] Debuts (Shiori, Bijou, Nerissa, FUWAMOCO) — `bible/world/Advent-Pairs.md` ("The Sweet Escape," the first group collab)
- 2023-07-31 JST [day, JST] Debut ("who let the dogs out?!") and FUWAMOCO MORNING pilot — `bible/world/FUWAMOCO.md` ("BAU BAU!! 🐾✨" (first post))
- 2023-07-25 [day] "WANTED!" debut PV reveals the five — `bible/world/hololive--Advent.md` (The fugitive premise)
- 2023-07 (end) [month] Debuts; Nerissa's on 2023-07-31 (JST) — `bible/world/hololive--Advent.md` ("Advent")
- 2023-07-02 [day] hololive English 1st concert "-Connect the World-" — `bible/world/hololive-History-2023-2026.md` (EN's first concert)
- 2023-07-25/31 [day-range] **-Advent- revealed ("WANTED!") and debuts**: Shiori, Bijou, **Nerissa**, Fuwawa, Mococo — `bible/world/hololive-History-2023-2026.md` (Nerissa's origin)

### 2023-08
- 2023-08-12 [day] An Undertale mod starring Calli, played with Calli on stream — `bible/characters/Koseki-Bijou.md` ([Observed KB3])
- 2023-08-12 [day] Advent on Kiara's HOLOTALK — `bible/characters/Shiori-Novella.md` ([Observed SN3; Kiara archive])
- 2023-08-12 [day] HOLOTALK with Kiara; Bijou's Undertale replay with Calli — `bible/world/Advent-Pairs.md` (senior ties)
- 2023-08-14 [day] Nerissa's compatibility test with Kiara — `bible/world/IRyS-and-Nerissa-Pairs.md` (KiaRissa)
- 2023-08-12 [day] Advent are Kiara's 29th HOLOTALK guests — `bible/world/hololive--Advent.md` (First big senior collab)

### 2023-09
- 2023-09-13 [day] 3rd anniversary relay (#Myth3YearRelay), e.g. a homemade Family Feud with all five — `bible/world/hololive--Myth.md` (Anniversary relays)
- 2023-09-09/10 [day-range] hololive DEV_IS opens with ReGLOSS (Ao, Kanade, Ririka, Raden, Hajime) — `bible/world/hololive-History-2023-2026.md` (Japanese kouhai)

### 2023-10
- 2023-10-09 [day] Joins hololive English -Promise- — `bible/characters/Ceres-Fauna.md` ([Official])
- 2023-10-09 [day] Joins hololive English -Promise- with Fauna, Kronii, Mumei and Bae — `bible/characters/IRyS.md` ([Observed R2 §2023])
- 2023-10-09 [day] Joins hololive English -Promise- — `bible/characters/Nanashi-Mumei.md` ([Official])
- 2023-10-10 [day] Second original song "mumei" — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2023])
- 2023-10-09 [day] Joins hololive English -Promise- alongside IRyS, Ceres Fauna, Nanashi Mumei and Hakos Baelz — `bible/characters/Ouro-Kronii.md` ([Official K3])
- 2023-10-09 [day] -Promise- formed — `bible/world/Fauna-and-Mumei-Pairs.md` (—)
- 2023-10-09 [day] -Promise- formed: IRyS and Kronii genmates — `bible/world/IRyS-and-Nerissa-Pairs.md` (—)
- 2023-10-08 PDT / 10-09 JST [day-range, PDT] -Promise- formed with IRyS (closing Project: HOPE) — `bible/world/hololive--Promise.md` (The current group name)
- 2023-10-08/09 [day-range] "CouncilRyS" 3D showcase; **-Promise- formed** (IRyS joins the Council) — `bible/world/hololive-History-2023-2026.md` (Kronii's and IRyS's group)
- 2023-10-09 [day] -Promise- formed (IRyS joins the remaining Council) — `bible/world/hololive.md` (Kronii's group name)

### 2023-12
- 2023-12 [month] VTuber Awards: "League of Their Own" (as FUWAMOCO) — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §Awards])
- 2023-12 [month] VTuber Awards: "League of Their Own" — `bible/world/FUWAMOCO.md` (—)

### 2024
- 2024 [year] MECONOPSIS and TEMARI; she discusses MECONOPSIS's conflict between duty and protecting others — `bible/characters/Ninomae-Inanis.md` ([Official I1 music list] [Observed—published interview I7b])

### 2024-01
- 2024-01-26 [day] 1,000,000 subscribers, the first of Council/Promise — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2024])
- 2024-01-16 [day] Yozora Mel leaves hololive — `bible/world/hololive-History-2023-2026.md` (Not discussed in stories)

### 2024-03
- 2024-03-04 [day] "TAKOTORI OFFCOLLAB!!" — `bible/world/TakoTori.md` (The pair name in their own titles)
- 2024-03-16/17 [day-range] SUPER EXPO 2024 and 5th fes. "Capture the Moment" — `bible/world/hololive-History-2023-2026.md` (—)

### 2024-04
- 2024-04-27 [day] First original song "Say My Name" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2024])
- 2024-04 [month] holoMeet 2024 ambassadors include Hakos Baelz — `bible/world/hololive-History-2023-2026.md` (—)

### 2024-06
- 2024-06-22 PDT [day, PDT] Debut ("It's wind-up time!!"), with a chat-controlled game (implemented by nullrefrepro per the credits; Raora drew the ending screen and sweeping art) and a violin performance; official profile lists June 23 (JST) — `bible/characters/Cecilia-Immergreen.md` ([Official CI1] [Observed CI3])
- 2024-06-21 PDT [day, PDT] Debut ("Ello Ello Ello~!"), first of Justice; official profile lists June 22 (JST) — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB1] [Observed EB3])
- 2024-06-21 PDT [day, PDT] Debut ("GG STANDS FOR GIGI!"), second of Justice; official profile lists June 22 (JST) — `bible/characters/Gigi-Murin.md` ([Official GG1] [Observed GG3])
- 2024-06-22 PDT [day, PDT] Debut ("I've got my eyes on you 🐱 mamma mia"), last of Justice; official profile lists June 23 (JST) — `bible/characters/Raora-Panthera.md` ([Official RP1] [Observed RP3])
- 2024-06-26 [day] Raora's first collab, "Chat & Art w/ Liz!" — `bible/world/Justice-Pairs.md` (FlamePanther)
- 2024-06-18 [day] Announcement video "The Mission Begins!" — `bible/world/hololive--Justice.md` (the manhunt premise)
- 2024-06-21/22 PDT [day-range, PDT] Debuts: Elizabeth (06-21 8 PM), Gigi (06-21 8:45 PM), Cecilia (06-22 8 PM), Raora (06-22 8:45 PM); official profiles list June 22/23 (JST) — `bible/world/hololive--Justice.md` ("ABOVE BELOW" released; first collab "Ello! Hi! Hallo! Ciao!" (06-22 9:30 PM PDT))
- 2024-06–07 [month-range] Content Warning, Chained Together, Left 4 Dead 2, a Justice Minecraft server and "Justice HQ" — `bible/world/hololive--Justice.md` (the group's first weeks)
- 2024-06 [month] Myth One-Block Minecraft series — `bible/world/hololive--Myth.md` (A recent full-group project)
- 2024-06-21/22 PDT [day-range, PDT] **-Justice- debuts**: Elizabeth Rose Bloodflame, Gigi Murin, Cecilia Immergreen, Raora Panthera ("law enforcers" chasing Advent) — `bible/world/hololive-History-2023-2026.md` (EN's newest kouhai)

### 2024-07
- 2024-07-31 [day] First original song "Born to be 'BAU'DOL☆★" — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2024])
- 2024-07-31 [day] First original song "Born to be 'BAU'DOL☆★" — `bible/world/FUWAMOCO.md` (—)
- 2024-07-03 [day] Cecilia and Raora's Minecraft duo — `bible/world/Justice-Pairs.md` (Raviolin)
- 2024-07-19 [day] Cecilia shows Elizabeth around Minecraft — `bible/world/Justice-Pairs.md` (FiddleFlame)
- 2024-07-21/22 [day-range] Advent VS Justice, Party Animals — `bible/world/Justice-Pairs.md` (the rivalry as a game)
- 2024-07-21/22 [day-range] "Advent VS Justice" in Party Animals — `bible/world/hololive--Justice.md` (the rivalry as a game)

### 2024-08
- 2024-08-24/25 [day-range] hololive English 2nd concert -Breaking Dimensions-: premieres "It's Not a Phase" with Mumei and sings "Mayonaka no Door" solo (day 1); "Lonely in Gorgeous" with Shiori and Nerissa (day 2) — `bible/characters/Ceres-Fauna.md` ([Official F5])
- 2024-08-10 PDT [day, PDT] 3D debut with a wrestling segment and cameos by Okayu and Korone — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2024])
- 2024-08-03 PDT [day, PDT] 3D debut; first performs "Prism no Mahou" ("Prism Magic") — `bible/characters/Koseki-Bijou.md` ([Observed KB2 §2024] [Official KB7])
- 2024-08-17 PDT [day, PDT] Advent's 3D collaboration stream — `bible/characters/Koseki-Bijou.md` ([Official KB7])
- 2024-08-11 [day] #BAEBISleepOver with Hakos Baelz — `bible/characters/Koseki-Bijou.md` ([Observed KB3])
- 2024-08-10 PDT [day, PDT] 3D debut — `bible/characters/Mococo-Abyssgard.md` ([Observed MC2 §2024])
- 2024-08-05 [day] 3D birthday live "Outside the Box"; guests Gura, IRyS, Bae, Nekomata Okayu, Inugami Korone, Momosuzu Nene, Hakui Koyori — `bible/characters/Nanashi-Mumei.md` ([Observed M3 title, description])
- 2024-08-24 [day] -Breaking Dimensions- day 1: premieres "It's Not a Phase" with Fauna; "Beyond the way" with Kiara and Nerissa; day 2: her original "A New Start" — `bible/characters/Nanashi-Mumei.md` ([Official M5])
- 2024-08-09 PDT [day, PDT] 3D debut; the "Demon of Soup" soup — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2])
- 2024-08-08 [day] First EP "In My Feelings" — `bible/characters/Nerissa-Ravencroft.md` ([Official N22])
- 2024-08-02 PDT [day, PDT] 3D debut "A New Chapter Begins!" with Nerissa, Bijou and FUWAMOCO as guests — `bible/characters/Shiori-Novella.md` ([Observed SN3 tIKQMFtbgOA])
- 2024-08-25 [day] -Breaking Dimensions-: "Lonely in Gorgeous" with Fauna and Nerissa — `bible/characters/Shiori-Novella.md` ([Official, Concerts card S8])
- 2024-08-02 → 08-10 PDT [day, PDT] 3D debuts (Shiori 08-02, Bijou 08-03, Nerissa 08-09, FUWAMOCO 08-10; JST dates are one day later) — `bible/world/Advent-Pairs.md` (genmates as guests [Official S9])
- 2024-08-17 PDT [day, PDT] Advent's 3D collaboration stream — `bible/world/Advent-Pairs.md` ([Official S9])
- 2024-08-10 PDT [day, PDT] 3D debut: a wrestling segment supervised by DDT Pro-Wrestling, Okayu and Korone cameos — `bible/world/FUWAMOCO.md` ("Lifetime Showtime" full version)
- 2024-08-24 [day] "It's Not a Phase" premiered at -Breaking Dimensions- — `bible/world/Fauna-and-Mumei-Pairs.md` (their duet (released 2024-12-22))
- 2024-08-02/10 PDT [day-range, PDT] 3D debuts: Shiori 08-02, Bijou 08-03, Nerissa 08-09, FUWAMOCO 08-10 (JST one day later) — `bible/world/hololive--Advent.md` (genmates as guests)
- 2024-08-17 PDT [day, PDT] Advent's 3D collaboration stream — `bible/world/hololive--Advent.md` (official 3D showcase schedule)
- 2024-08-02/10 PDT [day-range, PDT] Advent 3D debuts (JST dates one day later): Shiori (08-02), Bijou (08-03), Nerissa (08-09), FUWAMOCO (08-10, with Okayu and Korone cameos) — `bible/world/hololive-History-2023-2026.md` (genmates as guests)
- 2024-08-23 [day] "ENigmatic Recollection" (ENReco) announced: EN members in the fantasy world Libestal, via a Minecraft series, animation and songs — `bible/world/hololive-History-2023-2026.md` (Guilds: IRyS in "Cerulean Cup," Nerissa and Gura in "Scarlet Wand")
- 2024-08-23 EDT [day, EDT] World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 — `bible/world/hololive-History-2023-2026.md` (—)
- 2024-08-24/25 EDT [day-range, EDT] EN 2nd concert "-Breaking Dimensions-" (Kings Theatre, New York), a separate event — `bible/world/hololive-History-2023-2026.md` (—)
- 2024-08-28 [day] Minato Aqua graduates — `bible/world/hololive-History-2023-2026.md` (—)

### 2024-09
- 2024-09 [month] "2.0" model update — `bible/characters/Gawr-Gura.md` ([Observed G3])
- 2024-09-21 [day] Sings "September" 120 times in an eight-hour unarchived karaoke — `bible/characters/Gigi-Murin.md` ([Observed GG2, secondary])
- 2024-09-05 [day] Tutu, a cat, is added to her model as a toggle. — `bible/characters/Mori-Calliope.md` ([Observed C4 §Mascot and fans, secondary])
- 2024-09-30 [day] Concludes regular activities; remains a hololive affiliate — `bible/characters/Watson-Amelia.md` ([Official A4])
- 2024-09-29 [day] "Looking at our old DMs" — `bible/world/AmeSame.md` (Their last duo stream before Ame stepped back)
- 2024-09 [month] Calli performs Gura's "Full Color" at Myth's 4th-anniversary concert "The Show Goes On!" — `bible/world/Bone-Bros.md` (Carrying her song)
- 2024-09-22 [day] Ame on HOLOTALK — `bible/world/Myth-and-Kronii-Other-Pairs.md` (Kiara's oshi as guest)
- 2024-09 [month] Backrooms and DRG in Ame's last week — `bible/world/Time-Duo.md` (—)
- 2024-09-22 [day] Escape the Backrooms with Ame — `bible/world/Time-and-Death.md` (One of Ame's last collabs)
- 2024-09 [month] 4th anniversary song and voice pack; Ame's last week includes a Myth collab — `bible/world/hololive--Myth.md` (Ame's farewell to regular streaming)
- 2024-09-30 [day] **Watson Amelia concludes regular activities and stays an affiliate** — `bible/world/hololive-History-2023-2026.md` (Ame appears as a guest)
- 2024-09-30 [day] Watson Amelia concludes general activities, stays an affiliate — `bible/world/hololive.md` (Occasional guest appearances)

### 2024-10
- 2024-10-12 [day] FUWAMOCO reach 1,000,000 subscribers, first in Advent — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2024])
- 2024-10-06 / 10-08 [day-range] "Prism no Mahou" music video (10-06) and release (10-08) — `bible/characters/Koseki-Bijou.md` ([Observed KB2 §2024] [Official KB8])
- 2024-10-12 [day] 1,000,000 subscribers, first in Advent — `bible/world/FUWAMOCO.md` (—)
- 2024-10-31/11-01 [day-range] "Justice's Haunted VR Investigation" in VRChat, with Advent visitors; chibi 3D models — `bible/world/hololive--Justice.md` (Halloween tradition)
- 2024-10-12 [day] FUWAMOCO reach 1,000,000 subscribers, first in Advent; VTuber of the Year at the VTuber Awards (2024-12) — `bible/world/hololive-History-2023-2026.md` (—)

### 2024-11
- 2024-11-17 [day] 3D live "The Devil Wears Hope" — `bible/characters/IRyS.md` ([Observed R3 title])
- 2024-11-09 [day] DEV_IS second unit FLOW GLOW debuts (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya, Kikirara Vivi) — `bible/world/hololive-History-2023-2026.md` (—)
- 2024-11-29 [day] Two months after Ame's change of status, COVER names it: "conclusion of streaming activities," distinct from graduation (affiliates can still appear in projects) — `bible/world/hololive-History-2023-2026.md` (Why Ame can come back for events)

### 2024-12
- 2024-12-14 [day] -Promise- musical "The Broken Promise" — `bible/characters/Ceres-Fauna.md` ([Observed F2 §2024])
- 2024-12-22 [day] "It's Not a Phase" (Mumei & Fauna) released — `bible/characters/Ceres-Fauna.md` ([Official F6])
- 2024-12-27 [day] 1,000,000 subscribers; Kiara's HOLOTALK guest the same day — `bible/characters/Ceres-Fauna.md` ([Observed F2; F3 title])
- 2024-12-31 [day] The World Tree is complete — `bible/characters/Ceres-Fauna.md` ([Observed F3 title])
- 2024-12 [month] VTuber Awards: "VTuber of the Year" (as FUWAMOCO) — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §Awards])
- 2024-12-14 [day] VTuber Awards: Most Chaotic VTuber — `bible/characters/Gigi-Murin.md` ([Observed GG6; secondary reporting])
- 2024-12-14 [day] -Promise- musical "The Broken Promise" — `bible/characters/IRyS.md` ([Observed R2 §2024])
- 2024-12-22 [day] "It's Not a Phase" (Mumei & Fauna) released — `bible/characters/Nanashi-Mumei.md` ([Official M6])
- 2024-12-14 [day] VTuber Awards: Best Art VTuber — `bible/characters/Raora-Panthera.md` ([Observed RP6; secondary report])
- 2024-12 [month] VTuber Awards: "VTuber of the Year" — `bible/world/FUWAMOCO.md` (—)
- 2024-12-27 [day] Fauna on Kiara's HOLOTALK — `bible/world/Fauna-and-Mumei-Pairs.md` (—)
- 2024-12 [month] FUWAMOCO win "VTuber of the Year" at the VTuber Awards — `bible/world/hololive--Advent.md` (—)
- 2024-12-28 [day] Half-year anniversary (New Year outfits announced, shown 2025-01-01) — `bible/world/hololive--Justice.md` (—)

### 2025
- 2025 [year] Fauna (January) and Mumei (April) graduate; Promise's current members are Kronii, IRyS and Baelz — `bible/characters/Ouro-Kronii.md` (Shared history stays [Official K34])
- 2025–2026 [year-range] Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card — `bible/characters/Watson-Amelia.md` ([A8, A19])
- 2025 [year] Nerissa's 3D concert with Calli and IRyS as guests; "OVER//RIDE" duet — `bible/world/IRyS-and-Nerissa-Pairs.md` (Calli × Nerissa)
- 2025 [year] Myth relay for Gura's farewell — `bible/world/Streaming-Life.md` ("One last time" streams)
- 2025, 2026 [year] hololive SUPER EXPO with -Justice- — `bible/world/hololive--Advent.md` (Prisoner-and-guard bits)

### 2025-01
- 2025-01-03 [day] Graduates; last post on X: "LOVE & PEACE / Love, Fauna" — `bible/characters/Ceres-Fauna.md` ([Observed F2, secondary])
- 2025-01-18 [day] "Mephisto" cover with HOLOSTARS' Banzoin Hakka — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Observed EB3])
- 2025-01-29 [day] 500th on-stream sneeze, celebrated on X — `bible/characters/Mococo-Abyssgard.md` ([Observed MC6])
- 2025-01 [month] "Office lady" outfit (#OLRissa) — `bible/characters/Nerissa-Ravencroft.md` ([Observed N3 titles])
- 2025-01-03 [day] Fauna graduates — `bible/world/Fauna-and-Mumei-Pairs.md` (—)
- 2025-01-31 [day] Murky Divers, Advent × Justice (all nine) — `bible/world/Justice-Pairs.md` (—)
- 2025-01 [month] The "$KRONII" coin bit and Calli's mock exposé — `bible/world/Time-and-Death.md` (Mock feud)
- 2025-01-31 [day] "ADVENT VS JUSTICE" Murky Divers with all nine — `bible/world/hololive--Justice.md` (—)
- 2025-01-03 [day] Fauna graduates — `bible/world/hololive--Promise.md` (—)
- 2025-01-03 [day] Ceres Fauna graduates — `bible/world/hololive-History-2023-2026.md` (Promise remembers her)
- 2025-01-26 [day] Sakamata Chloe concludes streaming activities (affiliate) — `bible/world/hololive-History-2023-2026.md` (—)

### 2025-02
- 2025-02-02 [day] First birthday 3D concert, with Advent and JP guests — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW3 ouQF2A1l_cI])
- 2025-02-26 [day] "GriMoire" at the Hollywood Palladium, the first solo concert outside Japan by a hololive production talent. — `bible/characters/Mori-Calliope.md` ([Official C19])
- 2025-02-14 [day] 3.0 Live2D model — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2025])
- 2025-02-02 [day] First birthday 3D concert — `bible/world/FUWAMOCO.md` (—)
- 2025-02-27 [day] Kiara's watch party for Calli's GriMoire concert — `bible/world/TakaMori.md` (Cheering from the crowd)

### 2025-03
- 2025-03-15/16 [day-range] Birthday: "DIAMOND GIRLFRIEND," EP "YaBAI," 3D live "HOPE UPON A STAR" — `bible/characters/IRyS.md` ([Observed R2 §2025; R3])
- 2025-03-09 [day] 6th fes. "Color Rise Harmony," day 2 — `bible/characters/Nanashi-Mumei.md` ([Observed M2 §2025])
- 2025-03-08 [day] hololive 6th fes. Color Rise Harmony, day 1 — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2025])
- 2025-03-08 [day] Justice hosted a watchalong of hololive 6th fes. (Expo 2025) Stage 1 ("FIRST STAGE with JUSTICE!") — `bible/world/hololive--Justice.md` ([Observed S4 nEV7T8peRcw])
- 2025-03-08/09 [day-range] SUPER EXPO 2025 and 6th fes. "Color Rise Harmony" — `bible/world/hololive-History-2023-2026.md` (Nerissa performs on day 1)

### 2025-04
- 2025-04 [month] A farewell month of collabs across hololive: Overwatch with IRyS (04-22), a cover of "とんとんまーえ！" with Inugami Korone (04-23), Promise R.E.P.O. with IRyS, Kronii and Bae (04-24); last chatting stream with calls (04-26); 3D graduation stream (04-27, 04-28 JST) — `bible/characters/Nanashi-Mumei.md` ([Observed M2; M3 titles])
- 2025-04-30 [day] "One Last Minecraft Trip." (Myth relay) — `bible/world/Bone-Bros.md` (Last duo moments on stream)
- 2025-04 [month] Mumei's farewell month: "Donut Hole" with Kronii (04-11), Overwatch with IRyS (04-22), HOLOTALK (04-22), a Korone duet cover (04-23), Promise R.E.P.O. (04-24), Gura's room review — `bible/world/Fauna-and-Mumei-Pairs.md` (—)
- 2025-04-27 [day] Mumei graduates (04-28 JST) — `bible/world/Fauna-and-Mumei-Pairs.md` (—)
- 2025-04-26/30 [day-range] Kronii's and Kiara's last collabs with Gura — `bible/world/Myth-and-Kronii-Other-Pairs.md` (Farewells)
- 2025-04/05 [month-range] Split Fiction series ("takamori split screen nostalgia") — `bible/world/TakaMori.md` (Nostalgic co-op)
- 2025-04-30 [day] Myth relay "one last time" with Calli, Kiara, Ina and Gura before Gura's graduation — `bible/world/hololive--Myth.md` (Gura's farewell with Myth)
- 2025-04-27 [day] Mumei graduates — `bible/world/hololive--Promise.md` (Promise becomes three)
- 2025-04 [month] World Tour '25 "-Synchronize!-" announced, led by Momosuzu Nene, Kureiji Ollie, **Mori Calliope, IRyS and Nerissa Ravencroft**, with guests per city (Kronii and Bae in Sydney) — `bible/world/hololive-History-2023-2026.md` (Three of the cast on one tour)
- 2025-04-26 [day] Murasaki Shion graduates — `bible/world/hololive-History-2023-2026.md` (—)
- 2025-04-27 (04-28 JST) [day, JST] Nanashi Mumei graduates — `bible/world/hololive-History-2023-2026.md` (Promise becomes three)

### 2025-05
- 2025-05-01 [day] Graduates; final 3D mini live; last post "keep swimming! always! 💙" — `bible/characters/Gawr-Gura.md` ([Official G5] [Observed G3, G2])
- 2025-05-24 [day] 3D concert "Requiem for Love – A JukeBox Musical" (guests incl. Calli, IRyS) — `bible/characters/Nerissa-Ravencroft.md` ([Observed N3 titles])
- 2025-05-01 [day] Gura graduates — `bible/world/AmeSame.md` (—)
- 2025-05-01 [day] Gura graduates — `bible/world/Bone-Bros.md` (—)
- 2025-05-01 [day] **Gawr Gura graduates** — `bible/world/hololive-History-2023-2026.md` (Myth's first graduation; her last post: "keep swimming! always!")
- 2025-05-02 [day] ENReco chapter 2 "The Chains of Fate" — `bible/world/hololive-History-2023-2026.md` (—)
- 2025-05-01 [day] Gawr Gura graduates — `bible/world/hololive.md` (Alumna; remembered in songs and anniversaries)

### 2025-06
- 2025-06-29 [day] "THAT'S WILD?!" 24-hour charity stream with Calli (Wildlife Warriors Worldwide) — `bible/characters/Koseki-Bijou.md` ([Observed Calli archive J5u2aGUrNq8])
- 2025-06-20 [day] First anniversary, "Operation DECODE" — `bible/world/hololive--Justice.md` (—)

### 2025-07
- 2025-07-11 [day] 4th anniversary; 3.0 model — `bible/characters/IRyS.md` ([Observed R3 title])
- 2025-07-05 [day] hololive night at Dodger Stadium with Ina and IRyS: a stadium sing-along and the first VTuber stream from the stadium — `bible/characters/Koseki-Bijou.md` ([Official KB9])
- 2025-07-05 [day] hololive night at Dodger Stadium: Bijou with Ina and IRyS — `bible/world/Advent-Pairs.md` ([Official S8])
- 2025-07 [month] MYTHMASH: each active member releases a duet with a Japanese senpai (#mythmashchemythtry) — `bible/world/hololive--Myth.md` (Cross-branch songs)
- 2025-07-05 [day] hololive night at Dodger Stadium, Los Angeles, the second hololive–Dodgers collaboration: Ina, IRyS and Bijou — `bible/world/hololive-History-2023-2026.md` (a stadium sing-along)
- 2025-07-16 [day] hololive RECORDS label launched — `bible/world/hololive-History-2023-2026.md` (—)

### 2025-08
- 2025-08-08 PDT [day, PDT] 3D showcase (5 PM PDT; Aug 9 09:00 JST) — `bible/characters/Cecilia-Immergreen.md` ([Official CI7])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Cecilia-Immergreen.md` ([Official CI7])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice; "Wind-Up," the first Justice solo; "SHALLYS" with Ina and FUWAMOCO (on violin); "I'm Your Treasure Box" with Bijou and Raora — `bible/characters/Cecilia-Immergreen.md` ([Official CI5])
- 2025-08-01 PDT [day, PDT] 3D showcase (5 PM PDT); she arranged and directed most of it, including "Giri Giri" with Vestia Zeta — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB7] [ASR EB20])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB7])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice, "ALiCE&u" with Nerissa and guest Ayunda Risu, solo "Stellar Stellar," "START AGAIN" with Calli, IRyS and Nerissa (day 2 opener), "High Tide" with Kronii and guest Kureiji Ollie — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB5])
- 2025-08-23/24 [day-range] -All for One-: "HOT DUCK!", "Howling," "Lifetime Showtime," "SHALLYS" — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW5])
- 2025-08-02 PDT [day, PDT] 3D showcase (5 PM PDT; Aug 3 00:00 UTC) — `bible/characters/Gigi-Murin.md` ([Official GG8])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Gigi-Murin.md` ([Official GG8])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice, "Countach" with Bae and guest Kureiji Ollie, "MONSTER" with Ina, Kronii and Shiori, solo "Wonky Monkey," "III" with Nerissa — `bible/characters/Gigi-Murin.md` ([Official GG5])
- 2025-08-23/24 [day-range] -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora — `bible/characters/Koseki-Bijou.md` ([Official KB5])
- 2025-08-23/24 [day-range] -All for One- with Fuwawa — `bible/characters/Mococo-Abyssgard.md` ([Official MC5])
- 2025-08-29 [day] Advent 2nd-anniversary 3D live "On the Run!" ("The Story of Advent") — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2025])
- 2025-08-09 PDT [day, PDT] 3D showcase (5 PM PDT; Aug 10 09:00 JST) — `bible/characters/Raora-Panthera.md` ([Official RP8])
- 2025-08-16 PDT [day, PDT] Justice 3D collaboration stream — `bible/characters/Raora-Panthera.md` ([Official RP8])
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ABOVE BELOW" with Justice, solo "Gacha x Gacha ADVENTURE!," "Neko Kaburi-Na" with Ina, Shiori and guest Oozora Subaru, "I'm Your Treasure Box" with Bijou and Cecilia — `bible/characters/Raora-Panthera.md` ([Official RP5])
- 2025-08-29 [day] Advent 2nd-anniversary 3D live "On the Run!" — `bible/characters/Shiori-Novella.md` ([Observed SN2 §2025])
- 2025-08-23/24 [day-range] -All for One-: "Genesis" as five, and pair stages across EN — `bible/world/Advent-Pairs.md` (—)
- 2025-08-29 [day] "On the Run!" 2nd-anniversary 3D live — `bible/world/Advent-Pairs.md` ("The Story of Advent")
- 2025-08-23/24 [day-range] -All for One-: "HOT DUCK!" with Bijou and Subaru; their version of "Howling"; "Lifetime Showtime"; "SHALLYS" with Ina and Cecilia — `bible/world/FUWAMOCO.md` ([Official S5])
- 2025-08-16 PDT [day, PDT] Justice group 3D collab (after the individual showcases 08-01/02/08/09 PDT) — `bible/world/Justice-Pairs.md` (official schedule)
- 2025-08-23/24 EDT [day-range, EDT] -All for One-: "ALiCE&u," "START AGAIN," "High Tide" (Elizabeth); "Countach," "MONSTER," "III," "Wonky Monkey" (Gigi); "Wind-Up," "SHALLYS," "I'm Your Treasure Box" (Cecilia); "Gacha×Gacha ADVENTURE!," "Neko Kaburi-Na," "I'm Your Treasure Box" (Raora) — `bible/world/Justice-Pairs.md` ([Official S6])
- 2025-08-23 [day] -All for One- opens with all of EN, then Advent's "Genesis" — `bible/world/hololive--Advent.md` ([Official S9])
- 2025-08-29 [day] 2nd-anniversary 3D live "On the Run!" with "The Story of Advent" (five chapters, five songs) — `bible/world/hololive--Advent.md` (—)
- 2025-08-01/02/08/09 PDT [day-range, PDT] Individual 3D showcases, each at 5 PM PDT: Elizabeth (08-01), Gigi (08-02), Cecilia (08-08), Raora (08-09) — `bible/world/hololive--Justice.md` ([Official S7])
- 2025-08-16 PDT [day, PDT] Justice group 3D collaboration stream (5 PM PDT) — `bible/world/hololive--Justice.md` ([Official S7])
- 2025-08-23 EDT [day, EDT] -All for One-: Justice's first group performance at an in-person concert venue in 3D ("ABOVE BELOW"); Cecilia's "Wind-Up" was the first Justice solo number of that concert; see the member files for their other stages — `bible/world/hololive--Justice.md` ([Official S3])
- 2025-08-01/02/08/09 PDT [day-range, PDT] Justice 3D showcases, each at 5 PM PDT: Elizabeth (08-01), Gigi (08-02), Cecilia (08-08), Raora (08-09) — `bible/world/hololive-History-2023-2026.md` (official schedule)
- 2025-08-16 PDT [day, PDT] Justice group 3D collaboration stream — `bible/world/hololive-History-2023-2026.md` (before their first in-person concert stage)
- 2025-08-23/24 EDT [day-range, EDT] EN 3rd concert "-All for One-" (Radio City Music Hall, New York): day 1 opens with the all-member "All for One," followed by Advent's "Genesis"; Justice's first group performance at an in-person concert venue in 3D — `bible/world/hololive-History-2023-2026.md` (all fifteen EN members on one stage)
- 2025-08-29 [day] Advent 2nd-anniversary live "On the Run!" ("The Story of Advent") — `bible/world/hololive-History-2023-2026.md` (Nerissa's group milestone)

### 2025-09
- 2025-09-13 [day] 5th anniversary collab with announcements (Calli, Kiara, Ina) — `bible/world/hololive--Myth.md` (New anniversary hats)

### 2025-10
- 2025-10-18 [day] First original song "I'll still be here" presented (digital release 10-20) — `bible/characters/Gigi-Murin.md` ([Official GG7] [Observed GG2])
- 2025-10-10 [day] Promise releases "Run Back 'Round" — `bible/characters/Ouro-Kronii.md` ([Official K6])
- 2025-10-03 [day] Hiodoshi Ao (ReGLOSS) leaves — `bible/world/hololive-History-2023-2026.md` (—)
- 2025-10-15 [day] Official fan club launches — `bible/world/hololive-History-2023-2026.md` (—)

### 2025-11
- 2025-11-01 [day] Second original song "ROCK IN!" and a 3D live — `bible/characters/Koseki-Bijou.md` ([Observed KB2 §2025])
- 2025-11-16 [day] The "Doom" spell in Kiara's Mage Arena collab — `bible/characters/Raora-Panthera.md` ([Observed RP7])
- 2025-11-16 [day] Raora's "Doom" on her stream becomes a meme — `bible/characters/Takanashi-Kiara.md` ([Observed T6])
- 2025-11-23 [day] Duo concert announced — `bible/world/TakoTori.md` (—)
- 2025-11 [month] Raora's friendly-fire "Doom" spell in Kiara's Mage Arena collab becomes a widely shared fan meme (KYM dates the stream 11-16) — `bible/world/hololive-History-2023-2026.md` (a callback)
- 2025-11-15 [day] hololive Indonesia 1st concert "Chromatic Future" — `bible/world/hololive-History-2023-2026.md` (—)

### 2025-12
- 2025-12-22 [day] "Bright Tonight" with IRyS, Kronii and FUWAMOCO released — `bible/characters/Gigi-Murin.md` ([Official GG7])
- 2025-12-27 [day] Amane Kanata graduates — `bible/world/hololive-History-2023-2026.md` (—)

### 2026
- 2026 [year] TAKO∞TAKOVER, a deliberately unsettling takeover story; lyrics by Mori Calliope — `bible/characters/Ninomae-Inanis.md` ([Observed—published interview I19] [Official I25])
- 2026 [year] "Bound by Fate," 3rd-anniversary 3D live — `bible/world/Advent-Pairs.md` (—)
- 2026 [year] 3rd-anniversary live "Bound by Fate" (linked from Nerissa's official profile) — `bible/world/hololive--Advent.md` (—)

### 2026-01
- 2026-01-23 [day] Original song "OYOME♡HOLIC" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2026])
- 2026-01-08 [day] "TAKO∞TAKOVER" digital release (lyrics by Calli) — `bible/world/Myth-and-Kronii-Other-Pairs.md` (Ina × Calli)
- 2026-01-26 [day] Group song "Breakout" — `bible/world/hololive--Advent.md` (—)

### 2026-02
- 2026-02-06 [day] Her third major album, "DISASTERPIECE." — `bible/characters/Mori-Calliope.md` ([Official C16])
- 2026-02-02 [day] First EP "re:VISION" — `bible/characters/Ninomae-Inanis.md` ([Official I26])
- 2026-02-15 [day] First original song "Monsters and Men" — `bible/characters/Shiori-Novella.md` ([Observed SN2 Discography])
- 2026-02-08 [day] 2nd album *Vogelfrei* — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §2026; T8])
- 2026-02 [month] Kiara's "Blue & Gold" tribute — `bible/world/AmeSame.md` (The colors as a memory)
- 2026-02-20/22 JST [day-range, JST] GeoGuessr: Elizabeth, Gigi and Cecilia trained (02-20) and represented Justice against Advent (02-22), with Bijou hosting/commentating — `bible/world/hololive--Justice.md` ([Observed, secondary event roster])
- 2026-02 [month] Kiara's album includes "Blue & Gold," a tribute to Gura and Ame — `bible/world/hololive--Myth.md` (Remembering the two)

### 2026-03
- 2026-03 [month] Birthday live "Racing Towards Hope"; "BE MY FLAME"; solo album "DANGERyS" and solo concert announced — `bible/characters/IRyS.md` ([Observed R2 §2026; R3])
- 2026-03-28 [day] Single "Blue World" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §Discography])
- 2026-03-27/28 [day-range] "Drawn to Dawn" duo concert with Kiara (Los Angeles) — `bible/characters/Ninomae-Inanis.md` ([Official I20, I21])
- 2026-03-13 [day] 3D birthday live; Watson Amelia guests — `bible/characters/Ouro-Kronii.md` ([Observed K33, secondary, stream t=1711])
- 2026-03 [month] Bilingual show HoloEN REWIND begins — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §HoloEN REWIND])
- 2026-03-27/28 [day-range] "Drawn to Dawn" duo concert with Ina (The Wiltern, Los Angeles) — `bible/characters/Takanashi-Kiara.md` ([Official T11, T12])
- 2026-03 [month] Guest spot at Kronii's 3D birthday live — `bible/characters/Watson-Amelia.md` ([Observed Kronii file K33, stream locator qqi8yXuH35Y t=1711])
- 2026-03-27/28 [day-range] "Drawn to Dawn," the Wiltern, LA — `bible/world/TakoTori.md` (Their first concert as a duo)
- 2026-03-13 [day] Ame guests at Kronii's 3D birthday live — `bible/world/Time-Duo.md` (The affiliate's cameo)
- 2026-03-06/08 [day-range] SUPER EXPO 2026 and 7th fes. "Ridin' on Dreams" — `bible/world/hololive-History-2023-2026.md` (—)
- 2026-03-27/28 PDT [day-range, PDT] Kiara and Ina's duo concert "Drawn to Dawn" (Los Angeles) — `bible/world/hololive-History-2023-2026.md` (TakoTori on stage)

### 2026-04
- 2026-04 [month] "Mekurumeku Rendezvous," a TV anime ending theme — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW3 vSwxof0K8lk])
- 2026-04-02 [day] "Mekurumeku Rendezvous," a TV anime ending theme — `bible/world/FUWAMOCO.md` (their first TV anime song)
- 2026-04-23 [day] Nerissa's Tomodachi Life Miis of IRyS and Ina — `bible/world/IRyS-and-Nerissa-Pairs.md` (—)
- 2026-04-24 [day] "GETCHA!" cover — `bible/world/TakoTori.md` (—)

### 2026-05
- 2026-05 [month] CCGG 3D live with Gigi (after-talk 05-20, secondary archive evidence); "CCGG MADNESS" MV (05-17; digital 05-29) — `bible/characters/Cecilia-Immergreen.md` ([Official CI1] [Observed CI3 1rIXU_4xGvY, bTxEGwMOQQI])
- 2026-05 [month] 2026 birthday live with guests from several branches; the performances were released as cover videos ("Live from COVER Corp. Studio") — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Observed EB3, archived credits])
- 2026-05 [month] CCGG 3D live with Cecilia; "CCGG MADNESS" MV (05-17; digital 05-29) — `bible/characters/Gigi-Murin.md` ([Official GG1, GG7] [Observed GG3])
- 2026-05-10 [day] First birthday 3D live concert (secondary archive evidence, w37yVSXhV_c) — `bible/characters/Raora-Panthera.md` ([Observed RP3])
- 2026-05 [month] CCGG 3D live, "CCGG MADNESS" — `bible/world/Justice-Pairs.md` (Gigi and Cecilia's unit)
- 2026-05 [month] CCGG (Gigi and Cecilia) joint 3D live (secondary event coverage) and "CCGG MADNESS"; Raora's first birthday 3D live (05-10 JST / 05-09 PDT; secondary metadata) — `bible/world/hololive--Justice.md` (—)
- 2026-05 [month] Gigi and Cecilia's joint CCGG 3D live and "CCGG MADNESS"; Raora's first birthday 3D live (05-10 JST / 05-09 PDT) — `bible/world/hololive-History-2023-2026.md` (—)
- 2026-05-24 [day] ENReco chapter 3 "Broken Bonds" — `bible/world/hololive-History-2023-2026.md` (—)

### 2026-06
- 2026-06-25 [day] Original MV "enough" — `bible/characters/Gigi-Murin.md` ([Observed GG3])
- 2026-06-10 [day] Serendipity interview and partnership with Shiori Novella. — `bible/characters/Mori-Calliope.md` ([Official C11])
- 2026-06-12 [day] 1,000,000 subscribers — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2026])
- 2026-06-04 [day] Serendipity interview and partnership with Kronii — `bible/characters/Ninomae-Inanis.md` ([Official I7])
- 2026-06-04 [day] Serendipity interview and partnership with Ina — `bible/characters/Ouro-Kronii.md` (Puns, appreciation, performance goals [Official K4])
- 2026-06 [month] Serendipity interview and partnership with Koseki Bijou — `bible/characters/Takanashi-Kiara.md` ([Official T10])
- 2026-06-04 [day] Official Serendipity interview — `bible/world/OctoClock.md` (Their own words)
- 2026-06-24 [day] "It's Time for Octo'Clock!" short — `bible/world/OctoClock.md` (The unit name)
- 2026-06-27 PDT [day, PDT] Second-anniversary live "How to Protect JUSTICE!" (06-28 JST) — `bible/world/hololive--Justice.md` ([Official S1 video list])
- 2026-06-27 PDT [day, PDT] Justice's second-anniversary live "How to Protect JUSTICE!" (06-28 JST) — `bible/world/hololive-History-2023-2026.md` (—)

### 2026-07
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "SUPERNOVA SUPER GIRL" with Justice, "CCGG MADNESS" as Autofister with Gigi, "Break It Down" with Vestia Zeta and Shiori, "Cloudy Sheep" with Tsunomaki Watame and Calli (day 1); "ABOVE BELOW" in the Advent+Justice medley (day 2) — `bible/characters/Cecilia-Immergreen.md` ([Official CI4, CI8])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB4, EB8])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: the unit B.F.F with Mococo and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW4; Serendipity report])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "SUPERNOVA SUPER GIRL" with Justice and "CCGG MADNESS" as Autofister with Cecilia (day 1); "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO, and "ABOVE BELOW" in the Advent+Justice medley (day 2) — `bible/characters/Gigi-Murin.md` ([Official GG4, GG9])
- 2026-07-03/04 [day-range] Serendipity concert, duo with Takanashi Kiara ("Rocku Wawa") — `bible/characters/Koseki-Bijou.md` ([Official KB4])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: the unit B.F.F with Fuwawa and Raora Panthera ("Inu Neko. Seishun Massakari," day 2) — `bible/characters/Mococo-Abyssgard.md` ([Official MC4; Serendipity report])
- 2026-07-09 [day] Cast as "Risa" in the anime "Tenchi Galaxy" — `bible/characters/Nerissa-Ravencroft.md` ([Observed N2 §2026])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) — `bible/characters/Raora-Panthera.md` ([Official RP4, RP9])
- 2026-07-03/04 [day-range] Serendipity concert, duo with Mori Calliope — `bible/characters/Shiori-Novella.md` ([Official SN4])
- 2026-07-30 [day] "Into The Void" motion comic begins — `bible/characters/Shiori-Novella.md` ([Observed SN3])
- 2026-07-03/04 [day-range] Serendipity: Shiori–Calli, Bijou–Kiara, FUWAMOCO–Raora, Nerissa–Elizabeth — `bible/world/Advent-Pairs.md` (official interviews)
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: the unit B.F.F with Raora ("Inu Neko. Seishun Massakari") — `bible/world/FUWAMOCO.md` ([Official S4; Serendipity report])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: units Autofister (Gigi & Cecilia), Bloodraven (Nerissa & Elizabeth), B.F.F (FUWAMOCO & Raora); guests' songs with Justice members: "HELP!!" (Kobo, Bae, Elizabeth), "Break It Down" (Zeta, Shiori, Cecilia), "Cloudy Sheep" (Watame, Calli, Cecilia), "MAKE IT, BREAK IT" (Zeta, FUWAMOCO, Gigi), "What an amazing swing" (Watame, Kiara, Raora) — `bible/world/Justice-Pairs.md` ([Official S3, S7])
- 2026-07-03/04 [day-range] Serendipity concert, Los Angeles — `bible/world/OctoClock.md` (Their stage pairing)
- 2026-07-03/04 [day-range] Serendipity pairs: Shiori–Calli, Bijou–Kiara, Nerissa–Elizabeth, FUWAMOCO–Raora — `bible/world/hololive--Advent.md` ([Official S7, S10])
- 2026-07-03/04 PDT [day-range, PDT] Serendipity: day 1 "SUPERNOVA SUPER GIRL" (Justice); Autofister (Gigi & Cecilia, "CCGG MADNESS"); "HELP!!" (Kobo Kanaeru with Bae and Elizabeth); "Break It Down" (Vestia Zeta with Shiori and Cecilia); "Cloudy Sheep" (Tsunomaki Watame with Calli and Cecilia). Day 2: the Advent+Justice medley ("Rebellion," "ABOVE BELOW"); Bloodraven (Nerissa & Elizabeth, "Cruel Angel's Thesis"); "MAKE IT, BREAK IT" (Zeta, FUWAMOCO and Gigi); "What an amazing swing" (Watame with Kiara and Raora); B.F.F (FUWAMOCO & Raora, "Inu Neko. Seishun Massakari") — `bible/world/hololive--Justice.md` ([Official S6, S8])
- 2026-07-03/04 PDT [day-range, PDT] **EN 4th concert "Serendipity"** (Shrine Auditorium, Los Angeles), built around units: Last Writes (Calli–Shiori), Octo'clock (Ina–Kronii), Rocku Wawa (Kiara–Bijou), BaeRyS (IRyS–Bae), Bloodraven (Nerissa–Elizabeth), B.F.F (FUWAMOCO–Raora), Autofister (Gigi–Cecilia); guests Ookami Mio, Kobo Kanaeru, Vestia Zeta, Tsunomaki Watame (official report) — `bible/world/hololive-History-2023-2026.md` (The current partnerships)
- 2026-07/08 [month-range] Shiori's original motion comic "Into The Void" (with Elizabeth, Gigi, Nerissa); Advent's 3rd-anniversary 3D live "Bound by Fate"; FUWAMOCO announce their first album (08-29) — `bible/world/hololive-History-2023-2026.md` (—)
- 2026-07-23 [day] Rhythm game "hololive Dreams" released — `bible/world/hololive-History-2023-2026.md` (—)
- 2026-07-03/04 [day-range] hololive English 4th concert "Serendipity" (LA) — `bible/world/hololive.md` (Partner pairs (e.g. Kronii and Ina))

### 2026-08
- 2026-08-29 [day] First album "FUWAMOCO à la mode" announced — `bible/characters/Fuwawa-Abyssgard.md` ([Observed FW2 §2026; X via wiki])
- 2026-08-23 [day] EP "Way 2 U" (five tracks, including the earlier "Daydream") — `bible/characters/Ouro-Kronii.md` (Adds to earlier solo music [Official K7])
- 2026-08-29 [day] First album "FUWAMOCO à la mode" announced — `bible/world/FUWAMOCO.md` (hand-signed copies)
- 2026-08/09 [month-range] Official -Justice- merch tie-ins: Bandai Namco Amusement America pop-up (2026-08-27), Pinfinity AR pins (2026-09-30) — `bible/world/hololive--Justice.md` ([Official S1 news])

### 2026-09
- 2026-09-30 [day] Alum; her history stays part of Myth's shared memory — `bible/characters/Gawr-Gura.md` ([Adaptation])
- 2026-09-07 [day] Branch merger; her unit is "hololive -Promise-" — `bible/characters/IRyS.md` ([Observed R2])
- 2026-09-07 [day] The branches merge into one "hololive." Her unit is now hololive -Myth-. — `bible/characters/Mori-Calliope.md` ([Official C17, C1])
- 2026-09-07 [day] Branches merge; she is "Ninomae Ina'nis from hololive," unit hololive -Myth- — `bible/characters/Ninomae-Inanis.md` ([Official I28] [Observed I10])
- 2026-09-07 [day] Branches merge into one "hololive"; unit is hololive -Promise- — `bible/characters/Ouro-Kronii.md` ([Official K5, K1])
- 2026-09-07 [day] Branches merge; unit is hololive -Myth- — `bible/characters/Takanashi-Kiara.md` ([Official T20, T1])
- 2026-09-05 [day] GreyScaleX (Shiori and Zeta) "Purrfect Pair" merchandise opens — `bible/world/Advent-Pairs.md` ([Official S7])
- 2026-09-19 (announced) [day] Myth 6th anniversary live announced with both — `bible/world/TakaMori.md` (Still side by side)
- 2026-09-07 [day] Branches merge; COVER says it will update members' designs to fit their personalities, activities and future directions — `bible/world/VTuber-Persona-and-Lore.md` (Lore and looks can change officially)
- 2026-09 [month] Renamed "hololive -Advent-" in the merger — `bible/world/hololive--Advent.md` (Current name)
- 2026-09-19 (announced) [day] Myth 6th Anniversary 3D LIVE "Seasons From Within" announced with Calli, Kiara and Ina (S3, an official hololive English post); not verified as held — `bible/world/hololive--Myth.md` (The current three, as announced)
- 2026-09-07 [day] "hololive Next": the female-talent branches unify under **hololive**; new logo; members to get updated designs (Tokino Sora first); "hololive raku" app; TV anime "Odeholo"; 10th-anniversary countdown — `bible/world/hololive-History-2023-2026.md` (The present-day setting)
- 2026-09-18 [day] New unit ASOBI★MAWARI-TAI! reveals its four members (Hyakuto Kyoko, Achichi Mela, Suzuna Tsuzuri, Sorashina Sopia) — `bible/world/hololive-History-2023-2026.md` (—)
- 2026-09-24/25 [day-range] ASOBI★MAWARI-TAI! debut — `bible/world/hololive-History-2023-2026.md` (The newest kouhai at the baseline)
- 2026-09-07 [day] The female-talent branches unify under "hololive" — `bible/world/hololive.md` (Groups become units)

### 2026-10
- 2026-10-06 (upcoming) [day] IRyS's first solo concert "HOPE — `bible/world/hololive-History-2023-2026.md`

### undated/lore
- Lore [lore] An ancient automaton built for eternal servitude (official); secondary lore places her origin in Immerheim; in a public joke she attributed her maid duties to an earlier Justice — `bible/characters/Cecilia-Immergreen.md` ([Official CI1] [X post CI6, secondary])
- Lore [lore] Keeper of "Nature," the second concept created by the gods; a druid with kirin blood — `bible/characters/Ceres-Fauna.md` ([Official F1])
- Lore [lore] The Scarlet Queen and Harbinger of Order from Great Exardia; joined hololive to keep an eye on Advent and to become an idol; human, and not royalty despite the title — `bible/characters/Elizabeth-Rose-Bloodflame.md` ([Official EB1] [Observed EB2 §Lore, secondary])
- Lore [lore] Twin demonic guard dog from the Northwest Passage in the demon world; sealed in The Cell "for being a pain in the godly behind" — `bible/characters/Fuwawa-Abyssgard.md` ([Official FW1] [Observed FW2 §Lore])
- Lore [lore] Descendant of Atlantis (now ruins); swam to land because it was "so boring down there"; bought her clothes at a beachside store, paying in seashells; talks to marine life — `bible/characters/Gawr-Gura.md` ([Official G1] [Observed G2 §Lore])
- Lore [lore] Age jokes put her "somewhere in the 9,000s," with varying numbers across exchanges (9,361, 9,927, 9,485…); no fixed age is adopted. June 20 marks her arrival on land, not a remembered birthday — `bible/characters/Gawr-Gura.md` ([Observed G2 §Gura's age and §Lore])
- Lore [lore] A gremlin "Chaser" from Freesia, "born and raised under the flag of Freedom" — `bible/characters/Gigi-Murin.md` ([Official GG1])
- Lore [lore] A nephilim who was the embodiment of hope in "The Paradise," reawakened in an age of despair to deliver hope through song — `bible/characters/IRyS.md` ([Official R1])
- Lore [lore] Jewel of Emotions; imprisoned in secret after people fought over her; lured in with cake — `bible/characters/Koseki-Bijou.md` ([Official KB1] [Observed KB2 §Lore])
- Lore [lore] Younger twin demonic guard dog; in the prison break she barked at the guards and threw Pero at them — `bible/characters/Mococo-Abyssgard.md` ([Official MC1] [Observed MC2 §Lore])
- Lore [lore] She is the Grim Reaper's first apprentice. Modern medicine hurt the reaping business, so she turned to VTubing to harvest souls. — `bible/characters/Mori-Calliope.md` (Her central premise [Official C1])
- Lore [lore] She comes from an Underworld that looks like a modern city; she blamed debut lag on its bad internet. She waitressed there to save up for a trip to Japan. — `bible/characters/Mori-Calliope.md` (Secondary lore [Observed C4 §Lore and §Miscellaneous])
- Lore [lore] Guardian of "Civilization," the concept made by mankind rather than the gods; chose an owl form; has forgotten her name and age — `bible/characters/Nanashi-Mumei.md` ([Official M1] [Observed M2 §Lore])
- Lore [lore] The Demon of Sound, sealed by the gods in The Cell; one horn broken to limit her power; escaped with Advent — `bible/characters/Nerissa-Ravencroft.md` ([Official N1] [Observed N2 §Lore])
- Lore [lore] Picked up a strange book, gained tentacle powers and began hearing Ancient Whispers; VTubes "to deliver random sanity checks on humanity, as an ordinary girl" — `bible/characters/Ninomae-Inanis.md` ([Official I1])
- Lore [lore] Warden of "Time", the third concept created by the gods and the one most tied to humankind — `bible/characters/Ouro-Kronii.md` (Supervisory, haughty office [Official K2])
- Lore [lore] A big cat from the Romance Empire who prepares Justice's criminal reports; sent after FUWAMOCO, she got distracted by crane games — `bible/characters/Raora-Panthera.md` ([Official RP1] [Observed RP2 §Lore])
- Lore [lore] The Archiver; imprisoned in The Cell for forbidden knowledge; masterminded Advent's prison break — `bible/characters/Shiori-Novella.md` ([Official SN1] [Observed SN2 §Lore])
- Lore [lore] Phoenix idol who dreams of owning a fast-food chain; reborn from her ashes — `bible/characters/Takanashi-Kiara.md` ([Official T1])
- Lore [lore] CEO of KFP (Kiara Fried Phoenix); employees are chickens; the Usual Room; she denies KFP is a cult — `bible/characters/Takanashi-Kiara.md` ([Observed T2 §KFP, secondary])
- Lore (secondary-reported; original statements and continuity scope unverified; outside the baseline) [lore] Born circa the early 1920s and thrown forward in time; the pocket watch holds a time crystal; time travel makes loud screeching noises and can cause headaches; she won't use it to cheat — `bible/characters/Watson-Amelia.md` ([Observed A2 §Time travel, secondary])
- Lore [lore] Became an idol "just out of interest" after rumors of unusual beings in hololive; trains reflexes with shooters and her mind with puzzle games — `bible/characters/Watson-Amelia.md` ([Official A1])

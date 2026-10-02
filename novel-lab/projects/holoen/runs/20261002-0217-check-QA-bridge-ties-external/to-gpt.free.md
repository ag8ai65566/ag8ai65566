# Task 05 — Cross-cohort bridge audit

You are GPT, senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only, answer in English,
and run sequentially without parallel GPT audits.

Bridge: ties (external participants only)
Packet: projects/holoen/research/qa/packets/ties-external.md (inline below)
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

## Scope of this ties pass (Claude, 2026-10-02)

This pass covers **external participants**: people without a card (JP/ID members, DEV_IS, guests, alumni of
other branches) as they appear across all cohorts, using the packet `ties-external.md`. Cast-to-cast pairs and
claims naming more than three people were already compared from both sides by the seven cohort audits, whose
packets hold every outgoing and incoming claim for their members (see `research/qa/audit-*.md`); a separate
cast-ties pass would repeat that work and does not fit the remaining quota. If you see a cross-cohort tie
problem the cohort audits could not have caught, report it here; say in Merge handoff whether a further pass
is needed and what it would cover.

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

### projects/holoen/research/qa/packets/ties-external.md

# Bridge packet: ties (cast × reference-only people)

Snapshot: git c06ffa3. Every [SW] sentence and dossier row/bullet that names both people, grouped by
pair (names and short names matched; a sentence naming three people appears under each pair).

### AZKi × Mori Calliope
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019-05-19 | AZKi and Hoshimachi Suisei (formerly independent) join under the INoNaKa Music label; Suisei moves to hololive's main branch on 2019-12-01 | Calli's starstruck senpai Suisei |

### Airani Iofifteen × Gigi Murin
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Airani Iofi (ID), Pavolia Reine (ID) | "Fanfic Club" with Gigi | Monster Hunter Wilds with Iofi and Jurard (2025) | [Observed SN2; SN3] |
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club."

### Banzoin Hakka × Elizabeth Rose Bloodflame
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Banzoin Hakka (HOLOSTARS) | Duet partner | A "Mephisto" cover (2025-01-18); archived credits list Elizabeth's production and vocal-arrangement work | [Observed EB3, archived credits] |

### Cecilia Immergreen × Oozora Subaru
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-08-23/24 | -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora | [Official KB5] |

### Cecilia Immergreen × Vestia Zeta
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity.
- `bible/characters/Gigi-Murin.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice and "CCGG MADNESS" as Autofister with Cecilia (day 1); "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official GG4, GG9] |
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Mococo / FUWAMOCO | Advent ("GigiMoco," "bauBau"; secondary) | Secondary accounts: with Cecilia, a guest-host prank on FUWAMOCO MORNING #167 (2025-07-28); "Bright Tonight" (2025) and "MAKE IT, BREAK IT" with Zeta at Serendipity (2026) with both twins | [Observed GG2; Mococo file] [Official GG7, GG9] |
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Cecilia and Vestia Zeta: "Break It Down" at Serendipity.

### Ceres Fauna × Hakos Baelz
- `bible/characters/Ceres-Fauna.md › Behavioral Traits`: 6. She knows "surprisingly deep" cursed memes and plays horror games often, alone and with friends (Bae's and Fauna's "MONTH OF HORRORS," 2022). [Official F1] [Observed F3 titles]
- `bible/characters/Ceres-Fauna.md › Story Engine`: 5. A horror game with Bae where Fauna is calm and Bae is not, until the jump scare.
- `bible/characters/Ouro-Kronii.md › Behavioral Traits`: 5. When complimented, she may accept it deadpan ("I know.") [Observed K9, secondary snippet]. Fauna described a "gap moe" side of her [Observed K8 §Personality, secondary]. [Unverified, title only: that sincere or physical affection flusters her, e.g. Bae suddenly holding her hand (K27 clip title). Off the card until a transcript or recording is checked.]

### Ceres Fauna × Tsukumo Sana
- `bible/characters/Ceres-Fauna.md › Relationship Map`: | Tsukumo Sana | Council genmate (graduated 2022) | Sana designed the Council's "Beeg Smol" models; Fauna: "Go give [Sana] lots of love because she deserves it, even though she's a little bit... disgusting." | [Observed F2 §Quotes, secondary] |
- `bible/characters/Ceres-Fauna.md › [SW] Relationships`: Tsukumo Sana (graduated 2022): Council genmate who designed the "Beeg Smol" models; Fauna encouraged fans to support her while mixing praise with a disgust joke.

### Elizabeth Rose Bloodflame × Vestia Zeta
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Vestia Zeta | ID senior | Sang "Giri Giri" with her at her 2025 3D showcase; Elizabeth arranged it as a duet, choreographed it and taught Zeta the dance ("Zeta hit it out of the park") | [ASR EB20, Rk03Rh8P9ps 0:28:09–0:30:11; both models] |
- `bible/characters/Elizabeth-Rose-Bloodflame.md › [SW] Relationships`: Vestia Zeta (ID): her duet partner for "Giri Giri" at her 2025 3D showcase, which Elizabeth arranged and choreographed.

### Gavis Bettel × Shiori Novella
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Shiori Novella | Advent senior ("NovelFlame," "BloodQuill," secondary) | Credited in Shiori's non-canon motion comic "Into The Void" (2026); R.E.P.O. with Shiori, Flayon, Jurard and Gavis Bettel (2025) | [Observed EB2, EB3] |

### Gawr Gura × Houshou Marine
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate; fellow member of the official unit UMISEA (2021, with Aqua and Marine; the wiki also lists Chloe) | Ina drew chibi Bloop and warns that anyone who makes Gura cry faces "the wrath of Ina"; co-op games | [Observed G2 §Gura's antics and §Mascots and fans; G16] [Official G17] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate; fellow member of the official unit UMISEA (2021, with Minato Aqua and Houshou Marine; the wiki also lists Sakamata Chloe) [Official I31] | Ina says anyone who makes Gura cry will "face the wrath of Ina"; Ina drew chibi Bloop; a prank war is reported but [Unverified] | [Observed I2 §Relationships; Gura file G2 §Gura's antics and §Mascots and fans] |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |

### Gawr Gura × Pavolia Reine
- `bible/world/Cross-Branch-Friends.md › By Character`: - **Gawr Gura** (graduated): "Apex Predators" (Shishiro Botan), UMISEA, "SharPea" (Pavolia Reine), and Murasaki Shion (Minecraft and Mario Kart in 2021; a "Renai Circulation" duet cover, 2022). [Observed S1; S2 Gura]

### Gigi Murin × Pavolia Reine
- `bible/characters/Shiori-Novella.md › Relationship Map`: | Airani Iofi (ID), Pavolia Reine (ID) | "Fanfic Club" with Gigi | Monster Hunter Wilds with Iofi and Jurard (2025) | [Observed SN2; SN3] |
- `bible/characters/Shiori-Novella.md › [SW] Relationships`: Pavolia Reine and Airani Iofi (ID) with Gigi: the "Fanfic Club."

### Gigi Murin × Vestia Zeta
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity.
- `bible/characters/Gigi-Murin.md › [SW] Background`: (Gigi helped with the lyrics and designed the chibi models) and sang it at the Serendipity concert, where Gigi also sang "MAKE IT, BREAK IT" with Vestia Zeta and FUWAMOCO.

### Hakos Baelz × IRyS
- `bible/characters/IRyS.md › [SW] Relationships`: (born from a Minecraft bento; their joke fan-fiction made "Monopoly" a fandom euphemism), and a creative partner: at their 2026 Serendipity duo stage IRyS said she leans on Bae's "strong vision" when she's indecisive, and Bae, who met IRyS as her "very first senpai," admires her humor that makes everyone comfortable; they call their dynamic "a can of worms."
- `bible/characters/Mori-Calliope.md › Background Timeline`: | 2022 | CHADCast begins with IRyS and Hakos Baelz. | [Observed C12] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | IRyS, Hakos Baelz | CHADCast cohosts | A chaotic podcast trio. Bae calls her "Cori Malliope." | [Observed C12; C4 nickname list, secondary] |
- `bible/characters/Mori-Calliope.md › [SW] Background`: She co-hosts the CHADCast podcast with IRyS and Hakos Baelz, and she started a 2026 performance partnership with Shiori Novella.
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: IRyS and Hakos Baelz: her CHADCast cohosts ("Chaos, Hope, and Death"); Bae calls her "Cori Malliope," and IRyS joined her as the "Two Pink Women" of Silent Hill 2.
- `bible/characters/Ouro-Kronii.md › Behavioral Traits`: 7. [Unverified, title only] When someone else is easier to frighten, she helps set up the scare (with IRyS, on Baelz). [K16 clip title; off the card]
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Hakos Baelz | Council/Promise genmate | Bae called her "too talented, savage, and a 'tsundere granny'". [Unverified, title only: Bae suddenly holding her hand; Kronii and IRyS scaring Bae together] | [Observed K8 §Personality, secondary; K27, K16 clip titles] |
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Colleagues: by name or short form (Ina, Bae, IRyS).
- `bible/world/Concerts-and-Live-Events.md › The Cast on Stage`: | IRyS | Promise musical "The Broken Promise" (2024-12-14); 3D lives "The Devil Wears Hope" (2024-11-17), "HOPE UPON A STAR" (2025-03-16), "Racing Towards Hope" (2026-03, race-queen outfit); World Tour '25 lead; Serendipity with Hakos Baelz; first solo concert "HOPE ||: Beyond the Stars," Tokyo, 2026-10-06 | IRyS file R2, R3; S1 |
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: IRyS and Calli: Calli collabed with her on July 29, 2021, eighteen days after IRyS's debut; with Bae they host CHADCast ("Chaos, Hope, and Death!"), and they still team up (Silent Hill 2 as "Two Pink Women," karaoke).
- `bible/world/hololive--Promise.md › Conflicts and Story Hooks`: 6. Bae announces another BaeRyS "divorce"; IRyS demands the potato bento back.
- `bible/world/hololive--Promise.md › Hard Facts`: - Unverified title-only bits (Bae holding Kronii's hand, scaring Bae with IRyS) are not facts.
- `bible/world/hololive--Promise.md › How the Group Works`: - **IRyS and Bae at Serendipity (2026):** paired for the 4th concert, their first stage as a duo. IRyS: Bae "always has a strong vision" for projects, so when IRyS is "indecisive or wishy-washy" she turns to Bae's opinion, and she admires Bae's creativity; Bae: IRyS was "the very first senpai I had ever met," and she admires IRyS's "easy-going nature and natural humor" that makes everyone "laugh and feel comfortable." Their unit dynamic, in their words: "a can of worms lol" (IRyS), "Complicated XD" (Bae). [Official S6]
- `bible/world/hololive--Promise.md › Members and Status`: - Active: IRyS, Ouro Kronii, Hakos Baelz. [Observed S1 member table]
- `bible/world/hololive--Promise.md › One-line Concept`: 2023. After two graduations in 2025, the active members are IRyS, Ouro Kronii and Hakos Baelz.
- `bible/world/hololive--Promise.md › [SW] Description`: IRyS and Bae keep the "BaeRyS" bit of being "married" and "divorced," which turned "Monopoly" into a fandom euphemism, and they are also creative partners: paired for the 2026 Serendipity concert, IRyS leans on Bae's "strong vision" when she's indecisive, Bae admires IRyS's humor that makes everyone comfortable, and they call their dynamic "a can of worms" and "Complicated."
- `bible/world/hololive--Promise.md › [SW] Description`: The group of Ouro Kronii and IRyS, hololive -Promise-: IRyS, Ouro Kronii and Hakos Baelz at the 2026 baseline.

### Hakos Baelz × Koseki Bijou
- `bible/characters/IRyS.md › [SW] Relationships`: At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou.
- `bible/world/Advent-Pairs.md › With Promise`: - **Hakos Baelz:** "BaeBi" with Bijou (#BAEBISleepOver, 2024-08-11). [Observed S1]

### Hakos Baelz × Mori Calliope
- `bible/characters/IRyS.md › Relationship Map`: | Mori Calliope | First collab partner (2021) | "MorIRyS"; CHADCast podcast trio with Bae | [Observed R2 §2021, units] |
- `bible/characters/IRyS.md › [SW] Relationships`: Mori Calliope: her first collab partner (2021) and a CHADCast cohost with Bae.
- `bible/world/IRyS-and-Nerissa-Pairs.md › [SW] Description`: IRyS and Calli: Calli collabed with her on July 29, 2021, eighteen days after IRyS's debut; with Bae they host CHADCast ("Chaos, Hope, and Death!"), and they still team up (Silent Hill 2 as "Two Pink Women," karaoke).

### Hakos Baelz × Nanashi Mumei
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Nanashi Mumei (graduated) | Council genmate ("KronMei") | [Unverified, title only: the "Flower" bit with Mumei and Baelz; Mumei accidentally blowing up the Bunkeronii's entrance] | [Observed K14 clip, K8 §Quotes and §Relationships, secondary; K28 clip titles] |
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - "Flower." → quote [Observed K8 §Quotes, secondary]; the flat, repeated Minecraft bit with Baelz and Mumei is [Unverified, K14 clip title; off the card].

### Hakos Baelz × Nerissa Ravencroft
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |

### Hakos Baelz × Ninomae Ina'nis
- `bible/characters/Ouro-Kronii.md › Voice Profile`: - Colleagues: by name or short form (Ina, Bae, IRyS).
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 EDT | World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 | — |

### Hakos Baelz × Ouro Kronii
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Hakos Baelz | Council/Promise genmate | Bae called her "too talented, savage, and a 'tsundere granny'". [Unverified, title only: Bae suddenly holding her hand; Kronii and IRyS scaring Bae together] | [Observed K8 §Personality, secondary; K27, K16 clip titles] |
- `bible/world/hololive--Promise.md › Conflicts and Story Hooks`: 1. Kronii and Bae dare each other through a horror game; the "tsundere granny" line comes back.
- `bible/world/hololive--Promise.md › Hard Facts`: - Unverified title-only bits (Bae holding Kronii's hand, scaring Bae with IRyS) are not facts.
- `bible/world/hololive--Promise.md › Members and Status`: - Active: IRyS, Ouro Kronii, Hakos Baelz. [Observed S1 member table]
- `bible/world/hololive--Promise.md › One-line Concept`: 2023. After two graduations in 2025, the active members are IRyS, Ouro Kronii and Hakos Baelz.
- `bible/world/hololive--Promise.md › [SW] Description`: The group of Ouro Kronii and IRyS, hololive -Promise-: IRyS, Ouro Kronii and Hakos Baelz at the 2026 baseline.

### Hakos Baelz × Shiori Novella
- `bible/characters/Mori-Calliope.md › [SW] Background`: She co-hosts the CHADCast podcast with IRyS and Hakos Baelz, and she started a 2026 performance partnership with Shiori Novella.

### Hakos Baelz × Takanashi Kiara
- `bible/world/hololive-History-2023-2026.md › Timeline`: | 2024-08-23 EDT | World Tour '24 "-Soar!-" opens at Anime NYC (Javits Center) with Kiara, Ina and Bae among seven performers; it ends in Taipei on 2025-01-18 | — |

### Hoshimachi Suisei × Mori Calliope
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 1. Calli hosts another watch party for Suisei's concert and loses her composure on the high note.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones"
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Calli and Ina** (26 / 26 / 8 / 15 / 8 / 9; 2 in 2026): Ina designed Calli's Death Sensei and drew the cover of Calli's debut EP; Calli wrote the lyrics of Ina's 2026 song "TAKO∞TAKOVER." Calli is a recurring target of Ina's puns ("Every freaking time, Ina."). They watched Suisei's concert together in an off-collab (2023-02-20) and still game together (Elden Ring Nightreign, 2025-06). [Observed S5 Ina §Miscellaneous; Calli file C28; Ina file I8; S1]
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019-05-19 | AZKi and Hoshimachi Suisei (formerly independent) join under the INoNaKa Music label; Suisei moves to hololive's main branch on 2019-12-01 | Calli's starstruck senpai Suisei |

### Hoshimachi Suisei × Ninomae Ina'nis
- `bible/world/Myth-and-Kronii-Other-Pairs.md › Pairs`: - **Calli and Ina** (26 / 26 / 8 / 15 / 8 / 9; 2 in 2026): Ina designed Calli's Death Sensei and drew the cover of Calli's debut EP; Calli wrote the lyrics of Ina's 2026 song "TAKO∞TAKOVER." Calli is a recurring target of Ina's puns ("Every freaking time, Ina."). They watched Suisei's concert together in an off-collab (2023-02-20) and still game together (Elden Ring Nightreign, 2025-06). [Observed S5 Ina §Miscellaneous; Calli file C28; Ina file I8; S1]

### Houshou Marine × Mococo Abyssgard
- `bible/characters/Fuwawa-Abyssgard.md › Core Drive`: - **Want:** with Mococo, to protect the Ruffians' smiles; their debut list held more than a hundred goals (sing with Houshou Marine, a solo concert, an anime song, a scale figure). [Official FW1, FW4] [Observed FW2 §Hopes and dreams, secondary]

### Houshou Marine × Nerissa Ravencroft
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 4. Nerissa meets Marine at an event and forgets every word of Japanese.

### Houshou Marine × Ninomae Ina'nis
- `bible/characters/Gawr-Gura.md › Relationship Map`: | Ninomae Ina'nis | Myth genmate; fellow member of the official unit UMISEA (2021, with Aqua and Marine; the wiki also lists Chloe) | Ina drew chibi Bloop and warns that anyone who makes Gura cry faces "the wrath of Ina"; co-op games | [Observed G2 §Gura's antics and §Mascots and fans; G16] [Official G17] |
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Gawr Gura (graduated) | Myth genmate; fellow member of the official unit UMISEA (2021, with Minato Aqua and Houshou Marine; the wiki also lists Sakamata Chloe) [Official I31] | Ina says anyone who makes Gura cry will "face the wrath of Ina"; Ina drew chibi Bloop; a prank war is reported but [Unverified] | [Observed I2 §Relationships; Gura file G2 §Gura's antics and §Mascots and fans] |
- `bible/world/Myth-and-Kronii-Other-Pairs.md › History`: | 2021-09 | UMISEA formed (Ina, Gura, Aqua, Marine; Chloe joined later) | Ocean unit |

### Houshou Marine × Takanashi Kiara
- `bible/characters/Nerissa-Ravencroft.md › Behavioral Traits`: 3. She is an open fangirl of Houshou Marine and Takanashi Kiara (a self-described KFP member); in her lore she worked at KFP before hololive. [Observed N2 §Likes and dislikes, §Lore, secondary]
- `bible/characters/Nerissa-Ravencroft.md › Voice Profile`: | Fangirling (Kiara, Marine) | Fast, flustered, delighted | (no verified line; see Relationship Map) |

### IRyS × Kaela Kovalskia
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Kronii's steadiest cross-branch partner: Kaela. IRyS's closest JP friend: Flare.

### IRyS × Ookami Mio
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.

### IRyS × Tsukumo Sana
- `bible/world/hololive--Promise.md › Members and Status`: - Council history: Tsukumo Sana graduated from -Council- on 2022-07-31, before Promise existed; she was never a Promise member. IRyS and the four remaining Council members formed Promise in October 2023.

### Inugami Korone × Nanashi Mumei
- `bible/world/Fauna-and-Mumei-Pairs.md › [SW] Description`: Beyond EN, Mumei recorded a duet cover with Inugami Korone in her last week.

### Kaela Kovalskia × Koseki Bijou
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Kaela Kovalskia | ID senior ("SMITTEN"; "Graondstone" with Bijou; secondary) | Lethal Company, Don't Starve Together, Buckshot Roulette, PEAK; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement (secondary) | [Observed RP2, RP3] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Kaela Kovalskia ("SMITTEN"): co-op partner; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement; with Koseki Bijou they are "Graondstone."
- `bible/world/Advent-Pairs.md › Conflicts and Story Hooks`: 3. Kaela and Bijou build something enormous in silence while chat panics.
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Raora Panthera:** "Graondstone" with Bijou and Kaela; FUWAMOCO's 2026 Serendipity unit partner (B.F.F), who drew them a shikishi before her debut. [Official S6] [Observed S1]
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Of Advent: Bijou and Kaela Kovalskia are "Grindstone"

### Kaela Kovalskia × Ouro Kronii
- `bible/characters/Ouro-Kronii.md › Relationship Map`: | Kaela Kovalskia | hololive ID ("TimeSmith") | Kaela is a fan of Kronii's voice; constant bickering is reported but [Unverified] | [Observed K8 §Relationships, K35, secondary] |
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 2. Kronii and Kaela's endless sim co-op hits the in-game stock market.
- `bible/world/Cross-Branch-Friends.md › Hard Facts`: - Kronii's steadiest cross-branch partner: Kaela. IRyS's closest JP friend: Flare.

### Kaela Kovalskia × Raora Panthera
- `bible/characters/Koseki-Bijou.md › Relationship Map`: | Kaela Kovalskia (ID) | Friend ("Grindstone"; Kaela calls her "Beejoe") | Grindstone collabs include Raft and Minecraft (2023), Split Fiction (2025) and PEAK as "Graondstone" with Raora (archive counts 10 / 23 / 11 / 0) | [Observed KB2; KB3] |
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: (Kaela calls her "Beejoe"): Raft, Minecraft, Split Fiction, and with Raora "Graondstone."
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Kaela Kovalskia | ID senior ("SMITTEN"; "Graondstone" with Bijou; secondary) | Lethal Company, Don't Starve Together, Buckshot Roulette, PEAK; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement (secondary) | [Observed RP2, RP3] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Kaela Kovalskia ("SMITTEN"): co-op partner; their Minecraft and chat role-play includes the running joke that Kaela lives in Raora's basement; with Koseki Bijou they are "Graondstone."
- `bible/world/Advent-Pairs.md › With -Justice-`: - **Raora Panthera:** "Graondstone" with Bijou and Kaela; FUWAMOCO's 2026 Serendipity unit partner (B.F.F), who drew them a shikishi before her debut. [Official S6] [Observed S1]

### Kobo Kanaeru × Mori Calliope
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Kobo Kanaeru | Collaborator | "Uncle Dad" / "Dad" bits; Calli and Kiara play "Dad" and "Mom" to her. [Unverified, title only: Kobo picking up and repeating Calli's swear words] | [Observed C14; C25 §Takamori, secondary; C27 clip titles] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Takanashi Kiara | Myth genmate | Calli calls her "kusotori" ("shitty bird") and usually rebuffs her, while supporting "TakaMori." They play "Mom" and "Dad" to Kobo. | [Observed C7; C25 §Takamori, secondary] |
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo.
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Kobo Kanaeru | Collaborator | Kobo calls her "Mommy Kiwawa"; Kiara and Calli play her "Mom" and "Dad" | [Observed T5-gNEWWDKlTM8 clip title; T2 §Takamori] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Mori Calliope | Myth genmate | Kiara long called Calli her "wife" and coined "TakaMori"; Calli rebuffed her and calls her "kusotori" ("shitbird"). They announced in 2021 that they would tone the ship down (the wiki adds that "the two remain close friends"; a secondary statement, not a documented current relationship); they play "Mom" and "Dad" to Kobo as a performed family bit | [Observed T2 §Takamori, secondary; T14 title] |
- `bible/world/TakaMori.md › Hard Facts`: - Kobo's "parents" bit: Kiara "Mom," Calli "Dad"; "not married, Kobo is adopted."
- `bible/world/TakaMori.md › How It Works`: - They play "Mom" (Kiara, "Mommy Kiwawa") and "Dad" to Kobo Kanaeru; Calli insists she is not married to Kiara and Kobo is adopted. [Observed S2 §Takamori, secondary]

### Kobo Kanaeru × Nerissa Ravencroft
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "HELP!!" with Kobo Kanaeru and Hakos Baelz (day 1); unit Bloodraven with Nerissa, "Cruel Angel's Thesis" (day 2); "SUPERNOVA SUPER GIRL" and "ABOVE BELOW" with Justice | [Official EB4, EB8] |
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Nerissa and Kronii at Serendipity.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity.

### Kobo Kanaeru × Ouro Kronii
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Nerissa and Kronii at Serendipity.
- `bible/characters/Ouro-Kronii.md › [SW] Relationships`: Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii and Nerissa at Serendipity.

### Kobo Kanaeru × Takanashi Kiara
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Kobo Kanaeru | Collaborator | "Uncle Dad" / "Dad" bits; Calli and Kiara play "Dad" and "Mom" to her. [Unverified, title only: Kobo picking up and repeating Calli's swear words] | [Observed C14; C25 §Takamori, secondary; C27 clip titles] |
- `bible/characters/Mori-Calliope.md › Relationship Map`: | Takanashi Kiara | Myth genmate | Calli calls her "kusotori" ("shitty bird") and usually rebuffs her, while supporting "TakaMori." They play "Mom" and "Dad" to Kobo. | [Observed C7; C25 §Takamori, secondary] |
- `bible/characters/Mori-Calliope.md › [SW] Relationships`: Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo.
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Kobo Kanaeru | Collaborator | Kobo calls her "Mommy Kiwawa"; Kiara and Calli play her "Mom" and "Dad" | [Observed T5-gNEWWDKlTM8 clip title; T2 §Takamori] |
- `bible/characters/Takanashi-Kiara.md › Relationship Map`: | Mori Calliope | Myth genmate | Kiara long called Calli her "wife" and coined "TakaMori"; Calli rebuffed her and calls her "kusotori" ("shitbird"). They announced in 2021 that they would tone the ship down (the wiki adds that "the two remain close friends"; a secondary statement, not a documented current relationship); they play "Mom" and "Dad" to Kobo as a performed family bit | [Observed T2 §Takamori, secondary; T14 title] |
- `bible/world/TakaMori.md › Hard Facts`: - Kobo's "parents" bit: Kiara "Mom," Calli "Dad"; "not married, Kobo is adopted."
- `bible/world/TakaMori.md › How It Works`: - **Heard in 2025 (ASR, S6):** in the first Split Fiction stream (Kiara's channel, 2025-04-06) the "parents" bit is alive: when Kobo shows up in chat, they tell her "Hi Kobo, go to bed! … What are you doing out of bed? Go to bed!", wish her a happy anniversary, and apologize: "Sorry Kobo, you can't be part of this because it's two players only. Next time…" When their game characters split into a fire mage and an ice mage, they riff on their own song: "Fire and ice, yeah. Fire and ice, death and life." When the split screen separates them: "Oh, double Takamori." [ASR S6, nE12CyKbaX8 0:07:49, 0:08:01, 0:22:36, 0:13:28; both models agree; who said which line is not separable from the transcript]
- `bible/world/TakaMori.md › How It Works`: - They play "Mom" (Kiara, "Mommy Kiwawa") and "Dad" to Kobo Kanaeru; Calli insists she is not married to Kiara and Kobo is adopted. [Observed S2 §Takamori, secondary]

### Kobo Kanaeru × Watson Amelia
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Ame has "KoMeHa" with Kobo and Iroha.

### Koseki Bijou × Ookami Mio
- `bible/characters/IRyS.md › [SW] Relationships`: At Serendipity she and Bae performed "LUVATORRRRRY!" as BaeRyS, and she sang "Night Loop" with Ookami Mio (GAMERS) and Bijou.

### Koseki Bijou × Oozora Subaru
- `bible/world/Advent-Pairs.md › Inside Advent`: - **Bijou and FUWAMOCO ("Diamond Dogs"):** their first collab was Overcooked 2 (2023-08-08); Bijou's "Rock rock!" parodies "bau bau"; with Subaru they sang "HOT DUCK!" at the 2025 concert. [Observed S2; S1] [Official S5]

### Kureiji Ollie × Ouro Kronii
- `bible/characters/Elizabeth-Rose-Bloodflame.md › Relationship Map`: | Kureiji Ollie | ID senior; her "kami-oshi" (secondary); "HoloRed" | "Code Red" collabs: Liars Bar with Ollie and Jurard (2024), PEAK with Ollie, Flayon and Jurard (2025); "High Tide" with Kronii and Ollie at -All for One-; the 2026 "Yona Yona Dance" cover | [Observed EB2, EB3] [Official EB5] |

### Mococo Abyssgard × Vestia Zeta
- `bible/characters/Gigi-Murin.md › Relationship Map`: | Mococo / FUWAMOCO | Advent ("GigiMoco," "bauBau"; secondary) | Secondary accounts: with Cecilia, a guest-host prank on FUWAMOCO MORNING #167 (2025-07-28); "Bright Tonight" (2025) and "MAKE IT, BREAK IT" with Zeta at Serendipity (2026) with both twins | [Observed GG2; Mococo file] [Official GG7, GG9] |

### Moona Hoshinova × Nerissa Ravencroft
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Moona Hoshinova | ID senior ("V3LVET" with Raora) | Featured on Moona's "100% (feat. Nerissa Ravencroft)" (2025-02-16); Keep Talking and Nobody Explodes together (2024) | [Official N23; N3 title] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Nerissa Ravencroft, Moona Hoshinova | Seniors ("V3LVET," secondary) | Clubhouse Games with Nerissa (2024-12-09); Raft with both (2025-02-06); Monster Hunter Wilds as V3LVET (Nerissa's title, 2025-03-25) | [Observed RP2, RP3; Nerissa archive] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Nerissa Ravencroft and Moona Hoshinova ("V3LVET"): Raft and Monster Hunter Wilds; Clubhouse Games with Nerissa.

### Moona Hoshinova × Raora Panthera
- `bible/characters/Nerissa-Ravencroft.md › Relationship Map`: | Moona Hoshinova | ID senior ("V3LVET" with Raora) | Featured on Moona's "100% (feat. Nerissa Ravencroft)" (2025-02-16); Keep Talking and Nobody Explodes together (2024) | [Official N23; N3 title] |
- `bible/characters/Nerissa-Ravencroft.md › [SW] Relationships`: Raora Panthera: Clubhouse Games (2024); with Moona, Raft and Monster Hunter Wilds as "V3LVET"

### Mori Calliope × Regis Altare
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-07-18/23 | HOLOSTARS English -TEMPUS- (Regis Altare, Magni Dezmond, Axel Syrios, Noir Vesper) announced and debuts | Calli and Kronii's WARS partners Magni and Vesper |

### Mori Calliope × Rikka
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Calli is starstruck by Hoshimachi Suisei ("Death Star"): Suisei sang at Calli's first solo concert and Calli hosts watch parties of Suisei's lives; with HOLOSTARS' Rikka she released "spiral tones"
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2019-06 / 09 | HOLOSTARS, COVER's male group, starts (1st gen, incl. Rikka); 2nd gen in December | Calli's MoRikka partner |

### Mori Calliope × Tsukumo Sana
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Mori Calliope | Myth senior | "ANATOMY REVIEW" streams (with Calli and Sana, 2022; solo, 2025) | [Observed M3] |
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Calli:** "ANATOMY REVIEW with Calli + Sana + Mumei" (2022), a drawing bit Mumei brought back on her own in 2025. [Observed S1]

### Mori Calliope × Tsunomaki Watame
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Tsunomaki Watame (JP), Mori Calliope | Cross-branch; senior | "Cloudy Sheep" at Serendipity (2026) | [Official CI8] |
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Tsunomaki Watame (JP) and Mori Calliope: "Cloudy Sheep" at Serendipity.

### Mori Calliope × Vestia Zeta
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |

### Nanashi Mumei × Tsukumo Sana
- `bible/characters/Nanashi-Mumei.md › Relationship Map`: | Tsukumo Sana | Council genmate (graduated 2022) | Human: Fall Flat (2021); Sana sent a prerecorded message for Mumei's 2022 birthday | [Observed M2 §Miscellaneous; M3] |
- `bible/characters/Nanashi-Mumei.md › [SW] Relationships`: Tsukumo Sana (graduated 2022): Council genmate who sent a recorded message for Mumei's 2022 birthday.
- `bible/world/Fauna-and-Mumei-Pairs.md › With the cast`: - **Calli:** "ANATOMY REVIEW with Calli + Sana + Mumei" (2022), a drawing bit Mumei brought back on her own in 2025. [Observed S1]

### Ninomae Ina'nis × Ookami Mio
- `bible/characters/Fuwawa-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.
- `bible/characters/Mococo-Abyssgard.md › [SW] Relationships`: Ookami Mio (GAMERS) and Ina: "Dottabatta Chindouchuu" at Serendipity.
- `bible/characters/Ninomae-Inanis.md › [SW] Relationships`: Ookami Mio (GAMERS): "Dottabatta Chindouchuu" with Ina and FUWAMOCO at Serendipity.

### Ninomae Ina'nis × Oozora Subaru
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Shiori Novella, Oozora Subaru (JP) | Advent senior; JP senior | "Neko Kaburi-Na" with Ina at -All for One- (2025) | [Official RP5] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Ninomae Ina'nis, Shiori Novella and Oozora Subaru (JP): "Neko Kaburi-Na" on stage; Puyo Puyo Tetris 2 with Ina.

### Ninomae Ina'nis × Shiranui Flare
- `bible/characters/Ninomae-Inanis.md › Relationship Map`: | Shiranui Flare | JP senior | Gave her the nickname "Ore no Ina" | [Observed I2 nickname list] |

### Ookami Mio × Takanashi Kiara
- `bible/characters/Koseki-Bijou.md › [SW] Relationships`: At Serendipity: "Tententengoku Jigokukoku" with Kiara as Rocku Wawa, and "Night Loop" with Ookami Mio (GAMERS) and IRyS.

### Oozora Subaru × Raora Panthera
- `bible/characters/Koseki-Bijou.md › Background Timeline`: | 2025-08-23/24 | -All for One-: "HOT DUCK!" with FUWAMOCO and Subaru; solo "Dead Ma'am's Chest"; "I'm Your Treasure Box" with Cecilia and Raora | [Official KB5] |

### Oozora Subaru × Shiori Novella
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Shiori Novella, Oozora Subaru (JP) | Advent senior; JP senior | "Neko Kaburi-Na" with Ina at -All for One- (2025) | [Official RP5] |
- `bible/characters/Raora-Panthera.md › [SW] Relationships`: Ninomae Ina'nis, Shiori Novella and Oozora Subaru (JP): "Neko Kaburi-Na" on stage; Puyo Puyo Tetris 2 with Ina.

### Ouro Kronii × Regis Altare
- `bible/world/hololive-History-to-2022.md › Timeline`: | 2022-07-18/23 | HOLOSTARS English -TEMPUS- (Regis Altare, Magni Dezmond, Axel Syrios, Noir Vesper) announced and debuts | Calli and Kronii's WARS partners Magni and Vesper |

### Ouro Kronii × Tsukumo Sana
- `bible/world/hololive--Promise.md › [SW] Description`: It grew from the English -Council- generation (August 2021), whose personas were themed around concepts (Kronii is Time); Sana graduated from Council in 2022, before Promise existed.

### Pavolia Reine × Takanashi Kiara
- `bible/world/Cross-Branch-Friends.md › Conflicts and Story Hooks`: 5. Kiara and Reine plan another "vacation" in VR.
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI").

### Shiori Novella × Vestia Zeta
- `bible/characters/Cecilia-Immergreen.md › Relationship Map`: | Vestia Zeta (ID) | Cross-branch | "Break It Down" with Shiori at Serendipity (2026) | [Official CI8] |
- `bible/characters/Cecilia-Immergreen.md › [SW] Relationships`: Vestia Zeta (ID) and Shiori: "Break It Down" at Serendipity.
- `bible/world/Advent-Pairs.md › History`: | 2026-09-05 | GreyScaleX (Shiori and Zeta) "Purrfect Pair" merchandise opens | [Official S7] |

### Takanashi Kiara × Tsunomaki Watame
- `bible/characters/Raora-Panthera.md › Background Timeline`: | 2026-07-03/04 PDT | Serendipity: "SUPERNOVA SUPER GIRL" with Justice (day 1); the unit B.F.F with FUWAMOCO ("Inu Neko. Seishun Massakari"), "What an amazing swing" with Tsunomaki Watame and Kiara, and "ABOVE BELOW" in the Advent+Justice medley (day 2) | [Official RP4, RP9] |
- `bible/characters/Raora-Panthera.md › Relationship Map`: | Tsunomaki Watame (JP) | JP senior | "What an amazing swing" with Kiara at Serendipity (2026) | [Official RP9] |
- `bible/characters/Raora-Panthera.md › [SW] Background`: Seishun Massakari") and sang "What an amazing swing" with Tsunomaki Watame and Takanashi Kiara.

### Takanashi Kiara × Usada Pekora
- `bible/world/Cross-Branch-Friends.md › [SW] Description`: Kiara's oshi is Usada Pekora; Pavolia Reine is a recurring collaborator ("PavoNashi"; both in the bird unit "HOLOTORI").

### Takanashi Kiara × Vestia Zeta
- `bible/characters/Watson-Amelia.md › Background Timeline`: | 2025–2026 | Other reported appearances (Kiara's concerts, announcer at Zeta's birthday live 2025-11, a call "from 2021" at Calli's charity karaoke 2026-02): [Unverified locators] — event links in A8 and A19, segment timestamps not yet found; off the card | [A8, A19] |

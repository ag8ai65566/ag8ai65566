# 接續步驟（給下一個 session 或排程喚醒的 Claude）

狀態（2026-10-02 12:31 UTC）：第二批審查 C、D 已併入並收錄（Marine、Noel、Lamy、Botan、Vivi、JP Senpai Pairs 2；
共 28 位、27 張世界卡）。E 跑到一半撞 GPT 額度，重置 16:42 UTC，send_later 16:43 會叫醒、重開 gpt-resume
（log：scratchpad gpt_resume7.log）。佇列：E（La+ run）→ F（Chloe run）→ 聲音 v1、v2 → QA 審計 12 項。
- 合併方法：scratchpad `merge/`（apply.py、各卡 *.py、d_cross.py）；GPT 打不開的連結先用本地 rtmeta／rtjp／rtjp2
  標題核對，查得到就保留並在 Merge Record 寫影片 ID。
- E、F 的提示已依 C、D 的修正重建（La+ 草稿的 poker 名單、#マリラプ 已改）。F 合併後：`mk_voice_audit.py v3` 建 v3
  並插進佇列（放在 QA 審計前）。
- DEV_IS 在 2026-09-07 官方改組（run D）：Vivi 卡已改；hololive.md 的「hololive DEV_IS」分支描述留給 global 審計。

狀態（2026-10-02 07:55 UTC）：等 GPT 額度（11:31 UTC 重置；send_later 11:32 會叫醒、開跑 gpt-resume）。這段時間做完：
- 引句範圍：32 個 span 候選全部處理（`span_check.py` 0 筆；V13 只剩等 09 聲音審計）；V14 自動候選 0 筆。
- 關係網：JP 四人 ↔ EN、第二批 ↔ JP 四人/EN 的回填互指，one-way 29 → 16 → 1（08:25 再壓縮上限卡的句子補齊；只剩 Raora→IRyS，IRyS 沒空間。原本剩下的在 350 字上限的卡：Calli、
  Kiara、Ina、Kronii、IRyS）。第二批回填句已收錄，GPT D/F 會一起核對（mk_b2_review 自動帶入）。
- 新增 QA 審計 run：`20261002-0751-check-QA-cohort-{jp,jp2,holox}`，排在佇列最後（開跑前自動用 bible 重建 packet）。
- 草稿發佈包 r01-draft 重建（23 位＋26 張世界卡）；START-HERE 列出第二批「還沒收錄」。
- **09 聲音審計**（V13/V19，表演表 stamp 的前提）：`framework/prompts/gpt-voice-audit.md`＋`tools/mk_voice_audit.py`。
  v1（Myth＋Promise）、v2（Advent＋Justice）已排在 F 之後；v3（JP 十四人）等第二批收錄後
  `python3 tools/mk_voice_audit.py v3` 再插進佇列。結果合併到 `research/qa/voice-delivery.md`（逐條處置），
  卡片欄位走 run 的 final.md＋promote，表演表直接改，attestation 為 OK 的表用 `release.py stamp-sheets` 蓋章。

狀態（2026-10-02 08:00 UTC）：**JP 四人全部收錄**（A＝Suisei＋AZKi、B＝Ayame＋Okayu＋JP Senpai Pairs，一輪 GPT 後
作者裁決收錄；EN 回填句依 B 的審查修正：Calli 的 Suisei 生日 live 嘉賓刪除、Kiara 的 HOLOTALK 標成存檔紀錄、
Ina/Cross-Branch 只留「Kurukuru Cruise」、IRyS 的 High Tide 補 Moona、FUWAMOCO 的 AZKi/Okayu 句帶來源層級、
Gura 的 Dodgers 措辭、Gigi 的 Okayu 節慶互動、Mumei 的 HOLOTALK 改日期；TakoNeko 別名歸 JP Senpai Pairs）。
- **第二批**（Marine、Noel、Lamy、Botan、Vivi ＋ holoX 五人 ＋ holoX 卡 ＋ JP Senpai Pairs 2）：卡片、音檔報告
  （research/audio-check/{marine,noel,lamy,botan,vivi,laplus,lui,koyori,chloe,iroha}.md）、表演表（export/elevenlabs/，
  只用兩模型共有的引句、官方句與標明的 style demo）都完成；EN 卡的回填句已一起收錄（promotions.md 註明「GPT 輪次待跑」）。
- **GPT 佇列**（`.gpt-quota.json`，11:31 UTC 重置後依序）：C＝Marine＋Noel＋Lamy（Marine run）→ D＝Botan＋Vivi＋
  JP Senpai Pairs 2＋回填句（Botan run）→ E＝La+＋Lui＋Koyori（La+ run）→ F＝Chloe＋Iroha＋holoX＋回填句（Chloe run）
  → 之後才是 global → justice → myth1 → myth3 → myth4 → myth2 → promise → bridge events → ties-external。
  重建提示：`python3 tools/mk_b2_review.py`。審查回來 → 併進 claude-draft → 寫 final.md（Merge Record）→
  `lab.py promote <run> --force --reason "Author decision (2026-10-02): … run C/D/E/F …"` → promote-changed →
  export → `qa_packets.py holoen` → validate → commit/push。
- 已知：V18（表演表都還沒 stamp，等 09 聲音審計後 `release.py stamp-sheets`）；V13 的 Fauna:85 是舊的 span 候選；
  V08 baerys 別名（Bae 合併時已知）。

狀態（2026-10-02 06:28 UTC）：**JP 四人完成初稿**（Suisei、AZKi、Ayame、Okayu ＋ JP Senpai Pairs）：卡片、
音檔報告（research/audio-check/{suisei,azki,ayame,okayu}.md，日語兩模型、引句全部核對）、表演表（export/elevenlabs/）。
GPT 一輪審查已排在 Bae 之後：A＝Suisei＋AZKi（Suisei run 的 to-gpt.free.md），B＝Ayame＋Okayu＋JP Pairs＋EN 回填句
（Ayame run）；重建用 `tools/mk_jp_review.py`。審查回來 → 併入 → final.md → promote（連同 Bae 與 EN 回填）。
第二批（Marine、Noel、Lamy、Botan、Vivi ＋ holoX 五人 ＋ holoX 卡 ＋ JP Senpai Pairs 2）：run 資料夾已建、COHORTS
加 `jp2`、`holox`；La+ 的 stem 用 `Laplus-Darknesss`（避免「+」）。研究資料在 scratchpad `jp2/`。Chloe 已於
2025-01-26 結束一般活動、保留 affiliate（同 Ame 處理）。

狀態（2026-10-02 06:12 UTC）：**作者第三則命令**：JP 四人之後做 Marine、Noel、Lamy、Botan 與 holoX 全員
（La+、Lui、Koyori、Chloe、Iroha）＋ holoX 世界觀卡；不要閒下來。研究抓取在 scratchpad `jp2/`（fetch2.sh：
wiki、日文維基、官方頁、ragtag）。四人做完 → 立刻開下一批；GPT 審查依批次排隊（每批兩到三人一輪）。

狀態（2026-10-02 05:50 UTC）：**作者下令加入 hololive JP 的 Suisei、AZKi、Ayame、Okayu**（完整卡＋表演表＋關係網）。
- runs：`20261002-0529-character-{Hoshimachi-Suisei,AZKi,Nakiri-Ayame,Nekomata-Okayu}`、`20261002-0529-world-JP-Senpai-Pairs`。
  COHORTS 新增 `jp`（四人＋JP-Senpai-Pairs）；release 的 CAST_ORDER/WORLD_ORDER 已加。
- 研究：wiki（fandom API）、日文維基、官方頁、ragtag 檔案（EN 與 JP 頻道）；EN 卡的回填（Calli、Kiara、Ina、IRyS、
  Fuwawa、Mococo、Gura、Gigi）已寫進各 run 的 final.md（Merge Record 有記），跟 Bae 的回填一起等 promote。
- 音檔：scratchpad `jp/`（多語 small＋medium，`jacheck.py`、`jconfirm.py`、`jstats.py`）；2026 年 16 個窗口。
  私事（家人、童年、旅行、受傷、生病、計程車等日常）一律不引用不摘要。
- 待辦：四張卡寫完 → audio-check 報告（research/audio-check/{suisei,azki,ayame,okayu}.md）→ 表演表 →
  GPT 一輪審查（兩個 run：Suisei+AZKi、Ayame+Okayu+JP Pairs），排在 Bae 之後。

狀態（2026-10-02 04:25 UTC）：**作者使用指南完成**（d21f6ee）。`framework/templates/start-here-zh.md` 是發佈包的
00-START-HERE（中文：下載位置、檔案→Sudowrite 位置、十分鐘測試、寫作設定、ElevenLabs、更新、常見問題）；草稿包
`delivery/holoen-2026-09-30-r01-draft` 已重建（18/24，Bae 收錄前不放她的表演表，START-HERE 會寫「這一版還沒收錄」）。
Bae 收錄後要刪掉 r01-draft 重建一次。span_check 改成只拿卡片有引用的影片來比對（`--write` 重產 span-candidates，40→31）。

狀態（2026-10-02 04:00 UTC）：**作者下令加入 Hakos Baelz、不做 Tsukumo Sana**（2026-10-02）。
- **Bae 已起草**：角色卡 `runs/20261002-0236-character-Hakos-Baelz/claude-draft.md`、世界觀卡
  `runs/20261002-0236-world-Hakos-Baelz-Pairs/claude-draft.md`、表演表 `export/elevenlabs/Hakos-Baelz.md`、
  音檔報告 `research/audio-check/bae.md`（2026 年 5 個窗口、兩模型核對；私事段落不用）。13 張成員卡＋Promise、Concerts、
  Cross-Branch Friends 已加 Bae 的關係（在 runs 的 final.md，**尚未收錄**）。工具：COHORTS（promise 加 Bae＋Pairs）、
  SHORT、REFERENCE_ONLY、CHADCast 單位；release 的張數改由 COHORTS 推導（V02 在 Bae 收錄前會 fail，正常）。
- **GPT 佇列第一個是 Bae 的一輪 xhigh 主張核對**（`runs/20261002-0236-character-Hakos-Baelz/to-gpt.free.md`；
  重建用 scratchpad `mk_bae_review.py`）。結果出來後：逐條併進兩張草稿 → 複製成兩個 run 的 final.md（Merge Record 記處置）→
  其他卡的 Bae 修改一起處理 → `qa_runs.py promote-changed --reason "Author decision (2026-10-02): Hakos Baelz added…"`、
  兩張新卡用 `lab.py promote <run> --force` → export → qa_packets → validate（V02 應轉 pass）→ commit/push。
- 之後佇列照舊：global → justice → myth1 → myth3 → myth4 → myth2 → promise（含 Bae）→ bridge events → ties-external。
- **span_check 強化**：會抓跨行引句與表演表範例區塊；`asr_spans.py` 重跑不再丟掉舊的部分一致列。
  無法機械判定的 40 句列在 `research/qa/span-candidates.md`，交給 09 聲音審計。嚴格的「兩模型全文比對」需要把第二模型
  全文存進 repo（待辦）。

狀態（2026-10-02 02:30 UTC，全卷審計進行中；GPT 額度 06:29 UTC 重置，send_later 06:31 自動開跑）：
- **完成**：Advent cohort 審計（`research/qa/audit-advent.md`）已全部合併、收錄、匯出、推送；ledger 有 ADVENT-* 處置。
  另做 CLAUDE-SCOPE-002：流程紀錄（Merge Record、音檔報告、NEXT/project、舊草稿與提示副本）不再寫出被排除的具體私事。
- **GPT 額度**：Global 審計跑到一半撞上限（約 20 萬 tokens、無產出）→ 重置 2026-10-02 06:29 UTC。改進：
  1. `lab.py` 的 GPT 在開跑當下工作目錄的副本裡跑（不含 runs/、git，看不到之後的修改），並記 `gpt-free.events.jsonl`（工具呼叫與 token）。
  2. 審計提示把 packet、project.md、shared-rules、ledger、registry 摘錄**內嵌**，並訂「約 12 次工具呼叫、最多 6 次搜尋」的預算。
  3. Global 的 incoming 去掉泛用別名（hololive、off-collab…），110k→51k 字；Myth1 拆成 myth1（Calli）、myth3（Kiara）、myth4（Ina）。
- **工具**：`tools/qa_runs.py make cohort|bridge <name>`（建立 QA run 並寫 qa.json）、`apply <audit.md> [--dry]`（照審計表的
  exact old text 改 runs 的 final.md＋Merge Record）、`promote-changed --reason`。有 qa.json 的 run，`lab.py gpt <run> free`
  開跑前會自動重建 packets、重寫內嵌提示，GPT 讀的是當下工作目錄的副本（不含 runs/、git），所以合併中途也不會錯位。
- **GPT 佇列**（`.gpt-quota.json`，依序）：global → justice → myth1 → myth3 → myth4 → myth2 → promise → bridge events →
  bridge ties-external。額度重置後直接 `setsid nohup python3 novel-lab/tools/lab.py gpt-resume --now &`。
- **ties 的調整**：成員之間的關係（ties-cast）與多人聲明（ties-groups）已在各 cohort 審計的 incoming／outgoing 兩邊都比對過，
  不再另跑；bridge ties 只跑外部人物（ties-external）。V11 改為需要 ties-external＋七份 cohort 審計（`tools/release.py`）。
  提示裡請 GPT 若不同意就在 Merge handoff 說明。
- **06 近期補完：Claude 已做完**（省一個 GPT 窗口）：`research/refresh/myth-kronii-20260930.md`。Myth 六週年 3D live
  "Seasons From Within"（2026-09-19 PDT）確認已舉行＋新曲 "THIS IS MYTH"（CONSULT-P2-001 結案）、Calli "UNCUT ROCK!!"、
  Kiara 生日 3D、Kronii "STORM" 等；5 個證據不足的候選暫不收。GPT 會在 Myth 各 cohort 審計裡複核。
- **引句**：`tools/span_check.py` 掃出 23 處超出兩模型共同片段的引句，已修（CLAUDE-QUOTE-001）；V13 之後會自動擋。
- **交付預覽**：`delivery/holoen-2026-09-30-r01-draft/`（草稿，審計完成後重建正式版）。
- **之後**：08 年表＋X → 09 聲音 → 10 `release.py build` → 11 驗收。
- **Mococo（CONSULT-P1-007）**：已查整個頻道存檔，沒有其他可歸屬的單人窗口；聲音指示維持暫定（報告與卡已寫明）。
- **待辦（Claude）**：表演表在聲音審計後 `stamp-sheets`。Hakos Baelz、Tsukumo Sana 等作者下令。

（以下為較早的狀態紀錄）

狀態（2026-10-01 21:05 UTC，GPT 專案諮詢完成，全卷審計進行中）：
- **諮詢**：第 1 輪 `runs/20261001-1557-check-Project-Consult/gpt-free.md`（交付形式、到 10/4 的流程、跨卡問題），第 2 輪
  `runs/20261001-2050-check-Project-Consult-R2/gpt-free.md`（同意＋審計 prompt＋驗證規格）。P0（試鏡經歷、私人旅行、
  母語、Ina 的起床／睡衣句、貼上單缺 Style 區塊）與大部分 P1 已修並收錄；處置一律記在 `research/qa/resolutions.md`。
- **工具**：`tools/qa_packets.py holoen`（registry.json、各組 packets、manifest.json）；`tools/release.py validate|stamp-sheets|build holoen`
  （V01–V25；需要審查的檢查在對應審計檔出現前一律 fail）；`framework/prompts/gpt-cohort-audit.md`、`gpt-bridge-audit.md`。
- **GPT 佇列（依序，不並行）**：六個 cohort 審計 `runs/20261001-2100-check-QA-cohort-{advent,global,justice,myth1,myth2,promise}`
  （scratchpad `queue.py` + `cohort_queue.txt`；額度用完時剩下的會自動加進 `.gpt-quota.json`）。之後：bridge events／ties
  （`mk_audit.py bridge events|ties`）→ 06 近期補完 → 08 年表＋X → 09 聲音 → 10 發佈候選 → 11 驗收。
- **合併規則**：每份審計輸出複製成 `research/qa/audit-<cohort>.md`（validator 以此認定已審），逐條寫進卡的 Merge Record 與
  ledger，收錄 `--force`，重建 packets。注意：Elizabeth、Raora 的 final.md 之後有直接修改，**不要再重跑** merge_erb.py／merge_rao.py。
- **待辦（Claude）**：Kronii 音檔報告改成明確共同片段（CONSULT-P1-006）；Myth 六週年 live 查證（P2-001）；Mococo 個人窗口（P1-007）；
  表演表在聲音審計後 `stamp-sheets`。Hakos Baelz、Tsukumo Sana 等作者下令。

（以下為較早的狀態紀錄）

狀態（2026-10-01 16:30 UTC，Justice 完成並收錄；下一階段：GPT 專案諮詢與重任務）：
- **Justice 完成**：四張角色卡（Elizabeth Rose Bloodflame、Gigi Murin、Cecilia Immergreen、Raora Panthera）、世界觀卡
  `hololive -Justice-`、`Justice Pairs`；GPT 三輪 xhigh 逐條核對審查（`runs/20261001-1032-character-Elizabeth-Rose-Bloodflame/gpt-free.md`
  ＝Liz＋Gigi，`…-Cecilia-Immergreen/gpt-free.md`＝Cecilia＋Raora，`…-world-hololive--Justice/gpt-free.md`＝世界觀卡＋其他卡的 Justice diff）
  已逐條併進各卡 Merge Record，作者裁決收錄（`--force`）。合併腳本在 scratchpad `fill/merge_{erb,gigi,cec,rao,wjus,wpairs}.py`、
  `fill/cast_jus2.py`、`cast_jus3.py`、`cross_bff.py`、`cross_lyra.py`（scratchpad 不進 git、容器回收就消失；以各 run 的 final.md 與 bible 為準）。
  - 主要更正：3D showcase 是 08-01/02/08/09 PDT（不是 08-09/10），08-16 PDT 團體 3D 聯動；Serendipity 官方 unit 名（Autofister、Bloodraven、
    B.F.F 等七組）與客串曲；LYRA 是五人 "III" remix 翻唱；Cecilia 出道的聊天室遊戲是 nullrefrepro 實作；Raora／Cecilia 出道美術分工
    有方向性；"Uncle Erb" 改成 Liz 自己標題的「Nephew」叔姪梗；Cecemoco＝Cecilia＋Mococo；只引用兩模型一致的片段（Gigi 的 but/and、
    Cecilia 的 sign-off、Raora 的 "Hear me out" 都切成共同片段）；Gigi／Cecilia／Raora 的預設語氣改得不單一（不是一直大叫／一直挖苦／一直笑）。
  - 連動修改並重新收錄 21 張既有卡（Calli 的 Relationships 壓到 349／350 字）。
  - 表演表：`export/elevenlabs/{Elizabeth-Rose-Bloodflame,Gigi-Murin,Cecilia-Immergreen,Raora-Panthera}.md` 已依合併後的卡更新。
  - 匯出：`export/characters.csv`（18 張）、`export/worldbuilding.csv`（24 張）。
- **作者新指示（2026-10-01 16:00）**：作者重置了 GPT 額度，另有一張重置券（10/4 到期），10/4 前盡量用滿但要合理有效率；讓 GPT 了解專案全貌、
  設計流程、和 Claude 討論怎麼交付給作者最好。做法寫在 project.md。
- **GPT 待跑**：`runs/20261001-1557-check-Project-Consult`（第 1 輪：A 交付形式、B 到 10/4 的流程、C 跨卡／結構問題、D 問題）。16:05 額度用完，
  重置 20:27 UTC；send_later `trig_01KjXFjeULyTFPxWgxZhmZSL`（20:29）回來跑 `lab.py gpt-resume`。
- **下一步**：讀 GPT 第 1 輪提案 → Claude 寫第 2 輪回覆（同一 run 的新 to-gpt.free.md 或新 run）→ GPT 定案 → 依序跑議定的重任務
  （全卷交叉一致性審計、舊卡近期補完、世界年表完整性）→ 合併、收錄、匯出、推送、中文回報。Hakos Baelz、Tsukumo Sana 等作者下令。
- 排程：Claude 自動續做 `trig_01V2bEJdsw5EnZpMBaPKL4tQ`（每小時 :20，提示已改成這一階段）。

（以下為較早的狀態紀錄）

狀態（2026-10-01 14:00 UTC，Justice：草稿完成，等 GPT 審查）：
- **作者新指示**：Advent 之後做 Justice；GPT 全部 xhigh；GPT 額度用完時 Claude 繼續做；雙方額度用完都排程回來；
  想辦法把 GPT 的長處用到最大（做法寫在 project.md）。
- 排程：Claude 自動續做 `trig_01V2bEJdsw5EnZpMBaPKL4tQ`（每小時 :20）；GPT 重跑 send_later `trig_015aKJi4ANzUxSwwRBKEtvUX`
  （15:01 UTC，跑 `lab.py gpt-resume`）。Justice 全部收錄、匯出、推送後刪除前者並用中文回報。
- **完成（Claude）**：四張角色卡草稿（runs `20261001-1032-character-{Elizabeth-Rose-Bloodflame,Gigi-Murin,
  Cecilia-Immergreen,Raora-Panthera}/claude-draft.md`，含聲音段落）；世界觀卡 `hololive -Justice-`、`Justice Pairs`
  （runs `20261001-1032-world-*`）；其他 14 人 Relationships 與 5 張世界觀卡已加 Justice（final.md，尚未重新收錄）；
  音檔報告 `research/audio-check/{elizabeth,gigi,cecilia,raora}.md`（兩模型核對）；X 發文 `research/x-posts.md`。
- **GPT 待跑（依序）**：三個 xhigh 逐條主張核對審查（`framework/prompts/gpt-claimcheck-review.md`），提示在
  `runs/20261001-1032-character-Elizabeth-Rose-Bloodflame/to-gpt.free.md`（Liz＋Gigi）、
  `runs/20261001-1032-character-Cecilia-Immergreen/to-gpt.free.md`（Cecilia＋Raora）、
  `runs/20261001-1032-world-hololive--Justice/to-gpt.free.md`（兩張世界觀卡＋其他卡的 Justice 修改 diff）。
  原本的研究任務（`20261001-1021-research-*`）因草稿已先完成而改由審查涵蓋（審查同時查證與補缺漏），不再跑。
  若 `novel-lab/.gpt-quota.json` 遺失：依序跑 `python3 novel-lab/tools/lab.py gpt <上面三個 run> free`。
- 隱私（不寫）：休息及其原因、健康、家人、性向、試鏡、旅行、母語／國籍說法（口音只當聲音特徵寫）。
- 下一步：GPT 審查 → 逐條併進 final.md（Merge Record）→ `promote --force` → `export holoen` → 四份 ElevenLabs
  表演表 → NEXT.md／project.md → 推送 → 刪除每小時排程 → 中文回報。

（以下為較早的狀態紀錄）
狀態（2026-10-01，Advent 完成）：
- **Advent 全員完成並收錄（作者 2026-10-01 下令）**：角色卡 Shiori Novella、Koseki Bijou、Fuwawa Abyssgard、
  Mococo Abyssgard（Nerissa 先前已完成）；新世界觀卡 `FUWAMOCO`（雙胞胎單位／共用頻道）、`Advent Pairs`
  （團內與跨分部關係網）；`hololive -Advent-` 卡改寫成整團。
  - GPT 一輪審查 `runs/20261001-0549-world-Advent-Pairs/gpt-free.md`（high），逐條併進各卡 Merge Record，
    作者裁決收錄（`--force`）。主要更正：Shiori–Kronii 是「一起主持 Rating Your Clocks」（不寫誰的時鐘）；
    "2 Creatures + 1 Reaper" 只有 Fuwawa；Pero 一律寫成虛構吉祥物；子集合作不算全團（R.E.P.O. 時 Nerissa
    只是 "in Bird Spirit"）；存檔次數不寫成關係排名；Mococo 的「比較聰明／黏人」刪除；"æ" 是粉絲拼法不是 IPA；
    混音錄音的音高數字不進 Audio Tags；3D 日期標 PDT；-All for One- 首日先全員 "All for One" 再 "Genesis"。
  - 新增事實（官方頁查證）：GreyScaleX "Purrfect Pair" 周邊（2026-09-05 開賣）、hololive night（Dodger
    Stadium，2025-07-05，Ina／IRyS／Bijou）、Kiara 陪 Bijou 練難編舞（Serendipity 訪談 04）、
    Advent 3D 聯動（2024-08-17 PDT）。
  - 隱私：健康、家人、住處、睡眠、宣布的休息等一律不寫。
  - 連動修改並重新收錄：Calli、Kiara、Kronii、Gura、Ina、Ame、IRyS、Fauna、Mumei、Nerissa 的 Relationships；
    VTuber Persona、hololive、History 2023-2026、Concerts、Cross-Branch 世界觀卡。
  - 音檔報告：`research/audio-check/shiori.md`、`bijou.md`、`fuwamoco.md`（兩模型核對；只引用兩模型一致的片段）。
  - 表演表：`export/elevenlabs/Shiori-Novella.md`、`Koseki-Bijou.md`、`Fuwawa-Abyssgard.md`、`Mococo-Abyssgard.md`。
  - 匯出：`export/characters.csv`（14 張）、`export/worldbuilding.csv`（22 張）。
- **已完成成員**：Myth 五人、Kronii、IRyS、Fauna、Mumei、Advent 五人（含 Nerissa）。其餘成員（Justice 等）等作者下令。
- **下一步候選**（作者下令前不做新成員）：Mococo 缺乾淨的個人說話樣本（只有薄的 2025 個人台和雙人台）；
  Shiori 可補一段純雜談窗口；Bijou 可補一段雜談窗口。

（以下為較早的狀態紀錄）
狀態（2026-10-01 06:40 UTC）：
- **Ceres Fauna、Nanashi Mumei 完成並收錄（作者 2026-10-01 下令）**：角色卡＋`Fauna and Mumei Pairs` 世界觀卡。
  GPT 一輪審查 `runs/20261001-0454-world-Fauna-and-Mumei-Pairs/gpt-free.md`（high）已逐條併進 Merge Record，
  作者裁決收錄（`--force`）。音檔報告 `research/audio-check/fauna.md`、`mumei.md`（兩模型核對；
  Fauna 一段會員限定音檔誤抓後未使用）；表演表 `export/elevenlabs/Ceres-Fauna.md`、`Nanashi-Mumei.md`。
  - 連動修改並重新收錄：8 張既有角色卡的 Relationships、Promise／hololive／Cross-Branch／兩張 History／
    Concerts／VTuber Persona 世界觀卡。GPT 指出並已更正：Mumei「最後一場個人遊戲台」說法錯誤
    （04-22 與 IRyS 的 Overwatch 之後還有 04-24 Promise R.E.P.O.）、"Bae's most frequent partner" 改為
    recurring、Lui 的 "bird sisters" 是標題不是台詞、Cecilia／Gigi 分開、"sultry" 從所有演出指示移除。
  - 新增事實（官方頁查證）：Fauna＆Mumei 原創合唱 "It's Not a Phase"（-Breaking Dimensions- 2024-08-24 首演，
    2024-12-22 發售）；Breaking Dimensions 的 Kiara–Mumei–Nerissa、Fauna–Shiori–Nerissa 三人曲；
    Mumei 與 Korone 合唱翻唱（2025-04-23）、"Outside the Box" 的 JP 來賓（Okayu、Korone、Nene、Koyori）。
  - 未採納（理由寫在 Merge Record）："I'm always on time" 保留（第二模型全文有）；IPA 保留並標 provisional
    （與其他八張卡一致，作者要求教發音）。
  - 匯出：`export/characters.csv`（10 張）、`export/worldbuilding.csv`（20 張）。
- **已完成成員**：Myth 五人、Kronii、IRyS、Nerissa、Fauna、Mumei。其餘成員等作者下令。

（以下為較早的狀態紀錄）
狀態（2026-10-01 04:20 UTC）：
- **完成並收錄（作者裁決，GPT 只審一輪）**：19 張世界觀卡＋8 個角色（Myth 五人、Kronii、IRyS、Nerissa）。
  GPT 審查 `runs/20260930-2309-world-hololive/gpt-free.md`（high）；意見已逐卡併進 final.md 的 Merge Record。
  已匯出：`export/characters.csv`（8 張，含 Audio Tags 欄）、`export/worldbuilding.csv`（19 張）、
  `export/sudowrite-paste.md`、`export/cards/`；`export/elevenlabs/` 八人表演表＋`sudowrite-style.md`（Style 規則）。
- 審查後新增的官方來源：Serendipity 訪談（IRyS–Bae、Nerissa–Elizabeth）、World Tour '24 官方報告、
  DANGERyS（2026-07-12 發售）、In My Feelings（2024-08-08）、Moona "100%"（2025-02-16）、ASOBI★MAWARI-TAI!。
- **作者裁決（2026-10-01）**：宣布的休息一律不寫，也不寫成休息中。
- **下一步候選**（作者下令前不做新成員）：繼續擴充世界觀（更多跨分部關係、X 發文、各成員演唱會細節）；
  用音檔補強既有角色（Kiara–Nerissa 的 KiaRissa 台詞、各人的笑聲）。

- **作者新指示（2026-10-01，已寫進 project.md）**：
  1. 世界觀要大量補：人際關係（含 JP／ID／GAMERS 等其他分部）、新成員加入、團體／個人演唱會、
     3D、Expo／fes 等活動都是共同記憶；X 公開發文是關鍵來源。GPT 額度 0 時 Claude 自己盡量完善。
  2. 目標是 EN 全員，但**名單外的成員等作者下令**（目前已下令：IRyS、Nerissa）。
  3. **Sudowrite 會自己加 ElevenLabs 標籤**：要把每個角色影響「聲音」的一切（說話方式、性格、口癖、
     口音、語速、音域、笑聲、招牌聲音、情境轉換、發音）完整教給 Sudowrite。
     計畫：角色卡加一個 [SW] 欄位「Audio Tags」（情境→標籤、招牌聲音、發音、不要做的），
     故事層 Style 加標籤格式規則；export 也輸出。內容來源＝`export/elevenlabs/<名字>.md`。
- 新世界觀卡（2026-10-01）：`hololive -Advent-`、`IRyS and Nerissa Pairs`（runs `20261001-0001-world-*`）；
  `hololive -Promise-` 改成涵蓋 IRyS。Kiara／Calli／Kronii／Ina 的 Relationships 已加 IRyS／Nerissa（final.md）。
- IRyS：草稿完成（runs `20260930-2334-character-IRyS`），音檔報告 `research/audio-check/irys.md`，
  表演表 `export/elevenlabs/IRyS.md`。`lab.py export` 現在會保留 `export/elevenlabs/`。

- **作者定案（新）**：以真實性為主，卡片優先用**真實台詞**（含粗口、挑逗）；音檔由 Claude 自己核對。
- **音檔核對已完成**（六人）：報告在 `research/audio-check/<名字>.md`，工具在 `novel-lab/tools/audiocheck/`。
  - 方法：ragtag 直播存檔 → whisper small.en 轉寫 + Praat 量音高 → **上卡片的句子再用 medium.en 第二模型核對**。
  - 檔案一律標 [ASR]，並寫「machine-transcribed … without independent listening verification」。不是人耳聽寫。
  - 第二模型推翻的句子已從卡片移除（Kronii 一處 hellos、Calli "Fucking adorable."、Kiara 整串 "so cute"、
    "Damn it"、Gura "god damn"/"Damn."、Ame "Bitch."）。
- **gen-1 Myth ＋ Kronii、Calli 六人全部收錄（2026-09-30 22:53 UTC）**，已匯出：
  `export/characters.csv`（6 張）、`export/sudowrite-paste.md`、`export/cards/*.csv`。
  - Kiara：GPT APPROVE 收錄。
  - Kronii、Calli、Ina、Ame：作者裁決 (b) 收錄（`--force`，記在各 run 的 `author-decision.md`，不算 GPT 核准）。
  - Gura：Claude 比照作者對上述四人的裁決收錄（第 2 輪上限、意見已照改），作者可推翻。
- **世界觀（2026-09-30 作者指示）**：13 張世界觀卡草稿完成（runs `20260930-2309-world-*`，各有 claude-draft.md）：
  hololive、VTuber Persona and Lore（最重要：她們知道自己是有人設的實況主）、Streaming Life、hololive -Myth-、
  hololive -Promise-、TakaMori、TakoTori、AmeSame、Bone Bros、Time and Death、Time Duo、Octo'Clock、Myth Pairs。
  六張角色卡已改成人設框架（"a VTuber whose lore… makes her…"、"her avatar…"）並更新 Relationships；
  Kronii 聲音描述更正（K8 其實有寫深嗓音／音域廣）。這些改動在 runs 的 final.md，**還沒重新收錄**。
  - 作者指示：GPT 只審一輪。`runs/20260930-2309-world-hololive/to-gpt.free.md` 已備好（13 張卡＋角色卡改動）。
  - **Codex 額度 02:22 UTC 重置**；send_later `trig_012rQiQwJKBepLjf73cYGMgw` 在 02:27 UTC 叫醒這個 session。
  - 審完：意見併進各 world run 的 final.md（claude-draft.md → final.md，加 Merge Record），六張角色卡也一起，
    然後 `promote --force --reason "作者指示 GPT 只審一輪"`，`export holoen`。
- **IRyS、Nerissa Ravencroft**（作者：世界觀做完後接著做）：runs `20260930-2334-character-IRyS`、
  `20260930-2334-character-Nerissa-Ravencroft` 已建立；音檔 jobsG 轉寫中；Claude 研究與初稿進行中。
- **ElevenLabs v4 交接（作者 2026-09-30 問）**：指南 `novel-lab/docs/elevenlabs-v4.md`；六人表演表
  `export/elevenlabs/<名字>.md`（原創聲音描述、起始設定、腳本習慣、情境標籤、招牌聲音、IPA、不要做的事、示範）。
  **不複製成員本人聲音**（ElevenLabs Use Policy §5、COVER 規範）。IRyS／Nerissa 的表演表等她們的聲音段落完成後補。
- **近期權重**（作者定案，已寫進 project.md）：描述現在的預設說話方式時，近期直播權重較高；
  早期梗保留為共同記憶。六人都已照此檢查（Ame 換上 2024 台詞、Calli 招呼語順序、Gura 以 2024 為預設）。
- 下一步（額度允許時）：Council/Promise 其他成員，或繼續用音檔補強既有六人（例如 Kronii 的 GWAK、
  Calli 的笑聲，這些 whisper 寫不出來，需要別的方法）。
- **框架**：GPT 已 APPROVE（`docs/reviews/gpt-framework-review-20260930-1621.md`）。
- 作者定案：初稿 xhigh，審稿／驗收 high（lab.py 預設已是如此）。

合併與修改的規則：
- wiki 一律寫「X2 §Section」段落標記；wiki 原文可重抓：
  `https://virtualyoutuber.fandom.com/api.php?action=parse&page=<Page>&prop=wikitext&format=json`
- 檔案開頭有「Audio status」；clip 標題只證明「上傳者這樣描述」；頻率是估計（字幕／轉寫計數除外）。
- **只有兩個模型都同意的 [ASR] 句子可以上卡片**；第一模型的次數統計只是參考（small.en 遇日語會憑空寫英文）。
- 卡片去重：精確台詞只放 Catchphrases；Personality 寫行為；Dialogue Style 寫句法（可附 "Lines of hers:"）；
  Voice & Delivery 寫聲音，不放台詞。
- 不把玩笑寫成永久規則；引述要有確切來源段落，否則 [Unverified] 並移出卡片。
- 粗口與挑逗台詞照原樣保留（作者定案），wiki 打碼的字寫出來並標「censored in source / inferred」。
- 不寫真人資訊（寵物原型、家人、健康、國籍、畢業原因）。

```bash
L="python3 novel-lab/tools/lab.py"; R=novel-lab/projects/holoen/runs
K=$R/20260930-0704-character-Ouro-Kronii; C=$R/20260930-0704-character-Mori-Calliope
KI=$R/20260930-1113-character-Takanashi-Kiara; IN=$R/20260930-1113-character-Ninomae-Inanis
GU=$R/20260930-1113-character-Gawr-Gura; AM=$R/20260930-1113-character-Watson-Amelia

$L doctor                                   # 必須顯示「會透過 Codex CLI 呼叫 GPT」
$L gpt $KI $IN $GU $AM verify               # 四人第 1 輪（若 CHANGES：修正後第 2 輪）
$L gpt $K $C verify                         # Kronii/Calli 額外一輪
$L promote <run>   # 每個 APPROVE 的
$L export holoen
```

音檔核對重跑（scratchpad 內，需要 `pip install faster-whisper praat-parselmouth numpy imageio-ffmpeg`）：
見 `novel-lab/tools/audiocheck/README.md`。YouTube 本身仍擋這個容器；不要繞過它的防機器人機制。

回報給使用者時用中文摘要。之後的成員名單見 project.md。

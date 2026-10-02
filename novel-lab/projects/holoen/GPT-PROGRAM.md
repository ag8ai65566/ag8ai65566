# GPT 工作計畫（作者命令 2026-10-02 17:00 UTC）

作者命令：規劃 GPT 之後所有審查、找新資料、規劃並統整 Sudowrite＋ElevenLabs 工作流；先全部交給 GPT 做，不必顧慮
GPT 額度。Claude 的週額度快到上限，所以 Claude 只負責排程，**結果出來後先不合併，等作者下令再動工**。

## 怎麼跑
- 佇列在 `novel-lab/.gpt-quota.json`（不進 git）；`tools/gpt_autorun.py` 在背景一個接一個跑（不並行），額度用完就睡到
  重置時間再繼續，每跑完一個就把 run 目錄提交並推送（commit 標題「GPT output … (unattended queue, merge pending
  author order)」）。log：Claude scratchpad 的 `gpt_autorun.log`。
- 每個任務的提示在各 run 目錄的 `to-gpt.free.md`，GPT 的回覆是同目錄的 `gpt-free.md`。
- 重建提示：`tools/mk_b2_review.py`（E、F）、`tools/mk_voice_audit.py v1 v2 v3`、`tools/mk_gpt_program.py`
  （P1、W1、R1–R7）；QA 審計在開跑前自動用 bible 重建。

## 佇列（依序）
| # | run | 內容 | 產出用在哪 |
|---|---|---|---|
| 1 | 20261002-0615-character-Laplus-Darknesss（E） | La+、Lui、Koyori 一輪 claim check | 合併後收錄 holoX 三人 |
| 2 | 20261002-0615-character-Sakamata-Chloe（F） | Chloe、Iroha、holoX 世界卡、其他卡上的 holoX 句 | 合併後收錄 holoX |
| 3 | 20261002-1715-check-GPT-plan（P1） | 審這份計畫，設計合併後的驗收輪次、發佈條件（V01–V25 對應） | 之後的審查排程 |
| 4 | 20261002-1715-research-workflow-SW-EL（W1） | 即時查證 Sudowrite 與 ElevenLabs 現況；端到端工作流、腳本格式、轉換工具程式碼、發佈包缺口、作者用快速上手 | docs/、export/、START-HERE、新工具 |
| 5–7 | 20261002-0755-check-QA-voice-v1、v2；20261002-1657-check-QA-voice-v3 | 09 聲音審計：Myth＋Promise、Advent＋Justice、JP 九人 | voice-delivery.md、表演表 stamp |
| 8–13 | 20261002-1715-research-new-R1…R6 | 找新資料（各團）：更正、2025–2026 近況與說話方式、里程碑、跨團互動、引句候選（給 Claude 做音檔核對） | 卡片增補 |
| 14 | 20261002-1715-research-new-R7-Ties | 全卡司關係網：單向關係與空白配對的有據互動 | Relationships 與 dossier |
| 15–25 | QA 審計：global、justice、myth1、myth3、myth4、myth2、promise、bridge-events、ties-external、jp、jp2 | 既有內容的正確性與一致性 | resolutions.md |

暫不排（要先合併 E、F）：holoX 的 QA cohort 審計（`20261002-0751-check-QA-cohort-holox`）、聲音審計 v4（holoX 五人，
`mk_voice_audit.py v4`）。P1 的建議會一起列出其他缺口。

## 合併（作者下令後才做）
E、F：照 NEXT.md 的方法（final.md＋Merge Record → promote → export → packets → validate）。聲音審計：逐條處置寫進
research/qa/voice-delivery.md，卡片欄位走 run 的 final.md，表演表直接改，OK 的表 stamp。新資料：P1 優先、FIX 必看，
引句候選先做兩模型音檔核對；關係句注意 350 字上限。W1：工作流文件、轉換工具、發佈包修正分開提交。QA 審計：
`qa_runs.py apply`（先 --dry）＋ resolutions.md。

---
name: novel-lab
description: 小說設定工作台。使用者要調查／設計角色、世界觀、故事點子、現實考據，或要檢查設定一致性，並把結果放進 Sudowrite 時使用。每次都和 GPT（GPT-6 Astra/Sol，推理 high 以上）協作：盲寫初稿 → 互審 → Claude 合併 → GPT 驗收 → 匯出 Sudowrite 貼上單。
---

# novel-lab 協作流程

工具：`python3 novel-lab/tools/lab.py`（在 repo 根目錄執行）。框架說明在 `novel-lab/README.md`，
Sudowrite 欄位與上限在 `novel-lab/framework/sudowrite-fields.json`，Sudowrite 調查在
`novel-lab/docs/sudowrite-2026-09.md`。

## 大前提（不可違反）

- **每一次任務都要和 GPT 協作。** GPT 只能是 GPT-6 家族的 Astra 或 Sol，推理強度 high 以上；
  `lab.py` 會硬性檢查。GPT 呼叫失敗時不可以改用其他模型，也不可以跳過 GPT 自己做完——
  改走人工轉貼（見下）或停下來告訴使用者。
- **不寫露骨的成人內容。** 那部分由 Sudowrite 處理；我們只做非露骨的角色化定位，
  並標記 `【Sudowrite 處理】`。規則全文在 `novel-lab/framework/prompts/shared-rules.md`。

## 步驟

0. **接收需求。** 使用者一句話就夠（例：「角色：一個在殯儀館打工的大學生，外冷內熱」）。
   判斷 kind（character / world / idea / research / check）與專案。只有一個專案就直接用；
   沒有專案就先 `lab.py new-project <slug>`，並請使用者之後補 project.md（不要因此卡住）。
   然後 `lab.py brief <slug> <kind> "<原文>" [--name 名稱]`，印出的路徑就是這次的 run 目錄。

1. **盲寫初稿（平行）。** 先用背景指令跑 `lab.py gpt <run> draft`，同時我照
   `novel-lab/framework/templates/dossier-<kind>.md` 寫 `<run>/claude-draft.md`。
   **寫完自己的稿子之前不可以讀 gpt-draft.md**——兩份稿子要真的獨立，合併才有意義。
   先讀 `novel-lab/framework/prompts/shared-rules.md` 與專案的 project.md、bible。
   research 類要用 WebSearch 查證並附來源（GPT 那邊會自動開啟即時網路搜尋）。

2. **互審（平行）。** 背景跑 `lab.py gpt <run> review`（GPT 審我的稿），
   同時我照 `novel-lab/framework/prompts/rubric.md` 審 GPT 的稿，寫進 `<run>/claude-review.md`。
   要誠實列出「GPT 比我好的地方」。

3. **合併。** 以兩份審稿意見為依據寫 `<run>/final.md`：同一份 schema，
   front matter 保留 kind / name / sw_section，`## [SW]` 卡片必須在字數上限內。
   文末加「## 合併紀錄」：各段採用了誰的版本、分歧怎麼決定、哪些分歧留給作者決定。

4. **GPT 驗收。** `lab.py gpt <run> verify`。第一行是 `CHANGES` 就修 final.md 再驗收；
   最多來回 2 次，還不同意就把雙方立場並列給使用者決定。

5. **收錄與匯出。** `APPROVE` 後 `lab.py promote <run>`，再 `lab.py export <slug>`
   （⛔ 超過 Sudowrite 官方上限會 exit 2，要回頭縮短；⚠ 超過建議長度只是提醒）。
   產出：`export/characters.csv`、`export/worldbuilding.csv`（Sudowrite 官方 CSV 格式）、
   `export/cards/*.csv`（單張）、`export/sudowrite-paste.md`（Story 欄位與逐欄內容）。

6. **回報。** 用使用者的語言，簡短給：這次產出的重點（3–5 行）、雙方主要分歧與怎麼決定、
   「待確認」問題、要匯入或貼上的檔案與 Sudowrite 裡的位置（新卡片用 CSV 匯入；
   更新既有卡片請逐欄貼上，因為重複匯入可能產生重複卡片）。然後 commit 並 push 到目前的開發分支。

## 改框架本身

框架（模板、規則、流程）的修改也要和 GPT 商擬：改完跑 `lab.py framework-review`，
依 GPT 的回覆（第一行 AGREE / AGREE-WITH-CHANGES / DISAGREE）調整，再回報使用者。
`novel-lab/docs/reviews/` 裡若只有 `*.to-gpt.md` 而沒有對應的回覆，代表上一次審查還沒完成，
GPT 可以連線時先補跑。

## GPT 連不上時（exit 3）

`lab.py gpt` 找不到 Codex 登入或 `OPENAI_API_KEY` 時，會把完整提示寫成 `*.to-gpt.md` 並以
exit 3 結束。**使用者不採用人工轉貼（2026-09-30 表明）**：這時先把 Claude 這邊能做的做完
（初稿、審稿），commit 並 push，然後停下來請使用者在雲端環境設定 `OPENAI_API_KEY` 後開新 session
接續。不要把 `*.to-gpt.md` 丟給使用者，也不要因為 GPT 連不上就自己把 GPT 的部分寫掉。
多個角色同一階段請用批次：`lab.py gpt <run1> <run2> … <stage>`。

## check（一致性檢查）

不產生卡片。兩邊各自列出矛盾清單（位置、衝突內容、建議改法），合併成 final.md，
GPT 驗收後直接回報，不用 promote。

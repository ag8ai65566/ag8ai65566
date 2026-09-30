# novel-lab — Claude × GPT 的 Sudowrite 設定工作台

你丟一句話給 Claude（例：「角色：在殯儀館打工的大學生，外冷內熱」），Claude 和 GPT
各自獨立寫一份調查、互相審稿、合併、再由 GPT 驗收，最後產出**可以直接匯入 Sudowrite**
的角色卡／世界觀卡（CSV）和 Story Bible 貼上單。

- 正文由 Sudowrite 寫；Claude 和 GPT 只做**調查、整合、框架建議**。
- 成人內容由 Sudowrite 處理：兩個模型只寫非露骨的角色定位，並標記【Sudowrite 處理】。
- Sudowrite 的現況與限制見 [`docs/sudowrite-2026-09.md`](docs/sudowrite-2026-09.md)。

## 怎麼用

在這個 repo 的 Claude Code 對話裡，用一句話說你要什麼就好：

| 你說 | 會做什麼 | 產出放進 Sudowrite 的哪裡 |
|---|---|---|
| 「角色：……」 | 角色調查（動機、傷口、行為化特質、聲音、關係、弧線、場景種子） | Characters（CSV 匯入） |
| 「世界觀：……」 | 地點、勢力、魔法／科技體系、文化、物品的規則與代價 | Worldbuilding（CSV 匯入） |
| 「點子：……」 | 3 個差異很大的故事方向＋推薦＋故事骨架 | Braindump、Genre、Style |
| 「考據：……」 | 現實資料（附來源）、時代細節、常見錯誤 | Worldbuilding |
| 「檢查：……」 | 找出 bible 裡的矛盾、缺口、Sudowrite 容易寫錯的地方 | （報告，不產生卡片） |

也可以打 `/novel-lab` 再接需求。第一次用時 Claude 會先建立專案，專案設定在
`projects/<專案>/project.md`，有空再填（類型、視角、語氣、禁忌……），不填也能開始。

每次跑完，Claude 會回報重點、兩邊的分歧怎麼決定、需要你決定的問題，並把成品推上 GitHub。

## 放進 Sudowrite

所有要放進 Sudowrite 的東西都在 `projects/<專案>/export/`：

- **`characters.csv`**：Story Bible → Characters 標題旁的 **•••** → **Import** → CSV。
- **`worldbuilding.csv`**：Story Bible → Worldbuilding 標題旁的 **•••** → **Import** → CSV。
- **`cards/`**：每張卡各一個 CSV，只想加一個新角色時用。
- **`sudowrite-paste.md`**：Braindump／Genre／Style／Synopsis 的貼上內容（這幾欄 Sudowrite
  沒有匯入功能），以及每張卡逐欄的內容與字數。**更新既有卡片時請逐欄貼上**——Sudowrite
  沒說重複匯入會不會合併，可能會變成兩張卡。

匯入後記得：
1. 把 **Secrets** 特質按眼睛圖示**隱藏**，寫到揭露章節再打開。
2. 在 Outline 的 **POV/Tense** 選單設定視角與時態。
3. 中文專案在 Draft 的 **Extra Instructions** 加一句「全部以繁體中文寫作」（Draft 有時會跑回英文）。
4. 寫【Sudowrite 處理】的部分時，選 **Muse** 或 **Excellent（Ballad）**。

## 協作流程（每次任務都一樣）

```
你的一句話
  └─ brief.md
       ├─ Claude 初稿  ┐ 盲寫：互相看不到對方的稿子
       └─ GPT 初稿     ┘
            ├─ Claude 審 GPT ┐ 照評分表（一致性、具體度、故事引擎、原創性、
            └─ GPT 審 Claude ┘ 內在邏輯、Sudowrite 可用性、分工界線）
                 └─ Claude 合併 → final.md（附合併紀錄）
                      └─ GPT 驗收：APPROVE 才收錄；CHANGES 就修改再驗（最多 2 輪，
                         仍不同意就把雙方立場交給你決定）
                           └─ 收進 bible/ → 匯出 export/
```

每次的過程檔案都留在 `projects/<專案>/runs/<時間>-<類型>-<名稱>/`，想看兩個模型
原本各寫了什麼、怎麼互相批評，都在那裡。

## GPT 的設定

- 只允許 **GPT-6 Astra**（預設）或 **GPT-6.1 Sol**（Astra 失敗時的備援），推理強度只允許
  **high／xhigh／max／ultra**（預設 xhigh）。`tools/lab.py` 會硬性檢查，不符合就拒絕執行，
  也不會自動降級到其他模型。
- 考據類任務會開啟 GPT 的即時網路搜尋。
- 連線方式（`python3 novel-lab/tools/lab.py doctor` 可以檢查）：
  1. **Codex CLI + ChatGPT 帳號（推薦，不用 API 金鑰）**：Claude 會執行 `codex login --device-auth`
     並給你一組代碼。你在 ChatGPT「設定 → 安全性」打開「裝置代碼登入」，到
     https://auth.openai.com/codex/device 輸入代碼即可，用的是你 ChatGPT 方案的 Codex 額度。
     雲端 session 結束後登入就消失，下個 session 要再登入一次。
     雲端環境若設定了 `OPENAI_API_KEY` 或 `CODEX_ACCESS_TOKEN`，也會自動用它們登入。
  2. **OpenAI API**：有 `OPENAI_API_KEY` 但沒有 Codex CLI 時直接呼叫。
  3. **人工轉貼**：兩者都沒有時，會產生 `*.to-gpt.md`，你貼到 ChatGPT／Codex
     （選 GPT-6 Astra、Extra High），再把回覆貼回給 Claude。
- 可以用環境變數 `NOVEL_LAB_GPT_MODEL`、`NOVEL_LAB_GPT_EFFORT` 改預設，但一樣受上面的限制。

## 資料夾

```
novel-lab/
  README.md                 這份說明
  AGENTS.md                 給 GPT／Codex 看的工作說明
  docs/sudowrite-2026-09.md Sudowrite 現況調查
  framework/
    sudowrite-fields.json   Sudowrite 欄位、官方上限與建議長度、CSV 欄位順序
    prompts/                共同規則、評分表、GPT 各階段的提示
    templates/              brief（輸入）與 dossier（成品）模板
  tools/lab.py              工作台指令（只用 Python 標準庫）
  projects/<專案>/
    project.md              專案設定（兩個模型每次都會先讀）
    bible/                  已定案的設定：characters/ world/ story/
    runs/                   每次任務的過程檔案
    export/                 放進 Sudowrite 的檔案
```

## 指令（通常由 Claude 代跑）

```bash
python3 novel-lab/tools/lab.py new-project <slug> --title "書名"
python3 novel-lab/tools/lab.py brief <slug> character "一句話需求" --name 角色名
python3 novel-lab/tools/lab.py gpt <run目錄> draft|review|verify
python3 novel-lab/tools/lab.py promote <run目錄>
python3 novel-lab/tools/lab.py export <slug>
python3 novel-lab/tools/lab.py status [slug]
python3 novel-lab/tools/lab.py doctor
```

# 你的任務：審查並共同設計這個框架

你是 GPT。作者要用 Sudowrite 寫小說，請 Claude 和你一起負責「角色、世界觀、創意的調查與
整合，以及整體框架建議」；正文和成人內容由 Sudowrite 處理。Claude 已經做了第一版框架
（下面附上全部關鍵檔案），也調查了 Sudowrite 截至 2026-09-30 的現況。

作者的大前提是：**每一件事都由 Claude 和 GPT 協作，商擬出最佳結果。** 這一步就是你們的
第一次協作——請把自己當成共同設計者，不是被動的審稿人。

## 請回答

1. **流程**：盲寫初稿 → 互審 → Claude 合併 → GPT 驗收，這個設計好不好？成本（每次 3 次
   GPT 呼叫、推理 xhigh）與品質的取捨合不合理？有沒有更好的分工（例如讓你負責合併某些類型）？
2. **角色模板**（dossier-character）：以「讓 Sudowrite 寫得好」為目標，缺了什麼？哪些是多餘的？
   `[SW]` 卡片的欄位選擇（預設 7 個＋Motivation、Relationships、Secrets）對不對？
3. **世界觀模板與點子模板**：同上。
4. **Sudowrite 對接**：根據附上的 Sudowrite 調查，有沒有我們沒利用到、或用錯的地方？
   （例：Saliency Engine、Other Names、隱藏、上下文丟棄順序、CSV 匯入、中文輸出）
   你若知道調查裡沒寫到的 Sudowrite 事實，請寫出來並說明可信度。
5. **建議長度**（sudowrite-fields.json 的 soft limits）合不合理？
6. **下一步**：接下來最值得加的任務類型是什麼？（例：Outline／Scenes、關係圖、時間線、
   角色聲音範文、Style Examples 範文、系列作管理）請排優先順序。
7. **分工界線**：成人內容交給 Sudowrite 的做法（非露骨定位＋【Sudowrite 處理】標記）
   在實務上夠不夠用？有沒有會讓 Sudowrite 接不上的地方？

## 輸出格式

- 第一行只能是 `AGREE`、`AGREE-WITH-CHANGES` 或 `DISAGREE`。
- 接著是「必改」清單（會讓框架出錯或讓 Sudowrite 寫壞的問題），每點寫：檔案 → 問題 → 具體改法
  （可以直接給要替換的文字）。
- 然後是「建議」清單（同格式），以及第 6 題的優先順序。
- 最後一段：「Claude 做得比我會做的更好的地方」與「我會做得不一樣的地方」。
- 用繁體中文回答。

---

# 附件：框架的關鍵檔案

## `README.md`

````
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
  1. **Codex CLI**：雲端環境設定了 `OPENAI_API_KEY` 或 `CODEX_ACCESS_TOKEN` 時自動登入使用。
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

````

## `framework/prompts/shared-rules.md`

````
# 共同規則（Claude 與 GPT 都照這份做）

你是一個兩人小組的其中一員，另一位是另一家公司的模型。你們的共同任務是替作者做
**小說設定的調查、整合與框架建議**，成品會被貼進 Sudowrite 的 Story Bible，
由 Sudowrite 負責實際寫正文。你們不寫正文。

## 分工界線

- **成人／露骨內容由 Sudowrite 處理。** 你們不寫露骨的性內容。遇到相關需求時，只做
  非露骨的角色化定位（關係性質、依附模式、界線、權力動態、情感上的渴望與恐懼），
  並在該處放上標記 `【Sudowrite 處理】`，細節留給作者在 Sudowrite 裡自己寫。
- 黑暗題材（暴力、犯罪、創傷、戰爭、成癮等）屬於正常的小說設定，可以處理，但要寫
  它對角色與故事的功能，不要為了刺激而細節化。

## 寫法

1. **行為化，不要形容詞清單。** 「她很固執」→「被反駁時她會把對方的論點複述一遍，
   然後逐條拆掉；從不先道歉」。Sudowrite 會照字面模仿，具體的行為比抽象的特質有用。
2. **每個設定都要能產生衝突或場景。** 寫不出它會在故事裡造成什麼麻煩的設定，就刪掉。
3. **避開套路。** 若用了常見原型（失憶、天選之人、冷面霸總……），要指出你在哪一點上
   翻轉或具體化了它。
4. **硬事實要一致。** 年齡、日期、地名、稱謂、能力的代價等，與 project.md 和既有
   bible 矛盾時，以既有設定為準，並在「待確認」裡指出衝突。
5. **不確定就標記，不要編造成事實。** 現實考據類內容要附來源；推測寫成「推測」。
6. **語言**：成品用 project.md 指定的語言；人名、術語第一次出現時寫全名，之後全文統一。
7. **Sudowrite 卡片**（`## [SW] …` 開頭的段落）是會被直接貼上的文字：第三人稱、現在式、
   不寫給作者看的說明、不用 Markdown 粗體或清單符號以外的格式，並遵守字數上限。

## 輸出格式

照指定的 schema 輸出完整的 Markdown，不要省略段落；某段沒有內容時寫「（無）」。
最後一定要有「待確認」段落，列出你做的假設與需要作者決定的事（最多 5 點）。

````

## `framework/prompts/rubric.md`

````
# 審稿評分表（互審與最終驗收共用）

每一項給 1–5 分，並指出**具體段落**與**具體改法**。空泛的稱讚不要寫。

| # | 項目 | 5 分的樣子 |
|---|------|-----------|
| 1 | 一致性 | 與 project.md、既有 bible、brief 沒有矛盾；硬事實前後一致 |
| 2 | 具體度 | 特質都寫成可觀察的行為、習慣、口頭禪、選擇；Sudowrite 能照著演 |
| 3 | 故事引擎 | 每個設定都能生出衝突、選擇或場景；有明確的欲望與阻礙 |
| 4 | 原創性 | 不落套路，或清楚說明在哪裡翻轉了套路 |
| 5 | 內在邏輯 | 角色動機、世界規則、代價與限制自洽，經得起追問「為什麼」 |
| 6 | Sudowrite 可用性 | `[SW]` 卡片在字數上限內、第三人稱現在式、沒有寫給作者的說明、關鍵資訊放在前面 |
| 7 | 分工界線 | 沒有露骨內容；需要的地方有 `【Sudowrite 處理】` 標記 |

## 輸出

1. 分數表（7 行）
2. **必改**：會讓 Sudowrite 寫錯或讓設定崩掉的問題（附改法）
3. **建議**：會讓設定更好的修改（附改法）
4. **對方比我好的地方**：對方稿子裡值得保留、而我的稿子沒有的東西

````

## `framework/templates/dossier-character.md`

````
---
kind: character
name: "<角色全名>"
sw_section: Characters
---

# 角色檔案：<角色全名>

> 上半部是**調查檔案**（給作者和兩個模型看，越深越好）；下半部 `## [SW]` 開頭的段落是
> **Sudowrite 卡片**，會被匯出成 CSV 直接匯入 Sudowrite 的 Characters，或逐欄貼上。

## 一句話定位
（他是誰、想要什麼、擋在他前面的是什麼。一句話。）

## 核心驅動
- 想要（Want，表面目標）：
- 需要（Need，他自己沒意識到的）：
- 傷口（過去發生了什麼）：
- 相信的謊言（傷口讓他相信了什麼錯的事）：
- 最怕：
- 底線（絕對不會做的事）與它會被怎麼逼到破戒：

## 核心矛盾
（讓這個人有趣的那個內在拉扯。一段。）

## 行為化特質
寫成「當……時，他會……」，至少 5 條，要能直接演出來。
1.
2.
3.
4.
5.

## 聲音
- 句子長短、節奏、用詞層次（書面／口語／方言／行話）：
- 口頭禪或習慣用語：
- 他絕對不會說的話：
- 情緒激動時的說話方式：
- 範例台詞（3 句，不同情境）：

## 外觀錨點
（3 個讀者一看就認得的具體細節，不要全身清單。）

## 背景時間線
| 年齡／年份 | 事件 | 對他的影響 |
|---|---|---|

## 關係網
| 對象 | 關係 | 張力來源 | 他在對方面前會變成什麼樣 |
|---|---|---|---|

## 弧線
- 起點（故事開始時的狀態）：
- 轉折點（2–4 個）：
- 終點（或開放的可能性）：
- 卡片更新點：在哪些章節之後，Sudowrite 卡片的 Personality／Background 應該改寫成新狀態
  （Sudowrite 官方建議卡片要反映「你目前正在寫的時間點」的角色）

## 故事引擎
- 他會替故事帶來的麻煩：
- 場景種子（5 個，一句一個，要有衝突）：
  1.
  2.
  3.
  4.
  5.

## 秘密與伏筆
（讀者或其他角色還不知道的事；何時、如何揭露。對應到下面的 `[SW] Secrets`，
在 Sudowrite 裡預設隱藏，寫到揭露章節時再打開。）

## 親密關係與界線（非露骨）
（依附模式、渴望與恐懼、界線、權力動態。細節【Sudowrite 處理】。與故事無關就寫「（無）」。）

## 硬事實（連續性）
（年齡、生日、身高、傷疤、住址、職稱、稱謂……之後不能改的東西）

---

## [SW] Name
<角色全名>

## [SW] Role
<Protagonist / Antagonist / Supporting 等，照 Sudowrite 的下拉選單>

## [SW] Pronouns
<例：她（she/her）>

## [SW] Groups
<他所屬的團體、組織、家族，用逗號分隔；沒有就寫「（無）」>

## [SW] Other Names
<所有暱稱、綽號、稱謂、頭銜、別人怎麼叫他，用逗號分隔。Sudowrite 靠這欄辨認「文中提到的是誰」，要寫齊>

## [SW] Personality
<最重要的放最前面。用行為寫，不用形容詞清單>

## [SW] Background
<與目前故事時間點相關的過去；不要寫到還沒發生的事>

## [SW] Physical Description
<外觀錨點 + 動作習慣（怎麼走路、手放哪裡）>

## [SW] Dialogue Style
<句長、用詞、口頭禪、情緒時的變化，附 1–2 句範例台詞>

## [SW] Motivation
<想要什麼、為什麼、怕什麼>

## [SW] Relationships
<每個重要對象一句：名字——關係——張力>

## [SW] Secrets
<秘密。匯入後請在 Sudowrite 按眼睛圖示隱藏，揭露時再打開>

---

## 待確認
1.

````

## `framework/templates/dossier-world.md`

````
---
kind: world
name: "<元素名稱>"
sw_section: Worldbuilding
---

# 世界觀元素：<元素名稱>

> 上半部是調查檔案；下半部 `## [SW]` 是 Sudowrite 的 Worldbuilding 卡片。

## 一句話定位
（這是什麼、為什麼故事需要它。）

## 類型
（地點／勢力或組織／魔法或科技體系／文化習俗／歷史事件／物品／生物／線索……）

## 運作規則
- 能做到什麼：
- 做不到什麼（硬限制）：
- 代價（誰付、付什麼）：
- 例外與漏洞（故事會想利用的地方）：

## 感官調色盤
- 看：
- 聽：
- 聞／嘗：
- 觸：
- 一個只有這裡才有的細節：

## 社會與權力
- 誰因它受益、誰因它受害：
- 日常生活因它而變成什麼樣：
- 經濟／政治影響：

## 歷史
| 時間 | 事件 | 留下的痕跡 |
|---|---|---|

## 術語表
| 詞 | 意思 | 誰會這樣說 |
|---|---|---|

## 衝突與故事鉤子
（5 個，一句一個，要能變成場景。）
1.
2.
3.
4.
5.

## 與角色的連結
（哪些角色被它塑造、依賴它、想毀掉它。）

## 秘密
（表面之下的真相；揭露時機。對應 `[SW] Secrets`，在 Sudowrite 預設隱藏。）

## 硬事實（連續性）

---

## [SW] Name
<元素名稱>

## [SW] Role
<Setting / Item / Clue / 或自訂類型，例：Faction、Magic System>

## [SW] Other Names
<別名、舊名、俗稱、縮寫，用逗號分隔>

## [SW] Description
<是什麼、看起來感覺起來如何、為什麼重要。最重要的放最前面>

## [SW] Rules
<運作規則、硬限制、代價>

## [SW] Sensory Details
<寫到這裡時要出現的感官細節>

## [SW] Secrets
<秘密。匯入後在 Sudowrite 隱藏，揭露時再打開；沒有就寫「（無）」>

---

## 待確認
1.

````

## `framework/templates/dossier-idea.md`

````
---
kind: idea
name: "<點子名稱>"
sw_section: Story
---

# 創意／故事核心：<點子名稱>

> 先提出 3 個差異很大的方向，再推薦一個，並替推薦的方向寫好 Sudowrite 的
> Braindump／Genre／Style（Synopsis 可以交給 Sudowrite 從 Braindump 生成）。

## 方向 A：<名稱>
- Logline（一句話，含主角、目標、阻礙、代價）：
- 鉤子（讀者為什麼要翻第一頁）：
- 核心問題（讀者一路想知道的事）：
- 主題：
- 語氣與參考作品：
- 新鮮在哪裡／翻轉了哪個套路：
- 風險（這個方向最可能寫壞的地方）：

## 方向 B：<名稱>
（同上）

## 方向 C：<名稱>
（同上）

## 推薦
（推薦哪個方向、為什麼；或怎麼混合。）

## 推薦方向的故事骨架
- 開場狀態：
- 引發事件：
- 中點翻轉：
- 最低點：
- 高潮與結局（或開放的可能）：
- 需要進一步調查的角色／世界觀元素（可直接變成下一次的 brief）：

---

## [SW] Braindump
<給 Sudowrite 的「電梯簡報＋我知道的一切」：前提、主角與對手、關鍵事件、結局方向、
不可改的設定、語氣。至少幾百字，越具體越好（上限 4,000 字）>

## [SW] Genre
<不要只寫類型標籤，要寫主題與閱讀體驗，例：「都市奇幻／職場，帶黑色幽默的成長故事」>

## [SW] Style
<短句描述文風，例：「冷靜克制，短句多，對白犀利，環境描寫只給一個精準細節。」
非英文專案最後加一句語言指令，例：「全部以繁體中文（台灣用語）寫作。」
視角與時態請在 Sudowrite 的 POV/Tense 選單設定，這裡只重複一句給外掛看>

## [SW] Synopsis
<選填。留「（交給 Sudowrite 生成）」也可以>

---

## 待確認
1.

````

## `framework/sudowrite-fields.json`

````
{
  "_about": "Sudowrite Story Bible 欄位與上限。hard = Sudowrite 官方公布的上限（超過會被擋或截斷）；soft = 本框架的建議值（Sudowrite 沒公布，但卡片太長時 Characters/Worldbuilding 會最先被擠出上下文）。字數算法：每個中日韓字元算 1、每個英文單字算 1。來源見 docs/sudowrite-2026-09.md，查核日 2026-09-30。",

  "hard_limits_words": {
    "Braindump": 4000,
    "Synopsis": 4000,
    "Style Examples": 1000
  },
  "hard_limits_chars": {
    "Portrait Appearance": 2500
  },
  "soft_limits_words": {
    "Genre": 80,
    "Style": 120,
    "Personality": 400,
    "Background": 500,
    "Physical Description": 200,
    "Dialogue Style": 250,
    "Motivation": 200,
    "Relationships": 350,
    "Secrets": 250,
    "Description": 450,
    "Rules": 350,
    "Sensory Details": 200,
    "Story Hooks": 250
  },

  "story_fields": ["Braindump", "Genre", "Style", "Synopsis"],
  "character_columns": ["Name", "Role", "Pronouns", "Groups", "Other Names", "Personality",
                        "Background", "Physical Description", "Dialogue Style"],
  "worldbuilding_columns": ["Name", "Role", "Other Names", "Description"],

  "hide_in_sudowrite": ["Secrets"],

  "export_order": ["story", "characters", "world"]
}

````

## `docs/sudowrite-2026-09.md`

````
# Sudowrite 現況調查（2026-09-30）

> 來源以官方文件（docs.sudowrite.com，大多標示 2026 年 1 月更新）與官方 changelog
> （feedback.sudowrite.com，讀到 2026-09-28 的 190 則）為主，網址列在文末。
> 標 **未證實** 的是官方沒寫、或只有第三方說法的事。Reddit、YouTube 這次抓不到，沒有社群實測資料。

## 一、先講結論：這對我們的框架代表什麼

1. **角色和世界觀可以用 CSV 一次匯入，而且不經 AI 改寫。** 所以我們的成品直接輸出成
   Sudowrite 官方模板格式的 CSV，最省事、最不會走樣。
2. **Sudowrite 靠名字辨認「現在提到的是誰」。** 卡片的 Other Names（暱稱、稱謂、綽號）
   一定要寫齊，否則寫到「阿晚」時它不會帶入「林晚」的卡片。
3. **上下文不夠時，Worldbuilding 和 Characters 最先被擠掉。** 卡片要把最重要的資訊放前面，
   不要寫成長篇散文。但官方也說「越具體，AI 寫得越好」——具體而不冗長。
4. **角色卡要反映「目前寫到的時間點」。** 整條弧線放在我們的調查檔案裡，Sudowrite 卡片只放
   當下的狀態，寫到轉折後再更新。
5. **劇透用「隱藏」處理。** 每張卡、每個特質都有眼睛圖示，隱藏後所有 AI 功能都看不到。
   我們把秘密放在獨立的 `Secrets` 特質，匯入後隱藏，寫到揭露章節再打開。
6. **中文可以用，但要明說。** Write 會跟著你的語言；Draft 和外掛有時會跑回英文。
   官方建議在 Extra Instructions、外掛提示裡加「全部以某語言輸出」這類指令（要用那個語言寫）。
   我們的 Style 欄位最後固定加一句語言指令。

## 二、「一次寫很多字」實際上是什麼

你提到 Sudowrite 現在可以一次寫完很長的小說。查到的官方資料是：

- **Draft**（打字機圖示，以前叫 Chapter Generator，更早叫 Story Engine）是寫長文的主力：
  依照你給的 **Scenes**（逐條列出的場景）一次寫一整章。官方部落格（2026-08-06 更新）說
  一章大約 **3,000–5,000 字以上**。**沒有字數設定**，長度由場景條數決定。產生前會先估
  字數與點數，2026-08-14 起估計值的上限就是最高收費；中途可以暫停。
- **Write**：一次 1–6 張卡，每張約 50–1,500 字，或選 Max words（約 2,000 字）。
- **First Draft**：空白文件一次最多 3,000 字。**Rewrite**：最多 6,000 字。
- **Chat（開啟 Allow edits）**：可以建立、編輯文件，更新 Story Bible，執行你核准的多步驟計畫。
- 到 2026-09-28 為止，官方文件和 changelog 裡**找不到**「一鍵寫完整本書」的功能。
  有一則第三方搜尋摘要提到「Story Engine 3.0 全書生成」，官方沒有對應資料，視為**未證實**。

所以實務流程是：**Story Bible → Outline（分章摘要）→ 每章的 Scenes → Draft 一章一章寫**。
我們的框架負責把 Story Bible 做到最好；Outline 與 Scenes 之後可以加一個任務類型來做。

## 三、Story Bible 的七個區塊

| 區塊 | 作用 | 誰會讀它 |
|---|---|---|
| Braindump | 你手寫的「電梯簡報＋我知道的一切」，官方建議至少幾百字 | Synopsis |
| Genre | 你手寫；要寫主題，不要只寫標籤（「友情變愛情的浪漫喜劇」而不是「浪漫」） | Synopsis、Outline、Scenes、正文 |
| Style | 你手寫，或用 Match My Style 分析範文產生；短句描述文風 | Draft、Write 的正文 |
| Synopsis | 由 Braindump＋Genre 生成（用 Muse） | Characters、Worldbuilding、Outline、Scenes |
| Characters | 角色卡；可從 Synopsis 一次生成，或手動、或匯入 | Outline、Scenes、Draft、Write、Quick Edit、Chat |
| Worldbuilding | 世界觀卡；用模板（Setting、Item、Clue…）或自訂 | Outline、Scenes、正文 |
| Outline | 幕與分章摘要；POV／時態在這裡設定；「Start Chapter」會建立連結的文件 | Scenes 生成、Draft |

**流水線：** Braindump（＋Genre）→ Synopsis → Characters／Worldbuilding → Outline →
Scenes → Draft 寫正文。Style 不從別處生成，但影響所有正文。

### 角色卡
- 欄位：名字、Role（下拉選單，例：Protagonist、Supporting）、預設特質 **Pronouns、Groups、
  Other Names、Personality、Background、Physical Description、Dialogue Style**。
- 可以替單張卡加特質，也可以改所有卡的預設特質；2025-11-26 起每種 Role 可以有自己的特質模板。
- 每個特質都有 Generate／Rewrite，每張卡有版本紀錄。2026-09-25 起可以生成角色肖像
  （Appearance details 上限 2,500 字元，每張圖 5,000 點）。
- Role 下拉選單的完整選項官方沒列出（**未證實**）。

### 世界觀卡
- 欄位：名字、類型、各模板的特質、Other Names。官方只舉了 Setting、Item、Clue 三種模板當例子。
- 官方寫法建議：「如果一個資淺的作家或校對看得懂你的特質，AI 就處理得來。」

### Sudowrite 怎麼決定帶入哪些卡
- **Saliency Engine**：自動挑出相關的卡片與特質（外掛用 `{{characters}}` 時也是；用
  `{{characters_raw}}` 則全部帶入）。
- **Story Bible Detection**：在 Scenes 裡用底線標出認得的角色與元素。官方說 Draft 一直是
  靠「認得出來」才帶入卡片，建議用底線檢查錯字。→ **名字與 Other Names 一定要一致。**
- **隱藏（Visibility）**：眼睛圖示，卡片與單一特質都能隱藏，所有 AI 功能都看不到。
  官方沒有「永遠帶入」的開關。
- **上下文不夠時的丟棄順序**：Worldbuilding → Characters → 前一章 → 連結的大綱摘要 →
  Genre → Key Details → Tone → Style → 前文 → 選取的文字。

## 四、字數上限

Sudowrite 以英文 word 計。中文怎麼算官方沒說，我們保守地把每個中文字當一個 word。

| 欄位 | 上限 | 來源 |
|---|---|---|
| Braindump | 4,000 words | changelog 2026-01-12 |
| Synopsis | 4,000 words | changelog 2025-12-22、2026-01-12 |
| Style Examples（範文） | 1,000 words，只用在 Draft | Muse 文件 |
| 角色卡數量 | 每個 Story Bible 最多 2,000 張，單一特質沒有公布上限 | Characters 文件 |
| 世界觀卡數量 | 最多 2,000 個 | CSV 模板 |
| Outline | 沒有字數上限，章數不限 | Outline 文件 |
| 角色／世界觀 AI 匯入（非 CSV） | 輸入 ≤ 60,000 words，每次 ≤ 30 項 | Import 文件 |
| 肖像 Appearance details | 2,500 字元 | Portraits 文件 |
| Genre、Style、Scenes、Extra Instructions | 官方沒公布（**未證實**） | — |

框架在 `framework/sudowrite-fields.json` 另外訂了「建議長度」（soft），超過只警告不擋。

## 五、匯入與匯出

- **角色 CSV**（Characters 標題旁 ••• → Import → CSV，不經 AI）：一列一個角色、一欄一個特質、
  第一列是欄名。官方模板欄位：
  `Name,Role,Pronouns,Groups,Other Names,Personality,Background,Physical Description,Dialogue Style,<自訂特質…>`
- **世界觀 CSV**（Worldbuilding 標題旁 ••• → Import → CSV）：
  `Name,Role,Other Names,Description,<自訂特質…>`（這裡的 Role 就是類型，例：Setting）
- **Outline**：••• → Import Outline，可貼文字或上傳檔案；CSV 是兩欄（左欄章名、右欄內容），
  官方說這樣匯入不會被 AI 改動。
- **Braindump、Genre、Style、Synopsis** 沒有匯入功能，只能貼上（或請 Chat 幫你填）。
- **重複匯入會不會合併同名卡片，官方沒寫**（未證實）。更新既有卡片請逐欄貼上。
- **Import Novel**：匯入既有小說（建議 12 萬字以內），自動建立 Story Bible 與 5–7 個主要角色。
- **匯出**：專案可匯出 .zip 或合併成一份 .docx，但**不含 Story Bible**；Outline、Characters、
  Worldbuilding 可以各自匯出成 CSV。→ **我們的 repo 就是你的 Story Bible 備份。**
- **Series 資料夾**：同一系列的書共用 Characters 與 Worldbuilding（改一處全部同步）。

## 六、模型與成人內容（照官方說法整理）

- **Muse**（Muse 1.5）：Draft 和 Write 的預設，也負責 Expand 與 Synopsis。官方說它
  「什麼都會寫、沒有過濾」，是站上最不設限的模型。
- **Excellent** = Sudowrite 自家的 **Ballad 1.1**（2026-06-02 起，取代 Claude 3.7 Sonnet）；
  官方形容「非常寬鬆」。Rewrite 在 2026-09-22 改用 Ballad。
- **實驗模型**（Write、Draft、外掛都能選）：Claude（Opus 4.6–5.5、Sonnet 4.6–5.5、Fable 5.1）、
  GPT（5.4、5.6 系列、GPT-6 Astra／Sol／Luna）、Gemini、Kimi、GLM、Qwen、Grok 等。
  官方說 Claude 系列「中等」、OpenAI 系列「嚴格」、Grok「寬鬆」。
- **沒有「成人內容開關」。** 用模型選擇、Key Details（寫明尺度）、Extra Instructions、
  Tone Shift（Sensual／Romantic）來控制。
- 服務條款禁止涉及未成年人的性內容、違法用途等。外掛的標題與說明要維持 PG-13。

→ 框架裡標了【Sudowrite 處理】的部分，建議在 Sudowrite 用 **Muse 或 Excellent（Ballad）** 寫。

## 七、其他功能

- **Style 工具**：Match My Style 從範文產生 Style 描述；Style Examples 最多 1,000 字範文
  （格式 `Example 1: "…"`，全帳號共用，只用在 Draft）；Style Guide 2026-06-30 起搶先體驗（細節未證實）；
  My Voice（自訓模型）已停止開發。
- **外掛（Plugins）**：社群外掛上千個，可以選任何模型，能用 `{{braindump}}`、`{{characters}}`、
  `{{worldbuilding}}`、`{{outline}}` 等變數讀 Story Bible。
- **Canvas**：白板，有 Hero's Journey、Hollywood Beats、Story Circle、Romance 等大綱模板，可以生成大綱再複製出來。
- **方案**（2026-09 定價頁）：Hobby & Student 225,000 點／月（年繳 $10、月繳 $19）、
  Professional 1,000,000 點（$22／$29）、Max 2,000,000 點、可累積 12 個月（$44／$59）。
  不同模型耗點差很多：官方範例 200 字，GPT-5 Nano 約 70 點，Claude 4.1 Opus 超過 8,000 點。

## 八、官方的寫卡建議

- 具體、一致、清楚；刪掉過時或互相矛盾的內容。
- 卡片要反映目前寫到的時間點。
- Scenes 裡要把事情講明白：寫「Suzie 知道他殺了鄰居的狗並把牠埋了」，不要寫「他做的事」。
- 暱稱與團體寫在 Other Names、Groups，並用 Scenes 的底線確認有被認出來。
- Genre 要寫主題；Style 用短句描述（例：「冷峻、陰森，短句，充滿威脅感的對白」），每章前可以調整。
- 視角與時態用 POV/Tense 選單設定，不要只寫在 Style（Style 裡重複一句給外掛看即可）。
- 一個 Scene 只寫一個轉折，「寫變化，不寫氣氛」；語氣放在 Extra Instructions。
- 劇透（例如兇手的動機）先隱藏；系列作可以每本書一張卡，視需要顯示或隱藏。
- 「特質寫成具體行為」「用現在式」是我們框架的做法，**不是**官方建議。

## 來源

- Story Bible 各區塊：[Braindump](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/braindump/bgfrku4qGdfbiFH3ar9PE2)、
  [Genre](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/genre/hCJPQqQYtUQm7ntdcRFJHg)、
  [Style](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/style/4gqKgVVjdN6XTKo71HChqV)、
  [Synopsis](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/synopsis/r4GGUdR23VKcK2WrQVdheb)、
  [Characters](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/characters/a7tdE1ZB8KvAwMD3Mopwpd)、
  [Worldbuilding](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/worldbuilding/uc5NfWSz4x8Wm3S19LZeo8)、
  [Outline](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/outline/3owKyHXUm1bCdp41b2Npjk)、
  [What is Story Bible](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/what-is-story-bible/jmWepHcQdJetNrE991fjJC)
- 帶入機制：[Saliency Engine](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/saliency-engine/4KL8gFeLZNvk8CEeXpfwB2)、
  [Visibility](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/visibility-settings/4KL8gFeLZP6ep8keUhKVGp)、
  [Chapter Continuity](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/chapter-continuity/4KL8gFeLZQ6GSBjDWtSbV6)、
  [Story Bible Detection](https://feedback.sudowrite.com/changelog/mag-story-bible-detection-and-visibility-update)
- 寫作功能：[Scenes & Draft](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/scenes--draft/49p5MTVxTKkVFEC5rVUzpY)、
  [Write](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/write/pvxUvbQqYybfEosqx1sXjY)、
  [First Draft](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/first-draft/gMcJCRTRFqB8w3hBWYAC5M)、
  [Chat](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/chat/5vbuELXf6LZQnGfVzsEXCV)、
  [官方部落格：Scenes/Beats](https://www.sudowrite.com/blog/your-outline-sucks-heres-how-to-use-sudowrite-beats-to-fix-it/)、
  [Draft 估算](https://feedback.sudowrite.com/changelog/improved-draft-estimates-plus-a-bunch-of-fixes)、
  [Write Max words](https://feedback.sudowrite.com/changelog/new-to-write-max-words)
- 上限與改版：[Simplified Story Bible](https://feedback.sudowrite.com/changelog/simplified-story-bible)、
  [Three big improvements](https://feedback.sudowrite.com/changelog/three-big-improvements)、
  [Larger synopsis](https://feedback.sudowrite.com/changelog/text-highlighting-and-larger-synopsis)、
  [Role-based templates](https://feedback.sudowrite.com/changelog/new-role-based-character-templates)
- 模型與內容政策：[Muse](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/sudowrite-muse/4k9bFDMSyic6mFPkYFHrkZ)、
  [Which AI model](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/which-ai-model-should-i-use/veMq9xRH6KLCQPFm5XkQx7)、
  [Prose modes](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/prose-modes--models/2X5FuivhsbwUiMNym5eUqm)、
  [Ballad 1.1](https://feedback.sudowrite.com/changelog/even-more-excellent-prose)、
  [服務條款](https://docs.sudowrite.com/legal-stuff/h8ppDEnJAwytH3jhJKu6c1/terms-and-conditions/sMnXucDXEq8wBDjjsQq37A)
- 匯入匯出：[Importing](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/importing-files/rbGUgrZM6tNuXFG1hjDFyS)、
  [Exporting](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/exporting-files/3NtVWXcnwYaRCmPW2iwcCB)、
  [Series](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/series-support/3vfbZPCB1ANLm75FXmJf28)、
  [角色 CSV 模板](https://editor.sudowrite.com/assets/sudowrite-characters-import-template.csv)、
  [世界觀 CSV 模板](https://editor.sudowrite.com/assets/sudowrite-worldbuilding-import-template.csv)
- 語言：[Can I use Sudowrite in other languages?](https://docs.sudowrite.com/resources/ktuxRrzphwp3uTNneRtaos/can-i-use-sudowrite-in-other-languages/aR5Me5vw2J3wmLD9acqrvw)
- 方案：[Plans](https://docs.sudowrite.com/plans--account/wBnmhtSyMcWtk2BLzifGkz/what-plans-are-available/mwfVvj2rGcKYs1BQy4Pdcb)、
  [Pricing](https://sudowrite.com/pricing)
- 其他：[Tips & Tricks](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/tips--tricks/eBjBne7foMi8uYFxWEPCai)、
  [POV/Tense](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/setting-pov-and-tense/5gKBNzBQLB7C8yuBhHQ983)、
  [Canvas](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/canvas/pQGLNzeYo1kLhGo14rdBy6)、
  [Plugins](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/how-do-i-build-plugins/a3iVxJb4UZLKfSxf8BG3mY)、
  [Portraits](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/portraits/8FB59VFrbbhcmBRYNicXis)

````

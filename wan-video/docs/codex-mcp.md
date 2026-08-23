# 讓 Claude Code 跟 OpenAI Codex 協作

雙擊 **`setup-codex.bat`** 就好。下面是它做了什麼、以及幾件你應該先知道的事。

---

## 先回答你的三個問題

### 1. 我要給你 Codex API key 嗎？

**不要，而且不需要。**

- **不要**：貼進對話的東西會存成 transcript。任何 key 貼進來就等於外洩了，
  跟 CivitAI key 一樣的規矩 —— 那個是你自己填進 `.env`，這個也一樣不經過我。
- **不需要**：`codex login` 是**開瀏覽器登入**，直接用你的 ChatGPT 方案
  （Plus / Pro / Business 都可以），根本沒有 key 這回事。

真的想用 API key 的話，Codex 是**從 stdin 讀**的，所以連你的 shell 歷史都不會留下：

```powershell
$env:OPENAI_API_KEY = "sk-..."          # 只存在這個視窗
$env:OPENAI_API_KEY | codex login --with-api-key
```

這個設計就是為了讓 key 不要出現在指令參數裡。腳本**刻意不幫你做這一步** ——
憑證是你的，不該經過任何腳本或對話。

### 2. 你可以幫我裝嗎？

**我可以驗證整條流程，但沒辦法幫你「裝好放著」**，原因很實際：

我跑 Claude Code 的這個容器是**用完就丟的**。我剛剛在裡面真的裝了一次
（`codex-cli 0.147.0`）、註冊成 MCP server、確認 `claude mcp list` 顯示
**`codex: codex mcp-server - ✓ Connected`**，然後把註冊移除、把環境還原。
那次安裝隨著容器一起消失了。

所以我能給你最有用的東西是**一個可以重複執行的安裝腳本**，commit 進 repo，
在你自己那台機器上跑 —— 那才會留下來。就是 `setup-codex.bat`。

### 3. 怎麼裝

```
雙擊 setup-codex.bat
```

它會：

1. 確認有 npm（沒有的話告訴你去裝 Node.js LTS，**不會自己動手裝**）
2. `npm install -g @openai/codex`
3. 檢查登入狀態 —— **沒登入的話只會告訴你自己跑 `codex login`**
4. `claude mcp add codex -- codex mcp-server`（已經註冊過就跳過）
5. 跑 `codex doctor` 把健康狀況印出來

跑完**重開 Claude Code**，然後 `claude mcp list` 應該看到 `codex ... ✓ Connected`。

---

## 裝好之後怎麼用（**沒有 `/codex` 這個指令**）

先講最容易踩的：**打 `/codex` 不會有任何反應，因為那個指令不存在。**

MCP server 只有在提供 **prompts** 的時候才會產生斜線指令，而且名字長得像
`/mcp__codex__<prompt名>`，永遠不會是 `/codex`。而 Codex 的 server
**一個 prompt 都沒有提供**。實測（JSON-RPC 直接問它）：

```
initialize  → capabilities: {"tools": {"listChanged": true}}   ← 只有 tools
tools/list  → ["codex", "codex-reply"]
prompts/list → 沒有回應，連這個方法都不答
```

它提供的是兩個**工具**：

| 工具 | 作用 |
| --- | --- |
| `codex` | 開一個新的 Codex session 跑一件事 |
| `codex-reply` | 接續既有 session 再問一輪（就是下面「多輪有問題」講的那個機制） |

**工具是 Claude Code 呼叫的，不是你打的。** 所以用法是直接用講話交代：

```
叫 Codex 去看 app/images.py 的 ControlNet 那段有沒有問題
讓 Codex 獨立驗證一次 charpacks.py 的權重計算跟 index.html 對得上
```

Claude Code 會呼叫 `codex` 工具、把結果拿回來。你不用記任何指令。

---

## 「在這個對話裡直接裝」為什麼行不通

你問能不能裝在這邊、直接用 `/codex`。我照做了一次並實測，結果是**兩個都卡住**，
所以寫清楚免得你再試：

```
npm install -g @openai/codex     已經裝好      codex-cli 0.147.0
claude mcp add codex -- ...      註冊成功      codex: codex mcp-server - ✓ Connected
這個對話看得到那個工具嗎？        ✗ 看不到
codex login status               ✗ Not logged in
```

**第一個卡點：MCP server 是「開對話時」載入的。** `claude --help` 裡
`--mcp-config` 跟其他設定並列在啟動參數，**沒有任何 reload 指令**。
所以我在對話中途註冊，這個正在跑的對話不會看到它 —— 我實測搜過工具清單，
`mcp__codex__codex` 不存在。

**第二個卡點：Codex 沒有登入。** 而登入要你的憑證，那個不能經過我。

**第三個卡點（最關鍵）：這個容器是用完就丟的。** 就算開新對話，也是**新的容器**，
上面沒有 codex。所以「裝在這邊」在這個雲端環境裡永遠不會留下來。

### 那要怎麼「刷新」

**沒有指令可以刷新，只能開新對話。** 你記得的 `bash /reload-skills` 那種東西
在這個環境裡不存在（我找過 `/root/.claude` 和專案的 `.claude/`，沒有任何 reload 指令）。

skills 跟 MCP server 都一樣：**在對話啟動時掃一次**，之後不再重掃。

---

## 這在做什麼

`codex mcp-server` 是 Codex CLI 內建的子命令（不是第三方套件），
它讓 Codex 用 stdio 當一個 MCP server 跑起來。註冊之後，
Claude Code 就能**把工作交給 Codex 當成一個工具來呼叫**。

```
你 ──► Claude Code ──MCP/stdio──► codex mcp-server ──► OpenAI
                │
                └─► 原本的工具（檔案、bash、git…）
```

反方向也可以（Codex 當 client、Claude Code 當 server，用 `claude mcp serve`），
但那個方向要另外設定，而且對這個專案沒什麼用 —— 你的主要工作流程在 Claude Code 這邊。

---

## 什麼時候值得用

老實說：**多數時候你不需要它。** 值得叫 Codex 的情況是這幾種：

| 情況 | 為什麼交給 Codex |
| --- | --- |
| **第二意見** | 同一段程式讓另一個模型看，抓到的東西不一樣。這個專案已經吃過兩次 review 的好處了 |
| **規格很明確的大批修改** | 「把這 40 個檔案的 X 改成 Y」這種，Codex 執行得又快又不囉唆 |
| **獨立驗證** | 我說「這條線路是對的」，你可以叫 Codex 自己去看一遍，不用信我 |

不值得的情況：需要長對話上下文、跨檔案架構推理、或者本來就在做的漸進式開發 ——
多一層轉手只是變慢。

---

## 幾個要注意的地方

- **要花錢或吃額度。** 走 ChatGPT 方案就吃你的方案額度，走 API key 就是按 token 計費。
  這跟這個專案其他部分完全相反 —— app 本身是全本機、免費、不連外的。
- **官方 `mcp-server` 的多輪對話有已知問題。** 社群回報它的 conversation tracking
  有 bug，導致多輪 session 不太能用，所以有一堆第三方 bridge 在補這個洞
  （[參考](https://codex.danielvaughan.com/2026/03/27/claude-code-codex-mcp-in-practice/)）。
  **這點我沒有實際驗證過** —— 我只驗到「連得上」，沒有跑過多輪對話（那需要憑證）。
  如果你用起來覺得多輪很怪，那大概就是這個問題，不是你設定錯。
- **它會看到你的程式碼。** Codex 是雲端服務，你叫它處理的內容會送到 OpenAI。
  這個 repo 是本機 AI 工具的程式碼，沒什麼敏感的；但你的 `.env`（CivitAI key）
  和 `models/`、`data/` 就不要丟給它。

---

## 我驗過什麼、沒驗過什麼

在這個 Linux 容器裡實測過的：

| 驗過 | 結果 |
| --- | --- |
| `npm install -g @openai/codex` | 成功，`codex-cli 0.147.0` |
| `codex mcp-server` 這個子命令存在 | 有，help 寫 "Start Codex as an MCP server (stdio)" |
| `codex login --with-api-key` 從 stdin 讀 key | 有，help 明寫 `printenv OPENAI_API_KEY \| codex login --with-api-key` |
| `claude mcp add codex -- codex mcp-server` | 成功 |
| `claude mcp list` | **`codex: codex mcp-server - ✓ Connected`** |
| 重複執行安裝腳本 | 正確偵測「已經註冊過」，不會重複加 |
| `setup-codex.ps1` 通過 PowerShell parser、BOM + CRLF 正確 | 有測試釘住 |

**沒驗過的**：實際叫 Codex 做事（要憑證，而憑證是你的）、
Windows 上的行為（我只有 Linux + PowerShell 7，`setup-codex.bat` 跑的是 5.1）、
上面提到的多輪對話問題。

腳本本身用了跟 `update-windows.ps1` 同一套 `Invoke-Native` 包裝 ——
就是修「一個成功的 `git pull` 被當成失敗」那個 bug 學到的教訓：
**原生指令的成敗只看結束代碼，不看 stderr。**

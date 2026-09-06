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

**可以，而且現在已經裝好了。這一節本來寫「不行」，那個答案已經過期了。**

> **2026-09-06 更正。** 這份文件原本寫「我沒辦法幫你裝好放著」，理由是
> 容器裡的工具在對話中途註冊、這個對話看不到它，而且登入要瀏覽器。
> 現在兩件事都不成立了：
>
> * **工具是可見的。** 這個雲端環境會在**對話啟動時**就把 codex 註冊好，
>   所以 `mcp__codex__codex` 一開始就在工具清單裡。實測 `claude mcp list`
>   顯示 `codex: codex mcp-server - ✓ Connected`。
> * **登入不需要瀏覽器。** `codex login --device-auth` 是給無頭機器用的流程：
>   它印一個網址和一組一次性代碼，你在**自己的電腦上**打開輸入，
>   token 由 OpenAI 直接發回容器。**憑證完全不經過對話。**
>
> 下面那一節（「在這個對話裡直接裝為什麼行不通」）也一起改了，
> 原本的內容留著並標明哪裡錯，因為那是當時實測的結果，不是憑空寫的。

所以現在的做法是：

```bash
bash scripts/codex-login.sh
```

它會自己判斷情況 —— 已經登入就不重跑；有 `OPENAI_API_KEY` 就用它
（從 pipe 讀，不走參數，所以不會出現在 `ps` 或 shell 歷史裡）；
兩個都沒有就跑裝置碼流程。

`setup-codex.bat` 仍然有用，但它是給**你自己那台 Windows** 的 —— 兩件不同的事。

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

## 在這個對話裡直接用：現在可以了

**現況（2026-09-06 實測）：**

```
codex --version                  codex-cli 0.147.0          ✓ 容器裡已安裝
claude mcp list                  codex: ✓ Connected         ✓ 對話啟動時就註冊好
工具清單有 mcp__codex__codex 嗎？  ✓ 有
~/.codex/auth.json               ✗ 不存在  ← 只缺這個
實際打一發                        401 Unauthorized           ← 就是上面那行的後果
```

**「Connected」只代表那個 process 起得來，不代表登入了。** 這是最容易誤會的一點：
`claude mcp list` 是綠的，工具也在，但第一次真的呼叫才會撞到 401。

補上登入（`bash scripts/codex-login.sh`）之後就能用了 —— **但還有一步**，見下。

### 最容易卡住的一步：登入之後要重啟 MCP server

實測到的（2026-09-06）：

```
codex mcp-server  process 啟動   19:02:00
~/.codex/auth.json 寫入          19:09:00   ← 晚了七分鐘
呼叫 mcp__codex__codex           401 Unauthorized
```

**`codex mcp-server` 是在啟動時把憑證讀進記憶體的。** 你事後才登入，
那個已經在跑的 process 不知道 —— 它會一直回 401，而 `claude mcp list`
還是好端端顯示 `✓ Connected`。

**這就是「Connected 不等於登入」最貴的一次示範。** 解法是把它砍掉，
下次呼叫時會用新憑證重開：

```bash
kill $(pgrep -f 'codex mcp-server')
```

`scripts/codex-login.sh` 登入成功後會自己偵測有沒有這個 process，
有的話直接把該執行的 `kill` 指令印給你。

驗證通了沒有，就叫它讀一個真的檔案（不要只叫它回「OK」——
那不能證明它讀得到你的 repo）：

> 叫 codex 讀 `app/shortdrama.py`，回答定義了幾種景別、以及「過肩」的 tag 是什麼。

答對了就是真的通了。

### 三件仍然成立的事

1. **沒有 `/codex` 這個斜線指令。** Codex 在這裡是 **MCP server**，
   也就是**我去呼叫它**，不是你打指令。你要它做事就直接跟我說
   「叫 codex 看一下 X」。
2. **一般的 `codex login` 在這裡還是不行。** 它會開瀏覽器、等
   `127.0.0.1:1455` 的 OAuth callback，而那個 callback 你的電腦碰不到。
   要用 `--device-auth`。
3. **容器是用完就丟的。** token 會跟著消失，新 session 要重登。
   不想每次重登就把 `OPENAI_API_KEY` 設在**環境設定的環境變數**裡
   （不是貼在對話裡），新 session 一開就有。

### 原本這一節寫錯的地方

原本寫「這個對話看不到那個工具」，理由是 MCP server 只在對話啟動時載入、
沒有 reload 指令。**那個觀察本身沒錯，錯的是結論**：這個環境會在啟動時
就把 codex 註冊進去，所以不需要中途 reload。「無法中途載入」不等於「不能用」。

至於刷新：**確實沒有指令可以在對話中途重載 MCP server 或 skills，只能開新對話。**
你記得的 `bash /reload-skills` 在這個環境裡不存在（找過 `/root/.claude`
和專案的 `.claude/`）。這一點沒有變。

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

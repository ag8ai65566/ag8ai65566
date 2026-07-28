# GitHub 逐步教學：讓它每天自動去讀開放時刻

寫給完全沒用過 GitHub 的人。**全部在瀏覽器裡點，不用裝任何東西、不用打任何指令。**

一次做完，之後每天早上 06:10（日本時間）它會自己去讀一次，把結果存起來。你的旅行在
2027 年 1 月，第一個要動作的是 2026 年 10 月 1 日的 とり茶太郎 —— 也就是這件事要
自己跑兩個多月，之後還要繼續跑到旅行結束。所以值得花這 10 分鐘設好。

---

## 名詞先講清楚

| 名詞 | 是什麼 |
| --- | --- |
| **Repository（倉庫，簡稱 repo）** | 一個專案的資料夾。你的叫 `ag8ai65566/ag8ai65566` |
| **Branch（分支）** | 同一個專案的不同版本線。我的東西全在 `claude/new-session-network-2ujcou` 這條 |
| **Actions** | GitHub 幫你免費跑程式的功能。就是「每天自動執行」的那個東西 |
| **Workflow（工作流程）** | 一份「要做什麼、什麼時候做」的設定檔。我已經寫好放進 repo 了 |
| **Secret（機密）** | 加密存放的密碼。存進去之後**連你自己都看不到內容**，只有程式跑的時候能用 |

---

## 第 1 步：打開你的 repo

1. 打開 <https://github.com/ag8ai65566/ag8ai65566>
2. 沒登入的話它會叫你登入，登入完會自己回到這頁
3. 畫面最上面應該看到 **ag8ai65566 / ag8ai65566**

> 看到 **404** 的話，就是還沒登入，或登入的帳號不是這個 repo 的擁有者。

---

## 第 1.5 步：把預設分支換掉（**沒做這步，後面全部不會動**）

GitHub 有一條規則沒有例外：**定時執行和「Run workflow」按鈕，只認「預設分支」上的
workflow 檔案。** 檔案在別的分支，Actions 頁面就當它不存在。

這個 repo 沒有 `main`，預設分支是第一次做的舊分支
`claude/tokyo-restaurant-planner-yunbi0`，而程式碼全在
`claude/new-session-network-2ujcou`。所以要先換過去。

新分支完整包含舊分支的所有內容（舊分支獨有的 commit 是 0 個），換過去不會丟任何東西。

1. repo 最上方橫排點 **Settings**（最右邊那個）
2. 左側選單點 **Branches**
3. 最上面區塊 **Default branch**，現在顯示 `claude/tokyo-restaurant-planner-yunbi0`，
   右邊有個**兩箭頭交換的圖示**（⇄，滑過去會顯示 *Switch to another branch*）—— 點它
4. 下拉選 **`claude/new-session-network-2ujcou`** → 按 **Update**
5. 跳出確認視窗，按 **I understand, update the default branch**

做完 Default branch 那行應該變成 `claude/new-session-network-2ujcou`。

> 之前如果誤按過「Skip this and set up a workflow yourself」進到編輯畫面，
> 按左上的 **Cancel changes** 離開就好，不要 commit —— 那會在舊分支上留一個空的
> `main.yml`。

---

## 第 2 步：存入 OMAKASE 帳密（兩個 Secret）

1. 在 repo 頁面**最上方橫排**找到 **⚙︎ Settings**（設定）。
   那排從左到右是：`Code` `Issues` `Pull requests` `Actions` `Projects` `Wiki`
   `Security` `Insights` **`Settings`** —— **Settings 是最右邊那個**。
   > 沒看到 Settings，表示你登入的帳號沒有這個 repo 的管理權。

2. 進去之後看**左側的長條選單**，往下找到 **Secrets and variables**，
   點它會展開三個子項：**Actions** / Codespaces / Dependabot。
   **點 `Actions`**。

3. 現在畫面中間有兩個頁籤：**Secrets** 和 **Variables**。確定你在 **Secrets**。

4. 按右上角綠色按鈕 **New repository secret**。

5. 出現兩個欄位：
   - **Name**（名稱）欄填：`OMAKASE_EMAIL`
     ⚠️ 全部大寫、中間是**底線**不是減號、前後不要有空格
   - **Secret**（值）欄填：你的 OMAKASE 登入 email
   - 按綠色 **Add secret**

6. 回到列表，**再按一次 New repository secret**，加第二個：
   - **Name**：`OMAKASE_PASSWORD`
   - **Secret**：你的 OMAKASE 密碼
   - 按 **Add secret**

做完列表上應該有**兩筆**：

```
OMAKASE_EMAIL       Updated now
OMAKASE_PASSWORD    Updated now
```

> 看不到值是正常的，GitHub 加密之後任何人都看不到，包括你。要改只能整個覆蓋
> （點該筆右邊的鉛筆圖示 → 填新值 → Update secret）。

---

## 第 3 步：允許 Actions 寫回 repo

輪詢的結果要存回 repo，預設權限是唯讀的，要開一下。

1. 還在 **Settings** 裡，左側選單找 **Actions** → 點它展開 → 點 **General**
2. 頁面**滑到最下面**，找到區塊 **Workflow permissions**
3. 選 **Read and write permissions**（預設是 Read repository contents…）
4. 按該區塊下方的 **Save**

> 沒設這個的話，workflow 會跑完但最後 push 失敗，錯誤訊息是
> `remote: Permission to ... denied` 或 `403`。

---

## 第 4 步：手動跑一次，看它到底行不行

1. 回到 repo 最上方橫排，點 **Actions**
2. 第一次進來可能出現綠色大按鈕
   **I understand my workflows, go ahead and enable them** —— 按它
3. 看**左側**的 workflow 清單，應該出現 **poll bookings** —— 點它

   > **左側沒有 poll bookings，反而出現「Get started with GitHub Actions」和一堆
   > 範本？** 那就是第 1.5 步沒做成功，預設分支還是舊的。回去確認 Settings →
   > Branches 的 Default branch 是不是 `claude/new-session-network-2ujcou`。
   > **不要**按「set up a workflow yourself」去自己建檔案 —— 檔案已經在 repo 裡了，
   > 只是 GitHub 沒在看那條分支。

4. 右邊會出現一條藍色提示 *This workflow has a workflow_dispatch event trigger.*，
   右端有個按鈕 **Run workflow ▾** —— 點它
5. 展開的小框裡 **Use workflow from** 已經是預設分支，直接按綠色 **Run workflow**
6. 等 3～5 秒，**重新整理頁面**，清單最上面會出現一筆帶黃色圓點的紀錄
7. 點進去 → 點左邊的 **poll** → 展開每個步驟看進度

**看圖示判斷結果：**

| 圖示 | 意思 |
| --- | --- |
| 🟡 黃色轉圈 | 正在跑（大約 2～4 分鐘） |
| ✅ 綠色勾 | 成功 |
| ❌ 紅色叉 | 失敗，往下看「失敗怎麼辦」 |

成功的話，**Poll OMAKASE** 這個步驟展開會長這樣：

```
✓ とり茶太郎  枠なし  次回 2026-08-01T08:00:00+09:00
✓ 酉囃子      枠なし  次回 2026-08-01T15:00:00+09:00
✓ 明寂        予約可  次回 2026-08-01T23:00:00+09:00
✓ 蒼          予約可  次回 未定
✓ スペイン料理 acá  枠なし  次回 2026-08-01T13:00:00+09:00  抽選応募締切 ...
```

那就成了。**之後它每天自己跑，你不用再碰。**

---

## 第 5 步：確認結果真的存下來了

1. 回 repo 首頁（點左上 **Code**）
2. 做完第 1.5 步之後，左上角的分支選單本來就會是
   `claude/new-session-network-2ujcou`，不用切
3. 進入 **`data`** 資料夾 → 應該有一個 **`booking-state.json`**
4. 點開它，會看到每家店的 `nextOpenAt`、`windowUntil` 等等

**最有用的東西在這裡**：點該檔案右上角的 **History**（歷史），
就能看到每天的變化。你問過「三個月後還是同樣的規律嗎」—— 這份歷史就是答案，
累積幾個月之後，哪家店的時刻會漂移、哪家穩定，一翻就知道。

---

## 失敗怎麼辦

點進紅色叉的那次紀錄，展開**紅色**的那個步驟看訊息，對照下表：

| 訊息裡有 | 意思 | 怎麼修 |
| --- | --- | --- |
| `missing env: OMAKASE_EMAIL` | Secret 名字打錯 | 回第 2 步，確認**完全**是 `OMAKASE_EMAIL`（大寫、底線） |
| `login rejected` | 帳密不對 | 回第 2 步覆蓋成正確的 |
| `403` / `Cloudflare is blocking this machine's IP` | GitHub 的機器被擋（**必定發生**） | 往下看「Cloudflare 擋住 GitHub 的機器」 |
| `Permission to ... denied` | 沒開寫入權限 | 回第 3 步 |
| `Process completed with exit code 1` | 要往上找真正的紅字 | 展開該步驟捲到最上面 |
| 左側根本沒有 poll bookings | 預設分支不對 | 回第 1.5 步 |

### Cloudflare 擋住 GitHub 的機器（**已確認會發生**）

2026-07-28 實測結果：**會**。log 裡是

```
Error: https://omakase.in/users/sign_in — HTTP 403
```

其他每一環都正常 —— 安裝成功、Playwright 裝好、21 個測試全過、兩個 Secret 正確載入。
唯一的問題是 GitHub 的機器在資料中心，而 Cloudflare 擋資料中心的 IP。**家用網路不會被擋。**

**2026-07-28 續：家用網路也一樣。** 在自己的 Windows 上跑（真實家用 IP、真的登入成功、
UA 與平台一致）之後，首頁和登入頁都正常，但**五個店家頁全部 403**。

結論：擋的不是 IP，也不是帳號，是**「這是自動化瀏覽器」本身** —— Playwright 會設
`navigator.webdriver = true`，而店家頁的防護門檻比首頁高。用一般 Chrome 手動開完全正常。

技術上有辦法隱藏那個特徵，**但這個專案不做** —— 那是刻意規避網站明確表達的意願，
跟繞過 IP 封鎖是同一件事。

**所以 OMAKASE 這五家不走爬蟲。** 改用下面「更好的辦法」。

---

## 更好的辦法：用 OMAKASE 自己的功能

OMAKASE 的店家頁上就有這個按鈕：

> **お気に入り店舗の予約開始日を一覧で見る**（用清單看收藏店家的預約開始日）

以及「お気に入り」旁邊的**鈴鐺圖示**。也就是說：**把店加進收藏，OMAKASE 自己會給你
一頁列出全部的開放日期**，鈴鐺很可能還有開放前通知。

這比爬蟲好：官方支援、一頁看完五家、不會被擋、不用登入自動化。

**做法**

1. 用一般瀏覽器登入 OMAKASE
2. 把這五家都按「お気に入り」：とり茶太郎、酉囃子、明寂、蒼、スペイン料理 acá
3. 點任一頁上的「お気に入り店舗の予約開始日を一覧で見る」，把日期看一遍
4. 打開訂位雷達，點該餐廳 → 詳情頁的「**開放資訊（自己更新）**」→ 填「下次開放」和
   「受付期間到」→ **儲存**。倒數立刻重算

一個月做一次就夠 —— 開放時刻是每月變一次，不是每天。

> 鈴鐺如果會寄通知信，連「記得去看」都省了。設定一次值得試。

---

## 下面這段留著給 TableAll／未來的其他來源

GitHub 免費的機器跑不了 OMAKASE。兩條路，程式碼都不用改：

---

#### 路線 B（先做這個）：偶爾自己在電腦上跑一行

對你的實際需求這樣就夠了。到 2027 年 1 月之前真正要動作的日期只有幾個
（2026/10/01、11/01、11/04、12/01、12/24、12/29），每天輪詢的價值主要是
「偵測規律有沒有改變」，一週跑一次完全足夠。

照 [`windows-setup.md`](windows-setup.md) 把環境設好（只要做一次），之後每次就是
開 PowerShell 切到 `scraper` 資料夾，跑：

```powershell
node poll-omakase.mjs
```

結果會寫進 `..\data\booking-state.json`。把那個檔案內容貼給我，我確認讀到的東西正確。

**為什麼先做這個**：`readBookingState` 抓 DOM 的部分還沒對真實頁面驗證過（解析文字的
部分有 21 個測試，但「文字從哪個元素來」沒驗過）。先手動跑一次確認讀得到東西，再去弄
路線 A 的自動化，順序才對。

---

#### 路線 A：讓 GitHub 用你家的電腦跑（完整自動化）

一次設定，之後照排程每天自己跑。步驟瑣碎但都是複製貼上。

**A-1. 告訴 workflow 要用你的機器**

1. Settings → Secrets and variables → **Actions** → 切到 **Variables** 頁籤
2. **New repository variable**
   - **Name**：`POLL_RUNNER`
   - **Value**：`self-hosted`
   - 按 **Add variable**

**A-2. 在你的 Windows 上註冊一台 runner**

1. Settings → 左側 **Actions** → **Runners**
2. 按綠色 **New self-hosted runner**
3. **Runner image 選 Windows**、Architecture 選 **x64**
4. 頁面會列出指令，分 **Download** 和 **Configure** 兩區。在你電腦上開 PowerShell
   （不要 x86 那個），把 **Download** 區每一行照順序貼上執行 —— 它會建
   `C:\actions-runner` 並下載 runner
5. 再貼 **Configure** 區那行 `./config.cmd --url ... --token ...`
   （token 是一次性的，用它給你的那行，不要自己改）

   會問幾個問題，**全部直接按 Enter** 用預設值：runner group、runner 名稱、
   額外標籤、work folder
6. **不要**執行它給的 `./run.cmd` —— 那個關掉視窗就停了。改成裝成服務，照 GitHub
   頁面上 **Configure as a service** 那段的指令做（Windows 通常是
   `./config.cmd --runasservice`，或用它列出的 `svc` 指令）
7. 回 Settings → Actions → **Runners**，應該看到一台狀態 **Idle**（綠色）的 runner

**A-3. 再跑一次**

回 Actions → poll bookings → **Run workflow**。這次會在你的電腦上跑，出口 IP 是你家的
網路，不會被擋。

> **注意**：排程時間（06:10 JST）到的時候電腦要開著。關機那天就跳過，不會補跑。
> 對這個用途影響不大 —— 開放時刻是每月變一次，不是每分鐘。

---

## 之後要加新餐廳的話

不用再找我，兩種情況：

**有 Tabelog 頁面的**：編輯 `scraper/watchlist.txt`
1. Code（分支已經是預設的那條）
2. 進 `scraper` → 點 `watchlist.txt` → 右上角**鉛筆圖示**（Edit this file）
3. 貼上新的 Tabelog 網址，一行一個
4. 頁面下方 **Commit changes** → 綠色 **Commit changes**

**只在 OMAKASE 上的**（像 acá）：同樣方式編輯 `scraper/observed-seed.json`，
照 acá 那筆的格式加一筆，`slug` 就是網址 `omakase.in/r/` 後面那串。

加完之後隔天輪詢就會自動包含它。

---

## 為什麼分支這件事這麼要命

值得記一下，因為它的錯誤訊息完全看不出原因：**GitHub 的定時執行和手動按鈕，只讀
「預設分支」上的 workflow 檔案。** 不是「你選的分支」，也不是「有檔案的分支」。

所以檔案明明在 repo 裡、明明 commit 了、路徑也對，Actions 頁面還是說「你還沒有任何
workflow」，然後引導你去新建一個 —— 照著建下去只會在錯的分支上留一個空檔案。

以後如果我又開了新分支做東西，要讓自動化生效，就是回到 Settings → Branches
把預設分支指過去（或叫我把它合併進預設分支）。

---

## 一句話總結

第 1.5 步（換預設分支）→ 第 2 步（兩個 Secret）→ 第 3 步（開寫入權限）
→ 第 4 步（跑一次看綠勾）。

綠勾出現之後，這件事就自己跑一年，你到 2026 年 10 月再回來看
とり茶太郎 的倒數就好。

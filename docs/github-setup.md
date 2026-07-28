# GitHub 逐步教學：讓它每天自動去讀開放時刻

寫給完全沒用過 GitHub 的人。**全部在瀏覽器裡點，不用裝任何東西、不用打任何指令。**

一次做完，之後每天早上 06:10（日本時間）它會自己去讀一次，把結果存起來。你的旅行在
2027 年 7 月，也就是這件事要自己跑大概一年 —— 所以值得花這 10 分鐘設好。

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
3. 看**左側**的 workflow 清單，點 **poll bookings**
4. 右邊會出現一條藍色提示，右端有個按鈕 **Run workflow ▾** —— 點它
5. 展開的小框裡：
   - **Use workflow from** 選 **`claude/new-session-network-2ujcou`**
     ⚠️ **這步很重要**，選到 `main` 會找不到檔案
   - 按綠色 **Run workflow**
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
2. 左上角有個分支選單（預設顯示 `main`）—— 點它，選
   **`claude/new-session-network-2ujcou`**
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
| `403` / `you have been blocked` | **Cloudflare 擋 GitHub 的機器** | 往下看「Cloudflare 擋住的話」 |
| `Permission to ... denied` | 沒開寫入權限 | 回第 3 步 |
| `Process completed with exit code 1` | 要往上找真正的紅字 | 展開該步驟捲到最上面 |

### Cloudflare 擋住的話

這是唯一我從雲端**測不出來**的部分 —— OMAKASE 擋掉了我這邊的 IP，我不知道
GitHub 的機器會不會也被擋。如果被擋，**程式不用改，只要換執行的機器**：

1. Settings → Secrets and variables → **Actions** → 切到 **Variables** 頁籤
2. **New repository variable**
   - **Name**：`POLL_RUNNER`
   - **Value**：`self-hosted`
   - **Add variable**
3. 然後照 GitHub 的指引在你自己的 Windows 上註冊一台 runner
   （Settings → Actions → Runners → **New self-hosted runner**，照它給的指令貼上）

這樣它就會用你家的網路去跑，跟你自己開瀏覽器一樣。

---

## 之後要加新餐廳的話

不用再找我，兩種情況：

**有 Tabelog 頁面的**：編輯 `scraper/watchlist.txt`
1. Code → 切到 `claude/new-session-network-2ujcou` 分支
2. 進 `scraper` → 點 `watchlist.txt` → 右上角**鉛筆圖示**（Edit this file）
3. 貼上新的 Tabelog 網址，一行一個
4. 頁面下方 **Commit changes** → 綠色 **Commit changes**

**只在 OMAKASE 上的**（像 acá）：同樣方式編輯 `scraper/observed-seed.json`，
照 acá 那筆的格式加一筆，`slug` 就是網址 `omakase.in/r/` 後面那串。

加完之後隔天輪詢就會自動包含它。

---

## 一句話總結

第 2 步（兩個 Secret）→ 第 3 步（開寫入權限）→ 第 4 步（跑一次看綠勾）。
綠勾出現之後，這件事就自己跑一年，你到 2027 年 4 月再回來看倒數就好。

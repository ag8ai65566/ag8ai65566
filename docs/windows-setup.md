# Windows 逐步教學：把 OMAKASE 頁面抓下來

寫給沒用過命令列的人。**不需要安裝 Git**，全部大約 15 分鐘，其中十分鐘是等下載。

一次做完之後，以後每次只要重複第 6 步（一行指令）。

---

## 1. 安裝 Node.js

1. 打開 <https://nodejs.org/>
2. 下載標示 **LTS** 的 Windows 版本（`.msi` 檔）
3. 打開下載的檔案，**一路按「Next」到底，全部用預設值**，最後按 Install
4. 裝完按 Finish

> 需要 Node 20.12 以上。LTS 版本一定夠。

---

## 2. 下載這個專案

1. 點這個連結，瀏覽器會直接下載一個 zip：

   <https://github.com/ag8ai65566/ag8ai65566/archive/refs/heads/claude/new-session-network-2ujcou.zip>

2. 到「下載」資料夾找到那個 zip，**右鍵 → 解壓縮全部 → 解壓縮**
3. 為了後面好打字，把解壓出來的資料夾**改名成 `ledger`**，然後**拖到桌面**

現在桌面上應該有一個 `ledger` 資料夾，點進去看得到 `scraper`、`prototype`、`docs`。

---

## 3. 打開 PowerShell

1. 進到 `桌面 \ ledger \ scraper` 資料夾
2. 在資料夾**空白處**按住 **Shift** 再按**滑鼠右鍵**
3. 選「**在這裡開啟 PowerShell 視窗**」（或「在終端中開啟」）

會跳出一個黑色或藍色的視窗，最後一行長得像：

```
PS C:\Users\你的名字\Desktop\ledger\scraper>
```

**確認結尾是 `\scraper`。** 不對的話關掉重來，位置錯了後面每一步都會失敗。

> 下面每一段指令，都是「複製 → 在視窗裡按右鍵貼上 → 按 Enter」。
> PowerShell 貼上是按右鍵，不是 Ctrl+V。

---

## 4. 安裝需要的東西

```powershell
npm install
```

跑大約 1～3 分鐘，會刷很多字，正常。看到游標回到 `PS C:\...>` 就是好了。

接著裝瀏覽器（約 150MB，看網速 2～5 分鐘）：

```powershell
npx playwright install chromium
```

> 中間如果問你 `Ok to proceed? (y)`，打 `y` 再按 Enter。

---

## 5. 填入 OMAKASE 帳密

```powershell
notepad .env
```

記事本會問「找不到檔案，要建立新檔案嗎？」→ 按「**是**」。

把下面兩行貼進去（就是你 OMAKASE 的帳密）：

```
OMAKASE_EMAIL=你的email
OMAKASE_PASSWORD=你的密碼
```

**Ctrl + S 存檔**，關掉記事本。

> 這個檔案只留在你自己電腦上，不會上傳到 GitHub。

---

## 6. 執行

```powershell
node dump-omakase.mjs
```

接下來會：

1. **跳出一個 Chrome 視窗**（會自己動，不要關掉它）
2. 自動登入 OMAKASE
3. 依序打開四家餐廳的頁面，各停留幾秒抓資料
4. 全部跑完視窗自己關閉

**如果自動登入失敗**，視窗會停在登入畫面，命令列會出現：

```
請在打開的視窗裡自己登入 OMAKASE（有驗證就順手點掉）。
處理完按 Enter 繼續…
```

這時你就**自己在那個視窗裡登入**（有「我不是機器人」之類的就點掉），
弄好之後回到命令列視窗按 **Enter**。它會繼續跑。

---

## 7. 把結果給我

跑完之後，`scraper` 裡會多一個 **`dump`** 資料夾，裡面每家店三個檔案：

| 檔案 | 內容 |
| --- | --- |
| `xxxx.txt` | 整頁文字 |
| `xxxx.calendar.html` | 日曆的原始碼 |
| `xxxx.png` | 整頁截圖 |

**先自己看一眼 `.png`**——那是你**登入後**的畫面，會有你的帳號名稱，
也可能有你已經訂到的位子。確認沒問題再把 `.txt` 的內容貼給我（或把圖丟上來）。

---

## 出錯的時候

| 畫面上寫 | 意思 | 怎麼辦 |
| --- | --- | --- |
| `npm : 無法辨識...` | Node 沒裝好，或視窗是裝之前開的 | 關掉 PowerShell 重開一個再試 |
| `Cannot find module` | 位置不對，或漏了 `npm install` | 確認提示字元結尾是 `\scraper`，重跑第 4 步 |
| `missing env: OMAKASE_EMAIL` | `.env` 沒建好或存錯地方 | 重做第 5 步，確認記事本標題列是 `.env` 不是 `.env.txt` |
| `login rejected` | 帳密打錯 | 檢查 `.env`；或用第 6 步的手動登入 |
| 跳出「我不是機器人」 | Cloudflare 驗證 | 自己在視窗裡點掉，回命令列按 Enter |

指令跑不動就把**整個視窗的文字複製給我**，我看得出是哪裡卡住。

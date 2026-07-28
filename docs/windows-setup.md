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

## 3. 打開 PowerShell 並切換到 scraper 資料夾

按開始鍵，打 `powershell`，點「**Windows PowerShell**」（**不要**選有 `(x86)` 的那個）。

視窗打開時位置是你的家目錄，像 `PS C:\Users\Louis>`。**這不是我們要的位置**，
要把它切到 `scraper` 資料夾。最不會錯的做法是用拖的，不用打路徑：

1. 在 PowerShell 裡打 `cd` 再加**一個空白**。畫面變成 `PS C:\Users\Louis> cd `
   —— **先不要按 Enter**
2. 打開檔案總管，找到第 2 步解壓出來的 `scraper` 資料夾（看到就好，不用點進去）
3. **把那個資料夾拖進 PowerShell 視窗放開**，完整路徑會自動填上
4. **這時**才按 Enter

想用打字的話，桌面路徑通常是這兩個之一（Windows 有時把桌面放在 OneDrive 底下）：

```powershell
cd "$HOME\Desktop\ledger\scraper"
```

```powershell
cd "$HOME\OneDrive\Desktop\ledger\scraper"
```

**確認位置對不對**，貼這行按 Enter：

```powershell
Test-Path poll-omakase.mjs
```

出現 `True` 才往下做。出現 `False` 有兩種可能：

- **位置不對** —— 回到上面重切一次
- **zip 是舊的** —— 這支程式是後來才加的。如果你以前下載過，那份裡面沒有它。
  回第 2 步用同一個連結重新下載（連結永遠給最新版），舊資料夾刪掉或改名

  > 重下載之前先把帳密存一份，免得重打：
  > `Copy-Item .env "$HOME\Desktop\env-backup.txt"`
  > 換好資料夾之後再 `Copy-Item "$HOME\Desktop\env-backup.txt" .env` 放回去。
  >
  > **Playwright 那 150MB 不用重下** —— 瀏覽器裝在
  > `%USERPROFILE%\AppData\Local\ms-playwright`，不在專案資料夾裡。
  > 只有 `npm.cmd install` 要再跑一次。

**檢查要跑的那支程式在不在，而不是隨便一個檔案** —— 這份教學原本檢查
`dump-omakase.mjs`，結果舊 zip 明明缺了 `poll-omakase.mjs` 卻通過檢查，
一路走到第 6 步才炸 `Cannot find module`。

> 「Shift + 右鍵 →『在這裡開啟 PowerShell 視窗』」也可以，但那是在**檔案總管的
> 資料夾裡**按，不是在 PowerShell 裡按。已經開好視窗就用上面的 `cd` 就好。

> 下面每一段指令，都是「複製 → 在視窗裡按**滑鼠右鍵**貼上 → 按 Enter」。
> PowerShell 貼上是按右鍵，不是 Ctrl+V。

---

## 4. 安裝需要的東西

**注意結尾的 `.cmd`，這不是打錯**：

```powershell
npm.cmd install
```

跑大約 1～3 分鐘，會刷很多字，正常。看到游標回到 `PS C:\...>` 就是好了。

接著裝瀏覽器（約 150MB，看網速 2～5 分鐘）：

```powershell
npx.cmd playwright install chromium
```

> 中間如果問你 `Ok to proceed? (y)`，打 `y` 再按 Enter。

### 為什麼要加 `.cmd`

PowerShell 預設**禁止執行腳本檔**，而 `npm` 在 PowerShell 裡指向的是 `npm.ps1`
（一個腳本），所以直接打 `npm install` 會被擋掉：

```
npm : File C:\Program Files\nodejs\npm.ps1 cannot be loaded because running
scripts is disabled on this system.
```

npm 同時也裝了 `npm.cmd`，那個不受這條規則管。加兩個字就繞過整個問題，
**不用改任何系統設定**——這是最乾淨的做法。

真的想一次解決（只影響你這個使用者帳號，不動整台電腦）也可以：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

問 `Do you want to change the execution policy?` 時打 `Y` 按 Enter。
之後 `npm install` 就能直接用。

> 第 6 步的 `node ...` 不受影響，`node` 是 `.exe` 不是腳本。

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
node poll-omakase.mjs --headed
```

`--headed` 是「開一個看得見的視窗」。**第一次一定要加**，之後給排程自動跑才不用。

接下來會：

1. **跳出一個 Chrome 視窗**（會自己動，不要關掉它）
2. 自動登入 OMAKASE
3. 依序打開五家餐廳的頁面，各停留幾秒讀「予約ルール詳細」那塊
4. 全部跑完視窗自己關閉

**如果自動登入失敗**，視窗會停在登入畫面，命令列出現：

```
自動登入失敗 / login failed: ...
請在打開的視窗裡自己登入 OMAKASE，完成後按 Enter…
```

這時**自己在那個視窗裡登入**（有「我不是機器人」順手點掉），弄好回到命令列按 **Enter**，
它會繼續跑。登入狀態會存起來，下次不用再來一遍。

跑完長這樣就對了：

```
✓ とり茶太郎  枠なし  次回 2026-08-01T08:00:00+09:00
✓ 酉囃子      枠なし  次回 2026-08-01T15:00:00+09:00
✓ 明寂        予約可  次回 2026-08-01T23:00:00+09:00
✓ 蒼          予約可  次回 未定
✓ スペイン料理 acá  枠なし  次回 2026-08-01T13:00:00+09:00  抽選応募締切 ...

polled 5 ok, 0 failed → ..\data\booking-state.json
```

> **如果每家都是 `次回 —`，或全部是 `✗`**，那就是「文字要從哪個元素抓」沒對上
> —— 這是整個專案最後一塊還沒對真實頁面驗證過的部分。這時候改跑這支，它會把整頁
> 原封不動存下來，我照真實內容修：
>
> ```powershell
> node dump-omakase.mjs
> ```
>
> 結果在 `dump\` 資料夾，每家店有 `.txt`、`.calendar.html` 和整頁 `.png`。

---

## 7. 把結果給我

跑完之後，結果在 **`data\booking-state.json`**（`scraper` 的上一層，也就是
`ledger\data\` 裡面）。

用記事本打開，或直接在 PowerShell 裡看：

```powershell
type ..\data\booking-state.json
```

**把那個內容貼給我**，我核對讀到的東西跟你之前給我的截圖是否一致 —— 一致就表示
DOM 抓取那段是對的，整條線就完全通了。

> 如果是跑了 `dump-omakase.mjs`，結果會在 `scraper\dump\`。
> **那裡面的 `.png` 是你登入後的畫面**，會有你的帳號名稱、也可能有你已經訂到的位子 ——
> 傳給我之前自己先看一眼。其實貼 `.txt` 的文字就夠我修了。

---

## 出錯的時候

| 畫面上寫 | 意思 | 怎麼辦 |
| --- | --- | --- |
| `npm : 無法辨識...` | Node 沒裝好，或視窗是裝之前開的 | 關掉 PowerShell 重開一個再試；還是不行就改開沒有 `(x86)` 的那個 PowerShell |
| `npm.ps1 cannot be loaded because running scripts is disabled` | PowerShell 擋腳本 | 用 `npm.cmd install` / `npx.cmd ...`，見第 4 步的說明 |
| `Cannot find module ...poll-omakase.mjs` | zip 是舊版，缺這支程式 | 重新下載 zip，見第 3 步的說明 |
| `Cannot find module` 其他模組名 | 漏了 `npm.cmd install` | 確認 `Test-Path poll-omakase.mjs` 是 `True`，再重跑第 4 步 |
| `missing env: OMAKASE_EMAIL` | `.env` 沒建好或存錯地方 | 重做第 5 步，確認記事本標題列是 `.env` 不是 `.env.txt` |
| `login rejected` | 帳密打錯 | 檢查 `.env`；或用第 6 步的手動登入 |
| 跳出「我不是機器人」 | Cloudflare 驗證 | 自己在視窗裡點掉，回命令列按 Enter |

指令跑不動就把**整個視窗的文字複製給我**，我看得出是哪裡卡住。

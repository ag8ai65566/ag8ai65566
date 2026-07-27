# 東京 予約台帳

東京餐廳的收藏、評分與訂位規劃系統。

- **去過的**：評分、感想、照片、花費、地址
- **想去的**：分類、優先度、訂位平台
- **訂位雷達**：依每家店的開放規則回推「最早該在什麼時候搶訂」，並在開放前提醒
- **行程表**：把餐廳排進旅行的每一餐，匯出成 Google My Maps 能匯入的 CSV
- **匯入**：貼 Tabelog 網址，自動抓店名、分類、地址、車站、預算、訂位規則

## 現在的進度

| 階段 | 狀態 |
| --- | --- |
| 視覺原型（單檔 Artifact） | ✅ 完成 — `prototype/ledger.html` |
| Tabelog 匯入（店家資料） | ✅ 完成，已對真實頁面驗證 |
| Tabelog 空席快照（每日累積） | ✅ 完成 — 首跑 15 家 × 66 天 = 925 筆 |
| OMAKASE／TableCheck／TableAll 空席 | 待做 — 網站進得去，但要登入後才看得到日曆 |
| 雲端儲存（Supabase）與照片上傳 | 待做 |
| 手機推播提醒（Claude 排程） | 待做 |

原型的資料存在瀏覽器 `localStorage`，只在你自己的裝置上。原型裡的範例餐廳**店名是
虛構的**，只用來確認版面；真實資料由 Tabelog 匯入，寫進 `data/`（gitignore，不進版控）。

匯入與快照都已經對真實頁面跑過。目前 `data/` 裡的 15 家是**驗證用的樣本**，從 Tabelog
的分類列表隨手取的，不是你的清單——把你要追的 Tabelog 網址丟進 `npm run import` 就會
換成你的。

## 訂位開放規則模型

日本餐廳的訂位開放方式大致四種，`RULES` 物件各實作一種 `opensAt(rule, diningDate)`：

| 規則 | 例 | 想在 2027/01/06 用餐 → 開放時刻 |
| --- | --- | --- |
| `monthlyFirst` | 毎月 1 日 10:00 に翌月分 | 2026/12/01 10:00 |
| `monthsBefore` | 3ヶ月前の同日 | 2026/10/06 |
| `daysBefore` | 30 日前より | 2026/12/07 |
| `unknown` | 需登入或去電確認 | — |

一律以日本時間計算。

### Tabelog 的 予約 欄其實不寫開放規則

實測 15 家：**沒有一家**的「予約可否」欄寫得出開放規則，內容清一色是「予約可」「完全
予約制」這種。所以 `rule` 目前全部是 `unknown`——這是正確行為，不是壞掉：猜錯規則會
害你在錯的日子去搶，比不猜更糟。開放規則要從店家自己的訂位頁或社群公告來，之後接
OMAKASE／TableCheck 時再補。

## 抓取

```bash
cd scraper && npm i
npm test                                    # 不需要網路的部分（規則判讀、統計）
npm run import -- https://tabelog.com/tokyo/A1303/A130301/13157208/
npm run snapshot                            # 每天跑一次，累積空席歷史
```

`import` 從 schema.org JSON-LD 讀店名、評分、電話、地址、經緯度，其餘欄位（ジャンル、
交通手段、営業時間、席数、予算）從 `rstinfo-table` 讀。營業時間那格同時藏著定休日，
而且有三種寫法（日別時段／定休日列／店家自己打的 ■ 標題自由文字），三種都處理了。

`snapshot` 打的是店頁訂位小工具自己的 JSON 端點 `/booking/calendar/initial_vacancy`，
一次拿到約 66 天的日別狀態。`available` 代碼對照：

| 代碼 | 意義 | 記成 |
| --- | --- | --- |
| `2` | 空席あり | `true` |
| `0` | 満席／受付不可 | `false` |
| `1` | 未確認（疑似殘席わずか） | `null` |
| `3` | 定休日・休業 | 整天略過 |
| `4` | 當日／隔日，線上受付已截止 | 整天略過 |

`3` 和 `4` 不寫進歷史是有意的：**店沒開不等於賣完**，把公休日記成賣完會低估這家店的
座位實際撐多久。`1` 記成 `null`（不是 `false`）也是同樣的道理，而且每筆都留著原始
`code`，之後查清楚了可以直接重新解讀，不用重抓。

## 開發

```bash
cd prototype
npm i @fontsource/instrument-serif @fontsource/ibm-plex-sans @fontsource/ibm-plex-mono
python3 build.py     # 把字型內嵌進 src/app.html → ledger.html
```

`src/app.html` 是原始碼，`ledger.html` 是內嵌字型後的產物（Artifact 的 CSP 擋掉所有
外部資源，字型必須以 data URI 隨檔案一起走）。

## 設計

- 版面取自日本餐廳的**予約台帳**與**時刻表**：細分隔線、等寬數字、資訊密度高，不用圓角卡片
- 色彩取自**染付**（藍白瓷）：靛藍為主色，中性色帶藍調；語意色（可訂／即將開放／逾期）獨立於主色
- 字體：Instrument Serif（店名與標題）／IBM Plex Sans（介面）／IBM Plex Mono（日期、倒數、評分）
- 深淺色主題各自調校，非直接反轉

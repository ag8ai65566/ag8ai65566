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
| 即時抓取 Tabelog／OMAKASE／TableAll | ⛔ 被環境網路政策擋住，見 [docs/network-setup.md](docs/network-setup.md) |
| 雲端儲存（Supabase）與照片上傳 | 待做 |
| 手機推播提醒（Claude 排程） | 待做 |

原型的資料存在瀏覽器 `localStorage`，只在你自己的裝置上。範例餐廳的**店名是虛構的**，
只用來確認版面與流程；真實資料會在網路開通後由 Tabelog 匯入覆蓋。

## 訂位開放規則模型

日本餐廳的訂位開放方式大致四種，`RULES` 物件各實作一種 `opensAt(rule, diningDate)`：

| 規則 | 例 | 想在 2027/01/06 用餐 → 開放時刻 |
| --- | --- | --- |
| `monthlyFirst` | 毎月 1 日 10:00 に翌月分 | 2026/12/01 10:00 |
| `monthsBefore` | 3ヶ月前の同日 | 2026/10/06 |
| `daysBefore` | 30 日前より | 2026/12/07 |
| `unknown` | 需登入或去電確認 | — |

一律以日本時間計算。

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

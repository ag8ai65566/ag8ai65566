# RA 批次上傳工具

把 manager 每週寄來的 AUTOZONE MX 出貨報表,整理成 RA (KSMART) Client Container
Status 頁面「Upload Excel」所需要的批次上傳檔。

**直接用這個檔案:[`dist/RA-Batch-Upload.html`](dist/RA-Batch-Upload.html)**

下載後雙擊用瀏覽器打開就能用。不用安裝任何東西,不需要網路,Excel 檔完全不會離開
你的電腦 — 所有處理都在瀏覽器裡完成。

---

## 怎麼用

1. 打開 `RA-Batch-Upload.html`
2. 把當週的 Excel 拖進去
3. 看一下「日期檢查」的結果(見下)
4. 勾選要上傳的 milestone
5. 檢查預覽,特別是標紅色的列
6. 按匯出,把產生的檔案拿去 RA 上傳

RA 那邊的步驟不變:Client Container Status → Upload Excel → Excel 格式選
`MBL#` → 選檔 → Upload → 確認沒有錯誤訊息 → Save。

## 支援的 milestone

| Milestone | Event code | 來源欄位 |
| --- | --- | --- |
| Port ETA | `X2` | ETA POD |
| Port ATA | `VA` | ATA POD |
| Empty Return | `RD` | EMPTY RETURN DATE(時間取自 EMPTY RETURN TIME) |
| Last Free Day | `LF` | LAST FREE DAY OF DETENTION |

## 輸出格式

六欄,固定順序,**沒有標題列**,沒有空白列:

| A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- |
| Container # | MBL | Event | Date | Time | Update By |
| TGHU5237965 | HDMUCANM25646300 | X2 | 7/5/2026 | 0:00:00 | C |

- `Update By` 固定是 `C`(update by CNTR)
- `Time` 除了 Empty Return 會帶實際時間外,其餘都是 `0:00:00`
- 所有儲存格都以**文字**寫入,避免日期又被任何地區設定重新解讀
- 自動略過沒有櫃號、沒有 MBL、或該 milestone 沒有日期的列;櫃號是 `TBA` 的也會略過

---

## 日期檢查在做什麼

來源報表目前有一個問題:**部分日期的日與月被對調了**。

原因是報表在匯出時被 dd/mm/yyyy 語系(西班牙文/墨西哥)的 Excel 讀過一次。
`7/8/2026`(7月8日)會被讀成 8 月 7 日;而 `6/15/2026` 因為沒有第 15 個月,
解析失敗,反而原樣保留成文字。所以同一個檔案裡會有兩種日期混在一起 —— 而且
**壞掉的那些看起來完全正常**。

工具每次載入檔案都會自動做這個判斷,依據是一個很明確的統計特徵:

- 存成真日期格式的儲存格,**沒有任何一個**日期超過 12 號
- 存成文字的儲存格,**每一個**日期都超過 12 號

正常的日期資料裡,大約 60% 會落在 13 號之後。這種零例外的切割只可能來自
dd/mm 誤判。

判斷結果有三種:

| 判斷 | 自動修正 | 意思 |
| --- | --- | --- |
| 偵測到日/月對調 | **自動開啟** | 出現上述特徵,會把日月還原,每筆修正都在預覽中標黃 |
| 部分可疑 | 關閉 | 大多數日期偏小但有例外,無法判斷哪些該改,需人工確認 |
| 看起來正常 | 關閉 | 沒有這個特徵。**如果哪天來源修好了,工具會自動不做修正** |

修正邏輯經過三份不同週次的實際檔案驗證,並用「卸櫃日 + 免費天數 = 最後免費日」
這個獨立條件交叉檢查:修正前只有 36% 的 LFD 對得上,修正後是 93%。

> 這是繞過問題,不是解決問題。來源報表本身還是錯的,其他部門拿到的也還是錯的。
> 根本的修法在匯出端 —— 產生報表那台機器的地區日期格式要設成 mm/dd/yyyy,
> 或是把日期欄位直接以文字寫出。

## MBL 船公司前綴

RA 裡有些 MBL 會前綴船公司代碼(`NGB600492000` 在 RA 是 `PABVNGB600492000`)。
沒有前綴就上傳會得到 `Container No. does not exist` 錯誤。

工具的判斷方式:**只有當 MBL 開頭不是檔案裡出現過的任何一個船公司代碼時**,
才會標記。這樣 `OOCL` 配 `OOLU…` 這種同一家船公司的正常寫法不會被誤判。

預設開啟,可以整個關掉,展開清單也能看到每一筆會怎麼改。

## 會被標記的其他狀況

預覽裡標紅色的列代表有疑慮,建議上傳前看一下:

- LFD 與「卸櫃日 + 免費天數」相差超過 3 天
- 還櫃日早於卸櫃日
- ETA 晚於已記錄的 ATA
- 同一個櫃號在同一個 event 出現兩次
- 存成日期格式、但日月無法對調(日期大於 12,理論上不該出現)

這些**不會**阻擋匯出,只是提醒。

---

## 開發

```
src/index.html   版面與樣式
src/core.js      欄位辨識、儲存格解讀、日期診斷、前綴判斷
src/build.js     把來源列轉成上傳記錄、交叉檢查
src/app.js       介面邏輯
src/test.cjs     單元測試(對三份真實檔案驗證)
vendor/          SheetJS 0.18.5
build.py         把上面全部內嵌成 dist/ 裡的單一 HTML
```

改完之後要重新 build:

```bash
python3 build.py
```

跑測試(需要三份真實 Excel 放在 `FIXTURES` 指到的目錄):

```bash
FIXTURES=/path/to/xlsx-files node src/test.cjs
```

測試涵蓋:欄位辨識、日期診斷的實際數字、五個已知櫃號的修正結果、四種
milestone 的筆數、MBL 前綴判斷、輸出格式,以及「乾淨的檔案不可以被修正」。
時區無關性也有測 —— UTC / Asia/Taipei / America/Los_Angeles 等都跑過。

### 一個要注意的坑

HTML 元素的 `id` 會變成 `window` 上的全域變數。如果某個 `id` 剛好叫
`exports`、`module`、`define` 之類,SheetJS 的 UMD 包裝會誤判環境,把整個
函式庫掛到那個 DOM 節點上而不是 `window.XLSX`,而且**不會報任何錯**。
`build.py` 有擋這件事,加新元素時如果撞名會直接 build 失敗。

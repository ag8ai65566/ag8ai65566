# 音檔核對工具（audio check）

用直播存檔的**實際音訊**核對角色卡上的口頭禪、語速與音高。2026-09-30 起用於 holoen 專案。

## 為什麼不用 YouTube

雲端容器被 YouTube 擋（429／要求登入、PO token）。我們**不破解**它的防機器人機制，改用公開的第三方
直播存檔站 [archive.ragtag.moe](https://archive.ragtag.moe)（hololive 直播存檔），只擷取需要的時間段。
2026 年的部分直播沒有存檔；2020–2025 的大多有。

## 流程

1. `acheck.py <jobs.json> [threads]`：對每個 `[角色, 影片ID, 開始秒數(負數=從結尾倒數), 長度秒數, 標籤]`
   - 用 ragtag API 找檔案（優先純音訊 f251/f140，否則影音檔），ffmpeg 透過代理只擷取該段 → 16 kHz 單聲道 wav；
   - faster-whisper `small.en`（int8、CPU、VAD、逐字時間戳）轉寫；
   - 存成 `trans/<角色>_<影片ID>_<標籤>.json`（逐字稿**只留在本機 scratchpad，不進 repo**）。
2. `repitch.py`：用 Praat（parselmouth）在「whisper 標出正在說字」的時段量音高，女聲設定
   pitch floor 100 Hz、ceiling 600 Hz（75 Hz 會把背景音樂的低頻誤當成聲音）。輸出中位數、p10–p90 與半音範圍。
3. `analyze.py <角色> [每項顯示幾句]`：搜尋該角色的口頭禪與粗口，算每小時次數，列出附時間戳連結的原句。

安裝：`pip install faster-whisper praat-parselmouth numpy imageio-ffmpeg`（模型第一次會從 Hugging Face 下載）。

## 限制（寫進檔案時要一起寫）

- 轉寫是機器轉寫（whisper），我們有對照上下文判讀，但沒有逐句人工聽寫。
- 尖叫、笑聲、「Guh」「GWAK」這類非語言聲音 whisper 通常不會寫出來 → 這類只能記「該時間點有反應」。
- 遊戲音效、背景音樂、合作對象的聲音會混進去；音高是**近似值**，適合做成員之間的相對比較，不是聲學鑑定。
- 讀 superchat 時念出的是觀眾的字，不是本人口癖（例如念到觀眾寫的粗口）→ 判讀時要排除。
- 引用只取短句，不放長篇逐字稿、不抄歌詞。

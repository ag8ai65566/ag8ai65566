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
4. `table.py <角色>`：輸出報告用的「Windows measured」表格。
5. `confirm.py <quotes.json> [threads]`：**第二模型核對**。對每個 `[角色, 影片ID, 秒數, 引句]`，先用第一個模型
   的逐字時間戳找到引句位置，剪出涵蓋該句的片段（約 24–60 秒），用較大的 `medium.en` 重新轉寫，並記錄字詞重疊率。
   結果存成 `<quotes>.out.json`。
6. `secondmodel.py <角色…>`：把核對結果整理成報告結尾的「Second-model check」表格；`verdicts.json` 放人工判讀
   （重疊率會誤導的情況，例如拼法不同或只對一半）。

**上卡片的台詞必須兩個模型都同意**；只有第一個模型寫出來的句子只能留在檔案裡並標明。

安裝：`pip install faster-whisper praat-parselmouth numpy imageio-ffmpeg`（模型第一次會從 Hugging Face 下載）。

## 限制（寫進檔案時要一起寫）

- 轉寫是機器轉寫（whisper），我們有對照上下文判讀，但沒有逐句人工聽寫。
- 尖叫、笑聲、「Guh」「GWAK」這類非語言聲音 whisper 通常不會寫出來 → 這類只能記「該時間點有反應」。
- 遊戲音效、背景音樂、合作對象的聲音會混進去；音高是**近似值**，適合做成員之間的相對比較，不是聲學鑑定。
- 讀 superchat 時念出的是觀眾的字，不是本人口癖（例如念到觀眾寫的粗口）→ 判讀時要排除。
- 引用只取短句，不放長篇逐字稿、不抄歌詞。
- `small.en` 是純英文模型：遇到**日語**或遊戲音樂段落，可能「翻譯」或憑空寫出英文句子。2026-09-30 的實例：
  Kiara 一整串 "It's so cute!" 在第二模型下全部對不上（其中一處第二模型聽到的是日語），該發現已撤回。
  → 第一個模型的**次數統計只是參考**；單句要用第二模型核對後才可上卡片。
- 第二模型也是機器轉寫。兩個模型一致 ≠ 人耳聽過；檔案中一律寫 [ASR]，不寫 verified by listening。

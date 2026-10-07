# 1. 安裝與啟動

## 你需要什麼

| 項目 | 說明 |
|---|---|
| Windows 10 或 11（64 位元） | 平台本身也能在 Linux 跑，但安裝腳本是給 Windows 用的。 |
| NVIDIA 顯示卡 | 處理錄音（語音辨識）和本機合成語音用。VoxCPM2 合成約需 **8 GB** 顯示記憶體：10 GB（例如 RTX 3080）以上就可以，12 GB 以上最寬裕。 |
| 最新的 NVIDIA 驅動 | 到 nvidia.com/drivers 下載 Game Ready 或 Studio 驅動。 |
| 硬碟空間 | 程式約 10 GB，加上每個引擎 5–8 GB，再加上你的錄音。 |
| RunPod 帳號 | 雲端訓練用，詳見〈雲端訓練〉。 |

訓練不在你的電腦上做，所以顯示卡不用很強；它只負責整理資料和最後的合成。

### 顯示卡 10 GB（例如 RTX 3080 10GB）

- VoxCPM2 合成約用 8 GB，放得下，但剩下的不多：合成時請關掉遊戲、OBS、影片剪輯軟體，以及瀏覽器的「硬體加速」大量分頁。
- 合成後的「檢查漏字」會自動改用 CPU 執行（每句多幾秒），不跟語音模型搶顯示記憶體。
- 處理錄音時平台會先把語音模型移出顯示卡，處理完再載入，不用手動操作。
- 遇到「CUDA out of memory」：按文字轉語音頁右上角「釋放顯示卡」，關掉其他程式後再試。
- Qwen3-TTS 合成約用 6 GB，也沒問題。

## 下載

1. 下載程式（ZIP，約 14 MB）：
   https://github.com/ag8ai65566/ag8ai65566/archive/refs/heads/claude/sudowrite-novel-framework-2cmja7.zip
   （也可以到 https://github.com/ag8ai65566/ag8ai65566 ，左上角切換到 `claude/sudowrite-novel-framework-2cmja7` 分支，按綠色的「Code」→「Download ZIP」。）
2. **解壓縮之前**：在 ZIP 檔上按右鍵 →「內容」→ 最下面勾選「解除封鎖」→ 確定。這樣之後執行 `.bat` 時，Windows 比較不會擋。
3. 解壓縮後打開 `ag8ai65566-claude-sudowrite-novel-framework-2cmja7` 資料夾，裡面的 **`voice-studio`** 資料夾就是平台本體，`install.bat` 在它裡面。其他資料夾（小說設定等）和平台無關，可以不理。

## 安裝

1. 把 `voice-studio` 資料夾搬到一個**路徑沒有中文、空白或特殊符號**的位置，例如 `D:\voice-studio`。
2. 雙擊 **`install.bat`**（如果出現藍色的「Windows 已保護您的電腦」，按「其他資訊」→「仍要執行」）。它會：
   - 安裝 Python 管理工具 uv 和 Python 3.11（不影響你電腦上其他的 Python）；
   - 安裝 GPU 版 PyTorch（約 3 GB）；
   - 安裝 Voice Studio 和語音辨識；
   - 在桌面建立「Voice Studio」捷徑。
3. 看到「安裝完成」就好了。

第一次處理錄音時，平台會再自動下載語音辨識模型（Whisper large-v3 和 large-v3-turbo，約 4.5 GB）、語音偵測模型和說話者辨識模型。

## 啟動

雙擊桌面上的 **Voice Studio**（或資料夾裡的 `start.bat`）。瀏覽器會自動打開 `http://127.0.0.1:7860`。

- 要關閉時，關掉那個黑色視窗就好。
- **雲端訓練不會因為關掉而中斷**：雲端機器會繼續跑，下次開啟 Voice Studio 時會自動接上、下載結果。

## 安裝本機合成引擎

訓練好的模型要在你的電腦上說話，需要安裝對應的引擎：

1. 打開 **設定 → 引擎**。
2. 在 **VoxCPM2** 旁邊按「安裝」（約 5–8 GB，含模型權重，10–20 分鐘）。
3. 要用 Qwen3-TTS 的模型時，再安裝 Qwen3-TTS。

安裝在背景進行，可以先去做別的事；進度在右上角和「工作佇列」。

## 更新

雙擊 `update.bat`。你的錄音、模型和設定都在 `data` 資料夾裡，更新不會動到它們。

## 你的資料在哪裡

全部在 `voice-studio\data`：

| 資料夾 | 內容 |
|---|---|
| `sources` | 上傳的錄音複本（用「匯入資料夾」匯入的檔案不會複製，留在原位） |
| `segments` | 切好的句子 |
| `datasets` | 每次建立的訓練資料集（快照） |
| `models` | 下載回來的模型、檢查點樣本、參考片段 |
| `outputs` | 合成的語音 |
| `studio.db` | 資料庫（聲音、同意紀錄、片段文字……） |
| `hf` | 下載的基礎模型 |

**備份**：關掉 Voice Studio 後，把整個 `data` 資料夾複製到別的硬碟即可。

API 金鑰不在 `data` 裡，而是在 Windows 的「認證管理員」（控制台 → 使用者帳戶 → 認證管理員 → Windows 認證，名稱是 `voice-studio`）。

## 從手機或另一台電腦打開（選用）

預設只有這台電腦能打開，而且平台會拒絕其他網站的網頁偷偷呼叫它。若要讓同一個網路的其他裝置連進來：

1. 在 `start.bat` 裡 `python.exe` 那一行前面加上兩行：
   ```
   set VSTUDIO_HOST=0.0.0.0
   set VSTUDIO_PASSWORD=換成一個長密碼
   ```
2. 其他裝置打開 `http://這台電腦的IP:7860`，第一次會跳出密碼視窗。開了網路模式後，連這台電腦自己也要輸入密碼。

連線是一般的 http，密碼在區網裡沒有加密。只在自己家裡的網路用，不要把 7860 埠開放到網際網路上。

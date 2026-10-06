# Voice Studio

個人用的聲音訓練與語音合成平台：把大量錄音丟進去，自動整理成訓練資料，租雲端 GPU 微調最新的開放語音模型，再在自己的電腦上用訓練好的聲音做文字轉語音和整場劇本配音。

**只用於有同意的聲音**：你自己、簽了同意書的人、原創設計聲音。沒有完整同意紀錄的聲音，平台不會讓它進入訓練或合成。

## 功能

- **匯入**：拖進長影片／錄音或整個資料夾；自動抽音訊、偵測語音（Silero VAD）、在停頓處切成 2–15 秒、辨認說話者（WeSpeaker 聲紋）、用 Whisper large-v3 與 large-v3-turbo 雙重轉寫並比對、打品質分數；可選 BS-RoFormer 去背景音樂。
- **檢查**：鍵盤操作的審核介面，批次核可、篩選警告、修文字；資料集是版本化快照，記錄當時的同意內容。
- **雲端訓練（RunPod）**：一鍵上傳、開機、安裝固定版本的官方訓練程式、訓練、每個檢查點試念同一批未見過的句子、打包下載、自動關機；三重保險避免忘記關機；關掉平台也能在下次開啟時接回。費用依實測速度校正。
- **引擎**：VoxCPM2（主力：LoRA／完整微調，最高相似度）與 Qwen3-TTS 1.7B（對照：最低錯字率），皆 Apache-2.0。
- **模型比較**：自動用聲紋相似度＋語音辨識念對程度評分各檢查點並推薦；逐句和本人錄音並排試聽。
- **文字轉語音**：只用模型／參考音色／完整複製（參考音＋逐字稿接續，最能保留口音與節奏）；風格提示；一次多個版本自動挑最好的；WAV／MP3；輸出標記為 AI 合成。
- **劇本配音**：novel-lab 場景格式，每個角色指定模型，整場合成並附逐句清單；可匯入 novel-lab 角色表演單作為「怎麼演」的預設。
- **介面**：繁體中文、深色模式、內建圖文教學（`docs/`）。

## 安裝（Windows + NVIDIA）

1. 安裝最新 NVIDIA 驅動。
2. 雙擊 `install.bat`。
3. 雙擊桌面「Voice Studio」或 `start.bat`，瀏覽器會打開 http://127.0.0.1:7860 。
4. 設定 → 引擎 → 安裝 VoxCPM2（本機合成用）。
5. 設定 → 雲端 GPU：填 RunPod 金鑰（存在 Windows 認證管理員）。

詳細步驟見 `docs/01-install.md`，或啟動後的「教學」頁。

## 開發

```bash
uv venv --python 3.11 && uv pip install -e ".[prep,dev]"
python -m vstudio.server          # API + 已建置的介面，port 7860
cd web && npm install && npm run dev   # 介面開發（proxy 到 7860）
VSTUDIO_TEST_WAV=speech.wav pytest  # 後端端對端測試（含模擬雲端機器的完整來回）；需要一段約 10 秒的真人語音
```

結構：

| 路徑 | 內容 |
|---|---|
| `vstudio/pipeline/` | 匯入處理：VAD、說話者、ASR、人聲分離 |
| `vstudio/datasets.py` | 同意檢查、資料集快照、以錄音為單位切驗證集 |
| `vstudio/engines/` | 引擎轉接層；`remote/` 是在雲端 GPU 上執行的訓練腳本 |
| `vstudio/training.py` | RunPod 訓練流程、模型註冊、零樣本模型、參考片段 |
| `vstudio/evaluate.py` | 檢查點評分 |
| `vstudio/tts.py` | 合成、多版本篩選、劇本 |
| `vstudio/cloud/` | RunPod REST／S3 與開機腳本 |
| `web/` | React 介面（`web/dist` 已建置並納入版本控制，使用者不需要 Node.js） |
| `docs/` | 教學 |

## 授權與致謝

- VoxCPM2（OpenBMB）、Qwen3-TTS（Alibaba Qwen）：Apache-2.0
- faster-whisper、OpenAI Whisper、Silero VAD、python-audio-separator：MIT
- WeSpeaker ResNet34-LM 說話者模型：CC BY 4.0，© WeSpeaker 團隊（https://github.com/wenet-e2e/wespeaker）

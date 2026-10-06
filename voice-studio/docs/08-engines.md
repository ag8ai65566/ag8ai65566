# 8. 為什麼選這些引擎

2026 年 10 月，Claude 和 GPT 分別獨立調查了可以**自己訓練**、支援**日文＋英文**的開放模型，再對照彼此的結果。結論：

| | 引擎 | 理由 |
|---|---|---|
| 主力 | **VoxCPM2**（OpenBMB，2026-04） | 程式與權重都是 Apache-2.0；官方提供 LoRA 和完整微調；30 種語言含日英；在同一份多語評測中音色相似度最高；有「完整複製」模式；本機合成約 8 GB 顯示記憶體 |
| 對照 | **Qwen3-TTS-12Hz-1.7B-Base**（阿里巴巴 Qwen，2026-01） | Apache-2.0；官方單一說話者微調；同一評測中念錯字最少 |

## 公開評測（零樣本，越像越好／錯越少越好）

MiniMax 多語評測，數字取自 VoxCPM2 技術報告表 6–7（作者自己報的數字，不是平台實測）：

| 模型 | 日文 WER ↓ | 日文相似度 ↑ | 英文 WER ↓ | 英文相似度 ↑ |
|---|---:|---:|---:|---:|
| Qwen3-TTS | 3.82% | 78.8 | **0.93%** | 77.5 |
| Fish Audio S2 | **2.76%** | 79.6 | 1.62% | 79.7 |
| VoxCPM2 | 4.63% | **82.8** | 2.29% | **85.4** |

這是「相似度 vs. 念對程度」的取捨，沒有全勝的模型。而且這些都是**沒有訓練**的結果；用你的大量錄音微調之後誰最好，目前沒有公開的對照實驗——所以平台讓你**用同一份資料集訓練不同引擎，在模型頁直接比較**。

## 有考慮但沒有選為預設的

| 模型 | 原因 |
|---|---|
| Fish Audio S2 Pro | 品質很好、支援行內情緒標籤，但程式和權重都是 Fish Audio Research License（商業用途受限），官方也警告微調 RL 訓練過的模型可能變差 |
| dots.tts（2026-06） | Apache-2.0、日文相似度在作者評測中很高（83.7），有官方微調；但很新、日文錯字率較高（約 5.2%），平台之後可以加入 |
| CosyVoice 3 | Apache-2.0、有訓練流程；中文最強，日英證據較少 |
| GPT-SoVITS v2ProPlus | MIT、日文社群成熟、有整合介面；新一代多語模型的相似度與穩定性較好 |
| IndexTTS 2.5 | 8 月新增日文，情緒控制好；官方訓練流程未確認、授權為自訂條款 |
| MOSS-TTS、Higgs TTS 3、Sarashina2.2-TTS、OmniVoice、F5-TTS、Spark-TTS、Llasa | 授權限制（非商業）、缺日文、或沒有完整的訓練流程 |
| Qwen-Audio-3.0-TTS、Fish S2.1 Pro | 只有雲端 API，沒有可下載的權重 |

## 版本固定

為了讓每次訓練可以重現，平台固定使用：

- VoxCPM：commit `f0c787f`（2026-09-30，2.0.3 之後），映像檔 `runpod/pytorch:2.8.0-py3.11-cuda12.8.1`
- Qwen3-TTS：commit `022e286`（2026-03-17，套件 0.1.1）
- 基礎模型的權重：每次訓練都記下 Hugging Face 上確切的版本（commit），本機載入 LoRA 時用同一版，不會套到更新過的權重上。

## 引擎的細節（GPT 程式碼審查後確認）

- **Qwen3-TTS 的參考錄音必須是 24 kHz**：官方訓練程式會檢查，平台上傳前自動轉好。
- **Qwen3-TTS 訓練時其實不使用語言標籤**（官方程式讀了但沒用），所以訓練好的模型合成時固定用「自動判斷語言」，和訓練時一致。
- **VoxCPM2 官方訓練程式最後會存兩份一模一樣的檢查點**，平台會去掉重複的，比較時才不會被誤導。
- **訓練步數**由「epoch 數」直接換算，預估和實際送出的參數是同一份；資料少到不夠做一次更新時，會直接告訴你，不會偷偷多跑好幾輪。

## 來源

- VoxCPM：github.com/OpenBMB/VoxCPM、huggingface.co/openbmb/VoxCPM2、voxcpm.readthedocs.io（微調指南）、arXiv 2606.06928
- Qwen3-TTS：github.com/QwenLM/Qwen3-TTS（finetuning/）、huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base、arXiv 2601.15621
- Fish Audio S2：github.com/fishaudio/fish-speech（LICENSE、微調文件）、arXiv 2603.08823
- dots.tts：huggingface.co/dots-studio/dots.tts-soar
- RunPod 價格：runpod.io/pricing（2026-09-27 更新）

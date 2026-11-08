# 17. 檢查標準（完整規格）

平台在每一關怎麼判斷一段聲音能不能用：用了哪些程式、量什麼、門檻多少。數字都直接取自程式碼（表格裡寫了檔案），改程式時這一頁要一起改。

> **給另一個 AI 的說明**（整頁可以直接貼給它）
>
> 你要判斷的音檔，之後會進 Voice Studio 這個語音訓練平台，依序經過下面七關。每一關的程式、量法和門檻都列在下面，最後的「附錄：門檻清單（JSON）」是同一組數字的機器可讀版本，可以直接拿來寫程式重現判斷。
>
> - 所有「比人聲小 X dB」都是跟「說話時每 20 毫秒音量的第 90 百分位」比。
> - dBFS 是相對於數位滿刻度（1.0）的音量。
> - 一個檔案在「檢查音檔」的結果取最差的一項：任何一項不通過就是「不通過」；沒有不通過、但有一項「勉強可用」就是「勉強可用」；「無法判斷」的項目不影響結果。所以要讓檔案變成「通過」，**每一項都要通過（或無法判斷）**。
> - 「勉強可用」的檔案不會自動匯入（要另外勾選），匯入後每一句還會被第三、四關再判一次。

| 關卡 | 什麼時候 | 判斷什麼 | 程式 |
|---|---|---|---|
| 一、檢查音檔 | 匯入前（「檢查音檔」頁） | 整個檔案的音質：通過／勉強可用／不通過 | `vstudio/audiocheck.py` |
| 二、匯入處理 | 匯入時 | 切句、認人、轉文字 | `vstudio/pipeline/`（vad、speaker、asr、separate、prepare） |
| 三、片段分數 | 匯入時 | 每一句 0–1 分和標記 | `vstudio/pipeline/prepare.py` 的 `score` |
| 四、自動審核 | 匯入後（「檢查資料」頁） | 每一句核可／排除／需要人聽 | `vstudio/pipeline/autoreview.py` |
| 五、交付資料夾匯入 | 「交付資料夾」頁 | 已切好的片段直接核可的條件 | `vstudio/delivery.py` |
| 六、原音片段 | 加入口頭禪或聲音標籤的原音時 | 單一短片段的音質 | `vstudio/phrases.py` 的 `check_clip` |
| 七、資料集與訓練 | 建立資料集、開始訓練前 | 收哪些句子、資料夠不夠 | `vstudio/datasets.py`、`vstudio/training.py` |

---

## 一、檢查音檔（匯入前）

### 怎麼量

1. **讀檔**：用 ffmpeg 解碼成單聲道、原取樣率（最高 48 kHz）。20 分鐘以內整個分析；更長的檔案平均取 20 段、每段 60 秒。
2. **找說話的地方**：Silero VAD（`silero_vad.onnx`，onnxruntime，輸入 16 kHz），切段規則同第二節。
3. **停頓**：說話段落之間（也包含開頭和結尾），離說話至少 0.2 秒的地方才算，這樣呼吸聲和句尾的尾音不會被算進去。
4. **人聲的基準**：說話時每 20 毫秒（每 10 毫秒移動一次）量一次音量，取第 90 百分位當「人聲的大聲端」（下面寫的「比人聲小 X dB」都是跟它比）。
5. **停頓的內容**：每半秒量一段，依序判斷它是哪一類：
   | 分類 | 條件 |
   |---|---|
   | 安靜 | 比人聲小 50 dB 以上 |
   | 別人說話 | 這半秒 VAD 平均機率 ≥ 0.35 |
   | 電源嗡嗡聲 | 50 或 60 Hz 的前 8 個諧波中，至少 3 個比周圍高 10 dB 以上，而且音量穩定（逐格標準差 < 3 dB） |
   | 音樂／音效 | 頻譜平坦度 < 0.05（有音高，100–8000 Hz） |
   | 突發聲（敲擊、喀噠、呼吸） | 逐格音量標準差 ≥ 4 dB |
   | 穩定雜音（風扇、沙沙聲） | 以上都不是 |

### 各項目和門檻

每一項是「通過／勉強可用（warn）／不通過（fail）」；**整個檔案的結果取最差的一項**（任何一項不通過 → 不通過；沒有不通過、但有任何一項勉強可用 → 勉強可用；「無法判斷」不算）。

| 項目 | 量法 | 通過 | 勉強可用 | 不通過 |
|---|---|---|---|---|
| 有沒有說話 | VAD 偵測到的說話秒數 | — | — | 不到 2 秒，或不到分析長度的 5%（其他項目不判斷） |
| 背景音（音樂、音效、別人說話） | 停頓中被分類成「音樂／音效」或「別人說話」、而且比人聲小不到 42 dB 的時間 | 沒有，或不到停頓時間的 2% | 停頓時間的 2% 以上 | 比人聲小不到 30 dB 的佔停頓時間 5% 以上，而且合計至少 2 秒 |
| 背景音：停頓太少 | 停頓合計不到 3 秒 | — | 一律勉強可用（無法確認，建議用深入檢查） | — |
| 雜音（底噪、風扇） | 人聲大聲端減去停頓音量的中位數（停頓不到 2 秒時用全段最安靜的第 10 百分位） | 25 dB 以上 | 18–25 dB | 不到 18 dB |
| 雜音：電源嗡嗡聲 | 嗡嗡聲的半秒段落合計 ≥ 1 秒、而且 ≥ 停頓的 20% | — | 比人聲小 30–40 dB | 比人聲小不到 30 dB |
| 回音 | 句尾後有 0.35 秒以上停頓的地方：在句尾前 0.35 秒內找音量最高點，量它從「最高點 −5 dB」再往下掉 20 dB（最高點比停頓底噪大 30 dB 以上時）或 15 dB（大 24–30 dB 時；不到 24 dB 不量）所花的時間，乘上 60 ÷ 20（或 60 ÷ 15）換算成下降 60 dB 的秒數，取中位數（至少要 3 個量得到的句尾） | 0.35 秒以下 | 0.35–0.6 秒 | 超過 0.6 秒 |
| 回音：量不到 | 量得到的句尾不到 3 個 | 無法判斷（不影響結果） | — | — |
| 破音（爆音） | 取樣點絕對值 ≥ 0.995，或檔案峰值 ≥ 0.25 時連續 3 個以上取樣點停在峰值的 99.9%（破音後又調小聲的情況），佔說話取樣數的比例 | 0.01% 以下 | 0.01%–0.1% | 超過 0.1% |
| 音量 | 說話時（大聲端往下 30 dB 以內的格子）音量的中位數 | −35 dBFS 以上 | −45 到 −35 dBFS | 低於 −45 dBFS |
| 音質（頻寬） | 說話時的平均頻譜，以 500 Hz 為一段，找「1.5 kHz 內掉 30 dB 以上、之後沒有回升」的斷崖；沒有斷崖、而且高頻底部離 300–3000 Hz 不到 60 dB 時算全頻 | 13 kHz 以上 | 7–13 kHz | 不到 7 kHz（電話音質） |
| 後製痕跡 | 停頓中音量低於 −90 dB（數位完全無聲）的比例；或說話段落裡 5 毫秒以上完全無聲、前後不夠大聲的次數 | 停頓有自然底噪 | 停頓 50% 以上完全無聲，或字和字之間完全無聲 ≥ 5 次且 ≥ 說話秒數 ÷ 12 | — |
| 斷訊 | 說話段落裡 5 毫秒以上完全無聲，而且前後 10 毫秒都在人聲大聲端往下 25 dB 以內 | 沒有 | 1–2 處 | 3 處以上 |
| 說話時底下的背景（勾「深入檢查」才有） | 用 BS-RoFormer 分離出人聲，原音減人聲＝背景；說話時（大聲端往下 30 dB 以內）背景比人聲小多少 dB 的中位數 | 小 30 dB 以上 | 小 20–30 dB | 小不到 20 dB |

這些門檻用合成的測試錄音校正過（乾淨人聲分別加上音樂、音效、白噪音、風扇聲、嗡嗡聲、不同房間大小的回音、破音、電話音質）。

### 「可以當 bgm 匯入」的條件

檢查結果標「可以去背景音樂後匯入」的條件（`quiet_bgm`）：有做深入檢查，「說話時底下的背景」是通過或勉強可用（背景比人聲小 20 dB 以上），而且除了「背景音」和這一項之外，沒有任何一項不通過。

### 匯入通過的

「匯入通過的」有兩種：
- 匯入通過的：只匯入結果為「通過」的檔案；勾「也匯入『勉強可用』的」才會加入勉強可用的。
- 匯入可以去背景音樂的：只匯入符合上面 `quiet_bgm` 條件的檔案，而且匯入時一定去背景音樂（BS-RoFormer）。

---

## 二、匯入處理

| 步驟 | 程式和設定 |
|---|---|
| 解碼 | ffmpeg → 48 kHz、單聲道、16-bit WAV（平台內部的母帶格式） |
| 去背景音樂（選用） | python-audio-separator，模型 `model_bs_roformer_ep_317_sdr_12.9755.ckpt`（BS-RoFormer），只留 Vocals |
| 找說話 | Silero VAD：機率門檻 0.5、說話至少 0.25 秒、靜音 0.3 秒以上才斷開、前後各留 0.08 秒 |
| 切句 | 間隔 0.6 秒以內的相鄰段落併起來，直到約 8 秒；超過 15 秒的在最安靜的地方切開（切出來每段至少 2 秒）。設定：`segment_min_s` 2、`segment_target_s` 8、`segment_max_s` 15 |
| 認人 | WeSpeaker ResNet34-LM 聲紋（`wespeaker_resnet34_LM.onnx`，VoxCeleb 訓練，16 kHz），和每個聲音的參考聲紋（登錄的參考片段平均）比餘弦相似度；≥ 0.62（設定 `speaker_match_threshold`）算是這個人。第二像的也 ≥ 0.62、而且兩者差不到 0.08 → 標「可能多人同時說話」 |
| 轉文字 | faster-whisper（GPU 用 float16、CPU 用 int8，beam size 5）：`large-v3` 和 `large-v3-turbo` 各轉一次（設定 `asr_primary`、`asr_secondary`）。一致度＝1 − 兩者的編輯距離 ÷ 較長的長度（日文、中文以字為單位，英文以詞為單位）。語言已知時，兩個模型都拿到同一段提示：保留語助詞（日文「えーと、あの、まあ、なんか、うーん、そうそう。」、英文「Um, uh, like, you know, I mean, yeah.」）加上這個聲音的口頭禪寫法，所以保留下來的語助詞和口頭禪不會被算成不一致 |
| 品質訊號 | 每句的峰值、破音比例（取樣絕對值 > 0.985 的比例）、粗估訊噪比（每 20 毫秒能量的第 90 ÷ 第 10 百分位） |

---

## 三、片段分數（每一句）

從 1 開始乘：

| 條件 | 分數 | 標記 |
|---|---|---|
| 兩個辨識結果一致度 a | × (0.4 + 0.6 × a) | a < 0.75 →「兩個辨識結果不一致」 |
| 訊噪比 < 15 dB | × 0.7 | 「雜音多」 |
| 破音比例 > 0.1% | × 0.6 | 「爆音」 |
| 認不出是誰 | × 0.5 | 「不確定是誰」 |
| 可能多人同時說話 | × 0.5 | 「可能多人同時說話」 |
| 沒有文字 | × 0.2 | 「沒有文字」 |

---

## 四、自動審核

每一句依下面的規則分成三堆：有任何「排除」條件 → 排除；沒有排除、但有任何「需要人聽」條件 → 需要你聽；都沒有 → 核可。**量不到的數值不算通過。**你手動決定或改過的句子不會被動到，整次審核可以復原。

### 一般（平衡／嚴格）

| 項目 | 需要人聽（平衡；括號是嚴格） | 排除 |
|---|---|---|
| 文字 | — | 沒有文字 |
| 長度 | — | 不在 1–30 秒 |
| 兩個辨識結果一致度 | 低於 0.88（0.95），或量不到 | 低於 0.5 |
| 訊噪比 | 低於 18 dB（22 dB），或量不到 | 低於 10 dB |
| 破音比例 | 超過 0.1% | 超過 1% |
| 聲紋相似度（對這個聲音的參考聲紋，重新量一次） | 低於 0.62（0.67），或量不到 | 低於 0.47 |
| 中途換人（每 2 秒一窗、每 1 秒移動，最不像的一窗比中位數低多少） | 超過 0.22（0.15） | 超過 0.4 |
| 辨識信心（平均 log 機率） | 低於 −0.8（−0.5） | — |
| 不是說話的機率 | 超過 0.5（0.3） | 超過 0.8 |
| 語速（日文、中文每秒字數；英文每秒詞數） | — | 日文、中文不在 1–14；英文不在 0.6–5.5 |

核可的句子會隨機抽一部分標「抽查」（最少 10 句、最多 100 句，約核可數的 2%）。抽查時你排除的超過 10%，頁面會建議改用嚴格重審。

### 已篩選過（給 AI 或人已經篩過的素材）

只檢查文字和明顯不能用的：

| 項目 | 需要人聽 | 排除 |
|---|---|---|
| 文字 | — | 沒有文字 |
| 長度 | — | 不在 1–30 秒 |
| 兩個辨識結果一致度 | 低於 0.85，或量不到 | 低於 0.5 |
| 訊噪比 | — | 低於 10 dB |
| 破音比例 | — | 超過 1% |
| 不是說話的機率 | — | 超過 0.8 |
| 語速 | — | 同上 |

---

## 五、交付資料夾匯入

已經切好的片段不重新切句、不重新轉文字（用 clips.csv 的逐字稿）。每段算一次品質訊號和片段分數（第三節，沒有一致度這一項），然後：

| 條件 | 結果 |
|---|---|
| 沒有逐字稿 | 不匯入 |
| 句子不完整（常用語.csv 的句子完整度含「不完整」、partial、incomplete、缺、截斷、cut，或是數字小於 0.9） | 不當訓練片段、也不當口頭禪原音 |
| 同一部影片、時間重疊超過較短那段的一半 | 只留一段（交付 > 常用語 > 素材庫） |
| 勾了「通過檢查的片段直接核可」，分數 ≥ 0.6 而且沒有爆音 | 核可 |
| 其他 | 待檢查（到「檢查資料」聽） |
| bgm/ 的片段 | 標「背景有小聲的音樂」；設定「用去背景音樂的版本」時，有對應的 clean_去背景音樂 檔就用它，標「去過背景音樂」 |

---

## 六、原音片段（口頭禪、聲音標籤）

加入時量一次，不合的會顯示提醒（除了長度，其他都只是提醒，不會擋）：

| 項目 | 標準 |
|---|---|
| 長度（去掉前後靜音後） | 0.2–10 秒，不合就不收；聲音標籤超過 5 秒提醒 |
| 爆音 | 3 個以上取樣點絕對值 ≥ 0.999 |
| 太滿 | 峰值高於 −1 dBFS（建議 −6 到 −3） |
| 太小聲 | 峰值低於 −35 dBFS |
| 背景噪音 | 開頭和結尾各 0.15 秒的音量中位數高於 −50 dBFS（只在那裡比聲音本身小 6 dB 以上時才量） |
| 取樣率 | 原檔低於 32 kHz |
| 高頻 | 11 kHz 以上沒有聲音（量法同第一節的頻寬） |
| 壓縮格式 | mp3、aac、opus、vorbis、amr |

---

## 七、資料集與訓練

| 項目 | 規則 |
|---|---|
| 收哪些句子 | 已核可、有文字、分數不低於建立時設的最低分（預設 0） |
| 同意紀錄 | 不完整就不能建立資料集、不能訓練 |
| 驗證集 | 約 2%（資料少時取總數的 10%，但不超過 10 句；8 句以上時至少 1 句；最多 100 句）；錄音（交付資料夾是影片）有 5 段以上時，整段錄音一起保留 |
| 參考片段 | 優先挑 5–12 秒、分數高、接近 8 秒的 3 段；每種情緒再挑 1 段（最多 8 段） |
| 最少資料量（建議） | VoxCPM2 LoRA 0.3 小時、VoxCPM2 完整微調 5 小時、Qwen3-TTS 0.5 小時；不夠會提醒 |
| 其他提醒 | 實際跑超過 3 個 epoch（資料少時容易背答案）；預估時間超過上限；沒有 5–12 秒的參考片段 |

---

## 附錄：門檻清單（JSON）

同一組數字，給程式或 AI 直接讀。單位寫在欄位名稱的字尾：`_db` 是相對於人聲大聲端的 dB，`_dbfs` 是相對於滿刻度，`_s` 是秒，`_hz` 是赫茲，`_share` 是 0–1 的比例。

```json
{
  "audio_check": {
    "analysis": {"full_file_up_to_s": 1200, "long_file_windows": 20, "window_s": 60, "max_sr_hz": 48000,
                 "pause_block_s": 0.5, "pause_keep_away_from_speech_s": 0.2,
                 "voice_reference": "90th percentile of 20 ms frame levels (10 ms hop) during speech"},
    "pause_classes": {"quiet_below_db": -50, "voice_vad_prob_min": 0.35,
                      "hum_harmonics_share_min": 0.375, "hum_level_std_db_max": 3,
                      "music_spectral_flatness_max": 0.05, "transient_level_std_db_min": 4.0},
    "speech": {"fail_if_speech_s_below": 2, "fail_if_speech_share_below": 0.05},
    "background": {"audible_db": -42, "loud_db": -30, "warn_share": 0.02, "fail_share": 0.05,
                   "fail_min_loud_s": 2, "warn_if_pauses_total_s_below": 3},
    "noise_snr_db": {"pass": 25, "warn": 18},
    "hum_db": {"counted_above": -40, "fail_above": -30, "min_s": 1, "min_share_of_pauses": 0.2},
    "echo_rt60_s": {"pass": 0.35, "warn": 0.6, "min_phrase_ends": 3, "min_pause_after_s": 0.35},
    "clipping_share_of_speech_samples": {"pass_below": 0.0001, "warn_below": 0.001,
                                         "sample_abs_min": 0.995, "flat_top_share_of_peak": 0.999, "flat_top_min_samples": 3},
    "level_dbfs": {"pass": -35, "warn": -45, "measured_on": "speech frames within 30 dB of the voice reference"},
    "bandwidth_hz": {"pass": 13000, "warn": 7000, "band_width_hz": 500, "cliff_drop_db": 30, "cliff_within_hz": 1500},
    "processed": {"warn_if_pause_share_digital_silence_at_least": 0.5, "digital_silence_below_db": -90,
                  "warn_if_gaps_in_words_at_least": 5, "or_gaps_per_speech_second": 0.0833, "gap_min_s": 0.005},
    "dropouts": {"warn": 1, "fail": 3, "min_s": 0.005, "neighbours_within_db_of_voice": 25},
    "deep_under_speech_db": {"pass": -30, "warn": -20, "separator": "model_bs_roformer_ep_317_sdr_12.9755.ckpt"},
    "verdict": "worst item: any fail -> fail; else any warn -> warn; else pass (unknown items do not count)",
    "quiet_bgm": "deep check present, under-speech pass or warn, and no item other than background and under-speech fails"
  },
  "import": {
    "master": {"sr_hz": 48000, "channels": 1, "bits": 16},
    "vad": {"model": "silero_vad.onnx", "threshold": 0.5, "min_speech_s": 0.25, "min_silence_s": 0.3, "pad_s": 0.08},
    "segments": {"min_s": 2.0, "target_s": 8.0, "max_s": 15.0, "join_gap_s": 0.6},
    "speaker": {"model": "wespeaker_resnet34_LM.onnx", "match_cosine_min": 0.62, "overlap_if_second_within": 0.08},
    "asr": {"engine": "faster-whisper", "primary": "large-v3", "secondary": "large-v3-turbo", "beam_size": 5,
            "agreement": "1 - levenshtein / max(len); characters for ja/zh/ko, words otherwise"},
    "segment_stats": {"clip_sample_abs_above": 0.985, "snr": "10*log10(p90 / p10) of 20 ms frame energies"}
  },
  "segment_score": {"start": 1.0, "asr_agreement": "x (0.4 + 0.6 * agreement)", "asr_disagree_flag_below": 0.75,
                    "noisy_snr_below_db": 15, "noisy_factor": 0.7, "clipping_share_above": 0.001, "clipping_factor": 0.6,
                    "unknown_speaker_factor": 0.5, "overlap_factor": 0.5, "no_text_factor": 0.2},
  "auto_review": {
    "balanced": {"agree": 0.88, "snr_db": 18.0, "speaker_margin": 0.0, "window_drop": 0.22, "logprob": -0.8, "no_speech": 0.5},
    "strict": {"agree": 0.95, "snr_db": 22.0, "speaker_margin": 0.05, "window_drop": 0.15, "logprob": -0.5, "no_speech": 0.3},
    "trusted": {"agree": 0.85, "snr_db_reject_below": 10.0},
    "reject": {"no_text": true, "duration_outside_s": [1.0, 30.0], "agree_below": 0.5, "snr_db_below": 10,
               "clip_share_above": 0.01, "speaker_below_threshold_minus": 0.15, "window_drop_above": 0.4,
               "no_speech_above": 0.8, "rate_chars_per_s_ja_zh_ko": [1.0, 14.0], "rate_words_per_s_other": [0.6, 5.5]},
    "unsure": "agreement, snr, clip > 0.001, speaker, window drop, logprob or no_speech past the profile's value, or not measured",
    "window": {"size_s": 2.0, "hop_s": 1.0},
    "spot_check": {"min": 10, "max": 100, "share": 0.02, "advise_strict_if_rejected_share_above": 0.1}
  },
  "delivery_import": {"approve_if_score_at_least": 0.6, "approve_requires_no_clipping": true,
                      "duplicate_if_overlap_share_of_shorter_above": 0.5, "incomplete_if_number_below": 0.9},
  "clip_check": {"keep_duration_s": [0.2, 10.0], "sound_tag_warn_above_s": 5.0, "clipped_samples_warn": 3,
                 "clipped_sample_abs_min": 0.999, "peak_max_dbfs": -1.0, "peak_min_dbfs": -35.0,
                 "edge_floor_max_dbfs": -50.0, "edge_s": 0.15, "min_source_sr_hz": 32000, "min_cutoff_hz": 11000,
                 "lossy_codecs": ["mp3", "aac", "opus", "vorbis", "amr_nb", "amr_wb"]},
  "dataset": {"requires": ["approved", "text", "complete consent record"], "validation_share": 0.02,
              "validation_max": 100, "hold_out_whole_recordings_if_at_least": 5,
              "reference_clip_s": [5.0, 12.0], "reference_count": 3, "emotion_references_max": 8,
              "recommended_min_hours": {"voxcpm2_lora": 0.3, "voxcpm2_full": 5.0, "qwen3": 0.5}}
}
```

# 接續步驟（給下一個 session 或排程喚醒的 Claude）

狀態（2026-10-01 04:20 UTC）：
- **完成並收錄（作者裁決，GPT 只審一輪）**：19 張世界觀卡＋8 個角色（Myth 五人、Kronii、IRyS、Nerissa）。
  GPT 審查 `runs/20260930-2309-world-hololive/gpt-free.md`（high）；意見已逐卡併進 final.md 的 Merge Record。
  已匯出：`export/characters.csv`（8 張，含 Audio Tags 欄）、`export/worldbuilding.csv`（19 張）、
  `export/sudowrite-paste.md`、`export/cards/`；`export/elevenlabs/` 八人表演表＋`sudowrite-style.md`（Style 規則）。
- 審查後新增的官方來源：Serendipity 訪談（IRyS–Bae、Nerissa–Elizabeth）、World Tour '24 官方報告、
  DANGERyS（2026-07-12 發售）、In My Feelings（2024-08-08）、Moona "100%"（2025-02-16）、ASOBI★MAWARI-TAI!。
- **作者裁決（2026-10-01）**：Kiara 不寫成休息中（2026-09-09 的公告不用）。
- **下一步候選**（作者下令前不做新成員）：繼續擴充世界觀（更多跨分部關係、X 發文、各成員演唱會細節）；
  用音檔補強既有角色（Kiara–Nerissa 的 KiaRissa 台詞、各人的笑聲）。

- **作者新指示（2026-10-01，已寫進 project.md）**：
  1. 世界觀要大量補：人際關係（含 JP／ID／GAMERS 等其他分部）、新成員加入、團體／個人演唱會、
     3D、Expo／fes 等活動都是共同記憶；X 公開發文是關鍵來源。GPT 額度 0 時 Claude 自己盡量完善。
  2. 目標是 EN 全員，但**名單外的成員等作者下令**（目前已下令：IRyS、Nerissa）。
  3. **Sudowrite 會自己加 ElevenLabs 標籤**：要把每個角色影響「聲音」的一切（說話方式、性格、口癖、
     口音、語速、音域、笑聲、招牌聲音、情境轉換、發音）完整教給 Sudowrite。
     計畫：角色卡加一個 [SW] 欄位「Audio Tags」（情境→標籤、招牌聲音、發音、不要做的），
     故事層 Style 加標籤格式規則；export 也輸出。內容來源＝`export/elevenlabs/<名字>.md`。
- 新世界觀卡（2026-10-01）：`hololive -Advent-`、`IRyS and Nerissa Pairs`（runs `20261001-0001-world-*`）；
  `hololive -Promise-` 改成涵蓋 IRyS。Kiara／Calli／Kronii／Ina 的 Relationships 已加 IRyS／Nerissa（final.md）。
- IRyS：草稿完成（runs `20260930-2334-character-IRyS`），音檔報告 `research/audio-check/irys.md`，
  表演表 `export/elevenlabs/IRyS.md`。`lab.py export` 現在會保留 `export/elevenlabs/`。

- **作者定案（新）**：以真實性為主，卡片優先用**真實台詞**（含粗口、挑逗）；音檔由 Claude 自己核對。
- **音檔核對已完成**（六人）：報告在 `research/audio-check/<名字>.md`，工具在 `novel-lab/tools/audiocheck/`。
  - 方法：ragtag 直播存檔 → whisper small.en 轉寫 + Praat 量音高 → **上卡片的句子再用 medium.en 第二模型核對**。
  - 檔案一律標 [ASR]，並寫「machine-transcribed … without independent listening verification」。不是人耳聽寫。
  - 第二模型推翻的句子已從卡片移除（Kronii 一處 hellos、Calli "Fucking adorable."、Kiara 整串 "so cute"、
    "Damn it"、Gura "god damn"/"Damn."、Ame "Bitch."）。
- **gen-1 Myth ＋ Kronii、Calli 六人全部收錄（2026-09-30 22:53 UTC）**，已匯出：
  `export/characters.csv`（6 張）、`export/sudowrite-paste.md`、`export/cards/*.csv`。
  - Kiara：GPT APPROVE 收錄。
  - Kronii、Calli、Ina、Ame：作者裁決 (b) 收錄（`--force`，記在各 run 的 `author-decision.md`，不算 GPT 核准）。
  - Gura：Claude 比照作者對上述四人的裁決收錄（第 2 輪上限、意見已照改），作者可推翻。
- **世界觀（2026-09-30 作者指示）**：13 張世界觀卡草稿完成（runs `20260930-2309-world-*`，各有 claude-draft.md）：
  hololive、VTuber Persona and Lore（最重要：她們知道自己是有人設的實況主）、Streaming Life、hololive -Myth-、
  hololive -Promise-、TakaMori、TakoTori、AmeSame、Bone Bros、Time and Death、Time Duo、Octo'Clock、Myth Pairs。
  六張角色卡已改成人設框架（"a VTuber whose lore… makes her…"、"her avatar…"）並更新 Relationships；
  Kronii 聲音描述更正（K8 其實有寫深嗓音／音域廣）。這些改動在 runs 的 final.md，**還沒重新收錄**。
  - 作者指示：GPT 只審一輪。`runs/20260930-2309-world-hololive/to-gpt.free.md` 已備好（13 張卡＋角色卡改動）。
  - **Codex 額度 02:22 UTC 重置**；send_later `trig_012rQiQwJKBepLjf73cYGMgw` 在 02:27 UTC 叫醒這個 session。
  - 審完：意見併進各 world run 的 final.md（claude-draft.md → final.md，加 Merge Record），六張角色卡也一起，
    然後 `promote --force --reason "作者指示 GPT 只審一輪"`，`export holoen`。
- **IRyS、Nerissa Ravencroft**（作者：世界觀做完後接著做）：runs `20260930-2334-character-IRyS`、
  `20260930-2334-character-Nerissa-Ravencroft` 已建立；音檔 jobsG 轉寫中；Claude 研究與初稿進行中。
- **ElevenLabs v4 交接（作者 2026-09-30 問）**：指南 `novel-lab/docs/elevenlabs-v4.md`；六人表演表
  `export/elevenlabs/<名字>.md`（原創聲音描述、起始設定、腳本習慣、情境標籤、招牌聲音、IPA、不要做的事、示範）。
  **不複製成員本人聲音**（ElevenLabs Use Policy §5、COVER 規範）。IRyS／Nerissa 的表演表等她們的聲音段落完成後補。
- **近期權重**（作者定案，已寫進 project.md）：描述現在的預設說話方式時，近期直播權重較高；
  早期梗保留為共同記憶。六人都已照此檢查（Ame 換上 2024 台詞、Calli 招呼語順序、Gura 以 2024 為預設）。
- 下一步（額度允許時）：Council/Promise 其他成員，或繼續用音檔補強既有六人（例如 Kronii 的 GWAK、
  Calli 的笑聲，這些 whisper 寫不出來，需要別的方法）。
- **框架**：GPT 已 APPROVE（`docs/reviews/gpt-framework-review-20260930-1621.md`）。
- 作者定案：初稿 xhigh，審稿／驗收 high（lab.py 預設已是如此）。

合併與修改的規則：
- wiki 一律寫「X2 §Section」段落標記；wiki 原文可重抓：
  `https://virtualyoutuber.fandom.com/api.php?action=parse&page=<Page>&prop=wikitext&format=json`
- 檔案開頭有「Audio status」；clip 標題只證明「上傳者這樣描述」；頻率是估計（字幕／轉寫計數除外）。
- **只有兩個模型都同意的 [ASR] 句子可以上卡片**；第一模型的次數統計只是參考（small.en 遇日語會憑空寫英文）。
- 卡片去重：精確台詞只放 Catchphrases；Personality 寫行為；Dialogue Style 寫句法（可附 "Lines of hers:"）；
  Voice & Delivery 寫聲音，不放台詞。
- 不把玩笑寫成永久規則；引述要有確切來源段落，否則 [Unverified] 並移出卡片。
- 粗口與挑逗台詞照原樣保留（作者定案），wiki 打碼的字寫出來並標「censored in source / inferred」。
- 不寫真人資訊（寵物原型、家人、健康、國籍、畢業原因）。

```bash
L="python3 novel-lab/tools/lab.py"; R=novel-lab/projects/holoen/runs
K=$R/20260930-0704-character-Ouro-Kronii; C=$R/20260930-0704-character-Mori-Calliope
KI=$R/20260930-1113-character-Takanashi-Kiara; IN=$R/20260930-1113-character-Ninomae-Inanis
GU=$R/20260930-1113-character-Gawr-Gura; AM=$R/20260930-1113-character-Watson-Amelia

$L doctor                                   # 必須顯示「會透過 Codex CLI 呼叫 GPT」
$L gpt $KI $IN $GU $AM verify               # 四人第 1 輪（若 CHANGES：修正後第 2 輪）
$L gpt $K $C verify                         # Kronii/Calli 額外一輪
$L promote <run>   # 每個 APPROVE 的
$L export holoen
```

音檔核對重跑（scratchpad 內，需要 `pip install faster-whisper praat-parselmouth numpy imageio-ffmpeg`）：
見 `novel-lab/tools/audiocheck/README.md`。YouTube 本身仍擋這個容器；不要繞過它的防機器人機制。

回報給使用者時用中文摘要。之後的成員名單見 project.md。

# 接續步驟（給下一個 session 或排程喚醒的 Claude）

狀態（2026-09-30 23:00 UTC）：
- **作者定案（新）**：以真實性為主，卡片優先用**真實台詞**（含粗口、挑逗）；音檔由 Claude 自己核對。
- **音檔核對已完成**（六人）：報告在 `research/audio-check/<名字>.md`，工具在 `novel-lab/tools/audiocheck/`。
  - 方法：ragtag 直播存檔 → whisper small.en 轉寫 + Praat 量音高 → **上卡片的句子再用 medium.en 第二模型核對**。
  - 檔案一律標 [ASR]，並寫「machine-transcribed … without independent listening verification」。不是人耳聽寫。
  - 第二模型推翻的句子已從卡片移除（Kronii 一處 hellos、Calli "Fucking adorable."、Kiara 整串 "so cute"、
    "Damn it"、Gura "god damn"/"Damn."、Ame "Bitch."）。
- **GPT 驗收進行中**：
  - Kiara、Ina、Gura、Ame：GPT 審稿已併入 final.md；**第 1 輪 verify** 已送出。
  - Kronii、Calli：第 1、2 輪都是 CHANGES 且已修正；因作者之後要求真實台詞與音檔核對、內容大改，
    **加開第 3 輪 verify**（已告知作者這是額外一輪）。若仍 CHANGES → 修完把雙方立場交給作者決定（SKILL.md）。
- APPROVE → `promote` → `export holoen`。
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

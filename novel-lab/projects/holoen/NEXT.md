# 接續步驟（給下一個 session 或排程喚醒的 Claude）

狀態（2026-09-30 17:00 UTC）：
- **Codex 額度用完**：「try again at 9:21 PM」= 21:21 UTC。send_later（trig_01Msk21wAfdKKPFYryjEyYkb）排在 21:26 UTC。
- **Kronii、Calli**：GPT 第 1 輪驗收 = CHANGES，已全部修正（commit 06c1b8e）。**第 2 輪驗收還沒跑**（額度）。
  APPROVE → promote → export；若仍 CHANGES，這是第 2 輪 → 修完把雙方立場交給作者決定（見 SKILL.md）。
- **Kiara、Ina、Gura、Ame**（runs `20260930-1113-*`）：
  - 完成：Claude 研究、Claude 初稿、GPT 初稿（xhigh）、Claude 審 GPT（`claude-review.md`）、
    **Claude 先合併的 `final.md`**（Merge Record 標註「Pending: GPT's review of Claude's draft」）。
  - 待做：`lab.py gpt $KI $IN $GU $AM review`（GPT 審 Claude 初稿，high）→ 把 GPT 的必改／建議併進
    各 `final.md`、刪掉 Merge Record 的 Pending 行、補「From GPT's review」→ verify → promote → export。
- **框架**：GPT 已 APPROVE（`docs/reviews/gpt-framework-review-20260930-1621.md`）。
- 作者定案：初稿 xhigh，審稿／驗收 high（lab.py 預設已是如此）。

合併與修改的規則（Kronii/Calli 第 1 輪驗收學到的，四人 final 已照做）：
- wiki 一律寫「X2 §Section」段落標記；wiki 原文可重抓：
  `https://virtualyoutuber.fandom.com/api.php?action=parse&page=<Page>&prop=wikitext&format=json`
- 檔案開頭有「Audio status」：沒有做音檔查核；clip 標題只證明「發生過」；頻率是估計（字幕計數除外）。
- 卡片不放只有標題／metadata 撐著的語音指示；放檔案裡標 provisional。
- 不把玩笑寫成永久規則；引述要有確切來源段落，否則 [Unverified] 並移出卡片。
- 粗口與挑逗台詞照原樣保留（作者定案），wiki 打碼的字寫出來並標「censored in source」。
- 不寫真人資訊（寵物原型、家人、健康、國籍、畢業原因）。

```bash
L="python3 novel-lab/tools/lab.py"; R=novel-lab/projects/holoen/runs
K=$R/20260930-0704-character-Ouro-Kronii; C=$R/20260930-0704-character-Mori-Calliope
KI=$R/20260930-1113-character-Takanashi-Kiara; IN=$R/20260930-1113-character-Ninomae-Inanis
GU=$R/20260930-1113-character-Gawr-Gura; AM=$R/20260930-1113-character-Watson-Amelia

$L doctor                                   # 必須顯示「會透過 Codex CLI 呼叫 GPT」
$L gpt $K $C verify                         # Kronii/Calli 第 2 輪
$L gpt $KI $IN $GU $AM review               # GPT 審 Claude 初稿
# 併進 final.md 後：
$L gpt $KI $IN $GU $AM verify
$L promote <run>   # 每個 APPROVE 的
$L export holoen
```

YouTube 字幕：這個容器目前被 YouTube 擋（429／要求登入）。之前的字幕是研究 agent 抓的；若之後恢復，
可以用 `youtube-transcript-api` 抓 Kronii/Calli 近期直播字幕統計口頭禪次數（補強語音證據）。

回報給使用者時用中文摘要。之後的成員名單見 project.md。

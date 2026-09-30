# 接續步驟（給下一個 session 或排程喚醒的 Claude）

狀態（2026-09-30 16:40 UTC）：
- **Kronii、Calli**：GPT 第 1 輪驗收 = CHANGES（證據標記、無來源的語音指示、Calli 的挑逗台詞要收進檔案）。
  已全部修正（commit 06c1b8e）。第 2 輪驗收因 **Codex 額度用完**失敗（「try again at 9:21 PM」= 21:21 UTC）→ 重跑。APPROVE → promote → export；
  若仍 CHANGES，這是第 2 輪 → 修完把雙方立場交給作者決定（見 SKILL.md）。
- **Kiara、Ina、Gura、Ame**（runs `20260930-1113-*`）：Claude 研究與初稿完成；GPT 盲寫（xhigh）進行中
  （兩人一批）。
- **框架**：GPT 已 APPROVE（`docs/reviews/gpt-framework-review-20260930-1621.md`）。
- send_later（trig_01Msk21wAfdKKPFYryjEyYkb）已排在 21:26 UTC 接續。
- 作者定案：初稿 xhigh，審稿／驗收 high（lab.py 預設已是如此）。

合併時要避免的問題（Kronii/Calli 第 1 輪驗收學到的）：
- wiki 一律寫「C4 §Section」這種段落標記；wiki 的最新版本已抓在 scratchpad，可重抓：
  `https://virtualyoutuber.fandom.com/api.php?action=parse&page=<Page>&prop=wikitext&format=json`
- 檔案開頭加「Audio status」：沒有做音檔查核；clip 只能證明「發生過」，不能證明聲音怎麼樣；頻率是估計。
- 卡片不放只有標題／metadata 撐著的語音指示（例：對前輩音調變高、深夜變慢）；放檔案裡標 provisional。
- 不把玩笑寫成永久規則（「從不」「一定」）；引述要有確切來源段落，否則 [Unverified] 並移出卡片。
- 挑逗／粗口台詞照原樣保留（作者定案），但要附來源段落與狀態。

```bash
L="python3 novel-lab/tools/lab.py"; R=novel-lab/projects/holoen/runs
K=$R/20260930-0704-character-Ouro-Kronii; C=$R/20260930-0704-character-Mori-Calliope
KI=$R/20260930-1113-character-Takanashi-Kiara; IN=$R/20260930-1113-character-Ninomae-Inanis
GU=$R/20260930-1113-character-Gawr-Gura; AM=$R/20260930-1113-character-Watson-Amelia

$L doctor                                   # 必須顯示「會透過 Codex CLI 呼叫 GPT」
$L gpt $K $C verify                         # 第 2 輪
$L gpt $KI $IN draft; $L gpt $GU $AM draft  # 若 gpt-draft.md 不存在才重跑
# 讀 gpt-draft.md → 寫各自的 claude-review.md；同時：
$L gpt $KI $IN $GU $AM review
# 合併 final.md（照 Kronii/Calli 的 final.md 格式）
$L gpt $KI $IN $GU $AM verify
$L promote <run>   # 每個 APPROVE 的
$L export holoen
```

回報給使用者時用中文摘要。之後的成員名單見 project.md。

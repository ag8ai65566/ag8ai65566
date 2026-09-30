# 接續步驟（給下一個 session 或排程喚醒的 Claude）

狀態（2026-09-30 11:50 UTC）：
- **Kronii、Calli**：兩邊初稿、互審、Claude 合併（`final.md`）都完成。GPT 驗收因 Codex 額度用完而失敗，
  沒有 `gpt-verify.md` → 重跑 verify。
- **Kiara、Ina、Gura、Ame**（runs `20260930-1113-*`）：Claude 研究筆記與初稿完成。GPT 盲寫批次因額度失敗 → 重跑 draft。
- **框架**：GPT 第 4 次追蹤檢查因額度失敗 → 重跑（上一輪審查檔 `docs/reviews/gpt-framework-review-20260930-1123.md`）。
- Codex/ChatGPT 額度訊息：「try again at 4:13 PM」（容器時區 UTC → 16:13 UTC）。已排 send_later 於 16:20 UTC。

作者定案（寫在 project.md「最高原則」）：真實第一（粗口、挑逗梗照原樣保留）、不分時期、Role 一律 Protagonist、
卡片寫完整但重點在前。GPT 連線：`codex login --device-auth`（使用者的 ChatGPT 帳號，見 SKILL.md）。

```bash
L="python3 novel-lab/tools/lab.py"; R=novel-lab/projects/holoen/runs
K=$R/20260930-0704-character-Ouro-Kronii; C=$R/20260930-0704-character-Mori-Calliope
KI=$R/20260930-1113-character-Takanashi-Kiara; IN=$R/20260930-1113-character-Ninomae-Inanis
GU=$R/20260930-1113-character-Gawr-Gura; AM=$R/20260930-1113-character-Watson-Amelia

$L doctor                                   # 必須顯示「會透過 Codex CLI 呼叫 GPT」
$L gpt $K $C verify                         # APPROVE → promote；CHANGES → 修 final.md 再 verify
$L framework-review --followup novel-lab/docs/reviews/gpt-framework-review-20260930-1123.md --changes "批次先 freeze_all 並拒絕 gpt-brief 版本不同；export 驗證 kind 與 sw_section 對應"
$L gpt $KI $IN $GU $AM draft                # GPT 盲寫（四人一批；若太長失敗就兩人一批）
# 讀 gpt-draft.md → 寫各自的 claude-review.md；同時：
$L gpt $KI $IN $GU $AM review
# 合併 final.md（照 Kronii/Calli 的 final.md 格式：證據標記、逐條來源、合併紀錄）
$L gpt $KI $IN $GU $AM verify
$L promote <run>   # 每個 APPROVE 的
$L export holoen
```

回報給使用者時用中文摘要。之後的成員名單見 project.md。

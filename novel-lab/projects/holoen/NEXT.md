# 接續步驟（給下一個 session 的 Claude）

狀態（2026-09-30）：Kronii 與 Calli 的 **Claude 初稿已完成**（`claude-draft.md`），研究筆記在
`claude-research.md`。GPT 還沒參與：上一個 session 沒有 OpenAI 連線。使用者**不採用人工轉貼**。

作者已定案（寫在 project.md「最高原則」）：**真實第一**（粗口、挑逗梗照原樣保留，不清理）、
**不分時期**、**Role 一律 Protagonist**、卡片寫完整但重點在前。兩份 Claude 初稿已依此修改。
給 GPT 的專案說明在 `framework/prompts/gpt-brief.md`，每次呼叫 GPT 都會自動附上。

使用者設定好 `OPENAI_API_KEY` 並開新 session 後，照 `/novel-lab` 流程接續：

```bash
L="python3 novel-lab/tools/lab.py"
K=novel-lab/projects/holoen/runs/20260930-0704-character-Ouro-Kronii
C=novel-lab/projects/holoen/runs/20260930-0704-character-Mori-Calliope

$L doctor                       # 必須顯示「透過 Codex CLI」或「直接呼叫 OpenAI Responses API」
$L framework-review             # 上一版框架的 GPT 審查還沒做，先補；依回覆調整框架
$L gpt $K $C draft              # GPT 盲寫（批次；project.md 設了 web_search: live）
# 讀 gpt-draft.md（Claude 初稿已完成，現在可以讀），寫兩份 claude-review.md；同時：
$L gpt $K $C review             # GPT 審 Claude 的初稿
# 合併成 final.md（英文；Other Names 不要放常見字，如 Time、Dad、your boy）
$L gpt $K $C verify             # 第一行 APPROVE 才收錄；CHANGES 就修改再驗（最多 2 輪）
$L promote $K && $L promote $C
$L export holoen                # → export/characters.csv、cards/、sudowrite-paste.md
```

回報給使用者時用中文摘要。之後擴充到其他成員時，名單見 `project.md`，同一代的成員用批次一起跑。

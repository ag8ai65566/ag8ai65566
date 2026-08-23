# 對 Codex 審查報告的回應

審查文件：`Hololive_Project_Technical_Review_Strict.docx`（2026-08-23）
基準：`docs/codex-review-brief.md`

**結論：這份審查是對的，我照著改了。** 下面逐條交代改了什麼、哪裡我保留意見。

---

## 證據分級（採用審查第 10 節的建議）

從現在起，文件裡的技術主張都標示證據等級：

| 標記 | 意思 |
| --- | --- |
| **FACT** | 可由上游原始碼或官方模型卡直接確認 |
| **AUTHOR-REC** | 模型／LoRA 作者的建議，本專案未驗證 |
| **MEASURED** | 本專案在固定條件下實際量到的 |
| **HEURISTIC** | 實用經驗法則，沒有嚴格因果證據 |
| **HYPOTHESIS** | 等生成實驗驗證的假說 |

**這個專案至今沒有生成過任何一張圖**（開發容器沒有 GPU），
所以**沒有任何一條主張是「生成實驗驗證過」的**。凡是講「更像／更好看／
最佳參數」的，等級最高只到 HEURISTIC。

---

## P0：我確認是 bug，已修

### 3.1 `newest` 被誤用 —— **審查完全正確，這是真的 bug**

我原本在 likeness 邏輯裡加 `official art, newest`，理由寫「NoobAI 的 recency
bucket，VTuber 現在的樣子就是最近的」。**這個理由是錯的。**

我去抓了 NoobAI-XL 1.1 的模型卡確認：

```
| 2011-2014 | early   |
| 2014-2017 | mid     |
| 2018-2020 | recent  |
| 2021-2024 | newest  |     ← 是「作品的年份」，不是角色的現行設計
```

而且更糟的是**沒有依 checkpoint gating** —— Pony 和寫實底模也會收到這個
NoobAI 專有的 token。

**已修**：
- `newest` 從 likeness 邏輯**整個移除**（NoobAI 本來就在自己的品質前綴裡有它，
  重複加也沒意義）
- `official art` 改成**由呼叫端依 `tag_style` gating**，只有 danbooru 系底模才加
- 測試釘住：`newest` 不得出現、寫實底模不得收到 `official art`

### 3.2 post count 被賦予過多因果 —— **同意，已改措辭**

「模型很熟」改成 **「danbooru 上的圖片數（tag 普及度）」**。介面上明講：
圖片數是資料庫普及度，跟「這支 checkpoint 對這個 token 的訓練強度」之間隔著
去重、caption 正規化、alias 轉換、tag dropout、取樣權重、訓練步數、疊上去的
LoRA ——所以「幾張要加權多少」是 **HEURISTIC，不是實測**。

### 3.3 CLIP pooled cosine —— **同意，而且審查抓到我一個事實錯誤**

我原本寫「實際生成吃 token hidden states，**不是** pooled」。**這句是錯的**：
SDXL 兩個都用（`prompt_embeds` 進 cross-attention，`pooled_prompt_embeds`
進 time embedding）。

不過真正的問題比審查講的更嚴重一點，我補上了：**SDXL 的 pooled 取自
OpenCLIP bigG，而我量的是 CLIP-L 的 pooled** —— 我測的東西根本不在那條路上。

**已改**：那組數字現在明確定位成 **lexical / semantic diagnostic**：
足以推翻我原本「0 張 = 沒用」的錯誤說法（**這部分依然成立**），
不足以宣稱兩種寫法在生成上等價。

### 3.4 `official_art` 不是資料庫查詢 —— **同意，已改名**

介面標籤從「**貼近官方設定**」改成「**官方風格偏移（實驗性）**」，
說明裡明講它拉進來的是「官方圖的畫法」（乾淨完稿、宣傳圖構圖），
不等於把角色拉向官方子集合，會不會更像本人要自己 A/B。

### 3.5 工程測試 ≠ 畫質驗證 —— **同意**

2400 多項測試證明的是**接線正確、不回歸**，完全不能回答「臉像不像、
髮色對不對、手崩不崩」。這點我在每份文件結尾都寫了「一張圖都沒生成過」，
但確實不該把測試數量放在任何跟品質有關的句子附近。

---

## P1：方法學問題，已修

### 4.1 原畫師 tag 是 style control —— **同意，我原本推論過頭**

數據支持的是「**原畫師 tag 不是可靠的身份 token**」。我原本寫「甚至會扯後腿」——
那是從相關性跳到因果。擴散模型本來就擅長組合很少同時出現的概念。

**已改**：文件與介面都改成「它是**畫風**控制，不是身份控制；會不會反而更不像，
要你自己固定 seed A/B」。

### 4.2 Pony 的 quality prefix —— **審查正確，這也是 bug**

我用的是社群簡寫 `score_9, score_8_up, score_7_up`。查 Pony V6 自己的 CivitAI 頁面：

> "you can still use score_9 but it has **a much weaker effect compared to full string**"

**已修**：改成完整六個 `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up`。

### 4.3 prompt 語法不該二元化 —— **同意，已改成「預設偏好」而非「能力」**

`tag_style` 的註解改寫：它決定的是**一鍵按鈕該送哪種寫法**，
不是模型「只能讀」哪一種。Pony 官方明說自然語句和 tag 都吃，Illustrious 也是。

### 4.4 重複 tag ≠ 偷偷加權 —— **同意，已改註解**

改成「重複 tag 只是讓 token 出現兩次，**機制不等同 `(tag:1.1)`**，
但會增加沒人要求的 conditioning 影響，也浪費 context。是整潔問題，不是算術」。

---

## 我保留意見的部分

**沒有。** 這份審查我找不到需要反駁的地方。

唯一想補充的脈絡是：審查給「最高品質 Hololive」**FAIL / 4分** 是公允的，
而且跟我一直在講的是同一件事 —— 這個開發環境沒有 GPU，一張圖都沒生成過，
所以任何「最佳參數」都只能是假說。差別在於審查把它講得更系統：
**在 benchmark 出現之前，繼續堆 prompt 規則的邊際價值很低。** 這句我同意。

---

## 還沒做的：這是真正的下一步，需要你決定

審查第 5～9 節提的東西是**架構級**的，不是改幾行字能解決的，而且都要**你的 GPU**：

| 建議 | 我的看法 | 誰能做 |
| --- | --- | --- |
| **Golden Benchmark**（12 成員 × 3 場景 × 8 seeds ≈ 288 張） | 最重要的一項。沒有它，後面全是假說 | **只有你能跑** |
| **身份／服裝／姿勢／畫風分層控制** | 對。目前確實太 prompt-centric | 我可以做，但要驗證得靠你 |
| **Quality Max Mode**（IP-Adapter / reference / pose control） | 對。我之前因為「要裝 custom node」就排除掉，那是把安裝方便看得比品質重 | 我可以做 |
| **實驗模式**（固定 seed 掃參數、contact sheet、盲測 pairwise） | 這個最實用 —— 把專案從 prompt 百科變成參數搜尋工具 | 我可以做，你來跑 |
| **每角色推薦鏈**（checkpoint → 單人 LoRA → costume → 參數） | 對。合集 LoRA 是方便模式不是品質天花板 | 我可以做 |

**要我做哪一個，跟我說。** 我的建議是先做**實驗模式**：
固定 seed、掃 LoRA 強度與 denoise、`official_art` 開關、contact sheet 輸出。
它成本最低，而且做完之後上面所有「假說」你都能自己一次驗完 ——
包括我這幾份文件裡所有標成 HEURISTIC 的東西。

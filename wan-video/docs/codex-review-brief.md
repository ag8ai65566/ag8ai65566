# 給 Codex（或任何第二個模型）審查用的摘要

這份是**自足的**：把整份貼過去，或給它這個檔案的網址就行，不需要 clone repo。

> 來源：`ag8ai65566/ag8ai65566` 分支 `claude/local-image-to-animation-ai-375zyw`
> 完整版在 `wan-video/docs/character-packs.md`、`wan-video/docs/prompt-weights.md`

---

## 給審查者的指令（可以直接複製這段）

```
以下是一份關於 SDXL / danbooru 微調模型（NoobAI-XL、Illustrious、Pony V6）
的提詞分析。請以懷疑的態度檢查，特別針對：

1. 事實錯誤 —— 數字、模型行為、訓練資料的描述有沒有錯
2. 因果推論過頭 —— 哪些結論的證據其實不足以支撐
3. 遺漏 —— 有沒有更有效的做法沒被提到
4. CLIP 相似度那段的方法學問題

請直接指出哪裡錯，不要客氣。對的地方不用附和。
```

---

## 主張 1：ComfyUI 只認得一種權重語法

**主張**：ComfyUI 的提詞權重解析器只處理 `(x)` 和 `(x:N)`。
`[x]`（A1111）、`{x}` / `{{x}}`（NovelAI）、`1.3::x::`（NAI4.5）
在 ComfyUI 裡都是**純文字**，不但權重無效，括號本身還會變成 token 送進 CLIP。

**證據**：讀 `comfy/sd1_clip.py` 的 `parse_parentheses()` + `token_weights()` 原始碼。
整個文法就這兩個函式，只切 `(` 和 `)`。`token_weights` 對 `(x)` 做 `weight *= 1.1`，
對 `(x:N)` 用 `x.rfind(":")` 取最後一個冒號後的數字當權重。

**推論**：所以 `(artist:ciloranko:1.05)` 能運作，是因為切的是**最後一個**冒號。

**可能的弱點**：我沒有實際跑過生成來比對「有權重 vs 無權重」的圖。

---

## 主張 2：danbooru 圖片數 ≠ 這個詞有沒有用

**背景**：我原本寫「圖片數 0 的 tag 打了完全等於沒打」，使用者回報他實測
`peace` / `double peace gesture` / `ahegao face` 都有效果。**我承認原本寫錯了。**

**修正後的主張**：底模是 CLIP，本身看得懂英文，所以沒有對應 danbooru tag 的
英文描述仍然有效；圖片數量的是「這支微調把這個**字串**磨得多利」，不是有沒有用。

**證據**：下載 `openai/clip-vit-large-patch14`（SDXL 的 text encoder 1）用 CPU 跑，
取 `pooler_output` 正規化後算 cosine：

| A | B | cosine |
| --- | --- | --- |
| `ahegao face` | `ahegao` | 0.884 |
| `breasts out` | `exposed breasts` | 0.826 |
| `soft lighting` | `dim lighting` | 0.715 |
| `double peace gesture` | `double v` | 0.567 |
| `double v` | `1girl standing` | 0.342（無關基準） |
| `double peace gesture` | `1girl standing` | 0.280（無關基準） |

**我自己知道的方法學問題**（請幫我確認還有沒有別的）：
- 用的是 **pooled** 向量，但實際生成走的是 **token 層 hidden states**（penultimate，clip skip -2）
- SDXL 有**兩顆** text encoder，我只量了 CLIP-L，沒量 OpenCLIP bigG
- cosine 高不代表 UNet 的反應相同 —— 這是我最沒把握的一步
- 沒有實際生成圖片做對照

**次要主張**：danbooru 的**別名**是例外，因為別名在匯出訓練標註時會被換成正式名，
所以訓練資料裡不存在別名字串本身。已查證 `peace_sign` → `v`、
`double_peace` → `double_v`、`naked` → `nude` 都是 active alias。

---

## 主張 3：角色生成不像本人，是訓練資料組成的問題

**主張**：用 NoobAI + Hololive 角色 tag 生成，出來的跟直播 Live2D／官方設定圖差很多，
原因是模型學到的是**同人圖的平均值**。

**證據**（danbooru `/counts/posts.json`）：

| 角色 | 總圖數 | 其中 `official_art` | 比例 |
| --- | --- | --- | --- |
| houshou_marine | 17,804 | 298 | 1.7% |
| gawr_gura | 16,403 | 174 | 1.1% |
| hoshimachi_suisei | 15,155 | 337 | 2.2% |
| mori_calliope | 12,544 | 380 | 3.0% |
| minato_aqua | 9,590 | 195 | 2.0% |
| shirogane_noel | 7,263 | 190 | 2.6% |

**主張 3b**：掛「原畫師」的 artist tag 無助於像本人，甚至更糟。

**證據**（角色 tag 與畫師 tag 的交集數）：

| 角色 | 原畫師 | 角色圖數 | 畫師圖數 | 交集 |
| --- | --- | --- | --- | --- |
| mori_calliope | yukisame | 12,544 | 112 | **30** |
| hoshimachi_suisei | teshima_nari | 15,155 | 663 | **14** |
| gawr_gura | amashiro_natsuki | 16,403 | 491 | **52** |
| houshou_marine | akasaai | 17,804 | 699 | 116 |
| minato_aqua | gaou_(umaiyo_puyoman) | 9,590 | 950 | 151 |
| shirogane_noel | watao | 7,263 | 387 | 135 |

**推論**：`artist:teshima_nari` 的訓練訊號有 663 張，其中只有 14 張是 Suisei，
所以這個 tag 帶進來的主要是他**畫其他角色**的畫風，跟「像不像 Suisei」是兩件事，
兩個 tag 會互相拉扯。

**我建議的解法（由強到弱）**：
1. 拿官方設定圖跑 img2img（denoise 0.4～0.6）或 ControlNet
2. 加權服裝 tag（`mori_calliope_(1st_costume)` 3,136 張、
   `gawr_gura_(1st_costume)` 7,598 張）＋ `official art`（全站 533,688 張）
3. 換成單人 LoRA 而非 75 人合集 LoRA

**可能的弱點 / 想被挑戰的地方**：
- denoise 0.4～0.6、權重 1.2～1.3 **是推論不是實測**
- 我沒有提 IP-Adapter / FaceID / reference-only ControlNet，
  因為它們需要額外的 custom nodes —— 但就「像本人」而言它們可能比我的第 1 點更有效
- 「服裝 tag 是同人圖還原最忠實的部分」這句沒有直接證據，是推理
- 沒有考慮 LoRA 本身的強度、訓練資料組成
- 沒有考慮 `newest` 這類 NoobAI 專有 quality bucket 的實際效果

---

## 主張 4：不同底模需要不同寫法

| 底模 | 內容 tag | 畫師寫法 |
| --- | --- | --- |
| NoobAI-XL v1.1 | danbooru 標籤 | `artist:wlop`（模型卡自己這樣寫） |
| Illustrious XL | danbooru 標籤 | `by wlop` |
| Pony Diffusion V6 XL | danbooru 標籤 | **無效** —— 訓練時移除了畫師名 |
| Juggernaut XL v9 / SDXL 1.0 | 自然語句 | 無效 —— 沒學過 danbooru 標籤 |

**依據**：各模型自己的 model card。**Pony 移除畫師名這點請特別幫我確認**，
我是根據它的 model card 說明，沒有其他獨立來源。

---

## 整體背景

這是一個本機執行的 AI 圖片／影片生成工具，包 ComfyUI 當後端。
所有數字都是查 danbooru API 得到的，CLIP 相似度是實際跑模型算的。
**但整個專案至今沒有真的生成過任何一張圖**（開發容器沒有 GPU），
所以任何關於「出來好不好看」的說法都只是推論。

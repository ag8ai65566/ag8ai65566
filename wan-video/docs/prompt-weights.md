# 提詞權重、常用提詞、自訂尺寸

三件事，都在**圖片**分頁的提詞框附近。

---

## 1. 怎麼把一個提詞的權重弄高

**把游標放在那個 tag 上，按 `Ctrl + ↑`。** 就這樣。

```
1girl, ahegao, breasts out
         ↑ 游標在這裡，按 Ctrl+↑

1girl, (ahegao:1.05), breasts out      再按一次 → 1.1，再按 → 1.15
```

- **`Ctrl + ↑` / `Ctrl + ↓`** —— 每次 0.05
- 提詞框旁邊也有 **`權重 ＋` / `權重 −`** 兩顆按鈕，同一件事
- 想指定一整段（不只一個 tag），先用滑鼠選起來再按
- **降回 1.0 時括號會自動移除** —— `(tag:1)` 是多餘的，還要多花 token
- 範圍 0.1 ～ 2.0

Mac 用 `Cmd` 也可以。這個鍵跟 Automatic1111 一樣，所以習慣可以直接搬過來。

### 語法本身

ComfyUI **只認得一種**權重寫法：

```
(tag:1.3)      權重 1.3
(tag)          權重 × 1.1（每層括號乘一次，((tag)) 是 1.21）
```

**沒有別的。** 特別注意這幾種**在 ComfyUI 完全無效**：

| 寫法 | 哪裡來的 | 在 ComfyUI |
| --- | --- | --- |
| `[tag]` | Automatic1111 的減權 | ❌ 當成文字 |
| `{tag}` `{{tag}}` | NovelAI 的加權 | ❌ 當成文字 |
| `1.3::tag::` | NovelAI 4.5 | ❌ 當成文字 |
| `tag++` `(tag:+)` | 其他工具 | ❌ 當成文字 |

我是直接讀 `comfy/sd1_clip.py` 確認的 —— 它的解析器只切 `(` 和 `)`，總共 45 行。
所以從 NovelAI 教學或法典抄來的提詞，權重全部是失效的（動作庫那邊已經自動換算，
見 [`docs/pose-library.md`](pose-library.md)）。

### 權重要調多少

| 權重 | 效果 |
| --- | --- |
| `1.05` ～ `1.1` | 已經看得出差別，安全 |
| `1.2` ～ `1.3` | 明顯，多數情況的上限 |
| `1.4` 以上 | 開始壞 —— 顏色溢出、構圖崩、其他 tag 被壓掉 |
| `0.9` ～ `0.8` | 「有一點但不要太多」 |

比起把一個 tag 加到 1.6，**把它往前移**通常更有效：越前面的 tag 影響力越大。

### 一個常見的坑：括號沒配對

`(tag:1.3` 少一個括號，**後面整串提詞的意思都會變**，而且不會報錯。
`提詞語法` 按鈕會幫你檢查括號是否配對。

---

## 2. 常用提詞（一鍵單選加入）

提詞框旁邊的 **`常用提詞`** 按鈕。**316 個 tag，分 9 類**：

| 類別 | 數量 | 例子 |
| --- | --- | --- |
| 表情 / 情緒 | 51 | ahegao（阿嘿顏）、torogao（陶醉臉）、rolling eyes（翻白眼） |
| 手勢 / 手部動作 | 35 | double v（雙剪刀手）、heart hands（手比愛心） |
| 服裝狀態 / 脫衣 | 54 | breasts out（露胸）、clothing aside、see-through clothes |
| 姿勢 / 體位 | 38 | top-down bottom-up、m legs（M 字腿）、all fours |
| 視角 / 構圖 | 28 | pov、from below、cowboy shot（七分身） |
| 體液 / 事後 | 22 | cum on body、pussy juice、after sex |
| 身體特徵 | 43 | thick thighs、skindentation（陷肉）、tanlines |
| 場景 / 地點 | 28 | on bed、locker room、love hotel |
| 光影 / 質感 | 17 | backlighting（逆光）、motion lines（動態線） |

搜尋框**中英都吃**：打 `ahegao`、`阿嘿顏`、`愛心` 都找得到。點一下就加到提詞後面，
而且**游標會停在剛加的那個 tag 上**，所以要加權就是再按一下 `Ctrl+↑`。

已經在提詞裡的不會重複加（連加權過的形式也算得出來）。

### 為什麼每個 tag 旁邊有圖片數

**先更正我之前寫錯的一段。** 這份文件原本寫「圖片數 0 的 tag 打了完全等於沒打」——
**那句話是錯的**。你實測 `peace` / `double peace gesture` / `ahegao face` 有效果，是對的。

我後來把 SDXL 自己的文字編碼器（CLIP ViT-L/14）抓下來用 CPU 實跑，
量兩段文字在它的語意空間裡有多近（1.0 = 完全相同；無關的文字大約 0.28～0.34）：

| A | B | 相似度 |
| --- | --- | --- |
| `ahegao face` | `ahegao` | **0.884** ← 幾乎是同一個向量 |
| `breasts out` | `exposed breasts` | 0.826 |
| `soft lighting` | `dim lighting` | 0.715 |
| `double peace gesture` | `double v` | **0.567** |
| `double v` | `1girl standing` | 0.342 ← 無關的基準線 |
| `double peace gesture` | `1girl standing` | 0.280 ← 無關的基準線 |

**底模是 CLIP，它本來就看得懂英文。** 你打 `double peace gesture`，
它不需要 danbooru 有這個 tag 才知道你要 V 手勢 ——「peace」「gesture」這些字
它在原始的四億張圖文預訓練裡就學過了。所以那個詞當然有效果。

### 那圖片數到底在量什麼

**它量的是「這支底模被磨得多利」，不是「有沒有用」。**

NoobAI、Illustrious、Pony 是拿 **danbooru 的 tag 字串**微調的，所以：

- **正式 tag** → 又準又穩，權重 1.0 就吃得到，不容易飄到旁邊的概念
- **自己描述** → 落在大概對的區域，通常還是會出，但**比較鬆、比較不穩，
  常常要加到 1.2 才跟正式 tag 一樣明顯**

兩個都有用，差別在銳利度。清單提供的是「更省事的寫法」，不是「唯一能用的寫法」。

### 有兩種情況差距確實比較大

1. **它是 danbooru 的別名。** `peace_sign` 是 `v` 的**啟用中別名**，
   `double_peace` 是 `double_v` 的別名，`naked` 是 `nude` 的別名。
   別名在匯出訓練標註時會被換成正式名，所以**訓練資料裡從來沒出現過別名本身**。
   這種情況正式名確實明顯比較好（不過 CLIP 還是懂那個英文詞，所以仍然不是零）。
2. **圖片數真的很少。** 幾千張以下的 tag，微調可能沒把它跟鄰近概念分開。
   這份清單裡最弱的是 `disgust`（4,078 張），介面上會標出來。

### chip 深淺的意思

- **深色** = 10 萬張以上，模型很熟，權重不用動
- 中等 = 1 萬～10 萬
- 淺色 = 1 萬以下，**可能要加到 1.2 才明顯**

搜尋打了不在清單裡的字，它會告訴你 danbooru 練過的是哪個字串，
但**不會說你原本那樣打沒用** —— 因為那樣講是錯的。

### 你給我的四個例子

| 你打的 | danbooru 上的狀態 | 建議 |
| --- | --- | --- |
| `breasts out` | ✅ 正式 tag，87,622 張 | **照用**，這個一直都是對的 |
| `ahegao face` | tag 名存在但 0 張 | 有效果（跟 `ahegao` 相似度 0.884），但 **`ahegao`** 更準 |
| `double peace gesture` | 不是 danbooru 的 tag | 有效果（跟 `double v` 相似度 0.567），**`double v`** 更準更穩 |
| `half naked` | tag 名存在但 0 張 | 有效果，但 **`topless female`**（88,273 張）明確得多 |

`peace` / `peace sign` 也一樣：`peace_sign` 是 `v` 的**別名**，
訓練標註裡只會出現 `v`。你打 `peace sign` 還是會出 V 手勢（CLIP 懂），
只是 `v` 對這幾支底模更直接。

### 那些「畫質咒語」

網路教學很愛寫 `soft lighting`、`cinematic lighting`、`dramatic lighting`、
`rim lighting`、`volumetric lighting` —— 這五個 danbooru **都沒有練過**（0 張）。

一樣要講清楚：**這不代表打了完全沒差**。`soft lighting` 跟 `dim lighting`
在 CLIP 裡是 0.715，還是會往那個方向推。只是這幾支動漫底模真正磨利的是這四個：

```
backlighting      45,176 張   逆光
sidelighting      12,879 張   側光
underlighting      1,264 張   底光
dim lighting       1,288 張   昏暗
```

所以清單只提供這四個。至於 danbooru 的**別名**是上面講的第 1 種情況，
已經全部指到正式名：`naked`→`nude`、`see-through`→`see-through clothes`、
`cat pose`→`paw pose`、`presenting`→`presenting own body`、
`erect nipples`→`covered nipples`。

---

## 2.5 常用動作／表情：釘在角色包旁邊

**圖片分頁 → 🎤 角色包**（Hololive 那一塊）最下面多了一排一鍵按鈕，
就是你最常用的那幾個：

```
單手比 V   雙手比 V   露胸   阿嘿顏   阿嘿顏＋雙手 V
上身全裸   下身全裸   蹲馬步（蹲姿張腿）   M 字腿
無表情   厭惡表情   認真表情   高興表情
```

點一下加進提詞，**再點一下拿掉**。已經在提詞裡的會亮起來 ——
而且亮不亮是**直接看提詞框的內容**判斷的，所以你手動改提詞、或角色包重新填入，
按鈕狀態都會跟著對。加完游標就在那個 tag 上，要加權按一下 `Ctrl+↑` 就好。

### 它會跟著底模自動換寫法

這是你要求的「確認每個模型下面都能用」。同一顆按鈕，底模不同送出的字不一樣：

| 按鈕 | NoobAI / Illustrious / Pony | Juggernaut / SDXL 官方 |
| --- | --- | --- |
| 雙手比 V | `double v` | `making a peace sign with both hands` |
| 露胸 | `breasts out` | `bare breasts, breasts exposed` |
| 阿嘿顏 | `ahegao` | `ahegao, eyes rolled back, tongue out, blissful expression` |
| 蹲馬步 | `squatting, spread legs` | `squatting low with legs wide apart, horse stance` |
| 無表情 | `expressionless` | `expressionless, blank face` |

因為 **Juggernaut 和 SDXL 官方底模從來沒學過 danbooru 標籤** —— 它們吃的是
自然句子。三支動漫底模則是反過來。切底模時上面那行字會告訴你現在是哪一種。

滑鼠停在按鈕上會顯示它實際要送出的字，以及 danbooru 圖片數。

### 幾個實際查證的結果

- **`bottomless female` 在 danbooru 是 0 張**，正式 tag 就是 `bottomless`（121,953 張），
  按鈕用的是後者。
- **danbooru 沒有單一的「馬步」tag**（`horse stance` 只有 30 張）。
  實務上是 `squatting` + `spread legs`，按鈕一次加這兩個。
- **`厭惡` 是這幾個裡最弱的**（`disgust` 只有 4,078 張），可能要加權到 1.2 才明顯。
- 高興用 `happy, smile` 兩個一起 —— `smile` 有 412 萬張，是整個 danbooru 最強的表情 tag。

---

## 3. 自訂尺寸可以拉滑桿了

尺寸選 **`自訂尺寸`** 之後，寬高各有一條滑桿，跟數字框**雙向同步**：

- **滑桿**以 **64 為單位**（SDXL 自己的 bucket 步進），拖起來不會卡
- **數字框**維持 8 為單位，要輸入精確值還是可以
- **鎖定目前比例** —— 勾了之後拉一邊，另一邊跟著動
- **常用比例**一鍵：`1:1` `2:3` `3:2` `3:4` `4:3` `9:16` `16:9`

下面那行即時顯示 **實際尺寸 · 百萬像素 · 比例 · 這個尺寸會不會出問題**：

```
1536×1024 · 1.57 MP · 比例 3:2 · 已經超出 SDXL 的所有訓練尺寸（它最大的也只有約 1.05 MP）
                                  —— 開始容易出現雙頭、肢體重複。
```

SDXL 是在**約 100 萬像素**上訓練的，離太遠就會出現雙頭、多手多腳。
要大圖的正確做法是**用正常尺寸生成，再開高解析度放大**，不是直接把尺寸拉大。

比例按鈕會**維持約 100 萬像素**而不是維持目前寬度 —— 不然換個比例就默默走進雙頭區。

### 一個誠實的小細節

按 `9:16` 之後，讀數會顯示 `768×1344 · 比例 4:7 · 你按的是 9:16，對齊 64 之後最接近的就是這個`。

因為在這個像素預算下，**沒有任何 64 的倍數組合剛好是 9:16**。顯示 4:7（真正的比例）
再說明你按的是什麼，比直接印「9:16」騙你要好。

---

## 我驗過什麼

| 驗過 | 結果 |
| --- | --- |
| ComfyUI 只認得 `(x)` / `(x:N)` | 讀 `comfy/sd1_clip.py` 的 `parse_parentheses` + `token_weights` 原始碼 |
| 316 個 tag 的圖片數 | 逐一查 danbooru API；圖片數 <500 的一律不收 |
| 43 組更準的寫法對照 | 每組都確認過左邊是別名或 0 張、右邊是正式 tag |
| 「0 張的字到底有沒有用」 | 把 CLIP ViT-L/14 下載下來用 CPU 實跑，量文字相似度（見上表）——**證明我原本寫的是錯的** |
| 常用按鈕在 5 支底模下各送出什麼 | Chromium 實機切換底模驗證 |
| 權重編輯（Ctrl+↑↓、按鈕、選取、夾限、回到 1.0 移除括號） | Chromium 實機操作驗證 |
| 加了 tag 不重複（含已加權的形式） | 實機驗證（這個 bug 是實機測出來的） |
| 滑桿 ↔ 數字框雙向、比例鎖、比例按鈕、像素警告 | 實機驗證 |
| 手機寬度（375px）全部展開不溢出 | 0px |

**沒驗過的**：權重調到多少「最好看」。那張建議表是社群共識加模型結構的推論，
不是我實測的 —— 這個容器沒有 GPU，這專案至今**一張圖都沒有真的生成過**。

### 關於上面那些相似度數字的但書（第二個模型審查後修正）

我原本寫「實際生成吃的是 token 層隱藏狀態，**不是** pooled」—— **這句話講太死了**。
SDXL 兩個都用：`prompt_embeds`（token 層隱藏狀態，進 cross-attention）
**和** `pooled_prompt_embeds`（進 time embedding）。pooled 有參與生成。

但真正的問題其實更嚴重一點：**SDXL 的 pooled 是從 OpenCLIP bigG 那顆取的，
而我量的是 CLIP-L 的 pooled** —— 所以我測的東西根本不在那條路上。

所以這些數字的正確定位是：**詞義診斷（lexical / semantic diagnostic）**。

- ✅ 足以證明「`double peace gesture` 跟 `double v` 在 CLIP 語意空間裡明顯相關，
  遠高於無關基準」，因此**足以推翻我原本「0 張 = 沒用」的說法**。
- ❌ **不足以**證明 NoobAI / Illustrious / Pony 的 U-Net 對兩者反應相同。
  要證明那個，唯一的辦法是同 checkpoint、同 seed、同 latent、同 sampler、同 CFG、
  同 steps，只換那一個 token，多個 seed 統計成功率。**這個實驗我沒做，這台機器也做不了。**
所以那些數字是**方向性的證據，不是精確的等價度** —— 它足以證明「0 張 ≠ 沒用」，
但不足以宣稱「0.884 就等於一模一樣」。

# 風格靈感庫 / Style Library

一組可以疊在角色提詞上面的「畫面配方」：線條、上色、打光、構圖。
**不是模仿畫師**——畫師另外有一欄，在 [artists.md](artists.md)。

打開方式：圖片分頁 → 提詞框下面的 **風格靈感庫** 按鈕。

---

## 這份清單是怎麼來的（重要）

配方本身是從一份規格書來的。那份規格書的作者沒有看過這個 repo 的程式碼，
也**沒有查過裡面的 tag**。

我把裡面全部 135 個 tag 一個一個丟去 danbooru API 查。結果：

| | 數量 |
|---|---|
| 真的存在的 danbooru tag | 63 |
| 0 張，但是**模型作者訓練時自己塞進 caption** 的詞 | 10 |
| **完全查不到、也不在任何 model card 上的自創詞** | **64（47%）** |

自創的那 64 個包括 `clean lineart`、`dramatic lighting`、`cinematic composition`、
`detailed eyes`、`rim light`、`volumetric lighting`、`cel shading`、
`detailed background`、`glossy skin`、`soft lighting`……全部 0 張。

### 「0 張」不等於「沒用」

這一點在 [prompt-weights.md](prompt-weights.md) 講過，這裡再講一次，
因為它同時有兩個方向會被講錯：

* **底模是 CLIP，看得懂英文。** `dramatic lighting` 打進去一定有效果。
  你自己實測有效，那就是有效。
* **但 danbooru 訓練過的字串更準。** NoobAI / Illustrious / Pony 的 caption
  就是 danbooru 的 tag 字串，那個字串被銳化過——落點更集中、需要的權重更低、
  比較不會飄到旁邊的概念去。

所以規則是：**只要有一個意思相同的真 tag，就出真 tag**。
沒有的就整個拿掉，不留一個看起來很專業但其實是模糊描述的詞。
每一個替換都寫在 `app/styles.py` 的 `REPLACED` 裡面，UI 上也看得到
（配方面板最下面那個摺疊區）。

### 有第三種：caption-time token

這是我自己原本的規則有漏洞的地方，值得單獨寫出來。

`masterpiece`、`best quality`、`worst quality`、`newest` 這些字在 danbooru 上
**也是 0 張**。但它們跟 `clean lineart` 完全不是同一回事——它們是
**模型作者在訓練時自己算出來塞進 caption 的**：

> NoobAI-XL 1.1 model card：
> 分數前 5% → `masterpiece`，5-15% → `best quality`，15-40% → `good quality`，
> 40-70% → `normal quality`，後 70% → `worst quality`。
> 上傳年份 2005-2010 → `old`，2011-2014 → `early`，2014-2017 → `mid`，
> 2018-2020 → `recent`，2021-2024 → `newest`。

這些是**整個提詞裡訓練得最扎實的字**，查 danbooru 的張數對它們毫無意義。

所以 UI 上 tag 分三種顏色：

| 標記 | 意思 |
|---|---|
| `tag  55k` | 真 danbooru tag，後面是圖片數 |
| `tag  caption` | 模型作者訓練時塞的詞，查 danbooru 是 0 張很正常，出處寫在 tooltip |
| `tag  en` | 一般英文，靠 CLIP 讀懂，沒有專門訓練 |

---

## 最該注意的一個替換：`2d`

規格書的「霧面 2D / 去 AI 油亮感」配方推薦 `2d`。

**在 danbooru 上，`2d` 是畫師 `nidy` 的現行別名（409 張）。**

也就是說，在 NoobAI 或 Illustrious 上打 `2d`，你是在點名一位特定畫師的畫風——
跟這個配方想做的事（去掉風格、回到中性平塗）正好相反。

它沒有出貨。那個配方改用 `flat color`（13,671 張）＋ `muted colors`（9,114 張）。

順便：規格書在同一個配方裡放的 `spot color` 是真 tag（62,361 張），
但它的意思是「整張黑白只留一個顏色」，放進去會把圖推向單色。也拿掉了。

---

## 22 組配方

| id | 名字 | 在做什麼 |
|---|---|---|
| `clean-anime-keyvisual` | 清爽官方動畫 Key Visual | 乾淨線條、動畫上色、官方宣傳圖感 |
| `anime-screencap-flat` | 真正動畫截圖感 | 電視動畫的一格，粗線平色 |
| `matte-2d-no-ai-gloss` | 霧面 2D／去 AI 油亮感 | 壓掉皮膚高光和塑膠感 |
| `cinematic-anime` | 電影感動漫 | 淺景深、逆光、黑邊、顆粒 |
| `soft-light-novel` | 柔和輕小說封面 | 柔光、粉彩、亮眼 |
| `gacha-key-art` | 手遊角色 Key Art | 金邊、荷葉邊、首飾、光點 |
| `game-cg` | 高質感遊戲 CG | 比電視動畫細，仍是 2D |
| `dreamy-pastel` | 夢幻粉彩 | 低對比、散景、浮動光點 |
| `golden-hour` | 黃金時刻逆光 | 只加光線，不動人物 |
| `moonlit-blue` | 月夜冷色光 | 夜景、月光、空氣感 |
| `neon-cyberpunk` | 霓虹賽博動漫 | 霓虹、雨夜反射 |
| `dark-fantasy` | 暗黑奇幻插畫 | 明暗對照、霧、火星 |
| `watercolor` | 水彩動漫插畫 | 傳統媒材那一組 |
| `ink-manga` | 墨線漫畫 | 黑白、網點、排線 |
| `retro-90s` | 90 年代動畫 | 舊畫風、顆粒、低飽和 |
| `dynamic-action` | 動態戰鬥構圖 | 姿勢、透視、速度線 |
| `beauty-closeup` | 精緻人物近景 | 像素集中在臉和眼睛 |
| `hair-detail` | 髮絲質感 | 給頭髮一個會動的理由 |
| `environmental-portrait` | 人物＋高資訊背景 | 空間層次、具體場景 |
| `magic-effects` | 魔法特效插畫 | 魔法陣、光軌、氣場 |
| `fashion-portrait` | 時裝人物插畫 | 布料、飾品、乾淨背景 |
| `rainy-cinematic` | 雨夜電影感 | 雨、水窪反光、散景 |

配方會**依底模過濾**：NoobAI / Illustrious 看得到全部 22 組，
Juggernaut 和 SDXL base 只會看到不靠 danbooru 詞彙的那幾組
（電影感、黃金時刻、月夜、霓虹、近景、背景、時裝、雨夜），
而且它們的 tag 會自動換成自然語句的寫法。

---

## 套用時到底做了什麼

**不是** `prompt + ", " + recipe`。這樣做至少會壞四件事：
同一個 tag 用兩種拼法出現兩次、新風格跟舊風格打架、
別的模型的方言留在提詞裡（`score_9` 在 NoobAI 上）、
以及你看不到改了什麼所以你不敢按第二次。

實際流程：

1. **切開**——逗號分隔，但括號裡的逗號不算（`(a, b:1.2)` 是一個 tag），
   跳脫過的括號也不算（角色名 `shenhe \(genshin impact\)` 完整保留）。
2. **比對**——比的是「去掉權重和括號、底線換空格、小寫」之後的形式。
   所以 `(smile:1.3)` 和 `smile` 是同一個 tag。
3. **去重**——**你原本的拼法和權重贏**。配方不會去改你自己打的權重。
4. **換掉衝突的**——只有在下面那張衝突表上的 tag 會被換掉。
5. **清方言**——把不屬於這個底模的品質詞拿掉，逐字比對。
6. **給 diff**——列出加了什麼、換掉什麼、清掉什麼，**你按確認才寫進提詞框**。

兩條規則是硬的：

* **你的 tag 贏。** 已經在提詞裡的字，拼法和權重都不動。
* **不認得的東西一律不碰。** 角色名、LoRA 觸發詞、`{紅|藍}` 萬用字、
  你自己發明的詞，全部原封不動送出去。
  一個會吃掉 LoRA 觸發詞的提詞工具，比沒有提詞工具還糟。

面板上有個 **保留目前畫風** 的勾選，勾了就連第 4 步也不做。

---

## 衝突表是量出來的，不是講出來的

規格書給的是一個「群組」清單——同一組裡面每個字都跟其他字互斥。
那樣寫錯了兩次：`monochrome` 和 `greyscale` 是同一件事，
`photorealistic` 是 `realistic` 的子集。照那樣做，這兩對都會互相刪掉對方。

所以這裡的衝突有**邊**：同一邊共存，跨邊才互斥。
而且除了「一張圖只有一個上傳年份、一個分級」這兩個先天互斥的以外，
其他三組都是去 danbooru 數出來的。

`lift` ＝ 兩個 tag 實際共現次數 ÷ 假設互相獨立時的期望次數。
底數是 2026-08-23 當天 danbooru 的 12,003,162 張圖。

**同一邊（會一起出現）**

| 組合 | lift | |
|---|---|---|
| `monochrome` + `greyscale` | 14.2× | 同一件事 |
| `monochrome` + `spot color` | 9.8× | spot color 是單色加一點顏色 |
| `realistic` + `photorealistic` | 370× | 全部 1,750 張 photorealistic 都是 realistic |
| `portrait` + `close-up` | 11.2× | 一起用很正常 |

**跨邊（互斥）**

| 組合 | lift |
|---|---|
| `greyscale` + `pastel colors` | 0.007× |
| `monochrome` + `anime coloring` | 0.011× |
| `anime coloring` + `realistic` | 0.033× |
| `monochrome` + `pastel colors` | 0.072× |
| `3d` + `flat color` | 0.15× |
| `3d` + `anime coloring` | 0.21× |
| `flat color` + `realistic` | 0.22× |

**規格書會弄成衝突、但量出來根本不衝突的**

| 組合 | lift | |
|---|---|---|
| `anime coloring` + `flat color` | 0.57× | 兩個一起出貨沒問題 |
| `portrait` + `upper body` | 0.64× | 沒問題 |
| `muted colors` + `pastel colors` | 2.2× | 反而是會一起出現 |

最後一組特別重要：**取景／構圖的 tag 完全不在衝突表裡**。
Illustrious 的 model card 說的是「不要**濫用** `close-up`、`cowboy shot`」，
不是「不能一起用」，數據也同意。那件事放在提詞健康度當提醒，不是在這裡當刪除。

---

## 品質預設

跟風格配方**分開**——配方改的是畫面長相，品質預設是底模自己的鷹架。
兩個混在一起，就是為什麼有人的提詞裡有九個品質詞而且說不出為什麼。

每一串都是從 model card 抄的，不是社群口耳相傳的：

| 預設 | 適用 | 正面 | 出處 |
|---|---|---|---|
| NoobAI 官方建議 | noobai | `masterpiece, best quality, newest, absurdres, highres` | NoobAI-XL 1.1 card 的範例提詞 |
| Illustrious 官方建議 | illustrious | `masterpiece, best quality` | Illustrious-XL v0.1 card |
| Pony 官方 score 串 | pony | 完整六個 `score_*` | Pony V6 官方頁 |
| 極簡 | 動漫系 | `masterpiece` | 品質詞表的最上一格 |
| 去 AI 塑膠感 | 動漫系 | `anime coloring, flat color` | 本專案，全部查證過 |

### 一個查證出來的修正：Illustrious 的品質詞

這個 app 之前給 Illustrious 的預設前綴是
`masterpiece, best quality, amazing quality, very aesthetic`。

去看它自己的 model card，上面白紙黑字寫：

> The model supports quality tags such as: "worst quality," "bad quality,"
> "average quality," "good quality," "best quality," and "masterpiece (quality)."

**沒有 `amazing quality`，沒有 `very aesthetic`。**
那兩個是 WAI-NSFW-illustrious 和 Animagine 這些**微調**自己加的詞，
不是 base Illustrious 的。已經改掉了。

同一張 card 還給了兩件本來不知道的事：

* 它的官方負面裡有 `displeasing` / `very displeasing`——
  這也是 caption-time token，danbooru 上 0 張。
* 它的官方負面裡有 `comic`、`monochrome`、`greyscale`、`2koma`、`4koma`、
  `multiple views`。這個 app 把這幾個拿掉了，不然墨線漫畫那組配方就永遠出不來。

---

## 提詞健康度（Prompt Doctor）

提詞框下面那一行。每次改提詞、改負面、改尺寸都會重算。

會講的事，以及它憑什麼講：

| 檢查 | 依據 |
|---|---|
| **畫布太小**（512² 配 SDXL） | SDXL 訓練在 ~1024²。這通常才是「圖很爛」的真正原因，比提詞長度重要得多 |
| 畫布太大（>2.6 倍原生面積） | SDXL 直接生成大圖容易雙頭、多手 |
| Pony 的 `score_*` 出現在別的模型上 | 那是 Pony 訓練時自己加的 caption，別的模型沒有 |
| Pony 少了 `score_*` | Pony 官方頁：只用 `score_9` 效果比完整六個弱很多 |
| `8k` / `ultra detailed` / `trending on artstation` | 沒有任何一張 anime model card 列過。不會壞事，但會稀釋真正有用的詞 |
| 品質詞超過 6 個 | NoobAI 一張圖只會被貼到**一個**品質詞（五選一），堆再多是重複講同一件事 |
| 這個模型的 card 沒列過的品質詞 | 例如 Illustrious 上的 `amazing quality` |
| 同一個字同時在正面和負面 | 自己抵銷自己 |
| 提詞內部互相衝突 | 上面那張量過的 lift 表 |
| 重複的 tag | 重複 ≠ 加權（ComfyUI 是逗號切開各自 tokenise），要加權請用 `(tag:1.2)` |
| 三個以上的取景 tag | Illustrious card 自己的提醒 |
| 畫師標籤的寫法不合這個模型 | NoobAI 用 `artist:name`、Illustrious 用 `by name`、Pony 訓練時把畫師名拿掉了 |
| 沒有 `1girl` / `1boy` / `no humans` | danbooru caption 幾乎每張都以這個開頭，少了人數會跑掉 |

有 **移除 / 改尺寸 / 補上** 的按鈕，按下去直接改提詞框或畫布。

### 它不會講的事

它**不會**說「這樣會好看」或「這樣會難看」。
每一條都是可以去查的規則——某張 model card 上的一句話，或 danbooru 上的一個數字。

因為這個專案**從來沒有生成過任何一張圖**——開發用的機器沒有 GPU。
所有跟「畫面品質」有關的東西都還是假設。想把假設變成量測，
用 [experiments.md](experiments.md) 的固定 seed 掃描＋盲測。

---

## 檔案

| 檔案 | 是什麼 |
|---|---|
| `app/styles.py` | 22 組配方、115 個查證過的 tag、5 組品質預設、71 條替換紀錄 |
| `app/promptmerge.py` | 切詞、比對、去重、衝突、清方言、diff |
| `app/promptdoctor.py` | 健康度檢查 |
| `GET /api/styles?model=` | 全部配方＋預設＋替換表 |
| `GET /api/styles/search?q=&model=` | 搜尋 |
| `POST /api/styles/apply` | 套用，回傳合併結果＋diff（不會自己寫進任何地方） |
| `POST /api/styles/remove` | 把指定的 tag 拿掉 |
| `POST /api/prompt/check` | 健康度 |

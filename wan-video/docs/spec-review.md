# 對「Prompt 靈感庫 / Style Explorer」規格書的審查回覆

> 對象：`CLAUDE IMPLEMENTATION BRIEF — Anime Prompt Recommendation / Style Explorer`（2,195 行）
> 分支：`claude/local-image-to-animation-ai-375zyw`　日期：2026-08-23
>
> 這份要回給規格書的作者再審一輪。想直接跳到「哪裡有問題」請看第 2 節。

規格書一開頭就寫「先做 repository inspection，禁止一上來就重寫 UI」——
這條照做了，而且順便照它自己的精神多做了一件它沒要求的事：
**把它列的每一個 tag 都拿去 danbooru API 查過**。
規格書自己也承認作者沒有看過原始碼；查完之後可以再加一句，
作者也**沒有查過自己寫的 tag**。

---

## 1. 做了什麼

| | |
|---|---|
| `app/styles.py` | 22 組風格配方、115 個查證過的 tag、5 組品質預設、71 條替換紀錄 |
| `app/promptmerge.py` | 切詞／比對／去重／衝突／清方言／diff |
| `app/promptdoctor.py` | 13 項提詞健康度檢查 |
| `app/static/index.html` | 風格庫面板、diff 確認框、健康度那一行 |
| `app/server.py` | `/api/styles`、`/api/styles/search`、`/api/styles/apply`、`/api/styles/remove`、`/api/prompt/check` |
| `docs/style-library.md` | 使用者文件，含全部量測數字 |
| 測試 | Python 2,666 項（其中 99 項是這次新增的）、Chromium 169 項（新增 31 項） |

**沒有做的，以及為什麼**（規格書第 5、6、25、29 節）：

* **ThetaCursed 16k 畫師 pack**（§5、§6）——約 900MB 的外部預覽圖。
  這台機器上沒辦法驗證它的內容，也沒辦法確認授權範圍。
  現有的 `app/artists.py` 是 52 位、每一位都查過 danbooru 圖片數和特徵 tag 的清單，
  在能實際跑生成之前，把它換成一份沒驗證過的 16k 清單是往回走。
* **CLIP 相似畫風搜尋**（§25）——需要對整個畫師庫跑 embedding。
  沒有 GPU，而且在能生成之前無從驗證結果對不對。
* **拖曳排序 chips**（§29）——規格書自己標「有餘力再做」。
* **Preview 圖**（§22、§23）——這個專案**從來沒有生成過任何一張圖**。
  放假的預覽圖比沒有預覽圖糟。

---

## 2. 規格書裡查證後不成立的地方

### 2.1 135 個 tag 裡有 64 個（47%）在 danbooru 上不存在

全部丟 `https://danbooru.donmai.us/tags.json?search[name_matches]=` 查過：

| | 數量 |
|---|---|
| 真的存在 | 63 |
| 0 張，但是 model card 上的 caption-time token | 10 |
| **完全不存在，也不在任何 model card 上** | **64** |

不存在的包括：`clean lineart`、`delicate lineart`、`cel shading`、`simple shading`、
`soft shading`、`subtle shading`、`soft skin shading`、`matte colors`、
`rim light`、`rim lighting`、`warm rim light`、`dramatic lighting`、
`volumetric lighting`、`volumetric fog`、`studio lighting`、`soft lighting`、
`soft glow`、`colored lighting`、`dynamic shadows`、`long shadows`、`harsh shadows`、
`catchlight`、`subtle highlights`、`light reflecting on hair`、
`detailed eyes`、`detailed face`、`face focus`、`detailed background`、
`detailed fabric`、`detailed hair strands`、`flyaway hair`、`intricate costume`、
`clean background`、`background`、`foreground`、
`balanced composition`、`cinematic composition`、`dynamic composition`、
`dramatic perspective`、`perspective in effects`、`environmental storytelling`、
`floating particles`、`glowing particles`、`energy trails`、
`light novel illustration`、`fashion illustration`、`retro anime`、`cel animation`、
`dark fantasy`、`dreamy`、`elegant`、`glossy skin`、`oily skin`、`plastic`、`cgi`、
`oversaturated`、`harsh contrast`、`full color`、`static pose`、`wet street`、
`reflections`（少一個 s——單數 `reflection` 有 55,899 張）、`worst detail`。

**這不代表它們沒用**——底模是 CLIP，看得懂英文，這一點在
`docs/prompt-weights.md` 裡有量測支撐，而且是使用者實測打臉我之後補的。
但規格書自己在 §1.1 主張「Prompt 必須 model-aware」、
在 §39.4 主張「artist style 影響非常大」，這兩個主張的前提都是
**這些模型是拿 danbooru tag 字串訓練的**。
既然如此，同一份文件裡有 47% 的推薦 tag 不是 danbooru 字串，
就跟它自己的論證衝突。

處理方式：**有意思相同的真 tag 就換成真 tag，沒有就整個拿掉**，
71 條替換全部寫在 `styles.REPLACED` 裡面，UI 上也看得到。

### 2.2 `2d` 是畫師 `nidy` 的別名（這條最嚴重）

規格書的 `matte-2d-no-ai-gloss` 配方第一個 chip 就是 `2d`。

```
GET /tag_aliases.json?search[antecedent_name]=2d
  -> consequent_name: "nidy"        (409 posts)
```

在 danbooru 訓練的模型上打 `2d`，是在點名**一位特定畫師**。
這個配方的目的是「去掉 AI 的塑膠味、回到中性平塗」——
結果它會給你 nidy 的畫風。**沒有出貨。**

### 2.3 `spot color` 是真 tag，但意思相反

同一個「霧面 2D」配方裡的 `spot color`（62,361 張）意思是
「整張黑白只留一個顏色」。放進去會把圖推向單色。移除。

### 2.4 NoobAI 的年代桶是五格不是六格

§15 的 `CONFLICT_GROUPS` 寫
`["newest", "recent", "mid", "early", "old", "oldest"]`。

NoobAI-XL 1.1 的 model card 只有五格：
`old` 2005-2010、`early` 2011-2014、`mid` 2014-2017、`recent` 2018-2020、
`newest` 2021-2024。**沒有 `oldest`。**

### 2.5 `newest` 被當成品質詞用在負面

`retro-90s` 配方把 `newest` 放進 negative。
`newest` 是**年代桶**不是品質詞。想要舊畫風，正面直接寫 `old` 或 `early`，
那才是它訓練時的用法。（這個錯誤這個 repo 自己也犯過，
上一輪 Codex 審查抓到的，見 `docs/review-response.md`。）

### 2.6 衝突群組用「平面群組」表示，會讓同義詞互相刪除

§15 給的是一串扁平陣列，語意上等於「同一組裡每個字都跟其他每個字互斥」。
照這樣做：

* `["monochrome", "greyscale", "full color"]` → `monochrome` 會刪掉 `greyscale`。
  可是這兩個在 danbooru 上共現 **684,962** 次（lift 14.2×），是同一件事。
* `realistic` 跟 `photorealistic` 如果放同一組 → 互相刪除。
  可是 `photorealistic` 的 1,750 張**全部**都是 `realistic`（lift 370×）。

改成有「邊」的結構：同一邊共存，跨邊才互斥。

另外規格書的 `["flat color", "hyperrealistic shading"]` 裡，
`hyperrealistic shading` 不存在；`["anime screencap", "photorealistic"]` 裡
`anime screencap` 是 `anime_screenshot` 的別名。

### 2.7 衝突關係全部改成量出來的

不是用講的。lift ＝ 實際共現 ÷ 獨立假設下的期望，
底數是 2026-08-23 的 12,003,162 張 danbooru 圖片。

**互斥（採用）**：`greyscale`+`pastel colors` 0.007×、
`monochrome`+`anime coloring` 0.011×、`anime coloring`+`realistic` 0.033×、
`monochrome`+`pastel colors` 0.072×、`3d`+`flat color` 0.15×、
`3d`+`anime coloring` 0.21×、`flat color`+`realistic` 0.22×。

**同一邊（不互斥）**：`monochrome`+`greyscale` 14.2×、
`monochrome`+`spot color` 9.8×、`realistic`+`photorealistic` 370×、
`portrait`+`close-up` 11.2×。

**規格書會判成衝突、量出來不衝突的三組**：
`anime coloring`+`flat color` 0.57×、`portrait`+`upper body` 0.64×、
`muted colors`+`pastel colors` **2.2×**（反而是會一起出現）。

最後這組讓 §15 的取景群組整個從衝突表拿掉了。
Illustrious 的 card 說的是「不要**濫用**」，不是「不能一起用」——
所以它變成提詞健康度的一條提醒，不是一個刪除動作。

### 2.8 Illustrious 的品質詞抄錯了（這條 repo 自己也錯）

規格書 §8 給 `waiOfficialLike` 是
`masterpiece, best quality, amazing quality`，負面 `bad quality, worst quality,
worst detail, sketch`，而且把它套用在 `["wai", "illustrious"]` 兩個上。

去看 base Illustrious-XL v0.1 自己的 model card：

> The model supports quality tags such as: "worst quality," "bad quality,"
> "average quality," "good quality," "best quality," and "masterpiece (quality)."

**沒有 `amazing quality`。** 也沒有 `very aesthetic`（那是 Animagine 的）。
`worst detail` 更是不在任何 card 上。
`amazing quality` 是 **WAI-NSFW-illustrious 這個微調自己加的**，
規格書把微調的方言掛到 base 上了。

這個 repo 的 `app/images.py` 之前也是抄同一串，一起改掉了。

同一張 card 另外讀到兩件事，都用上了：

* 官方負面有 `displeasing` / `very displeasing`——danbooru 上 0 張，
  是 Illustrious 自己的 caption-time token。
* 官方負面有 `comic`、`monochrome`、`greyscale`、`2koma`、`4koma`、`multiple views`。
  這個 app 把這幾個拿掉，否則墨線漫畫配方永遠出不來。
  （規格書的 `ink-manga` 配方正面第一個字就是 `manga`，
  而 `manga` 是 `comic` 的別名——等於直接撞上 Illustrious 官方負面。）

### 2.9 §20.5「AI gloss」推薦的四個詞有三個不存在

`cel shading` 0 張、`glossy skin` 0 張、`plastic skin` 只有 28 張。
換成 `flat color`（13,671）跟 `shiny skin`（**156,524**）。
`shiny skin` 是 danbooru 真正在用來標「油亮皮膚」的字，
規格書完全沒提到它。

---

## 3. 規格書講對、而且很有價值的地方

不是每一條都要挑毛病，這幾條是這次最值得做的東西：

* **§20.3 SDXL resolution 警告。** 這是整份規格書最有用的一句話。
  「圖很爛」最常見的真正原因就是 512² 配 SDXL，而這件事光讀提詞看不出來。
  做成健康度裡等級最高的一條，附一鍵改尺寸。
* **§11「Quality Presets 不要跟 Style Recipe 綁死」。** 完全同意，照做。
* **§12「禁止 `setPrompt(prompt + ", " + recipe)`」** 以及後面 parse / normalize /
  dedupe / conflict / cleanup / diff 那一串。這是整份規格書架構上最對的一段。
* **§16「不要在使用者沒要求時自動移除他的 LoRA trigger」。**
  這條寫進測試了：merge 對付一個塞滿 `my_lora_trigger`、`{紅|藍}` 萬用字、
  加權過的 tag 的提詞，全部原樣送出。
* **§39.1「Resolution 可能比多 20 個 prompt words 更重要」。** 對。
* **§7「不要把 artist tags 與品質配方混為一談」。** 對，兩者在 UI 上分開。
* **§39.5「不要預設混十個 artists」。** 對。

---

## 4. 給下一輪審查的具體問題

請針對這幾點回，其他地方對就不用附和：

1. **lift 門檻。** 我用 lift ≤ 0.25 判定互斥、≥ 5 判定同一邊，中間留白不動。
   這兩個門檻是我拍的。有沒有更站得住腳的定法？
   還有，danbooru 的共現統計能不能代表「模型訓練後的行為」？
   我認為它是**先驗**不是**量測**，這樣講夠不夠保守？

2. **caption-time token 這一類。** 我把 tag 分成 danbooru / caption / plain 三種，
   理由是 `masterpiece` 跟 `clean lineart` 同樣是 0 張，但完全不是同一回事。
   這個分類有沒有漏掉第四種？
   （例如 e621 那邊帶進來的字——NoobAI 有吃 e621 資料集。）

3. **`game asset` 這個代換。** `game cg` 是 `game_asset` 的別名（169,726 張），
   但 `game_asset` 涵蓋立繪、介面素材、精靈圖，不只是過場 CG。
   換過去是對的嗎？還是應該整個拿掉？

4. **`ink-manga` 配方沒有放 `comic`。** 理由是 Illustrious 官方負面有它，
   而且它會讓畫面變多格分鏡。但 `comic` 有 724,516 張、
   而我放的 `ink (medium)` 只有 974 張。取捨對嗎？

5. **健康度的「品質詞超過 6 個」門檻。** 這個數字也是我拍的。
   NoobAI 一張圖只會被貼到一個品質詞，照這個邏輯門檻應該更低（3？），
   但實務上大家都會同時寫 `masterpiece, best quality, absurdres, highres`（4 個）。
   6 是不是太寬鬆？

6. **最大的那個洞：什麼都沒生成過。**
   這台機器沒有 GPU，所以上面每一條關於「畫面會變怎樣」的話都是推論。
   `docs/experiments.md` 裡有一台固定 seed 掃描＋盲測的機器可以把推論變量測，
   但還沒有跑過。在能跑之前，這份東西應該再加什麼保留？

---

## 5. 已知的、還沒解決的問題

寫出來免得下一輪又被當成新發現：

* **沒有生成過任何一張圖。** 上面第 6 點。
* **danbooru 的數字是 2026-08-23 抓的**，會隨時間變。沒有做自動更新。
* **`golden hour` 只有 380 張、`atmospheric perspective` 359 張、
  `chiaroscuro` 436 張**——這幾個是配方裡最薄的 tag。有標出來，但沒有拿掉，
  因為它們是真 tag 而且沒有更好的替代。
* **自然語言版本的拼法（`natural=`）沒有任何驗證。**
  它們是我寫的英文句子，給 Juggernaut / SDXL base 用的。
  這些字沒有 danbooru 數字可查，也沒生成過。
* **`REPLACED` 是人工維護的表。** 測試會檢查已知的自創詞不會偷偷回來，
  但如果將來新增一個新的自創詞，測試抓不到。

# 本機 AI 影像工作台

**圖生影片**（丟圖 + 指令 → 幾秒動畫）、**文生圖片**（打提詞 → 圖）和**漫畫分鏡**（一格到六格，全彩，對白是真的字）三條線，共用一套模型、LoRA 和素材管理。**完全在你自己的機器上跑** —— 裝好之後
不需要網路、不需要帳號、不需要透過任何人。圖片和成品都不會離開你的電腦。

模型也在網頁上直接選跟下載，不用回命令列。

---

## 一、包了哪些模型

網頁的「模型管理」分頁按一下就下載，下載完就出現在「生成」分頁的下拉選單裡。

| id | 模型 | 顯存 | 下載 | 特點 |
| --- | --- | --- | --- | --- |
| `wan22-14b-fp8` | Wan 2.2 I2V 14B fp8 | 24GB | 38GB | **畫質最好，NSFW 生態最完整** |
| `wan22-14b-q8` | Wan 2.2 I2V 14B GGUF Q8 | 16GB | 40GB | 接近 fp8 |
| `wan22-14b-q4` | Wan 2.2 I2V 14B GGUF Q4_K_M | 12GB | 29GB | 12GB 顯卡的主力 |
| `wan22-5b` | Wan 2.2 TI2V 5B | 12GB | 18GB | 輕量、原生 720p、快 |
| `hy15-480p` | HunyuanVideo 1.5 480p fp8 | 10GB | 22GB | **最省顯存**，人臉物理自然 |
| `hy15-720p` | HunyuanVideo 1.5 720p fp8 | 12GB | 22GB | |
| `hy15-720p-hq` | HunyuanVideo 1.5 720p fp16 | 20GB | 30GB | 官方設定，品質優先 |
| `ltx23` | LTX-2.3 22B | 24GB | 43GB | 影音同步，**只下載檔案**（見下） |

共用元件（文字編碼器、VAE）只會下載一次，所以第二個同家族的模型會小很多。

### 為什麼是這幾個

Wan 2.2 是本地 NSFW 圖生影片的首選，理由是三個條件的交集：

- **開源權重**：Wan 官方開源**到 2.2 為止就停了**。2.5 / 2.6 / 2.7 只有雲端 API，沒有權重檔。
  網路上寫「Wan 2.6 開源可自架」的文章是錯的 —— 要本地跑，上限就是 2.2。
- **授權**：Apache 2.0（HunyuanVideo 有商用限制，LTX 是自訂社群授權）。
- **NSFW 不是靠「解鎖」而是靠生態**。ComfyUI 本身沒有內容過濾器，這些基礎模型也沒有內建
  拒絕機制 —— 真正的差別是社群為 Wan 2.2 訓練的 LoRA 遠多於其他模型。

HunyuanVideo 1.5 放進來是因為它的主模型只有 8.3GB，10GB 顯卡也跑得動，而且人臉和物理
比較自然。NSFW 生態比 Wan 少，但當備選很有用。

### LTX-2.3 為什麼只下載檔案

LTX-2.3 官方的圖生影片流程是一個約 50 個節點的圖：兩段取樣、latent 上採樣、影音共用
latent、還有一個改寫提詞的 LLM 節點。我可以下載它全部的檔案（包含那個
`gemma-3-12b-it-abliterated` 未閹版文字編碼器），但**用程式重建那張圖會是猜的，而我沒有
顯卡可以驗證猜得對不對** —— 所以我沒把它做成本頁能跑的模型，那會是在賣沒驗證過的東西。

檔案下載完之後，在 ComfyUI（<http://127.0.0.1:8188>）用
**Workflow → Browse Templates → LTX-2.3 Image to Video**，那是官方維護、一定對的流程。

---

## 二、你需要什麼硬體

必須是 **NVIDIA** 顯卡（AMD / Intel / 內顯都跑不動）。

### 顯存數字是建議值，不是門檻

上表的顯存欄位是「順順跑」需要的量，**不是能不能跑的界線**。顯存不夠時 ComfyUI 會把
權重換到系統記憶體，一樣跑得出來，只是慢。這套 app **不會**因為顯存小而拒絕任何模型 ——
它會讀你的實際顯卡，告訴你差多少、大概慢幾倍、該加哪個參數，然後讓你自己決定。

| 你的顯存 vs 建議值 | 加什麼 | 大概 |
| --- | --- | --- |
| 夠 | 不用加 | 正常速度 |
| 約一半 | `COMFY_ARGS=--lowvram` | 慢 2～4 倍 |
| 遠低於 | `COMFY_ARGS=--novram` | 慢 5 倍以上，但能跑 |

一支 5 秒 480p：顯存充足的 24GB 卡約 1～3 分鐘；12GB 卡約 6～12 分鐘。
720p 大約是 480p 的 2～3 倍。上面是開了 4 步 Lightning 加速的數字。

**磁碟**：一個模型 18～43GB，可以裝多個（共用元件不會重複下載）。**記憶體**：建議 32GB
—— 如果你要靠 `--lowvram` / `--novram` 跑大模型，系統記憶體就是替代顯存的那塊，越多越好。

安裝腳本會依顯存挑一個「順順跑」的模型當起點，但你隨時可以在網頁上裝更大的來試。

---

## 三、安裝

### Windows（推薦你走這條）

> **沒用過命令列的話,看這份逐步教學**:[docs/windows-tutorial.md](docs/windows-tutorial.md)
> —— 從「怎麼確認自己的顯卡行不行」開始寫,命令列只有兩行。

1. 先裝 **Python 3.12**（<https://www.python.org/downloads/>，安裝時**務必勾
   「Add python.exe to PATH」**）和 **Git**（<https://git-scm.com/download/win>，一路 Next）。
2. 下載這個資料夾，在裡面按右鍵 →「在終端中開啟」。
3. 貼上這行，按 Enter，然後去做別的事：

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1
   ```

   它會依顯存自動挑一個模型下載。想自己指定：`-Model hy15-480p`。
   想先只裝程式、模型稍後在網頁上挑：`-SkipModels`。

4. 之後每次要用：

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\start-windows.ps1
   ```

   會跳出兩個黑色視窗（**不要關**），瀏覽器自動開 <http://127.0.0.1:8000>。

下載中斷不用怕，重跑會從斷點續傳。

**之後要更新程式**：雙擊 `update.bat`（或 `powershell -ExecutionPolicy Bypass -File
.\update-windows.ps1`）。它下載最新程式碼覆蓋上去，但 `ComfyUI\`、`venv\`、`data\`、
`models\`、`.env` 一律不動，所以模型和成品不會重下。更新後要重啟才生效。
更新是**全有全無**的：它會先確認每個要覆蓋的檔案都寫得進去，只要有一個不行就整個不動，
不會留下一半新一半舊的狀態。跑完最後一行會直接寫 `UPDATE OK` 或 `UPDATE DID NOT COMPLETE`。

> **這個資料夾可以隨便搬。** 所有腳本都用相對路徑，Python 一律用
> `venv\Scripts\python.exe -m pip` 而不是 `pip.exe`（`.exe` 捷徑寫死絕對路徑，搬家就壞）。
> 所以覺得放桌面會被 Windows 擋，直接把整個資料夾拖到 `C:\anim` 就好，模型不用重下。

### Linux + Docker

```bash
cp .env.example .env
docker compose up -d --build     # 加 --profile watch 順便開拖檔模式
```

開 <http://127.0.0.1:8000>，到「模型管理」按下載即可 —— 不必先用命令列抓模型。
需要主機有 NVIDIA 驅動與
[nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)。

### Linux 裸機

```bash
./setup-linux.sh                 # 自動挑模型；或 ./setup-linux.sh wan22-14b-q4 / none
./start-linux.sh                 # 之後每次
```

### 命令列下載模型（可選）

```bash
python3 scripts/fetch-model.py --list           # 看清單
python3 scripts/fetch-model.py hy15-480p        # 下載
python3 scripts/fetch-model.py hy15-480p --check  # 只檢查現況
```

---

## 四、怎麼用

開 <http://127.0.0.1:8000>，上面有七個分頁。

### 影片

圖拖進框裡（或 Ctrl+V 貼上）→ 選模型 → 打指令 → 按「生成」。

- **長度用「秒」選，不是幀**。下拉會直接寫「5 秒（81 幀 @16fps）」——
  幀數是照官方 Wan 範本的公式 `floor(秒 × fps + 1)` 算出來再修成 4n+1 的
- 卡片上會寫**成品實際多長**（秒 + fps）和**這次跑了多久**，兩個都看得到
- 沒下載的模型也在選單裡（標 `·`），選了會出現「先下載這個模型」
- 選到比你顯卡大的模型時只會出現說明，**不會阻止你**

**出片後處理**（「出片後處理」摺疊區，兩個都是畫完之後才做，不吃生成時的顯存）：

| 選項 | 做什麼 | 代價 |
| --- | --- | --- |
| **補幀** | Wan 出來是 16fps，看起來會頓。補 2 倍就變 32fps，動作順很多 | 幾秒，要先下載一個 22MB 的 RIFE |
| **放大成品** | 用 GAN 放大模型把整支影片放大（多半 4 倍） | 幾秒，要先下載一個 ~65MB 的放大模型 |

補幀後卡片上的 fps 會直接寫「@32fps（補幀）」，長度（秒）不變 —— 補幀是讓它變順，
不是變慢動作。

### 圖片

不需要輸入圖，全靠提詞。四個 SDXL 系底模，都是 CivitAI 上實測下載量最高的：

| 底模 | 適合 | 顯存 | 下載 |
| --- | --- | --- | --- |
| **NoobAI-XL v1.1** | **動漫首選**。最新全量 danbooru + e621，**認得 VTuber 角色，也吃畫師標籤** | 8GB | 7.1GB |
| **Illustrious XL** | 動漫 / 插畫，**NSFW LoRA 生態最大** | 8GB | 7.3GB |
| **Pony Diffusion V6 XL** | 動漫 / 多元題材，NSFW 生態第二大 | 8GB | 7.3GB |
| **Juggernaut XL v9** | 寫實照片風 | 8GB | 7.4GB |
| **SDXL 1.0 官方** | 中性基準 | 8GB | 7.3GB |

**每個底模的「眉角」寫在介面上**，這是 ComfyUI 不會告訴你的部分：

- **Pony 的提詞開頭一定要有 `score_9, score_8_up, score_7_up`**，否則畫面會爛 ——
  app 幫你自動加，也可以取消
- **NoobAI 要照它的標籤順序寫**：`1girl, 角色, 作品, by 畫師, 其他標籤`，CFG 5~6、Euler a。
  它是唯一同時**認得角色又認得畫師**的一個 —— 想貼近原畫師畫風就選它
- **Illustrious 要用 danbooru 標籤**（`1girl, long hair, sitting`），句子式描述效果差；
  CLIP skip 要 -2
- **Juggernaut 相反**，要用自然句子描述場景光線，CLIP skip -1、不要品質標籤

可調的東西都有一句話解釋在旁邊。不想調就不用碰，預設值是照每個底模的建議填的。

| 分區 | 有什麼 |
| --- | --- |
| 基本 | 尺寸（含自訂寬高）、一次幾張、種子、步數、CFG、sampler（44 種）、scheduler（9 種）、CLIP skip |
| 以圖生圖 | 放一張來源圖，用「重畫強度」決定改多少 —— 拉桿旁邊會直接寫「0.55 · 保構圖換風格」 |
| 放大與重繪 | 高解析重繪（倍率／重繪強度／步數／用哪種放大）、生成後直接放大 |
| 畫質補丁 | FreeU、PAG、Rescale CFG、分塊解碼（省顯存） |
| LoRA | 每支可以**分開**調「對畫面」和「對文字理解」兩個強度（點 🔗 拆開） |

**批量**：一次最多 16 張，同設定不同種子，一次挑好的。

**提詞語法**（按「提詞語法」看說明）：

- `(字:1.3)` 加重、`(字:0.7)` 減弱 —— 這是 ComfyUI 真的會解析的權重語法
- `{紅|藍|綠}裙子` 每張隨機挑一個，`{2$$長髮|貓耳|眼鏡}` 挑兩個 ——
  **一次生 8 張就是 8 種變化**，按「看看隨機變化」可以先預覽會長怎樣
- 介面上也直接列出 **ComfyUI 不支援** 的寫法（`[字]`、`<lora:名字:1>`、`BREAK`），
  免得你照 A1111 的習慣打完發現沒作用；打了會在送出前就擋下來並說原因

### 看圖猜設定（丟一張圖進來）

圖片分頁右上角有「🔍 看圖猜設定」。丟一張圖進去，它會給你兩種答案 ——
**而且分得很清楚，因為一個是事實、一個是意見**：

**一、檔案裡寫的（精確，不用下載任何東西）**

ComfyUI 存 PNG 的時候會把**整張工作流程**塞進檔案裡（`nodes.py` 裡就是
`metadata.add_text("prompt", json.dumps(prompt))`），A1111 則是寫一段 `parameters`
文字，JPEG 的話藏在 EXIF 裡。所以只要那張圖是這兩者生的，這些全部原封不動讀得出來：

提詞、負面提詞、底模、**每一支 LoRA 和它的強度**、種子、步數、CFG、sampler、scheduler、CLIP skip、尺寸。

它還會告訴你**那些 LoRA 你有沒有裝**，沒裝的直接附一個 CivitAI 搜尋連結。
按「套用到下面的設定」就全部帶進表單，按生成就是重畫同一張。

**二、看圖猜的（要下載一個約 380MB 的分析模型）**

如果那張圖沒帶參數（截圖、別人轉貼過、或根本是照片），就改用 **WD ViT v3 tagger** ——
動漫圈在用的那支 danbooru 標籤模型，在 app 裡直接跑，不用裝 ComfyUI 外掛。
它會列出一串 danbooru 標籤，**直接就是可以貼進提詞框的格式**（底線換成空格、
括號自動跳脫，不然 `rem_(re:zero)` 裡的括號會被 ComfyUI 當成加權語法）。
順便會判斷分級（全年齡／擦邊／成人），以及該用動漫底模還是寫實底模。

> **關於「猜 LoRA」要說實話**：從像素**沒辦法**反推是哪一支 LoRA 畫的，沒有任何工具做得到。
> 只有在檔案自己寫了 LoRA 名字的時候才會報出來，那是「讀」不是「猜」。
> 另外它會列出「你裝的 LoRA 裡，觸發詞和畫面對得上的有哪些」當參考 ——
> 介面上也直接寫明這只是詞對得上，不代表原圖就是用它畫的。

### 漫畫分鏡（全彩，支援 NSFW）

圖片分頁上方有「單張圖片 / 漫畫分鏡」兩個模式。切到漫畫分鏡，選一個版型，**每一格自己寫要畫什麼**，按「畫這一頁」。

| 版型 | 格數 |
| --- | --- |
| 1 格（單張 / 橫幅） | 1 |
| 2 格（上下 / 左右） | 2 |
| 3 格（直排 / 上大下兩小） | 3 |
| 4 格（田字） | 4 |
| **4 格（日式四格）** | 4 |
| 6 格（2×3） | 6 |

它是這樣做的，每一步都有理由：

- **不用另外裝漫畫模型。** 你已經裝的 Illustrious / Pony 就是拿 danbooru 訓練的，
  而 danbooru 上 `comic` 有 **72 萬張**、`speech_bubble` 51 萬、`4koma` 11 萬 ——
  這些模型本來就會畫分鏡，缺的只是有人幫你把提詞組好。
- **全彩是「排除」出來的，不是「要求」出來的。** 那 72 萬張 `comic` 裡有 **37 萬張同時標了
  `monochrome`** ——所以只寫「comic」有一半機率給你黑白稿。勾著「全彩」時，
  `monochrome, greyscale, sketch, lineart` 會被放進負面詞把它擋掉。想要黑白漫畫風就取消勾選。
- **每一格分開畫，再拼版。** 一張 1024×1024 裡塞四格，每格只剩 512×512，SDXL 在那個尺寸會糊掉。
  所以每格都用**接近 100 萬像素、而且符合那一格形狀**的尺寸單獨算（寬格用 1344×768，
  直格用 832×1216），畫完才縮進版面。格線和間距是真的幾何圖形，不是模型手抖畫出來的。
- **對白是真的字。** SDXL 不會寫字，它畫出來的一定是亂碼 —— 所以模型那邊被告知「不要畫文字」，
  對白由程式在事後用真正的字型畫上去，中文一樣清楚。每格可以放一句，位置六選一，
  尾巴會自動指向格子中央。
- **共用提詞**填一次（`1girl, long black hair, red dress`），每格都會自動帶上，角色才不會每格都變一個人。

**照著現成的一頁重畫（換角色）** —— 完整教程在 [`docs/comic-restage.md`](docs/comic-restage.md)

漫畫模式上面有「📄 照現成的一頁重畫」。丟一張現成的漫畫頁 + 一張你的角色圖，它會：

1. **量出分鏡** —— 用遞迴 XY-cut 把格線找出來。這是讀這種版面的標準做法：
   格溝是整條的背景色，就從那裡切開，再在每一塊裡面找直的格溝，遞迴下去。
   「上面一大格、下面兩小格」就是這個遞迴的兩層。
2. **看懂每一格在幹嘛** —— 每格單獨丟給 tagger，拿到 danbooru 標籤
3. **把標籤分成「這場戲的」和「這個人的」** —— 運鏡、姿勢、表情、場景、幾個人留下來；
   髮色、瞳色、體型換成你的角色。服裝可以選要跟人走還是跟原頁走
4. **連鏡頭角度一起複製** —— 每一格的原圖會單獨裁下來，經過邊緣偵測交給
   ControlNet 導引那一格的生成。只複製標籤只能得到「一間教室、俯角」；
   加上這個才會得到**那間教室、那個俯角**，只是換了個人。
   （要先下載 ControlNet 模型，2.5GB；沒有的話前三步照樣能用。）
5. 把量到的格子當成一個一次性版型，每格提詞都填好給你，**還可以再改**

**分鏡先出現，格子再一格一格填進來。** 九格的頁面全部讀完要半分鐘，
但版面一秒就回來了 —— 下面有進度條，讀到一半發現分鏡量錯可以直接取消，
不用盯著空白畫面等。

它也會**明講自己在猜哪裡**：吻合度百分比、哪些原角色特徵被換掉了、
哪一格沒有人所以沒套角色，都列出來。遇到斜的格子、破格、滿版單張，它不會硬掰 ——
格溝寬度差太多的時候會直接說「這比較像一張滿版圖」，然後讓你手動挑一個接近的版型。
這是量出來的判斷：本頁所有內建版型的格溝寬度差異是 0.00～0.20，
一張被誤切成六格的滿版圖是 9.97。

> 角色圖請用**畫出來或生出來的角色**，不要放真人照片。

**構圖鎖定（ControlNet）也可以單獨用在一般圖片上** —— 在「進階設定」裡，
選一張參考圖，它就會照著那張的構圖畫別的東西。三個模型可選
（Union Promax 一個檔案包含線稿／深度／姿勢／tile；Canny 只做線稿；
Scribble 抓得最鬆）。全部只用 ComfyUI 核心節點，不需要任何 custom node。

| 旋鈕 | 預設 | 什麼時候調 |
| --- | --- | --- |
| 抓多緊 | 0.75 | 超過 1.0 連原角色體型都會複製過來，反而換不掉人 |
| 管到幾成 | 0.75 | **最重要的一格**。前 75% 照構圖、後 25% 放手畫細節，臉和手會明顯變好 |
| 細線門檻 | 0.4 | 原稿網點多、線很花的時候調高 |

右邊有**即時版面預覽** —— 灰色代表畫面會出現的地方，改對白或格線粗細會馬上重畫，
不用等 GPU 跑完才知道版面對不對。

成品是**一張完整的頁面**，每一格也會單獨存一份，想單獨重畫或重排都拿得到。

**兩個接力按鈕**（在每張成品卡片上）：

- **接著修** —— 拿這張成品當來源圖再畫一次，設定全部帶回來
- **→ 做成影片** —— 直接把這張丟到影片分頁，不用先下載再拖回來
- **同種子微調** —— 種子和所有設定都保持一樣，只改你想試的那一個，做 A/B 對照

### 提詞庫（把你自己的範例收藏匯進來）

如果你手上已經有一份收集了很多範例的文件，直接丟進「提詞庫」分頁就好。
**檔案只在你自己電腦上處理，不會上傳到任何地方。**

支援 `.txt` `.md` `.csv` `.tsv` `.json` `.jsonl` `.docx` `.pdf`。

重點是**它會自己看出你的檔案是怎麼分段的**，因為沒有人寫這種文件的格式是一樣的。
目前認得這幾種，會各試一次然後挑分數最高的：

| 你的檔案長這樣 | 認得 |
| --- | --- |
| 一行一個提詞（標籤流水帳） | ✓ |
| 用空行隔開，第一行是標題 | ✓ |
| `Prompt:` / `Negative:` / `Tags:` 標籤式 | ✓ |
| `---` 或 `===` 分隔線 | ✓ |
| Markdown 標題 + ``` 程式碼區塊 | ✓ |
| 從 A1111 / CivitAI 直接複製的參數區塊 | ✓ 連負面詞和步數、CFG 都讀得出來 |
| JSON 陣列 / JSONL / CSV / TSV | ✓ 自動找 prompt、negative、title、tags 欄位 |

幾個實作上的細節：

- **匯入前一定先給你看抓到什麼**，確認沒問題才存。對別人寫的文件做自動判斷，
  本來就該讓人先看過。
- 「一行一個」和「一段多行」很容易搞混，判斷方式是：如果每一行都自成一個
  逗號分隔的提詞、而且沒有一行以逗號結尾（結尾有逗號代表下一行是接續的），
  就當成一行一個。
- **重複的會自動略過**，所以同一個檔案匯入兩次不會變兩份。
- Windows 常見的 Big5 和 UTF-16 編碼都讀得出來。
- `.docx` 是用標準函式庫拆的（`.docx` 本質是個 zip），不用裝任何額外套件。

進去之後可以搜尋（空白分隔＝要全部符合）、加星號、按一下就**帶進圖片或影片的提詞框**。
也可以整批移除某一個來源檔案匯入的東西。

### 素材庫

所有成品在這裡。**預設只顯示縮圖，點一下才載入影片** —— 卡片多的時候瀏覽器就不會一直在
背景解碼幾十支影片。上面有：

| 控制 | 作用 |
| --- | --- |
| 自動播放 | 打開才會像以前那樣自動循環播放。預設關 |
| 卡片大小 | 140～420px，拉桿即時生效 |
| 只看星號 | 過濾 |
| 種類 | 只看影片 / 只看圖片 / 全部 |
| 清孤兒檔 | 刪掉硬碟上沒有對應紀錄的影片檔 |
| 清空（保留星號） | 刪掉所有沒加星號的成品，**檔案會真的從硬碟刪掉** |

每張卡片可以加星號、下載、「再跑一次」（帶回原本的指令和模型、換新種子）、刪除。
右上角顯示影片數量和佔用空間。這些設定記在瀏覽器裡，下次打開一樣。

**紀錄現在會存到硬碟**（`data/outputs/.history.jsonl`），重啟 app 不會消失。

### LoRA

直接在 app 裡搜 CivitAI，不用開瀏覽器來回複製檔案：

- 搜尋框 + 排序 / 期間，結果附預覽圖、下載數、觸發詞、檔案大小
- **用在哪**：切「影片模型」或「圖片底模」，篩選會跟著換（影片的 LoRA 對圖片沒用，反之亦然）
- **找什麼**：LoRA 或**底模 Checkpoint** —— 想裝 CivitAI 上其他底模也從這裡裝
- **相容範圍**：預設只顯示和你當前模型 base model 完全相符的（Wan 2.2 I2V 有 380+ 支）；
  放寬成「含可能相容」會加上鄰近版本；「全部」不篩
- 「只看 NSFW」和「模糊預覽圖」兩個開關，設定會記住
- 每個檔案一顆「裝」，直接下進 `models/loras/`，已裝的顯示「已裝」
- 下載時同時存一份 `<檔名>.civitai.json`，所以**觸發詞和來源之後還看得到**

**已安裝的 LoRA 是一面預覽圖牆，不是一排檔名**：

- 安裝時會順手把 CivitAI 的示範圖存成 `<檔名>.preview.jpg` 放在權重旁邊 ——
  這是 ComfyUI 自己的慣例，所以你直接開 ComfyUI 也看得到同一張圖
- 沒有預覽圖的（自己丟進去的）可以按「封面」用自己生的圖當封面
- 上面有篩選框，打字就篩（名字、底模、觸發詞都能搜）
- 選 LoRA 時清單旁邊有縮圖，**點觸發詞就會自動加進提詞**並勾選那支 LoRA

**自動偵測更新**：按「檢查更新」會一次看三件事 ——

| 檢查什麼 | 怎麼判斷 | 有更新時 |
| --- | --- | --- |
| 這個 app | 和 git remote 比 | 說「跑一次 `update.bat`」 |
| ComfyUI | 同上 | 說「`git pull` 後重開」 |
| 你裝的 LoRA / 底模 | 用 sidecar 裡的頁面網址問 CivitAI 現在的最新版 | 卡片變黃框 + 一顆「下載新版」 |

結果在伺服器端快取 6 小時，所以重整頁面不會一直去打 CivitAI；三項各自獨立，
其中一項失敗不會影響另外兩項。

> **下載需要 CivitAI API key，搜尋不用。** 到 civitai.com → 右上頭像 →
> Account settings → API Keys 產生一個，填進 `.env` 的 `CIVITAI_API_KEY=`，重啟 app。
> 沒設的話 LoRA 分頁上方會有提示。

### 模型

每個模型的建議顯存、下載大小、安裝狀態，以及**你實際顯卡**的對照建議。按下載會顯示
即時進度、速度、剩餘時間，可以中途停掉再接著下。最上面顯示讀到的顯卡型號與顯存。

分成三區：

- **影片模型** —— 上面那幾個大的
- **放大模型（圖片和影片共用）** —— 4x-UltraSharp / RealESRGAN / Remacri /
  UltraSharpV2，每個 ~65MB。旁邊寫清楚各自適合什麼（銳利 vs 柔和 vs 皮膚紋理）
- **補幀模型（影片用）** —— RIFE 4.26（22MB，通用首選）／RIFE 4.25 heavy／FILM

### 設定

現況一覽（ComfyUI 狀態、各個目錄、`COMFY_ARGS`、有沒有 CivitAI key），以及常見的
`.env` 改法。

### 指令怎麼寫

這些模型吃「描述動作與鏡頭」的句子，中英文都行：

```
她慢慢轉頭看向鏡頭，長髮被風吹動，鏡頭緩慢推近
he raises the glass and drinks, warm candlelight flickering, slow dolly in
```

寫得越具體越穩。不要只寫「讓它動起來」——那會得到隨機的漂移。想固定結果就把 seed
從 -1 改成一個數字，同樣的圖 + 指令 + seed + 模型會得到同樣的片子。

### 拖檔案模式（批次）

不想開瀏覽器就用這個：圖片丟進 `data/inbox/`，成品自己出現在 `data/outputs/`。

- 指令放在同名的 `.txt`（`cat.png` → `cat.txt`）
- 沒有 `.txt` 的話，**檔名本身就當指令**（`她轉頭看鏡頭.png` 會照著做）
- 處理完的原圖搬到 `data/inbox/done/`
- 用哪個模型看 `.env` 的 `WATCH_MODEL`（留空就用 `MODEL`）

啟動：Windows `start.bat -Watch`、Linux `./start-linux.sh --watch`、
Docker `docker compose --profile watch up -d`。

## 五、加 LoRA（畫風 / 題材 / NSFW）

基礎模型本身沒有內容過濾，但要特定題材的品質，靠的是 LoRA。

**最省事的做法是用 app 內建的 LoRA 分頁**（見上）—— 搜尋、看預覽、一鍵安裝，
觸發詞也會一起存下來。需要一個 CivitAI API key 才能下載。

### 實驗模式 —— 教程在 [`docs/experiments.md`](docs/experiments.md)

**素材庫分頁**多了「實驗（固定 seed 掃參數）」。這個 app 講的所有「最佳參數」
目前都還是**推測**（一張圖都沒生成過），這裡把推測變成量測：

- 選要掃的軸（LoRA 強度／重繪強度／CFG／步數／底模／官方風格偏移／畫師權重／sampler）
- **每個組合都跑同一批 seed** —— 不然量到的是骰子不是參數
- 記下 checkpoint 與 LoRA 的 **SHA256**、ComfyUI 與 app 的 commit（檔名會被重複使用）
- 跑完並排看，然後**蓋住設定盲測投票**，左右順序隨機
- **「好看」和「像本人」分開計分** —— 漂亮但不像的圖不該在「像不像」贏

跑完之後，文件裡標成 HEURISTIC 的建議值你都能自己換成實測結果。

### 官方參考圖 —— 教程在 [`docs/reference-art.md`](docs/reference-art.md)

角色包面板可以**整包匯入**你收集的官方設定圖／立繪（幾百個檔案或一個 zip 都行），
它會**照檔名自動分給每個角色** —— `Mori Calliope - 1st Costume.png`、
`hoshimachi_suisei_03.jpg`、`星街すいせい.png`、`兎田ぺこら.png` 都認得，
解析度與 `official`／`wallpaper`／編號之類的雜訊會忽略。

**對不上的它不會亂猜**（`IMG_2831.PNG`、只有名沒有姓的 `noel.png`、
或兩位角色同樣符合時），留在「沒對到」清單讓你一秒指定 ——
因為對錯人比沒對到麻煩得多。

然後點縮圖就能把那張圖**當來源圖（以圖生圖）或構圖參考（ControlNet）**。
這是唯一能把「官方長相」直接餵給模型的方法：danbooru 上這些角色只有 1～3%
是官方圖，所以純靠提詞永遠只會得到同人平均值 —— **文字會平均，圖片不會**。

**已經有一整包整理好的圖庫的話走「從資料夾匯入」**：貼上路徑
（例如 `C:\anim\wan-video\Holo pic\Hololive_Ultimate_Archive\01_官方角色全身立繪_最重要`），
先按「先掃描看看」——**這一步不動任何檔案**，只讀檔名和資料夾名，
然後告訴你掃到幾張、幾張對到角色、**幾張是靠資料夾名字認出來的**、
以及**對不到的實際長什麼樣**。看了滿意再匯入。

匯入預設**不搬也不複製**，只記住檔案在哪 —— 一包立繪動輒好幾 GB，
而且那是你自己的資料夾。你之後把它搬走，那些參考會自動從清單消失。

**中文名字現在也認得，而且繁簡都有**：`星街彗星`、`兔田佩克拉`、
`寶鐘瑪琳`／`宝钟玛琳`、`時乃空`／`时乃空`、`森美聲`⋯⋯共 73 位。
這些名字不是我翻的，是從 zh.wikipedia 的 Hololive production 條目
用它自己的字體轉換器讀兩次（`variant=zh-tw` 和 `zh-cn`）拿到的。
兩位沒收：AZKi（名字本來就是拉丁字母）和 Pekomama（沒條目、譯名不只一種），
**猜不如不猜**。

順帶修掉一個會出錯的比對方式：中文名原本是拆成單字比對，
那樣兩個字的名字會 match 到幾乎所有東西（`可律的圖.png` 會 100% 命中 `律可`）。
改成**連續子字串**比對之後，順序也要對。

### 提詞權重與常用提詞 —— 教程在 [`docs/prompt-weights.md`](docs/prompt-weights.md)

游標放在一個 tag 上按 **`Ctrl + ↑`** 就加權（每次 0.05，回到 1.0 時括號自動移除），
提詞框旁也有按鈕。ComfyUI **只認得 `(x:N)`** —— `[x]`、`{{x}}`、`1.3::x::` 全部無效，
這是讀 `comfy/sd1_clip.py` 原始碼確認的。

**`常用提詞`** 按鈕有 **316 個 tag**，分表情／手勢／服裝狀態／姿勢／視角／體液／
身體／場景／光影九類，中英都能搜，點一下加進提詞。每一個都查過 danbooru 的
**實際圖片數**並顯示強弱。要講清楚的是：**圖片數少不等於沒用** —— 底模是 CLIP，
看得懂英文，所以 `ahegao face`、`double peace gesture` 這種自己描述的寫法確實有效果
（實測 CLIP 相似度分別是 0.884 和 0.567，無關文字的基準線只有 0.28）。
圖片數量的是**這支底模被磨得多利**：danbooru 正式 tag 更準、更省權重。
清單附 43 組「更準的寫法」對照。

### 畫師風格清單 —— 教程在 [`docs/artists.md`](docs/artists.md)

同一塊面板再下面是 **52 位畫師**，分厚塗寫實／通透插畫／日系輕柔／鮮豔設計／
漫畫四格／成人向／其他七類，每位附風格說明、danbooru 張數與**從統計算出來的特徵**
（lift：出現率 ÷ 全站基準，所以 `bkub` 會列網點和四格、`wlop` 會列紅唇和寫實）。
其中 20 位是你那份法典用過的。

**前綴會跟著底模自動換**：NoobAI 用 `artist:wlop`、Illustrious 用 `by wlop`、
**Pony V6 完全不吃**（它訓練時把畫師名字從標註裡拿掉了），切到 Pony 或寫實底模會
直接告訴你並提供一鍵換回 NoobAI。順帶查到你法典裡用最多的兩位畫師名字是錯的：
`artist:hiten`（37 條）和 `aritst:deadflow`（32 條）在 danbooru 上都是 0 張，
正確的是 `hiten (hitenkei)` 和 `bee (deadflow)`。

另外**角色包（Hololive）那一塊下面釘了一排常用動作／表情**一鍵按鈕
（單/雙手比 V、露胸、阿嘿顏、上身/下身全裸、蹲馬步、M 字腿、無表情/厭惡/認真/高興），
點一下加、再點一下拿掉，而且**會跟著底模自動換寫法** —— 動漫底模送 danbooru 標籤，
Juggernaut / SDXL 官方底模送自然句子，因為後者從來沒學過 danbooru 標籤。

**自訂尺寸**改成可以拉滑桿（64 為單位）＋比例鎖＋常用比例一鍵，並即時顯示
百萬像素與「這個尺寸會不會出雙頭」。

### 風格靈感庫 —— 教程在 [`docs/style-library.md`](docs/style-library.md)

提詞框下面的 **風格靈感庫**：22 組可以疊在角色提詞上的畫面配方
（清爽動畫 key visual／動畫截圖／霧面 2D／電影感／輕小說封面／手遊立繪／遊戲 CG／
夢幻粉彩／黃金時刻／月夜／賽博霓虹／暗黑奇幻／水彩／墨線漫畫／90 年代／動態戰鬥／
精緻近景／髮絲／高資訊背景／魔法特效／時裝／雨夜）。**這不是模仿畫師**，畫師另外一欄。

配方本身是別人寫的規格書給的。**我把裡面 135 個 tag 一個一個查過 danbooru，
64 個（47%）根本不存在** —— `clean lineart`、`dramatic lighting`、`detailed eyes`、
`rim light`、`cel shading`、`glossy skin` 全部 0 張。有同義的真 tag 就換真 tag，
沒有就整個拿掉，**71 條替換全部列在面板最下面可以自己看**。

最該注意的一條：規格書推薦的 `2d` 在 danbooru 上**是畫師 `nidy` 的別名**（409 張）。
在 NoobAI 上打它等於點名一位特定畫師，跟那個配方的目的正好相反。沒有出貨。

每個 tag 標了它的來源：<code>tag 55k</code> 是真 danbooru tag、
<code>tag caption</code> 是**模型作者訓練時自己塞進標註的詞**（品質詞、年代桶，
查 danbooru 是 0 張很正常）、<code>tag en</code> 是一般英文。

**套用會先給你看 diff**，確認才寫進提詞框。合併不是字串相加：
你原本的拼法和權重贏、角色名和 LoRA 觸發詞絕對不碰、
衝突的 tag 才換掉——而衝突表是去 danbooru **數出來**的
（`monochrome`+`greyscale` 共現 14.2 倍是同一件事，
`monochrome`+`pastel colors` 只有 0.072 倍才是真衝突）。

### 提詞健康度

提詞框下面那一行，改提詞或改尺寸就重算。會講的話包括：

- **512×512 配 SDXL** —— 這通常才是「圖很爛」的真正原因，附一鍵改尺寸
- Pony 的 `score_9` 出現在 NoobAI 上（或 Pony 上少了那六個）
- `8k`／`ultra detailed`／`trending on artstation` —— 沒有任何 anime model card 列過
- 同一個字同時在正面和負面、提詞內部互相衝突、重複的 tag
- 畫師標籤的寫法不合這個底模

順帶查證出一個這個 app 自己的錯：Illustrious 的預設前綴本來是
`masterpiece, best quality, amazing quality, very aesthetic`。
去看它自己的 model card，上面只列 worst／bad／average／good／best quality
跟 masterpiece 六個 —— **`amazing quality` 和 `very aesthetic` 是 WAI 和 Animagine
那些微調自己加的詞，不是 base Illustrious 的**。已經改掉了。

### 動作／姿勢庫（法典）—— 教程在 [`docs/pose-library.md`](docs/pose-library.md)

**提詞庫**分頁最上面：285 個動作、26 位畫師、依原文的 8 大類 / 35 小節排好，
填上你要的角色 → 點動作 → 送到圖片提詞。

要緊的是這份法典是給 **NovelAI** 寫的，而 **ComfyUI 完全不認得 NAI 的權重語法**
（`{{{x}}}`、`[[[x]]]`、`1.3::x::` 全部被當成純文字，權重一律 1.0 外加括號雜訊）。
匯入時整份都照法典自己寫的換算率轉成 `(x:1.2)`，並拿 ComfyUI 自己的解析器
驗過 **2643 個加權 tag**。同時把**畫師 tag 和測試角色抽成獨立、預設關閉的兩組** ——
它們是當初測試者的選擇，留在裡面會直接蓋掉你在角色包選的畫師和角色。

### 角色包（大型角色 LoRA 一鍵切換）—— 教程在 [`docs/character-packs.md`](docs/character-packs.md)

一支大型角色 LoRA 不是一個觸發詞，是好幾百個。**Hololive Collection 一支就有
75 位角色、319 套衣裝**，而這些資訊只存在 CivitAI 說明頁上的一大坨文字裡 ——
每次要用都得回去翻，那才是真正花時間的地方。

所以圖片分頁上多了一塊「🎤 角色包」：**選期別 → 點成員 → 點衣裝 → 提詞就好了**。
成員照出道順序排（JP 0期生 → 1期生 → … → ゲーマーズ → … → EN Myth → … → ID 3期生），
搜尋框打 `suisei`、`すいせい` 或 `星街` 都找得到。

按下「填入提詞」會一次做完四件事：

1. 提詞填好：**觸發詞 → 這套衣服的外觀標籤 → 你自己打的字 → 品質標籤**（放最後，
   因為 Pony 把 score 標籤當整體品質訊號，那支 LoRA 的每個官方範例也都這樣寫）
2. 負面提詞換成作者建議的那組
3. **這支 LoRA 自動勾選**，強度設成作者建議的值
4. 底模不對就提醒你，旁邊直接有「**一鍵切換到 Pony**」——
   走的是跟下拉選單同一條路，所以 sampler、CLIP skip、`score_9…` 前綴會一起換過去

| 內建的包 | 內容 | 要的底模 | LoRA |
| --- | --- | --- | --- |
| [Hololive Collection JP・EN・ID](https://civitai.com/models/713551)（motimalu） | 75 位 · 319 套衣裝 | **Pony Diffusion V6 XL** | 914MB |

已畢業的成員（ココ、るしあ、アロエ、メル、あくあ、Sana）**留在原本的期別裡並標「已畢業」**——
你找 4 期生的時候，ココ 本來就該在那裡。

**要加新的包：給我 CivitAI 連結就好**，我會把成員和衣裝抓出來排好。
加一個包不用改程式，只是往 `app/packs/` 放一個 JSON 檔；
格式和自己動手的做法寫在上面那份教程裡。壞掉的檔案只會被略過，不會讓 app 掛掉。

手動也行：
1. 到 [CivitAI](https://civitai.com/) 找 **Wan Video** 分類、標 **Wan 2.2** 的 LoRA。
2. `.safetensors` 檔丟進 `models/loras/`（Windows 是 `ComfyUI\models\loras\`）。
3. 回網頁，LoRA 清單會自動出現它 —— 勾起來、拉強度，就這樣。不用重啟。

**Wan 2.2 是雙專家模型**，有 high-noise 和 low-noise 兩個模型。很多 CivitAI 的 LoRA 也分成
兩個檔 —— **兩個都勾**，app 會各自套到對應的專家上。

強度先從 0.7～1.0 試。疊太多支會互相打架、畫面崩掉 —— 一次加一支，確認效果再加下一支。

想「每次都自動套用」某些 LoRA，寫在 `.env` 的 `LORAS=` / `LORAS_HIGH=` / `LORAS_LOW=`。

### 界線

這套工具跑在你自己的機器上，成品不會外傳，成年人的創作內容你自己決定。有兩件事無論在誰的
機器上都不行，也請不要拿這套去做：**真人的臉**（未經同意的深偽，多數地區已經違法）和
**任何未成年的描繪**。這不是設定選項的問題，是別做。

---

## 六、出問題的時候

> **先看這份**：[docs/faq.md](docs/faq.md) —— CivitAI key 怎麼填、ComfyUI 怎麼更新、為什麼 `update.bat` 更新完 ComfyUI 還是舊的、多支 LoRA 怎麼共存、怎麼讓成品貼近原畫師的畫風。

先跑檢查工具。它會逐項列出每個模型的安裝狀態，並把每個工作流程拿去跟你這台 ComfyUI
對照，哪個節點、哪個參數不對都會指名道姓：

```powershell
.\venv\Scripts\python.exe app\check.py          # Windows
```
```bash
docker compose run --rm app python check.py     # Docker
./venv/bin/python app/check.py                  # Linux 裸機
```

| 症狀 | 原因 |
| --- | --- |
| `CUDA out of memory` | 先加 `COMFY_ARGS=--lowvram`（還不行就 `--novram`），再考慮降解析度 / 減長度 / 換小模型 |
| 想用大模型但顯存不夠 | **可以用**，加 `--lowvram` 或 `--novram`，會慢但跑得動。模型分頁會告訴你該加哪個 |
| CivitAI 下載失敗 401 | 沒設 `CIVITAI_API_KEY`。搜尋不用 key，下載要 |
| 某模型下拉選單裡是灰的 / 標 `·` | 還沒下載完 —— 去「模型管理」 |
| `'xxx' is not a valid unet_name` | 檔案缺了或名字不符。「模型管理」按「重新檢查／補齊」 |
| `ComfyUI has no node type 'UnetLoaderGGUF'` | ComfyUI-GGUF 沒裝好，重跑安裝腳本 |
| 網頁說「ComfyUI 還沒就緒」 | 第一次載模型要一兩分鐘。更久就看黑視窗裡的紅字 |
| 動作很小、幾乎靜止 | 指令太抽象；把動作和鏡頭講明確。或關掉 4 步加速 |
| 畫面糊掉、顏色壞掉 | LoRA 強度太高或疊太多支，降到 0.6～0.8 |
| `update.bat` 說 `Access to the path ... is denied` | Windows 擋住寫入。見下面一段 |

### update.bat 說「Access to the path ... is denied」

這是 Windows 拒絕覆蓋檔案，不是程式壞掉。**更新沒有完成**，畫面最後會直接寫
`UPDATE DID NOT COMPLETE`。腳本會先檢查每個要覆蓋的檔案寫不寫得進去，**寫不進去就
什麼都不改**，所以你原本的程式仍然是完整的、可以照常用。

三個常見原因，由高到低：

1. **資料夾放在桌面**，而 Windows 的「受控資料夾存取」（勒索軟體防護）預設會保護桌面。
2. **OneDrive 正在同步**桌面／文件夾，同步中的檔案會被鎖住。
3. **有程式開著那個檔案** —— 編輯器、檔案總管的預覽窗格、或防毒的即時掃描。

**最快的解法是把整個 `anim` 資料夾搬離桌面**，例如搬到 `C:\anim`，一次避開前兩個原因。
搬完直接在新位置雙擊 `update.bat` 就好 —— 所有腳本都用相對路徑，Python 也一律用
`venv\Scripts\python.exe -m pip` 而不是 `pip.exe`（`.exe` 捷徑會寫死絕對路徑，搬家就壞），
所以**整個資料夾可以隨便搬**，模型和成品都不用重下。

如果不想搬，就把 PowerShell 加進「Windows 安全性 → 病毒與威脅防護 → 勒索軟體防護 →
允許應用程式通過受控資料夾存取」，或先暫停 OneDrive 同步。處理完再跑一次 `update.bat`。

> **萬一真的中途失敗了**（畫面寫「一半新一半舊」）：不要啟動，把原因排除後再跑一次
> `update.bat`。它是可以重複執行的，第二次會把缺的補齊。

---

## 七、這裡面有什麼

```
docker-compose.yml     ComfyUI（GPU）+ app + 選用的拖檔監看
Dockerfile.comfy       ComfyUI + ComfyUI-GGUF + VideoHelperSuite + Manager
setup-windows.ps1      Windows 原生安裝（不用 Docker）
start-windows.ps1      Windows 啟動 · update-windows.ps1 更新程式碼（不動模型）
install.bat / start.bat / update.bat   上面三支的雙擊包裝
setup-codex.bat        選用：裝 OpenAI Codex 並註冊給 Claude Code 當工具
                       （見 docs/codex-mcp.md；憑證由你自己輸入，不經過腳本）
setup-linux.sh         Linux 裸機安裝
scripts/
  fetch-model.py       命令列下載模型，可續傳。只用標準函式庫
app/
  registry.py          影片模型目錄：檔名、repo 路徑、大小、取樣參數、CivitAI base 對應
  images.py            圖片底模目錄 + SDXL 文生圖／圖生圖／漫畫工作流程 + 每個旋鈕的解釋
  comics.py            漫畫版型、拼版、真文字對白框（danbooru 標籤數字都查過）
  pagelayout.py        從現成漫畫頁量出格子（遞迴 XY-cut，含「這不是分格頁」的判斷）
  inspect_image.py     從 PNG/EXIF 讀回生成參數（ComfyUI 與 A1111 兩種格式）
  tags.py              WD tagger：看圖產生 danbooru 標籤（BGR 前處理是實測出來的）
  promptbook.py        匯入提詞範例文件，自動判斷分段方式（8 種格式）
  upscalers.py         GAN 放大模型與補幀模型目錄（圖片和影片共用）
  controlnets.py       ControlNet 目錄：鎖住構圖重畫內容（分鏡克隆的核心）
  charpacks.py         角色包：一支角色 LoRA 的所有角色與衣裝，一鍵出提詞
  packs/*.json         角色包資料（加一個檔案就多一個包，不用改程式）
  prompts.py           {A|B} 隨機提詞展開、權重語法檢查、語法小抄
  updates.py           app / ComfyUI / CivitAI 三邊的更新偵測，各自獨立、失敗不互相影響
  civitai.py           CivitAI 搜尋與下載（需要 User-Agent；下載需要 API key）
  library.py           成品紀錄持久化、星號、磁碟統計、孤兒清理
  workflow.py          按家族組出 ComfyUI 工作流程（Wan 14B / Wan 5B / Hunyuan 1.5）
  comfy_client.py      ComfyUI HTTP + websocket 客戶端，含送出前的圖驗證
  downloader.py        背景下載，續傳、進度、大小驗證
  server.py            上傳 → 佇列 → mp4；模型與 LoRA 的 API
  watcher.py           拖檔模式
  check.py             環境檢查
  naiweights.py        NovelAI 語法 → ComfyUI 權重（{{}} / [[]] / 1.3::x::）
  posebook.py          動作／姿勢法典的解析與一鍵組裝
  quicktags.py         常用提詞清單（每個都查過 danbooru 實際圖片數）
  refs.py              官方參考圖庫（檔名／資料夾名→角色的比對，對不上就不猜）
  refnames.py          73 位成員的中文名（繁簡都有，從 zh.wikipedia 兩種字體轉換讀來的）
  experiments.py       實驗矩陣、內容雜湊來源記錄、盲測配對與計分
  artists.py           畫師清單（風格特徵用 danbooru lift 統計出來）
  styles.py            22 組風格配方（每個 tag 都查過 danbooru，47% 的原始建議是不存在的字）
  promptmerge.py       套用配方時的合併：去重、衝突（用共現量出來的）、清方言、給 diff
  promptdoctor.py      提詞健康度：畫布尺寸、模型方言、互相矛盾、重複
  poses/               法典資料（一個 JSON 一份法典）
  static/index.html    網頁介面（影片 / 圖片 / 素材庫 / LoRA / 模型 / 提詞庫 / 設定）
docs/
  comic-restage.md     漫畫分鏡克隆的完整教程
  character-packs.md   角色包的用法與資料格式
  faq.md               設定、更新、LoRA 共存、畫風貼近原畫師
  pose-library.md      動作／姿勢法典：NAI→ComfyUI 權重換算、畫師 tag 分離
  prompt-weights.md    提詞權重、316 個查證過的常用 tag、自訂尺寸滑桿
  artists.md           52 位畫師 tag：風格、danbooru 張數、各底模的正確前綴
  codex-mcp.md         讓 Claude Code 跟 OpenAI Codex 協作（選用）
  codex-review-brief.md 給第二個模型審查用的自足摘要（主張＋數據＋我自己知道的弱點）
  review-response.md   對 Codex 審查的逐條回應：改了什麼、還沒做什麼
  reference-art.md     官方參考圖：整包資料夾匯入、中文名比對、一鍵當來源圖／構圖參考
  experiments.md       固定 seed 掃參數、來源記錄、盲測 pairwise
  style-library.md     22 組風格配方、量出來的衝突表、提詞健康度
  spec-review.md       對「Prompt 靈感庫」規格書的逐條審查回覆（給下一輪 review 用）
  refs-review.md       參考圖庫整包匯入與中文名比對的審查說明（給下一輪 review 用）
  windows-tutorial.md  Windows 從零開始的圖文教學
tests/
  test_flow.py         用假的 ComfyUI / Hugging Face / CivitAI 跑完整流程，不需要顯卡
  fake_civitai.py      假的 CivitAI，重現「沒 User-Agent 就 403」「沒 key 下載就 401」
  schema_core.json     從真的 ComfyUI 0.33.0 匯出的節點結構，當測試基準
  fake_comfy.py        假的 ComfyUI，用上面那份結構回答 /object_info
  dump_schema.py       ComfyUI 升級後用它重新匯出
```

### 為什麼可以信這些工作流程

節點名稱和參數不是憑印象寫的：

- 每個模型的**檔名、repo 路徑、位元組大小**都是從 Hugging Face API 讀出來的。
- 每個**節點名稱和取樣參數**（Wan 5B 的 `uni_pc`、Hunyuan 的 `shift 7 / cfg 6`、
  `DualCLIPLoader` 的 `hunyuan_video_15`⋯）都對照過 ComfyUI 官方內建的範例工作流程。
- 影片和圖片兩邊加起來 **154 種組合**（三個影片家族 × 加速開關 × 解析度 × 補幀／放大，
  四個圖片底模 × 高解析重繪方式 × 放大 × 分塊解碼 × 文生圖／圖生圖），全部拿
  **真的 ComfyUI 0.33.0** 跑過結構驗證，0 個失敗。
- ComfyUI 0.33 把 `/object_info` 的 combo 格式換成了三種並存
  （舊的清單式、`["COMBO", {options: [...]}]`、以及 options 是物件的
  `COMFY_DYNAMICCOMBO_V3`）。驗證器三種都認得 —— 只讀舊格式的話，
  一半以上的欄位會被靜靜跳過不檢查。
- 執行期 `comfy_client.validate()` 還會再拿你那台的 `/object_info` 比對一次，所以檔名打錯、
  節點沒裝、sampler 名字不對，會在送出前就講清楚是哪一個，而不是等 ComfyUI 回一句
  看不懂的 400。

`tests/schema_core.json` 是真實 ComfyUI 的節點結構匯出檔，測試就是拿它當假伺服器的
schema —— 所以測試不會因為我手寫的假結構而失真。ComfyUI 升級後跑
`python3 tests/dump_schema.py http://127.0.0.1:8188` 重新匯出即可。

跑測試（不需要顯卡）：

```bash
python3 tests/test_flow.py

# 如果你本機有 ComfyUI 在跑，順便對真的驗證一遍每個工作流程：
COMFY_URL=http://127.0.0.1:8188 python3 tests/test_flow.py --live
```

**沒有驗證的部分**：這些程式是在沒有顯卡的環境寫的，所以**沒有實際生成過一支影片**。
結構、參數、下載、續傳、API、UI 都測過了，但真正的 GPU 執行要在你那邊才能確認。
`app/check.py` 就是為了讓那一步不用瞎猜。

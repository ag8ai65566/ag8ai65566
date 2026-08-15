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

開 <http://127.0.0.1:8000>，上面有六個分頁。

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
| **Illustrious XL** | 動漫 / 插畫，**NSFW LoRA 生態最大** | 8GB | 7.3GB |
| **Pony Diffusion V6 XL** | 動漫 / 多元題材，NSFW 生態第二大 | 8GB | 7.3GB |
| **Juggernaut XL v9** | 寫實照片風 | 8GB | 7.4GB |
| **SDXL 1.0 官方** | 中性基準 | 8GB | 7.3GB |

**每個底模的「眉角」寫在介面上**，這是 ComfyUI 不會告訴你的部分：

- **Pony 的提詞開頭一定要有 `score_9, score_8_up, score_7_up`**，否則畫面會爛 ——
  app 幫你自動加，也可以取消
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

右邊有**即時版面預覽** —— 灰色代表畫面會出現的地方，改對白或格線粗細會馬上重畫，
不用等 GPU 跑完才知道版面對不對。

成品是**一張完整的頁面**，每一格也會單獨存一份，想單獨重畫或重排都拿得到。

**兩個接力按鈕**（在每張成品卡片上）：

- **接著修** —— 拿這張成品當來源圖再畫一次，設定全部帶回來
- **→ 做成影片** —— 直接把這張丟到影片分頁，不用先下載再拖回來
- **同種子微調** —— 種子和所有設定都保持一樣，只改你想試的那一個，做 A/B 對照

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
setup-linux.sh         Linux 裸機安裝
scripts/
  fetch-model.py       命令列下載模型，可續傳。只用標準函式庫
app/
  registry.py          影片模型目錄：檔名、repo 路徑、大小、取樣參數、CivitAI base 對應
  images.py            圖片底模目錄 + SDXL 文生圖／圖生圖／漫畫工作流程 + 每個旋鈕的解釋
  comics.py            漫畫版型、拼版、真文字對白框（danbooru 標籤數字都查過）
  upscalers.py         GAN 放大模型與補幀模型目錄（圖片和影片共用）
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
  static/index.html    網頁介面（影片 / 圖片 / 素材庫 / LoRA / 模型 / 設定）
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

# 圖片 → 短動畫（本機執行）

丟一張圖、選模型、打一句指令、拿到一支幾秒的動畫。**完全在你自己的機器上跑** —— 裝好之後
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

一支 5 秒 480p 大概要：24GB 卡 1～3 分鐘、12GB 卡 6～12 分鐘、8GB 會很痛苦。
720p 大約是 480p 的 2～3 倍時間與顯存。上面的時間是開了 4 步 Lightning 加速的結果。

**磁碟**：一個模型 18～43GB，可以裝多個（共用元件不會重複下載）。**記憶體**：建議 32GB。

安裝腳本會讀你的顯存自動挑第一個模型，之後在網頁上加裝其他的。

---

## 三、安裝

### Windows（推薦你走這條）

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

開 <http://127.0.0.1:8000>：

**生成分頁** —— 圖拖進框裡（或 Ctrl+V 貼上）→ 選模型 → 打指令 → 按「生成」。
下面會排隊、跑進度條，完成後直接在頁面上播放。沒下載的模型會標 `·` 並提示去下載。

**模型管理分頁** —— 每個模型顯示顯存需求、下載大小、安裝狀態。按下載會顯示即時進度、
速度和剩餘時間，可以中途停掉，之後接著下。已安裝的按「重新檢查／補齊」會補上缺的檔。

**指令怎麼寫**，這些模型吃「描述動作與鏡頭」的句子，中英文都行：

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

啟動：Windows `.\start-windows.ps1 -Watch`、Linux `./start-linux.sh --watch`、
Docker `docker compose --profile watch up -d`。

---

## 五、加 LoRA（畫風 / 題材 / NSFW）

基礎模型本身沒有內容過濾，但要特定題材的品質，靠的是 LoRA。

1. 到 [CivitAI](https://civitai.com/) 找 **Wan Video** 分類、標 **Wan 2.2** 的 LoRA。
2. `.safetensors` 檔丟進 `models/loras/`（Windows 是 `ComfyUI\models\loras\`）。
3. 回網頁，「LoRA」區塊會自動出現它 —— 勾起來、拉強度，就這樣。不用重啟。

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
| `CUDA out of memory` | 換小一點的模型（`hy15-480p` 最省）、降解析度、減長度、`COMFY_ARGS=--lowvram` |
| 某模型下拉選單裡是灰的 / 標 `·` | 還沒下載完 —— 去「模型管理」 |
| `'xxx' is not a valid unet_name` | 檔案缺了或名字不符。「模型管理」按「重新檢查／補齊」 |
| `ComfyUI has no node type 'UnetLoaderGGUF'` | ComfyUI-GGUF 沒裝好，重跑安裝腳本 |
| 網頁說「ComfyUI 還沒就緒」 | 第一次載模型要一兩分鐘。更久就看黑視窗裡的紅字 |
| 動作很小、幾乎靜止 | 指令太抽象；把動作和鏡頭講明確。或關掉 4 步加速 |
| 畫面糊掉、顏色壞掉 | LoRA 強度太高或疊太多支，降到 0.6～0.8 |

---

## 七、這裡面有什麼

```
docker-compose.yml     ComfyUI（GPU）+ app + 選用的拖檔監看
Dockerfile.comfy       ComfyUI + ComfyUI-GGUF + VideoHelperSuite + Manager
setup-windows.ps1      Windows 原生安裝（不用 Docker）／ start-windows.ps1 啟動
setup-linux.sh         Linux 裸機安裝
scripts/
  fetch-model.py       命令列下載模型，可續傳。只用標準函式庫
app/
  registry.py          模型目錄：檔名、repo 路徑、大小、每個模型的取樣參數
  workflow.py          按家族組出 ComfyUI 工作流程（Wan 14B / Wan 5B / Hunyuan 1.5）
  comfy_client.py      ComfyUI HTTP + websocket 客戶端，含送出前的圖驗證
  downloader.py        背景下載，續傳、進度、大小驗證
  server.py            上傳 → 佇列 → mp4；模型與 LoRA 的 API
  watcher.py           拖檔模式
  check.py             環境檢查
  static/index.html    網頁介面（生成 + 模型管理兩個分頁）
tests/
  test_flow.py         153 項檢查，用假的 ComfyUI 和假的 Hugging Face，不需要顯卡
  schema_core.json     從真的 ComfyUI 0.32.0 匯出的節點結構，當測試基準
  dump_schema.py       ComfyUI 升級後用它重新匯出
```

### 為什麼可以信這些工作流程

節點名稱和參數不是憑印象寫的：

- 每個模型的**檔名、repo 路徑、位元組大小**都是從 Hugging Face API 讀出來的。
- 每個**節點名稱和取樣參數**（Wan 5B 的 `uni_pc`、Hunyuan 的 `shift 7 / cfg 6`、
  `DualCLIPLoader` 的 `hunyuan_video_15`⋯）都對照過 ComfyUI 官方內建的範例工作流程。
- 三個家族 × 加速開關 × 每個解析度，總共 19 種組合，全部拿**真的 ComfyUI 0.32.0**
  跑過結構驗證。
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

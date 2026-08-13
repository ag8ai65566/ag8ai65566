# 圖片 → 短動畫（本機執行）

丟一張圖、打一句指令、拿到一支幾秒的動畫。全部在你自己的機器上跑，圖片和成品都不會離開你的電腦。

---

## 一、結論：用 Wan 2.2 I2V A14B

問「現在最好的、可本地部署、支援 NSFW、品質好」的圖生影片模型，2026 年 8 月的答案是
**阿里巴巴 Wan 2.2 的 I2V-A14B**。理由是三個條件的交集，而不是單看畫質：

| 模型 | 開源權重 | 授權 | 顯存 | NSFW 生態 | 判斷 |
| --- | --- | --- | --- | --- | --- |
| **Wan 2.2 I2V-A14B** | ✅ 2025-08 | Apache 2.0 | fp8 約 24GB / GGUF 可到 12GB | **最完整**，CivitAI 上大量 LoRA、remix、專用工作流 | **這套用它** |
| LTX-2.3（22B） | ✅ | LTX-2 社群授權 | fp8 可進 16GB | 稀少 | 影音同步一次生成很強，但這個用途生態不足 |
| HunyuanVideo 1.5（8.3B） | ✅ | 有商用限制 | 14GB（開 offload） | 中等 | 最省顯存、人臉與物理自然，授權較綁手 |
| Wan 2.5 / 2.6 / 2.7 | ❌ **從未釋出** | 僅 API | — | — | **不可能本地部署**，別被行銷文帶走 |

兩個容易踩的坑：

- **Wan 官方開源到 2.2 為止就停了。** 2.5 之後（含 2.6、2.7）只有雲端 API，沒有權重檔。
  網路上寫「Wan 2.6 開源可自架」的文章是錯的。要本地跑，上限就是 2.2。
- **NSFW 不是靠「解鎖」而是靠生態。** ComfyUI 本身沒有內容過濾器，Wan 2.2 的基礎模型也
  沒有內建拒絕機制 —— 真正的差別在於社群為 Wan 2.2 訓練了遠比其他模型多的 LoRA。
  這也是選它而不選畫質同級的 LTX-2.3 的主因。

至於 Wan 2.2 還有一個 **TI2V-5B** 單模型版本（約 10GB，24GB 顯卡跑 720p 約 9 分鐘），
省資源但畫質明顯輸 14B。**這套環境只做 14B 雙專家版**，沒有實作 5B 的流程。

---

## 二、你需要什麼硬體

必須是 **NVIDIA** 顯卡（AMD / Intel / 內顯都跑不動）。

| 顯存 | 設定 | 一支 5 秒 480p 大概要 |
| --- | --- | --- |
| 24GB+（4090 / 5090 / A6000） | `PROFILE=fp8` | 1～3 分鐘 |
| 16GB（4080 / 4060 Ti 16G） | `PROFILE=gguf` `GGUF_QUANT=Q8_0` | 3～6 分鐘 |
| 12GB（3060 12G / 4070） | `PROFILE=gguf` `GGUF_QUANT=Q4_K_M` | 6～12 分鐘 |
| 8GB | `PROFILE=gguf` `GGUF_QUANT=Q4_K_S` + `COMFY_ARGS=--lowvram` | 15 分鐘以上，會很痛苦 |

720p 大約是 480p 的 2～3 倍時間與顯存。安裝腳本會讀你的顯存自動選檔，選錯了再改 `.env`。

**磁碟**：fp8 約 40GB，GGUF 約 30GB。**記憶體**：建議 32GB（模型在 GPU/CPU 之間換進換出）。

上面的時間是開了 4 步 Lightning 加速 LoRA 的結果（預設開）。關掉會慢 4～5 倍，換到略好的
動態與細節。

---

## 三、安裝

### Windows（推薦你走這條）

1. 先確認有裝 **Python 3.12**（<https://www.python.org/downloads/>，安裝時**務必勾
   「Add python.exe to PATH」**）和 **Git**（<https://git-scm.com/download/win>，一路 Next）。
2. 下載這個資料夾到電腦上，在資料夾裡按右鍵 →「在終端中開啟」。
3. 貼上這行，按 Enter，然後去做別的事（要下載約 40GB）：

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1
   ```

   顯存不到 20GB 的話它會自動改用 GGUF。想自己指定：
   `powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1 -Profile gguf -Quant Q4_K_M`

4. 裝完之後，每次要用就執行：

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\start-windows.ps1
   ```

   會跳出兩個黑色視窗（**不要關**），瀏覽器自動開 <http://127.0.0.1:8000>。

下載中斷不用怕，重跑 `setup-windows.ps1` 會從斷點續傳。

### Linux + Docker

```bash
cp .env.example .env
./scripts/download-models.sh fp8        # 或 gguf Q4_K_M
docker compose up -d --build            # 加 --profile watch 順便開拖檔模式
```

需要主機上有 NVIDIA 驅動與
[nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)。
開 <http://127.0.0.1:8000>。

### Linux 裸機（不用 Docker）

```bash
./setup-linux.sh                # 或 ./setup-linux.sh gguf Q4_K_M
./start-linux.sh                # 之後每次
```

---

## 四、怎麼用

### 網頁（主要方式）

開 <http://127.0.0.1:8000>：把圖拖進框裡（或 Ctrl+V 貼上）→ 打指令 → 按「生成」。
下面會排隊、跑進度條，完成後直接在頁面上播放，可以下載。

**指令怎麼寫**，這個模型吃「描述動作與鏡頭」的句子，中英文都行：

```
她慢慢轉頭看向鏡頭，長髮被風吹動，鏡頭緩慢推近
he raises the glass and drinks, warm candlelight flickering, slow dolly in
```

寫得越具體越穩。不要只寫「讓它動起來」——那會得到隨機的漂移。想固定結果就把 seed
從 -1 改成一個數字，同樣的圖 + 指令 + seed 會得到同樣的片子。

### 拖檔案模式（批次）

不想開瀏覽器就用這個：圖片丟進 `data/inbox/`，成品自己出現在 `data/outputs/`。

- 指令放在同名的 `.txt`（`cat.png` → `cat.txt`）
- 沒有 `.txt` 的話，**檔名本身就當指令**（`她轉頭看鏡頭.png` 會照著做）
- 處理完的原圖會搬到 `data/inbox/done/`

啟動方式：Windows `.\start-windows.ps1 -Watch`、Linux `./start-linux.sh --watch`、
Docker `docker compose --profile watch up -d`。

---

## 五、加 LoRA（畫風 / 題材 / NSFW）

基礎模型本身沒有內容過濾，但要特定題材的品質，靠的是 LoRA。

1. 到 [CivitAI](https://civitai.com/) 找 **Wan Video** 分類、標 **Wan 2.2** 的 LoRA。
2. `.safetensors` 檔丟進 `models/loras/`（Windows 是 `ComfyUI\models\loras\`）。
3. 在 `.env` 填檔名，格式是 `檔名:強度`，逗號分隔：

   ```
   LORAS=my_style.safetensors:0.8, another.safetensors
   ```

4. 重啟 app（ComfyUI 不用重啟）。

**Wan 2.2 是雙專家模型**，有 high-noise 和 low-noise 兩個模型。很多 CivitAI 的 LoRA 也會
分成兩個檔，這時候要分開指定，不要用 `LORAS`：

```
LORAS_HIGH=thing_high_noise.safetensors:1.0
LORAS_LOW=thing_low_noise.safetensors:1.0
```

`LORAS` 是「兩邊都套」，適合只有單一檔案的 LoRA。強度先從 0.7～1.0 試，疊太多支會互相
打架、畫面崩掉 —— 一次加一支、確認效果再加下一支。

### 界線

這套工具跑在你自己的機器上，成品不會外傳，成年人的創作內容你自己決定。有兩件事無論
在誰的機器上都不行，也請不要拿這套去做：**真人的臉**（未經同意的深偽，多數地區已經違法）
和**任何未成年的描繪**。這不是設定選項的問題，是別做。

---

## 六、調整

改 `.env` 之後重啟 app。完整清單看 `.env.example`，最常動的是：

| 設定 | 作用 |
| --- | --- |
| `LIGHTNING=false` | 關掉 4 步加速，改 20 步取樣。慢 4～5 倍，動態與細節略好 |
| `TIER=720p` | 預設解析度（網頁上也能逐次選） |
| `LENGTH=121` | 幀數，**必須是 4n+1**（填錯會自動往下修）。16fps 之下 121 幀 ≈ 7.5 秒 |
| `COMFY_ARGS=--lowvram` | 顯存不夠時加。還不夠就 `--novram` |
| `WEIGHT_DTYPE=fp8_e4m3fn_fast` | 40 系以上 fp8 再快一點 |

想自己接工作流程、看每個節點在幹嘛，ComfyUI 本體在 <http://127.0.0.1:8188>。

---

## 七、出問題的時候

先跑檢查工具，它會逐項告訴你哪裡不對（模型檔名、缺少的節點、參數不合法）：

```powershell
.\venv\Scripts\python.exe app\check.py          # Windows
```
```bash
docker compose run --rm app python check.py     # Docker
./venv/bin/python app/check.py                  # Linux 裸機
```

| 症狀 | 原因 |
| --- | --- |
| `CUDA out of memory` | 換小一點的 `GGUF_QUANT`、降 `TIER=480p`、減 `LENGTH`、加 `COMFY_ARGS=--lowvram` |
| `'xxx.safetensors' is not a valid unet_name` | 模型沒下載完或檔名不符。重跑下載腳本，或在 `.env` 用 `MODEL_HIGH`/`MODEL_LOW` 指定實際檔名 |
| `ComfyUI has no node type 'UnetLoaderGGUF'` | ComfyUI-GGUF 沒裝好，重跑安裝腳本 |
| 網頁一直說「ComfyUI 還沒就緒」 | 第一次載模型要一兩分鐘。更久就看黑視窗裡的紅字 |
| 動作很小、幾乎靜止 | 指令寫得太抽象；把動作和鏡頭講明確。或 `LIGHTNING=false` 試試 |
| 畫面糊掉、顏色壞掉 | LoRA 強度太高或疊太多支，降到 0.6～0.8 |

---

## 八、這裡面有什麼

```
docker-compose.yml     ComfyUI（GPU）+ app + 選用的拖檔監看
Dockerfile.comfy       ComfyUI + ComfyUI-GGUF + VideoHelperSuite + Manager
Dockerfile.app         這個 app
setup-windows.ps1      Windows 原生安裝（不用 Docker）
start-windows.ps1      Windows 啟動
setup-linux.sh         Linux 裸機安裝
scripts/
  download-models.sh   模型下載，可續傳、可重跑
app/
  server.py            上傳 → 佇列 → mp4 的 HTTP 服務（一次跑一支，GPU 是瓶頸）
  workflow.py          用程式組出 Wan 2.2 I2V 的 ComfyUI 工作流程
  comfy_client.py      ComfyUI HTTP + websocket 客戶端，含送出前的圖驗證
  watcher.py           拖檔模式
  check.py             環境檢查
  static/index.html    網頁介面
tests/
  test_flow.py         整條流程的測試，用假的 ComfyUI，不需要顯卡
```

`workflow.py` 是用程式組工作流程，不是讀死的 `.json`，所以解析度、長度、LoRA、步數
都能從設定驅動。送出前 `comfy_client.validate()` 會拿你這台 ComfyUI 的 `/object_info`
比對每個節點和參數 —— 檔名打錯、節點沒裝、sampler 名字不對，會在送出前就講清楚是哪個，
而不是等 ComfyUI 回一句看不懂的 400。

跑測試（不需要顯卡，會起一個假的 ComfyUI）：

```bash
python3 tests/test_flow.py
```

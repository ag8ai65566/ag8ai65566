# 影片模型：為什麼「最新的」跟「跑在你電腦上的」已經不是同一份清單

**簡短版**：Seedance 匯入不了，Wan 2.5 也匯入不了。這兩個都是**閉源 API**，
沒有權重可以下載。目前開放權重裡最新的是 **LTX-2.5**，已經加進「模型」分頁。

---

## 為什麼 Seedance 匯不進來

Seedance 是 ByteDance 的影片模型（2.0 是 2026-02，2.5 是 2026-07 宣布、
API 還在 pre-release）。**ByteDance 從來沒有釋出過權重。**

會有誤會是因為 ComfyUI「支援 Seedance」—— 但那是 **Partner Node（API 節點）**，
不是 checkpoint。它把你的提詞和圖片送到 ByteDance 的伺服器，跑完把影片傳回來。
實際條件：

| | |
|---|---|
| 帳號 | 要 comfy.org 帳號 **+ 預付點數**；目前**不能用你自己的 ByteDance API key**（官方說還在測試階段） |
| 網路 | 本機只允許 `127.0.0.1` / `localhost`。**這個專案的 ComfyUI 是 `--listen 0.0.0.0`**（`Dockerfile.comfy:40`），照官方說明這樣 Partner Node 不會動，要改成 API Key 登入 |
| 價格 | Replicate 每輸出秒 $0.1028（480p）/ $0.2312（720p）→ 5 秒約 **$0.51 / $1.16**；有影片輸入更貴（480p 5 秒 $0.553–2.152） |
| 真人 | **真人肖像要先過 ByteDance 的活體驗證**；AI 生成的臉不用 |

也就是說它跟這個專案的每一個前提都相反：本機→雲端、免費→按次計費、
沒有內容過濾→有過濾、離線→要網路，而且你的圖會離開你的電腦。
**不是不能做，是你要知道自己在換什麼。**

同樣的情況也適用 **Wan 2.5**（阿里巴巴）—— 一樣是閉源 API。
只有 **Wan 2.2** 有開放權重，而它已經在這個專案裡了。

---

## 開放權重這邊有什麼

| 模型 | 狀態 | 適合 |
|---|---|---|
| Wan 2.2 I2V 14B | 已收錄（fp8 / GGUF Q8 / Q4） | NSFW LoRA 生態最完整 |
| Wan 2.2 TI2V 5B | 已收錄 | 輕量、原生 720p |
| HunyuanVideo 1.5 | 已收錄（480p / 720p / 720p-HQ） | **人臉與物理最自然**，寫實向 |
| LTX-2.3 22B | 已收錄 | 影音同步一次生成 |
| **LTX-2.5 22B** | **新增** | 影音同步，官方說支援到 4K HDR / 50fps |

**沒有實測。** 這台開發機沒有 GPU，這個專案從頭到現在**一張圖、一段影片都沒生成過**。
上面「適合什麼」是規格與 model card 的整理，不是比較結果。
要真的排出高下，用 [`experiments.md`](experiments.md) 那台固定 seed ＋盲測的機器。

---

## LTX-2.5：下載前要先做兩件事

這是這份目錄裡**第一個 gated（閘門式）的倉庫**。
`Lightricks/LTX-2.5` 對匿名請求直接回 **401** —— 權重是免費的，但要登入。

實測（2026-09-05）：

```
GET https://huggingface.co/Lightricks/LTX-2.5/resolve/main/...  →  401
API: {"gated": "auto", "license": "other"}
```

所以要做兩件事，**少一件都會 401**：

1. 開 <https://huggingface.co/Lightricks/LTX-2.5>，登入，**按同意授權**
2. 到「設定」分頁貼上 **Hugging Face access token**
   （huggingface.co → 頭像 → Settings → Access Tokens → New token，read 權限就夠）

模型分頁上那張卡片會直接把這兩步列出來，並顯示你的 token 有沒有設好 —— 
因為 gated 倉庫是**第一個 byte 就 401**，等下載失敗才講等於讓你白等。

### 它會下載什麼

檔名與大小全部讀自 HuggingFace 的 tree API，不是抄來的：

| 檔案 | 放哪 | 大小 |
|---|---|---|
| `ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors` | `diffusion_models` | 21.50 GB |
| `gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors` | `text_encoders` | 15.37 GB |
| `ltx-2.5-video-vae-bf16.safetensors` | `vae` | 1.47 GB |
| `ltx-2.5-audio-vae-bf16.safetensors` | `vae` | 0.36 GB |
| `ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors` | `latent_upscale_models` | 1.00 GB |
| | | **合計 39.7 GB** |

幾個選檔上的決定：

- **用 int8 的 `convrot` 版本，不是 bf16。** bf16 的 transformer 是 42GB 一個檔，
  而 ComfyUI 官方 LTX-2.5 頁面列的就是 int8 這個。多花 20GB 買不到東西。
- **用 distilled 不是 dev。** 官方 workflow 載的是 distilled。
- **text encoder 不能拿 LTX-2.3 的 Gemma 3 來用。** 這一版的投影層是包在檔案裡的，
  載入時會比對 encoder 版本跟 checkpoint 訓練時的版本，所以只有這個檔可以。
- **兩個 VAE 都要。** 聲音是跟畫面在同一個 pass 生成的，audio VAE 不是可選項。
- 沒有收 `gemma4_e2b_it_int8_convrot`（提詞增強器用的），官方標為 optional。

跟 LTX-2.3 一樣是 **files_only**：這個 app 只負責把檔案放對位置，
生成請到 ComfyUI（`:8188`）→ Workflow → Browse Templates → LTX-2.5。
本頁的影片產生器不會出現這個選項 —— 我沒有辦法在沒有 GPU 的機器上驗證那張圖，
所以不假裝它能跑。

---

## Hugging Face token 怎麼被使用

- 只送給 `huggingface.co`。**`RemoteFile`（CivitAI 之類的外部來源）永遠拿不到它** ——
  那種來源的網址可以指向任何主機，把使用者的 token 貼上去就是外洩。
  這件事有測試盯著。
- **每次請求才讀 `os.environ`**，跟 CivitAI key 一樣。
  在 import 時快取住，正是讓設定框「看起來壞掉」的原因 —— 你剛存的值不是程式在用的值。
- 401/403 的錯誤訊息會**分辨是哪一把鑰匙**：
  沒 token 就叫你去設定分頁貼 token 並附上該按同意的網址；
  有 token 還被拒就叫你去按同意授權（因為那才是剩下的那件事）；
  CivitAI 的 401 則指向 CivitAI key。一句籠統的「需要 API key」會把人送去錯的地方。

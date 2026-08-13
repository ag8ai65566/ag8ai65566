# 一鍵安裝（Windows + NVIDIA 顯卡）
#
#   在這個資料夾按右鍵 → 「在終端中開啟」，然後貼上：
#     powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1
#
#   選項：
#     -Profile gguf -Quant Q4_K_M   顯存不到 24GB 時用
#     -SkipModels                    只裝程式、不下載模型
[CmdletBinding()]
param(
  [ValidateSet('fp8', 'gguf')][string]$Profile = 'fp8',
  [string]$Quant = 'Q4_K_M',
  [switch]$SkipModels
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
Set-Location $root

function Say($m) { Write-Host "`n=== $m ===" -ForegroundColor Cyan }
function Ok($m) { Write-Host "  OK  $m" -ForegroundColor Green }
function Warn($m) { Write-Host "  !!  $m" -ForegroundColor Yellow }
function Die($m) { Write-Host "`n失敗：$m" -ForegroundColor Red; exit 1 }

# ---- 0. 檢查環境 ------------------------------------------------------------
Say '檢查環境'

$smi = Get-Command nvidia-smi -ErrorAction SilentlyContinue
if (-not $smi) {
  Die @'
找不到 nvidia-smi，表示沒有 NVIDIA 顯卡驅動。
這套東西一定要 NVIDIA 顯卡（AMD / Intel / 內顯都跑不動）。
請先到 https://www.nvidia.com/download/index.aspx 安裝驅動再重來。
'@
}

$gpuName = (& nvidia-smi --query-gpu=name --format=csv,noheader | Select-Object -First 1).Trim()
$vramMB = [int]((& nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits | Select-Object -First 1).Trim())
$vramGB = [math]::Round($vramMB / 1024, 1)
Ok "顯卡：$gpuName（${vramGB}GB 顯存）"

if ($vramGB -lt 8) {
  Warn "顯存只有 ${vramGB}GB，跑起來會非常慢甚至失敗。建議 12GB 以上。"
} elseif ($vramGB -lt 20 -and $Profile -eq 'fp8') {
  Warn "顯存 ${vramGB}GB 用 fp8 會爆。自動改用 GGUF $Quant。"
  $Profile = 'gguf'
}

$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
  Die @'
找不到 Python。請到 https://www.python.org/downloads/ 下載 3.12 版，
安裝時務必勾選最下面的「Add python.exe to PATH」，裝完把這個視窗關掉重開再執行一次。
'@
}
$pyVer = (& python -c "import sys;print('%d.%d' % sys.version_info[:2])").Trim()
if ([version]$pyVer -lt [version]'3.10' -or [version]$pyVer -ge [version]'3.14') {
  Die "Python 版本是 $pyVer，需要 3.10 ~ 3.13。請安裝 3.12。"
}
Ok "Python $pyVer"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  Die @'
找不到 git。請到 https://git-scm.com/download/win 下載安裝（一路 Next 用預設值），
裝完把這個視窗關掉重開再執行一次。
'@
}
Ok 'git'

if (-not (Get-Command curl.exe -ErrorAction SilentlyContinue)) {
  Die 'curl.exe 不存在，需要 Windows 10 1803 以上。'
}
Ok 'curl'

# 50 系列（Blackwell）需要 CUDA 12.8 版的 PyTorch
$cuda = if ($gpuName -match 'RTX\s*50\d\d') { 'cu128' } else { 'cu126' }
Ok "PyTorch 版本：$cuda"

# ---- 1. 虛擬環境 ------------------------------------------------------------
Say '建立 Python 虛擬環境'
if (-not (Test-Path "$root\venv")) { & python -m venv "$root\venv" }
$pip = "$root\venv\Scripts\pip.exe"
$vpy = "$root\venv\Scripts\python.exe"
& $pip install --upgrade pip --quiet
Ok 'venv 就緒'

Say "安裝 PyTorch（$cuda，約 2~3GB，會等一下）"
& $pip install torch torchvision torchaudio --index-url "https://download.pytorch.org/whl/$cuda"
if ($LASTEXITCODE -ne 0) { Die 'PyTorch 安裝失敗' }
$torchOk = & $vpy -c "import torch;print(torch.cuda.is_available())"
if ($torchOk.Trim() -ne 'True') { Die 'PyTorch 裝好了但看不到顯卡，請更新顯卡驅動。' }
Ok 'PyTorch 認得顯卡'

# ---- 2. ComfyUI ------------------------------------------------------------
Say ' 安裝 ComfyUI'
if (-not (Test-Path "$root\ComfyUI")) {
  & git clone https://github.com/comfyanonymous/ComfyUI.git "$root\ComfyUI"
} else {
  Ok 'ComfyUI 已存在，跳過下載'
}
& $pip install -r "$root\ComfyUI\requirements.txt"
Ok 'ComfyUI 就緒'

Say '安裝擴充節點'
$nodes = @(
  @{ name = 'ComfyUI-GGUF'; url = 'https://github.com/city96/ComfyUI-GGUF.git' },
  @{ name = 'ComfyUI-VideoHelperSuite'; url = 'https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git' },
  @{ name = 'ComfyUI-Manager'; url = 'https://github.com/ltdrdata/ComfyUI-Manager.git' }
)
foreach ($n in $nodes) {
  $dest = "$root\ComfyUI\custom_nodes\$($n.name)"
  if (-not (Test-Path $dest)) { & git clone $n.url $dest }
  $req = "$dest\requirements.txt"
  if (Test-Path $req) { & $pip install -r $req --quiet }
  Ok $n.name
}

Say '安裝這個 app'
& $pip install -r "$root\app\requirements.txt" --quiet
Ok 'app 就緒'

# ---- 3. 模型 ---------------------------------------------------------------
$models = "$root\ComfyUI\models"
foreach ($d in 'diffusion_models', 'unet', 'text_encoders', 'vae', 'loras') {
  New-Item -ItemType Directory -Force -Path "$models\$d" | Out-Null
}

function Get-Model($repo, $path, $dest) {
  $url = "https://huggingface.co/$repo/resolve/main/$path"
  $name = Split-Path $dest -Leaf
  if (Test-Path $dest) {
    $localSize = (Get-Item $dest).Length
    $head = & curl.exe -sIL $url
    $remote = ($head | Select-String -Pattern '^(x-linked-size|content-length):\s*(\d+)' |
               Select-Object -Last 1).Matches.Groups[2].Value
    if ($remote -and [int64]$remote -eq $localSize) { Ok "$name（已完成）"; return }
    Write-Host "  續傳 $name" -ForegroundColor Yellow
  } else {
    Write-Host "  下載 $name" -ForegroundColor Gray
  }
  & curl.exe -fL --retry 5 --retry-delay 2 --retry-all-errors -C - -o $dest $url
  if (-not (Test-Path $dest)) { Die "下載失敗：$name" }
}

if ($SkipModels) {
  Warn '跳過模型下載（-SkipModels）'
} else {
  $repack = 'Comfy-Org/Wan_2.2_ComfyUI_Repackaged'
  Say '下載共用元件（約 8GB）'
  Get-Model $repack 'split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors' "$models\text_encoders\umt5_xxl_fp8_e4m3fn_scaled.safetensors"
  Get-Model $repack 'split_files/vae/wan_2.1_vae.safetensors' "$models\vae\wan_2.1_vae.safetensors"
  Get-Model $repack 'split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors' "$models\loras\wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors"
  Get-Model $repack 'split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors' "$models\loras\wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"

  if ($Profile -eq 'fp8') {
    Say '下載主模型 fp8（2 × 14.3GB，很久）'
    Get-Model $repack 'split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors' "$models\diffusion_models\wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors"
    Get-Model $repack 'split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors' "$models\diffusion_models\wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors"
  } else {
    Say "下載主模型 GGUF $Quant"
    Get-Model 'QuantStack/Wan2.2-I2V-A14B-GGUF' "HighNoise/Wan2.2-I2V-A14B-HighNoise-$Quant.gguf" "$models\unet\Wan2.2-I2V-A14B-HighNoise-$Quant.gguf"
    Get-Model 'QuantStack/Wan2.2-I2V-A14B-GGUF' "LowNoise/Wan2.2-I2V-A14B-LowNoise-$Quant.gguf" "$models\unet\Wan2.2-I2V-A14B-LowNoise-$Quant.gguf"
  }
}

# ---- 4. 設定檔 -------------------------------------------------------------
Say '寫入設定'
$comfyArgs = if ($vramGB -lt 12) { '--lowvram' } elseif ($vramGB -lt 20) { '--normalvram' } else { '' }
if (-not (Test-Path "$root\.env")) {
  @"
PROFILE=$Profile
GGUF_QUANT=$Quant
LIGHTNING=true
TIER=480p
LENGTH=81
FPS=16
LORAS=
COMFY_ARGS=$comfyArgs
"@ | Set-Content -Path "$root\.env" -Encoding UTF8
  Ok '.env 已建立'
} else {
  Ok '.env 已存在，保留原設定'
}

New-Item -ItemType Directory -Force -Path "$root\data\outputs", "$root\data\inbox" | Out-Null

Say '完成'
Write-Host @"
接下來每次要用，只要在這個資料夾執行：

    .\start-windows.ps1

它會開兩個黑色視窗（ComfyUI 和 app，都不要關），然後自動打開瀏覽器。
"@ -ForegroundColor Green

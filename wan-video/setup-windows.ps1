# 一鍵安裝（Windows + NVIDIA 顯卡）
#
#   最簡單的用法：直接雙擊 install.bat
#
#   或在這個資料夾按右鍵 → 「在終端中開啟」，然後貼上：
#     powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1
#
#   選項：
#   -Model wan22-14b-q4   裝指定的模型（不給就依顯存自動挑）
#   -SkipModels           只裝程式，模型稍後在網頁上挑
#
# 這個檔案必須存成「UTF-8 with BOM + CRLF」。Windows PowerShell 5.1 在沒有 BOM 時
# 會用系統的 ANSI codepage 讀檔，中文會變成亂碼，而 Big5 的次位元組包含 { } ' " \
# 這些字元，會讓整份腳本語法錯誤。這裡也刻意不使用 here-string（@'...'@），
# 因為 5.1 在 LF-only 換行下無法正確結束 here-string。
[CmdletBinding()]
param(
  [string]$Model = '',
  [switch]$SkipModels
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
Set-Location $root

function Say($m) { Write-Host ''; Write-Host "=== $m ===" -ForegroundColor Cyan }
function Ok($m) { Write-Host "  OK  $m" -ForegroundColor Green }
function Warn($m) { Write-Host "  !!  $m" -ForegroundColor Yellow }
function Die($lines) {
  Write-Host ''
  Write-Host '失敗：' -ForegroundColor Red
  foreach ($line in @($lines)) { Write-Host "  $line" -ForegroundColor Red }
  Write-Host ''
  Write-Host '（修好之後重跑這個腳本，已經下載的東西不會重來）' -ForegroundColor Gray
  exit 1
}

# ---- 0. 檢查環境 ------------------------------------------------------------
Say '檢查環境'

if (-not (Get-Command nvidia-smi -ErrorAction SilentlyContinue)) {
  Die @(
    '找不到 nvidia-smi，表示沒有 NVIDIA 顯卡驅動。',
    '這套東西一定要 NVIDIA 顯卡（AMD / Intel / 內顯都跑不動）。',
    '請先到 https://www.nvidia.com/download/index.aspx 安裝驅動再重來。'
  )
}

$gpuName = (& nvidia-smi --query-gpu=name --format=csv,noheader | Select-Object -First 1).Trim()
$vramMB = [int]((& nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits | Select-Object -First 1).Trim())
$vramGB = [math]::Round($vramMB / 1024, 1)
Ok "顯卡：$gpuName（${vramGB}GB 顯存）"

# Pick a starter model that actually fits this card. Everything else can be
# added later from the web UI's model manager.
if (-not $Model) {
  if ($vramGB -ge 24) { $Model = 'wan22-14b-fp8' }
  elseif ($vramGB -ge 16) { $Model = 'wan22-14b-q8' }
  elseif ($vramGB -ge 12) { $Model = 'wan22-14b-q4' }
  else { $Model = 'hy15-480p' }
}
if ($vramGB -lt 8) {
  Warn "顯存只有 ${vramGB}GB，跑起來會非常慢甚至失敗。建議 12GB 以上。"
}
Ok "先裝的模型：$Model（之後可以在網頁上加裝其他的）"

$pyHelp = @(
  '請到 https://www.python.org/downloads/ 下載 3.12 版，',
  '安裝時務必勾選最下面的「Add python.exe to PATH」，',
  '裝完把這個視窗關掉重新開一個，再執行一次這個腳本。'
)

$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { Die (@('找不到 Python。') + $pyHelp) }

# Windows ships a 0-byte python.exe stub under WindowsApps that just opens the
# Microsoft Store. Get-Command finds it, so check for it explicitly rather than
# letting the version probe fail with something unreadable.
if ($py.Source -like '*\WindowsApps\*') {
  Die (@("找到的 python 是 Windows 商店的空殼（$($py.Source)），不是真的 Python。") + $pyHelp)
}

$pyVer = $null
try {
  $pyVer = (& python -c "import sys;print('%d.%d' % sys.version_info[:2])" 2>$null | Select-Object -First 1)
} catch { }
if (-not $pyVer -or $pyVer -notmatch '^\d+\.\d+$') {
  Die (@("python 有找到（$($py.Source)）但問不出版本，可能裝壞了。") + $pyHelp)
}
$pyVer = $pyVer.Trim()
if ([version]$pyVer -lt [version]'3.10' -or [version]$pyVer -ge [version]'3.14') {
  Die (@("Python 版本是 $pyVer，需要 3.10 ~ 3.13。建議裝 3.12。") + $pyHelp)
}
Ok "Python $pyVer（$($py.Source)）"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  Die @(
    '找不到 git。請到 https://git-scm.com/download/win 下載安裝',
    '（一路 Next 用預設值），裝完把這個視窗關掉重新開一個，再執行一次。'
  )
}
Ok 'git'

# 50 系列（Blackwell）需要 CUDA 12.8 版的 PyTorch
$cuda = if ($gpuName -match 'RTX\s*50\d\d') { 'cu128' } else { 'cu126' }
Ok "PyTorch 版本：$cuda"

# A free-space read must never abort the install, and Get-PSDrive throws on
# UNC paths (where there is no drive letter to ask about).
$freeGB = $null
try { $freeGB = [math]::Round((Get-PSDrive -Name $root.Substring(0, 1) -ErrorAction Stop).Free / 1GB, 1) } catch { }
if ($null -eq $freeGB) {
  Warn '看不出這個位置的剩餘空間。請自己確認有 60GB 以上。'
} elseif ($freeGB -lt 60) {
  Warn "這個磁碟只剩 ${freeGB}GB。程式約 10GB，模型 18~43GB，建議留 60GB 以上。"
} else {
  Ok "磁碟空間：剩 ${freeGB}GB"
}

# ---- 1. 虛擬環境 ------------------------------------------------------------
Say '建立 Python 虛擬環境'
if (-not (Test-Path "$root\venv")) { & python -m venv "$root\venv" }
$vpy = "$root\venv\Scripts\python.exe"
# Everything below goes through "python.exe -m pip" rather than pip.exe. The
# .exe shims in a venv hard-code the absolute path of the interpreter they were
# built against, so a venv stops working the moment the folder is moved - and
# moving the folder is the standard cure for Windows refusing writes on the
# Desktop. Invoked this way, the whole tree can be dragged anywhere.
if (-not (Test-Path $vpy)) { Die 'venv 建立失敗，$root\venv\Scripts\python.exe 不存在。' }
& $vpy -m pip install --upgrade pip --quiet
Ok 'venv 就緒'

Say "安裝 PyTorch（$cuda，約 2~3GB，會等一下）"
& $vpy -m pip install torch torchvision torchaudio --index-url "https://download.pytorch.org/whl/$cuda"
if ($LASTEXITCODE -ne 0) { Die 'PyTorch 安裝失敗。檢查網路，然後重跑這個腳本。' }
$torchOk = (& $vpy -c "import torch; print(torch.cuda.is_available())" | Select-Object -First 1)
if ("$torchOk".Trim() -ne 'True') {
  Die @(
    'PyTorch 裝好了但看不到顯卡。',
    '通常是顯卡驅動太舊 —— 到 https://www.nvidia.com/download/index.aspx 更新後重跑。'
  )
}
Ok 'PyTorch 認得顯卡'

# ---- 2. ComfyUI ------------------------------------------------------------
Say '安裝 ComfyUI'
if (-not (Test-Path "$root\ComfyUI")) {
  & git clone https://github.com/comfyanonymous/ComfyUI.git "$root\ComfyUI"
  if ($LASTEXITCODE -ne 0) { Die 'ComfyUI 下載失敗。檢查網路後重跑。' }
} else {
  Ok 'ComfyUI 已存在，跳過下載'
}
& $vpy -m pip install -r "$root\ComfyUI\requirements.txt"
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
  if (Test-Path $req) { & $vpy -m pip install -r $req --quiet }
  Ok $n.name
}

Say '安裝這個 app'
& $vpy -m pip install -r "$root\app\requirements.txt" --quiet
Ok 'app 就緒'

# ---- 3. 模型 ---------------------------------------------------------------
$models = "$root\ComfyUI\models"
foreach ($d in 'diffusion_models', 'unet', 'text_encoders', 'vae', 'loras', 'clip_vision', 'checkpoints', 'latent_upscale_models') {
  New-Item -ItemType Directory -Force -Path "$models\$d" | Out-Null
}

if ($SkipModels) {
  Warn '跳過模型下載（-SkipModels）—— 之後在網頁的「模型管理」下載'
} else {
  Say "下載模型 $Model（很久，可以先去做別的事）"
  & $vpy "$root\scripts\fetch-model.py" $Model --models-dir $models
  if ($LASTEXITCODE -ne 0) {
    Warn '模型沒下載完。重跑這個腳本會續傳，或之後在網頁的「模型管理」按下載。'
  }
}

# ---- 4. 設定檔 -------------------------------------------------------------
Say '寫入設定'
$comfyArgs = if ($vramGB -lt 12) { '--lowvram' } elseif ($vramGB -lt 20) { '--normalvram' } else { '' }
if (-not (Test-Path "$root\.env")) {
  $envLines = @(
    "MODEL=$Model",
    'LIGHTNING=true',
    'LORAS=',
    "COMFY_ARGS=$comfyArgs"
  )
  # Explicitly BOM-less: PowerShell 5.1's -Encoding UTF8 adds a BOM, which would
  # end up glued to the first key name when .env is read back.
  [IO.File]::WriteAllLines("$root\.env", $envLines, (New-Object System.Text.UTF8Encoding $false))
  Ok '.env 已建立'
} else {
  Ok '.env 已存在，保留原設定'
}

New-Item -ItemType Directory -Force -Path "$root\data\outputs", "$root\data\inbox" | Out-Null

Say '完成'
Write-Host '接下來每次要用，只要雙擊 start.bat' -ForegroundColor Green
Write-Host '（或執行 .\start-windows.ps1）' -ForegroundColor Green
Write-Host ''
Write-Host '它會開兩個黑色視窗（ComfyUI 和 app，都不要關），然後自動打開瀏覽器。' -ForegroundColor Green
Write-Host '在網頁的「模型管理」分頁可以直接下載其他模型，不用再回到命令列。' -ForegroundColor Green

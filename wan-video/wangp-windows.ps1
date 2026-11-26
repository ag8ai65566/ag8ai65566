# WanGP（自動導演）：安裝、啟動、更新（Windows）
#
#   最簡單的用法：雙擊 wangp.bat，或在 update-and-start.bat 的選單按 4
#
#   powershell -ExecutionPolicy Bypass -File .\wangp-windows.ps1 [-Action install|start|update|tips]
#
# WanGP 是另一個獨立的開源 app（https://github.com/deepbeepmeep/Wan2GP）。
# 它的 Showrunner 會用本機的語言模型看你的圖、規劃鏡頭、生成、檢查每一段、
# 重做失敗的，最後剪成一支影片。這支腳本只做三件事：
#   1. 把它下載到這個資料夾的 WanGP\ 底下，用它自己的安裝程式（自動模式）裝好；
#   2. 啟動前請 ComfyUI 把顯存讓出來（兩個 app 共用同一張顯卡）；
#   3. 更新時交給它自己的 update.bat。
# 它的環境是獨立的（WanGP\env_venv），不會動到這個 app 的 venv、模型或成品。
#
# 這個檔案必須存成「UTF-8 with BOM + CRLF」，理由見 setup-windows.ps1 的說明。
param([string]$Action = '')

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$wg = Join-Path $root 'WanGP'
$repo = 'https://github.com/deepbeepmeep/Wan2GP.git'
$port = 7860
$url = "http://127.0.0.1:$port"
$manager = 'https://github.com/deepbeepmeep/WanGP/releases/latest/download/WanGPManager.exe'

function Say($m) { Write-Host ''; Write-Host "=== $m ===" -ForegroundColor Cyan }
function Ok($m) { Write-Host "  OK  $m" -ForegroundColor Green }
function Warn($m) { Write-Host "  !!  $m" -ForegroundColor Yellow }
function Die($lines) {
  Write-Host ''
  Write-Host '失敗：' -ForegroundColor Red
  foreach ($line in @($lines)) { Write-Host "  $line" -ForegroundColor Red }
  exit 1
}
function Ask($question) {
  $answer = Read-Host "  $question (Y/N)"
  return ($answer -match '^[Yy]')
}
function Busy($p) {
  $null -ne (Get-NetTCPConnection -LocalPort $p -State Listen -ErrorAction SilentlyContinue)
}
function Test-Installed { Test-Path -LiteralPath (Join-Path $wg 'wgp.py') }
function Test-EnvReady { Test-Path -LiteralPath (Join-Path $wg 'envs.json') }

# Same reason as Invoke-Git in update-windows.ps1: under Windows PowerShell 5.1
# a redirected stderr line becomes a terminating error while the preference is
# 'Stop', so the exit code is read instead.
function Invoke-Native {
  param([string]$Exe, [string[]]$ArgList)
  $prev = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  try {
    $lines = & $Exe @ArgList 2>&1
    $code = $LASTEXITCODE
    $text = ''
    if ($null -ne $lines) {
      $text = (($lines | ForEach-Object { $_.ToString() }) -join "`n").Trim()
    }
    return [pscustomobject]@{ Code = $code; Text = $text }
  } catch {
    return [pscustomobject]@{ Code = -1; Text = $_.Exception.Message }
  } finally {
    $ErrorActionPreference = $prev
  }
}

# For the long steps: the output goes to this window as it happens. Piped to
# Out-Host so it is shown rather than returned as the function's value.
function Invoke-Live {
  param([string]$Exe, [string[]]$ArgList)
  $prev = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  try {
    & $Exe @ArgList | Out-Host
    return $LASTEXITCODE
  } catch {
    Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
    return -1
  } finally {
    $ErrorActionPreference = $prev
  }
}

function Get-Py311 {
  $r = Invoke-Native 'py' @('-3.11', '-c', 'import sys; print(sys.version.split()[0])')
  if ($r.Code -eq 0 -and $r.Text -match '^3\.11\.') { return $r.Text }
  return $null
}

function Get-Gpu {
  $r = Invoke-Native 'nvidia-smi' @('--query-gpu=name,driver_version,memory.total', '--format=csv,noheader,nounits')
  if ($r.Code -ne 0 -or -not $r.Text) { return $null }
  $parts = (($r.Text -split "`n")[0]) -split ',\s*'
  if ($parts.Count -lt 3) { return $null }
  $mem = 0
  [void][int]::TryParse($parts[2].Trim(), [ref]$mem)
  $major = 0
  [void][int]::TryParse(($parts[1].Trim() -split '\.')[0], [ref]$major)
  return [pscustomobject]@{ Name = $parts[0].Trim(); Driver = $parts[1].Trim(); Major = $major; MemMB = $mem }
}

function Show-Tips {
  Say '怎麼用：給一張圖，讓它自己拍成一支影片'
  Write-Host '  1. 上方 app 列打開 Showrunner，選一個格式（Short film 或 Anything），替作品取名。'
  Write-Host '  2. 在 Brief 寫一句想法，把你的圖拖進 Cast（人物）或 References（參考），設定總長度。'
  Write-Host '  3. 按 Plan with the showrunner：它會寫好每一鏡讓你看，想改就改。'
  Write-Host '  4. 按 Shoot：它逐鏡生成、自己檢查每一段、重做失敗的，最後剪成一支，在 Deliver 看。'
  Write-Host '  只要一段影片：一般生成頁選圖生影片模型，用 Prompt Enhancer 讓它看圖寫提詞；要更長就開 Sliding Window。'
  Say '你的顯卡（10GB 左右）'
  Write-Host '  Showrunner 靠 Deepy Prime（本機語言模型）。10GB 顯卡它第一次會自動選 Qwen3.8 的 Bonsai 版（權重不到 6GB）。'
  Write-Host '  Configuration > Deepy / Prompt Enhancer 可以改選 Bonsai 2.5：官方說它專門加強了 Showrunner 這種多步驟工作。'
  Say '成人內容只留在本機'
  Write-Host '  Deepy 和 Prompt Enhancer 都用本機模型。不要接遠端 LLM（Codex、Claude Code 等），也不要打開網路搜尋：'
  Write-Host '  那會把你的圖和文字送出這台電腦。'
  Write-Host '  未成年人物、拿真人的臉做性內容：不管用哪個工具都不做。'
  Say '和這個 app 一起用'
  Write-Host '  兩個 app 共用同一張顯卡：同一時間只讓一邊生成。'
  Write-Host '  WanGP 的 MCP 伺服器預設用 8000 port，跟這個 app 撞在一起；要開 MCP 的話先在 Configuration > Agents 改 port。'
  Write-Host "  WanGP 的網址：$url"
}

function Install-WanGP {
  Say '檢查'
  $git = Invoke-Native 'git' @('--version')
  if ($git.Code -ne 0) {
    Die @('找不到 Git（這個 app 安裝時也需要它）：https://git-scm.com/download/win', '裝好後關掉這個視窗，再執行一次。')
  }
  Ok $git.Text

  $gpu = Get-Gpu
  if ($null -eq $gpu) {
    Warn '讀不到 NVIDIA 顯卡（nvidia-smi 沒有回應）。WanGP 要 NVIDIA 顯卡（或它另外支援的 AMD 顯卡）。'
    if (-not (Ask '還是要繼續嗎？')) { exit 1 }
  } else {
    Ok ("顯卡：" + $gpu.Name + "，" + [math]::Round($gpu.MemMB / 1024) + " GB，驅動 " + $gpu.Driver)
    if ($gpu.Major -gt 0 -and $gpu.Major -lt 580) {
      Warn ("驅動 " + $gpu.Driver + " 偏舊。WanGP 給 RTX 30 系列裝的是 CUDA 13 版的 PyTorch，")
      Warn 'CUDA 13 要 580 版以上的驅動。先用 NVIDIA App 或 https://www.nvidia.com/drivers 更新，再回來裝。'
      if (-not (Ask '不更新、直接繼續嗎？')) { exit 1 }
    }
  }

  $free = (Get-Item -LiteralPath $root).PSDrive.Free
  $freeGB = [math]::Round($free / 1GB)
  if ($freeGB -lt 60) {
    Warn "這顆硬碟只剩 $freeGB GB。WanGP 的環境加上第一次用時下載的模型，很容易就要幾十 GB。"
    if (-not (Ask '還是要繼續嗎？')) { exit 1 }
  } else {
    Ok "硬碟剩 $freeGB GB"
  }

  $py = Get-Py311
  if (-not $py) {
    Warn 'WanGP 在 RTX 30 系列上要用 Python 3.11 建它自己的環境。'
    Warn '這個 app 用的 Python 3.12 不受影響，兩個版本可以並存。'
    if (-not (Ask '現在用 winget 自動安裝 Python 3.11 嗎？')) {
      Die @('請手動安裝 Python 3.11（64-bit）：https://www.python.org/downloads/windows/', '安裝畫面記得勾 py launcher，裝好後再執行一次。')
    }
    $winget = Invoke-Native 'winget' @('--version')
    if ($winget.Code -ne 0) {
      Die @('這台電腦沒有 winget。請手動安裝 Python 3.11（64-bit）：https://www.python.org/downloads/windows/', '裝好後再執行一次。')
    }
    $code = Invoke-Live 'winget' @('install', '-e', '--id', 'Python.Python.3.11', '--scope', 'user', '--accept-package-agreements', '--accept-source-agreements')
    $py = Get-Py311
    if (-not $py) {
      Die @("winget 裝完了（代碼 $code），但 py -3.11 還是找不到。", '關掉這個視窗、重新執行一次；還是不行就手動安裝：https://www.python.org/downloads/windows/')
    }
  }
  Ok "Python $py（給 WanGP 用）"

  Say '下載 WanGP'
  if (Test-Path -LiteralPath $wg) {
    if (-not (Test-Path -LiteralPath (Join-Path $wg '.git'))) {
      Die @("$wg 已經存在，但不是 WanGP 的 git 資料夾。", '把它改名或刪掉，再執行一次。')
    }
    Ok '已經下載過，沿用'
  } else {
    $code = Invoke-Live 'git' @('clone', $repo, $wg)
    if ($code -ne 0 -or -not (Test-Installed)) {
      Die @('下載失敗（看上面 git 的訊息）。檢查網路後再試一次。')
    }
    Ok "WanGP 放在 $wg"
  }

  Say '安裝 WanGP 的環境'
  Write-Host '  用 WanGP 自己的安裝程式（自動模式）：它會依你的顯卡建一個獨立的 Python 3.11 環境，'
  Write-Host '  裝 PyTorch 和加速套件。要一段時間，請不要關掉這個視窗。'
  Push-Location -LiteralPath $wg
  try {
    $code = Invoke-Live 'py' @('-3.11', 'setup.py', 'install', '--env', 'venv', '--auto')
  } finally {
    Pop-Location
  }
  if ($code -ne 0 -or -not (Test-EnvReady)) {
    Die @(
      "WanGP 的安裝程式回報失敗（代碼 $code，看上面的訊息）。",
      "也可以改用 WanGP 官方的安裝器：$manager",
      "執行後選 Install / Add -> Use existing installation，指到 $wg。"
    )
  }
  Ok '安裝完成。第一次啟動時，它會再下載你選的模型。'
}

function Start-WanGP {
  if (-not (Test-Installed) -or -not (Test-EnvReady)) {
    Die @('WanGP 還沒裝好。先選「安裝」。')
  }
  if (Busy $port) {
    Ok "WanGP 已經在跑了：$url"
    Start-Process $url
    return
  }
  if (Busy 8188) {
    try {
      Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:8188/free' -ContentType 'application/json' -Body '{"unload_models": true, "free_memory": true}' -TimeoutSec 10 | Out-Null
      Ok '已請 ComfyUI 把顯存讓出來（兩個 app 共用同一張顯卡）'
    } catch {
      Warn 'ComfyUI 沒有回應「釋放顯存」。如果 WanGP 說顯存不夠，先把這個 app 的兩個黑視窗關掉。'
    }
  }
  Say '啟動 WanGP'
  Start-Process -FilePath 'cmd.exe' -ArgumentList '/c', 'scripts\run.bat' -WorkingDirectory $wg
  Write-Host '  開了一個新的黑視窗給 WanGP，用的時候不要關。'
  Write-Host '  第一次啟動比較久（它會準備需要的檔案）。好了會自動開瀏覽器。'
  for ($i = 0; $i -lt 180; $i++) {
    if (Busy $port) {
      Ok "WanGP 好了：$url"
      Start-Process $url
      return
    }
    Start-Sleep -Seconds 5
  }
  Warn "等了 15 分鐘還沒好。看 WanGP 那個黑視窗的訊息；好了之後自己打開 $url"
}

function Update-WanGP {
  if (-not (Test-Installed)) { Die @('WanGP 還沒裝。先選「安裝」。') }
  if (Busy $port) {
    Warn 'WanGP 還在跑。先關掉它的黑視窗再更新。'
    if (-not (Ask '已經關了，繼續嗎？')) { exit 1 }
  }
  Say '更新 WanGP（交給它自己的 update.bat）'
  Write-Host '  選 1 是一般更新（拉新程式 + 補套件）；2 是升級 PyTorch 等大套件，沒問題就不用選。'
  Push-Location -LiteralPath $wg
  try {
    $code = Invoke-Live 'cmd.exe' @('/c', 'scripts\update.bat')
  } finally {
    Pop-Location
  }
}

Set-Location -LiteralPath $root
if (-not $Action) {
  Write-Host ''
  Write-Host '  WanGP：給一張圖，它自己判斷、自己拍成連續影片（全部在本機）' -ForegroundColor Cyan
  Write-Host ''
  if ((Test-Installed) -and (Test-EnvReady)) {
    Write-Host '    [1] 啟動'
    Write-Host '    [2] 更新'
    Write-Host '    [3] 怎麼用'
    $pick = Read-Host '  按 1、2 或 3'
    $Action = @{ '1' = 'start'; '2' = 'update'; '3' = 'tips' }[$pick.Trim()]
  } else {
    Write-Host '    還沒安裝。[1] 安裝（第一次，要一段時間）  [3] 怎麼用'
    $pick = Read-Host '  按 1 或 3'
    $Action = @{ '1' = 'install'; '3' = 'tips' }[$pick.Trim()]
  }
  if (-not $Action) { exit 0 }
}

switch ($Action.ToLower()) {
  'install' {
    Install-WanGP
    Show-Tips
    if (Ask '現在啟動 WanGP 嗎？') { Start-WanGP }
  }
  'start' { Start-WanGP }
  'update' { Update-WanGP }
  'tips' { Show-Tips }
  default { Die @("不認識的動作：$Action（可以用 install、start、update、tips）") }
}

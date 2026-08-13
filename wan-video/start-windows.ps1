# 啟動（Windows）。setup-windows.ps1 跑完之後，每次只要執行這個。
#
#   最簡單的用法：直接雙擊 start.bat
#
#   或：powershell -ExecutionPolicy Bypass -File .\start-windows.ps1
#   -Watch  同時啟動拖檔模式：丟進 data\inbox 的圖片會自動生成
#
# 這個檔案必須存成「UTF-8 with BOM + CRLF」，理由見 setup-windows.ps1 的說明。
param([switch]$Watch)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
Set-Location $root

$vpy = "$root\venv\Scripts\python.exe"
if (-not (Test-Path $vpy)) {
  Write-Host '還沒安裝。請先雙擊 install.bat（或執行 setup-windows.ps1）。' -ForegroundColor Red
  exit 1
}

# .env -> 這個行程的環境變數，兩個子行程都會繼承。
# \uFEFF? 是為了容忍別人用「UTF-8 with BOM」的編輯器存過 .env —— 否則那個 BOM
# 會黏在第一個變數名前面，讓第一行整行被忽略。
if (Test-Path "$root\.env") {
  foreach ($line in Get-Content "$root\.env") {
    if ($line -match '^\uFEFF?\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$') {
      [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2].Trim(), 'Process')
    }
  }
}
$env:COMFY_URL = 'http://127.0.0.1:8188'
# The model manager downloads straight into ComfyUI's own models tree.
$env:MODELS_DIR = "$root\ComfyUI\models"
$env:OUTPUT_DIR = "$root\data\outputs"
$env:INBOX_DIR = "$root\data\inbox"
$env:DONE_DIR = "$root\data\inbox\done"
$env:APP_URL = 'http://127.0.0.1:8000'
New-Item -ItemType Directory -Force -Path $env:OUTPUT_DIR, $env:INBOX_DIR | Out-Null

function Busy($port) {
  $null -ne (Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue)
}

if (Busy 8188) {
  Write-Host 'ComfyUI 已經在跑（8188），沿用它' -ForegroundColor Yellow
} else {
  Write-Host '啟動 ComfyUI…' -ForegroundColor Cyan
  $extra = @()
  if ("$env:COMFY_ARGS".Trim()) { $extra = "$env:COMFY_ARGS".Trim() -split '\s+' }
  $comfyArgList = @('main.py', '--listen', '127.0.0.1', '--port', '8188') + $extra
  Start-Process -FilePath $vpy -ArgumentList $comfyArgList -WorkingDirectory "$root\ComfyUI"
}

if (Busy 8000) {
  Write-Host 'app 已經在跑（8000）' -ForegroundColor Yellow
} else {
  Write-Host '啟動 app…' -ForegroundColor Cyan
  Start-Process -FilePath $vpy -ArgumentList @('-m', 'uvicorn', 'server:app', '--host', '127.0.0.1', '--port', '8000') -WorkingDirectory "$root\app"
}

if ($Watch) {
  Write-Host "啟動拖檔監看（$env:INBOX_DIR）…" -ForegroundColor Cyan
  Start-Process -FilePath $vpy -ArgumentList @('watcher.py') -WorkingDirectory "$root\app"
}

Write-Host '等 ComfyUI 載入（第一次可能要一兩分鐘）…' -ForegroundColor Gray
$ready = $false
foreach ($i in 1..150) {
  try {
    $raw = (Invoke-WebRequest -Uri 'http://127.0.0.1:8000/api/health' -TimeoutSec 5 -UseBasicParsing).Content
    if (($raw | ConvertFrom-Json).comfy.ok) { $ready = $true; break }
  } catch { }
  Start-Sleep -Seconds 2
}

Write-Host ''
if ($ready) {
  Write-Host '好了。瀏覽器開 http://127.0.0.1:8000' -ForegroundColor Green
  Write-Host 'ComfyUI 本身在 http://127.0.0.1:8188（要調 LoRA / 看細節時才用）' -ForegroundColor Gray
  Start-Process 'http://127.0.0.1:8000'
} else {
  Write-Host 'ComfyUI 遲遲沒就緒。看一下那兩個黑視窗裡的紅字訊息。' -ForegroundColor Red
  Write-Host '也可以執行檢查工具：' -ForegroundColor Gray
  Write-Host '    .\venv\Scripts\python.exe app\check.py' -ForegroundColor Gray
}

Write-Host ''
Write-Host '那兩個黑視窗不要關掉，關掉就停了。' -ForegroundColor Yellow

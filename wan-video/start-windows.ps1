# 啟動（Windows）。setup-windows.ps1 跑完之後，每次只要執行這個。
#
#   powershell -ExecutionPolicy Bypass -File .\start-windows.ps1
#
#   -Watch  同時啟動拖檔模式：丟進 data\inbox 的圖片會自動生成
param([switch]$Watch)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
Set-Location $root

$vpy = "$root\venv\Scripts\python.exe"
if (-not (Test-Path $vpy)) {
  Write-Host '還沒安裝。請先執行： powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1' -ForegroundColor Red
  exit 1
}

# .env -> 這個行程的環境變數，兩個子行程都會繼承
if (Test-Path "$root\.env") {
  Get-Content "$root\.env" | ForEach-Object {
    if ($_ -match '^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$') {
      [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2].Trim(), 'Process')
    }
  }
}
$env:COMFY_URL = 'http://127.0.0.1:8188'
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
  $comfyArgs = "$env:COMFY_ARGS".Trim()
  Start-Process -FilePath $vpy `
    -ArgumentList (@('main.py', '--listen', '127.0.0.1', '--port', '8188') + ($comfyArgs -split '\s+' | Where-Object { $_ })) `
    -WorkingDirectory "$root\ComfyUI"
}

if (Busy 8000) {
  Write-Host 'app 已經在跑（8000）' -ForegroundColor Yellow
} else {
  Write-Host '啟動 app…' -ForegroundColor Cyan
  Start-Process -FilePath $vpy `
    -ArgumentList @('-m', 'uvicorn', 'server:app', '--host', '127.0.0.1', '--port', '8000') `
    -WorkingDirectory "$root\app"
}

if ($Watch) {
  Write-Host "啟動拖檔監看（$env:INBOX_DIR）…" -ForegroundColor Cyan
  Start-Process -FilePath $vpy -ArgumentList @('watcher.py') -WorkingDirectory "$root\app"
}

Write-Host '等 ComfyUI 載入（第一次可能要一兩分鐘）…' -ForegroundColor Gray
$ready = $false
foreach ($i in 1..150) {
  try {
    Invoke-WebRequest -Uri 'http://127.0.0.1:8000/api/health' -TimeoutSec 3 -UseBasicParsing | Out-Null
    $health = (Invoke-WebRequest -Uri 'http://127.0.0.1:8000/api/health' -TimeoutSec 5 -UseBasicParsing).Content | ConvertFrom-Json
    if ($health.comfy.ok) { $ready = $true; break }
  } catch { }
  Start-Sleep -Seconds 2
}

if ($ready) {
  Write-Host "`n好了。瀏覽器開 http://127.0.0.1:8000" -ForegroundColor Green
  Write-Host "ComfyUI 本身在 http://127.0.0.1:8188（要調 LoRA / 看細節時才用）" -ForegroundColor Gray
  Start-Process 'http://127.0.0.1:8000'
} else {
  Write-Host "`nComfyUI 遲遲沒就緒。看一下那兩個黑視窗裡的紅字訊息。" -ForegroundColor Red
  Write-Host '也可以執行檢查工具：' -ForegroundColor Gray
  Write-Host "    .\venv\Scripts\python.exe app\check.py" -ForegroundColor Gray
}

Write-Host "`n那兩個黑視窗不要關掉，關掉就停了。" -ForegroundColor Yellow

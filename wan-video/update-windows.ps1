# 更新程式碼到最新版（Windows）
#
#   最簡單的用法：雙擊 update.bat
#
# 只換程式碼。以下這些一律不動，所以幾十 GB 的模型和你的成品都會留著：
#   ComfyUI\  venv\  data\  models\  .env
#
# 這個檔案必須存成「UTF-8 with BOM + CRLF」，理由見 setup-windows.ps1 的說明。
param(
  [string]$Branch = 'claude/local-image-to-animation-ai-375zyw',
  [switch]$Force
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
  exit 1
}

# 這些絕對不覆蓋。zip 裡本來就沒有，這裡再擋一層。
$keep = @('ComfyUI', 'venv', 'data', 'models', '.env')

Say '檢查'
if (-not (Test-Path "$root\app\server.py")) {
  Die @(
    "這裡看起來不是 wan-video 資料夾（找不到 app\server.py）。",
    "請把 update.bat 放在 wan-video 裡面再執行。"
  )
}
Ok "資料夾：$root"

# app 還在跑的話，換掉的檔案要重啟才會生效 —— 先講清楚。
$busy = @()
foreach ($port in 8188, 8000) {
  if (Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue) { $busy += $port }
}
if ($busy.Count -and -not $Force) {
  Warn "偵測到 app 還在跑（port $($busy -join '、')）。"
  Write-Host '  更新完一定要把那兩個黑視窗關掉、重新跑 start.bat，新程式才會生效。' -ForegroundColor Yellow
  $answer = Read-Host '  現在繼續更新嗎？(Y/N)'
  if ($answer -notmatch '^[Yy]') { Write-Host '  取消。'; exit 0 }
}

$tmp = Join-Path $env:TEMP ("wan-update-" + [guid]::NewGuid().ToString('N').Substring(0, 8))
New-Item -ItemType Directory -Force -Path $tmp | Out-Null
$zip = Join-Path $tmp 'src.zip'
$url = "https://github.com/ag8ai65566/ag8ai65566/archive/refs/heads/$Branch.zip"

try {
  Say '下載最新程式碼'
  Write-Host "  $url" -ForegroundColor Gray
  # curl.exe ships with Windows 10 1803+ and follows redirects properly.
  & curl.exe -fL --retry 4 --retry-delay 2 --retry-all-errors -o $zip $url
  if (-not (Test-Path $zip) -or (Get-Item $zip).Length -lt 1000) {
    Die @("下載失敗或檔案是空的。", "檢查網路，或確認分支名稱對不對：$Branch")
  }
  Ok ("下載完成（" + [math]::Round((Get-Item $zip).Length / 1KB) + " KB）")

  Say '解壓縮'
  Expand-Archive -Path $zip -DestinationPath $tmp -Force
  $src = Get-ChildItem -Path $tmp -Directory |
         ForEach-Object { Join-Path $_.FullName 'wan-video' } |
         Where-Object { Test-Path $_ } |
         Select-Object -First 1
  if (-not $src) { Die 'zip 裡找不到 wan-video 資料夾 —— 分支結構變了？' }
  Ok '解壓縮完成'

  Say '複製程式碼（保留模型與設定）'
  $copied = 0
  foreach ($entry in Get-ChildItem -Path $src -Force) {
    if ($keep -contains $entry.Name) { Warn "跳過 $($entry.Name)（保留你現有的）"; continue }
    Copy-Item -Path $entry.FullName -Destination $root -Recurse -Force
    Write-Host "  → $($entry.Name)" -ForegroundColor Gray
    $copied++
  }
  Ok "$copied 個項目已更新"

  foreach ($name in $keep) {
    if (Test-Path (Join-Path $root $name)) { Ok "$name 沒有被動到" }
  }

  Say '補裝可能新增的 Python 套件'
  $pip = "$root\venv\Scripts\pip.exe"
  if (Test-Path $pip) {
    & $pip install -r "$root\app\requirements.txt" --quiet
    Ok '套件已同步'
  } else {
    Warn 'venv 不存在，跳過。之後跑 install.bat 會建立。'
  }
} finally {
  Remove-Item -Path $tmp -Recurse -Force -ErrorAction SilentlyContinue
}

Say '完成'
Write-Host '程式碼已是最新版。模型、成品、.env 都保留。' -ForegroundColor Green
if ($busy.Count) {
  Write-Host ''
  Write-Host '請把那兩個黑視窗關掉，再雙擊 start.bat —— 新程式要重啟才生效。' -ForegroundColor Yellow
} else {
  Write-Host '雙擊 start.bat 就可以用了。' -ForegroundColor Green
}

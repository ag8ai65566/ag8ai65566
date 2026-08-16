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

# Windows refuses a write for several different reasons that all surface as the
# same "Access to the path ... is denied". Naming the likely one saves an hour.
function Get-BlockReasons($path) {
  $why = @()
  try {
    $cfa = (Get-MpPreference -ErrorAction Stop).EnableControlledFolderAccess
    if ($cfa -eq 1) {
      $why += "Windows 資安的「受控資料夾存取」是開的。它專門擋程式寫入桌面／文件夾，"
      $why += "這正是你這個資料夾的位置。到「Windows 安全性 → 病毒與威脅防護 →"
      $why += "勒索軟體防護 → 允許應用程式通過受控資料夾存取」把 PowerShell 加進去，"
      $why += "或直接把 anim 資料夾搬離桌面（例如 C:\anim）。"
    }
  } catch { }
  if ($env:OneDrive -and $path.StartsWith($env:OneDrive, 'OrdinalIgnoreCase')) {
    $why += "這個資料夾在 OneDrive 底下，同步中的檔案會被鎖住。暫停 OneDrive 同步，"
    $why += "或把資料夾搬到不同步的地方（例如 C:\anim）。"
  }
  $desktop = [Environment]::GetFolderPath('Desktop')
  if ($desktop -and $path.StartsWith($desktop, 'OrdinalIgnoreCase') -and -not $why.Count) {
    $why += "資料夾在桌面上。桌面常被 OneDrive 同步或防毒軟體特別保護，"
    $why += "把它搬到 C:\anim 之類的地方通常就好了。"
  }
  if (-not $why.Count) {
    $why += "可能是防毒軟體擋住，或有程式正開著那個檔案（編輯器？檔案總管預覽窗格？）。"
  }
  return $why
}

# Copy-Item -Force handles a read-only destination but not a locked one, and a
# lock is usually momentary. Clear the attribute, then retry a few times.
function Copy-One($from, $to) {
  $dir = Split-Path -Parent $to
  if ($dir -and -not (Test-Path -LiteralPath $dir)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
  }
  for ($try = 1; $try -le 4; $try++) {
    try {
      if (Test-Path -LiteralPath $to) {
        $item = Get-Item -LiteralPath $to -Force
        if ($item.Attributes -band [IO.FileAttributes]::ReadOnly) {
          $item.Attributes = [IO.FileAttributes]::Normal
        }
      }
      Copy-Item -LiteralPath $from -Destination $to -Force -ErrorAction Stop
      return $true
    } catch {
      if ($try -eq 4) { return $false }
      Start-Sleep -Milliseconds (200 * $try)
    }
  }
  return $false
}

# Can we actually open this for writing right now? Asked about every file we are
# about to overwrite, *before* overwriting any of them. Read-only is not a
# blocker because the copy clears it, so this clears it too - and puts it back
# if the write turns out to be blocked anyway, so a refused update really does
# leave everything as it was.
function Test-Writable($path) {
  $item = $null
  $was = $null
  try {
    $item = Get-Item -LiteralPath $path -Force -ErrorAction Stop
    $was = $item.Attributes
    if ($was -band [IO.FileAttributes]::ReadOnly) {
      $item.Attributes = [IO.FileAttributes]::Normal
    }
    $stream = [System.IO.File]::Open($path, 'Open', 'Write', 'None')
    $stream.Close()
    return $true
  } catch {
    if ($item -and $null -ne $was) {
      try { $item.Attributes = $was } catch { }
    }
    return $false
  }
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

  # Everything the update would write, as paths relative to the source root.
  # Flattened on purpose: the old code handed whole directories to Copy-Item
  # -Recurse, so one unwritable file part-way through left app\ holding a mix of
  # new and old modules. That runs, and then fails later in ways that look like
  # a bug in the program rather than a half-finished update.
  $plan = @()
  foreach ($file in Get-ChildItem -Path $src -Recurse -File -Force) {
    $rel = $file.FullName.Substring($src.Length).TrimStart('\')
    if ($keep -contains $rel.Split('\')[0]) { continue }
    $plan += [pscustomobject]@{
      Rel  = $rel
      From = $file.FullName
      To   = Join-Path $root $rel
      Size = $file.Length
    }
  }
  if (-not $plan.Count) { Die 'zip 裡沒有可複製的檔案 —— 下載壞掉了？' }

  Say '檢查檔案能不能寫'
  $blocked = @($plan | Where-Object { (Test-Path -LiteralPath $_.To) -and -not (Test-Writable $_.To) })
  if ($blocked.Count) {
    Write-Host ''
    Write-Host "  有 $($blocked.Count) 個檔案不能覆蓋，例如：" -ForegroundColor Red
    foreach ($b in ($blocked | Select-Object -First 5)) {
      Write-Host "    $($b.Rel)" -ForegroundColor Red
    }
    Write-Host ''
    Write-Host '  什麼都還沒改 —— 你原本的程式是完整的，可以照常使用。' -ForegroundColor Yellow
    Write-Host ''
    Write-Host '  可能的原因：' -ForegroundColor Yellow
    foreach ($line in (Get-BlockReasons $root)) { Write-Host "    $line" -ForegroundColor Yellow }
    Write-Host ''
    Die @(
      '更新沒有進行。把上面的原因處理掉（最快的辦法通常是把整個 anim 資料夾',
      '搬到 C:\anim），關掉 app 的黑視窗，然後再跑一次 update.bat。'
    )
  }
  Ok "$($plan.Count) 個檔案都可以寫"

  Say '複製程式碼（保留模型與設定）'
  $failed = @()
  foreach ($item in $plan) {
    if (-not (Copy-One $item.From $item.To)) { $failed += $item }
  }
  if ($failed.Count) {
    Write-Host ''
    foreach ($f in ($failed | Select-Object -First 5)) {
      Write-Host "    $($f.Rel)" -ForegroundColor Red
    }
    Die @(
      "有 $($failed.Count) 個檔案複製失敗，現在程式是「一半新一半舊」的狀態，先不要啟動。",
      '把檔案總管、編輯器、防毒的即時掃描先關掉，再跑一次 update.bat 就會補齊。'
    )
  }

  Say '驗證'
  $bad = @($plan | Where-Object {
    (-not (Test-Path -LiteralPath $_.To)) -or
    ((Get-Item -LiteralPath $_.To -Force).Length -ne $_.Size)
  })
  if ($bad.Count) {
    Die @(
      "複製完之後有 $($bad.Count) 個檔案對不上（例如 $($bad[0].Rel)）。",
      '再跑一次 update.bat。還是不行的話，把 anim 搬到 C:\anim 再試。'
    )
  }
  Ok "$($plan.Count) 個檔案全部就位，大小相符"

  foreach ($name in $keep) {
    if (Test-Path (Join-Path $root $name)) { Ok "$name 沒有被動到" }
  }

  Say '補裝可能新增的 Python 套件'
  # python.exe -m pip, not pip.exe: the .exe shim hard-codes the absolute path
  # of the interpreter it was built against, so it stops working the moment the
  # folder is moved - and moving the folder off the Desktop is the standard fix
  # for the permission problems this script exists to survive.
  $vpy = "$root\venv\Scripts\python.exe"
  if (Test-Path $vpy) {
    & $vpy -m pip install -r "$root\app\requirements.txt" --quiet
    if ($LASTEXITCODE -ne 0) {
      Warn '套件安裝回報錯誤。程式碼是新的，但如果啟動時說少套件，請跑一次 install.bat。'
    } else {
      Ok '套件已同步'
    }
  } else {
    Warn 'venv 不存在，跳過。之後跑 install.bat 會建立。'
  }

  # ComfyUI is a separate checkout and is on the never-overwrite list above -
  # every model lives inside it. So it is updated the only safe way: a
  # fast-forward git pull in place. Its own .gitignore covers models/,
  # custom_nodes/, output/, input/ and user/, so none of those can be touched.
  Say '更新 ComfyUI 本體'
  $comfy = "$root\ComfyUI"
  if (-not (Test-Path "$comfy\.git")) {
    Warn 'ComfyUI 不是 git 目錄，跳過（模型完全沒事）。'
  } else {
    $dirty = & git -C $comfy status --porcelain --untracked-files=no 2>&1
    if ($LASTEXITCODE -ne 0) {
      Warn "讀不到 ComfyUI 的狀態，跳過：$dirty"
    } elseif ("$dirty".Trim()) {
      Warn 'ComfyUI 資料夾裡有被改過的檔案，跳過更新（怕蓋掉你的修改）。'
    } else {
      $before = (& git -C $comfy rev-parse --short HEAD 2>$null)
      & git -C $comfy pull --ff-only 2>&1 | Out-Null
      if ($LASTEXITCODE -ne 0) {
        Warn 'ComfyUI 更新失敗（通常是網路）。app 本身已經更新好了，之後再試即可。'
      } else {
        $after = (& git -C $comfy rev-parse --short HEAD 2>$null)
        if ($before -eq $after) {
          Ok 'ComfyUI 已經是最新的'
        } else {
          Ok "ComfyUI 更新完成：$before -> $after"
          if (Test-Path $vpy) {
            & $vpy -m pip install -r "$comfy\requirements.txt" --quiet
            if ($LASTEXITCODE -ne 0) {
              Warn 'ComfyUI 的套件安裝回報錯誤。啟動時若說少套件，跑一次 install.bat。'
            } else { Ok 'ComfyUI 套件已同步' }
          }
        }
      }
    }
  }
} finally {
  Remove-Item -Path $tmp -Recurse -Force -ErrorAction SilentlyContinue
}

Say '完成'
Write-Host 'app 程式碼和 ComfyUI 本體都已更新。模型、成品、.env 都保留。' -ForegroundColor Green
if ($busy.Count) {
  Write-Host ''
  Write-Host '請把那兩個黑視窗關掉，再雙擊 start.bat —— 新程式要重啟才生效。' -ForegroundColor Yellow
} else {
  Write-Host '雙擊 start.bat 就可以用了。' -ForegroundColor Green
}

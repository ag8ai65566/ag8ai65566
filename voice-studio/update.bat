@echo off
chcp 65001 >nul
setlocal EnableExtensions
title Voice Studio 更新

rem This file can be replaced by the update while it runs (cmd reads .bat files line by line),
rem so the work is done by a copy of it in %TEMP%.
if /i not "%~1"=="--from-temp" (
  copy /y "%~f0" "%TEMP%\voice-studio-update.bat" >nul || (echo [!] 無法建立暫存檔。& pause & exit /b 1)
  "%TEMP%\voice-studio-update.bat" --from-temp "%~dp0"
)
set "DIR=%~2"
cd /d "%DIR%" || (echo [!] 找不到 Voice Studio 資料夾：%DIR% & pause & exit /b 1)
set "PATH=%USERPROFILE%\.local\bin;%PATH%"
set "URL=https://github.com/ag8ai65566/ag8ai65566/archive/refs/heads/claude/sudowrite-novel-framework-2cmja7.zip"
set "TMPZIP=%TEMP%\voice-studio-update.zip"
set "TMPDIR=%TEMP%\voice-studio-update"

echo.
echo  ================================================
echo   Voice Studio 更新（你的錄音、模型、設定不會動到）
echo  ================================================
echo.

:running
netstat -ano | findstr /r /c:":7860 .*LISTENING" >nul
if not errorlevel 1 (
  echo [!] Voice Studio 還開著。請先關掉它的黑色視窗，再按任意鍵繼續。
  pause >nul
  goto running
)

rem A git checkout updates with git; a ZIP install downloads the newest ZIP and copies the program files over.
where git >nul 2>nul
if not errorlevel 1 (
  git -C "%DIR%." rev-parse --is-inside-work-tree >nul 2>nul
  if not errorlevel 1 (
    echo  [1/2] 用 git 取得最新版...
    git -C "%DIR%." pull --ff-only || (echo [!] git 更新失敗：可能有你自己改過的檔案。& pause & exit /b 1)
    goto install
  )
)

echo  [1/3] 下載最新版（約 15 MB）...
if exist "%TMPZIP%" del /q "%TMPZIP%"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -UseBasicParsing -Uri '%URL%' -OutFile '%TMPZIP%'"
if not exist "%TMPZIP%" (echo [!] 下載失敗，請檢查網路後再執行一次。& pause & exit /b 1)

echo  [2/3] 解壓縮並更新程式檔案...
if exist "%TMPDIR%" rmdir /s /q "%TMPDIR%"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '%TMPZIP%' -DestinationPath '%TMPDIR%' -Force"
set "SRC="
for /d %%d in ("%TMPDIR%\*") do if exist "%%d\voice-studio\pyproject.toml" set "SRC=%%d\voice-studio"
if not defined SRC (echo [!] 下載的檔案不完整，請再執行一次。& pause & exit /b 1)
rem data (recordings, models, settings) and .venv (installed packages) are never touched
robocopy "%SRC%" "%DIR%." /E /XD data .venv node_modules __pycache__ /R:2 /W:2 /NFL /NDL /NJH /NJS /NP
if errorlevel 8 (echo [!] 複製檔案失敗：確認 Voice Studio 已關閉，再執行一次。& pause & exit /b 1)
rmdir /s /q "%TMPDIR%" 2>nul
del /q "%TMPZIP%" 2>nul

:install
echo  [最後] 更新套件...
where uv >nul 2>nul || (echo [!] 找不到 uv，請重新執行 install.bat。& pause & exit /b 1)
uv pip install --python .venv\Scripts\python.exe -e ".[prep]" || (echo [!] 套件更新失敗，請把上面的錯誤訊息複製下來詢問。& pause & exit /b 1)
echo.
echo  更新完成！雙擊桌面的「Voice Studio」重新開啟。
echo  已安裝的本機引擎不受影響；若「設定 → 引擎」顯示需要更新，再按一次安裝。
echo.
pause
exit /b 0

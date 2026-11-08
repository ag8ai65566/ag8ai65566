@echo off
chcp 65001 >nul
setlocal EnableExtensions
title 安裝 Claude 右側的 Voice Manager 面板

rem One-time setup: adds the plugin folder next to this file as a plugin source of Claude Code, and installs the
rem voice-manager plugin from it. The plugin is read from that folder, so update.bat keeps it up to date.
set "PATH=%USERPROFILE%\.local\bin;%APPDATA%\npm;%PATH%"
set "SRC=%~dp0claude-plugin"

echo.
echo  ================================================
echo   安裝 Claude 右側的 Voice Manager 面板（只要一次）
echo  ================================================
echo.
if not exist "%SRC%\.claude-plugin\marketplace.json" (echo [!] 找不到 %SRC%，請先執行 update.bat。& pause & exit /b 1)
where claude >nul 2>nul
if errorlevel 1 (
  echo [!] 找不到 claude 指令。這個面板要在你電腦上的 Claude Code 裡用：
  echo     先安裝 Claude Code（https://code.claude.com/docs），再執行一次這個檔案。
  pause
  exit /b 1
)

echo  [1/2] 加入外掛來源：%SRC%
claude plugin marketplace add "%SRC%" || goto fail
echo  [2/2] 安裝 voice-manager
claude plugin install voice-manager@voice-studio --scope user || goto fail
echo.
echo  完成。之後在你電腦上開 Claude（本機的工作階段），右側會有 Voice Manager 面板：
echo  按「開啟 Voice Manager」，第一次選要開啟的程式，之後按一下就開。
echo  已經開著的 Claude 輸入 /reload-plugins 就會出現。
echo.
pause
exit /b 0

:fail
echo.
echo [!] 安裝沒有完成，請把上面的訊息拍照傳給 Claude。
pause
exit /b 1

@echo off
REM WanGP: a separate open-source app (github.com/deepbeepmeep/Wan2GP). Its
REM Showrunner plans the shots from your picture, generates them, checks each
REM one, redoes the failed ones and cuts a video - all on this computer.
REM This installs it under WanGP\ next to this file, or starts or updates it.
REM Plain ASCII on purpose - see install.bat.
chcp 65001 >nul
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0wangp-windows.ps1" %*
echo.
pause

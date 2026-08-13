@echo off
REM Double-click me to start. See install.bat for why this file is plain ASCII.
REM Pass -Watch to also start the drop-folder watcher:  start.bat -Watch
chcp 65001 >nul
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start-windows.ps1" %*
echo.
echo  Two black windows should have opened - leave them running.
echo  The browser opens http://127.0.0.1:8000 automatically.
echo.
pause

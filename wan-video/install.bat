@echo off
REM Double-click me to install. Kept plain ASCII on purpose: .bat files are read
REM in the system ANSI codepage, so non-ASCII text here would break on some
REM Windows locales. The PowerShell script it launches does the talking.
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  Installing... this window will show progress. Do not close it.
echo  (Model download is tens of GB and can take hours.)
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup-windows.ps1" %*
echo.
echo  ============================================
echo   Done. Next time, double-click start.bat
echo  ============================================
echo.
pause

@echo off
REM Double-click me to update the program code to the latest version.
REM Models, venv, outputs and .env are left alone. See install.bat for why this
REM file is plain ASCII.
chcp 65001 >nul
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0update-windows.ps1" %*
echo.
pause

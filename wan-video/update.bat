@echo off
REM Double-click me to update the program code to the latest version.
REM Models, venv, outputs and .env are left alone. See install.bat for why this
REM file is plain ASCII.
chcp 65001 >nul
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0update-windows.ps1" %*
echo.
REM The script exits non-zero when the update did not complete. Say so here as
REM well: a failure message can scroll off, and a half-read screen has already
REM been mistaken for a successful update.
if errorlevel 1 (
  echo ============================================
  echo   UPDATE DID NOT COMPLETE - see the reason above.
  echo   Fix it, then run update.bat again.
  echo ============================================
) else (
  echo ============================================
  echo   UPDATE OK - close the black windows and run start.bat
  echo ============================================
)
echo.
pause

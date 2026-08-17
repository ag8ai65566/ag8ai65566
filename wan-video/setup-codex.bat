@echo off
REM Double-click wrapper. Keep this file pure ASCII with CRLF endings:
REM cmd.exe reads it in the system codepage and echoes a BOM as text.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup-codex.ps1" %*
echo.
pause

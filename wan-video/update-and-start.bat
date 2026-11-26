@echo off
REM One file you can keep anywhere - the Desktop, for instance. It finds the app
REM folder, updates the code to the latest version, and starts the app.
REM Inside the app folder it works as well: one double-click instead of
REM update.bat followed by start.bat.
REM Plain ASCII on purpose - see install.bat.
setlocal EnableExtensions DisableDelayedExpansion
chcp 65001 >nul
title Update and start
set "MEMO=%LOCALAPPDATA%\wan-video-launcher.txt"
set "APP="

REM 1. Next to this file.
if exist "%~dp0start-windows.ps1" set "APP=%~dp0"
REM 2. Where it was found last time.
if not defined APP if exist "%MEMO%" set /p APP=<"%MEMO%"
if defined APP if not exist "%APP%\start-windows.ps1" set "APP="
REM 3. The usual places.
for %%D in ("C:\anim\wan-video" "C:\anim" "%USERPROFILE%\Desktop\anim\wan-video" "%USERPROFILE%\Desktop\anim" "%USERPROFILE%\Desktop\wan-video" "%USERPROFILE%\Downloads\wan-video") do (
  if not defined APP if exist "%%~D\start-windows.ps1" set "APP=%%~D"
)

:ask
if defined APP goto found
echo.
echo  Could not find the app folder - the one that has start.bat in it.
echo  Drag that folder onto this window, then press Enter.
echo.
echo  Never installed it? Download and unzip
echo    https://github.com/ag8ai65566/ag8ai65566/archive/refs/heads/claude/local-image-to-animation-ai-375zyw.zip
echo  then open the wan-video folder inside and double-click install.bat.
echo.
echo  (Press Enter on an empty line to quit.)
set /p "APP=  Folder: "
if not defined APP goto end
set "APP=%APP:"=%"
if "%APP:~-1%"=="\" set "APP=%APP:~0,-1%"
if exist "%APP%\start-windows.ps1" goto found
echo.
echo  There is no start-windows.ps1 in that folder.
set "APP="
goto ask

:found
if "%APP:~-1%"=="\" set "APP=%APP:~0,-1%"
REM Remembered for next time, so this file can live on the Desktop.
>"%MEMO%" (set /p "=%APP%" <nul)
cd /d "%APP%"
echo.
echo  App folder: "%APP%"
echo.
echo    [1] Update, then start    - use this after new changes were pushed
echo    [2] Start only
echo    [3] Update only
echo    [4] WanGP - picture in, finished video out (install / start / update)
echo.
choice /C 1234 /N /M "  Press 1, 2, 3 or 4: "
if errorlevel 4 goto wangp
if errorlevel 3 goto update_only
if errorlevel 2 goto start_only
if errorlevel 1 goto update_start
goto end

:update_start
call :wait_closed
call :update
if errorlevel 1 goto failed
goto start_only

:update_only
call :wait_closed
call :update
if errorlevel 1 goto failed
echo.
echo  ============================================
echo    UPDATE OK
echo  ============================================
goto end

:start_only
powershell -NoProfile -ExecutionPolicy Bypass -File "%APP%\start-windows.ps1"
echo.
echo  Two black windows should have opened - leave them running.
echo  The browser opens http://127.0.0.1:8000 automatically.
goto end

:wangp
if not exist "%APP%\wangp-windows.ps1" (
  echo.
  echo  This app folder is older than the WanGP launcher.
  echo  Press 3 first to update it, then run this again and press 4.
  goto end
)
powershell -NoProfile -ExecutionPolicy Bypass -File "%APP%\wangp-windows.ps1"
goto end

:failed
echo.
echo  ============================================
echo    UPDATE DID NOT COMPLETE - see the reason above.
echo    The app was not started. Fix it, then run this again.
echo  ============================================
goto end

REM New code is only loaded when the app starts, and start-windows.ps1 reuses
REM an app that is already running. So an update waits for the old one to go.
REM Only the app's own port is checked: a ComfyUI the user runs separately on
REM 8188 is theirs to keep open.
:wait_closed
powershell -NoProfile -Command "if (Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue) { exit 1 }"
if not errorlevel 1 exit /b 0
echo.
echo  The app is running. An update only takes effect after a restart:
echo  close the two black windows, then press any key here.
pause >nul
goto wait_closed

:update
powershell -NoProfile -ExecutionPolicy Bypass -File "%APP%\update-windows.ps1"
exit /b %errorlevel%

:end
echo.
pause

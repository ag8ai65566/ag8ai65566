@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Voice Studio
if not exist .venv\Scripts\python.exe (
  echo 還沒安裝，先執行 install.bat。
  pause
  exit /b 1
)
echo Voice Studio 啟動中... 瀏覽器會自動打開 http://127.0.0.1:7860
echo 要關閉時，直接關掉這個視窗。（雲端訓練會繼續，下次開啟時自動接上。）
.venv\Scripts\python.exe -m vstudio.server
if errorlevel 1 pause

@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Voice Studio 更新
where git >nul 2>nul
if errorlevel 1 (
  echo 找不到 git。請重新下載最新版的 voice-studio 資料夾覆蓋（data 資料夾會保留）。
  pause
  exit /b 1
)
git pull --ff-only || (echo [!] 更新失敗：你可能修改過檔案。& pause & exit /b 1)
uv pip install --python .venv\Scripts\python.exe -e ".[prep]"
echo 更新完成。已安裝的引擎不受影響；若「設定 → 引擎」顯示需要更新，再按一次安裝。
pause

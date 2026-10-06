@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Voice Studio 安裝
echo.
echo  ================================================
echo   Voice Studio 安裝（第一次約 10-20 分鐘）
echo  ================================================
echo.

where nvidia-smi >nul 2>nul
if errorlevel 1 (
  echo [!] 找不到 NVIDIA 顯示卡驅動程式（nvidia-smi）。
  echo     請先到 https://www.nvidia.com/drivers 安裝最新的 Game Ready 或 Studio 驅動，再重新執行。
  echo     沒有 NVIDIA 顯示卡也可以繼續，只是語音辨識和合成會很慢。
  echo.
  choice /m "要繼續安裝嗎"
  if errorlevel 2 exit /b 1
) else (
  for /f "tokens=*" %%g in ('nvidia-smi --query-gpu^=name^,memory.total --format^=csv^,noheader') do echo  顯示卡：%%g
)

where uv >nul 2>nul
if errorlevel 1 (
  echo  [1/5] 安裝 uv（Python 管理工具）...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
  set "PATH=%USERPROFILE%\.local\bin;%PATH%"
)
where uv >nul 2>nul || (echo [!] uv 安裝失敗，請檢查網路後重試。 & pause & exit /b 1)

echo  [2/5] 準備 Python 3.11 ...
uv python install 3.11 || goto :fail
if not exist .venv uv venv --python 3.11 .venv || goto :fail

echo  [3/5] 安裝 GPU 版 PyTorch（約 3 GB）...
uv pip install --python .venv\Scripts\python.exe torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu128 || goto :fail

echo  [4/5] 安裝 Voice Studio 與語音辨識...
uv pip install --python .venv\Scripts\python.exe -e ".[prep]" || goto :fail

echo  [5/5] 檢查...
.venv\Scripts\python.exe -c "import torch; print('  PyTorch', torch.__version__, '| CUDA', torch.cuda.is_available(), '|', torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')" || goto :fail

if not exist "%USERPROFILE%\Desktop\Voice Studio.lnk" (
  powershell -NoProfile -Command "$s=(New-Object -ComObject WScript.Shell).CreateShortcut([Environment]::GetFolderPath('Desktop')+'\Voice Studio.lnk');$s.TargetPath='%~dp0start.bat';$s.WorkingDirectory='%~dp0';$s.Save()" >nul 2>nul
)
echo.
echo  安裝完成！桌面上有「Voice Studio」捷徑，或直接執行 start.bat。
echo  要在本機合成語音，請在 Voice Studio 的「設定 → 引擎」按「安裝」。
echo.
pause
exit /b 0

:fail
echo.
echo [!] 安裝失敗。請把上面的錯誤訊息複製下來詢問（不含任何金鑰）。
pause
exit /b 1

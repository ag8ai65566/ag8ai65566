#!/usr/bin/env bash
# 一鍵安裝（Linux，不用 Docker）。Docker 版看 README 的 docker compose 段。
#
#   ./setup-linux.sh              # fp8，24GB+ 顯存
#   ./setup-linux.sh gguf Q4_K_M  # 顯存較小
set -euo pipefail

PROFILE="${1:-fp8}"
QUANT="${2:-Q4_K_M}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

say() { printf '\n\033[36m== %s ==\033[0m\n' "$1"; }
ok() { printf '  \033[32m✓\033[0m %s\n' "$1"; }
die() { printf '\n\033[31m失敗：%s\033[0m\n' "$1" >&2; exit 1; }

say "檢查環境"
command -v nvidia-smi >/dev/null || die "找不到 nvidia-smi，需要 NVIDIA 顯卡與驅動"
GPU="$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1)"
VRAM="$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits | head -1)"
ok "顯卡：$GPU（$((VRAM / 1024))GB）"

if [[ "$VRAM" -lt 20000 && "$PROFILE" == "fp8" ]]; then
  echo "  !! 顯存 $((VRAM / 1024))GB 用 fp8 會爆，改用 GGUF $QUANT"
  PROFILE=gguf
fi

command -v git >/dev/null || die "需要 git"
PYTHON="${PYTHON:-python3}"
command -v "$PYTHON" >/dev/null || die "需要 python3"
PYVER="$($PYTHON -c 'import sys;print("%d.%d" % sys.version_info[:2])')"
ok "Python $PYVER"

CUDA=cu126
[[ "$GPU" =~ RTX\ *50[0-9][0-9] ]] && CUDA=cu128
ok "PyTorch 版本：$CUDA"

say "建立虛擬環境"
[[ -d venv ]] || "$PYTHON" -m venv venv
PIP="$ROOT/venv/bin/pip"
VPY="$ROOT/venv/bin/python"
"$PIP" install --upgrade pip --quiet
ok "venv 就緒"

say "安裝 PyTorch（$CUDA，約 2~3GB）"
"$PIP" install torch torchvision torchaudio --index-url "https://download.pytorch.org/whl/$CUDA"
[[ "$("$VPY" -c 'import torch;print(torch.cuda.is_available())')" == "True" ]] \
  || die "PyTorch 看不到顯卡，請檢查驅動"
ok "PyTorch 認得顯卡"

say "安裝 ComfyUI"
[[ -d ComfyUI ]] || git clone https://github.com/comfyanonymous/ComfyUI.git ComfyUI
"$PIP" install -r ComfyUI/requirements.txt --quiet
ok "ComfyUI 就緒"

say "安裝擴充節點"
install_node() {
  local name="$1" url="$2" dest="ComfyUI/custom_nodes/$1"
  [[ -d "$dest" ]] || git clone --quiet "$url" "$dest"
  [[ -f "$dest/requirements.txt" ]] && "$PIP" install -r "$dest/requirements.txt" --quiet
  ok "$name"
}
install_node ComfyUI-GGUF https://github.com/city96/ComfyUI-GGUF.git
install_node ComfyUI-VideoHelperSuite https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git
install_node ComfyUI-Manager https://github.com/ltdrdata/ComfyUI-Manager.git

say "安裝 app"
"$PIP" install -r app/requirements.txt --quiet
ok "app 就緒"

say "下載模型"
# 讓下載腳本把檔案放進 ComfyUI 自己的 models 目錄
if [[ ! -e models ]]; then ln -s ComfyUI/models models; fi
./scripts/download-models.sh "$PROFILE" "$QUANT"

if [[ ! -f .env ]]; then
  COMFY_ARGS=""
  [[ "$VRAM" -lt 12000 ]] && COMFY_ARGS="--lowvram"
  cat > .env <<EOF
PROFILE=$PROFILE
GGUF_QUANT=$QUANT
LIGHTNING=true
TIER=480p
LENGTH=81
FPS=16
LORAS=
COMFY_ARGS=$COMFY_ARGS
EOF
  ok ".env 已建立"
fi
mkdir -p data/outputs data/inbox

cat > start-linux.sh <<'EOF'
#!/usr/bin/env bash
# 啟動 ComfyUI + app。Ctrl-C 一起關掉。
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
set -a; [[ -f .env ]] && . ./.env; set +a
export COMFY_URL=http://127.0.0.1:8188
export OUTPUT_DIR="$ROOT/data/outputs" INBOX_DIR="$ROOT/data/inbox" DONE_DIR="$ROOT/data/inbox/done"
export APP_URL=http://127.0.0.1:8000
mkdir -p "$OUTPUT_DIR" "$INBOX_DIR"

trap 'kill 0' EXIT INT TERM
(cd ComfyUI && "$ROOT/venv/bin/python" main.py --listen 127.0.0.1 --port 8188 ${COMFY_ARGS:-}) &
(cd app && "$ROOT/venv/bin/python" -m uvicorn server:app --host 127.0.0.1 --port 8000) &
[[ "${1:-}" == "--watch" ]] && (cd app && "$ROOT/venv/bin/python" watcher.py) &

echo
echo "app:    http://127.0.0.1:8000"
echo "ComfyUI: http://127.0.0.1:8188"
wait
EOF
chmod +x start-linux.sh

say "完成"
echo "以後每次執行： ./start-linux.sh    （拖檔模式： ./start-linux.sh --watch）"

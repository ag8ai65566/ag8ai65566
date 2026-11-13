#!/usr/bin/env bash
# Boot script for the rented GPU machine. The app at home starts the machine
# with one command - "download this file and run it" - and everything the
# machine needs is installed from here.
#
# Order matters, and the first thing is not ComfyUI:
#
#   1. Start the agent. It takes one second and answers "how is boot going?"
#      for the rest of this script. On a machine that bills by the second, a
#      boot nobody can see into is the failure this file is built to avoid -
#      every step below writes one line to a log the agent serves.
#   2. Install ComfyUI at the exact release the app's workflows were checked
#      against. Not "latest": a newer ComfyUI can rename a node between two
#      boots, and then the same shot works on Monday and not on Tuesday.
#   3. Start ComfyUI, and keep restarting it if it dies.
#
# Everything lives under /workspace, which survives stopping the machine. A
# second boot finds the install already there and is up in well under a minute.
#
# Nothing here prints a secret. The only one this script ever holds is the
# agent's token, and it is passed through the environment, never echoed.

set -uo pipefail

ROOT="${WAN_ROOT:-/workspace/wan}"
RAW="${WAN_REPO_RAW:-}"
REF="${WAN_COMFY_REF:-v0.45.0}"
PORT="${WAN_COMFY_PORT:-8188}"
# ComfyUI itself listens here, on this machine only. PORT is the gate in front
# of it (cloud/gate.py): ComfyUI has no login, and a Runpod address is public.
INNER="${WAN_COMFY_INNER_PORT:-8187}"
AGENT_PORT="${WAN_AGENT_PORT:-8189}"
EXTRA_ARGS="${WAN_COMFY_ARGS:-}"
COMFY_REPO="${WAN_COMFY_REPO:-https://github.com/comfyanonymous/ComfyUI.git}"

mkdir -p "$ROOT"
LOG="$ROOT/boot.log"
: > "$LOG"

say() { printf '[%s] %s\n' "$(date -u +%H:%M:%S)" "$*" | tee -a "$LOG"; }
phase() { printf '%s\n' "$1" > "$ROOT/phase"; say "== $1"; }

# A failed boot keeps the machine up on purpose. The agent is still answering,
# so the app can show this log; a script that exited would take the container
# down with it and leave nothing to read.
fail() {
  phase "failed: $1"
  say "開機失敗：$1"
  while true; do sleep 3600; done
}

PY="$(command -v python3.12 || command -v python3 || command -v python || true)"
[ -n "$PY" ] || fail "這個映像檔裡沒有 Python"
[ -n "$RAW" ] || fail "沒有收到 WAN_REPO_RAW（不知道去哪裡抓 agent）"
[ -n "${WAN_AGENT_TOKEN:-}" ] || fail "沒有收到 WAN_AGENT_TOKEN"

# -- 1. the agent -----------------------------------------------------------
phase "booting"
for f in agent.py gate.py; do
  curl -fsSL --retry 3 "$RAW/cloud/$f" -o "$ROOT/$f.new" || fail "抓不到 $f（$RAW）"
  mv "$ROOT/$f.new" "$ROOT/$f"
done
pkill -f "$ROOT/agent.py" 2>/dev/null || true
# The agent asks ComfyUI "are you busy?" before its dead-man switch stops the
# machine, and it asks on the inside port - the gate would turn it away.
WAN_COMFY_PORT="$INNER" nohup "$PY" "$ROOT/agent.py" --root "$ROOT" --port "$AGENT_PORT" \
  >> "$ROOT/agent.log" 2>&1 &
say "agent 已啟動（:$AGENT_PORT）"

# -- 2. ComfyUI at a pinned release ----------------------------------------
phase "installing: ComfyUI $REF"
COMFY="$ROOT/ComfyUI"
if [ ! -d "$COMFY/.git" ]; then
  rm -rf "$COMFY.tmp"
  git -c advice.detachedHead=false clone --quiet --depth 1 --branch "$REF" "$COMFY_REPO" "$COMFY.tmp" 2>>"$LOG" \
    || fail "git clone ComfyUI $REF 失敗"
  # Models may already be here from an earlier, broken install - keep them.
  if [ -d "$COMFY/models" ]; then
    rm -rf "$COMFY.tmp/models"
    mv "$COMFY/models" "$COMFY.tmp/models"
  fi
  rm -rf "$COMFY"
  mv "$COMFY.tmp" "$COMFY"
  say "ComfyUI 已下載"
else
  have="$(git -C "$COMFY" describe --tags --exact-match 2>/dev/null || git -C "$COMFY" rev-parse --abbrev-ref HEAD)"
  if [ "$have" != "$REF" ]; then
    say "ComfyUI 從 $have 換到 $REF"
    git -C "$COMFY" fetch --quiet --depth 1 origin "$REF" 2>>"$LOG" \
      && git -C "$COMFY" -c advice.detachedHead=false checkout --quiet -f FETCH_HEAD 2>>"$LOG" \
      && git -C "$COMFY" tag -f "$REF" >/dev/null 2>&1 \
      || fail "切換 ComfyUI 到 $REF 失敗"
  else
    say "ComfyUI 已經是 $REF"
  fi
fi

# -- 3. Python environment ---------------------------------------------------
VENV="$ROOT/venv"
if [ ! -x "$VENV/bin/python" ]; then
  phase "installing: Python 環境"
  # --system-site-packages: the image already carries a CUDA build of torch,
  # several gigabytes that there is no reason to download a second time.
  "$PY" -m venv --system-site-packages "$VENV" 2>>"$LOG" || fail "建立 venv 失敗"
fi
VPY="$VENV/bin/python"

if ! "$VPY" -c "import torch" 2>/dev/null; then
  phase "installing: PyTorch（映像檔裡沒有，要下載幾 GB）"
  "$VPY" -m pip install --quiet torch torchvision torchaudio 2>>"$LOG" \
    || fail "安裝 PyTorch 失敗"
fi

if [ -z "${WAN_CPU:-}" ]; then
  if ! "$VPY" -c "import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>>"$LOG"; then
    fail "PyTorch 看不到顯卡（CUDA 不可用）。換一種 GPU 或映像檔再試。"
  fi
  say "顯卡：$("$VPY" -c "import torch; print(torch.cuda.get_device_name(0), round(torch.cuda.get_device_properties(0).total_memory/2**30), 'GB')" 2>/dev/null)"
fi

# Reinstall requirements only when the file changed, so a normal restart does
# not spend a minute re-resolving packages that are already there.
need_install() {
  local file="$1" mark
  mark="$ROOT/.req.$(sha256sum "$file" | cut -c1-16)"
  [ -f "$mark" ] && return 1
  echo "$mark"
}

if mark="$(need_install "$COMFY/requirements.txt")"; then
  phase "installing: ComfyUI 的套件"
  "$VPY" -m pip install --quiet -r "$COMFY/requirements.txt" 2>>"$LOG" \
    || fail "安裝 ComfyUI 的套件失敗（看上面的 pip 訊息）"
  touch "$mark"
fi

# -- 4. the node packs this app's workflows can use ---------------------------
# Neither is fatal. A pack that fails to install costs the workflows that need
# it, and the app says which node is missing when one of those is submitted.
node_pack() {
  local name="$1" url="$2" dest="$COMFY/custom_nodes/$1" mark
  if [ ! -d "$dest/.git" ]; then
    git clone --quiet --depth 1 "$url" "$dest" 2>>"$LOG" || { say "（略過）$name 下載失敗"; return; }
  fi
  if [ -f "$dest/requirements.txt" ] && mark="$(need_install "$dest/requirements.txt")"; then
    "$VPY" -m pip install --quiet -r "$dest/requirements.txt" 2>>"$LOG" \
      && touch "$mark" || say "（略過）$name 的套件裝不起來"
  fi
}
phase "installing: 節點套件"
node_pack ComfyUI-GGUF https://github.com/city96/ComfyUI-GGUF.git
node_pack ComfyUI-VideoHelperSuite https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git
# IP-Adapter: a reference picture as a one-off LoRA (style, composition or
# both) for SDXL checkpoints. Maintenance-only upstream since 2025-04, so it is
# not pinned to a newer feature than the app uses.
node_pack ComfyUI_IPAdapter_plus https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

# -- 5. run ------------------------------------------------------------------
phase "starting"
(
  until curl -fs -m 5 "http://127.0.0.1:$INNER/system_stats" >/dev/null 2>&1; do sleep 2; done
  until curl -s -m 5 -o /dev/null -w '%{http_code}' "http://127.0.0.1:$PORT/system_stats" 2>/dev/null | grep -q 401; do sleep 1; done
  phase "ready"
) &

# The gate, restarted if it ever dies. Without it nothing outside can reach
# ComfyUI at all, which is the safe way to fail.
pkill -f "$ROOT/gate.py" 2>/dev/null || true
(
  while true; do
    "$VPY" "$ROOT/gate.py" --port "$PORT" --upstream "127.0.0.1:$INNER" >> "$ROOT/gate.log" 2>&1
    say "gate 結束了（代碼 $?），3 秒後重新啟動"
    sleep 3
  done
) &

cd "$COMFY" || fail "找不到 ComfyUI 資料夾"
CPU_FLAG=""
[ -n "${WAN_CPU:-}" ] && CPU_FLAG="--cpu"
while true; do
  # Keep the last couple of megabytes; the agent only ever serves the tail.
  if [ -f "$ROOT/comfy.log" ]; then
    tail -c 2000000 "$ROOT/comfy.log" > "$ROOT/comfy.log.tmp" 2>/dev/null && mv "$ROOT/comfy.log.tmp" "$ROOT/comfy.log"
  fi
  # shellcheck disable=SC2086 - EXTRA_ARGS is a list of flags, split on purpose
  "$VPY" main.py --listen 127.0.0.1 --port "$INNER" $CPU_FLAG $EXTRA_ARGS >> "$ROOT/comfy.log" 2>&1
  say "ComfyUI 結束了（代碼 $?），5 秒後重新啟動"
  [ -n "${WAN_ONCE:-}" ] && exit 0
  sleep 5
done

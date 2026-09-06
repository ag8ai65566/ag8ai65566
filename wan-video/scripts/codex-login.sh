#!/usr/bin/env bash
# Log this container's Codex CLI in, without any credential passing through chat.
#
# Claude Code on the web runs in a throwaway container: there is no browser in
# it, and nothing you can reach on its localhost - so the ordinary `codex login`
# (which listens on 127.0.0.1:1455 for the OAuth callback) cannot finish here.
#
# `--device-auth` is the flow for exactly this shape of machine. It prints a URL
# and a one-time code; you open the URL on your own computer, type the code, and
# the token comes back to the container directly from OpenAI. The credential
# never appears in the conversation, which is the same rule this project applies
# to the CivitAI and Hugging Face keys.
#
#   bash scripts/codex-login.sh
#
# The container is reclaimed after a while, and the token goes with it - so this
# has to be run again in a new session. See docs/codex-mcp.md for the two ways
# to avoid retyping it.
set -u

if ! command -v codex >/dev/null 2>&1; then
  echo "找不到 codex CLI。先裝：npm i -g @openai/codex" >&2
  exit 1
fi

if [ -f "${CODEX_HOME:-$HOME/.codex}/auth.json" ]; then
  echo "已經登入了（${CODEX_HOME:-$HOME/.codex}/auth.json 存在）。"
  codex login status 2>&1 | sed 's/^/  /'
  echo
  echo "要換帳號就先刪掉那個檔案再跑一次。"
  exit 0
fi

# An API key set in the environment is the other supported path, and it needs no
# browser at all. Read from the environment through a pipe, never from an
# argument: arguments show up in `ps` and in shell history.
if [ -n "${OPENAI_API_KEY:-}" ]; then
  echo "偵測到 OPENAI_API_KEY，直接用它登入（不會印出來，也不經過參數）。"
  printenv OPENAI_API_KEY | codex login --with-api-key
  codex login status
  exit $?
fi

echo "用裝置碼登入（沒有 API key、不需要瀏覽器在這台機器上）。"
echo "下面會給你一個網址和一組碼，在你自己的電腦上開啟並輸入。"
echo
exec codex login --device-auth

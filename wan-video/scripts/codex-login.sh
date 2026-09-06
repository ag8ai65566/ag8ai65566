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

# The gotcha that costs the most time, so the script says it rather than leaving
# it to be rediscovered: `codex mcp-server` reads the credentials once, at
# startup, and holds them. Logging in afterwards does not reach a process that
# is already running - it keeps answering 401 while `claude mcp list` cheerfully
# reports "Connected", because Connected only means the process is alive.
restart_note() {
  pids=$(pgrep -f 'codex mcp-server' 2>/dev/null | tr '\n' ' ')
  echo
  echo "登入完成。還有最後一步："
  if [ -n "$pids" ]; then
    echo "  codex 的 MCP server 已經在跑了（PID: $pids），而它是**在啟動時**"
    echo "  把憑證讀進記憶體的 —— 現在才登入，那個 process 不知道。"
    echo "  要讓它重讀，把它砍掉，下次呼叫時會用新憑證重開："
    echo
    echo "      kill $pids"
    echo
    echo "  不砍的話會一直回 401，而 'claude mcp list' 還是顯示 Connected"
    echo "  —— Connected 只代表 process 活著，不代表登入了。"
  else
    echo "  目前沒有 codex mcp-server 在跑，下次呼叫會用新憑證重開，不用做事。"
  fi
}

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
  printenv OPENAI_API_KEY | codex login --with-api-key || exit $?
  codex login status
  restart_note
  exit 0
fi

echo "用裝置碼登入（沒有 API key、不需要瀏覽器在這台機器上）。"
echo "下面會給你一個網址和一組碼，在你自己的電腦上開啟並輸入。"
echo
codex login --device-auth || exit $?
restart_note

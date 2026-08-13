#!/usr/bin/env bash
# Thin wrapper kept for compatibility. The catalogue now lives in app/registry.py
# and is shared with the web UI, so this just forwards to fetch-model.py.
#
#   ./scripts/download-models.sh --list
#   ./scripts/download-models.sh wan22-14b-fp8
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Old call style was `download-models.sh fp8|gguf [QUANT]`; map it to model ids
# so anyone following the previous README still lands somewhere sensible.
case "${1:-}" in
  fp8) set -- wan22-14b-fp8 ;;
  gguf)
    case "${2:-Q4_K_M}" in
      Q8_0) set -- wan22-14b-q8 ;;
      *) set -- wan22-14b-q4 ;;
    esac
    ;;
esac

exec python3 "$ROOT/scripts/fetch-model.py" "$@"

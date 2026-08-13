#!/usr/bin/env bash
# Download the Wan 2.2 I2V model files into ./models.
#
#   ./scripts/download-models.sh fp8            # 24GB+ VRAM (recommended)
#   ./scripts/download-models.sh gguf Q4_K_M    # 8-16GB VRAM
#   ./scripts/download-models.sh gguf Q8_0      # 16-24GB VRAM, closer to fp8
#
# Resumable: re-run it after an interruption and it picks up where it stopped.
set -euo pipefail

PROFILE="${1:-fp8}"
QUANT="${2:-Q4_K_M}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODELS="$ROOT/models"

REPACK="Comfy-Org/Wan_2.2_ComfyUI_Repackaged"
GGUF_REPO="QuantStack/Wan2.2-I2V-A14B-GGUF"

mkdir -p "$MODELS"/{diffusion_models,unet,text_encoders,vae,loras}

have() { command -v "$1" >/dev/null 2>&1; }
if ! have curl; then
  echo "需要 curl，請先安裝" >&2
  exit 1
fi

# fetch <repo> <path-in-repo> <destination-file>
fetch() {
  local repo="$1" path="$2" dest="$3"
  local url="https://huggingface.co/${repo}/resolve/main/${path}"
  local name; name="$(basename "$dest")"

  if [[ -f "$dest" ]]; then
    local remote local_size
    remote="$(curl -sIL "$url" | awk 'BEGIN{IGNORECASE=1} /^x-linked-size:|^content-length:/ {v=$2} END{gsub(/\r/,"",v); print v}')"
    local_size="$(stat -c%s "$dest" 2>/dev/null || stat -f%z "$dest" 2>/dev/null || echo 0)"
    if [[ -n "$remote" && "$remote" == "$local_size" ]]; then
      echo "  ✓ $name（已完成）"
      return 0
    fi
    echo "  ↻ $name（續傳）"
  else
    echo "  ↓ $name"
  fi

  local attempt
  for attempt in 1 2 3 4; do
    if curl -fL --retry 5 --retry-delay 2 --retry-all-errors \
         -C - -o "$dest" "$url"; then
      return 0
    fi
    # A completed file makes curl exit 33/416 on the range request; accept that.
    if [[ -s "$dest" ]] && curl -fsI "$url" >/dev/null; then
      local remote local_size
      remote="$(curl -sIL "$url" | awk 'BEGIN{IGNORECASE=1} /^x-linked-size:|^content-length:/ {v=$2} END{gsub(/\r/,"",v); print v}')"
      local_size="$(stat -c%s "$dest" 2>/dev/null || stat -f%z "$dest" 2>/dev/null || echo 0)"
      [[ -n "$remote" && "$remote" == "$local_size" ]] && return 0
    fi
    echo "     重試 $attempt/4 …" >&2
    sleep $((attempt * 3))
  done
  echo "下載失敗：$path" >&2
  return 1
}

echo "== 共用元件（文字編碼器 / VAE / 加速 LoRA）=="
fetch "$REPACK" "split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors" \
      "$MODELS/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors"
fetch "$REPACK" "split_files/vae/wan_2.1_vae.safetensors" \
      "$MODELS/vae/wan_2.1_vae.safetensors"
fetch "$REPACK" "split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors" \
      "$MODELS/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors"
fetch "$REPACK" "split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors" \
      "$MODELS/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"

case "$PROFILE" in
  fp8)
    echo "== 主模型 fp8（2 × 14.3GB）=="
    fetch "$REPACK" "split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors" \
          "$MODELS/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors"
    fetch "$REPACK" "split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors" \
          "$MODELS/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors"
    echo
    echo "完成。請在 .env 設 PROFILE=fp8"
    ;;
  gguf)
    echo "== 主模型 GGUF $QUANT（2 個檔）=="
    fetch "$GGUF_REPO" "HighNoise/Wan2.2-I2V-A14B-HighNoise-${QUANT}.gguf" \
          "$MODELS/unet/Wan2.2-I2V-A14B-HighNoise-${QUANT}.gguf"
    fetch "$GGUF_REPO" "LowNoise/Wan2.2-I2V-A14B-LowNoise-${QUANT}.gguf" \
          "$MODELS/unet/Wan2.2-I2V-A14B-LowNoise-${QUANT}.gguf"
    echo
    echo "完成。請在 .env 設 PROFILE=gguf 與 GGUF_QUANT=$QUANT"
    ;;
  *)
    echo "不認識的 profile：$PROFILE（可用 fp8 或 gguf）" >&2
    exit 1
    ;;
esac

echo "模型目錄用量：$(du -sh "$MODELS" | cut -f1)"

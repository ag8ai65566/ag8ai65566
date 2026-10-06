#!/bin/bash
# Voice Studio cloud training bootstrap. Runs as the pod's start command on RunPod.
# Everything lives on the network volume under /workspace/vs, so the engine environment is installed only once
# and the outputs survive the pod. The pod removes itself when it finishes, fails, or hits the time limit.
set -uo pipefail
JOB="/workspace/vs/jobs/${VS_TRAINING_ID}"
export HF_HOME=/workspace/vs/hf PYTHONUNBUFFERED=1 VS_SRC="/workspace/vs/src/${VS_ENGINE}" VS_WORK=/root/vswork
mkdir -p "$JOB"
exec > >(tee -a "$JOB/train.log") 2>&1
echo "[vs] start $(date -u +%FT%TZ) pod=${RUNPOD_POD_ID:-?} gpu=$(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null) disk=$(df -h /root | tail -1 | awk '{print $4}') free"

finish() {
  echo "[vs] removing pod ${RUNPOD_POD_ID:-?} ($1)"
  sync
  runpodctl remove pod "${RUNPOD_POD_ID}" >/dev/null 2>&1 || runpodctl stop pod "${RUNPOD_POD_ID}" >/dev/null 2>&1
  sleep 60
  exit 0
}
fail() {
  printf '{"status":"error","stage":"%s","at":"%s"}\n' "$1" "$(date -u +%FT%TZ)" > "$JOB/error.json"
  finish "error in $1"
}

# hard time limit, independent of the training process
( sleep "${VS_MAX_SECONDS:-43200}"; printf '{"status":"timeout"}\n' > "$JOB/error.json"; finish timeout ) &

echo '{"phase":"setup"}' > "$JOB/progress.json"
bash "$JOB/setup_env.sh" || fail setup

echo '{"phase":"unpack"}' > "$JOB/progress.json"
mkdir -p /root/vsdata && tar -xf "$JOB/dataset.tar" -C /root/vsdata || fail unpack

source /workspace/vs/envs/"${VS_ENGINE}"/bin/activate 2>/dev/null || true
python "$JOB/train_entry.py" --config "$JOB/config.json" --data /root/vsdata || fail train

[ -f "$JOB/model.tar" ] || fail package
printf '{"status":"done","at":"%s"}\n' "$(date -u +%FT%TZ)" > "$JOB/done.json"
finish done

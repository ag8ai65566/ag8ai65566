#!/bin/bash
# Voice Studio cloud training bootstrap. Runs as the pod's start command on RunPod.
# Everything lives on the network volume under /workspace/vs, so the engine environment is installed only once
# and the outputs survive the pod. The pod removes itself when it finishes, fails, is signalled or hits the time
# limit; removal is retried until RunPod confirms it. The studio and its orphan check remove it too.
set -uo pipefail
set -m   # background jobs get their own process group, so the watchdog can stop all of the work at once
VS_ROOT="${VS_ROOT:-/workspace/vs}"   # the network volume (overridable only for local tests)
JOB="$VS_ROOT/jobs/${VS_TRAINING_ID}"
export VS_ROOT HF_HOME="$VS_ROOT/hf" PYTHONUNBUFFERED=1 VS_SRC="$VS_ROOT/src/${VS_ENGINE}" VS_WORK="${VS_WORK:-/root/vswork}"
# model.tar / samples.tar go on the volume in parts of this size, with a manifest (<name>.json): RunPod's S3 API
# checksums a file written here the first time it is read; a 28.6 GB one could not be read at all (524)
export VS_PART_MB="${VS_PART_MB:-64}"
mkdir -p "$JOB"
exec > >(tee -a "$JOB/train.log") 2>&1
echo "[vs] start $(date -u +%FT%TZ) pod=${RUNPOD_POD_ID:-?} gpu=$(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null) disk=$(df -h /root | tail -1 | awk '{print $4}') free"

VS_DATA="${VS_DATA:-/root/vsdata}"
STAGE_FILE="${VS_WORK}.stage"
put() { printf '%s\n' "$2" > "$JOB/$1.tmp" && mv -f "$JOB/$1.tmp" "$JOB/$1"; }   # atomic: never read half-written
WORK_PID=""
FINISHING=0

finish() {
  [ "$FINISHING" = 1 ] && return
  FINISHING=1
  echo "[vs] finishing: $1"
  [ -n "${WATCH_PID:-}" ] && kill "$WATCH_PID" 2>/dev/null   # the time limit has done its job or is not needed
  if [ -n "$WORK_PID" ]; then
    kill -TERM -- "-$WORK_PID" 2>/dev/null; sleep "${VS_KILL_GRACE:-5}"; kill -KILL -- "-$WORK_PID" 2>/dev/null
  fi
  timeout 30s sync || true
  local n=0
  until timeout 30s runpodctl remove pod "${RUNPOD_POD_ID:?}"; do
    n=$((n + 1))
    echo "[vs] pod removal failed (attempt $n); retrying"
    # whether RunPod gave this pod its own key at all (never the key itself); Voice Studio removes the pod anyway
    # when it sees the run end, and its reaper does when it is next opened
    [ "$n" = 1 ] && echo "[vs] RUNPOD_API_KEY $([ -n "${RUNPOD_API_KEY:-}" ] && echo "present (${#RUNPOD_API_KEY} chars)" || echo missing); runpodctl $(runpodctl version 2>/dev/null | head -1)"
    # after ~10 minutes of failed deletes, stop the pod: that ends GPU billing, but also this loop, so from then on
    # the studio's reaper (every 5 minutes while it is open) deletes the stopped pod
    [ "$n" = 10 ] && timeout 30s runpodctl stop pod "${RUNPOD_POD_ID}"
    sleep $(( n < 6 ? ${VS_RETRY_SLEEP:-10} : ${VS_RETRY_SLEEP_LONG:-60} ))
  done
  sleep "${VS_FINISH_SLEEP:-300}"   # the pod is being deleted; never fall through to restarting work
  exit 0
}
fail() {
  put error.json "$(printf '{"status":"error","stage":"%s","at":"%s"}' "$1" "$(date -u +%FT%TZ)")"
  finish "error in $1"
}
on_timeout() {
  [ "$FINISHING" = 1 ] && return   # already cleaning up after a normal end
  put error.json "$(printf '{"status":"timeout","stage":"%s","at":"%s"}' "$(cat "$STAGE_FILE" 2>/dev/null)" "$(date -u +%FT%TZ)")"
  finish timeout
}
trap on_timeout USR1
trap 'finish signal' TERM INT HUP
trap 'finish exit' EXIT

# The studio rents this pod first and uploads dataset.tar while the environment is being set up, so a scarce GPU is
# not lost during a long upload. It rewrites upload.json about once a minute while uploading, then marks it done with
# the size. If upload.json stops changing for VS_UPLOAD_STALL seconds (the studio was closed, the network went down)
# the pod gives up and removes itself instead of waiting on rented time.
wait_upload() {
  [ -n "${VS_WAIT_UPLOAD:-}" ] || return 0
  echo upload > $STAGE_FILE
  put progress.json '{"phase":"upload"}'
  local last="" since=$SECONDS s want have
  while :; do
    s=$(cat "$JOB/upload.json" 2>/dev/null || true)
    if [[ "$s" == *'"status":"done"'* ]]; then
      want=$(printf '%s' "$s" | sed -n 's/.*"total":\([0-9]*\).*/\1/p')
      have=$(stat -c %s "$JOB/dataset.tar" 2>/dev/null || echo -1)
      if [ -z "$want" ] || [ "$have" = "$want" ]; then
        echo "[vs] dataset uploaded ($have bytes)"
        return 0
      fi
    fi
    if [ "$s" != "$last" ]; then last="$s"; since=$SECONDS; fi
    if [ $((SECONDS - since)) -ge "${VS_UPLOAD_STALL:-900}" ]; then
      echo "[vs] no word from the upload for ${VS_UPLOAD_STALL:-900} s; giving up"
      return 1
    fi
    sleep "${VS_UPLOAD_POLL:-10}"
  done
}

run_work() {
  echo setup > $STAGE_FILE
  put progress.json '{"phase":"setup"}'
  bash "$JOB/setup_env.sh" || return 1
  wait_upload || return 1
  echo unpack > $STAGE_FILE
  put progress.json '{"phase":"unpack"}'
  mkdir -p "$VS_DATA" && tar -xf "$JOB/dataset.tar" -C "$VS_DATA" || return 1
  echo train > $STAGE_FILE
  # shellcheck disable=SC1090
  source "$VS_ROOT/envs/${VS_ENGINE}/bin/activate" || return 1
  python "$JOB/train_entry.py" --config "$JOB/config.json" --data "$VS_DATA"
}

# hard time limit, independent of the training process
( sleep "${VS_MAX_SECONDS:-43200}"; kill -USR1 $$ ) &
WATCH_PID=$!

run_work &
WORK_PID=$!
wait "$WORK_PID"
rc=$?
WORK_PID=""

# model.tar is written atomically as soon as the weights are ready, before the optional sample phase,
# so a failure while sampling still delivers the trained model
if [ -f "$JOB/model.tar.json" ] || [ -f "$JOB/model.tar" ]; then
  put done.json "$(printf '{"status":"done","rc":%d,"samples":%s,"at":"%s"}' "$rc" \
    "$( { [ -f "$JOB/samples.tar.json" ] || [ -f "$JOB/samples.tar" ]; } && echo true || echo false)" "$(date -u +%FT%TZ)")"
  finish done
fi
fail "$(cat $STAGE_FILE 2>/dev/null || echo unknown)"

# Code review request: Voice Studio (engines, cloud training, evaluation)

You are GPT, reviewing code that Claude wrote for novel-lab's author. Use live web search to check upstream code and
documentation. Work read-only and answer in English. Today is 2026-10-06.

## What this is

In run 20261006-0603 you and Claude chose **VoxCPM2** as the primary engine (LoRA first, full fine-tuning for 5 h+) and
**Qwen3-TTS-12Hz-1.7B-Base** (official single-speaker SFT) as the fallback. Claude then built `voice-studio/`, a
personal platform for Windows + NVIDIA:

- import → VAD slicing → speaker matching → two-model Whisper transcription → review → versioned dataset;
- cloud fine-tuning on the user's own RunPod account (network volume + S3 API + REST pods);
- checkpoint scoring (speaker-embedding similarity + ASR accuracy) and local TTS.

The consent boundary from the research run still binds: only consented voices; no talent audio.

Pinned upstream code:
- VoxCPM: https://github.com/OpenBMB/VoxCPM at commit `f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629` (main, 2026-09-30).
  Trainer `scripts/train_voxcpm_finetune.py`; configs `conf/voxcpm_v2/voxcpm_finetune_{lora,all}.yaml`;
  inference `src/voxcpm/core.py`.
- Qwen3-TTS: https://github.com/QwenLM/Qwen3-TTS at commit `022e286b98fbec7e1e916cb940cdf532cd9f488e`.
  `finetuning/prepare_data.py`, `finetuning/sft_12hz.py`, `finetuning/dataset.py`, package `qwen_tts`.
- Pod image: `runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04`.
- RunPod REST v1 (`https://rest.runpod.io/v1`), S3-compatible API per datacenter (`https://s3api-<dc>.runpod.io`).

How a run works: the studio exports the dataset (`engines/export.py`), tars it, uploads config + `bootstrap.sh` +
the engine's `setup_env.sh`, `train_entry.py`, `vs_common.py` and `dataset.tar` to `s3://<volume>/vs/jobs/<id>/`,
then creates a pod whose start command runs `bootstrap.sh`. The pod writes `progress.json`, `model.tar`,
`done.json` or `error.json` and removes itself. The studio polls over S3, downloads `model.tar`, registers the model
and queues `evaluate_model`. Tests run the mock engine's `train_entry.py` locally to cover packaging and install.

## What to check (priority order)

1. **Upstream correctness.** Do `voxcpm2_train.py` and `qwen3_train.py` call the pinned trainers correctly (config
   keys, argument names, output layout, LoRA/full checkpoint folders, `load_lora`, `set_lora_enabled`,
   `from_pretrained(..., lora_weights_path=...)`, `generate(...)` arguments; Qwen `prepare_data.py` / `sft_12hz.py`
   arguments, `language` field, `generate_custom_voice` / `generate_voice_clone` / `create_voice_clone_prompt`)?
   Read the pinned files; cite file and line.
2. **Training defaults.** Are the step counts, learning rates, save intervals, `max_batch_tokens`, `ref_fraction`,
   epoch targets, GPU choices and container disk sizes sound for 1–50 h of single-speaker JA/EN data? Anything that
   will predictably OOM, overfit, run out of disk, or waste money?
3. **Pod lifecycle and cost safety.** Can any path leave a pod running or a run stuck (bootstrap traps, watchdog,
   self-removal with `runpodctl`, studio-side removal, resume after restart, cancellation)? Is the RunPod REST/S3
   usage right (`networkVolumeId`, `dataCenterIds`, `gpuTypeIds`, `containerDiskInGb`, `dockerStartCmd`, S3
   region/endpoint, 500 MB part limit)?
4. **Environment setup** (`remote/__init__.py` template): venv with system site-packages, torch/torchcodec
   constraints, editable install with `SETUPTOOLS_SCM_PRETEND_VERSION`, FlashAttention wheel URL, ffmpeg/sox.
   Will it install cleanly on that image? Local Windows install (`engines/install.py`, archive-zip installs)?
5. **Evaluation.** Is the checkpoint recommendation rule sound? Is comparing samples with and without a reference
   meaningful? Anything misleading in how similarity / accuracy are computed or shown?
6. **Local inference** (`engines/voxcpm2.py`, `engines/qwen3.py`, `tts.py`): modes (plain / ref / hifi), VRAM,
   Windows pitfalls (torch.compile/triton, flash-attn, DLLs).
7. **Security and privacy**: secrets handling, path traversal, the LAN password guard, anything written to logs.

## Output format

1. **Verdict** — one paragraph: ready for a first real run or not, and why.
2. **Findings** — a numbered list, most severe first. For each: severity (blocker / major / minor), file and
   function, what is wrong, evidence (pinned upstream file + line, or doc URL with checked date), and a concrete fix
   (a short patch or exact replacement code).
3. **Defaults table** — any parameter you would change, with old value, new value and reason.
4. **Open questions** — things only a real GPU run can settle, and the cheapest experiment to settle each.

Do not restate code that is fine. Do not invent APIs: if you cannot verify a call against the pinned code, say so.

## The code (voice-studio/, commit 8108599)

### `vstudio/cloud/bootstrap/bootstrap.sh`

```bash
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

```

### `vstudio/engines/remote/__init__.py`

```python
"""Files the engines upload next to bootstrap.sh for a cloud training run."""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).parent

SETUP_TEMPLATE = r"""#!/bin/bash
# Installs the {name} training environment on the network volume. It runs at the start of every training run but
# installs only once per pinned version: later runs find the stamp file and skip straight to training.
set -euo pipefail
ENV=/workspace/vs/envs/{engine}
SRC=/workspace/vs/src/{engine}
STAMP="$ENV/.ready-{commit}"

# system packages live on the container disk, so they are checked on every run (fast when present)
command -v ffmpeg >/dev/null 2>&1 || {{ apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg sox >/dev/null; }} || true

if [ -f "$STAMP" ]; then echo "[vs] {engine} environment ready"; exit 0; fi
echo "[vs] installing {engine} environment (first run only, about 10 minutes)"
rm -rf "$ENV" "$SRC"
python3 -m venv --system-site-packages "$ENV" || {{ pip install -q virtualenv && python3 -m virtualenv --system-site-packages "$ENV"; }}
source "$ENV/bin/activate"
python -m pip install -q --upgrade pip wheel
# keep the image's CUDA build of torch; never let a dependency replace it
python - <<'PY' > "$ENV/constraints.txt"
import torch, torchaudio
t = torch.__version__.split("+")[0]
print(f"torch=={{t}}"); print(f"torchaudio=={{torchaudio.__version__.split('+')[0]}}")
codec = {{"2.6": "0.2.*", "2.7": "0.5.*", "2.8": "0.7.*", "2.9": "0.8.*"}}.get(".".join(t.split(".")[:2]))
if codec: print(f"torchcodec=={{codec}}")
PY
cat "$ENV/constraints.txt"
mkdir -p "$SRC" && cd "$SRC"
git init -q && git fetch -q --depth 1 {repo} {commit} && git checkout -q FETCH_HEAD
export SETUPTOOLS_SCM_PRETEND_VERSION={version}
pip install -q -c "$ENV/constraints.txt" -e "$SRC" {extra_pip}
{post}
python -c "import {module}; print('[vs] {module} import ok')"
touch "$STAMP"
"""


def setup_script(engine: str, name: str, repo: str, commit: str, version: str, module: str, extra_pip: str = "",
                 post: str = "") -> str:
    return SETUP_TEMPLATE.format(engine=engine, name=name, repo=repo, commit=commit, version=version, module=module,
                                 extra_pip=extra_pip, post=post)


def read(name: str) -> str:
    return (HERE / name).read_text(encoding="utf-8")

```

### `vstudio/engines/remote/vs_common.py`

```python
"""Helpers shared by the engines' cloud training entry points.

This file runs on the rented GPU machine (inside the engine's environment), not on your PC. It is uploaded next to
bootstrap.sh for every training run. It only uses the standard library so it works in any engine environment.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import threading
import time
from pathlib import Path

LANG_NAMES = {"ja": "Japanese", "en": "English", "zh": "Chinese", "ko": "Korean", "de": "German", "fr": "French",
              "ru": "Russian", "pt": "Portuguese", "es": "Spanish", "it": "Italian"}


def log(msg: str) -> None:
    print(f"[vs] {msg}", flush=True)


class Job:
    """One training run: paths, parameters, progress reporting and packaging."""

    def __init__(self) -> None:
        argv = sys.argv
        self.config_path = Path(argv[argv.index("--config") + 1]).resolve()
        self.dir = self.config_path.parent                      # on the network volume (visible to the studio)
        self.data = Path(argv[argv.index("--data") + 1]) / "data"  # unpacked dataset (container disk)
        self.cfg = json.loads(self.config_path.read_text(encoding="utf-8"))
        self.params: dict = self.cfg.get("params", {})
        self.work = Path(os.environ.get("VS_WORK", "/root/vswork"))
        self.work.mkdir(parents=True, exist_ok=True)
        self.out = self.work / "model"                           # becomes model.tar → model/
        self.out.mkdir(parents=True, exist_ok=True)
        self._t0 = time.time()
        self._train_t0: float | None = None
        self._train_s0 = 0
        self._state: dict = {}

    # progress.json is read by the studio every 30 s over the S3 API
    def progress(self, **kw) -> None:
        self._state.update(kw)
        now = time.time()
        self._state["elapsed_s"] = int(now - self._t0)
        if kw.get("phase") == "train":  # measured speed, used by the studio to calibrate future estimates
            if self._train_t0 is None:
                self._train_t0, self._train_s0 = now, int(kw.get("step") or 0)
            elif (kw.get("step") or 0) > self._train_s0 + 2:
                self._state["s_per_step"] = round((now - self._train_t0) / (kw["step"] - self._train_s0), 3)
        tmp = self.dir / "progress.json.tmp"
        tmp.write_text(json.dumps(self._state), encoding="utf-8")
        os.replace(tmp, self.dir / "progress.json")

    def read_jsonl(self, name: str) -> list[dict]:
        f = self.data / name
        if not f.exists():
            return []
        return [json.loads(x) for x in f.read_text(encoding="utf-8").splitlines() if x.strip()]

    def run(self, cmd: list[str], cwd: Path | None = None, on_line=None, env: dict | None = None) -> None:
        """Run a command, echo its output to train.log and feed each line to on_line; raise on failure."""
        log("$ " + " ".join(str(c) for c in cmd))
        p = subprocess.Popen([str(c) for c in cmd], cwd=str(cwd) if cwd else None, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, bufsize=1, env={**os.environ, **(env or {})},
                             errors="replace")
        assert p.stdout is not None
        for line in p.stdout:
            sys.stdout.write(line)
            if on_line:
                try:
                    on_line(line.rstrip("\n"))
                except Exception as e:  # progress parsing must never stop training
                    log(f"progress parse: {e}")
        code = p.wait()
        if code != 0:
            raise RuntimeError(f"command failed with exit code {code}: {cmd[:3]}")

    def package(self, meta: dict) -> None:
        """Write engine.json and pack model/ into model.tar on the network volume (atomic rename)."""
        meta = {**meta, "training_id": self.cfg.get("training_id"), "params": self.params,
                "train_seconds": int(time.time() - self._t0)}
        (self.out / "engine.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        self.progress(phase="package")
        tmp = self.dir / "model.tar.tmp"
        with tarfile.open(tmp, "w") as t:
            t.add(self.out, arcname="model")
        os.replace(tmp, self.dir / "model.tar")
        log(f"packaged {(self.dir / 'model.tar').stat().st_size / 1e9:.2f} GB")


def sample_plan(job: Job) -> dict:
    """The held-out lines every checkpoint reads aloud, so checkpoints can be compared by ear and by score."""
    f = job.data / "samples.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"lines": [], "reference": None}


def free_gb(path: str = "/root") -> float:
    return shutil.disk_usage(path).free / 1e9


class LogTail(threading.Thread):
    """Follow a log file written by a trainer and call on_line for each new line."""

    def __init__(self, path: Path, on_line) -> None:
        super().__init__(daemon=True)
        self.path, self.on_line, self.stop = path, on_line, threading.Event()

    def run(self) -> None:
        pos = 0
        while not self.stop.is_set():
            if self.path.exists():
                with self.path.open("r", encoding="utf-8", errors="replace") as f:
                    f.seek(pos)
                    for line in f:
                        try:
                            self.on_line(line.rstrip("\n"))
                        except Exception:
                            pass
                    pos = f.tell()
            self.stop.wait(2)


METRIC = re.compile(r"([\w/]+):\s*(-?[\d.]+(?:e-?\d+)?)")


def parse_metrics(s: str) -> dict:
    return {k: float(v) for k, v in METRIC.findall(s)}

```

### `vstudio/engines/remote/voxcpm2_train.py`

```python
#!/usr/bin/env python3
"""VoxCPM2 fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/voxcpm2).

1. writes a training config from the studio's preset (LoRA or full fine-tuning, official recipe values);
2. runs the official trainer (scripts/train_voxcpm_finetune.py from the pinned VoxCPM commit);
3. every saved checkpoint, plus the untrained base model, reads the same held-out lines aloud (with and without a
   reference clip), so you can compare checkpoints by ear and the studio can score them;
4. packs the chosen checkpoints and the samples into model.tar.
"""
from __future__ import annotations

import json
import math
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import Job, LogTail, free_gb, log, parse_metrics, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/voxcpm2"))
BASE = "openbmb/VoxCPM2"
SEED = 1234


def count_lines(p: Path) -> int:
    return sum(1 for x in p.read_text(encoding="utf-8").splitlines() if x.strip())


def main() -> None:
    job = Job()
    p = job.params
    mode = p.get("mode", "lora")
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE, revision=p.get("base_revision") or None)
    log(f"base model at {base_path}")

    train_manifest, val_manifest = job.data / "train.jsonl", job.data / "val.jsonl"
    n_train = count_lines(train_manifest)
    bs, accum = int(p.get("batch_size", 2)), int(p.get("grad_accum", 8))
    per_epoch = max(1, n_train // bs // accum)
    total = int(round(per_epoch * float(p.get("epochs", 2))))
    total = max(int(p.get("min_steps", 150)), min(total, int(p.get("max_steps_cap", 30000))))
    n_saves = int(p.get("saves", 6))
    save_every = max(25, math.ceil(total / n_saves))
    ckpt = job.work / "ckpt"
    conf = {
        "pretrained_path": base_path,
        "train_manifest": str(train_manifest),
        "val_manifest": str(val_manifest) if val_manifest.exists() and count_lines(val_manifest) else "",
        "sample_rate": 16000,
        "out_sample_rate": 48000,
        "batch_size": bs,
        "grad_accum_steps": accum,
        "num_workers": 4,
        "preprocessing_num_workers": 4,
        "num_iters": total,
        "max_steps": total,
        "log_interval": 5,
        "valid_interval": save_every,
        "save_interval": save_every,
        "learning_rate": float(p.get("lr", 1e-4 if mode == "lora" else 1e-5)),
        "weight_decay": 0.01,
        "warmup_steps": max(10, min(100, total // 10)),
        "max_batch_tokens": int(p.get("max_batch_tokens", 8192)),
        "max_grad_norm": 1.0,
        "save_path": str(ckpt),
        "tensorboard": str(job.work / "tb"),
        "lambdas": {"loss/diff": 1.0, "loss/stop": 1.0},
    }
    if mode == "lora":
        conf["lora"] = {"enable_lm": True, "enable_dit": True, "enable_proj": bool(p.get("lora_proj", False)),
                        "r": int(p.get("rank", 32)), "alpha": int(p.get("alpha", 32)), "dropout": 0.0}
    conf_path = job.work / "train_conf.yaml"
    conf_path.write_text(json.dumps(conf, indent=2), encoding="utf-8")  # JSON is valid YAML
    log(f"{mode}: {n_train} clips, {per_epoch} updates/epoch, {total} updates, save every {save_every}")
    job.progress(phase="train", step=0, total=total, per_epoch=per_epoch, mode=mode)

    metrics_f = (job.out / "train_metrics.jsonl").open("w", encoding="utf-8")

    def on_line(line: str) -> None:
        # "[train] step 120: loss/diff: 0.41, loss/stop: 0.01, lr: ..., epoch: 1.2, grad_norm: ..."
        if line.startswith("[train] step ") or line.startswith("[val] step "):
            split = line[1:line.index("]")]
            step = int(line.split("step ", 1)[1].split(":", 1)[0])
            m = parse_metrics(line.split(":", 1)[1])
            metrics_f.write(json.dumps({"split": split, "step": step, **m}) + "\n")
            metrics_f.flush()
            loss = m.get("loss/diff", 0) + m.get("loss/stop", 0)
            if split == "train":
                job.progress(phase="train", step=step + 1, total=total, loss=round(loss, 4),
                             epoch=round(m.get("epoch", 0), 2))
            else:
                job.progress(val_loss=round(loss, 4))
        if mode == "full":
            prune_optimizer_states(ckpt)

    tail = LogTail(ckpt / "train.log", on_line)
    tail.start()
    job.run([sys.executable, SRC / "scripts" / "train_voxcpm_finetune.py", "--config_path", conf_path], cwd=SRC)
    tail.stop.set()
    tail.join(5)
    metrics_f.close()
    prune_optimizer_states(ckpt, keep_latest=False)

    steps = sorted(d for d in ckpt.iterdir() if d.is_dir() and d.name.startswith("step_"))
    if not steps:
        raise RuntimeError("trainer produced no checkpoints")
    keep = steps if mode == "lora" else steps[-int(p.get("keep_full", 3)):]
    log(f"checkpoints: {[d.name for d in steps]}; keeping weights of {[d.name for d in keep]}")

    # samples from every checkpoint (+ the untrained base for comparison)
    job.progress(phase="samples", step=0, total=len(steps) + 1)
    plan = sample_plan(job)
    ref = plan.get("reference")
    ref_path = str(job.data / ref["audio"]) if ref else None
    import soundfile as sf
    from voxcpm import VoxCPM

    def speak(model, name: str) -> None:
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        for i, line in enumerate(plan.get("lines", [])):
            for kind in ("plain", "ref"):
                if kind == "ref" and not ref_path:
                    continue
                try:
                    wav = model.generate(text=line["text"], reference_wav_path=ref_path if kind == "ref" else None,
                                         cfg_value=2.0, inference_timesteps=10, seed=SEED)
                    sf.write(str(d / f"{i}_{kind}.wav"), wav, model.tts_model.sample_rate)
                except Exception as e:
                    log(f"sample {name}/{i}_{kind} failed: {e}")

    ck_meta = []
    if mode == "lora":
        model = VoxCPM.from_pretrained(base_path, load_denoiser=False, optimize=False,
                                       lora_weights_path=str(steps[0]))
        model.set_lora_enabled(False)
        speak(model, "base")
        model.set_lora_enabled(True)
        for i, d in enumerate(steps):
            model.load_lora(str(d))
            speak(model, d.name)
            job.progress(phase="samples", step=i + 2, total=len(steps) + 1)
        del model
    else:
        model = VoxCPM.from_pretrained(base_path, load_denoiser=False, optimize=False)
        speak(model, "base")
        del model
        for i, d in enumerate(steps):
            model = VoxCPM.from_pretrained(str(d), load_denoiser=False, optimize=False)
            speak(model, d.name)
            del model
            job.progress(phase="samples", step=i + 2, total=len(steps) + 1)

    for d in steps:
        st = int(d.name.split("_")[1])
        has = d in keep
        if has:
            dst = job.out / "checkpoints" / d.name
            shutil.copytree(d, dst, ignore=shutil.ignore_patterns("optimizer.pth", "scheduler.pth"))
        ck_meta.append({"name": d.name, "step": st, "epoch": round(st / per_epoch, 2), "weights": has})
    log(f"free disk before packaging: {free_gb():.0f} GB")
    job.package({"engine": "voxcpm2", "mode": mode, "base": BASE, "base_revision": p.get("base_revision"),
                 "checkpoints": ck_meta, "samples": plan, "sample_rate": 48000, "total_steps": total,
                 "per_epoch": per_epoch, "seed": SEED})


def prune_optimizer_states(ckpt: Path, keep_latest: bool = True) -> None:
    """Full fine-tuning saves ~3× the model size of optimizer state per checkpoint; only `latest` needs it."""
    if not ckpt.exists():
        return
    for d in ckpt.iterdir():
        if d.is_dir() and d.name.startswith("step_") and (d / "training_state.json").exists():
            for f in ("optimizer.pth", "scheduler.pth"):
                (d / f).unlink(missing_ok=True)
    if not keep_latest:
        shutil.rmtree(ckpt / "latest", ignore_errors=True)


if __name__ == "__main__":
    main()

```

### `vstudio/engines/remote/qwen3_train.py`

```python
#!/usr/bin/env python3
"""Qwen3-TTS-12Hz-1.7B-Base single-speaker fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/qwen3).

Follows the official finetuning/ recipe of the pinned Qwen3-TTS commit:
prepare_data.py (extract 12 Hz audio codes) → sft_12hz.py (full SFT, one checkpoint per epoch).
Then every epoch's checkpoint, plus the untrained base model (zero-shot clone), reads the held-out lines aloud.
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import LANG_NAMES, Job, free_gb, log, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/qwen3"))
BASE = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
TOKENIZER = "Qwen/Qwen3-TTS-Tokenizer-12Hz"
SPEAKER = "vs_speaker"
SEED = 1234


def main() -> None:
    job = Job()
    p = job.params
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE)
    tok_path = snapshot_download(TOKENIZER)
    attn = "flash_attention_2" if importlib.util.find_spec("flash_attn") else "sdpa"
    log(f"attention: {attn}")

    plan = sample_plan(job)
    ref = plan.get("reference") or {}
    ref_abs = str(job.data / ref["audio"]) if ref.get("audio") else None
    if not ref_abs:
        raise RuntimeError("dataset has no reference clip")
    raw = job.work / "train_raw.jsonl"
    items = job.read_jsonl("train.jsonl")
    with raw.open("w", encoding="utf-8") as f:
        for it in items:  # the recipe recommends one fixed ref_audio for every line
            f.write(json.dumps({"audio": str(job.data / it["audio"]), "text": it["text"], "ref_audio": ref_abs,
                                "language": LANG_NAMES.get(it.get("lang") or "", "Auto")}, ensure_ascii=False) + "\n")

    job.progress(phase="prepare")
    codes = job.work / "train_with_codes.jsonl"
    ft = SRC / "finetuning"
    job.run([sys.executable, ft / "prepare_data.py", "--device", "cuda:0", "--tokenizer_model_path", tok_path,
             "--input_jsonl", raw, "--output_jsonl", codes], cwd=ft)

    # the official trainer hard-codes FlashAttention 2; fall back to PyTorch SDPA when it is not installed
    script = (ft / "sft_12hz.py").read_text(encoding="utf-8")
    if attn != "flash_attention_2":
        script = script.replace('"flash_attention_2"', '"sdpa"')
    (ft / "sft_vs.py").write_text(script, encoding="utf-8")

    bs, epochs = int(p.get("batch_size", 2)), int(p.get("epochs", 3))
    per_epoch = math.ceil(len(items) / bs)
    total = per_epoch * epochs
    out = job.work / "out"
    job.progress(phase="train", step=0, total=total, per_epoch=per_epoch, mode="sft")
    pat = re.compile(r"Epoch (\d+) \| Step (\d+) \| Loss: ([\d.]+)")
    metrics_f = (job.out / "train_metrics.jsonl").open("w", encoding="utf-8")

    def on_line(line: str) -> None:
        m = pat.search(line)
        if m:
            e, s, loss = int(m.group(1)), int(m.group(2)), float(m.group(3))
            step = e * per_epoch + s + 1
            metrics_f.write(json.dumps({"split": "train", "step": step, "loss": loss, "epoch": e}) + "\n")
            metrics_f.flush()
            job.progress(phase="train", step=step, total=total, loss=round(loss, 4),
                         epoch=round(step / per_epoch, 2))

    job.run([sys.executable, "sft_vs.py", "--init_model_path", base_path, "--output_model_path", out,
             "--train_jsonl", codes, "--batch_size", bs, "--lr", float(p.get("lr", 2e-5)),
             "--num_epochs", epochs, "--speaker_name", SPEAKER], cwd=ft, on_line=on_line)
    metrics_f.close()

    ckpts = sorted((d for d in out.iterdir() if d.name.startswith("checkpoint-epoch-")),
                   key=lambda d: int(d.name.rsplit("-", 1)[1]))
    if not ckpts:
        raise RuntimeError("trainer produced no checkpoints")
    keep = ckpts[-int(p.get("keep", 2)):]

    import soundfile as sf
    import torch
    from qwen_tts import Qwen3TTSModel

    job.progress(phase="samples", step=0, total=len(ckpts) + 1)
    lines = plan.get("lines", [])

    def write(name: str, i: int, wavs, sr) -> None:
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        sf.write(str(d / f"{i}_plain.wav"), wavs[0], sr)

    base = Qwen3TTSModel.from_pretrained(base_path, device_map="cuda:0", dtype=torch.bfloat16,
                                         attn_implementation=attn)
    prompt = base.create_voice_clone_prompt(ref_audio=ref_abs, ref_text=ref.get("text") or "",
                                            x_vector_only_mode=not ref.get("text"))
    for i, line in enumerate(lines):
        try:
            torch.manual_seed(SEED)
            wavs, sr = base.generate_voice_clone(text=line["text"], language=LANG_NAMES.get(line.get("lang"), "Auto"),
                                                 voice_clone_prompt=prompt)
            write("base", i, wavs, sr)
        except Exception as e:
            log(f"base sample {i} failed: {e}")
    del base
    torch.cuda.empty_cache()
    for k, d in enumerate(ckpts):
        m = Qwen3TTSModel.from_pretrained(str(d), device_map="cuda:0", dtype=torch.bfloat16, attn_implementation=attn)
        for i, line in enumerate(lines):
            try:
                torch.manual_seed(SEED)
                wavs, sr = m.generate_custom_voice(text=line["text"], speaker=SPEAKER,
                                                   language=LANG_NAMES.get(line.get("lang"), "Auto"))
                write(d.name, i, wavs, sr)
            except Exception as e:
                log(f"sample {d.name}/{i} failed: {e}")
        del m
        torch.cuda.empty_cache()
        job.progress(phase="samples", step=k + 2, total=len(ckpts) + 1)

    ck_meta = []
    for d in ckpts:
        ep = int(d.name.rsplit("-", 1)[1])
        has = d in keep
        if has:
            shutil.copytree(d, job.out / "checkpoints" / d.name)
        ck_meta.append({"name": d.name, "step": (ep + 1) * per_epoch, "epoch": ep + 1, "weights": has})
    log(f"free disk before packaging: {free_gb():.0f} GB")
    job.package({"engine": "qwen3", "mode": "sft", "base": BASE, "speaker": SPEAKER, "checkpoints": ck_meta,
                 "samples": plan, "total_steps": total, "per_epoch": per_epoch, "attn": attn, "seed": SEED})


if __name__ == "__main__":
    main()

```

### `vstudio/engines/base.py`

```python
"""The engine interface: one adapter per TTS model family.

An engine knows how to
- turn a studio dataset into its own training format (export_dataset);
- describe the cloud job that fine-tunes it (setup script, training entry point, container image, GPU sizes);
- load a fine-tuned model and synthesize speech locally (load / synthesize);
- translate the project's bracket performance tags ([deadpan], [laughs]) into its own control format.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


@dataclass
class TrainPreset:
    id: str
    label: str           # shown in the UI (zh-TW)
    description: str
    params: dict
    gpu: list[str]       # RunPod gpuTypeIds, in order of preference
    hours_per_data_hour: float  # rough wall-clock estimate per hour of training audio (before calibration)
    s_per_step: float = 0.0     # first guess of seconds per training step, replaced by measured speed after a run
    disk_gb: int = 80           # pod container disk
    min_hours: float = 0.0      # recommended minimum amount of approved audio
    recommended: bool = False


MODES = {"plain": "只用模型", "ref": "參考音色", "hifi": "完整複製"}


@dataclass
class Synthesis:
    audio: np.ndarray
    sr: int
    info: dict = field(default_factory=dict)


class Engine:
    id = "base"
    name = "Base"
    summary = ""
    license = ""
    license_note = ""
    languages: tuple[str, ...] = ()
    supports_tags = False       # inline bracket tags understood natively
    supports_instruct = False   # free-text style instruction
    needs_reference = False     # synthesis needs a reference clip
    infer_vram_gb = 0.0
    image = ""                  # container image for cloud training
    presets: list[TrainPreset] = []

    # --- dataset & training ---------------------------------------------------------------------------------
    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        """Write the engine's training files for dataset `ds` into out_dir; return info for config.json."""
        raise NotImplementedError

    def cloud_files(self) -> dict[str, str]:
        """Remote file name → contents (setup_env.sh, train_entry.py …) placed next to bootstrap.sh."""
        raise NotImplementedError

    def steps(self, n_train: int, preset_id: str) -> int:
        """Training steps the cloud script will run for n_train clips (0 = unknown)."""
        return 0

    def estimate(self, data_hours: float, preset_id: str, usd_h: float, n_train: int = 0,
                 s_per_step: float | None = None) -> dict:
        """Wall-clock and cost estimate. Uses the measured speed of an earlier run when there is one."""
        p = self.preset(preset_id)
        steps = self.steps(n_train, preset_id) if n_train else 0
        sps = s_per_step or p.s_per_step
        if steps and sps:
            train_h = steps * sps / 3600
            basis = "measured" if s_per_step else "guess"
        else:
            train_h = data_hours * p.hours_per_data_hour
            basis = "guess"
        hours = max(0.2, train_h) + 0.45  # + environment check, model download, samples, packaging
        return {"hours": round(hours, 2), "usd": round(hours * usd_h, 2), "steps": steps, "basis": basis}

    def preset(self, preset_id: str) -> TrainPreset:
        for p in self.presets:
            if p.id == preset_id:
                return p
        return self.presets[0]

    # --- inference ------------------------------------------------------------------------------------------
    def available(self) -> tuple[bool, str]:
        """Whether this machine can run the engine locally (packages installed, GPU memory)."""
        return False, "未安裝"

    def install_spec(self) -> dict:
        """pip requirements (and environment) to install the engine locally for inference."""
        return {}

    def modes(self, meta: dict) -> list[str]:
        """Synthesis modes a model supports: plain (model only), ref (reference timbre), hifi (reference + transcript)."""
        return ["plain"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        raise NotImplementedError

    def synthesize(self, handle, text: str, language: str | None = None, style: str = "", mode: str = "plain",
                   reference: dict | None = None, seed: int | None = None, **kw) -> Synthesis:
        """reference: {"path": wav, "text": transcript or ""}"""
        raise NotImplementedError

    def unload(self, handle) -> None:
        try:
            import gc
            del handle
            gc.collect()
            import torch
            torch.cuda.empty_cache()
        except Exception:
            pass

    # --- helpers for model folders -------------------------------------------------------------------------
    @staticmethod
    def model_meta(model_dir: Path) -> dict:
        """engine.json written by the cloud script; zero-shot models have none (or mode=zeroshot)."""
        import json
        f = Path(model_dir) / "engine.json"
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"mode": "zeroshot", "checkpoints": []}

    @staticmethod
    def checkpoint_dir(model_dir: Path, meta: dict, checkpoint: str | None) -> Path | None:
        cks = [c for c in meta.get("checkpoints", []) if c.get("weights")]
        if not cks:
            return None
        names = [c["name"] for c in cks]
        name = checkpoint if checkpoint in names else names[-1]
        return Path(model_dir) / "checkpoints" / name

    # --- tags -----------------------------------------------------------------------------------------------
    def render_tags(self, text_with_tags: str) -> tuple[str, str]:
        """Return (text for the engine, style instruction). Default: strip tags into a style instruction."""
        import re
        tags = re.findall(r"\[([^\[\]]+)\]", text_with_tags)
        text = re.sub(r"\s*\[[^\[\]]+\]\s*", " ", text_with_tags).strip()
        style = ", ".join(dict.fromkeys(t.strip() for t in tags))
        return text, style

    def info(self) -> dict:
        ok, why = self.available()
        return {"id": self.id, "name": self.name, "summary": self.summary, "license": self.license,
                "license_note": self.license_note, "languages": list(self.languages),
                "supports_tags": self.supports_tags, "supports_instruct": self.supports_instruct,
                "needs_reference": self.needs_reference, "infer_vram_gb": self.infer_vram_gb,
                "available": ok, "available_note": why,
                "install": bool(self.install_spec()),
                "presets": [{"id": p.id, "label": p.label, "description": p.description, "gpu": p.gpu,
                             "params": p.params, "min_hours": p.min_hours, "recommended": p.recommended}
                            for p in self.presets]}

```

### `vstudio/engines/voxcpm2.py`

```python
"""VoxCPM2 (OpenBMB, 2026-04): the studio's primary engine.

Why it is the default (research of 2026-10, with GPT): Apache-2.0 code and weights; official LoRA and full
fine-tuning; Japanese and English among 30 languages; the highest speaker similarity of the open models in the
shared MiniMax multilingual comparison (ja SIM 82.8, en 85.4); 48 kHz output; about 8 GB of VRAM for inference.
Its weak spot is a somewhat higher word error rate than Qwen3-TTS, which the studio's best-of-N screening and
checkpoint scoring are there to catch.

Synthesis modes
- plain: the fine-tuned model alone; a parenthesised style note may lead the text, e.g. "(quiet, unhurried)…".
- ref:   adds a reference clip for timbre; style notes still work.
- hifi:  "ultimate cloning": reference clip + its exact transcript, the model continues from it, keeping rhythm,
         accent and habits closest to the recording. Style notes are ignored in this mode.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

from . import export, remote
from .base import Engine, Synthesis, TrainPreset

REPO = "https://github.com/OpenBMB/VoxCPM.git"
COMMIT = "f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629"  # main on 2026-09-30, after release 2.0.3
VERSION = "2.0.3.post1"
BASE = "openbmb/VoxCPM2"
IMAGE = "runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04"
GPU_48 = ["NVIDIA L40S", "NVIDIA RTX 6000 Ada Generation", "NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB"]
GPU_80 = ["NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB", "NVIDIA H100 PCIe", "NVIDIA H100 80GB HBM3"]


class VoxCPM2Engine(Engine):
    id = "voxcpm2"
    name = "VoxCPM2"
    summary = ("OpenBMB 2026 年 4 月發表，20 億參數、48 kHz、支援日文與英文等 30 種語言。公開評測中音色相似度最高，"
               "有官方 LoRA 與完整微調。「完整複製」模式會接著參考錄音說下去，最能保留口音、節奏和說話習慣。")
    license = "Apache-2.0"
    license_note = "程式與權重皆為 Apache-2.0，個人與商業使用都可以；聲音本人的同意另外記錄在平台裡。"
    languages = ("ja", "en", "zh", "ko", "fr", "de", "es", "it", "pt", "ru")
    supports_instruct = True
    infer_vram_gb = 8
    image = IMAGE
    presets = [
        TrainPreset("lora", "LoRA 微調（建議先跑這個）",
                    "官方 LoRA 設定（rank 32、學習率 1e-4、有效批次 16），跑 2 個 epoch，途中存 6 個檢查點，"
                    "每個檢查點都會念同一批沒看過的句子讓你比較。適合 30 分鐘到 20 小時的資料。",
                    {"mode": "lora", "epochs": 2, "lr": 1e-4, "batch_size": 2, "grad_accum": 8, "rank": 32,
                     "alpha": 32, "saves": 6, "max_batch_tokens": 8192, "ref_fraction": 0.4},
                    GPU_48, hours_per_data_hour=0.12, s_per_step=7.0, disk_gb=80, min_hours=0.3, recommended=True),
        TrainPreset("full", "完整微調（資料 5 小時以上）",
                    "官方完整微調設定（學習率 1e-5、有效批次 16），跑 1.5 個 epoch，保留最後 3 個檢查點的權重。"
                    "資料多時可能比 LoRA 更像，但模型檔約 8 GB、需要 80 GB 顯示卡。建議先跑 LoRA 當對照。",
                    {"mode": "full", "epochs": 1.5, "lr": 1e-5, "batch_size": 2, "grad_accum": 8, "saves": 6,
                     "keep_full": 3, "max_batch_tokens": 8192, "ref_fraction": 0.4},
                    GPU_80, hours_per_data_hour=0.15, s_per_step=9.0, disk_gb=250, min_hours=5.0),
    ]

    # --- dataset & training ---------------------------------------------------------------------------------
    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        frac = float((params or {}).get("ref_fraction", 0.4))
        return export.write(ds, out_dir, ref_fraction=frac)

    def cloud_files(self) -> dict[str, str]:
        return {"setup_env.sh": remote.setup_script(self.id, "VoxCPM2", REPO, COMMIT, VERSION, "voxcpm"),
                "train_entry.py": remote.read("voxcpm2_train.py"), "vs_common.py": remote.read("vs_common.py")}

    def steps(self, n_train: int, preset_id: str) -> int:
        p = self.preset(preset_id).params
        per_epoch = max(1, n_train // (p["batch_size"] * p["grad_accum"]))
        return max(150, round(per_epoch * p["epochs"]))

    # --- inference ------------------------------------------------------------------------------------------
    def install_spec(self) -> dict:
        return {"pip": [f"voxcpm @ https://github.com/OpenBMB/VoxCPM/archive/{COMMIT}.zip"],
                "env": {"SETUPTOOLS_SCM_PRETEND_VERSION": VERSION}, "module": "voxcpm",
                "download": [BASE]}

    def available(self):
        if importlib.util.find_spec("voxcpm") is None:
            return False, "尚未安裝（設定 → 引擎 → 安裝）"
        try:
            import torch
            if not torch.cuda.is_available():
                return True, "已安裝，但沒有偵測到 NVIDIA GPU（可以用，但很慢）"
            total = torch.cuda.mem_get_info()[1] / 1e9
            if total < self.infer_vram_gb:
                return True, f"已安裝；顯示卡記憶體 {total:.0f} GB，低於建議的 {self.infer_vram_gb} GB"
        except Exception:
            pass
        return True, "已安裝"

    def modes(self, meta: dict) -> list[str]:
        return ["plain", "ref", "hifi"] if meta.get("mode") != "zeroshot" else ["ref", "hifi"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        from voxcpm import VoxCPM
        meta = self.model_meta(model_dir)
        kw = {"load_denoiser": False, "optimize": False}
        ck = self.checkpoint_dir(model_dir, meta, checkpoint)
        if meta.get("mode") == "lora" and ck:
            m = VoxCPM.from_pretrained(meta.get("base") or BASE, lora_weights_path=str(ck), **kw)
        elif meta.get("mode") == "full" and ck:
            m = VoxCPM.from_pretrained(str(ck), **kw)
        else:
            m = VoxCPM.from_pretrained(BASE, **kw)
        return {"model": m, "meta": meta, "checkpoint": ck.name if ck else None}

    def synthesize(self, handle, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
        m = handle["model"]
        args = {"cfg_value": float(kw.get("cfg", 2.0)), "inference_timesteps": int(kw.get("timesteps", 10)),
                "seed": seed}
        ref_path = str(reference["path"]) if reference and reference.get("path") else None
        if mode == "hifi" and ref_path and reference.get("text"):
            args.update(text=text, prompt_wav_path=ref_path, prompt_text=reference["text"],
                        reference_wav_path=ref_path)
        else:
            args["text"] = f"({style}){text}" if style else text
            if mode in ("ref", "hifi") and ref_path:
                args["reference_wav_path"] = ref_path
        wav = m.generate(**args)
        return Synthesis(wav, m.tts_model.sample_rate, {"mode": mode, "checkpoint": handle.get("checkpoint")})

```

### `vstudio/engines/qwen3.py`

```python
"""Qwen3-TTS-12Hz-1.7B-Base (Alibaba Qwen, 2026-01): the studio's second engine.

Why it is here: Apache-2.0; official single-speaker fine-tuning; the lowest word error rate of the open models in
the shared comparison (en WER 0.93 %, ja 3.82 %), so it is the one to try when VoxCPM2 mispronounces or skips words.
Its speaker similarity trails VoxCPM2 in the same comparison. The fine-tuned model is a full copy (~4 GB).

Modes: a fine-tuned model speaks on its own (plain), optionally with a style instruction (not guaranteed to work after
fine-tuning the Base model). A zero-shot model clones from a reference clip (ref) or clip + transcript (hifi).
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

from . import export, remote
from .base import Engine, Synthesis, TrainPreset

REPO = "https://github.com/QwenLM/Qwen3-TTS.git"
COMMIT = "022e286b98fbec7e1e916cb940cdf532cd9f488e"  # main on 2026-03-17 (package 0.1.1)
VERSION = "0.1.1"
BASE = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
IMAGE = "runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04"
FLASH_WHEEL = ("https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/"
               "flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp311-cp311-linux_x86_64.whl")
LANG = {"ja": "Japanese", "en": "English", "zh": "Chinese", "ko": "Korean", "de": "German", "fr": "French",
        "ru": "Russian", "pt": "Portuguese", "es": "Spanish", "it": "Italian"}


class Qwen3Engine(Engine):
    id = "qwen3"
    name = "Qwen3-TTS 1.7B"
    summary = ("阿里巴巴 Qwen 2026 年 1 月發表，17 億參數、10 種語言（含日文、英文）。公開評測中念錯字最少，"
               "有官方單一說話者微調。音色相似度略低於 VoxCPM2；當 VoxCPM2 念錯或漏字時拿來對照。")
    license = "Apache-2.0"
    license_note = "程式與權重皆為 Apache-2.0，個人與商業使用都可以。"
    languages = tuple(LANG)
    supports_instruct = True
    infer_vram_gb = 8
    image = IMAGE
    presets = [
        TrainPreset("sft", "官方微調（完整）",
                    "官方 finetuning 流程：先抽出 12 Hz 音訊碼，再做完整微調 3 個 epoch（學習率 2e-5、批次 2、"
                    "梯度累積 4），每個 epoch 一個檢查點，保留最後 2 個。",
                    {"epochs": 3, "lr": 2e-5, "batch_size": 2, "keep": 2},
                    ["NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB", "NVIDIA L40S", "NVIDIA H100 PCIe"],
                    hours_per_data_hour=0.12, s_per_step=0.5, disk_gb=120, min_hours=0.5, recommended=True),
    ]

    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        return export.write(ds, out_dir, ref_fraction=0.0)

    def cloud_files(self) -> dict[str, str]:
        post = (f'pip install -q --no-deps "{FLASH_WHEEL}" '
                '|| echo "[vs] FlashAttention wheel not available; training will use PyTorch SDPA"')
        return {"setup_env.sh": remote.setup_script(self.id, "Qwen3-TTS", REPO, COMMIT, VERSION, "qwen_tts",
                                                    post=post),
                "train_entry.py": remote.read("qwen3_train.py"), "vs_common.py": remote.read("vs_common.py")}

    def steps(self, n_train: int, preset_id: str) -> int:
        p = self.preset(preset_id).params
        return -(-n_train // p["batch_size"]) * p["epochs"]

    # --- inference ------------------------------------------------------------------------------------------
    def install_spec(self) -> dict:
        return {"pip": [f"qwen-tts @ https://github.com/QwenLM/Qwen3-TTS/archive/{COMMIT}.zip"], "env": {},
                "module": "qwen_tts", "download": [BASE, "Qwen/Qwen3-TTS-Tokenizer-12Hz"]}

    def available(self):
        if importlib.util.find_spec("qwen_tts") is None:
            return False, "尚未安裝（設定 → 引擎 → 安裝）"
        try:
            import torch
            if not torch.cuda.is_available():
                return True, "已安裝，但沒有偵測到 NVIDIA GPU（可以用，但很慢）"
        except Exception:
            pass
        return True, "已安裝"

    def modes(self, meta: dict) -> list[str]:
        return ["plain"] if meta.get("mode") == "sft" else ["ref", "hifi"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        import torch
        from qwen_tts import Qwen3TTSModel
        meta = self.model_meta(model_dir)
        ck = self.checkpoint_dir(model_dir, meta, checkpoint)
        cuda = torch.cuda.is_available()
        attn = "flash_attention_2" if cuda and importlib.util.find_spec("flash_attn") else "sdpa"
        src = str(ck) if (meta.get("mode") == "sft" and ck) else BASE
        m = Qwen3TTSModel.from_pretrained(src, device_map="cuda:0" if cuda else "cpu",
                                          dtype=torch.bfloat16 if cuda else torch.float32, attn_implementation=attn)
        return {"model": m, "meta": meta, "checkpoint": ck.name if ck and src != BASE else None, "prompts": {}}

    def synthesize(self, handle, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
        import torch
        m, meta = handle["model"], handle["meta"]
        lang = LANG.get(language or "", "Auto")
        if seed is not None:
            torch.manual_seed(seed)
        if meta.get("mode") == "sft":
            spk = meta.get("speaker", "vs_speaker")
            try:
                wavs, sr = m.generate_custom_voice(text=text, language=lang, speaker=spk, instruct=style or None)
            except TypeError:
                wavs, sr = m.generate_custom_voice(text=text, language=lang, speaker=spk)
        else:
            if not reference or not reference.get("path"):
                raise ValueError("零樣本模型需要參考片段")
            hifi = mode == "hifi" and bool(reference.get("text"))
            key = (str(reference["path"]), hifi)
            if key not in handle["prompts"]:
                handle["prompts"][key] = m.create_voice_clone_prompt(
                    ref_audio=str(reference["path"]), ref_text=reference.get("text") if hifi else None,
                    x_vector_only_mode=not hifi)
            wavs, sr = m.generate_voice_clone(text=text, language=lang, voice_clone_prompt=handle["prompts"][key])
        return Synthesis(wavs[0], sr, {"mode": mode, "checkpoint": handle.get("checkpoint")})

```

### `vstudio/engines/export.py`

```python
"""Dataset export shared by the real engines: training manifests plus the held-out lines every checkpoint reads."""
from __future__ import annotations

import json
import random
from pathlib import Path

from .. import datasets

MANIFEST_KEYS = ("audio", "text", "duration", "lang")


def _row(it: dict) -> dict:
    return {k: it[k] for k in MANIFEST_KEYS}


def pick_samples(val: list[dict], n: int = 6) -> list[dict]:
    """Up to n held-out lines, balanced across languages, preferring 3–12 s clips with good scores."""
    by_lang: dict[str, list[dict]] = {}
    for it in sorted(val, key=lambda i: (not 3 <= i["duration"] <= 12, -(i.get("score") or 0))):
        by_lang.setdefault(it.get("lang") or "", []).append(it)
    out: list[dict] = []
    while len(out) < n and any(by_lang.values()):
        for lang in list(by_lang):
            if by_lang[lang] and len(out) < n:
                out.append(by_lang[lang].pop(0))
    return [{"id": i["id"], "text": i["text"], "lang": i.get("lang") or "", "audio": i["audio"]} for i in out]


def write(ds: dict, out_dir: Path, ref_fraction: float = 0.0, seed: int = 11) -> dict:
    """train.jsonl / val.jsonl / samples.json in out_dir (paths relative to it; the wavs travel as wavs/).

    ref_fraction > 0 adds a reference clip of the same voice to that share of training lines (VoxCPM recommends
    30–50 % so the model keeps reference-based cloning), taken from a different recording where possible."""
    out_dir.mkdir(parents=True, exist_ok=True)
    train, val = datasets.load_items(ds, "train"), datasets.load_items(ds, "val")
    rnd = random.Random(seed)
    pool = [i for i in train if 3.0 <= i["duration"] <= 15.0]
    if len(pool) < 2:
        pool = train
    n_ref = 0
    with open(out_dir / "train.jsonl", "w", encoding="utf-8") as f:
        for it in train:
            row = _row(it)
            if ref_fraction and rnd.random() < ref_fraction and len(pool) > 1:
                others = [p for p in pool if p["id"] != it["id"] and p.get("source") != it.get("source")]
                ref = rnd.choice(others or [p for p in pool if p["id"] != it["id"]])
                row.update(ref_audio=ref["audio"], ref_duration=ref["duration"])
                n_ref += 1
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(out_dir / "val.jsonl", "w", encoding="utf-8") as f:
        for it in val:
            f.write(json.dumps(_row(it), ensure_ascii=False) + "\n")
    refs = ds["meta"].get("reference_items") or [{"audio": a, "text": ""} for a in ds["meta"].get("reference", [])]
    lines = pick_samples(val)
    if not lines:  # tiny datasets have no held-out lines; fall back to training lines (marked as seen)
        lines = [{**x, "seen": True} for x in pick_samples(train, 3)]
    samples = {"lines": lines, "reference": refs[0] if refs else None}
    (out_dir / "samples.json").write_text(json.dumps(samples, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"n_train": len(train), "n_val": len(val), "n_ref": n_ref, "files": ["train.jsonl", "val.jsonl",
                                                                               "samples.json"]}

```

### `vstudio/engines/install.py`

```python
"""Install a real engine into the studio's own Python environment (for local text to speech), then download its
base weights. Runs as a background job so the page stays usable; the full pip output goes to the job log."""
from __future__ import annotations

import importlib
import importlib.util
import os
import shutil
import subprocess
import sys

from .. import config, jobs
from . import get

TORCHCODEC = {"2.6": "0.2.*", "2.7": "0.5.*", "2.8": "0.7.*", "2.9": "0.8.*"}


def _constraints() -> str:
    """Pin the installed CUDA build of torch so no engine dependency can swap it for a CPU build."""
    import torch
    lines = [f"torch=={torch.__version__.split('+')[0]}"]
    try:
        import torchaudio
        lines.append(f"torchaudio=={torchaudio.__version__.split('+')[0]}")
    except ImportError:
        pass
    codec = TORCHCODEC.get(".".join(torch.__version__.split(".")[:2]))
    if codec:
        lines.append(f"torchcodec=={codec}")
    f = config.path("tmp", "constraints.txt")
    f.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(f)


@jobs.handler("install_engine", queue="io")
def install_engine(ctx: jobs.JobContext) -> dict:
    eng = get(ctx.params["engine"])
    spec = eng.install_spec()
    if not spec:
        return {"message": "這個引擎不需要安裝"}
    if importlib.util.find_spec("torch") is None:
        raise RuntimeError("還沒有安裝 PyTorch。請關掉 Voice Studio，重新執行 install.bat（會安裝 GPU 版 PyTorch）。")
    ctx.progress(0.05, "準備安裝", force=True)
    cons = _constraints()
    uv = shutil.which("uv")
    base = [uv, "pip", "install", "--python", sys.executable] if uv else [sys.executable, "-m", "pip", "install",
                                                                         "--progress-bar", "off"]
    cmd = [*base, "-c", cons, *spec["pip"]]
    ctx.log("$ " + " ".join(cmd))
    env = {**os.environ, **spec.get("env", {})}
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env, errors="replace",
                         creationflags=flags)
    assert p.stdout is not None
    n = 0
    for line in p.stdout:
        ctx.log(line)
        n += 1
        ctx.progress(min(0.6, 0.05 + n * 0.004), "安裝套件：" + line.strip()[:60])
    if p.wait() != 0:
        raise RuntimeError("安裝失敗，詳細訊息在工作紀錄。常見原因：網路中斷、磁碟空間不足。")
    importlib.invalidate_caches()
    if importlib.util.find_spec(spec["module"]) is None:
        raise RuntimeError("套件裝好了但載入不到，請重新啟動 Voice Studio 再試。")
    from huggingface_hub import snapshot_download
    repos = spec.get("download", [])
    for k, repo in enumerate(repos):
        ctx.progress(0.6 + 0.4 * k / max(1, len(repos)), f"下載模型權重 {repo}（數 GB，請稍候）", force=True)
        ctx.log(f"download {repo}")
        snapshot_download(repo, token=config.get_secret("hf_token") or None)
    return {"message": f"{eng.name} 已安裝，可以在本機合成語音"}

```

### `vstudio/datasets.py`

```python
"""Datasets: frozen, versioned snapshots of a voice's approved segments.

A dataset copies (or hard-links) its audio, so later edits to segments never change a dataset that was already used
for training. Every dataset records the voice's consent at the time it was built; training refuses a dataset
without one.
"""
from __future__ import annotations

import json
import os
import random
import shutil
from pathlib import Path

from . import config, db


class ConsentMissing(Exception):
    pass


def consent_ok(voice: dict) -> bool:
    c = voice.get("consent") or {}
    if not c.get("agreed") or not c.get("signed_name") or not c.get("date"):
        return False
    if voice["kind"] == "other" and not (voice.get("consent_doc") or c.get("document_note")):
        return False
    scope = set(c.get("scope") or [])
    return {"train", "generate"} <= scope


def _link(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def choose_reference(items: list[dict], n: int = 3) -> list[dict]:
    """Best-scoring clean clips of 5–12 s, used where an engine wants reference audio."""
    good = [i for i in items if 5.0 <= i["duration"] <= 12.0] or items
    good.sort(key=lambda i: (-(i.get("score") or 0), abs(i["duration"] - 8.0)))
    return good[:n]


def split_validation(items: list[dict], val_fraction: float, seed: int) -> set[str]:
    """Hold out whole recordings when there are enough of them, so validation lines are truly unseen
    (neighbouring clips of one recording share room sound and mood). Otherwise hold out random clips."""
    rnd = random.Random(seed)
    want = min(100, max(min(10, len(items) // 10), int(len(items) * val_fraction), 1 if len(items) >= 8 else 0))
    by_src: dict[str, list[dict]] = {}
    for i in items:
        by_src.setdefault(i.get("source") or "", []).append(i)
    if len(by_src) >= 5:
        srcs = list(by_src)
        rnd.shuffle(srcs)
        srcs.sort(key=lambda k: len(by_src[k]))  # small recordings first, so few are sacrificed
        picked: list[dict] = []
        for k in srcs:
            if len(picked) >= want:
                break
            if len(picked) + len(by_src[k]) <= max(want * 2, 12):
                picked += by_src[k]
        if picked:
            return {i["id"] for i in picked}
    order = items[:]
    rnd.shuffle(order)
    return {i["id"] for i in order[:want]}


def build(voice_id: str, name: str, min_score: float = 0.0, val_fraction: float = 0.02, seed: int = 7) -> dict:
    voice = db.get("voices", voice_id)
    if not voice:
        raise KeyError(voice_id)
    if not consent_ok(voice):
        raise ConsentMissing("這個聲音還沒有完整的同意紀錄，不能建立訓練資料。")
    segs = db.query("SELECT * FROM segments WHERE voice_id=? AND status='approved' AND COALESCE(score,1)>=? "
                    "AND text<>'' ORDER BY source_id, start", (voice_id, min_score))
    if not segs:
        raise ValueError("沒有已核可的片段。請先到「檢查資料」核可片段。")
    did = db.new_id("ds")
    root = config.DATA / "datasets" / did
    items = []
    for s in segs:
        dst = root / "wavs" / f"{s['id']}.wav"
        _link(Path(s["path"]), dst)
        items.append({"id": s["id"], "audio": f"wavs/{s['id']}.wav", "text": s["text"], "lang": s["lang"] or "",
                      "duration": round(s["duration"], 3), "score": s["score"], "source": s["source_id"]})
    val_ids = split_validation(items, val_fraction, seed)
    refs = choose_reference([i for i in items if i["id"] not in val_ids])
    with open(root / "train.jsonl", "w", encoding="utf-8") as tr, open(root / "val.jsonl", "w", encoding="utf-8") as va:
        for i in items:
            (va if i["id"] in val_ids else tr).write(json.dumps(i, ensure_ascii=False) + "\n")
    hours = sum(i["duration"] for i in items) / 3600
    langs = sorted({i["lang"] for i in items if i["lang"]})
    meta = {"voice": {"id": voice["id"], "name": voice["name"], "kind": voice["kind"]},
            "consent": voice["consent"], "consent_doc": voice.get("consent_doc"),
            "languages": langs, "n_train": len(items) - len(val_ids), "n_val": len(val_ids),
            "reference": [r["audio"] for r in refs],
            "reference_items": [{k: r[k] for k in ("id", "audio", "text", "lang", "duration")} for r in refs],
            "n_sources": len({i["source"] for i in items}), "min_score": min_score, "built_at": db.now()}
    (root / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    return db.insert("datasets", {"id": did, "voice_id": voice_id, "name": name, "n_items": len(items),
                                  "hours": round(hours, 3), "path": str(root), "meta": meta, "created_at": db.now()})


def load_items(ds: dict, split: str = "train") -> list[dict]:
    f = Path(ds["path"]) / f"{split}.jsonl"
    return [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]


def remove(dataset_id: str) -> None:
    ds = db.get("datasets", dataset_id)
    if ds:
        shutil.rmtree(ds["path"], ignore_errors=True)
        db.delete("datasets", dataset_id)

```

### `vstudio/training.py`

```python
"""Training runs: cloud (RunPod) fine-tuning, the model registry and zero-shot (no training) models."""
from __future__ import annotations

import json
import shutil
import tarfile
import time
from pathlib import Path

from . import config, datasets, db, engines, evaluate, jobs  # noqa: F401  (evaluate registers evaluate_model)
from .cloud import runpod

BOOTSTRAP = (Path(__file__).parent / "cloud" / "bootstrap" / "bootstrap.sh").read_text(encoding="utf-8")


def _speed_key(engine_id: str, preset_id: str, gpu: str) -> str:
    return f"{engine_id}:{preset_id}:{gpu}"


def plan(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, usd_h: float | None = None) -> dict:
    """What a run will use and roughly cost, shown before the user confirms."""
    ds = db.get("datasets", dataset_id)
    if not ds:
        raise KeyError(dataset_id)
    eng = engines.get(engine_id)
    p = eng.preset(preset_id)
    gpu = gpu or p.gpu[0]
    usd_h = usd_h or runpod.GPUS.get(gpu, {}).get("usd_h", 1.5)
    st = config.load_settings()
    measured = (st.get("speed") or {}).get(_speed_key(eng.id, p.id, gpu), {}).get("s_per_step")
    n_train = int(ds["meta"].get("n_train") or ds["n_items"])
    est = eng.estimate(ds["hours"], p.id, usd_h, n_train=n_train, s_per_step=measured)
    limit = float(st.get("runpod_max_hours") or 12)
    warnings = []
    if ds["hours"] < p.min_hours:
        warnings.append(f"這個設定建議至少 {p.min_hours:g} 小時已核可語音，目前只有 {ds['hours']:.2f} 小時。")
    if est["hours"] > limit:
        warnings.append(f"預估時間超過你設定的上限 {limit:g} 小時，訓練會在上限時被強制停止。請到設定調高上限。")
    if not ds["meta"].get("reference_items") and not ds["meta"].get("reference"):
        warnings.append("資料集沒有 5–12 秒的參考片段，樣本比較會比較不準。")
    return {"engine": eng.id, "preset": p.id, "gpu": gpu, "usd_per_hour": usd_h, "data_hours": ds["hours"],
            "n_train": n_train, "steps": est["steps"], "estimate_hours": est["hours"], "estimate_usd": est["usd"],
            "estimate_basis": est["basis"], "max_hours": limit, "max_usd": round(limit * usd_h, 2),
            "disk_gb": p.disk_gb, "warnings": warnings}


def start(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, name: str = "",
          params: dict | None = None, usd_h: float | None = None) -> dict:
    ds = db.get("datasets", dataset_id)
    voice = db.get("voices", ds["voice_id"])
    if not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音的同意紀錄不完整，不能訓練。")
    eng = engines.get(engine_id)
    pl = plan(dataset_id, engine_id, preset_id, gpu, usd_h)
    tid = db.new_id("tr")
    db.insert("trainings", {"id": tid, "voice_id": voice["id"], "dataset_id": dataset_id, "engine": engine_id,
                            "preset": {"id": pl["preset"], "params": {**eng.preset(preset_id).params, **(params or {})},
                                       "name": name},
                            "target": "runpod", "status": "queued", "gpu": pl["gpu"],
                            "remote_prefix": f"vs/jobs/{tid}", "progress": {}, "cost_estimate": pl["estimate_usd"],
                            "created_at": db.now()})
    job = jobs.submit("cloud_train", {"training_id": tid}, message="準備上傳")
    return db.update("trainings", tid, {"job_id": job["id"]})


def _set(tid: str, **kw) -> None:
    db.update("trainings", tid, kw)


def package_dataset(tid: str, work: Path) -> tuple[Path, dict]:
    """Export the dataset in the engine's format and pack it with its audio into dataset.tar."""
    tr = db.get("trainings", tid)
    ds = db.get("datasets", tr["dataset_id"])
    eng = engines.get(tr["engine"])
    exp = work / "export"
    shutil.rmtree(exp, ignore_errors=True)
    info = eng.export_dataset(ds, exp, tr["preset"]["params"])
    tar_path = work / "dataset.tar"
    with tarfile.open(tar_path, "w") as t:
        t.add(exp, arcname="data")
        t.add(Path(ds["path"]) / "wavs", arcname="data/wavs")
        t.add(Path(ds["path"]) / "meta.json", arcname="data/meta.json")
    cfg = {"training_id": tid, "engine": eng.id, "preset": tr["preset"]["id"], "params": tr["preset"]["params"],
           "dataset": {"id": ds["id"], "hours": ds["hours"], **info}, "voice_name": ds["meta"]["voice"]["name"],
           "languages": ds["meta"].get("languages", [])}
    return tar_path, cfg


@jobs.handler("cloud_train", queue="io")
def cloud_train(ctx: jobs.JobContext) -> dict:
    """Upload → pod → watch → download. Whatever goes wrong, the training row ends in a final state and no pod is
    left running."""
    tid = ctx.params["training_id"]
    try:
        return _cloud_train(ctx)
    except BaseException as e:
        tr = db.get("trainings", tid)
        if tr and tr["status"] not in ("done", "failed", "canceled"):
            if tr.get("pod_id"):
                try:
                    runpod.remove_pod(tr["pod_id"])
                except Exception:
                    pass
            _set(tid, status="canceled" if isinstance(e, jobs.Cancelled) else "failed", finished_at=db.now())
        raise


def _cloud_train(ctx: jobs.JobContext) -> dict:
    tid = ctx.params["training_id"]
    tr = db.get("trainings", tid)
    eng = engines.get(tr["engine"])
    st = config.load_settings()
    prefix = tr["remote_prefix"]
    work = config.DATA / "jobs" / tid
    work.mkdir(parents=True, exist_ok=True)

    resume = bool(ctx.params.get("resume") and tr.get("pod_id"))
    if resume:  # the studio was closed while the pod kept working: pick the run up again
        pod_id = tr["pod_id"]
        gpu_name = (tr.get("progress") or {}).get("gpu_name") or tr["gpu"]
        ctx.log(f"resuming watch of pod {pod_id}")
    else:
        # 1. package and upload
        _set(tid, status="uploading")
        ctx.progress(0.01, "整理訓練資料")
        tar_path, cfg = package_dataset(tid, work)
        runpod.put_text(f"{prefix}/config.json", json.dumps(cfg, ensure_ascii=False, indent=2))
        runpod.put_text(f"{prefix}/bootstrap.sh", BOOTSTRAP)
        for fname, text in eng.cloud_files().items():
            runpod.put_text(f"{prefix}/{fname}", text)
        runpod.upload(tar_path, f"{prefix}/dataset.tar",
                      progress=lambda f: ctx.progress(0.02 + 0.16 * f, f"上傳資料 {f * 100:.0f}%"))
        tar_path.unlink(missing_ok=True)
        ctx.check()

        # 2. create the pod
        _set(tid, status="starting")
        ctx.progress(0.19, "啟動雲端 GPU")
        max_h = float(st.get("runpod_max_hours") or 12)
        env = {"VS_TRAINING_ID": tid, "VS_ENGINE": eng.id, "VS_MAX_SECONDS": str(int(max_h * 3600))}
        hf = config.get_secret("hf_token")
        if hf:
            env["HF_TOKEN"] = hf
        preset = eng.preset(tr["preset"]["id"])
        gpus = [tr["gpu"]] + [g for g in preset.gpu if g != tr["gpu"]]
        pod = runpod.create_pod(f"voice-studio-{tid}", eng.image, gpus, env,
                                ["bash", "-c", f"bash /workspace/{prefix}/bootstrap.sh"],
                                container_disk_gb=preset.disk_gb)
        pod_id = pod.get("id")
        gpu_name = (pod.get("machine") or {}).get("gpuDisplayName") or tr["gpu"]
        _set(tid, status="running", pod_id=pod_id)
        ctx.log(f"pod {pod_id} created on {gpu_name}")

    # 3. watch
    max_h = float(st.get("runpod_max_hours") or 12)
    started = tr["created_at"] if resume else time.time()
    last_poll = 0.0
    prog: dict = {}
    try:
        while True:
            ctx.check()
            time.sleep(5)
            if time.time() - last_poll < 30:
                continue
            last_poll = time.time()
            prog = runpod.get_json(f"{prefix}/progress.json") or prog
            done = runpod.get_json(f"{prefix}/done.json")
            err = runpod.get_json(f"{prefix}/error.json")
            _set(tid, progress={**prog, "wall_s": int(time.time() - started), "gpu_name": gpu_name})
            ctx.progress(0.2 + 0.65 * _fraction(prog), _phase_label(prog))
            if done:
                break
            if err:
                raise RuntimeError(f"雲端訓練失敗（{_stage_label(err)}）。請到「雲端訓練」看紀錄。")
            if time.time() - started > max_h * 3600 + 900:
                raise RuntimeError("超過最長時數，已強制停止。")
            if runpod.get_pod(pod_id) is None and not runpod.get_json(f"{prefix}/done.json"):
                raise RuntimeError("雲端機器意外消失（可能被平台回收）。可以重試。")
    except jobs.Cancelled:
        runpod.remove_pod(pod_id)
        _set(tid, status="canceled", finished_at=db.now())
        _save_log(tid, prefix, work)
        raise
    except Exception:
        runpod.remove_pod(pod_id)
        _set(tid, status="failed", finished_at=db.now())
        _save_log(tid, prefix, work)
        raise
    runpod.remove_pod(pod_id)  # in case the pod did not remove itself
    _set(tid, status="downloading")
    if prog.get("s_per_step"):
        _remember_speed(eng.id, tr["preset"]["id"], tr["gpu"], float(prog["s_per_step"]))

    # 4. download and register
    tar_local = work / "model.tar"
    runpod.download(f"{prefix}/model.tar", tar_local,
                    progress=lambda f: ctx.progress(0.86 + 0.12 * f, f"下載模型 {f * 100:.0f}%"))
    _save_log(tid, prefix, work)
    m = install_model(tid, tar_local)
    _set(tid, status="done", finished_at=db.now())
    for name in ("dataset.tar", "model.tar"):  # keep the volume small; the log and config stay for reference
        try:
            runpod.delete_prefix(f"{prefix}/{name}")
        except Exception:
            pass
    return {"model_id": m["id"], "message": "訓練完成，模型已下載，正在評分各檢查點"}


def resume_interrupted() -> list[str]:
    """At start-up: runs whose watcher died with the app are picked up again (the pod kept training);
    runs interrupted before their pod existed are marked failed."""
    resumed = []
    for tr in db.query("SELECT * FROM trainings WHERE status IN ('queued','uploading','starting','running',"
                       "'downloading')"):
        j = db.get("jobs", tr["job_id"]) if tr.get("job_id") else None
        if j and j["status"] in ("queued", "running"):
            continue
        if tr["status"] in ("running", "downloading") and tr.get("pod_id"):
            job = jobs.submit("cloud_train", {"training_id": tr["id"], "resume": True}, "重新連上雲端訓練")
            _set(tr["id"], job_id=job["id"])
            resumed.append(tr["id"])
        else:
            if tr.get("pod_id"):
                try:
                    runpod.remove_pod(tr["pod_id"])
                except Exception:
                    pass
            _set(tr["id"], status="failed", finished_at=db.now())
    return resumed


def install_model(tid: str, tar_local: Path) -> dict:
    """Unpack model.tar into data/models/<id>, register it and queue checkpoint scoring."""
    tr = db.get("trainings", tid)
    ds = db.get("datasets", tr["dataset_id"])
    eng = engines.get(tr["engine"])
    model_id = db.new_id("mdl")
    mdir = config.DATA / "models" / model_id
    tmp = config.DATA / "tmp" / f"unpack-{model_id}"
    with tarfile.open(tar_local) as t:
        t.extractall(tmp, filter="data")
    shutil.move(str(tmp / "model"), str(mdir))
    shutil.rmtree(tmp, ignore_errors=True)
    tar_local.unlink(missing_ok=True)
    refs = _copy_references(ds, mdir)
    voice = db.get("voices", tr["voice_id"])
    emeta = eng.model_meta(mdir)
    cks = [c for c in emeta.get("checkpoints", []) if c.get("weights")]
    m = db.insert("models", {
        "id": model_id, "voice_id": voice["id"], "engine": eng.id,
        "name": tr["preset"].get("name") or f"{voice['name']} · {eng.name} · {eng.preset(tr['preset']['id']).label}",
        "training_id": tid, "path": str(mdir),
        "meta": {"dataset_id": ds["id"], "preset": tr["preset"], "consent": ds["meta"].get("consent"),
                 "mode": emeta.get("mode"), "checkpoint": cks[-1]["name"] if cks else None, "references": refs,
                 "languages": ds["meta"].get("languages", [])},
        "metrics": {}, "created_at": db.now()})
    jobs.submit("evaluate_model", {"model_id": model_id}, message="評分檢查點")
    return m


def _copy_references(ds: dict, mdir: Path, limit: int = 3) -> list[dict]:
    items = ds["meta"].get("reference_items") or [{"audio": a, "text": "", "lang": ""}
                                                    for a in ds["meta"].get("reference", [])]
    out = []
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    for k, it in enumerate(items[:limit]):
        src = Path(ds["path"]) / it["audio"]
        if not src.exists():
            continue
        dst = mdir / "references" / f"ref{k}.wav"
        shutil.copy2(src, dst)
        out.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": it.get("text", ""),
                    "lang": it.get("lang", ""), "label": "資料集參考 " + str(k + 1), "segment_id": it.get("id")})
    return out


def create_zeroshot(voice_id: str, engine_id: str, segment_ids: list[str], name: str = "") -> dict:
    """A model without training: the base model cloning from reference clips. Free and instant; a good way to hear
    an engine before paying for training, though it copies habits and accent far less than a fine-tuned model."""
    voice = db.get("voices", voice_id)
    if not voice:
        raise KeyError(voice_id)
    if not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音的同意紀錄不完整，不能用來合成。")
    eng = engines.get(engine_id)
    if "ref" not in eng.modes({"mode": "zeroshot"}):
        raise ValueError("這個引擎不支援零樣本")
    model_id = db.new_id("mdl")
    mdir = config.DATA / "models" / model_id
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    refs = []
    for k, sid in enumerate(segment_ids[:5]):
        s = db.get("segments", sid)
        if not s or s["voice_id"] != voice_id:
            continue
        shutil.copy2(s["path"], mdir / "references" / f"ref{k}.wav")
        refs.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": s["text"], "lang": s["lang"] or "",
                     "label": (s["text"][:24] + "…") if len(s["text"]) > 24 else s["text"], "segment_id": sid})
    if not refs:
        raise ValueError("請至少選一個這個聲音的片段當參考")
    (mdir / "engine.json").write_text(json.dumps({"engine": eng.id, "mode": "zeroshot", "checkpoints": []}),
                                      encoding="utf-8")
    return db.insert("models", {"id": model_id, "voice_id": voice_id, "engine": eng.id,
                                "name": name or f"{voice['name']} · {eng.name} · 免訓練", "path": str(mdir),
                                "meta": {"mode": "zeroshot", "references": refs, "languages": voice["languages"]},
                                "metrics": {}, "created_at": db.now()})


def add_reference(model_id: str, segment_id: str, label: str = "") -> dict:
    m = db.get("models", model_id)
    s = db.get("segments", segment_id)
    if not m or not s:
        raise KeyError("model or segment")
    if s["voice_id"] != m["voice_id"]:
        raise ValueError("只能用同一個聲音的片段當參考")
    refs = list((m["meta"] or {}).get("references", []))
    k = max([int(r["id"][3:]) for r in refs if r["id"].startswith("ref")] + [-1]) + 1
    mdir = Path(m["path"])
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    shutil.copy2(s["path"], mdir / "references" / f"ref{k}.wav")
    refs.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": s["text"], "lang": s["lang"] or "",
                 "label": label or s["text"][:24], "segment_id": segment_id})
    return db.update("models", model_id, {"meta": {**m["meta"], "references": refs}})


def remove_reference(model_id: str, ref_id: str) -> dict:
    m = db.get("models", model_id)
    refs = [r for r in m["meta"].get("references", []) if r["id"] != ref_id]
    (Path(m["path"]) / "references" / f"{ref_id}.wav").unlink(missing_ok=True)
    return db.update("models", model_id, {"meta": {**m["meta"], "references": refs}})


def _remember_speed(engine_id: str, preset_id: str, gpu: str, s_per_step: float) -> None:
    st = config.load_settings()
    speed = dict(st.get("speed") or {})
    speed[_speed_key(engine_id, preset_id, gpu)] = {"s_per_step": s_per_step, "at": db.now()}
    config.save_settings({"speed": speed})


def _save_log(tid: str, prefix: str, work: Path) -> None:
    try:
        (work / "train.log").write_text(runpod.get_text(f"{prefix}/train.log"), encoding="utf-8")
    except Exception:
        pass


def _fraction(p: dict) -> float:
    """Overall cloud progress 0–1 across phases (training dominates)."""
    ph = p.get("phase")
    frac = (p.get("step", 0) / p["total"]) if p.get("total") else 0.0
    return {"setup": 0.02, "unpack": 0.04, "download": 0.06, "prepare": 0.08}.get(ph) or \
        {"train": 0.1 + 0.75 * frac, "samples": 0.85 + 0.12 * frac, "package": 0.98}.get(ph, 0.0)


def _phase_label(p: dict) -> str:
    ph = p.get("phase")
    if ph == "setup":
        return "雲端安裝環境（第一次約 10 分鐘，之後會跳過）"
    if ph == "unpack":
        return "解開資料"
    if ph == "download":
        return "下載基礎模型（第一次較久）"
    if ph == "prepare":
        return "預先處理音訊"
    if ph == "samples":
        return f"各檢查點試念樣本 {p.get('step', 0)}/{p.get('total', '?')}"
    if ph == "package":
        return "打包模型"
    if ph == "train" and p.get("total"):
        loss = f"，loss {p['loss']:.3f}" if isinstance(p.get("loss"), (int, float)) else ""
        eta = ""
        if p.get("s_per_step"):
            left = (p["total"] - p.get("step", 0)) * p["s_per_step"] / 60
            eta = f"，約剩 {left:.0f} 分"
        return f"訓練中 {p.get('step', 0)}/{p['total']}{loss}{eta}"
    return "雲端執行中"


def _stage_label(err: dict) -> str:
    return {"setup": "安裝環境", "unpack": "解開資料", "train": "訓練", "package": "打包",
            None: "逾時" if err.get("status") == "timeout" else "未知"}.get(err.get("stage"), err.get("stage") or "?")


def remove_model(model_id: str) -> None:
    m = db.get("models", model_id)
    if m:
        from . import tts
        tts.unload_if(model_id)
        shutil.rmtree(m["path"], ignore_errors=True)
        db.delete("models", model_id)

```

### `vstudio/evaluate.py`

```python
"""Score a trained model's checkpoints on the held-out lines they read aloud in the cloud.

For every checkpoint (and the untrained base, for comparison) and every sample clip:
- similarity: speaker-embedding cosine to the voice (its enrollment centroid, else the real held-out recordings);
- accuracy: speech recognition of the clip compared with the line it should have said (1 = word for word).
The recommendation is the most similar checkpoint whose accuracy is within 0.05 of the most accurate one, because
fine-tuning can raise similarity while the model starts to skip or invent words. Listening still decides: the
Models page plays every clip next to the real recording.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from . import audio, config, db, engines, jobs
from .pipeline import asr, prepare, speaker


def _clip(path: Path) -> np.ndarray:
    y, _ = audio.load(path, 16000)
    return y


@jobs.handler("evaluate_model", queue="gpu")
def evaluate_model(ctx: jobs.JobContext) -> dict:
    m = db.get("models", ctx.params["model_id"])
    mdir = Path(m["path"])
    eng = engines.get(m["engine"])
    meta = eng.model_meta(mdir)
    plan = meta.get("samples") or {}
    lines = plan.get("lines", [])
    sdir = mdir / "samples"
    names = ["base"] + [c["name"] for c in meta.get("checkpoints", [])]
    names = [n for n in names if (sdir / n).exists()]
    if not lines or not names:
        return {"message": "沒有可評分的樣本"}
    st = config.load_settings()
    emb = speaker.Embedder()
    target = prepare.voice_centroids([m["voice_id"]]).get(m["voice_id"])
    ds = db.get("datasets", (m["meta"] or {}).get("dataset_id", "")) if m.get("meta") else None
    gt_sims = []
    if ds:
        gts = [Path(ds["path"]) / ln["audio"] for ln in lines if ln.get("audio")]
        gt_embs = [emb.embed(_clip(g)) for g in gts if g.exists()]
        if gt_embs and target is None:
            c = np.mean(gt_embs, axis=0)
            target = c / (np.linalg.norm(c) + 1e-9)
            # the ceiling: each real recording against the others (leave-one-out, so it is not inflated)
            if len(gt_embs) > 1:
                gt_sims = [speaker.cosine(e, np.mean([o for j, o in enumerate(gt_embs) if j != i], axis=0))
                           for i, e in enumerate(gt_embs)]
        elif target is not None:
            gt_sims = [speaker.cosine(e, target) for e in gt_embs]
    if target is None:
        return {"message": "這個聲音沒有登錄片段，也找不到原始資料，無法計算相似度"}

    total = len(names) * len(lines)
    done = 0
    rows = []
    asr_ok = True
    for name in names:
        sims, agrees, clips = [], [], []
        for i, ln in enumerate(lines):
            ctx.check()
            for kind in ("plain", "ref"):
                f = sdir / name / f"{i}_{kind}.wav"
                if not f.exists():
                    continue
                y = _clip(f)
                sim = speaker.cosine(emb.embed(y), target)
                agree = None
                if asr_ok:
                    try:
                        t = asr.transcribe(y, st["asr_secondary"], language=ln.get("lang") or None,
                                           device=st["asr_device"])
                        agree = asr.agreement(ln["text"], t["text"], ln.get("lang") or t["lang"])
                    except Exception:
                        asr_ok = False
                sims.append(sim)
                if agree is not None:
                    agrees.append(agree)
                clips.append({"line": i, "kind": kind, "sim": round(sim, 3),
                              "agree": None if agree is None else round(agree, 3)})
            done += 1
            ctx.progress(done / total, f"評分 {name}")
        rows.append({"name": name, "sim": round(float(np.mean(sims)), 4) if sims else None,
                     "agree": round(float(np.mean(agrees)), 4) if agrees else None, "clips": clips})

    with_weights = {c["name"] for c in meta.get("checkpoints", []) if c.get("weights")}
    cands = [r for r in rows if r["name"] in with_weights and r["sim"] is not None]
    rec = None
    if cands:
        best_agree = max((r["agree"] for r in cands if r["agree"] is not None), default=None)
        ok = [r for r in cands if best_agree is None or r["agree"] is None or r["agree"] >= best_agree - 0.05]
        rec = max(ok or cands, key=lambda r: r["sim"])["name"]
    metrics = {"checkpoints": rows, "recommended": rec,
               "ground_truth_sim": round(float(np.mean(gt_sims)), 4) if gt_sims else None,
               "asr": asr_ok, "evaluated_at": db.now()}
    new_meta = dict(m["meta"] or {})
    if rec and not new_meta.get("checkpoint_chosen_by_user"):
        new_meta["checkpoint"] = rec
    db.update("models", m["id"], {"metrics": metrics, "meta": new_meta})
    return {"recommended": rec, "message": f"評分完成，建議使用 {rec}" if rec else "評分完成"}

```

### `vstudio/tts.py`

```python
"""Text to speech: single lines, best-of-N takes, and whole scene scripts."""
from __future__ import annotations

import json
import re
import threading
from pathlib import Path

import numpy as np

from . import audio, config, db, engines, jobs
from .pipeline import asr

_loaded: dict = {"key": None, "handle": None, "engine": None}
_load_lock = threading.Lock()

KANA = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")


def detect_language(text: str) -> str:
    """Good enough for ja/en scripts: any kana or kanji means Japanese."""
    return "ja" if KANA.search(text) else "en"


def _handle(model_id: str):
    """Keep one model in GPU memory at a time; switching models (or checkpoints) unloads the previous one."""
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    ck = (m["meta"] or {}).get("checkpoint")
    key = (model_id, ck)
    with _load_lock:
        if _loaded["key"] == key:
            return m, _loaded["engine"], _loaded["handle"]
        if _loaded["handle"] is not None:
            _loaded["engine"].unload(_loaded["handle"])
            _loaded.update(key=None, handle=None, engine=None)
        eng = engines.get(m["engine"])
        ok, why = eng.available()
        if not ok:
            raise RuntimeError(f"{eng.name}：{why}")
        h = eng.load(Path(m["path"]), ck)
        _loaded.update(key=key, handle=h, engine=eng)
        return m, eng, h


def unload() -> None:
    with _load_lock:
        if _loaded["handle"] is not None:
            _loaded["engine"].unload(_loaded["handle"])
        _loaded.update(key=None, handle=None, engine=None)


def unload_if(model_id: str) -> None:
    if _loaded["key"] and _loaded["key"][0] == model_id:
        unload()


def loaded() -> dict | None:
    k = _loaded["key"]
    return {"model_id": k[0], "checkpoint": k[1]} if k else None


def reference(m: dict, ref_id: str | None) -> dict | None:
    refs = (m["meta"] or {}).get("references") or []
    r = next((x for x in refs if x["id"] == ref_id), refs[0] if refs else None)
    if not r:
        return None
    return {"id": r["id"], "path": Path(m["path"]) / r["file"], "text": r.get("text", ""), "lang": r.get("lang", "")}


def _screen(y: np.ndarray, sr: int, text: str, lang: str | None) -> dict:
    """Transcribe a take and compare it with the requested text (catches skipped, repeated or garbled words)."""
    try:
        x16 = audio.resample(y, sr, 16000)
        st = config.load_settings()
        t = asr.transcribe(x16, st["asr_secondary"], language=lang, device=st["asr_device"])
        return {"heard": t["text"], "match": round(asr.agreement(text, t["text"], lang or t["lang"]), 3)}
    except Exception as e:  # ASR not installed (e.g. test machines)
        return {"heard": "", "match": None, "note": str(e)[:120]}


def generate(model_id: str, text: str, language: str | None = None, style: str = "", takes: int = 1,
             seed: int | None = None, screen: bool = True, batch: str | None = None, mode: str | None = None,
             ref_id: str | None = None, extra: dict | None = None) -> dict:
    """Generate `takes` versions, score them, keep all, and mark the best."""
    m, eng, h = _handle(model_id)
    meta = eng.model_meta(Path(m["path"]))
    modes = eng.modes(meta)
    mode = mode if mode in modes else modes[0]
    text_engine, tag_style = eng.render_tags(text)
    if eng.supports_tags:
        text_engine = text
    full_style = ", ".join(s for s in (tag_style, style) if s)
    lang = language if language and language != "auto" else detect_language(text_engine)
    ref = reference(m, ref_id) if mode in ("ref", "hifi") else None
    if mode in ("ref", "hifi") and ref is None:
        raise ValueError("這個模式需要參考片段，請先在模型頁加入參考片段")
    outs = []
    base_seed = seed if seed is not None else int(np.random.default_rng().integers(0, 2 ** 31 - 1))
    for k in range(max(1, min(8, takes))):
        s = base_seed + k
        with jobs.GPU_LOCK:
            syn = eng.synthesize(h, text_engine, language=lang, style=full_style, mode=mode, reference=ref, seed=s,
                                 **(extra or {}))
        oid = db.new_id("out")
        path = audio.save(config.DATA / "outputs" / f"{oid}.wav", syn.audio, syn.sr,
                          synthetic={"engine": eng.id, "model": model_id, "voice": m["voice_id"]})
        dur = len(syn.audio) / syn.sr
        sc = _screen(syn.audio, syn.sr, text_engine, lang) if screen else {}
        outs.append(db.insert("outputs", {"id": oid, "model_id": model_id, "text": text,
                                          "params": {"language": lang, "style": full_style, "seed": s,
                                                     "engine": eng.id, "mode": mode,
                                                     "ref": ref["id"] if ref else None,
                                                     "checkpoint": syn.info.get("checkpoint"), **(extra or {})},
                                          "path": str(path), "duration": round(dur, 3), "score": sc,
                                          "batch": batch, "created_at": db.now()}))
    if len(outs) > 1:
        durs = np.array([o["duration"] for o in outs])
        med = float(np.median(durs))
        for o in outs:
            match = o["score"].get("match")
            ratio = o["duration"] / med if med else 1
            o["score"]["rank_value"] = (match if match is not None else 0.5) - abs(1 - ratio) * 0.5
        best = max(outs, key=lambda o: o["score"]["rank_value"])
        for o in outs:
            o["score"]["best"] = o["id"] == best["id"]
            db.update("outputs", o["id"], {"score": o["score"]})
    elif outs:
        outs[0]["score"]["best"] = True
        db.update("outputs", outs[0]["id"], {"score": outs[0]["score"]})
    return {"outputs": outs, "mode": mode, "language": lang}


# --- scene scripts -------------------------------------------------------------------------------------------------

LINE = re.compile(r"^(?P<speaker>[^:]{1,80}?)\s*::\s*(?P<text>.*)$")
RESERVED = {"STAGE", "SFX", "PAUSE", "ROMAJI", "GLOSS", "NOTE"}


def parse_script(text: str) -> list[dict]:
    """The novel-lab scene format: `Name :: [tags] line`, with STAGE/SFX/PAUSE/ROMAJI/GLOSS metadata lines.
    Returns turns and pauses in order; narration and metadata are kept for the listening sheet but not spoken."""
    events = []
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("@@"):
            continue
        m = LINE.match(line)
        if not m:
            continue
        who, body = m.group("speaker").strip(), m.group("text").strip()
        if who in RESERVED:
            if who == "PAUSE":
                try:
                    events.append({"kind": "pause", "seconds": float(body), "line": n})
                except ValueError:
                    pass
            elif who in ("ROMAJI", "GLOSS") and events and events[-1]["kind"] == "turn":
                events[-1][who.lower()] = body
            else:
                events.append({"kind": who.lower(), "text": body, "line": n})
            continue
        events.append({"kind": "turn", "speaker": who, "text": body, "line": n})
    return events


@jobs.handler("render_script", queue="gpu")
def render_script(ctx: jobs.JobContext) -> dict:
    """Render a whole scene: every turn with its cast model, joined with natural gaps and PAUSE lines."""
    p = ctx.params
    events = parse_script(p["script"])
    cast: dict = p["cast"]  # speaker name → {model_id, language, style}
    batch = db.new_id("scene")
    turns = [e for e in events if e["kind"] == "turn" and e["speaker"].lower() != "narrator"]
    missing = sorted({t["speaker"] for t in turns if t["speaker"] not in cast})
    if missing:
        raise ValueError("這些角色還沒有指定聲音：" + "、".join(missing))
    parts, sheet, sr_out = [], [], 48000
    for i, e in enumerate(events):
        ctx.progress(i / max(1, len(events)), f"第 {i + 1}/{len(events)} 行")
        if e["kind"] == "pause" and parts:
            parts[-1] = (parts[-1][0], parts[-1][1] + e["seconds"])
            continue
        if e["kind"] != "turn" or e["speaker"].lower() == "narrator":
            continue
        c = cast[e["speaker"]]
        res = generate(c["model_id"], e["text"], language=c.get("language"), style=c.get("style", ""),
                       takes=int(p.get("takes", 2)), batch=batch, mode=c.get("mode"), ref_id=c.get("ref_id"))
        best = next((o for o in res["outputs"] if o["score"].get("best")), res["outputs"][0])
        y, sr = audio.load(Path(best["path"]), sr_out)
        parts.append((y, float(p.get("gap", 0.35))))
        sheet.append({"line": e["line"], "speaker": e["speaker"], "text": e["text"], "romaji": e.get("romaji"),
                      "output": best["id"], "match": best["score"].get("match")})
    mix = audio.concat(parts, sr_out)
    path = audio.save(config.DATA / "outputs" / f"{batch}.wav", mix, sr_out, synthetic={"scene": batch})
    (config.DATA / "outputs" / f"{batch}.json").write_text(json.dumps(sheet, ensure_ascii=False, indent=2),
                                                           encoding="utf-8")
    db.insert("outputs", {"id": batch, "model_id": None, "text": p["script"][:2000], "params": {"scene": True},
                          "path": str(path), "duration": round(len(mix) / sr_out, 2), "score": {"lines": len(sheet)},
                          "batch": batch, "created_at": db.now()})
    return {"output_id": batch, "lines": len(sheet), "message": f"場景完成：{len(sheet)} 句"}

```

### `vstudio/cloud/runpod.py`

```python
"""RunPod: network volume storage over the S3-compatible API, and GPU pods over the REST API.

Flow for one training run (all from the user's own RunPod account):
1. upload the dataset, the engine's setup and training scripts, and a config to the network volume
   (s3://<volume id>/vs/jobs/<training id>/);
2. create a pod on that volume's datacenter; its start command runs bootstrap.sh, which installs the engine once
   (cached on the volume), trains, writes progress.json while it works and model.tar at the end, then removes itself;
3. the studio polls the pod and progress.json, downloads model.tar when done.json appears, and removes the pod itself
   too if the pod is still there (belt and braces: a forgotten GPU is the main way to lose money).
Keys are read from the OS credential store; they are never written to disk or logs by the studio.
"""
from __future__ import annotations

import json
from pathlib import Path

import httpx

from .. import config

REST = "https://rest.runpod.io/v1"
# S3 endpoints are per datacenter: https://s3api-<dc>.runpod.io (lower-case id; the region is the upper-case id).
# Not every datacenter offers the S3 API; the settings page lists the ones that do.
S3_FMT = "https://s3api-{dc}.runpod.io"

S3_DATACENTERS = ["EU-CZ-1", "EU-RO-1", "EUR-IS-1", "EUR-NO-1", "US-CA-2", "US-GA-2", "US-IL-1", "US-KS-2",
                  "US-MD-1", "US-MO-1", "US-MO-2", "US-NC-1", "US-NC-2", "US-NE-1", "US-WA-1"]

GPUS = {  # Secure Cloud on-demand prices from runpod.io/pricing (updated 2026-09-27); network volumes need Secure Cloud
    "NVIDIA H100 80GB HBM3": {"label": "H100 SXM 80GB", "vram": 80, "usd_h": 3.49},
    "NVIDIA H100 PCIe": {"label": "H100 PCIe 80GB", "vram": 80, "usd_h": 2.89},
    "NVIDIA A100-SXM4-80GB": {"label": "A100 SXM 80GB", "vram": 80, "usd_h": 1.59},
    "NVIDIA A100 80GB PCIe": {"label": "A100 PCIe 80GB", "vram": 80, "usd_h": 1.59},
    "NVIDIA L40S": {"label": "L40S 48GB", "vram": 48, "usd_h": 1.09},
    "NVIDIA RTX 6000 Ada Generation": {"label": "RTX 6000 Ada 48GB", "vram": 48, "usd_h": 0.84},
    "NVIDIA GeForce RTX 5090": {"label": "RTX 5090 32GB", "vram": 32, "usd_h": 0.99},
    "NVIDIA GeForce RTX 4090": {"label": "RTX 4090 24GB", "vram": 24, "usd_h": 0.74},
}


class RunPodError(Exception):
    pass


def _key() -> str:
    k = config.get_secret("runpod_api_key")
    if not k:
        raise RunPodError("尚未設定 RunPod API 金鑰（設定 → 雲端）。")
    return k


def _h() -> dict:
    return {"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"}


def _req(method: str, path: str, **kw):
    with httpx.Client(timeout=60) as c:
        r = c.request(method, REST + path, headers=_h(), **kw)
    if r.status_code >= 400:
        raise RunPodError(f"RunPod {method} {path}: {r.status_code} {r.text[:300]}")
    return r.json() if r.content else {}


def check() -> dict:
    """Verify the API key and the volume; returns the volume's datacenter and size."""
    st = config.load_settings()
    vols = _req("GET", "/networkvolumes")
    vols = vols if isinstance(vols, list) else vols.get("data", vols)
    out = {"ok": True, "volumes": [{"id": v.get("id"), "name": v.get("name"), "dataCenterId": v.get("dataCenterId"),
                                    "size": v.get("size")} for v in vols]}
    vid = st.get("runpod_volume_id")
    if vid:
        match = [v for v in out["volumes"] if v["id"] == vid]
        out["volume"] = match[0] if match else None
    return out


def create_pod(name: str, image: str, gpu_types: list[str], env: dict, start_cmd: list[str],
               container_disk_gb: int = 80) -> dict:
    st = config.load_settings()
    vol, dc = st.get("runpod_volume_id"), st.get("runpod_datacenter")
    if not vol or not dc:
        raise RunPodError("請先在設定裡填網路磁碟（Network Volume）ID 和它的資料中心。")
    body = {"name": name[:180], "imageName": image, "gpuTypeIds": gpu_types, "gpuCount": 1,
            "cloudType": st.get("runpod_cloud_type") or "SECURE", "networkVolumeId": vol, "dataCenterIds": [dc],
            "volumeMountPath": "/workspace", "containerDiskInGb": container_disk_gb, "env": env,
            "dockerStartCmd": start_cmd, "ports": ["22/tcp"]}
    return _req("POST", "/pods", json=body)


def get_pod(pod_id: str) -> dict | None:
    try:
        return _req("GET", f"/pods/{pod_id}")
    except RunPodError as e:
        if " 404 " in str(e):
            return None
        raise


def remove_pod(pod_id: str) -> None:
    try:
        _req("DELETE", f"/pods/{pod_id}")
    except RunPodError as e:
        if " 404 " not in str(e):
            raise


def gpu_catalog(datacenter: str | None = None) -> list[dict]:
    """Live GPU prices and stock for pods (api.runpod.io/v2/catalog/gpus); falls back to the static table."""
    st = config.load_settings()
    cloud = st.get("runpod_cloud_type") or "SECURE"
    try:
        with httpx.Client(timeout=30) as c:
            r = c.get("https://api.runpod.io/v2/catalog/gpus", headers=_h(),
                      params={"include": "AVAILABILITY", "product": "POD", "cloud": cloud})
        r.raise_for_status()
        out = []
        for g in r.json().get("gpus", []):
            dcs = {d["id"]: d.get("availability") for d in g.get("dataCenters", [])}
            if datacenter and datacenter not in dcs:
                continue
            price = (g.get("price") or {}).get("secure" if cloud == "SECURE" else "community")
            out.append({"id": g["id"], "label": g.get("name") or g["id"], "vram": g.get("memory"), "usd_h": price,
                        "availability": dcs.get(datacenter) if datacenter else g.get("availability")})
        return sorted(out, key=lambda x: (x["usd_h"] is None, x["usd_h"] or 0))
    except Exception:
        return [{"id": k, **v, "availability": None} for k, v in GPUS.items()]


# --- S3 (network volume) ----------------------------------------------------------------------------------------

def s3():
    import boto3
    from botocore.config import Config
    st = config.load_settings()
    ak, sk = config.get_secret("runpod_s3_access_key"), config.get_secret("runpod_s3_secret_key")
    if not ak or not sk:
        raise RunPodError("尚未設定 RunPod S3 金鑰（設定 → 雲端）。")
    dc = (st.get("runpod_datacenter") or "").strip()
    return boto3.client("s3", aws_access_key_id=ak, aws_secret_access_key=sk, region_name=dc.upper(),
                        endpoint_url=S3_FMT.format(dc=dc.lower()),
                        config=Config(signature_version="s3v4", retries={"max_attempts": 8, "mode": "adaptive"},
                                      s3={"addressing_style": "path"}))


def bucket() -> str:
    return config.load_settings()["runpod_volume_id"]


def upload(local: Path, key: str, progress=None) -> None:
    from boto3.s3.transfer import TransferConfig
    size = local.stat().st_size
    done = [0]

    def cb(n):
        done[0] += n
        if progress:
            progress(done[0] / max(1, size))
    s3().upload_file(str(local), bucket(), key, Callback=cb,
                     Config=TransferConfig(multipart_chunksize=64 << 20, max_concurrency=4))


def put_text(key: str, text: str) -> None:
    s3().put_object(Bucket=bucket(), Key=key, Body=text.encode("utf-8"))


def get_json(key: str) -> dict | None:
    try:
        obj = s3().get_object(Bucket=bucket(), Key=key)
        return json.loads(obj["Body"].read().decode("utf-8"))
    except Exception:
        return None


def get_text(key: str, tail: int = 20000) -> str:
    try:
        obj = s3().get_object(Bucket=bucket(), Key=key)
        return obj["Body"].read().decode("utf-8", "replace")[-tail:]
    except Exception:
        return ""


def download(key: str, local: Path, progress=None) -> Path:
    c = s3()
    size = c.head_object(Bucket=bucket(), Key=key)["ContentLength"]
    done = [0]

    def cb(n):
        done[0] += n
        if progress:
            progress(done[0] / max(1, size))
    local.parent.mkdir(parents=True, exist_ok=True)
    c.download_file(bucket(), key, str(local), Callback=cb)
    return local


def delete_prefix(prefix: str) -> int:
    c = s3()
    n = 0
    token = None
    while True:
        kw = {"Bucket": bucket(), "Prefix": prefix}
        if token:
            kw["ContinuationToken"] = token
        r = c.list_objects_v2(**kw)
        for o in r.get("Contents", []):
            c.delete_object(Bucket=bucket(), Key=o["Key"])
            n += 1
        if not r.get("IsTruncated"):
            return n
        token = r.get("NextContinuationToken")

```

### `vstudio/server.py`

```python
"""The web app: API under /api, the built web UI everywhere else."""
from __future__ import annotations

import ipaddress
import os
import secrets as _secrets
import webbrowser
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse

from . import __version__, config, db, evaluate, jobs, training, tts  # noqa: F401  (modules register job handlers)
from .api import data, docs, speak, system, train, voices
from .engines import install  # noqa: F401  (registers install_engine)
from .pipeline import prepare  # noqa: F401  (registers prepare_source / enroll_voice)

WEB = config.ROOT / "web" / "dist"


def create_app() -> FastAPI:
    config.ensure_dirs()
    db.connect()

    @asynccontextmanager
    async def lifespan(_app):
        jobs.start()
        try:
            training.resume_interrupted()
        except Exception:  # never block start-up on the cloud
            pass
        yield
        jobs.stop()

    app = FastAPI(title="Voice Studio", version=__version__, lifespan=lifespan)
    for r in (voices.router, data.router, train.router, speak.router, system.router, docs.router):
        app.include_router(r)

    password = os.environ.get("VSTUDIO_PASSWORD", "")

    @app.middleware("http")
    async def guard(request: Request, call_next):
        """Loopback is trusted. Any other client needs VSTUDIO_PASSWORD (when the studio is opened to a network)."""
        host = request.client.host if request.client else "127.0.0.1"
        try:
            local = ipaddress.ip_address(host).is_loopback
        except ValueError:
            local = host in ("localhost", "testclient")
        if not local:
            given = request.headers.get("x-studio-password") or request.cookies.get("studio_pw") or ""
            if not password or not _secrets.compare_digest(given, password):
                return JSONResponse({"detail": "需要密碼"}, status_code=401)
        return await call_next(request)

    @app.get("/api/health")
    def health():
        return {"ok": True, "version": __version__}

    @app.get("/{full_path:path}")
    def spa(full_path: str):
        if full_path.startswith("api/"):
            return JSONResponse({"detail": "Not Found"}, status_code=404)
        f = (WEB / full_path).resolve()
        if full_path and f.is_file() and WEB.resolve() in f.parents:
            return FileResponse(f)
        index = WEB / "index.html"
        if index.exists():
            return FileResponse(index)
        return JSONResponse({"detail": "web UI not built: run `npm run build` in web/"}, status_code=404)

    return app


app = create_app()


def main() -> None:
    import uvicorn
    st = config.load_settings()
    host, port = os.environ.get("VSTUDIO_HOST", st["host"]), int(os.environ.get("VSTUDIO_PORT", st["port"]))
    if os.environ.get("VSTUDIO_NO_BROWSER") != "1":
        import threading
        threading.Timer(1.5, lambda: webbrowser.open(f"http://127.0.0.1:{port}")).start()
    uvicorn.run(app, host=host, port=port, log_level="warning")


if __name__ == "__main__":
    main()

```

### `vstudio/config.py`

```python
"""Paths, settings and secrets.

Settings that are not secret live in data/settings.json. Secrets (API keys) live in the operating system's credential
store through `keyring` (Windows Credential Manager on Windows), so they never sit in a plain file, a log or git.
"""
from __future__ import annotations

import json
import os
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(os.environ.get("VSTUDIO_DATA", ROOT / "data")).resolve()
KEYRING_SERVICE = "voice-studio"
# model downloads (Hugging Face) are kept with the studio's data, not in the user profile
os.environ.setdefault("HF_HOME", str(DATA / "hf"))
SECRET_NAMES = ("runpod_api_key", "runpod_s3_access_key", "runpod_s3_secret_key", "hf_token")

DEFAULTS = {
    "language_ui": "zh-TW",
    "host": "127.0.0.1",
    "port": 7860,
    # data preparation
    "asr_primary": "large-v3",
    "asr_secondary": "large-v3-turbo",
    "asr_device": "auto",
    "segment_min_s": 2.0,
    "segment_max_s": 15.0,
    "segment_target_s": 8.0,
    "separate_vocals": False,
    "speaker_match_threshold": 0.62,
    # cloud
    "runpod_volume_id": "",
    "runpod_datacenter": "",
    "runpod_cloud_type": "SECURE",
    "runpod_max_hours": 12.0,
    # engine
    "default_engine": "voxcpm2",
    "speed": {},          # measured seconds per training step, per engine:preset:gpu (filled in after runs)
}

_lock = threading.Lock()


def path(*parts: str) -> Path:
    p = DATA.joinpath(*parts)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def ensure_dirs() -> None:
    for d in ("sources", "segments", "voices", "datasets", "models", "outputs", "jobs", "presets", "tmp"):
        (DATA / d).mkdir(parents=True, exist_ok=True)


def load_settings() -> dict:
    f = DATA / "settings.json"
    data = dict(DEFAULTS)
    if f.exists():
        try:
            data.update(json.loads(f.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            pass
    return data


def save_settings(update: dict) -> dict:
    with _lock:
        data = load_settings()
        for k, v in update.items():
            if k in DEFAULTS:
                data[k] = v
        f = DATA / "settings.json"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return data


# --- secrets -----------------------------------------------------------------------------------------------------

def _keyring():
    try:
        import keyring
        keyring.get_keyring()
        return keyring
    except Exception:  # no usable backend (headless Linux test boxes)
        return None


def get_secret(name: str) -> str | None:
    if name not in SECRET_NAMES:
        raise KeyError(name)
    env = os.environ.get("VSTUDIO_" + name.upper())
    if env:
        return env
    kr = _keyring()
    if kr is None:
        return None
    try:
        return kr.get_password(KEYRING_SERVICE, name)
    except Exception:
        return None


def set_secret(name: str, value: str | None) -> bool:
    if name not in SECRET_NAMES:
        raise KeyError(name)
    kr = _keyring()
    if kr is None:
        return False
    try:
        if value:
            kr.set_password(KEYRING_SERVICE, name, value)
        else:
            try:
                kr.delete_password(KEYRING_SERVICE, name)
            except Exception:
                pass
        return True
    except Exception:
        return False


def secret_status() -> dict:
    """Which secrets are set, never their values."""
    return {n: bool(get_secret(n)) for n in SECRET_NAMES}

```

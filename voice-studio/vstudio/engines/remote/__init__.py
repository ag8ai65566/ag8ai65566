"""Files the engines upload next to bootstrap.sh for a cloud training run."""
from __future__ import annotations

import hashlib
from pathlib import Path

HERE = Path(__file__).parent

SETUP_TEMPLATE = r"""#!/bin/bash
# Installs the {name} training environment on the network volume. It runs at the start of every training run but
# installs only once per pinned version: later runs find the stamp file and skip straight to training.
set -euo pipefail
ENV="${{VS_ROOT:-/workspace/vs}}/envs/{engine}"
SRC="${{VS_ROOT:-/workspace/vs}}/src/{engine}"
# the stamp names the exact recipe (this script), the image's Python/torch build and the upstream commit
STAMP="$ENV/.ready-{recipe}-$(python3 -c 'import sys,torch;print(f"py{{sys.version_info[0]}}{{sys.version_info[1]}}-torch{{torch.__version__}}")' 2>/dev/null)"

# system packages live on the container disk, so they are checked on every run (fast when present)
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v sox >/dev/null 2>&1; then
  apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg sox >/dev/null
fi

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
# smoke test in a fresh interpreter: the public model class imports and audio decodes
python - <<'PY'
import numpy as np, soundfile as sf, librosa
from {module} import {cls}
sf.write("/tmp/vs_probe.wav", np.zeros(16000, dtype="float32"), 16000)
y, sr = librosa.load("/tmp/vs_probe.wav", sr=24000)
assert len(y) == 24000, len(y)
print("[vs] {module}.{cls} import and audio decode ok")
PY
touch "$STAMP"
"""


def setup_script(engine: str, name: str, repo: str, commit: str, version: str, module: str, cls: str,
                 extra_pip: str = "", post: str = "") -> str:
    fields = dict(engine=engine, name=name, repo=repo, commit=commit, version=version, module=module, cls=cls,
                  extra_pip=extra_pip, post=post)
    recipe = hashlib.sha256(SETUP_TEMPLATE.format(recipe="", **fields).encode()).hexdigest()[:12]
    return SETUP_TEMPLATE.format(recipe=recipe, **fields)


def read(name: str) -> str:
    return (HERE / name).read_text(encoding="utf-8")

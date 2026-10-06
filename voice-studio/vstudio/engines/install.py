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

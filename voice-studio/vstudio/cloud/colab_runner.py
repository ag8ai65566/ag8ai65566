"""Voice Studio on Google Colab: trains one run that Voice Studio prepared in a Google Drive folder.

Voice Studio (on your computer) writes each run to <Drive>/<folder>/jobs/<training id>/ through Google Drive for
desktop: config.json, the engine's setup and training scripts, dataset.tar and job.json. The notebook mounts Drive
and calls main(); this file then does on Colab what bootstrap.sh does on a RunPod pod:

- pick the newest run that is waiting (or the one asked for), and mark it as taken (claim.json, heartbeat.json);
- wait until dataset.tar has finished syncing, copy it once to the Colab disk and unpack it there (reading many small
  files from Drive is slow; one archive is fast);
- install the engine environment on the Colab disk, train, and let the engine script write progress.json, model.tar
  (weights, as soon as they are final) and samples.tar straight into the run folder on Drive;
- write done.json or error.json, stop if Voice Studio asks (cancel.json) or the time limit passes, and finally
  disconnect the runtime so it stops using compute units.

Voice Studio watches the same folder on your computer and installs the model when it arrives.
"""
from __future__ import annotations

import json
import os
import shutil
import signal
import subprocess
import sys
import tarfile
import threading
import time
from pathlib import Path

LOCAL = Path(os.environ.get("VS_COLAB_LOCAL", "/content"))  # the Colab VM's own disk (fast, erased at disconnect)
STALE_CLAIM_S = 600       # a taken run whose heartbeat is older than this was abandoned (the runtime disconnected)


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _read(p: Path) -> dict | None:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def _put(d: Path, name: str, data: dict) -> None:
    """Write a status file atomically, so the studio never reads half of it."""
    tmp = d / f"{name}.tmp"
    tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, d / name)


def _gpu() -> tuple[str, float]:
    try:
        out = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=30).stdout.strip().splitlines()[0]
        name, mem = [x.strip() for x in out.split(",")]
        return name, float(mem) / 1024
    except Exception:
        return "", 0.0


def _pick(jobs_dir: Path, want: str | None) -> Path | None:
    if want:
        d = jobs_dir / want
        return d if (d / "job.json").exists() else None
    ready = []
    for d in jobs_dir.iterdir() if jobs_dir.exists() else []:
        job = _read(d / "job.json")
        if not job or any((d / f).exists() for f in ("done.json", "error.json", "cancel.json")):
            continue
        hb = _read(d / "heartbeat.json") or {}
        if (d / "claim.json").exists() and time.time() - float(hb.get("t", 0)) < STALE_CLAIM_S:
            continue  # another runtime is working on it
        ready.append((float(job.get("created", 0)), d))
    return max(ready)[1] if ready else None


class Run:
    def __init__(self, d: Path, job: dict) -> None:
        self.d, self.job = d, job
        self.proc: subprocess.Popen | None = None
        self.cancelled = threading.Event()
        self.timed_out = threading.Event()
        self.stop = threading.Event()
        self.stage = "start"
        self.log = open(d / "train.log", "a", encoding="utf-8")

    def say(self, msg: str) -> None:
        line = f"[vs] {msg}"
        print(line, flush=True)
        self.log.write(line + "\n")
        self.log.flush()

    def watch(self) -> None:
        """Heartbeat for the studio; stop the work when it asks or when the time limit passes."""
        t0, limit = time.time(), float(self.job.get("max_seconds") or 11.5 * 3600)
        while not self.stop.wait(30):
            try:
                _put(self.d, "heartbeat.json", {"t": time.time(), "stage": self.stage, "at": _now()})
            except Exception:
                pass
            if (self.d / "cancel.json").exists():
                self.cancelled.set()
            if time.time() - t0 > limit:
                self.timed_out.set()
            if (self.cancelled.is_set() or self.timed_out.is_set()) and self.proc and self.proc.poll() is None:
                self.say("stopping: " + ("cancelled in Voice Studio" if self.cancelled.is_set() else "time limit"))
                try:
                    os.killpg(self.proc.pid, signal.SIGTERM)
                    time.sleep(5)
                    os.killpg(self.proc.pid, signal.SIGKILL)
                except Exception:
                    pass

    def sh(self, cmd: list[str], env: dict) -> int:
        """Run a step in its own process group; its output goes to the notebook and to train.log on Drive."""
        self.proc = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                     errors="replace", bufsize=1, start_new_session=True)
        last = time.time()
        assert self.proc.stdout is not None
        for line in self.proc.stdout:
            sys.stdout.write(line)
            self.log.write(line)
            if time.time() - last > 5:
                self.log.flush()
                last = time.time()
        self.log.flush()
        return self.proc.wait()


def main(folder: str = "VoiceStudio", job: str | None = None, auto_disconnect: bool = True,
         drive_root: str = "/content/drive/MyDrive") -> None:
    root = Path(drive_root) / folder
    d = _pick(root / "jobs", job)
    if d is None:
        print(f"在 {root / 'jobs'} 找不到等待中的訓練。請先在 Voice Studio 的「雲端訓練」選 Colab 並按開始，"
              "等它顯示「等你在 Colab 執行」，而且雲端硬碟同步完成後再執行。")
        return
    spec = _read(d / "job.json") or {}
    run = Run(d, spec)
    gpu, vram = _gpu()
    run.say(f"run {d.name}: engine {spec.get('engine')} / {spec.get('preset')}, GPU {gpu or 'none'} ({vram:.0f} GB)")
    need = float(spec.get("min_vram_gb") or 0)
    if need and vram < need:
        msg = (f"這個訓練需要至少 {need:.0f} GB 顯示記憶體，這個執行階段是 {gpu or '沒有 GPU'}（{vram:.0f} GB）。"
               "請到「執行階段 → 變更執行階段類型」選 A100（或 L4 等更大的 GPU）後再執行一次。")
        print(msg)
        run.say(msg)
        return  # nothing claimed: the run stays waiting for a bigger GPU
    _put(d, "claim.json", {"at": _now(), "t": time.time(), "gpu": gpu, "vram_gb": round(vram, 1)})
    _put(d, "heartbeat.json", {"t": time.time(), "stage": "start", "at": _now()})
    watcher = threading.Thread(target=run.watch, daemon=True)
    watcher.start()

    vs_root, work, data = LOCAL / "vs", LOCAL / "vswork", LOCAL / "vsdata"
    engine = str(spec.get("engine"))
    # the same environment bootstrap.sh gives a RunPod pod, with everything on the Colab disk
    env = {**os.environ, "VS_ROOT": str(vs_root), "HF_HOME": str(vs_root / "hf"), "VS_WORK": str(work),
           "VS_SRC": str(vs_root / "src" / engine), "VS_ENGINE": engine, "VS_IMAGE": "colab",
           "VS_TRAINING_ID": d.name, "PYTHONUNBUFFERED": "1"}
    rc = 1
    try:
        # 1. wait until Google Drive has the whole dataset (it may still be uploading from the studio's computer)
        run.stage = "sync"
        want = int((spec.get("sizes") or {}).get("dataset.tar") or 0)
        tar = d / "dataset.tar"
        t0 = time.time()
        while not (tar.exists() and (not want or tar.stat().st_size == want)):
            if run.cancelled.is_set() or time.time() - t0 > 3 * 3600:
                raise RuntimeError("cancelled" if run.cancelled.is_set() else "dataset.tar never finished syncing")
            have = tar.stat().st_size if tar.exists() else 0
            run.say(f"waiting for Google Drive to sync dataset.tar: {have / 1e9:.2f} / {want / 1e9:.2f} GB")
            time.sleep(30)

        # 2. environment (installed on the Colab disk; a new runtime installs it again, about 5–10 minutes)
        run.stage = "setup"
        _put(d, "progress.json", {"phase": "setup"})
        if run.sh(["bash", str(d / "setup_env.sh")], env) != 0:
            raise RuntimeError("setup")

        # 3. one archive copied from Drive and unpacked on the local disk
        run.stage = "unpack"
        _put(d, "progress.json", {"phase": "unpack"})
        local_tar = LOCAL / "vs_dataset.tar"
        shutil.copyfile(tar, local_tar)
        shutil.rmtree(data, ignore_errors=True)
        data.mkdir(parents=True)
        with tarfile.open(local_tar) as t:
            t.extractall(data, filter="data")
        local_tar.unlink(missing_ok=True)

        # 4. train; the engine script writes progress.json, model.tar and samples.tar into the run folder on Drive
        run.stage = "train"
        py = vs_root / "envs" / engine / "bin" / "python"
        rc = run.sh([str(py), str(d / "train_entry.py"), "--config", str(d / "config.json"), "--data", str(data)], env)
    except Exception as e:
        run.say(f"stopped in {run.stage}: {e}")
    finally:
        run.stop.set()
        sizes = {n: (d / n).stat().st_size for n in ("model.tar", "samples.tar") if (d / n).exists()}
        if "model.tar" in sizes:  # weights are published before the optional samples, so a late failure keeps them
            _put(d, "done.json", {"status": "done", "rc": rc, "samples": "samples.tar" in sizes, "sizes": sizes,
                                  "gpu": gpu, "at": _now()})
            run.say("finished: the model is in Google Drive; Voice Studio installs it when it has synced")
        else:
            status = "cancelled" if run.cancelled.is_set() else "timeout" if run.timed_out.is_set() else "error"
            _put(d, "error.json", {"status": status, "stage": run.stage, "at": _now()})
            run.say(f"failed ({status}) in {run.stage}")
        run.log.close()
        if auto_disconnect and Path("/content").exists():
            try:
                from google.colab import runtime  # type: ignore
                print("完成，自動斷線以停止使用運算單位。")
                runtime.unassign()
            except Exception:
                pass


if __name__ == "__main__":
    main(*sys.argv[1:2])

"""Training on Google Colab with the compute units of a Google AI plan.

There is no API to start a Colab runtime, so the exchange goes through a Google Drive folder that Google Drive for
desktop keeps in sync on this computer:

    <My Drive>/<folder>/VoiceStudio-Colab.ipynb   the notebook the person runs (one cell)
    <My Drive>/<folder>/colab_runner.py           what the notebook calls (same version as this studio)
    <My Drive>/<folder>/jobs/<training id>/        one run: config, scripts, dataset.tar, job.json …

The studio writes the run, the person opens the notebook in Colab and runs it, and the runner (colab_runner.py)
trains and writes progress.json / model.tar / samples.tar / done.json back into the run folder. A poller here reads
those files as they sync down and installs the model exactly like a RunPod run.
"""
from __future__ import annotations

import json
import os
import shutil
import string
import tarfile
import time
from pathlib import Path

from .. import config, db, jobs

RUNNER = (Path(__file__).parent / "colab_runner.py").read_text(encoding="utf-8")
NOTEBOOK_NAME = "VoiceStudio-Colab.ipynb"
STALE_S = 20 * 60          # a running run without a heartbeat for this long is treated as disconnected
# rough Colab compute units per hour (third-party measurements; Google publishes none): A100 40 GB ≈ 5.4,
# A100 80 GB ≈ 7.5, other reports up to ≈ 15
CU_PER_HOUR = (5.0, 15.0)
# GPU memory a run needs; the runner refuses a smaller runtime instead of failing after the install
MIN_VRAM_GB = {("voxcpm2", "lora"): 20, ("voxcpm2", "full"): 40, ("qwen3", "sft"): 40, ("mock", "quick"): 0}


class ColabError(Exception):
    pass


# --- where the shared folder is ----------------------------------------------------------------------------------

def detect_roots() -> list[str]:
    """Folders that look like the root of "My Drive" as Google Drive for desktop shows it on Windows (a virtual
    drive such as G:\\My Drive in streaming mode, or a folder in the user profile in mirroring mode)."""
    names = ("My Drive", "我的雲端硬碟", "我的云端硬盘", "マイドライブ")
    cands: list[Path] = []
    if os.name == "nt":
        cands += [Path(f"{L}:\\") / n for L in string.ascii_uppercase[3:] for n in names]
    home = Path.home()
    cands += [home / n for n in names] + [home / "Google Drive" / n for n in names] + [home / "Google Drive"]
    out = []
    for c in cands:
        try:
            if c.is_dir() and str(c) not in out:
                out.append(str(c))
        except OSError:
            continue
    return out


def folder(st: dict | None = None) -> Path:
    st = st or config.load_settings()
    root = (st.get("colab_drive_root") or "").strip()
    if not root:
        raise ColabError("還沒設定 Google 雲端硬碟資料夾：到「設定 → Google Colab」選擇。")
    r = Path(root)
    if not r.is_dir():
        raise ColabError(f"找不到雲端硬碟資料夾 {r}。Google 雲端硬碟電腦版有沒有開著？")
    return r / (st.get("colab_folder") or "VoiceStudio")


def install_files(st: dict | None = None) -> Path:
    """Write (or refresh) the notebook and the runner into the shared folder."""
    f = folder(st)
    (f / "jobs").mkdir(parents=True, exist_ok=True)
    _write(f / "colab_runner.py", RUNNER)
    _write(f / NOTEBOOK_NAME, json.dumps(notebook((st or config.load_settings()).get("colab_folder") or "VoiceStudio"),
                                         ensure_ascii=False, indent=1))
    return f


def status() -> dict:
    st = config.load_settings()
    out = {"drive_root": st.get("colab_drive_root") or "", "folder": st.get("colab_folder") or "VoiceStudio",
           "detected": detect_roots(), "ok": False, "notebook": False, "error": ""}
    try:
        f = folder(st)
        out.update(ok=True, path=str(f), notebook=(f / NOTEBOOK_NAME).exists())
    except ColabError as e:
        out["error"] = str(e)
    return out


def _write(p: Path, text: str) -> None:
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, p)


def notebook(folder_name: str) -> dict:
    """One code cell: mount Drive, run the newest waiting run, disconnect at the end. A100 is requested in the
    notebook's metadata; Colab offers it when the plan and availability allow."""
    intro = (
        "# Voice Studio：在 Colab 訓練\n\n"
        "1. 上方選單「執行階段 → 變更執行階段類型」選 **A100**（沒有的話選 L4）。\n"
        "2. 按下面那一格左邊的 ▶。第一次會要你允許存取 Google 雲端硬碟，請選**和電腦上同步的同一個帳號**。\n"
        "3. 訓練時這個分頁要開著、電腦不要睡眠（Google AI Pro 沒有背景執行）。完成後會自動斷線，停止使用運算單位。\n\n"
        "結果會寫回雲端硬碟，Voice Studio 會在你的電腦上自動安裝模型。\n\n"
        "注意：Colab 的使用規則禁止製作深偽內容。這裡只訓練有同意紀錄的聲音。")
    code = (
        "#@title Voice Studio 訓練（按左邊的 ▶ 執行）\n"
        f"FOLDER = \"{folder_name}\"  #@param {{type:\"string\"}}\n"
        "JOB = \"\"  #@param {type:\"string\"}\n"
        "AUTO_DISCONNECT = True  #@param {type:\"boolean\"}\n"
        "# FOLDER：雲端硬碟裡 Voice Studio 的資料夾；JOB：留空＝最新一個等待中的訓練；AUTO_DISCONNECT：完成後自動斷線\n"
        "from google.colab import drive\n"
        "drive.mount(\"/content/drive\")\n"
        "import runpy\n"
        "runner = runpy.run_path(f\"/content/drive/MyDrive/{FOLDER}/colab_runner.py\")\n"
        "runner[\"main\"](folder=FOLDER, job=JOB.strip() or None, auto_disconnect=AUTO_DISCONNECT)\n")
    lines = lambda s: [ln + "\n" for ln in s.split("\n")][:-1] + [s.split("\n")[-1]]  # noqa: E731
    return {"nbformat": 4, "nbformat_minor": 0,
            "metadata": {"accelerator": "GPU", "colab": {"provenance": [], "gpuType": "A100"},
                         "kernelspec": {"name": "python3", "display_name": "Python 3"},
                         "language_info": {"name": "python"}},
            "cells": [{"cell_type": "markdown", "metadata": {}, "source": lines(intro)},
                      {"cell_type": "code", "metadata": {"cellView": "form"}, "execution_count": None,
                       "outputs": [], "source": lines(code)}]}


def job_dir(tr: dict) -> Path:
    s = tr.get("storage") or {}
    return Path(s["drive_root"]) / s["folder"] / "jobs" / tr["id"]


def read_json(p: Path) -> dict | None:
    """None while a file is missing, still syncing or half-written."""
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


# --- preparing a run ----------------------------------------------------------------------------------------------

@jobs.handler("colab_prepare", queue="io")
def colab_prepare(ctx: jobs.JobContext) -> dict:
    from .. import engines, training
    tid = ctx.params["training_id"]
    tr = db.get("trainings", tid)
    try:
        eng = engines.get(tr["engine"])
        d = job_dir(tr)
        work = config.DATA / "jobs" / tid
        work.mkdir(parents=True, exist_ok=True)
        training._require_consent(tr["voice_id"])
        training._set(tid, status="uploading")
        install_files()
        ctx.progress(0.02, "整理訓練資料")
        tar_path, cfg = training.package_dataset(tid, work)
        training._check_reference(tr, eng)
        training._require_consent(tr["voice_id"])
        d.mkdir(parents=True, exist_ok=True)
        _write(d / "config.json", json.dumps(cfg, ensure_ascii=False, indent=2))
        for name, text in eng.cloud_files().items():
            _write(d / name, text)
        size = tar_path.stat().st_size
        part = d / "dataset.tar.part"
        with open(tar_path, "rb") as src, open(part, "wb") as dst:
            done = 0
            while chunk := src.read(16 << 20):
                dst.write(chunk)
                done += len(chunk)
                ctx.check()
                ctx.progress(0.05 + 0.9 * done / max(1, size), f"放進雲端硬碟資料夾 {done * 100 // max(1, size)}%")
        os.replace(part, d / "dataset.tar")
        tar_path.unlink(missing_ok=True)
        max_h = min(11.5, float(config.load_settings().get("runpod_max_hours") or 11.5))
        # job.json last: the runner treats a run as ready only once it exists
        _write(d / "job.json", json.dumps({
            "training_id": tid, "engine": eng.id, "preset": tr["preset"]["id"], "created": time.time(),
            "sizes": {"dataset.tar": size}, "max_seconds": int(max_h * 3600),
            "min_vram_gb": MIN_VRAM_GB.get((eng.id, tr["preset"]["id"]), 24)}, ensure_ascii=False, indent=2))
        training._set(tid, status="waiting", note="")
        return {"message": "已放進雲端硬碟。等同步完成後，到 Colab 打開 VoiceStudio-Colab.ipynb 執行。"}
    except BaseException as e:
        cur = db.get("trainings", tid)
        if cur and cur["status"] not in ("done", "failed", "canceled"):
            training._set(tid, status="canceled" if isinstance(e, jobs.Cancelled) else "failed",
                          finished_at=db.now(), note=f"準備 Colab 訓練失敗：{str(e)[:200]}")
        raise


# --- watching and installing --------------------------------------------------------------------------------------

def poll() -> None:
    """Read the status files of every Colab run that is waiting or running (called every ~20 s)."""
    from .. import training
    for tr in db.query("SELECT * FROM trainings WHERE target='colab' AND status IN ('waiting','running')"):
        try:
            _poll_one(tr, training)
        except Exception:  # a half-synced file or a missing drive must never stop the poller
            continue


def _poll_one(tr: dict, training) -> None:
    d = job_dir(tr)
    if not d.exists():
        return
    tid = tr["id"]
    claim, hb = read_json(d / "claim.json"), read_json(d / "heartbeat.json")
    prog, done, err = read_json(d / "progress.json"), read_json(d / "done.json"), read_json(d / "error.json")
    upd: dict = {}
    if claim and tr["status"] == "waiting":
        upd.update(status="running", started_at=tr.get("started_at") or time.time(), note="")
    if prog or claim:
        started = upd.get("started_at") or tr.get("started_at") or time.time()
        upd["progress"] = {**(tr.get("progress") or {}), **(prog or {}), "gpu_name": (claim or {}).get("gpu"),
                           "wall_s": int(time.time() - started)}
    if done or (err and (d / "model.tar").exists()):
        upd["status"] = "downloading"
        training._set(tid, **upd)
        job = jobs.submit("colab_install", {"training_id": tid, "partial": not done or done.get("rc", 0) != 0},
                          "從雲端硬碟取回模型")
        training._set(tid, job_id=job["id"])
        return
    if err:
        if err.get("status") == "cancelled":
            upd.update(status="canceled", finished_at=db.now())
        else:
            upd.update(status="failed", finished_at=db.now(),
                       note=f"Colab 訓練失敗（{training._stage_label(err)}）。按「紀錄」看 Colab 的輸出。")
        _copy_log(tid, d)
    elif claim and hb and time.time() - float(hb.get("t", 0)) > STALE_S:
        # the runtime went away (closed tab, idle timeout, 12-hour limit): the run can be started again
        upd.update(status="waiting", note="Colab 好像斷線了（超過 20 分鐘沒有回應）。再執行一次筆記本會從頭重新訓練。")
        for f in ("claim.json", "heartbeat.json", "progress.json"):
            (d / f).unlink(missing_ok=True)
    if upd:
        training._set(tid, **upd)


def _copy_log(tid: str, d: Path) -> None:
    try:
        work = config.DATA / "jobs" / tid
        work.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(d / "train.log", work / "train.log")
    except Exception:
        pass


def _wait_synced(ctx: jobs.JobContext, f: Path, size: int | None, what: str, limit_s: float) -> bool:
    """Wait until Google Drive for desktop has brought the whole file down (its size matches what Colab wrote)."""
    t0 = time.time()
    while time.time() - t0 < limit_s:
        ctx.check()
        have = f.stat().st_size if f.exists() else 0
        if f.exists() and (size is None or have == size):
            return True
        ctx.progress(0.1, f"等雲端硬碟同步{what}到這台電腦（{have / 1e6:.0f} / {(size or 0) / 1e6:.0f} MB）")
        time.sleep(15)
    return False


def _fetch(ctx: jobs.JobContext, src: Path, dst: Path, size: int | None, lo: float, hi: float, label: str) -> Path:
    """Copy a synced archive to the studio's own folder (reading it makes Drive download it) and check it opens."""
    total = size or src.stat().st_size
    done = 0
    with open(src, "rb") as a, open(dst, "wb") as b:
        while chunk := a.read(16 << 20):
            b.write(chunk)
            done += len(chunk)
            ctx.progress(lo + (hi - lo) * done / max(1, total), f"{label} {done * 100 // max(1, total)}%")
    with tarfile.open(dst) as t:
        t.getmembers()
    return dst


@jobs.handler("colab_install", queue="io")
def colab_install(ctx: jobs.JobContext) -> dict:
    from .. import training
    tid = ctx.params["training_id"]
    tr = db.get("trainings", tid)
    d = job_dir(tr)
    work = config.DATA / "jobs" / tid
    work.mkdir(parents=True, exist_ok=True)
    done = read_json(d / "done.json") or {}
    sizes = done.get("sizes") or {}
    try:
        if not _wait_synced(ctx, d / "model.tar", sizes.get("model.tar"), "模型", 3 * 3600):
            raise RuntimeError("等了 3 小時，模型還沒從雲端硬碟同步到這台電腦。確認 Google 雲端硬碟電腦版有開著，再按「救回模型」。")
        model = _fetch(ctx, d / "model.tar", work / "model.tar", sizes.get("model.tar"), 0.2, 0.8, "取回模型")
        samples = None
        if done.get("samples") and _wait_synced(ctx, d / "samples.tar", sizes.get("samples.tar"), "樣本", 1800):
            try:
                samples = _fetch(ctx, d / "samples.tar", work / "samples.tar", sizes.get("samples.tar"), 0.8, 0.95,
                                 "取回樣本")
            except Exception as e:
                ctx.log(f"samples copy failed: {e}")
        _copy_log(tid, d)
        prog = read_json(d / "progress.json") or {}
        if prog.get("s_per_step"):
            training._remember_speed(tr["engine"], tr["preset"]["id"], tr["gpu"], float(prog["s_per_step"]))
        m = training.install_model(tid, model, samples)
        note = "" if not ctx.params.get("partial") and samples else "樣本試念沒有完成：模型可以用，但檢查點比較不完整。"
        training._set(tid, status="done", finished_at=db.now(), note=note)
        for name in ("dataset.tar", "model.tar", "samples.tar"):  # keep the shared folder small; logs stay
            (d / name).unlink(missing_ok=True)
        return {"model_id": m["id"], "message": "Colab 訓練完成，模型已安裝，正在評分各檢查點"}
    except BaseException as e:
        if not isinstance(e, jobs.Cancelled):
            training._set(tid, status="failed", finished_at=db.now(), note=str(e)[:300])
        raise


def cancel(tr: dict) -> None:
    """Ask the runner to stop (it checks every 30 s); a run nobody has started yet simply stays unclaimed."""
    try:
        d = job_dir(tr)
        if d.exists():
            _write(d / "cancel.json", json.dumps({"at": time.time()}))
    except Exception:
        pass


def recoverable(tr: dict) -> bool:
    try:
        return (job_dir(tr) / "model.tar").exists()
    except Exception:
        return False


def estimate_units(hours: float) -> list[float]:
    return [round(hours * CU_PER_HOUR[0], 1), round(hours * CU_PER_HOUR[1], 1)]
